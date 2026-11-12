"""Exhaustive search tools: 'must / could / cannot be true' and 'find all solutions'."""

from __future__ import annotations

import itertools
from fractions import Fraction

from .ds import MAX_POINTS, parse_domain
from .exact import MathError, evaluate, fmt, parse, require_names


def _space(domains: list[str]):
    doms = [parse_domain(d) for d in domains]
    names = [n for n, _ in doms]
    size = 1
    for _, v in doms:
        size *= len(v)
    if size > MAX_POINTS:
        raise MathError(f"search space {size:,} points > {MAX_POINTS:,}; narrow the domains")
    return names, doms, size


def must_could(domains: list[str], choices: list[tuple[str, str]], given: list[str] | None = None) -> dict:
    """For each choice (a condition), decide whether it MUST, COULD or CANNOT be true given the stem."""
    names, doms, size = _space(domains)
    cons = [parse(g) for g in (given or [])]
    for c in cons:
        require_names(c, set(names), "given")
    trees = []
    for label, expr in choices:
        t = parse(expr)
        require_names(t, set(names), f"choice {label}")
        trees.append((label, expr, t))
    stats = {label: {"true": 0, "false": 0, "true_example": None, "false_example": None} for label, _, _ in trees}
    admissible = 0
    for combo in itertools.product(*(v for _, v in doms)):
        env = dict(zip(names, combo))
        try:
            if not all(evaluate(c, env) for c in cons):
                continue
        except MathError:
            continue
        admissible += 1
        for label, _, t in trees:
            try:
                ok = bool(evaluate(t, env))
            except MathError:
                continue
            st = stats[label]
            key = "true" if ok else "false"
            st[key] += 1
            if st[f"{key}_example"] is None:
                st[f"{key}_example"] = {k: fmt(v) for k, v in env.items()}
    if admissible == 0:
        raise MathError("no value satisfies the stem conditions in the searched domain")
    rows = []
    for label, expr, _ in trees:
        st = stats[label]
        verdict = ("MUST be true (no counterexample found)" if st["false"] == 0 else
                   "CANNOT be true (never true in the domain)" if st["true"] == 0 else
                   "COULD be true (but need not be)")
        row = {"choice": label, "condition": expr, "verdict": verdict}
        if st["false_example"] and st["true"]:
            row["counterexample"] = st["false_example"]
        if st["true_example"] and st["false"]:
            row["example_true"] = st["true_example"]
        rows.append(row)
    return {"domains": domains, "given": given or [], "admissible_points": admissible, "points_searched": size,
            "choices": rows,
            "must_be_true": [r["choice"] for r in rows if r["verdict"].startswith("MUST")],
            "cannot_be_true": [r["choice"] for r in rows if r["verdict"].startswith("CANNOT")],
            "caveat": "COULD/CANNOT are proved by the examples; MUST is evidence only. Confirm it algebraically, "
                      "and include negatives, zero and fractions in the domain when the stem allows them."}


def find_all(domains: list[str], condition: str, value: str | None = None, limit: int = 200) -> dict:
    """List every assignment satisfying a condition (e.g. an equation or inequality), with count and sum."""
    names, doms, size = _space(domains)
    cond = parse(condition)
    require_names(cond, set(names), "condition")
    val = parse(value) if value else None
    if val is not None:
        require_names(val, set(names), "value")
    sols, values = [], []
    for combo in itertools.product(*(v for _, v in doms)):
        env = dict(zip(names, combo))
        try:
            if not evaluate(cond, env):
                continue
            v = evaluate(val, env) if val is not None else (combo[0] if len(combo) == 1 else None)
        except MathError:
            continue
        if len(sols) < limit:
            sols.append({k: fmt(x) for k, x in env.items()})
        if v is not None:
            values.append(v)
    out = {"condition": condition, "domains": domains, "count": len(values) if values else len(sols),
           "solutions": sols if len(sols) < limit else sols + ["… (truncated)"]}
    if values and all(not isinstance(v, float) for v in values):
        distinct = sorted(set(values))
        out["distinct_values"] = [fmt(v) for v in distinct[:50]]
        out["sum_of_distinct_values"] = fmt(sum(distinct, Fraction(0)))
        out["min"], out["max"] = fmt(distinct[0]), fmt(distinct[-1])
    out["caveat"] = ("Only values in the searched domain are listed. Solutions between grid points or outside "
                     "the range are missed, so widen or refine the domain if the answer depends on it.")
    return out
