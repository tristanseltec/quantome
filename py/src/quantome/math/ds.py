"""Data Sufficiency tester: brute-force search for counterexamples.

A counterexample (two admissible assignments that give different answers to the question) PROVES that a
statement is insufficient. Finding no counterexample in the searched domain is only EVIDENCE of sufficiency,
which must be confirmed algebraically, especially when the true domain is larger than the one searched.

Domains: ``x=int:-20..20``, ``n=posint:1..60``, ``x=grid:-5..5/4`` (multiples of 1/4), or ``p=set:2,3,5,7``.
"""

from __future__ import annotations

import itertools
from fractions import Fraction

from .exact import MathError, evaluate, fmt, parse

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
         constraints: list[str] | None = None, max_examples: int = 3) -> dict:
    """Evaluate sufficiency of (1), (2) and (1)+(2) for a value or yes/no question."""
    doms = [parse_domain(d) for d in domains]
    names = [n for n, _ in doms]
    size = 1
    for _, vals in doms:
        size *= len(vals)
    if size > MAX_POINTS:
        raise MathError(f"search space {size:,} points > {MAX_POINTS:,}; narrow the domains")
    q = parse(question)
    stmts = {k: parse(v) for k, v in statements.items()}
    cons = [parse(c) for c in (constraints or [])]

    answers: dict[str, dict] = {"1": {}, "2": {}, "1+2": {}}
    admissible = 0
    for combo in itertools.product(*(v for _, v in doms)):
        env = dict(zip(names, combo))
        try:
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

    if suff("1") and suff("2"):
        letter = "D"
    elif suff("1"):
        letter = "A"
    elif suff("2"):
        letter = "B"
    elif suff("1+2"):
        letter = "C"
    else:
        letter = "E"
    return {
        "question": question, "statements": statements, "domains": domains, "constraints": constraints or [],
        "points_searched": size, "admissible_points": admissible,
        "verdicts": verdict, "suggested_answer": letter,
        "caveat": ("INSUFFICIENT verdicts are proved by the counterexamples shown. SUFFICIENT? verdicts only mean no "
                   "counterexample exists in the searched domain: confirm them algebraically, and widen the domain "
                   "(negatives, fractions, larger values) whenever the question allows it."),
    }
