+++
summary = "Use the division algorithm and remainder arithmetic to find remainders of sums, products and huge powers, build numbers from remainder conditions, and find units digits from their cycles."
+++

# Remainders and Units Digits

Remainder questions look intimidating because the numbers are often enormous: "what is the remainder when $2^{100}$ is divided by 7?" The trick is that you never need the huge number. Remainders obey their own small arithmetic, in which big numbers can be swapped for their remainders at every step. Units digits are a special case: the units digit of a number *is* its remainder on division by 10.

This chapter builds on [Number properties](../../arithmetic/number-properties/) and [Divisibility, primes and factors](../../arithmetic/divisibility-primes-and-factors/).

## Key ideas

### The division algorithm

When a positive integer $d$ divides an integer $n$, there is exactly one way to write

$$
n = dq + r, \qquad 0 \le r < d,
$$

where $q$ is the **quotient** and $r$ the **remainder**. For example, $47 = 6 \times 7 + 5$, so $47$ divided by $6$ gives quotient 7 and remainder 5.

Three consequences are worth stating explicitly:

- **The remainder is always less than the divisor.** Dividing by 6 can only leave $0, 1, 2, 3, 4, 5$. So "remainder 6 when divided by 6" is impossible, and dividing by $d$ gives exactly $d$ possible remainders.
- **If $n < d$ (and $n \ge 0$), the quotient is 0 and the remainder is $n$ itself.** For example, 4 divided by 9 leaves remainder 4. Many test-takers forget this case.
- **A remainder of 0 means divisible.** "$n$ leaves remainder $r$ when divided by $d$" is the same as "$n - r$ is a multiple of $d$".

For negative $n$ the remainder is still between $0$ and $d - 1$: $-7 = 3 \times (-3) + 2$, so $-7$ divided by 3 leaves remainder 2, not $-1$. The GMAT rarely asks about negatives, but the "remainder must be non-negative" rule is useful when you work backwards.

> [!TIP]
> "$n$ leaves remainder $r$ when divided by $d$" translates directly into $n = dq + r$. Write this down and either (a) list the first few values, $r, r + d, r + 2d, \dots$, or (b) substitute it into the expression the question asks about. Listing is usually faster.

### Remainder arithmetic: sums, products and powers

Suppose $a = dq_1 + r_1$ and $b = dq_2 + r_2$. Then

$$
a + b = d(q_1 + q_2) + (r_1 + r_2), \qquad ab = d(\dots) + r_1 r_2.
$$

In the product, every term except $r_1 r_2$ contains a factor of $d$. So:

> [!IMPORTANT]
> **Remainders can replace the numbers.** The remainder of $a + b$, $a - b$ or $ab$ on division by $d$ equals the remainder of $r_1 + r_2$, $r_1 - r_2$ or $r_1 r_2$ on division by $d$. Powers are repeated products, so the remainder of $a^k$ is the remainder of $r_1^k$.

Two cautions. First, the result may need one more reduction: $r_1 + r_2$ or $r_1 r_2$ can exceed $d$. Second, this works for $+$, $-$ and $\times$, **not** for division.

**Examples.**

- Remainder of $17 \times 23$ divided by 5: replace 17 by 2 and 23 by 3. $2 \times 3 = 6$, which leaves 1. (Check: $391 = 5 \times 78 + 1$.)
- If $n$ leaves remainder 5 when divided by 7, then $3n + 4$ leaves the same remainder as $3 \times 5 + 4 = 19$, which is 5.

**Negative remainders are a shortcut.** It is often easier to say "$99$ is 1 less than a multiple of 100" than "99 leaves remainder 99". Then $99^{10}$ behaves like $(-1)^{10} = 1$, so $99^{10}$ leaves remainder 1 when divided by 100. Convert back to a non-negative remainder at the end: a "remainder" of $-1$ on division by 7 is really 6.

### Remainders of large powers: find the cycle

The remainders of $a, a^2, a^3, \dots$ on division by $d$ must eventually repeat, because there are only $d$ possible remainders and each one is determined by the previous one. Find the cycle, then use the position in the cycle.

**Example: $2^{100}$ divided by 7.** The powers of 2 leave remainders

$$
2^1 \to 2, \quad 2^2 \to 4, \quad 2^3 = 8 \to 1, \quad 2^4 \to 2, \dots
$$

Since $2^3$ leaves remainder 1, the pattern repeats every 3. Now $100 = 3 \times 33 + 1$, so $2^{100} = (2^3)^{33} \times 2$ behaves like $1^{33} \times 2 = 2$. The remainder is **2**.

> [!TIP]
> Look for a power that leaves remainder **1** (or $-1$). Once $a^m$ leaves 1, every block of $m$ factors collapses to 1, and only the leftover exponent $k \bmod m$ matters. If $a^m$ leaves $-1$, then $a^{2m}$ leaves 1.

### Finding numbers from remainder conditions

Questions such as "$n$ leaves remainder 3 when divided by 5 and remainder 4 when divided by 7" are solved by listing.

1. List numbers that satisfy the condition with the **larger** divisor (fewer to check): $4, 11, 18, 25, \dots$
2. Find the first one that satisfies the other condition: $4 \to$ remainder 4 on division by 5 (no), $11 \to 1$ (no), $18 \to 3$ (yes).
3. All solutions differ by the LCM of the divisors: $n = 35k + 18$.

> [!IMPORTANT]
> If $n$ satisfies remainder conditions for divisors $d_1$ and $d_2$, and $n_0$ is the smallest solution, then every solution is $n_0 + \operatorname{lcm}(d_1, d_2) \times k$. So $n$ leaves a **fixed remainder** ($n_0$, reduced) when divided by the LCM.

Why must the solutions be spaced by the LCM? If $n$ and $m$ both satisfy both conditions, then $n - m$ is divisible by $d_1$ and by $d_2$, hence by their LCM. (When the divisors are coprime, as in 5 and 7, a solution always exists. This is the idea behind the Chinese remainder theorem, though you never need the name.)

**The "same deficit" shortcut.** If $n$ leaves remainder 3 on division by 4 and remainder 4 on division by 5, notice that $n$ is **one short** of a multiple of 4 and of 5. So $n + 1$ is a multiple of 20, and $n = 20k - 1$: 19, 39, 59, ... The same trick works whenever $d - r$ is the same for every condition. And when the remainders themselves are equal (say remainder 1 for every divisor), $n - 1$ is a multiple of the LCM.

### Units digits and their cycles

The units digit of a number is its remainder on division by 10, so remainder arithmetic applies: **the units digit of a sum, product or power depends only on the units digits of the inputs.** The units digit of $87^{47}$ is the units digit of $7^{47}$.

Powers of each digit cycle:

| Last digit | Units digits of successive powers | Period |
|---|---|---|
| 0, 1, 5, 6 | always 0, 1, 5, 6 respectively | 1 |
| 4 | 4, 6, 4, 6, ... | 2 |
| 9 | 9, 1, 9, 1, ... | 2 |
| 2 | 2, 4, 8, 6, ... | 4 |
| 3 | 3, 9, 7, 1, ... | 4 |
| 7 | 7, 9, 3, 1, ... | 4 |
| 8 | 8, 4, 2, 6, ... | 4 |

Every cycle has length 1, 2 or 4, so a period of 4 works for all digits.

**Method.** To find the units digit of $a^k$ for $k \ge 1$:

1. Keep only the units digit of $a$.
2. Find the remainder of $k$ on division by 4 (or by 2 for digits 4 and 9).
3. A remainder of 1, 2 or 3 picks the 1st, 2nd or 3rd entry of the cycle. A remainder of 0 picks the **last** entry (the 4th, or the 2nd for period 2).

For $87^{47}$: $47 = 4 \times 11 + 3$, and the third entry of the 7-cycle is 3. The units digit is **3**.

> [!WARNING]
> The off-by-one error is the most common mistake. If the exponent is a multiple of 4, use the **4th** entry of the cycle (6 for base 2, 1 for bases 3 and 7, 6 for base 8), not the first. Also, the units digit of $a^k + b^k$ is the units digit of the *sum of the two units digits*, so add first and then keep the last digit.

### Decimal remainders

Dividing $n$ by $d$ gives

$$
\frac{n}{d} = q + \frac{r}{d}.
$$

So the **decimal part** of $n/d$ is $r/d$. For example, $17/4 = 4.25$: the quotient is 4, and the remainder is 1 because $1/4 = 0.25$.

This links remainders to decimals. If you know that $x/y = 64.12$, then $r/y = 0.12 = \tfrac{3}{25}$. The remainder must be a multiple of 3 and $y$ the same multiple of 25: $(r, y) = (3, 25)$, $(6, 50)$, $(9, 75)$, and so on. Questions then ask which value $r$ (or $y$) *could* take.

> [!TIP]
> In decimal-remainder questions, convert the decimal part to a fraction **in lowest terms** first. The remainder is then a multiple of the numerator, and the divisor the same multiple of the denominator.

### Common traps

> [!WARNING]
> Wrong answer choices in this topic are usually built from:
> - a "remainder" that is equal to or larger than the divisor;
> - forgetting the case $n < d$, where the remainder is $n$ itself;
> - not reducing again after adding or multiplying remainders;
> - the off-by-one error in units-digit cycles when the exponent is a multiple of the period;
> - excluding the smallest solution (often $n = r$ itself, with quotient 0) when counting numbers that satisfy remainder conditions;
> - dividing remainders, which is not allowed.

## Worked examples

**Example 1** *(Easy)*. When the positive integer $n$ is divided by 7, the remainder is 5. What is the remainder when $3n + 4$ is divided by 7?

(A) 0 (B) 1 (C) 3 (D) 5 (E) 6

**Solution.** Replace $n$ by its remainder: $3 \times 5 + 4 = 19 = 2 \times 7 + 5$. The remainder is 5. **Answer: (D).**

**Fast method: pick a number.** The smallest $n$ is 5 itself, so $3n + 4 = 19$, remainder 5. Confirm with $n = 12$: $40 = 5 \times 7 + 5$.

**Example 2** *(Medium)*. What is the units digit of $7^{83} + 3^{41}$?

(A) 0 (B) 2 (C) 4 (D) 6 (E) 8

**Solution.** For $7^{83}$: $83 = 4 \times 20 + 3$, so take the third entry of $7, 9, 3, 1$, which is 3. For $3^{41}$: $41 = 4 \times 10 + 1$, so take the first entry of $3, 9, 7, 1$, which is 3. The sum ends in $3 + 3 = 6$. **Answer: (D).**

**Example 3** *(Medium)*. How many integers $n$ with $100 < n < 200$ leave a remainder of 3 when divided by 7 and a remainder of 1 when divided by 4?

(A) 2 (B) 3 (C) 4 (D) 5 (E) 6

**Solution.** List numbers leaving remainder 3 on division by 7: $3, 10, 17, \dots$ Check each on division by 4: $3 \to 3$, $10 \to 2$, $17 \to 1$. So the smallest solution is 17, and all solutions are $17 + 28k$, since $\operatorname{lcm}(7, 4) = 28$.

Between 100 and 200: $17 + 84 = 101$, then 129, 157 and 185. The next one, 213, is too big. That is 4 numbers. **Answer: (C).**

**Example 4** *(Hard)*. What is the remainder when $2^{100}$ is divided by 7?

(A) 1 (B) 2 (C) 3 (D) 4 (E) 6

**Solution.** $2^3 = 8$ leaves remainder 1, so the remainders of powers of 2 cycle with period 3: $2, 4, 1, 2, 4, 1, \dots$ Since $100 = 3 \times 33 + 1$,

$$
2^{100} = (2^3)^{33} \times 2,
$$

which behaves like $1^{33} \times 2 = 2$. **Answer: (B).**

The trap (D) is an off-by-one slip in the cycle: $100 = 3 \times 33 + 1$ points to the **first** entry of $2, 4, 1$, not the second. Choice (A) is what you get if you assume $2^{100}$ lines up with the end of a cycle. Each divisor has its own cycle length, so find the cycle for the divisor in the question rather than reusing the period 4 from units digits.

**Example 5** *(Hard)*. When the positive integer $x$ is divided by the positive integer $y$, the result is $64.12$. Which of the following could be the remainder when $x$ is divided by $y$?

(A) 2 (B) 8 (C) 14 (D) 15 (E) 20

**Solution.** The decimal part is $r/y = 0.12 = \tfrac{12}{100} = \tfrac{3}{25}$ in lowest terms. So $r = 3k$ and $y = 25k$ for some positive integer $k$, and $r$ must be a multiple of 3. Among the choices only 15 is ($k = 5$, $y = 125$, $x = 64 \times 125 + 15 = 8015$). **Answer: (D).**

The trap is to reason from $\tfrac{12}{100}$ without reducing and conclude that $r$ must be a multiple of 12. None of the choices is, which tempts people to guess. The other trap is to pick 2 or 8 because they divide 64.

## Practice

<details>
<summary>Data Sufficiency answer choices (the same on every DS question)</summary>

- **(A)** Statement (1) ALONE is sufficient, but statement (2) alone is not sufficient.
- **(B)** Statement (2) ALONE is sufficient, but statement (1) alone is not sufficient.
- **(C)** BOTH statements TOGETHER are sufficient, but NEITHER statement ALONE is sufficient.
- **(D)** EACH statement ALONE is sufficient.
- **(E)** Statements (1) and (2) TOGETHER are NOT sufficient.

</details>

**1.** *(Easy)* When $n$ is divided by 9, the remainder is 7. What is the remainder when $n + 5$ is divided by 9?

(A) 1 (B) 2 (C) 3 (D) 4 (E) 12

<details>
<summary>Answer</summary>

**(C).** $7 + 5 = 12 = 9 + 3$, so the remainder is 3. Choice (E) forgets to reduce: a remainder on division by 9 cannot be 12.

</details>

**2.** *(Easy)* What is the units digit of $13^{47}$?

(A) 0 (B) 1 (C) 3 (D) 7 (E) 9

<details>
<summary>Answer</summary>

**(D).** Only the 3 matters. The cycle for 3 is $3, 9, 7, 1$, and $47 = 4 \times 11 + 3$, so take the third entry: 7.

</details>

**3.** *(Easy)* When $a$ is divided by 8 the remainder is 5, and when $b$ is divided by 8 the remainder is 6. What is the remainder when $ab$ is divided by 8?

(A) 1 (B) 2 (C) 3 (D) 6 (E) 7

<details>
<summary>Answer</summary>

**(D).** $5 \times 6 = 30 = 3 \times 8 + 6$. The remainder is 6. Choice (C) is the remainder of $a + b$, which is $11 \to 3$.

</details>

**4.** *(Medium)* When 75 is divided by the positive integer $k$, the remainder is 5. How many values of $k$ are possible?

(A) 3 (B) 4 (C) 5 (D) 6 (E) 8

<details>
<summary>Answer</summary>

**(C).** $75 = kq + 5$ means $k$ divides $70$, and the remainder 5 must be less than $k$, so $k > 5$. The divisors of 70 are 1, 2, 5, 7, 10, 14, 35, 70. Those greater than 5 are 7, 10, 14, 35, 70: five values. Choice (E) forgets the condition $k > 5$.

</details>

**5.** *(Medium)* When $n$ is divided by 6, the remainder is 4. What is the remainder when $n^2$ is divided by 6?

(A) 0 (B) 1 (C) 2 (D) 3 (E) 4

<details>
<summary>Answer</summary>

**(E).** $4^2 = 16 = 2 \times 6 + 4$. Check with $n = 10$: $100 = 16 \times 6 + 4$.

</details>

**6.** *(Medium)* What is the units digit of $4^{33} + 9^{22}$?

(A) 1 (B) 3 (C) 5 (D) 7 (E) 9

<details>
<summary>Answer</summary>

**(C).** Powers of 4 end in 4 (odd exponent) or 6 (even exponent), so $4^{33}$ ends in 4. Powers of 9 end in 9 (odd) or 1 (even), so $9^{22}$ ends in 1. The sum ends in $4 + 1 = 5$.

</details>

**7.** *(Medium)* When the positive integer $x$ is divided by the positive integer $y$, the quotient is 6 and the remainder is 8. If $x / y = 6.32$, what is $y$?

(A) 16 (B) 20 (C) 25 (D) 32 (E) 40

<details>
<summary>Answer</summary>

**(C).** The decimal part is $r / y$, so $8 / y = 0.32$ and $y = 8 / 0.32 = 25$. Check: $x = 6 \times 25 + 8 = 158$, and $158 / 25 = 6.32$.

</details>

**8.** *(Medium, Data Sufficiency)* What is the remainder when the positive integer $n$ is divided by 12?

(1) When $n$ is divided by 4, the remainder is 3.

(2) When $n$ is divided by 3, the remainder is 2.

<details>
<summary>Answer</summary>

**(C).** (1): $n$ could be 3, 7 or 11, giving remainders 3, 7, 11 on division by 12. Not sufficient. (2): $n$ could be 2, 5, 8, 11, ..., giving several remainders. Not sufficient. Together: $n$ is 1 short of a multiple of 4 and 1 short of a multiple of 3, so $n + 1$ is a multiple of 12. The remainder is always 11. Sufficient.

</details>

**9.** *(Hard)* What is the remainder when $2^{51}$ is divided by 9?

(A) 1 (B) 2 (C) 4 (D) 7 (E) 8

<details>
<summary>Answer</summary>

**(E).** $2^3 = 8$ leaves remainder $-1$ (one less than 9), so $2^6$ leaves remainder 1. Since $51 = 6 \times 8 + 3$, $2^{51} = (2^6)^8 \times 2^3$ behaves like $1 \times 8 = 8$. A shorter route: $2^{51} = (2^3)^{17}$ behaves like $(-1)^{17} = -1$, which is remainder 8.

</details>

**10.** *(Hard)* How many positive integers less than 500 leave a remainder of 1 when divided by 4, by 5 and by 6?

(A) 7 (B) 8 (C) 9 (D) 10 (E) 24

<details>
<summary>Answer</summary>

**(C).** $n - 1$ is divisible by 4, 5 and 6, hence by $\operatorname{lcm}(4, 5, 6) = 60$. So $n = 60k + 1$ with $k \ge 0$: $1, 61, 121, \dots, 481$. That is $k = 0$ to $8$, nine numbers. The trap (B) leaves out $n = 1$, which does leave remainder 1 on each division (quotient 0). Choice (E) comes from checking only the divisors 4 and 5 (multiples of $\operatorname{lcm}(4, 5) = 20$) and also leaving out $n = 1$: that gives $21, 41, \dots, 481$, which is 24 numbers.

</details>

**11.** *(Hard)* When $n$ is divided by 5 the remainder is 3, and when $n$ is divided by 7 the remainder is 5. What is the remainder when $n$ is divided by 35?

(A) 2 (B) 12 (C) 23 (D) 28 (E) 33

<details>
<summary>Answer</summary>

**(E).** In both cases $n$ is 2 short of a multiple: $n + 2$ is divisible by 5 and by 7, so by 35. Then $n = 35k - 2 = 35(k - 1) + 33$, and the remainder is 33. Check: $33 = 6 \times 5 + 3$ and $33 = 4 \times 7 + 5$.

</details>

**12.** *(Hard, Data Sufficiency)* If $n$ is a positive integer, what is the units digit of $7^n$?

(1) $n$ is a multiple of 6.

(2) $n$ is a multiple of 10.

<details>
<summary>Answer</summary>

**(E).** The units digit depends on the remainder of $n$ on division by 4. (1): $n = 6$ leaves 2 (units digit 9) and $n = 12$ leaves 0 (units digit 1). Not sufficient. (2): $n = 10$ leaves 2 (digit 9) and $n = 20$ leaves 0 (digit 1). Not sufficient. Together $n$ is a multiple of 30: $n = 30$ leaves 2 (digit 9) and $n = 60$ leaves 0 (digit 1). Still not sufficient. The trap (C) assumes a multiple of 30 pins down the cycle position, but $30$ is not a multiple of 4.

</details>

> [!NOTE]
> If you use Claude Code, the `quantome-math` plugin (`/plugin install quantome-math@quantome`) can confirm a remainder or a units digit after you have worked it out by hand.

## Takeaways

- Translate "remainder $r$ on division by $d$" into $n = dq + r$ with $0 \le r < d$, then list values or substitute.
- In sums, differences, products and powers, replace each number by its remainder, then reduce again. Never divide remainders.
- For large powers, find a power that leaves remainder 1 (or $-1$) and use the exponent's position in the cycle.
- Solutions to two remainder conditions are spaced by the LCM of the divisors. Use the "same deficit" or "same remainder" shortcut when it applies.
- Units digits cycle with period 1, 2 or 4. When the exponent is a multiple of the period, use the *last* entry of the cycle.
- The decimal part of $n / d$ is $r / d$. Reduce the decimal to lowest terms before deciding what $r$ can be.

## Further reading

- GMAC, *GMAT Official Guide* (current edition): practise remainder and units-digit questions from its Problem Solving and Data Sufficiency sets.
- Related chapters: [Divisibility, primes and factors](../../arithmetic/divisibility-primes-and-factors/) and [Exponents and roots](../../algebra/exponents-and-roots/).
