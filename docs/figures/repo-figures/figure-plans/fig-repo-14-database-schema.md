# fig-repo-14: Database Schema

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-repo-14 |
| **Title** | Database Schema: PostgreSQL + pgvector Entity-Relationship Diagram |
| **Audience** | Technical (backend developers, data engineers) |
| **Complexity** | L3 (detailed implementation) |
| **Location** | docs/architecture/database.md |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

The database uses PostgreSQL 17 with the pgvector extension for semantic similarity search. This figure shows the core tables, their relationships, and the key columns -- especially the confidence scores, provenance tracking, and vector embedding columns. It helps backend developers understand the data model and how attribution records relate to works, artists, and sources.

The key message is: "Every attribution record carries per-field confidence scores, full source provenance, and optional vector embeddings for semantic search -- stored in PostgreSQL with pgvector."

## Visual Concept (ASCII Layout)

```
+-----------------------------------------------------------------------+
|  DATABASE SCHEMA                                                       |
|  ■ PostgreSQL 17 + pgvector ERD                                        |
+-----------------------------------------------------------------------+
|                                                                        |
|  ┌──────────────────────┐        ┌──────────────────────┐             |
|  │  WORKS               │        │  ARTISTS             │             |
|  │  ──────              │        │  ───────             │             |
|  │  id         UUID PK  │        │  id         UUID PK  │             |
|  │  title      TEXT     │        │  name       TEXT     │             |
|  │  isrc       TEXT     │◄──┐    │  isni       TEXT     │             |
|  │  iswc       TEXT     │   │    │  artist_id  TEXT     │◄──┐        |
|  │  confidence FLOAT    │   │    │  assurance  ENUM     │   │        |
|  │  embedding  VECTOR   │   │    │  confidence FLOAT    │   │        |
|  │  created_at TIMESTZ  │   │    │  embedding  VECTOR   │   │        |
|  └──────────────────────┘   │    └──────────────────────┘   │        |
|                              │                               │        |
|  ┌──────────────────────────┴───────────────────────────────┴──┐     |
|  │  ATTRIBUTION_RECORDS                                         │     |
|  │  ──────────────────────                                      │     |
|  │  id              UUID PK                                     │     |
|  │  work_id         UUID FK ──▶ works.id                        │     |
|  │  artist_id       UUID FK ──▶ artists.id                      │     |
|  │  role            ENUM (composer, performer, producer, ...)   │     |
|  │  confidence      FLOAT [0.0 - 1.0]                          │     |
|  │  assurance_level ENUM (A0, A1, A2, A3)                       │     |
|  │  sources         JSONB (provenance array)                    │     |
|  │  created_at      TIMESTAMPTZ                                 │     |
|  │  updated_at      TIMESTAMPTZ                                 │     |
|  └──────────────────────────────────────────────────────────────┘     |
|                                                                        |
|  ┌──────────────────────────────────────────────────────────────┐     |
|  │  PERMISSIONS                                                  │     |
|  │  ───────────                                                  │     |
|  │  id         UUID PK   │  work_id    UUID FK                  │     |
|  │  scope      ENUM      │  granted_by TEXT                     │     |
|  │  granted_at TIMESTZ   │  expires_at TIMESTZ                  │     |
|  └──────────────────────────────────────────────────────────────┘     |
|                                                                        |
|  ■ pgvector: VECTOR columns enable semantic similarity (cosine)        |
|  ■ JSONB sources: [{source: "discogs", retrieved: "...", data: ...}]  |
|  ■ Alembic manages all migrations                                      |
+-----------------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title | `heading_display` | "DATABASE SCHEMA" Instrument Serif ALL-CAPS |
| Works table | `entity_box` | Core work entity with ISRC, ISWC |
| Artists table | `entity_box` | Artist entity with ISNI |
| Attribution Records table | `entity_box` | Junction table with confidence + provenance |
| Permissions table | `entity_box` | MCP consent records |
| Foreign key arrows | `relationship_arrow` | work_id FK, artist_id FK |
| Column names | `data_mono` | IBM Plex Mono |
| Data types | `data_mono` | UUID, TEXT, FLOAT, ENUM, JSONB, VECTOR, TIMESTAMPTZ |
| Confidence range annotation | `callout_tip` | [0.0 - 1.0] range |
| Assurance level enum | `enum_values` | A0, A1, A2, A3 |
| pgvector note | `footer_note` | Accent square + explanation of VECTOR columns |
| JSONB structure note | `footer_note` | Example provenance array structure |

## Anti-Hallucination Rules

1. The database is PostgreSQL 17 with pgvector extension -- not MySQL, MongoDB, or SQLite.
2. The pgvector extension must be explicitly created: `CREATE EXTENSION vector`.
3. Confidence scores are FLOAT values between 0.0 and 1.0 -- not integers or percentages.
4. Assurance levels are an enum with values A0, A1, A2, A3 (four levels).
5. Source provenance is stored as JSONB array, not as separate normalized tables.
6. All timestamps use TIMESTAMPTZ (timezone-aware), not TIMESTAMP.
7. Primary keys are UUIDs, not auto-incrementing integers.
8. Migrations are managed by Alembic (in `alembic/` directory), not Django migrations or raw SQL.
9. The ORM is SQLAlchemy 2.0 (models in `src/music_attribution/db/models.py`).
10. Music identifiers include ISRC (recordings), ISWC (compositions), ISNI (people) -- use correct abbreviations.
11. This is a SCAFFOLD -- the exact schema may vary by implementation. Show the core concept.

## Alt Text

Architecture diagram: PostgreSQL 17 entity-relationship schema for the music attribution scaffold showing Works table with ISRC and ISWC identifiers, Artists table with ISNI, Attribution Records junction table carrying per-field transparent confidence scores from 0.0 to 1.0, A0-A3 assurance levels, and JSONB source provenance arrays, plus a Permissions table for MCP machine-readable consent -- with pgvector VECTOR columns enabling semantic similarity search across music metadata.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Architecture diagram: PostgreSQL 17 entity-relationship schema for the music attribution scaffold showing Works table with ISRC and ISWC identifiers, Artists table with ISNI, Attribution Records junction table carrying per-field transparent confidence scores from 0.0 to 1.0, A0-A3 assurance levels, and JSONB source provenance arrays, plus a Permissions table for MCP machine-readable consent -- with pgvector VECTOR columns enabling semantic similarity search across music metadata.](docs/figures/repo-figures/assets/fig-repo-14-database-schema.jpg)

*Figure 14. The database schema embeds attribution-by-design principles: every attribution record carries per-field confidence scores (FLOAT 0.0-1.0), A0-A3 assurance levels, and full JSONB source provenance, while pgvector VECTOR columns enable semantic similarity search across works and artists, all managed by Alembic migrations over SQLAlchemy 2.0 models.*

### From this figure plan (relative)

![Architecture diagram: PostgreSQL 17 entity-relationship schema for the music attribution scaffold showing Works table with ISRC and ISWC identifiers, Artists table with ISNI, Attribution Records junction table carrying per-field transparent confidence scores from 0.0 to 1.0, A0-A3 assurance levels, and JSONB source provenance arrays, plus a Permissions table for MCP machine-readable consent -- with pgvector VECTOR columns enabling semantic similarity search across music metadata.](../assets/fig-repo-14-database-schema.jpg)
