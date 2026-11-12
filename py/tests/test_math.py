"""Tests for the exact maths toolkit used by the quantome-math skills."""
import math
from fractions import Fraction

import pytest

from quantome.math import algebra, ds, numbers
from quantome.math.exact import MathError, evaluate, fmt
from quantome.mathcli import main


# --- safe exact evaluator ---
@pytest.mark.parametrize("expr, value", [
    ("3/4 + 1/6", Fraction(11, 12)),
    ("2^10", 1024),
    ("comb(10,3) * 2**3", 960),
    ("sqrt(49/4)", Fraction(7, 2)),
    ("0.1 + 0.2", Fraction(3, 10)),        # decimals are exact, not floating point
    ("lcm(4, 6) - gcd(12, 18)", 6),
    ("factorial(5) / perm(5, 2)", 6),
    ("(-2)^3", -8),
    ("17 % 5", 2),
])
def test_exact_values(expr, value):
    assert evaluate(expr) == value


def test_irrational_is_flagged_approximate():
    v = evaluate("sqrt(2)")
    assert isinstance(v, float) and fmt(v).startswith("≈")


@pytest.mark.parametrize("evil", [
    "__import__('os').system('echo pwned')",
    "().__class__.__bases__",
    "open('/etc/passwd')",
    "[x for x in range(10)]",
    "lambda: 1",
    "exec('1')",
])
def test_rejects_code(evil):
    with pytest.raises(MathError):
        evaluate(evil)


def test_division_by_zero_and_limits():
    with pytest.raises(MathError):
        evaluate("1/(2-2)")
    with pytest.raises(MathError):
        evaluate("2**100000")


# --- number theory ---
def test_factor_report():
    r = numbers.factor_report(72)
    assert r["number_of_divisors"] == 12 and r["odd_divisors"] == 3 and not r["is_perfect_square"]
    assert numbers.factor_report(36)["is_perfect_square"]
    assert numbers.factor_report(180)["number_of_divisors"] == 18


def test_legendre_and_trailing_zeros():
    assert numbers.legendre(30, 2)["exponent"] == 26
    assert numbers.trailing_zeros(100)["trailing_zeros_of_factorial"] == 24
    for n in range(1, 60):  # brute-force agreement
        f = math.factorial(n)
        z = len(str(f)) - len(str(f).rstrip("0"))
        assert numbers.trailing_zeros(n)["trailing_zeros_of_factorial"] == z


def test_units_digit_matches_pow():
    for b in range(0, 20):
        for e in range(1, 40):
            assert numbers.units_digit_power(b, e)["units_digit"] == pow(b, e, 10)


def test_gcd_lcm():
    r = numbers.gcd_lcm([12, 18, 30])
    assert r["gcd"] == 6 and r["lcm"] == 180


# --- algebra ---
def test_linear_systems():
    assert algebra.solve_linear(["3x + 2y = 17", "2x + 3y = 13"])["solution"] == {"x": "5", "y": "1"}
    assert algebra.solve_linear(["x + 2y = 3", "2x + 4y = 6"])["status"].startswith("infinitely")
    assert algebra.solve_linear(["x + 2y = 3", "2x + 4y = 7"])["status"].startswith("no solution")
    assert algebra.solve_linear(["x/2 + y = 4", "x - y = -1"])["solution"] == {"x": "2", "y": "3"}


def test_combination_determined():
    r = algebra.combination_determined(["x + 2y + 3z = 10", "2x + 4y + 6z = 20"], "x + 2y + 3z")
    assert r["determined"] and r["value"] == "10"
    r = algebra.combination_determined(["x + y + z = 10", "x - z = 2"], "2x + y")
    assert r["determined"] and r["value"] == "12"
    assert not algebra.combination_determined(["x + y + z = 10"], "x + y")["determined"]


def test_quadratic_vieta_and_surds():
    r = algebra.quadratic("2", "3", "-2")
    assert r["roots"] == ["-2", "1/2 (≈ 0.5)"]
    assert r["sum_of_roots (−b/a)"].startswith("-3/2") and r["product_of_roots (c/a)"] == "-1"
    assert algebra.quadratic("1", "-2", "-1")["roots"].startswith("1 ± √2")
    assert "no real roots" in algebra.quadratic("1", "0", "1")["roots"]


def test_sequences_counting_stats():
    assert algebra.arithmetic_sequence("3", "4", 20)["sum"] == "820"
    assert algebra.geometric_sequence("2", "3", 5)["sum"] == "242"
    assert algebra.count("multiset", word="MISSISSIPPI")["arrangements"] == 34650
    assert algebra.count("circular", n=6)["arrangements"] == 120
    s = algebra.describe(["2", "4", "4", "4", "5", "5", "7", "9"])
    assert s["mean"] == "5" and s["population_sd"] == "2"


# --- Data Sufficiency tester ---
def test_ds_classic_B():
    r = ds.test("x > 0", {"1": "x**2 == 9", "2": "x**3 == 27"}, ["x=int:-20..20"])
    assert r["suggested_answer"] == "B"
    assert r["verdicts"]["1"]["status"].startswith("INSUFFICIENT")


def test_ds_value_question_C_and_E():
    # What is x? (1) x + y = 10  (2) x - y = 2  → C
    r = ds.test("x", {"1": "x + y == 10", "2": "x - y == 2"}, ["x=int:-30..30", "y=int:-30..30"])
    assert r["suggested_answer"] == "C"
    # What is x? (1) x + y = 10  (2) 2x + 2y = 20  → E (same line)
    r = ds.test("x", {"1": "x + y == 10", "2": "2*x + 2*y == 20"}, ["x=int:-30..30", "y=int:-30..30"])
    assert r["suggested_answer"] == "E"


def test_ds_fractions_matter():
    # Is n an integer? (1) 2n is an integer (2) 3n is an integer → C (n = 3n − 2n); grid with step 1/6
    r = ds.test("is_int(n)", {"1": "is_int(2*n)", "2": "is_int(3*n)"}, ["n=grid:-3..3/6"])
    assert r["suggested_answer"] == "C"


def test_ds_stem_constraint_and_D():
    # n positive integer: is n even? (1) n^2 even (2) 3n even → D
    r = ds.test("is_even(n)", {"1": "is_even(n**2)", "2": "is_even(3*n)"}, ["n=posint:1..200"])
    assert r["suggested_answer"] == "D"


def test_ds_rejects_huge_search():
    with pytest.raises(MathError):
        ds.test("x", {"1": "x>0", "2": "y>0"}, ["x=int:-2000..2000", "y=int:-2000..2000"])


# --- CLI ---
def test_cli_choices_and_errors(capsys):
    assert main(["choices", "--answer", "comb(5,2)/comb(8,2)", "--choices", "A=5/14,B=3/8,C=1/4,D=5/28,E=2/7"]) == 0
    assert "['A']" in capsys.readouterr().out
    assert main(["eval", "__import__('os')"]) == 2


# --- improvements driven by the Part I verification reports ---
from quantome.math import search  # noqa: E402
from quantome.math.exact import _normalise  # noqa: E402


@pytest.mark.parametrize("src, out", [
    ("2x+1", "2*x+1"), ("3(x+2)", "3*(x+2)"), ("(x+1)(x-1)", "(x+1)*(x-1)"), ("2sqrt(9)", "2*sqrt(9)"),
    ("1e3", "1e3"), ("x == 0 and y", "x == 0 and y"), ("2 if x else 3", "2 if x else 3"), ("comb(5,2)", "comb(5,2)"),
])
def test_implicit_multiplication_is_safe(src, out):
    assert _normalise(src) == out


def test_fail_loudly_on_unknown_names():
    with pytest.raises(MathError, match="unknown name"):
        ds.test("x > 0", {"1": "x**2 == 9", "2": "S > 0"}, ["x=int:-5..5"])
    with pytest.raises(MathError, match="unknown name"):
        ds.test("x", {"1": "x > 0", "2": "x < 3"}, ["x=int:-5..5"], constraints=["T > 1"])
    assert main(["backsolve", "--var", "x", "--condition", "x + y == 2", "--choices", "A=1,B=2"]) == 2


def test_ds_contradictions_are_flagged_not_answered_E():
    r = ds.test("x", {"1": "x > 100", "2": "x < 0"}, ["x=int:-10..10"])
    assert r["suggested_answer"].startswith("undetermined") and r["warnings"]
    with pytest.raises(MathError, match="no admissible"):
        ds.test("x", {"1": "x > 0", "2": "x < 3"}, ["x=int:-5..5"], constraints=["x > 50"])


def test_ds_defines():
    r = ds.test("S", {"1": "k == 4", "2": "a == 3"}, ["k=posint:1..10", "a=int:-10..10"],
                defines=["S = k*a + k*(k-1)/2"])
    assert r["suggested_answer"] == "C"


def test_choices_modes_and_picking_numbers(capsys):
    assert main(["--json", "choices", "--mode", "closest", "--answer", "1",
                 "--choices", "A=7/8,B=9/10,C=11/10,D=21/20,E=4/5"]) == 0
    assert '"D"' in capsys.readouterr().out.split('"correct_choices"')[1]
    assert main(["--json", "choices", "--mode", "greatest", "--choices", "A=2**30,B=3**20,C=5**13,D=6**12"]) == 0
    assert '"B"' in capsys.readouterr().out.split('"correct_choices"')[1]
    assert main(["--json", "choices", "--answer", "2x + 3y", "--choices", "A=2(x+y)+y,B=3(x+y),C=5*x*y",
                 "--at", "x=3,y=5", "--at", "x=7,y=2"]) == 0
    assert '"exactly_one_correct": true' in capsys.readouterr().out


def test_must_could_cannot():
    r = search.must_could(["x=int:-20..20", "y=int:-20..20"],
                          [("I", "x + y != 0"), ("II", "x > 0"), ("III", "x*y < 0")], ["x*y > 0"])
    assert r["must_be_true"] == ["I"] and r["cannot_be_true"] == ["III"]


def test_find_all_solutions():
    r = search.find_all(["x=grid:-20..20/2"], "abs(2x - 7) == x + 1")
    assert r["distinct_values"] == ["2", "8"] and r["sum_of_distinct_values"] == "10"
    r = search.find_all(["n=int:-100..100"], "n**2 < 50")
    assert r["count"] == 15


def test_valuation_decimal_recurrence_arith():
    assert numbers.valuation(evaluate("factorial(50)/factorial(25)"), 5)["exponent"] == 6
    d = numbers.decimal_expansion(3, 7, digit=100)
    assert d["repeating_block"] == "428571" and d["digit_100_after_point"] == 5
    assert numbers.decimal_expansion(7, 40)["terminating"] and numbers.decimal_expansion(7, 40)["decimal"] == "0.175"
    assert numbers.decimal_expansion(1, 6)["decimal"] == "0.1(6)"
    assert algebra.recurrence(["1", "1"], "prev + prev2", 10)["nth_term"] == "55"
    a = algebra.arithmetic_sequence("7", "4", last="99")
    assert a["n"] == 24 and a["sum"] == "1272"
    with pytest.raises(MathError):
        algebra.arithmetic_sequence("7", "4", last="100")


def test_statistics_helpers_in_expressions():
    assert evaluate("median(7, 2, 9, 4)") == Fraction(11, 2)
    assert evaluate("mean((1, 2, 3, 6))") == 3
    assert evaluate("spread(3, 10, 4)") == 7 and evaluate("distinct(1, 2, 2)") is False
    r = ds.test("median(a, b, c)", {"1": "mean(a, b, c) == 5", "2": "a == 5"},
                ["a=int:0..10", "b=int:0..10", "c=int:0..10"], constraints=["a <= b", "b <= c"])
    assert r["verdicts"]["1"]["status"].startswith("INSUFFICIENT")
