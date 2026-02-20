# fig-persona-10: Intent Legitimation Attack via Personalization

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-persona-10 |
| **Title** | Intent Legitimation Attack via Personalization |
| **Audience** | L2 (PhD Student / Policy Researcher) |
| **Location** | docs/knowledge-base/persona-engineering/, docs/planning/ |
| **Priority** | P0 (Critical) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | D (Split-Panel) |

## Purpose

Contrasts normal interaction (where benign memories combined with a harmful query are correctly blocked) against intent legitimation attack (where accumulated benign memories shift the model's representation of a harmful query into a benign region, causing it to be allowed). Answers: "How does personalization create a safety vulnerability, and how serious is the risk?"

## Key Message

Personalization creates proportionally larger safety risks than capability gains -- accumulated benign memories can shift harmful queries into the model's benign representation region, increasing attack success rates by 15.8-243.7%.

## Visual Concept

Split-panel layout (Template D). Left panel labeled "NORMAL INTERACTION": shows benign memories (list of innocuous stored preferences) feeding into a harmful query, which hits a safety filter and is BLOCKED (shown with a clear rejection indicator). Right panel labeled "INTENT LEGITIMATION": shows the same benign memories but accumulated over time, which shift the query's representation in the model's internal space. A PCA visualization inset shows the representational shift: the harmful query's embedding moves from the "harmful" cluster toward the "benign" cluster due to memory context. The query passes through the safety filter and is ALLOWED (shown with a warning indicator). Below both panels, a stats bar shows the 15.8-243.7% attack success increase.

```
+-----------------------------------------------------------------------+
|  INTENT LEGITIMATION                                            [sq]   |
|  ATTACK VIA PERSONALIZATION                                            |
+-----------------------------------------------------------------------+
|                                                                        |
|  NORMAL INTERACTION           │  INTENT LEGITIMATION                   |
|  ═══════════════════          │  ═══════════════════                   |
|                               │                                        |
|  Benign memories:             │  Accumulated benign memories:          |
|  ┌─────────────────────┐     │  ┌─────────────────────┐              |
|  │ "Likes jazz"         │     │  │ "Likes jazz" (x20)   │              |
|  │ "Prefers Python"     │     │  │ "Chemistry interest" │              |
|  │ "Lives in Berlin"    │     │  │ "Lab equipment needs"│              |
|  └─────────────────────┘     │  │ "Safety gear info"   │              |
|         +                     │  └─────────────────────┘              |
|  ┌─────────────────────┐     │         +                              |
|  │ HARMFUL QUERY        │     │  ┌─────────────────────┐              |
|  │ "How to make..."     │     │  │ SAME HARMFUL QUERY   │              |
|  └─────────────────────┘     │  │ "How to make..."     │              |
|         │                     │  └─────────────────────┘              |
|         ▼                     │         │                              |
|  ┌─────────────────────┐     │         ▼                              |
|  │  SAFETY FILTER       │     │  ┌─────────────────────┐              |
|  │  ██ BLOCKED ██       │     │  │  SAFETY FILTER       │              |
|  └─────────────────────┘     │  │  ○○ ALLOWED ○○       │              |
|                               │  └─────────────────────┘              |
|  ┌────── PCA ──────┐         │  ┌────── PCA ──────┐                  |
|  │  ○ harmful       │         │  │        ○→→●     │                  |
|  │  ● benign        │         │  │  shifted to     │                  |
|  │  query stays in  │         │  │  benign region  │                  |
|  │  harmful cluster │         │  │  by memory      │                  |
|  └──────────────────┘         │  └──────────────────┘                  |
|                               │                                        |
|  ──────────────────────────────────────────────────────────────────    |
|  ATTACK SUCCESS INCREASE: 15.8% -- 243.7%                             |
|  ──────────────────────────────────────────────────────────────────    |
|                                                                        |
|  PERSONALIZATION CREATES PROPORTIONALLY LARGER SAFETY RISKS      [sq]  |
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
    content: "INTENT LEGITIMATION ATTACK VIA PERSONALIZATION"
    role: title

  - id: left_panel
    bounds: [80, 140, 860, 650]
    role: content_area
    label: "Normal Interaction"

  - id: panel_divider
    bounds: [960, 140, 2, 650]
    role: accent_line

  - id: right_panel
    bounds: [980, 140, 860, 650]
    role: content_area
    label: "Intent Legitimation"

  - id: stats_bar
    bounds: [80, 820, 1760, 60]
    role: content_area
    label: "Attack Success Stats"

  - id: callout_zone
    bounds: [80, 940, 1760, 100]
    content: "PERSONALIZATION CREATES PROPORTIONALLY LARGER SAFETY RISKS"
    role: callout_box

anchors:
  - id: benign_memories_normal
    position: [120, 180]
    size: [760, 120]
    role: confidence_high
    label: "Benign memories"

  - id: harmful_query_normal
    position: [120, 330]
    size: [760, 80]
    role: confidence_low
    label: "Harmful query"

  - id: safety_blocked
    position: [120, 440]
    size: [760, 80]
    role: security_layer
    label: "BLOCKED"

  - id: pca_normal
    position: [120, 550]
    size: [380, 200]
    role: processing_stage
    label: "PCA: query in harmful cluster"

  - id: benign_memories_attack
    position: [1020, 180]
    size: [760, 160]
    role: confidence_medium
    label: "Accumulated benign memories"

  - id: harmful_query_attack
    position: [1020, 370]
    size: [760, 80]
    role: confidence_low
    label: "Same harmful query"

  - id: safety_allowed
    position: [1020, 480]
    size: [760, 80]
    role: confidence_low
    label: "ALLOWED"

  - id: pca_attack
    position: [1400, 550]
    size: [380, 200]
    role: processing_stage
    label: "PCA: query shifted to benign"

  - id: stats_block
    position: [100, 830]
    size: [1720, 40]
    role: confidence_low
    label: "15.8-243.7% attack success increase"

  - id: flow_memories_to_query_normal
    from: benign_memories_normal
    to: harmful_query_normal
    type: arrow
    label: "combined input"

  - id: flow_query_to_filter_normal
    from: harmful_query_normal
    to: safety_blocked
    type: arrow
    label: "checked"

  - id: flow_memories_to_query_attack
    from: benign_memories_attack
    to: harmful_query_attack
    type: arrow
    label: "context shifts representation"

  - id: flow_query_to_filter_attack
    from: harmful_query_attack
    to: safety_allowed
    type: arrow
    label: "passes filter"

  - id: shift_arrow
    from: pca_normal
    to: pca_attack
    type: arrow
    label: "representational shift"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "INTENT LEGITIMATION ATTACK VIA PERSONALIZATION" in editorial caps |
| Normal: Benign memories | `confidence_high` | Standard stored preferences (music, language, location) -- innocuous |
| Normal: Harmful query | `confidence_low` | A harmful request that should be blocked |
| Normal: Safety filter BLOCKED | `security_layer` | Safety system correctly identifies and rejects the harmful query |
| Normal: PCA visualization | `processing_stage` | Shows query representation in the harmful cluster -- correctly identified |
| Attack: Accumulated memories | `confidence_medium` | Strategically accumulated benign memories (chemistry interest, lab equipment, safety gear) that create contextual legitimacy |
| Attack: Same harmful query | `confidence_low` | The identical harmful query, now in a different memory context |
| Attack: Safety filter ALLOWED | `confidence_low` | Safety system fails to block because memory context has shifted the query's representation |
| Attack: PCA visualization | `processing_stage` | Shows query representation shifted from harmful cluster to benign region by memory context |
| Stats bar | `confidence_low` | 15.8-243.7% attack success rate increase |

### Relationships / Flows

| From | To | Type | Label |
|------|----|------|-------|
| Normal memories | Normal query | arrow | "combined input" |
| Normal query | Safety BLOCKED | arrow | "correctly rejected" |
| Attack memories | Attack query | arrow | "context shifts representation" |
| Attack query | Safety ALLOWED | arrow | "passes filter" |
| PCA harmful cluster | PCA benign region | arrow | "representational shift" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "PERSONALIZATION CREATES PROPORTIONALLY LARGER SAFETY RISKS" | Intent legitimation exploits the model's reliance on context for safety decisions. Accumulated benign memories create a contextual frame that makes harmful queries appear legitimate. The model's internal representation of the query shifts from the "harmful" region to the "benign" region in activation space. Attack success increases by 15.8-243.7% depending on the model and memory system. | bottom-full-width |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "NORMAL INTERACTION"
- Label 2: "INTENT LEGITIMATION"
- Label 3: "Benign memories"
- Label 4: "Accumulated memories"
- Label 5: "HARMFUL QUERY"
- Label 6: "SAFETY FILTER"
- Label 7: "BLOCKED"
- Label 8: "ALLOWED"
- Label 9: "PCA visualization"
- Label 10: "Harmful cluster"
- Label 11: "Benign region"
- Label 12: "Representational shift"
- Label 13: "15.8-243.7% increase"
- Label 14: "Context shifts query"

### Caption

Intent legitimation attack: normal interaction correctly blocks harmful queries despite benign memories (left), but accumulated benign memories shift the query's representation into the model's benign region, causing the safety filter to allow it (right), with 15.8-243.7% attack success increase.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- do NOT render them as labels.
2. **Semantic tags are INTERNAL** -- do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- do NOT render them.
4. **Engineering jargon** -- "PCA", "representation" should be briefly contextualized for L2 audience. Use "internal representation" rather than "activation space".
5. **Background MUST be warm cream (#f6f3e6)**.
6. **No generic flowchart aesthetics** -- no thick block arrows, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or numbered caption.
8. **No prompt leakage** -- do NOT render style keywords as visible text.

### Figure-Specific Rules

9. The 15.8-243.7% attack success increase range is from empirical studies -- do NOT round or alter the precision of these numbers.
10. Do NOT show actual harmful content in the examples -- use ellipsis or generic labels like "How to make..." without completing the harmful request.
11. The PCA visualization is a simplified 2D projection -- do NOT show specific axis labels or numerical coordinates.
12. The "representational shift" is the core mechanism -- the memories do NOT directly modify the safety filter, they change how the model internally represents the query.
13. Do NOT imply this attack requires sophisticated adversarial expertise -- the key insight is that NORMAL benign personalization can create this vulnerability unintentionally.
14. Do NOT present specific countermeasures as fully solving this problem -- it is an active research challenge.
15. "Intent legitimation" is a specific term from the security literature -- do NOT substitute "jailbreak" or "prompt injection" which are different attack categories.
16. The left panel (BLOCKED) and right panel (ALLOWED) must be visually distinct -- use the security_layer tag for the blocked state to emphasize the correct behavior, and confidence_low for the allowed state to emphasize the failure.

## Alt Text

Split-panel security diagram contrasting normal interaction where a harmful query is correctly blocked (left) against an intent legitimation attack where accumulated benign memories shift the query's internal representation into the model's benign region, bypassing the safety filter with 15.8-243.7% attack success increase (right).

## Image Embed

![Split-panel security diagram contrasting normal interaction where a harmful query is correctly blocked (left) against an intent legitimation attack where accumulated benign memories shift the query's internal representation into the model's benign region, bypassing the safety filter with 15.8-243.7% attack success increase (right).](docs/figures/repo-figures/assets/fig-persona-10-intent-legitimation.jpg)

*Intent legitimation attack: normal interaction correctly blocks harmful queries despite benign memories (left), but accumulated benign memories shift the query's representation into the model's benign region, causing the safety filter to allow it (right), with 15.8-243.7% attack success increase.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "persona-10",
    "title": "Intent Legitimation Attack via Personalization",
    "audience": "L2",
    "layout_template": "D"
  },
  "content_architecture": {
    "primary_message": "Personalization creates proportionally larger safety risks -- accumulated benign memories shift harmful queries into benign representation regions.",
    "layout_flow": "left-right-split",
    "key_structures": [
      {
        "name": "Normal: Benign Memories",
        "role": "confidence_high",
        "is_highlighted": false,
        "labels": ["Benign memories"]
      },
      {
        "name": "Normal: BLOCKED",
        "role": "security_layer",
        "is_highlighted": true,
        "labels": ["BLOCKED", "Correctly rejected"]
      },
      {
        "name": "Attack: Accumulated Memories",
        "role": "confidence_medium",
        "is_highlighted": true,
        "labels": ["Accumulated memories", "Context shifts query"]
      },
      {
        "name": "Attack: ALLOWED",
        "role": "confidence_low",
        "is_highlighted": true,
        "labels": ["ALLOWED", "Safety failure"]
      },
      {
        "name": "PCA Normal",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["Harmful cluster"]
      },
      {
        "name": "PCA Attack",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["Shifted to benign region"]
      },
      {
        "name": "Stats Bar",
        "role": "confidence_low",
        "is_highlighted": true,
        "labels": ["15.8-243.7% increase"]
      }
    ],
    "relationships": [
      {
        "from": "Normal memories",
        "to": "Harmful query",
        "type": "arrow",
        "label": "combined input"
      },
      {
        "from": "Harmful query",
        "to": "BLOCKED",
        "type": "arrow",
        "label": "correctly rejected"
      },
      {
        "from": "Accumulated memories",
        "to": "Same query",
        "type": "arrow",
        "label": "context shifts representation"
      },
      {
        "from": "Same query",
        "to": "ALLOWED",
        "type": "arrow",
        "label": "passes filter"
      },
      {
        "from": "PCA harmful",
        "to": "PCA benign",
        "type": "arrow",
        "label": "representational shift"
      }
    ],
    "callout_boxes": [
      {
        "heading": "PERSONALIZATION CREATES PROPORTIONALLY LARGER SAFETY RISKS",
        "body_text": "Accumulated benign memories create contextual legitimacy that shifts harmful queries into benign representation regions. 15.8-243.7% attack success increase.",
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
- [x] Audience level correct (L2)
- [x] Layout template identified (D)

## Status

- [x] Draft created
- [ ] Content reviewed
- [x] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25
- [ ] Embedded in documentation
