# fig-feature-03: MCP Patchbay

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-feature-03 |
| **Title** | MCP Patchbay — Permission Grid as Geometric Art |
| **Audience** | General + Technical |
| **Complexity** | L2 (overview) |
| **Location** | Landing page, Feature III section |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3 aspect ratio) |

## Purpose & Key Message

Abstract permission grid/matrix as Bauhaus-inspired geometric art. Each cell represents a permission (allow/deny/ask) as colored squares. Communicates: "machine-readable consent with visual clarity."

## Visual Concept (ASCII Layout)

```
┌──────────────────────────────────────┐
│                                      │
│  ■ ■ □ ■ □    STREAM                │
│  ■ □ ■ □ ■    AI TRAINING           │
│  □ ■ □ ■ □    VOICE CLONING         │
│  ■ ■ ■ □ □    STYLE LEARNING        │
│  □ □ ■ ■ ■    DERIVATIVE            │
│                                      │
│  ■ Allow  □ Deny  ◧ Ask             │
│                                      │
│  ── PERMISSION MATRIX ──             │
│                                      │
└──────────────────────────────────────┘
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|-------------|-------------|
| Allow cells | `status_allow` | Green squares |
| Deny cells | `status_deny` | Red squares (coral) |
| Ask cells | `status_ask` | Amber squares |
| Row labels | `label_editorial` | ALL-CAPS permission type names |
| Grid lines | `line_subtle` | Very thin rules between rows |

## Anti-Hallucination Rules

These are INTERNAL instructions for the image generator. They must NEVER appear as visible text in the output:

1. **Font names are internal** — "Plus Jakarta Sans", "IBM Plex Mono", "Instrument Serif" are CSS font references. Do NOT render them as visible labels in the figure.
2. **Semantic tags are internal** — `status_allow`, `label_editorial`, etc. are for the figure plan system. Do NOT render them.
3. The legend should show colored squares with the words "Allow", "Deny", "Ask" — NOT font names.
4. Only the following text should appear in the figure: "MCP PATCHBAY", "STREAM", "AI TRAINING", "VOICE CLONING", "STYLE LEARNING", "DERIVATIVE", "Allow", "Deny", "Ask", "PERMISSION MATRIX".

## Alt Text

Bauhaus-inspired grid of colored squares representing an AI permission matrix. Green, red, and amber squares indicate allow, deny, and ask states for different music usage permissions including streaming, AI training, voice cloning, and style learning.
