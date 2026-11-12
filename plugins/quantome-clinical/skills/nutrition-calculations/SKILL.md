---
name: nutrition-calculations
description: Calculate glucose infusion rate (GIR, mg/kg/min) and the dextrose concentration or rate needed for a target GIR; summarise infant and neonatal enteral + parenteral nutrition regimens per kg (fluid, energy by source, protein, lipid, GIR); and estimate adult resting energy expenditure (Mifflin–St Jeor). Use when a healthcare professional asks about "GIR", "glucose infusion rate", "dextrose 10% at X mL/h", "PN calories", "kcal/kg/day", "protein g/kg/day for a preterm baby", "enteral feeds", or "Mifflin-St Jeor".
---

# Nutrition calculations (GIR, infant regimens, adult REE)

**Audience: healthcare professionals** working with dietitians and pharmacists. Neonatal and infant nutrition is protocol-driven and specialist-led.

## Rules (non-negotiable)

1. **Compute with the script, never mentally.** Report only numbers printed by `scripts/qcalc.py`.
2. **Never guess** weight, rates, concentrations or milk composition. Ask for them. For milk energy and protein, use the product label or the dietitian's values. The defaults (67 kcal and 1.3 g per 100 mL) are only for standard term formula, so say when you used them.
3. **Target ranges come from the user's unit protocol.** You may mention the orientation ranges in the caveats, labelled as such, but never present them as the prescription.
4. Flag every **warning** the script prints (GIR > 12, dextrose above the peripheral limit, lipid > 4 g/kg/day) prominently.
5. **No identifiable patient data.**
6. Electrolytes, minerals and trace elements are **out of scope**. Say so if asked, and point to the specialist protocol.

## Commands

Run from this skill's base directory:

```bash
python3 scripts/qcalc.py gir --dextrose-pct <%> --rate <mL/h> --weight <kg> [--target <mg/kg/min>]
python3 scripts/qcalc.py infant-regimen --weight <kg> [--enteral-ml-kg-day <n> --milk-kcal <kcal/100mL> --milk-protein <g/100mL>] \
    [--aqueous-ml-h <n> --dextrose-pct <%> --aa-pct <%>] [--lipid20-ml-h <n>]
python3 scripts/qcalc.py ree --weight <kg> --height-cm <cm> --age <y> --sex M|F
```

When building a neonatal PN regimen, calculate the **lipid volume first** (g/kg/day ÷ 0.2 g/mL), subtract it and any drug or line fluids from the total allowance, then size the aqueous bag. Then verify the result with `infant-regimen`.

## How to answer

Inputs, then results per kg, working, warnings and caveats. End with:
*"Verify against your unit's nutrition protocol with the dietitian and pharmacist. Preview software (verification L1)."*

Teaching chapters:
- https://tristanseltec.github.io/quantome/clinical-mathematics/infant-and-neonatal-nutrition/
- https://tristanseltec.github.io/quantome/clinical-mathematics/nutrition-energy-and-parenteral-calculations/
