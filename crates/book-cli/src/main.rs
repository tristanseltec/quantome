//! `book` — build, preview and extend the modular book.
//!
//! ```text
//! book build                       # render ./content into ./dist
//! book serve --port 3000           # build, serve, rebuild on change
//! book new module "Geometry"       # scaffold content/modules/NN-geometry
//! book new chapter geometry "Circles"
//! ```

use anyhow::{Context, Result, bail};
use book_core::{Book, markdown::slugify, search};
use clap::{Parser, Subcommand};
use std::fs;
use std::path::{Path, PathBuf};
use std::sync::Arc;
use std::time::{Duration, Instant, SystemTime};

#[derive(Parser)]
#[command(name = "book", version, about = "Build and serve the modular book")]
struct Cli {
    /// Content directory (contains book.toml and modules/)
    #[arg(long, global = true, default_value = "content")]
    content: PathBuf,
    /// Static assets copied to <out>/assets
    #[arg(long, global = true, default_value = "assets")]
    assets: PathBuf,
    /// Output directory
    #[arg(long, global = true, default_value = "dist")]
    out: PathBuf,
    #[command(subcommand)]
    cmd: Cmd,
}

#[derive(Subcommand)]
enum Cmd {
    /// Render the whole book to static HTML.
    Build {
        /// Override `base_url` from book.toml (e.g. `/my-repo/` for GitHub Pages).
        #[arg(long)]
        base_url: Option<String>,
    },
    /// Build, serve locally and rebuild when content changes.
    Serve {
        #[arg(long, default_value_t = 3000)]
        port: u16,
    },
    /// Build, then validate the output: internal links, answer blocks, summaries.
    /// Exits non-zero on any problem, so CI and contributors can rely on it.
    Check,
    /// Scaffold new content.
    #[command(subcommand)]
    New(New),
}

#[derive(Subcommand)]
enum New {
    /// Create a new module folder with module.toml and a first chapter.
    Module { title: String },
    /// Add a chapter to an existing module (match by slug or folder name).
    Chapter { module: String, title: String },
}

fn main() -> Result<()> {
    let cli = Cli::parse();
    match &cli.cmd {
        Cmd::Build { base_url } => {
            build(&cli, base_url.as_deref())?;
        }
        Cmd::Serve { port } => serve(&cli, *port)?,
        Cmd::Check => check(&cli)?,
        Cmd::New(New::Module { title }) => new_module(&cli.content, title)?,
        Cmd::New(New::Chapter { module, title }) => new_chapter(&cli.content, module, title)?,
    }
    Ok(())
}

fn build(cli: &Cli, base_url: Option<&str>) -> Result<()> {
    let t = Instant::now();
    let mut book = Book::load(&cli.content)?;
    if let Some(b) = base_url {
        book.config.base_url = format!("/{}/", b.trim_matches('/')).replace("//", "/");
    }
    let book = Arc::new(book);

    if cli.out.exists() {
        fs::remove_dir_all(&cli.out).with_context(|| format!("cleaning {}", cli.out.display()))?;
    }
    let pages = book_ui::render_site(book.clone());
    for p in &pages {
        let path = cli.out.join(&p.path);
        fs::create_dir_all(path.parent().unwrap())?;
        fs::write(&path, &p.html)?;
    }
    let index = serde_json::to_string(&search::build_index(&book))?;
    fs::create_dir_all(cli.out.join("assets"))?;
    fs::write(cli.out.join("assets/search-index.json"), index)?;
    copy_dir(&cli.assets, &cli.out.join("assets"))?;
    // Images and other files that live next to the content.
    let static_dir = cli.content.join("static");
    if static_dir.is_dir() {
        copy_dir(&static_dir, &cli.out)?;
    }

    println!(
        "Built {} modules, {} chapters, {} pages → {} in {:.0?}",
        book.modules.len(),
        book.chapter_count(),
        pages.len(),
        cli.out.display(),
        t.elapsed()
    );
    Ok(())
}

fn check(cli: &Cli) -> Result<()> {
    // Build with a sub-path base URL so absolute links that ignore
    // `base_url` are caught too.
    build(cli, Some("/__check__/"))?;
    let book = Book::load(&cli.content)?;
    let mut problems = Vec::new();

    for m in &book.modules {
        for c in &m.chapters {
            if c.summary.is_empty() {
                problems.push(format!("{}: missing `summary` in front matter", c.source));
            }
        }
    }

    let mut pages = Vec::new();
    collect_html(&cli.out, &mut pages)?;
    for page in &pages {
        let html = fs::read_to_string(page)?;
        let rel = page
            .strip_prefix(&cli.out)
            .unwrap_or(page)
            .display()
            .to_string();
        if html.matches("<details").count() != html.matches("</details>").count() {
            problems.push(format!("{rel}: unbalanced <details> blocks"));
        }
        let dir = page.parent().unwrap();
        for href in html
            .split("href=\"")
            .skip(1)
            .filter_map(|s| s.split('"').next())
        {
            let target = href.split('#').next().unwrap_or("");
            if target.is_empty() || target.contains("://") || target.starts_with("mailto:") {
                continue;
            }
            let path = match target.strip_prefix("/__check__/") {
                Some(rest) => cli.out.join(rest),
                None if target.starts_with('/') => {
                    problems.push(format!(
                        "{rel}: link `{href}` ignores base_url (use a relative link)"
                    ));
                    continue;
                }
                None => dir.join(target),
            };
            let path = if target.ends_with('/') {
                path.join("index.html")
            } else {
                path
            };
            if !path.exists() {
                problems.push(format!("{rel}: broken link `{href}`"));
            }
        }
    }

    // Leave a normal build behind.
    build(cli, None)?;
    if problems.is_empty() {
        println!("✓ check passed: {} pages, no problems", pages.len());
        Ok(())
    } else {
        problems.sort();
        problems.dedup();
        for p in &problems {
            eprintln!("✗ {p}");
        }
        bail!("{} problem(s) found", problems.len())
    }
}

fn collect_html(dir: &Path, out: &mut Vec<PathBuf>) -> Result<()> {
    for entry in fs::read_dir(dir)? {
        let path = entry?.path();
        if path.is_dir() {
            collect_html(&path, out)?;
        } else if path.extension().is_some_and(|e| e == "html") {
            out.push(path);
        }
    }
    Ok(())
}

fn copy_dir(from: &Path, to: &Path) -> Result<()> {
    if !from.is_dir() {
        return Ok(());
    }
    fs::create_dir_all(to)?;
    for entry in fs::read_dir(from)? {
        let entry = entry?;
        let dest = to.join(entry.file_name());
        if entry.file_type()?.is_dir() {
            copy_dir(&entry.path(), &dest)?;
        } else {
            fs::copy(entry.path(), dest)?;
        }
    }
    Ok(())
}

fn serve(cli: &Cli, port: u16) -> Result<()> {
    build(cli, Some("/"))?;

    // Poll for changes — no extra dependencies, plenty fast for a book.
    let watched = [cli.content.clone(), cli.assets.clone()];
    let (content, assets, out) = (cli.content.clone(), cli.assets.clone(), cli.out.clone());
    std::thread::spawn(move || {
        let cli = Cli {
            content,
            assets,
            out,
            cmd: Cmd::Build { base_url: None },
        };
        let mut last = newest_mtime(&watched);
        loop {
            std::thread::sleep(Duration::from_millis(500));
            let now = newest_mtime(&watched);
            if now > last {
                last = now;
                if let Err(e) = build(&cli, Some("/")) {
                    eprintln!("build failed: {e:#}");
                }
            }
        }
    });

    let out = cli.out.clone();
    tokio::runtime::Runtime::new()?.block_on(async move {
        use tower_http::services::{ServeDir, ServeFile};
        let svc = ServeDir::new(&out).not_found_service(ServeFile::new(out.join("404.html")));
        let app = axum::Router::new().fallback_service(svc);
        let listener = tokio::net::TcpListener::bind(("127.0.0.1", port)).await?;
        println!("Serving on http://127.0.0.1:{port}  (watching for changes, Ctrl+C to stop)");
        axum::serve(listener, app).await?;
        Ok(())
    })
}

fn newest_mtime(dirs: &[PathBuf]) -> SystemTime {
    fn walk(p: &Path, best: &mut SystemTime) {
        if let Ok(meta) = fs::metadata(p) {
            if let Ok(m) = meta.modified() {
                *best = (*best).max(m);
            }
            if meta.is_dir()
                && let Ok(rd) = fs::read_dir(p)
            {
                for e in rd.flatten() {
                    walk(&e.path(), best);
                }
            }
        }
    }
    let mut best = SystemTime::UNIX_EPOCH;
    for d in dirs {
        walk(d, &mut best);
    }
    best
}

fn new_module(content: &Path, title: &str) -> Result<()> {
    let modules = content.join("modules");
    let next = fs::read_dir(&modules)?
        .flatten()
        .filter_map(|e| {
            e.file_name()
                .to_string_lossy()
                .split('-')
                .next()?
                .parse::<u32>()
                .ok()
        })
        .max()
        .map_or(1, |n| n + 1);
    let dir = modules.join(format!("{next:02}-{}", slugify(title)));
    fs::create_dir_all(&dir)?;
    fs::write(
        dir.join("module.toml"),
        format!(
            "title = {title:?}\nsummary = \"One sentence describing what this module covers.\"\n"
        ),
    )?;
    write_chapter(&dir.join("01-introduction.md"), "Introduction")?;
    println!("Created {}", dir.display());
    println!(
        "If book.toml lists `modules = [...]`, add \"{}\" there.",
        dir.file_name().unwrap().to_string_lossy()
    );
    Ok(())
}

fn new_chapter(content: &Path, module: &str, title: &str) -> Result<()> {
    let modules = content.join("modules");
    let dir = fs::read_dir(&modules)?
        .flatten()
        .map(|e| e.path())
        .find(|p| {
            let name = p.file_name().unwrap().to_string_lossy();
            name == module || book_core::slugify_name(&name) == module
        });
    let Some(dir) = dir else {
        bail!("no module named `{module}` in {}", modules.display())
    };
    let next = fs::read_dir(&dir)?
        .flatten()
        .filter_map(|e| {
            e.file_name()
                .to_string_lossy()
                .split('-')
                .next()?
                .parse::<u32>()
                .ok()
        })
        .max()
        .map_or(1, |n| n + 1);
    let path = dir.join(format!("{next:02}-{}.md", slugify(title)));
    write_chapter(&path, title)?;
    println!("Created {}", path.display());
    Ok(())
}

fn write_chapter(path: &Path, title: &str) -> Result<()> {
    if path.exists() {
        bail!("{} already exists", path.display());
    }
    fs::write(
        path,
        format!(
            "+++\nsummary = \"What the reader will be able to do after this chapter.\"\n+++\n\n\
             # {title}\n\n## Key ideas\n\nWrite the concept here. Inline math: $x^2 + y^2 = r^2$.\n\n\
             > [!TIP]\n> A strategy or shortcut.\n\n## Worked example\n\n**Problem.** …\n\n\
             **Solution.** …\n\n## Practice\n\n1. …\n\n<details>\n<summary>Answer</summary>\n\n…\n\n</details>\n"
        ),
    )?;
    Ok(())
}
