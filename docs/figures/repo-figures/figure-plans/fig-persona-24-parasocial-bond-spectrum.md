# fig-persona-24: Parasocial Bond Spectrum

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-persona-24 |
| **Title** | Parasocial Bond Spectrum -- Design Target vs Danger Zone |
| **Audience** | L1 (Music Industry Professional) |
| **Location** | docs/planning/persona-coherence.md, docs/architecture/ |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | E (Steps) |

## Purpose

Shows the spectrum of human-AI relationship depth from purely transactional to parasocial dependency, marking where music attribution agents should target ("Trusted Advisor") and where guardrails must prevent progression. Answers: "How deep should the AI relationship go, and where must we draw the line?"

## Key Message

Music attribution agents should be designed for the "Trusted Advisor" zone -- warm enough to sustain engagement, competent enough to be reliable -- while actively guarding against progression into emotional dependency and parasocial bonding through session limits, dependency detection, and "AI Chaperones."

## Visual Concept

A horizontal spectrum with 5 labeled stages from left (safe) to right (dangerous). The middle stage ("Trusted Advisor") is marked as the design target with a highlight zone. The rightmost two stages are marked as a danger zone with warning treatment. Below the spectrum, guardrail mechanisms are listed. The overall flow is a left-to-right progression with a clear "stop here" boundary.

```
+---------------------------------------------------------------+
|  PARASOCIAL BOND SPECTRUM                                      |
+---------------------------------------------------------------+
|                                                                |
|  SAFE ZONE                TARGET        DANGER ZONE            |
|  ◄────────────────────────  ■  ──────────────────────────►    |
|                                                                |
|  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────┐|
|  │TRANSACT- │ │ HELPFUL  │ │ TRUSTED  │ │ EMOTIONAL│ │PARA- │|
|  │IONAL     │ │ASSISTANT │ │ ADVISOR  │ │COMPANION │ │SOCIAL│|
|  │TOOL      │ │          │ │   ★      │ │          │ │BOND  │|
|  │          │ │          │ │  TARGET   │ │          │ │      │|
|  └──────────┘ └──────────┘ └──────────┘ └──────────┘ └──────┘|
|                                                                |
|                             ▲              ▲                   |
|                             │              │                   |
|                        Design here    Guard against this       |
|                                                                |
|  GUARDRAILS:                                                   |
|  ■ Session time limits                                         |
|  ■ Dependency pattern detection                                |
|  ■ "AI Chaperones" -- meta-agents monitoring relationship      |
|  ■ Explicit "I am an AI" reminders                             |
|                                                                |
+---------------------------------------------------------------+
|  DESIGN FOR TRUSTED ADVISOR, GUARD AGAINST PARASOCIAL          |
|  DEPENDENCY                                                    |
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
    content: "PARASOCIAL BOND SPECTRUM"
    role: title

  - id: spectrum_zone
    bounds: [80, 160, 1760, 400]
    role: content_area

  - id: guardrails_zone
    bounds: [80, 600, 1760, 260]
    role: content_area

  - id: callout_zone
    bounds: [80, 920, 1760, 120]
    role: callout_box

anchors:
  - id: stage_transactional
    position: [240, 350]
    size: [280, 180]
    role: assurance_a0
    label: "TRANSACTIONAL TOOL"

  - id: stage_assistant
    position: [580, 350]
    size: [280, 180]
    role: assurance_a1
    label: "HELPFUL ASSISTANT"

  - id: stage_advisor
    position: [920, 350]
    size: [280, 180]
    role: confidence_high
    label: "TRUSTED ADVISOR"

  - id: stage_companion
    position: [1260, 350]
    size: [280, 180]
    role: confidence_low
    label: "EMOTIONAL COMPANION"

  - id: stage_parasocial
    position: [1600, 350]
    size: [280, 180]
    role: problem_statement
    label: "PARASOCIAL BOND"

  - id: target_marker
    position: [920, 220]
    size: [280, 40]
    role: selected_option
    label: "DESIGN TARGET"

  - id: danger_marker
    position: [1430, 220]
    size: [560, 40]
    role: problem_statement
    label: "DANGER ZONE"

  - id: flow_spectrum
    from: stage_transactional
    to: stage_parasocial
    type: arrow
    label: "increasing relationship depth"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "PARASOCIAL BOND SPECTRUM" with accent square |
| Transactional Tool | `assurance_a0` | Minimal relationship -- pure utility, no personality |
| Helpful Assistant | `assurance_a1` | Polite, responsive, but no persistent identity |
| Trusted Advisor | `confidence_high` | TARGET -- warm, competent, remembered context, reliable |
| Emotional Companion | `confidence_low` | DANGER -- user forms emotional attachment |
| Parasocial Bond | `problem_statement` | CRITICAL DANGER -- user treats AI as real relationship |
| Target marker | `selected_option` | Highlights "Trusted Advisor" as the design goal |
| Danger zone marker | `problem_statement` | Marks "Emotional Companion" and "Parasocial Bond" as forbidden |
| Guardrails list | `security_layer` | Session limits, dependency detection, AI Chaperones, reminders |
| Callout bar | `callout_bar` | Design for Trusted Advisor, guard against parasocial dependency |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Transactional Tool | Helpful Assistant | arrow | "increasing depth" |
| Helpful Assistant | Trusted Advisor | arrow | "increasing depth" |
| Trusted Advisor | Emotional Companion | dashed | "boundary -- guard here" |
| Emotional Companion | Parasocial Bond | arrow | "escalation risk" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "DESIGN TARGET" | Trusted Advisor -- warm enough to sustain engagement, competent enough to be reliable for music attribution | center-top |
| "GUARDRAILS" | Session limits, dependency detection, AI Chaperones, explicit AI reminders prevent rightward drift | bottom-left |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "TRANSACTIONAL TOOL"
- Label 2: "HELPFUL ASSISTANT"
- Label 3: "TRUSTED ADVISOR"
- Label 4: "EMOTIONAL COMPANION"
- Label 5: "PARASOCIAL BOND"
- Label 6: "DESIGN TARGET"
- Label 7: "DANGER ZONE"
- Label 8: "Session time limits"
- Label 9: "Dependency detection"
- Label 10: "AI Chaperones"
- Label 11: "AI identity reminders"

### Caption (for embedding in documentation)

Parasocial bond spectrum showing five stages of human-AI relationship depth from Transactional Tool to Parasocial Bond, with the music attribution agent targeting "Trusted Advisor" and guardrails (session limits, dependency detection, AI Chaperones) preventing progression into dangerous emotional dependency.

## Anti-Hallucination Rules

These are INTERNAL instructions for prompt construction. They MUST NEVER appear as visible text in the generated image.

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `assurance_a0`, `confidence_high`, `problem_statement` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear. This is L1 -- use plain business language.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. Exactly 5 stages on the spectrum -- do NOT add or remove stages.
10. "Trusted Advisor" is the target -- it MUST be visually highlighted as the recommended zone.
11. "Emotional Companion" and "Parasocial Bond" are the danger zone -- they MUST be visually distinct as warnings.
12. The boundary between "Trusted Advisor" and "Emotional Companion" is the critical design line.
13. "AI Chaperones" is a specific concept (meta-agents monitoring relationship health) -- do NOT simplify to generic "monitoring."
14. Do NOT imply the spectrum is a slider users control -- it describes emergent relationship dynamics.
15. The guardrails are preventive mechanisms, not reactive interventions.
16. This is L1 -- use "how sure" language, avoid "confidence scores" or "assurance tiers."

## Alt Text

Parasocial bond spectrum for music attribution agents showing five stages from Transactional Tool through Helpful Assistant to Trusted Advisor design target, with guardrails including session limits, dependency detection, and AI Chaperones preventing progression into dangerous emotional dependency

## Image Embed

![Parasocial bond spectrum for music attribution agents showing five stages from Transactional Tool through Helpful Assistant to Trusted Advisor design target, with guardrails including session limits, dependency detection, and AI Chaperones preventing progression into dangerous emotional dependency](docs/figures/repo-figures/assets/fig-persona-24-parasocial-bond-spectrum.jpg)

*Parasocial bond spectrum showing five stages of human-AI relationship depth from Transactional Tool to Parasocial Bond, with the music attribution agent targeting "Trusted Advisor" and guardrails (session limits, dependency detection, AI Chaperones) preventing progression into dangerous emotional dependency.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "persona-24",
    "title": "Parasocial Bond Spectrum",
    "audience": "L1",
    "layout_template": "E"
  },
  "content_architecture": {
    "primary_message": "Design for Trusted Advisor, guard against parasocial dependency with session limits, dependency detection, and AI Chaperones.",
    "layout_flow": "left-to-right",
    "key_structures": [
      {
        "name": "Transactional Tool",
        "role": "assurance_a0",
        "is_highlighted": false,
        "labels": ["TRANSACTIONAL TOOL"]
      },
      {
        "name": "Helpful Assistant",
        "role": "assurance_a1",
        "is_highlighted": false,
        "labels": ["HELPFUL ASSISTANT"]
      },
      {
        "name": "Trusted Advisor",
        "role": "confidence_high",
        "is_highlighted": true,
        "labels": ["TRUSTED ADVISOR", "DESIGN TARGET"]
      },
      {
        "name": "Emotional Companion",
        "role": "confidence_low",
        "is_highlighted": false,
        "labels": ["EMOTIONAL COMPANION", "DANGER ZONE"]
      },
      {
        "name": "Parasocial Bond",
        "role": "problem_statement",
        "is_highlighted": false,
        "labels": ["PARASOCIAL BOND", "DANGER ZONE"]
      }
    ],
    "relationships": [
      {
        "from": "Transactional Tool",
        "to": "Helpful Assistant",
        "type": "arrow",
        "label": "increasing depth"
      },
      {
        "from": "Helpful Assistant",
        "to": "Trusted Advisor",
        "type": "arrow",
        "label": "increasing depth"
      },
      {
        "from": "Trusted Advisor",
        "to": "Emotional Companion",
        "type": "dashed",
        "label": "boundary -- guard here"
      },
      {
        "from": "Emotional Companion",
        "to": "Parasocial Bond",
        "type": "arrow",
        "label": "escalation risk"
      }
    ],
    "callout_boxes": [
      {
        "heading": "DESIGN TARGET",
        "body_text": "Trusted Advisor -- warm, competent, remembered context, reliable for music attribution",
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
- [x] Audience level correct (L1)
- [x] Layout template identified (E)

## Status

- [x] Draft created
- [ ] Content reviewed
- [x] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
