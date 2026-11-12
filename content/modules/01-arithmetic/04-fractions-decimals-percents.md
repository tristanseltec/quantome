+++
summary = "Compute and compare fractions, know which decimals terminate or repeat, and handle percent change, successive changes and reverse percents without a calculator."
+++

# Fractions, Decimals & Percents

Fractions, decimals and percents are three spellings of the same idea: a part of a whole. $\tfrac38$, $0.375$ and $37.5\%$ are the same number. The GMAT rewards moving freely between the three forms, because each form makes a different job easy. Fractions are best for multiplying and cancelling, decimals for ordering, and percents for describing change. This chapter covers the skills in that order, then spends most of its time on percents, which appear in a large share of Quant questions and in almost every word-problem topic.

## Key ideas

### Operations with fractions

A fraction $\tfrac{a}{b}$ means "$a$ divided by $b$". Every rule follows from that.

- **Adding and subtracting** need a common denominator, because you can only add pieces of the same size:
  $\tfrac23 + \tfrac34 = \tfrac{8}{12} + \tfrac{9}{12} = \tfrac{17}{12}$. Use the LCM of the denominators to keep numbers small: $\tfrac56 - \tfrac14 = \tfrac{10}{12} - \tfrac{3}{12} = \tfrac{7}{12}$.
- **Multiplying**: multiply tops and bottoms, cancelling first. $\tfrac{14}{15} \times \tfrac{25}{28} = \tfrac{1}{3} \times \tfrac{5}{2} = \tfrac56$ (cancel 14 with 28 and 25 with 15).
- **Dividing**: multiply by the reciprocal, because dividing by $\tfrac{c}{d}$ asks "how many $\tfrac{c}{d}$s fit?", and that is $\tfrac{d}{c}$ per unit. $\tfrac34 \div \tfrac{9}{10} = \tfrac34 \times \tfrac{10}{9} = \tfrac{5}{6}$.
- **Complex fractions** (fractions inside fractions): simplify the top and the bottom separately, then divide. Or multiply top and bottom by the LCM of all the small denominators.

> [!TIP]
> Cancel before you multiply. On a no-calculator test, $\tfrac{36}{49} \times \tfrac{35}{48}$ is easy if you first cancel 36 with 48 (to $\tfrac34$) and 35 with 49 (to $\tfrac57$), giving $\tfrac{15}{28}$. Multiplying out first creates four-digit numbers that you then have to reduce.

### Comparing fractions

Choose the method that fits the numbers:

1. **Cross-multiply.** For positive fractions, $\tfrac{a}{b} < \tfrac{c}{d}$ exactly when $ad < bc$. (Multiply both sides by the positive number $bd$.) Compare $\tfrac79$ and $\tfrac{11}{14}$: $7 \times 14 = 98 < 99 = 9 \times 11$, so $\tfrac79 < \tfrac{11}{14}$.
2. **Benchmarks.** Compare each fraction to $\tfrac12$, $1$ or another easy value. $\tfrac{7}{15}$ is below $\tfrac12$ and $\tfrac{8}{15}$ is above, so no further work is needed.
3. **Distance from 1.** $\tfrac{13}{16}$ is $\tfrac{3}{16}$ short of 1 and $\tfrac56$ is $\tfrac16$ short. Since $\tfrac{3}{16} > \tfrac{3}{18} = \tfrac16$, the fraction $\tfrac{13}{16}$ is farther from 1, so it is smaller.
4. **Same numerator or same denominator.** With the same numerator, the larger denominator gives the smaller fraction: $\tfrac{5}{11} < \tfrac{5}{9}$.

**Adding to the top and the bottom moves a fraction towards 1.** For a positive fraction less than 1, adding the same positive amount to its numerator and denominator makes it larger (closer to 1): $\tfrac{3}{5} < \tfrac{4}{6} < \tfrac{5}{7}$. For a fraction greater than 1, the same move makes it smaller. You can check this by cross-multiplying: $\tfrac{a}{b} < \tfrac{a+k}{b+k} \iff ab + ak < ab + bk \iff a < b$.

### Terminating decimals

A fraction in lowest terms gives a **terminating** decimal exactly when its denominator has no prime factors other than 2 and 5.

**Why.** A terminating decimal is a fraction over a power of 10, such as $0.075 = \tfrac{75}{1000}$, and $10^k = 2^k 5^k$. So the reduced denominator can only contain 2s and 5s. Conversely, if the denominator is $2^a 5^b$, multiply the top and bottom by enough 2s or 5s to make it $10^{\max(a, b)}$:

$$
\frac{3}{40} = \frac{3}{2^3 \cdot 5} = \frac{3 \cdot 5^2}{2^3 \cdot 5^3} = \frac{75}{1000} = 0.075.
$$

The number of decimal places is $\max(a, b)$, here 3.

> [!WARNING]
> **Reduce first.** $\tfrac{21}{56}$ looks like it has a 7 in the denominator, but $\tfrac{21}{56} = \tfrac38 = 0.375$ terminates. And $\tfrac{9}{30}$ looks like it has a 3, but $\tfrac{9}{30} = \tfrac{3}{10}$. Always cancel before checking the denominator.

### Repeating decimals

Every fraction that does not terminate **repeats**, because long division by $d$ can only produce $d$ different remainders, so the digits must cycle. Some to know:

- $\tfrac19 = 0.\overline{1}$, $\tfrac{2}{9} = 0.\overline{2}$, and so on: ninths repeat their numerator.
- $\tfrac{1}{11} = 0.\overline{09}$, $\tfrac{2}{11} = 0.\overline{18}$: elevenths repeat $9 \times$ the numerator, as two digits.
- $\tfrac17 = 0.\overline{142857}$, a 6-digit cycle. The other sevenths use the same six digits in rotation: $\tfrac37 = 0.\overline{428571}$.

**Converting a repeating decimal to a fraction.** A block of $k$ repeating digits goes over $k$ nines: $0.\overline{27} = \tfrac{27}{99} = \tfrac{3}{11}$. This works because if $x = 0.\overline{27}$ then $100x = 27.\overline{27}$, and subtracting gives $99x = 27$.

**Finding the $n$th digit.** For a cycle of length $L$, the $n$th digit after the decimal point is at position ($n$ mod $L$) in the cycle, using position $L$ when the remainder is 0. This is the same cycle logic as units digits in [Remainders and units digits](../../arithmetic/remainders-and-units-digits/).

### Percent of

"Percent" means "per hundred", so $p\% = \tfrac{p}{100}$. "Of" means multiply.

- $15\%$ of $240$ is $0.15 \times 240 = 36$. Break it up mentally: $10\%$ is 24 and $5\%$ is 12.
- $x\%$ of $y$ equals $y\%$ of $x$, because both are $\tfrac{xy}{100}$. So $16\%$ of $25$ is $25\%$ of $16$, which is 4.
- "$A$ is what percent of $B$?" means $\tfrac{A}{B} \times 100\%$.

Fraction equivalents are often faster than decimals: $12.5\% = \tfrac18$, $37.5\% = \tfrac38$, $62.5\% = \tfrac58$, $87.5\% = \tfrac78$, $16\tfrac23\% = \tfrac16$, $33\tfrac13\% = \tfrac13$. A fuller table is in [Estimation and mental math](../../arithmetic/estimation-and-mental-math/).

### Percent change

> [!IMPORTANT]
> $$\text{Percent change} = \frac{\text{new} - \text{old}}{\text{old}} \times 100\%$$
> An increase of $p\%$ multiplies a value by $\left(1 + \tfrac{p}{100}\right)$. A decrease of $p\%$ multiplies it by $\left(1 - \tfrac{p}{100}\right)$.

The denominator is always the **original** value. A drop from 80 to 60 is a $\tfrac{20}{80} = 25\%$ decrease, while a rise from 60 to 80 is a $\tfrac{20}{60} = 33\tfrac13\%$ increase. The same 20-unit gap gives different percents, because the base differs.

**Percent versus percentage points.** If a rate rises from 20% to 25%, it rose by **5 percentage points**, but by $\tfrac{5}{20} = 25\%$ in relative terms. Read carefully to see which the question wants.

### Successive changes

Percent changes in sequence **multiply**. They do not add, because each change applies to a new base.

- $+10\%$ then $+20\%$: $1.1 \times 1.2 = 1.32$, a 32% increase (not 30%).
- $+20\%$ then $-20\%$: $1.2 \times 0.8 = 0.96$, a 4% decrease (not 0%).
- $+50\%$ then $-50\%$: $1.5 \times 0.5 = 0.75$, a 25% decrease.

For two changes of $a\%$ and $b\%$ (use negative numbers for decreases), the net change is

$$
a + b + \frac{ab}{100} \text{ percent},
$$

which you get by expanding $\left(1 + \tfrac{a}{100}\right)\left(1 + \tfrac{b}{100}\right)$. For $+20$ and $-20$ this gives $0 - 4 = -4$. A rise and a fall of the same percent always give a net loss of $\tfrac{p^2}{100}$ percent.

The order of the changes does not matter, since multiplication is commutative: $-20\%$ then $+20\%$ also gives $0.96$.

> [!TIP]
> **Start with 100.** If no starting value is given, call it 100. Every percent becomes a plain number, and the final answer can be read off directly. For $+20\%$, $-25\%$, $+10\%$: $100 \to 120 \to 90 \to 99$, a 1% net decrease.

### "Percent more than" versus "percent of"

These phrases build most of the trap answers in percent questions.

- "$A$ is 25% **more than** $B$" means $A = 1.25B$.
- "$A$ is 125% **of** $B$" means the same thing, $A = 1.25B$.
- "$A$ is 25% **of** $B$" means $A = 0.25B$, which is very different.
- "$A$ is 20% **less than** $B$" means $A = 0.8B$.

**The base is the word after "than" or "of".** If $A$ is 25% more than $B$, then $B$ is **not** 25% less than $A$. With $B = 100$, $A = 125$, and $B$ is $\tfrac{25}{125} = 20\%$ less than $A$. In general, if $A = (1 + r)B$ then $B$ is $\tfrac{r}{1 + r}$ less than $A$.

### Reverse percents

When you know the value **after** a percent change and want the original, **divide** by the multiplier. Never subtract the percent from the new value.

> [!IMPORTANT]
> $$\text{original} = \frac{\text{new}}{\text{multiplier}}$$
> A coat that costs \$64 after a 20% discount was $\tfrac{64}{0.8} = \$80$, not $64 \times 1.2 = \$76.80$.

The same idea handles chains: if a price after a 15% discount and then 8% tax is \$91.80, the original is $\tfrac{91.80}{0.85 \times 1.08}$. Profit, markup and discount questions are developed further in [Profit, discount and percent problems](../../word-problems/profit-discount-and-percent-problems/).

> [!WARNING]
> Wrong answers in percent questions are built from:
> - using the new value instead of the original as the base for percent change;
> - adding successive percents instead of multiplying the factors;
> - reversing a percent by applying the opposite percent ($+20\%$ is undone by $-16\tfrac23\%$, not $-20\%$);
> - confusing "percent of" with "percent more than", or percent with percentage points;
> - checking the denominator for terminating decimals before reducing the fraction.

## Worked examples

**Example 1** *(Easy)*. Which of the following fractions is the greatest?

(A) $\tfrac58$ (B) $\tfrac{7}{11}$ (C) $\tfrac{9}{14}$ (D) $\tfrac{13}{20}$ (E) $\tfrac23$

**Solution.** Use $\tfrac23$ as a benchmark and cross-multiply each other choice against it, comparing $3 \times \text{numerator}$ with $2 \times \text{denominator}$:

- $\tfrac58$: $15$ vs $16$, so smaller than $\tfrac23$.
- $\tfrac{7}{11}$: $21$ vs $22$, smaller.
- $\tfrac{9}{14}$: $27$ vs $28$, smaller.
- $\tfrac{13}{20}$: $39$ vs $40$, smaller.

So $\tfrac23$ is the greatest. **Answer: (E).** In decimals the choices are $0.625$, $0.636\ldots$, $0.643\ldots$, $0.65$ and $0.667$, which are close together. That is why the benchmark method beats converting all five.

**Example 2** *(Medium)*. Which of the following fractions is equal to a terminating decimal?

(A) $\tfrac{7}{12}$ (B) $\tfrac{11}{30}$ (C) $\tfrac{21}{56}$ (D) $\tfrac{5}{18}$ (E) $\tfrac{9}{14}$

**Solution.** Reduce, then look at the denominator:

- $\tfrac{7}{12}$: denominator $2^2 \cdot 3$. Repeats.
- $\tfrac{11}{30}$: $2 \cdot 3 \cdot 5$. Repeats.
- $\tfrac{21}{56} = \tfrac{3}{8}$: $2^3$. **Terminates** ($0.375$).
- $\tfrac{5}{18}$: $2 \cdot 3^2$. Repeats.
- $\tfrac{9}{14}$: $2 \cdot 7$. Repeats.

**Answer: (C).** If you don't reduce $\tfrac{21}{56}$, the 7 in 56 makes it look like a repeating decimal.

**Example 3** *(Medium)*. The number $A$ is 25% greater than the positive number $B$. By what percent is $B$ less than $A$?

(A) 15% (B) 20% (C) 25% (D) 30% (E) 80%

**Solution.** Pick $B = 100$, so $A = 125$. $B$ is $25$ less than $A$, and as a percent of $A$ that is $\tfrac{25}{125} = 20\%$. **Answer: (B).**

The trap (C) assumes percent changes reverse symmetrically. Choice (E) is "$B$ is 80% **of** $A$", which is true but answers a different question.

**Example 4** *(Medium)*. The price of a share rises 20% on Monday, falls 25% on Tuesday and rises 10% on Wednesday. What is the net change over the three days?

(A) a 5% decrease (B) a 1% decrease (C) no change (D) a 1% increase (E) a 5% increase

**Solution.** Start at 100: $100 \times 1.2 = 120$, then $120 \times 0.75 = 90$, then $90 \times 1.1 = 99$. The net change is a 1% decrease. **Answer: (B).** The trap (E) adds the percents: $20 - 25 + 10 = 5$.

**Example 5** *(Hard)*. A jacket is discounted by 15%, and then 8% sales tax is added to the discounted price. The customer pays \$91.80. What was the original price of the jacket?

(A) \$85.00 (B) \$90.00 (C) \$95.00 (D) \$100.00 (E) \$108.00

**Solution.** The total multiplier is $0.85 \times 1.08$. Compute it without a calculator: $0.85 \times 1.08 = 0.85 + 0.85 \times 0.08 = 0.85 + 0.068 = 0.918$. So the original price is $\tfrac{91.80}{0.918} = \$100$. **Answer: (D).**

**Fast method: backsolve.** The choices include a round \$100. Test it: $100 \to 85 \to 85 \times 1.08 = 91.80$. It matches at once.

Choices (A) and (E) are what a \$100 jacket costs after only one of the two changes.

## Practice

<details>
<summary>Data Sufficiency answer choices (the same on every DS question)</summary>

- **(A)** Statement (1) ALONE is sufficient, but statement (2) alone is not sufficient.
- **(B)** Statement (2) ALONE is sufficient, but statement (1) alone is not sufficient.
- **(C)** BOTH statements TOGETHER are sufficient, but NEITHER statement ALONE is sufficient.
- **(D)** EACH statement ALONE is sufficient.
- **(E)** Statements (1) and (2) TOGETHER are NOT sufficient.

</details>

**1.** *(Easy)* What is the value of $\left(\tfrac23 + \tfrac14\right) \div \tfrac56$?

(A) $\tfrac{11}{15}$ (B) $\tfrac{55}{72}$ (C) $\tfrac{10}{11}$ (D) $\tfrac{11}{10}$ (E) $\tfrac65$

<details>
<summary>Answer</summary>

**(D).** $\tfrac23 + \tfrac14 = \tfrac{8}{12} + \tfrac{3}{12} = \tfrac{11}{12}$. Dividing by $\tfrac56$ means multiplying by $\tfrac65$: $\tfrac{11}{12} \times \tfrac65 = \tfrac{66}{60} = \tfrac{11}{10}$. Choice (B) multiplies by $\tfrac56$ instead of dividing.

</details>

**2.** *(Easy)* Which fraction equals $0.363636\ldots$, where the digits 36 repeat forever?

(A) $\tfrac{4}{11}$ (B) $\tfrac{9}{25}$ (C) $\tfrac{36}{100}$ (D) $\tfrac38$ (E) $\tfrac25$

<details>
<summary>Answer</summary>

**(A).** A two-digit repeating block goes over 99: $\tfrac{36}{99} = \tfrac{4}{11}$. Choices (B) and (C) both equal $0.36$ exactly, which terminates.

</details>

**3.** *(Easy)* 30% of 70 is what percent of 140?

(A) 10% (B) 15% (C) 20% (D) 30% (E) 60%

<details>
<summary>Answer</summary>

**(B).** $30\%$ of $70$ is $21$, and $\tfrac{21}{140} = \tfrac{3}{20} = 15\%$. Faster: 140 is twice 70, so the same amount is half the percent.

</details>

**4.** *(Medium)* What is the 100th digit after the decimal point in the decimal form of $\tfrac37$?

(A) 1 (B) 2 (C) 4 (D) 5 (E) 8

<details>
<summary>Answer</summary>

**(D).** $\tfrac37 = 0.\overline{428571}$, a cycle of 6. Since $100 = 6 \times 16 + 4$, the 100th digit is the 4th in the cycle: 5.

</details>

**5.** *(Medium)* A share price falls 20% on Monday. By what percent must it rise on Tuesday to return to its value before Monday?

(A) 16% (B) 20% (C) 24% (D) 25% (E) 30%

<details>
<summary>Answer</summary>

**(D).** $100 \to 80$. To get back to 100 it must gain 20 on a base of 80: $\tfrac{20}{80} = 25\%$. The trap is (B).

</details>

**6.** *(Medium)* How many of the following fractions are equal to terminating decimals?

$\tfrac{3}{40}$, $\tfrac{7}{56}$, $\tfrac{11}{60}$, $\tfrac{13}{65}$, $\tfrac{5}{24}$

(A) 1 (B) 2 (C) 3 (D) 4 (E) 5

<details>
<summary>Answer</summary>

**(C).** $\tfrac{3}{40}$ (denominator $2^3 \cdot 5$) terminates. $\tfrac{7}{56} = \tfrac18$ terminates. $\tfrac{11}{60}$ has a 3 in the denominator and cannot be reduced, so it repeats. $\tfrac{13}{65} = \tfrac15$ terminates. $\tfrac{5}{24}$ has a 3, so it repeats. Three terminate.

</details>

**7.** *(Medium)* A class grew from 200 to 240 students. Over the same period, the percent of students taking Spanish rose from 40% to 50%. By what percent did the number of students taking Spanish increase?

(A) 10% (B) 20% (C) 25% (D) 50% (E) 60%

<details>
<summary>Answer</summary>

**(D).** Before: $0.4 \times 200 = 80$. After: $0.5 \times 240 = 120$. The increase is $\tfrac{40}{80} = 50\%$. Choice (A) is the change in percentage points, and (C) is the relative change in the percentage alone ($\tfrac{10}{40}$), ignoring the growth of the class. (B) is the growth of the class alone.

</details>

**8.** *(Hard)* The number $x$ is 40% greater than $y$, and $z$ is 30% less than $x$. If $y > 0$, then $z$ is what percent of $y$?

(A) 70% (B) 90% (C) 98% (D) 102% (E) 110%

<details>
<summary>Answer</summary>

**(C).** $x = 1.4y$ and $z = 0.7x = 0.7 \times 1.4y = 0.98y$. So $z$ is 98% of $y$. The trap (E) adds the percents ($+40 - 30 = +10$).

</details>

**9.** *(Hard)* Which of the following is closest to 1?

(A) $\tfrac{17}{19}$ (B) $\tfrac{19}{17}$ (C) $\tfrac{23}{25}$ (D) $\tfrac{25}{23}$ (E) $\tfrac{29}{31}$

<details>
<summary>Answer</summary>

**(E).** Each fraction differs from 1 by $\tfrac{2}{\text{denominator}}$: $\tfrac{2}{19}$, $\tfrac{2}{17}$, $\tfrac{2}{25}$, $\tfrac{2}{23}$, $\tfrac{2}{31}$. The largest denominator, 31, gives the smallest gap. Note that $\tfrac{19}{17}$ is farther from 1 than $\tfrac{17}{19}$, because its gap is measured over the smaller denominator.

</details>

**10.** *(Hard)* A retailer marks up the cost of an item by 40%, then sells it at 15% off the marked price. The retailer's profit is \$19. What did the item cost the retailer?

(A) \$80 (B) \$95 (C) \$100 (D) \$119 (E) \$125

<details>
<summary>Answer</summary>

**(C).** Selling price $= 1.4 \times 0.85 \times \text{cost} = 1.19 \times \text{cost}$, so the profit is $0.19 \times \text{cost} = 19$ and the cost is \$100. Backsolving with \$100 also works at once: marked price \$140, selling price \$119, profit \$19. Choice (D) is the selling price, not the cost.

</details>

**11.** *(Hard, Data Sufficiency)* If $k$ is a positive integer, is $\tfrac{k}{120}$ equal to a terminating decimal?

(1) $k$ is divisible by 3.

(2) $k$ is even.

<details>
<summary>Answer</summary>

**(A).** $120 = 2^3 \cdot 3 \cdot 5$. The decimal terminates exactly when the 3 cancels, that is when 3 divides $k$. (1): yes, always. Sufficient. (2): $k = 2$ gives $\tfrac{1}{60}$ (repeats), but $k = 6$ gives $\tfrac{1}{20} = 0.05$ (terminates). Not sufficient. The 2s in the denominator never matter.

</details>

**12.** *(Medium, Data Sufficiency)* The price of an item is increased by $p\%$, and then the new price is decreased by $p\%$, where $p < 100$. Is the final price lower than the original price?

(1) $p = 10$

(2) $p > 0$

<details>
<summary>Answer</summary>

**(D).** The final price is $\left(1 + \tfrac{p}{100}\right)\left(1 - \tfrac{p}{100}\right) = 1 - \tfrac{p^2}{10{,}000}$ times the original. This is below 1 whenever $p \ne 0$. (1): $1.1 \times 0.9 = 0.99$, yes. Sufficient. (2): $p > 0$ means $p^2 > 0$, so yes. Sufficient. Without either statement $p = 0$ would be possible (no change), which is why the stem alone does not answer the question.

</details>

> [!NOTE]
> If you use Claude Code, the `quantome-math` plugin (`/plugin install quantome-math@quantome`) can check percent chains and fraction arithmetic after you have done them by hand.

## Takeaways

- Use fractions to multiply and cancel, decimals to order, and percents to describe change.
- Compare fractions by cross-multiplying, against benchmarks, or by distance from 1.
- A reduced fraction terminates exactly when its denominator is $2^a 5^b$, with $\max(a, b)$ decimal places. Reduce first.
- A $k$-digit repeating block equals that block over $k$ nines.
- Percent change uses the **original** as the base. Successive changes multiply: net $= a + b + \tfrac{ab}{100}$ percent.
- "More than" and "of" name the base. If $A$ is $r$ more than $B$, then $B$ is $\tfrac{r}{1 + r}$ less than $A$.
- Reverse a percent change by dividing by the multiplier. Start with 100 when no value is given.

## Further reading

- GMAC, *GMAT Official Guide* (current edition): its Problem Solving section has many retired percent and fraction questions.
- Related chapters: [Ratios](../../arithmetic/ratios/), [Estimation and mental math](../../arithmetic/estimation-and-mental-math/) and [Profit, discount and percent problems](../../word-problems/profit-discount-and-percent-problems/).
