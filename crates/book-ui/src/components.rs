use book_core::{Book, ChapterRef};
use leptos::prelude::*;
use std::sync::Arc;

/// Self-hosted KaTeX — vendored in `assets/vendor/katex` (version pinned in
/// `assets/vendor/README.md`) so the book renders math without a network.
const KATEX: &str = "assets/vendor/katex";

/// Applied before first paint so the page never flashes the wrong theme.
const THEME_BOOT: &str = "try{var t=localStorage.getItem('theme');if(t)document.documentElement.dataset.theme=t}catch(e){}";

/// The full HTML document: `<head>`, top bar, sidebar and a content slot.
#[component]
pub fn Shell(
    book: Arc<Book>,
    title: String,
    #[prop(optional)] description: String,
    /// Highlights this chapter in the sidebar.
    #[prop(optional)]
    current: Option<ChapterRef>,
    /// Highlights this module in the sidebar.
    #[prop(optional)]
    current_module: Option<usize>,
    children: Children,
) -> impl IntoView {
    let cfg = &book.config;
    let page_title = if title == cfg.title {
        title.clone()
    } else {
        format!("{title} · {}", cfg.title)
    };
    let description = if description.is_empty() {
        cfg.description.clone()
    } else {
        description
    };
    let home = cfg.base_url.clone();
    let book_title = cfg.title.clone();
    let repo = cfg.repository.clone();
    let base = cfg.base_url.clone();

    view! {
        <html lang="en">
            <head>
                <meta charset="utf-8" />
                <meta name="viewport" content="width=device-width, initial-scale=1" />
                <title>{page_title}</title>
                <meta name="description" content=description />
                <script inner_html=THEME_BOOT></script>
                <link rel="icon" href=book.asset_url("assets/favicon.svg") type="image/svg+xml" />
                <link rel="stylesheet" href=book.asset_url(&format!("{KATEX}/katex.min.css")) />
                <link rel="stylesheet" href=book.asset_url("assets/style.css") />
                <script defer src=book.asset_url(&format!("{KATEX}/katex.min.js"))></script>
                <script defer src=book.asset_url("assets/book.js") data-base=base></script>
            </head>
            <body>
                <a class="skip" href="#content">"Skip to content"</a>
                <header class="topbar">
                    <button class="icon-btn menu-btn" id="menu-toggle" aria-label="Toggle navigation" aria-controls="sidebar">
                        "☰"
                    </button>
                    <a class="brand" href=home>{book_title}</a>
                    <div class="search">
                        <input id="search" type="search" placeholder="Search…  ( / )" autocomplete="off" aria-label="Search the book" />
                        <ul id="search-results" class="search-results" hidden></ul>
                    </div>
                    <button class="icon-btn" id="theme-toggle" aria-label="Toggle dark mode">"◐"</button>
                    {repo.map(|r| view! { <a class="icon-btn gh" href=r aria-label="Source on GitHub">"GitHub"</a> })}
                </header>
                <div class="layout">
                    <Sidebar book=book.clone() current=current current_module=current_module />
                    <main id="content">{children()}</main>
                </div>
            </body>
        </html>
    }
}

#[component]
pub fn Sidebar(
    book: Arc<Book>,
    current: Option<ChapterRef>,
    current_module: Option<usize>,
) -> impl IntoView {
    let modules = book
        .modules
        .iter()
        .enumerate()
        .map(|(mi, m)| {
            let open = current.map(|c| c.module) == Some(mi) || current_module == Some(mi);
            let chapters = m
                .chapters
                .iter()
                .enumerate()
                .map(|(ci, c)| {
                    let here = current == Some(ChapterRef { module: mi, chapter: ci });
                    let url = book.chapter_url(m, c);
                    view! {
                        <li>
                            <a href=url.clone() class:active=here data-chapter=url aria-current=here.then_some("page")>
                                {c.title.clone()}
                            </a>
                        </li>
                    }
                })
                .collect_view();
            let part = book.part_start(mi).map(|p| view! { <p class="nav-part">{p.to_string()}</p> });
            view! {
                {part}
                <details class="nav-module" open=open>
                    <summary>
                        <span class="num">{format!("{:02}", mi + 1)}</span>
                        <a href=book.module_url(m) class:active=current_module == Some(mi)>{m.title.clone()}</a>
                    </summary>
                    <ol>{chapters}</ol>
                </details>
            }
        })
        .collect_view();

    view! {
        <nav class="sidebar" id="sidebar" aria-label="Book contents">
            <div class="progress-summary">
                <div class="bar"><span id="progress-bar"></span></div>
                <small id="progress-label" data-total=book.chapter_count()>"0 / "{book.chapter_count()}" chapters done"</small>
            </div>
            {modules}
        </nav>
    }
}

/// "Previous / Next" footer navigation.
#[component]
pub fn PrevNext(
    book: Arc<Book>,
    prev: Option<ChapterRef>,
    next: Option<ChapterRef>,
) -> impl IntoView {
    let link = |r: ChapterRef, label: &'static str, class: &'static str| {
        let (m, c) = book.chapter(r);
        view! {
            <a class=format!("pn {class}") href=book.chapter_url(m, c) rel=if class == "prev" { "prev" } else { "next" }>
                <small>{label}</small>
                <span>{c.title.clone()}</span>
            </a>
        }
    };
    view! {
        <nav class="prev-next" aria-label="Chapter navigation">
            {prev.map(|r| link(r, "← Previous", "prev"))}
            {next.map(|r| link(r, "Next →", "next"))}
        </nav>
    }
}
