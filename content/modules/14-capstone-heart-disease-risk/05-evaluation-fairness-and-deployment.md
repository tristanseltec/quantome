+++
summary = "Finish the capstone like a real study: recalibrate, compute net benefit, audit performance across ancestry and sex, interpret the model with in-silico mutagenesis and Shapley values, and document it with TRIPOD+AI and a model card, with privacy and regulation in view."
+++

# Evaluation, Fairness and Deployment

A trained model with a good AUC is the *middle* of a clinical prediction project, not the end. Before anyone could responsibly use our CAD model, we must answer harder questions. Are its probabilities right? Would acting on it do more good than harm? Does it work equally well for everyone? What has it actually learned? How would we report, validate, protect and regulate it?

This chapter answers each question for the models from [chapter 03](../baselines-prs-and-clinical-models/) and [chapter 04](../designing-a-deep-learning-model/), using one script, `evaluate.py`. It then closes the capstone with a model card and a roadmap for your own research.

> [!NOTE]
> **Recall.** [Model evaluation](../../classical-machine-learning/model-evaluation/) · [interpretability](../../deep-architectures-for-sequences/interpretability/) · [Bayes' theorem](../../probability-and-statistics/probability-and-bayes-theorem/) · [logistic regression](../../classical-machine-learning/linear-and-logistic-regression/).

## Key ideas

### Calibration and recalibration

A model is **calibrated** if, among people given risk $r$, a fraction $r$ have events. We check this three ways:

- a **calibration table or plot**: bin people by predicted risk (quintiles here) and compare mean predicted with observed event rates;
- **calibration-in-the-large**: mean predicted risk vs. observed prevalence;
- **calibration slope**: the slope $b$ in $\operatorname{logit}P(y=1) = a + b\cdot\operatorname{logit}\hat p$. A slope below 1 means predictions are too extreme (overfitting); above 1 means too timid.

Our network was trained with `pos_weight` $\approx 9$, which, as derived in chapter 04, multiplies every predicted odds by about 9. Its raw outputs average around 50% in a population with 10% prevalence. The fix is **logistic recalibration** (Platt scaling) fitted on the **validation** split:

$$
\hat p_\text{recal} = \sigma\big(a + b\cdot\operatorname{logit}\hat p_\text{raw}\big).
$$

If class weighting were the only distortion, we would expect $b \approx 1$ and $a \approx -\log 9 \approx -2.2$. Recalibration fixes calibration-in-the-large and the slope. It does **not** change the ranking, so AUC is untouched. More flexible alternatives (isotonic regression) need more data.

> [!WARNING]
> Recalibrating on the test set and then reporting test calibration is circular. Fit the recalibration on validation data, or by cross-validation within training, and check it on test.

### Decision curves and net benefit

Suppose a clinician offers a statin to everyone whose predicted risk is at least $t$. Choosing $t$ says how many false positives the clinician will accept per true positive. At threshold $t$, treating a person with risk exactly $t$ is a toss-up, so the harm of one unnecessary treatment is valued at $\frac{t}{1-t}$ of the benefit of one necessary treatment. This gives the **net benefit**:

$$
\text{NB}(t) = \frac{\text{TP}}{n} - \frac{\text{FP}}{n}\cdot\frac{t}{1-t}.
$$

Units: "net true positives per person". Two reference strategies:

- **treat none**: $\text{NB}=0$;
- **treat all**: $\text{NB} = \pi - (1-\pi)\frac{t}{1-t}$, where $\pi$ is prevalence.

A **decision curve** plots NB against $t$ over the plausible range of thresholds. A model is clinically useful at $t$ only if it beats *both* reference strategies there. Unlike AUC, net benefit penalises miscalibration: a model whose risks are inflated treats too many people.

### Subgroup and ancestry fairness

We report, for each ancestry group and each sex:

- **discrimination**: within-group AUC with a bootstrap CI;
- **calibration**: observed / expected events (O/E), where 1 is perfect, above 1 means risk is underestimated, below 1 overestimated;
- **error rates at the decision threshold**: the true-positive rate (TPR, the share of future cases flagged) and the false-positive rate (FPR).

Fairness criteria conflict. When prevalence differs between groups, a model cannot in general be calibrated within every group *and* have equal TPR and FPR across groups. This is a known impossibility result. In clinical risk prediction, **calibration within groups** usually comes first, so that a "10% risk" means 10% for everyone. Error-rate gaps are then reported and discussed, not hidden.

> [!CAUTION]
> Ancestry groups are not races, and genetic ancestry PCs are not the same thing as social categories. Our model uses PCs partly as stand-ins for *non-genetic* differences between groups. In the simulation those come from the $e_\text{group}$ term, which represents environment and access to care. In real data this can encode social inequities into a "genetic" score. Report it, question it, and involve affected communities and clinicians in deciding what is acceptable.

### Interpretation

**In-silico mutagenesis (ISM).** For a sequence model $f$, mutate each position $\ell$ to each alternative base $b$ and record $\Delta_{\ell,b} = f(x^{\ell\to b}) - f(x)$. This needs $3L$ forward passes and no gradients. It answers the most natural question about a variant: *what does this change do to predicted risk?* We compare the model's $\Delta$ at the 8 real variant sites with the **true** simulated effect. A homozygous motif-destroying change removes 2 copies, so $0.5 \times (-2) = -1.0$ log-odds. The motif-creating change adds 2 copies, $+1.0$.

**Shapley values for clinical features.** For a model $f$ and players (features) $N = \{1,\dots,P\}$, the Shapley value of feature $j$ is its average marginal contribution over all orders in which features could be "revealed":

$$
\phi_j = \sum_{S \subseteq N\setminus\{j\}} \frac{|S|!\,(P-|S|-1)!}{P!}\Big[v(S\cup\{j\}) - v(S)\Big],
$$

where $v(S)$ is the model's output when features in $S$ take the person's values and the others take a **baseline** (here the training mean). Shapley values are the unique attribution satisfying efficiency ($\sum_j \phi_j = f(x) - f(\text{baseline})$), symmetry, dummy and additivity. With $P = 7$ players there are only $2^7 = 128$ coalitions, so we compute them **exactly**. SHAP's approximations are needed only for many features.

### External validation

Everything so far is **internal validation**: the test people come from the same (simulated) population, recruitment process and measurement procedures as the training people. **External validation** applies the frozen model to a different cohort: another country, health system, time period, or ancestry mix. Expect:

- **calibration drift** (different baseline risk), often fixable by updating the intercept;
- **discrimination loss**, if case mix or measurement differs;
- **PRS portability loss** in different ancestries, as in chapter 03.

A model is not ready for clinical use until it has been externally validated, ideally prospectively and ideally with an impact study showing that using it improves care.

### Reporting: TRIPOD+AI

**TRIPOD+AI** (2024) is the reporting guideline for clinical prediction models built with regression or machine learning. Its checklist covers, among other things:

- the source of data and participants;
- outcome definition and timing;
- predictors and how they were measured;
- sample size;
- missing data handling;
- the model specification and tuning;
- performance measures with CIs (discrimination **and** calibration);
- fairness across subgroups;
- model updating;
- open code and data availability.

Use it as a checklist while writing, not after.

### Privacy and consent

- **Genomic data identifies people.** Studies have shown that surnames can be inferred from Y-chromosome markers matched to genealogy databases, and that individuals can be detected in aggregate statistics under some conditions. "De-identified" genotypes are not anonymous. They also reveal information about relatives who never consented.
- **Consent** defines allowed uses. Data used for research under broad consent may not be usable for a commercial product. Returning individual genetic risk results raises additional duties: counselling, and what to do with incidental findings.
- **Federated learning** trains a shared model without pooling raw data. Each site computes updates (gradients or weights) on its own data, and only the updates are aggregated (for example federated averaging). It reduces, but does not eliminate, privacy risk: updates can leak information. Secure aggregation and differential privacy add protection, at some cost in accuracy.

### Regulation

Software that informs diagnosis or treatment of individual patients is typically regulated as **Software as a Medical Device (SaMD)**: in the US by the FDA, in the EU under the Medical Device Regulation, in the UK by the MHRA. Conceptually, regulators ask about intended use and risk class, clinical evidence (validation and performance), quality management and software lifecycle, cybersecurity, post-market surveillance, and how a learning system's changes over time are controlled. Genetic tests also involve laboratory regulation. A research prototype like ours is far from this bar. Knowing it exists shapes how you design studies from the start.

## Worked example

**Net benefit by hand.** In a test set of $n = 1{,}000$ people with 100 cases, a model at threshold $t = 0.10$ flags 300 people, of whom 70 are cases.

- $\text{TP}/n = 70/1000 = 0.070$, $\text{FP}/n = 230/1000 = 0.230$, and $t/(1-t) = 0.1/0.9 = 0.1111$.
- $\text{NB} = 0.070 - 0.230 \times 0.1111 = 0.070 - 0.0256 = 0.0444$.
- Treat all: $\text{NB} = 0.10 - 0.90 \times 0.1111 = 0.10 - 0.10 = 0$.

So the model provides 0.0444 net true positives per person: the equivalent of finding 44 extra cases per 1,000 people with no unnecessary treatments.

**Shapley values by hand, two features.** A model has $f(\text{baseline}) = -2.0$. Revealing only LDL gives $-1.4$, only age gives $-1.6$, and both give $-0.8$. Then

$$
\phi_\text{LDL} = \tfrac12\big[(-1.4) - (-2.0)\big] + \tfrac12\big[(-0.8) - (-1.6)\big] = \tfrac12(0.6) + \tfrac12(0.8) = 0.7,
$$

$$
\phi_\text{age} = \tfrac12\big[(-1.6)-(-2.0)\big] + \tfrac12\big[(-0.8)-(-1.4)\big] = \tfrac12(0.4) + \tfrac12(0.6) = 0.5 .
$$

Check efficiency: $0.7 + 0.5 = 1.2 = -0.8 - (-2.0)$. ✓

## In code

`evaluate.py` uses the files written by chapters 02–04. Calibration and recalibration:

```python
# evaluate.py: calibration, recalibration, net benefit, fairness, interpretation
import numpy as np
import torch
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from cad_model import load_inputs, CADDataset, CADRiskNet

d, b, dl = np.load("cad_cohort.npz"), np.load("baseline_preds.npz"), np.load("dl_preds.npz")
y, pop, split = d["y"].astype(int), d["pop"], d["split"]
va, te = split == 1, split == 2
logit = lambda p: np.log(p / (1 - p))


def recalibrate(p, fit_mask):
    """Logistic recalibration: refit intercept and slope on logit(p), using VAL only."""
    lr = LogisticRegression(C=1e6).fit(logit(p[fit_mask])[:, None], y[fit_mask])
    return lr.predict_proba(logit(p)[:, None])[:, 1], lr.intercept_[0], lr.coef_[0, 0]


def calibration_table(p, mask, bins=5):
    """Quintiles of predicted risk: mean predicted vs observed event rate."""
    edges = np.quantile(p[mask], np.linspace(0, 1, bins + 1))
    q = np.clip(np.searchsorted(edges, p[mask], side="right") - 1, 0, bins - 1)
    return [(p[mask][q == k].mean(), y[mask][q == k].mean()) for k in range(bins)]


p_dl_raw = dl["p_full"]
p_dl, a, s = recalibrate(p_dl_raw, va)
print(f"recalibration fitted on val: intercept {a:+.2f}, slope {s:.2f}")
models = {"clinical + PCs": b["clinical_pcs"], "clinical + PRS(ext) + FH": b["clin_prs_ext"],
          "multimodal, raw": p_dl_raw, "multimodal, recalibrated": p_dl}
for name, p in models.items():
    rows = calibration_table(p, te)
    print(f"{name:26s} mean risk {p[te].mean():.3f} (observed {y[te].mean():.3f}) | quintiles "
          + " ".join(f"{pr:.2f}/{ob:.2f}" for pr, ob in rows))
```

Net benefit across thresholds:

```python
def net_benefit(p, mask, t):
    """Net benefit of 'treat if predicted risk >= t' = TP/n - FP/n * t/(1-t)."""
    treat = p[mask] >= t
    n = mask.sum()
    tp = (treat & (y[mask] == 1)).sum()
    fp = (treat & (y[mask] == 0)).sum()
    return tp / n - fp / n * t / (1 - t)


thresholds = [0.05, 0.075, 0.10, 0.15, 0.20, 0.30]
print("threshold      " + " ".join(f"{t:>7.3f}" for t in thresholds))
prev = y[te].mean()
print("treat all      " + " ".join(f"{prev - (1 - prev) * t / (1 - t):7.4f}" for t in thresholds))
print("treat none     " + " ".join(f"{0:7.4f}" for t in thresholds))
for name in ["clinical + PCs", "clinical + PRS(ext) + FH", "multimodal, raw", "multimodal, recalibrated"]:
    print(f"{name[:14]:14s} " + " ".join(f"{net_benefit(models[name], te, t):7.4f}" for t in thresholds)
          + ("  <- " + name if len(name) > 14 else ""))
```

Subgroup audit with bootstrap CIs:

```python
def subgroup_report(p, t=0.10, n_boot=500, seed=0):
    rng = np.random.default_rng(seed)
    groups = {f"ancestry {g}": pop == k for k, g in enumerate("ABC")}
    groups |= {"female": d["clin"][:, 1] == 0, "male": d["clin"][:, 1] == 1}
    print(f"{'subgroup':12s} {'n':>5s} {'cases':>5s} {'AUC':>6s} {'95% CI':>13s} {'O/E':>5s} "
          f"{'TPR@10%':>8s} {'FPR@10%':>8s}")
    for name, g in groups.items():
        idx = np.flatnonzero(te & g)
        boots = []
        for _ in range(n_boot):
            bi = rng.choice(idx, len(idx))
            boots.append(roc_auc_score(y[bi], p[bi]))
        lo, hi = np.percentile(boots, [2.5, 97.5])
        flag = p[idx] >= t
        tpr = flag[y[idx] == 1].mean()
        fpr = flag[y[idx] == 0].mean()
        oe = y[idx].sum() / p[idx].sum()                 # observed / expected events
        print(f"{name:12s} {len(idx):5d} {y[idx].sum():5d} {roc_auc_score(y[idx], p[idx]):6.3f} "
              f"[{lo:.3f},{hi:.3f}] {oe:5.2f} {tpr:8.2f} {fpr:8.2f}")


subgroup_report(p_dl)
```

In-silico mutagenesis of the sequence branch. Clinical and genotype inputs are held at their training means (zeros), so only the window changes:

```python
# In-silico mutagenesis (ISM) on the sequence branch: start from the reference window
# (homozygous), make every single-base change, record the change in predicted log-odds.
A = load_inputs()
model = CADRiskNet(A["geno"].shape[1], A["clin"].shape[1])
model.load_state_dict(torch.load("cad_model.pt"))
model.eval()
code = {c: i for i, c in enumerate("ACGT")}
ref = np.array([code[c] for c in d["ref"]])
L = len(ref)
batch = np.repeat(np.eye(4, dtype=np.float32)[ref].T[None], 4 * L, axis=0)   # (4L, 4, L)
for pos in range(L):
    for base in range(4):
        batch[4 * pos + base, :, pos] = np.eye(4)[base]          # row 4*pos+ref = reference
n = len(batch)
inputs = {"seq": torch.from_numpy(batch), "geno": torch.zeros(n, A["geno"].shape[1]),
          "clin": torch.zeros(n, A["clin"].shape[1]), "prs": torch.zeros(n, 1), "y": torch.zeros(n)}
with torch.no_grad():
    out = model(inputs).numpy().reshape(L, 4)
delta = out - out[np.arange(L), ref][:, None]                   # (L, 4); 0 for the ref base

# 1) the variants that actually occur in the cohort: model vs. simulated truth
seq_hap = d["seq"]
print("site  ref>alt  model delta  true delta  (homozygous change, log-odds)")
for j, pos in enumerate(d["sites"]):
    alt = int(seq_hap[:, :, pos][seq_hap[:, :, pos] != ref[pos]][0])
    true = {0: -1.0, 1: +1.0}.get(j, 0.0)                       # 2 motif copies lost / gained
    print(f"{pos:4d}   {'ACGT'[ref[pos]]}>{'ACGT'[alt]}    {delta[pos, alt]:+8.3f}    {true:+6.1f}")

# 2) all 3L possible mutations, most of which never occur in the training data
never = np.setdiff1d(np.arange(L), d["sites"])
eff = np.abs(delta[never]).max(1)                               # strongest change per position
d98 = abs(delta[98, int(seq_hap[:, :, 98].max())])
print(f"{L - 8} never-varying positions: median max|delta| {np.median(eff):.3f}, "
      f"largest {eff.max():.3f} (position {never[eff.argmax()]}); "
      f"{(eff > d98).sum()} exceed the motif-disrupting variant ({d98:.3f})")
```

Exact Shapley values for the clinical features of the highest-risk test person:

```python
# Exact Shapley values for the clinical features of one person. Players: age, male, LDL,
# SBP, smoker, diabetes, and the 4 ancestry PCs as one player. A player that is "absent"
# takes the training mean (0 after standardisation), as in baseline Shapley.
from itertools import combinations
from math import factorial
names = ["age", "male", "LDL", "SBP", "smoker", "diabetes", "PCs"]
cols = [[0], [1], [2], [3], [4], [5], [6, 7, 8, 9]]
P = len(names)
i = int(np.flatnonzero(te)[np.argmax(p_dl[te])])                # highest predicted risk in test
one = {key: torch.from_numpy(A[key][i:i + 1]) for key in ("geno", "seq", "clin", "prs", "y")}


def value(coalition):
    x = dict(one)
    clin = torch.zeros_like(one["clin"])
    for j in coalition:
        clin[:, cols[j]] = one["clin"][:, cols[j]]
    x["clin"] = clin
    with torch.no_grad():
        return model(x).item()


v = {S: value(S) for r in range(P + 1) for S in combinations(range(P), r)}
phi = np.zeros(P)
for j in range(P):
    for S in v:
        if j not in S:
            w = factorial(len(S)) * factorial(P - len(S) - 1) / factorial(P)
            phi[j] += w * (v[tuple(sorted(S + (j,)))] - v[S])
raw = d["clin"][i]
print(f"person {i}: age {raw[0]:.0f}, male {raw[1]:.0f}, LDL {raw[2]:.1f}, SBP {raw[3]:.0f}, "
      f"smoker {raw[4]:.0f}, diabetes {raw[5]:.0f}; recalibrated risk {p_dl[i]:.2f}")
for nme, ph in sorted(zip(names, phi), key=lambda t: -abs(t[1])):
    print(f"  {nme:9s} {ph:+.3f}")
print(f"sum of Shapley values {phi.sum():+.3f} = f(person) - f(baseline) "
      f"= {v[tuple(range(P))] - v[()]:+.3f}")
```

Output (a few seconds):

```text
recalibration fitted on val: intercept -2.79, slope 1.17
clinical + PCs             mean risk 0.100 (observed 0.101) | quintiles 0.02/0.04 0.04/0.04 0.07/0.08 0.12/0.11 0.24/0.24
clinical + PRS(ext) + FH   mean risk 0.100 (observed 0.101) | quintiles 0.02/0.03 0.04/0.04 0.07/0.07 0.12/0.11 0.25/0.25
multimodal, raw            mean risk 0.520 (observed 0.101) | quintiles 0.21/0.02 0.38/0.06 0.54/0.07 0.66/0.12 0.81/0.24
multimodal, recalibrated   mean risk 0.101 (observed 0.101) | quintiles 0.01/0.02 0.04/0.06 0.07/0.07 0.12/0.12 0.26/0.24
threshold        0.050   0.075   0.100   0.150   0.200   0.300
treat all       0.0534  0.0278  0.0008 -0.0580 -0.1241 -0.2847
treat none      0.0000  0.0000  0.0000  0.0000  0.0000  0.0000
clinical + PCs  0.0586  0.0445  0.0325  0.0204  0.0115  0.0010
clinical + PRS  0.0601  0.0462  0.0387  0.0251  0.0139  0.0026  <- clinical + PRS(ext) + FH
multimodal, ra  0.0534  0.0280  0.0015 -0.0519 -0.1060 -0.2071  <- multimodal, raw
multimodal, re  0.0583  0.0440  0.0369  0.0213  0.0130  0.0036  <- multimodal, recalibrated
subgroup         n cases    AUC        95% CI   O/E  TPR@10%  FPR@10%
ancestry A    2531   240  0.741 [0.708,0.769]  1.02     0.68     0.31
ancestry B     704    91  0.722 [0.662,0.775]  0.92     0.78     0.43
ancestry C     350    30  0.699 [0.623,0.787]  1.14     0.47     0.23
female        1762   124  0.722 [0.672,0.769]  0.93     0.56     0.22
male          1823   237  0.719 [0.684,0.754]  1.04     0.76     0.43
site  ref>alt  model delta  true delta  (homozygous change, log-odds)
  98   G>T      -0.454      -1.0
  47   A>T      +0.735      +1.0
  78   A>G      -0.054      +0.0
  35   T>A      -0.010      +0.0
 118   T>A      -0.204      +0.0
 199   G>T      -0.056      +0.0
  34   G>T      -0.116      +0.0
 121   G>C      +0.069      +0.0
192 never-varying positions: median max|delta| 0.329, largest 7.119 (position 13); 56 exceed the motif-disrupting variant (0.454)
person 12935: age 71, male 1, LDL 5.0, SBP 134, smoker 1, diabetes 0; recalibrated risk 0.86
  LDL       +0.696
  PCs       +0.606
  age       +0.601
  smoker    +0.429
  male      +0.238
  diabetes  -0.046
  SBP       +0.032
sum of Shapley values +2.556 = f(person) - f(baseline) = +2.556
```

### What we learn

**Calibration.** The raw network predicts a mean risk of 52% where 10.1% is observed. That is the class-weighting distortion, as predicted. Recalibration fitted on validation (intercept −2.79, slope 1.17) brings it to 10.1% overall and close agreement in every quintile, for example 0.26 predicted vs 0.24 observed in the top fifth. The logistic baselines were calibrated from the start. The intercept (−2.79) is a bit lower than the $-\log 9 = -2.2$ we would expect from class weighting alone, and the slope is 1.17 instead of 1. Weight decay, dropout and early stopping also shrink the network's logits, so the empirical fit is needed rather than the theoretical correction.

**Net benefit.** At every threshold from 5% to 30%, both logistic models and the recalibrated network beat "treat all" and "treat none". The **raw** network does *worse than treating nobody* for thresholds of 15% and above. That is a vivid demonstration that a model with a decent AUC can be harmful if its probabilities are wrong. Clinical + PRS(ext) + FH has the highest net benefit at every threshold up to 20%. For example, at $t = 10\%$ it reaches 0.0387 vs 0.0325 for clinical + PCs, which is about 6 extra net true positives per 1,000 people. The recalibrated network is level with clinical + PCs at 5–7.5%, between the two logistic models at 10–20%, and marginally highest at 30%, where all net benefits are tiny.

**Fairness.** Point estimates of AUC fall from A (0.741) to B (0.722) to C (0.699). Group C's 95% CI is very wide (0.623–0.787) because it has only 30 test cases. We *cannot* rule out a substantial gap, and we cannot confirm one either. Underpowered subgroups are themselves a finding: the remedy is more data from under-represented groups, not a smaller error bar from clever statistics. Calibration differs too: O/E is 0.92 in B (risk overestimated) and 1.14 in C (underestimated). At a 10% threshold, the model flags 78% of future cases in B but only 47% in C. Group-specific recalibration, or better data, would be needed before deployment.

**ISM.** At the variant sites the model has seen, it has learned the right *direction*. The motif-destroying G>T at 98 lowers the log-odds (−0.45) and the motif-creating A>T at 47 raises it (+0.74), while the six neutral sites have smaller effects (all within ±0.21). The magnitudes are smaller than the truth (±1.0), which matches the attenuated sequence signal seen in the chapter 04 ablations. But at the 192 positions that **never vary** in the cohort, the model's responses are arbitrary. 56 of them exceed the real motif-destroying variant, and one reaches 7.1 log-odds. Nothing in the training data constrained the network there, so ISM is extrapolating *off the data distribution*. **Interpret ISM only where the model has seen variation, or use models pretrained on many sequences, where every position has been constrained.**

**Shapley values.** For the highest-risk test person (71-year-old male smoker, LDL 5.0 mmol/L, recalibrated risk 0.86), LDL (+0.70), age (+0.60) and smoking (+0.43) push risk up, as expected clinically. The **ancestry PCs contribute +0.61**: this person is in group B, whose excess risk in the simulation is *non-genetic*. That is exactly the kind of attribution a fairness review should question. (He also carries 4 intact motif copies. In fact he did not have a recorded CAD event, a reminder that an 86% risk is a probability, not a prediction of certainty.) The sum of the Shapley values equals the difference between the person's output and the baseline output, +2.556, as efficiency guarantees.

### A model card for our capstone model

```text
MODEL CARD: CAD-Multimodal-v0 (research prototype, synthetic data)

Intended use      Research and teaching only. Estimate risk of a recorded CAD event in a
                  simulated cohort. NOT for clinical use.
Out of scope      Diagnosis; individual treatment decisions; populations unlike the
                  training data; children; people with prior CAD.
Data              Synthetic cohort, 17,928 people in 12,000 families, 3 ancestry groups
                  (70/20/10%), family-level split 60/20/20, stratified by ancestry and case.
Inputs            Age, sex, LDL, SBP, smoking, diabetes; 4 ancestry PCs; 1,902 QC'd
                  SNP dosages; external PRS; 3 FH-like variants; 200 bp DNA window.
Outcome           Binary recorded CAD; ~10% prevalence; ~8% of true cases unrecorded.
Architecture      Genotype MLP + reverse-complement CNN + clinical MLP, gated fusion,
                  wide linear path; 34,592 parameters; BCE with class weighting;
                  logistic recalibration on validation.
Performance       Test AUC 0.735 (seed 0; 0.749 seed 1); PR-AUC 0.256; calibrated after
(test, n=3,585)   recalibration. Does NOT outperform logistic regression with the same
                  inputs (AUC 0.763).
Subgroups         AUC A 0.741, B 0.722, C 0.699 (C: 30 cases, CI 0.62 to 0.79).
                  O/E: A 1.02, B 0.92, C 1.14.
Interpretation    ISM recovers the direction of both real motif variants; responses at
                  never-varying positions are unreliable. Ancestry PCs carry
                  non-genetic risk.
Limitations       Simulated data; small case count; binary outcome ignores time and
                  censoring; label noise; no external validation.
Ethics, privacy   Real genomic data would be identifying; consent and data-use limits
                  apply; ancestry-related performance gaps must be reported.
Recommendation    Prefer the logistic model with window-variant dosages on this data.
```

## Biomedical connection

The lessons here are well documented in cardiovascular risk prediction. Existing calculators are known to be miscalibrated when moved to new populations or eras, which is why SCORE2 is recalibrated by region and QRISK is periodically updated. Decision curve analysis has become a standard way to argue clinical utility for new markers, PRS included. Reporting of PRS studies has its own guidance, the PRS Reporting Standards (Wand et al., 2021), alongside TRIPOD+AI. Questions of ancestry, equity and consent are central to large programmes like All of Us, which was designed partly to correct the European-ancestry imbalance of earlier genomic research.

> [!CAUTION]
> Nothing in this capstone is medical advice. A real CAD risk tool must be developed with clinicians, validated externally and prospectively, assessed for equity, protected for privacy, and cleared by the relevant regulator before it influences any patient's care.

### Next steps for your own research

1. **Make the simulation harder and more realistic.** Add LD between neighbouring SNPs (then implement clumping), admixed individuals, age at event with censoring (then a Cox loss), and nonlinear gene–environment interactions, where a deep model *might* earn its place.
2. **Replace the from-scratch CNN with pretrained embeddings.** Score each window variant with a [genomic foundation model](../../deep-architectures-for-sequences/genomic-foundation-models/) and use the scores as features. Compare against chapter 04 using several seeds.
3. **Do the statistics properly.** Repeat everything over 5–10 seeds and splits. Report mean ± SD and paired bootstrap CIs for every comparison. Pre-register the analysis plan.
4. **Work with real data.** Use open GWAS summary statistics to build and compare PRSs on public reference genotypes (such as the 1000 Genomes Project). Then apply for access to a cohort such as UK Biobank or All of Us through your institution.
5. **Write it up with TRIPOD+AI**, publish the code, and include a model card and a fairness section from day one.

## Practice

1. In the output, compute the net benefit of "treat all" at $t = 0.15$ from the test prevalence 0.1007, and confirm the printed value.

<details>
<summary>Answer</summary>

$\text{NB} = 0.1007 - 0.8993 \times \frac{0.15}{0.85} = 0.1007 - 0.8993 \times 0.17647 = 0.1007 - 0.1587 = -0.0580$. That matches the printed −0.0580.

</details>

2. A model has calibration slope 0.7 on external data. What does that mean, and what simple update could fix it?

<details>
<summary>Answer</summary>

The predictions are too extreme: high risks are too high and low risks too low, typical of overfitting or a change in case mix. Logistic recalibration ($\sigma(a + b\cdot \operatorname{logit}\hat p)$ fitted on local data) shrinks the logits by $b \approx 0.7$ and resets the intercept. The ranking, and so the AUC, is unchanged.

</details>

3. Compute three-feature Shapley values for $f(\varnothing)=0$, $f(\{1\})=1$, $f(\{2\})=1$, $f(\{3\})=0$, $f(\{1,2\})=3$, $f(\{1,3\})=1$, $f(\{2,3\})=1$, $f(\{1,2,3\})=3$.

<details>
<summary>Answer</summary>

Weights: $|S|=0$: $\tfrac13$; $|S|=1$: $\tfrac16$; $|S|=2$: $\tfrac13$.
Feature 3 never changes $f$, so $\phi_3 = 0$ (dummy).
$\phi_1 = \tfrac13(1-0) + \tfrac16(3-1) + \tfrac16(1-0) + \tfrac13(3-1) = \tfrac13 + \tfrac13 + \tfrac16 + \tfrac23 = 1.5$.
By symmetry $\phi_2 = 1.5$. Check: $1.5+1.5+0 = 3 = f(\{1,2,3\}) - f(\varnothing)$.

</details>

4. Group C has 30 test cases and AUC 0.699 (95% CI 0.623–0.787). A reviewer asks whether the model is "fair to group C". Draft a two-sentence answer.

<details>
<summary>Answer</summary>

For example: "With only 30 test cases in group C, our data cannot distinguish a small performance gap from a large one (AUC 95% CI 0.62–0.79), and calibration suggests risk is underestimated in this group (O/E 1.14). We therefore make no fairness claim for group C and identify recruitment of more participants from this group and external validation as prerequisites for any use."

</details>

5. Explain why federated learning alone does not guarantee privacy, and name one complementary technique.

<details>
<summary>Answer</summary>

Shared model updates are functions of local data and can leak information about individuals, for example through gradient inversion or membership inference. Complementary techniques: secure aggregation (the server sees only the sum of updates), and differential privacy (calibrated noise added to updates, with a formal privacy guarantee).

</details>

## Further reading

- Van Calster B, et al. "Calibration: the Achilles heel of predictive analytics." *BMC Medicine* (2019).
- Vickers AJ, Elkin EB. "Decision curve analysis: a novel method for evaluating prediction models." *Medical Decision Making* (2006).
- Collins GS, et al. "TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods." *BMJ* (2024).
- Wand H, et al. "Improving reporting standards for polygenic scores in risk prediction studies." *Nature* (2021).
- Mitchell M, et al. "Model cards for model reporting." *Proceedings of FAT\** (2019).
- Lundberg SM, Lee S-I. "A unified approach to interpreting model predictions." *NeurIPS* (2017).
- Kleinberg J, Mullainathan S, Raghavan M. "Inherent trade-offs in the fair determination of risk scores." *ITCS* (2017).
- Gymrek M, et al. "Identifying personal genomes by surname inference." *Science* (2013).
- McMahan HB, et al. "Communication-efficient learning of deep networks from decentralized data." *AISTATS* (2017).
