# fig-topic-08: Drift Detection & Monitoring

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-topic-08 |
| **Title** | Drift Detection — When the Music World Changes Under Your Model |
| **Audience** | General + Technical |
| **Complexity** | L3 (detailed) |
| **Location** | Landing page, Topic Card VIII (Governance & Security group) |
| **Priority** | P2 (Medium) |
| **Dimensions** | 1200 x 900px (4:3 aspect ratio) |

## Purpose & Key Message

Music is a non-stationary domain — genres evolve, rights transfer, AI-generated content floods catalogs, platforms change schemas. A model trained on 1990s electronic music encounters 2024 AI-generated tracks with fundamentally different statistical properties. This figure shows the four drift types from Lu et al. (2019) mapped to concrete music scenarios, with a layered monitoring architecture that triggers tiered responses. Communicates: "the ground shifts under your model constantly — drift detection catches degradation before artists lose royalties, and the AI-generated content inflection point is the most significant drift event in music attribution history."

Key concepts from Lu et al. (IEEE TKDE, 2019):
- **Sudden drift**: Spotify removes audio features API overnight
- **Gradual drift**: Hyperpop emerges 2017–2021, blurring genre boundaries
- **Incremental drift**: Loudness normalization shifts LUFS distributions over decades
- **Recurring drift**: Vinyl revival cycles acoustic properties back toward analog characteristics

## Visual Concept (ASCII Layout)

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  FOUR DRIFT TYPES IN MUSIC ATTRIBUTION                      │
│  ─────────────────────────────────────                      │
│                                                              │
│  SUDDEN              GRADUAL            INCREMENTAL         │
│  ╱╲                  ╱ ╲                     ╱              │
│ ╱  ╲                ╱   ╲  ╱╲              ╱               │
│╱    ╲──            ╱  ╲ ╱  ╲──          ──╱                │
│                                                              │
│  Spotify drops     Hyperpop emerges    Loudness war         │
│  audio features    2017→2021           LUFS shift           │
│  API (Nov 2024)                        over 20 years        │
│                                                              │
│  RECURRING                                                   │
│  ╱╲  ╱╲  ╱╲                                                │
│ ╱  ╲╱  ╲╱  ╲                                               │
│  Vinyl revival     Q4 holiday release                       │
│  cycles back       floods every year                        │
│                                                              │
│  WHAT SHIFTS — AND WHY IT BREAKS                            │
│  ───────────────────────────────                            │
│                                                              │
│  P(X) INPUT DRIFT        │ AI-generated tracks flood        │
│  Features change,        │ catalogs: new acoustic           │
│  labels stay same        │ signatures, sparse metadata      │
│                          │                                   │
│  P(Y|X) CONCEPT DRIFT   │ Rights transfer: Hipgnosis       │
│  Correct label changes   │ buys catalog → 60K tracks        │
│  for same input          │ change publisher overnight        │
│                          │                                   │
│  P(Y) PRIOR SHIFT        │ A0 proportion rises as           │
│  Class balance changes   │ AI content lacks identifiers     │
│                                                              │
│  THE AI INFLECTION POINT (biggest drift event ever)         │
│  ──────────────────────────────────────────────             │
│                                                              │
│  Model trained on:          Now encountering:               │
│  ● Human-produced music     ● AI-generated tracks           │
│  ● Analog synth jitter      ● Perfectly quantized timing    │
│  ● Rich metadata (ISRC,     ● Sparse metadata (no ISNI,    │
│    ISWC, session credits)     fabricated artist names)       │
│  ● Entity resolution works  ● New "artists" don't resolve  │
│                                                              │
│  Confidence distribution becomes bimodal:                    │
│  genuine: ████████░░ 0.75-0.90                              │
│  AI-gen:  ░░████░░░░ 0.40-0.60                              │
│                                                              │
│  MONITORING METRICS                                         │
│  ─────────────────                                          │
│                                                              │
│  Confidence mean shift    K-S test weekly                   │
│  ER match rate drop       ADWIN daily                       │
│  New-artist cold-start    Control chart                     │
│  A3→A0 proportion drift   Chi-squared monthly               │
│  Human override rate      Ground truth signal               │
│                                                              │
│  ALERT TIERS                                                │
│  ───────────                                                │
│  ■ WARNING:  confidence mean drops > 0.05                   │
│  ■ ELEVATED: match rate drops > 10%                         │
│  ■ CRITICAL: K-S p < 0.001 → halt auto-attribution         │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|-------------|-------------|
| Four drift type curves | `data_primary` | Teal line charts: sudden (step), gradual (S-curve), incremental (ramp), recurring (wave) |
| Music examples per type | `label_editorial` | Concrete scenario under each curve |
| Three P-shift rows | `data_warning` | Orange panel: P(X), P(Y\|X), P(Y) with music-specific examples |
| AI inflection comparison | `region_secondary` | Two-column: "trained on" vs "now encountering" |
| Bimodal confidence bars | `data_gradient` | Split distribution showing genuine vs AI-generated score clusters |
| Monitoring metrics table | `data_primary` | Teal rows: metric name + statistical test + cadence |
| Alert tiers | `data_accent` | Three coral/orange/amber levels with thresholds and actions |
| Music scenario callouts | `label_editorial` | Concrete examples: Spotify API, Hipgnosis acquisition, hyperpop |

## Anti-Hallucination Rules

1. **Font names are internal** — do NOT render them as visible labels.
2. **Semantic tags are internal** — do NOT render them.
3. **Pixel sizes and rendering instructions are internal** — do NOT render.
4. Only the following text should appear: "FOUR DRIFT TYPES", "SUDDEN", "GRADUAL", "INCREMENTAL", "RECURRING", music scenario descriptions, "P(X) INPUT DRIFT", "P(Y|X) CONCEPT DRIFT", "P(Y) PRIOR SHIFT", "THE AI INFLECTION POINT", comparison columns, confidence distribution bars, "MONITORING METRICS", metric names and tests, "ALERT TIERS", "WARNING", "ELEVATED", "CRITICAL", threshold values.

## Alt Text

Drift detection infographic showing four drift types mapped to music attribution. Sudden drift: Spotify removes audio features API. Gradual: hyperpop emerges 2017–2021. Incremental: loudness war shifts LUFS over decades. Recurring: vinyl revival cycles acoustic properties. Below, three probability shifts are explained with music examples: P(X) input drift from AI-generated content, P(Y|X) concept drift from catalog acquisitions, P(Y) prior shift as A0 proportion rises. A highlighted section identifies the AI-generated content inflection point as the biggest drift event, showing how confidence distributions become bimodal (genuine tracks at 0.75–0.90, AI-generated at 0.40–0.60). Monitoring metrics include confidence mean shift (K-S test weekly), entity resolution match rate (ADWIN daily), new-artist cold-start rate, and A3-to-A0 proportion drift. Three alert tiers: warning (confidence drops >0.05), elevated (match rate drops >10%), critical (K-S p<0.001, halt auto-attribution).
