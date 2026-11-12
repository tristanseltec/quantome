---
name: iv-fluids
description: Calculate maintenance IV fluid volumes and rates with the Holliday–Segar method (100/50/20 mL/kg/day and 4-2-1 mL/kg/h), dehydration deficits, and Parkland burns resuscitation volumes, for children and adults (not neonates). Use when a healthcare professional asks for "maintenance fluids", "fluid rate for a X kg child", "4-2-1 rule", "Holliday-Segar", "fluid deficit", "% dehydration" or "Parkland formula".
---

# IV fluids (Holliday–Segar, deficit, Parkland)

**Audience: healthcare professionals.** Results support, and never replace, clinical judgement and the local protocol.

## Rules (non-negotiable)

1. **Compute with the script, never mentally.** Every number you report must come from `scripts/qcalc.py` in this skill's directory.
2. **Never guess an input.** If weight, age (to exclude neonates), %TBSA or hours since the burn are missing, ask for them. Don't use "typical" weights.
3. **Never accept identifiable patient data.** If you are given names, dates of birth or hospital numbers, don't repeat or store them; work only with the clinical numbers.
4. If the script **refuses** an input (exit code 2, `REFUSED`), explain why and don't work around it. Neonates (< 28 days) need neonatal day-of-life protocols.
5. Always show the **inputs, working, result, caveats, sources and verification level** that the script prints. Keep the caveats; don't paraphrase them away.

## Commands

Run from this skill's base directory (Python ≥ 3.11, standard library only):

```bash
python3 scripts/qcalc.py fluids   --weight <kg> [--age-days <days>]
python3 scripts/qcalc.py deficit  --weight <kg> --percent <% dehydration>
python3 scripts/qcalc.py parkland --weight <kg> --tbsa <%> [--hours-since-burn <h>]
```

Add `--json` before the subcommand for machine-readable output.

## How to answer

1. Restate the inputs with units.
2. Give the result: for maintenance, both mL/h (4-2-1) and mL/day (100/50/20), noting they differ slightly.
3. Include the working lines from the script.
4. Include the caveats, especially **isotonic fluids**, **50–80 % restriction when ADH is raised**, and **adult guidance of 25–30 mL/kg/day** for adult-sized patients.
5. End with: *"Verify against your local protocol; this is preview software (verification level L1, not yet expert-reviewed)."*
6. For total fluid plans (maintenance + deficit + ongoing losses), run each part separately and add them, showing the sum.

Teaching chapter: https://tristanseltec.github.io/quantome/clinical-mathematics/maintenance-fluids-holliday-segar/
