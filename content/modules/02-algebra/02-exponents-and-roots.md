+++
summary = "Use the exponent rules with understanding, simplify and rationalise roots, solve exponential equations by matching bases, and compare huge powers without a calculator."
+++

# Exponents & Roots

Exponent questions on the GMAT look intimidating, with numbers like $3^{30}$ or $\dfrac{12^5}{18^3}$, but they are designed so that you never compute a large power. Every one of them gives way to a handful of rules plus two habits: **rewrite with prime bases** and **factor out the common power**. This chapter derives each rule from the meaning of an exponent, so you can rebuild any rule you forget, and then shows the moves that turn monstrous expressions into one-digit answers.

## Key ideas

### What an exponent means, and where the rules come from

For a positive integer $n$, $a^n$ means $n$ copies of $a$ multiplied together: $a^4 = a \cdot a \cdot a \cdot a$. Every rule below is just **counting factors**.

- **Product rule.** $a^3 \cdot a^2 = (a\cdot a\cdot a)(a \cdot a) = a^5$. In general, $a^m a^n = a^{m+n}$: you add the counts.
- **Quotient rule.** $\dfrac{a^5}{a^2} = \dfrac{a\cdot a\cdot a\cdot a\cdot a}{a\cdot a} = a^3$. Cancelling removes 2 factors: $\dfrac{a^m}{a^n} = a^{m-n}$.
- **Power of a power.** $(a^3)^2 = a^3 \cdot a^3 = a^6$. You have $n$ groups of $m$ factors: $(a^m)^n = a^{mn}$.
- **Power of a product or quotient.** $(ab)^3 = ab \cdot ab \cdot ab = a^3 b^3$, and likewise $\left(\dfrac ab\right)^n = \dfrac{a^n}{b^n}$.

> [!IMPORTANT]
> **The exponent rules** (for $a, b \ne 0$)
> $$a^m a^n = a^{m+n} \qquad \frac{a^m}{a^n} = a^{m-n} \qquad (a^m)^n = a^{mn}$$
> $$(ab)^n = a^n b^n \qquad \left(\frac ab\right)^n = \frac{a^n}{b^n}$$
> $$a^0 = 1 \qquad a^{-n} = \frac{1}{a^n} \qquad a^{1/n} = \sqrt[n]{a} \qquad a^{m/n} = \left(\sqrt[n]{a}\right)^m = \sqrt[n]{a^m}$$

There are **no** rules for sums. $a^m + a^n$ does not simplify to a single power, and $(a + b)^n \ne a^n + b^n$: for instance $(1 + 2)^2 = 9$, but $1^2 + 2^2 = 5$. When you see a sum of powers, the move is to **factor**, as shown below.

### Zero, negative and fractional exponents

The definitions for other exponents are not arbitrary: they are the only choices that keep the rules above working.

- **Zero.** The quotient rule gives $\dfrac{a^n}{a^n} = a^{n - n} = a^0$, and the left side is 1. So $a^0 = 1$ (for $a \ne 0$).
- **Negative.** $a^0 / a^n = a^{-n}$, so $a^{-n} = \dfrac{1}{a^n}$. A negative exponent means "reciprocal", not "negative number": $2^{-3} = \tfrac18$, which is positive. And $\left(\tfrac23\right)^{-2} = \left(\tfrac32\right)^2 = \tfrac94$.
- **Fractional.** The power-of-a-power rule needs $\left(a^{1/n}\right)^n = a^{1} = a$. So $a^{1/n}$ is the number whose $n$th power is $a$: the $n$th root. Then $a^{m/n} = \left(a^{1/n}\right)^m$. For example $27^{2/3} = (\sqrt[3]{27})^2 = 3^2 = 9$, and $16^{-3/4} = \dfrac{1}{(\sqrt[4]{16})^3} = \dfrac18$.

> [!TIP]
> With a fractional exponent, **take the root first**, then the power: $64^{5/6} = (\sqrt[6]{64})^5 = 2^5 = 32$. Taking the power first gives the same answer, but through enormous numbers.

### Prime bases: the master move

Most exponent problems become easy once every base is written as a power of a prime. Memorise these:

| Base 2 | Base 3 | Base 5 | Others |
|---|---|---|---|
| $2^5 = 32$, $2^6 = 64$ | $3^3 = 27$, $3^4 = 81$ | $5^3 = 125$ | $6^2 = 36$, $6^3 = 216$ |
| $2^7 = 128$, $2^8 = 256$ | $3^5 = 243$ | $5^4 = 625$ | $7^2 = 49$, $7^3 = 343$ |
| $2^9 = 512$, $2^{10} = 1024$ | $3^6 = 729$ | $5^5 = 3125$ | $11^2 = 121$, $12^2 = 144$ |

Composite bases split into primes: $12 = 2^2 \cdot 3$, so $12^5 = 2^{10} 3^5$; $18 = 2 \cdot 3^2$, so $18^3 = 2^3 3^6$. Then
$$
\frac{12^5}{18^3} = \frac{2^{10} 3^5}{2^3 3^6} = \frac{2^7}{3} = \frac{128}{3}.
$$

Because every positive integer has exactly **one** prime factorisation, if $2^a 3^b = 2^c 3^d$ then $a = c$ and $b = d$. That uniqueness is what lets you "match exponents" in equations.

### Exponential equations: match the bases

If $b^x = b^y$ with $b > 0$ and $b \ne 1$, then $x = y$. So rewrite both sides with a common base and compare exponents:
$$
4^{x} = 8^{3} \;\Rightarrow\; 2^{2x} = 2^{9} \;\Rightarrow\; 2x = 9 \;\Rightarrow\; x = 4.5.
$$

Base 1 is excluded because $1^x = 1$ for every $x$, and base 0 because $0^x = 0$ for every positive $x$. Base $-1$ is excluded too: $(-1)^2 = (-1)^4$ but $2 \ne 4$. On the GMAT, an equation like $x^4 = x^6$ has the solutions $0$, $1$ and $-1$, which "matching exponents" would miss.

### Factoring out the common power

A sum or difference of powers of the same base simplifies by pulling out the **smallest** power:
$$
2^{10} + 2^{12} = 2^{10}(1 + 2^2) = 5 \cdot 2^{10}, \qquad 3^{x+2} - 3^{x} = 3^{x}(9 - 1) = 8 \cdot 3^{x}.
$$
This works because of the product rule read backwards: $3^{x+2} = 3^x \cdot 3^2$. It turns an equation like $3^x + 3^{x+1} + 3^{x+2} = 117$ into $13 \cdot 3^x = 117$, which you can solve in your head.

> [!TIP]
> When a question contains a **sum or difference** of powers, factor before anything else. The test writers choose numbers so that the bracket becomes a small integer like 5, 8 or 13.

Sometimes the expression is a quadratic in disguise. In $9^x - 3^{x+1} = 54$, write $u = 3^x$, so $9^x = u^2$ and $3^{x+1} = 3u$. Then $u^2 - 3u - 54 = 0$, which factors as $(u - 9)(u + 6) = 0$. Since $3^x > 0$, only $u = 9$ works, and $x = 2$. Factoring quadratics is covered in [Quadratics and polynomials](../../algebra/quadratics-and-polynomials/).

### Roots: simplifying and combining

For non-negative $a$ and $b$, $\sqrt{ab} = \sqrt a\,\sqrt b$ and $\sqrt{a/b} = \sqrt a / \sqrt b$. These follow from the power-of-a-product rule with exponent $\tfrac12$. To **simplify** a root, pull out the largest perfect-square factor:
$$
\sqrt{72} = \sqrt{36 \cdot 2} = 6\sqrt2, \qquad \sqrt{48} = \sqrt{16 \cdot 3} = 4\sqrt3.
$$

**Like radicals** combine like like terms: $5\sqrt2 + 3\sqrt2 = 8\sqrt2$, just as $5y + 3y = 8y$. Unlike radicals do not: $\sqrt2 + \sqrt3$ is already as simple as it gets.

> [!WARNING]
> $\sqrt{a + b} \ne \sqrt a + \sqrt b$. Test it: $\sqrt{9 + 16} = 5$, but $\sqrt9 + \sqrt{16} = 7$. The root of a sum does not split; the root of a product does.

### Rationalising denominators and conjugates

A root in a denominator is removed by multiplying top and bottom by something that turns it into an integer:

- **One term.** $\dfrac{6}{\sqrt3} = \dfrac{6\sqrt3}{3} = 2\sqrt3$.
- **Two terms.** Use the **conjugate**, which flips the sign between the terms. Because $(p - q)(p + q) = p^2 - q^2$, the roots disappear:
$$
\frac{1}{\sqrt5 - 2} = \frac{\sqrt5 + 2}{(\sqrt5 - 2)(\sqrt5 + 2)} = \frac{\sqrt5 + 2}{5 - 4} = \sqrt5 + 2.
$$

Multiplying by $\dfrac{\sqrt5 + 2}{\sqrt5 + 2}$ is multiplying by 1, so the value is unchanged. Only the form changes, into one that matches the answer choices.

### Comparing powers

To compare two powers, make **either the bases or the exponents** the same.

- **Same base** (greater than 1): the bigger exponent wins. $2^{33} > 2^{30}$.
- **Same exponent** (positive bases): the bigger base wins. To compare $2^{30}$ and $3^{20}$, use the common factor 10 of the exponents: $2^{30} = (2^3)^{10} = 8^{10}$ and $3^{20} = (3^2)^{10} = 9^{10}$, so $3^{20}$ is larger.

> [!TIP]
> To compare $a^m$ and $b^n$, take the greatest common divisor $g$ of $m$ and $n$ and compare $a^{m/g}$ with $b^{n/g}$. For $2^{50}$ versus $6^{20}$, $g = 10$: compare $2^5 = 32$ with $6^2 = 36$.

### Signs: even and odd powers

- A **positive** base gives a positive power.
- A **negative** base gives a **positive** result for an even exponent and a **negative** result for an odd one: $(-2)^4 = 16$, $(-2)^3 = -8$.
- Hence $x^2 = 9$ has **two** solutions ($\pm3$), but $x^3 = -27$ has **one** ($-3$). Even powers hide the sign; odd powers keep it.
- An even power is never negative, so $x^2 = -4$ has no real solution, and even roots of negative numbers are not real numbers. Odd roots are fine: $\sqrt[3]{-8} = -2$.

> [!WARNING]
> - $-2^4 = -(2^4) = -16$, but $(-2)^4 = 16$. The exponent applies only to what it touches.
> - The symbol $\sqrt{\phantom{x}}$ means the **non-negative** root: $\sqrt{25} = 5$, never $-5$. So $\sqrt{x^2} = |x|$, not $x$. If $x = -3$, $\sqrt{x^2} = 3$.
> - $x^2 = 9$ gives $x = \pm 3$. Writing only $x = 3$ is the trap behind many Data Sufficiency "Not sufficient" answers.

### Raising fractions to powers

Multiplying a positive number by something less than 1 makes it smaller. So for $0 < x < 1$, each extra power shrinks it, and roots grow it:
$$
0 < x^3 < x^2 < x < \sqrt{x} < 1 \qquad \text{(for } 0 < x < 1\text{)}.
$$
For example, with $x = \tfrac14$: $x^2 = \tfrac1{16}$ and $\sqrt x = \tfrac12$. For $x > 1$, the order reverses. For $-1 < x < 0$, the even powers are positive and shrink, while the odd powers are negative and move **up** towards 0: with $x = -\tfrac12$, $x^3 = -\tfrac18$ is greater than $x$.

> [!TIP]
> For "which must be true" questions about powers, **test one number from each region**: something like $-2$, $-\tfrac12$, $\tfrac12$ and $2$. The regions $x < -1$, $-1 < x < 0$, $0 < x < 1$ and $x > 1$ behave differently, and the wrong answer choices are true in some regions but not all. Remember $0$, $1$ and $-1$ as special cases too.

Big-number and units-digit questions (for example, the last digit of $7^{43}$) are covered in [Remainders and units digits](../../arithmetic/remainders-and-units-digits/).

## Worked examples

**Example 1** *(Easy)*. What is the value of $\dfrac{2^5 \cdot 4^3}{8^3}$?

- (A) $\tfrac12$
- (B) 2
- (C) 4
- (D) 8
- (E) 16

*Solution.* Rewrite with base 2: $4^3 = 2^6$ and $8^3 = 2^9$. So the expression is $\dfrac{2^{5+6}}{2^9} = 2^2 = 4$. **Answer: (C).** A common slip is $4^3 = 2^5$ (adding instead of multiplying the exponents in $(2^2)^3$), which gives 2.

**Example 2** *(Medium)*. If $3^x + 3^{x+1} + 3^{x+2} = 117$, what is the value of $x$?

- (A) 1
- (B) 2
- (C) 3
- (D) 4
- (E) 9

*Solution.* Factor out the smallest power: $3^x(1 + 3 + 9) = 13 \cdot 3^x = 117$, so $3^x = 9$ and $x = 2$. **Answer: (B).** Choice (E) is $3^x$, not $x$.

*Backsolving* also works quickly: at $x = 2$ the sum is $9 + 27 + 81 = 117$. ✓

**Example 3** *(Medium)*. Which of the following equals $\dfrac{\sqrt5 + 2}{\sqrt5 - 2}$?

- (A) 1
- (B) $3 + 2\sqrt5$
- (C) $9 - 4\sqrt5$
- (D) $9 + 4\sqrt5$
- (E) $9 + 2\sqrt5$

*Solution.* Multiply top and bottom by the conjugate $\sqrt5 + 2$:
$$
\frac{(\sqrt5 + 2)^2}{(\sqrt5)^2 - 2^2} = \frac{5 + 4\sqrt5 + 4}{1} = 9 + 4\sqrt5.
$$
**Answer: (D).** (E) forgets the factor 2 in the middle term of $(\sqrt5 + 2)^2 = 5 + 2 \cdot 2\sqrt5 + 4$.

*Estimation check:* $\sqrt5 \approx 2.24$, so the fraction is about $\dfrac{4.24}{0.24} \approx 18$, and $9 + 4(2.24) \approx 18$. Choice (C) is about $0.06$ and (B) is about $7.5$, so both are clearly out.

**Example 4** *(Hard)*. Which of the following is greatest?

- (A) $2^{50}$
- (B) $3^{30}$
- (C) $5^{20}$
- (D) $6^{20}$
- (E) $31^{10}$

*Solution.* All the exponents are multiples of 10, so write each as a tenth power:
$$
2^{50} = 32^{10}, \quad 3^{30} = 27^{10}, \quad 5^{20} = 25^{10}, \quad 6^{20} = 36^{10}, \quad 31^{10}.
$$
With equal exponents, the largest base wins: 36. **Answer: (D).** The trap is (A): $2^{50}$ has the biggest exponent, but its base is the smallest.

**Example 5** *(Hard)*. If $-1 < x < 0$, which of the following orderings must be true?

- (A) $x < x^3 < x^2 < \dfrac1x$
- (B) $\dfrac1x < x < x^3 < x^2$
- (C) $\dfrac1x < x^3 < x < x^2$
- (D) $x^3 < x < \dfrac1x < x^2$
- (E) $x < \dfrac1x < x^3 < x^2$

*Solution.* Pick $x = -\tfrac12$: $\dfrac1x = -2$, $x = -0.5$, $x^3 = -0.125$, $x^2 = 0.25$. So $\dfrac1x < x < x^3 < x^2$. **Answer: (B).**

Why it holds for every $x$ in the interval, not just $-\tfrac12$: $x^2$ is the only positive value, so it is the largest. $x^3 = x \cdot x^2$ is $x$ scaled by a factor between 0 and 1, so it is closer to 0 than $x$ is, which makes it greater than $x$. And $\dfrac1x$ has absolute value greater than 1, so it is the most negative. Testing one number is fast; knowing *why* it generalises lets you trust it.

## Practice

Data Sufficiency items use the fixed answer choices explained in [The data sufficiency method](../../data-sufficiency/the-data-sufficiency-method/): **(A)** statement (1) alone is sufficient, but (2) alone is not; **(B)** (2) alone is sufficient, but (1) alone is not; **(C)** both together are sufficient, but neither alone is; **(D)** each alone is sufficient; **(E)** the statements together are not sufficient.

**1.** *(Easy)* If $2^{2x} \cdot 4^{x} = 256$, what is the value of $x$?

- (A) 1
- (B) 2
- (C) 3
- (D) 4
- (E) 8

<details>
<summary>Answer</summary>

$4^x = 2^{2x}$, so the left side is $2^{2x} \cdot 2^{2x} = 2^{4x}$. And $256 = 2^8$. So $4x = 8$ and $x = 2$. **(B)**.

</details>

**2.** *(Easy)* What is $\sqrt{48} + \sqrt{27} - \sqrt{12}$?

- (A) $3\sqrt3$
- (B) $4\sqrt3$
- (C) $5\sqrt3$
- (D) $6\sqrt3$
- (E) $\sqrt{63}$

<details>
<summary>Answer</summary>

$\sqrt{48} = 4\sqrt3$, $\sqrt{27} = 3\sqrt3$ and $\sqrt{12} = 2\sqrt3$. Combine like radicals: $(4 + 3 - 2)\sqrt3 = 5\sqrt3$. **(C)**. (E) adds and subtracts under one root, which is illegal: $48 + 27 - 12 = 63$, but roots of sums do not split.

</details>

**3.** *(Medium)* What is the value of $\dfrac{5^{12} - 5^{10}}{5^{11} + 5^{10}}$?

- (A) $\tfrac15$
- (B) 1
- (C) 4
- (D) 5
- (E) 25

<details>
<summary>Answer</summary>

Factor $5^{10}$ out of the top and the bottom: $\dfrac{5^{10}(25 - 1)}{5^{10}(5 + 1)} = \dfrac{24}{6} = 4$. **(C)**. Do not "cancel" powers term by term across a sum or difference: only a common **factor** of the whole numerator and the whole denominator can be cancelled, which is why you factor first.

</details>

**4.** *(Medium)* What is the value of $8^{-2/3} + 16^{3/4}$?

- (A) 4
- (B) $\tfrac{33}{4}$
- (C) $\tfrac{17}{2}$
- (D) 12
- (E) 16

<details>
<summary>Answer</summary>

Root first, then power. $8^{-2/3} = \dfrac{1}{(\sqrt[3]{8})^2} = \dfrac{1}{4}$. $16^{3/4} = (\sqrt[4]{16})^3 = 2^3 = 8$. Sum: $8\tfrac14 = \tfrac{33}{4}$. **(B)**. (A) treats the negative exponent as a negative number: $-4 + 8$.

</details>

**5.** *(Medium)* If $4^x - 4^{x-1} = 24$, what is the value of $x$?

- (A) $\tfrac32$
- (B) 2
- (C) $\tfrac52$
- (D) 3
- (E) $\tfrac72$

<details>
<summary>Answer</summary>

Factor out the smaller power: $4^{x-1}(4 - 1) = 24$, so $4^{x-1} = 8$. In base 2: $2^{2x - 2} = 2^3$, so $2x - 2 = 3$ and $x = \tfrac52$. **(C)**. Check: $4^{5/2} = 32$ and $4^{3/2} = 8$; $32 - 8 = 24$. ✓

</details>

**6.** *(Medium)* Which of the following equals $\dfrac{6}{3 - \sqrt3}$?

- (A) $3 - \sqrt3$
- (B) $3 + \sqrt3$
- (C) $2 + \sqrt3$
- (D) $\dfrac{3 + \sqrt3}{2}$
- (E) $6 + 2\sqrt3$

<details>
<summary>Answer</summary>

Multiply by the conjugate: $\dfrac{6(3 + \sqrt3)}{9 - 3} = \dfrac{6(3 + \sqrt3)}{6} = 3 + \sqrt3$. **(B)**. (E) forgets to divide by $9 - 3 = 6$ and instead divides by 3. *Estimate:* $\dfrac{6}{1.27} \approx 4.7$ and $3 + 1.73 = 4.73$. ✓

</details>

**7.** *(Medium)* Which of the following is greatest?

- (A) $4^{15}$
- (B) $8^{11}$
- (C) $16^{8}$
- (D) $32^{6}$
- (E) $64^{5}$

<details>
<summary>Answer</summary>

All the bases are powers of 2: $4^{15} = 2^{30}$, $8^{11} = 2^{33}$, $16^8 = 2^{32}$, $32^6 = 2^{30}$, $64^5 = 2^{30}$. The largest exponent is 33. **(B)**.

</details>

**8.** *(Medium, Data Sufficiency)* What is the value of $n$?

(1) $2^n \cdot 4 = 8^{n-2}$

(2) $n^2 = 16$

<details>
<summary>Answer</summary>

(1): $2^{n+2} = 2^{3n-6}$. With base 2, the exponents must be equal: $n + 2 = 3n - 6$, so $n = 4$. Sufficient.

(2): $n = 4$ or $n = -4$. Not sufficient (even power hides the sign).

**(A)**.

</details>

**9.** *(Hard)* If $\dfrac{12^5}{18^3} = 2^a \cdot 3^b$, where $a$ and $b$ are integers, what is the value of $a + b$?

- (A) 4
- (B) 5
- (C) 6
- (D) 7
- (E) 8

<details>
<summary>Answer</summary>

$12^5 = (2^2 \cdot 3)^5 = 2^{10} 3^5$ and $18^3 = (2 \cdot 3^2)^3 = 2^3 3^6$. So the quotient is $2^{7} 3^{-1}$. By uniqueness of prime factorisation, $a = 7$ and $b = -1$, so $a + b = 6$. **(C)**. (E) comes from taking $b = +1$.

</details>

**10.** *(Hard)* If $0 < x < 1$, which of the following must be less than $x$?

I. $x^2$

II. $\sqrt{x}$

III. $\dfrac{x + x^2}{2}$

- (A) I only
- (B) II only
- (C) I and III only
- (D) II and III only
- (E) I, II and III

<details>
<summary>Answer</summary>

I: $x^2 = x \cdot x$ is $x$ times a number less than 1, so it is less than $x$. True.

II: $\sqrt x > x$ for $0 < x < 1$ (for example $\sqrt{0.25} = 0.5$). False.

III: the average of $x$ and something smaller than $x$ (namely $x^2$) is less than $x$. True.

**(C)**.

</details>

**11.** *(Hard, Data Sufficiency)* Is $x < 0$?

(1) $x^3 < x^2$

(2) $x^5 < x^3$

<details>
<summary>Answer</summary>

(1): $x^2(x - 1) < 0$. Since $x^2 > 0$ (and $x \ne 0$), this means $x < 1$, $x \ne 0$. Both $x = \tfrac12$ (no) and $x = -2$ (yes) work. Not sufficient.

(2): $x^3(x^2 - 1) < 0$, so $x^3$ and $x^2 - 1$ have opposite signs: either $0 < x < 1$ or $x < -1$. Not sufficient.

Together: $x$ is in $(0, 1)$ or below $-1$; both regions satisfy (1). $x = \tfrac12$ satisfies both statements (answer no) and so does $x = -2$ (answer yes). Not sufficient. **(E)**.

</details>

**12.** *(Hard)* If $9^x - 3^{x+1} = 54$, what is the value of $x$?

- (A) 1
- (B) 2
- (C) 3
- (D) 6
- (E) 9

<details>
<summary>Answer</summary>

Let $u = 3^x$. Then $9^x = u^2$ and $3^{x+1} = 3u$, so $u^2 - 3u - 54 = 0$, that is $(u - 9)(u + 6) = 0$. A power of 3 is positive, so $u = 9 = 3^2$ and $x = 2$. **(B)**. Check: $81 - 27 = 54$. ✓ (E) is $u$, not $x$.

</details>

> [!NOTE]
> If you use Claude Code, the `quantome-math` plugin (`/plugin install quantome-math@quantome`) can check your arithmetic after you have worked a problem by hand. Practise without it: the GMAT has no calculator.

## Takeaways

- Every exponent rule is counting factors; zero, negative and fractional exponents are defined so the rules keep working.
- Rewrite every base as a power of a prime, then match exponents. Prime factorisation is unique, so this is legal.
- For a sum or difference of powers, factor out the smallest power first.
- Roots of products split; roots of sums do not. Rationalise $p \pm \sqrt q$ denominators with the conjugate.
- Compare powers by making the bases or the exponents equal.
- Even powers hide the sign ($x^2 = 9$ has two solutions); $\sqrt{x^2} = |x|$.
- Between 0 and 1, higher powers are smaller and roots are larger. Test values from each region: below $-1$, between $-1$ and 0, between 0 and 1, above 1.

## Further reading

- GMAC, *GMAT Official Guide* (current edition) and the *GMAT Official Guide Quantitative Review*: real retired questions on exponents and roots for timed practice.
- In this book: [Number properties](../../arithmetic/number-properties/), [Remainders and units digits](../../arithmetic/remainders-and-units-digits/), [Estimation and mental math](../../arithmetic/estimation-and-mental-math/) and [Problem-solving strategies](../../getting-started/problem-solving-strategies/).
