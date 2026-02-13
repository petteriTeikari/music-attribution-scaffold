"""Entity resolution pipeline.

Multi-signal entity resolution for music attribution. Implements a cascade
of resolution strategies ordered by confidence and cost:

1. **Identifier matching** -- ISRC/ISWC/ISNI exact match (confidence=1.0)
2. **String similarity** -- Jaro-Winkler + token-sort fuzzy matching
3. **Embedding similarity** -- Sentence-transformer cosine similarity via pgvector
4. **Splink linkage** -- Fellegi-Sunter probabilistic record linkage
5. **Graph resolution** -- Shared-relationship evidence from knowledge graph
6. **LLM disambiguation** -- PydanticAI structured disambiguation (cost-gated)

The orchestrator combines signals from all active strategies using weighted
scoring and produces ``ResolvedEntity`` objects with per-method confidence
breakdowns and A0-A3 assurance levels.

See Also
--------
music_attribution.schemas.resolved : Pydantic models for resolution output.
music_attribution.attribution : Downstream attribution scoring.

Notes
-----
Implements the resolution cascade described in Teikari (2026), Section 4.
The cascade design balances accuracy against computational cost: cheap
deterministic methods run first, expensive probabilistic methods only fire
when earlier stages produce ambiguous results.
"""

from __future__ import annotations
