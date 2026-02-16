# Visual Documentation Gallery

> All 200 figures generated for the Music Attribution Scaffold documentation. Each figure provides a visual explanation of architecture decisions, implementation patterns, and design choices.
>
> Figures generated with [Nano Banana Pro](https://nanobananapro.com/) (Google Gemini image generation). Figure plans in [`docs/figures/repo-figures/figure-plans/`](https://github.com/petteriTeikari/music-attribution-scaffold/tree/main/docs/figures/repo-figures/figure-plans).

---

## Repository Overview

The repository overview figures provide the first orientation for newcomers -- covering the project hero, pipeline architecture, directory layout, technology stack, quickstart flow, developer tooling, quality gates, CI/CD, Docker infrastructure, testing, frontend/backend connection, and security considerations including MCP threat models and protocol landscape.

<details>
<summary><strong>31 figures</strong> -- click to expand</summary>

![Repository overview: split-panel infographic contrasting fragmented music metadata across siloed databases with an open-source attribution scaffold that unifies sources into a single record with 0.87 transparent confidence scoring, multi-source resolution, and A0-A3 assurance levels for music credits provenance](figures/fig-repo-01-hero-overview.jpg)

*What This Repo Does: from broken metadata to transparent attribution -- the hero overview contrasting fragmented music metadata with the unified attribution scaffold.*

---

![Architecture diagram: five-pipeline data flow for music attribution showing ETL ingestion from Discogs and MusicBrainz, entity resolution with fuzzy matching, transparent confidence scoring engine, FastAPI REST and MCP permission server, and PydanticAI chat interface with Pydantic boundary objects ensuring type-safe handoffs across the open-source attribution scaffold](figures/fig-repo-02-five-pipeline-architecture.jpg)

*Five-pipeline architecture: ETL, entity resolution, attribution engine, API/MCP server, and chat agent connected by Pydantic boundary objects.*

---

![Reference card: annotated directory tree of the open-source music attribution scaffold showing Python 3.13 backend in src/music_attribution with five pipeline modules, Next.js 15 frontend, 393 backend tests plus 265 frontend tests, Docker infrastructure, and pyproject.toml as the single source of truth for dependency management via uv](figures/fig-repo-03-directory-map.jpg)

*Annotated directory tree showing the project structure with five pipeline modules, frontend, tests, and infrastructure.*

---

![Reference card: full technology stack for the open-source music attribution scaffold listing Python 3.13 backend with FastAPI, SQLAlchemy, and PydanticAI for transparent confidence scoring, Next.js 15 frontend with Jotai and CopilotKit AG-UI, and shared infrastructure including Docker, GitHub Actions, PostgreSQL with pgvector, and uv package manager](figures/fig-repo-04-technology-stack.jpg)

*Full technology stack: Python 3.13 backend, Next.js 15 frontend, PostgreSQL with pgvector, and every dependency a deliberate PRD decision.*

---

![Workflow diagram: four-step quickstart for the open-source music attribution scaffold using Makefile commands -- clone and install with uv, start Docker Compose development stack with PostgreSQL and FastAPI, verify health endpoints, and run 658 tests across backend pytest and frontend Vitest suites](figures/fig-repo-05-quickstart-flow.jpg)

*Four-step quickstart: clone, install with uv, start Docker Compose, verify with 658 tests -- a five-minute path to running locally.*

---

![Reference card: Makefile developer command interface for the music attribution scaffold organized into eight categories across Docker CI-parity and local fast-iteration modes](figures/fig-repo-06-make-commands-map.jpg)

*Makefile command map: eight categories covering dependency management, testing, linting, frontend, and agent workflows.*

---

![Workflow diagram: seven pre-commit quality gates for the music attribution scaffold showing sequential hooks from whitespace trimming and YAML validation through uv lockfile sync, ruff linting, ruff formatting, mypy static type checking, and detect-secrets scanning](figures/fig-repo-07-precommit-quality-gates.jpg)

*Seven pre-commit quality gates: any hook failure blocks the commit, enforcing zero-exception code quality.*

---

![Workflow diagram: GitHub Actions CI pipeline for the music attribution scaffold with path-based filtering that conditionally triggers five jobs](figures/fig-repo-08-ci-cd-pipeline.jpg)

*GitHub Actions CI/CD pipeline with path-based filtering: backend lint, type check, pytest with Codecov, integration tests, frontend Vitest, and Playwright E2E.*

---

![Architecture diagram: Docker Compose six-service development stack for the music attribution scaffold showing PostgreSQL 17 with pgvector, PgBouncer, Valkey cache, FastAPI backend, Next.js 15 frontend, and Prometheus plus Grafana monitoring](figures/fig-repo-09-docker-architecture.jpg)

*Docker Compose six-service stack: PostgreSQL 17, PgBouncer, Valkey, FastAPI, Next.js, and optional Prometheus/Grafana monitoring.*

---

![Quality assurance diagram: testing pyramid for the open-source music attribution scaffold with 658 total tests across four layers](figures/fig-repo-10-testing-pyramid.jpg)

*Testing pyramid: 351 unit tests, 42 integration tests, 265 Vitest frontend tests, and Playwright E2E at the tip.*

---

![Architecture diagram: Next.js 15 App Router frontend for the music attribution scaffold showing four route pages, 19 component modules, and cross-cutting layers](figures/fig-repo-11-frontend-architecture.jpg)

*Frontend architecture: Next.js 15 App Router with four routes, 19 component modules, Jotai state, and CopilotKit agent integration.*

---

![Architecture diagram: two communication channels connecting the music attribution scaffold frontend and backend -- REST JSON and AG-UI Server-Sent Events](figures/fig-repo-12-backend-frontend-connection.jpg)

*Backend-frontend connection: REST JSON for CRUD operations and AG-UI SSE for real-time agent conversations.*

---

![Reference card: environment variable configuration map for the music attribution scaffold organized by service](figures/fig-repo-13-environment-variables.jpg)

*Environment variables: FastAPI backend, PostgreSQL, PgBouncer, and Next.js frontend following 12-factor app principles.*

---

![Architecture diagram: PostgreSQL 17 entity-relationship schema for the music attribution scaffold showing Works, Artists, Attribution Records with confidence scores, and Permissions tables](figures/fig-repo-14-database-schema.jpg)

*Database schema: Works with ISRC/ISWC, Artists with ISNI, Attribution Records with per-field confidence, and MCP Permissions.*

---

![Reference card: CLAUDE.md AI-assisted development configuration hierarchy for the music attribution scaffold](figures/fig-repo-15-claude-md-hierarchy.jpg)

*CLAUDE.md hierarchy: root behavior contract, five domain rules, TDD skill workflows, and file-pattern context loading triggers.*

---

![Music AI attribution landscape overview: four-quadrant infographic with PRD v3.0.0 node annotations mapping company nodes to attribution infrastructure, AI music generation, and licensing bodies](figures/fig-repo-16-landscape-overview.jpg)

*Landscape overview: four-quadrant map with PRD v3.0.0 company nodes, integration archetypes, and ecosystem positioning.*

---

![MCP security threat model: four attack surfaces mapped to four defense layers with benchmark showing 40.71% average attack success rate](figures/fig-repo-17-mcp-security-threat-model.jpg)

*MCP security threat model: tool manifest, communication, resource access, and execution attack surfaces against four defense layers.*

---

![EU AI Act compliance timeline for music attribution from August 2024 through August 2027 full enforcement](figures/fig-repo-18-eu-ai-act-timeline.jpg)

*EU AI Act timeline: entry into force through full enforcement, highlighting GPAI transparency obligations and A0-A3 compliance.*

---

![Agentic commerce ecosystem: three-tier protocol landscape showing MCP as foundation, four commerce protocols as transaction layer, and music attribution server feeding into the stack](figures/fig-repo-19-agentic-commerce-ecosystem.jpg)

*Agentic commerce ecosystem: MCP foundation, ACP/AP2/TAP/A2A transaction layer, and the music attribution MCP server.*

---

![MCP attack surface taxonomy showing six attack vectors with measured success rates](figures/fig-repo-20-mcp-attack-taxonomy.jpg)

*MCP attack taxonomy: tool poisoning at 72.8%, cross-server contamination at 85%+, supply chain compromise, prompt injection, rug pulls, and path traversal.*

---

![Conceptual scatter plot showing the inverse scaling paradox where attack success rate increases with model capability](figures/fig-repo-21-inverse-scaling-paradox.jpg)

*Inverse scaling paradox: more capable AI models are more vulnerable to MCP attacks due to stronger instruction-following.*

---

![MCP-Guard three-stage defense pipeline: static scanner, neural classifier at 96.01% accuracy, LLM arbiter at 89.07% F1](figures/fig-repo-22-mcp-guard-three-stage.jpg)

*MCP-Guard three-stage defense: static scanner under 2ms, neural classifier, and LLM arbiter achieving 12x speedup.*

---

![Horizontal bar chart showing MCP authentication distribution: 32% no auth, 53% static secrets, 8.5% OAuth, 4% mTLS](figures/fig-repo-23-mcp-auth-crisis.jpg)

*MCP authentication crisis: 85% of 500+ deployed servers are insecure -- 32% with no authentication, 53% with static secrets.*

---

![Agentic protocol landscape showing three convergent layers: XAA identity, A2A coordination, MCP tools, plus vertical niches ACP and TAP](figures/fig-repo-24-protocol-landscape.jpg)

*Protocol landscape: XAA identity from Okta, A2A coordination from Google, MCP tools from Anthropic, plus ACP and TAP verticals.*

---

![Timeline showing MCP protocol evolution from November 2024 through December 2025 AAIF Linux Foundation governance](figures/fig-repo-25-mcp-evolution-timeline.jpg)

*MCP evolution timeline: initial release through OAuth 2.1 mandate, streamable HTTP, registry preview, to AAIF governance.*

---

![Split-panel comparison of current trust-on-first-use MCP versus target zero-trust architecture with DIDs and Verifiable Credentials](figures/fig-repo-26-zero-trust-mcp.jpg)

*Zero-trust MCP: current TOFU model versus target architecture with Decentralized Identifiers and Agent Name Service.*

---

![Gallery of three real-world MCP CVEs from 2025: Figma SSRF, mcp-remote RCE, and Anthropic Git MCP command injection](figures/fig-repo-27-mcp-cve-gallery.jpg)

*MCP CVE gallery: Figma SSRF (CVSS 7.5), mcp-remote RCE (558K+ downloads), and Git MCP command injection.*

---

![Three-column comparison of MCP sandbox isolation: Cloudflare Workers, Docker containers, and Deno sandbox](figures/fig-repo-28-sandbox-isolation.jpg)

*Sandbox isolation patterns: V8 isolates, Docker containers, and Deno sandbox -- Docker recommended for the scaffold.*

---

![OWASP Agentic AI Top 10 checklist for MCP servers showing seven of ten risks addressed by the scaffold](figures/fig-repo-29-owasp-agentic-top10.jpg)

*OWASP Agentic AI Top 10: seven risks addressed by the scaffold defense architecture, three requiring additional investment.*

---

![Split-panel MCP production observability: data plane with logs, traces, and metrics feeding analysis plane with compliance dashboards](figures/fig-repo-30-mcp-observability.jpg)

*MCP observability: structured logs, OpenTelemetry traces, and security metrics feeding EU AI Act compliance dashboards.*

---

![AAIF governance structure: Linux Foundation umbrella, five platinum members, Technical Steering Committee, governing MCP and A2A](figures/fig-repo-31-aaif-governance.jpg)

*AAIF governance: Linux Foundation umbrella with AWS, Anthropic, Google, Microsoft, OpenAI as platinum members governing MCP and A2A.*

</details>

---

## Backend Pipelines

The backend pipeline figures trace the complete data flow from raw source extraction through entity resolution to confidence-scored attribution records. Covers the ETL pipeline, boundary object schemas, quality gates, rate limiting, string similarity, embedding matching, Splink linkage, attribution engine, conformal calibration, review queue, FastAPI routing, database ERD, and dependency injection.

<details>
<summary><strong>20 figures</strong> -- click to expand</summary>

![Pipeline diagram showing the open-source music attribution ETL pipeline where five music metadata sources converge through token bucket rate limiting and a three-check data quality gate into a unified NormalizedRecord boundary object](figures/fig-backend-01-etl-pipeline-overview.jpg)

*ETL pipeline: five sources -- MusicBrainz, Discogs, AcoustID, tinytag, Artist Input -- converge through rate limiting and quality gates into NormalizedRecord.*

---

![Data schema diagram of the NormalizedRecord Pydantic model with 12 top-level fields, nested IdentifierBundle with seven identifiers, SourceMetadata, and three validation rules](figures/fig-backend-02-normalized-record-schema.jpg)

*NormalizedRecord schema: 12 fields, IdentifierBundle with ISRC/ISWC/ISNI/IPI/MBID/Discogs ID/AcoustID, and three validation rules.*

---

![Pipeline diagram of the data quality gate showing three batch validation checks: identifier coverage, duplicate detection, and source distribution capping](figures/fig-backend-03-data-quality-gate.jpg)

*Data quality gate: identifier coverage at 50% threshold, duplicate detection, and source distribution capping at 95%.*

---

![Comparison diagram of five music metadata ETL extractors with their libraries, default confidence, and returned data fields](figures/fig-backend-04-source-specific-extraction.jpg)

*Source-specific extraction: MusicBrainz (0.90), Discogs (0.85), AcoustID (variable), tinytag (0.70), Artist Input (0.60).*

---

![Architecture diagram of the token bucket rate limiter with per-source API rate configurations and async locking](figures/fig-backend-05-rate-limiting-strategy.jpg)

*Rate limiting strategy: per-source token bucket with MusicBrainz at 1 req/s, Discogs at 1 req/s, AcoustID at 3 req/s.*

---

![Flow diagram of the multi-signal entity resolution pipeline with cascade from exact identifier matching through six weighted signals](figures/fig-backend-06-resolution-orchestrator-flow.jpg)

*Resolution orchestrator: exact identifiers, fuzzy strings, embeddings, graph evidence, LLM disambiguation, and Splink linkage producing ResolvedEntity.*

---

![Comparison diagram of Jaro-Winkler and token sort ratio string similarity algorithms with music-domain normalization](figures/fig-backend-07-string-similarity-methods.jpg)

*String similarity methods: Jaro-Winkler for typo detection and token sort ratio for word reordering at 0.85 match threshold.*

---

![Architecture diagram of semantic embedding entity resolution with all-MiniLM-L6-v2 vectors in pgvector HALFVEC columns](figures/fig-backend-08-pgvector-embedding-match.jpg)

*pgvector embedding match: 768-dimensional sentence-transformer vectors catching translations and alias variations that string matching misses.*

---

![Pipeline diagram of Splink probabilistic record linkage with Fellegi-Sunter EM algorithm and union-find clustering](figures/fig-backend-09-splink-probabilistic-linkage.jpg)

*Splink probabilistic linkage: Fellegi-Sunter match/non-match probabilities via EM, DuckDB backend, and 0.85 threshold clustering.*

---

![Data schema diagram of the ResolvedEntity Pydantic model with assurance levels A0-A3, source provenance, per-method confidence, and conflict detection](figures/fig-backend-10-resolved-entity-schema.jpg)

*ResolvedEntity schema: assurance levels A0-A3, source provenance references, per-method confidence breakdown, and conflict severity.*

---

![Pipeline diagram of the three-stage attribution engine: weighted aggregation, conformal calibration, and active learning review](figures/fig-backend-11-attribution-engine-flow.jpg)

*Attribution engine: weighted credit aggregation, conformal prediction calibration at 90% coverage, and active learning review prioritization.*

---

![Mathematical diagram of the weighted source aggregation formula with bar chart of five source reliability weights and worked example](figures/fig-backend-12-weighted-source-aggregation.jpg)

*Weighted source aggregation: MusicBrainz 0.95, Discogs 0.85, AcoustID 0.80, file 0.70, Artist Input 0.60 -- worked example computing 0.845.*

---

![Pipeline diagram of conformal prediction calibration with Adaptive Prediction Sets, reliability diagram, and ECE formula](figures/fig-backend-13-conformal-calibration-pipeline.jpg)

*Conformal calibration: APS method accumulating predictions until 90% coverage, with reliability diagram and Expected Calibration Error.*

---

![Data schema diagram of the AttributionRecord with per-credit confidence, conformal prediction sets, provenance chain, and review prioritization](figures/fig-backend-14-attribution-record-schema.jpg)

*AttributionRecord schema: per-credit confidence for 14 role types, conformal sets, six provenance event types, and A0-A3 assurance.*

---

![Architecture diagram of the active learning review priority queue with five-factor weighted formula](figures/fig-backend-15-review-priority-queue.jpg)

*Review priority queue: boundary proximity (30%), source disagreement (25%), conformal ambiguity (15%), never-reviewed (15%), staleness (15%).*

---

![Architecture diagram of the FastAPI route map with five router groups and CORS middleware](figures/fig-backend-16-fastapi-route-map.jpg)

*FastAPI route map: health, Prometheus metrics, attribution CRUD with hybrid search, MCP permissions, and CopilotKit AG-UI endpoint.*

---

![Entity-relationship diagram of the PostgreSQL database with 8 tables mapping five boundary objects to persistent storage](figures/fig-backend-17-database-erd.jpg)

*Database ERD: normalized_records, resolved_entities, attribution_records with JSONB, feedback_cards, permissions, graph edges, embeddings, and audit log.*

---

![Architecture diagram of hybrid search combining full-text, vector similarity, and graph context with Reciprocal Rank Fusion](figures/fig-backend-18-hybrid-search-architecture.jpg)

*Hybrid search: full-text LIKE, sentence-transformer pgvector embeddings, and 1-hop graph context fused with RRF (k=60).*

---

![Flow diagram of four sequential reversible Alembic migrations documenting PostgreSQL schema evolution](figures/fig-backend-19-alembic-migration-chain.jpg)

*Alembic migration chain: initial schema, permissions and pgvector, uncertainty metadata, and display fields -- all reversible.*

---

![Architecture diagram of FastAPI dependency injection with async PostgreSQL engine, request-scoped sessions, repository and service layers](figures/fig-backend-20-dependency-injection.jpg)

*Dependency injection: lifespan creates async engine on app.state, request-scoped sessions flow through repository and service layers.*

</details>

---

## Agentic UI

The agentic UI figures cover the complete end-to-end architecture of the AI-assisted chat interface, from CopilotKit frontend integration through AG-UI protocol to PydanticAI agent tools, model failover, conversation flow, voice agent upsell, and testing strategy.

![Architecture diagram: end-to-end agentic UI stack showing CopilotKit sidebar sending messages via AG-UI Server-Sent Events to a FastAPI backend where a PydanticAI agent queries music metadata with four domain tools](figures/fig-agent-01-full-stack.jpg)

*Full-stack agentic UI: CopilotKit sidebar to AG-UI SSE to PydanticAI agent with four tools and bidirectional DuetUI context.*

---

![Architecture diagram: PydanticAI agent configuration with system prompt, AgentDeps injection, four tools, and model routing](figures/fig-agent-02-pydantic-ai-architecture.jpg)

*PydanticAI agent architecture: domain-specific system prompt, AgentDeps for database access, four tools, and Claude Haiku default.*

---

![Sequence diagram: AG-UI protocol flow showing SSE lifecycle from POST request through six event types](figures/fig-agent-03-agui-protocol-flow.jpg)

*AG-UI protocol flow: RunStarted, TextMessageStart, chunked Content, TextMessageEnd, StateSnapshot, RunFinished via SSE.*

---

![Integration diagram: CopilotKit bidirectional context with provider, sidebar, useCopilotReadable hooks, and useCopilotAction hooks](figures/fig-agent-04-copilotkit-integration.jpg)

*CopilotKit integration: provider with graceful degradation, useCopilotReadable for context, and four useCopilotAction hooks.*

---

![Flow diagram: explain_confidence agent tool tracing execution from work ID through database lookup to natural language explanation](figures/fig-agent-05-tool-get-work.jpg)

*Tool: explain_confidence -- work ID to database lookup, source agreement extraction, confidence factors, and human-readable output.*

---

![Flow diagram: search_attributions agent tool showing hybrid text-and-vector search with result formatting](figures/fig-agent-06-tool-explain-confidence.jpg)

*Tool: search_attributions -- hybrid search across attribution records with confidence percentages and assurance levels per hit.*

---

![Configuration diagram: PydanticAI FallbackModel failover strategy with Claude Haiku default and automatic cascading](figures/fig-agent-07-model-failover.jpg)

*Model failover: environment variable configuration defaulting to Haiku, automatic cascading to more capable models on failure.*

---

![Conversation flow diagram: multi-turn agentic interaction chaining search and explain tools with live state updates](figures/fig-agent-08-conversation-flow.jpg)

*Conversation flow: user query chains search_attributions and explain_confidence with source agreement breakdown and live sidebar updates.*

---

![UI component mockup: voice agent Pro-tier upsell banner with coral microphone icon and upgrade call-to-action](figures/fig-agent-09-voice-agent-upsell.jpg)

*Voice agent upsell: subtle aspirational banner for Pro tier -- microphone icon, example query, "Upgrade to Pro" -- no actual voice processing.*

---

![Testing strategy diagram: 11 integration tests covering proficiency model, PostHog events, and feature flags with mock agent pattern](figures/fig-agent-10-testing-strategy.jpg)

*Testing strategy: deterministic tests around non-deterministic AI -- proficiency thresholds, event schema validation, and mock agent endpoint testing.*

---

## Frontend Design

The frontend design figures document the Next.js 15 application architecture, design token system, page routing, component patterns, state management, typography, color system, responsive layout, accessibility, analytics, and adaptive UI proficiency model.

<details>
<summary><strong>15 figures</strong> -- click to expand</summary>

![Architecture diagram showing the four-layer Next.js 15 frontend: App Router pages, 19 component modules, lib utilities, and three custom hooks](figures/fig-frontend-01-architecture-overview.jpg)

*Frontend architecture: four layers -- pages compose components, components consume lib, hooks wire to Jotai state and CopilotKit agent.*

---

![Design system diagram showing CSS custom property token architecture with 60+ color tokens flowing through Tailwind v4 utilities](figures/fig-frontend-02-design-token-architecture.jpg)

*Design token architecture: 60+ CSS custom properties in globals.css, Tailwind v4 utilities, zero hardcoded hex enforced by lint tests.*

---

![Component diagram mapping Next.js 15 App Router page tree with five page files from shared RootLayout](figures/fig-frontend-03-page-router-map.jpg)

*Page router map: five routes -- home, works catalog, work detail, review queue, and MCP permissions -- branching from shared layout.*

---

![UI component diagram of the ConfidenceGauge: 270-degree SVG arc with three tiers, three size variants, ARIA meter role, and mount animation](figures/fig-frontend-04-confidence-gauge.jpg)

*ConfidenceGauge: 270-degree SVG arc in green/amber/red tiers with ARIA meter role and motion-safe mount animation.*

---

![Design system diagram of A0-A3 assurance badge system with four color-coded levels from gray to green](figures/fig-frontend-05-assurance-badge-system.jpg)

*Assurance badges: A0 gray (no data), A1 amber (single source), A2 blue (multi-source), A3 green (artist verified).*

---

![Interface mockup of works catalog page with fixed sidebar, horizontal rows, confidence gauges, and assurance badges](figures/fig-frontend-06-works-list-layout.jpg)

*Works list layout: fixed sidebar navigation, horizontal rows with confidence gauges, assurance badges, and Jotai-driven search/sort.*

---

![Interface mockup of work detail page with hero confidence gauge, per-credit scores, provenance panel, and timeline](figures/fig-frontend-07-work-detail-layout.jpg)

*Work detail layout: hero confidence gauge, per-credit scores with source tags, Perplexity-style provenance, and chronological timeline.*

---

![UI wireframe of AI-assisted review queue with agent narration, progress bar, Roman numeral indexing, suggestion diffs, and batch approval](figures/fig-frontend-08-review-queue-workflow.jpg)

*Review queue workflow: agent narration header, progress tracking, suggestion diffs showing before/after, and batch approval.*

---

![Component diagram of Jotai state architecture with four store files managing theme, role, works, and proficiency model](figures/fig-frontend-09-jotai-state-architecture.jpg)

*Jotai state architecture: four atom stores for theme, role mode, works catalog with filtered/sorted atoms, and localStorage proficiency.*

---

![Design system diagram of three-font typography system: Instrument Serif, Plus Jakarta Sans, and IBM Plex Mono](figures/fig-frontend-10-typography-system.jpg)

*Typography system: Instrument Serif for editorial display, Plus Jakarta Sans for body/UI, IBM Plex Mono for data values.*

---

![Design system diagram of complete light and dark mode color palettes with surface, brand, confidence, assurance, source, and role tokens](figures/fig-frontend-11-color-system.jpg)

*Color system: warm cream/dark navy surfaces, coral red accent, confidence tiers, A0-A3 assurance, five source colors, and role accents.*

---

![UI wireframe showing responsive layout: desktop with 60px left sidebar and editorial grid, mobile with 48px top bar and hamburger overlay](figures/fig-frontend-12-responsive-layout.jpg)

*Responsive layout: desktop fixed sidebar, mobile top bar with hamburger, Tailwind v4 breakpoints for any device.*

---

![Architecture diagram of two-layer WCAG 2.1 AA accessibility testing: Vitest plus vitest-axe and Playwright plus axe-core](figures/fig-frontend-13-accessibility-architecture.jpg)

*Accessibility architecture: fast component-level vitest-axe checks and real-browser Playwright axe-core validation with ARIA pattern catalog.*

---

![Component diagram of PostHog analytics with 12 type-safe events across review, agentic, interaction, and feedback categories](figures/fig-frontend-14-posthog-analytics.jpg)

*PostHog analytics: 12 typed events tracking review approval, agent chat, interactions, and feedback with graceful no-op fallback.*

---

![Component diagram of adaptive UI proficiency model with Jotai store, computeLevel producing three tiers, and useFeatureFlags](figures/fig-frontend-15-adaptive-ui-proficiency.jpg)

*Adaptive UI proficiency: user interactions feed Jotai store, computeLevel produces novice/intermediate/expert, useFeatureFlags adapts UI density.*

</details>

---

## Technology Choices

Each technology choice figure documents a specific architecture decision from the probabilistic PRD -- comparing selected options against alternatives with rationale. Covers framework selection, database strategy, confidence methods, package management, deployment, and sovereignty considerations.

<details>
<summary><strong>18 figures</strong> -- click to expand</summary>

![Comparison chart: PydanticAI versus LangChain showing typed agent code versus middleware-heavy chains](figures/fig-choice-01-pydanticai-over-langchain.jpg)

*PydanticAI over LangChain: typed Pydantic-native agents with fewer dependencies and readable stack traces.*

---

![Architecture decision: CopilotKit with AG-UI protocol comparing open-source streaming against Vercel AI SDK and custom WebSocket](figures/fig-choice-02-copilotkit-agui.jpg)

*CopilotKit AG-UI: open-source streaming with 31 event types and MCP integration for bidirectional shared state.*

---

![Architecture decision: PostgreSQL with pgvector and Apache AGE unifying relational, graph, and vector in single database](figures/fig-choice-03-postgresql-pgvector.jpg)

*PostgreSQL pgvector: relational, graph, and vector unified -- compared against Pinecone, Chroma, and Supabase with hosting spectrum.*

---

![Trade-off analysis: conformal prediction providing distribution-free coverage guarantees over Bayesian posteriors and bootstrap](figures/fig-choice-04-conformal-prediction.jpg)

*Conformal prediction: distribution-free coverage guarantees for heterogeneous music metadata where quality varies across sources.*

---

![Decision diagram: Splink selected for entity resolution using Fellegi-Sunter probabilistic linkage compared against dedupe.io and custom rules](figures/fig-choice-05-splink-linkage.jpg)

*Splink linkage: Fellegi-Sunter EM-trained match weights for artist identity matching across MusicBrainz, Discogs, and file metadata.*

---

![Comparison chart: FastAPI versus Django highlighting async-native Pydantic integration and MCP endpoint streaming](figures/fig-choice-06-fastapi-over-django.jpg)

*FastAPI over Django: async-native, Pydantic-integrated, lightweight modular monolith with MCP streaming support.*

---

![Architecture decision: Next.js 15 App Router driven by CopilotKit React dependency compared against SvelteKit and HTMX](figures/fig-choice-07-nextjs-app-router.jpg)

*Next.js App Router: CopilotKit React dependency, server components, and streaming SSR for confidence display.*

---

![Comparison chart: Jotai atomic state selected over Redux and Zustand showing minimal two-line atom definitions](figures/fig-choice-08-jotai-over-redux.jpg)

*Jotai over Redux: minimal two-line atom definitions for theme, role mode, and works state with zero boilerplate.*

---

![Design token architecture: CSS custom properties flowing through Tailwind v4 with text-var pitfall warning](figures/fig-choice-09-tailwind-v4-css-properties.jpg)

*Tailwind v4 CSS properties: zero-hardcoded-hex color tokens with critical text-[var()] pitfall warning.*

---

![Comparison chart: uv package manager selected over banned pip and conda showing 100x faster Rust-based resolution](figures/fig-choice-10-uv-over-pip.jpg)

*uv over pip: 100x faster Rust-based resolution, deterministic lockfiles, native dependency groups -- pip and conda banned.*

---

![Decision diagram: MCP as consent infrastructure showing machine-readable permission queries compared against REST API and blockchain](figures/fig-choice-11-mcp-permissions.jpg)

*MCP permissions: machine-readable AI training consent queries replacing ambiguous license text with structured allow/deny responses.*

---

![Comparison chart: Alembic selected for database migrations with SQLAlchemy-native autogeneration compared against Django and manual SQL](figures/fig-choice-12-alembic-migrations.jpg)

*Alembic migrations: SQLAlchemy-native autogeneration for version-controlled schema evolution.*

---

![Trade-off analysis: tinytag BSD-3 license selected over mutagen GPL-2.0 preserving permissive licensing](figures/fig-choice-13-tinytag-over-mutagen.jpg)

*tinytag over mutagen: BSD-3 preserves permissive licensing while providing read-only ID3, FLAC, and MP4 tag support.*

---

![Architecture decision: PostHog plus Sentry for observability compared against Datadog, Grafana, and defunct Highlight.io](figures/fig-choice-14-observability-posthog-sentry.jpg)

*PostHog plus Sentry: typed product analytics and error tracking -- Highlight.io deprecated, Datadog cost-prohibitive.*

---

![Corrected cost versus complexity scatter plot showing five deployment paths from Render to Hetzner bare-metal](figures/fig-choice-15-deployment-options.jpg)

*Deployment options: Render (simplest), Hetzner+Ubicloud (recommended), Big Three hyperscalers, and bare-metal Kubernetes.*

---

![Architecture decision: Cloudflare R2 with zero egress fees versus Hetzner, Backblaze, and AWS S3 at 100TB scale](figures/fig-choice-16-object-storage-strategy.jpg)

*Object storage: R2 at $0 egress versus S3 at $9,000/month at 100TB -- critical FinOps for audio-heavy workloads.*

---

![Architecture decision: Pulumi over Terraform showing Python-native alignment, MCP server, and Apache 2.0 versus BSL](figures/fig-choice-17-pulumi-over-terraform.jpg)

*Pulumi over Terraform: Python-native IaC, official MCP server for Claude deployments, Apache 2.0 versus HashiCorp BSL.*

---

![Cloud sovereignty assessment comparing four EU-sovereign providers against US-headquartered providers with CLOUD Act exposure](figures/fig-choice-18-cloud-sovereignty.jpg)

*Cloud sovereignty: Hetzner, OVHcloud, UpCloud, Scaleway versus CLOUD Act/FISA-exposed providers with four sovereignty tiers.*

</details>

---

## PRD Decision Network

The probabilistic PRD figures explain the novel decision framework used to capture architecture choices as a Bayesian network rather than fixed specifications. Covers the ELI5 introduction, full network visualization, foundation/integration/operational decisions, node anatomy, team archetypes, domain overlays, versioning history, and scaffold-versus-product distinction.

![Comparison chart: traditional PRD versus probabilistic PRD showing weighted decision options replacing fixed specs](figures/fig-prd-01-probabilistic-prd-eli5.jpg)

*Probabilistic PRD ELI5: weighted options replace fixed specs, adapting to different team archetypes.*

---

![Network visualization: 78-node Bayesian decision network across five levels with dual-subgraph layout](figures/fig-prd-02-full-decision-network.jpg)

*Full decision network: 78 nodes, 131 conditional probability edges, five levels, dual-subgraph (50 core + 28 ecosystem).*

---

![Decision diagram: four foundational business decisions cascading into architecture-level choices](figures/fig-prd-03-foundation-decisions.jpg)

*Foundation decisions: build vs buy, target market, revenue model, and regulatory posture cascading into architecture.*

---

![Architecture overview: integration-layer decisions showing L2 choices cascading into selected implementation stack](figures/fig-prd-04-integration-decisions.jpg)

*Integration decisions: Anthropic LLM, PydanticAI routing, CopilotKit agentic UI with conditional probability reinforcement.*

---

![Decision diagram: deployment and operations layers with 13 L4 and 14 L5 nodes including ecosystem extensions](figures/fig-prd-05-operational-decisions.jpg)

*Operational decisions: 13 deployment nodes and 14 operations nodes with ecosystem compliance, monitoring, and health.*

---

![Annotated anatomy of a single Bayesian decision node using the LLM provider node as example](figures/fig-prd-06-decision-node-anatomy.jpg)

*Decision node anatomy: options with priors, conditional dependencies, archetype weight overrides, volatility, and domain applicability.*

---

![Comparison chart: four team archetypes producing different probability distributions for database, compute, and build-versus-buy](figures/fig-prd-07-team-archetypes.jpg)

*Team archetypes: Engineer-Heavy, Musician-First, Solo Hacker, Well-Funded Startup -- each activating different PRD paths.*

---

![Architecture overview: domain overlay system showing music attribution and DPP traceability sharing isomorphic core pipeline](figures/fig-prd-08-domain-overlay-system.jpg)

*Domain overlay: music attribution and Digital Product Passport share core pipeline -- differing in sources, assurance levels, and regulation.*

---

![Timeline visualization: PRD evolution from v1.0 through v3.0 showing growth from 15 to 78 decision nodes](figures/fig-prd-09-versioning-timeline.jpg)

*PRD versioning timeline: v1.0 (15 nodes) to v3.0 (78 nodes) across ten versions with 28-node ecosystem expansion.*

---

![Comparison chart: scaffold versus production system showing configurable decision paths versus one fixed architecture](figures/fig-prd-10-scaffold-vs-product.jpg)

*Scaffold vs product: configurable research framework with four archetypes versus deployed production with one fixed architecture.*

---

## Ecosystem Integration

The ecosystem integration figures map the 28 external-facing nodes in the PRD network -- covering integration archetypes, partnership models, TDA providers, CMO licensing, content ID, platform connectors, metadata registries, agent interop protocols, knowledge graphs, ethical certification, compliance reporting, edge inference, eval frameworks, and strategic ambiguity.

<details>
<summary><strong>16 figures</strong> -- click to expand</summary>

![Subgraph overview: 28 ecosystem integration nodes forming coherent cluster within 78-node PRD network](figures/fig-ecosystem-01-subgraph-overview.jpg)

*Ecosystem subgraph: 28 integration nodes within the 78-node PRD network forming a coherent external-facing cluster.*

---

![Three integration archetypes from lightweight MCP adapters to institutional CMO federation](figures/fig-ecosystem-02-three-integration-archetypes.jpg)

*Three archetypes: Simple MCP adapter, Platform Integration connector, and institutional CMO Federation -- escalating commitment.*

---

![Partnership model decision tree cascading to six company node activations](figures/fig-ecosystem-03-partnership-model-decision-tree.jpg)

*Partnership model decision tree: cascading from business posture to activation of six specific company nodes.*

---

![TDA provider landscape: training-time versus post-hoc attribution approaches compared](figures/fig-ecosystem-04-tda-provider-landscape.jpg)

*TDA provider landscape: training-time versus post-hoc attribution approaches with seven methods compared.*

---

![CMO licensing architecture with scaffold providing attribution confidence for royalties](figures/fig-ecosystem-05-cmo-licensing-architecture.jpg)

*CMO licensing architecture: scaffold feeds attribution confidence into CMO royalty distribution pipelines.*

---

![Content ID comparison: fingerprinting versus watermark detection versus embedding similarity](figures/fig-ecosystem-06-content-id-comparison.jpg)

*Content ID comparison: three detection paradigms -- fingerprinting, watermark detection, and embedding similarity.*

---

![Platform connector design normalizing AI music platform metadata to NormalizedRecord](figures/fig-ecosystem-07-platform-connector-design.jpg)

*Platform connector design: normalizing diverse AI music platform metadata into the NormalizedRecord schema.*

---

![Metadata registry map: MusicBrainz, Discogs, SoundExchange, DDEX unified by resolution](figures/fig-ecosystem-08-metadata-registry-map.jpg)

*Metadata registry map: four major registries unified through the entity resolution pipeline.*

---

![Protocol stack: MCP tool access to A2A coordination to agentic commerce layers](figures/fig-ecosystem-09-agent-interop-protocol-stack.jpg)

*Agent interop protocol stack: MCP for tool access, A2A for coordination, ACP/TAP for commerce layers.*

---

![Knowledge graph backends: Apache AGE co-located versus Neo4j Aura versus LightRAG hybrid](figures/fig-ecosystem-10-knowledge-graph-backend-options.jpg)

*Knowledge graph options: Apache AGE co-located with PostgreSQL, Neo4j Aura managed, and LightRAG hybrid.*

---

![Fairly Trained certification: binary audit signal complementing A0-A3 assurance levels](figures/fig-ecosystem-11-fairly-trained-certification-flow.jpg)

*Fairly Trained certification: binary trained/not-trained audit signal complementing the scaffold's A0-A3 assurance levels.*

---

![Compliance pipeline: audit logs and confidence scores into EU AI Act reports](figures/fig-ecosystem-12-compliance-reporting-pipeline.jpg)

*Compliance reporting: audit logs and confidence scores flowing into EU AI Act transparency reports.*

---

![Edge inference decision: server-only MVP default versus edge deployment for latency](figures/fig-ecosystem-13-edge-inference-strategy.jpg)

*Edge inference strategy: server-only MVP default with optional edge deployment for latency-sensitive use cases.*

---

![Eval framework maturity: manual spot-check to automated regression to CI golden datasets](figures/fig-ecosystem-14-attribution-eval-framework-maturity.jpg)

*Eval framework maturity: manual spot-checks, automated regression, CI golden datasets -- three maturity stages.*

---

![Company node activation matrix: partnership model determines which six companies engage](figures/fig-ecosystem-15-company-node-activation-matrix.jpg)

*Company node activation: partnership model determines which of six companies (Sureel, Musical AI, Suno, Udio, STIM, SoundExchange) engage.*

---

![None prior heatmap: ecosystem nodes show 0.40-0.55 strategic ambiguity encoding](figures/fig-ecosystem-16-none-prior-heatmap.jpg)

*None-prior heatmap: ecosystem nodes at 0.40-0.55 encode strategic ambiguity -- deliberate optionality, not missing data.*

</details>

---

## Music AI Landscape

The landscape figures provide the broadest context -- mapping the entire music AI field across problem taxonomy, funding patterns, research-to-product gaps, disruption points, maturity spectrum, stakeholder incentives, regulatory fragmentation, TDA methods, watermarking robustness, content ID evolution, licensing models, and research priorities.

<details>
<summary><strong>33 figures</strong> -- click to expand</summary>

![12-category music AI taxonomy grid: generative, analytical, and infrastructure problems each with maturity levels](figures/fig-landscape-01-problem-taxonomy.jpg)

*Problem taxonomy: 12 music AI categories in generative, analytical, and infrastructure groups -- each with distinct maturity levels.*

---

![Split-panel funding comparison: $375M+ to music generation versus less than $70M to attribution showing 5:1 gap](figures/fig-landscape-02-funding-by-category.jpg)

*Funding by category: $375M+ to generation versus under $70M to attribution -- a 5:1 investment gap.*

---

![Three research streams flowing from papers to products through a translation gap](figures/fig-landscape-03-papers-to-products.jpg)

*Papers to products: influence functions, embeddings, and attribution-by-design streams bridging the research-to-product gap.*

---

![Music value chain with five AI disruption points, each creating a corresponding attribution question](figures/fig-landscape-04-disruption-points.jpg)

*Disruption points: five places in the music value chain where AI creates new attribution questions.*

---

![Six attribution approaches on three axes: TRL, adoption, regulation](figures/fig-landscape-05-maturity-spectrum.jpg)

*Maturity spectrum: six approaches mapped by technology readiness, industry adoption, and regulatory pressure.*

---

![Decision funnel: 7 attribution methods filtered by 4 constraints to 1-2 viable approaches per startup](figures/fig-landscape-06-founder-decision-framework.jpg)

*Founder decision framework: seven methods through four constraint filters yielding one to two viable approaches.*

---

![Four stakeholder panels: artists, labels, platforms, and regulators with conflicting attribution wants](figures/fig-landscape-07-misaligned-incentives.jpg)

*Misaligned incentives: artists want credit, labels want control, platforms want scale, regulators want transparency.*

---

![Five jurisdiction panels: EU, US, UK, Nordic, Asia-Pacific regulatory approaches to AI music attribution](figures/fig-landscape-08-regulatory-fragmentation.jpg)

*Regulatory fragmentation: five jurisdictions with incompatible approaches -- EU AI Act, US copyright, UK code of practice.*

---

![Seven TDA methods compared: what each measures, model access needed, and scalability](figures/fig-landscape-09-seven-tda-methods.jpg)

*Seven TDA methods: influence functions, Shapley values, activation analysis, probing, embedding similarity, watermarking, and provenance -- on a causal-to-corroborative axis.*

---

![Split panel: post-hoc and by-design attribution paradigms converging toward hybrid zone with A0-A3 bridge](figures/fig-landscape-10-two-paradigms.jpg)

*Two paradigms: post-hoc detection versus attribution-by-design converging at a hybrid zone bridged by A0-A3 assurance.*

---

![22 watermarking schemes tested against 22 attacks with robustness matrix](figures/fig-landscape-11-watermarking-robustness.jpg)

*Watermarking robustness: 22 schemes versus 22 attacks -- no single scheme survives all attack types.*

---

![Four generations of content ID: fingerprinting to AI detection, each solving prior generation failures](figures/fig-landscape-12-content-id-evolution.jpg)

*Content ID evolution: four generations from acoustic fingerprinting through perceptual hashing and watermarks to AI detection.*

---

![Six music identity standards as disconnected islands with broken bridges](figures/fig-landscape-13-metadata-mess.jpg)

*Metadata mess: ISRC, ISWC, ISNI, IPI, DDEX, and MBID as disconnected islands -- no unified provenance chain exists.*

---

![On-chain versus off-chain provenance trade-offs with EU pharmaceutical serialization as hybrid precedent](figures/fig-landscape-14-onchain-offchain.jpg)

*On-chain vs off-chain: provenance trade-offs with pharmaceutical serialization as a cross-domain hybrid precedent.*

---

![Four-stage evidence chain from AI detection to legal claim showing confidence degradation at each stage](figures/fig-landscape-15-evidence-chain.jpg)

*Evidence chain: confidence degrades from AI detection (0.95) through attribution (0.80) and provenance (0.70) to legal claim (0.50).*

---

![Cross-domain UQ isomorphism: medical, automotive, financial domains mapped to music attribution](figures/fig-landscape-16-uq-cross-domain.jpg)

*UQ cross-domain: medical diagnosis, autonomous vehicles, and financial risk share uncertainty quantification methods with music attribution.*

---

![Five licensing models compared at 1K, 1M, and 1B scale showing where economics break down](figures/fig-landscape-17-licensing-models.jpg)

*Licensing models: per-track, blanket, micro-licensing, subscription, and revenue-share compared at three scale points.*

---

![Four ascending steps: CMO evolution from traditional blanket through digital streaming to AI licensing and federation](figures/fig-landscape-18-cmo-transformation.jpg)

*CMO transformation: blanket licensing to digital streaming to AI licensing to multi-CMO federation -- four evolutionary stages.*

---

![Three trust layers: binary Fairly Trained, graduated A0-A3 assurance, and EU AI Act regulation with food safety analogy](figures/fig-landscape-19-ethical-certification.jpg)

*Ethical certification: Fairly Trained (binary), A0-A3 (graduated), and EU AI Act (regulatory) -- three complementary trust layers.*

---

![Split panel: music A0-A3 assurance and code attribution stacks with shared Oracle Problem](figures/fig-landscape-19b-ai-code-landscape.jpg)

*AI code landscape: music A0-A3 assurance parallels code unknown/AI/mixed/human attribution -- both face the Oracle Problem.*

---

![Five-layer voice rights stack from consent to compensation with coverage matrix](figures/fig-landscape-20-voice-rights-stack.jpg)

*Voice rights stack: five layers from consent through detection to compensation -- no company spans all layers.*

---

![Timeline from 2000-2025: MIR milestones above and commercial products below with citation gap](figures/fig-landscape-21-mir-history.jpg)

*MIR history: 25-year timeline of research milestones and commercial products with a persistent citation gap.*

---

![Four ascending stages of AI music platform maturation from consumer toy to attribution-integrated professional tools](figures/fig-landscape-22-platform-evolution.jpg)

*Platform evolution: consumer toy to prosumer to professional to attribution-integrated -- four maturation stages.*

---

![Decision matrix mapping 12 infrastructure components to build/buy/partner for three team archetypes](figures/fig-landscape-23-build-vs-buy.jpg)

*Build vs buy: 12 components mapped across three team archetypes -- each making different build/buy/partner choices.*

---

![Two scenarios: $7.4B market split without and with attribution showing 20% revenue flow to artists](figures/fig-landscape-24-revenue-distribution.jpg)

*Revenue distribution: without attribution 80% to platforms, with attribution 20% flows to artists from $7.4B market.*

---

![Four-panel research priority forecast: multimodal, streaming, AI-assisted, and federated attribution for 2026-2028](figures/fig-landscape-25-research-priorities.jpg)

*Research priorities 2026-2028: multimodal, streaming, AI-assisted, and federated attribution as four priority areas.*

---

![Four-domain method transfer: supply chain, finance, pharma, game theory mapped to music attribution](figures/fig-landscape-26-cross-domain-transfer.jpg)

*Cross-domain transfer: supply chain, finance, pharma, and game theory solutions mapped to music attribution targets.*

---

![Agentic attribution flowchart: AI agent queries MCP, coordinates via A2A, pays via ACP automatically](figures/fig-landscape-27-agentic-attribution.jpg)

*Agentic attribution: AI agent queries MCP for rights, coordinates via A2A, and pays via ACP -- fully automated.*

---

![Five emerging 2026 service categories: attribution-aaS, ethical certification, voice rights, CMO federation, AI detection](figures/fig-landscape-28-emerging-categories.jpg)

*Emerging categories: attribution-as-a-service, ethical certification, voice rights, CMO federation, and AI detection.*

---

![Four-level regulatory cascade: legislation to codes of practice to standards to architecture](figures/fig-landscape-29-regulatory-cascade.jpg)

*Regulatory cascade: legislation (EU AI Act) cascades to codes of practice, then standards, then architecture requirements.*

---

![Three-circle Venn: MIR, XAI, and UQ converge at music attribution triple intersection](figures/fig-landscape-30-convergence-thesis.jpg)

*Convergence thesis: MIR + XAI + UQ converge at the triple intersection -- music attribution as the synthesis field.*

---

![Three-panel open problems by time horizon: solvable 2yr, hard 5yr, fundamental 10yr+](figures/fig-landscape-31-open-problems.jpg)

*Open problems: solvable in 2 years, hard in 5 years, fundamental in 10+ years -- with funding inversion pattern.*

---

![Six-step circular meta-loop: landscape scan to market intel to PRD update to architecture to product to response](figures/fig-landscape-32-meta-loop.jpg)

*Meta-loop: landscape scan feeds market intel, updates PRD, shapes architecture, builds product, monitors market response -- repeat.*

</details>

---

## Theoretical Foundations

The theory figures explain the six theoretical pillars from the companion paper: the Oracle Problem, attribution-by-design, deterrence economics, A0-A3 assurance levels, the two-friction taxonomy, confidence and uncertainty, entity resolution, and MCP consent infrastructure. Each concept is presented at both ELI5 and technical depth.

<details>
<summary><strong>22 figures</strong> -- click to expand</summary>

![Concept diagram: three paint tubes flow into a blender producing uniform purple that cannot be unmixed -- the Oracle Problem](figures/fig-theory-01-oracle-problem-eli5.jpg)

*Oracle Problem ELI5: once creative works are blended in an AI model, separating individual contributions is as impossible as unmixing paint.*

---

![Technical pipeline: creator audio, MIDI, and metadata enter a training black box where tokenization and gradient descent destroy attribution identity](figures/fig-theory-02-oracle-problem-technical.jpg)

*Oracle Problem technical: tokenization, gradient descent, and weight averaging destroy attribution identity at each training stage.*

---

![Comparison chart: post-hoc detection with broken arrows versus attribution-by-design with embedded A0-A3 provenance](figures/fig-theory-03-attribution-by-design-vs-posthoc.jpg)

*Attribution-by-design vs post-hoc: embedded provenance at ISRC/ISWC assurance levels versus reverse engineering after the fact.*

---

![Deterrence economics formula p times d times F >= g with tax audit analogy](figures/fig-theory-04-deterrence-economics.jpg)

*Deterrence economics: 3% audit rate deters infringement when penalties are large -- imperfect detection still protects via economic incentives.*

---

![Four-step staircase: A0 sticky note, A1 business card, A2 passport, A3 biometric scan](figures/fig-theory-05-assurance-levels-eli5.jpg)

*Assurance levels ELI5: A0 no ID, A1 single claim, A2 multiple sources agree, A3 direct artist verification -- escalating trust.*

---

![Pyramid mapping A0-A3 to industry identifiers: A0 none, A1 ISRC, A2 ISWC, A3 ISNI plus IPI](figures/fig-theory-06-assurance-standards-mapping.jpg)

*Assurance-standards mapping: A0 no identifier, A1 ISRC only, A2 adds ISWC, A3 adds ISNI and IPI -- with analog hole warning.*

---

![Decision tree: deterministic flowchart classifying attribution records into A0-A3 assurance levels](figures/fig-theory-07-assurance-decision-tree.jpg)

*Assurance decision tree: check artist verification (A3), source agreement (A2), any identifier (A1), default to A0.*

---

![Split panel: airport security line (administrative friction to automate) versus record store browsing (discovery friction to preserve)](figures/fig-theory-08-two-friction-eli5.jpg)

*Two-friction ELI5: administrative friction (licensing forms) to automate versus discovery friction (curation) to preserve.*

---

![Three-question diagnostic: human agency, artistic identity, community building -- YES is discovery, all NO is administrative](figures/fig-theory-09-friction-diagnostic-test.jpg)

*Friction diagnostic: three questions classify any process as administrative (automate) or discovery (preserve).*

---

![Real-world examples: sync licensing, PRO registration, ISRC assignment to automate versus DJ curation, collaboration, playlist gatekeeping to preserve](figures/fig-theory-10-friction-examples.jpg)

*Friction examples: sync licensing and royalty reporting are administrative; DJ curation and artist collaboration are discovery.*

---

![Weather forecast analogy: 80% rain versus 70-90% range paralleling 0.85 versus 0.78-0.92 confidence](figures/fig-theory-11-confidence-vs-uncertainty-eli5.jpg)

*Confidence vs uncertainty ELI5: point estimate versus interval -- narrow ranges signal certainty, wide ranges signal need for evidence.*

---

![Four-step conformal prediction: calibration set to nonconformity scores to quantile threshold to prediction sets with coverage guarantee](figures/fig-theory-12-conformal-prediction.jpg)

*Conformal prediction: distribution-free, finite-sample valid confidence intervals requiring no model assumptions.*

---

![Reliability diagram: predicted confidence versus observed frequency with perfect diagonal, overconfident curve below, and ECE metric](figures/fig-theory-13-reliability-diagram.jpg)

*Reliability diagram: evaluating calibration quality -- perfect diagonal, overconfident below, underconfident above, with ECE metric.*

---

![Venn-style overlap of five metadata sources with confidence rising from 0.35 (one source) to 0.94 (four plus artist)](figures/fig-theory-14-source-agreement-scoring.jpg)

*Source agreement scoring: confidence rises from 0.35 with one source to 0.94 with four sources plus artist verification.*

---

![Three conference name tags: E. Voss, Elena Voss, VOSS ELENA converging to single unified person with ISNI](figures/fig-theory-15-entity-resolution-eli5.jpg)

*Entity resolution ELI5: the same artist appears differently across sources -- resolution unifies variants into one identity with ISNI.*

---

![Five-step cascade: identifier match, string similarity, embedding match, LLM judgment, Splink linkage -- cheapest first](figures/fig-theory-16-resolution-cascade.jpg)

*Resolution cascade: five steps from free identifier match to expensive LLM judgment -- each fires only when prior is inconclusive.*

---

![2D t-SNE projection of entity embeddings showing three tight clusters with ambiguous zone escalating to LLM](figures/fig-theory-17-embedding-space.jpg)

*Embedding space: three artist clusters with within-cluster distance below 0.1, between-cluster above 0.7, and ambiguous zone.*

---

![Graph-based resolution: mention nodes connected by weighted edges, community detection identifies two ISNI-resolved clusters](figures/fig-theory-18-graph-resolution.jpg)

*Graph resolution: weighted edges from cascade scoring, community detection resolves mention nodes into distinct ISNI entities.*

---

![Library card analogy: borrow yes, photocopy no paralleling streaming yes, AI voice cloning no](figures/fig-theory-19-mcp-consent-eli5.jpg)

*MCP consent ELI5: library permissions map to music permissions -- streaming yes, AI voice cloning no, remix ask first.*

---

![Sequence diagram: AI agent sends check_permission query with ISRC, MCP server returns DENY with reason and alternatives](figures/fig-theory-20-mcp-permission-flow.jpg)

*MCP permission flow: structured ISRC query, PostgreSQL lookup, DENY response with machine-readable reason and allowed alternatives.*

---

![Architecture: MCP server for AI agents and FastAPI REST for humans sharing PostgreSQL permission store with audit log](figures/fig-theory-21-consent-infrastructure.jpg)

*Consent infrastructure: dual interfaces -- MCP for machines and REST for humans -- sharing permission store with audit log.*

---

![Permission matrix: five Imogen Heap songs versus five use types colored green/red/amber for allow/deny/conditional](figures/fig-theory-22-permission-matrix.jpg)

*Permission matrix: granular per-work, per-use-type consent -- streaming, sync, download, AI training, voice cloning.*

</details>

---

## Scenarios

Scenario figures illustrate how different teams and strategies activate different subsets of the 78-node PRD network, including MVP activation paths, archetype comparisons, build-versus-buy cascades, volatility patterns, network growth, ecosystem dependencies, component clustering, and strategic ambiguity encoding.

![MVP scenario: 23 of 78 nodes activated as highest-probability path through PRD network](figures/fig-scenario-01-mvp-scenario-activation.jpg)

*MVP scenario: 23 nodes activated as the highest-probability path through the 78-node PRD network.*

---

![Four archetypes activating different 78-node subsets with ecosystem sensitivity](figures/fig-scenario-02-four-archetype-comparison.jpg)

*Four-archetype comparison: each team type activates different PRD subsets with varying ecosystem sensitivity.*

---

![Decision cascade from build_vs_buy_posture: highest-influence node with 27 downstream edges](figures/fig-scenario-03-decision-cascade-build-vs-buy.jpg)

*Build vs buy cascade: the highest-influence node with 27 downstream edges -- every decision ripples from this posture.*

---

![Volatility heatmap: 78 PRD nodes showing core stable versus ecosystem volatile bifurcation](figures/fig-scenario-04-volatility-heatmap.jpg)

*Volatility heatmap: core infrastructure nodes are stable; ecosystem integration nodes show high volatility.*

---

![Network growth: 15 to 78 nodes across 10 versions maintaining disciplined edge-to-node ratio](figures/fig-scenario-05-network-growth-over-time.jpg)

*Network growth: 15 to 78 nodes across ten PRD versions maintaining a disciplined edge-to-node ratio.*

---

![Ecosystem dependency graph: partnership_model gating company nodes in activation chains](figures/fig-scenario-06-ecosystem-dependency-graph.jpg)

*Ecosystem dependencies: partnership_model node gates which company nodes activate in downstream chains.*

---

![L3 component clustering: 24 nodes in TDA/ID, licensing, platform, infrastructure, and company groups](figures/fig-scenario-07-l3-component-clustering.jpg)

*L3 component clustering: 24 nodes grouped into TDA/ID, licensing, platform, infrastructure, and company clusters.*

---

![Strategic ambiguity: core nodes committed versus ecosystem nodes preserving 0.40-0.55 optionality](figures/fig-scenario-08-strategic-ambiguity-encoding.jpg)

*Strategic ambiguity: committed core selections versus ecosystem nodes deliberately preserving 0.40-0.55 optionality.*

---

## How-To Guides

Step-by-step visual guides for common tasks: adding data sources, reproducing paper claims, querying the API, using the agent sidebar, checking MCP permissions, running tests, deploying to production, creating figures, and contributing to the project.

<details>
<summary><strong>9 figures</strong> -- click to expand</summary>

![Five-step workflow for adding a new data source to the ETL pipeline](figures/fig-howto-01-add-new-data-source.jpg)

*How to add a data source: five steps from extractor creation through BaseExtractor interface to quality gate configuration and tests.*

---

![Three-column reproducibility map linking paper sections to code modules and test commands](figures/fig-howto-02-reproduce-paper-claims.jpg)

*How to reproduce paper claims: paper sections map to code modules map to test commands -- every claim verifiable via make test.*

---

![API request lifecycle from curl through FastAPI routing to JSON response with confidence scores](figures/fig-howto-03-query-the-api.jpg)

*How to query the API: curl to FastAPI to attribution engine to JSON response with per-field confidence and A0-A3 assurance.*

---

![Split-panel: works dashboard with confidence scores on left, three-step conversational flow on right](figures/fig-howto-04-use-agent-sidebar.jpg)

*How to use the agent sidebar: natural-language query, tool invocation, transparent confidence-scored answer with provenance.*

---

![Four-step MCP permission check workflow from AI agent query through server evaluation to ALLOW/DENY response](figures/fig-howto-05-check-permissions-mcp.jpg)

*How to check MCP permissions: query training rights, server evaluates, returns structured ALLOW/DENY with assurance level.*

---

![Decision tree for selecting the correct test suite based on code change type](figures/fig-howto-06-run-tests.jpg)

*How to run tests: decision tree branching from Python backend, frontend, or config change to the correct make command.*

---

![Five-step deployment pipeline with four deployment paths from Render to bare-metal Kubernetes](figures/fig-howto-07-deploy-to-production.jpg)

*How to deploy: Docker build, configure, push, then branch to Render, Kamal 2, Hetzner+Ubicloud, or Big Three -- health check last.*

---

![Six-step figure creation pipeline from plan through Nano Banana Pro generation to quality verification](figures/fig-howto-08-create-figures-nano-banana.jpg)

*How to create figures: read plan, compose prompt, generate via Nano Banana Pro, verify quality, commit -- content-style decoupling.*

---

![Six-step contribution workflow from fork through CLAUDE.md rules to pre-commit verification and PR](figures/fig-howto-09-how-to-contribute.jpg)

*How to contribute: fork, branch, code under CLAUDE.md rules, pre-commit hooks, pytest, and PR -- quality gates non-negotiable.*

</details>

---

## Technology Trends

Trend figures track the fast-moving technology landscape that influences PRD node selections -- agent framework consolidation, pgvector performance, OpenTelemetry GenAI stack, evaluation frameworks, edge AI platforms, graph knowledge bases, STIM revenue flows, and the trend-to-scaffold implication matrix.

![Agent framework consolidation: PydanticAI, LangGraph, and CrewAI/AG2 in three tiers](figures/fig-trends-01-agent-framework-consolidation.jpg)

*Agent framework consolidation: PydanticAI (typed, Pydantic-native), LangGraph (graph orchestration), CrewAI/AG2 (multi-agent).*

---

![pgvector evolution: 471 QPS at 99% recall validates PostgreSQL Unified architecture](figures/fig-trends-02-pgvector-performance-evolution.jpg)

*pgvector performance: 471 QPS at 99% recall -- validates the PostgreSQL Unified architecture decision.*

---

![OTel GenAI stack: PydanticAI to Logfire to any OpenTelemetry-compatible backend](figures/fig-trends-03-otel-genai-stack.jpg)

*OpenTelemetry GenAI: PydanticAI instrumented via Logfire to any OTel-compatible observability backend.*

---

![Eval maturity spectrum: PydanticAI mocks to Promptfoo CI to Braintrust dataset eval](figures/fig-trends-04-eval-framework-maturity-spectrum.jpg)

*Eval framework maturity: PydanticAI mocks (fast), Promptfoo CI regression (automated), Braintrust golden datasets (comprehensive).*

---

![Edge AI platforms: Cloudflare Workers AI, Deno Deploy, and Supabase Edge compared](figures/fig-trends-05-edge-ai-platforms.jpg)

*Edge AI platforms: Cloudflare Workers AI, Deno Deploy, and Supabase Edge Functions -- latency versus ecosystem trade-offs.*

---

![Graph knowledge bases: Neo4j Aura Agent versus Apache AGE with LightRAG on PostgreSQL](figures/fig-trends-06-graph-knowledge-base-options.jpg)

*Graph knowledge bases: Neo4j Aura managed versus Apache AGE co-located with PostgreSQL plus LightRAG hybrid.*

---

![STIM revenue flow: AI output to confidence scoring to per-output royalty to rights holders](figures/fig-trends-07-stim-revenue-flow.jpg)

*STIM revenue flow: AI-generated output triggers confidence scoring, per-output royalty calculation, and rights holder distribution.*

---

![Trend-to-scaffold matrix: 10 tech trends mapped to PRD node impacts and reclassifications](figures/fig-trends-08-scaffold-to-trend-implication-matrix.jpg)

*Trend-to-scaffold matrix: ten technology trends mapped to specific PRD node impacts and option reclassifications.*
