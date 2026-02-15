"""ETL pipeline connectors for external music data sources.

This package contains connectors for the four data sources in the
attribution pipeline:

* ``musicbrainz`` — MusicBrainz API (recordings, works, artists)
* ``discogs`` — Discogs API (release credits, artist profiles)
* ``acoustid`` — AcoustID fingerprint service (audio identification)
* ``file_metadata`` — Embedded audio file tags (tinytag)

Supporting modules:

* ``rate_limiter`` — token-bucket rate limiter for API compliance
* ``quality_gate`` — batch validation before entity resolution
* ``persistence`` — NormalizedRecord storage in PostgreSQL

All connectors produce ``NormalizedRecord`` boundary objects (defined
in ``music_attribution.schemas.normalized``) that serve as the handover
contract to the entity resolution pipeline.
"""

from __future__ import annotations
