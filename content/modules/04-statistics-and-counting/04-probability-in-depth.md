+++
summary = "Solve GMAT probability questions with the complement, the multiplication and addition rules, conditional probability, counting-based probability and repeated trials, while avoiding the classic traps."
+++

# Probability in Depth

GMAT probability questions are short, but they are built to punish one specific habit: reaching for a formula before thinking about **what the outcomes are**. Is the second draw affected by the first? Are the events allowed to happen together? Are the outcomes you are counting really equally likely? Answer those three questions and almost every problem becomes a short calculation. This chapter turns the brief introduction in [Counting and probability](../../statistics-and-counting/counting-and-probability/) into a complete toolkit for the exam.

## Key ideas

### The definition

When every outcome of an experiment is **equally likely**,

> [!IMPORTANT]
> $$P(\text{event}) = \frac{\text{number of favourable outcomes}}{\text{total number of outcomes}}$$

A probability is always between 0 (impossible) and 1 (certain). On the GMAT the answer is usually a fraction in lowest terms, so keep your work in fractions, not decimals.

The words "equally likely" carry the whole definition. Rolling two dice gives 36 equally likely **ordered** pairs $(1,1), (1,2), \dots, (6,6)$, but the 11 possible **sums** 2 to 12 are *not* equally likely: a sum of 7 arises in 6 ways, a sum of 2 in only one. Whenever you count, count outcomes that are genuinely equally likely, which usually means treating identical-looking objects as distinguishable (the two dice, the three red marbles) and keeping track of order.

### Complementary events and "at least one"

Every event $A$ has a complement "not $A$", and exactly one of them happens:

$$P(\text{not } A) = 1 - P(A).$$

The most important application is **"at least one"**. "At least one success" is the complement of "no successes", and "no successes" is usually a single, easy product:

$$P(\text{at least one}) = 1 - P(\text{none}).$$

If each of 4 independent attempts succeeds with probability $\tfrac{1}{3}$, then $P(\text{no success}) = \left(\tfrac{2}{3}\right)^4 = \tfrac{16}{81}$, so $P(\text{at least one}) = \tfrac{65}{81}$. Doing it directly would need four separate cases (exactly 1, 2, 3, 4 successes).

> [!TIP]
> Whenever you see "at least one", "at least 1 of", or "not all", try the complement first. It is the single most useful shortcut in GMAT probability.

### "And": independent events

Two events are **independent** if the outcome of one does not change the probability of the other: separate coin tosses, separate dice, draws **with replacement**. For independent events,

$$P(A \text{ and } B) = P(A) \times P(B).$$

*Why it works:* if $A$ happens in a fraction $P(A)$ of all trials and, independently, $B$ happens in a fraction $P(B)$ of *those*, then both happen in a fraction $P(A) \cdot P(B)$ of all trials. It is the counting principle with fractions: two dice have $6 \times 6$ outcomes, and "first die 6 and second die 6" is $1 \times 1$ of them, $\tfrac{1}{6} \times \tfrac{1}{6} = \tfrac{1}{36}$.

### "And": dependent events (without replacement)

When the first outcome changes what is available for the second, the events are **dependent**, and you multiply by the **updated** probability:

$$P(A \text{ and } B) = P(A) \times P(B \mid A),$$

where $P(B \mid A)$ is the probability of $B$ once you know $A$ happened. A bag holds 3 red and 2 blue marbles. Draw two **without** replacement:

$$P(\text{both red}) = \frac{3}{5} \times \frac{2}{4} = \frac{3}{10}.$$

After the first red marble is gone, only 2 of the remaining 4 are red. **With** replacement the draws are independent: $\tfrac{3}{5} \times \tfrac{3}{5} = \tfrac{9}{25}$. The question's wording ("without replacement", "two different", "at the same time", "a committee") tells you which one applies. Drawing two at once is the same as drawing one after the other without replacement.

### "Or": the addition rule

For "$A$ or $B$" (meaning at least one of them):

$$P(A \text{ or } B) = P(A) + P(B) - P(A \text{ and } B).$$

This is the two-set formula from [Overlapping sets](../../statistics-and-counting/overlapping-sets/): adding $P(A)$ and $P(B)$ counts the outcomes where both happen twice, so subtract them once. If $A$ and $B$ are **mutually exclusive** (they cannot happen together), the overlap is 0 and the probabilities simply add.

Example: a card is drawn from cards numbered 1 to 20. $P(\text{even}) = \tfrac{10}{20}$, $P(\text{multiple of 5}) = \tfrac{4}{20}$, and $P(\text{both}) = \tfrac{2}{20}$ (10 and 20). So $P(\text{even or multiple of 5}) = \tfrac{10 + 4 - 2}{20} = \tfrac{3}{5}$.

> [!WARNING]
> "Mutually exclusive" and "independent" are different, almost opposite, ideas. Mutually exclusive events with positive probabilities are *dependent*: if one happens, the other certainly doesn't. Add probabilities for mutually exclusive events ("or"); multiply for independent events ("and").

### Conditional probability

$P(A \mid B)$, "the probability of $A$ given $B$", is the probability of $A$ when you already know $B$ happened. Knowing $B$ **shrinks the sample space** to the outcomes in $B$:

$$P(A \mid B) = \frac{P(A \text{ and } B)}{P(B)} = \frac{\text{outcomes in both } A \text{ and } B}{\text{outcomes in } B}.$$

A die shows a number greater than 3. What is the probability it is even? The new sample space is $\{4, 5, 6\}$, and two of these are even: $\tfrac{2}{3}$.

On the GMAT, conditional probability almost always appears as a **table of counts**: a double-set matrix (see [Overlapping sets](../../statistics-and-counting/overlapping-sets/)) with a question like "if a person chosen at random tested positive, what is the probability that..." The method is mechanical: find the row or column for the condition, and use **its total** as the denominator. The same idea, with general probabilities instead of counts, is Bayes' theorem in [Probability and Bayes' theorem](../../probability-and-statistics/probability-and-bayes-theorem/).

> [!WARNING]
> $P(A \mid B)$ is not $P(B \mid A)$. "The probability of a positive test among people with the condition" and "the probability of having the condition among people who test positive" have different denominators and are usually very different numbers. Both always appear among the answer choices.

### Probability via counting

When outcomes are equally likely, count with the tools from [Counting and probability](../../statistics-and-counting/counting-and-probability/):

$$P = \frac{\text{favourable selections}}{\text{all selections}}.$$

For unordered selections (committees, hands, handfuls of marbles), use **combinations in both numerator and denominator**. Choosing 3 people from 6 men and 4 women, the probability of exactly 2 women is

$$\frac{\binom{4}{2}\binom{6}{1}}{\binom{10}{3}} = \frac{6 \times 6}{120} = \frac{3}{10}.$$

The one rule: numerator and denominator must count the same kind of object. If the denominator counts unordered groups, so must the numerator; if you count ordered sequences on the bottom, count ordered sequences on top. Either approach gives the same probability, because each unordered group corresponds to the same number of ordered sequences.

> [!TIP]
> Many problems can be done **both** ways: sequential multiplication ($\tfrac{4}{10} \cdot \tfrac{3}{9} \cdots$) or combinations. When the sequential method needs an "arrangements" factor (which draw was the man?), combinations are usually safer; when there are just two or three draws with no ordering issue, multiplication is faster.

### Repeated trials: "exactly $k$ of $n$"

Suppose a trial with success probability $p$ is repeated $n$ times independently. Any **one particular** sequence with exactly $k$ successes (say SSFF...) has probability $p^k(1-p)^{n-k}$. The successes can be placed in any $k$ of the $n$ positions, which can be done in $\binom{n}{k}$ ways, and these sequences are mutually exclusive, so

> [!IMPORTANT]
> $$P(\text{exactly } k \text{ successes in } n \text{ trials}) = \binom{n}{k}\, p^k (1-p)^{n-k}$$

Four fair coin tosses, exactly 2 heads: $\binom{4}{2}\left(\tfrac{1}{2}\right)^4 = \tfrac{6}{16} = \tfrac{3}{8}$. For "at least $k$", add the cases from $k$ to $n$, or use the complement if that has fewer cases. This is the binomial distribution, treated more formally in [Distributions and likelihood](../../probability-and-statistics/distributions-and-likelihood/).

> [!TIP]
> **Sanity checks.** A probability must be between 0 and 1. "At least one" must be at least as large as each single event. "Exactly $k$" summed over all $k$ must give 1. If an answer choice violates one of these, cross it out, even before you compute.

### Common probability traps

> [!WARNING]
> **What the wrong answer choices are built from**
> - **Missing the $\binom{n}{k}$ factor.** "Exactly 2 heads in 3 tosses" is not $\left(\tfrac12\right)^3 = \tfrac18$: there are 3 orders (HHT, HTH, THH), so it is $\tfrac38$.
> - **Treating non-equally-likely outcomes as equally likely.** "0, 1, 2 or 3 heads, so each has probability $\tfrac14$" is wrong for the same reason.
> - **With vs without replacement.** Using $\tfrac35 \cdot \tfrac35$ when the marble is not put back.
> - **Adding instead of multiplying** (or the reverse): "and" for independent events multiplies; "or" for exclusive events adds.
> - **Forgetting the overlap** in "or" questions: counting multiples of both 3 and 5 twice.
> - **Inverting a conditional probability**: dividing by the wrong row or column total.
> - **Computing "at least one" as a sum** $P(A) + P(B)$ for events that can happen together, which can even give a "probability" above 1.

> [!NOTE]
> Readers using Claude Code can check their working with the `quantome-math` plugin (`/plugin install quantome-math@quantome`). It is optional: every problem here is designed to be done by hand.

## Worked examples

### Example 1 (Easy): counting outcomes with two dice

Two fair six-sided dice are rolled. What is the probability that the sum of the numbers rolled is 8?

(A) $\tfrac{1}{9}$ · (B) $\tfrac{5}{36}$ · (C) $\tfrac{1}{6}$ · (D) $\tfrac{7}{36}$ · (E) $\tfrac{2}{9}$

**Solution.** There are 36 equally likely ordered outcomes. Sum 8: $(2,6), (3,5), (4,4), (5,3), (6,2)$, five outcomes. $P = \tfrac{5}{36}$. **Answer: (B).** Counting $(2,6)$ and $(6,2)$ as one outcome gives 3 favourable cases out of 21 "unordered" outcomes, which are not equally likely.

### Example 2 (Medium): at least one

A fair die is rolled 3 times. What is the probability of rolling at least one 6?

(A) $\tfrac{1}{6}$ · (B) $\tfrac{25}{72}$ · (C) $\tfrac{91}{216}$ · (D) $\tfrac{1}{2}$ · (E) $\tfrac{125}{216}$

**Solution.** $P(\text{no 6}) = \left(\tfrac{5}{6}\right)^3 = \tfrac{125}{216}$, so $P(\text{at least one 6}) = 1 - \tfrac{125}{216} = \tfrac{91}{216}$. **Answer: (C).**

Each distractor has a story: (E) is $P(\text{no 6})$, forgetting to subtract from 1; (B) is $P(\text{exactly one 6}) = 3 \cdot \tfrac{1}{6} \cdot \tfrac{25}{36} = \tfrac{75}{216}$; (D) is $\tfrac{1}{6} + \tfrac{1}{6} + \tfrac{1}{6}$, the "just add them" error (which would give more than 1 for seven rolls).

### Example 3 (Medium): without replacement

A box contains 12 light bulbs, 4 of which are defective. Two bulbs are chosen at random without replacement. What is the probability that exactly one of them is defective?

(A) $\tfrac{1}{11}$ · (B) $\tfrac{8}{33}$ · (C) $\tfrac{14}{33}$ · (D) $\tfrac{4}{9}$ · (E) $\tfrac{16}{33}$

**Solution (counting).** Pairs in total: $\binom{12}{2} = 66$. Pairs with one defective and one good: $4 \times 8 = 32$. $P = \tfrac{32}{66} = \tfrac{16}{33}$. **Answer: (E).**

**Solution (sequential).** Defective then good: $\tfrac{4}{12} \cdot \tfrac{8}{11} = \tfrac{8}{33}$. Good then defective: $\tfrac{8}{12} \cdot \tfrac{4}{11} = \tfrac{8}{33}$. These are exclusive, so add: $\tfrac{16}{33}$. Choice (B) forgets the second order. Choice (D) is the answer *with* replacement ($2 \cdot \tfrac{1}{3} \cdot \tfrac{2}{3}$), and (C) is the probability of no defective bulb.

### Example 4 (Hard): conditional probability from a table

In a screening study of 200 people, 40 have a certain condition. Of those 40, 30 test positive; of the 160 without the condition, 16 test positive. If a person in the study who tested positive is chosen at random, what is the probability that the person has the condition?

(A) $\tfrac{3}{20}$ · (B) $\tfrac{23}{100}$ · (C) $\tfrac{8}{23}$ · (D) $\tfrac{15}{23}$ · (E) $\tfrac{3}{4}$

**Solution.** Build the table:

| | Positive | Negative | **Total** |
|---|---|---|---|
| **Condition** | 30 | 10 | 40 |
| **No condition** | 16 | 144 | 160 |
| **Total** | 46 | 154 | 200 |

"Given positive" restricts us to the Positive column, 46 people. Of these, 30 have the condition: $\tfrac{30}{46} = \tfrac{15}{23}$. **Answer: (D).**

Choice (E) is the inverse conditional, $P(\text{positive} \mid \text{condition}) = \tfrac{30}{40}$. Choice (A) uses the wrong denominator ($\tfrac{30}{200}$, the probability of *both*). Choice (B) is $P(\text{positive})$, and (C) is the probability of *not* having the condition given a positive test.

### Example 5 (Hard): exactly $k$ of $n$

A basketball player makes each free throw with probability $\tfrac{2}{3}$, independently of other throws. If she takes 3 free throws, what is the probability that she makes exactly 2?

(A) $\tfrac{4}{27}$ · (B) $\tfrac{8}{27}$ · (C) $\tfrac{4}{9}$ · (D) $\tfrac{2}{3}$ · (E) $\tfrac{20}{27}$

**Solution.** One particular order (make, make, miss) has probability $\tfrac{2}{3} \cdot \tfrac{2}{3} \cdot \tfrac{1}{3} = \tfrac{4}{27}$. The miss can be any of the 3 throws, so

$$P = \binom{3}{2} \cdot \frac{4}{27} = \frac{12}{27} = \frac{4}{9}.$$

**Answer: (C).** Choice (A) forgets the 3 orders (the most common binomial trap), (B) is $P(\text{all three})$ and (E) is $P(\text{at least two}) = \tfrac{12}{27} + \tfrac{8}{27}$.

## Practice

**1.** *(Easy)* A card is drawn at random from 30 cards numbered 1 to 30. What is the probability that the number is a multiple of 3 or a multiple of 5?

(A) $\tfrac{1}{3}$ · (B) $\tfrac{7}{15}$ · (C) $\tfrac{1}{2}$ · (D) $\tfrac{8}{15}$ · (E) $\tfrac{3}{5}$

<details>
<summary>Answer</summary>

**(B).** Multiples of 3: 10. Multiples of 5: 6. Multiples of both (of 15): 2. Using the addition rule, $\tfrac{10 + 6 - 2}{30} = \tfrac{14}{30} = \tfrac{7}{15}$. Choice (D) forgets to subtract the overlap (15 and 30).

</details>

**2.** *(Easy)* On any given day, the probability of rain in a town is 0.3, independently of other days. What is the probability that it rains on at least one of the next two days?

(A) 0.09 · (B) 0.3 · (C) 0.42 · (D) 0.51 · (E) 0.6

<details>
<summary>Answer</summary>

**(D).** $P(\text{no rain on either day}) = 0.7 \times 0.7 = 0.49$, so $P(\text{at least one}) = 1 - 0.49 = 0.51$. Choice (E) adds the probabilities and double-counts the days with rain on both; (C) is "exactly one day"; (A) is "both days".

</details>

**3.** *(Medium)* Two fair six-sided dice are rolled. What is the probability that the product of the two numbers is even?

(A) $\tfrac{1}{4}$ · (B) $\tfrac{1}{2}$ · (C) $\tfrac{2}{3}$ · (D) $\tfrac{3}{4}$ · (E) $\tfrac{5}{6}$

<details>
<summary>Answer</summary>

**(D).** A product is odd only if both numbers are odd: $\tfrac{1}{2} \cdot \tfrac{1}{2} = \tfrac{1}{4}$. So $P(\text{even}) = 1 - \tfrac{1}{4} = \tfrac{3}{4}$. Choice (A) is the probability of an odd product.

</details>

**4.** *(Medium)* A drawer contains 5 black socks and 3 white socks. Two socks are taken out at random without replacement. What is the probability that they are the same colour?

(A) $\tfrac{5}{14}$ · (B) $\tfrac{13}{28}$ · (C) $\tfrac{1}{2}$ · (D) $\tfrac{17}{32}$ · (E) $\tfrac{15}{28}$

<details>
<summary>Answer</summary>

**(B).** Pairs: $\binom{8}{2} = 28$. Same colour: $\binom{5}{2} + \binom{3}{2} = 10 + 3 = 13$. $P = \tfrac{13}{28}$. Choice (D) is the with-replacement answer $\left(\tfrac{25}{64} + \tfrac{9}{64}\right)$; (A) counts only two black socks; (E) is the probability of different colours.

</details>

**5.** *(Medium)* Three people are chosen at random from a group of 5 men and 5 women. What is the probability that at least one woman is chosen?

(A) $\tfrac{1}{12}$ · (B) $\tfrac{1}{2}$ · (C) $\tfrac{5}{6}$ · (D) $\tfrac{7}{8}$ · (E) $\tfrac{11}{12}$

<details>
<summary>Answer</summary>

**(E).** $P(\text{no woman}) = \dfrac{\binom{5}{3}}{\binom{10}{3}} = \dfrac{10}{120} = \dfrac{1}{12}$, so the answer is $1 - \tfrac{1}{12} = \tfrac{11}{12}$. Sequentially: $\tfrac{5}{10} \cdot \tfrac{4}{9} \cdot \tfrac{3}{8} = \tfrac{1}{12}$. Choice (D) treats the choices as independent with probability $\tfrac{1}{2}$ each, $1 - \left(\tfrac{1}{2}\right)^3$, ignoring that people are not replaced.

</details>

**6.** *(Medium)* Two archers each shoot once at a target. Archer X hits with probability $\tfrac{1}{2}$ and archer Y hits with probability $\tfrac{1}{3}$, independently. What is the probability that exactly one of them hits the target?

(A) $\tfrac{1}{6}$ · (B) $\tfrac{1}{3}$ · (C) $\tfrac{1}{2}$ · (D) $\tfrac{2}{3}$ · (E) $\tfrac{5}{6}$

<details>
<summary>Answer</summary>

**(C).** X hits and Y misses: $\tfrac{1}{2} \cdot \tfrac{2}{3} = \tfrac{1}{3}$. X misses and Y hits: $\tfrac{1}{2} \cdot \tfrac{1}{3} = \tfrac{1}{6}$. These are exclusive, so add: $\tfrac{1}{2}$. Choice (D) is "at least one" ($1 - \tfrac{1}{2} \cdot \tfrac{2}{3}$), and (E) is the invalid sum $\tfrac{1}{2} + \tfrac{1}{3}$.

</details>

**7.** *(Hard)* Two fair six-sided dice are rolled, and the sum is 8. Given this, what is the probability that at least one of the dice shows a 6?

(A) $\tfrac{1}{18}$ · (B) $\tfrac{1}{6}$ · (C) $\tfrac{11}{36}$ · (D) $\tfrac{1}{3}$ · (E) $\tfrac{2}{5}$

<details>
<summary>Answer</summary>

**(E).** The condition shrinks the sample space to the 5 outcomes with sum 8: $(2,6), (3,5), (4,4), (5,3), (6,2)$. Two of them contain a 6: $\tfrac{2}{5}$. Choice (C) ignores the condition ($P(\text{at least one 6}) = \tfrac{11}{36}$); (A) is $P(\text{sum 8 and a 6}) = \tfrac{2}{36}$, the wrong denominator.

</details>

**8.** *(Hard)* Three people are chosen at random from 4 married couples. What is the probability that no two of the people chosen are married to each other?

(A) $\tfrac{1}{7}$ · (B) $\tfrac{3}{7}$ · (C) $\tfrac{4}{7}$ · (D) $\tfrac{5}{7}$ · (E) $\tfrac{6}{7}$

<details>
<summary>Answer</summary>

**(C).** *Counting:* choose 3 of the 4 couples to be represented, $\binom{4}{3} = 4$, then one partner from each, $2^3 = 8$: 32 favourable groups out of $\binom{8}{3} = 56$. $\tfrac{32}{56} = \tfrac{4}{7}$.

*Sequential:* the first person can be anyone; the second must avoid the first person's spouse, $\tfrac{6}{7}$; the third must avoid both spouses, $\tfrac{4}{6}$. $\tfrac{6}{7} \cdot \tfrac{2}{3} = \tfrac{4}{7}$. Choice (B) is the complement (at least one couple chosen).

</details>

**9.** *(Hard)* A quiz has 5 questions, each with 4 answer options, exactly one of which is correct. A student guesses every answer at random. What is the probability that the student gets at least 4 questions right?

(A) $\tfrac{1}{1024}$ · (B) $\tfrac{1}{256}$ · (C) $\tfrac{15}{1024}$ · (D) $\tfrac{1}{64}$ · (E) $\tfrac{5}{256}$

<details>
<summary>Answer</summary>

**(D).** Exactly 4: $\binom{5}{4}\left(\tfrac{1}{4}\right)^4\left(\tfrac{3}{4}\right) = \tfrac{15}{1024}$. Exactly 5: $\left(\tfrac{1}{4}\right)^5 = \tfrac{1}{1024}$. Total $\tfrac{16}{1024} = \tfrac{1}{64}$. Choice (C) forgets the "all 5" case, (A) is that case alone, and (B), $\left(\tfrac{1}{4}\right)^4$, forgets both the 5 positions of the wrong answer and the $\tfrac{3}{4}$.

</details>

**10.** *(Hard)* A bag contains 2 red and 3 blue marbles. Ana and Ben take turns drawing one marble at a time, without replacement, with Ana drawing first. The first person to draw a red marble wins. What is the probability that Ana wins?

(A) $\tfrac{1}{2}$ · (B) $\tfrac{3}{5}$ · (C) $\tfrac{2}{3}$ · (D) $\tfrac{7}{10}$ · (E) $\tfrac{4}{5}$

<details>
<summary>Answer</summary>

**(B).** Ana draws 1st, 3rd and 5th. She wins on draw 1 with probability $\tfrac{2}{5}$. She wins on draw 3 if the first two are blue and the third red: $\tfrac{3}{5} \cdot \tfrac{2}{4} \cdot \tfrac{2}{3} = \tfrac{1}{5}$. Draw 5 never decides the game: with only 3 blue marbles, a red marble appears by draw 4 at the latest. Total $\tfrac{2}{5} + \tfrac{1}{5} = \tfrac{3}{5}$.

*Check:* Ben wins on draw 2 ($\tfrac{3}{5} \cdot \tfrac{2}{4} = \tfrac{3}{10}$) or draw 4 ($\tfrac{3}{5} \cdot \tfrac{2}{4} \cdot \tfrac{1}{3} \cdot 1 = \tfrac{1}{10}$), total $\tfrac{2}{5}$, and $\tfrac{3}{5} + \tfrac{2}{5} = 1$.

</details>

**11.** *(Hard, Data Sufficiency)* A bag contains only red and blue marbles. Two marbles are drawn at random without replacement. Is the probability that both are red greater than $\tfrac{1}{2}$?

(1) More than $\tfrac{3}{4}$ of the marbles in the bag are red.
(2) There are 12 marbles in the bag.

(A) Statement (1) alone is sufficient, but statement (2) alone is not sufficient.
(B) Statement (2) alone is sufficient, but statement (1) alone is not sufficient.
(C) Both statements together are sufficient, but neither statement alone is sufficient.
(D) Each statement alone is sufficient.
(E) Statements (1) and (2) together are not sufficient.

<details>
<summary>Answer</summary>

**(A).** Let there be $r$ red marbles out of $n$; $P(\text{both red}) = \tfrac{r}{n} \cdot \tfrac{r-1}{n-1}$.

(1): $\tfrac{r}{n} > \tfrac{3}{4}$ and $r, n$ are integers, so $4r \ge 3n + 1$, i.e. $r - 1 \ge \tfrac{3n - 3}{4}$, which gives $\tfrac{r-1}{n-1} \ge \tfrac{3}{4}$. Then $P > \tfrac{3}{4} \cdot \tfrac{3}{4} = \tfrac{9}{16} > \tfrac{1}{2}$. The answer is always "yes". Sufficient. (The tightest cases, such as 7 red out of 9 with $P = \tfrac{7}{12}$, confirm it.)

(2): with 12 marbles, 12 red gives $P = 1$ (yes), while 6 red gives $P = \tfrac{6}{12} \cdot \tfrac{5}{11} = \tfrac{5}{22}$ (no). Not sufficient.

</details>

**12.** *(Medium, Data Sufficiency)* $A$ and $B$ are events. What is the probability that at least one of $A$ and $B$ occurs?

(1) $P(A) = 0.5$ and $P(B) = 0.4$.
(2) $A$ and $B$ are independent.

(A) Statement (1) alone is sufficient, but statement (2) alone is not sufficient.
(B) Statement (2) alone is sufficient, but statement (1) alone is not sufficient.
(C) Both statements together are sufficient, but neither statement alone is sufficient.
(D) Each statement alone is sufficient.
(E) Statements (1) and (2) together are not sufficient.

<details>
<summary>Answer</summary>

**(C).** $P(A \text{ or } B) = P(A) + P(B) - P(A \text{ and } B)$. (1) leaves the overlap unknown: anywhere from 0 (giving 0.9) to 0.4 (giving 0.5). Not sufficient. (2) gives no probabilities at all. Not sufficient. Together, independence gives $P(A \text{ and } B) = 0.5 \times 0.4 = 0.2$, so $P(A \text{ or } B) = 0.5 + 0.4 - 0.2 = 0.7$. Sufficient.

</details>

## Takeaways

- Probability is favourable over total **only** for equally likely outcomes; make outcomes distinguishable and ordered when in doubt.
- "At least one" $= 1 - P(\text{none})$.
- "And": multiply, using updated probabilities when drawing without replacement.
- "Or": add, then subtract the overlap; the overlap is 0 only for mutually exclusive events.
- Conditional probability shrinks the sample space: divide by the total of the given row or column.
- For selections, use combinations in both numerator and denominator, or multiply sequential fractions and account for orders.
- Exactly $k$ of $n$ independent trials: $\binom{n}{k} p^k (1-p)^{n-k}$; never forget the $\binom{n}{k}$.

## Further reading

- GMAC, *GMAT Official Guide* (current edition): real retired probability questions in Problem Solving and Data Sufficiency format.
- Within this book: [Probability and Bayes' theorem](../../probability-and-statistics/probability-and-bayes-theorem/) develops conditional probability into Bayes' theorem, and [Distributions and likelihood](../../probability-and-statistics/distributions-and-likelihood/) treats the binomial distribution formally.
