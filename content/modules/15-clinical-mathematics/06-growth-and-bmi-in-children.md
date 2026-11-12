+++
summary = "Compute a child's BMI, turn it into a z-score and centile with the LMS method using real CDC and WHO reference values, classify it with the right cut-offs, and estimate mid-parental height and growth velocity."
+++

# Growth and BMI in Children

A 10-year-old girl has a BMI of 20.4 kg/m². By the adult cut-offs she is comfortably "normal". On a growth chart she sits above the 85th centile, which the CDC calls overweight and the WHO places above +1 SD. The arithmetic is the same in both cases, but the adult answer is wrong for her. Children's BMI changes a great deal with age and sex, so a child's number only means something when you compare it with other children of the same age and sex.

This chapter shows how that comparison works. You will compute BMI with dimensional analysis, see why adult thresholds fail, and learn the **LMS method** (Cole, 1990), which turns any measurement into a z-score and a centile. You will then apply it to **real reference rows** downloaded from the CDC and the WHO, and check the results against the centiles those organisations publish. We finish with weight-for-length under 2 years, corrected age for preterm infants, mid-parental height and growth velocity.

> [!CAUTION]
> These worked examples teach the arithmetic of growth assessment. They are not a diagnosis. In practice, plot measurements on the growth chart your service uses (for example UK-WHO charts in the UK, or WHO/CDC charts in the US). Use accurately measured weight and height and the child's exact age, and follow local guidance on what to do with the result. If a calculator and the chart disagree, find out why before you act.

## Key ideas

### BMI and its units

Body mass index is mass divided by height squared:

$$
\text{BMI} = \frac{\text{weight (kg)}}{\text{height (m)}^2} \quad [\text{kg/m}^2].
$$

Dimensional analysis catches the most common error. Height must be in **metres**. A 40 kg child who is 140 cm tall has BMI $40/1.40^2 = 20.4$. If you type 140 instead of 1.40, you get $0.0020$. If you forget to square, you get $28.6$. Neither of these could be a real BMI.

In US customary units, $1 \text{ lb} = 0.45359237$ kg and $1 \text{ in} = 0.0254$ m, so

$$
\text{BMI} = \frac{w_{\text{lb}} \times 0.45359237}{(h_{\text{in}} \times 0.0254)^2} = 703.07 \times \frac{w_{\text{lb}}}{h_{\text{in}}^2},
$$

which is where the familiar "× 703" comes from.

Because height is squared, a small error in height makes about twice that percentage error in BMI. A 1% error in height gives roughly a 2% error in BMI, since $(1.01)^{-2} \approx 0.98$. So you need a properly measured height. Use a stadiometer, or a length board for infants.

### Why adult cut-offs don't apply to children

For adults (18 or 20 and over, depending on the system), WHO uses fixed cut-offs: underweight below 18.5, overweight 25 or more, obesity 30 or more (class I 30–34.9, class II 35–39.9, class III 40 and above). Fixed cut-offs work in adults because adult BMI distributions change slowly with age.

In children the median moves a lot with age. These are the median BMIs (the $M$ column) for boys, taken from the CDC file `bmiagerev.csv` (Sex = 1):

| Age (Agemos) | 24.5 | 36.5 | 48.5 | 60.5 | 72.5 | 96.5 | 120.5 | 144.5 | 168.5 | 192.5 | 240 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Median BMI | 16.55 | 16.00 | 15.63 | 15.42 | 15.38 | 15.78 | 16.65 | 17.81 | 19.16 | 20.56 | 23.02 |

Median BMI **falls** from age 2 to about 5–6 years and then rises again. The low point is called the *adiposity rebound*. The median also differs between boys and girls, and the spread around it grows during childhood. A fixed number such as 25 would sit at completely different points of the distribution at ages 4, 10 and 16. So we describe a child's BMI by **where it sits among children of the same age and sex**.

### Centiles and z-scores

A **centile** (percentile) is the percentage of the reference population at or below a value. A **z-score** (SDS, standard deviation score) is the number of standard deviations from the reference median, after the distribution has been made normal. The two are linked by the standard normal CDF $\Phi$:

$$
\text{centile} = 100\,\Phi(z), \qquad \Phi(z) = \tfrac12\left[1 + \operatorname{erf}\!\left(\tfrac{z}{\sqrt 2}\right)\right].
$$

Useful anchors: $z = 0$ is the 50th centile, $z = \pm 1$ is about the 15.9th and 84.1th, $z = \pm 1.036$ is the 15th and 85th, $z = \pm 1.645$ is the 5th and 95th, $z = \pm 1.881$ is the 3rd and 97th, and $z = \pm 2$ is the 2.3rd and 97.7th.

Centiles are easier to explain to families. **Z-scores are better for calculations.** They are on a continuous scale, so you can average them and track change over time. They also keep separating children far from the median, where centiles bunch up near 0 or 100: a 99.6th and a 99.9th centile look alike, but their z-scores differ a lot.

### The LMS method

BMI in children is **skewed**: the right tail (heavier children) is longer than the left. A plain "(value − mean)/SD" would mislabel children in the tails. Cole's LMS method fixes this with three numbers for each age and sex:

- **L** (lambda): the Box–Cox power that removes the skew,
- **M** (mu): the median,
- **S** (sigma): the generalised coefficient of variation.

**Derivation.** The Box–Cox transform of a ratio $X/M$ is

$$
Y = \frac{(X/M)^L - 1}{L}.
$$

When $X = M$, $Y = 0$. The LMS model assumes that, at a given age, $Y$ is normally distributed with mean 0 and standard deviation $S$. Standardise by dividing by $S$:

> [!IMPORTANT]
> **LMS z-score** (Cole 1990)
> $$z = \frac{(X/M)^L - 1}{L\,S} \quad (L \ne 0), \qquad z = \frac{\ln(X/M)}{S} \quad (L = 0).$$
> **Inverse** (the value at a given z-score):
> $$X = M\,(1 + L\,S\,z)^{1/L} \quad (L \ne 0), \qquad X = M\,e^{S z} \quad (L = 0).$$

The $L = 0$ case is the limit of the general formula. As $L \to 0$, $(r^L - 1)/L \to \ln r$, which is why log-normal data have $L = 0$. To get the inverse, solve $z L S = (X/M)^L - 1$ for $X$.

Some checks on the formula. If $L = 1$, then $z = (X - M)/(M S)$, an ordinary z-score with SD $= M S$. That is why $S$ behaves like a coefficient of variation. A negative $L$ (as for BMI) shortens the long right tail, so the same distance above the median counts for fewer SDs than the same distance below it.

> [!WARNING]
> **Large positive z-scores get squeezed when $L < 0$.** As $X \to \infty$, $(X/M)^L \to 0$, so $z \to -1/(L S)$. The z-score cannot go above this limit. For CDC boys at Agemos 180.5 ($L = -2.132$, $S = 0.1351$) the limit is $z = 3.47$. A BMI of 35 gives $z = 2.43$, 40 gives $2.69$ and 45 gives only $2.86$. The CDC therefore advises against using LMS z-scores to track children with very high BMI. Use the **BMI as a percentage of the 95th centile** ("%BMIp95") instead, as in the extended BMI-for-age charts published in 2022.

### Which reference, which cut-offs

| System | Ages | Classification of BMI-for-age |
|---|---|---|
| **WHO Child Growth Standards** (2006) | 0–5 years | Under 5 years, weight-for-length/height or BMI-for-age: overweight > +2 SD, obesity > +3 SD (WHO also flags "possible risk of overweight" > +1 SD) |
| **WHO Growth Reference** (2007, de Onis et al.) | 5–19 years | Overweight > +1 SD, obesity > +2 SD; thinness < −2 SD, severe thinness < −3 SD |
| **CDC 2000 growth charts** | 2–20 years | Underweight < 5th; healthy 5th to < 85th; overweight 85th to < 95th; obesity ≥ 95th centile |
| **CDC extended BMI-for-age** (2022) | 2–20 years | Severe obesity ≥ 120% of the 95th centile (class 2: 120% to < 140%; class 3: ≥ 140%) |
| **UK90** (Cole, Freeman & Preece 1995), within the UK-WHO charts | 4–18 years | NICE clinical thresholds: overweight ≥ 91st, obesity ≥ 98th centile (population monitoring uses the 85th and 95th) |

The WHO *standards* (0–5) describe how healthy, breastfed children *should* grow under good conditions. The WHO 5–19 *reference* and the CDC charts describe how particular populations *did* grow. Different systems give different answers for the same child, so always state which one you used. The UK-WHO charts use WHO standards from 2 weeks to 4 years and UK90 data at birth and from 4 to 18 years.

### Under 2 years: weight-for-length

BMI-for-age is not used to diagnose overweight in infants under 2. Instead, use **weight-for-length** (length measured lying down) on the WHO standards. US guidance (Grummer-Strawn et al., 2010) recommends the WHO charts, not the CDC ones, for children under 2.

For babies born preterm, plot against **corrected age** until about 2 years:

$$
\text{corrected age} = \text{chronological age} - (40 - \text{gestational age at birth in weeks}) \text{ weeks}.
$$

### Mid-parental height and growth velocity

**Mid-parental height** (Tanner's method) estimates a child's adult height from the parents' heights. Men are on average about 13 cm taller than women, so you adjust for the child's sex before averaging:

$$
\text{boys: } \frac{h_{\text{father}} + h_{\text{mother}} + 13}{2}, \qquad \text{girls: } \frac{h_{\text{father}} + h_{\text{mother}} - 13}{2} \quad (\text{cm}).
$$

The **target range** is about ±8.5 cm around this figure (roughly ±2 SD; some sources use ±10 cm). If the child's height centile is far below the parents' expected centile, that is more informative than the height alone.

**Growth velocity** is the change in height divided by the time between measurements, in cm/year:

$$
v = \frac{h_2 - h_1}{t_2 - t_1 \text{ (years)}}.
$$

Measure over at least 6 months, and preferably 12. The error in each measurement can be a few millimetres, and over a short interval it gets divided by a small time, which inflates it. Velocity falls fast after infancy and stays fairly steady through mid-childhood until the pubertal growth spurt. A prepubertal child whose velocity stays low, so that they drift down across centile lines, needs a clinical review, whatever their current centile.

## Worked examples

All LMS values below are copied from two official files, downloaded on 12 November 2026:

- CDC `bmiagerev.csv` from `https://www.cdc.gov/growthcharts/data/zscore/bmiagerev.csv` (columns `Sex, Agemos, L, M, S, P3 … P97`; Sex 1 = male, 2 = female).
- WHO `bmi-girls-z-who-2007-exp.xlsx` and `bmi-boys-z-who-2007-exp.xlsx` (WHO Growth Reference 5–19 years, monthly LMS with SD columns).

> [!NOTE]
> **Agemos convention.** In the CDC file, half-month values stand for the middle of a completed month. A child aged 120 completed months (10 years 0 months to just under 10 years 1 month) uses the row `Agemos = 120.5`. The WHO 5–19 file is indexed by whole months starting at 61. Check the documentation of whichever table you use, because being half a month out matters most in infancy.

### Example 1 · Child (girl, 10 years 0 months): the full LMS calculation with real values

She weighs 40.0 kg and is 1.40 m tall.

**Step 1: BMI.** $40.0 / 1.40^2 = 40.0 / 1.96 = 20.41$ kg/m².

**Step 2: find the row.** CDC `bmiagerev.csv`, line 319 of the file (Sex = 2, Agemos = 120.5):

```
2,120.5,-2.171295888,16.86231366,0.137057004,13.7407435,14.03535405,14.5310003,15.49992271,16.86231366,18.69520235,19.98399779,21.03668675,22.98257733,24.60332779
```

So $L = -2.1713$, $M = 16.8623$, $S = 0.13706$. The published centiles include P85 = 19.98 and P95 = 22.98.

**Step 3: z-score.**

$$
\frac{X}{M} = \frac{20.408}{16.862} = 1.2103, \qquad 1.2103^{-2.1713} = 0.6607,
$$

$$
z = \frac{0.6607 - 1}{(-2.1713)(0.13706)} = \frac{-0.3393}{-0.2976} = +1.14.
$$

**Step 4: centile.** $100\,\Phi(1.14) = 87.3$, so she is at the 87th centile.

**Step 5: check against the published columns.** Her BMI of 20.41 lies between P85 (19.98) and P95 (22.98). That agrees with a centile between 85 and 95. Working backwards, the LMS inverse with $z = 1.0364$ gives $16.862 \times (1 + (-2.1713)(0.13706)(1.0364))^{-1/2.1713} = 19.98$, which is exactly the file's P85. Running the same check on every centile column of all 438 rows gives z-scores that match the published centiles to within $2.2 \times 10^{-8}$.

**Step 6: classify.**

- **CDC:** 85th ≤ centile < 95th, so *overweight*.
- **WHO 2007:** `bmi-girls-z-who-2007-exp.xlsx`, row Month = 120: $L = -1.4864$, $M = 16.6133$, $S = 0.12307$, with SD1 = 19.032 and SD2 = 22.570. Her z-score is $+1.44$ (92.5th centile). That is above +1 SD, so *overweight* by WHO too, although the two references put her at different z-scores.
- **Adult cut-offs:** 20.4 is "normal". This is the error the chapter opened with.

**Step 7: what weight is the 95th centile at her height?** $X_{95} = 22.98$, so $22.98 \times 1.40^2 = 45.0$ kg. The 85th centile is $19.98 \times 1.96 = 39.2$ kg. These are useful for counselling, but she is still growing in height, so a target BMI centile means more than a target weight.

### Example 2 · Young child (boy, 5 years 1 month): near the median

He weighs 18.5 kg and is 1.10 m tall. BMI $= 18.5 / 1.21 = 15.29$.

- CDC line 40 (Sex 1, Agemos 61.5): $L = -2.6848$, $M = 15.4095$, $S = 0.076482$. $z = -0.10$, which is the 46th centile: healthy weight.
- WHO boys row Month 61: $L = -0.7387$, $M = 15.2641$, $S = 0.0839$. $z = +0.02$.

*Sanity check:* his BMI is almost exactly the median $M$, so a z-score near 0 is what you should expect. If you got $z = 2$ here, something would be wrong (the row, the units or the sign of $L$).

### Example 3 · Adolescent (boy, 15 years 0 months): very high BMI

He weighs 95 kg and is 1.70 m tall. BMI $= 95 / 2.89 = 32.87$.

CDC line 159 (Sex 1, Agemos 180.5): $L = -2.1323$, $M = 19.8577$, $S = 0.13511$, P95 = 26.837.

- $z = +2.29$, which is the 98.9th centile, so he is at or above the 95th centile: obesity.
- $\%\text{BMIp95} = 32.87 / 26.837 = 122\%$. That is 120% or more, so **severe (class 2) obesity**. The 120% threshold is $1.2 \times 26.837 = 32.20$ and the 140% threshold is $37.57$.
- His z-score is in the compressed tail ($z > 1.88$, above the 97th centile). If he gains another 5 BMI units, his z-score only moves from 2.29 to about 2.6. Report and track **%BMIp95**, not z.
- WHO boys, Month 180 ($L = -1.4961$, $M = 19.7744$, $S = 0.12412$, SD2 = 26.969, SD3 = 34.081): $z = +2.87$, between +2 and +3 SD, so obesity.

### Example 4 · Infant (born at 32 weeks, now 20 weeks old)

His corrected age is $20 - (40 - 32) = 12$ weeks. Plot his weight, length and head circumference at 12 weeks on the WHO (or UK-WHO) charts. If you plot at 20 weeks he will look falsely small. To judge weight relative to size, use weight-for-length, not BMI-for-age thresholds. For actual values, read the WHO weight-for-length tables or the chart. Don't estimate them from memory.

### Example 5 · Growth velocity and mid-parental height (girl, 7 years)

She measured 120.0 cm, and 9 months later 124.2 cm. Her velocity is $4.2 / 0.75 = 5.6$ cm/year. With a measurement error of ±0.3 cm at each visit, the difference could be off by up to 0.6 cm, which is ±0.8 cm/year over 9 months. Over 3 months the same error would be ±2.4 cm/year, which is why short intervals mislead.

Her father is 180 cm and her mother 165 cm, so her mid-parental height is $(180 + 165 - 13)/2 = 166$ cm, with a target range of about 157.5–174.5 cm.

### Example 6 · Adult with obesity

An adult weighing 120 kg and 1.75 m tall has BMI $120 / 3.0625 = 39.2$, which is WHO obesity class II (35–39.9). Adult cut-offs apply here. NICE recommends lower action thresholds (23 for overweight, 27.5 for obesity) for people of South Asian, Chinese, other Asian, Middle Eastern, Black African or African-Caribbean family background, because their cardiometabolic risk rises at lower BMI.

### Example 7 · Older adult: the height problem

An 82-year-old woman weighs 58 kg. Her height was 1.66 m in mid-life, but she now measures 1.60 m because of vertebral compression. Her BMI is $58/1.60^2 = 22.7$ with today's height, or $58/1.66^2 = 21.0$ with the historical height. A 3.6% difference in height becomes a $(1.66/1.60)^2 - 1 = 7.6\%$ difference in BMI. In older adults BMI also cannot tell muscle loss from fat. Record which height you used, and use nutrition screening tools validated for older people rather than BMI alone.

## Sanity checks & common errors

> [!WARNING]
> - **Height in cm instead of m**: gives a BMI of about 0.002. Most code catches this, but some hand calculations don't.
> - **Adult cut-offs in a child**: a BMI of 20 can be overweight at 10 and underweight at 18.
> - **Wrong row**: the wrong sex (the CDC file codes 1 = male, 2 = female), or age in years used as months, or decimal age not converted to completed months. Always check that your answer agrees with the published centile columns next to L, M and S.
> - **Mixing references**: a WHO z-score and a CDC centile are not interchangeable. Example 1 gives $+1.14$ (CDC) against $+1.44$ (WHO) for the same girl.
> - **Trusting z far above the 97th centile** when $L < 0$: use %BMIp95 instead.
> - **Data gotcha**: CDC `bmiagerev.csv` repeats its header line before the girls' rows (line 221). A naive parser crashes or quietly reads `"L"` as a number.
> - **Velocity over too short an interval**: measurement error dominates.

Quick estimates that help:

- In a school-age child, BMI near the median $M$ means z ≈ 0.
- If BMI is about 20% above $M$ in mid-childhood, expect z somewhere around +1 to +1.5, because $S$ is 0.12–0.15.
- The published P85 and P95 columns let you classify a CDC result without computing z at all. Use them to check your calculation.

## In code

A reusable calculator using the three real CDC rows quoted above. In practice you would load the whole file, as shown in the second block. Note that `centile` uses only `math.erf`.

```python
import math

# Rows copied from CDC bmiagerev.csv (Sex 1 = male, 2 = female; Agemos = age in months).
# Each value is (L, M, S, P95). Download the full file to cover every month from 24 to 240.5.
CDC_BMI = {
    (1, 61.5):  (-2.684789516, 15.40947356, 0.076482128, 17.96602144),
    (2, 120.5): (-2.171295888, 16.86231366, 0.137057004, 22.98257733),
    (1, 180.5): (-2.132344989, 19.85766121, 0.135110159, 26.83688026),
}

def bmi(weight_kg, height_m):
    if not 0.3 <= weight_kg <= 350:
        raise ValueError(f"implausible weight {weight_kg} kg")
    if not 0.4 <= height_m <= 2.5:
        raise ValueError(f"implausible height {height_m} m (did you enter cm?)")
    return weight_kg / height_m**2

def lms_z(x, L, M, S):
    """Cole's LMS z-score."""
    if abs(L) < 1e-12:
        return math.log(x / M) / S
    return ((x / M) ** L - 1) / (L * S)

def lms_value(z, L, M, S):
    """Inverse: the measurement that sits at z-score z."""
    if abs(L) < 1e-12:
        return M * math.exp(S * z)
    return M * (1 + L * S * z) ** (1 / L)

def centile(z):
    """Standard normal CDF via math.erf, as a percentage."""
    return 50 * (1 + math.erf(z / math.sqrt(2)))

def cdc_category(sex, agemos, weight_kg, height_m):
    L, M, S, p95 = CDC_BMI[(sex, agemos)]
    b = bmi(weight_kg, height_m)
    z = lms_z(b, L, M, S)
    pct = centile(z)
    pct_p95 = 100 * b / p95
    if pct < 5:        cat = "underweight"
    elif pct < 85:     cat = "healthy weight"
    elif pct < 95:     cat = "overweight"
    elif pct_p95 < 120: cat = "obesity"
    elif pct_p95 < 140: cat = "severe obesity (class 2)"
    else:              cat = "severe obesity (class 3)"
    note = "  [z above ~1.88 (97th): report %BMIp95, not z]" if z > 1.88 else ""
    return f"BMI {b:.2f}  z {z:+.2f}  centile {pct:.1f}  {pct_p95:.0f}% of P95  -> {cat}{note}"

print("boy 5y1m :", cdc_category(1, 61.5, 18.5, 1.10))
print("girl 10y :", cdc_category(2, 120.5, 40.0, 1.40))
print("boy 15y  :", cdc_category(1, 180.5, 95.0, 1.70))

# BMI and weight at the 85th and 95th centiles for the 10-year-old girl, height 1.40 m
L, M, S, _ = CDC_BMI[(2, 120.5)]
for p, z in [(85, 1.0364334), (95, 1.6448536)]:
    b = lms_value(z, L, M, S)
    print(f"P{p}: BMI {b:.2f} -> weight {b * 1.40**2:.1f} kg at 1.40 m")
try:
    bmi(40, 140)
except ValueError as e:
    print("refused:", e)
```

Output:

```
boy 5y1m : BMI 15.29  z -0.10  centile 45.9  85% of P95  -> healthy weight
girl 10y : BMI 20.41  z +1.14  centile 87.3  89% of P95  -> overweight
boy 15y  : BMI 32.87  z +2.29  centile 98.9  122% of P95  -> severe obesity (class 2)  [z above ~1.88 (97th): report %BMIp95, not z]
P85: BMI 19.98 -> weight 39.2 kg at 1.40 m
P95: BMI 22.98 -> weight 45.0 kg at 1.40 m
refused: implausible height 140 m (did you enter cm?)
```

Once you have downloaded the official file, load it and **verify it before you trust it**. Every published centile column should convert back to its own z-score:

```python
import csv, math, sys
from statistics import NormalDist

def load_cdc_lms(path):
    """Read CDC bmiagerev.csv into {(sex, agemos): row}. Skips repeated header lines."""
    table = {}
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            if row["Sex"] not in ("1", "2"):      # the file repeats its header before the girls
                continue
            key = (int(row["Sex"]), float(row["Agemos"]))
            table[key] = {k: float(v) for k, v in row.items() if k not in ("Sex", "Agemos")}
    return table

def lms_z(x, L, M, S):
    return math.log(x / M) / S if abs(L) < 1e-12 else ((x / M) ** L - 1) / (L * S)

def check_table(table):
    """Every published centile column should map back to its own z-score."""
    nd = NormalDist()
    worst = 0.0
    for r in table.values():
        for p in (3, 5, 10, 25, 50, 75, 85, 90, 95, 97):
            z = lms_z(r[f"P{p}"], r["L"], r["M"], r["S"])
            worst = max(worst, abs(z - nd.inv_cdf(p / 100)))
    return worst

table = load_cdc_lms(sys.argv[1])
print(len(table), "rows; worst z mismatch =", f"{check_table(table):.1e}")
print("girl, Agemos 120.5:", {k: round(v, 4) for k, v in table[(2, 120.5)].items() if k in "LMS"})
```

Run as `python check_cdc.py bmiagerev.csv`:

```
438 rows; worst z mismatch = 2.2e-08
girl, Agemos 120.5: {'L': -2.1713, 'M': 16.8623, 'S': 0.1371}
```

The same check on the WHO 5–19 files (LMS against the SD columns, which are rounded to 3 decimals) agrees to within 0.0005 kg/m² for all 168 monthly rows of each sex.

## Practice

**1.** A girl weighs 50 kg and is 152 cm tall. What is her BMI? Why can't you say whether she is overweight from this number alone?

<details>
<summary>Answer</summary>

$50 / 1.52^2 = 50 / 2.3104 = 21.64$ kg/m². Whether that is high depends on her **age and sex**. At 10 years it would be above the CDC P85 for girls (19.98). At 18 it would be close to the median. You need the reference row for her age.

</details>

**2.** Using the CDC girls' row at Agemos 120.5 ($L = -2.171295888$, $M = 16.86231366$, $S = 0.137057004$), find the z-score and centile for a BMI of 15.0.

<details>
<summary>Answer</summary>

$X/M = 15.0/16.8623 = 0.88956$, and $0.88956^{-2.1713} = 1.2893$.
$z = (1.2893 - 1)/((-2.1713)(0.13706)) = 0.2893 / (-0.2976) = -0.97$.
Centile $= 100\,\Phi(-0.97) = 16.5$. That is within the healthy range (5th to < 85th). It is consistent with the file: P10 = 14.53 < 15.0 < P25 = 15.50.

</details>

**3.** With the same row, use the inverse LMS formula to find the BMI at the 5th centile ($z = -1.6449$). Check it against the file.

<details>
<summary>Answer</summary>

$X = 16.8623 \times (1 + (-2.1713)(0.13706)(-1.6449))^{-1/2.1713} = 16.8623 \times (1.4895)^{-0.4605} = 14.035$. The file's P5 column is 14.03535405, so they match.

</details>

**4.** Show that when $L = 1$ the LMS z-score is an ordinary z-score, and say what the SD is. What does $L = 0$ give?

<details>
<summary>Answer</summary>

With $L = 1$: $z = (X/M - 1)/S = (X - M)/(M S)$, a normal z-score with mean $M$ and SD $M S$, so $S$ is the coefficient of variation. With $L = 0$: $z = \ln(X/M)/S$, so $\ln X$ is normal (log-normal data) and the inverse is $X = M e^{Sz}$.

</details>

**5.** A girl's father is 175 cm and her mother 160 cm. Find her mid-parental height and target range.

<details>
<summary>Answer</summary>

$(175 + 160 - 13)/2 = 161.0$ cm. Target range is about $161 \pm 8.5$ cm, that is 152.5–169.5 cm (some sources use ±10 cm).

</details>

**6.** A prepubertal boy measures 131.2 cm, then 134.0 cm seven months later. What is his height velocity, and what should make you cautious about it?

<details>
<summary>Answer</summary>

$2.8 / (7/12) = 4.8$ cm/year. The interval is short, and a measurement error of a few millimetres at each visit can change the velocity by more than 1 cm/year. Repeat over 12 months with the same stadiometer and technique, and interpret it alongside his centile trajectory and mid-parental height.

</details>

**7.** A 15-year-old boy has BMI 38.0. Using the CDC P95 at Agemos 180.5 (26.837), classify him. Why not report his z-score?

<details>
<summary>Answer</summary>

$38.0 / 26.837 = 141.6\%$ of P95, which is 140% or more, so class 3 (severe) obesity. With $L = -2.132$ and $S = 0.1351$ the LMS z-score can never exceed $-1/(LS) = 3.47$, so very high BMIs are squeezed together. Changes in %BMIp95 track change much better at this level.

</details>

**8.** Convert: an adolescent is 5 ft 4 in (64 in) and 140 lb. Find the BMI two ways.

<details>
<summary>Answer</summary>

Shortcut: $703 \times 140 / 64^2 = 24.03$. Exact: $140 \times 0.45359237 = 63.50$ kg, and $64 \times 0.0254 = 1.6256$ m, so $63.50/1.6256^2 = 24.03$ kg/m². Then look up the BMI-for-age centile for age and sex.

</details>

## Further reading

- Cole TJ. The LMS method for constructing normalized growth standards. *European Journal of Clinical Nutrition*. 1990;44:45–60.
- Cole TJ, Green PJ. Smoothing reference centile curves: the LMS method and penalized likelihood. *Statistics in Medicine*. 1992;11:1305–1319.
- Cole TJ, Freeman JV, Preece MA. Body mass index reference curves for the UK, 1990. *Archives of Disease in Childhood*. 1995;73:25–29.
- Kuczmarski RJ et al. 2000 CDC Growth Charts for the United States: methods and development. *Vital and Health Statistics* Series 11, No. 246. 2002.
- WHO Multicentre Growth Reference Study Group. WHO Child Growth Standards based on length/height, weight and age. *Acta Paediatrica* Suppl. 2006;450:76–85.
- de Onis M, Onyango AW, Borghi E, Siyam A, Nishida C, Siekmann J. Development of a WHO growth reference for school-aged children and adolescents. *Bulletin of the World Health Organization*. 2007;85:660–667.
- Grummer-Strawn LM, Reinold C, Krebs NF. Use of World Health Organization and CDC growth charts for children aged 0–59 months in the United States. *MMWR Recommendations and Reports*. 2010;59(RR-9).
- Data: CDC growth chart LMS files (cdc.gov/growthcharts, "Percentile Data Files with LMS Values") and the WHO growth reference 5–19 years tables (who.int). Software: WHO Anthro and AnthroPlus. These adjust z-scores beyond ±3 SD for some indicators, so use them for extreme values.

Related chapters: [weight and body-size-based dosing](../../clinical-mathematics/weight-and-body-size-based-dosing/) (why weight, BSA and IBW matter for drugs), [nutrition and energy](../../clinical-mathematics/nutrition-energy-and-parenteral-calculations/), and [distributions and likelihood](../../probability-and-statistics/distributions-and-likelihood/) for the normal distribution behind z-scores.
