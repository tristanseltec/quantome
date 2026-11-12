+++
summary = "Calculate feed volumes, energy, protein, glucose infusion rate and growth velocity for term and preterm infants, and plan the switch from parenteral to enteral feeding."
+++

# Infant & Neonatal Nutrition Calculations

The [previous chapter](../nutrition-energy-and-parenteral-calculations/) introduced energy equations, macronutrient energy densities and the glucose infusion rate (GIR) for patients of all ages. This chapter zooms in on the group where the arithmetic matters most and the margins are smallest: **infants**, and especially **newborn and preterm babies**.

A 1.2 kg preterm baby has almost no stored fat and very little glycogen. Their requirements per kilogram are several times an adult's, and a 1 mL/h pump error is close to 20 mL/kg/day. Small mistakes in units, concentration or weight quickly become clinically significant.

> [!CAUTION]
> This chapter teaches **calculation**, not prescribing. Neonatal and infant nutrition is protocol-driven and specialist-led. Target ranges differ between guidelines, units and patients, and they change as evidence evolves. Always use your unit's current neonatal or paediatric nutrition protocol, involve the neonatal dietitian and pharmacist, and have parenteral nutrition (PN) prescriptions independently checked. All target ranges below are given **for illustration and arithmetic practice**. Confirm them against the sources in *Further reading* and your local guidance before any clinical use.

## Why infants are different

| Feature | Consequence for the calculation |
|---|---|
| Very high energy and protein needs **per kg** (growth is fast) | Small absolute volumes must carry a lot of nutrition |
| Tiny reserves: little fat, glycogen lasting hours rather than days | Interruptions to feeds or infusions matter quickly; hypoglycaemia risk |
| High body water, immature kidneys, large insensible losses (especially preterm skin) | Fluid volume is set by day of life and maturity, and nutrition must fit *inside* that volume |
| Weight changes daily, and drops after birth | You must state **which weight** you are using (birth weight vs current weight) |
| Stomach capacity and gut immaturity | Enteral feeds are introduced and advanced gradually, so PN often bridges the gap |

The central tension of neonatal nutrition is that **fluid volume is limited, but nutrient needs are high**. Almost every calculation in this chapter is about fitting enough energy, protein and glucose into a fixed volume.

## Key ideas

### Which weight?

- Newborns normally lose some weight in the first days of life, and usually regain their birth weight within about the first two weeks.
- Many neonatal protocols calculate on **birth weight** until birth weight is regained, then on **current (working) weight**, updated at set intervals.
- Whatever your unit does, write the weight and its date on every calculation. Using yesterday's weight, or the wrong baby's, is a classic error.

### Feeds: from mL/kg/day to mL per feed

Enteral feeds are prescribed in **mL/kg/day** and given as a number of feeds per day (e.g. 8 three-hourly feeds, or 12 two-hourly feeds for small preterm infants):

> [!IMPORTANT]
> $$\text{volume per feed (mL)} = \frac{\text{mL/kg/day} \times \text{weight (kg)}}{\text{feeds per day}}$$

Dimensional check: $\dfrac{\text{mL}}{\text{kg}\cdot\text{day}} \times \text{kg} \div \dfrac{\text{feeds}}{\text{day}} = \dfrac{\text{mL}}{\text{feed}}$ ✓

### Energy and protein from milk

Milk composition is quoted **per 100 mL**, so:

> [!IMPORTANT]
> $$\text{energy (kcal/kg/day)} = \text{volume (mL/kg/day)} \times \frac{\text{kcal per 100 mL}}{100}$$
> $$\text{protein (g/kg/day)} = \text{volume (mL/kg/day)} \times \frac{\text{g protein per 100 mL}}{100}$$

Typical approximate values (always use the actual product's label or your dietitian's reference):

| Feed | Energy (kcal/100 mL) | Protein (g/100 mL) |
|---|---|---|
| Mature human (breast) milk | about 65–70 (varies widely between mothers and through a feed) | about 0.9–1.2 |
| Standard term infant formula | about 60–70 (the EU legal range for infant formula) | about 1.2–1.4 |
| Preterm formula | about 80 | about 2.6–3.0 |
| Breast milk + fortifier | depends on the product and its strength | depends on the product |

> [!NOTE]
> Expressed breast milk varies a lot. Hindmilk is richer in fat than foremilk, and fat can stick to tubing during slow infusions. Calculations based on "67 kcal/100 mL" are estimates, so **growth** is the real test of adequacy.

### Parenteral nutrition: three components

Neonatal PN is usually given as two infusions:

1. an **aqueous** solution containing dextrose, amino acids, electrolytes, minerals and trace elements
2. a **lipid emulsion**, often 20%, with vitamins

For each component, convert volume into mass, then mass into energy:

> [!IMPORTANT]
> $$\text{dextrose (g/day)} = \text{mL/day} \times \frac{\text{dextrose \%}}{100}, \qquad \text{energy} \approx 3.4\ \text{kcal/g}$$
> $$\text{amino acids (g/day)} = \text{mL/day} \times \frac{\text{amino acid \%}}{100}, \qquad \text{energy} \approx 4\ \text{kcal/g}$$
> $$\text{lipid (g/day)} = \text{mL/day of 20\% emulsion} \times 0.2, \qquad \text{energy of 20\% emulsion} \approx 2\ \text{kcal/mL}$$

The 20% emulsion provides about 2 kcal/mL, that is about 10 kcal per gram of fat, rather than the 9 kcal/g of pure fat. The extra comes from the glycerol and phospholipid in the emulsion. See the [previous chapter](../nutrition-energy-and-parenteral-calculations/) for the dextrose 3.4 vs 3.75 kcal/g conventions.

### The glucose infusion rate, revisited

> [!IMPORTANT]
> $$\text{GIR (mg/kg/min)} = \frac{\text{dextrose \%} \times \text{rate (mL/h)} \times 10}{60 \times \text{weight (kg)}}$$

Derivation in one line: $d\%$ means $d$ g per 100 mL, which is $10d$ mg/mL. Multiplying by the rate in mL/h gives mg/h; dividing by 60 gives mg/min, and dividing by weight gives mg/kg/min.

Two handy rearrangements:

$$\text{dextrose \% needed} = \frac{\text{GIR} \times 60 \times \text{weight}}{\text{rate} \times 10} \qquad \text{rate needed (mL/h)} = \frac{\text{GIR} \times 60 \times \text{weight}}{\text{dextrose \%} \times 10}$$

Converting from g/kg/day, which some protocols use: $1\ \text{g/kg/day} = \dfrac{1000\ \text{mg}}{1440\ \text{min}} \approx 0.694\ \text{mg/kg/min}$.

**Orientation values.** The ESPGHAN/ESPEN/ESPR/CSPEN 2018 paediatric PN guideline (carbohydrate chapter) suggests the following. Verify them against the source and your protocol:

| | Day 1 GIR (mg/kg/min) | From day 2: target (mg/kg/min) | Upper limit |
|---|---|---|---|
| Preterm newborn | 4–8 | 8–10 | about 12 |
| Term newborn | 2.5–5 | 5–10 | about 12 |

The GIR is then adjusted to blood glucose: up for hypoglycaemia, down for hyperglycaemia. Very high GIRs promote lipogenesis and hyperglycaemia.

### Protein and energy targets: orientation only

These are broad ranges from major European guidance (ESPGHAN 2018 for PN; ESPGHAN 2022 for enteral feeding of preterm infants). Your unit's protocol is the authority.

| | Preterm infant | Term infant |
|---|---|---|
| PN amino acids | at least 1.5 g/kg/day from day 1; then about 2.5–3.5 g/kg/day | about 1.5–3 g/kg/day |
| PN lipid | usually started early, built up, generally not above 4 g/kg/day | generally not above 4 g/kg/day |
| PN energy (stable, growing phase) | about 90–120 kcal/kg/day | lower than on full enteral feeds; depends on phase of illness |
| Full enteral energy | about 115–140 kcal/kg/day (more if growth is poor, but not above 160) | about 100–120 kcal/kg/day in early infancy |
| Full enteral protein | at least 3.5–4.0 g/kg/day (up to 4.5 if growth is slow) | met by breast milk or standard formula at normal volumes |

> [!WARNING]
> **PN needs less energy than enteral feeding** for the same growth, because there are no losses from digestion and absorption. Don't "correct" a PN regimen up to enteral energy targets.

### Expected growth

Growth is the outcome measure that tells you whether your calculations are working.

- **Preterm infants:** weight gain is usually expressed in **g/kg/day**. A frequently used target is about 15–20 g/kg/day, roughly the fetal growth rate.
- **Term infants:** weight gain in early infancy is often around 25–35 g/day. Plot on growth charts (WHO-based in many countries) rather than relying on single numbers. See [Growth & BMI in children](../growth-and-bmi-in-children/).

Because babies grow roughly exponentially, the most accurate way to calculate growth velocity is the **exponential method** (Patel et al., 2005):

> [!IMPORTANT]
> $$\text{GV (g/kg/day)} = \frac{1000 \times \ln(W_n / W_1)}{D_n - D_1}$$

Here $W$ is weight in grams and $D$ is day of life. The simpler "average-weight" method gives

$$\frac{(W_n - W_1)/(D_n - D_1)}{\tfrac12 (W_1 + W_n)/1000}$$

which agrees closely over short intervals. Over long intervals, using the birth weight alone as the denominator overestimates velocity.

### Catch-up growth

For an infant with faltering growth, a classic estimate of the energy needed for catch-up growth is:

> [!IMPORTANT]
> $$\text{kcal/kg/day} = \frac{\text{requirement for weight-age (kcal/kg/day)} \times \text{ideal weight for length (kg)}}{\text{actual weight (kg)}}$$

The same structure works for protein. *Weight-age* is the age at which the infant's current weight sits on the 50th centile, and *ideal weight for length* is the 50th-centile weight for the infant's current length. Methods vary, so treat this as a starting estimate that dietetic review refines.

## Worked examples

### 1. Term baby, formula-fed (3.5 kg, day 5)

The plan is 150 mL/kg/day of standard formula (67 kcal and 1.3 g protein per 100 mL, as on the label), given as 8 feeds a day.

- Daily volume: $150 \times 3.5 = 525$ mL/day.
- Per feed: $525 / 8 = 65.6$ mL. In practice this is rounded to a measurable volume, e.g. 65 mL.
- Energy: $150 \times 0.67 = 100.5$ kcal/kg/day.
- Protein: $150 \times 0.013 = 1.95$ g/kg/day.

Sanity check: about 100 kcal/kg/day is in the expected range for a well term baby. A breastfed baby on demand isn't "prescribed" volumes at all; you judge adequacy by output, weight and clinical review.

### 2. Preterm baby on PN only (1.2 kg, day 3)

The total fluid allowance is 120 mL/kg/day: $120 \times 1.2 = 144$ mL/day. The plan is lipid 3 g/kg/day and amino acids 3 g/kg/day, with 10% dextrose in the aqueous bag.

1. **Lipid volume first:** $3 \times 1.2 = 3.6$ g/day. A 20% emulsion holds 0.2 g/mL, so $3.6 / 0.2 = 18$ mL/day, which is **0.75 mL/h**.
2. **Aqueous volume** is the remainder: $144 - 18 = 126$ mL/day, which is **5.25 mL/h**.
3. **Amino acid concentration needed:** $3.6\ \text{g} / 126\ \text{mL} = 2.86$ g per 100 mL, i.e. 2.86%.
4. **GIR:** $\dfrac{10 \times 5.25 \times 10}{60 \times 1.2} = 7.29$ mg/kg/min. This is within the illustrative preterm range.
5. **Energy:**
   - dextrose $126 \times 0.10 \times 3.4 = 42.8$ kcal
   - amino acids $3.6 \times 4 = 14.4$ kcal
   - lipid $18 \times 2 = 36$ kcal

   The total is 93.2 kcal/day, or **77.7 kcal/kg/day**.

At 77.7 kcal/kg/day this baby is still building up. As fluid allowance rises over the next days, the same method gives more energy. Notice that **lipid volume is calculated first**, because it is set in g/kg; the aqueous bag fills the rest of the fluid allowance.

> [!WARNING]
> Don't forget the **other infusions**: drug infusions, line-flush fluids and arterial-line fluids also count towards total fluid, and sometimes contribute sodium or glucose. In tiny babies they can be 10–20% of the daily allowance. Most units subtract them before calculating the PN volume.

### 3. Switching from PN to enteral feeds (1.2 kg)

Enteral milk (breast milk, here 67 kcal and 1.2 g protein per 100 mL) is advanced by 30 mL/kg/day. The total fluid stays at 150 mL/kg/day, and the aqueous PN (10% dextrose, 2.86% amino acids) makes up the difference. Lipid stays at 3 g/kg/day until enteral volume reaches 120 mL/kg/day. The calculator below produces this table:

| Enteral (mL/kg/d) | Aqueous PN (mL/h) | Lipid (mL/h) | Energy (kcal/kg/d) | Protein (g/kg/d) | GIR (mg/kg/min) |
|---|---|---|---|---|---|
| 0 | 6.75 | 0.75 | 91.3 | 3.86 | 9.38 |
| 30 | 5.25 | 0.75 | 97.8 | 3.36 | 7.29 |
| 60 | 3.75 | 0.75 | 104.3 | 2.86 | 5.21 |
| 90 | 2.25 | 0.75 | 110.7 | 2.37 | 3.12 |
| 120 | 1.50 | 0 | 94.0 | 2.30 | 2.08 |
| 150 | 0 | 0 | 100.5 | **1.80** | 0 |

Read the table critically:

- **Energy dips** when lipid stops at 120 mL/kg/day (110.7 to 94.0). Units manage this differently, for example by stepping lipid down gradually.
- **Protein falls steadily.** On full *unfortified* breast milk the baby gets only 1.8 g/kg/day, about half the preterm enteral target. This is exactly why **breast-milk fortifiers** exist (example 6).
- **The GIR falls** as dextrose volume falls. Blood glucose has to be watched during the transition, and the enteral feeds must actually be *tolerated* before the PN is reduced.

### 4. Hypoglycaemia: changing the glucose infusion rate (term baby, 3.0 kg)

The baby is on 10% dextrose at 60 mL/kg/day, which is $60 \times 3 / 24 = 7.5$ mL/h.

- Current GIR: $\dfrac{10 \times 7.5 \times 10}{60 \times 3} = 4.17$ mg/kg/min.
- The team wants a GIR of 6 mg/kg/min **without** increasing volume. Required concentration: $\dfrac{6 \times 60 \times 3}{7.5 \times 10} = 14.4\%$.
- Many units restrict **peripheral** dextrose to about 12.5% at most, because concentrated solutions damage veins. 14.4% would therefore need central access.
- The alternative is to keep 12.5% and raise the rate: $\dfrac{6 \times 60 \times 3}{12.5 \times 10} = 8.64$ mL/h, about **69 mL/kg/day**. Is the extra fluid acceptable for this baby?

This is the fluid-versus-glucose trade-off. The arithmetic shows the options clearly, and the clinical team chooses between them.

### 5. Faltering growth (infant aged 6 months, 5.6 kg)

The infant's ideal weight for their current length is 7.0 kg. The dietitian's reference requirement for the weight-age is taken as 100 kcal/kg/day; this number is illustrative, so use your reference.

- Catch-up energy: $\dfrac{100 \times 7.0}{5.6} = 125$ kcal/kg/day.
- Volume of standard formula needed (67 kcal/100 mL): $125 / 0.67 = 186.6$ mL/kg/day. That is a large volume for many infants.
- With an energy-dense infant formula of about 100 kcal/100 mL, used under dietetic supervision: $125 / 1.0 = 125$ mL/kg/day.

> [!WARNING]
> **Never concentrate formula by adding extra powder or reducing water** unless a dietitian has specifically designed and supervised it. Wrong concentrations cause dangerous solute loads, dehydration and electrolyte disturbance. Use licensed energy-dense products or prescribed recipes.

### 6. Fortified breast milk (preterm, 160 mL/kg/day)

Take a fortifier that adds about 15 kcal and 1.1 g protein per 100 mL of breast milk. These values are illustrative; products differ.

- Fortified milk is about $67 + 15 = 82$ kcal/100 mL and $1.2 + 1.1 = 2.3$ g/100 mL.
- At 160 mL/kg/day: energy $160 \times 0.82 = 131.2$ kcal/kg/day, and protein $160 \times 0.023 = 3.68$ g/kg/day.

Compare this with the 1.8 g/kg/day from unfortified milk in example 3. Fortification roughly doubles the protein intake.

### 7. Fluid restriction cuts nutrition (infant with bronchiolitis, 5 kg)

The infant is restricted to two-thirds of the Holliday–Segar maintenance volume ([chapter 04](../maintenance-fluids-holliday-segar/)).

- Maintenance: $100 \times 5 = 500$ mL/day. Two-thirds is **333 mL/day**, or 66.7 mL/kg/day.
- If that is all standard formula: $66.7 \times 0.67 = 44.7$ kcal/kg/day, **less than half** of the usual intake.

Restricting fluid restricts nutrition. That is acceptable for a short illness, but if the restriction lasts days, involve the dietitian. Options include energy-dense feeds and reviewing whether the restriction is still needed.

### 8. Is the preterm baby growing well enough?

Weight was 1,200 g on day 7 and 1,480 g on day 21.

- Exponential method: $\dfrac{1000 \times \ln(1480/1200)}{14} = 14.98$ g/kg/day.
- Average-weight method: 14.93 g/kg/day. Over a two-week interval the two methods agree closely.

About 15 g/kg/day is at the lower edge of the frequently quoted 15–20 g/kg/day. Combined with example 3's protein table, the next step is to review protein intake and fortification.

## Sanity checks and common errors

| Check | Why |
|---|---|
| Write **weight, date and which weight** (birth vs current) on every calculation | Weights change daily in neonates |
| Do the totals add up to the **total fluid allowance**, including drug and line fluids? | Hidden fluids can exceed 10% of intake |
| Calculate **lipid first** (set in g/kg), then the aqueous volume | Otherwise lipid squeezes the aqueous PN unnoticed |
| Is the **GIR** plausible for this baby, and has it changed with the regimen? | GIR falls silently when PN is reduced |
| Does the **dextrose concentration** suit the line (peripheral vs central)? | Concentrated dextrose injures peripheral veins |
| mL/**hour** vs mL/**day**, g/kg/**day** vs mg/kg/**min** | The commonest errors are 24× and 60× slips |
| One decimal place in mL/h, for a 1 kg baby, is 2.4 mL/kg/day | Rounding rules matter at this scale; follow your unit's pump practice |
| **Growth** is the real test | Calculated intake is only an estimate of what is actually absorbed |

> [!CAUTION]
> Preterm infants and malnourished infants can develop **refeeding-type electrolyte problems**, especially low phosphate, when nutrition is advanced quickly. Electrolytes and minerals (sodium, potassium, calcium, phosphate, magnesium) are prescribed and monitored by protocol and are not covered here. Their calculations follow the same mmol/kg/day ↔ mmol/L logic as [chapter 01](../units-concentrations-and-conversions/), but the targets must come from specialist guidance.

## In code

The calculator below summarises any combination of enteral feeds, aqueous PN and lipid. It reports fluid, energy (by source), protein, lipid and GIR per kilogram, and flags values outside target ranges **that you supply** from your local protocol.

```python
"""Infant nutrition calculator: a teaching tool, not a prescribing system."""
import math
from dataclasses import dataclass

DEXTROSE_KCAL_PER_G = 3.4      # dextrose monohydrate convention (see previous chapter)
AMINO_ACID_KCAL_PER_G = 4.0
LIPID_20PCT_KCAL_PER_ML = 2.0  # approximate; includes glycerol and phospholipid


def gir_mg_kg_min(dextrose_pct, rate_ml_h, weight_kg):
    """Glucose infusion rate in mg/kg/min."""
    return dextrose_pct * rate_ml_h * 10 / (60 * weight_kg)


@dataclass
class Regimen:
    weight_kg: float
    enteral_ml_kg_day: float = 0.0
    milk_kcal_per_100ml: float = 67.0
    milk_protein_g_per_100ml: float = 1.3
    aqueous_ml_h: float = 0.0          # PN bag (dextrose + amino acids) or plain dextrose
    dextrose_pct: float = 0.0          # g per 100 mL
    amino_acid_pct: float = 0.0        # g per 100 mL
    lipid20_ml_h: float = 0.0

    def __post_init__(self):
        if not 0.3 <= self.weight_kg <= 15:
            raise ValueError(f"weight {self.weight_kg} kg outside infant range: check units")

    def summary(self):
        w = self.weight_kg
        ent_ml = self.enteral_ml_kg_day * w
        aq_ml = self.aqueous_ml_h * 24
        lip_ml = self.lipid20_ml_h * 24
        kcal = {
            "enteral": ent_ml * self.milk_kcal_per_100ml / 100,
            "dextrose": aq_ml * self.dextrose_pct / 100 * DEXTROSE_KCAL_PER_G,
            "amino acids": aq_ml * self.amino_acid_pct / 100 * AMINO_ACID_KCAL_PER_G,
            "lipid": lip_ml * LIPID_20PCT_KCAL_PER_ML,
        }
        protein_g = ent_ml * self.milk_protein_g_per_100ml / 100 + aq_ml * self.amino_acid_pct / 100
        return {
            "fluid mL/kg/d": (ent_ml + aq_ml + lip_ml) / w,
            "energy kcal/kg/d": sum(kcal.values()) / w,
            "  of which": {k: round(v / w, 1) for k, v in kcal.items() if v},
            "protein g/kg/d": protein_g / w,
            "lipid g/kg/d": lip_ml * 0.2 / w,
            "GIR mg/kg/min": gir_mg_kg_min(self.dextrose_pct, self.aqueous_ml_h, w),
        }


def check(summary, targets):
    """Compare against target ranges YOU take from your local protocol."""
    flags = []
    for key, (lo, hi) in targets.items():
        v = summary[key]
        if v < lo:
            flags.append(f"LOW  {key}: {v:.1f} (target {lo}-{hi})")
        elif v > hi:
            flags.append(f"HIGH {key}: {v:.1f} (target {lo}-{hi})")
    return flags or ["all within the supplied targets"]


def show(title, r, targets=None):
    s = r.summary()
    print(f"--- {title}")
    for k, v in s.items():
        print(f"{k:>18}: {v if isinstance(v, dict) else round(v, 2)}")
    if targets:
        for f in check(s, targets):
            print("  ->", f)


# Example 2: preterm 1.2 kg on PN (day 3). Targets are ILLUSTRATIVE.
preterm_targets = {"GIR mg/kg/min": (4, 12), "protein g/kg/d": (2.5, 3.5),
                   "lipid g/kg/d": (0, 4)}
show("Preterm 1.2 kg, PN only",
     Regimen(1.2, aqueous_ml_h=5.25, dextrose_pct=10, amino_acid_pct=2.86,
             lipid20_ml_h=0.75), preterm_targets)

# Example 3: the PN -> enteral transition table
for ent in (0, 30, 60, 90, 120, 150):
    lipid = 0.75 if ent < 120 else 0.0
    aq = max(150 * 1.2 - ent * 1.2 - lipid * 24, 0) / 24
    s = Regimen(1.2, enteral_ml_kg_day=ent, milk_protein_g_per_100ml=1.2,
                aqueous_ml_h=aq, dextrose_pct=10,
                amino_acid_pct=2.86 if aq else 0, lipid20_ml_h=lipid).summary()
    print(f"{ent:4} {aq:5.2f} {lipid:5.2f} {s['energy kcal/kg/d']:6.1f}"
          f" {s['protein g/kg/d']:5.2f} {s['GIR mg/kg/min']:5.2f}")

# Example 8: growth velocity
print("GV:", round(1000 * math.log(1480 / 1200) / 14, 2), "g/kg/day")
```

Output:

```text
--- Preterm 1.2 kg, PN only
     fluid mL/kg/d: 120.0
  energy kcal/kg/d: 77.71
          of which: {'dextrose': 35.7, 'amino acids': 12.0, 'lipid': 30.0}
    protein g/kg/d: 3.0
      lipid g/kg/d: 3.0
     GIR mg/kg/min: 7.29
  -> all within the supplied targets
   0  6.75  0.75   91.3  3.86  9.38
  30  5.25  0.75   97.8  3.36  7.29
  60  3.75  0.75  104.3  2.86  5.21
  90  2.25  0.75  110.7  2.37  3.12
 120  1.50  0.00   94.0  2.30  2.08
 150  0.00  0.00  100.5  1.80  0.00
GV: 14.98 g/kg/day
```

> [!TIP]
> To extend the tool, add electrolytes as mmol/kg/day per component, a non-protein-energy ratio, and an osmolarity estimate for peripheral PN. Each is the same "volume × concentration ÷ weight" pattern. Then turn the transition table into a printable chart for your unit, as in [Building your own clinical scales](../building-your-own-clinical-scales/), with the same validation and governance.

## Practice

1. A 2.4 kg baby is prescribed 120 mL/kg/day of feeds as 8 feeds a day. What volume per feed?

<details>
<summary>Answer</summary>

$120 \times 2.4 = 288$ mL/day, and $288 / 8 = 36$ mL per feed.

</details>

2. A 900 g baby receives 10% dextrose at 3.6 mL/h. What is the GIR?

<details>
<summary>Answer</summary>

$\dfrac{10 \times 3.6 \times 10}{60 \times 0.9} = \dfrac{360}{54} = 6.67$ mg/kg/min.

</details>

3. A 1.5 kg baby needs a GIR of 8 mg/kg/min. The aqueous fluid allowance is 4.5 mL/h. What dextrose concentration is needed?

<details>
<summary>Answer</summary>

$\dfrac{8 \times 60 \times 1.5}{4.5 \times 10} = \dfrac{720}{45} = 16\%$. That exceeds a typical peripheral limit, so it would need central access, or a review of the volume or the target.

</details>

4. A 1.0 kg baby is prescribed 2 g/kg/day of lipid as a 20% emulsion. What rate in mL/h, and how many kcal/kg/day does it provide?

<details>
<summary>Answer</summary>

2 g/day ÷ 0.2 g/mL = 10 mL/day, which is $10/24 = 0.42$ mL/h. Energy: $10 \times 2 = 20$ kcal/day = 20 kcal/kg/day.

</details>

5. Convert a glucose intake of 9 g/kg/day into mg/kg/min.

<details>
<summary>Answer</summary>

$9000 / 1440 = 6.25$ mg/kg/min.

</details>

6. A term baby on 160 mL/kg/day of formula at 67 kcal/100 mL. Energy intake?

<details>
<summary>Answer</summary>

$160 \times 0.67 = 107.2$ kcal/kg/day.

</details>

7. A preterm baby weighed 1,050 g on day 10 and 1,300 g on day 24. Calculate the exponential growth velocity.

<details>
<summary>Answer</summary>

$1000 \times \ln(1300/1050) / 14 = 1000 \times 0.2136 / 14 = 15.3$ g/kg/day.

</details>

8. An 8-month-old weighs 6.3 kg. Ideal weight for length is 7.7 kg, and the reference requirement for weight-age is 95 kcal/kg/day (illustrative). Estimate catch-up energy needs, and the volume of a 1 kcal/mL feed.

<details>
<summary>Answer</summary>

$95 \times 7.7 / 6.3 = 116.1$ kcal/kg/day. At 1 kcal/mL that is about 116 mL/kg/day, or $116.1 \times 6.3 \approx 731$ mL/day.

</details>

## Further reading

- Holliday MA, Segar WE. The maintenance need for water in parenteral fluid therapy. *Pediatrics*. 1957;19(5):823–832.
- ESPGHAN/ESPEN/ESPR/CSPEN guidelines on pediatric parenteral nutrition. *Clinical Nutrition*. 2018;37(6 Pt B), especially the chapters on energy, amino acids, lipids, carbohydrates, and fluid and electrolytes.
- Embleton ND, et al. Enteral nutrition in preterm infants (2022): a position paper from the ESPGHAN Committee on Nutrition and invited experts. *Journal of Pediatric Gastroenterology and Nutrition*. 2023;76(2):248–268.
- NICE guideline NG154. *Neonatal parenteral nutrition*. 2020.
- Patel AL, Engstrom JL, Meier PP, Kimura RE. Accuracy of methods for calculating postnatal growth velocity for extremely low birth weight infants. *Pediatrics*. 2005;116(6):1466–1473.
- Koletzko B, et al. (eds.) *Pediatric Nutrition in Practice*. Karger (World Review of Nutrition and Dietetics series).
