# fig-backend-01: ETL Pipeline Overview

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-backend-01 |
| **Title** | ETL Pipeline: Five Sources to NormalizedRecord |
| **Audience** | L2 (PhD Student / Policy Researcher) |
| **Complexity** | L2 |
| **Location** | docs/architecture/, docs/etl/ |
| **Priority** | P0 (Critical) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure shows how five external data sources converge through the ETL pipeline into a single unified boundary object (NormalizedRecord). It answers "Where does the attribution data come from, and how is it unified?" for researchers who need to understand the data provenance chain.

The key message is: "Five independent data sources -- each with different APIs, rate limits, and data quality -- are normalized into a common schema before any resolution or scoring occurs."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  I. ETL PIPELINE                                               |
|  ■ Data Engineering — Source Extraction & Normalization         |
+---------------------------------------------------------------+
|                                                                 |
|  ┌────────────┐                                                |
|  │ MusicBrainz │──┐   Rate Limits                              |
|  │  1 req/s    │  │   ──────────                               |
|  └────────────┘  │                                              |
|  ┌────────────┐  │   ┌──────────────┐    ┌──────────────────┐  |
|  │  Discogs   │──┼──>│ Token Bucket  │──>│  Quality Gate     │  |
|  │ 60 req/min │  │   │ Rate Limiter  │   │  ─────────────   │  |
|  └────────────┘  │   └──────────────┘    │  identifier_cov  │  |
|  ┌────────────┐  │          │            │  no_duplicates    │  |
|  │ AcoustID   │──┤          │            │  source_distrib   │  |
|  │  3 req/s   │  │          ▼            └────────┬─────────┘  |
|  └────────────┘  │   ┌──────────────┐             │            |
|  ┌────────────┐  │   │  Connector    │             ▼            |
|  │  tinytag   │──┤   │  Transform    │    ┌────────────────┐   |
|  │  (local)   │  │   │  ──────────   │    │ NormalizedRecord│   |
|  └────────────┘  │   │  Raw → BO-1   │    │    (BO-1)       │   |
|  ┌────────────┐  │   └──────────────┘    │  ■ Boundary Obj  │   |
|  │  Artist    │──┘                       └────────────────┘   |
|  │  Input     │                                                |
|  └────────────┘                                                |
|                                                                 |
+---------------------------------------------------------------+
|  ■ Each source has its own connector, rate limiter, and retry  |
|    strategy. All converge to NormalizedRecord (BO-1).           |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "ETL PIPELINE" in editorial caps with accent square |
| Subtitle | `label_editorial` | "Data Engineering -- Source Extraction & Normalization" |
| MusicBrainz source box | `source_musicbrainz` | Box showing source name and rate limit "1 req/s" |
| Discogs source box | `source_discogs` | Box showing source name and rate limit "60 req/min" |
| AcoustID source box | `source_acoustid` | Box showing source name and rate limit "3 req/s" |
| tinytag source box | `source_file` | Box showing source name and "(local)" -- no rate limit |
| Artist Input source box | `source_artist` | Box showing source name -- no rate limit |
| Token Bucket Rate Limiter | `processing_stage` | Intermediate stage enforcing API compliance |
| Connector Transform | `processing_stage` | Transform step converting raw API responses to BO-1 |
| Quality Gate | `processing_stage` | Validation step with three named checks |
| NormalizedRecord output | `primary_outcome` | Boundary object output with accent marker |
| Rate limit labels | `data_mono` | Per-source rate limits in monospace |
| Convergence arrows | `data_flow` | Five arrows merging into single pipeline |
| Footer callout | `callout_box` | Summary: each source has own connector, all converge to BO-1 |

## Anti-Hallucination Rules

1. There are exactly 5 sources: MUSICBRAINZ, DISCOGS, ACOUSTID, FILE_METADATA (tinytag), ARTIST_INPUT. Do NOT add Spotify, Apple, or any other source.
2. MusicBrainz rate limit is 1 req/s. Discogs is 60 req/min authenticated (1/s), 25 req/min unauthenticated. AcoustID is 3 req/s. These are from the actual code.
3. tinytag reads local files -- it has no API rate limit.
4. The output boundary object is called NormalizedRecord (BO-1), not "NormalizedEntity" or "RawRecord".
5. The quality gate has exactly three checks: identifier_coverage, no_duplicates, source_distribution. Do not invent additional checks.
6. The rate limiter is a TokenBucketRateLimiter class, not a sliding window or leaky bucket.
7. Background must be warm cream (#f6f3e6), not white.

## Alt Text

Pipeline diagram showing the open-source music attribution ETL pipeline where five music metadata sources — MusicBrainz, Discogs, AcoustID, tinytag file reader, and Artist Input — converge through token bucket rate limiting and a three-check data quality gate into a unified NormalizedRecord boundary object, enabling transparent confidence scoring downstream.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Pipeline diagram showing the open-source music attribution ETL pipeline where five music metadata sources — MusicBrainz, Discogs, AcoustID, tinytag file reader, and Artist Input — converge through token bucket rate limiting and a three-check data quality gate into a unified NormalizedRecord boundary object, enabling transparent confidence scoring downstream.](docs/figures/repo-figures/assets/fig-backend-01-etl-pipeline-overview.jpg)

*Figure 1. The ETL pipeline extracts music metadata from five independent sources, each with distinct APIs and rate limits, normalizing all records into a common NormalizedRecord schema before entity resolution or confidence scoring occurs.*

### From this figure plan (relative)

![Pipeline diagram showing the open-source music attribution ETL pipeline where five music metadata sources — MusicBrainz, Discogs, AcoustID, tinytag file reader, and Artist Input — converge through token bucket rate limiting and a three-check data quality gate into a unified NormalizedRecord boundary object, enabling transparent confidence scoring downstream.](../assets/fig-backend-01-etl-pipeline-overview.jpg)
