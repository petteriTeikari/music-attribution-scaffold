# Architecture Documentation

This directory contains architectural documentation and decision records for the Music Attribution Scaffold.

## System Architecture

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'background': '#fcfaf5', 'primaryColor': '#1E3A5F', 'lineColor': '#5C5C5C'}}}%%
graph TB
    subgraph external[" External Sources "]
        DIS[Discogs API]
        MB[MusicBrainz API]
    end

    subgraph security[" Security Layers "]
        AUTH[OAuth 2.0<br/>Authentication]
        VALID[Input Validation<br/>Injection Prevention]
        SANDBOX[Capability<br/>Sandbox]
        AUDIT[Audit Trail<br/>EU AI Act]
    end

    subgraph core[" Attribution Core "]
        AE[Attribution Engine]
        MCP[MCP Server]
        CHAT[Chat Interface]
        DB[(PostgreSQL<br/>+ pgvector)]
    end

    subgraph clients[" Clients "]
        AI[AI Platforms<br/>Tier 2-3]
        WEB[Web App<br/>Artists]
        INT[Internal Apps<br/>Tier 1]
    end

    DIS --> AE
    MB --> AE
    AE --> DB
    DB --> MCP
    DB --> CHAT

    AI --> AUTH
    WEB --> AUTH
    INT --> AUTH
    AUTH --> VALID
    VALID --> SANDBOX
    SANDBOX --> MCP
    SANDBOX --> CHAT
    MCP --> AUDIT
    CHAT --> AUDIT

    style AE fill:#1E3A5F,color:#fff
    style MCP fill:#2E7D7B,color:#fff
    style CHAT fill:#D4A03C,color:#000
    style DB fill:#4A7C59,color:#fff
    style DIS fill:#8B8B8B,color:#fff
    style MB fill:#8B8B8B,color:#fff
    style AI fill:#8B8B8B,color:#fff
    style WEB fill:#8B8B8B,color:#fff
    style INT fill:#8B8B8B,color:#fff
    style AUTH fill:#4A7C59,color:#fff
    style VALID fill:#2E7D7B,color:#fff
    style SANDBOX fill:#1E3A5F,color:#fff
    style AUDIT fill:#D4A03C,color:#000
```

### Security Architecture

Per [MCP security research](../knowledge-base/technical/agentic-systems-research-2026-02-03.md), the system implements defense-in-depth:

| Layer | Function | Threat Mitigated |
|-------|----------|------------------|
| **Authentication** | OAuth 2.0 + RFC 8707 Resource Indicators | Unauthorized access |
| **Input Validation** | Static + Neural + LLM three-stage detection | Prompt injection, SQL injection |
| **Capability Sandbox** | Permission grants with expiration | Privilege escalation |
| **Audit Trail** | Immutable logging (EU AI Act Art. 12) | Non-compliance, liability |

**Research basis**: 40.71% average attack success rate across MCP implementations (MCPSecBench 2025).

## Technical Diagrams (Generated)

### Attribution Pipeline

![Attribution Pipeline](../figures/assets/fig-tech-01-attribution-pipeline.jpg)

*Multi-source data flows through entity resolution to produce unified entities with per-field confidence scores.*

### MCP Server Architecture

![MCP Architecture](../figures/assets/fig-tech-02-mcp-architecture.jpg)

*MCP server exposes attribution data via tools, resources, and prompts with three-tier access control.*

### Confidence Scoring

![Confidence Scoring](../figures/assets/fig-tech-03-confidence-scoring.jpg)

*Conformal prediction provides calibrated uncertainty bounds on attribution confidence.*

### Database Schema

![Database Schema](../figures/assets/fig-tech-04-database-schema.jpg)

*PostgreSQL + pgvector schema for artists, tracks, contributions with full provenance tracking.*

### MCP Access Control (Visual)

![Backstage / VIP / General — The Three-Tier Trust Model](../figures/assets/fig-mcp-01-backstage-vip-general.jpg)
*Your data, your rules. We just make sure the right people get the right level of access.*

### Chat Interface Processing

![Conversation as Cochlea — How Your Words Become Verified Credits](../figures/assets/fig-chat-01-conversation-as-cochlea.jpg)
*Natural language input is transformed into structured, verified credit data.*

---

## L3: Sequence Diagrams

### Entity Resolution Flow

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'background': '#fcfaf5', 'actorLineColor': '#5C5C5C'}}}%%
sequenceDiagram
    participant C as Client
    participant AE as Attribution Engine
    participant DIS as Discogs
    participant MB as MusicBrainz
    participant DB as PostgreSQL

    C->>AE: Query artist "John Smith"

    par Fetch from sources
        AE->>DIS: GET /artists/search
        DIS-->>AE: Candidates[]
    and
        AE->>MB: GET /artist/?query=
        MB-->>AE: Candidates[]
    end

    AE->>AE: Entity Resolution<br/>(fuzzy match, ID match)
    AE->>AE: Conflict Resolution<br/>(voting + authority)
    AE->>AE: Confidence Scoring

    AE->>DB: Upsert unified entity
    DB-->>AE: entity_id

    AE-->>C: UnifiedEntity + confidence
```

### MCP Request Flow

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'background': '#fcfaf5', 'actorLineColor': '#5C5C5C'}}}%%
sequenceDiagram
    participant AI as AI Platform
    participant MCP as MCP Server
    participant AUTH as Auth Service
    participant AE as Attribution Engine
    participant DB as PostgreSQL

    AI->>MCP: Tool call: get_artist_attribution
    MCP->>AUTH: Validate OAuth token
    AUTH-->>MCP: ClientInfo (tier, scopes)

    alt Tier 3 (Public)
        MCP->>MCP: Apply rate limit (100/hr)
    else Tier 2 (Verified)
        MCP->>MCP: Apply rate limit (1000/hr)
    end

    MCP->>AE: Fetch attribution
    AE->>DB: Query unified_entities
    DB-->>AE: Entity data
    AE-->>MCP: ArtistAttributionResponse

    MCP->>MCP: Log audit trail
    MCP-->>AI: JSON response
```

---

## L4: Data Models

### Database ER Diagram

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'background': '#fcfaf5'}}}%%
erDiagram
    SOURCE_RECORDS ||--o{ ENTITY_LINKS : "links to"
    UNIFIED_ENTITIES ||--o{ ENTITY_LINKS : "has"
    UNIFIED_ENTITIES ||--o{ FIELD_CONFIDENCE : "tracks"
    UNIFIED_ENTITIES ||--o{ CREDITS : "has"
    WORKS ||--o{ CREDITS : "has"
    ARTIST_IDS ||--o{ CREDITS : "claims"
    ARTIST_IDS ||--o{ PERMISSIONS : "grants"
    WORKS ||--o{ PERMISSIONS : "governed by"

    SOURCE_RECORDS {
        uuid id PK
        text source_name
        text source_id
        text record_type
        jsonb raw_data
        timestamptz fetched_at
    }

    UNIFIED_ENTITIES {
        uuid id PK
        text entity_type
        text canonical_name
        float overall_confidence
        jsonb metadata
    }

    ENTITY_LINKS {
        uuid source_record_id FK
        uuid unified_entity_id FK
        float match_confidence
        text match_method
    }

    FIELD_CONFIDENCE {
        uuid unified_entity_id FK
        text field_name
        text field_value
        float confidence
        text[] sources
    }

    ARTIST_IDS {
        uuid id PK
        text name
        text verified_email
        timestamptz created_at
    }

    WORKS {
        uuid id PK
        text title
        text isrc
        date release_date
    }

    CREDITS {
        uuid id PK
        text role
        float confidence
        text attribution_level
    }

    PERMISSIONS {
        uuid id PK
        boolean ai_training
        boolean commercial_use
        timestamptz valid_until
    }
```

### Attribution Level State Machine

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'background': '#fcfaf5'}}}%%
stateDiagram-v2
    direction LR

    [*] --> A0

    A0: A0 Unknown
    A1: A1 Claimed
    A2: A2 Corroborated
    A3: A3 Verified

    A0 --> A1: Artist claims credit
    A1 --> A2: External source confirms
    A2 --> A3: Multiple sources agree<br/>(confidence > 0.8)

    A1 --> A0: Claim retracted
    A2 --> A1: Source removed
    A3 --> A2: Confidence drops

    note right of A3
        Highest trust level
        Multiple independent
        sources agree
    end note
```

### Confidence Scoring Algorithm

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'background': '#fcfaf5', 'primaryColor': '#1E3A5F', 'lineColor': '#5C5C5C'}}}%%
graph TD
    INPUT[Source Data] --> COUNT[Count agreeing<br/>sources]
    COUNT --> RATIO[Agreement ratio<br/>n_agree / n_total]

    INPUT --> WEIGHT[Apply authority<br/>weights]
    WEIGHT --> BOOST[Authority boost<br/>avg weighted score]

    RATIO --> COMBINE[Combine scores<br/>0.7 × ratio + 0.3 × boost]
    BOOST --> COMBINE

    COMBINE --> CAP[Cap at 0.95]
    CAP --> LEVEL{Assign level}

    LEVEL -->|≥0.8 + artist| VERIFIED[verified]
    LEVEL -->|≥0.8| HIGH[high]
    LEVEL -->|≥0.7| MEDIUM[medium]
    LEVEL -->|<0.7| LOW[low]

    style INPUT fill:#8B8B8B,color:#fff
    style COMBINE fill:#1E3A5F,color:#fff
    style LEVEL fill:#D4A03C,color:#000
    style VERIFIED fill:#4A7C59,color:#fff
    style HIGH fill:#4A7C59,color:#fff
    style MEDIUM fill:#2E7D7B,color:#fff
    style LOW fill:#C75050,color:#fff
```

## Architecture Decision Records

| ADR | Title | Status | Date |
|-----|-------|--------|------|
| [0001](adr/0001-use-postgresql-pgvector.md) | Use PostgreSQL + pgvector | Accepted | 2026-02-03 |
| [0002](adr/0002-pure-markdown-no-latex.md) | Pure Markdown Documentation | Accepted | 2026-02-03 |
| [0003](adr/0003-pure-python-no-langchain.md) | Pure Python + Pydantic | Accepted | 2026-02-03 |
| [0004](adr/0004-conformal-prediction-mapie.md) | Conformal Prediction via MAPIE | Accepted | 2026-02-03 |
| [0005](adr/0005-single-agent-architecture.md) | Single-Agent Attribution Pipeline | Accepted | 2026-02-03 |

## Related Documentation

- [PRDs](../prd/README.md) - Product requirements
- [Knowledge Base](../knowledge-base/README.md) - Domain and technical knowledge
