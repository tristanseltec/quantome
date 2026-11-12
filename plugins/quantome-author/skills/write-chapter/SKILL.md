---
name: write-chapter
description: Write or substantially revise a chapter of the Quantome open textbook (maths, biology, medicine, AI) in the house style, with derivations, worked examples, runnable Python whose output is real, hidden-answer practice and verified references. Use when contributing to the Quantome repository and asked to "write a chapter", "add a section", "add practice problems" or "draft a module".
---

# Write a Quantome chapter

Use this in a clone of https://github.com/tristanseltec/quantome. First read `AGENTS.md` at the repo root.

## Before writing

1. Read `references/house-style.md` (in this skill's directory). For clinical content, also read `references/clinical-rules.md`.
2. Read one or two existing chapters in the target module, plus a well-formed example such as
   `content/modules/08-probability-and-statistics/01-probability-and-bayes-theorem.md`.
3. Check the curriculum. List `content/modules/*/` and link prerequisites with relative links.
4. For a new chapter, scaffold it with `cargo run -p book-cli -- new chapter <module-slug> "Title"`, or create
   `NN-<slug>.md` directly. Numeric prefixes set the order, and URLs use the slug.

## While writing

- Follow the chapter template: intuition → derivation → worked example → code with real output → practice → further reading.
- Put every numeric claim through code as you go. Keep scratch scripts outside the repository.
- If a formula belongs in the shared library (`py/src/quantome`), add it there with a `registry.toml` entry and
  tests, then run `python3 scripts/sync_plugins.py`.

## Finish with verification. Don't skip it.

Use the **verify-chapter** skill: it runs every code block and compares outputs, then runs `book check`.
For factual and citation claims, use **check-citations**. For clinical content, ask the `clinical-reviewer`
agent for an independent review before opening the PR.

Open the PR with the template. Tick **AI assistance**, name your model, and list exactly what was verified and how.
