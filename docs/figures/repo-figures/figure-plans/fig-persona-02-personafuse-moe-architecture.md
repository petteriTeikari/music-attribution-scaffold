# fig-persona-02: PersonaFuse Mixture-of-Experts Architecture

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-persona-02 |
| **Title** | PersonaFuse Mixture-of-Experts Architecture |
| **Audience** | L4 (AI/ML Architect) |
| **Location** | docs/knowledge-base/persona-engineering/, docs/planning/ |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | E (Steps) |

## Purpose

Shows the PersonaFuse architecture that uses 10 LoRA experts (one per Big Five personality pole) with a situation-aware router to compose arbitrary personas at inference time, trained through a three-stage pipeline. Answers: "How can you implement fine-grained personality control without training a separate model per persona?"

## Key Message

PersonaFuse composes arbitrary personas from 10 Big Five LoRA experts via a lightweight situation-aware router, achieving +37.9% EmoBench and +69.0% EQ-Bench improvements while preserving safety.

## Visual Concept

Steps layout (Template E) with three training stages flowing left to right across the top, and the inference architecture shown below. Stage 1: LoRA Warmup (10 experts trained independently). Stage 2: Router Training (Qwen2.5-0.5B situation classifier). Stage 3: Joint Training (end-to-end fine-tuning). Below the stages, a detailed inference flow shows: input prompt entering the router, which produces expert weights, then the weighted combination of LoRA experts applied to the base LLM, passing through Persona-CoT reasoning, and producing the final output.

```
+-----------------------------------------------------------------------+
|  PERSONAFUSE                                                    [sq]   |
|  MIXTURE-OF-EXPERTS ARCHITECTURE                                       |
+-----------------------------------------------------------------------+
|                                                                        |
|  TRAINING PIPELINE                                                     |
|  ════════════════                                                      |
|                                                                        |
|  STAGE 1              STAGE 2              STAGE 3                     |
|  LoRA Warmup          Router Training      Joint Training              |
|  ┌──────────┐         ┌──────────┐         ┌──────────┐               |
|  │ 10 LoRA  │ ──────> │ Qwen2.5  │ ──────> │ End-to-  │               |
|  │ experts  │         │ 0.5B     │         │ end      │               |
|  │ trained  │         │ router   │         │ fine-    │               |
|  │ per pole │         │ trained  │         │ tuning   │               |
|  └──────────┘         └──────────┘         └──────────┘               |
|                                                                        |
|  ─────────────────────────────────────────────────────────────         |
|                                                                        |
|  INFERENCE ARCHITECTURE                                                |
|  ═════════════════════                                                 |
|                                                                        |
|  ┌────────┐   ┌─────────────┐   ┌─────────────────────┐              |
|  │ Input  │──>│ Situation   │──>│  Expert Weights      │              |
|  │ Prompt │   │ Router      │   │  O+ A+ C- E+ N-     │              |
|  └────────┘   │ (Qwen 0.5B)│   │  0.8 0.6 0.2 0.7 0.1│              |
|               └─────────────┘   └──────────┬──────────┘              |
|                                             │                          |
|                                             ▼                          |
|               ┌─────────────────────────────────────────┐             |
|               │  BASE LLM + Weighted LoRA Combination   │             |
|               │  Σ (weight_i × LoRA_i)                   │             |
|               └──────────────────┬──────────────────────┘             |
|                                  │                                     |
|                                  ▼                                     |
|               ┌──────────────────────────────────┐                    |
|               │  Persona-CoT Pipeline            │                    |
|               │  Think → Reflect → Respond       │                    |
|               └──────────────────┬───────────────┘                    |
|                                  │                                     |
|                                  ▼                                     |
|               ┌──────────────────────────────────┐                    |
|               │  Output with persona consistency  │                    |
|               └──────────────────────────────────┘                    |
|                                                                        |
|  +37.9% EMOBENCH, +69.0% EQ-BENCH WHILE PRESERVING SAFETY      [sq]  |
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
    content: "PERSONAFUSE MIXTURE-OF-EXPERTS ARCHITECTURE"
    role: title

  - id: training_label
    bounds: [80, 130, 400, 30]
    content: "TRAINING PIPELINE"
    role: label_editorial

  - id: training_zone
    bounds: [80, 160, 1760, 260]
    role: content_area

  - id: divider
    bounds: [80, 440, 1760, 2]
    role: accent_line

  - id: inference_label
    bounds: [80, 460, 400, 30]
    content: "INFERENCE ARCHITECTURE"
    role: label_editorial

  - id: inference_zone
    bounds: [80, 490, 1760, 440]
    role: content_area

  - id: callout_zone
    bounds: [80, 960, 1760, 100]
    content: "+37.9% EMOBENCH, +69.0% EQ-BENCH WHILE PRESERVING SAFETY"
    role: callout_box

anchors:
  - id: stage_1
    position: [120, 180]
    size: [480, 200]
    role: processing_stage
    label: "STAGE 1: LoRA WARMUP"

  - id: stage_2
    position: [720, 180]
    size: [480, 200]
    role: processing_stage
    label: "STAGE 2: ROUTER TRAINING"

  - id: stage_3
    position: [1320, 180]
    size: [480, 200]
    role: processing_stage
    label: "STAGE 3: JOINT TRAINING"

  - id: input_prompt
    position: [120, 510]
    size: [200, 80]
    role: data_flow
    label: "Input Prompt"

  - id: router
    position: [400, 510]
    size: [320, 100]
    role: decision_point
    label: "Situation Router"

  - id: expert_weights
    position: [800, 510]
    size: [400, 100]
    role: decision_point
    label: "Expert Weights"

  - id: base_llm_lora
    position: [400, 650]
    size: [800, 80]
    role: processing_stage
    label: "BASE LLM + Weighted LoRA"

  - id: persona_cot
    position: [500, 770]
    size: [600, 80]
    role: processing_stage
    label: "Persona-CoT Pipeline"

  - id: output
    position: [600, 880]
    size: [400, 60]
    role: final_score
    label: "Persona-consistent Output"

  - id: flow_1_to_2
    from: stage_1
    to: stage_2
    type: arrow
    label: "pretrained experts"

  - id: flow_2_to_3
    from: stage_2
    to: stage_3
    type: arrow
    label: "trained router"

  - id: flow_input_to_router
    from: input_prompt
    to: router
    type: arrow
    label: "situation context"

  - id: flow_router_to_weights
    from: router
    to: expert_weights
    type: arrow
    label: "weight distribution"

  - id: flow_weights_to_llm
    from: expert_weights
    to: base_llm_lora
    type: arrow
    label: "weighted combination"

  - id: flow_llm_to_cot
    from: base_llm_lora
    to: persona_cot
    type: arrow
    label: "raw generation"

  - id: flow_cot_to_output
    from: persona_cot
    to: output
    type: arrow
    label: "persona-consistent"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "PERSONAFUSE MIXTURE-OF-EXPERTS ARCHITECTURE" in editorial caps |
| Stage 1: LoRA Warmup | `processing_stage` | 10 LoRA experts trained independently, one per Big Five pole (O+, O-, A+, A-, C+, C-, E+, E-, N+, N-) |
| Stage 2: Router Training | `processing_stage` | Qwen2.5-0.5B situation-aware router trained to classify conversation context |
| Stage 3: Joint Training | `processing_stage` | End-to-end fine-tuning of router + experts together |
| Input Prompt | `data_flow` | User input entering the inference pipeline |
| Situation Router | `decision_point` | Qwen2.5-0.5B model that produces per-expert activation weights based on context |
| Expert Weights | `decision_point` | Weight distribution across 10 LoRA experts (e.g., O+ 0.8, A+ 0.6, C- 0.2) |
| Base LLM + Weighted LoRA | `processing_stage` | Base model with weighted sum of LoRA expert parameters applied |
| Persona-CoT Pipeline | `processing_stage` | Chain-of-thought reasoning: Think, Reflect, Respond stages |
| Persona-consistent Output | `final_score` | Final generation maintaining persona consistency |

### Relationships / Flows

| From | To | Type | Label |
|------|----|------|-------|
| Stage 1 | Stage 2 | arrow | "pretrained experts" |
| Stage 2 | Stage 3 | arrow | "trained router" |
| Input Prompt | Situation Router | arrow | "situation context" |
| Situation Router | Expert Weights | arrow | "weight distribution" |
| Expert Weights | Base LLM + LoRA | arrow | "weighted combination" |
| Base LLM + LoRA | Persona-CoT | arrow | "raw generation" |
| Persona-CoT | Output | arrow | "persona-consistent output" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "+37.9% EMOBENCH, +69.0% EQ-BENCH WHILE PRESERVING SAFETY" | PersonaFuse achieves large gains on emotional intelligence benchmarks without degrading safety alignment. The MoE architecture allows composing new personality profiles at inference time without retraining. | bottom-full-width |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "TRAINING PIPELINE"
- Label 2: "INFERENCE ARCHITECTURE"
- Label 3: "STAGE 1: LoRA WARMUP"
- Label 4: "STAGE 2: ROUTER TRAINING"
- Label 5: "STAGE 3: JOINT TRAINING"
- Label 6: "10 Big Five LoRA experts"
- Label 7: "Qwen2.5-0.5B router"
- Label 8: "End-to-end fine-tuning"
- Label 9: "Situation Router"
- Label 10: "Expert Weights"
- Label 11: "BASE LLM + Weighted LoRA"
- Label 12: "Persona-CoT Pipeline"
- Label 13: "Think > Reflect > Respond"
- Label 14: "O+ A+ C- E+ N-"
- Label 15: "Weighted combination"

### Caption

PersonaFuse Mixture-of-Experts architecture showing three-stage training pipeline (LoRA Warmup, Router Training, Joint Training) and inference flow where a situation-aware Qwen2.5-0.5B router composes 10 Big Five personality LoRA experts into arbitrary persona profiles via Persona-CoT reasoning.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- do NOT render them as labels.
2. **Semantic tags are INTERNAL** -- do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- do NOT render them.
4. **Engineering jargon** -- LoRA, MoE, Big Five, Qwen2.5 are appropriate for L4 audience.
5. **Background MUST be warm cream (#f6f3e6)**.
6. **No generic flowchart aesthetics** -- no thick block arrows, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or numbered caption.
8. **No prompt leakage** -- do NOT render style keywords as visible text.

### Figure-Specific Rules

9. PersonaFuse is a specific architecture from Cao et al. (2025) -- do NOT attribute it to other authors.
10. The Big Five poles are: Openness (O+/O-), Agreeableness (A+/A-), Conscientiousness (C+/C-), Extraversion (E+/E-), Neuroticism (N+/N-) -- exactly 10 experts.
11. The router is specifically Qwen2.5-0.5B -- do NOT substitute a different model.
12. Persona-CoT is a specific prompting pipeline (Think, Reflect, Respond) -- do NOT conflate with generic chain-of-thought.
13. The +37.9% EmoBench and +69.0% EQ-Bench numbers are from the PersonaFuse paper -- do NOT round or alter them.
14. "While preserving safety" means the model did NOT degrade on safety benchmarks -- do NOT imply zero safety cost without qualification.
15. The three training stages are sequential and mandatory -- do NOT show them as optional or parallel.

## Alt Text

System architecture diagram of PersonaFuse Mixture-of-Experts showing a three-stage training pipeline and inference flow where a Qwen2.5-0.5B situation-aware router composes 10 Big Five personality LoRA experts via weighted combination and Persona-CoT reasoning.

## Image Embed

![System architecture diagram of PersonaFuse Mixture-of-Experts showing a three-stage training pipeline and inference flow where a Qwen2.5-0.5B situation-aware router composes 10 Big Five personality LoRA experts via weighted combination and Persona-CoT reasoning.](docs/figures/repo-figures/assets/fig-persona-02-personafuse-moe-architecture.jpg)

*PersonaFuse Mixture-of-Experts architecture showing three-stage training pipeline (LoRA Warmup, Router Training, Joint Training) and inference flow where a situation-aware Qwen2.5-0.5B router composes 10 Big Five personality LoRA experts into arbitrary persona profiles via Persona-CoT reasoning.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "persona-02",
    "title": "PersonaFuse Mixture-of-Experts Architecture",
    "audience": "L4",
    "layout_template": "E"
  },
  "content_architecture": {
    "primary_message": "PersonaFuse composes arbitrary personas from 10 Big Five LoRA experts via a lightweight situation-aware router.",
    "layout_flow": "left-to-right-then-top-to-bottom",
    "key_structures": [
      {
        "name": "Stage 1: LoRA Warmup",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["STAGE 1: LoRA WARMUP", "10 Big Five LoRA experts"]
      },
      {
        "name": "Stage 2: Router Training",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["STAGE 2: ROUTER TRAINING", "Qwen2.5-0.5B router"]
      },
      {
        "name": "Stage 3: Joint Training",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["STAGE 3: JOINT TRAINING", "End-to-end fine-tuning"]
      },
      {
        "name": "Situation Router",
        "role": "decision_point",
        "is_highlighted": true,
        "labels": ["Situation Router", "Qwen2.5-0.5B"]
      },
      {
        "name": "Expert Weights",
        "role": "decision_point",
        "is_highlighted": true,
        "labels": ["Expert Weights", "O+ A+ C- E+ N-"]
      },
      {
        "name": "Base LLM + Weighted LoRA",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["BASE LLM + Weighted LoRA"]
      },
      {
        "name": "Persona-CoT Pipeline",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["Persona-CoT Pipeline", "Think > Reflect > Respond"]
      }
    ],
    "relationships": [
      {
        "from": "Stage 1",
        "to": "Stage 2",
        "type": "arrow",
        "label": "pretrained experts"
      },
      {
        "from": "Stage 2",
        "to": "Stage 3",
        "type": "arrow",
        "label": "trained router"
      },
      {
        "from": "Input Prompt",
        "to": "Situation Router",
        "type": "arrow",
        "label": "situation context"
      },
      {
        "from": "Situation Router",
        "to": "Expert Weights",
        "type": "arrow",
        "label": "weight distribution"
      },
      {
        "from": "Expert Weights",
        "to": "Base LLM + LoRA",
        "type": "arrow",
        "label": "weighted combination"
      },
      {
        "from": "Base LLM + LoRA",
        "to": "Persona-CoT",
        "type": "arrow",
        "label": "raw generation"
      },
      {
        "from": "Persona-CoT",
        "to": "Output",
        "type": "arrow",
        "label": "persona-consistent"
      }
    ],
    "callout_boxes": [
      {
        "heading": "+37.9% EMOBENCH, +69.0% EQ-BENCH WHILE PRESERVING SAFETY",
        "body_text": "Large emotional intelligence gains without degrading safety alignment. MoE enables composing new personality profiles at inference time.",
        "position": "bottom-full-width"
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
- [x] Audience level correct (L4)
- [x] Layout template identified (E)

## Status

- [x] Draft created
- [ ] Content reviewed
- [x] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25
- [ ] Embedded in documentation
