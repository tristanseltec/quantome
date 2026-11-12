+++
summary = "Reason quickly about integers, signs, odd and even, consecutive integers, zero and one, and distance on the number line."
+++

# Number Properties

Many GMAT questions look like algebra but are really about **what kind of number** something is. Is it positive or negative? Odd or even? Could it be zero? If you can answer those questions without solving anything, you can often eliminate four answer choices in seconds. This chapter builds those reflexes, and proves each rule so that you can rebuild it under pressure instead of memorising a table.

Divisibility, primes and factor counting now have their own chapter, [Divisibility, primes and factors](../../arithmetic/divisibility-primes-and-factors/). Remainders and units digits are in [Remainders and units digits](../../arithmetic/remainders-and-units-digits/).

## Key ideas

### The integers and the number line

The **integers** are $\dots, -3, -2, -1, 0, 1, 2, 3, \dots$. They are the whole numbers together with their negatives. Picture them as equally spaced marks on a horizontal line, with negatives to the left of $0$ and positives to the right. Every real number, such as $-2.5$, $\tfrac13$ or $\sqrt2$, sits somewhere on the same line.

Three facts about the number line settle many questions:

- **Order.** $a < b$ means $a$ is to the left of $b$. So $-10 < -2$, even though 10 is "bigger" than 2. Among negatives, the one with the larger size is the smaller number.
- **Counting integers in a range.** The number of integers from $a$ to $b$ inclusive is $b - a + 1$. From 14 to 37 there are $37 - 14 + 1 = 24$. The "+1" counts both endpoints: think of fence posts, not fence panels.
- **Distance.** The distance between $a$ and $b$ is $\vert a - b\vert$. From $-4$ to $9$ is $\vert -4 - 9\vert = 13$ units.

> [!WARNING]
> "Integer" does **not** mean "positive integer". Unless a question says *positive*, test $0$ and negative values. Also, "number" without "integer" allows fractions such as $\tfrac12$: a value between 0 and 1 behaves very differently from an integer (its square is *smaller* than itself).

### Sign rules, and why they hold

The rules for multiplying signs are not arbitrary. Multiplying by $-1$ reflects a number to the other side of $0$, so each negative factor flips the sign once:

| Product or quotient | Sign |
|---|---|
| positive × positive | positive |
| positive × negative | negative |
| negative × negative | positive (two flips) |
| a product with $k$ negative factors | positive if $k$ is even, negative if $k$ is odd |

Division follows the same rules, because $a \div b = a \times \tfrac1b$ and $\tfrac1b$ has the same sign as $b$.

Useful consequences:

- An **even power** is never negative: $x^2 \ge 0$, $x^4 \ge 0$, with equality only at $x = 0$.
- An **odd power keeps the sign**: $x^3$ is negative exactly when $x$ is negative.
- If $xy > 0$, then $x$ and $y$ have the **same** sign. If $xy < 0$, they have **opposite** signs.
- If $x^2 y > 0$, then $y > 0$ (and $x \ne 0$), because $x^2$ is positive. The even power hides the sign of $x$.

Addition has no such clean rule: a positive plus a negative can be either sign. That is why "which must be true" questions often hinge on a sum.

> [!TIP]
> For sign questions, make a tiny table of the possible sign patterns rather than picking one set of numbers. If $xy < 0$, either $x > 0 > y$ or $x < 0 < y$. Check every answer choice against **both** patterns. A statement that "must be true" survives every pattern.

### Zero and one

These two numbers break more GMAT "rules" than any others, so learn their properties explicitly.

**Zero**

- $0$ is an **integer** and it is **even** (it is $2 \times 0$).
- $0$ is **neither positive nor negative**. "Non-negative" means $\ge 0$ and includes zero.
- $0$ is a **multiple of every integer** ($0 = n \times 0$), but $0$ is a factor of nothing except itself. Division by zero is undefined.
- $0 \times$ anything $= 0$. So if a product is zero, at least one factor is zero.
- $0^2 = 0$, so the claim "$x^2 > x$" fails at $0$ (and for $0 < x < 1$).

**One**

- $1$ is a factor of every integer, and $1$ is **not prime** (a prime needs exactly two distinct positive factors).
- $1^n = 1$ for every $n$, so in exponent questions $x = 1$ makes many different expressions equal.
- The numbers equal to their own square are exactly $0$ and $1$. The numbers equal to their own cube are $-1$, $0$ and $1$.

> [!TIP]
> When a "must be true" question gives you an integer variable, the fastest counterexamples are almost always $0$, $1$, $-1$ and a fraction like $\tfrac12$ (if fractions are allowed). Try them first.

### Odd and even, proved by parity

An integer is **even** if it can be written $2k$ for some integer $k$, and **odd** if it can be written $2k + 1$. Every integer is exactly one of the two. Whether a number is odd or even is called its **parity**.

Every parity rule follows from these two forms:

- $\text{even} + \text{even} = 2a + 2b = 2(a+b)$, which is even.
- $\text{odd} + \text{odd} = (2a+1) + (2b+1) = 2(a + b + 1)$, which is even.
- $\text{even} + \text{odd} = 2a + 2b + 1 = 2(a+b) + 1$, which is odd.
- $\text{even} \times \text{anything} = 2a \cdot m = 2(am)$, which is even.
- $\text{odd} \times \text{odd} = (2a+1)(2b+1) = 4ab + 2a + 2b + 1 = 2(2ab + a + b) + 1$, which is odd.

Subtraction behaves exactly like addition, because $-m$ has the same parity as $m$.

| Operation | Result |
|---|---|
| even ± even, odd ± odd | even |
| even ± odd | odd |
| even × any integer | even |
| odd × odd | odd |
| $n^k$ for a positive integer $k$ | same parity as $n$ |

Three deeper consequences come up again and again:

1. **A sum is odd exactly when it contains an odd number of odd terms.** Even terms don't matter, and odd terms cancel in pairs.
2. **A product is odd only if every factor is odd.** One even factor makes the whole product even.
3. **$a + b$ and $a - b$ always have the same parity**, because they differ by $2b$. Similarly, $a^2 - b^2 = (a+b)(a-b)$ is odd exactly when $a$ and $b$ have opposite parity.

A quotient has no parity rule: $\tfrac{12}{4} = 3$ is odd, $\tfrac{12}{6} = 2$ is even, and $\tfrac{12}{8}$ is not an integer at all. Only reason about the parity of a quotient after you know it is an integer.

> [!IMPORTANT]
> The product of two consecutive integers, $n(n+1)$, is **always even**, because one of the two is even. The same reasoning shows $n(n+3)$ is always even ($n$ and $n+3$ have opposite parity), while $n(n+2)$ has the same parity as $n$.

### Consecutive integers

**Consecutive integers** follow each other with step 1: $n, n+1, n+2, \dots$. **Consecutive even** or **consecutive odd** integers step by 2. All of these are **evenly spaced** sets, and evenly spaced sets have one beautiful property.

**The mean equals the median equals the average of the first and last terms.** Pair the first term with the last, the second with the second-last, and so on. Each pair has the same sum, so

$$
\text{sum} = (\text{number of terms}) \times \frac{\text{first} + \text{last}}{2}.
$$

For the integers 1 to 100: $100 \times \tfrac{1 + 100}{2} = 5050$.

> [!IMPORTANT]
> **Sum of an evenly spaced list** $= n \times \text{mean}$, with mean $= \dfrac{\text{first} + \text{last}}{2}$ and, for step size $s$, $n = \dfrac{\text{last} - \text{first}}{s} + 1$.

**When is the sum of $k$ consecutive integers divisible by $k$?** The sum equals $k \times \text{mean}$. If $k$ is odd, the mean is the middle term, an integer, so the sum is a multiple of $k$. If $k$ is even, the mean is halfway between the two middle terms, a number ending in $.5$. Then the sum is $\tfrac{k}{2} \times (\text{an odd number})$, which is **never** a multiple of $k$. For example, $4 + 5 + 6 + 7 = 22$, not a multiple of 4.

**Products of consecutive integers.** Among any $k$ consecutive integers, one is a multiple of $k$, one of every two is even, one of every three is a multiple of 3, and so on. In fact a stronger result holds:

> [!IMPORTANT]
> The product of any $k$ consecutive integers is divisible by $k! = 1 \times 2 \times \cdots \times k$.
>
> - 2 consecutive: divisible by $2! = 2$.
> - 3 consecutive: divisible by $3! = 6$.
> - 4 consecutive: divisible by $4! = 24$.

**Why $k!$ and not just $k$?** For positive integers, $\dfrac{n(n+1)\cdots(n+k-1)}{k!}$ is the number of ways to choose $k$ items from $n + k - 1$ items, which you will meet in [Counting and probability](../../statistics-and-counting/counting-and-probability/). A count of choices is always a whole number, so the division leaves no remainder. If one of the integers is zero the product is $0$, which is divisible by everything, and a run of negative integers is just $\pm$ a run of positive ones.

For four consecutive integers, you can also see it directly. Two of them are even, and one of those two is a multiple of 4, which gives $2 \times 4 = 8$. One of them is a multiple of 3. So the product is a multiple of $8 \times 3 = 24$.

**Consecutive even integers** carry an extra factor of 2 each. Three consecutive even integers are $2m, 2m+2, 2m+4 = 2^3 \cdot m(m+1)(m+2)$, a multiple of $8 \times 6 = 48$.

> [!TIP]
> To test a "must be divisible by" claim, plug in the **smallest** allowed case. For $n(n+1)(n+2)(n+3)$ with $n \ge 1$, the smallest product is $1 \cdot 2 \cdot 3 \cdot 4 = 24$. Anything that must divide every such product must divide 24, which instantly kills choices like 48 or 18.

### Absolute value basics

The **absolute value** $\vert x\vert$ is the distance from $x$ to $0$ on the number line. Distance is never negative, so $\vert x\vert \ge 0$.

- $\vert x\vert = x$ when $x \ge 0$, and $\vert x\vert = -x$ when $x < 0$. (For negative $x$, $-x$ is positive: $\vert -6\vert = -(-6) = 6$.)
- $\vert -x\vert = \vert x\vert$ and $\vert xy\vert = \vert x\vert\,\vert y\vert$.
- $\sqrt{x^2} = \vert x\vert$, not $x$. For example, $\sqrt{(-5)^2} = 5$.
- $\vert a - b\vert$ is the distance between $a$ and $b$. So $\vert x - 3\vert = 4$ asks "which points are 4 units from 3?", giving $x = 7$ or $x = -1$.

Equations and inequalities with absolute values are developed in [Inequalities and absolute value](../../algebra/inequalities-and-absolute-value/).

> [!WARNING]
> $\vert a + b\vert$ is **not** always $\vert a\vert + \vert b\vert$. It is equal only when $a$ and $b$ have the same sign (or one is zero). Otherwise $\vert a + b\vert < \vert a\vert + \vert b\vert$. Answer choices often assume the equality.

### Common traps in number-property questions

> [!WARNING]
> Wrong answer choices in this topic are built from a few predictable mistakes:
> - testing only positive integers, and forgetting $0$, negatives and fractions;
> - assuming that $x^2 > 0$ (false at $x = 0$) or that $x^2 > x$ (false for $0 \le x \le 1$);
> - treating "could be true" as "must be true" because one example worked;
> - claiming parity for a quotient, or for a sum when the number of odd terms is unknown;
> - forgetting the "+1" when counting integers in an inclusive range;
> - assuming the sum of $k$ consecutive integers is always a multiple of $k$ (false when $k$ is even).

## Worked examples

**Example 1** *(Easy)*. If $xy < 0$ and $yz > 0$, which of the following must be true?

(A) $xz > 0$ (B) $xz < 0$ (C) $x < 0$ (D) $y > 0$ (E) $x + z = 0$

**Solution.** $xy < 0$ means $x$ and $y$ have opposite signs. $yz > 0$ means $y$ and $z$ have the same sign. So $z$ has the same sign as $y$, which is the opposite of $x$'s sign. Therefore $x$ and $z$ have opposite signs, and $xz < 0$. **Answer: (B).**

Choices (C) and (D) could be true, but the pattern $x > 0$, $y < 0$, $z < 0$ also satisfies both conditions, so neither must be true. Choice (E) is a single coincidence ($x = 1$, $z = -1$), not a rule.

**Example 2** *(Medium)*. If $m$ and $n$ are integers and $3m + 5n$ is even, which of the following must be true?

(A) $m$ is even (B) $n$ is even (C) $m + n$ is even (D) $mn$ is even (E) $m - n$ is odd

**Solution.** Multiplying by an odd number does not change parity, so $3m$ has the parity of $m$ and $5n$ has the parity of $n$. The sum $3m + 5n$ is even exactly when $m$ and $n$ have the **same** parity. Then $m + n$ is even. **Answer: (C).**

**Fast method: test cases.** $m = n = 1$ gives $3 + 5 = 8$, even. This kills (A), (B) and (D), since $m$, $n$ and $mn$ are all odd. It also kills (E), since $m - n = 0$ is even. Only (C) survives.

**Example 3** *(Medium)*. The sum of seven consecutive integers is 189. What is the largest of the seven integers?

(A) 27 (B) 29 (C) 30 (D) 33 (E) 36

**Solution.** Seven is odd, so the middle (fourth) integer is the mean: $189 \div 7 = 27$. The integers are $24, 25, \dots, 30$, and the largest is $27 + 3 = 30$. **Answer: (C).**

The trap is (A): 27 is the middle term, not the largest. Choice (D) comes from adding 6 to the mean instead of 3.

**Example 4** *(Hard)*. If $n$ is an odd integer greater than 1, what is the greatest integer that must divide $(n-1)(n+1)(n+3)$?

(A) 8 (B) 16 (C) 24 (D) 48 (E) 96

**Solution.** Since $n$ is odd, $n - 1$, $n + 1$ and $n + 3$ are three **consecutive even** integers. Write $n - 1 = 2m$. Then

$$
(n-1)(n+1)(n+3) = 2m \cdot (2m+2) \cdot (2m+4) = 8\, m(m+1)(m+2).
$$

The product $m(m+1)(m+2)$ of three consecutive integers is divisible by $3! = 6$, so the whole expression is divisible by $8 \times 6 = 48$.

Is 48 the *greatest* such divisor? Try the smallest case, $n = 3$: $2 \times 4 \times 6 = 48$. Any number that must divide every value must divide 48, so nothing larger works. **Answer: (D).**

**Fast method.** Compute the expression for $n = 3$ (48) and $n = 5$ ($4 \times 6 \times 8 = 192$). The answer must divide 48, which eliminates (E), and the largest remaining choice that divides both values is 48.

## Practice

<details>
<summary>Data Sufficiency answer choices (the same on every DS question)</summary>

- **(A)** Statement (1) ALONE is sufficient, but statement (2) alone is not sufficient.
- **(B)** Statement (2) ALONE is sufficient, but statement (1) alone is not sufficient.
- **(C)** BOTH statements TOGETHER are sufficient, but NEITHER statement ALONE is sufficient.
- **(D)** EACH statement ALONE is sufficient.
- **(E)** Statements (1) and (2) TOGETHER are NOT sufficient.

</details>

**1.** *(Easy)* If $x$ is negative, which of the following must be positive?

(A) $x^3$ (B) $-x^2$ (C) $x^2 - x$ (D) $x + 1$ (E) $2x$

<details>
<summary>Answer</summary>

**(C).** For negative $x$, $x^2$ is positive and $-x$ is positive, so $x^2 - x$ is a sum of two positives. (A) and (E) are negative, (B) is negative, and (D) is negative for $x = -2$ but positive for $x = -\tfrac12$.

</details>

**2.** *(Easy)* How many integers lie strictly between $-3.5$ and $4.2$?

(A) 6 (B) 7 (C) 8 (D) 9 (E) 10

<details>
<summary>Answer</summary>

**(C).** The integers are $-3, -2, \dots, 4$. Count them with "last − first + 1": $4 - (-3) + 1 = 8$.

</details>

**3.** *(Easy)* If $p$ is an odd integer and $q$ is an even integer, which of the following must be odd?

(A) $p + q + 1$ (B) $pq$ (C) $p^2 + q$ (D) $3q$ (E) $(p+1)q$

<details>
<summary>Answer</summary>

**(C).** $p^2$ is odd (odd × odd), and odd + even is odd. (A) is odd + even + odd = even. (B), (D) and (E) each contain the even factor $q$, so they are even.

</details>

**4.** *(Medium)* What is the sum of all the even integers from 20 to 60, inclusive?

(A) 800 (B) 820 (C) 840 (D) 860 (E) 880

<details>
<summary>Answer</summary>

**(C).** Number of terms: $\tfrac{60 - 20}{2} + 1 = 21$. Mean: $\tfrac{20 + 60}{2} = 40$. Sum: $21 \times 40 = 840$. The trap (A) uses 20 terms, forgetting the "+1".

</details>

**5.** *(Medium)* If $ab < 0$ and $bc^2 > 0$, which of the following must be true?

(A) $a > 0$ (B) $c > 0$ (C) $ac < 0$ (D) $a < b$ (E) $a + b < 0$

<details>
<summary>Answer</summary>

**(D).** $bc^2 > 0$ forces $c \ne 0$ and $c^2 > 0$, so $b > 0$. Then $ab < 0$ gives $a < 0$. A negative number is less than a positive one, so $a < b$. The sign of $c$ is unknown, which kills (B) and (C). (E) depends on sizes: $a = -1$, $b = 3$ gives $a + b = 2 > 0$.

</details>

**6.** *(Medium)* If $n$ is a positive integer, which of the following must divide $n(n+1)(n+2)(n+3)$?

(A) 16 (B) 18 (C) 24 (D) 30 (E) 48

<details>
<summary>Answer</summary>

**(C).** The product of four consecutive integers is divisible by $4! = 24$. The smallest case, $n = 1$, gives exactly $24$, which is not divisible by 16, 18, 30 or 48, so those choices fail.

</details>

**7.** *(Medium, Data Sufficiency)* Is the integer $n$ odd?

(1) $(n+1)^2$ is even.

(2) $n(n+3)$ is even.

<details>
<summary>Answer</summary>

**(A).** (1): a square has the parity of its base, so $n + 1$ is even and $n$ is odd. Sufficient. (2): $n$ and $n + 3$ always have opposite parity, so their product is even for **every** integer $n$. It tells us nothing: $n = 1$ and $n = 2$ both satisfy it. Not sufficient.

</details>

**8.** *(Hard)* How many of the integers from 1 to 100, inclusive, can be written as the sum of three consecutive **positive** integers?

(A) 30 (B) 31 (C) 32 (D) 33 (E) 34

<details>
<summary>Answer</summary>

**(C).** $k + (k+1) + (k+2) = 3(k+1)$ with $k \ge 1$. So the possible sums are the multiples of 3 that are at least 6: $6, 9, \dots, 99$. Those are $3 \times 2$ up to $3 \times 33$, which is $33 - 2 + 1 = 32$ numbers. The trap (D) counts all 33 multiples of 3, but $3 = 0 + 1 + 2$ needs a zero.

</details>

**9.** *(Hard)* If $x$ and $y$ are integers and $x^2 - y^2$ is odd, which of the following must be true?

I. $x + y$ is odd

II. $xy$ is even

III. $x - y$ is odd

(A) I only (B) I and II only (C) I and III only (D) II and III only (E) I, II and III

<details>
<summary>Answer</summary>

**(E).** $x^2 - y^2$ has the same parity as $x - y$ (squares keep parity), so $x$ and $y$ have opposite parity. Then $x + y$ and $x - y$ are both odd, and one of $x$, $y$ is even, so $xy$ is even. All three hold. You can also see it from $x^2 - y^2 = (x+y)(x-y)$: an odd product needs both factors odd.

</details>

**10.** *(Medium)* On the number line, point $P$ is at $-7$ and point $Q$ is at $11$. Point $R$ lies between $P$ and $Q$ and is twice as far from $P$ as it is from $Q$. Where is $R$?

(A) $-1$ (B) 2 (C) 4 (D) 5 (E) 6

<details>
<summary>Answer</summary>

**(D).** The distance $PQ$ is $11 - (-7) = 18$. Splitting it in the ratio $2 : 1$ gives $PR = 12$ and $RQ = 6$. So $R = -7 + 12 = 5$. Check: $\vert 5 - 11\vert = 6$. The trap (B) is the midpoint.

</details>

**11.** *(Hard, Data Sufficiency)* $S$ is the sum of $k$ consecutive integers, where $k$ is a positive integer. Is $S$ divisible by $k$?

(1) $k$ is a multiple of 4.

(2) $k > 10$

<details>
<summary>Answer</summary>

**(A).** $S = k \times \text{mean}$. If $k$ is odd, the mean is the middle term, an integer, so $S$ is a multiple of $k$. If $k$ is even, the mean is a half-integer, $\tfrac{2a+1}{2}$ for some integer $a$, so $S = \tfrac{k}{2}(2a+1)$. For this to be a multiple of $k$, the odd number $2a+1$ would have to be even, which is impossible.

(1): $k$ is even, so the answer is always "no". A definite "no" is sufficient. (2): $k = 11$ gives "yes" (for example $1 + 2 + \cdots + 11 = 66 = 6 \times 11$) and $k = 12$ gives "no" ($1 + 2 + \cdots + 12 = 78$, not a multiple of 12). Not sufficient. The trap is (E) or (C), from feeling that statement (1) "doesn't give a yes".

</details>

**12.** *(Hard)* $n$ is the sum of 12 consecutive odd integers. Which of the following must divide $n$?

(A) 18 (B) 24 (C) 36 (D) 48 (E) 72

<details>
<summary>Answer</summary>

**(B).** If the smallest is the odd number $a$, the sum is $12a + 2(0 + 1 + \cdots + 11) = 12a + 132 = 12(a + 11)$. Since $a$ is odd, $a + 11$ is even, so $n$ is a multiple of 24. Starting at $a = 3$ gives $n = 12 \times 14 = 168$, which is not divisible by 18, 36, 48 or 72. (Starting at $a = 1$ gives 144, which *is* divisible by all five choices, so a single test case is not enough here.)

</details>

> [!NOTE]
> If you use Claude Code, the `quantome-math` plugin (`/plugin install quantome-math@quantome`) can check your working on problems like these. Try each problem by hand first.

## Takeaways

- Before solving, ask what *kind* of number each quantity is: positive, negative, zero, integer, fraction, odd, even.
- Count the negative factors to get the sign of a product. Even powers hide the sign, and odd powers keep it.
- $0$ is even and neither positive nor negative. $1$ is not prime. Test $0$, $1$, $-1$ and $\tfrac12$ first when hunting counterexamples.
- Prove parity rules from $2k$ and $2k + 1$. A sum is odd exactly when it has an odd number of odd terms, and a product is odd only when every factor is odd.
- For evenly spaced lists, sum $=$ number of terms $\times$ average of the first and last terms, and the count is $\tfrac{\text{last} - \text{first}}{\text{step}} + 1$.
- The product of $k$ consecutive integers is divisible by $k!$. The sum of $k$ consecutive integers is divisible by $k$ only when $k$ is odd.
- $\vert a - b\vert$ is a distance, and $\sqrt{x^2} = \vert x\vert$.

## Further reading

- GMAC, *GMAT Official Guide* (current edition, Quantitative Review section). The source of real retired questions; use it to practise these ideas on authentic problems.
- Next in this module: [Divisibility, primes and factors](../../arithmetic/divisibility-primes-and-factors/) and [Remainders and units digits](../../arithmetic/remainders-and-units-digits/).
- For strategies such as testing cases and picking numbers, see [Problem-solving strategies](../../getting-started/problem-solving-strategies/).
