# fig-pitch-03: Unified PostgreSQL: Relational + Vector + Graph

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-pitch-03 |
| **Title** | Unified PostgreSQL: Relational + Vector + Graph |
| **Audience** | L2/L3 (PhD/Policy + Engineer) |
| **Location** | docs/planning/managerial-roadmap-planning.md, pitch deck |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | C (Flowchart) |

## Purpose

This figure shows the full system architecture with the 5-pipeline flow and the unified PostgreSQL strategy (relational + pgvector + Apache AGE for graph). It answers: "How does one database serve three data paradigms, and how do the five pipelines connect?"

## Key Message

A single PostgreSQL instance handles relational data, vector embeddings, and graph queries -- eliminating multi-database complexity while powering five attribution pipelines.

## Visual Concept

A left-to-right flowchart showing five pipeline stages as connected blocks, with PostgreSQL as a large unified block beneath them. The database block is subdivided into three zones (relational, vector, graph) to show how one instance serves all needs. Above the pipeline, the frontend (Next.js) and agent layer (PydanticAI) connect to the API stage. The flow emphasizes that data moves through sequential stages but all stages share the same database.

```
+---------------------------------------------------------------+
|  UNIFIED POSTGRESQL ARCHITECTURE                               |
|  ■ Relational + Vector + Graph                                 |
+---------------------------------------------------------------+
|                                                                |
|           [Next.js 15]     [PydanticAI Agent]                  |
|               \                /                               |
|                \              /                                 |
|  ┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐            |
|  │  I   │  │  II  │  │ III  │  │  IV  │  │  V   │            |
|  │ ETL  ├─>│ENTITY├─>│ATTRIB├─>│ API/ ├─>│ CHAT │            |
|  │      │  │RESOLN│  │ENGINE│  │ MCP  │  │      │            |
|  └──┬───┘  └──┬───┘  └──┬───┘  └──┬───┘  └──┬───┘            |
|     |         |         |         |         |                  |
|     v         v         v         v         v                  |
|  ┌─────────────────────────────────────────────────┐           |
|  │              POSTGRESQL 17                       │           |
|  │  ┌──────────┐  ┌──────────┐  ┌──────────┐      │           |
|  │  │Relational│  │ pgvector │  │Apache AGE│      │           |
|  │  │ Tables   │  │ Embeddings│  │  Graph   │      │           |
|  │  └──────────┘  └──────────┘  └──────────┘      │           |
|  └─────────────────────────────────────────────────┘           |
|                                                                |
+---------------------------------------------------------------+
|  ■ "One database, three paradigms, zero sync headaches"        |
+---------------------------------------------------------------+
```

## Spatial Anchors

```yaml
canvas:
  width: 1920
  height: 1080
  background: warm_cream

title_block:
  position: [60, 40]
  width: 1800
  height: 80
  elements:
    - type: heading_display
      text: "UNIFIED POSTGRESQL ARCHITECTURE"
    - type: label_editorial
      text: "Relational + Vector + Graph"

frontend_layer:
  position: [900, 140]
  width: 600
  height: 80
  elements:
    - { id: "nextjs", label: "Next.js 15", position: [950, 160] }
    - { id: "agent", label: "PydanticAI Agent", position: [1250, 160] }

pipeline_stages:
  position: [60, 280]
  width: 1800
  height: 200
  stages:
    - { id: "etl", numeral: "I", label: "ETL", position: [120, 320], size: [280, 160] }
    - { id: "resolution", numeral: "II", label: "ENTITY RESOLUTION", position: [460, 320], size: [280, 160] }
    - { id: "attribution", numeral: "III", label: "ATTRIBUTION ENGINE", position: [800, 320], size: [280, 160] }
    - { id: "api", numeral: "IV", label: "API / MCP", position: [1140, 320], size: [280, 160] }
    - { id: "chat", numeral: "V", label: "CHAT", position: [1480, 320], size: [280, 160] }

database_block:
  position: [120, 560]
  width: 1680
  height: 280
  label: "POSTGRESQL 17"
  sub_zones:
    - { id: "relational", label: "Relational Tables", position: [200, 620], size: [440, 160] }
    - { id: "vector", label: "pgvector Embeddings", position: [720, 620], size: [440, 160] }
    - { id: "graph", label: "Apache AGE Graph", position: [1240, 620], size: [440, 160] }

callout_bar:
  position: [60, 900]
  width: 1800
  height: 120
  elements:
    - type: callout_bar
      text: "One database, three paradigms, zero sync headaches"

arrows:
  - { from: "etl", to: "resolution", type: "arrow" }
  - { from: "resolution", to: "attribution", type: "arrow" }
  - { from: "attribution", to: "api", type: "arrow" }
  - { from: "api", to: "chat", type: "arrow" }
  - { from: "nextjs", to: "api", type: "arrow" }
  - { from: "agent", to: "api", type: "arrow" }
  - { from: "etl", to: "database_block", type: "arrow", direction: "down" }
  - { from: "resolution", to: "database_block", type: "arrow", direction: "down" }
  - { from: "attribution", to: "database_block", type: "arrow", direction: "down" }
  - { from: "api", to: "database_block", type: "arrow", direction: "down" }
  - { from: "chat", to: "database_block", type: "arrow", direction: "down" }
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "UNIFIED POSTGRESQL ARCHITECTURE" with coral accent square |
| Subtitle | `label_editorial` | "Relational + Vector + Graph" |
| ETL stage | `etl_extract` | Pipeline Stage I -- data ingestion and normalization |
| Entity Resolution stage | `entity_resolve` | Pipeline Stage II -- fuzzy matching, deduplication |
| Attribution Engine stage | `source_corroborate` | Pipeline Stage III -- multi-source agreement scoring |
| API/MCP stage | `api_endpoint` | Pipeline Stage IV -- REST and MCP external interface |
| Chat stage | `processing_stage` | Pipeline Stage V -- agent-powered conversational interface |
| PostgreSQL block | `storage_layer` | Unified database with three sub-zones |
| Relational sub-zone | `storage_layer` | Traditional SQL tables for structured data |
| pgvector sub-zone | `storage_layer` | Vector embeddings for similarity search |
| Apache AGE sub-zone | `storage_layer` | Graph queries for relationship traversal |
| Next.js block | `processing_stage` | Frontend application |
| PydanticAI block | `processing_stage` | AI agent layer |
| Roman numerals | `section_numeral` | I through V for pipeline stages |
| Callout bar | `callout_bar` | Bottom insight statement |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| ETL | Entity Resolution | arrow | "normalized records" |
| Entity Resolution | Attribution Engine | arrow | "resolved entities" |
| Attribution Engine | API/MCP | arrow | "attribution records" |
| API/MCP | Chat | arrow | "agent tools" |
| Next.js | API/MCP | arrow | "REST calls" |
| PydanticAI | API/MCP | arrow | "tool invocations" |
| All stages | PostgreSQL | arrow | "shared storage" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| Unified Database | "One database, three paradigms, zero sync headaches" | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- UNIFIED POSTGRESQL ARCHITECTURE
- Relational + Vector + Graph
- ETL
- ENTITY RESOLUTION
- ATTRIBUTION ENGINE
- API / MCP
- CHAT
- POSTGRESQL 17
- Relational Tables
- pgvector Embeddings
- Apache AGE Graph
- Next.js 15
- PydanticAI Agent

### Caption (for embedding in documentation)

Five-stage attribution pipeline (ETL, Entity Resolution, Attribution Engine, API/MCP, Chat) backed by a unified PostgreSQL 17 instance handling relational data, pgvector embeddings, and Apache AGE graph queries -- eliminating multi-database complexity.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- do NOT render them as labels.
2. **Semantic tags are INTERNAL** -- do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- do NOT render them.
4. **Background MUST be warm cream (#f6f3e6)**.
5. **No generic flowchart aesthetics** -- no thick block arrows, no PowerPoint look.
6. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or numbered caption.
7. **No prompt leakage** -- do NOT render style keywords as visible text.

### Figure-Specific Rules

1. Pipeline stages flow left-to-right in order: ETL, Entity Resolution, Attribution Engine, API/MCP, Chat.
2. PostgreSQL version is 17 -- do NOT use 15 or 16.
3. Vector extension is pgvector -- do NOT use "pg_vector" or "PostgreSQL vectors."
4. Graph extension is Apache AGE -- do NOT use Neo4j or other graph databases.
5. The agent framework is PydanticAI -- do NOT use LangChain or LlamaIndex.
6. The frontend is Next.js 15 (App Router) -- do NOT use React alone or older Next.js.
7. All five pipeline stages connect to the SAME PostgreSQL instance -- show unified, not separate databases.
8. L2/L3 audience: technology names (pgvector, AGE, PydanticAI) ARE appropriate to show.

## Alt Text

Five-pipeline architecture with unified PostgreSQL handling relational, vector, and graph data.

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "pitch-03",
    "title": "Unified PostgreSQL: Relational + Vector + Graph",
    "audience": "L2/L3",
    "layout_template": "C"
  },
  "content_architecture": {
    "primary_message": "A single PostgreSQL instance handles relational, vector, and graph data for five attribution pipelines.",
    "layout_flow": "left-to-right",
    "key_structures": [
      {
        "name": "Pipeline Stages",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["I ETL", "II Entity Resolution", "III Attribution Engine", "IV API/MCP", "V Chat"]
      },
      {
        "name": "PostgreSQL Unified",
        "role": "storage_layer",
        "is_highlighted": true,
        "labels": ["Relational Tables", "pgvector Embeddings", "Apache AGE Graph"]
      },
      {
        "name": "Frontend + Agent",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["Next.js 15", "PydanticAI Agent"]
      }
    ],
    "relationships": [
      {
        "from": "ETL",
        "to": "Entity Resolution",
        "type": "arrow",
        "label": "normalized records"
      },
      {
        "from": "Entity Resolution",
        "to": "Attribution Engine",
        "type": "arrow",
        "label": "resolved entities"
      },
      {
        "from": "All stages",
        "to": "PostgreSQL",
        "type": "arrow",
        "label": "shared storage"
      }
    ],
    "callout_boxes": [
      {
        "heading": "UNIFIED DATABASE",
        "body_text": "One database, three paradigms, zero sync headaches",
        "position": "bottom-center"
      }
    ]
  }
}
```

## Quality Checklist

- [x] Primary message clear in one sentence
- [x] Semantic tags used (no colors, hex codes, or font names in content spec)
- [x] ASCII layout sketched
- [x] Spatial anchors defined in YAML
- [x] Labels under 30 characters
- [x] Anti-hallucination rules listed
- [x] Alt text provided (125 chars max)
- [x] JSON export block included
- [x] Audience level correct (L1/L2/L3/L4)
- [x] Layout template identified (A/B/C/D/E)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25
- [ ] Embedded in documentation

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Five-pipeline architecture with unified PostgreSQL handling relational, vector, and graph data.](docs/figures/repo-figures/assets/fig-pitch-03-architecture.jpg)

*Five-stage attribution pipeline backed by a unified PostgreSQL 17 instance handling relational data, pgvector embeddings, and Apache AGE graph queries.*

### From this figure plan (relative)

![Five-pipeline architecture with unified PostgreSQL handling relational, vector, and graph data.](../assets/fig-pitch-03-architecture.jpg)
