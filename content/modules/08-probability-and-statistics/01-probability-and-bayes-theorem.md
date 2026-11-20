+++
summary = "Use the rules of probability and Bayes' theorem to turn a test result into a calibrated risk, and explain why the same genetic test means very different things in different populations."
+++

# Probability and Bayes' Theorem

Every model in this book ends with a number like "this person has a 12% ten-year risk of coronary artery disease". That number is a **probability**, and it only means something if it obeys the rules of probability. The rules are few and simple, but one consequence, **Bayes' theorem**, catches out doctors, patients and machine-learning engineers alike. A genetic test that is "99% accurate" can still be wrong most of the time it says *positive*. By the end of this chapter you will be able to show exactly why, and to compute the right answer in your head.

This chapter builds on the counting-based probability of [Counting and probability](../../statistics-and-counting/counting-and-probability/). There, probabilities were ratios of equally likely outcomes. Here we make the rules general enough to reason about diseases, variants and test results.

## Key ideas

### Sample spaces, events and the three axioms

A **sample space** $\Omega$ is the set of all possible outcomes of an experiment. An **event** is a subset of $\Omega$. If we pick a random person and record (carrier of a variant? yes/no, test result: +/−), then $\Omega$ has four outcomes, and "test is positive" is the event made of two of them.

A **probability** $P$ assigns a number to each event so that three axioms (Kolmogorov, 1933) hold:

1. $P(A) \ge 0$ for every event $A$.
2. $P(\Omega) = 1$.
3. If $A$ and $B$ are **disjoint** (they cannot both happen), $P(A \cup B) = P(A) + P(B)$. The same holds for any countable list of pairwise-disjoint events.

Everything else is derived. Two consequences you will use constantly:

- **Complement rule.** $A$ and "not $A$" ($A^c$) are disjoint and together make up $\Omega$, so $P(A) + P(A^c) = 1$, that is $P(A^c) = 1 - P(A)$.
- **Inclusion–exclusion.** $A \cup B$ splits into the disjoint pieces $A$ and $B \setminus A$, so $P(A \cup B) = P(A) + P(B) - P(A \cap B)$. We subtract the overlap because it was counted twice.

### Conditional probability

Often we learn something, and want to update. The **conditional probability** of $A$ given $B$ is

$$
P(A \mid B) = \frac{P(A \cap B)}{P(B)}, \qquad P(B) > 0.
$$

Read it as: *restrict the world to the outcomes where $B$ happened, then ask what fraction of that world also has $A$.* Rearranging gives the **multiplication rule**:

$$
P(A \cap B) = P(A \mid B)\,P(B) = P(B \mid A)\,P(A).
$$

> [!WARNING]
> $P(A \mid B)$ and $P(B \mid A)$ are different numbers. "The probability of a positive test given that you carry the variant" (the test's sensitivity) is not "the probability you carry the variant given a positive test" (what the patient actually wants to know). Mixing them up is called the **confusion of the inverse**, or the prosecutor's fallacy.

### The law of total probability

If $B_1, \dots, B_k$ split $\Omega$ into disjoint pieces (a **partition**), then any event $A$ splits along them too:

$$
P(A) = \sum_{i=1}^{k} P(A \mid B_i)\,P(B_i).
$$

The most common case is the two-piece partition $\{D, D^c\}$ (disease, no disease):

$$
P(+) = P(+ \mid D)\,P(D) + P(+ \mid D^c)\,P(D^c).
$$

The positives are a mixture: true positives from the sick, false positives from the healthy.

### Independence

$A$ and $B$ are **independent** if knowing one tells you nothing about the other: $P(A \mid B) = P(A)$. Equivalently,

$$
P(A \cap B) = P(A)\,P(B).
$$

> [!WARNING]
> Independent is not the same as disjoint. Disjoint events with non-zero probability are strongly *dependent*: if $A$ happened, $B$ certainly did not. "Carries two copies of an allele" and "carries zero copies" are disjoint, not independent.

A subtler idea is **conditional independence**: $A$ and $B$ are independent *given* $C$ if $P(A \cap B \mid C) = P(A \mid C)\,P(B \mid C)$. Two different lab tests may both be more likely positive in carriers, so they are dependent overall, but independent once you know carrier status. Naive Bayes classifiers and the "multiply likelihood ratios" rule below rely on this assumption.

### Bayes' theorem

Write the multiplication rule both ways and divide by $P(B)$:

$$
P(A \mid B)\,P(B) = P(B \mid A)\,P(A) \quad\Longrightarrow\quad P(A \mid B) = \frac{P(B \mid A)\,P(A)}{P(B)}.
$$

Expanding the denominator with the law of total probability gives the form used in medicine.

> [!IMPORTANT]
> **Bayes' theorem** for a condition $D$ and a positive test:
> $$P(D \mid +) = \frac{P(+ \mid D)\,P(D)}{P(+ \mid D)\,P(D) + P(+ \mid D^c)\,P(D^c)}$$
> The names: $P(D)$ is the **prior**, $P(+ \mid D)$ is the **likelihood**, $P(D \mid +)$ is the **posterior**.

The prior is what you believed before the evidence, the likelihood says how well each hypothesis predicts the evidence, and the posterior is your updated belief.

## Diagnostic tests

### The 2×2 table

Cross-classify people by true status and test result:

| | Condition present ($D$) | Condition absent ($D^c$) |
|---|---|---|
| Test positive | true positive (TP) | false positive (FP) |
| Test negative | false negative (FN) | true negative (TN) |

Four summary numbers come from this table. Two are properties of the **test** (computed down the columns), two are what the **patient** needs (computed across the rows).

| Quantity | Definition | In probability | Question it answers |
|---|---|---|---|
| Sensitivity | TP / (TP + FN) | $P(+ \mid D)$ | Of those with the condition, what fraction does the test catch? |
| Specificity | TN / (TN + FP) | $P(- \mid D^c)$ | Of those without it, what fraction does the test clear? |
| PPV | TP / (TP + FP) | $P(D \mid +)$ | I tested positive. How likely is it that I have it? |
| NPV | TN / (TN + FN) | $P(D^c \mid -)$ | I tested negative. How likely is it that I am clear? |

Sensitivity and specificity do not depend on how common the condition is. PPV and NPV do, strongly. Bayes' theorem gives the link. With prevalence $\pi = P(D)$, sensitivity $\text{se}$ and specificity $\text{sp}$:

$$
\text{PPV} = \frac{\text{se}\cdot\pi}{\text{se}\cdot\pi + (1-\text{sp})(1-\pi)}, \qquad
\text{NPV} = \frac{\text{sp}\,(1-\pi)}{\text{sp}\,(1-\pi) + (1-\text{se})\,\pi}.
$$

As $\pi \to 0$, the numerator of the PPV shrinks faster than the false-positive term $(1-\text{sp})(1-\pi) \approx 1 - \text{sp}$, so PPV falls towards zero. **For rare conditions, even a small false-positive rate swamps the true positives.**

> [!TIP]
> Do Bayes with **natural frequencies**. Imagine 100,000 people, split them by prevalence, then apply sensitivity and specificity to each group. You get whole numbers of people, and the PPV is a simple fraction. Gigerenzer and Hoffrage (1995) showed that people reason far more accurately this way.

### Likelihood ratios and the odds form of Bayes

The **odds** of an event is $p/(1-p)$. A probability of $0.2$ is odds of $0.2/0.8 = 0.25$, often written "1 to 4". To go back, $p = \text{odds}/(1 + \text{odds})$.

Write Bayes' theorem for $D$ and for $D^c$, both given a positive test, and divide one by the other. The awkward denominator $P(+)$ cancels:

$$
\frac{P(D \mid +)}{P(D^c \mid +)} = \frac{P(+ \mid D)}{P(+ \mid D^c)} \times \frac{P(D)}{P(D^c)}.
$$

> [!IMPORTANT]
> **Odds form of Bayes' theorem**
> $$\text{posterior odds} = \text{likelihood ratio} \times \text{prior odds}$$
> with the positive and negative likelihood ratios
> $$\text{LR}^{+} = \frac{\text{se}}{1-\text{sp}}, \qquad \text{LR}^{-} = \frac{1-\text{se}}{\text{sp}}.$$

The likelihood ratio packs everything about the test into one number that does not depend on prevalence. $\text{LR}^+ = 10$ means a positive result multiplies your odds by 10. $\text{LR}^- = 0.1$ means a negative result divides them by 10. An LR of 1 means the test is useless.

Taking logarithms turns the product into a sum:

$$
\log(\text{posterior odds}) = \log(\text{prior odds}) + \log \text{LR}.
$$

If several pieces of evidence are **conditionally independent given $D$**, you can add their log-LRs one after another. That is exactly the structure of **logistic regression**, where each feature adds a term to the log-odds. You will meet it in [linear and logistic regression](../../classical-machine-learning/linear-and-logistic-regression/).

### Sequential updating: two tests in a row

Evidence rarely arrives all at once: a screening assay comes back positive, then a confirmatory assay is run. In the odds form, **the posterior after the first result is the prior for the second**.

To find the second multiplier, apply the odds form inside the world where the first result $T_1$ has already happened, so that every probability carries an extra "given $T_1$":

$$
\frac{P(D \mid T_1, T_2)}{P(D^c \mid T_1, T_2)} = \frac{P(T_2 \mid D, T_1)}{P(T_2 \mid D^c, T_1)} \times \frac{P(D \mid T_1)}{P(D^c \mid T_1)}.
$$

This is always true. The catch is the first factor. It is the likelihood ratio of test 2 *among people who already have result $T_1$*, and a validation study of test 2 alone does not report that. It reduces to the ordinary likelihood ratio of test 2 only if the two results are conditionally independent given the true status, so that $P(T_2 \mid D, T_1) = P(T_2 \mid D)$ and likewise for $D^c$.

> [!IMPORTANT]
> **Sequential updating.** If the results are conditionally independent given $D$ and given $D^c$:
> $$\text{posterior odds} = \text{LR}_2 \times \text{LR}_1 \times \text{prior odds}.$$
> The order of the results does not matter, and the rule extends to any number of them.

**A small example** (illustrative numbers). A condition has prevalence 1%, so the prior odds are $1/99$. Test A has sensitivity 90% and specificity 95%, so $\text{LR}^+_A = 0.90/0.05 = 18$. Test B has sensitivity 80% and specificity 90%, so $\text{LR}^+_B = 0.80/0.10 = 8$. Both come back positive.

- After A: odds $= 18/99 \approx 0.182$, probability $0.182/1.182 \approx 0.154$.
- After B, starting from those odds: $0.182 \times 8 \approx 1.455$, probability $1.455/2.455 \approx 0.593$.

Two positives move a 1% prior to 59%, *if* the tests make their errors independently.

### Conditional independence is not independence

Tests A and B above are conditionally independent given the true status, yet overall they are strongly dependent. By the law of total probability, $P(A^+) = 0.0585$ and $P(B^+) = 0.107$, while

$$
P(A^+ \cap B^+) = (0.90 \times 0.80) \times 0.01 + (0.05 \times 0.10) \times 0.99 = 0.01215,
$$

about twice the product $0.0585 \times 0.107 \approx 0.0063$ that independence would need. A positive A makes the condition more likely, and the condition makes a positive B more likely. The tests are linked *through* $D$, and only through $D$: once the true status is known, A's result says nothing more about B's.

That assumption defines the **naive Bayes** model. If findings $x_1, \dots, x_n$ are conditionally independent given the class, the joint likelihood factorises,

$$
P(x_1, \dots, x_n \mid D) = \prod_{i=1}^{n} P(x_i \mid D), \qquad\text{so}\qquad \text{posterior odds} = \text{prior odds} \times \prod_{i=1}^{n} \text{LR}_i.
$$

A full table of $n$ yes/no findings has $2^n$ rows for each class, while the factorised model needs only $n$ numbers for each class. Later chapters use the same factorisation whenever they multiply per-item likelihoods: the reads covering a site, given the genotype, in [sequencing data](../../genomics-foundations/sequencing-data/); the pieces of evidence for classifying a variant in [genetics of heart disease](../../genomics-foundations/genetics-of-heart-disease/); and the positions of a motif in [information theory](../../probability-and-statistics/information-theory/).

> [!WARNING]
> The model is called "naive" because real findings usually share causes other than the condition itself. Multiplying their likelihood ratios then counts the same evidence twice, and the posterior comes out overconfident. Polygenic scores meet the same double counting when they add up correlated variants, as you will see in [GWAS and polygenic risk scores](../../genomics-foundations/gwas-and-polygenic-risk-scores/).

## Worked example

**Problem.** A laboratory offers a genetic test for a pathogenic variant. The test has sensitivity 99% and specificity 99%. Compare what a positive result means in two settings:

- (a) screening the general population for a rare variant carried by about 1 in 250 people;
- (b) testing for a common condition with prevalence 20%, using a test of the same sensitivity and specificity.

**Step 1: natural frequencies for (a).** Take 100,000 people. Prevalence $1/250$ gives $100{,}000 / 250 = 400$ carriers and $99{,}600$ non-carriers.

- Carriers who test positive: $0.99 \times 400 = 396$ (true positives). The other 4 are false negatives.
- Non-carriers who test positive: $0.01 \times 99{,}600 = 996$ (false positives). The other $98{,}604$ are true negatives.

| | Carrier | Non-carrier | Total |
|---|---|---|---|
| Positive | 396 | 996 | 1,392 |
| Negative | 4 | 98,604 | 98,608 |
| Total | 400 | 99,600 | 100,000 |

**Step 2: read off PPV and NPV.**

$$
\text{PPV} = \frac{396}{1392} \approx 0.284, \qquad \text{NPV} = \frac{98{,}604}{98{,}608} \approx 0.99996.
$$

A positive screen means only about a **28%** chance of carrying the variant. More than 7 in 10 positives are false alarms, because there are 249 non-carriers for every carrier and 1% of a large number is still large. A negative result, on the other hand, is very reassuring.

**Step 3: same test, common condition (b).** Of 100,000 people, 20,000 have the condition and 80,000 do not.

- True positives: $0.99 \times 20{,}000 = 19{,}800$.
- False positives: $0.01 \times 80{,}000 = 800$.
- $\text{PPV} = 19{,}800 / 20{,}600 \approx 0.961$.

Same test, same "99% accuracy", but now a positive result is right 96% of the time.

**Step 4: check with the odds form.** $\text{LR}^+ = 0.99 / 0.01 = 99$.

- (a) Prior odds $= (1/250)/(249/250) = 1/249$. Posterior odds $= 99/249 \approx 0.398$. Probability $= 0.398 / 1.398 \approx 0.284$. ✓
- (b) Prior odds $= 0.2/0.8 = 0.25$. Posterior odds $= 24.75$. Probability $= 24.75/25.75 \approx 0.961$. ✓

**Step 5: what would help in (a)?** Raise the prior. If we only test the first-degree relatives of a known carrier of an autosomal dominant variant, each relative has a prior of about $1/2$, odds 1, and a positive result gives posterior odds 99, a probability of 0.99. This is the logic of **cascade testing**. Or confirm with a second, independent assay: if its errors are conditionally independent of the first, posterior odds become $99 \times 99 / 249 \approx 39.4$, a probability of about 0.975.

> [!NOTE]
> Real clinical sequencing of a known variant usually has specificity much higher than 99%. The numbers here are chosen to make the arithmetic clear. The lesson about prevalence holds for any test whose false-positive rate is not tiny compared with the prevalence.

### A second example: two tests that share a weakness

**Problem.** Take tests A and B from the sequential-updating example: prevalence 1%, $\text{LR}^+$ of 18 and 8. Now suppose their false positives are not independent. Both assays cross-react with the same harmless look-alike sequence, so among healthy people who are positive on A, 60% are also positive on B, not 10%. Among people with the condition the two tests still make their errors independently. What is the probability of the condition after two positive results?

**Step 1: natural frequencies.** Of 100,000 people, 1,000 have the condition and 99,000 do not.

- With the condition and positive on both: $0.90 \times 0.80 \times 1{,}000 = 720$.
- Without it and positive on A: $0.05 \times 99{,}000 = 4{,}950$. Of those, positive on B as well: $0.60 \times 4{,}950 = 2{,}970$.

**Step 2: the right answer.** $P(D \mid A^+, B^+) = 720/(720 + 2{,}970) = 720/3{,}690 \approx 0.195$.

**Step 3: the naive answer.** With independent false positives, only $0.10 \times 4{,}950 = 495$ healthy people would be positive twice, giving $720/1{,}215 \approx 0.593$. That is the figure we got by multiplying the two likelihood ratios. Here it overstates the probability about threefold.

**Step 4: the odds form still works, with the right ratio.** Among A-positives, B is positive in 80% of people with the condition and 60% of people without it. The likelihood ratio of B *given A positive* is $0.80/0.60 \approx 1.33$, not 8. Posterior odds $= 1.33 \times 18/99 \approx 0.242$, and probability $= 0.242/1.242 \approx 0.195$. ✓

## In code

The function below computes PPV, NPV and likelihood ratios. We then check the formula against a simulation of a million people.

```python
import numpy as np

def test_metrics(prevalence, sensitivity, specificity):
    """Return PPV, NPV, LR+ and LR- for a binary diagnostic test."""
    tp = sensitivity * prevalence
    fn = (1 - sensitivity) * prevalence
    fp = (1 - specificity) * (1 - prevalence)
    tn = specificity * (1 - prevalence)
    ppv = tp / (tp + fp)
    npv = tn / (tn + fn)
    lr_pos = sensitivity / (1 - specificity)
    lr_neg = (1 - sensitivity) / specificity
    return ppv, npv, lr_pos, lr_neg

for prev in [1/250, 0.05, 0.20]:
    ppv, npv, lrp, lrn = test_metrics(prev, 0.99, 0.99)
    print(f"prevalence={prev:.4f}  PPV={ppv:.3f}  NPV={npv:.5f}  LR+={lrp:.0f}  LR-={lrn:.4f}")

# Odds form of Bayes gives the same PPV
prev = 1/250
prior_odds = prev / (1 - prev)
post_odds = prior_odds * 99
print("PPV via odds form:", round(post_odds / (1 + post_odds), 3))

# Monte Carlo check: simulate 1,000,000 people
rng = np.random.default_rng(0)
n = 1_000_000
carrier = rng.random(n) < prev
positive = np.where(carrier, rng.random(n) < 0.99, rng.random(n) < 0.01)
print("simulated PPV:", round(carrier[positive].mean(), 3))
print("simulated NPV:", round((~carrier[~positive]).mean(), 5))
```

Output:

```text
prevalence=0.0040  PPV=0.284  NPV=0.99996  LR+=99  LR-=0.0101
prevalence=0.0500  PPV=0.839  NPV=0.99947  LR+=99  LR-=0.0101
prevalence=0.2000  PPV=0.961  NPV=0.99748  LR+=99  LR-=0.0101
PPV via odds form: 0.284
simulated PPV: 0.288
simulated NPV: 0.99996
```

The likelihood ratios do not move with prevalence, but PPV climbs from 28% to 96%. The simulated PPV (0.288) differs slightly from 0.284 because only about 4,000 carriers were drawn, so there is sampling noise. You will learn to quantify that noise in [distributions and likelihood](../../probability-and-statistics/distributions-and-likelihood/).

The second snippet simulates the two tests twice: once with conditionally independent errors, once with the shared false positives of the second worked example. Each run measures the likelihood ratios from the simulated people and compares three ways of getting $P(D \mid A^+, B^+)$.

```python
import numpy as np

rng = np.random.default_rng(11)
n, prev = 2_000_000, 0.01
se_a, sp_a = 0.90, 0.95          # test A
se_b, sp_b = 0.80, 0.90          # test B

def simulate(fp_b_if_a_pos):
    """Both tests on n people. fp_b_if_a_pos = P(B+ | A+, healthy)."""
    d = rng.random(n) < prev
    a = rng.random(n) < np.where(d, se_a, 1 - sp_a)
    # B's false-positive rate among A-negatives keeps its overall rate at 1 - sp_b
    fp_b_if_a_neg = ((1 - sp_b) - (1 - sp_a) * fp_b_if_a_pos) / sp_a
    b = rng.random(n) < np.where(d, se_b, np.where(a, fp_b_if_a_pos, fp_b_if_a_neg))
    return d, a, b

for label, fp in [("conditionally independent", 1 - sp_b), ("shared false positives", 0.60)]:
    d, a, b = simulate(fp)                                # disease, A positive, B positive
    prior_odds = d.mean() / (~d).mean()
    lr_a = a[d].mean() / a[~d].mean()                     # each test measured on its own
    lr_b = b[d].mean() / b[~d].mean()
    lr_b_given_a = b[d & a].mean() / b[~d & a].mean()     # B among the A-positives only
    naive = prior_odds * lr_a * lr_b
    chained = prior_odds * lr_a * lr_b_given_a
    print(f"{label}: LR_A = {lr_a:.1f}, LR_B = {lr_b:.1f}, LR_B given A+ = {lr_b_given_a:.2f}")
    print(f"  P(D | A+, B+): LR_A x LR_B -> {naive / (1 + naive):.3f} | "
          f"LR_A x LR_B given A+ -> {chained / (1 + chained):.3f} | counted -> {d[a & b].mean():.3f}")
```

```text
conditionally independent: LR_A = 18.0, LR_B = 8.0, LR_B given A+ = 8.09
  P(D | A+, B+): LR_A x LR_B -> 0.593 | LR_A x LR_B given A+ -> 0.596 | counted -> 0.596
shared false positives: LR_A = 18.0, LR_B = 8.0, LR_B given A+ = 1.33
  P(D | A+, B+): LR_A x LR_B -> 0.594 | LR_A x LR_B given A+ -> 0.196 | counted -> 0.196
```

Each test, measured on its own, has the same likelihood ratio in both runs, so multiplying them gives about 0.59 both times. A validation study of B alone could not tell the two situations apart. In the first run 0.59 is right, up to sampling noise. In the second the true answer is 0.196, close to the 0.195 of the hand calculation, and only the likelihood ratio of B *given* A's result recovers it.

## Biomedical connection

Our running goal is a model that maps a person's DNA and clinical data to a risk of coronary artery disease. Bayes' theorem shapes that project in three ways.

1. **A model's output is a posterior.** A classifier trained with cross-entropy loss is trying to estimate $P(\text{CAD} \mid \text{features})$. That estimate implicitly includes the prevalence of CAD in the training data. If you train on a case–control dataset with 50% cases, then deploy in a population where 5% develop CAD, the predicted probabilities will be far too high unless you recalibrate. The fix is the odds form: the model's likelihood ratio is unchanged, so you swap in the new prior odds.

2. **Rare variants versus common risk.** Some heart-disease genetics is about rare, high-impact variants, such as those causing familial hypercholesterolemia (see [genetics of heart disease](../../genomics-foundations/genetics-of-heart-disease/)). Population screening for such variants faces exactly the low-prevalence problem of the worked example. Testing relatives of a known carrier, where the prior is high, is far more informative per test.

3. **Evidence combines additively on the log-odds scale.** A polygenic risk score, age, sex, LDL cholesterol and blood pressure each shift the log-odds of disease. Whether those shifts simply add depends on conditional independence, which is never exactly true. Learning how to combine them well is the job of the models in Part IV.

> [!CAUTION]
> A predictive value is only as good as the prevalence you plug in. When you read that a test or risk score has a given PPV, ask "in which population?". This chapter is educational. Interpreting a real genetic test result needs a clinician or genetic counsellor who knows the person's family history and the test's validated performance.

## Practice

1. Events $A$ and $B$ are independent with $P(A) = 0.3$ and $P(B) = 0.5$. Find $P(A \cup B)$.

<details>
<summary>Answer</summary>

Independence gives $P(A \cap B) = 0.3 \times 0.5 = 0.15$. Inclusion–exclusion: $P(A \cup B) = 0.3 + 0.5 - 0.15 = 0.65$.

</details>

2. A test has sensitivity 90% and specificity 95%. The condition has prevalence 2%. Compute the PPV and NPV.

<details>
<summary>Answer</summary>

Per 1,000 people: 20 have the condition, 980 do not. TP $= 18$, FN $= 2$, FP $= 0.05 \times 980 = 49$, TN $= 931$.

PPV $= 18/(18+49) = 18/67 \approx 0.269$. NPV $= 931/(931+2) = 931/933 \approx 0.998$.

</details>

3. For the same test, compute $\text{LR}^+$. A patient's pre-test probability is 10%. What is the probability after a positive result? Use the odds form.

<details>
<summary>Answer</summary>

$\text{LR}^+ = 0.90/0.05 = 18$. Prior odds $= 0.1/0.9 = 1/9$. Posterior odds $= 18/9 = 2$. Probability $= 2/(1+2) = 2/3 \approx 0.667$.

</details>

4. In the worked example (prevalence 1/250, sensitivity and specificity 99%), a person tests **negative**. Use $\text{LR}^-$ to find their posterior probability of carrying the variant.

<details>
<summary>Answer</summary>

$\text{LR}^- = 0.01/0.99 \approx 0.0101$. Prior odds $= 1/249$. Posterior odds $= 0.0101/249 \approx 4.06 \times 10^{-5}$, so the probability is about $4.06 \times 10^{-5}$, that is 4 in about 98,600. This matches the table: $4/98{,}608$. And $1 - \text{NPV} = 1 - 0.99996$.

</details>

5. Two events $A$ and $B$ have $P(A) = 0.4$, $P(B) = 0.5$ and $P(A \cap B) = 0$. Are they independent? Explain.

<details>
<summary>Answer</summary>

No. Independence would require $P(A \cap B) = 0.4 \times 0.5 = 0.2$, but it is 0. They are disjoint, so learning $A$ happened makes $P(B \mid A) = 0$, which is very different from $P(B) = 0.5$.

</details>

6. A patient has a pre-test probability of 5%. Test A (sensitivity 90%, specificity 95%) is **positive**. Then test B (sensitivity 80%, specificity 90%) is **negative**. Assuming the tests are conditionally independent given true status, find the probability after each result.

<details>
<summary>Answer</summary>

Prior odds $= 0.05/0.95 = 1/19$. After A: $\text{LR}^+_A = 0.90/0.05 = 18$, so odds $= 18/19 \approx 0.947$ and probability $= 18/37 \approx 0.486$.

After B: $\text{LR}^-_B = (1 - 0.80)/0.90 = 2/9 \approx 0.222$, so odds $= \tfrac{18}{19} \times \tfrac{2}{9} = \tfrac{4}{19} \approx 0.211$ and probability $= 4/23 \approx 0.174$. The posterior after A served as the prior for B. The negative result pulls the probability back down, but not to where it started.

</details>

7. In the first worked example (prevalence 1/250, $\text{LR}^+ = 99$), a laboratory re-runs the **same** assay on the **same** sample and gets a second positive. A colleague multiplies the odds by 99 again and reports a probability of 0.975. When is that justified? What is the right answer if false positives come from a feature of the sample itself, so that a repeat run always reproduces the first result?

<details>
<summary>Answer</summary>

Multiplying by 99 twice assumes the two results are conditionally independent given carrier status. That holds if errors arise afresh on every run, and then the posterior odds are $99 \times 99/249 \approx 39.4$, a probability of about 0.975.

If the error is a property of the sample, the second result is certain to match the first whether or not the person is a carrier. The likelihood ratio of the repeat, given the first result, is $1/1 = 1$, and the probability stays at about 0.284. To gain evidence you need a test whose errors have a different cause, such as a different assay method or a fresh sample.

</details>

8. A condition has prevalence 20%. Test A has sensitivity and specificity 90%, test B has sensitivity and specificity 80%, and the two are conditionally independent given true status. Compute $P(A^+)$, $P(B^+)$ and $P(A^+ \cap B^+)$. Are the two test results independent?

<details>
<summary>Answer</summary>

$P(A^+) = 0.9 \times 0.2 + 0.1 \times 0.8 = 0.26$. $P(B^+) = 0.8 \times 0.2 + 0.2 \times 0.8 = 0.32$.

$P(A^+ \cap B^+) = (0.9 \times 0.8) \times 0.2 + (0.1 \times 0.2) \times 0.8 = 0.144 + 0.016 = 0.16$.

Independence would need $0.26 \times 0.32 = 0.0832$, about half of 0.16, so the results are **not** independent. Equivalently, $P(B^+ \mid A^+) = 0.16/0.26 \approx 0.615$, far above $P(B^+) = 0.32$: a positive A raises the probability of the condition from 0.20 to $0.18/0.26 \approx 0.69$, and that makes a positive B more likely.

</details>

## Further reading

- Blitzstein, J. K. & Hwang, J. *Introduction to Probability*, 2nd ed. CRC Press, 2019. Chapters 1–2 cover the axioms, conditional probability and Bayes with many examples.
- Gigerenzer, G. & Hoffrage, U. (1995). How to improve Bayesian reasoning without instruction: frequency formats. *Psychological Review*, 102(4), 684–704.
- Altman, D. G. & Bland, J. M. (1994). Diagnostic tests 2: predictive values. *BMJ*, 309, 102.
