+++
summary = "Build and honestly evaluate the baselines any new CAD model must beat: a clinical logistic model, a GWAS-based polygenic risk score, their combination and gradient boosting, overall and per ancestry."
+++

# Baselines: PRS and Clinical Models

A new model is only "better" relative to something. This chapter builds the comparison set for our capstone, using the cohort from [chapter 02](../the-data-pipeline/):

- **(a)** a **clinical-only** logistic model, standing in for the risk calculator clinics already use;
- **(b)** a **polygenic risk score (PRS)** from a GWAS, built two ways: from a GWAS on our *training split only*, and from large *external* summary statistics;
- **(c)** **clinical + PRS + FH status**;
- **(d)** **gradient boosting** on everything, the strongest "off-the-shelf" tabular learner.

We evaluate all of them on the untouched test split: discrimination (AUC, PR-AUC), calibration (Brier score, calibration slope and intercept), and results **per ancestry group**. Along the way, the data will teach three lessons that real projects learn the hard way: **population stratification**, **GWAS power**, and **overfitting through reused data**.

> [!NOTE]
> **Recall.** [Logistic regression](../../classical-machine-learning/linear-and-logistic-regression/) · [regularisation](../../classical-machine-learning/regularization-and-the-bias-variance-tradeoff/) · [boosting](../../classical-machine-learning/trees-forests-and-boosting/) · [model evaluation](../../classical-machine-learning/model-evaluation/) · [GWAS and PRS](../../genomics-foundations/gwas-and-polygenic-risk-scores/) · [multiple testing](../../probability-and-statistics/hypothesis-testing-and-multiple-comparisons/).

## Key ideas

### (a) The clinical model

We standardise the six clinical inputs (age, sex, LDL, SBP, smoking, diabetes) using training means and SDs, then fit

$$
\operatorname{logit} P(y=1\mid \mathbf{c}) = w_0 + \mathbf{w}^\top \mathbf{c}.
$$

With standardised inputs, $e^{w_k}$ is the odds ratio per one-SD change in feature $k$. This makes the coefficients comparable. We also fit a version with the four ancestry PCs added, "clinical + PCs". The genetic models include PCs, so this is the fair comparison when we ask what the *PRS* adds.

### (b1) A GWAS, the fast way

For each SNP $j$ we fit $y = \alpha + \boldsymbol\gamma^\top \mathbf{c} + \beta_j x_j + \varepsilon$, where the covariates $\mathbf{c}$ are age, sex and PCs 1–4. Doing about 1,900 separate regressions is slow. The **Frisch–Waugh–Lovell theorem** gives a shortcut: the OLS estimate of $\beta_j$ equals the slope from regressing *residualised* $y$ on *residualised* $x_j$, where both are residualised on the covariates $C$:

$$
\tilde{\mathbf y} = (I - H)\mathbf y, \quad \tilde{\mathbf x}_j = (I-H)\mathbf x_j, \quad H = C(C^\top C)^{-1}C^\top,
\qquad
\hat\beta_j = \frac{\tilde{\mathbf x}_j^\top \tilde{\mathbf y}}{\tilde{\mathbf x}_j^\top \tilde{\mathbf x}_j}.
$$

*Why it works:* $H$ projects onto the covariates' column space, and $I-H$ removes it. Any part of $x_j$ that the covariates can explain cannot contribute to $\hat\beta_j$. After removing it from both $x_j$ and $y$, a single-variable regression through the origin is all that is left. We residualise $y$ once and all SNP columns in one matrix operation, then get every $\hat\beta_j$, its standard error $\sqrt{\hat\sigma_j^2/\tilde{\mathbf x}_j^\top\tilde{\mathbf x}_j}$ and its $t$-test p-value with vector arithmetic.

This is a **linear** model on a 0/1 outcome. For *testing* association it is valid and widely used (linear mixed-model GWAS software works this way). For odds ratios you would fit a logistic regression per SNP. For a PRS only the *relative* weights matter, so the linear betas work fine.

> [!IMPORTANT]
> **Genomic inflation factor.** Under the null, the $\chi^2_1$ statistics have median $0.455$. So
> $$\lambda_{GC} = \frac{\operatorname{median}(\chi^2_{1,j})}{0.455}$$
> should be close to 1. A value well above 1 across thousands of SNPs signals confounding, usually population stratification, or a highly polygenic trait in a very large sample.

**Population stratification.** In our cohort, group B has higher CAD prevalence for *non-genetic* reasons (the $e_\text{group}$ term). Thousands of null SNPs have slightly different frequencies in group B. A GWAS without ancestry covariates sees "allele more common in B" plus "B has more CAD" and reports an association. Adding PCs as covariates absorbs the ancestry signal.

**Multiple testing.** With about a million roughly independent common variants in the genome, the conventional genome-wide significance threshold is $5\times10^{-8}$, which is a Bonferroni correction of $0.05/10^6$.

### (b2) A polygenic risk score

The simplest PRS is **clumping and thresholding (C+T)**:

$$
\text{PRS}_i = \sum_{j:\ p_j < \tau} \hat\beta_j\, x_{ij}.
$$

*Clumping* keeps only the most significant SNP in each LD block, so that one signal is not counted many times. Our simulated SNPs are unlinked, so we skip it. The threshold $\tau$ is a **hyperparameter**: a strict $\tau$ keeps a few reliable SNPs, while a loose $\tau$ keeps more true signals but also more noise. We choose $\tau$ by validation AUC. Modern methods (LDpred, PRS-CS) replace the hard threshold with Bayesian shrinkage of all betas. They usually do better, but the idea is the same.

**Where should $\hat\beta$ come from?** In real projects, PRS weights almost always come from a *separate, much larger* GWAS, such as consortium summary statistics like CARDIoGRAMplusC4D. They are not estimated in the same cohort. Our generator simulates such external statistics: a group-A GWAS of 300,000 people. We build PRSs both ways and compare.

> [!WARNING]
> **Reusing data overfits.** If the GWAS betas are estimated on the training people, the PRS "knows" those people's labels. Its association with $y$ *in training* is inflated: this is winner's curse plus fitting noise. A logistic model fit on the same training data then gives the PRS too much weight, and that weight does not transfer to new people. Estimate weights on one set of people and combine or evaluate on another.

### (c) Combining clinical factors and genetics

Model (c) is a logistic regression on the standardised clinical features, the PRS, an FH-carrier flag and PCs 1–4. FH status comes from sequencing, and in a real setting from ClinVar-style variant interpretation. It is a separate input because the MAF filter removed those rare variants from the array matrix.

### (d) Gradient boosting

`HistGradientBoostingClassifier` fits shallow trees one after another, each correcting the previous ones' errors. Our version sees all clinical features, PCs, the FH flag, the external PRS and *all* about 1,900 SNP dosages. Boosting can find nonlinearities and interactions automatically. With roughly 1,000 training cases and 1,900 mostly useless SNP columns, it can also overfit noise. Early stopping on an internal validation fraction keeps it in check.

### Evaluation metrics

| Metric | Definition | Ideal | Notes |
|---|---|---|---|
| AUC | $P(\hat p_\text{case} > \hat p_\text{control})$ | 1 | rank-based; ignores calibration |
| PR-AUC | area under precision–recall | 1 | baseline equals prevalence (about 0.10 here), so sensitive to performance at the top of the risk distribution |
| Brier | $\frac1n\sum (\hat p_i - y_i)^2$ | 0 | mixes calibration and discrimination; a constant prediction of $\bar y$ gives $\bar y(1-\bar y) \approx 0.09$ |
| Calibration slope | $b$ in $\operatorname{logit}P(y) = a + b\,\operatorname{logit}\hat p$ | 1 | $< 1$: predictions too extreme (overfitting) |
| Calibration-in-the-large (CITL) | $a$ with $b$ fixed at 1 | 0 | $> 0$: risk underestimated on average |

Every metric is computed on **test** people, overall and within each ancestry group. For the key comparison, the gain from adding genetics, we use a **paired bootstrap**. Resample test people with replacement, compute $\text{AUC}_\text{new} - \text{AUC}_\text{old}$ on the *same* resample, repeat 1,000 times and take the 2.5th and 97.5th percentiles.

## Worked example

**A PRS by hand.** An external GWAS reports four SNPs:

| SNP | $\hat\beta$ | p-value | person's dosage $x$ |
|---|---|---|---|
| s1 | 0.10 | $2\times10^{-9}$ | 2 |
| s2 | −0.05 | $3\times10^{-6}$ | 1 |
| s3 | 0.08 | $4\times10^{-3}$ | 0 |
| s4 | 0.20 | $0.30$ | 1 |

With $\tau = 10^{-4}$, only s1 and s2 are kept: $\text{PRS} = 0.10\cdot 2 + (-0.05)\cdot 1 = 0.15$. With $\tau = 10^{-2}$, s3 is added, but the person's dosage is 0, so the PRS is still 0.15. With $\tau=1$, s4 is added: $0.15 + 0.20 = 0.35$. That last SNP is weakly supported ($p = 0.3$), so its 0.20 may be mostly noise.

Suppose that in training the PRS has mean 0.12 and SD 0.10. The standardised score is $z = (0.15 - 0.12)/0.10 = 0.3$. A combined model has $\operatorname{logit} = -2.4 + 0.35\,z + (\text{clinical terms})$. If this person's clinical terms sum to 0.5, then

$$
\operatorname{logit} = -2.4 + 0.35(0.3) + 0.5 = -1.795, \qquad \hat p = \frac{1}{1+e^{1.795}} = 0.142 .
$$

Without the PRS term the logit is $-1.9$ and $\hat p = 0.130$. The PRS moved this person's risk by 1.2 percentage points. That is small, as expected for a near-average score.

**$\lambda_{GC}$ by hand.** A GWAS of 1,900 SNPs has median $\chi^2 = 0.976$. Then $\lambda_{GC} = 0.976/0.455 = 2.15$, a strong sign of confounding. After adding PCs, the median is $0.516$, so $\lambda_{GC} = 0.516/0.455 = 1.13$.

## In code

Save as `baselines.py` next to `cad_cohort.npz`. First, loading data and the evaluation helpers. Calibration-in-the-large uses a few Newton steps on the intercept, with the slope fixed at 1.

```python
# baselines.py: GWAS on train, PRS, clinical and gradient-boosting baselines
import numpy as np
from scipy.stats import t as t_dist
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.metrics import roc_auc_score, average_precision_score, brier_score_loss

d = np.load("cad_cohort.npz")
X, y, pop, split = d["X"], d["y"].astype(int), d["pop"], d["split"]
clin, pcs = d["clin"], d["pcs"]
tr, va, te = split == 0, split == 1, split == 2
fh_flag = (d["fh_variants"].sum(1) > 0).astype(np.float32)


def calib_slope_intercept(y, p):
    """Regress the outcome on logit(p): ideal slope 1, ideal intercept 0."""
    lp = np.log(p / (1 - p))[:, None]
    slope = LogisticRegression(C=1e6).fit(lp, y).coef_[0, 0]
    # calibration-in-the-large: intercept with the slope fixed at 1 (offset model)
    a = 0.0
    for _ in range(25):                                  # Newton steps on the intercept
        q = 1 / (1 + np.exp(-(a + lp[:, 0])))
        a += (y - q).sum() / (q * (1 - q)).sum()
    return slope, a


def evaluate(name, p, mask=te):
    s, a = calib_slope_intercept(y[mask], p[mask])
    row = dict(model=name, auc=roc_auc_score(y[mask], p[mask]),
               pr_auc=average_precision_score(y[mask], p[mask]),
               brier=brier_score_loss(y[mask], p[mask]), slope=s, citl=a)
    for k, g in enumerate("ABC"):
        m = mask & (pop == k)
        row[f"auc_{g}"] = roc_auc_score(y[m], p[m])
    return row
```

The GWAS, run on the training split only, with and without PCs:

```python
# GWAS on the TRAINING split only: per-SNP linear regression with covariates,
# using the Frisch-Waugh trick (residualise y and every SNP on the covariates once).
def gwas(Xs, ys, covs):
    C = np.column_stack([np.ones(len(ys)), covs])
    proj = lambda A: A - C @ np.linalg.lstsq(C, A, rcond=None)[0]
    yr, Xr = proj(ys.astype(float)), proj(Xs.astype(float))
    sxx = (Xr ** 2).sum(0)
    beta = Xr.T @ yr / sxx
    dof = len(ys) - C.shape[1] - 1
    resid_var = ((yr[:, None] - Xr * beta) ** 2).sum(0) / dof
    se = np.sqrt(resid_var / sxx)
    pval = 2 * t_dist.sf(np.abs(beta / se), dof)
    return beta, se, pval


def lambda_gc(pval):
    """Genomic inflation: median chi-square / 0.455 (about 1 if no confounding)."""
    from scipy.stats import chi2
    return np.median(chi2.isf(pval, 1)) / chi2.ppf(0.5, 1)


cov_noPC = clin[tr][:, :2]                               # age, sex
cov_PC = np.column_stack([clin[tr][:, :2], pcs[tr][:, :4]])
_, _, p_noPC = gwas(X[tr], y[tr], cov_noPC)
beta, se, pval = gwas(X[tr], y[tr], cov_PC)
print(f"lambda_GC without PCs: {lambda_gc(p_noPC):.3f}   with 4 PCs: {lambda_gc(pval):.3f}")
is_tag = d["is_tag"][d["snp_keep"]]
for thr in [5e-8, 1e-5, 1e-3]:
    hit = pval < thr
    print(f"p < {thr:.0e}: {hit.sum():4d} SNPs, of which {is_tag[hit].sum():3d} tag a causal locus")
```

Two PRSs: one from the training GWAS, one from external summary statistics. Each has its threshold chosen on validation data.

```python
# C+T PRS: sum of dosage * beta over SNPs passing a p-value threshold (no clumping needed:
# our simulated SNPs are unlinked). The threshold is a hyperparameter, so pick it on VAL.
from scipy.stats import norm
ext_beta, ext_se = d["ext_beta"][d["snp_keep"]], d["ext_se"][d["snp_keep"]]
ext_p = 2 * norm.sf(np.abs(ext_beta / ext_se))


def prs(b, p, threshold):
    score = X @ np.where(p < threshold, b, 0.0)
    return (score - score[tr].mean()) / (score[tr].std() + 1e-12)


def choose_threshold(b, p, label):
    best = (None, -1)
    for thr in [1e-5, 1e-4, 1e-3, 1e-2, 0.05, 0.1, 0.5, 1.0]:
        if (p < thr).sum() == 0:
            continue
        auc_val = roc_auc_score(y[va], prs(b, p, thr)[va])
        print(f"  {label} p<{thr:6.0e}: {(p < thr).sum():4d} SNPs, val AUC = {auc_val:.3f}")
        best = max(best, (thr, auc_val), key=lambda t: t[1])
    return prs(b, p, best[0]), best[0]


PRS_int, thr_int = choose_threshold(beta, pval, "train-GWAS")
PRS_ext, thr_ext = choose_threshold(ext_beta, ext_p, "external  ")
print(f"chosen thresholds: train-GWAS {thr_int:.0e}, external {thr_ext:.0e}")
for k, g in enumerate("ABC"):          # g_true = the causal polygenic logit (unobservable)
    m = te & (pop == k)
    r_int = np.corrcoef(PRS_int[m], d["g_true"][m])[0, 1]
    r_ext = np.corrcoef(PRS_ext[m], d["g_true"][m])[0, 1]
    print(f"  group {g}: corr(PRS, true genetic logit): train-GWAS {r_int:.2f}, external {r_ext:.2f}")
```

The models:

```python
mu_c, sd_c = clin[tr].mean(0), clin[tr].std(0)
C = (clin - mu_c) / sd_c
feats = {
    "clinical": C,
    "clinical + PCs": np.column_stack([C, pcs[:, :4]]),
    "PRS(ext) + PCs": np.column_stack([PRS_ext, pcs[:, :4]]),
    "clinical + PRS(train) + FH": np.column_stack([C, PRS_int, fh_flag, pcs[:, :4]]),
    "clinical + PRS(ext) + FH": np.column_stack([C, PRS_ext, fh_flag, pcs[:, :4]]),
}
preds = {}
for name, F in feats.items():
    m = LogisticRegression(C=1.0, max_iter=2000).fit(F[tr], y[tr])
    preds[name] = m.predict_proba(F)[:, 1]
# The train-GWAS PRS was estimated on the same people the combiner is fit on, so on TRAIN
# it looks far more predictive than it is. One fix: learn the combining weights on VAL.
F = feats["clinical + PRS(train) + FH"]
m = LogisticRegression(C=1.0, max_iter=2000).fit(F[va], y[va])
preds["  same, combiner fit on val"] = m.predict_proba(F)[:, 1]

# gradient boosting on everything: clinical, PCs, FH flag, external PRS, all SNP dosages
F_all = np.column_stack([clin, pcs[:, :4], fh_flag, PRS_ext, X])
gbm = HistGradientBoostingClassifier(learning_rate=0.05, max_iter=500, max_leaf_nodes=15,
                                     l2_regularization=1.0, early_stopping=True,
                                     validation_fraction=0.15, random_state=0)
gbm.fit(F_all[tr], y[tr])
preds["gradient boosting (all)"] = gbm.predict_proba(F_all)[:, 1]
print(f"boosting stopped after {gbm.n_iter_} trees")

# the unattainable ceiling: the true risk used to simulate the labels
preds["oracle (true risk)"] = 1 / (1 + np.exp(-d["true_logit"]))
```

Evaluation on test, plus the paired bootstrap:

```python
rows = [evaluate(n, p) for n, p in preds.items()]
print(f"{'model':28s} {'AUC':>6s} {'PR-AUC':>7s} {'Brier':>6s} {'slope':>6s} {'CITL':>6s}"
      f" {'AUC_A':>6s} {'AUC_B':>6s} {'AUC_C':>6s}")
for r in rows:
    print(f"{r['model']:28s} {r['auc']:6.3f} {r['pr_auc']:7.3f} {r['brier']:6.4f} "
          f"{r['slope']:6.2f} {r['citl']:+6.2f} {r['auc_A']:6.3f} {r['auc_B']:6.3f} {r['auc_C']:6.3f}")

# paired bootstrap for the AUC gain of adding genetics to the clinical model
rng = np.random.default_rng(0)
idx = np.flatnonzero(te)
base, full = preds["clinical + PCs"], preds["clinical + PRS(ext) + FH"]
deltas = []
for _ in range(1000):
    b = rng.choice(idx, len(idx))
    deltas.append(roc_auc_score(y[b], full[b]) - roc_auc_score(y[b], base[b]))
lo, hi = np.percentile(deltas, [2.5, 97.5])
print(f"delta AUC, (clinical + PCs + PRS(ext) + FH) minus (clinical + PCs) = {np.mean(deltas):.3f} "
      f"[95% CI {lo:.3f} to {hi:.3f}]")
keys = ["clinical", "clinical_pcs", "prs_pcs", "clin_prs_int", "clin_prs_ext", "clin_prs_int_valfit", "gbm", "oracle"]
np.savez("baseline_preds.npz", prs_ext=PRS_ext, prs_int=PRS_int,
         **{k: preds[n] for k, n in zip(keys, preds)})
```

Output (about 20 seconds):

```text
lambda_GC without PCs: 2.145   with 4 PCs: 1.133
p < 5e-08:    0 SNPs, of which   0 tag a causal locus
p < 1e-05:    0 SNPs, of which   0 tag a causal locus
p < 1e-03:    5 SNPs, of which   3 tag a causal locus
  train-GWAS p< 1e-04:    1 SNPs, val AUC = 0.512
  train-GWAS p< 1e-03:    5 SNPs, val AUC = 0.502
  train-GWAS p< 1e-02:   40 SNPs, val AUC = 0.507
  train-GWAS p< 5e-02:  139 SNPs, val AUC = 0.519
  train-GWAS p< 1e-01:  239 SNPs, val AUC = 0.518
  train-GWAS p< 5e-01:  996 SNPs, val AUC = 0.531
  train-GWAS p< 1e+00: 1902 SNPs, val AUC = 0.529
  external   p< 1e-05:  100 SNPs, val AUC = 0.608
  external   p< 1e-04:  109 SNPs, val AUC = 0.609
  external   p< 1e-03:  129 SNPs, val AUC = 0.604
  external   p< 1e-02:  157 SNPs, val AUC = 0.607
  external   p< 5e-02:  240 SNPs, val AUC = 0.602
  external   p< 1e-01:  335 SNPs, val AUC = 0.605
  external   p< 5e-01: 1069 SNPs, val AUC = 0.605
  external   p< 1e+00: 1902 SNPs, val AUC = 0.603
chosen thresholds: train-GWAS 5e-01, external 1e-04
  group A: corr(PRS, true genetic logit): train-GWAS 0.29, external 0.93
  group B: corr(PRS, true genetic logit): train-GWAS 0.18, external 0.58
  group C: corr(PRS, true genetic logit): train-GWAS -0.06, external 0.33
boosting stopped after 82 trees
model                           AUC  PR-AUC  Brier  slope   CITL  AUC_A  AUC_B  AUC_C
clinical                      0.721   0.223 0.0851   0.90  +0.00  0.725  0.729  0.691
clinical + PCs                0.723   0.231 0.0847   0.89  +0.00  0.724  0.726  0.691
PRS(ext) + PCs                0.627   0.155 0.0889   0.95  +0.02  0.647  0.553  0.582
clinical + PRS(train) + FH    0.647   0.167 0.0976   0.31  +0.15  0.656  0.615  0.637
clinical + PRS(ext) + FH      0.747   0.268 0.0827   0.93  +0.01  0.755  0.728  0.701
  same, combiner fit on val   0.720   0.225 0.0855   0.79  -0.02  0.723  0.722  0.682
gradient boosting (all)       0.749   0.272 0.0826   1.12  +0.04  0.756  0.731  0.704
oracle (true risk)            0.779   0.335 0.0789   0.87  +0.02  0.782  0.772  0.753
delta AUC, (clinical + PCs + PRS(ext) + FH) minus (clinical + PCs) = 0.024 [95% CI 0.012 to 0.036]
```

### Results table

Test set: 3,585 people, 361 recorded cases. Per-group test sizes are A 2,531 (240 cases), B 704 (91) and C 350 (30).

| Model | AUC | PR-AUC | Brier | Cal. slope | AUC A | AUC B | AUC C |
|---|---|---|---|---|---|---|---|
| (a) clinical | 0.721 | 0.223 | 0.0851 | 0.90 | 0.725 | 0.729 | 0.691 |
| (a′) clinical + PCs | 0.723 | 0.231 | 0.0847 | 0.89 | 0.724 | 0.726 | 0.691 |
| (b) PRS(ext) + PCs | 0.627 | 0.155 | 0.0889 | 0.95 | 0.647 | 0.553 | 0.582 |
| (c) clinical + PRS(train) + FH | 0.647 | 0.167 | 0.0976 | **0.31** | 0.656 | 0.615 | 0.637 |
| (c) clinical + PRS(ext) + FH | **0.747** | 0.268 | **0.0827** | 0.93 | 0.755 | 0.728 | 0.701 |
| (d) gradient boosting (all) | **0.749** | 0.272 | 0.0826 | 1.12 | 0.756 | 0.731 | 0.704 |
| oracle (true simulated risk) | 0.779 | 0.335 | 0.0789 | 0.87 | 0.782 | 0.772 | 0.753 |

What the numbers say:

1. **Stratification is real, and PCs fix most of it.** $\lambda_{GC}$ falls from 2.15 to 1.13 when PCs are added. The remaining inflation of 1.13 is expected: about 10% of our SNPs tag real causal loci.
2. **Our own GWAS is badly underpowered.** No SNP reaches $5\times10^{-8}$. Validation chose $\tau = 0.5$ (996 SNPs), and that PRS has validation AUC 0.53, barely better than a coin. Its correlation with the true genetic score is 0.29 in group A and slightly negative in C. About 1,000 cases cannot estimate hundreds of small effects. That is why real PRSs use GWAS of hundreds of thousands of people.
3. **Reusing the training data is worse than useless.** Combining that PRS with clinical factors *on the same training people* **lowers** the test AUC from 0.721 to 0.647, and the calibration slope collapses to 0.31. This is the overfitting trap from the warning box: on training data the overfit PRS looks very predictive, so it gets a large coefficient. Fitting the combiner on validation data instead ("same, combiner fit on val") brings the model back to about the clinical-only AUC (0.720). The fix removes the harm but cannot create signal that is not there.
4. **External summary statistics work.** The external PRS alone has AUC 0.627. Added to clinical factors and PCs, it raises the AUC by **0.024 (95% CI 0.012 to 0.036)** and PR-AUC from 0.231 to 0.268, with good calibration (slope 0.93). That is a realistic size for the added value of a PRS on top of clinical risk factors.
5. **Portability shows up clearly.** The external PRS correlates 0.93 with the true genetic risk in group A, 0.58 in B and 0.33 in C. Its AUC falls from 0.647 (A) to 0.553 (B) and 0.582 (C). Group C's AUCs are based on only 30 cases, so their confidence intervals are wide. Chapter 05 computes them.
6. **Boosting matches, but does not beat, the logistic model.** At 0.749 vs 0.747, the two are within noise. Its calibration slope of 1.12 means its predictions are slightly *too cautious*.
7. **The ceiling is low.** Even the true simulated risk only reaches AUC 0.779, partly because 8% of cases are missing from the labels. Every model is competing for the gap between about 0.72 and 0.78.

> [!TIP]
> The bar for chapter 04 is now concrete. A new model has to beat **clinical + PRS(ext) + FH (AUC 0.747)** and **boosting (0.749)** on the same test set, with good calibration and a CI that excludes zero. Matching boosting with a neural network is not a win.

## Biomedical connection

- **Real PRS performance.** In published work, adding a CAD PRS to conventional risk factors typically improves the C-statistic by a small amount, often around 0.01–0.03. Our 0.024 is in that range by design of the simulation, not as evidence.
- **Summary statistics are the currency.** Large consortia such as CARDIoGRAMplusC4D, and biobank GWAS such as UK Biobank and FinnGen, publish per-SNP effect sizes for CAD. A PRS for a new cohort is built by matching their variants to the cohort's imputed dosages, harmonising which allele is the effect allele (strand flips are a classic bug), and choosing a method and tuning set.
- **Portability is an equity problem.** Most large CAD GWAS have been dominated by European-ancestry participants, and PRS accuracy is reduced in other ancestries, especially African-ancestry groups (Martin et al., 2019). Our groups B and C reproduce this mechanism through differing LD. Multi-ancestry GWAS and methods that model ancestry-specific LD are active research areas.
- **FH remains separate.** Our FH flag adds little to AUC because the clinical model already sees the high LDL it causes. But FH carriers are individually at high risk, and cascade testing of their relatives is valuable. Population-level AUC is not the only measure of clinical value.

## Practice

1. Prove the key step of Frisch–Waugh–Lovell: $\tilde{\mathbf x}^\top \tilde{\mathbf y} = \tilde{\mathbf x}^\top \mathbf y$. (Hint: $I-H$ is symmetric and idempotent.)

<details>
<summary>Answer</summary>

$\tilde{\mathbf x}^\top \tilde{\mathbf y} = \mathbf x^\top (I-H)^\top (I-H)\mathbf y = \mathbf x^\top (I-H)(I-H)\mathbf y = \mathbf x^\top (I-H)\mathbf y = \tilde{\mathbf x}^\top \mathbf y$. So residualising $y$ is not even necessary for $\hat\beta$, only for the residual variance.

</details>

2. A GWAS gives median $\chi^2_1 = 0.62$. Compute $\lambda_{GC}$ and name two possible causes of the inflation.

<details>
<summary>Answer</summary>

$\lambda_{GC} = 0.62/0.455 = 1.36$. Possible causes: population stratification (missing or too few PCs), cryptic relatedness, or genuine polygenic signal in a very large sample. LD-score regression can separate confounding from polygenicity.

</details>

3. With the table above, compute the PR-AUC "lift" of the clinical + PRS(ext) + FH model over random ranking, given test prevalence $361/3585$.

<details>
<summary>Answer</summary>

Prevalence $= 361/3585 = 0.1007$. Lift $= 0.268/0.1007 = 2.66$. The model's average precision is about 2.7 times what random ranking achieves.

</details>

4. In `baselines.py`, change the train-GWAS threshold to $\tau = 10^{-3}$ (5 SNPs) and refit "clinical + PRS(train) + FH" on train. Predict what happens to the calibration slope compared with $\tau=0.5$, and explain why. Then run it.

<details>
<summary>Answer</summary>

The slope should move back towards 1. With only 5 SNPs, the PRS has far fewer fitted noise terms, so it is much less overfit to the training labels, and the combiner gives it a smaller, more honest coefficient. The AUC will be close to the clinical-only model, because the 5 SNPs carry little signal. Running it gives slope 0.84 and AUC 0.719. Overfitting grows with the number of noisy weights estimated on the same people.

</details>

5. Why do we report AUC within each ancestry group instead of only pooled AUC? Give a way pooled AUC can *exceed* every within-group AUC.

<details>
<summary>Answer</summary>

Pooled AUC mixes between-group and within-group ranking. If one group has both higher average predicted risk and higher prevalence, the model gets "free" correct rankings *between* groups. Pooled AUC can then be higher than the AUC inside any single group, while hiding poor performance in a small group. Within-group AUC measures what matters for an individual: ranking people with a similar background.

</details>

## Further reading

- Hastie T, Tibshirani R, Friedman J. *The Elements of Statistical Learning*, 2nd ed. Springer (2009). Logistic regression, boosting.
- Devlin B, Roeder K. "Genomic control for association studies." *Biometrics* (1999).
- Price AL, et al. "Principal components analysis corrects for stratification in genome-wide association studies." *Nature Genetics* (2006).
- Choi SW, Mak TSH, O'Reilly PF. "Tutorial: a guide to performing polygenic risk score analyses." *Nature Protocols* (2020).
- Vilhjálmsson BJ, et al. "Modeling linkage disequilibrium increases accuracy of polygenic risk scores." *American Journal of Human Genetics* (2015). LDpred.
- Ge T, et al. "Polygenic prediction via Bayesian regression and continuous shrinkage priors." *Nature Communications* (2019). PRS-CS.
- Nikpay M, et al. "A comprehensive 1000 Genomes-based genome-wide association meta-analysis of coronary artery disease." *Nature Genetics* (2015). CARDIoGRAMplusC4D.
- Martin AR, et al. "Clinical use of current polygenic risk scores may exacerbate health disparities." *Nature Genetics* (2019).
