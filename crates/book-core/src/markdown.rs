//! Markdown → HTML with heading anchors, GFM alerts, tables and math.
//!
//! Math (`$x^2$`, `$$\frac{a}{b}$$`) is emitted as
//! `<span class="math math-inline|math-display">` and typeset by KaTeX in the
//! browser.

use pulldown_cmark::{CowStr, Event, HeadingLevel, Options, Parser, Tag, TagEnd, html};
use std::collections::HashMap;

#[derive(Debug, Clone)]
pub struct Heading {
    pub level: u8,
    pub id: String,
    pub text: String,
}

#[derive(Debug, Clone)]
pub struct Rendered {
    pub html: String,
    /// Text of the first `#` heading, if any.
    pub title: Option<String>,
    /// `##` and `###` headings, for the on-page table of contents.
    pub headings: Vec<Heading>,
    pub plain_text: String,
}

pub fn render(src: &str) -> Rendered {
    let opts = Options::ENABLE_TABLES
        | Options::ENABLE_FOOTNOTES
        | Options::ENABLE_STRIKETHROUGH
        | Options::ENABLE_TASKLISTS
        | Options::ENABLE_SMART_PUNCTUATION
        | Options::ENABLE_HEADING_ATTRIBUTES
        | Options::ENABLE_MATH
        | Options::ENABLE_GFM;

    let mut events: Vec<Event> = Parser::new_ext(src, opts).collect();

    let mut title = None;
    let mut headings = Vec::new();
    let mut plain = String::new();
    let mut used: HashMap<String, usize> = HashMap::new();
    let mut skip_title_range = None;

    let mut i = 0;
    while i < events.len() {
        match &events[i] {
            Event::Start(Tag::Heading { level, id, .. }) => {
                let level = *level;
                let explicit = id.clone();
                let start = i;
                let mut text = String::new();
                i += 1;
                while i < events.len() && !matches!(events[i], Event::End(TagEnd::Heading(_))) {
                    match &events[i] {
                        Event::Text(t) | Event::Code(t) | Event::InlineMath(t) => text.push_str(t),
                        _ => {}
                    }
                    i += 1;
                }
                let text = text.trim().to_string();

                if level == HeadingLevel::H1 && title.is_none() {
                    // The page template renders the title itself.
                    title = Some(text);
                    skip_title_range = Some((start, i));
                } else {
                    let base = explicit
                        .map(|s| s.to_string())
                        .unwrap_or_else(|| slugify(&text));
                    let n = used.entry(base.clone()).or_insert(0);
                    let id = if *n == 0 {
                        base.clone()
                    } else {
                        format!("{base}-{n}")
                    };
                    *n += 1;
                    if let Event::Start(Tag::Heading { id: slot, .. }) = &mut events[start] {
                        *slot = Some(CowStr::from(id.clone()));
                    }
                    if matches!(level, HeadingLevel::H2 | HeadingLevel::H3) {
                        headings.push(Heading {
                            level: level as u8,
                            id,
                            text: text.clone(),
                        });
                    }
                    plain.push_str(&text);
                    plain.push('\n');
                }
            }
            Event::Text(t) | Event::Code(t) => {
                plain.push_str(t);
                plain.push(' ');
            }
            Event::End(TagEnd::Paragraph | TagEnd::Item) => plain.push('\n'),
            _ => {}
        }
        i += 1;
    }

    if let Some((a, b)) = skip_title_range {
        events.drain(a..=b);
    }

    let mut out = String::with_capacity(src.len() * 3 / 2);
    html::push_html(&mut out, events.into_iter());
    let out = add_heading_anchors(&out);

    Rendered {
        html: out,
        title,
        headings,
        plain_text: collapse_ws(&plain),
    }
}

/// Append a `#` permalink inside every `<h2 id=..>`–`<h6 id=..>`.
fn add_heading_anchors(html: &str) -> String {
    let mut out = String::with_capacity(html.len() + 256);
    let mut rest = html;
    while let Some(pos) = rest.find("<h") {
        let (before, after) = rest.split_at(pos);
        out.push_str(before);
        let is_heading = after
            .as_bytes()
            .get(2)
            .is_some_and(|b| (b'2'..=b'6').contains(b))
            && after[3..].starts_with(" id=\"");
        if !is_heading {
            out.push_str("<h");
            rest = &after[2..];
            continue;
        }
        let id_start = 8;
        let id_end = id_start + after[id_start..].find('"').unwrap_or(0);
        let id = &after[id_start..id_end];
        let close = after.find('>').map(|p| p + 1).unwrap_or(after.len());
        out.push_str(&after[..close]);
        out.push_str(&format!(
            "<a class=\"anchor\" href=\"#{id}\" aria-label=\"Link to this section\">#</a>"
        ));
        rest = &after[close..];
    }
    out.push_str(rest);
    out
}

pub fn slugify(s: &str) -> String {
    let mut out = String::new();
    let mut dash = false;
    for c in s.chars().flat_map(char::to_lowercase) {
        if c.is_alphanumeric() {
            out.push(c);
            dash = false;
        } else if !dash && !out.is_empty() {
            out.push('-');
            dash = true;
        }
    }
    while out.ends_with('-') {
        out.pop();
    }
    if out.is_empty() {
        "section".into()
    } else {
        out
    }
}

fn collapse_ws(s: &str) -> String {
    s.split_whitespace().collect::<Vec<_>>().join(" ")
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn extracts_title_and_headings() {
        let r = render("# Title\n\nIntro.\n\n## First part\n\n### Sub\n\n## First part\n");
        assert_eq!(r.title.as_deref(), Some("Title"));
        assert!(!r.html.contains("<h1"));
        let ids: Vec<_> = r.headings.iter().map(|h| h.id.as_str()).collect();
        assert_eq!(ids, ["first-part", "sub", "first-part-1"]);
        assert!(r.html.contains("<h2 id=\"first-part\"><a class=\"anchor\""));
    }

    #[test]
    fn math_is_marked_for_katex() {
        let r = render("Solve $x^2 = 4$.\n\n$$\\frac{a}{b}$$\n");
        assert!(r.html.contains("math-inline"));
        assert!(r.html.contains("math-display"));
    }

    #[test]
    fn gfm_alerts() {
        let r = render("> [!TIP]\n> Plug in numbers.\n");
        assert!(r.html.contains("markdown-alert-tip"), "{}", r.html);
    }
}
