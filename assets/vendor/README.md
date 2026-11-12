# Vendored front-end assets

Third-party libraries the book needs at read time are **checked into this
directory instead of loaded from a public CDN**, so the site works offline
(and behind strict CSPs). Nothing here is fetched at runtime.

| Package | Version | Files | Upstream | License |
|---|---|---|---|---|
| KaTeX | 0.16.22 | `katex/katex.min.css`, `katex/katex.min.js`, `katex/fonts/*` (60 files: woff2/woff/ttf) | <https://cdn.jsdelivr.net/npm/katex@0.16.22/dist> | `katex/LICENSE` (MIT) |
| Mermaid | 11.4.1 | `mermaid/mermaid.min.js` | <https://cdn.jsdelivr.net/npm/mermaid@11.4.1/dist> | `mermaid/LICENSE` (MIT) |
| highlight.js | 11.9.0 | `highlight.js/highlight.min.js` | <https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/> | `highlight.js/LICENSE` (BSD-3-Clause) |

Versions are exactly the ones the site used from the CDN before this
directory existed, so rendering (math, diagrams, code highlighting) is
unchanged.

## How the pages use these

- `crates/book-ui/src/components.rs` (`Shell`) emits
  `assets/vendor/katex/katex.min.css` and `…/katex.min.js` with `defer`,
  via `Book::asset_url`, so math typesets on every page.
- `assets/book.js` loads `highlight.js` and Mermaid **lazily**, only on
  pages that actually contain code blocks or ` ```mermaid ` diagrams.
  `book build` copies this whole tree to `dist/assets/vendor/`.

## Why Mermaid ships as one file

The CDN previously served `dist/mermaid.esm.min.mjs`, which imports
`dist/chunks/mermaid.esm.min/*` — 126 chunk files, ~11.7 MB. The
`dist/mermaid.min.js` build is self-contained (2.6 MB) and exposes the
same `mermaid.initialize()` / `mermaid.run()` API, so it is vendored
instead: one file, same rendering, still lazy-loaded.

## Bumping a version

```bash
V=0.16.22   # or 11.4.1 / 11.9.0
curl -sSL -o assets/vendor/katex/katex.min.css \
  "https://cdn.jsdelivr.net/npm/katex@$V/dist/katex.min.css"
# …same pattern for katex.min.js, fonts/, mermaid.min.js, highlight.min.js,
# and the LICENSE file from the matching upstream tag.
sha256sum assets/vendor/*/*.js assets/vendor/*/*.css   # update the table below
cargo run --release -p book-cli -- check
```

### Checksums (sha256)

```
19095127357ed6d29fe0a63a6b000c913a89f7f1963b765dd3715e97c9852e75  katex/katex.min.css
e8d885505949f3a5f4abdd5dd0d53696bd1371ad26ffbf4f310dcd77c8cdae89  katex/katex.min.js
a43bc1afd446f9c4cc66ac5dd45d02e8d65e26fc5344ec0ef787f88d6ddb6f9e  mermaid/mermaid.min.js
837a6fa5b0c736b52bbde2b2b6190f305da3fc9ed41681db5321507057b5c846  highlight.js/highlight.min.js
```
