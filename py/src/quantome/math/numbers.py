"""Number theory for GMAT-level questions: factorisation, divisors, gcd/lcm, factorial powers, cyclicity."""

from __future__ import annotations

import math


def factorize(n: int) -> dict[int, int]:
    """Prime factorisation of n ≥ 2 as {prime: exponent}."""
    if not isinstance(n, int) or n < 2:
        raise ValueError("factorize needs an integer n ≥ 2")
    if n > 10**15:
        raise ValueError("n too large for trial division (limit 10^15)")
    out: dict[int, int] = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def factor_report(n: int) -> dict:
    f = factorize(n)
    count = math.prod(e + 1 for e in f.values())
    total = math.prod((p ** (e + 1) - 1) // (p - 1) for p, e in f.items())
    odd = math.prod(e + 1 for p, e in f.items() if p != 2)
    divisors = sorted(_divisors(f)) if count <= 200 else None
    return {
        "n": n,
        "factorization": " × ".join(f"{p}^{e}" if e > 1 else str(p) for p, e in f.items()),
        "number_of_divisors": count,
        "formula": " × ".join(f"({e}+1)" for e in f.values()) + f" = {count}",
        "sum_of_divisors": total,
        "odd_divisors": odd,
        "even_divisors": count - odd,
        "is_perfect_square": all(e % 2 == 0 for e in f.values()),
        "divisors": divisors,
    }


def _divisors(f: dict[int, int]) -> list[int]:
    ds = [1]
    for p, e in f.items():
        ds = [d * p**k for d in ds for k in range(e + 1)]
    return ds


def legendre(n: int, p: int) -> dict:
    """Exponent of prime p in n! = Σ floor(n / p^k)."""
    if n < 0 or not _is_prime(p):
        raise ValueError("need n ≥ 0 and p prime")
    terms, pk = [], p
    while pk <= n:
        terms.append(n // pk)
        pk *= p
    return {"n": n, "p": p, "exponent": sum(terms),
            "working": " + ".join(f"⌊{n}/{p}^{i + 1}⌋={t}" for i, t in enumerate(terms)) or "0"}


def trailing_zeros(n: int) -> dict:
    r = legendre(n, 5)
    return {"n": n, "trailing_zeros_of_factorial": r["exponent"], "working": r["working"]}


def units_digit_power(base: int, exp: int) -> dict:
    """Units digit of base^exp via the cycle of units digits."""
    if exp < 1:
        raise ValueError("exponent must be ≥ 1")
    u = abs(base) % 10
    cycle, x = [], u
    while x not in cycle:
        cycle.append(x)
        x = (x * u) % 10
    start = cycle.index(x)  # cycle may have a pre-period (e.g. never here for units digits, but safe)
    period = len(cycle) - start
    idx = exp - 1 if exp - 1 < start else start + (exp - 1 - start) % period
    digit = cycle[idx]
    if base < 0 and exp % 2 == 1 and digit:
        note = "negative base with odd exponent: the result is negative; its last digit is still shown"
    else:
        note = ""
    return {"base": base, "exp": exp, "cycle": cycle[start:], "period": period, "units_digit": digit,
            "check": pow(abs(base), exp, 10) == digit, "note": note}


def powmod(base: int, exp: int, mod: int) -> dict:
    if mod < 1 or exp < 0:
        raise ValueError("need mod ≥ 1 and exp ≥ 0")
    return {"base": base, "exp": exp, "mod": mod, "remainder": pow(base, exp, mod)}


def gcd_lcm(nums: list[int]) -> dict:
    if len(nums) < 2 or any(n <= 0 for n in nums):
        raise ValueError("give at least two positive integers")
    return {"numbers": nums, "gcd": math.gcd(*nums), "lcm": math.lcm(*nums),
            "factorizations": {n: (" × ".join(f"{p}^{e}" for p, e in factorize(n).items()) if n > 1 else "1")
                               for n in nums}}


def _is_prime(n: int) -> bool:
    return n >= 2 and all(n % d for d in range(2, math.isqrt(n) + 1))
