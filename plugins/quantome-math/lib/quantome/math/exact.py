"""A safe, exact expression evaluator.

Expressions are parsed with :mod:`ast` and evaluated against an allow-list. Python's ``eval`` is never used.
Rational arithmetic is exact (:class:`fractions.Fraction`). Irrational results (non-perfect-square roots,
fractional powers) fall back to ``float`` and are reported as approximate.

    >>> evaluate("3/4 + 1/6")
    Fraction(11, 12)
    >>> evaluate("comb(10, 3) * 2**3")
    Fraction(960, 1)
"""

from __future__ import annotations

import ast
import math
import re
import operator
from fractions import Fraction
from typing import Any, Mapping

Number = Fraction | float


class MathError(ValueError):
    """Invalid or unsupported expression, or an undefined operation (e.g. division by zero)."""


def _to_int(x: Number, what: str) -> int:
    f = Fraction(x) if isinstance(x, (int, Fraction)) else None
    if f is None or f.denominator != 1:
        raise MathError(f"{what} needs an integer, got {fmt(x)}")
    return int(f)


def exact_sqrt(x: Number) -> Number:
    if x < 0:
        raise MathError("square root of a negative number")
    if isinstance(x, Fraction):
        n, d = x.numerator, x.denominator
        rn, rd = math.isqrt(n), math.isqrt(d)
        if rn * rn == n and rd * rd == d:
            return Fraction(rn, rd)
    return math.sqrt(float(x))


def _pow(a: Number, b: Number) -> Number:
    if isinstance(b, Fraction) and b.denominator == 1 and isinstance(a, Fraction):
        e = int(b)
        if abs(e) > 10_000:
            raise MathError("exponent too large")
        if a == 0 and e < 0:
            raise MathError("division by zero (0 to a negative power)")
        return a**e
    if isinstance(b, Fraction) and b == Fraction(1, 2):
        return exact_sqrt(a)
    if a < 0:
        raise MathError("negative base with non-integer exponent")
    return float(a) ** float(b)


def _div(a: Number, b: Number) -> Number:
    if b == 0:
        raise MathError("division by zero")
    return a / b


def _mod(a: Number, b: Number) -> Number:
    if b == 0:
        raise MathError("modulo by zero")
    return Fraction(_to_int(a, "%")) % _to_int(b, "%")


def _floordiv(a: Number, b: Number) -> Number:
    if b == 0:
        raise MathError("division by zero")
    return Fraction(math.floor(Fraction(a) / Fraction(b)) if not isinstance(a, float) else math.floor(a / b))


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def _int_fn(fn):
    def wrapped(*args):
        return Fraction(fn(*(_to_int(a, fn.__name__) for a in args)))
    return wrapped


def _bool_int(pred):
    def wrapped(x):
        f = Fraction(x) if not isinstance(x, float) else None
        if f is None or f.denominator != 1:
            return False
        return pred(int(f))
    return wrapped


def _flat(args) -> list:
    """median(a, b, c) and median((a, b, c)) both work."""
    if len(args) == 1 and isinstance(args[0], tuple):
        args = args[0]
    if not args:
        raise MathError("needs at least one value")
    return list(args)


def _median(*args):
    xs = sorted(_flat(args))
    n = len(xs)
    return xs[n // 2] if n % 2 else (xs[n // 2 - 1] + xs[n // 2]) / 2


FUNCTIONS: dict[str, Any] = {
    "mean": lambda *a: sum(_flat(a)) / len(_flat(a)),
    "median": _median,
    "total": lambda *a: sum(_flat(a)),
    "spread": lambda *a: max(_flat(a)) - min(_flat(a)),
    "distinct": lambda *a: len(set(_flat(a))) == len(_flat(a)),
    "sqrt": exact_sqrt,
    "abs": abs,
    "min": min,
    "max": max,
    "factorial": _int_fn(lambda n: math.factorial(n) if 0 <= n <= 1000 else (_ for _ in ()).throw(MathError("factorial range 0..1000"))),
    "comb": _int_fn(math.comb),
    "perm": _int_fn(math.perm),
    "gcd": _int_fn(math.gcd),
    "lcm": _int_fn(math.lcm),
    "floor": lambda x: Fraction(math.floor(x)),
    "ceil": lambda x: Fraction(math.ceil(x)),
    "is_int": lambda x: not isinstance(x, float) and Fraction(x).denominator == 1,
    "is_prime": _bool_int(is_prime),
    "is_even": _bool_int(lambda n: n % 2 == 0),
    "is_odd": _bool_int(lambda n: n % 2 == 1),
    "is_square": _bool_int(lambda n: n >= 0 and math.isqrt(n) ** 2 == n),
}

_BIN = {
    ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul, ast.Div: _div,
    ast.Pow: _pow, ast.Mod: _mod, ast.FloorDiv: _floordiv,
}
_CMP = {
    ast.Eq: operator.eq, ast.NotEq: operator.ne, ast.Lt: operator.lt,
    ast.LtE: operator.le, ast.Gt: operator.gt, ast.GtE: operator.ge,
}


_IMPLICIT_MUL = [
    # 2x, 3(x+1), 2sqrt(5): digit IMMEDIATELY followed by a letter or "(" (not 1e5; never across spaces,
    # so keywords like "0 and y" are untouched). Variables must still be separated: write 5*x*y, not 5xy.
    (re.compile(r"(?<![A-Za-z_\d.])(\d+(?:\.\d+)?)(?=(?:[A-Za-df-zA-Z_(]|e(?![+-]?\d)))"), r"\1*"),
    # (x+1)(x-1), (x+1)y, (x+1)2: closing bracket immediately followed by a term
    (re.compile(r"\)(?=[A-Za-z_\d(])"), ")*"),
]


def _normalise(src: str) -> str:
    s = (src.replace("^", "**").replace("×", "*").replace("÷", "/").replace("−", "-")
            .replace("≤", "<=").replace("≥", ">=").replace("≠", "!=").replace("·", "*"))
    for pat, rep in _IMPLICIT_MUL:
        s = pat.sub(rep, s)
    return s


def free_names(tree: ast.AST) -> set[str]:
    """Variable names an expression uses (excluding known functions and constants)."""
    return {n.id for n in ast.walk(tree)
            if isinstance(n, ast.Name) and n.id not in FUNCTIONS and n.id not in ("pi", "True", "False")}


def require_names(tree: ast.AST, allowed: set[str], where: str) -> None:
    """Fail loudly if an expression uses a variable that has no value or domain."""
    unknown = free_names(tree) - set(allowed)
    if unknown:
        raise MathError(f"{where}: unknown name(s) {', '.join(sorted(unknown))}; "
                        f"defined: {', '.join(sorted(allowed)) or 'none'}")


def parse(src: str) -> ast.Expression:
    if len(src) > 2000:
        raise MathError("expression too long")
    try:
        tree = ast.parse(_normalise(src), mode="eval")
    except SyntaxError as e:
        raise MathError(f"cannot parse {src!r}: {e.msg}") from None
    for node in ast.walk(tree):
        if isinstance(node, (ast.Attribute, ast.Subscript, ast.Lambda, ast.ListComp, ast.DictComp,
                             ast.SetComp, ast.GeneratorExp, ast.Starred, ast.NamedExpr, ast.JoinedStr)):
            raise MathError(f"unsupported syntax: {type(node).__name__}")
    return tree


def evaluate(src: str | ast.Expression, env: Mapping[str, Number] | None = None) -> Any:
    """Evaluate an expression exactly. ``env`` maps variable names to numbers."""
    tree = parse(src) if isinstance(src, str) else src
    env = env or {}

    def ev(n: ast.AST) -> Any:
        match n:
            case ast.Expression(body=b):
                return ev(b)
            case ast.Constant(value=v) if isinstance(v, bool):
                return v
            case ast.Constant(value=v) if isinstance(v, (int, float)):
                return Fraction(str(v)) if isinstance(v, float) else Fraction(v)
            case ast.Name(id=name):
                if name in env:
                    v = env[name]
                    return v if isinstance(v, (Fraction, float, bool)) else Fraction(v)
                if name in ("pi",):
                    return math.pi
                raise MathError(f"unknown name {name!r}")
            case ast.UnaryOp(op=ast.USub(), operand=o):
                return -ev(o)
            case ast.UnaryOp(op=ast.UAdd(), operand=o):
                return ev(o)
            case ast.UnaryOp(op=ast.Not(), operand=o):
                return not ev(o)
            case ast.BinOp(left=l, op=op, right=r) if type(op) in _BIN:
                a, b = ev(l), ev(r)
                if isinstance(a, float) or isinstance(b, float):
                    if type(op) in (ast.Mod, ast.FloorDiv):
                        raise MathError("% and // need exact integers")
                    if type(op) is ast.Div:
                        return _div(float(a), float(b))
                    if type(op) is ast.Pow:
                        return _pow(a, b)
                    return float(_BIN[type(op)](float(a), float(b)))
                return _BIN[type(op)](a, b)
            case ast.BoolOp(op=ast.And(), values=vs):
                return all(ev(v) for v in vs)
            case ast.BoolOp(op=ast.Or(), values=vs):
                return any(ev(v) for v in vs)
            case ast.Compare(left=l, ops=ops, comparators=cs):
                left = ev(l)
                for op, c in zip(ops, cs):
                    if type(op) not in _CMP:
                        raise MathError("unsupported comparison")
                    right = ev(c)
                    if isinstance(left, float) or isinstance(right, float):
                        ok = (math.isclose(float(left), float(right), rel_tol=1e-12, abs_tol=1e-12)
                              if type(op) is ast.Eq else
                              not math.isclose(float(left), float(right), rel_tol=1e-12, abs_tol=1e-12)
                              if type(op) is ast.NotEq else _CMP[type(op)](float(left), float(right)))
                    else:
                        ok = _CMP[type(op)](left, right)
                    if not ok:
                        return False
                    left = right
                return True
            case ast.IfExp(test=t, body=b, orelse=o):
                return ev(b) if ev(t) else ev(o)
            case ast.Call(func=ast.Name(id=fname), args=args, keywords=[]) if fname in FUNCTIONS:
                return FUNCTIONS[fname](*(ev(a) for a in args))
            case ast.Tuple(elts=es) | ast.List(elts=es):
                return tuple(ev(e) for e in es)
        raise MathError(f"unsupported expression element: {ast.dump(n)[:60]}")

    try:
        return ev(tree)
    except ZeroDivisionError:
        raise MathError("division by zero") from None
    except (OverflowError, RecursionError):
        raise MathError("result too large") from None


def fmt(x: Any) -> str:
    """Human-friendly exact formatting: 11/12 (≈ 0.916667)."""
    if isinstance(x, bool):
        return "true" if x else "false"
    if isinstance(x, Fraction):
        if x.denominator == 1:
            return str(x.numerator)
        return f"{x.numerator}/{x.denominator} (≈ {float(x):.6g})"
    if isinstance(x, float):
        return f"≈ {x:.10g}"
    if isinstance(x, tuple):
        return "(" + ", ".join(fmt(v) for v in x) + ")"
    return str(x)
