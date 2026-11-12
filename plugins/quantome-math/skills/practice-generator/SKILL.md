---
name: practice-generator
description: Generate ORIGINAL GMAT-style practice problems (Problem Solving with five choices, or Data Sufficiency) on a requested topic and difficulty, with distractors built from real traps and every answer machine-verified to have exactly one correct choice. Output can be Quantome Markdown with hidden answers. Use for "give me practice problems", "make a quiz", "drill me on…", or "write questions for chapter X".
---

# Practice generator (verified)

## Rules

1. **Original only.** Never reproduce or paraphrase GMAC Official Guide, GMATPrep or commercial prep questions.
   Invent your own contexts and numbers.
2. **Friendly numbers.** The GMAT Quant section has no calculator, so design numbers that work with mental or paper arithmetic.
3. **Distractors come from traps.** Each wrong choice should be the result of a specific, named mistake, e.g. adding
   percents instead of multiplying, the wrong base, forgetting a negative root, double counting, or answering a different
   question. Keep a private note of which trap each distractor represents.
4. **Verify every item before showing it. No exceptions:**
   - Problem Solving: `python3 scripts/qmath.py choices --answer "<independent expression for the truth>" --choices "A=..,B=..,C=..,D=..,E=.."`
     must report `exactly_one_correct: True`, and the correct letter must be the one you intended.
   - For counting and probability, also confirm by brute-force enumeration in a short Python snippet.
   - Data Sufficiency: run `python3 scripts/qmath.py ds ...` (see the data-sufficiency skill). Every INSUFFICIENT
     verdict must have a counterexample, and every SUFFICIENT verdict needs an algebraic justification.
   - If verification fails, fix or discard the item. Never ship it with a note.
5. **Difficulty labels:**
   - *Easy*: one concept, direct.
   - *Medium*: two steps, or one trap.
   - *Hard*: several concepts, a subtle trap, or abstraction (variables in the choices, DS edge cases).
6. Vary the position of the correct letter across a set.

## Output format (Quantome Markdown)

```markdown
**1.** *(Medium)* A store raises a price by 20% and later lowers the new price by 20%. The final price is what percent of the original?

(A) 80% (B) 96% (C) 100% (D) 104% (E) 120%

<details>
<summary>Answer</summary>

**(B) 96%.** $1.2 \times 0.8 = 0.96$. Trap: (C) assumes the changes cancel.

</details>
```

Literal dollar signs must be written `\$`, and the `<details>` block needs the blank lines shown.
End a set with an answer key table and the topics to review (with Quantome chapter links; see the `gmat-tutor` skill's chapter map).
