# quantome-math

Exact, verifiable maths skills for learners and AI agents. These skills make the model **check its maths with
exact computation** before answering, which removes the arithmetic slips language models are prone to.

```bash
/plugin marketplace add tristanseltec/quantome
/plugin install quantome-math@quantome
```

| Skill | What it does |
|---|---|
| `solve-and-verify` | Step-by-step solutions; every number checked with exact rational arithmetic; confirms **exactly one** answer choice is correct |
| `data-sufficiency` | AD/BCE method plus an exhaustive **counterexample search** that *proves* insufficiency |
| `gmat-tutor` | Socratic hint ladder, diagnosis of traps, error log, links to the Quantome chapter |
| `practice-generator` | Original GMAT-style problems with trap-based distractors, machine-verified before display |

The `answer-verifier` agent re-solves problems independently: use it before publishing a practice set.

## The `qmath` tool

Standard-library Python ≥ 3.11. Expressions are parsed safely with an allow-list (no `eval`) and evaluated exactly.
Undefined names, contradictory statements and impossible conditions fail loudly instead of giving a plausible wrong answer.

```text
qmath eval "3/4 + 1/6"                         → 11/12
qmath choices --answer "comb(5,2)/comb(8,2)" --choices "A=5/14,B=3/8,C=1/4,D=5/28,E=2/7"   → only A
qmath backsolve --var x --condition "x**2-5*x+6==0" --choices "A=1,B=2,C=4,D=5,E=6"       → only B
qmath linsolve "3x + 2y = 17" "2x + 3y = 13"   → x = 5, y = 1 (or: no / infinitely many solutions)
qmath combo --target "x + y" "3x + 2y = 17" "2x + 3y = 13"   → determined: 6
qmath quadratic 1 -2 -1                        → 1 ± √2, sum 2, product −1
qmath factor 72 · gcd-lcm 12 18 30 · factorial-power 30 2 · trailing-zeros 100 · units-digit 7 2026 · powmod 2 100 7
qmath count multiset --word MISSISSIPPI        → 34650
qmath stats 2 4 4 4 5 5 7 9                    → mean 5, SD 2
qmath ds --question "x > 0" --s1 "x**2 == 9" --s2 "x**3 == 27" --domain "x=int:-20..20"  → B (with proof for (1))
qmath must --domain "x=int:-20..20" --domain "y=int:-20..20" --given "x*y > 0" --choices "I=x+y != 0,II=x > 0"  → I must, II could
qmath find --domain "x=grid:-20..20/2" --condition "abs(2x - 7) == x + 1"       → x = 2, 8 (sum 10)
qmath choices --mode greatest --choices "A=2**30,B=3**20,C=5**13,D=6**12"       → B
qmath choices --answer "2x+3y" --choices "A=2(x+y)+y,B=3(x+y)" --at "x=3,y=5" --at "x=7,y=2"   → A (picking numbers)
qmath decimal 3 7 --digit 100 · valuation "factorial(50)/factorial(25)" 5 · recur --init 1,1 --rule "prev + prev2" --n 10
```

Don't edit `lib/`: it is generated from `py/src/quantome` by `scripts/sync_plugins.py`. Licence: Apache-2.0.
