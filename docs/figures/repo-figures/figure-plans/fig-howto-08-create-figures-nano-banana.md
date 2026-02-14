# fig-howto-08: How to Create Figures (Nano Banana Pro)

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-howto-08 |
| **Title** | How to Create Figures (Nano Banana Pro) |
| **Audience** | L2 (PhD Student / Policy Researcher) |
| **Complexity** | L2 (structural mapping) |
| **Location** | docs/figures/repo-figures/README.md, docs/contributing.md |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure documents the figure creation workflow used by this project -- a structured pipeline from reading the plan file through style guide application to generation in Nano Banana Pro and quality verification. It answers: "How do I create a new figure that matches the visual identity of this project?"

The key message is: "Figure creation follows a six-step pipeline: read the figure plan, load the style guide, compose the generation prompt, generate in Nano Banana Pro, verify against the quality checklist, and commit to the repo. Plans define WHAT (content), the style guide defines HOW (visual)."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  HOW TO CREATE FIGURES                                         |
|  ■ Nano Banana Pro Workflow                                    |
+---------------------------------------------------------------+
|                                                                |
|  I. READ FIGURE PLAN               II. READ STYLE GUIDE       |
|  ───────────────────               ─────────────────────       |
|  ┌───────────────────┐             ┌───────────────────┐      |
|  │ figure-plans/      │             │ STYLE-GUIDE-      │      |
|  │  fig-repo-NN.md    │             │  REPO.md           │      |
|  │                    │             │                    │      |
|  │ ■ ASCII layout     │             │ ■ Color palette    │      |
|  │ ■ Content elements │             │ ■ Typography       │      |
|  │ ■ Semantic tags    │             │ ■ Layout rules     │      |
|  │ ■ Anti-halluc.     │             │ ■ Scoring rubric   │      |
|  └────────┬──────────┘             └────────┬──────────┘      |
|            └──────────────┬─────────────────┘                  |
|                           v                                    |
|  III. COMPOSE PROMPT                                           |
|  ───────────────────                                           |
|  ┌─────────────────────────────────────────────┐              |
|  │ Combine: plan content + style rules          │              |
|  │ ■ Paste figure plan (WHAT to show)           │              |
|  │ ■ Paste style guide (HOW it should look)     │              |
|  │ ■ Add "warm cream background #f6f3e6"        │              |
|  │ ■ Specify 1200x900 or target dimensions      │              |
|  └──────────────────────┬──────────────────────┘              |
|                          v                                      |
|  IV. GENERATE IN NANO BANANA PRO                               |
|  ───────────────────────────────                               |
|  ┌─────────────────────────────────────────────┐              |
|  │ ■ Upload prompt to Nano Banana Pro           │              |
|  │ ■ Generate image                             │              |
|  │ ■ Iterate if needed (refine prompt)          │              |
|  └──────────────────────┬──────────────────────┘              |
|                          v                                      |
|  V. VERIFY QUALITY                  VI. COMMIT                 |
|  ─────────────────                  ─────────                  |
|  ┌───────────────────┐             ┌───────────────────┐      |
|  │ Quality checklist: │             │ docs/figures/      │      |
|  │ ■ Score >= 21/25   │     ──>     │  repo-figures/     │      |
|  │ ■ Background cream │             │  generated/        │      |
|  │ ■ No hex visible   │             │  fig-repo-NN.png   │      |
|  │ ■ Fonts correct    │             │                    │      |
|  │ ■ Alt text matches │             │ git add + commit   │      |
|  └───────────────────┘             └───────────────────┘      |
|                                                                |
+---------------------------------------------------------------+
|  ■ Content/style decoupling: plans define WHAT, guide HOW     |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "HOW TO CREATE FIGURES" in Instrument Serif ALL-CAPS with coral accent square |
| Subtitle | `label_editorial` | "Nano Banana Pro Workflow" in Plus Jakarta Sans caps |
| Step I: Figure plan | `processing_stage` | Reading the figure plan file with its content elements (ASCII layout, semantic tags, anti-hallucination rules) |
| Step II: Style guide | `processing_stage` | Reading the style guide for visual specifications (palette, typography, layout, scoring) |
| Step III: Compose prompt | `processing_stage` | Combining plan content with style rules into a generation prompt |
| Step IV: Generate | `processing_stage` | Uploading to Nano Banana Pro and generating the image |
| Step V: Verify | `processing_stage` | Quality checklist verification (score >= 21/25, background color, no visible hex codes) |
| Step VI: Commit | `processing_stage` | Saving to generated/ directory and committing to repo |
| Flow arrows (I+II merge to III, then sequential) | `data_flow` | Two inputs merge, then linear flow through remaining steps |
| Roman numerals I-VI | `section_numeral` | Step headers in editorial style |
| File paths | `data_mono` | IBM Plex Mono for file path references |
| Footer callout | `callout_box` | "Content/style decoupling: plans define WHAT, guide HOW" |

## Anti-Hallucination Rules

1. Nano Banana Pro is the specific image generation tool used -- do not substitute DALL-E, Midjourney, or other tools.
2. The quality score threshold is >= 21/25 as defined in STYLE-GUIDE-REPO.md -- do not change this number.
3. Figure plans live in `docs/figures/repo-figures/figure-plans/` -- not in a different directory.
4. The style guide is `STYLE-GUIDE-REPO.md` -- not a generic style guide.
5. The content/style decoupling principle is central: plans use semantic tags (not colors or fonts), and the style guide maps tags to visual properties.
6. Generated figures go in `docs/figures/repo-figures/generated/` -- not alongside the plans.
7. Background color is always warm cream (#f6f3e6) -- this must be specified in every prompt.
8. The quality checklist includes: no visible hex codes, no visible font names, no visible semantic tags -- these are internal instructions only.
9. Background must be warm cream (#f6f3e6), not white or gray.

## Alt Text

Workflow diagram: six-step figure creation pipeline for the music attribution scaffold documentation, from reading the figure plan and style guide through prompt composition and Nano Banana Pro image generation to quality verification and repository commit -- demonstrating content-style decoupling where plans define what to show and the style guide defines how, ensuring consistent open-source visual identity.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Workflow diagram: six-step figure creation pipeline for the music attribution scaffold documentation, from reading the figure plan and style guide through prompt composition and Nano Banana Pro image generation to quality verification and repository commit -- demonstrating content-style decoupling where plans define what to show and the style guide defines how, ensuring consistent open-source visual identity.](docs/figures/repo-figures/assets/fig-howto-08-create-figures-nano-banana.jpg)

*Figure creation workflow for the Music Attribution Scaffold. The content-style decoupling principle separates semantic figure plans (what to communicate) from the visual style guide (how it should look), enabling reproducible, quality-gated figure generation via Nano Banana Pro with a minimum score threshold of 21/25 (Teikari, 2026).*

### From this figure plan (relative)

![Workflow diagram: six-step figure creation pipeline for the music attribution scaffold documentation, from reading the figure plan and style guide through prompt composition and Nano Banana Pro image generation to quality verification and repository commit -- demonstrating content-style decoupling where plans define what to show and the style guide defines how, ensuring consistent open-source visual identity.](../assets/fig-howto-08-create-figures-nano-banana.jpg)
