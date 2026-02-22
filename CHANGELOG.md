# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.0] - 2026-02-22

### Added
- `.zenodo.json` metadata for Zenodo academic deposit
- `.gitattributes` with `export-ignore` rules for clean archive builds
- `make zenodo-archive` target to build reproducible release archives
- Zenodo DOI badge placeholder in README

### Changed
- Version bump to 1.0.0 across `pyproject.toml`, `__init__.py`, and `frontend/package.json`
- Development status classifier upgraded from Alpha to Beta
- `CITATION.cff` updated with version and date-released fields

## [0.9.0] - 2026-02-20

### Added
- Open-source voice agent MVP built on Pipecat (BSD-2-Clause) with 5-stage pipeline: Transport → STT → LLM → TTS → output (#196)
- 5-dimension persona architecture with EWMA-smoothed drift detection
- 78 architecture figures for voice agent documentation
- Protocol-based component swapping (`STTServiceProtocol`, `TTSServiceProtocol`, `DriftDetectorProtocol`)
- Zero-API-key local dev stack (Whisper + Piper + WebSocket)
- Persona coherence tests and drift monitoring
- Voice agent tutorial and component alternatives documentation
- Tiered dependency license audit with GPL isolation strategy (#197)

## [0.8.0] - 2026-02-17

### Added
- MkDocs documentation site with 200+ figures, API reference, concept pages, and tutorials (#71, #122)
- 116+ Nano Banana Pro figure plans covering all 5 pipelines (#71)
- PRD v3.0.0 with regulatory compliance nodes and team archetype profiles (#70, #71)
- Managerial roadmap: 18-month plan, 25 GitHub issues, 30 pitch-deck figures (#149)
- Preprint submission polish: README hero section, QA fixes (#121)
- UI polish for preprint: permissions page, progressive disclosure (#119)
- Path-based CI filtering to skip irrelevant jobs (#69)
- `create-pr` Claude skill for complete PR metadata (#68)

### Fixed
- Dollar signs rendering as LaTeX math in MkDocs (#150)
- Removed stale auracles-sprint figures from repo (#123)
- Mermaid diagram contrast fixes for dark backgrounds (#122)

## [0.7.0] - 2026-02-14

### Added
- SSRN housekeeping: pyproject.toml metadata, CITATION.cff, CONTRIBUTING.md, SECURITY.md (#52)
- GitHub issue templates and PR template (#52)
- This CHANGELOG (#52)
- Commercial landscape stubs: enums, schemas, PRD decision nodes (#53)
- xOps Tier 1: pipeline DAG runner, production Dockerfile, Prometheus metrics, Grafana dashboard (#54)
- PRD v1.9.0 with deployment and observability nodes (#54)

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

[Unreleased]: https://github.com/petteriTeikari/music-attribution-scaffold/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/petteriTeikari/music-attribution-scaffold/compare/v0.9.0...v1.0.0
[0.9.0]: https://github.com/petteriTeikari/music-attribution-scaffold/compare/v0.8.0...v0.9.0
[0.8.0]: https://github.com/petteriTeikari/music-attribution-scaffold/compare/v0.7.0...v0.8.0
[0.7.0]: https://github.com/petteriTeikari/music-attribution-scaffold/compare/v0.6.0...v0.7.0
[0.6.0]: https://github.com/petteriTeikari/music-attribution-scaffold/compare/v0.5.0...v0.6.0
[0.5.0]: https://github.com/petteriTeikari/music-attribution-scaffold/compare/v0.4.0...v0.5.0
[0.4.0]: https://github.com/petteriTeikari/music-attribution-scaffold/compare/v0.3.0...v0.4.0
[0.3.0]: https://github.com/petteriTeikari/music-attribution-scaffold/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/petteriTeikari/music-attribution-scaffold/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/petteriTeikari/music-attribution-scaffold/releases/tag/v0.1.0
