# Hierarchical Composable PRD Architecture Plan

**Status**: Ready for Implementation
**Created**: 2026-02-04
**Decisions Finalized**: 2026-02-04
**Purpose**: Transform flat PRD structure into multi-hypothesis, composable hierarchy inspired by Hydra config composition

---

## Executive Summary

This plan proposes restructuring the Music Attribution PRD system from a **flat hierarchy** (vision → components) to a **composable tree structure** with:

1. **Human-readable main PRD** (L1) - Vision and strategy
2. **Domain sub-PRDs** (L2) - Feature areas with option branches
3. **Implementation sub-PRDs** (L3) - Specific technology choices with trade-offs
4. **Cross-cutting concerns** - Observability, evals, infrastructure that span branches
5. **Negative prompts** - Explicit "why not X" documentation for rejected options

The goal: Enable **progressive disclosure** for LLM context engineering—an agent working on voice should not need to read GraphRAG details, only the relevant branch plus cross-cutting concerns.

---

## 1. Current State Analysis

### 1.1 Existing Structure

```
docs/prd/
├── vision-v1.md      # L1: Master vision (human + LLM)
├── attribution-engine-prd.md   # L2: Component PRD
├── chat-interface-prd.md       # L2: Component PRD
├── mcp-server-prd.md           # L2: Component PRD
├── SYNTHESIS.md                # Cross-cutting decisions
└── README.md                   # Index
```

**Issues with Current Structure**:
- All PRDs at same depth (no L3 implementation options)
- No multi-hypothesis branching (single path assumed)
- No "negative prompts" documenting rejected alternatives
- Cross-cutting concerns (evals, observability) not explicitly structured
- LLM must read entire PRD to understand any decision

### 1.2 Target Structure (Hydra-Inspired)

```
docs/prd/
├── defaults.yaml                    # Current active composition
├── vision-v1.md            # L1: Human-readable master
│
├── voice-agent/                     # L2: Domain branch
│   ├── _index.md                    # Branch summary + decision matrix
│   ├── pipeline/
│   │   ├── vapi.md                  # L3: Managed option
│   │   ├── pipecat.md               # L3: Self-hosted option
│   │   └── retell.md                # L3: Alternative (rejected)
│   ├── tts/
│   │   ├── inworld.md
│   │   ├── elevenlabs.md
│   │   └── cartesia.md
│   └── stt/
│       ├── deepgram.md
│       └── assemblyai.md
│
├── data-layer/                      # L2: Domain branch
│   ├── _index.md
│   ├── graph/
│   │   ├── neo4j.md                 # L3: NOT RECOMMENDED
│   │   ├── apache-age.md            # L3: Preferred (pg extension)
│   │   └── pgvector-only.md         # L3: MVP option
│   └── vector/
│       ├── pgvector.md
│       └── dedicated-vdb.md         # Pinecone, Weaviate (rejected)
│
├── observability/                   # Cross-cutting (L2*)
│   ├── _index.md
│   ├── langfuse.md                  # Applies to voice + LLM
│   └── prometheus-grafana.md
│
├── evals/                           # Cross-cutting (L2*)
│   ├── _index.md
│   ├── braintrust.md                # General LLM evals
│   ├── voice-evals.md               # Domain-specific
│   └── attribution-evals.md         # Domain-specific
│
└── REJECTED.md                      # Master "negative prompt" index
```

---

## 2. Core Concepts

### 2.1 Composition Model (Hydra-Inspired)

**defaults.yaml** defines the current active configuration:

```yaml
# defaults.yaml - Current active PRD composition
composition:
  vision: vision-v1

  voice_agent:
    pipeline: vapi           # Could override to pipecat
    tts: inworld            # Could override to elevenlabs
    stt: deepgram

  data_layer:
    graph: apache-age       # NOT neo4j
    vector: pgvector

  observability:
    - langfuse              # Cross-cutting, always included
    - prometheus-grafana

  evals:
    - braintrust            # General
    - voice-evals           # Domain-specific
```

**Override example** (different project variant):

```yaml
# overrides/scale-mode.yaml
voice_agent:
  pipeline: pipecat         # Self-hosted for cost at scale
  tts: cartesia            # Lower latency
```

### 2.2 Progressive Disclosure for LLMs

**Principle**: An LLM working on task X should receive:
1. L1 vision summary (always, ~500 tokens)
2. Relevant L2 domain index (path to X)
3. Relevant L3 implementation details
4. Cross-cutting concerns that apply to X
5. NOT: unrelated branches

**Example: Voice agent development context**

```
CONTEXT WINDOW:
├── vision-v1.md#executive-summary     (~500 tokens)
├── voice-agent/_index.md                       (~1000 tokens)
├── voice-agent/pipeline/vapi.md                (~2000 tokens)
├── voice-agent/tts/inworld.md                  (~1500 tokens)
├── observability/langfuse.md#voice-integration (~500 tokens)
├── evals/voice-evals.md                        (~1000 tokens)
└── REJECTED.md#voice-agent                     (~300 tokens) - WHY NOT neo4j, etc.

TOTAL: ~6800 tokens (not 50K+ for full PRD tree)
```

### 2.3 Negative Prompts

**Purpose**: Prevent LLMs from repeatedly suggesting rejected options

**Format per rejected option**:

```markdown
## neo4j (data-layer/graph)

**Status**: NOT RECOMMENDED
**Last Evaluated**: 2026-02-04
**May Reconsider If**: Project requires native Cypher queries, graph algorithms at scale

### Why Rejected

1. **Operational Complexity**: Separate database to manage vs. PostgreSQL extension
2. **Cost**: Neo4j Aura pricing vs. free Apache AGE on existing Postgres
3. **Team Expertise**: No Neo4j experience, strong Postgres knowledge
4. **Migration Risk**: Would require data model changes if we later want relational joins

### When neo4j WOULD Be Right

- Native graph traversal algorithms (PageRank, community detection)
- Graph-first data model (not relational with graph extensions)
- Enterprise budget for managed service

### Reference

- Evaluation doc: knowledge-base/technical/databases/neo4j-evaluation.md
- Decision date: 2026-02-04
```

### 2.4 Cross-Cutting Concern References

Cross-cutting concerns use **forward references** in domain PRDs:

```markdown
<!-- In voice-agent/_index.md -->

## Observability

This domain uses the shared observability stack:
- **LLM Tracing**: See [observability/langfuse.md](../observability/langfuse.md)
- **System Metrics**: See [observability/prometheus-grafana.md](../observability/prometheus-grafana.md)

### Voice-Specific Extensions

Langfuse integration for voice includes:
- Persona drift scoring (custom metric)
- Per-turn latency attribution
- TTS/STT cost breakdown

For full implementation: [observability/langfuse.md#voice-agent-integration](../observability/langfuse.md#voice-agent-integration)
```

---

## 3. Implementation Plan

### Phase 1: Structure Migration

1. Create directory structure
2. Extract L3 options from existing large PRDs
3. Write `_index.md` for each L2 domain
4. Create initial `defaults.yaml`
5. Write `REJECTED.md` skeleton

### Phase 2: Content Optimization

1. Optimize L2 indexes for LLM scanning (headers, tables, decision matrices)
2. Add "Quick Reference" sections to L3 docs
3. Create cross-reference links
4. Write negative prompts for known rejections (neo4j, etc.)

### Phase 3: Context Engineering Tooling

1. Script to assemble context for specific task types
2. Integration with Claude Code knowledge base
3. Validation that all L3 options have decision rationale

---

## 4. Open Questions for Clarification

See [Questions](#6-clarifying-questions) section below.

---

## 5. Success Criteria (Revised per Imogen/Andy Vision)

| Criteria | Measurement | Target |
|----------|-------------|--------|
| **Confidence-first clarity** | PRDs clearly define 90/70/low confidence thresholds | Thresholds documented in uncertainty/calibration.md |
| **Source attribution** | Every confidence score traceable to source contributions | source-attribution.md complete |
| **Gap analysis actionable** | Low-confidence data suggests remediation actions | gap-analysis.md with action taxonomy |
| **Multi-tenant ready** | Security PRDs cover data isolation patterns | security/multi-tenancy.md complete |
| Progressive disclosure | LLM can work on attribution without reading MCP details | Attribution context < 8K tokens |
| Negative prompts effective | Claude stops suggesting neo4j after reading context | Zero neo4j suggestions post-implementation |
| Composition clarity | `defaults.yaml` accurately represents current active choices | 100% accuracy on active/rejected status |
| Cross-cutting emergence | High-reference docs automatically identified as cross-cutting | Langfuse, UQ referenced by 3+ domains |
| Context assembly | Frontmatter `requires` graph produces valid context | Script validates all paths resolve |
| Changelog discipline | All PRDs have version history | 100% changelog coverage |
| Schema compliance | All frontmatter validates against schema.yaml | Zero validation errors |

---

## 6. Decisions Made

*Clarified 2026-02-04*

### D1: Hierarchy Depth → **Shallow (3 levels max)**

```
docs/prd/
├── vision-v1.md           # L1
├── voice-agent/                    # L2
│   ├── _index.md
│   └── tts/inworld.md              # L3 (max depth)
```

**Rationale**: Simpler navigation, easier maintenance. No `voice-agent/tts/providers/inworld/voices/nel-warm.md` deep nesting.

### D2: Negative Prompts → **Brief + Adaptive Detail References**

**Default**: 3-5 bullet summary (why rejected, when to reconsider)

**Adaptive extension**: For substantive technical decisions (e.g., neo4j vs pgvector), link to detailed evaluation doc in knowledge-base:

```markdown
## neo4j (data-layer/graph)

**Status**: NOT RECOMMENDED
**Last Evaluated**: 2026-02-04
**Detailed Analysis**: [knowledge-base/technical/databases/neo4j-vs-pgvector-evaluation.md](...)

### Brief Summary (3-5 bullets)
1. Operational complexity vs PostgreSQL extension
2. Cost (Neo4j Aura vs free Apache AGE)
3. Team expertise gap
4. Migration risk for relational joins
```

For subjective/UX decisions (e.g., Railway vs Render), brief summary suffices without deep analysis.

### D3: Cross-Cutting Concerns → **Knowledge Graph Model**

**Shift from categorical to emergent**: Instead of predetermining "these are cross-cutting", treat the PRD structure as a **knowledge graph with hierarchical backbone**:

```yaml
# Relationships emerge from content, not predetermined categories
graph_model:
  backbone: hierarchical         # L1 → L2 → L3
  edges: bidirectional_references  # Any doc can reference any other
  cross_cutting_detection: data_driven  # Emerges from reference frequency

  # User priors for likely cross-cutting concerns:
  priors:
    high_probability:
      - observability/langfuse.md
      - evals/braintrust.md
      - infrastructure/render-vs-hetzner.md
    medium_probability:
      - auth/oauth-patterns.md
      - error-handling/retry-patterns.md
```

**Implementation**: Use bidirectional links (`[[wiki-style]]` or explicit markdown links) and let cross-cutting nature emerge from reference patterns. A doc referenced by 5+ domains is de facto cross-cutting.

### D4: Version Tracking → **Changelog Sections**

Each PRD includes embedded changelog:

```markdown
## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 0.3.0 | 2026-02-04 | Added Cartesia TTS option |
| 0.2.0 | 2026-01-15 | Switched from ElevenLabs to Inworld as default |
| 0.1.0 | 2026-01-01 | Initial draft |
```

**Trade-off accepted**: Docs grow over time, but self-contained history is valuable for understanding decision evolution.

### D5: Composition Tooling → **Frontmatter-Driven**

Each PRD declares its context dependencies in YAML frontmatter:

```yaml
---
# voice-agent/tts/inworld.md
id: voice-agent/tts/inworld
title: Inworld TTS Integration
status: active  # active | deprecated | experimental
version: 0.2.0

# Context assembly for LLMs
requires:
  - vision-v1.md#executive-summary    # Always load vision summary
  - voice-agent/_index.md                       # Parent domain context

cross_refs:
  - observability/langfuse.md#voice-integration # Related cross-cutting
  - evals/voice-evals.md#tts-quality           # Related evals

alternatives:
  - voice-agent/tts/elevenlabs.md              # Sibling options
  - voice-agent/tts/cartesia.md

rejection_of: null  # If this doc is a "why not X", reference X here
---
```

**Benefits**:
- Self-describing: Each doc declares what context it needs
- Portable: Works with any tool that can parse YAML frontmatter
- Composable: Assemble context by walking `requires` graph
- Explicit alternatives: LLM knows sibling options exist

---

## 7. Finalized Target Structure (Revised per Imogen/Andy Input)

**Key Insight from Andy**: Focus on confidence-first UX and source attribution for low-confidence data

```
docs/prd/
├── defaults.yaml                    # Current active composition
├── schema.yaml                      # Frontmatter schema definition
├── llm-context.md                   # System prompt for AI assistants (NEW)
│
├── toc-prd.md                       # Main PRD index (renamed from README.md)
├── vision-v1.md            # L1: Human-readable master
│
├── attribution-engine/              # L2: CORE DOMAIN (HIGH PRIORITY)
│   ├── toc-attribution-engine.md
│   ├── multi-source-aggregation.md  # Discogs + MusicBrainz + system own
│   ├── confidence-scoring.md        # "90-100% confident" per Imogen
│   ├── source-attribution.md        # NEW: Per-source confidence (Andy's insight)
│   ├── gap-analysis.md              # NEW: "Suggest reaching out" (Andy)
│   └── conflict-resolution.md       # When sources disagree
│
├── chat-interface/                  # L2: USER INTERFACE (HIGH PRIORITY)
│   ├── toc-chat-interface.md
│   ├── data-gathering-mode.md       # Role 1: Gather/edit data
│   ├── query-mode.md                # Role 2: External users query
│   ├── conversational-gap-filling.md  # "Fill in gaps conversationally"
│   └── album-workflow.md            # "One album at a time"
│
├── mcp-server/                      # L2: API LAYER (HIGH PRIORITY)
│   ├── toc-mcp-server.md
│   ├── read-api.md                  # Query attribution data
│   ├── write-api.md                 # Contribute/edit data
│   └── permissions-api.md           # "How Mogen gets permission"
│
├── data-layer/                      # L2: Infrastructure
│   ├── toc-data-layer.md
│   ├── graph/
│   │   ├── apache-age.md            # Preferred (pg extension)
│   │   └── neo4j.md                 # NOT RECOMMENDED
│   ├── vector/
│   │   ├── pgvector.md              # Preferred (unified DB)
│   │   └── dedicated-vdb.md         # NOT RECOMMENDED
│   └── hybrid-retrieval.md          # Cross-reference pattern
│
├── voice-agent/                     # L2: Voice interface
│   ├── toc-voice-agent.md
│   ├── pipeline/
│   │   ├── vapi.md                  # Managed (fast iteration)
│   │   └── pipecat.md               # Self-hosted (scale)
│   ├── tts/
│   │   ├── inworld.md               # Primary (cost-effective)
│   │   └── elevenlabs.md            # Alternative (quality)
│   └── stt/
│       └── deepgram.md              # Primary (low latency)
│   # NOTE: Voice agent serves DUAL purposes:
│   # 1. the attribution (conversational data gathering)
│   # 2. Imogen digital twin (connected business case)
│
├── identity-permissions/            # L2: Business logic
│   ├── toc-identity-permissions.md
│   ├── artist-id.md                # Self-sovereign identity
│   └── permission-bundles.md        # AI consent management
│
├── observability/                   # L2*: Cross-cutting
│   ├── toc-observability.md
│   ├── langfuse.md                  # LLM tracing (confidence tracking)
│   └── prometheus-grafana.md        # System metrics
│
├── uncertainty/                     # L2*: ARCHITECTURAL PRINCIPLE
│   ├── toc-uncertainty.md
│   ├── conformal-prediction.md      # Formal guarantees
│   ├── calibration.md               # "90-100% confident" accuracy
│   └── selective-prediction.md      # When to abstain
│
├── security/                        # L2*: Cross-cutting
│   ├── toc-security.md
│   ├── multi-tenancy.md             # Rights orgs, labels isolation
│   └── audit-logging.md             # Who changed what
│
├── infrastructure/                  # L2*: Cross-cutting
│   ├── toc-infrastructure.md
│   ├── render.md                    # Primary (simplicity)
│   └── neon.md                      # PostgreSQL hosting
│
└── REJECTED.md                      # Master rejection index
```

**Note**: `voice-agent/` serves dual purposes: (1) the attribution via conversational data gathering, (2) Imogen digital twin - these are connected business cases sharing infrastructure.

---

## 8. Implementation Roadmap (Revised per Imogen/Andy Input)

### Phase 1: Foundation + Core Domain (Week 1)

**Tasks**:
1. Create directory structure per Section 7 (revised)
2. Define `schema.yaml` for frontmatter validation
3. Create `llm-context.md` with system prompt for AI assistants
4. Write `toc-*.md` templates (not `_index.md`)
5. **Start HIGH PRIORITY PRDs**:
   - `attribution-engine/multi-source-aggregation.md`
   - `attribution-engine/confidence-scoring.md`

**Deliverables**:
- [ ] Directory structure created
- [ ] Schema definition complete
- [ ] LLM context document written
- [ ] Two core PRDs drafted

### Phase 2: Andy's Insights + Chat Interface (Week 2)

**Tasks**:
1. **Source Attribution** (Andy's key insight):
   - `attribution-engine/source-attribution.md`
   - `attribution-engine/gap-analysis.md`
2. **Chat Interface**:
   - `chat-interface/toc-chat-interface.md`
   - `chat-interface/conversational-gap-filling.md`
3. Create `REJECTED.md` with neo4j entry (detailed rationale)

**Deliverables**:
- [ ] Source attribution PRD complete
- [ ] Gap analysis PRD complete
- [ ] Chat interface PRDs drafted
- [ ] REJECTED.md with neo4j entry

### Phase 3: MCP + Uncertainty Architecture (Week 3)

**Tasks**:
1. **MCP Server** (for ChatGPT/Mogen integration):
   - `mcp-server/toc-mcp-server.md`
   - `mcp-server/permissions-api.md`
2. **Uncertainty as Architecture**:
   - `uncertainty/toc-uncertainty.md`
   - `uncertainty/conformal-prediction.md`
3. Add cross_refs to all domain PRDs

**Deliverables**:
- [ ] MCP PRDs complete (Mogen integration path clear)
- [ ] Uncertainty PRDs complete
- [ ] Cross-reference graph validated

### Phase 4: Cross-Cutting + Tooling (Week 4)

**Tasks**:
1. Create observability/ branch with Langfuse (confidence tracking)
2. Create security/ branch with multi-tenancy (per user answer)
3. Write Python script to parse frontmatter and assemble context
4. Add `defaults.yaml` with final active choices
5. Validate progressive disclosure (<10K tokens for attribution context)

**Deliverables**:
- [ ] Observability PRDs complete
- [ ] Security/multi-tenancy PRDs complete
- [ ] `scripts/prd-context.py` working
- [ ] Context assembly validation passing

---

## 9. Frontmatter Schema Definition

```yaml
# schema.yaml - PRD frontmatter schema
type: object
required:
  - id
  - title
  - status
  - version
  - requires

properties:
  id:
    type: string
    description: Unique path-based identifier (e.g., "voice-agent/tts/inworld")

  title:
    type: string
    description: Human-readable title

  status:
    type: string
    enum: [active, deprecated, experimental, rejected]
    description: Current status of this option

  version:
    type: string
    pattern: "^\\d+\\.\\d+\\.\\d+$"
    description: Semantic version

  last_updated:
    type: string
    format: date
    description: Last modification date

  requires:
    type: array
    items:
      type: string
    description: PRDs that MUST be loaded for context (with optional #section)

  cross_refs:
    type: array
    items:
      type: string
    description: Related PRDs (optional context enrichment)

  alternatives:
    type: array
    items:
      type: string
    description: Sibling options in same decision space

  rejection_of:
    type: string
    nullable: true
    description: If this is a rejection doc, what option it rejects

  rejection_detail:
    type: string
    nullable: true
    description: Path to detailed evaluation doc (for substantive rejections)

  tags:
    type: array
    items:
      type: string
    description: Freeform tags for discovery

  changelog:
    type: array
    items:
      type: object
      properties:
        version: { type: string }
        date: { type: string, format: date }
        changes: { type: string }
```

---

## 10. Example: Fully Specified PRD

```markdown
---
id: voice-agent/tts/inworld
title: Inworld TTS Integration
status: active
version: 0.2.0
last_updated: 2026-02-04

requires:
  - vision-v1.md#executive-summary
  - voice-agent/_index.md

cross_refs:
  - observability/langfuse.md#voice-integration
  - evals/voice-evals.md#tts-quality
  - infrastructure/hetzner.md#latency-requirements

alternatives:
  - voice-agent/tts/elevenlabs.md
  - voice-agent/tts/cartesia.md

rejection_of: null
rejection_detail: null

tags:
  - tts
  - voice
  - latency-critical
  - cost-optimized

changelog:
  - version: "0.2.0"
    date: 2026-02-04
    changes: "Added emotion markup support, updated pricing"
  - version: "0.1.0"
    date: 2026-01-15
    changes: "Initial evaluation"
---

# Inworld TTS Integration

## Quick Reference

| Aspect | Value |
|--------|-------|
| **Provider** | [Inworld AI](https://inworld.ai/tts) |
| **Cost** | $5/1M characters |
| **Latency** | <250ms TTFB |
| **Status** | Active - Primary TTS |

## Why Inworld

1. **Cost**: 6× cheaper than ElevenLabs
2. **Quality**: #1 on TTS Arena benchmarks
3. **Latency**: Sub-250ms, critical for voice UX
4. **Emotion**: Native emotion markup support

## When to Reconsider

- If latency requirements drop below 100ms → evaluate Cartesia
- If custom voice cloning needed → evaluate ElevenLabs
- If cost ceiling increases → more options viable

## Integration

See [voice-agent-tech-prd.md Section 5.1](../../../dpp-agents/knowledge-base/documentation/prd/voice-agent-tech-prd.md#51-inworld-tts-integration-primary) for implementation details.

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 0.2.0 | 2026-02-04 | Added emotion markup support |
| 0.1.0 | 2026-01-15 | Initial evaluation |
```

---

## Appendix A: Original User Prompt (Verbatim)

> Can we work next on a plan how to improve our PRD here: /home/petteri/Dropbox/github-personal/music-attribution-scaffold/docs/prd . Let's create a plan to /home/petteri/Dropbox/github-personal/music-attribution-scaffold/docs/planning/prd-improvement-for-hierarchical-composable-plan.md on how to make it more multi-hypothesis and more suitable for this open-ended product design planning phase in which the only high-level vision of this product and project (the-attribution-system) is known, but the there are a lot of options for the low-level implementation then. COuld we take inspiration from https://hydra.cc/docs/0.11/tutorial/composition/ in which we can add now a third level to the config hierarchy. There is now a main-level PRD, 2-nd level PRD e.g. for voice-agent options, and then depeding how you want to design the PRD tree hierarchy, the sub-PRD could talk about different voice architectures (see e.g. /home/petteri/Dropbox/github-personal/dpp-agents/knowledge-base/documentation/prd/voice-agent-tech-prd.md that is already quite big, and could be composed into .yaml pieces, right? e.g. Elevanlabs sub-PRD, inworld TTS sub-PRD. different sub-PRD for Vapi for the pipeline? Then LangFuse is more "around the PRD tree-type of piece" that could be referenced across the PRD hierarchy right? As it could work both for text-based LLMs and then the voice agents! And how do voice-agent evals work? If we have Braintrust for "general LLM evals", and should there be evals sub-config that again cross-references this "evals" main config with voice agent and llm evals as sub-evals PRDs? The main-level PRD should be mostly for human reading with the sub-PRDs then mostly for LLM Context engineering and they should be optimized for LLM use so that the PRD would be crystal clear for progressive disclosure type of smart traversing through the "graph" with you not needing to read the whole PRD hierarchy to get an idea! E.g. if we would be working on just the voice agent development, should we need to know about all the other sub-PRDs (only the high-level PRD on the main vision)? What do you say. Same goes e.g. for GraphRAG for example with neo4j sub-PRD and the simpler postgresql/pgvector sub-PRD. So all the options we would have ever considered would be on this PRD structure? For example, you often like to offer neo4j whereas I am not interested in using that and there should be clear "negative prompt" in the PRD tree why we think that at the moment neo4j should not be sugggested? But then we should have the "full scope" of all the options, as if an "input specifications" change a bit, then a whole new PRD combination would make more sense, right? Continuous PRD optimization-type of scenario based on living specifications as we are a startup so the world is quite dynamic and quickly changing. Could you start the planning by saving this prompt as verbatim to the appendix, and then LLM-optimized prompt as a second appendix from my rambling so that it is more concise and optimized for LLM use. Then do the initial planning, and ask me then further multi-answer questions from me to clarify any uncertainties in the plan

---

## Appendix B: LLM-Optimized Prompt

### Context

Transform flat PRD structure into Hydra-inspired composable hierarchy for open-ended product design with multi-hypothesis branching.

### Requirements

1. **Three-level hierarchy**:
   - L1: Human-readable master vision
   - L2: Domain sub-PRDs (voice-agent, data-layer, etc.)
   - L3: Implementation options (Vapi vs Pipecat, neo4j vs pgvector)

2. **Cross-cutting concerns**: Observability (Langfuse), Evals (Braintrust + domain-specific) span multiple branches

3. **Negative prompts**: Explicitly document WHY options are rejected (e.g., "neo4j NOT RECOMMENDED because...") to prevent LLM suggestions of rejected choices

4. **Progressive disclosure**: LLM working on voice-agent should NOT need to read GraphRAG PRDs—only relevant branch + cross-cutting concerns

5. **Living specification**: Structure must support dynamic updates as startup pivots; changing one input could make different PRD combination optimal

### Constraints

- Main PRD: optimized for human reading
- Sub-PRDs: optimized for LLM context engineering
- Must enable smart graph traversal without reading full hierarchy
- All considered options documented (even rejected) for specification changes

### Inspiration

- Hydra config composition: defaults + overrides + config groups
- Example decomposition: voice-agent-tech-prd.md → pipeline/, tts/, stt/ sub-PRDs

### Deliverable

Plan for PRD restructuring with directory structure, composition model, and implementation phases.

---

## Appendix C: Reference Documents

- **Hydra Composition**: https://hydra.cc/docs/0.11/tutorial/composition/
- **Example Large PRD**: `/home/petteri/Dropbox/github-personal/dpp-agents/knowledge-base/documentation/prd/voice-agent-tech-prd.md`
- **Current PRD Structure**: `/home/petteri/Dropbox/github-personal/music-attribution-scaffold/docs/prd/`
