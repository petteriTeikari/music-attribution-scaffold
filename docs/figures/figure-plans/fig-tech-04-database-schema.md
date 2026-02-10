# fig-tech-04: Database Schema

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-tech-04 |
| **Title** | PostgreSQL Attribution Schema |
| **Audience** | Technical (developers) |
| **Complexity** | L3 (detailed implementation) |
| **Location** | docs/prd/attribution-engine-prd.md, docs/architecture/ |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:10 |

## Purpose

Show the PostgreSQL database schema for storing attribution data with confidence scores, provenance tracking, and vector embeddings for semantic search.

## Key Message

"Four core tables (source_records, unified_entities, entity_links, field_confidence) with pgvector for semantic search enable full provenance tracking and confidence transparency."

## Visual Concept

Entity-relationship diagram showing table structures and foreign key relationships.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  POSTGRESQL ATTRIBUTION SCHEMA                                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────────────┐         ┌─────────────────────────┐           │
│  │    source_records       │         │   unified_entities      │           │
│  ├─────────────────────────┤         ├─────────────────────────┤           │
│  │ PK id                   │         │ PK id                   │           │
│  │    source_name          │    ┌───▶│    entity_type          │           │
│  │    external_id          │    │    │    canonical_name       │           │
│  │    entity_type          │    │    │    merged_data (JSONB)  │           │
│  │    raw_data (JSONB)     │    │    │    embedding (vector)   │◀─pgvector │
│  │    fetched_at           │    │    │    created_at           │           │
│  │    checksum             │    │    │    updated_at           │           │
│  └─────────────────────────┘    │    └─────────────────────────┘           │
│              │                   │               │                          │
│              │                   │               │                          │
│              ▼                   │               ▼                          │
│  ┌─────────────────────────┐    │    ┌─────────────────────────┐           │
│  │     entity_links        │────┘    │   field_confidence      │           │
│  ├─────────────────────────┤         ├─────────────────────────┤           │
│  │ PK id                   │         │ PK id                   │           │
│  │ FK source_record_id     │────────▶│ FK unified_entity_id    │           │
│  │ FK unified_entity_id    │         │    field_name           │           │
│  │    match_confidence     │         │    confidence_score     │           │
│  │    match_method         │         │    attribution_level    │◀─A0-A3    │
│  │    created_at           │         │    sources (JSONB)      │           │
│  └─────────────────────────┘         │    last_updated         │           │
│                                      └─────────────────────────┘           │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│  EXTENSIONS: pgvector (semantic search), pg_trgm (fuzzy matching)           │
│  INDEXES: B-tree on FKs, GIN on JSONB, HNSW on vector embeddings            │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| source_records | `source_discogs` | Raw data from external sources |
| unified_entities | `source_system` | Merged canonical entities |
| entity_links | `processing_stage` | Many-to-many mapping |
| field_confidence | `primary_pathway` | Per-field confidence scores |
| pgvector | `storage_layer` | Vector embedding extension |

### Relationships/Flows

| From | To | Type | Label |
|------|-----|------|-------|
| source_records | entity_links | FK | "source_record_id" |
| unified_entities | entity_links | FK | "unified_entity_id" |
| unified_entities | field_confidence | FK | "unified_entity_id" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "EXTENSIONS" | pgvector, pg_trgm | Bottom left |
| "INDEXES" | B-tree, GIN, HNSW | Bottom right |

## Text Content

### Labels (Max 30 chars each)

- "source_records"
- "unified_entities"
- "entity_links"
- "field_confidence"
- "PK id"
- "FK source_record_id"
- "raw_data (JSONB)"
- "embedding (vector)"
- "confidence_score"
- "attribution_level (A0-A3)"

### Caption (for embedding)

PostgreSQL attribution schema: source_records stores raw external data, unified_entities holds merged canonical data with pgvector embeddings, entity_links maps sources to unified entities, field_confidence tracks per-field confidence scores and A0-A3 attribution levels with full provenance in JSONB.

## Prompts for Nano Banana Pro

### Style Prompt

Database schema diagram on warm off-white background (#F8F6F0).
Clean ER diagram style, professional technical documentation.
Four table boxes with field lists, PK/FK indicators clearly marked.
Relationship lines with crow's foot notation or arrows.
Deep blue for primary tables, gray for supporting tables.
Callout badges for pgvector and extension info.

### Content Prompt

Create a database schema diagram showing:
- TOP LEFT: source_records table
  - Fields: id (PK), source_name, external_id, entity_type, raw_data (JSONB), fetched_at, checksum
- TOP RIGHT: unified_entities table
  - Fields: id (PK), entity_type, canonical_name, merged_data (JSONB), embedding (vector with pgvector badge), timestamps
- BOTTOM LEFT: entity_links table
  - Fields: id (PK), source_record_id (FK), unified_entity_id (FK), match_confidence, match_method, created_at
- BOTTOM RIGHT: field_confidence table
  - Fields: id (PK), unified_entity_id (FK), field_name, confidence_score, attribution_level (A0-A3 badge), sources (JSONB)
- Relationship lines connecting FKs to PKs
- Bottom callout: Extensions (pgvector, pg_trgm) and Indexes (B-tree, GIN, HNSW)

### Refinement Notes

- Tables should look like database schema boxes
- PK fields should be visually distinct (bold or underlined)
- FK relationships should be clear with lines
- JSONB and vector fields should have type indicators
- A0-A3 annotation near attribution_level field

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "tech-04",
    "title": "PostgreSQL Attribution Schema",
    "audience": "technical"
  },
  "content_architecture": {
    "primary_message": "Four core tables with pgvector enable provenance tracking and confidence transparency",
    "layout_flow": "quad-panel",
    "key_structures": [
      {
        "name": "source_records",
        "role": "storage_layer",
        "is_highlighted": false,
        "labels": ["Raw external data", "JSONB storage"]
      },
      {
        "name": "unified_entities",
        "role": "source_system",
        "is_highlighted": true,
        "labels": ["Canonical entities", "Vector embeddings"]
      },
      {
        "name": "entity_links",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["Many-to-many", "Match confidence"]
      },
      {
        "name": "field_confidence",
        "role": "primary_pathway",
        "is_highlighted": true,
        "labels": ["Per-field scores", "A0-A3 levels"]
      }
    ],
    "relationships": [
      {"from": "source_records", "to": "entity_links", "type": "one-to-many", "label": "source_record_id"},
      {"from": "unified_entities", "to": "entity_links", "type": "one-to-many", "label": "unified_entity_id"},
      {"from": "unified_entities", "to": "field_confidence", "type": "one-to-many", "label": "unified_entity_id"}
    ],
    "callout_boxes": [
      {
        "heading": "EXTENSIONS",
        "body_text": "pgvector (semantic search), pg_trgm (fuzzy matching)",
        "position": "bottom-left"
      },
      {
        "heading": "INDEXES",
        "body_text": "B-tree on FKs, GIN on JSONB, HNSW on vectors",
        "position": "bottom-right"
      }
    ]
  }
}
```

## Alt Text

PostgreSQL database schema with four tables: source_records (raw external data), unified_entities (merged data with pgvector embeddings), entity_links (source-to-entity mapping), field_confidence (per-field scores and A0-A3 attribution levels). Foreign key relationships connect tables.

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Embedded in documentation
