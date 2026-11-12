//! A small JSON search index consumed by `assets/book.js`.

use crate::Book;
use serde::Serialize;

#[derive(Serialize)]
pub struct Entry<'a> {
    pub title: &'a str,
    pub module: &'a str,
    pub url: String,
    pub headings: Vec<&'a str>,
    pub text: String,
}

const MAX_TEXT: usize = 4000;

pub fn build_index(book: &Book) -> Vec<Entry<'_>> {
    book.reading_order()
        .into_iter()
        .map(|r| {
            let (m, c) = book.chapter(r);
            let text = match c.plain_text.char_indices().nth(MAX_TEXT) {
                Some((i, _)) => c.plain_text[..i].to_string(),
                None => c.plain_text.clone(),
            };
            Entry {
                title: &c.title,
                module: &m.title,
                url: book.chapter_url(m, c),
                headings: c.headings.iter().map(|h| h.text.as_str()).collect(),
                text,
            }
        })
        .collect()
}
