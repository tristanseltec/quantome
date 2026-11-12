---
name: check-citations
description: Check the references and factual claims in a Quantome chapter (papers, guidelines, model specifications, gene facts, thresholds) against primary or official sources, and fix or flag anything unsupported. Use when asked to "check citations", "fact-check a chapter", or "verify references", and for every chapter that cites clinical guidelines or genomics or AI papers.
---

# Check citations and factual claims

1. **Inventory.** List every citation in *Further reading* and every specific factual claim in the text: numbers
   attributed to studies, guideline thresholds, model sizes or architectures, gene–disease links.
2. **Verify each one** against a primary or official source: PubMed or the DOI landing page, the guideline
   publisher (NICE, WHO, CDC, ESPGHAN), or the official model paper or repository. Use web search and fetch.
   Match authors, year, journal, volume and pages, and check that the claim actually appears in the source.
3. **Classify** each item:
   - ✅ **confirmed** (cite the URL you checked)
   - ✏️ **corrected** (show before → after)
   - ⚠️ **unverifiable**: soften the wording or remove the claim. Never leave a confident unverified claim.
4. **Edit minimally.** Keep the house style (`\$`, `\vert` in tables, `> ` inside callouts).
5. **Report** a table of all items with their status and source URLs, for the PR description.

Never invent a citation to support a claim. If no source supports it, the claim goes.
