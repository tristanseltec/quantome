use crate::components::{PrevNext, Shell};
use book_core::{Book, ChapterRef};
use leptos::prelude::*;
use std::sync::Arc;

#[component]
pub fn HomePage(book: Arc<Book>) -> impl IntoView {
    let cfg = book.config.clone();
    let start = book.reading_order().first().map(|r| {
        let (m, c) = book.chapter(*r);
        book.chapter_url(m, c)
    });
    // Group consecutive modules by their `part` heading.
    let mut groups: Vec<(String, Vec<usize>)> = Vec::new();
    for mi in 0..book.modules.len() {
        match book.part_start(mi) {
            Some(p) => groups.push((p.to_string(), vec![mi])),
            None => match groups.last_mut() {
                Some(g) => g.1.push(mi),
                None => groups.push(("Modules".to_string(), vec![mi])),
            },
        }
    }
    let card = |mi: usize| {
        let m = &book.modules[mi];
        let urls = m
            .chapters
            .iter()
            .map(|c| book.chapter_url(m, c))
            .collect::<Vec<_>>()
            .join(" ");
        view! {
            <a class="card" href=book.module_url(m) data-chapters=urls>
                <span class="num">{format!("Module {:02}", mi + 1)}</span>
                <h3>{m.title.clone()}</h3>
                <p>{m.summary.clone()}</p>
                <small class="card-meta">{format!("{} chapters", m.chapters.len())}</small>
            </a>
        }
    };
    let sections = groups
        .into_iter()
        .map(|(title, mods)| {
            let cards = mods.into_iter().map(card).collect_view();
            view! {
                <section class="part">
                    <h2>{title}</h2>
                    <div class="cards">{cards}</div>
                </section>
            }
        })
        .collect_view();
    let authors = (!cfg.authors.is_empty()).then(|| format!("By {}", cfg.authors.join(", ")));
    let license = cfg.license.clone();

    view! {
        <Shell book=book.clone() title=cfg.title.clone()>
            <section class="hero">
                <h1>{cfg.title.clone()}</h1>
                <p class="subtitle">{cfg.subtitle.clone()}</p>
                <p>{cfg.description.clone()}</p>
                <div class="hero-actions">
                    {start.map(|s| view! { <a class="btn primary" href=s>"Start reading →"</a> })}
                    <a class="btn" id="resume" hidden>"Resume where you left off"</a>
                </div>
            </section>
            {sections}
            <footer class="page-footer">
                {authors.map(|a| view! { <p>{a}</p> })}
                {license.map(|l| view! { <p>{l}</p> })}
                <p>"Built with Rust + Leptos."</p>
            </footer>
        </Shell>
    }
}

#[component]
pub fn ModulePage(book: Arc<Book>, module: usize) -> impl IntoView {
    let m = book.modules[module].clone();
    let items = m
        .chapters
        .iter()
        .enumerate()
        .map(|(ci, c)| {
            let url = book.chapter_url(&m, c);
            view! {
                <li>
                    <a href=url.clone() data-chapter=url>
                        <span class="num">{format!("{}.{}", module + 1, ci + 1)}</span>
                        <span>
                            <strong>{c.title.clone()}</strong>
                            {(!c.summary.is_empty()).then(|| view! { <small>{c.summary.clone()}</small> })}
                        </span>
                    </a>
                </li>
            }
        })
        .collect_view();

    view! {
        <Shell book=book.clone() title=m.title.clone() description=m.summary.clone() current_module=module>
            <article class="chapter">
                <p class="eyebrow">{format!("Module {:02}", module + 1)}</p>
                <h1>{m.title.clone()}</h1>
                <p class="lead">{m.summary.clone()}</p>
                <ol class="chapter-list">{items}</ol>
            </article>
        </Shell>
    }
}

#[component]
pub fn ChapterPage(
    book: Arc<Book>,
    at: ChapterRef,
    prev: Option<ChapterRef>,
    next: Option<ChapterRef>,
) -> impl IntoView {
    let (m, c) = book.chapter(at);
    let (m, c) = (m.clone(), c.clone());
    let url = book.chapter_url(&m, &c);
    let edit = book.edit_url(&c);
    let toc = (!c.headings.is_empty()).then(|| {
        let items = c
            .headings
            .iter()
            .map(|h| {
                view! {
                    <li class=format!("toc-h{}", h.level)>
                        <a href=format!("#{}", h.id)>{h.text.clone()}</a>
                    </li>
                }
            })
            .collect_view();
        view! {
            <aside class="toc" aria-label="On this page">
                <strong>"On this page"</strong>
                <ul>{items}</ul>
            </aside>
        }
    });

    view! {
        <Shell book=book.clone() title=c.title.clone() description=c.summary.clone() current=at>
            <div class="chapter-wrap">
                <article class="chapter">
                    <p class="eyebrow">
                        <a href=book.module_url(&m)>{format!("Module {:02} · {}", at.module + 1, m.title)}</a>
                    </p>
                    <h1>{c.title.clone()}</h1>
                    <div class="prose" inner_html=c.html.clone()></div>
                    <div class="chapter-actions">
                        <button class="btn" id="mark-done" data-chapter=url>"Mark chapter as done"</button>
                        {edit.map(|e| view! { <a class="edit" href=e>"✎ Suggest an edit"</a> })}
                    </div>
                    <PrevNext book=book.clone() prev=prev next=next />
                </article>
                {toc}
            </div>
        </Shell>
    }
}

#[component]
pub fn NotFound(book: Arc<Book>) -> impl IntoView {
    let home = book.config.base_url.clone();
    view! {
        <Shell book=book.clone() title="Page not found".to_string()>
            <article class="chapter">
                <h1>"Page not found"</h1>
                <p>"That page doesn't exist (yet). "<a href=home>"Back to the start"</a>"."</p>
            </article>
        </Shell>
    }
}
