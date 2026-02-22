# fig-persona-26: Brand Voice Validation Pipeline

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-persona-26 |
| **Title** | Brand Voice Validation -- Deterministic Last-Mile Guardrail |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/architecture/persona.md, docs/planning/ |
| **Priority** | P2 (Medium) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | D (Split-Panel) |

## Purpose

Shows the two-stage response pipeline where an LLM generates a candidate response (left panel) and a deterministic brand voice validator catches violations before delivery (right panel). Answers: "Why do we need a deterministic post-LLM filter, and what violation patterns does it catch?"

## Key Message

A deterministic regex + rule-based validator sits between the LLM output and the user, catching brand voice violations (multiple exclamation marks, emojis, corporate jargon, cold rejections) that LLM guardrails alone miss -- providing a reliable last-mile defense for persona consistency.

## Visual Concept

Split-panel layout. Left panel shows the LLM generating a candidate response with potential violations highlighted. Right panel shows the brand voice validator with a pass/fail gate. Violation patterns are listed as rules. An arrow flows from left to right through the validator gate to the user. Failed responses are shown being caught and corrected.

```
+---------------------------------------------------------------+
|  BRAND VOICE VALIDATION                                        |
+---------------------------------------------------------------+
|                                                                |
|  LEFT: LLM RESPONSE          RIGHT: BRAND VOICE VALIDATOR     |
|                                                                |
|  ┌──────────────────┐       ┌──────────────────────────┐      |
|  │  LLM generates   │       │  DETERMINISTIC VALIDATOR  │      |
|  │  candidate        │       │  (regex + rule-based)     │      |
|  │  response         │       │                          │      |
|  │                   │       │  VIOLATION PATTERNS:      │      |
|  │  ┌─────────────┐ │       │  ╳ Multiple !! or !!!    │      |
|  │  │ "Great       │ │──────>│  ╳ Emojis in response    │      |
|  │  │  news!!!"    │ │       │  ╳ Corporate jargon      │      |
|  │  │  🎵         │ │       │    ("synergize",          │      |
|  │  │ "Let's       │ │       │     "leverage")           │      |
|  │  │  synergize   │ │       │  ╳ Cold rejections       │      |
|  │  │  on this"    │ │       │    ("I cannot help")      │      |
|  │  └─────────────┘ │       │                          │      |
|  │                   │       │  ┌────────┐ ┌────────┐  │      |
|  └──────────────────┘       │  │  PASS  │ │  FAIL  │  │      |
|                              │  │  ────> │ │  ────> │  │      |
|                              │  │ deliver│ │ correct│  │      |
|                              │  │ to user│ │ & retry│  │      |
|                              │  └────────┘ └────────┘  │      |
|                              └──────────────────────────┘      |
|                                                                |
+---------------------------------------------------------------+
|  DETERMINISTIC VALIDATORS CATCH WHAT LLM GUARDRAILS MISS       |
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
    content: "BRAND VOICE VALIDATION"
    role: title

  - id: left_panel
    bounds: [80, 160, 800, 700]
    role: content_area

  - id: right_panel
    bounds: [1000, 160, 840, 700]
    role: content_area

  - id: callout_zone
    bounds: [80, 920, 1760, 120]
    role: callout_box

anchors:
  - id: llm_generator
    position: [480, 360]
    size: [640, 300]
    role: processing_stage
    label: "LLM RESPONSE GENERATOR"

  - id: candidate_response
    position: [480, 600]
    size: [500, 200]
    role: confidence_medium
    label: "Candidate response (may contain violations)"

  - id: validator
    position: [1420, 360]
    size: [640, 500]
    role: security_layer
    label: "DETERMINISTIC VALIDATOR"

  - id: violation_list
    position: [1420, 500]
    size: [500, 200]
    role: problem_statement
    label: "Violation patterns"

  - id: pass_gate
    position: [1220, 740]
    size: [200, 100]
    role: confidence_high
    label: "PASS"

  - id: fail_gate
    position: [1520, 740]
    size: [200, 100]
    role: confidence_low
    label: "FAIL"

  - id: flow_llm_to_validator
    from: llm_generator
    to: validator
    type: arrow
    label: "candidate response"

  - id: flow_pass_to_user
    from: pass_gate
    to: user_delivery
    type: arrow
    label: "deliver to user"

  - id: flow_fail_to_correction
    from: fail_gate
    to: llm_generator
    type: dashed
    label: "correct & retry"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "BRAND VOICE VALIDATION" with accent square |
| LLM response generator | `processing_stage` | PydanticAI agent producing candidate response |
| Candidate response | `confidence_medium` | Raw LLM output that may contain voice violations |
| Deterministic validator | `security_layer` | Regex + rule-based post-processing filter |
| Violation patterns | `problem_statement` | Multiple !!, emojis, corporate jargon, cold rejections |
| Pass gate | `confidence_high` | Response passes validation -- deliver to user |
| Fail gate | `confidence_low` | Response fails validation -- correct and retry |
| Callout bar | `callout_bar` | Deterministic validators catch what LLM guardrails miss |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| LLM response generator | Deterministic validator | arrow | "candidate response" |
| Pass gate | User delivery | arrow | "deliver to user" |
| Fail gate | LLM response generator | dashed | "correct & retry" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "LAST-MILE DEFENSE" | Deterministic validators catch what LLM guardrails miss -- regex and rules are more reliable than prompt instructions for surface-level brand voice consistency | bottom-center |
| "VIOLATION PATTERNS" | Multiple exclamation marks, emojis, corporate jargon, cold rejections | right-panel |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "LLM RESPONSE GENERATOR"
- Label 2: "DETERMINISTIC VALIDATOR"
- Label 3: "regex + rule-based"
- Label 4: "Multiple !! or !!!"
- Label 5: "Emojis in response"
- Label 6: "Corporate jargon"
- Label 7: "Cold rejections"
- Label 8: "PASS -- deliver to user"
- Label 9: "FAIL -- correct & retry"
- Label 10: "candidate response"

### Caption (for embedding in documentation)

Brand voice validation pipeline showing a deterministic regex + rule-based validator as a last-mile guardrail between LLM output and user delivery, catching violation patterns (multiple exclamation marks, emojis, corporate jargon, cold rejections) that LLM guardrails alone miss.

## Anti-Hallucination Rules

These are INTERNAL instructions for prompt construction. They MUST NEVER appear as visible text in the generated image.

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `processing_stage`, `security_layer`, `confidence_high` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- This is L3 so PydanticAI, regex, rule-based ARE allowed.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. The validator is DETERMINISTIC (regex + rules), NOT another LLM -- this is the key architectural point.
10. Violation patterns are exactly: multiple exclamation marks, emojis, corporate jargon ("synergize", "leverage"), cold rejections ("I cannot help").
11. The fail path loops BACK to the LLM for correction -- it does NOT silently drop the response.
12. The pass/fail gate is binary -- there is no "partial pass" or confidence score here.
13. Do NOT confuse this with content safety filtering -- this is BRAND VOICE consistency.
14. "Deterministic last-mile" means this runs AFTER the LLM, not as a prompt prefix.
15. The example violations shown ("Great news!!!", emoji, "synergize") are illustrative -- the actual rule set is configurable.
16. Do NOT imply the validator replaces LLM prompt engineering -- it complements it.

## Alt Text

Brand voice validation pipeline showing a deterministic regex and rule-based validator as a last-mile guardrail between LLM output and user delivery, catching persona coherence violations like excessive punctuation, emojis, corporate jargon, and cold rejections in music attribution agents

## Image Embed

![Brand voice validation pipeline showing a deterministic regex and rule-based validator as a last-mile guardrail between LLM output and user delivery, catching persona coherence violations like excessive punctuation, emojis, corporate jargon, and cold rejections in music attribution agents](docs/figures/repo-figures/assets/fig-persona-26-brand-voice-validation.jpg)

*Brand voice validation pipeline showing a deterministic regex + rule-based validator as a last-mile guardrail between LLM output and user delivery, catching violation patterns (multiple exclamation marks, emojis, corporate jargon, cold rejections) that LLM guardrails alone miss.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "persona-26",
    "title": "Brand Voice Validation Pipeline",
    "audience": "L3",
    "layout_template": "D"
  },
  "content_architecture": {
    "primary_message": "A deterministic regex + rule-based validator catches brand voice violations that LLM guardrails miss, providing reliable last-mile persona consistency.",
    "layout_flow": "left-to-right",
    "key_structures": [
      {
        "name": "LLM Response Generator",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["LLM RESPONSE GENERATOR"]
      },
      {
        "name": "Candidate Response",
        "role": "confidence_medium",
        "is_highlighted": false,
        "labels": ["Candidate response"]
      },
      {
        "name": "Deterministic Validator",
        "role": "security_layer",
        "is_highlighted": true,
        "labels": ["DETERMINISTIC VALIDATOR", "regex + rule-based"]
      },
      {
        "name": "Pass Gate",
        "role": "confidence_high",
        "is_highlighted": false,
        "labels": ["PASS", "deliver to user"]
      },
      {
        "name": "Fail Gate",
        "role": "confidence_low",
        "is_highlighted": false,
        "labels": ["FAIL", "correct & retry"]
      }
    ],
    "relationships": [
      {
        "from": "LLM Response Generator",
        "to": "Deterministic Validator",
        "type": "arrow",
        "label": "candidate response"
      },
      {
        "from": "Pass Gate",
        "to": "User Delivery",
        "type": "arrow",
        "label": "deliver to user"
      },
      {
        "from": "Fail Gate",
        "to": "LLM Response Generator",
        "type": "dashed",
        "label": "correct & retry"
      }
    ],
    "callout_boxes": [
      {
        "heading": "LAST-MILE DEFENSE",
        "body_text": "Deterministic validators catch what LLM guardrails miss",
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
- [x] Layout template identified (D)

## Status

- [x] Draft created
- [ ] Content reviewed
- [x] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
