# Additional rules for clinical content (Part VI and any dosing, fluid or nutrition numbers)

Quantome's clinical content is **professional-facing**: for medical students, doctors, nurses, pharmacists and dietitians.

1. Put a `> [!CAUTION]` box near the top of every clinical chapter saying that the examples teach arithmetic, not
   prescribing. Readers must check the current local formulary or guideline (e.g. BNF/BNFc, national guidance,
   hospital protocols) and use independent double-checks.
2. Use generic, illustrative drugs ("Drug X, 10 mg/kg, max 500 mg per dose, stock 250 mg/5 mL"). State a real
   drug's dose only if it is standard and verified against an official source, and label it with that source.
3. Give worked examples across **patient profiles**: infant (only where you are sure of the numbers), child,
   adolescent, adult, older adult with renal impairment, and obese adult.
4. Every formula must be standard and correctly attributed. Every number must be recomputed with code.
5. No invented guideline thresholds. If unsure, describe the threshold qualitatively and point to the source.
6. Prefer SI units and show conversions (creatinine mg/dL × 88.4 = µmol/L).
7. Neonatal numbers: only well-sourced values. Otherwise say "follow your unit's neonatal protocol".
8. Never remove existing safety caveats.
9. Request a **clinical reviewer** on the PR (label `clinical-review`). Clinical content is not merged without one.
