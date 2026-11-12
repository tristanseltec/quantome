+++
summary = "Work with means through sums, handle weighted averages, find medians in sorted lists, reason about standard deviation without heavy computation, and solve max/min problems built on mean and median."
+++

# Descriptive Statistics

GMAT statistics questions look like arithmetic, but they are really questions about **structure**. You will rarely be asked to compute a standard deviation to two decimal places. Instead you will be asked what happens to an average when one value leaves, which of five sets is most spread out, or how large one value can be when the mean and median are fixed. Every one of these questions rewards the same habit: translate averages into **sums**, keep lists **sorted**, and think about spread as **distance from the centre**.

This chapter covers the five summary statistics the GMAT uses (mean, median, mode, range and standard deviation), the special case of evenly spaced sets, the classic "greatest possible value" problems, and reading a frequency table.

## Key ideas

### The mean is a sum in disguise

The arithmetic mean (the GMAT says "average (arithmetic mean)") of $n$ values is

> [!IMPORTANT]
> $$\text{Mean} = \frac{\text{Sum}}{n} \qquad\Longleftrightarrow\qquad \text{Sum} = \text{Mean} \times n$$

The second form is the one you will use. An average is hard to manipulate, because averages do not add: the average of a group of 10 and a group of 30 is not the average of their averages. **Sums do add.** So whenever a problem says "the average of ...", immediately write down the sum.

**Adding or removing values.** The mean of 5 numbers is 12, so their sum is 60. If an 18 joins them, the new sum is 78 over 6 values, and the new mean is 13. Notice the shortcut: the newcomer is 6 above the old mean, and that excess is shared among 6 values, raising the mean by $6/6 = 1$. In general:

$$\text{new mean} = \text{old mean} + \frac{\text{new value} - \text{old mean}}{n + 1}.$$

A value above the mean pulls the mean up, a value below it pulls it down, and a value **equal** to the mean leaves it unchanged. Removing a value works the same way in reverse: subtract it from the sum, divide by $n - 1$.

**Deviations from the mean sum to zero.** Because $\text{Sum} = n \times \text{Mean}$, the total amount by which values sit above the mean exactly balances the total amount by which others sit below it. This "balance" view is why the mean is called the centre of mass of the data, and it gives fast solutions: if the scores 70, 85 and $x$ average 80, the deviations $-10$ and $+5$ must be balanced by $x$ having deviation $+5$, so $x = 85$.

### Weighted averages

When groups of different sizes are combined, each group's average counts in proportion to its size:

$$\text{Weighted mean} = \frac{n_1 \bar{x}_1 + n_2 \bar{x}_2 + \dots}{n_1 + n_2 + \dots}.$$

This is just "add the sums, divide by the total count". Three groups at 80 and one at 60 average $(3 \cdot 80 + 60)/4 = 75$, not 70.

For **two** groups there is a picture worth memorising. The combined mean lies between the two group means, and closer to the larger group. Specifically, the distances from the combined mean to the group means are in the **inverse ratio** of the group sizes:

$$\frac{n_1}{n_2} = \frac{\bar{x}_2 - \bar{x}}{\bar{x} - \bar{x}_1}.$$

*Why it works:* $n_1(\bar{x} - \bar{x}_1) = n_2(\bar{x}_2 - \bar{x})$ is just the statement that deviations from the overall mean sum to zero, the "balance" idea again. If 3 times as many people are in group 1, the combined mean sits 3 times closer to group 1's mean.

> [!TIP]
> **The see-saw.** For two-group averages, draw a number line with the two group means and the combined mean. The gaps tell you the ratio of the group sizes instantly, often with no algebra at all. This is the same idea as mixtures in [Mixtures and interest](../../word-problems/mixtures-and-interest/).

### Median and mode

The **median** is the middle value of the **sorted** list. With $n$ values, sort them; if $n$ is odd, the median is the value in position $\tfrac{n+1}{2}$; if $n$ is even, it is the average of the values in positions $\tfrac{n}{2}$ and $\tfrac{n}{2} + 1$. So the median of $\{9, 2, 7, 4, 11, 4\}$ is found from $2, 4, 4, 7, 9, 11$: the 3rd and 4th values average to $5.5$.

The median depends only on **order**, not on how far the extreme values are from the middle. Changing the largest value from 11 to 1,000 does not move the median at all, while it drags the mean far up. This insensitivity is what makes max/min problems possible (see below).

The **mode** is the most frequent value. A list can have several modes, or none if every value appears once. When a problem says "the **unique** mode", one value must appear strictly more often than every other value, which is a real constraint you must enforce.

**Range** is $\text{max} - \text{min}$. Like the median, it only cares about two specific positions in the sorted list.

### Standard deviation: the concept

Standard deviation (SD) measures how far values typically sit from the mean. The GMAT uses the **population** SD:

$$\sigma = \sqrt{\frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n}}.$$

The recipe: find the mean, take each value's deviation from it, square, average the squares (this average is the **variance**), then take the square root. For $\{3, 5, 7, 9, 11\}$, the mean is 7, the deviations are $-4, -2, 0, 2, 4$, the squares sum to $16 + 4 + 0 + 4 + 16 = 40$, the variance is $40/5 = 8$ and the SD is $\sqrt{8} = 2\sqrt{2}$. That is about as much computation as the GMAT ever asks for, and usually it asks for less.

Squaring makes all deviations positive and punishes large deviations more than small ones, so one far-away value raises the SD a lot.

> [!NOTE]
> Statistics courses often divide by $n - 1$ instead of $n$ (the *sample* SD, see [Distributions and likelihood](../../probability-and-statistics/distributions-and-likelihood/)). On the GMAT, comparisons between sets of the same size never depend on this choice, and when a computation is needed the question is set up so that the intended formula is clear.

### How transformations affect mean and SD

Think of SD as the typical **distance** between values and their mean.

| Change to every value | Mean | Median | SD | Range |
|---|---|---|---|---|
| add a constant $k$ | $+k$ | $+k$ | unchanged | unchanged |
| multiply by $k$ | $\times k$ | $\times k$ | $\times \vert k \vert$ | $\times \vert k \vert$ |
| multiply by $k$, then add $c$ | $\times k$, then $+c$ | $\times k$, then $+c$ | $\times \vert k \vert$ | $\times \vert k \vert$ |

*Why:* adding $k$ slides the whole set along the number line, so every distance stays the same. Multiplying by $k$ stretches every distance by $\vert k \vert$. A negative $k$ also flips the set, but a flipped set is exactly as spread out.

Adding **new values** changes SD in a predictable direction:

- A new value **equal to the mean** leaves the mean unchanged and **decreases** the SD (the same total squared deviation is shared among more values).
- A new value **far from the mean** increases the SD.
- Adding two values symmetric about the mean (like $\bar{x} - d$ and $\bar{x} + d$) keeps the mean, and lowers the SD if $d$ is smaller than the current SD, raises it if $d$ is larger.

### Comparing SDs without computing

To decide which of several sets has the larger SD, compare the **deviations from each set's own mean**:

1. Shift each set mentally so that its mean is at 0. Sets that are translations of each other (like $\{1, 2, 3\}$ and $\{101, 102, 103\}$) have the same SD.
2. Compare the sizes of the deviations. If one set's deviations are, value by value, at least as large as another's, its SD is at least as large.
3. If the comparison is not obvious, add up the **squared** deviations. Same $n$ means you can compare those sums directly.

> [!TIP]
> More values bunched at the mean means a smaller SD; more values pushed to the extremes means a larger SD. $\{2, 6, 6, 6, 10\}$ and $\{2, 2, 6, 10, 10\}$ have the same mean and range, but the second set has twice the total squared deviation.

### Evenly spaced sets

An **evenly spaced** set (arithmetic sequence) such as consecutive integers, consecutive odd numbers or $7, 11, 15, \dots, 47$ is symmetric about its centre, so

$$\text{mean} = \text{median} = \frac{\text{first} + \text{last}}{2}.$$

Two companion facts:

- **Count:** $\dfrac{\text{last} - \text{first}}{\text{spacing}} + 1$. For $7, 11, \dots, 47$: $\tfrac{40}{4} + 1 = 11$ terms.
- **Sum:** $\text{count} \times \text{mean}$. Here $11 \times 27 = 297$.

For an odd number of terms, the mean *is* the middle term; for an even number, it is halfway between the two middle terms (and, for consecutive integers, it is not an integer). The same formula appears in [Functions and sequences](../../algebra/functions-and-sequences/).

### Maximising or minimising one value

A favourite hard question fixes the mean (so the **sum** is fixed) and the median, then asks for the greatest or least possible value of one element. The method:

1. Convert the mean to a sum.
2. Write the sorted list as blanks, and place the median.
3. To make one value **as large as possible**, make every other value **as small as possible**, subject to the ordering and any rules (positive, integer, distinct, unique mode). To make one value as small as possible, make the others as large as possible.
4. The target value is whatever is left of the sum.

The constraints are where the trap is. "Distinct" forces values above the median to step up by at least 1 each; "positive integers" means the smallest possible value is 1, not 0; and everything to the right of the median must be at least the median.

> [!TIP]
> **Testing cases** is the natural strategy for max/min questions. Build the extreme list explicitly, check every condition in the stem against it, and only then read off the answer.

### Reading data summaries

The GMAT often gives data as a **frequency table** ("value: how many times it occurs") rather than a list. Do not expand the list. Instead:

- **Mean:** $\dfrac{\sum (\text{value} \times \text{frequency})}{\sum \text{frequency}}$, a weighted average.
- **Median:** find the position ($\tfrac{n+1}{2}$ for odd $n$) and walk through **cumulative** frequencies until you reach it.
- **Mode:** the value with the largest frequency (not the largest frequency itself).

> [!WARNING]
> **Common traps in statistics questions**
> - Averaging averages: combining groups of different sizes by taking the plain mean of their means.
> - Forgetting to sort before taking the median, or using the middle *position* number instead of the value there.
> - Reporting the frequency instead of the value as the mode or median in a frequency table.
> - Thinking adding a constant changes the SD, or that multiplying by $-2$ makes the SD negative.
> - In max/min problems, ignoring "distinct", "positive" or "unique mode", which is exactly what the wrong answers are built from.
> - Confusing "SD decreases" with "range decreases": adding a value at the mean shrinks SD but never changes range.

> [!NOTE]
> Readers using Claude Code can check their working on these problems with the `quantome-math` plugin (`/plugin install quantome-math@quantome`). It is optional: everything here is designed to be done by hand.

## Worked examples

### Example 1 (Easy): adding a value

The average (arithmetic mean) of 6 numbers is 14. When a seventh number is added, the average of the 7 numbers is 15. What is the seventh number?

(A) 15 · (B) 16 · (C) 19 · (D) 21 · (E) 22

**Solution.** Old sum $= 6 \times 14 = 84$. New sum $= 7 \times 15 = 105$. The seventh number is $105 - 84 = 21$. **Answer: (D).**

*Faster:* the newcomer raised each of 7 values by 1 on average, so it brought $7 \times 1 = 7$ above the old mean of 14: $14 + 7 = 21$. Choice (A) is the trap of assuming the new value equals the new average.

### Example 2 (Medium): weighted average

A class of 30 students has an average test score of 72, and a class of 20 students has an average of 82 on the same test. What is the average score of all 50 students?

(A) 74 · (B) 75 · (C) 76 · (D) 77 · (E) 78

**Solution.** Sum of scores $= 30 \cdot 72 + 20 \cdot 82 = 2160 + 1640 = 3800$, and $3800 / 50 = 76$. **Answer: (C).**

*See-saw method:* the means are 10 apart and the sizes are in the ratio $30 : 20 = 3 : 2$, so the combined mean divides the gap in the inverse ratio $2 : 3$. It sits $\tfrac{2}{5} \times 10 = 4$ above 72, at 76. Choice (D), 77, is the plain average of 72 and 82, the "average of averages" trap.

### Example 3 (Medium): reading a frequency table

Twenty-five students reported their number of siblings:

| Siblings | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| Students | 4 | 9 | 7 | 3 | 2 |

By how much does the mean number of siblings exceed the median?

(A) 0 · (B) 0.4 · (C) 0.6 · (D) 1 · (E) 1.6

**Solution.** *Median:* with 25 values, the median is the 13th. Cumulative counts: 4 students have 0 siblings (positions 1 to 4), then 9 have 1 (positions 5 to 13). The 13th value is 1.

*Mean:* $\dfrac{0 \cdot 4 + 1 \cdot 9 + 2 \cdot 7 + 3 \cdot 3 + 4 \cdot 2}{25} = \dfrac{40}{25} = 1.6$.

The difference is $1.6 - 1 = 0.6$. **Answer: (C).** Choice (E) is the mean itself; a student who reads the middle of the *header row* gets a median of 2 and a negative difference.

### Example 4 (Medium): comparing standard deviations

Which of the following sets has the greatest standard deviation?

(A) $\{2, 4, 6, 8, 10\}$ · (B) $\{12, 14, 16, 18, 20\}$ · (C) $\{2, 6, 6, 6, 10\}$ · (D) $\{2, 2, 6, 10, 10\}$ · (E) $\{4, 6, 6, 6, 8\}$

**Solution.** (B) is (A) shifted by 10, so they have the same SD: if one of them had the greatest SD, so would the other, and neither can be the single answer. Sets (A), (C), (D) and (E) all have mean 6 and five values, so compare their deviations from 6:

| Set | Deviations | Sum of squares |
|---|---|---|
| (A) | $-4, -2, 0, 2, 4$ | 40 |
| (C) | $-4, 0, 0, 0, 4$ | 32 |
| (D) | $-4, -4, 0, 4, 4$ | 64 |
| (E) | $-2, 0, 0, 0, 2$ | 8 |

(D) pushes four of its five values to the extremes. **Answer: (D).** Notice that (A), (C) and (D) all have range 8: range alone does not decide SD.

### Example 5 (Hard): greatest possible value

A list of 7 different positive integers has an average (arithmetic mean) of 20 and a median of 22. What is the greatest possible value of the largest integer in the list?

(A) 64 · (B) 65 · (C) 69 · (D) 71 · (E) 103

**Solution.** The sum is $7 \times 20 = 140$. Sorted, the list is $a < b < c < 22 < e < f < g$. To maximise $g$, minimise everything else:

- $a, b, c$ are different positive integers, so at least $1, 2, 3$.
- $e$ and $f$ must exceed 22 and differ, so at least $23, 24$.

Then $g = 140 - (1 + 2 + 3 + 22 + 23 + 24) = 140 - 75 = 65$, and $65 > 24$, so the list $\{1, 2, 3, 22, 23, 24, 65\}$ satisfies everything. **Answer: (B).**

The traps: (D) 71 comes from ignoring "different" (using $1, 1, 1, 22, 22, 22$), and (E) 103 from forgetting that $e$ and $f$ must be at least the median (using $1, 2, 3, 4, 5$ for the other five values).

## Practice

**1.** *(Easy)* What is the median of the list $12, 5, 9, 15, 5, 20$?

(A) 5 · (B) 9 · (C) 10 · (D) 10.5 · (E) 11

<details>
<summary>Answer</summary>

**(D).** Sorted: $5, 5, 9, 12, 15, 20$. With 6 values the median is the average of the 3rd and 4th: $\tfrac{9 + 12}{2} = 10.5$. Choice (E) is the mean ($66/6 = 11$), (A) the mode.

</details>

**2.** *(Easy)* The average of 8 numbers is 25. When two of the numbers are removed, the average of the remaining 6 numbers is 22. What is the average of the two numbers that were removed?

(A) 22 · (B) 25 · (C) 28 · (D) 34 · (E) 68

<details>
<summary>Answer</summary>

**(D).** Sums: $8 \times 25 = 200$ and $6 \times 22 = 132$. The two removed numbers sum to $68$ (the trap in (E)), so their average is $34$.

</details>

**3.** *(Easy)* The list $6, 11, 3, x, 8$ has a range of 12. If $x$ is positive, what is $x$?

(A) $-1$ · (B) 9 · (C) 12 · (D) 14 · (E) 15

<details>
<summary>Answer</summary>

**(E).** Without $x$, the values run from 3 to 11 (range 8), so $x$ must be a new extreme. If $x$ is the minimum, $11 - x = 12$ gives $x = -1$, which is not positive. If $x$ is the maximum, $x - 3 = 12$ gives $x = 15$.

</details>

**4.** *(Medium)* Each of 15 packages weighs either 5 kg or 10 kg. If the average weight of the packages is 8 kg, how many of them weigh 10 kg?

(A) 5 · (B) 6 · (C) 8 · (D) 9 · (E) 10

<details>
<summary>Answer</summary>

**(D).** Total weight $= 15 \times 8 = 120$. If $b$ packages weigh 10 kg, then $5(15 - b) + 10b = 120$, so $75 + 5b = 120$ and $b = 9$.

*See-saw:* 8 is 3 above 5 and 2 below 10, so the counts of 5 kg and 10 kg packages are in the ratio $2 : 3$, i.e. 6 and 9.

</details>

**5.** *(Medium)* A set of numbers has mean 40 and standard deviation 6. Each number in the set is multiplied by 3 and then decreased by 10. What are the mean and standard deviation of the new set?

(A) 110 and 8 · (B) 110 and 18 · (C) 120 and 18 · (D) 120 and 8 · (E) 130 and 18

<details>
<summary>Answer</summary>

**(B).** The mean follows every operation: $3 \times 40 - 10 = 110$. The SD is multiplied by 3 but ignores the subtraction: $3 \times 6 = 18$. Choice (A) wrongly applies the $-10$ to the SD; (C) forgets the $-10$ for the mean.

</details>

**6.** *(Medium)* The sum of 15 consecutive even integers is 480. What is the largest of these integers?

(A) 44 · (B) 46 · (C) 48 · (D) 50 · (E) 60

<details>
<summary>Answer</summary>

**(B).** The mean is $480/15 = 32$, and in an evenly spaced set with an odd count the mean is the middle (8th) term. The largest term is 7 steps of 2 above it: $32 + 14 = 46$.

</details>

**7.** *(Medium)* Two numbers are added to the set $\{10, 14, 18, 22, 26\}$. Which of the following pairs would decrease the standard deviation the most?

(A) 10 and 26 · (B) 14 and 22 · (C) 18 and 18 · (D) 16 and 20 · (E) 0 and 36

<details>
<summary>Answer</summary>

**(C).** The mean is 18, and every pair listed is symmetric about 18, so the mean stays 18. The original total squared deviation is $64 + 16 + 0 + 16 + 64 = 160$; now it is shared among 7 values. The pair that adds the least squared deviation wins: (C) adds 0, (D) adds 8, (B) adds 32, (A) adds 128 and (E) adds 648. With (C) the variance falls from $160/5 = 32$ to $160/7 \approx 22.9$.

</details>

**8.** *(Hard)* A list of 5 positive integers has an average of 12, a median of 14, and a unique mode of 15. What is the greatest possible value of the smallest integer in the list?

(A) 2 · (B) 6 · (C) 7 · (D) 8 · (E) 14

<details>
<summary>Answer</summary>

**(C).** The sum is 60. Sorted: $a \le b \le 14 \le d \le e$. Since 15 is the mode, it appears at least twice, and it cannot be in the first three positions (they are at most 14), so $d = e = 15$. Then $a + b = 60 - 14 - 30 = 16$.

To maximise $a$, make $a$ and $b$ as close as possible. $a = b = 8$ would make 8 appear twice, tying with 15, so the mode would not be unique. The best is $a = 7$, $b = 9$: list $\{7, 9, 14, 15, 15\}$. Choice (D) is the trap that ignores "unique".

</details>

**9.** *(Hard)* Nine students took a test scored in whole numbers from 0 to 100. The average score was 70 and the median score was 75. What is the greatest possible value of the lowest score?

(A) 63 · (B) 64 · (C) 66 · (D) 70 · (E) 75

<details>
<summary>Answer</summary>

**(A).** Total $= 9 \times 70 = 630$. Sorted: $s_1 \le s_2 \le s_3 \le s_4 \le 75 \le s_6 \le \dots \le s_9$. To make $s_1$ large, make the top four as small as allowed: each is at least 75, so take $75$. Then $s_1 + s_2 + s_3 + s_4 = 630 - 5 \times 75 = 255$. Four numbers with sum 255, the smallest as large as possible: they cannot all be equal ($255/4 = 63.75$), so the smallest is at most 63, achieved by $63, 64, 64, 64$. Choice (B) rounds 63.75 the wrong way, and (E) assumes every score equals the median.

</details>

**10.** *(Hard)* At a company, the average salary of the men is \$60,000 and the average salary of the women is \$75,000. The average salary of all employees is \$66,000. If there are 40 more men than women, how many employees does the company have?

(A) 80 · (B) 120 · (C) 140 · (D) 160 · (E) 200

<details>
<summary>Answer</summary>

**(E).** See-saw: the overall mean is 6 (thousand) above the men's mean and 9 below the women's, so men : women $= 9 : 6 = 3 : 2$. The difference of 1 part is 40 people, so there are $5 \times 40 = 200$ employees (120 men, 80 women; choices (A) and (B) are the separate groups). Check: $(120 \cdot 60 + 80 \cdot 75)/200 = 13{,}200/200 = 66$.

</details>

**11.** *(Medium, Data Sufficiency)* The average (arithmetic mean) of the 5 numbers in list $L$ is 20. What is the median of $L$?

(1) The numbers in $L$ are consecutive multiples of 4.
(2) The range of $L$ is 16.

(A) Statement (1) alone is sufficient, but statement (2) alone is not sufficient.
(B) Statement (2) alone is sufficient, but statement (1) alone is not sufficient.
(C) Both statements together are sufficient, but neither statement alone is sufficient.
(D) Each statement alone is sufficient.
(E) Statements (1) and (2) together are not sufficient.

<details>
<summary>Answer</summary>

**(A).** (1): consecutive multiples of 4 form an evenly spaced set, so median = mean = 20. Sufficient. (2): $\{12, 20, 20, 20, 28\}$ has mean 20, range 16 and median 20, but $\{12, 14, 18, 28, 28\}$ has mean 20, range 16 and median 18. Not sufficient.

</details>

**12.** *(Medium, Data Sufficiency)* The average score of the $n$ students in a class is 80. What is $n$?

(1) If the student who scored 92 left the class, the average of the remaining students would be 79.
(2) If a new student who scored 94 joined the class, the average would be 81.

(A) Statement (1) alone is sufficient, but statement (2) alone is not sufficient.
(B) Statement (2) alone is sufficient, but statement (1) alone is not sufficient.
(C) Both statements together are sufficient, but neither statement alone is sufficient.
(D) Each statement alone is sufficient.
(E) Statements (1) and (2) together are not sufficient.

<details>
<summary>Answer</summary>

**(D).** (1): $80n - 92 = 79(n - 1)$ gives $n = 13$. (2): $80n + 94 = 81(n + 1)$ gives $n = 13$. Each statement is one linear equation in $n$ with a unique solution, so each is sufficient on its own. The trap is to think you need "both sums".

</details>

## Takeaways

- Turn every average into a sum ($\text{Sum} = \text{Mean} \times n$); sums add, averages do not.
- A two-group weighted average divides the gap between the group means in the inverse ratio of the group sizes.
- The median and range depend only on positions in the sorted list; the mean depends on every value.
- SD measures typical distance from the mean: adding a constant leaves it unchanged, multiplying by $k$ multiplies it by $\vert k \vert$.
- Compare SDs through deviations from each set's own mean, not through range.
- In evenly spaced sets, mean = median = (first + last)/2.
- To maximise one value with a fixed sum, minimise all the others, respecting every constraint in the stem.

## Further reading

- GMAC, *GMAT Official Guide* (current edition): the source of real retired Problem Solving and Data Sufficiency questions on statistics. Use it for timed practice after this chapter.
- Next in this module: [Overlapping sets](../../statistics-and-counting/overlapping-sets/) and [Counting and probability](../../statistics-and-counting/counting-and-probability/). For the statistics behind standard deviation beyond the GMAT, see [Distributions and likelihood](../../probability-and-statistics/distributions-and-likelihood/).
