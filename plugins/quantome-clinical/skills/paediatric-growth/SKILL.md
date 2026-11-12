---
name: paediatric-growth
description: Compute a child's BMI, BMI-for-age z-score and centile, and CDC weight category (including severe obesity as a percentage of the 95th centile) for ages 2–20 years, using the bundled official CDC 2000 LMS reference data; also explains the LMS method. Use when a healthcare professional asks for "BMI centile", "BMI z-score", "BMI-for-age", "is this child overweight", "percent of the 95th percentile", or "LMS".
---

# Paediatric growth: BMI-for-age (CDC 2000)

**Audience: healthcare professionals.** A single BMI is a screening result, not a diagnosis.

## Rules (non-negotiable)

1. **Compute with the script, never mentally.** It uses the official CDC `bmiagerev.csv` LMS table, bundled and tested against every published centile.
2. **Ages 24–240 months only.** Under 2 years, use WHO weight-for-length standards; this skill doesn't cover them. Ask for age in months if it is given in years and months (completed months).
3. **Reference choice matters.** These are **CDC (US)** references. Many countries use WHO (5–19 years: overweight > +1 SD, obesity > +2 SD) or UK-WHO/UK90 charts. Ask which reference the user's service uses. If it isn't CDC, say that this result is not directly comparable.
4. Never guess sex, age, weight or height. **No identifiable patient data.**
5. For **severe obesity**, report the **percentage of the 95th centile**, not just z: LMS z-scores are compressed at the extremes.

## Command

Run from this skill's base directory:

```bash
python3 scripts/qcalc.py bmi-z --sex M|F --age-months <completed months> --weight <kg> --height-cm <cm>
```

## How to answer

Give the BMI, z, centile, % of the 95th centile and CDC category, with the CDC row used (shown in the working) and the caveats. Recommend plotting serial measurements on the appropriate chart. End with:
*"Preview software (verification L1)."*

Teaching chapter: https://tristanseltec.github.io/quantome/clinical-mathematics/growth-and-bmi-in-children/
