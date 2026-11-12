# Quantome house style

## Audience and depth
- Assume GMAT-level algebra (Part I). Build every idea from intuition, then formal maths, then code.
- Derive key results rather than just stating them. Show tensor shapes. Work small numeric examples by hand, then
  reproduce them in code.
- Aim for about 1,800–3,500 words of prose per chapter. Quality and correctness matter more than length.
- Connect to the book's running examples where natural: the DNA → heart-disease risk project (Parts II–V), and
  patient profiles (Part VI).

## Chapter template
```
+++
summary = "One sentence: what the reader can do after this chapter."
+++

# Chapter Title

Motivating intro.

## Key ideas            (### subsections; derivations)
## Worked example(s)    (by hand, step by step)
## In code              (runnable Python, synthetic data, fixed seed, real output in a ```text block)
## <Domain> connection  (Biomedical connection / Sanity checks & common errors for clinical chapters)
## Practice             (3–8 problems, each with a hidden answer)
## Further reading      (only sources you have verified)
```

## Markdown that renders correctly
| Need | Write |
|---|---|
| Inline / display math | `$x$` / `$$...$$` on its own line, with blank lines around it outside callouts |
| No spaces inside inline delimiters | `$x = 1$`, never `$ x = 1 $` |
| Literal dollar | `\$` |
| `\|` inside math in a table | `\vert` |
| Callouts | `> [!TIP]` (shown as "Strategy"), `> [!IMPORTANT]` ("Key formula"), `> [!WARNING]` ("Common trap"), `> [!NOTE]`, `> [!CAUTION]`. Prefix every line, including display math, with `> ` |
| Hidden answer | `<details>`, `<summary>Answer</summary>`, **blank line**, Markdown, **blank line**, `</details>` |
| Diagram | a ```` ```mermaid ```` block, `flowchart LR/TD`, labels in `"double quotes"`, no `$` math |
| Code output | a ```` ```text ```` block directly after the ```` ```python ```` block it belongs to |
| Cross-link | relative only: `../../<module-slug>/<chapter-slug>/` (slug = name without the `NN-` prefix) |

KaTeX supports `\mathbf`, `\boldsymbol`, `\operatorname`, `\begin{bmatrix}`, `\begin{aligned}`, `\tfrac`, `\dfrac`
and `\cancel`. Avoid macros that KaTeX doesn't support.

## Code
- Python ≥ 3.11 with numpy, scikit-learn or PyTorch (CPU). Self-contained, synthetic data, seeded RNG, under ~3 minutes on a CPU.
- Never download restricted datasets in chapter code. You may name real datasets in the prose.
- Every shown output must be real: `verify-chapter` checks it.
- If a formula already exists in `py/src/quantome`, import it or mirror it exactly. If you add a new reusable formula,
  add it to the library, with a registry entry and tests from the source.

## Accuracy
- No invented citations, statistics, gene facts, model specifications or guideline thresholds.
- Recompute every number in worked examples and answers with code.
- Flag anything you could not verify in the PR, and phrase it carefully in the text.
