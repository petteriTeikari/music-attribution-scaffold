# fig-supplementary-03: Work Detail + Confidence Gauge

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-supplementary-03 |
| **Title** | Work Detail + Confidence Gauge |
| **Audience** | L1 (Music Industry Professional) |
| **Location** | Supplementary materials, docs/figures/repo-figures/ |
| **Priority** | P0 (Critical) |
| **Aspect Ratio** | 16:10 |
| **Layout Template** | A (Hero) |
| **Medium** | Frontend screenshot |

## Purpose

Shows a single work detail view with confidence gauge, source provenance, assurance level explanation. Answers: "How does the scaffold present detailed attribution transparency for an individual music work?"

## Key Message

The work detail view provides full attribution transparency -- a visual confidence gauge, source-by-source provenance breakdown, and assurance level explanation for each music work.

## Visual Concept

Full browser screenshot of a single work detail page (preferably "Hide and Seek" at 0.87 confidence) showing the confidence gauge component, source provenance cards, and assurance level explanation text.

```
+--+----------------------------------------------------------+
|  |  HIDE AND SEEK                                            |
|S |  Imogen Heap                                              |
|I |  ■                                                        |
|D |                                                           |
|E |  CONFIDENCE             ASSURANCE                         |
|B |  ┌───────────────┐      ┌───────────────┐                |
|A |  │               │      │               │                |
|R |  │   ◉ 0.87      │      │   A2           │                |
|  |  │   ████████░░  │      │  Corroborated  │                |
|  |  │               │      │               │                |
|  |  └───────────────┘      └───────────────┘                |
|  |                                                           |
|  |  SOURCE PROVENANCE                                        |
|  |  ─────────────────────────────────────                   |
|  |  MusicBrainz  ■  matched    0.91                         |
|  |  Discogs      ■  matched    0.84                         |
|  |  AcoustID     ■  matched    0.79                         |
|  |  File Meta    ■  partial    0.65                         |
|  |  Artist Input ■  verified   1.00                         |
|  |                                                           |
+--+----------------------------------------------------------+
```

## Screenshot Specification

| Parameter | Value |
|-----------|-------|
| **Browser** | Chrome / headless Chromium |
| **Viewport** | 1440 x 900 px |
| **Theme** | Light |
| **URL** | `localhost:3000/works/[id]` (select work with ~0.87 confidence, e.g. "Hide and Seek") |
| **State** | Work detail expanded, all sections loaded, no modals |
| **Annotations** | Optional -- callout arrows pointing to gauge, sources, assurance badge |
| **Device pixel ratio** | 1x (standard) |
| **Font loading** | Wait for all three font families to load |
| **Network** | Mock data loaded, no loading skeletons visible |
| **Scroll position** | Top of page, showing gauge and source provenance |

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Work title | `heading_display` | "Hide and Seek" in Instrument Serif |
| Artist name | `label_secondary` | "Imogen Heap" |
| Confidence gauge | `confidence_meter` | Visual gauge with role="meter", showing 0.87 in green tier |
| Confidence score | `data_mono` | "0.87" in IBM Plex Mono |
| Assurance badge | `badge_label` | "A2 -- Corroborated" badge in blue |
| Source provenance list | `source_list` | Row per source: MusicBrainz, Discogs, AcoustID, file metadata, artist input |
| Source confidence scores | `data_mono` | Per-source scores in monospace |
| Source color indicators | `source_indicator` | Color dots/squares per source identity |
| Sidebar | `navigation` | 60px fixed left sidebar |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Individual source scores | Aggregated confidence | arrow | "weighted aggregation" |
| Source count and agreement | Assurance level | arrow | "determines A0-A3" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "CONFIDENCE GAUGE" | Optional annotation arrow if annotations enabled | center-left |
| "SOURCE PROVENANCE" | Optional annotation arrow if annotations enabled | bottom-left |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "Work Detail + Confidence"
- Label 2: "Source Provenance Breakdown"
- Label 3: "Assurance Level A2"
- Label 4: "0.87 Confidence Score"

### Caption (for embedding in documentation)

The work detail view for "Hide and Seek" (0.87 confidence, A2 Corroborated) shows the ConfidenceGauge component with role="meter" accessibility, source-by-source provenance breakdown across MusicBrainz, Discogs, AcoustID, file metadata, and artist input, with per-source confidence scores.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `confidence_meter`, `source_list`, `badge_label` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. **This is a SCREENSHOT, not AI-generated.** Do NOT use Nano Banana Pro for this figure.
10. **Do NOT mock the screenshot** -- capture actual running frontend.
11. The ConfidenceGauge component uses `role="meter"` for accessibility (ARIA).
12. Sources shown: MusicBrainz, Discogs, AcoustID, file metadata, artist input. These are the five data source types in the scaffold.
13. Assurance levels: A0 (gray, "Unknown"), A1 (amber, "Claimed"), A2 (blue, "Corroborated"), A3 (green, "Verified").
14. Select a high-confidence work (like "Hide and Seek" at 0.87) for the best visual demonstration of the gauge.
15. Source color coding uses CSS vars: `--color-source-musicbrainz` (purple), `--color-source-discogs` (dark gray), `--color-source-acoustid` (teal), `--color-source-artist` (gold), `--color-source-file` (gray).

## Alt Text

Work detail screenshot: confidence gauge with source provenance and assurance breakdown

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "supplementary-03",
    "title": "Work Detail + Confidence Gauge",
    "audience": "L1",
    "layout_template": "A",
    "medium": "frontend_screenshot"
  },
  "content_architecture": {
    "primary_message": "The work detail view provides full attribution transparency with a visual confidence gauge, source-by-source provenance, and assurance level explanation.",
    "layout_flow": "top-to-bottom",
    "key_structures": [
      {
        "name": "Confidence Gauge",
        "role": "confidence_meter",
        "is_highlighted": true,
        "labels": ["0.87", "Green tier", "role=meter"]
      },
      {
        "name": "Assurance Badge",
        "role": "badge_label",
        "is_highlighted": true,
        "labels": ["A2", "Corroborated"]
      },
      {
        "name": "Source Provenance List",
        "role": "source_list",
        "is_highlighted": true,
        "labels": ["MusicBrainz", "Discogs", "AcoustID", "File Meta", "Artist Input"]
      }
    ],
    "relationships": [
      {
        "from": "Individual Sources",
        "to": "Aggregated Confidence",
        "type": "arrow",
        "label": "weighted aggregation"
      }
    ],
    "callout_boxes": []
  },
  "screenshot_spec": {
    "browser": "Chrome/headless",
    "viewport": "1440x900",
    "theme": "light",
    "url": "localhost:3000/works/[id]",
    "state": "work detail expanded, high-confidence work selected",
    "annotations": "optional callout arrows"
  }
}
```

## Quality Checklist

- [x] Primary message clear in one sentence
- [x] Semantic tags used (no colors, hex codes, or font names in content spec)
- [x] ASCII layout sketched
- [x] Screenshot specification defined (replaces spatial anchors)
- [x] Labels under 30 characters
- [x] Anti-hallucination rules listed (8 default + 7 figure-specific)
- [x] Alt text provided (125 chars max)
- [x] JSON export block included
- [x] Audience level correct (L1)
- [x] Layout template identified (A)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Frontend running and screenshot captured
- [ ] Quality reviewed
- [ ] Embedded in supplementary materials
