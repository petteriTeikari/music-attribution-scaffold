# fig-landscape-07: Same Landscape, Four Perspectives: Misaligned Incentives

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-landscape-07 |
| **Title** | Same Landscape, Four Perspectives: Misaligned Incentives |
| **Audience** | L1 (Music Industry) |
| **Location** | docs/planning/music-tech-landscape/, docs/planning/music-tech-figure-coverage-plan.md |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | B (Multi-Panel) |

## Purpose

This figure reveals the structural misalignment between four key stakeholder groups in music attribution. Each stakeholder wants something fundamentally different, and these wants are not merely politically difficult to reconcile but structurally incompatible. It answers: "Why can't stakeholders just agree on attribution -- what specifically is misaligned?"

## Key Message

Artists want per-song credit, labels want catalog protection, platforms want blanket licenses, regulators want transparency -- these are structurally misaligned, not just politically difficult.

## Visual Concept

Four equal-sized panels in a 2x2 grid, each representing one stakeholder perspective. Each panel contains the stakeholder name, their top 3 wants, and their primary concern. A center element (where the four panels meet) shows the conflict/alignment zones. The center element is a small diamond or intersection marker showing which wants conflict and which align.

```
+---------------------------------------------------------------+
|  SAME LANDSCAPE, FOUR PERSPECTIVES                             |
|  ■ Misaligned Incentives                                       |
+-------------------------------+-------------------------------+
|                               |                               |
|  I. ARTIST                    |  II. LABEL                    |
|  ──────                       |  ─────                        |
|                               |                               |
|  WANTS:                       |  WANTS:                       |
|  ■ Per-song credit            |  ■ Catalog-level licensing    |
|  ■ Fair per-stream royalty    |  ■ Bulk licensing deals       |
|  ■ Voice protection           |  ■ Competitive moat           |
|                               |                               |
|  FEARS:                       |  FEARS:                       |
|  Replacement by AI            |  Catalog devaluation          |
|                               |                               |
+───────────────┬───────────────+───────────────────────────────+
|               │  CONFLICTS    │                               |
|               │  ■ Granularity│                               |
|               │  ■ Revenue    │                               |
|               │  ■ Control    │                               |
|               │               │                               |
|               │  ALIGNS ON    │                               |
|               │  ○ Provenance │                               |
|               │  ○ Enforcement│                               |
+───────────────┴───────────────+───────────────────────────────+
|                               |                               |
|  III. PLATFORM                |  IV. REGULATOR                |
|  ────────                     |  ─────────                    |
|                               |                               |
|  WANTS:                       |  WANTS:                       |
|  ■ Blanket license            |  ■ Transparency               |
|  ■ Minimal compliance cost    |  ■ Auditability               |
|  ■ User growth                |  ■ Consumer protection        |
|                               |                               |
|  FEARS:                       |  FEARS:                       |
|  Litigation exposure          |  Unregulable technology       |
|                               |                               |
+-------------------------------+-------------------------------+
```

## Spatial Anchors

```yaml
canvas:
  width: 1920
  height: 1080
  background: warm_cream

title_block:
  position: [60, 40]
  width: 1800
  height: 80
  elements:
    - type: heading_display
      text: "SAME LANDSCAPE, FOUR PERSPECTIVES"
    - type: label_editorial
      text: "Misaligned Incentives"

panel_artist:
  position: [60, 140]
  width: 860
  height: 380
  label: "I. ARTIST"
  wants:
    - "Per-song credit"
    - "Fair per-stream royalty"
    - "Voice protection"
  fears: "Replacement by AI"

panel_label:
  position: [960, 140]
  width: 860
  height: 380
  label: "II. LABEL"
  wants:
    - "Catalog-level licensing"
    - "Bulk licensing deals"
    - "Competitive moat"
  fears: "Catalog devaluation"

center_element:
  position: [760, 400]
  width: 400
  height: 280
  conflicts:
    - "Granularity (per-song vs catalog)"
    - "Revenue (per-stream vs bulk)"
    - "Control (individual vs institutional)"
  alignments:
    - "Provenance matters"
    - "Enforcement needed"

panel_platform:
  position: [60, 560]
  width: 860
  height: 380
  label: "III. PLATFORM"
  wants:
    - "Blanket license"
    - "Minimal compliance cost"
    - "User growth"
  fears: "Litigation exposure"

panel_regulator:
  position: [960, 560]
  width: 860
  height: 380
  label: "IV. REGULATOR"
  wants:
    - "Transparency"
    - "Auditability"
    - "Consumer protection"
  fears: "Unregulable technology"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "SAME LANDSCAPE, FOUR PERSPECTIVES" with coral accent square |
| Subtitle | `label_editorial` | "Misaligned Incentives" |
| Artist panel | `stakeholder_artist` | Top-left: per-song credit, fair royalty, voice protection |
| Label panel | `stakeholder_label` | Top-right: catalog licensing, bulk deals, competitive moat |
| Platform panel | `stakeholder_platform` | Bottom-left: blanket license, minimal compliance, user growth |
| Regulator panel | `processing_stage` | Bottom-right: transparency, auditability, consumer protection |
| Want items | `label_editorial` | Three wants per stakeholder with accent square bullets |
| Fear items | `problem_statement` | One primary fear per stakeholder |
| Center conflict zone | `decision_point` | Diamond/intersection showing conflicts and alignments |
| Conflict labels | `problem_statement` | "Granularity", "Revenue", "Control" |
| Alignment labels | `solution_component` | "Provenance", "Enforcement" |
| Panel dividers | `callout_bar` | Coral accent lines between panels |
| Roman numerals | `section_numeral` | I, II, III, IV for each panel |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Artist (per-song) | Label (catalog-level) | conflict | "Granularity mismatch" |
| Artist (fair royalty) | Platform (blanket license) | conflict | "Revenue model clash" |
| Label (competitive moat) | Platform (user growth) | conflict | "Control tension" |
| Artist | Regulator | partial_align | "Both want transparency" |
| Label | Regulator | partial_align | "Both want enforcement" |
| Platform | Regulator | tension | "Compliance cost vs requirements" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| Conflicts | "Granularity, Revenue, Control" | Center element |
| Alignments | "Provenance, Enforcement" | Center element |
| Artist fears | "Replacement by AI" | Bottom of artist panel |
| Label fears | "Catalog devaluation" | Bottom of label panel |
| Platform fears | "Litigation exposure" | Bottom of platform panel |
| Regulator fears | "Unregulable technology" | Bottom of regulator panel |

## Text Content

### Labels (Max 30 chars each)

- FOUR PERSPECTIVES
- Misaligned Incentives
- ARTIST
- LABEL
- PLATFORM
- REGULATOR
- Per-song credit
- Fair per-stream royalty
- Voice protection
- Catalog-level licensing
- Bulk licensing deals
- Competitive moat
- Blanket license
- Minimal compliance cost
- User growth
- Transparency
- Auditability
- Consumer protection
- CONFLICTS
- ALIGNS ON
- Granularity
- Revenue
- Control
- Provenance
- Enforcement

### Caption (for embedding in documentation)

Four stakeholder perspectives on music AI attribution reveal structural misalignment: artists want per-song credit and voice protection, labels want catalog-level licensing and competitive moats, platforms want blanket licenses and minimal compliance, and regulators want transparency and auditability. They conflict on granularity, revenue models, and control -- but align on the need for provenance and enforcement.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- do NOT render them as labels.
2. **Semantic tags are INTERNAL** -- do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- do NOT render them.
4. **Background MUST be warm cream (#f6f3e6)**.
5. **No generic flowchart aesthetics** -- no thick block arrows, no PowerPoint look.
6. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or numbered caption.
7. **No prompt leakage** -- do NOT render style keywords as visible text.

### Figure-Specific Rules

1. There are exactly 4 stakeholders: Artist, Label, Platform, Regulator -- do NOT add others (e.g., no "fans", "publishers", "PROs").
2. Each stakeholder has exactly 3 wants and 1 fear -- do NOT add or remove items.
3. The misalignment is STRUCTURAL, not just political -- do NOT imply it can be solved by "better communication."
4. Do NOT name specific artists, labels, platforms, or regulatory bodies.
5. The center element shows BOTH conflicts and alignments -- this is not a purely adversarial picture.
6. "Voice protection" refers to voice cloning protection, not vocal health.
7. "Blanket license" is a specific music licensing term -- do NOT substitute with generic language.
8. Fears are stated neutrally -- do NOT editorialize about whether fears are justified.

## Alt Text

Four stakeholder panels showing artists, labels, platforms, and regulators with conflicting attribution wants.

## JSON Export Block

```json
{
  "id": "fig-landscape-07",
  "title": "Same Landscape, Four Perspectives: Misaligned Incentives",
  "audience": "L1",
  "priority": "P1",
  "layout": "B",
  "aspect_ratio": "16:9",
  "group": "landscape",
  "markov_phase": "Explain",
  "stakeholders": [
    {
      "name": "Artist",
      "wants": ["Per-song credit", "Fair per-stream royalty", "Voice protection"],
      "fears": "Replacement by AI"
    },
    {
      "name": "Label",
      "wants": ["Catalog-level licensing", "Bulk licensing deals", "Competitive moat"],
      "fears": "Catalog devaluation"
    },
    {
      "name": "Platform",
      "wants": ["Blanket license", "Minimal compliance cost", "User growth"],
      "fears": "Litigation exposure"
    },
    {
      "name": "Regulator",
      "wants": ["Transparency", "Auditability", "Consumer protection"],
      "fears": "Unregulable technology"
    }
  ],
  "conflicts": ["Granularity", "Revenue", "Control"],
  "alignments": ["Provenance", "Enforcement"],
  "semantic_tags_used": [
    "heading_display", "label_editorial", "stakeholder_artist", "stakeholder_label",
    "stakeholder_platform", "decision_point", "problem_statement", "solution_component",
    "callout_bar", "section_numeral"
  ]
}
```

## Quality Checklist

- [x] Primary message clear in one sentence
- [x] Semantic tags used (no colors, hex codes, or font names in content spec)
- [x] ASCII layout sketched
- [x] Spatial anchors defined in YAML
- [x] Labels under 30 characters
- [x] Anti-hallucination rules listed
- [x] Alt text provided (125 chars max)
- [x] JSON export block included
- [x] Audience level correct (L1/L2/L3/L4)
- [x] Layout template identified (A/B/C/D/E)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25
- [ ] Embedded in documentation
