# fig-voice-41: Memory Integration: Letta + Mem0

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-voice-41 |
| **Title** | Memory Integration: Letta + Mem0 |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/tutorials/voice-agent-implementation.md, Section 8.3-8.4 |
| **Priority** | P1 (Important) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | D (Split-Panel) |

## Purpose

Show Letta (read-only persona block + mutable human block) and Mem0 (category-level prefs + safety gate) side by side, with how both feed into build_system_prompt(). Answers: "How do two complementary memory systems combine to produce the voice agent's system prompt?"

## Key Message

Two memory systems with complementary roles: Letta anchors the persona (immutable persona block + mutable user memory), Mem0 tracks user preferences (category-level only, with a safety gate filtering claims that contradict factual data). Both feed context into build_system_prompt().

## Visual Concept

Split-panel (Template D). Left: "LETTA (MemGPT)" showing persona block (read-only, locked icon) and human block (mutable, unlocked icon). Right: "MEM0" showing category preferences (e.g., "prefers detailed explanations") and safety gate (with _UNSAFE_PATTERNS blocking claims like "I wrote that song"). Center: both converge into build_system_prompt() which outputs the assembled system prompt.

```
+-------------------------------------------------------------------+
|  MEMORY INTEGRATION: LETTA + MEM0                          [sq]    |
|  -- Complementary Memory for Voice Persona                         |
+-------------------------------------------------------------------+
|                          |                                         |
|   LETTA (MemGPT)        |        MEM0                              |
|   ──────────────         |        ────                              |
|                          |                                         |
|   [lock] PERSONA BLOCK   |   CATEGORY PREFERENCES                  |
|   Core identity          |   "prefers detailed explanations"        |
|   ALWAYS immutable       |   "focuses on songwriter credits"        |
|                          |                                         |
|   [unlock] HUMAN BLOCK   |   SAFETY GATE                           |
|   User expertise/prefs   |   apply_safety_gate()                   |
|   Updated per session    |   _UNSAFE_PATTERNS                      |
|                          |   Blocks: "I wrote that song"            |
|   get_user_context()     |                                         |
|   Falls back to ""       |   NO fine-grained facts                  |
|                          |   (PS-Bench: 244% attack surface)        |
|          \               |              /                           |
|           \              |             /                            |
|            +---> build_system_prompt() <---+                        |
|                    |                                                |
|              [ASSEMBLED SYSTEM PROMPT]                              |
|                                                                    |
+-------------------------------------------------------------------+
|  ELI5: Letta = permanent bio + personal notepad.            [sq]   |
|  Mem0 = studio whiteboard with a bouncer.                          |
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
    content: "MEMORY INTEGRATION: LETTA + MEM0"
    role: title

  - id: left_panel
    bounds: [40, 140, 900, 680]
    content: "LETTA (MemGPT)"
    role: content_area

  - id: right_panel
    bounds: [980, 140, 900, 680]
    content: "MEM0"
    role: content_area

  - id: convergence_zone
    bounds: [660, 740, 600, 120]
    role: processing_stage

  - id: eli5_callout
    bounds: [40, 920, 1840, 120]
    role: callout_box

anchors:
  - id: letta_heading
    position: [460, 180]
    size: [400, 50]
    role: heading_display
    label: "LETTA (MemGPT)"

  - id: persona_block
    position: [460, 300]
    size: [360, 100]
    role: security_layer
    label: "PERSONA BLOCK"

  - id: lock_icon
    position: [240, 300]
    size: [40, 40]
    role: security_layer
    label: "locked"

  - id: human_block
    position: [460, 460]
    size: [360, 100]
    role: data_flow
    label: "HUMAN BLOCK"

  - id: unlock_icon
    position: [240, 460]
    size: [40, 40]
    role: data_flow
    label: "unlocked"

  - id: get_user_context
    position: [460, 600]
    size: [300, 40]
    role: data_flow
    label: "get_user_context()"

  - id: mem0_heading
    position: [1440, 180]
    size: [400, 50]
    role: heading_display
    label: "MEM0"

  - id: category_prefs
    position: [1440, 300]
    size: [360, 100]
    role: data_flow
    label: "CATEGORY PREFERENCES"

  - id: safety_gate
    position: [1440, 460]
    size: [360, 120]
    role: security_layer
    label: "SAFETY GATE"

  - id: no_fine_grained
    position: [1440, 620]
    size: [360, 50]
    role: security_layer
    label: "NO fine-grained facts"

  - id: build_system_prompt
    position: [960, 780]
    size: [360, 60]
    role: processing_stage
    label: "build_system_prompt()"

  - id: assembled_prompt
    position: [960, 860]
    size: [360, 40]
    role: data_flow
    label: "ASSEMBLED SYSTEM PROMPT"

  - id: panel_divider
    position: [960, 140]
    size: [2, 580]
    role: accent_line_v

  - id: letta_to_convergence
    from: get_user_context
    to: build_system_prompt
    type: arrow
    label: "persona + user memory"

  - id: mem0_to_convergence
    from: no_fine_grained
    to: build_system_prompt
    type: arrow
    label: "filtered preferences"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Letta panel | `content_area` | Left panel: Letta/MemGPT persona and human memory blocks |
| Persona block | `security_layer` | Read-only core identity -- ALWAYS immutable, locked icon |
| Human block | `data_flow` | Mutable user expertise/preferences, updated per session |
| get_user_context() | `data_flow` | Retrieves user memory, falls back to "" if unavailable |
| Mem0 panel | `content_area` | Right panel: Mem0 category preferences and safety gate |
| Category preferences | `data_flow` | "prefers detailed explanations", "focuses on songwriter credits" |
| Safety gate | `security_layer` | apply_safety_gate() with _UNSAFE_PATTERNS regex filter |
| No fine-grained facts | `security_layer` | Deliberately omits fine-grained facts (PS-Bench: 244% attack surface) |
| build_system_prompt() | `processing_stage` | Convergence point assembling both memory sources into prompt |
| Panel divider | `accent_line_v` | Vertical coral accent line separating Letta and Mem0 panels |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Persona block | build_system_prompt() | arrow | "immutable identity context" |
| Human block | build_system_prompt() | arrow | "mutable user context" |
| Category preferences | Safety gate | arrow | "raw preferences" |
| Safety gate | build_system_prompt() | arrow | "filtered preferences" |
| build_system_prompt() | Assembled prompt | arrow | "output" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "ELI5" | Letta is like a musician's permanent bio that never changes, plus a personal notepad about what each collaborator likes. Mem0 is like a studio whiteboard where you track each client's preferences -- but with a bouncer who erases anything that contradicts the master credits sheet. | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "LETTA (MemGPT)"
- Label 2: "MEM0"
- Label 3: "PERSONA BLOCK"
- Label 4: "HUMAN BLOCK"
- Label 5: "CATEGORY PREFERENCES"
- Label 6: "SAFETY GATE"
- Label 7: "build_system_prompt()"
- Label 8: "ASSEMBLED SYSTEM PROMPT"
- Label 9: "get_user_context()"
- Label 10: "apply_safety_gate()"
- Label 11: "_UNSAFE_PATTERNS"
- Label 12: "ALWAYS immutable"
- Label 13: "Updated per session"
- Label 14: "NO fine-grained facts"

### Caption (for embedding in documentation)

Split-panel view of Letta and Mem0 memory systems showing how immutable persona blocks (Letta) and safety-gated category preferences (Mem0) converge into build_system_prompt() to produce the voice agent's assembled system prompt.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `processing_stage`, `security_layer`, `data_flow` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon is ALLOWED** -- this is an L3 figure. Letta, MemGPT, Mem0, build_system_prompt(), _UNSAFE_PATTERNS are appropriate.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption.
8. **No prompt leakage** -- do NOT render style keywords as visible text in the figure.

### Figure-Specific Rules

9. Letta persona block must be visually locked/immutable -- never shown as writable.
10. Mem0 safety gate must be shown as an active filter, not just a passive check.
11. The convergence point must be build_system_prompt(), not any other function.
12. Do NOT show database schemas -- only the conceptual memory model.

## Alt Text

Split-panel: Letta persona+human blocks and Mem0 safety-gated preferences converge into build_system_prompt() for voice agent context.

## Image Embed

![Split-panel: Letta persona+human blocks and Mem0 safety-gated preferences converge into build_system_prompt() for voice agent context.](docs/figures/repo-figures/assets/fig-voice-41-memory-integration-letta-mem0.jpg)

*Split-panel view of Letta and Mem0 memory systems showing how immutable persona blocks (Letta) and safety-gated category preferences (Mem0) converge into build_system_prompt() to produce the voice agent's assembled system prompt.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "voice-41",
    "title": "Memory Integration: Letta + Mem0",
    "audience": "L3",
    "layout_template": "D"
  },
  "content_architecture": {
    "primary_message": "Two complementary memory systems -- Letta (immutable persona + mutable user context) and Mem0 (category preferences + safety gate) -- converge into build_system_prompt().",
    "layout_flow": "left-right-to-center",
    "key_structures": [
      {
        "name": "Letta Persona Block",
        "role": "security_layer",
        "is_highlighted": true,
        "labels": ["PERSONA BLOCK", "ALWAYS immutable"]
      },
      {
        "name": "Letta Human Block",
        "role": "data_flow",
        "is_highlighted": false,
        "labels": ["HUMAN BLOCK", "Updated per session"]
      },
      {
        "name": "Mem0 Category Preferences",
        "role": "data_flow",
        "is_highlighted": false,
        "labels": ["CATEGORY PREFERENCES"]
      },
      {
        "name": "Mem0 Safety Gate",
        "role": "security_layer",
        "is_highlighted": true,
        "labels": ["SAFETY GATE", "apply_safety_gate()"]
      },
      {
        "name": "build_system_prompt()",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["build_system_prompt()", "ASSEMBLED SYSTEM PROMPT"]
      }
    ],
    "relationships": [
      {"from": "Persona Block", "to": "build_system_prompt()", "type": "arrow", "label": "immutable identity context"},
      {"from": "Human Block", "to": "build_system_prompt()", "type": "arrow", "label": "mutable user context"},
      {"from": "Category Preferences", "to": "Safety Gate", "type": "arrow", "label": "raw preferences"},
      {"from": "Safety Gate", "to": "build_system_prompt()", "type": "arrow", "label": "filtered preferences"}
    ],
    "callout_boxes": [
      {
        "heading": "ELI5",
        "body_text": "Letta is like a musician's permanent bio that never changes, plus a personal notepad about what each collaborator likes. Mem0 is like a studio whiteboard where you track each client's preferences -- but with a bouncer who erases anything that contradicts the master credits sheet.",
        "position": "bottom-center"
      }
    ]
  }
}
```

## Quality Checklist

- [ ] Primary message clear in one sentence
- [ ] Semantic tags used (no colors, hex codes, or font names in content spec)
- [ ] ASCII layout sketched
- [ ] Spatial anchors defined in YAML
- [ ] Labels under 30 characters
- [ ] Anti-hallucination rules listed (8 default + 4 figure-specific)
- [ ] Alt text provided (125 chars max)
- [ ] JSON export block included
- [ ] Audience level correct (L3)
- [ ] Layout template identified (D)

## Status

- [ ] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
