# AGENTS.md: guide for AI agents

You're welcome to contribute to Quantome, an open mathematics textbook (GMAT quant → genomics and AI → clinical maths) published as a static site built with Rust + Leptos. This file tells you how to work here. Human contributors follow the same rules in [CONTRIBUTING.md](CONTRIBUTING.md).

## Repository map

| Path | What it is |
|---|---|
| `content/book.toml` | Book settings (title, base URL, module order) |
| `content/modules/NN-<module>/module.toml` | Module title, summary, `part` heading |
| `content/modules/NN-<module>/NN-<chapter>.md` | One chapter (TOML front matter between `+++`) |
| `crates/book-core` | Content loader, Markdown → HTML (pulldown-cmark), search index |
| `crates/book-ui` | Leptos components, server-rendered to static HTML |
| `crates/book-cli` | `book` binary: `build`, `serve`, `check`, `new` |
| `assets/` | `style.css`, `book.js` (KaTeX, Mermaid, highlight.js, search, progress) |

URL slugs are file and folder names without the numeric prefix: `content/modules/02-algebra/01-linear-equations.md` becomes `/algebra/linear-equations/`.

## Commands

```bash
cargo run --release -p book-cli -- check   # build + validate links/answers/front matter (REQUIRED)
cargo run --release -p book-cli -- build --out /tmp/<you>/dist   # build to a private dir if others build in parallel
cargo fmt --all && cargo clippy --workspace --all-targets -- -D warnings && cargo test --workspace   # Rust changes
python -I path/to/snippet.py               # run extracted code blocks (numpy, scikit-learn, torch)
```

## Workflow

1. **Pick a scope.** Choose an issue labelled `agent-friendly` or `good first issue`, or one clearly bounded task, such as one chapter, one fix or one feature. Don't start large rewrites without an issue.
2. **Read before writing.** Read the target module's existing chapters, and one well-formed chapter for style (e.g. `content/modules/08-probability-and-statistics/01-probability-and-bayes-theorem.md`).
3. **Write** using the chapter shape in CONTRIBUTING.md: intuition → derivation → worked example → runnable code → practice with hidden answers → further reading.
4. **Verify. Never skip this step.**
   - Extract and **run every Python block**. Output shown in the text must be real output.
   - **Recompute every number** in worked examples and answers with code.
   - Check every citation and factual claim. If you can't verify it, remove it or mark it as uncertain in the PR.
   - Run `book check` and fix everything it reports.
5. **Open a PR** using the template. Tick "AI assistance", name your model or tool, and list exactly what you verified and how. Flag anything you are unsure about. Honest uncertainty is valued; confident errors are not.

## Hard rules

- **No fabrication.** No invented references, statistics, gene facts, model specifications or guideline thresholds.
- **Clinical safety (Part VI and any dosing content).**
  - Every clinical chapter keeps a `> [!CAUTION]` box saying that examples teach arithmetic, not prescribing.
  - Use illustrative drugs ("Drug X, 10 mg/kg, max 500 mg").
  - Never state a real-drug dose unless it is standard and verified against an official source.
  - Never remove existing safety caveats.
- **Synthetic data only** in code. Never require downloading restricted datasets (UK Biobank, dbGaP). Never include real patient data.
- **Relative links only** (`../../<module>/<chapter>/`), because the site is served under a sub-path.
- **Stay in scope.** Don't edit unrelated files, reformat whole files, change the licence, or touch CI secrets.
- **Markdown gotchas.**
  - A literal `$` is written `\$`.
  - Inline math needs no space inside the delimiters: `$x$`, not `$ x $`.
  - Inside tables, `|` in math is written `\vert`.
  - `<details>` blocks need blank lines around their Markdown content.
  - Mermaid labels go in double quotes.
- **Licence.** Contributions are Apache-2.0. Don't paste copyrighted text, or questions from GMAC or commercial prep materials.

## Good tasks for agents

- Add practice problems (with verified answers) to chapters that have fewer than five.
- Turn a chapter's formula into a reusable, tested Python snippet.
- Check citations in a module and report or fix discrepancies.
- Add worked examples for missing patient profiles in Part VI (have a human clinician review them).
- Engine work: offline KaTeX, an i18n scaffold, accessibility audits, interactive calculators.
