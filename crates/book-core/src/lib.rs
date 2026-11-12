//! Content model and loader for a modular book.
//!
//! A book lives in a directory laid out like this:
//!
//! ```text
//! content/
//!   book.toml                 # book-wide settings (title, module order, ...)
//!   modules/
//!     01-arithmetic/
//!       module.toml           # module title + summary
//!       01-number-properties.md
//!       02-fractions.md
//!     02-algebra/
//!       ...
//! ```
//!
//! Every module is self-contained: add, remove or reorder a folder and the
//! site navigation follows. Numeric prefixes (`01-`) control ordering and are
//! stripped from URLs.

pub mod markdown;
pub mod search;

use anyhow::{Context, Result, bail};
use serde::Deserialize;
use std::fs;
use std::path::{Path, PathBuf};

pub use markdown::{Heading, Rendered};

/// `content/book.toml`
#[derive(Debug, Clone, Deserialize)]
pub struct BookConfig {
    pub title: String,
    #[serde(default)]
    pub subtitle: String,
    #[serde(default)]
    pub description: String,
    #[serde(default)]
    pub authors: Vec<String>,
    #[serde(default)]
    pub repository: Option<String>,
    /// Branch + path used for "Edit this page" links, e.g. `main/content`.
    #[serde(default = "default_edit_path")]
    pub edit_path: String,
    /// URL prefix the site is served under (`/` or `/repo-name/`).
    #[serde(default = "default_base_url")]
    pub base_url: String,
    /// Explicit module directory order. Empty = all directories, sorted.
    #[serde(default)]
    pub modules: Vec<String>,
    #[serde(default)]
    pub license: Option<String>,
}

fn default_base_url() -> String {
    "/".into()
}
fn default_edit_path() -> String {
    "main/content".into()
}

/// `content/modules/<dir>/module.toml`
#[derive(Debug, Clone, Deserialize)]
struct ModuleConfig {
    title: String,
    #[serde(default)]
    summary: String,
    /// Optional part heading (e.g. "Part II · Mathematics for AI") that
    /// groups consecutive modules in the navigation.
    #[serde(default)]
    part: Option<String>,
    /// Module is skipped when `draft = true`.
    #[serde(default)]
    draft: bool,
}

/// Optional TOML front matter at the top of a chapter, fenced by `+++`.
#[derive(Debug, Default, Deserialize)]
struct FrontMatter {
    title: Option<String>,
    #[serde(default)]
    summary: String,
    #[serde(default)]
    draft: bool,
}

#[derive(Debug, Clone)]
pub struct Book {
    pub config: BookConfig,
    pub modules: Vec<Module>,
}

#[derive(Debug, Clone)]
pub struct Module {
    /// Directory name, e.g. `01-arithmetic`.
    pub dir: String,
    /// URL segment, e.g. `arithmetic`.
    pub slug: String,
    pub title: String,
    pub summary: String,
    pub part: Option<String>,
    pub chapters: Vec<Chapter>,
}

#[derive(Debug, Clone)]
pub struct Chapter {
    pub slug: String,
    pub title: String,
    pub summary: String,
    /// Path relative to the content root (used for "edit" links).
    pub source: String,
    pub html: String,
    pub headings: Vec<Heading>,
    pub plain_text: String,
}

/// A position in reading order, for prev/next links.
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub struct ChapterRef {
    pub module: usize,
    pub chapter: usize,
}

impl Book {
    /// Load and render a whole book from a content directory.
    pub fn load(root: &Path) -> Result<Self> {
        let cfg_path = root.join("book.toml");
        let mut config: BookConfig = toml::from_str(
            &fs::read_to_string(&cfg_path)
                .with_context(|| format!("reading {}", cfg_path.display()))?,
        )
        .with_context(|| format!("parsing {}", cfg_path.display()))?;
        if !config.base_url.ends_with('/') {
            config.base_url.push('/');
        }
        if !config.base_url.starts_with('/') {
            config.base_url.insert(0, '/');
        }

        let modules_dir = root.join("modules");
        let dirs: Vec<String> = if config.modules.is_empty() {
            sorted_entries(&modules_dir, |p| p.is_dir())?
        } else {
            config.modules.clone()
        };

        let mut modules = Vec::new();
        for dir in dirs {
            if let Some(m) = load_module(root, &modules_dir.join(&dir), &dir)? {
                if modules.iter().any(|o: &Module| o.slug == m.slug) {
                    bail!("two modules share the URL slug `{}`", m.slug);
                }
                modules.push(m);
            }
        }
        Ok(Book { config, modules })
    }

    /// All chapters in reading order.
    pub fn reading_order(&self) -> Vec<ChapterRef> {
        self.modules
            .iter()
            .enumerate()
            .flat_map(|(mi, m)| {
                (0..m.chapters.len()).map(move |ci| ChapterRef {
                    module: mi,
                    chapter: ci,
                })
            })
            .collect()
    }

    pub fn chapter(&self, r: ChapterRef) -> (&Module, &Chapter) {
        let m = &self.modules[r.module];
        (m, &m.chapters[r.chapter])
    }

    pub fn module_url(&self, m: &Module) -> String {
        format!("{}{}/", self.config.base_url, m.slug)
    }

    pub fn chapter_url(&self, m: &Module, c: &Chapter) -> String {
        format!("{}{}/{}/", self.config.base_url, m.slug, c.slug)
    }

    pub fn asset_url(&self, path: &str) -> String {
        format!("{}{}", self.config.base_url, path.trim_start_matches('/'))
    }

    pub fn edit_url(&self, c: &Chapter) -> Option<String> {
        self.config.repository.as_ref().map(|repo| {
            format!(
                "{}/edit/{}/{}",
                repo.trim_end_matches('/'),
                self.config.edit_path.trim_matches('/'),
                c.source
            )
        })
    }

    /// The part heading to show before module `mi`, if it starts a new part.
    pub fn part_start(&self, mi: usize) -> Option<&str> {
        let part = self.modules[mi].part.as_deref()?;
        let prev = mi
            .checked_sub(1)
            .and_then(|p| self.modules[p].part.as_deref());
        (prev != Some(part)).then_some(part)
    }

    pub fn chapter_count(&self) -> usize {
        self.modules.iter().map(|m| m.chapters.len()).sum()
    }
}

fn load_module(root: &Path, dir: &Path, name: &str) -> Result<Option<Module>> {
    let cfg_path = dir.join("module.toml");
    let cfg: ModuleConfig = toml::from_str(
        &fs::read_to_string(&cfg_path)
            .with_context(|| format!("reading {}", cfg_path.display()))?,
    )
    .with_context(|| format!("parsing {}", cfg_path.display()))?;
    if cfg.draft {
        return Ok(None);
    }

    let mut chapters = Vec::new();
    for file in sorted_entries(dir, |p| p.extension().is_some_and(|e| e == "md"))? {
        let path = dir.join(&file);
        let raw =
            fs::read_to_string(&path).with_context(|| format!("reading {}", path.display()))?;
        let (fm, body) = split_front_matter(&raw)
            .with_context(|| format!("front matter in {}", path.display()))?;
        if fm.draft {
            continue;
        }
        let rendered = markdown::render(body);
        let title = fm
            .title
            .or_else(|| rendered.title.clone())
            .unwrap_or_else(|| file.trim_end_matches(".md").to_string());
        let source = path
            .strip_prefix(root)
            .unwrap_or(&path)
            .to_string_lossy()
            .replace('\\', "/");
        chapters.push(Chapter {
            slug: slugify_name(file.trim_end_matches(".md")),
            title,
            summary: fm.summary,
            source,
            html: rendered.html,
            headings: rendered.headings,
            plain_text: rendered.plain_text,
        });
    }

    Ok(Some(Module {
        dir: name.to_string(),
        slug: slugify_name(name),
        title: cfg.title,
        summary: cfg.summary,
        part: cfg.part,
        chapters,
    }))
}

fn split_front_matter(raw: &str) -> Result<(FrontMatter, &str)> {
    let trimmed = raw.trim_start_matches('\u{feff}');
    if let Some(rest) = trimmed.strip_prefix("+++") {
        if let Some(end) = rest.find("\n+++") {
            let fm: FrontMatter = toml::from_str(&rest[..end])?;
            let body = rest[end + 4..].trim_start_matches(['\r', '\n']);
            return Ok((fm, body));
        }
        bail!("unterminated `+++` front matter");
    }
    Ok((FrontMatter::default(), trimmed))
}

fn sorted_entries(dir: &Path, keep: impl Fn(&PathBuf) -> bool) -> Result<Vec<String>> {
    let mut names: Vec<String> = fs::read_dir(dir)
        .with_context(|| format!("listing {}", dir.display()))?
        .filter_map(|e| e.ok().map(|e| e.path()))
        .filter(|p| keep(p))
        .filter_map(|p| p.file_name().map(|n| n.to_string_lossy().into_owned()))
        .filter(|n| !n.starts_with(['.', '_']))
        .collect();
    names.sort();
    Ok(names)
}

/// `01-number-properties` -> `number-properties`
pub fn slugify_name(name: &str) -> String {
    let stripped = name.trim_start_matches(|c: char| c.is_ascii_digit());
    let stripped = stripped.strip_prefix(['-', '_']).unwrap_or(stripped);
    let base = if stripped.is_empty() { name } else { stripped };
    markdown::slugify(base)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn strips_numeric_prefix() {
        assert_eq!(slugify_name("01-number-properties"), "number-properties");
        assert_eq!(slugify_name("10_Word Problems"), "word-problems");
        assert_eq!(slugify_name("2024"), "2024");
    }

    #[test]
    fn part_headings_start_groups() {
        let module = |part: Option<&str>| Module {
            dir: String::new(),
            slug: String::new(),
            title: String::new(),
            summary: String::new(),
            part: part.map(str::to_string),
            chapters: vec![],
        };
        let book = Book {
            config: toml::from_str("title = \"t\"").unwrap(),
            modules: vec![
                module(Some("A")),
                module(Some("A")),
                module(None),
                module(Some("B")),
            ],
        };
        let starts: Vec<_> = (0..4).map(|i| book.part_start(i)).collect();
        assert_eq!(starts, [Some("A"), None, None, Some("B")]);
    }

    #[test]
    fn front_matter() {
        let (fm, body) = split_front_matter("+++\ntitle = \"Hi\"\n+++\n\n# Body").unwrap();
        assert_eq!(fm.title.as_deref(), Some("Hi"));
        assert_eq!(body, "# Body");
        let (fm, body) = split_front_matter("# No fm").unwrap();
        assert!(fm.title.is_none());
        assert_eq!(body, "# No fm");
    }
}
