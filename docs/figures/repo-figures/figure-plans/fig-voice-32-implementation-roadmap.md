# fig-voice-32: Voice Agent Implementation Roadmap

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-voice-32 |
| **Title** | Voice Agent Implementation Roadmap |
| **Audience** | L2 (Technical Manager) |
| **Location** | docs/tutorials/voice-agent-implementation.md |
| **Priority** | P0 (Critical) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | E (Steps) |

## Purpose

Define a five-phase implementation roadmap for adding voice capabilities to the music attribution scaffold, from minimal viable voice input (Phase I) through premium features (Phase V). Each phase builds on the previous, with clear timelines, deliverables, and dependencies. Answers: "What is the sequence for implementing voice, and how fast can we ship the first phase?"

## Key Message

Phase I (voice-to-text attribution) ships in 2 months with ZERO TTS work -- it simply pipes STT output into the existing text agent. Each subsequent phase adds one capability layer: TTS response, turn detection, digital twin, and premium features. The roadmap is deliberately incremental, delivering user value at each phase while deferring costly components (voice cloning, emotional TTS) until product-market fit is validated.

## Visual Concept

Five phases as horizontal steps flowing left to right (Template E), each connected by dependency arrows. Each phase box contains the phase number (Roman numeral), timeline, key deliverable, and technology additions. Phase I is visually emphasized as the "ship first" milestone. A dependency chain shows each phase building on the previous.

```
+-------------------------------------------------------------------+
|  VOICE AGENT IMPLEMENTATION ROADMAP                          [sq]   |
|  -- Five Phases from STT Input to Premium Features                 |
+-------------------------------------------------------------------+
|                                                                    |
|  PHASE I                    PHASE II                               |
|  VOICE-TO-TEXT              SYSTEM VOICE RESPONSE                  |
|  Month 1-2                  Month 2-3                              |
|  ┌─────────────────────┐   ┌─────────────────────┐               |
|  │                      │   │                      │               |
|  │  ■ STT input to      │──>│  ■ Add Cartesia TTS  │               |
|  │    existing text     │   │  ■ Basic voice output │               |
|  │    agent             │   │  ■ Response streaming  │               |
|  │  ■ Deepgram Nova-3   │   │  ■ Orpheus fallback   │               |
|  │  ■ No TTS required   │   │                      │               |
|  │  ■ WebSocket audio   │   │  NEW: TTS layer      │               |
|  │                      │   │                      │               |
|  │  SHIPS IN 2 MONTHS   │   └──────────┬──────────┘               |
|  └──────────────────────┘               │                          |
|                                          ▼                          |
|  PHASE III                  PHASE IV                               |
|  TURN DETECTION             DIGITAL TWIN                           |
|  Month 3-4                  Month 4-6                              |
|  ┌─────────────────────┐   ┌─────────────────────┐               |
|  │                      │   │                      │               |
|  │  ■ Pipecat Smart     │   │  ■ Voice cloning     │               |
|  │    Turn integration  │<──│    (ElevenLabs Pro)  │               |
|  │  ■ Interrupt handling│   │  ■ Persona management │               |
|  │  ■ Natural pause     │   │  ■ Consent framework  │               |
|  │    detection         │   │  ■ PRAC3 compliance   │               |
|  │                      │   │                      │               |
|  │  NEW: Conversation   │   │  NEW: Identity +     │               |
|  │  flow management     │   │  rights management   │               |
|  └──────────────────────┘   └──────────┬──────────┘               |
|                                          │                          |
|                                          ▼                          |
|                             PHASE V                                |
|                             PREMIUM FEATURES                       |
|                             Month 6+                               |
|                             ┌─────────────────────┐               |
|                             │                      │               |
|                             │  ■ Emotional TTS      │               |
|                             │  ■ Multi-language      │               |
|                             │  ■ Fan interactions    │               |
|                             │  ■ On-device fallback  │               |
|                             │                      │               |
|                             │  NEW: Scale +         │               |
|                             │  differentiation      │               |
|                             └─────────────────────┘               |
|                                                                    |
|  ─────────────────────────────────────────────── [accent line]     |
|                                                                    |
|  DEPENDENCIES: I ──> II ──> III ──> IV ──> V                       |
|  Each phase builds on the previous                                 |
|                                                                    |
+-------------------------------------------------------------------+
|  PHASE I SHIPS IN 2 MONTHS -- voice input to existing agent        |
|  requires ZERO TTS work                                            |
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
    content: "VOICE AGENT IMPLEMENTATION ROADMAP"
    role: title

  - id: roadmap_zone
    bounds: [60, 140, 1800, 680]
    role: content_area

  - id: dependency_zone
    bounds: [60, 840, 1800, 60]
    role: content_area

  - id: callout_zone
    bounds: [60, 940, 1800, 100]
    content: "PHASE I SHIPS IN 2 MONTHS"
    role: callout_box

anchors:
  - id: phase_i
    position: [260, 320]
    size: [460, 280]
    role: selected_option
    label: "PHASE I: VOICE-TO-TEXT"

  - id: phase_ii
    position: [820, 320]
    size: [460, 280]
    role: processing_stage
    label: "PHASE II: SYSTEM VOICE"

  - id: phase_iii
    position: [260, 660]
    size: [460, 220]
    role: processing_stage
    label: "PHASE III: TURN DETECTION"

  - id: phase_iv
    position: [820, 660]
    size: [460, 220]
    role: processing_stage
    label: "PHASE IV: DIGITAL TWIN"

  - id: phase_v
    position: [1420, 500]
    size: [420, 340]
    role: deferred_option
    label: "PHASE V: PREMIUM"

  - id: flow_i_to_ii
    from: phase_i
    to: phase_ii
    type: arrow
    label: "add TTS"

  - id: flow_ii_to_iii
    from: phase_ii
    to: phase_iii
    type: arrow
    label: "add turn mgmt"

  - id: flow_iii_to_iv
    from: phase_iii
    to: phase_iv
    type: arrow
    label: "add identity"

  - id: flow_iv_to_v
    from: phase_iv
    to: phase_v
    type: arrow
    label: "add premium"

  - id: timeline_i
    position: [260, 240]
    size: [200, 30]
    role: data_mono
    label: "Month 1-2"

  - id: timeline_ii
    position: [820, 240]
    size: [200, 30]
    role: data_mono
    label: "Month 2-3"

  - id: timeline_iii
    position: [260, 600]
    size: [200, 30]
    role: data_mono
    label: "Month 3-4"

  - id: timeline_iv
    position: [820, 600]
    size: [200, 30]
    role: data_mono
    label: "Month 4-6"

  - id: timeline_v
    position: [1420, 440]
    size: [200, 30]
    role: data_mono
    label: "Month 6+"

  - id: ship_badge
    position: [260, 560]
    size: [240, 40]
    role: selected_option
    label: "SHIPS IN 2 MONTHS"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "VOICE AGENT IMPLEMENTATION ROADMAP" with coral accent square |
| Phase I: Voice-to-Text | `selected_option` | Month 1-2. STT input to existing text agent. Deepgram Nova-3. No TTS. WebSocket audio. Ships in 2 months. |
| Phase II: System Voice | `processing_stage` | Month 2-3. Add Cartesia TTS. Basic voice output. Response streaming. Orpheus fallback. |
| Phase III: Turn Detection | `processing_stage` | Month 3-4. Pipecat Smart Turn. Interrupt handling. Natural pause detection. Conversation flow. |
| Phase IV: Digital Twin | `processing_stage` | Month 4-6. Voice cloning (ElevenLabs Pro). Persona management. Consent framework. PRAC3 compliance. |
| Phase V: Premium Features | `deferred_option` | Month 6+. Emotional TTS. Multi-language. Fan interactions. On-device fallback. Scale + differentiation. |
| "SHIPS IN 2 MONTHS" badge | `selected_option` | Emphasized badge on Phase I |
| Dependency chain | `data_flow` | I -> II -> III -> IV -> V |
| Timeline markers | `data_mono` | Month ranges for each phase |
| Phase dividers | `accent_line` | Coral lines between phase descriptions |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Phase I | Phase II | arrow | "add TTS layer" |
| Phase II | Phase III | arrow | "add conversation management" |
| Phase III | Phase IV | arrow | "add identity + rights" |
| Phase IV | Phase V | arrow | "add premium features" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "PHASE I SHIPS IN 2 MONTHS" | Voice input to existing agent requires ZERO TTS work. Pipe Deepgram STT output directly into the PydanticAI agent. Text responses displayed in the existing chat UI. | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "PHASE I: VOICE-TO-TEXT"
- Label 2: "PHASE II: SYSTEM VOICE"
- Label 3: "PHASE III: TURN DETECTION"
- Label 4: "PHASE IV: DIGITAL TWIN"
- Label 5: "PHASE V: PREMIUM FEATURES"
- Label 6: "Month 1-2"
- Label 7: "Month 2-3"
- Label 8: "Month 3-4"
- Label 9: "Month 4-6"
- Label 10: "Month 6+"
- Label 11: "SHIPS IN 2 MONTHS"
- Label 12: "STT to existing agent"
- Label 13: "Add Cartesia TTS"
- Label 14: "Pipecat Smart Turn"
- Label 15: "Voice cloning + consent"
- Label 16: "Emotional TTS + i18n"
- Label 17: "ZERO TTS work"
- Label 18: "NEW: TTS layer"
- Label 19: "NEW: Conversation flow"
- Label 20: "NEW: Identity + rights"

### Caption (for embedding in documentation)

Five-phase voice agent implementation roadmap for music attribution -- Phase I (voice-to-text, Month 1-2) ships with ZERO TTS work by piping STT into the existing agent, through Phase V (premium features, Month 6+) adding emotional TTS, multi-language, and on-device fallback.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `selected_option`, `processing_stage`, `deferred_option` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption. The editorial display title is allowed.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. Phase I requires ZERO TTS work -- this is the key insight. STT audio comes in via Deepgram, gets transcribed, and feeds the existing PydanticAI text agent. The response is displayed as text in the chat UI.
10. The "2 months" timeline for Phase I assumes a team familiar with the existing scaffold. Adjust expectations for teams starting fresh.
11. Phase IV (Digital Twin) requires ElevenLabs Professional Voice Cloning, which has its own consent and verification requirements. This is not a trivial feature.
12. PRAC3 compliance in Phase IV refers to the Privacy, Reputation, Accountability, Consent, Credit, Compensation framework mapped in fig-voice-29.
13. Emotional TTS in Phase V refers to models like Orpheus that support emotion tags (`<laugh>`, `<sigh>`). This is an emerging capability, not a mature feature.
14. Multi-language in Phase V refers to TTS models with multilingual support (e.g., CosyVoice from Alibaba). The STT side already handles multiple languages via Deepgram.
15. On-device fallback in Phase V moves STT and TTS to client-side processing, eliminating per-minute API costs for basic interactions.
16. Each phase's timeline is cumulative -- Phase III starts at Month 3, not Month 3 after Phase II completes. Phases can overlap.
17. "Fan interactions" in Phase V refers to artist-fan voice interactions where the artist's digital twin responds to fan queries about their music -- this requires the consent framework from Phase IV.

## Alt Text

Five-phase voice agent implementation roadmap for music attribution starting with STT-only input shipping in 2 months with zero TTS work, progressing through system voice response, turn detection, digital twin with consent framework, to premium features including emotional TTS and multi-language support.

## Image Embed

![Five-phase voice agent implementation roadmap for music attribution starting with STT-only input shipping in 2 months with zero TTS work, progressing through system voice response, turn detection, digital twin with consent framework, to premium features including emotional TTS and multi-language support.](docs/figures/repo-figures/assets/fig-voice-32-implementation-roadmap.jpg)

*Five-phase voice agent implementation roadmap for music attribution -- Phase I (voice-to-text, Month 1-2) ships with ZERO TTS work by piping STT into the existing agent, through Phase V (premium features, Month 6+) adding emotional TTS, multi-language, and on-device fallback.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "voice-32",
    "title": "Voice Agent Implementation Roadmap",
    "audience": "L2",
    "layout_template": "E"
  },
  "content_architecture": {
    "primary_message": "Phase I ships in 2 months with ZERO TTS work -- STT input to existing text agent. Five phases build incrementally through digital twin and premium features.",
    "layout_flow": "left-to-right-and-down",
    "key_structures": [
      {
        "name": "Phase I: Voice-to-Text",
        "role": "selected_option",
        "is_highlighted": true,
        "labels": ["PHASE I", "Month 1-2", "SHIPS IN 2 MONTHS", "ZERO TTS"]
      },
      {
        "name": "Phase II: System Voice",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["PHASE II", "Month 2-3", "Add Cartesia TTS"]
      },
      {
        "name": "Phase III: Turn Detection",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["PHASE III", "Month 3-4", "Pipecat Smart Turn"]
      },
      {
        "name": "Phase IV: Digital Twin",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["PHASE IV", "Month 4-6", "Voice cloning + consent"]
      },
      {
        "name": "Phase V: Premium Features",
        "role": "deferred_option",
        "is_highlighted": false,
        "labels": ["PHASE V", "Month 6+", "Emotional TTS + i18n"]
      }
    ],
    "relationships": [
      {
        "from": "Phase I",
        "to": "Phase II",
        "type": "arrow",
        "label": "add TTS"
      },
      {
        "from": "Phase II",
        "to": "Phase III",
        "type": "arrow",
        "label": "add conversation"
      },
      {
        "from": "Phase III",
        "to": "Phase IV",
        "type": "arrow",
        "label": "add identity"
      },
      {
        "from": "Phase IV",
        "to": "Phase V",
        "type": "arrow",
        "label": "add premium"
      }
    ],
    "callout_boxes": [
      {
        "heading": "PHASE I SHIPS IN 2 MONTHS",
        "body_text": "Voice input to existing agent requires ZERO TTS work. Pipe Deepgram STT into PydanticAI agent.",
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
- [x] Anti-hallucination rules listed (8 default + 9 figure-specific)
- [x] Alt text provided (125 chars max)
- [x] JSON export block included
- [x] Audience level correct (L2)
- [x] Layout template identified (E)

## Status

- [x] Draft created
- [ ] Content reviewed
- [x] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
