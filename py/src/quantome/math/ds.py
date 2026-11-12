"""Data Sufficiency tester: brute-force search for counterexamples.

A counterexample (two admissible assignments that give different answers to the question) PROVES that a
statement is insufficient. Finding no counterexample in the searched domain is only EVIDENCE of sufficiency,
which must be confirmed algebraically, especially when the true domain is larger than the one searched.

Domains: ``x=int:-20..20``, ``n=posint:1..60``, ``x=grid:-5..5/4`` (multiples of 1/4), or ``p=set:2,3,5,7``.
"""

from __future__ import annotations

import itertools
from fractions import Fraction

from .exact import MathError, evaluate, fmt, parse, require_names

MAX_POINTS = 2_000_000


def parse_domain(spec: str) -> tuple[str, list[Fraction]]:
    try:
        name, rest = spec.split("=", 1)
        kind, rng = rest.split(":", 1)
    except ValueError:
        raise MathError(f"bad domain {spec!r}; use e.g. x=int:-20..20") from None
    name, kind = name.strip(), kind.strip()
    if kind == "set":
        vals = [Fraction(evaluate(v)) for v in rng.split(",")]
    else:
        step = Fraction(1)
        if "/" in rng and kind == "grid":
            rng, den = rng.rsplit("/", 1)
            step = Fraction(1, int(den))
        lo_s, hi_s = rng.split("..")
        lo, hi = Fraction(evaluate(lo_s)), Fraction(evaluate(hi_s))
        if kind == "posint":
            lo = max(lo, Fraction(1))
        elif kind not in ("int", "grid"):
            raise MathError(f"unknown domain kind {kind!r} (int, posint, grid, set)")
        vals, v = [], lo
        while v <= hi:
            vals.append(v)
            v += step
    if not vals:
        raise MathError(f"empty domain {spec!r}")
    return name, vals


def test(question: str, statements: dict[str, str], domains: list[str],
         constraints: list[str] | None = None, max_examples: int = 3,
         defines: list[str] | None = None) -> dict:
    """Evaluate sufficiency of (1), (2) and (1)+(2) for a value or yes/no question.

    ``defines`` are derived variables, e.g. ``"S = k*a + k*(k-1)/2"``, computed in order for every assignment.
    Every name used anywhere must be a domain variable or a define: anything else raises MathError.
    """
    doms = [parse_domain(d) for d in domains]
    names = [n for n, _ in doms]
    if len(set(names)) != len(names):
        raise MathError("a variable has two domains")
    known = set(names)
    derived = []
    for d in defines or []:
        if "=" not in d:
            raise MathError(f"define must look like 'S = expression', got {d!r}")
        dname, dexpr = (t.strip() for t in d.split("=", 1))
        if not dname.isidentifier() or dname in known:
            raise MathError(f"bad or duplicate define name {dname!r}")
        tree = parse(dexpr)
        require_names(tree, known, f"define {dname}")
        derived.append((dname, tree))
        known.add(dname)
    size = 1
    for _, vals in doms:
        size *= len(vals)
    if size > MAX_POINTS:
        raise MathError(f"search space {size:,} points > {MAX_POINTS:,}; narrow the domains")
    q = parse(question)
    require_names(q, known, "question")
    stmts = {k: parse(v) for k, v in statements.items()}
    for k, t in stmts.items():
        require_names(t, known, f"statement ({k})")
    cons = [parse(c) for c in (constraints or [])]
    for c in cons:
        require_names(c, known, "given")

    answers: dict[str, dict] = {"1": {}, "2": {}, "1+2": {}}
    admissible = 0
    for combo in itertools.product(*(v for _, v in doms)):
        env = dict(zip(names, combo))
        try:
            for dname, tree in derived:
                env[dname] = evaluate(tree, env)
            if not all(evaluate(c, env) for c in cons):
                continue
            ok1 = bool(evaluate(stmts["1"], env))
            ok2 = bool(evaluate(stmts["2"], env))
            ans = evaluate(q, env)
        except MathError:
            continue  # undefined here (e.g. division by zero): not an admissible case
        admissible += 1
        key = ans if not isinstance(ans, float) else round(ans, 9)
        for label, ok in (("1", ok1), ("2", ok2), ("1+2", ok1 and ok2)):
            if ok:
                bucket = answers[label]
                if key not in bucket and len(bucket) < 50:
                    bucket[key] = env
    if admissible == 0:
        raise MathError("no admissible assignment at all: the stem constraints contradict the domains "
                        "(or every case is undefined). Check --given and --domain.")
    verdict = {}
    for label, bucket in answers.items():
        if not bucket:
            verdict[label] = {"status": "no admissible case found (statement contradicts the domain?)"}
        elif len(bucket) == 1:
            (val, ex), = bucket.items()
            verdict[label] = {"status": "SUFFICIENT? (no counterexample found)", "answer": fmt(val),
                              "example": {k: fmt(v) for k, v in ex.items()}}
        else:
            exs = list(bucket.items())[:max_examples]
            verdict[label] = {"status": "INSUFFICIENT (proved by counterexample)",
                              "different_answers": [{"answer": fmt(v), "when": {k: fmt(x) for k, x in e.items()}}
                                                    for v, e in exs]}

    def suff(lbl):
        return verdict[lbl]["status"].startswith("SUFFICIENT")

    warnings = []
    for lbl in ("1", "2"):
        if verdict[lbl]["status"].startswith("no admissible"):
            warnings.append(f"Statement ({lbl}) is never true in the searched domain: real DS statements are "
                            "always possible, so check the statement and the domain.")
    if verdict["1+2"]["status"].startswith("no admissible") and not warnings:
        warnings.append("Statements (1) and (2) are never true together: GMAT statements never contradict each "
                        "other, so the question or the domain is wrong.")
    if any(":grid:" in d.replace(" ", "") or "=grid:" in d.replace(" ", "") for d in domains):
        warnings.append("Grid domains only test multiples of the step: a threshold between grid points can hide a "
                        "counterexample. Re-run with a finer step near any boundary in the statements.")
    if warnings and any(w.startswith("Statement") for w in warnings):
        letter = "undetermined (see warnings)"
    elif suff("1") and suff("2"):
        letter = "D"
    elif suff("1"):
        letter = "A"
    elif suff("2"):
        letter = "B"
    elif suff("1+2"):
        letter = "C"
    else:
        letter = "E"
    if verdict["1+2"]["status"].startswith("no admissible"):
        letter = "undetermined (see warnings)"
    return {
        "question": question, "statements": statements, "domains": domains, "constraints": constraints or [],
        "points_searched": size, "admissible_points": admissible,
        "verdicts": verdict, "suggested_answer": letter, "warnings": warnings,
        "caveat": ("INSUFFICIENT verdicts are proved by the counterexamples shown. SUFFICIENT? verdicts only mean no "
                   "counterexample exists in the searched domain: confirm them algebraically, and widen the domain "
                   "(negatives, fractions, larger values) whenever the question allows it."),
    }
