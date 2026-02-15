# fig-trends-06: Graph Knowledge Base Options

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-trends-06 |
| **Title** | Graph Knowledge Base Options |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/planning/tech-trends-agentic-infrastructure-2026.md |
| **Priority** | P2 (Medium) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | D (Split-Panel) |

## Purpose

Compares two graph knowledge base approaches for the scaffold -- a managed Neo4j Aura Agent service versus co-located Apache AGE + LightRAG on PostgreSQL. Answers: "Should we add a separate graph database or keep everything in PostgreSQL?"

## Key Message

Two graph knowledge base approaches -- Neo4j Aura Agent (managed, native graph, LLM query interface) vs Apache AGE + LightRAG (PostgreSQL co-located, zero network hop, hybrid graph-RAG).

## Visual Concept

Split-panel with left showing Neo4j Aura Agent and right showing AGE + LightRAG. Each panel shows architecture diagram and key characteristics. Bottom bar lists decision criteria.

```
+-----------------------------------------------------------------------+
|  GRAPH KNOWLEDGE BASE OPTIONS                                          |
|  ■ Separate service vs. co-located extension                           |
+----------------------------------+------------------------------------+
|                                  |                                    |
|  NEO4J AURA AGENT                |  AGE + LIGHTRAG                    |
|  ────────────────                |  ─────────────                     |
|                                  |                                    |
|  ┌──────────────────────┐       |  ┌──────────────────────────────┐  |
|  │  Neo4j Aura (cloud)  │       |  │  PostgreSQL                   │  |
|  │  ┌────────────────┐  │       |  │  ┌──────────┐ ┌───────────┐  │  |
|  │  │ Native graph   │  │       |  │  │ Apache   │ │ LightRAG  │  │  |
|  │  │ Cypher queries │  │       |  │  │ AGE      │ │ hybrid    │  │  |
|  │  │ LLM interface  │  │       |  │  │ (graph)  │ │ (RAG)     │  │  |
|  │  └────────────────┘  │       |  │  └──────────┘ └───────────┘  │  |
|  └──────────────────────┘       |  │  ┌──────────┐ ┌───────────┐  │  |
|          │                       |  │  │ pgvector │ │ reltnl    │  │  |
|          │ network hop           |  │  └──────────┘ └───────────┘  │  |
|          ▼                       |  └──────────────────────────────┘  |
|  ┌──────────────────────┐       |  Zero network hop                   |
|  │ Application server   │       |  Everything in one process          |
|  └──────────────────────┘       |                                    |
|                                  |                                    |
|  ■ Managed service               |  ■ PostgreSQL extension             |
|  ■ Native graph engine           |  ■ Co-located with existing DB     |
|  ■ Built-in LLM integration     |  ■ Hybrid vector + graph           |
|  ■ Separate billing              |  ■ Single billing                  |
|                                  |                                    |
+----------------------------------+------------------------------------+
|  DECISION CRITERIA                                                     |
|  ■ Team graph expertise  ■ Operational budget  ■ Latency reqs         |
|  PRD: knowledge_graph_backend                                          |
|  Priors: age_co_located 0.45 | neo4j_aura 0.30 | lightrag 0.25       |
+-----------------------------------------------------------------------+
```

## Spatial Anchors

```yaml
canvas:
  width: 1920
  height: 1080
  background: primary_background

zones:
  - id: title_zone
    bounds: [0, 0, 1920, 120]
    content: "GRAPH KNOWLEDGE BASE OPTIONS"
    role: title

  - id: left_panel
    bounds: [60, 140, 880, 680]
    content: "NEO4J AURA AGENT"
    role: content_area

  - id: right_panel
    bounds: [980, 140, 880, 680]
    content: "AGE + LIGHTRAG"
    role: content_area

  - id: decision_bar
    bounds: [60, 870, 1800, 140]
    content: "DECISION CRITERIA"
    role: callout_box

anchors:
  - id: neo4j_aura
    position: [120, 220]
    size: [760, 280]
    role: deferred_option

  - id: app_server
    position: [120, 560]
    size: [760, 100]
    role: processing_stage

  - id: flow_neo4j_to_app
    from: neo4j_aura
    to: app_server
    type: arrow
    label: "network hop"

  - id: pg_unified
    position: [1040, 220]
    size: [760, 400]
    role: selected_option

  - id: age_extension
    position: [1080, 300]
    size: [320, 120]
    role: processing_stage

  - id: lightrag_extension
    position: [1440, 300]
    size: [320, 120]
    role: processing_stage

  - id: pgvector_ext
    position: [1080, 440]
    size: [320, 80]
    role: processing_stage

  - id: relational_ext
    position: [1440, 440]
    size: [320, 80]
    role: processing_stage
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Neo4j Aura Agent | `deferred_option` | Managed cloud service with native graph, Cypher queries, LLM integration |
| Application server | `processing_stage` | App server connected to Neo4j via network hop |
| PostgreSQL Unified | `selected_option` | Single PostgreSQL with AGE, LightRAG, pgvector, relational |
| Apache AGE block | `processing_stage` | PostgreSQL extension for graph queries (Cypher-compatible) |
| LightRAG block | `processing_stage` | Hybrid graph-RAG on PostgreSQL |
| pgvector block | `processing_stage` | Vector search co-located |
| Decision criteria bar | `callout_box` | Team expertise, operational budget, latency requirements |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Neo4j Aura Agent | Application server | arrow | "network hop" |
| Apache AGE | LightRAG | bidirectional | "hybrid queries" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "DECISION CRITERIA" | Team graph expertise, operational budget, latency requirements. PRD priors: age_co_located 0.45, neo4j_aura 0.30, lightrag_hybrid 0.25 | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "NEO4J AURA AGENT"
- Label 2: "AGE + LIGHTRAG"
- Label 3: "Native graph engine"
- Label 4: "Cypher queries"
- Label 5: "LLM interface"
- Label 6: "Managed service"
- Label 7: "Apache AGE"
- Label 8: "LightRAG hybrid"
- Label 9: "Zero network hop"
- Label 10: "Everything in one process"
- Label 11: "PostgreSQL extension"
- Label 12: "Co-located with existing DB"

### Caption (for embedding in documentation)

Two graph knowledge base approaches: Neo4j Aura Agent (managed, separate service) vs Apache AGE + LightRAG (PostgreSQL co-located, zero network hop). PRD favors AGE co-located (P=0.45).

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `selected_option`, `deferred_option`, `processing_stage` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption. The editorial display title is allowed.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. PRD node: knowledge_graph_backend. Priors: age_co_located (P=0.45), neo4j_aura (P=0.30), lightrag_hybrid (P=0.25).
10. Neo4j Aura Agent is the managed cloud product with built-in LLM integration -- do NOT conflate with Neo4j Community Edition.
11. LightRAG is a PostgreSQL-native graph-RAG framework -- it is separate from Apache AGE.
12. Apache AGE is a PostgreSQL extension providing Cypher-compatible graph queries -- it is not a standalone database.
13. graph_strategy and primary_database are strong parent nodes influencing this decision.
14. Do NOT claim one approach is universally better -- the choice depends on team expertise, budget, and latency.
15. The "co-located" advantage is zero network hop for combined graph + vector + relational queries.

## Alt Text

Graph knowledge bases: Neo4j Aura Agent vs Apache AGE with LightRAG on PostgreSQL

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "trends-06",
    "title": "Graph Knowledge Base Options",
    "audience": "L3",
    "layout_template": "D"
  },
  "content_architecture": {
    "primary_message": "Two graph KB approaches: Neo4j Aura Agent (managed, separate) vs AGE + LightRAG (PostgreSQL co-located, zero hop).",
    "layout_flow": "left-to-right",
    "key_structures": [
      {
        "name": "Neo4j Aura Agent",
        "role": "deferred_option",
        "is_highlighted": false,
        "labels": ["Managed service", "Native graph", "Cypher queries", "LLM interface"]
      },
      {
        "name": "PostgreSQL Unified (AGE + LightRAG)",
        "role": "selected_option",
        "is_highlighted": true,
        "labels": ["Apache AGE", "LightRAG hybrid", "pgvector", "Zero network hop"]
      }
    ],
    "relationships": [
      {
        "from": "Neo4j Aura Agent",
        "to": "Application Server",
        "type": "arrow",
        "label": "network hop"
      },
      {
        "from": "Apache AGE",
        "to": "LightRAG",
        "type": "bidirectional",
        "label": "hybrid queries"
      }
    ],
    "callout_boxes": [
      {
        "heading": "DECISION CRITERIA",
        "body_text": "Team graph expertise, operational budget, latency reqs. Priors: age_co_located 0.45, neo4j_aura 0.30, lightrag 0.25",
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
- [x] Audience level correct (L3)
- [x] Layout template identified (D)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
