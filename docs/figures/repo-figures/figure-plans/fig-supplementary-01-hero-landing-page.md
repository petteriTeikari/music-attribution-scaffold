# fig-supplementary-01: Hero Landing Page

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-supplementary-01 |
| **Title** | Hero Landing Page |
| **Audience** | L1 (Music Industry Professional) |
| **Location** | Supplementary materials, docs/figures/repo-figures/ |
| **Priority** | P0 (Critical) |
| **Aspect Ratio** | 16:10 |
| **Layout Template** | A (Hero) |
| **Medium** | Frontend screenshot |

## Purpose

Shows the scaffold's landing page as it appears in the browser -- editorial typography, coral accent, warm cream background, sidebar navigation. Answers: "What does the actual running application look like?"

## Key Message

The music attribution scaffold presents a premium editorial interface -- not a generic SaaS dashboard -- with Instrument Serif headings, warm cream surfaces, and coral red accents.

## Visual Concept

Full browser screenshot at 1440x900px, light theme, showing the landing/home page with hero heading, sidebar navigation with rotated text, accent squares, and editorial layout.

```
+--+----------------------------------------------------------+
|  |                                                          |
|  |  MUSIC ATTRIBUTION                                       |
|S |  SCAFFOLD                                                |
|I |  ■                                                       |
|D |                                                          |
|E |  Open-source research infrastructure for                 |
|B |  transparent confidence scoring                          |
|A |                                                          |
|R |  ─────────────────────────────────                       |
|  |                                                          |
|  |  [Hero content area with editorial layout]               |
|  |                                                          |
|  |  Accent squares and horizontal dividers                  |
|  |                                                          |
+--+----------------------------------------------------------+
```

## Screenshot Specification

| Parameter | Value |
|-----------|-------|
| **Browser** | Chrome / headless Chromium |
| **Viewport** | 1440 x 900 px |
| **Theme** | Light |
| **URL** | `localhost:3000` |
| **State** | Default landing page, no modals, no sidebar open |
| **Annotations** | None (raw screenshot) |
| **Device pixel ratio** | 1x (standard) |
| **Font loading** | Wait for Instrument Serif + Plus Jakarta Sans + IBM Plex Mono to load |
| **Network** | All mock data available (no loading skeletons) |

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Fixed left sidebar | `navigation` | 60px wide sidebar with rotated text links, MA logo, role toggle |
| Hero heading | `heading_display` | Instrument Serif display heading, 48-96px |
| Cream background | `primary_background` | Warm cream surface (#f6f3e6 via --color-surface) |
| Coral accent elements | `accent_square` | 28x28px coral squares, accent lines |
| Body text | `body_text` | Plus Jakarta Sans, editorial layout |
| Noise grain overlay | `texture_overlay` | SVG feTurbulence at 0.035 opacity |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Sidebar navigation | Main content area | spatial | "margin-left: 60px" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| N/A | No callout annotations for raw screenshot | N/A |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "Hero Landing Page"
- Label 2: "Light Theme, 1440x900"

### Caption (for embedding in documentation)

The scaffold's landing page demonstrates the editorial design philosophy: Instrument Serif headings, warm cream surfaces, fixed sidebar navigation with rotated text, and coral red accent elements.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `navigation`, `heading_display`, `primary_background` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. **This is a SCREENSHOT, not AI-generated.** The frontend must be running at localhost:3000. Do NOT use Nano Banana Pro for this figure.
10. **Do NOT mock the screenshot** -- capture actual running frontend via headless Chromium or manual browser screenshot.
11. The sidebar is exactly 60px wide with rotated text (vertical-rl, rotate 180deg).
12. Cream background is `#f6f3e6` (CSS var `--color-surface`).
13. Heading font is Instrument Serif. Body font is Plus Jakarta Sans.
14. Accent color is coral `#E84C4F` (CSS var `--color-accent`).
15. Wait for all web fonts to load before capturing -- no FOUT (flash of unstyled text).

## Alt Text

Landing page screenshot: editorial typography with coral accents on warm cream background

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "supplementary-01",
    "title": "Hero Landing Page",
    "audience": "L1",
    "layout_template": "A",
    "medium": "frontend_screenshot"
  },
  "content_architecture": {
    "primary_message": "The music attribution scaffold presents a premium editorial interface with Instrument Serif headings, warm cream surfaces, and coral red accents.",
    "layout_flow": "top-to-bottom",
    "key_structures": [
      {
        "name": "Fixed Left Sidebar",
        "role": "navigation",
        "is_highlighted": false,
        "labels": ["MA logo", "Rotated nav links", "Role toggle"]
      },
      {
        "name": "Hero Heading",
        "role": "heading_display",
        "is_highlighted": true,
        "labels": ["Instrument Serif", "48-96px display"]
      },
      {
        "name": "Cream Background",
        "role": "primary_background",
        "is_highlighted": false,
        "labels": ["--color-surface"]
      }
    ],
    "relationships": [],
    "callout_boxes": []
  },
  "screenshot_spec": {
    "browser": "Chrome/headless",
    "viewport": "1440x900",
    "theme": "light",
    "url": "localhost:3000",
    "state": "default landing page",
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
