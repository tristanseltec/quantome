+++
summary = "The fixed answer choices, the AD/BCE elimination grid, and how to avoid solving."
+++

# The Data Sufficiency Method

## The fixed answer choices

Every Data Sufficiency question gives a question stem and two statements. The answer choices never change:

| Choice | Meaning |
|---|---|
| **A** | Statement (1) alone is sufficient, (2) alone is not |
| **B** | Statement (2) alone is sufficient, (1) alone is not |
| **C** | Both together are sufficient, neither alone is |
| **D** | Each statement alone is sufficient |
| **E** | Even together, the statements are not sufficient |

> [!IMPORTANT]
> "Sufficient" means the information leads to **exactly one** answer. For a yes/no question, a definite "no" is sufficient.

## The AD / BCE grid

1. Evaluate statement (1) alone. If it is sufficient, the answer is **A or D**. If not, it is **B, C or E**.
2. Evaluate statement (2) alone, **forgetting statement (1)**.
3. Only if both fail alone, combine them.

> [!TIP]
> You almost never need the actual value. Stop as soon as you know a unique answer *exists*.

> [!WARNING]
> Classic traps:
> - Carrying information from statement (1) into your analysis of statement (2).
> - Assuming variables are integers or positive when the question doesn't say so.
> - Treating two equations as sufficient when they are actually the same equation.

## Worked example

**Question.** Is $x > 0$?

1. $x^2 = 9$
2. $x^3 = 27$

**Solution.** (1) gives $x = 3$ or $x = -3$, so the answer could be yes or no. Not sufficient (BCE). (2) gives $x = 3$, since cube roots are unique. Sufficient. **Answer: B.**

## Practice

**Question.** What is the value of the integer $n$?

1. $n^2 < 10$
2. $n > 2$

<details>
<summary>Answer</summary>

(1): $n \in \{-3, \dots, 3\}$. Not sufficient. (2): $n \ge 3$. Not sufficient. Together: $n = 3$. **C**.

</details>

**Question.** Is the positive integer $k$ even?

1. $k^2$ is even
2. $3k$ is even

<details>
<summary>Answer</summary>

(1): if $k$ were odd, $k^2$ would be odd. So $k$ is even. Sufficient. (2): $3k$ is even, and 3 is odd, so $k$ is even. Sufficient. **D**.

</details>

**Question.** Is $x > 5$?

1. $x^2 > 25$
2. $x$ is positive

<details>
<summary>Answer</summary>

(1): $x > 5$ or $x < -5$, so the answer could be yes or no. Not sufficient (BCE). (2): $x$ could be 1 or 6. Not sufficient. Together: positive *and* outside $(-5, 5)$ forces $x > 5$. **C**.

</details>

**Question.** What is the value of $|x|$?

1. $x = -7$
2. $x^2 = 49$

<details>
<summary>Answer</summary>

(1): $x = -7$, so $|x| = 7$. Sufficient (A or D). (2): $x = 7$ or $x = -7$, but either way $|x| = 7$. Sufficient. **D**.

</details>

**Question.** What is the value of $x$?

1. $x + 2y = 7$
2. $2x + 4y = 14$

<details>
<summary>Answer</summary>

(1): one equation with two unknowns, so infinitely many solutions. Not sufficient (BCE). (2): dividing by 2 gives $x + 2y = 7$ — the same line as (1), so it adds no information. Even together, not sufficient. **E**.

</details>
