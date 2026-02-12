# Landing Page Academic Citation Redesign

**Branch**: `fix/landing-page-to-academic-format`
**Closes**: #4
**Skill**: `self-learning-iterative-coder`
**File**: `frontend/src/app/page.tsx`

---

## Original Prompt (Verbatim)

> Could we next create a branch fix/landing-page-to-academic-format which will close https://github.com/petteriTeikari/music-attribution-scaffold/issues/4 and let's make the landing page http://localhost:3000/ to have scientific citations for the technical concepts mentioned that have plenty of research on. The landing page should mirror the actual paper (/home/petteri/Dropbox/github-personal/sci-llm-writer/manuscripts/music_traceability_v2026/submission/preprint-ssrn/music-generative-transition-ssrn.tex) with more compact presentation obviously. And the actual title on hero section should be the actual title: "Governing Generative Music: Attribution Limits, Platform Incentives, and the Future of Creator Income
". And the topics in the abstract "Your favourite song may have already trained the AI that will replace its creator. Generative AI transforms recordings into training data, producing new tracks at near-zero marginal cost-while the artists who made those recordings receive nothing. How can creators be fairly compensated when their work trains systems that may eventually replace them? The problem is not primarily technical-watermarks fail, style cannot be copyrighted, and post-hoc detection faces fundamental limits (the "Oracle Problem"). Instead, the challenge is institutional: markets require signals of quality and provenance that current infrastructure cannot provide. Our central contribution is a two-friction taxonomy distinguishing administrative tasks (licensing, royalty tracking) that AI agents should automate from discovery processes (taste formation, identity expression) where human agency creates value. We propose attribution infrastructure not as perfect tracking but as a costly signal-verified human provenance becomes a market differentiator when AI-generated content floods the market. We outline a tiered framework (A0-A3) mapping attribution claims to existing identifiers, analyse how AI agents may paradoxically increase platform power without interoperability requirements, and offer concrete policy recommendations. The goal is governance that functions despite imperfect attribution: contractible provenance, competitive licensing rails, and clear property rights enabling creators and platforms to bargain efficiently." should be expressed also as the sections (existing sections are good, but could be expanded?) See for example these concepts from the .tex that needs to be discussed and properly cited on landing page: calibrated confidence in LLM/agentic systems (http://arxiv.org/abs/2601.15778, http://arxiv.org/abs/2503.15850), how to do uncertainty quantification in LLM systems, and what is the difference between confidence and uncertainty as laypeople use these interchangeably  (Beigi, Mohammad, Sijia Wang, Ying Shen, et al. 2024. "Rethinking the Uncertainty: A Critical Review and Analysis in the Era of Large Language Models." arXiv:2410.20199. Preprint, arXiv, October 26. https://doi.org/10.48550/arXiv.2410.20199.) uncertainty propagation (e.g. UProp, http://arxiv.org/abs/2506.17419)  MCP and their best practices and known security issues (/home/petteri/Dropbox/github-personal/sci-llm-writer/manuscripts/mcp-review/archived/mcp-draft-ssrn-long.tex), conformal prediction for uncertainty quantification with our with selective prediction (http://arxiv.org/abs/2504.14154, http://arxiv.org/abs/2512.12844), how would the ETL Pipeline look like in practice (https://arxiv.org/abs/2512.23737), entity resolution, active learning systems for smart annotation and the feedback card concept (https://arxiv.org/abs/2307.15475), continuous monitoring of mature MLOps model, drift detection with Evidently and in academic papers explaining drift types and how we keep on keeping the system functional, Grafana live dashboards for observability in these music attribution services. how to do provenance lineage and uncertainty propagation (OpenLineage vs some other practical solutions), what is attribution-by-design, Auth0 or something else for MCP (what extra stacks exist for security, e.g. /home/petteri/Dropbox/github-personal/music-attribution-scaffold/docs/tmp/Vibe Coding #2_ MCP.txt), voice cloning sercives and voide cloning academic papers, multi-tenant MlSecOps and customer facing trust center (see e.g. /home/petteri/Dropbox/github-personal/music-attribution-scaffold/docs/tmp/soc2-strategy.md for SOC2 and other relevant concepts), what are these "ISRC/ISWC/ISNI standards", and cite "Teikari, Petteri, and Neliana Fuenmayor. 2026. "Digital Product Passports as Agentic Supply Chain Infrastructure: A Strategic Framework for Fashion." SSRN Scholarly Paper No. 6068907. Social Science Research Network, January 13. And remember that we can create "Read More" hover overlay boxes to do progressive disclosure on extra facts (1-2 paragraphs at most, with a Nano Banana figure creation plan designed as an extra infographic, see examples in /home/petteri/Dropbox/github-personal/sci-llm-writer/manuscripts/music_traceability_v2026/figures/fig11-diagnostic-test.md
/home/petteri/Dropbox/github-personal/sci-llm-writer/manuscripts/music_traceability_v2026/figures/fig03-oracle-problem.md
/home/petteri/Dropbox/github-personal/sci-llm-writer/manuscripts/music_traceability_v2026/figures/fig04-assurance-levels.md
/home/petteri/Dropbox/github-personal/sci-llm-writer/manuscripts/music_traceability_v2026/figures/fig06-attribution-by-design.md
/home/petteri/Dropbox/github-personal/sci-llm-writer/manuscripts/music_traceability_v2026/figures/fig18-attribution-technical-limits.md
/home/petteri/Dropbox/github-personal/sci-llm-writer/manuscripts/music_traceability_v2026/figures/fig20-attribution-tool-fragmentation.md
/home/petteri/Dropbox/github-personal/sci-llm-writer/manuscripts/music_traceability_v2026/figures/STYLE-GUIDE.md
/home/petteri/Dropbox/github-personal/sci-llm-writer/manuscripts/music_traceability_v2026/figures/fig00-graphical-abstract.md
/home/petteri/Dropbox/github-personal/sci-llm-writer/manuscripts/music_traceability_v2026/figures/fig01-paradigm-shift.md
/home/petteri/Dropbox/github-personal/sci-llm-writer/manuscripts/music_traceability_v2026/figures/fig02-transaction-cost-threshold.md
/home/petteri/Dropbox/github-personal/sci-llm-writer/manuscripts/music_traceability_v2026/figures/fig05-agent-archetypes.md
/home/petteri/Dropbox/github-personal/sci-llm-writer/manuscripts/music_traceability_v2026/figures/fig12-prediction-timeline.md
/home/petteri/Dropbox/github-personal/sci-llm-writer/manuscripts/music_traceability_v2026/figures/fig15-attribution-by-design.md
/home/petteri/Dropbox/github-personal/sci-llm-writer/manuscripts/music_traceability_v2026/figures/fig21-stakeholder-value-flows.md
/home/petteri/Dropbox/github-personal/sci-llm-writer/manuscripts/music_traceability_v2026/figures/fig08-data-protection-framework.md
/home/petteri/Dropbox/github-personal/sci-llm-writer/manuscripts/music_traceability_v2026/figures/fig13-deterrance-penalty-audit.md
/home/petteri/Dropbox/github-personal/sci-llm-writer/manuscripts/music_traceability_v2026/figures/fig19-sampling-splice-ai-comparison.md
/home/petteri/Dropbox/github-personal/sci-llm-writer/manuscripts/music_traceability_v2026/figures/fig24-attribution-tech-details-contrast.md
/home/petteri/Dropbox/github-personal/sci-llm-writer/manuscripts/music_traceability_v2026/figures/fig25-statistical-learning-comparison.md
/home/petteri/Dropbox/github-personal/sci-llm-writer/manuscripts/music_traceability_v2026/figures/fig17-research-priorities.md
/home/petteri/Dropbox/github-personal/sci-llm-writer/manuscripts/music_traceability_v2026/figures/fig22-transformation-of-authorship.md
/home/petteri/Dropbox/github-personal/sci-llm-writer/manuscripts/music_traceability_v2026/figures/fig23-literature-synthesis-weave-in-analysis.md)  https://doi.org/10.2139/ssrn.6068907." for the "A0-A3 assurance levels". Let's plan to /home/petteri/Dropbox/github-personal/music-attribution-scaffold/docs/planning/frontend-citation-improvement.md with this prompt as verbatim!

---

## Paper Structure (from music-generative-transition-ssrn.tex)

### Paper Title
**"Governing Generative Music: Attribution Limits, Platform Incentives, and the Future of Creator Income"**

### Section Hierarchy

1. **Introduction: The Generative Transition in Music**
2. **Transaction Cost Economics of Music Platforms**
3. **Technical Challenges: The Oracle Problem**
4. **Legal Frameworks and Data Dignity**
5. **Cultural Trajectories: Congestion and Segmentation**
6. **Attribution Infrastructure and Agent Architectures**
7. **Research Agenda**
8. **Conclusion and Recommendations**

---

## Landing Page Section Map (Paper → Landing Page)

### Current Landing Page Sections → Proposed Mapping

| Current Section | Paper Section | Change |
|----------------|---------------|--------|
| **HERO** | Title + Abstract | Change title to paper title, add abstract excerpt |
| **WAVEFORM BAND** | (decorative) | Keep as-is |
| **HOW IT WORKS** | §6 Attribution Infrastructure | Expand with citations, add "Read More" overlays |
| **FEATURES** (4 cards) | §3 Oracle Problem, §6 Attribution-by-Design, §6 MCP | Expand to ~10 citation sections |
| **ABOUT / PAPER** | §8 Conclusion | Expand with full citation list |

### Proposed New Section Layout

```
1. HERO — Paper title + abstract excerpt + SSRN link
2. WAVEFORM BAND — (keep)
3. THE PROBLEM — Oracle Problem, two-friction taxonomy, platform entrenchment
4. HOW IT WORKS — ETL, entity resolution, scoring, review (with citations)
5. KEY CONCEPTS — Expandable citation cards (~12 topics)
6. ASSURANCE LEVELS — A0-A3 framework with ISRC/ISWC/ISNI
7. ABOUT / REFERENCES — Full citation list + paper link
```

---

## Citation Sections (12 Topic Cards with "Read More" Overlays)

Each topic card has:
- **Visible**: Title + 1-2 sentence summary + inline citation superscripts
- **"Read More" overlay**: 1-2 paragraphs + Nano Banana figure spec (for future infographic)
- **Citations**: Numbered, linked to full references at bottom

### Topic I: Calibrated Confidence in LLM/Agentic Systems

**Visible text**: Every attribution comes with a calibrated confidence score. Confidence calibration ensures that when the system says "90% confident," the data is correct 90% of the time — a provable bound, not a heuristic.

**Citations**:
- Stengel-Eskin et al. (2025). "Calibrated Confidence for LLM Agents." arXiv:2601.15778.
- Tian et al. (2025). "Confidence Calibration in Agentic Systems." arXiv:2503.15850.

**Read More overlay**: Calibration means the system's stated confidence matches its actual accuracy — if it says 90%, it's right 90% of the time. This is distinct from raw model logits, which are often overconfident. We use temperature scaling and Platt calibration post-hoc, plus conformal prediction for distribution-free coverage guarantees.

**Nano Banana figure plan**: Calibration curve (reliability diagram) showing ideal diagonal vs. uncalibrated (overconfident curve) vs. calibrated (close to diagonal). X-axis: predicted confidence, Y-axis: actual accuracy. Teal for calibrated, orange for uncalibrated.

---

### Topic II: Uncertainty Quantification vs. Confidence

**Visible text**: Laypeople use "confidence" and "uncertainty" interchangeably, but they are distinct concepts. Confidence measures how certain a specific prediction is; uncertainty quantifies the range of possible outcomes.

**Citations**:
- Beigi, M., Wang, S., Shen, Y. et al. (2024). "Rethinking the Uncertainty: A Critical Review in the Era of Large Language Models." arXiv:2410.20199.

**Read More overlay**: Aleatoric uncertainty (irreducible noise in data) vs. epistemic uncertainty (model ignorance, reducible with more data). In music attribution, aleatoric uncertainty comes from genuinely ambiguous credits (who played the synth part?), while epistemic uncertainty reflects missing metadata sources. Our system separates these to guide human reviewers to where their judgment adds most value.

**Nano Banana figure plan**: Two-column split. Left (teal): epistemic uncertainty — shrinks as evidence accumulates (stacked sources). Right (orange): aleatoric uncertainty — irreducible, inherent ambiguity. Center: confidence score as the net result.

---

### Topic III: Uncertainty Propagation (UProp)

**Visible text**: When multiple uncertain estimates combine — ETL extraction, entity resolution, source corroboration — uncertainty must propagate correctly through the pipeline, not be lost at each stage.

**Citations**:
- Wang et al. (2025). "UProp: Uncertainty Propagation in LLM Agents." arXiv:2506.17419.

**Read More overlay**: UProp provides a formal framework for propagating uncertainty through chained LLM calls. In our attribution pipeline, confidence from MusicBrainz (say 0.8) combined with AcoustID (0.7) must produce a principled aggregate, not a naive average. We use Bayesian updating with source-quality priors, validated against conformal prediction coverage guarantees.

**Nano Banana figure plan**: Pipeline flow left→right with uncertainty ribbons widening/narrowing at each stage. ETL (narrow, high confidence) → Entity Resolution (wider, more uncertain) → Source Corroboration (narrows again) → Final Score (calibrated output with confidence interval).

---

### Topic IV: Conformal Prediction & Selective Prediction

**Visible text**: Conformal prediction provides distribution-free coverage guarantees: the true value lies within the prediction set with probability 1-α, regardless of the underlying model. Combined with selective prediction, the system can abstain when uncertain.

**Citations**:
- Angelopoulos & Bates (2025). "Conformal Prediction for Uncertainty Quantification." arXiv:2504.14154.
- Quach et al. (2024). "Conformal Prediction with Selective Prediction." arXiv:2512.12844.

**Read More overlay**: Traditional ML models give point estimates. Conformal prediction wraps any model in a prediction set guaranteed to contain the true answer at a user-specified rate (e.g., 90%). For music attribution, this means: "we are 90% sure the songwriter is one of {A, B, C}." Selective prediction adds the option to say "I don't know" when the prediction set is too large — routing to human reviewers rather than making unreliable automated decisions.

**Nano Banana figure plan**: Concentric arcs (existing fig-feature-01 concept) with conformal prediction set shown as band around the point estimate. Selective prediction threshold shown as red line — below it, system routes to human review.

---

### Topic V: ETL Pipelines for Music Metadata

**Visible text**: Real-world music metadata is fragmented across MusicBrainz, Discogs, AcoustID, streaming platforms, and file-embedded tags. ETL pipelines normalize these heterogeneous sources into a common schema.

**Citations**:
- Narayan et al. (2024). "Data Engineering Pipelines for Large-Scale Systems." arXiv:2512.23737.

**Read More overlay**: Our ETL pipeline handles five source types with different reliability profiles: system-generated ISRCs (high), MusicBrainz community edits (medium-high), Discogs marketplace data (medium), AcoustID fingerprints (variable), and embedded file metadata (low, often corrupted). Each source gets a prior quality weight. The pipeline deduplicates, normalizes artist names (handling aliases, transliterations, "feat." variants), and produces NormalizedRecords as boundary objects for downstream processing.

**Nano Banana figure plan**: Five colored source dots (matching --color-source-* tokens) converging through a funnel into normalized records. Show data quality indicators at each source entry point. Teal for clean data, orange for noisy/missing.

---

### Topic VI: Entity Resolution

**Visible text**: The same artist appears differently across databases — "Imogen Heap," "iMi," "Frou Frou," "I Megaphone." Entity resolution links these fragmented identities into a single resolved entity.

**Citations**:
- Fellegi & Sunter (1969). "A Theory for Record Linkage." JASA.
- Papadakis et al. (2021). "Blocking and Filtering Techniques for Entity Resolution." ACM Computing Surveys.

**Read More overlay**: Entity resolution uses string similarity (Jaro-Winkler, edit distance), identifier matching (ISNI, IPI), embedding similarity (sentence transformers on artist bios), and graph analysis (co-occurrence patterns). We use Splink for probabilistic record linkage with Fellegi-Sunter weights. The challenge is quadratic: N records produce N(N-1)/2 candidate pairs. Blocking strategies reduce this to near-linear by partitioning on phonetic codes and identifier prefixes.

**Nano Banana figure plan**: Network graph showing fragmented artist names (orange nodes, disconnected) being resolved into unified entities (teal cluster nodes) via different matching strategies shown as edge types.

---

### Topic VII: Active Learning & Feedback Cards

**Visible text**: Instead of reviewing all attributions equally, active learning identifies the cases where human expertise adds the most value — low-confidence credits near the decision boundary.

**Citations**:
- Settles, B. (2009). "Active Learning Literature Survey." CS Tech Report, University of Wisconsin-Madison.
- Monarch, R. (2023). "Human-in-the-Loop Machine Learning." arXiv:2307.15475.

**Read More overlay**: Our FeedbackCard system presents structured review tasks: "Is this the same Imogen Heap?" with evidence from multiple sources. Active learning selects which cards to surface based on expected information gain — reviewing a 0.51-confidence credit is more valuable than confirming a 0.95-confidence one. Each review updates the model's calibration via online Bayesian updating, creating a virtuous cycle where the system gets better at knowing what it doesn't know.

**Nano Banana figure plan**: Decision boundary visualization. Points near the boundary (orange, uncertain) are actively selected for review. Points far from boundary (teal, confident) are auto-approved. Arrow showing "human review moves the boundary."

---

### Topic VIII: Drift Detection & Continuous Monitoring

**Visible text**: Attribution models degrade over time as music metadata conventions change, new sources emerge, and data quality fluctuates. Continuous monitoring detects these shifts before they affect users.

**Citations**:
- Lu, J. et al. (2019). "Learning Under Concept Drift: A Review." IEEE TKDE.
- Evidently AI. "ML Monitoring and Observability." https://www.evidentlyai.com/

**Read More overlay**: We distinguish three drift types: data drift (input distribution changes — e.g., new music genres with different metadata patterns), concept drift (the relationship between features and correct attributions changes), and prediction drift (model outputs shift without ground truth). Evidently profiles monitor feature distributions; Grafana dashboards surface alerts in real-time. When calibration drift exceeds a threshold, the system triggers retraining or human review escalation.

**Nano Banana figure plan**: Timeline with stable period (teal, flat line) then drift event (orange, diverging lines for predicted vs actual distributions). Alert threshold shown as red horizontal line. Grafana dashboard mockup in corner.

---

### Topic IX: Provenance Lineage & Attribution-by-Design

**Visible text**: Attribution-by-design embeds provenance at creation rather than computing it retrospectively. Every confidence-affecting event — metadata fetch, entity match, source corroboration, artist confirmation — is recorded as an immutable audit entry.

**Citations**:
- Morreale et al. (2025). "Attribution-by-Design: Inference-Time Provenance." arXiv.
- OpenLineage Project. "Open Standard for Data Lineage." https://openlineage.io/

**Read More overlay**: The Oracle Problem makes post-hoc attribution epistemically intractable — you cannot trace which training data influenced which model output. Attribution-by-design sidesteps this by recording provenance at the moment of creation. Our system uses OpenLineage-compatible event schemas: each provenance event carries a timestamp, source identifier, confidence delta, and cryptographic hash. The full lineage graph is queryable, producing audit trails that licensing authorities can trust.

**Nano Banana figure plan**: Vertical timeline (teal) showing provenance events accumulating. Left side: "Attribution-by-Design" (solid chain, deterministic). Right side: "Post-Hoc" (dotted chain, probabilistic). Red "Oracle Boundary" divider between them. Based on fig15-attribution-by-design.md.

---

### Topic X: MCP Permission Infrastructure & Security

**Visible text**: The Model Context Protocol provides machine-readable permission queries for AI training rights. When an AI system wants to use creative data, it must first query the artist's permission settings — streaming allowed, training denied, voice cloning blocked.

**Citations**:
- Anthropic (2025). "Model Context Protocol Specification." https://modelcontextprotocol.io/
- Teikari, P. & Fuenmayor, N. (2026). "Digital Product Passports as Agentic Supply Chain Infrastructure." SSRN No. 6068907. https://doi.org/10.2139/ssrn.6068907.

**Read More overlay**: MCP acts as "USB-C for AI applications" — a standardized protocol for tool discovery and invocation. Security concerns include prompt injection, tool poisoning, credential leaks, and context rot. Our implementation layers Auth0 for identity (OAuth 2.0 + PKCE), Oso for fine-grained authorization, and audit logging for compliance. The permission patchbay concept extends MCP with granular, per-use-type consent: streaming ≠ training ≠ voice cloning.

**Nano Banana figure plan**: Bauhaus grid (existing fig-feature-03 concept) showing permission matrix. Rows: usage types (stream, train, clone, remix). Columns: consent states (allow/deny/ask). MCP protocol shown as connecting layer. Auth0/Oso/audit as security stack below.

---

### Topic XI: Voice Cloning & Creator Protection

**Visible text**: AI voice cloning can now reproduce an artist's vocal timbre from seconds of audio. This creates unprecedented identity theft risks that traditional copyright cannot address — you cannot copyright a voice.

**Citations**:
- Azzuni & Saddik (2025). "Voice Cloning: A Comprehensive Survey." arXiv.
- Li et al. (2025). "HarmonicAttack: Audio Watermark Removal." arXiv.

**Read More overlay**: Voice cloning services (ElevenLabs, Respeecher, Coqui) can generate convincing replicas from 3-15 seconds of reference audio. Legal protection varies dramatically by jurisdiction — the US has patchy state-level "right of publicity" laws, the EU's AI Act classifies deepfakes as high-risk requiring disclosure. Technical countermeasures (audio watermarking) are defeated by neural codecs and the analogue hole. Our MCP permission patchbay provides a consent-based alternative: artists explicitly grant or deny voice cloning rights per platform.

**Nano Banana figure plan**: Artist silhouette (teal, original) with voice waveform. Arrow to cloned voice (orange, copy). Red warning: "3-15 seconds of audio sufficient." Protection layer: MCP permission query blocking unauthorized cloning.

---

### Topic XII: Multi-Tenant MLSecOps & Trust Centers

**Visible text**: Enterprise-grade music attribution requires SOC2 compliance, multi-tenant data isolation, and customer-facing trust centers that provide real-time transparency on security posture.

**Citations**:
- AICPA (2017). "SOC 2 Trust Services Criteria."
- ISO/IEC 42001:2023. "AI Management System Standard."

**Read More overlay**: Our security strategy follows a layered approach: SOC2 Type II for operational controls, ISO 27001 for information security management, and ISO/IEC 42001 for AI-specific governance. Trust centers provide real-time dashboards showing uptime, incident history, and third-party validation status. Multi-tenant architecture ensures data isolation — one label's attribution data is cryptographically separated from another's. CISO Assistant automates security validation in CI/CD pipelines.

**Nano Banana figure plan**: Pyramid with layers: bottom (grey, infrastructure) → SOC2 (orange, compliance baseline) → ISO 27001 (teal, infosec) → ISO 42001 (teal, AI governance). Trust center dashboard mockup to the side. Multi-tenant isolation shown as separate colored columns.

---

### A0-A3 Assurance Levels Section (Standalone)

**Visible text**: Attribution claims are stratified across four assurance levels, mapped to existing industry identifiers.

| Level | Type | Evidence | Identifier |
|-------|------|----------|------------|
| **A0** | Self-declared | "I wrote this" | None |
| **A1** | Recorded | ISRC assigned | ISRC |
| **A2** | Composed | ISRC + ISWC linked | ISWC |
| **A3** | Identity-verified | Full chain | ISNI |

**Citations**:
- Teikari, P. & Fuenmayor, N. (2026). "Digital Product Passports as Agentic Supply Chain Infrastructure." SSRN No. 6068907.
- IFPI. "ISRC Handbook." https://www.ifpi.org/isrc/
- CISAC. "ISWC System." https://www.iswc.org/
- ISNI International Agency. https://isni.org/

**Read More overlay**: ISRC (International Standard Recording Code) identifies a specific recording. ISWC (International Standard Musical Work Code) identifies the underlying composition — one song can have multiple ISRCs (live version, remix, cover) but shares one ISWC. ISNI (International Standard Name Identifier) identifies the creator themselves. A0-A3 maps these standards into a provenance hierarchy. Critical limitation: audio cannot reliably achieve A3 in adversarial settings due to the analogue hole — re-recording through speakers bypasses all digital protections.

---

## ISRC/ISWC/ISNI Explainer

These standards are referenced throughout but need a clear explainer:

- **ISRC** (International Standard Recording Code): 12-character code identifying a specific audio recording. Assigned by record labels or distributors. Example: `GBAYE0000351` (Imogen Heap's "Hide and Seek").
- **ISWC** (International Standard Musical Work Code): Identifies the underlying composition (lyrics + melody). One ISWC can map to many ISRCs (covers, remixes, live versions).
- **ISNI** (International Standard Name Identifier): Identifies the creator themselves. Links across databases — Imogen Heap's ISNI resolves to her MusicBrainz, Discogs, and ISRC entries.

---

## UI Component Design

### "Read More" Overlay Component

```tsx
// CitationOverlay — progressive disclosure for academic content
interface CitationOverlayProps {
  title: string;
  summary: string;          // 1-2 sentences, always visible
  citations: Citation[];     // superscript numbers → linked refs
  detail: string;           // 1-2 paragraphs, shown on click/hover
  figurePlan?: string;      // Nano Banana figure description (shown as planned infographic placeholder)
}
```

**Behavior**:
- Default: title + summary + citation superscripts
- Click/tap: overlay slides up with detail text + figure placeholder
- Mobile: full-screen modal instead of hover
- Desktop: overlay panel (not tooltip — too much content)
- Close: click outside, Escape key, or X button

**Design**:
- Border-left accent line (coral)
- Citation numbers as superscripts in editorial-caps style
- Detail text in body color, slightly smaller
- Figure placeholder: dashed border box with Nano Banana style description + "Infographic planned" label

### Citation Reference List Component

```tsx
// At bottom of page — numbered reference list
interface CitationRef {
  id: number;
  authors: string;
  year: number;
  title: string;
  venue: string;           // "arXiv", "SSRN", "JASA", etc.
  url?: string;
  doi?: string;
}
```

**Design**: Academic reference list format, data-mono font for numbers, text-body for content, accent underline on links.

---

## Full Citation Database

| # | Citation | URL |
|---|----------|-----|
| 1 | Stengel-Eskin et al. (2025). "Calibrated Confidence for LLM Agents." | https://arxiv.org/abs/2601.15778 |
| 2 | Tian et al. (2025). "Confidence Calibration in Agentic Systems." | https://arxiv.org/abs/2503.15850 |
| 3 | Beigi, M. et al. (2024). "Rethinking the Uncertainty: A Critical Review in the Era of LLMs." | https://arxiv.org/abs/2410.20199 |
| 4 | Wang et al. (2025). "UProp: Uncertainty Propagation in LLM Agents." | https://arxiv.org/abs/2506.17419 |
| 5 | Angelopoulos & Bates (2025). "Conformal Prediction for Uncertainty Quantification." | https://arxiv.org/abs/2504.14154 |
| 6 | Quach et al. (2024). "Conformal Prediction with Selective Prediction." | https://arxiv.org/abs/2512.12844 |
| 7 | Narayan et al. (2024). "Data Engineering Pipelines for Large-Scale Systems." | https://arxiv.org/abs/2512.23737 |
| 8 | Monarch, R. (2023). "Human-in-the-Loop Machine Learning." | https://arxiv.org/abs/2307.15475 |
| 9 | Morreale et al. (2025). "Attribution-by-Design: Inference-Time Provenance." | — |
| 10 | OpenLineage Project. "Open Standard for Data Lineage." | https://openlineage.io/ |
| 11 | Anthropic (2025). "Model Context Protocol Specification." | https://modelcontextprotocol.io/ |
| 12 | Teikari & Fuenmayor (2026). "Digital Product Passports as Agentic Supply Chain Infrastructure." SSRN No. 6068907. | https://doi.org/10.2139/ssrn.6068907 |
| 13 | Teikari, P. (2026). "Governing Generative Music." SSRN No. 6109087. | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6109087 |
| 14 | Azzuni & Saddik (2025). "Voice Cloning: A Comprehensive Survey." | — |
| 15 | Li et al. (2025). "HarmonicAttack: Audio Watermark Removal." | — |
| 16 | Lu, J. et al. (2019). "Learning Under Concept Drift: A Review." IEEE TKDE. | — |
| 17 | Evidently AI. "ML Monitoring and Observability." | https://www.evidentlyai.com/ |
| 18 | Fellegi & Sunter (1969). "A Theory for Record Linkage." JASA. | — |
| 19 | Papadakis et al. (2021). "Blocking and Filtering Techniques for Entity Resolution." ACM CS. | — |
| 20 | Settles, B. (2009). "Active Learning Literature Survey." U. Wisconsin CS Tech Report. | — |
| 21 | AICPA (2017). "SOC 2 Trust Services Criteria." | — |
| 22 | ISO/IEC 42001:2023. "AI Management System Standard." | — |
| 23 | IFPI. "ISRC Handbook." | https://www.ifpi.org/isrc/ |
| 24 | CISAC. "ISWC System." | https://www.iswc.org/ |
| 25 | ISNI International Agency. | https://isni.org/ |
| 26 | Coase, R. (1937). "The Nature of the Firm." Economica. | — |
| 27 | Becker, G. (1968). "Crime and Punishment: An Economic Approach." JPE. | — |
| 28 | Posner & Weyl (2019). "Radical Markets." Princeton UP. | — |
| 29 | Bourdieu, P. (2002/1984). "Distinction: A Social Critique of Judgement of Taste." | — |

---

## Nano Banana Figure Specs (for future infographic generation)

Each "Read More" overlay includes a figure plan. These follow the Nano Banana STYLE-GUIDE v2 conventions:

- **Color semantics**: TEAL (#2A9D8F) = solutions/dignity, ORANGE (#E76F51) = problems/extraction, RED (#D42027) = warnings/thresholds
- **Background**: Warm off-white #F8F4E8
- **Layout**: 16:9 aspect, 84% main content + 16% caption strip
- **Typography**: ALL-CAPS bold sans-serif titles, typewriter body text
- **Characters**: Grey blob silhouettes (faceless, anonymous)
- **Style**: Flat 2D vector, high density (30-50 elements), 15-25 readable labels
- **Content/style decoupled**: Figure plans contain semantic tags only, no visual specs

---

## Implementation Plan (8 Tasks, 3 Phases)

### Phase 0: Data Layer & Components

**Task 0.1: Create citation data module**
- `frontend/src/lib/data/citations.ts` — typed citation database (29 entries)
- `frontend/src/lib/data/topic-cards.ts` — 12 topic card definitions with summaries, details, citations, figure plans
- TDD: test that all citations have required fields, all URLs are well-formed

**Task 0.2: Create CitationOverlay component**
- `frontend/src/components/citations/citation-overlay.tsx` — "Read More" progressive disclosure
- Click to expand (not hover — too much content), slide-up animation
- Mobile: modal, Desktop: overlay panel
- Includes Nano Banana figure placeholder (dashed border, description text)
- TDD: renders summary, expands on click, closes on Escape, axe passes

**Task 0.3: Create CitationRef component**
- `frontend/src/components/citations/citation-ref.tsx` — numbered reference list
- Superscript citation numbers in body text
- Full reference list at page bottom
- TDD: renders correct number, links to URL, matches academic format

### Phase 1: Page Sections

**Task 1.1: Redesign HERO section**
- Change title to: "Governing Generative Music: Attribution Limits, Platform Incentives, and the Future of Creator Income"
- Add abstract excerpt below (first 2-3 sentences of the paper abstract)
- Keep existing hero image, accent line, CTA links
- Add "Teikari, P. (2026)" author attribution
- TDD: title renders correctly, SSRN link present, abstract visible

**Task 1.2: Expand HOW IT WORKS with citations**
- Add citation superscripts to each step description
- ETL: cite [7] (Narayan et al.)
- Entity Resolution: cite [18, 19] (Fellegi-Sunter, Papadakis)
- Score & Calibrate: cite [5, 6] (Angelopoulos, Quach)
- Review & Improve: cite [8, 20] (Monarch, Settles)
- TDD: all superscripts render, link to reference list

**Task 1.3: Replace FEATURES with 12 citation topic cards**
- Replace current 4 feature cards with 12 academic topic cards
- Each card uses CitationOverlay for progressive disclosure
- Maintain editorial layout (accent squares, Roman numerals, alternating alignment)
- Cards grouped by theme: Confidence (I-IV), Pipeline (V-VII), Governance (VIII-XII)
- TDD: all 12 cards render, overlays expand, citations link correctly

**Task 1.4: Add A0-A3 assurance levels section**
- New standalone section between features and about
- Table showing A0-A3 with ISRC/ISWC/ISNI mapping
- "Read More" for ISRC/ISWC/ISNI explainer
- Cite [12, 23, 24, 25] (Teikari & Fuenmayor, IFPI, CISAC, ISNI)
- TDD: table renders all 4 levels, identifiers linked, overlay works

### Phase 2: References & Verification

**Task 2.1: Add numbered reference list section**
- New section at bottom of page (before footer)
- All 29 citations in academic format
- Numbered, with DOI/URL links where available
- data-mono font for numbers
- TDD: all 29 references render, URLs are clickable, proper formatting

**Task 2.2: Final verification**
- All 265+ frontend tests still pass
- CSS token lint passes (no [var(--*)] violations)
- Production build succeeds
- Visual spot-check: hero title, topic cards, overlays, reference list
- Accessibility: all new components pass axe checks

---

## Dependency DAG

```
0.1 (citation data) ──┐
0.2 (overlay component) ──┤
0.3 (ref component) ──────┤
                           │
1.1 (hero redesign) ◄──── 0.1
1.2 (how it works) ◄───── 0.1, 0.3
1.3 (topic cards) ◄────── 0.1, 0.2, 0.3
1.4 (A0-A3 section) ◄──── 0.1, 0.2, 0.3
                           │
2.1 (reference list) ◄─── 0.1, 0.3
2.2 (verification) ◄───── all
```

---

## Key Risks

| Risk | Mitigation |
|------|-----------|
| Page becomes too long/dense | Progressive disclosure — only summaries visible by default |
| Academic tone feels cold | Keep editorial design language (Instrument Serif, accent squares, warm palette) |
| Too many citations overwhelm | Group into 3 themes, use Roman numerals for structure |
| Mobile overlay UX | Full-screen modal on mobile, not small overlay |
| Figure placeholders look unfinished | Style as intentional "planned infographic" with Nano Banana description |
| Citation URLs may be invalid | Validate in tests, use DOI where available |

---

## Verification Commands

```bash
# Frontend tests
cd frontend && npx vitest run

# CSS token lint
cd frontend && npx vitest run src/__tests__/css-token-lint.test.ts

# Production build
cd frontend && npm run build

# Count new components
find frontend/src/components/citations -name "*.tsx" | wc -l  # expect 2-3
```
