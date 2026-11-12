+++
summary = "Turn a prescribed dose rate into a pump rate or a gravity drip rate and back again, derive the micrograms/kg/min formula and the 'rule of 6', and plan infusion durations and bag changes with built-in checks."
+++

# Infusions and Drip Rates

An infusion is a dose spread out over time. Instead of "give 500 mg", the prescription says "give 500 mg over 30 minutes", "run 1 litre over 8 hours", or "0.1 micrograms/kg/min, titrate to blood pressure". The equipment does not understand any of those. A volumetric pump wants **mL/h**. A gravity set wants **drops per minute**. Your job is to translate, correctly, every time, often at night and under pressure.

There is only one new idea in this chapter: a **rate** is an amount divided by a time, and rates convert with the same dimensional analysis as everything in [units, concentrations and conversions](../../clinical-mathematics/units-concentrations-and-conversions/). If rates and work problems feel rusty, see [rates and work](../../word-problems/rates-and-work/). Weight-based infusions use the dosing weights from [weight- and body-size-based dosing](../../clinical-mathematics/weight-and-body-size-based-dosing/).

> [!CAUTION]
> These examples teach arithmetic, not prescribing. Drug names, concentrations and dose rates here are illustrative. Infusions of high-risk drugs (vasopressors, inotropes, insulin, anticoagulants, potassium, opioids, and anything in children) must follow your current local protocol or formulary (for example BNF or BNFc, national guidance, hospital infusion charts), use the standard concentrations your unit has adopted, and be independently double-checked before starting and at every change.

## Key ideas

### From dose rate to mL/h

If a drug is in a solution of concentration $C$ (mg/mL) and you want it delivered at a dose rate $R$ (mg/h), then

$$
\text{pump rate (mL/h)} = R\ \frac{\cancel{\text{mg}}}{\text{h}} \times \frac{1\ \text{mL}}{C\ \cancel{\text{mg}}} = \frac{R}{C}.
$$

This is the universal dose formula from chapter 1, with "per hour" carried along. For an intermittent infusion ("1 g in 100 mL over 30 minutes"), the rate is just volume over time: $100\ \text{mL} / 0.5\ \text{h} = 200$ mL/h.

### Gravity drip rates

Without a pump, the nurse counts drops in the drip chamber. A giving set's **drop factor** is how many drops make 1 mL. It is printed on the packaging. Common values:

| Set | Drop factor |
|---|---|
| Standard adult set for clear fluids (UK) | 20 drops/mL |
| Blood administration set | often 15 drops/mL |
| Micro-drip (paediatric burette) set | 60 drops/mL |

(Sets with 10 or 15 drops/mL are common in some countries. Always read the packet.)

Then

$$
\text{drops/min} = \frac{\text{volume (mL)} \times \text{drop factor (drops/mL)}}{\text{time (min)}}.
$$

The units check: $\text{mL} \times \text{drops/mL} / \text{min} = \text{drops/min}$.

> [!TIP]
> With a 60 drops/mL micro-drip set, **drops/min equals mL/h**, because 60 drops/mL and 60 min/h cancel. 25 mL/h is 25 drops/min. With a 20 drops/mL set, drops/min is one third of mL/h.

Round drip rates to a whole number of drops: no one can count 41.7 drops. Gravity infusions are imprecise (the rate drifts with the height of the bag, the position of the arm and the cannula), so they are unsuitable for drugs where small rate errors matter.

### Weight-based dose rates: micrograms/kg/min

Vasoactive drugs are usually prescribed in **micrograms per kg per minute**. Suppose the prescription is $D$ micrograms/kg/min for a patient of $W$ kg, and the syringe holds $C$ micrograms/mL. Build the rate with dimensional analysis, one step at a time:

$$
D\ \frac{\text{micrograms}}{\cancel{\text{kg}}\cdot\cancel{\text{min}}}
\times W\ \cancel{\text{kg}}
\times 60\ \frac{\cancel{\text{min}}}{\text{h}}
\times \frac{1\ \text{mL}}{C\ \text{micrograms}}
= \frac{D \times W \times 60}{C}\ \frac{\text{mL}}{\text{h}}.
$$

Rearranging gives the reverse direction, which you need when you walk up to a pump that is already running and want to know what the patient is getting.

> [!IMPORTANT]
> **micrograms/kg/min ↔ mL/h**
> $$\text{rate (mL/h)} = \frac{D \times W \times 60}{C} \qquad\qquad D = \frac{\text{rate} \times C}{W \times 60}$$
> $D$ in micrograms/kg/min, $W$ in kg, $C$ in micrograms/mL.

**The "make up X mg in Y mL" method.** Infusions are prepared by adding $X$ mg of drug to make a total of $Y$ mL. The concentration in micrograms/mL is

$$
C = \frac{X \times 1000}{Y}.
$$

Everything else follows from the boxed formula. The steps never change:

```mermaid
flowchart LR
  A["Prescribed dose per kg per min"] --> B["x weight: dose per min"]
  B --> C["x 60: dose per hour"]
  C --> D["divide by concentration: mL per hour"]
  D --> E["Estimate and independent double-check"]
```

> [!WARNING]
> Check that $D$ and $C$ are in the **same mass unit**. A dose in micrograms/kg/min with a concentration in mg/mL gives a rate 1,000 times too high unless you convert. Converting the concentration to micrograms/mL first avoids this.

### The paediatric "rule of 6"

The rule of 6 is an old shortcut for inotrope infusions in children:

> Put $6 \times W$ mg of drug (where $W$ is the weight in kg) in a total of 100 mL. Then **1 mL/h delivers 1 microgram/kg/min**.

**Derivation.** $6W$ mg in 100 mL is $C = 6W \times 1000/100 = 60W$ micrograms/mL. Put rate = 1 mL/h into the reverse formula:

$$
D = \frac{1 \times 60W}{W \times 60} = 1\ \text{microgram/kg/min}.
$$

The weight cancels. That is the whole trick: the concentration is chosen to be proportional to the weight. A variant, the "rule of 0.6" ($0.6 \times W$ mg in 100 mL), gives 1 mL/h = 0.1 micrograms/kg/min for more potent drugs.

**Its limits.** The rule creates a different concentration for every patient. That means bedside calculations at the time of mixing (a source of error in its own right), concentrations that pharmacy and smart-pump libraries can't standardise, and in small infants a significant volume of fluid: a 3 kg infant on 10 micrograms/kg/min receives 10 mL/h, which is $240/3 = 80$ mL/kg/day from that one infusion. Patient-safety organisations (in the US, for example, ISMP and the Joint Commission) have pushed for **standard concentrations** programmed into smart pumps instead. Treat the rule of 6 as history and as a good algebra exercise, and use your unit's standard concentrations.

### Duration and bag changes

$$
\text{duration (h)} = \frac{\text{volume (mL)}}{\text{rate (mL/h)}}.
$$

1,000 mL at 125 mL/h lasts $1000/125 = 8$ hours. Planning the finish time lets you order the next bag or syringe before it runs out. This matters most for short-half-life drugs, where a gap of a few minutes can drop the blood pressure. The same formula tells you how much volume a patient gets from all their infusions, which links to [maintenance fluids](../../clinical-mathematics/maintenance-fluids-holliday-segar/).

### Independent double-checks

An **independent** double-check means a second qualified person does the calculation from the original prescription, without seeing your answer, then compares. Reading your working and nodding is not independent: people tend to confirm what they are shown. Check the drug, concentration, dosing weight, units, pump rate, line and patient identity. Smart pumps with drug libraries add another layer by flagging rates outside set limits, but they only work if the right drug and concentration are selected.

## Worked examples

### Example 1 · Infant (4 kg): rule-of-6 arithmetic

**Problem.** An illustrative inotrope, Drug D, is ordered at 5 micrograms/kg/min for a 4 kg infant, and the infusion is made up by the rule of 6. What goes in the syringe, and what is the pump rate?

**Make-up.** $6 \times 4 = 24$ mg in a total of 100 mL, so $C = 24{,}000/100 = 240$ micrograms/mL.

**Rate.** By the rule, 1 mL/h = 1 microgram/kg/min, so 5 micrograms/kg/min = **5 mL/h**. Check with the general formula: $5 \times 4 \times 60/240 = 1200/240 = 5$ mL/h.

### Example 2 · Child (20 kg): the general method with a standard concentration

**Problem.** Drug D, 10 micrograms/kg/min, 20 kg child. The unit's standard syringe is 80 mg in 50 mL.

**Estimate.** The dose is 200 micrograms/min, or 12 mg/h. The syringe has 1.6 mg/mL, so a bit under 10 mL/h.

**Calculate.** $C = 80{,}000/50 = 1{,}600$ micrograms/mL. Rate $= 10 \times 20 \times 60/1{,}600 = 12{,}000/1{,}600 = 7.5$ mL/h.

**Reverse check.** $7.5 \times 1{,}600/(20 \times 60) = 12{,}000/1{,}200 = 10$ micrograms/kg/min. This matches.

### Example 3 · Adolescent (55 kg): units/kg/h

**Problem.** An illustrative Drug H is ordered at 15 units/kg/h. The syringe contains 25,000 units in 50 mL.

**Calculate.** $C = 25{,}000/50 = 500$ units/mL. Dose rate $= 15 \times 55 = 825$ units/h. Pump rate $= 825/500 = 1.65$ mL/h.

**Check.** Same pattern, different units: amount per kg per hour × kg ÷ amount per mL. No factor of 60 here, because the dose is already per hour. Forgetting which time unit the prescription uses is a 60-fold error.

### Example 4 · Adult (80 kg): a vasopressor in micrograms/kg/min, both directions

**Problem.** A noradrenaline (norepinephrine)-style vasopressor is made up as 4 mg in 50 mL (an example concentration; units differ). The prescription is 0.1 micrograms/kg/min for an 80 kg adult.

**Concentration.** $C = 4{,}000/50 = 80$ micrograms/mL.

**Forward.**

$$
\text{rate} = \frac{0.1 \times 80 \times 60}{80} = 6\ \text{mL/h}.
$$

**Estimate check.** 0.1 micrograms/kg/min × 80 kg = 8 micrograms/min = 480 micrograms/h. At 80 micrograms/mL that is 6 mL/h. This matches.

**Reverse.** Later the pump is found running at 9 mL/h. What dose is that?

$$
D = \frac{9 \times 80}{80 \times 60} = 0.15\ \text{micrograms/kg/min}.
$$

> [!WARNING]
> Some noradrenaline products state their strength as noradrenaline **base** and others as noradrenaline **tartrate**, which differ by about a factor of two. Protocols must say which they mean. The same issue arises with other salts. Read the label, and use your unit's chart.

### Example 5 · Older adult with renal impairment: gravity rate and bag timing

**Problem.** An older adult with renal impairment is prescribed 500 mL of fluid over 4 hours by gravity, with a 20 drops/mL set. Later, a 250 mL bag of a renally adjusted infusion is started at 40 mL/h at 08:00. Find the drip rate and the time the second bag will finish.

**Drip rate.** $500 \times 20/(4 \times 60) = 10{,}000/240 \approx 41.7$, so set **42 drops/min** (125 mL/h).

**Duration.** $250/40 = 6.25$ h = 6 h 15 min, so the bag finishes at **14:15**.

**Why it matters here.** Patients with poor renal function handle fluid and drug loads less well. A gravity infusion that runs "a bit fast" can deliver the whole volume in half the time. For anything where that matters, a pump is safer.

### Example 6 · Obese adult (130 kg): which weight drives the pump?

**Problem.** The same 80 micrograms/mL vasopressor, 0.1 micrograms/kg/min, for the 180 cm, 130 kg man from the previous chapter (adjusted body weight about 97.0 kg).

**Calculate.**

| Dosing weight | Rate (mL/h) |
|---|---|
| Total body weight, 130 kg | $0.1 \times 130 \times 60/80 = 9.75$ |
| Adjusted body weight, 97.0 kg | $0.1 \times 97.0 \times 60/80 \approx 7.28$ |

The two rates differ by about a third. Local protocols specify the dosing weight for each infusion (some vasoactive protocols avoid the problem by prescribing in micrograms/min rather than per kg). Record which weight you used on the chart, so the next person doing the reverse check gets the same answer.

## Sanity checks and common errors

- **Estimate first**, in words: "about 8 micrograms a minute, about half a milligram an hour, the syringe has nearly a tenth of a milligram per mL, so around 6 mL/h."
- **Same mass unit for dose and concentration.** Convert mg/mL to micrograms/mL before using the formula.
- **Per minute or per hour?** micrograms/kg/**min** needs the factor 60. units/kg/**h** does not.
- **Total volume, not diluent volume.** "4 mg made up to 50 mL" is 50 mL total.
- **Reverse-calculate** every new rate back to the prescribed dose. If the two don't match, find out why before starting.
- **Drop factor from the packet**, not from memory.
- **Round sensibly.** Pumps accept one or two decimals; drops are whole numbers. Round at the end, not in the middle.
- **Bag timing.** Work out when the infusion ends and plan the next one. Check the running total of all infusions as fluid.
- **Salt form and dosing weight.** Write both on the chart.

## In code

The calculator below converts both ways, refuses implausible weights and doses above a protocol maximum, computes gravity drip rates and plans finish times. It reproduces Examples 1, 4 and 5.

```python
from datetime import datetime, timedelta

def concentration_mcg_per_ml(drug_mg, total_ml):
    """'Make up drug_mg in total_ml' -> micrograms per mL."""
    if drug_mg <= 0 or total_ml <= 0:
        raise ValueError("amount and volume must be positive")
    return drug_mg * 1000 / total_ml

def ml_per_h(dose_mcg_kg_min, kg, conc_mcg_ml, max_dose=None):
    """Pump rate (mL/h) for a dose in micrograms/kg/min."""
    if not 0.3 <= kg <= 350:
        raise ValueError(f"implausible weight {kg} kg")
    if max_dose is not None and dose_mcg_kg_min > max_dose:
        raise ValueError(f"{dose_mcg_kg_min} exceeds the protocol maximum {max_dose}")
    return dose_mcg_kg_min * kg * 60 / conc_mcg_ml

def dose_from_rate(rate_ml_h, kg, conc_mcg_ml):
    """Inverse: what micrograms/kg/min is this pump rate delivering?"""
    return rate_ml_h * conc_mcg_ml / (kg * 60)

def drops_per_min(volume_ml, minutes, drop_factor):
    return volume_ml * drop_factor / minutes

def finish_time(start, volume_ml, rate_ml_h):
    return start + timedelta(hours=volume_ml / rate_ml_h)

# Adult, 80 kg: 4 mg in 50 mL, 0.1 micrograms/kg/min
c = concentration_mcg_per_ml(4, 50)
print(f"4 mg in 50 mL = {c:.0f} micrograms/mL")
print(f"80 kg at 0.1: {ml_per_h(0.1, 80, c):.2f} mL/h")
print(f"pump at 9 mL/h delivers {dose_from_rate(9, 80, c):.3f} micrograms/kg/min")
# Infant, 4 kg, rule of 6: 6 x 4 = 24 mg in 100 mL
c6 = concentration_mcg_per_ml(6 * 4, 100)
print(f"rule of 6, 4 kg: 1 mL/h = {dose_from_rate(1, 4, c6):.2f} micrograms/kg/min;"
      f" 5 micrograms/kg/min = {ml_per_h(5, 4, c6):.1f} mL/h")
# Gravity sets
print(f"1000 mL over 8 h, 20 drops/mL: {drops_per_min(1000, 8 * 60, 20):.1f} drops/min")
print(f"500 mL over 24 h, 60 drops/mL: {drops_per_min(500, 24 * 60, 60):.1f} drops/min")
end = finish_time(datetime(2026, 1, 1, 8, 0), 250, 40)
print("250 mL at 40 mL/h from 08:00 finishes at", end.strftime("%H:%M"))
try:
    ml_per_h(1.0, 80, c, max_dose=0.5)
except ValueError as e:
    print("Refused:", e)
```

Output:

```
4 mg in 50 mL = 80 micrograms/mL
80 kg at 0.1: 6.00 mL/h
pump at 9 mL/h delivers 0.150 micrograms/kg/min
rule of 6, 4 kg: 1 mL/h = 1.00 micrograms/kg/min; 5 micrograms/kg/min = 5.0 mL/h
1000 mL over 8 h, 20 drops/mL: 41.7 drops/min
500 mL over 24 h, 60 drops/mL: 20.8 drops/min
250 mL at 40 mL/h from 08:00 finishes at 14:15
Refused: 1.0 exceeds the protocol maximum 0.5
```

The code does the arithmetic. It cannot check that 4 mg in 50 mL is what is actually in the syringe, or that the patient really weighs 80 kg. Those checks belong to people. A printable rate table built from `ml_per_h` is one of the projects in [building your own clinical scales](../../clinical-mathematics/building-your-own-clinical-scales/).

## Practice

1. 1 litre of fluid is to run over 10 hours with a 20 drops/mL set. What is the rate in mL/h and in drops/min?

<details>
<summary>Answer</summary>

$1000/10 = 100$ mL/h. $1000 \times 20/600 \approx 33.3$, so 33 drops/min.

</details>

2. A child's fluid is running through a 60 drops/mL micro-drip set at 30 mL/h. How many drops per minute should you count?

<details>
<summary>Answer</summary>

With a 60 drops/mL set, drops/min = mL/h, so 30 drops/min. (Check: $30 \times 60/60 = 30$.)

</details>

3. A 70 kg adult is prescribed an illustrative Drug D at 5 micrograms/kg/min. The syringe contains 200 mg in 50 mL. What pump rate?

<details>
<summary>Answer</summary>

$C = 200{,}000/50 = 4{,}000$ micrograms/mL. Rate $= 5 \times 70 \times 60/4{,}000 = 21{,}000/4{,}000 = 5.25$ mL/h.

</details>

4. A 60 kg patient has a syringe of 8 mg in 50 mL running at 4.5 mL/h. What dose in micrograms/kg/min is that?

<details>
<summary>Answer</summary>

$C = 8{,}000/50 = 160$ micrograms/mL. $D = 4.5 \times 160/(60 \times 60) = 720/3{,}600 = 0.2$ micrograms/kg/min.

</details>

5. Using the rule of 6 for a 15 kg child: how many mg go in the 100 mL, what rate gives 3 micrograms/kg/min, and if the drug comes as 40 mg/mL, how much drug and how much diluent do you use?

<details>
<summary>Answer</summary>

$6 \times 15 = 90$ mg in 100 mL total. 3 micrograms/kg/min = 3 mL/h. Drug volume $= 90/40 = 2.25$ mL, made up with $100 - 2.25 = 97.75$ mL of diluent. (That awkward volume is one reason units prefer standard concentrations.)

</details>

6. A 1,000 mL bag is started at 80 mL/h at 22:00. When will it finish?

<details>
<summary>Answer</summary>

$1000/80 = 12.5$ h, so at 10:30 the next morning.

</details>

7. A 30 kg child is prescribed an illustrative Drug H at 20 units/kg/h. The syringe holds 50 units/mL. What pump rate?

<details>
<summary>Answer</summary>

$30 \times 20 = 600$ units/h. $600/50 = 12$ mL/h. (No factor of 60: the dose is already per hour.)

</details>

8. 1 g of an illustrative Drug R is in 250 mL and runs at 50 mL/h. What dose rate in mg/h is the patient getting, and how long will the bag last?

<details>
<summary>Answer</summary>

Concentration $1000/250 = 4$ mg/mL. Dose rate $= 50 \times 4 = 200$ mg/h. Duration $= 250/50 = 5$ h.

</details>

## Further reading

- Joint Formulary Committee. *British National Formulary* and *BNF for Children*. Sections on intravenous administration and drug-specific infusion guidance.
- Institute for Safe Medication Practices (ISMP). Guidance on standard concentrations and smart infusion pumps, at ismp.org.
- Lapham, R. *Drug Calculations for Nurses: A Step-by-Step Approach.* CRC Press. Chapters on infusion rates and drip rates.
- In this course: [rates and work](../../word-problems/rates-and-work/), and the next chapter, [maintenance fluids (Holliday–Segar)](../../clinical-mathematics/maintenance-fluids-holliday-segar/).
