+++
summary = "Integers, divisibility, primes, odd/even rules and remainders."
+++

# Number Properties

## Key ideas

### Integers and divisibility

An integer $a$ is **divisible** by $b$ if $a = bk$ for some integer $k$. Then $b$ is a **factor** of $a$, and $a$ is a **multiple** of $b$.

| Divisible by | Rule |
|---|---|
| 2 | last digit is even |
| 3 | digit sum divisible by 3 |
| 4 | last two digits divisible by 4 |
| 5 | last digit 0 or 5 |
| 6 | divisible by 2 **and** 3 |
| 8 | last three digits divisible by 8 |
| 9 | digit sum divisible by 9 |

### Primes and prime factorisation

A **prime** has exactly two positive factors: 1 and itself. **1 is not prime**, and **2 is the only even prime**.

> [!IMPORTANT]
> If $n = p_1^{a}\, p_2^{b}\, p_3^{c}\cdots$, then the number of positive factors of $n$ is
> $$(a+1)(b+1)(c+1)\cdots$$

For example, $72 = 2^3 \cdot 3^2$ has $(3+1)(2+1) = 12$ factors.

### Odd and even

| Operation | Result |
|---|---|
| even ± even, odd ± odd | even |
| even ± odd | odd |
| even × anything | even |
| odd × odd | odd |

### Remainders

When $n$ is divided by $d$: $n = dq + r$, with $0 \le r < d$.

> [!TIP]
> To find a number that leaves remainder 3 when divided by 5, list $3, 8, 13, 18, \dots$. Testing small cases often beats algebra.

> [!WARNING]
> "Integer" includes 0 and negatives. Unless the question says *positive*, test $0$ and negative values.

## Worked example

**Problem.** If $n$ is a positive integer and $n^2$ is divisible by 72, what is the largest integer that must divide $n$?

**Solution.** $72 = 2^3 \cdot 3^2$. For $n^2$ to contain $2^3$, $n$ must contain at least $2^2$, because exponents in $n^2$ are even. For $n^2$ to contain $3^2$, $n$ needs at least $3^1$. So $n$ must be a multiple of $2^2 \cdot 3 = 12$. **Answer: 12.**

## Practice

1. How many positive factors does $180$ have?

<details>
<summary>Answer</summary>

$180 = 2^2 \cdot 3^2 \cdot 5$, so $(2+1)(2+1)(1+1) = 18$.

</details>

2. If $x$ and $y$ are integers and $xy + x$ is odd, which must be true: (A) $x$ is even (B) $y$ is even (C) $x$ is odd and $y$ is even?

<details>
<summary>Answer</summary>

$xy + x = x(y+1)$. A product is odd only if both factors are odd. So $x$ is odd and $y + 1$ is odd, which means $y$ is even. **(C)**

</details>

3. When $n$ is divided by 6 the remainder is 4. What is the remainder when $2n$ is divided by 6?

<details>
<summary>Answer</summary>

$n = 6q + 4 \Rightarrow 2n = 12q + 8 = 6(2q+1) + 2$. Remainder **2**. Check: $n = 4 \Rightarrow 2n = 8$, and $8 \div 6$ leaves remainder 2.

</details>
