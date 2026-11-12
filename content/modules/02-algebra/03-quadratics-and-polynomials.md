+++
summary = "Expand and factor quadratics on sight, solve them by factoring or the formula, use the sum and product of roots, solve quadratic inequalities by sign analysis, and simplify algebraic fractions without losing roots."
+++

# Quadratics & Polynomials

A quadratic is any expression of the form $ax^2 + bx + c$ with $a \ne 0$. On the GMAT, quadratics appear in two disguises. Sometimes they are obvious: "solve $x^2 - 5x + 6 = 0$". More often they are hidden inside a word problem (consecutive integers, area, a price that changes with quantity), inside an exponent question, or inside an expression like $\dfrac{x^2 - 9}{x + 3}$ that is begging to be factored.

The good news is that the GMAT tests a small, predictable toolkit: three special products, factoring, the zero-product rule, the discriminant, the sum and product of the roots, and sign analysis. This chapter builds each tool from first principles and shows the traps the wrong answer choices are made from.

## Key ideas

### Expanding: FOIL and why it works

Multiplying two binomials is just the distributive law applied twice:
$$
(x + 3)(x - 5) = x(x - 5) + 3(x - 5) = x^2 - 5x + 3x - 15 = x^2 - 2x - 15.
$$
The mnemonic **FOIL** (First, Outer, Inner, Last) lists the four products: $x \cdot x$, $x \cdot (-5)$, $3 \cdot x$, $3 \cdot (-5)$. In general
$$
(x + p)(x + q) = x^2 + (p + q)x + pq.
$$
Read that identity carefully: the **middle coefficient is the sum** of $p$ and $q$, and the **constant is their product**. This is the key to factoring.

### The three special products

> [!IMPORTANT]
> $$(a + b)^2 = a^2 + 2ab + b^2$$
> $$(a - b)^2 = a^2 - 2ab + b^2$$
> $$(a + b)(a - b) = a^2 - b^2$$

Each one is FOIL with a pattern. In $(a + b)^2 = (a + b)(a + b)$ the outer and inner products are both $ab$, so they add to $2ab$. In $(a + b)(a - b)$ they are $-ab$ and $+ab$, so they cancel, leaving the **difference of squares**.

> [!WARNING]
> $(a + b)^2 \ne a^2 + b^2$. The cross term $2ab$ is the most commonly forgotten piece of algebra on the GMAT, and answer choices are built from it. Test: $(3 + 4)^2 = 49$, but $3^2 + 4^2 = 25$.

The GMAT rarely shows these identities openly. Learn to **spot them in disguise**:

- **Given a sum and a product.** If $a + b = 7$ and $ab = 6$, then $a^2 + b^2 = (a + b)^2 - 2ab = 49 - 12 = 37$. You never find $a$ and $b$.
- **Given a sum and a difference.** If $x + y = 12$ and $x - y = 4$, then $x^2 - y^2 = (x + y)(x - y) = 48$.
- **Mental arithmetic.** $201 \times 199 = (200 + 1)(200 - 1) = 40{,}000 - 1 = 39{,}999$, and $98^2 = (100 - 2)^2 = 10{,}000 - 400 + 4 = 9{,}604$.
- **Reciprocals.** $\left(x + \dfrac1x\right)^2 = x^2 + 2 + \dfrac{1}{x^2}$, because the cross term is $2 \cdot x \cdot \tfrac1x = 2$.
- **Perfect squares in disguise.** $4x^2 + 12x + 9 = (2x)^2 + 2(2x)(3) + 3^2 = (2x + 3)^2$.
- **Repeated difference of squares.** $x^4 - 16 = (x^2 - 4)(x^2 + 4) = (x - 2)(x + 2)(x^2 + 4)$.

> [!TIP]
> When you see $x^2 - y^2$, $a^2 + b^2$, or $(\text{something})^2$ in a question, ask: "which special product is this?" before doing anything else. If the question gives you $x + y$, $x - y$ or $xy$, it is almost certainly a special-product question.

### Factoring trinomials

**When $a = 1$.** To factor $x^2 + bx + c$, find two numbers with **product $c$** and **sum $b$**. For $x^2 - 2x - 15$: the product is negative, so the numbers have opposite signs; the sum is $-2$, so the larger one is negative. The pair is $3$ and $-5$, giving $(x + 3)(x - 5)$.

Sign shortcuts: if $c > 0$, the two numbers share the sign of $b$. If $c < 0$, they have opposite signs, and the one with the larger absolute value has the sign of $b$.

**When $a \ne 1$ (the "ac method").** To factor $2x^2 - 5x - 12$:

1. Multiply $a \cdot c = 2 \cdot (-12) = -24$.
2. Find two numbers with product $-24$ and sum $-5$: $-8$ and $3$.
3. Split the middle term: $2x^2 - 8x + 3x - 12$.
4. Factor in pairs: $2x(x - 4) + 3(x - 4) = (2x + 3)(x - 4)$.

Always check by expanding: $(2x + 3)(x - 4) = 2x^2 - 8x + 3x - 12$. ✓

Two other first moves are worth trying before anything else:

- **Take out a common factor.** $3x^2 - 12 = 3(x^2 - 4) = 3(x - 2)(x + 2)$.
- **Higher powers.** $x^3 - x = x(x^2 - 1) = (x - 1)x(x + 1)$, a product of three consecutive integers when $x$ is an integer, so it is always divisible by 6. (See [Divisibility, primes and factors](../../arithmetic/divisibility-primes-and-factors/).)

### Solving by factoring: the zero-product rule

If a product is zero, at least one factor is zero: $PQ = 0 \Rightarrow P = 0$ or $Q = 0$. This is the only reason factoring solves equations, and it works **only when one side is 0**.

To solve $2x^2 - 5x = 12$, first move everything to one side: $2x^2 - 5x - 12 = 0$. Then factor: $(2x + 3)(x - 4) = 0$, so $x = -\tfrac32$ or $x = 4$.

> [!WARNING]
> $(x - 2)(x + 1) = 4$ does **not** mean $x - 2 = 4$ or $x + 1 = 4$. Only zero has the property that a product equal to it forces a factor to equal it. Expand, move the 4 across, and factor again: $x^2 - x - 6 = 0$, so $(x - 3)(x + 2) = 0$.

### The divide-by-a-variable trap

Consider $x(x - 5) = 3(x - 5)$. It is tempting to divide both sides by $x - 5$ and conclude $x = 3$. But dividing by $x - 5$ is only legal if $x - 5 \ne 0$, and $x = 5$ is in fact a solution: both sides are 0. The safe method:
$$
x(x - 5) - 3(x - 5) = 0 \;\Rightarrow\; (x - 5)(x - 3) = 0 \;\Rightarrow\; x = 5 \text{ or } x = 3.
$$

> [!WARNING]
> **Never divide both sides by an expression containing the variable** unless you know it is non-zero. Move everything to one side and factor instead. In Data Sufficiency, the lost root is often the whole point: $x^2 = 4x$ does **not** tell you $x = 4$, because $x = 0$ also works.

### The quadratic formula and the discriminant

Not every quadratic factors nicely. Completing the square solves all of them. Start from $ax^2 + bx + c = 0$, divide by $a$, and add the square of half the $x$ coefficient to both sides:
$$
x^2 + \frac ba x = -\frac ca \;\Rightarrow\; \left(x + \frac{b}{2a}\right)^2 = \frac{b^2}{4a^2} - \frac ca = \frac{b^2 - 4ac}{4a^2}.
$$
Taking square roots gives the formula.

> [!IMPORTANT]
> **Quadratic formula.** The solutions of $ax^2 + bx + c = 0$ are
> $$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}.$$
> The **discriminant** $D = b^2 - 4ac$ counts the real solutions: two if $D > 0$, exactly one (a "double root") if $D = 0$, none if $D < 0$.

The derivation explains the discriminant: the right side of the last line is a square, so it cannot be negative. If $b^2 - 4ac < 0$, there is no real $x$.

On the GMAT you rarely need the full formula, because the numbers are designed to factor. You do need the **discriminant**, typically in questions like "for which $k$ does $x^2 + kx + 16 = 0$ have exactly one solution?" Set $k^2 - 4 \cdot 16 = 0$, so $k = \pm 8$. (Check: $x^2 + 8x + 16 = (x + 4)^2$, a perfect square.)

### Sum and product of the roots (Vieta's formulas)

If $r$ and $s$ are the roots of $ax^2 + bx + c = 0$, the quadratic factors as $a(x - r)(x - s) = a\left(x^2 - (r + s)x + rs\right)$. Matching coefficients with $ax^2 + bx + c$:

> [!IMPORTANT]
> $$r + s = -\frac ba, \qquad rs = \frac ca.$$
> For $x^2 + bx + c$ (with $a = 1$): the roots add to $-b$ and multiply to $c$.

This answers questions about the roots **without** finding them. For $x^2 - 6x + 4 = 0$, the roots are $3 \pm \sqrt5$, which are awkward. But $r + s = 6$ and $rs = 4$, so $r^2 + s^2 = (r + s)^2 - 2rs = 36 - 8 = 28$. Equally, if you are told that one root of $x^2 + bx - 24 = 0$ is 3, the product of the roots is $-24$, so the other root is $-8$ and $b = -(3 + (-8)) = 5$.

> [!TIP]
> If a question gives you one root and asks about a coefficient, **plug the root in**: $3^2 + 3b - 24 = 0$ gives $b = 5$ at once. If it asks about a symmetric expression of both roots ($r + s$, $rs$, $r^2 + s^2$, $\tfrac1r + \tfrac1s$), use Vieta's formulas instead of solving.

### Quadratic inequalities: sign analysis

To solve $x^2 - 2x - 15 < 0$:

1. **Factor**, with 0 on one side: $(x - 5)(x + 3) < 0$.
2. **Mark the critical points** where each factor is zero: $x = -3$ and $x = 5$. They split the number line into three regions.
3. **Find the sign in each region.** A product is negative when exactly one factor is negative.

| Region | $x + 3$ | $x - 5$ | Product |
|---|---|---|---|
| $x < -3$ | $-$ | $-$ | $+$ |
| $-3 < x < 5$ | $+$ | $-$ | $-$ |
| $x > 5$ | $+$ | $+$ | $+$ |

So the solution is $-3 < x < 5$.

The picture behind this: $y = x^2 - 2x - 15$ is an upward-opening parabola (positive $x^2$ coefficient) that crosses zero at $-3$ and $5$. It is **below** zero between the roots and **above** zero outside them.

> [!TIP]
> For an upward-opening parabola: **"less than 0" means between the roots; "greater than 0" means outside the roots.** If you forget which, test $x = 0$ (or any easy point) in the original inequality.

> [!WARNING]
> Do not "square-root both sides" of an inequality. $x^2 < 9$ is **not** $x < 3$: it is $-3 < x < 3$. And $x^2 > 9$ is $x < -3$ **or** $x > 3$. More on this in [Inequalities and absolute value](../../algebra/inequalities-and-absolute-value/).

### Algebraic fractions

An **algebraic fraction** is a ratio of polynomials. The rules are those of ordinary fractions:

- **Simplify** by factoring the numerator and denominator and cancelling **common factors**:
  $$\frac{x^2 - 9}{x^2 + x - 6} = \frac{(x - 3)(x + 3)}{(x + 3)(x - 2)} = \frac{x - 3}{x - 2}, \quad x \ne -3,\ x \ne 2.$$
  The cancelled factor still matters: the original expression is undefined at $x = -3$, so $x = -3$ can never be an answer.
- **Add or subtract** over a common denominator:
  $$\frac{2}{x - 1} - \frac{2}{x + 1} = \frac{2(x + 1) - 2(x - 1)}{(x - 1)(x + 1)} = \frac{4}{x^2 - 1}.$$

> [!WARNING]
> Cancel **factors**, never **terms**. $\dfrac{x^2 + 9}{x + 3}$ does not simplify to $x + 3$ (try $x = 1$: $\tfrac{10}{4} \ne 4$), and $\dfrac{x + 6}{x}$ is not $6$. If the numerator and denominator do not factor with a common factor, nothing cancels.

## Worked examples

**Example 1** *(Easy)*. If $x + y = 12$ and $x - y = 4$, what is the value of $x^2 - y^2$?

- (A) 16
- (B) 32
- (C) 48
- (D) 64
- (E) 144

*Solution.* $x^2 - y^2 = (x + y)(x - y) = 12 \times 4 = 48$. **Answer: (C).** You could also solve ($x = 8$, $y = 4$, $64 - 16 = 48$), but spotting the difference of squares is faster. (E) is $(x + y)^2$; (A) is $(x - y)^2$.

**Example 2** *(Medium)*. If $2x^2 - 5x = 12$ and $x > 0$, what is the value of $x$?

- (A) $\tfrac32$
- (B) 2
- (C) 3
- (D) 4
- (E) 6

*Solution.* Set one side to zero: $2x^2 - 5x - 12 = 0$. Factor with the ac method (product $-24$, sum $-5$: the numbers $-8$ and $3$): $(2x + 3)(x - 4) = 0$. The roots are $-\tfrac32$ and $4$; the positive one is 4. **Answer: (D).**

*Backsolving:* $x = 4$ gives $32 - 20 = 12$. ✓ Choice (A) is the absolute value of the negative root, built for students who mix up the signs in the factors.

**Example 3** *(Medium)*. The two roots of $x^2 - 6x + 4 = 0$ are $r$ and $s$. What is the value of $r^2 + s^2$?

- (A) 20
- (B) 28
- (C) 32
- (D) 36
- (E) 44

*Solution.* By Vieta, $r + s = 6$ and $rs = 4$. Then
$$
r^2 + s^2 = (r + s)^2 - 2rs = 36 - 8 = 28.
$$
**Answer: (B).** The distractors come from errors in the identity: (D) is $(r + s)^2$ alone, (C) subtracts $rs$ instead of $2rs$, and (E) adds $2rs$. Solving directly gives $r, s = 3 \pm \sqrt5$, and $(3 + \sqrt5)^2 + (3 - \sqrt5)^2 = 14 + 14 = 28$: correct, but slower.

**Example 4** *(Hard)*. How many integers $x$ satisfy $x^2 - 2x - 15 < 0$?

- (A) 5
- (B) 6
- (C) 7
- (D) 8
- (E) 9

*Solution.* Factor: $(x - 5)(x + 3) < 0$. The parabola opens upward, so it is negative strictly between its roots: $-3 < x < 5$. The integers are $-2, -1, 0, 1, 2, 3, 4$: seven of them. **Answer: (C).** (E) wrongly includes the endpoints $-3$ and $5$, where the expression equals 0, which is not less than 0.

*Counting tip:* the number of integers strictly between two integers $m < n$ is $n - m - 1 = 5 - (-3) - 1 = 7$.

**Example 5** *(Hard)*. If $\dfrac{x^2 - 9}{x^2 + x - 6} = 2$, what is the value of $x$?

- (A) $-3$
- (B) $-1$
- (C) 1
- (D) 2
- (E) 3

*Solution.* Factor and cancel: $\dfrac{(x - 3)(x + 3)}{(x + 3)(x - 2)} = \dfrac{x - 3}{x - 2}$, valid for $x \ne -3$ and $x \ne 2$. Solve $\dfrac{x - 3}{x - 2} = 2$: $x - 3 = 2x - 4$, so $x = 1$. It is not excluded, so it stands. **Answer: (C).**

*Check:* at $x = 1$, $\dfrac{1 - 9}{1 + 1 - 6} = \dfrac{-8}{-4} = 2$. ✓ Choice (A) is a trap: $x = -3$ makes the original denominator zero, so it is never a valid answer, even though it appears when you "solve" carelessly by cross-multiplying, getting $x^2 - 9 = 2x^2 + 2x - 12$, that is $x^2 + 2x - 3 = 0$, with roots $1$ and $-3$.

## Practice

Data Sufficiency items use the fixed answer choices explained in [The data sufficiency method](../../data-sufficiency/the-data-sufficiency-method/): **(A)** statement (1) alone is sufficient, but (2) alone is not; **(B)** (2) alone is sufficient, but (1) alone is not; **(C)** both together are sufficient, but neither alone is; **(D)** each alone is sufficient; **(E)** the statements together are not sufficient.

**1.** *(Easy)* If $(a + b)^2 = 49$ and $ab = 6$, what is the value of $a^2 + b^2$?

- (A) 25
- (B) 31
- (C) 37
- (D) 43
- (E) 55

<details>
<summary>Answer</summary>

$(a + b)^2 = a^2 + 2ab + b^2$, so $a^2 + b^2 = 49 - 2(6) = 37$. **(C)**. (D) subtracts $ab$ once instead of $2ab$. (For instance $a = 1$, $b = 6$: $1 + 36 = 37$. ✓)

</details>

**2.** *(Easy)* What is the value of $201 \times 199$?

- (A) 39,601
- (B) 39,999
- (C) 40,000
- (D) 40,001
- (E) 40,401

<details>
<summary>Answer</summary>

$(200 + 1)(200 - 1) = 200^2 - 1^2 = 40{,}000 - 1 = 39{,}999$. **(B)**. (A) is $199^2$ and (E) is $201^2$.

</details>

**3.** *(Medium)* What is the sum of all values of $x$ that satisfy $x(x - 5) = 3(x - 5)$?

- (A) $-2$
- (B) 3
- (C) 5
- (D) 8
- (E) 15

<details>
<summary>Answer</summary>

Do not divide by $x - 5$. Move everything to one side: $(x - 5)(x - 3) = 0$, so $x = 5$ or $x = 3$. The sum is 8. **(D)**. Dividing by $x - 5$ loses the root 5 and leads to (B).

</details>

**4.** *(Medium)* If $k > 0$ and the equation $x^2 + kx + 16 = 0$ has exactly one solution, what is the value of $k$?

- (A) 4
- (B) 8
- (C) 16
- (D) 32
- (E) 64

<details>
<summary>Answer</summary>

Exactly one solution means the discriminant is zero: $k^2 - 4(1)(16) = 0$, so $k^2 = 64$ and, since $k > 0$, $k = 8$. **(B)**. Check: $x^2 + 8x + 16 = (x + 4)^2$, which is zero only at $x = -4$. (E) is $k^2$.

</details>

**5.** *(Medium)* Which of the following is a factor of $3x^2 + 10x - 8$?

- (A) $x - 4$
- (B) $3x + 2$
- (C) $3x - 2$
- (D) $x + 2$
- (E) $3x + 4$

<details>
<summary>Answer</summary>

ac method: $3 \times (-8) = -24$; two numbers with product $-24$ and sum $10$ are $12$ and $-2$. Split: $3x^2 + 12x - 2x - 8 = 3x(x + 4) - 2(x + 4) = (3x - 2)(x + 4)$. **(C)**. (A) and (B) have the right numbers but the wrong signs; always check by expanding.

</details>

**6.** *(Medium)* For $x \ne \pm 1$, which of the following is equal to $\dfrac{2}{x - 1} - \dfrac{2}{x + 1}$?

- (A) 0
- (B) $\dfrac{4}{x^2 - 1}$
- (C) $\dfrac{4x}{x^2 - 1}$
- (D) $\dfrac{-4}{x^2 - 1}$
- (E) $\dfrac{2}{x^2 - 1}$

<details>
<summary>Answer</summary>

Common denominator $(x - 1)(x + 1) = x^2 - 1$. Numerator: $2(x + 1) - 2(x - 1) = 2x + 2 - 2x + 2 = 4$. So the result is $\dfrac{4}{x^2 - 1}$. **(B)**. (A) comes from writing $-2(x - 1) = -2x - 2$. *Picking numbers:* $x = 3$ gives $1 - \tfrac12 = \tfrac12$, and $\tfrac48 = \tfrac12$. ✓

</details>

**7.** *(Medium)* The product of two consecutive positive even integers is 168. What is their sum?

- (A) 22
- (B) 24
- (C) 26
- (D) 28
- (E) 30

<details>
<summary>Answer</summary>

Let the integers be $n$ and $n + 2$: $n(n + 2) = 168$, so $n^2 + 2n - 168 = 0$, which factors as $(n + 14)(n - 12) = 0$. Since $n > 0$, $n = 12$, and the integers are 12 and 14, with sum 26. **(C)**.

*Faster:* two numbers that differ by 2 and multiply to 168 lie on either side of $\sqrt{168} \approx 13$, so try 12 and 14: $12 \times 14 = 168$. ✓

</details>

**8.** *(Medium, Data Sufficiency)* What is the value of $x^2 - y^2$?

(1) $x + y = 0$

(2) $x - y = 6$

<details>
<summary>Answer</summary>

$x^2 - y^2 = (x + y)(x - y)$.

(1): the first factor is 0, so $x^2 - y^2 = 0$ whatever $x - y$ is. Sufficient.

(2): $x^2 - y^2 = 6(x + y)$, which depends on $x + y$. For example $(6, 0)$ gives 36 and $(3, -3)$ gives 0. Not sufficient.

**(A)**. The trap is (C): "I need both factors". When one factor is zero, you do not.

</details>

**9.** *(Hard)* If $x + \dfrac1x = 5$, what is the value of $x^2 + \dfrac{1}{x^2}$?

- (A) 10
- (B) 21
- (C) 23
- (D) 25
- (E) 27

<details>
<summary>Answer</summary>

Square both sides: $x^2 + 2 \cdot x \cdot \tfrac1x + \tfrac{1}{x^2} = 25$, that is $x^2 + 2 + \tfrac{1}{x^2} = 25$. So $x^2 + \tfrac{1}{x^2} = 23$. **(C)**. (D) forgets the cross term, and (E) adds it instead of subtracting.

</details>

**10.** *(Hard)* One root of $x^2 + bx - 24 = 0$ is 3. What is the value of $b$?

- (A) $-5$
- (B) $-3$
- (C) 3
- (D) 5
- (E) 8

<details>
<summary>Answer</summary>

*Plugging in:* $9 + 3b - 24 = 0$, so $b = 5$. **(D)**.

*Vieta:* the roots multiply to $-24$, so the other root is $-8$. They add to $-b$: $3 + (-8) = -5 = -b$, so $b = 5$. (A) forgets the minus sign in "sum $= -b$". (E) is the absolute value of the other root.

</details>

**11.** *(Hard)* Which of the following describes all values of $x$ for which $x^2 > 4x + 12$?

- (A) $-2 < x < 6$
- (B) $x > 6$
- (C) $x < -2$ or $x > 6$
- (D) $x < -6$ or $x > 2$
- (E) $-6 < x < 2$

<details>
<summary>Answer</summary>

Move everything to one side: $x^2 - 4x - 12 > 0$, that is $(x - 6)(x + 2) > 0$. An upward parabola is positive **outside** its roots $-2$ and $6$: $x < -2$ or $x > 6$. **(C)**. (A) is the "less than" region; (B) forgets the negative branch; (D) and (E) flip the signs of the roots. *Test a value:* $x = -3$ gives $9 > 0$, true, which rules out (A), (B) and (D).

</details>

**12.** *(Hard, Data Sufficiency)* What is the value of $x$?

(1) $x^2 - 7x + 12 = 0$

(2) $x^2 = 9$

<details>
<summary>Answer</summary>

(1): $(x - 3)(x - 4) = 0$, so $x = 3$ or $4$. Not sufficient.

(2): $x = 3$ or $-3$. Not sufficient.

Together: the only value in both lists is $x = 3$. Sufficient. **(C)**.

</details>

> [!NOTE]
> If you use Claude Code, the `quantome-math` plugin (`/plugin install quantome-math@quantome`) can check your factoring after you have done it by hand. Build the skill first: the GMAT has no calculator.

## Takeaways

- Know $(a \pm b)^2$ and $(a + b)(a - b)$ in both directions, and look for them whenever a question gives $x + y$, $x - y$ or $xy$.
- Factor $x^2 + bx + c$ by finding two numbers with product $c$ and sum $b$; use the ac method when $a \ne 1$; always check by expanding.
- The zero-product rule needs **zero** on one side. Never divide by an expression that might be zero: factor it out instead.
- Discriminant $b^2 - 4ac$: positive means two roots, zero means one, negative means none.
- Sum of roots $-b/a$, product $c/a$: answer root questions without finding the roots.
- Upward parabola: less than 0 between the roots, greater than 0 outside them.
- Cancel factors, never terms; a cancelled factor still excludes its root from the answer.

## Further reading

- GMAC, *GMAT Official Guide* (current edition) and the *GMAT Official Guide Quantitative Review*: real retired questions for timed practice of these patterns.
- In this book: [Linear equations and systems](../../algebra/linear-equations/), [Exponents and roots](../../algebra/exponents-and-roots/) (quadratics in disguise), [Inequalities and absolute value](../../algebra/inequalities-and-absolute-value/) and [Data sufficiency by topic](../../data-sufficiency/data-sufficiency-by-topic/).
