// Progressive enhancements for the statically rendered book.
// Everything works without JS except search, math typesetting and progress.
(() => {
  "use strict";
  const BASE = document.currentScript?.dataset.base || "/";
  const store = {
    get(k, d) { try { return JSON.parse(localStorage.getItem(k)) ?? d; } catch { return d; } },
    set(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch {} },
  };

  // ---- Theme ----
  document.getElementById("theme-toggle")?.addEventListener("click", () => {
    const root = document.documentElement;
    const dark = root.dataset.theme
      ? root.dataset.theme === "dark"
      : matchMedia("(prefers-color-scheme: dark)").matches;
    root.dataset.theme = dark ? "light" : "dark";
    try { localStorage.setItem("theme", root.dataset.theme); } catch {}
  });

  // ---- Mobile nav ----
  document.getElementById("menu-toggle")?.addEventListener("click", () =>
    document.body.classList.toggle("nav-open"));
  document.getElementById("sidebar")?.querySelector("li a.active")?.scrollIntoView({ block: "center" });

  // ---- Math (KaTeX loads with `defer`, before DOMContentLoaded) ----
  addEventListener("DOMContentLoaded", () => {
    if (!window.katex) return;
    document.querySelectorAll(".math").forEach((el) => {
      try {
        katex.render(el.textContent, el, {
          displayMode: el.classList.contains("math-display"),
          throwOnError: false,
        });
      } catch {}
    });
  });

  // ---- Code highlighting & diagrams (loaded only on pages that need them) ----
  const loadScript = (src) => new Promise((ok, err) => {
    const s = document.createElement("script");
    s.src = src; s.onload = ok; s.onerror = err; document.head.appendChild(s);
  });
  addEventListener("DOMContentLoaded", async () => {
    const diagrams = [...document.querySelectorAll("pre > code.language-mermaid")];
    const code = [...document.querySelectorAll("pre > code[class*='language-']")]
      .filter((c) => !c.classList.contains("language-mermaid"));
    if (code.length) {
      try {
        await loadScript("https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js");
        code.forEach((c) => window.hljs.highlightElement(c));
      } catch {}
    }
    if (diagrams.length) {
      const nodes = diagrams.map((c) => {
        const div = document.createElement("div");
        div.className = "mermaid";
        div.textContent = c.textContent;
        c.parentElement.replaceWith(div);
        return div;
      });
      try {
        const { default: mermaid } = await import("https://cdn.jsdelivr.net/npm/mermaid@11.4.1/dist/mermaid.esm.min.mjs");
        const root = document.documentElement;
        const dark = root.dataset.theme ? root.dataset.theme === "dark" : matchMedia("(prefers-color-scheme: dark)").matches;
        mermaid.initialize({ startOnLoad: false, theme: dark ? "dark" : "neutral", securityLevel: "strict" });
        await mermaid.run({ nodes });
      } catch {}
    }
  });

  // ---- Reading progress ----
  const done = new Set(store.get("done", []));
  const paint = () => {
    document.querySelectorAll("[data-chapter]").forEach((a) =>
      a.classList.toggle("done", a.tagName === "A" && done.has(a.dataset.chapter)));
    const label = document.getElementById("progress-label");
    if (label) {
      const total = +label.dataset.total || 1;
      const n = [...document.querySelectorAll("#sidebar li a[data-chapter]")]
        .filter((a) => done.has(a.dataset.chapter)).length;
      label.textContent = `${n} / ${total} chapters done`;
      document.getElementById("progress-bar").style.width = `${(100 * n) / total}%`;
    }
    const btn = document.getElementById("mark-done");
    if (btn) {
      const on = done.has(btn.dataset.chapter);
      btn.classList.toggle("is-done", on);
      btn.textContent = on ? "✓ Done — click to undo" : "Mark chapter as done";
    }
    document.querySelectorAll(".card[data-chapters]").forEach((c) => {
      const urls = c.dataset.chapters.split(" ").filter(Boolean);
      const n = urls.filter((u) => done.has(u)).length;
      const meta = c.querySelector(".card-meta");
      if (meta && n) meta.textContent = `${n} / ${urls.length} chapters done`;
    });
  };
  document.getElementById("mark-done")?.addEventListener("click", (e) => {
    const k = e.currentTarget.dataset.chapter;
    done.has(k) ? done.delete(k) : done.add(k);
    store.set("done", [...done]);
    paint();
  });
  const markBtn = document.getElementById("mark-done");
  if (markBtn) store.set("last", { url: markBtn.dataset.chapter, title: document.querySelector("h1")?.textContent });
  const resume = document.getElementById("resume");
  const last = store.get("last", null);
  if (resume && last?.url) {
    resume.href = last.url;
    resume.textContent = `Resume: ${last.title}`;
    resume.hidden = false;
  }
  paint();

  // ---- On-page TOC highlight ----
  const tocLinks = [...document.querySelectorAll(".toc a")];
  if (tocLinks.length && "IntersectionObserver" in window) {
    const byId = new Map(tocLinks.map((a) => [decodeURIComponent(a.hash.slice(1)), a]));
    const io = new IntersectionObserver((entries) => {
      for (const e of entries) if (e.isIntersecting) {
        tocLinks.forEach((a) => a.classList.remove("active"));
        byId.get(e.target.id)?.classList.add("active");
      }
    }, { rootMargin: "0px 0px -70% 0px" });
    byId.forEach((_, id) => { const h = document.getElementById(id); if (h) io.observe(h); });
  }

  // ---- Search ----
  const input = document.getElementById("search");
  const list = document.getElementById("search-results");
  let index = null, sel = -1;
  const load = async () => {
    if (index) return index;
    const r = await fetch(`${BASE}assets/search-index.json`);
    index = (await r.json()).map((d) => ({
      ...d, _t: d.title.toLowerCase(), _h: d.headings.join(" ").toLowerCase(), _x: d.text.toLowerCase(),
    }));
    return index;
  };
  const esc = (s) => s.replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const snippet = (text, term) => {
    const i = text.toLowerCase().indexOf(term);
    if (i < 0) return esc(text.slice(0, 120)) + "…";
    const s = Math.max(0, i - 50), raw = text.slice(s, i + 90);
    const j = i - s;
    return (s ? "…" : "") + esc(raw.slice(0, j)) + "<mark>" + esc(raw.slice(j, j + term.length)) + "</mark>" + esc(raw.slice(j + term.length)) + "…";
  };
  const search = async (q) => {
    const terms = q.toLowerCase().split(/\s+/).filter(Boolean);
    if (!terms.length) { list.hidden = true; return; }
    const docs = await load();
    const hits = docs.map((d) => {
      let score = 0;
      for (const t of terms) {
        const s = (d._t.includes(t) ? 10 : 0) + (d._h.includes(t) ? 4 : 0) + (d._x.includes(t) ? 1 : 0);
        if (!s) return null;
        score += s;
      }
      return { d, score };
    }).filter(Boolean).sort((a, b) => b.score - a.score).slice(0, 8);
    sel = -1;
    list.innerHTML = hits.length
      ? hits.map(({ d }) => `<li><a href="${d.url}"><strong>${esc(d.title)}</strong><small>${esc(d.module)}</small><small>${snippet(d.text, terms[0])}</small></a></li>`).join("")
      : `<li class="empty">No results for “${esc(q)}”</li>`;
    list.hidden = false;
  };
  if (input && list) {
    let timer;
    input.addEventListener("input", () => { clearTimeout(timer); timer = setTimeout(() => search(input.value), 80); });
    input.addEventListener("focus", () => input.value && search(input.value));
    input.addEventListener("keydown", (e) => {
      const links = [...list.querySelectorAll("a")];
      if (e.key === "ArrowDown" || e.key === "ArrowUp") {
        e.preventDefault();
        sel = (sel + (e.key === "ArrowDown" ? 1 : -1) + links.length) % links.length;
        links.forEach((a, i) => a.classList.toggle("sel", i === sel));
      } else if (e.key === "Enter" && links.length) {
        location.href = links[Math.max(sel, 0)].href;
      } else if (e.key === "Escape") {
        list.hidden = true; input.blur();
      }
    });
    document.addEventListener("click", (e) => { if (!e.target.closest(".search")) list.hidden = true; });
    document.addEventListener("keydown", (e) => {
      if (e.key === "/" && !/INPUT|TEXTAREA/.test(document.activeElement.tagName)) { e.preventDefault(); input.focus(); }
    });
  }
})();
