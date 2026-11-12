+++
summary = "Solve linear equations and systems quickly, target the combination a question asks for, and recognise when a system has no unique solution."
+++

# Linear Equations & Systems

Linear equations are the plumbing of GMAT Quant. Almost every word problem, from ticket sales to mixtures to ages, ends with one or two linear equations, and many Data Sufficiency questions are really asking, "do these equations pin the unknown down?" You already know how to solve $2x + 3 = 11$. This chapter is about doing it **fast and safely**, and about the strategic questions the GMAT actually tests: Which combination is being asked for? Do I even need to solve? Is the system secretly one equation in disguise?

If you need to turn a story into equations first, see [Translating words into equations](../../word-problems/translating-words-into-equations/). Here we assume the equations are on the page.

## Key ideas

### One equation, one unknown: the balance

An equation is a balance. Whatever you do to one side, you must do to the other, and the balance stays true. To solve a **linear** equation (every variable to the first power, no variable in a denominator), you undo the operations around the variable, in reverse order:

1. **Clear fractions** by multiplying every term by the least common denominator (LCD).
2. **Expand brackets**, taking care with minus signs in front of them.
3. **Collect** the variable terms on one side and the constants on the other.
4. **Divide** by the coefficient of the variable.

For example, with $\dfrac{x}{2} - \dfrac{x - 1}{3} = 2$, multiply every term by 6: $3x - 2(x - 1) = 12$. Expand: $3x - 2x + 2 = 12$. So $x = 10$.

Why is step 1 safe? Multiplying both sides by a **non-zero** number gives an equivalent equation: you can always divide back. Multiplying by zero (or by something that might be zero, such as a variable) is not reversible, and that is where errors come from. We return to this in the traps section.

> [!WARNING]
> The most common arithmetic error on linear equations is a **minus sign in front of a bracket or fraction**. $-\dfrac{x - 1}{3}$ means $-\tfrac13(x - 1) = -\tfrac{x}{3} + \tfrac13$. When you clear the denominator, the whole numerator is negated: $-2(x - 1) = -2x + 2$, not $-2x - 2$. Wrong answer choices are built from exactly this slip.

### Two equations, two unknowns

A linear equation in $x$ and $y$ describes a straight line. A **solution of a system** is a point on both lines, so two lines can give:

- **exactly one** solution (the lines cross),
- **no** solution (the lines are parallel and distinct),
- **infinitely many** solutions (the two equations describe the same line).

There are two standard methods.

**Substitution.** Solve one equation for one variable and substitute into the other. Best when a variable already has coefficient 1 or $-1$, for example $x + y = 50$ gives $y = 50 - x$ at once.

**Elimination.** Multiply the equations by suitable numbers so that one variable has opposite coefficients, then add. For
$$
3x + 2y = 16, \qquad 5x - 4y = 12,
$$
double the first to get $6x + 4y = 32$ and add: $11x = 44$, so $x = 4$ and $y = 2$. Elimination is usually faster on the GMAT, because the coefficients are often chosen to make it clean.

Why is elimination legal? If two equations are both true, then any sum of multiples of them is also true: you are adding equal amounts to both sides of a balance. As long as you keep enough independent equations, you lose no information.

### Combination questions: solve for what is asked

The GMAT loves to ask for $x + y$, $x - y$, $2a + b$ or $\dfrac{p}{q}$ instead of the individual unknowns. Very often you can get the combination directly, with less work and fewer chances to slip.

- **Symmetric coefficients.** If $7x + 3y = 41$ and $3x + 7y = 29$, adding gives $10x + 10y = 70$, so $x + y = 7$; subtracting gives $4x - 4y = 12$, so $x - y = 3$.
- **The target is a multiple of an equation.** If $4a + 6b = 18$, then $2a + 3b = 9$ immediately, without knowing $a$ or $b$.

The general method: you want numbers $p$ and $q$ such that $p \times (\text{equation 1}) + q \times (\text{equation 2})$ has exactly the coefficients of the target. Match coefficients and solve for $p$ and $q$. This is the key to the next idea.

> [!TIP]
> Before solving any system, look at **what the question asks for**. Add the equations, subtract them, or scale one. If the target appears in one or two moves, stop there. On test day, solving for $x$ and $y$ separately when the question wants $x + y$ costs time and adds steps where you can slip.

### Three unknowns, two equations: when only a combination is determined

Two equations in three unknowns normally have **infinitely many** solutions, so you cannot find $x$, $y$ and $z$ individually. But some combinations may still be fixed. Take
$$
x + 2y + 3z = 20, \qquad 3x + 4y + 5z = 34.
$$
Is $x + y + z$ determined? Look for $p, q$ with $p(1, 2, 3) + q(3, 4, 5) = (1, 1, 1)$:
$$
p + 3q = 1, \quad 2p + 4q = 1, \quad 3p + 5q = 1.
$$
The first two give $q = \tfrac12$, $p = -\tfrac12$, and these also satisfy the third. So $x + y + z = \tfrac12(34) - \tfrac12(20) = 7$, even though $x$, $y$ and $z$ are not individually determined.

If no $p$ and $q$ satisfy all three coefficient equations, the combination is **not** determined: different solutions of the system give different values. In Data Sufficiency this is the whole question. "Can I build the target from the equations I have?" is exactly "Is the information sufficient?"

> [!TIP]
> In word problems this looks like: "3 pens, 2 notebooks and a folder cost \$13; 5 pens, 3 notebooks and a folder cost \$19. What do one pen, one notebook and one folder cost?" You cannot price each item, but $2 \times (\text{first}) - (\text{second})$ gives the answer. Spot it by looking at the coefficients: you need $(1, 1, 1)$.

### No solution or infinitely many

For a $2 \times 2$ system
$$
a_1 x + b_1 y = c_1, \qquad a_2 x + b_2 y = c_2,
$$
compare the ratios of the coefficients.

> [!IMPORTANT]
> - If $\dfrac{a_1}{a_2} \ne \dfrac{b_1}{b_2}$: exactly **one** solution (the lines have different slopes).
> - If $\dfrac{a_1}{a_2} = \dfrac{b_1}{b_2} \ne \dfrac{c_1}{c_2}$: **no** solution (parallel lines).
> - If $\dfrac{a_1}{a_2} = \dfrac{b_1}{b_2} = \dfrac{c_1}{c_2}$: **infinitely many** solutions (the same line).

The reason: if the $x$ and $y$ coefficients are in the same ratio, one equation's left side is a multiple of the other's, say $2(x + 2y)$ and $x + 2y$. Then either the right sides are in the same ratio (the equations say the same thing) or they contradict each other ($x + 2y = 5$ and $x + 2y = 6$ cannot both hold). If a coefficient is zero, use the cross-multiplied form $a_1 b_2 = a_2 b_1$ instead of dividing.

> [!WARNING]
> "Two equations, two unknowns, so it is solvable" is the single most expensive myth in Data Sufficiency. The equations might be the same line ($x + 2y = 3$ and $2x + 4y = 6$), which gives infinitely many solutions. And the reverse also fails: a **single** equation can be sufficient if it pins down the combination the question asks for, or if the unknowns are restricted, for example to positive integers.

### Literal equations: solving for one letter

A **literal equation** is a formula with several letters, such as $d = rt$ or $\dfrac1a + \dfrac1b = \dfrac1c$. "Solve for $b$" means isolate $b$ using the same moves as before, treating the other letters as numbers.

For $\dfrac1a + \dfrac1b = \dfrac1c$, isolate the $b$ term first: $\dfrac1b = \dfrac1c - \dfrac1a = \dfrac{a - c}{ac}$, then flip both sides: $b = \dfrac{ac}{a - c}$.

When the target letter appears in **two places**, gather those terms on one side and factor it out. For $y = \dfrac{2x + 1}{x - 3}$: multiply by $x - 3$ to get $xy - 3y = 2x + 1$, collect $xy - 2x = 3y + 1$, factor $x(y - 2) = 3y + 1$, and divide: $x = \dfrac{3y + 1}{y - 2}$.

> [!TIP]
> **Pick numbers** to check literal-equation answer choices. Choose values that make the original equation easy, compute the target letter, then test each choice. In the example above, $x = 4$ gives $y = 9$. Plug $y = 9$ into each choice and keep the one that returns 4. Avoid 0 and 1 and avoid making two letters equal, because those values make different expressions agree by accident.

### Manipulation traps

Most wrong answers on algebra questions are not random; they come from a small set of illegal moves.

- **Dividing by a variable.** From $x(x - 4) = 3x$, dividing by $x$ gives $x - 4 = 3$, so $x = 7$, but $x = 0$ is also a solution. Dividing by an expression is only safe when you know it is not zero. (Quadratics are covered in [Quadratics and polynomials](../../algebra/quadratics-and-polynomials/).)
- **Cancelling a factor that could be zero.** $\dfrac{x + 2}{x - 1} = \dfrac{2x + 1}{x - 1}$ seems to give $x + 2 = 2x + 1$, so $x = 1$. But $x = 1$ makes the denominators zero. There is **no** solution.
- **Distributing incorrectly.** $-(3 - x) = -3 + x$, and $2(x + 3) = 2x + 6$, not $2x + 3$.
- **Cancelling terms instead of factors.** $\dfrac{x + 6}{3}$ is not $x + 2$. Only a factor of the whole numerator and the whole denominator can be cancelled.
- **Taking reciprocals of a sum.** $\dfrac1a + \dfrac1b \ne \dfrac{1}{a + b}$. Combine over a common denominator first.

> [!TIP]
> **Backsolving.** When the answer choices are numbers and the equation is messy, plug the choices in. Start with (C): if it is too big or too small, that often tells you which direction to move, so you test at most two or three choices.

## Worked examples

**Example 1** *(Easy)*. If $\dfrac{3x - 1}{4} - \dfrac{x + 3}{6} = 1$, what is the value of $x$?

- (A) $\tfrac97$
- (B) $\tfrac{15}{7}$
- (C) $3$
- (D) $\tfrac{21}{5}$
- (E) $6$

*Solution.* The LCD of 4 and 6 is 12. Multiply every term by 12:
$$
3(3x - 1) - 2(x + 3) = 12 \;\Rightarrow\; 9x - 3 - 2x - 6 = 12 \;\Rightarrow\; 7x = 21 \;\Rightarrow\; x = 3.
$$
**Answer: (C).** Choice (A) is what you get if you write $-2(x + 3) = -2x + 6$: then $7x + 3 = 12$ and $x = \tfrac97$. *Fast check:* at $x = 3$ the left side is $\tfrac84 - \tfrac66 = 2 - 1 = 1$. ✓

**Example 2** *(Medium)*. A café sells small coffees for \$3 and large coffees for \$5. One morning it sold 84 coffees for a total of \$332. How many large coffees did it sell?

- (A) 36
- (B) 40
- (C) 44
- (D) 48
- (E) 52

*Textbook method.* Let $s$ and $\ell$ be the numbers of small and large coffees. Then $s + \ell = 84$ and $3s + 5\ell = 332$. Substitute $s = 84 - \ell$: $252 - 3\ell + 5\ell = 332$, so $2\ell = 80$ and $\ell = 40$.

*Fast method.* If all 84 had been small, revenue would be $84 \times 3 = 252$. Each large coffee adds \$2 more, and the actual revenue is $332 - 252 = 80$ more, so there are $80 / 2 = 40$ large coffees. **Answer: (B).** Choice (C), 44, is the number of *small* coffees, a classic trap: always re-read which quantity is asked for.

**Example 3** *(Medium)*. If $x + 2y + 3z = 20$ and $3x + 4y + 5z = 34$, what is the value of $x + y + z$?

- (A) 5
- (B) 6
- (C) 7
- (D) 8
- (E) 9

*Solution.* Three unknowns and two equations, so you cannot find each variable, but you might find the combination. Subtract the first equation from the second: $2x + 2y + 2z = 14$, so $x + y + z = 7$. **Answer: (C).**

This is the $p = -\tfrac12$, $q = \tfrac12$ combination from the key ideas, found by noticing that the coefficients $(3, 4, 5)$ minus $(1, 2, 3)$ are $(2, 2, 2)$. Look for a quick difference or sum before setting up the general method.

**Example 4** *(Hard)*. For which value of $k$ does the system below have **no** solution?
$$
2x - 3y = 7, \qquad kx + 6y = 5
$$

- (A) $-4$
- (B) $-3$
- (C) $3$
- (D) $4$
- (E) $6$

*Solution.* No solution requires parallel lines: the coefficient ratios must match, $\dfrac{k}{2} = \dfrac{6}{-3} = -2$, so $k = -4$. Then check the constants: the second equation becomes $-4x + 6y = 5$, that is, $2x - 3y = -\tfrac52$, which contradicts $2x - 3y = 7$. So there is no solution. **Answer: (A).**

Two lessons. (D), $k = 4$, comes from ignoring the minus sign in $-3$. And had the second constant been $-14$ instead of 5, the same $k$ would give **infinitely many** solutions, because the second equation would be exactly $-2$ times the first. Always check the constants after matching the coefficients.

**Example 5** *(Hard)*. If $\dfrac1a + \dfrac1b = \dfrac1c$, where $a$, $b$, $c$ are non-zero and $a \ne c$, which of the following expresses $b$ in terms of $a$ and $c$?

- (A) $\dfrac{ac}{a - c}$
- (B) $\dfrac{ac}{c - a}$
- (C) $a - c$
- (D) $\dfrac{a - c}{ac}$
- (E) $\dfrac{ac}{a + c}$

*Algebra.* $\dfrac1b = \dfrac1c - \dfrac1a = \dfrac{a - c}{ac}$, so $b = \dfrac{ac}{a - c}$. **Answer: (A).**

*Picking numbers.* Let $a = 3$ and $c = 2$. Then $\dfrac1b = \dfrac12 - \dfrac13 = \dfrac16$, so $b = 6$. The choices give (A) 6, (B) $-6$, (C) 1, (D) $\tfrac16$, (E) $\tfrac65$. Only (A) matches. (B) is the sign slip from computing $\tfrac1a - \tfrac1c$; (D) forgets to take the reciprocal at the end.

## Practice

Data Sufficiency items use the fixed answer choices explained in [The data sufficiency method](../../data-sufficiency/the-data-sufficiency-method/): **(A)** statement (1) alone is sufficient, but (2) alone is not; **(B)** (2) alone is sufficient, but (1) alone is not; **(C)** both together are sufficient, but neither alone is; **(D)** each alone is sufficient; **(E)** the statements together are not sufficient.

**1.** *(Easy)* If $7 - 2(3 - x) = 4x - 9$, what is the value of $x$?

- (A) $-5$
- (B) 2
- (C) 4
- (D) 5
- (E) 8

<details>
<summary>Answer</summary>

Expand: $7 - 6 + 2x = 4x - 9$, so $1 + 2x = 4x - 9$, so $10 = 2x$ and $x = 5$. **(D)**. Check: left side $7 - 2(-2) = 11$; right side $20 - 9 = 11$. ✓

</details>

**2.** *(Easy)* If $3p - q = 14$ and $p + q = 10$, what is the value of $pq$?

- (A) 16
- (B) 21
- (C) 24
- (D) 28
- (E) 32

<details>
<summary>Answer</summary>

Add the equations to eliminate $q$: $4p = 24$, so $p = 6$ and $q = 10 - 6 = 4$. Then $pq = 24$. **(C)**.

</details>

**3.** *(Medium)* If $4m + 7n = 50$ and $7m + 4n = 49$, what is the value of $m + n$?

- (A) 7
- (B) 8
- (C) 9
- (D) 10
- (E) 11

<details>
<summary>Answer</summary>

The coefficients are symmetric, so add: $11m + 11n = 99$, so $m + n = 9$. **(C)**. There is no need to find $m$ and $n$ (which are not integers: $m = \tfrac{13}{3}$, $n = \tfrac{14}{3}$).

</details>

**4.** *(Medium)* A jar contains only nickels (5 cents) and dimes (10 cents): 37 coins worth \$2.75 in total. How many dimes are in the jar?

- (A) 15
- (B) 17
- (C) 18
- (D) 19
- (E) 22

<details>
<summary>Answer</summary>

Work in cents. If all 37 coins were nickels, they would be worth 185 cents. The actual value is 275 cents, which is 90 cents more, and each dime adds 5 cents more than a nickel. So there are $90 / 5 = 18$ dimes. **(C)**. (D), 19, is the number of nickels. Check: $19 \times 5 + 18 \times 10 = 95 + 180 = 275$. ✓

</details>

**5.** *(Medium)* Ana is now three times as old as Ben. In 8 years, Ana will be twice as old as Ben. How old is Ana now?

- (A) 16
- (B) 18
- (C) 24
- (D) 30
- (E) 32

<details>
<summary>Answer</summary>

Let Ben be $b$, so Ana is $3b$. In 8 years: $3b + 8 = 2(b + 8)$, so $3b + 8 = 2b + 16$ and $b = 8$. Ana is $24$. **(C)**. *Backsolving:* if Ana is 24, Ben is 8; in 8 years they are 32 and 16, and $32 = 2 \times 16$. ✓

</details>

**6.** *(Medium)* If $y = \dfrac{3x + 2}{x - 4}$ and $y \ne 3$, which of the following expresses $x$ in terms of $y$?

- (A) $\dfrac{4y + 2}{y - 3}$
- (B) $\dfrac{4y - 2}{y - 3}$
- (C) $\dfrac{4y + 2}{3 - y}$
- (D) $\dfrac{3y + 2}{y - 4}$
- (E) $\dfrac{y + 2}{y - 3}$

<details>
<summary>Answer</summary>

Multiply by $x - 4$: $xy - 4y = 3x + 2$. Collect the $x$ terms: $xy - 3x = 4y + 2$. Factor: $x(y - 3) = 4y + 2$, so $x = \dfrac{4y + 2}{y - 3}$. **(A)**.

*Picking numbers:* $x = 5$ gives $y = \tfrac{17}{1} = 17$. At $y = 17$, (A) gives $\tfrac{70}{14} = 5$ ✓, (B) $\tfrac{66}{14}$, (C) $-5$, (D) $\tfrac{53}{13}$, (E) $\tfrac{19}{14}$. (D) simply swaps the roles of $x$ and $y$, a tempting but wrong shortcut.

</details>

**7.** *(Medium, Data Sufficiency)* What is the value of $x + y + z$?

(1) $x + 2y + 3z = 14$

(2) $3x + 2y + z = 10$

<details>
<summary>Answer</summary>

(1) alone: one equation in three unknowns. For example $(x, y, z) = (14, 0, 0)$ gives a sum of 14, and $(0, 7, 0)$ gives 7. Not sufficient.

(2) alone: $(\tfrac{10}{3}, 0, 0)$ gives $\tfrac{10}{3}$, and $(0, 0, 10)$ gives 10. Not sufficient.

Together: add the equations: $4x + 4y + 4z = 24$, so $x + y + z = 6$. Note that the individual values are still not determined (for example $(1, 2, 3)$ and $(2, 0, 4)$ both satisfy both equations), but the sum is. **(C)**.

</details>

**8.** *(Hard)* At a stationery shop, 3 pens, 2 notebooks and 1 folder cost \$13 in total, and 5 pens, 3 notebooks and 1 folder cost \$19 in total. What is the total cost of 1 pen, 1 notebook and 1 folder?

- (A) \$5
- (B) \$6
- (C) \$7
- (D) \$8
- (E) It cannot be determined from the information given.

<details>
<summary>Answer</summary>

Let the prices be $p$, $n$, $f$. We need $\alpha(3, 2, 1) + \beta(5, 3, 1) = (1, 1, 1)$. From the last coordinate, $\alpha + \beta = 1$; from the second, $2\alpha + 3\beta = 1$. So $\beta = -1$, $\alpha = 2$, and the first coordinate checks: $6 - 5 = 1$. ✓

Therefore $p + n + f = 2(13) - 19 = 7$. **(C)**. The individual prices are not determined (for example \$1, \$4, \$2 works, and so do other combinations), which is why (E) tempts people, but the combination is fixed.

</details>

**9.** *(Hard)* The system $ax + 4y = 6$ and $3x + 2y = b$ has infinitely many solutions $(x, y)$. What is the value of $a + b$?

- (A) 5
- (B) 6
- (C) 8
- (D) 9
- (E) 12

<details>
<summary>Answer</summary>

Infinitely many solutions means the first equation is a multiple of the second. The $y$ coefficients show the multiple is $4 / 2 = 2$. So $a = 2 \times 3 = 6$ and $6 = 2b$, giving $b = 3$. Then $a + b = 9$. **(D)**.

</details>

**10.** *(Hard, Data Sufficiency)* What is the value of $k$?

(1) The system $x + 2y = 5$, $3x + ky = 12$ has no solution.

(2) $k^2 = 36$

<details>
<summary>Answer</summary>

(1): a $2 \times 2$ system fails to have a unique solution only when the coefficient ratios match: $\tfrac31 = \tfrac{k}{2}$, so $k = 6$. Check that $k = 6$ really gives *no* solution: $3x + 6y = 12$ means $x + 2y = 4$, contradicting $x + 2y = 5$. ✓ For every other $k$ there is exactly one solution. So (1) forces $k = 6$. Sufficient.

(2): $k = 6$ or $k = -6$. Not sufficient.

**(A)**.

</details>

**11.** *(Hard)* How many values of $x$ satisfy $\dfrac{x + 2}{x - 1} = \dfrac{2x + 1}{x - 1}$?

- (A) 0
- (B) 1
- (C) 2
- (D) 3
- (E) Infinitely many

<details>
<summary>Answer</summary>

Multiplying both sides by $x - 1$ gives $x + 2 = 2x + 1$, so $x = 1$. But $x = 1$ makes both denominators zero, so it is not allowed. Multiplying by $x - 1$ was only valid for $x \ne 1$, and the only candidate is $x = 1$. There is **no** solution. **(A)**. Choice (B) is the trap.

</details>

> [!NOTE]
> If you use Claude Code, the `quantome-math` plugin (`/plugin install quantome-math@quantome`) can check your algebra after you have worked a problem by hand. Do the work yourself first: the GMAT has no calculator.

## Takeaways

- Clear fractions first, and negate the **whole** numerator when a minus sign sits in front of a fraction.
- Read the question before solving: if it asks for $x + y$ or $2a + 3b$, add, subtract or scale the equations to get it directly.
- Two equations in three unknowns can still fix a combination. Find $p$ and $q$ that build the target's coefficients.
- Equal coefficient ratios mean the lines are parallel: no solution if the constants disagree, infinitely many if they agree.
- "Two equations, two unknowns" does not guarantee a unique solution, and one equation can sometimes be enough.
- Never divide by, or cancel, an expression that might be zero; check candidates against the original equation.
- For literal equations, gather every term with the target letter, factor it out, then divide; check the answer choices by picking numbers.

## Further reading

- GMAC, *GMAT Official Guide* (current edition) and the *GMAT Official Guide Quantitative Review*: the source of real retired GMAT questions. Use them to practise these patterns under timed conditions.
- In this book: [Translating words into equations](../../word-problems/translating-words-into-equations/), [Problem-solving strategies](../../getting-started/problem-solving-strategies/) (backsolving and picking numbers) and [Data sufficiency by topic](../../data-sufficiency/data-sufficiency-by-topic/).
