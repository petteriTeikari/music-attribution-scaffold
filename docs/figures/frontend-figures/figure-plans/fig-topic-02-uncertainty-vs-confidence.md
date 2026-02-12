# fig-topic-02: Uncertainty Taxonomy for Music Attribution

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-topic-02 |
| **Title** | Uncertainty Taxonomy — Four Types in Music Attribution |
| **Audience** | General + Technical |
| **Complexity** | L2 (overview) |
| **Location** | Landing page, Topic Card II (Confidence & Uncertainty group) |
| **Priority** | P2 (Medium) |
| **Dimensions** | 1200 x 900px (4:3 aspect ratio) |

## Purpose & Key Message

Four-quadrant infographic showing the four types of uncertainty from Beigi et al. (arXiv:2410.20199, ICLR 2025), each with a concrete music attribution example. Replaces the old aleatoric/epistemic split with the modern 4-type taxonomy: data uncertainty, model uncertainty, operational uncertainty, and output uncertainty. Communicates: "uncertainty comes from four distinct sources — understanding which type you're dealing with determines whether you can reduce it and how."

Key distinction: **Confidence ≠ Uncertainty**. Confidence is a model output (0–1 score). Uncertainty is the model's knowledge state. A system can be confidently wrong (high confidence, high uncertainty).

## Visual Concept (ASCII Layout)

```
┌──────────────────────────────────────────────────────────┐
│                                                          │
│        CONFIDENCE ≠ UNCERTAINTY                          │
│  confidence is output; uncertainty is knowledge state    │
│                                                          │
│  ┌──── OPERATIONAL ─────┐  ┌──── OUTPUT ──────────┐    │
│  │  (how text/scores     │  │  (reliability of     │    │
│  │   are generated)      │  │   final knowledge)   │    │
│  │                       │  │                       │    │
│  │  ① DATA UNCERTAINTY   │  │  ③ INCOMPLETE        │    │
│  │  "Producer" means     │  │  KNOWLEDGE            │    │
│  │  different things     │  │  1978 dub album:      │    │
│  │  across genres        │  │  vocalist known,      │    │
│  │  Irreducible noise    │  │  engineer unknown     │    │
│  │  in training data     │  │  → A0: no data        │    │
│  │                       │  │                       │    │
│  │  ② MODEL UNCERTAINTY  │  │  ④ CONTRADICTING     │    │
│  │  Splink trained on    │  │  SOURCES              │    │
│  │  English pop: fails   │  │  MusicBrainz: sole    │    │
│  │  on Japanese names    │  │  writer. Discogs:     │    │
│  │  Reducible with       │  │  co-writer listed     │    │
│  │  more data            │  │  → conflict severity  │    │
│  │                       │  │                       │    │
│  └───────────────────────┘  └───────────────────────┘    │
│                                                          │
│  OPERATIONAL                   OUTPUT                    │
│  ① Data: irreducible          ③ Incomplete: missing     │
│     noise in sources              evidence → A0          │
│  ② Model: reducible           ④ Contradicting: sources  │
│     with more training            disagree → conflict    │
│                                                          │
│  ■ REDUCIBLE  ■ IRREDUCIBLE  ■ CONFIDENCE (separate)  │
│                                                          │
│  (Beigi et al. 2025, arXiv:2410.20199)                  │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|-------------|-------------|
| Top banner | `typography_display` | "CONFIDENCE ≠ UNCERTAINTY" in display type |
| Two main columns | `region_secondary` | Operational (left) vs Output (right) |
| Data uncertainty box | `data_warning` | Orange background — irreducible |
| Model uncertainty box | `data_primary` | Teal background — reducible |
| Incomplete knowledge box | `data_subtle` | Grey background — missing evidence |
| Contradicting sources box | `data_error` | Coral background — source conflict |
| Music examples | `label_editorial` | Concrete scenarios in each quadrant |
| Number labels | `data_accent` | Circled ①②③④ for each type |
| Legend | `label_editorial` | Reducible vs irreducible distinction |
| Divider | `line_accent` | Coral vertical accent between columns |
| Citation | `label_subtle` | Beigi et al. reference |

## Anti-Hallucination Rules

1. **Font names are internal** — do NOT render them as visible labels.
2. **Semantic tags are internal** — do NOT render them.
3. **Pixel sizes and rendering instructions are internal** — do NOT render.
4. Only the following text should appear: "CONFIDENCE ≠ UNCERTAINTY", "OPERATIONAL", "OUTPUT", "DATA UNCERTAINTY", "MODEL UNCERTAINTY", "INCOMPLETE KNOWLEDGE", "CONTRADICTING SOURCES", "REDUCIBLE", "IRREDUCIBLE", music examples text, circled numbers ①②③④, citation text.

## Alt Text

Four-quadrant infographic distinguishing four types of uncertainty in music attribution. Left column (Operational): data uncertainty shown in orange (irreducible — e.g., "producer" means different things across genres) and model uncertainty in teal (reducible — e.g., name matching trained on English pop fails on Japanese names). Right column (Output): incomplete knowledge in grey (missing evidence — a 1978 dub album with unknown engineer, mapped to assurance level A0) and contradicting sources in coral (MusicBrainz says sole writer, Discogs lists co-writer). A banner at the top states "Confidence ≠ Uncertainty" — confidence is a model output, uncertainty is the knowledge state.
