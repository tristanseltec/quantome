+++
summary = "Estimate energy and protein needs with standard equations, count the calories in dextrose, lipid and feeds, derive and use the glucose infusion rate, compute nitrogen balance, and recognise refeeding risk."
+++

# Nutrition, Energy and Parenteral Calculations

A patient who is "nil by mouth" on a bag of 5% dextrose is being given water, sugar and not much else. How many calories is that? Is it enough? If the patient later needs parenteral nutrition (PN), how do you check that the bag the pharmacy sends matches the dietitian's target, and that the glucose is not running faster than the body can use it? And why does feeding a starved patient too fast sometimes kill them?

These are arithmetic questions sitting on top of physiology. This chapter gives the arithmetic: energy equations and their limits, the energy density of each macronutrient, calories from dextrose and lipid, the **glucose infusion rate** (GIR) derived from first principles, nitrogen balance, and the arithmetic side of refeeding syndrome. It ends with a small calculator for PN and enteral feeds.

> [!CAUTION]
> Worked examples teach arithmetic, not prescribing. Nutrition support is planned with a dietitian and a nutrition pharmacist, and PN is compounded to a validated prescription. Always check targets, products and rates against the current local formulary, product data sheets and guidelines (for example NICE CG32, ESPEN or ASPEN guidance, or your hospital's nutrition protocol), and have calculations independently double-checked. Neonatal and paediatric PN follow specialist protocols.

This chapter uses concentration arithmetic from [units, concentrations and conversions](../../clinical-mathematics/units-concentrations-and-conversions/), the different body weights from [weight and body-size based dosing](../../clinical-mathematics/weight-and-body-size-based-dosing/), and the maintenance-fluid ideas of [Holliday–Segar](../../clinical-mathematics/maintenance-fluids-holliday-segar/).

## Key ideas

### Energy: what an equation predicts

The body's daily energy expenditure has three parts: **resting energy expenditure** (REE, close to the basal metabolic rate, the energy to stay alive at rest), the **thermic effect of food**, and **activity**. Illness adds or subtracts: fever, sepsis, burns and healing raise expenditure, while sedation and paralysis lower it.

The gold standard for measuring expenditure in a patient is **indirect calorimetry** (measuring oxygen consumed and carbon dioxide produced). Because it is not always available, we use **predictive equations** fitted by regression to measurements in groups of people. They predict an *average* for people like the patient, and individuals scatter around it, often by 10% or more.

### Mifflin–St Jeor (adults)

Mifflin, St Jeor and colleagues (1990) fitted REE to weight $W$ (kg), height $H$ (cm) and age $A$ (years) in healthy adults, including people with obesity:

> [!IMPORTANT]
> **Mifflin–St Jeor** (kcal/day):
> $$\text{REE} = 10\,W + 6.25\,H - 5\,A + s, \qquad s = +5 \text{ (men)}, \; s = -161 \text{ (women)}$$

Read the coefficients as rates: each extra kilogram adds 10 kcal/day, each extra centimetre 6.25 kcal/day, and each year of age removes 5 kcal/day. The sex term shifts the whole line by $5 - (-161) = 166$ kcal/day. A systematic review by Frankenfield and colleagues (2005) found it the most accurate of the common equations in healthy non-obese and obese adults. It was not built for children or for the critically ill.

### Harris–Benedict (historical)

The **Harris–Benedict** equations (Harris and Benedict, 1918–1919) were the standard for most of the twentieth century and you will still meet them in older protocols and software. The original coefficients, as usually quoted:

$$
\begin{aligned}
\text{men: } & 66.5 + 13.75\,W + 5.003\,H - 6.755\,A \\
\text{women: } & 655.1 + 9.563\,W + 1.850\,H - 4.676\,A
\end{aligned}
$$

They were fitted to a small group of mostly young, lean volunteers a century ago, and tend to overestimate REE in modern populations. Treat them as history and as a cross-check.

### Schofield (children and adults)

**Schofield (1985)** pooled a large international set of basal metabolic rate measurements and fitted separate linear equations for each sex and age band (from infancy through to older adulthood), some using weight alone and some weight and height. These are the equations UK paediatric dietitians most often use for children, and many adult protocols use them too. Because each band has its own coefficients, look them up in the original paper or your dietetic handbook rather than from memory. This chapter does not reproduce them.

### Simple weight-based rules, and the factors on top

At the bedside, adult targets are often set per kilogram. NICE CG32 suggests that nutrition support for people who are not severely ill or injured, and not at risk of refeeding syndrome, should provide **25–35 kcal/kg/day** of total energy, including energy from protein. Many teams use 25–30 kcal/kg/day as a first estimate.

Predictive equations give *resting* expenditure, so dietitians multiply by an **activity factor** and sometimes a **stress factor** for illness. Published factor tables vary between sources and are themselves estimates; they are a matter for the dietitian's handbook, not memory. In this chapter, any factor in a worked example is labelled *illustrative*.

Two rules always apply: per-kg rules applied to **actual weight in obesity** overestimate needs, so guidelines specify an ideal or adjusted weight for those patients; and in the critically ill, early full feeding is not necessarily better, and current ICU guidance builds up gradually.

### Protein and nitrogen

NICE CG32 gives a general adult range of **0.8–1.5 g protein/kg/day** for nutrition support. Higher amounts are used in some critical illness, burns and wound healing, and targets in kidney disease depend on whether the patient is on dialysis. Ask the renal or ICU dietitian.

Proteins are on average about 16% nitrogen by mass, so

$$
\text{nitrogen (g)} = \frac{\text{protein (g)}}{6.25}, \qquad \text{because } \frac{1}{0.16} = 6.25 .
$$

The CG32 range is therefore $0.8/6.25 \approx 0.13$ to $1.5/6.25 = 0.24$ g nitrogen/kg/day.

**Nitrogen balance** compares nitrogen in with nitrogen out. Most nitrogen leaves as urinary urea. One urea molecule, $\text{CO(NH}_2)_2$, carries two nitrogen atoms ($2 \times 14 = 28$ g per mol), so in SI units:

$$
\text{urinary urea nitrogen (g/day)} = \text{urine urea (mmol/day)} \times 0.028 .
$$

A classical approximation adds about 4 g/day for nitrogen lost in other ways (faeces, skin, non-urea urinary nitrogen):

> [!IMPORTANT]
> **Nitrogen balance** (g/day) $\approx \dfrac{\text{protein intake (g)}}{6.25} - \left(\text{urine urea (mmol/24 h)} \times 0.028 + 4\right)$.
> Negative means net protein breakdown.

It needs a complete 24-hour urine collection and is unreliable when kidney function is impaired or changing, when urea is being removed by dialysis, or when there are large losses from wounds, burns or fistulae.

### Energy density of each macronutrient

| Substance | Energy | Notes |
|---|---|---|
| Carbohydrate (food) | 4 kcal/g | Atwater factor |
| Protein / amino acids | 4 kcal/g | Atwater factor |
| Fat (food) | 9 kcal/g | Atwater factor |
| Alcohol | 7 kcal/g | worth knowing for history-taking |
| IV dextrose (glucose monohydrate) | 3.4 kcal/g | see below |
| 20% lipid emulsion | about 2 kcal/mL | approximate; includes glycerol and phospholipid; check the data sheet |

**Why 3.4 for dextrose?** IV dextrose is often expressed as glucose *monohydrate*, $\text{C}_6\text{H}_{12}\text{O}_6 \cdot \text{H}_2\text{O}$, molar mass about 198.2 g/mol, against 180.2 g/mol for anhydrous glucose. Only $180.2/198.2 \approx 0.909$ of each gram is glucose. Anhydrous glucose yields about 3.75 kcal/g, and $0.909 \times 3.75 \approx 3.4$ kcal/g.

> [!NOTE]
> Read the label. Some products state the percentage as glucose monohydrate (US D5W contains 5 g dextrose monohydrate per 100 mL). Others state it as anhydrous glucose; for example UK "Glucose 5%" bags typically state 50 g/L anhydrous glucose, present as about 55 g/L of monohydrate. For that UK bag the energy comes out the same whichever way you count it, because $55 \times 3.4 \approx 50 \times 3.75 \approx 187$ kcal/L. A US D5W bag, by contrast, holds 50 g of *monohydrate* per litre: $50 \times 3.4 = 170$ kcal/L, about 10% less. UK data sheets usually quote about 200 kcal/L for glucose 5%, because they count 50 g of anhydrous glucose at 4 kcal/g. These figures (170, 187, 200 kcal/L) differ only by convention; the mistake to avoid is mixing a mass stated one way with an energy factor meant for the other. In this chapter "$d\%$ dextrose" means $d$ g per 100 mL at 3.4 kcal/g.

**Calories from a dextrose infusion.** A $d\%$ solution contains $d$ g per 100 mL, i.e. $d/100$ g/mL. At $r$ mL/h for 24 hours:

$$
\text{kcal/day} = r \times 24 \times \frac{d}{100} \times 3.4 .
$$

A 70 kg adult on 5% dextrose at 100 mL/h receives $100 \times 24 \times 0.05 = 120$ g, i.e. $120 \times 3.4 = 408$ kcal/day: about a fifth of what they need. Maintenance dextrose prevents ketosis and hypoglycaemia; it is not nutrition.

### The glucose infusion rate (GIR)

Glucose is used, and tolerated, in proportion to body size and time, so we express the dose as **mg of glucose per kg per minute**. Derive it with dimensional analysis:

$$
\underbrace{\frac{d \text{ g}}{100 \text{ mL}}}_{\text{concentration}} \times \frac{1000 \text{ mg}}{1 \text{ g}} = 10\,d \;\frac{\text{mg}}{\text{mL}}, \qquad
10\,d \;\frac{\text{mg}}{\text{mL}} \times r\;\frac{\text{mL}}{\text{h}} \times \frac{1 \text{ h}}{60 \text{ min}} \times \frac{1}{w \text{ kg}} .
$$

> [!IMPORTANT]
> **Glucose infusion rate** (mg/kg/min):
> $$\text{GIR} = \frac{d \times r \times 10}{60 \times w} = \frac{d \times r}{6\,w}$$
> where $d$ = dextrose % (g/100 mL), $r$ = rate (mL/h), $w$ = weight (kg).
> From a daily total instead: $\text{GIR} = \dfrac{\text{grams per day} \times 1000}{1440 \times w}$.

The formula can be turned round: to deliver a target GIR, the rate is $r = 6\,w \times \text{GIR} / d$.

**Useful reference points (check local guidance).** Normal hepatic glucose production in term newborns is often quoted at roughly 4–6 mg/kg/min, and neonatal units set GIR targets by protocol. In adults, glucose oxidation is limited, and an upper limit of around 4–5 mg/kg/min is often quoted for PN. Above that, excess glucose drives hyperglycaemia, fat synthesis and extra carbon dioxide production.

### Refeeding syndrome

After a period of starvation, the body has adapted to burning fat and has depleted intracellular phosphate, potassium and magnesium, often with normal blood levels. When carbohydrate arrives, insulin rises and drives these ions (and glucose) into cells. Blood phosphate, potassium and magnesium can fall sharply, and thiamine is used up, causing arrhythmia, heart failure, respiratory failure, confusion and death. The arithmetic response is: **identify the risk, start low, build up slowly, and check electrolytes.**

NICE CG32, summarised (read the guideline for the full wording), regards an adult as at **high risk** with *one* of: BMI below 16 kg/m²; unintentional weight loss above 15% in the previous 3–6 months; little or no nutritional intake for more than 10 days; or low potassium, phosphate or magnesium before feeding. Or with *two* of: BMI below 18.5 kg/m²; unintentional weight loss above 10% in 3–6 months; little or no intake for more than 5 days; or a history of alcohol misuse or of drugs including insulin, chemotherapy, antacids or diuretics.

For high-risk patients CG32 advises starting at **no more than 10 kcal/kg/day**, increasing slowly to meet or exceed full needs over 4–7 days, and in extreme cases (for example BMI below 14 kg/m² or negligible intake for more than 15 days) starting at 5 kcal/kg/day, alongside thiamine and other vitamins and electrolyte replacement as the guideline describes. Children and adolescents, including those with eating disorders, are managed under separate specialist guidance.

## Worked examples

### 1. A term newborn on IV dextrose: GIR and calories

A 3.5 kg term baby is on 10% dextrose at 12 mL/h (rate set by the neonatal protocol; we only check the arithmetic).

- GIR $= \dfrac{10 \times 12}{6 \times 3.5} = \dfrac{120}{21} \approx 5.7$ mg/kg/min.
- Sanity check: within the 4–6 mg/kg/min range often quoted for neonatal glucose production. ✓
- Energy: $12 \times 24 = 288$ mL/day, containing $28.8$ g dextrose, i.e. $28.8 \times 3.4 \approx 98$ kcal/day, about $28$ kcal/kg/day. Far below a growing baby's needs, which is why feeds or PN follow quickly.

### 2. A school-age child on enteral feeds

A 25 kg child is fed by nasogastric tube. The dietitian, using Schofield with a factor, sets a target of 1,500 kcal/day using a 1 kcal/mL feed, run over 20 hours to allow a break.

- Volume: $1500 / 1.0 = 1{,}500$ mL/day.
- Rate: $1500 / 20 = 75$ mL/h.
- Fluid check: Holliday–Segar maintenance at 25 kg is 1,600 mL/day. The feed is mostly, but not entirely, water (the data sheet gives free water), and flushes and medicines add more. Look at the total fluid, not just the feed.

As a curiosity, the Holliday–Segar *energy* curve (100/50/20 kcal/kg/day) gives 1,600 kcal/day at 25 kg, which is in the same region. It was built as an estimate for resting hospitalised children, not as a feeding target.

### 3. An adolescent on maintenance dextrose

A 45 kg adolescent is on maintenance isotonic fluid containing 5% dextrose at 85 mL/h.

- GIR $= \dfrac{5 \times 85}{6 \times 45} \approx 1.57$ mg/kg/min.
- Energy: $85 \times 24 = 2{,}040$ mL contains $102$ g dextrose, $102 \times 3.4 \approx 347$ kcal/day.

Mifflin–St Jeor is not validated below 18 years, so a dietitian would use a paediatric equation such as Schofield. The point is the gap: a few hundred kcal against needs of well over a thousand. A few days of this is acceptable; a week is not.

### 4. An adult: three estimates and nitrogen balance

A 40-year-old man, 70 kg, 175 cm.

- **Mifflin–St Jeor:** $10(70) + 6.25(175) - 5(40) + 5 = 700 + 1093.75 - 200 + 5 = 1{,}598.75 \approx 1{,}600$ kcal/day (resting).
- **Harris–Benedict:** $66.5 + 13.75(70) + 5.003(175) - 6.755(40) = 66.5 + 962.5 + 875.5 - 270.2 \approx 1{,}634$ kcal/day.
- **With an illustrative factor of 1.2:** $1598.75 \times 1.2 \approx 1{,}919$ kcal/day.
- **Simple rule:** 25–30 kcal/kg/day gives 1,750–2,100 kcal/day.

The estimates cluster around 1,600–2,100 kcal/day: the highest is about 30% above the lowest, which is a realistic picture of their precision.

**Protein:** 0.8–1.5 g/kg/day gives 56–105 g/day, which is $56/6.25 \approx 9.0$ to $105/6.25 = 16.8$ g nitrogen.

**Nitrogen balance.** He takes 70 g protein a day, and his 24-hour urine contains 300 mmol urea.

- N in $= 70/6.25 = 11.2$ g.
- N out $\approx 300 \times 0.028 + 4 = 8.4 + 4 = 12.4$ g.
- Balance $\approx 11.2 - 12.4 = -1.2$ g/day. Mildly catabolic.

### 5. An older adult with renal impairment

A 78-year-old woman, 60 kg, 160 cm, with chronic kidney disease.

- **Mifflin–St Jeor:** $600 + 1000 - 390 - 161 = 1{,}049$ kcal/day (resting).
- **Harris–Benedict (women):** $655.1 + 9.563(60) + 1.850(160) - 4.676(78) \approx 1{,}160$ kcal/day.
- **Simple rule:** 25–30 kcal/kg/day gives 1,500–1,800 kcal/day.

Now the methods disagree by more: the equations give *resting* expenditure and the per-kg rule a *total*. That is a reason to involve a dietitian, not to average the numbers. Do not use nitrogen balance here: with impaired kidney function, urine urea no longer reflects protein breakdown. Protein targets depend on her renal status and treatment.

### 6. An obese adult

A 50-year-old man, 120 kg, 170 cm (BMI $= 120/1.70^2 \approx 41.5$ kg/m²).

- **Mifflin–St Jeor** (built including people with obesity, uses actual weight): $1200 + 1062.5 - 250 + 5 = 2{,}017.5$ kcal/day.
- **25 kcal/kg on actual weight:** $3{,}000$ kcal/day. Too high: adipose tissue uses less energy per kg than lean tissue.
- **Using adjusted body weight** (IBW 65.9 kg from the Devine formula; ABW $= 65.9 + 0.4(120 - 65.9) \approx 87.6$ kg): $25 \times 87.6 \approx 2{,}189$ kcal/day.

Different guidelines specify different weights for obese patients (actual, ideal or adjusted), especially in critical care, so state which weight you used.

### 7. An adult PN bag, checked from its components

A 65 kg adult needs about 25 kcal/kg/day total ($1{,}625$ kcal) and 1.2 g/kg/day protein ($78$ g). The proposed 24-hour bag is: 50% dextrose 478 mL, 10% amino acids 780 mL, 20% lipid 250 mL.

- Dextrose: $0.50 \times 478 = 239$ g, $\times 3.4 \approx 813$ kcal.
- Amino acids: $0.10 \times 780 = 78$ g protein, $\times 4 = 312$ kcal; nitrogen $78/6.25 = 12.48$ g.
- Lipid: $250 \times 2 \approx 500$ kcal.
- Total $\approx 1{,}625$ kcal ($25$ kcal/kg), of which non-protein $\approx 1{,}313$ kcal. Volume $1{,}508$ mL.
- GIR $= 239 \times 1000 / (1440 \times 65) \approx 2.55$ mg/kg/min, comfortably below the 4–5 mg/kg/min often quoted as an adult upper limit.

Note whether a target is "total" or "non-protein" kcal. Here the total meets 25 kcal/kg, but the non-protein energy is only about 20 kcal/kg.

### 8. A refeeding-risk adult

A 24-year-old woman, 160 cm, 39 kg, has eaten almost nothing for 12 days.

- BMI $= 39 / 1.60^2 \approx 15.2$ kg/m², below 16. That alone, and also 12 days of little intake, places her at high risk.
- Start at no more than $10 \times 39 = 390$ kcal/day, then build up over 4–7 days, with electrolytes (phosphate, potassium, magnesium) checked and replaced and thiamine given, as CG32 describes.

## Sanity checks and common errors

- **Units of the rate.** GIR is per **minute**; pumps run per **hour**. Forgetting the 60 makes the GIR 60 times too large.
- **Percent means g/100 mL.** 10% dextrose is 100 g/L, not 10 g/L.
- **Dextrose is not 4 kcal/g.** Use 3.4 for the monohydrate; know which form your label states.
- **Lipid volume is not lipid mass.** 250 mL of 20% emulsion contains 50 g fat. Use the per-mL energy from the data sheet (about 2 kcal/mL for 20%), not 9 kcal/g on 250 g.
- **Hidden calories.** Propofol is given in a lipid emulsion, and dextrose in drug infusions adds up. Count them.
- **Resting vs total.** Equations predict REE. Don't compare them directly with per-kg totals without a factor.
- **Which weight?** Actual, ideal or adjusted changes the answer by a third or more in obesity.
- **Refeeding.** In a malnourished patient, "full needs from day 1" is the error. The safe answer is lower, not higher.

## In code

The calculator below sums the energy, protein and nitrogen in a PN regimen from its components, computes the GIR, and flags values outside common limits. It also includes Mifflin–St Jeor (refusing ages it was not built for) and a refeeding starting-energy helper.

```python
KCAL_PER_G = {"dextrose": 3.4, "amino_acid": 4.0}   # dextrose monohydrate, protein
KCAL_PER_ML_LIPID_20 = 2.0                          # approximate; check the product data sheet

def mifflin_st_jeor(weight_kg, height_cm, age_y, sex):
    if not (30 <= weight_kg <= 300 and 120 <= height_cm <= 230 and 18 <= age_y <= 110):
        raise ValueError("outside the adult range the equation was built for")
    return 10 * weight_kg + 6.25 * height_cm - 5 * age_y + (5 if sex == "M" else -161)

def gir(dextrose_percent, rate_ml_h, weight_kg):
    """Glucose infusion rate in mg/kg/min."""
    return dextrose_percent * rate_ml_h * 10 / (60 * weight_kg)

def pn_summary(weight_kg, dextrose=(0, 0), amino=(0, 0), lipid20_ml=0, hours=24):
    """dextrose and amino are (percent w/v, mL per bag); lipid20_ml is mL of 20% emulsion."""
    if not 0.5 <= weight_kg <= 300:
        raise ValueError(f"implausible weight {weight_kg} kg")
    dex_g = dextrose[0] / 100 * dextrose[1]
    prot_g = amino[0] / 100 * amino[1]
    kcal = {"dextrose": dex_g * KCAL_PER_G["dextrose"],
            "protein": prot_g * KCAL_PER_G["amino_acid"],
            "lipid": lipid20_ml * KCAL_PER_ML_LIPID_20}
    total = sum(kcal.values())
    out = {"volume_mL": dextrose[1] + amino[1] + lipid20_ml,
           "kcal_total": total, "kcal_non_protein": total - kcal["protein"],
           "kcal_per_kg": total / weight_kg, "protein_g_per_kg": prot_g / weight_kg,
           "nitrogen_g": prot_g / 6.25,
           "GIR_mg_kg_min": dex_g * 1000 / (hours * 60) / weight_kg}
    flags = []
    if out["GIR_mg_kg_min"] > 5:
        flags.append("GIR above about 5 mg/kg/min: check against local limits")
    if out["kcal_per_kg"] > 35:
        flags.append("energy above 35 kcal/kg/day: check target and weight used")
    return out, flags

def refeeding_start_kcal(weight_kg, kcal_per_kg=10):
    """NICE CG32: high-risk patients start at no more than 10 kcal/kg/day (5 in extreme cases)."""
    return kcal_per_kg * weight_kg

print("Mifflin, M 70 kg 175 cm 40 y:", mifflin_st_jeor(70, 175, 40, "M"), "kcal/day")
print("GIR, 3.5 kg on 10% at 12 mL/h:", round(gir(10, 12, 3.5), 2), "mg/kg/min")
print("GIR, 70 kg on 5% at 100 mL/h:", round(gir(5, 100, 70), 2), "mg/kg/min")
bag, flags = pn_summary(65, dextrose=(50, 478), amino=(10, 780), lipid20_ml=250)
for k, v in bag.items():
    print(f"  {k:<18}{v:8.2f}")
print("  flags:", flags or "none")
print("Refeeding start, 39 kg:", refeeding_start_kcal(39), "kcal/day")
try:
    mifflin_st_jeor(45, 160, 15, "F")
except ValueError as e:
    print("refused:", e)
```

Output:

```text
Mifflin, M 70 kg 175 cm 40 y: 1598.75 kcal/day
GIR, 3.5 kg on 10% at 12 mL/h: 5.71 mg/kg/min
GIR, 70 kg on 5% at 100 mL/h: 1.19 mg/kg/min
  volume_mL          1508.00
  kcal_total         1624.60
  kcal_non_protein   1312.60
  kcal_per_kg          24.99
  protein_g_per_kg      1.20
  nitrogen_g           12.48
  GIR_mg_kg_min         2.55
  flags: none
Refeeding start, 39 kg: 390 kcal/day
refused: outside the adult range the equation was built for
```

The output reproduces worked examples 1, 4, 7 and 8. Two extensions are natural: add an enteral feed as another component (kcal/mL and protein per 100 mL from its data sheet), and print a day-by-day build-up schedule for refeeding risk. Turning such helpers into printed charts safely is the subject of [building your own clinical scales](../../clinical-mathematics/building-your-own-clinical-scales/).

## Practice

1. Use Mifflin–St Jeor to estimate the REE of a 30-year-old woman, 65 kg, 165 cm.

<details>
<summary>Answer</summary>

$10(65) + 6.25(165) - 5(30) - 161 = 650 + 1031.25 - 150 - 161 = 1{,}370.25 \approx 1{,}370$ kcal/day.

</details>

2. A 5 kg infant is on 10% dextrose at 25 mL/h. What is the GIR?

<details>
<summary>Answer</summary>

$\text{GIR} = \dfrac{10 \times 25}{6 \times 5} = \dfrac{250}{30} \approx 8.3$ mg/kg/min.

</details>

3. How many kcal are in 1 L of 10% dextrose (expressed as monohydrate)?

<details>
<summary>Answer</summary>

$100$ g $\times 3.4$ kcal/g $= 340$ kcal.

</details>

4. A patient receives 90 g protein per day. The 24-hour urine urea is 450 mmol. Estimate the nitrogen balance.

<details>
<summary>Answer</summary>

N in $= 90/6.25 = 14.4$ g. N out $\approx 450 \times 0.028 + 4 = 12.6 + 4 = 16.6$ g. Balance $\approx 14.4 - 16.6 = -2.2$ g/day (catabolic).

</details>

5. A 4 kg infant on 10% dextrose needs a GIR of 6 mg/kg/min. Rearrange the GIR formula to find the rate in mL/h.

<details>
<summary>Answer</summary>

$r = \dfrac{6\,w \times \text{GIR}}{d} = \dfrac{6 \times 4 \times 6}{10} = 14.4$ mL/h.

</details>

6. An adult weighing 52 kg has a BMI of 17.5 kg/m², a history of alcohol misuse, and has eaten little for 7 days. Is she at high risk of refeeding syndrome by the NICE CG32 criteria, and what is the maximum starting energy?

<details>
<summary>Answer</summary>

None of the single criteria applies (BMI is not below 16, intake has not been poor for more than 10 days). But she has two of the second list: BMI below 18.5, little intake for more than 5 days, and alcohol misuse (three, in fact). So she is high risk. Start at no more than $10 \times 52 = 520$ kcal/day and build up over 4–7 days with electrolyte monitoring.

</details>

7. An adult's target is 1,800 kcal/day from a 1.5 kcal/mL enteral feed given over 18 hours. What volume and rate?

<details>
<summary>Answer</summary>

Volume $= 1800 / 1.5 = 1{,}200$ mL. Rate $= 1200 / 18 \approx 66.7$ mL/h.

</details>

## Further reading

- Mifflin, M. D., St Jeor, S. T., Hill, L. A., Scott, B. J., Daugherty, S. A. & Koh, Y. O. (1990). A new predictive equation for resting energy expenditure in healthy individuals. *American Journal of Clinical Nutrition*, 51(2), 241–247.
- Harris, J. A. & Benedict, F. G. (1918). A biometric study of human basal metabolism. *Proceedings of the National Academy of Sciences*, 4(12), 370–373.
- Schofield, W. N. (1985). Predicting basal metabolic rate, new standards and review of previous work. *Human Nutrition: Clinical Nutrition*, 39 Suppl 1, 5–41.
- Frankenfield, D., Roth-Yousey, L. & Compher, C. (2005). Comparison of predictive equations for resting metabolic rate in healthy nonobese and obese adults: a systematic review. *Journal of the American Dietetic Association*, 105(5), 775–789.
- NICE clinical guideline CG32. *Nutrition support for adults: oral nutrition support, enteral tube feeding and parenteral nutrition.* National Institute for Health and Care Excellence (2006, updated 2017).
