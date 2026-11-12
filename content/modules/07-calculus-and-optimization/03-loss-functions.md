+++
summary = "Derive mean squared error and cross-entropy from likelihoods, compute their gradients (including the clean p − y), handle rare disease cases with class weights and focal loss, and compute losses stably from logits."
+++

# Loss Functions

A model learns by minimising a **loss**: one number that says how wrong its predictions are on the training data. The choice of loss quietly decides what the model is trying to do. Should a heart-disease model be judged by squared error, by log-probability, or by something that pays extra attention to rare cases? Should it output well-calibrated probabilities or just rank people correctly?

This chapter shows that the standard losses are not arbitrary recipes. Each one falls out of a probability model of the data through **maximum likelihood**, and each has a gradient simple enough to compute by hand. We then deal with two practical problems you will meet immediately with disease data: rare positive cases and numerical overflow.

## Key ideas

### From likelihood to loss

Suppose a model with parameters $\boldsymbol\theta$ assigns a probability (or probability density) $P(y_i\mid\mathbf{x}_i;\boldsymbol\theta)$ to each observed outcome. If the $n$ examples are independent, the probability of the whole dataset is the product, the **likelihood**:

$$
\mathcal{L}(\boldsymbol\theta) = \prod_{i=1}^n P(y_i\mid\mathbf{x}_i;\boldsymbol\theta).
$$

**Maximum likelihood** chooses the $\boldsymbol\theta$ that makes the observed data most probable. Products of many small numbers are awkward (and underflow on computers), so take logs, which turn products into sums and preserve where the maximum is. Then flip the sign so that we *minimise*:

> [!IMPORTANT]
> $$\text{loss}(\boldsymbol\theta) = -\frac1n\sum_{i=1}^n\log P(y_i\mid\mathbf{x}_i;\boldsymbol\theta)\qquad\text{(average negative log-likelihood, NLL)}$$

Every loss below is this formula with a different choice of probability distribution. (Likelihood is developed fully in [distributions and likelihood](../../probability-and-statistics/distributions-and-likelihood/).)

### Mean squared error from a Gaussian

For a continuous outcome, such as LDL cholesterol in mmol/L, assume the true value is the model's prediction plus Gaussian noise: $y_i = \hat y_i + \varepsilon_i$ with $\varepsilon_i\sim\mathcal{N}(0,\sigma^2)$. The density of one observation is

$$
P(y_i\mid\mathbf{x}_i) = \frac{1}{\sqrt{2\pi\sigma^2}}\exp\!\left(-\frac{(y_i - \hat y_i)^2}{2\sigma^2}\right).
$$

Its negative log is

$$
-\log P(y_i\mid\mathbf{x}_i) = \frac{(y_i - \hat y_i)^2}{2\sigma^2} + \frac12\log(2\pi\sigma^2).
$$

With $\sigma$ fixed, the second term is a constant and the first is the squared error times the positive constant $1/(2\sigma^2)$. Neither changes *where* the minimum is. So minimising the Gaussian NLL is the same as minimising

> [!IMPORTANT]
> $$\text{MSE} = \frac1n\sum_{i=1}^n(\hat y_i - y_i)^2,\qquad \frac{\partial\,\text{MSE}}{\partial\hat y_i} = \frac2n(\hat y_i - y_i)$$

The gradient is proportional to the error, signed: too high, push down; too low, push up. The derivation also tells you when MSE is a poor choice. Squaring makes large errors dominate, so a few outliers (a mis-entered lab value) can drag the fit. Assuming Laplace-distributed noise instead gives the **mean absolute error**, which is more robust to outliers.

### Binary cross-entropy from a Bernoulli

For a yes/no outcome, such as "has coronary artery disease", $y_i\in\{0, 1\}$. The model outputs a probability $p_i = P(y_i = 1\mid\mathbf{x}_i)$. A Bernoulli variable has

$$
P(y_i\mid\mathbf{x}_i) = p_i^{\,y_i}(1 - p_i)^{1 - y_i},
$$

which is just $p_i$ when $y_i = 1$ and $1 - p_i$ when $y_i = 0$, written as one formula. Taking the negative log:

> [!IMPORTANT]
> $$\text{BCE} = -\frac1n\sum_{i=1}^n\Big[y_i\log p_i + (1 - y_i)\log(1 - p_i)\Big]$$

For a case ($y = 1$) only $-\log p$ survives: the loss is near zero when the model gives the case a high probability and grows without bound as $p\to0$. Confident wrong answers are punished severely. This is also called **log-loss**.

**Logits and the clean gradient.** The network's last layer produces an unbounded score $z$, the **logit**, and $p = \sigma(z)$ with the sigmoid from [derivatives and gradients](../../calculus-and-optimization/derivatives-and-gradients/). Using the chain rule for one example:

$$
\frac{\partial L}{\partial p} = -\frac{y}{p} + \frac{1 - y}{1 - p},\qquad \frac{\partial p}{\partial z} = p(1 - p),
$$

$$
\frac{\partial L}{\partial z} = \Big(-\frac{y}{p} + \frac{1-y}{1-p}\Big)p(1-p) = -y(1-p) + (1-y)p = p - y.
$$

> [!IMPORTANT]
> For sigmoid + binary cross-entropy, $\dfrac{\partial L}{\partial z} = p - y$: predicted probability minus outcome.

The awkward $p(1-p)$ factor from the sigmoid cancels exactly. Compare MSE on top of a sigmoid, whose gradient $2(p - y)\,p(1-p)$ keeps that factor: when the model is confidently wrong ($p\approx0$ for a case), $p(1-p)\approx0$ and learning stalls. Cross-entropy keeps the gradient large precisely when the model is badly wrong. That, and its likelihood justification, is why classification uses cross-entropy.

The logit has its own meaning: since $p = \sigma(z)$, $z = \log\frac{p}{1-p}$, the **log-odds**. Logistic regression on SNP dosages is this model with $z = \mathbf{w}^\top\mathbf{x} + b$, and each weight is a log-odds ratio per allele ([linear and logistic regression](../../classical-machine-learning/linear-and-logistic-regression/)).

### Softmax and categorical cross-entropy

With $K > 2$ classes (say: no CAD, stable angina, prior myocardial infarction), the network outputs $K$ logits $\mathbf{z} = (z_1,\dots,z_K)$. The **softmax** turns them into probabilities that are positive and sum to 1:

$$
p_k = \operatorname{softmax}(\mathbf{z})_k = \frac{e^{z_k}}{\sum_{j=1}^K e^{z_j}}.
$$

The outcome is encoded one-hot, $\mathbf{y} = (0,\dots,1,\dots,0)$ with the 1 at the true class $c$. The categorical distribution gives $P(y = c) = p_c$, so the NLL for one example is

> [!IMPORTANT]
> $$\text{CE} = -\sum_{k=1}^K y_k\log p_k = -\log p_c$$

**The gradient.** Write the log-probability using the **log-sum-exp** function $\operatorname{LSE}(\mathbf{z}) = \log\sum_j e^{z_j}$:

$$
\log p_c = z_c - \operatorname{LSE}(\mathbf{z})\quad\Rightarrow\quad\text{CE} = \operatorname{LSE}(\mathbf{z}) - z_c.
$$

Now differentiate with respect to $z_k$. By the chain rule, $\dfrac{\partial\operatorname{LSE}}{\partial z_k} = \dfrac{1}{\sum_j e^{z_j}}\cdot e^{z_k} = p_k$. And $\partial z_c/\partial z_k$ is 1 if $k = c$ and 0 otherwise, which is $y_k$. So

$$
\frac{\partial\,\text{CE}}{\partial z_k} = p_k - y_k,\qquad\text{i.e.}\qquad \nabla_\mathbf{z}\,\text{CE} = \mathbf{p} - \mathbf{y}.
$$

The same clean form as the binary case (which is the special case $K = 2$). The gradient pushes the true class's logit up by $1 - p_c$ and every other logit down by its probability.

### Rare disease cases: class weighting

Many outcomes are rare. In a population cohort, a given disease might affect a few percent of participants; a monogenic cardiomyopathy far fewer. With 5% cases, the average BCE is dominated by the 95% controls, and the model can achieve a low loss by predicting a low probability for everyone.

That is not necessarily wrong: a model trained with plain BCE learns **calibrated** probabilities, and a predicted 5% risk for an average person is correct. The problem arises when you then threshold at 0.5 and find that it flags almost no cases. Two common responses:

**Class weighting.** Multiply each case's loss by a weight $w_+ > 1$:

$$
L = -\frac1n\sum_i\Big[w_+\,y_i\log p_i + (1 - y_i)\log(1 - p_i)\Big].
$$

A common choice is $w_+ = n_\text{controls}/n_\text{cases}$, which makes the two classes contribute equally in total. This is equivalent to duplicating each case $w_+$ times. PyTorch's `BCEWithLogitsLoss(pos_weight=...)` implements it.

**Focal loss** (Lin et al., 2017). Let $p_t$ be the probability the model assigns to the *true* class ($p_t = p$ for a case, $1 - p$ for a control). Then BCE is $-\log p_t$, and focal loss multiplies it by a factor that shrinks for easy examples:

> [!IMPORTANT]
> $$\text{FL} = -\alpha_t\,(1 - p_t)^\gamma\log p_t$$
> With $\gamma = 0$ and $\alpha_t = 1$ it is ordinary BCE. Typical values: $\gamma = 2$; $\alpha_t$ a class weight.

An example the model already gets right with $p_t = 0.9$ has its loss scaled by $(0.1)^2 = 0.01$; a hard example with $p_t = 0.1$ keeps $0.9^2 = 81\%$. Training effort shifts to the hard, often rare, examples.

> [!WARNING]
> Class weighting and focal loss distort predicted probabilities. A model trained with $w_+ = 19$ will systematically overestimate risk. If you need calibrated risks (and for clinical risk prediction you usually do), either train with plain cross-entropy and choose a decision threshold separately, or recalibrate afterwards ([model evaluation](../../classical-machine-learning/model-evaluation/)).

### Logits and numerical stability

Computers store numbers with limited range. In 64-bit floats, $e^{710}$ overflows to infinity; in 32-bit floats (the default for neural networks) the limit is near $e^{88}$. Naive softmax with logits like $(1000, 1001, 1002)$ computes $\infty/\infty$, which is NaN.

The fix is an identity: for any constant $m$,

$$
\operatorname{LSE}(\mathbf{z}) = m + \log\sum_j e^{z_j - m}.
$$

(Factor $e^m$ out of the sum.) Choose $m = \max_j z_j$. Then every exponent is $\le 0$, the largest term is $e^0 = 1$, and nothing overflows. Softmax is $p_k = e^{z_k - \operatorname{LSE}(\mathbf{z})}$, and softmax itself is unchanged by subtracting a constant from all logits.

The binary case has the same problem in another form. If the logit is $-120$, $\sigma(z)$ underflows to exactly 0 in float32, and $\log 0 = -\infty$. Working directly from the logit, BCE for a case can be written $\log(1 + e^{-z})$, which libraries evaluate stably.

> [!TIP]
> Make the network output **logits**, and use the loss functions that take logits: `nn.CrossEntropyLoss` (which applies log-softmax internally) and `nn.BCEWithLogitsLoss`. Apply `softmax` or `sigmoid` only when you need probabilities for reporting.

## Worked example

**1. MSE for LDL prediction.** Three people have measured LDL $(3.1, 4.0, 2.6)$ mmol/L and predictions $(3.4, 3.5, 2.9)$. Errors $\hat y - y$: $(0.3, -0.5, 0.3)$. Squares: $(0.09, 0.25, 0.09)$, sum $0.43$. MSE $= 0.43/3\approx0.1433$. Gradient for person 2: $\frac23(-0.5) = -0.333$; increasing that prediction reduces the loss.

**2. Binary cross-entropy.** A model predicts $p = 0.9$.
- If the person is a case ($y = 1$): $L = -\log0.9 = 0.1054$, gradient wrt the logit $p - y = -0.1$.
- If a control ($y = 0$): $L = -\log0.1 = 2.3026$, gradient $p - y = 0.9$.

Being confidently wrong costs about 22 times as much as being confidently right.

**3. Softmax and cross-entropy.** Logits $\mathbf{z} = (2, 1, 0)$, true class 1 (the first).
- Exponentials: $e^2 = 7.3891$, $e^1 = 2.7183$, $e^0 = 1$. Sum $= 11.1073$.
- Softmax: $\mathbf{p} = (7.3891, 2.7183, 1)/11.1073 = (0.6652,\ 0.2447,\ 0.0900)$.
- Loss: $-\log0.6652 = 0.4076$. Via LSE: $\log11.1073 - z_1 = 2.4076 - 2 = 0.4076$. Same.
- Gradient: $\mathbf{p} - \mathbf{y} = (0.6652 - 1,\ 0.2447,\ 0.0900) = (-0.3348,\ 0.2447,\ 0.0900)$. The components sum to 0, as they always do (both $\mathbf{p}$ and $\mathbf{y}$ sum to 1).

**4. Stability.** For $\mathbf{z} = (1000, 1001, 1002)$, take $m = 1002$: shifted logits $(-2, -1, 0)$, the same pattern as example 3 in reverse order. So $\operatorname{LSE} = 1002 + 2.4076 = 1002.4076$ and $\mathbf{p} = (0.0900, 0.2447, 0.6652)$, with no overflow.

**5. Focal loss** with $\gamma = 2$, $\alpha_t = 1$:
- Easy example, $p_t = 0.9$: BCE $0.1054$, focal $0.01\times0.1054 = 0.00105$.
- Hard example, $p_t = 0.1$: BCE $2.3026$, focal $0.81\times2.3026 = 1.8651$.

The hard-to-easy ratio rises from about 22 (BCE) to about 1,770 (focal).

## In code

First, confirm the softmax example, the $\mathbf{p} - \mathbf{y}$ gradient via autograd, and the stability issues.

```python
import numpy as np
import torch
import torch.nn.functional as F

# Worked example: 3-class softmax + cross-entropy
z = torch.tensor([2.0, 1.0, 0.0], requires_grad=True)   # logits
target = torch.tensor(0)                                 # true class index
p = torch.softmax(z, dim=0)
loss = F.cross_entropy(z.unsqueeze(0), target.unsqueeze(0))
loss.backward()
print("softmax p     :", p.detach().numpy().round(4))
print("cross-entropy :", round(loss.item(), 4))
print("autograd grad :", z.grad.numpy().round(4))
print("p - y         :", (p.detach() - F.one_hot(target, 3)).numpy().round(4))

# Naive softmax overflows for large logits; log-sum-exp does not
big = np.array([1000.0, 1001.0, 1002.0])
with np.errstate(over="ignore", invalid="ignore"):
    naive = np.exp(big) / np.exp(big).sum()
m = big.max()
lse = m + np.log(np.exp(big - m).sum())
print("naive softmax :", naive)
print("stable softmax:", np.exp(big - lse).round(4))
print("log-sum-exp   :", round(lse, 4))

# Binary case: never apply sigmoid then log yourself; use the logits version
logit = torch.tensor([-120.0])    # model is very sure the person is a control
y = torch.tensor([1.0])           # ...but they are a case
p1 = torch.sigmoid(logit)
print("sigmoid(-120) in float32:", p1.item())
print("naive BCE   :", F.binary_cross_entropy(p1, y).item())
print("logits BCE  :", F.binary_cross_entropy_with_logits(logit, y).item())
```

```text
softmax p     : [0.6652 0.2447 0.09  ]
cross-entropy : 0.4076
autograd grad : [-0.3348  0.2447  0.09  ]
p - y         : [-0.3348  0.2447  0.09  ]
naive softmax : [nan nan nan]
stable softmax: [0.09   0.2447 0.6652]
log-sum-exp   : 1002.4076
sigmoid(-120) in float32: 0.0
naive BCE   : 100.0
logits BCE  : 120.0
```

The naive binary loss reports 100 rather than the correct 120: PyTorch clamps $\log 0$ to $-100$ to avoid infinity, which hides the error and also gives a zero gradient. The logits version returns the exact value $\log(1 + e^{120})\approx120$.

Next, compare plain BCE, class-weighted BCE and focal loss on a synthetic cohort where about 5% of people are cases. Each trains the same logistic-regression model.

```python
import torch
import torch.nn.functional as F
from sklearn.metrics import roc_auc_score

torch.manual_seed(0)

# Synthetic cohort: 5,000 people, 10 features, about 5% are cases
n, d = 5000, 10
X = torch.randn(n, d)
true_w = torch.zeros(d)
true_w[:3] = torch.tensor([1.5, 1.0, -1.0])
y = (torch.rand(n) < torch.sigmoid(X @ true_w - 4.5)).float()
print(f"prevalence: {y.mean():.3f}")

def focal_loss(logits, y, gamma=2.0, alpha=0.75):
    """Binary focal loss (Lin et al., 2017), computed from logits."""
    bce = F.binary_cross_entropy_with_logits(logits, y, reduction="none")
    p_t = torch.exp(-bce)                       # probability of the true class
    alpha_t = alpha * y + (1 - alpha) * (1 - y)
    return (alpha_t * (1 - p_t) ** gamma * bce).mean()

n_pos = y.sum()
losses = {
    "plain BCE":   lambda z: F.binary_cross_entropy_with_logits(z, y),
    "weighted BCE": lambda z: F.binary_cross_entropy_with_logits(
        z, y, pos_weight=(n - n_pos) / n_pos),
    "focal":       lambda z: focal_loss(z, y),
}

for name, loss_fn in losses.items():
    w = torch.zeros(d, requires_grad=True)
    b = torch.zeros(1, requires_grad=True)
    opt = torch.optim.Adam([w, b], lr=0.05)
    for _ in range(500):                       # full-batch training
        opt.zero_grad()
        loss = loss_fn(X @ w + b)
        loss.backward()
        opt.step()
    with torch.no_grad():
        p = torch.sigmoid(X @ w + b)
    recall = ((p > 0.5) & (y == 1)).sum() / n_pos
    print(f"{name:12s}  mean predicted risk {p.mean():.3f}  "
          f"recall@0.5 {recall:.2f}  AUC {roc_auc_score(y, p):.3f}")
```

```text
prevalence: 0.050
plain BCE     mean predicted risk 0.051  recall@0.5 0.21  AUC 0.901
weighted BCE  mean predicted risk 0.278  recall@0.5 0.84  AUC 0.901
focal         mean predicted risk 0.242  recall@0.5 0.46  AUC 0.901
```

Read this carefully, because it contains the main lesson:

- **Plain BCE** is calibrated: mean predicted risk 0.051 matches the prevalence 0.050. At a 0.5 threshold it catches only 21% of cases.
- **Weighted BCE** catches 84% of cases at 0.5, but its mean predicted risk of 0.278 is more than five times the true prevalence. Its probabilities are no longer risks.
- **AUC is identical** for all three. For this linear model, the losses rank people in essentially the same order; they mainly shift where 0.5 falls. Choosing a threshold on the plain-BCE model would achieve similar recall while keeping calibrated risks.

Weighting and focal loss matter more for flexible deep models trained on very imbalanced data, where they change *what* the model spends its capacity learning. Even then, check calibration.

## Biomedical connection

The losses in this chapter map directly onto the prediction targets in a heart-disease project:

| Target | Example | Distribution | Loss |
|---|---|---|---|
| continuous biomarker | LDL cholesterol, lipoprotein(a) level | Gaussian | MSE |
| binary diagnosis | CAD case or control | Bernoulli | BCE with logits |
| several categories | cardiomyopathy subtype | categorical | softmax cross-entropy |
| time to event | age at first myocardial infarction | survival models | Cox partial likelihood (beyond this chapter) |

A multi-task model might predict LDL and CAD status together, adding an MSE term and a BCE term with weights chosen so that neither dominates.

Class imbalance is unavoidable. Even with a common disease like CAD, the number of incident cases over a few years of follow-up in a population cohort is a small fraction of participants, and for rare-variant conditions such as familial hypercholesterolemia (often due to variants in *LDLR*, *APOB* or *PCSK9*) the carriers are a small minority. The decision between "calibrated risk" and "flag more cases" is a clinical question, not only a technical one.

> [!CAUTION]
> A clinical risk score is useful only if a predicted 10% risk really corresponds to about 10% of such patients having the event. Loss tricks that improve recall at a fixed threshold can make the reported probabilities misleading. Report calibration alongside discrimination, and never present an uncalibrated score as an absolute risk.

## Practice

1. Show that if the Gaussian noise has a different known variance $\sigma_i^2$ for each person (for example because some lab measurements are less precise), maximum likelihood gives a **weighted** MSE. What are the weights?

<details>
<summary>Answer</summary>

$-\log P(y_i) = \dfrac{(y_i - \hat y_i)^2}{2\sigma_i^2} + \tfrac12\log(2\pi\sigma_i^2)$. The second term does not depend on the model, so we minimise $\sum_i\dfrac{1}{2\sigma_i^2}(y_i - \hat y_i)^2$: squared errors weighted by $1/\sigma_i^2$. Precise measurements count more.

</details>

2. A model outputs logit $z = 0$ for a case. Compute $p$, the BCE loss and $\partial L/\partial z$. Repeat for $z = 2$.

<details>
<summary>Answer</summary>

$z = 0$: $p = 0.5$, $L = -\log0.5 = 0.6931$, gradient $p - y = -0.5$.
$z = 2$: $p = \sigma(2) = 1/(1 + e^{-2}) = 0.8808$, $L = -\log0.8808 = 0.1269$, gradient $-0.1192$.

</details>

3. Logits $(0, 0, \ln 2)$, true class 3. Find the softmax probabilities, the loss and the gradient.

<details>
<summary>Answer</summary>

Exponentials $(1, 1, 2)$, sum 4. $\mathbf{p} = (0.25, 0.25, 0.5)$. Loss $= -\log0.5 = 0.6931$. Gradient $\mathbf{p} - \mathbf{y} = (0.25, 0.25, -0.5)$.

</details>

4. Show that adding the same constant $m$ to every logit leaves the softmax unchanged.

<details>
<summary>Answer</summary>

$\dfrac{e^{z_k + m}}{\sum_j e^{z_j + m}} = \dfrac{e^m e^{z_k}}{e^m\sum_j e^{z_j}} = \dfrac{e^{z_k}}{\sum_j e^{z_j}}$. This is why subtracting $\max_j z_j$ is safe.

</details>

5. A dataset has 400 cases and 9,600 controls. What `pos_weight` balances the classes? If a case currently gets $p = 0.2$, what is its contribution to the summed loss with and without the weight?

<details>
<summary>Answer</summary>

$w_+ = 9600/400 = 24$. Unweighted: $-\log0.2 = 1.609$. Weighted: $24\times1.609 = 38.63$.

</details>

## Further reading

- Christopher M. Bishop, *Pattern Recognition and Machine Learning*, Springer, 2006 (chapters 1.2, 4.3).
- Kevin P. Murphy, *Probabilistic Machine Learning: An Introduction*, MIT Press, 2022 (chapters on logistic regression and maximum likelihood).
- Ian Goodfellow, Yoshua Bengio and Aaron Courville, *Deep Learning*, MIT Press, 2016 (sections 5.5 and 6.2).
- Tsung-Yi Lin, Priya Goyal, Ross Girshick, Kaiming He and Piotr Dollár, "Focal loss for dense object detection", *ICCV*, 2017.
