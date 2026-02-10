# the system Vision PRD v1

## Metadata

- **Version**: 0.8.0
- **Status**: Draft
- **Created**: 2026-02-03
- **Updated**: 2026-02-03
- **Author**: Claude Code (with Imogen Heap's vision)
- **Lineage**: Synthesizes original-prompt.md, PLAN.md, Imogen Heap Medium articles

## Executive Summary

- **What**: Autonomous artist identity and data hub for music attribution with AI-ready permissions
- **Why**:
  - 40%+ of music metadata contains incorrect attribution
  - Major label AI deals exclude independent artists
  - No machine-readable permissions standard exists for AI training
- **Investment**: Sprint MVP (4-6 weeks), full platform (6-12 months)
- **Confidence**: High for core attribution engine, medium for AI ecosystem adoption

## Table of Contents

1. [Problem Statement](#1-problem-statement)
2. [Product Vision](#2-product-vision)
3. [User Stories](#3-user-stories)
4. [Technical Architecture](#4-technical-architecture)
5. [Data Model](#5-data-model)
6. [Implementation Roadmap](#6-implementation-roadmap)
7. [Success Metrics](#7-success-metrics)
8. [Risks & Dependencies](#8-risks--dependencies)
9. [Cross-References](#9-cross-references)

## 1. Problem Statement

### 1.1 Current State

The music industry operates on fragmented, incomplete attribution data scattered across multiple databases (Discogs, MusicBrainz, proprietary label systems). Each source contains partial truths, and no single authority can verify all claims.

#### Industry Ecosystem Map

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'background': '#fcfaf5', 'primaryColor': '#1E3A5F', 'lineColor': '#5C5C5C'}}}%%
flowchart TB
    subgraph creators[" Music Creators "]
        direction TB
        ART[Artists]
        SESS[Session Musicians]
        PROD[Producers]
        SONG[Songwriters]
    end

    subgraph databases[" Fragmented Data Sources "]
        direction TB
        DIS[(Discogs)]
        MB[(MusicBrainz)]
        ISRC[(ISRC Registry)]
        PRO[(PRO Databases)]
        LABEL[(Label Systems)]
    end

    subgraph platforms[" Consumption Platforms "]
        direction TB
        STREAM[Streaming Services]
        AI[AI Music Platforms]
        RADIO[Radio/Broadcast]
    end

    subgraph problems[" Current Problems "]
        direction TB
        P1[40% incorrect<br/>metadata]
        P2[$2.5B unclaimed<br/>royalties]
        P3[No AI consent<br/>standard]
    end

    creators -->|contribute to| databases
    databases -->|partial data| platforms
    databases -.->|inconsistencies cause| problems

    style ART fill:#D4A03C,color:#000
    style SESS fill:#D4A03C,color:#000
    style PROD fill:#D4A03C,color:#000
    style SONG fill:#D4A03C,color:#000
    style DIS fill:#8B8B8B,color:#fff
    style MB fill:#8B8B8B,color:#fff
    style ISRC fill:#8B8B8B,color:#fff
    style PRO fill:#8B8B8B,color:#fff
    style LABEL fill:#8B8B8B,color:#fff
    style STREAM fill:#2E7D7B,color:#fff
    style AI fill:#2E7D7B,color:#fff
    style RADIO fill:#2E7D7B,color:#fff
    style P1 fill:#C75050,color:#fff
    style P2 fill:#C75050,color:#fff
    style P3 fill:#C75050,color:#fff
```

**For Stakeholders**: This diagram shows how music attribution data is currently scattered across multiple incompatible systems, leading to massive value leakage.

**For Engineers**: Each data source has different APIs, schemas, and update frequencies. The system must reconcile these into a unified model.

### 1.2 Pain Points

| Pain Point | Impact | Who Suffers |
|------------|--------|-------------|
| **Incorrect credits** | Lost royalties, misattribution | Composers, session musicians |
| **Data silos** | Duplicate effort, inconsistency | Labels, distributors, platforms |
| **No AI permissions** | Unauthorized training, no compensation | Independent artists |
| **Manual verification** | Expensive, slow, doesn't scale | Rights organizations |

### 1.3 Market Opportunity

The rise of generative AI in music creates urgent demand for:

1. **Machine-readable permissions**: AI companies need to know who consents to training
2. **Attribution provenance**: AI outputs need traceable credit chains
3. **Independent artist representation**: 80% of music is independent, but AI deals favor majors

#### Market Forces Driving Adoption

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'background': '#fcfaf5', 'primaryColor': '#1E3A5F', 'lineColor': '#5C5C5C'}}}%%
quadrantChart
    title Market Forces for Music Attribution Solutions
    x-axis Low Urgency --> High Urgency
    y-axis Low Market Size --> High Market Size
    quadrant-1 Strategic Priority
    quadrant-2 Long-term Investment
    quadrant-3 Deprioritize
    quadrant-4 Quick Wins

    AI Training Consent: [0.85, 0.75]
    Royalty Accuracy: [0.65, 0.90]
    EU AI Act Compliance: [0.90, 0.60]
    Heritage Catalog Fix: [0.40, 0.70]
    Indie Artist Tools: [0.70, 0.55]
```

**For Stakeholders**: AI training consent and EU AI Act compliance are high-urgency drivers. Royalty accuracy represents the largest market but slightly lower urgency.

**For Engineers**: Priority implementation order should follow the urgency axis. Phase 1 focuses on compliance-critical features.

### 1.4 Regulatory Drivers

- EU AI Act transparency requirements
- Potential US legislation on AI training data consent
- Industry pressure for "ethical AI" standards

### Visual: EU AI Act Compliance Timeline

![EU AI Act Compliance](../figures/assets/fig-domain-05-eu-ai-act-compliance.jpg)

*EU AI Act timeline for music AI: GPAI obligations (training data transparency) active from August 2025. The system provides L3 traceability for compliance. Non-compliance penalties up to [€35M or 7% turnover](https://www.dlapiper.com/en-us/insights/publications/2025/08/latest-wave-of-obligations-under-the-eu-ai-act-take-effect).*

## 2. Product Vision

### 2.1 Vision Statement

> Artists are the experts on their work. The system enables them to control their digital identity and do business with AI and third-party platforms on their own terms.

### 2.2 Target Users

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'background': '#fcfaf5', 'primaryColor': '#1E3A5F', 'lineColor': '#5C5C5C'}}}%%
graph LR
    subgraph creators[" Creators "]
        A1[Independent<br/>Artist]
        A2[Session<br/>Musician]
        A3[Heritage<br/>Artist]
    end

    subgraph business[" Business "]
        B1[Manager]
        B2[Rights Org]
    end

    subgraph platforms[" Platforms "]
        P1[AI Platform]
        P2[Streaming<br/>Service]
    end

    creators --> AUR[The System]
    business --> AUR
    AUR --> platforms

    style AUR fill:#1E3A5F,color:#fff
    style A1 fill:#D4A03C,color:#000
    style A2 fill:#D4A03C,color:#000
    style A3 fill:#D4A03C,color:#000
    style B1 fill:#4A7C59,color:#fff
    style B2 fill:#4A7C59,color:#fff
    style P1 fill:#2E7D7B,color:#fff
    style P2 fill:#2E7D7B,color:#fff
```

| Persona | Need | Attribution Solution |
|---------|------|-------------------|
| **Independent Artist** | Catalog works, set AI permissions | Artist ID + permission dashboard |
| **Session Musician** | Prove contributions | Verified credit claims |
| **Manager** | Manage multiple artists | Multi-artist data hub |
| **AI Platform** | Licensed training data | MCP API with consent verification |
| **Rights Organization** | Accurate attribution | Cross-referenced data feeds |

### 2.3 Success Definition

The system succeeds when:

1. Artists can create verified identities in < 5 minutes
2. Attribution confidence reaches 90%+ for cross-referenced claims
3. AI platforms prefer attribution data over scraping due to quality and licensing clarity

## 3. User Stories

### Artist Stories

- **As an independent artist**, I want to catalog my discography with proper credits so that streaming platforms and AI systems attribute me correctly.
- **As a session musician**, I want to claim my contributions to recordings so that I receive proper recognition even without formal contracts.
- **As a heritage artist**, I want to verify historical credits album-by-album so that decades of misattribution can be corrected.

### Platform Stories

- **As an AI music platform**, I want to query artist permissions via API so that I can train models only on consented works.
- **As a streaming service**, I want high-confidence attribution data so that royalty payments go to the right people.

### Manager Stories

- **As a manager**, I want to manage multiple artists' data in one place so that I can ensure consistency across their catalogs.

## 4. Technical Architecture

### 4.1 System Design

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'background': '#fcfaf5', 'primaryColor': '#1E3A5F', 'lineColor': '#5C5C5C'}}}%%
graph TB
    subgraph ui[" User Interfaces "]
        CHAT[Chat UI<br/>Gap-filling]
        ADMIN[Admin UI<br/>Management]
        MCP[MCP Server<br/>AI Access]
    end

    subgraph core[" Core Engine "]
        AE[Attribution<br/>Engine]
    end

    subgraph adapters[" Data Adapters "]
        DIS[Discogs<br/>Adapter]
        MB[MusicBrainz<br/>Adapter]
        OWN[System<br/>Own Data]
    end

    subgraph storage[" Storage "]
        DB[(PostgreSQL<br/>+ pgvector)]
    end

    CHAT --> AE
    ADMIN --> AE
    MCP --> AE

    DIS --> AE
    MB --> AE
    OWN --> AE

    AE --> DB

    style AE fill:#1E3A5F,color:#fff
    style CHAT fill:#D4A03C,color:#000
    style ADMIN fill:#D4A03C,color:#000
    style MCP fill:#2E7D7B,color:#fff
    style DB fill:#4A7C59,color:#fff
    style DIS fill:#8B8B8B,color:#fff
    style MB fill:#8B8B8B,color:#fff
    style OWN fill:#8B8B8B,color:#fff
```

### 4.2 Technology Stack

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'background': '#fcfaf5', 'primaryColor': '#1E3A5F', 'lineColor': '#5C5C5C'}}}%%
block-beta
    columns 3

    block:presentation["Presentation Layer"]:3
        CHAT["Chat UI<br/>(React/Next.js)"]
        ADMIN["Admin Dashboard<br/>(React)"]
        VOICE["Voice Agent<br/>(WebRTC)"]
    end

    block:api["API Layer"]:3
        MCP["MCP Server<br/>(Python/FastAPI)"]
        REST["REST API<br/>(Internal)"]
        WS["WebSocket<br/>(Real-time)"]
    end

    block:core["Core Services"]:3
        AE["Attribution Engine<br/>(Python 3.13)"]
        UQ["Uncertainty Module<br/>(Conformal)"]
        SYNC["Sync Service<br/>(Background)"]
    end

    block:data["Data Layer"]:3
        PG["PostgreSQL<br/>(pgvector)"]
        REDIS["Redis<br/>(Cache)"]
        S3["Object Storage<br/>(Backups)"]
    end

    block:external["External Services"]:3
        CLAUDE["Claude API"]
        DISCOGS["Discogs API"]
        MB["MusicBrainz API"]
    end

    style CHAT fill:#D4A03C,color:#000
    style ADMIN fill:#D4A03C,color:#000
    style VOICE fill:#D4A03C,color:#000
    style MCP fill:#4A7C59,color:#fff
    style AE fill:#1E3A5F,color:#fff
    style UQ fill:#1E3A5F,color:#fff
    style PG fill:#2E7D7B,color:#fff
```

**For Stakeholders**: Each layer has a specific responsibility. The presentation layer serves users; the API layer connects to AI platforms; the core services handle business logic; the data layer persists everything.

**For Engineers**: All components use Python except the presentation layer. The MCP Server is the primary integration point for external AI platforms.

| Component | Technology | Rationale |
|-----------|------------|-----------|
| Language | Python 3.13 | Team expertise, AI ecosystem |
| Database | PostgreSQL + pgvector | Relational + vector search |
| API | MCP Protocol | AI-native, tool-use friendly |
| AI | Claude API (Pydantic) | No framework lock-in |
| Infrastructure | Render + Neon | Serverless, low ops |

### 4.3 Integration Points

- **Discogs API**: Artist, release, label data
- **MusicBrainz API**: Artist, recording, work data
- **MCP Protocol**: AI agent access (Claude, ChatGPT, Mogen)
- **OAuth 2.0**: Third-party authentication

### 4.4 Decision Log

| Decision | Options | Chosen | Rationale |
|----------|---------|--------|-----------|
| Database | Postgres/Neo4j | Postgres | ACID, pgvector, simpler ops |
| AI Framework | LangChain/Pure Python | Pure Python | Debuggability, no lock-in |
| UQ Approach | Logits/Conformal | Conformal | API-compatible, formal guarantees |
| Docs Format | LaTeX/Markdown | Markdown | Claude Code native |

## 5. Data Model

### 5.1 Core Entities

- **ArtistID**: Verified artist identity (permanent, portable)
- **Work**: A musical composition or recording
- **Credit**: A claim of contribution (role, confidence, sources)
- **Permission**: AI training consent (per-work or catalog-wide)

### 5.2 Relationships

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'background': '#fcfaf5', 'lineColor': '#5C5C5C'}}}%%
erDiagram
    ARTIST_ID ||--o{ CREDIT : "claims"
    ARTIST_ID ||--o{ PERMISSION : "grants"
    WORK ||--o{ CREDIT : "has"
    WORK ||--o{ PERMISSION : "governed by"

    ARTIST_ID {
        uuid id PK
        string name
        string verified_email
        timestamp created_at
    }

    WORK {
        uuid id PK
        string title
        string isrc
        date release_date
    }

    CREDIT {
        uuid id PK
        string role
        float confidence
        string attribution_level
    }

    PERMISSION {
        uuid id PK
        boolean ai_training
        boolean commercial_use
        timestamp valid_until
    }
```

### 5.3 Confidence Scoring

See [attribution-engine-prd.md](attribution-engine-prd.md) Section 5.3 for full confidence scoring algorithm.

## 6. Implementation Roadmap

### Strategic Roadmap Timeline

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'background': '#fcfaf5', 'primaryColor': '#1E3A5F', 'lineColor': '#5C5C5C'}}}%%
timeline
    title the system Development Roadmap 2026
    section Phase 1: Sprint MVP
        Weeks 1-2 : Attribution Engine Core
                  : Multi-source data adapters
                  : Entity resolution foundation
        Weeks 3-4 : MCP Server v1
                  : Read-only API
                  : Heuristic confidence scoring
    section Phase 2: Identity
        Weeks 5-6 : ArtistID System
                  : Artist verification flow
                  : Chat interface launch
        Weeks 7-8 : Permission Management
                  : Write operations
                  : Consent dashboard
    section Phase 3: Ecosystem
        Weeks 9-12 : Partner Integrations
                   : Mogen integration
                   : Platform onboarding
        Weeks 13-16 : Calibration & Scale
                    : Conformal prediction
                    : Heritage program launch
```

**For Stakeholders**: Each phase has clear success criteria. Phase 1 delivers a working proof-of-concept; Phase 2 enables artist control; Phase 3 builds the ecosystem.

**For Engineers**: Dependencies flow left-to-right. Attribution Engine is the critical path for Phase 1.

### Phase 1: Sprint MVP (Weeks 1-4)

- [ ] Attribution engine with multi-source aggregation
- [ ] Confidence scoring (heuristic, not calibrated)
- [ ] MCP server with read-only access
- [ ] Basic chat interface for gap-filling

**Success criteria**: Can query artist attribution via MCP with confidence scores

### Phase 2: Identity & Permissions (Weeks 5-8)

- [ ] ArtistID creation and verification
- [ ] Permission management dashboard
- [ ] Write operations via MCP (Tier 2)

**Success criteria**: Artists can claim identities and set AI permissions

### Phase 3: Ecosystem Growth (Weeks 9-16)

- [ ] Partner API integrations (Mogen, verified platforms)
- [ ] Calibrated confidence scoring (100+ validation examples)
- [ ] Heritage artist onboarding program

**Success criteria**: 1000+ verified ArtistIDs, 10+ platform integrations

### Value Delivery Curve

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'background': '#fcfaf5', 'primaryColor': '#1E3A5F', 'lineColor': '#5C5C5C'}}}%%
xychart-beta
    title "Cumulative Value Delivery Over Time"
    x-axis ["W1", "W2", "W3", "W4", "W5", "W6", "W7", "W8", "W9", "W10", "W11", "W12", "W13", "W14", "W15", "W16"]
    y-axis "Value Units" 0 --> 100
    bar [5, 10, 15, 25, 35, 45, 55, 65, 72, 78, 84, 90, 93, 96, 98, 100]
    line [5, 10, 15, 25, 35, 45, 55, 65, 72, 78, 84, 90, 93, 96, 98, 100]
```

**For Stakeholders**: The steepest value growth occurs in Phases 1-2 (weeks 1-8). Phase 3 delivers diminishing returns per week but critical ecosystem scale.

**For Engineers**: Front-load architectural decisions. Technical debt accumulated in Phase 1 compounds in later phases.

## 7. Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Attribution accuracy | 90% | Cross-source validation |
| ArtistID creation time | < 5 min | User analytics |
| API response time | < 500ms | P95 latency |
| AI platform adoption | 10+ partners | Contract count |
| Artist satisfaction | 8/10 | NPS survey |

## 8. Risks & Dependencies

### Risk Heat Map

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'background': '#fcfaf5', 'primaryColor': '#1E3A5F', 'lineColor': '#5C5C5C'}}}%%
quadrantChart
    title Risk Assessment Matrix
    x-axis Low Probability --> High Probability
    y-axis Low Impact --> Critical Impact
    quadrant-1 Monitor Closely
    quadrant-2 Critical Risks
    quadrant-3 Accept
    quadrant-4 Mitigate Actively

    API Changes: [0.50, 0.70]
    Low Adoption: [0.50, 0.85]
    Platforms Ignore Permissions: [0.75, 0.55]
    Confidence Score Errors: [0.50, 0.70]
    Regulatory Shift: [0.40, 0.60]
    Major Label Competition: [0.60, 0.75]
    MCP Protocol Changes: [0.30, 0.50]
```

**For Stakeholders**: "Low Artist Adoption" is the highest-impact risk. Mitigation requires community partnerships and frictionless onboarding.

**For Engineers**: "API Changes" and "Confidence Score Errors" are technical risks that require defensive architecture (abstraction layers, validation frameworks).

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Data source API changes | Medium | High | Abstraction layer, caching |
| Low artist adoption | Medium | Critical | Partner with FAC, Imogen Heap network |
| AI platforms ignore permissions | High | Medium | Legal framework, industry pressure |
| Incorrect confidence scores | Medium | High | Validation set, calibration metrics |

## 8.1 Research-Informed Risk Analysis

Per research synthesis ([music-attribution-research-2026-02-03.md](../knowledge-base/domain/music-industry/music-attribution-research-2026-02-03.md)):

### The Oracle Problem (Technical Limits)

**Three things The system CANNOT prove:**
1. A model trained *only* on consented data
2. Output resemblance is causal (not coincidental)
3. A model did *not* learn from a specific work

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'background': '#fcfaf5', 'primaryColor': '#1E3A5F', 'lineColor': '#5C5C5C'}}}%%
graph LR
    subgraph barriers[" Three Epistemic Barriers "]
        B1[Training<br/>Verification]
        B2[Influence<br/>Attribution]
        B3[Absence<br/>Proof]
    end

    subgraph limits[" What Cannot Be Proven "]
        L1[Model trained<br/>only on consent]
        L2[Resemblance<br/>is causal]
        L3[Model did not<br/>learn from X]
    end

    subgraph response[" System Response "]
        R1[Deterrence<br/>not Detection]
        R2[Evidence Strength<br/>not Proof]
        R3[Consent Before<br/>not After]
    end

    B1 -.->|✗| L1
    B2 -.->|✗| L2
    B3 -.->|✗| L3

    L1 --> R1
    L2 --> R2
    L3 --> R3

    style B1 fill:#8B8B8B,color:#fff
    style B2 fill:#8B8B8B,color:#fff
    style B3 fill:#8B8B8B,color:#fff
    style L1 fill:#D4A03C,color:#000
    style L2 fill:#D4A03C,color:#000
    style L3 fill:#D4A03C,color:#000
    style R1 fill:#4A7C59,color:#fff
    style R2 fill:#4A7C59,color:#fff
    style R3 fill:#4A7C59,color:#fff
```

**Research basis**: [Morreale et al. (2025)](https://arxiv.org/abs/2510.08062) "Attribution-by-design: Ensuring Inference-Time Provenance in Generative Music Systems" — similarity does not imply causation.

**Mitigation**: Position confidence as "evidence strength for compliant participants"—deterrence-based, not detection-based.

### Three Market Failures the system Addresses

| Market Failure | Research Basis | System Response |
|----------------|----------------|-------------------|
| **Incomplete Property Rights** | "Style" isn't copyrightable (Teikari, 2026) | Create tradable permission bundles |
| **Information Asymmetry** | Artists don't know if they're in training sets (Longpre, 2024) | Transparent provenance tracking |
| **Market Power** | Major labels negotiate, independents don't (Heap, 2025) | MCP enables direct artist-platform negotiation |

### The "Slop" Opportunity

Per Madsen & Puyt (2025): When AI content floods markets, verified human provenance becomes a **market differentiator**. The system provides this costly signal.

## 9. Cross-References

### Related PRDs

- [attribution-engine-prd.md](attribution-engine-prd.md) - Core engine details
- [chat-interface-prd.md](chat-interface-prd.md) - Conversational UX
- [mcp-server-prd.md](mcp-server-prd.md) - API specification

### Knowledge Base

- [domain/attribution/](../knowledge-base/domain/attribution/) - A0-A3 framework
- [technical/uncertainty/](../knowledge-base/technical/uncertainty/) - UQ approaches

### External References

- [Imogen Heap: What Do Musicians Do About GenAI?](https://medium.com/@imogenheap/what-do-musicians-do-about-genai-3ff458f955f0)
- [MCP Specification](https://modelcontextprotocol.io/)
- [Creative Passport (predecessor)](https://www.creativepassport.net/)

### Research Synthesis

- [music-attribution-research-2026-02-03.md](../knowledge-base/domain/music-industry/music-attribution-research-2026-02-03.md) - 200+ paper synthesis with actionable insights

## 10. Unknown Unknowns

### What We Don't Know We Don't Know

This section captures areas where our assumptions may be fundamentally wrong, beyond the known risks above.

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'background': '#fcfaf5', 'primaryColor': '#1E3A5F', 'lineColor': '#5C5C5C'}}}%%
mindmap
  root((Unknown<br/>Unknowns))
    Artist Behavior
      Will artists actually fill gaps?
      Chat fatigue risk
      Heritage artist digital literacy
    Market Dynamics
      AI platform consolidation
      New competing standards
      Regulatory pivots
    Technical Surprises
      Entity resolution at scale
      Cross-language names
      Future source integrations
    Business Model
      Willingness to pay
      Rights org resistance
      Major label competition
```

#### Areas of Deep Uncertainty

| Domain | Unknown Unknown | Mitigation Approach |
|--------|-----------------|---------------------|
| **User Adoption** | Artists may find even chat-based data entry tedious | A/B test engagement; consider voice-first interface |
| **Data Quality** | Entity resolution may fail for non-Western names | Partner with international music communities early |
| **Market Timing** | AI regulation may shift faster than we can adapt | Build flexible permission model, monitor policy closely |
| **Competition** | Major labels may build their own systems | Focus on indie artist value proposition |
| **Technical Debt** | MCP protocol may evolve incompatibly | Abstract protocol layer, stay close to spec committee |

#### Questions for Domain Experts

See [UNKNOWNS-FOR-DOMAIN-EXPERTS.md](UNKNOWNS-FOR-DOMAIN-EXPERTS.md) for structured questions that only Imogen, Andy, and industry insiders can answer.

---

## 11. Hierarchical PRD Navigation

### PRD Ecosystem

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'background': '#fcfaf5', 'primaryColor': '#1E3A5F', 'lineColor': '#5C5C5C'}}}%%
graph TB
    subgraph level1[" L1: Vision "]
        VISION[vision-v1<br/>THIS DOCUMENT]
    end

    subgraph level2[" L2: Domain PRDs "]
        AE[attribution-engine/]
        CI[chat-interface/]
        MCP[mcp-server/]
        DL[data-layer/]
    end

    subgraph cross[" Cross-Cutting "]
        UQ[uncertainty/]
        OBS[observability/]
        SEC[security/]
        IP[identity-permissions/]
    end

    subgraph support[" Support Docs "]
        REJ[REJECTED.md]
        SYN[SYNTHESIS.md]
        LLM[llm-context.md]
    end

    VISION --> AE
    VISION --> CI
    VISION --> MCP
    VISION --> DL

    AE --> UQ
    AE --> OBS
    CI --> UQ
    MCP --> SEC

    style VISION fill:#1E3A5F,color:#fff
    style AE fill:#2E7D7B,color:#fff
    style CI fill:#D4A03C,color:#000
    style MCP fill:#4A7C59,color:#fff
    style DL fill:#8B8B8B,color:#fff
    style UQ fill:#C75050,color:#fff
    style OBS fill:#C75050,color:#fff
    style SEC fill:#C75050,color:#fff
```

### Navigation Guide

| Level | Documents | Purpose |
|-------|-----------|---------|
| **L1** | This document | Master vision, stakeholder alignment |
| **L2** | Domain TOCs | Component-specific requirements |
| **L3** | Feature PRDs | Detailed implementation specs |
| **Cross** | Uncertainty, Observability, Security | Shared concerns across domains |

**Start Here**:
- New to project? Read [llm-context.md](llm-context.md) first
- Technical deep-dive? Start with [attribution-engine/toc-attribution-engine.md](attribution-engine/toc-attribution-engine.md)
- UX focus? Start with [chat-interface/toc-chat-interface.md](chat-interface/toc-chat-interface.md)
- API integration? Start with [mcp-server/toc-mcp-server.md](mcp-server/toc-mcp-server.md)

---

## Appendices

### A. Glossary

| Term | Definition |
|------|------------|
| **ArtistID** | Verified artist identity in the system system |
| **MCP** | Model Context Protocol - AI agent communication standard |
| **A0-A3** | Attribution assurance levels (Unknown → Verified) |
| **pgvector** | PostgreSQL extension for vector similarity search |
| **Conformal Prediction** | Statistical method for providing formal confidence guarantees |
| **ITA** | Inference-Time Attribution - attribution applied at generation, not training |

### B. Open Questions

1. How to handle disputed credits between artists?
2. What's the minimum validation set size for calibrated confidence?
3. Should permissions be transferable with catalog sales?
4. What is the optimal confidence threshold for auto-population vs. manual review?
5. How do we handle non-Latin character names in entity resolution?

### C. Stakeholder Map

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'background': '#fcfaf5', 'primaryColor': '#1E3A5F', 'lineColor': '#5C5C5C'}}}%%
graph TB
    subgraph primary[" Primary Stakeholders "]
        A1[Independent<br/>Artists]
        A2[Heritage<br/>Artists]
        A3[Session<br/>Musicians]
    end

    subgraph secondary[" Secondary Stakeholders "]
        B1[Managers]
        B2[Labels]
        B3[Rights Orgs]
    end

    subgraph platforms[" Platform Partners "]
        C1[Mogen]
        C2[ChatGPT]
        C3[Streaming<br/>Services]
    end

    subgraph regulators[" Regulators "]
        D1[EU AI Act]
        D2[PROs]
        D3[Industry<br/>Bodies]
    end

    AUR((The System))

    A1 --> AUR
    A2 --> AUR
    A3 --> AUR
    B1 --> AUR
    B2 --> AUR
    B3 --> AUR
    AUR --> C1
    AUR --> C2
    AUR --> C3
    D1 -.->|Compliance| AUR
    D2 -.->|Data Feed| AUR
    D3 -.->|Standards| AUR

    style AUR fill:#1E3A5F,color:#fff
    style A1 fill:#D4A03C,color:#000
    style A2 fill:#D4A03C,color:#000
    style A3 fill:#D4A03C,color:#000
    style C1 fill:#4A7C59,color:#fff
    style C2 fill:#4A7C59,color:#fff
```

### D. Reviewer Feedback Log

| Date | Reviewer | Feedback | Resolution |
|------|----------|----------|------------|
| 2026-02-03 | Initial draft | - | - |
| 2026-02-04 | Structure review | Add unknown unknowns, hierarchical navigation | Added sections 10-11 |
