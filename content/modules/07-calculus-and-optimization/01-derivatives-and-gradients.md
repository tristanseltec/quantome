+++
summary = "Compute derivatives, partial derivatives, gradients and Jacobians by hand, and check them numerically with finite differences."
+++

# Derivatives and Gradients

Training a model means adjusting its parameters to make its predictions less wrong. A heart-disease risk model may have one parameter per SNP or millions of parameters in a deep network. To improve them we need to answer, for every parameter at once: *if I nudge this number up a little, does the error go up or down, and how fast?* That question is answered by the **derivative**, and its many-parameter version, the **gradient**. Everything in the rest of this module (backpropagation, loss functions, optimisers) is built on this chapter.

You need no prior calculus. We start from slopes of straight lines, which you know from GMAT coordinate geometry.

## Key ideas

### The derivative as a rate of change

For a straight line $y = mx + c$, the slope $m$ tells you how much $y$ changes per unit change in $x$, everywhere. A curve has no single slope, but if you zoom in far enough on any smooth curve it looks straight. The **derivative** at a point is the slope of that zoomed-in line, the **tangent line**.

To compute it, take the slope between $x$ and a nearby point $x + h$, then let $h$ shrink to zero:

> [!IMPORTANT]
> $$f'(x) = \frac{df}{dx} = \lim_{h\to0}\frac{f(x+h) - f(x)}{h}$$

**Example from the definition.** For $f(x) = x^2$:

$$
\frac{(x+h)^2 - x^2}{h} = \frac{x^2 + 2xh + h^2 - x^2}{h} = 2x + h \ \xrightarrow{h\to0}\ 2x.
$$

So the slope of $x^2$ at $x = 3$ is 6: near $x = 3$, increasing $x$ by a small amount $\Delta x$ increases $f$ by about $6\,\Delta x$. That approximation is the most useful way to think about derivatives:

$$
f(x + \Delta x) \approx f(x) + f'(x)\,\Delta x \qquad\text{for small }\Delta x.
$$

The sign tells you direction: $f'(x) > 0$ means $f$ is increasing, $f'(x) < 0$ decreasing. At a minimum or maximum of a smooth function, $f'(x) = 0$; the tangent is flat. That is why training looks for points where derivatives vanish.

### Rules so you never use the limit again

| Function | Derivative | Note |
|---|---|---|
| $c$ (constant) | $0$ | |
| $x^n$ | $n x^{n-1}$ | power rule, any real $n$ |
| $e^x$ | $e^x$ | its own slope |
| $\ln x$ | $1/x$ | for $x > 0$ |
| $c\,f(x)$ | $c\,f'(x)$ | constants pass through |
| $f + g$ | $f' + g'$ | sum rule |
| $f\,g$ | $f'g + fg'$ | product rule |
| $f/g$ | $(f'g - fg')/g^2$ | quotient rule |
| $f(g(x))$ | $f'(g(x))\,g'(x)$ | chain rule |

The **chain rule** is the star of the [next chapter](../../calculus-and-optimization/the-chain-rule-and-backpropagation/). For now, read it as: if $g$ changes at rate $g'$ and $f$ responds to $g$ at rate $f'$, the rates multiply. For example, $\frac{d}{dx}(3x + 1)^2 = 2(3x + 1)\cdot3$.

### Derivatives of the functions neural networks use

**The sigmoid** $\sigma(z) = \dfrac{1}{1 + e^{-z}}$ squashes any number into $(0,1)$, so it turns a score into a probability (such as the probability of coronary artery disease). Its derivative has a beautiful form. Write $\sigma = (1 + e^{-z})^{-1}$ and use the chain rule:

$$
\sigma'(z) = -1\cdot(1 + e^{-z})^{-2}\cdot(-e^{-z}) = \frac{e^{-z}}{(1+e^{-z})^2} = \underbrace{\frac{1}{1+e^{-z}}}_{\sigma(z)}\cdot\underbrace{\frac{e^{-z}}{1+e^{-z}}}_{1 - \sigma(z)}.
$$

> [!IMPORTANT]
> $$\sigma'(z) = \sigma(z)\,\bigl(1 - \sigma(z)\bigr)$$

At $z = 0$, $\sigma = 0.5$ and $\sigma' = 0.25$, its largest value. For large $|z|$, $\sigma$ flattens and $\sigma'\to0$: the sigmoid **saturates**, which slows learning in deep networks.

**ReLU** $\operatorname{ReLU}(z) = \max(0, z)$ has derivative 1 for $z > 0$ and 0 for $z < 0$. At exactly $z = 0$ it is not differentiable (there is a corner); software simply uses 0 there.

**Logarithm** $\ln p$ has derivative $1/p$, which explodes as $p\to0$. That is why a confident wrong prediction is punished so heavily by the log-loss in [loss functions](../../calculus-and-optimization/loss-functions/).

### Partial derivatives

Models have many parameters. For a function of several variables, $f(w_1, w_2, \dots, w_n)$, the **partial derivative** $\partial f/\partial w_i$ is the ordinary derivative with respect to $w_i$ while every other variable is held fixed.

Example: $f(w_1, w_2) = w_1^2 + 3w_1w_2$.

- Treat $w_2$ as a constant: $\dfrac{\partial f}{\partial w_1} = 2w_1 + 3w_2$.
- Treat $w_1$ as a constant: $\dfrac{\partial f}{\partial w_2} = 3w_1$.

Picture $f$ as a landscape over the $(w_1, w_2)$ plane. $\partial f/\partial w_1$ is the slope you feel walking due east; $\partial f/\partial w_2$ is the slope walking due north.

### The gradient

Collect all partial derivatives into a vector, the **gradient**:

> [!IMPORTANT]
> $$\nabla f(\mathbf{w}) = \begin{bmatrix}\partial f/\partial w_1 \\ \vdots \\ \partial f/\partial w_n\end{bmatrix}, \qquad f(\mathbf{w} + \Delta\mathbf{w}) \approx f(\mathbf{w}) + \nabla f(\mathbf{w})^\top\Delta\mathbf{w}$$

The approximation on the right is the multi-variable version of the tangent line: a small step $\Delta\mathbf{w}$ changes $f$ by approximately the dot product of the gradient with the step.

**The gradient points uphill, steepest.** Consider steps of a fixed small length $\varepsilon$, $\Delta\mathbf{w} = \varepsilon\mathbf{u}$ with $\lVert\mathbf{u}\rVert = 1$. The change in $f$ is about $\varepsilon\,\nabla f^\top\mathbf{u} = \varepsilon\,\lVert\nabla f\rVert\cos\theta$, where $\theta$ is the angle between $\mathbf{u}$ and $\nabla f$ ([dot product geometry](../../linear-algebra/vectors-and-matrices/)). This is largest when $\theta = 0$: the gradient direction increases $f$ fastest, at rate $\lVert\nabla f\rVert$. Its opposite, $-\nabla f$, **decreases $f$ fastest**. Gradient descent is just "take a small step in direction $-\nabla f$, repeat" ([gradient descent](../../calculus-and-optimization/gradient-descent-and-optimizers/)). Directions perpendicular to the gradient ($\cos\theta = 0$) leave $f$ unchanged to first order: they run along the contour lines.

The gradient always has the **same shape as the parameters**. If the weights of a layer form a $64\times4$ matrix, the gradient of the loss with respect to them is also a $64\times4$ matrix. PyTorch stores it in `weight.grad`, with the same shape as `weight`.

### The Jacobian

So far $f$ has had a single number as output. A layer of a network maps a vector to a vector, $\mathbf{f}:\mathbb{R}^n\to\mathbb{R}^m$. Its derivative is the $m\times n$ **Jacobian matrix**, whose row $i$ is the gradient of output $i$:

$$
\mathbf{J} = \frac{\partial\mathbf{f}}{\partial\mathbf{x}} = \begin{bmatrix}
\partial f_1/\partial x_1 & \cdots & \partial f_1/\partial x_n\\
\vdots & \ddots & \vdots\\
\partial f_m/\partial x_1 & \cdots & \partial f_m/\partial x_n
\end{bmatrix}, \qquad
\mathbf{f}(\mathbf{x} + \Delta\mathbf{x}) \approx \mathbf{f}(\mathbf{x}) + \mathbf{J}\,\Delta\mathbf{x}.
$$

The Jacobian is the best **linear** approximation of $\mathbf{f}$ near $\mathbf{x}$. Two important cases:

- For a linear layer $\mathbf{f}(\mathbf{x}) = \mathbf{W}\mathbf{x} + \mathbf{b}$: $\partial f_i/\partial x_j = W_{ij}$, so $\mathbf{J} = \mathbf{W}$. A linear map is its own best linear approximation.
- For an element-wise activation such as $\mathbf{f}(\mathbf{z}) = \sigma(\mathbf{z})$ applied entry by entry: output $i$ depends only on input $i$, so $\mathbf{J}$ is diagonal with entries $\sigma'(z_i)$.

In the next chapter, backpropagation will multiply Jacobians together via the chain rule, without ever forming most of them explicitly.

### Numerical derivatives and gradient checking

The definition suggests computing a derivative numerically by plugging in a small $h$. There are two common recipes:

$$
\text{forward: }\frac{f(x+h) - f(x)}{h}\quad(\text{error}\propto h), \qquad
\text{central: }\frac{f(x+h) - f(x-h)}{2h}\quad(\text{error}\propto h^2).
$$

The central difference is much more accurate because the error terms from the curvature cancel symmetrically. (For $f = x^3$, one can check by expansion that the forward formula gives $3x^2 + 3xh + h^2$ while the central formula gives $3x^2 + h^2$.)

But $h$ cannot be made arbitrarily small: computers store about 16 significant digits, and subtracting two nearly equal numbers loses most of them (**round-off error**). For central differences in 64-bit floats, $h\approx10^{-5}$ to $10^{-6}$ is a good compromise.

Why not always use numerical derivatives? A network with $n$ parameters would need $2n$ evaluations of the loss for one gradient, which is hopeless for millions of parameters. Backpropagation computes all $n$ partial derivatives for roughly the cost of a couple of forward passes. Numerical derivatives are used for **gradient checking**: verifying, on a small example, that a hand-written gradient is correct.

> [!TIP]
> Compare analytic and numeric gradients with the **relative error** $\dfrac{\lVert\mathbf{g}_a - \mathbf{g}_n\rVert}{\lVert\mathbf{g}_a\rVert + \lVert\mathbf{g}_n\rVert}$. In float64, around $10^{-7}$ or smaller means correct; $10^{-2}$ or larger means a bug.

> [!WARNING]
> Gradient checks fail spuriously near kinks such as ReLU at 0, or with float32 precision. Check in float64, at random points, and away from non-differentiable corners.

## Worked example

**1. Gradient of a two-variable function.** $f(w_1, w_2) = w_1^2 + 3w_1w_2$ at $(1, 2)$:

$$
\frac{\partial f}{\partial w_1} = 2(1) + 3(2) = 8,\qquad \frac{\partial f}{\partial w_2} = 3(1) = 3,\qquad \nabla f(1,2) = (8, 3).
$$

Check with the linear approximation. Step to $(1.01, 2.02)$, so $\Delta\mathbf{w} = (0.01, 0.02)$. Predicted change: $8(0.01) + 3(0.02) = 0.14$. Actual: $f(1,2) = 1 + 6 = 7$, and $f(1.01, 2.02) = 1.0201 + 3(1.01)(2.02) = 1.0201 + 6.1206 = 7.1407$, a change of $0.1407$. Very close; the small difference comes from curvature.

The steepest-ascent rate is $\lVert\nabla f\rVert = \sqrt{64 + 9} = \sqrt{73}\approx8.54$ per unit step, in direction $(8,3)/\sqrt{73}$.

**2. A single sigmoid neuron.** A one-feature risk model $p = \sigma(wx + b)$ with $x = 2$, $w = 0.5$, $b = -1$. Then $z = 0.5\cdot2 - 1 = 0$, $p = \sigma(0) = 0.5$.

By the chain rule, $\dfrac{\partial p}{\partial w} = \sigma'(z)\cdot\dfrac{\partial z}{\partial w} = p(1-p)\cdot x = 0.25\cdot2 = 0.5$, and $\dfrac{\partial p}{\partial b} = p(1-p)\cdot1 = 0.25$.

Numerical check for $\partial p/\partial w$ with $h = 0.01$: $w = 0.51$ gives $z = 0.02$, and $w = 0.49$ gives $z = -0.02$.
$\sigma(0.02) = 1/(1 + e^{-0.02}) \approx 0.5050$ and $\sigma(-0.02)\approx0.4950$. Central difference: $(0.504999833 - 0.495000167)/0.02 \approx 0.499983$. Matches 0.5 to four decimal places.

**3. A Jacobian.** $\mathbf{f}(x_1, x_2) = (x_1x_2,\ x_1 + x_2^2)$ at $(1, 2)$:

$$
\mathbf{J} = \begin{bmatrix} x_2 & x_1\\ 1 & 2x_2\end{bmatrix} = \begin{bmatrix}2 & 1\\ 1 & 4\end{bmatrix}.
$$

A step $\Delta\mathbf{x} = (0.1, 0)$ changes the outputs by about $\mathbf{J}\Delta\mathbf{x} = (0.2, 0.1)$. Actual: $\mathbf{f}(1.1, 2) = (2.2, 5.1)$ versus $\mathbf{f}(1,2) = (2, 5)$: exactly $(0.2, 0.1)$, because $\mathbf{f}$ is linear in $x_1$.

## In code

First, see the two error sources of finite differences on $f(x) = x^3$ at $x = 2$, where the true derivative is 12.

```python
import numpy as np

# f(x) = x^3 at x = 2; the true derivative is 3 * 2^2 = 12
f = lambda x: x**3
x0, true = 2.0, 12.0
print(f"{'h':>8} {'forward error':>15} {'central error':>15}")
for h in [1e-1, 1e-2, 1e-3, 1e-5, 1e-8, 1e-11]:
    fwd = (f(x0 + h) - f(x0)) / h
    cen = (f(x0 + h) - f(x0 - h)) / (2 * h)
    print(f"{h:8.0e} {abs(fwd - true):15.2e} {abs(cen - true):15.2e}")
```

```text
       h   forward error   central error
   1e-01        6.10e-01        1.00e-02
   1e-02        6.01e-02        1.00e-04
   1e-03        6.00e-03        1.00e-06
   1e-05        6.00e-05        2.12e-10
   1e-08        7.29e-08        1.17e-07
   1e-11        9.93e-07        9.93e-07
```

The forward error shrinks like $h$ (it is $6h + h^2$ exactly), the central error like $h^2$ (exactly $h^2$), until round-off takes over below about $h = 10^{-5}$ and both get *worse* as $h$ shrinks further.

Next, a gradient check for a small risk model: predicted probability $p_i = \sigma(\mathbf{w}^\top\mathbf{x}_i)$ and squared error loss $L = \frac1n\sum_i(p_i - y_i)^2$. (Squared error on probabilities is used here only to exercise the chain rule; the better loss for this problem is derived in [loss functions](../../calculus-and-optimization/loss-functions/).) By the chain rule, $\dfrac{\partial L}{\partial\mathbf{w}} = \frac1n\sum_i 2(p_i - y_i)\,p_i(1-p_i)\,\mathbf{x}_i$.

```python
import numpy as np

rng = np.random.default_rng(0)

def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))

# Toy cohort: 50 people, 3 standardised features (e.g. LDL, BP, PRS)
X = rng.normal(size=(50, 3))
y = (rng.uniform(size=50) < sigmoid(X @ np.array([1.0, 0.5, 0.8]))).astype(float)

def loss(w):
    """Mean squared error between predicted risk and the 0/1 outcome."""
    p = sigmoid(X @ w)
    return np.mean((p - y) ** 2)

def grad_analytic(w):
    p = sigmoid(X @ w)
    # chain rule: d/dw mean((p-y)^2) = mean(2(p-y) * p(1-p) * x)
    return X.T @ (2 * (p - y) * p * (1 - p)) / len(y)

def grad_numeric(f, w, h=1e-5):
    g = np.zeros_like(w)
    for i in range(len(w)):
        e = np.zeros_like(w)
        e[i] = h                               # nudge one coordinate
        g[i] = (f(w + e) - f(w - e)) / (2 * h) # central difference
    return g

w = np.array([0.3, -0.2, 0.1])
ga, gn = grad_analytic(w), grad_numeric(loss, w)
print("analytic:", ga.round(6))
print("numeric: ", gn.round(6))
rel = np.linalg.norm(ga - gn) / (np.linalg.norm(ga) + np.linalg.norm(gn))
print(f"relative error: {rel:.1e}")

# Plant a bug (forget the p(1-p) factor) and the check catches it
bad = X.T @ (2 * (sigmoid(X @ w) - y)) / len(y)
rel_bad = np.linalg.norm(bad - gn) / (np.linalg.norm(bad) + np.linalg.norm(gn))
print(f"relative error with bug: {rel_bad:.1e}")
```

```text
analytic: [-0.10553  -0.014708  0.015512]
numeric:  [-0.10553  -0.014708  0.015512]
relative error: 2.3e-11
relative error with bug: 6.2e-01
```

Note the matrix form `X.T @ (...)`: the per-person terms $\mathbf{x}_i\cdot(\text{scalar}_i)$ are summed by one matrix–vector product, which has shape $(3, 50)(50,) \to (3,)$, the shape of $\mathbf{w}$.

## Biomedical connection

Derivatives are more than a training tool; they also answer scientific questions about a trained model.

- **Training.** Every parameter of a DNA-based risk model, from a logistic regression on SNP dosages to a convolutional network on raw sequence, is updated using the gradient of the loss. The gradient tells each weight how much responsibility it bears for the current errors.
- **Sensitivity of a prediction.** The gradient of a predicted risk with respect to the **input** (not the weights) asks: which input features, if changed slightly, would change this person's predicted risk most? For a one-hot DNA input, $\partial p/\partial\mathbf{X}$ has shape $L\times4$ and highlights positions and bases the model is sensitive to. These "saliency maps" are a starting point for [interpretability](../../deep-architectures-for-sequences/interpretability/), with known limitations.
- **Marginal effects.** In a logistic risk model, $\partial p/\partial x_j = p(1-p)\,w_j$: the same weight has the largest effect on absolute risk for people near $p = 0.5$ and a small effect for people at very low or very high baseline risk. This is one reason the same genetic variant can matter more, in absolute terms, for some patients than others.

> [!CAUTION]
> A large gradient means the *model's output* is sensitive to an input. It does not mean that changing that input in a real person would change their disease risk. Causal claims need causal evidence.

## Practice

1. Differentiate: (a) $f(x) = 4x^3 - 2x + 7$; (b) $g(x) = x^2e^x$; (c) $h(x) = \ln(1 + x^2)$.

<details>
<summary>Answer</summary>

(a) $12x^2 - 2$. (b) Product rule: $2xe^x + x^2e^x = e^x(x^2 + 2x)$. (c) Chain rule: $\dfrac{1}{1+x^2}\cdot2x = \dfrac{2x}{1+x^2}$.

</details>

2. For $f(w_1, w_2) = (2w_1 - w_2 - 3)^2$, find $\nabla f$ at $(1, 1)$. In which direction should you step to decrease $f$ fastest?

<details>
<summary>Answer</summary>

Let $r = 2w_1 - w_2 - 3$. Then $\partial f/\partial w_1 = 2r\cdot2 = 4r$ and $\partial f/\partial w_2 = 2r\cdot(-1) = -2r$. At $(1,1)$, $r = 2 - 1 - 3 = -2$, so $\nabla f = (-8, 4)$. Step in direction $-\nabla f = (8, -4)$, i.e. increase $w_1$ and decrease $w_2$.

</details>

3. Show that $\tanh'(z) = 1 - \tanh^2(z)$, using $\tanh(z) = 2\sigma(2z) - 1$ and $\sigma' = \sigma(1-\sigma)$.

<details>
<summary>Answer</summary>

$\tanh'(z) = 2\sigma'(2z)\cdot2 = 4\sigma(2z)(1 - \sigma(2z))$. Let $s = \sigma(2z)$, so $\tanh = 2s - 1$. Then $1 - \tanh^2 = 1 - (2s-1)^2 = 1 - 4s^2 + 4s - 1 = 4s(1 - s)$. Equal.

</details>

4. Find the Jacobian of $\mathbf{f}(\mathbf{x}) = \operatorname{ReLU}(\mathbf{W}\mathbf{x})$ at $\mathbf{x} = (1, 1)$ with $\mathbf{W} = \begin{bmatrix}1 & 2\\ -1 & -1\end{bmatrix}$.

<details>
<summary>Answer</summary>

$\mathbf{z} = \mathbf{W}\mathbf{x} = (3, -2)$. ReLU's derivative is 1 for $z_1 = 3$ and 0 for $z_2 = -2$, so the activation Jacobian is $\operatorname{diag}(1, 0)$. By the chain rule, $\mathbf{J} = \operatorname{diag}(1,0)\,\mathbf{W} = \begin{bmatrix}1 & 2\\ 0 & 0\end{bmatrix}$. The inactive unit's row is zeroed.

</details>

5. A model has 2 million parameters and one forward pass takes 10 ms. Roughly how long would one central-difference gradient take? Why does that rule it out for training?

<details>
<summary>Answer</summary>

$2\times2{,}000{,}000 = 4$ million loss evaluations at 10 ms each is $40{,}000$ s, about 11 hours, for a single gradient. Training needs thousands of gradients. Backpropagation gets the exact gradient for roughly the cost of a few forward passes.

</details>

## Further reading

- Marc Peter Deisenroth, A. Aldo Faisal and Cheng Soon Ong, *Mathematics for Machine Learning*, Cambridge University Press, 2020 (chapter 5, "Vector Calculus").
- Ian Goodfellow, Yoshua Bengio and Aaron Courville, *Deep Learning*, MIT Press, 2016 (chapter 4, "Numerical Computation").
- Gilbert Strang, *Calculus*, Wellesley-Cambridge Press. A complete, freely available calculus course.
