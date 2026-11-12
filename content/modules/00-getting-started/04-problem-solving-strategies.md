+++
summary = "Use the core GMAT Quant toolkit (picking numbers, backsolving, estimation, elimination, testing cases, working backwards) and pace 21 questions in 45 minutes."
+++

# Problem-Solving Strategies

Most GMAT Quant questions can be solved two ways: the way a textbook would do it, and a faster way that uses the fact that the test is **multiple choice**. One of the five answers on the screen is correct. The other four were built by someone who predicted the mistakes you are likely to make. A strong test-taker uses both facts.

This chapter is the toolkit you will use in every later chapter of Part I. Each strategy comes with a worked five-choice example, so you can see when it pays off and when it doesn't. None of these methods replaces knowing the maths. They are ways to **apply** the maths with less algebra, fewer careless slips and less time.

> [!NOTE]
> Throughout Part I, boxes labelled "Strategy" give fast methods and boxes labelled "Common trap" describe the mistakes that wrong answer choices are built from. When a strategy box in a later chapter names a method you don't know, come back here.

## Key ideas

### Why shortcuts work on this test

The GMAT is not a test of whether you *can* solve a problem with unlimited time. It tests whether you can choose a good method under time pressure. Three features of the format make shortcuts legitimate:

1. **The answer is on the screen.** You can test answer choices instead of solving from scratch.
2. **The choices are usually spread out.** If they are far apart, a rough estimate is enough to choose.
3. **"Must be true" and "could be true" questions are about every case.** One counterexample eliminates a choice, so a few well-chosen numbers can do the work of a proof.

You still need the textbook method. Some questions are written to defeat a particular shortcut. But for a large share of questions, the shortcut is faster and *less* error-prone, because concrete numbers are easier to check than abstract algebra.

### Picking numbers (smart numbers)

When a question uses variables or unknown totals, and the answer does not depend on the actual size of those unknowns, you can **choose convenient values**, do the arithmetic with them, and match the result.

**Why it works.** If the answer is the same for every valid value of the unknown, it is in particular the same for the value you picked. Percent questions where no starting amount is given, and fraction-of-a-remainder questions, are the classic cases. The answer is a *ratio*, so the starting size cancels.

Choose numbers that make the arithmetic easy:

| Situation | Smart number | Why |
|---|---|---|
| Percent changes, no starting value | 100 | Percents of 100 are just the numbers themselves |
| Fractions of a whole: $\tfrac13$, $\tfrac14$, $\tfrac25$ | the LCM of the denominators (or a multiple of it) | Every step stays an integer |
| Rates "$d$ miles in $h$ hours" | numbers that divide evenly, e.g. $d = 120$, $h = 2$ | Avoids fractions in the rate |
| Variables in the answer choices | small, *different* values that are not 0 or 1 | 0 and 1 make different expressions look equal |

> [!TIP]
> **Picking numbers with variable answer choices.** Pick values, compute the target number, then plug the *same* values into all five choices. Check every choice: if two choices match, pick new numbers and test only those two.

### Backsolving from the answer choices

When the question asks for a single number and the answer choices are numbers in increasing (or decreasing) order, you can **test the choices in the conditions of the problem** instead of setting up and solving an equation.

**Start with (C).** The choices are almost always listed in order. If (C) is too small, the answer must be (D) or (E). If it is too big, the answer must be (A) or (B). One more test then settles it, so you need at most two tests, and often only one.

Backsolving is best when the equation would be awkward to set up (ages, consecutive integers, tickets of two prices). It is poor when the choices are expressions or when each test needs a lot of arithmetic.

### Estimation and ballparking

If the choices are far apart, you do not need the exact value. Round each number to something friendly, compute, and pick the choice in the right range. Round some numbers up and others down so the errors partly cancel. Watch the **order of magnitude**: most estimation questions are really asking "how many zeros?".

### Eliminating unreasonable choices

Before you calculate, ask what the answer *must* look like:

- Is it bigger or smaller than some value in the problem?
- Must it be an integer (people, tickets), positive, or less than a total?
- If two groups are combined, a combined average must lie between the group averages, closer to the bigger group.
- If two machines work together, the joint time is less than the faster machine's time alone.

Every choice you eliminate raises your guessing odds, and sometimes only one choice survives.

### Testing cases

For "must be true", "could be true" and inequality questions, test numbers from **different categories**, because the GMAT hides counterexamples in the cases people forget. The standard checklist:

| Case | Example | Why it breaks rules |
|---|---|---|
| Zero | $0$ | $0^2 = 0$; you cannot divide by it |
| One | $1$ | $1^2 = 1$, so $x^2 > x$ fails |
| Negatives | $-2$, $-\tfrac12$ | Multiplying an inequality by them flips it; $x^2 > 0 > x$ |
| Fractions between 0 and 1 | $\tfrac12$ | Squaring makes them *smaller*: $(\tfrac12)^2 < \tfrac12$ |
| Large numbers | $10$ | Show long-run behaviour |

**Why it works.** "Must be true" means "true in every case". A single counterexample proves a statement is *not* always true. Testing cannot prove a "must be true" statement on its own, but once the other choices are eliminated, the survivor is the answer.

### Work backwards from what is asked

Read the **last sentence first** and write down exactly what you need, such as "$a + b$", not "$a$ and $b$". The GMAT often asks for a combination that you can find without finding each variable: adding or subtracting the given equations, or using an identity like $(x + \tfrac1x)^2 = x^2 + 2 + \tfrac1{x^2}$. Knowing the target before you start tells you which manipulation to try.

> [!WARNING]
> **What wrong choices are built from.** Expect to see the answer to the wrong question (the value of $a$ when $a + b$ was asked), a number from an intermediate step, the result of a common slip (adding percents instead of compounding them, averaging rates instead of combining them), and the right number with the wrong sign. If your answer appears instantly among the choices after a rushed calculation, check that you answered what was asked.

## Worked examples

**Example 1 (picking numbers: percents).** A retailer raises the price of a coat by 25%. A month later it reduces the new price by 20%, and in a clearance sale it takes a further 10% off. The final price is what percent of the original price?

(A) 85% (B) 90% (C) 95% (D) 100% (E) 105%

**Solution.** No price is given, so pick 100. After the rise: 125. After 20% off: $125 \times 0.8 = 100$. After a further 10% off: 90. So the final price is 90% of the original. **Answer: (B).**

The textbook method multiplies the factors, $1.25 \times 0.8 \times 0.9 = 0.9$. With 100, the arithmetic is the same but every intermediate number means something, which makes slips easier to catch. The trap answer is (C), from adding the percent changes: $+25 - 20 - 10 = -5$, so "95%". Percent changes compound; they don't add.

**Example 2 (picking numbers: fractions).** A water tank is full. On Monday $\tfrac13$ of the water is used. On Tuesday $\tfrac14$ of the remaining water is used, and on Wednesday $\tfrac12$ of what is left after Tuesday is used. What fraction of the original water remains?

(A) $\tfrac18$ (B) $\tfrac16$ (C) $\tfrac14$ (D) $\tfrac13$ (E) $\tfrac{5}{12}$

**Solution.** The denominators are 3, 4 and 2, with LCM 12. Using 12 would give a half-unit at the last step, so use 24, a multiple of it. Monday uses 8, leaving 16. Tuesday uses $\tfrac14$ of 16, which is 4, leaving 12. Wednesday uses 6, leaving 6. The fraction left is $\tfrac{6}{24} = \tfrac14$. **Answer: (C).**

> [!WARNING]
> "$\tfrac14$ of the **remaining** water" is not $\tfrac14$ of the tank. Subtracting $\tfrac13 + \tfrac14 + \tfrac12$ from 1 gives a negative number, a sign that the fractions refer to different wholes.

**Example 3 (backsolving).** A theatre sold 40 tickets: adult tickets at \$12 each and child tickets at \$7 each. Ticket revenue was \$400. How many adult tickets were sold?

(A) 18 (B) 21 (C) 22 (D) 24 (E) 26

**Solution (backsolving).** Start with (C): 22 adult and 18 child tickets bring in $22 \times 12 + 18 \times 7 = 264 + 126 = 390$. That is \$10 too little, so there must be more adult tickets: eliminate (A), (B) and (C). Each extra adult ticket (replacing a child ticket) adds $12 - 7 = 5$ dollars, so we need 2 more: 24 adult tickets. Check (D): $24 \times 12 + 16 \times 7 = 288 + 112 = 400$. **Answer: (D).**

**Solution (algebra).** $12a + 7(40 - a) = 400$, so $5a + 280 = 400$ and $a = 24$. Here algebra is also quick. Backsolving shines when the equation is harder to write than to check.

**Example 4 (estimation).** Which of the following is closest to $\dfrac{0.049 \times 812}{1.97 \times 0.101}$?

(A) 0.2 (B) 2 (C) 20 (D) 200 (E) 2,000

**Solution.** Round: $0.049 \approx 0.05$, $812 \approx 800$, $1.97 \approx 2$, $0.101 \approx 0.1$. The numerator is about $0.05 \times 800 = 40$ and the denominator about $2 \times 0.1 = 0.2$. So the value is about $40 / 0.2 = 200$. **Answer: (D).** The choices differ by factors of 10, so this estimate is far more precise than needed. (The exact value is about 199.97.)

**Example 5 (eliminating unreasonable choices).** Pipe P can fill a tank in 8 hours, and pipe Q can fill it in 12 hours. Working together at these rates, how many hours do they take to fill the empty tank?

(A) 4 (B) 4.8 (C) 6 (D) 10 (E) 20

**Solution (elimination).** Two pipes as fast as P would take $8 / 2 = 4$ hours. Two pipes as slow as Q would take $12/2 = 6$ hours. P and Q together are faster than two Qs and slower than two Ps, so the time is strictly between 4 and 6. Only (B) survives. **Answer: (B).**

**Solution (rates).** Rates add: $\tfrac18 + \tfrac1{12} = \tfrac{3}{24} + \tfrac{2}{24} = \tfrac{5}{24}$ tank per hour, so the time is $\tfrac{24}{5} = 4.8$ hours. Note where the distractors come from: (D) is the average of 8 and 12, (E) is their sum, and (C) is the two-slow-pipes bound.

**Example 6 (testing cases).** If $x^3 < x$, which of the following must be true?

I. $x < 1$  II. $x^2 < 1$  III. $x < 0$

(A) I only (B) II only (C) III only (D) I and II only (E) I, II and III

**Solution (testing cases).** First find numbers that satisfy the condition. $x = \tfrac12$ works: $\tfrac18 < \tfrac12$. It makes III false, so eliminate (C) and (E). $x = -2$ also works: $-8 < -2$. It makes II false ($4 > 1$), so eliminate (B) and (D). Only (A) remains. **Answer: (A).**

**Why I must be true.** $x^3 < x$ means $x(x - 1)(x + 1) < 0$. A sign chart gives $x < -1$ or $0 < x < 1$. In both pieces $x < 1$.

> [!TIP]
> On "must be true" questions, first find numbers that **satisfy the condition**, choosing from different categories (negative, fraction, large). Then use each number to knock out statements. Testing $x = 2$ here would be useless, since it does not satisfy $x^3 < x$.

**Example 7 (work backwards from what is asked).** If $2a + 3b = 11$ and $3a + 2b = 14$, what is the value of $a + b$?

(A) 3 (B) 4 (C) 5 (D) 6 (E) 7

**Solution.** The target is $a + b$, not $a$ and $b$. The coefficients are symmetric, so add the equations: $5a + 5b = 25$, so $a + b = 5$. **Answer: (C).** Solving fully ($a = 4$, $b = 1$) gives the same answer in three times the work, and (B) is waiting for anyone who reports $a$ by mistake, (A) for anyone who subtracts the equations instead ($a - b = 3$).

## Timing strategy

The Quantitative Reasoning section has 21 questions in 45 minutes, about **2 minutes 8 seconds per question**. You cannot spend that evenly: some questions take 60 seconds and some take 3 minutes. What matters is the running total.

### Pacing checkpoints

Use the on-screen clock at two checkpoints:

| After question | Time remaining (about) | If you are behind |
|---|---|---|
| 7 | 30 minutes | Speed up: guess sooner on the next hard question |
| 14 | 15 minutes | Be strict: 2 minutes per question from here |
| 21 | 0–3 minutes | Use spare time for review (below) |

Being 2–3 minutes behind at question 7 is recoverable. Being 6 minutes behind is not, unless you make a deliberate guess or two now rather than rushing the last five questions.

### When to guess

Unanswered questions at the end of the section cost a lot, and a rushed run of the last few questions usually costs more than one early, deliberate guess. Use this rule:

1. After about **30 seconds**, you should know what kind of problem it is and have a plan. If not, read it once more.
2. After about **2 minutes**, if you are not close to an answer, stop. Eliminate whatever you can with the tools above (sign, size, integer, units digit) and guess among the rest.
3. Never let one question take more than about **3 minutes**. The time is better spent on two questions you can answer.

> [!TIP]
> Guessing well is a skill. Before you guess, spend 15 seconds eliminating. Removing two choices raises a random guess from a 20% chance to 33%.

> [!WARNING]
> The worst timing pattern is "sunk cost": you have already spent 3 minutes, so you spend 2 more to justify them. The first 3 minutes are gone either way. Decide based on the time you still need, not the time you have already spent.

### The review-and-edit feature

On the GMAT Focus Edition you can **bookmark** any question while you work. If time remains when you reach the end of a section, a review screen lists all questions and your bookmarks, and you can revisit questions and **change up to three answers in that section**. Review uses the section's own 45 minutes. It does not add time.

Use it well:

- **Bookmark guesses**, especially questions where you eliminated down to two choices. These are the best candidates for a second look.
- Don't plan to come back. Answer every question as if there were no review. Review is a bonus for spare minutes, not a strategy for skipping hard questions.
- Change an answer only for a **specific reason** (a calculation error you can point to, a misread condition), not a vague feeling. Your first careful answer is usually better than a nervous second guess.

> [!NOTE]
> Always confirm the current rules (number of edits, section order, timing) on the official GMAC website before test day. See [The GMAT Quant section](../../getting-started/the-gmat-quant-section/) for the format.

## Choosing a strategy

The same question can often be solved several ways. Ask, in this order:

1. **Do I see the direct method, and is it quick?** If yes, use it. Strategies are for when it is slow or unclear.
2. **Are there variables in the choices, or an unknown total?** Pick numbers.
3. **Are the choices numbers, in order, and easy to check?** Backsolve, starting with (C).
4. **Are the choices far apart?** Estimate.
5. **Is it "must be true" or "could be true"?** Test cases from different categories.
6. **Does it ask for a combination?** Work backwards from what is asked.

> [!NOTE]
> Readers using Claude Code can check their working with the `quantome-math` plugin (`/plugin install quantome-math@quantome`). Use it after you have solved a problem yourself, never instead.

## Practice

**1.** *(Easy)* The price of a bicycle falls by 20% and then rises by 30%. Overall, the price has changed by:

(A) a 4% decrease (B) no change (C) a 4% increase (D) a 6% increase (E) a 10% increase

<details>
<summary>Answer</summary>

**(C).** Pick 100. After the fall: 80. After a 30% rise: $80 \times 1.3 = 104$. That is a 4% increase. (E) is the trap answer from adding $-20 + 30$. The 30% rise is applied to a smaller base, so it adds only 24, not 30.

</details>

**2.** *(Easy)* The sum of three consecutive odd integers is 15 more than twice the largest of them. What is the smallest of the three integers?

(A) 11 (B) 13 (C) 15 (D) 17 (E) 19

<details>
<summary>Answer</summary>

**(D).** Backsolve from (C): $15 + 17 + 19 = 51$, while $2 \times 19 + 15 = 53$. The sum is 2 too small. Moving up by 2 adds 6 to the sum but only 4 to the right-hand side, so the gap closes by 2: try 17. Then $17 + 19 + 21 = 57$ and $2 \times 21 + 15 = 57$. ✓

Algebra: $n + (n + 2) + (n + 4) = 2(n + 4) + 15$ gives $3n + 6 = 2n + 23$, so $n = 17$.

</details>

**3.** *(Medium)* Ana spends $\tfrac25$ of her monthly income on rent, $\tfrac14$ of the remainder on food, and $\tfrac13$ of what is then left on transport. What fraction of her income is left after these three expenses?

(A) $\tfrac16$ (B) $\tfrac{3}{10}$ (C) $\tfrac13$ (D) $\tfrac25$ (E) $\tfrac12$

<details>
<summary>Answer</summary>

**(B).** The denominators are 5, 4 and 3, so pick an income of 60. Rent: 24, leaving 36. Food: $\tfrac14 \times 36 = 9$, leaving 27. Transport: $\tfrac13 \times 27 = 9$, leaving 18. The fraction left is $\tfrac{18}{60} = \tfrac{3}{10}$.

As a check: $\tfrac35 \times \tfrac34 \times \tfrac23 = \tfrac{18}{60} = \tfrac3{10}$.

</details>

**4.** *(Medium)* A car travels $d$ miles in $h$ hours. At this rate, how many **minutes** will it take to travel $m$ miles?

(A) $\dfrac{60mh}{d}$ (B) $\dfrac{mh}{60d}$ (C) $\dfrac{60md}{h}$ (D) $\dfrac{60d}{mh}$ (E) $\dfrac{md}{60h}$

<details>
<summary>Answer</summary>

**(A).** Pick $d = 120$, $h = 2$, $m = 30$. The speed is 60 mph, so 30 miles take half an hour, which is **30 minutes**. Now test the choices: (A) $\tfrac{60 \times 30 \times 2}{120} = 30$ ✓. (B) $\tfrac{60}{7200}$, no. (C) $\tfrac{60 \times 30 \times 120}{2} = 108{,}000$, no. (D) $\tfrac{7200}{60} = 120$, no. (E) $\tfrac{30 \times 120}{60 \times 2} = 30$ as well.

Two choices match, so pick new numbers and test only (A) and (E). Try $d = 30$, $h = 3$, $m = 15$: the speed is 10 mph, so 15 miles take 1.5 hours = 90 minutes. (A) $\tfrac{60 \times 15 \times 3}{30} = 90$ ✓. (E) $\tfrac{15 \times 30}{60 \times 3} = 2.5$, no. The answer is (A).

Algebra: time in hours $= \tfrac{m}{d/h} = \tfrac{mh}{d}$; multiply by 60 for minutes. This problem shows why you must check **all** the choices after picking numbers: the first pick was unlucky because speed 60 mph makes "minutes" and "miles" numerically equal.

</details>

**5.** *(Medium)* Which of the following is closest to $\sqrt{0.0098 \times 4{,}050}$?

(A) 0.2 (B) 0.6 (C) 2 (D) 6 (E) 20

<details>
<summary>Answer</summary>

**(D).** $0.0098 \approx 0.01$ and $4{,}050 \approx 4{,}000$, so the product is about $40$, and $\sqrt{40}$ is between 6 and 7 (since $6^2 = 36$, $7^2 = 49$). The closest choice is 6. (The exact value is 6.3.) (B) is the trap from misplacing a decimal: $\sqrt{0.4} \approx 0.63$.

</details>

**6.** *(Medium)* If $ab < 0$ and $a < b$, which of the following must be true?

I. $a < 0$  II. $b^2 > a^2$  III. $\dfrac{a}{b} < 0$

(A) I only (B) III only (C) I and III only (D) II and III only (E) I, II and III

<details>
<summary>Answer</summary>

**(C).** $ab < 0$ means $a$ and $b$ have opposite signs. With $a < b$, the negative one is $a$: so $a < 0 < b$. I is true. III is true, because a negative divided by a positive is negative. For II, test $a = -5$, $b = 1$: $1 > 25$ is false. So II need not be true.

</details>

**7.** *(Medium)* A class of 30 students has an average test score of 72. A second class of 20 students has an average score of 82. What is the average score of all 50 students?

(A) 74 (B) 76 (C) 77 (D) 78 (E) 80

<details>
<summary>Answer</summary>

**(B).** Eliminate first: the combined average lies between 72 and 82, and it is closer to 72, because the 72-class is bigger. The midpoint is 77, so (C), (D) and (E) are out.

Exact: $\dfrac{30 \times 72 + 20 \times 82}{50} = \dfrac{2160 + 1640}{50} = \dfrac{3800}{50} = 76$.

Faster: the weights are $30 : 20 = 3 : 2$, so the average sits $\tfrac25$ of the way from 72 to 82: $72 + \tfrac25 \times 10 = 76$.

</details>

**8.** *(Medium)* If $x + \dfrac1x = 5$, what is the value of $x^2 + \dfrac{1}{x^2}$?

(A) 23 (B) 24 (C) 25 (D) 27 (E) 125

<details>
<summary>Answer</summary>

**(A).** Work backwards from what is asked: square the given expression. $\left(x + \tfrac1x\right)^2 = x^2 + 2 \cdot x \cdot \tfrac1x + \tfrac1{x^2} = x^2 + 2 + \tfrac1{x^2}$. So $25 = x^2 + \tfrac1{x^2} + 2$, and $x^2 + \tfrac1{x^2} = 23$. (C) is the trap from forgetting the middle term. Solving for $x$ itself, $x = \tfrac{5 \pm \sqrt{21}}{2}$, is possible but slow.

</details>

**9.** *(Hard)* If $x \ne 0$ and $\dfrac{x}{|x|} < x$, which of the following must be true?

(A) $x > 1$ (B) $x > -1$ (C) $|x| < 1$ (D) $x^2 > 1$ (E) $x < 0$

<details>
<summary>Answer</summary>

**(B).** $\tfrac{x}{|x|}$ is $1$ if $x > 0$ and $-1$ if $x < 0$.

- If $x > 0$: the condition is $1 < x$, so $x > 1$.
- If $x < 0$: the condition is $-1 < x$, so $-1 < x < 0$.

So $x$ is in $(-1, 0)$ or $(1, \infty)$. Test cases: $x = -\tfrac12$ satisfies the condition and kills (A) and (D). $x = 2$ satisfies it and kills (C) and (E). In both pieces, $x > -1$.

</details>

**10.** *(Hard)* If $a$, $b$ and $c$ are consecutive positive even integers with $a < b < c$, which of the following must be divisible by 48?

(A) $a + b + c$ (B) $ab$ (C) $c^2 - a^2$ (D) $a^2 + b^2 + c^2$ (E) $abc$

<details>
<summary>Answer</summary>

**(E).** Test the smallest case: $2, 4, 6$. (A) $12$, (B) $8$, (C) $36 - 4 = 32$, (D) $4 + 16 + 36 = 56$, (E) $48$. Only (E) is divisible by 48, so the others are eliminated by this one case.

Why (E) always works: write $a = 2k$, $b = 2k + 2$, $c = 2k + 4$. Then $abc = 8 \cdot k(k + 1)(k + 2)$. The product of three consecutive integers is divisible by $2$ and by $3$, so by $6$. So $abc$ is divisible by $8 \times 6 = 48$.

</details>

**11.** *(Hard)* Working alone, Ravi takes 5 hours longer than Bea to paint a fence. Working together, they paint it in 6 hours. How many hours would Bea take alone?

(A) 6 (B) 8 (C) 10 (D) 12 (E) 15

<details>
<summary>Answer</summary>

**(C).** Eliminate first: together they take 6 hours, so Bea alone must take *more* than 6. Eliminate (A).

Backsolve from (C): Bea takes 10 hours and Ravi 15. Together: $\tfrac1{10} + \tfrac1{15} = \tfrac{3}{30} + \tfrac{2}{30} = \tfrac16$ fence per hour, so 6 hours. ✓

Algebra: $\tfrac1b + \tfrac1{b+5} = \tfrac16$ gives $6(2b + 5) = b(b + 5)$, so $b^2 - 7b - 30 = 0$, $(b - 10)(b + 3) = 0$, and $b = 10$. Backsolving avoids the quadratic.

</details>

**12.** *(Hard, Data Sufficiency)* What is the value of $2a + 3b$?

(1) $4a + 6b = 18$
(2) $b = 3 - \tfrac23 a$

(A) Statement (1) ALONE is sufficient, but statement (2) alone is not sufficient.
(B) Statement (2) ALONE is sufficient, but statement (1) alone is not sufficient.
(C) BOTH statements TOGETHER are sufficient, but NEITHER statement ALONE is sufficient.
(D) EACH statement ALONE is sufficient.
(E) Statements (1) and (2) TOGETHER are NOT sufficient.

<details>
<summary>Answer</summary>

**(D).** Work backwards from what is asked: the target is the combination $2a + 3b$, not $a$ and $b$.

(1): divide by 2: $2a + 3b = 9$. Sufficient.

(2): multiply by 3: $3b = 9 - 2a$, so $2a + 3b = 9$. Sufficient.

Each statement is one equation in two unknowns, so neither gives $a$ or $b$, but each fixes the expression asked for. Data Sufficiency is covered in [The Data Sufficiency method](../../data-sufficiency/the-data-sufficiency-method/).

</details>

## Takeaways

- The answer choices are information. Use them to backsolve, to eliminate and to check the size of your answer.
- Pick numbers when the answer does not depend on the size of an unknown: 100 for percents, the LCM for fractions, and small distinct values (not 0 or 1) for variables. Test all five choices.
- Backsolve from (C) when the choices are ordered numbers. The result tells you which direction to go.
- Estimate when the choices are far apart, and always check the order of magnitude.
- For "must be true", find numbers that satisfy the condition from different categories: 0, 1, negatives, fractions, large numbers.
- Read the question's target first. Many questions ask for a combination you can get without solving for each variable.
- Pace with checkpoints: about 30 minutes left after question 7, and 15 after question 14. Guess deliberately after about 2 minutes without progress, and bookmark guesses for review.

## Further reading

- GMAC, *GMAT Official Guide* (current edition) and the official GMAT Focus practice exams: the best source of real questions to practise these strategies on under timed conditions.
- The official GMAC website (mba.com) for the current section format, timing and review-and-edit rules.
- George Pólya, *How to Solve It* (Princeton University Press, 1945): the classic account of general problem-solving heuristics such as working backwards and testing special cases.
