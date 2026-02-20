# fig-persona-13: User Modeling Spectrum

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-persona-13 |
| **Title** | User Modeling Spectrum: From No Modeling to Deep Behavioral Profiles |
| **Audience** | L2 (PhD Student / Policy Researcher) |
| **Location** | docs/knowledge-base/, docs/planning/ |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | E (Steps) |

## Purpose

Maps the full spectrum of user modeling approaches from zero personalization to deep behavioral profiling, showing data requirements, privacy cost, and personalization depth at each level. Marks the music attribution scaffold's current position (Proficiency Tiers) to ground the theoretical spectrum in a concrete design choice. Answers: "Where should a system sit on the user modeling spectrum, and why?"

## Key Message

Choose the minimum modeling depth that delivers value -- the music attribution scaffold uses Proficiency Tiers (Level 3 of 5), balancing meaningful personalization against minimal data requirements.

## Visual Concept

Five levels arranged left-to-right as ascending steps. Each step is a vertical column showing the modeling approach name, data requirements (low to extreme), privacy cost (none to high), and personalization depth (none to deep). The scaffold's current position at Level 3 is marked with a highlight. Below each column, a concrete example grounds the abstraction.

```
+-----------------------------------------------------------------------+
|  USER MODELING SPECTRUM                                                |
|  -- Five Levels of Personalization Depth                               |
+-----------------------------------------------------------------------+
|                                                                        |
|  DATA REQUIREMENTS                                                     |
|  ■ none    ■■ minimal    ■■■ moderate    ■■■■ high    ■■■■■ extreme   |
|                                                                        |
|                                                         ┌───────────┐ |
|                                           ┌───────────┐ │ 5. DEEP   │ |
|                            ┌────────────┐ │ 4. BEHAV- │ │ BEHAVIORAL│ |
|             ┌────────────┐ │ 3. PROFI-  │ │ IORAL     │ │ MODEL     │ |
|  ┌────────┐ │ 2. EXPLICIT│ │ CIENCY    │ │ PROFILING │ │           │ |
|  │ 1. NO  │ │ PREFER-   │ │ TIERS     │ │           │ │ Full      │ |
|  │ MODEL- │ │ ENCES     │ │           │ │ Clicks,   │ │ cognitive │ |
|  │ ING    │ │           │ │ Adaptive  │ │ dwell     │ │ model,    │ |
|  │        │ │ User-set  │ │ tooltips, │ │ times,    │ │ predict-  │ |
|  │ Same   │ │ options,  │ │ feature   │ │ scroll    │ │ ive       │ |
|  │ for    │ │ saved     │ │ gates,    │ │ patterns, │ │ intent    │ |
|  │ every- │ │ filters   │ │ role-     │ │ session   │ │ modeling  │ |
|  │ one    │ │           │ │ based UI  │ │ replay    │ │           │ |
|  │        │ │ Data: ■■  │ │           │ │           │ │ Data:     │ |
|  │ Data:  │ │ Privacy:  │ │ Data: ■■■ │ │ Data:■■■■ │ │ ■■■■■    │ |
|  │ ■      │ │ Low       │ │ Privacy:  │ │ Privacy:  │ │ Privacy:  │ |
|  │ Priv:  │ │ Depth:    │ │ Moderate  │ │ High      │ │ Extreme   │ |
|  │ None   │ │ Shallow   │ │ Depth:    │ │ Depth:    │ │ Depth:    │ |
|  │ Depth: │ │           │ │ Moderate  │ │ Deep      │ │ Deepest   │ |
|  │ None   │ │           │ │           │ │           │ │           │ |
|  └────────┘ └────────────┘ └─────┬──────┘ └───────────┘ └───────────┘ |
|                                  │                                     |
|                            ◆ SCAFFOLD                                  |
|                              POSITION                                  |
|                                                                        |
|  -- CHOOSE THE MINIMUM MODELING DEPTH THAT DELIVERS VALUE              |
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
    content: "USER MODELING SPECTRUM"
    role: title

  - id: legend_zone
    bounds: [80, 120, 1760, 60]
    content: "Data requirements legend"
    role: data_mono

  - id: steps_zone
    bounds: [80, 200, 1760, 680]
    content: "Five modeling levels"
    role: content_area

  - id: callout_zone
    bounds: [80, 940, 1760, 100]
    content: "CHOOSE THE MINIMUM MODELING DEPTH THAT DELIVERS VALUE"
    role: callout_box

anchors:
  - id: level_1
    position: [120, 560]
    size: [280, 300]
    role: processing_stage
    label: "No Modeling"

  - id: level_2
    position: [440, 460]
    size: [280, 400]
    role: processing_stage
    label: "Explicit Preferences"

  - id: level_3
    position: [760, 360]
    size: [280, 500]
    role: selected_option
    label: "Proficiency Tiers"

  - id: level_4
    position: [1080, 280]
    size: [280, 580]
    role: deferred_option
    label: "Behavioral Profiling"

  - id: level_5
    position: [1400, 220]
    size: [280, 640]
    role: deferred_option
    label: "Deep Behavioral Model"

  - id: scaffold_marker
    position: [840, 880]
    size: [120, 40]
    role: selected_option
    label: "SCAFFOLD POSITION"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Level 1: No Modeling | `processing_stage` | Same experience for all users, zero data collected |
| Level 2: Explicit Preferences | `processing_stage` | User-set options and saved filters, minimal data |
| Level 3: Proficiency Tiers | `selected_option` | Adaptive tooltips, feature gates, role-based UI -- scaffold's current position |
| Level 4: Behavioral Profiling | `deferred_option` | Click tracking, dwell times, scroll patterns, session replay |
| Level 5: Deep Behavioral Model | `deferred_option` | Full cognitive model, predictive intent modeling |
| Scaffold position marker | `selected_option` | Highlighted indicator at Level 3 |
| Data requirements legend | `data_mono` | Visual scale from none to extreme |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Level 1 | Level 2 | arrow | "add user control" |
| Level 2 | Level 3 | arrow | "add behavioral inference" |
| Level 3 | Level 4 | dashed | "diminishing returns" |
| Level 4 | Level 5 | dashed | "extreme data cost" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "DESIGN PRINCIPLE" | "CHOOSE THE MINIMUM MODELING DEPTH THAT DELIVERS VALUE" | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "1. NO MODELING"
- Label 2: "2. EXPLICIT PREFERENCES"
- Label 3: "3. PROFICIENCY TIERS"
- Label 4: "4. BEHAVIORAL PROFILING"
- Label 5: "5. DEEP BEHAVIORAL MODEL"
- Label 6: "Data: none to extreme"
- Label 7: "Privacy: none to high"
- Label 8: "Depth: none to deepest"
- Label 9: "SCAFFOLD POSITION"

### Caption (for embedding in documentation)

Five levels of user modeling depth from zero personalization to deep behavioral profiling, with the music attribution scaffold positioned at Level 3 (Proficiency Tiers) -- choosing the minimum modeling depth that delivers meaningful adaptive UI value.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `processing_stage`, `selected_option`, `deferred_option` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption. The editorial display title is allowed.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. The scaffold uses Proficiency Tiers (Level 3) implemented via Jotai atoms and localStorage. Do NOT claim it uses behavioral tracking.
10. The five levels are a spectrum, not discrete categories -- teams may sit between levels.
11. Level 3 is the scaffold's CURRENT position, not a universal recommendation. Do NOT imply all projects should use Level 3.
12. "Diminishing returns" between Levels 3-4 is a design judgment, not a proven metric. Do NOT present specific ROI numbers.
13. The scaffold marker must be visually prominent -- it is the key grounding element that connects theory to practice.

## Alt Text

Stepped diagram of user modeling spectrum with five personalization depth levels from no modeling to deep behavioral profiling, with the music attribution scaffold positioned at Level 3 (Proficiency Tiers) balancing adaptive UI against minimal data requirements.

## Image Embed

![Stepped diagram of user modeling spectrum with five personalization depth levels from no modeling to deep behavioral profiling, with the music attribution scaffold positioned at Level 3 (Proficiency Tiers) balancing adaptive UI against minimal data requirements.](docs/figures/repo-figures/assets/fig-persona-13-user-modeling-spectrum.jpg)

*Five levels of user modeling depth from zero personalization to deep behavioral profiling, with the music attribution scaffold positioned at Level 3 (Proficiency Tiers) -- choosing the minimum modeling depth that delivers meaningful adaptive UI value.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "persona-13",
    "title": "User Modeling Spectrum: From No Modeling to Deep Behavioral Profiles",
    "audience": "L2",
    "layout_template": "E"
  },
  "content_architecture": {
    "primary_message": "Choose the minimum modeling depth that delivers value -- the scaffold uses Proficiency Tiers (Level 3 of 5).",
    "layout_flow": "left-to-right",
    "key_structures": [
      {
        "name": "Level 1: No Modeling",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["1. NO MODELING", "Data: none", "Same for everyone"]
      },
      {
        "name": "Level 2: Explicit Preferences",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["2. EXPLICIT PREFERENCES", "Data: minimal", "User-set options"]
      },
      {
        "name": "Level 3: Proficiency Tiers",
        "role": "selected_option",
        "is_highlighted": true,
        "labels": ["3. PROFICIENCY TIERS", "Data: moderate", "SCAFFOLD POSITION"]
      },
      {
        "name": "Level 4: Behavioral Profiling",
        "role": "deferred_option",
        "is_highlighted": false,
        "labels": ["4. BEHAVIORAL PROFILING", "Data: high", "Click tracking"]
      },
      {
        "name": "Level 5: Deep Behavioral Model",
        "role": "deferred_option",
        "is_highlighted": false,
        "labels": ["5. DEEP BEHAVIORAL MODEL", "Data: extreme", "Predictive intent"]
      }
    ],
    "relationships": [
      {
        "from": "Level 1",
        "to": "Level 3",
        "type": "arrow",
        "label": "increasing personalization depth"
      },
      {
        "from": "Level 3",
        "to": "Level 5",
        "type": "dashed",
        "label": "diminishing returns, increasing privacy cost"
      }
    ],
    "callout_boxes": [
      {
        "heading": "DESIGN PRINCIPLE",
        "body_text": "CHOOSE THE MINIMUM MODELING DEPTH THAT DELIVERS VALUE",
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
- [x] Audience level correct (L2)
- [x] Layout template identified (E)

## Status

- [x] Draft created
- [ ] Content reviewed
- [x] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
