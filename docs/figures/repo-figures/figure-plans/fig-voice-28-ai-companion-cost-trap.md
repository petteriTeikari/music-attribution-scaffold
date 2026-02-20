# fig-voice-28: The AI Companion Cost Trap

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-voice-28 |
| **Title** | The AI Companion Cost Trap |
| **Audience** | L1 (Executive / Non-Technical) |
| **Location** | docs/tutorials/voice-agent-implementation.md |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | D (Split-Panel) |

## Purpose

Illustrate the structural economics problem of flat-rate AI companion pricing, where power users consume disproportionate compute resources, creating unsustainable unit economics. Shows both the trap (Character.AI-style losses) and the escape routes (tiering, on-device, rate limiting). Answers: "Why do flat-rate voice subscriptions fail, and how should we price voice features?"

## Key Message

Flat-rate subscriptions combined with power users create structural losses -- Character.AI's 1% of users consumed 99% of tokens, generating $365M/year in serving costs against $32M revenue. The escape requires tiered pricing, on-device fallback, token budgets, and semantic caching from day one. The Dolores case study shows 70% of voice agent revenue going to ElevenLabs.

## Visual Concept

Split-panel (Template D). Left panel "THE TRAP" shows the economics death spiral with large, alarming numbers. Right panel "THE ESCAPE" shows the five mitigation strategies. A coral vertical divider separates the panels. The left is visually heavier (the problem), the right is lighter (the solution).

```
+-------------------------------------------------------------------+
|  THE AI COMPANION COST TRAP                                  [sq]   |
|  -- Why Flat-Rate Voice Subscriptions Fail                         |
+-------------------------------+-----------------------------------+
|                               |                                    |
|  THE TRAP                     |  THE ESCAPE                        |
|  ─────────                    |  ──────────                        |
|                               |                                    |
|  Flat pricing: $9.99/mo       |  I. TIERED PRICING                 |
|                               |     Free: 60 min/mo voice          |
|  Power users: 12 hr/day       |     Pro: 300 min/mo                |
|                               |     Enterprise: unlimited           |
|  ┌─────────────────────────┐ |                                    |
|  │  CHARACTER.AI            │ |  II. ON-DEVICE FALLBACK            |
|  │                          │ |     Whisper + Kokoro locally       |
|  │  Serving: $365M/year     │ |     Cloud only for complex tasks   |
|  │  Revenue: $32M/year      │ |                                    |
|  │                          │ |  III. RATE LIMITING                 |
|  │  11x LOSS RATIO          │ |      Token budgets per session     |
|  │                          │ |      Graceful degradation           |
|  │  1% of users consume     │ |                                    |
|  │  99% of tokens            │ |  IV. SEMANTIC CACHING              |
|  └─────────────────────────┘ |     Cache common voice responses    |
|                               |     15-30% compute reduction        |
|  ┌─────────────────────────┐ |                                    |
|  │  THE DOLORES CASE        │ |  V. INFRASTRUCTURE MIGRATION       |
|  │                          │ |     TPU migration saved Midjourney  |
|  │  $25/day from 1K beta    │ |     $16.8M/year. Custom silicon     |
|  │  users                    │ |     changes the cost curve.        |
|  │  70% of revenue goes     │ |                                    |
|  │  to ElevenLabs voice     │ |  ─────────────────────────         |
|  └─────────────────────────┘ |  TIER YOUR PRICING FROM DAY ONE    |
|                               |                                    |
+-------------------------------+-----------------------------------+
|  FLAT-RATE SUBSCRIPTIONS + POWER USERS = STRUCTURAL LOSS --        |
|  tier your pricing from day one                                    |
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
    content: "THE AI COMPANION COST TRAP"
    role: title

  - id: left_panel
    bounds: [60, 150, 880, 700]
    content: "THE TRAP"
    role: content_area

  - id: right_panel
    bounds: [980, 150, 880, 700]
    content: "THE ESCAPE"
    role: content_area

  - id: divider
    bounds: [950, 150, 4, 700]
    role: accent_line_v

  - id: callout_zone
    bounds: [60, 920, 1800, 120]
    content: "FLAT-RATE + POWER USERS = STRUCTURAL LOSS"
    role: callout_box

anchors:
  - id: trap_header
    position: [480, 180]
    size: [400, 60]
    role: warning_box
    label: "THE TRAP"

  - id: flat_pricing
    position: [480, 260]
    size: [600, 40]
    role: data_mono
    label: "$9.99/mo flat pricing"

  - id: character_ai_box
    position: [480, 420]
    size: [700, 260]
    role: warning_box
    label: "CHARACTER.AI"

  - id: serving_cost
    position: [400, 460]
    size: [300, 40]
    role: data_mono
    label: "$365M/year serving"

  - id: revenue
    position: [400, 510]
    size: [300, 40]
    role: data_mono
    label: "$32M/year revenue"

  - id: loss_ratio
    position: [480, 570]
    size: [200, 50]
    role: warning_box
    label: "11x LOSS RATIO"

  - id: power_users
    position: [480, 630]
    size: [400, 40]
    role: data_mono
    label: "1% consume 99% of tokens"

  - id: dolores_box
    position: [480, 720]
    size: [700, 140]
    role: warning_box
    label: "THE DOLORES CASE"

  - id: escape_header
    position: [1420, 180]
    size: [400, 60]
    role: selected_option
    label: "THE ESCAPE"

  - id: escape_tiered
    position: [1420, 280]
    size: [700, 100]
    role: processing_stage
    label: "I. TIERED PRICING"

  - id: escape_ondevice
    position: [1420, 400]
    size: [700, 80]
    role: processing_stage
    label: "II. ON-DEVICE FALLBACK"

  - id: escape_ratelimit
    position: [1420, 500]
    size: [700, 80]
    role: processing_stage
    label: "III. RATE LIMITING"

  - id: escape_caching
    position: [1420, 600]
    size: [700, 80]
    role: processing_stage
    label: "IV. SEMANTIC CACHING"

  - id: escape_infra
    position: [1420, 700]
    size: [700, 100]
    role: processing_stage
    label: "V. INFRASTRUCTURE MIGRATION"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "THE AI COMPANION COST TRAP" with coral accent square |
| Left panel: THE TRAP | `warning_box` | Economics death spiral with Character.AI and Dolores case studies |
| Right panel: THE ESCAPE | `selected_option` | Five mitigation strategies |
| Character.AI box | `warning_box` | $365M serving vs $32M revenue, 11x loss ratio, 1% consume 99% |
| Dolores case box | `warning_box` | $25/day from 1K beta, 70% revenue to ElevenLabs |
| Tiered Pricing | `processing_stage` | Free 60min, Pro 300min, Enterprise unlimited |
| On-Device Fallback | `processing_stage` | Whisper + Kokoro locally, cloud for complex only |
| Rate Limiting | `processing_stage` | Token budgets per session, graceful degradation |
| Semantic Caching | `processing_stage` | Cache common responses, 15-30% compute reduction |
| Infrastructure Migration | `processing_stage` | TPU migration saved Midjourney $16.8M/year |
| Center divider | `accent_line_v` | Coral vertical separator between trap and escape |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Flat pricing | Character.AI losses | arrow | "leads to" |
| Power users | 11x loss ratio | arrow | "drives" |
| THE TRAP | THE ESCAPE | dashed | "mitigated by" |
| Dolores case | Tiered Pricing | dashed | "lesson learned" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "FLAT-RATE SUBSCRIPTIONS + POWER USERS = STRUCTURAL LOSS" | Tier your pricing from day one. The scaffold's voice-as-Pro-feature philosophy avoids this trap by design. | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "THE TRAP"
- Label 2: "THE ESCAPE"
- Label 3: "$9.99/mo flat pricing"
- Label 4: "12 hr/day power users"
- Label 5: "$365M/year serving"
- Label 6: "$32M/year revenue"
- Label 7: "11x LOSS RATIO"
- Label 8: "1% consume 99% of tokens"
- Label 9: "$25/day from 1K beta"
- Label 10: "70% revenue to ElevenLabs"
- Label 11: "I. TIERED PRICING"
- Label 12: "II. ON-DEVICE FALLBACK"
- Label 13: "III. RATE LIMITING"
- Label 14: "IV. SEMANTIC CACHING"
- Label 15: "V. INFRA MIGRATION"
- Label 16: "$16.8M/year saved"

### Caption (for embedding in documentation)

Split-panel showing the AI companion cost trap (Character.AI's 11x loss ratio from flat-rate pricing with power users) and five escape strategies (tiered pricing, on-device fallback, rate limiting, semantic caching, infrastructure migration) for sustainable voice agent economics.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `warning_box`, `selected_option`, `processing_stage` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption. The editorial display title is allowed.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. Character.AI's $365M serving cost and $32M revenue are reported figures from 2024/2025 financial analysis. The 11x loss ratio is derived from these numbers ($365M / $32M ≈ 11.4x).
10. The "1% of users consume 99% of tokens" is a reported statistic for Character.AI -- do NOT generalize to all platforms.
11. The Dolores case study ($25/day revenue from 1K beta users, 70% to ElevenLabs) is from publicly reported data about the AI companion startup.
12. Midjourney's TPU migration savings of $16.8M/year is from reported infrastructure cost analysis. This is a real case study, not a hypothetical.
13. The "12 hr/day" power user figure is from Character.AI usage reports -- some users kept conversations running continuously.
14. Do NOT present the $9.99/mo as Character.AI's actual pricing -- it is representative of typical AI companion subscription pricing.
15. The scaffold's "voice as Pro feature" philosophy (documented in UX rules) inherently avoids the flat-rate trap.
16. This figure targets L1 audience -- use plain language, avoid technical jargon, lead with the business impact numbers.

## Alt Text

Split-panel diagram illustrating the AI companion cost trap with Character.AI's 11x loss ratio from $365M serving costs against $32M revenue from flat-rate pricing, alongside five FinOps escape strategies including tiered pricing, on-device fallback, rate limiting, semantic caching, and infrastructure migration.

## Image Embed

![Split-panel diagram illustrating the AI companion cost trap with Character.AI's 11x loss ratio from $365M serving costs against $32M revenue from flat-rate pricing, alongside five FinOps escape strategies including tiered pricing, on-device fallback, rate limiting, semantic caching, and infrastructure migration.](docs/figures/repo-figures/assets/fig-voice-28-ai-companion-cost-trap.jpg)

*Split-panel showing the AI companion cost trap (Character.AI's 11x loss ratio from flat-rate pricing with power users) and five escape strategies (tiered pricing, on-device fallback, rate limiting, semantic caching, infrastructure migration) for sustainable voice agent economics.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "voice-28",
    "title": "The AI Companion Cost Trap",
    "audience": "L1",
    "layout_template": "D"
  },
  "content_architecture": {
    "primary_message": "Flat-rate subscriptions + power users = structural loss. Character.AI's 11x loss ratio proves the model fails. Tier pricing from day one.",
    "layout_flow": "left-to-right",
    "key_structures": [
      {
        "name": "THE TRAP",
        "role": "warning_box",
        "is_highlighted": true,
        "labels": ["$365M serving", "$32M revenue", "11x LOSS", "1% = 99% tokens"]
      },
      {
        "name": "Character.AI Case",
        "role": "warning_box",
        "is_highlighted": true,
        "labels": ["$365M/year serving", "$32M/year revenue"]
      },
      {
        "name": "Dolores Case",
        "role": "warning_box",
        "is_highlighted": false,
        "labels": ["$25/day from 1K beta", "70% to ElevenLabs"]
      },
      {
        "name": "THE ESCAPE",
        "role": "selected_option",
        "is_highlighted": true,
        "labels": ["Tiered pricing", "On-device", "Rate limit", "Cache", "Infra"]
      },
      {
        "name": "Midjourney TPU",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["$16.8M/year saved"]
      }
    ],
    "relationships": [
      {
        "from": "THE TRAP",
        "to": "THE ESCAPE",
        "type": "dashed",
        "label": "mitigated by"
      }
    ],
    "callout_boxes": [
      {
        "heading": "FLAT-RATE SUBSCRIPTIONS + POWER USERS = STRUCTURAL LOSS",
        "body_text": "Tier your pricing from day one. The scaffold's voice-as-Pro-feature philosophy avoids this trap by design.",
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
- [x] Layout template identified (D)

## Status

- [x] Draft created
- [ ] Content reviewed
- [x] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
