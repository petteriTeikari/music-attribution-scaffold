# Probabilistic PRD — 2026 Technology Landscape Report

> **Generated**: 2026-02-10
> **Purpose**: Comprehensive technology options mapped to the probabilistic PRD decision nodes
> **Audience**: Implementation teams evaluating options, portfolio reviewers assessing breadth
> **Scope**: Music attribution MVP + CV-driven development (learning portfolio)

---

## How to Read This Document

This report covers technology options for the 23 decision nodes in [`../prd/decisions/`](../prd/decisions/). L1 business decisions set the context; L2-L5 sections detail specific technology options. For each tool:

- **What it is**: Brief description with 2026 status
- **Pricing**: Current tier/model as of Feb 2026
- **Music attribution fit**: Suitability for entity resolution, knowledge graphs, confidence scoring
- **CV/portfolio value**: Does implementing this demonstrate relevant skills?
- **Prior project experience**: Relevant usage in KusiKasa (uad-copilot — property valuation AI) or DPP agents (digital product passport system)

---

## Table of Contents

### L1: Business Decisions (Root Nodes)

1. [L1: Build vs Buy Posture](#l1-build-vs-buy-posture)
2. [L1: Target Market Segment](#l1-target-market-segment)
3. [L1: Revenue Model](#l1-revenue-model)
4. [L1: Regulatory Posture](#l1-regulatory-posture)

### L2: Architecture Decisions

5. [L2: Data Model Complexity](#l2-data-model-complexity)
6. [L2: API Protocol](#l2-api-protocol)
7. [L2: Service Decomposition](#l2-service-decomposition)
8. [L2: AI Framework Strategy](#l2-ai-framework-strategy)

### L3: Implementation Decisions

9. [L3: Primary Database](#l3-primary-database)
10. [L3: Graph Strategy](#l3-graph-strategy)
11. [L3: Vector Strategy](#l3-vector-strategy)
12. [L3: LLM Provider](#l3-llm-provider)
13. [L3: Frontend Framework](#l3-frontend-framework)
14. [L3: Auth Strategy](#l3-auth-strategy)

### L4: Deployment Decisions

15. [L4: Compute Platform](#l4-compute-platform)
16. [L4: Database Hosting](#l4-database-hosting)
17. [L4: CI/CD Pipeline](#l4-cicd-pipeline)
18. [L4: IaC Tooling](#l4-iac-tooling)
19. [L4: Container Strategy](#l4-container-strategy)

### L5: Operations Decisions

20. [L5: Observability Stack](#l5-observability-stack)
21. [L5: Scaling Strategy](#l5-scaling-strategy)
22. [L5: Backup & DR Strategy](#l5-backup--dr-strategy)
23. [L5: Secrets Management](#l5-secrets-management)

### Cross-Cutting Concerns

24. [Cross-Cutting: Uncertainty Quantification](#cross-cutting-uncertainty-quantification)
25. [Cross-Cutting: Voice/Audio Pipeline](#cross-cutting-voiceaudio-pipeline)
26. [Cross-Cutting: Protocol Landscape](#cross-cutting-protocol-landscape)
27. [Cross-Cutting: Python Web Frameworks](#cross-cutting-python-web-frameworks)
28. [Cross-Cutting: Graph RAG](#cross-cutting-graph-rag)
29. [Cross-Cutting: Entity Resolution](#cross-cutting-entity-resolution)

### Music-Specific Tools (Domain-Critical)

30. [Music: Audio Fingerprinting](#music-audio-fingerprinting)
31. [Music: Industry APIs & Data Sources](#music-industry-apis--data-sources)
32. [Music: Metadata Standards & Identifiers](#music-metadata-standards--identifiers)
33. [Music: Audio Analysis Libraries](#music-audio-analysis-libraries)
34. [Music: Python Metadata Libraries](#music-python-metadata-libraries)

### Supporting Infrastructure

35. [Python Development Toolchain](#python-development-toolchain)
36. [Embedding Models](#embedding-models)
37. [Full-Text Search](#full-text-search)
38. [Task Queues & Background Processing](#task-queues--background-processing)
39. [Caching: Redis & Alternatives](#caching-redis--alternatives)
40. [Data Quality & Validation](#data-quality--validation)
41. [Database Migrations](#database-migrations)
42. [Object Storage](#object-storage)
43. [Content Provenance (C2PA)](#content-provenance-c2pa)
44. [Documentation Tools](#documentation-tools)

### Synthesis

45. [Recommended MVP Stack](#recommended-mvp-stack)
46. [Technology Volatility Watch](#technology-volatility-watch-next-review-may-2026)

---

## L1: Build vs Buy Posture

> Decision node: [`../prd/decisions/L1-business/build-vs-buy-posture.decision.yaml`](../prd/decisions/L1-business/build-vs-buy-posture.decision.yaml)

The root decision that cascades through all downstream choices. Options:

| Option | Prior | Description | Downstream Impact |
|--------|-------|-------------|-------------------|
| **Custom Build** | 0.40 | Full control, PostgreSQL + custom code | Enables AGE, pgvector, Pulumi, full observability |
| **Managed Services** | 0.35 | Mix of custom + managed (Supabase, Neon) | Balances control with operational simplicity |
| **SaaS Maximalist** | 0.25 | Minimize custom code, maximize platforms | Supabase-everything, no IaC, minimal ops |

This is the strongest predictor of L3 (database, auth) and L4 (compute, IaC) decisions.

---

## L1: Target Market Segment

> Decision node: [`../prd/decisions/L1-business/target-market-segment.decision.yaml`](../prd/decisions/L1-business/target-market-segment.decision.yaml)

| Option | Prior | Description | Downstream Impact |
|--------|-------|-------------|-------------------|
| **Independent Artists** | 0.35 | Individual musicians, small catalogs | Chat-first UX, simple onboarding |
| **Labels & Publishers** | 0.30 | Catalog managers, bulk operations | DDEX integration, batch processing, admin UI |
| **AI Platforms** | 0.20 | API consumers (training consent queries) | MCP-first, API-key auth, no frontend |
| **Rights Organizations** | 0.15 | PROs, CMOs | Enterprise auth, audit logging, compliance |

Drives API protocol choice (REST vs MCP vs GraphQL), frontend necessity, and auth complexity.

---

## L1: Revenue Model

> Decision node: [`../prd/decisions/L1-business/revenue-model.decision.yaml`](../prd/decisions/L1-business/revenue-model.decision.yaml)

| Option | Prior | Description |
|--------|-------|-------------|
| **API Usage-Based** | 0.35 | Pay-per-query (attribution lookups, consent checks) |
| **SaaS Subscription** | 0.30 | Monthly plans for artists/labels |
| **Data Licensing** | 0.20 | License curated attribution datasets |
| **Open Core** | 0.15 | Free tier + premium features |

Revenue model influences infrastructure scaling strategy and multi-tenancy requirements.

---

## L1: Regulatory Posture

> Decision node: [`../prd/decisions/L1-business/regulatory-posture.decision.yaml`](../prd/decisions/L1-business/regulatory-posture.decision.yaml)

| Option | Prior | Description | Downstream Impact |
|--------|-------|-------------|-------------------|
| **Compliance-First** | 0.30 | EU AI Act, GDPR-ready from day one | Audit logging, data residency, consent management |
| **Best Effort** | 0.45 | Address compliance as needed | Simpler MVP, regulatory debt |
| **Minimal** | 0.25 | Focus on product, defer compliance | Fastest MVP, highest regulatory risk |

For DPP traceability domain overlay, compliance-first probability increases by +0.20 (EU ESPR mandate).

---

## L2: Data Model Complexity

> Decision node: [`../prd/decisions/L2-architecture/data-model-complexity.decision.yaml`](../prd/decisions/L2-architecture/data-model-complexity.decision.yaml)

| Option | Prior | Description | Downstream Impact |
|--------|-------|-------------|-------------------|
| **Graph-Enriched Relational** | 0.45 | PostgreSQL + Apache AGE for graph traversals | Requires graph strategy decision |
| **Pure Relational** | 0.30 | Standard SQL, joins for relationships | Simplest; limits attribution network queries |
| **Multi-Model** | 0.15 | Separate stores (relational + graph + vector) | Maximum capability, maximum ops complexity |
| **Document-Centric** | 0.10 | MongoDB-style flexible schemas | Poor fit for attribution relationships |

Strongly determines graph strategy and primary database choice.

---

## L2: API Protocol

> Decision node: [`../prd/decisions/L2-architecture/api-protocol.decision.yaml`](../prd/decisions/L2-architecture/api-protocol.decision.yaml)

| Option | Prior | Description | Music Attribution Fit |
|--------|-------|-------------|----------------------|
| **MCP Primary** | 0.35 | Model Context Protocol as main interface | Core for AI platform integration (consent queries) |
| **REST + MCP** | 0.30 | REST for humans, MCP for AI agents | Covers both artist-facing and AI-facing use cases |
| **GraphQL** | 0.20 | Flexible queries for complex attribution graphs | Good for frontend; overkill for simple consent API |
| **REST Only** | 0.15 | Traditional REST API | Simplest; misses AI platform opportunity |

MCP is the differentiator — it enables AI platforms to query attribution and consent data directly.

---

## L2: Service Decomposition

> Decision node: [`../prd/decisions/L2-architecture/service-decomposition.decision.yaml`](../prd/decisions/L2-architecture/service-decomposition.decision.yaml)

| Option | Prior | Description | Downstream Impact |
|--------|-------|-------------|-------------------|
| **Modular Monolith** | 0.45 | Single deployment, internal module boundaries | Simplest deployment; recommended for MVP |
| **API + Workers** | 0.30 | FastAPI server + background task workers | Good for async attribution resolution |
| **Microservices** | 0.15 | Independent services per domain | Enterprise-scale; requires K8s or equivalent |
| **Serverless** | 0.10 | Function-based (Lambda, Edge Functions) | Cold starts problematic for graph queries |

Strongly influences compute platform and container strategy choices.

---

## L3: Primary Database

> Decision node: [`../prd/decisions/L3-implementation/primary-database.decision.yaml`](../prd/decisions/L3-implementation/primary-database.decision.yaml)

### PostgreSQL 18 (Released Sep 2025)

| Aspect | Details |
|--------|---------|
| **Version** | PostgreSQL 18 (GA Sep 2025) |
| **Key 2026 features** | Asynchronous I/O (io_uring — up to 3x faster scans), UUIDv7 native (`uuidv7()` function), virtual generated columns (compute-on-read), OAuth authentication |
| **Music attribution fit** | Excellent — unified relational + pgvector + Apache AGE in one process |
| **CV value** | High — PostgreSQL expertise is universally valued |
| **Prior experience** | KusiKasa: Cloud SQL PostgreSQL; DPP: PostgreSQL + pgvector |

**Key insight**: PostgreSQL 18's UUIDv7 is ideal for attribution records — sortable, timestamp-ordered, no external UUID library needed. AIO with io_uring delivers significant performance gains for sequential scans of large attribution tables.

### Supabase

| Aspect | Details |
|--------|---------|
| **Pricing** | Free (2 projects, 500MB), Pro ($25/mo, 8GB), Team ($599/mo) |
| **Key 2026 features** | Edge Functions (Deno runtime with V8 isolates), built-in Auth, Realtime (Broadcast + Presence + Postgres Changes), pgvector support |
| **Music attribution fit** | Good for MVP — built-in auth, realtime for live attribution updates, REST/GraphQL auto-generated |
| **Constraints** | Limited extension support (pgvector yes, Apache AGE unclear), Supabase-specific features create lock-in |
| **CV value** | Medium — demonstrates rapid prototyping skills |

### SQLite / Turso (libSQL)

| Aspect | Details |
|--------|---------|
| **Pricing** | Turso: Free (500 DBs, 9GB), Scaler ($29/mo), Pro ($99/mo) |
| **Key 2026 features** | Rust rewrite with DiskANN vector indexes, edge replication, embedded-first |
| **Music attribution fit** | Limited — no graph queries, vector via DiskANN is new/experimental |
| **CV value** | Medium — demonstrates edge-first and embedded DB skills |

### CockroachDB

| Aspect | Details |
|--------|---------|
| **Pricing** | Serverless: Free (10GB, 50M RUs), Dedicated: from $295/mo |
| **Key 2026 features** | Distributed SQL, multi-region, PostgreSQL wire compatibility |
| **Music attribution fit** | Overkill for MVP — relevant only at enterprise/global scale |
| **CV value** | High — demonstrates distributed systems knowledge |

### DuckDB + MotherDuck (Analytics Companion)

| Aspect | Details |
|--------|---------|
| **Pricing** | DuckDB: Free/open-source; MotherDuck: Free (10GB), Pro ($35/mo) |
| **Key 2026 features** | In-process OLAP, Parquet/CSV native, excellent for analytics queries |
| **Music attribution fit** | Complementary — batch analytics on attribution data, not primary store |
| **CV value** | High — modern analytics skill, increasingly demanded |

### SurrealDB (Experimental)

| Aspect | Details |
|--------|---------|
| **Status** | v2.x, multi-model (document + graph + relational + vector) |
| **Music attribution fit** | Interesting but immature — single DB for all data models |
| **CV value** | Medium — shows awareness of multi-model databases |
| **Risk** | Pre-production maturity for critical workloads |

---

## L3: Graph Strategy

> Decision node: [`../prd/decisions/L3-implementation/graph-strategy.decision.yaml`](../prd/decisions/L3-implementation/graph-strategy.decision.yaml)

### Apache AGE (PostgreSQL Extension)

| Aspect | Details |
|--------|---------|
| **Status** | Apache Incubator → Top-Level Project trajectory, openCypher support |
| **Music attribution fit** | Ideal — artist-credit-track-release-label traversals within PostgreSQL |
| **Prior experience** | Referenced in DPP agents as future GraphRAG path |
| **CV value** | High — graph queries on PostgreSQL is a differentiating skill |

### Neo4j

| Aspect | Details |
|--------|---------|
| **Pricing** | Community (free, GPLv3), Aura Free (1 instance), Aura Pro ($65/mo+) |
| **Status** | Rejected in REJECTED.md but viable for enterprise |
| **Music attribution fit** | Maximum graph capability but operational overhead |
| **CV value** | High — Neo4j/Cypher experience is highly valued |
| **Prior experience** | KusiKasa: Used for knowledge graphs (comps) |

### FalkorDB

| Aspect | Details |
|--------|---------|
| **Status** | Redis-compatible graph database, openCypher |
| **Music attribution fit** | Lightweight graph queries, fast for small-medium graphs |
| **CV value** | Medium — newer, less recognized |

### Memgraph

| Aspect | Details |
|--------|---------|
| **Status** | In-memory graph DB, Cypher compatible, streaming-friendly |
| **Music attribution fit** | Good for real-time attribution updates |
| **CV value** | Medium — shows awareness of streaming graph processing |

### NetworkX (Application-Layer)

| Aspect | Details |
|--------|---------|
| **Status** | Python standard for graph analysis |
| **Music attribution fit** | Good for batch analysis, confidence propagation, visualization |
| **Prior experience** | DPP agents: Graph feature engineering (betweenness_centrality, clustering) |
| **CV value** | Medium — well-known, not differentiating |

---

## L3: Vector Strategy

> Decision node: [`../prd/decisions/L3-implementation/vector-strategy.decision.yaml`](../prd/decisions/L3-implementation/vector-strategy.decision.yaml)

### pgvector (PostgreSQL Extension)

| Aspect | Details |
|--------|---------|
| **Version** | 0.8.0+ (2026) |
| **Key features** | HNSW indexes, IVFFlat, quantization, improved performance |
| **Music attribution fit** | Entity resolution (matching "John Lennon" across sources), semantic search |
| **Prior experience** | KusiKasa: pgvector; DPP: PostgreSQL + pgvector |
| **CV value** | High — unified stack skill |

### Qdrant

| Aspect | Details |
|--------|---------|
| **Pricing** | Open-source (self-hosted), Cloud: Free (1GB), from $25/mo |
| **Key features** | Rust-based, payload filtering, hybrid search, multitenancy |
| **Music attribution fit** | Excellent at scale (>1M vectors), good for large music catalogs |
| **Prior experience** | KusiKasa: Planned production VDB; DPP: Planned Qdrant migration |
| **CV value** | High — Rust-based, production-grade vector DB |

### Weaviate

| Aspect | Details |
|--------|---------|
| **Status** | Rejected in REJECTED.md (separate service unnecessary for <10M vectors) |
| **Pricing** | Open-source, Cloud: Sandbox (free), Standard ($25/mo+) |
| **Key features** | Multi-modal search, generative search, hybrid BM25+vector |
| **Music attribution fit** | Multi-modal interesting for album art + metadata search |
| **CV value** | Medium — less differentiated from Qdrant |

### Milvus / Zilliz Cloud

| Aspect | Details |
|--------|---------|
| **Pricing** | Zilliz: $99/mo dedicated, $4/M vCUs serverless, storage $0.04/GB/mo |
| **Key features** | Milvus 2.6.x: JSON shredding (100x faster metadata filtering), 7x faster full-text search than Elasticsearch, 87% lower storage costs |
| **Music attribution fit** | Enterprise-scale; metadata filtering is excellent for attribution queries |
| **CV value** | High — demonstrates large-scale vector infrastructure knowledge |

### Chroma

| Aspect | Details |
|--------|---------|
| **Pricing** | Cloud: $100 credits, then usage-based; open-source free |
| **Key features** | Rust rewrite (4x faster), serverless cloud, hybrid + full-text search |
| **Music attribution fit** | Good for prototyping, lightweight development |
| **Prior experience** | DPP: Used for demo/prototyping phase |
| **CV value** | Low — primarily a prototyping tool |

### LanceDB (Emerging)

| Aspect | Details |
|--------|---------|
| **Status** | Embedded vector DB built on Lance columnar format |
| **Music attribution fit** | Interesting for edge/embedded use cases |
| **CV value** | Medium — emerging, differentiating if it gains traction |

### Pinecone

| Aspect | Details |
|--------|---------|
| **Pricing** | Storage $0.33/GB/mo, RUs $16-24/M, Dedicated Read Nodes available |
| **Status** | Rejected in REJECTED.md (separate service unnecessary) |
| **Music attribution fit** | Good but separate service adds complexity |
| **CV value** | Medium — well-known but not differentiating |

---

## L3: LLM Provider

> Decision node: [`../prd/decisions/L3-implementation/llm-provider.decision.yaml`](../prd/decisions/L3-implementation/llm-provider.decision.yaml)

### Anthropic (Claude) — Feb 2026

| Model | Input/Output per M tokens | Context | Key Capability |
|-------|---------------------------|---------|----------------|
| **Opus 4.6** | $5 / $25 | 1M tokens, 128K output | Best agentic coding (65.4% Terminal-Bench), 84% BrowseComp, adaptive thinking |
| **Sonnet 4.5** | $3 / $15 | 200K (1M with beta header) | 77.2% SWE-bench, 30hr+ autonomous operation |
| **Haiku 4.5** | $1 / $5 | 200K, 64K output | 73.3% SWE-bench, extended thinking, 4-5x faster than Sonnet |

**Music attribution fit**: Claude excels at structured output extraction (Pydantic models), MCP-native integration, long context for processing full album metadata. Batch API gives 50% output discount.

**CV value**: Very high — demonstrates cutting-edge AI integration.

**Prior experience**: DPP: Claude Haiku via OpenRouter for voice, Claude Opus for evaluation/judge.

### OpenAI (GPT) — Feb 2026

| Model | Input/Output per M tokens | Key Capability |
|-------|---------------------------|----------------|
| **GPT-5.2** | ~$1.25 / $5 (estimated) | Within 0.7 points of Opus on Terminal-Bench |
| **GPT-4o** | $2.50 / $10 | Mature function calling, Assistants API |
| **GPT-4o-mini** | $0.15 / $0.60 | Cost-effective for simple tasks |

### Google (Gemini) — Feb 2026

| Model | Key Capability |
|-------|----------------|
| **Gemini 3 Pro** | 2M token native context (largest), leads visual reasoning (MMMU Pro) |
| **Gemini 2.5 Flash** | Cost-effective, long context |

### Open Source — Feb 2026

| Model | Parameters | Key Capability |
|-------|-----------|----------------|
| **Llama 4** | Various | Meta's latest; strong coding and reasoning |
| **DeepSeek V3/R1** | 671B MoE | Cost-effective reasoning; Chinese-developed |
| **Qwen 3** | Various | Strong multilingual; Alibaba |
| **Mistral Large** | Various | EU-based; GDPR-friendly |

### Multi-Provider Routing Strategy (from DPP agents)

The DPP agents project demonstrated a powerful multi-tier LLM routing approach:

| Tier | Model | Cost/1M | Use Case |
|------|-------|---------|----------|
| Classification | SmolLM2-1.7B | Free (HuggingFace) | Route queries |
| Simple (60%) | Llama 3.1 8B | $0.04 | FAQ, simple lookups |
| Reasoning (30%) | Qwen 2.5 7B | $0.06 | Moderate complexity |
| Complex (9%) | Claude Haiku 4.5 | $0.25 | Attribution reasoning |
| Frontier (1%) | Claude Sonnet 4.5 | $3.00 | Complex gap-filling |
| Judge | Claude Opus 4.6 | $5.00 | Evaluation, calibration |

**Result**: ~$0.70/month for 10K queries vs $35+/month with all-frontier models.

---

## L2: AI Framework Strategy

> Decision node: [`../prd/decisions/L2-architecture/ai-framework-strategy.decision.yaml`](../prd/decisions/L2-architecture/ai-framework-strategy.decision.yaml)

### Direct API + Pydantic (Recommended)

Direct LLM API calls with Pydantic models for structured output. Maximum debuggability. The music attribution manuscript explicitly cautions against over-abstraction.

### PydanticAI (Production-Stable as of Feb 2026)

| Aspect | Details |
|--------|---------|
| **Status** | v1.0+ released Feb 6, 2026 — "Production/Stable" |
| **Key features** | Durable execution, graph support, MCP integration, A2A integration, model-agnostic, type-safe |
| **Music attribution fit** | Excellent — structured output for attribution records, durable agents for long-running resolution |
| **CV value** | Very high — newest production framework, demonstrates early adoption |

**Key insight**: PydanticAI bridges the gap between "direct API" and "orchestration framework" — it's the lightweight SDK option with production-grade features including durable execution and graph support.

### Instructor

| Aspect | Details |
|--------|---------|
| **Status** | Stable, widely adopted |
| **Key features** | Structured output extraction, retry logic, validation |
| **Music attribution fit** | Good for metadata extraction from unstructured text |
| **CV value** | Medium — well-known, practical |

### LangGraph

| Aspect | Details |
|--------|---------|
| **Status** | Leading agent framework in benchmarks |
| **Key features** | State machine for multi-step agent workflows, persistence, human-in-the-loop |
| **Music attribution fit** | Good for complex attribution pipelines (multi-source resolution) |
| **Prior experience** | KusiKasa: Used for conversation agent management |
| **CV value** | High — leading agent orchestration framework |
| **Caveat** | LangChain ecosystem remains rejected per REJECTED.md; LangGraph is more focused |

### Claude Agent SDK / OpenAI Agents SDK / Google ADK

All three cloud providers now have native agent SDKs. These are thin wrappers around their respective APIs with tool use, conversation management, and structured output.

| SDK | Provider | Key Feature |
|-----|----------|-------------|
| Claude Agent SDK | Anthropic | MCP-native, computer use |
| OpenAI Agents SDK | OpenAI | Assistants API, code interpreter |
| Google ADK | Google | A2A-native, Vertex AI integration |

### DSPy

| Aspect | Details |
|--------|---------|
| **Status** | Research → production transition |
| **Key features** | Programmatic LLM optimization, prompt compilation |
| **Music attribution fit** | Interesting for optimizing entity resolution prompts |
| **CV value** | High — demonstrates ML-for-ML optimization thinking |

### LlamaIndex (Rejected — see REJECTED.md)

| Aspect | Details |
|--------|---------|
| **Status** | NOT RECOMMENDED — same over-abstraction concerns as LangChain |
| **Key features** | Data connectors, indexing, RAG pipeline orchestration |
| **When to reconsider** | If many pre-built data connectors needed for diverse music sources |

---

## L3: Frontend Framework

> Decision node: [`../prd/decisions/L3-implementation/frontend-framework.decision.yaml`](../prd/decisions/L3-implementation/frontend-framework.decision.yaml)

### Next.js 15+ (React)

| Aspect | Details |
|--------|---------|
| **Status** | Dominant React meta-framework |
| **Key 2026 features** | App Router stable, React Server Components, Turbopack |
| **Music attribution fit** | Chat interface, album workflow UI, admin dashboards |
| **CV value** | High — largest ecosystem, most hiring demand |

### SvelteKit 2+ (Svelte 5)

| Aspect | Details |
|--------|---------|
| **Status** | Growing adoption, Svelte 5 runes |
| **Key 2026 features** | Fine-grained reactivity, smaller bundles, simpler reactive model |
| **Music attribution fit** | Good for responsive attribution review UI |
| **CV value** | High — demonstrates awareness of React alternatives |

### HTMX + Jinja (Python-First)

| Aspect | Details |
|--------|---------|
| **Status** | HTMX 2.0, growing Python ecosystem (FastHTML, PyHAT stack) |
| **Key 2026 features** | Server-rendered HTML, minimal JavaScript, works with FastAPI |
| **Music attribution fit** | Ideal for CRUD admin interfaces; limited for rich chat UIs |
| **CV value** | High for Python devs — demonstrates Python-first full-stack |

### Astro 5 (Content-First)

| Aspect | Details |
|--------|---------|
| **Status** | Content-first, Islands Architecture |
| **Key features** | Zero JS by default, any component library (React/Svelte/Vue/Solid) |
| **Music attribution fit** | Good for public attribution explorer; less for interactive chat |
| **CV value** | Medium — niche but growing |

### React Router 7 (Remix)

| Aspect | Details |
|--------|---------|
| **Status** | Remix unified with React Router v7 |
| **Key features** | Single Fetch, progressive enhancement, form handling |
| **Music attribution fit** | Good for data-heavy attribution workflows |

### Chat-Specific UI Libraries

| Library | Description |
|---------|-------------|
| **Vercel AI SDK** | React hooks for chat/streaming, model-agnostic |
| **CopilotKit** | AI copilot components for React |
| **shadcn/ui** | Tailwind-based components, copy-paste architecture |
| **Radix** | Headless UI primitives |

### CSS Styling (2026)

| Tool | Status |
|------|--------|
| **Tailwind CSS 4** | `@theme` directive, `@utility` directive, faster engine |
| **Panda CSS** | Build-time CSS-in-JS, type-safe, RSC compatible |
| **StyleX** | Meta's zero-runtime CSS-in-JS, 2026 roadmap: better ergonomics |

---

## L3: Auth Strategy

> Decision node: [`../prd/decisions/L3-implementation/auth-strategy.decision.yaml`](../prd/decisions/L3-implementation/auth-strategy.decision.yaml)

### Managed Auth Services

| Service | Pricing | Key Features |
|---------|---------|--------------|
| **Clerk** | Free (10K MAU), Pro ($25/mo) | Best DX, React/Next.js native, organizations |
| **WorkOS** | Free (1M MAU!), paid for SSO | Enterprise SSO focus, generous free tier |
| **Stytch** | Free (25K users) | Passwordless, B2B auth, flexible |
| **Auth0** | Free (25K MAU) | Mature, enterprise features |
| **Supabase Auth** | Included with Supabase | Row-level security, social logins, magic links |

### Self-Hosted Auth

| Library | Status |
|---------|--------|
| **Better Auth** | Absorbed Auth.js (formerly NextAuth); actively maintained |
| **Lucia Auth** | Archived — evolved to educational project |
| **Auth.js v5** | Now maintained by Better Auth team; still in beta |

**Key insight**: Auth.js (NextAuth) v5 is now maintained by Better Auth. For Python backends, no equivalent to Better Auth exists — use managed services or implement JWT with FastAPI security utilities.

---

## L4: Compute Platform

> Decision node: [`../prd/decisions/L4-deployment/compute-platform.decision.yaml`](../prd/decisions/L4-deployment/compute-platform.decision.yaml)

### Platform Comparison (Feb 2026)

| Platform | Free Tier | Paid Starting | Python Support | Database Addons |
|----------|-----------|---------------|----------------|-----------------|
| **Render** | Static sites, limited compute | $7/mo (Individual) | Docker, native Python | Managed PostgreSQL |
| **Railway** | $5 credit/mo | Usage-based (~$5/mo min) | Docker, native buildpacks | Managed PostgreSQL |
| **Fly.io** | 3 shared VMs, 1GB volumes | ~$2/mo per machine | Docker, Firecracker microVMs | Tigris (S3), LiteFS |
| **Vercel** | Generous for frontend | $20/mo Pro | Serverless Functions, limited | Vercel Postgres (Neon) |
| **Hetzner Cloud** | None | €3.29/mo (CX22) | Full VM, any stack | None (self-managed) |
| **AWS ECS** | Free tier (12mo) | ~$30/mo+ | Full container orchestration | RDS, Aurora, etc. |

### Self-Hosted PaaS (on Hetzner)

| Tool | Pricing | Key Features |
|------|---------|--------------|
| **Coolify** | Cloud: $5/mo (2 servers) + server costs; Self-hosted: free | Git-push deploy, Docker support, auto-SSL, real-time terminal |
| **Dokku** | Free (self-hosted) | Heroku-like on single server, buildpacks |
| **CapRover** | Free (self-hosted) | Docker-based, one-click apps, Let's Encrypt |

**Key insight**: Hetzner + Coolify = self-hosted PaaS at ~$15/mo total (Coolify $5 + Hetzner CX22 $3.29 + bigger server $10). This is 80% cheaper than equivalent PaaS services.

**Prior experience**: DPP agents: Hetzner CPX21 at ~€9/mo with FastAPI + PostgreSQL; 30% savings over Azure.

---

## L4: Database Hosting

> Decision node: [`../prd/decisions/L4-deployment/database-hosting.decision.yaml`](../prd/decisions/L4-deployment/database-hosting.decision.yaml)

| Provider | PostgreSQL Support | pgvector | Pricing | Notes |
|----------|-------------------|----------|---------|-------|
| **Neon** | Serverless PostgreSQL, branching | Yes | Free (0.5GB), Launch ($19/mo), Scale ($69/mo) | Acquired by Databricks; scale-to-zero, branching for dev/test |
| **Supabase** | Managed PostgreSQL | Yes | Free (500MB), Pro ($25/mo), Team ($599/mo) | Built-in Auth, Realtime, Edge Functions |
| **Ubicloud on Hetzner** | Managed PostgreSQL on Hetzner | Likely | From $12/mo | 10x value vs AWS RDS |
| **AWS RDS** | Managed PostgreSQL | Yes | ~$15/mo+ (db.t4g.micro) | Enterprise-grade, multi-AZ |
| **Hetzner self-managed** | Self-hosted PostgreSQL | Yes (install extension) | $0 (on existing VPS) | Full control, full responsibility |

**Note**: Hetzner does not offer native managed PostgreSQL. Third-party services like Ubicloud provide managed PostgreSQL on Hetzner infrastructure.

---

## L4: CI/CD Pipeline

> Decision node: [`../prd/decisions/L4-deployment/ci-cd-pipeline.decision.yaml`](../prd/decisions/L4-deployment/ci-cd-pipeline.decision.yaml)

### GitHub Actions (2026 Pricing Update)

| Aspect | Details |
|--------|---------|
| **Key change** | 40% price reduction on hosted runners + $0.002/min platform charge (Jan 2026) |
| **Impact** | 96% of customers see no change; public repos remain free |
| **Self-hosted** | Now consume usage quota (March 2026) with $0.002/min platform fee |

### Build Acceleration

| Tool | Key Feature | Pricing |
|------|-------------|---------|
| **Depot** | Remote Docker builds (40x faster), NVMe cache, OIDC auth | Startup plan includes 5K build + 20K Actions minutes |
| **Earthly** | Reproducible builds, Dockerfile-like syntax | Open-source + paid cloud |
| **Dagger** | Programmable CI/CD pipelines in Python/Go/TypeScript | Open-source |

---

## L4: IaC Tooling

> Decision node: [`../prd/decisions/L4-deployment/iac-tooling.decision.yaml`](../prd/decisions/L4-deployment/iac-tooling.decision.yaml)

| Tool | Language | Key 2026 Feature | Music Attribution Fit |
|------|----------|-----------------|----------------------|
| **None (Platform-Native)** | N/A | Use PaaS deploy buttons (Render, Railway) | Solo hacker — skip IaC entirely |
| **OpenTofu** | HCL | State encryption (AES-GCM, AWS/GCP KMS) — big advantage over Terraform | Production — open-source, no BSL |
| **Pulumi** | Python, TypeScript, Go | Native Python IaC; CrossGuard policy-as-code | Engineer-heavy — Python-native IaC |
| **Terraform** | HCL | BSL license (reason for OpenTofu fork) | Legacy — prefer OpenTofu |
| **SST (Serverless Stack)** | TypeScript | AWS-focused, full-stack deployment | Only if serverless architecture |

**Prior experience**: KusiKasa: Pulumi for GCP infrastructure.

---

## L4: Container Strategy

> Decision node: [`../prd/decisions/L4-deployment/container-strategy.decision.yaml`](../prd/decisions/L4-deployment/container-strategy.decision.yaml)

| Option | Description | Music Attribution Fit |
|--------|-------------|----------------------|
| **Docker Compose** | Multi-container local dev; single-server production | Recommended for MVP — PostgreSQL + FastAPI + worker |
| **Docker (Single Container)** | Single Dockerfile, platform-deployed | Simplest; works with Render, Railway, Fly.io |
| **Kubernetes** | Container orchestration at scale | Rejected per REJECTED.md unless >10 services |
| **No Containers** | Direct process deployment (PaaS buildpacks) | Solo hacker — Railway/Render buildpacks |

**Recommendation**: Docker Compose for local development (PostgreSQL + pgvector + AGE + FastAPI), single Docker container for PaaS deployment. Avoid K8s until justified by scale.

---

## L5: Observability Stack

> Decision node: [`../prd/decisions/L5-operations/observability-stack.decision.yaml`](../prd/decisions/L5-operations/observability-stack.decision.yaml)

### LLM-Specific Observability

| Tool | Key Features | Pricing |
|------|-------------|---------|
| **Langfuse** | Open-source LLM tracing, prompt management, evals, OTEL-native SDK v3, 50+ integrations | Self-hosted free; Cloud free tier available |
| **Braintrust** | LLM-as-Judge, heuristics, production evals | Free tier + usage-based |
| **Phoenix/Arize** | LLM observability, hallucination detection | Open-source + paid |

**Prior experience**: DPP agents: Langfuse for LLM tracing and cost attribution. KusiKasa: Braintrust for LLM evals.

### System Observability

| Tool | Key Features | Pricing |
|------|-------------|---------|
| **Grafana Stack** | Prometheus + Loki + Tempo, open-source, Grafana Cloud free tier | Self-hosted free; Cloud from $0 |
| **Datadog** | Enterprise APM, logs, metrics | $15-30/host/mo |
| **Better Stack** | Uptime monitoring, log management | Free tier + $24/mo |
| **Sentry** | Error tracking, performance monitoring, session replay; Python SDK | Free (5K errors/mo), Team $26/mo |

**Note**: Sentry is near-universal for Python web backends (FastAPI integration). Consider it orthogonal to the LLM observability decision — most stacks use both Langfuse (LLM) + Sentry (errors).

---

## L5: Scaling Strategy

> Decision node: [`../prd/decisions/L5-operations/scaling-strategy.decision.yaml`](../prd/decisions/L5-operations/scaling-strategy.decision.yaml)

| Option | Description | Music Attribution Fit |
|--------|-------------|----------------------|
| **Vertical Scaling** | Bigger server (Hetzner CX32 → CX52) | Simplest; handles 10K+ users on single server |
| **Horizontal (PaaS-Managed)** | Auto-scaling via Render/Railway | No infrastructure management; limited control |
| **Horizontal (Container Orchestrated)** | Multiple instances behind load balancer | For enterprise; requires K8s or ECS |
| **Database Read Replicas** | Primary + read replicas for query load | Neon supports read replicas on Scale plan |

**Recommendation**: Vertical scaling for MVP (Hetzner CAX21 ARM: excellent price/performance), add Neon read replicas when query load requires it.

---

## L5: Backup & DR Strategy

> Decision node: [`../prd/decisions/L5-operations/backup-dr-strategy.decision.yaml`](../prd/decisions/L5-operations/backup-dr-strategy.decision.yaml)

| Option | Description | Music Attribution Fit |
|--------|-------------|----------------------|
| **Provider-Managed** | Neon PITR (point-in-time recovery), Supabase daily backups | Simplest; recommended for MVP |
| **Custom + Provider** | pg_dump scripts + provider backups | Belt-and-suspenders approach |
| **Multi-Region Replication** | Cross-region database replication | Enterprise; CockroachDB or Aurora use case |
| **Self-Managed** | pgBackRest, WAL-G on self-hosted PostgreSQL | Full control; Hetzner archetype |

**Key consideration**: Attribution data is high-value (incorrect credits cause royalty misrouting). Even MVP should have PITR capability.

---

## L5: Secrets Management

> Decision node: [`../prd/decisions/L5-operations/secrets-management.decision.yaml`](../prd/decisions/L5-operations/secrets-management.decision.yaml)
>
> **Note**: This decision node is declared in `_network.yaml` but the `.decision.yaml` file has not yet been created.

| Tool | Key Features | Pricing |
|------|-------------|---------|
| **Environment Variables** | Simplest approach; platform-managed (.env, Render/Railway secrets) | Free |
| **Infisical** | Open-source secrets management, CLI, SDK, env sync | Free (5 users), paid $8/user/mo |
| **Doppler** | Universal secrets platform, env sync, rotation | Free (5 users), paid $6/user/mo |
| **1Password CLI** | Developer secrets, SSH keys, env injection | Included with 1Password subscription |
| **SOPS** | File-based encryption (age, KMS), Git-friendly | Free (open-source) |

---

## Cross-Cutting: Uncertainty Quantification

> Related PRDs: [`../prd/uncertainty/toc-uncertainty.md`](../prd/uncertainty/toc-uncertainty.md)

### Libraries for Conformal Prediction

| Library | Key Features | Music Attribution Fit |
|---------|-------------|----------------------|
| **MAPIE** | Scikit-learn compatible conformal prediction, calibrated intervals | Primary choice — "90% confident" must mean 90% accurate |
| **pgmpy** | Probabilistic graphical models, Bayesian networks | Bayesian updating across knowledge graphs |
| **Fortuna** | AWS uncertainty quantification library | Research-grade alternative |

**Prior experience**: KusiKasa: Conformal Prediction with MAPIE. DPP: M-GAM + MAPIE, pgmpy for Bayesian multi-signal integration.

### UQ Research Landscape (2026)

Active research area with KDD 2025 tutorial on "Uncertainty Quantification and Confidence Calibration in LLMs" covering:
- Token-level entropy for LLM uncertainty
- Sampling-based consistency methods
- Supervised uncertainty estimation from hidden activations
- Confidence elicitation frameworks

---

## Cross-Cutting: Voice/Audio Pipeline

> Related PRD: [`../prd/voice-agent/toc-voice-agent.md`](../prd/voice-agent/toc-voice-agent.md)

| Component | Primary | Alternative | Pricing |
|-----------|---------|-------------|---------|
| **Voice Platform** | Vapi | Pipecat (self-hosted), LiveKit | Vapi: $0.05/min |
| **STT** | Deepgram Nova-2 | AssemblyAI, Whisper | Deepgram: $0.0043/min |
| **TTS** | Inworld | ElevenLabs (6x more expensive), Cartesia | Inworld: $5/1M chars |

**Prior experience**: DPP agents: Full Vapi → Pipecat migration path documented. Cost analysis: $0.12/conversation (Vapi) → $0.02/conversation (Pipecat at scale).

---

## Cross-Cutting: Protocol Landscape

> Related PRD: [`../prd/mcp-server/toc-mcp-server.md`](../prd/mcp-server/toc-mcp-server.md)

### Agent Communication Protocols (Feb 2026)

| Protocol | Provider | Purpose | Maturity |
|----------|----------|---------|----------|
| **MCP** | Anthropic | Agent ↔ Tool communication | Most mature; growing server ecosystem |
| **A2A** | Google/Linux Foundation | Agent ↔ Agent coordination | Growing; Agent Cards for discovery |
| **ACP** | OpenAI + Stripe | Agentic commerce checkout | Early; payment token delegation |
| **AP2** | Google | Payment mandates + crypto consent | Early; Ed25519 signatures |
| **TAP** | Visa | Agent identity verification | Announced 2026 |

**Key insight from DPP agents**: All protocols are <1 year old. Best practices don't exist. Architecture should use hexagonal design with swappable protocol adapters.

---

## Cross-Cutting: Python Web Frameworks

### Backend Framework Comparison

| Framework | Performance | Async | Ecosystem | Music Attribution Fit |
|-----------|------------|-------|-----------|----------------------|
| **FastAPI** | High | Native async | Largest Python API ecosystem; used by OpenAI, Anthropic | Primary recommendation — Pydantic native, OpenAPI auto-docs |
| **Litestar** | Slightly faster in micro-benchmarks | Native async | Smaller but growing | Alternative — less ecosystem, more performance |
| **Django 5** | Medium | Partial (ORM still sync) | Largest overall Python web | Admin interface; ORM limits async benefits |

**Prior experience**: KusiKasa: FastAPI backend. DPP agents: FastAPI.

---

## Cross-Cutting: Graph RAG

### Knowledge Graph + Retrieval

| Tool | Key Features | Music Attribution Fit |
|------|-------------|----------------------|
| **Microsoft GraphRAG** | Community detection, entity extraction, multi-level summarization | Interesting for attribution network analysis |
| **LightRAG** | Lightweight graph-based RAG, simpler than GraphRAG | Good for MVP — less infrastructure |
| **nano-graphrag** | Minimal GraphRAG implementation | Prototyping only |

**Music attribution insight**: The attribution knowledge graph (artist → credit → track → release → label) is a natural fit for Graph RAG. Entity resolution across sources (Discogs, MusicBrainz, artist input) benefits from graph-based retrieval.

---

## Cross-Cutting: Entity Resolution

> Core problem for music attribution — matching "John Lennon" across MusicBrainz, Discogs, Spotify, and artist input

### Dedicated Entity Resolution Libraries

| Library | Key Features | Music Attribution Fit |
|---------|-------------|----------------------|
| **Splink** | Probabilistic record linkage at scale; DuckDB-based; Fellegi-Sunter model; Python | High — handles millions of music records; probability-based matching aligns with confidence scoring philosophy |
| **dedupe** | ML-based deduplication; active learning (human-in-the-loop training); Python | High — semi-supervised approach ideal for artist name disambiguation |
| **Record Linkage Toolkit** | Python toolkit for record linkage; classifiers, string similarity, blocking | Medium — academic-oriented; good for prototyping |

### Complementary Approaches

| Approach | Tools | Music Attribution Fit |
|----------|-------|----------------------|
| **Embedding similarity** | sentence-transformers + pgvector | Semantic matching ("The Beatles" ≈ "Beatles, The") |
| **String similarity** | jellyfish, thefuzz (fuzzywuzzy) | Quick fuzzy matching for artist names |
| **Knowledge graph resolution** | Apache AGE traversals | Resolve via known relationships (same label, same album) |
| **LLM-assisted** | Claude/GPT structured output | Complex disambiguation requiring context ("John Williams" the composer vs guitarist) |

**Key insight**: Music attribution entity resolution is a multi-signal problem. The best approach combines string similarity (fast filter), embedding similarity (semantic), graph traversal (relationship evidence), and LLM reasoning (complex cases) — scoring each signal's confidence via conformal prediction.

---

## Music: Audio Fingerprinting

> Domain-critical for identifying recordings across sources

### AcoustID + Chromaprint

| Aspect | Details |
|--------|---------|
| **Status** | Active, open-source. Chromaprint 1.6.0 (Aug 2025) |
| **License** | Chromaprint: LGPL 2.1+ / MIT; AcoustID web service: free for non-commercial |
| **Rate limit** | AcoustID: 3 requests/second |
| **Python SDK** | [pyacoustid](https://pypi.org/project/pyacoustid/) v1.3.0 (Beetbox project) |
| **Key features** | Compact acoustic fingerprints, near-identical audio matching, links to MusicBrainz recording IDs |
| **Music attribution fit** | Essential — resolves "what recording is this?" as the first step in any attribution pipeline |
| **CV value** | High — demonstrates MIR (Music Information Retrieval) knowledge |

**Chromaprint 1.6.0 highlights**: FFmpeg 8.0 support, `chromaprint_decode_fingerprint_header` function, optimized simhash calculation, improved compression performance, Linux ARM64 binaries.

**Caveat**: pyacoustid hasn't seen a PyPI release in 12+ months. Functionally stable but low maintenance cadence. The C library (Chromaprint) is actively maintained.

### Dejavu (Private Fingerprint Database)

| Aspect | Details |
|--------|---------|
| **Status** | Maintenance-only / effectively dormant |
| **License** | MIT |
| **Key features** | Spectrogram-based fingerprinting (Shazam-style), MySQL/PostgreSQL backend, custom audio database matching |
| **Music attribution fit** | Low-medium — useful for private catalog matching, not public lookup |

### audfprint (Research Reference)

| Aspect | Details |
|--------|---------|
| **Status** | Academic/research tool (Dan Ellis, Columbia University) |
| **License** | Apache 2.0 |
| **Key features** | Landmark-based fingerprinting, configurable hash density, temporal alignment |
| **Music attribution fit** | Low — research reference, not production-grade |

---

## Music: Industry APIs & Data Sources

> Sources for resolving credits, recordings, and compositions

### MusicBrainz API (Critical)

| Aspect | Details |
|--------|---------|
| **Status** | Active, open-source, community-maintained (MetaBrainz Foundation) |
| **Pricing** | Free |
| **Rate limits** | 1 request/second (higher with identified user agents) |
| **Python SDK** | [python-musicbrainzngs](https://pypi.org/project/musicbrainzngs/) v0.7.1 |
| **Data** | Recordings, releases, artists, works, ISRCs, ISWCs, artist-recording relationships, cover art, AcoustID integration |
| **Music attribution fit** | Critical — richest open relationships model for who-played/wrote/produced-what |
| **Self-hosted** | Full database dumps available (PostgreSQL), enabling unlimited queries |

### Discogs API

| Aspect | Details |
|--------|---------|
| **Status** | Active |
| **Pricing** | Free |
| **Rate limits** | 60 req/min (authenticated), 25 req/min (unauthenticated) |
| **Python SDK** | [python3-discogs-client](https://pypi.org/project/python3-discogs-client/) v2.8 (Feb 2025) |
| **Data** | Detailed release credits (musicians, engineers, producers), physical release info, label discographies |
| **Music attribution fit** | High — excels at liner-notes-style credits, complementary to MusicBrainz |

### Spotify Web API (Declining)

| Aspect | Details |
|--------|---------|
| **Status** | Active but significantly restricted (Nov 2024 → Feb 2026) |
| **Deprecated endpoints** | Audio features, audio analysis, recommendations, related artists, 30s previews |
| **Access restrictions** | Extended access: 250K+ MAU organizations only (May 2025); Premium required for dev mode (Feb 2026) |
| **Python SDK** | [spotipy](https://github.com/spotipy-dev/spotipy) — actively maintained (Jan 2026) |
| **Music attribution fit** | Medium (declining) — still useful for ISRC resolution and basic metadata, but increasingly restrictive |

**Key insight**: Spotify's deprecation of audio features/analysis forces local computation via librosa/Essentia. This is actually better for attribution systems needing reproducible, transparent feature extraction.

### Genius API

| Aspect | Details |
|--------|---------|
| **Pricing** | Free (requires API token) |
| **Python SDK** | [lyricsgenius](https://pypi.org/project/lyricsgenius/) v3.7.5 |
| **Music attribution fit** | Low-medium — primarily lyrics/annotations; songwriter credits supplementary to MusicBrainz/Discogs |

### Jaxsta (Decommissioned)

| Aspect | Details |
|--------|---------|
| **Status** | DECOMMISSIONED — API and commercial services shut down |
| **Previous value** | World's largest official music credits database (380+ industry partners) |
| **Music attribution fit** | None (as of Feb 2026) |

**Significance**: Jaxsta's closure validates the Oracle Problem discussed in the companion paper — even the most comprehensive credits database could not sustain itself commercially. Technology and dataset "being preserved for potential future opportunities."

### ASCAP/BMI Songview

| Aspect | Details |
|--------|---------|
| **Status** | Active (web search only — no public developer API) |
| **Data** | 38+ million musical works with PRO-level ownership/administration shares |
| **Music attribution fit** | High value data, low integration value — no API means manual lookup or fragile scraping |
| **Future** | May explore "customizable interactive API solutions" |

### SoundExchange

| Aspect | Details |
|--------|---------|
| **API** | Repertoire Search API (by request — contact api@soundexchange.com); MDX platform (DDEX MWN XML) |
| **ISRC Search** | Public web tool at isrc.soundexchange.com |
| **Music attribution fit** | Medium — ISRC lookups against ~20M ISRCs; access requires direct contact |

---

## Music: Metadata Standards & Identifiers

> The identifier ecosystem for recordings, works, and people

| Standard | Managed By | Format | Identifies | Lookup APIs |
|----------|-----------|--------|------------|-------------|
| **ISRC** | IFPI | CC-XXX-YY-NNNNN | A specific *recording* | IFPI ISRC Search, SoundExchange, Quansic API (RIAA-approved), MusicBrainz |
| **ISWC** | CISAC | T-NNN.NNN.NNN-C | A *musical composition* | ISWC Portal (iswcnet.cisac.org), ISWC IPI Context Search (Dec 2025), MusicBrainz |
| **ISNI** | ISNI International Agency | 16-digit number | A *person or organization* | AtomPub API (membership required), Quansic ISNI API, OCLC PID Lookup |
| **IPI** | SUISA/CISAC | 11-digit number | A specific *rightsholder* | Via PROs (ASCAP/BMI), ISWC IPI Context Search |

### DDEX (Digital Data Exchange)

| Aspect | Details |
|--------|---------|
| **Current ERN** | ERN 4.3.2 (ERN v3.x and v4.0 sunset Mar 2025) |
| **Key standards** | ERN (Electronic Release Notification), MEAD/MWN (Musical Works) |
| **Python libraries** | [anthonycorletti/ddex](https://github.com/anthonycorletti/ddex) (validation/creation), [ddex-suite](https://github.com/daddykev/ddex-suite) (Rust core + PyO3, parser v0.4.5, targeting v1.0 Q1 2026) |
| **Music attribution fit** | High for production — industry standard for label/distributor/DSP metadata exchange |

### ID3 Tags (Embedded Metadata)

| Aspect | Details |
|--------|---------|
| **Standard** | ID3v2.4 (current); ID3v2.3 (broadest compatibility) |
| **Attribution frames** | TSRC (ISRC), TIPL (involved people), TMCL (musician credits) |
| **Python libraries** | mutagen, eyeD3, music-tag (see [Music: Python Metadata Libraries](#music-python-metadata-libraries)) |

**Key insight (Dec 2025)**: CISAC launched the ISWC IPI Context Search — an API allowing publishers to search for creator IPI numbers using name + known work titles. First programmatic access to composition-level identity data.

---

## Music: Audio Analysis Libraries

> Local audio feature extraction — fills the gap left by Spotify API deprecations

### librosa

| Aspect | Details |
|--------|---------|
| **Version** | 0.11.0 |
| **License** | ISC |
| **Python** | 3.8+ (3.12 support in 0.11.0) |
| **Key features** | Spectrograms, MFCCs, chroma, beat tracking, tempo, onset detection, CQT, STFT, harmonic-percussive separation |
| **Music attribution fit** | High — standard MIR library for cover song detection (chroma), tempo/key analysis, structural segmentation |
| **CV value** | High — standard in MIR research |

### Essentia

| Aspect | Details |
|--------|---------|
| **Version** | 2.1b6.dev1389 (Jul 2025) |
| **License** | AGPL 3 (proprietary license available) |
| **Python** | 3.9-3.13 wheels |
| **Key features** | 200+ algorithms, TensorFlow model integration, genre classification, instrument detection, chord recognition, key detection |
| **Origin** | Music Technology Group, Universitat Pompeu Fabra (Barcelona) |
| **Music attribution fit** | High — most comprehensive audio analysis library; ML-based classification aids confidence scoring |
| **Caveat** | AGPL license requires consideration for commercial use |

### madmom (Declining)

| Aspect | Details |
|--------|---------|
| **Status** | Dormant — last PyPI release 12+ months ago |
| **Key features** | State-of-the-art beat/downbeat tracking, deep learning models |
| **Music attribution fit** | Low-medium — excellent algorithms but Python 3.13 compatibility issues |

### aubio (Legacy)

| Aspect | Details |
|--------|---------|
| **Version** | 0.4.9 on PyPI (Feb 2019); 0.5.0-alpha stalled |
| **Key features** | Pitch detection, onset detection, beat tracking; C core |
| **Music attribution fit** | Low — source-only PyPI distribution, stalled development |

---

## Music: Python Metadata Libraries

> Reading and writing music file metadata

| Library | Version | License | Formats | Key Feature |
|---------|---------|---------|---------|-------------|
| **mutagen** | Latest (stable) | GPL 2+ | MP3, FLAC, OGG, MP4, AIFF, WavPack + more | Zero-dependency, broadest format support |
| **music-tag** | 0.4.3 | MIT | All (via mutagen) | Format-agnostic dict interface, CLI batch ops |
| **eyeD3** | 0.9.9 (Nov 2025) | GPL 3 | MP3 only | Full ID3v2 support, plugin architecture |
| **musicbrainzngs** | 0.7.1 | BSD 2-Clause | N/A (API client) | Full MusicBrainz Web Service 2 coverage |
| **spotipy** | Latest (Jan 2026) | MIT | N/A (API client) | Full Spotify Web API; CVE-2025-27154 patched |
| **pylast** | 7.0.1 | Apache 2.0 | N/A (API client) | Last.fm/Libre.fm interface |
| **python3-discogs-client** | 2.8 | MIT | N/A (API client) | Discogs API with rate limiting |

**Recommendation**: mutagen as the foundation for file-level metadata, musicbrainzngs for open data lookups, python3-discogs-client for credits resolution.

---

## Python Development Toolchain

> The tools used to build the scaffold itself

### Astral Suite (uv + ruff + ty)

| Tool | Version | Key 2026 Feature | Status |
|------|---------|-----------------|--------|
| **uv** | Latest | Package manager replacing pip/pip-tools/poetry/pdm; 10-100x faster installs | Production — project standard |
| **ruff** | Latest | Linter + formatter replacing flake8/black/isort; Rust-based | Production — project standard |
| **ty** | Beta (Dec 2025) | Type checker: 10-60x faster than mypy; intersection types, advanced narrowing | Beta — stable release targeting 2026; use alongside mypy |

**Key insight**: ty (Astral's type checker) achieves 4.7ms recheck on PyTorch repo — 80x faster than Pyright, 500x faster than Pyrefly. Stable 2026 roadmap targets >60% conformance, Pydantic/Django support.

### Data Processing

| Tool | Version | Key Feature | Music Attribution Fit |
|------|---------|-------------|----------------------|
| **Polars** | 1.38.1 (Feb 2026) | Rust-based DataFrame library; lazy evaluation, multithreaded | High — batch processing of attribution data, catalog analytics |
| **Pydantic** | 2.13 | 17x faster than v1; MISSING sentinel, per-call extra behavior, ML-specific validators | Critical — data model foundation for the entire system |

### Testing

| Tool | Key Feature | Music Attribution Fit |
|------|-------------|----------------------|
| **pytest** | Project standard; fixtures, parametrize, async support | Standard |
| **Hypothesis** | Property-based testing; generates edge cases automatically | High — test attribution logic with generated metadata combinations |
| **Testcontainers** | Disposable Docker containers for integration tests | High — spin up PostgreSQL + pgvector + AGE for real DB tests |
| **pytest-asyncio** | Async test support for FastAPI endpoints | Required for async backend |

---

## Embedding Models

> Vector representations for entity resolution and semantic search

| Model | Provider | Dimensions | Context | Key Feature | Pricing |
|-------|----------|-----------|---------|-------------|---------|
| **jina-embeddings-v4** | Jina AI | Variable | 32K tokens | Multimodal (text+image+PDF), 89 languages, task-specific LoRA adapters, 3.8B params | 10M free tokens, then usage-based |
| **text-embedding-3-large** | OpenAI | 3072 | 8K | Matryoshka dimensions (256-3072), best general-purpose | $0.13/M tokens |
| **Cohere Embed v3** | Cohere | 1024 | 512 | Compression (int8, binary), search quality focus | $0.10/M tokens |
| **Nomic Embed** | Nomic AI | 768 | 8K | Open-source, Matryoshka, good multilingual | Free (self-hosted) or API |
| **Voyage AI** | Voyage | Variable | 32K | Code + text specialized models | $0.06-0.12/M tokens |
| **sentence-transformers** | HuggingFace | Various | Model-dependent | Open-source framework; host any model locally | Free (self-hosted) |

**Music attribution fit**: Entity resolution ("John Lennon" across MusicBrainz/Discogs/Spotify) benefits from embedding similarity. sentence-transformers with a fine-tuned model on music metadata is the highest-value approach for the scaffold.

---

## Full-Text Search

> Structured search across attribution records

| Tool | Type | Key Feature | Music Attribution Fit |
|------|------|-------------|----------------------|
| **ParadeDB (pg_search)** | PostgreSQL extension | BM25 full-text search inside PostgreSQL; Elasticsearch-like queries without separate service | High — unified stack, avoids external search service |
| **Typesense** | Standalone | Sub-50ms search, typo tolerance, faceted search, geo-aware | Medium — good for artist/track search UI |
| **Meilisearch** | Standalone | Developer-friendly, fast, good for small-medium datasets | Medium — alternative to Typesense |
| **PostgreSQL FTS** | Built-in | tsvector/tsquery, GIN indexes | Baseline — sufficient for MVP; ParadeDB upgrades this significantly |

**Recommendation**: Start with PostgreSQL native FTS, upgrade to ParadeDB (pg_search) when BM25 quality is needed — no infrastructure change required.

---

## Task Queues & Background Processing

> Async job execution for multi-source attribution resolution

| Tool | Version | Key Feature | Music Attribution Fit |
|------|---------|-------------|----------------------|
| **Celery** | 5.6.2 (Jan 2026) | Distributed task queue; Pydantic model support (new); RabbitMQ quorum queues; soft shutdown | High — batch attribution resolution across multiple APIs |
| **ARQ** | Latest | Async Redis queue; lightweight, FastAPI-native | High — simpler alternative for single-server MVP |
| **Huey** | 2.6.0 (Jan 2026) | Lightweight; Redis/SQLite/in-memory backends | Medium — good for solo hacker archetype |
| **TaskIQ** | Latest | Modern async Celery alternative; FastAPI integration, PEP-612 typing | High — best DX for async Python; PostgreSQL result backend |
| **Dramatiq** | Latest | Alternative to Celery; RabbitMQ/Redis; simpler API | Medium — less ecosystem than Celery |

**Recommendation for music attribution**: ARQ for MVP (single server, Redis-backed), Celery or TaskIQ for scale (multi-worker, distributed resolution across MusicBrainz/Discogs/AcoustID).

---

## Caching: Redis & Alternatives

> API response caching, rate limit management, session storage

| Tool | Status | Key Feature | Pricing |
|------|--------|-------------|---------|
| **Valkey** | 8.x (2026) | Redis fork (Linux Foundation); fully compatible; post-license-change standard | Free (open-source) |
| **Redis** | 8.x | Original; SSPL license since 2024 | Free (open-source with SSPL restrictions); Redis Cloud from $7/mo |
| **DragonflyDB** | Latest | Drop-in Redis replacement; 25x throughput on single instance | Free (open-source); Cloud available |
| **KeyDB** | Latest | Multi-threaded Redis fork; active-active replication | Free (open-source) |

**Music attribution fit**: Caching is essential for API rate limit compliance (MusicBrainz: 1 req/s, Discogs: 60 req/min). Valkey is the recommended choice post-Redis license change.

---

## Data Quality & Validation

> Ensuring attribution data integrity

| Tool | Key Feature | Music Attribution Fit |
|------|-------------|----------------------|
| **Pydantic v2** | Runtime validation; 17x faster than v1; ML-specific validators | Foundation — all attribution records as Pydantic models |
| **Pandera** | DataFrame validation (pandas/Polars); statistical assertions | High — validate batch imports from MusicBrainz/Discogs data dumps |
| **Great Expectations** | Data pipeline validation; expectations as tests; data docs | Medium — more infrastructure; useful for data pipeline monitoring |

---

## Database Migrations

> Schema evolution for PostgreSQL + pgvector + Apache AGE

| Tool | Key Feature | Music Attribution Fit |
|------|-------------|----------------------|
| **Alembic** | SQLAlchemy migration tool; autogenerate from models; branching | Standard — if using SQLAlchemy ORM |
| **yoyo-migrations** | Raw SQL migrations; simple, no ORM dependency | Good for raw SQL + Apache AGE DDL |
| **aerich** | Tortoise ORM migrations | Only if using Tortoise ORM |

**Recommendation**: Alembic for ORM-managed tables + raw SQL migration files for Apache AGE graph schemas and pgvector index management.

---

## Object Storage

> Audio file storage, data dump archives, backup artifacts

| Provider | Pricing | Key Feature | Music Attribution Fit |
|----------|---------|-------------|----------------------|
| **Cloudflare R2** | Free (10GB), $0.015/GB/mo | Zero egress fees; S3-compatible | High — audio file storage without bandwidth costs |
| **MinIO** | Free (self-hosted) | S3-compatible; self-hosted on Hetzner | High for engineer-heavy — full control |
| **Backblaze B2** | Free (10GB), $0.006/GB/mo | Cheapest storage; S3-compatible | Good for archival (data dumps) |
| **Tigris** | Included with Fly.io | S3-compatible; globally distributed | Only if using Fly.io compute |

---

## Content Provenance (C2PA)

> Digital provenance for attribution records — bridges to AI Passport / DPP research

| Aspect | Details |
|--------|---------|
| **Standard** | C2PA (Coalition for Content Provenance and Authenticity) |
| **Status** | 3,700+ member coalition; 2026 is "turning point" for adoption; Google, TikTok, OpenAI, Meta, LinkedIn, Sony onboard |
| **Python SDK** | [c2pa-python](https://opensource.contentauthenticity.org/docs/c2pa-python/) — read/validate/create/sign C2PA manifests; Python 3.10+; Apache 2.0 + MIT |
| **Key capability** | Embed provenance manifests in media files; sign with various algorithms; verify chain of custody |
| **Music attribution fit** | High for research — attribution records could carry C2PA manifests proving provenance chain; directly connects to AI Passport / DPP traceability research |
| **CV value** | Very high — demonstrates content authenticity expertise; emerging standard |

**Key insight**: C2PA for *music attribution records* is novel. A track's attribution could include a signed manifest showing: original credits source (MusicBrainz), verification method (AcoustID fingerprint), confidence score (conformal prediction), and consent status (MCP permission query). This connects the music attribution scaffold to the broader content provenance ecosystem.

---

## Documentation Tools

> Documentation as a portfolio deliverable

| Tool | Key Feature | Music Attribution Fit |
|------|-------------|----------------------|
| **MkDocs Material** | Markdown-based; search, versioning, dark mode, mermaid support | Recommended — Python-ecosystem standard; excellent theme |
| **Marimo** | Reactive Python notebooks; version-controlled (pure .py); replaces Jupyter for explorations | High — interactive attribution demos, confidence calibration visualizations |
| **Jupyter Book 2** | MyST Markdown engine; executable content; Typst PDF rendering | Alternative — better for academic publication companion |

---

## Recommended MVP Stack

Based on cross-referencing the probabilistic PRD defaults, prior project experience, and 2026 landscape:

### For "Engineer-Heavy" Archetype (Portfolio-Optimized)

| Category | Choice | Rationale |
|----------|--------|-----------|
| **Core Infrastructure** | | |
| Primary Database | PostgreSQL 18 (unified) | UUIDv7, AIO, pgvector + AGE |
| Graph Strategy | Apache AGE | Same-database graph queries |
| Vector Strategy | pgvector | Unified stack, sufficient for <1M vectors |
| Full-Text Search | PostgreSQL FTS → ParadeDB | Start native, upgrade to BM25 when needed |
| Caching | Valkey | Post-Redis-license-change standard |
| Task Queue | ARQ (MVP) → TaskIQ (scale) | Async-native, FastAPI integration |
| Object Storage | Cloudflare R2 | Zero egress, S3-compatible |
| **AI & LLM** | | |
| LLM Provider | Multi-provider (Claude primary) | Multi-tier routing for cost; Claude for quality |
| AI Framework | PydanticAI | Production-stable, durable execution, MCP-native |
| Embeddings | sentence-transformers (local) + Jina v4 (API) | Fine-tunable local + multimodal API fallback |
| UQ | MAPIE + pgmpy | Conformal prediction + Bayesian networks |
| **Music-Specific** | | |
| Audio Fingerprinting | AcoustID + Chromaprint | De facto standard, links to MusicBrainz |
| Metadata Backbone | MusicBrainz API (musicbrainzngs) | Open, richest relationships model |
| Credits Source | Discogs API (python3-discogs-client) | Best liner-notes-style credit data |
| Audio Analysis | librosa + Essentia | Feature extraction replacing Spotify |
| File Metadata | mutagen | Zero-dependency, broadest format support |
| DDEX Integration | ddex-suite (when v1.0 ships Q1 2026) | Industry standard for label workflows |
| **Frontend & Auth** | | |
| Frontend | Next.js 15 + shadcn/ui | Largest ecosystem, Vercel AI SDK for chat |
| Auth | Clerk or WorkOS | WorkOS free tier is exceptional |
| Backend | FastAPI | Pydantic-native, async, proven |
| **Deployment & Ops** | | |
| Compute | Render (MVP) → Hetzner + Coolify (scale) | Simple start, cost-optimize later |
| Database Hosting | Neon | Serverless PostgreSQL, branching for dev |
| CI/CD | GitHub Actions + Depot | 40% cheaper runners + fast Docker builds |
| IaC | Pulumi (Python) | Python-native IaC |
| Observability | Langfuse + Grafana Stack | LLM tracing + system metrics |
| Secrets | Infisical or SOPS | Open-source, Git-friendly |
| Migrations | Alembic + raw SQL for AGE | ORM tables + graph schema |
| **Dev Toolchain** | | |
| Package Manager | uv | 10-100x faster; project standard |
| Linter/Formatter | ruff | Replaces flake8+black+isort |
| Type Checker | mypy (now) → ty (when stable 2026) | Speed upgrade path clear |
| Testing | pytest + Hypothesis + Testcontainers | Property-based + real DB integration tests |
| Data Processing | Polars | Rust-based, lazy eval, multithreaded |
| Documentation | MkDocs Material + Marimo | Static docs + interactive notebooks |

### For "Solo Hacker" Archetype (Minimum Viable)

| Category | Choice | Rationale |
|----------|--------|-----------|
| **Core Infrastructure** | | |
| Primary Database | Supabase | Built-in auth, realtime, pgvector |
| Graph Strategy | SQL joins only | Minimal complexity |
| Vector Strategy | pgvector (via Supabase) | Included with database |
| Full-Text Search | PostgreSQL FTS (Supabase) | Built-in |
| Caching | None (or Supabase Edge Cache) | Skip for MVP |
| Task Queue | Huey (SQLite backend) | Zero-dependency task execution |
| **AI & LLM** | | |
| LLM Provider | Claude Haiku 4.5 | Best cost/quality ratio |
| AI Framework | Instructor | Minimal overhead |
| Embeddings | Nomic Embed (free API) | No infrastructure needed |
| **Music-Specific** | | |
| Audio Fingerprinting | AcoustID (web service only) | No local Chromaprint compilation |
| Metadata Backbone | MusicBrainz API | Same as above; free, open |
| Credits Source | Discogs API | Free, good rate limits |
| File Metadata | music-tag | Simpler API than raw mutagen |
| **Frontend & Auth** | | |
| Frontend | HTMX + Jinja | Python-only stack |
| Auth | Supabase Auth | Included |
| Backend | FastAPI | Standard |
| **Deployment & Ops** | | |
| Compute | Railway | Usage-based, free credits |
| Database Hosting | Supabase | Included |
| CI/CD | GitHub Actions | Free for public repos |
| IaC | None (platform-native) | Skip entirely |
| Observability | Minimal logging + Langfuse free | Structured JSON to stdout |
| Secrets | Environment variables | Simple for MVP |
| **Dev Toolchain** | | |
| Package Manager | uv | Same as engineer-heavy |
| Linter/Formatter | ruff | Same |
| Testing | pytest | Minimal |
| Documentation | README.md + docstrings | Keep simple |

---

## Technology Volatility Watch (Next Review: May 2026)

### Volatile (Review Monthly)

| Area | Watch For |
|------|----------|
| LLM Providers | Gemini 3 Pro (2M context), GPT-5.x pricing, open-source convergence |
| Agent Frameworks | PydanticAI adoption, Claude Agent SDK features, Google ADK maturity |
| Protocol Landscape | MCP adoption, A2A maturity, new protocols emerging |
| Embedding Models | Jina v4 benchmarks, OpenAI new models, open-source parity |
| Spotify API | Further endpoint restrictions, alternative data source viability |

### Shifting (Review Quarterly)

| Area | Watch For |
|------|----------|
| Vector Databases | pgvector vs dedicated VDB performance parity |
| Frontend Frameworks | React Server Components stability, Svelte 5 adoption |
| Auth Services | WorkOS free tier sustainability, Better Auth ecosystem |
| Deployment | Hetzner managed services, Coolify maturity |
| Type Checkers | ty stable release (2026); Pyrefly competition |
| DDEX Libraries | ddex-suite v1.0 target Q1 2026 |
| C2PA Adoption | Content Credentials for audio/music media |
| Task Queues | TaskIQ vs Celery ecosystem maturity |

### Stable (Review Semi-Annually)

| Area | Watch For |
|------|----------|
| PostgreSQL | Extension ecosystem (AGE stability, ParadeDB maturity) |
| FastAPI | Litestar competitive pressure |
| GitHub Actions | Pricing model stability |
| Conformal Prediction | MAPIE alternatives, LLM-native UQ |
| MusicBrainz/Discogs | API stability, data completeness |
| Audio Fingerprinting | AcoustID/Chromaprint maintenance; alternative services |
| Polars | pandas migration path; ecosystem plugin growth |

---

## Sources & Cross-References

### Internal Documents

- [Probabilistic PRD Design](probabilistic-prd-design.md) — Bayesian network model
- [Probabilistic PRD Decision Network](../prd/decisions/README.md) — 23 decision nodes
- [Network Report](../prd/decisions/REPORT.md) — Visualizations
- [Archetypes](../prd/archetypes/README.md) — Team profiles
- [Defaults](../prd/defaults.yaml) — Current active choices
- [Rejected Technologies](../prd/REJECTED.md) — Why NOT certain technologies

### External Projects Referenced

- KusiKasa uad-copilot: `techstack.md`, `techstack_poc2.md`, `techstack_poc3.md`
- DPP agents: `pre-voice-mva-refactoring-plan-v3-final.md`, `probabilistic-dpp-schema-research.md`, `agentic-commerce-revolution-research.md`, PRD directory

### Key 2026 Sources

**Infrastructure & Cloud**:
- PostgreSQL 18 release notes: [postgresql.org/about/news/postgresql-18-released-3142](https://www.postgresql.org/about/news/postgresql-18-released-3142/)
- GitHub Actions 2026 pricing: [resources.github.com/actions/2026-pricing-changes](https://resources.github.com/actions/2026-pricing-changes-for-github-actions)
- OpenTofu state encryption: [opentofu.org/blog/opentofu-1-7-0](https://opentofu.org/blog/opentofu-1-7-0/)
- Milvus 2.6.x features: [morningstar.com news release](https://www.morningstar.com/news/pr-newswire/20260120cn67271/)

**AI & Frameworks**:
- PydanticAI stable release: [pypi.org/project/pydantic-ai](https://pypi.org/project/pydantic-ai/)
- Claude Opus 4.6: [anthropic.com/news/claude-opus-4-6](https://www.anthropic.com/news/claude-opus-4-6)
- Jina Embeddings v4: [jina.ai/news/jina-embeddings-v4](https://jina.ai/news/jina-embeddings-v4-universal-embeddings-for-multimodal-multilingual-retrieval/)

**Auth & Frontend**:
- Auth.js → Better Auth merger: [github.com/nextauthjs/next-auth/discussions/13252](https://github.com/nextauthjs/next-auth/discussions/13252)

**Music Industry**:
- Chromaprint 1.6.0: [github.com/acoustid/chromaprint/releases](https://github.com/acoustid/chromaprint/releases)
- AcoustID web service: [acoustid.org/webservice](https://acoustid.org/webservice)
- Spotify API restrictions (Feb 2026): [developer.spotify.com/blog](https://developer.spotify.com/documentation/web-api/references/changes/february-2026)
- CISAC ISWC IPI Context Search (Dec 2025): [iswc.org/creators-publishers](https://www.iswc.org/creators-publishers)
- DDEX ERN 4.3.2: [ddex.net/standards](https://ddex.net/standards/)
- ddex-suite (Rust+PyO3): [github.com/daddykev/ddex-suite](https://github.com/daddykev/ddex-suite)
- Jaxsta decommissioned: [jaxsta.com/info/api](https://jaxsta.com/info/api)
- Quansic ISRC/ISNI API: [quansic.com/api](https://quansic.com/api/)

**Python Toolchain**:
- ty (Astral type checker): [astral.sh/blog/ty](https://astral.sh/blog/ty)
- Polars 1.38.1: [pypi.org/project/polars](https://pypi.org/project/polars/)
- Celery 5.6.2: [docs.celeryq.dev](https://docs.celeryq.dev/)
- Pydantic 2.13: [docs.pydantic.dev](https://docs.pydantic.dev/latest/)

**Content Provenance**:
- C2PA Python library: [opensource.contentauthenticity.org/docs/c2pa-python](https://opensource.contentauthenticity.org/docs/c2pa-python/)
- State of Content Authenticity 2026: [contentauthenticity.org/blog](https://contentauthenticity.org/blog/the-state-of-content-authenticity-in-2026)
