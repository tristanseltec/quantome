+++
summary = "Flip the sign when multiplying by negatives, and split absolute values into cases."
+++

# Inequalities & Absolute Value

## Key ideas

Solve inequalities like equations, with one exception:

> [!WARNING]
> Multiplying or dividing both sides by a **negative** number flips the inequality sign. Never multiply by a variable unless you know its sign.

### Absolute value

$|x|$ is the distance from $x$ to $0$. $|x - a|$ is the distance from $x$ to $a$.

> [!IMPORTANT]
> $$|x - a| < b \iff a - b < x < a + b$$
> $$|x - a| > b \iff x < a - b \;\text{ or }\; x > a + b$$

> [!TIP]
> Read $|x - 3| \le 5$ as "$x$ is within 5 of 3". The answer, $-2 \le x \le 8$, follows immediately.

## Worked example

**Problem.** How many integers $n$ satisfy $|2n - 5| < 7$?

**Solution.** $-7 < 2n - 5 < 7 \Rightarrow -2 < 2n < 12 \Rightarrow -1 < n < 6$. The integers $0$ through $5$ satisfy this, so there are **6**.

## Practice

1. Solve $-3x + 4 > 10$.

<details>
<summary>Answer</summary>

$-3x > 6 \Rightarrow x < -2$. The sign flips because you divide by $-3$.

</details>

2. If $|x + 1| = 2x - 4$, what is $x$?

<details>
<summary>Answer</summary>

Case 1: $x + 1 = 2x - 4 \Rightarrow x = 5$. Check: $|6| = 6$ ✓.
Case 2: $-(x + 1) = 2x - 4 \Rightarrow x = 1$. Check: $|2| = 2$, but $2x - 4 = -2$ ✗.
So **$x = 5$**. Always check absolute-value solutions.

</details>

3. Solve $|x - 10| > 6$.

<details>
<summary>Answer</summary>

Read it as a distance: $x$ must be more than 6 away from 10, so $x < 4$ or $x > 16$.

</details>

4. Solve $3(x - 2) \le 2x + 1$.

<details>
<summary>Answer</summary>

$3x - 6 \le 2x + 1 \Rightarrow x \le$ **7**.

</details>

5. How many integers $n$ satisfy $|n + 2| \le 5$?

<details>
<summary>Answer</summary>

$-5 \le n + 2 \le 5 \Rightarrow -7 \le n \le 3$. Counting the endpoints, $7 + 3 + 1 =$ **11** integers.

</details>
