# fig-repo-02: Five-Pipeline Architecture

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-repo-02 |
| **Title** | Five-Pipeline Architecture: ETL to Chat |
| **Audience** | Technical (developers, contributors) |
| **Complexity** | L2 (system architecture) |
| **Location** | README.md architecture section, docs/architecture/README.md |
| **Priority** | P0 (Critical) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This is the single most important technical diagram in the repository. It shows the five-pipeline data flow from raw external sources through to the conversational chat interface. Each pipeline is a distinct module with well-defined boundary objects (Pydantic models) at each transition point.

The key message is: "Data flows left-to-right through five sequential pipelines, with Pydantic boundary objects ensuring type-safe handoffs at every stage."

## Visual Concept (ASCII Layout)

```
+-----------------------------------------------------------------------+
|  FIVE-PIPELINE ARCHITECTURE                                            |
|  ■ Data Flow: Source to Conversation                                   |
+-----------------------------------------------------------------------+
|                                                                        |
|  I              II               III              IV            V      |
|  ETL            ENTITY           ATTRIBUTION      API /         CHAT   |
|  PIPELINE       RESOLUTION       ENGINE           MCP                  |
|                                                                        |
|  ┌─────────┐   ┌─────────────┐  ┌────────────┐  ┌──────────┐  ┌────┐ |
|  │ Discogs │   │             │  │            │  │ FastAPI  │  │    │ |
|  │ MBrainz │──▶│  Fuzzy      │─▶│ Confidence │─▶│ REST     │─▶│ AI │ |
|  │ System  │   │  Match +    │  │ Scoring +  │  │ MCP      │  │Chat│ |
|  │ Own     │   │  Dedupe     │  │ Provenance │  │ Server   │  │    │ |
|  └─────────┘   └─────────────┘  └────────────┘  └──────────┘  └────┘ |
|       │              │                │               │           │    |
|  NormalizedRecord  ResolvedEntity  AttributionRecord  JSON API   SSE  |
|  (Pydantic)       (Pydantic)       (Pydantic)        + MCP     AG-UI |
|                                                                        |
|  ┌─────────────────────────────────────────────────────────────────┐  |
|  │  CROSS-CUTTING: BatchEnvelope │ DriftDetector │ PipelineFeedback│  |
|  └─────────────────────────────────────────────────────────────────┘  |
|                                                                        |
|  ■ PostgreSQL + pgvector (persistence layer beneath all pipelines)     |
+-----------------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title | `heading_display` | "FIVE-PIPELINE ARCHITECTURE" Instrument Serif ALL-CAPS |
| Roman numerals I-V | `section_numeral` | Pipeline identifiers above each stage |
| Pipeline I: ETL | `pipeline_stage` | Three source icons converging into normalizer |
| Pipeline II: Entity Resolution | `pipeline_stage` | Fuzzy matching and deduplication |
| Pipeline III: Attribution Engine | `pipeline_stage` | Confidence scoring and provenance |
| Pipeline IV: API/MCP | `pipeline_stage` | FastAPI REST + MCP permission server |
| Pipeline V: Chat | `pipeline_stage` | PydanticAI agent with AG-UI streaming |
| Flow arrows | `primary_pathway` | Coral accent arrows left-to-right between stages |
| Boundary objects row | `data_mono` | NormalizedRecord, ResolvedEntity, AttributionRecord in IBM Plex Mono |
| Cross-cutting bar | `infrastructure_bar` | BatchEnvelope, DriftDetector, PipelineFeedback |
| PostgreSQL bar | `storage_layer` | Database cylinder or bar at bottom |
| Accent squares | `accent_square` | Coral squares as visual punctuation |

## Anti-Hallucination Rules

1. Exactly FIVE pipelines in this exact order: ETL, Entity Resolution, Attribution Engine, API/MCP, Chat.
2. Boundary objects are: NormalizedRecord, ResolvedEntity, AttributionRecord -- these are actual Pydantic models in the codebase.
3. Cross-cutting concerns are: BatchEnvelope, DriftDetector, PipelineFeedback -- all real classes.
4. The database is PostgreSQL with pgvector extension, not MySQL or MongoDB.
5. The MCP server is for machine-readable permission queries, not a generic microservice protocol.
6. Chat uses PydanticAI (not LangChain, not CrewAI) with AG-UI protocol via CopilotKit.
7. Do NOT add pipelines that do not exist (no "ML Training Pipeline" or "Analytics Pipeline").
8. Arrow direction is strictly left-to-right; there are no backwards flows in this diagram.

## Alt Text

Horizontal five-stage pipeline: ETL ingests from Discogs/MusicBrainz/System, Entity Resolution deduplicates, Attribution Engine scores confidence, API/MCP exposes data, Chat provides AI conversation.
