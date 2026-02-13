# fig-theory-14: Source Agreement Scoring

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-theory-14 |
| **Title** | Source Agreement Scoring |
| **Audience** | L2 (PhD Student / Policy Researcher) |
| **Complexity** | L2 (academic terms, structural understanding) |
| **Location** | docs/theory/confidence-scoring.md |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure shows how confidence increases when multiple independent sources agree on the same attribution claim. It answers: "How does agreement between different databases affect the confidence score?"

The key message is: "More independent sources agreeing on the same attribution claim yields higher confidence -- a claim confirmed by MusicBrainz, Discogs, AND an artist's own input is far more trustworthy than a single file tag."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  SOURCE AGREEMENT SCORING                                      |
|  ■ More Agreement = Higher Confidence                          |
+---------------------------------------------------------------+
|                                                                |
|                  ┌─────────────────┐                           |
|                  │                 │                           |
|           ┌──────┤   MusicBrainz   ├──────┐                   |
|           │      │                 │      │                   |
|           │      └────────┬────────┘      │                   |
|           │               │               │                   |
|    ┌──────┴──────┐  ┌─────┴─────┐  ┌─────┴──────┐           |
|    │             │  │           │  │            │           |
|    │   Discogs   │  │  CENTER   │  │  AcoustID  │           |
|    │             │  │  OVERLAP  │  │            │           |
|    └──────┬──────┘  │  = HIGH   │  └─────┬──────┘           |
|           │         │CONFIDENCE │        │                   |
|           │         └─────┬─────┘        │                   |
|           │               │               │                   |
|    ┌──────┴──────┐        │        ┌──────┴──────┐           |
|    │  File       │        │        │  Artist     │           |
|    │  Metadata   ├────────┘        │  Input      │           |
|    │             │                 │             │           |
|    └─────────────┘                 └─────────────┘           |
|                                                                |
+---------------------------------------------------------------+
|                                                                |
|  AGREEMENT EXAMPLES                                            |
|  ──────────────────                                            |
|                                                                |
|  ┌─────────────────────┐  Confidence                          |
|  │ 1 source (file tag) │  ████░░░░░░  0.35                    |
|  └─────────────────────┘                                       |
|  ┌─────────────────────┐                                       |
|  │ 2 sources agree     │  ██████░░░░  0.62                    |
|  │ (file + MusicBrainz)│                                       |
|  └─────────────────────┘                                       |
|  ┌─────────────────────┐                                       |
|  │ 3 sources agree     │  ████████░░  0.81                    |
|  │ (+ Discogs)         │                                       |
|  └─────────────────────┘                                       |
|  ┌─────────────────────┐                                       |
|  │ 4+ sources + artist │  ██████████  0.94                    |
|  │ verification        │                                       |
|  └─────────────────────┘                                       |
|                                                                |
+---------------------------------------------------------------+
|  ■ Each source has an AUTHORITY WEIGHT. Artist input weighs    |
|    most. File metadata weighs least.                           |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "SOURCE AGREEMENT SCORING" with coral accent square |
| Subtitle | `label_editorial` | "More Agreement = Higher Confidence" |
| MusicBrainz circle | `source_musicbrainz` | Source database bubble in Venn-style layout |
| Discogs circle | `source_discogs` | Source database bubble |
| AcoustID circle | `source_acoustid` | Source database bubble |
| File Metadata circle | `source_file` | Source with lowest authority weight |
| Artist Input circle | `source_artist` | Source with highest authority weight |
| Center overlap label | `confidence_high` | "HIGH CONFIDENCE" in the center where all sources agree |
| 1-source bar | `confidence_low` | Red-coded bar at 0.35 confidence |
| 2-source bar | `confidence_medium` | Amber-coded bar at 0.62 confidence |
| 3-source bar | `confidence_medium` | Amber-coded bar at 0.81 confidence |
| 4-source bar | `confidence_high` | Green-coded bar at 0.94 confidence |
| Confidence values | `data_mono` | 0.35, 0.62, 0.81, 0.94 in monospace |
| Footer callout | `callout_box` | Authority weight hierarchy: artist > databases > file metadata |

## Anti-Hallucination Rules

1. The five sources are: MusicBrainz, Discogs, AcoustID, File Metadata, Artist Input. Do NOT add Spotify, Apple, etc.
2. Authority weight order: Artist Input (highest) > MusicBrainz = Discogs (medium) > AcoustID (low-medium) > File Metadata (lowest).
3. Confidence values (0.35, 0.62, 0.81, 0.94) are ILLUSTRATIVE examples, not exact computed values.
4. Do NOT claim that simple counting determines confidence -- sources have different WEIGHTS.
5. "Agreement" means the sources report the same attribution claim -- not just that they have data.
6. Do NOT include mathematical formulas for weighted voting -- this is L2.
7. The Venn diagram is CONCEPTUAL -- do NOT imply that all sources always have overlapping data.
8. Background must be warm cream (#f6f3e6), not white or gray.

## Alt Text

Venn diagram of five data sources with center overlap labeled high confidence, plus bar chart showing confidence rising from 0.35 with one source to 0.94 with four sources plus artist verification.
