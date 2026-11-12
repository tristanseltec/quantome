+++
summary = "Represent patients and DNA as vectors and datasets as matrices, and measure size, similarity and distance with norms, dot products and cosine similarity."
+++

# Vectors and Matrices

Every model in this course, from a polygenic risk score to a transformer, takes numbers in and gives numbers out. Before a computer can learn anything about a person's heart, we have to turn that person into a list of numbers, and turn a cohort of people into a table of numbers. Linear algebra is the language for those lists and tables. In this chapter you will learn to see a patient as a **vector**, a cohort as a **matrix**, and to ask simple but powerful geometric questions: how big is this vector, how similar are these two patients, how far apart are they?

Everything here builds on GMAT algebra. The only new idea is to do arithmetic on whole lists at once.

## Key ideas

### Vectors: a patient as a list of numbers

A **vector** is an ordered list of numbers. We write vectors in bold lower case and, by convention, as columns:

$$
\mathbf{x} = \begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_p \end{bmatrix} \in \mathbb{R}^p
$$

The number of entries $p$ is the **dimension**. $\mathbb{R}^p$ ("R p") is the set of all such vectors with real entries.

A vector can describe almost anything about a person:

- **Clinical features.** $\mathbf{x} = (\text{age}, \text{LDL cholesterol}, \text{systolic BP}, \text{smoker})$, for example $(54, 4.1, 138, 1)$. Here $p = 4$.
- **Genotypes.** At a single-nucleotide polymorphism (SNP) a person carries 0, 1 or 2 copies of the alternate allele. This count is called the **dosage**. Five SNPs give a vector such as $(0, 1, 2, 1, 0)$.
- **A DNA sequence.** The sequence `ACGT` can be written as four vectors, one per base, using one-hot encoding: A $= (1,0,0,0)$, C $= (0,1,0,0)$, and so on. We will stack these into a matrix shortly.

Geometrically, a vector in $\mathbb{R}^2$ is an arrow from the origin to the point $(x_1, x_2)$. In $\mathbb{R}^{500\,000}$ (half a million SNPs) we cannot draw it, but the algebra works exactly the same way. That is the power of linear algebra: intuition from 2D and 3D transfers to any dimension.

### Vector arithmetic

Vectors of the same dimension add entry by entry, and a scalar (an ordinary number) multiplies every entry:

$$
\mathbf{x} + \mathbf{y} = \begin{bmatrix} x_1 + y_1 \\ \vdots \\ x_p + y_p \end{bmatrix}, \qquad
c\,\mathbf{x} = \begin{bmatrix} c x_1 \\ \vdots \\ c x_p \end{bmatrix}
$$

A **linear combination** is a weighted sum $c_1 \mathbf{x}_1 + c_2 \mathbf{x}_2 + \dots$. Much of machine learning is linear combinations: a risk score is a weighted sum of features.

> [!WARNING]
> You cannot add vectors of different dimensions. In code, numpy may silently "broadcast" mismatched shapes instead of raising an error (see the [next chapter](../../linear-algebra/matrix-multiplication-and-tensors/)). Always know the shape of every array.

### Norms: how big is a vector?

A **norm** measures the length or size of a vector. Two norms dominate machine learning.

> [!IMPORTANT]
> **L2 (Euclidean) norm** and **L1 (Manhattan) norm**:
> $$\lVert \mathbf{x} \rVert_2 = \sqrt{x_1^2 + x_2^2 + \dots + x_p^2}, \qquad \lVert \mathbf{x} \rVert_1 = \lvert x_1 \rvert + \lvert x_2 \rvert + \dots + \lvert x_p \rvert$$

The L2 norm is Pythagoras' theorem extended to $p$ dimensions: the straight-line length of the arrow. The L1 norm is the distance you would walk along a city grid, moving only parallel to the axes. For a genotype vector with entries 0, 1, 2, the L1 norm simply counts the total number of alternate alleles the person carries across those SNPs.

Every norm satisfies three properties: it is zero only for the zero vector, $\lVert c\mathbf{x}\rVert = \lvert c\rvert\,\lVert\mathbf{x}\rVert$, and the **triangle inequality** $\lVert \mathbf{x} + \mathbf{y}\rVert \le \lVert\mathbf{x}\rVert + \lVert\mathbf{y}\rVert$ (the direct route is never longer than a detour).

Norms reappear as **regularisers**. Adding $\lambda\lVert\mathbf{w}\rVert_2^2$ to a training loss (ridge) shrinks all weights smoothly; adding $\lambda\lVert\mathbf{w}\rVert_1$ (lasso) pushes many weights to exactly zero, which is attractive when you believe only a few SNPs matter. You will meet both in [regularisation](../../classical-machine-learning/regularization-and-the-bias-variance-tradeoff/).

The **distance** between two vectors is the norm of their difference, $d(\mathbf{x},\mathbf{y}) = \lVert \mathbf{x} - \mathbf{y}\rVert$.

### The dot product

The **dot product** (inner product) of two vectors of the same dimension multiplies matching entries and adds:

$$
\mathbf{x} \cdot \mathbf{y} = \mathbf{x}^\top \mathbf{y} = \sum_{i=1}^{p} x_i y_i
$$

Three facts make the dot product central:

1. **It is a weighted sum.** If $\mathbf{w}$ holds per-SNP effect sizes and $\mathbf{x}$ holds a person's dosages, then $\mathbf{w}^\top\mathbf{x}$ is a **polygenic score**: each allele copy adds its weight.
2. **It gives length.** $\mathbf{x}\cdot\mathbf{x} = \lVert\mathbf{x}\rVert_2^2$.
3. **It measures alignment.** Geometrically,

$$
\mathbf{x}\cdot\mathbf{y} = \lVert\mathbf{x}\rVert_2\,\lVert\mathbf{y}\rVert_2 \cos\theta
$$

where $\theta$ is the angle between the arrows. If they point the same way, $\cos\theta = 1$; at right angles, $\cos\theta = 0$ and the vectors are **orthogonal**; in opposite directions, $\cos\theta = -1$.

Where does the cosine formula come from? Apply the law of cosines to the triangle with sides $\mathbf{x}$, $\mathbf{y}$ and $\mathbf{x}-\mathbf{y}$: $\lVert\mathbf{x}-\mathbf{y}\rVert^2 = \lVert\mathbf{x}\rVert^2 + \lVert\mathbf{y}\rVert^2 - 2\lVert\mathbf{x}\rVert\lVert\mathbf{y}\rVert\cos\theta$. Expanding the left side with the dot product gives $\mathbf{x}\cdot\mathbf{x} - 2\,\mathbf{x}\cdot\mathbf{y} + \mathbf{y}\cdot\mathbf{y}$. Cancel the squared lengths on both sides and the identity drops out.

### Cosine similarity

Rearranging gives **cosine similarity**, which compares direction and ignores length:

> [!IMPORTANT]
> $$\cos(\mathbf{x},\mathbf{y}) = \frac{\mathbf{x}\cdot\mathbf{y}}{\lVert\mathbf{x}\rVert_2\,\lVert\mathbf{y}\rVert_2} \in [-1, 1]$$

It is used to compare embeddings (the learned vectors a neural network produces for a sequence or a patient), to find nearest neighbours, and in attention, where a transformer scores how relevant one position is to another with a scaled dot product ([attention](../../deep-architectures-for-sequences/attention-and-transformers/)).

> [!WARNING]
> Cosine similarity on raw 0/1/2 dosages depends on which allele you called "alternate". Swap the coding of one SNP and the similarity changes. In genetics we usually **centre** each SNP (subtract its mean) and often scale it before comparing people. Centred cosine similarity is exactly the Pearson correlation.

### Matrices: a cohort as a table

A **matrix** is a rectangular grid of numbers. An $n \times p$ matrix has $n$ rows and $p$ columns. The convention in statistics and machine learning is:

> **rows = samples (people), columns = features (SNPs, lab values).**

A **genotype matrix** $\mathbf{G} \in \{0,1,2\}^{n\times p}$ stores the dosage of person $i$ at SNP $j$ in entry $G_{ij}$:

$$
\mathbf{G} = \begin{bmatrix}
G_{11} & G_{12} & \cdots & G_{1p} \\
G_{21} & G_{22} & \cdots & G_{2p} \\
\vdots & & \ddots & \vdots \\
G_{n1} & G_{n2} & \cdots & G_{np}
\end{bmatrix}
$$

Row $i$ is person $i$'s genotype vector. Column $j$ is SNP $j$ across the whole cohort. Biobank-scale studies have $n$ in the hundreds of thousands and $p$ in the hundreds of thousands to millions, so the matrix is enormous, but conceptually it is just this table.

A one-hot DNA sequence of length $L$ is an $L \times 4$ matrix: one row per position, one column per base.

Useful matrix summaries come straight from rows and columns. The mean of column $j$ divided by 2 estimates the **allele frequency** of SNP $j$ in the cohort, because each person has two copies of the genome.

### Transpose

The **transpose** $\mathbf{G}^\top$ flips a matrix over its diagonal: $(\mathbf{G}^\top)_{ij} = G_{ji}$. An $n\times p$ matrix becomes $p\times n$, so the SNPs become rows. A column vector $\mathbf{x}$ becomes a row vector $\mathbf{x}^\top$, which is why the dot product is written $\mathbf{x}^\top\mathbf{y}$. Two rules worth memorising: $(\mathbf{A}^\top)^\top = \mathbf{A}$ and $(\mathbf{A}\mathbf{B})^\top = \mathbf{B}^\top\mathbf{A}^\top$ (the order reverses).

A matrix with $\mathbf{A}^\top = \mathbf{A}$ is **symmetric**. Covariance matrices and similarity matrices are symmetric, a fact that will matter a great deal in [PCA](../../linear-algebra/eigenvectors-svd-and-pca/).

### Identity and inverse

The **identity matrix** $\mathbf{I}$ is square with ones on the diagonal and zeros elsewhere. It plays the role of the number 1: $\mathbf{I}\mathbf{x} = \mathbf{x}$ for every $\mathbf{x}$.

A square matrix $\mathbf{A}$ is **invertible** if there is a matrix $\mathbf{A}^{-1}$ with $\mathbf{A}\mathbf{A}^{-1} = \mathbf{A}^{-1}\mathbf{A} = \mathbf{I}$. The inverse "undoes" $\mathbf{A}$, like dividing by a number undoes multiplying. For a $2\times 2$ matrix there is a formula:

> [!IMPORTANT]
> $$\begin{bmatrix} a & b \\ c & d \end{bmatrix}^{-1} = \frac{1}{ad - bc}\begin{bmatrix} d & -b \\ -c & a \end{bmatrix}, \quad \text{provided } ad - bc \neq 0$$

The quantity $ad - bc$ is the **determinant**. If it is zero, the matrix squashes the plane onto a line and no inverse exists (just as you cannot divide by zero). This happens when columns are redundant, for example two SNPs in perfect linkage disequilibrium that always carry identical dosages.

We use inverses mostly in derivations, such as the least-squares solution $\hat{\mathbf{w}} = (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbf{y}$ in [linear regression](../../classical-machine-learning/linear-and-logistic-regression/). In code we almost never compute an inverse explicitly; solving the system with `np.linalg.solve` is faster and more accurate.

> [!NOTE]
> Matrix multiplication itself (needed to make sense of $\mathbf{A}\mathbf{A}^{-1}$) is covered properly in the [next chapter](../../linear-algebra/matrix-multiplication-and-tensors/). For now, read $\mathbf{A}\mathbf{x}$ as "take the dot product of each row of $\mathbf{A}$ with $\mathbf{x}$".

## Worked example

Two people are genotyped at five SNPs:

$$
\mathbf{a} = (0, 1, 2, 1, 0), \qquad \mathbf{b} = (1, 1, 2, 0, 0)
$$

**1. Norms of $\mathbf{a}$.**
L1: $0 + 1 + 2 + 1 + 0 = 4$ alternate alleles in total.
L2: $\sqrt{0 + 1 + 4 + 1 + 0} = \sqrt{6} \approx 2.449$.

**2. Dot product.**
$\mathbf{a}\cdot\mathbf{b} = 0\cdot1 + 1\cdot1 + 2\cdot2 + 1\cdot0 + 0\cdot0 = 0 + 1 + 4 + 0 + 0 = 5$.

**3. Cosine similarity.**
$\lVert\mathbf{b}\rVert_2 = \sqrt{1 + 1 + 4 + 0 + 0} = \sqrt 6$. So

$$
\cos(\mathbf{a},\mathbf{b}) = \frac{5}{\sqrt6\cdot\sqrt6} = \frac{5}{6} \approx 0.833.
$$

The angle is $\arccos(0.833) \approx 33.6^\circ$: quite similar genotypes.

**4. Distances.** $\mathbf{a} - \mathbf{b} = (-1, 0, 0, 1, 0)$.
L1 distance $= 1 + 0 + 0 + 1 + 0 = 2$ (two allele differences).
L2 distance $= \sqrt{1 + 1} = \sqrt2 \approx 1.414$.

**5. A risk score.** Suppose per-allele effect weights are $\mathbf{w} = (0.2, -0.1, 0.3, 0.0, 0.5)$. Person $\mathbf{a}$'s score is $\mathbf{w}^\top\mathbf{a} = 0 - 0.1 + 0.6 + 0 + 0 = 0.5$. Person $\mathbf{b}$'s score is $0.2 - 0.1 + 0.6 + 0 + 0 = 0.7$.

**6. An inverse.** For $\mathbf{A} = \begin{bmatrix} 2 & 1 \\ 1 & 1\end{bmatrix}$, the determinant is $2\cdot1 - 1\cdot1 = 1$, so

$$
\mathbf{A}^{-1} = \begin{bmatrix} 1 & -1 \\ -1 & 2\end{bmatrix}.
$$

Check the first entry of $\mathbf{A}\mathbf{A}^{-1}$: row 1 of $\mathbf{A}$ dotted with column 1 of $\mathbf{A}^{-1}$ is $2\cdot1 + 1\cdot(-1) = 1$. The off-diagonal entry: $2\cdot(-1) + 1\cdot 2 = 0$. As expected.

## In code

In numpy, a vector is a 1-D array and a matrix is a 2-D array. The `@` operator computes dot products and matrix products.

```python
import numpy as np

rng = np.random.default_rng(0)

# Genotype matrix: n = 6 people (rows) x p = 5 SNPs (columns), dosages 0/1/2
G = rng.integers(0, 3, size=(6, 5))
print("G =\n", G)
print("shape:", G.shape)                      # (n, p)

# Rows are people, columns are SNPs
alice, bob = G[0], G[1]
print("L1 norm of alice:", np.abs(alice).sum())
print("L2 norm of alice:", np.linalg.norm(alice).round(3))
print("dot(alice, bob): ", alice @ bob)

def cosine(u, v):
    return (u @ v) / (np.linalg.norm(u) * np.linalg.norm(v))

print("cosine(alice, bob):", cosine(alice, bob).round(3))

# Column means / 2 = estimated alternate-allele frequency of each SNP
freq = G.mean(axis=0) / 2
print("allele frequencies:", freq.round(3))

# Pairwise cosine similarity between all people, in one line
Gn = G / np.linalg.norm(G, axis=1, keepdims=True)
S = Gn @ Gn.T                                  # (n, n)
print("similarity matrix shape:", S.shape)
print(S.round(2))

# Transpose: SNPs become rows
print("G.T shape:", G.T.shape)

# Identity and inverse of a small matrix
A = np.array([[2.0, 1.0], [1.0, 1.0]])
A_inv = np.linalg.inv(A)
print("A_inv =\n", A_inv)
print("A @ A_inv =\n", A @ A_inv)
print("equal to I?", np.allclose(A @ A_inv, np.eye(2)))
```

Output:

```text
G =
 [[2 1 1 0 0]
 [0 0 0 0 2]
 [1 2 1 1 2]
 [2 1 1 1 2]
 [0 2 2 0 1]
 [2 1 0 2 2]]
shape: (6, 5)
L1 norm of alice: 4
L2 norm of alice: 2.449
dot(alice, bob):  0
cosine(alice, bob): 0.0
allele frequencies: [0.583 0.583 0.417 0.333 0.75 ]
similarity matrix shape: (6, 6)
[[1.   0.   0.62 0.74 0.54 0.57]
 [0.   1.   0.6  0.6  0.33 0.55]
 [0.62 0.6  1.   0.91 0.8  0.84]
 [0.74 0.6  0.91 1.   0.6  0.92]
 [0.54 0.33 0.8  0.6  1.   0.37]
 [0.57 0.55 0.84 0.92 0.37 1.  ]]
G.T shape: (5, 6)
A_inv =
 [[ 1. -1.]
 [-1.  2.]]
A @ A_inv =
 [[1. 0.]
 [0. 1.]]
equal to I? True
```

Notice a few things:

- Alice and Bob happen to be **orthogonal**: wherever one has an alternate allele, the other has none, so the dot product is 0. With centred data this would no longer be true, which is the point of the warning above.
- The similarity matrix $\mathbf{S}$ is $6\times6$, **symmetric**, and has ones on the diagonal (everyone is perfectly similar to themselves).
- `Gn @ Gn.T` computed all 36 dot products at once. This "normalise rows, then multiply by the transpose" trick is how nearest-neighbour search and attention scores are computed in practice.

## Biomedical connection

The genotype matrix is the central object of statistical genetics. A genome-wide association study (GWAS) tests each column of $\mathbf{G}$ against a disease label. A **polygenic risk score** for coronary artery disease is a dot product $\mathbf{w}^\top\mathbf{x}$ between a person's dosage vector and a vector of per-allele weights estimated from a GWAS; Khera et al. (2018) showed that scores of this form, built from millions of variants, identify people with risk comparable to that of monogenic familial hypercholesterolemia. You will build such scores in [GWAS and polygenic risk scores](../../genomics-foundations/gwas-and-polygenic-risk-scores/).

The matrix view also reveals hidden structure. People whose ancestors lived in the same region share allele frequencies, so their rows of $\mathbf{G}$ are more similar. In [eigenvectors, SVD and PCA](../../linear-algebra/eigenvectors-svd-and-pca/) we will extract that structure from $\mathbf{G}$ and see why it must be accounted for, or a model will confuse ancestry with disease risk.

Finally, clinical data (age, LDL, blood pressure) are also columns. In the capstone, a person becomes one long vector that concatenates genotype features and clinical features, and a cohort becomes one design matrix.

> [!CAUTION]
> Genotype vectors are identifying data. Even a few hundred SNPs can single out an individual and reveal information about their relatives. Real genotype matrices are held under strict access agreements (UK Biobank, All of Us); the examples in this course use synthetic data only.

## Practice

1. Compute $\lVert\mathbf{x}\rVert_1$ and $\lVert\mathbf{x}\rVert_2$ for $\mathbf{x} = (3, -4, 0, 12)$.

<details>
<summary>Answer</summary>

$\lVert\mathbf{x}\rVert_1 = 3 + 4 + 0 + 12 = 19$.
$\lVert\mathbf{x}\rVert_2 = \sqrt{9 + 16 + 0 + 144} = \sqrt{169} = 13$.

</details>

2. Find the cosine similarity between $\mathbf{u} = (1, 2, 2)$ and $\mathbf{v} = (2, 0, 1)$.

<details>
<summary>Answer</summary>

$\mathbf{u}\cdot\mathbf{v} = 2 + 0 + 2 = 4$. $\lVert\mathbf{u}\rVert = \sqrt{1+4+4} = 3$, $\lVert\mathbf{v}\rVert = \sqrt{4+0+1} = \sqrt5$.
Cosine $= 4/(3\sqrt5) = 4/6.708 \approx 0.596$.

</details>

3. A genotype matrix has 1,200 rows and 80,000 columns. What does row 7 represent, what does column 7 represent, and what is the shape of $\mathbf{G}^\top$?

<details>
<summary>Answer</summary>

Row 7 is the dosage vector of person 7 across all 80,000 SNPs. Column 7 is the dosages of SNP 7 across all 1,200 people. $\mathbf{G}^\top$ has shape $80{,}000 \times 1{,}200$.

</details>

4. Find the inverse of $\begin{bmatrix} 4 & 2 \\ 3 & 2\end{bmatrix}$, and explain why $\begin{bmatrix} 1 & 2 \\ 2 & 4\end{bmatrix}$ has none.

<details>
<summary>Answer</summary>

Determinant $= 4\cdot2 - 2\cdot3 = 2$. Inverse $= \tfrac12\begin{bmatrix} 2 & -2 \\ -3 & 4\end{bmatrix} = \begin{bmatrix} 1 & -1 \\ -1.5 & 2\end{bmatrix}$.
Check one entry: row 1 of the original times column 1 of the inverse is $4\cdot1 + 2\cdot(-1.5) = 1$.

The second matrix has determinant $1\cdot4 - 2\cdot2 = 0$: its second column is twice its first, so it collapses the plane onto a line and cannot be undone.

</details>

5. Show that if you centre two vectors (subtract each one's mean from its entries), their cosine similarity equals the Pearson correlation $r = \dfrac{\sum (x_i-\bar x)(y_i - \bar y)}{\sqrt{\sum(x_i-\bar x)^2}\sqrt{\sum(y_i-\bar y)^2}}$.

<details>
<summary>Answer</summary>

Let $\tilde x_i = x_i - \bar x$ and $\tilde y_i = y_i - \bar y$. Then $\tilde{\mathbf{x}}\cdot\tilde{\mathbf{y}} = \sum(x_i-\bar x)(y_i-\bar y)$, $\lVert\tilde{\mathbf{x}}\rVert_2 = \sqrt{\sum(x_i-\bar x)^2}$ and likewise for $\tilde{\mathbf{y}}$. Substituting into the cosine formula gives exactly $r$.

</details>

## Further reading

- Gilbert Strang, *Introduction to Linear Algebra*, Wellesley-Cambridge Press (chapters 1–2). The classic gentle introduction.
- Marc Peter Deisenroth, A. Aldo Faisal and Cheng Soon Ong, *Mathematics for Machine Learning*, Cambridge University Press, 2020 (chapters 2–3). Free online.
- Ian Goodfellow, Yoshua Bengio and Aaron Courville, *Deep Learning*, MIT Press, 2016 (chapter 2, "Linear Algebra").
- Amit V. Khera et al., "Genome-wide polygenic scores for common diseases identify individuals with risk equivalent to monogenic mutations", *Nature Genetics*, 2018.
