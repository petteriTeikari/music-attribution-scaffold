# fig-topic-05: Data Harmonization Pipelines

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-topic-05 |
| **Title** | Data Harmonization — Reconciling Five Heterogeneous Metadata Sources |
| **Audience** | General + Technical |
| **Complexity** | L2 (overview) |
| **Location** | Landing page, Topic Card V (Pipeline & Data group) |
| **Priority** | P2 (Medium) |
| **Dimensions** | 1200 x 900px (4:3 aspect ratio) |

## Purpose & Key Message

Five data sources converging through a harmonization pipeline into unified records, following Santos et al. (arXiv:2502.07132). Uses "harmonize" rather than "normalize" because we are *reconciling semantically heterogeneous schemas* — not just reformatting a single source. Each source has different schema conventions, vocabulary, and quality characteristics. Communicates: "five music databases describe the same reality using five different vocabularies — harmonization reconciles them while preserving provenance."

Key distinction from Santos et al.:
- **Normalization** = squashing to a single canonical form (lossy, one-directional)
- **Harmonization** = reconciling multiple valid representations while respecting source-specific semantics
- Three primitives: `match_schema` → `match_values` → `materialize_mapping`

## Visual Concept (ASCII Layout)

```
┌──────────────────────────────────────────────────────────┐
│                                                          │
│  SOURCE SCHEMAS (each different)                         │
│  ─────────────────────────────                          │
│                                                          │
│  ● MusicBrainz ────╲  artist_credit (structured obj)    │
│  ● Discogs     ────╲╲  artists[] + extraartists[]       │
│  ● AcoustID    ─────►► HARMONIZE ──► Unified Records   │
│  ● Streaming   ────╱╱  spotify_id / apple_id            │
│  ● File Meta   ────╱  ID3 free-text fields              │
│                                                          │
│  THREE PRIMITIVES                                        │
│  ─────────────────                                      │
│  ① MATCH SCHEMA    ② MATCH VALUES    ③ MATERIALIZE     │
│  source cols →     "Written-By" →    declarative        │
│  target fields     "SONGWRITER"      pipeline           │
│                                                          │
│  SCHEMA CONFLICTS (real examples)                        │
│  ────────────────────────────────                       │
│  MusicBrainz: "artist credit" = structured object       │
│  Discogs: "Written-By" vs "Songwriter" vs "Composed By" │
│  Streaming: Spotify genre "electronica" ≠               │
│             MusicBrainz tag "electronic"                 │
│  File Meta: free-text, user-entered, no vocabulary      │
│                                                          │
│  quality: ████ ████ ███ ██ █                            │
│           MB   Disc  AcID Str  File                     │
│                                                          │
│  ■ CLEAN ■ NOISY ■ MISSING  Provenance preserved       │
│                                                          │
│  (Santos et al. 2025, arXiv:2502.07132)                 │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|-------------|-------------|
| Source dots | `data_sources` | Five colored dots with source-specific schema notes |
| Convergence arrows | `line_flow` | Arrows converging to harmonization funnel |
| Funnel | `data_primary` | Teal trapezoid labeled "HARMONIZE" |
| Three primitives | `region_secondary` | Three boxes: match_schema, match_values, materialize |
| Schema conflict examples | `data_warning` | Orange-highlighted real vocabulary conflicts |
| Quality bars | `data_gradient` | Horizontal bars per source, teal (clean) to orange (noisy) |
| Output records | `data_accent` | Coral square markers for harmonized records |
| Source labels | `label_editorial` | ALL-CAPS source names with schema annotations |
| Provenance note | `label_subtle` | "Provenance preserved" — which source contributed what |
| Citation | `label_subtle` | Santos et al. reference |

## Anti-Hallucination Rules

1. **Font names are internal** — do NOT render them as visible labels.
2. **Semantic tags are internal** — do NOT render them.
3. **Pixel sizes and rendering instructions are internal** — do NOT render.
4. Only the following text should appear: "DATA HARMONIZATION", "MUSICBRAINZ", "DISCOGS", "ACOUSTID", "STREAMING", "FILE METADATA", "HARMONIZE", "MATCH SCHEMA", "MATCH VALUES", "MATERIALIZE", schema conflict examples, quality labels, "CLEAN", "NOISY", "MISSING", "Provenance preserved", citation text.

## Alt Text

Infographic showing five music metadata sources (MusicBrainz, Discogs, AcoustID, Streaming, File Metadata) converging through a harmonization funnel into unified records. Each source is annotated with its schema characteristics — MusicBrainz uses structured artist credit objects, Discogs uses role-labeled arrays, streaming has platform-specific IDs, and file metadata contains free-text. Below the funnel, three harmonization primitives are shown: match_schema (mapping columns), match_values (reconciling vocabularies like "Written-By" to "SONGWRITER"), and materialize (producing the final pipeline). Concrete schema conflicts are listed. Quality bars range from high (teal, MusicBrainz) to low (orange, file metadata). A note emphasizes that provenance is preserved through harmonization.
