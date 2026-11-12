+++
summary = "Test whether a genetic variant is associated with disease, report an odds ratio with a confidence interval, and control false positives across a million tests with Bonferroni and the Benjamini–Hochberg procedure."
+++

# Hypothesis Testing and Multiple Comparisons

A genome-wide association study (GWAS) for coronary artery disease asks the same question about a million different variants: *is this variant more common in people with CAD than in people without it?* Some variants will look associated purely by chance. If you use the textbook threshold $p < 0.05$ a million times, you expect about 50,000 false alarms. This chapter shows how a single association test works, what a p-value does and does not mean, how to measure effect size with odds ratios and confidence intervals, and how geneticists arrived at the famous genome-wide threshold of $5 \times 10^{-8}$.

You need the normal distribution and the central limit theorem from [distributions and likelihood](../../probability-and-statistics/distributions-and-likelihood/).

## Key ideas

### Null and alternative hypotheses

A hypothesis test compares two statements about the world:

- the **null hypothesis** $H_0$: nothing interesting is happening. For a variant, "allele frequency is the same in cases and controls" or equivalently "odds ratio = 1";
- the **alternative hypothesis** $H_1$: something is. "The frequencies differ", "odds ratio ≠ 1".

We compute a **test statistic** $T$ from the data, a number that tends to be small under $H_0$ and large under $H_1$. The logic is like proof by contradiction, softened by probability: *if $H_0$ were true, would data this extreme be surprising?*

### p-values

> [!IMPORTANT]
> The **p-value** is the probability, computed assuming $H_0$ is true, of getting a test statistic at least as extreme as the one observed:
> $$p = P(T \ge t_{\text{obs}} \mid H_0).$$

If $p$ is below a pre-chosen **significance level** $\alpha$, we **reject** $H_0$. Otherwise we **fail to reject** it, which is not the same as showing it is true.

A useful fact: if $H_0$ is true (and the test is valid), the p-value is uniformly distributed between 0 and 1. So $P(p < \alpha \mid H_0) = \alpha$. Testing many true nulls at $\alpha = 0.05$ gives "significant" results 5% of the time.

> [!WARNING]
> **What a p-value is not.**
> - It is **not** the probability that $H_0$ is true. That would be $P(H_0 \mid \text{data})$, which needs a prior (Bayes' theorem again, see [probability and Bayes' theorem](../../probability-and-statistics/probability-and-bayes-theorem/)).
> - It is **not** the probability that the result is a fluke, nor one minus the probability it will replicate.
> - It is **not** a measure of effect size. A tiny, clinically useless effect gives a tiny p-value in a big enough sample.
> - $p = 0.06$ and $p = 0.04$ are not qualitatively different evidence.
>
> The American Statistical Association's 2016 statement on p-values (Wasserstein and Lazar) lists these points.

### Type I and type II errors, and power

| | $H_0$ true | $H_0$ false |
|---|---|---|
| Reject $H_0$ | **Type I error** (false positive), rate $\alpha$ | Correct: true positive, rate = **power** $= 1 - \beta$ |
| Fail to reject | Correct | **Type II error** (false negative), rate $\beta$ |

You choose $\alpha$. Power depends on the effect size, the sample size and $\alpha$. For a test based on an approximately normal estimate $\hat\theta$ with standard error $\text{SE}$, the statistic is $z = \hat\theta / \text{SE}$. If the true effect is $\theta$, $z$ is roughly $\mathcal{N}(\theta/\text{SE}, 1)$, so for a two-sided test

$$
\text{power} \approx \Phi\!\left(\frac{|\theta|}{\text{SE}} - z_{\alpha/2}\right),
$$

where $\Phi$ is the standard normal cumulative distribution and $z_{\alpha/2}$ is the critical value ($1.96$ for $\alpha = 0.05$). Since $\text{SE} \propto 1/\sqrt{n}$, **halving the effect size needs four times the sample size** for the same power.

### Effect sizes: risk, odds, relative risk and odds ratio

Suppose we follow people for ten years and record whether they carry a variant (exposed) and whether they develop CAD.

| | CAD | No CAD |
|---|---|---|
| Carrier | $a$ | $b$ |
| Non-carrier | $c$ | $d$ |

- **Risk** in carriers: $a/(a+b)$. In non-carriers: $c/(c+d)$.
- **Relative risk** $\text{RR} = \dfrac{a/(a+b)}{c/(c+d)}$.
- **Odds** in carriers: $a/b$. In non-carriers: $c/d$.
- **Odds ratio** $\text{OR} = \dfrac{a/b}{c/d} = \dfrac{ad}{bc}$.

Why bother with odds? Because most genetic studies are **case–control**: we recruit, say, 1,000 cases and 1,000 controls. The proportion of cases is then set by the design, so risks and RR cannot be estimated. The OR, however, is the same whether you compute it along rows or down columns, and a case–control study estimates it correctly. Logistic regression also produces ORs naturally.

When the disease is **rare** (risk a few percent or less), $b \approx a + b$ and $d \approx c + d$, so $\text{OR} \approx \text{RR}$. For common outcomes, the OR is further from 1 than the RR.

> [!WARNING]
> "Odds ratio 1.3" does not mean "30% higher risk" unless the outcome is rare. Always state which one you report.

### Confidence intervals

A 95% **confidence interval** is produced by a procedure that, over repeated studies, captures the true value 95% of the time. Ratios are skewed, so we build intervals on the log scale, where the CLT makes the estimate approximately normal.

> [!IMPORTANT]
> **Wald intervals for ratio measures** (from the 2×2 table above):
> $$\text{SE}(\log \text{OR}) = \sqrt{\tfrac{1}{a} + \tfrac{1}{b} + \tfrac{1}{c} + \tfrac{1}{d}}, \qquad \text{SE}(\log \text{RR}) = \sqrt{\tfrac{1}{a} - \tfrac{1}{a+b} + \tfrac{1}{c} - \tfrac{1}{c+d}}$$
> $$\text{95\% CI} = \exp\big(\log(\text{ratio}) \pm 1.96 \times \text{SE}\big)$$

If the 95% CI for an OR excludes 1, the two-sided Wald test has $p < 0.05$. The interval also shows the effect size and its precision, which the p-value hides.

### The chi-square test on a 2×2 table

In a case–control GWAS, the simplest test is the **allelic test**: count alleles rather than people. Each person contributes two alleles. Form the table

| | Allele A | Allele a | Total |
|---|---|---|---|
| Cases | $O_{11}$ | $O_{12}$ | $R_1$ |
| Controls | $O_{21}$ | $O_{22}$ | $R_2$ |
| Total | $C_1$ | $C_2$ | $N$ |

Under $H_0$, allele and case status are independent, so $P(\text{case and A}) = P(\text{case})\,P(\text{A})$, giving the expected count $E_{ij} = R_i C_j / N$. **Pearson's chi-square statistic** adds up the squared, scaled discrepancies:

$$
X^2 = \sum_{i,j} \frac{(O_{ij} - E_{ij})^2}{E_{ij}}.
$$

Under $H_0$ it approximately follows a $\chi^2$ distribution with 1 degree of freedom, which is the distribution of $Z^2$ for standard normal $Z$. So $X^2 = 3.84 = 1.96^2$ corresponds to $p = 0.05$.

> [!NOTE]
> The allelic test assumes the two alleles in a person are independent (Hardy–Weinberg equilibrium). Modern GWAS instead use **logistic regression** of case status on dosage 0/1/2, with covariates such as age, sex and ancestry principal components. For a single SNP without covariates it gives a very similar answer. See [GWAS and polygenic risk scores](../../genomics-foundations/gwas-and-polygenic-risk-scores/).

## Multiple testing

### The problem

Run $m$ independent tests at level $\alpha$ when every null is true. The chance of at least one false positive, the **family-wise error rate** (FWER), is

$$
\text{FWER} = 1 - (1 - \alpha)^m.
$$

With $\alpha = 0.05$ and $m = 100$, that is $1 - 0.95^{100} \approx 0.994$. A false positive is nearly guaranteed.

### Bonferroni

By the union bound, $P(\text{any false positive}) \le \sum_{i} P(\text{test } i \text{ false positive}) = m \cdot \alpha'$. Choosing $\alpha' = \alpha / m$ keeps the FWER at most $\alpha$, with no independence assumption.

> [!IMPORTANT]
> **Bonferroni:** to keep the family-wise error rate at $\alpha$ across $m$ tests, use the per-test threshold $\alpha / m$.

### Why $5 \times 10^{-8}$?

The human genome has millions of common variants, but nearby variants are correlated through **linkage disequilibrium** (LD, see [DNA, genes and variation](../../genomics-foundations/dna-genes-and-variation/)). Testing two variants in strong LD is nearly one test, not two. Studies of the LD structure in European-ancestry genomes (for example Pe'er et al., 2008) estimated that a GWAS of common variants carries a testing burden of roughly **one million independent tests**. Bonferroni then gives

$$
\frac{0.05}{10^{6}} = 5 \times 10^{-8},
$$

the conventional **genome-wide significance** threshold. In z-score terms this is $|z| > 5.45$. Populations with more genetic diversity and shorter LD blocks, such as many African-ancestry populations, have more effectively independent tests, and studies of rare variants also test more, so some authors argue for stricter thresholds in those settings.

### False discovery rate and Benjamini–Hochberg

Bonferroni controls the chance of **any** false positive. That is the right goal when a single error is costly. In exploratory work it is often too strict, and we would accept a few false leads to find many more true ones. The **false discovery rate** (FDR) is the expected fraction of discoveries that are false:

$$
\text{FDR} = \mathbb{E}\left[\frac{V}{\max(R, 1)}\right],
$$

where $R$ is the number of rejections and $V$ the number of false ones.

> [!IMPORTANT]
> **Benjamini–Hochberg (BH) procedure** at FDR level $q$:
> 1. Sort the $m$ p-values: $p_{(1)} \le p_{(2)} \le \dots \le p_{(m)}$.
> 2. Find the largest $k$ such that $p_{(k)} \le \dfrac{k}{m}\,q$.
> 3. Reject the hypotheses with the $k$ smallest p-values.
>
> For independent (or positively dependent) tests this controls the FDR at $q$.

The threshold grows with rank: the smallest p-value faces the Bonferroni bar $q/m$, the second $2q/m$, and so on. Note step 2 asks for the **largest** such $k$: a p-value above its own line can still be rejected if a later one dips below its line.

**Intuition.** If all $m$ nulls were true, p-values would be uniform, so about $m \cdot t$ of them would fall below any threshold $t$. If we reject the $k$ smallest using threshold $t = kq/m$, the expected number of false discoveries is at most $m \cdot kq/m = kq$, out of $k$ discoveries: a fraction $q$.

## Worked example

### A single allelic test

A case–control study genotypes 1,000 CAD cases and 1,000 controls at one SNP, giving 2,000 alleles per group.

| | Risk allele A | Other allele a | Total |
|---|---|---|---|
| Cases | 1,100 | 900 | 2,000 |
| Controls | 1,000 | 1,000 | 2,000 |
| Total | 2,100 | 1,900 | 4,000 |

**Allele frequencies.** Cases: $1100/2000 = 0.55$. Controls: $1000/2000 = 0.50$.

**Expected counts.** $E_{11} = 2000 \times 2100 / 4000 = 1050$, $E_{12} = 950$, $E_{21} = 1050$, $E_{22} = 950$.

**Chi-square.** Every cell is off by 50:

$$
X^2 = \frac{50^2}{1050} + \frac{50^2}{950} + \frac{50^2}{1050} + \frac{50^2}{950} = 2500\left(\frac{2}{1050} + \frac{2}{950}\right) \approx 2500 \times 0.004010 \approx 10.03.
$$

With 1 degree of freedom, $p \approx 0.0015$.

**Odds ratio and CI.** $\text{OR} = \dfrac{1100 \times 1000}{900 \times 1000} \approx 1.222$, so $\log \text{OR} \approx 0.2007$.

$$
\text{SE} = \sqrt{\tfrac{1}{1100} + \tfrac{1}{900} + \tfrac{1}{1000} + \tfrac{1}{1000}} = \sqrt{0.004020} \approx 0.0634.
$$

$95\%$ CI: $\exp(0.2007 \pm 1.96 \times 0.0634) = \exp(0.0764,\ 0.3250) \approx (1.08,\ 1.38)$.

**Verdict.** Significant at $0.05$, but nowhere near $5 \times 10^{-8}$. The Wald statistic is $z = 0.2007/0.0634 \approx 3.16$, while genome-wide significance needs $|z| > 5.45$. The power formula gives $\Phi(3.16 - 5.45) \approx 0.011$: a study this size would detect an effect like this at genome-wide significance only about 1% of the time. For 80% power we need $\theta/\text{SE} = 5.45 + 0.84 = 6.29$, that is $\text{SE} \approx 0.2007/6.29 \approx 0.0319$. That is half the current SE, so we need about four times the sample: roughly 4,000 cases and 4,000 controls. Real CAD GWAS enrol tens to hundreds of thousands of cases for exactly this reason.

### Relative risk versus odds ratio in a cohort

In a cohort of 2,000 people followed for ten years, 30 of 200 carriers and 90 of 1,800 non-carriers develop CAD.

- Risks: $30/200 = 0.15$ and $90/1800 = 0.05$. $\text{RR} = 3.0$.
- Odds: $30/170 \approx 0.1765$ and $90/1710 \approx 0.0526$. $\text{OR} \approx 3.35$.
- $\text{SE}(\log \text{RR}) = \sqrt{\tfrac{1}{30} - \tfrac{1}{200} + \tfrac{1}{90} - \tfrac{1}{1800}} \approx \sqrt{0.03889} \approx 0.197$, giving a 95% CI for RR of $\exp(1.0986 \pm 0.386) \approx (2.04,\ 4.42)$.

The OR exceeds the RR because a 15% risk is not rare.

### Benjamini–Hochberg by hand

Ten p-values from a candidate-gene study, already sorted, with $q = 0.05$ and $m = 10$, so the BH line is $k \times 0.005$:

| Rank $k$ | $p_{(k)}$ | $kq/m$ | $p_{(k)} \le kq/m$? |
|---|---|---|---|
| 1 | 0.0001 | 0.005 | yes |
| 2 | 0.0008 | 0.010 | yes |
| 3 | 0.0021 | 0.015 | yes |
| 4 | 0.0090 | 0.020 | yes |
| 5 | 0.0120 | 0.025 | yes |
| 6 | 0.0280 | 0.030 | yes |
| 7 | 0.0410 | 0.035 | no |
| 8 | 0.2000 | 0.040 | no |
| 9 | 0.4700 | 0.045 | no |
| 10 | 0.8800 | 0.050 | no |

The largest $k$ with "yes" is 6, so BH rejects six hypotheses. Bonferroni uses $0.05/10 = 0.005$ for every test and rejects only three (0.0001, 0.0008, 0.0021).

## In code

The first snippet reproduces the single-SNP worked example, including the power calculation.

```python
import numpy as np
from scipy import stats

# Allelic 2x2 table: rows = cases, controls; columns = risk allele A, other allele a
table = np.array([[1100,  900],
                  [1000, 1000]])

# Chi-square test by hand
row = table.sum(axis=1, keepdims=True)      # shape (2, 1)
col = table.sum(axis=0, keepdims=True)      # shape (1, 2)
expected = row @ col / table.sum()          # shape (2, 2)
chi2 = ((table - expected) ** 2 / expected).sum()
p = stats.chi2.sf(chi2, df=1)
print("expected:\n", expected)
print(f"chi2 = {chi2:.3f}, p = {p:.2e}")

# Same thing with scipy (no Yates continuity correction)
chi2_s, p_s, _, _ = stats.chi2_contingency(table, correction=False)
print(f"scipy: chi2 = {chi2_s:.3f}, p = {p_s:.2e}")

# Odds ratio with a 95% Wald confidence interval on the log scale
a, b = table[0]
c, d = table[1]
log_or = np.log((a * d) / (b * c))
se = np.sqrt(1/a + 1/b + 1/c + 1/d)
lo, hi = np.exp(log_or + np.array([-1.96, 1.96]) * se)
print(f"OR = {np.exp(log_or):.3f}, SE(log OR) = {se:.4f}, 95% CI = ({lo:.3f}, {hi:.3f})")
z = log_or / se
print(f"Wald z = {z:.2f}, z^2 = {z**2:.2f}")

# Power of this design at genome-wide significance
z_crit = stats.norm.isf(5e-8 / 2)
print(f"z threshold for p<5e-8: {z_crit:.2f}")
print(f"power at alpha=5e-8: {stats.norm.cdf(abs(z) - z_crit):.3f}")
print(f"power at alpha=0.05: {stats.norm.cdf(abs(z) - 1.96):.3f}")
```

```text
expected:
 [[1050.  950.]
 [1050.  950.]]
chi2 = 10.025, p = 1.54e-03
scipy: chi2 = 10.025, p = 1.54e-03
OR = 1.222, SE(log OR) = 0.0634, 95% CI = (1.079, 1.384)
Wald z = 3.16, z^2 = 10.02
z threshold for p<5e-8: 5.45
power at alpha=5e-8: 0.011
power at alpha=0.05: 0.886
```

The Wald $z^2$ (10.02) and the Pearson $X^2$ (10.03) nearly agree, as they should for a large table.

The second snippet simulates a small "GWAS" of 10,000 tests, 100 of which are real, and compares three decision rules.

```python
import numpy as np
from scipy import stats

rng = np.random.default_rng(7)
m, m_true = 10_000, 100

# z-statistics: null SNPs ~ N(0,1); true associations shifted by 4.5
z = rng.normal(size=m)
is_true = np.zeros(m, dtype=bool)
is_true[:m_true] = True
z[is_true] += 4.5
p = 2 * stats.norm.sf(np.abs(z))

def benjamini_hochberg(p, q=0.05):
    """Return a boolean mask of discoveries at FDR level q."""
    m = len(p)
    order = np.argsort(p)
    thresholds = q * np.arange(1, m + 1) / m
    below = p[order] <= thresholds
    k = np.max(np.nonzero(below)[0]) + 1 if below.any() else 0
    reject = np.zeros(m, dtype=bool)
    reject[order[:k]] = True
    return reject

rules = {
    "unadjusted p<0.05": p < 0.05,
    "Bonferroni": p < 0.05 / m,
    "BH, FDR 5%": benjamini_hochberg(p, 0.05),
}
for name, hits in rules.items():
    tp = np.sum(hits & is_true)
    fp = np.sum(hits & ~is_true)
    print(f"{name:18s} discoveries={hits.sum():4d}  true={tp:3d}  false={fp:3d}  "
          f"FDP={fp / max(hits.sum(), 1):.3f}")

# Cross-check with scipy's implementation (adjusted p-values)
q_adj = stats.false_discovery_control(p)
print("matches scipy:", np.array_equal(q_adj <= 0.05, rules["BH, FDR 5%"]))
```

```text
unadjusted p<0.05  discoveries= 602  true=100  false=502  FDP=0.834
Bonferroni         discoveries=  38  true= 38  false=  0  FDP=0.000
BH, FDR 5%         discoveries=  87  true= 82  false=  5  FDP=0.057
matches scipy: True
```

Without correction, 83% of "hits" are false. Bonferroni makes no false calls but misses 62 of the 100 real effects. BH finds more than twice as many real effects with a false discovery proportion close to the 5% target.

## Biomedical connection

The first wave of CAD GWAS in 2007 found the **9p21** locus at genome-wide significance in several independent studies at once, and that replication is part of why it is trusted (see [genetics of heart disease](../../genomics-foundations/genetics-of-heart-disease/)). Since then, sample sizes have grown into the hundreds of thousands, and the number of genome-wide significant CAD loci has grown into the hundreds. Most have small odds ratios, typically well under 1.2 per allele, which is exactly why such large samples are needed.

Three lessons carry forward into model building:

- **Significance is not importance.** A variant with $p = 10^{-30}$ and OR 1.05 explains very little risk on its own. Polygenic risk scores ([GWAS and PRS](../../genomics-foundations/gwas-and-polygenic-risk-scores/)) gain power by adding up many such small effects.
- **Selection inflates effects.** Variants that just cross a significance threshold tend to have overestimated effects (the "winner's curse"). Shrinkage methods for PRS partly correct this.
- **Your model evaluation is a hypothesis test too.** If you try 200 architectures and report the best test-set AUC, you have run 200 comparisons. Hold out a final test set you touch once, as in [model evaluation](../../classical-machine-learning/model-evaluation/).

> [!CAUTION]
> A statistically significant association between a variant and CAD in a population does not mean that a person who carries it will develop CAD, nor that the variant causes disease. Association can reflect linkage disequilibrium with the real causal variant, or confounding by ancestry.

## Practice

1. Explain in one sentence why "$p = 0.01$, so there is a 1% chance the null hypothesis is true" is wrong.

<details>
<summary>Answer</summary>

The p-value is $P(\text{data this extreme} \mid H_0)$, computed assuming $H_0$ is true; the probability that $H_0$ is true given the data is a different quantity, $P(H_0 \mid \text{data})$, which also depends on the prior plausibility of $H_0$.

</details>

2. In a case–control study, 300 of 500 cases and 250 of 500 controls carry a variant. Compute the odds ratio and its 95% Wald confidence interval.

<details>
<summary>Answer</summary>

Table: $a = 300$, $b = 200$ (cases: carriers, non-carriers), $c = 250$, $d = 250$. $\text{OR} = \frac{300 \times 250}{200 \times 250} = 1.5$. $\log 1.5 \approx 0.405$.

$\text{SE} = \sqrt{\tfrac{1}{300} + \tfrac{1}{200} + \tfrac{1}{250} + \tfrac{1}{250}} = \sqrt{0.003333 + 0.005 + 0.004 + 0.004} = \sqrt{0.016333} \approx 0.128$.

CI: $\exp(0.405 \pm 1.96 \times 0.128) = \exp(0.155,\ 0.656) \approx (1.17,\ 1.93)$.

</details>

3. You test 20 independent true null hypotheses at $\alpha = 0.05$. What is the probability of at least one false positive? What Bonferroni threshold keeps it at most 5%?

<details>
<summary>Answer</summary>

$1 - 0.95^{20} \approx 1 - 0.358 = 0.642$. Bonferroni threshold: $0.05/20 = 0.0025$.

</details>

4. Apply Benjamini–Hochberg at $q = 0.10$ to the sorted p-values $0.002, 0.009, 0.025, 0.031, 0.18$ ($m = 5$). How many are rejected?

<details>
<summary>Answer</summary>

Thresholds $kq/m = 0.02, 0.04, 0.06, 0.08, 0.10$. Compare: $0.002 \le 0.02$ yes; $0.009 \le 0.04$ yes; $0.025 \le 0.06$ yes; $0.031 \le 0.08$ yes; $0.18 \le 0.10$ no. Largest $k = 4$, so **four** are rejected.

</details>

5. A study has 50% power to detect a given effect at $\alpha = 5\times10^{-8}$. Roughly how much larger must it be to have 80% power?

<details>
<summary>Answer</summary>

50% power means $\theta/\text{SE} = z_{\text{crit}} = 5.45$. 80% power needs $\theta/\text{SE} = 5.45 + 0.84 = 6.29$. The SE must shrink by a factor $5.45/6.29 \approx 0.866$, and since $\text{SE} \propto 1/\sqrt{n}$, $n$ must grow by $(6.29/5.45)^2 \approx 1.33$, about 33% more participants.

</details>

## Further reading

- Wasserstein, R. L. & Lazar, N. A. (2016). The ASA statement on p-values: context, process, and purpose. *The American Statistician*, 70(2), 129–133.
- Benjamini, Y. & Hochberg, Y. (1995). Controlling the false discovery rate: a practical and powerful approach to multiple testing. *Journal of the Royal Statistical Society, Series B*, 57(1), 289–300.
- Risch, N. & Merikangas, K. (1996). The future of genetic studies of complex human diseases. *Science*, 273(5281), 1516–1517.
- Pe'er, I., Yelensky, R., Altshuler, D. & Daly, M. J. (2008). Estimation of the multiple testing burden for genomewide association studies of nearly all common variants. *Genetic Epidemiology*, 32(4), 381–385.
- Agresti, A. *Categorical Data Analysis*, 3rd ed. Wiley, 2013.
