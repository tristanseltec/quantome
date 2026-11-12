---
name: data-sufficiency
description: Solve and explain GMAT Data Sufficiency questions (answer choices A–E) with the AD/BCE method, backed by an exhaustive counterexample search that proves insufficiency. Use for any question with "Statement (1)… Statement (2)…", "is the information sufficient", or "data sufficiency".
---

# Data Sufficiency, with proof

## The fixed answer choices

| | Meaning |
|---|---|
| **A** | (1) alone sufficient, (2) alone not |
| **B** | (2) alone sufficient, (1) alone not |
| **C** | together sufficient, neither alone |
| **D** | each alone sufficient |
| **E** | not sufficient even together |

"Sufficient" means exactly **one** answer: one value, or a definite yes, or a definite no.

## Procedure

1. **Rephrase the question.** Simplify it: "Is x² > x?" becomes "Is x > 1 or x < 0?". Note what the stem
   guarantees, e.g. "n is a positive integer".
2. **Analyse (1) alone**, then **(2) alone, forgetting (1)**, then both together only if needed (AD/BCE grid).
3. **Prove insufficiency by counterexample, using the tool** (`scripts/qmath.py` in *this skill's directory*; in a
   clone of the Quantome repository you can also run `PYTHONPATH=py/src python3 -m quantome.mathcli`):
   ```bash
   python3 scripts/qmath.py ds --question "<value expr or yes/no condition>" \
       --s1 "<statement 1 as a condition>" --s2 "<statement 2>" \
       --domain "x=int:-30..30" [--domain "y=..."] [--given "<stem constraint>"] [--define "S = k*a + k*(k-1)/2"]
   ```
   - Domains: `int:a..b`, `posint:1..b`, `grid:a..b/4` (multiples of 1/4, to test fractions), `set:2,3,5,7`.
   - **Choose domains that respect the stem.** If the stem doesn't say "integer", also run a `grid` domain:
     fractions and negatives are the most common hidden counterexamples.
   - Conditions use `==`, `<`, `and`, `or`, `not`, and `is_int`, `is_even`, `is_odd`, `is_prime`, `is_square`, `abs`.
   - `--define` creates derived quantities (sums, averages, "Neither = Total − A − B + Both") from the domain variables,
     which also keeps the search small. The search is capped at 2,000,000 points.
   - Statistics helpers: `mean(a,b,c)`, `median(a,b,c)`, `total(...)`, `spread(...)` (range), `distinct(...)`;
     inequality: `!=`.
   - The tool **fails loudly** if any expression uses an undefined name. If a statement is never true, or the two
     statements contradict each other, it answers `undetermined` with a warning, never a silent E. Fix the
     translation before going on.
   - **Thresholds:** a `grid` only tests multiples of its step. If a statement has a boundary such as `r > 0.07`,
     re-run with a finer step around it (e.g. `grid:0.06..0.08/10000`) before trusting SUFFICIENT?.
4. **Interpret the result honestly:**
   - `INSUFFICIENT (proved by counterexample)`: quote the two cases. This is a proof.
   - `SUFFICIENT? (no counterexample found)`: this is only **evidence**. Give the **algebraic argument** that
     the answer is fixed over the whole allowed domain, not just the one searched.
5. **Answer** with the letter, the reasoning for each statement, and the counterexamples used.

## Classic traps to check explicitly

- Squares hide signs (x² = 9 allows ±3). Cubes don't.
- Two equations may be the **same line** (E), or the question may ask for a **combination** that one equation fixes
  (`qmath combo --target "x + y" ...`).
- Multiplying an inequality by a variable of unknown sign is not allowed.
- "No" is a sufficient answer.
- The **C-trap**: one statement alone is often already enough. The **E-trap**: together isn't always enough.

Chapters: https://tristanseltec.github.io/quantome/data-sufficiency/the-data-sufficiency-method/
