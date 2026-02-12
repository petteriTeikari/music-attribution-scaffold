# fig-topic-11: Voice Cloning & Creator Protection

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-topic-11 |
| **Title** | Voice Cloning — Identity Risk & Consent Gate |
| **Audience** | General |
| **Complexity** | L1 (conceptual) |
| **Location** | Landing page, Topic Card XI (Governance & Security group) |
| **Priority** | P2 (Medium) |
| **Dimensions** | 1200 x 900px (4:3 aspect ratio) |

## Purpose & Key Message

Artist silhouette with original voice waveform being cloned, blocked by an MCP consent gate. Communicates: "AI can clone a voice from seconds of audio — consent infrastructure is the defense."

## Visual Concept (ASCII Layout)

```
┌──────────────────────────────────────┐
│                                      │
│  ♪ ORIGINAL         ♪ CLONE         │
│                                      │
│  ╭───╮  ∿∿∿∿∿     ╭───╮  ∿∿∿∿∿    │
│  │   │  voice  ──> │   │  voice     │
│  │   │  wave       │   │  wave      │
│  ╰───╯             ╰───╯            │
│  teal              orange            │
│                                      │
│       ⚠ 3–15 SECONDS                │
│         SUFFICIENT                   │
│                                      │
│  ──── MCP CONSENT GATE ────         │
│  [✓ ALLOW]  [✗ DENY]               │
│                                      │
└──────────────────────────────────────┘
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|-------------|-------------|
| Original silhouette | `data_primary` | Teal abstract figure with waveform |
| Clone silhouette | `data_warning` | Orange abstract figure with replicated waveform |
| Transfer arrow | `line_flow` | Navy arrow from original to clone |
| Warning text | `typography_warning` | Red "3-15 SECONDS SUFFICIENT" |
| Consent gate | `line_accent` | Coral horizontal bar with allow/deny buttons |
| Allow button | `status_allow` | Teal |
| Deny button | `status_deny` | Coral |

## Anti-Hallucination Rules

1. **Font names are internal** — do NOT render them as visible labels.
2. **Semantic tags are internal** — do NOT render them.
3. Only the following text should appear: "ORIGINAL", "CLONE", "3-15 SECONDS SUFFICIENT", "MCP CONSENT GATE", "ALLOW", "DENY".

## Alt Text

Two abstract silhouettes side by side: a teal original artist with voice waveform on the left, and an orange clone with replicated waveform on the right, connected by an arrow. A red warning notes that 3 to 15 seconds of audio is sufficient for cloning. An MCP consent gate with allow and deny options blocks unauthorized cloning.
