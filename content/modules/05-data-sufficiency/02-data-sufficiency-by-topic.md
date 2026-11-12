+++
summary = "Recognise the recurring Data Sufficiency patterns in number properties, algebra, inequalities, statistics, word problems and overlapping sets, and know in advance which kind of statement is sufficient."
+++

# Data Sufficiency by Topic

The [Data Sufficiency method](../../data-sufficiency/the-data-sufficiency-method/) works on any question. But DS questions in each content area are built from a small number of recurring patterns, and once you know the pattern you often know the answer's shape before doing any work. "Two linear equations" suggests C, unless the lines are the same. "Integer constraint" suggests that a statement which looks insufficient might be sufficient. "Standard deviation" suggests that you need the *spread*, not the *values*.

This chapter goes through the six content areas that DS questions draw on most often. For each, it gives the patterns, what makes a statement sufficient, and two or three worked items. All items use the standard DS answer choices:

| Choice | Meaning |
|---|---|
| **A** | (1) alone is sufficient, (2) alone is not |
| **B** | (2) alone is sufficient, (1) alone is not |
| **C** | Together sufficient, neither alone |
| **D** | Each alone is sufficient |
| **E** | Together not sufficient |

## Number properties

**Odd and even.** Rephrase parity questions with the rules odd × odd = odd, anything × even = even, and odd ± odd = even. Some expressions have a **fixed** parity whatever $n$ is: $n(n + 1)$ is always even (one of two consecutive integers is even), and $n^2 + n + 1$ is always odd. A statement saying something that is always true carries no information.

**Primes.** Remember that 2 is the only even prime and 1 is not prime. A statement like "$pq$ is even", where $p$ and $q$ are primes, means one of them is 2.

**Divisibility.** "Divisible by $a$ and by $b$" means "divisible by $\operatorname{lcm}(a, b)$", not by $ab$. For $n^2$ or $n^3$, use prime factorisation: if $n^2$ is divisible by a prime $p$, then $n$ is divisible by $p$.

**Remainders.** List the numbers: "remainder 2 when divided by 3" means $2, 5, 8, 11, \dots$. A remainder on division by a **multiple** of $d$ determines the remainder on division by $d$, but not the other way round. If $n = 24q + 17$, then $n = 12(2q + 1) + 5$, so the remainder on division by 12 is 5.

> [!TIP]
> For number-property questions, list small cases. Five or six values usually reveal whether a statement fixes the answer, and the pattern points to the algebraic reason.

> [!WARNING]
> "Integer" does not mean "positive integer". If the question says only "integer", test 0 and negatives. And "$n$ is a multiple of 4 and 6" is not "$n$ is a multiple of 24".

**Example 1.** If $n$ is an integer, is $n$ odd?

(1) $n^2 + 3n$ is even.
(2) $5n + 2$ is odd.

**Solution.** (1): $n^2 + 3n = n(n + 3)$. If $n$ is even, the product is even; if $n$ is odd, $n + 3$ is even, so the product is even again. The statement is always true, so it tells us nothing: $n = 1$ (yes) and $n = 2$ (no) both satisfy it. Not sufficient. (2): $5n + 2$ odd means $5n$ is odd, so $n$ is odd. Sufficient. **Answer: B.**

**Example 2.** Is the positive integer $p$ prime?

(1) $p + 2$ is prime.
(2) $p$ is odd and $20 < p < 26$.

**Solution.** (1): $p = 3$ gives $5$ (prime, and $p$ is prime: yes). $p = 9$ gives $11$ (prime, but 9 is not: no). Not sufficient.

(2): $p \in \{21, 23, 25\}$. 23 is prime; 21 and 25 are not. Not sufficient.

Together: check $p + 2$ for each candidate. $21 + 2 = 23$ is prime. $23 + 2 = 25$ is not. $25 + 2 = 27$ is not. So $p = 21$, which is not prime. A definite **no**. **Answer: C.**

**Example 3.** What is the remainder when the positive integer $n$ is divided by 12?

(1) When $n$ is divided by 24, the remainder is 17.
(2) When $n$ is divided by 6, the remainder is 5.

**Solution.** (1): $n = 24q + 17 = 12(2q + 1) + 5$. Remainder 5. Sufficient. (2): $n \in \{5, 11, 17, 23, \dots\}$, with remainders 5, 11, 5, 11 on division by 12. Not sufficient. **Answer: A.** Dividing by a multiple of 12 tells you about 12; dividing by a factor of 12 does not.

## Algebra

### Linear equations: one line, two lines, the same line

Each linear equation in $x$ and $y$ is a line. Two equations together can be:

| Two equations are… | Example | Solutions | DS consequence |
|---|---|---|---|
| Different lines that cross | $3x - 2y = 7$ and $x + y = 9$ | exactly one | Together sufficient |
| The same line in disguise | $3x - 2y = 7$ and $6x - 4y = 14$ | infinitely many | Together no better than one: D or E |
| Parallel lines | $3x - 2y = 7$ and $6x - 4y = 10$ | none | Never appears: DS statements cannot contradict |

So "two linear equations, two unknowns" is sufficient **only if the equations are genuinely different**. Check: is one a multiple of the other? If the left sides are proportional but the right sides are not, the statements contradict, and you have misread something.

And remember the E-trap from the method chapter: if the question asks for a combination such as $6x - 4y$, a single equation such as $3x - 2y = 7$ may be enough.

### Quadratics: two roots

A quadratic statement usually allows **two** values. It is sufficient alone only when:

- the two roots coincide (a perfect square, such as $(x - 4)^2 = 0$),
- the question's answer is the same for both roots (for example it asks for $x^2$ or $|x|$ when the roots are $\pm a$), or
- a constraint in the question (such as $x > 0$) rules one root out.

Two quadratics together are sufficient if they share exactly one root.

### Ratios

A ratio fixes **proportions**, not sizes. A statement like "boys : girls $= 3 : 5$" answers any question about fractions or percents of the group, but no question about counts. To get a count, you need one actual number as well (a total, a difference, or one group's size).

> [!TIP]
> Before combining two statements in an algebra question, count *independent* pieces of information, not statements. Two equations that are multiples of each other are one piece of information.

**Example 4.** What is the value of $x$?

(1) $3x - 2y = 7$
(2) $x + y = 9$

**Solution.** Each equation alone has infinitely many solutions, for example $(1, -2)$ and $(3, 1)$ for (1). Not sufficient. Together: these are different lines (the coefficients $3 : -2$ are not proportional to $1 : 1$), so they cross at exactly one point. From (2), $y = 9 - x$; then $3x - 18 + 2x = 7$, so $x = 5$. **Answer: C.** In DS you could stop at "different lines, so one solution".

If statement (2) were instead $6x - 4y = 14$, it would be (1) doubled, and the answer would be **E**.

**Example 5.** What is the value of $x$?

(1) $x^2 - 7x + 12 = 0$
(2) $x^2 - 9x + 20 = 0$

**Solution.** (1): $(x - 3)(x - 4) = 0$, so $x = 3$ or $x = 4$. Not sufficient. (2): $(x - 4)(x - 5) = 0$, so $x = 4$ or $x = 5$. Not sufficient. Together: the only value in both lists is 4. **Answer: C.**

**Example 6.** A class has only boys and girls. How many girls are in the class?

(1) The ratio of boys to girls is $3 : 5$.
(2) There are 8 more girls than boys.

**Solution.** (1): 3 boys and 5 girls, or 6 and 10, or 30 and 50. Not sufficient. (2): 1 boy and 9 girls, or 10 and 18. Not sufficient. Together: boys $= 3k$, girls $= 5k$, and $5k - 3k = 2k = 8$, so $k = 4$ and there are 20 girls. **Answer: C.**

If the question had asked "What fraction of the class are girls?", (1) alone would have been sufficient ($\tfrac58$), and the answer would be A.

## Inequalities and absolute value

Inequality questions are almost always **yes/no** questions about where a number lies. Two tools do most of the work:

1. **Draw the number line.** Turn every statement into a set of intervals: $|x - 1| > 1$ becomes "$x < 0$ or $x > 2$". A statement is sufficient for "Is $x > 2$?" exactly when its whole set lies on one side of 2.
2. **Track the sign.** Multiplying or dividing an inequality by a negative number reverses it. So a statement like $ac > bc$ says nothing about $a$ versus $b$ unless you know the sign of $c$.

$|x - a| < r$ means "$x$ is within $r$ of $a$", that is $a - r < x < a + r$. Reading absolute values as distances makes most of them one-line translations.

> [!WARNING]
> Combining two statements means taking the **intersection** of their sets. If a "no" region survives in the intersection (often a negative region you forgot), the answer is E, not C.

**Example 7.** Is $x > 2$?

(1) $|x - 1| > 1$
(2) $x^2 > 4$

**Solution.** (1): the distance from $x$ to 1 is more than 1, so $x < 0$ or $x > 2$. Not sufficient. (2): $x < -2$ or $x > 2$. Not sufficient. Together: the intersection is $x < -2$ or $x > 2$. $x = 3$ gives yes and $x = -3$ gives no. **Answer: E.** Both statements have the same "no" region below $-2$, so combining them cannot remove it.

**Example 8.** Is $a > b$?

(1) $a - c > b - c$
(2) $ac > bc$

**Solution.** (1): add $c$ to both sides: $a > b$. Sufficient. (2): if $c > 0$, then $a > b$; if $c < 0$, then $a < b$. For example $a = 2, b = 1, c = 1$ gives yes, and $a = 1, b = 2, c = -1$ gives no. Not sufficient. **Answer: A.**

**Example 9.** Is $|x - 4| < 3$?

(1) $2 < x < 5$
(2) $|x - 5| < 1$

**Solution.** Rephrase: is $1 < x < 7$? (1): the interval $(2, 5)$ lies inside $(1, 7)$: always yes. Sufficient. (2): $4 < x < 6$, also inside $(1, 7)$: always yes. Sufficient. **Answer: D.** Neither statement fixes $x$, and they do not need to.

## Statistics

DS statistics questions test whether you know **what each statistic depends on**:

| Statistic | Determined by | Not determined by |
|---|---|---|
| Mean | the **sum** and the count | the individual values |
| Median | the **middle** value(s) after sorting | the extreme values |
| Range | the largest and smallest values | the values in between |
| Standard deviation | the distances of the values from their mean | the location (adding a constant changes nothing) |

So "What is the mean?" rephrases to "What is the sum?". A median question often depends only on whether a new value lands above or below the middle. And standard deviation questions are about **spread**: adding the same number to every value leaves the SD unchanged, and multiplying every value by $k$ multiplies the SD by $|k|$. See [Descriptive statistics](../../statistics-and-counting/descriptive-statistics/) for the definitions.

> [!TIP]
> For standard deviation, you almost never compute. Compare spreads: values clustered near the mean mean a small SD, and values pushed out to the extremes mean a large one.

**Example 10.** The list $3, 7, 8, 12, x$ has five numbers. Is the median of the list 8?

(1) $x < 7$
(2) $x$ is a positive even integer.

**Solution.** (1): sorted, the list is $x, 3, 7, 8, 12$ or $3, x, 7, 8, 12$; either way the middle value is 7. A definite **no**. Sufficient. (2): $x = 2$ gives median 7 (no); $x = 10$ gives $3, 7, 8, 10, 12$ with median 8 (yes). Not sufficient. **Answer: A.** A definite no is just as sufficient as a definite yes.

**Example 11.** List A is $4, 6, 8, 10, 12$. List B also contains five numbers. Is the standard deviation of B greater than that of A?

(1) Each number in B is 5 more than the corresponding number in A.
(2) The range of B is 8, the same as the range of A.

**Solution.** (1): adding 5 to every value shifts the list without changing any distance from the mean, so the SDs are equal. A definite no. Sufficient. (2): B could be $4, 8, 8, 8, 12$, more clustered around its mean than A (SD smaller: no), or $4, 4, 4, 4, 12$, with one value far from the others (SD larger: yes). The range alone does not fix the spread. Not sufficient. **Answer: A.**

The two lists in (2) are easy to compare by hand. Using the population variance (the mean squared distance from the mean), A has $\tfrac{16 + 4 + 0 + 4 + 16}{5} = 8$. The list $4, 8, 8, 8, 12$ has $\tfrac{16 + 0 + 0 + 0 + 16}{5} = 6.4$. The list $4, 4, 4, 4, 12$ has mean 5.6 and variance $\tfrac{4 \times 2.56 + 40.96}{5} = 10.24$.

**Example 12.** Four different positive integers have an average (arithmetic mean) of 15. What is the largest of the four integers?

(1) The three smallest integers are consecutive.
(2) The smallest integer is 12.

**Solution.** Rephrase: the sum is $4 \times 15 = 60$. (1): the integers are $a, a + 1, a + 2$ and $60 - (3a + 3)$. With $a = 1$ the largest is 54; with $a = 2$ it is 51. Not sufficient. (2): $12, 13, 14, 21$ and $12, 13, 15, 20$ both work. Not sufficient. Together: $12, 13, 14$ and $60 - 39 = 21$. **Answer: C.**

## Word problems and percents

Word-problem DS questions mostly reduce to the algebra patterns above, after translation. Two extra patterns are specific to them.

**Percents need a base for amounts, but not for percents.** "Revenue rose by \$50,000" gives an amount, not a percent: you also need the starting revenue. "Revenue in 2025 was 125% of revenue in 2024" gives the percent change (25%) without any amounts. Decide whether the question asks for an amount or a percent before reading the statements.

**Hidden integer constraints.** People, tickets, boxes and coins come in whole numbers. One equation in two unknowns usually has infinitely many solutions, but if the unknowns must be **non-negative integers**, there may be only a few, or one. This is the most common source of the E-trap in word problems: list the solutions before deciding.

> [!WARNING]
> In word problems, don't stop at "one equation, two unknowns, so not sufficient". Ask whether the unknowns must be whole numbers, and if so, list the possibilities.

**Example 13.** By what percent did a company's revenue increase from 2024 to 2025?

(1) The company's revenue was \$50,000 greater in 2025 than in 2024.
(2) The company's revenue in 2025 was 125% of its revenue in 2024.

**Solution.** (1): an increase of \$50,000 is 50% of \$100,000 but 25% of \$200,000. Not sufficient. (2): 125% of the old value means an increase of 25%. Sufficient. **Answer: B.**

**Example 14.** Lena bought pens at \$3 each and notebooks at \$7 each, at least one of each. How many notebooks did she buy?

(1) She spent a total of \$47.
(2) She bought more pens than notebooks.

**Solution.** (1): $3p + 7n = 47$ with $p, n \ge 1$ integers. Try $n = 1, 2, \dots, 6$: $47 - 7n$ must be a positive multiple of 3. $n = 2$ gives $33 = 3 \times 11$, and $n = 5$ gives $12 = 3 \times 4$. So $(p, n) = (11, 2)$ or $(4, 5)$. Not sufficient. (2): clearly not sufficient. Together: only $(11, 2)$ has more pens than notebooks, so $n = 2$. **Answer: C.**

## Overlapping sets

Two overlapping groups are governed by one equation:

$$
\text{Total} = A + B - \text{Both} + \text{Neither}.
$$

There are five quantities in this equation, so you need four of them to find the fifth. Better still, notice combinations: "$A$ or $B$ or both" is the single quantity $A + B - \text{Both}$, so knowing it and the total gives "Neither" at once. When it helps, draw the $2 \times 2$ table (in $A$ / not in $A$ against in $B$ / not in $B$): each row and column must add up. See [Overlapping sets](../../statistics-and-counting/overlapping-sets/) for the full treatment.

> [!TIP]
> Write the overlapping-sets equation first, mark which quantities each statement gives, and count what is still unknown.

**Example 15.** Each of 80 students studies French, Spanish, both or neither. How many study both?

(1) 50 students study French and 40 study Spanish.
(2) 10 students study neither language.

**Solution.** The equation is $80 = F + S - \text{Both} + \text{Neither}$. (1): $80 = 90 - \text{Both} + \text{Neither}$, with two unknowns left. Both could be 10 (with none studying neither) or 20 (with 10 studying neither). Not sufficient. (2): nothing about $F$ or $S$. Not sufficient. Together: $80 = 90 - \text{Both} + 10$, so Both $= 20$. **Answer: C.**

**Example 16.** Each of 100 employees owns a car, a bicycle, both or neither. How many own neither?

(1) 70 employees own a car or a bicycle or both.
(2) 40 employees own a car and 35 own a bicycle.

**Solution.** (1): 70 own at least one, so $100 - 70 = 30$ own neither. Sufficient. (2): the number owning at least one is $75 - \text{Both}$, where Both is anything from 0 to 35. Not sufficient. **Answer: A.** Statement (1) gives the union directly, which is exactly what "neither" needs.

## Practice

**1.** *(Easy)* If $m$ is an integer, is $m$ even?

(1) $m + 7$ is odd.
(2) $m^2$ is a multiple of 4.

<details>
<summary>Answer</summary>

**D.** (1): $m + 7$ odd means $m$ even (even + odd = odd). Sufficient. (2): if $m$ were odd, $m^2$ would be odd, so not a multiple of 4. So $m$ is even. Sufficient.

</details>

**2.** *(Easy)* What is the value of $y$?

(1) $2y + x = 9$
(2) $x = 3$

<details>
<summary>Answer</summary>

**C.** (1): one equation in two unknowns ($x = 1, y = 4$ or $x = 3, y = 3$). Not sufficient. (2): says nothing about $y$. Not sufficient. Together: $2y + 3 = 9$, so $y = 3$.

</details>

**3.** *(Easy)* What is the average (arithmetic mean) of $a$, $b$, $c$ and $d$?

(1) $a + b = 14$ and $c + d = 22$.
(2) $a = c - 4$

<details>
<summary>Answer</summary>

**A.** Rephrase: what is $a + b + c + d$? (1): the sum is $36$, so the mean is 9. Sufficient. (2): relates two of the values but says nothing about $b$ or $d$. Not sufficient.

</details>

**4.** *(Medium)* If $n$ is a positive integer, what is the units digit of $3^n$?

(1) $n$ is even.
(2) $n$ is divisible by 4.

<details>
<summary>Answer</summary>

**B.** The units digits of $3^1, 3^2, 3^3, 3^4, \dots$ are $3, 9, 7, 1$, repeating every 4. (1): $n = 2$ gives 9 and $n = 4$ gives 1. Not sufficient. (2): $n = 4, 8, 12, \dots$ all give units digit 1. Sufficient. See [Remainders and units digits](../../arithmetic/remainders-and-units-digits/).

</details>

**5.** *(Medium)* Is $x < 0$?

(1) $x^3 < x^2$
(2) $x^5 < x^3$

<details>
<summary>Answer</summary>

**E.** (1): $x^2(x - 1) < 0$ means $x \ne 0$ and $x < 1$. $x = \tfrac12$ gives no; $x = -1$ gives yes. Not sufficient. (2): $x^3(x^2 - 1) < 0$ means $x < -1$ or $0 < x < 1$. Not sufficient. Together: $x < -1$ or $0 < x < 1$ (both pieces satisfy (1)). $x = \tfrac12$: $\tfrac18 < \tfrac14$ and $\tfrac1{32} < \tfrac18$, so both hold, and the answer is no. $x = -2$: $-8 < 4$ and $-32 < -8$, and the answer is yes. Not sufficient.

</details>

**6.** *(Medium)* A club has 120 members. How many members play neither chess nor go?

(1) 70 members play chess and 50 play go.
(2) 30 members play both chess and go.

<details>
<summary>Answer</summary>

**C.** $120 = \text{Chess} + \text{Go} - \text{Both} + \text{Neither}$. (1): $120 = 120 - \text{Both} + \text{Neither}$, so Neither = Both, which could be anything from 0 to 50. Not sufficient. (2): alone, not sufficient. Together: Neither $= 30$.

</details>

**7.** *(Medium)* A jacket was sold at a 20% discount from its original price. What was the original price?

(1) The discount was \$18.
(2) The sale price was \$72.

<details>
<summary>Answer</summary>

**D.** (1): 20% of the original price is \$18, so the price was \$90. Sufficient. (2): 80% of the original price is \$72, so the price was \$90. Sufficient. Each statement gives one actual amount and the question supplies the percent.

</details>

**8.** *(Hard)* If $p$ and $q$ are prime numbers, is $p + q$ odd?

(1) $pq$ is even.
(2) $p \ne q$

<details>
<summary>Answer</summary>

**C.** A sum of two primes is odd only if exactly one of them is 2. (1): one of them is 2. If $p = q = 2$, the sum is 4 (no); if $p = 2$, $q = 3$, it is 5 (yes). Not sufficient. (2): $p = 3$, $q = 5$ gives 8 (no); $p = 2$, $q = 3$ gives yes. Not sufficient. Together: one of them is 2 and the other is a different prime, so the other is odd. Even + odd is odd: yes. Sufficient.

</details>

**9.** *(Hard)* What is the value of $x$?

(1) $x^2 = 2x + 15$
(2) $x^2 - 9 = 2(x + 3)$

<details>
<summary>Answer</summary>

**E.** (1): $x^2 - 2x - 15 = 0$, so $(x - 5)(x + 3) = 0$ and $x = 5$ or $x = -3$. Not sufficient. (2): $x^2 - 9 = 2x + 6$, so $x^2 - 2x - 15 = 0$: the **same** equation. Together the two statements still allow 5 and $-3$.

The trap is to factor (2) as $(x - 3)(x + 3) = 2(x + 3)$ and divide by $x + 3$, which loses the root $x = -3$ and leaves $x = 5$ (suggesting B). Never divide by an expression that could be 0.

</details>

**10.** *(Hard)* The list $4, 9, 11, 15, x$ has five numbers. Is the average (arithmetic mean) of the list greater than its median?

(1) $x > 15$
(2) $x > 20$

<details>
<summary>Answer</summary>

**B.** If $x > 15$, the sorted list is $4, 9, 11, 15, x$ and the median is 11. The mean is $\tfrac{39 + x}{5}$, which is greater than 11 exactly when $39 + x > 55$, that is $x > 16$.

(1): $x = 15.5$ gives a mean of 10.9 (no); $x = 20$ gives a mean of 11.8 (yes). Not sufficient. Even with integers, $x = 16$ gives a mean of exactly 11, which is not greater (no), and $x = 17$ gives yes.

(2): $x > 20 > 16$, so the mean is greater than the median. Sufficient.

</details>

**11.** *(Hard)* A bakery packs muffins in boxes of 4 and boxes of 9. Last week it sold only full boxes. How many boxes of 9 did it sell?

(1) It sold 43 muffins in total.
(2) It sold 7 boxes in total.

<details>
<summary>Answer</summary>

**A.** (1): $4a + 9b = 43$, with $a, b$ non-negative integers. $b$ can be at most 4. Check: $b = 0$ leaves 43, $b = 1$ leaves 34, $b = 2$ leaves 25, $b = 3$ leaves 16, $b = 4$ leaves 7. Only 16 is a multiple of 4, so $b = 3$ (and $a = 4$). Sufficient. (2): $a + b = 7$ allows $b = 0, 1, \dots, 7$. Not sufficient.

This is the E-trap in a word problem: one equation in two unknowns looks insufficient, but the integer constraint leaves a single solution.

</details>

**12.** *(Medium)* What is the value of $2a - b$?

(1) $4a = 2b + 10$
(2) $b = 2a - 5$

<details>
<summary>Answer</summary>

**D.** (1): $4a - 2b = 10$, so $2a - b = 5$. Sufficient. (2): $2a - b = 5$ directly. Sufficient. The two statements are the same line, so this is a D-trap in reverse: equivalent statements give D or E, and here each one is enough.

</details>

## Takeaways

- Number properties: list small cases, use LCMs (not products) for "divisible by both", and remember that a remainder on division by a multiple of $d$ fixes the remainder on division by $d$.
- Linear equations: two different lines give one solution; the same line twice is one piece of information. Check whether the question needs only a combination.
- Quadratics usually give two roots. Look for a constraint or a second equation that removes one, and never divide by an expression that might be 0.
- Inequalities: draw the number line, intersect the sets, and watch the sign of anything you multiply or divide by.
- Statistics: the mean needs the sum, the median needs the middle, and the SD needs the spread (adding a constant changes nothing).
- Word problems: amounts need a base, percents don't; and integer constraints can make one equation sufficient.
- Overlapping sets: Total $= A + B - \text{Both} + \text{Neither}$. Count what is known, and spot the union as a single quantity.

## Further reading

- GMAC, *GMAT Official Guide* (current edition) and the official *Data Insights Review*: real Data Sufficiency questions, which you can sort by the topics in this chapter.
- The content chapters behind each section: [Number properties](../../arithmetic/number-properties/), [Linear equations](../../algebra/linear-equations/), [Inequalities and absolute value](../../algebra/inequalities-and-absolute-value/), [Descriptive statistics](../../statistics-and-counting/descriptive-statistics/) and [Overlapping sets](../../statistics-and-counting/overlapping-sets/).
