# Detailed License Information

This project is licensed under [MIT](LICENSE). All dependencies are
MIT-compatible unless explicitly noted. This document provides a tiered
audit so users know exactly what they pull in at each `uv sync` group.

## TL;DR

| Install tier | Strictest license | MIT-compatible? |
|---|---|---|
| **Baseline** (`uv sync`) | Apache-2.0 / BSD-2-Clause | Yes |
| **Voice agent** (`uv sync --group voice`) | BSD-2-Clause / Apache-2.0 | Yes |
| **Voice persona** (`uv sync --group voice-persona`) | Apache-2.0 | Yes |
| **Voice GPL** (`uv sync --group voice-gpl`) | **GPL-3.0-or-later** | **No** — opt-in only |
| **Frontend** (`npm install`) | ISC | Yes |
| **Dev / Test** (not shipped) | LGPL-3.0 / Apache-2.0 | N/A (not distributed) |

---

## Python Core Dependencies (25 packages)

Installed by default with `uv sync`. All are permissive.

| Package | Version constraint | SPDX | Notes |
|---|---|---|---|
| alembic | — | MIT | DB migrations |
| asyncpg | — | Apache-2.0 | PostgreSQL driver |
| fastapi | — | MIT | Web framework |
| httpx | — | BSD-3-Clause | HTTP client |
| jellyfish | — | MIT | String similarity |
| loguru | — | MIT | Logging |
| mcp | — | MIT | Model Context Protocol SDK |
| musicbrainzngs | — | BSD-2-Clause | MusicBrainz API |
| tinytag | — | MIT | Audio metadata reader |
| pandera | — | MIT | DataFrame validation |
| pgvector | — | MIT | Vector extension for PostgreSQL |
| polars | — | MIT | DataFrame library |
| prometheus-client | — | Apache-2.0 | Metrics |
| pyacoustid | — | MIT | AcoustID fingerprinting |
| pydantic | — | MIT | Data validation |
| pydantic-ai-slim | — | MIT | LLM agent framework |
| pydantic-settings | — | MIT | Settings management |
| python3-discogs-client | — | BSD-2-Clause | Discogs API |
| sentence-transformers | — | Apache-2.0 | Embedding models |
| splink | — | MIT | Entity resolution |
| sqlalchemy | — | MIT | ORM |
| sse-starlette | — | BSD-3-Clause | Server-Sent Events |
| thefuzz | — | MIT | Fuzzy string matching |
| uvicorn | — | BSD-3-Clause | ASGI server |
| valkey | — | MIT | Cache client |

## Python Dev & Test Dependencies (11 packages)

Installed with `uv sync --group dev --group test`. These are **not shipped**
to end users and do not affect the license of distributed software.

| Package | SPDX | Notes |
|---|---|---|
| pre-commit | MIT | Git hook manager |
| ruff | MIT | Linter + formatter |
| mypy | MIT | Type checker |
| testcontainers | Apache-2.0 | Docker test containers |
| psycopg | LGPL-3.0 | PostgreSQL adapter (test-only) |
| aiosqlite | MIT | Async SQLite (test shims) |
| pillow | HPND (PIL License) | Image processing (test fixtures) |
| pytest | MIT | Test framework |
| pytest-cov | MIT | Coverage plugin |
| pytest-timeout | MIT | Timeout plugin |
| pytest-asyncio | MIT | Async test support |

> **Note on psycopg LGPL-3.0**: Used only in the test suite for integration
> tests against PostgreSQL. It is never bundled or distributed with the
> library. Production code uses `asyncpg` (Apache-2.0).

## Python Docs Dependencies (6 packages)

Build-time only, used for documentation generation. Not distributed.

| Package | SPDX | Notes |
|---|---|---|
| mkdocs | BSD-2-Clause | Documentation generator |
| mkdocs-material | MIT | Material theme |
| mkdocstrings | ISC | Auto-generate from docstrings |
| mkdocstrings-python | ISC | Python handler |
| mkdocs-mermaid2-plugin | MIT | Mermaid diagrams |
| pymdown-extensions | MIT | Markdown extensions |

## Python Voice — Optional (3 entries)

Installed with `uv sync --group voice`. Adds real-time voice agent
capabilities. All permissive.

| Package | SPDX | Notes |
|---|---|---|
| pipecat-ai | BSD-2-Clause | Real-time voice pipeline |
| pipecat-ai[smallwebrtc] | BSD-2-Clause | WebRTC transport |
| deepeval | Apache-2.0 | Voice agent evaluation |

## Python Voice Persona — Optional (3 packages)

Installed with `uv sync --group voice-persona`. Adds conversational memory
and guardrails for the voice agent persona. All Apache-2.0.

| Package | SPDX | Notes |
|---|---|---|
| letta | Apache-2.0 | Conversational memory |
| mem0ai | Apache-2.0 | Memory layer |
| nemoguardrails | Apache-2.0 | Safety guardrails |

## Python Voice GPL — Excluded by Default (1 entry)

Installed **only** with explicit `uv sync --group voice-gpl`. This group is
**not** included in any default install and must be opted into deliberately.

| Package | SPDX | Notes |
|---|---|---|
| pipecat-ai[piper] | **GPL-3.0-or-later** | Local TTS via Piper |

### Why is this isolated?

[Piper TTS](https://github.com/rhasspy/piper) is licensed under GPL-3.0.
When `pipecat-ai` is installed with the `[piper]` extra, it pulls in
GPL-licensed Piper binaries. To prevent unintentional GPL contamination:

1. Piper is in a **separate dependency group** (`voice-gpl`)
2. It is **never installed** by `uv sync`, `uv sync --group voice`, or CI
3. Users who want local TTS must explicitly opt in, understanding the
   GPL-3.0 implications for their distribution

If you distribute a binary that includes `pipecat-ai[piper]`, your
distribution must comply with GPL-3.0-or-later.

---

## JavaScript Frontend — Production (10 packages)

| Package | SPDX | Notes |
|---|---|---|
| @copilotkit/react-core | MIT | AG-UI agent framework |
| @copilotkit/react-ui | MIT | Agent UI components |
| animejs | MIT | Animation library |
| d3 | ISC | Data visualization |
| jotai | MIT | Atomic state management |
| motion | MIT | Animation (motion/react) |
| next | MIT | React framework |
| posthog-js | MIT | Product analytics |
| react | MIT | UI library |
| react-dom | MIT | React DOM renderer |

## JavaScript Frontend — Dev (21 packages)

Dev dependencies are **not shipped** in the production bundle. All MIT.

Includes: `@testing-library/react`, `@testing-library/jest-dom`,
`@testing-library/user-event`, `@playwright/test`, `vitest`, `vitest-axe`,
`tailwindcss`, `@tailwindcss/postcss`, `postcss`, `typescript`,
`@types/react`, `@types/react-dom`, `@types/d3`, `@types/animejs`,
`eslint`, `eslint-config-next`, `@eslint/eslintrc`, `jsdom`,
`@vitejs/plugin-react`, `@copilotkit/react-textarea`, `happy-dom`.

---

## GPL Transitive Dependencies

### igraph (GPL-2.0-or-later)

`igraph` is a transitive dependency of `splink` (entity resolution). It is:

- **Not imported** by any code in this repository
- **Not used at runtime** — splink's graph features are not exercised
- Present only because `splink` declares it as a dependency

This is a transitive, unused dependency. It does not affect the license of
this project because:

1. We do not distribute igraph binaries
2. We do not link against igraph at runtime
3. Users installing from source get igraph via pip/uv as a separate package

If this concerns your compliance team, you can verify with:

```bash
# Confirm igraph is never imported
uv run python -c "
import ast, pathlib
for p in pathlib.Path('src').rglob('*.py'):
    tree = ast.parse(p.read_text(encoding='utf-8'))
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                assert 'igraph' not in alias.name, f'{p}: imports igraph'
        elif isinstance(node, ast.ImportFrom) and node.module:
            assert 'igraph' not in node.module, f'{p}: imports from igraph'
print('Confirmed: igraph is never imported')
"
```

---

## Summary Statistics

| License family | Count | Distributed? |
|---|---|---|
| MIT | 42 | Yes (core + frontend) |
| Apache-2.0 | 9 | Yes (core) + optional (voice) |
| BSD-2-Clause | 4 | Yes (core) + optional (voice) |
| BSD-3-Clause | 3 | Yes (core) |
| ISC | 3 | Yes (frontend + docs) |
| HPND (PIL) | 1 | No (test only) |
| LGPL-3.0 | 1 | No (test only) |
| GPL-3.0-or-later | 1 | No (opt-in only) |
| GPL-2.0-or-later | 1 | No (transitive, unused) |

**Bottom line**: The default install (`uv sync` + `npm install`) pulls in
**zero** copyleft dependencies. GPL exposure exists only through explicit
opt-in (`voice-gpl` group) or as an unused transitive dependency (`igraph`).
