# fig-repo-18: EU AI Act Compliance Timeline

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-repo-18 |
| **Title** | EU AI Act Compliance Timeline for Music Attribution |
| **Audience** | L2 (PhD/Policy) |
| **Location** | docs/prd/README.md, docs/knowledge-base/ |
| **Priority** | P2 (Medium) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | E (Steps) |

## Purpose

Show the EU AI Act regulatory timeline as it applies to music AI and attribution infrastructure, helping policy researchers and engineers understand which obligations are already active, which are approaching, and how the scaffold's A0-A3 assurance levels map to compliance requirements.

## Key Message

GPAI training data transparency obligations are already active (August 2025) — the scaffold's provenance tracking provides the traceability infrastructure needed for compliance.

## Visual Concept

Vertical timeline flowing downward with milestone markers. Left side shows EU AI Act dates, right side shows scaffold compliance capabilities. A horizontal band highlights "YOU ARE HERE" at the current date.

```
+-----------------------------------------------------------------------+
|  EU AI ACT COMPLIANCE TIMELINE                                         |
|  ■ Music Attribution Obligations                                       |
+-----------------------------------------------------------------------+
|                                                                        |
|  REGULATION                         SCAFFOLD CAPABILITY                |
|  ──────────                         ────────────────────               |
|                                                                        |
|  Aug 2024                                                              |
|  ○── AI Act enters force ─────────  (Framework published)              |
|  │                                                                     |
|  Feb 2025                                                              |
|  ○── Prohibited practices ────────  N/A (no prohibited uses)           |
|  │                                                                     |
|  Aug 2025    ★ ACTIVE NOW ★                                            |
|  ●── GPAI obligations ────────────  A0-A3 provenance tracking          |
|  │   Training data transparency     Audit trail (EU AI Act Art. 12)    |
|  │   Copyright compliance            MCP permission queries             |
|  │                                                                     |
|  Aug 2026                                                              |
|  ○── High-risk AI obligations ────  Confidence calibration reports     |
|  │   Conformity assessments          Conformal prediction bounds       |
|  │                                                                     |
|  Aug 2027                                                              |
|  ○── Full enforcement ────────────  Complete audit infrastructure      |
|  │   Penalties: €35M / 7% turnover                                     |
|                                                                        |
|  ┌───────────────────────────────────────────────────────────────────┐ |
|  │  Non-compliance: up to €35M or 7% of global turnover  ■  GPAI   │ |
|  │  providers MUST document training data sources                    │ |
|  └───────────────────────────────────────────────────────────────────┘ |
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
    content: "EU AI ACT COMPLIANCE TIMELINE"
    role: title

  - id: timeline_zone
    bounds: [80, 140, 1760, 780]
    role: content_area

  - id: callout_zone
    bounds: [80, 940, 1760, 100]
    role: callout_box

anchors:
  - id: milestone_2024_aug
    position: [200, 200]
    size: [200, 60]
    role: processing_stage

  - id: milestone_2025_feb
    position: [200, 340]
    size: [200, 60]
    role: processing_stage

  - id: milestone_2025_aug
    position: [200, 480]
    size: [200, 80]
    role: processing_stage

  - id: milestone_2026_aug
    position: [200, 640]
    size: [200, 60]
    role: processing_stage

  - id: milestone_2027_aug
    position: [200, 780]
    size: [200, 60]
    role: processing_stage

  - id: scaffold_gpai
    position: [800, 460]
    size: [900, 120]
    role: solution_component

  - id: scaffold_highrisk
    position: [800, 620]
    size: [900, 80]
    role: solution_component

  - id: scaffold_full
    position: [800, 760]
    size: [900, 80]
    role: solution_component
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Aug 2024 milestone | `processing_stage` | AI Act enters into force |
| Feb 2025 milestone | `processing_stage` | Prohibited AI practices ban |
| Aug 2025 milestone (active) | `processing_stage` | GPAI obligations begin — training data transparency |
| Aug 2026 milestone | `processing_stage` | High-risk AI system obligations |
| Aug 2027 milestone | `processing_stage` | Full enforcement with penalties |
| A0-A3 provenance | `solution_component` | Scaffold's assurance levels map to GPAI transparency |
| Conformal prediction | `solution_component` | Calibrated confidence for conformity assessments |
| Audit infrastructure | `solution_component` | Complete logging for full enforcement compliance |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Aug 2024 | Feb 2025 | arrow | timeline flow |
| Feb 2025 | Aug 2025 | arrow | timeline flow |
| Aug 2025 | Aug 2026 | arrow | timeline flow |
| Aug 2026 | Aug 2027 | arrow | timeline flow |
| Aug 2025 milestone | A0-A3 provenance | dashed | "addressed by" |
| Aug 2026 milestone | Conformal prediction | dashed | "addressed by" |
| Aug 2027 milestone | Audit infrastructure | dashed | "addressed by" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "PENALTY" | Non-compliance: up to EUR 35M or 7% of global turnover. GPAI providers MUST document training data sources. | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "AI Act enters force"
- Label 2: "Prohibited practices"
- Label 3: "GPAI obligations"
- Label 4: "High-risk obligations"
- Label 5: "Full enforcement"
- Label 6: "A0-A3 provenance tracking"
- Label 7: "Conformal prediction bounds"
- Label 8: "Complete audit trail"

### Caption (for embedding in documentation)

EU AI Act compliance timeline for music attribution, showing GPAI training data transparency obligations (active since August 2025) and how the scaffold's provenance tracking addresses each phase.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- Do NOT render them.
4. **Background MUST be warm cream (#f6f3e6)**.
5. **No generic flowchart aesthetics**.
6. **No figure captions** -- do NOT render "Figure 18." or any numbered caption.
7. **No prompt leakage**.

### Figure-Specific Rules

8. Dates MUST be accurate: Aug 2024 (entry into force), Feb 2025 (prohibited practices), Aug 2025 (GPAI obligations), Aug 2026 (high-risk), Aug 2027 (full enforcement).
9. Penalty amounts: EUR 35M or 7% of global annual turnover — these are the MAXIMUM penalties for the most serious violations.
10. GPAI = General Purpose AI. The obligations apply to providers of GPAI models, including those used for music generation.
11. Do NOT claim the scaffold provides "full compliance" — it provides the traceability infrastructure component.
12. The DLA Piper source for penalty amounts is authoritative (August 2025 analysis).

## Alt Text

EU AI Act compliance timeline for music attribution: vertical timeline from August 2024 entry into force through August 2027 full enforcement, highlighting active GPAI training data transparency obligations and the scaffold's A0-A3 provenance tracking as compliance infrastructure.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![EU AI Act compliance timeline for music attribution showing regulatory milestones and scaffold compliance capabilities.](docs/figures/repo-figures/assets/fig-repo-18-eu-ai-act-timeline.jpg)

*Figure 18. EU AI Act compliance timeline mapping regulatory obligations to scaffold provenance capabilities.*

### From this figure plan (relative)

![EU AI Act compliance timeline](../assets/fig-repo-18-eu-ai-act-timeline.jpg)

## Quality Checklist

- [x] Primary message clear in one sentence
- [x] Semantic tags used (no colors, hex codes, or font names in content spec)
- [x] ASCII layout sketched
- [x] Spatial anchors defined in YAML
- [x] Labels under 30 characters
- [x] Anti-hallucination rules listed
- [x] Alt text provided
- [x] Audience level correct (L2)
- [x] Layout template identified (E)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25
- [ ] Embedded in documentation
