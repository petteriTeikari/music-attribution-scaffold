# Music Attribution Scaffold

[![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
[![Type checked: mypy](https://img.shields.io/badge/type%20checked-mypy-blue.svg)](https://mypy-lang.org/)
[![Package manager: uv](https://img.shields.io/badge/package%20manager-uv-blueviolet.svg)](https://docs.astral.sh/uv/)
[![Docs](https://img.shields.io/badge/docs-GitHub%20Pages-blue)](https://petteriTeikari.github.io/music-attribution-scaffold/)

**Open-source research scaffold for music attribution with transparent confidence scoring.**

Companion code to: **Teikari, P. (2026). *Governing Generative Music: Attribution Limits, Platform Incentives, and the Future of Creator Income*. SSRN No. 6109087.**
[Read the preprint](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6109087)

---

## What This Repo Demonstrates

- **Multi-source ETL pipeline** -- Fetches and normalizes music metadata from MusicBrainz, Discogs, AcoustID, audio file tags, and artist self-reports into a unified schema.
- **Probabilistic entity resolution with 5-strategy cascade** -- Resolves "is this the same artist?" across sources using exact identifiers, fuzzy string matching, embedding similarity, graph relationships, and LLM-assisted disambiguation.
- **Per-field confidence scoring with conformal calibration** -- Every attribution field carries a calibrated confidence score. "90% confident" actually means 90% coverage via Adaptive Prediction Sets (APS).

This scaffold is **not** a single-architecture implementation. It is a general framework that could be instantiated by teams with very different constraints. The [probabilistic PRD](docs/prd/decisions/REPORT.md) captures these branching paths as a decision network.

---

## Quick Start

```bash
# 1. Clone and set up (installs deps, starts Docker, runs migrations, seeds data)
git clone https://github.com/petteriTeikari/music-attribution-scaffold.git
cd music-attribution-scaffold
make setup

# 2. Start the backend API + PostgreSQL
make dev

# 3. Start the frontend (in a second terminal)
make dev-frontend

# 4. Or start the full agentic UI (backend + CopilotKit sidebar)
make agent
```

The backend API runs at `http://localhost:8000` with Swagger docs at `/docs`. The frontend runs at `http://localhost:3000`.

---

## Architecture Overview

The system is organized as five sequential pipelines connected by typed boundary objects:

```
                      +-----------+     +-----------+     +-----------+
  Audio files  ------>|           |     |           |     |           |
  MusicBrainz ------->|    ETL    |---->|  Entity   |---->|Attribution|
  Discogs ----------->|  Pipeline |     |Resolution |     |  Engine   |
  AcoustID ---------->|           |     |           |     |           |
  Artist input ------>+-----------+     +-----------+     +-----------+
                            |                |                  |
                      NormalizedRecord  ResolvedEntity   AttributionRecord
                            |                |                  |
                            v                v                  v
                      +-----------+     +-----------+
                      |  API/MCP  |<----|   Chat    |
                      |  Server   |     |  Agent    |
                      +-----------+     +-----------+
                            |                |
                      REST + MCP tools  CopilotKit AG-UI
```

Each boundary crossing is a Pydantic model with validation, confidence scores, and provenance metadata. Reverse feedback flows (dispute signals, recalibration requests) travel upstream via `PipelineFeedback` objects.

---

## Project Structure

```
music-attribution-scaffold/
├── src/music_attribution/           # Python package root
│   ├── schemas/                     # Boundary objects (Pydantic models)
│   ├── etl/                         # Data source connectors + quality gate
│   ├── resolution/                  # 5-strategy entity resolution cascade
│   ├── attribution/                 # Aggregation, conformal scoring, priority queue
│   ├── api/                         # FastAPI app factory + routes
│   ├── chat/                        # PydanticAI agent + AG-UI endpoint
│   ├── mcp/                         # MCP permission patchbay server
│   ├── db/                          # SQLAlchemy models + async engine
│   ├── search/                      # Hybrid search (text + vector + graph)
│   ├── pipeline/                    # DAG runner for pipeline orchestration
│   ├── seed/                        # Imogen Heap mock data loader
│   ├── observability/               # Prometheus metrics
│   ├── config.py                    # Pydantic Settings (env vars)
│   ├── constants.py                 # Shared constants
│   └── core.py                      # Core utilities
├── tests/
│   ├── unit/                        # 351 fast tests, mock everything
│   ├── integration/                 # 42 tests, real PostgreSQL via Docker
│   ├── e2e/                         # End-to-end tests
│   └── smoke/                       # Smoke tests
├── frontend/                        # Next.js 15 editorial UI
│   ├── src/app/                     # App Router pages
│   ├── src/components/              # React components
│   └── src/lib/                     # State, data, analytics
├── docker/                          # Dockerfiles (dev, test, prod)
├── alembic/                         # Database migrations
├── docs/                            # Documentation site + planning
│   ├── site/                        # MkDocs source files
│   ├── prd/                         # Probabilistic decision network
│   ├── planning/                    # Architecture plans
│   └── knowledge-base/              # RAG-optimized markdown
├── scripts/                         # Setup, migration, test scripts
├── .claude/                         # AI behavior contract + rules
├── pyproject.toml                   # Single source of truth for deps
├── Makefile                         # Developer commands
└── mkdocs.yml                       # Documentation site config
```

---

## Sample Data

The scaffold ships with 8 Imogen Heap works as seed data, spanning the full confidence spectrum from 0.0 to 0.95. This demonstrates how the system behaves across assurance levels:

| Work Title | Confidence | Assurance | Sources | Status |
|---|---|---|---|---|
| Hide and Seek | 0.95 | A3 (artist-verified) | MB, Discogs, AcoustID, Artist | Verified |
| Tiny Human | 0.91 | A3 (artist-verified) | MB, Discogs, Artist | Verified |
| The Moment I Said It | 0.82 | A2 (multi-source) | MB, Discogs, File | Stable |
| Goodnight and Go | 0.72 | A2 (multi-source) | MB, Discogs | Stable |
| Headlock | 0.58 | A1 (single source) | MB, Discogs | Needs review |
| Just for Now | 0.35 | A1 (single source) | MB only | Needs review |
| 2-1 | 0.28 | A1 (single source) | File metadata only | Needs review |
| Blanket (unreleased) | 0.00 | A0 (no data) | None verified | Needs review |

Each record includes a full provenance chain showing how confidence evolved through fetch, resolve, score, and review events.

---

## Technology Stack

| Layer | Technology |
|---|---|
| **Language** | Python 3.13 |
| **Package Manager** | [uv](https://docs.astral.sh/uv/) (only -- pip/conda banned) |
| **Web Framework** | FastAPI with async SQLAlchemy |
| **Database** | PostgreSQL + pgvector |
| **Migrations** | Alembic |
| **Agent Framework** | PydanticAI (Claude Haiku 4.5 default, FallbackModel) |
| **MCP Server** | FastMCP (mcp-sdk) |
| **Entity Resolution** | Splink + jellyfish + thefuzz + sentence-transformers |
| **Audio Fingerprinting** | AcoustID / Chromaprint |
| **File Metadata** | tinytag (MIT, pure Python) |
| **Observability** | Prometheus metrics, PostHog analytics |
| **Frontend** | Next.js 15 (App Router), React 19, TypeScript strict |
| **CSS** | Tailwind CSS v4, CSS custom property tokens |
| **Frontend State** | Jotai (atoms for theme, role, works) |
| **Agentic UI** | CopilotKit (AG-UI protocol via SSE) |
| **Frontend Testing** | Vitest + React Testing Library + vitest-axe |
| **E2E Testing** | Playwright + @axe-core/playwright |
| **Linter/Formatter** | ruff |
| **Type Checker** | mypy (strict) |
| **Test Framework** | pytest |

---

## Running Tests

```bash
# Unit tests (fast, no Docker needed)
make test-local

# Unit + integration tests in Docker (CI-parity)
make test

# Full CI simulation (lint + typecheck + tests)
make test-all

# Frontend tests (265 Vitest tests including WCAG checks)
make test-frontend

# Coverage report
make test-cov

# Lint and format
make lint-local
make format
```

---

## Documentation

Full documentation is available at the [GitHub Pages site](https://petteriTeikari.github.io/music-attribution-scaffold/).

To preview locally:

```bash
uv run mkdocs serve
```

The docs include getting started guides, concept explainers, API reference (auto-generated from docstrings), and tutorials.

---

## Key Concepts

These concepts from the paper are implemented throughout the scaffold:

**Oracle Problem** -- Digital systems cannot fully verify physical/training reality. The scaffold designs for deterrence (making misattribution costly and traceable) rather than detection (trying to prove ground truth).

**A0-A3 Assurance Levels** -- Tiered provenance verification mapped to industry identifiers:
- **A0** (None): No external verification. Claimed only.
- **A1** (Single source): One database confirms the attribution (e.g., ISRC from MusicBrainz).
- **A2** (Multi-source): Multiple independent sources agree (e.g., MusicBrainz + Discogs).
- **A3** (Artist-verified): Identity-verified confirmation, typically via ISNI + artist self-report.

**Two-Friction Taxonomy** -- Administrative friction (form-filling, manual data entry) should be automated away. Discovery friction (the effort to find and evaluate music) should be preserved as a quality signal.

**Conformal Prediction** -- Confidence scores are calibrated using Adaptive Prediction Sets (APS). A stated 90% confidence interval actually contains the true value at least 90% of the time, unlike typical ML "confidence" that is often miscalibrated.

**MCP as Consent Infrastructure** -- The Model Context Protocol server provides machine-readable permission queries. AI platforms can ask "may I use this recording for training?" and receive structured ALLOW/DENY/ASK responses with conditions.

See the [full concepts documentation](https://petteriTeikari.github.io/music-attribution-scaffold/concepts/) for details.

---

## Contributing

Contributions are welcome. Please follow these guidelines:

1. **Use `uv` for all dependency management** -- never pip, conda, or requirements.txt.
2. **Run `pre-commit run --all-files`** before pushing any changes.
3. **Write tests** for all new functionality. Follow the existing test structure in `tests/`.
4. **Type-annotate** all public functions and use `from __future__ import annotations`.
5. **Use `pathlib.Path`** for file paths and always specify `encoding='utf-8'` for file I/O.
6. **Never modify** sections marked with `# AIDEV-IMMUTABLE`.

See [.claude/CLAUDE.md](.claude/CLAUDE.md) for the full behavior contract.

---

## License

MIT

---

## Citation

If you use this scaffold in your research, please cite:

```bibtex
@article{teikariGoverningGenerativeMusic2026,
	type = {{SSRN} {Scholarly} {Paper}},
	title = {Governing {Generative} {Music}: {Attribution} {Limits}, {Platform} {Incentives}, and the {Future} of {Creator} {Income}},
	shorttitle = {Governing {Generative} {Music}},
	url = {https://doi.org/10.2139/ssrn.6109087},
	doi = {10.2139/ssrn.6109087},
	urldate = {2026-02-03},
	publisher = {Social Science Research Network},
	author = {Teikari, Petteri},
	month = jan,
	year = {2026},
	keywords = {Generative AI, Attribution Infrastructure, Agentic Commerce, Hedonic Consumption, Market Design, Music Industry, Platform Economics, Provenance Verification, Transaction Costs, Voice Cloning}
}
```
