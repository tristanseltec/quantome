+++
summary = "Calculate weight-based doses with caps and divided doses, choose and compute total, ideal, adjusted and lean body weight and body surface area, estimate renal function, and use Vd, clearance and half-life to reason about loading and maintenance doses."
+++

# Weight- and Body-Size-Based Dosing

An adult and a 4 kg infant cannot receive the same dose of most drugs. The obvious fix is to scale the dose with body size: so many mg per kg, or per square metre of body surface. Scaling works well for most children, but it raises questions that this chapter answers with simple algebra. What happens when a large teenager's mg/kg dose exceeds the adult dose? Which "weight" do you use in a patient with obesity, when fat and muscle handle drugs differently? How do kidneys that clear less drug change the dose? And why does a drug take days to reach a steady level in some patients and hours in others?

The arithmetic builds on [units, concentrations and conversions](../../clinical-mathematics/units-concentrations-and-conversions/). The pharmacokinetics section uses exponential decay, which you can revisit in [exponents and roots](../../algebra/exponents-and-roots/).

> [!CAUTION]
> The worked examples teach arithmetic, not prescribing. "Drug X", "Drug Y" and the other generic drugs below are illustrative, and their numbers were chosen for clarity. Real doses, caps, dosing weights and renal adjustments differ by drug, indication and country. Always check against the current local formulary or guideline (for example the BNF or BNFc, national guidance, or your hospital protocol), and use an independent double-check, especially for children.

## Key ideas

### mg/kg dosing with a cap

The simplest rule is proportional: dose $= w \times d$, where $w$ is weight in kg and $d$ is the dose in mg/kg. The units check: $\text{kg} \times \text{mg/kg} = \text{mg}$.

Proportional scaling would give a 90 kg teenager more than the usual adult dose, so weight-based doses come with a **maximum** (often the usual adult dose):

$$
\text{dose} = \min(w \times d,\ \text{maximum dose}).
$$

> [!IMPORTANT]
> **Capped weight-based dose**
> $$\text{dose (mg)} = \min\big(\text{weight (kg)} \times \text{dose (mg/kg)},\ \text{max dose (mg)}\big)$$
> Then convert to a volume with $\text{volume} = \text{dose} / \text{concentration}$.

### mg/kg/day and divided doses

Many doses are written per day, to be split into $n$ equal doses:

$$
\text{each dose} = \frac{w \times d_{\text{day}}}{n}.
$$

Read the prescription carefully. "30 mg/kg/day in 3 divided doses" means 10 mg/kg per dose. "30 mg/kg three times a day" means 90 mg/kg per day. Confusing the two is a classic three-fold error. Caps can apply to each dose, to the daily total, or both.

### Which weight? Total, ideal, adjusted and lean

In a lean patient, all reasonable definitions of weight are close. In obesity they diverge, and the choice matters because fat tissue holds water-soluble drugs poorly and contributes less to clearance than lean tissue.

- **Total body weight (TBW):** what the scale says.
- **Ideal body weight (IBW):** a weight predicted from height and sex. The most widely used formula is from **Devine (1974)**, originally written in inches:

$$
\text{IBW}_{\text{male}} = 50 + 2.3 \times (\text{height in inches} - 60), \qquad
\text{IBW}_{\text{female}} = 45.5 + 2.3 \times (\text{height in inches} - 60).
$$

  Since 1 inch = 2.54 cm, "inches over 60" is $(\text{height (cm)}/2.54) - 60$. The formula is meant for adults of at least 5 ft (152 cm). Below that it gives implausibly low values.

- **Adjusted body weight (AdjBW):** IBW plus a fraction of the excess. The factor 0.4 is the one most often used:

$$
\text{AdjBW} = \text{IBW} + 0.4\,(\text{TBW} - \text{IBW}).
$$

- **Lean body weight (LBW):** weight minus fat. A common formula is **Janmahasatian et al. (2005)**, with BMI in kg/m²:

$$
\text{LBW}_{\text{male}} = \frac{9270 \times \text{TBW}}{6680 + 216 \times \text{BMI}}, \qquad
\text{LBW}_{\text{female}} = \frac{9270 \times \text{TBW}}{8780 + 244 \times \text{BMI}}.
$$

Which one a drug uses depends on how it distributes and how it is cleared, and the drug's own guidance decides. In general terms:

| Situation | Weight commonly used | Reasoning |
|---|---|---|
| Patient not obese | TBW | All weights are similar |
| Water-soluble drugs that stay mostly in lean tissue and extracellular fluid (aminoglycosides are the textbook example) | IBW or AdjBW in obesity | Fat adds little to the volume of distribution |
| Drugs whose guidance specifies TBW, often with a maximum | TBW, capped | Set by the drug's own studies |
| Some anaesthetic and highly lipid-soluble agents | LBW for some doses, TBW for others | Depends on the drug and on loading versus maintenance |
| Children | Measured weight, and IBW-type adjustments only if obese and if guidance says so | Growth makes adult formulas unreliable |

> [!NOTE]
> This table describes patterns, not rules. For any specific drug, use the dosing weight that your formulary or local protocol names. When a guideline says "use adjusted body weight", check which factor it means (0.4 is usual, but not universal).

### Body surface area (BSA)

Some drugs, mainly cytotoxic chemotherapy, are dosed per m² of body surface area. BSA tracks metabolic rate and organ size across ages more closely than weight does. Two standard formulas, with height $h$ in cm and weight $w$ in kg:

> [!IMPORTANT]
> **Mosteller (1987)**
> $$\text{BSA (m}^2) = \sqrt{\frac{h \times w}{3600}}$$
> **Du Bois and Du Bois (1916)**
> $$\text{BSA (m}^2) = 0.007184 \times w^{0.425} \times h^{0.725}$$

Mosteller is popular because you can do it on a basic calculator. For most adults the two agree within a few percent. A typical adult is about 1.7 to 2.0 m², which is a useful sanity check.

### Estimating a child's weight when you can't measure it

**Always weigh the child.** Only when that is impossible (for example in resuscitation before arrival or in the first minutes), age-based estimates give a starting point. Recent editions of the UK Advanced Paediatric Life Support (APLS) manual teach:

| Age | Estimated weight (kg) |
|---|---|
| 0 to 12 months | $0.5 \times \text{age in months} + 4$ |
| 1 to 5 years | $2 \times \text{age in years} + 8$ |
| 6 to 12 years | $3 \times \text{age in years} + 7$ |

> [!WARNING]
> Age-based formulas are a **last resort**. They are built from average children and can be badly wrong for an individual: they underestimate weight in populations with high obesity rates and overestimate it in malnourished children. Length-based tapes (such as the Broselow tape) or a parent's recent weight are usually better. Replace the estimate with a measured weight as soon as you can.

### Historical age and weight rules (do not use)

Before weight-based dosing became standard, children's doses were derived from the adult dose:

- **Clark's rule:** child dose $= \text{adult dose} \times \dfrac{\text{weight in lb}}{150}$.
- **Young's rule:** child dose $= \text{adult dose} \times \dfrac{\text{age in years}}{\text{age} + 12}$.

They are history only. Children are not small adults: their body water, organ maturity and clearance change with age in ways a single ratio cannot capture. Modern paediatric formularies give drug-specific doses by weight and age band.

### Renal function: Cockcroft–Gault and bedside Schwartz

Many drugs are cleared by the kidney, so the dose must fall when kidney function falls. Two classic estimates:

**Cockcroft–Gault (1976)** estimates creatinine clearance (CrCl) in adults, in mL/min, from age, weight and serum creatinine (SCr) in mg/dL:

> [!IMPORTANT]
> **Cockcroft–Gault**
> $$\text{CrCl (mL/min)} = \frac{(140 - \text{age}) \times \text{weight (kg)}}{72 \times \text{SCr (mg/dL)}} \times (0.85 \text{ if female})$$
> With SCr in µmol/L, divide it by 88.4 first. Equivalently, $\text{CrCl} = \dfrac{1.23 \times (140 - \text{age}) \times \text{weight}}{\text{SCr (µmol/L)}}$ for men, with factor 1.04 for women (since $88.4/72 \approx 1.23$ and $1.23 \times 0.85 \approx 1.04$).

Each piece makes sense. Creatinine comes from muscle, so more weight means more creatinine produced, and a given SCr implies a higher clearance. Muscle mass falls with age, so $(140 - \text{age})$ shrinks. Women have less muscle on average, hence the 0.85.

Laboratories usually report **eGFR** from equations such as CKD-EPI, normalised to a standard 1.73 m² of body surface. Many drug labels were built on Cockcroft–Gault, which gives an absolute clearance in mL/min. Which estimate to use for a given drug is set by its guidance. In older adults with low muscle mass, a "normal" creatinine can hide significant impairment, and in obesity, using TBW in Cockcroft–Gault overestimates clearance (see Example 6).

**Bedside Schwartz (Schwartz et al., 2009)** estimates GFR in children from height and creatinine:

> [!IMPORTANT]
> **Bedside Schwartz**
> $$\text{eGFR (mL/min/1.73 m}^2) = \frac{0.413 \times \text{height (cm)}}{\text{SCr (mg/dL)}} = \frac{36.5 \times \text{height (cm)}}{\text{SCr (µmol/L)}}$$
> The constant 0.413 assumes an enzymatic creatinine assay.

For example, a 10-year-old who is 140 cm tall with SCr 0.6 mg/dL (53 µmol/L) has $0.413 \times 140 / 0.6 \approx 96$ mL/min/1.73 m².

### Basic pharmacokinetics: Vd, clearance and half-life

Three quantities describe what the body does to a drug.

- **Volume of distribution** $V_d$ (L) links the amount of drug in the body $A$ to the plasma concentration $C$: $A = V_d \times C$. It is an apparent volume. A drug that hides in fat or tissue has a huge $V_d$, larger than the body itself.
- **Clearance** $CL$ (L/h) is the volume of plasma completely cleared of drug per unit time. The elimination rate is $CL \times C$ (mg/h).
- **Half-life** $t_{1/2}$ is the time for the concentration to halve.

**Deriving the half-life.** For most drugs at usual doses, elimination rate is proportional to concentration (first-order kinetics). The amount changes as

$$
\frac{dA}{dt} = -CL \times C = -\frac{CL}{V_d}\,A.
$$

The solution is exponential decay, $A(t) = A_0 e^{-kt}$ with $k = CL/V_d$. Setting $A = A_0/2$ gives $e^{-kt_{1/2}} = 1/2$, so

$$
t_{1/2} = \frac{\ln 2}{k} = \frac{0.693 \times V_d}{CL}.
$$

Half-life rises if $V_d$ rises (more drug hidden away from the eliminating organs) or if $CL$ falls (kidneys or liver working less).

**Loading dose.** To reach a target concentration $C_t$ at once, you must fill the volume: amount $= V_d \times C_t$. If only a fraction $F$ (the **bioavailability**, 1 for IV) of an oral dose reaches the circulation, you give more:

> [!IMPORTANT]
> **Loading dose**
> $$\text{LD} = \frac{V_d \times C_t}{F}$$
> **Maintenance dose rate** (at steady state, rate in = rate out, so $F \times \text{dose rate} = CL \times C_{ss}$)
> $$\text{MD rate} = \frac{CL \times C_{ss}}{F}$$
> For intermittent dosing every $\tau$ hours, each dose is $\text{MD rate} \times \tau$.

**Time to steady state.** Without a loading dose, after $n$ half-lives the concentration has reached $1 - (1/2)^n$ of its steady-state value:

| Half-lives | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| Fraction of steady state | 50% | 75% | 87.5% | 93.75% | 96.9% |

Hence the rule of thumb: **steady state takes about 4 to 5 half-lives**, whatever the dose. A bigger maintenance dose gives a higher steady state, not a faster one. A loading dose is how you get there faster.

> [!TIP]
> In renal impairment a renally cleared drug has a lower $CL$. The **maintenance** dose falls in proportion. The **loading** dose depends on $V_d$, not $CL$, so it usually stays the same. The half-life gets longer, so steady state (and accumulation if you don't adjust) takes longer too.

## Worked examples

### Example 1 · Infant (7 kg): a simple mg/kg dose

**Problem.** Drug X (illustrative): 10 mg/kg per dose, max 500 mg per dose. Stock 250 mg/5 mL. Find the dose and volume.

**Estimate.** 7 kg × 10 mg/kg is about 70 mg, well below the cap. The stock is 50 mg/mL, so a bit more than 1 mL.

**Calculate.** Stock: $250/5 = 50$ mg/mL. Dose: $7 \times 10 = 70$ mg. Volume: $70/50 = 1.4$ mL.

### Example 2 · Child (4 years, 18 kg): mg/kg/day in divided doses, and estimating weight

**Problem.** Drug X is ordered as 30 mg/kg/day in 3 divided doses. The child was weighed at 18 kg.

**Calculate.** Daily: $18 \times 30 = 540$ mg. Each dose: $540/3 = 180$ mg, which is $180/50 = 3.6$ mL of the 50 mg/mL stock, three times a day. (Per dose this is 10 mg/kg, matching Example 1.)

**If the child could not be weighed.** The APLS formula for 1 to 5 years gives $2 \times 4 + 8 = 16$ kg. Doses based on it would be $(18-16)/18 \approx 11\%$ lower than with the true weight. Here that error is modest. In a child far from the average, it can be much larger, which is why the formula is a last resort.

### Example 3 · Adolescent (14 years, 62 kg): hitting the cap

**Problem.** Same Drug X, 10 mg/kg per dose, max 500 mg.

**Calculate.** $62 \times 10 = 620$ mg, which exceeds 500 mg. Give **500 mg**, which is $500/50 = 10$ mL.

**Check.** An adolescent who weighs as much as a small adult should never receive more than an adult. The cap does that. Any paediatric dose that exceeds the usual adult dose should trigger a second look.

### Example 4 · Adult (170 cm, 70 kg): BSA dosing and a loading dose

**BSA.** Mosteller: $\sqrt{170 \times 70/3600} = \sqrt{3.306} \approx 1.82$ m². Du Bois: $0.007184 \times 70^{0.425} \times 170^{0.725} \approx 1.81$ m². They agree within 1%. A Drug B at 100 mg/m² would be $100 \times 1.82 \approx 182$ mg.

**Pharmacokinetics.** Drug Y (illustrative) has $V_d = 0.5$ L/kg, $CL = 3$ L/h, target $C = 10$ mg/L, given IV ($F = 1$).

- $V_d = 0.5 \times 70 = 35$ L.
- Loading dose: $35 \times 10 = 350$ mg.
- Maintenance rate: $3 \times 10 = 30$ mg/h, that is 720 mg/day, or 240 mg every 8 hours.
- Half-life: $0.693 \times 35/3 \approx 8.1$ h, so without a loading dose steady state takes about $4$ to $5 \times 8.1 \approx 32$ to $40$ hours.

If the same drug were given orally with $F = 0.8$, both doses would be divided by 0.8: a 437.5 mg load and 900 mg/day maintenance.

### Example 5 · Older adult with renal impairment (82 years, woman, 60 kg, SCr 120 µmol/L)

**Renal function.** Convert: $120/88.4 \approx 1.357$ mg/dL. Then

$$
\text{CrCl} = \frac{(140 - 82) \times 60}{72 \times 1.357} \times 0.85 \approx 30\ \text{mL/min}.
$$

With the SI shortcut, $1.04 \times 58 \times 60/120 \approx 30.2$ mL/min. The same answer, as expected.

Note that SCr 120 µmol/L looks only mildly raised, yet her clearance is roughly a third of a young adult's. Low muscle mass in older people hides renal impairment.

**Effect on Drug Y.** Suppose Drug Y is cleared entirely by the kidneys, and its clearance falls in proportion to CrCl, from 3 L/h at 100 mL/min to $3 \times 30/100 = 0.9$ L/h. Her $V_d = 0.5 \times 60 = 30$ L.

- Loading dose (unchanged rule): $30 \times 10 = 300$ mg. It is lower than in Example 4 only because she weighs less.
- Maintenance: $0.9 \times 10 = 9$ mg/h, that is 216 mg/day, less than a third of the 720 mg/day in Example 4.
- Half-life: $0.693 \times 30/0.9 \approx 23$ h. Steady state takes about $92$ to $115$ hours, roughly 4 to 5 days.

Giving her the "standard" 720 mg/day would make the drug accumulate to more than three times the target over several days. This is the mechanism behind much drug toxicity in older people.

### Example 6 · Obese adult (man, 180 cm, 130 kg, age 45, SCr 90 µmol/L)

**Weights.**

- BMI $= 130/1.8^2 \approx 40.1$ kg/m².
- Height in inches: $180/2.54 \approx 70.9$. IBW $= 50 + 2.3 \times (70.9 - 60) \approx 75.0$ kg.
- AdjBW $= 75.0 + 0.4 \times (130 - 75.0) \approx 97.0$ kg.
- LBW $= 9270 \times 130/(6680 + 216 \times 40.1) \approx 78.5$ kg.

**Renal function depends on the weight you choose.** Cockcroft–Gault with SCr $90/88.4 \approx 1.018$ mg/dL:

| Weight used | kg | CrCl (mL/min) |
|---|---|---|
| TBW | 130 | about 168 |
| AdjBW | 97.0 | about 126 |
| IBW | 75.0 | about 97 |

The estimates span almost a factor of two. Using TBW overestimates his clearance, because fat does not produce creatinine. Local guidance usually specifies which weight to use in Cockcroft–Gault for obese patients. A drug dosed at 10 mg/kg would be 1,300 mg on TBW and 970 mg on AdjBW (before any cap), so the choice of weight is a clinical decision with large consequences.

## Sanity checks and common errors

- **Weight in kg, measured today.** A weight in pounds entered as kg multiplies every dose by 2.2. An old weight in a growing child underdoses.
- **Per dose or per day?** Read "mg/kg/day in divided doses" and "mg/kg per dose" aloud before calculating.
- **Never exceed the adult dose** without a specific, documented reason. Caps are part of the dose.
- **Which weight?** In obesity, write down which weight you used and why. Using TBW for a drug meant for IBW can double the dose.
- **Creatinine units.** mg/dL and µmol/L differ by 88.4. Putting µmol/L into the mg/dL form of Cockcroft–Gault gives a clearance 88 times too low.
- **eGFR is not CrCl.** eGFR is normalised to 1.73 m². In a very small or very large patient, the absolute clearance differs.
- **Loading doses don't scale with renal function**, maintenance doses do. Reducing both is a common error that leaves patients undertreated for days.
- **Plausibility.** BSA for an adult is around 1.5 to 2.5 m². A BSA near 5.7 m² (for a 170 cm, 70 kg adult) means height was entered in mm; near 57 m², weight in grams.

## In code

The calculator below refuses impossible weights, caps doses, and computes the body-size quantities from this chapter. It reproduces Examples 1 to 6.

```python
from math import sqrt

def check_weight(kg):
    if not 0.3 <= kg <= 350:
        raise ValueError(f"implausible weight {kg} kg: re-weigh or re-check the units")
    return kg

def weight_dose(kg, mg_per_kg, max_mg=None):
    """Single dose in mg, capped at max_mg (the usual adult dose)."""
    dose = check_weight(kg) * mg_per_kg
    if max_mg is not None and dose > max_mg:
        print(f"  CAP: {dose:.0f} mg exceeds {max_mg} mg; giving {max_mg} mg")
        dose = max_mg
    return dose

def ideal_body_weight(height_cm, sex):
    """Devine (1974): 50 kg (male) or 45.5 kg (female) + 2.3 kg per inch over 5 ft."""
    base = {"male": 50.0, "female": 45.5}[sex]
    return base + 2.3 * (height_cm / 2.54 - 60)

def adjusted_body_weight(tbw, ibw, factor=0.4):
    return ibw + factor * (tbw - ibw) if tbw > ibw else tbw

def lean_body_weight(tbw, height_cm, sex):
    """Janmahasatian et al. (2005)."""
    bmi = tbw / (height_cm / 100) ** 2
    a, b = {"male": (6680, 216), "female": (8780, 244)}[sex]
    return 9270 * tbw / (a + b * bmi)

def bsa_mosteller(height_cm, kg):
    return sqrt(height_cm * check_weight(kg) / 3600)

def cockcroft_gault(age, kg, scr_umol_l, sex):
    """Creatinine clearance (mL/min); SCr converted to mg/dL by dividing by 88.4."""
    scr_mg_dl = scr_umol_l / 88.4
    crcl = (140 - age) * check_weight(kg) / (72 * scr_mg_dl)
    return crcl * (0.85 if sex == "female" else 1.0)

def bedside_schwartz(height_cm, scr_umol_l):
    """eGFR (mL/min/1.73 m^2) = 0.413 x height (cm) / SCr (mg/dL)."""
    return 0.413 * height_cm / (scr_umol_l / 88.4)

# Drug X (illustrative): 10 mg/kg per dose, max 500 mg; stock 250 mg/5 mL = 50 mg/mL
for kg in (7, 18, 62):
    mg = weight_dose(kg, 10, max_mg=500)
    print(f"{kg:>3} kg: {mg:.0f} mg = {mg / 50:.1f} mL")

ibw = ideal_body_weight(180, "male")
abw = adjusted_body_weight(130, ibw)
lbw = lean_body_weight(130, 180, "male")
print(f"180 cm, 130 kg man: IBW {ibw:.1f}, AdjBW {abw:.1f}, LBW {lbw:.1f} kg")
for name, w in (("TBW", 130), ("IBW", ibw), ("AdjBW", abw)):
    print(f"  CrCl with {name:<5}: {cockcroft_gault(45, w, 90, 'male'):.0f} mL/min")
print(f"BSA 170 cm, 70 kg: {bsa_mosteller(170, 70):.2f} m^2")
print(f"CrCl, woman 82 y, 60 kg, SCr 120: {cockcroft_gault(82, 60, 120, 'female'):.0f} mL/min")
print(f"Schwartz, 140 cm, SCr 53: {bedside_schwartz(140, 53):.0f} mL/min/1.73 m^2")
try:
    weight_dose(700, 10)
except ValueError as e:
    print("Refused:", e)
```

Output:

```
  7 kg: 70 mg = 1.4 mL
 18 kg: 180 mg = 3.6 mL
  CAP: 620 mg exceeds 500 mg; giving 500 mg
 62 kg: 500 mg = 10.0 mL
180 cm, 130 kg man: IBW 75.0, AdjBW 97.0, LBW 78.5 kg
  CrCl with TBW  : 168 mL/min
  CrCl with IBW  : 97 mL/min
  CrCl with AdjBW: 126 mL/min
BSA 170 cm, 70 kg: 1.82 m^2
CrCl, woman 82 y, 60 kg, SCr 120: 30 mL/min
Schwartz, 140 cm, SCr 53: 96 mL/min/1.73 m^2
Refused: implausible weight 700 kg: re-weigh or re-check the units
```

A natural extension is to print a whole weight-band table from `weight_dose`. The chapter on [building your own clinical scales](../../clinical-mathematics/building-your-own-clinical-scales/) does exactly that, with rounding to measurable volumes, and discusses how to validate such a table before anyone uses it.

## Practice

1. A 9 kg infant is prescribed Drug X 10 mg/kg (max 500 mg). Stock 250 mg/5 mL. Dose and volume?

<details>
<summary>Answer</summary>

$9 \times 10 = 90$ mg (below the cap). Stock is 50 mg/mL, so $90/50 = 1.8$ mL.

</details>

2. A 25 kg child is prescribed an illustrative Drug A at 40 mg/kg/day in 4 divided doses. What is each dose?

<details>
<summary>Answer</summary>

Daily $25 \times 40 = 1{,}000$ mg. Each dose $1{,}000/4 = 250$ mg, four times a day.

</details>

3. Use Mosteller to find the BSA of a patient 150 cm tall weighing 45 kg.

<details>
<summary>Answer</summary>

$\sqrt{150 \times 45/3600} = \sqrt{1.875} \approx 1.37$ m².

</details>

4. A woman is 165 cm tall and weighs 110 kg. Find her Devine IBW and her adjusted body weight (factor 0.4).

<details>
<summary>Answer</summary>

$165/2.54 \approx 64.96$ inches. IBW $= 45.5 + 2.3 \times 4.96 \approx 56.9$ kg. AdjBW $= 56.9 + 0.4 \times (110 - 56.9) \approx 78.1$ kg.

</details>

5. A 70-year-old man weighs 75 kg and has SCr 150 µmol/L. Estimate his creatinine clearance with Cockcroft–Gault.

<details>
<summary>Answer</summary>

$150/88.4 \approx 1.697$ mg/dL. $\text{CrCl} = (140-70) \times 75/(72 \times 1.697) = 5{,}250/122.2 \approx 43$ mL/min. (SI shortcut: $1.23 \times 70 \times 75/150 \approx 43$.)

</details>

6. A drug has a half-life of 12 hours. Roughly how long until it reaches steady state without a loading dose? What fraction of steady state is reached after 36 hours?

<details>
<summary>Answer</summary>

4 to 5 half-lives: about 48 to 60 hours. 36 hours is 3 half-lives: $1 - (1/2)^3 = 87.5\%$.

</details>

7. An illustrative drug has $V_d = 40$ L and oral bioavailability $F = 0.5$. What oral loading dose reaches a target concentration of 2 mg/L?

<details>
<summary>Answer</summary>

$\text{LD} = V_d \times C_t / F = 40 \times 2/0.5 = 160$ mg.

</details>

8. A renally cleared drug's clearance halves because of kidney disease. What happens to (a) the maintenance dose needed for the same steady-state level, (b) the loading dose, (c) the half-life?

<details>
<summary>Answer</summary>

(a) Halves, since $\text{MD rate} = CL \times C_{ss}/F$. (b) Unchanged, since $\text{LD} = V_d \times C_t/F$ does not involve $CL$. (c) Doubles, since $t_{1/2} = 0.693\,V_d/CL$. Steady state takes twice as long.

</details>

## Further reading

- Cockcroft, D. W. & Gault, M. H. (1976). Prediction of creatinine clearance from serum creatinine. *Nephron*, 16(1), 31–41.
- Schwartz, G. J. et al. (2009). New equations to estimate GFR in children with CKD. *Journal of the American Society of Nephrology*, 20(3), 629–637.
- Mosteller, R. D. (1987). Simplified calculation of body-surface area. *New England Journal of Medicine*, 317(17), 1098.
- Du Bois, D. & Du Bois, E. F. (1916). A formula to estimate the approximate surface area if height and weight be known. *Archives of Internal Medicine*, 17, 863–871.
- Devine, B. J. (1974). Gentamicin therapy. *Drug Intelligence and Clinical Pharmacy*, 8, 650–655.
- Janmahasatian, S. et al. (2005). Quantification of lean bodyweight. *Clinical Pharmacokinetics*, 44(10), 1051–1065.
- Rowland, M. & Tozer, T. N. *Clinical Pharmacokinetics and Pharmacodynamics: Concepts and Applications.* Lippincott Williams & Wilkins. The standard text for Vd, clearance and half-life.
- Advanced Life Support Group. *Advanced Paediatric Life Support: A Practical Approach to Emergencies.* Wiley-Blackwell.
- Joint Formulary Committee. *BNF for Children.* For drug-specific doses, dosing weights and renal adjustments.
