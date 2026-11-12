#!/usr/bin/env python3
"""Vendor the single-source `py/src/quantome` package into plugins that need it.

    python3 scripts/sync_plugins.py          # copy
    python3 scripts/sync_plugins.py --check  # exit 1 if any vendored copy has drifted (CI)

Plugins are installed as self-contained directories, so each one carries its own copy of the
library. The copy is generated: never edit files under plugins/*/lib/ directly.
"""
import filecmp
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "py" / "src" / "quantome"
TARGETS = [ROOT / "plugins" / name / "lib" / "quantome" for name in ("quantome-clinical", "quantome-math")]
IGNORE = shutil.ignore_patterns("__pycache__", "*.pyc")


def drift(a: Path, b: Path) -> list[str]:
    if not b.exists():
        return [f"{b} missing"]
    cmp = filecmp.dircmp(a, b, ignore=["__pycache__"])
    out = [f"{b}/{n}: differs" for n in cmp.diff_files]
    out += [f"{b}/{n}: missing" for n in cmp.left_only]
    out += [f"{b}/{n}: extra" for n in cmp.right_only]
    for sub in cmp.common_dirs:
        out += drift(a / sub, b / sub)
    return out


def main() -> int:
    if "--check" in sys.argv:
        problems = [p for t in TARGETS for p in drift(SOURCE, t)]
        for p in problems:
            print("drift:", p)
        print("vendored libraries in sync" if not problems else "run: python3 scripts/sync_plugins.py")
        return 1 if problems else 0
    for t in TARGETS:
        if t.exists():
            shutil.rmtree(t)
        shutil.copytree(SOURCE, t, ignore=IGNORE)
        (t.parent / "GENERATED.md").write_text(
            "Generated from `py/src/quantome` by `scripts/sync_plugins.py`. Do not edit here.\n")
        print("synced", t.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
