"""`qmath`: exact, verifiable maths tools for learners and AI agents.

    python -m quantome.mathcli eval "3/4 + 1/6"
    python -m quantome.mathcli choices --answer "comb(5,2)/comb(8,2)" --choices "A=5/14,B=3/8,C=1/4,D=5/28,E=2/7"
    python -m quantome.mathcli backsolve --var x --condition "x**2 - 5*x + 6 == 0" --choices "A=1,B=2,C=4,D=5,E=6"
    python -m quantome.mathcli ds --question "x > 0" --s1 "x**2 == 9" --s2 "x**3 == 27" --domain "x=int:-20..20"
"""

from __future__ import annotations

import argparse
import json
import sys
from fractions import Fraction

from .math import algebra, ds, numbers, search
from .math.exact import MathError, evaluate, fmt, parse, require_names


def _choices(spec: str) -> list[tuple[str, str]]:
    out = []
    for part in spec.split(","):
        label, _, expr = part.partition("=")
        if not expr:
            raise MathError(f"choices must look like A=3/4,B=2 (got {part!r})")
        out.append((label.strip(), expr.strip()))
    return out


def cmd_eval(a):
    envs = _envs(a.at) if a.at else [{}]
    tree = parse(a.expr)
    require_names(tree, set(envs[0]), "expression")
    rows = []
    for env in envs:
        v = evaluate(tree, env)
        rows.append({"at": {k: fmt(x) for k, x in env.items()} or None, "value": fmt(v), "exact": not isinstance(v, float)})
    if not a.at:
        return {"expression": a.expr, "value": rows[0]["value"], "exact": rows[0]["exact"]}
    return {"expression": a.expr, "results": rows}


def _envs(at: list[str]) -> list[dict]:
    """--at "x=3,y=5" (repeatable) → list of variable assignments for picking numbers."""
    envs = []
    for spec in at:
        env = {}
        for part in spec.split(","):
            k, _, v = part.partition("=")
            if not k.strip().isidentifier() or not v.strip():
                raise MathError(f"--at must look like x=3,y=5 (got {spec!r})")
            env[k.strip()] = Fraction(evaluate(v))
        envs.append(env)
    return envs


def _approx_eq(x, y) -> bool:
    return abs(float(x) - float(y)) <= 1e-9 * max(1.0, abs(float(x)), abs(float(y)))


def cmd_choices(a):
    opts = _choices(a.choices)
    envs = _envs(a.at) if a.at else [{}]
    names = set(envs[0]) if a.at else set()
    trees = {"answer": parse(a.answer) if a.answer else None}
    if a.mode in ("equal", "closest") and trees["answer"] is None:
        raise MathError(f"--answer is required for mode {a.mode}")
    if trees["answer"] is not None:
        require_names(trees["answer"], names, "answer")
    for label, expr in opts:
        trees[label] = parse(expr)
        require_names(trees[label], names, f"choice {label}")
    approximate = False
    per_env = []
    for env in envs:
        vals = {label: evaluate(trees[label], env) for label, _ in opts}
        truth = evaluate(trees["answer"], env) if trees["answer"] is not None else None
        approximate |= any(isinstance(v, float) for v in vals.values()) or isinstance(truth, float)
        if a.mode == "equal":
            winners = {l for l, v in vals.items()
                       if (_approx_eq(v, truth) if isinstance(v, float) or isinstance(truth, float) else v == truth)}
        elif a.mode == "closest":
            dist = {l: abs(float(v) - float(truth)) if isinstance(v, float) or isinstance(truth, float) else abs(v - truth)
                    for l, v in vals.items()}
            best = min(dist.values())
            winners = {l for l, d in dist.items() if d == best or (isinstance(d, float) and _approx_eq(d, best))}
        else:
            pick = max if a.mode == "greatest" else min
            best = pick(vals.values(), key=float)
            winners = {l for l, v in vals.items() if _approx_eq(v, best)}
        per_env.append({"at": {k: fmt(v) for k, v in env.items()} or None,
                        "answer": fmt(truth) if truth is not None else None,
                        "values": {l: fmt(v) for l, v in vals.items()}, "winners": sorted(winners)})
    winners = set.intersection(*(set(r["winners"]) for r in per_env))
    out = {"mode": a.mode, "results": per_env if a.at else None,
           "computed_answer": per_env[0]["answer"] if not a.at else None,
           "choices": None if a.at else [{"choice": l, "value": per_env[0]["values"][l], "selected": l in winners}
                                         for l, _ in opts],
           "correct_choices": sorted(winners), "exactly_one_correct": len(winners) == 1}
    out = {k: v for k, v in out.items() if v is not None}
    if approximate:
        out["note"] = "irrational values involved: comparison used a 1e-9 relative tolerance, not exact equality"
    if a.at and len(envs) < 2:
        out["note_picking"] = "picking numbers: use at least two --at assignments, with distinct non-special values"
    return out


def cmd_backsolve(a):
    cond = parse(a.condition)
    require_names(cond, {a.var}, "condition")
    rows, matches = [], []
    for label, expr in _choices(a.choices):
        tree = parse(expr)
        require_names(tree, set(), f"choice {label}")
        val = evaluate(tree)
        try:
            ok = bool(evaluate(cond, {a.var: val}))
            shown = fmt(val)
        except MathError as e:  # genuinely undefined at this value (e.g. division by zero)
            ok, shown = False, f"{fmt(val)} (undefined here: {e})"
        rows.append({"choice": label, a.var: shown, "satisfies": ok})
        if ok:
            matches.append(label)
    return {"condition": a.condition, "choices": rows, "satisfying_choices": matches,
            "exactly_one": len(matches) == 1}


def _parser():
    p = argparse.ArgumentParser(prog="qmath", description="Exact maths tools (Quantome).")
    p.add_argument("--json", action="store_true")
    s = p.add_subparsers(dest="cmd", required=True)
    x = s.add_parser("eval", help="exact evaluation: fractions, powers, sqrt, comb, perm, gcd, lcm, factorial")
    x.add_argument("expr")
    x.add_argument("--at", action="append", default=[], help='variable values, e.g. --at "x=3,y=5" (repeatable)')
    x = s.add_parser("choices", help="mark which answer choice(s) equal / are closest to the true value, or are greatest/least")
    x.add_argument("--answer", help="expression that computes the correct answer (not needed for greatest/least)")
    x.add_argument("--choices", required=True, help="A=...,B=...,C=...,D=...,E=...  (may use variables with --at)")
    x.add_argument("--mode", choices=["equal", "closest", "greatest", "least"], default="equal")
    x.add_argument("--at", action="append", default=[],
                   help='picking numbers for choices with variables, e.g. --at "x=3,y=5" --at "x=7,y=2"')
    x = s.add_parser("backsolve", help="plug each answer choice into a condition")
    x.add_argument("--var", required=True)
    x.add_argument("--condition", required=True)
    x.add_argument("--choices", required=True)
    x = s.add_parser("factor", help="prime factorisation, divisor counts")
    x.add_argument("n", type=int)
    x = s.add_parser("gcd-lcm")
    x.add_argument("nums", type=int, nargs="+")
    x = s.add_parser("factorial-power", help="exponent of prime p in n! (Legendre)")
    x.add_argument("n", type=int)
    x.add_argument("p", type=int)
    x = s.add_parser("trailing-zeros", help="trailing zeros of n!")
    x.add_argument("n", type=int)
    x = s.add_parser("units-digit", help="units digit of base^exp via cyclicity")
    x.add_argument("base", type=int)
    x.add_argument("exp", type=int)
    x = s.add_parser("powmod", help="remainder of base^exp divided by mod")
    x.add_argument("base", type=int)
    x.add_argument("exp", type=int)
    x.add_argument("mod", type=int)
    x = s.add_parser("linsolve", help="exact linear system; classifies unique/none/infinite")
    x.add_argument("equations", nargs="+")
    x = s.add_parser("combo", help="is a linear combination (e.g. 'x + y') determined by the equations?")
    x.add_argument("--target", required=True)
    x.add_argument("equations", nargs="+")
    x = s.add_parser("quadratic", help="ax²+bx+c=0: discriminant, exact roots, Vieta sums/products")
    for k in "abc":
        x.add_argument(k)
    x = s.add_parser("arith", help="arithmetic sequence: nth term, sum, first terms (give --n or --last)")
    x.add_argument("--first", required=True)
    x.add_argument("--diff", required=True)
    x.add_argument("--n", type=int)
    x.add_argument("--last", help="last term instead of --n (counts the terms)")
    x = s.add_parser("geom", help="geometric sequence nth term and sum")
    x.add_argument("--first", required=True)
    x.add_argument("--ratio", required=True)
    x.add_argument("--n", type=int, required=True)
    x = s.add_parser("recur", help="recursive sequence terms; rule uses prev, prev2, n")
    x.add_argument("--init", required=True, help="initial term(s), comma-separated, e.g. 1,1")
    x.add_argument("--rule", required=True, help='e.g. "prev + prev2" or "2*prev - n"')
    x.add_argument("--n", type=int, required=True)
    x = s.add_parser("count", help="comb / perm / circular / multiset arrangements")
    x.add_argument("kind", choices=["comb", "perm", "circular", "multiset"])
    x.add_argument("--n", type=int)
    x.add_argument("--k", type=int)
    x.add_argument("--word")
    x = s.add_parser("stats", help="mean, median, mode, range, SD (exact)")
    x.add_argument("values", nargs="+")
    x = s.add_parser("ds", help="Data Sufficiency counterexample search")
    x.add_argument("--question", required=True, help="value expression, or a yes/no condition")
    x.add_argument("--s1", required=True)
    x.add_argument("--s2", required=True)
    x.add_argument("--domain", action="append", required=True, help="e.g. x=int:-20..20 (repeatable)")
    x.add_argument("--given", action="append", default=[], help="constraint from the question stem (repeatable)")
    x.add_argument("--define", action="append", default=[], help='derived variable, e.g. "S = k*a + k*(k-1)/2"')
    x = s.add_parser("must", help="which choices MUST / COULD / CANNOT be true over a domain (I/II/III questions)")
    x.add_argument("--domain", action="append", required=True)
    x.add_argument("--given", action="append", default=[], help="stem conditions (repeatable)")
    x.add_argument("--choices", required=True, help='conditions, e.g. "A=is_even(x*y),B=x+y>0"')
    x = s.add_parser("find", help="all solutions of a condition over a domain, with count and sum")
    x.add_argument("--domain", action="append", required=True)
    x.add_argument("--condition", required=True)
    x.add_argument("--value", help="expression to collect (default: the single variable)")
    x = s.add_parser("valuation", help="exponent of prime p in a positive integer expression")
    x.add_argument("expr")
    x.add_argument("p", type=int)
    x = s.add_parser("decimal", help="decimal expansion of num/den: terminating?, repeating block, nth digit")
    x.add_argument("num", type=int)
    x.add_argument("den", type=int)
    x.add_argument("--digit", type=int, help="position after the decimal point")
    return p


def run(a) -> dict:
    match a.cmd:
        case "eval": return cmd_eval(a)
        case "choices": return cmd_choices(a)
        case "backsolve": return cmd_backsolve(a)
        case "factor": return numbers.factor_report(a.n)
        case "gcd-lcm": return numbers.gcd_lcm(a.nums)
        case "factorial-power": return numbers.legendre(a.n, a.p)
        case "trailing-zeros": return numbers.trailing_zeros(a.n)
        case "units-digit": return numbers.units_digit_power(a.base, a.exp)
        case "powmod": return numbers.powmod(a.base, a.exp, a.mod)
        case "linsolve": return algebra.solve_linear(a.equations)
        case "combo": return algebra.combination_determined(a.equations, a.target)
        case "quadratic": return algebra.quadratic(a.a, a.b, a.c)
        case "arith": return algebra.arithmetic_sequence(a.first, a.diff, a.n, a.last)
        case "recur": return algebra.recurrence(a.init.split(","), a.rule, a.n)
        case "geom": return algebra.geometric_sequence(a.first, a.ratio, a.n)
        case "count": return algebra.count(a.kind, a.n, a.k, a.word)
        case "stats": return algebra.describe(a.values)
        case "ds": return ds.test(a.question, {"1": a.s1, "2": a.s2}, a.domain, a.given, defines=a.define)
        case "must": return search.must_could(a.domain, _choices(a.choices), a.given)
        case "find": return search.find_all(a.domain, a.condition, a.value)
        case "valuation": return numbers.valuation(evaluate(a.expr), a.p)
        case "decimal": return numbers.decimal_expansion(a.num, a.den, a.digit)


def _render(d, indent=0) -> str:
    pad = "  " * indent
    lines = []
    for k, v in d.items():
        if isinstance(v, dict):
            lines.append(f"{pad}{k}:")
            lines.append(_render(v, indent + 1))
        elif isinstance(v, list) and v and isinstance(v[0], dict):
            lines.append(f"{pad}{k}:")
            for item in v:
                lines.append(f"{pad}  - " + ", ".join(f"{ik}: {iv}" for ik, iv in item.items()))
        else:
            lines.append(f"{pad}{k}: {v}")
    return "\n".join(lines)


def main(argv=None) -> int:
    a = _parser().parse_args(argv)
    try:
        out = run(a)
    except (MathError, ValueError, ZeroDivisionError) as e:
        print(json.dumps({"error": str(e)}) if a.json else f"ERROR: {e}")
        return 2
    print(json.dumps(out, indent=2, ensure_ascii=False, default=str) if a.json else _render(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
