# fig-landscape-14: On-Chain vs Off-Chain Provenance Trade-offs

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-landscape-14 |
| **Title** | On-Chain vs Off-Chain Provenance Trade-offs |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/planning/music-tech-landscape/, docs/planning/music-tech-figure-coverage-plan.md |
| **Priority** | P2 (Medium) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | B (Multi-Panel) |

## Purpose

Compares on-chain and off-chain provenance architectures by showing their trade-offs, then introduces the pharmaceutical serialization precedent (EU FMD) as a cross-domain hybrid solution that music attribution can learn from. Answers: "Should music provenance live on a blockchain, in a centralized registry, or both -- and has anyone solved this before?"

## Key Message

Blockchain provides immutability but adds cost; C2PA/DDEX provide speed but require trust -- the drug serialization industry (EU FMD) solved this exact dilemma with a hybrid approach.

## Visual Concept

Three panels arranged left-center-right. Left panel shows on-chain approaches (Mubert Protocol/Polkadot, Audius) with their properties: immutable, transparent, slow, costly. Right panel shows off-chain approaches (C2PA, DDEX) with their properties: fast, standards-based, trust-dependent. Center panel is the key insight -- the EU FMD pharmaceutical serialization hybrid architecture as a cross-domain precedent. The center panel is visually emphasized with an accent border to signal "look here for the answer." Trade-off axes run along the bottom.

```
+-----------------------------------------------------------------------+
|  ON-CHAIN VS OFF-CHAIN                                                 |
|  ■ Provenance Trade-offs                                               |
+-----------------------------------------------------------------------+
|                                                                        |
|  ON-CHAIN                HYBRID PRECEDENT           OFF-CHAIN          |
|  ════════                ════════════════           ═════════          |
|                                                                        |
|  ┌──────────────┐    ┌─────────────────────┐    ┌──────────────┐      |
|  │              │    │                     │    │              │      |
|  │ Mubert       │    │ EU FMD              │    │ C2PA         │      |
|  │ Protocol     │    │ PHARMACEUTICAL      │    │ ─────────    │      |
|  │ (Polkadot)   │    │ SERIALIZATION       │    │ Cryptographic│      |
|  │              │    │ ───────────────     │    │ manifests    │      |
|  │ Audius       │    │                     │    │ Fast verify  │      |
|  │ (Solana→own) │    │ Unique identifiers  │    │ Trust-based  │      |
|  │              │    │ per unit on-chain   │    │              │      |
|  │ Properties:  │    │ Batch metadata      │    │ DDEX         │      |
|  │ ■ Immutable  │    │ off-chain           │    │ ─────────    │      |
|  │ ■ Transparent│    │ Verification at     │    │ XML exchange │      |
|  │ ■ Slow       │    │ point of dispensing │    │ B2B standard │      |
|  │ ■ Costly     │    │                     │    │ No immutable │      |
|  │ ■ Permanent  │    │ ■ Music can learn:  │    │ guarantee    │      |
|  │              │    │   ISRC on-chain     │    │              │      |
|  │              │    │   Metadata off-chain│    │ Properties:  │      |
|  │              │    │   Verify at play    │    │ ■ Fast       │      |
|  │              │    │                     │    │ ■ Standards  │      |
|  │              │    │                     │    │ ■ Revocable  │      |
|  └──────────────┘    └─────────────────────┘    └──────────────┘      |
|                                                                        |
|  ◄── Immutability / Cost ──────────────── Speed / Trust ──────────►   |
|                                                                        |
|  ■ Cross-domain insight: pharma solved track-and-trace with hybrid     |
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
    bounds: [0, 0, 1920, 100]
    content: "ON-CHAIN VS OFF-CHAIN"
    role: title

  - id: subtitle_zone
    bounds: [0, 100, 1920, 40]
    content: "Provenance Trade-offs"
    role: subtitle

  - id: left_panel
    bounds: [60, 180, 500, 680]
    role: content_area
    label: "ON-CHAIN"

  - id: center_panel
    bounds: [620, 180, 680, 680]
    role: content_area
    label: "HYBRID PRECEDENT"

  - id: right_panel
    bounds: [1360, 180, 500, 680]
    role: content_area
    label: "OFF-CHAIN"

  - id: tradeoff_axis
    bounds: [60, 900, 1800, 60]
    role: data_flow
    label: "Immutability/Cost vs Speed/Trust"

  - id: footer_callout
    bounds: [60, 980, 1800, 60]
    role: callout_bar
    label: "Cross-domain insight: pharma solved track-and-trace with hybrid"

anchors:
  - id: mubert
    position: [80, 220]
    size: [460, 180]
    role: solution_component
    label: "Mubert Protocol"

  - id: audius
    position: [80, 420]
    size: [460, 140]
    role: solution_component
    label: "Audius"

  - id: onchain_properties
    position: [80, 580]
    size: [460, 240]
    role: processing_stage
    label: "On-chain properties"

  - id: eu_fmd
    position: [640, 220]
    size: [640, 600]
    role: solution_component
    label: "EU FMD Pharmaceutical Serialization"

  - id: music_lesson
    position: [660, 620]
    size: [600, 180]
    role: callout_bar
    label: "Music can learn from pharma"

  - id: c2pa
    position: [1380, 220]
    size: [460, 200]
    role: solution_component
    label: "C2PA"

  - id: ddex
    position: [1380, 440]
    size: [460, 180]
    role: solution_component
    label: "DDEX"

  - id: offchain_properties
    position: [1380, 640]
    size: [460, 180]
    role: processing_stage
    label: "Off-chain properties"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "ON-CHAIN VS OFF-CHAIN" in editorial caps with accent square |
| Subtitle | `label_editorial` | "Provenance Trade-offs" |
| On-chain panel | `solution_component` | Left panel: Mubert Protocol (Polkadot), Audius -- immutable, transparent, slow, costly |
| Hybrid precedent panel | `solution_component` | Center panel: EU FMD pharmaceutical serialization -- hybrid on-chain/off-chain |
| Off-chain panel | `solution_component` | Right panel: C2PA cryptographic manifests, DDEX XML exchange -- fast, trust-based |
| Mubert Protocol | `solution_component` | Blockchain-based music creation on Polkadot with on-chain provenance |
| Audius | `solution_component` | Decentralized streaming protocol, migrated from Solana to own chain |
| EU FMD | `solution_component` | Falsified Medicines Directive: unique serial per unit on-chain, batch metadata off-chain |
| C2PA | `solution_component` | Content provenance with cryptographic manifests, fast verification, trust-dependent |
| DDEX | `solution_component` | XML-based B2B metadata exchange, industry standard, no immutability guarantee |
| Music lesson | `callout_bar` | How music can adapt pharma's approach: ISRC on-chain, metadata off-chain, verify at play |
| Trade-off axis | `data_flow` | Horizontal axis: Immutability/Cost on left, Speed/Trust on right |
| Footer callout | `callout_bar` | Cross-domain insight from pharmaceutical industry |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| On-chain | Immutability | property | Permanent, transparent record |
| On-chain | Cost | property | Gas fees, slow confirmation |
| Off-chain | Speed | property | Fast verification |
| Off-chain | Trust | property | Requires trusted intermediary |
| EU FMD | Both | bridge | Hybrid approach solves both |
| Pharma precedent | Music lesson | arrow | Cross-domain transfer |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "PHARMA PRECEDENT" | EU's Falsified Medicines Directive achieved end-to-end track-and-trace with unique serial numbers on-chain and batch/logistics metadata off-chain -- verification happens at the point of dispensing | center panel, emphasized |
| "MUSIC ANALOG" | Map pharma to music: ISRC = serial number (on-chain), rich metadata = batch data (off-chain), playback = dispensing (verification point) | center panel bottom |
| "AUDIUS LESSON" | Audius migrated from Solana to its own chain -- illustrating that pure on-chain has governance and cost challenges even for well-funded projects | left panel bottom |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "On-Chain Provenance"
- Label 2: "Off-Chain Provenance"
- Label 3: "Hybrid Precedent"
- Label 4: "Mubert Protocol (Polkadot)"
- Label 5: "Audius"
- Label 6: "C2PA Manifests"
- Label 7: "DDEX XML Exchange"
- Label 8: "EU FMD Serialization"
- Label 9: "Immutable"
- Label 10: "Transparent"
- Label 11: "Slow / Costly"
- Label 12: "Fast / Standards-Based"
- Label 13: "Trust-Dependent"
- Label 14: "ISRC On-Chain"
- Label 15: "Metadata Off-Chain"

### Caption (for embedding in documentation)

On-chain provenance (Mubert Protocol, Audius) provides immutability but at cost and speed penalties. Off-chain approaches (C2PA, DDEX) offer speed and standardization but require trust. The EU Falsified Medicines Directive solved an identical track-and-trace dilemma with a hybrid architecture -- unique identifiers on-chain, batch metadata off-chain, verification at point of dispensing -- providing a direct cross-domain precedent for music attribution.

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

8. Mubert Protocol uses Polkadot -- do NOT say Ethereum or Solana.
9. Audius migrated from Solana to its own chain -- do NOT describe it as still on Solana.
10. EU FMD is the Falsified Medicines Directive -- do NOT invent a different directive name.
11. The pharma-to-music analogy is a PROPOSED cross-domain transfer -- do NOT claim it has been implemented.
12. C2PA is NOT blockchain-based -- it uses cryptographic signing, not distributed ledger.
13. Do NOT claim blockchain is "the answer" or "dead" -- present trade-offs neutrally.
14. DDEX is a consortium standard, not a company -- do NOT describe it as a product.
15. Do NOT add NFTs or token economics -- this figure is about provenance architecture, not financialization.

## Alt Text

On-chain vs off-chain provenance trade-offs with EU pharmaceutical serialization as hybrid cross-domain precedent

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "landscape-14",
    "title": "On-Chain vs Off-Chain Provenance Trade-offs",
    "audience": "L3",
    "layout_template": "B"
  },
  "content_architecture": {
    "primary_message": "Pharma solved the immutability-vs-speed dilemma with hybrid on-chain/off-chain -- music can learn from this precedent.",
    "layout_flow": "left-center-right",
    "key_structures": [
      {
        "name": "On-Chain Panel",
        "role": "solution_component",
        "is_highlighted": false,
        "labels": ["Mubert Protocol", "Audius", "Immutable", "Costly"]
      },
      {
        "name": "EU FMD Hybrid",
        "role": "solution_component",
        "is_highlighted": true,
        "labels": ["EU FMD", "Serial on-chain", "Metadata off-chain"]
      },
      {
        "name": "Off-Chain Panel",
        "role": "solution_component",
        "is_highlighted": false,
        "labels": ["C2PA", "DDEX", "Fast", "Trust-dependent"]
      }
    ],
    "relationships": [
      {
        "from": "On-chain",
        "to": "Immutability",
        "type": "property",
        "label": "permanent record"
      },
      {
        "from": "Off-chain",
        "to": "Speed",
        "type": "property",
        "label": "fast verification"
      },
      {
        "from": "EU FMD",
        "to": "Both",
        "type": "bridge",
        "label": "hybrid solves both"
      }
    ],
    "callout_boxes": [
      {
        "heading": "PHARMA PRECEDENT",
        "body_text": "EU FMD: unique serial on-chain, batch metadata off-chain, verify at dispensing",
        "position": "center"
      },
      {
        "heading": "MUSIC ANALOG",
        "body_text": "ISRC on-chain, rich metadata off-chain, verify at playback",
        "position": "center-bottom"
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
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25
- [ ] Embedded in documentation
