+++
summary = "Multiply matrices by hand and in code, read a linear layer y = Wx + b as a map between spaces, and track the shape of every tensor, including batches of one-hot DNA."
+++

# Matrix Multiplication and Tensors

A neural network is, to a first approximation, a stack of matrix multiplications with simple non-linear functions in between. When a deep model reads a DNA sequence and outputs a heart-disease risk, almost all of the arithmetic happens inside operations of the form $\mathbf{y} = \mathbf{W}\mathbf{x} + \mathbf{b}$. If you understand matrix multiplication and can keep track of array **shapes**, you can read any architecture diagram and debug most model code. Shape errors are the most common bug in deep learning; this chapter teaches you to avoid them.

## Key ideas

### Matrix times vector

Let $\mathbf{W}$ be an $m\times n$ matrix and $\mathbf{x}\in\mathbb{R}^n$. The product $\mathbf{W}\mathbf{x}$ is a vector in $\mathbb{R}^m$ whose $i$-th entry is the dot product of row $i$ of $\mathbf{W}$ with $\mathbf{x}$:

$$
(\mathbf{W}\mathbf{x})_i = \sum_{j=1}^{n} W_{ij}\,x_j
$$

There are two equally useful ways to read this.

- **Row view:** each output is a weighted sum of the inputs. Row $i$ of $\mathbf{W}$ is a "detector", and $(\mathbf{W}\mathbf{x})_i$ says how strongly $\mathbf{x}$ matches it.
- **Column view:** $\mathbf{W}\mathbf{x} = x_1\,\mathbf{w}_{:,1} + x_2\,\mathbf{w}_{:,2} + \dots + x_n\,\mathbf{w}_{:,n}$, a linear combination of the columns of $\mathbf{W}$ with the entries of $\mathbf{x}$ as weights.

### Matrix times matrix

If $\mathbf{A}$ is $m\times n$ and $\mathbf{B}$ is $n\times k$, then $\mathbf{C} = \mathbf{A}\mathbf{B}$ is $m\times k$ with

> [!IMPORTANT]
> $$C_{ij} = \sum_{l=1}^{n} A_{il}\,B_{lj} \qquad (m\times n)\,(n\times k) \to (m\times k)$$

Entry $(i,j)$ is row $i$ of $\mathbf{A}$ dotted with column $j$ of $\mathbf{B}$. The **inner dimensions must match** (both $n$), and they disappear; the outer dimensions survive. Saying the shapes out loud, "$m$ by $n$ times $n$ by $k$ gives $m$ by $k$", catches most errors before you run any code.

Key properties:

- **Associative:** $(\mathbf{A}\mathbf{B})\mathbf{C} = \mathbf{A}(\mathbf{B}\mathbf{C})$.
- **Distributive:** $\mathbf{A}(\mathbf{B} + \mathbf{C}) = \mathbf{A}\mathbf{B} + \mathbf{A}\mathbf{C}$.
- **Not commutative:** in general $\mathbf{A}\mathbf{B}\neq\mathbf{B}\mathbf{A}$, and often only one of them is even defined.
- **Transpose reverses order:** $(\mathbf{A}\mathbf{B})^\top = \mathbf{B}^\top\mathbf{A}^\top$.

Multiplying an $m\times n$ matrix by an $n\times k$ matrix costs $m\cdot n\cdot k$ multiply-adds. GPUs exist largely to do this fast.

### The linear layer as a linear map

A function $f$ is **linear** if $f(\mathbf{u} + \mathbf{v}) = f(\mathbf{u}) + f(\mathbf{v})$ and $f(c\,\mathbf{u}) = c\,f(\mathbf{u})$. Every matrix defines a linear function $\mathbf{x}\mapsto\mathbf{W}\mathbf{x}$, and every linear function between finite-dimensional spaces can be written as a matrix. So a matrix *is* a linear map: it can rotate, stretch, squash, project or reflect space, but it keeps straight lines straight and the origin fixed.

A neural network's **linear (fully connected, dense) layer** adds a bias:

> [!IMPORTANT]
> $$\mathbf{y} = \mathbf{W}\mathbf{x} + \mathbf{b}, \qquad \mathbf{x}\in\mathbb{R}^{n_\text{in}},\ \mathbf{W}\in\mathbb{R}^{n_\text{out}\times n_\text{in}},\ \mathbf{b}\in\mathbb{R}^{n_\text{out}},\ \mathbf{y}\in\mathbb{R}^{n_\text{out}}$$

Strictly, adding $\mathbf{b}$ makes the map **affine** (it moves the origin), but deep-learning usage calls it linear anyway. The layer has $n_\text{out}\cdot n_\text{in} + n_\text{out}$ parameters.

Why do we need non-linear activations between layers? Because composing linear maps gives another linear map: $\mathbf{W}_2(\mathbf{W}_1\mathbf{x}) = (\mathbf{W}_2\mathbf{W}_1)\mathbf{x}$. A hundred stacked linear layers without activations are no more expressive than one. This is the first lesson of [from perceptron to MLP](../../neural-networks/from-perceptron-to-mlp/).

### Shapes and the batch dimension

We never feed a network one example at a time; we feed a **batch** of $B$ examples. Stack the inputs as the rows of a matrix $\mathbf{X}\in\mathbb{R}^{B\times n_\text{in}}$. Then the whole batch is processed by one matrix multiplication:

$$
\underbrace{\mathbf{Y}}_{B\times n_\text{out}} = \underbrace{\mathbf{X}}_{B\times n_\text{in}}\;\underbrace{\mathbf{W}^\top}_{n_\text{in}\times n_\text{out}} + \underbrace{\mathbf{b}^\top}_{1\times n_\text{out}}
$$

Row $r$ of $\mathbf{Y}$ is exactly $\mathbf{W}\mathbf{x}_r + \mathbf{b}$ for example $r$, transposed into a row. PyTorch's `nn.Linear` stores `weight` with shape `(out_features, in_features)` and computes `x @ weight.T + bias`, which is this formula.

> [!TIP]
> By convention, **the batch dimension comes first** and is never mixed with the others: each example in a batch is processed independently. When reading model code, mentally drop the batch dimension, check the per-example shapes, then put it back.

### Tensors

A **tensor** (in the deep-learning sense) is just an array with any number of axes. A scalar has 0 axes, a vector 1, a matrix 2. Genomic models routinely use 3-axis tensors.

A DNA sequence of length $L$, one-hot encoded with $C = 4$ channels (A, C, G, T), is an $L\times 4$ matrix. A batch of $B$ such sequences is a tensor of shape

$$
(B, L, C) = (\text{batch}, \text{length}, \text{channels}).
$$

For example, 32 sequences of 1,000 base pairs form a $32\times1000\times4$ tensor with 128,000 entries. Some libraries prefer **channels-first** layout $(B, C, L)$; PyTorch's `Conv1d` does. Converting between them is a permutation of axes, not a reshape.

> [!WARNING]
> `x.reshape(B, C, L)` and `x.permute(0, 2, 1)` both produce shape $(B, C, L)$ from $(B, L, C)$, but only `permute` keeps each base in its own channel. `reshape` just re-reads the same numbers in a different order and silently scrambles the sequence. Use `permute` (or `transpose`) to swap axes.

A linear layer applied to a $(B, L, C)$ tensor acts on the **last** axis only: it maps each position's $C$-vector to an $n_\text{out}$-vector with the same weights, giving $(B, L, n_\text{out})$. That is exactly a width-1 convolution, and it is how transformers apply their feed-forward blocks to every token.

### Broadcasting

Element-wise operations (such as $+$, $-$, $\times$) between arrays of different shapes follow **broadcasting** rules (numpy and PyTorch use the same ones):

1. Line the shapes up from the **right**.
2. Two axes are compatible if they are equal or one of them is 1 (a missing axis counts as 1).
3. Axes of size 1 are virtually copied to match.

So $(B, n_\text{out}) + (n_\text{out},)$ works: the bias is added to every row. $(3, 6, 4) - (1, 1, 4)$ subtracts one per-channel mean from every position of every sequence. But $(3, 6, 4) + (6,)$ fails, because the last axes, 4 and 6, do not match.

> [!WARNING]
> Broadcasting can hide bugs. If `y` has shape `(B,)` and `pred` has shape `(B, 1)`, then `y - pred` has shape `(B, B)`, not `(B,)`, and a loss averaged over it will be silently wrong. Check shapes before reductions.

### Einstein summation (einsum)

`einsum` writes a tensor operation by naming every axis with a letter. Letters that appear in the inputs but not the output are **summed over**; the rest are kept.

| Operation | Formula | einsum string |
|---|---|---|
| dot product | $\sum_i x_i y_i$ | `"i,i->"` |
| matrix–vector | $y_i = \sum_j W_{ij}x_j$ | `"ij,j->i"` |
| matrix–matrix | $C_{ik} = \sum_j A_{ij}B_{jk}$ | `"ij,jk->ik"` |
| batched linear layer | $Y_{bo} = \sum_i X_{bi}W_{oi}$ | `"bi,oi->bo"` |
| transpose | $B_{ji} = A_{ij}$ | `"ij->ji"` |
| score each DNA position | $s_{bl} = \sum_c X_{blc}w_c$ | `"blc,c->bl"` |
| attention scores | $S_{bqk} = \sum_d Q_{bqd}K_{bkd}$ | `"bqd,bkd->bqk"` |

The last row is the heart of [attention](../../deep-architectures-for-sequences/attention-and-transformers/). Einsum strings double as documentation: they state the shapes.

## Worked example

**A linear layer by hand.** Let

$$
\mathbf{W} = \begin{bmatrix} 1 & 0 & -1 \\ 2 & 1 & 0 \end{bmatrix},\quad
\mathbf{x} = \begin{bmatrix} 1 \\ 2 \\ 3\end{bmatrix},\quad
\mathbf{b} = \begin{bmatrix} 0.5 \\ -1\end{bmatrix}.
$$

Shapes: $(2\times3)(3\times1) \to (2\times1)$. Good.

- Row 1: $1\cdot1 + 0\cdot2 + (-1)\cdot3 = 1 + 0 - 3 = -2$.
- Row 2: $2\cdot1 + 1\cdot2 + 0\cdot3 = 2 + 2 + 0 = 4$.

So $\mathbf{W}\mathbf{x} = (-2, 4)$ and $\mathbf{y} = \mathbf{W}\mathbf{x} + \mathbf{b} = (-1.5,\ 3)$.

Column view check: $1\cdot(1,2) + 2\cdot(0,1) + 3\cdot(-1,0) = (1 + 0 - 3,\ 2 + 2 + 0) = (-2, 4)$. Same answer.

**A batch.** Stack four inputs as rows: $(1,2,3)$, $(0,0,0)$, $(1,0,0)$, $(0,1,1)$. Then $\mathbf{X}$ is $4\times3$, $\mathbf{W}^\top$ is $3\times2$, and $\mathbf{X}\mathbf{W}^\top + \mathbf{b}^\top$ is $4\times2$:

- $(0,0,0)$ maps to $\mathbf{b} = (0.5, -1)$: the bias is the output for a zero input.
- $(1,0,0)$ maps to column 1 of $\mathbf{W}$ plus $\mathbf{b}$: $(1, 2) + (0.5, -1) = (1.5, 1)$.
- $(0,1,1)$: row 1 gives $0 + 0 - 1 = -1$, row 2 gives $0 + 1 + 0 = 1$; adding $\mathbf{b}$ gives $(-0.5, 0)$.

**Order matters.** With $\mathbf{A} = \begin{bmatrix}1&2\\3&4\end{bmatrix}$ and $\mathbf{B} = \begin{bmatrix}0&1\\1&0\end{bmatrix}$:

$$
\mathbf{A}\mathbf{B} = \begin{bmatrix} 1\cdot0+2\cdot1 & 1\cdot1+2\cdot0 \\ 3\cdot0+4\cdot1 & 3\cdot1+4\cdot0\end{bmatrix} = \begin{bmatrix}2&1\\4&3\end{bmatrix},\qquad
\mathbf{B}\mathbf{A} = \begin{bmatrix}3&4\\1&2\end{bmatrix}.
$$

$\mathbf{B}$ swaps things: on the right it swaps the columns of $\mathbf{A}$; on the left it swaps the rows.

**Shapes through a tiny DNA model.** Batch of $B = 32$ sequences, $L = 1000$, one-hot $C = 4$:

1. Input: $(32, 1000, 4)$.
2. Permute for `Conv1d`: $(32, 4, 1000)$.
3. `Conv1d(4, 64, kernel_size=9)` without padding: $(32, 64, 1000 - 9 + 1) = (32, 64, 992)$.
4. Average over the length axis: $(32, 64)$.
5. `Linear(64, 1)`: $(32, 1)$, one risk logit per sequence.

## In code

First, the worked example in numpy and PyTorch, with einsum as a cross-check.

```python
import numpy as np
import torch

# --- The worked example, in numpy ---
W = np.array([[1.0, 0.0, -1.0],
              [2.0, 1.0,  0.0]])        # (out=2, in=3)
b = np.array([0.5, -1.0])               # (2,)
x = np.array([1.0, 2.0, 3.0])           # (3,)
print("Wx + b =", W @ x + b)            # [-1.5  3. ]

# A batch of 4 inputs, one per row: (B=4, in=3)
X = np.array([[1.0, 2.0, 3.0],
              [0.0, 0.0, 0.0],
              [1.0, 0.0, 0.0],
              [0.0, 1.0, 1.0]])
Y = X @ W.T + b                         # (4,3)@(3,2) -> (4,2), b broadcasts
print("batched output:\n", Y)

# --- The same layer in PyTorch ---
layer = torch.nn.Linear(in_features=3, out_features=2)
with torch.no_grad():                   # copy our numbers into the layer
    layer.weight.copy_(torch.tensor(W))
    layer.bias.copy_(torch.tensor(b))
print("weight shape:", tuple(layer.weight.shape))   # (out, in)
Yt = layer(torch.tensor(X, dtype=torch.float32))
print("torch output:\n", Yt.detach().numpy())

# --- einsum: the same computation spelled out by index ---
Ye = np.einsum("bi,oi->bo", X, W) + b
print("einsum matches:", np.allclose(Y, Ye))

# Matrix multiplication is not commutative
A = np.array([[1, 2], [3, 4]])
B = np.array([[0, 1], [1, 0]])
print("AB =\n", A @ B)
print("BA =\n", B @ A)
```

```text
Wx + b = [-1.5  3. ]
batched output:
 [[-1.5  3. ]
 [ 0.5 -1. ]
 [ 1.5  1. ]
 [-0.5  0. ]]
weight shape: (2, 3)
torch output:
 [[-1.5  3. ]
 [ 0.5 -1. ]
 [ 1.5  1. ]
 [-0.5  0. ]]
einsum matches: True
AB =
 [[2 1]
 [4 3]]
BA =
 [[3 4]
 [1 2]]
```

Next, a batch of one-hot DNA sequences as a $(B, L, C)$ tensor, broadcasting, einsum, and the channels-first layout that `Conv1d` expects.

```python
import numpy as np
import torch

BASES = "ACGT"

def one_hot(seq):
    """Return an (L, 4) one-hot matrix for a DNA string."""
    idx = np.array([BASES.index(c) for c in seq])
    return np.eye(4, dtype=np.float32)[idx]      # pick rows of the identity

seqs = ["ACGTAC", "GGGTTA", "TACCAG"]            # B = 3 sequences, L = 6
X = np.stack([one_hot(s) for s in seqs])         # (B, L, C) = (3, 6, 4)
print("batch shape (B, L, C):", X.shape)
print("first sequence:\n", X[0])

# Base composition per sequence: sum over the length axis
print("base counts per sequence:\n", X.sum(axis=1))      # (3, 4)

# Score every position with a per-base weight vector (a width-1 "filter")
w = np.array([0.5, -1.0, 2.0, 0.0], dtype=np.float32)   # (C,)
scores = np.einsum("blc,c->bl", X, w)                    # (B, L)
print("per-position scores:\n", scores)
print("same as X @ w:", np.allclose(scores, X @ w))

# Broadcasting: subtract the per-channel mean over batch and length
mean = X.mean(axis=(0, 1), keepdims=True)                # (1, 1, 4)
Xc = X - mean                                            # (3,6,4) - (1,1,4)
print("mean shape:", mean.shape, "-> centred shape:", Xc.shape)

# PyTorch Conv1d expects (B, C, L): channels before length
xt = torch.from_numpy(X).permute(0, 2, 1)                # (3, 4, 6)
conv = torch.nn.Conv1d(in_channels=4, out_channels=8, kernel_size=3)
out = conv(xt)
print("conv input:", tuple(xt.shape), "-> output:", tuple(out.shape))

# A Linear layer acts on the LAST axis and keeps the others
lin = torch.nn.Linear(4, 16)
print("linear on (B, L, C):", tuple(lin(torch.from_numpy(X)).shape))
```

```text
batch shape (B, L, C): (3, 6, 4)
first sequence:
 [[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]
 [0. 0. 0. 1.]
 [1. 0. 0. 0.]
 [0. 1. 0. 0.]]
base counts per sequence:
 [[2. 2. 1. 1.]
 [1. 0. 3. 2.]
 [2. 2. 1. 1.]]
per-position scores:
 [[ 0.5 -1.   2.   0.   0.5 -1. ]
 [ 2.   2.   2.   0.   0.   0.5]
 [ 0.   0.5 -1.  -1.   0.5  2. ]]
same as X @ w: True
mean shape: (1, 1, 4) -> centred shape: (3, 6, 4)
conv input: (3, 4, 6) -> output: (3, 8, 4)
linear on (B, L, C): (3, 6, 16)
```

Two details to notice. One-hot encoding is itself a matrix operation: `np.eye(4)[idx]` selects rows of the identity matrix. And multiplying a one-hot row by a weight vector just *looks up* the weight for that base, which is why the per-position scores are drawn from $\{0.5, -1, 2, 0\}$. Embedding layers in language models work the same way.

## Biomedical connection

Every architecture in [deep architectures for sequences](../../deep-architectures-for-sequences/convolutional-networks-for-dna/) is a pipeline of tensor operations whose shapes you can now track. A convolutional filter sliding along a one-hot sequence takes, at each position, a dot product between a small $k\times4$ weight matrix and a $k\times4$ window of DNA; a filter that has learned a transcription-factor binding motif fires where that motif occurs. A transformer turns each position into a vector and computes all pairwise dot products in one batched matrix multiplication.

For tabular genetics, the batched linear layer $\mathbf{X}\mathbf{W}^\top + \mathbf{b}$ with one output is the polygenic score $\mathbf{w}^\top\mathbf{x} + b$ computed for a whole cohort at once. With $n = 400{,}000$ people and $p = 1{,}000{,}000$ SNPs, $\mathbf{X}\mathbf{w}$ needs $4\times10^{11}$ multiply-adds, and the dense genotype matrix stored as 32-bit floats would need 1.6 terabytes. That is why genetics software stores genotypes compactly (2 bits per dosage) and processes them in blocks, and why deep models usually see either a selected subset of variants or local sequence windows.

## Practice

1. $\mathbf{A}$ is $5\times3$, $\mathbf{B}$ is $3\times7$ and $\mathbf{C}$ is $7\times2$. What are the shapes of $\mathbf{A}\mathbf{B}$, $\mathbf{A}\mathbf{B}\mathbf{C}$ and $\mathbf{C}^\top\mathbf{B}^\top$? Is $\mathbf{B}\mathbf{A}$ defined?

<details>
<summary>Answer</summary>

$\mathbf{A}\mathbf{B}$: $5\times7$. $\mathbf{A}\mathbf{B}\mathbf{C}$: $5\times2$. $\mathbf{C}^\top\mathbf{B}^\top = (\mathbf{B}\mathbf{C})^\top$: $\mathbf{B}\mathbf{C}$ is $3\times2$, so this is $2\times3$. $\mathbf{B}\mathbf{A}$ would be $(3\times7)(5\times3)$; inner dimensions 7 and 5 differ, so it is **not defined**.

</details>

2. Compute $\begin{bmatrix}2 & -1\\ 0 & 3\end{bmatrix}\begin{bmatrix}1 & 4\\ 2 & -2\end{bmatrix}$.

<details>
<summary>Answer</summary>

Entry (1,1): $2\cdot1 + (-1)\cdot2 = 0$. (1,2): $2\cdot4 + (-1)(-2) = 10$. (2,1): $0\cdot1 + 3\cdot2 = 6$. (2,2): $0\cdot4 + 3\cdot(-2) = -6$.
Result: $\begin{bmatrix}0 & 10\\ 6 & -6\end{bmatrix}$.

</details>

3. A network takes 2,000 SNP dosages per person, has a hidden layer of 128 units and outputs 1 logit. How many parameters do the two linear layers have in total? With a batch of 64 people, what are the shapes of the input, the hidden activations and the output?

<details>
<summary>Answer</summary>

Layer 1: $128\times2000 + 128 = 256{,}128$. Layer 2: $1\times128 + 1 = 129$. Total $256{,}257$.
Shapes: input $(64, 2000)$, hidden $(64, 128)$, output $(64, 1)$.

</details>

4. Which of these broadcast, and to what shape? (a) $(8, 1, 4) + (5, 4)$ (b) $(8, 5) + (8,)$ (c) $(16, 100, 4) \times (4,)$.

<details>
<summary>Answer</summary>

(a) Align right: $(8,1,4)$ vs $(\,\cdot\,,5,4)$. Axes: $4{=}4$, $1$ vs $5$ OK, $8$ vs missing OK. Result $(8, 5, 4)$.
(b) Align right: last axes 5 vs 8 differ and neither is 1. **Error.** (To add a per-row value, use shape $(8, 1)$.)
(c) Last axes 4 and 4 match. Result $(16, 100, 4)$: each channel is scaled.

</details>

5. Write einsum strings for: (a) the trace $\sum_i A_{ii}$; (b) a batched matrix product of $(B, n, m)$ with $(B, m, k)$; (c) summing a $(B, L, C)$ tensor over length.

<details>
<summary>Answer</summary>

(a) `"ii->"`. (b) `"bnm,bmk->bnk"`. (c) `"blc->bc"`.

</details>

## Further reading

- Gilbert Strang, *Introduction to Linear Algebra*, Wellesley-Cambridge Press (chapters on matrix multiplication and linear transformations).
- Ian Goodfellow, Yoshua Bengio and Aaron Courville, *Deep Learning*, MIT Press, 2016 (chapter 2).
- The NumPy documentation on broadcasting and `numpy.einsum`, and the PyTorch documentation for `torch.nn.Linear` and `torch.nn.Conv1d`.
