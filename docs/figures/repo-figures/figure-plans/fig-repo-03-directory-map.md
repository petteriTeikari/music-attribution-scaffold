# fig-repo-03: Directory Map

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-repo-03 |
| **Title** | Annotated Directory Tree: Where Everything Lives |
| **Audience** | All (new contributors, code reviewers) |
| **Complexity** | L1 (orientation) |
| **Location** | README.md, CONTRIBUTING.md |
| **Priority** | P0 (Critical) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

New contributors need to know where things live. This figure provides an annotated directory tree with color-coded zones showing the backend source, frontend, tests, configuration, documentation, and Docker infrastructure. The annotation callouts explain what each top-level directory contains without requiring the reader to open files.

The key message is: "The repository has a clear separation of concerns -- backend Python in src/, frontend Next.js in frontend/, tests mirroring source, and all configuration at root level."

## Visual Concept (ASCII Layout)

```
+-----------------------------------------------------------------------+
|  DIRECTORY MAP                                                         |
|  ■ Where Everything Lives                                              |
+-----------------------------------------------------------------------+
|                                                                        |
|  music-attribution-scaffold/                                           |
|  ├── src/music_attribution/  ◄─── BACKEND SOURCE ──────────── ■      |
|  │   ├── api/                     FastAPI routes + app factory         |
|  │   ├── etl/                     Pipeline I: source adapters          |
|  │   ├── resolution/              Pipeline II: entity matching         |
|  │   ├── attribution/             Pipeline III: confidence scoring     |
|  │   ├── chat/                    Pipeline V: PydanticAI agent         |
|  │   ├── mcp/                     Pipeline IV: MCP permission server   |
|  │   ├── schemas/                 Pydantic boundary objects            |
|  │   ├── db/                      SQLAlchemy models + engine           |
|  │   └── config.py                Settings via pydantic-settings       |
|  │                                                                     |
|  ├── frontend/               ◄─── FRONTEND ────────────────── ■      |
|  │   └── src/app/                 Next.js 15 App Router pages          |
|  │   └── src/components/          React components (19 modules)        |
|  │                                                                     |
|  ├── tests/                  ◄─── TESTS ──────────────────── ■       |
|  │   ├── unit/                    351 unit tests                       |
|  │   ├── integration/             42 integration tests (testcontainers)|
|  │   └── e2e/                     Playwright browser tests             |
|  │                                                                     |
|  ├── docker/                 ◄─── INFRASTRUCTURE ──────────── ■      |
|  ├── .claude/                ◄─── AI CONFIG ─────────────────  ■     |
|  ├── docs/                   ◄─── DOCUMENTATION ──────────────  ■    |
|  ├── alembic/                ◄─── MIGRATIONS ─────────────────  ■    |
|  ├── scripts/                ◄─── BUILD SCRIPTS ──────────────  ■    |
|  ├── pyproject.toml               Single source of truth for deps      |
|  └── Makefile                     Developer command interface          |
+-----------------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title | `heading_display` | "DIRECTORY MAP" Instrument Serif ALL-CAPS |
| Tree structure | `data_mono` | IBM Plex Mono tree with unicode box-drawing characters |
| Backend zone | `zone_backend` | Coral accent square + annotation callout |
| Frontend zone | `zone_frontend` | Teal accent marker |
| Tests zone | `zone_tests` | Green accent marker |
| Infrastructure zone | `zone_infra` | Gray accent marker |
| AI Config zone | `zone_ai` | Purple accent marker |
| Annotation callouts | `label_editorial` | Plus Jakarta Sans descriptions right-aligned |
| Pipeline cross-references | `cross_ref` | "Pipeline I", "Pipeline II" etc. linking to fig-repo-02 |
| Accent squares | `accent_square` | Coral squares as zone markers |

## Anti-Hallucination Rules

1. The source directory is `src/music_attribution/` (not `src/app/` or `music_attribution/` at root).
2. There are exactly these subdirectories under src/music_attribution/: api, attribution, chat, cli, confidence, config.py, constants.py, core.py, db, etl, feedback, mcp, observability, permissions, pipeline, quality, resolution, schemas, search, seed.
3. The frontend is in `frontend/` with Next.js 15 App Router (pages in `frontend/src/app/`).
4. Test counts: 351 unit + 42 integration + 265 frontend Vitest tests -- do not invent other numbers.
5. Configuration single source of truth is `pyproject.toml`, not requirements.txt or setup.py.
6. The `.claude/` directory contains AI assistant configuration, not a Claude API client.
7. Package manager is uv (not pip, not conda).
8. Do NOT show files that do not exist in the repository.

## Alt Text

Reference card: annotated directory tree of the open-source music attribution scaffold showing Python 3.13 backend in src/music_attribution with five pipeline modules, Next.js 15 frontend, 393 backend tests plus 265 frontend tests, Docker infrastructure, and pyproject.toml as the single source of truth for dependency management via uv.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Reference card: annotated directory tree of the open-source music attribution scaffold showing Python 3.13 backend in src/music_attribution with five pipeline modules, Next.js 15 frontend, 393 backend tests plus 265 frontend tests, Docker infrastructure, and pyproject.toml as the single source of truth for dependency management via uv.](docs/figures/repo-figures/assets/fig-repo-03-directory-map.jpg)

*Figure 3. The repository follows a clear separation of concerns: backend Python source in src/music_attribution/ maps directly to the five-pipeline architecture, while tests mirror the source structure and all configuration converges on pyproject.toml as the single source of truth.*

### From this figure plan (relative)

![Reference card: annotated directory tree of the open-source music attribution scaffold showing Python 3.13 backend in src/music_attribution with five pipeline modules, Next.js 15 frontend, 393 backend tests plus 265 frontend tests, Docker infrastructure, and pyproject.toml as the single source of truth for dependency management via uv.](../assets/fig-repo-03-directory-map.jpg)
