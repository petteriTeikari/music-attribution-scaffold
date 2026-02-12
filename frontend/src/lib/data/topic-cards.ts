/**
 * Topic card definitions for the landing page academic citation sections.
 *
 * Each card maps to a concept from the SSRN paper with:
 * - A concise visible summary
 * - A "Read More" detail paragraph
 * - Citation IDs referencing the citation database
 * - A Nano Banana figure plan for future infographic generation
 */

export interface TopicCard {
  id: string;
  marker: string;
  title: string;
  summary: string;
  detail: string;
  citationIds: number[];
  figurePlan: string;
  image?: string;
  imageAlt?: string;
}

export interface TopicGroup {
  label: string;
  cardIds: string[];
  image?: string;
  imageAlt?: string;
}

export const TOPIC_CARDS: TopicCard[] = [
  // ── CONFIDENCE GROUP (I–IV) ──
  {
    id: "calibrated-confidence",
    marker: "I",
    title: "Calibrated Confidence",
    summary:
      "Every attribution comes with a calibrated confidence score. When the system says \u201c90% confident,\u201d the data is correct 90% of the time \u2014 a provable bound, not a heuristic.",
    detail:
      "Calibration means the system\u2019s stated confidence matches its actual accuracy. This is distinct from raw model logits, which are often overconfident. We use temperature scaling and Platt calibration post-hoc, plus conformal prediction for distribution-free coverage guarantees. Evidence is stratified across assurance levels (A0 unverified \u2192 A3 artist-verified), mapped to industry standards like ISRC, ISWC, and ISNI.",
    citationIds: [1, 2],
    figurePlan:
      "Calibration curve (reliability diagram) showing ideal diagonal vs. uncalibrated (overconfident curve) vs. calibrated (close to diagonal). X-axis: predicted confidence, Y-axis: actual accuracy. Teal for calibrated, orange for uncalibrated.",
    image: "/images/figures/fig-topic-01-calibrated-confidence.webp",
    imageAlt:
      "Split infographic with a reliability diagram showing three curves: ideal diagonal, calibrated model in teal closely following it, and overconfident uncalibrated model curving away in orange with ECE gap shaded. A concrete music attribution example using Imogen Heap demonstrates the difference.",
  },
  {
    id: "uncertainty-vs-confidence",
    marker: "II",
    title: "Uncertainty vs. Confidence",
    summary:
      "Laypeople use \u201cconfidence\u201d and \u201cuncertainty\u201d interchangeably, but they are distinct concepts. Confidence measures how certain a specific prediction is; uncertainty quantifies the range of possible outcomes.",
    detail:
      "Aleatoric uncertainty (irreducible noise in data) vs. epistemic uncertainty (model ignorance, reducible with more data). In music attribution, aleatoric uncertainty comes from genuinely ambiguous credits (who played the synth part?), while epistemic uncertainty reflects missing metadata sources. Our system separates these to guide human reviewers to where their judgment adds most value.",
    citationIds: [3],
    figurePlan:
      "Two-column split. Left (teal): epistemic uncertainty \u2014 shrinks as evidence accumulates. Right (orange): aleatoric uncertainty \u2014 irreducible, inherent ambiguity. Center: confidence score as net result.",
    image: "/images/figures/fig-topic-02-uncertainty-vs-confidence.webp",
    imageAlt:
      "Four-quadrant infographic distinguishing data uncertainty (irreducible), model uncertainty (reducible), incomplete knowledge, and contradicting sources in music attribution. A banner states Confidence does not equal Uncertainty.",
  },
  {
    id: "uncertainty-propagation",
    marker: "III",
    title: "Uncertainty Propagation",
    summary:
      "When multiple uncertain estimates combine \u2014 ETL extraction, entity resolution, source corroboration \u2014 uncertainty must propagate correctly through the pipeline, not be lost at each stage.",
    detail:
      "UProp provides a formal framework for propagating uncertainty through chained LLM calls. In our attribution pipeline, confidence from MusicBrainz (say 0.8) combined with AcoustID (0.7) must produce a principled aggregate, not a naive average. We use Bayesian updating with source-quality priors, validated against conformal prediction coverage guarantees.",
    citationIds: [4],
    figurePlan:
      "Pipeline flow left\u2192right with uncertainty ribbons widening/narrowing at each stage. ETL (narrow) \u2192 Entity Resolution (wider) \u2192 Source Corroboration (narrows) \u2192 Final Score with confidence interval.",
    image: "/images/figures/fig-topic-03-uncertainty-propagation.webp",
    imageAlt:
      "Horizontal pipeline showing uncertainty propagation through four music attribution stages for Hide and Seek by Imogen Heap, with uncertainty ribbons widening at entity resolution and narrowing at source corroboration, settling at 0.91 plus-minus 0.10.",
  },
  {
    id: "conformal-prediction",
    marker: "IV",
    title: "Conformal & Selective Prediction",
    summary:
      "Conformal prediction provides distribution-free coverage guarantees: the true value lies within the prediction set with probability 1\u2212\u03b1. Combined with selective prediction, the system can abstain when uncertain.",
    detail:
      "Traditional ML models give point estimates. Conformal prediction wraps any model in a prediction set guaranteed to contain the true answer at a user-specified rate (e.g., 90%). For music attribution: \u201cwe are 90% sure the songwriter is one of {A, B, C}.\u201d Selective prediction adds the option to say \u201cI don\u2019t know\u201d when the prediction set is too large \u2014 routing to human reviewers rather than making unreliable automated decisions.",
    citationIds: [5, 6],
    figurePlan:
      "Concentric arcs with conformal prediction set shown as band around point estimate. Selective prediction threshold shown as red line \u2014 below it, system routes to human review.",
    image: "/images/figures/fig-topic-04-conformal-prediction.webp",
    imageAlt:
      "Three-layer infographic distinguishing conformal prediction (concentric arcs with 90% coverage guarantee), selective prediction (abstention gate with threshold line), and SConU (principled synthesis using conformal p-values). A risk slider shows user-controllable alpha parameter.",
  },
  // ── PIPELINE GROUP (V–VII) ──
  {
    id: "etl-pipelines",
    marker: "V",
    title: "ETL Pipelines",
    summary:
      "Real-world music metadata is fragmented across MusicBrainz, Discogs, AcoustID, streaming platforms, and file-embedded tags. ETL pipelines normalize these heterogeneous sources into a common schema.",
    detail:
      "Our ETL pipeline handles five source types with different reliability profiles: system-generated ISRCs (high), MusicBrainz community edits (medium-high), Discogs marketplace data (medium), AcoustID fingerprints (variable), and embedded file metadata (low, often corrupted). Each source gets a prior quality weight. The pipeline deduplicates, normalizes artist names (handling aliases, transliterations, \u201cfeat.\u201d variants), and produces NormalizedRecords as boundary objects for downstream processing.",
    citationIds: [7],
    figurePlan:
      "Five colored source dots converging through a funnel into normalized records. Data quality indicators at each source entry point. Teal for clean data, orange for noisy/missing.",
    image: "/images/figures/fig-topic-05-etl-pipelines.webp",
    imageAlt:
      "Infographic showing five music metadata sources (MusicBrainz, Discogs, AcoustID, Streaming, File Metadata) converging through a harmonization funnel into unified records, with schema characteristics and quality bars ranging from high (teal) to low (orange).",
  },
  {
    id: "entity-resolution",
    marker: "VI",
    title: "Entity Resolution",
    summary:
      'The same artist appears differently across databases \u2014 "Imogen Heap," "iMi," "Frou Frou," "I Megaphone." Entity resolution links these fragmented identities into a single resolved entity.',
    detail:
      "Entity resolution uses string similarity (Jaro-Winkler, edit distance), identifier matching (ISNI, IPI), embedding similarity (sentence transformers on artist bios), and graph analysis (co-occurrence patterns). We use Splink for probabilistic record linkage with Fellegi-Sunter weights. The challenge is quadratic: N records produce N(N-1)/2 candidate pairs. Blocking strategies reduce this to near-linear.",
    citationIds: [18, 19],
    figurePlan:
      "Network graph showing fragmented artist names (orange nodes, disconnected) being resolved into unified entities (teal cluster nodes) via different matching strategies shown as edge types.",
    image: "/images/figures/fig-topic-06-entity-resolution.webp",
    imageAlt:
      "Entity resolution infographic showing how Imogen Heap appears as five different database entries. Fellegi-Sunter match weights per field: ISNI +13.3 bits, name +6.5 bits. Two worked examples: Heap + Frou Frou resolving via shared ISNI (0.92 LINK) and I Megaphone + Heap falling into review (0.58 POSSIBLE LINK).",
  },
  {
    id: "active-learning",
    marker: "VII",
    title: "Active Learning & Feedback Cards",
    summary:
      "Instead of reviewing all attributions equally, active learning identifies the cases where human expertise adds the most value \u2014 low-confidence credits near the decision boundary.",
    detail:
      'Our FeedbackCard system presents structured review tasks: "Is this the same Imogen Heap?" with evidence from multiple sources. Active learning selects which cards to surface based on expected information gain \u2014 reviewing a 0.51-confidence credit is more valuable than confirming a 0.95-confidence one. Each review updates calibration via online Bayesian updating, creating a virtuous cycle.',
    citationIds: [8, 20],
    figurePlan:
      "Decision boundary visualization. Points near boundary (orange, uncertain) actively selected for review. Points far from boundary (teal, confident) auto-approved. Arrow showing human review moves the boundary.",
    image: "/images/figures/fig-topic-07-active-learning.webp",
    imageAlt:
      "Active learning infographic showing an artist's 200-track catalog split: 170 high-confidence tracks auto-approved (teal) and 30 near-boundary tracks routed to review (orange). Progressive time savings bars show auto-approval rates improving from 85% to 95% across iterations.",
  },
  // ── GOVERNANCE GROUP (VIII–XII) ──
  {
    id: "drift-detection",
    marker: "VIII",
    title: "Drift Detection & Monitoring",
    summary:
      "Attribution models degrade over time as metadata conventions change, new sources emerge, and data quality fluctuates. Continuous monitoring detects these shifts before they affect users.",
    detail:
      "We distinguish three drift types: data drift (input distribution changes), concept drift (feature-to-attribution relationship changes), and prediction drift (model outputs shift without ground truth). Evidently profiles monitor feature distributions; Grafana dashboards surface real-time alerts. When calibration drift exceeds a threshold, the system triggers retraining or human review escalation.",
    citationIds: [16, 17],
    figurePlan:
      "Timeline with stable period (teal, flat line) then drift event (orange, diverging lines). Alert threshold shown as red horizontal line. Grafana dashboard mockup in corner.",
    image: "/images/figures/fig-topic-08-drift-detection.webp",
    imageAlt:
      "Drift detection infographic showing four drift types mapped to music attribution: sudden (Spotify API removal), gradual (hyperpop emergence), incremental (LUFS shift), recurring (vinyl revival). AI-generated content inflection point shows bimodal confidence distributions.",
  },
  {
    id: "provenance-lineage",
    marker: "IX",
    title: "Provenance & Attribution-by-Design",
    summary:
      "Attribution-by-design embeds provenance at creation rather than computing it retrospectively. Every confidence-affecting event is recorded as an immutable audit entry.",
    detail:
      "The Oracle Problem makes post-hoc attribution epistemically intractable \u2014 you cannot trace which training data influenced which output. Attribution-by-design sidesteps this by recording provenance at the moment of creation. Our system uses OpenLineage-compatible event schemas: each provenance event carries a timestamp, source identifier, confidence delta, and cryptographic hash. The full lineage graph is queryable for audit.",
    citationIds: [9, 10],
    figurePlan:
      'Vertical timeline (teal) showing provenance events accumulating. Left: "Attribution-by-Design" (solid chain). Right: "Post-Hoc" (dotted chain). Red "Oracle Boundary" divider between them.',
    image: "/images/figures/fig-topic-09-provenance-lineage.webp",
    imageAlt:
      "Provenance infographic split by an Oracle Boundary. Left: attribution-by-design with Hide and Seek as a solid provenance chain (CREATE, REGISTER, DISTRIBUTE, DERIVE, AI CONSENT). Right: post-hoc attribution hitting three epistemic barriers. Deterrence equation below.",
  },
  {
    id: "mcp-permissions",
    marker: "X",
    title: "MCP Permission Infrastructure",
    summary:
      "The Model Context Protocol provides machine-readable permission queries for AI training rights. When an AI system wants to use creative data, it must first query the artist\u2019s permission settings.",
    detail:
      'MCP acts as "USB-C for AI applications" \u2014 a standardized protocol for tool discovery and invocation. Security concerns include prompt injection, tool poisoning, credential leaks, and context rot. Our implementation layers OAuth 2.0 + PKCE for identity, fine-grained authorization, and audit logging for compliance. The permission patchbay extends MCP with granular per-use-type consent: streaming \u2260 training \u2260 voice cloning.',
    citationIds: [11, 12],
    figurePlan:
      "Bauhaus grid showing permission matrix. Rows: usage types (stream, train, clone, remix). Columns: consent states (allow/deny/ask). MCP protocol as connecting layer. Auth stack below.",
    image: "/images/figures/fig-topic-10-mcp-permissions.webp",
    imageAlt:
      "MCP permission infrastructure infographic showing a four-step consent flow with JSON-RPC query and response, a nuanced consent matrix for three Imogen Heap tracks across five use types, and an assurance gate mapping A0-A3 to permission granularity.",
  },
  {
    id: "voice-cloning",
    marker: "XI",
    title: "Voice Cloning & Creator Protection",
    summary:
      "AI voice cloning can reproduce an artist\u2019s vocal timbre from seconds of audio. This creates identity theft risks that traditional copyright cannot address \u2014 you cannot copyright a voice.",
    detail:
      "Voice cloning services can generate convincing replicas from 3\u201315 seconds of reference audio. Legal protection varies \u2014 the US has patchy state-level \u201cright of publicity\u201d laws, the EU\u2019s AI Act classifies deepfakes as high-risk. Technical countermeasures (audio watermarking) are defeated by neural codecs and the analogue hole. Our MCP permission patchbay provides a consent-based alternative: artists explicitly grant or deny voice cloning rights per platform.",
    citationIds: [14, 15],
    figurePlan:
      'Artist silhouette (teal, original) with voice waveform. Arrow to cloned voice (orange, copy). Red warning: "3\u201315 seconds sufficient." MCP permission query blocking unauthorized cloning.',
    image: "/images/figures/fig-topic-11-voice-cloning.webp",
    imageAlt:
      "Voice cloning infographic showing the collapsing audio barrier from 10+ minutes to 3 seconds. Three case studies spanning the consent spectrum: Holly+ (A3 consent-first), Grimes Elf.Tech (A2 permissive), Drake/Weeknd deepfake (A0 adversarial). ELVIS Act highlighted.",
  },
  {
    id: "mlsecops-trust",
    marker: "XII",
    title: "MLSecOps & Trust Centers",
    summary:
      "Enterprise-grade music attribution requires SOC2 compliance, multi-tenant data isolation, and customer-facing trust centers with real-time transparency on security posture.",
    detail:
      "Our security strategy follows a layered approach: SOC2 Type II for operational controls, ISO 27001 for information security management, and ISO/IEC 42001 for AI-specific governance. Trust centers provide real-time dashboards showing uptime, incident history, and third-party validation. Multi-tenant architecture ensures cryptographic data isolation between labels.",
    citationIds: [21, 22],
    figurePlan:
      "Pyramid: infrastructure (grey) \u2192 SOC2 (orange) \u2192 ISO 27001 (teal) \u2192 ISO 42001 (teal). Trust center dashboard mockup. Multi-tenant isolation as separate colored columns.",
    image: "/images/figures/fig-topic-12-mlsecops-trust.webp",
    imageAlt:
      "MLSecOps infographic with asset-threat-layer table mapping five protected assets to music-specific threats. Security pyramid with certification tiers. Trust center dashboard showing 99.97% uptime, assurance distribution, and consent query metrics.",
  },
];

export const TOPIC_GROUPS: TopicGroup[] = [
  {
    label: "Confidence & Uncertainty",
    cardIds: [
      "calibrated-confidence",
      "uncertainty-vs-confidence",
      "uncertainty-propagation",
      "conformal-prediction",
    ],
    image: "/images/figures/fig-group-01-confidence-uncertainty.webp",
    imageAlt:
      "Narrow portrait overview of calibration curve, reducible vs irreducible uncertainty, pipeline uncertainty ribbon, and conformal prediction set with abstention threshold.",
  },
  {
    label: "Pipeline & Data",
    cardIds: [
      "etl-pipelines",
      "entity-resolution",
      "active-learning",
    ],
    image: "/images/figures/fig-group-02-pipeline-data.webp",
    imageAlt:
      "Narrow portrait overview of five data sources converging through ETL, entity resolution linking fragmented identities, and active learning decision boundary for human review.",
  },
  {
    label: "Governance & Security",
    cardIds: [
      "drift-detection",
      "provenance-lineage",
      "mcp-permissions",
      "voice-cloning",
      "mlsecops-trust",
    ],
    image: "/images/figures/fig-group-03-governance-security.webp",
    imageAlt:
      "Narrow portrait overview of drift detection, solid vs broken provenance chains, consent matrix, voice cloning protection, and security pyramid.",
  },
];
