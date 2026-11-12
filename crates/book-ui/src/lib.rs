//! Leptos components for the book. Each page is server-rendered to static
//! HTML; small progressive enhancements (search, theme, progress tracking,
//! KaTeX) live in `assets/book.js`.

mod components;
mod pages;

use book_core::Book;
use leptos::prelude::*;
use std::sync::Arc;

/// One output file: a path relative to the site root and its HTML.
pub struct Page {
    pub path: String,
    pub html: String,
}

/// Render every page of the book.
pub fn render_site(book: Arc<Book>) -> Vec<Page> {
    let mut out = Vec::new();

    out.push(Page {
        path: "index.html".into(),
        html: doc(pages::HomePage(pages::HomePageProps { book: book.clone() })),
    });
    out.push(Page {
        path: "404.html".into(),
        html: doc(pages::NotFound(pages::NotFoundProps { book: book.clone() })),
    });

    for (mi, m) in book.modules.iter().enumerate() {
        out.push(Page {
            path: format!("{}/index.html", m.slug),
            html: doc(pages::ModulePage(pages::ModulePageProps {
                book: book.clone(),
                module: mi,
            })),
        });
    }

    let order = book.reading_order();
    for (i, r) in order.iter().enumerate() {
        let (m, c) = book.chapter(*r);
        out.push(Page {
            path: format!("{}/{}/index.html", m.slug, c.slug),
            html: doc(pages::ChapterPage(pages::ChapterPageProps {
                book: book.clone(),
                at: *r,
                prev: i.checked_sub(1).map(|p| order[p]),
                next: order.get(i + 1).copied(),
            })),
        });
    }
    out
}

fn doc(view: impl IntoView + 'static) -> String {
    let owner = Owner::new();
    let html = owner.with(|| view.into_view().to_html());
    // Static output never hydrates, so drop Leptos' empty hydration markers.
    format!("<!DOCTYPE html>\n{}", html.replace("<!>", ""))
}
