# fig-backend-17: Database ERD

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-backend-17 |
| **Title** | Database Entity-Relationship Diagram: 8 Tables with pgvector |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 |
| **Location** | docs/architecture/, docs/database/ |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure shows the complete database schema as an entity-relationship diagram -- all 8 tables, their primary keys, foreign key relationships, and the pgvector HALFVEC column. Engineers need this to understand data persistence, query patterns, and how boundary objects map to SQL tables.

The key message is: "Eight PostgreSQL tables mirror the five boundary objects (BO-1 through BO-5) plus three infrastructure tables (edges for graph, entity_embeddings for vectors, audit_log for permissions) -- with JSONB for flexible nested data and HALFVEC(768) for semantic search."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  DATABASE ERD                                                  |
|  ■ PostgreSQL — 8 Tables with pgvector                         |
+---------------------------------------------------------------+
|                                                                 |
|  ┌──────────────────┐       ┌──────────────────┐              |
|  │ normalized_records│       │ resolved_entities │              |
|  │ (BO-1)            │       │ (BO-2)            │              |
|  │──────────────────│       │──────────────────│              |
|  │ record_id PK      │       │ entity_id PK      │              |
|  │ source             │       │ entity_type        │              |
|  │ source_id          │       │ canonical_name     │              |
|  │ entity_type        │       │ source_records JSONB│             |
|  │ canonical_name     │       │ resolution_method  │              |
|  │ identifiers JSONB  │       │ resolution_conf    │              |
|  │ metadata JSONB     │       │ assurance_level    │              |
|  │ source_confidence  │       │ needs_review       │              |
|  │ UQ(source,src_id)  │       │ resolved_at        │              |
|  └──────────────────┘       └────────┬─────────┘              |
|                                      │ FK                      |
|                         ┌────────────┼─────────────┐          |
|                         │            │             │          |
|                         ▼            ▼             ▼          |
|  ┌──────────────────┐  ┌──────────┐  ┌───────────────────┐   |
|  │ edges             │  │entity_   │  │ permission_bundles │   |
|  │──────────────────│  │embeddings│  │ (BO-5)             │   |
|  │ edge_id PK        │  │──────────│  │───────────────────│   |
|  │ from_entity_id FK │  │embed_id PK│  │ permission_id PK  │   |
|  │ to_entity_id FK   │  │entity_id FK│  │ entity_id FK     │   |
|  │ relationship_type │  │model_name │  │ scope             │   |
|  │ confidence        │  │embedding  │  │ permissions JSONB │   |
|  │ metadata JSONB    │  │HALFVEC   │  │ delegation_chain  │   |
|  │ UQ(from,to,type)  │  │(768)     │  │ effective_from    │   |
|  └──────────────────┘  │UQ(ent,mod)│  │ default_permission│   |
|                         └──────────┘  └─────────┬─────────┘   |
|                                                  │ FK           |
|  ┌──────────────────┐                           ▼              |
|  │ attribution_records│  ┌──────────────────────────┐          |
|  │ (BO-3)            │  │ audit_log                  │          |
|  │──────────────────│  │──────────────────────────│          |
|  │ attribution_id PK │  │ audit_id PK               │          |
|  │ work_entity_id    │  │ permission_id FK           │          |
|  │ work_title        │  │ requester_id               │          |
|  │ artist_name       │  │ permission_type            │          |
|  │ credits JSONB     │  │ result                     │          |
|  │ confidence_score  │  │ request_context JSONB      │          |
|  │ conformal_set JSONB│  │ checked_at                │          |
|  │ provenance JSONB  │  └──────────────────────────┘          |
|  │ uncertainty JSONB │                                         |
|  │ needs_review      │  ┌──────────────────────────┐          |
|  │ review_priority   │  │ feedback_cards (BO-4)      │          |
|  │ version           │  │──────────────────────────│          |
|  └──────────────────┘  │ feedback_id PK             │          |
|           ▲             │ attribution_id FK          │          |
|           └─────────────│ reviewer_id                │          |
|              FK         │ corrections JSONB          │          |
|                         │ overall_assessment         │          |
|                         └──────────────────────────┘          |
|                                                                 |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "DATABASE ERD" |
| normalized_records table | `etl_extract` | BO-1 table with UQ constraint on (source, source_id) |
| resolved_entities table | `entity_resolve` | BO-2 table, central node with 3 FK dependents |
| attribution_records table | `final_score` | BO-3 table with JSONB for credits, provenance, conformal |
| feedback_cards table | `feedback_loop` | BO-4 table with FK to attribution_records |
| permission_bundles table | `security_layer` | BO-5 table with FK to resolved_entities |
| edges table | `storage_layer` | Graph relationships between entities |
| entity_embeddings table | `storage_layer` | pgvector HALFVEC(768) embeddings |
| audit_log table | `security_layer` | Permission check audit trail |
| Foreign key arrows | `data_flow` | Arrows showing FK relationships |
| JSONB columns | `data_mono` | Highlighted JSONB columns for flexible nested data |
| Unique constraints | `data_mono` | UQ annotations on constrained column groups |
| PK/FK labels | `data_mono` | Primary key and foreign key annotations |

## Anti-Hallucination Rules

1. There are exactly 8 tables as defined in `src/music_attribution/db/models.py`: normalized_records, resolved_entities, attribution_records, permission_bundles, feedback_cards, edges, entity_embeddings, audit_log.
2. entity_embeddings uses HALFVEC(768), not VECTOR(768) or a different dimension.
3. Foreign key relationships: edges.from_entity_id/to_entity_id -> resolved_entities, entity_embeddings.entity_id -> resolved_entities, permission_bundles.entity_id -> resolved_entities, feedback_cards.attribution_id -> attribution_records, audit_log.permission_id -> permission_bundles.
4. Unique constraints: normalized_records(source, source_id), edges(from_entity_id, to_entity_id, relationship_type), entity_embeddings(entity_id, model_name).
5. JSONB columns: identifiers, metadata, relationships (in normalized_records), source_records, resolution_details, conflicts (in resolved_entities), credits, conformal_set, provenance_chain, uncertainty_summary (in attribution_records).
6. attribution_records has work_title and artist_name columns (added in migration 004).
7. All timestamp columns use DateTime(timezone=True).
8. The ORM base is SQLAlchemy DeclarativeBase with Mapped[T] annotations.

## Alt Text

Entity-relationship diagram of 8 PostgreSQL tables: normalized_records, resolved_entities (central), attribution_records, feedback_cards, permission_bundles, edges, entity_embeddings with HALFVEC, and audit_log.
