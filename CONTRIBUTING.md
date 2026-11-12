# Contributing to Quantome

Thank you for helping build an open mathematics textbook! Quantome welcomes **human researchers, educators, clinicians, students and AI agents**. This guide applies to everyone. AI agents should also read [AGENTS.md](AGENTS.md).

## Ways to contribute

| Contribution | How |
|---|---|
| Fix a typo or unclear sentence | Click **Suggest an edit** on any page, or edit the Markdown file and open a PR |
| Report a mathematical, clinical or factual error | [Open an issue](https://github.com/tristanseltec/quantome/issues/new/choose) using the *Content error* form. Clinical errors are triaged first |
| Add practice problems or worked examples | Edit the chapter and open a PR |
| Propose a new chapter or module | Open a *New chapter proposal* issue first, so we can agree on scope and placement |
| Improve the engine (Rust), styles or JS | Open an issue or a small PR |
| Review | Comment on open PRs, especially clinical and citation-heavy ones |
| Add or fix a formula | Edit `py/src/quantome` (library + `registry.toml` + tests from the source), then `python3 scripts/sync_plugins.py` |
| Build a skill | Add or extend a plugin under `plugins/`, with eval cases; see [docs/VISION.md](docs/VISION.md) |
| **Become an expert reviewer** | Clinicians, pharmacists and statisticians: sign off formulas to move them from L1 to L2 ([issue #1](https://github.com/tristanseltec/quantome/issues/1)) |

## Development setup

```bash
git clone https://github.com/tristanseltec/quantome && cd quantome
cargo run --release -p book-cli -- serve        # live preview at http://127.0.0.1:3000
cargo run --release -p book-cli -- check        # must pass before you open a PR

# Optional: run the Python examples
python -m venv .venv && source .venv/bin/activate
pip install numpy scikit-learn torch
```

## Writing content

Chapters live in `content/modules/NN-<module>/NN-<chapter>.md`. Scaffold one with:

```bash
cargo run -p book-cli -- new chapter <module-slug> "Chapter Title"
```

### Chapter shape

```markdown
+++
summary = "One sentence: what the reader can do after this chapter."
+++

# Chapter Title

Motivation: why this matters.

## Key ideas          ← intuition, then derivation
## Worked example     ← by hand, step by step
## In code            ← runnable Python, small synthetic data, fixed seed
## Practice           ← problems with hidden answers
## Further reading    ← only sources you have checked
```

Part VI (clinical) chapters also need a `> [!CAUTION]` box near the top, and worked examples for several patient profiles.

### Markdown cheatsheet

| Feature | Syntax |
|---|---|
| Inline / display math | `$x^2$` / `$$\frac{a}{b}$$` on its own line |
| Literal dollar sign | `\$` |
| `\|` inside math in a table | `\vert` |
| Callouts | `> [!TIP]` Strategy · `> [!IMPORTANT]` Key formula · `> [!WARNING]` Common trap · `> [!NOTE]` · `> [!CAUTION]` |
| Hidden answer | `<details>` + `<summary>Answer</summary>` + **blank line** + Markdown + **blank line** + `</details>` |
| Diagram | a ` ```mermaid ` block (`flowchart LR`, labels in `"double quotes"`) |
| Link to another chapter | relative only: `../../<module-slug>/<chapter-slug>/` |
| Images | put them in `content/static/` and link relatively |

## Quality bar

Every contribution must meet these rules, whoever writes it:

1. **Correct.** Recompute every number in examples and answers. Run every code block, and paste only real output.
2. **Sourced.** Cite only references you have actually checked. No invented papers, statistics or guideline thresholds. If unsure, say so or leave it out.
3. **Safe.** Clinical content teaches calculation, not prescribing. Use illustrative drugs ("Drug X") unless a dose is standard and verified, and point readers to their local formulary.
4. **Original.** Don't copy questions from official GMAC material, commercial prep books or paywalled texts.
5. **Focused.** One topic per PR. Don't reformat files you aren't changing.
6. **Single-sourced.** Formulas live in `py/src/quantome`, with tests whose expected values come from the source. Skills run that code.
7. **Checked.** `book check` passes. For Rust changes, `cargo fmt`, `cargo clippy -- -D warnings` and `cargo test` pass too (or run `just check`).

## Using AI tools

AI-assisted contributions are welcome, and so are fully agent-authored PRs. In return we ask for transparency:

- Tick the **AI assistance** box in the PR template and name the tool or model.
- Say **what you verified, and how**: which code you ran and which numbers and citations you checked.
- A human maintainer reviews every PR before it is merged. Clinical PRs need a second reviewer with clinical background.

## Review process

1. CI runs tests, `book check` and a site build on every PR.
2. A maintainer reviews for correctness, clarity and fit.
3. Clinical (Part VI) and genomics-claims PRs get an extra domain review.
4. Squash-merge. The site redeploys automatically.

## License

By contributing, you agree that your contributions are licensed under the [Apache License 2.0](LICENSE), the license that covers the whole project, code and content alike.

Please follow our [Code of Conduct](CODE_OF_CONDUCT.md).
