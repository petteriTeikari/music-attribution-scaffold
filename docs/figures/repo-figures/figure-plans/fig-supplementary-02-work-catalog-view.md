# fig-supplementary-02: Work Catalog View

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-supplementary-02 |
| **Title** | Work Catalog View |
| **Audience** | L1 (Music Industry Professional) |
| **Location** | Supplementary materials, docs/figures/repo-figures/ |
| **Priority** | P0 (Critical) |
| **Aspect Ratio** | 16:10 |
| **Layout Template** | A (Hero) |
| **Medium** | Frontend screenshot |

## Purpose

Shows the works catalog page with Imogen Heap mock data -- horizontal rows with dividers, confidence indicators, assurance badges. Answers: "How does the scaffold display a collection of music works with their attribution status?"

## Key Message

The work catalog displays 8 Imogen Heap works with confidence indicators and assurance badges in a horizontal row layout -- not card-based -- with editorial typography.

## Visual Concept

Full browser screenshot showing the /works page with all 8 mock works visible in a horizontal row layout with dividers, confidence scores in monospace, and assurance level badges color-coded A0-A3.

```
+--+----------------------------------------------------------+
|  |  WORKS CATALOG                                            |
|S |  ■ 8 works                                                |
|I |                                                           |
|D |  ─────────────────────────────────────────────────        |
|E |  Hide and Seek          Imogen Heap   0.87  [A2]         |
|B |  ─────────────────────────────────────────────────        |
|A |  Goodnight and Go       Imogen Heap   0.72  [A1]         |
|R |  ─────────────────────────────────────────────────        |
|  |  Headlock               Imogen Heap   0.95  [A3]         |
|  |  ─────────────────────────────────────────────────        |
|  |  Just for Now           Imogen Heap   0.45  [A0]         |
|  |  ─────────────────────────────────────────────────        |
|  |  [... 4 more works ...]                                   |
|  |                                                           |
+--+----------------------------------------------------------+
```

## Screenshot Specification

| Parameter | Value |
|-----------|-------|
| **Browser** | Chrome / headless Chromium |
| **Viewport** | 1440 x 900 px |
| **Theme** | Light |
| **URL** | `localhost:3000/works` |
| **State** | Catalog loaded with all 8 mock works visible, no filters active |
| **Annotations** | None (raw screenshot) |
| **Device pixel ratio** | 1x (standard) |
| **Font loading** | Wait for all three font families to load |
| **Network** | Mock data loaded, no loading skeletons visible |
| **Scroll position** | Top of page (all 8 works should be visible without scrolling if possible) |

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Page heading | `heading_display` | "WORKS CATALOG" or similar in Instrument Serif |
| Work rows | `content_row` | Horizontal rows with divider lines between each work |
| Work title | `label_primary` | Work title in body font |
| Artist name | `label_secondary` | "Imogen Heap" for all 8 works |
| Confidence score | `data_mono` | Numeric 0.00-0.95 in IBM Plex Mono, color-coded by tier |
| Assurance badge | `badge_label` | A0/A1/A2/A3 badge, color-coded per assurance level |
| Divider lines | `accent_line` | Horizontal dividers between rows (not shadow-box cards) |
| Sidebar | `navigation` | 60px fixed left sidebar |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Work row | Work detail page | click | "navigate to /works/[id]" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| N/A | No callout annotations for raw screenshot | N/A |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "Work Catalog View"
- Label 2: "8 Imogen Heap Mock Works"
- Label 3: "Confidence 0.0-0.95"
- Label 4: "Assurance A0-A3"

### Caption (for embedding in documentation)

The work catalog displays Imogen Heap mock data in horizontal rows with confidence scores (green >= 0.85, amber 0.50-0.84, red < 0.50) and assurance level badges (A0-A3), demonstrating the editorial row layout with dividers rather than card-based design.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `content_row`, `data_mono`, `badge_label` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. **This is a SCREENSHOT, not AI-generated.** Do NOT use Nano Banana Pro for this figure.
10. **Do NOT mock the screenshot** -- capture actual running frontend at localhost:3000/works.
11. The catalog shows exactly 8 Imogen Heap mock works spanning confidence 0.0-0.95.
12. Layout uses horizontal rows with dividers (NOT shadow-box cards). This is a deliberate design choice per `.claude/rules/10-frontend-design-system.md`.
13. Each row shows: work title, artist name, confidence score, assurance level badge (A0-A3).
14. Confidence colors: green >= 0.85, amber 0.50-0.84, red < 0.50 (CSS vars `--color-confidence-high`, `--color-confidence-medium`, `--color-confidence-low`).
15. Assurance badge colors: A3 green, A2 blue, A1 amber, A0 gray.

## Alt Text

Work catalog screenshot: 8 Imogen Heap works with confidence and assurance indicators

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "supplementary-02",
    "title": "Work Catalog View",
    "audience": "L1",
    "layout_template": "A",
    "medium": "frontend_screenshot"
  },
  "content_architecture": {
    "primary_message": "The work catalog displays 8 Imogen Heap works with confidence indicators and assurance badges in a horizontal row layout with editorial typography.",
    "layout_flow": "top-to-bottom",
    "key_structures": [
      {
        "name": "Work Rows",
        "role": "content_row",
        "is_highlighted": true,
        "labels": ["8 rows with dividers", "Not card-based"]
      },
      {
        "name": "Confidence Scores",
        "role": "data_mono",
        "is_highlighted": true,
        "labels": ["0.0-0.95 range", "Color-coded by tier"]
      },
      {
        "name": "Assurance Badges",
        "role": "badge_label",
        "is_highlighted": true,
        "labels": ["A0 through A3", "Color-coded"]
      }
    ],
    "relationships": [],
    "callout_boxes": []
  },
  "screenshot_spec": {
    "browser": "Chrome/headless",
    "viewport": "1440x900",
    "theme": "light",
    "url": "localhost:3000/works",
    "state": "catalog loaded, all 8 works visible",
    "annotations": "none"
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
