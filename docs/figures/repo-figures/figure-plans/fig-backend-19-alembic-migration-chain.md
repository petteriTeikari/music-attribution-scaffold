# fig-backend-19: Alembic Migration Chain

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-backend-19 |
| **Title** | Alembic Migration Chain: Schema Evolution Timeline |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 |
| **Location** | docs/architecture/, docs/database/ |
| **Priority** | P2 (Medium) |
| **Dimensions** | 1200 x 675px (16:9) |

## Purpose & Key Message

This figure shows the linear chain of Alembic database migrations, documenting what each migration adds or changes and when it was created. Engineers need this to understand schema evolution and what to expect when running `alembic upgrade head`.

The key message is: "Four migrations build the full schema incrementally: initial boundary object tables, then permissions/feedback/graph/vectors, then uncertainty metadata, then display fields -- each migration is reversible and the chain forms a linear sequence."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  ALEMBIC MIGRATION CHAIN                                       |
|  ■ Schema Evolution — 4 Migrations                             |
+---------------------------------------------------------------+
|                                                                 |
|  None                                                          |
|   │                                                             |
|   ▼                                                             |
|  ┌──────────────────────────────────────────────────────┐      |
|  │ 001 — Initial Schema (2026-02-10)                     │      |
|  │ ───────────────────────────────                       │      |
|  │ + normalized_records (BO-1)                           │      |
|  │ + resolved_entities (BO-2)                            │      |
|  │ + attribution_records (BO-3)                          │      |
|  │ 3 tables, all JSONB columns                           │      |
|  └──────────────────────────────────────┬───────────────┘      |
|                                          │                      |
|                                          ▼                      |
|  ┌──────────────────────────────────────────────────────┐      |
|  │ 002 — Permissions, Feedback, Graph, Vectors (2026-02-11)│    |
|  │ ──────────────────────────────────────────────        │      |
|  │ + permission_bundles (BO-5)                           │      |
|  │ + feedback_cards (BO-4)                               │      |
|  │ + edges (graph relationships)                         │      |
|  │ + entity_embeddings (pgvector HALFVEC 768)            │      |
|  │ + audit_log (permission audit trail)                  │      |
|  │ + UQ constraint on normalized_records(source, src_id) │      |
|  │ 5 new tables + 1 constraint                           │      |
|  └──────────────────────────────────────┬───────────────┘      |
|                                          │                      |
|                                          ▼                      |
|  ┌──────────────────────────────────────────────────────┐      |
|  │ 003 — Add uncertainty_summary (2026-02-11)            │      |
|  │ ─────────────────────────────────                     │      |
|  │ + attribution_records.uncertainty_summary (JSONB)     │      |
|  │ 1 new column                                          │      |
|  └──────────────────────────────────────┬───────────────┘      |
|                                          │                      |
|                                          ▼                      |
|  ┌──────────────────────────────────────────────────────┐      |
|  │ 004 — Add display fields (2026-02-12)                 │      |
|  │ ────────────────────────────                          │      |
|  │ + attribution_records.work_title (varchar 500)        │      |
|  │ + attribution_records.artist_name (varchar 500)       │      |
|  │ 2 new columns, server_default=""                      │      |
|  └──────────────────────────────────────────────────────┘      |
|                                                                 |
|  Current HEAD: 004                                             |
|                                                                 |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "ALEMBIC MIGRATION CHAIN" |
| Migration 001 | `storage_layer` | Initial 3 tables: normalized_records, resolved_entities, attribution_records |
| Migration 002 | `storage_layer` | 5 tables + 1 constraint: permissions, feedback, edges, embeddings, audit |
| Migration 003 | `storage_layer` | 1 JSONB column: uncertainty_summary on attribution_records |
| Migration 004 | `storage_layer` | 2 varchar columns: work_title, artist_name on attribution_records |
| Date labels | `data_mono` | Creation dates in monospace |
| Chain arrows | `data_flow` | Linear chain from None to 004 |
| Table counts | `data_mono` | "3 tables", "5 new tables", "1 column", "2 columns" |
| HEAD indicator | `primary_outcome` | "Current HEAD: 004" |

## Anti-Hallucination Rules

1. There are exactly 4 migrations: 001, 002, 003, 004. Do NOT invent additional migrations.
2. Migration 001 creates: normalized_records, resolved_entities, attribution_records.
3. Migration 002 creates: permission_bundles, feedback_cards, edges, entity_embeddings, audit_log. Also adds UQ constraint on normalized_records.
4. Migration 003 adds: uncertainty_summary (JSONB, nullable) to attribution_records.
5. Migration 004 adds: work_title (varchar 500, server_default="") and artist_name (varchar 500, server_default="") to attribution_records.
6. The chain is linear: None -> 001 -> 002 -> 003 -> 004.
7. Dates: 001 = 2026-02-10, 002 = 2026-02-11, 003 = 2026-02-11, 004 = 2026-02-12.
8. entity_embeddings uses HALFVEC(768) from pgvector -- this is specified in migration 002.

## Alt Text

Linear chain of four Alembic database migrations from initial schema (3 tables) through permissions and vectors (5 tables) to uncertainty and display field additions, with dates and table counts.
