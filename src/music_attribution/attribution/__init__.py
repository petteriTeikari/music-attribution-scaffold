"""Music Attribution Scaffold - attribution module.

Pipeline 3 of the five-pipeline architecture. Transforms ``ResolvedEntity``
objects from the resolution pipeline into ``AttributionRecord`` objects with:

- **Multi-source credit aggregation** -- weighted voting across data sources
  (MusicBrainz > Discogs > file metadata) to produce per-credit confidence.
- **Conformal prediction calibration** -- ensures stated confidence levels
  have calibrated coverage (e.g., "90% confident" actually covers 90% of
  cases) using Adaptive Prediction Sets (APS).
- **Persistence** -- both in-memory (dev/test) and async PostgreSQL
  repositories with versioned provenance chains.
- **Priority queue** -- active-learning-inspired review ordering that
  surfaces the most informative records for human expert review.

Notes
-----
Implements the attribution scoring framework described in Teikari (2026),
Section 5. The conformal prediction approach follows Vovk et al. (2005)
and produces prediction sets rather than point estimates, providing
mathematically grounded uncertainty quantification.

See Also
--------
music_attribution.resolution : Upstream entity resolution (Pipeline 2).
music_attribution.schemas.attribution : Pydantic models for attribution output.
"""

from __future__ import annotations
