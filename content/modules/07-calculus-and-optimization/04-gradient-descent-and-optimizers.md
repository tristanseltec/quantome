+++
summary = "Train models with gradient descent, predict when a learning rate converges or diverges, and understand SGD, momentum, RMSProp, Adam, learning-rate schedules and weight decay well enough to choose and tune them."
+++

# Gradient Descent and Optimizers

We can now compute the loss of a model ([loss functions](../../calculus-and-optimization/loss-functions/)) and its gradient with respect to every parameter ([backpropagation](../../calculus-and-optimization/the-chain-rule-and-backpropagation/)). The final step is to use the gradient to improve the parameters, over and over, until the model is good. The algorithms that do this are **optimizers**. Every model in this course, from logistic regression on SNP dosages to a transformer reading DNA, is trained by some variant of gradient descent, and a surprising share of "my model doesn't train" problems are optimizer problems: a learning rate too high or too low, a missing warmup, weight decay applied the wrong way.

This chapter builds each optimizer from the one before, with the exact update equations PyTorch uses.

## Key ideas

### Gradient descent

The gradient $\nabla L(\mathbf{w})$ points in the direction of steepest increase of the loss ([derivatives and gradients](../../calculus-and-optimization/derivatives-and-gradients/)). So take a small step the other way, and repeat:

> [!IMPORTANT]
> $$\mathbf{w}_{t+1} = \mathbf{w}_t - \eta\,\nabla L(\mathbf{w}_t)$$
> $\eta > 0$ is the **learning rate** (step size).

Near $\mathbf{w}_t$, the loss is approximately linear: $L(\mathbf{w}_t - \eta\mathbf{g})\approx L(\mathbf{w}_t) - \eta\lVert\mathbf{g}\rVert^2$, which is smaller as long as $\mathbf{g}\neq\mathbf{0}$ and $\eta$ is small enough for the linear approximation to hold. Gradient descent stops moving when the gradient is zero: at a minimum, but possibly also at a maximum or a saddle point.

### Convexity: when is the minimum the minimum?

A function is **convex** if the straight line between any two points on its graph lies on or above the graph:

$$
L(\theta\mathbf{a} + (1-\theta)\mathbf{b})\le\theta L(\mathbf{a}) + (1-\theta)L(\mathbf{b})\quad\text{for all }\mathbf{a},\mathbf{b}\text{ and }0\le\theta\le1.
$$

For a one-variable function, convex means the second derivative is $\ge0$ everywhere: the graph is a bowl, never a dome. The crucial property: **for a convex function, every local minimum is a global minimum**, so gradient descent with a suitable learning rate cannot get stuck in the wrong valley.

Linear regression with MSE and logistic regression with cross-entropy have convex losses. Neural networks do not: their losses have many minima and saddle points, and different initialisations reach different solutions. In practice, for large networks, many of the minima that gradient methods find generalise similarly well, but there is no guarantee; this is why random seeds matter and why we report variability across runs.

### The learning rate, worked out on a quadratic

The simplest convex function shows everything. Let $L(w) = \tfrac{a}{2}w^2$ with curvature $a > 0$ and minimum at $w = 0$. Then $L'(w) = aw$ and the update is

$$
w_{t+1} = w_t - \eta a w_t = (1 - \eta a)\,w_t\quad\Rightarrow\quad w_t = (1 - \eta a)^t\,w_0.
$$

Everything depends on the factor $r = 1 - \eta a$:

| Learning rate | Factor $r$ | Behaviour |
|---|---|---|
| $0 < \eta < 1/a$ | $0 < r < 1$ | smooth convergence (slow if $\eta$ is tiny) |
| $\eta = 1/a$ | $r = 0$ | lands on the minimum in one step |
| $1/a < \eta < 2/a$ | $-1 < r < 0$ | overshoots, oscillates, but converges |
| $\eta = 2/a$ | $r = -1$ | bounces forever between $\pm w_0$ |
| $\eta > 2/a$ | $r < -1$ | oscillates with growing amplitude: **diverges** |

> [!IMPORTANT]
> On a quadratic with curvature $a$, gradient descent converges if and only if $0 < \eta < 2/a$.

**More dimensions.** Near a minimum, any smooth loss looks like a quadratic bowl $\tfrac12\mathbf{w}^\top\mathbf{H}\mathbf{w}$, where $\mathbf{H}$ is the matrix of second derivatives (the **Hessian**). Its eigenvectors are the bowl's principal axes and its eigenvalues $\lambda_\text{max}\ge\dots\ge\lambda_\text{min}$ are the curvatures along them ([eigenvectors](../../linear-algebra/eigenvectors-svd-and-pca/)). Gradient descent acts on each axis separately, like the 1-D case. Stability requires $\eta < 2/\lambda_\text{max}$ (set by the *steepest* direction), but then progress along the *flattest* direction has factor $1 - \eta\lambda_\text{min}$, close to 1. The ratio $\kappa = \lambda_\text{max}/\lambda_\text{min}$, the **condition number**, measures how bad this is. A long narrow valley ($\kappa$ large) makes gradient descent zig-zag across the valley while creeping along it.

> [!TIP]
> Standardising input features (mean 0, variance 1) makes the loss bowl rounder and the condition number smaller. It is the cheapest optimisation trick there is. Clinical variables in mixed units (age in years, LDL in mmol/L, CRP in mg/L) badly need it.

### Stochastic gradient descent and mini-batches

The training loss is an average over $n$ examples, $L(\mathbf{w}) = \frac1n\sum_i\ell_i(\mathbf{w})$, so its gradient is the average of per-example gradients. With $n = 400{,}000$ people, computing it exactly for every step is wasteful. **Stochastic gradient descent (SGD)** estimates it from a random **mini-batch** $\mathcal{B}$ of $B$ examples:

$$
\mathbf{g}_t = \frac1B\sum_{i\in\mathcal{B}}\nabla\ell_i(\mathbf{w}_t),\qquad\mathbf{w}_{t+1} = \mathbf{w}_t - \eta\,\mathbf{g}_t.
$$

Because the batch is random, $\mathbf{g}_t$ is an **unbiased** estimate of the full gradient (correct on average), and its variance shrinks in proportion to $1/B$. One pass through the whole training set is an **epoch**; data are reshuffled each epoch.

The noise is not only a cost. It lets SGD take many cheap steps instead of a few expensive ones, and it helps the optimiser escape saddle points and sharp minima. Typical batch sizes are 32 to 1,024, often limited by GPU memory for long DNA sequences.

### Momentum

Gradient descent in a narrow valley zig-zags: the gradient components across the valley flip sign each step, while the component along the valley is small but consistent. **Momentum** keeps a running "velocity" that accumulates past gradients:

> [!IMPORTANT]
> $$\mathbf{v}_t = \beta\,\mathbf{v}_{t-1} + \mathbf{g}_t,\qquad\mathbf{w}_{t+1} = \mathbf{w}_t - \eta\,\mathbf{v}_t\qquad(\beta\approx0.9)$$

Oscillating components cancel in the sum; consistent components add up. If the gradient were constant, $\mathbf{v}$ would approach $\mathbf{g}(1 + \beta + \beta^2 + \dots) = \mathbf{g}/(1-\beta)$: with $\beta = 0.9$, ten times the step of plain GD along consistent directions. Picture a heavy ball rolling down the valley, which gains speed downhill and averages out the bumps. (This is the form PyTorch's `SGD(momentum=0.9)` uses.)

### RMSProp: a learning rate per parameter

Different parameters can need very different step sizes. A weight attached to a rare variant gets a non-zero gradient only in the few batches containing a carrier; a bias gets one every step. **RMSProp** (Tieleman and Hinton, 2012) divides each parameter's step by a running root-mean-square of its recent gradients:

> [!IMPORTANT]
> $$\mathbf{r}_t = \rho\,\mathbf{r}_{t-1} + (1-\rho)\,\mathbf{g}_t^2,\qquad\mathbf{w}_{t+1} = \mathbf{w}_t - \frac{\eta}{\sqrt{\mathbf{r}_t} + \epsilon}\odot\mathbf{g}_t$$
> All operations are element-wise; $\rho\approx0.9$ to $0.99$; $\epsilon\approx10^{-8}$ prevents division by zero.

Parameters with consistently large gradients (steep directions) get smaller steps; parameters with small gradients (flat directions) get larger ones. This partly undoes poor conditioning, at least along the coordinate axes. Roughly, the step size per parameter becomes about $\eta$, whatever the gradient's scale.

### Adam

**Adam** (Kingma and Ba, 2015) combines momentum (a running mean of gradients, the "first moment") with RMSProp (a running mean of squared gradients, the "second moment"), and corrects a start-up bias:

> [!IMPORTANT]
> $$\begin{aligned}
> \mathbf{m}_t &= \beta_1\mathbf{m}_{t-1} + (1-\beta_1)\,\mathbf{g}_t &&\text{first moment}\\
> \mathbf{v}_t &= \beta_2\mathbf{v}_{t-1} + (1-\beta_2)\,\mathbf{g}_t^2 &&\text{second moment}\\
> \hat{\mathbf{m}}_t &= \frac{\mathbf{m}_t}{1-\beta_1^t},\quad\hat{\mathbf{v}}_t = \frac{\mathbf{v}_t}{1-\beta_2^t} &&\text{bias correction}\\
> \mathbf{w}_{t+1} &= \mathbf{w}_t - \eta\,\frac{\hat{\mathbf{m}}_t}{\sqrt{\hat{\mathbf{v}}_t} + \epsilon}
> \end{aligned}$$
> Defaults: $\beta_1 = 0.9$, $\beta_2 = 0.999$, $\epsilon = 10^{-8}$, $\mathbf{m}_0 = \mathbf{v}_0 = \mathbf{0}$; $t$ counts steps from 1.

**Why bias correction?** The moments start at zero, so early averages are pulled toward zero. If every gradient so far equalled $\mathbf{g}$, then $\mathbf{m}_t = (1-\beta_1)(1 + \beta_1 + \dots + \beta_1^{t-1})\mathbf{g} = (1 - \beta_1^t)\,\mathbf{g}$ (a geometric series). Dividing by $1 - \beta_1^t$ recovers exactly $\mathbf{g}$. The same holds for $\mathbf{v}_t$. Without the correction, $\mathbf{v}$ (with $\beta_2 = 0.999$) stays tiny for hundreds of steps, and since it sits in the denominator, the first steps would be far too large. As $t$ grows, $\beta^t\to0$ and the correction fades away.

Adam is the default optimiser for most deep learning, including genomic sequence models, because it works reasonably well with little tuning. A learning rate around $10^{-3}$ is a common starting point for small models, and smaller for large transformers.

### Learning-rate schedules and warmup

A fixed learning rate is a compromise: large is fast early on but leaves the parameters bouncing around the minimum (with SGD noise, it cannot settle); small settles precisely but is slow. **Schedules** change $\eta$ over training:

- **Step decay:** multiply $\eta$ by, say, 0.1 at fixed epochs.
- **Cosine decay** (Loshchilov and Hutter, 2017): $\eta_t = \eta_\text{min} + \tfrac12(\eta_\text{max} - \eta_\text{min})\bigl(1 + \cos(\pi t/T)\bigr)$, a smooth fall from $\eta_\text{max}$ to $\eta_\text{min}$ over $T$ steps.
- **Linear warmup:** start near zero and increase linearly to $\eta_\text{max}$ over the first few hundred or thousand steps, then decay.

Warmup protects the start of training, when weights are random, gradients can be large and erratic, and Adam's second-moment estimates are still based on few samples. It is close to essential for training transformers and for very large batch sizes (Goyal et al., 2017). **Warmup followed by cosine decay** is a common default.

> [!TIP]
> To find a reasonable learning rate quickly, train briefly at several values spaced by factors of about 3 (for example $10^{-4}, 3\times10^{-4}, 10^{-3}, 3\times10^{-3}$) and pick the largest that trains stably. If the loss becomes NaN or jumps upward, the rate is too high.

### Weight decay versus L2 regularisation

**L2 regularisation** adds a penalty to the loss: $L_\text{reg} = L + \tfrac{\lambda}{2}\lVert\mathbf{w}\rVert^2$, whose gradient adds $\lambda\mathbf{w}$. With plain SGD:

$$
\mathbf{w}_{t+1} = \mathbf{w}_t - \eta(\mathbf{g}_t + \lambda\mathbf{w}_t) = (1 - \eta\lambda)\,\mathbf{w}_t - \eta\,\mathbf{g}_t.
$$

Each step first shrinks the weights by the factor $(1 - \eta\lambda)$, hence the name **weight decay**. For SGD, L2 penalty and weight decay are the same thing.

For Adam they are **not**. If you add $\lambda\mathbf{w}$ to the gradient, it passes through the adaptive denominator $\sqrt{\hat{\mathbf{v}}_t}$, so weights with large gradient history are barely regularised and weights with small gradients are regularised heavily, which is not what L2 intends. **AdamW** (Loshchilov and Hutter, 2019) **decouples** the decay from the gradient:

$$
\mathbf{w}_{t+1} = \mathbf{w}_t - \eta\Big(\frac{\hat{\mathbf{m}}_t}{\sqrt{\hat{\mathbf{v}}_t} + \epsilon} + \lambda\,\mathbf{w}_t\Big),
$$

where $\hat{\mathbf{m}}_t$ and $\hat{\mathbf{v}}_t$ are computed from the loss gradient alone. In PyTorch, `Adam(weight_decay=...)` implements the coupled L2 version and `AdamW(weight_decay=...)` the decoupled one. Use AdamW. Regularisation itself is the topic of [regularisation and the bias–variance tradeoff](../../classical-machine-learning/regularization-and-the-bias-variance-tradeoff/).

## Worked example

**1. Learning rates on $L(w) = 2w^2$** (so $a = 4$, $2/a = 0.5$), starting at $w_0 = 1$, $L_0 = 2$:

| $\eta$ | $r = 1 - 4\eta$ | $w_1$ | $w_2$ | $w_3$ | verdict |
|---|---|---|---|---|---|
| 0.1 | 0.6 | 0.6 | 0.36 | 0.216 | smooth convergence |
| 0.25 | 0 | 0 | 0 | 0 | one step |
| 0.4 | −0.6 | −0.6 | 0.36 | −0.216 | oscillating convergence |
| 0.5 | −1 | −1 | 1 | −1 | stuck bouncing |
| 0.6 | −1.4 | −1.4 | 1.96 | −2.744 | divergence |

For $\eta = 0.1$ the loss goes $2\to0.72\to0.2592\to0.0933$, falling by the factor $r^2 = 0.36$ each step. Note that $\eta = 0.1$ and $\eta = 0.4$ converge at the *same* speed ($\lvert r\rvert = 0.6$), one from one side, the other by overshooting.

**2. An ill-conditioned bowl.** $L(\mathbf{w}) = \tfrac12(w_1^2 + 25w_2^2)$ has curvatures 1 and 25, so $\kappa = 25$. Stability needs $\eta < 2/25 = 0.08$. Even the best single learning rate, $\eta = 2/(1 + 25)\approx0.077$, reduces the error along each axis only by a factor of $(\kappa - 1)/(\kappa + 1) = 24/26\approx0.92$ per step. The code below confirms that $\eta = 0.081$ diverges while $\eta = 0.07$ converges.

**3. Adam's first step.** One parameter, $\eta = 0.01$, default betas, first gradient $g_1 = 2$:
- $m_1 = 0.9\cdot0 + 0.1\cdot2 = 0.2$; $\hat m_1 = 0.2/(1 - 0.9) = 2$.
- $v_1 = 0.999\cdot0 + 0.001\cdot4 = 0.004$; $\hat v_1 = 0.004/(1 - 0.999) = 4$.
- Step: $0.01\cdot2/(\sqrt4 + 10^{-8})\approx0.01$.

The first step has size $\eta$ whatever the gradient's magnitude: $g_1 = 2000$ would give the same step. Without bias correction, the step would be $0.01\cdot0.2/\sqrt{0.004} = 0.01\cdot3.162 = 0.0316$, more than three times too large.

**4. Weight decay.** With SGD, $\eta = 0.1$ and $\lambda = 0.01$, every step multiplies the weights by $1 - 0.001 = 0.999$ before the gradient step. Over 1,000 steps, with no gradient pushing back, a weight would shrink by $0.999^{1000}\approx0.37$.

## In code

First, gradient descent, momentum, RMSProp and Adam implemented directly from the equations, on the ill-conditioned bowl from worked example 2.

```python
import numpy as np

# An ill-conditioned bowl: f(w) = 0.5 * (w1^2 + 25 * w2^2), minimum at (0, 0)
A = np.array([1.0, 25.0])                 # curvatures (Hessian diagonal)
f = lambda w: 0.5 * np.sum(A * w**2)
grad = lambda w: A * w

def run(update, steps=100, w0=(-4.0, 1.0)):
    w, state = np.array(w0), {}
    for t in range(1, steps + 1):
        w = update(w, grad(w), state, t)
    return f(w)

def gd(lr):
    return lambda w, g, s, t: w - lr * g

def momentum(lr, beta=0.9):
    def step(w, g, s, t):
        s["v"] = beta * s.get("v", 0) + g          # velocity
        return w - lr * s["v"]
    return step

def rmsprop(lr, rho=0.9, eps=1e-8):
    def step(w, g, s, t):
        s["r"] = rho * s.get("r", 0) + (1 - rho) * g**2
        return w - lr * g / (np.sqrt(s["r"]) + eps)
    return step

def adam(lr, b1=0.9, b2=0.999, eps=1e-8):
    def step(w, g, s, t):
        s["m"] = b1 * s.get("m", 0) + (1 - b1) * g
        s["v"] = b2 * s.get("v", 0) + (1 - b2) * g**2
        m_hat = s["m"] / (1 - b1**t)               # bias correction
        v_hat = s["v"] / (1 - b2**t)
        return w - lr * m_hat / (np.sqrt(v_hat) + eps)
    return step

print(f"start: f = {f(np.array([-4.0, 1.0])):.2f}")
for lr in [0.01, 0.07, 0.081]:
    print(f"GD        lr={lr:<6} f after 100 steps = {run(gd(lr)):.3e}")
print(f"Momentum  lr=0.01   f after 100 steps = {run(momentum(0.01)):.3e}")
print(f"RMSProp   lr=0.05   f after 100 steps = {run(rmsprop(0.05)):.3e}")
print(f"Adam      lr=0.1    f after 100 steps = {run(adam(0.1)):.3e}")
```

```text
start: f = 20.50
GD        lr=0.01   f after 100 steps = 1.072e+00
GD        lr=0.07   f after 100 steps = 3.978e-06
GD        lr=0.081  f after 100 steps = 1.745e+03
Momentum  lr=0.01   f after 100 steps = 5.610e-05
RMSProp   lr=0.05   f after 100 steps = 8.230e-03
Adam      lr=0.1    f after 100 steps = 3.374e-04
```

What this shows:

- GD with $\eta = 0.01$ is safe but slow along the flat axis: $0.99^{100}\approx0.37$, so $w_1$ is still about $-1.46$.
- $\eta = 0.081$ is just above $2/25$; the steep coordinate grows by a factor of $1.025$ per step and the loss explodes from 20.5 to 1,745.
- Momentum with the *same* small rate as the slow GD run reaches $5.6\times10^{-5}$: the velocity builds up along the flat axis.
- RMSProp and Adam make fast early progress, but with a constant learning rate they end up hovering near the minimum with steps of roughly size $\eta$ rather than converging exactly. That is one reason to decay the learning rate.

Second, the PyTorch optimizers on a more realistic task: a small network trained with mini-batches on a synthetic binary outcome, with a few badly scaled features to make the problem ill-conditioned. The last configuration uses AdamW with linear warmup and cosine decay.

```python
import math
import torch

torch.manual_seed(0)

# Synthetic cohort: 2,000 people x 50 features (e.g. standardised SNP dosages)
n, d = 2000, 50
X = torch.randn(n, d)
X[:, :5] *= 5.0                              # a few features on a larger scale
true_w = torch.randn(d) / math.sqrt(d)
y = (torch.rand(n) < torch.sigmoid(X @ true_w)).float()

def make_model():
    torch.manual_seed(1)                     # identical start for every optimizer
    return torch.nn.Sequential(torch.nn.Linear(d, 32), torch.nn.ReLU(),
                               torch.nn.Linear(32, 1))

def warmup_cosine(total, warmup):
    """Multiplier on the base learning rate: linear warmup, then cosine decay."""
    def f(step):
        if step < warmup:
            return (step + 1) / warmup
        progress = (step - warmup) / max(1, total - warmup)
        return 0.5 * (1 + math.cos(math.pi * progress))
    return f

configs = {
    "SGD":            lambda p: torch.optim.SGD(p, lr=0.01),
    "SGD + momentum": lambda p: torch.optim.SGD(p, lr=0.01, momentum=0.9),
    "RMSprop":        lambda p: torch.optim.RMSprop(p, lr=1e-3),
    "Adam":           lambda p: torch.optim.Adam(p, lr=1e-3),
    "AdamW + sched":  lambda p: torch.optim.AdamW(p, lr=3e-3, weight_decay=1e-2),
}

epochs, batch = 20, 64
steps = epochs * math.ceil(n / batch)
loss_fn = torch.nn.BCEWithLogitsLoss()
for name, make_opt in configs.items():
    model = make_model()
    opt = make_opt(model.parameters())
    sched = None
    if "sched" in name:
        sched = torch.optim.lr_scheduler.LambdaLR(opt, warmup_cosine(steps, 100))
    for epoch in range(epochs):
        perm = torch.randperm(n)             # reshuffle every epoch
        for i in range(0, n, batch):
            idx = perm[i:i + batch]          # one mini-batch
            opt.zero_grad()
            loss = loss_fn(model(X[idx]).squeeze(1), y[idx])
            loss.backward()
            opt.step()
            if sched:
                sched.step()
        if epoch in (0, 4, 19):
            with torch.no_grad():
                full = loss_fn(model(X).squeeze(1), y).item()
            print(f"{name:15s} epoch {epoch + 1:2d}  training loss {full:.4f}")
```

```text
SGD             epoch  1  training loss 0.5973
SGD             epoch  5  training loss 0.4761
SGD             epoch 20  training loss 0.4168
SGD + momentum  epoch  1  training loss 0.4478
SGD + momentum  epoch  5  training loss 0.3816
SGD + momentum  epoch 20  training loss 0.2948
RMSprop         epoch  1  training loss 0.4159
RMSprop         epoch  5  training loss 0.3509
RMSprop         epoch 20  training loss 0.2945
Adam            epoch  1  training loss 0.5396
Adam            epoch  5  training loss 0.3794
Adam            epoch 20  training loss 0.3031
AdamW + sched   epoch  1  training loss 0.5965
AdamW + sched   epoch  5  training loss 0.3405
AdamW + sched   epoch 20  training loss 0.2771
```

Plain SGD lags far behind; momentum and the adaptive methods are much faster. AdamW with a schedule starts slowly, because its first 100 steps are warmup (an epoch here is 32 mini-batches, so warmup spans about three epochs), and ends lowest. Treat the ranking with care: it is one seed, one problem and untuned learning rates, and these are *training* losses. Whether a lower training loss gives better predictions on new people is a separate question, answered on held-out data ([model evaluation](../../classical-machine-learning/model-evaluation/)).

## Biomedical connection

Genomic data stress optimizers in specific ways:

- **Sparse, rare features.** Rare-variant dosages are zero for almost everyone, so their weights receive gradient only in the occasional mini-batch that contains a carrier. Adaptive methods (RMSProp, Adam) give these parameters larger effective steps when their gradients do appear, which is one reason Adam is popular for genomic models.
- **Mixed scales.** Combining standardised genotypes with raw clinical variables creates exactly the ill-conditioned valley in worked example 2. Standardise every input.
- **Long sequences, small batches.** DNA models that read tens of thousands of bases often fit only a handful of sequences in GPU memory, so gradients are noisy. Warmup, a decaying schedule, and techniques like gradient accumulation (summing gradients over several small batches before stepping) help.
- **Many parameters, few cases.** A deep model with millions of weights trained on a few thousand cases can memorise the training cohort. Weight decay (AdamW), early stopping on a validation set and the regularisers in [training deep networks](../../neural-networks/training-deep-networks/) are standard defences.

When you build the capstone model in [designing a deep learning model](../../capstone-heart-disease-risk/designing-a-deep-learning-model/), the optimizer choices (AdamW, warmup plus cosine decay, a learning-rate sweep) will be part of the design, recorded and reported like any other modelling decision.

> [!CAUTION]
> Training runs differ with random seeds, data order and hardware. A risk model that looks better than a baseline by a small margin in one run may not be better at all. Repeat training with several seeds and report the spread before drawing conclusions that could influence clinical decisions.

## Practice

1. For $L(w) = 5w^2$, what is the largest learning rate for which gradient descent converges? Which learning rate reaches the minimum in one step?

<details>
<summary>Answer</summary>

$L(w) = \tfrac{a}{2}w^2$ with $a = 10$. Converges for $0 < \eta < 2/10 = 0.2$. One step: $\eta = 1/a = 0.1$ (factor $1 - 0.1\cdot10 = 0$).

</details>

2. Run three steps of gradient descent on $L(w_1, w_2) = w_1^2 + 4w_2^2$ from $(1, 1)$ with $\eta = 0.2$. What happens to each coordinate?

<details>
<summary>Answer</summary>

Gradient $(2w_1, 8w_2)$. Factors: $w_1$: $1 - 0.4 = 0.6$; $w_2$: $1 - 1.6 = -0.6$.
Step 1: $(0.6, -0.6)$. Step 2: $(0.36, 0.36)$. Step 3: $(0.216, -0.216)$.
$w_1$ decreases smoothly; $w_2$ overshoots and oscillates, but both shrink by 0.6 per step.

</details>

3. With momentum $\beta = 0.9$ and a constant gradient $g = 1$, starting from $v_0 = 0$, compute $v_1, v_2, v_3$. What value does $v_t$ approach?

<details>
<summary>Answer</summary>

$v_1 = 1$, $v_2 = 0.9 + 1 = 1.9$, $v_3 = 1.71 + 1 = 2.71$. It approaches $1/(1 - 0.9) = 10$.

</details>

4. In Adam with $\beta_2 = 0.999$, what is the bias-correction factor $1/(1 - \beta_2^t)$ at $t = 1$, $t = 10$ and $t = 1000$? (Use $0.999^{10}\approx0.990$ and $0.999^{1000}\approx0.368$.)

<details>
<summary>Answer</summary>

$t = 1$: $1/0.001 = 1000$. $t = 10$: $1/(1 - 0.990) = 1/0.010\approx100$. $t = 1000$: $1/(1 - 0.368) = 1/0.632\approx1.58$. The correction is enormous at first and fades over thousands of steps.

</details>

5. Explain why `torch.optim.Adam(params, weight_decay=0.01)` and `torch.optim.AdamW(params, weight_decay=0.01)` behave differently, while for SGD the two notions coincide.

<details>
<summary>Answer</summary>

`Adam(weight_decay)` adds $\lambda\mathbf{w}$ to the gradient, so the decay term is divided by $\sqrt{\hat{\mathbf{v}}}+\epsilon$ like the rest of the gradient: parameters with large past gradients are barely decayed. `AdamW` subtracts $\eta\lambda\mathbf{w}$ directly, so all weights shrink at the same relative rate. For SGD there is no per-parameter denominator, so adding $\lambda\mathbf{w}$ to the gradient gives exactly $\mathbf{w}\leftarrow(1 - \eta\lambda)\mathbf{w} - \eta\mathbf{g}$.

</details>

## Further reading

- Diederik P. Kingma and Jimmy Ba, "Adam: A method for stochastic optimization", *ICLR*, 2015.
- Ilya Loshchilov and Frank Hutter, "Decoupled weight decay regularization", *ICLR*, 2019.
- Ilya Loshchilov and Frank Hutter, "SGDR: Stochastic gradient descent with warm restarts", *ICLR*, 2017.
- Priya Goyal et al., "Accurate, large minibatch SGD: Training ImageNet in 1 hour", arXiv:1706.02677, 2017.
- Tijmen Tieleman and Geoffrey Hinton, Lecture 6.5, "RMSProp: Divide the gradient by a running average of its recent magnitude", *Coursera: Neural Networks for Machine Learning*, 2012.
- Ilya Sutskever, James Martens, George Dahl and Geoffrey Hinton, "On the importance of initialization and momentum in deep learning", *ICML*, 2013.
- Stephen Boyd and Lieven Vandenberghe, *Convex Optimization*, Cambridge University Press, 2004.
- Ian Goodfellow, Yoshua Bengio and Aaron Courville, *Deep Learning*, MIT Press, 2016 (chapter 8, "Optimization for Training Deep Models").
