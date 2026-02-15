# fig-landscape-18: CMO Digital Transformation: Four Phases

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-landscape-18 |
| **Title** | CMO Digital Transformation: Four Phases |
| **Audience** | L2 (PhD/Policy) |
| **Location** | docs/planning/music-tech-landscape/, docs/planning/music-tech-figure-coverage-plan.md |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | E (Steps) |

## Purpose

This figure traces how collective management organizations are evolving through four distinct phases, each demanding progressively more sophisticated attribution infrastructure. It answers: "How are CMOs transforming to handle AI licensing, and what infrastructure does each phase require?"

## Key Message

Collective management organizations are transforming through four phases -- traditional blanket licensing, digital streaming, AI licensing (STIM pilot), and multi-CMO federation -- each requiring more attribution infrastructure.

## Visual Concept

Four ascending vertical steps arranged left-to-right, each representing a CMO evolution phase. Each step is taller than the previous, symbolizing increasing infrastructure complexity. Below each step, a bar shows the attribution infrastructure required. A coral accent line connects the steps. A callout highlights STIM's Sep 2025 pilot as the Phase III proof of concept.

```
+---------------------------------------------------------------+
|  CMO DIGITAL TRANSFORMATION                                    |
|  ■ Four Phases of Collective Licensing Evolution                |
+---------------------------------------------------------------+
|                                                                |
|                                              ┌──────────────┐  |
|                                              │  IV. MULTI-  │  |
|                               ┌──────────────│  CMO FEDERAT.│  |
|                               │  III. AI     │              │  |
|                ┌──────────────│  LICENSING    │  ASCAP+BMI+  │  |
|                │  II. DIGITAL │              │  PRS+GEMA+   │  |
| ┌──────────────│  STREAMING   │  STIM-Sureel │  SACEM coord │  |
| │  I. TRADTNL  │              │  pilot       │              │  |
| │  BLANKET     │  Per-stream  │  Attribution │  Global AI   │  |
| │              │  ISRC-based  │  opted-in    │  licensing    │  |
| │  Radio/TV    │  Spotify/    │  works only  │  coordinatd  │  |
| │  statistical │  Apple       │              │              │  |
| │  sampling    │              │  Sep 2025    │  Future      │  |
| └──────────────┘──────────────┘──────────────┘──────────────┘  |
|                                                                |
|  ATTRIBUTION INFRASTRUCTURE REQUIRED                            |
|  ═══════════════════════════════════════════════════════════    |
|  [  None  ] [  ISRC  ] [ Attrib. ] [ Federated Attribution ]   |
|  statistical  per-stream  per-model   cross-CMO harmonized     |
|                                                                |
|  ■ STIM's Sep 2025 pilot is Phase III's proof of concept       |
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
      text: "CMO DIGITAL TRANSFORMATION"
    - type: label_editorial
      text: "Four Phases of Collective Licensing Evolution"

step_i:
  position: [60, 160]
  width: 420
  height: 500
  label: "I. TRADITIONAL BLANKET"
  era: "Pre-digital"
  mechanism: "Radio/TV, statistical sampling, approximate distribution"
  attribution_infra: "None — statistical sampling only"

step_ii:
  position: [500, 160]
  width: 420
  height: 500
  label: "II. DIGITAL STREAMING"
  era: "2010s"
  mechanism: "Per-stream reporting, ISRC-based, Spotify/Apple"
  attribution_infra: "ISRC per-stream tracking"

step_iii:
  position: [940, 160]
  width: 420
  height: 500
  label: "III. AI LICENSING"
  era: "2025"
  mechanism: "STIM-Sureel pilot, attribution-based, opted-in works only"
  attribution_infra: "Per-model attribution analysis"

step_iv:
  position: [1380, 160]
  width: 420
  height: 500
  label: "IV. MULTI-CMO FEDERATION"
  era: "Future"
  mechanism: "ASCAP+BMI+PRS+GEMA+SACEM coordinating AI licensing globally"
  attribution_infra: "Federated cross-CMO attribution"

infra_bar:
  position: [60, 700]
  width: 1800
  height: 120
  elements:
    - type: label_editorial
      text: "ATTRIBUTION INFRASTRUCTURE REQUIRED"
    - type: data_mono
      segments:
        - { label: "None", phase: "I" }
        - { label: "ISRC", phase: "II" }
        - { label: "Attribution", phase: "III" }
        - { label: "Federated Attribution", phase: "IV" }

callout_stim:
  position: [60, 860]
  width: 1800
  height: 80
  elements:
    - type: callout_bar
      text: "STIM's Sep 2025 pilot is Phase III's proof of concept"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "CMO DIGITAL TRANSFORMATION" with coral accent square |
| Subtitle | `label_editorial` | "Four Phases of Collective Licensing Evolution" |
| Phase I step | `processing_stage` | Traditional blanket: radio/TV, statistical sampling |
| Phase II step | `processing_stage` | Digital streaming: per-stream, ISRC-based |
| Phase III step | `processing_stage` | AI licensing: STIM-Sureel pilot, attribution-based |
| Phase IV step | `processing_stage` | Multi-CMO federation: global AI licensing coordination |
| Infrastructure bar | `data_flow` | Progressive infrastructure requirements across phases |
| Roman numerals | `section_numeral` | I through IV phase headers |
| STIM callout | `callout_bar` | "STIM's Sep 2025 pilot is Phase III's proof of concept" |
| Step connectors | `data_flow` | Coral accent lines connecting ascending steps |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Phase I | Phase II | evolution | "Digitization enables per-stream" |
| Phase II | Phase III | evolution | "AI demands attribution" |
| Phase III | Phase IV | evolution | "Scale demands federation" |
| Infrastructure bar | All phases | dependency | "Each phase requires more infrastructure" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| STIM Pilot | "STIM's Sep 2025 pilot is Phase III's proof of concept" | Bottom full-width bar |
| Infrastructure Scale | "From statistical sampling to federated cross-CMO attribution" | Within infrastructure bar |

## Text Content

### Labels (Max 30 chars each)

- CMO DIGITAL TRANSFORMATION
- Four Phases of Evolution
- TRADITIONAL BLANKET
- DIGITAL STREAMING
- AI LICENSING
- MULTI-CMO FEDERATION
- Radio/TV sampling
- Per-stream ISRC-based
- STIM-Sureel pilot
- Global AI coordination
- Attribution Infra Required
- Statistical sampling
- Per-stream tracking
- Per-model attribution
- Federated attribution

### Caption (for embedding in documentation)

Collective management organizations are transforming through four phases: traditional blanket licensing (statistical sampling), digital streaming (ISRC per-stream), AI licensing (STIM-Sureel attribution pilot, Sep 2025), and future multi-CMO federation (ASCAP+BMI+PRS+GEMA+SACEM global coordination) -- each phase demanding progressively more sophisticated attribution infrastructure.

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

1. There are exactly FOUR phases -- do NOT add or remove any.
2. The phases are SEQUENTIAL evolution, not parallel alternatives.
3. STIM-Sureel is a real pilot (Sep 2025) -- do NOT describe as hypothetical.
4. Phase IV (Multi-CMO Federation) is FUTURE/aspirational -- do NOT describe as current.
5. CMO names (ASCAP, BMI, PRS, GEMA, SACEM) are real organizations -- do NOT invent others.
6. Do NOT conflate this with fig-trends-07 which shows the STIM flow for a single model.
7. The infrastructure bar must show PROGRESSIVE complexity, not equal weight per phase.
8. Do NOT imply Phase IV is inevitable -- it is a projected trajectory.

## Alt Text

Four ascending steps showing CMO evolution: traditional blanket, digital streaming, AI licensing, and multi-CMO federation.

## JSON Export Block

```json
{
  "id": "fig-landscape-18",
  "title": "CMO Digital Transformation: Four Phases",
  "audience": "L2",
  "priority": "P1",
  "layout": "E",
  "aspect_ratio": "16:9",
  "group": "landscape",
  "markov_phase": "Synthesize",
  "phases": [
    { "number": "I", "name": "Traditional Blanket", "era": "Pre-digital", "infra": "None", "example": "Radio/TV sampling" },
    { "number": "II", "name": "Digital Streaming", "era": "2010s", "infra": "ISRC per-stream", "example": "Spotify/Apple" },
    { "number": "III", "name": "AI Licensing", "era": "2025", "infra": "Per-model attribution", "example": "STIM-Sureel pilot" },
    { "number": "IV", "name": "Multi-CMO Federation", "era": "Future", "infra": "Federated cross-CMO", "example": "ASCAP+BMI+PRS+GEMA+SACEM" }
  ],
  "semantic_tags_used": [
    "heading_display", "label_editorial", "processing_stage", "data_flow",
    "section_numeral", "callout_bar", "data_mono"
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
