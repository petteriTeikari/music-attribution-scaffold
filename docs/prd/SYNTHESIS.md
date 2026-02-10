# PRD Synthesis

Cross-cutting insights and decisions across all Music Attribution PRDs.

---

## Executive Summary (For Both Audiences)

**For Stakeholders**: This document shows how all system components work together to solve the music attribution problem.

**For Engineers**: This document defines the contracts between components and shared architectural decisions.

### System Overview

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'background': '#fcfaf5', 'primaryColor': '#1E3A5F', 'lineColor': '#5C5C5C'}}}%%
C4Context
    title Music Attribution System Context Diagram

    Person(artist, "Artist", "Creates music, owns rights")
    Person(manager, "Manager", "Manages artist catalogs")

    System(attribution, "Attribution Platform", "Attribution engine + permissions hub")

    System_Ext(discogs, "Discogs", "Release database")
    System_Ext(mb, "MusicBrainz", "Music metadata")
    System_Ext(ai_platform, "AI Platforms", "Mogen, ChatGPT, etc.")
    System_Ext(streaming, "Streaming Services", "Spotify, Apple Music")

    Rel(artist, attribution, "Claims credits, sets permissions")
    Rel(manager, attribution, "Manages multiple artists")
    Rel(attribution, discogs, "Fetches release data")
    Rel(attribution, mb, "Fetches artist data")
    Rel(ai_platform, attribution, "Queries permissions via MCP")
    Rel(streaming, attribution, "Receives verified attribution")

    UpdateLayoutConfig($c4ShapeInRow="3", $c4BoundaryInRow="1")
```

**For Stakeholders**: The system sits at the center of the music data ecosystem, aggregating from sources and serving to platforms.

**For Engineers**: External integrations use distinct protocols: REST for sources, MCP for AI platforms, webhooks for streaming services.

---

## Key Architectural Decisions

| Decision | Choice | Rationale | PRD Reference |
|----------|--------|-----------|---------------|
| Database | PostgreSQL + pgvector | ACID + vectors, no Neo4j complexity | attribution-engine |
| AI Framework | Pure Python + Pydantic | Debuggability, no lock-in | vision-v1 |
| API Protocol | MCP | AI-native, emerging standard | mcp-server |
| UQ Approach | Heuristic → Conformal | API-compatible, formal guarantees | attribution-engine |
| Security | Defense-in-depth | MCPSecBench findings, 4-layer model | mcp-server |

## Cross-PRD Data Flow

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'background': '#fcfaf5', 'primaryColor': '#1E3A5F', 'lineColor': '#5C5C5C'}}}%%
graph LR
    subgraph sources[" External Sources "]
        DIS[Discogs]
        MB[MusicBrainz]
    end

    subgraph internal[" Internal Systems "]
        AE[Attribution<br/>Engine]
        CI[Chat<br/>Interface]
        MCP[MCP<br/>Server]
    end

    subgraph platforms[" External Platforms "]
        MOGEN[Mogen]
        GPT[ChatGPT]
        STREAM[Streaming]
    end

    DIS --> AE
    MB --> AE
    AE --> CI
    AE --> MCP
    CI -->|Artist Input| AE
    MCP --> MOGEN
    MCP --> GPT
    MCP --> STREAM

    style AE fill:#1E3A5F,color:#fff
    style CI fill:#D4A03C,color:#000
    style MCP fill:#4A7C59,color:#fff
    style DIS fill:#8B8B8B,color:#fff
    style MB fill:#8B8B8B,color:#fff
```

### Data Flow Description

| Flow | Description | Contracts |
|------|-------------|-----------|
| Sources → Engine | Raw attribution data ingestion | Source adapter interface |
| Engine → Chat | Confidence-scored data for verification | `SongAttribution` model |
| Chat → Engine | Artist-verified corrections | `GapFillRequest` model |
| Engine → MCP | API-ready attribution responses | `ArtistAttributionResponse` model |
| MCP → Platforms | Permission-checked data access | MCP tool schemas |

## Confidence Score Propagation

Confidence flows through the system:

1. **Attribution Engine** computes per-field confidence (0.0-1.0)
2. **Chat Interface** displays confidence as UX treatment (verified/high/medium/low)
3. **MCP Server** exposes confidence in API responses with `confidence_threshold` filter

### Confidence Flow Diagram

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'background': '#fcfaf5', 'primaryColor': '#1E3A5F', 'lineColor': '#5C5C5C'}}}%%
flowchart LR
    subgraph sources[" Data Sources "]
        S1[Discogs]
        S2[MusicBrainz]
        S3[Artist Input]
    end

    subgraph engine[" Attribution Engine "]
        AGG[Aggregation]
        CONF[Confidence<br/>Calculator]
        AGG --> CONF
    end

    subgraph outputs[" Consumer Interfaces "]
        CHAT[Chat UI<br/>Visual Treatment]
        MCP[MCP API<br/>Filtered Response]
        ADMIN[Admin<br/>Review Queue]
    end

    S1 -->|weight: 0.7| AGG
    S2 -->|weight: 0.8| AGG
    S3 -->|weight: 1.0| AGG

    CONF -->|0.0-1.0 score| CHAT
    CONF -->|threshold filter| MCP
    CONF -->|low scores| ADMIN

    style S1 fill:#8B8B8B,color:#fff
    style S2 fill:#8B8B8B,color:#fff
    style S3 fill:#D4A03C,color:#000
    style CONF fill:#1E3A5F,color:#fff
    style CHAT fill:#D4A03C,color:#000
    style MCP fill:#4A7C59,color:#fff
```

**For Stakeholders**: Artist input has the highest confidence weight (1.0). External sources have lower weights. The system prioritizes artist-verified data.

**For Engineers**: Confidence thresholds are centralized in configuration. All components read from the same source of truth to maintain consistency.

**Consistency requirement**: All components must use the same confidence thresholds:

| Level | Score | Engine | Chat | MCP |
|-------|-------|--------|------|-----|
| verified | ≥0.8 + artist confirm | `level="verified"` | Green checkmark | `confidence_level: "verified"` |
| high | ≥0.8 | `level="high"` | Gray checkmark | `confidence_level: "high"` |
| medium | 0.7-0.8 | `level="medium"` | Yellow question | `confidence_level: "medium"` |
| low | <0.7 | `level="low"` | Red gap | `confidence_level: "low"` |

## Three-Tier Trust Model Application

The MCP trust model affects multiple PRDs:

| Tier | Attribution Engine | Chat Interface | MCP Server |
|------|-------------------|----------------|------------|
| Internal | Full access | Full access | Unlimited |
| Verified | Read + contribute | N/A | 1000 req/hr |
| Public | Read only | N/A | 100 req/hr |

## Open Questions (Cross-PRD)

1. **Disputed credits**: How does chat interface handle conflicts surfaced by attribution engine?
2. **Permission inheritance**: If artist grants permission in chat, how quickly does MCP reflect it?
3. **Confidence calibration**: How large must validation set be before confidence scores are "calibrated"?

## Implementation Sequencing

### Component Dependency Graph

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'background': '#fcfaf5', 'primaryColor': '#1E3A5F', 'lineColor': '#5C5C5C'}}}%%
flowchart TB
    subgraph phase1[" Phase 1: Sprint MVP "]
        AE[Attribution Engine]
        CONF[Confidence Module]
        MCP1[MCP Server<br/>Read-only]
        AE --> CONF
        CONF --> MCP1
    end

    subgraph phase2[" Phase 2: Identity "]
        CI[Chat Interface]
        ID[ArtistID System]
        MCP2[MCP Server<br/>Write Ops]
        CI --> MCP2
        ID --> MCP2
    end

    subgraph phase3[" Phase 3: Ecosystem "]
        PART[Partner Integrations]
        CAL[Calibrated Confidence]
        VOICE[Voice Agent]
    end

    MCP1 --> CI
    MCP1 --> ID
    MCP2 --> PART
    MCP2 --> CAL
    CI --> VOICE

    style AE fill:#1E3A5F,color:#fff
    style CONF fill:#1E3A5F,color:#fff
    style MCP1 fill:#4A7C59,color:#fff
    style CI fill:#D4A03C,color:#000
    style ID fill:#D4A03C,color:#000
    style MCP2 fill:#4A7C59,color:#fff
    style PART fill:#2E7D7B,color:#fff
    style CAL fill:#2E7D7B,color:#fff
    style VOICE fill:#2E7D7B,color:#fff
```

**For Stakeholders**: Arrows show dependencies. Nothing in Phase 2 can start until Phase 1 components are complete.

**For Engineers**: The Attribution Engine is the critical path. Delays there cascade to all downstream components.

```
Phase 1 (Sprint MVP)
├── attribution-engine (core data)
├── mcp-server (read-only API)
└── confidence module (scoring)

Phase 2 (Identity)
├── chat-interface (gap-filling)
└── mcp-server (write ops, permissions)

Phase 3 (Ecosystem)
├── Partner integrations
└── Calibrated confidence
```

### Build vs Buy Decision Matrix

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'background': '#fcfaf5', 'primaryColor': '#1E3A5F', 'lineColor': '#5C5C5C'}}}%%
quadrantChart
    title Build vs Buy: Component Decisions
    x-axis Off-the-shelf Available --> Custom Required
    y-axis Low Strategic Value --> Core Differentiator
    quadrant-1 Build In-house
    quadrant-2 Build with Care
    quadrant-3 Buy/Use OSS
    quadrant-4 Partner/Integrate

    Attribution Engine: [0.85, 0.90]
    Confidence Scoring: [0.70, 0.85]
    MCP Server: [0.60, 0.75]
    Chat UI: [0.40, 0.50]
    Database: [0.15, 0.30]
    Auth System: [0.20, 0.35]
    Observability: [0.10, 0.25]
    Entity Resolution: [0.75, 0.70]
```

**For Stakeholders**: Components in the top-right (Attribution Engine, Confidence Scoring) are our core differentiators. Components in the bottom-left (Database, Auth) should use existing solutions.

**For Engineers**: Focus engineering effort on top-right quadrant. Use PostgreSQL, standard auth libraries, and observability platforms (Langfuse) for bottom-left.

## Hierarchical PRD Navigation

### PRD Ecosystem Map

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'background': '#fcfaf5', 'primaryColor': '#1E3A5F', 'lineColor': '#5C5C5C'}}}%%
graph TB
    subgraph level1[" L1: Vision & Synthesis "]
        VISION[vision-v1-v1.md]
        SYN[SYNTHESIS.md<br/>THIS DOCUMENT]
        LLM[llm-context.md]
    end

    subgraph level2[" L2: Domain PRDs "]
        AE[attribution-engine/]
        CI[chat-interface/]
        MCP[mcp-server/]
        DL[data-layer/]
        VA[voice-agent/]
    end

    subgraph cross[" Cross-Cutting Concerns "]
        UQ[uncertainty/]
        OBS[observability/]
        SEC[security/]
        IP[identity-permissions/]
    end

    subgraph support[" Support Documents "]
        REJ[REJECTED.md]
        UNK[UNKNOWNS-FOR-DOMAIN-EXPERTS.md]
        DEF[defaults.yaml]
    end

    VISION --> AE
    VISION --> CI
    VISION --> MCP
    SYN --> AE
    SYN --> CI
    SYN --> MCP

    AE --> UQ
    AE --> OBS
    CI --> UQ
    MCP --> SEC
    MCP --> IP

    style VISION fill:#1E3A5F,color:#fff
    style SYN fill:#1E3A5F,color:#fff
    style AE fill:#2E7D7B,color:#fff
    style CI fill:#D4A03C,color:#000
    style MCP fill:#4A7C59,color:#fff
    style UQ fill:#C75050,color:#fff
    style SEC fill:#C75050,color:#fff
```

### Navigation by Role

| Role | Start Here | Then Read |
|------|------------|-----------|
| **New to project** | [llm-context.md](llm-context.md) | [vision-v1-v1.md](vision-v1-v1.md) |
| **Domain expert** | [UNKNOWNS-FOR-DOMAIN-EXPERTS.md](UNKNOWNS-FOR-DOMAIN-EXPERTS.md) | Vision doc |
| **Backend engineer** | [attribution-engine/toc-attribution-engine.md](attribution-engine/toc-attribution-engine.md) | Data layer PRDs |
| **Frontend engineer** | [chat-interface/toc-chat-interface.md](chat-interface/toc-chat-interface.md) | Voice agent PRDs |
| **API engineer** | [mcp-server/toc-mcp-server.md](mcp-server/toc-mcp-server.md) | Security PRDs |
| **DevOps** | [infrastructure/toc-infrastructure.md](infrastructure/toc-infrastructure.md) | Observability PRDs |

---

## Cross-PRD Unknown Unknowns

Synthesized from individual PRD unknown unknowns sections:

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'background': '#fcfaf5', 'primaryColor': '#1E3A5F', 'lineColor': '#5C5C5C'}}}%%
mindmap
  root((Cross-PRD<br/>Unknowns))
    User Adoption
      Artist engagement
      Chat fatigue
      Heritage digital literacy
    Technical Scale
      Entity resolution at 1M+
      Real-time sync latency
      API rate economics
    Market Dynamics
      AI platform consolidation
      Competing standards
      Regulatory shifts
    Security Landscape
      Novel attack vectors
      Protocol evolution
      Trust model accuracy
```

| Unknown | Affected PRDs | Monitoring Approach |
|---------|---------------|---------------------|
| Artist engagement drop-off | Chat Interface, Voice Agent | Session analytics, A/B testing |
| Entity resolution failures | Attribution Engine | Error rate tracking, manual review sampling |
| MCP spec breaking changes | MCP Server | AAIF governance monitoring, abstraction layer |
| Confidence calibration drift | All | Continuous calibration via Langfuse |
| Security zero-days | MCP Server, Data Layer | Bug bounty, security audit schedule |

---

---

## Integration Points Matrix

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'background': '#fcfaf5', 'primaryColor': '#1E3A5F', 'lineColor': '#5C5C5C'}}}%%
block-beta
    columns 4

    block:header:4
        H1["Component"]
        H2["Inputs"]
        H3["Outputs"]
        H4["Contract"]
    end

    block:ae:4
        AE["Attribution<br/>Engine"]
        AE_IN["Discogs, MB,<br/>Artist Input"]
        AE_OUT["SongAttribution,<br/>Confidence Scores"]
        AE_CON["Source Adapter<br/>Interface"]
    end

    block:ci:4
        CI["Chat<br/>Interface"]
        CI_IN["User Messages,<br/>Attribution Data"]
        CI_OUT["GapFillRequest,<br/>Confirmations"]
        CI_CON["Message Schema,<br/>WebSocket Protocol"]
    end

    block:mcp:4
        MCP["MCP<br/>Server"]
        MCP_IN["Attribution Data,<br/>Permissions"]
        MCP_OUT["Tool Responses,<br/>Filtered Data"]
        MCP_CON["MCP Protocol,<br/>Tool Schemas"]
    end

    block:data:4
        DL["Data<br/>Layer"]
        DL_IN["All CRUD ops"]
        DL_OUT["Persisted State,<br/>Query Results"]
        DL_CON["SQLAlchemy Models,<br/>Migration Files"]
    end

    style AE fill:#1E3A5F,color:#fff
    style CI fill:#D4A03C,color:#000
    style MCP fill:#4A7C59,color:#fff
    style DL fill:#2E7D7B,color:#fff
```

**For Stakeholders**: Each component has defined inputs and outputs. This ensures teams can work in parallel with clear boundaries.

**For Engineers**: Contracts are enforced via Pydantic models and interface definitions. Breaking changes require migration plans.

---

## Related Knowledge

- [domain/attribution/](../knowledge-base/domain/attribution/) - A0-A3 framework, oracle problem
- [technical/uncertainty/](../knowledge-base/technical/uncertainty/) - Conformal prediction, calibration
- [technical/mcp/](../knowledge-base/technical/mcp/) - Protocol security
- [UNKNOWNS-FOR-DOMAIN-EXPERTS.md](UNKNOWNS-FOR-DOMAIN-EXPERTS.md) - Questions for Imogen/Andy
- [REJECTED.md](REJECTED.md) - Why NOT to use certain technologies
