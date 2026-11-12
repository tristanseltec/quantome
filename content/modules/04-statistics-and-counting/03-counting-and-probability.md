+++
summary = "The fundamental counting principle, permutations, combinations and basic probability."
+++

# Counting & Probability

## Key ideas

**Fundamental counting principle:** if one choice can be made in $m$ ways and a second in $n$ ways, together they can be made in $mn$ ways.

> [!IMPORTANT]
> Order matters (arrangements): $\displaystyle P(n,k) = \frac{n!}{(n-k)!}$
> Order doesn't matter (groups): $\displaystyle \binom{n}{k} = \frac{n!}{k!\,(n-k)!}$

### Probability

$$P(\text{event}) = \frac{\text{favourable outcomes}}{\text{total outcomes}}$$

- Independent events: $P(A \text{ and } B) = P(A)\,P(B)$
- Complement: $P(\text{at least one}) = 1 - P(\text{none})$

> [!TIP]
> "At least one" is almost always faster to compute through the complement.

> [!WARNING]
> Ask "does order matter?" before every counting question. Choosing a committee of 3 from 10 is $\binom{10}{3} = 120$. Choosing a president, VP and treasurer is $10 \cdot 9 \cdot 8 = 720$.

## Worked example

**Problem.** A fair coin is tossed 4 times. What is the probability of getting at least one head?

**Solution.** $P(\text{no heads}) = \left(\tfrac12\right)^4 = \tfrac1{16}$, so $P(\text{at least one}) = 1 - \tfrac1{16} = \tfrac{15}{16}$.

## Practice

1. How many ways can 5 people sit in a row if two of them insist on sitting together?

<details>
<summary>Answer</summary>

Treat the pair as one unit: $4!$ arrangements, times $2!$ for the order within the pair. That gives $24 \times 2 =$ **48**.

</details>

2. Two cards are drawn without replacement from a standard 52-card deck. What is the probability that both are aces?

<details>
<summary>Answer</summary>

$\tfrac{4}{52} \cdot \tfrac{3}{51} = \tfrac{12}{2652} = \tfrac{1}{221}$.

</details>

3. In how many ways can 3 different books be arranged on a shelf, chosen from a set of 7 books?

<details>
<summary>Answer</summary>

Order matters, so $P(7,3) = 7 \times 6 \times 5 =$ **210**.

</details>

4. A fair die is rolled twice. What is the probability of rolling at least one 6?

<details>
<summary>Answer</summary>

$P(\text{no 6}) = \tfrac{5}{6} \cdot \tfrac{5}{6} = \tfrac{25}{36}$, so $P(\text{at least one 6}) = 1 - \tfrac{25}{36} =$ **$\tfrac{11}{36}$**.

</details>

5. How many even three-digit numbers can be formed from the digits 1, 2, 3, 4, 5 if no digit is repeated?

<details>
<summary>Answer</summary>

The units digit must be even: 2 choices (2 or 4). Then 4 choices for the hundreds digit and 3 for the tens digit: $2 \times 4 \times 3 =$ **24**.

</details>
