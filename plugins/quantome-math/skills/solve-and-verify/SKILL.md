---
name: solve-and-verify
description: Solve quantitative problems (GMAT Quant, arithmetic, algebra, word problems, statistics, counting, probability) step by step, then VERIFY the answer with exact computation before stating it, including checking that exactly one answer choice is correct. Use when asked to "solve", "check my answer", "which choice is right", or "explain this maths problem", or for any multiple-choice quantitative question.
---

# Solve and verify

**The model's mental arithmetic is not trusted.** Every number in the final answer must be confirmed by
`scripts/qmath.py` in this skill's directory (exact fractions, no floating-point surprises, safe: no code execution).
In a clone of the Quantome repository you can also run `PYTHONPATH=py/src python3 -m quantome.mathcli`.

## Procedure

1. **Understand.** Restate what is asked: a value, an expression, or yes/no. Note the constraints (integer?
   positive? distinct?) and the units.
2. **Plan.** Pick the fastest sound method and name it:
   - algebra, or picking numbers (100 for percents; the LCM for fractions)
   - backsolving from the choices (start with the middle value)
   - testing cases (0, 1, negatives, fractions), estimation, the complement ("at least one")
3. **Solve** with clear, numbered steps that a learner can follow.
4. **Verify** with the tools. Never skip this:
   - Exact value: `python3 scripts/qmath.py eval "<expression>"`
   - Which choice is correct, and is it the only one: `python3 scripts/qmath.py choices --answer "<expr for the true value>" --choices "A=..,B=..,C=..,D=..,E=.."`
   - Equation or condition questions: `python3 scripts/qmath.py backsolve --var x --condition "<condition>" --choices "A=..,..."`
   - Specialised tools. All take exact expressions; implicit multiplication like `2x`, `3(x+1)` or `(a+b)(a-b)` is
     allowed, but separate variables explicitly: `5*x*y`, not `5xy`.

     | Need | Command |
     |---|---|
     | value with variables | `eval "2x+1" --at "x=3" --at "x=1/2"` |
     | closest / greatest / least choice | `choices --mode closest --answer "1" --choices ...` · `choices --mode greatest --choices ...` |
     | choices containing variables (picking numbers) | `choices --answer "2x+3y" --choices "A=2(x+y)+y,..." --at "x=3,y=5" --at "x=7,y=2"` |
     | must / could / cannot be true (I, II, III) | `must --domain "x=int:-20..20" --given "x*y > 0" --choices "I=x+y != 0,II=x > 0"` |
     | all solutions, their count and sum | `find --domain "x=grid:-20..20/2" --condition "abs(2x-7) == x+1"` |
     | linear systems | `linsolve "3x + 2y = 17" "2x + 3y = 13"` (classifies unique / none / infinite) |
     | is a combination fixed? | `combo --target "x + y" "3x + 2y = 17" "2x + 3y = 13"` |
     | quadratics | `quadratic 1 -2 -1` (exact surd roots, Vieta) |
     | factors / gcd / lcm | `factor 360` · `gcd-lcm 12 18 30` |
     | powers of primes | `factorial-power 30 2` · `valuation "factorial(50)/factorial(25)" 5` · `trailing-zeros 100` |
     | remainders, units digits | `powmod 2 100 7` · `units-digit 7 2026` |
     | decimals | `decimal 3 7 --digit 100` (terminating?, repeating block, nth digit) |
     | sequences | `arith --first 7 --diff 4 --last 99` (or `--n`) · `geom --first 2 --ratio 3 --n 5` · `recur --init 1,1 --rule "prev + prev2" --n 10` |
     | counting | `count comb --n 10 --k 3` · `count perm ...` · `count circular --n 6` · `count multiset --word MISSISSIPPI` |
     | statistics | `stats 2 4 4 4 5 5 7 9` · inside expressions: `mean(...)`, `median(...)`, `total(...)`, `spread(...)`, `distinct(...)` |

     Domains for `must`, `find` and `ds`: `int:a..b`, `posint:1..b`, `grid:a..b/den` (multiples of 1/den), `set:2,3,5`.
     Searches print a caveat: results outside the domain, or between grid points, are not covered.
   - When a closed form is hard, verify by **brute-force enumeration** in a short Python snippet.
5. **Sanity-check.** Is the magnitude plausible? Do the units match? Does the answer satisfy the original
   conditions? Is it one of the choices?
6. **Answer.** Give the result (and the letter), the key steps, and the verification line, e.g.
   *"Verified: `qmath choices` → only (A) equals 5/14."*

## Rules

- If verification disagrees with your working, **trust the verification**, find the error, and explain it.
- If two or more choices match, or none does, say so. The question may be flawed or misread.
- Expressions use `*` for multiplication, `**` or `^` for powers, `/` for exact division, `%` for remainders, and
  the functions `sqrt, comb, perm, factorial, gcd, lcm, abs, min, max, floor, ceil, is_int, is_prime, is_even, is_odd, is_square`.
- For a learner, explain the *method* and the trap that wrong choices exploit, not just the arithmetic.
  Link the relevant Quantome chapter: https://tristanseltec.github.io/quantome/
