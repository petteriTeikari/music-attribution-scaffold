# fig-theory-01: The Oracle Problem -- ELI5 (Mixing Paint Analogy)

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-theory-01 |
| **Title** | The Oracle Problem -- ELI5 (Mixing Paint Analogy) |
| **Audience** | L1 (Music Industry Professional) |
| **Complexity** | L1 (concept introduction -- no code, real-world analogy) |
| **Location** | docs/theory/oracle-problem.md, README.md theory section |
| **Priority** | P0 (Critical) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure introduces the Oracle Problem to non-technical readers using a universally understood analogy: mixing paint. It answers: "Why can't we just look at AI-generated music and figure out whose work went into it?"

The key message is: "Once creative works are blended inside an AI model, separating the individual contributions is as impossible as unmixing paint -- you cannot reverse-engineer the original ingredients from the final result."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  THE ORACLE PROBLEM                                            |
|  ■ Why AI Attribution Is Hard                                  |
+---------------------------------------------------------------+
|                                                                |
|  STEP 1: INGREDIENTS          STEP 2: BLEND        STEP 3:    |
|  ──────────────────          ─────────────         RESULT      |
|                                                    ──────      |
|  ┌──────────┐                                                  |
|  │ RED tube │────┐           ┌──────────┐     ┌──────────┐    |
|  │ (Artist A)│    │          │          │     │          │    |
|  └──────────┘    ├──────►   │ BLENDER  │────►│ UNIFORM  │    |
|  ┌──────────┐    │          │  (Model) │     │ PURPLE   │    |
|  │ BLUE tube│────┤          │          │     │          │    |
|  │ (Artist B)│    │          └──────────┘     └──────────┘    |
|  └──────────┘    │                                 │          |
|  ┌──────────┐    │                                 ▼          |
|  │WHITE tube│────┘                            ┌──────────┐    |
|  │ (Artist C)│                                 │  ???     │    |
|  └──────────┘                                 │ Which    │    |
|                                                │ paint    │    |
|                                                │ made the │    |
|                                                │ purple?  │    |
|                                                └──────────┘    |
|                                                                |
+---------------------------------------------------------------+
|  ■ TRANSLATION                                                 |
|  Paint tubes = training data from individual artists           |
|  Blender = AI model training (gradient descent, weight avg.)   |
|  Purple = generated output. You CANNOT unmix it.               |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "THE ORACLE PROBLEM" in editorial ALL-CAPS with coral accent square |
| Subtitle | `label_editorial` | "Why AI Attribution Is Hard" in Plus Jakarta Sans caps |
| Paint tube A (Red) | `stakeholder_artist` | Red paint tube labeled "Artist A" -- represents one creator's training data |
| Paint tube B (Blue) | `stakeholder_artist` | Blue paint tube labeled "Artist B" -- represents second creator |
| Paint tube C (White) | `stakeholder_artist` | White paint tube labeled "Artist C" -- represents third creator |
| Blender | `processing_stage` | Central blending vessel representing AI model training |
| Uniform purple output | `problem_statement` | Single-color output representing generated content |
| Question mark callout | `problem_statement` | "Which paint made the purple?" -- the unanswerable question |
| Flow arrows (tubes to blender) | `data_flow` | Solid arrows showing inputs being combined |
| Flow arrow (blender to output) | `data_flow` | Solid arrow showing irreversible transformation |
| Translation box | `callout_box` | Three-line mapping: tubes=data, blender=model, purple=output |
| Step labels I/II/III | `section_numeral` | Sequential step markers in editorial style |

## Anti-Hallucination Rules

1. This is an ANALOGY figure -- do not include any code, API names, or engineering terminology.
2. The analogy is specifically PAINT MIXING, not cooking, chemistry, or any other metaphor.
3. Do NOT claim that unmixing is "difficult" -- it is IMPOSSIBLE. This is the core message.
4. Do NOT suggest that watermarking or fingerprinting solves the Oracle Problem -- they are complementary but do not reverse the mixing.
5. The Oracle Problem is a FUNDAMENTAL LIMITATION, not a temporary engineering challenge.
6. Three paint tubes only -- do not add more or fewer to the analogy.
7. Background must be warm cream (#f6f3e6), not white or gray.
8. Do NOT include any musical notation, waveforms, or audio imagery -- this is purely the paint analogy.

## Alt Text

Concept diagram: three paint tubes labeled Artist A, B, and C flow into a blender representing AI model training, producing uniform purple output that cannot be unmixed -- illustrating the oracle problem in music attribution, where transparent confidence scoring is impossible after creative works are blended during generative AI training, a fundamental limitation for open-source attribution scaffolds.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Concept diagram: three paint tubes labeled Artist A, B, and C flow into a blender representing AI model training, producing uniform purple output that cannot be unmixed -- illustrating the oracle problem in music attribution, where transparent confidence scoring is impossible after creative works are blended during generative AI training, a fundamental limitation for open-source attribution scaffolds.](docs/figures/repo-figures/assets/fig-theory-01-oracle-problem-eli5.jpg)

*Figure 1. The Oracle Problem explained through a paint-mixing analogy: once creative works are blended inside an AI model through gradient descent and weight averaging, separating individual contributions is fundamentally impossible -- motivating the attribution-by-design approach used in this scaffold.*

### From this figure plan (relative)

![Concept diagram: three paint tubes labeled Artist A, B, and C flow into a blender representing AI model training, producing uniform purple output that cannot be unmixed -- illustrating the oracle problem in music attribution, where transparent confidence scoring is impossible after creative works are blended during generative AI training, a fundamental limitation for open-source attribution scaffolds.](../assets/fig-theory-01-oracle-problem-eli5.jpg)
