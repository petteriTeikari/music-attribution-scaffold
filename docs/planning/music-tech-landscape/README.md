# Music AI Attribution — Industry Landscape Report

> **Generated**: 2026-02-10
> **Purpose**: Comprehensive competitive landscape, buy-vs-build analysis, and strategic positioning for the music-attribution-scaffold
> **Audience**: Domain experts, engineers, and potential stakeholders evaluating the space
> **Cross-references**: [probabilistic-prd-tool-landscape.md](probabilistic-prd-tool-landscape.md), [../prd/decisions/](../prd/decisions/)

---

## How to Read This Document

This report maps the music AI attribution ecosystem across five dimensions:

1. **Who's building what** — Companies, products, funding, and technical approaches
2. **What's in the literature** — Academic papers on training data attribution (TDA)
3. **What's open-source** — Libraries for the "build" side of buy-vs-build
4. **What to buy vs build** — Strategic analysis for this scaffold
5. **How to decide** — MVA definition, risk framework, and domain expert feedback mechanisms

Each company profile includes: approach, funding, traction, and relevance to this scaffold.

---

## Table of Contents

### This Document (Overview & Summary)

1. [Executive Summary](#executive-summary)
2. [Competitive Landscape](#competitive-landscape) (summary; details in sub-files)
3. [Competitive Comparison Matrix](#competitive-comparison-matrix)
4. [Market Dynamics & Funding](#market-dynamics--funding)
5. [Academic Research Landscape](#academic-research-landscape) (summary; details in sub-file)
6. [Open-Source Library Catalog](#open-source-library-catalog) (summary; details in sub-file)
7. [Buy vs Build Analysis](#buy-vs-build-analysis) (summary; details in sub-file)
8. [Minimum Viable Architecture (MVA)](#minimum-viable-architecture-mva) (summary; details in sub-file)
9. [Risk & Probability Framework](#risk--probability-framework) (summary; details in sub-file)
10. [Human-Machine Decision Making](#human-machine-decision-making) (summary; details in sub-file)
11. [Domain Expert Feedback Mechanisms](#domain-expert-feedback-mechanisms) (summary; details in sub-file)
12. [Strategic Implications for This Scaffold](#strategic-implications-for-this-scaffold) (summary; details in sub-file)

### Detailed Sub-Files

| File | Focus | Contents |
|------|-------|----------|
| [01-attribution-companies.md](01-attribution-companies.md) | **Tier 1: Attribution Infrastructure** | Musical AI (full profile, SWOT, estimated architecture), Sureel AI (patents, partnerships, integration modes), Vermillio (TraceID, Sony backing), ProRata.ai, Pex |
| [02-generation-platforms.md](02-generation-platforms.md) | **Tier 2: AI Music Generation** | Suno ($2.45B, legal status, 2026 changes), Udio (pivot details), Soundverse (6-stage whitepaper, DNA Models, pilot results), Boomy, Stability/Google/Meta/AIVA/Mubert/Soundful |
| [03-licensing-ecosystem.md](03-licensing-ecosystem.md) | **Tier 3-4: Licensing & Registries** | Fairly Trained (19 certified entities), LANDR Fair Trade AI, Lemonaide (cohort-based), Source Audio, Rightsify/DPA, SoundExchange AI Registry, STIM collective licence, Kits AI, Voicemod, Voice-Swap |
| [04-academic-research.md](04-academic-research.md) | **Academic Research** | 10 core papers with full summaries, supplemental resources, two paradigms analysis (post-hoc TDA vs attribution-by-design), A0-A3 mapping |
| [05-open-source-catalog.md](05-open-source-catalog.md) | **Open-Source Libraries** | Python MIR (librosa, essentia, madmom), fingerprinting (dejavu, chromaprint, audfprint), metadata (musicbrainzngs, beets, discogs), AI/ML (CLAP, AudioLDM2, muzic), Rust, JS/TS, standards (ISRC/ISWC/ISNI/DDEX), MVA library selection matrix |
| [06-web3-blockchain.md](06-web3-blockchain.md) | **Web3 & Blockchain** | Mubert Protocol (Polkadot rollup, architecture), Audius, Royal, Arpeggi, blockchain attribution patterns, blockchain vs traditional comparison |
| [07-buy-vs-build.md](07-buy-vs-build.md) | **Buy vs Build + MVA** | Decision matrix, component-by-component analysis, Musical AI reverse-engineered architecture, MVA definition, cost/timeline estimates, post-MVA expansion path |
| [08-risk-framework.md](08-risk-framework.md) | **Risk & Probability** | Marginal return curves, risk matrix (8 risks with probabilities), adoption flywheel analysis, engineering allocation, scenario analysis, decision gates |
| [09-feedback-mechanisms.md](09-feedback-mechanisms.md) | **Expert Feedback** | FeedbackCards (full YAML schema), VAS design, HOPs visualization, calibration interface, active learning loop, priority queue logic, multi-reviewer convergence, probabilistic PRD integration |
| [10-strategic-implications.md](10-strategic-implications.md) | **Strategy & Positioning** | 6 differentiators, positioning map, competitive strategy, 6 recommendations, market timing analysis, reviewer feedback log, comprehensive sources index |

---

## Executive Summary

The music AI attribution space is undergoing rapid consolidation and legitimization. Key dynamics as of February 2026:

**Market size**: Generative AI in music projected to grow from $558M (2024) to $7.4B (2035) at 26.5% CAGR.

**Funding concentration**: Suno ($375M+ total, $2.45B valuation), Vermillio ($16M, Sony-backed), Musical AI ($6M total), with >$250M in equity across the sector in 2025 alone.

**The attribution trilemma**: Companies face three competing approaches:
1. **Training-time attribution** (Sureel, Musical AI) — precise but requires model integration
2. **Inference-time attribution** (Morreale et al., 2025) — by design, more scalable
3. **Licensing without attribution** (LANDR, Source Audio) — simpler, predictable, but less fair

**The uncomfortable truth** (per Water & Music): "Perfect attribution for music AI doesn't currently exist. All the attribution approaches studied provide approximations at best." The companies most likely to succeed aren't those with the most technically sophisticated systems, but those who can "solve the immense political challenge of fostering cross-industry trust."

**What this means for our scaffold**: The open-source scaffold has unique value as a *neutral, transparent, research-backed* alternative to proprietary black-box attribution systems. Our A0-A3 assurance levels, conformal prediction confidence, and MCP permission patchbay are differentiators no commercial player currently offers.

---

## Competitive Landscape

### Tier 1: Attribution Infrastructure

These companies build the core technology for tracing AI outputs back to training data.

#### Musical AI (formerly Somms.ai)

| Attribute | Details |
|-----------|---------|
| **HQ** | Ottawa/Halifax, Canada |
| **Founded** | ~2023 (rebranded 2024) |
| **Funding** | $1.5M seed + $4.5M Series A (Jan 2026, led by Heavybit) |
| **Team** | ~5 employees |
| **Founders** | Sean Power (CEO), Matthew Adell (COO, ex-Beatport CEO) |
| **Advisors** | Vickie Nauman, Alastair Croll |
| **Certification** | Fairly Trained certified |

**Technical approach**: Musical AI traces which training data influences specific outputs, producing "royalty sheets" with percentage attribution. Their technology determines *what percentage of a generated output came from which source*. They require integration during initial model training — post-hoc analysis is not supported.

**Business model**: Two-sided marketplace connecting rights holders (catalogs from Pro Sound Effects, SourceAudio, Symphonic Distribution) with AI companies needing licensed training data. Attribution + licensing bundled as turnkey infrastructure.

**Key partnerships**:
- **Beatoven.ai** (Dec 2024): First "fully licensed, rightsholder-compensating" AI music platform. 30% of revenue to training data contributors.
- **SoundBreak AI** (ex-SESHY, cofounded by Better Than Ezra's Kevin Griffin): Licensed model training
- **Symphonic Distribution**: Catalog access
- **Kanjian**: Chinese market distribution

**Estimated architecture** (reverse-engineered from public statements):
```
Rights Holder Catalog → Musical AI Ingestion Pipeline
                         ↓
                    Embedding/Fingerprint Index
                         ↓
              AI Company Model Training (integrated)
                         ↓
                   Influence Tracking Layer
                         ↓
                    Royalty Sheet Generation
                         ↓
              Payment Distribution to Rights Holders
```

**Strengths**: Turnkey "attribution simple" positioning; strong industry relationships via Adell's Beatport network; expansion plans beyond music to "other creative sectors."

**Weaknesses**: Only 5 employees; requires training-time integration (no post-hoc); no published patents; no publicly quantified accuracy claims.

**Sources**: [Music Business Worldwide](https://www.musicbusinessworldwide.com/musical-ai-bags-4-5m-in-funding-round-to-scale-ai-attribution-tech/), [Digital Music News](https://www.digitalmusicnews.com/2026/01/13/musical-ai-funding-january-2026/), [Record of the Day](https://www.recordoftheday.com/on-the-move/news-press/musical-ai-tames-the-chaos-and-ushers-in-a-sustainable-generative-ai-future)

---

#### Sureel AI

| Attribute | Details |
|-----------|---------|
| **HQ** | Palo Alto, CA |
| **Founded** | 2022 |
| **Funding** | Undisclosed (CDL Montreal 2023/24 AI cohort) |
| **Team** | ~10-15 |
| **Founders** | Dr. Tamay Aykut (CEO, PhD AI/Robotics, TU Munich) |
| **Leadership** | Benji Rogers (Co-President, PledgeMusic founder), Aileen Crowley (Co-President, ex-UMG) |
| **Patents** | 1 published + 4 pending |

**Technical approach**: The most technically ambitious player. Sureel creates **"attribution graphs"** mapping relationships between songs and claims **86-90% accuracy at the works level**. Key innovation: **compositional vs. recording rights separation** — distinguishing melody/lyrics (publishing rights) from production/performance (master rights).

**Two integration modes**:
1. **Decoupled** (lighter): Requires dataset + model encoder; only needs text prompt and output for inference-time attribution
2. **Integrated** (full): Requires all training data, entire training history including weights, gradients, and loss values

**Patent portfolio covers**:
- Training-time gradient tracking for attribution vectors
- Output-to-creator correlation via embeddings
- Compensation determination from attribution vectors

**Product capabilities**: Audio attribution, lyric attribution (multi-language), AI audio detection, stem-wise attribution, temporal attribution (influence changes across track segments), AIBI (AI Business Intelligence) for prompt-to-output mapping.

**Key partnerships**:
- **STIM** (Sep 2025): Swedish music rights society's world-first collective AI music licence. Sureel is the preferred attribution provider.
- **BeatStars** (Apr 2025): Entire marketplace catalog registered, monthly "Do Not Train" notices to AI companies
- **OpenPlay** (Dec 2024): AI detection/monetization for API marketplace
- **Triple 8 Management** (Apr 2025): First management company to offer AI IP protection
- **~10M registered assets** across partnerships

**Business model**: Attribution-as-a-Service (AaaS). B2B API-driven. "Attribution Share" replaces traditional market share — revenue allocated from each transaction based on influence of rights holder assets.

**Strengths**: Strongest patent portfolio; compositional/recording separation is a genuine innovation; STIM partnership gives access to CMO infrastructure globally; multi-modal ambitions (audio, image, text, video); academic pedigree (Stanford EE talk, CDL).

**Weaknesses**: No publicly disclosed funding amount; no peer-reviewed papers; accuracy claims not independently verified; no major label deals.

**Sources**: [Water & Music](https://www.waterandmusic.com/music-ai-attribution/), [Digital Music News - STIM](https://www.digitalmusicnews.com/2025/09/26/stim-taps-sureel-ai-attribution-tracking/), [A2IM Spotlight](https://a2im.org/ams-sureel-ai/), [Justia Patents](https://patents.justia.com/assignee/sureel-inc), [MusicWorks Substack](https://musicworks.substack.com/p/bringing-responsible-and-explainable)

---

#### Vermillio

| Attribute | Details |
|-----------|---------|
| **HQ** | Chicago, IL |
| **Founded** | ~2022 |
| **Funding** | $16M Series A (Mar 2025, led by Sony Music + DNS Capital) |
| **Pricing** | $4,000/month + transaction fees |
| **Clients** | Sony Pictures, Sony Music, WME, individual talent |

**Technical approach**: **TraceID** system monitors online content for IP usage, including name/image/likeness. Automatic takedown requests and payment management for licensed content. More focused on content protection and licensing enforcement than training-time attribution.

**Key distinction**: This is Sony Music's *first-ever AI investment*. Vermillio was named to the TIME100 Most Influential Companies List in 2025.

**Notable project**: Sony Pictures Spider-Verse AI character generation; The Orb/David Gilmour fan remix project.

**Strengths**: Deepest pockets (Sony backing); proven enterprise clients; TIME100 recognition.

**Weaknesses**: Protection/enforcement focus rather than attribution; high price point ($48K/year); less technically transparent than competitors.

**Sources**: [Axios](https://www.axios.com/2025/03/03/vermillio-ai-rights-licensing-sony-music), [Billboard](https://www.billboard.com/pro/sony-music-ai-investment-vermillio-funding-round/), [BusinessWire](https://www.businesswire.com/news/home/20250228026074/en/)

---

#### ProRata.ai

| Attribute | Details |
|-----------|---------|
| **Funding** | $40M Series B |
| **Key deal** | Universal Music Group partnership |

**Technical approach**: Broader AI attribution beyond music — determines how much specific content influenced AI outputs across text, audio, and visual media. UMG deal suggests significant music industry traction.

**Limited public technical details available.**

---

### Tier 2: AI Music Generation Platforms

These companies generate music and are increasingly forced to adopt attribution practices.

#### Suno

| Attribute | Details |
|-----------|---------|
| **Valuation** | $2.45B (Nov 2025) |
| **Funding** | $375M+ total ($250M Series C led by Menlo Ventures + NVentures) |
| **Revenue** | $200M ARR |
| **Launched** | Suno Studio ("generative audio workstation") |

**Attribution status**: Settling lawsuits. Warner Music deal (Nov 2025) requires: licensed-only models in 2026, current unlicensed models deprecated, users pay to download. UMG lawsuit ongoing. Sony unresolved.

**Key development**: Suno Studio positions them as professional tools (stems, MIDI export) rather than just consumer toy.

---

#### Udio

**Attribution status**: Settled with both UMG and Warner Music. Pivoting from open generation to "walled garden" — licensed remixing and fan engagement platform launching 2026. Fingerprinting, filtering, and other measures being added.

**Key distinction**: Udio must pivot its entire product, while Suno keeps its model largely intact. Udio becomes a "fan engagement" platform where creations cannot leave the platform.

---

#### Soundverse

| Attribute | Details |
|-----------|---------|
| **HQ** | Sweden, USA, India |
| **Users** | 1.6M+ creators, 3M+ songs generated |
| **Key feature** | "DNA Models" — artist-owned AI models |
| **Competitive rank** | 33rd of 277 active competitors |

**Attribution approach**: Published a whitepaper ("Ethical AI Music Framework") with six stages:
1. **Model Creation**: Partnership-based, artist consent
2. **Application Layer**: DNA models for artist-owned AI
3. **Inference**: Influence functions and embedding analysis for tracking
4. **Export**: Provenance embedded in audio via digital signatures
5. **External Audio**: Catalog scanning for similarity
6. **Compensation**: Ongoing royalties with 5% minimum influence threshold

**Pilot findings** (50 creators, Apr 2024): Real-time transparency dashboards essential; audio quality > volume; creators prefer recurring royalties over one-time; clear thresholds improve functionality.

**Strengths**: Published transparent methodology; Fairly Trained aspirations; strong user traction.

**Sources**: [Soundverse Blog](https://www.soundverse.ai/blog/article/soundverse-just-released-a-blueprint-for-fair-ai-music), [Crunchbase](https://www.crunchbase.com/organization/soundverse)

---

#### Boomy

| Attribute | Details |
|-----------|---------|
| **Founded** | 2019 |
| **Scale** | 14.5M+ songs created (claimed "14% of world's recorded music") |
| **Certification** | Fairly Trained certified (product level) |
| **Distribution** | 40+ streaming platforms |

**Attribution approach**: Models not trained on copyrighted data — uses copyright-safe generative approach. Provides commercial rights to users.

---

#### Other Generation Platforms

| Platform | Attribution Status | Notes |
|----------|-------------------|-------|
| **Stability AI (Stable Audio)** | Trained on licensed data from AudioSparx | Music-specific diffusion model |
| **Google (MusicLM/MusicFX)** | No public attribution mechanism | Research-only, limited release |
| **Meta (MusicGen)** | Open-source, no attribution | CC-BY-NC license on models |
| **AIVA** | Licensed training data | Classical/film score focus |
| **Mubert** | Web3/on-chain attribution (see Tier 6) | Polkadot rollup for creator economy |

---

### Tier 3: Licensing, Certification & Data Providers

#### Fairly Trained (Certification Body)

**Mission**: "Certify fair training data use in Generative AI." Provides "Licensed Model" certification for AI companies that don't use copyrighted work without a license.

**19 certified entities** across three certification levels:

**Company certifications (12)**: Beatoven.ai, Endel, Infinite Album, Lemonaide, LifeScore, Musical AI, Rightsify, Soundful, Splash, Tuney, Voicemod, Voice-Swap

**Product certifications (2)**: Boomy, Frostbite Orckings

**Model certifications (5)**: Jen, Kits, KL3M, Mitsua Likes, Vocalist.ai

**Source**: [fairlytrained.org/certified-models](https://www.fairlytrained.org/certified-models)

---

#### LANDR — Fair Trade AI Program

**Approach**: Pro-rata revenue sharing. Artists using LANDR Distribution can opt-in to allow their music in training, receiving a monthly cut of revenue from LANDR's AI tools. Reported as ~20% pro-rata distribution.

**Key advantage**: Massive existing user base via mastering/distribution platform. AI mastering (Synapse engine) continuously refined by human engineers and user feedback.

**Source**: [LANDR](https://www.landr.com/), [Water & Music](https://www.waterandmusic.com/music-ai-attribution/)

---

#### Lemonaide

**Approach**: Cohort-based attribution. Rather than tracing individual track influence, groups training contributions by genre/style cohorts. MIDI generator with licensed training data. Fairly Trained certified.

---

#### Source Audio / SongLab

**Approach**: Upfront licensing of 33M+ track production music library. "One-stop shop" controlling both master and publishing rights — can move quickly without complex approval chains.

---

#### Human Native AI

**Approach**: Licensing broker connecting rights holders with AI companies. No attribution technology — pure deal-making intermediary.

---

#### Dataset Providers Alliance (DPA)

**Members include**: Rightsify (10M+ owned songs, GCX with 4.4M hours audio), Pro Sound Effects (1.2M sound effects), Sound Ideas. Focus on setting industry standards for data licensing and annotation quality.

---

#### Kits AI

**Approach**: Ethical voice cloning. All voice models trained on directly licensed vocal data from artists. Dynamic revenue-sharing — every conversion compensates the artist. Fairly Trained certified (voice and instrument models).

---

#### Soundful

| Attribute | Details |
|-----------|---------|
| **HQ** | San Diego, CA |
| **Founded** | 2019 |
| **Funding** | $4.5M seed (Jan 2022) |
| **Team** | 11-50 employees |

**Unique approach**: Recorded individual notes from live musicians and built AI models from scratch — never trained on existing songs. Fairly Trained certified. Provides STEM files and MIDI in Pro plan.

---

### Tier 4: Registries & Rights Organizations

#### SoundExchange AI Registry

**Status**: Announced Sep 2024, expected launch Q1 2025. Global ISRC-based registry for sound recording creators to "reserve" rights against AI training. Voluntary tool; leverages SoundExchange's authoritative ISRC database.

**Significance**: If widely adopted, this becomes the canonical "opt-in/opt-out" database for AI training permissions — directly relevant to our MCP permission patchbay concept.

---

#### STIM (Swedish Music Rights Society)

**World-first collective AI music licence** (Sep 2025). Pilot with Songfox using Sureel attribution. Structure: upfront payment + revenue share + attribution-based royalties. Only opted-in works included in first phase.

**Blueprint potential**: If STIM model succeeds, expect other CMOs (ASCAP, BMI, PRS, GEMA, SACEM) to follow with similar frameworks. This creates a global network of collective licensing that our scaffold could interface with.

---

### Tier 5: Content Protection & Detection

#### Pex

**Approach**: Content identification and licensing platform. Blog post on "Navigating AI music tools and copyright" suggests they're positioning for AI attribution adjacent to their existing content ID infrastructure.

---

#### AI Music Detection Research

Key finding from Afchar et al. (IEEE ICASSP 2025): AI music detectors achieve 99.8% accuracy in controlled settings, but face "robustness vulnerabilities when audio undergoes manipulation" and "generalization failures across different generative model architectures." Time-stretching and pitch-shifting bypass detection — similar to how social media users evade copyright fingerprinting.

---

### Tier 6: Web3 & Blockchain Approaches

#### Mubert Protocol

**Approach**: Polkadot-backed rollup for on-chain music attribution. Smart contracts distribute revenue instantly and proportionally. Every audio element fingerprinted, traced, and monetized via tokenized datasets. Partnership with Talisman for data ownership on Polkadot.

**100M+ tracks** generated; integrations with Canva, Restream, Instories.

**Assessment**: Most ambitious decentralized approach, but Web3 adoption in music remains niche. Blockchain overhead may not justify the transparency gains for most use cases.

---

## Competitive Comparison Matrix

| Company | Approach | Funding | Accuracy | Integration | Major Labels | Open Source |
|---------|----------|---------|----------|-------------|-------------|-------------|
| **Sureel** | Training-time gradient tracking | Undisclosed | 86-90% claimed | Decoupled or Integrated | None (indie focus) | No |
| **Musical AI** | Training-time influence tracking | $6M | Not disclosed | Training-time only | None | No |
| **Vermillio** | Content monitoring (TraceID) | $16M | N/A | Post-hoc | Sony | No |
| **ProRata** | Cross-media attribution | $40M | Not disclosed | Various | UMG | No |
| **Soundverse** | Influence functions + embedding | Undisclosed | Not disclosed | Training + inference | None | No |
| **LANDR** | Pro-rata revenue share | N/A | N/A (no attribution) | Opt-in | None | No |
| **Mubert** | On-chain fingerprinting | Web3 Foundation | N/A | Blockchain | None | Partial |
| **This scaffold** | A0-A3 assurance + conformal prediction | Research | TBD | MCP protocol | N/A | **Yes** |

---

## Market Dynamics & Funding

### Funding Timeline

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'background': '#fcfaf5', 'primaryColor': '#1E3A5F'}}}%%
gantt
    title Music AI Attribution Funding (2024-2026)
    dateFormat YYYY-MM
    section Attribution
        Musical AI Seed ($1.5M)         :2025-02, 1M
        Vermillio Series A ($16M)       :2025-03, 1M
        Sureel CDL (undisclosed)        :2024-06, 1M
        Musical AI Series A ($4.5M)     :2026-01, 1M
    section Generation
        Suno Series B ($125M)           :2024-05, 1M
        Suno Series C ($250M)           :2025-11, 1M
        Udio settlements + pivot        :2025-11, 2M
    section Ecosystem
        SoundExchange Registry          :2024-09, 3M
        STIM-Sureel licence             :2025-09, 1M
        Warner-Suno deal                :2025-11, 1M
```

### Key Market Signals

1. **Investor thesis shift**: "Industry alignment, rather than disruption, is the thesis that investors are betting on in 2025." (Water & Music investor recap)
2. **Majority of funded startups focus on rights management**: Musical AI, Vermillio, and Bria lead the rights-management cohort.
3. **Attribution is not yet the bottleneck**: The biggest companies (Suno, Udio) are settling with flat licensing deals, not attribution-based models. Actual per-song attribution remains a research problem.
4. **One-stop rights holders have structural advantages**: Production music libraries and digital distributors move fastest because they control both master and publishing rights.

---

## Academic Research Landscape

### Core Papers on Training Data Attribution (TDA)

| Paper | Authors | Venue | Year | Key Contribution |
|-------|---------|-------|------|-----------------|
| **Large-Scale TDA via Unlearning** | Choi, Koo, Cheuk, Serrà, et al. (Sony) | NeurIPS Creative AI | 2025 | First large-scale TDA for music generation; unlearning-based methods for text-to-music diffusion models |
| **Attribution-by-Design** | Morreale, Hutiri, Serrà, Xiang, Mitsufuji | arXiv 2510.08062 | 2025 | Inference-time provenance; argues training-time TDA is impractical at scale — attribution should be embedded in architecture |
| **Musical Roots via Audio Embeddings** | Barnett, Flores Garcia, Pardo | arXiv 2401.14542 | 2024 | Compares CLMR and CLAP embeddings across 5M clips on VampNet; validates with human listening studies |
| **Watermarking Training Data** | Epple, Shilov, Stevanoski, de Montjoye | arXiv 2412.08549 | 2024 | Audio watermarks persist through training; imperceptible marks cause "noticeable shifts" in model outputs |
| **MiRA: Music Replication Assessment** | Batlle-Roca, Liao, Serra, Mitsufuji, Gómez | ISMIR | 2024 | Model-independent tool detecting exact data replication at >10% rates; open-source |
| **AudioGenX** | Kang, Han, Jeong, Park | AAAI | 2025 | XAI for text-to-audio; input token importance scoring |
| **AI-Generated Music Detection** | Afchar, Meseguer-Brocal, Hennequin | IEEE ICASSP | 2025 | 99.8% detection accuracy but poor robustness to manipulation |
| **Diffusion Attribution Score** | Lin, Tao, Dong, Xu | arXiv 2410.18639 | 2024 | DAS metric for direct comparison of predicted distributions in diffusion models |
| **SSIMuse** | Ji, Wang, Ma, Yu, Zhang | arXiv 2509.13658 | 2025 | Structural similarity for symbolic music replication detection |
| **Gen AI Training & Copyright** | Dornis, Stober | TISMIR | 2025 | Legal analysis: AI training ≠ TDM; memorization creates independent copyright issues |

### Supplemental Resources (from Water & Music)

- [Training data influence analysis survey](https://link.springer.com/article/10.1007/s10994-023-06495-7) (Springer 2023)
- [Anthropic: Tracing Model Outputs to Training Data](https://www.anthropic.com/research/influence-functions)
- [MusicLIME: Explainable Multimodal Music Understanding](https://www.semanticscholar.org/paper/MusicLIME)
- [Data Dividends mapping](https://arxiv.org/abs/1912.00757) (conceptual framework for profit-sharing from AI)

### Key Technical Insight

The Sony NeurIPS paper (Choi et al., 2025) and the Morreale et al. "Attribution-by-Design" paper represent the two fundamental paradigms:

1. **Post-hoc TDA** (Sony): Compute influence after the fact via unlearning. Precise but computationally expensive and requires access to the full model.
2. **Attribution-by-Design** (Morreale): Build provenance into the generation architecture. Scalable but requires adoption during system design.

Our scaffold's A0-A3 assurance levels bridge these paradigms — we don't *require* training-time access (unlike Sureel/Musical AI) but we *incentivize* it through higher assurance ratings.

---

## Open-Source Library Catalog

### Python: Music Information Retrieval

| Library | Stars | License | Last Update | Attribution Relevance |
|---------|-------|---------|-------------|----------------------|
| **librosa** | 8.2k | ISC | Mar 2025 (v0.11) | Audio features, spectrograms, beat tracking |
| **essentia** (MTG) | 3.4k | AGPL-3.0 | Active dev | Comprehensive audio analysis, MIR features |
| **madmom** (CPJKU) | 1.6k | BSD / CC-BY-NC-SA | Nov 2018 (v0.16.1) | Beat/tempo detection, onset detection |
| **mir_eval** | 687 | MIT | Feb 2025 (v0.8.2) | Evaluation metrics for MIR systems |
| **mirdata** | 398 | BSD-3 | Sep 2025 (v1.0) | Standardized MIR dataset loading |
| **aubio** | ~3k | GPL-3.0 | Active | Pitch detection, onset detection |

### Python: Audio Fingerprinting

| Library | Stars | License | Last Update | Attribution Relevance |
|---------|-------|---------|-------------|----------------------|
| **dejavu** | 6.7k | MIT | ~2020 | Audio fingerprinting (Shazam-like) |
| **chromaprint** (AcoustID) | 1.2k | Various | Aug 2025 (v1.6) | Chromagram-based audio fingerprinting |
| **pyacoustid** | 373 | MIT | v1.3.0 | Python bindings for AcoustID/Chromaprint |
| **audfprint** | 591 | MIT | Active | Audio fingerprinting for large collections |

### Python: Music Metadata

| Library | Stars | License | Notes |
|---------|-------|---------|-------|
| **musicbrainzngs** | ~500 | ISC | MusicBrainz API bindings |
| **beets** | ~12k | MIT | Music library manager with MusicBrainz matching |
| **discogs_client** | ~300 | MIT | Discogs API bindings |
| **pylast** | ~400 | Apache-2.0 | Last.fm API bindings |

### Python: AI/ML for Music

| Library | Stars | License | Notes |
|---------|-------|---------|-------|
| **AudioLDM/AudioLDM2** | ~3k | Apache-2.0 | Text-to-audio diffusion model |
| **CLAP** (LAION) | ~1k | Apache-2.0 | Contrastive Language-Audio Pretraining |
| **muzic** (Microsoft) | ~4k | MIT | Music understanding and generation |
| **HeartMuLa** | New | Open | Open-source music foundation models |

### Rust: Audio Processing

| Crate | Downloads | License | Notes |
|-------|-----------|---------|-------|
| **symphonia** | 3.2M+ | MPL-2.0 | Pure Rust audio decoding (±15% of FFmpeg perf) |
| **rodio** | Popular | MIT/Apache-2.0 | Audio playback |
| **rubato** | Growing | MIT | Sample rate conversion |

### JavaScript/TypeScript

| Library | Notes |
|---------|-------|
| **Tone.js** | Web Audio framework |
| **Meyda** | Audio feature extraction for the web |
| **Essentia.js** | WASM port of Essentia |

### Metadata Standards & Identifiers

| Standard | Scope | Relevance |
|----------|-------|-----------|
| **ISRC** | International Standard Recording Code | Recording-level identification |
| **ISWC** | International Standard Musical Work Code | Composition-level identification |
| **ISNI** | International Standard Name Identifier | Creator identification |
| **DDEX** | Digital Data Exchange | B2B metadata standard for music |
| **MusicBrainz** | Open music encyclopedia | Community-maintained entity resolution |
| **AcoustID** | Audio fingerprint database | Links fingerprints to MusicBrainz |

---

## Buy vs Build Analysis

### The Matrix

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'background': '#fcfaf5', 'primaryColor': '#1E3A5F'}}}%%
quadrantChart
    title Buy vs Build Decision Space
    x-axis "Commodity (Buy)" --> "Differentiator (Build)"
    y-axis "Low Risk" --> "High Risk"
    quadrant-1 "Build: Core Differentiator"
    quadrant-2 "Partner: Critical but Standard"
    quadrant-3 "Buy: Commodity"
    quadrant-4 "Experiment: Research Frontier"
    "Auth (Clerk/Supabase)": [0.15, 0.20]
    "Database (Postgres)": [0.20, 0.15]
    "Hosting (Render)": [0.10, 0.10]
    "MusicBrainz API": [0.25, 0.30]
    "Audio fingerprinting": [0.35, 0.40]
    "Entity resolution": [0.65, 0.55]
    "Confidence scoring": [0.80, 0.45]
    "A0-A3 assurance": [0.85, 0.50]
    "MCP server": [0.75, 0.60]
    "Training-time TDA": [0.90, 0.90]
    "LLM (Claude/GPT)": [0.15, 0.35]
    "Embedding models": [0.30, 0.25]
    "Graph RAG": [0.60, 0.65]
```

### Decision Table

| Component | Decision | Rationale |
|-----------|----------|-----------|
| **Auth** | BUY (Clerk or Supabase Auth) | Commodity; ~$0/month at MVP scale |
| **Database** | BUY (PostgreSQL + pgvector) | Well-solved; Neon free tier for dev |
| **Hosting** | BUY (Render or Railway) | Commodity for MVP; migrate later |
| **LLM** | BUY (Claude API) | Commodity; no moat in model choice |
| **Embedding models** | BUY (OpenAI or Cohere) | Commodity; swap later if needed |
| **MusicBrainz integration** | BUILD (thin wrapper) | Open API, but our entity resolution logic is custom |
| **Audio fingerprinting** | BUILD ON (Chromaprint + custom) | Open-source base, custom similarity scoring on top |
| **Entity resolution** | BUILD (core differentiator) | Cross-source reconciliation with confidence is our moat |
| **Confidence scoring** | BUILD (core differentiator) | A0-A3 assurance + conformal prediction is unique |
| **MCP permission server** | BUILD (core differentiator) | No one else offers MCP-based consent infrastructure |
| **Training-time TDA** | SKIP for now | Research frontier; leave to Sureel/Musical AI/Sony |
| **Graph knowledge base** | BUILD (core differentiator) | Graph RAG over entity-resolved music data |
| **Chat gap-filling** | BUILD (moderate differentiator) | LLM integration is commodity, but the UX workflow is unique |

### What Musical AI Is Building (Estimated Architecture)

Based on public statements, Musical AI's stack likely includes:
1. **Catalog ingestion pipeline** — audio fingerprinting + metadata normalization
2. **Embedding index** — vector representation of training data
3. **Training-time hooks** — integration with partner AI models during training
4. **Influence computation** — post-training analysis of training-data contribution percentages
5. **Royalty calculation engine** — translates influence % to payment amounts
6. **Payment distribution** — connects to rights holder payment systems
7. **Dashboard/API** — for rights holders and AI companies

**What we could replicate**: Items 1-2, 6-7 are standard infrastructure. Items 3-5 are their differentiation.

**What we uniquely add**: The scaffold provides *transparent confidence scoring* (not a black box), *MCP-based permission queries* (machine-readable consent), and *academic rigor* (conformal prediction, published methodology). No commercial player currently offers open, verifiable confidence metrics on attribution.

---

## Minimum Viable Architecture (MVA)

### Definition

The MVA is the minimum technical architecture that demonstrates enough value to attract initial users (artists, rights holders) and generate meaningful feedback. It must balance:

- **Technical credibility** — enough to convince engineers this is real
- **Domain value** — enough to convince musicians this is useful
- **Business viability** — enough to convince investors this has a path to revenue

### MVA Components

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'background': '#fcfaf5', 'primaryColor': '#1E3A5F', 'lineColor': '#333333'}}}%%
flowchart TB
    subgraph mvp["MVA (Minimum Viable Architecture)"]
        direction TB
        DB[(PostgreSQL<br/>+ pgvector)]
        API[FastAPI<br/>Backend]
        MB[MusicBrainz<br/>Integration]
        ER[Entity<br/>Resolution]
        CS[Confidence<br/>Scoring<br/>A0-A3]
        MCP[MCP Permission<br/>Server]
        CHAT[Chat Interface<br/>Gap-Filling]
        DASH[Artist<br/>Dashboard]
    end

    subgraph external["External Services"]
        LLM[Claude API]
        EMB[Embedding<br/>Model]
        AUTH[Clerk/Supabase<br/>Auth]
    end

    subgraph data["Data Sources"]
        MBD[MusicBrainz]
        DIS[Discogs]
        AID[AcoustID]
    end

    DASH --> API
    CHAT --> API
    API --> DB
    API --> ER
    API --> CS
    API --> MCP
    API --> LLM
    API --> EMB
    ER --> MB
    MB --> MBD
    MB --> DIS
    MB --> AID
    API --> AUTH

    style DB fill:#1E3A5F,color:#fff
    style ER fill:#C75050,color:#fff
    style CS fill:#C75050,color:#fff
    style MCP fill:#4A7C59,color:#fff
    style CHAT fill:#D4A03C,color:#000
```

### MVA Cost Estimate

| Component | Monthly Cost (MVP) | Notes |
|-----------|-------------------|-------|
| Render/Railway (API + worker) | $7-25 | Starter tier |
| Neon PostgreSQL (free → $19) | $0-19 | 0.5 GB storage free |
| Claude API | $10-50 | Low volume during dev |
| Embedding model API | $5-20 | OpenAI text-embedding-3-small |
| Clerk/Supabase Auth | $0-25 | Free tier generous |
| Domain + DNS | $12/year | — |
| **Total** | **$22-139/month** | — |

### MVA Timeline Estimate

| Phase | Duration | Output |
|-------|----------|--------|
| Core backend (API + DB + entity resolution) | 4-6 weeks | Working API with MusicBrainz integration |
| Confidence scoring (A0-A3) | 2-3 weeks | Assurance level assignment |
| Chat gap-filling interface | 2-3 weeks | Basic conversational UX |
| MCP permission server | 1-2 weeks | Read-only permission queries |
| Artist dashboard | 2-3 weeks | Basic catalog view + confidence |
| **Total to demo** | **11-17 weeks** | — |

For a solo developer or 2-person team, this is roughly **3-4 months to a demonstrable prototype**. Industry benchmarks suggest SaaS MVPs with AI features cost $30-100K and take 3-6 months.

### MVA Encoding in Probabilistic PRD

The MVA maps to specific decision node paths in the probabilistic PRD:

```yaml
mva_path:
  L1_build_vs_buy: managed_services     # Buy infrastructure, build differentiators
  L1_target_market: indie_artists       # Not majors (too complex for MVP)
  L2_data_model: graph_enhanced_rdbms   # PostgreSQL + entity graph
  L2_api_protocol: rest_mcp_hybrid      # REST API + MCP server
  L2_service_decomposition: modular_monolith
  L3_primary_database: postgresql_unified
  L3_graph_strategy: pg_recursive_cte   # Start simple, migrate to Neo4j if needed
  L3_llm_provider: anthropic_primary
  L3_frontend: next_js_app_router
  L3_auth: clerk_or_supabase
  L4_compute: render_or_railway
  L4_database_hosting: neon
  joint_probability: 0.35               # Given solo_hacker archetype
```

---

## Risk & Probability Framework

### Engineering Investment vs Business Return

The fundamental question: **If we invest 3x engineering resources beyond the MVA, does the business outcome improve more than 1.01x?**

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'background': '#fcfaf5', 'primaryColor': '#1E3A5F'}}}%%
xychart-beta
    title "Marginal Engineering Return Curve"
    x-axis "Engineering Investment (Normalized)" [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y-axis "Business Value (Normalized)" 0 --> 10
    line "With Traction" [0.5, 2, 4, 6, 7.5, 8.5, 9, 9.3, 9.5, 9.6]
    line "Without Traction" [0.5, 1, 1.5, 1.8, 2, 2.1, 2.15, 2.18, 2.2, 2.2]
```

**Key insight**: The curve depends entirely on **traction**. With user adoption (artists, labels engaging), engineering investment compounds — better entity resolution means better confidence, which attracts more users, which provides more data. Without traction, engineering beyond MVA has near-zero marginal return.

### Risk Matrix

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| **No user traction** | 0.45 | Critical | Start with Imogen/Andy's catalog; demonstrate value before scaling |
| **Major label builds competing system** | 0.30 | High | Focus on indie/heritage artists; open-source creates different value |
| **AI platforms ignore permissions** | 0.35 | High | Monitor legal developments; EU AI Act enforcement |
| **MCP protocol doesn't stabilize** | 0.20 | Medium | Abstract protocol layer; MCP is Anthropic-backed with momentum |
| **Confidence calibration fails with limited data** | 0.40 | Medium | Use conformal prediction (works with small samples); Bayesian updating |
| **Entity resolution doesn't scale** | 0.25 | Medium | Start simple (MusicBrainz fuzzy match); PostgreSQL handles millions |
| **Regulatory shift changes everything** | 0.30 | Medium | Flexible architecture; monitor EU AI Act, US legislation |
| **Funding dries up** | 0.50 | High | Open-source ensures continuity; academic paper provides credibility |

### The Adoption Flywheel

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'background': '#fcfaf5', 'primaryColor': '#1E3A5F', 'lineColor': '#333333'}}}%%
flowchart TB
    A[Artists register<br/>catalogs] --> B[Entity resolution<br/>improves]
    B --> C[Confidence scores<br/>calibrate]
    C --> D[API trust<br/>increases]
    D --> E[AI platforms<br/>query permissions]
    E --> F[Artists see<br/>value]
    F --> A

    G[No traction] -.->|breaks| A
    H[Competition] -.->|breaks| D

    style A fill:#D4A03C,color:#000
    style C fill:#1E3A5F,color:#fff
    style E fill:#4A7C59,color:#fff
    style G fill:#C75050,color:#fff
    style H fill:#C75050,color:#fff
```

**Critical path**: The flywheel only spins if artists register. Technical excellence without artist adoption is worthless. This is why the domain expert feedback system (next section) is architecturally critical, not just nice-to-have.

---

## Human-Machine Decision Making

### The Problem

Domain experts (musicians, rights administrators) need to:
1. **Validate** automated confidence scores — "Is this attribution correct?"
2. **Provide** knowledge that no database contains — "This session musician was uncredited"
3. **Refine** system probabilities — "Your 70% confidence feels more like 90% to me"
4. **Detect** edge cases — "This is a pseudonym for the same person"

These experts may not be tech-savvy. The system must meet them where they are.

### Uncertainty Visualization

**Hypothetical Outcome Plots (HOPs)** are the gold standard for communicating uncertainty to non-experts. Research shows HOPs "greatly improve multivariate probability estimation over conventional static uncertainty visualizations" and "leverage the ability of the visual system to quickly, accurately, and automatically process the summary statistical properties of ensembles."

For our attribution context, HOPs would show: "Here are 20 possible attribution scenarios for this song, animated. In most of them, Artist X has >60% contribution."

### Visual Analogue Scale (VAS) for Expert Feedback

Rather than asking experts "Is the confidence 0.73?", present a slider:

```
How confident are you that this attribution is correct?

Not at all ├──────────────|───────────────────┤ Completely
confident   0%            50%        ↑(73%)    100%   confident
                                   System says
```

The expert's slider position becomes a Bayesian prior update on the system's confidence.

### Calibration Interface Pattern

```
Song: "Midnight Shadows" (2019)
System Attribution (A2 — Source-Verified):
  - Primary songwriter: Jamie Chen (85% confidence)
  - Producer: Studio X (72% confidence)
  - Session drummer: Unknown (flagged for review)

┌─────────────────────────────────────────┐
│ Do you agree with this attribution?     │
│                                         │
│ [✓ Correct] [~ Partially] [✗ Wrong]     │
│                                         │
│ If partially or wrong, what's missing?  │
│ ┌─────────────────────────────────────┐ │
│ │ The session drummer is actually     │ │
│ │ Marcus Williams, he played on the   │ │
│ │ whole album...                      │ │
│ └─────────────────────────────────────┘ │
│                                         │
│ How confident are you?                  │
│ Low ├──────────────────|──┤ High        │
│                        ↑                │
│                   (You: 85%)            │
└─────────────────────────────────────────┘
```

---

## Domain Expert Feedback Mechanisms

### FeedbackCards (Zhou et al., 2023)

FeedbackCards ([arXiv:2307.15475](https://arxiv.org/abs/2307.15475)) are structured documents for capturing stakeholder corrections and overrides that support continual learning. Applied to our context:

**FeedbackCard for Attribution Review**:

```yaml
feedback_card:
  version: 1.0
  reviewer:
    id: expert_001
    role: artist  # artist | manager | rights_admin | musicologist
    expertise_level: domain_expert  # novice | intermediate | domain_expert
    catalog_size: 47  # songs in their catalog

  reviewed_entity:
    type: song_attribution
    song_id: "isrc:GBAYE0000001"
    title: "Midnight Shadows"

  system_attribution:
    assurance_level: A2
    primary_songwriter: { name: "Jamie Chen", confidence: 0.85 }
    producer: { name: "Studio X", confidence: 0.72 }
    session_drummer: { name: null, confidence: 0.0 }

  expert_corrections:
    - field: session_drummer
      system_value: null
      corrected_value: "Marcus Williams"
      expert_confidence: 0.95
      evidence: "I was at the session. He played on tracks 1-8."
      evidence_type: firsthand_knowledge

    - field: primary_songwriter.confidence
      system_value: 0.85
      corrected_value: 0.95
      expert_confidence: 0.90
      evidence: "Jamie wrote this solo, no co-writers."

  meta_feedback:
    overall_quality: 4  # 1-5 scale
    missing_roles: ["backing_vocalist"]
    unexpected_roles: []
    time_spent_minutes: 3
    would_review_again: true
```

### Active Learning Loop

The feedback system implements an active learning strategy:

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'background': '#fcfaf5', 'primaryColor': '#1E3A5F', 'lineColor': '#333333'}}}%%
flowchart TB
    subgraph system["System Side"]
        A[Entity Resolution<br/>Engine] --> B[Confidence<br/>Scorer]
        B --> C[Uncertainty<br/>Detector]
        C -->|High uncertainty<br/>items| D[Review Queue<br/>Prioritizer]
    end

    subgraph expert["Expert Side"]
        D --> E[Expert Dashboard]
        E --> F[FeedbackCard<br/>Submission]
        F --> G[Bayesian<br/>Update]
        G --> A
    end

    subgraph convergence["Convergence Monitor"]
        G --> H{Expert agreement<br/>reached?}
        H -->|No| D
        H -->|Yes| I[Promote to<br/>higher assurance]
    end

    style C fill:#C75050,color:#fff
    style E fill:#D4A03C,color:#000
    style I fill:#4A7C59,color:#fff
```

**Priority queue logic**: Present experts with items where:
1. Confidence is near a decision boundary (e.g., 0.48-0.52 for binary decisions)
2. Multiple sources disagree
3. Entity resolution produced multiple candidates
4. The item has never been reviewed

### Multi-Reviewer Convergence

For critical attributions, require multiple independent reviews:

| Assurance Target | Min Reviewers | Agreement Threshold | Notes |
|-----------------|---------------|--------------------|----|
| **A1** (Self-Declared) | 1 | N/A | Artist's own declaration |
| **A2** (Source-Verified) | 1 expert | Single confirmation | Cross-checked against source data |
| **A3** (Identity-Verified) | 2+ experts | 80% agreement | Independent verification required |

### Implementation in the Probabilistic PRD

The expert feedback system connects to the probabilistic PRD via a new decision node:

```yaml
decision_id: expert_feedback_mechanism
decision_level: L3_implementation
options:
  - option_id: inline_vas_cards
    prior_probability: 0.45
    description: "VAS sliders + FeedbackCards inline with dashboard"
    status: recommended
  - option_id: separate_review_app
    prior_probability: 0.25
    description: "Dedicated review application with queue management"
    status: viable
  - option_id: chat_based_review
    prior_probability: 0.20
    description: "Review embedded in conversational gap-filling"
    status: viable
  - option_id: email_questionnaire
    prior_probability: 0.10
    description: "Periodic email with review requests"
    status: deferred
```

---

## Strategic Implications for This Scaffold

### What No One Else Offers

| Differentiator | Why It Matters | Nearest Competitor |
|---------------|----------------|-------------------|
| **Open-source transparency** | Auditable attribution — not a black box | None (all competitors are proprietary) |
| **A0-A3 assurance levels** | Tiered confidence with formal definitions | Sureel has "attribution likelihood" but no formal framework |
| **Conformal prediction** | Statistically valid confidence intervals | No competitor uses formal UQ methods |
| **MCP permission patchbay** | Machine-readable consent for AI platforms | SoundExchange registry is closest but not MCP-native |
| **Domain-agnostic backbone** | Same architecture works for DPP/traceability | All competitors are music-only |
| **Academic foundation** | SSRN preprint provides credibility | Morreale et al. is closest but theoretical only |

### Strategic Positioning

This scaffold occupies a unique position: **the research-grade, open, neutral infrastructure layer** that complements (rather than competes with) the commercial players.

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'background': '#fcfaf5', 'primaryColor': '#1E3A5F', 'lineColor': '#333333'}}}%%
quadrantChart
    title Strategic Positioning
    x-axis "Closed/Proprietary" --> "Open/Transparent"
    y-axis "Simple (Licensing Only)" --> "Sophisticated (Full Attribution)"
    quadrant-1 "Our Target Position"
    quadrant-2 "Research Papers"
    quadrant-3 "Licensing Deals"
    quadrant-4 "Commercial Attribution"
    "Sureel": [0.15, 0.85]
    "Musical AI": [0.20, 0.75]
    "Vermillio": [0.10, 0.50]
    "LANDR Fair Trade": [0.30, 0.15]
    "Lemonaide": [0.25, 0.30]
    "Suno deals": [0.10, 0.10]
    "SoundExchange": [0.40, 0.25]
    "This scaffold": [0.90, 0.80]
    "Sony TDA paper": [0.85, 0.90]
    "Morreale (AttrByDesign)": [0.80, 0.85]
```

### Recommendations

1. **Don't compete on training-time TDA** — Leave gradient-tracking to Sureel/Sony. Our value is in the *metadata layer* (entity resolution, confidence, permissions), not the model internals.

2. **Partner, don't replace** — Design the MCP server so Musical AI, Sureel, or STIM could *plug into* our permission infrastructure. We provide the consent query layer; they provide the attribution computation.

3. **Traction > technical sophistication** — The market repeatedly shows that trust and adoption matter more than attribution precision. Focus first on getting Imogen/Andy's catalogs into the system.

4. **Open-source is the moat** — In a market where everyone is proprietary, being the only open, auditable attribution system creates unique positioning for regulatory compliance (EU AI Act) and academic credibility.

5. **Start with A1-A2, earn A3** — MVP should handle self-declared (A1) and source-verified (A2) attributions well. Identity-verified (A3) requires real-world verification infrastructure that can come later.

6. **The feedback loop IS the product** — The domain expert FeedbackCard system is not a feature — it's the core value proposition. Better human input → better confidence → more trust → more users.

---

## Reviewer Feedback Log

| Date | Reviewer | Domain | Feedback | Resolution |
|------|----------|--------|----------|------------|
| 2026-02-10 | Initial draft | — | Generated from web research + local sources | — |
| — | *Imogen* | Artist/songwriter | *Pending* | — |
| — | *Andy* | Rights administration | *Pending* | — |
| — | *Technical reviewer* | Engineering | *Pending* | — |

---

## Sources Index

### Company Sources
- [Musical AI funding — MBW](https://www.musicbusinessworldwide.com/musical-ai-bags-4-5m-in-funding-round-to-scale-ai-attribution-tech/)
- [Musical AI funding — Digital Music News](https://www.digitalmusicnews.com/2026/01/13/musical-ai-funding-january-2026/)
- [Sureel — A2IM Spotlight](https://a2im.org/ams-sureel-ai/)
- [Sureel patents — Justia](https://patents.justia.com/assignee/sureel-inc)
- [STIM-Sureel deal — Digital Music News](https://www.digitalmusicnews.com/2025/09/26/stim-taps-sureel-ai-attribution-tracking/)
- [Vermillio — Axios](https://www.axios.com/2025/03/03/vermillio-ai-rights-licensing-sony-music)
- [Suno Series C — TechCrunch](https://techcrunch.com/2025/11/19/legally-embattled-ai-music-startup-suno-raises-at-2-45b-valuation-on-200m-revenue/)
- [Warner-Suno deal — MBW](https://www.musicbusinessworldwide.com/warner-music-group-settles-with-suno-strikes-first-of-its-kind-deal-with-ai-song-generator/)
- [UMG-Udio settlement — Hollywood Reporter](https://www.hollywoodreporter.com/music/music-industry-news/universal-music-group-announces-settlement-with-udio-1236414023/)
- [Fairly Trained certified models](https://www.fairlytrained.org/certified-models)
- [Soundverse whitepaper](https://www.soundverse.ai/blog/article/soundverse-just-released-a-blueprint-for-fair-ai-music)
- [SoundExchange AI Registry](https://www.soundexchange.com/news/soundexchange-developing-global-ai-sound-recording-registry/)
- [Mubert Polkadot rollup](https://mubert.com/blog/mubert-partners-with-polkadot-and-web3-foundation-to-build-a-decentralized-data-chain-for-creators-and-generative-ai)
- [Billboard Top AI Music Companies 2026](https://www.billboard.com/lists/top-ai-music-companies-2026-future-music/)

### Academic Sources
- Choi et al. "Large-Scale TDA via Unlearning" — [arXiv:2506.18312](https://arxiv.org/abs/2506.18312) (NeurIPS 2025)
- Morreale et al. "Attribution-by-Design" — [arXiv:2510.08062](https://arxiv.org/abs/2510.08062)
- Barnett et al. "Musical Roots via Audio Embeddings" — [arXiv:2401.14542](https://arxiv.org/abs/2401.14542)
- Epple et al. "Watermarking Training Data" — [arXiv:2412.08549](https://arxiv.org/abs/2412.08549)
- Batlle-Roca et al. "MiRA" — [arXiv:2407.14364](https://arxiv.org/abs/2407.14364) (ISMIR 2024)
- Kang et al. "AudioGenX" — [arXiv:2502.00459](https://arxiv.org/abs/2502.00459) (AAAI 2025)
- Afchar et al. "AI-Generated Music Detection" — [arXiv:2501.10111](https://arxiv.org/abs/2501.10111) (ICASSP 2025)
- Dornis & Stober "Gen AI Training & Copyright" — [arXiv:2502.15858](https://arxiv.org/abs/2502.15858) (TISMIR 2025)
- Lin et al. "Diffusion Attribution Score" — [arXiv:2410.18639](https://arxiv.org/abs/2410.18639)
- Ji et al. "SSIMuse" — [arXiv:2509.13658](https://arxiv.org/abs/2509.13658)
- Zhou et al. "FeedbackCards" — [arXiv:2307.15475](https://arxiv.org/abs/2307.15475)

### Industry Analysis
- [Water & Music: How music AI attribution actually works](https://www.waterandmusic.com/music-ai-attribution/)
- [Water & Music: Music tech capital investor recap](https://www.waterandmusic.com/music-tech-capital-investor-recap-nyc/)
- [Music Ally: A to Z of AI Music 2025](https://musically.com/2025/12/17/the-a-to-z-of-ai-music-in-2025-part-4-transparency-to-zero-sum-game/)
- [MusicWorks: Data, Licensing, and Future of Music AI](https://musicworks.substack.com/p/data-licensing-and-the-future-of)
- [Appetite for Distraction: Computational Copyright](https://www.appetitefordistraction.xyz/p/not-another-rant-on-ethical-training)

---

## Visual Documentation

Visual companion figures for the landscape report, organized by topic.

### Problem & Market (Figures 01--05)

<details>
<summary>Expand: Problem & Market figures (5 images)</summary>

![Problem taxonomy of music AI attribution challenges](../../figures/repo-figures/assets/fig-landscape-01-problem-taxonomy.jpg)

*Caption: Taxonomy of core problems in music AI attribution — metadata errors, unclaimed royalties, and missing consent frameworks.*

![Funding by category across the music AI attribution sector](../../figures/repo-figures/assets/fig-landscape-02-funding-by-category.jpg)

*Caption: Funding distribution across attribution infrastructure, generation platforms, licensing, and Web3 categories.*

![Papers to products pipeline in music attribution](../../figures/repo-figures/assets/fig-landscape-03-papers-to-products.jpg)

*Caption: The path from academic research papers to commercial attribution products — transfer gaps and timelines.*

![Disruption points in the music value chain](../../figures/repo-figures/assets/fig-landscape-04-disruption-points.jpg)

*Caption: Key disruption points where AI-generated music challenges existing attribution and royalty distribution.*

![Maturity spectrum of attribution approaches](../../figures/repo-figures/assets/fig-landscape-05-maturity-spectrum.jpg)

*Caption: Maturity spectrum from research prototypes to production-grade attribution systems.*

</details>

### Decision & Strategy (Figures 06--08)

<details>
<summary>Expand: Decision & Strategy figures (3 images)</summary>

![Founder decision framework for music attribution startups](../../figures/repo-figures/assets/fig-landscape-06-founder-decision-framework.jpg)

*Caption: Decision framework for founders choosing between training-time attribution, inference-time attribution, and licensing-only approaches.*

![Misaligned incentives across the music AI ecosystem](../../figures/repo-figures/assets/fig-landscape-07-misaligned-incentives.jpg)

*Caption: Mapping misaligned incentives between AI platforms, rights holders, artists, and CMOs.*

![Regulatory fragmentation across jurisdictions](../../figures/repo-figures/assets/fig-landscape-08-regulatory-fragmentation.jpg)

*Caption: Regulatory fragmentation — EU AI Act, US copyright cases, and emerging global frameworks create a patchwork compliance landscape.*

</details>

### Technical Methods (Figures 09--16)

<details>
<summary>Expand: Technical Methods figures (8 images)</summary>

![Seven training data attribution methods compared](../../figures/repo-figures/assets/fig-landscape-09-seven-tda-methods.jpg)

*Caption: Seven TDA methods — influence functions, unlearning, data Shapley, gradient tracking, embedding analysis, watermarking, and replication detection.*

![Two paradigms of attribution: post-hoc vs by-design](../../figures/repo-figures/assets/fig-landscape-10-two-paradigms.jpg)

*Caption: The two fundamental paradigms — post-hoc training data attribution (Sony/Sureel) vs. attribution-by-design (Morreale et al.).*

![Watermarking robustness across audio transformations](../../figures/repo-figures/assets/fig-landscape-11-watermarking-robustness.jpg)

*Caption: Watermarking robustness — how audio watermarks survive compression, time-stretching, pitch-shifting, and re-encoding.*

![Content ID system evolution from fingerprinting to AI](../../figures/repo-figures/assets/fig-landscape-12-content-id-evolution.jpg)

*Caption: Content ID evolution from simple audio fingerprinting to AI-powered content identification and attribution.*

![The metadata mess across music industry databases](../../figures/repo-figures/assets/fig-landscape-13-metadata-mess.jpg)

*Caption: The metadata mess — fragmented, inconsistent, and incomplete records across ISRC, ISWC, MusicBrainz, Discogs, and proprietary databases.*

![On-chain vs off-chain attribution approaches](../../figures/repo-figures/assets/fig-landscape-14-onchain-offchain.jpg)

*Caption: On-chain vs. off-chain attribution — blockchain transparency trade-offs against scalability and adoption barriers.*

![Evidence chain for multi-source attribution](../../figures/repo-figures/assets/fig-landscape-15-evidence-chain.jpg)

*Caption: Evidence chain construction — how multiple data sources combine into confidence-scored attribution records.*

![Uncertainty quantification across attribution domains](../../figures/repo-figures/assets/fig-landscape-16-uq-cross-domain.jpg)

*Caption: Cross-domain uncertainty quantification — conformal prediction, Bayesian updating, and calibration applied to music attribution.*

</details>

### Business Models (Figures 17--24)

<details>
<summary>Expand: Business Models figures (9 images)</summary>

![Licensing models for AI music training data](../../figures/repo-figures/assets/fig-landscape-17-licensing-models.jpg)

*Caption: Licensing model comparison — upfront licensing, pro-rata revenue share, attribution-based royalties, and cohort-based approaches.*

![CMO transformation from analog to AI-era licensing](../../figures/repo-figures/assets/fig-landscape-18-cmo-transformation.jpg)

*Caption: CMO transformation — how collective management organizations are adapting from analog-era blanket licenses to AI-era attribution-based licensing.*

![Ethical certification landscape for AI music](../../figures/repo-figures/assets/fig-landscape-19-ethical-certification.jpg)

*Caption: Ethical certification landscape — Fairly Trained, LANDR Fair Trade AI, and emerging standards for responsible AI music training.*

![AI code and tool landscape for music attribution](../../figures/repo-figures/assets/fig-landscape-19b-ai-code-landscape.jpg)

*Caption: AI code and tool landscape — open-source libraries, commercial APIs, and emerging frameworks for music attribution engineering.*

![Voice rights stack for AI voice cloning and synthesis](../../figures/repo-figures/assets/fig-landscape-20-voice-rights-stack.jpg)

*Caption: Voice rights stack — consent, cloning, synthesis, and compensation layers for AI voice technology.*

![History of music information retrieval research](../../figures/repo-figures/assets/fig-landscape-21-mir-history.jpg)

*Caption: MIR history — from early audio fingerprinting research through deep learning to modern attribution systems.*

![Platform evolution from streaming to AI-native music](../../figures/repo-figures/assets/fig-landscape-22-platform-evolution.jpg)

*Caption: Platform evolution — how music platforms are transitioning from streaming-only to AI-native generation and attribution.*

![Build vs buy analysis for attribution infrastructure](../../figures/repo-figures/assets/fig-landscape-23-build-vs-buy.jpg)

*Caption: Build vs. buy decision matrix — which attribution components to build in-house vs. purchase or partner for.*

![Revenue distribution models in AI-generated music](../../figures/repo-figures/assets/fig-landscape-24-revenue-distribution.jpg)

*Caption: Revenue distribution models — how AI-generated music revenue flows to training data contributors, platforms, and artists.*

</details>

### Research & Future (Figures 25--32)

<details>
<summary>Expand: Research & Future figures (8 images)</summary>

![Research priorities for music AI attribution](../../figures/repo-figures/assets/fig-landscape-25-research-priorities.jpg)

*Caption: Research priorities — key open problems ranked by impact and feasibility for the attribution community.*

![Cross-domain transfer of attribution techniques](../../figures/repo-figures/assets/fig-landscape-26-cross-domain-transfer.jpg)

*Caption: Cross-domain transfer — how attribution methods from text, image, and code domains apply to music.*

![Agentic attribution with AI agents managing provenance](../../figures/repo-figures/assets/fig-landscape-27-agentic-attribution.jpg)

*Caption: Agentic attribution — AI agents autonomously querying permissions, verifying provenance, and managing consent via MCP.*

![Emerging categories in music AI attribution](../../figures/repo-figures/assets/fig-landscape-28-emerging-categories.jpg)

*Caption: Emerging categories — new market segments forming around AI music attribution, voice rights, and consent infrastructure.*

![Regulatory cascade from EU AI Act to global frameworks](../../figures/repo-figures/assets/fig-landscape-29-regulatory-cascade.jpg)

*Caption: Regulatory cascade — how EU AI Act enforcement triggers adaptation in US, UK, and Asian markets.*

![Convergence thesis for music attribution approaches](../../figures/repo-figures/assets/fig-landscape-30-convergence-thesis.jpg)

*Caption: Convergence thesis — training-time, inference-time, and licensing-based attribution are converging toward hybrid approaches.*

![Open problems in music AI attribution research](../../figures/repo-figures/assets/fig-landscape-31-open-problems.jpg)

*Caption: Open problems — unsolved challenges including scalable TDA, cross-model attribution, and adversarial robustness.*

![Meta-loop of attribution system improvement](../../figures/repo-figures/assets/fig-landscape-32-meta-loop.jpg)

*Caption: Meta-loop — how attribution systems improve through artist feedback, confidence calibration, and ecosystem adoption.*

</details>
