"""Shared machinery: range checks, provenance-carrying results, and the registry."""

from __future__ import annotations

import tomllib
from dataclasses import dataclass, field
from functools import cache
from importlib import resources

BOOK_URL = "https://tristanseltec.github.io/quantome/"


class OutOfRange(ValueError):
    """Raised when an input lies outside the formula's validated range."""


def check_range(name: str, value: float, lo: float, hi: float, unit: str = "") -> float:
    if not isinstance(value, (int, float)) or value != value:  # rejects NaN
        raise OutOfRange(f"{name} must be a number, got {value!r}")
    if not lo <= value <= hi:
        raise OutOfRange(
            f"{name} = {value}{(' ' + unit) if unit else ''} is outside the validated range "
            f"[{lo}, {hi}]{(' ' + unit) if unit else ''}. Check the units; this formula does not extrapolate."
        )
    return float(value)


@cache
def _registry() -> dict:
    text = resources.files("quantome").joinpath("registry.toml").read_text(encoding="utf-8")
    return tomllib.loads(text)["formula"]


def registry_entry(formula_id: str) -> dict:
    """Metadata for a formula: title, sources, level, chapter, caveats."""
    try:
        return _registry()[formula_id]
    except KeyError:
        raise KeyError(f"{formula_id!r} is not in registry.toml") from None


@dataclass
class Result:
    """A value plus everything a professional needs to check it."""

    formula_id: str
    value: dict
    inputs: dict
    working: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    @property
    def meta(self) -> dict:
        return registry_entry(self.formula_id)

    def to_dict(self) -> dict:
        m = self.meta
        return {
            "formula_id": self.formula_id,
            "title": m["title"],
            "inputs": self.inputs,
            "result": self.value,
            "working": self.working,
            "warnings": self.warnings,
            "caveats": m.get("caveats", []),
            "sources": m["sources"],
            "verification_level": m["level"],
            "chapter": f"{BOOK_URL}{m['chapter']}/" if m.get("chapter") else None,
        }

    def render(self) -> str:
        d = self.to_dict()
        lines = [f"{d['title']}  [{d['formula_id']} · verification {d['verification_level']}]", ""]
        lines += ["Inputs:"] + [f"  {k}: {v}" for k, v in d["inputs"].items()]
        lines += ["", "Working:"] + [f"  {w}" for w in d["working"]]
        lines += ["", "Result:"] + [f"  {k}: {v}" for k, v in d["result"].items()]
        if d["warnings"]:
            lines += ["", "⚠ Warnings:"] + [f"  - {w}" for w in d["warnings"]]
        lines += ["", "Caveats:"] + [f"  - {c}" for c in d["caveats"]]
        lines += ["", "Sources:"] + [f"  - {s}" for s in d["sources"]]
        if d["chapter"]:
            lines += [f"Explained in: {d['chapter']}"]
        lines += ["", "Professional use only: verify against your local protocol before acting."]
        return "\n".join(lines)
