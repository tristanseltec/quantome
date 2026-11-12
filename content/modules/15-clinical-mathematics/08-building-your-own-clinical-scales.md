+++
summary = "Turn a guideline formula into a printable, validated weight-band chart, log your own cases in a safe structured way, build a points score from data with logistic regression, and know what validation and approval a personal scale needs before it touches patient care."
+++

# Building Your Own Clinical Scales

Every experienced clinician carries private rules of thumb: "children in this weight range get one full syringe", "with these three findings I always call the registrar", "this sort of patient usually needs more fluid than the formula says". Some of these rules are good, built from hundreds of cases. Others are memories of one dramatic case, distorted by hindsight. The aim of this chapter is to keep the good rules and catch the bad ones. You will learn to:

1. **Write a guideline formula down as a reference chart.** A weight-band dosing table, rounded to volumes you can actually measure, with the maximum dose built in, and checked against the formula at every weight.
2. **Record your experience as data.** A small, de-identified, approved case log, and honest descriptive statistics of your own practice, including how uncertain they are.
3. **Turn data into a score.** Fit a logistic regression and convert it into a simple points score, the way the Framingham risk score was made (Sullivan et al., 2004).
4. **Validate it and get it approved** before any patient is affected.

The maths is the easy part. The hard part is being honest about what your data can and cannot show.

> [!CAUTION]
> Everything here is a **method**, shown with an illustrative "Drug X" and **synthetic** patient data. None of the tables, points or risks in this chapter is a real dosing chart or a real clinical score. Before a personal chart or score guides real care, check it against the current formulary or guideline (BNF/BNFc, national guidance, hospital protocols). Have it independently checked, and approved through your organisation's governance route (pharmacy, the drug and therapeutics committee, clinical safety). Until then it is a draft.

## Key ideas

### Three kinds of personal tool

| Tool | Source of truth | Main risk | Validation |
|---|---|---|---|
| **Reference chart** (dose bands, fluid-rate table, nomogram) | An existing formula or guideline | Transcription, rounding and banding errors | Compare with the formula at **every** weight in range |
| **Case log and descriptive statistics** | Your own cases | Small numbers, selective memory, confidentiality | Pre-defined fields and outcomes, confidence intervals, approval |
| **Points score / prediction rule** | A model fitted to data | Overfitting, poor calibration in new settings | Discrimination, calibration, external validation, governance |

The first kind adds no new medical knowledge. It only makes an existing rule faster and safer to use at the bedside. The third kind claims new knowledge, so it needs much stronger evidence.

### (a) Reference charts generated from a formula

A weight-band chart replaces "multiply weight by dose, check the cap, convert to volume, round" with "find the row". To build one safely you need a few design decisions, and you should write them down:

- **The formula and its source.** Illustrative example: Drug X 10 mg/kg per dose, maximum 500 mg per dose, oral stock 250 mg/5 mL (= 50 mg/mL).
- **Where in the band the dose is calculated.** If you calculate at the **lower edge**, nobody in the band gets more than the target mg/kg, but heavier children in the band get less. If you calculate at the midpoint, half the band gets slightly more than the target. Which is acceptable depends on the drug (therapeutic index, whether under-dosing matters), so it is a decision for pharmacy, not for the programmer.
- **Rounding to a measurable volume.** Nobody can draw up 1.37 mL accurately with a 5 mL oral syringe. Pick increments that the available devices can measure and round in the safer direction (here, down).
- **The maximum dose cap**, applied *before* converting to volume, and one row for "weight at or above the cap weight". For Drug X the cap weight is $500/10 = 50$ kg.
- **A tolerance.** For example, "delivered dose within *a%* to 100% of the target for every weight in the band". The value of *a* comes from the drug's guideline or pharmacy, not from this chapter.

The number of bands is a trade-off. Narrow bands keep each patient close to the target, but a longer table is easier to misread. Validation tells you where the bands are too wide.

**Nomograms** are charts that do the calculation graphically. Classic examples are the BSA nomogram (a ruler laid across height and weight scales) and drug-level nomograms that plot concentration against time. They are built the same way: choose a formula, sample it on a grid, draw it, and **check it against the formula** at many points, including the extremes. Printing and photocopying can distort the scale, so a printed nomogram needs a check that it was printed at the right size, and must say which formula and version it encodes.

The same generator pattern works for any formula. The maintenance-fluid "4-2-1" rule from [Holliday–Segar](../../clinical-mathematics/maintenance-fluids-holliday-segar/) gives 12 mL/h at 3 kg, 40 at 10 kg, 50 at 15 kg, 60 at 20 kg and 70 at 30 kg. A table printed from code is less likely to contain a slip than one copied by hand.

### (b) Turning experience into data

Memory is a poor database. We remember the vivid case, forget the ordinary ones, and tend to recall our successes. A **structured log** fixes this if you decide in advance what you will record:

- **One row per case, a fixed list of fields, and pre-defined outcomes.** Write down what counts as a "complication" *before* you start, so you can't redefine it later to suit the data.
- **Consecutive cases.** Record every eligible case, not just the interesting ones.
- **Data minimisation.** Store only what you need to answer your question. Use a random case code, not names, hospital numbers or dates of birth. Record age in bands and month rather than date. Keep the key that links codes to patients separately and securely, or don't keep one at all. Small subgroups can still identify people (the only 16-year-old with condition Y last March), so count the cells before you share any table.
- **Approval first.** Find out from your organisation whether this is **clinical audit or service evaluation** (usually registered with the audit or clinical governance team) or **research** (needs research ethics approval). Data-protection law applies in both cases, for example UK GDPR with the Caldicott principles in the UK, or HIPAA in the US, where "de-identified" has specific legal meanings. Don't keep a spreadsheet of patients on a personal device.

**Descriptive statistics of your own practice.** Report medians and IQRs for doses, and proportions **with confidence intervals**. Your own numbers are small, so the intervals are wide. The 95% **Wilson interval** for a proportion $k/n$, with $\hat p = k/n$ and $z = 1.96$, is

$$
\frac{\hat p + \frac{z^2}{2n} \pm z\sqrt{\frac{\hat p(1-\hat p)}{n} + \frac{z^2}{4n^2}}}{1 + \frac{z^2}{n}}.
$$

It behaves better than the textbook $\hat p \pm 1.96\sqrt{\hat p(1-\hat p)/n}$ when $k$ is small. If you have seen **0 events in $n$ cases**, the "rule of three" gives an approximate 95% upper limit of $3/n$. "No complications in my last 20 cases" is still compatible with a true rate of about 15%.

### (c) From data to a points score

Many bedside scores are logistic regression models in disguise. Logistic regression models the log-odds of an outcome as a weighted sum ([linear and logistic regression](../../classical-machine-learning/linear-and-logistic-regression/)):

$$
\ln\frac{p}{1-p} = \beta_0 + \beta_1 x_1 + \dots + \beta_k x_k.
$$

Clinicians can't do exponentials at the bedside, but they can add small integers. **Sullivan, Massaro and D'Agostino (2004)** described how the Framingham investigators turned the regression into points:

1. Fit the model and get each $\beta_i$.
2. Split continuous variables into categories, and give each category $j$ a reference value $W_{ij}$ (for example its midpoint). Pick a **base category** $W_{i,\text{ref}}$ for each variable.
3. Choose a constant $B$, the number of regression units that will be worth **one point**. A common choice is the effect of a meaningful change in a key variable, for example 10 years of age: $B = 10\,\beta_{\text{age}}$.
4. Points for category $j$ of variable $i$:

> [!IMPORTANT]
> **Sullivan points**
> $$\text{points}_{ij} = \operatorname{round}\!\left(\frac{\beta_i\,(W_{ij} - W_{i,\text{ref}})}{B}\right)$$
> For a yes/no variable coded 0/1 this is just $\operatorname{round}(\beta_i / B)$.

5. Convert a total score back to a risk. Each point is worth about $B$ on the log-odds scale, so

$$
\hat p(\text{total}) = \frac{1}{1 + \exp\!\big(-(\beta_0 + \textstyle\sum_i \beta_i W_{i,\text{ref}} + B \cdot \text{total})\big)}.
$$

Rounding loses a little information. Always check how much, by comparing the AUC and calibration of the points score against the full model.

### (d) Validation: the part that matters

**For a reference chart**, validation is exhaustive and cheap. Compute the chart's dose and the formula's dose at every weight in range (every 0.1 kg). Check that the cap is never exceeded, that the chart never gives more than the formula (if that is your rule), and find the worst under-dose. Then have someone else check the printed version against the code output.

**For a score**, use the ideas from [model evaluation](../../classical-machine-learning/model-evaluation/):

- **Discrimination**: does the score rank patients correctly? This is measured by the AUC (C-statistic). An AUC of 0.5 is chance level.
- **Calibration**: when it predicts 20%, do about 20% of those patients have the outcome? Check **calibration-in-the-large** (mean predicted against observed), the **calibration slope** (ideal 1; below 1 means the predictions are too extreme, the classic sign of overfitting), and a calibration plot. Calibration is the property most often lost when a score moves to a new hospital (Van Calster et al., 2019).
- **Internal validation** (bootstrap or cross-validation) estimates optimism within your own data. **External validation** uses patients from another time or place. A score built from one clinician's cases has to show that it works on other people's patients.
- **Sample size.** A score fitted to too few events will overfit. The old rule of thumb is about 10 **events per variable** (EPV; Peduzzi et al., 1996), which is a minimum, not a target. Modern sample-size methods (Riley et al., 2020) often require more. Count *candidate* variables, including every one you tried and dropped, not just those that ended up in the score.
- **Reporting**: follow the TRIPOD statement (Collins et al., 2015) and assess risk of bias with PROBAST (Wolff et al., 2019).

### Governance: why your personal scale needs approval

The moment a chart or score is used for patients other than your own, or in place of the official tool, it becomes an organisational matter:

- **Dosing charts**: pharmacy check, and approval by the **drug and therapeutics committee** (or your organisation's equivalent). Version control, an owner, a review date, and withdrawal of old copies.
- **Scores and calculators**: approval by the clinical governance or guideline committee. If it is software that calculates doses or risks for individual patients, it may count as a **medical device** under the rules of your regulator (for example the MHRA in the UK or the FDA in the US). In the UK, clinical risk management standards for health IT (DCB0129 for manufacturers, DCB0160 for deploying organisations) may also apply.
- **Transparency**: the chart or score should state its source formula or development data, its version, its validated weight or age range, and what it must not be used for.

Expert-derived rules are not worthless. Several widely used scores began as expert consensus and were then tested on data. That testing is what makes them trustworthy.

## Worked examples

### Example 1 · Reading and checking a weight-band chart across patient profiles

The chart from the code below, for **illustrative Drug X** (10 mg/kg, maximum 500 mg, stock 50 mg/mL, volume rounded down to 0.1 mL below 5 mL and 0.5 mL from 5 mL), gives:

| Weight band | Dose | Volume | Delivered mg/kg across the band |
|---|---|---|---|
| 4 to < 5 kg | 40 mg | 0.8 mL | 8.0–10.0 |
| 6 to < 8 kg | 60 mg | 1.2 mL | 7.5–10.0 |
| 14 to < 16 kg | 140 mg | 2.8 mL | 8.8–10.0 |
| 26 to < 30 kg | 250 mg | 5.0 mL | 8.3–9.6 |
| ≥ 50 kg | 500 mg | 10.0 mL | maximum dose (cap) |

(Selected rows. The full table is in the code output.)

- **Infant, 7.9 kg.** The chart gives 60 mg (1.2 mL), but the formula gives 79 mg. That is $60/79 = 76\%$ of the target, the worst point on the whole chart. The validation loop finds it automatically. *Fix:* split the band at 7 kg. Then 6–<7 kg gives 60 mg and 7–<8 kg gives 70 mg (1.4 mL), and the worst case in either band is about 8.6 mg/kg.
- **Child, 14 kg.** 140 mg = 2.8 mL. *Check:* $14 \times 10 = 140$ mg, and $140 / 50 = 2.8$ mL. ✓
- **Child, 26 kg.** The formula gives 260 mg = 5.2 mL. Because 5.2 mL falls in the 0.5 mL rounding zone, it rounds down to 5.0 mL = 250 mg (9.6 mg/kg). The rounding rule, not the band, set this dose. Your design notes should explain it.
- **Adolescent, 62 kg.** $62 \times 10 = 620$ mg, which is above the 500 mg maximum, so the dose is 500 mg = 10 mL. A chart without a cap row would invite 12.4 mL.
- **Adult, 80 kg.** Capped at 500 mg. For an adult, check whether the formulary gives a fixed adult dose rather than mg/kg at all.
- **Older adult with renal impairment.** A woman of 84, 60 kg, creatinine 150 µmol/L ($150/88.4 = 1.70$ mg/dL). Cockcroft–Gault: $\frac{(140-84)\times 60}{72 \times 1.70} \times 0.85 = 23.4$ mL/min. A weight-band chart knows nothing about renal function. If Drug X is renally cleared, the chart must say "check renal dosing in the formulary" and must not be used on its own (see [weight and body-size-based dosing](../../clinical-mathematics/weight-and-body-size-based-dosing/)).
- **Adult with obesity, 130 kg, 1.70 m, male.** IBW (Devine) $= 50 + 2.3 \times (66.9 - 60) = 65.9$ kg, and adjusted body weight $= 65.9 + 0.4(130 - 65.9) = 91.6$ kg. The cap makes the answer 500 mg here whichever weight you use. For an uncapped drug, the chart must say which weight it expects (total, ideal or adjusted), because the doses differ by a factor of 2.

### Example 2 · What your log can and cannot tell you

A synthetic log of 120 cases has 8 complications. That is 6.7%, with 95% Wilson CI 3.4% to 12.6%. Split into five age bands of 20–32 cases, each band's interval runs from about 1–3% up to 22–26%. **The bands cannot be told apart.** An impression such as "older children do worse" cannot be supported by these numbers. The log also shows a maximum dose of 10.8 mg/kg against an intended 10 mg/kg. That is a finding worth following up as an audit result, in a way that a recollection could never be.

### Example 3 · Points by hand

Suppose a fitted model gives $\beta_{\text{age}} = 0.034$ per year, $\beta_{\text{RR}\ge22} = 0.908$, $\beta_{\text{SpO}_2<94\%} = 0.931$ and $\beta_{\text{confusion}} = 1.257$. Take $B = 10\,\beta_{\text{age}} = 0.336$ (one point ≈ 10 years of age; the unrounded coefficient is 0.0336). Age bands 18–39, 40–59, 60–74 and 75+ have midpoints 29, 50, 67.5 and 85, with reference 29.

- Age 40–59: $0.0336 \times (50-29)/0.336 = 2.1$, so **2** points. Age 60–74: $38.5/10 = 3.85$, so **4**. Age 75+: $56/10 = 5.6$, so **6**.
- RR ≥ 22: $0.908/0.336 = 2.70$, so **3**. SpO₂ < 94%: $0.931/0.336 = 2.77$, so **3**. Confusion: $1.257/0.336 = 3.74$, so **4**.

A 70-year-old with RR 24 and normal saturation and no confusion scores $4 + 3 = 7$, which the table in the code maps to a predicted risk of about 26% *in the synthetic population*. The maximum score is $6 + 3 + 3 + 4 = 16$.

## Sanity checks & common errors

> [!WARNING]
> - **Validating only the band edges you happened to pick.** Check every 0.1 kg, including the exact cap weight and the extremes of the range.
> - **Rounding after capping vs before.** Cap the mg first, then convert to mL and round. Make sure rounding can never push the dose above the cap.
> - **A chart without its assumptions.** Every printed chart should state the drug, strength of stock, formula, cap, rounding rule, weight range, version, date and who approved it. A chart for 250 mg/5 mL used with a 125 mg/5 mL bottle halves every dose.
> - **"My experience shows…" from 20 cases.** Put a confidence interval on it first.
> - **Choosing outcomes after seeing the data**, or logging only memorable cases.
> - **Overfitting.** Too few events per variable gives scores that look excellent on your own cases and fail on the next clinician's. The code below shows this.
> - **Reporting only the AUC.** A score can rank perfectly well yet predict 18% when the real rate is 24%. Check calibration.
> - **Using a score outside its population** (different age range, setting or baseline risk) without re-checking calibration.
> - **Skipping governance** because "it's only my own chart". Copies spread.

## In code

### A chart generator with built-in validation

```python
import math

# ILLUSTRATIVE "Drug X": 10 mg/kg per dose, max 500 mg per dose, oral stock 250 mg/5 mL.
DOSE_MG_PER_KG = 10
MAX_DOSE_MG = 500
STOCK_MG_PER_ML = 250 / 5          # = 50 mg/mL

def measurable(volume_ml):
    """Round DOWN to what an oral syringe can measure: 0.1 mL below 5 mL, 0.5 mL above."""
    step = 0.1 if volume_ml < 5 else 0.5
    return math.floor(volume_ml / step + 1e-9) * step

def exact_dose(weight_kg):
    if not 2 <= weight_kg <= 250:
        raise ValueError(f"weight {weight_kg} kg outside chart range")
    return min(DOSE_MG_PER_KG * weight_kg, MAX_DOSE_MG)

def make_bands(edges):
    """One row per band [lo, hi): dose computed at the band's LOWER edge, so no one in the band
    gets more than 10 mg/kg; report the mg/kg range actually delivered across the band."""
    rows = []
    for lo, hi in zip(edges[:-1], edges[1:]):
        vol = measurable(exact_dose(lo) / STOCK_MG_PER_ML)
        mg = vol * STOCK_MG_PER_ML
        rows.append((lo, hi, mg, vol, mg / hi, mg / lo))
    return rows

edges = [4, 5, 6, 8, 10, 12, 14, 16, 18, 20, 23, 26, 30, 35, 40, 45, 50, 250]
print(" weight band |  dose   | volume  | delivered mg/kg")
for lo, hi, mg, vol, kmin, kmax in make_bands(edges):
    if hi < 250:
        print(f"{f'{lo}-<{hi} kg':>12} | {mg:4.0f} mg | {vol:4.1f} mL | {kmin:4.1f} to {kmax:4.1f}")
    else:
        print(f"{f'>= {lo} kg':>12} | {mg:4.0f} mg | {vol:4.1f} mL | maximum dose (cap)")

# Validation against the formula over the full range, every 0.1 kg
bands = make_bands(edges)
ratios = []
for i in range(40, 2500):
    w = i / 10
    lo, hi, mg, *_ = next(b for b in bands if b[0] <= w < b[1])
    assert mg <= MAX_DOSE_MG and mg <= exact_dose(w) + 1e-9   # never above formula or cap
    ratios.append((mg / exact_dose(w), w))
print("lowest chart/formula ratio %.2f at %.1f kg; highest %.2f" % (*min(ratios), max(ratios)[0]))
```

Output:

```
 weight band |  dose   | volume  | delivered mg/kg
     4-<5 kg |   40 mg |  0.8 mL |  8.0 to 10.0
     5-<6 kg |   50 mg |  1.0 mL |  8.3 to 10.0
     6-<8 kg |   60 mg |  1.2 mL |  7.5 to 10.0
    8-<10 kg |   80 mg |  1.6 mL |  8.0 to 10.0
   10-<12 kg |  100 mg |  2.0 mL |  8.3 to 10.0
   12-<14 kg |  120 mg |  2.4 mL |  8.6 to 10.0
   14-<16 kg |  140 mg |  2.8 mL |  8.8 to 10.0
   16-<18 kg |  160 mg |  3.2 mL |  8.9 to 10.0
   18-<20 kg |  180 mg |  3.6 mL |  9.0 to 10.0
   20-<23 kg |  200 mg |  4.0 mL |  8.7 to 10.0
   23-<26 kg |  230 mg |  4.6 mL |  8.8 to 10.0
   26-<30 kg |  250 mg |  5.0 mL |  8.3 to  9.6
   30-<35 kg |  300 mg |  6.0 mL |  8.6 to 10.0
   35-<40 kg |  350 mg |  7.0 mL |  8.8 to 10.0
   40-<45 kg |  400 mg |  8.0 mL |  8.9 to 10.0
   45-<50 kg |  450 mg |  9.0 mL |  9.0 to 10.0
    >= 50 kg |  500 mg | 10.0 mL | maximum dose (cap)
lowest chart/formula ratio 0.76 at 7.9 kg; highest 1.00
```

The loop checks 2,460 weights. It confirms that no weight ever gets more than the formula or the cap, and it points directly at the band that needs splitting (7.9 kg).

### A structured, de-identified case log

```python
import csv, io, math, random, statistics
from dataclasses import dataclass, asdict, fields

@dataclass
class Case:
    case_id: str        # random code; the key linking it to the patient is stored separately
    month: str          # "2026-03": month, not date of birth or admission date
    age_band: str       # "0-1", "1-5", "5-12", "12-18", "18-65", "65+"
    sex: str            # "F", "M", "X"
    weight_kg: float
    dose_mg_per_kg: float
    complication: int   # pre-defined outcome: 1/0
    def __post_init__(self):
        if not 0.3 <= self.weight_kg <= 350:
            raise ValueError(f"{self.case_id}: implausible weight {self.weight_kg}")
        if self.complication not in (0, 1):
            raise ValueError(f"{self.case_id}: complication must be 0 or 1")

def wilson(k, n, z=1.96):
    """95% Wilson score interval for a proportion k/n."""
    p = k / n
    centre = (p + z*z/(2*n)) / (1 + z*z/n)
    half = z * math.sqrt(p*(1-p)/n + z*z/(4*n*n)) / (1 + z*z/n)
    return max(0.0, centre - half), min(1.0, centre + half)

# SYNTHETIC log of 120 cases (no real patients)
rng = random.Random(7)
bands = ["1-5", "5-12", "12-18", "18-65", "65+"]
log = []
for i in range(120):
    band = rng.choice(bands)
    wt = {"1-5": 15, "5-12": 30, "12-18": 55, "18-65": 78, "65+": 72}[band] * rng.uniform(0.75, 1.3)
    log.append(Case(f"C{rng.randrange(16**6):06x}", f"2026-{rng.randint(1, 9):02d}", band,
                    rng.choice("FM"), round(wt, 1), round(rng.gauss(9.6, 0.5), 1),
                    int(rng.random() < 0.06)))

buf = io.StringIO()                                   # export: one CSV, one row per case
w = csv.DictWriter(buf, fieldnames=[f.name for f in fields(Case)])
w.writeheader(); w.writerows(asdict(c) for c in log)
print(buf.getvalue().splitlines()[:3])

doses = [c.dose_mg_per_kg for c in log]
q1, med, q3 = statistics.quantiles(doses, n=4)
print(f"n={len(log)}  dose mg/kg median {med:.1f} (IQR {q1:.1f}-{q3:.1f}), max {max(doses)}")
k = sum(c.complication for c in log)
lo, hi = wilson(k, len(log))
print(f"complications {k}/{len(log)} = {k/len(log):.1%}  (95% CI {lo:.1%} to {hi:.1%})")
for b in bands:
    sub = [c for c in log if c.age_band == b]
    kb = sum(c.complication for c in sub)
    lo, hi = wilson(kb, len(sub))
    print(f"  {b:>6}: {kb}/{len(sub):<3} 95% CI {lo:.0%} to {hi:.0%}")
print(f"0 events in 20 cases: Wilson upper {wilson(0, 20)[1]:.1%}, rule of three {3/20:.0%}")
```

Output (synthetic data):

```
['case_id,month,age_band,sex,weight_kg,dose_mg_per_kg,complication', 'Cca264e,2026-01,12-18,F,69.9,9.7,0', 'C2c0146,2026-07,65+,M,62.5,9.4,0']
n=120  dose mg/kg median 9.6 (IQR 9.2-10.0), max 10.8
complications 8/120 = 6.7%  (95% CI 3.4% to 12.6%)
     1-5: 1/22  95% CI 1% to 22%
    5-12: 3/32  95% CI 3% to 24%
   12-18: 2/24  95% CI 2% to 26%
   18-65: 1/20  95% CI 1% to 24%
     65+: 1/22  95% CI 1% to 22%
0 events in 20 cases: Wilson upper 16.1%, rule of three 15%
```

The `__post_init__` check refuses impossible values at entry time. That is when they are cheapest to fix.

### From synthetic data to a points score, and an external check

```python
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

rng = np.random.default_rng(2026)

def simulate(n, intercept=-4.6):
    """SYNTHETIC adults: age (years), resp. rate >= 22, SpO2 < 94%, new confusion.
    The 'true' log-odds of the outcome (escalation within 48 h) is known to us."""
    age = rng.uniform(18, 95, n)
    rr22 = rng.random(n) < 0.25
    spo2 = rng.random(n) < 0.20
    conf = rng.random(n) < 0.10
    logit = intercept + 0.035 * age + 0.9 * rr22 + 1.1 * spo2 + 1.3 * conf
    y = rng.random(n) < 1 / (1 + np.exp(-logit))
    X = np.column_stack([age, rr22, spo2, conf]).astype(float)
    return X, y.astype(int)

X, y = simulate(1500)
print(f"development: n={len(y)}, events={y.sum()}, EPV={y.sum() / X.shape[1]:.0f}")
model = LogisticRegression(C=np.inf, max_iter=1000).fit(X, y)
b0, b = model.intercept_[0], model.coef_[0]
names = ["age (per year)", "RR >= 22", "SpO2 < 94%", "new confusion"]
for n_, bi in zip(names, b):
    print(f"  {n_:<15} beta = {bi:+.3f}   OR = {np.exp(bi):.2f}")

# Sullivan et al. (2004): age in bands with reference value W_ref; constant B = beta for 10 years of age
age_bands = [(18, 40, 29), (40, 60, 50), (60, 75, 67.5), (75, 96, 85)]   # (lo, hi, midpoint)
B = 10 * b[0]
age_pts = [round(b[0] * (mid - 29) / B) for _, _, mid in age_bands]
bin_pts = [round(bi / B) for bi in b[1:]]
print("B =", round(B, 3), "| age-band points", age_pts, "| RR, SpO2, confusion points", bin_pts)

def points(X):
    band = np.searchsorted([40, 60, 75], X[:, 0], side="right")
    return np.array(age_pts)[band] + X[:, 1:] @ np.array(bin_pts)

def risk_from_points(p):                     # log-odds at the reference profile + B per point
    return 1 / (1 + np.exp(-(b0 + b[0] * 29 + B * p)))

pts = points(X)
print("points -> predicted risk:", {int(p): f"{risk_from_points(p):.0%}" for p in range(0, int(pts.max()) + 1)})
print(f"AUC dev: full model {roc_auc_score(y, model.predict_proba(X)[:, 1]):.3f}, points {roc_auc_score(y, pts):.3f}")

# "External" site: same predictors, but a higher baseline risk (different patients, different referral pattern)
Xe, ye = simulate(1500, intercept=-4.0)
pe = risk_from_points(points(Xe))
lp = np.log(pe / (1 - pe)).reshape(-1, 1)
slope = LogisticRegression(C=np.inf).fit(lp, ye).coef_[0][0]
print(f"external: AUC {roc_auc_score(ye, pe):.3f}, observed {ye.mean():.1%} vs predicted {pe.mean():.1%}, "
      f"calibration slope {slope:.2f}")
```

Output:

```
development: n=1500, events=249, EPV=62
  age (per year)  beta = +0.034   OR = 1.03
  RR >= 22        beta = +0.908   OR = 2.48
  SpO2 < 94%      beta = +0.931   OR = 2.54
  new confusion   beta = +1.257   OR = 3.52
B = 0.336 | age-band points [0, 2, 4, 6] | RR, SpO2, confusion points [3, 3, 4]
points -> predicted risk: {0: '3%', 1: '4%', 2: '6%', 3: '8%', 4: '11%', 5: '15%', 6: '20%', 7: '26%', 8: '33%', 9: '41%', 10: '49%', 11: '57%', 12: '65%', 13: '73%', 14: '79%', 15: '84%', 16: '88%'}
AUC dev: full model 0.752, points 0.749
external: AUC 0.775, observed 23.5% vs predicted 18.0%, calibration slope 1.06
```

Three things to notice:

1. The points score loses almost nothing compared with the full model on the development data (AUC 0.749 vs 0.752).
2. At the "external" site, ranking is still good (AUC 0.775), but the score **under-predicts**: 18.0% predicted against 23.5% observed. The predictors work the same way there (slope ≈ 1), but the baseline risk is higher. The usual fix is to *recalibrate the intercept* on local data, which needs local data and approval.
3. EPV here is 62, which is generous. The next block shows what happens when it isn't.

### Overfitting when events are few

```python
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

rng = np.random.default_rng(11)
def simulate(n):                       # same SYNTHETIC truth as before
    age = rng.uniform(18, 95, n)
    Z = rng.random((n, 3)) < [0.25, 0.20, 0.10]
    logit = -4.6 + 0.035 * age + Z @ [0.9, 1.1, 1.3]
    X = np.column_stack([age, Z]).astype(float)
    return X, (rng.random(n) < 1 / (1 + np.exp(-logit))).astype(int)

Xv, yv = simulate(30000)               # a big "future" population to judge each model
for n_dev in (100, 300, 1500):
    slopes, apparent, future, epv = [], [], [], []
    for _ in range(60):
        X, y = simulate(n_dev)
        if y.sum() < 3: continue
        m = LogisticRegression(C=np.inf, max_iter=1000).fit(X, y)
        lp = m.decision_function(Xv).reshape(-1, 1)
        slopes.append(LogisticRegression(C=np.inf).fit(lp, yv).coef_[0][0])
        apparent.append(roc_auc_score(y, m.decision_function(X)))
        future.append(roc_auc_score(yv, lp.ravel()))
        epv.append(y.sum() / 4)
    print(f"n={n_dev:5d} EPV~{np.median(epv):4.1f}  AUC apparent {np.median(apparent):.3f} "
          f"-> future {np.median(future):.3f}   calibration slope {np.median(slopes):.2f}")
```

Output:

```
n=  100 EPV~ 3.9  AUC apparent 0.800 -> future 0.743   calibration slope 0.65
n=  300 EPV~11.8  AUC apparent 0.771 -> future 0.755   calibration slope 0.88
n= 1500 EPV~58.0  AUC apparent 0.765 -> future 0.760   calibration slope 0.95
```

With about 4 events per variable, the model looks *better* on its own data (apparent AUC 0.800) than it really is on future patients (0.743). Its calibration slope of 0.65 means its predictions are far too extreme. With more events, the gap closes and the slope approaches 1. One clinician's year of cases often sits in the top row.

## A checklist for a personal clinical scale

1. **Purpose.** What decision will this support, for which patients, and what will it never be used for?
2. **Source.** Which formula, guideline version or dataset is it based on? Is that cited on the tool itself?
3. **Design choices written down**: dose calculated at lower edge or midpoint, rounding increments and direction, caps, the weight to use, renal and hepatic flags.
4. **Exhaustive check against the formula** over the full range, with the worst case reported. Then an independent check of the printed or digital version.
5. **For data-driven scores**: pre-registered outcome definition, consecutive cases, enough events (EPV and a formal sample-size calculation), and internal validation.
6. **Discrimination and calibration**, then **external validation** in other clinicians' patients or another site.
7. **Information governance**: de-identification, approval as audit, service evaluation or research, and secure storage.
8. **Approval**: pharmacy and the drug and therapeutics committee for dosing tools; clinical governance and clinical safety (and the medical-device rules, if it is software) for scores.
9. **Version control, an owner and a review date.** Withdraw old copies when the guideline changes.
10. **Monitor in use**: audit errors, near misses and calibration drift.

## Practice

**1.** Drug X (10 mg/kg, maximum 500 mg, 50 mg/mL). Using the lower-edge rule and rounding down to 0.1 mL, what are the dose and volume for the band 35 to < 40 kg? What is the lowest mg/kg anyone in the band receives?

<details>
<summary>Answer</summary>

At 35 kg: 350 mg = 7.0 mL. Volumes from 5 mL round to 0.5 mL steps, and 7.0 is already a multiple. The lowest is just under $350/40 = 8.75$ mg/kg, at the top of the band (the chart shows 8.8).

</details>

**2.** Someone proposes a single band of 20 to < 30 kg at 200 mg. What is the worst delivered mg/kg, and what would you suggest?

<details>
<summary>Answer</summary>

$200/30 \approx 6.7$ mg/kg at the top of the band, only 67% of the target. Split the band (for example 20–23, 23–26 and 26–30 kg, as in the chart) and rerun the full-range validation.

</details>

**3.** In 25 consecutive procedures you had 0 complications. Give an approximate 95% upper confidence limit for your true rate.

<details>
<summary>Answer</summary>

Rule of three: $3/25 = 12\%$. Your true complication rate could plausibly be as high as about 12%. You can't claim it is near zero.

</details>

**4.** A log shows 3 complications in 40 cases. Compute the 95% Wilson interval.

<details>
<summary>Answer</summary>

$\hat p = 0.075$, $n = 40$, $z^2 = 3.8416$.
Centre: $(0.075 + 3.8416/80)/(1 + 3.8416/40) = (0.075 + 0.04802)/1.09604 = 0.1122$.
Half-width: $1.96\sqrt{0.075 \times 0.925/40 + 3.8416/6400}/1.09604 = 1.96\sqrt{0.0017344 + 0.0006003}/1.09604 = 1.96 \times 0.04832/1.09604 = 0.0864$.
The interval is about **2.6% to 19.9%**.

</details>

**5.** A model has $\beta = 0.70$ for "diabetes" and $\beta = 0.025$ per year of age. With $B$ = the effect of 5 years of age, how many points is diabetes worth?

<details>
<summary>Answer</summary>

$B = 5 \times 0.025 = 0.125$, and $0.70/0.125 = 5.6$, which rounds to **6** points. Having diabetes counts about as much as 28 extra years of age ($0.70/0.025 = 28$).

</details>

**6.** You develop a score with 6 candidate predictors on 300 patients, 24 of whom had the outcome. What is the EPV, and what do you expect to happen to its calibration slope in new patients?

<details>
<summary>Answer</summary>

EPV $= 24/6 = 4$. That is well below the old minimum of about 10, and modern methods would ask for more. Expect overfitting: apparent AUC higher than future AUC, and a calibration slope well below 1 (predictions too extreme). Collect more data, use fewer predictors or penalised regression, and validate internally (bootstrap) and externally.

</details>

**7.** Your score has AUC 0.80 in another hospital but predicts a mean risk of 10% where 20% of patients had the outcome. Is it "validated"?

<details>
<summary>Answer</summary>

Its discrimination held up, but its calibration did not. It under-predicts by about half, so any decision threshold based on its predicted risk would be wrong there. It needs recalibration (at least of the intercept) on local data, followed by re-validation and approval, before it is used.

</details>

## Further reading

- Sullivan LM, Massaro JM, D'Agostino RB Sr. Presentation of multivariate data for clinical use: the Framingham Study risk score functions. *Statistics in Medicine*. 2004;23:1631–1660.
- Peduzzi P, Concato J, Kemper E, Holford TR, Feinstein AR. A simulation study of the number of events per variable in logistic regression analysis. *Journal of Clinical Epidemiology*. 1996;49:1373–1379.
- Riley RD et al. Calculating the sample size required for developing a clinical prediction model. *BMJ*. 2020;368:m441.
- Collins GS, Reitsma JB, Altman DG, Moons KGM. Transparent reporting of a multivariable prediction model for individual prognosis or diagnosis (TRIPOD): the TRIPOD statement. *BMJ*. 2015;350:g7594.
- Wolff RF et al. PROBAST: a tool to assess the risk of bias and applicability of prediction model studies. *Annals of Internal Medicine*. 2019;170:51–58.
- Van Calster B et al. Calibration: the Achilles heel of predictive analytics. *BMC Medicine*. 2019;17:230.
- Steyerberg EW. *Clinical Prediction Models: A Practical Approach to Development, Validation, and Updating*. 2nd ed. Springer; 2019.

Related chapters: [units and concentrations](../../clinical-mathematics/units-concentrations-and-conversions/), [infusions and drip rates](../../clinical-mathematics/infusions-and-drip-rates/), [growth and BMI in children](../../clinical-mathematics/growth-and-bmi-in-children/) (a reference chart built from LMS formulas), [linear and logistic regression](../../classical-machine-learning/linear-and-logistic-regression/), [model evaluation](../../classical-machine-learning/model-evaluation/).
