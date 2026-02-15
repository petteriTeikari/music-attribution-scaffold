# fig-repo-10: Testing Pyramid

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-repo-10 |
| **Title** | Testing Pyramid: 658 Tests Across Three Layers |
| **Audience** | Technical (contributors, reviewers) |
| **Complexity** | L2 (quality assurance) |
| **Location** | README.md, CONTRIBUTING.md, docs/architecture/testing.md |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

The testing strategy follows a classic pyramid with unit tests at the base, integration tests in the middle, and E2E/frontend tests at the top. This figure shows the exact counts, execution environments, and what each layer validates. It demonstrates the project's commitment to quality and helps contributors understand where to add their tests.

The key message is: "658 total tests -- 351 backend unit, 42 integration (real PostgreSQL via testcontainers), 265 frontend Vitest -- forming a robust pyramid that catches bugs at every level."

## Visual Concept (ASCII Layout)

```
+-----------------------------------------------------------------------+
|  TESTING PYRAMID                                                       |
|  ■ 658 Tests Across Three Layers                                       |
+-----------------------------------------------------------------------+
|                                                                        |
|                         /\                                             |
|                        /  \          E2E                               |
|                       / PW \         Playwright (chromium)              |
|                      /──────\        Browser-level WCAG + flows        |
|                     /        \                                         |
|                    /  265     \       FRONTEND                          |
|                   /  Vitest   \      React Testing Library              |
|                  /  + RTL      \     11 agent integration tests         |
|                 /  + vitest-axe \    Component-level WCAG               |
|                /────────────────\                                      |
|               /                  \                                     |
|              /   42 INTEGRATION   \  INTEGRATION                       |
|             /    testcontainers    \ Real PostgreSQL + pgvector         |
|            /     PostgreSQL 17     \ SQLAlchemy round-trips             |
|           /──────────────────────── \                                  |
|          /                           \                                 |
|         /     351 UNIT TESTS          \  UNIT                          |
|        /      pytest + mocks           \ Fast, isolated                |
|       /       schemas, pipelines,      \ All Pydantic models           |
|      /        attribution, API          \ All pipeline stages          |
|     /────────────────────────────────────\                             |
|                                                                        |
|  ────────────────────────────────────────────                          |
|  EXECUTION:                                                            |
|  ■ Unit:        make test (Docker) or make test-local                  |
|  ■ Integration: make test-integration (requires Docker daemon)         |
|  ■ Frontend:    make test-frontend (Vitest) + make test-e2e (PW)       |
+-----------------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title | `heading_display` | "TESTING PYRAMID" Instrument Serif ALL-CAPS |
| Pyramid shape | `pyramid_structure` | Triangle divided into three horizontal bands |
| Unit band (bottom) | `pyramid_base` | Widest, 351 tests, coral accent |
| Integration band (middle) | `pyramid_mid` | Medium width, 42 tests |
| Frontend band (upper) | `pyramid_upper` | 265 Vitest tests |
| E2E tip (top) | `pyramid_tip` | Narrowest, Playwright |
| Test counts | `data_mono` | IBM Plex Mono, prominent numbers (351, 42, 265) |
| Layer descriptions | `label_editorial` | What each layer validates, right-aligned |
| Execution commands | `data_mono` | Make targets for running each layer |
| Accent squares | `accent_square` | Coral squares as bullet markers |
| Total count callout | `callout_stat` | "658" as large display number |

## Anti-Hallucination Rules

1. Exact test counts: 351 unit tests, 42 integration tests, 265 frontend Vitest tests.
2. Total is 658 (351 + 42 + 265), plus Playwright E2E tests (count varies).
3. Integration tests use testcontainers with real PostgreSQL, NOT SQLite.
4. Frontend tests use Vitest (not Jest) with React Testing Library.
5. There are 11 agent integration tests within the 265 frontend tests.
6. Component-level WCAG testing uses vitest-axe, browser-level uses @axe-core/playwright.
7. There is 1 xfail test in the backend suite.
8. Unit tests run in Docker via `make test` or locally via `make test-local`.
9. Integration tests require Docker daemon for testcontainers (even when run "locally").
10. Do NOT include performance tests or load tests -- they do not exist yet.

## Alt Text

Quality assurance diagram: testing pyramid for the open-source music attribution scaffold with 658 total tests across four layers -- 351 pytest unit tests validating Pydantic schemas and confidence scoring at the base, 42 integration tests against real PostgreSQL via testcontainers, 265 Vitest frontend tests with WCAG accessibility checks, and Playwright E2E browser tests at the tip, ensuring robust music metadata quality.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Quality assurance diagram: testing pyramid for the open-source music attribution scaffold with 658 total tests across four layers -- 351 pytest unit tests validating Pydantic schemas and confidence scoring at the base, 42 integration tests against real PostgreSQL via testcontainers, 265 Vitest frontend tests with WCAG accessibility checks, and Playwright E2E browser tests at the tip, ensuring robust music metadata quality.](docs/figures/repo-figures/assets/fig-repo-10-testing-pyramid.jpg)

*Figure 10. The testing pyramid demonstrates the project's quality commitment: 351 unit tests cover all Pydantic models and pipeline stages, 42 integration tests validate against real PostgreSQL with pgvector via testcontainers, and 265 frontend tests include 11 agent integration tests and component-level WCAG checks via vitest-axe.*

### From this figure plan (relative)

![Quality assurance diagram: testing pyramid for the open-source music attribution scaffold with 658 total tests across four layers -- 351 pytest unit tests validating Pydantic schemas and confidence scoring at the base, 42 integration tests against real PostgreSQL via testcontainers, 265 Vitest frontend tests with WCAG accessibility checks, and Playwright E2E browser tests at the tip, ensuring robust music metadata quality.](../assets/fig-repo-10-testing-pyramid.jpg)
