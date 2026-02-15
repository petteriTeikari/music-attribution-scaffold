# Expanding the Probabilistic PRD: From MVP Results to Discussion

**Date:** 2026-02-14
**Status:** Strategic Roadmap
**PRD Version:** 2.2.0 → 3.0.0
**Companion to:** Teikari, P. (2026). *Music Attribution with Transparent Confidence*. SSRN No. 6109087.

---

## 1. Framing: Paper → Scaffold → Discussion

The academic manuscript follows a conventional structure that maps onto the scaffold's development lifecycle:

| Paper Section | Scaffold Equivalent | Artifact |
|---------------|---------------------|----------|
| **Methods** | PRD concept + library selection | Probabilistic decision network (v1.0–v2.0), technology landscape reports |
| **Results** | MVP implementation | 50 PRD nodes, working frontend, 493 passing tests, 5-pipeline architecture |
| **Discussion** | **This expansion** | 28 new ecosystem nodes, integration strategies, future directions |

The "Methods" established *how* we make decisions (Bayesian priors, archetype conditioning, conditional probability edges). The "Results" demonstrated that the approach produces a working system. The "Discussion" now asks: *what happens when this scaffold encounters the real world?*

This is deliberately the most speculative section of the project. While the MVP nodes (L1–L5 core) have selected options backed by working code, the expansion nodes capture possibility spaces — companies we might partner with, regulations we might need to comply with, protocols we might adopt. High prior probabilities on "none" options encode honest uncertainty: we haven't committed, and that's the point.

---

## 2. From MVP Results to Discussion Questions

The MVP's 50-node network answers "how do you build a music attribution system?" The expansion asks:

### 2.1 Integration Questions

- **How does the scaffold interact with existing music-tech infrastructure?** Companies like Musical AI (training-time attribution), Sureel AI (identification), SoundExchange (rights registry), and Fairly Trained (certification) each represent potential integration surfaces. The scaffold can consume their APIs, provide data to their systems, or remain standalone.

- **What happens when AI music platforms (Suno, Udio) start producing attribution metadata?** The scaffold needs connectors to ingest platform-specific metadata formats, normalize them against the NormalizedRecord schema, and score confidence against multiple sources.

- **How does collective licensing infrastructure affect the system?** STIM's pilot with Sureel AI suggests that CMOs may become both data sources and customers. The scaffold could serve as an attribution provider to CMOs, consume CMO licensing data, or both.

### 2.2 Compliance Questions

- **What does EU AI Act GPAI compliance actually require?** Article 12 logging, Article 52 transparency obligations, and the GPAI Code of Practice each create infrastructure requirements. The `compliance_reporting_pipeline` and `regulatory_monitoring` nodes capture the implementation options.

- **How do TDM (Text and Data Mining) rights reservations scale?** The existing `tdm_rights_reservation` node covers the legal framework, but the expansion adds operational infrastructure for monitoring reservation status at scale.

### 2.3 Platform Questions

- **Is the scaffold a standalone tool, an integration platform, or an acquisition target?** The `platform_strategy` node makes this question explicit. Each option implies different engineering investments: standalone tools need excellent UX, platforms need developer APIs, acquisition targets need defensible IP.

- **What partnership model enables the most leverage?** API marketplace (breadth), strategic alliance (depth), or CMO federation (institutional) — each maps to different business development strategies and technical requirements.

### 2.4 Infrastructure Questions

- **When does edge inference become necessary?** Audio fingerprinting at the edge (Cloudflare Workers AI, Deno Deploy) reduces latency for real-time attribution but adds deployment complexity. The `edge_inference_strategy` and `edge_deployment_target` nodes capture the trade-off.

- **What does agent observability look like at scale?** OpenTelemetry semantic conventions for GenAI, Pydantic Logfire, and dedicated eval frameworks represent a maturing but still fragmented space.

---

## 3. The 28 New Nodes — Rationale

### 3.1 Why Hybrid Granularity

The expansion uses a **hybrid** approach: category nodes for generic capabilities + named company nodes for strategic partners. This reflects the reality that some integration decisions are technology-generic (e.g., "do we need watermark detection?") while others are relationship-specific (e.g., "do we partner with Musical AI specifically?").

**Category nodes** (12) capture capability decisions independent of specific vendors:
- `tda_provider_integration` — Training data attribution capability (any provider)
- `cmo_licensing_integration` — Collective licensing infrastructure
- `content_id_system` — Audio fingerprinting approach
- `ai_music_platform_connector` — Platform metadata ingestion
- `metadata_registry_integration` — External registry breadth
- `watermark_detection` — Digital watermarking capability
- `agent_interop_protocol` — Multi-protocol agent communication
- `edge_inference_strategy` — Edge computing for attribution
- `attribution_eval_framework` — Evaluation infrastructure
- `agent_observability_otel` — Agent observability approach
- `agentic_commerce_protocol` — Machine-readable licensing
- `knowledge_graph_backend` — Graph storage implementation

**Named company nodes** (6) capture specific partnership decisions where the company's offering is sufficiently unique that a generic category node would be misleading:
- `musical_ai_partnership` — Musical AI's training-time TDA is architecturally unique (requires integration during model training, not post-hoc)
- `sureel_ai_partnership` — Sureel's STIM relationship and patent portfolio create a specific integration surface
- `stim_cmo_pilot` — STIM's pilot is the only operational collective AI licence globally
- `soundexchange_registry` — SoundExchange's 126M+ ISRCs make it the definitive U.S. recording registry
- `fairly_trained_certification` — Binary certification with market signaling value
- `suno_udio_licensing` — The two dominant platforms with divergent business models

### 3.2 Level Distribution

| Level | Existing Nodes | New Nodes | Total | Rationale |
|-------|---------------|-----------|-------|-----------|
| L1 Business | 4 | 0 | 4 | Business fundamentals unchanged |
| L2 Architecture | 7 | 2 | 9 | `platform_strategy` and `partnership_model` are architectural decisions with L1 inputs |
| L3 Components | 6 | 18 | 24 | The "Discussion" lives here — specific integration decisions, most uncertainty |
| L4 Deployment | 9 | 4 | 13 | Compliance, provenance, evaluation, and edge deployment infrastructure |
| L5 Operations | 10 | 4 | 14 | Monitoring and intelligence for the expanded system |
| **Total** | **36** (excl. L3-impl) | **28** | **64** (+14 L3-impl = **78**) | |

L3 receives the most new nodes (18 of 28) because ecosystem integration decisions are fundamentally implementation-level: they depend on architectural choices (L2) and constrain deployment options (L4), but they represent specific component selections rather than system-wide architectural patterns.

---

## 4. Integration Strategies

The expansion nodes imply three distinct integration archetypes:

### 4.1 Simple MCP: Lightweight API Adapters

The lowest-friction integration path. The scaffold wraps external APIs (SoundExchange lookup, Fairly Trained status check, MusicBrainz extended queries) as MCP tools. Each tool:
- Accepts structured input (Pydantic model)
- Returns structured output (confidence-annotated JSON)
- Runs in the existing FastAPI process
- Requires only an API key and rate limiting

**Applicable nodes:** `soundexchange_registry` (read-only lookup), `fairly_trained_certification` (status check), `metadata_registry_integration` (multi-registry queries), `content_id_system` (fingerprint queries)

### 4.2 Platform Integration: Bidirectional Data Exchange

Deeper integration where the scaffold both consumes and provides data. Requires schema mapping, webhook handlers, and potentially shared state:
- Attribution data flows out to partner systems
- Partner metadata flows in to the scaffold
- Both systems maintain independent copies with reconciliation

**Applicable nodes:** `musical_ai_partnership` (training-time attribution data exchange), `sureel_ai_partnership` (identification results + attribution graphs), `suno_udio_licensing` (platform metadata ingestion)

### 4.3 CMO Federation: Institutional Infrastructure

The most ambitious integration pattern. The scaffold serves as attribution infrastructure for collective management organizations:
- Multiple CMOs query the same attribution engine
- Licensing decisions are informed by confidence scores
- Audit trails satisfy regulatory requirements
- Federation protocol handles cross-CMO data sharing

**Applicable nodes:** `cmo_licensing_integration` (multi-CMO federation), `stim_cmo_pilot` (initial pilot), `compliance_reporting_pipeline` (regulatory reporting)

---

## 5. Strategic Ambiguity by Design

The expansion nodes deliberately preserve strategic ambiguity. This is a feature, not a limitation:

### 5.1 High "None" Priors

Most new nodes assign 0.40–0.55 probability to their "none" or "no integration" option. This encodes:
- **Honest uncertainty**: We genuinely don't know which partnerships will materialize
- **Resource constraints**: A small team can't pursue all 18 L3 integration options simultaneously
- **Sequential strategy**: Some decisions only become relevant after others are resolved (e.g., `stim_cmo_pilot` only matters if `cmo_licensing_integration` selects `single_cmo_pilot` or higher)

### 5.2 No Archetype Weights

Unlike core PRD nodes (which have conditional probability tables for 4 archetypes), expansion nodes use a simpler `influences:` array format. This reflects:
- **Insufficient data**: We don't have archetype-specific evidence for most ecosystem integration decisions
- **Scope control**: Adding full conditional tables for 28 nodes would require 112 probability distributions without the evidence base to populate them meaningfully
- **Progressive elaboration**: Nodes can be upgraded from stub to full format as evidence accumulates

### 5.3 Competitive Intelligence Protection

By capturing the possibility space broadly (28 nodes covering ~50 companies across 6 tiers) without committing to specific partnership strategies, the PRD demonstrates awareness without revealing intent. A reader learns that we've evaluated Musical AI, Sureel, STIM, and SoundExchange — but not whether we're actively pursuing any of them. This is the academic equivalent of a Discussion section: showing you understand the field without disclosing your unpublished results.

---

## 6. Edge Estimation and Network Topology

### 6.1 New Edge Categories

The 28 new nodes introduce approximately 55 new edges, categorized as:

| Category | Count | Pattern |
|----------|-------|---------|
| L1 → L2 (new) | 6 | Business → platform strategy/partnership model |
| L2 → L3 (new) | 10 | Architecture → ecosystem integration components |
| Existing → new L3 | 20 | Existing nodes (build_vs_buy, ai_framework, etc.) → new integration nodes |
| L3 category → L3 company | 8 | Generic capability → specific partner (e.g., `tda_provider_integration` → `musical_ai_partnership`) |
| L3 → L4 (new) | 6 | Integration components → deployment infrastructure |
| L4 → L5 (new) | 5 | Deployment → monitoring/operations |

### 6.2 Network Statistics Update

| Metric | v2.2.0 | v3.0.0 | Change |
|--------|--------|--------|--------|
| Total nodes | 50 | 78 | +28 |
| Total edges | 68 | ~123 | +55 |
| L3 nodes | 20 | 38 | +18 |
| L4 nodes | 9 | 13 | +4 |
| L5 nodes | 10 | 14 | +4 |
| Avg. in-degree | 1.36 | ~1.58 | +0.22 |
| Max in-degree | 5 | ~7 | +2 |

### 6.3 DAG Integrity

All new edges maintain acyclicity by respecting the level hierarchy (higher level → same or lower level) with the following allowed patterns:
- **Same-level cross-influences**: L3 category → L3 company (e.g., `tda_provider_integration` → `musical_ai_partnership`)
- **Adjacent-level edges**: L2 → L3, L3 → L4, L4 → L5
- **Skip-connections**: L1 → L3, L1 → L4, L2 → L4, L2 → L5 (continuing established pattern)

No edges flow upward (lower level → higher level), preserving the topological sort property.

---

## 7. Future Work

### 7.1 Deferred: New Archetypes

The current 4-archetype system (Engineer-Heavy, Musician-First, Solo Hacker, Well-Funded Startup) doesn't capture all relevant team profiles for ecosystem integration decisions. Potential additions:

- **CMO/Rights Org Team**: Institutional actors with regulatory constraints and existing music-industry relationships
- **AI Platform Team**: Suno/Udio-like companies needing attribution as a feature within their product

These are deferred until the expansion nodes accumulate sufficient interaction data to warrant archetype-specific probability distributions.

### 7.2 Planned: Two New Scenarios

Two scenario compositions will be added to REPORT.md:

1. **Partnership-Focused Scenario**: Platform integration strategy → strategic alliances → Musical AI + STIM pilot → full compliance reporting → partnership health monitoring
2. **Compliance-First Scenario**: Compliance-first regulatory posture → GPAI compliance → SoundExchange registry → automated compliance reporting → regulatory monitoring

These scenarios trace specific paths through the expanded network, demonstrating how the 28 new nodes create meaningful new compositions beyond the existing 4 scenarios.

### 7.3 Domain Overlay Expansion

The existing domain overlay system (music attribution + DPP traceability) can be extended to capture ecosystem-specific overlays:

- **CMO overlay**: Emphasizes `cmo_licensing_integration`, `stim_cmo_pilot`, `compliance_reporting_pipeline`
- **Platform overlay**: Emphasizes `ai_music_platform_connector`, `suno_udio_licensing`, `edge_inference_strategy`

These overlays would adjust prior probabilities for the subset of nodes relevant to each domain, paralleling how the DPP overlay adjusts probabilities for supply chain traceability contexts.

---

## 8. GitHub Backlog Strategy

The expansion generates approximately 43 GitHub issues across 5 categories:

| Category | Issues | P1 | P2 | Focus |
|----------|--------|----|----|-------|
| Regulatory/Compliance | 7 | 3 | 4 | EU AI Act GPAI, TDM rights, compliance automation |
| Music Tech Integration | 12 | 3 | 9 | CMO pilots, platform connectors, registry integration |
| Infrastructure/Platform | 10 | 6 | 4 | Edge inference, OTel, eval framework, knowledge graph |
| Business/Strategy | 6 | 2 | 4 | Platform strategy, partnership model, market intelligence |
| Research/Academic | 8 | 3 | 5 | Gold datasets, accuracy monitoring, supplementary paper |

Issues are deliberately **comprehensive and overwhelming** — establishing the project's scope of awareness without committing to execution timelines. This serves the academic purpose of demonstrating thorough landscape analysis while creating a structured backlog for potential contributors.

Each issue cross-references the relevant PRD node, enabling traceability from backlog item to decision context to technology analysis.

---

## References

- Tech trends report: `docs/planning/tech-trends-agentic-infrastructure-2026.md`
- PRD decision network: `docs/prd/decisions/_network.yaml`
- PRD network report: `docs/prd/decisions/REPORT.md`
- MCP security research: `docs/planning/mcp-security-production-research.md`
- Commercial landscape stubs: `docs/planning/commercial-landscape-stubs.xml`
- AI tooling landscape: `docs/planning/ai-tooling-landscape-2026-02.md`
