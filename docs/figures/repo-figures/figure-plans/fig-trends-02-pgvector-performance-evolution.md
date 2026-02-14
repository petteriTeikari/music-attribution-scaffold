# fig-trends-02: pgvector Performance Evolution

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-trends-02 |
| **Title** | pgvector Performance Evolution |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/planning/tech-trends-agentic-infrastructure-2026.md |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | D (Split-Panel) |

## Purpose

Shows how pgvector's performance trajectory validates the "PostgreSQL Unified" architecture decision -- keeping vector search, graph queries, and relational data in a single database process rather than adding a dedicated vector DB. Answers: "Is pgvector fast enough for production music attribution?"

## Key Message

pgvector reached 471 QPS at 99% recall (Shakudo 2026) -- crossing the production threshold that validates the "PostgreSQL Unified" architecture over dedicated vector databases for music attribution workloads.

## Visual Concept

Split-panel layout. Left panel shows the performance trajectory chart (mid-2025 to 2026). Right panel shows architecture comparison: PostgreSQL Unified vs dedicated vector DB. Bottom bar shows cost and operational complexity trade-off.

```
+-----------------------------------------------------------------------+
|  PGVECTOR PERFORMANCE EVOLUTION                                        |
|  ■ Validating PostgreSQL Unified                                       |
+----------------------------------+------------------------------------+
|                                  |                                    |
|  PERFORMANCE TRAJECTORY          |  ARCHITECTURE COMPARISON           |
|  ──────────────────────          |  ───────────────────────           |
|                                  |                                    |
|         471 QPS ──── ■           |  PostgreSQL Unified                |
|        /                         |  ┌──────────────────────────┐     |
|       /                          |  │  PostgreSQL               │     |
|      /                           |  │  ┌────────┐ ┌─────────┐  │     |
|     / ~200 QPS                   |  │  │pgvector│ │  AGE    │  │     |
|    /                             |  │  └────────┘ └─────────┘  │     |
|   ■                              |  │  ┌────────┐ ┌─────────┐  │     |
|   mid-2025          2026         |  │  │reltnl  │ │full-text│  │     |
|                                  |  │  └────────┘ └─────────┘  │     |
|   @ 99% recall                   |  └──────────────────────────┘     |
|   HNSW indexing                  |  One process, zero network hop    |
|   ~30% memory reduction          |                                    |
|                                  |  Dedicated Vector DB               |
|                                  |  ┌────────────┐ ┌──────────────┐  |
|                                  |  │ Pinecone / │ │ PostgreSQL   │  |
|                                  |  │ Weaviate   │ │ (relational) │  |
|                                  |  └────────────┘ └──────────────┘  |
|                                  |  Two services, network hop        |
|                                  |                                    |
+----------------------------------+------------------------------------+
|  COST & OPS  ■ Unified: 1 DB to manage, hybrid queries in SQL         |
|              ■ Dedicated: 2 services, sync overhead, vendor lock-in    |
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
    content: "PGVECTOR PERFORMANCE EVOLUTION"
    role: title

  - id: left_panel
    bounds: [60, 140, 880, 720]
    content: "PERFORMANCE TRAJECTORY"
    role: content_area

  - id: right_panel
    bounds: [980, 140, 880, 720]
    content: "ARCHITECTURE COMPARISON"
    role: content_area

  - id: bottom_bar
    bounds: [60, 900, 1800, 100]
    content: "COST & OPS"
    role: callout_box

anchors:
  - id: perf_chart
    position: [120, 240]
    size: [760, 400]
    role: data_flow

  - id: perf_annotation
    position: [120, 660]
    size: [760, 140]
    role: data_flow

  - id: unified_arch
    position: [1040, 200]
    size: [760, 320]
    role: selected_option

  - id: dedicated_arch
    position: [1040, 560]
    size: [760, 240]
    role: deferred_option

  - id: qps_marker
    position: [700, 240]
    size: [120, 40]
    role: confidence_high
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Performance chart | `data_flow` | QPS trajectory from ~200 (mid-2025) to 471 (2026) at 99% recall |
| QPS marker | `confidence_high` | "471 QPS" highlighted as production threshold crossing |
| Unified architecture | `selected_option` | Single PostgreSQL with pgvector + AGE + relational + full-text |
| Dedicated architecture | `deferred_option` | Separate vector DB (Pinecone/Weaviate) alongside PostgreSQL |
| Memory annotation | `data_flow` | HNSW ~30% memory reduction vs IVFFlat |
| Cost comparison bar | `callout_box` | Operational complexity comparison |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Performance chart | QPS marker | arrow | "production threshold" |
| Unified architecture | Cost bar | arrow | "1 DB to manage" |
| Dedicated architecture | Cost bar | arrow | "2 services, sync overhead" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "COST & OPS" | Unified: 1 DB, hybrid queries in SQL. Dedicated: 2 services, sync overhead, vendor lock-in | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "PERFORMANCE TRAJECTORY"
- Label 2: "ARCHITECTURE COMPARISON"
- Label 3: "471 QPS @ 99% recall"
- Label 4: "PostgreSQL Unified"
- Label 5: "pgvector"
- Label 6: "AGE"
- Label 7: "relational"
- Label 8: "full-text"
- Label 9: "One process, zero network hop"
- Label 10: "Dedicated Vector DB"
- Label 11: "Two services, network hop"
- Label 12: "HNSW indexing"

### Caption (for embedding in documentation)

pgvector reached 471 QPS at 99% recall, validating the PostgreSQL Unified architecture where vector search, graph queries, and relational data share a single database process.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `selected_option`, `deferred_option`, `data_flow` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption. The editorial display title is allowed.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. 471 QPS at 99% recall is from Shakudo 2026 benchmarks -- cite as "Shakudo 2026", not as internal testing.
10. HNSW indexing improvements yield ~30% memory reduction vs IVFFlat -- this is approximate, not exact.
11. pgvector enables hybrid search (vector + full-text + structured filters) in a single SQL query.
12. PRD nodes: vector_strategy, primary_database -- the scaffold uses pgvector (selected option).
13. Do NOT claim pgvector beats all dedicated vector DBs in all scenarios -- it validates the "good enough for this workload" threshold.
14. Do NOT invent specific QPS numbers for intermediate dates -- only mid-2025 (~200) and 2026 (471) are sourced.
15. Apache AGE is a PostgreSQL extension for graph queries -- do NOT confuse with Neo4j.

## Alt Text

pgvector evolution: 471 QPS at 99% recall validates PostgreSQL Unified architecture

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "trends-02",
    "title": "pgvector Performance Evolution",
    "audience": "L3",
    "layout_template": "D"
  },
  "content_architecture": {
    "primary_message": "pgvector reached 471 QPS at 99% recall, crossing the production threshold that validates PostgreSQL Unified over dedicated vector databases.",
    "layout_flow": "left-to-right",
    "key_structures": [
      {
        "name": "Performance Chart",
        "role": "data_flow",
        "is_highlighted": true,
        "labels": ["471 QPS @ 99% recall", "HNSW indexing", "~30% memory reduction"]
      },
      {
        "name": "PostgreSQL Unified",
        "role": "selected_option",
        "is_highlighted": true,
        "labels": ["pgvector", "AGE", "relational", "full-text"]
      },
      {
        "name": "Dedicated Vector DB",
        "role": "deferred_option",
        "is_highlighted": false,
        "labels": ["Pinecone / Weaviate", "PostgreSQL (relational)"]
      }
    ],
    "relationships": [
      {
        "from": "Performance Chart",
        "to": "QPS Marker",
        "type": "arrow",
        "label": "production threshold"
      },
      {
        "from": "PostgreSQL Unified",
        "to": "Cost Bar",
        "type": "arrow",
        "label": "1 DB to manage"
      }
    ],
    "callout_boxes": [
      {
        "heading": "COST & OPS",
        "body_text": "Unified: 1 DB, hybrid queries. Dedicated: 2 services, sync overhead, vendor lock-in.",
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
