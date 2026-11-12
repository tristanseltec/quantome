+++
summary = "Evaluate and compose functions, handle domain restrictions and made-up operations, and work with arithmetic, geometric and recursive sequences, including sums and repeating patterns."
+++

# Functions & Sequences

Functions and sequences look like advanced topics, but on the GMAT they test something very basic: can you **follow a rule exactly**? A function is a rule that turns an input into an output. A sequence is a list made by a rule. A "custom operation" such as $a \oplus b = ab + a - b$ is a rule the test writer invented five seconds ago. Students who lose points here rarely lack knowledge; they substitute carelessly, drop a parenthesis, apply two functions in the wrong order, or try to list 100 terms when a pattern repeats every 3.

This chapter gives you the careful substitution habits first, then the formulas for arithmetic and geometric sequences (with the reasoning behind them, so you can rebuild them), and finally the pattern-hunting skills that recursive sequences demand.

## Key ideas

### Functions and function notation

A **function** $f$ assigns to each allowed input $x$ exactly one output, written $f(x)$. If $f(x) = x^2 - 4x + 1$, then $f$ is the rule "square the input, subtract 4 times the input, add 1". The letter $x$ is just a placeholder for the input. To evaluate $f$ at anything, **replace every $x$ with that thing, in parentheses**:
$$
f(-3) = (-3)^2 - 4(-3) + 1 = 9 + 12 + 1 = 22.
$$

The parentheses are not decoration. Without them, $-3^2$ is read as $-(3^2) = -9$, and $-4 \cdot -3$ is easily misread as $-4 - 3$.

The same habit handles inputs that are expressions:
$$
f(x + 1) = (x + 1)^2 - 4(x + 1) + 1 = x^2 - 2x - 2, \qquad f(2t) = 4t^2 - 8t + 1.
$$

> [!WARNING]
> $f(a + b)$ is **not** $f(a) + f(b)$ in general, and $f(2x)$ is **not** $2f(x)$. With $f(x) = x^2$: $f(1 + 2) = 9$, but $f(1) + f(2) = 5$. Only very special functions (like $f(x) = 3x$) behave that way. Whenever you are tempted to "distribute" a function, stop and substitute instead.

Functions can also be given in words or as a table, for example "the cost of printing $n$ flyers is $C(n) = 40 + 0.15n$ dollars". Then $C(200) = 70$ is the cost of 200 flyers, and solving $C(n) = 100$ gives $n = 400$: the number of flyers that \$100 buys.

### Composite functions

A **composite** $f(g(x))$ means "apply $g$ first, then feed the result into $f$". Work from the **inside out**. With $f(x) = 3x - 1$ and $g(x) = x^2 + 2$:
$$
f(g(2)) = f(6) = 17, \qquad g(f(2)) = g(5) = 27.
$$

The order matters: in general $f(g(x)) \ne g(f(x))$. To find a composite as a formula, substitute the whole inner expression: $f(g(x)) = 3(x^2 + 2) - 1 = 3x^2 + 5$, while $g(f(x)) = (3x - 1)^2 + 2 = 9x^2 - 6x + 3$.

> [!TIP]
> For "$f(f(3))$" or "$f(g(a)) = 10$" questions with numbers, evaluate step by step and write each intermediate value down. If an unknown is involved, call the inner output $u$, solve for $u$ first, then solve $g(a) = u$. Two easy equations beat one messy one.

### Domain: which inputs are allowed

On the GMAT, every function deals with real numbers, so two things can exclude an input:

- **Division by zero.** $\dfrac{1}{x - 5}$ is undefined at $x = 5$.
- **Even roots of negative numbers.** $\sqrt{x - 2}$ needs $x - 2 \ge 0$, so $x \ge 2$. Note that $x = 2$ itself is fine: $\sqrt0 = 0$.

So the domain of $f(x) = \dfrac{\sqrt{x - 2}}{x - 5}$ is $x \ge 2$ with $x \ne 5$. Questions about the **range** (possible outputs) usually rest on facts like $x^2 \ge 0$ and $|x| \ge 0$: the function $g(x) = x^2 + 3$ never outputs anything below 3.

### Custom operations (symbolism)

GMAT questions often define a new symbol, such as "for all numbers $a$ and $b$, $a \oplus b = ab + a - b$." This is a function of two inputs dressed up. The rules:

1. **Substitute exactly** as defined, matching positions: in $a \oplus b$, the first input plays the role of $a$. Here $2 \oplus 3 = 6 + 2 - 3 = 5$, but $3 \oplus 2 = 6 + 3 - 2 = 7$.
2. **Work from the innermost parentheses outward**, as with composite functions.
3. **Do not assume familiar properties.** A made-up operation need not be commutative ($a \oplus b = b \oplus a$) or associative ($(a \oplus b) \oplus c = a \oplus (b \oplus c)$). Check, or simply compute in the order given.

When the unknown is inside the operation, write out the definition and you get an ordinary equation. For $x \star y = x^2 - 3y$, the equation $4 \star k = k \star 4$ becomes $16 - 3k = k^2 - 12$, a quadratic.

> [!TIP]
> Questions like "for which of the following operations is $a \ast b = b \ast a$ for all $a, b$?" are fastest by testing one pair of unequal numbers, for example $a = 1$ and $b = 2$. Any operation that gives different answers is out. If more than one survives, test a second pair.

### Sequences

A **sequence** is an ordered list $a_1, a_2, a_3, \dots$, where $a_n$ is the $n$th term. It can be given by an **explicit formula** ($a_n = 3n + 2$, so $a_{10} = 32$) or by a **recursive rule** that builds each term from earlier ones ($a_1 = 5$ and $a_n = a_{n-1} + 3$).

### Arithmetic sequences

In an **arithmetic sequence**, you add the same **common difference** $d$ each time: $7, 11, 15, 19, \dots$ has $d = 4$. To reach the $n$th term from the first you take $n - 1$ steps, so:

> [!IMPORTANT]
> **Arithmetic sequence**
> $$a_n = a_1 + (n - 1)d$$
> $$\text{Number of terms from } a_1 \text{ to } a_n = \frac{a_n - a_1}{d} + 1$$
> $$S_n = a_1 + a_2 + \dots + a_n = n \times \frac{a_1 + a_n}{2}$$

**Why the sum formula works (Gauss's trick).** Write the sum forwards and backwards and add the two lines term by term:
$$
\begin{aligned}
S &= a_1 + a_2 + \dots + a_n \\
S &= a_n + a_{n-1} + \dots + a_1 \\
2S &= (a_1 + a_n) + (a_2 + a_{n-1}) + \dots + (a_n + a_1).
\end{aligned}
$$
Each pair has the same total, $a_1 + a_n$, because moving one step in from each end adds $d$ to one term and subtracts $d$ from the other. There are $n$ pairs, so $2S = n(a_1 + a_n)$. In words: **sum = number of terms × average of the first and last terms**. For evenly spaced numbers, the average equals the average of the first and last, which is also the middle term (or the average of the two middle terms).

Useful consequences:

- $1 + 2 + \dots + n = \dfrac{n(n + 1)}{2}$, so $1 + 2 + \dots + 100 = 5050$.
- $1 + 3 + 5 + \dots + (2n - 1) = n \times \dfrac{1 + (2n - 1)}{2} = n^2$.
- If two terms are given, the gap between them is a whole number of steps: from $a_5 = 17$ to $a_{12} = 45$ is 7 steps covering 28, so $d = 4$.
- **Symmetric terms.** If $m + n = p + q$, then $a_m + a_n = a_p + a_q$. In particular $a_4 + a_{16} = 2a_{10}$, because 4 and 16 are equally far from 10.

> [!WARNING]
> The **off-by-one** error is the most common sequence mistake. The multiples of 6 from 102 to 198 are not $\tfrac{198 - 102}{6} = 16$ numbers but $16 + 1 = 17$: the count of **gaps** is one less than the count of **terms**, just as a fence with 16 gaps has 17 posts. Similarly, the $n$th term uses $n - 1$ steps, not $n$.

### Geometric sequences

In a **geometric sequence**, you **multiply** by the same **common ratio** $r$ each time: $2, 6, 18, 54, \dots$ has $r = 3$. After $n - 1$ multiplications:

> [!IMPORTANT]
> **Geometric sequence**
> $$a_n = a_1 \, r^{\,n-1}$$
> $$S_n = a_1 \, \frac{r^n - 1}{r - 1} \quad (r \ne 1)$$

To find $r$ from two terms, divide: if $a_2 = 6$ and $a_5 = 162$, then $\dfrac{a_5}{a_2} = r^3 = 27$, so $r = 3$ and $a_1 = 2$.

Geometric sequences model anything that grows or shrinks by a fixed **percentage**: a population that doubles every 3 hours, a price that rises 10% a year, a medicine whose amount halves every 6 hours. "Doubles every 3 hours, for 15 hours" means $\tfrac{15}{3} = 5$ doublings, a factor of $2^5 = 32$. The sum formula comes from writing $S - rS$: all the middle terms cancel, leaving $a_1 - a_1 r^n$. You will rarely need it on the GMAT, but it is good to know where it comes from.

### Recursive sequences and patterns

A recursive rule such as $a_n = 2a_{n-1} - 1$ gives you no shortcut formula on the GMAT. You **compute terms** one by one until either you reach the term you need or a **pattern** appears. Three patterns cover almost every question:

- **Cycles.** If the terms repeat every $p$ terms, then $a_n$ depends only on the remainder when $n$ is divided by $p$. (The same idea finds units digits of powers: see [Remainders and units digits](../../arithmetic/remainders-and-units-digits/).)
- **Recognisable formulas.** $a_1 = 1$, $a_n = a_{n-1} + 2n - 1$ gives $1, 4, 9, 16, \dots$: the perfect squares.
- **Sums given directly.** If $S_n$ (the sum of the first $n$ terms) has a formula, then each term is a difference of consecutive sums: $a_n = S_n - S_{n-1}$.

> [!TIP]
> When a question asks for the 50th, 100th or 2,000th term of a recursive sequence, it is almost never asking you to compute that many terms. **Write out 6 to 8 terms** and look for a cycle or a formula. Once you see the period $p$, find the remainder of $n$ divided by $p$, and for sums, add whole cycles at once.

> [!WARNING]
> When a cycle has period $p$, the term with **remainder 0** is the **last** term of the cycle ($a_p$), not the first. If $a_1, a_2, a_3$ repeat, then $a_{99} = a_3$, because 99 leaves remainder 0 on division by 3.

## Worked examples

**Example 1** *(Easy)*. If $f(x) = 2x^2 - 3x$, what is the value of $f(-2)$?

- (A) $-14$
- (B) $-2$
- (C) 2
- (D) 10
- (E) 14

*Solution.* $f(-2) = 2(-2)^2 - 3(-2) = 2(4) + 6 = 14$. **Answer: (E).** (C) comes from $-3(-2) = -6$, a sign error. (B) comes from $2(-2)^2$ computed as $-8$, that is, from dropping the parentheses.

**Example 2** *(Medium)*. For all numbers $a$ and $b$, the operation $\oplus$ is defined by $a \oplus b = ab + a - b$. What is the value of $(2 \oplus 3) \oplus 1$?

- (A) 5
- (B) 7
- (C) 9
- (D) 11
- (E) 13

*Solution.* Inner first: $2 \oplus 3 = 6 + 2 - 3 = 5$. Then $5 \oplus 1 = 5 + 5 - 1 = 9$. **Answer: (C).**

Choice (B) is the result of grouping the other way: $3 \oplus 1 = 3 + 3 - 1 = 5$, then $2 \oplus 5 = 10 + 2 - 5 = 7$. This operation is **not** associative, which is exactly why the order of evaluation matters.

**Example 3** *(Medium)*. What is the sum of all multiples of 6 between 100 and 200?

- (A) 2,400
- (B) 2,450
- (C) 2,550
- (D) 2,700
- (E) 2,850

*Solution.* The first multiple of 6 above 100 is 102; the last below 200 is 198. Number of terms: $\dfrac{198 - 102}{6} + 1 = 16 + 1 = 17$. Average of first and last: $\dfrac{102 + 198}{2} = 150$. Sum $= 17 \times 150 = 2{,}550$. **Answer: (C).**

(A) is the off-by-one error ($16 \times 150$). Always find the actual first and last terms before counting.

**Example 4** *(Hard)*. The function $f$ is defined by $f(x) = 2x + k$, where $k$ is a constant. If $f(f(3)) = 27$, what is the value of $k$?

- (A) 3
- (B) 4
- (C) 5
- (D) 6
- (E) 7

*Textbook method.* Inside out: $f(3) = 6 + k$. Then $f(6 + k) = 2(6 + k) + k = 12 + 3k$. Set $12 + 3k = 27$, so $k = 5$. **Answer: (C).**

*Backsolving.* Try (C), $k = 5$: $f(3) = 11$ and $f(11) = 27$. ✓ A common error is to compute $f(f(3))$ as $2 \cdot f(3)$, forgetting to add $k$ the second time: $2(6 + k) = 27$ gives a non-integer, which is a hint that something has gone wrong.

**Example 5** *(Hard)*. In a sequence, $a_1 = 3$ and $a_n = \dfrac{1}{1 - a_{n-1}}$ for all $n \ge 2$. What is the value of $a_{100}$?

- (A) $-\tfrac12$
- (B) $\tfrac23$
- (C) 1
- (D) $\tfrac32$
- (E) 3

*Solution.* Compute terms until something repeats:
$$
a_1 = 3, \quad a_2 = \frac{1}{1 - 3} = -\frac12, \quad a_3 = \frac{1}{1 + \frac12} = \frac23, \quad a_4 = \frac{1}{1 - \frac23} = 3.
$$
$a_4 = a_1$, and each term depends only on the previous one, so the sequence repeats with period 3: $3, -\tfrac12, \tfrac23, 3, -\tfrac12, \tfrac23, \dots$ Since $100 = 3 \times 33 + 1$, the 100th term is in position 1 of a cycle: $a_{100} = a_1 = 3$. **Answer: (E).**

Check the indexing on a small case: $a_4$ has remainder 1 and equals $a_1$. ✓ (A) is what you get if you think "remainder 1 means the term after $a_1$".

## Practice

Data Sufficiency items use the fixed answer choices explained in [The data sufficiency method](../../data-sufficiency/the-data-sufficiency-method/): **(A)** statement (1) alone is sufficient, but (2) alone is not; **(B)** (2) alone is sufficient, but (1) alone is not; **(C)** both together are sufficient, but neither alone is; **(D)** each alone is sufficient; **(E)** the statements together are not sufficient.

**1.** *(Easy)* If $f(x) = x^2 - 4x + 1$, what is $f(-3)$?

- (A) $-20$
- (B) $-2$
- (C) 4
- (D) 10
- (E) 22

<details>
<summary>Answer</summary>

$f(-3) = (-3)^2 - 4(-3) + 1 = 9 + 12 + 1 = 22$. **(E)**. (B) comes from the sign slip $9 - 12 + 1$. (C) comes from writing $(-3)^2$ as $-9$, and (A) from making both errors.

</details>

**2.** *(Easy)* In an arithmetic sequence, the 5th term is 17 and the 12th term is 45. What is the 30th term?

- (A) 113
- (B) 117
- (C) 120
- (D) 121
- (E) 125

<details>
<summary>Answer</summary>

From term 5 to term 12 is 7 steps covering $45 - 17 = 28$, so $d = 4$. Then $a_{30} = a_{12} + 18d = 45 + 72 = 117$. **(B)**. (D) uses 19 steps instead of 18.

</details>

**3.** *(Medium)* For the function $f(x) = \dfrac{\sqrt{x - 2}}{x - 5}$, which of the following values of $x$ is **not** in the domain of $f$?

- (A) 2
- (B) 3
- (C) 4
- (D) 5
- (E) 6

<details>
<summary>Answer</summary>

The domain needs $x - 2 \ge 0$ (so $x \ge 2$) and $x - 5 \ne 0$. All the choices satisfy $x \ge 2$, but $x = 5$ makes the denominator zero. **(D)**. Note $x = 2$ is allowed: $f(2) = \tfrac{0}{-3} = 0$.

</details>

**4.** *(Medium)* In a geometric sequence of positive numbers, the 2nd term is 6 and the 5th term is 162. What is the 7th term?

- (A) 486
- (B) 729
- (C) 1,458
- (D) 2,187
- (E) 4,374

<details>
<summary>Answer</summary>

$\dfrac{a_5}{a_2} = r^3 = 27$, so $r = 3$. Then $a_7 = a_5 \cdot r^2 = 162 \times 9 = 1{,}458$. **(C)**. (A) is $a_6$; (E) is $a_8$.

</details>

**5.** *(Medium)* A runner runs 12 km in the first week of a training plan and increases the weekly distance by 3 km each week. What is the total distance run in the first 10 weeks?

- (A) 210 km
- (B) 240 km
- (C) 255 km
- (D) 270 km
- (E) 285 km

<details>
<summary>Answer</summary>

Week 10 distance: $12 + 9 \times 3 = 39$ km. Sum $= 10 \times \dfrac{12 + 39}{2} = 10 \times 25.5 = 255$ km. **(C)**. (D) uses $12 + 10 \times 3 = 42$ km for week 10, an off-by-one error: $10 \times \tfrac{12 + 42}{2} = 270$.

</details>

**6.** *(Medium)* A bacterial culture doubles in size every 3 hours. At noon it contains 500 cells. If it keeps growing at this rate, how many cells will it contain at 3 a.m. the next day?

- (A) 4,000
- (B) 7,500
- (C) 8,000
- (D) 16,000
- (E) 32,000

<details>
<summary>Answer</summary>

Noon to 3 a.m. is 15 hours, which is $15 / 3 = 5$ doublings. $500 \times 2^5 = 500 \times 32 = 16{,}000$. **(D)**. (C) counts only 4 doublings and (E) counts 6. (B) is $500 \times 15$, which treats the growth as linear. Geometric growth multiplies.

</details>

**7.** *(Medium)* If $f(x) = x^2$ and $g(x) = x - 3$, for what value of $x$ is $f(g(x)) = g(f(x))$?

- (A) 0
- (B) 1
- (C) 2
- (D) 3
- (E) 6

<details>
<summary>Answer</summary>

$f(g(x)) = (x - 3)^2 = x^2 - 6x + 9$ and $g(f(x)) = x^2 - 3$. Setting them equal: $-6x + 9 = -3$, so $x = 2$. **(C)**. Check: $f(g(2)) = f(-1) = 1$ and $g(f(2)) = g(4) = 1$. ✓

</details>

**8.** *(Hard)* For all numbers $x$ and $y$, let $x \star y = x^2 - 3y$. If $4 \star k = k \star 4$ and $k \ne 4$, what is the value of $k$?

- (A) $-7$
- (B) $-4$
- (C) 3
- (D) 7
- (E) 12

<details>
<summary>Answer</summary>

$4 \star k = 16 - 3k$ and $k \star 4 = k^2 - 12$. Setting them equal: $k^2 + 3k - 28 = 0$, so $(k + 7)(k - 4) = 0$. Since $k \ne 4$, $k = -7$. **(A)**. Check: $4 \star (-7) = 16 + 21 = 37$ and $(-7) \star 4 = 49 - 12 = 37$. ✓ (D) is a sign error in the factoring.

</details>

**9.** *(Hard)* In a sequence, $a_1 = 1$, $a_2 = 2$, and $a_n = a_{n-1} - a_{n-2}$ for all $n \ge 3$. What is the sum of the first 50 terms?

- (A) $-3$
- (B) 0
- (C) 1
- (D) 2
- (E) 3

<details>
<summary>Answer</summary>

Compute: $1, 2, 1, -1, -2, -1, 1, 2, \dots$ The terms repeat every 6, and each block of 6 sums to $1 + 2 + 1 - 1 - 2 - 1 = 0$. The first 48 terms are 8 full blocks, summing to 0. The remaining terms are $a_{49} = a_1 = 1$ and $a_{50} = a_2 = 2$. Total: $3$. **(E)**.

</details>

**10.** *(Hard)* For every positive integer $n$, the sum of the first $n$ terms of a sequence is $n^2 + 2n$. What is the 10th term of the sequence?

- (A) 19
- (B) 20
- (C) 21
- (D) 23
- (E) 120

<details>
<summary>Answer</summary>

The 10th term is the sum of the first 10 terms minus the sum of the first 9: $(100 + 20) - (81 + 18) = 120 - 99 = 21$. **(C)**. (E) is the sum $S_{10}$, not the term. (The sequence is $3, 5, 7, \dots$, the odd numbers from 3, so $a_{10} = 21$. ✓)

</details>

**11.** *(Hard, Data Sufficiency)* In an arithmetic sequence $a_1, a_2, a_3, \dots$, what is the value of $a_{10}$?

(1) $a_4 + a_{16} = 46$

(2) $a_{19} - a_1 = 36$

<details>
<summary>Answer</summary>

(1): $a_4 = a_{10} - 6d$ and $a_{16} = a_{10} + 6d$, so $a_4 + a_{16} = 2a_{10} = 46$ and $a_{10} = 23$, whatever $a_1$ and $d$ are. Sufficient.

(2): $18d = 36$, so $d = 2$, but $a_1$ is unknown, so $a_{10} = a_1 + 18$ can be anything. Not sufficient.

**(A)**. Many people choose (C), thinking they need $a_1$ and $d$ separately. Symmetric terms give the middle term directly.

</details>

**12.** *(Hard, Data Sufficiency)* The function $f$ is defined by $f(x) = ax + b$, where $a$ and $b$ are constants. What is the value of $f(3)$?

(1) $f(1) + f(5) = 18$

(2) $f(5) - f(1) = 8$

<details>
<summary>Answer</summary>

(1): $f(1) + f(5) = (a + b) + (5a + b) = 6a + 2b = 2(3a + b) = 2f(3)$. So $f(3) = 9$. Sufficient. (A linear function's value at the midpoint of 1 and 5 is the average of its values there.)

(2): $4a = 8$, so $a = 2$, but $b$ is unknown: $f(3) = 6 + b$. Not sufficient.

**(A)**.

</details>

> [!NOTE]
> If you use Claude Code, the `quantome-math` plugin (`/plugin install quantome-math@quantome`) can list the terms of a sequence so you can check a pattern you found by hand. Find the pattern yourself first: that is the skill the GMAT rewards.

## Takeaways

- Substitute into a function with parentheses around the input; $f(a + b) \ne f(a) + f(b)$ in general.
- Composite functions work inside out, and the order matters: $f(g(x))$ is usually not $g(f(x))$.
- Domains exclude zeros of denominators and negative values under even roots.
- Custom operations are functions in disguise: substitute exactly, evaluate the innermost brackets first, and assume no commutativity or associativity.
- Arithmetic: $a_n = a_1 + (n - 1)d$; number of terms $= \tfrac{\text{last} - \text{first}}{d} + 1$; sum $=$ number of terms $\times$ average of first and last.
- Geometric: $a_n = a_1 r^{n-1}$; find $r$ by dividing two terms; percentage growth is geometric.
- Recursive sequences: write out 6 to 8 terms, find the cycle, and use remainders (remainder 0 means the last term of the cycle). And $a_n = S_n - S_{n-1}$.

## Further reading

- GMAC, *GMAT Official Guide* (current edition) and the *GMAT Official Guide Quantitative Review*: real retired questions on functions, symbolism and sequences for timed practice.
- In this book: [Translating words into equations](../../word-problems/translating-words-into-equations/), [Remainders and units digits](../../arithmetic/remainders-and-units-digits/) (cycles), [Exponents and roots](../../algebra/exponents-and-roots/) (geometric growth) and [Problem-solving strategies](../../getting-started/problem-solving-strategies/).
