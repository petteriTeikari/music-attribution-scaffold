# fig-repo-21: The Inverse Scaling Paradox

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-repo-21 |
| **Title** | The Inverse Scaling Paradox: Smarter Models, More Vulnerable |
| **Audience** | L2 (PhD/Policy) |
| **Location** | docs/planning/mcp-security-production-research.md |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | C (Data-Viz) |

## Purpose

Visualize the counterintuitive finding from MCPSecBench that more capable AI models are MORE vulnerable to MCP-based attacks due to stronger instruction-following capabilities making them more susceptible to adversarial instructions in tool descriptions.

## Key Message

The inverse scaling paradox means upgrading to more capable models INCREASES security risk in MCP deployments — infrastructure-level defense is required, not model-level.

## Visual Concept

Data-viz layout with a conceptual scatter plot showing the directional trend of increasing attack success rate as model capability increases. An explanation callout below the chart clarifies the instruction-following hypothesis, and an implication box drives home the infrastructure defense requirement.

```
+-----------------------------------------------------------------------+
|  THE INVERSE SCALING PARADOX                                           |
|  ■ Smarter Models, More Vulnerable                                     |
+-----------------------------------------------------------------------+
|                                                                        |
|  ATTACK SUCCESS RATE vs MODEL CAPABILITY                               |
|                                                                        |
|       ▲ ASR                                                            |
|       │                                        ●  GPT-4o              |
|       │                                   ●  Claude 3.5               |
|       │                              ●                                 |
|       │                         ●                                      |
|       │                    ●                                           |
|       │               ●                                                |
|       │          ●                                                     |
|       │     ●  Less capable models                                     |
|       └─────────────────────────────────────▶  Model Capability        |
|                                                                        |
|  ┌─────────────────────────────────────────────────────────────────┐   |
|  │  WHY? Stronger instruction-following = more susceptible to     │   |
|  │  adversarial instructions embedded in tool descriptions        │   |
|  └─────────────────────────────────────────────────────────────────┘   |
|                                                                        |
|  IMPLICATION:                                                          |
|  Model upgrades ≠ Security upgrades                                    |
|  → Infrastructure-level defense required                               |
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
    content: "THE INVERSE SCALING PARADOX"
    role: title

  - id: chart_zone
    bounds: [80, 160, 1760, 520]
    role: data_visualization

  - id: explanation_zone
    bounds: [80, 720, 1760, 120]
    role: callout_box

  - id: implication_zone
    bounds: [80, 880, 1760, 140]
    role: callout_box

anchors:
  - id: y_axis
    position: [200, 200]
    size: [40, 460]
    role: data_flow
    label: "Attack Success Rate"

  - id: x_axis
    position: [200, 660]
    size: [1520, 40]
    role: data_flow
    label: "Model Capability"

  - id: trend_line
    position: [280, 580]
    size: [1360, 400]
    role: processing_stage
    label: "Upward trend — conceptual"

  - id: low_capability_cluster
    position: [300, 480]
    size: [400, 200]
    role: processing_stage
    label: "Less capable models (lower ASR)"

  - id: high_capability_cluster
    position: [1200, 220]
    size: [400, 200]
    role: processing_stage
    label: "More capable models (higher ASR)"

  - id: explanation_box
    position: [80, 720]
    size: [1760, 120]
    role: callout_box

  - id: implication_box
    position: [80, 880]
    size: [1760, 140]
    role: callout_box
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Conceptual scatter plot | `data_visualization` | ASR vs model capability directional trend |
| Y-axis | `data_flow` | Attack Success Rate (ascending) |
| X-axis | `data_flow` | Model Capability (ascending) |
| Trend direction | `processing_stage` | Positive correlation — higher capability, higher ASR |
| Explanation callout | `callout_box` | Instruction-following hypothesis |
| Implication callout | `callout_box` | Infrastructure defense requirement |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Model Capability | Attack Success Rate | trend | "positive correlation" |
| Explanation | Implication | logical | "therefore" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "WHY?" | Stronger instruction-following = more susceptible to adversarial instructions embedded in tool descriptions | below-chart |
| "IMPLICATION" | Model upgrades do not equal security upgrades — infrastructure-level defense required | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "ATTACK SUCCESS RATE"
- Label 2: "MODEL CAPABILITY"
- Label 3: "Less capable models"
- Label 4: "More capable models"
- Label 5: "Model upgrades ≠ Security"
- Label 6: "Infrastructure defense"
- Label 7: "Instruction-following"

### Caption (for embedding in documentation)

Conceptual visualization of the inverse scaling paradox from MCPSecBench showing that more capable AI models exhibit higher attack success rates in MCP deployments.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- Do NOT render them.
4. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color.
5. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
6. **No figure captions** -- do NOT render "Figure 21." or any numbered academic caption.
7. **No prompt leakage** -- do NOT render style keywords as visible text.

### Figure-Specific Rules

8. The inverse scaling paradox is from MCPSecBench (Cheng et al. 2025, arXiv:2508.13220). Do NOT attribute to MSB.
9. The chart is CONCEPTUAL — do NOT invent specific percentage values for individual models. Show the directional trend only.
10. The explanation (instruction-following capability) is the authors' stated hypothesis. Present as hypothesis, not proven fact.
11. Do NOT claim this applies to all security tasks — it is specific to MCP tool-based attacks.

## Alt Text

Conceptual scatter plot showing the inverse scaling paradox from MCPSecBench where attack success rate increases with model capability, demonstrating that more capable AI models are more vulnerable to MCP-based attacks due to stronger instruction-following capabilities.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Conceptual scatter plot showing the inverse scaling paradox where more capable models are more vulnerable to MCP attacks.](docs/figures/repo-figures/assets/fig-repo-21-inverse-scaling-paradox.jpg)

*Figure 21. The inverse scaling paradox from MCPSecBench showing that more capable AI models exhibit higher attack success rates in MCP deployments.*

### From this figure plan (relative)

![Inverse scaling paradox](../assets/fig-repo-21-inverse-scaling-paradox.jpg)

## Quality Checklist

- [x] Primary message clear in one sentence
- [x] Semantic tags used (no colors, hex codes, or font names in content spec)
- [x] ASCII layout sketched
- [x] Spatial anchors defined in YAML
- [x] Labels under 30 characters
- [x] Anti-hallucination rules listed
- [x] Alt text provided
- [x] Audience level correct (L2)
- [x] Layout template identified (C)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25
- [ ] Embedded in documentation
