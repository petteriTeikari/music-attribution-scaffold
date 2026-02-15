# fig-ecosystem-15: Company Node Activation Matrix

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-ecosystem-15 |
| **Title** | Company Node Activation Matrix |
| **Audience** | L2 (PhD/Policy) |
| **Location** | docs/prd/decisions/REPORT.md, docs/planning/ |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | B (Multi-Panel) |

## Purpose

Shows how 6 company nodes in the PRD activate conditionally based on the `partnership_model` selection, with "none" (P=0.40) as the highest-probability outcome leaving all company nodes deactivated. Answers: "Which partnerships activate under which model, and why is 'no partnership' the default?"

## Key Message

6 company nodes activate conditionally based on partnership_model selection -- with "none" (P=0.40) as highest-probability option, only 2-4 companies activate per partnership archetype.

## Visual Concept

Matrix/table layout with partnership model options as rows and company nodes as columns. Cells are marked active (filled square) or inactive (empty). The "none" row is visually distinct (highlighted) as the default. A bottom callout explains the strategic rationale for high "none" priors.

```
+---------------------------------------------------------------+
|  COMPANY NODE ACTIVATION MATRIX                                |
|  -- Partnership Model Determines Activation                    |
+---------------------------------------------------------------+
|                                                                |
|                   COMPANY NODES                                |
|           ┌──────┬──────┬──────┬──────┬──────┬──────┐        |
|           │Music │Sureel│ STIM │Sound │Fairly│ Suno │        |
|           │ AI   │  AI  │ CMO  │Exch. │Train │/Udio │        |
|  P'SHIP   │Part. │Part. │Pilot │Reg.  │Cert. │Lic.  │        |
|  MODEL    ├──────┼──────┼──────┼──────┼──────┼──────┤        |
|  ─────────│      │      │      │      │      │      │        |
|           │      │      │      │      │      │      │        |
|  ■ NONE   │  --  │  --  │  --  │  --  │  --  │  --  │        |
|  P=0.40   │      │      │      │      │      │      │        |
|           ├──────┼──────┼──────┼──────┼──────┼──────┤        |
|  API      │  ■   │  ■   │  --  │  --  │  --  │  ■   │        |
|  MARKET   │      │      │      │      │      │      │        |
|  P=0.25   │      │      │      │      │      │      │        |
|           ├──────┼──────┼──────┼──────┼──────┼──────┤        |
|  STRATEGIC│  ■   │  --  │  --  │  ■   │  ■   │  --  │        |
|  ALLIANCE │      │      │      │      │      │      │        |
|  P=0.20   │      │      │      │      │      │      │        |
|           ├──────┼──────┼──────┼──────┼──────┼──────┤        |
|  CMO      │  --  │  --  │  ■   │  ■   │  ■   │  ■   │        |
|  FEDER.   │      │      │      │      │      │      │        |
|  P=0.15   │      │      │      │      │      │      │        |
|           └──────┴──────┴──────┴──────┴──────┴──────┘        |
|                                                                |
+---------------------------------------------------------------+
|  "none" leaves all 6 deactivated -- honest uncertainty,        |
|  not disinterest. Only 2-4 companies activate per archetype.   |
+---------------------------------------------------------------+
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
    content: "COMPANY NODE ACTIVATION MATRIX"
    role: title

  - id: matrix_zone
    bounds: [80, 150, 1760, 720]
    role: content_area

  - id: callout_zone
    bounds: [80, 900, 1760, 120]
    role: callout_box

anchors:
  - id: row_none
    position: [960, 300]
    size: [1600, 100]
    role: selected_option
    label: "NONE (P=0.40)"

  - id: row_api
    position: [960, 430]
    size: [1600, 100]
    role: deferred_option
    label: "API MARKETPLACE (P=0.25)"

  - id: row_strategic
    position: [960, 560]
    size: [1600, 100]
    role: deferred_option
    label: "STRATEGIC ALLIANCE (P=0.20)"

  - id: row_cmo
    position: [960, 690]
    size: [1600, 100]
    role: deferred_option
    label: "CMO FEDERATION (P=0.15)"

  - id: col_musical_ai
    position: [420, 200]
    size: [200, 60]
    role: decision_point
    label: "Musical AI"

  - id: col_sureel
    position: [640, 200]
    size: [200, 60]
    role: decision_point
    label: "Sureel AI"

  - id: col_stim
    position: [860, 200]
    size: [200, 60]
    role: decision_point
    label: "STIM CMO"

  - id: col_soundexchange
    position: [1080, 200]
    size: [200, 60]
    role: decision_point
    label: "SoundExchange"

  - id: col_fairly
    position: [1300, 200]
    size: [200, 60]
    role: decision_point
    label: "Fairly Trained"

  - id: col_suno_udio
    position: [1520, 200]
    size: [200, 60]
    role: decision_point
    label: "Suno/Udio"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "COMPANY NODE ACTIVATION MATRIX" with coral accent square |
| None row (highlighted) | `selected_option` | P=0.40, all 6 companies inactive, default state |
| API Marketplace row | `deferred_option` | P=0.25, activates Musical AI, Sureel AI, Suno/Udio |
| Strategic Alliance row | `deferred_option` | P=0.20, activates Musical AI, SoundExchange, Fairly Trained |
| CMO Federation row | `deferred_option` | P=0.15, activates STIM, SoundExchange, Fairly Trained, Suno/Udio |
| Column headers | `decision_point` | 6 company nodes as column headers |
| Active cells | `confidence_high` | Filled square indicating activation |
| Inactive cells | `assurance_a0` | Dash indicating no activation |
| Bottom callout | `callout_bar` | Explains "none" as honest uncertainty |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| partnership_model | musical_ai_partnership | dashed | "conditional activation" |
| partnership_model | sureel_ai_partnership | dashed | "conditional activation" |
| partnership_model | stim_cmo_pilot | dashed | "conditional activation" |
| partnership_model | soundexchange_registry | dashed | "conditional activation" |
| partnership_model | fairly_trained_certification | dashed | "conditional activation" |
| partnership_model | suno_udio_licensing | dashed | "conditional activation" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "DEFAULT: NONE" | P=0.40 -- honest uncertainty, not disinterest. No partnerships assumed until materialized. | bottom-center |
| "ACTIVATION RANGE" | Only 2-4 companies activate per partnership archetype -- never all 6 simultaneously | right-margin |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "NONE (P=0.40)"
- Label 2: "API MARKETPLACE (P=0.25)"
- Label 3: "STRATEGIC ALLIANCE (P=0.20)"
- Label 4: "CMO FEDERATION (P=0.15)"
- Label 5: "Musical AI Partnership"
- Label 6: "Sureel AI Partnership"
- Label 7: "STIM CMO Pilot"
- Label 8: "SoundExchange Registry"
- Label 9: "Fairly Trained Cert."
- Label 10: "Suno/Udio Licensing"

### Caption (for embedding in documentation)

Company node activation matrix showing how 6 ecosystem company nodes activate conditionally based on partnership_model selection -- "none" (P=0.40) as default leaves all deactivated, while api_marketplace, strategic_alliance, and cmo_federation each activate 2-4 companies.

## Anti-Hallucination Rules

These are INTERNAL instructions for prompt construction. They MUST NEVER appear as visible text in the generated image.

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `selected_option`, `deferred_option`, `decision_point` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. `partnership_model` options: `none` (P=0.40), `api_marketplace` (P=0.25), `strategic_alliance` (P=0.20), `cmo_federation` (P=0.15).
10. Company nodes: `musical_ai_partnership`, `sureel_ai_partnership`, `stim_cmo_pilot`, `soundexchange_registry`, `fairly_trained_certification`, `suno_udio_licensing`.
11. All company nodes have high "none" priors (0.40-0.55) -- this encodes honest uncertainty.
12. Activation is conditional, not guaranteed -- partnership model selection creates the possibility, not certainty.
13. The "none" row must be visually highlighted as the default/highest-probability option.
14. Do NOT imply any partnership currently exists -- all are potential future states.
15. The matrix shows which companies WOULD activate, not which HAVE activated.
16. Never show all 6 companies activating simultaneously -- max 4 per partnership archetype.

## Alt Text

Company node activation matrix: partnership model determines which 6 companies engage

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "ecosystem-15",
    "title": "Company Node Activation Matrix",
    "audience": "L2",
    "layout_template": "B"
  },
  "content_architecture": {
    "primary_message": "6 company nodes activate conditionally based on partnership_model selection -- with 'none' (P=0.40) as highest-probability option, only 2-4 companies activate per partnership archetype.",
    "layout_flow": "top-to-bottom",
    "key_structures": [
      {
        "name": "None Row",
        "role": "selected_option",
        "is_highlighted": true,
        "labels": ["NONE (P=0.40)", "All inactive"]
      },
      {
        "name": "API Marketplace Row",
        "role": "deferred_option",
        "is_highlighted": false,
        "labels": ["API MARKETPLACE (P=0.25)"]
      },
      {
        "name": "Strategic Alliance Row",
        "role": "deferred_option",
        "is_highlighted": false,
        "labels": ["STRATEGIC ALLIANCE (P=0.20)"]
      },
      {
        "name": "CMO Federation Row",
        "role": "deferred_option",
        "is_highlighted": false,
        "labels": ["CMO FEDERATION (P=0.15)"]
      }
    ],
    "relationships": [
      {
        "from": "partnership_model",
        "to": "musical_ai_partnership",
        "type": "dashed",
        "label": "conditional activation"
      },
      {
        "from": "partnership_model",
        "to": "sureel_ai_partnership",
        "type": "dashed",
        "label": "conditional activation"
      },
      {
        "from": "partnership_model",
        "to": "stim_cmo_pilot",
        "type": "dashed",
        "label": "conditional activation"
      },
      {
        "from": "partnership_model",
        "to": "soundexchange_registry",
        "type": "dashed",
        "label": "conditional activation"
      },
      {
        "from": "partnership_model",
        "to": "fairly_trained_certification",
        "type": "dashed",
        "label": "conditional activation"
      },
      {
        "from": "partnership_model",
        "to": "suno_udio_licensing",
        "type": "dashed",
        "label": "conditional activation"
      }
    ],
    "callout_boxes": [
      {
        "heading": "DEFAULT: NONE",
        "body_text": "P=0.40 -- honest uncertainty, not disinterest",
        "position": "bottom-center"
      },
      {
        "heading": "ACTIVATION RANGE",
        "body_text": "Only 2-4 companies activate per partnership archetype",
        "position": "right-margin"
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
- [x] Anti-hallucination rules listed (8 default + 8 figure-specific)
- [x] Alt text provided (125 chars max)
- [x] JSON export block included
- [x] Audience level correct (L2)
- [x] Layout template identified (B)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
