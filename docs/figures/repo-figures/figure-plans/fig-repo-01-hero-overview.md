# fig-repo-01: Hero Overview

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-repo-01 |
| **Title** | What This Repo Does: From Broken Metadata to Transparent Attribution |
| **Audience** | All (newcomers, contributors, reviewers) |
| **Complexity** | L1 (concept introduction) |
| **Location** | README.md hero section, docs/index.md |
| **Priority** | P0 (Critical) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This is the first figure any visitor sees. It must answer "What does this repo do?" in under 5 seconds. The split-panel layout contrasts the problem (fragmented, unverified music metadata across siloed databases) with the solution (a transparent, confidence-scored attribution scaffold that unifies sources and exposes provenance).

The key message is: "Music metadata is broken -- 40%+ incorrect or incomplete. This scaffold provides the open-source infrastructure to fix it with probabilistic confidence, multi-source resolution, and machine-readable consent."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  MUSIC ATTRIBUTION SCAFFOLD                                    |
|  ■ Open-Source Research Infrastructure                         |
+-------------------------------+-------------------------------+
|                               |                               |
|  I. THE PROBLEM               |  II. THE SOLUTION             |
|  ─────────────                |  ──────────────               |
|                               |                               |
|  ┌─────────┐  ┌─────────┐   |  ┌─────────────────────────┐  |
|  │ Discogs │  │MusicBrz │   |  │   Unified Attribution    │  |
|  │  ???    │  │  ???    │   |  │   Record                 │  |
|  └────┬────┘  └────┬────┘   |  │                         │  |
|       │            │         |  │  Confidence: 0.87  ■    │  |
|    NO LINK     CONFLICTS     |  │  Sources: 3/3           │  |
|                               |  │  Provenance: Full       │  |
|  ┌─────────┐                 |  └─────────────────────────┘  |
|  │ Labels  │                 |                               |
|  │  ???    │  40%+ wrong     |  ■ Per-field confidence       |
|  └─────────┘                 |  ■ Multi-source resolution    |
|                               |  ■ Machine-readable consent  |
|  Siloed. Incomplete.         |  ■ A0-A3 assurance levels     |
|  Unverified.                 |  Transparent. Verified.       |
|                               |  Open-source.                |
+-------------------------------+-------------------------------+
|  "Companion code to Teikari (2026), SSRN No. 6109087"        |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "MUSIC ATTRIBUTION SCAFFOLD" in Instrument Serif ALL-CAPS with coral accent square |
| Subtitle | `label_editorial` | "Open-Source Research Infrastructure" in Plus Jakarta Sans caps |
| Problem panel (left) | `problem_zone` | Cream background, disconnected source boxes with "???" labels |
| Solution panel (right) | `solution_zone` | Slightly elevated, unified record card with confidence score |
| Source boxes (Discogs, MusicBrainz, Labels) | `source_fragment` | Disconnected, dashed borders, muted colors |
| Unified Record card | `primary_outcome` | Solid border, coral accent line, confidence gauge |
| Confidence score "0.87" | `data_mono` | IBM Plex Mono, green tier color |
| Bullet list (solution features) | `feature_list` | Four items with coral accent squares as bullets |
| Roman numerals I/II | `section_numeral` | Panel headers in editorial style |
| Footer citation | `citation_bar` | SSRN reference, muted text |
| Vertical divider | `accent_line_v` | Coral red vertical line separating panels |

## Anti-Hallucination Rules

1. The repo is a SCAFFOLD (framework/template), not a deployed product or SaaS application.
2. Confidence score example must be between 0.0 and 1.0 -- use 0.87 as shown.
3. Three external sources only: Discogs, MusicBrainz, System Own (not Spotify, Apple, etc.).
4. The SSRN number is 6109087 -- do not invent a different number.
5. "40%+" statistic refers to incorrect/incomplete metadata industry-wide -- do not cite a different figure.
6. Assurance levels are A0-A3 (four levels), not A1-A4 or any other range.
7. Do NOT include any AI-generated music or audio waveform imagery -- this is about metadata infrastructure.
8. Background must be warm cream (#f6f3e6), not white or yellow.

## Alt Text

Repository overview: split-panel infographic contrasting fragmented music metadata across siloed databases with an open-source attribution scaffold that unifies sources into a single record with 0.87 transparent confidence scoring, multi-source resolution, and A0-A3 assurance levels for music credits provenance.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Repository overview: split-panel infographic contrasting fragmented music metadata across siloed databases with an open-source attribution scaffold that unifies sources into a single record with 0.87 transparent confidence scoring, multi-source resolution, and A0-A3 assurance levels for music credits provenance.](docs/figures/repo-figures/assets/fig-repo-01-hero-overview.jpg)

*Figure 1. The Music Attribution Scaffold addresses the industry-wide problem of 40%+ incorrect or incomplete music metadata by providing open-source infrastructure for probabilistic confidence scoring, multi-source entity resolution, and machine-readable consent (companion code to Teikari, 2026, SSRN No. 6109087).*

### From this figure plan (relative)

![Repository overview: split-panel infographic contrasting fragmented music metadata across siloed databases with an open-source attribution scaffold that unifies sources into a single record with 0.87 transparent confidence scoring, multi-source resolution, and A0-A3 assurance levels for music credits provenance.](../assets/fig-repo-01-hero-overview.jpg)
