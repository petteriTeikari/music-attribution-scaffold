# fig-theory-02: The Oracle Problem -- Technical Pipeline

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-theory-02 |
| **Title** | The Oracle Problem -- Technical Pipeline |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 (code terms, API references, implementation detail) |
| **Location** | docs/theory/oracle-problem.md |
| **Priority** | P0 (Critical) |
| **Dimensions** | 1200 x 675px (16:9) |

## Purpose & Key Message

This figure shows the Oracle Problem at a technical level for engineers who need to understand why post-hoc attribution from model weights is computationally intractable. It answers: "Where exactly in the ML pipeline does attribution information get destroyed?"

The key message is: "Attribution information is destroyed during training through tokenization, gradient descent, and weight averaging -- the analog hole means digital provenance cannot survive the training process."

## Visual Concept (ASCII Layout)

```
+-------------------------------------------------------------------------------+
|  THE ORACLE PROBLEM — TECHNICAL PIPELINE                                       |
|  ■ Where Attribution Gets Destroyed                                            |
+-------------------------------------------------------------------------------+
|                                                                                |
|  INPUT                    TRAINING (Black Box)                    OUTPUT        |
|  ─────                    ────────────────────                    ──────        |
|                                                                                |
|  ┌──────────┐    ┌─────────────────────────────────────┐    ┌──────────┐      |
|  │ Creator  │    │                                     │    │Generated │      |
|  │ Audio    │    │  Tokenization   Gradient   Weight   │    │  Output  │      |
|  │ (FLAC)   │───►│  ┌─────┐       Descent    Avg.     │───►│          │      |
|  ├──────────┤    │  │Tok.A│──►──┐  ┌────┐   ┌────┐   │    │  ???     │      |
|  │ Creator  │    │  └─────┘     ├─►│∇L  │──►│W̄   │   │    │          │      |
|  │ MIDI     │───►│  ┌─────┐     │  │    │   │    │   │    │ Who made │      |
|  │ (stems)  │    │  │Tok.B│──►──┤  └────┘   └────┘   │    │  this?   │      |
|  ├──────────┤    │  └─────┘     │                     │    │          │      |
|  │ Metadata │    │  ┌─────┐     │  ×1000 epochs       │    └──────────┘      |
|  │ (JSON)   │───►│  │Tok.C│──►──┘                     │         │            |
|  └──────────┘    │  └─────┘                           │         ▼            |
|       │          │                                     │    ┌──────────┐      |
|       │          │  ■ Identity destroyed at each step   │    │QUESTIONS │      |
|       │          └─────────────────────────────────────┘    │──────────│      |
|       │                                                     │• % from A?│     |
|       │          ┌────────────────────────────┐             │• Style or │     |
|       │          │  ANALOG HOLE BYPASS         │             │  copy?    │     |
|       └─────────►│  ──────────────────         │             │• License  │     |
|                  │  Re-record → new digital    │             │  needed?  │     |
|                  │  identity. Provenance chain  │             └──────────┘     |
|                  │  broken at physical layer.   │                              |
|                  └────────────────────────────┘                               |
+-------------------------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "THE ORACLE PROBLEM -- TECHNICAL PIPELINE" with coral accent square |
| Subtitle | `label_editorial` | "Where Attribution Gets Destroyed" in editorial caps |
| Input column | `etl_extract` | Three input types: Audio (FLAC), MIDI (stems), Metadata (JSON) |
| Tokenization stage | `processing_stage` | Tokens A/B/C -- where structured data becomes undifferentiated vectors |
| Gradient descent stage | `processing_stage` | Loss minimization (nabla L) -- where individual contributions merge into gradients |
| Weight averaging stage | `processing_stage` | Final averaged weights (W-bar) -- where all identity is destroyed |
| Black box container | `problem_statement` | Dashed border around training stages, labeled "Black Box" |
| Output column | `problem_statement` | Generated output with unanswerable questions |
| Unanswerable questions list | `problem_statement` | "% from A?", "Style or copy?", "License needed?" |
| Analog hole callout | `problem_statement` | Side callout explaining physical-to-digital re-encoding bypass |
| Flow arrows (input to training) | `data_flow` | Solid arrows showing data entering the black box |
| Flow arrows (internal stages) | `data_flow` | Arrows between tokenization, gradient descent, weight averaging |
| Flow arrow (training to output) | `data_flow` | Solid arrow showing irreversible transformation |
| Epoch counter | `data_mono` | "x1000 epochs" annotation showing iteration scale |
| Destruction annotation | `callout_box` | "Identity destroyed at each step" inside the black box |

## Anti-Hallucination Rules

1. The training pipeline stages are: Tokenization -> Gradient Descent -> Weight Averaging. Do NOT add or reorder stages.
2. The analog hole is a FUNDAMENTAL bypass -- do NOT suggest it can be closed with technology.
3. Do NOT include specific model names (GPT, Stable Diffusion, etc.) -- this is architecture-agnostic.
4. The questions listed are UNANSWERABLE from model weights alone -- do NOT imply they have solutions.
5. "Black Box" refers to the opacity of training, not to a specific architecture or vendor.
6. Input types are audio (FLAC), MIDI (stems), metadata (JSON) -- do NOT add text/lyrics as a separate input.
7. Background must be warm cream (#f6f3e6), not white or gray.
8. Do NOT show watermarking or fingerprinting as solutions within this figure -- those belong to fig-theory-03.

## Alt Text

Technical pipeline diagram: creator audio, MIDI, and music metadata enter a training black box where tokenization, gradient descent, and weight averaging destroy attribution identity at each stage -- showing the oracle problem's analog hole bypass that breaks digital provenance chains, a core challenge for transparent confidence in music attribution systems.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Technical pipeline diagram: creator audio, MIDI, and music metadata enter a training black box where tokenization, gradient descent, and weight averaging destroy attribution identity at each stage -- showing the oracle problem's analog hole bypass that breaks digital provenance chains, a core challenge for transparent confidence in music attribution systems.](docs/figures/repo-figures/assets/fig-theory-02-oracle-problem-technical.jpg)

*Figure 2. The Oracle Problem at the technical level: attribution information is irreversibly destroyed through tokenization, gradient descent, and weight averaging during model training, while the analog hole further undermines provenance by allowing physical re-encoding to break digital identity chains.*

### From this figure plan (relative)

![Technical pipeline diagram: creator audio, MIDI, and music metadata enter a training black box where tokenization, gradient descent, and weight averaging destroy attribution identity at each stage -- showing the oracle problem's analog hole bypass that breaks digital provenance chains, a core challenge for transparent confidence in music attribution systems.](../assets/fig-theory-02-oracle-problem-technical.jpg)
