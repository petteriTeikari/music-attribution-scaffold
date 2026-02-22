# fig-persona-29: Persona Coherence Recommended Stack

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-persona-29 |
| **Title** | Persona Coherence Recommended Stack -- Six Layers |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/architecture/persona.md, docs/planning/ |
| **Priority** | P0 (Critical) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | E (Steps) |

## Purpose

Shows the six-layer recommended technology stack for persona coherence, from the agent framework foundation (PydanticAI) through memory, persona engine, drift detection, voice persona, and evaluation layers. Answers: "What specific technologies should we stack to build a coherent persona system, and how do they layer on the existing MVP?"

## Key Message

The persona coherence stack builds on the existing PydanticAI MVP with six layers: agent framework, memory (Letta/MemGPT + Zep/Graphiti), persona engine (PersonaFuse MoE or Persona Vectors), drift detection (EchoMode + probe-based), voice persona (Pipecat + Cartesia/ElevenLabs), and evaluation (PersonaGym + CharacterBench).

## Visual Concept

Six horizontal layers stacked from bottom to top, each with a Roman numeral, layer name, and specific technology recommendations. The bottom layer (PydanticAI) is wider to convey it as the foundation. Each layer shows primary and secondary tool choices. An annotation on the left marks which layers are "existing MVP" vs "new additions." A callout emphasizes that the persona layer wraps the existing agent.

```
+---------------------------------------------------------------+
|  PERSONA COHERENCE RECOMMENDED STACK                           |
+---------------------------------------------------------------+
|                                                                |
|              NEW   ┌────────────────────────────────────┐     |
|           ADDITIONS│ VI. EVALUATION                      │     |
|              ▲     │     PersonaGym + CharacterBench     │     |
|              │     └────────────────────────────────────┘     |
|              │     ┌────────────────────────────────────┐     |
|              │     │ V. VOICE PERSONA                    │     |
|              │     │    Pipecat + Cartesia/ElevenLabs    │     |
|              │     └────────────────────────────────────┘     |
|              │     ┌────────────────────────────────────┐     |
|              │     │ IV. DRIFT DETECTION                 │     |
|              │     │     EchoMode + Probe-based +        │     |
|              │     │     Persona Vector Monitoring       │     |
|              │     └────────────────────────────────────┘     |
|              │     ┌────────────────────────────────────┐     |
|              │     │ III. PERSONA ENGINE                  │     |
|              │     │      PersonaFuse MoE or              │     |
|              │     │      Persona Vectors                 │     |
|              │     └────────────────────────────────────┘     |
|              │     ┌────────────────────────────────────┐     |
|              │     │ II. MEMORY                           │     |
|              │     │     Letta/MemGPT (core) +            │     |
|              │     │     Zep/Graphiti (temporal KG)       │     |
|              │     └────────────────────────────────────┘     |
|   EXISTING   │     ┌────────────────────────────────────────┐ |
|      MVP ────┘     │ I. AGENT FRAMEWORK                      │ |
|                    │    PydanticAI                            │ |
|                    └────────────────────────────────────────┘ |
|                                                                |
+---------------------------------------------------------------+
|  BUILDS ON EXISTING MVP -- PERSONA LAYER WRAPS THE PYDANTICAI  |
|  AGENT                                                         |
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
    content: "PERSONA COHERENCE RECOMMENDED STACK"
    role: title

  - id: stack_zone
    bounds: [300, 160, 1400, 720]
    role: content_area

  - id: annotation_zone
    bounds: [80, 160, 200, 720]
    role: content_area

  - id: callout_zone
    bounds: [80, 920, 1760, 120]
    role: callout_box

anchors:
  - id: layer_1_agent
    position: [960, 800]
    size: [1200, 100]
    role: selected_option
    label: "I. AGENT FRAMEWORK: PydanticAI"

  - id: layer_2_memory
    position: [960, 690]
    size: [1100, 100]
    role: processing_stage
    label: "II. MEMORY: Letta/MemGPT + Zep/Graphiti"

  - id: layer_3_persona
    position: [960, 580]
    size: [1100, 100]
    role: processing_stage
    label: "III. PERSONA ENGINE: PersonaFuse MoE or Persona Vectors"

  - id: layer_4_drift
    position: [960, 470]
    size: [1100, 100]
    role: processing_stage
    label: "IV. DRIFT DETECTION: EchoMode + Probe-based"

  - id: layer_5_voice
    position: [960, 360]
    size: [1100, 100]
    role: processing_stage
    label: "V. VOICE PERSONA: Pipecat + Cartesia/ElevenLabs"

  - id: layer_6_eval
    position: [960, 250]
    size: [1100, 100]
    role: processing_stage
    label: "VI. EVALUATION: PersonaGym + CharacterBench"

  - id: mvp_bracket
    position: [180, 800]
    size: [100, 100]
    role: selected_option
    label: "EXISTING MVP"

  - id: new_bracket
    position: [180, 500]
    size: [100, 550]
    role: decision_point
    label: "NEW ADDITIONS"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "PERSONA COHERENCE RECOMMENDED STACK" with accent square |
| Layer I: Agent Framework | `selected_option` | PydanticAI -- existing MVP foundation, wider base |
| Layer II: Memory | `processing_stage` | Letta/MemGPT for core memory + Zep/Graphiti for temporal KG |
| Layer III: Persona Engine | `processing_stage` | PersonaFuse MoE or Persona Vectors for persona control |
| Layer IV: Drift Detection | `processing_stage` | EchoMode + probe-based + Persona Vector Monitoring |
| Layer V: Voice Persona | `processing_stage` | Pipecat framework + Cartesia/ElevenLabs for TTS |
| Layer VI: Evaluation | `processing_stage` | PersonaGym + CharacterBench for persona quality metrics |
| MVP annotation | `selected_option` | Marks Layer I as existing implementation |
| New additions annotation | `decision_point` | Marks Layers II-VI as proposed additions |
| Callout bar | `callout_bar` | Builds on existing MVP -- persona layer wraps PydanticAI agent |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Layer I | Layer II | arrow | "provides agent context" |
| Layer II | Layer III | arrow | "feeds memory to persona" |
| Layer III | Layer IV | arrow | "monitored for drift" |
| Layer IV | Layer V | arrow | "voice consistency check" |
| Layer V | Layer VI | arrow | "evaluated by benchmarks" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "BUILDS ON MVP" | Persona layer wraps the existing PydanticAI agent -- no rewrite needed, additive layers only | bottom-center |
| "DUAL MEMORY" | Letta/MemGPT for core persistent memory + Zep/Graphiti for temporal knowledge graph -- complementary, not competing | right-margin |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "I. AGENT FRAMEWORK"
- Label 2: "PydanticAI"
- Label 3: "II. MEMORY"
- Label 4: "Letta/MemGPT + Zep/Graphiti"
- Label 5: "III. PERSONA ENGINE"
- Label 6: "PersonaFuse MoE"
- Label 7: "IV. DRIFT DETECTION"
- Label 8: "EchoMode + Probe-based"
- Label 9: "V. VOICE PERSONA"
- Label 10: "Pipecat + Cartesia"
- Label 11: "VI. EVALUATION"
- Label 12: "PersonaGym + CharacterBench"
- Label 13: "EXISTING MVP"
- Label 14: "NEW ADDITIONS"

### Caption (for embedding in documentation)

Six-layer persona coherence recommended stack building on the existing PydanticAI MVP: Agent Framework, Memory (Letta/MemGPT + Zep/Graphiti), Persona Engine (PersonaFuse MoE), Drift Detection (EchoMode), Voice Persona (Pipecat + Cartesia), and Evaluation (PersonaGym + CharacterBench).

## Anti-Hallucination Rules

These are INTERNAL instructions for prompt construction. They MUST NEVER appear as visible text in the generated image.

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `selected_option`, `processing_stage`, `decision_point` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- This is L3 so all tool names (PydanticAI, Letta, MemGPT, Zep, Graphiti, PersonaFuse, EchoMode, Pipecat, Cartesia, ElevenLabs, PersonaGym, CharacterBench) ARE allowed.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. Exactly 6 layers numbered with Roman numerals I-VI from bottom to top.
10. Layer I (PydanticAI) is EXISTING MVP -- it MUST be visually distinct as the foundation.
11. Layers II-VI are NEW ADDITIONS -- they MUST be annotated as proposed, not implemented.
12. Memory layer has TWO complementary systems: Letta/MemGPT (core) AND Zep/Graphiti (temporal KG).
13. Persona Engine offers TWO options: PersonaFuse MoE OR Persona Vectors -- these are alternatives, not both.
14. Drift Detection has THREE components: EchoMode, probe-based, Persona Vector Monitoring.
15. Voice Persona combines Pipecat (framework) with Cartesia OR ElevenLabs (TTS provider).
16. Do NOT imply any layer above I is currently implemented -- they are recommendations.

## Alt Text

Six-layer persona coherence recommended technology stack for music attribution building on PydanticAI MVP foundation with Memory, Persona Engine, Drift Detection, Voice Persona, and Evaluation layers using Letta, PersonaFuse, EchoMode, Pipecat, and PersonaGym tools

## Image Embed

![Six-layer persona coherence recommended technology stack for music attribution building on PydanticAI MVP foundation with Memory, Persona Engine, Drift Detection, Voice Persona, and Evaluation layers using Letta, PersonaFuse, EchoMode, Pipecat, and PersonaGym tools](docs/figures/repo-figures/assets/fig-persona-29-persona-coherence-recommended-stack.jpg)

*Six-layer persona coherence recommended stack building on the existing PydanticAI MVP: Agent Framework, Memory (Letta/MemGPT + Zep/Graphiti), Persona Engine (PersonaFuse MoE), Drift Detection (EchoMode), Voice Persona (Pipecat + Cartesia), and Evaluation (PersonaGym + CharacterBench).*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "persona-29",
    "title": "Persona Coherence Recommended Stack",
    "audience": "L3",
    "layout_template": "E"
  },
  "content_architecture": {
    "primary_message": "Six-layer persona coherence stack builds on existing PydanticAI MVP with memory, persona engine, drift detection, voice persona, and evaluation layers.",
    "layout_flow": "top-to-bottom",
    "key_structures": [
      {
        "name": "Layer I: Agent Framework",
        "role": "selected_option",
        "is_highlighted": true,
        "labels": ["I. AGENT FRAMEWORK", "PydanticAI", "EXISTING MVP"]
      },
      {
        "name": "Layer II: Memory",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["II. MEMORY", "Letta/MemGPT + Zep/Graphiti"]
      },
      {
        "name": "Layer III: Persona Engine",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["III. PERSONA ENGINE", "PersonaFuse MoE or Persona Vectors"]
      },
      {
        "name": "Layer IV: Drift Detection",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["IV. DRIFT DETECTION", "EchoMode + Probe-based"]
      },
      {
        "name": "Layer V: Voice Persona",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["V. VOICE PERSONA", "Pipecat + Cartesia/ElevenLabs"]
      },
      {
        "name": "Layer VI: Evaluation",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["VI. EVALUATION", "PersonaGym + CharacterBench"]
      }
    ],
    "relationships": [
      {
        "from": "Layer I",
        "to": "Layer II",
        "type": "arrow",
        "label": "provides agent context"
      },
      {
        "from": "Layer II",
        "to": "Layer III",
        "type": "arrow",
        "label": "feeds memory to persona"
      },
      {
        "from": "Layer III",
        "to": "Layer IV",
        "type": "arrow",
        "label": "monitored for drift"
      },
      {
        "from": "Layer IV",
        "to": "Layer V",
        "type": "arrow",
        "label": "voice consistency check"
      },
      {
        "from": "Layer V",
        "to": "Layer VI",
        "type": "arrow",
        "label": "evaluated by benchmarks"
      }
    ],
    "callout_boxes": [
      {
        "heading": "BUILDS ON MVP",
        "body_text": "Persona layer wraps the existing PydanticAI agent -- no rewrite needed",
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
- [x] Audience level correct (L3)
- [x] Layout template identified (E)

## Status

- [x] Draft created
- [ ] Content reviewed
- [x] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
