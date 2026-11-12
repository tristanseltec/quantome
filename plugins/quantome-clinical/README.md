# quantome-clinical (preview)

Verified clinical calculations for **healthcare professionals**, as Claude Code skills.
Every number comes from tested code (the single-source `quantome` Python library), and every answer shows its
inputs, working, caveats, sources and **verification level**.

```bash
/plugin marketplace add tristanseltec/quantome
/plugin install quantome-clinical@quantome
```

| Skill | Calculates |
|---|---|
| `iv-fluids` | Holliday–Segar maintenance (4-2-1 and 100/50/20), dehydration deficit, Parkland burns |
| `dose-calculation` | mg/kg dose with maximum cap and stock volume; IBW (Devine), adjusted BW, BSA (Mosteller, Du Bois); Cockcroft–Gault, bedside Schwartz |
| `nutrition-calculations` | GIR and target rearrangements; infant enteral + PN per-kg summary; Mifflin–St Jeor |
| `paediatric-growth` | BMI-for-age z-score, centile, CDC category and % of the 95th centile (official CDC LMS data) |

The `clinical-calc-checker` subagent gives an independent second check of any calculation.

## Safety design

- **Compute, don't guess.** Skills must run the scripts and never do arithmetic in the model.
- **Refuses** inputs outside validated ranges (e.g. weights in grams, neonates for Holliday–Segar).
- **Never supplies drug doses.** mg/kg values and maxima must come from the user's formulary.
- **No identifiable patient data.**
- **Preview status.** All formulas are currently **L1 (machine-verified)**. Version 1.0 requires every formula to reach **L2 (expert-reviewed)**; see [docs/VISION.md](../../docs/VISION.md) and [issue #1](https://github.com/tristanseltec/quantome/issues/1).

> [!CAUTION]
> Educational and decision-support software for professionals, not a medical device. Verify every result against
> your local protocol and use independent double-checks.

Requirements: Python ≥ 3.11 (standard library only). Licence: Apache-2.0.
Don't edit `lib/`: it is generated from `py/src/quantome` by `scripts/sync_plugins.py`.
