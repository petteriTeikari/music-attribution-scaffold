# fig-howto-06: How to Run Tests (Which Tests, When)

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-howto-06 |
| **Title** | How to Run Tests (Which Tests, When) |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 (implementation detail) |
| **Location** | docs/contributing.md, docs/guides/testing.md |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure is a decision tree that helps engineers choose the right test suite based on what they changed. Instead of always running every test, developers can follow the tree to run only what matters. It answers: "I just changed some code -- which tests do I need to run before committing?"

The key message is: "Follow the decision tree: Python backend changes need pytest (unit or integration depending on scope), frontend changes need Vitest, and all changes must pass pre-commit hooks before any commit."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  HOW TO RUN TESTS                                              |
|  ■ Which Tests, When                                           |
+---------------------------------------------------------------+
|                                                                |
|                    I. WHAT DID YOU CHANGE?                      |
|                    ──────────────────────                       |
|                           ┌───┐                                |
|                           │ ? │                                |
|                           └─┬─┘                                |
|              ┌──────────────┼──────────────┐                  |
|              v              v              v                    |
|  II. PYTHON CODE?    III. FRONTEND?   IV. CONFIG/DOCS?        |
|  ────────────────    ──────────────   ────────────────        |
|     ┌───┐               ┌───┐            ┌───┐               |
|     │ ? │               │ ? │            │ ? │               |
|     └─┬─┘               └─┬─┘            └─┬─┘               |
|    ┌──┴──┐            ┌──┴──┐          ┌──┴──┐              |
|    v     v            v     v          v     v               |
|                                                                |
|  Logic  DB/API    Components  E2E    pyproject  .pre-commit   |
|  only?  models?   only?      flows?  .toml?     config?       |
|    │      │          │        │        │          │            |
|    v      v          v        v        v          v            |
|                                                                |
|  ┌─────┐ ┌─────┐  ┌─────┐ ┌─────┐ ┌─────┐  ┌─────┐        |
|  │make │ │make │  │make │ │make │ │make │  │pre-  │        |
|  │test │ │test │  │test-│ │test-│ │test │  │commit│        |
|  │-local│ │     │  │front│ │front│ │     │  │run   │        |
|  │-k   │ │(int.)│  │end  │ │end  │ │     │  │--all │        |
|  │unit │ │     │  │     │ │--e2e│ │     │  │      │        |
|  └─────┘ └─────┘  └─────┘ └─────┘ └─────┘  └─────┘        |
|                                                                |
|  V. ALWAYS BEFORE COMMIT                                       |
|  ───────────────────────                                       |
|  ┌─────────────────────────────────────────────┐              |
|  │ pre-commit run --all-files                   │              |
|  │ (ruff check + ruff format + mypy + secrets)  │              |
|  └─────────────────────────────────────────────┘              |
|                                                                |
+---------------------------------------------------------------+
|  ■ CI runs all four checks — match locally before pushing      |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "HOW TO RUN TESTS" in Instrument Serif ALL-CAPS with coral accent square |
| Subtitle | `label_editorial` | "Which Tests, When" in Plus Jakarta Sans caps |
| Root decision node (I) | `decision_point` | "WHAT DID YOU CHANGE?" diamond/question node |
| Branch II: Python code | `decision_point` | Sub-decision: logic-only vs. DB/API models |
| Branch III: Frontend | `decision_point` | Sub-decision: components-only vs. E2E flows |
| Branch IV: Config/Docs | `decision_point` | Sub-decision: pyproject.toml vs. pre-commit config |
| Leaf: make test-local -k unit | `processing_stage` | Unit tests for pure logic changes |
| Leaf: make test (integration) | `processing_stage` | Integration tests for DB/API model changes |
| Leaf: make test-frontend | `processing_stage` | Vitest for component changes |
| Leaf: make test-frontend --e2e | `processing_stage` | Playwright E2E for flow changes |
| Leaf: make test (full) | `processing_stage` | Full test suite for config changes |
| Leaf: pre-commit run --all | `processing_stage` | Pre-commit hooks for config file changes |
| Step V: Always before commit | `callout_box` | Pre-commit command that must always run |
| Decision arrows | `data_flow` | Branching paths from each decision node |
| Roman numerals I-V | `section_numeral` | Step and branch headers |
| Footer callout | `callout_box` | "CI runs all four checks" reminder |

## Anti-Hallucination Rules

1. Pre-commit hooks run: ruff check, ruff format --check, mypy, detect-secrets -- not just ruff.
2. CI runs four checks: ruff check, ruff format --check, mypy, pytest -- all must pass locally.
3. Frontend tests use Vitest (not Jest) with React Testing Library.
4. E2E tests use Playwright with @axe-core/playwright for accessibility.
5. `make test` runs in Docker for CI parity; `make test-local` runs directly in .venv.
6. The test suite has 351 unit tests + 42 integration tests for backend, 265 Vitest tests for frontend -- but do NOT show exact counts (they change).
7. Do NOT show `pytest` as the user-facing command -- use `make test` variants.
8. Background must be warm cream (#f6f3e6), not white or gray.

## Alt Text

Decision tree diagram: starting from what code changed, branches to Python, frontend, or config paths, each leading to specific test commands.
