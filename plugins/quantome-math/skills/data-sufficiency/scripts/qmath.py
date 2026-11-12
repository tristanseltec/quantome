#!/usr/bin/env python3
"""Exact, verifiable maths tools (Quantome): python3 qmath.py [--json] <command> ...  (see --help)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "lib"))  # plugin/lib (vendored, single source)
from quantome.mathcli import main  # noqa: E402

sys.exit(main())
