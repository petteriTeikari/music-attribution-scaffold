# Remaining Final Tasks Before SSRN Repo Submission

## Original Prompt (verbatim)

> this got merged and deleted, so could you fetch the latest remote! delete extra local branch, and let's create a new branch to address any remaining Issues that should be address before this could be submitted as a companion repo to my preprint. So we are missing the installer scripts at least! And let's keep the final documentation task as the very last PR so that it reflects the final submission-ready state. Using mkdocs (or sphynx) with 100+ Gemini figures created as repo inforgraphics describing the repo as we did in our previous repo: /home/petteri/Dropbox/github-personal/foundation-PLR/foundation_PLR/docs/repo-figures/figure-plans /home/petteri/Dropbox/github-personal/foundation-PLR/foundation_PLR/docs/repo-figures/generated). So let's analyse what issues from our Project need closing, and are there so new Issues that need to be created? We can also create new P2 tasks to prepare the repo as well for new features what other companies are doing (without actually implementing then), e.g. https://auracles.io/, https://www.wearemusical.ai/, /home/petteri/Dropbox/github-personal/music-attribution-scaffold/docs/planning/music-tech-landscape/01-attribution-companies.md . Let's plan to /home/petteri/Dropbox/github-personal/music-attribution-scaffold/docs/planning/remaining-final-tasks-before-ssrn-repo.md with reviewer agents until convergence into an optimal report on the remaining tasks! start by saving my prompt verbatim, and then let's continue with the report generation

---

## Executive Summary

**Goal**: Make this repo submission-ready as a companion to SSRN No. 6109087.

**Current state**: 22 open GitHub issues, strong codebase (402 backend + 265 frontend tests, 6-job CI, Docker-native dev, agentic UI). PR #51 just merged (housekeeping: Playwright E2E, frontend CI, WCAG fixes).

**What's missing** (in execution order):
1. **Housekeeping PR** — pyproject.toml metadata, CITATION.cff, CONTRIBUTING.md, SECURITY.md, CHANGELOG.md, GitHub templates
2. **P2 Future-Readiness PR** — Schema stubs and PRD nodes for commercial landscape (Auracles, Musical AI, Sureel, etc.)
3. **Documentation PR** (LAST) — README expansion, reproducing-the-paper.md, API examples, troubleshooting, license audit, MkDocs + 100+ Gemini figures

**New GitHub issues to create**: 10 (detailed in Section 5)

---

## 1. Current State Assessment

### Strengths (already complete)
- **Installation**: `scripts/setup.sh` (213 lines, 7-step bootstrap) + `make setup`
- **CI/CD**: 6 GitHub Actions jobs (backend, integration, frontend, E2E, guardrails, compliance)
- **Test coverage**: 351 unit + 42 integration (backend), 265 Vitest + 7 E2E (frontend)
- **Docker-native**: `docker-compose.dev.yml` with PostgreSQL+pgvector, PgBouncer, Valkey
- **Agentic UI**: PydanticAI agent → AG-UI/SSE → CopilotKit sidebar
- **Design system**: Complete CSS token system, editorial typography, WCAG AA
- **PRD**: 31-node decision network, team archetypes, domain overlays

### Critical Gaps

| Gap | Impact | Status |
|-----|--------|--------|
| README.md (41 lines, has TODO) | First thing reviewers see | Planned (D0.1) |
| CONTRIBUTING.md | GitHub shows warning | Planned (PR-A, 3.3) |
| CHANGELOG.md | Academic reproducibility | Planned (PR-A, 3.5; closes #43) |
| SECURITY.md | GitHub security tab empty | Planned (PR-A, 3.4) |
| CITATION.cff | GitHub "Cite this repo" widget | Planned (PR-A, 3.2) |
| pyproject.toml metadata incomplete | PyPI discoverability | Planned (PR-A, 3.1) |
| License audit TODO in README | Looks unprofessional | Planned (PR-C, D5.1) |
| MkDocs + figures | User's explicit requirement | Planned (PR-C, Section 6) |
| .github/ISSUE_TEMPLATE/ | Contributor experience | Planned (PR-A, 3.6) |
| .github/PULL_REQUEST_TEMPLATE.md | PR quality | Planned (PR-A, 3.7) |

---

## 2. GitHub Issues Triage (22 open)

### Issues to CLOSE

*None — all 22 open issues represent genuine remaining work.*

### Issues to UPDATE (add labels/notes)

| # | Title | Action |
|---|-------|--------|
| #17 | tracking: 10 deferred backend tasks | Update checklist — several items completed in recent PRs |

### Issues to KEEP as-is (P1/P2 future work)

| # | Title | Priority | Label |
|---|-------|----------|-------|
| #5 | Frontend: Voice Agents | P2 | phase-6-future |
| #9 | Docker custom image with Apache AGE | P2 | infrastructure |
| #10 | Apache AGE graph store | P2 | phase-6-future |
| #11 | LightRAG integration | P2 | enhancement |
| #12 | EdgeQuake evaluation | P2 | research |
| #20 | Calibration loop — feedback to confidence update | P1 | phase-5-chat |
| #21 | Voice/likeness protection (ELVIS Act) | P2 | phase-6-future |
| #22 | Platform power & discovery friction metrics | P2 | phase-6-future |
| #23 | Attribution failure graceful degradation | P0 | phase-6-future |
| #24 | C2PA manifest generation | P1 | phase-6-future |
| #25 | DDEX ERN 4.3.2 connector | P2 | phase-6-future |
| #26 | ETL orchestration (ARQ/Prefect) | P1 | phase-6-future |
| #27 | Bayesian network signal integration | P2 | phase-6-future |
| #30 | Production AG-UI adapter (31 event types) | P1 | agentic-ui |
| #31 | LLM routing with PydanticAI FallbackModel | P2 | agentic-ui |
| #32 | Sentry error monitoring | P2 | enhancement |
| #36 | Pydantic Logfire observability | P2 | agentic-ui |
| #40 | Feedback list view | P2 | agentic-ui |
| #41 | OpenAPI/Swagger UI endpoint | P2 | developer-experience |
| #42 | examples/ directory with runnable scripts | P2 | developer-experience |
| #43 | CHANGELOG.md with release notes | P2 | chore |

---

## 3. Pre-Submission Housekeeping Tasks (PR-A: `chore/ssrn-housekeeping`)

### 3.1 Enhance pyproject.toml metadata

**File**: `pyproject.toml`

Add missing fields:
```toml
[project]
keywords = ["music", "attribution", "provenance", "AI", "MCP", "confidence-scoring", "conformal-prediction"]
classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.13",
    "Topic :: Scientific/Engineering :: Artificial Intelligence",
    "Topic :: Multimedia :: Sound/Audio :: Analysis",
    "Framework :: FastAPI",
    "Typing :: Typed",
]

[project.urls]
Homepage = "https://doi.org/10.2139/ssrn.6109087"
Repository = "https://github.com/petterik/music-attribution-scaffold"
Documentation = "https://github.com/petterik/music-attribution-scaffold#readme"
"Bug Tracker" = "https://github.com/petterik/music-attribution-scaffold/issues"
```

### 3.2 Create CITATION.cff

Machine-readable citation for GitHub's "Cite this repository" widget:
```yaml
cff-version: 1.2.0
title: "Music Attribution Scaffold"
message: "If you use this software, please cite the accompanying paper."
type: software
authors:
  - family-names: Teikari
    given-names: Petteri
    orcid: "https://orcid.org/..."
repository-code: "https://github.com/petterik/music-attribution-scaffold"
license: MIT
preferred-citation:
  type: article
  title: "Governing Generative Music: Attribution Limits, Platform Incentives, and the Future of Creator Income"
  authors:
    - family-names: Teikari
      given-names: Petteri
  doi: "10.2139/ssrn.6109087"
  year: 2026
  publisher: "Social Science Research Network"
```

### 3.3 Create CONTRIBUTING.md

Standard open-source contribution guide:
- Development setup (`make setup`)
- Code style (ruff, mypy, pre-commit hooks)
- Testing requirements (`make test-all` must pass)
- PR process (branch naming, description template)
- uv-only policy (no pip/conda)
- Academic context note (companion to SSRN paper)

### 3.4 Create SECURITY.md

Security policy:
- Scope: research scaffold, not production deployment
- How to report vulnerabilities (email)
- Supported versions
- Reference to `scripts/security/compliance_check.py`
- detect-secrets baseline maintenance

### 3.5 Create CHANGELOG.md (closes #43)

Keep-a-Changelog format, retroactive entries:
- **v0.1.0** — Initial scaffold (5 pipelines, seed data, API, MCP)
- **v0.2.0** — Frontend UI (editorial design system, 8 Imogen Heap works)
- **v0.3.0** — Agentic UI (PydanticAI agent, CopilotKit sidebar, AG-UI)
- **v0.4.0** — SSRN MVP gate (tinytag, display fields, CI)
- **v0.5.0** — Academic landing page, Docker-native dev
- **v0.6.0** — Housekeeping (Playwright E2E, frontend CI, WCAG fixes)

### 3.6 Create .github/ISSUE_TEMPLATE/

Three templates: `bug_report.md`, `feature_request.md`, `research_question.md`

### 3.7 Create .github/PULL_REQUEST_TEMPLATE.md

Checklist: tests pass, pre-commit clean, related issue linked, description provided.

---

## 4. P2 Future-Readiness Tasks (PR-B: `feat/commercial-landscape-stubs`) — Commercial Landscape Alignment

These tasks add **schema stubs, enums, and documentation** for capabilities that commercial players (Auracles, Musical AI, Sureel, ProRata, Vermillio) already offer. No business logic — just architectural preparation.

### 4.1 Training Data Attribution (TDA) Schema Stubs

**Companies**: Musical AI ("royalty sheets"), Sureel (attribution graphs), Sony (unlearning-based TDA)

**New files/changes**:
- `schemas/enums.py`: Add `AttributionMethodEnum` (TRAINING_TIME_INFLUENCE, UNLEARNING_BASED, INFLUENCE_FUNCTIONS, EMBEDDING_SIMILARITY, WATERMARK_DETECTION)
- `schemas/enums.py`: Add `RightsTypeEnum` (MASTER_RECORDING, COMPOSITION_PUBLISHING, PERFORMANCE, MECHANICAL, SYNC)
- `schemas/training_attribution.py` (stub): `TrainingInfluence`, `TemporalSegment`, `StemInfluence` models

### 4.2 Rights Management Extensions

**Companies**: SoundExchange AI Registry, STIM collective licensing, LANDR Fair Trade AI, Kits AI

**New files/changes**:
- `schemas/enums.py`: Extend `PermissionTypeEnum` with fine-grained AI training permissions (AI_TRAINING_COMPOSITION, AI_TRAINING_RECORDING, AI_TRAINING_STYLE, DATASET_INCLUSION)
- `schemas/enums.py`: Add `RevenueModelEnum` (FLAT_FEE_UPFRONT, PRO_RATA_MONTHLY, PER_GENERATION, INFLUENCE_BASED, REVENUE_SHARE_PERCENT)

### 4.3 Multi-Modal Attribution Domain Overlay

**Companies**: Sureel (audio+image+text+video), ProRata ($75M, cross-media)

**New files/changes**:
- `schemas/enums.py`: Add `MediaTypeEnum` (AUDIO, IMAGE, VIDEO, TEXT, SYMBOLIC_MUSIC, MULTIMODAL)
- `docs/prd/domains/multimodal-attribution.yaml`: Domain overlay stub extending music_attribution_v1

### 4.4 Certification & Compliance Schema

**Standards**: Fairly Trained, C2PA (v2.2), EU AI Act Article 50

**New files/changes**:
- `schemas/enums.py`: Add `CertificationTypeEnum` (FAIRLY_TRAINED_LICENSED, C2PA_PROVENANCE, EU_AI_ACT_COMPLIANT, CMO_APPROVED)
- `schemas/compliance.py` (stub): `ComplianceAttestation` model

### 4.5 AI Detection & Provenance Stubs

**Technology**: Google SynthID (10B+ pieces), Meta AudioSeal, Digimarc

**New files/changes**:
- `schemas/enums.py`: Add `WatermarkTypeEnum` (SYNTHID, AUDIOSEAL, WAVMARK, DIGIMARC)
- `schemas/enums.py`: Add `ProvenanceVerificationEnum` (WATERMARK_DETECTED, CRYPTOGRAPHIC_SIGNATURE, BLOCKCHAIN_TIMESTAMP, AI_DETECTION_POSITIVE)

### 4.6 MCP Tool Roadmap Documentation

**New files**:
- `docs/api/mcp-roadmap.md`: Document future MCP tools (query_training_influence, check_registry_status, verify_license, query_watermark)

### 4.7 PRD Decision Network Extensions

**New PRD nodes** (add to `docs/prd/decisions/_network.yaml`):
- `training_attribution_integration` (L3): none | partner_api | self_hosted
- `rights_management_scope` (L3): recording_only | full_bundle (composition + recording + performance)
- `provenance_verification` (L3): metadata_only | watermark_detection | cryptographic
- `external_registry_integration` (L3): none | soundexchange | stim | multi_registry

### 4.8 Music Tech Landscape Documentation Update

**File**: `docs/planning/music-tech-landscape/01-attribution-companies.md`

Update with latest intelligence:
- **Auracles.io**: Sovereign identity + MCP-like permissions (closest commercial analogue)
- **Musical AI**: Training-time influence tracking, royalty sheets (100+ publishers signed)
- **Sureel**: Patent-pending attribution graphs, compositional vs. recording rights separation
- **ProRata**: $75M Series B, cross-media TDA, ProSearch inference engine
- **Vermillio**: Sony-backed, content protection + rights management platform
- **SoundExchange AI Registry**: ISRC-based global opt-out database (Q1 2025 launch)
- **Fairly Trained**: Certification standard (Licensed/L+ tiers)

---

## 5. New GitHub Issues to Create

### P0 (must have for submission)

| # | Title | Labels |
|---|-------|--------|
| NEW-1 | chore: pyproject.toml metadata (classifiers, keywords, URLs) | chore, P0 |
| NEW-2 | chore: CITATION.cff for GitHub citation widget | chore, documentation, P0 |
| NEW-3 | chore: CONTRIBUTING.md | documentation, P0 |
| NEW-4 | chore: SECURITY.md | documentation, P0 |
| NEW-5 | chore: .github/ templates (issue + PR) | chore, developer-experience, P0 |
| NEW-6 | docs: MkDocs site with 100+ Gemini-generated repo figures | documentation, P1 |

### P2 (future-readiness stubs)

| # | Title | Labels |
|---|-------|--------|
| NEW-7 | feat: TDA schema stubs (TrainingInfluence, RightsTypeEnum) | enhancement, P2, phase-6-future |
| NEW-8 | feat: rights management extensions (fine-grained permissions, RevenueModelEnum) | enhancement, P2 |
| NEW-9 | feat: AI detection & provenance schema stubs (WatermarkTypeEnum) | enhancement, P2, phase-6-future |
| NEW-10 | feat: PRD nodes for commercial landscape (training attribution, registry integration) | enhancement, P2 |

---

## 6. Documentation Strategy — MkDocs + Gemini Figures (LAST PR)

### Replicating the foundation-PLR Pattern

The `foundation-PLR` project has a mature documentation system:
- **MkDocs + Material theme** with dark/light mode toggle, strict mode, pymdownx extensions
- **166 figure plans** in structured markdown (CONTENT-TEMPLATE.md v2.3)
- **30 generated PNGs** via Nano Banana Pro (Gemini image generation)
- **STYLE-GUIDE.md v2.0**: Economist off-white (#FBF9F3), anti-sci-fi mandate, semantic color tags
- **Two-phase workflow**: Claude Code writes figure plans → Gemini + Nano Banana Pro generates images

### Adaptation for Music Attribution Scaffold

**Target**: 100+ figure plans, 30-50 initially generated

**Proposed figure categories** (following foundation-PLR prefix system):

| Prefix | Category | Est. Count | Examples |
|--------|----------|------------|---------|
| `fig-arch-` | Architecture & pipelines | 15 | 5-pipeline flow, boundary objects, event sourcing |
| `fig-schema-` | Schema & data models | 12 | AttributionRecord anatomy, enum taxonomy, conformal set |
| `fig-prd-` | PRD decision network | 10 | Decision tree visualization, archetype profiles |
| `fig-ui-` | Frontend design system | 15 | Color token map, component hierarchy, editorial typography |
| `fig-agent-` | Agentic UI stack | 10 | AG-UI protocol flow, CopilotKit architecture, tool dispatch |
| `fig-conf-` | Confidence & calibration | 12 | Conformal prediction, source agreement, A0-A3 levels |
| `fig-perm-` | Permissions & MCP | 10 | Permission matrix, MCP query flow, delegation chain |
| `fig-etl-` | ETL & data sources | 8 | Source integration, NormalizedRecord flow, entity resolution |
| `fig-landscape-` | Commercial landscape | 8 | Competitor positioning, feature comparison matrix |
| `fig-deploy-` | Deployment & CI | 5 | Docker compose topology, CI pipeline, test pyramid |
| **Total** | | **~105** | |

### MkDocs Configuration

```yaml
site_name: Music Attribution Scaffold
site_description: "Open-source research scaffold for music attribution with transparent confidence scoring"
site_url: https://petterik.github.io/music-attribution-scaffold
repo_url: https://github.com/petterik/music-attribution-scaffold

theme:
  name: material
  palette:
    - scheme: default  # Light mode primary (editorial warm)
    - scheme: slate    # Dark mode
  features:
    - navigation.tabs
    - navigation.sections
    - content.code.copy
    - search.suggest

nav:
  - Home: index.md
  - Getting Started:
    - Quick Start: getting-started/quickstart.md
    - Prerequisites: getting-started/prerequisites.md
    - Troubleshooting: troubleshooting.md
  - Architecture:
    - Overview: architecture/overview.md
    - Pipelines: architecture/pipelines.md
    - Schemas: architecture/schemas.md
    - ADRs: architecture/adrs.md
  - Reproducing the Paper: reproducing-the-paper.md
  - API Reference:
    - REST API: api/rest-api.md
    - MCP Server: api/mcp-server.md
    - Examples: api/examples.md
  - Frontend:
    - Design System: frontend/design-system.md
    - Components: frontend/components.md
    - Agentic UI: frontend/agentic-ui.md
  - PRD:
    - Decision Network: prd/decision-network.md
    - Archetypes: prd/archetypes.md
    - Domains: prd/domains.md
  - Research:
    - Knowledge Base: research/knowledge-base.md
    - Music Tech Landscape: research/landscape.md

plugins:
  - search
  - git-revision-date-localized
  - mkdocstrings:
      handlers:
        python:
          options:
            docstring_style: numpy

markdown_extensions:
  - pymdownx.highlight
  - pymdownx.superfences:
      custom_fences:
        - name: mermaid
          class: mermaid
          format: !!python/name:pymdownx.superfences.fence_code_format
  - pymdownx.tabbed
  - admonition
  - pymdownx.details
  - attr_list
  - md_in_html
```

### Figure Plan Template (adapted from foundation-PLR)

Each figure plan follows CONTENT-TEMPLATE.md v2.3:
```markdown
# fig-{category}-{NN}: {Title}

## Metadata
- **ID**: fig-{category}-{NN}
- **Complexity**: L1-L4
- **Target Persona**: PhD student / developer / artist
- **Priority**: P1-P4

## Purpose
1-2 sentences: WHY this figure exists

## Key Message
Single sentence takeaway

## Visual Concept
ASCII mockup + flow description

## Spatial Anchors
Normalized coordinates (0.0-1.0) for element placement

## Content Elements
Tables of structures, relationships, callout boxes

## Prompts for Nano Banana Pro
- Style Prompt (aesthetic keywords)
- Content Prompt (what to show)

## Alt Text
Accessibility description (125 chars max)
```

### STYLE-GUIDE.md Adaptations (from foundation-PLR)

- **Background**: #FBF9F3 (Economist off-white) — same as foundation-PLR
- **Accent**: #E84C4F (coral red) — project-specific
- **Domain tags**: `confidence_high`, `confidence_medium`, `confidence_low`, `assurance_a3`, `permission_allow`, `permission_deny`
- **Anti-SCI-FI mandate**: No glowing, neon, holographic, cyberpunk (same as foundation-PLR)
- **Aspect ratio**: 16:9 landscape for GitHub embedding
- **Resolution**: 300 DPI export

---

## 7. Proposed PR Sequence

```
PR-A: chore/ssrn-housekeeping (low complexity)
  ├── pyproject.toml metadata (classifiers, keywords, URLs)
  ├── CITATION.cff
  ├── CONTRIBUTING.md
  ├── SECURITY.md
  ├── CHANGELOG.md (closes #43)
  ├── .github/ISSUE_TEMPLATE/{bug,feature,research}.md
  └── .github/PULL_REQUEST_TEMPLATE.md

PR-B: feat/commercial-landscape-stubs (medium complexity)
  ├── schemas/enums.py extensions (6 new enums)
  ├── schemas/training_attribution.py (stub)
  ├── schemas/compliance.py (stub)
  ├── docs/prd/decisions/_network.yaml (4 new nodes)
  ├── docs/prd/domains/multimodal-attribution.yaml
  ├── docs/api/mcp-roadmap.md
  ├── docs/planning/music-tech-landscape/ updates
  └── Unit tests for new enum values

PR-C: docs/ssrn-release (LAST PR — high complexity)
  ├── README.md expansion (~250 lines, spec in D0.1)
  ├── docs/reproducing-the-paper.md (spec in D1.1)
  ├── docs/api-examples.md (spec in D2.1)
  ├── docs/troubleshooting.md (spec in D4.1)
  ├── .env.example inline comments (spec in D3.1)
  ├── frontend/README.md (spec in D6.1)
  ├── License audit — remove README TODO (spec in D5.1)
  ├── mkdocs.yml configuration
  ├── docs/repo-figures/STYLE-GUIDE.md
  ├── docs/repo-figures/CONTENT-TEMPLATE.md
  ├── docs/repo-figures/figure-plans/ (100+ plans)
  ├── docs/repo-figures/generated/ (initial batch via Gemini)
  └── .github/workflows/deploy-docs.yml

Note: PR-A and PR-B are independent (can be parallelized).
PR-C must be last (documentation reflects final state).
Task specs D0.1–D6.1 from documentation-tasks-for-ssrn-repo.xml.
```

---

## 8. Effort Estimates

| PR | Tasks | Complexity | Notes |
|----|-------|------------|-------|
| PR-A Housekeeping | 7 | Low | Mostly templated files |
| PR-B Commercial stubs | 8 | Medium | Schema design, PRD nodes, unit tests |
| PR-C Documentation | 12+ | High | README, figure plans, MkDocs setup, Gemini generation |

**Critical path**: PR-C must be last (documentation reflects final state).
PR-A and PR-B are independent and can be parallelized.

---

*Generated: 2026-02-13 by multi-agent research synthesis (4 parallel research agents → convergence review)*
