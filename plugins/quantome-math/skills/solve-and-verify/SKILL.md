---
name: solve-and-verify
description: Solve quantitative problems (GMAT Quant, arithmetic, algebra, word problems, statistics, counting, probability) step by step, then VERIFY the answer with exact computation before stating it, including checking that exactly one answer choice is correct. Use when asked to "solve", "check my answer", "which choice is right", or "explain this maths problem", or for any multiple-choice quantitative question.
---

# Solve and verify

**The model's mental arithmetic is not trusted.** Every number in the final answer must be confirmed by
`scripts/qmath.py` in this skill's directory (exact fractions, no floating-point surprises, safe: no code execution).

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
   - Specialised tools:

     | Tool | Command |
     |---|---|
     | linear systems | `linsolve "3x + 2y = 17" "2x + 3y = 13"` |
     | is a combination fixed? | `combo --target "x + y" ...` |
     | quadratics | `quadratic a b c` |
     | factors | `factor N` |
     | gcd and lcm | `gcd-lcm a b ...` |
     | power of a prime in n! | `factorial-power n p` |
     | trailing zeros | `trailing-zeros n` |
     | units digits | `units-digit b e` |
     | remainders of powers | `powmod b e m` |
     | sequences | `arith` / `geom` |
     | counting | `count comb\|perm\|circular\|multiset` |
     | statistics | `stats v1 v2 ...` |

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
