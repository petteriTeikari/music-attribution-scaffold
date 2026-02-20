# fig-voice-15: Speech LLM Architecture Taxonomy

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-voice-15 |
| **Title** | Speech LLM Architecture Taxonomy |
| **Audience** | L4 (Researcher) |
| **Location** | docs/tutorials/voice-agent-implementation.md |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | C (Flowchart) |

## Purpose

Classify the major Speech LLM architecture families from the ACL 2025 survey, with representative models and quality/latency indicators per family. Answers: "What are the three main architecture families for speech-native LLMs, and which models belong to each?"

## Key Message

Speech LLMs divide into three architecture families -- Encoder-Decoder (best quality, higher latency), Decoder-Only (fastest inference, emerging quality), and Hierarchical Codebook (rich audio, complex training) -- each with distinct tradeoffs. The ACL 2025 survey (arXiv:2410.03751) provides the definitive taxonomy.

## Visual Concept

Flowchart layout (Template C) with a root node "SPEECH LLM ARCHITECTURES" branching into three family columns. Each family box contains: architecture name, representative models, latency indicator, quality indicator, and key tradeoff. Connecting arrows from root to families. Bottom callout references the ACL 2025 survey paper.

```
+-------------------------------------------------------------------+
|  SPEECH LLM ARCHITECTURE TAXONOMY                          [sq]   |
|                                                                    |
|                    SPEECH LLM                                      |
|                   ARCHITECTURES                                    |
|                   /     |     \                                    |
|                  /      |      \                                   |
|  ┌──────────────┐ ┌──────────────┐ ┌──────────────────┐          |
|  │  ENCODER-    │ │  DECODER-    │ │  HIERARCHICAL    │          |
|  │  DECODER     │ │  ONLY        │ │  CODEBOOK        │          |
|  │              │ │              │ │                  │          |
|  │ Quality: ●●● │ │ Quality: ●●  │ │ Quality: ●●●    │          |
|  │ Latency: ●●  │ │ Latency: ●●● │ │ Latency: ●      │          |
|  │              │ │              │ │                  │          |
|  │ Models:      │ │ Models:      │ │ Models:          │          |
|  │ • Ultravox   │ │ • Moshi      │ │ • VALL-E         │          |
|  │ • SALMONN    │ │ • SpeechGPT  │ │ • SoundStorm     │          |
|  │ • Qwen-Audio │ │ • dGSLM     │ │ • AudioPaLM      │          |
|  │              │ │              │ │                  │          |
|  │ Tradeoff:    │ │ Tradeoff:    │ │ Tradeoff:        │          |
|  │ Best quality  │ │ Fastest      │ │ Rich audio       │          |
|  │ but higher   │ │ inference    │ │ but complex      │          |
|  │ latency      │ │ emerging     │ │ training         │          |
|  │              │ │ quality      │ │                  │          |
|  └──────────────┘ └──────────────┘ └──────────────────┘          |
|                                                                    |
|  "ACL 2025 SPEECHLM SURVEY (arXiv:2410.03751)"          [line]   |
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
    content: "SPEECH LLM ARCHITECTURE TAXONOMY"
    role: title

  - id: root_zone
    bounds: [760, 140, 400, 100]
    content: "SPEECH LLM ARCHITECTURES"
    role: decision_point

  - id: families_zone
    bounds: [40, 300, 1840, 580]
    role: content_area

  - id: callout_zone
    bounds: [40, 920, 1840, 120]
    content: "ACL 2025 SPEECHLM SURVEY"
    role: callout_box

anchors:
  - id: root_node
    position: [760, 160]
    size: [400, 80]
    role: decision_point
    label: "SPEECH LLM ARCHITECTURES"

  - id: family_encoder_decoder
    position: [80, 320]
    size: [560, 540]
    role: processing_stage
    label: "ENCODER-DECODER"

  - id: family_decoder_only
    position: [680, 320]
    size: [560, 540]
    role: processing_stage
    label: "DECODER-ONLY"

  - id: family_hierarchical
    position: [1280, 320]
    size: [560, 540]
    role: processing_stage
    label: "HIERARCHICAL CODEBOOK"

  - id: flow_root_to_enc_dec
    from: root_node
    to: family_encoder_decoder
    type: arrow
    label: "family 1"

  - id: flow_root_to_dec_only
    from: root_node
    to: family_decoder_only
    type: arrow
    label: "family 2"

  - id: flow_root_to_hierarchical
    from: root_node
    to: family_hierarchical
    type: arrow
    label: "family 3"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Root: Speech LLM Architectures | `decision_point` | Taxonomy root -- three architecture families for speech-native LLMs |
| Encoder-Decoder Family | `processing_stage` | Audio encoder + text decoder, best quality but higher latency. Models: Ultravox, SALMONN, Qwen-Audio |
| Decoder-Only Family | `processing_stage` | Single autoregressive decoder for both audio and text, fastest inference but emerging quality. Models: Moshi, SpeechGPT, dGSLM |
| Hierarchical Codebook Family | `processing_stage` | Multi-level discrete audio tokens, rich audio representation but complex training. Models: VALL-E, SoundStorm, AudioPaLM |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Root | Encoder-Decoder Family | arrow | "audio encoder + text decoder" |
| Root | Decoder-Only Family | arrow | "single autoregressive decoder" |
| Root | Hierarchical Codebook Family | arrow | "multi-level discrete tokens" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "ACL 2025 SPEECHLM SURVEY (arXiv:2410.03751)" | Definitive taxonomy of Speech LLM architectures from the ACL 2025 survey paper. The encoder-decoder family dominates current production deployments while decoder-only models show the fastest inference gains. | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "SPEECH LLM ARCHITECTURES"
- Label 2: "ENCODER-DECODER"
- Label 3: "DECODER-ONLY"
- Label 4: "HIERARCHICAL CODEBOOK"
- Label 5: "Ultravox"
- Label 6: "SALMONN"
- Label 7: "Qwen-Audio"
- Label 8: "Moshi"
- Label 9: "SpeechGPT"
- Label 10: "dGSLM"
- Label 11: "VALL-E"
- Label 12: "SoundStorm"
- Label 13: "AudioPaLM"
- Label 14: "Quality: high"
- Label 15: "Quality: emerging"
- Label 16: "Quality: rich audio"
- Label 17: "Latency: moderate"
- Label 18: "Latency: lowest"
- Label 19: "Latency: highest"
- Label 20: "Best quality, higher lat."
- Label 21: "Fastest inference"
- Label 22: "Rich audio, complex train."

### Caption (for embedding in documentation)

Three-family taxonomy of Speech LLM architectures from the ACL 2025 survey: Encoder-Decoder (Ultravox, SALMONN), Decoder-Only (Moshi, SpeechGPT), and Hierarchical Codebook (VALL-E, SoundStorm) with quality and latency indicators.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `processing_stage`, `decision_point`, etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear unless the figure is L3/L4 audience. This figure IS L4, so model names are appropriate.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption. The editorial display title is allowed.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. The ACL 2025 survey paper is arXiv:2410.03751 -- this is the authoritative source for the taxonomy. Do not cite a different paper ID.
10. Ultravox is an encoder-decoder model by Fixie.ai -- it uses a multimodal encoder feeding into a text LLM. Do not classify it as decoder-only.
11. SALMONN is from Tsinghua/ByteDance -- it is an encoder-decoder architecture. Do not misattribute.
12. Moshi is from Kyutai -- it is a decoder-only streaming speech model with 200ms latency. Do not classify as encoder-decoder.
13. SpeechGPT and dGSLM are decoder-only architectures that process speech tokens autoregressively.
14. VALL-E is from Microsoft -- it uses hierarchical neural audio codecs (EnCodec). SoundStorm is from Google.
15. The quality/latency indicators are relative within the three families -- not absolute scores. Use dot indicators or similar relative markers, not exact numbers.
16. Do NOT add models not listed in the specification -- the examples are curated, not exhaustive.
17. AudioPaLM is from Google -- it uses hierarchical audio token representations.

## Alt Text

Taxonomy diagram of three Speech LLM architecture families from the ACL 2025 survey: Encoder-Decoder (Ultravox, SALMONN, Qwen-Audio), Decoder-Only (Moshi, SpeechGPT, dGSLM), and Hierarchical Codebook (VALL-E, SoundStorm, AudioPaLM), with quality and latency tradeoff indicators.

## Image Embed

![Taxonomy diagram of three Speech LLM architecture families from the ACL 2025 survey: Encoder-Decoder (Ultravox, SALMONN, Qwen-Audio), Decoder-Only (Moshi, SpeechGPT, dGSLM), and Hierarchical Codebook (VALL-E, SoundStorm, AudioPaLM), with quality and latency tradeoff indicators.](docs/figures/repo-figures/assets/fig-voice-15-speech-llm-taxonomy.jpg)

*Three-family taxonomy of Speech LLM architectures from the ACL 2025 survey: Encoder-Decoder (Ultravox, SALMONN), Decoder-Only (Moshi, SpeechGPT), and Hierarchical Codebook (VALL-E, SoundStorm) with quality and latency indicators.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "voice-15",
    "title": "Speech LLM Architecture Taxonomy",
    "audience": "L4",
    "layout_template": "C"
  },
  "content_architecture": {
    "primary_message": "Speech LLMs divide into three architecture families -- Encoder-Decoder, Decoder-Only, Hierarchical Codebook -- each with distinct quality/latency tradeoffs.",
    "layout_flow": "top-to-bottom",
    "key_structures": [
      {
        "name": "Root: Speech LLM Architectures",
        "role": "decision_point",
        "is_highlighted": false,
        "labels": ["SPEECH LLM ARCHITECTURES"]
      },
      {
        "name": "Encoder-Decoder Family",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["ENCODER-DECODER", "Ultravox", "SALMONN", "Qwen-Audio", "Best quality"]
      },
      {
        "name": "Decoder-Only Family",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["DECODER-ONLY", "Moshi", "SpeechGPT", "dGSLM", "Fastest inference"]
      },
      {
        "name": "Hierarchical Codebook Family",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["HIERARCHICAL CODEBOOK", "VALL-E", "SoundStorm", "AudioPaLM", "Rich audio"]
      }
    ],
    "relationships": [
      {
        "from": "Root",
        "to": "Encoder-Decoder Family",
        "type": "arrow",
        "label": "audio encoder + text decoder"
      },
      {
        "from": "Root",
        "to": "Decoder-Only Family",
        "type": "arrow",
        "label": "single autoregressive decoder"
      },
      {
        "from": "Root",
        "to": "Hierarchical Codebook Family",
        "type": "arrow",
        "label": "multi-level discrete tokens"
      }
    ],
    "callout_boxes": [
      {
        "heading": "ACL 2025 SPEECHLM SURVEY (arXiv:2410.03751)",
        "body_text": "Definitive taxonomy of Speech LLM architectures. Encoder-decoder dominates production; decoder-only shows fastest inference gains.",
        "position": "bottom-center"
      }
    ]
  }
}
```

## Quality Checklist

- [ ] Primary message clear in one sentence
- [ ] Semantic tags used (no colors, hex codes, or font names in content spec)
- [ ] ASCII layout sketched
- [ ] Spatial anchors defined in YAML
- [ ] Labels under 30 characters
- [ ] Anti-hallucination rules listed
- [ ] Alt text provided (125 chars max)
- [ ] JSON export block included
- [ ] Audience level correct (L4)
- [ ] Layout template identified (C)

## Status

- [ ] Draft created
- [ ] Content reviewed
- [x] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
