+++
summary = "Convert confidently between mass units, volumes, percentage and ratio strengths, mmol and mEq, and dilutions, using dimensional analysis so that a 10-fold error shows up before it reaches a patient."
+++

# Units, Concentrations and Conversions

Most serious medication errors are not caused by hard mathematics. They are caused by easy mathematics done in a hurry: a decimal point in the wrong place, milligrams read as micrograms, "1:1,000" confused with "1:10,000". Each of these is a factor of 10 or 1,000, and the result is a dose that is ten or a thousand times too large or too small.

This chapter teaches one method, **dimensional analysis**, and applies it to every unit you meet on a drug chart: grams to nanograms, millilitres, mg/mL, % w/v, ratio strengths, mmol and mEq, and dilutions. The arithmetic is GMAT-level. If you want a refresher, see [fractions, decimals and percents](../../arithmetic/fractions-decimals-percents/), [ratios](../../arithmetic/ratios/) and [mixtures](../../word-problems/mixtures-and-interest/). The habits matter more than the arithmetic: write the units, cancel them, estimate first, and check.

> [!CAUTION]
> This chapter teaches arithmetic, not prescribing. Doses, concentrations and products in the examples are illustrative. Before giving any drug, check the dose against your current local formulary or guideline (for example the BNF or BNFc, national guidance, or your hospital's protocol), and use an independent double-check for high-risk drugs and for all children.

## Key ideas

### Dimensional analysis: multiply by 1

A conversion factor is a fraction whose top and bottom are equal, so it is just 1 in disguise. For example, $1\ \text{g} = 1000\ \text{mg}$, so

$$
\frac{1000\ \text{mg}}{1\ \text{g}} = 1 \quad\text{and}\quad \frac{1\ \text{g}}{1000\ \text{mg}} = 1.
$$

Multiplying a quantity by 1 does not change it. You choose the version of the fraction that **cancels the unit you have and leaves the unit you want**. To turn 0.25 g into mg:

$$
0.25\ \cancel{\text{g}} \times \frac{1000\ \text{mg}}{1\ \cancel{\text{g}}} = 250\ \text{mg}.
$$

Units cancel like algebraic symbols. If the units left at the end are not the units you want, the setup is wrong, whatever the numbers say. This catches most inverted fractions, which are the most common error in drug calculations.

> [!TIP]
> **The universal dose formula** is dimensional analysis in one line. With a dose $D$ (mg) and a stock concentration $C$ (mg/mL),
> $$\text{volume (mL)} = D\ \cancel{\text{mg}} \times \frac{1\ \text{mL}}{C\ \cancel{\text{mg}}} = \frac{D}{C}.$$
> Nurses often learn it as "what you want over what you've got, times what it's in". It is the same equation.

### Mass units and the 1,000× ladder

| Unit | Symbol on a chart | In grams |
|---|---|---|
| gram | g | $1$ |
| milligram | mg | $10^{-3}$ |
| microgram | write **micrograms** in full | $10^{-6}$ |
| nanogram | write **nanograms** in full | $10^{-9}$ |

Each step down the ladder multiplies the number by 1,000. Going from a larger unit to a smaller one, the number gets **bigger** (0.5 mg = 500 micrograms). Going from smaller to larger, it gets **smaller** (250 mg = 0.25 g).

> [!WARNING]
> **The 1,000× trap.** Milligrams and micrograms differ by a factor of 1,000. Handwritten "µg" can be read as "mg", which turns 50 micrograms into 50 mg: a thousand-fold overdose. This is why safe-prescribing guidance asks you to write "micrograms" and "nanograms" in full.

Volumes follow the same ladder: 1 L = 1000 mL, and 1 mL = 1000 microlitres. (1 mL is the same volume as 1 cm³. The abbreviation "cc" is discouraged because it can be misread.)

### Concentration as mass per volume

A concentration is a rate: mass per unit volume, usually **mg/mL**. Every other way of stating strength (%, ratio, mmol/L) can be converted to mg/mL, and you should do that first. Once everything is in mg and mL, the universal formula does the rest.

### Percentage strength (% w/v)

"% w/v" means **grams per 100 mL**. So

$$
1\% = \frac{1\ \text{g}}{100\ \text{mL}} = \frac{1000\ \text{mg}}{100\ \text{mL}} = 10\ \text{mg/mL}.
$$

> [!IMPORTANT]
> **Percent to mg/mL:** multiply the percentage by 10.
> $$x\%\ \text{w/v} = 10x\ \text{mg/mL} = 10x\ \text{g/L}$$

Examples: lidocaine 1% is 10 mg/mL and 2% is 20 mg/mL. Glucose 5% contains 50 g/L, glucose 10% contains 100 g/L. Sodium chloride 0.9% contains 9 g/L.

### Ratio strength (1 : x)

A ratio strength "1 in $x$" or "1 : $x$" means **1 g in $x$ mL**. It survives mainly for adrenaline (epinephrine) and for local anaesthetics with added adrenaline.

$$
1{:}1{,}000 = \frac{1\ \text{g}}{1000\ \text{mL}} = \frac{1000\ \text{mg}}{1000\ \text{mL}} = 1\ \text{mg/mL},
\qquad
1{:}10{,}000 = 0.1\ \text{mg/mL}.
$$

> [!IMPORTANT]
> **Ratio to mg/mL:** $1{:}x = \dfrac{1000}{x}\ \text{mg/mL}$.

The bigger the second number, the **weaker** the solution. 1:10,000 is ten times weaker than 1:1,000. Many countries now label adrenaline products in mg/mL as well, precisely because ratio strengths cause errors.

### Amount of substance: mmol and mEq

Electrolytes are dosed in **millimoles** (mmol), because the body cares about the number of ions, not their mass. One mole of a substance weighs its molar mass in grams, so one millimole weighs its molar mass in milligrams:

$$
\text{mmol} = \frac{\text{mass (mg)}}{\text{molar mass (g/mol)}}.
$$

A salt such as NaCl releases one Na⁺ and one Cl⁻ per formula unit, so 1 mmol NaCl gives 1 mmol Na⁺.

**Sodium chloride 0.9%.** 9 g/L, molar mass 58.44 g/mol:

$$
\frac{9000\ \text{mg/L}}{58.44\ \text{mg/mmol}} \approx 154\ \text{mmol/L of Na}^+ \text{ (and 154 mmol/L of Cl}^-).
$$

**Potassium chloride.** Molar mass 74.55 g/mol, so 1 g KCl contains about $1000/74.55 \approx 13.4$ mmol of K⁺. A 10 mL ampoule of 15% KCl contains $15 \times 10 = 150$ mg/mL $\times$ 10 mL $= 1500$ mg, which is $1500/74.55 \approx 20.1$, about **20 mmol** of K⁺.

**Sodium bicarbonate 8.4%.** 84 g/L, molar mass about 84 g/mol, so it is almost exactly **1 mmol/mL**. That neat number is the reason 8.4% was chosen.

**Milliequivalents** count charge. For an ion of valence (charge) $z$,

$$
\text{mEq} = \text{mmol} \times \lvert z \rvert.
$$

For Na⁺, K⁺ and Cl⁻ ($z = 1$), mmol and mEq are the same number. For Ca²⁺ and Mg²⁺ ($z = 2$), 1 mmol = 2 mEq. North American sources often use mEq; UK and European sources usually use mmol. Always check which one a protocol means.

> [!NOTE]
> Hydrated salts carry water in their molar mass. Magnesium sulfate for injection is the heptahydrate, MgSO₄·7H₂O (about 246.5 g/mol), so 1 g contains about $1000/246.5 \approx 4.1$ mmol of Mg²⁺, usually quoted as "about 4 mmol". Calcium gluconate (about 448 g/mol for the monohydrate) gives only about 2.2 mmol Ca²⁺ per gram. Use the molar mass of the exact salt on the label.

### Dilutions: C₁V₁ = C₂V₂

When you dilute, you add solvent but no drug, so the **amount of drug stays the same**. Amount = concentration × volume, so

$$
C_1 V_1 = C_2 V_2,
$$

where $C_1, V_1$ are the stock concentration and the volume of stock you take, and $C_2, V_2$ are the final concentration and the final **total** volume. Solve for whichever one you don't know. The volume of diluent to add is $V_2 - V_1$, not $V_2$.

Diluting by a factor $k$ (for example $k = 10$) means $C_2 = C_1/k$ and $V_2 = k V_1$: 1 mL of stock made up to 10 mL.

### Writing doses safely

Safe-writing rules exist because each one has caused deaths through a misread factor of 10.

| Rule | Unsafe | Safe | Why |
|---|---|---|---|
| Always a leading zero | .5 mg | 0.5 mg | ".5" can be read as "5" (10× overdose) |
| Never a trailing zero | 5.0 mg | 5 mg | "5.0" can be read as "50" (10× overdose) |
| Write micrograms and nanograms in full | 50 µg, 50 mcg, 50 ng | 50 micrograms, 50 nanograms | "µg" is read as "mg" (1,000×) |
| Write units in full | 10 U, 10 IU | 10 units | "U" is read as "0" (10 U becomes 100) |
| Avoid decimals where a smaller unit works | 0.05 mg | 50 micrograms | whole numbers are harder to misread |
| No "cc" | 5 cc | 5 mL | "cc" can be read as "00" or "u" |

(Trailing zeros are acceptable in laboratory results and device displays where precision is the point. On a prescription they are a hazard.)

### Ten-fold errors and how to catch them

A **10-fold error** is a dose out by a factor of 10 because a decimal point slipped, a zero was added or lost, or the wrong concentration was used. Children are at particular risk because every dose is calculated, the volumes are small, and the same drug comes in several strengths. Three checks catch most of them:

1. **Estimate first.** Before computing, say roughly what the answer should be ("about half a millilitre", "a few millilitres", "most of a vial"). If the calculation gives 0.05 or 50, stop.
2. **Check against a typical dose.** If a weight-based dose for a child comes out larger than the usual adult dose, something is wrong. See [weight- and body-size-based dosing](../../clinical-mathematics/weight-and-body-size-based-dosing/).
3. **Independent double-check.** A second person repeats the calculation from scratch, without seeing the first answer, and the two results are compared.

## Worked examples

Each example uses a different kind of patient. The point is the arithmetic, so check every real dose against your formulary.

### Example 1 · Infant (5 kg): a dose in micrograms, too small to measure

**Problem.** An illustrative Drug M is prescribed as 50 micrograms. The stock is 1 mg/mL. What volume do you draw up?

**Estimate.** 1 mg/mL is 1,000 micrograms per mL. 50 micrograms is one twentieth of 1,000, so the answer is a small fraction of a mL.

**Calculate.** Convert the dose to mg first: $50\ \text{micrograms} \times \dfrac{1\ \text{mg}}{1000\ \text{micrograms}} = 0.05\ \text{mg}$. Then

$$
\text{volume} = \frac{0.05\ \text{mg}}{1\ \text{mg/mL}} = 0.05\ \text{mL}.
$$

**Is it safe to measure?** 0.05 mL is a tiny volume, and the dead space in a syringe hub can be a large fraction of it. The usual answer is to dilute first. Take 1 mL of stock (1 mg) and make it up to 10 mL total. By $C_1V_1 = C_2V_2$, $C_2 = 1 \times 1 / 10 = 0.1$ mg/mL $= 100$ micrograms/mL. Now the dose is

$$
\frac{50\ \text{micrograms}}{100\ \text{micrograms/mL}} = 0.5\ \text{mL}.
$$

Note how one dilution step creates a new chance for a 10-fold error: if someone uses 0.5 mL of the **undiluted** stock, the infant receives 500 micrograms. Label diluted syringes clearly with the final concentration.

### Example 2 · Child (20 kg): what is in a bag of fluid?

**Problem.** A child is receiving 1,000 mL of sodium chloride 0.9% with glucose 5%. How many mmol of sodium and how many grams of glucose are in the bag?

**Sodium.** 0.9% is 9 g/L, which we showed is about 154 mmol/L. One litre therefore contains about **154 mmol** of Na⁺.

**Glucose.** 5% is 5 g per 100 mL, so $5 \times 10 = 50$ g per litre: **50 g** of glucose.

**Check.** 50 g of glucose is roughly 50 × 4 kcal ≈ 200 kcal, the figure UK product data sheets quote for glucose 5%, whose 50 g/L is stated as anhydrous glucose. US "D5W" contains 50 g/L of glucose *monohydrate*, conventionally counted at 3.4 kcal/g, about 170 kcal/L. Read the label; see [nutrition calculations](../../clinical-mathematics/nutrition-energy-and-parenteral-calculations/). How much of this bag a child should receive per day is the subject of [maintenance fluids](../../clinical-mathematics/maintenance-fluids-holliday-segar/).

### Example 3 · Adolescent: adrenaline and the two ratio strengths

**Problem.** Resuscitation guidelines in the UK give intramuscular adrenaline for anaphylaxis in adults and children over 12 as 500 micrograms (0.5 mg). Adrenaline comes as 1:1,000 and 1:10,000. What volume of each contains 0.5 mg? (Confirm the dose in your current national guideline.)

**Convert the strengths.** 1:1,000 = 1 mg/mL. 1:10,000 = 0.1 mg/mL.

**Volumes.**

$$
\frac{0.5\ \text{mg}}{1\ \text{mg/mL}} = 0.5\ \text{mL of }1{:}1{,}000,
\qquad
\frac{0.5\ \text{mg}}{0.1\ \text{mg/mL}} = 5\ \text{mL of }1{:}10{,}000.
$$

**The trap.** The two answers differ by a factor of 10. Picking up the wrong ampoule but keeping the volume you remember ("half a mL") gives one tenth of the intended dose. Remembering "5 mL" with the 1 mg/mL product gives ten times the dose. The IM route uses the 1 mg/mL (1:1,000) product. Read the mg/mL on the label, not just the ratio.

### Example 4 · Adult: potassium in mmol

**Problem.** An adult needs 40 mmol of potassium chloride added to a 1 L bag. The stock is 15% KCl in 10 mL ampoules. How many ampoules, and what is the final concentration?

**Ampoule content.** We showed 10 mL of 15% KCl contains 1,500 mg, about 20.1 mmol of K⁺. Call it 20 mmol, the figure printed on many labels.

**Ampoules.** $40 / 20 = 2$ ampoules (20 mL).

**Final concentration.** $40$ mmol in about $1{,}000 + 20 = 1{,}020$ mL, about 39 mmol/L, which most people round to 40 mmol/L.

> [!WARNING]
> Concentrated potassium chloride is a well-known cause of fatal errors, and many hospitals keep it out of general wards and use pre-mixed bags instead. Follow your local policy on potassium concentration, rate, and monitoring. This example shows the arithmetic only.

### Example 5 · Older adult with renal impairment: two unit systems for creatinine

**Problem.** An 82-year-old's referral letter says serum creatinine 1.5 mg/dL. Your laboratory reports in µmol/L. Convert it. Then convert 120 µmol/L back to mg/dL.

The molar mass of creatinine is about 113.12 g/mol. 1 mg/dL is 10 mg/L, and $10/113.12$ mmol/L $\approx 0.0884$ mmol/L $= 88.4$ µmol/L. So

$$
1.5\ \text{mg/dL} \times 88.4 = 132.6\ \text{µmol/L} \approx 133\ \text{µmol/L},
\qquad
120\ \text{µmol/L} \div 88.4 \approx 1.36\ \text{mg/dL}.
$$

Renal dose adjustments depend on these numbers, and mixing up the units makes creatinine clearance wrong by a factor of 88. The [next chapter](../../clinical-mathematics/weight-and-body-size-based-dosing/) uses them in the Cockcroft–Gault equation.

### Example 6 · Obese adult: imperial to SI

**Problem.** An adult is recorded as 264 lb and 5 ft 9 in. Convert to kg and cm before any dosing calculation.

**Weight.** 1 kg ≈ 2.2046 lb, so $264 / 2.2046 \approx 119.7$ kg.

**Height.** 5 ft 9 in $= 5 \times 12 + 9 = 69$ in, and $69 \times 2.54 = 175.26$ cm $\approx 175$ cm.

Weight in pounds entered into a field that expects kilograms more than doubles every weight-based dose. Always record weight in kg. Whether to dose this patient on total, ideal or adjusted body weight is covered in the next chapter.

## Sanity checks and common errors

- **Units at every step.** Write the unit after every number and cancel. If you are left with mg²/mL, you multiplied where you should have divided.
- **Bigger unit, smaller number.** 0.5 g is 500 mg, not 0.0005 mg. Converting down (g to mg) the number grows.
- **Ratio direction.** 1:10,000 is weaker than 1:1,000. Convert to mg/mL before comparing.
- **Percent means per 100 mL.** 2% is 20 mg/mL, not 2 mg/mL and not 200 mg/mL.
- **Diluent versus final volume.** "Make up to 10 mL" means a final volume of 10 mL, so 1 mL of stock plus 9 mL of diluent.
- **mmol versus mEq.** For divalent ions (Ca²⁺, Mg²⁺), 1 mmol = 2 mEq. A protocol written in mEq and drawn up in mmol is out by a factor of 2.
- **Salt form.** "1 g of magnesium sulfate" is not 1 g of magnesium. Use the molar mass of the actual salt.
- **Volumes you can't measure.** If a calculated volume is below what your syringe can measure accurately, dilute, or ask pharmacy for a more suitable product.
- **Too large or too small?** Any volume that is a whole vial for a small child, or a few drops for an adult, deserves a second look.

## In code

The calculator converts everything into mg and mL first, refuses unit spellings it doesn't recognise (rather than guessing what "ug" means), and warns when a volume is too small to draw up. The 0.1 mL threshold is a setting, not a rule: choose it to match your syringes and local practice.

```python
# Unit and concentration helpers: everything is converted to mg and mL first.
MASS_TO_MG = {"g": 1000.0, "mg": 1.0, "micrograms": 0.001, "ng": 0.000001}

def to_mg(value, unit):
    """Convert a mass to mg. Refuses ambiguous or unknown unit spellings."""
    if unit not in MASS_TO_MG:
        raise ValueError(f"unknown or unsafe unit {unit!r}; use one of {list(MASS_TO_MG)}")
    if value < 0:
        raise ValueError("mass cannot be negative")
    return value * MASS_TO_MG[unit]

def percent_wv_to_mg_per_ml(percent):
    """x % w/v = x g per 100 mL = 10x mg/mL."""
    return percent * 1000 / 100

def ratio_to_mg_per_ml(parts):
    """Ratio strength 1:parts means 1 g in `parts` mL."""
    return 1000.0 / parts

def mmol_from_mass(mass_mg, molar_mass_g_per_mol):
    """mg / (g/mol) = mmol."""
    return mass_mg / molar_mass_g_per_mol

def volume_to_draw(dose, dose_unit, stock_mg_per_ml, min_measurable_ml=0.1):
    """Volume (mL) for a dose; warns when the volume is too small to measure reliably."""
    ml = to_mg(dose, dose_unit) / stock_mg_per_ml
    if ml < min_measurable_ml:
        print(f"  WARNING: {ml:.3g} mL is below {min_measurable_ml} mL; dilute the stock first")
    return ml

def dilution_volume(c1, c2, v2):
    """C1 V1 = C2 V2: volume of stock (V1) needed to make V2 at concentration C2."""
    if c2 > c1:
        raise ValueError("cannot dilute to a higher concentration")
    return c2 * v2 / c1

print("1% w/v          =", percent_wv_to_mg_per_ml(1), "mg/mL")
print("1:1,000         =", ratio_to_mg_per_ml(1_000), "mg/mL")
print("1:10,000        =", ratio_to_mg_per_ml(10_000), "mg/mL")
na = mmol_from_mass(percent_wv_to_mg_per_ml(0.9) * 1000, 58.44)
print(f"NaCl 0.9%       = {na:.0f} mmol/L Na+")
k = mmol_from_mass(percent_wv_to_mg_per_ml(15) * 10, 74.55)
print(f"10 mL KCl 15%   = {k:.1f} mmol K+")
print("50 micrograms from 1 mg/mL stock:")
v = volume_to_draw(50, "micrograms", 1.0)
print(f"  {v} mL")
print("same dose after diluting 1 mL to 10 mL (0.1 mg/mL):",
      volume_to_draw(50, "micrograms", 0.1), "mL")
print("stock for 100 mL of 0.1 mg/mL from 1 mg/mL:", dilution_volume(1.0, 0.1, 100), "mL")
try:
    to_mg(5, "ug")
except ValueError as e:
    print("Refused:", e)
```

Output:

```
1% w/v          = 10.0 mg/mL
1:1,000         = 1.0 mg/mL
1:10,000        = 0.1 mg/mL
NaCl 0.9%       = 154 mmol/L Na+
10 mL KCl 15%   = 20.1 mmol K+
50 micrograms from 1 mg/mL stock:
  WARNING: 0.05 mL is below 0.1 mL; dilute the stock first
  0.05 mL
same dose after diluting 1 mL to 10 mL (0.1 mg/mL): 0.5 mL
stock for 100 mL of 0.1 mg/mL from 1 mg/mL: 10.0 mL
Refused: unknown or unsafe unit 'ug'; use one of ['g', 'mg', 'micrograms', 'ng']
```

Notice that the code accepts "micrograms" but not "ug" or "mcg". The same rule that protects handwritten charts protects software: one unambiguous spelling per unit.

## Practice

1. Convert (a) 2.5 mg to micrograms, (b) 0.075 g to mg, (c) 750 nanograms to micrograms.

<details>
<summary>Answer</summary>

(a) $2.5 \times 1000 = 2{,}500$ micrograms. (b) $0.075 \times 1000 = 75$ mg. (c) $750 / 1000 = 0.75$ micrograms.

</details>

2. How many mg of lidocaine are in 5 mL of a 2% solution?

<details>
<summary>Answer</summary>

2% = 20 mg/mL, so $5 \times 20 = 100$ mg.

</details>

3. A local anaesthetic contains adrenaline 1:200,000. Express this in micrograms/mL.

<details>
<summary>Answer</summary>

$1{:}200{,}000 = 1000/200{,}000 = 0.005$ mg/mL $= 5$ micrograms/mL.

</details>

4. How many mg of potassium chloride (molar mass 74.55 g/mol) provide 20 mmol of K⁺? What volume of 15% KCl is that?

<details>
<summary>Answer</summary>

$20 \times 74.55 = 1{,}491$ mg, about 1.5 g. 15% is 150 mg/mL, so $1{,}491 / 150 \approx 9.94$ mL, about 10 mL. This matches the "20 mmol per 10 mL ampoule" figure.

</details>

5. You need 100 mL of glucose 10% and you have glucose 50% and water for injection. How much of each?

<details>
<summary>Answer</summary>

$C_1V_1 = C_2V_2$: $50 \times V_1 = 10 \times 100$, so $V_1 = 20$ mL of 50% glucose, made up with $100 - 20 = 80$ mL of water to a total of 100 mL.

</details>

6. A protocol asks for 8 mEq of magnesium. How many mmol of Mg²⁺ is that, and roughly how many grams of magnesium sulfate heptahydrate (about 4 mmol Mg²⁺ per g)?

<details>
<summary>Answer</summary>

Mg²⁺ has valence 2, so $8\ \text{mEq} / 2 = 4$ mmol. At about 4 mmol per gram that is about 1 g of magnesium sulfate heptahydrate (more precisely $4 \times 246.5/1000 \approx 0.99$ g).

</details>

7. Rewrite each order safely: (a) ".5 mg", (b) "5.0 mg", (c) "100 µg", (d) "6 U insulin".

<details>
<summary>Answer</summary>

(a) 0.5 mg. (b) 5 mg. (c) 100 micrograms. (d) 6 units insulin.

</details>

8. A 12 kg child is prescribed 6 mg of an illustrative Drug X. The stock is 10 mg/mL. A colleague has drawn up 6 mL. Estimate the correct volume, and say what kind of error has happened.

<details>
<summary>Answer</summary>

$6\ \text{mg} / 10\ \text{mg/mL} = 0.6$ mL. 6 mL would deliver 60 mg, a **10-fold overdose**, probably from a lost decimal point ("0.6" read as "6"). The estimate "less than 1 mL, because the dose is less than one mL's worth of drug" would have caught it.

</details>

## Further reading

- Joint Formulary Committee. *British National Formulary* (BNF) and *BNF for Children* (BNFc). BMJ Group and Pharmaceutical Press, updated continuously. The "Guidance on prescribing" sections cover safe-writing rules.
- Institute for Safe Medication Practices (ISMP). *List of Error-Prone Abbreviations, Symbols, and Dose Designations.* ismp.org.
- Lapham, R. *Drug Calculations for Nurses: A Step-by-Step Approach.* CRC Press. A gentle book of worked problems on units, dilutions and infusions.
- In this course: [ratios](../../arithmetic/ratios/) and [mixtures](../../word-problems/mixtures-and-interest/) for the algebra behind dilutions.
