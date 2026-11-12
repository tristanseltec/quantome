+++
summary = "Describe genotype counts, read depths and clinical measurements with the right probability distribution, and derive maximum-likelihood estimates that turn into the loss functions used to train models."
+++

# Distributions and Likelihood

Genomic data is noisy in very regular ways. How many copies of a risk allele you carry follows a **binomial** distribution. How many sequencing reads land on a given base follows, roughly, a **Poisson** distribution. Your LDL cholesterol, averaged over many small genetic and lifestyle effects, looks **normal**. If you know these shapes you can say how surprising an observation is, and you can fit parameters to data by **maximum likelihood**.

Maximum likelihood is also the bridge from statistics to machine learning. The binary cross-entropy you will minimise to train a heart-disease classifier is a negative log-likelihood under a Bernoulli model. Mean squared error is a negative log-likelihood under a normal model. This chapter derives both.

## Key ideas

### Random variables, expectation and variance

A **random variable** $X$ is a number determined by a random outcome. A **discrete** random variable has a **probability mass function** (pmf) $p(x) = P(X = x)$. A **continuous** one has a **probability density function** (pdf) $f(x)$, where probabilities are areas: $P(a \le X \le b) = \int_a^b f(x)\,dx$.

The **expectation** (mean) is the probability-weighted average:

$$
\mathbb{E}[X] = \sum_x x\,p(x) \quad\text{or}\quad \mathbb{E}[X] = \int x\,f(x)\,dx.
$$

The **variance** measures spread around the mean:

$$
\operatorname{Var}(X) = \mathbb{E}\big[(X - \mathbb{E}X)^2\big] = \mathbb{E}[X^2] - (\mathbb{E}X)^2.
$$

The standard deviation is $\sqrt{\operatorname{Var}(X)}$, in the same units as $X$.

> [!IMPORTANT]
> **Rules you will use constantly.** For constants $a, b$ and random variables $X, Y$:
> $$\mathbb{E}[aX + b] = a\,\mathbb{E}[X] + b, \qquad \mathbb{E}[X + Y] = \mathbb{E}[X] + \mathbb{E}[Y]$$
> $$\operatorname{Var}(aX + b) = a^2 \operatorname{Var}(X), \qquad \operatorname{Var}(X + Y) = \operatorname{Var}(X) + \operatorname{Var}(Y) \text{ if } X, Y \text{ independent.}$$

Linearity of expectation holds **always**, even for dependent variables. The variance-of-a-sum rule needs independence (in general you add $2\operatorname{Cov}(X,Y)$).

### Bernoulli

A **Bernoulli** variable takes value 1 with probability $p$ and 0 otherwise: one coin flip, one chromosome carrying or not carrying an allele, one person who does or does not develop CAD.

$$
P(X = x) = p^x (1-p)^{1-x}, \quad x \in \{0, 1\}.
$$

That compact formula gives $p$ when $x=1$ and $1-p$ when $x = 0$. It will matter when we take logs. Mean: $\mathbb{E}[X] = 0\cdot(1-p) + 1\cdot p = p$. Since $X^2 = X$, $\mathbb{E}[X^2] = p$, so $\operatorname{Var}(X) = p - p^2 = p(1-p)$.

### Binomial: allele counts

Add up $n$ independent Bernoulli($p$) variables and you get a **binomial** count $K \sim \text{Bin}(n, p)$:

$$
P(K = k) = \binom{n}{k} p^k (1-p)^{n-k}, \qquad k = 0, 1, \dots, n.
$$

The $\binom{n}{k}$ counts the orderings, as in [counting and probability](../../statistics-and-counting/counting-and-probability/). By linearity, $\mathbb{E}[K] = np$, and by independence, $\operatorname{Var}(K) = np(1-p)$.

**Genotypes.** You have two copies of each autosome, one from each parent. If a variant's alternative allele has frequency $p$ in the population and the two copies are drawn independently (the Hardy–Weinberg assumption, derived in [DNA, genes and variation](../../genomics-foundations/dna-genes-and-variation/)), then your **dosage**, the number of alternative alleles you carry, is $\text{Bin}(2, p)$:

| Dosage $k$ | Genotype | Probability |
|---|---|---|
| 0 | ref/ref | $(1-p)^2$ |
| 1 | ref/alt | $2p(1-p)$ |
| 2 | alt/alt | $p^2$ |

Mean dosage $2p$, variance $2p(1-p)$. This variance appears again when we compute how much a SNP contributes to the variance of a polygenic score.

### Poisson: sequencing read depth

Sequencing chops the genome into many short reads at random positions. Suppose we sequence $N$ reads of length $L$ from a genome of length $G$. A given base is covered by a given read with a tiny probability $L/G$. The number of reads covering that base is then $\text{Bin}(N, L/G)$ with mean $c = NL/G$, the **coverage**.

When $N$ is huge and $L/G$ is tiny with $c$ fixed, the binomial converges to the **Poisson** distribution:

$$
P(D = d) = \frac{e^{-c}\,c^d}{d!}, \qquad d = 0, 1, 2, \dots
$$

*Why.* With $q = c/N$, $\binom{N}{d} q^d (1-q)^{N-d} = \frac{N(N-1)\cdots(N-d+1)}{N^d}\cdot\frac{c^d}{d!}\cdot\left(1 - \frac{c}{N}\right)^{N-d}$. As $N \to \infty$ the first fraction tends to 1 and $\left(1 - c/N\right)^{N} \to e^{-c}$.

A Poisson variable has $\mathbb{E}[D] = \operatorname{Var}(D) = c$. In particular, the fraction of bases with **zero** coverage is $e^{-c}$. This is the core of the Lander–Waterman model in [sequencing data](../../genomics-foundations/sequencing-data/).

> [!NOTE]
> Real read depth is **overdispersed**: its variance exceeds its mean because GC content, mappability and library preparation make some regions easier to sequence. The Poisson model is a baseline; the negative binomial is a common next step.

### Normal and the central limit theorem

The **normal** (Gaussian) distribution $\mathcal{N}(\mu, \sigma^2)$ has density

$$
f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\!\left(-\frac{(x - \mu)^2}{2\sigma^2}\right),
$$

with mean $\mu$ and variance $\sigma^2$. About 68% of the mass lies within $\mu \pm \sigma$, 95% within $\mu \pm 1.96\sigma$. If $X \sim \mathcal{N}(\mu, \sigma^2)$, the **z-score** $Z = (X - \mu)/\sigma$ is standard normal $\mathcal{N}(0,1)$.

Why is the normal everywhere? Because of the **central limit theorem** (CLT).

> [!IMPORTANT]
> **Central limit theorem.** If $X_1, \dots, X_n$ are independent and identically distributed with mean $\mu$ and finite variance $\sigma^2$, then for large $n$ the sample mean is approximately normal:
> $$\bar{X} = \frac{1}{n}\sum_{i=1}^n X_i \;\approx\; \mathcal{N}\!\left(\mu, \frac{\sigma^2}{n}\right).$$

The quantity $\sigma/\sqrt{n}$ is the **standard error** of the mean. Two consequences matter for us:

- **Estimates are approximately normal.** Allele frequency estimates, regression coefficients and log odds ratios are all (functions of) averages, so we can build confidence intervals and z-tests from them (next chapter).
- **Polygenic traits are approximately normal.** A trait influenced by thousands of variants, each adding a small independent amount, is a large sum. Fisher's 1918 paper used exactly this argument to reconcile Mendelian inheritance with continuously varying traits like height. Polygenic risk scores are sums of thousands of terms and are roughly normal too.

The binomial is itself a sum, so $\text{Bin}(n,p) \approx \mathcal{N}(np, np(1-p))$ when $np$ and $n(1-p)$ are both reasonably large (a common rule of thumb is at least 10).

## Maximum likelihood estimation

### The likelihood function

A model gives the probability of data $x$ for each parameter value $\theta$. Read the same formula the other way round, as a function of $\theta$ with the data fixed, and it is called the **likelihood**:

$$
\mathcal{L}(\theta) = P(\text{data} \mid \theta) = \prod_{i=1}^{n} p(x_i \mid \theta) \quad \text{for independent observations.}
$$

The **maximum likelihood estimate** (MLE) $\hat\theta$ is the parameter value that makes the observed data most probable.

Products of many small numbers underflow, and products are awkward to differentiate. Since $\log$ is increasing, maximising $\mathcal{L}$ is the same as maximising the **log-likelihood**

$$
\ell(\theta) = \log \mathcal{L}(\theta) = \sum_{i=1}^{n} \log p(x_i \mid \theta).
$$

> [!WARNING]
> A likelihood is not a probability distribution over $\theta$. It need not integrate to 1 over $\theta$. To get a distribution over parameters you need a prior and Bayes' theorem.

### MLE for the Bernoulli

Data: $x_1, \dots, x_n \in \{0,1\}$, with $k = \sum x_i$ ones. Then

$$
\ell(p) = \sum_{i=1}^{n} \big[x_i \log p + (1 - x_i)\log(1-p)\big] = k \log p + (n - k)\log(1-p).
$$

Differentiate (see [derivatives and gradients](../../calculus-and-optimization/derivatives-and-gradients/)) and set to zero:

$$
\frac{d\ell}{dp} = \frac{k}{p} - \frac{n-k}{1-p} = 0 \;\Longrightarrow\; k(1-p) = (n-k)p \;\Longrightarrow\; \hat p = \frac{k}{n}.
$$

The second derivative $-k/p^2 - (n-k)/(1-p)^2$ is negative, so this is a maximum. The MLE is the sample proportion, which is what intuition says.

### MLE for the normal

Data $y_1, \dots, y_n$, model $\mathcal{N}(\mu, \sigma^2)$. Taking the log of the density,

$$
\ell(\mu, \sigma^2) = -\frac{n}{2}\log(2\pi\sigma^2) - \frac{1}{2\sigma^2}\sum_{i=1}^{n}(y_i - \mu)^2.
$$

**For $\mu$.** Only the sum depends on $\mu$:

$$
\frac{\partial \ell}{\partial \mu} = \frac{1}{\sigma^2}\sum_{i=1}^{n}(y_i - \mu) = 0 \;\Longrightarrow\; \hat\mu = \frac{1}{n}\sum_{i=1}^{n} y_i = \bar y.
$$

**For $\sigma^2$.** Treat $s = \sigma^2$ as the variable:

$$
\frac{\partial \ell}{\partial s} = -\frac{n}{2s} + \frac{1}{2s^2}\sum_{i=1}^{n}(y_i - \mu)^2 = 0 \;\Longrightarrow\; \hat\sigma^2 = \frac{1}{n}\sum_{i=1}^{n}(y_i - \bar y)^2.
$$

Notice the divisor $n$, not $n-1$. The MLE of the variance is slightly biased low. The familiar "sample variance" with $n-1$ corrects that bias. For large $n$ the difference is negligible.

### From log-likelihood to loss functions

Now let the parameter depend on features. In a classifier, a model $f_{\mathbf{w}}(\mathbf{x}_i)$ outputs $q_i$, the predicted probability that person $i$ has CAD, and $y_i \in \{0,1\}$ is the label. Under a Bernoulli model with $p = q_i$ for person $i$, the average negative log-likelihood is

$$
-\frac{1}{n}\ell(\mathbf{w}) = -\frac{1}{n}\sum_{i=1}^{n}\big[y_i \log q_i + (1-y_i)\log(1-q_i)\big],
$$

which is exactly the **binary cross-entropy** loss.

In regression, a model predicts $\hat y_i = f_{\mathbf{w}}(\mathbf{x}_i)$ and we assume $y_i \sim \mathcal{N}(\hat y_i, \sigma^2)$ with fixed $\sigma$. The negative log-likelihood is a constant plus $\frac{1}{2\sigma^2}\sum (y_i - \hat y_i)^2$, so maximising likelihood is minimising **squared error**.

> [!IMPORTANT]
> **Training a model by minimising a loss is usually maximum likelihood in disguise.**
> Bernoulli likelihood $\leftrightarrow$ binary cross-entropy. Normal likelihood $\leftrightarrow$ mean squared error.

The [loss functions](../../calculus-and-optimization/loss-functions/) chapter uses these losses. The [information theory](../../probability-and-statistics/information-theory/) chapter explains the name "cross-entropy".

## Worked example

**(a) Genotype probabilities.** A variant has alternative-allele frequency $p = 0.3$. Under Hardy–Weinberg, the dosage is $\text{Bin}(2, 0.3)$:

- $P(0) = 0.7^2 = 0.49$
- $P(1) = 2 \times 0.3 \times 0.7 = 0.42$
- $P(2) = 0.3^2 = 0.09$

Check: $0.49 + 0.42 + 0.09 = 1$. Mean $= 0 \times 0.49 + 1 \times 0.42 + 2 \times 0.09 = 0.60 = 2p$. $\mathbb{E}[K^2] = 0.42 + 4 \times 0.09 = 0.78$, so $\operatorname{Var} = 0.78 - 0.36 = 0.42 = 2p(1-p)$. ✓

**(b) Read depth.** A region is sequenced at average coverage $c = 10$. Under the Poisson model, the chance a base has depth 2 or less is

$$
e^{-10}\left(1 + 10 + \frac{10^2}{2}\right) = 61\,e^{-10} \approx 61 \times 4.54\times10^{-5} \approx 0.0028.
$$

About 0.3% of bases would have too few reads to call a genotype confidently. At $c=30$ this becomes vanishingly small, which is one reason clinical genome sequencing targets around 30× or more.

**(c) An MLE by hand.** We sequence 10 chromosomes and find the alternative allele on 3 of them. The log-likelihood is $\ell(p) = 3\log p + 7\log(1-p)$. Setting $\frac{3}{p} - \frac{7}{1-p} = 0$ gives $3 - 3p = 7p$, so $\hat p = 0.3$. Compare two candidate values:

- $\ell(0.3) = 3\ln 0.3 + 7\ln 0.7 \approx 3(-1.204) + 7(-0.357) \approx -6.109$
- $\ell(0.5) = 10 \ln 0.5 \approx -6.931$

So $p = 0.3$ makes the data $e^{-6.109 + 6.931} = e^{0.822} \approx 2.3$ times more probable than $p = 0.5$. That ratio is a **likelihood ratio**, the same idea as in [Bayes' theorem](../../probability-and-statistics/probability-and-bayes-theorem/).

## In code

First we check the distributions by simulation: genotype dosages, Poisson read depth and the CLT.

```python
import numpy as np
from math import comb, exp, factorial

rng = np.random.default_rng(42)

# Binomial: alt-allele count in a diploid genotype with allele frequency p = 0.3
p = 0.3
dosage = rng.binomial(n=2, p=p, size=100_000)
print("P(0,1,2) theory :", [round(comb(2, k) * p**k * (1 - p)**(2 - k), 3) for k in range(3)])
print("P(0,1,2) sampled:", np.round(np.bincount(dosage) / dosage.size, 3))
print("mean dosage", dosage.mean().round(3), "theory", 2 * p,
      "| var", dosage.var().round(3), "theory", 2 * p * (1 - p))

# Poisson: read depth at a site when average coverage is 30x
lam = 30
depth = rng.poisson(lam, size=100_000)
p_lt_10 = sum(exp(-lam) * lam**k / factorial(k) for k in range(10))
print(f"P(depth < 10) theory {p_lt_10:.2e}, sampled {(depth < 10).mean():.2e}")
print("mean depth", depth.mean().round(2), "var", depth.var().round(2))

# Central limit theorem: means of 50 skewed (exponential) draws look normal
means = rng.exponential(scale=1.0, size=(20_000, 50)).mean(axis=1)
print("CLT: mean of means", means.mean().round(3), "sd", means.std().round(4),
      "theory sd", round(1 / np.sqrt(50), 4))
within = np.mean(np.abs(means - 1) < 1.96 / np.sqrt(50))
print("fraction within 1.96 SE:", within.round(3))
```

```text
P(0,1,2) theory : [0.49, 0.42, 0.09]
P(0,1,2) sampled: [0.487 0.423 0.09 ]
mean dosage 0.603 theory 0.6 | var 0.42 theory 0.42
P(depth < 10) theory 7.12e-06, sampled 1.00e-05
mean depth 29.99 var 30.11
CLT: mean of means 0.999 sd 0.1408 theory sd 0.1414
fraction within 1.96 SE: 0.953
```

The exponential distribution is very skewed, yet averages of 50 draws fall within $\pm 1.96$ standard errors 95% of the time, as the CLT predicts. (The sampled $P(\text{depth} < 10)$ is based on only one event in 100,000 draws, so it is noisy.)

Next, maximum likelihood. We confirm the closed-form MLEs against brute-force search, and confirm that the negative log-likelihood equals cross-entropy and is minimised where squared error is.

```python
import numpy as np

rng = np.random.default_rng(1)

# --- Bernoulli MLE: 0/1 outcomes (e.g. carries the risk allele on one chromosome) ---
x = rng.binomial(1, 0.27, size=200)
grid = np.linspace(0.01, 0.99, 981)
loglik = x.sum() * np.log(grid) + (len(x) - x.sum()) * np.log(1 - grid)
print("closed-form MLE  :", x.mean())
print("grid-search MLE  :", grid[np.argmax(loglik)].round(3))

# Average negative log-likelihood == binary cross-entropy
def bce(y, q):
    return -np.mean(y * np.log(q) + (1 - y) * np.log(1 - q))
q_hat = x.mean()
print("mean NLL at MLE  :", round(-loglik.max() / len(x), 4), "| BCE:", round(bce(x, q_hat), 4))

# --- Normal MLE: LDL cholesterol-like values (mmol/L), synthetic ---
y = rng.normal(loc=3.4, scale=0.9, size=500)
mu_hat = y.mean()
sigma2_hat = np.mean((y - mu_hat) ** 2)          # MLE divides by n
print("mu_hat", mu_hat.round(3), "sigma_hat", np.sqrt(sigma2_hat).round(3),
      "| unbiased sd (n-1)", y.std(ddof=1).round(3))

def normal_nll(mu, sigma, y):
    return 0.5 * len(y) * np.log(2 * np.pi * sigma**2) + np.sum((y - mu) ** 2) / (2 * sigma**2)

# Minimising NLL over mu (fixed sigma) is minimising squared error
mus = np.linspace(2.5, 4.5, 2001)
nll = [normal_nll(m, 0.9, y) for m in mus]
mse = [np.mean((y - m) ** 2) for m in mus]
print("argmin NLL", mus[np.argmin(nll)].round(3), "| argmin MSE", mus[np.argmin(mse)].round(3))
```

```text
closed-form MLE  : 0.285
grid-search MLE  : 0.285
mean NLL at MLE  : 0.5976 | BCE: 0.5976
mu_hat 3.372 sigma_hat 0.886 | unbiased sd (n-1) 0.887
argmin NLL 3.372 | argmin MSE 3.372
```

## Biomedical connection

Each distribution in this chapter shows up in the DNA-to-heart-disease pipeline:

- **Bernoulli** for the outcome: did this person have a coronary event within ten years? Our classifiers will be trained by maximising the Bernoulli likelihood, that is, by minimising binary cross-entropy.
- **Binomial** for genotypes: dosage 0, 1 or 2 at each variant, with mean $2p$ and variance $2p(1-p)$. Genotype calling from sequencing reads also uses binomial reasoning: in a heterozygote, each read shows the alternative allele with probability about 1/2.
- **Poisson** for read depth, which tells us how much sequencing we need before we can trust a genotype call.
- **Normal** for continuous risk factors (LDL cholesterol, blood pressure) and, via the CLT, for polygenic risk scores, which add up thousands of small effects. That is why a PRS can be summarised by a z-score and a percentile, as in [GWAS and polygenic risk scores](../../genomics-foundations/gwas-and-polygenic-risk-scores/).

> [!CAUTION]
> Model assumptions are claims about biology and measurement, and they fail in specific places. Read depth is overdispersed. Genotypes deviate from Hardy–Weinberg in structured populations. Lipid levels are skewed in people with monogenic disorders. Check the fit before trusting a likelihood-based conclusion.

## Practice

1. A variant has alternative-allele frequency 0.1. Under Hardy–Weinberg, what fraction of people are heterozygous, what fraction are homozygous for the alternative allele, and what is the mean dosage?

<details>
<summary>Answer</summary>

Heterozygous: $2 \times 0.1 \times 0.9 = 0.18$. Homozygous alternative: $0.1^2 = 0.01$. Mean dosage $= 2p = 0.2$.

</details>

2. A genome is sequenced at 8× average coverage. Under the Poisson model, what fraction of bases have zero reads? What fraction have at most one read?

<details>
<summary>Answer</summary>

$P(0) = e^{-8} \approx 3.35 \times 10^{-4}$. $P(\le 1) = e^{-8}(1 + 8) = 9e^{-8} \approx 3.02 \times 10^{-3}$.

</details>

3. Derive the MLE of the Poisson rate $\lambda$ from observed depths $d_1, \dots, d_n$. Apply it to depths 28, 31, 35, 26.

<details>
<summary>Answer</summary>

$\ell(\lambda) = \sum_i \left(-\lambda + d_i \log\lambda - \log d_i!\right)$. Then $\ell'(\lambda) = -n + \frac{1}{\lambda}\sum_i d_i = 0$, so $\hat\lambda = \bar d$. Here $\hat\lambda = (28+31+35+26)/4 = 120/4 = 30$.

</details>

4. $K \sim \text{Bin}(100, 0.3)$. Use the normal approximation (with continuity correction) to estimate $P(K \ge 40)$.

<details>
<summary>Answer</summary>

Mean $30$, variance $100 \times 0.3 \times 0.7 = 21$, sd $\approx 4.58$. $P(K \ge 40) \approx P\!\left(Z \ge \frac{39.5 - 30}{4.58}\right) = P(Z \ge 2.07) \approx 0.019$. The exact binomial value is about $0.021$.

</details>

5. A toy risk score is $S = 0.2\,G_1 + 0.1\,G_2$, where $G_1, G_2$ are independent dosages with allele frequencies $0.5$ and $0.2$. Find $\mathbb{E}[S]$ and $\operatorname{Var}(S)$.

<details>
<summary>Answer</summary>

$\mathbb{E}[S] = 0.2(2 \times 0.5) + 0.1(2 \times 0.2) = 0.2 + 0.04 = 0.24$.

$\operatorname{Var}(S) = 0.2^2 \times 2(0.5)(0.5) + 0.1^2 \times 2(0.2)(0.8) = 0.04 \times 0.5 + 0.01 \times 0.32 = 0.0232$.

</details>

## Further reading

- Blitzstein, J. K. & Hwang, J. *Introduction to Probability*, 2nd ed. CRC Press, 2019. Chapters 3–5 and 10 (distributions and the CLT).
- Wasserman, L. *All of Statistics: A Concise Course in Statistical Inference*. Springer, 2004. Chapter 9 covers maximum likelihood.
- Fisher, R. A. (1918). The correlation between relatives on the supposition of Mendelian inheritance. *Transactions of the Royal Society of Edinburgh*, 52, 399–433.
- Lander, E. S. & Waterman, M. S. (1988). Genomic mapping by fingerprinting random clones: a mathematical analysis. *Genomics*, 2(3), 231–239.
