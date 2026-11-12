"""Command-line entry point used by the Claude Code skills (and by humans).

    python -m quantome.cli fluids --weight 25
    python -m quantome.cli bmi-z --sex F --age-months 120 --weight 40 --height-cm 140 --json
"""

from __future__ import annotations

import argparse
import json
import sys

from ._core import OutOfRange
from .clinical import dosing, fluids, growth, nutrition


def _parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="quantome", description="Verified clinical calculations (professional use only).")
    p.add_argument("--json", action="store_true", help="machine-readable output")
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("fluids", help="Holliday–Segar maintenance fluids")
    s.add_argument("--weight", type=float, required=True, help="kg")
    s.add_argument("--age-days", type=float, help="refuses neonates (< 28 days)")

    s = sub.add_parser("deficit", help="dehydration deficit")
    s.add_argument("--weight", type=float, required=True)
    s.add_argument("--percent", type=float, required=True)

    s = sub.add_parser("parkland", help="burns resuscitation volume")
    s.add_argument("--weight", type=float, required=True)
    s.add_argument("--tbsa", type=float, required=True)
    s.add_argument("--hours-since-burn", type=float, default=0.0)

    s = sub.add_parser("dose", help="weight-based dose with cap and stock volume")
    s.add_argument("--weight", type=float, required=True)
    s.add_argument("--mg-per-kg", type=float, required=True)
    s.add_argument("--max-mg", type=float)
    s.add_argument("--stock-mg", type=float)
    s.add_argument("--stock-ml", type=float)

    s = sub.add_parser("ibw", help="ideal body weight (Devine)")
    s.add_argument("--height-cm", type=float, required=True)
    s.add_argument("--sex", required=True)

    s = sub.add_parser("adjbw", help="adjusted body weight")
    s.add_argument("--total-kg", type=float, required=True)
    s.add_argument("--ibw-kg", type=float, required=True)
    s.add_argument("--factor", type=float, default=0.4)

    s = sub.add_parser("bsa", help="body surface area")
    s.add_argument("--height-cm", type=float, required=True)
    s.add_argument("--weight", type=float, required=True)

    s = sub.add_parser("crcl", help="Cockcroft–Gault creatinine clearance")
    s.add_argument("--age", type=float, required=True)
    s.add_argument("--weight", type=float, required=True)
    s.add_argument("--scr-umol", type=float, required=True, help="µmol/L (mg/dL × 88.4)")
    s.add_argument("--sex", required=True)

    s = sub.add_parser("schwartz", help="bedside Schwartz paediatric eGFR")
    s.add_argument("--height-cm", type=float, required=True)
    s.add_argument("--scr-umol", type=float, required=True)

    s = sub.add_parser("gir", help="glucose infusion rate (+ target rearrangements)")
    s.add_argument("--dextrose-pct", type=float, required=True)
    s.add_argument("--rate", type=float, required=True, help="mL/h")
    s.add_argument("--weight", type=float, required=True)
    s.add_argument("--target", type=float)

    s = sub.add_parser("infant-regimen", help="per-kg summary of enteral + PN")
    s.add_argument("--weight", type=float, required=True)
    s.add_argument("--enteral-ml-kg-day", type=float, default=0.0)
    s.add_argument("--milk-kcal", type=float, default=67.0, help="kcal/100 mL")
    s.add_argument("--milk-protein", type=float, default=1.3, help="g/100 mL")
    s.add_argument("--aqueous-ml-h", type=float, default=0.0)
    s.add_argument("--dextrose-pct", type=float, default=0.0)
    s.add_argument("--aa-pct", type=float, default=0.0)
    s.add_argument("--lipid20-ml-h", type=float, default=0.0)

    s = sub.add_parser("ree", help="Mifflin–St Jeor resting energy expenditure")
    s.add_argument("--weight", type=float, required=True)
    s.add_argument("--height-cm", type=float, required=True)
    s.add_argument("--age", type=float, required=True)
    s.add_argument("--sex", required=True)

    s = sub.add_parser("bmi-z", help="CDC BMI-for-age z-score (2–20 y)")
    s.add_argument("--sex", required=True)
    s.add_argument("--age-months", type=float, required=True)
    s.add_argument("--weight", type=float, required=True)
    s.add_argument("--height-cm", type=float, required=True)
    return p


def _dispatch(a):
    match a.cmd:
        case "fluids": return fluids.holliday_segar(a.weight, a.age_days)
        case "deficit": return fluids.dehydration_deficit(a.weight, a.percent)
        case "parkland": return fluids.parkland(a.weight, a.tbsa, a.hours_since_burn)
        case "dose": return dosing.weight_based_dose(a.weight, a.mg_per_kg, a.max_mg, a.stock_mg, a.stock_ml)
        case "ibw": return dosing.ideal_body_weight_devine(a.height_cm, a.sex)
        case "adjbw": return dosing.adjusted_body_weight(a.total_kg, a.ibw_kg, a.factor)
        case "bsa": return dosing.bsa(a.height_cm, a.weight)
        case "crcl": return dosing.cockcroft_gault(a.age, a.weight, a.scr_umol, a.sex)
        case "schwartz": return dosing.schwartz_bedside(a.height_cm, a.scr_umol)
        case "gir": return nutrition.gir(a.dextrose_pct, a.rate, a.weight, a.target)
        case "infant-regimen":
            return nutrition.infant_regimen(a.weight, a.enteral_ml_kg_day, a.milk_kcal, a.milk_protein,
                                            a.aqueous_ml_h, a.dextrose_pct, a.aa_pct, a.lipid20_ml_h)
        case "ree": return nutrition.mifflin_st_jeor(a.weight, a.height_cm, a.age, a.sex)
        case "bmi-z": return growth.cdc_bmi_for_age(a.sex, a.age_months, a.weight, a.height_cm)


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        result = _dispatch(args)
    except (OutOfRange, ValueError) as e:
        msg = {"error": str(e)}
        print(json.dumps(msg) if args.json else f"REFUSED: {e}", file=sys.stdout)
        return 2
    print(json.dumps(result.to_dict(), indent=2, ensure_ascii=False) if args.json else result.render())
    return 0


if __name__ == "__main__":
    sys.exit(main())
