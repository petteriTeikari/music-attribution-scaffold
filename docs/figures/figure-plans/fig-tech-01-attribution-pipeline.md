# fig-tech-01: Attribution Pipeline

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-tech-01 |
| **Title** | Multi-Source Attribution Pipeline |
| **Audience** | Technical (developers) |
| **Complexity** | L3 (detailed implementation) |
| **Location** | docs/prd/attribution-engine-prd.md, docs/architecture/README.md |
| **Priority** | P0 (Critical) |
| **Aspect Ratio** | 16:9 |

## Purpose

Show how attribution data flows from multiple external sources through entity resolution to produce unified, confidence-scored entities in PostgreSQL.

## Key Message

"Three sources feed into entity resolution, producing unified entities with per-field confidence scores and full provenance tracking."

## Visual Concept

Left-to-right pipeline showing data aggregation and quality improvement.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  MULTI-SOURCE ATTRIBUTION PIPELINE                                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   SOURCES                PROCESSING                      OUTPUT             │
│   ───────                ──────────                      ──────             │
│                                                                             │
│   ┌─────────┐                                                               │
│   │ Discogs │─────┐                                                         │
│   │  API    │     │      ┌──────────────┐      ┌───────────────────┐       │
│   └─────────┘     │      │              │      │                   │       │
│                   ├─────▶│   Entity     │─────▶│  Unified Entity   │       │
│   ┌─────────┐     │      │  Resolution  │      │  + Confidence     │       │
│   │MusicBrz │─────┤      │              │      │  + Provenance     │       │
│   │  API    │     │      │  - Fuzzy     │      │                   │       │
│   └─────────┘     │      │    Match     │      └─────────┬─────────┘       │
│                   │      │  - Vote      │                │                 │
│   ┌─────────┐     │      │  - Weight    │                ▼                 │
│   │System  │─────┘      │              │      ┌───────────────────┐       │
│   │  Own    │            └──────────────┘      │    PostgreSQL     │       │
│   └─────────┘                                  │    + pgvector     │       │
│                                                └───────────────────┘       │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ KEY: Confidence = (agreement_ratio × 0.6) + (authority_weight × 0.4) │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Discogs Adapter | `source_discogs` | Dark gray, vinyl/catalog data |
| MusicBrainz Adapter | `source_musicbrainz` | Purple, open database |
| System Own | `source_system` | Deep blue, primary/authoritative |
| Entity Resolution | `processing_stage` | Central processing box |
| Unified Entity | `primary_pathway` | Output with confidence |
| PostgreSQL | `storage_layer` | Final persistence |

### Relationships/Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Discogs | Entity Resolution | Arrow | "raw records" |
| MusicBrainz | Entity Resolution | Arrow | "raw records" |
| System Own | Entity Resolution | Arrow | "raw records" |
| Entity Resolution | Unified Entity | Arrow | "resolved" |
| Unified Entity | PostgreSQL | Arrow | "persist" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "CONFIDENCE FORMULA" | agreement_ratio × 0.6 + authority_weight × 0.4 | Bottom center |

## Text Content

### Labels (Max 30 chars each)

- "Discogs API"
- "MusicBrainz API"
- "System Own"
- "Entity Resolution"
- "Fuzzy Match"
- "Voting + Weights"
- "Unified Entity"
- "Per-field Confidence"
- "Full Provenance"
- "PostgreSQL + pgvector"

### Caption (for embedding)

Multi-source attribution pipeline: data from Discogs, MusicBrainz, and System Own flows through entity resolution (fuzzy matching + weighted voting) to produce unified entities with per-field confidence scores stored in PostgreSQL with pgvector for semantic search.

## Prompts for Nano Banana Pro

### Style Prompt

Elegant technical architecture diagram on warm off-white background (#F8F6F0).
Medical illustration quality, Economist-style data visualization.
Clean sans-serif typography, organic flowing arrows between components.
Matte professional finish, subtle shadows on containers.
Three source boxes on left (dark gray, purple, deep blue), central processing stage,
output to database on right. Clear left-to-right flow.

### Content Prompt

Create a data pipeline diagram showing:
- LEFT: Three source adapters stacked vertically
  - Discogs (dark gray box)
  - MusicBrainz (purple box)
  - System Own (deep blue box, slightly larger/emphasized)
- CENTER: Entity Resolution processing stage
  - Shows "Fuzzy Match" and "Voting + Weights" inside
- RIGHT: Output section
  - "Unified Entity" box with "Confidence" and "Provenance" labels
  - Arrow down to "PostgreSQL + pgvector" database cylinder
- BOTTOM: Key insight callout with confidence formula

### Refinement Notes

- System Own should be visually primary (deeper blue, slightly larger)
- Arrows should be organic/flowing, not rigid
- Processing stage should show internal steps
- Database should use cylinder icon convention

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "tech-01",
    "title": "Multi-Source Attribution Pipeline",
    "audience": "technical"
  },
  "content_architecture": {
    "primary_message": "Three sources feed into entity resolution, producing unified entities with confidence scores",
    "layout_flow": "left-to-right",
    "key_structures": [
      {
        "name": "Discogs Adapter",
        "role": "source_discogs",
        "is_highlighted": false,
        "labels": ["Discogs API", "Vinyl/catalog data"]
      },
      {
        "name": "MusicBrainz Adapter",
        "role": "source_musicbrainz",
        "is_highlighted": false,
        "labels": ["MusicBrainz API", "Open database"]
      },
      {
        "name": "System Own",
        "role": "source_system",
        "is_highlighted": true,
        "labels": ["System Own", "Primary source"]
      },
      {
        "name": "Entity Resolution",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["Fuzzy Match", "Voting + Weights"]
      },
      {
        "name": "Unified Entity",
        "role": "primary_pathway",
        "is_highlighted": true,
        "labels": ["Per-field Confidence", "Full Provenance"]
      },
      {
        "name": "PostgreSQL",
        "role": "storage_layer",
        "is_highlighted": false,
        "labels": ["PostgreSQL", "pgvector"]
      }
    ],
    "relationships": [
      {"from": "Discogs", "to": "Entity Resolution", "type": "arrow", "label": "raw records"},
      {"from": "MusicBrainz", "to": "Entity Resolution", "type": "arrow", "label": "raw records"},
      {"from": "System Own", "to": "Entity Resolution", "type": "arrow", "label": "raw records"},
      {"from": "Entity Resolution", "to": "Unified Entity", "type": "arrow", "label": "resolved"},
      {"from": "Unified Entity", "to": "PostgreSQL", "type": "arrow", "label": "persist"}
    ],
    "callout_boxes": [
      {
        "heading": "CONFIDENCE FORMULA",
        "body_text": "confidence = (agreement_ratio × 0.6) + (authority_weight × 0.4)",
        "position": "bottom-center"
      }
    ]
  }
}
```

## Alt Text

Data pipeline diagram: Discogs, MusicBrainz, and the system sources feed into entity resolution stage performing fuzzy matching and weighted voting, outputting unified entities with per-field confidence scores to PostgreSQL database with pgvector.

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Embedded in documentation
