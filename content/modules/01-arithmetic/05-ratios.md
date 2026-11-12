+++
summary = "Turn any ratio into a multiplier, tell part-to-part from part-to-whole, combine and update ratios, and solve direct and inverse proportion problems."
+++

# Ratios & Proportions

A ratio compares quantities by **relative size**. "Boys to girls is $3 : 5$" doesn't tell you how many students there are, only that for every 3 boys there are 5 girls. Almost every ratio question on the GMAT is solved by one idea: replace the ratio with actual amounts using an unknown **multiplier**. Once you do that, ratios become ordinary linear equations, of the kind you solve in [Linear equations](../../algebra/linear-equations/).

## Key ideas

### The multiplier method

If $a : b = 3 : 5$, then $a = 3k$ and $b = 5k$ for some positive number $k$. The ratio fixes the **shape**, and $k$ fixes the **size**.

> [!IMPORTANT]
> **Multiplier method.** If $a : b : c = p : q : r$, write $a = pk$, $b = qk$, $c = rk$. Then the total is $(p + q + r)k$.

Two consequences:

- **Divisibility of the total.** When the quantities are whole things (people, marbles), $k$ is usually a positive integer, so the total must be a multiple of $p + q + r$. With boys : girls $= 3 : 5$, the class size must be a multiple of 8. This alone often eliminates answer choices.
- **Any one number fixes everything.** Knowing the total, one part, or the difference between two parts gives $k$, and then every other quantity follows. If girls outnumber boys by 16, then $5k - 3k = 2k = 16$, so $k = 8$, and there are 24 boys, 40 girls and 64 students.

The multiplier also makes it clear why ratios can be **scaled**: $3 : 5$, $6 : 10$ and $1.5 : 2.5$ are the same ratio, because $k$ absorbs the factor. Simplify ratios like fractions, and clear decimals or fractions by multiplying every term by the same number: $\tfrac12 : \tfrac13 = 3 : 2$ (multiply both by 6).

### Part-to-part versus part-to-whole

A ratio can compare two parts or a part with the whole. The same situation gives both:

| Situation: boys : girls $= 3 : 5$ | Value |
|---|---|
| boys : girls (part-to-part) | $3 : 5$ |
| boys : total (part-to-whole) | $3 : 8$ |
| fraction of students who are boys | $\tfrac38 = 37.5\%$ |
| boys as a fraction of girls | $\tfrac35 = 60\%$ |

To go from part-to-part to part-to-whole, add the parts to get the whole. To go back, subtract: if $\tfrac{2}{7}$ of a fleet is electric, then electric : non-electric is $2 : (7 - 2) = 2 : 5$.

> [!WARNING]
> Mixing up part-to-part and part-to-whole is the most common ratio error, and the wrong answer choice is almost always there. Before you compute, say in words what the 3 and the 5 count, and what the question asks for.

### Ratios as fractions and equations

A two-term ratio $a : b$ is the fraction $\tfrac{a}{b}$. So $a : b = 3 : 5$ is the equation $\tfrac{a}{b} = \tfrac35$, or $5a = 3b$ after cross-multiplying. A **proportion** is an equation between two ratios, $\tfrac{a}{b} = \tfrac{c}{d}$, solved by cross-multiplying: $ad = bc$.

**Picking numbers works perfectly with ratios.** If $x : y = 3 : 4$ and the question asks for $\tfrac{2x + y}{x + 2y}$, set $x = 3$ and $y = 4$: $\tfrac{10}{11}$. Any other multiplier gives the same answer, because $k$ cancels from top and bottom. This works whenever the expression is a ratio of terms with the same total power (here, every term is a single $x$ or $y$).

### Combining ratios

To combine $a : b = 2 : 3$ with $b : c = 4 : 5$, the shared term $b$ must have **the same number** in both ratios. Scale each ratio so that $b$ becomes the LCM of 3 and 4, which is 12:

$$
a : b = 8 : 12, \qquad b : c = 12 : 15 \quad\Longrightarrow\quad a : b : c = 8 : 12 : 15.
$$

**Why you can't just write $2 : 3 : 5$ or $2 : 4 : 5$.** The 3 and the 4 both describe $b$, but at different scales: in the first ratio, $b$ is 3 units; in the second, 4 units. Combining only makes sense after both are measured in the same units.

For a chain $a : b$, $b : c$, $c : d$, you can also multiply the fractions: $\tfrac{a}{d} = \tfrac{a}{b} \cdot \tfrac{b}{c} \cdot \tfrac{c}{d}$, since each middle term cancels.

### Changing ratios: adding or removing

When something is added to or removed from one part, the ratio changes. The method is always the same: write the original amounts with a multiplier, apply the change, and set up the new ratio as an equation.

**Example.** Red : blue $= 4 : 7$. After 6 red marbles are added, red : blue $= 2 : 3$. Then

$$
\frac{4k + 6}{7k} = \frac23 \;\Longrightarrow\; 12k + 18 = 14k \;\Longrightarrow\; k = 9,
$$

so there were 36 red and 63 blue marbles at the start.

**Unchanged parts are anchors.** In this example blue never changed, so you can also scale both ratios to give blue the same number. Blue is 7 in the first ratio and 3 in the second; the LCM is 21. Then old red : blue $= 12 : 21$ and new red : blue $= 14 : 21$. Red went up by 2 units, which equal the 6 added marbles, so 1 unit is 3 marbles. Blue is $21 \times 3 = 63$. This "unit" method avoids algebra.

> [!TIP]
> In change problems, look for the quantity that **doesn't change**: blue marbles when only red ones are added, the amount of salt when water evaporates, the age **difference** of two people over time. Equalise its number in the before and after ratios, then the change in the other part tells you the size of one unit.

When both parts change by the same amount (for example, both people's ages increase by 6 years), neither part is fixed, so use the multiplier equation.

### Direct and inverse proportion

**Direct proportion.** $y$ is directly proportional to $x$ if $y = kx$ for a constant $k$. Equivalently, the ratio $\tfrac{y}{x}$ is constant. Doubling $x$ doubles $y$. Cost and quantity at a fixed unit price are directly proportional: if 7 kg costs \$45.50, the unit price is \$6.50 per kg and 12 kg cost \$78.

**Inverse proportion.** $y$ is inversely proportional to $x$ if $y = \tfrac{k}{x}$, that is, the **product** $xy$ is constant. Doubling $x$ halves $y$. The classic case is workers and time: if 6 pumps empty a tank in 10 hours, the job is $6 \times 10 = 60$ pump-hours, so 4 pumps take $60 / 4 = 15$ hours.

> [!IMPORTANT]
> - Direct: $y = kx$, so $\dfrac{y_1}{x_1} = \dfrac{y_2}{x_2}$.
> - Inverse: $y = \dfrac{k}{x}$, so $x_1 y_1 = x_2 y_2$.
> - Joint: if $y = \dfrac{kx}{z^2}$, then doubling $x$ and tripling $z$ multiplies $y$ by $\dfrac{2}{3^2} = \dfrac29$.

**Several factors at once.** Work in "units of effort". If 8 workers paint 3 houses in 9 days, the effort is $8 \times 9 = 72$ worker-days for 3 houses, or 24 worker-days per house. Then 4 houses need 96 worker-days, and 6 workers take $96 / 6 = 16$ days. Each factor is either direct (more houses, more days) or inverse (more workers, fewer days), and the worker-day bookkeeping handles both. The same idea is developed for rates in [Rates and work](../../word-problems/rates-and-work/).

### Ratio word problems: a checklist

1. Write each quantity as (ratio number) $\times k$.
2. Translate the extra fact (total, difference, change) into one equation in $k$.
3. Solve for $k$, then answer **the question asked**, which is often not $k$ itself and not the first quantity you find.
4. Sanity check: the totals should be whole numbers and the new ratio should come out right.

> [!WARNING]
> Common traps in ratio questions:
> - answering with a part when the question wants the total, or the reverse;
> - reporting $k$ instead of a quantity;
> - combining ratios without matching the shared term;
> - adding the same amount to both terms and assuming the ratio stays the same (it doesn't: $1 : 2$ becomes $2 : 3$ when you add 1 to each);
> - treating inverse proportion as direct (more workers do **not** take more time).

## Worked examples

**Example 1** *(Easy)*. A recipe uses flour and sugar in the ratio $5 : 2$ by volume. A baker uses 35 cups of flour and sugar in total. How many cups of sugar does she use?

(A) 7 (B) 10 (C) 14 (D) 17.5 (E) 25

**Solution.** Flour $= 5k$ and sugar $= 2k$, so $7k = 35$ and $k = 5$. Sugar $= 2 \times 5 = 10$ cups. **Answer: (B).**

Choice (C) treats the ratio as part-to-whole ($\tfrac25$ of 35). Choice (E) is the flour.

**Example 2** *(Medium)*. If $a : b = 3 : 4$ and $b : c = 6 : 5$, what is $a : c$?

(A) $3 : 5$ (B) $9 : 10$ (C) $10 : 9$ (D) $18 : 25$ (E) $1 : 2$

**Solution.** Match $b$: the LCM of 4 and 6 is 12. Then $a : b = 9 : 12$ and $b : c = 12 : 10$, so $a : b : c = 9 : 12 : 10$ and $a : c = 9 : 10$. **Answer: (B).**

**Check by multiplying fractions:** $\tfrac{a}{c} = \tfrac{a}{b} \cdot \tfrac{b}{c} = \tfrac34 \cdot \tfrac65 = \tfrac{18}{20} = \tfrac{9}{10}$. Choice (A) ignores $b$ and pairs the outer numbers, 3 and 5.

**Example 3** *(Medium)*. In a club, the ratio of men to women is $5 : 3$. After 12 more women join and no one leaves, the ratio becomes $5 : 4$. How many members did the club have originally?

(A) 64 (B) 80 (C) 96 (D) 108 (E) 120

**Solution (anchor method).** The number of men is unchanged, and it is 5 in both ratios. So women went from 3 units to 4 units: 1 unit $= 12$ people. The original club had $5 + 3 = 8$ units, or $96$ members. **Answer: (C).**

**Solution (algebra).** $\dfrac{5k}{3k + 12} = \dfrac54$, so $20k = 15k + 60$ and $k = 12$. Total $= 8k = 96$.

Choice (D) is the total *after* the new members join, $96 + 12 = 108$. Always check which moment the question asks about.

**Example 4** *(Hard)*. Twelve identical machines working together can finish a job in 15 days. After 5 days, 4 of the machines break down, and the remaining machines finish the job. How many days does the whole job take?

(A) 18 (B) 20 (C) 22.5 (D) 25 (E) 30

**Solution.** The job is $12 \times 15 = 180$ machine-days. In the first 5 days, 12 machines do $60$ machine-days, leaving $120$. The remaining 8 machines need $120 / 8 = 15$ more days. Total: $5 + 15 = 20$ days. **Answer: (B).**

Choice (C) assumes 8 machines do the *whole* job ($180 / 8$). Choice (E) misreads the stem as 4 machines remaining ($120 / 4 = 30$).

**Example 5** *(Hard)*. The ratio of Ana's age to Ben's age is $4 : 3$. In 6 years the ratio will be $6 : 5$. What is the sum of their ages now?

(A) 14 (B) 21 (C) 28 (D) 35 (E) 42

**Solution.** Both ages change, so use the multiplier: $\dfrac{4k + 6}{3k + 6} = \dfrac{6}{5}$. Then $20k + 30 = 18k + 36$, so $k = 3$. Ana is 12, Ben is 9, and the sum is 21. **Answer: (B).**

**Anchor method.** The age **difference** never changes. It is $4 - 3 = 1$ unit now and $6 - 5 = 1$ unit later, so the units are already matched: Ana goes from 4 units to 6 units in 6 years. So 2 units = 6 years, 1 unit = 3 years, and the sum now is $7 \times 3 = 21$. Check: in 6 years, $18 : 15 = 6 : 5$.

## Practice

<details>
<summary>Data Sufficiency answer choices (the same on every DS question)</summary>

- **(A)** Statement (1) ALONE is sufficient, but statement (2) alone is not sufficient.
- **(B)** Statement (2) ALONE is sufficient, but statement (1) alone is not sufficient.
- **(C)** BOTH statements TOGETHER are sufficient, but NEITHER statement ALONE is sufficient.
- **(D)** EACH statement ALONE is sufficient.
- **(E)** Statements (1) and (2) TOGETHER are NOT sufficient.

</details>

**1.** *(Easy)* In a fleet of 84 cars, the ratio of electric to non-electric cars is $2 : 5$. How many cars are electric?

(A) 12 (B) 24 (C) 34 (D) 42 (E) 60

<details>
<summary>Answer</summary>

**(B).** $7k = 84$, so $k = 12$ and there are $2 \times 12 = 24$ electric cars. Choice (C) treats $\tfrac25$ as part-to-whole ($\tfrac25 \times 84 = 33.6$, rounded). Choice (E) is the non-electric cars.

</details>

**2.** *(Easy)* If $x : y = 2 : 5$, what is the value of $\dfrac{3x + y}{x + y}$?

(A) $\tfrac87$ (B) $\tfrac{11}{7}$ (C) $\tfrac32$ (D) $\tfrac{13}{7}$ (E) $\tfrac{11}{5}$

<details>
<summary>Answer</summary>

**(B).** Pick $x = 2$, $y = 5$: $\dfrac{6 + 5}{2 + 5} = \dfrac{11}{7}$. Any multiplier gives the same value.

</details>

**3.** *(Easy)* If 7 kilograms of coffee cost \$45.50, how much do 12 kilograms cost at the same price per kilogram?

(A) \$71.50 (B) \$75.00 (C) \$78.00 (D) \$81.50 (E) \$91.00

<details>
<summary>Answer</summary>

**(C).** $45.50 / 7 = 6.50$ per kilogram, and $12 \times 6.50 = 78$.

</details>

**4.** *(Medium)* If $a : b = 2 : 3$, $b : c = 4 : 5$ and $c : d = 6 : 7$, what is $a : d$?

(A) $2 : 7$ (B) $16 : 35$ (C) $12 : 35$ (D) $8 : 15$ (E) $48 : 35$

<details>
<summary>Answer</summary>

**(B).** $\tfrac{a}{d} = \tfrac23 \cdot \tfrac45 \cdot \tfrac67 = \tfrac{48}{105} = \tfrac{16}{35}$. Choice (A) pairs the outer numbers without matching the shared terms.

</details>

**5.** *(Medium)* A box holds red and white balls in the ratio $7 : 4$. After 18 red balls are removed, the box holds equal numbers of red and white balls. How many balls were in the box originally?

(A) 44 (B) 55 (C) 66 (D) 77 (E) 99

<details>
<summary>Answer</summary>

**(C).** White is unchanged and is 4 units, and red falls from 7 units to 4 units. So 3 units $= 18$ balls and 1 unit $= 6$. Originally there were $11 \times 6 = 66$. Check: 42 red and 24 white; removing 18 red leaves 24 and 24. Choice (E) uses 18 balls as 2 units.

</details>

**6.** *(Medium)* Eight workers can paint 3 houses in 9 days. Working at the same rate, how many days would 6 workers need to paint 4 houses?

(A) 12 (B) 14 (C) 16 (D) 18 (E) 24

<details>
<summary>Answer</summary>

**(C).** One house takes $\tfrac{8 \times 9}{3} = 24$ worker-days. Four houses take 96 worker-days, and 6 workers need $96 / 6 = 16$ days. Choice (A) adjusts for only one of the two changes: $9 \times \tfrac43$ (more houses) or $9 \times \tfrac86$ (fewer workers) both give 12.

</details>

**7.** *(Medium)* The ratio of Ama's savings to Bea's savings is $5 : 3$. Ama has \$240 more than Bea. How much do they have together?

(A) \$480 (B) \$640 (C) \$720 (D) \$960 (E) \$1,920

<details>
<summary>Answer</summary>

**(D).** The difference is $5k - 3k = 2k = 240$, so $k = 120$, and the total is $8k = 960$. Choice (E) uses $k = 240$.

</details>

**8.** *(Hard)* Alloy X is copper and zinc in the ratio $3 : 2$ by weight. Alloy Y is copper and zinc in the ratio $1 : 3$. In what ratio by weight must X and Y be mixed to give an alloy with equal amounts of copper and zinc?

(A) $2 : 5$ (B) $3 : 2$ (C) $5 : 2$ (D) $2 : 1$ (E) $5 : 3$

<details>
<summary>Answer</summary>

**(C).** Convert to part-to-whole: X is $\tfrac35 = 60\%$ copper, Y is $\tfrac14 = 25\%$ copper, and the target is 50%. With $x$ kg of X and $y$ kg of Y: $0.6x + 0.25y = 0.5(x + y)$, so $0.1x = 0.25y$ and $x : y = 5 : 2$. Mixing ideas like this are developed in [Mixtures and interest](../../word-problems/mixtures-and-interest/). Choice (A) inverts the answer.

</details>

**9.** *(Hard)* The ratio of boys to girls at a camp is $4 : 5$. If 10 boys and 10 girls leave, the ratio becomes $3 : 4$. How many children were at the camp originally?

(A) 72 (B) 81 (C) 90 (D) 99 (E) 108

<details>
<summary>Answer</summary>

**(C).** $\dfrac{4k - 10}{5k - 10} = \dfrac34$ gives $16k - 40 = 15k - 30$, so $k = 10$. The camp had $9k = 90$ children: 40 boys and 50 girls, then 30 and 40. Both parts changed, so there is no anchor; use the equation. Every choice is a multiple of 9, so divisibility alone doesn't help here.

</details>

**10.** *(Hard, Data Sufficiency)* The ratio of boys to girls in a class is $3 : 4$. How many students are in the class?

(1) There are 6 more girls than boys.

(2) If 2 boys left the class, the ratio of boys to girls would be $2 : 3$.

<details>
<summary>Answer</summary>

**(D).** (1): $4k - 3k = k = 6$, so there are $7k = 42$ students. Sufficient. (2): $\dfrac{3k - 2}{4k} = \dfrac23$ gives $9k - 6 = 8k$, so $k = 6$ and again there are 42 students. Sufficient. Each statement gives one linear equation in the single unknown $k$, so you could stop before solving either one.

</details>

**11.** *(Medium, Data Sufficiency)* A jar contains only red and blue marbles. What fraction of the marbles are red?

(1) There are 12 more blue marbles than red marbles.

(2) If 4 red marbles were added, the ratio of red to blue marbles would be $3 : 4$.

<details>
<summary>Answer</summary>

**(C).** (1): 1 red and 13 blue, or 20 red and 32 blue, give different fractions. Not sufficient. (2): $4(r + 4) = 3b$ has many solutions, such as $r = 2$, $b = 8$ and $r = 5$, $b = 12$, with different fractions. Not sufficient. Together: $b = r + 12$ and $4r + 16 = 3r + 36$, so $r = 20$, $b = 32$, and the fraction is $\tfrac{20}{52} = \tfrac{5}{13}$. Sufficient.

</details>

**12.** *(Medium)* The quantity $y$ is directly proportional to $x$ and inversely proportional to the square of $z$. If $x$ is doubled and $z$ is tripled, $y$ is multiplied by

(A) $\tfrac29$ (B) $\tfrac23$ (C) $\tfrac32$ (D) 6 (E) 18

<details>
<summary>Answer</summary>

**(A).** $y = \dfrac{kx}{z^2}$. The new value is $\dfrac{k(2x)}{(3z)^2} = \dfrac{2}{9} \cdot \dfrac{kx}{z^2}$. Choice (B) forgets to square the 3, and (E) multiplies by $3^2$ instead of dividing.

</details>

> [!NOTE]
> If you use Claude Code, the `quantome-math` plugin (`/plugin install quantome-math@quantome`) can check a ratio set-up once you have written it down by hand.

## Takeaways

- Replace a ratio $p : q$ with amounts $pk$ and $qk$. The total is a multiple of $p + q$ when the amounts are whole numbers.
- Identify whether a ratio is part-to-part or part-to-whole before computing. The other one is usually an answer choice.
- Combine ratios only after giving the shared term the same number (use the LCM), or multiply the fractions in a chain.
- In change problems, find the part that doesn't change and equalise it. Otherwise set up an equation in $k$.
- Direct proportion keeps the ratio constant, and inverse proportion keeps the product constant. Use worker-days or machine-days for multi-factor problems.
- Answer the question asked: a part, the total, before or after the change.

## Further reading

- GMAC, *GMAT Official Guide* (current edition): ratio questions appear throughout its Problem Solving and Data Sufficiency sections.
- Related chapters: [Fractions, decimals and percents](../../arithmetic/fractions-decimals-percents/), [Translating words into equations](../../word-problems/translating-words-into-equations/) and [Mixtures and interest](../../word-problems/mixtures-and-interest/).
