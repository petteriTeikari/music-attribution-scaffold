# fig-landscape-21: 25 Years of MIR: How Research Became Infrastructure

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-landscape-21 |
| **Title** | 25 Years of MIR: How Research Became Infrastructure |
| **Audience** | L2 (PhD/Policy) |
| **Location** | docs/planning/music-tech-landscape/, docs/planning/music-tech-figure-coverage-plan.md |
| **Priority** | P0 (Critical) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | C (Flowchart) |

## Purpose

This figure traces 25 years of Music Information Retrieval research showing how academic foundations became commercial infrastructure, while exposing the "citation gap" -- commercial companies build on MIR but rarely cite or fund the research that enables them. It answers: "Where did the technical foundations of music AI actually come from, and who is (not) acknowledging this?"

## Key Message

Every commercial attribution tool stands on 25 years of MIR research (librosa, CLAP, Chromaprint) -- yet companies rarely cite or fund the academic research that enables them.

## Visual Concept

A horizontal timeline flowing left to right across five eras (2000-2025), with academic milestones above the timeline and commercial applications below. Vertical dependency lines connect academic foundations to the commercial products that rely on them. A coral accent "citation gap" zone highlights the disconnect between academic origins and commercial use. The bottom callout references the 25-year MIR survey (2025).

```
+---------------------------------------------------------------+
|  25 YEARS OF MIR                                               |
|  ■ How Research Became Infrastructure                          |
+---------------------------------------------------------------+
|                                                                |
|  ACADEMIC FOUNDATIONS (above timeline)                          |
|                                                                |
|  ISMIR        librosa     Chromaprint   VGGish     CLAP        |
|  founded      essentia    AcoustID      OpenL3     AudioLDM    |
|  ○            madmom      ○             ○          ○           |
|  │            ○           │             │          │           |
|  │            │           │             │          │           |
|  ════════╤════════╤═══════════╤══════════════╤═══════════╤═══  |
|  2000    │ 2005   │ 2010      │ 2015         │ 2020      │2025 |
|  ════════╧════════╧═══════════╧══════════════╧═══════════╧═══  |
|                   │           │             │          │        |
|                   │           │             │          │        |
|                   ▼           ▼             ▼          ▼        |
|              ┌────────┐  ┌────────┐   ┌────────┐ ┌────────┐   |
|              │Shazam  │  │Content │   │ Suno   │ │Musical │   |
|              │Spotify │  │ID sys  │   │ Udio   │ │AI,     │   |
|              │recoms  │  │        │   │        │ │Sureel  │   |
|              └────────┘  └────────┘   └────────┘ └────────┘   |
|                                                                |
|  COMMERCIAL APPLICATIONS (below timeline)                       |
|                                                                |
|  ┌──────────────────────────────────────────────────────────┐  |
|  │  ■ THE CITATION GAP                                      │  |
|  │    Companies build on MIR but rarely cite or fund it      │  |
|  └──────────────────────────────────────────────────────────┘  |
|                                                                |
|  ref: 25-year MIR survey (2025)                                |
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
      text: "25 YEARS OF MIR"
    - type: label_editorial
      text: "How Research Became Infrastructure"

academic_row:
  position: [60, 140]
  width: 1800
  height: 280
  label: "ACADEMIC FOUNDATIONS"
  milestones:
    - { year: 2000, name: "ISMIR founded", type: "conference", x: 60 }
    - { year: 2005, name: "librosa", type: "library", x: 380 }
    - { year: 2006, name: "essentia", type: "library", x: 420 }
    - { year: 2007, name: "madmom", type: "library", x: 460 }
    - { year: 2010, name: "Chromaprint", type: "fingerprinting", x: 700 }
    - { year: 2011, name: "AcoustID", type: "infrastructure", x: 740 }
    - { year: 2017, name: "VGGish", type: "deep_learning", x: 1060 }
    - { year: 2019, name: "OpenL3", type: "embeddings", x: 1140 }
    - { year: 2023, name: "CLAP", type: "multimodal", x: 1420 }
    - { year: 2023, name: "AudioLDM", type: "generative", x: 1500 }

timeline:
  position: [60, 430]
  width: 1800
  height: 40
  markers: [2000, 2005, 2010, 2015, 2020, 2025]

commercial_row:
  position: [60, 480]
  width: 1800
  height: 280
  label: "COMMERCIAL APPLICATIONS"
  applications:
    - { era: "2005-2010", names: ["Shazam", "Spotify recommendations"], depends_on: ["librosa", "essentia"] }
    - { era: "2010-2015", names: ["Content ID systems", "fingerprint-based licensing"], depends_on: ["Chromaprint", "AcoustID"] }
    - { era: "2015-2020", names: ["Suno", "Udio", "AI generation platforms"], depends_on: ["VGGish", "OpenL3"] }
    - { era: "2020-2025", names: ["Musical AI", "Sureel", "attribution tools"], depends_on: ["CLAP", "AudioLDM"] }

dependency_lines:
  position: [60, 140]
  width: 1800
  height: 620
  connections:
    - { from: "librosa", to: "Spotify", style: "dashed" }
    - { from: "Chromaprint", to: "Content ID", style: "dashed" }
    - { from: "VGGish", to: "Suno", style: "dashed" }
    - { from: "CLAP", to: "Musical AI", style: "dashed" }

citation_gap:
  position: [60, 800]
  width: 1800
  height: 120
  elements:
    - type: callout_bar
      text: "THE CITATION GAP"
    - type: label_editorial
      text: "Companies build on MIR but rarely cite or fund it"

reference:
  position: [60, 960]
  width: 1800
  height: 60
  elements:
    - type: data_mono
      text: "ref: 25-year MIR survey (2025)"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "25 YEARS OF MIR" with coral accent square |
| Subtitle | `label_editorial` | "How Research Became Infrastructure" |
| Academic row | `processing_stage` | Milestones: ISMIR, librosa, essentia, Chromaprint, VGGish, CLAP |
| Timeline | `data_flow` | Horizontal axis: 2000 to 2025 with era markers |
| Commercial row | `stakeholder_platform` | Products: Shazam, Spotify, Content ID, Suno, Musical AI |
| Dependency lines | `data_flow` | Dashed vertical lines connecting academic to commercial |
| ISMIR milestone | `solution_component` | 2000: conference founding, community formation |
| librosa/essentia/madmom | `solution_component` | 2005-2007: foundational MIR libraries |
| Chromaprint/AcoustID | `solution_component` | 2010-2011: fingerprinting infrastructure |
| VGGish/OpenL3 | `solution_component` | 2017-2019: deep learning enters MIR |
| CLAP/AudioLDM | `solution_component` | 2023: multimodal and generative models |
| Citation gap callout | `problem_statement` | "Companies build on MIR but rarely cite or fund it" |
| Survey reference | `data_mono` | 25-year MIR survey (2025) |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| ISMIR (2000) | librosa (2005) | enables | "Community spawns tools" |
| librosa | Spotify recommendations | dependency | "Foundation for audio analysis" |
| Chromaprint | Content ID systems | dependency | "Fingerprinting enables identification" |
| VGGish/OpenL3 | Suno/Udio | dependency | "Embeddings enable generation" |
| CLAP | Musical AI/Sureel | dependency | "Multimodal enables attribution" |
| Academic foundations | Commercial applications | citation_gap | "Built on but rarely cited" |
| All commercial | Citation gap | reveals | "Structural acknowledgment deficit" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| Citation Gap | "Companies build on MIR but rarely cite or fund the academic research that enables them" | Below commercial row |
| Survey Reference | "25-year MIR survey (2025)" | Bottom-left |
| Foundational Era | "2005-2010: The libraries that power everything" | Above academic row, left cluster |

## Text Content

### Labels (Max 30 chars each)

- 25 YEARS OF MIR
- How Research Became Infra
- ACADEMIC FOUNDATIONS
- COMMERCIAL APPLICATIONS
- ISMIR founded
- librosa
- essentia
- madmom
- Chromaprint
- AcoustID
- VGGish
- OpenL3
- CLAP
- AudioLDM
- Shazam
- Spotify recommendations
- Content ID systems
- Suno
- Udio
- Musical AI
- Sureel
- THE CITATION GAP
- Rarely cited or funded

### Caption (for embedding in documentation)

Twenty-five years of Music Information Retrieval: academic milestones from ISMIR (2000) through librosa/essentia (2005-2007), Chromaprint/AcoustID (2010-2011), VGGish/OpenL3 (2017-2019), to CLAP/AudioLDM (2023) -- each enabling commercial products from Shazam to Suno to Musical AI. The "citation gap" reveals that companies rarely cite or fund the academic research that enables them.

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

1. All named tools (librosa, essentia, Chromaprint, etc.) are REAL open-source projects -- do NOT invent others.
2. ISMIR was founded in 2000 -- do NOT use a different year.
3. Dependency lines between academic and commercial are ILLUSTRATIVE, not exhaustive -- do NOT claim direct causal chains.
4. The "citation gap" is a STRUCTURAL observation, not an accusation against specific companies.
5. VGGish is from Google (2017), OpenL3 is from NYU (2019) -- do NOT conflate origins.
6. CLAP is a multimodal audio-language model -- do NOT describe as a fingerprinting tool.
7. Timeline spans 2000-2025 -- do NOT extend beyond or truncate.
8. Do NOT imply that MIR research has stopped -- it is ONGOING, and the commercial dependency continues.
9. The 25-year MIR survey reference is to a real publication -- do NOT alter the reference.
10. Approximate founding years are acceptable -- do NOT claim day-level precision for library releases.

## Alt Text

Timeline from 2000-2025 showing MIR milestones above and commercial products below, with citation gap highlighted.

## JSON Export Block

```json
{
  "id": "fig-landscape-21",
  "title": "25 Years of MIR: How Research Became Infrastructure",
  "audience": "L2",
  "priority": "P0",
  "layout": "C",
  "aspect_ratio": "16:9",
  "group": "landscape",
  "markov_phase": "Synthesize",
  "novelty": 4,
  "eras": [
    { "period": "2000-2005", "academic": ["ISMIR"], "commercial": [] },
    { "period": "2005-2010", "academic": ["librosa", "essentia", "madmom"], "commercial": ["Shazam", "Spotify"] },
    { "period": "2010-2015", "academic": ["Chromaprint", "AcoustID"], "commercial": ["Content ID systems"] },
    { "period": "2015-2020", "academic": ["VGGish", "OpenL3"], "commercial": ["Suno", "Udio"] },
    { "period": "2020-2025", "academic": ["CLAP", "AudioLDM"], "commercial": ["Musical AI", "Sureel"] }
  ],
  "key_insight": "citation_gap",
  "reference": "25-year MIR survey (2025)",
  "semantic_tags_used": [
    "heading_display", "label_editorial", "processing_stage", "data_flow",
    "stakeholder_platform", "solution_component", "problem_statement", "data_mono"
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
