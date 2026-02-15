# Documentation

This directory contains all documentation for the Music Attribution Scaffold, including the MkDocs site source, architecture plans, the probabilistic PRD, and the RAG-optimized knowledge base.

## Where to Find What

| Directory | Contents |
|---|---|
| `site/` | MkDocs source files (deployed to GitHub Pages) |
| `prd/` | Probabilistic decision network (23 nodes, 5 levels) |
| `prd/decisions/` | Individual decision node YAML files |
| `prd/archetypes/` | Team archetype profiles (engineer-heavy, musician-heavy, etc.) |
| `prd/domains/` | Domain overlay system (music attribution + DPP traceability) |
| `planning/` | Architecture plans, design rationale, task lists |
| `knowledge-base/` | RAG-optimized markdown for LLM consumption |
| `architecture/` | Architecture diagrams and design documents |
| `api/` | API documentation and OpenAPI extensions |
| `figures/` | Generated figures and visual references |
| `sources/` | Source materials (gitignored raw PDFs/HTML go in `raw-sources/`) |

## MkDocs Documentation Site

The project uses [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) for the documentation site, deployed to GitHub Pages.

### Local Preview

```bash
uv run mkdocs serve
```

This starts a local server at `http://localhost:8000` with live reload.

### Build

```bash
uv run mkdocs build --strict
```

The `--strict` flag ensures broken links and missing references cause build failures.

### Site Structure

The navigation is defined in `mkdocs.yml` at the project root. Key sections:

- **Getting Started**: Installation and quickstart guides
- **Concepts**: Oracle Problem, Assurance Levels, Conformal Prediction, etc.
- **User Guide**: Architecture, backend, frontend, agentic UI
- **API Reference**: Auto-generated from Python docstrings via mkdocstrings
- **Tutorials**: Reproducing the paper, adding data sources, API examples

### Adding a New Page

1. Create a `.md` file in the appropriate `docs/site/` subdirectory.
2. Add a nav entry in `mkdocs.yml` under the appropriate section.
3. Preview with `uv run mkdocs serve` to verify rendering.

## Figure Creation

Figures are generated using Nano Banana Pro and stored in `figures/`. Visual references for the editorial design system live in `figures/visual-references/`.

## Knowledge Base

The `knowledge-base/` directory contains markdown files optimized for RAG/LLM consumption. See `knowledge-base/README.md` for the conversion workflow from raw sources to clean markdown.

Important: Raw sources (PDFs, HTML) go in `raw-sources/` which is gitignored. Only clean markdown is committed.
