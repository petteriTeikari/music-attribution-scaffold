# fig-voice-05: Dual Persona Voice System

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-voice-05 |
| **Title** | Dual Persona Voice System |
| **Audience** | L2 (Technical Decision-Maker) |
| **Location** | docs/tutorials/voice-agent-implementation.md |
| **Priority** | P0 |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | D (Split-Panel) |

## Purpose

Show how a single voice pipeline branches into two distinct personas -- the Attribution Agent (system voice for gap-filling workflows) and the Digital Twin (artist voice clone for fan-facing interactions) -- gated by progressive consent levels. Answers: "How do voice personas work and what controls access to them?"

## Key Message

A shared voice pipeline serves two personas -- Attribution Agent and Digital Twin -- with consent levels (L1/L2/L3) gating which persona features are available.

## Visual Concept

Split-panel layout (Template D) with a shared pipeline strip at the top spanning full width. Below, the layout splits into two panels. Left panel: Attribution Agent persona -- system voice, gap-filling, structured queries, metadata correction. Right panel: Digital Twin persona -- artist voice clone, fan-facing, conversational, storytelling. Between the shared pipeline and the split panels, three horizontal consent gates (L1, L2, L3) act as progressive access barriers. L1 (basic metadata consent) enables the Attribution Agent. L2 (voice likeness consent) enables basic Digital Twin. L3 (full creative consent) enables full Digital Twin with improvisation. Coral accent squares mark the consent gate boundaries.

```
+---------------------------------------------------------------------+
|  DUAL PERSONA                                                [sq]   |
|  VOICE SYSTEM                                                       |
|                                                                     |
|  +---------------------------------------------------------------+  |
|  |  SHARED PIPELINE: Transport -> STT -> LLM -> TTS -> Out      |  |
|  +---------------------------------------------------------------+  |
|                              |                                      |
|         +--------------------+--------------------+                 |
|         |   CONSENT GATES                         |                 |
|    L1 --+-- basic metadata   --> [Attribution OK]  |                 |
|    L2 --+-- voice likeness   --> [Digital Twin OK] |                 |
|    L3 --+-- full creative    --> [Full Twin OK]    |                 |
|         +--------------------+--------------------+                 |
|                    |                    |                            |
|  +-----------------+--+  +--------------+-------------+             |
|  |  ATTRIBUTION       |  |  DIGITAL TWIN              |             |
|  |  AGENT              |  |                            |             |
|  |                     |  |  Artist voice clone         |             |
|  |  System voice       |  |  Fan-facing                 |             |
|  |  Gap-filling        |  |  Conversational             |             |
|  |  Metadata queries   |  |  Storytelling               |             |
|  |  Structured tasks   |  |  Creative responses         |             |
|  +---------------------+  +----------------------------+             |
|                                                                     |
|  CONSENT GATES PERSONA ACCESS                                [line] |
+---------------------------------------------------------------------+
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
    content: "DUAL PERSONA VOICE SYSTEM"
    role: title

  - id: shared_pipeline_zone
    bounds: [80, 140, 1760, 100]
    content: "Shared Pipeline"
    role: content_area

  - id: consent_gate_zone
    bounds: [80, 280, 1760, 200]
    content: "Consent Gates L1/L2/L3"
    role: security_layer

  - id: left_panel
    bounds: [80, 520, 840, 380]
    content: "Attribution Agent"
    role: content_area

  - id: right_panel
    bounds: [1000, 520, 840, 380]
    content: "Digital Twin"
    role: content_area

  - id: callout_zone
    bounds: [80, 940, 1760, 100]
    content: "CONSENT GATES PERSONA ACCESS"
    role: callout_box

anchors:
  - id: shared_pipeline
    position: [120, 160]
    size: [1680, 60]
    role: processing_stage
    label: "SHARED PIPELINE"

  - id: consent_l1
    position: [120, 300]
    size: [1680, 40]
    role: assurance_a1
    label: "L1 BASIC METADATA"

  - id: consent_l2
    position: [120, 360]
    size: [1680, 40]
    role: assurance_a2
    label: "L2 VOICE LIKENESS"

  - id: consent_l3
    position: [120, 420]
    size: [1680, 40]
    role: assurance_a3
    label: "L3 FULL CREATIVE"

  - id: attribution_agent
    position: [120, 540]
    size: [760, 340]
    role: persona_block
    label: "ATTRIBUTION AGENT"

  - id: digital_twin
    position: [1040, 540]
    size: [760, 340]
    role: persona_block
    label: "DIGITAL TWIN"

  - id: flow_pipeline_to_gates
    from: shared_pipeline
    to: consent_l1
    type: arrow
    label: "consent check"

  - id: flow_l1_to_attribution
    from: consent_l1
    to: attribution_agent
    type: arrow
    label: "L1 grants access"

  - id: flow_l2_to_twin
    from: consent_l2
    to: digital_twin
    type: arrow
    label: "L2 grants access"

  - id: flow_l3_to_full_twin
    from: consent_l3
    to: digital_twin
    type: arrow
    label: "L3 full features"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Shared Pipeline | `processing_stage` | Full voice pipeline shared by both personas: Transport -> STT -> LLM -> TTS -> Out |
| L1 Consent Gate | `assurance_a1` | Basic metadata consent -- enables Attribution Agent access |
| L2 Consent Gate | `assurance_a2` | Voice likeness consent -- enables basic Digital Twin |
| L3 Consent Gate | `assurance_a3` | Full creative consent -- enables Digital Twin with improvisation |
| Attribution Agent | `persona_block` | System voice persona for gap-filling, metadata queries, structured tasks |
| Digital Twin | `persona_block` | Artist voice clone persona for fan-facing, conversational, storytelling use |

### Relationships / Flows

| From | To | Type | Label |
|------|----|------|-------|
| Shared Pipeline | Consent Gates | arrow | "consent check" |
| L1 Gate | Attribution Agent | arrow | "basic metadata grants access" |
| L2 Gate | Digital Twin | arrow | "voice likeness grants access" |
| L3 Gate | Digital Twin | arrow | "full creative enables all" |
| Attribution Agent | Shared Pipeline | dashed | "results feed back" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "CONSENT GATES PERSONA ACCESS" | Artist consent level determines which voice persona features are available. L1 (metadata) enables the Attribution Agent. L2 (voice likeness) enables the Digital Twin with scripted responses. L3 (full creative) enables improvisation and conversational storytelling. | bottom-full-width |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "SHARED PIPELINE"
- Label 2: "ATTRIBUTION AGENT"
- Label 3: "DIGITAL TWIN"
- Label 4: "L1 BASIC METADATA"
- Label 5: "L2 VOICE LIKENESS"
- Label 6: "L3 FULL CREATIVE"
- Label 7: "System voice"
- Label 8: "Gap-filling workflows"
- Label 9: "Metadata queries"
- Label 10: "Structured tasks"
- Label 11: "Artist voice clone"
- Label 12: "Fan-facing"
- Label 13: "Conversational"
- Label 14: "Storytelling"
- Label 15: "Creative responses"
- Label 16: "CONSENT GATES"

### Caption

Dual persona voice system showing how a shared pipeline branches into Attribution Agent and Digital Twin personas, with progressive consent levels (L1/L2/L3) gating access to each persona's features.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- do NOT render them as labels
2. **Semantic tags are INTERNAL** -- do NOT render them as visible text
3. **Hex codes are INTERNAL** -- do NOT render them
4. **Background MUST be warm cream (#f6f3e6)**
5. **No generic flowchart aesthetics**
6. **No figure captions** -- no "Figure 1." prefix
7. **No prompt leakage**

### Figure-Specific Rules

8. The shared pipeline strip must visually span the full width -- both personas share it.
9. Consent gates must be visually distinct from processing stages -- they are access barriers, not pipeline stages.
10. The Attribution Agent and Digital Twin panels must be visually equal in size -- neither is more important than the other.
11. L1/L2/L3 labels must use the assurance level color semantics (amber, blue, green) -- they map to A1/A2/A3 conceptually.
12. Do NOT show specific artist names or likenesses -- the concept is generic.
13. The word "persona" in the diagram refers to voice agent behavior modes, not UI personas.

## Alt Text

Dual persona voice agent system showing a shared pipeline branching into Attribution Agent (system voice for metadata gap-filling) and Digital Twin (artist voice clone), gated by progressive consent levels L1 through L3 for music attribution.

## Image Embed

![Dual persona voice agent system showing a shared pipeline branching into Attribution Agent (system voice for metadata gap-filling) and Digital Twin (artist voice clone), gated by progressive consent levels L1 through L3 for music attribution.](docs/figures/repo-figures/assets/fig-voice-05-dual-persona-system.jpg)

*Dual persona voice system showing how a shared pipeline branches into Attribution Agent and Digital Twin personas, with progressive consent levels (L1/L2/L3) gating access to each persona's features.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "voice-05",
    "title": "Dual Persona Voice System",
    "audience": "L2",
    "layout_template": "D"
  },
  "content_architecture": {
    "primary_message": "A shared voice pipeline serves two personas gated by progressive consent levels.",
    "layout_flow": "top-to-bottom-split",
    "key_structures": [
      {
        "name": "Shared Pipeline",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["SHARED PIPELINE", "Transport -> STT -> LLM -> TTS -> Out"]
      },
      {
        "name": "L1 Consent Gate",
        "role": "assurance_a1",
        "is_highlighted": false,
        "labels": ["L1 BASIC METADATA"]
      },
      {
        "name": "L2 Consent Gate",
        "role": "assurance_a2",
        "is_highlighted": false,
        "labels": ["L2 VOICE LIKENESS"]
      },
      {
        "name": "L3 Consent Gate",
        "role": "assurance_a3",
        "is_highlighted": true,
        "labels": ["L3 FULL CREATIVE"]
      },
      {
        "name": "Attribution Agent",
        "role": "persona_block",
        "is_highlighted": true,
        "labels": ["ATTRIBUTION AGENT", "System voice", "Gap-filling", "Metadata queries"]
      },
      {
        "name": "Digital Twin",
        "role": "persona_block",
        "is_highlighted": true,
        "labels": ["DIGITAL TWIN", "Artist voice clone", "Fan-facing", "Storytelling"]
      }
    ],
    "relationships": [
      {
        "from": "Shared Pipeline",
        "to": "Consent Gates",
        "type": "arrow",
        "label": "consent check"
      },
      {
        "from": "L1 Gate",
        "to": "Attribution Agent",
        "type": "arrow",
        "label": "basic metadata grants access"
      },
      {
        "from": "L2 Gate",
        "to": "Digital Twin",
        "type": "arrow",
        "label": "voice likeness grants access"
      },
      {
        "from": "L3 Gate",
        "to": "Digital Twin",
        "type": "arrow",
        "label": "full creative enables all"
      }
    ],
    "callout_boxes": [
      {
        "heading": "CONSENT GATES PERSONA ACCESS",
        "body_text": "Artist consent level determines which voice persona features are available. L1 enables Attribution Agent. L2 enables basic Digital Twin. L3 enables full creative Digital Twin.",
        "position": "bottom-full-width"
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
- [ ] Anti-hallucination rules listed
- [ ] Alt text provided (125 chars max)
- [ ] JSON export block included
- [ ] Audience level correct (L2)
- [ ] Layout template identified (D)

## Status

- [ ] Draft created
- [ ] Content reviewed
- [x] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25
- [ ] Embedded in documentation
