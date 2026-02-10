# ADR-0001: Use PostgreSQL + pgvector

## Status

Accepted

## Context

The system needs a database solution for storing:
- Artist and song attribution data from multiple sources
- Vector embeddings for semantic search
- Entity relationships and provenance tracking

Options considered:
1. **Neo4j**: Graph database, natural for relationships
2. **PostgreSQL + pgvector**: Relational with vector extension
3. **Dedicated vector DB (Pinecone, Weaviate)**: Specialized for embeddings

## Decision

Use PostgreSQL with the pgvector extension.

## Consequences

### Positive

- **Single database**: No need to manage multiple systems
- **Mature ecosystem**: Well-understood, extensive tooling
- **pgvector performance**: Adequate for our scale (~1M vectors expected)
- **ACID compliance**: Strong consistency for attribution data
- **Neon compatibility**: Serverless PostgreSQL with pgvector support

### Negative

- **No native graph traversal**: Must use recursive CTEs or multiple queries
- **Scale ceiling**: May need partitioning at very high scale

### Rationale

Neo4j adds operational complexity without sufficient benefit for our use case. The relationship patterns in music attribution (artist → songs → credits) are well-served by relational joins. pgvector handles our embedding needs without requiring a separate vector database.

See [PLAN.md Section 11](../../planning/initial-hierarchical-doc-planning/PLAN.md) for full technical rationale.
