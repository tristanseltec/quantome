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

from .math import algebra, ds, numbers
from .math.exact import MathError, evaluate, fmt


def _choices(spec: str) -> list[tuple[str, str]]:
    out = []
    for part in spec.split(","):
        label, _, expr = part.partition("=")
        if not expr:
            raise MathError(f"choices must look like A=3/4,B=2 (got {part!r})")
        out.append((label.strip(), expr.strip()))
    return out


def cmd_eval(a):
    v = evaluate(a.expr)
    return {"expression": a.expr, "value": fmt(v), "exact": not isinstance(v, float)}


def cmd_choices(a):
    truth = evaluate(a.answer)
    rows, matches = [], []
    for label, expr in _choices(a.choices):
        val = evaluate(expr)
        eq = (abs(float(val) - float(truth)) < 1e-9) if isinstance(val, float) or isinstance(truth, float) else val == truth
        rows.append({"choice": label, "value": fmt(val), "correct": eq})
        if eq:
            matches.append(label)
    return {"computed_answer": fmt(truth), "choices": rows, "correct_choices": matches,
            "exactly_one_correct": len(matches) == 1}


def cmd_backsolve(a):
    rows, matches = [], []
    for label, expr in _choices(a.choices):
        val = evaluate(expr)
        try:
            ok = bool(evaluate(a.condition, {a.var: val}))
        except MathError as e:
            ok, val = False, f"{fmt(val)} (undefined: {e})"
        rows.append({"choice": label, a.var: fmt(val) if not isinstance(val, str) else val, "satisfies": ok})
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
    x = s.add_parser("choices", help="compute the true answer and mark which answer choice(s) equal it")
    x.add_argument("--answer", required=True, help="expression that computes the correct answer")
    x.add_argument("--choices", required=True, help="A=...,B=...,C=...,D=...,E=...")
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
    x = s.add_parser("arith", help="arithmetic sequence nth term and sum")
    x.add_argument("--first", required=True)
    x.add_argument("--diff", required=True)
    x.add_argument("--n", type=int, required=True)
    x = s.add_parser("geom", help="geometric sequence nth term and sum")
    x.add_argument("--first", required=True)
    x.add_argument("--ratio", required=True)
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
        case "arith": return algebra.arithmetic_sequence(a.first, a.diff, a.n)
        case "geom": return algebra.geometric_sequence(a.first, a.ratio, a.n)
        case "count": return algebra.count(a.kind, a.n, a.k, a.word)
        case "stats": return algebra.describe(a.values)
        case "ds": return ds.test(a.question, {"1": a.s1, "2": a.s2}, a.domain, a.given)


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
