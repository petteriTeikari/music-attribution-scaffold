# fig-persona-23: PersonaPlex Architecture

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-persona-23 |
| **Title** | PersonaPlex Architecture -- Dual-Input Persona Control |
| **Audience** | L4 (AI/ML Architect) |
| **Location** | docs/planning/persona-coherence.md, docs/architecture/ |
| **Priority** | P2 (Medium) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | E (Steps) |

## Purpose

Shows NVIDIA PersonaPlex's dual-input architecture where both a voice prompt and a text prompt feed into a Llama backbone that produces persona-controlled audio output. Answers: "How does PersonaPlex achieve 0.07s speaker-switch latency compared to Gemini Live's 1.3s, and what does dual-input persona control mean architecturally?"

## Key Message

PersonaPlex uses dual inputs (voice characteristics prompt + role definition prompt) through a 7B-parameter Llama backbone with a specialized audio decoder, achieving 0.07s speaker-switch latency -- 18x faster than Gemini Live's 1.3s -- enabling real-time full-duplex persona-controlled conversations.

## Visual Concept

A left-to-right stepped pipeline: two input sources (voice prompt and text prompt) converge at the Llama 7B backbone, which feeds into an audio decoder producing persona-controlled output. A comparison bar at the bottom contrasts PersonaPlex 0.07s vs Gemini Live 1.3s speaker-switch latency. Key specs (7B parameters, full-duplex) annotate the backbone stage.

```
+---------------------------------------------------------------+
|  PERSONAPLEX ARCHITECTURE                                      |
|  -- Dual-Input Persona Control                                 |
+---------------------------------------------------------------+
|                                                                |
|  I. VOICE PROMPT          II. LLAMA 7B           III. AUDIO    |
|  ┌──────────────┐          BACKBONE               DECODER      |
|  │ Voice charac- │         ┌──────────┐          ┌──────────┐  |
|  │ teristics     │────────>│          │          │          │  |
|  │ (timbre,      │         │ 7B param │─────────>│ Persona- │  |
|  │  pace, tone)  │         │ Full-    │          │ controlled│  |
|  └──────────────┘         │ duplex   │          │ audio     │  |
|                            │          │          │ output    │  |
|  ┌──────────────┐         │          │          └──────────┘  |
|  │ Text role     │────────>│          │                        |
|  │ definition    │         └──────────┘                        |
|  │ (personality, │                                             |
|  │  expertise)   │         SPECS:                              |
|  └──────────────┘         ■ 7B parameters                     |
|                            ■ Full-duplex                       |
|                            ■ 0.07s speaker-switch              |
|                                                                |
|  ┌─────────────────────────────────────────────────────┐      |
|  │  LATENCY COMPARISON                                  │      |
|  │  PersonaPlex  ██ 0.07s                               │      |
|  │  Gemini Live  ████████████████████████████ 1.3s       │      |
|  │                                  18x faster           │      |
|  └─────────────────────────────────────────────────────┘      |
|                                                                |
+---------------------------------------------------------------+
|  DUAL-INPUT PERSONA CONTROL -- VOICE CHARACTERISTICS +         |
|  ROLE DEFINITION                                               |
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
    content: "PERSONAPLEX ARCHITECTURE"
    role: title

  - id: pipeline_zone
    bounds: [80, 150, 1760, 480]
    role: content_area

  - id: comparison_zone
    bounds: [200, 660, 1520, 200]
    role: content_area

  - id: callout_zone
    bounds: [80, 920, 1760, 120]
    role: callout_box

anchors:
  - id: input_voice
    position: [280, 320]
    size: [360, 200]
    role: processing_stage
    label: "VOICE PROMPT"

  - id: input_text
    position: [280, 540]
    size: [360, 200]
    role: processing_stage
    label: "TEXT ROLE DEFINITION"

  - id: backbone
    position: [860, 400]
    size: [400, 260]
    role: processing_stage
    label: "LLAMA 7B BACKBONE"

  - id: decoder
    position: [1480, 400]
    size: [360, 200]
    role: final_score
    label: "AUDIO DECODER"

  - id: bar_personaplex
    position: [600, 720]
    size: [200, 40]
    role: confidence_high
    label: "PersonaPlex 0.07s"

  - id: bar_gemini
    position: [600, 780]
    size: [1100, 40]
    role: confidence_low
    label: "Gemini Live 1.3s"

  - id: flow_voice_to_backbone
    from: input_voice
    to: backbone
    type: arrow
    label: "timbre, pace, tone"

  - id: flow_text_to_backbone
    from: input_text
    to: backbone
    type: arrow
    label: "personality, expertise"

  - id: flow_backbone_to_decoder
    from: backbone
    to: decoder
    type: arrow
    label: "persona-fused representation"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "PERSONAPLEX ARCHITECTURE" with accent square |
| Voice prompt input | `processing_stage` | Voice characteristics: timbre, pace, tone, accent |
| Text role definition input | `processing_stage` | Personality definition: expertise, style, domain knowledge |
| Llama 7B backbone | `processing_stage` | 7B-parameter transformer backbone, full-duplex capable |
| Audio decoder | `final_score` | Specialized decoder producing persona-controlled audio |
| PersonaPlex bar | `confidence_high` | 0.07s speaker-switch latency bar (short) |
| Gemini Live bar | `confidence_low` | 1.3s speaker-switch latency bar (long, 18x) |
| Specs annotation | `data_mono` | Key numbers: 7B params, full-duplex, 0.07s |
| Callout bar | `callout_bar` | Dual-input persona control message |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Voice prompt | Llama 7B backbone | arrow | "timbre, pace, tone" |
| Text role definition | Llama 7B backbone | arrow | "personality, expertise" |
| Llama 7B backbone | Audio decoder | arrow | "persona-fused representation" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "DUAL-INPUT CONTROL" | Voice characteristics + role definition enter as separate prompts -- the backbone fuses them into a coherent persona | bottom-center |
| "18x FASTER" | PersonaPlex 0.07s vs Gemini Live 1.3s speaker-switch latency | bottom-right |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "VOICE PROMPT"
- Label 2: "TEXT ROLE DEFINITION"
- Label 3: "LLAMA 7B BACKBONE"
- Label 4: "AUDIO DECODER"
- Label 5: "timbre, pace, tone"
- Label 6: "personality, expertise"
- Label 7: "7B parameters"
- Label 8: "Full-duplex"
- Label 9: "0.07s speaker-switch"
- Label 10: "PersonaPlex 0.07s"
- Label 11: "Gemini Live 1.3s"
- Label 12: "18x faster"

### Caption (for embedding in documentation)

NVIDIA PersonaPlex architecture showing dual-input persona control -- voice characteristics prompt and text role definition prompt converge at a 7B-parameter Llama backbone with audio decoder, achieving 0.07s speaker-switch latency (18x faster than Gemini Live).

## Anti-Hallucination Rules

These are INTERNAL instructions for prompt construction. They MUST NEVER appear as visible text in the generated image.

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `processing_stage`, `final_score`, `confidence_high` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- This is L4 so ML terms (backbone, decoder, full-duplex, parameters) ARE allowed.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. PersonaPlex is an NVIDIA product -- do NOT attribute it to another company.
10. The backbone is Llama-based with 7B parameters -- do NOT change the parameter count or model family.
11. 0.07s is the speaker-switch latency, NOT the generation latency or first-token latency.
12. 1.3s is Gemini Live's speaker-switch latency for comparison -- do NOT confuse with other metrics.
13. Full-duplex means simultaneous send/receive -- do NOT describe as half-duplex or turn-based.
14. The dual inputs are SEPARATE prompts (voice + text), NOT a single combined prompt.
15. Do NOT imply PersonaPlex is integrated into the scaffold -- it is a reference architecture.
16. The comparison bar must make the 18x difference visually obvious through proportional length.

## Alt Text

NVIDIA PersonaPlex architecture diagram showing dual-input persona control where voice prompt and text role definition converge at a Llama 7B backbone with audio decoder, achieving 0.07s speaker-switch latency versus Gemini Live 1.3s for voice agent persona coherence

## Image Embed

![NVIDIA PersonaPlex architecture diagram showing dual-input persona control where voice prompt and text role definition converge at a Llama 7B backbone with audio decoder, achieving 0.07s speaker-switch latency versus Gemini Live 1.3s for voice agent persona coherence](docs/figures/repo-figures/assets/fig-persona-23-personaplex-architecture.jpg)

*NVIDIA PersonaPlex architecture showing dual-input persona control -- voice characteristics prompt and text role definition prompt converge at a 7B-parameter Llama backbone with audio decoder, achieving 0.07s speaker-switch latency (18x faster than Gemini Live).*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "persona-23",
    "title": "PersonaPlex Architecture -- Dual-Input Persona Control",
    "audience": "L4",
    "layout_template": "E"
  },
  "content_architecture": {
    "primary_message": "PersonaPlex uses dual inputs (voice + text prompts) through a 7B Llama backbone achieving 0.07s speaker-switch -- 18x faster than Gemini Live.",
    "layout_flow": "left-to-right",
    "key_structures": [
      {
        "name": "Voice Prompt",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["VOICE PROMPT", "timbre, pace, tone"]
      },
      {
        "name": "Text Role Definition",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["TEXT ROLE DEFINITION", "personality, expertise"]
      },
      {
        "name": "Llama 7B Backbone",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["LLAMA 7B BACKBONE", "7B parameters", "Full-duplex"]
      },
      {
        "name": "Audio Decoder",
        "role": "final_score",
        "is_highlighted": false,
        "labels": ["AUDIO DECODER"]
      },
      {
        "name": "Latency Comparison",
        "role": "confidence_high",
        "is_highlighted": true,
        "labels": ["PersonaPlex 0.07s", "Gemini Live 1.3s", "18x faster"]
      }
    ],
    "relationships": [
      {
        "from": "Voice Prompt",
        "to": "Llama 7B Backbone",
        "type": "arrow",
        "label": "timbre, pace, tone"
      },
      {
        "from": "Text Role Definition",
        "to": "Llama 7B Backbone",
        "type": "arrow",
        "label": "personality, expertise"
      },
      {
        "from": "Llama 7B Backbone",
        "to": "Audio Decoder",
        "type": "arrow",
        "label": "persona-fused representation"
      }
    ],
    "callout_boxes": [
      {
        "heading": "DUAL-INPUT CONTROL",
        "body_text": "Voice characteristics + role definition as separate prompts, fused in the backbone",
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
- [x] Anti-hallucination rules listed (8 default + 8 figure-specific)
- [x] Alt text provided (125 chars max)
- [x] JSON export block included
- [x] Audience level correct (L4)
- [x] Layout template identified (E)

## Status

- [x] Draft created
- [ ] Content reviewed
- [x] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
