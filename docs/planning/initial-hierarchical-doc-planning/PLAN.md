# Hierarchical Documentation & Knowledge Management Plan

**Status**: Draft v6 - Final (FinOps Optimization Added)
**Created**: 2026-02-03
**Updated**: 2026-02-03
**Branch**: feat/initial-prd
**Reviewers**: Architecture (a29a0d7), UQ Research (afb1470), Implementation Feasibility (a60282d)

---

## Executive Summary

This plan proposes a **Minimum Viable Architecture (MVA)** for the system documentation and knowledge management that:
1. Scales from MVP sprint to production platform
2. Enables token-efficient context engineering for Claude Code
3. Supports semantic search and retrieval-as-service (PostgreSQL + pgvector)
4. Organizes both domain knowledge (music attribution) and technical knowledge (AI/RAG trends)
5. Implements progressive disclosure like Claude Skills
6. Establishes foundation for uncertainty quantification & GEO provenance
7. **NEW**: Remains flexible as AI/ML landscape rapidly evolves

> **MVA Philosophy** (from InfoQ): *"Just enough architecture to meet known Quality Attribute Requirements. Delay design decisions until absolutely necessary. Avoid over-investing: solve current challenges while anticipating but not actually solving future challenges."*

**Recommendation**: Option A (Pure Markdown) with Option 3 knowledge base structure (SYNTHESIS.md pattern).

### Key Decisions (Resolved)

| Question | Decision | Rationale |
|----------|----------|-----------|
| Graph database | PostgreSQL + pgvector only | Neo4j is overkill for sprint; pgvector handles similarity search. Document graph query patterns that may require upgrade later (ADR). |
| Documentation format | Pure Markdown | No LaTeX needed; .md is sufficient |
| Mogen integration | Separate project | The system provides RAG-like data source; voice interface is out of scope |
| Confidence scoring | Own research project | Does not need to follow A0-A3; connects to GEO provenance & agentic commerce. Use MAPIE for conformal prediction. |
| AI frameworks | Pure Python + Pydantic | Avoid LangChain complexity; use LangGraph only if needed for control flow |
| Frontmatter validation | Pre-commit + CI/CD | Both: pre-commit for immediate feedback, CI/CD for enforcement |

### Architecture Flexibility Principles

1. **Anticipate change, don't solve for it**: Document what might change, but don't implement until needed
2. **Thin integration layers**: Keep domain logic separate from framework-specific code
3. **Explicit upgrade criteria**: Define thresholds that trigger architectural evolution
4. **4-week cycles**: Build fast, measure, iterate (Platform Engineering MVP pattern)

---

## Table of Contents

1. [Research Findings Summary](#1-research-findings-summary)
2. [Documentation Architecture Options](#2-documentation-architecture-options)
3. [Knowledge Base Structure Options](#3-knowledge-base-structure-options)
4. [PRD System Design](#4-prd-system-design)
5. [Progressive Disclosure Implementation](#5-progressive-disclosure-implementation)
6. [Semantic Search & Retrieval](#6-semantic-search--retrieval)
7. [Uncertainty Quantification & GEO Provenance](#7-uncertainty-quantification--geo-provenance)
8. [Recommended Architecture](#8-recommended-architecture)
9. [Implementation Roadmap](#9-implementation-roadmap)
10. [Open Questions](#10-open-questions)
11. [Data Warehouse Architecture](#11-data-warehouse-architecture-new---v4) ← v4
12. [Mogen Integration & Voice Architecture](#12-mogen-integration--voice-architecture-new---v6) ← **NEW v6**

---

## 1. Research Findings Summary

### 1.1 From dpp-agents Knowledge Base Analysis

**Strengths identified**:
- 692 markdown files organized into 17 semantic themes
- Progressive disclosure via README at each directory level
- Role-based navigation (Business/Developers/Researchers)
- Frontmatter metadata for RAG indexing (44% adoption)
- Explicit cross-references in every theme README

**Weaknesses identified**:
- Inconsistent frontmatter adoption (only 44%)
- Multiple naming conventions in transition
- Legacy folder growing without clear categorization
- SYNTHESIS.md files mostly missing (planned but not implemented)
- PRD vs product-strategy overlap

### 1.2 From dpp-agents PRD System

**Effective patterns**:
- 8 PRDs totaling ~8,000 lines with consistent template
- 4-level progressive disclosure (Executive → Problem → Technical → Deep)
- Document lineage tracking (v2 synthesizes v1 + research inputs)
- Decision matrices for technology choices
- Cost/benefit analysis in every PRD
- Cross-references via relative paths

**Template structure** (12 sections):
1. Metadata Header
2. Executive Summary
3. Table of Contents
4. Problem Statement
5. Product Vision
6. Architecture/Technical Details
7. Implementation Roadmap
8. Resourcing & Budget
9. Success Metrics
10. Risks & Dependencies
11. Cross-References
12. Appendices

### 1.3 From sci-llm-writer LaTeX Hierarchy

**Key patterns**:
- Master aggregator pattern (`00-overview.tex` composes all)
- 3-level nesting: Master → Domain → Section
- Numbered file sequencing (01, 02...99)
- `_README.md` at each domain level for metadata
- `_chapter.tex` as nested aggregators
- `99-synthesis.tex` or `99-takeaways.tex` for meta-summaries
- Thesis statement opens each file

**Statistics**:
- ~70 .tex files across 6 domains
- 109 figures with consistent naming (`fig-{chapter}-{section}-{descriptor}.png`)
- Academic narrative prose (80-250 word paragraphs)
- Citations woven into prose, not listed

### 1.4 From Meta-Learning Documents

**Critical lessons**:
1. **50 lines > 5×10 lines**: Consolidation prevents context fragmentation
2. **Explore before create**: Check existing configs/code before proposing new
3. **Runtime enforcement > prose documentation**: Rules that fail loudly work
4. **Single source of truth**: Duplication causes conflicting anchors
5. **AIDEV-NOTE comments**: Travel with code during refactors
6. **3-click rule**: Any concept reachable in ≤3 navigation steps

**Hallucination prevention**:
- STOP → EXPLORE → VERIFY → PROPOSE (never reverse)
- Mandatory verification checklist before creating anything
- Red flags: "representative combos", "best performing", "options available"

### 1.5 From Music Domain Analysis

**Core domain concepts for the system**:
- Attribution Framework (A0–A3 assurance levels)
- Oracle Problem (epistemic limits on verification)
- Friction Taxonomy (administrative vs. discovery)
- Agent Archetypes (BYO vs. Bowling-Shoe)
- Deterrence Economics (p × d × F ≥ g)

**Entity types needed**:
- Creator, Work, Recording, Rights, Claim
- Certifier, Evidence, Watermark, Forensic
- Agent, Permission, License, Audit
- Transaction, Platform, Deterrence, Mechanism

---

## 2. Documentation Architecture Options

### Option A: Pure Markdown Hierarchy (dpp-agents style)

```
docs/
├── README.md                    # Master navigation
├── prd/                         # Product requirements
│   ├── README.md
│   ├── vision-v1.md
│   ├── attribution-engine-prd.md
│   └── chat-interface-prd.md
├── knowledge-base/              # Domain + technical knowledge
│   ├── README.md
│   ├── domain/                  # Music industry
│   └── technical/               # AI/RAG trends
├── architecture/                # Technical decisions
├── planning/                    # Strategic planning
└── team/                        # Meetings, decisions
```

**Pros**:
- Simple tooling (any editor, Git-friendly)
- Native to Claude Code workflows
- Easy semantic search indexing
- Familiar to developers

**Cons**:
- No compilation to PDF for external sharing
- Tables/diagrams limited in markdown
- Academic citations harder to manage
- No figure numbering automation

### Option B: Hybrid LaTeX-Markdown Architecture

```
docs/
├── README.md                    # Master navigation (Markdown)
├── prd/                         # PRDs in Markdown
│   ├── README.md
│   └── *.md
├── knowledge-base/              # Research in LaTeX
│   ├── README.md                # Index (Markdown)
│   ├── domain/
│   │   ├── _README.md           # Domain overview
│   │   ├── 00-overview.tex      # Master aggregator
│   │   ├── attribution/
│   │   │   ├── 01-a0-a3-framework.tex
│   │   │   ├── 02-oracle-problem.tex
│   │   │   └── 99-synthesis.tex
│   │   └── economics/
│   │       └── *.tex
│   └── technical/
│       ├── _README.md
│       ├── 00-overview.tex
│       ├── rag/
│       ├── semantic-search/
│       └── agentic-systems/
├── architecture/                # ADRs in Markdown
└── .claude/                     # Claude Code context
    ├── CLAUDE.md
    ├── rules/
    └── domains/
```

**Pros**:
- LaTeX for academic-quality knowledge base (citations, figures)
- Markdown for operational docs (PRDs, ADRs)
- Can compile knowledge-base to PDF for external sharing
- Best of both worlds

**Cons**:
- More complex tooling (LaTeX + Markdown)
- Two syntaxes to maintain
- Knowledge base not directly indexable without conversion

### Option C: Obsidian-Style Knowledge Graph

```
docs/
├── README.md
├── prd/
├── knowledge-graph/             # Obsidian vault
│   ├── .obsidian/               # Obsidian config
│   ├── concepts/                # Atomic concept notes
│   │   ├── attribution-a0.md
│   │   ├── attribution-a1.md
│   │   ├── oracle-problem.md
│   │   └── ...
│   ├── sources/                 # Literature notes
│   │   ├── edge-2025-graph-rag.md
│   │   └── ...
│   ├── MOCs/                    # Maps of Content
│   │   ├── MOC-attribution.md
│   │   └── MOC-rag-systems.md
│   └── daily/                   # Daily notes
└── .claude/
```

**Pros**:
- True bidirectional linking (`[[concept]]` syntax)
- Graph visualization for relationships
- Atomic notes enable fine-grained retrieval
- Obsidian community plugins for academic work

**Cons**:
- Requires Obsidian tooling
- `[[wikilinks]]` not standard markdown
- Graph complexity grows fast
- May be overkill for sprint phase

---

## 3. Knowledge Base Structure Options

### Option 1: Flat Thematic (Current dpp-agents)

```
knowledge-base/
├── domain/
│   ├── attribution/
│   ├── music-industry/
│   ├── rights-management/
│   └── regulatory/
└── technical/
    ├── rag-systems/
    ├── semantic-search/
    ├── agentic-architecture/
    └── llmops/
```

**Pros**: Simple navigation
**Cons**: No progressive disclosure within themes

### Option 2: Academic Hierarchy (sci-llm-writer style)

```
knowledge-base/
├── domain/
│   ├── _README.md
│   ├── 00-overview.tex
│   ├── attribution/
│   │   ├── _README.md
│   │   ├── 01-framework-a0-a3.tex
│   │   ├── 02-oracle-problem.tex
│   │   ├── 03-verification-constraints.tex
│   │   └── 99-synthesis.tex
│   ├── economics/
│   │   ├── _README.md
│   │   ├── 01-friction-taxonomy.tex
│   │   ├── 02-deterrence-model.tex
│   │   └── 99-synthesis.tex
│   └── 99-domain-synthesis.tex
└── technical/
    ├── _README.md
    ├── 00-overview.tex
    ├── rag/
    │   ├── 01-vector-databases.tex
    │   ├── 02-graph-rag.tex      # Edge et al. 2025
    │   └── 99-synthesis.tex
    └── 99-technical-synthesis.tex
```

**Pros**:
- Progressive disclosure (overview → section → detail)
- Synthesis files aggregate knowledge
- Numbered sequencing shows progression

**Cons**:
- LaTeX learning curve
- Requires compilation workflow

### Option 3: Hybrid with Markdown Summaries (RECOMMENDED)

```
knowledge-base/
├── README.md                    # Quick navigation index
├── SYNTHESIS.md                 # Cross-domain synthesis
│
├── domain/
│   ├── README.md                # Domain overview table
│   ├── SYNTHESIS.md             # Domain synthesis
│   │
│   ├── attribution/
│   │   ├── README.md            # Section overview
│   │   ├── a0-a3-framework.md   # Core concepts
│   │   ├── oracle-problem.md
│   │   ├── verification-constraints.md
│   │   └── SYNTHESIS.md         # Section synthesis
│   │
│   ├── economics/
│   │   ├── README.md
│   │   ├── friction-taxonomy.md
│   │   ├── deterrence-model.md
│   │   └── SYNTHESIS.md
│   │
│   └── legal/
│       └── ...
│
├── technical/
│   ├── README.md
│   ├── SYNTHESIS.md
│   │
│   ├── rag/
│   │   ├── README.md
│   │   ├── vector-databases.md
│   │   ├── graph-rag.md         # Edge et al. 2025
│   │   ├── cursor-indexing.md   # Cursor blog insights
│   │   └── SYNTHESIS.md
│   │
│   ├── semantic-search/
│   ├── agentic-systems/
│   └── context-engineering/
│
└── sources/                     # Literature notes
    ├── README.md
    ├── edge-2025-graph-rag.md
    ├── netflix-2025-genai.md
    └── cursor-2026-indexing.md
```

**Pros**:
- All markdown (simple tooling)
- SYNTHESIS.md at each level enables RAG
- sources/ separates literature from synthesized knowledge
- README.md for navigation, SYNTHESIS.md for aggregation
- Can convert to LaTeX later if needed for publication

**Cons**:
- Manual citation management
- No automatic figure numbering

---

## 4. PRD System Design

### 4.1 PRD Hierarchy for the system

```
prd/
├── README.md                              # Navigation & lineage
│
├── vision-v1.md                  # MASTER: Consolidated vision
│   └── Synthesizes all below + domain research
│
├── attribution-engine-prd.md              # Core: Data cross-referencing
│   ├── Problem: 40%+ incorrect attribution
│   ├── Solution: Multi-source confidence scoring
│   └── Dependencies: data-sources, uncertainty-model
│
├── chat-interface-prd.md                  # UX: Conversational gap-filling
│   ├── Problem: Data entry is boring
│   ├── Solution: AI-assisted conversation
│   └── Dependencies: attribution-engine, llm-integration
│
├── mcp-server-prd.md                      # API: Third-party integration
│   ├── Problem: attribution data not accessible to agents
│   ├── Solution: MCP-ready API
│   └── Dependencies: attribution-engine, auth
│
└── mogen-integration-prd.md               # Extension: Digital twin
    ├── Problem: Personalized LLM context for artists
    ├── Solution: The system → Mogen data bridge
    └── Dependencies: mcp-server, permissions
```

### 4.2 PRD Template for the system

```markdown
# [Feature] PRD v[X.Y]

## Metadata
- **Version**: X.Y.Z
- **Status**: Draft | Ready | Implementing | Complete
- **Created**: YYYY-MM-DD
- **Updated**: YYYY-MM-DD
- **Author**: [name]
- **Lineage**: Synthesizes [list of predecessor docs]

## Executive Summary
<!-- 50-100 words, decision-maker level -->
- **What**: One-liner description
- **Why**: Business case in 3 bullets
- **Investment**: Effort estimate range
- **Confidence**: How certain is this spec?

## Table of Contents
<!-- Auto-generated or manual -->

## 1. Problem Statement
### 1.1 Current State
### 1.2 Pain Points
### 1.3 Market Opportunity
### 1.4 Regulatory Drivers

## 2. Product Vision
### 2.1 Vision Statement
### 2.2 Target Users
### 2.3 Success Definition

## 3. User Stories
<!-- By persona: Artist, Manager, Platform, Consumer -->

## 4. Technical Architecture
### 4.1 System Design
### 4.2 Technology Stack
### 4.3 Integration Points
### 4.4 Decision Log

| Decision | Options | Chosen | Rationale |
|----------|---------|--------|-----------|
| Database | Postgres/Mongo | Postgres | ACID, pgvector |

## 5. Data Model
### 5.1 Core Entities
### 5.2 Relationships
### 5.3 Confidence Scoring

## 6. Implementation Roadmap
### Phase 1: Foundation (Weeks 1-4)
- [ ] Deliverable 1
- [ ] Deliverable 2
- Success criteria: ...

### Phase 2: Core Features (Weeks 5-8)
...

## 7. Success Metrics
| Metric | Target | Measurement |
|--------|--------|-------------|
| Attribution accuracy | 90% | Cross-source validation |
| Artist satisfaction | 8/10 | Survey |

## 8. Risks & Dependencies
| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Data source API changes | Medium | High | Abstraction layer |

## 9. Cross-References
- Related PRDs: [relative paths]
- Knowledge Base: [domain/attribution/]
- External: [URLs]

## Appendices
### A. Glossary
### B. Open Questions
### C. Reviewer Feedback Log
```

---

## 5. Progressive Disclosure Implementation

### 5.1 Four-Level Disclosure Model

| Level | Time | Audience | Content | Files |
|-------|------|----------|---------|-------|
| **L1** | 5 min | Executives | What & Why | `README.md`, Executive Summaries |
| **L2** | 20 min | Stakeholders | Problem & Vision | Problem Statement, User Stories |
| **L3** | 45 min | Tech Leads | Architecture | Technical sections, Decision logs |
| **L4** | 90+ min | Implementers | Full specification | Complete PRDs, code examples |

### 5.2 File-Level Disclosure

Every directory implements disclosure through:

```
directory/
├── README.md          # L1: What is this? Navigation table
├── SYNTHESIS.md       # L2: Aggregated insights with citations
└── [content].md       # L3-L4: Detailed content
```

### 5.3 In-Document Disclosure

Each document implements disclosure through structure:

```markdown
## Executive Summary          <!-- L1: 5 min -->
## Problem Statement          <!-- L2: 15 min -->
## Technical Architecture     <!-- L3: 30 min -->
## Implementation Details     <!-- L4: 60+ min -->
## Appendices                 <!-- Reference -->
```

### 5.4 Navigation Patterns

**3-Click Rule**: Any concept reachable in ≤3 clicks from root README.

Navigation matrix to validate:

| From | → Attribution | → Graph RAG | → PRD Vision |
|------|---------------|-------------|--------------|
| Root README.md | 2 clicks | 2 clicks | 1 click |
| knowledge-base/README | 1 click | 1 click | 2 clicks |
| .claude/CLAUDE.md | 2 clicks | 2 clicks | 2 clicks |

---

## 6. Semantic Search & Retrieval

> **2026 Update**: Context Engineering replaces Prompt Engineering. Focus on *what information to include* and *how to structure it*, not just phrasing.

### 6.0 Production RAG Architecture (DPP-Agents Patterns + 2026 Research)

Based on production-tested patterns from dpp-agents (5M+ documents) and latest research:

#### Query Router Pattern (30% Cost Savings)

Route queries before expensive RAG:

```
Track Query
    ↓
Query Router (Intent Classification)
    ├→ Lookup (direct DB): "What's metadata for track ID 123?" → 0.05s, $0.001
    ├→ Simple RAG: "Which cover versions exist?" → 1s, $0.05
    └→ Complex RAG: "Is this track a derivative work?" → 3s, $0.15
```

**Impact**: 30% of queries are simple lookups. Saves 40% in embedding API calls.

#### Multi-Query Generation (Highest Impact)

Don't embed user query as-is. Generate 3-5 semantic variations in parallel:

```python
# Example: "Find similar tracks to X"
query_variations = [
    "acoustic cover songs similar to X",           # Semantic
    "same artist different album as X",            # Keyword
    "artist → related artists → their tracks",     # Graph traversal
    "songs released within 6 months of X",         # Temporal
]
# Execute all in parallel (no latency increase)
```

#### Reranking Layer (Precision 70% → 90%)

"5 lines of code" with huge impact:

```python
# Initial retrieval: 50 candidates
# Rerank by: relevance, source reliability, recency
# Output: Top 15 candidates
# Cost: ~$1/1000 reranks (Cohere API)
```

#### Agentic RAG Pattern (2026 Standard)

Instead of single retrieve→generate, use agent loops with verification:

```
┌─────────────────────────────────────────────────────────┐
│ Query → Agent Decides: What to fetch?                   │
│         ↓                                               │
│ Retrieve from multiple sources (parallel)               │
│         ↓                                               │
│ Agent Verifies: Is context sufficient?                  │
│    ├→ No: Rewrite query, fetch more                     │
│    └→ Yes: Generate with confidence bounds              │
│         ↓                                               │
│ Agent Validates: Is answer grounded?                    │
│    ├→ No: Flag for human review                         │
│    └→ Yes: Return with citations                        │
└─────────────────────────────────────────────────────────┘
```

#### Context Engineering Cost Optimization

| Technique | Token Reduction | Accuracy Impact | When to Use |
|-----------|----------------|-----------------|-------------|
| Prompt Caching | 10x cheaper cached tokens | None | Always (system prompts, docs) |
| JSON→YAML | 20-30% | None | Data serialization |
| Light Compression (2-3x) | 80% cost reduction | <5% | High-volume queries |
| Moderate Compression (5-7x) | 85-90% cost reduction | 5-15% | Cost-sensitive, accuracy-tolerant |

**Claude Sonnet Pricing**: $0.30/MTok (cached) vs $3/MTok (uncached) = 10x savings on cached context.

### 6.1 Frontmatter Schema for Indexing

```yaml
---
title: "Document Title"
type: prd | synthesis | concept | source | adr
domain: attribution | economics | rag | agentic
status: draft | active | superseded | archived
created: YYYY-MM-DD
updated: YYYY-MM-DD
confidence: high | medium | low
tags: [tag1, tag2, tag3]
related:
  - path/to/related-doc.md
  - path/to/another.md
sources:
  - "Edge et al. 2025"
  - "Cursor Blog 2026"
---
```

### 6.2 SYNTHESIS.md for RAG Aggregation

Each SYNTHESIS.md follows this pattern:

```markdown
# [Domain/Section] Synthesis

## Key Insights

1. **[Insight Title]** (Source: [citation])
   - Detail about insight
   - Implication for the system

2. **[Insight Title]** (Source: [citation])
   ...

## Cross-References

| Topic | Internal Link | Relationship |
|-------|---------------|--------------|
| Oracle Problem | domain/attribution/oracle-problem.md | explains |
| Graph RAG | technical/rag/graph-rag.md | implements |

## Sources

- [Edge et al. 2025](../sources/edge-2025-graph-rag.md) - Graph RAG approach
- [Cursor 2026](../sources/cursor-2026-indexing.md) - Merkle tree indexing

## Open Questions

- [ ] How does A0-A3 map to confidence scores?
- [ ] Which graph database for knowledge graph?
```

### 6.3 Retrieval-as-Service Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      the system Knowledge Layer (v2)                       │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌──────────────┐    ┌──────────────┐    ┌───────────────┐              │
│  │  Markdown    │    │   Vector     │    │  External     │              │
│  │  Files       │───▶│   Store      │◀───│  Sources      │              │
│  │  (Source)    │    │  (pgvector)  │    │  (MusicBrainz)│              │
│  └──────────────┘    └──────────────┘    └───────────────┘              │
│                              │                                           │
│                    ┌─────────▼─────────┐                                │
│                    │   Query Router     │◀── Intent classification      │
│                    │   (~30% cost save) │    (simple/complex/aggregate) │
│                    └─────────┬─────────┘                                │
│                              │                                           │
│           ┌──────────────────┼──────────────────┐                       │
│           ▼                  ▼                  ▼                        │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────────┐              │
│  │ Direct RAG  │    │ Multi-Query │    │  Multi-Agent    │              │
│  │ (simple)    │    │ Generation  │    │  Pipeline       │              │
│  └─────────────┘    └─────────────┘    └─────────────────┘              │
│                              │                  │                        │
│                    ┌─────────▼─────────────────▼┐                       │
│                    │       Reranker              │                       │
│                    │  (precision 70%→90%)        │                       │
│                    └─────────┬──────────────────┘                       │
│                              │                                           │
│                    ┌─────────▼─────────┐                                │
│                    │   MCP Gateway      │◀── Resource Indicators        │
│                    │   (RFC 8707)       │    (Nov 2025 spec)            │
│                    └─────────┬─────────┘                                │
│                              │                                           │
├──────────────────────────────┼───────────────────────────────────────────┤
│                              │                                           │
│  ┌──────────────┐    ┌───────▼──────┐    ┌──────────────┐              │
│  │ Claude Code  │◀───│   Context    │───▶│  Chat UI     │              │
│  │ (Dev)        │    │   Router     │    │  (Artist)    │              │
│  └──────────────┘    └──────────────┘    └──────────────┘              │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

#### 6.3.1 Multi-Agent Orchestration for Source Aggregation

Pattern from dpp-agents analysis: Use specialized agents for multi-source reconciliation.

**Agent Roles** (Hub-and-Spoke pattern for Phase 1):

| Agent | Responsibility | Input | Output |
|-------|---------------|-------|--------|
| `source_aggregator` | Fetch from MusicBrainz, Discogs, etc. | Artist/track query | Raw records |
| `conflict_detector` | Identify mismatches across sources | Raw records | Conflict report |
| `confidence_scorer` | Apply authority weights + conformal prediction | Records + conflicts | Scored assertions |
| `decision_synthesizer` | Generate human-readable summary | Scored assertions | Final response |

**Implementation Pattern** (Pure Python, no frameworks):

```python
from pydantic import BaseModel
from typing import Literal

class AgentMessage(BaseModel):
    """Inter-agent communication envelope."""
    sender: str
    recipient: str
    msg_type: Literal["request", "response", "error"]
    payload: dict
    trace_id: str  # For debugging/observability

class OrchestratorConfig(BaseModel):
    """Configuration for multi-agent pipeline."""
    pattern: Literal["hub_spoke", "mesh", "sequential"] = "hub_spoke"
    timeout_seconds: int = 30
    max_retries: int = 2
    # Future: Add mesh routing when agent count > 5

async def run_attribution_pipeline(query: str) -> AttributionResult:
    """Sequential orchestration - simplest pattern for MVP."""
    raw_data = await source_aggregator.fetch(query)
    conflicts = await conflict_detector.analyze(raw_data)
    scored = await confidence_scorer.score(raw_data, conflicts)
    return await decision_synthesizer.summarize(scored)
```

**When to Upgrade to Mesh**: Document criteria from dpp-agents:
- Agent count exceeds 5 specialized roles
- Latency requirements demand parallel processing
- Complex inter-agent dependencies emerge

#### 6.3.2 MCP Security (November 2025 Spec Updates)

From MCP spec analysis and Netflix webinar insights:

**Three-Tier Trust Model**:

| Tier | Access Level | Example |
|------|-------------|---------|
| **Tier 1** (Internal) | Full read/write | Claude Code in dev environment |
| **Tier 2** (Verified) | Read + scoped write | Verified third-party agents |
| **Tier 3** (Public) | Read-only, rate-limited | Unknown MCP clients |

**Resource Indicators (RFC 8707)** - Critical for security:

```python
from pydantic import BaseModel
from typing import Literal

class MCPResourceAccess(BaseModel):
    """Granular resource access control per RFC 8707."""
    resource: str  # e.g., "attribution://artists/{artist_id}"
    operations: list[Literal["read", "write", "delete"]]
    audience: str  # Specific client identifier
    scope: str     # OAuth-style scope string

# Example: Limit third-party to read-only artist data
third_party_access = MCPResourceAccess(
    resource="attribution://artists/*",
    operations=["read"],
    audience="agent-partner-xyz",
    scope="artists:read"
)
```

**Security Checklist for MCP Implementation**:
- [ ] OAuth 2.0 token validation for all requests
- [ ] Rate limiting per client tier (100/1000/10000 req/hour)
- [ ] Audit logging for all write operations
- [ ] Resource scoping (no wildcard access for Tier 3)
- [ ] Input validation using Pydantic models

### 6.4 Indexing Strategy (Cursor-Inspired)

From Cursor blog analysis:

1. **Merkle tree for change detection**: Hash files/directories, sync only changed
2. **Syntactic chunking**: Split files into semantic units
3. **Embedding caching**: Cache by chunk content hash
4. **Similarity hash (simhash)**: Enable index reuse across similar codebases

**For the system**:
- Use SYNTHESIS.md as high-signal chunks (already aggregated)
- Embed individual concept files for fine-grained retrieval
- Cache embeddings in DynamoDB/PostgreSQL
- MCP server exposes retrieval as tool for Claude Code

### 6.5 Agentic RAG with Verification Loops (2026 Pattern)

From dpp-agents and 2026 RAG research: **Verify before responding**.

```
┌─────────────────────────────────────────────────────────────┐
│                 Agentic RAG Pipeline                         │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  User Query                                                  │
│      │                                                       │
│      ▼                                                       │
│  ┌─────────────┐                                            │
│  │ RAG Retrieval│──────────────────────┐                    │
│  └──────┬──────┘                       │                    │
│         │                              │                    │
│         ▼                              ▼                    │
│  ┌─────────────┐                ┌─────────────┐            │
│  │  Generate   │                │  Retrieve   │            │
│  │  Draft      │                │  Verification│            │
│  │  Response   │                │  Sources    │            │
│  └──────┬──────┘                └──────┬──────┘            │
│         │                              │                    │
│         └──────────────┬───────────────┘                    │
│                        ▼                                    │
│              ┌─────────────────┐                            │
│              │    Verifier     │                            │
│              │    Agent        │                            │
│              └────────┬────────┘                            │
│                       │                                     │
│         ┌─────────────┼─────────────┐                       │
│         ▼             ▼             ▼                       │
│    ┌────────┐   ┌────────┐   ┌────────────┐                │
│    │ Accept │   │ Revise │   │ Flag for   │                │
│    │        │   │ & Loop │   │ Human      │                │
│    └────────┘   └────────┘   └────────────┘                │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

**Implementation Pattern**:

```python
from typing import Literal
from pydantic import BaseModel

class VerificationResult(BaseModel):
    """Output from verifier agent."""
    action: Literal["accept", "revise", "flag_human"]
    confidence: float
    issues: list[str]
    suggested_revision: str | None = None

async def agentic_rag_with_verification(
    query: str,
    max_revision_loops: int = 2
) -> AttributionResponse:
    """RAG with verification loop - stops runaway revisions."""

    for attempt in range(max_revision_loops + 1):
        # Step 1: Retrieve context
        context = await retrieve_from_knowledge_base(query)

        # Step 2: Generate draft response
        draft = await generate_response(query, context)

        # Step 3: Verify against sources
        verification = await verify_against_sources(draft, context)

        if verification.action == "accept":
            return draft.with_confidence(verification.confidence)

        if verification.action == "flag_human":
            return draft.mark_for_review(verification.issues)

        # Revise and loop
        query = f"{query}\n\nPrevious issues: {verification.issues}"

    # Max loops reached - flag for human
    return draft.mark_for_review(["Max revision loops exceeded"])
```

**Key Design Decisions**:
- **Max 2 revision loops**: Prevents infinite loops (MVA principle)
- **Always flag to human** if uncertain: Better to ask than guess
- **Confidence passed through**: Verifier confidence propagates to response

---

## 7. Uncertainty Quantification & GEO Provenance

> **Note**: This is a substantial research project of its own. This section captures initial framing based on recent literature.

### 7.1 GEO (Generative Engine Optimization) Provenance

From the AI Passport research, GEO represents a paradigm shift from traditional SEO to how LLM-based systems discover and rank content:

**Key Principles**:
- LLMs prioritize **low perplexity** (semantic consistency)
- **Citation authority** matters (third-party verification > self-reported claims)
- **Structured, verified data** enables confident assertions

**Implication for the system**: Music attributions with verified provenance gain preferential visibility in agent recommendations. This creates a flywheel:
1. Higher confidence → Better GEO ranking → More usage
2. More usage → More corrections/additions → Higher confidence

### 7.2 Confidence-Driven Governance Model

From the AI Passport framework, a tiered system for handling uncertainty:

| Confidence Level | Governance Action | User Experience |
|------------------|-------------------|-----------------|
| ≥0.8 (High) | Autonomous acceptance | Show as verified |
| 0.7-0.8 (Medium) | Display with warnings | Show with caveats |
| 0.6-0.7 (Low) | Human review required | Prompt for confirmation |
| <0.6 (Below threshold) | Excluded from recommendations | Hide or flag as unreliable |

**For System Chat Interface**: This maps directly to how we present attribution data:
- High confidence: "Based on Discogs + MusicBrainz + the system, the composer is [X]"
- Medium confidence: "Two sources agree on [X], but one shows [Y]"
- Low confidence: "Only one source has data—please verify"
- Below threshold: "Insufficient data—can you provide this information?"

### 7.2.1 LLM Uncertainty Taxonomy (Beigi et al. 2024) - FOUNDATIONAL

The [Beigi et al. 2024 framework](https://arxiv.org/abs/2410.20199) provides the foundational taxonomy for understanding LLM uncertainty:

**Four Categories of Uncertainty Estimation Methods**:

| Method | Approach | Limitations |
|--------|----------|-------------|
| **Logit-based** | Analyze probability distributions/entropy | Measures vocabulary probability, NOT truthfulness |
| **Self-evaluation** | Model assesses own correctness | Poor self-awareness, circular reasoning, overconfidence |
| **Consistency-based** | Agreement among multiple responses | Challenged by textual diversity, paraphrasing |
| **Internal-based** | Hidden state analysis with probes | High computational cost, poor transferability |

**Two Uncertainty Categories**:

1. **Operational Uncertainty** (throughout LLM lifecycle):
   - Pre-training: Semantic ambiguity, data errors, coverage gaps, biases
   - Alignment: Human annotation inconsistency
   - Inference: Distribution shifts, decoding strategy choices

2. **Output Uncertainty** (knowledge generation quality):
   - Lacking supporting evidence
   - Incomplete knowledge
   - Conflicting information from multiple sources

**Critical Insight for the system**: All current methods estimate *confidence*, but fail to identify *specific uncertainty sources*. For music attribution, we need **source-level explainability**—not just "70% confident" but "low confidence because Discogs and MusicBrainz disagree on composer."

**Implication**: Our Phase 1 heuristic confidence should track and report *why* confidence is low, not just the score.

### 7.3 Uncertainty Propagation in Multi-Step Workflows

Critical insight from UProp (Duan et al. 2025): **Uncertainty compounds at each step**.

For music attribution workflow:
```
Parse metadata → Match databases → Verify sources → Aggregate confidence
     ↓               ↓                ↓                  ↓
  Parsing UQ    Matching UQ      Verification UQ    Final confidence
```

**Key approaches from literature**:

1. **Conformal Prediction** (Angelopoulos & Bates 2021)
   - Generates prediction sets with mathematical coverage guarantees
   - Example: "Composer is {A, B, C} with 95% probability"

2. **Selective Prediction / Strategic Abstention** (Rabanser 2025)
   - System says "I don't know" when uncertainty is too high
   - Achieves high accuracy on answered queries by declining low-confidence ones

3. **Utility-Directed UQ** (Cortes-Gomez et al. 2025)
   - Incorporates decision costs into uncertainty thresholds
   - False positives in attribution may have different costs than false negatives

4. **Bayesian Knowledge Graphs** (Nafar et al. 2025)
   - Supply chain verification under uncertainty
   - Directly applicable to music attribution graphs

### 7.4 RAG-Specific Uncertainty Challenges

From Soudani et al. 2025 ("Why Uncertainty Estimation Methods Fall Short in RAG"):

**The RAG UQ Paradox**: Standard UQ methods fail because:
- Retrieval introduces **extrinsic uncertainty** (did we find the right documents?)
- Generation introduces **epistemic uncertainty** (does the model know the answer?)
- These interact non-linearly

**Implications for the system**:
- Confidence scores must account for **retrieval quality**, not just model certainty
- Multiple data sources improve confidence only if **semantically harmonized**
- "Garbage in, garbage out" applies to confidence scoring

### 7.5 Recommended UQ Framework for the system (MVA Approach)

> **Reviewer Note**: The framework below addresses entity resolution as a distinct uncertainty source (UQ Research Reviewer) and includes calibration requirements (missing from v2).

**Phase 1 (Sprint)**: Simple heuristic confidence + calibration baseline
```python
from dataclasses import dataclass
from typing import Optional

@dataclass
class DataSource:
    name: str
    authority_weight: float  # the system: 1.0, MusicBrainz: 0.8, Discogs: 0.7
    timestamp: str

# Authority weights (define explicitly per Reviewer feedback)
AUTHORITY_WEIGHTS = {
    "system_own": 1.0,
    "musicbrainz": 0.8,
    "discogs": 0.7,
    "user_submitted": 0.5,
    "automated_extraction": 0.4,
}

def compute_confidence(sources: list[DataSource]) -> float:
    """Simple multi-source agreement confidence.

    NOTE: This is NOT a calibrated probability. Phase 1 must include
    validation set (min 100 examples) to compute ECE before production.
    """
    if not sources:
        return 0.0  # Edge case: no sources

    n_sources = len(sources)
    n_agreeing = count_agreeing_sources(sources)  # Requires fuzzy matching

    # Base confidence from agreement ratio
    agreement_ratio = n_agreeing / n_sources

    # Boost for authoritative sources
    authority_boost = sum(s.authority_weight for s in sources) / n_sources

    # Cap at 0.95 to prevent overconfidence on perfect agreement
    return min(0.95, agreement_ratio * 0.7 + authority_boost * 0.3)

def count_agreeing_sources(sources: list[DataSource]) -> int:
    """Entity resolution with fuzzy matching.

    TODO Phase 1: Implement Fellegi-Sunter probabilistic matching
    or neural entity resolution for "John Smith" vs "J. Smith"
    """
    # Placeholder - this is NON-TRIVIAL
    raise NotImplementedError("Entity resolution requires dedicated implementation")
```

**Phase 1 MUST include** (per UQ Reviewer):
```python
def evaluate_calibration(predictions: list[float], ground_truth: list[bool]) -> dict:
    """Compute Expected Calibration Error on validation set.

    Requirements:
    - Minimum 100 labeled examples
    - If ECE > 0.15, acknowledge scores are not calibrated
    """
    from sklearn.calibration import calibration_curve
    import numpy as np

    fraction_of_positives, mean_predicted_value = calibration_curve(
        ground_truth, predictions, n_bins=10
    )
    ece = np.mean(np.abs(fraction_of_positives - mean_predicted_value))
    return {"ece": ece, "is_calibrated": ece < 0.15}
```

**Phase 2 (Future)**: Conformal prediction with MAPIE
```python
# Use MAPIE - the leader in conformal prediction (2025)
# pip install mapie
from mapie.classification import MapieClassifier

# Token-Entropy Conformal Prediction (TECP) for LLM outputs
# Coverage guarantees without requiring logit access
```
- Implement SConU (Wang et al. 2025) for selective answering
- Add calibration metrics (Brier score, ECE)
- Track calibration drift over time
- Use **UQLM** library for hallucination flagging

**Phase 3 (Research)**: Full uncertainty decomposition
- Epistemic vs. aleatoric separation using **Uncertainty Toolbox**
- **Bayesian RAG** for retrieval uncertainty (Frontier AI 2025)
- **UProp/AUQ frameworks** for agentic uncertainty propagation
- Human-in-the-loop active learning for low-confidence items

> **Note on MC Dropout**: Monte Carlo Dropout is less relevant for LLM-based systems because it requires access to model weights (not available for API-based LLMs like Claude). Conformal prediction methods (TECP, SConU) work without logit access and provide formal coverage guarantees—prefer these for the system.

### 7.5.1 Entity Resolution as Distinct UQ Source (NEW)

Per UQ Reviewer, the workflow must explicitly include entity resolution:

```
Parse metadata -> Resolve entities -> Match databases -> Verify sources -> Aggregate
     |               |                    |                 |               |
  Parsing UQ    Entity UQ           Matching UQ      Verification UQ    Final
```

**Entity Resolution Uncertainty**:
- "John Smith" on Discogs ≠ guaranteed same "John Smith" on MusicBrainz
- Use probabilistic entity resolution (Fellegi-Sunter or neural approaches)
- Track match probabilities that feed into confidence score

### 7.5.2 RAG Uncertainty Decomposition (NEW)

Per Soudani et al. 2025, decompose RAG uncertainty:

| Component | Description | How to Track |
|-----------|-------------|--------------|
| **Retrieval uncertainty** | Did we match the correct database entry? | P(correct entry \| query) |
| **Extraction uncertainty** | Did we extract the right field? | P(correct field \| matched entry) |
| **Combined** | Multiply for overall uncertainty | retrieval × extraction |

**Diagnostic use**: If retrieval uncertainty high → gather more data. If extraction uncertainty high → improve prompts/parsing.

### 7.6 Knowledge Base Structure for UQ Research

```
knowledge-base/
├── technical/
│   └── uncertainty/
│       ├── README.md
│       ├── conformal-prediction.md     # Angelopoulos & Bates 2021
│       ├── llm-uncertainty.md          # Liu et al. 2025 survey
│       ├── rag-uncertainty.md          # Soudani et al. 2025
│       ├── agentic-uncertainty.md      # UProp, Fleming et al.
│       ├── geo-provenance.md           # AI Passport framework
│       └── SYNTHESIS.md
```

### 7.7 UQ Research Bibliography (For Knowledge Base)

Key papers to synthesize (27 papers provided):

| Category | Papers | Focus |
|----------|--------|-------|
| **Foundational** | Angelopoulos & Bates 2021 | Conformal prediction primer |
| **LLM Surveys** | Beigi 2024, Liu 2025, Xia 2025 | UQ for LLMs overview |
| **RAG-Specific** | Soudani 2025 (2 papers) | Why UQ fails in RAG; solutions |
| **Agentic** | Duan 2025, Fleming 2025, Kirchhof 2025 | Multi-step uncertainty, access control |
| **Calibration** | Tomov 2025, Tao 2025 | Illusion of certainty, human-like UQ |
| **Selective** | Wang 2025 (2 papers), Stoisser 2025 | When to abstain, COIN framework |
| **Graphs** | Nafar 2025 | Bayesian knowledge graphs |
| **Applied** | Hasan 2025, Mehdiyev 2025 | Reject option, process monitoring |

---

## 8. Recommended Architecture

### 8.1 Overall Structure

```
music-attribution-scaffold/
├── README.md                    # Project overview (L1)
├── CLAUDE.md                    # AI assistant rules
│
├── docs/
│   ├── README.md                # Documentation navigation
│   │
│   ├── prd/                     # Product Requirements
│   │   ├── README.md            # PRD index & lineage
│   │   ├── vision-v1.md
│   │   ├── attribution-engine-prd.md
│   │   ├── chat-interface-prd.md
│   │   └── mcp-server-prd.md
│   │
│   ├── architecture/            # Architecture Decision Records
│   │   ├── README.md
│   │   ├── adr-001-database.md
│   │   └── adr-002-llm-provider.md
│   │
│   └── planning/                # Strategic planning
│       └── initial-hierarchical-doc-planning/
│
├── knowledge-base/              # Domain + Technical Knowledge
│   ├── README.md                # Knowledge navigation
│   ├── SYNTHESIS.md             # Cross-domain synthesis
│   │
│   ├── domain/                  # Music Attribution Domain
│   │   ├── README.md
│   │   ├── SYNTHESIS.md
│   │   ├── attribution/
│   │   │   ├── README.md
│   │   │   ├── a0-a3-framework.md
│   │   │   ├── oracle-problem.md
│   │   │   └── SYNTHESIS.md
│   │   ├── economics/
│   │   └── legal/
│   │
│   ├── technical/               # AI/Tech Knowledge
│   │   ├── README.md
│   │   ├── SYNTHESIS.md
│   │   ├── rag/
│   │   ├── semantic-search/
│   │   ├── agentic-systems/
│   │   └── context-engineering/
│   │
│   └── sources/                 # Literature Notes
│       ├── README.md
│       └── [source-notes].md
│
├── .claude/                     # Claude Code Configuration
│   ├── CLAUDE.md                # Extended rules
│   ├── rules/                   # Path-scoped rules
│   │   ├── 00-project-context.md
│   │   ├── 01-code-analysis-ban.md
│   │   └── 05-source-of-truth.md
│   ├── domains/                 # Domain-specific context
│   │   ├── attribution.md
│   │   └── testing.md
│   └── golden-paths.md          # Approved patterns
│
├── src/                         # Source code
│   └── attribution_sprint/
│
└── tests/                       # Test suite
```

### 8.2 Key Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Documentation format | Markdown | Native to Claude Code, Git-friendly |
| Knowledge aggregation | SYNTHESIS.md | Enables RAG without compilation |
| PRD location | `docs/prd/` | Clear separation from knowledge base |
| Knowledge base location | `knowledge-base/` (root level) | Easy MCP server access |
| Source notes | `knowledge-base/sources/` | Separates literature from synthesis |
| Claude context | `.claude/` | Standard location |

### 8.3 Frontmatter Requirements

**Mandatory fields** (100% adoption target):
- `title`, `type`, `status`, `created`, `updated`

**Recommended fields** (80% adoption target):
- `domain`, `tags`, `related`, `confidence`

**Optional fields**:
- `sources`, `supersedes`, `implementation_pr`

### 8.4 Context Engineering Patterns (2026 Best Practices)

From Netflix webinar and Cursor blog analysis:

**Token Efficiency Strategies**:

| Strategy | Impact | Implementation |
|----------|--------|----------------|
| Prompt caching | ~10x cost reduction | Anthropic API `cache_control` headers |
| JSON→YAML | 20-30% token savings | Use YAML for config, context windows |
| Layered disclosure | 50%+ context savings | SYNTHESIS.md at each level |
| Semantic chunking | Better retrieval | Split at heading/function boundaries |

**Prompt Caching Pattern** (for repeated context):

```python
from anthropic import Anthropic

client = Anthropic()

# Cache the knowledge base context
response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    system=[
        {
            "type": "text",
            "text": knowledge_base_synthesis,  # Large, stable context
            "cache_control": {"type": "ephemeral"}  # Cache for session
        }
    ],
    messages=[{"role": "user", "content": user_query}]
)
```

**YAML vs JSON for Context** (example token savings):

```yaml
# YAML: ~80 tokens
attribution:
  artist: "Example Artist"
  confidence: 0.85
  sources:
    - musicbrainz
    - discogs

# Equivalent JSON: ~110 tokens
{"attribution":{"artist":"Example Artist","confidence":0.85,"sources":["musicbrainz","discogs"]}}
```

**Compression Hierarchy for Claude Code**:

1. **First**: Load SYNTHESIS.md (aggregated, high-signal)
2. **On demand**: Drill into specific files via citations
3. **Never**: Load entire directory trees into context

---

## 9. Implementation Roadmap (Revised per Reviewer Feedback)

> **Key Changes**: Split Week 1, added quality gates, explicit Claude Code boundaries, escape hatches for over-engineering.

### Phase 1A: Foundation Lock (Days 1-2)

- [ ] Create directory structure (hard freeze by EOD Day 2)
- [ ] Write root README.md (navigation only, no prose)
- [ ] Create PRD template

**Success criteria**:
- Directory structure passes `tree -L 3` visual inspection
- README.md contains working links (verify via `markdown-link-check`)

### Phase 1B: Foundation Elaboration (Days 3-5)

- [ ] Write knowledge-base/README.md with domain/technical split
- [ ] vision-v1.md draft (sections 1-5 only)
- [ ] Basic frontmatter validation (defer full validation to Week 2)

**Success criteria**:
- vision-v1.md contains all 12 template sections with `TODO` placeholders
- 3-click rule validated for all current paths

**Quality Gate**: Directory structure stable → unblocks Week 2

### Phase 2: Domain Knowledge (Week 2)

- [ ] Populate `knowledge-base/domain/attribution/` from music paper
- [ ] Create SYNTHESIS.md files for each section (Claude-assisted draft, human review)
- [ ] Add source notes for key references
- [ ] Validate cross-references
- [ ] Implement frontmatter validation pre-commit hook

**Success criteria**:
- At least 3 domain concepts with SYNTHESIS.md
- Attribution framework documented
- Oracle problem explained

**Quality Gate**: Domain knowledge exists → unblocks Week 4 PRD elaboration

### Phase 3: Technical Knowledge (Week 3)

- [ ] Populate `knowledge-base/technical/rag/` (Graph RAG, etc.)
- [ ] Populate `knowledge-base/technical/uncertainty/` (from 27 papers bibliography)
- [ ] Document semantic search patterns (Cursor blog insights)
- [ ] Document Netflix GenAI patterns (webinar insights)
- [ ] Create technical SYNTHESIS.md files

**Success criteria**:
- RAG approaches documented with trade-offs
- UQ section has conformal prediction, agentic uncertainty coverage
- Cross-references to domain knowledge working

**Quality Gate**: Technical knowledge exists → unblocks Phase 5 design

### Phase 4: PRD Elaboration (Week 4)

- [ ] Complete attribution-engine-prd.md (v0.8 draft, not final)
- [ ] Complete chat-interface-prd.md (v0.8 draft)
- [ ] Draft mcp-server-prd.md
- [ ] Update vision PRD with synthesis

**Success criteria**:
- All PRDs follow template with `TODO` markers for unknowns
- Decision logs populated with options considered
- Implementation roadmaps defined (can have TBD items)

> **Scope Note**: 4 full PRDs in one week is aggressive. Accept "v0.8" drafts; elaboration continues post-sprint.

### Phase 5: Retrieval Infrastructure (Future - DEFERRED)

> **Sprint Status**: DEFERRED. Do not implement during sprint.

- [ ] Design MCP server for knowledge retrieval (ADR first)
- [ ] Implement embedding pipeline
- [ ] Set up vector store (pgvector)
- [ ] Create Claude Code MCP integration

**Upgrade Trigger**: Implement when semantic search becomes a bottleneck for development velocity.

### Quality Gates Summary

| Checkpoint | Criteria | Blocks |
|------------|----------|--------|
| Week 1 Gate | Directory structure stable, PRD template complete | Week 2 content |
| Week 2 Gate | ≥3 domain concepts with SYNTHESIS.md | Week 4 PRDs |
| Week 3 Gate | RAG + UQ sections documented | Phase 5 design |

### Claude Code Assist Boundaries

| Task | Claude Code Role | Human Role |
|------|------------------|------------|
| Directory creation | Execute `mkdir` commands | Approve final structure |
| README.md drafting | Generate from template | Review navigation accuracy |
| SYNTHESIS.md generation | Draft from source files | Validate citations, add insights |
| PRD elaboration | Expand outline sections | Business logic, priority decisions |
| Frontmatter validation | Implement script | Define schema requirements |
| UQ code examples | Implement skeleton | Review for domain correctness |

---

## 10. Open Questions

### Architecture Questions (Remaining)

1. **Obsidian compatibility**: Should we support `[[wikilinks]]` syntax? (Probably not—standard markdown links are more portable)

### Content Questions (Remaining)

2. **UQ complexity**: How much uncertainty quantification do we need for MVP vs. future phases?

### Process Questions (Remaining)

5. **Review workflow**: How do we implement "reviewer agents for multiple iterations"?
6. **Update cadence**: How often should SYNTHESIS.md files be regenerated?
7. **Frontmatter enforcement**: Pre-commit hook vs. CI/CD check?

### Resolved Questions

| Question | Resolution |
|----------|-----------|
| Graph database | PostgreSQL + pgvector (no Neo4j) |
| LaTeX/PDF | Not needed—pure Markdown |
| Mogen scope | Separate project; The system is RAG source |
| A0-A3 mapping | Own research project; GEO provenance framework |
| Data warehouse | Hetzner Object Storage (Parquet) + PostgreSQL (Section 11) |
| Source prioritization | Both Discogs + MusicBrainz dumps (owned); start batch, add API later |
| Data source coverage | Discogs + MusicBrainz + system own for sprint demo |
| Entity resolution | Rule-based + phonetic for sprint; embedding-based post-sprint |
| Cost target | ~€7-34/month on Hetzner (same datacenter for free transfer) |
| IaC tool | Pulumi (Python) - same language as app, official Hetzner provider |
| Managed DB (MVP) | Neon PostgreSQL €17.50/month - scale-to-zero, database branching |
| Object storage | Cloudflare R2 - zero egress for audio files |
| Container orchestration | Render (MVP) → Kamal (Growth) - best UX progression |

---

## 11. Data Warehouse Architecture (NEW - v4)

> **Design Philosophy**: "PyTorch approach" - simple primitives that compose into production systems. Start with demo-ready stack, scale without rebuild.

### 11.1 Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────┐
│                   Hetzner FSN1 Datacenter (Same Region)                  │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  LAYER 1: Raw Storage (Hetzner Object Storage - S3 compatible)          │
│  ─────────────────────────────────────────────────────────────          │
│  ┌───────────────┐  ┌───────────────┐  ┌───────────────┐                │
│  │ discogs/      │  │ musicbrainz/  │  │ system_own/ │                │
│  │ └─2026-02/    │  │ └─2026-02/    │  │ └─live/       │                │
│  │   └─*.parquet │  │   └─*.parquet │  │   └─*.parquet │                │
│  └───────────────┘  └───────────────┘  └───────────────┘                │
│         │                  │                   │                         │
│         └──────────────────┼───────────────────┘                         │
│                            ▼                                             │
│  LAYER 2: Processing (DuckDB + Python)                                  │
│  ─────────────────────────────────────                                  │
│  ┌──────────────────────────────────────────────────────────┐           │
│  │  - Query Parquet directly from object storage            │           │
│  │  - Same SQL works at any scale (laptop → production)     │           │
│  │  - Entity resolution + confidence scoring                │           │
│  └──────────────────────────────────────────────────────────┘           │
│                            │                                             │
│                            ▼                                             │
│  LAYER 3: Event Store (Append-only, Single Source of Truth)             │
│  ──────────────────────────────────────────────────────────             │
│  ┌──────────────────────────────────────────────────────────┐           │
│  │  ChangeEvent {source, entity_type, entity_id, payload}   │           │
│  │  - Batch and incremental produce SAME event format       │           │
│  │  - Enables replay, backfill, audit                       │           │
│  └──────────────────────────────────────────────────────────┘           │
│                            │                                             │
│                            ▼                                             │
│  LAYER 4: Serving (PostgreSQL + pgvector)                               │
│  ────────────────────────────────────────                               │
│  ┌──────────────────────────────────────────────────────────┐           │
│  │  unified_entities, source_records, entity_links,         │           │
│  │  field_confidence, embeddings (pgvector)                 │           │
│  │  → MCP Server connects here                              │           │
│  └──────────────────────────────────────────────────────────┘           │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

### 11.2 Data Source Access Patterns

| Source | Access Type | Refresh | Rate Limits | Sprint Strategy |
|--------|-------------|---------|-------------|-----------------|
| **Discogs** | Monthly dumps (owned) | Monthly | 60 req/min API | Dump for sprint, API for freshness later |
| **MusicBrainz** | Weekly dumps (owned) | Weekly | 1 req/sec API | Dump for sprint |
| **System Own** | Direct PostgreSQL | Real-time | N/A | Source of truth |
| **User Submissions** | API | Real-time | N/A | Direct write |

### 11.3 Entity Resolution Strategy

**Sprint Phase (Rule-Based + Phonetic)**:

```python
"""Entity resolution for sprint phase - rule-based with phonetic matching."""

from dataclasses import dataclass
from difflib import SequenceMatcher

# Authority weights for source prioritization
SOURCE_AUTHORITY = {
    "system_own": {"priority": 1, "name": 0.95, "royalty_split": 1.0},
    "musicbrainz": {"priority": 2, "name": 0.90, "release_date": 0.95, "isni": 0.98},
    "discogs": {"priority": 3, "name": 0.85, "genre": 0.90, "label": 0.95},
    "user_submission": {"priority": 4, "name": 0.60},
}

@dataclass
class MatchScore:
    """Multi-field match confidence."""
    name_score: float        # String similarity
    phonetic_score: float    # Metaphone/Soundex match
    catalog_overlap: float   # Shared releases/tracks
    temporal_overlap: float  # Active years overlap
    overall: float           # Weighted combination

def compute_match_confidence(record_a: dict, record_b: dict) -> MatchScore:
    """Compute entity match confidence using rule-based approach.

    Cold start solution: Bootstrap from ISNI/Wikidata links.
    - MusicBrainz artists often have ISNI identifiers
    - Both sources link to Wikidata QIDs
    - Use these as ground truth for initial training set
    """
    name_score = SequenceMatcher(
        None,
        normalize_name(record_a["name"]),
        normalize_name(record_b["name"])
    ).ratio()
    # ... additional scoring logic
    pass
```

**Post-Sprint**: Add embedding-based matching with `sentence-transformers` for edge cases.

### 11.4 Database Schema

```sql
-- Event store (append-only, immutable)
CREATE TABLE change_events (
    event_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    source TEXT NOT NULL,              -- 'discogs', 'musicbrainz', 'attribution'
    entity_type TEXT NOT NULL,         -- 'artist', 'release', 'track'
    entity_id TEXT NOT NULL,
    operation TEXT NOT NULL,           -- 'create', 'update', 'upsert'
    payload JSONB NOT NULL,
    ingestion_mode TEXT NOT NULL,      -- 'batch', 'incremental'
    batch_id UUID,                      -- Links events from same batch
    created_at TIMESTAMPTZ DEFAULT NOW()
);
CREATE INDEX idx_events_source_type ON change_events(source, entity_type);
CREATE INDEX idx_events_created ON change_events(created_at);

-- Source records (raw data with provenance)
CREATE TABLE source_records (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    source TEXT NOT NULL,
    source_id TEXT NOT NULL,
    entity_type TEXT NOT NULL,
    raw_data JSONB NOT NULL,
    snapshot_date DATE NOT NULL,
    content_hash TEXT NOT NULL,        -- For change detection
    created_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(source, source_id, snapshot_date)
);

-- Unified entities (resolved, deduplicated)
CREATE TABLE unified_entities (
    entity_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    entity_type TEXT NOT NULL,
    canonical_name TEXT NOT NULL,
    overall_confidence FLOAT NOT NULL,
    confidence_level TEXT NOT NULL,    -- 'verified', 'high', 'medium', 'low'
    resolution_method TEXT,
    embedding vector(1536),            -- pgvector for semantic search
    last_resolved TIMESTAMPTZ DEFAULT NOW()
);

-- Entity links (source_records <-> unified_entities)
CREATE TABLE entity_links (
    source TEXT NOT NULL,
    source_record_id TEXT NOT NULL,
    unified_entity_id UUID REFERENCES unified_entities(entity_id),
    link_confidence FLOAT NOT NULL,
    link_method TEXT,                  -- 'exact', 'fuzzy', 'embedding', 'isni'
    created_at TIMESTAMPTZ DEFAULT NOW(),
    PRIMARY KEY (source, source_record_id)
);

-- Per-field confidence (granular scoring)
CREATE TABLE field_confidence (
    id SERIAL PRIMARY KEY,
    entity_id UUID REFERENCES unified_entities(entity_id),
    field_name TEXT NOT NULL,
    field_value TEXT,
    confidence FLOAT NOT NULL,
    source TEXT NOT NULL,
    sources_agreeing TEXT[],           -- Which sources have same value
    UNIQUE(entity_id, field_name, source)
);
```

### 11.5 Batch to Real-Time Migration Path

**Lambda Architecture Lite**: Both paths produce identical `ChangeEvent` objects.

```
Sprint (Batch)                        Growth (Incremental)
─────────────                        ──────────────────────
Monthly dumps ─┐                     ┌─ API polling (CDC)
               │                     │
               ▼                     ▼
          ┌─────────────────────────────────┐
          │      ChangeEvent (unified)       │
          │  {source, entity_id, payload}    │
          └─────────────────────────────────┘
                         │
                         ▼
               ┌──────────────────┐
               │   Event Store    │  ◄── Single source of truth
               │  (PostgreSQL)    │
               └──────────────────┘
                         │
                         ▼
               ┌──────────────────┐
               │   Projections    │  ◄── Rebuild from events
               │  (Materialized)  │
               └──────────────────┘
```

**Synthetic CDC for APIs without change feeds**:
- Use checkpoint-based polling: Query `?sort=date_changed&limit=100`
- Hash comparison: Detect changes via content hash
- Interest-based tracking: Only poll entities users care about

### 11.6 Caching Strategy

| Tier | Storage | TTL | Purpose |
|------|---------|-----|---------|
| **L1** | In-memory (dict) | 30s | Deduplicate rapid requests |
| **L2** | SQLite/PostgreSQL | 5min | Warm data, survives restart |
| **L3** | Object Storage | 24h | Stale-while-revalidate |

**Stale-while-revalidate pattern**: Return cached data immediately, trigger background refresh.

### 11.7 Cost Estimates (Hetzner)

| Phase | Components | Monthly Cost |
|-------|------------|--------------|
| **Sprint** | Object Storage (100GB) + CX22 (4GB) + Block Storage (50GB) | **€7/month** |
| **Growth** | Object Storage (250GB) + CX42 (16GB) + Processing VM (CX32) | **€34/month** |
| **Scale** | Object Storage (500GB) + CX52 (32GB) + Read Replica + LB | **€112/month** |

**Key cost decisions**:
- Same datacenter (FSN1/NBG1) → FREE internal transfer
- Self-managed PostgreSQL → €15-20/month vs €25-50 managed
- DuckDB on same VM → €0 extra (can query object storage directly)

### 11.8 Sprint Simplification (Reviewer Recommendation)

For demo phase, further simplify:

```
┌─────────────────────────────────────────┐
│         Sprint Demo Stack               │
│    (SQLite + DuckDB, single VM)         │
├─────────────────────────────────────────┤
│                                         │
│  ┌─────────────────────────────────┐    │
│  │  Local Parquet files (dumps)    │    │
│  │  ~/data/discogs/*.parquet       │    │
│  └──────────────┬──────────────────┘    │
│                 │                       │
│                 ▼                       │
│  ┌─────────────────────────────────┐    │
│  │  DuckDB (query engine)          │    │
│  │  + SQLite (event store)         │    │
│  └──────────────┬──────────────────┘    │
│                 │                       │
│                 ▼                       │
│  ┌─────────────────────────────────┐    │
│  │  FastAPI + SQLite               │    │
│  │  (€10/month Hetzner VPS)        │    │
│  └─────────────────────────────────┘    │
│                                         │
└─────────────────────────────────────────┘
```

**When to upgrade**:
- >10 concurrent users → Add PostgreSQL
- >100GB data → Add Object Storage
- Need semantic search → Add pgvector

### 11.9 Conflict Resolution Matrix

| Field | Primary Source | Conflict Strategy |
|-------|---------------|-------------------|
| `release_date` | MusicBrainz | Source priority |
| `genre` | Discogs | Merge (combine lists) |
| `label` | Discogs | Source priority |
| `royalty_split` | System Own | Single source (authoritative) |
| `isni` | MusicBrainz | Source priority |
| `credits` | Both | Flag for review if confidence <0.7 |

### 11.10 FinOps & Infrastructure Optimization (NEW)

> **Detailed plan**: See [finops-optimization-plan.md](../finops-optimization-plan.md) for comprehensive multi-hypothesis analysis.

**Design Philosophy**: Every cent saved at small volume translates to massive savings at scale.

#### Recommended Stack by Phase

| Phase | Compute | Database | Storage | Monthly Cost |
|-------|---------|----------|---------|--------------|
| **MVP** | Render Free (€0) | Neon (€17.50) | Cloudflare R2 (€0) | **~€18** |
| **Growth** | Hetzner CX32 + Kamal (€6.80) | Neon/Ubicloud (€20-64) | R2 + Hetzner backup | **~€35-80** |
| **Scale** | Hetzner cluster / Fly.io | Managed HA Postgres | Multi-region R2 | **~€150-300** |

#### Key FinOps Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| IaC Tool | **Pulumi (Python)** | Same language as app, official Hetzner provider |
| Object Storage | **Cloudflare R2** | Zero egress costs for audio files |
| Managed DB | **Neon** | Scale-to-zero, database branching, pgvector |
| Container Orchestration | **Render → Kamal** | Best UX for small team |
| Cloud Credits | **NVIDIA Inception first** | Unlocks higher AWS/GCP tiers |

#### Cloud Credit Strategy (Bootstrapped)

Realistic total: **~€17,000-27,000** (not €500K+ - those require VC backing)

| Program | Realistic Amount | Priority |
|---------|------------------|----------|
| NVIDIA Inception | Unlocks higher tiers | 1st |
| OVHcloud START | €10,000 | 2nd (best for bootstrapped) |
| Azure Founders Hub | €920-4,600 | 3rd (use first - 90-180 day expiry) |
| AWS Activate | €920-9,200 | 4th |
| GCP Start | €1,840 | 5th |

#### Portability Guarantees

- [x] All services containerized (Docker)
- [x] Standard PostgreSQL (no proprietary extensions)
- [x] S3-compatible storage (R2/Hetzner/S3 interchangeable)
- [x] Pulumi IaC with provider abstraction
- [x] No serverless lock-in (containers over Lambda)

---

## 12. Mogen Integration & Voice Architecture (NEW - v6)

> **Scope Clarification**: Mogen (Imogen Heap's digital twin) is a **separate project**. The system serves as the authoritative music attribution data source that Mogen and other third-party voice agents can query via MCP. This section documents the architectural boundary and interface contracts.

### 12.1 Architectural Boundary (the system as Service)

**Design Principle**: The system is a **data provider**, not a voice platform. Voice interfaces like Mogen consume the system via MCP.

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                    ATTRIBUTION + MOGEN ECOSYSTEM ARCHITECTURE                       │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                  │
│  ┌─────────────────────────────────────────────────────────────────────────┐    │
│  │                         MOGEN (Separate Project)                         │    │
│  │                      Voice-First Digital Twin Layer                      │    │
│  ├─────────────────────────────────────────────────────────────────────────┤    │
│  │                                                                          │    │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐     │    │
│  │  │  Pipecat/   │  │   Claude/   │  │  Inworld/   │  │  Persona    │     │    │
│  │  │  Vapi Voice │  │   GPT LLM   │  │  11Labs TTS │  │  Drift Mon  │     │    │
│  │  │  Platform   │  │   Context   │  │   ~$0.02/   │  │  (Embedding)│     │    │
│  │  │  ~$0.05/min │  │   Window    │  │   conv.     │  │             │     │    │
│  │  └──────┬──────┘  └──────┬──────┘  └─────────────┘  └─────────────┘     │    │
│  │         │                │                                               │    │
│  │         │                ▼                                               │    │
│  │         │         ┌─────────────────────────────────────────────────┐   │    │
│  │         │         │        MCP CLIENT (Mogen → the system)            │   │    │
│  │         │         │  - Artist data requests                         │   │    │
│  │         │         │  - Song attribution queries                     │   │    │
│  │         │         │  - Permission verification                      │   │    │
│  │         │         └──────────────────────┬──────────────────────────┘   │    │
│  │         │                                │                               │    │
│  └─────────┼────────────────────────────────┼───────────────────────────────┘    │
│            │                                │                                     │
│            │     ════════════════════════════════════════════════                │
│            │     ║      MCP GATEWAY (RFC 8707 Resource Indicators)   ║           │
│            │     ║      Rate Limiting │ Audit Logging │ Tier Access  ║           │
│            │     ════════════════════════════════════════════════                │
│            │                                │                                     │
├────────────┼────────────────────────────────┼─────────────────────────────────────┤
│            │        ATTRIBUTION (This Project) │                                     │
│            │                                │                                     │
│            │  ┌─────────────────────────────▼─────────────────────────────┐      │
│            │  │          ATTRIBUTION ENGINE (Core Service)                │      │
│            │  │   - Multi-source aggregation (Discogs, MusicBrainz)       │      │
│            │  │   - Confidence scoring (0.6-0.95 range)                   │      │
│            │  │   - Entity resolution (fuzzy + phonetic)                  │      │
│            │  │   - Conflict detection & flagging                         │      │
│            │  └───────────────────────────────────────────────────────────┘      │
│            │                                │                                     │
│            │  ┌─────────────────────────────▼─────────────────────────────┐      │
│            │  │               PostgreSQL + pgvector                        │      │
│            │  │   - unified_entities (resolved, deduplicated)             │      │
│            │  │   - source_records (raw with provenance)                  │      │
│            │  │   - field_confidence (per-field scoring)                  │      │
│            │  └───────────────────────────────────────────────────────────┘      │
│                                                                                   │
│  ┌─────────────────────────────────────────────────────────────────────────┐     │
│  │                    OTHER MCP CLIENTS (Third-Party)                       │     │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐     │     │
│  │  │   ChatGPT   │  │  Claude AI  │  │   Custom    │  │   Future    │     │     │
│  │  │   Plugins   │  │  Desktop    │  │   Agents    │  │   Clients   │     │     │
│  │  │  (Tier 3)   │  │  (Tier 2)   │  │  (Tier 2/3) │  │             │     │     │
│  │  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘     │     │
│  └─────────────────────────────────────────────────────────────────────────┘     │
│                                                                                   │
└─────────────────────────────────────────────────────────────────────────────────┘
```

**Component Ownership Boundaries**:

| Component | Owned By | Responsibility |
|-----------|----------|----------------|
| MCP Server + Gateway | The System | Authentication, rate limiting, audit |
| Attribution Engine | The System | Data aggregation, confidence scoring |
| Chat Interface | The System | Artist data entry, gap-filling |
| Voice Platform | Mogen | STT, TTS, persona management |
| LLM Context | Mogen | Imogen Heap personalization |
| Permission System | The System | Who can access artist's data |

### 12.2 MCP Interface for Third-Party Clients

**Three-Tier Trust Model** (from Section 6.3.2):

| Tier | Access Level | Example Client | Rate Limit |
|------|-------------|----------------|------------|
| **Tier 1** (Internal) | Full read/write | System Chat, Admin | Unlimited |
| **Tier 2** (Verified) | Read + scoped write | Mogen, verified partners | 1000 req/hour |
| **Tier 3** (Public) | Read-only, rate-limited | ChatGPT, unknown agents | 100 req/hour |

**Interface Contract (the system ↔ Mogen)**:

```python
from pydantic import BaseModel
from typing import Literal

class ArtistAttributionRequest(BaseModel):
    """Request for artist attribution data."""
    artist_id: str
    include_sources: bool = True
    confidence_threshold: float = 0.6

class ArtistAttributionResponse(BaseModel):
    """Response with artist attribution and confidence."""
    artist_id: str
    canonical_name: str
    overall_confidence: float
    confidence_level: Literal["verified", "high", "medium", "low"]
    songs: list["SongAttribution"]
    sources_consulted: list[str]
    last_updated: str

class SongAttribution(BaseModel):
    """Individual song attribution with field-level confidence."""
    song_id: str
    title: str
    composers: list["Credit"]
    performers: list["Credit"]
    field_confidence: dict[str, float]  # {"composers": 0.95, "release_date": 0.7}

# MCP tool definitions for Mogen
MCP_TOOLS = {
    "get_artist_attribution": {
        "description": "Get complete attribution data for an artist",
        "input_schema": ArtistAttributionRequest.model_json_schema(),
    },
    "search_songs": {
        "description": "Search for songs with optional confidence filter",
        "input_schema": {"query": "str", "min_confidence": "float"},
    },
    "verify_credit": {
        "description": "Verify if a credit claim is accurate",
        "input_schema": {"song_id": "str", "credit_type": "str", "claimed_name": "str"},
    },
}
```

### 12.3 Hierarchical PRD Structure Pattern

**Token Efficiency via Progressive Disclosure**:

The hierarchical PRD structure prevents **context amnesia** by allowing targeted retrieval at the appropriate depth level. When querying about voice agent details, the system loads only the relevant level.

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                     HIERARCHICAL PRD STRUCTURE (Example: Voice)                  │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                  │
│  LEVEL 1: High-Level Overview (~500 tokens)                                      │
│  ══════════════════════════════════════════                                      │
│  docs/prd/README.md                                                              │
│  └─ Executive summary of all PRDs                                                │
│  └─ Navigation table with lineage                                                │
│                                                                                  │
│  LEVEL 2: Feature Domain Overview (~2,000 tokens)                                │
│  ═══════════════════════════════════════════════                                 │
│  docs/prd/voice-integration-prd.md                                               │
│  └─ Voice feature overview                                                       │
│  └─ Technology choices table                                                     │
│  └─ Cost summary                                                                 │
│  └─ Links to Level 3 docs                                                        │
│                                                                                  │
│  LEVEL 3.x: Feature Details (~5,000 tokens each)                                 │
│  ═══════════════════════════════════════════════                                 │
│  ├─ docs/prd/voice/3.1-voice-synthesis.md                                        │
│  │   └─ TTS provider comparison (Inworld, ElevenLabs, Cartesia)                  │
│  │   └─ Latency benchmarks (<250ms target)                                       │
│  │   └─ Cost per conversation (~$0.005 TTS)                                      │
│  │                                                                               │
│  ├─ docs/prd/voice/3.2-speech-to-text.md                                         │
│  │   └─ STT provider comparison (Deepgram Nova-2)                                │
│  │   └─ 100ms latency target                                                     │
│  │                                                                               │
│  └─ docs/prd/voice/3.3-persona-guardrails.md                                     │
│      └─ Persona drift detection via embedding similarity                         │
│      └─ Threshold: 0.75 cosine similarity                                        │
│      └─ Check frequency: every 5 turns                                           │
│                                                                                  │
│  LEVEL 3.x.x: Provider Specifics (~3,000 tokens each)                            │
│  ════════════════════════════════════════════════════                            │
│  ├─ docs/prd/voice/providers/3.1.1-inworld-tts.md                                │
│  │   └─ $5/1M chars, <250ms, #1 TTS Arena                                        │
│  │                                                                               │
│  ├─ docs/prd/voice/providers/3.1.2-elevenlabs-tts.md                             │
│  │   └─ Flash v2.5 75ms latency (fallback)                                       │
│  │                                                                               │
│  └─ docs/prd/voice/providers/3.2.1-deepgram-stt.md                               │
│      └─ Nova-2 model, 100ms latency                                              │
│                                                                                  │
│  SYNTHESIS.md at Each Level (RAG Aggregation Point)                              │
│  ═══════════════════════════════════════════════════                             │
│  docs/prd/voice/SYNTHESIS.md                                                     │
│  └─ Aggregated insights from all voice docs                                      │
│  └─ Cross-references to knowledge-base/technical/                                │
│                                                                                  │
└─────────────────────────────────────────────────────────────────────────────────┘
```

**Query Routing by Level**:

| Query Type | Load Level | Tokens | Response Quality |
|------------|------------|--------|------------------|
| "What voice features exist?" | L1 + L2 | ~2,500 | Overview |
| "How does TTS work?" | L2 + L3.1 | ~7,000 | Technical |
| "Configure ElevenLabs fallback" | L3.1 + L3.1.2 | ~8,000 | Implementation |
| "Full voice architecture" | All levels | ~20,000 | Comprehensive |

### 12.4 Team Scalability Through Decoupling

**Design Goal**: Clear decoupling enables parallel development whether by a solo developer or a team.

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                      TEAM SCALABILITY ARCHITECTURE                               │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                  │
│  SOLO DEVELOPER (Hobby Project)                                                  │
│  ═══════════════════════════════                                                 │
│  One person works on all components sequentially.                                │
│  Clear interfaces mean context switching is manageable.                          │
│                                                                                  │
│       Week 1-2: Attribution Engine                                               │
│       Week 3-4: MCP Server                                                       │
│       Week 5-6: Chat Interface                                                   │
│       Week 7-8: Integration testing                                              │
│                                                                                  │
│  SMALL TEAM (2-3 Developers)                                                     │
│  ═══════════════════════════                                                     │
│  Parallel development on decoupled components.                                   │
│  Interface contracts prevent blocking.                                           │
│                                                                                  │
│       ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐             │
│       │   Developer A   │  │   Developer B   │  │   Developer C   │             │
│       │   Backend       │  │   Frontend      │  │   Data          │             │
│       ├─────────────────┤  ├─────────────────┤  ├─────────────────┤             │
│       │ Attribution     │  │ Chat Interface  │  │ Entity          │             │
│       │ Engine          │  │                 │  │ Resolution      │             │
│       │ MCP Server      │  │ Voice UI        │  │ Source          │             │
│       │                 │  │ (if in scope)   │  │ Aggregation     │             │
│       └────────┬────────┘  └────────┬────────┘  └────────┬────────┘             │
│                │                    │                    │                       │
│                └────────────────────┼────────────────────┘                       │
│                                     │                                            │
│                          ┌──────────▼──────────┐                                 │
│                          │  Interface Contracts │                                │
│                          │  (Pydantic Models)   │                                │
│                          └─────────────────────┘                                 │
│                                                                                  │
└─────────────────────────────────────────────────────────────────────────────────┘
```

**Interface Contracts Enable Parallel Work**:

| Component | Interface | Can Work Independently When... |
|-----------|-----------|-------------------------------|
| Attribution Engine | `AttributionResult` Pydantic model | API contract defined |
| MCP Server | MCP tool schemas (JSON) | Resource URIs defined |
| Chat Interface | REST/GraphQL endpoints | OpenAPI spec exists |
| Entity Resolution | `MatchScore` dataclass | Authority weights defined |

**Placeholder Strategy**:

```python
# Early sprint: Placeholder with mock data
class AttributionEngine:
    async def get_attribution(self, song_id: str) -> AttributionResult:
        # TODO: Replace with real implementation
        return AttributionResult(song_id=song_id, confidence=0.85, sources=["placeholder"])

# Later sprint: Real implementation swaps in seamlessly
```

### 12.5 Voice Cost Reference (From dpp-agents voice-agent-tech-prd)

**Cost Projection for Voice Agents Consuming the System**:

| Scenario | Per Conversation | Components |
|----------|-----------------|------------|
| **Managed (Vapi)** | ~$0.12 | Vapi $0.10 + STT $0.01 + LLM $0.003 + TTS $0.005 |
| **Self-hosted (Pipecat)** | ~$0.02 | STT $0.01 + LLM $0.003 + TTS $0.005 |

**Migration Triggers (Mogen-specific)**:

| Trigger | Action |
|---------|--------|
| Monthly voice costs > $300 | Migrate Vapi → Pipecat |
| Latency requirements < 500ms | Evaluate self-hosted TTS |
| System query volume > 10K/day | Upgrade MCP gateway tier |

---

## Appendix A: Architecture Flexibility & Upgrade Criteria (NEW)

Per MVA philosophy: "Anticipate but don't solve future challenges."

### Scale Thresholds

| Metric | Threshold | Action Required |
|--------|-----------|-----------------|
| Knowledge-base files | 100 | Review directory granularity |
| Knowledge-base files | 500 | Consider federated indexing (per-domain embedding stores) |
| Knowledge-base files | 1000+ | Evaluate knowledge-base repository extraction |
| Semantic search latency | >500ms P95 | Optimize embedding pipeline |
| Entity resolution failures | >10% | Implement neural entity matching |

### Graph Query Patterns That May Require Upgrade

pgvector cannot natively support these queries (document for future):

1. **Traversal queries**: "Show all claims that trace back to this unverified source"
2. **Path queries**: "What's the chain from Artist → Composer → Publisher → Rights?"
3. **Influence queries**: "Which sources contributed to this confidence score?"

**Upgrade path**: PostgreSQL `ltree` or recursive CTEs first; Neo4j only if those fail.

### Technology Volatility Assessment

| Component | Volatility | Strategy |
|-----------|------------|----------|
| LLM APIs (Claude, GPT) | HIGH | Thin wrapper layer, no framework lock-in |
| Embedding models | HIGH | Abstract behind interface, easy swapping |
| Vector stores | MEDIUM | pgvector mature; monitor Postgres 17+ native vector |
| Conformal prediction | LOW | MAPIE is stable; mathematical foundations solid |
| Python ecosystem | LOW | Core tooling stable |

### Framework Avoidance (per StartupOps best practices)

| Avoid | Use Instead | Rationale |
|-------|-------------|-----------|
| LangChain | Pure Python + Pydantic | Debugging nightmare in production |
| Heavy ORMs | Raw SQL or SQLAlchemy Core | Control and debuggability |
| Complex CI/CD | GitHub Actions + simple scripts | 4-week MVP principle |

## Appendix B: Comparison Matrix

| Criterion | Option A (Pure MD) | Option B (Hybrid) | Option C (Obsidian) |
|-----------|-------------------|-------------------|---------------------|
| Tooling complexity | Low | Medium | Medium |
| Claude Code native | ✅ | ✅ | ⚠️ (wikilinks) |
| Academic citations | ⚠️ | ✅ | ⚠️ |
| PDF export | ⚠️ | ✅ | ⚠️ |
| Graph visualization | ❌ | ❌ | ✅ |
| Semantic search | ✅ | ✅ | ✅ |
| Sprint readiness | ✅ | ⚠️ | ⚠️ |
| Scale potential | Medium | High | High |

**Recommendation**: Option A (Pure Markdown)—confirmed as the right choice. Simple, sprint-ready, Claude Code native.

---

## Appendix B: Netflix GenAI Insights Applied

From the Netflix webinar, patterns applicable to the system:

1. **Profile Backend → Context Configuration**: Just-in-time context loading based on task
2. **Eval as Practice**: Evaluate context retrieval quality, not just code quality
3. **Tools as MCP Ecosystem**: Standardize on MCP for all external integrations
4. **Retrieval Team Investment**: Dedicated focus on "how to get context right"
5. **Sentiment > Metrics**: Developer happiness compounds over time

---

## Appendix C: Source References

### Primary Research Sources
1. dpp-agents knowledge-base structure analysis (692 files, 17 themes)
2. dpp-agents PRD system analysis (8 PRDs, ~8,000 lines)
3. sci-llm-writer LaTeX hierarchy analysis (70 .tex files, 6 domains)
4. Meta-learning documents synthesis (4 failure analysis docs)
5. Music traceability domain analysis (academic papers)

### External References
6. Edge et al. 2025 - "From Local to Global: A Graph RAG Approach"
7. Cursor blog 2026 - "Securely indexing large codebases"
8. Netflix GenAI webinar 2025 - "Scaling AI Agent Development at Netflix"
9. AI Passport v1.12 - GEO provenance framework

### Uncertainty Quantification Bibliography (27 papers)
10. Angelopoulos & Bates 2021 - Conformal Prediction introduction
11. Soudani et al. 2025 - "Why Uncertainty Estimation Methods Fall Short in RAG"
12. Duan et al. 2025 - "UProp: Uncertainty Propagation in Multi-Step Agentic Decision-Making"
13. Liu et al. 2025 - "Uncertainty Quantification and Confidence Calibration in LLMs: A Survey"
14. Nafar et al. 2025 - "Bayesian Knowledge Graphs for Supply Chain Verification"
15. Fleming et al. 2025 - "Uncertainty-Aware, Risk-Adaptive Access Control for Agentic Systems"
16. Wang et al. 2025 - "SConU: Selective Conformal Uncertainty in LLMs"
17. Kirchhof et al. 2025 - "Position: UQ Needs Reassessment for LLM Agents"

*(Full bibliography of 27 papers in original-prompt.md)*

---

## Appendix D: Reviewer Feedback Summary (NEW)

Three specialized reviewers assessed PLAN.md v2:

### Architecture Reviewer (a29a0d7)

**Strengths identified**:
- Pure Markdown choice is sound
- SYNTHESIS.md pattern well-conceived for RAG
- Separation of sources/ from synthesized knowledge
- Frontmatter schema pragmatic

**Key concerns addressed**:
1. ✅ SYNTHESIS.md maintenance burden → Added regeneration triggers
2. ✅ pgvector may constrain graph queries → Added upgrade criteria
3. ✅ 3-click rule incomplete → Added validation requirement
4. ✅ MCP server underspecified → Deferred to Phase 5 with ADR requirement
5. ✅ Scale thresholds missing → Added Appendix A

### UQ Research Reviewer (afb1470)

**Technical accuracy issues addressed**:
1. ✅ GEO vs Data Provenance conflation → Clarified in Section 7.1
2. ✅ Missing error cost asymmetry → Added to Section 7.2
3. ✅ Entity resolution as distinct UQ source → Added Section 7.5.1
4. ✅ RAG decomposition missing → Added Section 7.5.2
5. ✅ Phase 1 needs calibration baseline → Added ECE requirement
6. ✅ MC Dropout relevance questioned → Added note clarifying conformal prediction preference

**Missing elements added**:
- Beigi et al. 2024 taxonomy (foundational paper)
- Music-specific UQ challenges (name disambiguation, role ambiguity, temporal consistency)

### Implementation Feasibility Reviewer (a60282d)

**Roadmap changes implemented**:
1. ✅ Split Phase 1 into 1A (Lock) and 1B (Elaboration)
2. ✅ Added Quality Gates between phases
3. ✅ Defined Claude Code assist boundaries
4. ✅ Added escape hatches for over-engineering (DEFERRED markers)
5. ✅ Simplified success criteria to be measurable/automatable
6. ✅ Acknowledged Week 4 PRDs as "v0.8" drafts

**Risk mitigations added**:
- Scope creep: `BACKLOG.md` for deferred synthesis
- Frontmatter complexity: Phased implementation
- SYNTHESIS.md bottleneck: Claude-assisted draft with human review

---

## Appendix E: Music Attribution-Specific UQ Challenges (NEW)

Per UQ Reviewer, document music-specific issues:

| Challenge | Description | Impact on Confidence |
|-----------|-------------|---------------------|
| **Name disambiguation** | Same name, different artists (John Williams ×3) | Entity resolution uncertainty |
| **Role ambiguity** | "Producer" means different things in different contexts | Field-level uncertainty |
| **Temporal consistency** | Artist name changes (The Quarrymen → The Beatles) | Historical matching |
| **Derived works** | Samples, covers, remixes create attribution chains | Graph complexity |
| **Collective works** | Orchestras, bands, collaborative albums | Many-to-many relationships |
| **Language/script variation** | Romanization inconsistencies (Tchaikovsky variants) | Fuzzy matching required |

These inform the entity resolution component (Phase 1 `count_agreeing_sources`).
