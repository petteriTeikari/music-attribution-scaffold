# fig-choice-03: Why PostgreSQL + pgvector?

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-choice-03 |
| **Title** | Why PostgreSQL + pgvector? |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 (implementation detail) |
| **Location** | docs/prd/decisions/REPORT.md |
| **Priority** | P0 (Critical) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

Explains the primary database decision (PostgreSQL Unified) and vector strategy decision (pgvector). The key insight: a single PostgreSQL instance handles relational data, graph queries (via Apache AGE), and vector search (via pgvector) -- eliminating the need for separate databases. Shows comparison against Pinecone (managed, separate), Chroma (embedded, SQLite-backed), and Supabase (managed PostgreSQL).

The key message is: "One database does three jobs: relational, graph, and vector -- PostgreSQL + pgvector + Apache AGE eliminates multi-database complexity."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  WHY POSTGRESQL + PGVECTOR?                                    |
|  ■ One Database, Three Capabilities                            |
+---------------------------------------------------------------+
|                                                                |
|  ┌─────────────────────────────────────────────────────────┐   |
|  │              POSTGRESQL UNIFIED                          │   |
|  │  ┌──────────┐  ┌──────────┐  ┌──────────────┐          │   |
|  │  │Relational│  │ Graph    │  │ Vector       │          │   |
|  │  │  SQL     │  │ AGE ext  │  │ pgvector ext │          │   |
|  │  │  Tables  │  │ Cypher   │  │ HNSW index   │          │   |
|  │  └──────────┘  └──────────┘  └──────────────┘          │   |
|  │  Single process. Single backup. Single connection pool.  │   |
|  └─────────────────────────────────────────────────────────┘   |
|                                                                |
|  vs ALTERNATIVES                                               |
|  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐          |
|  │ Pinecone     │ │ Chroma       │ │ Supabase     │          |
|  │──────────────│ │──────────────│ │──────────────│          |
|  │ Managed SaaS │ │ Embedded     │ │ Managed PG   │          |
|  │ Vector-only  │ │ SQLite-backed│ │ + pgvector   │          |
|  │ Separate DB  │ │ Dev/test only│ │ + no AGE     │          |
|  │ $70+/month   │ │ Free         │ │ Free-$25/mo  │          |
|  │──────────────│ │──────────────│ │──────────────│          |
|  │ Con: Another │ │ Con: Not     │ │ Con: No graph│          |
|  │ system to    │ │ production   │ │ extension    │          |
|  │ manage       │ │ scale        │ │ support      │          |
|  └──────────────┘ └──────────────┘ └──────────────┘          |
|                                                                |
+---------------------------------------------------------------+
|  Archetype split: Engineers PG (0.60) | Musicians Supabase     |
|  (0.55) | Solo SQLite/Supabase (0.40/0.40)                    |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "WHY POSTGRESQL + PGVECTOR?" with coral accent square |
| Unified PostgreSQL banner | `selected_option` | Three capability boxes: Relational, Graph (AGE), Vector (pgvector) |
| Single-process callout | `feature_list` | "Single process, single backup, single connection pool" |
| Pinecone alternative | `deferred_option` | Managed SaaS, vector-only, separate DB |
| Chroma alternative | `deferred_option` | Embedded, SQLite-backed, dev/test only |
| Supabase alternative | `deferred_option` | Managed PG, pgvector yes, but no AGE |
| Archetype footer | `callout_bar` | How archetypes split on this decision |

## Anti-Hallucination Rules

1. PostgreSQL Unified prior probability is 0.45 -- from REPORT.md.
2. Graph strategy uses Apache AGE (P=0.65 given PostgreSQL) -- from REPORT.md conditional walkthrough.
3. Vector strategy uses pgvector (P=0.70 given PostgreSQL) -- from REPORT.md conditional walkthrough.
4. Archetype database probabilities from REPORT.md: Engineer PG 0.60, Musician Supabase 0.55, Solo Supabase/SQLite 0.40/0.40, Well-Funded PG 0.45.
5. Supabase is a managed PostgreSQL service -- it does support pgvector but NOT Apache AGE for graph queries.
6. Chroma is SQLite-backed and embedded -- suitable for dev/test, not production scale.
7. The scaffold does NOT currently use Pinecone, Qdrant, or Weaviate.
8. CockroachDB (0.15 prior) is the fourth option -- not shown for simplicity but exists.
9. Background must be warm cream (#f6f3e6).

## Alt Text

PostgreSQL unified architecture showing three capabilities (relational, graph, vector) in one database, compared against Pinecone, Chroma, and Supabase alternatives.
