# AI Music Generation Platforms — Detailed Profiles

> **Parent**: [README.md](README.md) > Tier 2: AI Music Generation Platforms
> **Updated**: 2026-02-10

---

## Suno

### Company Profile

| Attribute | Details |
|-----------|---------|
| **Valuation** | $2.45B (Nov 2025) |
| **Revenue** | $200M ARR |
| **Total funding** | $375M+ |
| **Latest round** | $250M Series C (Nov 2025, led by Menlo Ventures, NVentures) |
| **Previous round** | $125M Series B (May 2024, Lightspeed, Nat Friedman, Daniel Gross) |
| **Product** | Suno Studio — "generative audio workstation" |

### Legal Status

| Label | Status | Details |
|-------|--------|---------|
| **Warner Music Group** | Settled (Nov 2025) | Licensing deal. Licensed-only models in 2026; current models deprecated; users pay to download. |
| **Universal Music Group** | Ongoing lawsuit | PR battle over "walled gardens" in AI music |
| **Sony Music** | Ongoing | No settlement announced |

### 2026 Changes (per Warner deal)

- New advanced models trained on **only licensed works**
- Current unlicensed models **deprecated**
- Artists can **opt-in** to license works for Suno model training
- Users must **pay to download** tracks
- Suno keeps its core product model intact (unlike Udio's pivot)

### Suno Studio Features

Positions Suno as professional tool rather than consumer toy:
- Stems export (individual audio tracks)
- MIDI export
- Professional audio workstation interface
- Social/collaborative features planned

### Market Significance

Suno is the highest-funded and highest-revenue company in AI music generation. Their $200M ARR demonstrates genuine product-market fit for AI music creation tools. The transition to licensed models in 2026 is the most significant industry shift in this space.

### Sources

- [TechCrunch: $2.45B valuation](https://techcrunch.com/2025/11/19/legally-embattled-ai-music-startup-suno-raises-at-2-45b-valuation-on-200m-revenue/)
- [MBW: Warner deal](https://www.musicbusinessworldwide.com/warner-music-group-settles-with-suno-strikes-first-of-its-kind-deal-with-ai-song-generator/)
- [Digital Music News: 2026 changes](https://www.digitalmusicnews.com/2025/12/22/suno-warner-music-deal-changes/)

---

## Udio

### Legal Status

| Label | Status | Details |
|-------|--------|---------|
| **Universal Music Group** | Settled (Oct 2025) | Licensed AI music platform launching 2026 |
| **Warner Music Group** | Settled (Nov 2025) | Licensed AI music platform launching 2026 |
| **Sony Music** | Ongoing | Case active |

### The Pivot

Unlike Suno, Udio's deal **requires a fundamental product pivot**:

- **Before**: Generate new songs from text prompts
- **After**: "Walled garden" — licensed music remixing and fan engagement platform
- **Key constraint**: Creations cannot leave the platform
- **Transition measures**: Fingerprinting, filtering, and other safeguards during transition

The existing Udio product remains available during transition with additional guardrails.

### New Platform (2026)

- Powered by new generative AI trained on **authorized and licensed music**
- "Subscription service that transforms the user engagement experience"
- "Licensed and protected environment to customize, stream and share music responsibly"

### Significance for Attribution

Udio's pivot from open generation to walled-garden remixing is a direct result of the lack of robust attribution technology. If attribution were solved (precise per-song influence tracking), Udio could potentially maintain its open creation model with proper compensation. The pivot is an admission that the industry cannot yet solve attribution at the required precision.

### Sources

- [Hollywood Reporter: UMG settlement](https://www.hollywoodreporter.com/music/music-industry-news/universal-music-group-announces-settlement-with-udio-1236414023/)
- [TechCrunch: Warner settlement](https://techcrunch.com/2025/11/19/warner-music-settles-copyright-lawsuit-with-udio-signs-deal-for-ai-music-platform/)
- [Billboard: What deals mean](https://www.billboard.com/pro/what-suno-udio-licensing-deals-mean-future-ai-music/)

---

## Soundverse

### Company Profile

| Attribute | Details |
|-----------|---------|
| **HQ** | New York City (founded 2023); operations in Sweden, USA, India |
| **Website** | [soundverse.ai](https://www.soundverse.ai/) |
| **Founders** | Sourabh Pateriya (CEO), Riley Williams (CTO) |
| **Users** | 1.6M+ creators |
| **Songs generated** | 3M+ |
| **Competitive rank** | 33rd of 277 active competitors (Tracxn) |
| **Funding** | No confirmed public round disclosed |
| **V5 model** | Latest generation AI |
| **Patent status** | "Patent pending" in-house attribution technology |

### Products

**Generation tools**: Text-to-music, AI song/beat generation, AI singing voice, lyric generation

**Modification tools**: Stem separation, music extension, auto-loop, vocal splitting, voice swap, voice-to-instrument, inpainting, autocomplete

**Intelligence features**: Section analysis, BPM/key detection

### Attribution Stack: Soundverse Trace

The branded attribution stack consists of multiple technical components:
- **Influence Functions**: Measure per-training-input contribution to specific outputs
- **Dynamic Time Warping (DTW)**: Temporal alignment for comparing audio sequences
- **Embedding Analysis**: Vector-space similarity mapping between training and generated
- **Audio Watermarking**: Inaudible fingerprints embedded in exported audio
- **Deep Search**: High-precision scanning (1:1 and 1:N) detecting overlaps with existing catalogs

### Ethical AI Music Framework (Whitepaper, 50 pages, Jan 2026)

Published a comprehensive six-stage framework:

#### Stage 1: Model Creation
Partnership-based approach requiring artist consent. Replaces web scraping with voluntary contributions.

#### Stage 2: Application Layer — DNA Models
Artists can train private AI on their own music. "DNA Models" maintain data security while monetizing distinctive style. Artists control usage rights and earning structures without exposing training data.

#### Stage 3: Inference — Attribution Tracking
Uses **influence functions and embedding analysis** to transparently log which training tracks shaped generated music. Tracks token flow through the model during training.

#### Stage 4: Export — Provenance Embedding
Embeds provenance information directly into audio files via **digital signatures** containing licensing metadata.

#### Stage 5: External Audio — Similarity Scanning
Infrastructure scanning AI-generated music against existing catalogs to flag similarity and prevent infringement.

#### Stage 6: Compensation — Royalty Distribution
Ongoing royalty payments based on documented influence rather than flat fees. **5% minimum influence threshold** — below which micro-contributions aren't tracked due to practical and cost considerations.

### Pilot Results (April 2024, 50 creators)

| Finding | Implication |
|---------|------------|
| Real-time transparency dashboards essential | Build monitoring into core UX |
| Audio quality > volume | Focus on high-quality training data |
| Creators prefer recurring royalties over one-time payments | Build ongoing revenue model |
| Clear thresholds improve system functionality | 5% minimum influence is a practical choice |

### Content Partner Program

Opt-in licensing framework where rights-holders contribute audio for AI training in exchange for recurring royalties:
- **Influence-based payouts**: Creators earn per generation when their content influences outputs (not flat-rate)
- **Tiered licensing**: Musicians define level (Tier 1 for limited training to Tier 6 for full dataset participation)
- **Real-time dashboards**: Monitoring earnings and contribution influence
- **Transparency reports**: Documentation of how data contributes to outputs

Specific revenue-sharing percentages not publicly disclosed.

### Additional Programs

- "DNA Models" for artist-owned AI
- Affiliate program (soundverse.tolt.io)
- Partner page for collaboration opportunities

**Important caveats**: The whitepaper acknowledges some approaches "still need research." Pilot involved only 50 creators. The company is still exploring where in the model pipeline to implement attribution.

### Sources

- [Soundverse whitepaper](https://www.soundverse.ai/blog/article/soundverse-just-released-a-blueprint-for-fair-ai-music)
- [Soundverse attribution blog](https://www.soundverse.ai/blog/article/cracking-ai-attribution-in-music-and-how-soundverse-is-leading-the-charge)
- [Tracxn profile](https://tracxn.com/d/companies/soundverse/__hqre3VN2cp3YXyqGFnJuJ4M0Znnu59tioYQ5hCuMOH0)

---

## Boomy

| Attribute | Details |
|-----------|---------|
| **Founded** | 2019 |
| **Founders** | Alex Mitchell, Matthew Cohen Santorelli |
| **Songs created** | 14.5M+ (claimed "14% of world's total recorded music") |
| **Distribution** | 40+ streaming platforms (Spotify, Apple Music, YouTube) |
| **Certification** | Fairly Trained certified (product level) |

### Attribution Approach

Models are **not trained on copyrighted data** — uses copyright-safe generative approach based on proprietary algorithms. Users receive commercial rights to their songs (plan-dependent). This is the avoidance approach: no attribution needed because no copyrighted data used.

### Corporate API

Boomy Corporation offers B2B generative/AI API solutions at [boomycorporation.com](https://www.boomycorporation.com/).

---

## Klay Vision

| Attribute | Details |
|-----------|---------|
| **Significance** | **First AI music startup to license ALL THREE major labels** (UMG, Sony, Warner) + publishing arms |
| **Status** | Has not yet launched platform |
| **Product** | Streaming service allowing users to remake songs in different styles |
| **Model** | "Large music model" trained only on licensed music |

**Scope**: Planned to include all independent labels, artists, songwriters, and publishers. The most comprehensive licensing footprint of any AI music company.

**Positioning**: "Experiences will enhance, rather than replace, human creativity."

**History**: Announced Universal Music strategic collaboration October 2024; subsequently signed Sony and Warner.

**Significance for attribution**: If Klay Vision launches successfully with all-major-label licensing, it establishes the precedent for comprehensive licensing as a viable business model. The attribution question shifts from "did you train on this?" to "how much did each licensed track contribute?"

Source: [Variety](https://variety.com/2025/music/news/universal-warner-sony-strike-licensing-deals-ai-klay-1236586934/)

---

## Jen (Futureverse)

| Attribute | Details |
|-----------|---------|
| **Type** | Ethically-trained text-to-music AI |
| **Training** | 40 fully-licensed catalogs, verified against 150M songs |
| **Certification** | Fairly Trained (model-level) |
| **Founding partner** | Mike Caren (founder/CEO of Artist Partner Group, ex-major label) |

**Provenance innovation**: JENUINE indicator — cryptographic hash recorded on The Root Network blockchain verifying creation timestamp. This is a rare example of blockchain provenance in a commercially-oriented music AI product.

Source: [Billboard](https://www.billboard.com/pro/futureverse-jen-ai-music-model-launch/), [PR Newswire](https://www.prnewswire.com/news-releases/jen-launches-ethically-trained-ai-music-platform-for-text-to-music-generation-302177664.html)

---

## Wondera

| Attribute | Details |
|-----------|---------|
| **Type** | "World's first conversational AI platform for music creation" |
| **Data source** | SourceAudio (14M+ fully cleared tracks) |
| **User rights** | 100% ownership of created music; royalty-free for commercial use |
| **Features** | On-chain tools for royalty tracking |

Source: [PR Newswire](https://www.prnewswire.com/news-releases/wondera-partners-with-sourceaudio-to-license-industry-leading-ethical-music-dataset-for-ai-training-302491038.html)

---

## Other Generation Platforms

### Stability AI — Stable Audio

- **Stable Audio Open 1.0**: Trained on 486,492 recordings from Freesound and Free Music Archive (FMA), all CC0/CC BY/CC Sampling+ licensed; full attribution published
- **Community License**: Free commercial use under $1M revenue; requires "Powered by Stability AI" attribution
- Music-specific latent diffusion model; open-weight releases attract research community
- **Marketplace plans**: CEO Prem Akkaraju announced plans for artist licensing marketplace with fair compensation
- **Notable**: Ed Newton-Rex resigned as VP Audio (Nov 2023) over licensing stance, then founded Fairly Trained
- **Lawsuit** (Jan 2026): Musician sued for training despite explicit opt-out requests

### Google — MusicLM / MusicFX / Lyria

- **Lyria**: Google DeepMind's advanced music generation model
- **MusicFX**: Consumer-facing generation tool; 10M+ tracks generated
- **SynthID**: Imperceptible watermarks embedded in all Lyria/MusicFX audio; uses psychoacoustic principles (embedding in frequency ranges where human ears less sensitive); resistant to noise, MP3 compression, speed changes. **10+ billion pieces** watermarked across modalities
- **IPTC metadata**: Attribution metadata included with generated content
- **Prompt filtering**: Blocks prompts mentioning specific artists to prevent copyright issues
- **Music AI Incubator**: Industry collaboration with undisclosed partners
- **No per-artist attribution or revenue sharing** — provenance only ("was this AI-generated?"), not influence tracking

### Meta — MusicGen / AudioCraft

- **Training data**: ~400,000 recordings (20,000 hours) of Meta-owned or specifically licensed music
- **Code license**: MIT (open source)
- **Model weights**: CC-BY-NC 4.0 (non-commercial only) — not truly open source by OSI definition
- **Model cards**: Published for MusicGen and AudioGen detailing training data
- No attribution infrastructure, no revenue sharing, no watermarking
- Research contribution positioning; no commercial platform

### AIVA

- **SACEM recognition**: First AI to receive official **Composer status** from SACEM (French/Luxembourg rights society) — AIVA itself holds copyright and receives royalties
- **Tiered copyright**: Free plan (AIVA owns copyright, users credit AIVA); Standard (non-exclusive commercial for YouTube/Twitch/TikTok/Instagram); Pro (users own full copyright forever, no attribution required)
- **Technical models**: Lyra (transformer) and OmniCodec (neural codec) for instrumental music
- Classical and film score focus; no training-data attribution mechanism
- Different market segment from pop/commercial music

### Mubert

- See [06-web3-blockchain.md](06-web3-blockchain.md) for detailed profile
- Polkadot rollup for on-chain attribution
- 100M+ tracks generated
- Integrations with Canva, Restream

### Soundful

| Attribute | Details |
|-----------|---------|
| **HQ** | San Diego, CA |
| **Founded** | 2019 |
| **Funding** | $4.5M seed (Jan 2022) |
| **Team** | 11-50 employees |
| **Certification** | Fairly Trained certified |

**Unique training approach**: Recorded individual notes from live musicians and built AI models from scratch. Never trained on existing songs. Provides STEM files and MIDI in Pro plan. Models trained to be "emotionally resonant and stylistically coherent."

---

## Market-Level Attribution Status Summary

| Platform | Licensing Status | Attribution Tech | 2026 Plans |
|----------|-----------------|-----------------|------------|
| **Suno** | Warner deal; UMG/Sony ongoing | None public | Licensed-only models |
| **Udio** | UMG + Warner settled; Sony ongoing | Fingerprinting/filtering being added | Walled-garden pivot |
| **Klay Vision** | **All 3 majors + publishing** | Not disclosed | Streaming service for remaking songs |
| **Soundverse** | Licensed partnerships | Influence functions + embedding (whitepaper) | DNA Models |
| **Boomy** | Copyright-safe (no licensed data needed) | N/A (no copyrighted training data) | Continue current model |
| **Jen** | 40 licensed catalogs, verified vs 150M songs | Blockchain provenance (JENUINE hash) | Ethically-trained platform |
| **Wondera** | SourceAudio (14M+ cleared tracks) | On-chain royalty tracking | Conversational music creation |
| **Stability Audio** | Licensed from AudioSparx | None public | Unknown |
| **Google** | Unknown | None public | Cautious/limited release |
| **Meta** | Open-source release | None | Academic focus |
| **AIVA** | Licensed | None public | Classical/film niche |
| **Mubert** | On-chain licensing | Blockchain fingerprinting | Polkadot rollup |
