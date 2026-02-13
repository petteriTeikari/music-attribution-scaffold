# fig-repo-08: CI/CD Pipeline

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-repo-08 |
| **Title** | GitHub Actions CI Pipeline: Five Jobs, Path-Based Filtering |
| **Audience** | Technical (contributors, maintainers) |
| **Complexity** | L2 (workflow) |
| **Location** | CONTRIBUTING.md, docs/architecture/ci.md |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

The CI pipeline runs on every push and PR to main/dev. This figure shows the five jobs, their dependency chain, and the path-based filtering that skips irrelevant jobs. It helps contributors understand what CI will run on their PR and how long to expect.

The key message is: "Five CI jobs with intelligent path filtering -- backend changes trigger backend jobs, frontend changes trigger frontend jobs. No wasted compute."

## Visual Concept (ASCII Layout)

```
+-----------------------------------------------------------------------+
|  CI PIPELINE                                                           |
|  ■ GitHub Actions: Five Jobs, Smart Path Filtering                     |
+-----------------------------------------------------------------------+
|                                                                        |
|  push/PR to main or dev                                                |
|         │                                                              |
|         ▼                                                              |
|  ┌──────────────┐                                                      |
|  │   CHANGES    │  dorny/paths-filter                                  |
|  │   DETECT     │  outputs: backend, frontend                          |
|  └──────┬───────┘                                                      |
|         │                                                              |
|    ┌────┴─────────────────────┐                                        |
|    │                          │                                        |
|    ▼ backend=true             ▼ frontend=true                          |
|                                                                        |
|  I. TEST                    IV. FRONTEND-TEST                          |
|  ┌──────────────┐           ┌──────────────┐                           |
|  │ ruff check   │           │ ESLint       │                           |
|  │ ruff format  │           │ tsc --noEmit │                           |
|  │ mypy         │           │ Vitest       │                           |
|  │ pytest unit  │           │ next build   │                           |
|  │ + Codecov    │           └──────┬───────┘                           |
|  └──────┬───────┘                  │                                   |
|         │                          ▼                                   |
|         ▼                    V. E2E-TEST                               |
|  II. INTEGRATION             ┌──────────────┐                          |
|  ┌──────────────┐            │ Playwright   │                          |
|  │ testcontainers│            │ chromium     │                          |
|  │ PostgreSQL   │            └──────────────┘                          |
|  │ pytest integ │                                                      |
|  └──────────────┘                                                      |
|                                                                        |
|  III. VALIDATE-GUARDRAILS                                              |
|  ┌──────────────┐                                                      |
|  │ Claude       │  (backend=true only)                                 |
|  │ constraints  │                                                      |
|  └──────────────┘                                                      |
|                                                                        |
+-----------------------------------------------------------------------+
|  Path filters: src/ tests/ pyproject.toml ──▶ backend                  |
|                frontend/ ──▶ frontend                                   |
+-----------------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title | `heading_display` | "CI PIPELINE" Instrument Serif ALL-CAPS |
| Trigger event | `event_trigger` | "push/PR to main or dev" entry point |
| Changes detect job | `job_box` | First job, path filter logic |
| Test job (I) | `job_box` | Backend lint + type check + unit tests |
| Integration job (II) | `job_box` | Testcontainers PostgreSQL integration tests |
| Validate-guardrails job (III) | `job_box` | Claude constraint validation |
| Frontend-test job (IV) | `job_box` | ESLint + TypeScript + Vitest + build |
| E2E-test job (V) | `job_box` | Playwright chromium tests |
| Dependency arrows | `primary_pathway` | Showing job ordering (test before integration, frontend before e2e) |
| Path filter footer | `footer_bar` | Which paths trigger which job group |
| Roman numerals I-V | `section_numeral` | Job identifiers |
| Backend/frontend branch split | `decision_branch` | Visual fork after changes-detect |

## Anti-Hallucination Rules

1. There are exactly FIVE jobs: changes (detect), test, integration-test, frontend-test, e2e-test, validate-guardrails. The "changes" job is a gate, not a test job.
2. Path filtering uses `dorny/paths-filter@v3` -- not a custom script.
3. Backend paths: src/, tests/, pyproject.toml, uv.lock, alembic/, scripts/, docker/, docker-compose*.yml, .github/workflows/ci.yml.
4. Frontend paths: frontend/, .github/workflows/ci.yml.
5. integration-test depends on test (runs after); e2e-test depends on frontend-test.
6. validate-guardrails runs in parallel with test (both need backend=true).
7. The CI uses `uv sync --frozen` (not `uv install` or `pip install`).
8. Coverage uploads to Codecov (not Coveralls or SonarCloud).
9. Python version in CI is 3.13, Node version comes from frontend/.nvmrc.
10. Concurrency is set with cancel-in-progress: true per workflow+ref.

## Alt Text

GitHub Actions CI pipeline: changes-detect job filters paths, then backend jobs (test, integration, guardrails) and frontend jobs (vitest, e2e) run conditionally based on changed files.
