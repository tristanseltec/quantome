+++
summary = "Compute quickly without a calculator using memorised values and multiplication shortcuts, and know when (and how) to estimate instead of computing exactly."
+++

# Estimation and Mental Math

The GMAT Quant section gives you no calculator and about two minutes per question. Speed comes less from doing arithmetic faster than from **doing less of it**: knowing common values by heart, rearranging a product into an easy one, and noticing when the answer choices are far enough apart that a rough estimate is enough. This chapter collects the facts worth memorising, the shortcuts that rest on simple algebra, and a method for deciding when estimation is safe.

## Key ideas

### Numbers worth memorising

Recognising these on sight saves seconds on many questions, and it also helps you spot perfect squares, cubes and powers inside larger problems.

**Squares from $11^2$ to $25^2$** (you should already know $1^2$ to $10^2$):

| $n$ | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| $n^2$ | 121 | 144 | 169 | 196 | 225 | 256 | 289 | 324 | 361 | 400 | 441 | 484 | 529 | 576 | 625 |

**Cubes and powers of 2:**

| $n$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| $n^3$ | 1 | 8 | 27 | 64 | 125 | 216 | 343 | 512 | 729 | 1000 | | |
| $2^n$ | 2 | 4 | 8 | 16 | 32 | 64 | 128 | 256 | 512 | 1024 | 2048 | 4096 |

Note the overlaps: $64 = 2^6 = 4^3 = 8^2$ and $512 = 2^9 = 8^3$. Also $2^{10} = 1024 \approx 10^3$, which is the key to estimating large powers of 2.

**Fraction, decimal and percent equivalents:**

| Fraction | Decimal | Percent | | Fraction | Decimal | Percent |
|---|---|---|---|---|---|---|
| $\tfrac12$ | 0.5 | 50% | | $\tfrac16$ | $0.1\overline{6}$ | $16\tfrac23\%$ |
| $\tfrac13$ | $0.\overline{3}$ | $33\tfrac13\%$ | | $\tfrac56$ | $0.8\overline{3}$ | $83\tfrac13\%$ |
| $\tfrac23$ | $0.\overline{6}$ | $66\tfrac23\%$ | | $\tfrac18$ | 0.125 | 12.5% |
| $\tfrac14$ | 0.25 | 25% | | $\tfrac38$ | 0.375 | 37.5% |
| $\tfrac34$ | 0.75 | 75% | | $\tfrac58$ | 0.625 | 62.5% |
| $\tfrac15$ | 0.2 | 20% | | $\tfrac78$ | 0.875 | 87.5% |
| $\tfrac25$ | 0.4 | 40% | | $\tfrac19$ | $0.\overline{1}$ | $11\tfrac19\%$ |
| $\tfrac{1}{20}$ | 0.05 | 5% | | $\tfrac{1}{11}$ | $0.\overline{09}$ | $9\tfrac{1}{11}\%$ |
| $\tfrac{1}{25}$ | 0.04 | 4% | | $\tfrac17$ | $\approx 0.143$ | $\approx 14.3\%$ |

Two square roots are also worth knowing: $\sqrt2 \approx 1.41$ and $\sqrt3 \approx 1.73$.

### Multiplication shortcuts, and why they work

Every shortcut below is ordinary algebra applied to friendly numbers.

**Multiply by 5:** multiply by 10 and halve, since $5 = \tfrac{10}{2}$. $36 \times 5 = 360 / 2 = 180$.

**Multiply by 25:** multiply by 100 and divide by 4, since $25 = \tfrac{100}{4}$. $64 \times 25 = 6400 / 4 = 1600$. Similarly, $\times 125$ is $\times 1000 \div 8$.

**Multiply a two-digit number by 11:** write the sum of the digits between them, since $11 \times (10a + b) = 100a + 10(a + b) + b$. $43 \times 11$: $4$, $4 + 3 = 7$, $3$, giving 473. If the middle sum is 10 or more, carry the 1: $87 \times 11$: $8$, $15$, $7$, giving $957$.

**Multiply by 9, 99, 999:** multiply by the power of 10 and subtract. $999 \times 37 = 37{,}000 - 37 = 36{,}963$.

**Products near 100.** Write each factor as $100 - a$ and $100 - b$. Then

$$
(100 - a)(100 - b) = 100(100 - a - b) + ab.
$$

So for $97 \times 96$ (here $a = 3$, $b = 4$): take $97 - 4 = 93$ for the first two digits, and $3 \times 4 = 12$ for the last two, giving $9312$. Above 100 it works with plus signs: $104 \times 107 = 100 \times 111 + 28 = 11{,}128$.

**Difference of squares.** When two numbers are equally spaced around a round number, use $(m - d)(m + d) = m^2 - d^2$:

$$
47 \times 53 = 50^2 - 3^2 = 2500 - 9 = 2491, \qquad 38 \times 42 = 1600 - 4 = 1596.
$$

**Squaring numbers that end in 5.** $(10a + 5)^2 = 100a(a + 1) + 25$. So multiply the leading digits by the next integer and append 25: $65^2$ is $6 \times 7 = 42$ followed by 25, giving 4225. $85^2 = 7225$.

**Rearrange before you multiply.** Look for pairs that make round numbers: $4 \times 17 \times 25 = (4 \times 25) \times 17 = 1700$. And $2 \times 5$, $4 \times 25$ and $8 \times 125$ make 10, 100 and 1000.

### Division shortcuts

- **Divide by 5:** multiply by 2 and divide by 10. $420 / 5 = 840 / 10 = 84$.
- **Divide by 25:** multiply by 4 and divide by 100. $1600 / 25 = 6400 / 100 = 64$.
- **Divide by a fraction or small decimal:** dividing by $0.25 = \tfrac14$ multiplies by 4, dividing by $0.2$ multiplies by 5, dividing by $0.125$ multiplies by 8. So $7 / 0.25 = 28$.
- **Cancel before dividing.** In $\tfrac{36 \times 45}{27 \times 20}$, cancel $36/27 = 4/3$ and $45/20 = 9/4$ to get $\tfrac{4 \times 9}{3 \times 4} = 3$.
- **Clear decimals by scaling both parts:** $\tfrac{0.42}{0.006} = \tfrac{420}{6} = 70$. Multiply the top and the bottom by the same power of 10.

> [!TIP]
> Before multiplying out any fraction in an answer, factor and cancel. GMAT numbers are chosen so that things cancel. If you find yourself multiplying two three-digit numbers, look for a shortcut you have missed.

### Estimating with rounding and bounds

Estimation is not guessing. It is computing an approximation and knowing **which way** it errs.

**Round to friendly numbers.** $398 \times 0.0502 / 19.9 \approx 400 \times 0.05 / 20 = 1$.

**Track the direction of rounding.**

- In a product, rounding one factor up and another down tends to cancel the errors. Rounding both up gives an overestimate.
- In a quotient, rounding the **numerator up** or the **denominator down** makes the result bigger. So $\tfrac{62}{19}$ is an upper bound for $\tfrac{61}{19.5}$.

**Bounds** turn an estimate into a proof. To show the sum $\tfrac{1}{101} + \tfrac{1}{102} + \cdots + \tfrac{1}{150}$ is between $\tfrac13$ and $\tfrac12$: it has 50 terms, each at most $\tfrac{1}{101}$ and at least $\tfrac{1}{150}$. So the sum is at most $\tfrac{50}{101} < \tfrac12$ and at least $\tfrac{50}{150} = \tfrac13$. You never compute a single term exactly.

> [!WARNING]
> Estimation goes wrong when the errors pile up in the same direction, or when you round a number that is being **subtracted** from a nearly equal number. $1001 - 998 = 3$, but rounding both to 1000 gives 0. Compute differences of close numbers exactly.

### Ordering numbers

To order several numbers:

1. **Convert to one form**, usually decimals to two or three places, or fractions with a common denominator or numerator.
2. **Use benchmarks** such as $\tfrac12$, 1 or a nearby round number, and compare each number with the benchmark first.
3. **Compare differences from the benchmark** when the numbers are close. For $\sqrt{50}$, $7.1$ and $\tfrac{50}{7}$: $\sqrt{50}$ is a little over 7 (since $7.1^2 = 50.41 > 50$, it is below 7.1), and $\tfrac{50}{7} = 7\tfrac17 \approx 7.14$. So $\sqrt{50} < 7.1 < \tfrac{50}{7}$.
4. **For powers, rewrite with a common exponent or base.** $2^{30} = (2^3)^{10} = 8^{10}$ and $3^{20} = (3^2)^{10} = 9^{10}$, so $3^{20} > 2^{30}$.

### Scientific notation

A number in **scientific notation** is $a \times 10^n$ with $1 \le a < 10$. It makes the size of a number obvious and makes multiplication easy: multiply the front parts and add the exponents.

$$
(3 \times 10^5)(4 \times 10^{-2}) = 12 \times 10^3 = 1.2 \times 10^4.
$$

**Moving the decimal point.** Each place you move the point left raises the exponent by 1: $0.00062 = 6.2 \times 10^{-4}$ and $45{,}000 = 4.5 \times 10^4$. To divide, divide the front parts and subtract exponents. Rounding the front parts to one digit gives a fast order-of-magnitude estimate. Questions about the number of digits or decimal places reduce to this notation too. The exponent rules themselves are in [Exponents and roots](../../algebra/exponents-and-roots/).

### Approximating square roots

1. **Bracket between perfect squares.** $\sqrt{50}$ lies between $\sqrt{49} = 7$ and $\sqrt{64} = 8$, close to 7.
2. **Refine by interpolation.** Near $m^2$, $\sqrt{m^2 + d} \approx m + \dfrac{d}{2m}$. So $\sqrt{50} \approx 7 + \tfrac{1}{14} \approx 7.07$. (The true value is $7.0711\ldots$) This works because $(m + \tfrac{d}{2m})^2 = m^2 + d + \tfrac{d^2}{4m^2}$, which is just a little above $m^2 + d$, so the estimate is slightly too high.
3. **Square roots of perfect squares from the last digit.** A square ending in 1 has a root ending in 1 or 9. For $\sqrt{7921}$: $80^2 = 6400$ and $90^2 = 8100$, so the root is in the 80s, just below 90, ending in 1 or 9. Try 89: $89^2 = 8100 - 180 + 1 = 7921$.
4. **Move the decimal point in pairs.** $\sqrt{0.0049} = 0.07$ because $0.0049 = 49 \times 10^{-4}$ and $\sqrt{10^{-4}} = 10^{-2}$.

### When is estimation enough?

Estimate when:

- the question says "approximately" or "closest to";
- the answer choices are **far apart**, such as powers of 10, or values that differ by more than your estimate's error;
- you only need to know which side of a benchmark a value falls on (positive or negative, more or less than 1, more or less than another choice);
- it is a **Data Sufficiency** question: there you need to know whether a unique answer exists, never the answer itself.

Compute exactly when the choices are close together (for example 4,871 to 4,911), when the question involves the difference of two nearly equal numbers, or when the choices differ only in the last digit. In that last case, a **units digit check** is often faster than full computation: $67 \times 73$ ends in $7 \times 3 = 21$, so the answer ends in 1.

> [!TIP]
> **Look at the answer choices before you calculate.** Their spread tells you how precise you need to be. If they are 0.01, 0.1, 1, 10 and 100, you need only the power of 10. If they differ by 10 in the hundreds, you need the exact value or a units-digit check.

> [!WARNING]
> Common traps in estimation questions:
> - rounding so aggressively that two answer choices become indistinguishable;
> - losing a factor of 10 when moving decimal points (count them, or use scientific notation);
> - rounding several quantities in the same direction and then trusting a "closest" choice;
> - forgetting that $\sqrt{0.04} = 0.2$, not $0.02$ (decimal places in a square root halve);
> - assuming $2^{10} = 1000$ exactly when the choices are close.

## Worked examples

**Example 1** *(Easy)*. What is $48 \times 25$?

(A) 1,000 (B) 1,150 (C) 1,200 (D) 1,250 (E) 1,300

**Solution.** $48 \times 25 = 48 \times 100 / 4 = 4800 / 4 = 1200$. Or split 48: $(4 \times 25) \times 12 = 100 \times 12 = 1200$. **Answer: (C).**

**Example 2** *(Medium)*. What is $67 \times 73$?

(A) 4,871 (B) 4,881 (C) 4,891 (D) 4,901 (E) 4,911

**Solution.** The factors sit 3 either side of 70, so $67 \times 73 = 70^2 - 3^2 = 4900 - 9 = 4891$. **Answer: (C).**

Every choice ends in 1, so the units-digit check ($7 \times 3 = 21$) does not help here. The choices are only 10 apart, so estimation is not enough either. This is a question for an exact shortcut.

**Example 3** *(Medium)*. Which of the following is closest to $\dfrac{398 \times 0.0502}{19.9}$?

(A) 0.01 (B) 0.1 (C) 1 (D) 10 (E) 100

**Solution.** Round: $\dfrac{400 \times 0.05}{20} = \dfrac{20}{20} = 1$. The choices are powers of 10, so rounding errors of a few percent cannot change the answer. (The exact value is $1.004$.) **Answer: (C).**

**Example 4** *(Medium)*. Let $a = \sqrt{50}$, $b = 7.1$ and $c = \tfrac{50}{7}$. Which of the following is true?

(A) $a < b < c$ (B) $a < c < b$ (C) $b < a < c$ (D) $c < a < b$ (E) $c < b < a$

**Solution.** $7.1^2 = 50.41 > 50$, so $\sqrt{50} < 7.1$: $a < b$. And $c = 7\tfrac17$, with $\tfrac17 \approx 0.143 > 0.1$, so $c > 7.1 = b$. Hence $a < b < c$. **Answer: (A).**

Squaring $b$ is the key move: comparing $\sqrt{50}$ with 7.1 is the same as comparing 50 with $7.1^2$, because both numbers are positive.

**Example 5** *(Hard)*. The sum $S = \dfrac{1}{101} + \dfrac{1}{102} + \dfrac{1}{103} + \cdots + \dfrac{1}{150}$ lies in which interval?

(A) between 0 and $\tfrac14$ (B) between $\tfrac14$ and $\tfrac13$ (C) between $\tfrac13$ and $\tfrac12$ (D) between $\tfrac12$ and $\tfrac23$ (E) between $\tfrac23$ and 1

**Solution.** There are $150 - 101 + 1 = 50$ terms. Each is at most $\tfrac{1}{101}$ and at least $\tfrac{1}{150}$, and not all are equal, so

$$
\frac{50}{150} < S < \frac{50}{101}, \qquad\text{that is}\qquad \frac13 < S < \frac{50}{101} < \frac12.
$$

**Answer: (C).** (The actual value is about 0.404.)

The traps are miscounting the terms (49 or 51 doesn't change this answer, but it can in similar questions) and trying to add fractions, which is impossible in the time.

## Practice

<details>
<summary>Data Sufficiency answer choices (the same on every DS question)</summary>

- **(A)** Statement (1) ALONE is sufficient, but statement (2) alone is not sufficient.
- **(B)** Statement (2) ALONE is sufficient, but statement (1) alone is not sufficient.
- **(C)** BOTH statements TOGETHER are sufficient, but NEITHER statement ALONE is sufficient.
- **(D)** EACH statement ALONE is sufficient.
- **(E)** Statements (1) and (2) TOGETHER are NOT sufficient.

</details>

**1.** *(Easy)* What is $84 \times 25$?

(A) 1,900 (B) 2,000 (C) 2,100 (D) 2,150 (E) 2,400

<details>
<summary>Answer</summary>

**(C).** $84 \times 100 / 4 = 8400 / 4 = 2100$.

</details>

**2.** *(Easy)* What is $95^2$?

(A) 8,925 (B) 9,005 (C) 9,025 (D) 9,125 (E) 9,225

<details>
<summary>Answer</summary>

**(C).** Ends in 5: $9 \times 10 = 90$, then append 25: 9025. Or $(100 - 5)^2 = 10{,}000 - 1000 + 25$.

</details>

**3.** *(Easy)* Which of the following is closest to $2^{20}$?

(A) $10^4$ (B) $10^5$ (C) $10^6$ (D) $10^7$ (E) $2 \times 10^7$

<details>
<summary>Answer</summary>

**(C).** $2^{20} = (2^{10})^2 = 1024^2 \approx (10^3)^2 = 10^6$. The exact value is 1,048,576.

</details>

**4.** *(Medium)* What is $999 \times 37$?

(A) 36,663 (B) 36,936 (C) 36,963 (D) 36,973 (E) 37,963

<details>
<summary>Answer</summary>

**(C).** $999 \times 37 = 1000 \times 37 - 37 = 37{,}000 - 37 = 36{,}963$. The units digit alone ($9 \times 7 = 63$, ending in 3) eliminates (B), and (E) forgets to subtract.

</details>

**5.** *(Medium)* Which of the following is closest to $\dfrac{(3.9 \times 10^5)(6.1 \times 10^{-3})}{1.2 \times 10^2}$?

(A) 0.2 (B) 2 (C) 20 (D) 200 (E) 2,000

<details>
<summary>Answer</summary>

**(C).** Front parts: $\tfrac{4 \times 6}{1.2} = 20$. Powers of 10: $10^{5 - 3 - 2} = 10^0$. So the value is about 20 (exactly 19.825).

</details>

**6.** *(Medium)* What is $\sqrt{7921}$?

(A) 79 (B) 81 (C) 89 (D) 91 (E) 99

<details>
<summary>Answer</summary>

**(C).** $80^2 = 6400$ and $90^2 = 8100$, so the root is between 80 and 90, which leaves 81 and 89. A square ending in 1 has a root ending in 1 or 9, and 7921 is much closer to 8100 than to 6400, so try 89: $89^2 = 8100 - 180 + 1 = 7921$.

</details>

**7.** *(Medium)* Given that $1.05^{14} \approx 2$, which of the following is closest to $1.05^{42}$?

(A) 3.1 (B) 4 (C) 6 (D) 8 (E) 16

<details>
<summary>Answer</summary>

**(D).** $1.05^{42} = (1.05^{14})^3 \approx 2^3 = 8$. (The true value is about 7.76.) Choice (C) multiplies 2 by 3 instead of cubing, (B) squares instead of cubing, and (A) is simple growth, $1 + 42 \times 0.05 = 3.1$, which ignores compounding.

</details>

**8.** *(Medium)* 412 is approximately what percent of 1,987?

(A) 2% (B) 5% (C) 21% (D) 25% (E) 48%

<details>
<summary>Answer</summary>

**(C).** $\tfrac{412}{1987} \approx \tfrac{400}{2000} = 20\%$. Both numbers were rounded down by similar small amounts, and the true value is about 20.7%, so 21% is closest. Choice (E) inverts the ratio ($\tfrac{1987}{412} \approx 4.8$) and then misplaces the decimal point.

</details>

**9.** *(Hard)* Which of the following is the greatest?

(A) $2^{30}$ (B) $3^{20}$ (C) $5^{12}$ (D) $6^{11}$ (E) $10^9$

<details>
<summary>Answer</summary>

**(B).** Common exponent: $2^{30} = 8^{10}$ and $3^{20} = 9^{10}$, so (B) beats (A). Next, $2^{30} = (2^{10})^3 = 1024^3 > 10^9$, so (A), and therefore (B), beats (E). Finally, (C) and (D) are both below $10^9$: $5^{12} = \tfrac{10^{12}}{2^{12}} = \tfrac{10^{12}}{4096} < 10^9$, and $6^{11} = 6 \times 36^5 < 6 \times 40^5 = 6 \times 1.024 \times 10^8 \approx 6.1 \times 10^8$. So (B) is the greatest.

</details>

**10.** *(Hard)* Let $a = \tfrac{7}{11}$, $b = 0.636$ and $c = \sqrt{0.4}$. Which of the following is true?

(A) $a < b < c$ (B) $b < a < c$ (C) $c < a < b$ (D) $c < b < a$ (E) $b < c < a$

<details>
<summary>Answer</summary>

**(D).** $a = \tfrac{7}{11} = 0.\overline{63} = 0.636363\ldots$, which is greater than $b = 0.636$. For $c$, compare squares: $b^2 = 0.636^2 \approx 0.4045 > 0.4 = c^2$, so $c < b$. (In fact $c \approx 0.632$.) Order: $c < b < a$. The trap is to treat $\tfrac{7}{11}$ and $0.636$ as equal.

</details>

**11.** *(Hard, Data Sufficiency)* Is the positive number $n$ greater than 50?

(1) $n^2 > 2400$

(2) $n^3 < 125{,}500$

<details>
<summary>Answer</summary>

**(E).** (1): $n > \sqrt{2400} \approx 48.99$, since $49^2 = 2401$. Both 49 and 51 fit. Not sufficient. (2): $50^3 = 125{,}000$, so the bound allows $n$ slightly above 50 as well as anything below. Not sufficient. Together: $n$ is between about 48.99 and a little over 50. Both $n = 49.5$ (since $49.5^3 \approx 121{,}287$) and $n = 50.01$ (since $50.01^3 \approx 125{,}075$) satisfy both statements, and they give different answers. Not sufficient. The trap is (C), from rounding statement (2) to "$n < 50$".

</details>

**12.** *(Hard)* Which of the following is closest to $\sqrt{\dfrac{1{,}000{,}000}{62}}$?

(A) 40 (B) 80 (C) 127 (D) 160 (E) 400

<details>
<summary>Answer</summary>

**(C).** $\sqrt{\tfrac{10^6}{62}} = \tfrac{1000}{\sqrt{62}}$, and $\sqrt{62} \approx 7.9$ (just under 8). So the value is a little more than $\tfrac{1000}{8} = 125$. Only 127 is close. Choice (E) is $\tfrac{1000}{2.5}$, from mistaking $\sqrt{62}$ for $\sqrt{6.2} \approx 2.5$.

</details>

> [!NOTE]
> If you use Claude Code, the `quantome-math` plugin (`/plugin install quantome-math@quantome`) can confirm an exact value after you have estimated it. Practise the estimate first: on test day it is all you have.

## Takeaways

- Memorise squares to $25^2$, cubes to $10^3$, powers of 2 to $2^{12}$ and the common fraction–decimal–percent equivalents.
- Shortcuts are algebra: $\times 25 = \times 100 \div 4$, $(m - d)(m + d) = m^2 - d^2$, $(100 - a)(100 - b) = 100(100 - a - b) + ab$.
- Cancel and rearrange before multiplying; GMAT numbers are built to simplify.
- Estimate with a direction: know whether your approximation is too high or too low, and use bounds to prove an interval.
- Order numbers with a common form, benchmarks, or a common exponent. Compare square roots by squaring.
- Use scientific notation for very large or small numbers, and interpolate square roots: $\sqrt{m^2 + d} \approx m + \tfrac{d}{2m}$.
- Look at how far apart the answer choices are before deciding how precisely to compute.

## Further reading

- GMAC, *GMAT Official Guide* (current edition): practise these techniques on its retired Problem Solving questions, timing yourself.
- Related chapters: [Fractions, decimals and percents](../../arithmetic/fractions-decimals-percents/), [Exponents and roots](../../algebra/exponents-and-roots/) and [Problem-solving strategies](../../getting-started/problem-solving-strategies/).
