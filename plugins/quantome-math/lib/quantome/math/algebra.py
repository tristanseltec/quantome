"""Exact algebra: linear systems, quadratics, sequences, counting and descriptive statistics."""

from __future__ import annotations

import math
import re
from collections import Counter
from fractions import Fraction

from .exact import MathError, evaluate, exact_sqrt, fmt, parse


# ---------- linear systems (exact Gauss–Jordan elimination) ----------

_IMPLICIT = [(re.compile(r"(\d)\s*([A-Za-z(])"), r"\1*\2"), (re.compile(r"\)\s*([A-Za-z0-9(])"), r")*\1")]


def _variables(tree) -> list[str]:
    import ast
    from .exact import FUNCTIONS
    return sorted({n.id for n in ast.walk(tree) if isinstance(n, ast.Name) and n.id not in FUNCTIONS and n.id != "pi"})


def _parse_linear(eq: str) -> tuple[dict[str, Fraction], Fraction]:
    """'3x + 2y = 17', 'x/2 + y = 4', '3(x + 2) = y' → ({var: coefficient}, constant on the right).

    Coefficients are measured with the exact evaluator, then linearity is verified at test points.
    """
    if eq.count("=") != 1 or "==" in eq:
        raise MathError(f"need exactly one '=' in {eq!r}")
    lhs, rhs = eq.split("=")
    expr = f"({lhs}) - ({rhs})"
    for pat, rep in _IMPLICIT:
        expr = pat.sub(rep, expr)
    tree = parse(expr)
    names = _variables(tree)
    if not names:
        raise MathError(f"no variables in {eq!r}")
    zero = {v: Fraction(0) for v in names}
    c0 = Fraction(evaluate(tree, zero))
    coef = {v: Fraction(evaluate(tree, {**zero, v: Fraction(1)})) - c0 for v in names}
    for point in ([Fraction(i + 2) for i in range(len(names))], [Fraction(-3 * i - 5, 2) for i in range(len(names))]):
        env = dict(zip(names, point))
        if Fraction(evaluate(tree, env)) != c0 + sum(coef[v] * env[v] for v in names):
            raise MathError(f"not a linear equation: {eq!r}")
    return {v: c for v, c in coef.items() if c != 0}, -c0


def solve_linear(equations: list[str]) -> dict:
    """Solve a linear system exactly; classify it as unique / none / infinitely many."""
    rows = [_parse_linear(e) for e in equations]
    names = sorted({v for c, _ in rows for v in c})
    m = [[c.get(v, Fraction(0)) for v in names] + [k] for c, k in rows]
    r, pivots = 0, []
    for col in range(len(names)):
        piv = next((i for i in range(r, len(m)) if m[i][col] != 0), None)
        if piv is None:
            continue
        m[r], m[piv] = m[piv], m[r]
        m[r] = [x / m[r][col] for x in m[r]]
        for i in range(len(m)):
            if i != r and m[i][col] != 0:
                f = m[i][col]
                m[i] = [a - f * b for a, b in zip(m[i], m[r])]
        pivots.append(col)
        r += 1
    if any(all(x == 0 for x in row[:-1]) and row[-1] != 0 for row in m):
        return {"variables": names, "status": "no solution (inconsistent: e.g. parallel lines)"}
    free = [names[c] for c in range(len(names)) if c not in pivots]
    if free:
        determined = {}
        for i, col in enumerate(pivots):
            if all(m[i][names.index(f)] == 0 for f in free):
                determined[names[col]] = fmt(m[i][-1])
        return {"variables": names, "status": f"infinitely many solutions (free: {', '.join(free)})",
                "rank": len(pivots), "still_determined": determined or "no single variable is determined",
                "hint": "A combination (e.g. x + y) may still be determined: test it with `combo`."}
    return {"variables": names, "status": "unique solution",
            "solution": {names[c]: fmt(m[i][-1]) for i, c in enumerate(pivots)}}


def combination_determined(equations: list[str], target: str) -> dict:
    """Is a linear combination like '2x + 3y' fixed by the equations? (DS-style.)"""
    rows = [_parse_linear(e) for e in equations]
    tcoef, tconst = _parse_linear(f"{target} = 0")
    names = sorted({v for c, _ in rows for v in c} | set(tcoef))
    A = [[c.get(v, Fraction(0)) for v in names] for c, _ in rows]
    b = [k for _, k in rows]
    t = [tcoef.get(v, Fraction(0)) for v in names]
    base = solve_linear(equations)
    if base["status"].startswith("no solution"):
        return {"target": target, "determined": False, "reason": "system is inconsistent"}
    # target is determined iff t lies in the row space of A: rank(A) == rank([A; t])
    if _rank(A) == _rank(A + [t]):
        # find the value: solve for a particular solution with free vars = 0
        sol = _particular(A, b, names)
        val = sum(tc * sol[v] for tc, v in zip(t, names)) - tconst
        return {"target": target, "determined": True, "value": fmt(val)}
    return {"target": target, "determined": False,
            "reason": "target is not a combination of the given equations (rank test)"}


def _rank(M: list[list[Fraction]]) -> int:
    M = [row[:] for row in M]
    rank, cols = 0, len(M[0]) if M else 0
    for col in range(cols):
        piv = next((i for i in range(rank, len(M)) if M[i][col] != 0), None)
        if piv is None:
            continue
        M[rank], M[piv] = M[piv], M[rank]
        for i in range(len(M)):
            if i != rank and M[i][col] != 0:
                f = M[i][col] / M[rank][col]
                M[i] = [a - f * b for a, b in zip(M[i], M[rank])]
        rank += 1
    return rank


def _particular(A, b, names):
    m = [row[:] + [k] for row, k in zip(A, b)]
    sol = {v: Fraction(0) for v in names}
    r = 0
    piv_cols = []
    for col in range(len(names)):
        piv = next((i for i in range(r, len(m)) if m[i][col] != 0), None)
        if piv is None:
            continue
        m[r], m[piv] = m[piv], m[r]
        m[r] = [x / m[r][col] for x in m[r]]
        for i in range(len(m)):
            if i != r and m[i][col] != 0:
                f = m[i][col]
                m[i] = [a - f * c for a, c in zip(m[i], m[r])]
        piv_cols.append(col)
        r += 1
    for i, col in enumerate(piv_cols):
        sol[names[col]] = m[i][-1]
    return sol


# ---------- quadratics ----------

def _poly_str(A: Fraction, B: Fraction, C: Fraction) -> str:
    parts = []
    for coef, var in ((A, "x²"), (B, "x"), (C, "")):
        if coef == 0:
            continue
        mag = abs(coef)
        body = (var if mag == 1 and var else f"{_plain(mag)}{var}")
        sign = "-" if coef < 0 else "+"
        parts.append(("-" + body) if not parts and sign == "-" else body if not parts else f"{sign} {body}")
    return " ".join(parts) + " = 0"


def _plain(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def quadratic(a: str, b: str, c: str) -> dict:
    A, B, C = (Fraction(evaluate(x)) for x in (a, b, c))
    if A == 0:
        raise MathError("a must be non-zero")
    D = B * B - 4 * A * C
    out = {"equation": _poly_str(A, B, C), "discriminant": fmt(D),
           "sum_of_roots (−b/a)": fmt(-B / A), "product_of_roots (c/a)": fmt(C / A)}
    if D < 0:
        out["roots"] = "no real roots (discriminant < 0)"
        return out
    s = exact_sqrt(D)
    if isinstance(s, Fraction):
        roots = sorted({(-B - s) / (2 * A), (-B + s) / (2 * A)})
        out["roots"] = [fmt(r) for r in roots]
    else:
        # scale to integers: roots = (p ± k√r) / q, then reduce by gcd(p, k, q)
        L = math.lcm(A.denominator, B.denominator, C.denominator)
        a_i, b_i, c_i = int(A * L), int(B * L), int(C * L)
        k, r = _simplify_surd(Fraction(b_i * b_i - 4 * a_i * c_i))
        k = int(k)
        p_, q_ = -b_i, 2 * a_i
        g = math.gcd(math.gcd(p_, k), q_)
        p_, k, q_ = p_ // g, k // g, q_ // g
        if q_ < 0:
            p_, q_ = -p_, -q_
        surd = f"{k}√{r}" if k != 1 else f"√{r}"
        head = f"{p_} ± {surd}" if p_ else f"± {surd}"
        exact = head if q_ == 1 else f"({head}) / {q_}"
        approx = sorted({(-float(B) - math.sqrt(D)) / (2 * float(A)), (-float(B) + math.sqrt(D)) / (2 * float(A))})
        out["roots"] = f"{exact} ≈ " + ", ".join(f"{x:.6g}" for x in approx)
    out["repeated_root"] = D == 0
    return out


def _simplify_surd(D: Fraction) -> tuple[Fraction, int]:
    """√(p/q) = (1/q)·√(p·q) → k·√rest with rest square-free (integers)."""
    n = D.numerator * D.denominator
    k, rest = 1, n
    f = 2
    while f * f <= rest:
        while rest % (f * f) == 0:
            rest //= f * f
            k *= f
        f += 1
    return Fraction(k, D.denominator), rest


# ---------- sequences ----------

def arithmetic_sequence(first: str, diff: str, n: int) -> dict:
    a, d = Fraction(evaluate(first)), Fraction(evaluate(diff))
    last = a + (n - 1) * d
    return {"a1": fmt(a), "d": fmt(d), "n": n, "nth_term": fmt(last),
            "sum": fmt(n * (a + last) / 2), "working": f"a_n = a1 + (n−1)d; S_n = n × (a1 + a_n)/2"}


def geometric_sequence(first: str, ratio: str, n: int) -> dict:
    a, r = Fraction(evaluate(first)), Fraction(evaluate(ratio))
    nth = a * r ** (n - 1)
    s = a * n if r == 1 else a * (1 - r**n) / (1 - r)
    return {"a1": fmt(a), "r": fmt(r), "n": n, "nth_term": fmt(nth), "sum": fmt(s),
            "working": "a_n = a1·r^(n−1); S_n = a1(1 − r^n)/(1 − r)"}


# ---------- counting ----------

def count(kind: str, n: int | None = None, k: int | None = None, word: str | None = None) -> dict:
    match kind:
        case "comb":
            return {"C(n,k)": math.comb(n, k), "formula": f"{n}! / ({k}! × {n - k}!)"}
        case "perm":
            return {"P(n,k)": math.perm(n, k), "formula": f"{n}! / {n - k}!"}
        case "circular":
            return {"arrangements": math.factorial(n - 1), "formula": f"({n}−1)!",
                    "note": "halve it if clockwise and anticlockwise count as the same (necklace)"}
        case "multiset":
            if not word:
                raise MathError("give --word (e.g. MISSISSIPPI)")
            c = Counter(word.replace(" ", ""))
            total = math.factorial(sum(c.values()))
            for v in c.values():
                total //= math.factorial(v)
            return {"word": word, "letter_counts": dict(c), "arrangements": total,
                    "formula": f"{sum(c.values())}! / (" + " × ".join(f"{v}!" for v in c.values() if v > 1) + ")"}
    raise MathError("kind must be comb, perm, circular or multiset")


# ---------- descriptive statistics ----------

def describe(values: list[str]) -> dict:
    xs = [Fraction(evaluate(v)) for v in values]
    if not xs:
        raise MathError("no values")
    n = len(xs)
    s = sorted(xs)
    mean = sum(xs) / n
    median = s[n // 2] if n % 2 else (s[n // 2 - 1] + s[n // 2]) / 2
    c = Counter(xs)
    top = max(c.values())
    var_p = sum((x - mean) ** 2 for x in xs) / n
    out = {"n": n, "sorted": [fmt(x) for x in s], "sum": fmt(sum(xs)), "mean": fmt(mean), "median": fmt(median),
           "mode": [fmt(x) for x in sorted(k for k, v in c.items() if v == top)] if top > 1 else "none",
           "range": fmt(s[-1] - s[0]), "population_variance": fmt(var_p),
           "population_sd": fmt(exact_sqrt(var_p))}
    if n > 1:
        var_s = sum((x - mean) ** 2 for x in xs) / (n - 1)
        out["sample_sd"] = fmt(exact_sqrt(var_s))
    return out


__all__ = ["solve_linear", "combination_determined", "quadratic", "arithmetic_sequence",
           "geometric_sequence", "count", "describe", "parse"]
