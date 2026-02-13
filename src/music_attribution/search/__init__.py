"""Search services for music attribution scaffold.

Provides three search modalities and a hybrid fusion service:

Submodules
----------
text_search
    LIKE-based text search across attribution record JSONB fields.
    Upgradeable to PostgreSQL ``tsvector`` + GIN indexes for production.
vector_search
    Cosine similarity search across entity embeddings (pgvector).
    Supports HNSW index-accelerated queries on PostgreSQL.
hybrid_search
    Reciprocal Rank Fusion (RRF) combining text, vector, and graph
    context modalities into a single ranked result set.

See Also
--------
music_attribution.db.models.EntityEmbeddingModel : Embedding storage.
music_attribution.db.models.EdgeModel : Graph edges for context expansion.
"""

from __future__ import annotations
