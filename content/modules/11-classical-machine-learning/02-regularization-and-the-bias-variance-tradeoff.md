+++
summary = "Derive the bias–variance decomposition, explain why p ≫ n breaks ordinary regression, derive ridge in closed form, see why lasso gives sparse solutions, and choose the penalty by cross-validation on a synthetic genotype matrix."
+++

# Regularization and the Bias–Variance Tradeoff

A genotyping array measures hundreds of thousands of variants; imputation turns that into millions. Even the largest cohorts have far fewer *cases* of early coronary artery disease than they have variants. In this regime, $p \gg n$, ordinary least squares and unpenalised logistic regression do not just perform badly: they have infinitely many perfect solutions on the training data, nearly all of them useless on new people.

**Regularization** is the cure. It adds a penalty that pulls coefficients towards zero, deliberately introducing a little bias to buy a large reduction in variance. The same idea reappears throughout deep learning as weight decay, dropout and early stopping, so the intuition you build here will carry forward to [training deep networks](../../neural-networks/training-deep-networks/).

## Key ideas

### Overfitting

A model **overfits** when it fits the noise in its training data rather than the signal, so that its training error is low but its error on new data is high. Two ingredients make overfitting likely: a flexible model (many parameters) and little data. A model with as many free coefficients as there are people can reproduce every training outcome exactly, whatever the truth.

### The bias–variance decomposition

Suppose outcomes are generated as $y = f(\mathbf x) + \varepsilon$, with $\mathbb E[\varepsilon] = 0$, $\operatorname{Var}(\varepsilon) = \sigma^2$, and $\varepsilon$ independent of everything else. We train a model on a random training set $\mathcal D$ and get a prediction $\hat f(\mathbf x)$, which is itself random because $\mathcal D$ is. Fix a test point $\mathbf x$ and write $f = f(\mathbf x)$, $\hat f = \hat f(\mathbf x)$, and $\bar f = \mathbb E_{\mathcal D}[\hat f]$ for the *average* prediction over many possible training sets.

**Derivation.** Add and subtract $\bar f$:

$$
y - \hat f = \underbrace{(f - \bar f)}_{a} + \underbrace{(\bar f - \hat f)}_{b} + \varepsilon.
$$

Square and take the expectation over both $\mathcal D$ and the new noise $\varepsilon$:

$$
\mathbb E[(y - \hat f)^2] = a^2 + \mathbb E[b^2] + \mathbb E[\varepsilon^2] + 2a\,\mathbb E[b] + 2a\,\mathbb E[\varepsilon] + 2\,\mathbb E[b\,\varepsilon].
$$

The cross terms vanish: $a$ is a constant and $\mathbb E[b] = \bar f - \mathbb E[\hat f] = 0$; $\mathbb E[\varepsilon] = 0$; and $b$ depends only on $\mathcal D$ while $\varepsilon$ is independent of $\mathcal D$, so $\mathbb E[b\varepsilon] = \mathbb E[b]\,\mathbb E[\varepsilon] = 0$. What remains is

> [!IMPORTANT]
> **Bias–variance decomposition**
> $$\mathbb E\big[(y - \hat f(\mathbf x))^2\big] = \underbrace{\big(f(\mathbf x) - \bar f(\mathbf x)\big)^2}_{\text{bias}^2} + \underbrace{\mathbb E\big[(\hat f(\mathbf x) - \bar f(\mathbf x))^2\big]}_{\text{variance}} + \underbrace{\sigma^2}_{\text{irreducible noise}}.$$

- **Bias** is systematic error: how far the average model is from the truth. Too-simple or heavily penalised models have high bias.
- **Variance** is instability: how much the prediction would change with a different training sample. Flexible, lightly penalised models fitted to small data have high variance.
- **Noise** $\sigma^2$ cannot be removed by any model. For disease risk it is large: two people with identical genomes and identical clinical data can still have different outcomes.

Regularization trades one for the other. Total error is usually U-shaped in the penalty strength, and the bottom of the U is what we look for.

### The $p \gg n$ problem

If $X$ is $n \times p$ with $p > n$, then $\operatorname{rank}(X^\top X) \le n < p$, so $X^\top X$ is **singular** and the [normal equations](../../classical-machine-learning/linear-and-logistic-regression/) have infinitely many solutions. Most of them fit the training data *exactly* ($X\boldsymbol\beta = \mathbf y$), so the training $R^2$ is 1 and tells you nothing. In logistic regression the analogue is complete separation: coefficients run off to infinity.

Genomics adds two complications:

- **Linkage disequilibrium (LD).** Nearby SNPs are correlated because they are inherited together. Columns of $X$ are nearly collinear, so even when $p < n$, $X^\top X$ is ill-conditioned and individual coefficients are unstable.
- **Most effects are tiny.** For a polygenic trait like CAD, thousands of variants each have very small effects. Estimating each precisely is impossible; the goal is a good *combined* prediction.

### Ridge regression

Add a squared ($L_2$) penalty:

$$
L_{\text{ridge}}(\boldsymbol\beta) = \lVert \mathbf y - X\boldsymbol\beta\rVert^2 + \lambda \lVert \boldsymbol\beta\rVert^2, \qquad \lambda > 0.
$$

The gradient is $-2X^\top(\mathbf y - X\boldsymbol\beta) + 2\lambda\boldsymbol\beta$. Setting it to zero:

> [!IMPORTANT]
> **Ridge closed form**
> $$(X^\top X + \lambda I)\,\hat{\boldsymbol\beta}_{\text{ridge}} = X^\top \mathbf y \qquad\Longrightarrow\qquad \hat{\boldsymbol\beta}_{\text{ridge}} = (X^\top X + \lambda I)^{-1} X^\top \mathbf y.$$

$X^\top X$ has eigenvalues $d_j^2 \ge 0$; adding $\lambda I$ shifts each to $d_j^2 + \lambda > 0$, so the matrix is **always invertible**, even when $p \gg n$. Using the [SVD](../../linear-algebra/eigenvectors-svd-and-pca/) $X = UDV^\top$, the ridge fit is

$$
X\hat{\boldsymbol\beta}_{\text{ridge}} = \sum_j \mathbf u_j \frac{d_j^2}{d_j^2 + \lambda}\,\mathbf u_j^\top \mathbf y.
$$

Each principal direction of the data is shrunk by the factor $d_j^2/(d_j^2 + \lambda)$: directions with large variance (big $d_j$) are barely touched, low-variance directions (where estimates are noisy) are shrunk hard. Ridge keeps **every** coefficient non-zero, and it spreads weight across correlated features rather than choosing one.

Two practical rules: **standardise** features first (the penalty treats all coefficients alike, so their scales must be comparable), and **do not penalise the intercept**.

### Lasso and sparsity

Replace the squared penalty by an absolute-value ($L_1$) penalty:

$$
L_{\text{lasso}}(\boldsymbol\beta) = \tfrac12\lVert \mathbf y - X\boldsymbol\beta\rVert^2 + \lambda \lVert \boldsymbol\beta\rVert_1, \qquad \lVert\boldsymbol\beta\rVert_1 = \sum_j \lvert\beta_j\rvert.
$$

There is no closed form, but the one-dimensional case shows what happens. Minimise $g(\beta) = \tfrac12(b - \beta)^2 + \lambda\lvert\beta\rvert$, where $b$ is the unpenalised estimate:

- If $\beta > 0$: $g'(\beta) = \beta - b + \lambda = 0$ gives $\beta = b - \lambda$, valid only if $b > \lambda$.
- If $\beta < 0$: $\beta = b + \lambda$, valid only if $b < -\lambda$.
- Otherwise ($\lvert b\rvert \le \lambda$) neither works, and the minimum is at the kink, $\beta = 0$.

> [!IMPORTANT]
> **Soft thresholding** (lasso with an orthonormal design, $X^\top X = I$)
> $$\hat\beta_j = S(b_j, \lambda) = \operatorname{sign}(b_j)\,\max(\lvert b_j\rvert - \lambda,\ 0).$$
> Compare ridge in the same setting (with penalty $\lambda\lVert\boldsymbol\beta\rVert^2$ on $\lVert\mathbf y - X\boldsymbol\beta\rVert^2$): $\hat\beta_j = b_j/(1+\lambda)$, which shrinks but never reaches zero.

Lasso sets small coefficients **exactly** to zero: it does variable selection and fitting at once. For general $X$, **coordinate descent** applies soft thresholding to one coefficient at a time, cycling until convergence; this is how scikit-learn and glmnet fit lasso.

**The geometric picture.** Penalised regression is equivalent to minimising the squared error subject to a budget: $\lVert\boldsymbol\beta\rVert_1 \le t$ (lasso) or $\lVert\boldsymbol\beta\rVert_2^2 \le t$ (ridge). In two dimensions the least-squares contours are ellipses around $\hat{\boldsymbol\beta}_{\text{OLS}}$. We expand an ellipse until it first touches the constraint region. The ridge region is a disc, smooth everywhere, so the touching point is generically off the axes. The lasso region is a **diamond with corners on the axes**, and an expanding ellipse very often hits a corner first, where one coordinate is exactly zero. In high dimensions the $L_1$ ball has even more corners and edges, so sparsity is the typical outcome.

**The Bayesian picture.** Ridge is the posterior mode (MAP estimate) under a Gaussian prior $\beta_j \sim \mathcal N(0, \tau^2)$; lasso is the MAP under a Laplace (double-exponential) prior, which has a sharp peak at zero. The prior encodes the belief "most effects are small" or "most effects are zero".

### Elastic net

Lasso has two weaknesses: with $p > n$ it can select at most $n$ variables, and among a group of highly correlated features (SNPs in strong LD) it tends to pick one more or less arbitrarily. The **elastic net** mixes both penalties:

$$
L_{\text{EN}}(\boldsymbol\beta) = \tfrac12\lVert\mathbf y - X\boldsymbol\beta\rVert^2 + \lambda_1\lVert\boldsymbol\beta\rVert_1 + \tfrac{\lambda_2}{2}\lVert\boldsymbol\beta\rVert^2.
$$

It keeps lasso's sparsity but, thanks to the ridge part, tends to give correlated features similar coefficients (the "grouping effect"). In scikit-learn the two are parametrised by an overall strength `alpha` and a mixing proportion `l1_ratio` (1 = lasso, 0 = ridge).

### Choosing λ by cross-validation

$\lambda$ is a **hyperparameter**: it cannot be chosen by minimising training error (that always picks $\lambda = 0$). Instead:

1. Choose a grid of values, typically log-spaced (e.g. $10^{-3}$ to $10^{3}$).
2. Split the training data into $K$ folds. For each $\lambda$ and each fold, fit on the other $K-1$ folds and measure error on the held-out fold.
3. Average across folds and pick the $\lambda$ with the lowest CV error. A popular, more conservative alternative is the **one-standard-error rule**: the largest $\lambda$ whose CV error is within one standard error of the minimum.
4. Refit on all training data with that $\lambda$, then evaluate **once** on a separate test set.

Fitting along the whole grid traces the **regularization path**: how each coefficient changes as $\lambda$ decreases from "everything zero" to "barely penalised". Warm starts make computing the full path barely more expensive than a single fit. The details of honest validation are the subject of [model evaluation](../../classical-machine-learning/model-evaluation/).

## Worked example

Assume an orthonormal design ($X^\top X = I$), so the penalised estimates are simple functions of the ordinary least-squares estimates. Let

$$
\mathbf b = \hat{\boldsymbol\beta}_{\text{OLS}} = (2.0,\ 0.5,\ -0.3).
$$

**Ridge**, $\lambda = 0.4$ (objective $\lVert\mathbf y - X\boldsymbol\beta\rVert^2 + \lambda\lVert\boldsymbol\beta\rVert^2$): each coefficient becomes $b_j/1.4$.

$$
\hat{\boldsymbol\beta}_{\text{ridge}} = (1.429,\ 0.357,\ -0.214).
$$

All shrink by the same factor; none is zero.

**Lasso**, $\lambda = 0.4$ (objective $\tfrac12\lVert\mathbf y - X\boldsymbol\beta\rVert^2 + \lambda\lVert\boldsymbol\beta\rVert_1$): subtract 0.4 from each magnitude, flooring at 0.

$$
\hat{\boldsymbol\beta}_{\text{lasso}} = (2.0 - 0.4,\ 0.5 - 0.4,\ 0) = (1.6,\ 0.1,\ 0).
$$

The large effect is shifted by a constant 0.4 (lasso's characteristic bias on large coefficients), the medium one is nearly removed, and the smallest is eliminated.

**Elastic net**, $\lambda_1 = 0.2$, $\lambda_2 = 0.2$: in the orthonormal case the solution is $S(b_j, \lambda_1)/(1 + \lambda_2)$.

$$
\hat{\boldsymbol\beta}_{\text{EN}} = \frac{(1.8,\ 0.3,\ -0.1)}{1.2} = (1.5,\ 0.25,\ -0.083).
$$

**Bias–variance arithmetic.** Suppose that at some test point a model's predictions over many training sets have mean 4.2 and standard deviation 0.5, the true value is $f = 4.0$, and the noise variance is $\sigma^2 = 1$. Expected squared error $= (4.0 - 4.2)^2 + 0.5^2 + 1 = 0.04 + 0.25 + 1 = 1.29$. A stronger penalty might change this to mean 3.7, SD 0.2: $0.09 + 0.04 + 1 = 1.13$. More bias, less total error.

## In code

First, the bias–variance decomposition measured by simulation. We draw 4,000 independent training sets ($n = 50$, $p = 30$), fit ridge at several values of $\lambda$, and look at the predictions for one fixed test person.

```python
import numpy as np

rng = np.random.default_rng(0)
n, p, sigma = 50, 30, 1.0
beta_true = rng.normal(0, 0.3, p)
x0 = rng.normal(0, 1, p)                         # a fixed test person
f0 = x0 @ beta_true                              # true expected outcome there

def ridge(X, y, lam):
    return np.linalg.solve(X.T @ X + lam * np.eye(X.shape[1]), X.T @ y)

print(f"{'lambda':>7} {'bias^2':>8} {'variance':>9} {'noise':>6} {'sum':>7} {'MSE(sim)':>9}")
for lam in [0, 1, 5, 20, 100, 1000]:
    preds, errs = [], []
    for rep in range(4000):                      # many independent training sets
        X = rng.normal(0, 1, (n, p))
        y = X @ beta_true + rng.normal(0, sigma, n)
        pred = x0 @ ridge(X, y, lam)
        y0 = f0 + rng.normal(0, sigma)           # a fresh noisy outcome at x0
        preds.append(pred); errs.append((y0 - pred) ** 2)
    preds = np.array(preds)
    bias2 = (preds.mean() - f0) ** 2
    var = preds.var()
    print(f"{lam:7.0f} {bias2:8.3f} {var:9.3f} {sigma**2:6.2f} "
          f"{bias2 + var + sigma**2:7.3f} {np.mean(errs):9.3f}")
```

```text
 lambda   bias^2  variance  noise     sum  MSE(sim)
      0    0.001     1.531   1.00   2.532     2.516
      1    0.017     1.221   1.00   2.238     2.233
      5    0.202     0.730   1.00   1.932     1.926
     20    1.009     0.369   1.00   2.378     2.370
    100    3.311     0.105   1.00   4.416     4.413
   1000    5.983     0.003   1.00   6.986     6.932
```

The decomposition ("sum") matches the directly simulated error to within Monte Carlo noise. Unpenalised least squares ($\lambda = 0$) is essentially unbiased but has high variance; huge $\lambda$ has almost no variance but predicts nearly 0 for everyone. The best total error is in between, here near $\lambda = 5$.

Now a $p > n$ genetic example: 1,000 SNPs in LD blocks of 10, 400 training people, and a quantitative trait (think LDL) driven by 10 causal SNPs. We compare unpenalised least squares with ridge, lasso and elastic net, each tuned by cross-validation.

```python
import numpy as np
from sklearn.linear_model import LinearRegression, RidgeCV, LassoCV, ElasticNetCV
from sklearn.metrics import r2_score

rng = np.random.default_rng(7)
n, p, k = 600, 1000, 10                           # people, SNPs, causal SNPs
# Genotypes in LD blocks of 10 correlated SNPs (latent Gaussian -> two haplotypes)
blocks = p // 10
def haplotype():
    z = rng.normal(size=(n, blocks)).repeat(10, axis=1) * 0.9 + rng.normal(size=(n, p)) * 0.45
    return (z > 1.0).astype(int)                  # ALT freq ~ 0.13 per haplotype
G = haplotype() + haplotype()                     # dosage 0/1/2, shape (n, p)
causal = rng.choice(p, size=k, replace=False)
beta = np.zeros(p); beta[causal] = rng.choice([-1, 1], k) * rng.uniform(0.4, 0.8, k)
y = G @ beta + rng.normal(0, 1.0, n)              # quantitative trait, e.g. LDL

# Train/test split, and standardise using TRAIN statistics only
tr, te = np.arange(n) < 400, np.arange(n) >= 400
mu, sd = G[tr].mean(0), G[tr].std(0) + 1e-8
Z = (G - mu) / sd
print("train n =", tr.sum(), " p =", p, " corr of neighbouring SNPs ≈",
      np.corrcoef(G[:, 0], G[:, 1])[0, 1].round(2))

ols = LinearRegression().fit(Z[tr], y[tr])        # p > n: interpolates training data
print(f"OLS         train R2={r2_score(y[tr], ols.predict(Z[tr])):.3f}  "
      f"test R2={r2_score(y[te], ols.predict(Z[te])):.3f}")

ridge = RidgeCV(alphas=np.logspace(0, 5, 30)).fit(Z[tr], y[tr])
lasso = LassoCV(alphas=30, cv=5, max_iter=5000).fit(Z[tr], y[tr])
enet = ElasticNetCV(l1_ratio=0.5, alphas=30, cv=5, max_iter=5000).fit(Z[tr], y[tr])
for name, m in [("ridge", ridge), ("lasso", lasso), ("elastic net", enet)]:
    nz = np.sum(m.coef_ != 0)
    print(f"{name:11s} alpha={m.alpha_:9.4f}  test R2={r2_score(y[te], m.predict(Z[te])):.3f}"
          f"  nonzero coefs={nz}")

# Did lasso find the causal SNPs (or a neighbour in the same LD block)?
sel = np.flatnonzero(lasso.coef_)
exact = np.intersect1d(sel, causal).size
same_block = sum(np.any(sel // 10 == c // 10) for c in causal)
print(f"lasso: {exact}/{k} causal SNPs selected exactly, {same_block}/{k} blocks hit")
print("oracle test R2:", round(r2_score(y[te], G[te] @ beta), 3))
```

```text
train n = 400  p = 1000  corr of neighbouring SNPs ≈ 0.53
OLS         train R2=1.000  test R2=-0.230
ridge       alpha=2807.2162  test R2=0.135  nonzero coefs=1000
lasso       alpha=   0.1058  test R2=0.345  nonzero coefs=37
elastic net alpha=   0.1667  test R2=0.339  nonzero coefs=73
lasso: 10/10 causal SNPs selected exactly, 10/10 blocks hit
oracle test R2: 0.545
```

How to read this:

- **OLS** fits the training data perfectly ($R^2 = 1$) and is *worse than predicting the mean* on test data (negative $R^2$). Textbook overfitting.
- **Ridge** helps but is limited, because the truth is sparse and ridge spreads weight over all 1,000 SNPs.
- **Lasso** keeps 37 SNPs, including all 10 causal ones, and has the best test $R^2$. The 27 extra SNPs (only 3 of them in a causal LD block) are false positives, mostly with small coefficients.
- **Elastic net** is close to lasso and keeps more correlated neighbours, as its grouping effect predicts.
- Even the **oracle** that knows the true $\boldsymbol\beta$ only reaches $R^2 \approx 0.55$: the remaining variance is noise. No method can beat that ceiling.

> [!NOTE]
> Which penalty wins depends on the true genetic architecture. If the trait is driven by many tiny effects (as CAD largely is), ridge-like shrinkage tends to beat lasso. Change `k` to 500 and the effect sizes to `rng.uniform(0.05, 0.15, k)` and rerun: with this seed ridge reaches a test $R^2$ of about 0.16 while lasso drops to about 0.09.

## Biomedical connection

Building a polygenic risk score is a $p \gg n$ regression problem, and every PRS method is a form of regularization:

| PRS method family | Regularization idea |
|---|---|
| Clumping and thresholding (C+T) | keep only SNPs below a p-value threshold, one per LD region: a crude hard-threshold selection |
| Bayesian shrinkage with LD modelling (e.g. LDpred, PRS-CS) | Gaussian-like or continuous shrinkage priors on effect sizes: ridge-like or sparse-ish shrinkage computed from GWAS summary statistics and an LD reference |
| Penalised regression on individual-level data | lasso or elastic net fitted directly on biobank genotypes |

The genome-wide CAD score of Khera and colleagues (2018) was built with LDpred, a Bayesian shrinkage method. The penalty strength (or prior) is a hyperparameter, tuned on a validation set separate from both the GWAS discovery data and the final test data.

When we later combine a PRS with clinical variables and perhaps hundreds of other features (proteomics, imaging, EHR codes), regularization remains essential. And in a neural network, **weight decay** is exactly the ridge penalty applied to every weight.

> [!CAUTION]
> Sparse models are attractive because they "pick SNPs", but a selected SNP is not necessarily causal: lasso often picks an LD neighbour of the true causal variant, and which neighbour can change between samples. Selection from a penalised model is not evidence of biological mechanism and needs fine-mapping and functional follow-up.

## Practice

1. With $X^\top X = I$ and OLS estimates $\mathbf b = (1.2, -0.7, 0.2)$, compute the lasso solution with $\lambda = 0.5$ and the ridge solution with $\lambda = 1$.

<details>
<summary>Answer</summary>

Lasso: $(0.7, -0.2, 0)$. Ridge: $\mathbf b / 2 = (0.6, -0.35, 0.1)$.

</details>

2. Show that $X^\top X + \lambda I$ is invertible for any $\lambda > 0$, even if $X$ has more columns than rows.

<details>
<summary>Answer</summary>

For any non-zero $\mathbf v$: $\mathbf v^\top(X^\top X + \lambda I)\mathbf v = \lVert X\mathbf v\rVert^2 + \lambda\lVert\mathbf v\rVert^2 \ge \lambda\lVert\mathbf v\rVert^2 > 0$. So the matrix is positive definite, hence it has no zero eigenvalue and is invertible.

</details>

3. A model's predictions at a point have bias 0.3 and variance 0.16, and the noise variance is 0.5. What is the expected squared prediction error? Which term could a larger training set reduce?

<details>
<summary>Answer</summary>

$0.3^2 + 0.16 + 0.5 = 0.09 + 0.16 + 0.5 = 0.75$. More data mainly reduces **variance**. Bias is a property of the model class and penalty; noise is irreducible.

</details>

4. Two SNPs are perfectly correlated (identical columns) and both truly matter. Describe what ridge and lasso do.

<details>
<summary>Answer</summary>

Only the sum $\beta_1 + \beta_2$ is identifiable. Ridge minimises $\beta_1^2 + \beta_2^2$ for a fixed sum, so it splits the weight equally. Lasso's penalty $\lvert\beta_1\rvert + \lvert\beta_2\rvert$ is the same for any split with equal signs, so the solution is not unique; in practice coordinate descent typically puts all the weight on one of them. Elastic net splits it evenly, like ridge, while still allowing sparsity elsewhere.

</details>

5. Why must the training-set mean and SD, rather than the full-data mean and SD, be used to standardise genotypes before penalised regression?

<details>
<summary>Answer</summary>

Using the test data's statistics lets information from the test set influence the fitted model (the scaling, and therefore the effective penalty on each coefficient). That is data leakage: the test error would no longer be an honest estimate of performance on truly new people.

</details>

## Further reading

- Hoerl, A. E. and Kennard, R. W. (1970). Ridge regression: biased estimation for nonorthogonal problems. *Technometrics* 12(1).
- Tibshirani, R. (1996). Regression shrinkage and selection via the lasso. *Journal of the Royal Statistical Society, Series B* 58(1).
- Zou, H. and Hastie, T. (2005). Regularization and variable selection via the elastic net. *Journal of the Royal Statistical Society, Series B* 67(2).
- Friedman, J., Hastie, T. and Tibshirani, R. (2010). Regularization paths for generalized linear models via coordinate descent. *Journal of Statistical Software* 33(1).
- Hastie, T., Tibshirani, R. and Wainwright, M. (2015). *Statistical Learning with Sparsity: The Lasso and Generalizations.* CRC Press.
- Vilhjálmsson, B. J. et al. (2015). Modeling linkage disequilibrium increases accuracy of polygenic risk scores. *American Journal of Human Genetics* 97(4).
