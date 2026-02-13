# fig-backend-02: NormalizedRecord Schema

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-backend-02 |
| **Title** | NormalizedRecord (BO-1): Field-by-Field Schema |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 |
| **Location** | docs/architecture/, docs/schemas/ |
| **Priority** | P0 (Critical) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure shows the complete field layout of the NormalizedRecord Pydantic model -- the primary boundary object produced by the ETL pipeline. Engineers need to understand every field, its type, and whether it is required or optional, to build connectors that emit valid records.

The key message is: "NormalizedRecord is the universal schema that every data source must conform to -- 12 top-level fields with nested IdentifierBundle, SourceMetadata, and Relationship sub-models."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  NORMALIZEDRECORD (BO-1)                                       |
|  ■ Pydantic BaseModel — schema_version 1.0.0                  |
+---------------------------------------------------------------+
|                                                                 |
|  REQUIRED FIELDS                 OPTIONAL / DEFAULTED           |
|  ───────────────                 ──────────────────             |
|  source: SourceEnum              alternative_names: list[str]   |
|  source_id: str                  raw_payload: dict | None       |
|  entity_type: EntityTypeEnum                                    |
|  canonical_name: str             IDENTIFIERS (IdentifierBundle) |
|  fetch_timestamp: datetime(UTC)  ──────────────────────────     |
|  source_confidence: float[0,1]   isrc: str | None               |
|                                  iswc: str | None               |
|  record_id: UUID (auto)          isni: str | None               |
|  schema_version: "1.0.0"        ipi: str | None                |
|                                  mbid: str | None               |
|  METADATA (SourceMetadata)       discogs_id: int | None         |
|  ──────────────────────          acoustid: str | None           |
|  roles: list[str]                                               |
|  release_date: str | None        RELATIONSHIPS (list)           |
|  release_country: str | None     ──────────────────             |
|  genres: list[str]               relationship_type: Rel.Enum    |
|  duration_ms: int | None         target_source: SourceEnum      |
|  track_number: int | None        target_source_id: str          |
|  medium_format: str | None       target_entity_type: EntityEnum |
|  language: str | None            attributes: dict[str, str]     |
|  extras: dict[str, str]                                         |
|                                                                 |
+---------------------------------------------------------------+
|  VALIDATORS                                                     |
|  ■ canonical_name must be non-empty after strip                |
|  ■ fetch_timestamp must be timezone-aware (UTC)                |
|  ■ Machine sources require >= 1 identifier                     |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "NORMALIZEDRECORD (BO-1)" in editorial caps |
| Subtitle | `label_editorial` | "Pydantic BaseModel -- schema_version 1.0.0" |
| Required fields column | `primary_outcome` | Left column showing required fields with types |
| Optional fields column | `processing_stage` | Right column showing optional/defaulted fields |
| IdentifierBundle section | `processing_stage` | Nested model with 7 optional identifier fields |
| SourceMetadata section | `processing_stage` | Nested model with 8 metadata fields |
| Relationship section | `processing_stage` | Nested model showing relationship structure |
| Field type annotations | `data_mono` | Type annotations in monospace (str, UUID, float, etc.) |
| Validator rules | `callout_box` | Three Pydantic validators listed at bottom |
| Source/entity enums | `label_editorial` | SourceEnum and EntityTypeEnum references |
| Accent dividers | `accent_line` | Horizontal coral lines separating sections |

## Anti-Hallucination Rules

1. The exact fields come from `src/music_attribution/schemas/normalized.py`. Do NOT invent fields.
2. IdentifierBundle has exactly 7 fields: isrc, iswc, isni, ipi, mbid, discogs_id, acoustid.
3. SourceMetadata has exactly 8 fields: roles, release_date, release_country, genres, duration_ms, track_number, medium_format, language, extras.
4. There are exactly 3 validators: validate_canonical_name, validate_fetch_timestamp, validate_identifiers_for_machine_sources.
5. Machine sources requiring identifiers are: MUSICBRAINZ, DISCOGS, ACOUSTID. Not FILE_METADATA or ARTIST_INPUT.
6. source_confidence is a float constrained to [0.0, 1.0] via Pydantic Field(ge=0.0, le=1.0).
7. schema_version defaults to "1.0.0" -- do not use a different version.
8. Background must be warm cream (#f6f3e6).

## Alt Text

Schema diagram of the NormalizedRecord Pydantic model showing 12 top-level fields, nested IdentifierBundle with 7 identifiers, SourceMetadata with 8 fields, and 3 validation rules.
