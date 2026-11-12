+++
summary = "Test divisibility quickly, factor any number into primes, count its factors, find GCDs and LCMs, and handle factorial and 'must be divisible by' questions."
+++

# Divisibility, Primes and Factors

Prime factorisation is the single most useful tool in GMAT number theory. Once a number is written as a product of primes, questions about factors, multiples, perfect squares, GCDs, LCMs and factorials become bookkeeping on exponents. This chapter builds that bookkeeping from the ground up and explains *why* each rule works, so that you can adapt it to unfamiliar questions.

It continues [Number properties](../../arithmetic/number-properties/) and prepares for [Remainders and units digits](../../arithmetic/remainders-and-units-digits/).

## Key ideas

### Divisibility, factors and multiples

An integer $a$ is **divisible** by a non-zero integer $b$ if $a = bk$ for some integer $k$. Then $b$ is a **factor** (or **divisor**) of $a$, and $a$ is a **multiple** of $b$. On the GMAT, "factor" means a positive factor unless stated otherwise.

Two facts follow straight from the definition:

- If $d$ divides $a$ and $d$ divides $b$, then $d$ divides $a + b$ and $a - b$. (If $a = dk$ and $b = dm$, then $a \pm b = d(k \pm m)$.)
- If $d$ divides $a$, then $d$ divides every multiple of $a$.

The first fact has a useful twist: if $d$ divides $a$ but **not** $b$, then $d$ does not divide $a + b$. For example, $n! + 1$ is not divisible by any of $2, 3, \dots, n$, because each of them divides $n!$ but not $1$.

### Divisibility rules, and why they work

| Divisible by | Rule | Example |
|---|---|---|
| 2 | last digit even | 3,57**4** |
| 3 | digit sum divisible by 3 | 7,425: $7+4+2+5 = 18$ |
| 4 | last two digits divisible by 4 | 8,4**72**: $72 = 4 \times 18$ |
| 5 | last digit 0 or 5 | 7,42**5** |
| 6 | divisible by 2 **and** by 3 | 8,472 |
| 8 | last three digits divisible by 8 | 8,**472**: $472 = 8 \times 59$ |
| 9 | digit sum divisible by 9 | 7,425: digit sum 18 |
| 10 | last digit 0 | 3,140 |
| 11 | alternating digit sum divisible by 11 | 8,349: $9 - 4 + 3 - 8 = 0$ |
| 12 | divisible by 3 **and** by 4 | 6,372 |

**Why the last-digit rules work.** Write a number as $10a + u$, where $u$ is the units digit. Since $10$ is a multiple of 2 and of 5, $10a$ is too. So divisibility by 2 or 5 depends only on $u$. Likewise $100$ is a multiple of 4 and $1000$ is a multiple of 8, so only the last two or last three digits matter for 4 and 8.

**Why the digit-sum rules work.** Each power of 10 is one more than a multiple of 9: $10 = 9 + 1$, $100 = 99 + 1$, $1000 = 999 + 1$. So

$$
7425 = 7(999 + 1) + 4(99 + 1) + 2(9 + 1) + 5 = \underbrace{7 \cdot 999 + 4 \cdot 99 + 2 \cdot 9}_{\text{multiple of 9}} + (7 + 4 + 2 + 5).
$$

The number and its digit sum differ by a multiple of 9, so they leave the same remainder when divided by 9, and therefore by 3. The rule for 11 works the same way, because $10 = 11 - 1$, $100 = 99 + 1$, $1000 = 1001 - 1$: the powers of 10 alternate between "one less" and "one more" than a multiple of 11.

**Combined rules need coprime parts.** A number is divisible by 6 when it is divisible by 2 and 3, because 2 and 3 share no factor. For 12 you must use 3 and 4, **not** 2 and 6: the number 18 is divisible by both 2 and 6 but not by 12. The general principle is that $n$ is divisible by both $a$ and $b$ exactly when it is divisible by $\operatorname{lcm}(a, b)$, which is $ab$ only when $a$ and $b$ share no prime factor.

### Primes and the fundamental theorem

A **prime** is an integer greater than 1 whose only positive factors are 1 and itself. An integer greater than 1 that is not prime is **composite**.

- **1 is not prime.** It has only one positive factor.
- **2 is the only even prime.** Every other even number has 2 as a factor.
- The primes below 50 are 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47. There are 15 of them; knowing them saves time.

**Testing whether $n$ is prime.** You only need to try prime divisors up to $\sqrt n$. If $n = ab$ with both factors larger than $\sqrt n$, then $ab > n$, which is impossible, so any factorisation has a factor at most $\sqrt n$. To test 221, try 2, 3, 5, 7, 11, 13 (since $15^2 = 225 > 221$). It fails at 13: $221 = 13 \times 17$.

> [!IMPORTANT]
> **Fundamental theorem of arithmetic.** Every integer greater than 1 can be written as a product of primes in exactly one way, apart from the order of the factors:
> $$n = p_1^{a_1}\, p_2^{a_2} \cdots p_k^{a_k}.$$

Uniqueness is what makes the rest of this chapter work. It also gives the key fact that **if a prime $p$ divides $ab$, then $p$ divides $a$ or $p$ divides $b$**: the prime has to appear in one of the two factorisations. This fails for composite numbers: 6 divides $4 \times 9$ but divides neither 4 nor 9.

To factorise, divide out small primes repeatedly, or split the number into any convenient product first: $360 = 36 \times 10 = (2^2 \cdot 3^2)(2 \cdot 5) = 2^3 \cdot 3^2 \cdot 5$.

### Reading factors from a factorisation

Write $n = p_1^{a_1} p_2^{a_2} \cdots p_k^{a_k}$. Every factor of $n$ is built by choosing, for each prime, an exponent from 0 up to the exponent in $n$. For $72 = 2^3 \cdot 3^2$, a factor is $2^i 3^j$ with $i \in \{0, 1, 2, 3\}$ and $j \in \{0, 1, 2\}$. That is 4 choices times 3 choices.

> [!IMPORTANT]
> **Number of positive factors.** If $n = p_1^{a_1} p_2^{a_2} \cdots p_k^{a_k}$, then $n$ has
> $$(a_1 + 1)(a_2 + 1)\cdots(a_k + 1)$$
> positive factors.

So $72$ has $(3+1)(2+1) = 12$ factors, and $180 = 2^2 \cdot 3^2 \cdot 5$ has $3 \times 3 \times 2 = 18$.

The same "choose an exponent" idea answers restricted counts:

- **Odd factors**: force the exponent of 2 to be 0. For $72$, there are $1 \times 3 = 3$ odd factors (1, 3, 9).
- **Even factors**: total minus odd. For $72$, $12 - 3 = 9$.
- **Factors that are multiples of $m$**: write the factor as $m \times (\text{a factor of } n/m)$ and count the factors of $n / m$.

### Perfect squares, cubes and odd factor counts

A number is a **perfect square** exactly when every exponent in its prime factorisation is even, because squaring doubles each exponent: $(2^2 \cdot 3)^2 = 2^4 \cdot 3^2$. Likewise, a **perfect cube** has every exponent a multiple of 3.

This turns "smallest multiplier" questions into exponent repair. To make $540 = 2^2 \cdot 3^3 \cdot 5$ a perfect square, raise each odd exponent by 1: multiply by $3 \cdot 5 = 15$.

**Perfect squares are exactly the numbers with an odd number of factors.** Factors normally come in pairs $(d, n/d)$: for 72 the pairs are $1 \times 72$, $2 \times 36$, $3 \times 24$, $4 \times 18$, $6 \times 12$, $8 \times 9$. A pair only collapses to one factor when $d = n/d$, that is $d^2 = n$. So the count is odd precisely for perfect squares. 36 has the pairs $1 \times 36$, $2 \times 18$, $3 \times 12$, $4 \times 9$ and the single $6$, giving 9 factors. In the exponent formula, every $(a_i + 1)$ is odd exactly when every $a_i$ is even.

> [!TIP]
> A number with exactly **3** factors must be the square of a prime ($p^2$ has factors $1, p, p^2$), because $3$ can only be written as $(2 + 1)$. In general, translate a factor count back into possible exponent patterns: 4 factors means $p^3$ or $pq$, 6 factors means $p^5$ or $p^2 q$.

### GCD and LCM

The **greatest common divisor** $\gcd(a, b)$ is the largest integer dividing both. The **least common multiple** $\operatorname{lcm}(a, b)$ is the smallest positive integer divisible by both.

With prime factorisations, both come from comparing exponents prime by prime:

> [!IMPORTANT]
> - $\gcd$: for each prime, take the **smaller** exponent (primes missing from one number get exponent 0).
> - $\operatorname{lcm}$: for each prime, take the **larger** exponent.
> - For two positive integers, $\gcd(a, b) \times \operatorname{lcm}(a, b) = a \times b$.

Example: $84 = 2^2 \cdot 3 \cdot 7$ and $360 = 2^3 \cdot 3^2 \cdot 5$.

- $\gcd = 2^2 \cdot 3^1 = 12$ (5 and 7 drop out because each is missing from one number).
- $\operatorname{lcm} = 2^3 \cdot 3^2 \cdot 5 \cdot 7 = 2520$.
- Check: $12 \times 2520 = 30{,}240 = 84 \times 360$.

**Why $\gcd \times \operatorname{lcm} = ab$.** For each prime, the two exponents are some pair $x$ and $y$. The GCD takes $\min(x, y)$ and the LCM takes $\max(x, y)$, and $\min + \max = x + y$. So, prime by prime, the exponents in $\gcd \times \operatorname{lcm}$ add up to the exponents in $ab$. The identity is for **two** numbers only: it fails for three.

**Useful consequences.**

- If $\gcd(a, b) = g$, write $a = gm$ and $b = gn$ with $\gcd(m, n) = 1$. Then $\operatorname{lcm}(a, b) = gmn$. This is the standard way to count pairs with a given GCD and LCM.
- Two consecutive integers are always coprime (any common divisor would divide their difference, 1).
- LCM questions hide in word problems: "events that repeat every 12 and 18 days next coincide after $\operatorname{lcm}(12, 18) = 36$ days". GCD questions hide in "largest equal groups" or "largest square tile" wording.

### Factorials: trailing zeros and Legendre's formula

$n! = 1 \times 2 \times \cdots \times n$ contains every prime up to $n$, often many times. Two questions come up.

**Trailing zeros.** Each trailing zero is a factor of $10 = 2 \times 5$. In $n!$ there are far more factors of 2 than of 5, so the number of trailing zeros equals the number of factors of 5. Count them like this:

- every multiple of 5 contributes one 5: $\lfloor n/5 \rfloor$ of them;
- every multiple of 25 contributes a second 5: $\lfloor n/25 \rfloor$;
- every multiple of 125 a third: $\lfloor n/125 \rfloor$, and so on.

For $100!$: $20 + 4 = 24$ trailing zeros. (Here $\lfloor x \rfloor$ means "round down to an integer".)

> [!IMPORTANT]
> **Legendre's formula.** The exponent of a prime $p$ in $n!$ is
> $$\left\lfloor \frac{n}{p} \right\rfloor + \left\lfloor \frac{n}{p^2} \right\rfloor + \left\lfloor \frac{n}{p^3} \right\rfloor + \cdots$$
> stopping when $p^k > n$.

For example, the exponent of 3 in $50!$ is $16 + 5 + 1 = 22$, so $3^{22}$ divides $50!$ but $3^{23}$ does not. A quick way to compute the terms is to keep dividing the previous quotient by $p$: $50 \to 16 \to 5 \to 1$.

For a **composite** base, factor it first and find the bottleneck prime. The largest $k$ with $12^k = 2^{2k} 3^k$ dividing $n!$ is the smaller of $\lfloor (\text{exponent of 2}) / 2 \rfloor$ and the exponent of 3.

> [!WARNING]
> Counting only multiples of 5 for trailing zeros (forgetting 25, 50, 75, ...) is the classic error, and answer choices are built from it. For $100!$ the trap answer is 20.

### "Must be divisible by" questions

These ask what is forced by a condition. Work with exponents.

- **If $n^2$ is divisible by $m$**, look at each prime in $m$. Since every exponent in $n^2$ is even and equals twice the exponent in $n$, $n$ needs at least half the exponent, rounded up. If $72 = 2^3 \cdot 3^2$ divides $n^2$, then $n$ needs $2^2$ (since $2 \cdot 2 \ge 3$) and $3^1$, so $n$ must be a multiple of 12, and 12 is the best possible ($n = 12$ works).
- **If $n^3$ is divisible by $m$**, $n$ needs each exponent divided by 3 and rounded up.
- **If $n$ is divisible by $a$ and by $b$**, then $n$ is divisible by $\operatorname{lcm}(a, b)$, but not necessarily by $ab$.

> [!TIP]
> To find "the largest number that must divide $n$", construct the **smallest** $n$ that meets the condition. Whatever must divide every valid $n$ must divide that one, so the answer is usually that smallest $n$ itself.

> [!WARNING]
> Common traps in this topic:
> - calling 1 a prime, or forgetting that 2 is prime;
> - combining divisibility rules with overlapping parts (2 and 6 for 12);
> - assuming that $a \mid n$ and $b \mid n$ imply $ab \mid n$;
> - in "must divide $n$" questions, choosing a number that divides $n^2$ but not $n$;
> - applying $\gcd \times \operatorname{lcm} = ab$ to three numbers.

## Worked examples

**Example 1** *(Easy)*. How many positive factors does 360 have?

(A) 6 (B) 9 (C) 18 (D) 24 (E) 36

**Solution.** $360 = 2^3 \cdot 3^2 \cdot 5$, so the count is $(3+1)(2+1)(1+1) = 24$. **Answer: (D).** The distractors come from misusing the formula: (A) multiplies the exponents themselves ($3 \times 2 \times 1$), (B) adds the "exponent + 1" terms ($4 + 3 + 2$), and (C) comes from a factorisation that loses one of the 2s ($2^2 \cdot 3^2 \cdot 5 = 180$).

**Example 2** *(Medium)*. The greatest common divisor of two positive integers is 12 and their least common multiple is 360. If one of the integers is 72, what is the other?

(A) 30 (B) 45 (C) 60 (D) 90 (E) 120

**Solution.** Use $\gcd \times \operatorname{lcm} = ab$: the other integer is $\dfrac{12 \times 360}{72} = 60$. Check: $72 = 2^3 \cdot 3^2$ and $60 = 2^2 \cdot 3 \cdot 5$ give $\gcd = 2^2 \cdot 3 = 12$ and $\operatorname{lcm} = 2^3 \cdot 3^2 \cdot 5 = 360$. **Answer: (C).**

**Example 3** *(Medium)*. How many zeros are at the end of $80!$ when it is written out in full?

(A) 16 (B) 18 (C) 19 (D) 20 (E) 21

**Solution.** Count factors of 5: $\lfloor 80/5 \rfloor = 16$ multiples of 5, plus $\lfloor 80/25 \rfloor = 3$ multiples of 25 (25, 50, 75) that each give an extra 5. Total $16 + 3 = 19$. **Answer: (C).** The trap (A) ignores the multiples of 25.

**Example 4** *(Hard)*. If $n$ is a positive integer and $n^3$ is divisible by 360, what is the largest integer that must divide $n$?

(A) 6 (B) 12 (C) 30 (D) 60 (E) 360

**Solution.** $360 = 2^3 \cdot 3^2 \cdot 5$. The exponents in $n^3$ are three times those in $n$, so:

- $2^3$ in $n^3$ needs $2^1$ in $n$;
- $3^2$ in $n^3$ needs $3^1$ in $n$ (since $3 \times 1 = 3 \ge 2$);
- $5^1$ in $n^3$ needs $5^1$ in $n$.

So $n$ must be a multiple of $2 \cdot 3 \cdot 5 = 30$. And $n = 30$ works: $30^3 = 27{,}000 = 360 \times 75$. So no larger number must divide $n$. **Answer: (C).**

Choices (D) and (E) are traps from requiring $n$ itself, rather than $n^3$, to contain the factors of 360.

**Example 5** *(Hard)*. What is the largest integer $k$ such that $12^k$ is a factor of $30!$?

(A) 10 (B) 13 (C) 14 (D) 15 (E) 26

**Solution.** $12^k = 2^{2k} \cdot 3^k$. By Legendre's formula:

- exponent of 2 in $30!$: $15 + 7 + 3 + 1 = 26$, which allows $2k \le 26$, so $k \le 13$;
- exponent of 3 in $30!$: $10 + 3 + 1 = 14$, which allows $k \le 14$.

The 2s run out first, so $k = 13$. **Answer: (B).** Choice (C) is the trap of assuming the larger prime is always the bottleneck, and (E) forgets that each 12 uses two 2s.

## Practice

<details>
<summary>Data Sufficiency answer choices (the same on every DS question)</summary>

- **(A)** Statement (1) ALONE is sufficient, but statement (2) alone is not sufficient.
- **(B)** Statement (2) ALONE is sufficient, but statement (1) alone is not sufficient.
- **(C)** BOTH statements TOGETHER are sufficient, but NEITHER statement ALONE is sufficient.
- **(D)** EACH statement ALONE is sufficient.
- **(E)** Statements (1) and (2) TOGETHER are NOT sufficient.

</details>

**1.** *(Easy)* Which of the following is divisible by 12?

(A) 4,218 (B) 5,034 (C) 6,372 (D) 7,446 (E) 8,130

<details>
<summary>Answer</summary>

**(C).** All five numbers are even with digit sums divisible by 3, so all are divisible by 6. That is the trap. For 12 you need 3 and 4. Check the last two digits for 4: 18, 34, 72, 46, 30. Only $72 = 4 \times 18$ works, so 6,372 ($= 12 \times 531$).

</details>

**2.** *(Easy)* How many prime numbers are between 30 and 60?

(A) 5 (B) 6 (C) 7 (D) 8 (E) 9

<details>
<summary>Answer</summary>

**(C).** 31, 37, 41, 43, 47, 53, 59. To rule out the others, only 2, 3, 5 and 7 need testing, since $8^2 = 64 > 60$. Watch 51 ($= 3 \times 17$) and 57 ($= 3 \times 19$), which look prime.

</details>

**3.** *(Easy)* What is the least common multiple of 18, 24 and 30?

(A) 120 (B) 180 (C) 360 (D) 720 (E) 12,960

<details>
<summary>Answer</summary>

**(C).** $18 = 2 \cdot 3^2$, $24 = 2^3 \cdot 3$, $30 = 2 \cdot 3 \cdot 5$. Take the largest exponents: $2^3 \cdot 3^2 \cdot 5 = 360$. Choice (E) is the product $18 \times 24 \times 30$, a common multiple but not the least.

</details>

**4.** *(Medium)* How many of the positive factors of 720 are odd?

(A) 4 (B) 6 (C) 8 (D) 10 (E) 30

<details>
<summary>Answer</summary>

**(B).** $720 = 2^4 \cdot 3^2 \cdot 5$. An odd factor uses $2^0$, so count the factors of $3^2 \cdot 5$: $(2+1)(1+1) = 6$. They are 1, 3, 5, 9, 15, 45. Choice (E) is the total number of factors.

</details>

**5.** *(Medium)* What is the smallest positive integer $k$ such that $540k$ is a perfect square?

(A) 3 (B) 5 (C) 15 (D) 30 (E) 60

<details>
<summary>Answer</summary>

**(C).** $540 = 2^2 \cdot 3^3 \cdot 5$. The exponents of 3 and 5 are odd, so multiply by $3 \cdot 5 = 15$ to get $2^2 \cdot 3^4 \cdot 5^2 = 8100 = 90^2$.

</details>

**6.** *(Medium)* How many integers from 1 to 200, inclusive, have an odd number of positive factors?

(A) 7 (B) 13 (C) 14 (D) 15 (E) 100

<details>
<summary>Answer</summary>

**(C).** Only perfect squares have an odd number of factors. The squares up to 200 are $1^2, 2^2, \dots, 14^2 = 196$ (since $15^2 = 225$), so there are 14. Choice (E) confuses "odd number of factors" with "odd number".

</details>

**7.** *(Medium, Data Sufficiency)* Is the positive integer $n$ divisible by 12?

(1) $n$ is divisible by 6.

(2) $n$ is divisible by 8.

<details>
<summary>Answer</summary>

**(C).** (1): $n = 6$ (no) and $n = 12$ (yes). Not sufficient. (2): $n = 8$ (no) and $n = 24$ (yes). Not sufficient. Together, $n$ is a multiple of $\operatorname{lcm}(6, 8) = 24$, which is a multiple of 12. Sufficient. Note that the combination gives 24, not $6 \times 8 = 48$.

</details>

**8.** *(Hard)* Positive integers $a$ and $b$, with $a < b$, have greatest common divisor 6 and least common multiple 180. How many such pairs $(a, b)$ are there?

(A) 2 (B) 3 (C) 4 (D) 6 (E) 8

<details>
<summary>Answer</summary>

**(C).** Write $a = 6m$, $b = 6n$ with $\gcd(m, n) = 1$. Then $\operatorname{lcm} = 6mn = 180$, so $mn = 30 = 2 \cdot 3 \cdot 5$. Coprime $m$ and $n$ cannot share a prime, so each of the three primes goes wholly to $m$ or to $n$: $2^3 = 8$ ordered splits, or 4 with $m < n$. The pairs are $(6, 180)$, $(12, 90)$, $(18, 60)$, $(30, 36)$. Choice (E) counts ordered pairs, but $a < b$ means $(36, 30)$ and $(30, 36)$ count once.

</details>

**9.** *(Hard)* What is the largest integer $k$ such that $2^k$ divides the product $26 \times 27 \times 28 \times \cdots \times 50$?

(A) 22 (B) 24 (C) 25 (D) 26 (E) 47

<details>
<summary>Answer</summary>

**(C).** The product is $\dfrac{50!}{25!}$. Exponent of 2 in $50!$: $25 + 12 + 6 + 3 + 1 = 47$. In $25!$: $12 + 6 + 3 + 1 = 22$. The difference is $47 - 22 = 25$. Choices (A) and (E) are the two exponents on their own.

</details>

**10.** *(Hard)* If $n$ is a positive integer and $n^2$ is divisible by both 18 and 20, which of the following must divide $n$?

I. 12

II. 30

III. 60

(A) I only (B) II only (C) III only (D) I and II only (E) II and III only

<details>
<summary>Answer</summary>

**(B).** $n^2$ is divisible by $\operatorname{lcm}(18, 20) = 180 = 2^2 \cdot 3^2 \cdot 5$. Halving the exponents and rounding up, $n$ needs $2 \cdot 3 \cdot 5 = 30$. And $n = 30$ works ($900 = 180 \times 5$), but 30 is divisible by neither 12 nor 60. So only II must hold.

</details>

**11.** *(Hard, Data Sufficiency)* How many positive divisors does the positive integer $n$ have?

(1) $n = 2p$, where $p$ is an odd prime.

(2) $n^2$ has exactly 9 positive divisors.

<details>
<summary>Answer</summary>

**(A).** (1): $n = 2^1 p^1$ with $p \ne 2$, so $n$ has $(1+1)(1+1) = 4$ divisors whatever $p$ is. Sufficient. (2): the exponents of $n^2$ are all even, and $9 = 9$ or $3 \times 3$. So $n^2 = p^8$ (then $n = p^4$, with 5 divisors) or $n^2 = p^2 q^2$ (then $n = pq$, with 4 divisors). For example $n = 16$ and $n = 6$ both work. Not sufficient.

</details>

> [!NOTE]
> If you use Claude Code, the `quantome-math` plugin (`/plugin install quantome-math@quantome`) can factorise numbers and check counts like these. Do the exponent bookkeeping by hand first; the exam has no calculator.

## Takeaways

- Factor into primes first. Almost every question in this chapter becomes a question about exponents.
- Last-digit rules work because 10, 100 and 1000 are multiples of 2, 4, 5 and 8. Digit-sum rules work because each power of 10 is one more than a multiple of 9.
- Combine divisibility rules only with coprime parts: 12 needs 3 and 4, not 2 and 6.
- Number of factors $= (a_1 + 1)(a_2 + 1)\cdots$. Odd factor count $\iff$ perfect square.
- GCD takes the smaller exponent, LCM the larger, and $\gcd \times \operatorname{lcm} = ab$ for two numbers.
- Trailing zeros of $n!$ count the 5s: $\lfloor n/5 \rfloor + \lfloor n/25 \rfloor + \cdots$. Legendre's formula does the same for any prime.
- For "must divide $n$" questions, build the smallest valid $n$ and check the choices against it.

## Further reading

- GMAC, *GMAT Official Guide* (current edition). Its Problem Solving and Data Sufficiency sections contain many retired number-theory questions to practise on.
- Related chapters: [Number properties](../../arithmetic/number-properties/), [Remainders and units digits](../../arithmetic/remainders-and-units-digits/) and, for divisibility in Data Sufficiency, [Data sufficiency by topic](../../data-sufficiency/data-sufficiency-by-topic/).
