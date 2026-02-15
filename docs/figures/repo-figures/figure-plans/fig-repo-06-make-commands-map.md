# fig-repo-06: Make Commands Map

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-repo-06 |
| **Title** | Make Commands Map: Developer Command Interface |
| **Audience** | Technical (daily contributors) |
| **Complexity** | L2 (reference) |
| **Location** | README.md, CONTRIBUTING.md |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

The Makefile is the primary developer interface. This figure maps all make targets organized by category, showing which commands run in Docker (CI-parity) versus locally, and the dependency relationships between them. It helps developers choose the right command for their workflow.

The key message is: "Seven command categories, two execution modes (Docker for CI-parity, local for speed) -- always start with `make help` if unsure."

## Visual Concept (ASCII Layout)

```
+-----------------------------------------------------------------------+
|  MAKE COMMANDS MAP                                                     |
|  ■ Developer Command Interface                                         |
+-----------------------------------------------------------------------+
|                                                                        |
|  ┌─── DOCKER (CI-PARITY) ─────────────────────────────────────────┐   |
|  │                                                                 │   |
|  │  I. DEPS              II. DEV STACK         III. TESTING        │   |
|  │  ─────                ─────────             ────────            │   |
|  │  install              dev ──┐               test ■              │   |
|  │  install-dev          dev-down  │               test-all            │   |
|  │  setup ■              dev-logs  │               lint                 │   |
|  │                       ─────────┘               ci-docker            │   |
|  │                       postgres + pgbouncer                      │   |
|  │                       + valkey + backend                        │   |
|  │                       + frontend                                │   |
|  └─────────────────────────────────────────────────────────────────┘   |
|                                                                        |
|  ┌─── LOCAL (FAST ITERATION) ─────────────────────────────────────┐   |
|  │                                                                 │   |
|  │  IV. TESTING           V. QUALITY           VI. CLEANUP         │   |
|  │  ────────              ───────              ───────             │   |
|  │  test-local            lint-local           clean               │   |
|  │  test-integration      format               docker-clean        │   |
|  │  test-cov              typecheck                                │   |
|  │                        ci-local                                 │   |
|  └─────────────────────────────────────────────────────────────────┘   |
|                                                                        |
|  ┌─── FRONTEND ─────────────┐  ┌─── AGENT ──────────────────────┐    |
|  │  VII. NEXT.JS            │  │  VIII. PYDANTICAI + AG-UI      │    |
|  │  dev-frontend (:3000)    │  │  agent (:8000)                 │    |
|  │  test-frontend           │  │  dev-agent (both)              │    |
|  │  lint-frontend           │  └─────────────────────────────────┘    |
|  │  build-frontend          │                                         |
|  │  test-e2e                │  $ make help  ──▶  Show all targets     |
|  │  test-e2e-ui             │                                         |
|  └───────────────────────────┘                                         |
+-----------------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title | `heading_display` | "MAKE COMMANDS MAP" Instrument Serif ALL-CAPS |
| Docker zone box | `zone_docker` | Elevated panel, coral border for CI-parity commands |
| Local zone box | `zone_local` | Standard panel for fast-iteration commands |
| Frontend zone | `zone_frontend` | Separate smaller panel |
| Agent zone | `zone_agent` | Separate smaller panel |
| Command names | `data_mono` | IBM Plex Mono, each make target |
| Category headers (I-VIII) | `section_numeral` | Roman numerals with editorial caps |
| Docker badge | `badge_docker` | Indicator showing "runs in Docker" |
| Local badge | `badge_local` | Indicator showing "runs locally" |
| Accent squares on key commands | `accent_square` | Coral squares marking most-used commands (setup, test) |
| Port annotations | `annotation` | :3000, :8000 port labels |
| `make help` callout | `callout_tip` | Bottom-right, highlighted suggestion |

## Anti-Hallucination Rules

1. All make targets listed must exist in the actual Makefile -- cross-reference with the Makefile.
2. `make test` runs in Docker via `scripts/test-docker.sh --build`, NOT bare pytest.
3. `make test-local` runs `.venv/bin/python -m pytest tests/` locally.
4. `make dev` uses `docker-compose.dev.yml`, not `docker-compose.yml`.
5. `make lint` runs in Docker; `make lint-local` runs locally via `uv run ruff`.
6. Frontend runs on port 3000, backend/agent on port 8000.
7. `make setup` runs `scripts/setup.sh` for one-command setup.
8. There is no `make deploy` or `make prod` target -- do not invent targets.
9. `make ci-docker` is an alias for `make test-all`.

## Alt Text

Reference card: Makefile developer command interface for the music attribution scaffold organized into eight categories across Docker CI-parity and local fast-iteration modes, covering dependency management with uv, testing with pytest, linting with ruff and mypy, Next.js 15 frontend commands, and PydanticAI agent workflows -- a single entry point for all development tasks.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Reference card: Makefile developer command interface for the music attribution scaffold organized into eight categories across Docker CI-parity and local fast-iteration modes, covering dependency management with uv, testing with pytest, linting with ruff and mypy, Next.js 15 frontend commands, and PydanticAI agent workflows -- a single entry point for all development tasks.](docs/figures/repo-figures/assets/fig-repo-06-make-commands-map.jpg)

*Figure 6. The Makefile serves as the primary developer interface, organizing all commands into Docker-based (CI-parity) and local (fast-iteration) execution modes, ensuring contributors always use the correct environment for their workflow.*

### From this figure plan (relative)

![Reference card: Makefile developer command interface for the music attribution scaffold organized into eight categories across Docker CI-parity and local fast-iteration modes, covering dependency management with uv, testing with pytest, linting with ruff and mypy, Next.js 15 frontend commands, and PydanticAI agent workflows -- a single entry point for all development tasks.](../assets/fig-repo-06-make-commands-map.jpg)
