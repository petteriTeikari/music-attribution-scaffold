# fig-ecosystem-10: Knowledge Graph Backend Options

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-ecosystem-10 |
| **Title** | Knowledge Graph Backend Options |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/prd/decisions/REPORT.md, docs/planning/ |
| **Priority** | P2 (Medium) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | D (Split-Panel) |

## Purpose

Compares three knowledge graph backend options -- Apache AGE (co-located with PostgreSQL), Neo4j Aura (managed native graph), and LightRAG (hybrid graph-RAG) -- for the scaffold's provenance and relationship storage. Answers: "Which graph backend fits our existing PostgreSQL infrastructure and attribution use case?"

## Key Message

Three knowledge graph backends trade off co-location vs features -- Apache AGE runs inside PostgreSQL (zero network hop), Neo4j Aura provides native graph (managed), LightRAG adds RAG on either backend.

## Visual Concept

Split-panel layout with AGE on the left and Neo4j Aura on the right, separated by a center divider. Below both panels, a LightRAG overlay strip spans the full width, showing it can work with either backend. Each panel highlights the key characteristics: deployment model, network topology, and trade-offs.

```
+---------------------------------------------------------------+
|  KNOWLEDGE GRAPH BACKEND OPTIONS                               |
|  -- Co-location vs Features                                    |
+-------------------------------+-------------------------------+
|                               |                               |
|  APACHE AGE                   |  NEO4J AURA                   |
|  ─────────                    |  ──────────                    |
|                               |                               |
|  ┌─────────────────────────┐ |  ┌─────────────────────────┐  |
|  │  PostgreSQL Process      │ |  │  Managed Cloud Service   │  |
|  │  ┌───────────────────┐  │ |  │                          │  |
|  │  │  AGE Extension    │  │ |  │  Native graph engine     │  |
|  │  │  Cypher queries   │  │ |  │  Cypher + GDS            │  |
|  │  │  inside SQL       │  │ |  │  Separate service        │  |
|  │  └───────────────────┘  │ |  │                          │  |
|  │  Zero network hop       │ |  │  Network hop required    │  |
|  │  Same ACID guarantees   │ |  │  Managed scaling         │  |
|  └─────────────────────────┘ |  └─────────────────────────┘  |
|                               |                               |
|  P = 0.45 (approximate)      |  P = 0.30 (approximate)       |
|                               |                               |
+-------------------------------+-------------------------------+
|                                                                |
|  LIGHTRAG OVERLAY (works with either backend)                  |
|  ┌────────────────────────────────────────────────────────┐   |
|  │  Hybrid graph-RAG -- retrieval-augmented generation     │   |
|  │  on graph structure. Open-source. P = 0.25 (approx)    │   |
|  └────────────────────────────────────────────────────────┘   |
|                                                                |
+---------------------------------------------------------------+
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
    content: "KNOWLEDGE GRAPH BACKEND OPTIONS"
    role: title

  - id: left_panel
    bounds: [60, 150, 880, 600]
    role: content_area

  - id: right_panel
    bounds: [980, 150, 880, 600]
    role: content_area

  - id: divider
    bounds: [950, 150, 4, 600]
    role: accent_line_v

  - id: lightrag_zone
    bounds: [60, 790, 1800, 180]
    role: content_area

anchors:
  - id: age_panel
    position: [500, 450]
    size: [780, 500]
    role: selected_option
    label: "Apache AGE"

  - id: neo4j_panel
    position: [1420, 450]
    size: [780, 500]
    role: deferred_option
    label: "Neo4j Aura"

  - id: lightrag_strip
    position: [960, 880]
    size: [1700, 140]
    role: deferred_option
    label: "LightRAG Overlay"

  - id: age_to_pg
    from: age_panel
    to: age_panel
    type: internal
    label: "co-located in PostgreSQL"

  - id: neo4j_network
    from: neo4j_panel
    to: neo4j_panel
    type: internal
    label: "separate service, network hop"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "KNOWLEDGE GRAPH BACKEND OPTIONS" with coral accent square |
| AGE panel | `selected_option` | Apache AGE extension, co-located in PostgreSQL, zero network hop, Cypher-in-SQL |
| Neo4j Aura panel | `deferred_option` | Managed native graph, separate service, Cypher + Graph Data Science library |
| LightRAG overlay | `deferred_option` | Hybrid graph-RAG, works with either backend, open-source |
| Prior probabilities | `data_mono` | AGE P=0.45, Neo4j P=0.30, LightRAG P=0.25 |
| Center divider | `accent_line_v` | Coral vertical separator between panels |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| data_model_complexity (parent) | knowledge_graph_backend | arrow | "strong dependency" |
| graph_strategy (parent) | knowledge_graph_backend | arrow | "strong dependency" |
| primary_database (parent) | knowledge_graph_backend | arrow | "strong -- AGE requires PostgreSQL" |
| LightRAG overlay | AGE panel | dashed | "compatible backend" |
| LightRAG overlay | Neo4j panel | dashed | "compatible backend" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "CO-LOCATION ADVANTAGE" | AGE runs inside existing PostgreSQL -- zero network hop, shared ACID transactions | left-margin |
| "PRIORS ARE APPROXIMATE" | Probabilities reflect scaffold team assessment, not market share | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "APACHE AGE"
- Label 2: "NEO4J AURA"
- Label 3: "LIGHTRAG OVERLAY"
- Label 4: "Zero network hop"
- Label 5: "Managed cloud service"
- Label 6: "Hybrid graph-RAG"
- Label 7: "P = 0.45"
- Label 8: "P = 0.30"
- Label 9: "P = 0.25"

### Caption (for embedding in documentation)

Three knowledge graph backend options for the attribution scaffold -- Apache AGE co-located in PostgreSQL (P=0.45), Neo4j Aura managed native graph (P=0.30), and LightRAG hybrid graph-RAG overlay (P=0.25) -- trading off co-location simplicity against feature richness.

## Anti-Hallucination Rules

These are INTERNAL instructions for prompt construction. They MUST NEVER appear as visible text in the generated image.

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `selected_option`, `deferred_option`, `data_mono` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. PRD node: `knowledge_graph_backend`. This is the decision node driving this figure.
10. Parent nodes: `data_model_complexity` (strong), `graph_strategy` (strong), `primary_database` (strong).
11. Apache AGE is the Apache Age extension for PostgreSQL -- it adds Cypher query support inside SQL.
12. Neo4j Aura is the managed cloud version of Neo4j -- do NOT confuse with self-hosted Neo4j Community.
13. LightRAG is an open-source hybrid graph-RAG framework -- not a Neo4j or AGE product.
14. Options with approximate priors: `age_co_located` (P=0.45), `neo4j_aura` (P=0.30), `lightrag_hybrid` (P=0.25).
15. These priors are approximate scaffold team assessments, NOT market share data.
16. AGE requires PostgreSQL -- this is a hard constraint; the scaffold already uses PostgreSQL as primary database.

## Alt Text

Knowledge graph backends: Apache AGE co-located vs Neo4j Aura vs LightRAG hybrid

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "ecosystem-10",
    "title": "Knowledge Graph Backend Options",
    "audience": "L3",
    "layout_template": "D"
  },
  "content_architecture": {
    "primary_message": "Three knowledge graph backends trade off co-location vs features -- Apache AGE runs inside PostgreSQL (zero network hop), Neo4j Aura provides native graph (managed), LightRAG adds RAG on either backend.",
    "layout_flow": "left-to-right",
    "key_structures": [
      {
        "name": "Apache AGE Panel",
        "role": "selected_option",
        "is_highlighted": true,
        "labels": ["APACHE AGE", "Zero network hop", "P = 0.45"]
      },
      {
        "name": "Neo4j Aura Panel",
        "role": "deferred_option",
        "is_highlighted": false,
        "labels": ["NEO4J AURA", "Managed cloud", "P = 0.30"]
      },
      {
        "name": "LightRAG Overlay",
        "role": "deferred_option",
        "is_highlighted": false,
        "labels": ["LIGHTRAG OVERLAY", "Hybrid graph-RAG", "P = 0.25"]
      }
    ],
    "relationships": [
      {
        "from": "data_model_complexity",
        "to": "knowledge_graph_backend",
        "type": "arrow",
        "label": "strong dependency"
      },
      {
        "from": "graph_strategy",
        "to": "knowledge_graph_backend",
        "type": "arrow",
        "label": "strong dependency"
      },
      {
        "from": "primary_database",
        "to": "knowledge_graph_backend",
        "type": "arrow",
        "label": "strong -- AGE requires PostgreSQL"
      },
      {
        "from": "LightRAG",
        "to": "AGE",
        "type": "dashed",
        "label": "compatible backend"
      },
      {
        "from": "LightRAG",
        "to": "Neo4j",
        "type": "dashed",
        "label": "compatible backend"
      }
    ],
    "callout_boxes": [
      {
        "heading": "CO-LOCATION ADVANTAGE",
        "body_text": "AGE runs inside existing PostgreSQL -- zero network hop, shared ACID transactions",
        "position": "left-margin"
      },
      {
        "heading": "PRIORS ARE APPROXIMATE",
        "body_text": "Probabilities reflect scaffold team assessment, not market share",
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
- [x] Anti-hallucination rules listed (8 default + 8 figure-specific)
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
