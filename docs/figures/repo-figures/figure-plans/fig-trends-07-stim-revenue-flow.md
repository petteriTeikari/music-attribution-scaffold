# fig-trends-07: Music Rights Revenue Flow: STIM Model

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-trends-07 |
| **Title** | Music Rights Revenue Flow: STIM Model |
| **Audience** | L1 (Music Industry Professional) |
| **Location** | docs/planning/tech-trends-agentic-infrastructure-2026.md, README.md |
| **Priority** | P0 (Critical) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | C (Flowchart) |

## Purpose

Shows the end-to-end revenue flow when an AI platform generates music: from generation, through confidence scoring, to STIM royalty calculation and payment to rights holders. This is for music industry professionals -- uses business language, no code or technical jargon. Answers: "How does AI-generated music translate into royalty payments for creators?"

## Key Message

When an AI platform generates music, the attribution scaffold scores training influence, STIM calculates per-output royalties based on confidence, and rights holders receive payment -- the world's first collective AI music licence.

## Visual Concept

Left-to-right flowchart with four stages: AI Platform, Attribution Scoring, STIM CMO, Rights Holders. Each stage uses business-friendly language. A callout highlights "world's first collective AI music licence."

```
+-----------------------------------------------------------------------+
|  MUSIC RIGHTS REVENUE FLOW                                             |
|  ■ The STIM Model                                                      |
+-----------------------------------------------------------------------+
|                                                                        |
|  ┌──────────┐     ┌──────────────┐     ┌──────────┐     ┌──────────┐ |
|  │          │     │              │     │          │     │          │ |
|  │  AI      │     │  Attribution │     │  STIM    │     │  Rights  │ |
|  │  Platform│────►│  Scoring     │────►│  CMO     │────►│  Holders │ |
|  │          │     │              │     │          │     │          │ |
|  │  Creates │     │  How sure    │     │ Calculates│    │  Receive │ |
|  │  music   │     │  are we?     │     │  royalty  │     │  payment │ |
|  │          │     │  0-100%      │     │  per      │     │          │ |
|  │          │     │              │     │  output   │     │  Song-   │ |
|  │          │     │              │     │          │     │  writers  │ |
|  │          │     │              │     │          │     │  Composers│ |
|  └──────────┘     └──────────────┘     └──────────┘     └──────────┘ |
|                                                                        |
|  ┌─────────────────────────────────────────────────────────────────┐  |
|  │  ■ World's first collective AI music licence (Sep 2025)         │  |
|  │    Technology partner: Sureel AI                                 │  |
|  │    Per-output royalty based on how sure the system is            │  |
|  └─────────────────────────────────────────────────────────────────┘  |
|                                                                        |
+-----------------------------------------------------------------------+
```

## Spatial Anchors

```yaml
canvas:
  width: 1920
  height: 1080
  background: primary_background

zones:
  - id: title_zone
    bounds: [0, 0, 1920, 120]
    content: "MUSIC RIGHTS REVENUE FLOW"
    role: title

  - id: flow_zone
    bounds: [80, 180, 1760, 500]
    content: "Revenue flow stages"
    role: content_area

  - id: callout_zone
    bounds: [80, 740, 1760, 180]
    content: "STIM callout"
    role: callout_box

anchors:
  - id: ai_platform
    position: [120, 280]
    size: [360, 320]
    role: stakeholder_platform

  - id: attribution_scoring
    position: [560, 280]
    size: [360, 320]
    role: solution_component

  - id: stim_cmo
    position: [1000, 280]
    size: [360, 320]
    role: solution_component

  - id: rights_holders
    position: [1440, 280]
    size: [360, 320]
    role: stakeholder_artist

  - id: flow_1
    from: ai_platform
    to: attribution_scoring
    type: arrow
    label: "generated music"

  - id: flow_2
    from: attribution_scoring
    to: stim_cmo
    type: arrow
    label: "confidence score"

  - id: flow_3
    from: stim_cmo
    to: rights_holders
    type: arrow
    label: "royalty payment"

  - id: stim_callout
    position: [120, 760]
    size: [1640, 140]
    role: callout_box
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| AI Platform | `stakeholder_platform` | Stage 1: creates music using AI |
| Attribution Scoring | `solution_component` | Stage 2: scores "how sure are we?" (0-100%) |
| STIM CMO | `solution_component` | Stage 3: calculates per-output royalty based on confidence |
| Rights Holders | `stakeholder_artist` | Stage 4: songwriters and composers receive payment |
| STIM callout | `callout_box` | World's first collective AI music licence, Sep 2025, Sureel AI partner |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| AI Platform | Attribution Scoring | arrow | "generated music" |
| Attribution Scoring | STIM CMO | arrow | "how sure (0-100%)" |
| STIM CMO | Rights Holders | arrow | "royalty payment" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "WORLD'S FIRST" | World's first collective AI music licence (Sep 2025). Technology partner: Sureel AI. Per-output royalty based on how sure the system is. | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "AI Platform"
- Label 2: "Creates music"
- Label 3: "Attribution Scoring"
- Label 4: "How sure are we?"
- Label 5: "0-100%"
- Label 6: "STIM"
- Label 7: "Calculates royalty"
- Label 8: "Per output"
- Label 9: "Rights Holders"
- Label 10: "Receive payment"
- Label 11: "Songwriters"
- Label 12: "Composers"

### Caption (for embedding in documentation)

STIM revenue flow: when AI generates music, the attribution scaffold scores training influence, STIM calculates per-output royalties, and rights holders receive payment under the world's first collective AI music licence.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `stakeholder_platform`, `solution_component`, `stakeholder_artist` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption. The editorial display title is allowed.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. STIM is the Swedish Performing Rights Society -- use "STIM" not the full Swedish name.
10. Launched the FIRST collective AI music licence in September 2025 -- this is a verified fact.
11. Technology partner: Sureel AI -- do NOT claim other companies are partners.
12. Per-output royalty is based on attribution confidence scores -- do NOT claim specific royalty amounts.
13. This is L1 audience -- use "credits" not "attribution records", "trust level" not "assurance tier", "how sure" not "confidence score."
14. Do NOT use code identifiers, database names, protocol acronyms, or API endpoints.
15. Do NOT claim specific royalty rates, revenue splits, or dollar amounts -- the model is per-output, details are not public.

## Alt Text

STIM revenue flow: AI output to confidence scoring to per-output royalty to rights holders

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "trends-07",
    "title": "Music Rights Revenue Flow: STIM Model",
    "audience": "L1",
    "layout_template": "C"
  },
  "content_architecture": {
    "primary_message": "AI platform generates music, scaffold scores confidence, STIM calculates royalty, rights holders get paid.",
    "layout_flow": "left-to-right",
    "key_structures": [
      {
        "name": "AI Platform",
        "role": "stakeholder_platform",
        "is_highlighted": false,
        "labels": ["Creates music"]
      },
      {
        "name": "Attribution Scoring",
        "role": "solution_component",
        "is_highlighted": true,
        "labels": ["How sure are we?", "0-100%"]
      },
      {
        "name": "STIM CMO",
        "role": "solution_component",
        "is_highlighted": true,
        "labels": ["Calculates royalty", "Per output"]
      },
      {
        "name": "Rights Holders",
        "role": "stakeholder_artist",
        "is_highlighted": false,
        "labels": ["Songwriters", "Composers", "Receive payment"]
      }
    ],
    "relationships": [
      {
        "from": "AI Platform",
        "to": "Attribution Scoring",
        "type": "arrow",
        "label": "generated music"
      },
      {
        "from": "Attribution Scoring",
        "to": "STIM CMO",
        "type": "arrow",
        "label": "how sure (0-100%)"
      },
      {
        "from": "STIM CMO",
        "to": "Rights Holders",
        "type": "arrow",
        "label": "royalty payment"
      }
    ],
    "callout_boxes": [
      {
        "heading": "WORLD'S FIRST",
        "body_text": "First collective AI music licence (Sep 2025). Technology partner: Sureel AI. Per-output royalty.",
        "position": "bottom-center"
      }
    ]
  }
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
- [x] Audience level correct (L1)
- [x] Layout template identified (C)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
