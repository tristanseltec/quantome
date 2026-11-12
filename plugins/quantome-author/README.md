# quantome-author

The contributor toolkit for [Quantome](https://github.com/tristanseltec/quantome). It packages the verification process used to
build the book, so every human or AI contributor works to the same standard.

```bash
/plugin marketplace add tristanseltec/quantome
/plugin install quantome-author@quantome
```

| Component | What it does |
|---|---|
| `write-chapter` skill | House style, chapter template, Markdown rules and clinical rules (in `references/`) |
| `verify-chapter` skill | `run_code_blocks.py` runs every Python block and diffs the shown vs real output; then `book check` |
| `check-citations` skill | Verify every citation and sourced claim against primary sources; never invent references |
| `fact-checker` agent | Independent recompute + citation check with minimal fixes |
| `clinical-reviewer` agent | Independent clinical-accuracy review (doesn't replace human clinical sign-off) |

Use it inside a clone of the repository. See [AGENTS.md](../../AGENTS.md) and [CONTRIBUTING.md](../../CONTRIBUTING.md).
Licence: Apache-2.0.
