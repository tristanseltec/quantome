#!/usr/bin/env python3
"""Run a verified Quantome calculation: python3 qcalc.py [--json] <command> [options]  (see --help)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "lib"))  # plugin/lib (vendored, single source)
from quantome.cli import main  # noqa: E402

sys.exit(main())
