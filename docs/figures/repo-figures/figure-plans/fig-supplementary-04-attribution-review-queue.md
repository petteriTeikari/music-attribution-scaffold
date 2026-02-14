# fig-supplementary-04: Attribution Review Queue

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-supplementary-04 |
| **Title** | Attribution Review Queue |
| **Audience** | L1 (Music Industry Professional) |
| **Location** | Supplementary materials, docs/figures/repo-figures/ |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:10 |
| **Layout Template** | A (Hero) |
| **Medium** | Frontend screenshot |

## Purpose

Shows the attribution review queue where AI suggestions appear as diffs for batch approval. Answers: "How does the scaffold reduce the friction of reviewing and approving attribution corrections?"

## Key Message

The review queue is the key friction reducer -- AI suggestions appear as before/after diffs with "Approve All" for batch acceptance and progress counter showing momentum.

## Visual Concept

Full browser screenshot of the review queue page showing pending attribution suggestions as diff-style rows with before/after values, batch approve controls, and a progress counter.

```
+--+----------------------------------------------------------+
|  |  ATTRIBUTION REVIEW                                       |
|S |  ■ 5 pending · 3 approved                                 |
|I |                                                           |
|D |  [Approve All]                          Progress: 3/8     |
|E |                                                           |
|B |  ─────────────────────────────────────────────────        |
|A |  Hide and Seek                                            |
|R |  Composer:  - Unknown        + Imogen Heap     [Approve]  |
|  |  ISRC:      - (missing)      + GBUM70603001    [Approve]  |
|  |  ─────────────────────────────────────────────────        |
|  |  Goodnight and Go                                         |
|  |  Publisher: - Sony/ATV       + Megaphonic      [Approve]  |
|  |  ─────────────────────────────────────────────────        |
|  |  Just for Now                                             |
|  |  Writer:    - I. Heap        + Imogen Heap     [Approve]  |
|  |  ─────────────────────────────────────────────────        |
|  |                                                           |
+--+----------------------------------------------------------+
```

## Screenshot Specification

| Parameter | Value |
|-----------|-------|
| **Browser** | Chrome / headless Chromium |
| **Viewport** | 1440 x 900 px |
| **Theme** | Light |
| **URL** | `localhost:3000/review` (or `/attributions` if review is a tab) |
| **State** | Review queue with pending suggestions visible, some approved |
| **Annotations** | Optional -- callout on batch approve button |
| **Device pixel ratio** | 1x (standard) |
| **Font loading** | Wait for all three font families to load |
| **Network** | Mock data loaded, no loading skeletons visible |
| **Scroll position** | Top of page |
| **Note** | If review queue is partially implemented in MVP, capture whatever state exists and note in status |

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Page heading | `heading_display` | "ATTRIBUTION REVIEW" in Instrument Serif |
| Progress counter | `data_mono` | "3/8" or similar showing review momentum |
| Batch approve button | `action_primary` | "Approve All" button for batch acceptance |
| Diff rows | `content_row` | Before/after values for each suggested change |
| Before value | `diff_removed` | Old/missing value shown with removal indicator |
| After value | `diff_added` | New/suggested value shown with addition indicator |
| Per-item approve | `action_secondary` | Individual "Approve" button per suggestion |
| Work title grouping | `label_primary` | Work name grouping related field changes |
| Divider lines | `accent_line` | Horizontal dividers between work groups |
| Sidebar | `navigation` | 60px fixed left sidebar |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| AI suggestion | Diff row | arrow | "surfaces as before/after" |
| Approve action | Progress counter | arrow | "increments on acceptance" |
| Batch approve | All pending items | arrow | "approves all at once" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "BATCH APPROVAL" | Optional annotation on the "Approve All" control | top-right |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "Attribution Review Queue"
- Label 2: "Before/After Diffs"
- Label 3: "Batch Approve"
- Label 4: "Progress Counter"

### Caption (for embedding in documentation)

The attribution review queue surfaces AI suggestions as before/after diffs grouped by work, with individual and batch approval controls and a progress counter showing review momentum -- designed as the key friction reducer per the UX-first philosophy.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `diff_removed`, `diff_added`, `action_primary` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. **This is a SCREENSHOT, not AI-generated.** Do NOT use Nano Banana Pro for this figure.
10. **Do NOT mock the screenshot** -- capture actual running frontend.
11. The review queue MAY be partially implemented in MVP. If the full queue UI is not yet built, document the actual state captured and note it in the Status section.
12. AI suggestions show as diffs (before/after). "Approve All" enables batch acceptance. Progress counter shows review momentum. Smart sorting by review priority. Tab between fields like a spreadsheet. These requirements are from `.claude/rules/11-ux-first-philosophy.md` "Attribution Workflow" section.
13. Diff indicators: removal (dash/red) for old value, addition (plus/green) for new value.
14. Field types shown in diffs: Composer, ISRC, Publisher, Writer, and other attribution metadata fields.

## Alt Text

Review queue screenshot: AI attribution suggestions as diffs with batch approval controls

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "supplementary-04",
    "title": "Attribution Review Queue",
    "audience": "L1",
    "layout_template": "A",
    "medium": "frontend_screenshot"
  },
  "content_architecture": {
    "primary_message": "The review queue reduces friction with before/after diffs, batch approval, and progress momentum tracking.",
    "layout_flow": "top-to-bottom",
    "key_structures": [
      {
        "name": "Diff Rows",
        "role": "content_row",
        "is_highlighted": true,
        "labels": ["Before/after values", "Per-field changes"]
      },
      {
        "name": "Batch Approve",
        "role": "action_primary",
        "is_highlighted": true,
        "labels": ["Approve All"]
      },
      {
        "name": "Progress Counter",
        "role": "data_mono",
        "is_highlighted": true,
        "labels": ["3/8 reviewed"]
      }
    ],
    "relationships": [
      {
        "from": "AI Suggestion",
        "to": "Diff Row",
        "type": "arrow",
        "label": "surfaces as before/after"
      },
      {
        "from": "Approve Action",
        "to": "Progress Counter",
        "type": "arrow",
        "label": "increments on acceptance"
      }
    ],
    "callout_boxes": []
  },
  "screenshot_spec": {
    "browser": "Chrome/headless",
    "viewport": "1440x900",
    "theme": "light",
    "url": "localhost:3000/review",
    "state": "review queue with pending suggestions",
    "annotations": "optional callout on batch approve"
  }
}
```

## Quality Checklist

- [x] Primary message clear in one sentence
- [x] Semantic tags used (no colors, hex codes, or font names in content spec)
- [x] ASCII layout sketched
- [x] Screenshot specification defined (replaces spatial anchors)
- [x] Labels under 30 characters
- [x] Anti-hallucination rules listed (8 default + 6 figure-specific)
- [x] Alt text provided (125 chars max)
- [x] JSON export block included
- [x] Audience level correct (L1)
- [x] Layout template identified (A)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Frontend running and screenshot captured (note: review queue may be partially implemented)
- [ ] Quality reviewed
- [ ] Embedded in supplementary materials
