---
name: verify-chapter
description: Verify a Quantome textbook chapter before a PR. It runs every Python block, checks that each shown output matches the real output, recomputes worked-example and practice numbers, and runs the site's `book check` (links, answer blocks, front matter). Use when asked to "verify", "check", or "test" a chapter, or before committing any change under content/.
---

# Verify a Quantome chapter

Work from the repository root.

1. **Run the code blocks** (blocks run in order as one program by default):
   ```bash
   python3 <this skill's dir>/scripts/run_code_blocks.py content/modules/<module>/<chapter>.md --python <python with numpy/sklearn/torch>
   ```
   - `✗ shown output differs` → paste the *real* output into the ```` ```text ```` block, unless the code is wrong, in which case fix the code.
   - Add `--isolated` if the blocks are meant to be independent.
   - If no environment has the libraries: `python -m venv .venv && .venv/bin/pip install numpy scikit-learn torch`.
2. **Recompute the numbers in prose.** For every worked example and every `<details>` answer, write a short
   script that recomputes the stated numbers, and fix any that disagree. Don't trust arithmetic done in prose.
3. **Build and validate the site:**
   ```bash
   cargo run --release -p book-cli -- check
   ```
   Fix every reported problem: broken or absolute links, unbalanced `<details>`, missing `summary`.
4. **If you changed the shared library** (`py/`): run `cd py && python -m pytest`, then
   `python3 scripts/sync_plugins.py --check`.
5. **Report** a short table: blocks run (pass/fail), numbers recomputed, `book check` result, and anything unverified.
