---
name: dose-calculation
description: Calculate weight-based drug doses (mg/kg with a maximum-dose cap) and the volume of stock solution to give, plus body-size descriptors (ideal body weight by Devine, adjusted body weight, body surface area by Mosteller and Du Bois) and renal function (Cockcroft–Gault creatinine clearance, bedside Schwartz paediatric eGFR). Use when a healthcare professional asks "what dose for a X kg patient", "mg/kg", "how many mL of a 250 mg/5 mL suspension", "BSA", "IBW", "adjusted body weight", "creatinine clearance" or "Schwartz eGFR".
---

# Dose calculation, body size and renal function

**Audience: healthcare professionals.** This skill does **arithmetic**. It does not choose drugs or doses.

## Rules (non-negotiable)

1. **The mg/kg value and the maximum dose must come from the user's current formulary** (e.g. BNF/BNFc, local guideline). If they aren't given, ask. Never supply a drug's dose from memory.
2. **Compute with the script, never mentally.** Report only numbers printed by `scripts/qcalc.py`.
3. **Never guess an input.** Ask for any missing weight, height, sex, age or creatinine. Convert creatinine in mg/dL to µmol/L by × 88.4, and state that you did.
4. **No identifiable patient data**: work only with clinical numbers.
5. If the script **refuses** (exit code 2), explain why. Don't override it.
6. Always state **which weight** was used (actual, ideal or adjusted), and remind the user to check which one the drug reference specifies.
7. If the result is **capped**, say so prominently.

## Commands

Run from this skill's base directory:

```bash
python3 scripts/qcalc.py dose   --weight <kg> --mg-per-kg <n> [--max-mg <n>] [--stock-mg <n> --stock-ml <n>]
python3 scripts/qcalc.py ibw    --height-cm <cm> --sex M|F
python3 scripts/qcalc.py adjbw  --total-kg <kg> --ibw-kg <kg> [--factor 0.4]
python3 scripts/qcalc.py bsa    --height-cm <cm> --weight <kg>
python3 scripts/qcalc.py crcl   --age <y> --weight <kg> --scr-umol <µmol/L> --sex M|F
python3 scripts/qcalc.py schwartz --height-cm <cm> --scr-umol <µmol/L>
```

For an obese adult, chain the calls: `ibw`, then `adjbw`, then `dose` or `crcl` with the weight the drug reference specifies.

## How to answer

Restate the inputs, then give the dose (and volume), the working, the warnings (cap applied?) and the caveats. End with:
*"Independent double-check required before administration. Preview software (verification L1, not yet expert-reviewed)."*

Teaching chapter: https://tristanseltec.github.io/quantome/clinical-mathematics/weight-and-body-size-based-dosing/
