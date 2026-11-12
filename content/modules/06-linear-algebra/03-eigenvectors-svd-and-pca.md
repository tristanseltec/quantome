+++
summary = "Compute eigenvalues and eigenvectors, derive PCA as variance maximisation, connect it to the SVD, and use top principal components to reveal and correct for ancestry in genotype data."
+++

# Eigenvectors, SVD and PCA

A genotype matrix with 400,000 people and 600,000 SNPs is far too large to look at. Yet hidden inside it is a strikingly simple pattern: people with similar ancestry have similar genotypes. Principal component analysis (PCA) finds the few directions along which the data vary most, and when applied to genotypes, the first few directions typically line up with ancestry. Genetic studies of heart disease use exactly this to avoid mistaking ancestry for disease risk.

To understand PCA properly we need **eigenvectors** (special directions of a matrix), the **covariance matrix** (how features vary together) and the **singular value decomposition** (the most useful factorisation in applied linear algebra). We will derive PCA from scratch rather than treat it as a black box.

## Key ideas

### Eigenvalues and eigenvectors

A square matrix $\mathbf{A}$ moves most vectors in a new direction. An **eigenvector** is a non-zero vector that $\mathbf{A}$ only stretches (or shrinks, or flips):

> [!IMPORTANT]
> $$\mathbf{A}\mathbf{v} = \lambda\mathbf{v}, \qquad \mathbf{v}\neq\mathbf{0}$$
> The scalar $\lambda$ is the **eigenvalue**: the stretch factor along direction $\mathbf{v}$.

Any multiple of an eigenvector is also an eigenvector, so we usually scale them to length 1. An eigenvector's sign is arbitrary: if $\mathbf{v}$ works, so does $-\mathbf{v}$. (Software may return either, so PCA plots from two programs can be mirror images.)

**How to find them (2×2).** $\mathbf{A}\mathbf{v} = \lambda\mathbf{v}$ means $(\mathbf{A} - \lambda\mathbf{I})\mathbf{v} = \mathbf{0}$ has a non-zero solution. That happens only if $\mathbf{A}-\lambda\mathbf{I}$ squashes some direction to zero, that is, if it has no inverse, which means its determinant is zero:

$$
\det(\mathbf{A} - \lambda\mathbf{I}) = 0.
$$

For a $2\times2$ matrix this is a quadratic in $\lambda$, the **characteristic equation**. Solve it, then substitute each $\lambda$ back to find $\mathbf{v}$.

**Intuition.** Picture $\mathbf{A}$ acting on a circle of unit vectors. It turns the circle into an ellipse. For a symmetric matrix, the eigenvectors point along the ellipse's axes and the eigenvalues are the axis half-lengths (up to sign). Eigenvectors are the natural coordinate axes of the transformation.

### Symmetric matrices are especially nice

The matrices we care most about in this chapter (covariance matrices) are symmetric. The **spectral theorem** says a real symmetric $p\times p$ matrix $\mathbf{S}$ has

- $p$ real eigenvalues $\lambda_1\ge\lambda_2\ge\dots\ge\lambda_p$, and
- eigenvectors $\mathbf{v}_1,\dots,\mathbf{v}_p$ that can be chosen **orthonormal**: each has length 1 and every pair is orthogonal.

Collect the eigenvectors as the columns of $\mathbf{V}$ and the eigenvalues in a diagonal matrix $\boldsymbol{\Lambda}$. Then

$$
\mathbf{S} = \mathbf{V}\boldsymbol{\Lambda}\mathbf{V}^\top, \qquad \mathbf{V}^\top\mathbf{V} = \mathbf{I}.
$$

Read right to left: rotate into the eigenvector coordinate system ($\mathbf{V}^\top$), stretch each axis by its eigenvalue ($\boldsymbol{\Lambda}$), rotate back ($\mathbf{V}$).

### The covariance matrix

Let $\mathbf{X}$ be an $n\times p$ data matrix (rows = people, columns = features) whose columns have been **centred** (each column's mean subtracted). The sample **covariance matrix** is

> [!IMPORTANT]
> $$\mathbf{C} = \frac{1}{n-1}\mathbf{X}^\top\mathbf{X} \in \mathbb{R}^{p\times p}, \qquad C_{jk} = \frac{1}{n-1}\sum_{i=1}^n x_{ij}x_{ik}$$

The diagonal entry $C_{jj}$ is the variance of feature $j$; the off-diagonal $C_{jk}$ is the covariance between features $j$ and $k$. $\mathbf{C}$ is symmetric. If each column is also scaled to unit variance, $\mathbf{C}$ becomes the **correlation matrix**. For genotypes, neighbouring SNPs are correlated (linkage disequilibrium), which shows up as non-zero off-diagonal entries.

The key fact: for any unit vector $\mathbf{w}$, the data projected onto $\mathbf{w}$ are the numbers $\mathbf{X}\mathbf{w}$ (one per person), and their variance is

$$
\operatorname{Var}(\mathbf{X}\mathbf{w}) = \frac{1}{n-1}(\mathbf{X}\mathbf{w})^\top(\mathbf{X}\mathbf{w}) = \mathbf{w}^\top\Big(\frac{1}{n-1}\mathbf{X}^\top\mathbf{X}\Big)\mathbf{w} = \mathbf{w}^\top\mathbf{C}\mathbf{w}.
$$

(The projections have mean zero because the columns are centred.) Since a variance cannot be negative, $\mathbf{w}^\top\mathbf{C}\mathbf{w}\ge0$ for every $\mathbf{w}$, so all eigenvalues of $\mathbf{C}$ are $\ge 0$.

### PCA derived: maximise the variance

**Goal.** Find the unit direction $\mathbf{w}$ along which the data vary the most:

$$
\max_{\mathbf{w}}\ \mathbf{w}^\top\mathbf{C}\mathbf{w} \quad\text{subject to}\quad \lVert\mathbf{w}\rVert_2 = 1.
$$

(Without the length constraint we could make the variance infinite by scaling $\mathbf{w}$.)

**Derivation.** Write $\mathbf{w}$ in the orthonormal eigenvector basis of $\mathbf{C}$: $\mathbf{w} = c_1\mathbf{v}_1 + \dots + c_p\mathbf{v}_p$. Because the $\mathbf{v}_j$ are orthonormal, $\lVert\mathbf{w}\rVert^2 = c_1^2 + \dots + c_p^2 = 1$. Now

$$
\mathbf{C}\mathbf{w} = c_1\lambda_1\mathbf{v}_1 + \dots + c_p\lambda_p\mathbf{v}_p
\quad\Rightarrow\quad
\mathbf{w}^\top\mathbf{C}\mathbf{w} = \lambda_1c_1^2 + \lambda_2c_2^2 + \dots + \lambda_pc_p^2.
$$

This is a weighted average of the eigenvalues, with weights $c_j^2$ that sum to 1. A weighted average can never exceed its largest ingredient, so $\mathbf{w}^\top\mathbf{C}\mathbf{w}\le\lambda_1$, with equality when all the weight is on $\lambda_1$: $c_1 = \pm1$, all other $c_j = 0$, i.e. $\mathbf{w} = \pm\mathbf{v}_1$.

> [!IMPORTANT]
> The direction of maximum variance is the top eigenvector $\mathbf{v}_1$ of the covariance matrix, and the variance along it is the top eigenvalue $\lambda_1$.

The **second principal component** is the direction of maximum variance among unit vectors orthogonal to $\mathbf{v}_1$. Orthogonality forces $c_1 = 0$, so the same argument gives $\mathbf{v}_2$ with variance $\lambda_2$. Continuing, the principal components are the eigenvectors in order of decreasing eigenvalue. (The same result follows from Lagrange multipliers, which you will be able to apply after [derivatives and gradients](../../calculus-and-optimization/derivatives-and-gradients/).)

Each person's **PC score** on component $k$ is $\mathbf{x}_i^\top\mathbf{v}_k$, their coordinate along that axis. Keeping the top $K$ components compresses each person from $p$ numbers to $K$.

### Explained variance

The total variance is the sum of the per-feature variances, $\operatorname{tr}(\mathbf{C}) = \sum_j C_{jj}$, and the trace of a symmetric matrix equals the sum of its eigenvalues. So

$$
\text{fraction of variance explained by PC}_k = \frac{\lambda_k}{\lambda_1 + \lambda_2 + \dots + \lambda_p}.
$$

A **scree plot** of these fractions shows how many components carry real structure before the curve flattens into noise.

### The singular value decomposition

Every $n\times p$ matrix, square or not, can be factorised as

> [!IMPORTANT]
> $$\mathbf{X} = \mathbf{U}\boldsymbol{\Sigma}\mathbf{V}^\top$$
> $\mathbf{U}$ ($n\times r$) and $\mathbf{V}$ ($p\times r$) have orthonormal columns; $\boldsymbol{\Sigma}$ is diagonal with **singular values** $s_1\ge s_2\ge\dots\ge0$; $r = \min(n,p)$ in the "thin" form.

Geometrically: any linear map is a rotation, then a stretch along the axes, then another rotation.

The SVD *is* PCA. Substitute it into $\mathbf{X}^\top\mathbf{X}$:

$$
\mathbf{X}^\top\mathbf{X} = \mathbf{V}\boldsymbol{\Sigma}\mathbf{U}^\top\mathbf{U}\boldsymbol{\Sigma}\mathbf{V}^\top = \mathbf{V}\boldsymbol{\Sigma}^2\mathbf{V}^\top.
$$

This is an eigendecomposition. Therefore:

- the **right singular vectors** (columns of $\mathbf{V}$) are the principal directions;
- the eigenvalues of $\mathbf{C}$ are $\lambda_k = s_k^2/(n-1)$;
- the PC scores are $\mathbf{X}\mathbf{V} = \mathbf{U}\boldsymbol{\Sigma}$, column $k$ being $s_k\mathbf{u}_k$.

In practice we compute PCA with the SVD of the centred data, never by forming $\mathbf{C}$: it is more numerically accurate, and with $p = 600{,}000$ SNPs the $p\times p$ covariance matrix would have $3.6\times10^{11}$ entries. Genetics software goes further and uses randomised or iterative methods that compute only the top few components.

Truncating the SVD to the top $K$ terms, $\mathbf{X}_K = \sum_{k=1}^K s_k\mathbf{u}_k\mathbf{v}_k^\top$, gives the best possible rank-$K$ approximation of $\mathbf{X}$ in squared error (the Eckart–Young theorem). Low-rank ideas reappear in model compression and in fine-tuning large models.

> [!WARNING]
> PCA must be run on **centred** data, otherwise PC1 mostly points towards the mean. And it is scale-sensitive: a feature measured in large units (LDL in mg/dL rather than mmol/L) will dominate. Standardise features with different units first.

## Worked example

**Eigenvalues by hand.** Let $\mathbf{A} = \begin{bmatrix}2&1\\1&2\end{bmatrix}$.

$$
\det\begin{bmatrix}2-\lambda & 1\\ 1 & 2-\lambda\end{bmatrix} = (2-\lambda)^2 - 1 = 0 \ \Rightarrow\ 2-\lambda = \pm1 \ \Rightarrow\ \lambda = 3 \text{ or } 1.
$$

For $\lambda = 3$: $(\mathbf{A}-3\mathbf{I})\mathbf{v} = \begin{bmatrix}-1&1\\1&-1\end{bmatrix}\mathbf{v} = \mathbf{0}$ gives $v_1 = v_2$, so $\mathbf{v} = \tfrac{1}{\sqrt2}(1,1)$.
For $\lambda = 1$: $\begin{bmatrix}1&1\\1&1\end{bmatrix}\mathbf{v} = \mathbf{0}$ gives $v_1 = -v_2$, so $\mathbf{v} = \tfrac1{\sqrt2}(1,-1)$.
Check: $\mathbf{A}(1,1) = (3,3) = 3\cdot(1,1)$. The two eigenvectors are orthogonal, as the spectral theorem promises.

**PCA by hand.** Four people, two standardised measurements, already centred (each column sums to 0):

$$
\mathbf{X} = \begin{bmatrix} 3 & 1\\ 1 & 3\\ -1 & -3\\ -3 & -1\end{bmatrix}.
$$

*Covariance.* $\sum x_{i1}^2 = 9 + 1 + 1 + 9 = 20$, $\sum x_{i2}^2 = 20$, $\sum x_{i1}x_{i2} = 3 + 3 + 3 + 3 = 12$. With $n - 1 = 3$:

$$
\mathbf{C} = \frac13\begin{bmatrix}20&12\\12&20\end{bmatrix} = \begin{bmatrix}20/3 & 4\\ 4 & 20/3\end{bmatrix}.
$$

*Eigen-decomposition.* $\mathbf{C}$ has the form $\begin{bmatrix}a&b\\b&a\end{bmatrix}$, which (as above) has eigenvectors $\tfrac1{\sqrt2}(1,1)$ and $\tfrac1{\sqrt2}(1,-1)$ with eigenvalues $a+b$ and $a-b$:

$$
\lambda_1 = \tfrac{20}{3} + 4 = \tfrac{32}{3}\approx10.667,\qquad \lambda_2 = \tfrac{20}{3} - 4 = \tfrac83\approx2.667.
$$

*Explained variance.* Total $= 32/3 + 8/3 = 40/3$, which matches $\operatorname{tr}(\mathbf{C}) = 20/3 + 20/3$. PC1 explains $\frac{32/3}{40/3} = 80\%$.

*Scores.* Project onto $\mathbf{v}_1 = \tfrac1{\sqrt2}(1,1)$: person 1 gets $(3+1)/\sqrt2 = 4/\sqrt2 = 2\sqrt2\approx2.83$; persons 1 and 2 get $+2\sqrt2$, persons 3 and 4 get $-2\sqrt2$. The variance of these scores is $4\cdot8/3 = 32/3 = \lambda_1$, as it should be. PC1 cleanly splits the four people into two groups.

*SVD check.* $s_k = \sqrt{(n-1)\lambda_k}$: $s_1 = \sqrt{32}\approx5.657$ and $s_2 = \sqrt8\approx2.828$.

## In code

First, confirm the worked example. `np.linalg.eigh` is for symmetric matrices and returns eigenvalues in **ascending** order.

```python
import numpy as np

# Worked example: 4 centred points in 2-D
X = np.array([[3.0, 1.0], [1.0, 3.0], [-1.0, -3.0], [-3.0, -1.0]])
C = X.T @ X / (len(X) - 1)
print("covariance:\n", C)
vals, vecs = np.linalg.eigh(C)          # eigh: for symmetric matrices, ascending
print("eigenvalues:", vals)
print("eigenvectors (columns):\n", vecs)

U, s, Vt = np.linalg.svd(X, full_matrices=False)
print("singular values:", s)
print("s^2/(n-1):", s**2 / (len(X) - 1))
print("right singular vectors (rows of Vt):\n", Vt)
print("PC scores X @ v1:", X @ Vt[0])
```

```text
covariance:
 [[6.66666667 4.        ]
 [4.         6.66666667]]
eigenvalues: [ 2.66666667 10.66666667]
eigenvectors (columns):
 [[-0.70710678  0.70710678]
 [ 0.70710678  0.70710678]]
singular values: [5.65685425 2.82842712]
s^2/(n-1): [10.66666667  2.66666667]
right singular vectors (rows of Vt):
 [[-0.70710678 -0.70710678]
 [ 0.70710678 -0.70710678]]
PC scores X @ v1: [-2.82842712 -2.82842712  2.82842712  2.82842712]
```

Every number matches the hand calculation, except that the SVD happened to return $-\mathbf{v}_1$, so the scores have flipped sign. That is the sign ambiguity in action and it is harmless.

Now a synthetic genotype matrix with **population structure**. Two populations descend from a common ancestor; random genetic drift has shifted each SNP's allele frequency a little in each population. No single SNP is very different, but across 1,000 SNPs the small differences add up.

```python
import numpy as np

rng = np.random.default_rng(42)
n_per_pop, p = 200, 1000

# Two populations with related but different allele frequencies
p_anc = rng.uniform(0.1, 0.9, size=p)                 # ancestral frequency
drift = rng.normal(0, 0.1, size=(2, p))               # population drift
freqs = np.clip(p_anc + drift, 0.01, 0.99)            # (2, p)

pop = np.repeat([0, 1], n_per_pop)                    # labels, (n,)
G = rng.binomial(2, freqs[pop]).astype(float)         # (n, p) dosages 0/1/2
print("genotype matrix:", G.shape)

# Standardise each SNP (column): centre, then scale to unit variance
mu = G.mean(axis=0)
sd = G.std(axis=0)
Z = (G - mu) / sd

# PCA via SVD of the standardised matrix
U, s, Vt = np.linalg.svd(Z, full_matrices=False)
explained = s**2 / np.sum(s**2)
print("variance explained by PC1..PC5:", explained[:5].round(4))

scores = Z @ Vt[:2].T                                 # (n, 2) = U[:, :2] * s[:2]
print("scores equal U*s:", np.allclose(scores, U[:, :2] * s[:2]))
for k in (0, 1):
    print(f"pop {k}: mean PC1 = {scores[pop == k, 0].mean():7.2f}, "
          f"mean PC2 = {scores[pop == k, 1].mean():6.2f}")

# PCA is the eigen-decomposition of the covariance matrix
Cov = Z.T @ Z / (len(Z) - 1)                          # (p, p)
top_eig = np.linalg.eigvalsh(Cov)[::-1][:3]
print("top eigenvalues of covariance:", top_eig.round(2))
print("s^2/(n-1) from SVD:          ", (s[:3]**2 / (len(Z) - 1)).round(2))
```

```text
genotype matrix: (400, 1000)
variance explained by PC1..PC5: [0.0558 0.0062 0.0061 0.0061 0.006 ]
scores equal U*s: True
pop 0: mean PC1 =   -7.40, mean PC2 =   0.02
pop 1: mean PC1 =    7.40, mean PC2 =  -0.02
top eigenvalues of covariance: [55.94  6.2   6.13]
s^2/(n-1) from SVD:           [55.94  6.2   6.13]
```

PC1 separates the two populations: their means are −7.40 and +7.40, and in this run every person in population 0 scores below −4.9 while every person in population 1 scores above 4.6, even though the code never told PCA who belongs where. PC1 explains about 5.6% of the variance, roughly nine times as much as each of the following components, which are noise of similar size (the scree plot is flat after PC1). With real data from many populations, several top PCs carry structure; in Europe, PC1 and PC2 famously reproduce a map of geography (Novembre et al., 2008). The last two lines confirm that the SVD and the covariance eigendecomposition give the same eigenvalues.

> [!NOTE]
> In the output above, PC2's population means are printed as $0.02$ and $-0.02$; their exact values are noise. The sign and size of PC2 carry no population information here.

## Biomedical connection

Why does population structure matter for a heart-disease model? Suppose people of ancestry group 1 have, on average, higher measured values of some cardiovascular trait than group 0 because of diet, healthcare access or other environmental factors, and not because of any particular SNP. Thousands of SNPs differ in frequency between the groups simply because of drift. A naive association test of each SNP against the trait will "discover" all of those ancestry-differentiated SNPs: the SNP is correlated with ancestry, ancestry is correlated with the trait, so the SNP looks correlated with the trait. This is **confounding by ancestry** (population stratification).

The standard fix, popularised by Price et al. (2006) in the EIGENSTRAT method, is to include the top PC scores as **covariates** in every association regression. The PCs capture the ancestry axes, so after adjusting for them the remaining association between a SNP and the trait is no longer explained by ancestry.

We can watch this work. Using the same synthetic population, create a trait that depends on population but on **no SNP at all**, then test every SNP with and without the top 5 PCs as covariates:

```python
import numpy as np

rng = np.random.default_rng(42)
n_per_pop, p = 200, 1000
p_anc = rng.uniform(0.1, 0.9, size=p)
freqs = np.clip(p_anc + rng.normal(0, 0.1, size=(2, p)), 0.01, 0.99)
pop = np.repeat([0, 1], n_per_pop)
G = rng.binomial(2, freqs[pop]).astype(float)
Z = (G - G.mean(axis=0)) / G.std(axis=0)

# A trait that depends on ancestry (e.g. diet, environment) but on NO SNP
y = 1.0 * pop + rng.normal(0, 1, size=len(pop))

def t_stat(x, y, covars):
    """t-statistic for x in the regression y ~ 1 + x + covars."""
    D = np.column_stack([np.ones_like(x), x] + covars)   # design matrix
    beta, *_ = np.linalg.lstsq(D, y, rcond=None)
    resid = y - D @ beta
    sigma2 = resid @ resid / (len(y) - D.shape[1])
    se = np.sqrt(sigma2 * np.linalg.inv(D.T @ D)[1, 1])
    return beta[1] / se

U, s, Vt = np.linalg.svd(Z, full_matrices=False)
pcs = [U[:, k] * s[k] for k in range(5)]                 # top 5 PC scores

t_raw = np.array([t_stat(Z[:, j], y, []) for j in range(p)])
t_adj = np.array([t_stat(Z[:, j], y, pcs) for j in range(p)])

# With no true effects, about 5% of SNPs should have |t| > 1.96 by chance
print(f"fraction |t|>1.96, no adjustment:   {np.mean(np.abs(t_raw) > 1.96):.3f}")
print(f"fraction |t|>1.96, adjusted 5 PCs:  {np.mean(np.abs(t_adj) > 1.96):.3f}")
```

```text
fraction |t|>1.96, no adjustment:   0.405
fraction |t|>1.96, adjusted 5 PCs:  0.049
```

Without adjustment, 40.5% of SNPs look "significant" at the 5% level, although none has any effect. With the top 5 PCs as covariates, the rate falls to 4.9%, right where chance predicts. (The regression and $t$-statistic are explained in [linear and logistic regression](../../classical-machine-learning/linear-and-logistic-regression/) and [hypothesis testing](../../probability-and-statistics/hypothesis-testing-and-multiple-comparisons/).)

The same logic applies to a deep-learning risk model. A network trained on a mixed-ancestry cohort can learn to detect ancestry and use it as a shortcut for risk, which will not transfer to a cohort with different environments. Including PCs as inputs, stratifying evaluation by ancestry and checking performance per group are standard defences.

> [!CAUTION]
> Ancestry PCs are statistical summaries of genetic similarity, not biological categories, and they are not the same thing as race or ethnicity. Polygenic risk scores for coronary artery disease, largely developed in European-ancestry cohorts, are known to predict less accurately in other ancestries. Any clinical use must be validated in the population where it will be applied.

## Practice

1. Find the eigenvalues and unit eigenvectors of $\begin{bmatrix}4 & 0\\ 0 & 1\end{bmatrix}$. What fraction of variance would PC1 explain if this were a covariance matrix?

<details>
<summary>Answer</summary>

A diagonal matrix's eigenvalues are its diagonal entries: $\lambda_1 = 4$ with $\mathbf{v}_1 = (1,0)$, $\lambda_2 = 1$ with $\mathbf{v}_2 = (0,1)$. PC1 explains $4/(4+1) = 80\%$. The features are uncorrelated, so the principal axes are just the original axes.

</details>

2. Find the eigenvalues of $\begin{bmatrix}5 & 2\\ 2 & 2\end{bmatrix}$ and an eigenvector for the larger one.

<details>
<summary>Answer</summary>

$(5-\lambda)(2-\lambda) - 4 = \lambda^2 - 7\lambda + 6 = (\lambda-6)(\lambda-1) = 0$, so $\lambda = 6$ or $1$.
For $\lambda = 6$: $\begin{bmatrix}-1 & 2\\ 2 & -4\end{bmatrix}\mathbf{v} = \mathbf{0}$ gives $v_1 = 2v_2$, so $\mathbf{v} = (2,1)/\sqrt5$. Check: $(5\cdot2 + 2\cdot1,\ 2\cdot2 + 2\cdot1) = (12, 6) = 6\cdot(2,1)$.

</details>

3. A centred $500\times2000$ matrix has singular values $s_1 = 60$, $s_2 = 30$, and all the remaining singular values squared sum to $8{,}100$. What fraction of the variance does PC1 explain? What is the variance of the PC1 scores?

<details>
<summary>Answer</summary>

Total $\sum s_k^2 = 3600 + 900 + 8100 = 12{,}600$. PC1 explains $3600/12600 \approx 28.6\%$.
Variance of PC1 scores $= \lambda_1 = s_1^2/(n-1) = 3600/499 \approx 7.21$.

</details>

4. Show that if $\mathbf{v}$ is an eigenvector of $\mathbf{A}$ with eigenvalue $\lambda$, it is an eigenvector of $\mathbf{A}^2$, and find the eigenvalue.

<details>
<summary>Answer</summary>

$\mathbf{A}^2\mathbf{v} = \mathbf{A}(\mathbf{A}\mathbf{v}) = \mathbf{A}(\lambda\mathbf{v}) = \lambda\mathbf{A}\mathbf{v} = \lambda^2\mathbf{v}$. Eigenvalue $\lambda^2$. (Repeated multiplication amplifies the top eigenvector; this is the idea behind the "power iteration" algorithm for computing PC1.)

</details>

5. In a GWAS, a SNP is strongly associated with coronary artery disease without PC adjustment but not at all after adjusting for the top 10 PCs. Give the most likely explanation.

<details>
<summary>Answer</summary>

Confounding by ancestry: the SNP's allele frequency differs between ancestry groups in the sample, and disease rates (or case/control sampling) also differ between those groups for other reasons. The SNP was a marker of ancestry rather than of disease risk. Once ancestry is captured by the PCs, the association disappears.

</details>

## Further reading

- Gilbert Strang, *Introduction to Linear Algebra*, Wellesley-Cambridge Press (chapters on eigenvalues and the SVD).
- Lloyd N. Trefethen and David Bau III, *Numerical Linear Algebra*, SIAM, 1997. Why we compute PCA with the SVD.
- Alkes L. Price et al., "Principal components analysis corrects for stratification in genome-wide association studies", *Nature Genetics*, 2006.
- Nick Patterson, Alkes L. Price and David Reich, "Population structure and eigenanalysis", *PLoS Genetics*, 2006.
- John Novembre et al., "Genes mirror geography within Europe", *Nature*, 2008.
