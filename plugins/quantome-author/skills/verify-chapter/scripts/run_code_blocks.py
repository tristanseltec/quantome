#!/usr/bin/env python3
"""Run every ```python block in a Quantome chapter and compare with the ```text output shown after it.

    python3 run_code_blocks.py CHAPTER.md [--python PYTHON] [--isolated] [--timeout SECONDS]

By default the blocks run in order as ONE program, because chapters build on earlier blocks. Each block's
stdout is compared with the first ```text block that follows it, before the next ```python block.
Use --isolated to run each block on its own.

Exit code: 0 all blocks ran and shown outputs match · 1 a mismatch or an error · 2 bad usage.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
import tempfile
from pathlib import Path

FENCE = re.compile(r"^```(\w*)[^\n]*\n(.*?)^```", re.M | re.S)
MARK = "@@QUANTOME_BLOCK_END_{}@@"


def parse(md: str) -> list[dict]:
    """Return python blocks, each with the expected text output (or None)."""
    blocks, current = [], None
    for m in FENCE.finditer(md):
        lang, body = m.group(1), m.group(2)
        line = md.count("\n", 0, m.start()) + 1
        if lang == "python":
            current = {"code": body, "line": line, "expected": None}
            blocks.append(current)
        elif lang == "text" and current is not None and current["expected"] is None:
            current["expected"] = body
    return blocks


def norm(s: str) -> list[str]:
    return [ln.rstrip() for ln in s.strip("\n").splitlines()]


def run(code: str, python: str, timeout: int, cwd: str) -> tuple[int, str, str]:
    p = subprocess.run([python, "-I", "-c", code], capture_output=True, text=True, timeout=timeout, cwd=cwd)
    return p.returncode, p.stdout, p.stderr


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("chapter", type=Path)
    ap.add_argument("--python", default=sys.executable)
    ap.add_argument("--isolated", action="store_true")
    ap.add_argument("--timeout", type=int, default=600)
    a = ap.parse_args()
    if not a.chapter.is_file():
        print(f"no such file: {a.chapter}")
        return 2
    blocks = parse(a.chapter.read_text(encoding="utf-8"))
    if not blocks:
        print("no python blocks")
        return 0

    outputs: list[str | None] = []
    failed = False
    with tempfile.TemporaryDirectory() as tmp:
        if a.isolated:
            for b in blocks:
                rc, out, err = run(b["code"], a.python, a.timeout, tmp)
                outputs.append(out if rc == 0 else None)
                if rc:
                    print(f"✗ block at line {b['line']}: error\n{err.strip()[-1500:]}")
                    failed = True
        else:
            program = "".join(f"{b['code']}\nprint({MARK.format(i)!r}, flush=True)\n" for i, b in enumerate(blocks))
            rc, out, err = run(program, a.python, a.timeout, tmp)
            parts = out.split("\n")
            chunk, i = [], 0
            for ln in parts:
                if ln == MARK.format(i):
                    outputs.append("\n".join(chunk))
                    chunk, i = [], i + 1
                else:
                    chunk.append(ln)
            if rc:
                bad = blocks[len(outputs)] if len(outputs) < len(blocks) else blocks[-1]
                print(f"✗ error in or after block at line {bad['line']}\n{err.strip()[-1500:]}")
                failed = True
            outputs += [None] * (len(blocks) - len(outputs))

    for b, out in zip(blocks, outputs):
        if out is None:
            continue
        if b["expected"] is None:
            print(f"✓ block at line {b['line']}: ran (no output shown in chapter)")
        elif norm(out) == norm(b["expected"]):
            print(f"✓ block at line {b['line']}: output matches")
        else:
            failed = True
            print(f"✗ block at line {b['line']}: shown output differs from real output")
            exp, got = norm(b["expected"]), norm(out)
            for k in range(max(len(exp), len(got))):
                e = exp[k] if k < len(exp) else "<none>"
                g = got[k] if k < len(got) else "<none>"
                if e != g:
                    print(f"    first difference at output line {k + 1}:\n      shown: {e}\n      real:  {g}")
                    break
    print(f"{len(blocks)} block(s): {'FAIL' if failed else 'PASS'}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
