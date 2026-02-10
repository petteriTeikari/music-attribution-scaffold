# Music Attribution in the Generative AI Era: A Research Synthesis

**Date**: 2026-02-03
**Purpose**: Actionable research insights for the system product development
**Sources**: 200+ papers from [sci-llm-writer/biblio/biblio-music](../../../sci-llm-writer/biblio/biblio-music)

---

## Executive Summary

This synthesis extracts actionable product insights from 200+ academic papers on music attribution, AI governance, and creator economics. The core finding: **technical detection approaches have fundamental limits (the Oracle Problem), but market-based attribution infrastructure can still create value through costly signaling, not perfect verification.**

### Key Takeaways for the system

| Research Finding | Product Implication |
|------------------|---------------------|
| Watermarks fail under neural compression | Don't rely on embedded watermarks for attribution |
| Similarity ≠ causality | Confidence scores must distinguish corroboration from verification |
| Machine unlearning causes catastrophic forgetting | Opt-out cannot be "undone" post-training; focus on consent infrastructure |
| Artists accept AI tools, reject AI substitution | Position chat interface as collaborative gap-filling, not automation |
| 80%+ of training data has undocumented restrictions | Data provenance tracking is a competitive moat |

---

## 1. The Oracle Problem: Fundamental Attribution Limits

### 1.1 What Cannot Be Proven

The "Oracle Problem" (Teikari, 2026; Caldarelli, 2025) identifies three epistemic barriers:

1. **Training Verification**: Cannot prove a model trained *only* on consented data
2. **Influence Attribution**: Cannot prove output resemblance is causal vs coincidental
3. **Absence Verification**: Cannot prove a model did *not* learn from a specific work

> "There can be no certainty that a specific training data has actually been used for a specific generation." — (Morreale et al., 2025)

**Cross-reference**: [attribution-by-design-ensuring-inference-time-provenance-in-generative-music-systems.md](../../../sci-llm-writer/biblio/biblio-music/attribution-by-design-ensuring-inference-time-provenance-in-generative-music-systems.md)

### 1.2 Why Watermarking Fails

The RAW-Bench study (Özer et al., 2025) demonstrates:

- Neural codecs (Encodec, Descript Audio Codec) defeat all tested watermarks
- Even distortion-aware training cannot guarantee robustness
- Specific attacks (polarity inversion, time stretching) break individual schemes

| Attack Type | Watermark Survival Rate |
|-------------|------------------------|
| MP3 Compression | 60-80% |
| Neural Codec | **<20%** |
| Polarity Inversion | **0%** (some algorithms) |
| Room Reverb | Variable |

**Cross-reference**: [audio-watermarking-neural-codecs-benchmark-2505.19663.md](../../../sci-llm-writer/biblio/biblio-music/audio-watermarking-neural-codecs-benchmark-2505.19663.md)

### 1.3 Product Insight: Shift from Detection to Declaration

**Don't build**: Post-hoc watermark detection systems
**Do build**: Pre-hoc declaration infrastructure (A0-A3 framework)

The system should position confidence scores as "evidence strength for compliant participants, not adversarial conditions."

---

## 2. Data Provenance Crisis

### 2.1 The Scale of Undocumented Restrictions

The Data Provenance Initiative audit (Longpre et al., 2024) of ~4000 datasets reveals:

- **<33%** of datasets are restrictively licensed
- **>80%** of source content carries undocumented restrictions
- **55%** have licenses inconsistent with source restrictions
- African music: ~1.8% of training data despite 17% of population

**Cross-reference**: [bridging-data-provenance-gap-multimodal-2412.17847.md](../../../sci-llm-writer/biblio/biblio-music/key/bridging-data-provenance-gap-multimodal-2412.17847.md)

### 2.2 Four-Level Data Protection Taxonomy

Li et al. (2025) propose a protection hierarchy:

| Level | Protection | Trade-off |
|-------|------------|-----------|
| **L1: Non-usability** | Data cannot be used at all | Maximum protection, zero utility |
| **L2: Privacy-preservation** | Sensitive attributes protected | High protection, some utility |
| **L3: Traceability** | Origin/usage can be tracked | Moderate protection, full utility |
| **L4: Deletability** | Influence can be removed post-hoc | Minimal upfront protection |

**Cross-reference**: [rethinking-data-protection-in-the-generative-artificial-intelligence-era.md](../../../sci-llm-writer/biblio/biblio-music/key/rethinking-data-protection-in-the-generative-artificial-intelligence-era.md)

### 2.3 Product Insight: L3 is the System's Sweet Spot

The system should operate at **L3 (Traceability)** with optional **L4 (Deletability)** claims:

- Full data utility for attribution queries
- Transparent provenance tracking
- Machine-readable permissions for AI training consent

---

## 3. Artist Perspectives on AI

### 3.1 The Tool vs. Substitution Divide

Interview studies (Kawakami & Venkatagiri, 2024; Herington et al., 2025) reveal:

**Artists accept AI when:**
- Used as co-composition tool (melodies, harmonies, basslines)
- Used for sound design (samples, loops, synthetic vocals)
- Used for lyrics generation assistance
- Used for translation to reach new audiences

**Artists reject AI when:**
- Replaces human creative decisions
- Trained on their work without consent
- Outputs presented as equivalent to human work

**Cross-reference**: [impact-generative-ai-on-artists.md](../../../sci-llm-writer/biblio/biblio-music/key/impact-generative-ai-on-artists.md)

### 3.2 The Slop Problem

Madsen & Puyt (2025) identify "slop" — the flood of derivative AI content:

> "Creativity thrives on scarcity; slop thrives on glut."

This creates market opportunity: **verified human provenance becomes a differentiator when AI content floods the market.**

**Cross-reference**: [when-ai-turns-culture-into-slop-ai-society.md](../../../sci-llm-writer/biblio/biblio-music/key/when-ai-turns-culture-into-slop-ai-society.md)

### 3.3 Product Insight: Chat Interface as Gap-Filling Partner

Position the system chat interface as:
- "Help me remember who played drums on this 1998 session"
- "Confirm the credits I already know"
- Not: "Let me fill in your data automatically"

---

## 4. Attribution-by-Design Framework

### 4.1 Training-Time vs Inference-Time Attribution

Sony AI's framework (Morreale et al., 2025) distinguishes:

| Attribution Type | Definition | Tractability |
|-----------------|------------|--------------|
| **Training-Time (TTA)** | How much model learned from specific data | Intractable |
| **Inference-Time (ITA)** | How much output was conditioned on specific reference | **Tractable** |

### 4.2 The Inference Set Concept

Key innovation: Separate *training dataset* from *inference dataset*:

- **Training dataset**: What the model learned from (opaque)
- **Inference dataset**: What conditions a specific generation (transparent)

Attribution-by-design means: provenance is enforced at generation time, not reconstructed post-hoc.

**Cross-reference**: [attribution-by-design-ensuring-inference-time-provenance-in-generative-music-systems.md](../../../sci-llm-writer/biblio/biblio-music/attribution-by-design-ensuring-inference-time-provenance-in-generative-music-systems.md)

### 4.3 Product Insight: MCP as Inference-Time Attribution Layer

the attribution MCP server should enable:

1. **User selects reference songs** → Attribution is by-design
2. **Permission check** → Consent verification before generation
3. **Compensation trigger** → Royalty distribution on generation

This sidesteps the Oracle Problem entirely.

---

## 5. Machine Unlearning Limitations

### 5.1 Why "Opt-Out" Post-Training Fails

Two studies (Kim et al., 2025; Choi et al., 2025) demonstrate:

| Unlearning Method | Forget Set Impact | Retain Set Impact |
|-------------------|-------------------|-------------------|
| Gradient Ascent | Partial degradation | **Severe degradation** |
| Random Labeling | Partial degradation | **Severe degradation** |
| Leave-One-Out | Perfect removal | Computationally infeasible |

> "Existing machine unlearning methods cannot selectively erase pre-trained musical knowledge without harming model performance." — (Kim et al., 2025)

**Cross-reference**:
- [no-encore-unlearning-as-opt-out-in-music-generation.md](../../../sci-llm-writer/biblio/biblio-music/key/no-encore-unlearning-as-opt-out-in-music-generation.md)
- [large-scale-training-data-attribution-for-music-generative-models-via-unlearning.md](../../../sci-llm-writer/biblio/biblio-music/key/large-scale-training-data-attribution-for-music-generative-models-via-unlearning.md)

### 5.2 Product Insight: Consent Before Training, Not After

The system's permission system must operate *before* training:

- **A0**: Unknown (no consent recorded)
- **A1**: Claimed (artist declares intent)
- **A2**: Corroborated (third-party confirms)
- **A3**: Verified (multi-source agreement)

"Right to be forgotten" compliance requires preventing ingestion, not unlearning.

---

## 6. Deterrence Economics

### 6.1 The Compliance Formula

From inspection game theory (Becker, 1968; Avenhaus, 2002):

```
p × d × F ≥ g
```

Where:
- `p` = audit probability
- `d` = detection probability
- `F` = expected penalty
- `g` = gain from cheating

Even with low detection probability, sufficiently high penalties create compliance incentives.

### 6.2 HADOPI Evidence

French "three strikes" law increased music sales 22-25% through **awareness of monitoring**, not actual enforcement (Danaher, 2014).

### 6.3 Product Insight: Credible Audit Infrastructure

the attribution MCP audit logging creates deterrence value:

1. Log all attribution queries
2. Enable artist-owned audit agents
3. Integrate with legal frameworks

The threat of detection → compliance incentive, even without perfect detection.

---

## 7. Market Failure Analysis

### 7.1 Three Market Failures in Generative Music

| Failure | Description | System Response |
|---------|-------------|-------------------|
| **Incomplete Property Rights** | "Style" isn't copyrightable | Create tradable permission bundles |
| **Information Asymmetry** | Artists don't know if they're in training sets | Transparent provenance tracking |
| **Market Power** | Major labels negotiate, independents don't | MCP enables direct artist-platform negotiation |

### 7.2 The Signaling Collapse Problem

Madsen & Puyt (2025) formalize:

> "When generation costs approach zero, information congestion prevents high-quality human creations from distinguishing themselves."

**Solution**: Attribution infrastructure as **costly signal** — verified human provenance becomes market differentiator.

---

## 8. Actionable Research Agenda for the system

### 8.1 Priority 1: Inference-Time Provenance

| Task | Research Basis | Implementation |
|------|----------------|----------------|
| Build inference set registry | Morreale et al. (2025) | MCP `check_permissions` tool |
| User-selected reference tracking | Attribution-by-design | Chat interface integration |
| Real-time consent verification | Sony AI framework | Permission patchbay |

### 8.2 Priority 2: Multi-Source Aggregation Confidence

| Task | Research Basis | Implementation |
|------|----------------|----------------|
| Calibrate confidence scores | ECE validation (Teikari, 2026) | 100+ manual validation set |
| Distinguish correlation from causation | Morreale et al. (2025) | Explicit level labels |
| Authority-weighted agreement | Multi-source fusion literature | AUTHORITY_WEIGHTS config |

### 8.3 Priority 3: Permission Infrastructure

| Task | Research Basis | Implementation |
|------|----------------|----------------|
| Granular consent mechanisms | Li et al. (2025) L3 framework | Permission bundles |
| Pre-training consent | Unlearning limitations | A0-A3 before training |
| Audit trail for deterrence | HADOPI evidence | MCP logging |

---

## 9. PRD Update Recommendations

Based on this research synthesis, the following PRD updates are recommended:

### 9.1 Attribution Engine PRD

**Add**:
- Explicit disclaimer when ECE > 0.15 ("uncalibrated confidence scores")
- Corroborative vs. verified label distinction
- Training-time vs. inference-time attribution separation

### 9.2 MCP Server PRD

**Add**:
- Inference-time attribution protocol
- Artist-owned audit agent support
- Deterrence-based compliance framework

### 9.3 Chat Interface PRD

**Add**:
- Gap-filling positioning (not automation)
- Memory aids for heritage artists
- "Tool not substitution" messaging

---

## 10. Key Citations

### Primary Sources

1. **Morreale, F., et al.** (2025). Attribution-by-design: Ensuring Inference-Time Provenance in Generative Music Systems. *arXiv:2510.08062*.

2. **Longpre, S., et al.** (2024). Bridging the Data Provenance Gap Across Text, Speech, and Video. *Data Provenance Initiative*.

3. **Kim, J., et al.** (2025). No Encore: Unlearning as Opt-Out in Music Generation. *arXiv:2509.06277*.

4. **Choi, W., et al.** (2025). Large-Scale Training Data Attribution for Music Generative Models via Unlearning. *arXiv:2506.18312*.

5. **Li, Y., et al.** (2025). Rethinking Data Protection in the (Generative) Artificial Intelligence Era. *arXiv:2507.03034*.

6. **Özer, Y., et al.** (2025). RAW-Bench: A Comprehensive Real-World Assessment of Audio Watermarking Algorithms. *arXiv:2505.19663*.

7. **Kawakami, R. & Venkatagiri, S.** (2024). The Impact of Generative AI on Artists. *C&C '24*.

8. **Madsen, D.Ø. & Puyt, R.W.** (2025). When AI turns culture into slop. *AI & Society*.

### Theoretical Framework

9. **Teikari, P.** (2026). Governing Generative Music: Attribution Limits, Platform Incentives, and the Future of Creator Income. *Journal of Cultural Economics* (in review).

10. **Becker, G.S.** (1968). Crime and Punishment: An Economic Approach. *Journal of Political Economy*.

11. **Danaher, B., et al.** (2014). The Effect of Graduated Response Anti-Piracy Laws on Music Sales. *JEMS*.

---

## Cross-Reference Index

| Topic | Bibliography File |
|-------|------------------|
| Attribution-by-design | `attribution-by-design-*.md` |
| Artist perspectives | `key/impact-generative-ai-on-artists.md` |
| Watermark robustness | `audio-watermarking-neural-codecs-*.md` |
| Data provenance | `key/bridging-data-provenance-gap-*.md` |
| Machine unlearning | `key/no-encore-*.md`, `key/large-scale-training-data-*.md` |
| Data protection taxonomy | `key/rethinking-data-protection-*.md` |
| Cultural slop | `key/when-ai-turns-culture-into-slop-*.md` |
