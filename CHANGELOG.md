# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- SSRN housekeeping: pyproject.toml metadata, CITATION.cff, CONTRIBUTING.md, SECURITY.md
- GitHub issue templates and PR template
- This CHANGELOG

## [0.6.0] - 2026-02-13

### Added
- Playwright E2E smoke tests for landing page (7 tests) and works page (6 tests)
- Frontend-test CI job (lint, typecheck, vitest, build)
- E2E test CI job (Playwright + chromium)
- CSS token lint rule preventing undefined `--color-text` references
- Makefile targets: `test-e2e`, `test-e2e-ui`
- `.nvmrc` pinning Node 22

### Fixed
- WCAG AA color contrast for `--color-muted` and `--color-confidence-medium`
- 11 undefined CSS variable references (`--color-text` → `--color-heading`)
- Error handling for async page components (works, work detail, permissions)
- 2 failing landing-hero tests (author name + DOI link updated)

## [0.5.0] - 2026-02-12

### Added
- Academic landing page with citations, figures, and A0-A3 assurance framework
- Docker-native development with real PostgreSQL (docker-compose.dev.yml)
- PgBouncer connection pooler and Valkey cache in dev stack

### Fixed
- 387 Tailwind v4 `[var(--*)]` anti-patterns replaced with native utilities
- Configuration source-of-truth consolidation, fallback removal, DRY code

## [0.4.0] - 2026-02-12

### Added
- CI integration test job
- detect-secrets baseline and pre-commit hook

### Changed
- mutagen → tinytag for audio metadata (MIT license compatibility)

### Fixed
- Display fields persist through database round-trip
- CLAUDE.md private section removed

## [0.3.0] - 2026-02-11

### Added
- Agentic UI with CopilotKit sidebar + AG-UI streaming protocol
- PydanticAI agent with 4 tools (query attribution, check permission, list permissions, search)
- Adaptive UX: proficiency model, adaptive tooltips, feature flags
- PostHog analytics integration
- Uncertainty-aware provenance timeline with Perplexity-like citation UI
- Mock data wiring: apiClient, agent tools, feedback system

## [0.2.0] - 2026-02-11

### Added
- Next.js 15 frontend with editorial design system
- Instrument Serif + Plus Jakarta Sans + IBM Plex Mono typography
- CSS custom property token system (zero hardcoded hex)
- Fixed left sidebar navigation with rotated text
- PostgreSQL backend with pgvector hybrid search
- Full REST API (FastAPI): attributions, permissions, health
- MCP server with 3 tools

## [0.1.0] - 2026-02-10

### Added
- Initial project scaffold with 5-pipeline architecture
- Probabilistic PRD framework (27 decision nodes across 5 levels)
- Pydantic boundary objects: NormalizedRecord, ResolvedEntity, AttributionRecord
- ETL pipeline with MusicBrainz, Discogs, AcoustID connectors
- Entity resolution with Splink
- Attribution engine with conformal prediction
- In-memory implementations for dev/test
- 351 unit tests + 42 integration tests
- Pre-commit hooks (ruff, mypy, detect-secrets)
- Docker test container for CI

[Unreleased]: https://github.com/petteriTeikari/music-attribution-scaffold/compare/v0.6.0...HEAD
[0.6.0]: https://github.com/petteriTeikari/music-attribution-scaffold/compare/v0.5.0...v0.6.0
[0.5.0]: https://github.com/petteriTeikari/music-attribution-scaffold/compare/v0.4.0...v0.5.0
[0.4.0]: https://github.com/petteriTeikari/music-attribution-scaffold/compare/v0.3.0...v0.4.0
[0.3.0]: https://github.com/petteriTeikari/music-attribution-scaffold/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/petteriTeikari/music-attribution-scaffold/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/petteriTeikari/music-attribution-scaffold/releases/tag/v0.1.0
