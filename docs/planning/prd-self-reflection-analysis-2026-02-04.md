# PRD Self-Reflection Analysis

**Date**: 2026-02-04
**Purpose**: Second-pass reflection on hierarchical PRD structure based on tech stack documentation review
**Related**: [Original Plan](prd-improvement-for-hierarchical-composable-plan.md)

---

## Executive Summary

After reviewing 50+ technical documentation files across uad-copilot, dpp-agents, and open-mode repositories, several patterns emerge that should inform the Music Attribution PRD structure:

1. **TOC Pattern**: Use Table-of-Contents files as branch indexes (not just `_index.md`)
2. **Tech Stack Bundling**: Group related technologies into coherent sub-PRDs
3. **Decision Matrices**: Every tech choice needs alternatives + rationale table
4. **Cross-Cutting Reality**: Observability, Security, and UQ span ALL domains
5. **PostgreSQL Preference**: Documented preference over specialized databases

---

## Part 1: Observed Documentation Patterns

### Pattern 1: Table of Contents (TOC) Files

The uad-copilot docs use `toc-*.md` files as domain indexes:

```
docs/08-data-ml-platform/databases/
├── toc-knowledge-graphs.md      # Index with concept overview + links
├── toc-vector-databases.md      # Index with concept overview + links
└── [implementation docs]
```

**Structure of a good TOC**:
1. Overview/What is X
2. Why X for this project
3. Core concepts
4. Implementation patterns
5. Integration points
6. References (external docs, papers)
7. Related TOCs

**Adjustment to PRD Plan**: Rename `_index.md` files to follow this TOC pattern for consistency.

### Pattern 2: Tech Stack Documents with LLM Context

The `techstack.md` pattern includes:
1. **LLM System Prompt**: Context for AI assistants to understand the stack
2. **Decision Tables**: Winner + alternatives + rationale
3. **Implementation Examples**: Code snippets
4. **Migration Paths**: When to switch technologies
5. **Cost Analysis**: Per-unit economics

**Insight for the system**: The main PRD should include an "LLM Context" section that helps Claude/Opus understand the decision space quickly.

### Pattern 3: Cross-Cutting Concern Depth

The reviewed docs show certain concerns are deeply cross-cutting:

| Concern | Span | Evidence |
|---------|------|----------|
| **Observability** | Universal | Langfuse, OpenTelemetry, Prometheus appear in voice, RAG, UQ, security docs |
| **Uncertainty Quantification** | Universal | Integrated into schemas, workflows, UI, compliance |
| **Security (MLSecOps)** | Universal | CI/CD, secrets, model protection, audit logging |
| **PostgreSQL** | Universal | Preferred over Neo4j, Supabase, dedicated VDBs |

### Pattern 4: Hybrid Architecture Preference

Multiple docs show a pattern of PostgreSQL-centric hybrid architectures:

- **Hybrid RAG**: pgvector + recursive CTEs instead of Neo4j + Chroma
- **Graph queries**: Apache AGE (pg extension) instead of Neo4j
- **Vector search**: pgvector instead of Pinecone/Weaviate

**Quote from hybrid-rag-knowledge-graph.md**:
> "Neo4j adds operational complexity (separate database, JVM, licensing for production). PostgreSQL can handle graph queries with recursive CTEs + pgvector."

---

## Part 2: Recommended Sub-PRD Candidates for the system

Based on documentation review and the system domain (music attribution, AI permissions):

### Domain-Specific PRDs (L2)

| Domain | Sub-PRDs Needed | Priority |
|--------|-----------------|----------|
| **Attribution Engine** | Multi-source aggregation, confidence scoring, conflict resolution | High |
| **Data Layer** | pgvector, Apache AGE, hybrid retrieval | High |
| **AI Integration** | MCP server, LangGraph orchestration, agent patterns | High |
| **Voice Interface** | If Nel-like persona planned (TTS, STT, pipeline) | Medium |
| **Identity/Permissions** | ArtistID, permission bundles, consent management | High |

### Cross-Cutting PRDs (L2*)

| Concern | Sub-PRDs Needed | Why Cross-Cutting |
|---------|-----------------|-------------------|
| **Observability** | Langfuse (LLM), Prometheus/Grafana (system), OpenTelemetry | Applies to all LLM interactions |
| **Uncertainty Quantification** | Conformal prediction, calibration, selective prediction | Core to confidence scoring everywhere |
| **Security** | MLSecOps, secrets management, audit logging | Applies to all data/model operations |
| **Evals** | Braintrust (general), attribution evals, voice evals | Quality assurance across domains |
| **Infrastructure** | Render/Hetzner, Neon, deployment patterns | Foundation for everything |

### Implementation PRDs (L3) - Key Decisions

| Decision Space | Options to Document | Current Preference |
|----------------|---------------------|-------------------|
| **Graph Database** | Neo4j, Apache AGE, pgvector-only | Apache AGE (pg extension) |
| **Vector Database** | pgvector, Qdrant, Pinecone | pgvector (unified DB) |
| **LLM Orchestration** | LangGraph, raw Python, LangChain | LangGraph or raw Python |
| **Voice Pipeline** | Vapi, Pipecat, Retell | Vapi (managed) → Pipecat (scale) |
| **TTS Provider** | Inworld, ElevenLabs, Cartesia | Inworld (cost) |
| **LLM Provider** | Claude (direct), OpenRouter, local | Claude via OpenRouter |
| **Observability** | Langfuse, Arize, custom | Langfuse (open-source) |
| **Infrastructure** | Render, Hetzner, AWS | Render (simplicity) |

---

## Part 3: Adjustments to Original PRD Plan

### Adjustment 1: Add "LLM Context" Section to Main PRD

Every L1 and L2 PRD should include an LLM context section like `techstack.md`:

```markdown
## LLM Context

**System Prompt for Claude/Opus working on this project:**

You are advising the system, a music attribution platform. Key context:
- Target users: Independent artists, session musicians, AI platforms
- Core problem: 40%+ of music metadata contains incorrect attribution
- Tech philosophy: PostgreSQL-centric, no unnecessary complexity
- Decision framework: Every choice must either (1) improve attribution accuracy,
  (2) enable AI permissions, or (3) build artist trust

**Critical Constraints:**
- No Neo4j (operational complexity)
- Conformal prediction for all uncertainty (formal guarantees)
- Langfuse for all LLM tracing
```

### Adjustment 2: Explicit "Negative Prompts" for Common Suggestions

Add dedicated rejection entries for technologies Claude often suggests:

| Technology | Rejection Reason | When to Reconsider |
|------------|------------------|-------------------|
| **Neo4j** | Operational complexity, no team expertise | Native Cypher algorithms required |
| **LangChain** | Over-abstraction, debugging difficulty | Need many pre-built integrations |
| **Pinecone/Weaviate** | Separate service, pgvector sufficient | >10M vectors, dedicated scaling |
| **Kubernetes** | Over-engineering for startup scale | Multi-region, >10 services |
| **MongoDB** | ACID compliance required for attribution | Document-only workloads |

### Adjustment 3: Add Uncertainty Quantification as Architectural Principle

UQ isn't just a feature—it's an architectural pattern that pervades the system:

```markdown
## Architectural Principle: Uncertainty-First Design

Every field in attribution data model should support uncertainty:

1. **Schema Extension**: All values can carry confidence intervals
2. **Propagation**: Uncertainty compounds through multi-hop attribution
3. **Selective Prediction**: Abstain when uncertainty > threshold
4. **Human-in-Loop**: Route high-uncertainty cases to review
5. **Calibration**: Conformal prediction for formal guarantees

This is NOT optional—it's the core differentiator vs. existing metadata services.
```

### Adjustment 4: Domain-Level Guidance Mapping

**Imogen Heap's Vision** (from vision-v1.md) maps to tech choices:

| Vision Element | Technical Implementation |
|----------------|------------------------|
| "Artists are experts on their work" | ArtistID: Self-sovereign identity, artist-verified data takes precedence |
| "Control digital identity" | Permission bundles: Granular consent management, revocable |
| "Do business with AI on their terms" | MCP API: Machine-readable permissions, direct negotiation |
| "40%+ metadata is wrong" | Multi-source aggregation: Confidence scoring, conflict detection |

**Andy's Guidance** (if applicable): TBD - need to clarify specific inputs

### Adjustment 5: Rename `_index.md` to `toc-*.md` Pattern

For consistency with existing documentation patterns:

```
docs/prd/
├── toc-prd.md                    # Main PRD index (was README.md)
├── vision-v1.md         # L1
│
├── voice-agent/
│   ├── toc-voice-agent.md        # Branch index (was _index.md)
│   ├── pipeline/
│   │   ├── vapi.md
│   │   └── pipecat.md
```

### Adjustment 6: Add Implementation Examples to Each L3 PRD

Following the `uncertainty-quantification-implementation.md` pattern, each L3 PRD should include:

1. **Quick Reference Table**: Key specs at a glance
2. **Code Examples**: Actual Python/TypeScript snippets
3. **Integration Pattern**: How it connects to other components
4. **Monitoring Metrics**: What to track
5. **Migration Path**: When/how to switch

---

## Part 4: Revised Target Structure

```
docs/prd/
├── defaults.yaml                    # Current active composition
├── schema.yaml                      # Frontmatter schema
├── llm-context.md                   # System prompt for AI assistants
│
├── toc-prd.md                       # Master index
├── vision-v1.md            # L1: Human-readable master
│
├── attribution-engine/              # L2: Core domain
│   ├── toc-attribution-engine.md
│   ├── multi-source-aggregation.md
│   ├── confidence-scoring.md
│   └── conflict-resolution.md
│
├── data-layer/                      # L2: Infrastructure
│   ├── toc-data-layer.md
│   ├── graph/
│   │   ├── apache-age.md            # Preferred
│   │   └── neo4j.md                 # NOT RECOMMENDED
│   ├── vector/
│   │   ├── pgvector.md              # Preferred
│   │   └── dedicated-vdb.md         # NOT RECOMMENDED
│   └── hybrid-retrieval.md
│
├── ai-integration/                  # L2: AI/Agent layer
│   ├── toc-ai-integration.md
│   ├── mcp-server.md
│   ├── langgraph-orchestration.md
│   └── llm-providers/
│       ├── claude-openrouter.md
│       └── local-models.md
│
├── identity-permissions/            # L2: Business logic
│   ├── toc-identity-permissions.md
│   ├── artist-id.md
│   └── permission-bundles.md
│
├── observability/                   # L2*: Cross-cutting
│   ├── toc-observability.md
│   ├── langfuse.md
│   ├── prometheus-grafana.md
│   └── opentelemetry.md
│
├── uncertainty/                     # L2*: Cross-cutting (architectural)
│   ├── toc-uncertainty.md
│   ├── conformal-prediction.md
│   ├── calibration.md
│   └── selective-prediction.md
│
├── security/                        # L2*: Cross-cutting
│   ├── toc-security.md
│   ├── mlsecops.md
│   ├── secrets-management.md
│   └── audit-logging.md
│
├── evals/                           # L2*: Cross-cutting
│   ├── toc-evals.md
│   ├── braintrust.md
│   └── attribution-evals.md
│
├── infrastructure/                  # L2*: Cross-cutting
│   ├── toc-infrastructure.md
│   ├── render.md
│   ├── hetzner.md
│   └── neon.md
│
└── REJECTED.md                      # Master rejection index
```

---

## Part 5: Mapping Imogen/Andy Vision to Sub-PRD Selection

### Vision → Requirements → Sub-PRD Matrix

| Vision Statement | Derived Requirement | Sub-PRD Impact |
|------------------|---------------------|----------------|
| "Artists are experts on their work" | Artist-verified data > automated data | confidence-scoring.md: Artist verification = highest weight |
| "40%+ metadata wrong" | Multi-source aggregation needed | multi-source-aggregation.md: Required |
| "Control digital identity" | Self-sovereign identity model | artist-id.md: Required |
| "Do business with AI" | Machine-readable permissions | mcp-server.md, permission-bundles.md: Required |
| "No single authority" | Distributed verification | conflict-resolution.md: Required |
| "AI companies need consent" | Consent tracking at scale | permission-bundles.md: High priority |

### Specification Change → Sub-PRD Reconfiguration

**Example 1**: "We now need real-time voice interface for artist onboarding"
- **Enables**: voice-agent/ branch
- **Sub-PRDs activated**: toc-voice-agent.md, vapi.md, inworld.md
- **Cross-cutting impact**: observability/langfuse.md#voice-integration

**Example 2**: "AI platforms want batch attribution queries"
- **Enables**: batch-processing pattern
- **Sub-PRDs activated**: langgraph-orchestration.md#batch-mode
- **Cross-cutting impact**: infrastructure/render.md#scaling

**Example 3**: "We need to prove attribution chain for EU AI Act"
- **Enables**: provenance tracking
- **Sub-PRDs activated**: hybrid-retrieval.md, audit-logging.md
- **Cross-cutting impact**: uncertainty/conformal-prediction.md#traceability

---

## Part 6: Open Questions for Further Clarification

### ANSWERED: Clarified Requirements from Imogen & Andy

**Voice Interface**: NOT planned initially. Focus is on **chat interface** (text-based):
- Gather and edit data for system input
- Allow individuals to "speak" (chat/search) with the information
- Two-role model: (1) data gathering/editing, (2) external querying

**Andy's Technical Guidance**:
> "The bit which needs the more nuanced thought is how the end user (artist) chats to the AI to extract the information with the greatest Confidence scores. And then how we deal with the other stuff, i.e. we could analyse and see that the low confidence data all relates to a particular source (credit or dataset), so it could suggest reaching out to the relevant people"

**Key Technical Implications**:
1. **Confidence-first UX**: Present 90-100% confidence data first, then progressively disclose lower confidence
2. **Source attribution for gaps**: Identify which source is causing low confidence
3. **Actionable suggestions**: "Reach out to X for this missing data"
4. **Vibe coding acceptable**: Andy explicitly endorses Claude-assisted development

**Multi-Tenant**: Confirmed planned - rights orgs, labels with isolated data

---

## Part 7: Revised Sub-PRD Priority Based on Imogen/Andy Vision

### High Priority (MVP)

| Sub-PRD | Imogen/Andy Quote | Technical Implication |
|---------|-------------------|----------------------|
| **multi-source-aggregation.md** | "Take all these data sets, cross reference them" | Discogs + MusicBrainz + the system adapters |
| **confidence-scoring.md** | "Present data that is 90 to 100% confident" | Conformal prediction, calibrated thresholds |
| **chat-interface.md** | "Chat interface to help fill in the gaps conversationally" | Two-role: gather/edit + query |
| **source-attribution.md** | "Low confidence relates to a particular source" | Per-source confidence breakdown |
| **gap-analysis.md** | "Suggest reaching out to relevant people" | Identify who could verify missing data |
| **mcp-server.md** | "MCP ready the system for third-party services" | ChatGPT, Mogen integration |

### Medium Priority (Post-MVP)

| Sub-PRD | Imogen/Andy Quote | Technical Implication |
|---------|-------------------|----------------------|
| **permission-bundles.md** | "How Mogen would get permission from the system" | AI consent management |
| **album-workflow.md** | "One album at a time or easiest ones first" | Progressive disclosure UX |
| **fun-ux.md** | "Make it fun somehow through conversation" | Gamification, progress tracking |

### Medium Priority (Parallel Track)

| Sub-PRD | Reason |
|---------|--------|
| **voice-agent/** | Serves dual purpose: (1) the attribution, (2) Imogen digital twin - connected business case |
| **langgraph-orchestration.md** | May be overkill - "vibe coded with Claude" acceptable, evaluate as needed |

---

## Part 8: Andy's Nuanced Thought → Technical Architecture

Andy's key insight: **"How we deal with the other stuff"** (low-confidence data)

### Proposed Technical Solution

```
User Query: "Show me my discography"
    ↓
┌─────────────────────────────────────────────────────────────┐
│ CONFIDENCE TRIAGE SYSTEM                                     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  HIGH CONFIDENCE (≥90%)                                     │
│  ├─ Auto-populate fields                                    │
│  └─ Green checkmarks in UI                                  │
│                                                             │
│  MEDIUM CONFIDENCE (70-90%)                                 │
│  ├─ Show with yellow indicator                              │
│  ├─ Source: "MusicBrainz says X, Discogs says Y"            │
│  └─ Prompt: "Which is correct?"                             │
│                                                             │
│  LOW CONFIDENCE (<70%)                                      │
│  ├─ Show gap indicator                                      │
│  ├─ Source analysis: "Only Discogs has this, no other source" │
│  ├─ Suggestion: "Could you verify? Or reach out to [collaborator]?" │
│  └─ Chat prompt: "Tell me about your role on this track"    │
│                                                             │
│  NO DATA                                                    │
│  ├─ Explicit gap                                            │
│  └─ Chat-driven data gathering                              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Sub-PRD: source-attribution.md (NEW)

**Purpose**: Track which sources contribute to confidence, identify systematic gaps

```python
class SourceAttribution:
    """Per-field source tracking for confidence analysis."""

    sources: dict[str, SourceContribution]  # {"discogs": {...}, "musicbrainz": {...}}
    agreement_score: float  # How much sources agree
    gap_analysis: GapAnalysis  # Which sources are missing

    def suggest_action(self) -> str:
        if self.single_source_only:
            return f"Only {self.sole_source} has this data. Can you verify?"
        if self.sources_disagree:
            return f"Sources disagree: {self.format_disagreement()}"
        if self.no_sources:
            return "No data found. Tell me about this."
```

### Sub-PRD: gap-analysis.md (NEW)

**Purpose**: Identify actionable next steps for missing data

```python
class GapAnalysis:
    """Analyze data gaps and suggest remediation."""

    missing_fields: list[str]
    potential_contributors: list[Person]  # Collaborators who might know
    suggested_actions: list[Action]  # "Reach out to X", "Check liner notes"

    def prioritize_gaps(self) -> list[Gap]:
        """Sort gaps by importance and ease of filling."""
        return sorted(self.gaps, key=lambda g: (g.importance, -g.difficulty))
```

---

## Conclusion

The self-reflection reveals that the original PRD plan is sound but needs:

1. **LLM Context sections** for AI-assisted development
2. **Explicit negative prompts** for commonly-suggested-but-rejected technologies
3. **Uncertainty Quantification** elevated to architectural principle (not just feature)
4. **TOC naming convention** for consistency with existing documentation
5. **Implementation examples** in every L3 PRD

The documentation review confirms the PostgreSQL-centric, observability-first approach aligns with proven patterns from uad-copilot and dpp-agents.

**Next Step**: Implement Phase 1 of the PRD restructuring with these adjustments incorporated.
