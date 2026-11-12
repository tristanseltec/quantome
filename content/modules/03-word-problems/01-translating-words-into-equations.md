+++
summary = "Turn GMAT word problems into correct equations: a translation dictionary, choosing variables, and the standard age, consecutive-integer, coin, ticket and digit set-ups, with the traps that wrong answer choices are built from."
+++

# Translating Words into Equations

Most GMAT word problems are not hard algebra. Once the equation is on paper, the algebra is usually a line or two from [Linear equations](../../algebra/linear-equations/). The difficulty is the **translation**: turning a sentence like "seven less than four times a number is eleven more than the number" into $4x - 7 = x + 11$, and not into $7 - 4x = x + 11$.

The test writers know exactly where translations go wrong, and they build wrong answer choices from those mistakes. A reader who translates carefully gets the question right. A reader who translates quickly but carelessly gets one of the distractors, and the distractor is always there waiting.

This chapter gives you a translation dictionary, a method for choosing variables, and the five classic set-ups (age, consecutive integers, coins and tickets, number and digit problems, and "how many more" questions). The later chapters in this module, [Rates and work](../rates-and-work/), [Mixtures and interest](../mixtures-and-interest/) and [Profit, discount and percent problems](../profit-discount-and-percent-problems/), all rely on these skills.

## Key ideas

### The translation dictionary

English has a small number of words that map almost mechanically onto symbols. Learn them as you would learn vocabulary.

| English | Symbol | Example | Translation |
|---|---|---|---|
| is, was, will be, equals, gives, results in | $=$ | "A is 5 more than B" | $A = B + 5$ |
| of (with a fraction or percent) | $\times$ | "30% of $x$" | $0.3x$ |
| more than, increased by, exceeds by | $+$ | "3 more than $y$" | $y + 3$ |
| less than, fewer than, decreased by | $-$ (order reversed) | "3 less than $y$" | $y - 3$ |
| times, product of, twice, triple | $\times$ | "twice the sum of $a$ and $b$" | $2(a + b)$ |
| per, for each, ratio of, divided by | $\div$ | "miles per gallon" | $\dfrac{\text{miles}}{\text{gallons}}$ |
| what, a number, how many | variable | "what percent of 40 is 10?" | $\dfrac{p}{100}\cdot 40 = 10$ |
| $x$ percent | $\dfrac{x}{100}$ | "$x$ percent of 80" | $\dfrac{x}{100}\cdot 80$ |
| at least / at most | $\ge$ / $\le$ | "at least 12" | $\ge 12$ |
| exceeds, is greater than | $>$ | "$A$ exceeds $B$ by 4" | $A - B = 4$ |

Three entries need extra care.

**"Less than" reverses the order.** "Five less than $x$" means you start with $x$ and take 5 away: $x - 5$. The words appear in the order "5 … $x$", but the symbols appear in the order "$x$ … 5". The same is true of "fewer than" and "subtracted from": "$a$ subtracted from $b$" is $b - a$. By contrast, "$x$ minus 5" and "$x$ decreased by 5" keep the order of the words.

> [!WARNING]
> "$x$ less than $y$" is $y - x$, **not** $x - y$. "The number of boys is 4 less than the number of girls" is $B = G - 4$. Sanity check: girls outnumber boys, so the boys' count must equal the girls' count *minus* 4. Always ask "which quantity is larger?" and check that your equation agrees.

**"Of" means multiply only when it follows a fraction or percent.** "Half of the students" is $\tfrac12 S$. "Twenty percent of the remainder" is $0.2(\text{remainder})$, and the most common mistake is to apply that 20% to the original total instead of to the remainder.

**"Is" marks the equals sign.** Every sentence that contains "is" or "was" is a candidate equation. If a problem has two unknowns, look for two such sentences.

### Why a careful translation is enough

An equation is just a sentence written in a language with fewer ambiguities. If each phrase is translated faithfully and the pieces are joined with the grammar of the sentence, the equation must be correct, because each symbol stands for exactly the same quantity as the words. So the work is local: translate one phrase at a time, then assemble. Don't try to "see" the whole equation at once.

For example, "Seven less than four times a number is eleven more than the number":

1. "a number" → $x$
2. "four times a number" → $4x$
3. "seven less than [that]" → $4x - 7$
4. "is" → $=$
5. "eleven more than the number" → $x + 11$

Result: $4x - 7 = x + 11$, so $3x = 18$ and $x = 6$.

### Defining variables: choose what to call $x$

Before writing anything, write down what each variable means, **with units**: "$c$ = number of child tickets", not "$c$ = children". This forces you to notice whether $c$ is a count, a price, or a total amount of money.

Some rules for choosing variables:

- **Let $x$ be the quantity asked for**, when that keeps the equation simple. You can't then forget to answer the actual question.
- **Otherwise let $x$ be the smallest or most basic quantity**, and express the others in terms of it. If "Ann has 3 times as many as Bea, and Cal has 5 more than Ann", let Bea have $b$. Then Ann has $3b$ and Cal has $3b + 5$. No fractions appear. If you started from Ann, Bea would be $\tfrac{a}{3}$.
- **Use one variable when you can, two when the problem gives two separate facts.** Two variables with two equations is often clearer than one variable with a complicated expression. Use whichever you find less error-prone.
- **Use the middle term for symmetric lists.** For five consecutive integers, call them $m-2, m-1, m, m+1, m+2$. Their sum is $5m$ immediately.

> [!TIP]
> Before solving, **write the question in symbols** too. "How many more adult tickets than child tickets?" is "find $a - c$", not "find $a$". Many GMAT distractors are the value of a variable when the question asked for a difference, a sum, or a value at another time.

### Age problems

Age problems hinge on one fact: **everyone ages at the same rate**. If Maria is $m$ today, she was $m - 6$ six years ago and will be $m + 4$ four years from now. The difference between two people's ages never changes; their ratio does.

A reliable layout is a table with a row for each person and a column for each time:

| | 6 years ago | Now | In 4 years |
|---|---|---|---|
| Ken | $k - 6$ | $k$ | $k + 4$ |
| Lea | $l - 6$ | $l$ | $l + 4$ |

Then translate each sentence using **one column at a time**. "Six years ago, Ken was 4 times as old as Lea" uses only the first column: $k - 6 = 4(l - 6)$.

> [!WARNING]
> The classic error is mixing columns: writing $k - 6 = 4l - 6$ (forgetting to shift Lea's age) or $k + 4 = 2l + 4$. Each person's age gets the time shift, and the shift goes **inside** the parentheses before you multiply.

### Consecutive-integer problems

Consecutive integers differ by 1: $n, n+1, n+2, \dots$. Consecutive **even** integers and consecutive **odd** integers both differ by 2: $n, n+2, n+4, \dots$ (with $n$ even or odd, respectively).

Two facts make these quick:

- **The average of an evenly spaced list equals its middle term** (or the average of the two middle terms). So the sum of $k$ evenly spaced numbers is $k$ times the middle term. For example, seven consecutive integers with sum 182 have middle term $182 / 7 = 26$.
- **Shifting every term by $d$ shifts the sum by $kd$.** The next seven consecutive integers after a block of seven are each 7 larger, so their sum is $182 + 7 \times 7 = 231$.

Why does the average equal the middle term? Pair the terms from the outside in: smallest with largest, second smallest with second largest, and so on. Each pair has the same sum, so each pair averages to the middle.

### Coin, ticket and "mixture of items" problems

These problems always have **two kinds of equation**: one that counts items and one that counts value.

$$
\text{number of items: } a + c = N, \qquad \text{total value: } p_a a + p_c c = V
$$

Coins are the same, with values 5, 10 and 25 cents. Work in cents so that everything is an integer.

> [!TIP]
> **Backsolve** when the answer choices are counts. Pick choice (C), compute the total value, and see whether you need more or fewer of the expensive item. Because the value changes by the same amount for each item you swap, you can often see the correct answer after one test.

A useful shortcut: swapping one cheap item for one expensive item changes the total by the **difference in price**. In the ticket problem below, replacing all 250 tickets with child tickets would bring in $250 \times 7 = 1{,}750$; each adult ticket adds $12 - 7 = 5$ more; the actual total is 750 more than \$1,750, so there are $750 / 5 = 150$ adult tickets. This "assume all of one kind" method is fast and reliable.

There is also a hidden constraint: **counts are non-negative integers**. Sometimes one equation with two unknowns has only one solution in whole numbers. That matters a great deal in Data Sufficiency (see practice problem 7).

### Number and digit problems

A two-digit number with tens digit $t$ and units digit $u$ has value $10t + u$, not $tu$. Reversing the digits gives $10u + t$. Two facts follow:

- The difference between a number and its reversal is $(10t + u) - (10u + t) = 9(t - u)$, always a multiple of 9.
- The sum is $11(t + u)$, always a multiple of 11.

Digits are integers from 0 to 9, and the leading digit is not 0. These restrictions often pin down the answer.

### "How many more" and other targets

Read the last sentence of the problem twice. Questions such as "how many more", "by how much does $X$ exceed $Y$", "what is the sum of their ages in 5 years", or "how many coins in total" all ask for something other than a single variable. The answer choices almost always include the values of the individual variables, because those are the answers you get when you stop one step too early.

### Checking units

Every term in an equation must have the same units. You can't add litres per minute to litres per hour, or dollars to cents. Converting first and writing units next to each number catches a whole class of mistakes:

$$
18\ \tfrac{\text{L}}{\text{min}} \times 120\ \text{min} = 2{,}160\ \text{L}, \qquad 900\ \tfrac{\text{L}}{\text{h}} \times 2\ \text{h} = 1{,}800\ \text{L}.
$$

The units cancel like algebra. If the units of your answer are wrong (e.g. "litres per hour" when the question asked for hours), the set-up is wrong.

> [!TIP]
> **Plug the answer back into the words, not into your equation.** If your equation is wrong, the answer will satisfy it anyway. Checking against the original sentences ("is Maria really three times as old as her son? In 12 years is she twice as old?") catches translation errors that re-checking the algebra never will.

### Common translation traps

> [!WARNING]
> Wrong answer choices on translation problems are usually built from one of these:
> 1. **Reversed subtraction**: "$x$ less than $y$" written as $x - y$.
> 2. **Percent of the wrong base**: applying "20% of the remainder" to the original total.
> 3. **Missing parentheses**: "twice the sum of $a$ and 3" written as $2a + 3$ instead of $2(a + 3)$.
> 4. **Unshifted ages**: forgetting to add or subtract the years for *every* person.
> 5. **Answering the wrong question**: giving $a$ when asked for $a - c$, or today's age when asked for an age in the future.
> 6. **Mixed units**: minutes with hours, cents with dollars.
> 7. **Digits as a product**: treating the number with digits $t$ and $u$ as $tu$ instead of $10t + u$.

> [!NOTE]
> If you use Claude Code, the `quantome-math` plugin (`/plugin install quantome-math@quantome`) can check your algebra after you have done a problem yourself. Translate first, by hand; that is the skill the exam tests.

## Worked examples

### Example 1 *(Easy)*

Seven less than four times a number is eleven more than the number. What is the number?

(A) $-\tfrac45$ (B) $\tfrac{18}{5}$ (C) 6 (D) 13 (E) 18

**Solution.** Translate phrase by phrase: "four times a number" is $4x$; "seven less than" that is $4x - 7$; "is" is $=$; "eleven more than the number" is $x + 11$.

$$
4x - 7 = x + 11 \quad\Rightarrow\quad 3x = 18 \quad\Rightarrow\quad x = 6.
$$

Check in words: four times 6 is 24, seven less is 17; eleven more than 6 is 17. ✓ The answer is **(C)**.

Every distractor is a translation error. (A) comes from reversing the subtraction, $7 - 4x = x + 11$. (B) comes from writing "eleven more than the number" as $11 - x$. (D) comes from reading "seven less than four times a number" as $4(x - 7)$. (E) is $3x$, an answer given one step too early.

### Example 2 *(Medium)*

Maria is three times as old as her son. In 12 years, she will be twice as old as he will be then. How old is Maria now?

(A) 12 (B) 24 (C) 36 (D) 48 (E) 60

**Solution.** Let the son be $s$ now, so Maria is $3s$. In 12 years they will be $s + 12$ and $3s + 12$:

$$
3s + 12 = 2(s + 12) = 2s + 24 \quad\Rightarrow\quad s = 12.
$$

Maria is $3 \times 12 = 36$. Check: in 12 years she is 48 and he is 24. ✓ The answer is **(C)**.

**Faster: backsolve.** Maria's age must be a multiple of 3. Try (C) 36: son 12; in 12 years, 48 and 24; ratio 2. Done. Choice (A) is the son's age, the "stopped one step early" answer.

### Example 3 *(Medium)*

A theatre sold 250 tickets for one performance. Adult tickets cost \$12 and child tickets cost \$7, and ticket revenue was \$2,500. How many more adult tickets than child tickets were sold?

(A) 25 (B) 50 (C) 75 (D) 100 (E) 150

**Solution.** Let $a$ be the number of adult tickets and $c$ the number of child tickets. The question asks for $a - c$.

$$
a + c = 250, \qquad 12a + 7c = 2500.
$$

Substitute $c = 250 - a$: $12a + 1750 - 7a = 2500$, so $5a = 750$, $a = 150$, $c = 100$, and $a - c = 50$. The answer is **(B)**.

**Faster: assume all of one kind.** If all 250 were child tickets, revenue would be \$1,750. Each adult ticket adds \$5, and we need \$750 more, so there are 150 adult tickets. Choices (D) and (E) are $c$ and $a$, the answers for someone who did not reread the question.

### Example 4 *(Medium)*

The sum of five consecutive even integers is 108 more than the smallest of them. What is the smallest of the five integers?

(A) 18 (B) 20 (C) 22 (D) 24 (E) 26

**Solution.** Use the middle term: the integers are $m-4, m-2, m, m+2, m+4$, with sum $5m$. The smallest is $m - 4$:

$$
5m = (m - 4) + 108 \quad\Rightarrow\quad 4m = 104 \quad\Rightarrow\quad m = 26.
$$

The smallest is $26 - 4 = 22$. Check: $22 + 24 + 26 + 28 + 30 = 130 = 22 + 108$. ✓ The answer is **(C)**. Choice (E) is the middle term.

### Example 5 *(Hard)*

The tens digit of a two-digit positive integer is 3 more than its units digit, and the integer is 7 times the sum of its digits. What is the integer?

(A) 36 (B) 52 (C) 63 (D) 74 (E) 85

**Solution.** Let the units digit be $u$. The tens digit is $u + 3$, so the number is $10(u + 3) + u = 11u + 30$ and the digit sum is $2u + 3$:

$$
11u + 30 = 7(2u + 3) = 14u + 21 \quad\Rightarrow\quad 3u = 9 \quad\Rightarrow\quad u = 3.
$$

The number is $63$. Check: $6 = 3 + 3$, and $7 \times 9 = 63$. ✓ The answer is **(C)**.

**Faster: test the choices.** The tens digit must be 3 more than the units digit, which rules out (A) 36 (the reversal trap). Then the number must be divisible by 7: of 52, 63, 74 and 85, only 63 is. Answer choices are information; use them.

## Practice

**1.** *(Easy)* If 40% of a number is 18 more than 10% of the number, what is the number?

(A) 30 (B) 60 (C) 72 (D) 90 (E) 180

<details>
<summary>Answer</summary>

**(B) 60.** Translate: $0.4x = 0.1x + 18$, so $0.3x = 18$ and $x = 60$. Check: 40% of 60 is 24, 10% of 60 is 6, and $24 = 6 + 18$. ✓

</details>

**2.** *(Easy)* One number is 9 less than twice another number, and the sum of the two numbers is 54. What is the larger number?

(A) 21 (B) 27 (C) 31 (D) 33 (E) 39

<details>
<summary>Answer</summary>

**(D) 33.** Let the other number be $b$; the first is $2b - 9$ ("9 less than twice $b$"). Then $2b - 9 + b = 54$, so $3b = 63$, $b = 21$ and the first number is $33$. The question asks for the larger, 33. Choice (A) is the smaller number.

</details>

**3.** *(Medium)* Six years ago, Ken was 4 times as old as Lea. Four years from now, Ken will be twice as old as Lea. How old is Ken now?

(A) 11 (B) 22 (C) 26 (D) 30 (E) 34

<details>
<summary>Answer</summary>

**(C) 26.** Using one time column per sentence:

$$
k - 6 = 4(l - 6), \qquad k + 4 = 2(l + 4).
$$

From the first, $k = 4l - 18$. Substitute: $4l - 14 = 2l + 8$, so $l = 11$ and $k = 26$. Check: six years ago they were 20 and 5 (ratio 4); in four years they will be 30 and 15 (ratio 2). ✓ Choice (A) is Lea's age.

</details>

**4.** *(Medium)* A jar contains only nickels, dimes and quarters. There are twice as many dimes as nickels and 5 fewer quarters than dimes. If the coins are worth \$6.25 in total, how many quarters are in the jar?

(A) 10 (B) 15 (C) 20 (D) 25 (E) 45

<details>
<summary>Answer</summary>

**(B) 15.** Let $n$ be the number of nickels. Then there are $2n$ dimes and $2n - 5$ quarters. Working in cents:

$$
5n + 10(2n) + 25(2n - 5) = 625 \quad\Rightarrow\quad 75n - 125 = 625 \quad\Rightarrow\quad n = 10.
$$

So 10 nickels, 20 dimes and 15 quarters: $50 + 200 + 375 = 625$ cents. ✓ Choice (E) is the total number of coins; (A) and (C) are the nickels and dimes.

</details>

**5.** *(Medium)* The sum of four consecutive integers is 14 more than three times the smallest of them. What is the largest of the four integers?

(A) 8 (B) 9 (C) 10 (D) 11 (E) 12

<details>
<summary>Answer</summary>

**(D) 11.** The integers are $n, n+1, n+2, n+3$ with sum $4n + 6$. So $4n + 6 = 3n + 14$, giving $n = 8$. The largest is $n + 3 = 11$. Check: $8 + 9 + 10 + 11 = 38 = 3 \times 8 + 14$. ✓ Choice (A) is the smallest.

</details>

**6.** *(Easy)* Pump A moves 18 litres of water per minute, and pump B moves 900 litres per hour. In 2 hours, how many more litres does pump A move than pump B?

(A) 36 (B) 120 (C) 360 (D) 1,800 (E) 2,160

<details>
<summary>Answer</summary>

**(C) 360.** Convert to the same units first. In 2 hours (120 minutes), A moves $18 \times 120 = 2{,}160$ L and B moves $900 \times 2 = 1{,}800$ L. The difference is 360 L. Choices (D) and (E) are the individual amounts.

</details>

**7.** *(Hard, Data Sufficiency)* At a cinema, adult tickets cost \$13 and student tickets cost \$8. How many student tickets did Pat buy?

(1) Pat spent exactly \$100 on tickets.
(2) Pat bought 10 tickets.

(A) Statement (1) ALONE is sufficient, but statement (2) alone is not sufficient.
(B) Statement (2) ALONE is sufficient, but statement (1) alone is not sufficient.
(C) BOTH statements TOGETHER are sufficient, but NEITHER statement ALONE is sufficient.
(D) EACH statement ALONE is sufficient.
(E) Statements (1) and (2) TOGETHER are NOT sufficient.

<details>
<summary>Answer</summary>

**(A).** Statement (1) gives $13a + 8s = 100$, one equation in two unknowns, which *looks* insufficient. But $a$ and $s$ are non-negative integers. Since $8s$ and 100 are both multiples of 4, $13a$ must be a multiple of 4, so $a \in \{0, 4\}$ (since $13 \times 8 > 100$). $a = 0$ gives $8s = 100$, not an integer; $a = 4$ gives $8s = 48$, $s = 6$. So the only possibility is 4 adult and 6 student tickets: sufficient.

Statement (2) alone, $a + s = 10$, allows anything from $s = 0$ to $s = 10$: not sufficient.

The trap answer is (C), from the reflex "two unknowns need two equations". Integer constraints can make one equation enough.

</details>

**8.** *(Medium)* The tens digit of a two-digit number is twice its units digit. When the digits are reversed, the number decreases by 36. What is the sum of the digits?

(A) 6 (B) 9 (C) 10 (D) 12 (E) 15

<details>
<summary>Answer</summary>

**(D) 12.** Let the units digit be $u$; the number is $10(2u) + u = 21u$ and its reversal is $10u + 2u = 12u$. The decrease is $9u = 36$, so $u = 4$, the number is 84, and the digit sum is $8 + 4 = 12$. (This agrees with the general fact: a number minus its reversal is $9(t - u) = 9 \times 4 = 36$.)

</details>

**9.** *(Hard)* The ratio of Amir's age to Beth's age is $5 : 3$. Eight years ago, the ratio of their ages was $3 : 1$. What will be the sum of their ages 5 years from now?

(A) 32 (B) 37 (C) 40 (D) 42 (E) 52

<details>
<summary>Answer</summary>

**(D) 42.** Let the ages now be $5k$ and $3k$. Eight years ago:

$$
\frac{5k - 8}{3k - 8} = 3 \quad\Rightarrow\quad 5k - 8 = 9k - 24 \quad\Rightarrow\quad k = 4.
$$

They are 20 and 12 now (sum 32). In 5 years *each* is 5 years older, so the sum is $32 + 10 = 42$. Choice (A) is today's sum, and (B) adds the 5 years only once.

</details>

**10.** *(Hard, Data Sufficiency)* Is Ann older than Ben?

(1) In 5 years, Ann will be twice as old as Ben was 5 years ago.
(2) The sum of Ann's and Ben's current ages is 45.

(A) Statement (1) ALONE is sufficient, but statement (2) alone is not sufficient.
(B) Statement (2) ALONE is sufficient, but statement (1) alone is not sufficient.
(C) BOTH statements TOGETHER are sufficient, but NEITHER statement ALONE is sufficient.
(D) EACH statement ALONE is sufficient.
(E) Statements (1) and (2) TOGETHER are NOT sufficient.

<details>
<summary>Answer</summary>

**(C).** Statement (1): $a + 5 = 2(b - 5)$, so $a = 2b - 15$. Ann is older exactly when $2b - 15 > b$, that is $b > 15$. If $b = 10$, then $a = 5$ (no); if $b = 20$, then $a = 25$ (yes). Not sufficient.

Statement (2): $a + b = 45$ allows $a = 30, b = 15$ (yes) or $a = 15, b = 30$ (no). Not sufficient.

Together: $2b - 15 + b = 45$, so $b = 20$ and $a = 25$. Ann is older: a definite "yes".

</details>

**11.** *(Hard)* Ana has 30 coins, all dimes and quarters, worth \$5.70 in total. Ben also has 30 dimes and quarters: as many dimes as Ana has quarters, and as many quarters as Ana has dimes. How much more money does Ana have than Ben?

(A) \$0.60 (B) \$0.90 (C) \$1.50 (D) \$1.80 (E) \$2.70

<details>
<summary>Answer</summary>

**(B) \$0.90.** Ana: $d + q = 30$ and $10d + 25q = 570$ cents. If all 30 were dimes she would have 300 cents; each quarter adds 15, and she has 270 more, so $q = 18$ and $d = 12$. Ben has 18 dimes and 12 quarters: $180 + 300 = 480$ cents. The difference is $570 - 480 = 90$ cents.

**Faster.** Swapping one dime for one quarter changes the value by 15 cents. Ana has $q - d = 6$ more quarters than dimes, and Ben has 6 fewer, so the difference is $6 \times 15 = 90$ cents. Choice (E), \$2.70, is $18 \times 15$ cents, from counting every quarter instead of the net difference.

</details>

## Takeaways

- Translate one phrase at a time: "is" is $=$, "of" after a fraction or percent is $\times$, and "$x$ less than $y$" is $y - x$.
- Write down what each variable means, with units, and write the question in symbols before you solve.
- Let the basic or smallest quantity be the variable so the others are multiples of it; use the middle term for evenly spaced lists.
- Age problems: one table, one time column per sentence, and every person's age shifts.
- Count problems have two equations (items and value); "assume all of one kind" solves them fast, and integer constraints can make one equation enough.
- A two-digit number is $10t + u$; a number minus its reversal is a multiple of 9.
- Check your answer against the original words, not your equation, and make sure you answered what was asked.

## Further reading

- GMAC, *GMAT Official Guide* (current edition), the source of real Problem Solving and Data Sufficiency practice questions. Work its word problems after this chapter, paying attention to how often a wrong choice is the value of an intermediate variable.
- The next chapters in this module, [Rates and work](../rates-and-work/) and [Mixtures and interest](../mixtures-and-interest/), apply these translation habits to rate tables and weighted averages.
- For the algebra itself, see [Linear equations](../../algebra/linear-equations/) and, for fast arithmetic, [Estimation and mental math](../../arithmetic/estimation-and-mental-math/).
