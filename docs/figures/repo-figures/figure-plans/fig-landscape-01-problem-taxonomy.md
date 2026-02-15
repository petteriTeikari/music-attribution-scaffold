# fig-landscape-01: Music AI Problem Taxonomy: 12 Categories

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-landscape-01 |
| **Title** | Music AI Problem Taxonomy: 12 Categories |
| **Audience** | L2 (PhD/Policy) |
| **Location** | docs/planning/music-tech-landscape/, docs/planning/music-tech-figure-coverage-plan.md |
| **Priority** | P0 (Critical) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | B (Multi-Panel) |

## Purpose

This figure establishes that "music AI" is not a single field but 12 distinct problem categories, each with different technical requirements, maturity levels, and investment profiles. It answers: "What are all the different problems people mean when they say music AI?"

## Key Message

Music AI is 12 distinct problem categories, not one field -- each requires different approaches and carries different investment risk.

## Visual Concept

A 4x3 multi-panel grid where each cell represents one problem category. Each cell contains the category name, a maturity indicator (nascent/growing/mature), and a problem-type tag (generative/analytical/infrastructure). A coral accent line separates the grid into quadrants for visual grouping. The grid reads left-to-right, top-to-bottom, progressing from generative problems through analytical to infrastructure.

```
+---------------------------------------------------------------+
|  MUSIC AI PROBLEM TAXONOMY                                     |
|  ■ 12 Distinct Categories, Not One Field                       |
+---------------------------------------------------------------+
|                               |                                |
|  I. GENERATIVE                |  II. ANALYTICAL                |
|  ─────────────────            |  ──────────────                |
|                               |                                |
|  ┌──────────┐ ┌──────────┐   |  ┌──────────┐ ┌──────────┐    |
|  │ Content  │ │ Voice    │   |  │ Audio    │ │ Quality  │    |
|  │ Generatn │ │ Cloning  │   |  │ Detectn  │ │ Assessmt │    |
|  │ ■ mature │ │ ■ growing│   |  │ ■ mature │ │ ■ nascent│    |
|  └──────────┘ └──────────┘   |  └──────────┘ └──────────┘    |
|                               |                                |
|  ┌──────────┐ ┌──────────┐   |  ┌──────────┐ ┌──────────┐    |
|  │ Recommen-│ │ Music    │   |  │ Attrib./ │ │ Content  │    |
|  │ dation   │ │ Understdg│   |  │ Provennce│ │ ID       │    |
|  │ ■ mature │ │ ■ growing│   |  │ ■ nascent│ │ ■ mature │    |
|  └──────────┘ └──────────┘   |  └──────────┘ └──────────┘    |
|                               |                                |
+---------------------------------------------------------------+
|  III. INFRASTRUCTURE                                           |
|  ──────────────────                                            |
|                                                                |
|  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐         |
|  │ Rights   │ │ Metadata │ │ Licensing│ │ Royalty  │         |
|  │ Managemt │ │ Standard.│ │ Infra    │ │ Distrib. │         |
|  │ ■ growing│ │ ■ growing│ │ ■ nascent│ │ ■ mature │         |
|  └──────────┘ └──────────┘ └──────────┘ └──────────┘         |
|                                                                |
+---------------------------------------------------------------+
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
      text: "MUSIC AI PROBLEM TAXONOMY"
    - type: label_editorial
      text: "12 Distinct Categories, Not One Field"

quadrant_generative:
  position: [60, 140]
  width: 880
  height: 400
  label: "I. GENERATIVE"
  cells:
    - { name: "Content Generation", maturity: "mature", x: 0, y: 0 }
    - { name: "Voice Cloning", maturity: "growing", x: 1, y: 0 }
    - { name: "Recommendation", maturity: "mature", x: 0, y: 1 }
    - { name: "Music Understanding", maturity: "growing", x: 1, y: 1 }

quadrant_analytical:
  position: [960, 140]
  width: 880
  height: 400
  label: "II. ANALYTICAL"
  cells:
    - { name: "Audio Detection", maturity: "mature", x: 0, y: 0 }
    - { name: "Quality Assessment", maturity: "nascent", x: 1, y: 0 }
    - { name: "Attribution/Provenance", maturity: "nascent", x: 0, y: 1 }
    - { name: "Content ID", maturity: "mature", x: 1, y: 1 }

row_infrastructure:
  position: [60, 580]
  width: 1800
  height: 280
  label: "III. INFRASTRUCTURE"
  cells:
    - { name: "Rights Management", maturity: "growing", x: 0, y: 0 }
    - { name: "Metadata Standardization", maturity: "growing", x: 1, y: 0 }
    - { name: "Licensing Infrastructure", maturity: "nascent", x: 2, y: 0 }
    - { name: "Royalty Distribution", maturity: "mature", x: 3, y: 0 }
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "MUSIC AI PROBLEM TAXONOMY" with coral accent square |
| Subtitle | `label_editorial` | "12 Distinct Categories, Not One Field" |
| Generative quadrant | `processing_stage` | Top-left: content generation, voice cloning, recommendation, music understanding |
| Analytical quadrant | `processing_stage` | Top-right: audio detection, quality assessment, attribution/provenance, content ID |
| Infrastructure row | `storage_layer` | Bottom: rights management, metadata standardization, licensing infra, royalty distribution |
| Category cells | `solution_component` | 12 individual cells with name and maturity badge |
| Maturity badges | `badge_label` | nascent/growing/mature indicator per cell |
| Quadrant labels | `section_numeral` | Roman numerals I, II, III for each grouping |
| Quadrant dividers | `callout_bar` | Coral accent lines separating groupings |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Generative quadrant | Analytical quadrant | conceptual | "Creates need for" |
| Analytical quadrant | Infrastructure row | dependency | "Requires" |
| Content Generation | Attribution/Provenance | tension | "Generation growth increases attribution urgency" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| Maturity Legend | nascent / growing / mature with color coding | Bottom-right corner |
| Key Insight | "Each category requires fundamentally different technical approaches" | Below infrastructure row |

## Text Content

### Labels (Max 30 chars each)

- Content Generation
- Voice Cloning
- Audio Detection
- Quality Assessment
- Recommendation
- Music Understanding
- Attribution/Provenance
- Content ID
- Rights Management
- Metadata Standardization
- Licensing Infrastructure
- Royalty Distribution
- GENERATIVE
- ANALYTICAL
- INFRASTRUCTURE

### Caption (for embedding in documentation)

Music AI spans 12 distinct problem categories grouped into generative (content creation, voice cloning, recommendation, music understanding), analytical (audio detection, quality assessment, attribution/provenance, content ID), and infrastructure (rights management, metadata standardization, licensing, royalty distribution) -- each with different maturity levels and investment profiles.

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

1. There are exactly 12 categories -- do NOT add or remove any.
2. Categories are PROBLEM TYPES, not companies -- do NOT name specific companies.
3. Maturity labels are exactly three levels: nascent, growing, mature -- no other scale.
4. The grouping into Generative/Analytical/Infrastructure is conceptual, not a strict taxonomy -- some categories span boundaries.
5. Do NOT imply that any single solution addresses all 12 categories.
6. Do NOT rank categories by importance -- the point is that they are DIFFERENT, not hierarchical.

## Alt Text

12-category music AI taxonomy grid: generative, analytical, and infrastructure problems each with maturity levels.

## JSON Export Block

```json
{
  "id": "fig-landscape-01",
  "title": "Music AI Problem Taxonomy: 12 Categories",
  "audience": "L2",
  "priority": "P0",
  "layout": "B",
  "aspect_ratio": "16:9",
  "group": "landscape",
  "markov_phase": "Explain",
  "categories": [
    { "name": "Content Generation", "group": "generative", "maturity": "mature" },
    { "name": "Voice Cloning", "group": "generative", "maturity": "growing" },
    { "name": "Recommendation", "group": "generative", "maturity": "mature" },
    { "name": "Music Understanding", "group": "generative", "maturity": "growing" },
    { "name": "Audio Detection", "group": "analytical", "maturity": "mature" },
    { "name": "Quality Assessment", "group": "analytical", "maturity": "nascent" },
    { "name": "Attribution/Provenance", "group": "analytical", "maturity": "nascent" },
    { "name": "Content ID", "group": "analytical", "maturity": "mature" },
    { "name": "Rights Management", "group": "infrastructure", "maturity": "growing" },
    { "name": "Metadata Standardization", "group": "infrastructure", "maturity": "growing" },
    { "name": "Licensing Infrastructure", "group": "infrastructure", "maturity": "nascent" },
    { "name": "Royalty Distribution", "group": "infrastructure", "maturity": "mature" }
  ],
  "semantic_tags_used": [
    "heading_display", "label_editorial", "processing_stage", "storage_layer",
    "solution_component", "badge_label", "section_numeral", "callout_bar"
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
