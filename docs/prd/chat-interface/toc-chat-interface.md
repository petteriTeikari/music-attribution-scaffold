---
id: chat-interface/toc-chat-interface
title: Chat Interface - Table of Contents
status: active
version: 0.1.0
last_updated: 2026-02-04
priority: high

requires:
  - vision-v1.md#executive-summary
  - llm-context.md

cross_refs:
  - attribution-engine/toc-attribution-engine.md
  - attribution-engine/confidence-scoring.md
  - voice-agent/toc-voice-agent.md
  - observability/langfuse.md

tags:
  - chat
  - gap-filling
  - user-interface
  - conversational

changelog:
  - version: "0.1.0"
    date: 2026-02-04
    changes: "Initial structure based on Imogen's two-role chat vision"
---

# Chat Interface

**Purpose**: Conversational interface for attribution gap-filling and data exploration

**Key Insight from Imogen**: "Fill in the gaps in a conversational way whilst the documents are on screen. Adding this information is so bloody boring - make it fun through conversation."

---

## System Architecture

```mermaid
flowchart TB
    subgraph Users["User Types"]
        ARTIST[/"Artist<br/>(Role 1: Data Gathering)"/]
        EXTERNAL[/"External Party<br/>(Role 2: Query)"/]
    end

    subgraph ChatInterface["Chat Interface System"]
        direction TB

        subgraph SessionMgmt["Session Management"]
            AUTH[Authentication]
            ROLE[Role Detection]
            CTX[Context Loader]
        end

        subgraph ConversationEngine["Conversation Engine"]
            NLU[Intent Recognition]
            MEM[Multi-Turn Memory]
            GEN[Response Generator]
        end

        subgraph GapFilling["Gap-Filling System (Role 1)"]
            TRIGGER[Confidence Trigger]
            PROMPT[Smart Prompts]
            EXTRACT[Data Extraction]
            VALIDATE[Validation]
        end

        subgraph QuerySystem["Query System (Role 2)"]
            PARSE[Query Parser]
            PERM[Permission Check]
            RESP[Response Formatter]
        end
    end

    subgraph Backend["Backend Services"]
        ATTR[Attribution Engine]
        LANG[Langfuse<br/>Observability]
        LLM[LLM Provider]
    end

    subgraph UILayer["UI Integration"]
        DOC[Document Viewer]
        CHATUI[Chat Panel]
        NOTIF[Notifications]
    end

    ARTIST --> AUTH
    EXTERNAL --> AUTH
    AUTH --> ROLE
    ROLE -->|Artist| CTX
    ROLE -->|External| PARSE

    CTX --> TRIGGER
    TRIGGER --> PROMPT
    PROMPT --> GEN
    GEN --> NLU
    NLU --> MEM
    MEM --> GEN

    EXTRACT --> VALIDATE
    VALIDATE --> ATTR

    PARSE --> PERM
    PERM --> RESP
    RESP --> ATTR

    GEN --> LLM
    NLU --> LLM
    GEN --> LANG

    CHATUI --> DOC
    CHATUI --> NOTIF

    style ARTIST fill:#90EE90
    style EXTERNAL fill:#87CEEB
```

### Conversation State Flow

```mermaid
stateDiagram-v2
    [*] --> Idle: User opens chat

    Idle --> GapDetected: Low confidence field found
    Idle --> UserQuery: User asks question

    GapDetected --> PromptGenerated: Generate contextual prompt
    PromptGenerated --> WaitingResponse: Display prompt
    WaitingResponse --> ResponseReceived: User responds
    ResponseReceived --> Extracting: Parse response
    Extracting --> Validating: Extract structured data
    Validating --> Updated: Validation passes
    Validating --> Clarifying: Needs clarification
    Clarifying --> WaitingResponse: Ask follow-up
    Updated --> Celebrating: Show success
    Celebrating --> Idle: Continue or next gap

    UserQuery --> Processing: Parse intent
    Processing --> Answering: Generate response
    Answering --> Idle: Display response

    state "Role 1: Gap Filling" as GapFilling {
        GapDetected
        PromptGenerated
        WaitingResponse
        ResponseReceived
        Extracting
        Validating
        Updated
        Clarifying
        Celebrating
    }

    state "Role 2: Query" as Query {
        UserQuery
        Processing
        Answering
    }
```

---

## For Domain Experts (Imogen/Andy)

### Why This Matters

The Chat Interface is where The system transforms from a database into an **engaging experience**. Your insight that "adding this information is so bloody boring" is the core design challenge we're solving.

**Business Value:**
- **Completion Rates**: Conversational interfaces typically see 3-5x higher data completion rates than forms. For the system, this means dramatically more complete attribution data.
- **Artist Retention**: A chat that feels helpful rather than demanding keeps artists coming back. This is your primary engagement touchpoint.
- **Data Quality**: Natural language responses often contain richer context than form fields. "Dave mixed it at Electric Lady, we spent three weeks there" gives us location, duration, and relationship data.

### Key Decisions Requiring Your Input

1. **Tone & Personality**: Should the chat agent have a distinct personality? Warm and encouraging? Professional and efficient? Should it adapt to the artist's style?

2. **Progressive Disclosure**: How many gaps should we address per session? One at a time? Batch related questions? Let the artist choose?

3. **Context Presentation**: When chatting about a track, how much of the document should be visible? Full credits? Just the gaps? Should we highlight what we're asking about?

4. **Celebration Design**: What makes "filling a gap" feel rewarding? Animations? Progress meters? Gamification elements?

---

## Known Unknowns

> Questions requiring domain expertise or further research before implementation.

| Question | Impact | Suggested Owner |
|----------|--------|-----------------|
| What conversation length is optimal before artists disengage? | High - affects prompt batching | Imogen (user research) |
| Should external parties (Role 2) see confidence scores, or just answers? | Medium - affects trust/UX | Product + Legal |
| How do we handle artists who want to dispute existing data? | High - workflow design | Imogen |
| What's the escalation path when chat can't resolve a gap? | Medium - voice agent integration | Engineering |
| Should we allow artists to "skip" certain gap types permanently? | Medium - data completeness tradeoff | Product |
| How do we handle multilingual artists? | Medium - internationalization | Engineering + Domain |
| What happens when an artist provides contradictory information across sessions? | High - data integrity | Engineering |

---

## Overview

The Chat Interface serves two distinct roles per Imogen's guidance:

| Role | Purpose | User |
|------|---------|------|
| **Role 1: Data Gathering** | Gather and edit attribution data | Artist filling gaps |
| **Role 2: Data Exploration** | Allow queries against attribution data | External parties |

## Core Capabilities

| Capability | Description | PRD |
|------------|-------------|-----|
| **Conversational Gap-Filling** | Engage artist in natural dialogue to fill attribution gaps | [conversational-gap-filling.md](conversational-gap-filling.md) |
| **Confidence-Driven Prompts** | Trigger chat from medium/low confidence fields | [confidence-driven-prompts.md](confidence-driven-prompts.md) |
| **Document-Aware Context** | Chat while documents are visible on screen | [document-aware-context.md](document-aware-context.md) |
| **Multi-Turn Memory** | Remember context across conversation | [multi-turn-memory.md](multi-turn-memory.md) |
| **External Query Interface** | Role 2: Let others query artist's data | [external-query-interface.md](external-query-interface.md) |

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                      CHAT INTERFACE                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Role 1: Data Gathering          Role 2: Data Exploration       │
│  ──────────────────────          ────────────────────────       │
│                                                                 │
│  ┌─────────────┐                 ┌─────────────┐               │
│  │   Artist    │                 │  External   │               │
│  │   Session   │                 │   Query     │               │
│  └──────┬──────┘                 └──────┬──────┘               │
│         │                               │                       │
│         ▼                               ▼                       │
│  ┌─────────────┐                 ┌─────────────┐               │
│  │ Gap-Filling │                 │   Read-Only │               │
│  │   Prompts   │                 │   Answers   │               │
│  └──────┬──────┘                 └──────┬──────┘               │
│         │                               │                       │
│         ▼                               ▼                       │
│  ┌──────────────────────────────────────────────┐              │
│  │              Attribution Engine               │              │
│  │         (Confidence-Scored Data)              │              │
│  └──────────────────────────────────────────────┘              │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Gap-Filling Flow (Role 1)

Per Andy's insight, chat prompts are triggered by confidence levels:

```
Attribution Engine detects LOW confidence field
    ↓
┌─────────────────────────────────────────────────────────────┐
│ CHAT PROMPT GENERATION                                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Source Analysis                 Prompt Generation          │
│  ───────────────                ─────────────────          │
│                                                             │
│  "Only Discogs has      →      "I see you worked with      │
│   producer credit"              [name] on this track.       │
│                                 Can you tell me about       │
│  "Sources disagree"     →       their role?"                │
│                                                             │
│  "No data available"    →      "Who produced this track?"  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
    ↓
Artist responds naturally
    ↓
Extract structured data from response
    ↓
Update attribution with artist-confirmed data (highest confidence)
```

## Making It Fun

Per Imogen: "Adding this information is so bloody boring - make it fun"

| Strategy | Implementation |
|----------|----------------|
| **Conversational tone** | Natural dialogue, not form filling |
| **Progressive disclosure** | Ask about one thing at a time |
| **Context awareness** | Reference what's visible on screen |
| **Memory** | "Last time you mentioned..." |
| **Celebrate wins** | Acknowledge when gaps are filled |

## Implementation Priority

1. **conversational-gap-filling.md** - Core functionality
2. **confidence-driven-prompts.md** - Integration with attribution engine
3. **document-aware-context.md** - Screen context awareness
4. **multi-turn-memory.md** - Conversation state
5. **external-query-interface.md** - Role 2 (later phase)

## Cross-Cutting Dependencies

| Concern | Integration Point |
|---------|-------------------|
| **Attribution Engine** | Confidence scores trigger prompts |
| **Voice Agent** | Chat can escalate to voice for complex gaps |
| **Observability** | Track gap-fill success rates in Langfuse |
| **MCP Server** | Expose Role 2 queries via MCP |

## Related Documents

- [vision-v1.md](../vision-v1.md) - Product vision
- [attribution-engine/confidence-scoring.md](../attribution-engine/confidence-scoring.md) - What triggers chat
- [voice-agent/toc-voice-agent.md](../voice-agent/toc-voice-agent.md) - Voice alternative
- [observability/langfuse.md](../observability/langfuse.md) - Conversation tracking
