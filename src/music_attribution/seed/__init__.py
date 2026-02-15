"""Seed data loaders for the music attribution scaffold.

Provides idempotent seed data loaders that populate the database with
representative attribution records for development and demonstration.

Submodules
----------
imogen_heap
    Loader for 8 Imogen Heap attribution records spanning the full
    confidence range (0.0--0.95), with rich provenance chains and
    uncertainty metadata. Uses deterministic UUIDs (``uuid5``) for
    idempotent seeding.

See Also
--------
music_attribution.schemas.attribution : AttributionRecord schema.
"""

from __future__ import annotations
