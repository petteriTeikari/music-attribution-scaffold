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

Explains the primary database decision (PostgreSQL Unified) and vector strategy decision (pgvector). The key insight: a single PostgreSQL instance handles relational data, graph queries (via Apache AGE), and vector search (via pgvector) -- eliminating the need for separate databases. Shows comparison against alternatives and highlights the hosting spectrum from Neon (scale-to-zero for MVP) through Ubicloud managed PG (budget production) to self-managed (expert).

The key message is: "One database does three jobs: relational, graph, and vector -- PostgreSQL + pgvector + Apache AGE eliminates multi-database complexity. Hosting ranges from Neon (scale-to-zero, perfect for MVP) to Ubicloud managed (budget production on Hetzner)."

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
|  │ Vector-only  │ │ Dev/test     │ │ + pgvector   │          |
|  │ Separate DB  │ │ only         │ │ + no AGE     │          |
|  │ $70+/month   │ │ Free         │ │ Free-$25/mo  │          |
|  │──────────────│ │──────────────│ │──────────────│          |
|  │ Con: Another │ │ Con: Not     │ │ Con: No graph│          |
|  │ system       │ │ production   │ │ extension    │          |
|  └──────────────┘ └──────────────┘ └──────────────┘          |
|                                                                |
|  HOSTING SPECTRUM                                              |
|  ────────────────                                              |
|  ┌────────────┐  ┌────────────┐  ┌────────────┐             |
|  │ Neon       │  │ Ubicloud   │  │ Self-      │             |
|  │            │  │ Managed    │  │ Managed    │             |
|  │ Scale-to-  │  │            │  │            │             |
|  │ zero       │  │ Managed PG │  │ CNPG on    │             |
|  │ Branching  │  │ on Hetzner │  │ Hetzner    │             |
|  │ EU data    │  │ Open-src   │  │ bare-metal │             |
|  │ $0-19/mo   │  │ $10-40/mo  │  │ $5-20/mo   │             |
|  │            │  │            │  │            │             |
|  │ MVP ideal  │  │ Production │  │ Expert     │             |
|  └────────────┘  └────────────┘  └────────────┘             |
|                                                                |
+---------------------------------------------------------------+
|  Archetype: Engineers self-managed | Musicians Neon/Supabase   |
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
| Hosting spectrum | `branching_path` | Neon (MVP) → Ubicloud (production) → Self-managed (expert) |
| Archetype footer | `callout_bar` | How archetypes split on database and hosting |

## Anti-Hallucination Rules

1. PostgreSQL Unified prior probability is 0.45 -- from REPORT.md.
2. Graph strategy uses Apache AGE (P=0.65 given PostgreSQL) -- from REPORT.md conditional walkthrough.
3. Vector strategy uses pgvector (P=0.70 given PostgreSQL) -- from REPORT.md conditional walkthrough.
4. DB Hosting options in PRD v2.1.0: Neon (0.30, recommended), Supabase (0.20), Self-managed/CNPG (0.20), AWS RDS (0.10), Ubicloud managed (0.10), Turso (0.05).
5. Neon: scale-to-zero is optimal for MVP (90%+ idle time saves compute costs), database branching for preview environments, EU data residency (Frankfurt).
6. Ubicloud managed PostgreSQL on Hetzner: open-source, preview Feb 2026, Germany + Virginia regions.
7. Supabase is a managed PostgreSQL service -- it does support pgvector but NOT Apache AGE for graph queries.
8. Chroma is SQLite-backed and embedded -- suitable for dev/test, not production scale.
9. The scaffold does NOT currently use Pinecone, Qdrant, or Weaviate.
10. Background must be warm cream (#f6f3e6).

## Alt Text

Architecture decision: PostgreSQL with pgvector and Apache AGE unifying relational, graph, and vector capabilities in a single database for music attribution, compared against Pinecone, Chroma, and Supabase, with a hosting spectrum from Neon scale-to-zero for MVP through Ubicloud managed PostgreSQL on Hetzner for budget production to self-managed CloudNativePG for expert operators in the open-source attribution scaffold.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Architecture decision: PostgreSQL with pgvector and Apache AGE unifying relational, graph, and vector capabilities in a single database for music attribution, compared against Pinecone, Chroma, and Supabase, with a hosting spectrum from Neon scale-to-zero for MVP through Ubicloud managed PostgreSQL on Hetzner for budget production to self-managed CloudNativePG for expert operators in the open-source attribution scaffold.](docs/figures/repo-figures/assets/fig-choice-03-postgresql-pgvector.jpg)

*PostgreSQL Unified provides relational SQL, graph queries (Apache AGE), and vector search (pgvector) in a single process. Hosting ranges from Neon (scale-to-zero for MVP, EU data residency) through Ubicloud managed PG on Hetzner (budget production) to self-managed CloudNativePG (expert bare-metal).*

### From this figure plan (relative)

![Architecture decision: PostgreSQL with pgvector and Apache AGE unifying relational, graph, and vector capabilities in a single database for music attribution, compared against Pinecone, Chroma, and Supabase, with a hosting spectrum from Neon scale-to-zero for MVP through Ubicloud managed PostgreSQL on Hetzner for budget production to self-managed CloudNativePG for expert operators in the open-source attribution scaffold.](../assets/fig-choice-03-postgresql-pgvector.jpg)
