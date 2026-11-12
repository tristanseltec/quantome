+++
summary = "Treat every mixture as a weighted average, solve mixing, dilution and replacement problems with the seesaw method, and compare simple and compound interest, including compounding periods and quick approximations for growth."
+++

# Mixtures & Interest

A mixture problem asks what happens when you combine things that differ in some property: acid solutions of different strengths, coffees at different prices, classes with different average scores. An interest problem asks how money grows over time. They look like separate topics, but they share one idea. In a mixture, the result is a **weighted average** of the parts. In interest, growth is either **added** each period (simple interest) or **multiplied** each period (compound interest), and most questions test whether you know which.

This chapter builds both ideas from scratch, with the fast GMAT methods: the seesaw for weighted averages, the "track the pure ingredient" rule for dilution, the $(1 - f)^k$ formula for repeated replacement, and the approximations that make compound growth manageable without a calculator. It assumes comfort with percents ([Fractions, decimals and percents](../../arithmetic/fractions-decimals-percents/)) and ratios ([Ratios](../../arithmetic/ratios/)).

## Key ideas

### Weighted averages

If $w_1$ units have value $a$ and $w_2$ units have value $b$, the combined value is

$$
c = \frac{w_1 a + w_2 b}{w_1 + w_2}.
$$

"Value" can be a concentration (percent acid), a price per pound, an average score, or an average salary. "Units" can be litres, pounds, students or employees. The structure is identical in each case: total amount of the property divided by total quantity.

Two consequences follow immediately:

- The mixture's value $c$ always lies **between** $a$ and $b$. A 20% solution mixed with a 50% solution can never produce 55% or 15%. This alone eliminates answer choices.
- $c$ is closer to the value with the **larger weight**. If you have more of the 20% solution, the mix is below 35%.

### The seesaw (alligation) method, derived

Start from the weighted-average equation and multiply out:

$$
w_1 a + w_2 b = (w_1 + w_2)c \quad\Rightarrow\quad w_1(c - a) = w_2(b - c).
$$

So

$$
\frac{w_1}{w_2} = \frac{b - c}{c - a}.
$$

> [!IMPORTANT]
> **Seesaw rule.** The quantities are in the **inverse** ratio of their distances from the mixture's value:
> $$\frac{w_1}{w_2} = \frac{\text{distance from } c \text{ to } b}{\text{distance from } c \text{ to } a}$$

Picture a seesaw with $a$ and $b$ at the ends and the balance point at $c$. The heavier weight sits closer to the balance point. This is the same principle as a lever: weight times distance is equal on both sides, which is exactly $w_1(c - a) = w_2(b - c)$.

Example: coffee at \$8 per pound and \$14 per pound, mixed to sell at \$10 per pound. Distances: $10 - 8 = 2$ and $14 - 10 = 4$. The quantities are in the ratio $4 : 2 = 2 : 1$, with **more of the \$8 coffee** (it is closer to \$10). For 30 pounds of blend, that is 20 pounds at \$8 and 10 pounds at \$14.

> [!TIP]
> Draw a number line: $a$, then $c$, then $b$. Write the two distances above it, then **cross them over**: the distance on the right belongs to the quantity on the left. You can solve most mixture questions in 20 seconds this way, without an equation.

### Mixing solutions: track the pure ingredient

For concentration problems, the most reliable method is to track the **amount of the pure substance**, because it only changes when you add or remove that substance.

- **Diluting** (adding water): the amount of salt stays the same; the volume grows. 15 L of 40% salt water contains 6 L of salt. To make it 25%, the total must be $6 / 0.25 = 24$ L, so add 9 L of water.
- **Evaporating** (removing water): the salt stays; the volume shrinks. 50 kg of 4% salt water contains 2 kg of salt. At 5%, the total must be $2 / 0.05 = 40$ kg, so 10 kg of water evaporates.
- **Adding pure substance**: both the salt and the volume grow. Write $\tfrac{\text{salt} + x}{\text{volume} + x} = \text{target}$.

The seesaw still works for these: water is a 0% solution, and pure substance is a 100% solution.

> [!WARNING]
> Concentrations do not add. Mixing equal amounts of 20% and 40% solution gives 30%, not 60%. And adding 10 L of water to a 30% solution does not "lower it by 10 percentage points": the result depends on how much solution you started with.

### Replacement problems

A container holds $V$ litres with concentration $C_0$. You remove $x$ litres of the mixture and replace them with water, and you repeat this $k$ times. What is the final concentration?

Each removal takes out a fraction $f = \tfrac{x}{V}$ of **everything** in the container, including that fraction of the substance. Adding water brings the volume back to $V$ but adds no substance. So after each step, the amount of substance is multiplied by $(1 - f)$:

$$
C_k = C_0 \left(1 - \frac{x}{V}\right)^k.
$$

For example, 40 L of pure juice, remove 10 L and replace with water, twice: juice left $= 40 \times \left(\tfrac34\right)^2 = 22.5$ L.

> [!WARNING]
> The trap answer is the "linear" one: 10 L removed twice is 20 L of juice removed, leaving 20 L. That is wrong because the second removal takes out a *mixture*, only three-quarters of which is juice. Repeated replacement is **multiplicative**, like compound interest in reverse.

If the replacement liquid is not water (say, a 10% solution), the formula changes; in that case, track the substance step by step: subtract $f$ of the current amount, then add what the replacement brings in.

### Mixtures of prices and other weighted averages

The same equations apply to anything averaged by quantity:

- Two classes with averages 72 and 84, combined average 79: distances 7 and 5, so the class sizes are in the ratio $5 : 7$.
- A firm's average salary is \$60k; managers average \$90k and others \$50k. Distances 30 and 10, so managers : others $= 10 : 30 = 1 : 3$, and managers are $\tfrac14$ of the staff.
- Adding more of an ingredient to an existing blend: treat the existing blend as one "ingredient" with its own price and weight.

### Simple interest

Simple interest is paid only on the original principal $P$. At annual rate $r$ for $t$ years:

$$
I = Prt, \qquad A = P(1 + rt).
$$

Growth is **linear**: the same dollar amount is added every year. Time must be in years, so 30 months is $t = 2.5$.

### Compound interest

With compound interest, each period's interest is added to the balance and earns interest itself. After one year at rate $r$, the balance is $P(1 + r)$; after two years, $P(1 + r)(1 + r)$; after $t$ years,

$$
A = P(1 + r)^t.
$$

Growth is **exponential**: the balance is multiplied by the same factor every year.

**Compounding periods.** If a nominal annual rate $r$ is compounded $n$ times per year, each period pays $\tfrac{r}{n}$, and there are $nt$ periods:

$$
A = P\left(1 + \frac{r}{n}\right)^{nt}.
$$

"8% per year compounded quarterly" means 2% per quarter. Over 6 months, that is two quarters: $5000 \times 1.02^2 = 5{,}202$.

> [!WARNING]
> "6% compounded semiannually" means 3% every half-year, **not** 6% every half-year. And the number of periods is $nt$, not $t$.

### Why compounding wins, and by how much

Expand two years of compounding:

$$
(1 + r)^2 = 1 + 2r + r^2.
$$

Simple interest gives $1 + 2r$. The difference is $r^2$ per dollar: the interest earned on the first year's interest. On \$10,000 at 10% for 2 years, compound beats simple by $10{,}000 \times 0.01 = \$100$. This is tiny for small $r$ and short times, which is why the GMAT can set questions where compound interest at a lower rate beats simple interest at a higher rate by only a few dollars (Example 4).

More frequent compounding helps for the same reason. A year of 10% compounded semiannually gives $1.05^2 = 1.1025$, an **effective annual rate** of 10.25%, versus 10% compounded annually.

### Comparing investments

To compare two investments, compute each one's final value (or growth factor) over the **same** period. Don't compare rates directly when the compounding differs. Useful facts:

- For the same nominal rate, more frequent compounding gives more.
- Compound always beats simple at the same rate for any period longer than one compounding period.
- A rate that doubles money in $T$ years will multiply it by 4 in $2T$ years and by 8 in $3T$ years, because $(1 + r)^{3T} = \left((1 + r)^T\right)^3 = 2^3$.

### Approximations for compound growth

When exact arithmetic is impractical, the GMAT says "approximately" or "closest to". Three tools cover nearly every case.

**1. The binomial approximation.** For small $r$,

$$
(1 + r)^n \approx 1 + nr + \frac{n(n-1)}{2}r^2.
$$

These are the first three terms of the binomial expansion. The first two give simple interest; the third term is the "interest on interest". For $1.02^{10}$: $1 + 0.2 + 45 \times 0.0004 = 1.218$ (the exact value is about 1.219).

**2. The rule of 72.** Money growing at $r$% per year doubles in about $\tfrac{72}{r}$ years. At 3%, about 24 years (the exact value is 23.4); at 8%, about 9 years. The rule comes from $(1 + r)^n = 2$, so $n = \tfrac{\ln 2}{\ln(1 + r)} \approx \tfrac{0.693}{r}$; 72 is used instead of 69.3 because it has many divisors and partly corrects for $\ln(1 + r)$ being slightly less than $r$.

**3. Bounding.** Compound growth is always at least simple growth. So $1.02^{10} > 1.2$. If the choices are 1.1, 1.22, 1.5 and 2, you are done.

> [!TIP]
> On "closest to" questions, look at how far apart the answer choices are. If they differ by 10% or more, simple interest is a good enough estimate. If two choices are close (like 60,000 and 61,000 in practice problem 9), add the $\tfrac{n(n-1)}{2}r^2$ term.

### Common traps

> [!WARNING]
> Wrong answer choices on mixture and interest problems come from:
> 1. **Averaging concentrations or prices without weights**: assuming equal quantities.
> 2. **Crossing the seesaw the wrong way**: giving the larger quantity to the value farther from the mix.
> 3. **Linear replacement**: subtracting the removed amount each time instead of multiplying by $(1 - f)$.
> 4. **Forgetting what stays constant**: the salt when water is added or evaporated.
> 5. **Using the annual rate for each compounding period**, or $t$ periods instead of $nt$.
> 6. **Confusing interest with final amount**: \$300 of interest versus a \$2,700 balance.

> [!NOTE]
> Readers using Claude Code can confirm their arithmetic with the `quantome-math` plugin (`/plugin install quantome-math@quantome`). Try the seesaw by hand first: it is faster than any tool.

## Worked examples

### Example 1 *(Easy)*

A grocer mixes coffee that costs \$8 per pound with coffee that costs \$14 per pound to make 30 pounds of a blend that costs \$10 per pound. How many pounds of the \$8 coffee are in the blend?

(A) 10 (B) 12 (C) 15 (D) 18 (E) 20

**Solution (seesaw).** Distances from \$10: the \$8 coffee is 2 away, the \$14 coffee is 4 away. Cross them over: \$8 coffee : \$14 coffee $= 4 : 2 = 2 : 1$. Two-thirds of 30 pounds is **20 pounds**, choice **(E)**.

**Solution (algebra).** $8x + 14(30 - x) = 300$, so $420 - 6x = 300$ and $x = 20$.

Choice (A), 10, is what you get by giving the larger share to the wrong coffee. Quick check: \$10 is closer to \$8 than to \$14, so there must be more \$8 coffee.

### Example 2 *(Medium)*

In a test, the students in class A averaged 72 points and the students in class B averaged 84 points. The two classes together averaged 79 points. If class A has 20 students, how many students are in class B?

(A) 14 (B) 20 (C) 24 (D) 28 (E) 30

**Solution.** Distances from 79: class A is 7 away, class B is 5 away. So A : B $= 5 : 7$. With 20 students in A, class B has $20 \times \tfrac75 = 28$. The answer is **(D)**.

Check: $\tfrac{72 \times 20 + 84 \times 28}{48} = \tfrac{1440 + 2352}{48} = \tfrac{3792}{48} = 79$. ✓ Choice (A), 14, is roughly $20 \times \tfrac57 \approx 14.3$, the seesaw crossed the wrong way. Note that 79 is above 78 (the midpoint), so class B must be the bigger class.

### Example 3 *(Medium)*

A 40-litre container is full of pure orange juice. Ten litres are removed and replaced with water. Then 10 litres of the mixture are removed and replaced with water. How many litres of orange juice are now in the container?

(A) 20 (B) 22.5 (C) 25 (D) 27.5 (E) 30

**Solution.** Each step removes $\tfrac{10}{40} = \tfrac14$ of the contents, so it keeps $\tfrac34$ of the juice. After two steps: $40 \times \left(\tfrac34\right)^2 = 40 \times \tfrac{9}{16} = 22.5$ litres, choice **(B)**.

Step by step: after the first replacement, 30 L of juice in 40 L. The second removal takes 10 L of a 75% mixture, which is 7.5 L of juice, leaving 22.5 L. Choice (A) is the linear trap ($40 - 10 - 10$), and (E) counts only one replacement.

### Example 4 *(Hard)*

Investment X is \$8,000 deposited at 10% annual interest, compounded annually. Investment Y is \$8,000 deposited at 11% annual simple interest. After 3 years, which investment is worth more, and by how much?

(A) Y, by \$80 (B) Y, by \$8 (C) They are worth the same (D) X, by \$8 (E) X, by \$80

**Solution.** X: $8000 \times 1.1^3 = 8000 \times 1.331 = 10{,}648$. Y: $8000 \times (1 + 3 \times 0.11) = 8000 \times 1.33 = 10{,}640$. X is worth \$8 more: **(D)**.

**Why it is so close.** $1.1^3 = 1 + 0.3 + 0.03 + 0.001$ (the binomial expansion, exactly). Simple interest at 10% would give $1.30$; the "interest on interest" adds $0.031$. Y's extra 1% per year adds $0.03$. The difference is $0.001$ of \$8,000, which is \$8. The trap is to reason "Y has the higher rate, so Y wins", or to misplace the decimal and choose \$80.

## Practice

**1.** *(Easy)* How many litres of water must be added to 15 litres of a 40% salt solution to dilute it to a 25% salt solution?

(A) 3 (B) 6 (C) 9 (D) 12 (E) 24

<details>
<summary>Answer</summary>

**(C) 9.** The salt is unchanged: $0.40 \times 15 = 6$ L. At 25%, 6 L of salt needs a total of $6 / 0.25 = 24$ L, so add $24 - 15 = 9$ L. Choice (E) is the new total volume, not the amount added.

Seesaw check: water (0%) and the 40% solution, target 25%: distances 25 and 15, so water : solution $= 15 : 25 = 3 : 5$, and $\tfrac35 \times 15 = 9$. ✓

</details>

**2.** *(Easy)* How much simple interest does \$2,400 earn in 30 months at an annual rate of 5%?

(A) \$120 (B) \$250 (C) \$300 (D) \$360 (E) \$600

<details>
<summary>Answer</summary>

**(C) \$300.** $I = Prt = 2400 \times 0.05 \times 2.5 = 300$. Choice (A) is one year's interest; (E) wrongly uses $t = 5$.

</details>

**3.** *(Medium)* A tank holds 50 kilograms of salt water that is 4% salt by weight. How many kilograms of water must evaporate so that the remaining solution is 5% salt?

(A) 1 (B) 2.5 (C) 5 (D) 10 (E) 12.5

<details>
<summary>Answer</summary>

**(D) 10.** Salt stays at $0.04 \times 50 = 2$ kg. At 5%, the total is $2 / 0.05 = 40$ kg, so $50 - 40 = 10$ kg of water evaporates. Choice (A) confuses the one-percentage-point change in concentration with the mass of water lost.

</details>

**4.** *(Medium)* A chemist mixes a 15% acid solution with a 25% acid solution to make 60 litres of a 21% acid solution. How many litres of the 15% solution does she use?

(A) 20 (B) 24 (C) 30 (D) 36 (E) 40

<details>
<summary>Answer</summary>

**(B) 24.** Distances from 21: the 15% solution is 6 away, the 25% solution is 4 away. Crossing over, 15% : 25% $= 4 : 6 = 2 : 3$, so the 15% solution is $\tfrac25 \times 60 = 24$ L. Check: $0.15 \times 24 + 0.25 \times 36 = 3.6 + 9 = 12.6 = 0.21 \times 60$. ✓ Choice (D) is the amount of the 25% solution.

</details>

**5.** *(Medium)* \$5,000 is invested at an annual interest rate of 8%, compounded quarterly. What is the investment worth after 6 months?

(A) \$5,200 (B) \$5,202 (C) \$5,400 (D) \$5,408 (E) \$5,832

<details>
<summary>Answer</summary>

**(B) \$5,202.** The quarterly rate is $8\% / 4 = 2\%$, and 6 months is 2 quarters: $5000 \times 1.02^2 = 5000 \times 1.0404 = 5{,}202$. Choice (A) is simple interest; (D) uses 4% per quarter; (E) uses 8% per quarter for 2 quarters.

</details>

**6.** *(Medium)* At a company, the average annual salary of all employees is \$60,000. Managers earn an average of \$90,000 and all other employees earn an average of \$50,000. What fraction of the employees are managers?

(A) $\tfrac18$ (B) $\tfrac16$ (C) $\tfrac15$ (D) $\tfrac14$ (E) $\tfrac13$

<details>
<summary>Answer</summary>

**(D) $\tfrac14$.** Distances from \$60k: managers 30k, others 10k. Crossing over, managers : others $= 10 : 30 = 1 : 3$, so managers are $\tfrac{1}{1 + 3} = \tfrac14$ of the staff. Choice (E) is the ratio $1 : 3$ misread as a fraction of the whole.

</details>

**7.** *(Hard)* A vat contains 64 litres of pure syrup. Sixteen litres are drawn off and replaced with water. This is done two more times, so that there are three replacements in all. How many litres of water are in the vat at the end?

(A) 27 (B) 32 (C) 36 (D) 37 (E) 48

<details>
<summary>Answer</summary>

**(D) 37.** Each replacement keeps $1 - \tfrac{16}{64} = \tfrac34$ of the syrup. After three: $64 \times \left(\tfrac34\right)^3 = 64 \times \tfrac{27}{64} = 27$ L of syrup, so $64 - 27 = 37$ L of water. Choice (A) is the syrup, not the water; (E) is the linear trap $3 \times 16$.

</details>

**8.** *(Medium)* An amount of money invested at a fixed annual interest rate, compounded annually, doubles in 6 years. In how many years will it be worth 8 times the original amount?

(A) 18 (B) 24 (C) 30 (D) 36 (E) 48

<details>
<summary>Answer</summary>

**(A) 18.** The amount is multiplied by 2 every 6 years: $\times 2$ after 6, $\times 4$ after 12, $\times 8$ after 18. Formally, $(1 + r)^6 = 2$, so $(1 + r)^{18} = 2^3 = 8$. Choice (E), $6 \times 8$, assumes linear growth.

</details>

**9.** *(Hard)* A town has 50,000 residents, and its population grows by 2% each year, compounded annually. Its population after 10 years will be closest to which of the following?

(A) 55,000 (B) 60,000 (C) 61,000 (D) 65,000 (E) 70,000

<details>
<summary>Answer</summary>

**(C) 61,000.** Simple growth would give $50{,}000 \times 1.2 = 60{,}000$, but compound growth is larger. Use the binomial approximation:

$$
1.02^{10} \approx 1 + 10(0.02) + \frac{10 \times 9}{2}(0.02)^2 = 1 + 0.2 + 45 \times 0.0004 = 1.218.
$$

So the population is about $50{,}000 \times 1.218 = 60{,}900$, closest to 61,000. (The exact value is about 60,950.) Choice (B) is the simple-growth trap; the remaining terms of the expansion are tiny and cannot reach 65,000.

</details>

**10.** *(Hard)* A shop has 60 pounds of a nut mix worth \$7 per pound. Cashews cost \$10 per pound. How many pounds of cashews must be added so that the new mix is worth \$8 per pound?

(A) 15 (B) 20 (C) 30 (D) 40 (E) 120

<details>
<summary>Answer</summary>

**(C) 30.** Treat the existing mix as one ingredient at \$7. Distances from \$8: the mix is 1 away, the cashews 2 away. Crossing over, mix : cashews $= 2 : 1$, so with 60 pounds of mix you add 30 pounds of cashews.

Check: $\tfrac{60 \times 7 + 30 \times 10}{90} = \tfrac{720}{90} = 8$. ✓ Choice (E) comes from crossing the seesaw the wrong way.

</details>

**11.** *(Medium, Data Sufficiency)* Solutions X and Y are mixed. What is the percent concentration of acid in the mixture?

(1) Solution X is 20% acid and solution Y is 50% acid.
(2) The mixture contains twice as much of solution X as of solution Y, by volume.

(A) Statement (1) ALONE is sufficient, but statement (2) alone is not sufficient.
(B) Statement (2) ALONE is sufficient, but statement (1) alone is not sufficient.
(C) BOTH statements TOGETHER are sufficient, but NEITHER statement ALONE is sufficient.
(D) EACH statement ALONE is sufficient.
(E) Statements (1) and (2) TOGETHER are NOT sufficient.

<details>
<summary>Answer</summary>

**(C).** A weighted average needs both the values and the weights. (1) gives only the values: the mixture could be anywhere between 20% and 50%. (2) gives only the weights. Together: $\tfrac{2(20) + 1(50)}{3} = 30\%$. You don't need the actual volumes, only their ratio.

</details>

**12.** *(Hard, Data Sufficiency)* Two deposits of \$10,000 each are made on the same day at the same annual interest rate $r$. One earns simple interest; the other earns interest compounded annually. After 2 years, is the compound-interest deposit worth more than \$50 more than the simple-interest deposit?

(1) $r > 7\%$
(2) $r < 8\%$

(A) Statement (1) ALONE is sufficient, but statement (2) alone is not sufficient.
(B) Statement (2) ALONE is sufficient, but statement (1) alone is not sufficient.
(C) BOTH statements TOGETHER are sufficient, but NEITHER statement ALONE is sufficient.
(D) EACH statement ALONE is sufficient.
(E) Statements (1) and (2) TOGETHER are NOT sufficient.

<details>
<summary>Answer</summary>

**(E).** The difference after 2 years is $10{,}000\left[(1 + r)^2 - (1 + 2r)\right] = 10{,}000\,r^2$. The question is whether $10{,}000 r^2 > 50$, that is whether $r^2 > 0.005$, or $r > \sqrt{0.005} \approx 0.0707$.

The threshold, about 7.07%, lies **between** 7% and 8%. Even together, the statements allow $r = 7.05\%$ (difference $\approx \$49.70$, no) and $r = 7.5\%$ (difference $\$56.25$, yes). Not sufficient.

The trap is (C): it feels as if pinning $r$ between 7% and 8% must settle the question. Always find the threshold first.

</details>

## Takeaways

- Every mixture is a weighted average: total of the property divided by total quantity. The result lies between the parts, closer to the bigger one.
- Seesaw: quantities are in the inverse ratio of their distances from the mix, because $w_1(c - a) = w_2(b - c)$.
- For dilution and evaporation, track the pure ingredient; it is the quantity that does not change.
- Repeated replacement multiplies the substance by $(1 - \tfrac{x}{V})$ each time; it is never linear.
- Simple interest adds $Pr$ each year; compound interest multiplies by $(1 + \tfrac{r}{n})$ for each of $nt$ periods.
- Compound beats simple by "interest on interest": $r^2$ per dollar over two years.
- Approximate with $1 + nr + \tfrac{n(n-1)}{2}r^2$ or the rule of 72, and use the spacing of the answer choices to decide how precise you need to be.

## Further reading

- GMAC, *GMAT Official Guide* (current edition), for official mixture and interest questions; check each one with the seesaw.
- [Profit, discount and percent problems](../profit-discount-and-percent-problems/) for successive percent changes, which follow the same multiplicative logic as compound interest.
- [Rates and work](../rates-and-work/), where average speed turns out to be a time-weighted average, and [Estimation and mental math](../../arithmetic/estimation-and-mental-math/) for approximation techniques.
