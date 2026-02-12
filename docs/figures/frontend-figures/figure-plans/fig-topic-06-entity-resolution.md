# fig-topic-06: Entity Resolution

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-topic-06 |
| **Title** | Entity Resolution — From Fragmented Names to Unified Identity |
| **Audience** | General + Technical |
| **Complexity** | L3 (detailed) |
| **Location** | Landing page, Topic Card VI (Pipeline & Data group) |
| **Priority** | P2 (Medium) |
| **Dimensions** | 1200 x 900px (4:3 aspect ratio) |

## Purpose & Key Message

Entity resolution is why $2.5 billion in music royalties sit unclaimed. The same artist appears under five different names across five databases — and each name lives in a different system with different identifiers. This figure shows how probabilistic record linkage (Fellegi-Sunter 1969, operationalized via Splink) resolves fragments into unified entities, and how confidence in the match maps directly to the A0–A3 assurance framework. Communicates: "the same human appears as five different database entries — probabilistic matching unifies them, and the quality of that match determines how much we trust the attribution."

Key concepts from Fellegi & Sunter (1969) and Splink:
- **m-probability**: P(field agrees | true match) — how reliable is this field?
- **u-probability**: P(field agrees | non-match) — how often does it agree by coincidence?
- **Match weight**: log₂(m/u) — ISNI match = +13.3 bits, name match = +6.5 bits
- **Three decision regions**: LINK (confident match), POSSIBLE LINK (human review), NON-LINK
- The three regions map directly to: auto-approve, review queue, reject

## Visual Concept (ASCII Layout)

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  THE FRAGMENTATION PROBLEM                                   │
│  ─────────────────────────                                  │
│                                                              │
│  One human, five database entries:                           │
│                                                              │
│  MusicBrainz: "Imogen Heap"        MBID: 328d146c...       │
│  MusicBrainz: "Frou Frou"          MBID: (separate entity) │
│  Discogs:     "Imogen J. Heap"     Discogs ID: 59709       │
│  Streaming:   "iMi"                Spotify URI: ...         │
│  File Meta:   "I Megaphone"        (no identifier)          │
│                                                              │
│  ISNI: 0000 0000 7840 4022 (the answer — but who has it?)  │
│                                                              │
│  FELLEGI-SUNTER PROBABILISTIC MATCHING                      │
│  ─────────────────────────────────────                      │
│                                                              │
│  For each pair of records, compute match weight:             │
│                                                              │
│  Field        m      u      Weight (agree)                  │
│  ─────────────────────────────────────────                  │
│  ISNI         0.98   0.0001  +13.3 bits  ████████████████  │
│  Name (exact) 0.90   0.01    +6.5 bits   ████████          │
│  Birth year   0.95   0.012   +6.3 bits   ███████           │
│  Genre overlap 0.70  0.15    +2.2 bits   ███               │
│                                                              │
│  Composite weight → match probability                       │
│                                                              │
│  THREE DECISION REGIONS                                     │
│  ──────────────────────                                     │
│                                                              │
│  ◄── NON-LINK ──┼── POSSIBLE LINK ──┼── LINK ──►          │
│     (reject)     │   (human review)   │ (auto-approve)      │
│     < 0.50       │    0.50 – 0.85     │  > 0.85             │
│                                                              │
│  "Heap" + "Frou Frou":  name=0, genre=+2.2, ISNI=+13.3    │
│  → composite: 0.92 → LINK (same ISNI resolves it)          │
│                                                              │
│  "I Megaphone" + "Heap": name=+1.1 (partial), no ISNI     │
│  → composite: 0.58 → POSSIBLE LINK → human review          │
│                                                              │
│  WHY IT MATTERS                                             │
│  ──────────────                                             │
│                                                              │
│  $2.5B global royalty black box                             │
│  $424M MLC unmatched royalties                              │
│  ← caused by fragmented identities                         │
│                                                              │
│  RESOLVED ENTITY                                            │
│  ───────────────                                            │
│  ● HEAP, IMOGEN JENNIFER JANE                              │
│    ISNI: 0000 0000 7840 4022                               │
│    Aliases: Imogen Heap, Frou Frou, iMi, I Megaphone       │
│    Assurance: A3 (ISNI-verified)                            │
│                                                              │
│  ■ LINK  ■ POSSIBLE LINK  ■ NON-LINK                      │
│  ████ MATCH WEIGHT (bits of evidence)                      │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|-------------|-------------|
| Fragmentation examples | `data_warning` | Five orange entries showing the same person across databases with different names/IDs |
| ISNI callout | `data_accent` | Coral highlight — the unifying identifier that resolves ambiguity |
| Match weight table | `data_primary` | Teal horizontal bars showing evidential weight per field |
| m/u probabilities | `typography_mono` | Monospace numeric table with reliability vs. coincidence rates |
| Three decision regions | `region_interactive` | Horizontal scale: reject / review / approve with thresholds |
| Worked examples | `data_accent` | Two concrete pair comparisons showing how weights sum to decisions |
| Royalty black box | `data_warning` | Orange "$2.5B" and "$424M" — financial consequence of poor ER |
| Resolved entity | `data_primary` | Teal unified entity card with ISNI, aliases, assurance level |
| Assurance level badge | `data_primary` | A3 badge — ISNI verification enables highest assurance |
| Legend | `label_editorial` | ALL-CAPS labels with colored markers |

## Anti-Hallucination Rules

1. **Font names are internal** — do NOT render them as visible labels.
2. **Semantic tags are internal** — do NOT render them.
3. **Pixel sizes and rendering instructions are internal** — do NOT render.
4. Only the following text should appear: "THE FRAGMENTATION PROBLEM", database names and entries, ISNI number, "FELLEGI-SUNTER PROBABILISTIC MATCHING", field names with m/u/weight values, "THREE DECISION REGIONS", "NON-LINK", "POSSIBLE LINK", "LINK", threshold values, worked examples, "$2.5B", "$424M", "RESOLVED ENTITY", alias list, "A3".

## Alt Text

Entity resolution infographic showing how one person (Imogen Heap) appears as five different database entries across MusicBrainz, Discogs, streaming, and file metadata. A Fellegi-Sunter match weight table shows evidential strength per field: ISNI match provides +13.3 bits (strongest), exact name +6.5 bits, birth year +6.3 bits, genre overlap +2.2 bits. Three decision regions map composite weights to actions: below 0.50 reject, 0.50–0.85 route to human review, above 0.85 auto-approve. Two worked examples show "Heap + Frou Frou" resolving via shared ISNI (0.92 → LINK) and "I Megaphone + Heap" falling into review (0.58 → POSSIBLE LINK). Financial stakes: $2.5 billion in unclaimed royalties globally caused by fragmented identities. The resolved entity card shows the unified identity with ISNI, all aliases, and A3 assurance level.
