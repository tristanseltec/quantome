"""Growth references: the LMS method and CDC 2000 BMI-for-age (2–20 years)."""

from __future__ import annotations

import csv
import math
from functools import cache
from importlib import resources

from .._core import OutOfRange, Result, check_range


def lms_z(x: float, L: float, M: float, S: float) -> float:
    """Cole (1990): z = ((x/M)^L − 1)/(L·S), or ln(x/M)/S when L = 0."""
    if x <= 0 or M <= 0 or S <= 0:
        raise OutOfRange("x, M and S must be positive")
    if abs(L) < 1e-12:
        return math.log(x / M) / S
    return ((x / M) ** L - 1) / (L * S)


def lms_value(z: float, L: float, M: float, S: float) -> float:
    """Inverse LMS: the measurement at a given z-score."""
    if abs(L) < 1e-12:
        return M * math.exp(S * z)
    return M * (1 + L * S * z) ** (1 / L)


def centile(z: float) -> float:
    """Standard-normal CDF × 100."""
    return 50 * (1 + math.erf(z / math.sqrt(2)))


@cache
def _cdc_bmi() -> dict[tuple[int, float], dict[str, float]]:
    text = resources.files("quantome").joinpath("data/cdc_bmiagerev.csv").read_text(encoding="utf-8")
    rows = {}
    for row in csv.DictReader(text.splitlines()):
        if row["Sex"] == "Sex":  # the CDC file repeats its header partway through
            continue
        rows[(int(row["Sex"]), float(row["Agemos"]))] = {k: float(v) for k, v in row.items() if k not in {"Sex", "Agemos"}}
    return rows


def cdc_bmi_for_age(sex: str, age_months: float, weight_kg: float, height_cm: float) -> Result:
    """BMI z-score, centile and CDC category for ages 2–20 years (CDC 2000 LMS)."""
    key = str(sex).strip().lower()
    if key not in {"m", "male", "f", "female"}:
        raise ValueError("sex must be 'M' or 'F'")
    sex_code = 1 if key.startswith("m") else 2
    age = check_range("age", age_months, 24, 240, "months")
    w = check_range("weight", weight_kg, 5, 250, "kg")
    h = check_range("height", height_cm, 70, 220, "cm")
    bmi = w / (h / 100) ** 2
    completed = math.floor(age)
    agemos = 240.0 if completed >= 240 else completed + 0.5  # half-month rows = completed months
    row = _cdc_bmi()[(sex_code, agemos)]
    L, M, S = row["L"], row["M"], row["S"]
    z = lms_z(bmi, L, M, S)
    c = centile(z)
    pct_of_p95 = 100 * bmi / row["P95"]
    if c < 5:
        cat = "underweight (< 5th centile)"
    elif c < 85:
        cat = "healthy weight (5th to < 85th)"
    elif c < 95:
        cat = "overweight (85th to < 95th)"
    elif pct_of_p95 < 120:
        cat = "obesity (≥ 95th centile)"
    elif pct_of_p95 < 140:
        cat = "severe obesity, class 2 (≥ 120 % of the 95th centile)"
    else:
        cat = "severe obesity, class 3 (≥ 140 % of the 95th centile)"
    working = [
        f"BMI = {w:g} / ({h / 100:g})² = {bmi:.2f} kg/m²",
        f"CDC row: sex {sex_code}, Agemos {agemos:g} → L = {L:.4f}, M = {M:.4f}, S = {S:.5f}",
        f"z = (({bmi:.2f}/{M:.4f})^{L:.4f} − 1)/({L:.4f}×{S:.5f}) = {z:+.2f}",
        f"Centile = 100·Φ({z:.2f}) = {c:.1f}; published P85 = {row['P85']:.2f}, P95 = {row['P95']:.2f}",
        f"BMI is {pct_of_p95:.0f} % of the 95th centile",
    ]
    warnings = []
    if abs(z) > 3:
        warnings.append("|z| > 3: LMS z-scores are compressed at extremes; use % of the 95th centile for severe obesity.")
    return Result(
        "clin.growth.cdc_bmi_for_age",
        {"bmi": round(bmi, 2), "z": round(z, 2), "centile": round(c, 1),
         "percent_of_p95": round(pct_of_p95, 1), "cdc_category": cat},
        {"sex": sex, "age_months": age, "weight_kg": w, "height_cm": h},
        working,
        warnings,
    )
