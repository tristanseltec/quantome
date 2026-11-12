+++
summary = "Solve GMAT business and percent problems with multipliers: profit and break-even, markup versus margin, successive discounts and tax, commissions, hidden bases, and percent change in a product or quotient such as price × quantity."
+++

# Profit, Discount and Percent Problems

Business-flavoured percent questions are a GMAT staple: a store marks up, discounts, adds tax; a company's revenue rises while its costs rise faster; a salesperson earns a commission. The arithmetic is never more than multiplying by a few numbers like 1.2 or 0.75. The questions are hard because percents always refer to a **base**, and the base keeps changing. "Up 20%, then down 20%" does not bring you back where you started, and "25% profit" means a different thing depending on whether it is measured against cost or against price.

The single best habit for this whole chapter is to **turn every percent change into a multiplier**. Once you do that, successive changes multiply, hidden bases come out by division, and the traps are easy to see. This chapter builds on [Fractions, decimals and percents](../../arithmetic/fractions-decimals-percents/) and the translation skills in [Translating words into equations](../translating-words-into-equations/).

## Key ideas

### Percent changes as multipliers

An increase of $p\%$ multiplies a quantity by $1 + \tfrac{p}{100}$; a decrease of $p\%$ multiplies it by $1 - \tfrac{p}{100}$.

| Change | Multiplier |
|---|---|
| up 20% | 1.2 |
| down 25% | 0.75 |
| up 8% (sales tax) | 1.08 |
| down 15% (discount) | 0.85 |
| up 150% | 2.5 |

And in reverse, a multiplier $m$ means a change of $(m - 1) \times 100\%$: going from 80 to 92 is a multiplier of $\tfrac{92}{80} = 1.15$, a 15% increase.

**Why multipliers?** A percent change is always relative to the value **just before** the change. Writing it as a multiplier applies it to that value automatically. Successive changes then simply multiply:

$$
\text{final} = \text{original} \times m_1 \times m_2 \times \cdots
$$

### Cost, revenue and profit

> [!IMPORTANT]
> $$\text{Profit} = \text{Revenue} - \text{Cost}, \qquad \text{Revenue} = \text{Price} \times \text{Quantity}$$
> $$\text{Profit percent (on cost)} = \frac{\text{Profit}}{\text{Cost}} \times 100\%$$

On the GMAT, "a profit of 25%" or "sold at a 25% profit" means 25% **of cost**, unless the question says otherwise. So an item that cost \$80 and was sold at a 25% profit sold for $80 \times 1.25 = \$100$. A loss of 20% means it sold for $0.8 \times$ cost.

Costs often split into **fixed costs** (rent, equipment: the same however many units you make) and **variable costs** (materials, per-unit labour: proportional to the number of units). With fixed cost $F$, variable cost $v$ per unit, price $p$ and $q$ units:

$$
\text{Profit} = pq - vq - F = (p - v)q - F.
$$

The quantity $p - v$ is the **contribution per unit**: what each sale contributes toward covering the fixed costs and then toward profit.

### Break-even

The **break-even point** is where profit is zero:

$$
(p - v)q = F \quad\Rightarrow\quad q_{\text{break-even}} = \frac{F}{p - v}.
$$

Intuition: each unit chips in $p - v$ toward the fixed cost, so you need $F / (p - v)$ units to pay it off. To reach a **target profit** $T$, you need $\tfrac{F + T}{p - v}$ units: the fixed cost and the profit both have to be paid for by the contributions.

### Markup on cost versus margin on price

These two ideas use the same dollar amount (price minus cost) but **different bases**:

$$
\text{markup} = \frac{\text{price} - \text{cost}}{\text{cost}}, \qquad \text{margin} = \frac{\text{price} - \text{cost}}{\text{price}}.
$$

A shirt that costs \$60 and sells for \$80 has a profit of \$20: a markup of $\tfrac{20}{60} = 33\tfrac13\%$, but a margin of $\tfrac{20}{80} = 25\%$. Because price is larger than cost (when there is a profit), **the margin is always smaller than the markup**.

Converting between them: if the markup is $k$ (as a decimal), then price $= (1 + k)\times$ cost, so

$$
\text{margin} = \frac{k}{1 + k}, \qquad \text{markup} = \frac{\text{margin}}{1 - \text{margin}}.
$$

A 50% markup is a $\tfrac{0.5}{1.5} = 33\tfrac13\%$ margin. A 25% margin is a $\tfrac{0.25}{0.75} = 33\tfrac13\%$ markup.

> [!WARNING]
> "Profit of 20% of the selling price" and "profit of 20% of cost" are different. Read which base the question names. If none is named, it is cost.

### Successive discounts

A 20% discount followed by a further 25% discount is **not** a 45% discount. The second discount applies to the already reduced price:

$$
0.8 \times 0.75 = 0.6 \quad\Rightarrow\quad \text{a single discount of } 40\%.
$$

In general, successive discounts of $a\%$ and $b\%$ combine to

$$
1 - \left(1 - \tfrac{a}{100}\right)\left(1 - \tfrac{b}{100}\right) = \frac{a}{100} + \frac{b}{100} - \frac{ab}{100^2},
$$

that is, $a + b - \tfrac{ab}{100}$ percent. The correction $\tfrac{ab}{100}$ is the "discount on the discount": the second discount doesn't apply to the part already taken off. The order of the discounts doesn't matter, because multiplication is commutative.

### Discount then tax

The same reasoning shows that **the order of a discount and a sales tax does not matter**: $0.85 \times 1.08 = 1.08 \times 0.85$. What does matter is that you don't simply net the percents: 15% off and 8% tax is a multiplier of $0.918$, not $1 - 0.15 + 0.08 = 0.93$. On a \$40 item, that is \$36.72, not \$37.20.

### "Sold at $x$% profit" problems

When the question gives the **selling price** and the percent profit or loss, find the cost by **dividing** by the multiplier:

$$
\text{cost} = \frac{\text{selling price}}{1 + \tfrac{x}{100}}.
$$

A classic: two items each sell for \$9,600, one at a 20% profit and one at a 20% loss. The costs are $\tfrac{9600}{1.2} = 8000$ and $\tfrac{9600}{0.8} = 12{,}000$. Total cost \$20,000 against revenue \$19,200: an overall **loss** of \$800. The loss is larger in dollars because it is 20% of a larger base.

### Percent problems with a hidden base

When a question tells you the value **after** a change, the base is hidden. "After a 20% increase, the price is \$66" means $1.2 \times \text{original} = 66$, so the original is $66 / 1.2 = 55$.

> [!WARNING]
> The trap is to take 20% of the **new** value: $66 - 0.2 \times 66 = 52.80$. That treats \$66 as the base, but the 20% was computed on the original price. To undo a change, divide by its multiplier; never apply the "opposite" percent.

The same logic answers "by what percent must it now fall to return to the original?": from 66 back to 55 is $\tfrac{11}{66} = 16\tfrac23\%$, not 20%.

### The "raised then lowered by the same percent" trap

Raise a price by $p\%$ and then lower it by $p\%$:

$$
\left(1 + \tfrac{p}{100}\right)\left(1 - \tfrac{p}{100}\right) = 1 - \left(\tfrac{p}{100}\right)^2.
$$

The result is **always below** the original, by $\tfrac{p^2}{100}$ percent. Up 30% then down 30% is a net change of $-9\%$. Up 10% then down 10% is $-1\%$. The order doesn't matter; down-then-up gives the same loss. The reason is that the decrease is computed on a bigger base than the increase was.

### Percent change in a product or a quotient

Many business quantities are products: revenue = price × quantity, total cost = unit cost × number of units, area = length × width. If one factor changes by $a$ and the other by $b$ (as decimals),

$$
(1 + a)(1 + b) = 1 + a + b + ab.
$$

So the percent change of the product is $a + b + ab$, **not** $a + b$. Price up 20% and quantity down 25%: $1.2 \times 0.75 = 0.9$, revenue **down 10%**, not down 5%.

For a quotient, divide the multipliers. If miles per gallon rises 25%, the fuel used over a fixed distance (distance ÷ mpg) is multiplied by $\tfrac{1}{1.25} = 0.8$: down 20%, not 25%. To keep a product constant when one factor falls by $a$, the other must rise by $\tfrac{a}{1 - a}$: a 20% price cut needs a 25% rise in quantity to keep revenue the same.

> [!TIP]
> **Pick 100.** When a problem gives only percents, set the original price, revenue or cost to \$100 (or a number that makes the percents clean) and follow the dollars. Percent problems never depend on the starting value, so any convenient value gives the right answer, and you avoid algebra entirely.

### Commission

A commission is a percent of sales, often only on sales **above** a threshold, added to a base salary:

$$
\text{pay} = \text{base} + c \times (\text{sales} - \text{threshold}) \quad \text{if sales exceed the threshold}.
$$

Working backwards from pay to sales: subtract the base, divide by the commission rate, then **add back** the threshold. Forgetting that last step is the standard error.

### Common traps

> [!WARNING]
> Wrong answer choices on these problems are usually built from:
> 1. **Adding percents** that should be multiplied: successive discounts, discount plus tax, changes in a product.
> 2. **Applying a percent to the wrong base**: taking 20% of the new price to undo a 20% increase.
> 3. **Mixing markup and margin**: using cost when the question says "of the selling price", or vice versa.
> 4. **Assuming symmetric changes cancel**: up $p\%$ then down $p\%$.
> 5. **Forgetting the threshold** in commission problems, or the fixed costs in profit problems.
> 6. **Reporting the wrong quantity**: the new price when asked for the discount, or the profit in dollars when asked for a percent.

> [!NOTE]
> If you use Claude Code, the `quantome-math` plugin (`/plugin install quantome-math@quantome`) can confirm your multipliers once you have worked a problem by hand.

## Worked examples

### Example 1 *(Easy)*

A jacket is discounted by 20%, and the discounted price is then reduced by a further 25%. The final price is equivalent to a single discount of what percent off the original price?

(A) 40% (B) 42.5% (C) 45% (D) 50% (E) 55%

**Solution.** Multipliers: $0.8 \times 0.75 = 0.6$. The final price is 60% of the original, a single discount of **40%**: **(A)**.

With the formula: $20 + 25 - \tfrac{20 \times 25}{100} = 45 - 5 = 40$. **Pick 100**: \$100 → \$80 → \$60. Choice (C) is the "add the discounts" trap.

### Example 2 *(Medium)*

A retailer prices a lamp so that her profit is 25% of the selling price. If the lamp costs her \$60, what is the selling price?

(A) \$75 (B) \$78 (C) \$80 (D) \$84 (E) \$90

**Solution.** This is a **margin** on price. If the price is $p$, the profit is $p - 60 = 0.25p$, so $0.75p = 60$ and $p = 80$. The answer is **(C)**.

Check: profit \$20 is 25% of \$80. ✓ Choice (A), \$75, is a 25% **markup** on cost ($60 \times 1.25$), which gives a profit of only 20% of the price. Notice that the margin of 25% corresponds to a markup of $\tfrac{20}{60} = 33\tfrac13\%$.

### Example 3 *(Medium)*

A small company has fixed costs of \$12,000 per month. Each unit of its product costs \$15 to make and sells for \$40. How many units must it sell in a month to make a profit of \$8,000?

(A) 320 (B) 480 (C) 500 (D) 800 (E) 1,333

**Solution.** Each unit contributes $40 - 15 = \$25$. The contributions must cover the fixed costs and the target profit: $\tfrac{12{,}000 + 8{,}000}{25} = 800$ units, choice **(D)**.

Choice (B), 480, is the break-even quantity ($12{,}000 / 25$); (A), 320, covers only the \$8,000 profit; (C), 500, uses the \$40 price instead of the \$25 contribution ($20{,}000 / 40$).

### Example 4 *(Hard)*

A store buys a coat and marks it up 25% above its cost, to a selling price of \$150. During a sale, the coat is sold at 20% off that selling price. On this sale, the store made

(A) a loss of 5% of cost
(B) a loss of \$6
(C) neither a profit nor a loss
(D) a profit of \$6
(E) a profit of 5% of cost

**Solution.** The cost is hidden: $1.25 \times \text{cost} = 150$, so the cost is \$120. The sale price is $0.8 \times 150 = 120$. The store broke even: **(C)**.

**Why.** The multipliers are $1.25 \times 0.8 = 1$. A 25% increase is exactly undone by a 20% decrease, because $\tfrac{1}{1.25} = 0.8$. Choice (E) is the "add the percents" trap ($+25 - 20 = +5$). Choices (A), (B) and (D) come from losing track of which base each percent uses; for example, "undoing" the markup as $150 \times 0.75 = 112.50$ instead of $150 / 1.25$ makes the sale look profitable.

### Example 5 *(Hard)*

A café raises the price of its sandwiches by 20%, and as a result the number of sandwiches it sells per day falls by 25%. By what percent does the café's daily revenue from sandwiches change?

(A) It decreases by 15%.
(B) It decreases by 10%.
(C) It decreases by 5%.
(D) It does not change.
(E) It increases by 5%.

**Solution.** Revenue = price × quantity, so the multipliers multiply: $1.2 \times 0.75 = 0.9$. Revenue falls by **10%**: **(B)**.

**Pick numbers**: 100 sandwiches at \$10 is \$1,000. Afterwards, 75 sandwiches at \$12 is \$900, a 10% drop. Choice (C) is the trap $+20 - 25 = -5$, which ignores the cross term $ab = (0.2)(-0.25) = -0.05$.

## Practice

**1.** *(Easy)* A shirt is marked at \$40. It is sold at a 15% discount, and then 8% sales tax is added to the discounted price. What does the customer pay?

(A) \$34.00 (B) \$36.72 (C) \$36.80 (D) \$37.20 (E) \$43.20

<details>
<summary>Answer</summary>

**(B) \$36.72.** $40 \times 0.85 = 34$, then $34 \times 1.08 = 36.72$. Choice (D) nets the percents ($40 \times 0.93$); (A) forgets the tax; (E) forgets the discount.

</details>

**2.** *(Easy)* After a 20% increase, the price of a book is \$66. What was the price before the increase?

(A) \$52.80 (B) \$55.00 (C) \$56.00 (D) \$60.00 (E) \$79.20

<details>
<summary>Answer</summary>

**(B) \$55.00.** $1.2 \times \text{original} = 66$, so the original is $66 / 1.2 = 55$. Choice (A) takes 20% off the new price, the hidden-base trap; (E) adds another 20%.

</details>

**3.** *(Medium)* The price of a stock rises by 30% one week and falls by 30% the next week. Compared with its price at the start, its price at the end of the second week is

(A) 30% lower (B) 9% lower (C) 3% lower (D) unchanged (E) 9% higher

<details>
<summary>Answer</summary>

**(B) 9% lower.** $1.3 \times 0.7 = 0.91$. In general, up and down by $p\%$ leaves $1 - (p/100)^2$; here $1 - 0.09$. Choice (D) is the trap "the changes cancel".

</details>

**4.** *(Hard)* A dealer sold two cars for \$9,600 each. On one he made a profit of 20% of its cost, and on the other he made a loss of 20% of its cost. On the two sales combined, the dealer had

(A) a loss of \$800
(B) a loss of \$400
(C) a loss of \$384
(D) neither a profit nor a loss
(E) a profit of \$800

<details>
<summary>Answer</summary>

**(A) a loss of \$800.** The costs are hidden: $\tfrac{9600}{1.2} = 8{,}000$ (profit \$1,600) and $\tfrac{9600}{0.8} = 12{,}000$ (loss \$2,400). Total cost \$20,000, revenue \$19,200: a loss of \$800.

The 20% loss is on a bigger base than the 20% profit, so a loss is guaranteed. Choice (D) is the "they cancel" trap.

</details>

**5.** *(Medium)* A salesperson earns \$1,500 per month plus a commission of 6% on the part of her monthly sales above \$20,000. Last month she earned \$3,180. What were her sales for the month?

(A) \$28,000 (B) \$36,000 (C) \$48,000 (D) \$50,000 (E) \$53,000

<details>
<summary>Answer</summary>

**(C) \$48,000.** Commission $= 3180 - 1500 = 1680$, which is 6% of the sales above \$20,000: $1680 / 0.06 = 28{,}000$. Total sales $= 20{,}000 + 28{,}000 = 48{,}000$. Choice (A) forgets to add back the threshold; (E) is $3180 / 0.06$, which ignores both the base salary and the threshold.

</details>

**6.** *(Medium)* A store sets its prices by marking up each item 50% above its cost. The store's profit on an item is what percent of the item's selling price?

(A) 25% (B) $33\tfrac13\%$ (C) 50% (D) $66\tfrac23\%$ (E) 150%

<details>
<summary>Answer</summary>

**(B) $33\tfrac13\%$.** Pick a cost of \$100: the price is \$150 and the profit \$50, which is $\tfrac{50}{150} = \tfrac13$ of the price. In general, margin $= \tfrac{k}{1 + k} = \tfrac{0.5}{1.5}$. Choice (C) confuses margin with markup; (D) is cost as a percent of price.

</details>

**7.** *(Medium)* A car's fuel efficiency, in miles per gallon, improves by 25%. By what percent does the amount of fuel it needs for a 300-mile trip decrease?

(A) 12.5% (B) 15% (C) 18% (D) 20% (E) 25%

<details>
<summary>Answer</summary>

**(D) 20%.** Fuel $= \tfrac{\text{distance}}{\text{mpg}}$, so it is multiplied by $\tfrac{1}{1.25} = 0.8$, a 20% decrease. For example, at 30 mpg the trip needs 10 gallons; at 37.5 mpg it needs 8. Choice (E) assumes a quotient changes by the same percent as its denominator. (The 300 miles is irrelevant.)

</details>

**8.** *(Hard)* A product has fixed costs of \$18,000, a variable cost of \$30 per unit and a selling price of \$50 per unit. If the selling price is raised by 10% and costs do not change, by what percent does the break-even quantity decrease?

(A) 9.1% (B) 10% (C) 18% (D) 20% (E) 25%

<details>
<summary>Answer</summary>

**(D) 20%.** Originally the contribution is $50 - 30 = 20$ per unit, so break-even is $18{,}000 / 20 = 900$ units. The new price is \$55 and the contribution is \$25, so break-even is $18{,}000 / 25 = 720$ units: a decrease of $\tfrac{180}{900} = 20\%$.

A 10% rise in **price** is a 25% rise in **contribution** (from 20 to 25), and break-even is inversely proportional to contribution: $\tfrac{1}{1.25} = 0.8$. Choice (A), $1 - \tfrac{1}{1.1}$, applies the price change to the whole denominator; (B) assumes the quantities move one-for-one.

</details>

**9.** *(Medium)* A store advertises "30% off everything, and an extra $x$% off the sale price at the checkout". If the combined effect is a 44% discount from the original price, what is $x$?

(A) 10 (B) 12 (C) 14 (D) 16 (E) 20

<details>
<summary>Answer</summary>

**(E) 20.** $0.7 \times (1 - \tfrac{x}{100}) = 0.56$, so $1 - \tfrac{x}{100} = 0.8$ and $x = 20$. Pick 100: \$100 → \$70 → \$56, and taking \$14 off \$70 is 20%. Choice (C), $44 - 30$, adds the discounts.

</details>

**10.** *(Hard)* Last year, a company's profit was 20% of its revenue. This year, its revenue increased by 20% and its costs increased by 30%. By what percent did its profit change?

(A) It decreased by 20%.
(B) It decreased by 10%.
(C) It did not change.
(D) It increased by 10%.
(E) It increased by 20%.

<details>
<summary>Answer</summary>

**(A) It decreased by 20%.** Pick revenue \$100, so profit is \$20 and costs are \$80. This year: revenue \$120, costs $80 \times 1.3 = 104$, profit \$16. The change is $\tfrac{-4}{20} = -20\%$.

Costs are the larger base, so a 30% rise in costs (\$24) outweighs a 20% rise in revenue (\$20), and the \$4 shortfall comes out of a profit of only \$20. Choice (B), $20\% - 30\%$, treats percent changes on different bases as if they could be subtracted directly.

</details>

**11.** *(Hard, Data Sufficiency)* A store sold an item. What was the store's profit on the item, as a percent of the item's cost?

(1) The item was sold for \$84.
(2) If the item had been sold for 10% less, the store's profit would have been 5% of the item's cost.

(A) Statement (1) ALONE is sufficient, but statement (2) alone is not sufficient.
(B) Statement (2) ALONE is sufficient, but statement (1) alone is not sufficient.
(C) BOTH statements TOGETHER are sufficient, but NEITHER statement ALONE is sufficient.
(D) EACH statement ALONE is sufficient.
(E) Statements (1) and (2) TOGETHER are NOT sufficient.

<details>
<summary>Answer</summary>

**(B).** Let the price be $s$ and the cost $c$. The question asks for $\tfrac{s - c}{c} = \tfrac{s}{c} - 1$, so we only need the **ratio** $\tfrac{s}{c}$.

(1) gives $s$ but nothing about $c$: not sufficient.

(2) says $0.9s = 1.05c$, so $\tfrac{s}{c} = \tfrac{1.05}{0.9} = \tfrac76$. The profit is $\tfrac16 = 16\tfrac23\%$ of cost. Sufficient on its own.

The trap is (C): it seems you need a dollar amount, but a percent question needs only a ratio. (With both statements the cost would be \$72, but you don't need it.)

</details>

**12.** *(Medium, Data Sufficiency)* Was a shop's revenue from umbrellas in February greater than its revenue from umbrellas in January?

(1) The price per umbrella was 10% higher in February than in January.
(2) The number of umbrellas sold was 8% lower in February than in January.

(A) Statement (1) ALONE is sufficient, but statement (2) alone is not sufficient.
(B) Statement (2) ALONE is sufficient, but statement (1) alone is not sufficient.
(C) BOTH statements TOGETHER are sufficient, but NEITHER statement ALONE is sufficient.
(D) EACH statement ALONE is sufficient.
(E) Statements (1) and (2) TOGETHER are NOT sufficient.

<details>
<summary>Answer</summary>

**(C).** Revenue = price × quantity. (1) alone says nothing about quantity (if sales fell by half, revenue fell; if sales were unchanged, revenue rose): not sufficient. (2) alone says nothing about price: not sufficient. Together, revenue is multiplied by $1.1 \times 0.92 = 1.012$, so it rose by 1.2%: a definite yes.

</details>

## Takeaways

- Turn every percent change into a multiplier; successive changes multiply, they don't add.
- Profit percent is on cost unless the question says otherwise. Margin (on price) is always smaller than markup (on cost).
- Break-even quantity is fixed cost ÷ contribution per unit; add the target profit to the fixed cost to hit a profit goal.
- Successive discounts of $a\%$ and $b\%$ give $a + b - \tfrac{ab}{100}$ percent; discount and tax can be applied in either order.
- To recover a hidden base, divide by the multiplier; never apply the "opposite" percent.
- Up $p\%$ then down $p\%$ is always a net loss of $\tfrac{p^2}{100}$ percent.
- For a product, $(1 + a)(1 + b) = 1 + a + b + ab$; for a quotient, divide the multipliers.
- When only percents are given, pick 100 and follow the dollars.

## Further reading

- GMAC, *GMAT Official Guide* (current edition), for official percent and profit questions; many Data Sufficiency items in this area turn on whether a ratio, rather than an amount, is enough.
- [Mixtures and interest](../mixtures-and-interest/) for compound growth, the same multiplier idea repeated over many periods.
- [Fractions, decimals and percents](../../arithmetic/fractions-decimals-percents/) for fluency with fraction–percent equivalents such as $\tfrac16 = 16\tfrac23\%$ and $\tfrac18 = 12.5\%$.
