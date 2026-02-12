# fig-topic-11: Voice Cloning & Creator Protection

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-topic-11 |
| **Title** | Voice Cloning — From 3-Second Theft to Consent-First Licensing |
| **Audience** | General + Technical |
| **Complexity** | L3 (detailed) |
| **Location** | Landing page, Topic Card XI (Governance & Security group) |
| **Priority** | P2 (Medium) |
| **Dimensions** | 1200 x 900px (4:3 aspect ratio) |

## Purpose & Key Message

Voice cloning has collapsed from hours of audio to 3 seconds. This is identity appropriation — the AI becomes the artist. This figure shows the threat taxonomy (from Azzuni & El Saddik 2025), the collapsing audio requirements, three real cases spanning the consent spectrum (Holly+ = A3 consent-first, Grimes/Elf.Tech = A2 permissive licensing, Drake/Weeknd deepfake = A0 adversarial), why watermarking alone fails (Nemecek et al. 2025), and what defenses actually work. Communicates: "a 3-second clip can clone any voice — the question is not whether cloning is possible but whether consent infrastructure exists to make it legitimate."

Key concepts:
- **Azzuni & El Saddik (2025)**: Four cloning categories — full adaptation, few-shot, zero-shot, voice conversion
- **Collapsing requirements**: VALL-E (3 seconds), ElevenLabs (10s), XTTS (6s) — democratized overnight
- **Nemecek et al. (2025)**: Watermarking without standards = symbolic compliance, not governance
- **Three case studies**: Holly+ (DAO-governed consent), Grimes/Elf.Tech (50/50 royalty split), Drake/Weeknd (viral deepfake, 15M streams before takedown)
- **ELVIS Act**: First US voice cloning law (Tennessee, 2024, unanimous 93-0 / 30-0)

## Visual Concept (ASCII Layout)

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  THE COLLAPSING BARRIER                                     │
│  ──────────────────────                                     │
│                                                              │
│  Audio needed to clone a voice:                             │
│                                                              │
│  2020  Traditional     10+ min  ████████████████████████    │
│  2023  VALL-E           3 sec   ███                         │
│  2024  XTTS             6 sec   ██████                      │
│  2024  OpenVoice        ~5 sec  █████                       │
│  2025  ElevenLabs      10 sec   ██████████                  │
│                                                              │
│  Zero-shot: no fine-tuning. One clip at inference time.     │
│                                                              │
│  FOUR CLONING CATEGORIES (Azzuni & El Saddik 2025)         │
│  ─────────────────────────────────────────────              │
│                                                              │
│  ① FULL ADAPTATION    ② FEW-SHOT       ③ ZERO-SHOT        │
│  Fine-tune on hours   3-5 min of audio  Single utterance    │
│  of target audio      Model adapts      No fine-tuning      │
│  Highest quality       from samples     VALL-E, OpenVoice   │
│                                                              │
│  ④ VOICE CONVERSION                                        │
│  Transform source → target voice characteristics            │
│  Real-time possible (SVC, RVC)                              │
│                                                              │
│  THREE CASES: THE CONSENT SPECTRUM                          │
│  ─────────────────────────────────                          │
│                                                              │
│  ● Holly Herndon's Holly+ (2021)          ASSURANCE: A3    │
│  │ Artist trains model on own voice                         │
│  │ DAO governs submissions                                  │
│  │ Open-source, non-commercial default                      │
│  │ → CONSENT-FIRST: artist controls                        │
│  │                                                          │
│  ● Grimes' Elf.Tech (2023)                ASSURANCE: A2    │
│  │ 50/50 royalty split on masters                          │
│  │ $10/year for streaming distribution                      │
│  │ Label releases require approval                          │
│  │ → PERMISSIVE LICENSING: artist profits                  │
│  │                                                          │
│  ● Drake/Weeknd "Heart on My Sleeve"      ASSURANCE: A0    │
│    Ghostwriter977, April 2023                               │
│    15 million TikTok streams before takedown                │
│    No consent, no attribution, no revenue                   │
│    → ADVERSARIAL: no protection existed                     │
│                                                              │
│  WHY WATERMARKING ALONE FAILS                               │
│  ────────────────────────────                               │
│  (Nemecek, Jiang & Ayday 2025)                             │
│                                                              │
│  SynthID detection fails on simple edits                    │
│  (scores drop below 0.52 threshold after paraphrase)        │
│  15 companies made voluntary commitments →                  │
│  all implementations proprietary, no interop                │
│  "Symbolic compliance, not governance"                       │
│                                                              │
│  Three layers needed:                                       │
│  ① Technical standards (robustness benchmarks)              │
│  ② Audit infrastructure (independent third-party)           │
│  ③ Policy enforcement (legal mandates + certification)      │
│                                                              │
│  LEGAL DEFENSE: ELVIS Act (Tennessee 2024)                  │
│  Unanimous: 93-0 House, 30-0 Senate                        │
│  First US law protecting against AI voice cloning           │
│                                                              │
│  ■ CONSENT-FIRST  ■ PERMISSIVE  ■ ADVERSARIAL             │
│  ████ AUDIO REQUIRED (seconds)                              │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|-------------|-------------|
| Collapsing barrier bars | `data_gradient` | Horizontal bars showing audio duration per system/year, shrinking dramatically |
| Year labels | `typography_mono` | Monospace years with system names |
| Four cloning categories | `region_secondary` | Four panels with category name, description, example systems |
| Three case studies | `data_accent` | Coral vertical timeline: Holly+ (A3, teal), Elf.Tech (A2, amber), Heart on My Sleeve (A0, orange) |
| Assurance badges | `data_primary` | A3, A2, A0 badges next to each case |
| Consent spectrum labels | `label_editorial` | "CONSENT-FIRST", "PERMISSIVE LICENSING", "ADVERSARIAL" |
| Watermarking failure | `data_warning` | Orange panel with SynthID failure stats, Nemecek critique |
| Three defense layers | `data_primary` | Teal numbered list: standards, audit, policy |
| ELVIS Act callout | `data_accent` | Coral highlight with vote counts |
| Legend | `label_editorial` | Consent spectrum colors + audio bar scale |

## Anti-Hallucination Rules

1. **Font names are internal** — do NOT render them as visible labels.
2. **Semantic tags are internal** — do NOT render them.
3. **Pixel sizes and rendering instructions are internal** — do NOT render.
4. Only the following text should appear: "THE COLLAPSING BARRIER", year/system/duration entries, "FOUR CLONING CATEGORIES", category names and descriptions, "THREE CASES: THE CONSENT SPECTRUM", case study details with assurance levels, "WHY WATERMARKING ALONE FAILS", SynthID failure note, Nemecek quote, three defense layers, "ELVIS ACT", vote counts, legend labels.

## Alt Text

Voice cloning infographic showing the collapsing audio barrier: from 10+ minutes in 2020 to 3 seconds with VALL-E in 2023, with horizontal bars dramatically shrinking. Four cloning categories from Azzuni & El Saddik (2025): full adaptation (hours), few-shot (minutes), zero-shot (single utterance, no fine-tuning), and voice conversion (real-time). Three case studies spanning the consent spectrum: Holly Herndon's Holly+ (2021, A3 assurance, consent-first with DAO governance), Grimes' Elf.Tech (2023, A2 assurance, 50/50 royalty split), and the Drake/Weeknd "Heart on My Sleeve" deepfake (2023, A0 assurance, 15 million streams before takedown, no consent). A watermarking failure section cites Nemecek et al. (2025): SynthID detection fails on simple edits, 15 companies made voluntary commitments but all implementations are proprietary — "symbolic compliance, not governance." Three defense layers needed: technical standards, independent audit infrastructure, and policy enforcement. The ELVIS Act (Tennessee 2024, unanimous 93-0/30-0) is highlighted as the first US law protecting against AI voice cloning.
