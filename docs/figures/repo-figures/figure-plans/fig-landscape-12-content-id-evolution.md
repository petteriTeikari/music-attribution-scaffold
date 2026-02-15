# fig-landscape-12: Content ID Evolution: From Shazam to AI Detection

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-landscape-12 |
| **Title** | Content ID Evolution: From Shazam to AI Detection |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/planning/music-tech-landscape/, docs/planning/music-tech-figure-coverage-plan.md |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | E (Steps) |

## Purpose

Traces four generations of content identification technology, showing how each generation was developed to address the specific failures of its predecessor. Answers: "Why isn't Shazam-style fingerprinting enough for AI-era attribution, and what came after?"

## Key Message

Four generations of content identification -- fingerprinting, watermarking, embedding, AI detection -- each addressing the failures of the prior generation.

## Visual Concept

Vertical stepped layout with four generations descending from top to bottom. Each step is a horizontal band showing the generation name, key technology, what it solved, and what it still cannot do. Accent squares mark each generation number. Vertical connecting lines between steps show the "failure that motivated the next generation" relationship. The visual progression communicates evolution, not replacement -- all four generations coexist.

```
+-----------------------------------------------------------------------+
|  CONTENT ID EVOLUTION                                                  |
|  ■ From Shazam to AI Detection                                         |
+-----------------------------------------------------------------------+
|                                                                        |
|  ■ GEN 1: AUDIO FINGERPRINTING                                        |
|  ┌─────────────────────────────────────────────────────────────┐      |
|  │ Shazam / Chromaprint / AcoustID                              │      |
|  │ Exact matching of spectral fingerprints                      │      |
|  │ SOLVED: Identifying known recordings from short clips        │      |
|  │ FAILS:  Any transformation (remix, cover, AI generation)     │      |
|  └──────────────────────────┬──────────────────────────────────┘      |
|                              │ Fails on transforms                    |
|                              ▼                                         |
|  ■ GEN 2: WATERMARKING                                                |
|  ┌─────────────────────────────────────────────────────────────┐      |
|  │ AudioSeal / SynthID Audio / WavMark                          │      |
|  │ Embedded signal survives some transformations                │      |
|  │ SOLVED: Survives compression, noise, format conversion       │      |
|  │ FAILS:  Model-based attacks, neural regeneration             │      |
|  └──────────────────────────┬──────────────────────────────────┘      |
|                              │ Fails on model attacks                 |
|                              ▼                                         |
|  ■ GEN 3: EMBEDDING SIMILARITY                                        |
|  ┌─────────────────────────────────────────────────────────────┐      |
|  │ CLAP / CLMR / audio embeddings                               │      |
|  │ Learned representations handle style transfer                │      |
|  │ SOLVED: Handles style transfer, arrangement changes          │      |
|  │ FAILS:  Cannot prove causation (correlation only)            │      |
|  └──────────────────────────┬──────────────────────────────────┘      |
|                              │ Cannot prove causation                 |
|                              ▼                                         |
|  ■ GEN 4: AI DETECTION                                                |
|  ┌─────────────────────────────────────────────────────────────┐      |
|  │ Afchar et al. ICASSP 2025 / classifier-based detection       │      |
|  │ Binary: is this AI-generated?                                │      |
|  │ SOLVED: 99.8% accuracy on clean samples                      │      |
|  │ FAILS:  Poor robustness to post-processing                   │      |
|  └─────────────────────────────────────────────────────────────┘      |
|                                                                        |
|  ■ All four coexist -- no generation replaces the prior ones           |
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
    bounds: [0, 0, 1920, 100]
    content: "CONTENT ID EVOLUTION"
    role: title

  - id: subtitle_zone
    bounds: [0, 100, 1920, 40]
    content: "From Shazam to AI Detection"
    role: subtitle

  - id: gen1_band
    bounds: [120, 160, 1680, 180]
    role: content_area
    label: "GEN 1: AUDIO FINGERPRINTING"

  - id: gen1_to_gen2
    bounds: [940, 340, 40, 50]
    role: data_flow
    label: "Fails on transforms"

  - id: gen2_band
    bounds: [120, 390, 1680, 180]
    role: content_area
    label: "GEN 2: WATERMARKING"

  - id: gen2_to_gen3
    bounds: [940, 570, 40, 50]
    role: data_flow
    label: "Fails on model attacks"

  - id: gen3_band
    bounds: [120, 620, 1680, 180]
    role: content_area
    label: "GEN 3: EMBEDDING SIMILARITY"

  - id: gen3_to_gen4
    bounds: [940, 800, 40, 50]
    role: data_flow
    label: "Cannot prove causation"

  - id: gen4_band
    bounds: [120, 850, 1680, 180]
    role: content_area
    label: "GEN 4: AI DETECTION"

  - id: footer_callout
    bounds: [60, 1040, 1800, 40]
    role: callout_bar
    label: "All four coexist -- no generation replaces the prior ones"

anchors:
  - id: shazam
    position: [160, 200]
    size: [400, 100]
    role: processing_stage
    label: "Shazam / Chromaprint"

  - id: audioseal_gen2
    position: [160, 430]
    size: [400, 100]
    role: processing_stage
    label: "AudioSeal / SynthID Audio"

  - id: clap_gen3
    position: [160, 660]
    size: [400, 100]
    role: processing_stage
    label: "CLAP / CLMR"

  - id: afchar_gen4
    position: [160, 890]
    size: [400, 100]
    role: processing_stage
    label: "Afchar et al. ICASSP 2025"

  - id: solved_col
    position: [600, 180]
    size: [500, 40]
    role: label_editorial
    label: "SOLVED"

  - id: fails_col
    position: [1140, 180]
    size: [500, 40]
    role: label_editorial
    label: "STILL FAILS"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "CONTENT ID EVOLUTION" in editorial caps with accent square |
| Subtitle | `label_editorial` | "From Shazam to AI Detection" |
| Gen 1 band | `processing_stage` | Audio fingerprinting: Shazam, Chromaprint, AcoustID -- exact matching |
| Gen 2 band | `processing_stage` | Watermarking: AudioSeal, SynthID Audio, WavMark -- embedded signals |
| Gen 3 band | `processing_stage` | Embedding similarity: CLAP, CLMR -- learned representations |
| Gen 4 band | `processing_stage` | AI detection: Afchar et al. ICASSP 2025 -- binary classification |
| Gen 1 solved | `confidence_high` | Identifying known recordings from short clips |
| Gen 1 fails | `confidence_low` | Any transformation breaks matching |
| Gen 2 solved | `confidence_high` | Survives compression, noise, format conversion |
| Gen 2 fails | `confidence_low` | Model-based attacks, neural regeneration |
| Gen 3 solved | `confidence_high` | Handles style transfer, arrangement changes |
| Gen 3 fails | `confidence_low` | Cannot prove causation (correlation only) |
| Gen 4 solved | `confidence_high` | 99.8% accuracy on clean samples |
| Gen 4 fails | `confidence_low` | Poor robustness to post-processing |
| Connecting arrows | `data_flow` | Vertical lines between steps showing failure-to-motivation chain |
| Footer callout | `callout_bar` | "All four coexist -- no generation replaces the prior ones" |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Gen 1 fails | Gen 2 motivation | arrow | "Fails on transforms" |
| Gen 2 fails | Gen 3 motivation | arrow | "Fails on model attacks" |
| Gen 3 fails | Gen 4 motivation | arrow | "Cannot prove causation" |
| Gen 4 | Open problem | arrow | "Robustness unsolved" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "COEXISTENCE" | All four generations remain in active use -- Gen 1 fingerprinting still dominates for exact-match use cases like Content ID and radio monitoring | footer |
| "CAUSATION GAP" | No generation solves the fundamental problem: proving that a specific training example causally influenced a specific output | right margin |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "Gen 1: Audio Fingerprinting"
- Label 2: "Gen 2: Watermarking"
- Label 3: "Gen 3: Embedding Similarity"
- Label 4: "Gen 4: AI Detection"
- Label 5: "Shazam / Chromaprint"
- Label 6: "AudioSeal / SynthID Audio"
- Label 7: "CLAP / CLMR"
- Label 8: "Afchar ICASSP 2025"
- Label 9: "Exact Matching"
- Label 10: "Embedded Signal"
- Label 11: "Learned Representations"
- Label 12: "Binary Classification"
- Label 13: "99.8% Accuracy (clean)"
- Label 14: "Fails on Transforms"
- Label 15: "Cannot Prove Causation"

### Caption (for embedding in documentation)

Four generations of content identification: audio fingerprinting (Shazam/Chromaprint), watermarking (AudioSeal/SynthID), embedding similarity (CLAP/CLMR), and AI detection (Afchar et al. 2025). Each generation addresses the specific failure of its predecessor, but all four coexist -- none replaces the prior. The fundamental causation gap remains unsolved across all generations.

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

8. Shazam uses spectral fingerprinting -- do NOT describe it as watermarking or AI-based.
9. AcoustID uses Chromaprint -- they are part of the same ecosystem, not competitors.
10. Afchar et al. is ICASSP 2025 -- do NOT cite a different venue or year.
11. The 99.8% accuracy is specifically for Afchar et al. on clean samples -- do NOT generalize it to all AI detection.
12. CLAP is Contrastive Language-Audio Pretraining -- do NOT confuse with CLIP (vision).
13. Do NOT imply Gen 4 replaces Gen 1-3 -- all coexist for different use cases.
14. Do NOT add a "Gen 5" -- the figure covers the current state, not speculation.
15. "Fails" means the approach has known limitations, not that it is useless.

## Alt Text

Four generations of content ID from fingerprinting to AI detection, each solving prior generation failures

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "landscape-12",
    "title": "Content ID Evolution: From Shazam to AI Detection",
    "audience": "L3",
    "layout_template": "E"
  },
  "content_architecture": {
    "primary_message": "Four generations of content identification each address failures of the prior generation but all coexist.",
    "layout_flow": "top-to-bottom-steps",
    "key_structures": [
      {
        "name": "Gen 1: Audio Fingerprinting",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["Shazam / Chromaprint", "Exact matching"]
      },
      {
        "name": "Gen 2: Watermarking",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["AudioSeal / SynthID", "Embedded signal"]
      },
      {
        "name": "Gen 3: Embedding Similarity",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["CLAP / CLMR", "Learned representations"]
      },
      {
        "name": "Gen 4: AI Detection",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["Afchar ICASSP 2025", "Binary classification"]
      }
    ],
    "relationships": [
      {
        "from": "Gen 1",
        "to": "Gen 2",
        "type": "arrow",
        "label": "fails on transforms"
      },
      {
        "from": "Gen 2",
        "to": "Gen 3",
        "type": "arrow",
        "label": "fails on model attacks"
      },
      {
        "from": "Gen 3",
        "to": "Gen 4",
        "type": "arrow",
        "label": "cannot prove causation"
      }
    ],
    "callout_boxes": [
      {
        "heading": "COEXISTENCE",
        "body_text": "All four generations remain in active use for different use cases",
        "position": "footer"
      },
      {
        "heading": "CAUSATION GAP",
        "body_text": "No generation proves causal influence of training data on output",
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
- [x] Anti-hallucination rules listed
- [x] Alt text provided (125 chars max)
- [x] JSON export block included
- [x] Audience level correct (L3)
- [x] Layout template identified (E)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25
- [ ] Embedded in documentation
