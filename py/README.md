# quantome (Python)

The **single source of truth** for every formula in Quantome. The book chapters teach these formulas,
and the Claude Code skills in `plugins/` run them. A copy of this package is vendored into each plugin
by `scripts/sync_plugins.py`, and CI fails if the copies drift from this source.

- Standard library only (Python ≥ 3.11), so skills run anywhere without installing anything.
- Every public function has an entry in `src/quantome/registry.toml`: its source, units, validated input
  range, the chapter that teaches it, and its **verification level** (see `docs/VISION.md`).
- Inputs outside the validated range raise `OutOfRange`. The functions don't extrapolate.

```bash
cd py && python -m pip install -e '.[test]' && python -m pytest
python -m quantome.cli fluids --weight 25           # human-readable working
python -m quantome.cli bmi-z --sex F --age-months 120 --weight 40 --height-cm 140 --json
```

> Professional use only. These are educational reference implementations, not a medical device.
> Verify every result against local protocols.
