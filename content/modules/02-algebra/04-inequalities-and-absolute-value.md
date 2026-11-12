+++
summary = "Manipulate inequalities safely, combine and bound them, read absolute value as distance, and use number-line testing to solve inequality and absolute-value questions, including Data Sufficiency."
+++

# Inequalities & Absolute Value

Inequalities and absolute values are where the GMAT tests whether you really understand algebra or are just pushing symbols around. The rules are almost the same as for equations, but the few exceptions (multiplying by a negative, multiplying by a variable, squaring, subtracting two inequalities) are exactly where wrong answer choices come from. This chapter explains *why* each rule holds, so the exceptions stop being things to memorise and start being obvious. It then treats absolute value the way the test writers think about it: as **distance on a number line**.

## Key ideas

### The rules, and why the sign flips

An inequality $a < b$ says that $a$ lies to the left of $b$ on the number line. Ask what each operation does to that picture.

- **Adding or subtracting the same number** slides both points the same distance. Their order is unchanged: if $a < b$ then $a + c < b + c$ for **any** $c$.
- **Multiplying or dividing by a positive number** stretches or shrinks the line around 0. The order is unchanged.
- **Multiplying or dividing by a negative number** also reflects the line through 0, which reverses the order. From $2 < 5$, multiplying by $-1$ gives $-2$ and $-5$, and now $-2 > -5$.

> [!IMPORTANT]
> If $a < b$:
> - $a + c < b + c$ for every $c$.
> - $ac < bc$ if $c > 0$, but $ac > bc$ if $c < 0$ (**flip** the sign).
> - $\dfrac1a > \dfrac1b$ if $a$ and $b$ have the **same** sign (both positive or both negative).

So to solve $4 - 3x \ge 19$: subtract 4 to get $-3x \ge 15$, then divide by $-3$ **and flip**: $x \le -5$. A quick check: $x = -6$ gives $4 + 18 = 22 \ge 19$. ✓

> [!WARNING]
> **Never multiply or divide by a variable** unless you know its sign. If $\dfrac{5}{x} < 1$, multiplying by $x$ gives $5 < x$ only if $x > 0$. If $x < 0$, the inequality flips and gives $5 > x$, which is true of every negative $x$. The full answer is $x < 0$ or $x > 5$. Either split into cases or multiply by $x^2$, which is positive.

The reciprocal rule follows from dividing $a < b$ by the positive number $ab$: $\dfrac1b < \dfrac1a$. If $a < 0 < b$, then $ab < 0$ and the rule fails: $-2 < 3$ and $-\tfrac12 < \tfrac13$, with no flip.

### Compound inequalities

A compound inequality like $-2 < 5 - 3x \le 11$ holds two inequalities at once. Do the same operation to **all three parts**:
$$
-2 < 5 - 3x \le 11 \;\Rightarrow\; -7 < -3x \le 6 \;\Rightarrow\; \tfrac73 > x \ge -2.
$$
Dividing by $-3$ flipped both signs. Rewrite it in increasing order, $-2 \le x < \tfrac73$, before reading off an answer.

### Combining inequalities: add, never subtract

If $a < b$ and $c < d$, then $a + c < b + d$. Think of two runners who are each behind their rivals: together they are still behind. **Adding** inequalities that point the same way is always allowed.

**Subtracting** is not. From $5 > 1$ and $4 > 0$, subtracting gives $1 > 1$, which is false. The safe way to subtract is to multiply the second inequality by $-1$ (flipping it) and then add.

**Multiplying** two inequalities is allowed only when everything is positive: $2 > 1$ and $3 > 2$ give $6 > 2$, but $-1 > -2$ and $-1 > -3$ would give $1 > 6$.

> [!WARNING]
> Make the inequalities point the same way, then **add** them. To combine $x > 3$ and $y < 1$ into something about $x - y$, rewrite $y < 1$ as $-y > -1$ and add: $x - y > 2$.

### Maximising and minimising with inequalities

If $-3 \le x \le 5$ and $-4 \le y \le 2$, what are the possible values of combinations of $x$ and $y$?

- **Sums** and **differences**: use the extremes. $x + y$ ranges from $-3 + (-4) = -7$ to $5 + 2 = 7$. For $x - y$, the largest value uses the largest $x$ and the **smallest** $y$: $5 - (-4) = 9$. The smallest uses $-3 - 2 = -5$.
- **Products**: test the four **corners** (combinations of endpoints), because signs matter. Here the corners give $(-3)(-4) = 12$, $(-3)(2) = -6$, $5(-4) = -20$ and $5 \cdot 2 = 10$. So $xy$ ranges from $-20$ to $12$. The maximum comes from two negatives, not from the two largest numbers.
- **Squares**: $x^2$ is smallest at $x = 0$ if 0 is in the range. For $-3 \le x \le 5$, $x^2$ runs from 0 to 25, not from 9 to 25.

> [!TIP]
> For max/min questions, list the candidate values at the endpoints (and at 0 if squares or absolute values are involved), compute the expression at each, and pick the extreme. Also watch **strict** inequalities: if $2 < x < 6$, then 6 is not a possible value of $x$, so a "maximum" of $x$ does not exist. Answer choices often include the endpoint as a trap.

### Absolute value as distance

$|x|$ is the **distance from $x$ to 0** on the number line, so it is never negative: $|5| = |-5| = 5$. More useful: $|x - a|$ is the **distance between $x$ and $a$**. Then:

- $|x - 3| = 5$ means "$x$ is 5 away from 3": $x = -2$ or $x = 8$.
- $|x - 3| < 5$ means "$x$ is within 5 of 3": $-2 < x < 8$.
- $|x - 3| > 5$ means "$x$ is more than 5 away from 3": $x < -2$ or $x > 8$.
- $|x + 4| = |x - (-4)|$ is the distance from $x$ to $-4$.

> [!IMPORTANT]
> For $b > 0$:
> $$|x - a| = b \iff x = a \pm b$$
> $$|x - a| < b \iff a - b < x < a + b$$
> $$|x - a| > b \iff x < a - b \;\text{ or }\; x > a + b$$

For an expression like $|3x + 2| < 7$, apply the same pattern to the whole expression: $-7 < 3x + 2 < 7$, so $-3 < x < \tfrac53$.

> [!TIP]
> Translate tolerance language straight into absolute value: "within 0.05 of 4.20" is $|x - 4.20| \le 0.05$. The **centre** goes inside with $x$, and the **allowed distance** goes on the right.

### Solving absolute-value equations by cases

For $|ax + b| = c$ with a number $c$: if $c < 0$ there is no solution (a distance cannot be negative); if $c = 0$, one solution; if $c > 0$, solve $ax + b = c$ and $ax + b = -c$.

When the right side contains $x$, as in $|2x - 7| = x + 1$, the cases can produce **false** solutions, so check each one in the original equation:

- Case $2x - 7 = x + 1$: $x = 8$. Check: $|9| = 9$. ✓
- Case $2x - 7 = -(x + 1)$: $x = 2$. Check: $|-3| = 3$. ✓

Here both survive. In $|x + 1| = 2x$, the case $x + 1 = -2x$ gives $x = -\tfrac13$, but then the right side $2x$ is negative, which no absolute value can equal. So only $x = 1$ is a solution.

A useful identity: $|x| = x$ exactly when $x \ge 0$, and $|x| = -x$ exactly when $x \le 0$. So "$|x + 5| = -(x + 5)$" simply says $x + 5 \le 0$.

### Sums of absolute values: |x| + |y| situations

Several facts about $|x|$ and $|y|$ appear constantly in Data Sufficiency.

> [!IMPORTANT]
> **Triangle inequality.** $|x + y| \le |x| + |y|$, with equality exactly when $x$ and $y$ do not have opposite signs ($xy \ge 0$).
> Similarly $|x - y| \le |x| + |y|$, with equality exactly when $xy \le 0$.

Why: if $x$ and $y$ have the same sign, adding them piles the distances up, so $|x + y| = |x| + |y|$. If they have opposite signs, they partly cancel, so $|x + y|$ is smaller. Consequences:

- $|x + y| < |x| + |y|$ tells you **exactly** that $xy < 0$.
- $|x - y| = |x| + |y|$ tells you $xy \le 0$, which still allows $x = 0$ or $y = 0$.
- $|x| + |y| = 0$ forces $x = y = 0$, because both terms are non-negative.

**Sums of distances.** $|x - 3| + |x + 4|$ is the distance from $x$ to 3 plus the distance from $x$ to $-4$. For any $x$ **between** $-4$ and $3$, this is just the gap, 7. Outside that interval, each step away adds 2 (one to each distance). This picture solves equations and inequalities with two absolute values in seconds.

### The "square both sides" trap

Squaring is not a safe operation on inequalities. $-5 < 2$, but $25 > 4$. Squaring preserves an inequality only when **both sides are non-negative**.

> [!WARNING]
> - $x > y$ does **not** imply $x^2 > y^2$. Try $x = 1$, $y = -3$.
> - $x^2 > y^2$ does **not** imply $x > y$. It means $|x| > |y|$.
> - $x^2 < 9$ means $-3 < x < 3$, not $x < 3$.

But squaring is perfectly legal when both sides are already non-negative, and that includes absolute values: $|x - 2| > |x + 4| \iff (x - 2)^2 > (x + 4)^2$. Expanding gives $-4x + 4 > 8x + 16$, so $x < -1$. The distance view agrees: $x$ is closer to $-4$ than to $2$, so it is left of their midpoint, $-1$.

Odd powers are safe: $x < y \iff x^3 < y^3$ for all real numbers, because cubing keeps signs.

### Testing values on a number line

When an inequality or absolute-value expression has several "critical points" (where a factor or an expression inside $|\cdot|$ is zero), those points split the number line into regions. Within each region, the sign of every piece is constant, so **testing one value per region tells you everything**. This is the same sign analysis used for quadratic inequalities in [Quadratics and polynomials](../../algebra/quadratics-and-polynomials/).

> [!TIP]
> For "which must be true" and Data Sufficiency questions, test numbers deliberately: a positive, a negative, zero, a fraction between 0 and 1, and a fraction between $-1$ and 0. A statement is "sufficient" only if **every** allowed value gives the same answer. One counterexample is enough to kill it.

## Worked examples

**Example 1** *(Easy)*. How many integers $x$ satisfy $-2 < 5 - 3x \le 11$?

- (A) 3
- (B) 4
- (C) 5
- (D) 6
- (E) 7

*Solution.* Subtract 5 from all three parts: $-7 < -3x \le 6$. Divide by $-3$ and flip both signs: $\tfrac73 > x \ge -2$, that is $-2 \le x < 2\tfrac13$. The integers are $-2, -1, 0, 1, 2$: five of them. **Answer: (C).**

Choice (B) appears if you forget that $-2$ is included ($\le$ became $\ge$, still inclusive), and choice (D) if you round $2\tfrac13$ up to 3.

**Example 2** *(Medium)*. If $-3 \le x \le 5$ and $-4 \le y \le 2$, what is the greatest possible value of $xy$?

- (A) 6
- (B) 10
- (C) 12
- (D) 15
- (E) 20

*Solution.* Check the four corners: $(-3)(-4) = 12$, $(-3)(2) = -6$, $(5)(-4) = -20$, $(5)(2) = 10$. The greatest is 12. **Answer: (C).** The trap is (B): multiplying the two largest values. Two negatives with large absolute values can beat two positives.

**Example 3** *(Medium)*. What is the sum of all values of $x$ that satisfy $|2x - 7| = x + 1$?

- (A) 2
- (B) 6
- (C) 8
- (D) 10
- (E) 12

*Solution.* Case 1: $2x - 7 = x + 1$ gives $x = 8$. Case 2: $2x - 7 = -(x + 1)$ gives $3x = 6$, so $x = 2$. Check both in the original: $|9| = 9$ ✓ and $|-3| = 3$ ✓. The sum is $10$. **Answer: (D).** (C) and (A) are the single solutions for students who only do one case. Checking matters because, with $x$ on the right side, a case can produce a value that fails, as in the key ideas.

**Example 4** *(Hard)*. How many integers $x$ satisfy $|x - 3| + |x + 4| \le 11$?

- (A) 8
- (B) 10
- (C) 11
- (D) 12
- (E) 13

*Distance method.* $|x - 3| + |x + 4|$ is the total distance from $x$ to $3$ and to $-4$. Between $-4$ and $3$ it is exactly 7, which is within 11. Outside, every unit beyond an endpoint adds 2, so we can go $\tfrac{11 - 7}{2} = 2$ units beyond each end: $-6 \le x \le 5$. That contains $5 - (-6) + 1 = 12$ integers. **Answer: (D).**

*Case method.* For $x \ge 3$: $(x - 3) + (x + 4) = 2x + 1 \le 11$, so $x \le 5$. For $x \le -4$: $-(x - 3) - (x + 4) = -2x - 1 \le 11$, so $x \ge -6$. In between, the sum is 7. Same answer, with more writing.

**Example 5** *(Hard, Data Sufficiency)*. Is $xy < 0$?

(1) $|x + y| < |x| + |y|$

(2) $|x - y| = |x| + |y|$

*Solution.* (1): the triangle inequality is strict exactly when $x$ and $y$ have opposite signs, so $xy < 0$. Answer "yes". Sufficient.

(2): equality in $|x - y| \le |x| + |y|$ holds exactly when $xy \le 0$. That allows $xy < 0$ (for example $x = 2$, $y = -1$: $3 = 3$, answer "yes") but also $x = 0$ (for example $x = 0$, $y = 5$: $5 = 5$, answer "no"). Not sufficient.

**Answer: (A).** Zero is the counterexample people forget.

## Practice

Data Sufficiency items use the fixed answer choices explained in [The data sufficiency method](../../data-sufficiency/the-data-sufficiency-method/): **(A)** statement (1) alone is sufficient, but (2) alone is not; **(B)** (2) alone is sufficient, but (1) alone is not; **(C)** both together are sufficient, but neither alone is; **(D)** each alone is sufficient; **(E)** the statements together are not sufficient.

**1.** *(Easy)* Which of the following is the solution set of $4 - 3x \ge 19$?

- (A) $x \ge -5$
- (B) $x \le -5$
- (C) $x \ge 5$
- (D) $x \le 5$
- (E) $x \le -\tfrac{23}{3}$

<details>
<summary>Answer</summary>

$-3x \ge 15$, and dividing by $-3$ flips the sign: $x \le -5$. **(B)**. (A) forgets the flip. (E) comes from adding 4 instead of subtracting it.

</details>

**2.** *(Easy)* How many integers $x$ satisfy $|x - 6| \le 4$?

- (A) 4
- (B) 8
- (C) 9
- (D) 10
- (E) 11

<details>
<summary>Answer</summary>

$x$ is within 4 of 6: $2 \le x \le 10$. That is $10 - 2 + 1 = 9$ integers. **(C)**. (B) is the length of the interval, which forgets to count one endpoint.

</details>

**3.** *(Medium)* If $a > b$ and $c > d$, which of the following must be true?

I. $a + c > b + d$

II. $a - c > b - d$

III. $ac > bd$

- (A) I only
- (B) II only
- (C) I and II only
- (D) I and III only
- (E) I, II and III

<details>
<summary>Answer</summary>

I: adding two inequalities that point the same way is always valid. True.

II: subtracting is not valid. Counterexample: $a = 2$, $b = 1$, $c = 10$, $d = 0$ gives $-8 > 1$, false.

III: multiplying is valid only for positive numbers. Counterexample: $a = 1$, $b = 0$, $c = -1$, $d = -2$ gives $-1 > 0$, false.

**(A)**.

</details>

**4.** *(Medium)* If $2 < x < 6$ and $1 < y < 4$, which of the following could be the value of $x - y$?

- (A) $-3$
- (B) $-2$
- (C) 4
- (D) 5
- (E) 7

<details>
<summary>Answer</summary>

Rewrite $1 < y < 4$ as $-4 < -y < -1$ and add it to $2 < x < 6$: $-2 < x - y < 5$. The endpoints are **not** reachable because all the inequalities are strict. Only 4 lies strictly inside. **(C)**. For example $x = 5.5$, $y = 1.5$. (B) and (D) are the boundary traps.

</details>

**5.** *(Medium)* If $|x + 5| = -(x + 5)$, which of the following must be true?

- (A) $x < -5$
- (B) $x \le -5$
- (C) $x \ge -5$
- (D) $x = -5$
- (E) $x > 5$

<details>
<summary>Answer</summary>

$|t| = -t$ exactly when $t \le 0$. With $t = x + 5$: $x + 5 \le 0$, so $x \le -5$. **(B)**. (A) forgets that at $x = -5$ both sides are 0, which satisfies the equation.

</details>

**6.** *(Medium)* A machined part is acceptable only if its length $x$, in centimetres, is within 0.05 cm of 4.20 cm. Which of the following describes exactly the acceptable lengths?

- (A) $|x - 0.05| \le 4.20$
- (B) $|x + 4.20| \le 0.05$
- (C) $|x - 4.20| \le 0.05$
- (D) $|x - 4.20| \ge 0.05$
- (E) $|x| \le 4.25$

<details>
<summary>Answer</summary>

"Within 0.05 of 4.20" is "distance from 4.20 at most 0.05": $|x - 4.20| \le 0.05$, that is $4.15 \le x \le 4.25$. **(C)**. (A) swaps the centre and the distance; (B) centres at $-4.20$; (D) describes the *unacceptable* lengths (plus the two boundary values); (E) also accepts every length from 0 to 4.15.

</details>

**7.** *(Hard)* If $x$ and $y$ are non-zero numbers and $x < y$, which of the following must be true?

I. $x^2 < y^2$

II. $x^3 < y^3$

III. $\dfrac1x > \dfrac1y$

- (A) I only
- (B) II only
- (C) III only
- (D) I and II only
- (E) II and III only

<details>
<summary>Answer</summary>

I: fails for $x = -3$, $y = 1$ ($9 > 1$). Squaring does not preserve order when signs differ.

II: cubing keeps signs and order for all real numbers. True.

III: the reciprocal flip only works when $x$ and $y$ have the same sign. With $x = -1$, $y = 2$: $-1 > \tfrac12$ is false.

**(B)**.

</details>

**8.** *(Hard)* If $-2 \le a \le 3$ and $-5 \le b \le 1$, what is the least possible value of $a^2 - b$?

- (A) $-6$
- (B) $-5$
- (C) $-1$
- (D) 0
- (E) 3

<details>
<summary>Answer</summary>

Minimise each part separately. $a^2$ is smallest at $a = 0$ (allowed, since 0 is in the range), giving 0. $-b$ is smallest when $b$ is largest, $b = 1$, giving $-1$. So the minimum is $0 - 1 = -1$. **(C)**. (E) uses the endpoint $a = -2$ instead of $a = 0$: $4 - 1 = 3$. (B) takes $-b = -5$, as if $b$ could be 5.

</details>

**9.** *(Hard)* Which of the following describes all $x$ such that $|x - 2| > |x + 4|$?

- (A) $x > -1$
- (B) $x < -1$
- (C) $x < 1$
- (D) $x > 1$
- (E) $-4 < x < 2$

<details>
<summary>Answer</summary>

*Distance:* $x$ is farther from 2 than from $-4$, so it is on the $-4$ side of their midpoint, $\tfrac{2 + (-4)}{2} = -1$: $x < -1$.

*Algebra:* both sides are non-negative, so squaring is legal: $x^2 - 4x + 4 > x^2 + 8x + 16$, so $-12x > 12$, so $x < -1$ (dividing by $-12$ flips the sign). **(B)**. (A) forgets the flip.

</details>

**10.** *(Hard, Data Sufficiency)* Is $x > y$?

(1) $x^2 > y^2$

(2) $x > 0$

<details>
<summary>Answer</summary>

(1): this says $|x| > |y|$. $x = 3$, $y = 1$ gives "yes"; $x = -3$, $y = 1$ gives "no". Not sufficient.

(2): $x = 1$, $y = 2$ gives "no"; $x = 2$, $y = 1$ gives "yes". Not sufficient.

Together: $x > 0$, so $x = |x| > |y| \ge y$. Always "yes". Sufficient. **(C)**.

</details>

**11.** *(Hard, Data Sufficiency)* What is the value of $x$?

(1) $|x - 4| = 3$

(2) $|x + 1| = 2x$

<details>
<summary>Answer</summary>

(1): $x$ is 3 away from 4, so $x = 1$ or $x = 7$. Not sufficient.

(2): the right side must be non-negative, so $x \ge 0$, and then $x + 1 > 0$, so $|x + 1| = x + 1$. That gives $x + 1 = 2x$, so $x = 1$. (The other case, $-(x + 1) = 2x$, gives $x = -\tfrac13$, which makes $2x$ negative, so it is rejected.) Sufficient.

**(B)**. Many people choose (C) because both statements happen to share the value $x = 1$, but (2) alone already settles it.

</details>

> [!NOTE]
> If you use Claude Code, the `quantome-math` plugin (`/plugin install quantome-math@quantome`) can check a solution set after you have worked it out by hand. On test day you will rely on number-line testing instead.

## Takeaways

- Adding, subtracting, and multiplying by a positive keep the order; multiplying or dividing by a negative flips it. Never multiply by a variable of unknown sign.
- You may add inequalities that point the same way; never subtract them. Flip one and add instead.
- For ranges, use endpoints for sums and differences, all four corners for products, and remember 0 for squares and absolute values. Watch strict inequalities at the endpoints.
- $|x - a|$ is the distance from $x$ to $a$: "$< b$" means within $b$, "$> b$" means farther than $b$.
- With $x$ on both sides of an absolute-value equation, solve both cases and check each one in the original.
- $|x + y| < |x| + |y|$ exactly when $xy < 0$; $|x| + |y| = 0$ only when both are zero.
- Squaring an inequality is safe only when both sides are non-negative; $x^2 > y^2$ means $|x| > |y|$.
- Find the critical points, test one value per region, and look for one counterexample to kill a statement.

## Further reading

- GMAC, *GMAT Official Guide* (current edition) and the *GMAT Official Guide Quantitative Review*: real retired questions, especially Data Sufficiency, on inequalities and absolute value.
- In this book: [Number properties](../../arithmetic/number-properties/) (signs and parity), [Quadratics and polynomials](../../algebra/quadratics-and-polynomials/) (sign analysis), [Problem-solving strategies](../../getting-started/problem-solving-strategies/) and [Data sufficiency by topic](../../data-sufficiency/data-sufficiency-by-topic/).
