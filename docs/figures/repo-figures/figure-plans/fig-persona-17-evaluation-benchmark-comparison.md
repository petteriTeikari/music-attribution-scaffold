# fig-persona-17: Evaluation Benchmark Comparison

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-persona-17 |
| **Title** | Evaluation Benchmark Comparison: PersonaGym to RoleBench |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/knowledge-base/, docs/planning/ |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | B (Multi-Panel) |

## Purpose

Compares five major persona evaluation benchmarks across scale, methodology, and key findings. Highlights the counterintuitive PersonaGym result that model size does not correlate with persona adherence. Answers: "Which benchmark should we use to evaluate persona consistency, and what surprising findings exist?"

## Key Message

GPT-4 had identical PersonaScore to LLaMA-3-8B -- model size does not guarantee better persona adherence, making benchmark selection critical for attribution agent evaluation.

## Visual Concept

Five panel blocks arranged in a staggered layout (3 top, 2 bottom or similar asymmetric arrangement). Each panel shows: benchmark name, scale (number of personas/samples/conversations), methodology (task types or evaluation dimensions), and one key finding. A shared highlight box emphasizes the PersonaGym surprise finding. Metric scales are shown in monospace for scannability.

```
+-----------------------------------------------------------------------+
|  EVALUATION BENCHMARK COMPARISON                                       |
|  -- Five Frameworks for Persona Adherence                              |
+-----------------------------------------------------------------------+
|                                                                        |
|  ┌────────────────────────┐  ┌────────────────────────┐               |
|  │ I. PERSONAGYM           │  │ II. CHARACTERBENCH      │               |
|  │ ═══════════════         │  │ ═══════════════════     │               |
|  │                         │  │                         │               |
|  │ Scale:                  │  │ Scale:                  │               |
|  │   200 personas          │  │   22,859 samples        │               |
|  │   10,000 interactions   │  │   3,956 characters      │               |
|  │                         │  │                         │               |
|  │ Method:                 │  │ Method:                 │               |
|  │   5 task categories     │  │   11 dimensions         │               |
|  │   automated scoring     │  │   human + automated     │               |
|  │                         │  │                         │               |
|  │ Finding:                │  │ Finding:                │               |
|  │   GPT-4 = LLaMA-3-8B   │  │   Knowledge grounding   │               |
|  │   on PersonaScore       │  │   weakest dimension     │               |
|  │   ◆ MODEL SIZE ≠        │  │                         │               |
|  │     PERSONA ADHERENCE   │  │                         │               |
|  └────────────────────────┘  └────────────────────────┘               |
|                                                                        |
|  ┌───────────────────┐  ┌──────────────────┐  ┌───────────────────┐   |
|  │ III. INCHARACTER   │  │ IV. COSER         │  │ V. ROLEBENCH      │   |
|  │ ════════════════   │  │ ════════════      │  │ ═══════════════   │   |
|  │                    │  │                   │  │                   │   |
|  │ Scale:             │  │ Scale:            │  │ Scale:            │   |
|  │   32 characters    │  │   29,798 convs    │  │   168,093 samples │   |
|  │   14 psych scales  │  │   17,966 chars    │  │   100 roles       │   |
|  │                    │  │                   │  │                   │   |
|  │ Method:            │  │ Method:           │  │ Method:           │   |
|  │   MBTI, Big Five,  │  │   Acting method-  │  │   Instruction-    │   |
|  │   psychological    │  │   ology (Stanis-  │  │   tuning based,   │   |
|  │   measurement      │  │   lavski)         │  │   role profiles   │   |
|  │                    │  │                   │  │                   │   |
|  │ Finding:           │  │ Finding:          │  │ Finding:          │   |
|  │   LLMs have        │  │   Acting-based    │  │   Largest scale,  │   |
|  │   consistent       │  │   prompts beat    │  │   role-specific   │   |
|  │   personality      │  │   generic ones    │  │   fine-tuning     │   |
|  │   profiles         │  │                   │  │   effective       │   |
|  └───────────────────┘  └──────────────────┘  └───────────────────┘   |
|                                                                        |
|  -- GPT-4 HAD IDENTICAL PERSONASCORE TO LLAMA-3-8B                     |
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
    content: "EVALUATION BENCHMARK COMPARISON"
    role: title

  - id: top_row
    bounds: [40, 140, 1840, 400]
    content: "PersonaGym and CharacterBench"
    role: content_area

  - id: bottom_row
    bounds: [40, 560, 1840, 340]
    content: "InCharacter, CoSER, RoleBench"
    role: content_area

  - id: callout_zone
    bounds: [40, 940, 1840, 100]
    content: "GPT-4 HAD IDENTICAL PERSONASCORE TO LLAMA-3-8B"
    role: callout_box

anchors:
  - id: personagym_panel
    position: [80, 160]
    size: [860, 360]
    role: processing_stage
    label: "I. PERSONAGYM"

  - id: characterbench_panel
    position: [980, 160]
    size: [860, 360]
    role: processing_stage
    label: "II. CHARACTERBENCH"

  - id: incharacter_panel
    position: [80, 580]
    size: [560, 300]
    role: processing_stage
    label: "III. INCHARACTER"

  - id: coser_panel
    position: [680, 580]
    size: [560, 300]
    role: processing_stage
    label: "IV. COSER"

  - id: rolebench_panel
    position: [1280, 580]
    size: [560, 300]
    role: processing_stage
    label: "V. ROLEBENCH"

  - id: surprise_highlight
    position: [120, 420]
    size: [400, 60]
    role: problem_statement
    label: "MODEL SIZE != PERSONA ADHERENCE"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| PersonaGym panel | `processing_stage` | 200 personas, 5 task categories, finding: GPT-4 = LLaMA-3-8B on PersonaScore |
| CharacterBench panel | `processing_stage` | 22,859 samples, 11 evaluation dimensions, finding: knowledge grounding is weakest |
| InCharacter panel | `processing_stage` | 32 characters, 14 psychological scales (MBTI, Big Five), finding: LLMs show consistent personality |
| CoSER panel | `processing_stage` | 29,798 conversations, acting methodology (Stanislavski), finding: acting prompts beat generic |
| RoleBench panel | `processing_stage` | 168,093 samples, 100 roles, finding: role-specific fine-tuning effective |
| Surprise highlight | `problem_statement` | Emphasized finding that model size does not predict persona adherence |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| PersonaGym | CharacterBench | dashed | "complementary approaches" |
| InCharacter | CoSER | dashed | "psychological vs acting" |
| All benchmarks | Surprise finding | dashed | "shared implication" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "THE SURPRISE" | "GPT-4 HAD IDENTICAL PERSONASCORE TO LLAMA-3-8B" | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "I. PERSONAGYM"
- Label 2: "II. CHARACTERBENCH"
- Label 3: "III. INCHARACTER"
- Label 4: "IV. COSER"
- Label 5: "V. ROLEBENCH"
- Label 6: "200 personas"
- Label 7: "22,859 samples"
- Label 8: "32 characters"
- Label 9: "29,798 conversations"
- Label 10: "168,093 samples"
- Label 11: "5 task categories"
- Label 12: "11 dimensions"
- Label 13: "14 psychological scales"
- Label 14: "Acting methodology"
- Label 15: "MODEL SIZE != ADHERENCE"

### Caption (for embedding in documentation)

Five persona evaluation benchmarks compared: PersonaGym (200 personas, automated scoring), CharacterBench (22,859 samples, 11 dimensions), InCharacter (psychological measurement), CoSER (acting methodology), and RoleBench (168,093 samples) -- with the key finding that GPT-4 scored identically to LLaMA-3-8B on persona adherence.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `processing_stage`, `problem_statement`, `callout_box` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- Benchmark names and metrics are appropriate for L3 audience. Keep statistical terms precise.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption. The editorial display title is allowed.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. PersonaGym finding is specifically that GPT-4 and LLaMA-3-8B had identical PersonaScore. Do NOT generalize to "all large models fail."
10. CharacterBench has exactly 11 evaluation dimensions. Do NOT list them unless space permits -- cite the count.
11. InCharacter uses established psychological instruments (MBTI, Big Five). Do NOT invent additional scales.
12. CoSER methodology is explicitly based on Stanislavski acting method. Do NOT confuse with generic "role-playing."
13. RoleBench is the largest benchmark at 168,093 samples. Do NOT understate its scale.
14. All benchmark names are from published papers. Do NOT alter the names or attribute them to incorrect authors.
15. The "GPT-4" reference is to the model available during PersonaGym evaluation. Do NOT assume this applies to later model versions.

## Alt Text

Multi-panel comparison of five persona evaluation benchmarks -- PersonaGym, CharacterBench, InCharacter, CoSER, and RoleBench -- with scale, methodology, and key findings including the surprise that GPT-4 matched LLaMA-3-8B on persona adherence scoring.

## Image Embed

![Multi-panel comparison of five persona evaluation benchmarks -- PersonaGym, CharacterBench, InCharacter, CoSER, and RoleBench -- with scale, methodology, and key findings including the surprise that GPT-4 matched LLaMA-3-8B on persona adherence scoring.](docs/figures/repo-figures/assets/fig-persona-17-evaluation-benchmark-comparison.jpg)

*Five persona evaluation benchmarks compared: PersonaGym (200 personas, automated scoring), CharacterBench (22,859 samples, 11 dimensions), InCharacter (psychological measurement), CoSER (acting methodology), and RoleBench (168,093 samples) -- with the key finding that GPT-4 scored identically to LLaMA-3-8B on persona adherence.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "persona-17",
    "title": "Evaluation Benchmark Comparison: PersonaGym to RoleBench",
    "audience": "L3",
    "layout_template": "B"
  },
  "content_architecture": {
    "primary_message": "GPT-4 had identical PersonaScore to LLaMA-3-8B -- model size does not guarantee persona adherence.",
    "layout_flow": "left-to-right",
    "key_structures": [
      {
        "name": "PersonaGym Panel",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["I. PERSONAGYM", "200 personas", "GPT-4 = LLaMA-3-8B"]
      },
      {
        "name": "CharacterBench Panel",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["II. CHARACTERBENCH", "22,859 samples", "11 dimensions"]
      },
      {
        "name": "InCharacter Panel",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["III. INCHARACTER", "32 characters", "14 psych scales"]
      },
      {
        "name": "CoSER Panel",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["IV. COSER", "29,798 conversations", "Acting methodology"]
      },
      {
        "name": "RoleBench Panel",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["V. ROLEBENCH", "168,093 samples", "100 roles"]
      }
    ],
    "relationships": [
      {
        "from": "PersonaGym",
        "to": "CharacterBench",
        "type": "dashed",
        "label": "complementary automated evaluation approaches"
      },
      {
        "from": "InCharacter",
        "to": "CoSER",
        "type": "dashed",
        "label": "psychological vs acting methodology"
      }
    ],
    "callout_boxes": [
      {
        "heading": "THE SURPRISE",
        "body_text": "GPT-4 HAD IDENTICAL PERSONASCORE TO LLAMA-3-8B",
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
- [x] Anti-hallucination rules listed
- [x] Alt text provided (125 chars max)
- [x] JSON export block included
- [x] Audience level correct (L3)
- [x] Layout template identified (B)

## Status

- [x] Draft created
- [ ] Content reviewed
- [x] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
