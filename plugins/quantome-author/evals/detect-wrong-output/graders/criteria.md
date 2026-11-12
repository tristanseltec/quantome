---
type: llm
weight: 1
---

Pass only if the agent ran the verify-chapter skill's run_code_blocks.py (or equivalent execution of every python block) on the named chapter and reported per-block pass/fail with the overall result, rather than just reading the code. Fail if it declares the chapter verified without executing the code.
