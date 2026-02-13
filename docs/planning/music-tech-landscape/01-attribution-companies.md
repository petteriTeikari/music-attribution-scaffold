# Attribution Infrastructure Companies — Detailed Profiles

> **Parent**: [README.md](README.md) > Tier 1: Attribution Infrastructure
> **Updated**: 2026-02-10

---

## Musical AI (formerly Somms.ai)

### Company Profile

| Attribute | Details |
|-----------|---------|
| **Legal name** | Musical AI (formerly SOMMS AI) |
| **HQ** | Ottawa/Halifax, Canada |
| **Website** | [wearemusical.ai](https://wearemusical.ai/) |
| **Founded** | ~2023; rebranded to Musical AI in 2024 |
| **Employees** | ~5 (CBInsights) |
| **LinkedIn** | [linkedin.com/company/musical-ai](https://linkedin.com/company/musical-ai) |
| **Sales** | sales@wearemusical.ai |

### Funding History

| Round | Amount | Date | Lead | Participants |
|-------|--------|------|------|-------------|
| Pre-seed | $1.3M | ~2023-2024 | Build Ventures (Halifax) | Angels incl. Tommy Danvers (Ministry of Sound) |
| Seed | $1.5M ($2.1M CAD) | ~Feb 2025 | — | BDC (Business Development Bank of Canada) |
| Seed II | $4.5M | Jan 2026 | Heavybit | BDC, Build Ventures |
| **Total** | **~$7.3M** | | | |

### Leadership Team

| Role | Person | Background |
|------|--------|------------|
| **CEO & Co-founder** | Sean Power | — |
| **COO & Co-founder** | Matthew Adell | Former Beatport CEO |
| **Co-founder** | Nicolas Gonzalez Thomas | — |
| **Advisor** | Vickie Nauman | Music licensing expert |
| **Advisor** | Alastair Croll | Technology entrepreneur |

### Technical Approach

Musical AI's core capability: determining *what percentage of a generated output came from which source*. Their platform enables:

1. **Cleared data access** for generative AI companies
2. **Real-time usage monitoring** and payment distribution to rightsholders
3. **IP monetization control** for creators

The technology traces which training data influences specific outputs from generative AI models. This distinguishes between detecting AI audio generally and identifying specific source materials for compensation purposes — a critical gap as most DSPs still fail to properly tag machine-generated uploads.

**Integration model**: Requires presence during initial model training. Post-hoc analysis is not supported. Their platform claims it can determine what percentage of an AI-generated output originates from specific source materials, a crucial distinction that goes beyond basic AI detection and moves into the realm of compensation and licensing.

**No published patents** — in contrast to Sureel's portfolio.

### Estimated Architecture

Based on public statements and partnerships:

```
┌─────────────────────────────────────────────────────────────┐
│                      Rights Holder Side                      │
├─────────────────────────────────────────────────────────────┤
│ Pro Sound Effects │ SourceAudio │ Symphonic │ Kanjian       │
│ (catalog)         │ (catalog)   │ (distrib) │ (China)       │
└────────────┬──────┴─────────────┴───────────┴───────────────┘
             │
             ▼
┌─────────────────────────────────────────────────────────────┐
│              Musical AI Ingestion Pipeline                    │
│  - Audio fingerprinting / embedding generation               │
│  - Metadata normalization and validation                     │
│  - Rights chain verification                                 │
└────────────┬────────────────────────────────────────────────┘
             │
             ▼
┌─────────────────────────────────────────────────────────────┐
│              Embedding / Fingerprint Index                    │
│  - Vector representations of all training-eligible audio     │
│  - Searchable index for similarity/influence computation     │
└────────────┬────────────────────────────────────────────────┘
             │
             ▼
┌─────────────────────────────────────────────────────────────┐
│         AI Company Model Training (Integrated)               │
│  - Musical AI hooks integrated during training               │
│  - Monitors which data points influence model weights        │
│  - Partners: Beatoven.ai, SoundBreak AI                     │
└────────────┬────────────────────────────────────────────────┘
             │
             ▼
┌─────────────────────────────────────────────────────────────┐
│           Influence Computation / Royalty Sheets              │
│  - Post-training: compute % influence per source             │
│  - Generate "royalty sheets" mapping sources → percentages   │
│  - Aggregate across all generated outputs                    │
└────────────┬────────────────────────────────────────────────┘
             │
             ▼
┌─────────────────────────────────────────────────────────────┐
│              Payment Distribution System                     │
│  - Translate influence % → payment amounts                   │
│  - Beatoven deal: 30% of revenue to training data sources   │
│  - Distribute to rights holders via existing rails           │
└─────────────────────────────────────────────────────────────┘
```

### Partnerships & Customers

| Partner | Type | Date | Details |
|---------|------|------|---------|
| **Beatoven.ai** | AI generator | Dec 2024 | "First fully licensed, rightsholder-compensating" AI music platform. 30% of revenue to training contributors. |
| **SoundBreak AI** | AI generator | 2025 | Founded by Better Than Ezra's Kevin Griffin. Licensed model training via Musical AI. Formerly known as SESHY. |
| **Pro Sound Effects** | Data source | 2025 | 1.2M professionally recorded sound effects |
| **SourceAudio** | Data source | 2025 | Large production music catalog |
| **Symphonic Distribution** | Data source | 2024 | Indie music distribution. CEO Jorge Brea stated excitement to "innovate rapidly in the music AI space" |
| **Kanjian** | Market expansion | 2025 | Chinese market music distribution |
| **Fairly Trained** | Certification | 2024 | "Licensed Model" certification |

### Competitors (per CBInsights)

ProRata.ai, Human Native AI, Salt, Roon Labs, DigiTraxAI, and 7 more.

### Key Quotes

> "We have made attribution simple and turnkey" — Sean Power, CEO

> "[We] can not only license IP but also pay all involved rightsholders accurately and consistently"

### SWOT Analysis

| Strengths | Weaknesses |
|-----------|------------|
| Turnkey positioning; strong industry relationships via Adell network; Fairly Trained certified; plans to expand beyond music | Only 5 employees; requires training-time integration (no post-hoc); no patents; no public accuracy metrics |

| Opportunities | Threats |
|--------------|---------|
| Expansion to other creative sectors; growing regulatory demand for attribution; partnership with more AI generators | ProRata ($40M, UMG deal) has more resources; Sureel has stronger IP (patents); major labels may build in-house |

### Sources

- [Musical AI raises $4.5m — MBW](https://www.musicbusinessworldwide.com/musical-ai-bags-4-5m-in-funding-round-to-scale-ai-attribution-tech/)
- [Musical AI funding — Digital Music News](https://www.digitalmusicnews.com/2026/01/13/musical-ai-funding-january-2026/)
- [Musical AI funding — Music Ally](https://musically.com/2026/01/14/musical-ai-raises-4-5m-funding-for-its-attribution-tech/)
- [Musical AI funding — AI Insider](https://theaiinsider.tech/2026/01/15/musical-ai-announces-4-5m-in-funding-to-scale-attribution-and-licensing-infrastructure-for-generative-ai/)
- [Musical AI/Beatoven — MBW](https://www.musicbusinessworldwide.com/musical-ai-and-beatoven-ai-to-jointly-launch-fully-licensed-ai-music-generator1/)
- [Musical AI — Record of the Day](https://www.recordoftheday.com/on-the-move/news-press/musical-ai-tames-the-chaos-and-ushers-in-a-sustainable-generative-ai-future)
- [Musical AI — CBInsights](https://www.cbinsights.com/company/sommsai)
- [MusicWorks Substack — Musical AI](https://musicworks.substack.com/p/striking-the-right-chord-how-musical)

---

## Sureel AI

### Company Profile

| Attribute | Details |
|-----------|---------|
| **HQ** | Palo Alto, CA |
| **Website** | [sureel.ai](https://www.sureel.ai/) |
| **Founded** | 2022 |
| **Employees** | ~10-15 (ZoomInfo) |
| **Accelerator** | Creative Destruction Lab (CDL) Montreal, 2023/24 AI cohort |
| **A2IM Member** | Yes |

### Leadership Team

| Role | Person | Background |
|------|--------|------------|
| **Founder & CEO** | Dr. Tamay Aykut | PhD in AI/Computer Vision/Robotics, TU Munich (2016-2019). Nokia Bell Labs Best Student Award. Youngest visiting assistant professor at Stanford via Max Planck Center since 2002. Previously developed tools deployed across 2,000+ BMW plants generating EUR 20M+ in savings. |
| **Co-President** | Benji Rogers | Serial music tech entrepreneur. PledgeMusic founder. Joined Sureel March 2024. Partner at Lark42. Known music rights advocate. |
| **Co-President** | Aileen Crowley | Pioneered DigSin (new-model record label). Established first global streaming team at Universal Music Group. Partner at Lark42. |

**Patent co-inventors**: Christopher Benjamin Kuhn, Diego Ponce De Leon Vera, Paul Pauls, Christoph Burgmair.

### Patent Portfolio

| Status | Count | Key Coverage |
|--------|-------|-------------|
| **Published** | 1 | Training-time attribution tracking |
| **Pending** | 4 | Compositional/recording separation, attribution vectors, output-to-creator correlation |

**Detailed patent coverage**:

1. **Training-time attribution tracking**: Process to track how individual pieces of data influence the neural network throughout the training process, including all weights, gradients, and loss values.

2. **Attribution vector computation**: Training artificial intelligence and determining attribution vectors for content creators, with provisions for providing compensation to creators based on their contributions.

3. **Output-to-creator correlation**: Music generated by AI, where output embeddings are created and correlated to content creators used to train the AI, with one or more creator attributions determined based on this correlation.

**Key innovation**: **Compositional vs. recording rights separation** — distinguishing between melodic/lyrical influences (publishing rights) and production/performance influences (master rights). This maps directly to the dual-rights structure of the music industry and is a genuine technical breakthrough.

Source: [Patents Assigned to Sureel Inc. — Justia](https://patents.justia.com/assignee/sureel-inc)

### Technical Architecture

#### Attribution Graph System

Sureel's technology creates **"attribution graphs"** that map relationships between songs, understanding both compositional elements and recording styles. The system computes an **"Attribution Likelihood"** metric that claims **86-90% accuracy at the works level**.

#### Two Integration Modes

**1. Decoupled Option (Lighter Integration)**:
- Requires: the dataset used to train/fine-tune the AI model
- Encodes data with the chosen AI model
- For inference: only the text prompt and generated output needed
- The Sureel Engine only needs input, intermediate output, and final output

**2. Integrated Option (Maximum Precision)**:
- Requires: all training data
- Requires: entire training history including all weights, gradients, and loss values
- Requires: output of all encoders and model components used for training
- Offers the most precise and detailed attribution

#### Product Capabilities

| Capability | Details |
|-----------|---------|
| **Audio attribution** | Core: map AI output to training inputs |
| **Lyric attribution** | Multi-language support |
| **AI audio detection** | Claims to outperform existing market solutions |
| **Track attribution** | Full track-level attribution |
| **Stem-wise attribution** | Individual instrument/component attribution |
| **Temporal attribution** | Analyzing influence changes across track segments |
| **AIBI** | AI Business Intelligence: maps prompts to outputs, provides model behavior insights |
| **Image attribution** | Multi-modal: extends beyond music |
| **Output controls** | Rights holders set rules for alteration/combination limits |

#### Monitoring & Reporting

Real-time monitoring with reporting by: time, date, location, platform, catalog, and creator.

### Partnerships & Traction

| Partner | Date | Type | Significance |
|---------|------|------|-------------|
| **STIM** | Sep 2025 | Attribution technology provider | World's first collective AI music licence. Sureel is preferred attribution provider for all STIM AI licensing deals. |
| **Songfox** | Sep 2025 | Licensee via STIM | Stockholm-based AI covers/composition startup. First licensee under STIM framework. |
| **BeatStars** | Apr 2025 | Marketplace protection | Entire marketplace catalog auto-opted-out of AI training. Monthly "Do Not Train" notices sent to AI companies worldwide. |
| **Triple 8 Management** | Apr 2025 | Artist management | First management company to proactively offer AI IP protection to its roster. |
| **OpenPlay** | Dec 2024 | API marketplace | AI detection and monetization services for OpenPlay's API Marketplace. |
| **Rostrum Pacific** | ~2024 | Catalog registration | Parent company of Rostrum Records. |

**Registered assets**: Nearing **10 million** across the partnership ecosystem. The BeatStars partnership likely accounts for a substantial portion.

### Business Model

**Attribution-as-a-Service (AaaS)**:

- **B2B API-driven** (`api.sureel.ai/documentation`)
- **Revenue model**: "Attribution Share" — allocates revenue directly from each transaction based on the influence of rights holder assets in AI outputs
- **Dual-sided platform**:
  - For creators: Register assets, opt in/out, set usage rules, monitor, receive compensation
  - For AI companies: Access licensed data, ethical sourcing, transparency
- **Registry model**: Timestamped ownership proof with formal "Do Not Train" notices

**Pricing**: Not publicly disclosed. A pricing page exists at `app.dev.sureel.ai/apis/pricing`.

### Key Quote

> "Attribution technology is the foundation that will allow the creative community to both protect their rights and benefit from AI innovation." — Benji Rogers, Co-President

> "Attribution is a cornerstone of a maturing, compliant AI music market." — Simon Gozzi, STIM

### Public Presentations & Content

- Stanford EE talk (Feb 2024): "The Battle for Creative Credit and Provenance in the Gen AI Era: Confronting the Attribution Crisis"
- [Benji Rogers Medium article](https://medium.com/@lovingyourwork/sureel-ai-make-anything-from-everything-43617fb06d2d) (July 2024)
- [MusicWorks Substack interview](https://musicworks.substack.com/p/bringing-responsible-and-explainable) — most detailed public technical description
- Blog posts on synthetic data risks and sustainable AI business models

### Comparison with Musical AI

| Dimension | Sureel AI | Musical AI |
|-----------|-----------|------------|
| **Founded** | 2022 | ~2023 (rebranded 2024) |
| **HQ** | Palo Alto, CA | Ottawa/Halifax, Canada |
| **Founders** | Dr. Tamay Aykut (AI/robotics PhD) | Sean Power, Matt Adell (ex-Beatport CEO) |
| **Funding** | Undisclosed (CDL accelerator) | $6M total |
| **Patents** | 1 published + 4 pending | Not prominently disclosed |
| **Key innovation** | Compositional vs recording separation; gradient tracking | Royalty sheets with % influence; one-stop rights holder focus |
| **Integration** | Decoupled (lighter) or Integrated (full) | Training-time only |
| **Revenue sharing** | Attribution Share per transaction | 30% of revenue (Beatoven deal) |
| **Key partnerships** | STIM, BeatStars, OpenPlay, Triple 8 | Beatoven.ai, Symphonic, SoundBreak, Kanjian |
| **Major label ties** | None (indie focus) | None |
| **Scope** | Multi-modal (audio, image, text, video) | Music-focused |
| **Claimed accuracy** | 86-90% at works level | Not publicly quantified |
| **Registered assets** | ~10M | Not disclosed |
| **Headcount** | ~10-15 | ~5 |

**Strategic difference**: Sureel positions as multi-modal attribution infrastructure (music, images, text) that plugs into any AI ecosystem. Musical AI is more narrowly focused as a music rights marketplace connecting rights holders with AI companies. Sureel's STIM partnership gives CMO-level access; Musical AI builds through distributor partnerships.

### Sources

- [Water & Music: How music AI attribution actually works](https://www.waterandmusic.com/music-ai-attribution/)
- [Digital Music News: STIM Taps Sureel AI](https://www.digitalmusicnews.com/2025/09/26/stim-taps-sureel-ai-attribution-tracking/)
- [A2IM Member Spotlight: Sureel](https://a2im.org/ams-sureel-ai/)
- [Justia Patents: Sureel Inc.](https://patents.justia.com/assignee/sureel-inc)
- [MusicWorks Substack](https://musicworks.substack.com/p/bringing-responsible-and-explainable)
- [Billboard: BeatStars/Sureel](https://www.billboard.com/pro/beatstars-ai-training-opt-outs-creators-sureel/)
- [MusicRow: Triple 8/Sureel](https://musicrow.com/2025/04/triple-8-management-to-offer-artists-ai-protection-through-sureel-partnership/)
- [Creative Destruction Lab: Sureel](https://creativedestructionlab.com/companies/sureel/)
- [Benji Rogers Medium](https://medium.com/@lovingyourwork/sureel-ai-make-anything-from-everything-43617fb06d2d)

---

## Vermillio

### Company Profile

| Attribute | Details |
|-----------|---------|
| **HQ** | Chicago, IL |
| **Website** | [vermill.io](https://vermill.io/) |
| **Founded** | ~2022 |
| **Funding** | $16M Series A (Mar 2025) |
| **Pricing** | $4,000/month + transaction fees |
| **Recognition** | TIME100 Most Influential Companies (2025) |

### Funding

$16M Series A co-led by **DNS Capital** and **Sony Music**. This was **Sony Music's first-ever AI investment**.

### Core Technology: TraceID

TraceID monitors online content for use of intellectual property, including name, image, and likeness. The platform can:
- Automatically send takedown requests
- Manage payments for licensed content
- Enable talent and IP holders to take advantage of generative AI with secure data control

### Clients

| Client | Type | Project |
|--------|------|---------|
| Sony Pictures | Film studio | Spider-Verse AI character generation |
| Sony Music | Record label | Investment + partnership |
| WME | Talent agency | IP protection |
| The Orb / David Gilmour | Artists | Fan remix project for "Metallic Spheres" album |

### Key Distinction

Vermillio is focused on **content protection and licensing enforcement** rather than training-time attribution. Their TraceID system is closer to a Content ID system with AI capabilities than an attribution engine.

### Sources

- [Axios: Sony backs Vermillio](https://www.axios.com/2025/03/03/vermillio-ai-rights-licensing-sony-music)
- [Billboard: Sony investment](https://www.billboard.com/pro/sony-music-ai-investment-vermillio-funding-round/)
- [BusinessWire announcement](https://www.businesswire.com/news/home/20250228026074/en/)
- [Digital Music News](https://www.digitalmusicnews.com/2025/03/03/vermillio-series-a/)

---

## ProRata.ai

### Company Profile

| Attribute | Details |
|-----------|---------|
| **Funding** | $75M+ total ($40M Series B) |
| **Key deal** | Universal Music Group partnership |
| **Scope** | Cross-media attribution (text, audio, visual) |
| **Publisher partnerships** | 500+ |
| **Product** | Gist.ai — AI search engine with 50/50 revenue sharing with content partners |
| **Revenue model** | Attribution-based revenue sharing for AI-generated content |

ProRata has the strongest financial backing among pure attribution companies. Their 500+ publisher partnerships and UMG deal suggest significant traction at scale. The Gist.ai search engine demonstrates a concrete product applying attribution to commercial search, not just music.

---

## Pex

Pex is a content identification and licensing platform that has published analysis on navigating AI music tools and copyright. They position adjacent to attribution with existing content ID infrastructure but are not yet a direct attribution competitor.

Source: [Pex Blog](https://pex.com/blog/navigating-ai-music-tools-and-copyright-an-overview-for-rightsholders/)

---

## Auracles

### Company Profile

| Attribute | Details |
|-----------|---------|
| **HQ** | London, UK |
| **Website** | [auracles.io](https://auracles.io/) |
| **Focus** | Sovereign identity and verifiable credentials for music |
| **Approach** | W3C DID + Verifiable Credentials for artist identity |

### Core Concept

Auracles positions as **identity infrastructure** for the music industry. Rather than attribution of AI-generated content, they focus on establishing verified creator identity using W3C Decentralized Identifiers (DIDs) and Verifiable Credentials. This maps to the A0-A3 assurance level framework: Auracles provides the identity verification layer (A1-A3) that attribution systems depend on.

### Relevance to Scaffold

- **Identity layer**: Provides verified creator identities that attribution systems reference
- **W3C standards**: DID and Verifiable Credentials are open standards, not proprietary
- **Composable**: Can be layered under Musical AI, Sureel, or any attribution engine
- **A0-A3 mapping**: Auracles addresses the identity verification gap in current attribution approaches

---

## SoundExchange AI Registry

### Overview

SoundExchange, the US digital performance rights organization, announced an **AI music registry** initiative for tracking how AI models use human-created recordings. The registry aims to:

1. Establish a centralized database of recordings used in AI training
2. Enable rights holders to track AI usage of their catalog
3. Provide transparency into AI model training data provenance

### Relevance to Scaffold

- **Recording rights focus**: Maps to `RightsTypeEnum.MASTER_RECORDING`
- **Registry integration**: Maps to `external_registry_integration` PRD decision
- **Industry standard**: As a statutory organization, SoundExchange carries regulatory weight

---

## Fairly Trained

### Overview

| Attribute | Details |
|-----------|---------|
| **Website** | [fairlytrained.org](https://www.fairlytrained.org/) |
| **Founded** | 2024 |
| **Founder** | Ed Newton-Rex (ex-Suno VP of Audio) |
| **Certification** | "Licensed Model" mark for AI trained on licensed data |

### Certification Model

Fairly Trained provides a **certification mark** ("Licensed Model") for AI companies that train exclusively on licensed or authorized data. Musical AI was among the first certified companies. The certification process involves:

1. Audit of training data provenance
2. Verification of licensing agreements
3. Ongoing compliance monitoring

### Relevance to Scaffold

- **Certification type**: Maps to `CertificationTypeEnum.FAIRLY_TRAINED_LICENSED`
- **Compliance attestation**: Maps to `ComplianceAttestation` schema
- **Trust signal**: Provides A2-level assurance for training data provenance
