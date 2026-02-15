# fig-howto-01: How to Add a New Data Source

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-howto-01 |
| **Title** | How to Add a New Data Source |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 (implementation detail) |
| **Location** | docs/contributing.md, docs/guides/add-data-source.md |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure guides engineers through the five-step process of adding a new external data source (e.g., Spotify, Apple Music, or a custom catalog) to the ETL pipeline. It answers: "I have a new music metadata source -- what do I need to build, and in what order?"

The key message is: "Adding a data source follows a strict five-step path: create the extractor, implement the interface, register it in the orchestrator, define quality gate rules, and write tests. Each step has a corresponding module location."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  HOW TO ADD A NEW DATA SOURCE                                  |
|  ■ Five Steps from Interface to Integration                    |
+---------------------------------------------------------------+
|                                                                |
|  I. CREATE EXTRACTOR         II. IMPLEMENT INTERFACE           |
|  ─────────────────           ──────────────────────            |
|  ┌─────────────────┐         ┌─────────────────────┐          |
|  │ src/music_       │         │ class MyExtractor    │          |
|  │  attribution/    │   ──>   │   (BaseExtractor):   │          |
|  │  etl/            │         │                      │          |
|  │  extractors/     │         │   extract()          │          |
|  │  my_source.py    │         │   normalize()        │          |
|  └─────────────────┘         │   validate()         │          |
|           │                   └─────────────────────┘          |
|           │                             │                       |
|           v                             v                       |
|  III. REGISTER IN ORCHESTRATOR                                 |
|  ─────────────────────────────                                 |
|  ┌─────────────────────────────────────────────┐              |
|  │ etl/orchestrator.py                          │              |
|  │ EXTRACTORS = { ..., "my_source": MyExtractor │              |
|  │ }                                            │              |
|  └─────────────────────────────────────────────┘              |
|           │                             │                       |
|           v                             v                       |
|  IV. ADD QUALITY GATES       V. WRITE TESTS                   |
|  ─────────────────           ─────────────                     |
|  ┌─────────────────┐         ┌─────────────────┐              |
|  │ Quality rules:   │         │ tests/unit/      │              |
|  │ - Field coverage │         │   test_my_source │              |
|  │ - Authority wt.  │         │   .py            │              |
|  │ - Schema match   │         │                  │              |
|  └─────────────────┘         │ tests/integration │              |
|                               │   /test_my_       │              |
|                               │   source_e2e.py   │              |
|                               └─────────────────┘              |
|                                                                |
+---------------------------------------------------------------+
|  ■ Each step has a corresponding test — no step ships untested |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "HOW TO ADD A NEW DATA SOURCE" in Instrument Serif ALL-CAPS with coral accent square |
| Subtitle | `label_editorial` | "Five Steps from Interface to Integration" in Plus Jakarta Sans caps |
| Step I box | `etl_extract` | File path location for new extractor module |
| Step II box | `processing_stage` | BaseExtractor interface with three required methods |
| Step III box | `processing_stage` | Orchestrator registration showing EXTRACTORS dict |
| Step IV box | `processing_stage` | Quality gate rules: field coverage, authority weight, schema match |
| Step V box | `processing_stage` | Test file locations for unit and integration tests |
| Flow arrows (I to II, II to III, etc.) | `data_flow` | Sequential step progression arrows |
| Roman numerals I-V | `section_numeral` | Step headers in editorial style |
| Method names (extract, normalize, validate) | `data_mono` | IBM Plex Mono for code identifiers |
| Footer callout | `callout_box` | "Each step has a corresponding test" reminder |

## Anti-Hallucination Rules

1. The BaseExtractor interface has three methods: `extract()`, `normalize()`, `validate()` -- do not invent additional methods.
2. Extractors live in `src/music_attribution/etl/extractors/` -- not in a different directory.
3. The orchestrator is in `etl/orchestrator.py` -- not `pipeline.py` or `runner.py`.
4. Only three production data sources exist today: Discogs, MusicBrainz, file metadata -- do not show Spotify or Apple Music as existing sources.
5. Quality gate rules reference field coverage and authority weight -- not arbitrary thresholds.
6. SourceEnum values are defined in `src/music_attribution/schemas/` -- new sources must be added there too.
7. Background must be warm cream (#f6f3e6), not white or gray.
8. This is a scaffold -- the exact interface may vary by team archetype.

## Alt Text

How-to guide: five-step workflow for adding a new music metadata data source to the open-source attribution scaffold ETL pipeline, covering extractor creation, BaseExtractor interface implementation, orchestrator registration, quality gate configuration, and test coverage -- each step maps to a specific module path ensuring transparent confidence scoring from ingestion onward.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![How-to guide: five-step workflow for adding a new music metadata data source to the open-source attribution scaffold ETL pipeline, covering extractor creation, BaseExtractor interface implementation, orchestrator registration, quality gate configuration, and test coverage -- each step maps to a specific module path ensuring transparent confidence scoring from ingestion onward.](docs/figures/repo-figures/assets/fig-howto-01-add-new-data-source.jpg)

*Five-step data source integration path for the Music Attribution Scaffold ETL pipeline. Each step corresponds to a specific module in the `src/music_attribution/etl/` package, enforcing the attribution-by-design principle that every new source must implement extraction, normalization, and validation before registration (Teikari, 2026).*

### From this figure plan (relative)

![How-to guide: five-step workflow for adding a new music metadata data source to the open-source attribution scaffold ETL pipeline, covering extractor creation, BaseExtractor interface implementation, orchestrator registration, quality gate configuration, and test coverage -- each step maps to a specific module path ensuring transparent confidence scoring from ingestion onward.](../assets/fig-howto-01-add-new-data-source.jpg)
