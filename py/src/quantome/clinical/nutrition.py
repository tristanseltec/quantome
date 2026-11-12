"""Glucose infusion rate, infant/neonatal regimen summaries and adult energy estimates."""

from __future__ import annotations

from .._core import Result, check_range

DEXTROSE_KCAL_PER_G = 3.4      # dextrose monohydrate convention
AMINO_ACID_KCAL_PER_G = 4.0
LIPID_20PCT_KCAL_PER_ML = 2.0  # approximate; includes glycerol and phospholipid
MAX_PERIPHERAL_DEXTROSE_PCT = 12.5  # a common unit rule, not a guideline value


def gir(dextrose_pct: float, rate_ml_h: float, weight_kg: float, target_gir: float | None = None) -> Result:
    """GIR (mg/kg/min) = dextrose% × rate(mL/h) × 10 / (60 × weight); optional rearrangements for a target."""
    d = check_range("dextrose concentration", dextrose_pct, 0, 50, "%")
    r = check_range("rate", rate_ml_h, 0, 500, "mL/h")
    w = check_range("weight", weight_kg, 0.3, 150, "kg")
    g = d * r * 10 / (60 * w)
    working = [f"{d:g} × {r:g} × 10 / (60 × {w:g}) = {g:.2f} mg/kg/min",
               f"= {g * 1.44:.2f} g/kg/day"]
    value = {"gir_mg_kg_min": round(g, 2)}
    warnings = []
    if target_gir is not None:
        t = check_range("target GIR", target_gir, 0.5, 20, "mg/kg/min")
        if r > 0:
            need_pct = t * 60 * w / (r * 10)
            value["dextrose_pct_for_target_at_same_rate"] = round(need_pct, 1)
            working.append(f"Dextrose % for {t:g} at {r:g} mL/h = {t:g}×60×{w:g}/({r:g}×10) = {need_pct:.1f} %")
            if need_pct > MAX_PERIPHERAL_DEXTROSE_PCT:
                warnings.append(f"{need_pct:.1f} % exceeds the common peripheral limit of ~{MAX_PERIPHERAL_DEXTROSE_PCT} %: central access needed, or change volume/target.")
        if d > 0:
            need_rate = t * 60 * w / (d * 10)
            value["rate_mL_h_for_target_at_same_pct"] = round(need_rate, 2)
            working.append(f"Rate for {t:g} at {d:g} % = {t:g}×60×{w:g}/({d:g}×10) = {need_rate:.2f} mL/h"
                           f" ({need_rate * 24 / w:.1f} mL/kg/day)")
    if g > 12:
        warnings.append("GIR above ~12 mg/kg/min exceeds commonly quoted infant maxima (ESPGHAN 2018).")
    return Result("clin.nutrition.gir", value,
                  {"dextrose_pct": d, "rate_mL_h": r, "weight_kg": w, "target_gir": target_gir}, working, warnings)


def infant_regimen(
    weight_kg: float,
    enteral_ml_kg_day: float = 0.0,
    milk_kcal_per_100ml: float = 67.0,
    milk_protein_g_per_100ml: float = 1.3,
    aqueous_ml_h: float = 0.0,
    dextrose_pct: float = 0.0,
    amino_acid_pct: float = 0.0,
    lipid20_ml_h: float = 0.0,
) -> Result:
    """Per-kg fluid, energy (by source), protein, lipid and GIR for enteral + PN combinations."""
    w = check_range("weight", weight_kg, 0.3, 15, "kg")
    ent_ml = check_range("enteral volume", enteral_ml_kg_day, 0, 250, "mL/kg/day") * w
    aq_ml = check_range("aqueous rate", aqueous_ml_h, 0, 100, "mL/h") * 24
    lip_ml = check_range("lipid 20% rate", lipid20_ml_h, 0, 20, "mL/h") * 24
    kc = check_range("milk energy", milk_kcal_per_100ml, 40, 130, "kcal/100 mL")
    pr = check_range("milk protein", milk_protein_g_per_100ml, 0.5, 4, "g/100 mL")
    dp = check_range("dextrose", dextrose_pct, 0, 30, "%")
    ap = check_range("amino acids", amino_acid_pct, 0, 6, "%")
    kcal = {
        "enteral": ent_ml * kc / 100,
        "dextrose": aq_ml * dp / 100 * DEXTROSE_KCAL_PER_G,
        "amino_acids": aq_ml * ap / 100 * AMINO_ACID_KCAL_PER_G,
        "lipid": lip_ml * LIPID_20PCT_KCAL_PER_ML,
    }
    protein = ent_ml * pr / 100 + aq_ml * ap / 100
    g = dp * aqueous_ml_h * 10 / (60 * w)
    value = {
        "fluid_mL_kg_day": round((ent_ml + aq_ml + lip_ml) / w, 1),
        "energy_kcal_kg_day": round(sum(kcal.values()) / w, 1),
        "energy_by_source_kcal_kg_day": {k: round(v / w, 1) for k, v in kcal.items() if v},
        "protein_g_kg_day": round(protein / w, 2),
        "lipid_g_kg_day": round(lip_ml * 0.2 / w, 2),
        "gir_mg_kg_min": round(g, 2),
    }
    working = [
        f"Enteral {ent_ml:g} mL/day × {kc:g}/100 kcal = {kcal['enteral']:.1f} kcal",
        f"Aqueous {aq_ml:g} mL/day: dextrose {aq_ml * dp / 100:.2f} g × 3.4, amino acids {aq_ml * ap / 100:.2f} g × 4",
        f"Lipid 20 % {lip_ml:g} mL/day × 2 kcal/mL = {kcal['lipid']:.1f} kcal ({lip_ml * 0.2:.2f} g)",
        "All totals divided by weight; add drug/line fluids separately to the fluid total.",
    ]
    warnings = []
    if value["lipid_g_kg_day"] > 4:
        warnings.append("Lipid above 4 g/kg/day exceeds the ESPGHAN 2018 upper limit for infants.")
    if g > 12:
        warnings.append("GIR above ~12 mg/kg/min exceeds commonly quoted infant maxima.")
    if dp > MAX_PERIPHERAL_DEXTROSE_PCT:
        warnings.append(f"Dextrose {dp:g} % exceeds a common peripheral limit (~12.5 %): central access needed.")
    inputs = dict(weight_kg=w, enteral_ml_kg_day=enteral_ml_kg_day, milk_kcal_per_100ml=kc,
                  milk_protein_g_per_100ml=pr, aqueous_ml_h=aqueous_ml_h, dextrose_pct=dp,
                  amino_acid_pct=ap, lipid20_ml_h=lipid20_ml_h)
    return Result("clin.nutrition.infant_regimen", value, inputs, working, warnings)


def mifflin_st_jeor(weight_kg: float, height_cm: float, age_years: float, sex: str) -> Result:
    """REE (kcal/day) = 10W + 6.25H − 5A + 5 (men) or − 161 (women). Adults only."""
    w = check_range("weight", weight_kg, 30, 300, "kg")
    h = check_range("height", height_cm, 120, 230, "cm")
    a = check_range("age", age_years, 18, 110, "years")
    key = str(sex).strip().lower()
    if key not in {"m", "male", "f", "female"}:
        raise ValueError("sex must be 'M' or 'F'")
    s = 5 if key.startswith("m") else -161
    ree = 10 * w + 6.25 * h - 5 * a + s
    return Result("clin.nutrition.mifflin_st_jeor", {"ree_kcal_day": round(ree)},
                  {"weight_kg": w, "height_cm": h, "age_years": a, "sex": sex},
                  [f"10×{w:g} + 6.25×{h:g} − 5×{a:g} {'+ 5' if s == 5 else '− 161'} = {ree:.0f} kcal/day"],
                  ["Resting energy only: apply activity/stress factors as your protocol directs. Not for children or critical illness."])
