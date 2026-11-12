+++
summary = "Count arrangements and selections with the fundamental counting principle, permutations, combinations, identical items, restrictions, circular arrangements and the slot method, then turn counts into simple probabilities."
+++

# Counting & Probability

Counting questions ask "how many ways?", and the numbers get large quickly, so listing is rarely an option. What makes the topic manageable is that almost every GMAT counting problem is built from **one principle** (multiply independent choices) and **one question** (does order matter?). Restrictions, identical items, circles and committees are all variations on those two ideas. This chapter builds them up step by step, then shows how counting turns into probability. Probability itself gets a full treatment in [Probability in depth](../../statistics-and-counting/probability-in-depth/).

## Key ideas

### The fundamental counting principle

If a task is done in stages, and stage 1 can be done in $m$ ways and stage 2 in $n$ ways **no matter what happened in stage 1**, then the whole task can be done in $m \times n$ ways. More stages, more factors.

*Why it works:* picture a tree. Stage 1 has $m$ branches; from the end of each, $n$ branches grow. The number of leaves is $m$ copies of $n$, that is $mn$.

Two words control which operation to use:

- **AND** (one stage, then another): **multiply**. A shirt *and* a tie: $5 \times 4 = 20$ outfits.
- **OR** (one case, or a separate case): **add**. Travel by one of 3 trains *or* one of 2 buses: $3 + 2 = 5$ options.

Optional stages add a "none" option: if a meal must have a main course and may have a dessert from a menu of 3, the dessert stage has $3 + 1 = 4$ outcomes.

### The slot method

The slot method is the counting principle made visual. Draw one slot per position, write the number of options in each slot, and multiply. The rule that makes it reliable: **fill the most restricted slot first.**

Example: how many 3-letter codes can be made from $A, B, C, D, E$ without repetition if the code must start with a vowel? The first slot is restricted (2 vowels: $A$, $E$); fill it first, then the others have 4 and 3 options left:

$$\underline{2} \times \underline{4} \times \underline{3} = 24.$$

If you filled the slots left to right in a problem where the *last* slot is restricted (for example, "the number must be even"), you would not know how many options remained for it. Start with the restriction.

> [!TIP]
> The slot method solves most digit and code problems in under a minute. For numbers, remember two classic restrictions: the first digit cannot be 0, and parity (odd/even) depends only on the last digit. When both apply, fill the last digit first, then the first digit, then the rest.

### Permutations: order matters

How many ways can you arrange $n$ different objects in a row? $n$ choices for the first position, $n - 1$ for the second, down to 1: $n!$ ("$n$ factorial"). By convention $0! = 1$.

If you arrange only $k$ of the $n$ objects (the order of the chosen ones matters), stop after $k$ slots:

> [!IMPORTANT]
> $$P(n, k) = n(n-1)\cdots(n-k+1) = \frac{n!}{(n-k)!}$$

Choosing a president, vice-president and treasurer from 10 people: $10 \times 9 \times 8 = 720$.

### Combinations: order doesn't matter

If you only care **which** $k$ objects are chosen, not in what order, each group of $k$ has been counted $k!$ times in $P(n, k)$ (once for each ordering of its members). Divide that out:

> [!IMPORTANT]
> $$\binom{n}{k} = \frac{P(n,k)}{k!} = \frac{n!}{k!\,(n-k)!}$$

A committee of 3 from 10 people: $\tfrac{720}{6} = 120$.

Useful facts for mental arithmetic: $\binom{n}{1} = n$, $\binom{n}{2} = \tfrac{n(n-1)}{2}$ (also the number of handshakes or games in a round robin), and $\binom{n}{k} = \binom{n}{n-k}$ (choosing who is in is the same as choosing who is out).

> [!WARNING]
> Before every counting problem, ask: **if I swap two of the chosen items, do I get a different outcome?** If yes (titles, positions, ordered digits, rankings), it is a permutation. If no (committees, teams, hands of cards, sets of toppings), it is a combination. Mixing these up is the single largest source of wrong answers, and both values always appear among the choices.

### Arrangements with identical items

If some objects are identical, swapping them doesn't create a new arrangement, so $n!$ overcounts. Divide by the factorial of each group of repeats:

$$\frac{n!}{a!\,b!\,c!\cdots}$$

where $a, b, c, \dots$ are the sizes of the groups of identical items. The letters of MISSISSIPPI (11 letters: 4 I, 4 S, 2 P, 1 M) can be arranged in

$$\frac{11!}{4!\,4!\,2!} = 34{,}650$$

distinct ways. *Why:* if the I's were labelled $I_1, \dots, I_4$, each distinct word would appear $4!$ times; likewise for the S's and P's.

The same formula counts arrangements of two kinds of items. The number of ways to arrange 3 identical red flags and 5 identical blue flags in a row is $\tfrac{8!}{3!\,5!} = \binom{8}{3} = 56$: you are only choosing which 3 of the 8 positions are red.

### Restrictions: together, apart and the complement

**Together.** To count arrangements where certain items must be adjacent, glue them into one block. Arrange the block with the other items, then multiply by the arrangements *inside* the block. Five people in a row with two particular people adjacent: the block plus 3 others is 4 units, $4! = 24$, times $2!$ for the order inside the block: 48.

**Apart.** Count the complement: $\text{apart} = \text{total} - \text{together}$. Five people with the two **not** adjacent: $120 - 48 = 72$.

**The complement in general.** "At least one", "not all" and "not both" conditions are usually faster as $\text{total} - \text{the opposite}$. Choosing 3 people from 8 (3 women, 5 men) with at least one woman: $\binom{8}{3} - \binom{5}{3} = 56 - 10 = 46$.

> [!WARNING]
> **The "at least one" overcount.** A tempting direct method is "choose one woman first, then any 2 others": $3 \times \binom{7}{2} = 63$. This counts a committee with two women twice (once for each woman chosen "first"), so it exceeds the true 46. Use the complement or split into cases (exactly 1, exactly 2, exactly 3 women) and add.

### Circular arrangements

Seating $n$ people around a round table, where only relative positions matter (rotations of the same seating count as one), gives

$$(n - 1)!$$

arrangements. *Why:* each seating has $n$ rotations, so divide $n!$ by $n$. Equivalently, seat one person anywhere as a fixed reference point; the remaining $n - 1$ people fill the seats in a row relative to that person. Restrictions work as before: two particular people adjacent around a table of 6 is $2 \times 4! = 48$ (the block plus 4 others form 5 units around the circle, giving $(5-1)!$, times 2 inside the block).

### Distributing items

Two very different situations hide behind "give items to people":

- **Distinct items, any number per person.** Each item independently picks its recipient. With $n$ items and $k$ people: $k^n$. Four different tasks among 3 people: $3^4 = 81$ (not $4^3$: the *items* are the stages).
- **Identical items.** Only how many each person gets matters. Line up the $n$ items and insert $k - 1$ dividers among them; each arrangement of items and dividers is one distribution. That is $\binom{n + k - 1}{k - 1}$ ways (the "stars and bars" count). Six identical apples among 3 children: $\binom{8}{2} = 28$.

If each person must get **at least one** identical item, hand out one each first, then distribute the rest freely: six apples, each child at least one, is $\binom{5}{2} = 10$. Any "at least $m$" condition works the same way.

### Committees with conditions

Committee problems combine selections with AND and OR:

- "**Exactly** 2 women and 1 man": $\binom{W}{2} \times \binom{M}{1}$ (AND: multiply).
- "**At least** 2 women": exactly 2 **or** exactly 3 or ...: add the cases, or subtract the small cases from the total.
- "$X$ and $Y$ refuse to serve together": total minus the committees containing both.
- "$X$ must serve": put $X$ on the committee and choose the remaining members from everyone else.

> [!TIP]
> **Sanity checks.** Most answer choices in counting questions differ by factors like $2$, $k!$ or a whole term. If you are unsure, shrink the problem (2 people instead of 6, a 3-letter word instead of 8) and list the cases by hand; then check that your method gives the same count on the small version.

### A short introduction to probability

When all outcomes are **equally likely**,

$$P(\text{event}) = \frac{\text{number of favourable outcomes}}{\text{total number of outcomes}}.$$

So every counting technique above is also a probability technique: count the favourable outcomes, count all outcomes, divide. Toss a fair coin 4 times: there are $2^4 = 16$ equally likely sequences, and only one (TTTT) has no head, so

$$P(\text{at least one head}) = 1 - \frac{1}{16} = \frac{15}{16}.$$

The complement trick, $P(\text{at least one}) = 1 - P(\text{none})$, is just as powerful in probability as in counting. Independent and dependent events, the addition rule, conditional probability and repeated trials are covered in [Probability in depth](../../statistics-and-counting/probability-in-depth/).

> [!WARNING]
> **Common traps**
> - Using a permutation for an unordered group (or a combination for ordered positions).
> - Counting "at least one" directly by "pick one, then pick the rest", which double-counts.
> - Forgetting to multiply by the internal order of a "together" block.
> - Forgetting that the first digit of a number cannot be 0.
> - Writing $n^k$ instead of $k^n$ when distributing $n$ distinct items among $k$ people.
> - Treating seats around a table as a row ($n!$ instead of $(n-1)!$).

> [!NOTE]
> Readers using Claude Code can check their counts with the `quantome-math` plugin (`/plugin install quantome-math@quantome`). It is optional: every problem here is designed to be done by hand.

## Worked examples

### Example 1 (Easy): optional stages

A restaurant's menu lists 4 starters, 5 main courses and 3 desserts. A meal must include exactly one main course, and may include at most one starter and at most one dessert. How many different meals are possible?

(A) 12 · (B) 60 · (C) 80 · (D) 100 · (E) 120

**Solution.** Three stages: starter (4 options or none: 5), main (5), dessert (3 options or none: 4). $5 \times 5 \times 4 = 100$. **Answer: (D).** Choice (B) forces a starter and a dessert ($4 \times 5 \times 3$); (C) forgets the "no starter" option only.

### Example 2 (Medium): identical letters

How many distinct arrangements of the letters in the word BALLOON are there?

(A) 630 · (B) 840 · (C) 1260 · (D) 2520 · (E) 5040

**Solution.** 7 letters with L twice and O twice: $\dfrac{7!}{2!\,2!} = \dfrac{5040}{4} = 1260$. **Answer: (C).** Choice (E) ignores the repeats, (D) corrects for only one of them.

### Example 3 (Medium): apart, by complement

In how many ways can 6 people stand in a row if two of them, Ana and Ben, refuse to stand next to each other?

(A) 240 · (B) 480 · (C) 520 · (D) 600 · (E) 720

**Solution.** Total arrangements: $6! = 720$. Together: glue Ana and Ben into a block, giving 5 units: $5! \times 2! = 240$. Apart: $720 - 240 = 480$. **Answer: (B).**

*Direct check (slot method):* arrange the other 4 people ($4! = 24$), creating 5 gaps (before, between, after). Ana and Ben take two different gaps in order: $5 \times 4 = 20$. $24 \times 20 = 480$. Choice (A) is the "together" count.

### Example 4 (Hard): at least one, by complement

A committee of 4 is to be chosen from 6 nurses and 4 doctors. How many different committees include at least one doctor?

(A) 15 · (B) 80 · (C) 120 · (D) 195 · (E) 336

**Solution.** All committees: $\binom{10}{4} = 210$. Committees with no doctor (all nurses): $\binom{6}{4} = 15$. At least one doctor: $210 - 15 = 195$. **Answer: (D).**

*Case check:* exactly 1, 2, 3 or 4 doctors: $4 \cdot 20 + 6 \cdot 15 + 4 \cdot 6 + 1 \cdot 1 = 80 + 90 + 24 + 1 = 195$. The trap (E) is "choose a doctor, then any 3 of the other 9": $4 \times 84 = 336$, which counts a committee with $d$ doctors $d$ times. Choice (B) is "exactly one doctor".

### Example 5 (Hard): distributing identical items

In how many ways can 8 identical coins be given to 3 children if each child must receive at least one coin?

(A) 15 · (B) 21 · (C) 36 · (D) 45 · (E) 56

**Solution.** Give each child one coin first; 5 coins remain to be shared with no restriction. Stars and bars: 5 coins and 2 dividers in a row, $\binom{7}{2} = 21$. **Answer: (B).** Choice (D), $\binom{10}{2} = 45$, ignores the "at least one" condition.

## Practice

**1.** *(Easy)* A lock code consists of 3 digits, each from 1 to 5, with no digit repeated. How many codes are possible?

(A) 10 · (B) 15 · (C) 20 · (D) 60 · (E) 125

<details>
<summary>Answer</summary>

**(D).** Order matters (123 and 321 are different codes): $5 \times 4 \times 3 = 60$. Choice (E) allows repeats ($5^3$); (A) is $\binom{5}{3}$, which ignores order.

</details>

**2.** *(Easy)* In a league of 9 teams, each team plays every other team exactly once. How many games are played?

(A) 18 · (B) 36 · (C) 72 · (D) 81 · (E) 504

<details>
<summary>Answer</summary>

**(B).** A game is an unordered pair of teams: $\binom{9}{2} = \tfrac{9 \times 8}{2} = 36$. Choice (C) counts each game twice (once from each team's side).

</details>

**3.** *(Medium)* Six people sit around a circular table. In how many ways can they be seated if two particular people must sit next to each other? (Seatings that are rotations of each other are considered the same.)

(A) 24 · (B) 36 · (C) 48 · (D) 96 · (E) 240

<details>
<summary>Answer</summary>

**(C).** Treat the pair as one unit: 5 units around a circle give $(5-1)! = 24$ arrangements, times 2 for the order within the pair: 48. Choice (E) is the answer for a row ($5! \times 2$), and (A) forgets the factor of 2.

</details>

**4.** *(Medium)* How many distinct arrangements of the letters in the word REFERRED are there?

(A) 280 · (B) 336 · (C) 560 · (D) 1120 · (E) 6720

<details>
<summary>Answer</summary>

**(D).** REFERRED has 8 letters: R three times, E three times, F and D once each. $\dfrac{8!}{3!\,3!} = \dfrac{40{,}320}{36} = 1120$. Choice (E) divides by only one $3!$.

</details>

**5.** *(Medium)* A team of 3 is chosen from 5 men and 4 women. How many teams contain exactly 2 women?

(A) 30 · (B) 40 · (C) 60 · (D) 74 · (E) 84

<details>
<summary>Answer</summary>

**(A).** Choose the 2 women AND the 1 man: $\binom{4}{2} \times \binom{5}{1} = 6 \times 5 = 30$. Choice (E) is all teams, $\binom{9}{3}$; (D) is "at least one woman", $84 - 10$.

</details>

**6.** *(Hard)* How many odd integers between 1000 and 9999 have four different digits?

(A) 1680 · (B) 2016 · (C) 2240 · (D) 2520 · (E) 4536

<details>
<summary>Answer</summary>

**(C).** Fill the most restricted slots first. Units digit (odd): 5 options. Thousands digit: not 0 and not the units digit: 8 options. Hundreds: any of the 8 remaining digits. Tens: 7. Total $5 \times 8 \times 8 \times 7 = 2240$. Choice (D), $5 \times 9 \times 8 \times 7$, forgets that the first digit can't be 0; (E) is the count of all 4-digit numbers with distinct digits.

</details>

**7.** *(Hard)* A committee of 4 is chosen from 9 people. Two of the people, Kai and Lina, refuse to serve together. How many committees are possible?

(A) 21 · (B) 84 · (C) 91 · (D) 105 · (E) 126

<details>
<summary>Answer</summary>

**(D).** All committees: $\binom{9}{4} = 126$. Committees containing both Kai and Lina: choose the other 2 from 7, $\binom{7}{2} = 21$. Allowed: $126 - 21 = 105$. Case check: neither ($\binom{7}{4} = 35$) plus exactly one of them ($2 \times \binom{7}{3} = 70$) $= 105$.

</details>

**8.** *(Hard)* Ten identical books are to be placed on 4 different shelves so that each shelf holds at least 2 books. In how many ways can this be done?

(A) 4 · (B) 10 · (C) 35 · (D) 84 · (E) 286

<details>
<summary>Answer</summary>

**(B).** Put 2 books on each shelf first; 2 books remain to be placed freely on 4 shelves. Stars and bars: $\binom{2 + 3}{3} = \binom{5}{3} = 10$. Listing confirms it: both extra books on one shelf (4 ways) or on two different shelves ($\binom{4}{2} = 6$ ways). Choices (D) and (E) are the "at least 1" and "no restriction" counts.

</details>

**9.** *(Hard)* In how many arrangements of the letters of the word EQUATION are all five vowels next to each other?

(A) 120 · (B) 576 · (C) 720 · (D) 1440 · (E) 2880

<details>
<summary>Answer</summary>

**(E).** EQUATION has 8 different letters: vowels E, U, A, I, O and consonants Q, T, N. Glue the vowels into one block: the block and 3 consonants make 4 units, $4! = 24$ arrangements; inside the block, $5! = 120$. Total $24 \times 120 = 2880$. Choice (A) counts only the orders inside the block, and (C), $3! \times 5!$, forgets that the block can sit in different positions among the consonants.

</details>

**10.** *(Medium, Data Sufficiency)* A group consists of $n$ people. How many different pairs of people can be chosen from the group?

(1) The $n$ people can stand in a row in exactly 120 different orders.
(2) Exactly 10 different groups of 3 people can be chosen from the group.

(A) Statement (1) alone is sufficient, but statement (2) alone is not sufficient.
(B) Statement (2) alone is sufficient, but statement (1) alone is not sufficient.
(C) Both statements together are sufficient, but neither statement alone is sufficient.
(D) Each statement alone is sufficient.
(E) Statements (1) and (2) together are not sufficient.

<details>
<summary>Answer</summary>

**(D).** The question asks for $\binom{n}{2}$, so we need $n$. (1): $n! = 120$ gives $n = 5$, because factorials grow strictly. Sufficient. (2): $\binom{n}{3} = 10$. Since $\binom{n}{3}$ increases with $n$ for $n \ge 3$ ($\binom{4}{3} = 4$, $\binom{5}{3} = 10$, $\binom{6}{3} = 20$), $n = 5$. Sufficient. Either way, $\binom{5}{2} = 10$.

</details>

**11.** *(Medium)* Four different tasks are to be assigned to 3 employees. Each task goes to exactly one employee, and an employee may receive any number of tasks, including none. How many assignments are possible?

(A) 12 · (B) 24 · (C) 64 · (D) 81 · (E) 256

<details>
<summary>Answer</summary>

**(D).** Each of the 4 tasks independently chooses one of 3 employees: $3 \times 3 \times 3 \times 3 = 3^4 = 81$. Choice (C), $4^3$, has the roles reversed (it would let each employee choose a task); (B) is $4!$.

</details>

## Takeaways

- Stages joined by AND multiply; separate cases joined by OR add.
- Fill the most restricted slot first.
- Ask "does swapping two chosen items give a new outcome?" Yes: permutation, $\tfrac{n!}{(n-k)!}$. No: combination, $\tfrac{n!}{k!(n-k)!}$.
- Identical items: divide $n!$ by the factorial of each repeat count.
- Together: glue into a block and multiply by its internal order. Apart, at least one, not both: use the complement.
- Around a circle: $(n-1)!$. Distinct items to people: $k^n$. Identical items: stars and bars, after handing out any required minimum.
- Probability with equally likely outcomes is favourable over total: count both.

## Further reading

- GMAC, *GMAT Official Guide* (current edition): real retired counting and probability questions for timed practice.
- Next: [Probability in depth](../../statistics-and-counting/probability-in-depth/). Counting reappears in the binomial distribution in [Distributions and likelihood](../../probability-and-statistics/distributions-and-likelihood/).
