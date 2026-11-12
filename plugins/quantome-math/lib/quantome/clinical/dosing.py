"""Weight- and body-size-based dosing, body-size descriptors and renal function estimates."""

from __future__ import annotations

import math

from .._core import Result, check_range

UMOL_PER_MG_DL_CREATININE = 88.4


def weight_based_dose(
    weight_kg: float,
    mg_per_kg: float,
    max_dose_mg: float | None = None,
    stock_mg: float | None = None,
    stock_ml: float | None = None,
) -> Result:
    """Dose = mg/kg × weight, capped at max_dose_mg; optionally the volume of stock to give."""
    w = check_range("weight", weight_kg, 0.3, 250, "kg")
    d = check_range("dose per kg", mg_per_kg, 0.0001, 1000, "mg/kg")
    raw = w * d
    working = [f"{d:g} mg/kg × {w:g} kg = {raw:g} mg"]
    warnings = []
    dose = raw
    if max_dose_mg is not None:
        cap = check_range("maximum dose", max_dose_mg, 0.0001, 100_000, "mg")
        if raw > cap:
            dose = cap
            warnings.append(f"Calculated dose {raw:g} mg exceeds the maximum {cap:g} mg: capped at {cap:g} mg.")
            working.append(f"Capped at maximum dose {cap:g} mg")
    value = {"dose_mg": round(dose, 3), "capped": dose < raw}
    if stock_mg is not None or stock_ml is not None:
        if stock_mg is None or stock_ml is None:
            raise ValueError("give both stock_mg and stock_ml (e.g. 250 mg in 5 mL)")
        smg = check_range("stock amount", stock_mg, 0.0001, 100_000, "mg")
        sml = check_range("stock volume", stock_ml, 0.01, 1000, "mL")
        vol = dose * sml / smg
        working.append(f"Volume = {dose:g} mg × {sml:g} mL / {smg:g} mg = {vol:.3g} mL")
        value["volume_mL"] = round(vol, 3)
    return Result("clin.dosing.weight_based", value,
                  {"weight_kg": w, "mg_per_kg": d, "max_dose_mg": max_dose_mg, "stock": f"{stock_mg} mg / {stock_ml} mL"},
                  working, warnings)


def ideal_body_weight_devine(height_cm: float, sex: str) -> Result:
    """Devine (1974): 50 (male) / 45.5 (female) + 2.3 kg per inch over 60 inches."""
    h = check_range("height", height_cm, 152.4, 220, "cm")  # formula defined for ≥ 5 ft
    base = _sex_value(sex, male=50.0, female=45.5)
    inches = h / 2.54
    ibw = base + 2.3 * (inches - 60)
    return Result("clin.body.ibw_devine", {"ibw_kg": round(ibw, 1)}, {"height_cm": h, "sex": sex},
                  [f"{h:g} cm / 2.54 = {inches:.1f} in", f"{base:g} + 2.3 × ({inches:.1f} − 60) = {ibw:.1f} kg"])


def adjusted_body_weight(total_kg: float, ibw_kg: float, factor: float = 0.4) -> Result:
    """AdjBW = IBW + factor × (TBW − IBW); factor 0.4 is the common default."""
    t = check_range("total body weight", total_kg, 20, 350, "kg")
    i = check_range("ideal body weight", ibw_kg, 20, 150, "kg")
    f = check_range("factor", factor, 0.2, 0.6)
    adj = i + f * (t - i)
    warnings = [] if t > i else ["Total body weight ≤ IBW: adjusted body weight is not normally used."]
    return Result("clin.body.adjbw", {"adjusted_kg": round(adj, 1)}, {"total_kg": t, "ibw_kg": i, "factor": f},
                  [f"{i:g} + {f:g} × ({t:g} − {i:g}) = {adj:.1f} kg"], warnings)


def bsa(height_cm: float, weight_kg: float) -> Result:
    """Body surface area: Mosteller (1987) and Du Bois & Du Bois (1916)."""
    h = check_range("height", height_cm, 30, 250, "cm")
    w = check_range("weight", weight_kg, 0.5, 350, "kg")
    most = math.sqrt(h * w / 3600)
    dub = 0.007184 * w**0.425 * h**0.725
    return Result("clin.body.bsa", {"mosteller_m2": round(most, 3), "dubois_m2": round(dub, 3)},
                  {"height_cm": h, "weight_kg": w},
                  [f"Mosteller √({h:g}×{w:g}/3600) = {most:.3f} m²",
                   f"Du Bois 0.007184 × {w:g}^0.425 × {h:g}^0.725 = {dub:.3f} m²"])


def cockcroft_gault(age_years: float, weight_kg: float, scr_umol_l: float, sex: str) -> Result:
    """CrCl (mL/min) = (140 − age) × weight / (72 × SCr mg/dL) × 0.85 if female."""
    a = check_range("age", age_years, 18, 110, "years")
    w = check_range("weight", weight_kg, 30, 250, "kg")
    s = check_range("serum creatinine", scr_umol_l, 20, 2000, "µmol/L")
    female = _sex_value(sex, male=False, female=True)
    mgdl = s / UMOL_PER_MG_DL_CREATININE
    crcl = (140 - a) * w / (72 * mgdl) * (0.85 if female else 1.0)
    working = [f"SCr {s:g} µmol/L ÷ 88.4 = {mgdl:.3f} mg/dL",
               f"(140 − {a:g}) × {w:g} / (72 × {mgdl:.3f}){' × 0.85' if female else ''} = {crcl:.1f} mL/min"]
    return Result("clin.renal.cockcroft_gault", {"crcl_mL_min": round(crcl, 1)},
                  {"age_years": a, "weight_kg": w, "scr_umol_l": s, "sex": sex}, working,
                  ["State which weight you used (actual, ideal or adjusted); drug references differ."])


def schwartz_bedside(height_cm: float, scr_umol_l: float) -> Result:
    """Bedside Schwartz (2009): eGFR = 0.413 × height / SCr(mg/dL) = 36.5 × height / SCr(µmol/L)."""
    h = check_range("height", height_cm, 45, 200, "cm")
    s = check_range("serum creatinine", scr_umol_l, 10, 1500, "µmol/L")
    egfr = 0.413 * h / (s / UMOL_PER_MG_DL_CREATININE)
    return Result("clin.renal.schwartz_bedside", {"egfr_mL_min_1_73m2": round(egfr, 1)},
                  {"height_cm": h, "scr_umol_l": s},
                  [f"0.413 × {h:g} / ({s:g}/88.4) = {egfr:.1f} mL/min/1.73 m²"],
                  ["Assumes an enzymatic (IDMS-traceable) creatinine assay; intended for children."])


def _sex_value(sex: str, *, male, female):
    key = str(sex).strip().lower()
    if key in {"m", "male"}:
        return male
    if key in {"f", "female"}:
        return female
    raise ValueError("sex must be 'M' or 'F' (these equations use biological sex)")
