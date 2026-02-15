# fig-repo-16: Music AI Attribution Landscape Overview

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-repo-16 |
| **Title** | Music AI Attribution Landscape: Who's Building What |
| **Audience** | All (newcomers, domain experts, investors) |
| **Complexity** | L2 (landscape mapping) |
| **Location** | README.md landscape section, docs/planning/music-tech-landscape/ |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

A single overview infographic mapping the music AI attribution ecosystem across four tiers: Attribution Infrastructure (Sureel, Musical AI, Vermillio, ProRata, this scaffold), AI Music Generation (Suno, Udio, Soundverse, Boomy), Licensing & Certification (Fairly Trained, LANDR, STIM, SoundExchange), and Open-Source Tools (librosa, Splink, chromaprint). The scaffold is positioned distinctly as the only open-source, research-backed entry with formal uncertainty quantification. Updated for v3.0.0: PRD node annotations show which ecosystem decision nodes map to each company, and connection lines differentiated by integration archetype (Simple MCP, Platform Integration, CMO Federation) show the three engagement depth levels.

The key message is: "The music AI attribution space has ~$500M+ in funding across proprietary players — this scaffold is the only open-source, auditable alternative with calibrated confidence scoring. 28 ecosystem PRD nodes map to these companies across three integration archetypes."

## Visual Concept (ASCII Layout)

```
+-----------------------------------------------------------------------+
|  MUSIC AI ATTRIBUTION LANDSCAPE                                        |
|  ■ Who's Building What (Feb 2026)                                      |
+-----------------------------------------------------------------------+
|                                                                        |
|  I. ATTRIBUTION INFRASTRUCTURE        II. AI MUSIC GENERATION          |
|  ─────────────────────────────        ──────────────────────           |
|                                                                        |
|  ┌─────────┐ ┌─────────┐             ┌──────────┐ ┌──────────┐       |
|  │ Sureel  │ │ Musical │             │  Suno    │ │  Udio    │       |
|  │ 86-90%  │ │ AI $6M  │             │ $2.45B   │ │ settled  │       |
|  │ patents │ │ cert'd  │             │ settling │ │ pivoting │       |
|  └─────────┘ └─────────┘             └──────────┘ └──────────┘       |
|  ┌─────────┐ ┌─────────┐             ┌──────────┐ ┌──────────┐       |
|  │Vermillio│ │ProRata  │             │Soundverse│ │  Boomy   │       |
|  │ $16M    │ │ $40M    │             │ DNA mdls │ │  cert'd  │       |
|  │ Sony    │ │ UMG     │             │ ethical  │ │ 14.5M+   │       |
|  └─────────┘ └─────────┘             └──────────┘ └──────────┘       |
|                                                                        |
|  III. LICENSING & CERTIFICATION       IV. OPEN-SOURCE TOOLS            |
|  ──────────────────────────────      ─────────────────────             |
|                                                                        |
|  ┌──────────┐ ┌──────────┐           ┌──────────┐ ┌──────────┐       |
|  │ Fairly   │ │  STIM    │           │ librosa  │ │ Splink   │       |
|  │ Trained  │ │ 1st col  │           │  8.2k★   │ │  4k+★    │       |
|  │ 19 cert  │ │ licence  │           │ ISC      │ │  MIT     │       |
|  └──────────┘ └──────────┘           └──────────┘ └──────────┘       |
|  ┌──────────┐ ┌──────────┐           ┌──────────┐ ┌──────────┐       |
|  │SoundExch │ │  LANDR   │           │chromprint│ │  CLAP    │       |
|  │ Registry │ │ Fair AI  │           │  1.2k★   │ │  1k★     │       |
|  │ ISRC opt │ │ pro-rata │           │ LGPL     │ │ Apache   │       |
|  └──────────┘ └──────────┘           └──────────┘ └──────────┘       |
|                                                                        |
|  ┌───────────────────────────────────────────────────────────────────┐ |
|  │  THIS SCAFFOLD  ■  Open-source · A0-A3 assurance · Conformal     │ |
|  │  prediction · MCP consent · Research-backed · MIT License         │ |
|  └───────────────────────────────────────────────────────────────────┘ |
+-----------------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title | `heading_display` | "MUSIC AI ATTRIBUTION LANDSCAPE" Instrument Serif ALL-CAPS |
| Subtitle | `label_editorial` | "Who's Building What (Feb 2026)" |
| Tier I heading | `section_numeral` | "I. ATTRIBUTION INFRASTRUCTURE" with coral accent line |
| Tier II heading | `section_numeral` | "II. AI MUSIC GENERATION" |
| Tier III heading | `section_numeral` | "III. LICENSING & CERTIFICATION" |
| Tier IV heading | `section_numeral` | "IV. OPEN-SOURCE TOOLS" |
| Company cards | `entity_card` | Each company as a compact card with name, key metric, status |
| PRD node annotations | `label_editorial` | Small PRD node IDs next to each company (e.g., "sureel_ai_partnership" next to Sureel) |
| Integration archetype lines | `data_flow` | Thin = Simple MCP, Medium = Platform Integration, Thick = CMO Federation |
| Scaffold highlight bar | `primary_outcome` | Full-width bar at bottom with coral accent, differentiators listed |
| Funding annotations | `data_mono` | Dollar amounts in IBM Plex Mono |
| Star counts | `data_mono` | GitHub star counts for open-source tools |
| Certification badges | `badge_label` | "Fairly Trained" badges on certified entities |
| Ecosystem callout | `callout_bar` | "28 ecosystem PRD nodes map to these companies" |

## Anti-Hallucination Rules

1. Funding amounts are: Suno $375M+ ($2.45B valuation), Vermillio $16M, Musical AI $6M, ProRata $40M, Sureel undisclosed.
2. Sureel claims 86-90% accuracy — these are CLAIMED, not independently verified.
3. Fairly Trained has exactly 19 certified entities (12 company + 2 product + 5 model certifications).
4. Suno is SETTLING lawsuits, not settled. Udio HAS settled.
5. STIM's is the world's FIRST collective AI music licence (Sep 2025).
6. Boomy claims 14.5M+ songs created — this is their claim, not independently verified.
7. The scaffold is the ONLY open-source entry in the attribution tier.
8. Do NOT include companies not mentioned in the landscape report.
9. Background must be warm cream (#f6f3e6).
10. PRD node annotations: Sureel → sureel_ai_partnership, Musical AI → musical_ai_partnership, STIM → stim_cmo_pilot, SoundExchange → soundexchange_registry, Fairly Trained → fairly_trained_certification, Suno/Udio → suno_udio_licensing. These are L3_components nodes in _network.yaml v3.0.0.
11. Three integration archetype line styles: thin = Simple MCP (read-only API adapters), medium = Platform Integration (bidirectional data exchange), thick = CMO Federation (institutional infrastructure). See docs/planning/expand-probabilistic-prd-to-discussion.md Section 4.
12. 28 total ecosystem PRD nodes, but only 6 map directly to named companies. The remaining 22 are category/infrastructure nodes.

## Alt Text

Music AI attribution landscape overview: four-quadrant infographic with PRD v3.0.0 node annotations mapping 6 company nodes to attribution infrastructure (Sureel, Musical AI), AI music generation (Suno, Udio), and licensing bodies (STIM, SoundExchange, Fairly Trained), with integration archetype lines differentiating Simple MCP, Platform Integration, and CMO Federation engagement depths.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Music AI attribution landscape with PRD v3.0.0 node annotations: four-quadrant infographic mapping companies to 6 ecosystem decision nodes across three integration archetypes.](docs/figures/repo-figures/assets/fig-repo-16-landscape-overview.jpg)

*Figure 16. The music AI attribution ecosystem as of February 2026, with v3.0.0 PRD node annotations showing how 28 ecosystem decision nodes map to companies across three integration archetypes (Simple MCP, Platform Integration, CMO Federation).*

### From this figure plan (relative)

![Music AI attribution landscape with PRD v3.0.0 node annotations](../assets/fig-repo-16-landscape-overview.jpg)
