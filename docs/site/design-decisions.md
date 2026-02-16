# Design Decisions

> Every technology choice in this scaffold was deliberated through a probabilistic PRD decision network with 78 nodes across 5 levels. This page visualizes the key "why" behind each decision.

---

## How We Decide: Probabilistic PRDs

Traditional PRDs say "we will use X." A probabilistic PRD says "we will probably use X (60%), but Y (25%) and Z (15%) are viable depending on your team." The scaffold's decision network is a Bayesian graph where upstream choices shift downstream probabilities -- and four team archetypes (Engineer-Heavy, Musician-First, Solo Hacker, Well-Funded) produce four fundamentally different instantiations from the same network.

### What Is a Probabilistic PRD?

![Comparison chart: traditional product requirements document versus probabilistic PRD for music attribution scaffold, showing how weighted decision options replace fixed specs and adapt transparent confidence scoring to different team archetypes -- enabling open-source flexibility instead of one-size-fits-all architecture.](figures/fig-prd-01-probabilistic-prd-eli5.jpg)

*A probabilistic PRD replaces fixed specifications with weighted options that shift depending on team constraints, enabling the same music attribution scaffold to serve engineer-heavy startups, musician-first teams, and solo hackers alike.*

### Full Decision Network Overview

![Network visualization: 78-node Bayesian decision network for the music attribution scaffold across five levels with dual-subgraph layout -- 50 core infrastructure nodes and 28 ecosystem integration nodes connected by approximately 131 conditional probability edges governing transparent confidence scoring.](figures/fig-prd-02-full-decision-network.jpg)

*The full probabilistic PRD decision network (v3.0.0) maps 78 architectural choices across two coherent subgraphs -- core infrastructure (50 nodes) and ecosystem integration (28 nodes) -- from L1 business strategy through L5 operations, connected by approximately 131 conditional probability edges.*

### Foundation Decisions

![Decision diagram: four foundational business decisions -- build versus buy, target market, revenue model, and regulatory posture -- cascading into architecture-level choices for the music attribution scaffold, with skip connections showing how business strategy directly shapes music metadata infrastructure and confidence scoring design.](figures/fig-prd-03-foundation-decisions.jpg)

*The L1 business layer sets the probability landscape for all downstream technology decisions: Build vs Buy, Target Market, Revenue Model, and Regulatory Posture cascade into L2 architecture choices, with skip connections reaching directly to database and compute decisions.*

### Integration Decisions

![Architecture overview: integration-layer decisions in the music attribution scaffold showing how L2 architecture choices cascade into the selected implementation stack -- Anthropic LLM provider, PydanticAI routing, and CopilotKit agentic UI -- with conditional probability reinforcement between each open-source component selection.](figures/fig-prd-04-integration-decisions.jpg)

*The scaffold's reference implementation selects a coherent integration stack where each choice reinforces the others: Anthropic primary (Haiku 4.5 default), PydanticAI native routing (FallbackModel + env var override), and CopilotKit AG-UI (31-event SSE streaming), all connected by Bayesian conditional probabilities.*

### Operational Decisions

![Decision diagram: deployment and operations layers of the music attribution scaffold PRD v3.0.0, showing 13 L4 deployment nodes and 14 L5 operations nodes including ecosystem integration cascades for compliance reporting, attribution accuracy monitoring, and partnership health metrics.](figures/fig-prd-05-operational-decisions.jpg)

*PRD v3.0.0 expands deployment to 13 L4 nodes and operations to 14 L5 nodes. The v3.0.0 ecosystem expansion added 4 new L4 nodes (compliance reporting, provenance store, golden datasets, edge deployment) cascading into 4 new L5 monitoring nodes.*

### Decision Node Anatomy

![Annotated diagram: anatomy of a single Bayesian decision node in the music attribution scaffold probabilistic PRD, using the LLM provider node as example -- showing options with prior probabilities, conditional dependencies, team archetype weight overrides, volatility classification, and domain applicability scores for transparent confidence scoring.](figures/fig-prd-06-decision-node-anatomy.jpg)

*Each decision node is a self-contained Bayesian unit: options with prior probabilities summing to 1.0, conditional tables linking to parent decisions, archetype-specific weight overrides, and volatility classification -- all defined in a machine-readable YAML schema.*

### Team Archetypes

![Comparison chart: four team archetypes for the music attribution scaffold -- Engineer-Heavy, Musician-First, Solo Hacker, and Well-Funded Startup -- each producing different probability distributions for database, compute, and build-versus-buy decisions, demonstrating how the open-source attribution scaffold adapts to diverse music credits workflows.](figures/fig-prd-07-team-archetypes.jpg)

*Four team archetypes act as probability lenses on the same decision network: an engineer-heavy startup gravitates toward PostgreSQL and custom builds, while a musician-first team favors Supabase and managed services -- same scaffold, four fundamentally different instantiations.*

### Domain Overlay System

![Architecture overview: domain overlay system showing how the music attribution scaffold and Digital Product Passport traceability share an isomorphic core pipeline -- sources, entity resolution, unified record with confidence scoring, permissioned API, and agentic consumers -- while differing in music metadata sources, assurance levels (A0-A3 versus T0-T3), and regulatory requirements.](figures/fig-prd-08-domain-overlay-system.jpg)

*The domain overlay system demonstrates the scaffold's generalizability: music attribution (A0-A3 assurance, MCP consent API) and supply chain traceability (T0-T3 assurance, Digital Link API) are isomorphic instantiations of the same pipeline architecture.*

### PRD Versioning Timeline

![Timeline visualization: evolution of the music attribution scaffold probabilistic PRD from v1.0 core foundation through v3.0 ecosystem expansion, showing growth from 15 to 78 decision nodes across ten versions.](figures/fig-prd-09-versioning-timeline.jpg)

*The probabilistic PRD has grown from 15 initial nodes (v1.0) to 78 nodes (v3.0) across ten versions, with the v3.0 Discussion expansion adding 28 ecosystem integration nodes and approximately 63 edges -- the largest single increment, bringing total edges to approximately 131.*

### Scaffold vs Product

![Comparison chart: open-source music attribution scaffold versus production system -- the scaffold offers configurable decision paths, research-oriented trade-off exploration, and a probabilistic PRD with four team archetypes, while a production system deploys one fixed architecture, highlighting that this repository is a teaching and research framework for music credits and transparent confidence scoring.](figures/fig-prd-10-scaffold-vs-product.jpg)

*This repository is a scaffold -- a configurable research framework with weighted decision options, four team archetypes, and two domain overlays -- not a deployed production system. Companion code to Teikari (2026), SSRN No. 6109087.*

---

## Technology Choices

### AI & Agent Framework

#### PydanticAI over LangChain

![Comparison chart: PydanticAI versus LangChain for music attribution AI framework, showing typed Pydantic-native agent code versus middleware-heavy chain composition, with PydanticAI selected for transparent confidence scoring with fewer dependencies and readable stack traces in an open-source attribution scaffold.](figures/fig-choice-01-pydanticai-over-langchain.jpg)

*PydanticAI provides typed, zero-middleware LLM integration for the music attribution scaffold, chosen over LangChain for its simplicity, single-dependency footprint, and native FallbackModel failover (PRD node: `ai_framework_strategy = direct_api_pydantic`).*

The scaffold chose `direct_api_pydantic` over orchestration frameworks. This is a philosophical choice: thin typed wrappers over heavy middleware. PydanticAI provides typed, Pydantic-native LLM integration with zero middleware -- the scaffold values simplicity and type safety over framework magic. One dependency replaces fifty transitive ones, stack traces remain readable, and FallbackModel provides zero-config failover between providers.

#### CopilotKit + AG-UI

![Architecture decision: CopilotKit with AG-UI protocol selected for music attribution agentic UI, comparing open-source streaming with 31 event types and MCP integration against Vercel AI SDK and custom WebSocket, enabling transparent confidence scoring through bidirectional shared state.](figures/fig-choice-02-copilotkit-agui.jpg)

*CopilotKit + AG-UI was selected as the agentic UI framework, providing 31-event SSE streaming, native MCP permission queries, and bidirectional state sharing via `useCopilotReadable`/`useCopilotAction` hooks (PRD node: `agentic_ui_framework = copilotkit_agui`, P=0.50).*

CopilotKit provides the most complete open-source agentic UI stack: 28.7k GitHub stars, MCP integration shipping January 2026, and the AG-UI protocol with 31 event types for real-time streaming. The bidirectional shared state model lets the frontend expose attribution context to the agent while the agent pushes confidence updates back -- all over standard SSE.

---

### Data & Storage

#### PostgreSQL + pgvector

![Architecture decision: PostgreSQL with pgvector and Apache AGE unifying relational, graph, and vector capabilities in a single database for music attribution, compared against Pinecone, Chroma, and Supabase, with a hosting spectrum from Neon scale-to-zero for MVP through Ubicloud managed PostgreSQL on Hetzner for budget production to self-managed CloudNativePG for expert operators in the open-source attribution scaffold.](figures/fig-choice-03-postgresql-pgvector.jpg)

*PostgreSQL Unified provides relational SQL, graph queries (Apache AGE), and vector search (pgvector) in a single process. Hosting ranges from Neon (scale-to-zero for MVP, EU data residency) through Ubicloud managed PG on Hetzner (budget production) to self-managed CloudNativePG (expert bare-metal).*

One database does three jobs: relational, graph, and vector. A single PostgreSQL instance handles structured metadata, knowledge graph traversals (Apache AGE), and embedding similarity search (pgvector) -- eliminating multi-database complexity. The hosting spectrum accommodates every team archetype, from Neon's scale-to-zero at $0-19/month to self-managed CNPG on Hetzner bare-metal.

#### Splink for Entity Linkage

![Decision diagram: Splink selected for music attribution entity resolution using Fellegi-Sunter probabilistic linkage with EM-trained match weights, compared against dedupe.io and custom rules for matching artist identities across MusicBrainz, Discogs, and file metadata sources in the open-source attribution scaffold.](figures/fig-choice-05-splink-linkage.jpg)

*Splink implements the Fellegi-Sunter model with EM-trained match weights for probabilistic entity resolution, enabling scalable and interpretable linkage of artist identities across heterogeneous music metadata sources.*

The same artist appears differently across sources: "Bjork Gudmundsdottir" in MusicBrainz, "Bjork" in Discogs, "bjork" in ID3 tags. Splink applies the Fellegi-Sunter model with EM-trained match weights to produce interpretable probabilistic linkage, scaling to millions of records via DuckDB/Spark backends. The Splink v4 API uses `from splink import block_on` (top-level import).

#### Alembic for Migrations

![Comparison chart: Alembic selected for music attribution database migrations with SQLAlchemy-native autogeneration from PostgreSQL schema models, compared against Django migrations and manual SQL for version-controlled music metadata schema evolution in the open-source attribution scaffold.](figures/fig-choice-12-alembic-migrations.jpg)

*Alembic provides SQLAlchemy-native migration management, ensuring the same model definitions that drive data access also drive schema evolution with autogenerated, version-controlled migration files.*

The scaffold uses SQLAlchemy (not Django ORM) for data access, making Alembic the natural migration tool. The same model definition drives both runtime queries and schema evolution via `alembic revision --autogenerate`. Migration files live in the `alembic/` directory, version-controlled in git.

#### Object Storage Strategy

![Architecture decision: Cloudflare R2 selected for music attribution scaffold object storage with zero egress fees, compared against Hetzner Object Storage, Backblaze B2, and AWS S3 in an egress cost table showing $0 versus $9,000 per month at 100TB scale -- a critical FinOps decision for audio-heavy workloads where preview serving dominates bandwidth costs in the open-source attribution platform.](figures/fig-choice-16-object-storage-strategy.jpg)

*Cloudflare R2 eliminates egress fees entirely for audio workloads -- at 100TB/month, R2 saves $9,000 versus AWS S3. The S3-compatible API means switching requires only endpoint configuration, not code changes (PRD v2.1.0 node: object_storage).*

Audio previews, waveform renders, and metadata exports make egress the dominant storage cost. A 30-second MP3 preview is roughly 500KB per request. Cloudflare R2's zero-egress pricing ($0 at any scale) versus AWS S3's $0.09/GB makes it the recommended choice for audio-heavy workloads, with an S3-compatible API for drop-in migration.

---

### Confidence & Uncertainty

#### Conformal Prediction

![Trade-off analysis: conformal prediction selected for transparent confidence scoring in music attribution, providing distribution-free coverage guarantees over Bayesian posteriors and bootstrap intervals, essential for heterogeneous music metadata where data quality varies across MusicBrainz, Discogs, and file sources.](figures/fig-choice-04-conformal-prediction.jpg)

*Conformal prediction delivers mathematically guaranteed coverage rates without distributional assumptions, making it the preferred confidence scoring method where metadata quality varies wildly across curated, community, and file-embedded sources (see SConU calibration in SSRN 6109087).*

Music metadata quality varies wildly: MusicBrainz (curated) vs Discogs (community) vs ID3 tags (chaotic). No single distribution fits. Conformal prediction requires only exchangeability (the weakest distributional assumption) and provides a finite-sample coverage guarantee: P(true value in prediction set) >= 1 - alpha. The size of the prediction set itself signals uncertainty -- a set of size 1 means the model is confident, while a set of size 3 means it is not.

---

### Web & Frontend

#### FastAPI over Django

![Comparison chart: FastAPI versus Django for music attribution API serving, highlighting async-native Pydantic integration and MCP endpoint streaming for transparent confidence scoring, with FastAPI selected as lightweight modular monolith over Django's batteries-included ORM approach in the open-source scaffold.](figures/fig-choice-06-fastapi-over-django.jpg)

*FastAPI's async-native, Pydantic-native design aligns with the scaffold's need for REST and MCP serving without ORM overhead, providing auto-generated OpenAPI docs and SSE streaming for the AG-UI agentic endpoint.*

FastAPI provides async-native request handling, automatic OpenAPI documentation, and native Pydantic integration -- the same models validate API inputs and structure LLM outputs. The scaffold serves routes at `/health`, `/api/v1/attribution`, `/api/v1/permissions`, and `/api/v1/copilotkit`, all benefiting from Starlette's ASGI foundation and SSE streaming for the MCP endpoint.

#### Next.js 15 App Router

![Architecture decision: Next.js 15 App Router selected for music attribution frontend, driven by CopilotKit React dependency for agentic UI, compared against SvelteKit and HTMX alternatives, with server components and streaming SSR enabling transparent confidence display in the open-source attribution scaffold.](figures/fig-choice-07-nextjs-app-router.jpg)

*Next.js 15 with App Router was selected primarily because CopilotKit requires React, providing server components, nested layouts, and streaming SSR for real-time confidence scoring display.*

CopilotKit requires React -- this hard constraint drives the frontend framework choice. Next.js 15 with App Router provides React Server Components, nested layouts, and streaming SSR. All pages live in `frontend/src/app/` (App Router convention), with TypeScript strict mode and Tailwind CSS v4 for styling.

#### Jotai over Redux

![Comparison chart: Jotai atomic state management selected for music attribution frontend over Redux and Zustand, showing minimal two-line atom definitions for theme, role mode, and music credits state with zero boilerplate in the open-source attribution scaffold.](figures/fig-choice-08-jotai-over-redux.jpg)

*Jotai's atomic state model provides minimal-boilerplate state management for three client-side state domains (theme, role mode, works), chosen over Redux's action/reducer ceremony and Zustand's store-based approach for React concurrent compatibility.*

The scaffold has three state domains: theme (light/dark), role mode (artist/query), and works (attribution records). All are client-side with localStorage persistence. Jotai's atom-based approach handles this with two lines per state domain -- define an atom, use it -- versus Redux's 15+ lines of slice/action/reducer ceremony.

#### Tailwind v4 + CSS Custom Properties

![Design token architecture: CSS custom properties flowing through Tailwind v4 utilities for music attribution UI theming, showing zero-hardcoded-hex color tokens for confidence scoring tiers and music credits display, with critical text-var pitfall warning for the open-source attribution scaffold.](figures/fig-choice-09-tailwind-v4-css-properties.jpg)

*CSS custom properties define all design tokens -- confidence tier colors, assurance levels, data source indicators -- consumed via Tailwind v4 utility classes. Critical pitfall: `text-[var(--anything)]` is treated as color in Tailwind v4, not font-size.*

All colors are CSS custom properties in `frontend/src/app/globals.css` -- zero hardcoded hex values in any `.tsx` file. This enables theming via token swap (`:root` vs `.dark` class) while keeping the utility-first developer experience. The warm cream surface (`--color-surface: #f6f3e6`), coral red accent (`--color-accent: #E84C4F`), and confidence tier colors (green/amber/red) are all token-driven. A lint test enforces the no-hardcoded-hex rule.

---

### Development & Operations

#### uv over pip/conda

![Comparison chart: uv package manager selected exclusively for the music attribution scaffold over banned pip and conda, showing 100x faster Rust-based resolution, deterministic lockfiles, and native dependency groups for open-source music metadata project reproducibility.](figures/fig-choice-10-uv-over-pip.jpg)

*The scaffold enforces uv as the sole package manager, completely banning pip and conda for deterministic, fast dependency resolution via Rust-based tooling and a single `pyproject.toml` source of truth.*

uv is the ONLY allowed package manager -- pip and conda are completely banned. uv provides 10-100x faster Rust-based dependency resolution, a deterministic `uv.lock` lockfile, native dependency groups (`[dev]`, `[test]`), and integrated virtual environment management. All configuration lives in `pyproject.toml`, never in `requirements.txt`.

#### tinytag over mutagen

![Trade-off analysis: tinytag BSD-3 license selected over mutagen GPL-2.0 for music metadata extraction in the attribution scaffold, preserving permissive open-source licensing for the music attribution project while providing read-only ID3, FLAC, and MP4 tag support for music credits and ISRC identification.](figures/fig-choice-13-tinytag-over-mutagen.jpg)

*The license-driven decision to use tinytag (BSD-3) over mutagen (GPL-2.0) preserves the scaffold's permissive licensing, trading write capabilities and TIPL credits support for zero-dependency metadata reading of artist, title, album, duration, and ISRC fields (Issue #29).*

This is primarily a license decision. mutagen's GPL-2.0 would force the entire scaffold to be GPL-licensed, conflicting with the open-source research scaffold goal. tinytag (BSD-3, approximately 50KB, zero dependencies) reads standard metadata fields -- title, artist, album, duration, ISRC -- without write capabilities. The acknowledged limitation: no TIPL (credits list) support, which complex data models may eventually need.

#### Observability: PostHog + Sentry

![Architecture decision: PostHog plus Sentry selected for music attribution observability, providing typed product analytics and error tracking for confidence scoring workflows, compared against Datadog, Grafana, and defunct Highlight.io in the open-source attribution scaffold.](figures/fig-choice-14-observability-posthog-sentry.jpg)

*PostHog (product analytics with typed events and feature flags) paired with Sentry (error tracking and performance monitoring) provides cost-effective observability after Highlight.io's shutdown, with separate tools for separate concerns.*

The original plan was Highlight.io (combined analytics + error tracking), but Highlight.io shut down in 2025. The replacement: PostHog for product analytics (typed events in `frontend/src/lib/analytics/events.ts`, feature flags, session replay, 1M free events/month) and Sentry for error tracking (stack traces, issue grouping, release health). Separate tools for separate concerns, both with generous free tiers.

#### Deployment Options

![Corrected cost versus complexity scatter plot showing five deployment paths for the music attribution scaffold: Render (lowest complexity, moderate cost), Hetzner with Ubicloud managed Kubernetes (moderate complexity, low cost), Big Three hyperscalers AWS GCP Azure (moderate complexity, highest cost), and Hetzner bare-metal with self-managed Kubernetes (highest complexity, lowest cost), with a recommended migration arrow from Render to Hetzner plus Ubicloud.](figures/fig-choice-15-deployment-options.jpg)

*The scaffold deploys on Render (approximately 20-35 EUR/month, git push), Hetzner+Ubicloud (approximately 20-60 EUR/month, managed K8s), Big Three (200+ EUR/month, full managed), or Hetzner bare-metal (approximately 7-30 EUR/month, expert ops) -- same Docker image, different operational realities. Recommended path: start on Render, migrate to Hetzner when savings justify the ops burden.*

Five deployment paths on a cost-vs-complexity landscape. Render is the lowest complexity (git push deploy, zero DevOps). Hetzner bare-metal is the cheapest but requires self-managed K8s (Talos/K3s), CloudNativePG, cert-manager, and Ingress NGINX. The recommended migration path: start simple on Render, move to Hetzner+Ubicloud when the savings justify the operational burden. Same code, same Docker image across all five paths.

#### Pulumi over Terraform

![Architecture decision: Pulumi recommended over Terraform for music attribution scaffold infrastructure-as-code, showing Python-native language alignment with the scaffold backend, official MCP server enabling Claude to manage deployments, and Apache 2.0 license versus Terraform's BSL after IBM's HashiCorp acquisition -- compared against OpenTofu fork and no-IaC PaaS options in the open-source attribution platform.](figures/fig-choice-17-pulumi-over-terraform.jpg)

*Pulumi is recommended over Terraform: Python-native IaC (same language as the backend), an official MCP server for Claude-managed deployments, and Apache 2.0 licensing -- while Terraform's BSL after IBM's $6.4B HashiCorp acquisition creates vendor risk (PRD v2.1.0 node: iac_tooling, volatility: shifting).*

Three factors drove the promotion of Pulumi to `recommended` status in PRD v2.1.0: (1) Pulumi uses real Python -- same language as the scaffold backend, infrastructure code lives in the same repo, (2) Pulumi has an official MCP server (`@pulumi/mcp-server`) enabling Claude to manage infrastructure conversationally, (3) Terraform's BSL license after IBM's $6.4B HashiCorp acquisition creates vendor lock-in risk. OpenTofu (MPL-2.0, Linux Foundation fork) remains a viable HCL-compatible alternative.

#### Cloud Sovereignty

![Architecture decision: cloud sovereignty assessment for music attribution scaffold comparing four EU-sovereign providers -- Hetzner (Germany, budget leader), OVHcloud (France, SecNumCloud enterprise), UpCloud (Finland, premium managed services with CISPE certification), and Scaleway (France, GPU and AI focus) -- against US-headquartered providers exposed to the CLOUD Act and FISA Section 702, with four sovereignty tiers mapping MCP consent infrastructure and artist identity data to EU-only hosting requirements in the open-source attribution platform.](figures/fig-choice-18-cloud-sovereignty.jpg)

*Cloud sovereignty for music attribution: EU-sovereign providers (Hetzner, OVHcloud, UpCloud, Scaleway) eliminate CLOUD Act exposure while saving 60-93% versus hyperscalers. The scaffold's Docker architecture makes sovereignty a configuration change -- same container image deploys on any provider.*

Where your cloud provider is headquartered matters more than where your server physically sits. The CLOUD Act (2018) compels US-headquartered companies to provide data to US government regardless of physical storage location -- running AWS in Frankfurt still exposes data to US government access. Four sovereignty tiers map scaffold components to hosting requirements: MCP consent infrastructure and artist identity data (critical/high) require EU-sovereign providers, while frontend and CI/CD (low) can run anywhere.

---

### Permissions & MCP

#### MCP for Permissions

![Decision diagram: MCP as consent infrastructure for music attribution, showing machine-readable AI training permission queries with transparent confidence responses, compared against custom REST API and blockchain approaches for the open-source attribution scaffold enabling attribution-by-design.](figures/fig-choice-11-mcp-permissions.jpg)

*Model Context Protocol (MCP) enables standardized, machine-readable permission queries for AI training consent, allowing AI platforms to programmatically check training rights with confidence-scored responses before use, not after (Teikari 2026, SSRN 6109087).*

This is a core thesis of the companion paper: attribution infrastructure needs machine-readable permission queries so AI platforms can programmatically check training rights. MCP (Model Context Protocol) provides the standardized, agent-native protocol for this. An AI platform queries "Can I train on ISRC X12345?" and receives a structured response with permission status, conditions, and a confidence score tied to the A0-A3 assurance levels. The scaffold's permission routes live at `/api/v1/permissions`.
