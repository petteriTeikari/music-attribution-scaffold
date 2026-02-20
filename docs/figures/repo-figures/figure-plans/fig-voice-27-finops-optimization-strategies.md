# fig-voice-27: Voice AI FinOps: Six Cost Levers

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-voice-27 |
| **Title** | Voice AI FinOps: Six Cost Levers |
| **Audience** | L2 (Technical Manager) |
| **Location** | docs/tutorials/voice-agent-implementation.md |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | B (Multi-Panel) |

## Purpose

Present six actionable cost optimization strategies for voice AI infrastructure, each with quantified impact estimates. Teams building voice-enabled music attribution can apply these levers independently or in combination. Answers: "How do we reduce voice agent operating costs without sacrificing quality for paying users?"

## Key Message

Six cost levers -- model selection, semantic caching, on-device STT/TTS, context management, tiered quality, and volume commitments -- can be applied independently or combined for up to 16x total cost reduction. No single lever is sufficient; the combination creates compounding savings.

## Visual Concept

Six panels in a 3x2 grid, each labeled with a Roman numeral. Each panel contains the lever name, a brief description, the estimated cost reduction percentage, and a visual indicator of impact magnitude. A bottom callout bar shows the combined potential.

```
+-------------------------------------------------------------------+
|  VOICE AI FINOPS: SIX COST LEVERS                           [sq]   |
|  -- Optimization Strategies for Voice Agent Infrastructure         |
+-------------------------------------------------------------------+
|                                                                    |
|  ┌───────────────────────┐  ┌───────────────────────┐             |
|  │ I. MODEL SELECTION    │  │ II. SEMANTIC CACHING   │             |
|  │ ───────────────────── │  │ ─────────────────────  │             |
|  │                       │  │                        │             |
|  │ Right-size LLM per    │  │ Cache common responses │             |
|  │ query complexity.     │  │ by semantic similarity. │             |
|  │ Simple queries →      │  │ "What's the BPM?" hits │             |
|  │ Haiku/Flash. Complex  │  │ cache 40% of the time. │             |
|  │ → Sonnet/Opus.        │  │                        │             |
|  │                       │  │ ■ 15-30% REDUCTION     │             |
|  │ ■ 3-5x PER QUERY     │  │                        │             |
|  └───────────────────────┘  └───────────────────────┘             |
|                                                                    |
|  ┌───────────────────────┐  ┌───────────────────────┐             |
|  │ III. ON-DEVICE        │  │ IV. CONTEXT            │             |
|  │     STT / TTS         │  │     MANAGEMENT         │             |
|  │ ───────────────────── │  │ ─────────────────────  │             |
|  │                       │  │                        │             |
|  │ Eliminate per-minute   │  │ Aggressive truncation  │             |
|  │ API costs for basic   │  │ of conversation        │             |
|  │ interactions. Whisper  │  │ history. Keep last 3   │             |
|  │ + Kokoro run on-device│  │ turns + system prompt.  │             |
|  │ at ~$0.001/min.       │  │                        │             |
|  │                       │  │ ■ 20-40% TOKEN SAVINGS │             |
|  │ ■ 10-50x FOR STT+TTS │  │                        │             |
|  └───────────────────────┘  └───────────────────────┘             |
|                                                                    |
|  ┌───────────────────────┐  ┌───────────────────────┐             |
|  │ V. TIERED QUALITY     │  │ VI. VOLUME             │             |
|  │ ───────────────────── │  │     COMMITMENTS        │             |
|  │                       │  │ ─────────────────────  │             |
|  │ Free tier: self-hosted│  │ Growth/Enterprise tier  │             |
|  │ stack (Whisper +      │  │ volume discounts from   │             |
|  │ Gemini Flash + Kokoro)│  │ Deepgram, ElevenLabs,  │             |
|  │ Pro: commercial APIs  │  │ Anthropic. Commit to    │             |
|  │ (Deepgram + Cartesia) │  │ annual spend.           │             |
|  │                       │  │                        │             |
|  │ ■ 10x GAP BETWEEN    │  │ ■ 30-50% DISCOUNT      │             |
|  │   FREE AND PRO        │  │                        │             |
|  └───────────────────────┘  └───────────────────────┘             |
|                                                                    |
+-------------------------------------------------------------------+
|  COMBINED OPTIMIZATION CAN ACHIEVE 16x COST REDUCTION              |
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
    content: "VOICE AI FINOPS: SIX COST LEVERS"
    role: title

  - id: grid_zone
    bounds: [60, 140, 1800, 740]
    role: content_area

  - id: callout_zone
    bounds: [60, 940, 1800, 100]
    content: "COMBINED OPTIMIZATION CAN ACHIEVE 16x COST REDUCTION"
    role: callout_box

anchors:
  - id: panel_i
    position: [80, 160]
    size: [860, 220]
    role: processing_stage
    label: "I. MODEL SELECTION"

  - id: panel_ii
    position: [980, 160]
    size: [860, 220]
    role: processing_stage
    label: "II. SEMANTIC CACHING"

  - id: panel_iii
    position: [80, 420]
    size: [860, 220]
    role: processing_stage
    label: "III. ON-DEVICE STT/TTS"

  - id: panel_iv
    position: [980, 420]
    size: [860, 220]
    role: processing_stage
    label: "IV. CONTEXT MANAGEMENT"

  - id: panel_v
    position: [80, 680]
    size: [860, 220]
    role: processing_stage
    label: "V. TIERED QUALITY"

  - id: panel_vi
    position: [980, 680]
    size: [860, 220]
    role: processing_stage
    label: "VI. VOLUME COMMITMENTS"

  - id: impact_i
    position: [740, 340]
    size: [180, 40]
    role: selected_option
    label: "3-5x PER QUERY"

  - id: impact_ii
    position: [1640, 340]
    size: [180, 40]
    role: selected_option
    label: "15-30% REDUCTION"

  - id: impact_iii
    position: [740, 600]
    size: [180, 40]
    role: selected_option
    label: "10-50x FOR STT+TTS"

  - id: impact_iv
    position: [1640, 600]
    size: [180, 40]
    role: selected_option
    label: "20-40% TOKEN SAVINGS"

  - id: impact_v
    position: [740, 860]
    size: [180, 40]
    role: selected_option
    label: "10x GAP"

  - id: impact_vi
    position: [1640, 860]
    size: [180, 40]
    role: selected_option
    label: "30-50% DISCOUNT"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "VOICE AI FINOPS: SIX COST LEVERS" with coral accent square |
| Panel I: Model Selection | `processing_stage` | Right-size LLM per query complexity. Simple -> Haiku/Flash, complex -> Sonnet/Opus. 3-5x per query savings. |
| Panel II: Semantic Caching | `processing_stage` | Cache common responses by semantic similarity. 15-30% reduction for repetitive queries. |
| Panel III: On-Device STT/TTS | `processing_stage` | Eliminate per-minute API costs. Whisper + Kokoro run locally at ~$0.001/min. 10-50x savings on STT+TTS. |
| Panel IV: Context Management | `processing_stage` | Aggressive truncation of conversation history. Keep last 3 turns + system prompt. 20-40% token savings. |
| Panel V: Tiered Quality | `processing_stage` | Free tier gets self-hosted stack, Pro gets commercial APIs. 10x gap between tiers. |
| Panel VI: Volume Commitments | `processing_stage` | Annual spend commitments with Deepgram, ElevenLabs, Anthropic. 30-50% discount. |
| Impact badges | `selected_option` | Coral-accented impact quantification in each panel |
| Combined callout | `callout_box` | "16x COST REDUCTION" combined potential |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Panel I | Panel V | dashed | "model selection enables tiered quality" |
| Panel III | Panel V | dashed | "on-device enables free tier" |
| All panels | Combined callout | arrow | "compounding effect" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "COMBINED OPTIMIZATION CAN ACHIEVE 16x COST REDUCTION" | No single lever is sufficient. Model selection + semantic caching + on-device + context management + tiered quality + volume commitments compound to up to 16x savings. | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "I. MODEL SELECTION"
- Label 2: "II. SEMANTIC CACHING"
- Label 3: "III. ON-DEVICE STT/TTS"
- Label 4: "IV. CONTEXT MANAGEMENT"
- Label 5: "V. TIERED QUALITY"
- Label 6: "VI. VOLUME COMMITMENTS"
- Label 7: "3-5x PER QUERY"
- Label 8: "15-30% REDUCTION"
- Label 9: "10-50x FOR STT+TTS"
- Label 10: "20-40% TOKEN SAVINGS"
- Label 11: "10x GAP FREE vs PRO"
- Label 12: "30-50% DISCOUNT"
- Label 13: "Haiku/Flash for simple"
- Label 14: "Sonnet/Opus for complex"
- Label 15: "Cache hit rate ~40%"

### Caption (for embedding in documentation)

Six cost optimization levers for voice AI infrastructure -- model selection, semantic caching, on-device STT/TTS, context management, tiered quality, and volume commitments -- each independently quantified and combinable for up to 16x total cost reduction.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `processing_stage`, `selected_option` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption. The editorial display title is allowed.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. The "16x" combined figure is a theoretical maximum assuming all six levers are applied simultaneously. Present as "up to 16x", not as a guaranteed outcome.
10. Semantic caching hit rate of ~40% is for common queries like BPM, key, genre lookups. Complex attribution queries will have much lower cache rates.
11. On-device Whisper + Kokoro cost of ~$0.001/min assumes amortized GPU/CPU cost, not including hardware purchase.
12. Volume commitment discounts (30-50%) are typical for Growth/Enterprise tiers at providers like Deepgram and ElevenLabs -- exact rates are negotiable.
13. Context management "last 3 turns" is a starting heuristic -- actual optimal window depends on task complexity.
14. The scaffold already uses PydanticAI FallbackModel for LLM routing (model selection lever) -- this is an extension of existing architecture.
15. Do NOT claim these optimizations have been benchmarked in the scaffold -- they are recommendations based on industry practice.
16. Tiered quality is consistent with the voice-agent-as-Pro-feature philosophy in the UX rules.

## Alt Text

Six-panel FinOps grid presenting voice AI cost optimization levers -- model selection, semantic caching, on-device STT/TTS, context management, tiered quality, and volume commitments -- each with quantified savings estimates combining for up to 16x total cost reduction.

## Image Embed

![Six-panel FinOps grid presenting voice AI cost optimization levers -- model selection, semantic caching, on-device STT/TTS, context management, tiered quality, and volume commitments -- each with quantified savings estimates combining for up to 16x total cost reduction.](docs/figures/repo-figures/assets/fig-voice-27-finops-optimization-strategies.jpg)

*Six cost optimization levers for voice AI infrastructure -- model selection, semantic caching, on-device STT/TTS, context management, tiered quality, and volume commitments -- each independently quantified and combinable for up to 16x total cost reduction.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "voice-27",
    "title": "Voice AI FinOps: Six Cost Levers",
    "audience": "L2",
    "layout_template": "B"
  },
  "content_architecture": {
    "primary_message": "Six cost levers can be applied independently or combined for up to 16x total cost reduction in voice AI infrastructure.",
    "layout_flow": "grid-2x3",
    "key_structures": [
      {
        "name": "Model Selection",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["I. MODEL SELECTION", "3-5x PER QUERY"]
      },
      {
        "name": "Semantic Caching",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["II. SEMANTIC CACHING", "15-30% REDUCTION"]
      },
      {
        "name": "On-Device STT/TTS",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["III. ON-DEVICE STT/TTS", "10-50x FOR STT+TTS"]
      },
      {
        "name": "Context Management",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["IV. CONTEXT MANAGEMENT", "20-40% TOKEN SAVINGS"]
      },
      {
        "name": "Tiered Quality",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["V. TIERED QUALITY", "10x GAP"]
      },
      {
        "name": "Volume Commitments",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["VI. VOLUME COMMITMENTS", "30-50% DISCOUNT"]
      }
    ],
    "relationships": [
      {
        "from": "All panels",
        "to": "Combined callout",
        "type": "arrow",
        "label": "compounding effect"
      }
    ],
    "callout_boxes": [
      {
        "heading": "COMBINED OPTIMIZATION CAN ACHIEVE 16x COST REDUCTION",
        "body_text": "No single lever is sufficient. All six levers compound to up to 16x savings.",
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
- [x] Audience level correct (L2)
- [x] Layout template identified (B)

## Status

- [x] Draft created
- [ ] Content reviewed
- [x] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
