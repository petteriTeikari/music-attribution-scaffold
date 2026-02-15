# fig-landscape-30: The Convergence Thesis: MIR + XAI + UQ = Attribution

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-landscape-30 |
| **Title** | The Convergence Thesis: MIR + XAI + UQ = Attribution |
| **Audience** | L4 (AI/ML) |
| **Location** | docs/planning/music-tech-landscape/, docs/planning/music-tech-figure-coverage-plan.md |
| **Priority** | P0 (Critical) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | A (Hero) |

## Purpose

This is one of the three signature Markovian novelty figures. It names and visualizes a convergence that no one has previously framed explicitly: music attribution is the intersection of three mature research fields -- Music Information Retrieval (25 years of ISMIR conferences), Explainable AI (post-2016 interpretability methods), and Uncertainty Quantification (conformal prediction, Bayesian calibration). The NOVELTY is the framing itself -- recognizing that the intersection zone is where all novel research lives, and that each pairwise intersection produces a distinct sub-discipline. This figure defines the intellectual territory of the entire research program.

## Key Message

Three mature research fields -- MIR (25 years), XAI (post-2016), and UQ (conformal prediction) -- are converging into a new discipline of music attribution, and the intersection zone is where all novel research lives.

## Visual Concept

A hero layout centered on a three-circle Venn diagram. Each circle is large enough to contain key papers and methods. The three pairwise intersections are labeled as distinct sub-disciplines. The triple intersection at the center is labeled "MUSIC ATTRIBUTION" as the new discipline. Outside each circle, foundational references are listed. The visual weight is on the CENTER -- the triple intersection -- with progressively less visual weight outward. Coral accent lines highlight the triple intersection zone.

```
+---------------------------------------------------------------+
|  THE CONVERGENCE THESIS                                        |
|  ■ Three Fields → One New Discipline                           |
+---------------------------------------------------------------+
|                                                                |
|                        MIR                                     |
|                  (25 years, ISMIR)                              |
|                ┌───────────────┐                               |
|               │ librosa        │                               |
|              │  essentia       │                                |
|             │   CLAP            │                               |
|            │    Chromaprint      │                              |
|           │                      │                              |
|          │   ┌──────────────┐    │                              |
|         │   │ Explainable   │    │                              |
|        │    │ Music Under-  │     │                             |
|       │     │ standing      │      │                            |
|      │      └───────┬───────┘       │                           |
|     │               │                │                          |
|    │  ┌─────────────┼─────────────┐   │                         |
|   │  │              │              │   │                        |
|  │   │   ┌──────────▼──────────┐   │    │                       |
|  │   │   │                     │   │    │                       |
|  │   │   │  MUSIC ATTRIBUTION  │   │    │                       |
|  │   │   │  The New Discipline │   │    │                       |
|  │   │   │  ■ ■ ■              │   │    │                       |
|  │   │   └──────────▲──────────┘   │    │                       |
|  │   │              │              │    │                       |
|  │   └──────────────┼─────────────┘    │                        |
|  │                  │                   │                        |
|  │  ┌───────────────┘───────────────┐   │                       |
|  │  │ Calibrated     Uncertainty-   │   │                       |
|  │  │ Music          Aware          │   │                       |
|  │  │ Similarity     Explanations   │   │                       |
|  │  └───────────────────────────────┘   │                       |
|  │         XAI               UQ         │                       |
|  │    (post-2016)      (conformal)      │                       |
|  │  ┌────────────┐  ┌────────────┐      │                       |
|  │  │ LIME, SHAP │  │ Vovk 2005  │      │                       |
|  │  │ Attention  │  │ Bayesian   │      │                       |
|  │  │ AudioGenX  │  │ SConU      │      │                       |
|  │  │ MusicLIME  │  │ Calibration│      │                       |
|  │  └────────────┘  └────────────┘      │                       |
|  └──────────────────────────────────────┘                       |
|                                                                |
+---------------------------------------------------------------+
```

## Spatial Anchors

```yaml
canvas:
  width: 1920
  height: 1080
  background: warm_cream

title_block:
  position: [60, 40]
  width: 1800
  height: 80
  elements:
    - type: heading_display
      text: "THE CONVERGENCE THESIS"
    - type: label_editorial
      text: "Three Fields → One New Discipline"

venn_center:
  position: [960, 540]
  note: "Center of the three-circle Venn diagram"

circle_mir:
  center: [960, 340]
  radius: 320
  label: "MIR"
  sublabel: "Music Information Retrieval (25 years)"
  anchor_conference: "ISMIR"
  key_tools:
    - { type: data_mono, text: "librosa (audio analysis)" }
    - { type: data_mono, text: "essentia (feature extraction)" }
    - { type: data_mono, text: "CLAP (contrastive language-audio)" }
    - { type: data_mono, text: "Chromaprint (acoustic fingerprinting)" }
    - { type: data_mono, text: "MIREX evaluations" }

circle_xai:
  center: [720, 700]
  radius: 320
  label: "XAI"
  sublabel: "Explainable AI (post-2016)"
  key_methods:
    - { type: data_mono, text: "LIME (Ribeiro 2016)" }
    - { type: data_mono, text: "SHAP (Lundberg 2017)" }
    - { type: data_mono, text: "Attention visualization" }
    - { type: data_mono, text: "AudioGenX (audio-specific XAI)" }
    - { type: data_mono, text: "MusicLIME (music-specific XAI)" }

circle_uq:
  center: [1200, 700]
  radius: 320
  label: "UQ"
  sublabel: "Uncertainty Quantification"
  key_methods:
    - { type: data_mono, text: "Conformal prediction (Vovk 2005)" }
    - { type: data_mono, text: "Bayesian updating" }
    - { type: data_mono, text: "Calibration curves" }
    - { type: data_mono, text: "SConU (selective conformal)" }
    - { type: data_mono, text: "Beigi UQ taxonomy" }

intersection_mir_xai:
  center: [840, 520]
  label: "Explainable Music Understanding"
  elements:
    - { type: label_editorial, text: "Why does this sound like X?" }
    - { type: data_mono, text: "Attention over spectrograms" }
    - { type: data_mono, text: "Feature importance for MIR tasks" }

intersection_mir_uq:
  center: [1080, 520]
  label: "Calibrated Music Similarity"
  elements:
    - { type: label_editorial, text: "How confident are we in this match?" }
    - { type: data_mono, text: "Conformal prediction on embeddings" }
    - { type: data_mono, text: "Calibrated fingerprint confidence" }

intersection_xai_uq:
  center: [960, 700]
  label: "Uncertainty-Aware Explanations"
  elements:
    - { type: label_editorial, text: "What do we know we don't know?" }
    - { type: data_mono, text: "Confidence intervals on SHAP values" }
    - { type: data_mono, text: "Selective prediction (abstain when uncertain)" }

triple_intersection:
  center: [960, 580]
  label: "MUSIC ATTRIBUTION"
  sublabel: "The New Discipline"
  elements:
    - { type: heading_display, text: "MUSIC ATTRIBUTION" }
    - { type: label_editorial, text: "Who made this, how confident are we, and can we explain why?" }
    - { type: callout_bar, text: "This intersection is where ALL novel research lives" }
    - { type: data_mono, text: "A0-A3 assurance = UQ + provenance" }
    - { type: data_mono, text: "TDA = MIR + XAI + confidence" }
    - { type: data_mono, text: "Conformal attribution = all three" }
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "THE CONVERGENCE THESIS" with coral accent square |
| Subtitle | `label_editorial` | "Three Fields -> One New Discipline" |
| MIR circle | `solution_component` | Music Information Retrieval: 25 years of ISMIR, librosa, essentia, CLAP, Chromaprint |
| XAI circle | `solution_component` | Explainable AI: LIME, SHAP, attention visualization, AudioGenX, MusicLIME |
| UQ circle | `solution_component` | Uncertainty Quantification: conformal prediction, Bayesian updating, SConU, calibration |
| MIR+XAI intersection | `branching_path` | Explainable Music Understanding: why does this sound like X? |
| MIR+UQ intersection | `branching_path` | Calibrated Music Similarity: how confident in this match? |
| XAI+UQ intersection | `branching_path` | Uncertainty-Aware Explanations: what do we know we don't know? |
| Triple intersection | `selected_option` | MUSIC ATTRIBUTION: the new discipline at the center |
| Key papers per zone | `data_mono` | Specific references placed in their correct Venn zone |
| Accent markers | `callout_bar` | Coral accent highlighting the triple intersection |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| MIR | MIR+XAI intersection | convergence | "Audio features + interpretability" |
| XAI | MIR+XAI intersection | convergence | "Explanation methods + music domain" |
| MIR | MIR+UQ intersection | convergence | "Similarity metrics + calibration" |
| UQ | MIR+UQ intersection | convergence | "Confidence bounds + audio matching" |
| XAI | XAI+UQ intersection | convergence | "Explanations + uncertainty awareness" |
| UQ | XAI+UQ intersection | convergence | "Prediction intervals + interpretability" |
| MIR+XAI | Triple center | convergence | "Explainable music + confidence" |
| MIR+UQ | Triple center | convergence | "Calibrated similarity + explanations" |
| XAI+UQ | Triple center | convergence | "Uncertainty-aware explanations + music" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| The Novelty | "No one has framed music attribution as the intersection of MIR + XAI + UQ before -- this figure names the convergence" | Top-right corner |
| Research Implication | "Each pairwise intersection is a publishable sub-discipline; the triple intersection is the PhD thesis" | Bottom center |
| Maturity Asymmetry | "MIR: 25 years mature. XAI: 10 years. UQ (conformal): 20 years but not yet applied to music. The convergence is 3 years old." | Left margin |
| Key Question | "Who made this, how confident are we, and can we explain why?" | Inside triple intersection |

## Text Content

### Labels (Max 30 chars each)

- MIR (Music Info Retrieval)
- XAI (Explainable AI)
- UQ (Uncertainty Quantificn)
- Explainable Music Understdg
- Calibrated Music Similarity
- Uncertainty-Aware Explanatns
- MUSIC ATTRIBUTION
- librosa
- essentia
- CLAP
- Chromaprint
- LIME (Ribeiro 2016)
- SHAP (Lundberg 2017)
- AudioGenX
- MusicLIME
- Conformal Prediction
- Bayesian Updating
- SConU
- Beigi UQ Taxonomy
- Vovk 2005
- A0-A3 Assurance Levels
- TDA Methods
- ISMIR Conference

### Caption (for embedding in documentation)

Music attribution emerges as a new discipline at the intersection of three mature research fields: Music Information Retrieval (25 years of ISMIR conferences, librosa, essentia, CLAP, Chromaprint), Explainable AI (post-2016 interpretability: LIME, SHAP, attention visualization, AudioGenX, MusicLIME), and Uncertainty Quantification (conformal prediction via Vovk 2005, Bayesian updating, SConU, calibration). Each pairwise intersection produces a distinct sub-discipline -- explainable music understanding (MIR+XAI), calibrated music similarity (MIR+UQ), and uncertainty-aware explanations (XAI+UQ) -- while the triple intersection defines music attribution proper: answering "who made this, how confident are we, and can we explain why?" This convergence framing is novel -- no prior work has explicitly named music attribution as the MIR+XAI+UQ intersection.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- do NOT render them as labels.
2. **Semantic tags are INTERNAL** -- do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- do NOT render them.
4. **Background MUST be warm cream (#f6f3e6)**.
5. **No generic flowchart aesthetics** -- no thick block arrows, no PowerPoint look.
6. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or numbered caption.
7. **No prompt leakage** -- do NOT render style keywords as visible text.

### Figure-Specific Rules

1. The Venn diagram has exactly THREE circles -- do NOT add a fourth or reduce to two.
2. Each circle represents a RESEARCH FIELD, not a technology or product -- do NOT substitute tools for fields.
3. MIR is specifically MUSIC Information Retrieval (25 years, ISMIR) -- do NOT generalize to "audio processing."
4. XAI is specifically post-2016 interpretability methods -- do NOT include pre-2016 ML interpretability.
5. UQ is specifically CONFORMAL PREDICTION and Bayesian methods -- do NOT reduce to "error bars" or "standard deviation."
6. The pairwise intersections are DISTINCT sub-disciplines, not just overlapping topics -- each has its own research questions.
7. The triple intersection IS music attribution -- do NOT position music attribution as adjacent to or outside the Venn diagram.
8. Vovk 2005 is the specific foundational reference for conformal prediction -- do NOT omit or replace.
9. SConU (Selective Conformal Uncertainty) is a SPECIFIC method -- do NOT generalize.
10. Beigi UQ taxonomy is a SPECIFIC reference -- do NOT generalize to "taxonomy of uncertainty."
11. Do NOT imply that any single existing tool or paper occupies the triple intersection -- the convergence is EMERGENT.
12. The claim "no one has framed this before" is the NOVELTY -- do NOT weaken to "few have framed this."
13. Do NOT draw the circles with equal sizes -- MIR is the largest (25 years), UQ medium (20 years but niche in music), XAI smallest (10 years).
14. The key question "Who made this, how confident are we, and can we explain why?" must appear in or near the triple intersection.

## Alt Text

Three-circle Venn: MIR, XAI, and UQ converge into music attribution at the triple intersection center.

## JSON Export Block

```json
{
  "id": "fig-landscape-30",
  "title": "The Convergence Thesis: MIR + XAI + UQ = Attribution",
  "audience": "L4",
  "priority": "P0",
  "layout": "A",
  "aspect_ratio": "16:9",
  "group": "landscape",
  "markov_phase": "Speculate",
  "novelty": 5,
  "signature_figure": true,
  "fields": [
    {
      "name": "MIR",
      "full_name": "Music Information Retrieval",
      "maturity_years": 25,
      "anchor_conference": "ISMIR",
      "key_tools": ["librosa", "essentia", "CLAP", "Chromaprint"],
      "key_evaluations": ["MIREX"]
    },
    {
      "name": "XAI",
      "full_name": "Explainable AI",
      "maturity_years": 10,
      "founding_year": 2016,
      "key_methods": ["LIME (Ribeiro 2016)", "SHAP (Lundberg 2017)", "Attention visualization"],
      "music_specific": ["AudioGenX", "MusicLIME"]
    },
    {
      "name": "UQ",
      "full_name": "Uncertainty Quantification",
      "maturity_years": 20,
      "foundational_ref": "Vovk 2005 (conformal prediction)",
      "key_methods": ["Conformal prediction", "Bayesian updating", "Calibration curves", "SConU"],
      "taxonomy_ref": "Beigi UQ taxonomy"
    }
  ],
  "pairwise_intersections": [
    {
      "fields": ["MIR", "XAI"],
      "name": "Explainable Music Understanding",
      "question": "Why does this sound like X?"
    },
    {
      "fields": ["MIR", "UQ"],
      "name": "Calibrated Music Similarity",
      "question": "How confident are we in this match?"
    },
    {
      "fields": ["XAI", "UQ"],
      "name": "Uncertainty-Aware Explanations",
      "question": "What do we know we don't know?"
    }
  ],
  "triple_intersection": {
    "name": "MUSIC ATTRIBUTION",
    "subtitle": "The New Discipline",
    "key_question": "Who made this, how confident are we, and can we explain why?",
    "novel_claim": "No prior work explicitly names music attribution as the MIR+XAI+UQ intersection"
  },
  "semantic_tags_used": [
    "heading_display", "label_editorial", "solution_component", "branching_path",
    "selected_option", "data_mono", "callout_bar"
  ]
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
- [x] Audience level correct (L1/L2/L3/L4)
- [x] Layout template identified (A/B/C/D/E)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25
- [ ] Embedded in documentation
