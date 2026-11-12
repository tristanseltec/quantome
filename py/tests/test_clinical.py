"""Golden values from the original sources and from the book's verified worked examples."""
import csv
import math
from importlib import resources

import pytest

from quantome import OutOfRange, registry_entry
from quantome.cli import main
from quantome.clinical import dosing, fluids, growth, nutrition


# --- Holliday–Segar (Holliday & Segar 1957; chapter 04) ---
@pytest.mark.parametrize("w, daily, hourly", [
    (3, 300, 12), (10, 1000, 40), (15, 1250, 50), (20, 1500, 60), (25, 1600, 65), (35, 1800, 75), (70, 2500, 110),
])
def test_holliday_segar(w, daily, hourly):
    r = fluids.holliday_segar(w).value
    assert r["daily_mL_per_day"] == daily
    assert r["hourly_4_2_1_mL_per_h"] == hourly


def test_holliday_segar_forms_agree_at_35kg_and_differ_4pct_below_20kg():
    r35 = fluids.holliday_segar(35).value
    assert r35["daily_form_mL_per_h"] == r35["hourly_4_2_1_mL_per_h"]
    r10 = fluids.holliday_segar(10).value
    assert r10["hourly_4_2_1_mL_per_h"] / r10["daily_form_mL_per_h"] == pytest.approx(0.96, abs=1e-3)


def test_refuses_neonates_and_bad_units():
    with pytest.raises(OutOfRange):
        fluids.holliday_segar(3.2, age_days=5)
    with pytest.raises(OutOfRange):
        fluids.holliday_segar(25000)  # grams by mistake
    with pytest.raises(OutOfRange):
        fluids.holliday_segar(float("nan"))


def test_deficit_and_parkland():
    assert fluids.dehydration_deficit(15, 5).value["deficit_mL"] == 750
    p = fluids.parkland(70, 20).value
    assert p["total_24h_mL"] == 5600
    assert p["first_8h_rate_mL_per_h"] == 350
    assert p["next_16h_rate_mL_per_h"] == 175
    late = fluids.parkland(70, 20, hours_since_burn=2).value
    assert late["first_8h_rate_mL_per_h"] == round(2800 / 6)


# --- Dosing and body size (chapter 02) ---
def test_weight_based_dose_cap_and_volume():
    r = dosing.weight_based_dose(12, 10, max_dose_mg=500, stock_mg=250, stock_ml=5).value
    assert r == {"dose_mg": 120, "capped": False, "volume_mL": 2.4}
    capped = dosing.weight_based_dose(65, 10, max_dose_mg=500)
    assert capped.value["dose_mg"] == 500 and capped.value["capped"] and capped.warnings


def test_body_size():
    assert dosing.bsa(170, 70).value["mosteller_m2"] == pytest.approx(1.818, abs=1e-3)
    assert dosing.bsa(170, 70).value["dubois_m2"] == pytest.approx(1.81, abs=0.01)
    assert dosing.ideal_body_weight_devine(180, "M").value["ibw_kg"] == pytest.approx(75.0, abs=0.1)
    assert dosing.adjusted_body_weight(130, 75.0).value["adjusted_kg"] == 97.0


def test_renal():
    # Chapter 02 worked example: 82-year-old woman, 60 kg, SCr 120 µmol/L → ~30 mL/min
    assert dosing.cockcroft_gault(82, 60, 120, "F").value["crcl_mL_min"] == pytest.approx(30.2, abs=0.2)
    # Bedside Schwartz: 140 cm, SCr 0.6 mg/dL (53.04 µmol/L) → 0.413×140/0.6 ≈ 96.4
    assert dosing.schwartz_bedside(140, 0.6 * 88.4).value["egfr_mL_min_1_73m2"] == pytest.approx(96.4, abs=0.1)


# --- Nutrition (chapters 05–06) ---
def test_gir_and_rearrangements():
    r = nutrition.gir(10, 7.5, 3.0, target_gir=6)
    assert r.value["gir_mg_kg_min"] == 4.17
    assert r.value["dextrose_pct_for_target_at_same_rate"] == 14.4
    assert r.value["rate_mL_h_for_target_at_same_pct"] == 10.8  # 6×60×3/(10×10)
    assert any("central" in w for w in r.warnings)


def test_infant_regimen_matches_chapter_example_2():
    v = nutrition.infant_regimen(1.2, aqueous_ml_h=5.25, dextrose_pct=10, amino_acid_pct=2.86, lipid20_ml_h=0.75).value
    assert v["fluid_mL_kg_day"] == 120.0
    assert v["energy_kcal_kg_day"] == 77.7
    assert v["protein_g_kg_day"] == pytest.approx(3.0, abs=0.01)
    assert v["lipid_g_kg_day"] == 3.0
    assert v["gir_mg_kg_min"] == 7.29


def test_mifflin():
    # 10×70 + 6.25×175 − 5×40 + 5 = 1598.75
    assert nutrition.mifflin_st_jeor(70, 175, 40, "M").value["ree_kcal_day"] == 1599


# --- Growth (chapter 07) ---
def test_cdc_bmi_chapter_example():
    v = growth.cdc_bmi_for_age("F", 120, 40, 140).value
    assert v["bmi"] == 20.41
    assert v["z"] == 1.14
    assert round(v["centile"]) == 87
    assert v["cdc_category"].startswith("overweight")


def test_lms_reproduces_every_published_centile():
    """Every P-column of all 438 CDC rows must be reproduced by the LMS inverse."""
    z_for = {"P3": -1.880794, "P5": -1.644854, "P10": -1.281552, "P25": -0.674490, "P50": 0.0,
             "P75": 0.674490, "P85": 1.036433, "P90": 1.281552, "P95": 1.644854, "P97": 1.880794}
    text = resources.files("quantome").joinpath("data/cdc_bmiagerev.csv").read_text()
    n = 0
    for row in csv.DictReader(text.splitlines()):
        if row["Sex"] == "Sex":
            continue
        L, M, S = (float(row[k]) for k in "LMS")
        for col, z in z_for.items():
            assert growth.lms_z(float(row[col]), L, M, S) == pytest.approx(z, abs=1e-5)
        n += 1
    assert n == 438


# --- Registry and CLI ---
def test_every_result_has_registry_metadata():
    for r in [fluids.holliday_segar(20), nutrition.gir(10, 5, 2), growth.cdc_bmi_for_age("M", 61, 20, 110)]:
        d = r.to_dict()
        assert d["sources"] and d["verification_level"] in {"L0", "L1", "L2", "L3"}


def test_cli_refuses_out_of_range(capsys):
    assert main(["fluids", "--weight", "2500"]) == 2
    assert "REFUSED" in capsys.readouterr().out
    assert main(["--json", "fluids", "--weight", "25"]) == 0
