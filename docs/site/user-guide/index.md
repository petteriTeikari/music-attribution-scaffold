# User Guide

Technical documentation for developers working with the Music Attribution Scaffold.

## Architecture

The scaffold implements a **5-pipeline architecture** where data flows from raw sources to a user-facing application:

```mermaid
graph LR
    subgraph ETL["ETL Pipeline"]
        MB[MusicBrainz] --> NR[NormalizedRecord]
        DC[Discogs] --> NR
        AC[AcoustID] --> NR
        FM[File Metadata] --> NR
        AI[Artist Input] --> NR
    end

    subgraph ER["Entity Resolution"]
        NR --> ID[Identifier Match]
        ID --> SS[String Similarity]
        SS --> EM[Embedding Match]
        EM --> RE[ResolvedEntity]
    end

    subgraph AE["Attribution Engine"]
        RE --> AG[Aggregation]
        AG --> CF[Conformal Calibration]
        CF --> AR[AttributionRecord]
    end

    subgraph API["API Layer"]
        AR --> REST[REST API]
        AR --> MCP[MCP Server]
        AR --> AGUI[AG-UI Endpoint]
    end
```

## Sections

| Guide | What You'll Learn |
|-------|-------------------|
| [Architecture Overview](architecture.md) | 5-pipeline design, cross-cutting concerns, data flow |
| [Backend](backend.md) | Python modules, database, testing, Docker |
| [Frontend](frontend.md) | Next.js pages, design system, components, Jotai state |
| [Agentic UI](agent.md) | PydanticAI agent, CopilotKit, AG-UI protocol |
