"""Maintenance fluids (Holliday–Segar), deficits and burns (Parkland)."""

from __future__ import annotations

from .._core import Result, check_range


def holliday_segar(weight_kg: float, age_days: float | None = None) -> Result:
    """Maintenance water: daily 100/50/20 mL/kg/day and hourly 4-2-1 mL/kg/h forms."""
    w = check_range("weight", weight_kg, 3, 120, "kg")
    if age_days is not None and check_range("age", age_days, 0, 50_000, "days") < 28:
        from .._core import OutOfRange

        raise OutOfRange("Neonates (< 28 days) follow day-of-life neonatal fluid protocols, not Holliday–Segar.")

    daily = 100 * min(w, 10) + 50 * min(max(w - 10, 0), 10) + 20 * max(w - 20, 0)
    hourly = 4 * min(w, 10) + 2 * min(max(w - 10, 0), 10) + 1 * max(w - 20, 0)
    working = [
        f"Daily (100/50/20): 100×{min(w, 10):g} + 50×{min(max(w - 10, 0), 10):g} + 20×{max(w - 20, 0):g} = {daily:g} mL/day"
        f" = {daily / 24:.1f} mL/h",
        f"Hourly (4-2-1): 4×{min(w, 10):g} + 2×{min(max(w - 10, 0), 10):g} + 1×{max(w - 20, 0):g} = {hourly:g} mL/h"
        f" = {hourly * 24:g} mL/day",
    ]
    warnings = []
    if w >= 50:
        warnings.append(
            "Adult-sized patient: adult guidance (e.g. NICE CG174) uses 25–30 mL/kg/day, and ideal body weight in obesity. "
            f"25–30 mL/kg/day here = {25 * w:g}–{30 * w:g} mL/day."
        )
    return Result(
        "clin.fluids.holliday_segar",
        {"daily_mL_per_day": round(daily, 1), "daily_form_mL_per_h": round(daily / 24, 1), "hourly_4_2_1_mL_per_h": round(hourly, 1)},
        {"weight_kg": w, "age_days": age_days},
        working,
        warnings,
    )


def dehydration_deficit(weight_kg: float, percent_dehydration: float) -> Result:
    """Deficit (mL) = % dehydration × weight (kg) × 10."""
    w = check_range("weight", weight_kg, 3, 120, "kg")
    p = check_range("dehydration", percent_dehydration, 0, 15, "%")
    deficit = p * w * 10
    return Result(
        "clin.fluids.deficit",
        {"deficit_mL": round(deficit, 1)},
        {"weight_kg": w, "percent_dehydration": p},
        [f"{p:g} % × {w:g} kg × 10 = {deficit:g} mL"],
    )


def parkland(weight_kg: float, tbsa_percent: float, hours_since_burn: float = 0.0) -> Result:
    """Parkland: 4 mL × kg × %TBSA over 24 h; half in the first 8 h *from the time of the burn*."""
    w = check_range("weight", weight_kg, 3, 200, "kg")
    t = check_range("TBSA", tbsa_percent, 1, 100, "%")
    h = check_range("hours since burn", hours_since_burn, 0, 7.99, "h")
    total = 4 * w * t
    first_half = total / 2
    remaining_hours = 8 - h
    rate_first = first_half / remaining_hours
    rate_second = first_half / 16
    working = [
        f"Total 24 h = 4 × {w:g} kg × {t:g} % = {total:g} mL",
        f"First half {first_half:g} mL over the remaining {remaining_hours:g} h of the first 8 h → {rate_first:.0f} mL/h",
        f"Second half {first_half:g} mL over 16 h → {rate_second:.0f} mL/h",
    ]
    warnings = ["Titrate to urine output and clinical response; the formula is a starting estimate."]
    if h > 0:
        warnings.append("Assumes no resuscitation fluid has been given yet; subtract any already given.")
    return Result(
        "clin.fluids.parkland",
        {"total_24h_mL": round(total), "first_8h_rate_mL_per_h": round(rate_first), "next_16h_rate_mL_per_h": round(rate_second)},
        {"weight_kg": w, "tbsa_percent": t, "hours_since_burn": h},
        working,
        warnings,
    )
