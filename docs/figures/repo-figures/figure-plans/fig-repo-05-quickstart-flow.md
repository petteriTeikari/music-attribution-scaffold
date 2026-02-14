# fig-repo-05: Quickstart Flow

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-repo-05 |
| **Title** | Quickstart: Clone to Running in Four Steps |
| **Audience** | All (new contributors, evaluators) |
| **Complexity** | L1 (tutorial) |
| **Location** | README.md quickstart section, CONTRIBUTING.md |
| **Priority** | P0 (Critical) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

A step-by-step visual showing how to go from zero to a running local development environment. Uses Roman numerals (Warp Records homage) for the four steps. Each step shows the command and what it does, with a visual indicator of completion. The goal is to make the repo feel approachable -- "you can have this running in under 5 minutes."

The key message is: "Four commands from clone to a fully running development stack with PostgreSQL, backend, and frontend."

## Visual Concept (ASCII Layout)

```
+-----------------------------------------------------------------------+
|  QUICKSTART                                                            |
|  ■ Clone to Running in Under 5 Minutes                                |
+-----------------------------------------------------------------------+
|                                                                        |
|  I. CLONE + INSTALL                                                    |
|  ─────────────────                                                     |
|  $ git clone <repo-url>                                                |
|  $ cd music-attribution-scaffold                                       |
|  $ make install-dev              ──▶  uv sync + pre-commit install     |
|                                                    ■ DONE              |
|                                                                        |
|  II. START INFRASTRUCTURE                                              |
|  ────────────────────────                                              |
|  $ make dev                      ──▶  Docker Compose: postgres +       |
|                                       pgbouncer + valkey + backend +   |
|                                       frontend                         |
|                                                    ■ DONE              |
|                                                                        |
|  III. VERIFY                                                           |
|  ───────────                                                           |
|  localhost:8000/health           ──▶  Backend health check             |
|  localhost:3000                  ──▶  Frontend dashboard                |
|                                                    ■ DONE              |
|                                                                        |
|  IV. RUN TESTS                                                         |
|  ─────────────                                                         |
|  $ make test                     ──▶  Docker-isolated unit tests       |
|  $ make test-frontend            ──▶  265 Vitest tests                 |
|                                                    ■ DONE              |
|                                                                        |
+-----------------------------------------------------------------------+
|  Prerequisites: git, Docker, uv (curl -LsSf astral.sh/uv | sh)       |
+-----------------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title | `heading_display` | "QUICKSTART" Instrument Serif ALL-CAPS |
| Subtitle | `label_editorial` | "Clone to Running in Under 5 Minutes" Plus Jakarta Sans |
| Roman numeral steps I-IV | `section_numeral` | Large editorial numerals |
| Command blocks | `data_mono` | IBM Plex Mono, monospace terminal commands |
| Explanation arrows | `primary_pathway` | Coral arrows from command to description |
| Completion markers | `accent_square` | Coral squares with "DONE" label |
| Step descriptions | `label_editorial` | Plus Jakarta Sans, what each command does |
| Prerequisites footer | `footer_bar` | Git, Docker, uv with install URL |
| Progress line | `accent_line_v` | Vertical coral line connecting all four steps |

## Anti-Hallucination Rules

1. The install command is `make install-dev` which runs `uv sync --frozen --group dev --group test` and `uv run pre-commit install`.
2. The dev command is `make dev` which runs `docker compose -f docker-compose.dev.yml up --build`.
3. Backend runs on port 8000, frontend on port 3000 -- do not swap these.
4. The health endpoint is `/health` on port 8000.
5. Prerequisites are git, Docker (with Compose), and uv -- NOT pip, NOT Node.js (npm is installed via Docker).
6. The uv install command is `curl -LsSf https://astral.sh/uv/install.sh | sh`.
7. `make test` runs tests in Docker (CI-parity), not bare pytest.
8. Do NOT mention conda, virtualenv, or pyenv -- uv handles everything.
9. Frontend tests are 265 Vitest tests, not Jest tests.

## Alt Text

Workflow diagram: four-step quickstart for the open-source music attribution scaffold using Makefile commands -- clone and install with uv, start Docker Compose development stack with PostgreSQL and FastAPI, verify health endpoints, and run 658 tests across backend pytest and frontend Vitest suites, demonstrating a five-minute path to a running local environment.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Workflow diagram: four-step quickstart for the open-source music attribution scaffold using Makefile commands -- clone and install with uv, start Docker Compose development stack with PostgreSQL and FastAPI, verify health endpoints, and run 658 tests across backend pytest and frontend Vitest suites, demonstrating a five-minute path to a running local environment.](docs/figures/repo-figures/assets/fig-repo-05-quickstart-flow.jpg)

*Figure 5. The quickstart flow reduces onboarding to four commands: install dependencies via uv, launch the six-service Docker Compose stack, verify backend and frontend health endpoints, and run the full test suite -- requiring only git, Docker, and uv as prerequisites.*

### From this figure plan (relative)

![Workflow diagram: four-step quickstart for the open-source music attribution scaffold using Makefile commands -- clone and install with uv, start Docker Compose development stack with PostgreSQL and FastAPI, verify health endpoints, and run 658 tests across backend pytest and frontend Vitest suites, demonstrating a five-minute path to a running local environment.](../assets/fig-repo-05-quickstart-flow.jpg)
