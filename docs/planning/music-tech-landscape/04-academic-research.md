# Academic Research Landscape — Music AI Attribution

> **Parent**: [README.md](README.md) > Academic Research Landscape
> **Updated**: 2026-02-10

---

## Core Papers on Training Data Attribution (TDA)

### 1. Large-Scale Training Data Attribution for Music Generative Models via Unlearning

| Attribute | Details |
|-----------|---------|
| **Authors** | Woosung Choi, Junghyun Koo, Kin Wai Cheuk, Joan Serrà, Marco A. Martínez-Ramírez, Yukara Ikemiya, Naoki Murata, Yuhta Takida, Wei-Hsiang Liao, Yuki Mitsufuji |
| **Affiliation** | Sony AI / Sony Group |
| **arXiv** | [2506.18312](https://arxiv.org/abs/2506.18312) |
| **Venue** | NeurIPS 2025 Creative AI Track |
| **Year** | 2025 |

**Problem**: Identify which specific training data points contributed most to a particular AI-generated music output.

**Method**: Adapts unlearning-based attribution techniques to text-to-music diffusion models trained on large-scale datasets. Conducts grid searches over hyperparameter configurations and quantitatively evaluates unlearning consistency.

**Key contribution**: First large-scale TDA applied to the music generation domain. Compares attribution patterns from unlearning against non-counterfactual baselines.

**Relevance to scaffold**: This is the most rigorous academic work on music-specific TDA. The unlearning approach is computationally expensive (requiring retraining with data removed) but provides the strongest theoretical guarantees. Our scaffold doesn't need to implement this — it's what partners like Sureel/Musical AI should build — but we should understand the confidence bounds it provides.

---

### 2. Attribution-by-Design: Ensuring Inference-Time Provenance in Generative Music Systems

| Attribute | Details |
|-----------|---------|
| **Authors** | Fabio Morreale, Wiebke Hutiri, Joan Serrà, Alice Xiang, Yuki Mitsufuji |
| **arXiv** | [2510.08062](https://arxiv.org/abs/2510.08062) |
| **Year** | 2025 |

**Core argument**: Rather than retroactively estimating training data contributions (post-hoc TDA), attribution and compensation should be **embedded into the generative system's architecture**. This enables conditioning generation on specific songs with "transparent information about attribution and permitted usage."

**Key distinction**: Training-time attribution vs. inference-time attribution:
- **Training-time**: Identify source materials used during model development (Sony paper above)
- **Inference-time**: Enable "direct, verifiable compensation whenever an artist's catalogue is used to condition a generated output"

**Criticism of existing approaches**: "Current approaches lack scalability and technical rigour, while current data attribution mechanisms provide only uncertain estimates and are rarely implemented in practice."

**Relevance to scaffold**: This paper's philosophy aligns closely with our A0-A3 assurance model. Higher assurance levels (A2-A3) correspond to systems where attribution is by-design rather than post-hoc. Our MCP permission server is essentially an inference-time provenance mechanism.

---

### 3. Exploring Musical Roots: Applying Audio Embeddings to Empower Influence Attribution for a Generative Music Model

| Attribute | Details |
|-----------|---------|
| **Authors** | Julia Barnett, Hugo Flores Garcia, Bryan Pardo |
| **Affiliation** | Northwestern University |
| **arXiv** | [2401.14542](https://arxiv.org/abs/2401.14542) |
| **Year** | 2024 |

**Method**: Evaluated two audio embedding techniques — **CLMR** and **CLAP** — to measure musical similarity across approximately **5 million audio clips** used in VampNet (an open-source generative music model).

**Key contributions**:
1. Systematic, replicable approach for finding similar musical pieces that reveals training data attribution
2. Human validation via listening studies to ensure practical effectiveness
3. Robustness testing: pitch shifting, time stretching, and noise affect embedding similarity differently
4. Enables transition from "ignorant appropriation to informed creation"

**Relevance to scaffold**: Embedding-based similarity is a practical, scalable approach for our entity resolution component. We can use CLAP embeddings as one input to our confidence scoring system. This is correlation-based (not causation), but achieves A1-A2 assurance levels.

---

### 4. Watermarking Training Data of Music Generation Models

| Attribute | Details |
|-----------|---------|
| **Authors** | Pascal Epple, Igor Shilov, Bozhidar Stevanoski, Yves-Alexandre de Montjoye |
| **arXiv** | [2412.08549](https://arxiv.org/abs/2412.08549) |
| **Year** | 2024 |

**Key finding**: Audio watermarks that are **imperceptible to humans** can lead to **noticeable shifts in the model's outputs**. This means watermarking can be used to detect unauthorized use of content in training.

**Factors examined**: Watermarking technique, proportion of watermarked samples in training data, robustness against the model's tokenizer processing.

**Robustness**: Evaluates resistance of state-of-the-art watermarking to removal techniques.

**Relevance to scaffold**: Watermarking could be integrated as an A0→A1 assurance upgrade: if an audio track contains a verified watermark, its provenance is automatically elevated. However, watermarking is pre-emptive (must be applied before distribution), so it doesn't help with existing catalogs.

---

### 5. Towards Assessing Data Replication in Music Generation with Music Similarity Metrics on Raw Audio (MiRA)

| Attribute | Details |
|-----------|---------|
| **Authors** | Roser Batlle-Roca, Wei-Hsiang Liao, Xavier Serra, Yuki Mitsufuji, Emilia Gómez |
| **Venue** | ISMIR 2024 |
| **arXiv** | [2407.14364](https://arxiv.org/abs/2407.14364) |
| **Year** | 2024 |

**Contribution**: Music Replication Assessment (MiRA) tool — a model-independent open evaluation method using diverse audio music similarity metrics. Successfully detects exact data replication at rates **exceeding 10%**.

**Open source**: Code and examples publicly available.

**Relevance to scaffold**: MiRA could be used as a component in our confidence scoring pipeline — detecting whether an AI-generated output is significantly similar to any training data we have indexed. This is a detection tool, not an attribution tool, but detection is a prerequisite for attribution.

---

### 6. AudioGenX: Explainability on Text-to-Audio Generative Models

| Attribute | Details |
|-----------|---------|
| **Authors** | Hyunju Kang, Geonhee Han, Yoonjae Jeong, Hogun Park |
| **Venue** | AAAI 2025 |
| **arXiv** | [2502.00459](https://arxiv.org/abs/2502.00459) |
| **Year** | 2025 |

**Contribution**: XAI technique for text-to-audio models. Optimizes an Explainer component using factual and counterfactual objective functions. Provides token-level explanations: which input tokens were most important for the generated audio.

**Relevance to scaffold**: Potentially useful for explaining attribution decisions to non-experts — "your song influenced this AI output because of these specific characteristics."

---

### 7. AI-Generated Music Detection and its Challenges

| Attribute | Details |
|-----------|---------|
| **Authors** | Darius Afchar, Gabriel Meseguer-Brocal, Romain Hennequin |
| **Venue** | IEEE ICASSP 2025 |
| **arXiv** | [2501.10111](https://arxiv.org/abs/2501.10111) |
| **Year** | 2025 |

**Key findings**:
- 99.8% detection accuracy in controlled settings
- **But**: Vulnerable to audio manipulation (time-stretching, pitch-shifting)
- **But**: Poor generalization to unseen generative models
- "High test accuracy does not guarantee practical effectiveness"

**Relevance to scaffold**: Detection is necessary but insufficient for attribution. Our system should flag AI-generated content but not rely solely on detection for assurance level assignment.

---

### 8. Diffusion Attribution Score (DAS)

| Attribute | Details |
|-----------|---------|
| **Authors** | Jinxu Lin, Linwei Tao, Minjing Dong, Chang Xu |
| **arXiv** | [2410.18639](https://arxiv.org/abs/2410.18639) |
| **Year** | 2024 (revised Mar 2025) |

**Contribution**: New attribution metric for diffusion models. Directly compares predicted distributions rather than relying on diffusion loss. State-of-the-art on linear data-modelling benchmarks. Code available on GitHub.

**Relevance to scaffold**: If we ever need to provide attribution confidence for diffusion-based music generators, DAS provides a theoretically grounded metric.

---

### 9. SSIMuse: Structural Similarity for Symbolic Music Replication

| Attribute | Details |
|-----------|---------|
| **Authors** | Shulei Ji, Zihao Wang, Le Ma, Jiaxing Yu, Kejun Zhang |
| **arXiv** | [2509.13658](https://arxiv.org/abs/2509.13658) |
| **Year** | 2025 |

**Contribution**: Adapts SSIM (image similarity metric) to symbolic music (piano roll representation). Two variants: SSIMuse-B (compositional structure) and SSIMuse-V (dynamic performance). Bar-level precision for replication detection.

**Open source**: Implementation available.

---

### 10. Generative AI Training and Copyright Law

| Attribute | Details |
|-----------|---------|
| **Authors** | Tim W. Dornis, Sebastian Stober |
| **Venue** | Transactions of ISMIR (TISMIR) |
| **arXiv** | [2502.15858](https://arxiv.org/abs/2502.15858) |
| **Year** | 2025 |

**Core argument**: AI training fundamentally differs from Text and Data Mining (TDM). Creates derivative works rather than extracting knowledge. Memorization creates independent copyright issues beyond "fair use" and TDM exceptions.

**Key quote**: Models "undeniably contain some internal representation for parts of their training data, though this representation is not directly accessible like in a file storage or a database."

**Relevance to scaffold**: Legal foundation for why attribution matters. Our A0-A3 levels operationalize the legal concepts discussed here — from "unknown provenance" (A0) to "identity-verified" (A3).

---

### 11. Computational Copyright: Generative Content ID

| Attribute | Details |
|-----------|---------|
| **Authors** | Junwei Deng, Xiangyu Jiang, Shiyao Zhang, Siwei Zhang, Himabindu Lakkaraju, Ruoxi Gao, Chris Donahue, Jiaqi W. Ma |
| **arXiv** | [2312.06646](https://arxiv.org/abs/2312.06646) (v5, Dec 2025) |
| **Year** | 2023 (revised 2025) |

**Contribution**: Proposes "Generative Content ID" — inspired by YouTube's Content ID but adapted for generative AI. Uses TDA methods to approximate which training samples influenced a specific generated output. Key insight: perceived similarity (the legal standard) fails to capture the broader data contribution that drives model utility — a song sounding nothing like the output may still have been essential training data.

**Practical finding**: Efficient attribution methods (influence function approximations) provide reliable proxies for computationally expensive leave-one-out retraining.

**Relevance to scaffold**: This is the foundational "computational copyright" concept. Proposes operational principles for sustainable governance: systematic measurement, proportional compensation, scalable royalty distribution.

---

### 12. Influence Functions for Scalable Data Attribution in Diffusion Models

| Attribute | Details |
|-----------|---------|
| **Authors** | Bruno Mlodozeniec, Runa Eschenhagen, Juhan Bae, Alexander Immer, David Krueger, Richard Turner |
| **arXiv** | [2410.13850](https://arxiv.org/abs/2410.13850) (v5, May 2025) |
| **Year** | 2024 (revised 2025) |

**Contribution**: Develops influence functions framework specifically for diffusion models. Introduces K-FAC (Kronecker-Factored Approximate Curvature) approximations tailored to diffusion's generalised Gauss-Newton matrices. Unifies prior attribution methods as special cases. Outperforms existing methods on Linear Data-modelling Score benchmark without hyperparameter tuning.

**Relevance to scaffold**: While developed for image diffusion, directly applicable to music diffusion models. This is the methodological building block that makes white-box TDA practical at scale.

---

### 13. SoK: Audio Watermarking Robustness

| Attribute | Details |
|-----------|---------|
| **Authors** | Yizhi Wen, Anusha Innuganti, Adriana Bozic Ramos, Hang Guo, Qben Yan |
| **arXiv** | [2503.19176](https://arxiv.org/abs/2503.19176) |
| **Year** | 2025 |

**Critical finding**: Comprehensive evaluation of 22 audio watermarking schemes against 22 removal attack types across 109 configurations. **None of the surveyed schemes can withstand all tested distortions.** Identifies 8 previously unknown highly effective attacks.

**Relevance to scaffold**: Casts serious doubt on watermarking as a sole attribution mechanism. Supports our multi-layered A0-A3 approach rather than reliance on any single technique.

---

### 14. Towards Responsible AI Music

| Attribute | Details |
|-----------|---------|
| **Authors** | Jacopo de Berardinis, Lorenzo Porcaro, Albert Merono-Penuela, Angelo Cangelosi, Timothy Buckley |
| **arXiv** | [2503.18814](https://arxiv.org/abs/2503.18814) |
| **Year** | 2025 |

**Contribution**: Applies the European Commission's Ethics Guidelines for Trustworthy AI (7 macro requirements) to generative music systems. Identifies gaps in transparency, explainability, and fairness. Provides roadmap for operationalizing responsible design.

---

## Watermarking Systems Reference

| System | Developer | Type | Capacity | Status |
|--------|-----------|------|----------|--------|
| **AudioSeal** | Meta/FAIR | Localized, zero-bit | Binary detection | Open-source ([GitHub](https://github.com/facebookresearch/audioseal)) |
| **WavMark** | Academic | Spread-spectrum | Multi-bit strings | Open-source |
| **SilentCipher** | Academic | Deep watermarking | Multi-bit strings | Interspeech 2024 |
| **SynthID Audio** | Google DeepMind | Spectrogram-embedded | Binary detection | Integrated in Lyria/NotebookLM; not yet public |
| **Digimarc** | Digimarc Corp | Next-gen commercial | Multi-bit | Announced July 2025 |

---

## Provenance Standards

| Standard | Scope | Status |
|----------|-------|--------|
| **C2PA** (Coalition for Content Provenance and Authenticity) | Open content provenance standard (v2.2, May 2025) | Fast-tracked as ISO standard; supported by Adobe, Arm, Intel, Microsoft, Truepic; primarily images/video but extensible to audio |
| **ISRC/ISWC/ISNI** | Music metadata identifiers | Foundation layer for A0-A3 assurance levels |
| **EU AI Act Article 50** | Labeling AI-generated content | Creates regulatory demand for attribution infrastructure |

---

## Supplemental Academic Resources

### Surveys & Overviews

| Paper | Source | Focus |
|-------|--------|-------|
| "Training data influence analysis and estimation: a survey" | [Springer 2023](https://link.springer.com/article/10.1007/s10994-023-06495-7) | Comprehensive survey of TDA methods |
| "Tracing Model Outputs to Training Data" | [Anthropic Research](https://www.anthropic.com/research/influence-functions) | Influence functions applied to LLMs |
| "Is There A Coherent Theory of Attributing AI Training Data?" | [Michael Weinberg](https://michaelweinberg.org/blog/2024/07/15/ai-attribution-what-does-it-mean/) | Conceptual analysis |
| "Mapping the Potential of Data Dividends" | [arXiv:1912.00757](https://arxiv.org/abs/1912.00757) | Economic framework for sharing AI profits |

### Music-Specific Detection & Analysis

| Paper | Source | Focus |
|-------|--------|-------|
| "MusicLIME: Explainable Multimodal Music" | [Semantic Scholar](https://www.semanticscholar.org/paper/MusicLIME) | XAI for music understanding |
| "XAttnMark: Cross-Attention Audio Watermarking" | [arXiv:2502.04230](https://arxiv.org/abs/2502.04230) | Robust audio watermarking |
| "Digital Fingerprinting on Multimedia" | [arXiv:2408.14155](https://arxiv.org/html/2408.14155v1) | Survey of fingerprinting approaches |
| "Segment Transformer: AI Music Detection via Structure" | [arXiv:2509.08283](https://arxiv.org/html/2509.08283v1) | Structural analysis for detection |
| "From Audio Deepfake Detection to AI Music Detection" | [arXiv:2412.00571](https://arxiv.org/html/2412.00571v1) | Pathway overview |

### Key Videos

| Title | Source |
|-------|--------|
| "Studying LLM Generalization with Influence Functions" | [YouTube](https://www.youtube.com/watch?v=Q1h4NvveTZA) |

---

## Attribution Method Taxonomy

The full literature reveals seven distinct attribution approaches, each with different trade-offs:

| Approach | Type | Model Access | Scalability | What It Measures |
|----------|------|-------------|-------------|-----------------|
| **Unlearning-based TDA** | Counterfactual, white-box | Full (weights + training data) | Moderate (improving) | Causal contribution of training data |
| **Influence functions** | Counterfactual, white-box | Full (weights + gradients) | Moderate (K-FAC helps) | Approximate causal contribution |
| **Embedding similarity** | Corroborative, black-box | None (model-agnostic) | High | Perceptual similarity (not causation) |
| **Watermarking** | Proactive, embedded | Training-time access | High | Binary presence of marked data |
| **Token flow tracking** | Mechanistic, white-box | Full (inference-time) | Low (real-time per generation) | Activation patterns during generation |
| **Replication detection** (MiRA/SSIMuse) | Forensic, black-box | None (model-agnostic) | High | Exact or near-exact memorization |
| **Inference-time conditioning** | By-design | Full (architecture control) | High | Direct causal link (conditioning input) |

This taxonomy maps to our assurance levels: A0 (no attribution) → A1 (single method) → A2 (multiple corroborating methods) → A3 (identity-verified + multi-method + cryptographic provenance).

---

## Two Paradigms of Attribution

The academic literature reveals two fundamentally different approaches:

### Paradigm 1: Post-hoc TDA (Sony, Lin et al.)

**Philosophy**: After a model is trained, determine which training samples were most influential.

**Methods**: Unlearning (retrain without specific data), influence functions (compute gradient-based influence scores), DAS (compare predicted distributions).

**Pros**: Works on existing models; theoretically grounded; doesn't require architecture changes.

**Cons**: Computationally expensive (often requires retraining); requires model access; provides estimates, not guarantees; doesn't scale to real-time.

### Paradigm 2: Attribution-by-Design (Morreale et al.)

**Philosophy**: Build provenance into the system architecture so attribution is automatic and verifiable.

**Methods**: Inference-time conditioning on specific catalogs; embedded provenance metadata; digital signatures.

**Pros**: Scalable; real-time; doesn't require post-hoc analysis; provides direct compensation mechanism.

**Cons**: Requires adoption during system design; doesn't work for existing models; may not capture indirect influences.

### Our Scaffold's Position

Our A0-A3 assurance levels bridge these paradigms:

| Level | Paradigm | How |
|-------|----------|-----|
| **A0** (Unknown) | Neither | No provenance information |
| **A1** (Self-Declared) | By-design | Artist declares their own credits |
| **A2** (Source-Verified) | Hybrid | Cross-referenced against databases (post-hoc for existing data, by-design for new entries) |
| **A3** (Identity-Verified) | By-design | Full verification chain embedded from creation |

We don't require training-time access (unlike Sureel/Musical AI) but we incentivize higher-quality attribution through transparent assurance ratings.
