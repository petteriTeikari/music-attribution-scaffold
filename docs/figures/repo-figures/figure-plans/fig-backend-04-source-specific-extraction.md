# fig-backend-04: Source-Specific Extraction

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-backend-04 |
| **Title** | Five Extractors: What Each Source Returns |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 |
| **Location** | docs/architecture/, docs/etl/ |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure shows each of the five ETL connectors side by side, illustrating what data each source provides, its connector class, the library it wraps, and its default source_confidence value. Engineers need this to understand data coverage gaps and which sources contribute which fields.

The key message is: "Each source excels at different data -- MusicBrainz provides ISRCs and credits, Discogs provides personnel, AcoustID provides fingerprint matching, tinytag reads local file tags, and Artist Input captures declarations."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  SOURCE-SPECIFIC EXTRACTORS                                    |
|  ■ Five Connectors — Each Returns Different Data               |
+---------------------------------------------------------------+
|                                                                 |
|  MUSICBRAINZ         DISCOGS            ACOUSTID               |
|  ────────────        ───────            ────────               |
|  Class:              Class:             Class:                 |
|  MusicBrainzConn.    DiscogsConnector   AcoustIDConnector      |
|  Lib: musicbrainzngs Lib: discogs-client Lib: pyacoustid       |
|  Confidence: 0.90    Confidence: 0.85   Confidence: varies     |
|                                                                 |
|  Returns:            Returns:           Returns:               |
|  ■ ISRC identifiers  ■ Release credits  ■ Fingerprint match   |
|  ■ Artist credits    ■ Personnel roles  ■ MusicBrainz MBID    |
|  ■ ISNI (artists)    ■ Name variations  ■ Match score [0,1]   |
|  ■ Release dates     ■ Release dates    ■ Artist names        |
|  ■ Relationships     ■ Track durations  ■ Duration            |
|    (10 rel. types)   ■ Discogs ID       ■ AcoustID UUID       |
|  ■ MBID identifier   ■ Country/year                            |
|                                                                 |
|  ─────────────────────────────────────────────────────         |
|                                                                 |
|  TINYTAG (FILE)      ARTIST INPUT                              |
|  ──────────────      ────────────                              |
|  Class:              Class:                                    |
|  FileMetadataReader  (manual/form)                             |
|  Lib: tinytag        No external API                           |
|  Confidence: 0.70    Confidence: 0.60                          |
|                                                                 |
|  Returns:            Returns:                                  |
|  ■ Title/artist      ■ Artist declarations                    |
|  ■ Album name        ■ Role claims                            |
|  ■ Duration (ms)     ■ Evidence type                          |
|  ■ Year              ■ Free-text notes                        |
|  ■ No ISRC/credits   ■ Highest authority                     |
|    (tinytag limit)     when verified                           |
|                                                                 |
+---------------------------------------------------------------+
|  ■ source_confidence reflects data authority, not match score  |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "SOURCE-SPECIFIC EXTRACTORS" |
| MusicBrainz column | `source_musicbrainz` | Connector class, library, confidence, return fields |
| Discogs column | `source_discogs` | Connector class, library, confidence, return fields |
| AcoustID column | `source_acoustid` | Connector class, library, confidence, return fields |
| tinytag column | `source_file` | Reader class, library, confidence, return fields |
| Artist Input column | `source_artist` | No class (manual), confidence, return fields |
| Confidence values | `data_mono` | 0.90, 0.85, varies, 0.70, 0.60 in monospace |
| Return field bullets | `feature_list` | Bullet lists of what each source provides |
| Library names | `data_mono` | musicbrainzngs, discogs-client, pyacoustid, tinytag |
| Accent divider | `accent_line` | Coral horizontal line between top row and bottom row |
| Footer callout | `callout_box` | "source_confidence reflects data authority, not match score" |

## Anti-Hallucination Rules

1. MusicBrainz default source_confidence is 0.9, Discogs is 0.85, tinytag is 0.7. These are from the actual connector code.
2. AcoustID confidence varies per result (it uses the API-returned score), not a fixed value.
3. tinytag does NOT provide ISRC or detailed credits -- this is explicitly noted in the code with TODO comments.
4. The libraries are: musicbrainzngs (MusicBrainz), python3-discogs-client (Discogs), pyacoustid (AcoustID), tinytag (file metadata).
5. MusicBrainz maps 10 relationship types via _RELATION_TYPE_MAP. Discogs maps ~30 role strings via _ROLE_MAP.
6. FileMetadataReader supports: MP3, M4A, WAV, OGG, FLAC, WMA, AIFF via tinytag.
7. Artist Input is SourceEnum.ARTIST_INPUT, not USER_INPUT.
8. Do NOT include Spotify, Apple Music, or any source not in SourceEnum.

## Alt Text

Five-column comparison of ETL extractors showing MusicBrainz, Discogs, AcoustID, tinytag, and Artist Input with their connector classes, libraries, default confidence values, and returned data fields.
