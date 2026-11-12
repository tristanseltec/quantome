# List recipes
default:
    @just --list

# Build the static site into ./dist
build:
    cargo run --release -p book-cli -- build

# Live preview at http://127.0.0.1:3000 (rebuilds on change)
serve port="3000":
    cargo run --release -p book-cli -- serve --port {{port}}

# Scaffold a module:  just module "Geometry"
module title:
    cargo run -q -p book-cli -- new module "{{title}}"

# Scaffold a chapter: just chapter algebra "Quadratics"
chapter module title:
    cargo run -q -p book-cli -- new chapter {{module}} "{{title}}"

# Validate content (links, answers, front matter)
content-check:
    cargo run --release -p book-cli -- check

# Tests + lints + content validation (what CI runs)
check: content-check
    cargo fmt --all --check
    cargo clippy --workspace --all-targets -- -D warnings
    cargo test --workspace
