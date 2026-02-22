# fig-voice-26: Voice Agent Cost: Anatomy of a Minute

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-voice-26 |
| **Title** | Voice Agent Cost: Anatomy of a Minute |
| **Audience** | L2 (Technical Manager) |
| **Location** | docs/tutorials/voice-agent-implementation.md |
| **Priority** | P0 (Critical) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | E (Steps) |

## Purpose

Break down the per-minute cost of running a voice agent into its five component parts (STT, LLM, TTS, Transport, Platform) across three pricing tiers (Budget, Mid, Premium). Shows specific provider combinations at each tier so teams can make informed trade-offs. Answers: "What does it actually cost to run a voice agent per minute, and where does the money go?"

## Key Message

Voice agent costs range from $0.01-0.02/min (self-hosted budget) to $0.15-0.20/min (premium commercial), a 10x difference driven primarily by LLM and TTS component choices. The mid-tier ($0.05-0.08/min) using Deepgram Nova-3 + GPT-4o mini + Cartesia Sonic offers the best cost-quality balance for most production deployments.

## Visual Concept

Three vertical stacked bars side by side, each representing one pricing tier. Each bar is divided into five colored segments (STT, LLM, TTS, Transport, Platform) with proportional heights. Provider names appear inside or beside each segment. A horizontal dashed line at the Premium tier height emphasizes the 10x cost gap. Roman numerals label each tier.

```
+-------------------------------------------------------------------+
|  VOICE AGENT COST: ANATOMY OF A MINUTE                      [sq]   |
|  -- Component Breakdown by Tier                                    |
+-------------------------------------------------------------------+
|                                                                    |
|   $0.20 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┌────────┐ |
|                                                         │Platform│ |
|   $0.15                                                 │ markup │ |
|                                                         ├────────┤ |
|                                                         │ElevenLb│ |
|   $0.10                                                 │  TTS   │ |
|                                                         │$0.07/m │ |
|                                                         ├────────┤ |
|   $0.08 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┌────────┐             │ Claude │ |
|                                  │Cartesia│             │ Sonnet │ |
|   $0.05                         │  TTS   │             │$0.04/m │ |
|                                  ├────────┤             ├────────┤ |
|                                  │GPT-4o  │             │Deepgram│ |
|                                  │ mini   │             │Nova-3  │ |
|   $0.02 ─ ─ ─ ┌────────┐       ├────────┤             │$0.01/m │ |
|                │ Kokoro │       │Deepgram│             ├────────┤ |
|                │  TTS   │       │Nova-3  │             │Transprt│ |
|   $0.01        ├────────┤       ├────────┤             └────────┘ |
|                │Gemini  │       │Transprt│                         |
|                │ Flash  │       └────────┘                         |
|                ├────────┤                                          |
|                │Whisper │                                          |
|                │(local) │                                          |
|                ├────────┤                                          |
|                │Transprt│                                          |
|                └────────┘                                          |
|                                                                    |
|      I. BUDGET          II. MID            III. PREMIUM            |
|    $0.01-0.02/min     $0.05-0.08/min     $0.15-0.20/min           |
|                                                                    |
|    Self-hosted         Deepgram Nova-3    Deepgram Nova-3          |
|    Whisper +           + GPT-4o mini      + Claude Sonnet          |
|    Gemini Flash +      + Cartesia Sonic   + ElevenLabs Flash       |
|    Kokoro                                                          |
|                                                                    |
+-------------------------------------------------------------------+
|  10x COST DIFFERENCE BETWEEN BUDGET AND PREMIUM --                 |
|  choose based on user tier                                         |
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
    content: "VOICE AGENT COST: ANATOMY OF A MINUTE"
    role: title

  - id: chart_zone
    bounds: [80, 140, 1760, 680]
    role: content_area

  - id: labels_zone
    bounds: [80, 840, 1760, 80]
    role: content_area

  - id: callout_zone
    bounds: [60, 940, 1800, 100]
    content: "10x COST DIFFERENCE"
    role: callout_box

anchors:
  - id: y_axis
    position: [120, 480]
    size: [40, 680]
    role: data_flow
    label: "cost per minute ($)"

  - id: budget_bar
    position: [360, 640]
    size: [300, 240]
    role: processing_stage
    label: "I. BUDGET"

  - id: budget_stt
    position: [360, 740]
    size: [300, 60]
    role: processing_stage
    label: "Self-hosted Whisper"

  - id: budget_llm
    position: [360, 680]
    size: [300, 60]
    role: processing_stage
    label: "Gemini Flash"

  - id: budget_tts
    position: [360, 620]
    size: [300, 60]
    role: processing_stage
    label: "Kokoro TTS"

  - id: budget_transport
    position: [360, 780]
    size: [300, 30]
    role: processing_stage
    label: "Transport"

  - id: mid_bar
    position: [860, 480]
    size: [300, 400]
    role: selected_option
    label: "II. MID"

  - id: mid_stt
    position: [860, 680]
    size: [300, 80]
    role: processing_stage
    label: "Deepgram Nova-3"

  - id: mid_llm
    position: [860, 580]
    size: [300, 100]
    role: processing_stage
    label: "GPT-4o mini"

  - id: mid_tts
    position: [860, 480]
    size: [300, 100]
    role: processing_stage
    label: "Cartesia Sonic"

  - id: mid_transport
    position: [860, 760]
    size: [300, 40]
    role: processing_stage
    label: "Transport"

  - id: premium_bar
    position: [1360, 220]
    size: [300, 660]
    role: warning_box
    label: "III. PREMIUM"

  - id: premium_stt
    position: [1360, 680]
    size: [300, 80]
    role: processing_stage
    label: "Deepgram Nova-3"

  - id: premium_llm
    position: [1360, 480]
    size: [300, 200]
    role: processing_stage
    label: "Claude Sonnet"

  - id: premium_tts
    position: [1360, 280]
    size: [300, 200]
    role: processing_stage
    label: "ElevenLabs Flash"

  - id: premium_transport
    position: [1360, 780]
    size: [300, 40]
    role: processing_stage
    label: "Transport"

  - id: premium_platform
    position: [1360, 220]
    size: [300, 60]
    role: processing_stage
    label: "Platform markup"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "VOICE AGENT COST: ANATOMY OF A MINUTE" with coral accent square |
| Y-axis | `data_flow` | Vertical cost scale from $0.00 to $0.20 |
| Budget bar (I) | `processing_stage` | Stacked bar: Whisper + Gemini Flash + Kokoro, $0.01-0.02/min total |
| Mid bar (II) | `selected_option` | Stacked bar: Deepgram Nova-3 + GPT-4o mini + Cartesia Sonic, $0.05-0.08/min |
| Premium bar (III) | `warning_box` | Stacked bar: Deepgram Nova-3 + Claude Sonnet + ElevenLabs Flash, $0.15-0.20/min |
| STT segments | `processing_stage` | Speech-to-text cost component in each bar |
| LLM segments | `processing_stage` | Language model cost component in each bar (largest variance) |
| TTS segments | `processing_stage` | Text-to-speech cost component in each bar |
| Transport segments | `processing_stage` | WebRTC/transport cost component (relatively constant) |
| Platform segments | `processing_stage` | Platform markup (premium only, managed platforms) |
| Tier labels | `label_editorial` | Roman numeral tier names with price ranges |
| Provider stacks | `data_mono` | Specific provider names listed below each bar |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Budget bar | Mid bar | arrow | "~4x increase" |
| Mid bar | Premium bar | arrow | "~2.5x increase" |
| Budget bar | Premium bar | dashed | "10x total gap" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "10x COST DIFFERENCE BETWEEN BUDGET AND PREMIUM" | Choose based on user tier -- free users get budget self-hosted stack, paying users get mid-tier, enterprise gets premium with highest quality. | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "I. BUDGET"
- Label 2: "II. MID"
- Label 3: "III. PREMIUM"
- Label 4: "$0.01-0.02/min"
- Label 5: "$0.05-0.08/min"
- Label 6: "$0.15-0.20/min"
- Label 7: "Self-hosted Whisper"
- Label 8: "Gemini Flash"
- Label 9: "Kokoro TTS"
- Label 10: "Deepgram Nova-3"
- Label 11: "GPT-4o mini"
- Label 12: "Cartesia Sonic"
- Label 13: "Claude Sonnet"
- Label 14: "ElevenLabs Flash"
- Label 15: "STT"
- Label 16: "LLM"
- Label 17: "TTS"
- Label 18: "Transport"
- Label 19: "Platform"

### Caption (for embedding in documentation)

Stacked cost breakdown of voice agent operation per minute across three tiers -- Budget (self-hosted, $0.01-0.02/min), Mid (Deepgram + GPT-4o mini + Cartesia, $0.05-0.08/min), and Premium (Deepgram + Claude Sonnet + ElevenLabs, $0.15-0.20/min) -- showing a 10x cost difference driven primarily by LLM and TTS choices.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `selected_option`, `warning_box`, `processing_stage` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption. The editorial display title is allowed.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. Deepgram Nova-3 STT pricing is ~$0.0059/min (pay-as-you-go). This is approximate -- do NOT present as exact guaranteed price.
10. ElevenLabs pricing ranges $0.07-0.10/min depending on tier. Use $0.07/min as the representative figure.
11. Cartesia Sonic pricing is approximately $0.02-0.04/min for TTS. Lower latency than ElevenLabs.
12. Kokoro-82M is self-hosted and costs only compute (~$0.06/hr on GPU, effectively $0.001/min).
13. Gemini Flash is Google's budget LLM option -- pricing is per token but approximately $0.003-0.005/min for voice workloads.
14. Claude Sonnet pricing for voice workloads is approximately $0.03-0.05/min depending on context length.
15. Transport costs (WebRTC via Daily.co or similar) are approximately $0.002-0.004/min -- relatively constant across tiers.
16. The "10x" difference is between the Budget floor ($0.01-0.02) and the Premium ceiling ($0.15-0.20). This is approximate but directionally correct.
17. All prices are as of Feb 2026 and subject to change -- do NOT present as permanent pricing.

## Alt Text

Stacked cost breakdown of voice agent operation per minute across three FinOps tiers showing Budget at $0.01-0.02 with self-hosted components, Mid at $0.05-0.08 with Deepgram and Cartesia, and Premium at $0.15-0.20 with ElevenLabs, revealing a 10x cost difference driven by LLM and TTS choices.

## Image Embed

![Stacked cost breakdown of voice agent operation per minute across three FinOps tiers showing Budget at $0.01-0.02 with self-hosted components, Mid at $0.05-0.08 with Deepgram and Cartesia, and Premium at $0.15-0.20 with ElevenLabs, revealing a 10x cost difference driven by LLM and TTS choices.](docs/figures/repo-figures/assets/fig-voice-26-cost-per-minute-breakdown.jpg)

*Stacked cost breakdown of voice agent operation per minute across three tiers -- Budget (self-hosted, $0.01-0.02/min), Mid (Deepgram + GPT-4o mini + Cartesia, $0.05-0.08/min), and Premium (Deepgram + Claude Sonnet + ElevenLabs, $0.15-0.20/min) -- showing a 10x cost difference driven primarily by LLM and TTS choices.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "voice-26",
    "title": "Voice Agent Cost: Anatomy of a Minute",
    "audience": "L2",
    "layout_template": "E"
  },
  "content_architecture": {
    "primary_message": "Voice agent costs span 10x from $0.01-0.02/min (self-hosted) to $0.15-0.20/min (premium commercial), driven primarily by LLM and TTS component choices.",
    "layout_flow": "left-to-right",
    "key_structures": [
      {
        "name": "Budget Tier",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["I. BUDGET", "$0.01-0.02/min", "Whisper + Gemini Flash + Kokoro"]
      },
      {
        "name": "Mid Tier",
        "role": "selected_option",
        "is_highlighted": true,
        "labels": ["II. MID", "$0.05-0.08/min", "Deepgram + GPT-4o mini + Cartesia"]
      },
      {
        "name": "Premium Tier",
        "role": "warning_box",
        "is_highlighted": false,
        "labels": ["III. PREMIUM", "$0.15-0.20/min", "Deepgram + Claude Sonnet + ElevenLabs"]
      }
    ],
    "relationships": [
      {
        "from": "Budget Tier",
        "to": "Premium Tier",
        "type": "dashed",
        "label": "10x cost gap"
      }
    ],
    "callout_boxes": [
      {
        "heading": "10x COST DIFFERENCE BETWEEN BUDGET AND PREMIUM",
        "body_text": "Choose based on user tier -- free users get budget self-hosted stack, paying users get mid-tier, enterprise gets premium with highest quality.",
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
