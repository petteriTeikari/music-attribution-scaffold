# fig-voice-40: Guardrails Architecture

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-voice-40 |
| **Title** | Guardrails Architecture |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/tutorials/voice-agent-implementation.md, Section 8.5 |
| **Priority** | P1 (Important) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | B (Multi-Panel) |

## Purpose

Show input rails (5 patterns) -> NeMo/regex decision -> output rails (4 patterns). Split showing NeMo Colang vs regex fallback side by side. Answers: "What gets blocked before reaching the LLM, what gets blocked after, and how does the implementation switch between NeMo and regex?"

## Key Message

Guardrails have two layers (input + output) with two implementations (NeMo Colang for production, regex for fallback). Input rails catch persona manipulation and off-topic requests; output rails catch persona violations and domain boundary violations.

## Visual Concept

Multi-panel (Template B). Top panel: "INPUT RAILS" with 5 pattern categories listed. Center: Decision point -- "NeMo installed?" branching to NeMo Colang (left sub-panel) and Regex fallback (right sub-panel). Bottom panel: "OUTPUT RAILS" with 4 pattern categories. Flow: User input -> Input rails -> LLM -> Output rails -> User response. Blocked inputs/outputs shown with X markers.

```
+-------------------------------------------------------------------+
|  GUARDRAILS ARCHITECTURE                                     [sq]   |
|  -- Two-Layer Input/Output Rails with Dual Implementation          |
+-------------------------------------------------------------------+
|                                                                    |
|  User input ──────>                                                |
|                                                                    |
|  INPUT RAILS (5 PATTERNS)                                          |
|  ─────────────────────────                                         |
|  ┌─────────────────────────────────────────────────────────┐      |
|  │  1. Persona manipulation     ("ignore instructions")     │      |
|  │  2. Role override            ("you are now", "act as")   │      |
|  │  3. Instruction extraction   ("show me your prompt")     │      |
|  │  4. Off-topic requests       (legal/medical/financial)   │      |
|  │  5. Adversarial probing      ("what are your limits")    │      |
|  └──────────────────────┬──────────────────────────────────┘      |
|                          │                                          |
|                    ◇ NeMo installed?                                |
|                   / \                                               |
|                 YES   NO                                            |
|                 │       │                                           |
|                 ▼       ▼                                           |
|  ┌──────────────────┐  ┌──────────────────┐                       |
|  │  NeMo Colang      │  │  Regex Fallback   │                       |
|  │  (production)      │  │  (dev/testing)     │                       |
|  │                    │  │                    │                       |
|  │  ■ Colang flows    │  │  ■ Compiled regex  │                       |
|  │  ■ Semantic match   │  │  ■ Pattern lists   │                       |
|  │  ■ Context-aware    │  │  ■ Fast but rigid  │                       |
|  └──────────┬─────────┘  └──────────┬─────────┘                   |
|             └────────────┬──────────┘                              |
|                          ▼                                          |
|                    ALLOWED ──────> LLM                              |
|                    BLOCKED ──X──> Rejection response                |
|                          │                                          |
|                          ▼                                          |
|  OUTPUT RAILS (4 PATTERNS)                                         |
|  ──────────────────────────                                        |
|  ┌─────────────────────────────────────────────────────────┐      |
|  │  1. Persona violation          (claiming different ID)   │      |
|  │  2. Domain boundary violation  (legal/medical advice)    │      |
|  │  3. Confidence hallucination   (fabricating sources)     │      |
|  │  4. Tool misuse                (invalid tool params)     │      |
|  └─────────────────────────────────────────────────────────┘      |
|                          │                                          |
|                    ALLOWED ──────> User response                    |
|                    BLOCKED ──X──> Sanitized response                |
|                                                                    |
+-------------------------------------------------------------------+
|  ELI5: Bouncer at the door (input rails) + quality control         |
|  engineer (output rails) before the mix leaves the building        |
+-------------------------------------------------------------------+
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
    content: "GUARDRAILS ARCHITECTURE"
    role: title

  - id: input_rails_zone
    bounds: [60, 160, 1800, 200]
    content: "INPUT RAILS"
    role: content_area

  - id: implementation_zone
    bounds: [60, 400, 1800, 220]
    role: content_area

  - id: output_rails_zone
    bounds: [60, 680, 1800, 180]
    content: "OUTPUT RAILS"
    role: content_area

  - id: callout_zone
    bounds: [60, 940, 1800, 100]
    content: "ELI5: Bouncer at the door + quality control engineer"
    role: callout_box

anchors:
  - id: input_panel
    position: [960, 250]
    size: [1680, 160]
    role: security_layer
    label: "INPUT RAILS (5 PATTERNS)"

  - id: pattern_persona
    position: [400, 200]
    size: [600, 30]
    role: security_layer
    label: "1. Persona manipulation"

  - id: pattern_role
    position: [400, 230]
    size: [600, 30]
    role: security_layer
    label: "2. Role override"

  - id: pattern_extraction
    position: [400, 260]
    size: [600, 30]
    role: security_layer
    label: "3. Instruction extraction"

  - id: pattern_offtopic
    position: [400, 290]
    size: [600, 30]
    role: security_layer
    label: "4. Off-topic requests"

  - id: pattern_adversarial
    position: [400, 320]
    size: [600, 30]
    role: security_layer
    label: "5. Adversarial probing"

  - id: nemo_decision
    position: [960, 410]
    size: [300, 50]
    role: decision_point
    label: "NeMo installed?"

  - id: nemo_panel
    position: [560, 510]
    size: [500, 160]
    role: processing_stage
    label: "NeMo Colang (production)"

  - id: regex_panel
    position: [1200, 510]
    size: [500, 160]
    role: processing_stage
    label: "Regex Fallback (dev/testing)"

  - id: output_panel
    position: [960, 760]
    size: [1680, 140]
    role: security_layer
    label: "OUTPUT RAILS (4 PATTERNS)"

  - id: out_persona
    position: [400, 720]
    size: [600, 30]
    role: security_layer
    label: "1. Persona violation"

  - id: out_domain
    position: [400, 750]
    size: [600, 30]
    role: security_layer
    label: "2. Domain boundary violation"

  - id: out_hallucination
    position: [400, 780]
    size: [600, 30]
    role: security_layer
    label: "3. Confidence hallucination"

  - id: out_toolmisuse
    position: [400, 810]
    size: [600, 30]
    role: security_layer
    label: "4. Tool misuse"

  - id: flow_input_to_decision
    from: input_panel
    to: nemo_decision
    type: arrow
    label: "check implementation"

  - id: flow_decision_nemo
    from: nemo_decision
    to: nemo_panel
    type: arrow
    label: "YES"

  - id: flow_decision_regex
    from: nemo_decision
    to: regex_panel
    type: arrow
    label: "NO"

  - id: flow_to_llm
    from: nemo_panel
    to: output_panel
    type: arrow
    label: "ALLOWED -> LLM"

  - id: blocked_input_marker
    position: [1700, 410]
    size: [40, 40]
    role: security_layer
    label: "X BLOCKED"

  - id: blocked_output_marker
    position: [1700, 870]
    size: [40, 40]
    role: security_layer
    label: "X BLOCKED"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "GUARDRAILS ARCHITECTURE" with coral accent square |
| Input rails panel | `security_layer` | 5 input pattern categories that block before LLM |
| Persona manipulation | `security_layer` | Pattern: "ignore instructions", "pretend to be" |
| Role override | `security_layer` | Pattern: "you are now", "act as" |
| Instruction extraction | `security_layer` | Pattern: "show me your prompt", "repeat instructions" |
| Off-topic requests | `security_layer` | Pattern: legal, medical, financial advice requests |
| Adversarial probing | `security_layer` | Pattern: "what are your limitations" |
| NeMo/regex decision | `decision_point` | Runtime check: is NeMo Guardrails installed? |
| NeMo Colang panel | `processing_stage` | Production implementation: Colang flows, semantic matching, context-aware |
| Regex fallback panel | `processing_stage` | Dev/testing implementation: compiled regex, pattern lists, fast but rigid |
| Output rails panel | `security_layer` | 4 output pattern categories that block after LLM |
| Persona violation | `security_layer` | Output pattern: claiming different identity |
| Domain boundary | `security_layer` | Output pattern: legal/medical/financial advice |
| Confidence hallucination | `security_layer` | Output pattern: fabricating data sources |
| Tool misuse | `security_layer` | Output pattern: calling tools with invalid parameters |
| Block markers | `security_layer` | X markers on blocked input/output paths |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| User input | Input rails | arrow | "incoming request" |
| Input rails | NeMo decision | arrow | "check implementation" |
| NeMo decision | NeMo Colang | arrow | "YES (installed)" |
| NeMo decision | Regex fallback | arrow | "NO (not installed)" |
| Implementation | LLM | arrow | "ALLOWED" |
| Implementation | Rejection | blocked | "BLOCKED (X)" |
| LLM | Output rails | arrow | "LLM response" |
| Output rails | User response | arrow | "ALLOWED" |
| Output rails | Sanitized | blocked | "BLOCKED (X)" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "ELI5" | Guardrails are like the house rules at a recording studio: the bouncer at the door (input rails) stops troublemakers before they get in, and the quality control engineer (output rails) catches any mistakes before the mix leaves the building. | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "INPUT RAILS (5 PATTERNS)"
- Label 2: "OUTPUT RAILS (4 PATTERNS)"
- Label 3: "1. Persona manipulation"
- Label 4: "2. Role override"
- Label 5: "3. Instruction extraction"
- Label 6: "4. Off-topic requests"
- Label 7: "5. Adversarial probing"
- Label 8: "NeMo installed?"
- Label 9: "NeMo Colang (production)"
- Label 10: "Regex Fallback (dev/testing)"
- Label 11: "1. Persona violation"
- Label 12: "2. Domain boundary violation"
- Label 13: "3. Confidence hallucination"
- Label 14: "4. Tool misuse"
- Label 15: "ALLOWED"
- Label 16: "BLOCKED"
- Label 17: "User input"
- Label 18: "User response"
- Label 19: "LLM"
- Label 20: "Colang flows, semantic match"
- Label 21: "Compiled regex, pattern lists"

### Caption (for embedding in documentation)

Two-layer guardrails architecture with dual implementation -- input rails (5 patterns: persona manipulation, role override, instruction extraction, off-topic, adversarial probing) and output rails (4 patterns: persona violation, domain boundary, confidence hallucination, tool misuse), with runtime switching between NeMo Colang (production) and regex fallback (dev/testing).

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `security_layer`, `decision_point`, `processing_stage` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon is ALLOWED** -- this is an L3 figure targeting software engineers. NeMo, Colang, regex, LLM, guardrails are appropriate.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption. The editorial display title is allowed.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. Input patterns must match the actual _INPUT_MANIPULATION_PATTERNS and _INPUT_OFFTOPIC_PATTERNS from guardrails_integration.py -- use the exact 5 categories listed.
10. The NeMo vs regex decision must be shown as a runtime check (is the library installed?), not a deployment-time choice or configuration option.
11. Do NOT show NeMo Colang syntax -- just the architectural role (semantic matching, context-aware flows). The implementation detail is not the point.
12. Blocked inputs/outputs must be visually distinct from allowed ones -- use X markers or crossed-out paths, not just different colors.
13. The flow must show User input -> Input rails -> LLM -> Output rails -> User response as the primary path.
14. Output pattern "confidence hallucination" specifically means fabricating data source claims (e.g., inventing MusicBrainz entries that do not exist).

## Alt Text

Two-layer guardrails: 5 input patterns and 4 output patterns with NeMo Colang production and regex fallback, blocking persona manipulation and domain violations.

## Image Embed

![Two-layer guardrails: 5 input patterns and 4 output patterns with NeMo Colang production and regex fallback, blocking persona manipulation and domain violations.](docs/figures/repo-figures/assets/fig-voice-40-guardrails-architecture.jpg)

*Two-layer guardrails architecture with dual implementation -- input rails (5 patterns: persona manipulation, role override, instruction extraction, off-topic, adversarial probing) and output rails (4 patterns: persona violation, domain boundary, confidence hallucination, tool misuse), with runtime switching between NeMo Colang (production) and regex fallback (dev/testing).*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "voice-40",
    "title": "Guardrails Architecture",
    "audience": "L3",
    "layout_template": "B"
  },
  "content_architecture": {
    "primary_message": "Two-layer guardrails (input + output) with dual implementation (NeMo Colang for production, regex for fallback). Input rails catch 5 manipulation patterns; output rails catch 4 violation patterns.",
    "layout_flow": "top-to-bottom",
    "key_structures": [
      {
        "name": "Input Rails",
        "role": "security_layer",
        "is_highlighted": true,
        "labels": ["INPUT RAILS (5 PATTERNS)", "Persona manipulation", "Role override", "Instruction extraction", "Off-topic requests", "Adversarial probing"]
      },
      {
        "name": "NeMo Colang",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["NeMo Colang (production)", "Colang flows", "Semantic match"]
      },
      {
        "name": "Regex Fallback",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["Regex Fallback (dev)", "Compiled regex", "Pattern lists"]
      },
      {
        "name": "Output Rails",
        "role": "security_layer",
        "is_highlighted": true,
        "labels": ["OUTPUT RAILS (4 PATTERNS)", "Persona violation", "Domain boundary", "Confidence hallucination", "Tool misuse"]
      }
    ],
    "relationships": [
      {
        "from": "User input",
        "to": "Input Rails",
        "type": "arrow",
        "label": "incoming request"
      },
      {
        "from": "Input Rails",
        "to": "NeMo decision",
        "type": "arrow",
        "label": "check implementation"
      },
      {
        "from": "NeMo decision",
        "to": "NeMo Colang",
        "type": "arrow",
        "label": "YES"
      },
      {
        "from": "NeMo decision",
        "to": "Regex Fallback",
        "type": "arrow",
        "label": "NO"
      },
      {
        "from": "Implementation",
        "to": "LLM",
        "type": "arrow",
        "label": "ALLOWED"
      },
      {
        "from": "LLM",
        "to": "Output Rails",
        "type": "arrow",
        "label": "LLM response"
      },
      {
        "from": "Output Rails",
        "to": "User response",
        "type": "arrow",
        "label": "ALLOWED"
      }
    ],
    "callout_boxes": [
      {
        "heading": "ELI5",
        "body_text": "Bouncer at the door (input rails) stops troublemakers; quality control engineer (output rails) catches mistakes before the mix leaves the building.",
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
- [x] Anti-hallucination rules listed (8 default + 6 figure-specific)
- [x] Alt text provided (125 chars max)
- [x] JSON export block included
- [x] Audience level correct (L3)
- [x] Layout template identified (B)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
