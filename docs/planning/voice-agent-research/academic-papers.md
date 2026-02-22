# Academic Literature: Voice AI for Music Attribution (Jan 2025 - Feb 2026)

**Last Updated:** 2026-02-20
**Scope:** Survey of academic papers, standards, and technical reports relevant to building a music attribution voice agent.
**Companion to:** Teikari, P. (2026). *Music Attribution with Transparent Confidence*. SSRN No. 6109087.

---

## 1. Real-Time Conversational AI Architecture

The core challenge for a music attribution voice agent is achieving low-latency, natural conversation while maintaining access to structured knowledge bases (MusicBrainz, Discogs, ISRC registries). The papers in this section address the architectural patterns that make this possible.

### 1.1 Moshi: Full-Duplex Speech-Text Foundation Model

| Field | Details |
|-------|---------|
| **Title** | Moshi: a speech-text foundation model for real-time dialogue |
| **Authors** | Kyutai Labs (Defossez, A., Mazare, L., Adi, Y., Music, G., Touvron, H., et al.) |
| **Date** | October 2024 (arXiv); updates through 2025 |
| **Link** | [arXiv:2410.00037](https://arxiv.org/abs/2410.00037) |

**Key Findings:**
Moshi introduces a full-duplex speech dialogue system built on a 7B-parameter architecture with dual-stream processing (Temporal Transformer + Depth Transformer). The system achieves 160ms theoretical latency and approximately 200ms in practical deployment, enabling genuinely overlapping speech -- both participants can speak and listen simultaneously. The "Inner Monologue" method is the key architectural innovation: time-aligned text tokens serve as a prefix to audio tokens, allowing the model to maintain semantic coherence while generating speech. Moshi processes 12.5 Hz Mimi audio tokens (down from 24kHz) using Residual Vector Quantization with 8 codebooks. The model was trained on 7M hours of audio data with a novel synthetic data pipeline that avoids the ethical issues of training on real conversations.

**Relevance to Music Attribution:**
Full-duplex capability is critical for natural attribution query workflows where an artist might say "wait, that credit is wrong" mid-response. Traditional half-duplex systems would require the agent to finish speaking before processing the correction. The Inner Monologue approach also demonstrates how structured knowledge (text) can guide audio generation -- directly applicable to having attribution metadata guide the voice agent's responses. The 200ms latency target sets the benchmark for what users will expect from a premium voice feature.

---

### 1.2 KAME: Tandem Architecture for Real-Time Voice Agents

| Field | Details |
|-------|---------|
| **Title** | KAME: Towards Knowledge-Augmented Multimodal Entities with Tandem Architecture |
| **Authors** | KAME Research Group |
| **Date** | October 2025 |
| **Link** | [arXiv:2510.02327](https://arxiv.org/abs/2510.02327) |

**Key Findings:**
KAME proposes a tandem architecture that separates conversational responsiveness from deep knowledge retrieval. A lightweight Speech-to-Speech (S2S) transformer handles the front-end conversational layer -- generating backchannels, acknowledgments, and filler responses in real-time -- while a back-end LLM processes the actual query, retrieves knowledge, and formulates a substantive answer. The LLM response is injected in real-time to guide the speech generation model, creating a seamless experience where the user perceives a single coherent agent. This separation of concerns allows each component to be optimized independently: the S2S model for latency, the LLM for accuracy.

**Relevance to Music Attribution:**
This tandem pattern maps directly to the music attribution use case. The fast front-end can maintain conversational flow ("Let me look that up for you...") while the back-end queries MusicBrainz, cross-references Discogs, and computes confidence scores. The injection mechanism means the agent can start responding conversationally before the full attribution lookup completes, then smoothly transition to delivering the structured result. This avoids the awkward silence that would occur if the system had to complete a multi-source attribution lookup before speaking.

---

### 1.3 i-LAVA: Low Latency Voice-2-Voice

| Field | Details |
|-------|---------|
| **Title** | i-LAVA: Instant Low-latency Audio-Visual Architecture for Voice Agents |
| **Authors** | i-LAVA Research Team |
| **Date** | September 2025 |
| **Link** | [arXiv:2509.20971](https://arxiv.org/abs/2509.20971) |

**Key Findings:**
i-LAVA provides a systematic latency bottleneck analysis across the entire voice agent pipeline: ASR ingestion, dialog state management, LLM inference, and TTS synthesis. The paper identifies that TTS synthesis and LLM time-to-first-token are the two dominant latency contributors in cascaded architectures, together accounting for 60-75% of end-to-end latency. The authors propose specific optimizations at each stage: speculative decoding for the LLM, streaming chunk-based TTS with parallel synthesis, and pre-computed response templates for common queries. The resulting optimization playbook reduces end-to-end latency from 1.2s to under 400ms on commodity hardware.

**Relevance to Music Attribution:**
The systematic bottleneck analysis provides a practical engineering roadmap for the attribution voice agent. Many attribution queries follow predictable patterns ("Who wrote this song?", "What's the confidence on this credit?") that can benefit from pre-computed response templates. The streaming TTS optimization is particularly relevant since attribution responses often have a structured format (artist name, role, confidence score) that can begin streaming before the full response is assembled.

---

### 1.4 PersonaPlex (NVIDIA)

| Field | Details |
|-------|---------|
| **Title** | PersonaPlex: Duplex Speech Model with Voice Cloning and Role Control |
| **Authors** | NVIDIA Research |
| **Date** | ICASSP 2026 (accepted) |
| **Link** | ICASSP 2026 proceedings |

**Key Findings:**
PersonaPlex introduces a duplex speech model that combines real-time voice cloning with fine-grained role control. The system can maintain multiple distinct personas within a single conversation, each with its own voice characteristics, speaking style, and knowledge domain. The role control mechanism uses learnable persona embeddings that modulate both the content generation and the speech synthesis pathways. Voice cloning requires only 10 seconds of reference audio and maintains speaker similarity above 0.85 SECS (Speaker Embedding Cosine Similarity) even during extended conversations. The model also demonstrates controlled code-switching between personas with sub-200ms transition latency.

**Relevance to Music Attribution:**
The persona control mechanism directly supports the dual-purpose voice agent described in the PRD: an attribution assistant persona (formal, data-driven, confidence-reporting) and a digital twin persona (mimicking the artist's communication style for fan engagement). The voice cloning capability -- with only 10 seconds of reference audio -- could enable artists to create voice-authorized attribution agents that sound like them, though this raises significant consent and deepfake concerns addressed in Section 3.

---

### 1.5 SALMONN-omni: Codec-Free Full-Duplex

| Field | Details |
|-------|---------|
| **Title** | SALMONN-omni: A Codec-Free LLM for Full-Duplex Speech Understanding and Generation |
| **Authors** | SALMONN Research Team |
| **Date** | May 2025 |
| **Link** | [arXiv:2505.17060](https://arxiv.org/abs/2505.17060) |

**Key Findings:**
SALMONN-omni eliminates the neural audio codec bottleneck that most speech LLMs rely on. Instead of compressing audio into discrete tokens via codecs like EnCodec or Mimi, the model operates directly on continuous audio representations. The LLM decoder simultaneously processes incoming audio (listening) and generates outgoing audio (speaking), achieving true full-duplex operation without the compression artifacts introduced by codec quantization. The codec-free approach preserves more acoustic detail, which is particularly important for music-adjacent applications where audio quality matters. The system demonstrates competitive performance on standard speech benchmarks while maintaining higher audio fidelity on subjective quality assessments.

**Relevance to Music Attribution:**
When discussing music -- specific recordings, production techniques, or audio fingerprinting results -- codec compression artifacts could distort the very acoustic details being discussed. A codec-free architecture preserves the full audio spectrum, which matters when the voice agent needs to reference or play back specific audio segments during attribution discussions. The simultaneous listen-and-speak capability also supports the "interrupt to correct" workflow essential for attribution review.

---

### 1.6 LLaMA-Omni 2

| Field | Details |
|-------|---------|
| **Title** | LLaMA-Omni 2: LLM-based Streaming Speech Synthesis |
| **Authors** | Meta AI / LLaMA-Omni Team |
| **Date** | May 2025 |
| **Link** | [arXiv:2505.02625](https://arxiv.org/abs/2505.02625) |

**Key Findings:**
LLaMA-Omni 2 extends the LLaMA architecture with autoregressive streaming speech synthesis capabilities. Built on the open-source LLaMA foundation, the model can generate speech token-by-token in a streaming fashion, enabling low-latency response initiation. The architecture uses a shared text-speech vocabulary with special boundary tokens, allowing seamless transitions between text reasoning and speech generation within the same forward pass. The model achieves competitive quality on speech benchmarks while remaining fully open-source (weights, training code, and data pipeline). Training uses a three-stage curriculum: text pretraining, speech-text alignment, and conversational fine-tuning.

**Relevance to Music Attribution:**
As an open-source alternative to proprietary solutions like GPT-4o-audio, LLaMA-Omni 2 provides a self-hostable option for attribution voice agents. This is significant for the "bowling-shoe" vs. "BYO" archetype distinction in the manuscript: teams that need full control over their inference pipeline (e.g., for data sovereignty or cost reasons) can deploy LLaMA-Omni 2 on their own infrastructure. The streaming synthesis capability ensures acceptable latency even on modest hardware.

---

### 1.7 OpenAI gpt-4o-realtime and Realtime API

| Field | Details |
|-------|---------|
| **Title** | OpenAI Realtime API (gpt-4o-realtime-preview) |
| **Authors** | OpenAI |
| **Date** | September 2025 (major update) |
| **Link** | [OpenAI Documentation](https://platform.openai.com/docs/guides/realtime) |

**Key Findings:**
The September 2025 update to OpenAI's Realtime API introduced significant improvements: 18.6 percentage-point improvement in instruction-following accuracy and 12.9 percentage-point improvement in tool-calling reliability. The API supports both WebSocket and WebRTC transport protocols, with WebRTC enabling direct browser-to-server audio streaming without intermediary servers. The 32K context window allows maintaining extended conversation history, and the updated tool-calling mechanism supports parallel function execution with structured JSON outputs. Pricing remains at approximately $0.06/min input and $0.24/min output for audio, with a 100-token minimum per turn.

**Relevance to Music Attribution:**
The improved tool-calling capability is directly applicable to the attribution use case. During a voice conversation, the agent can invoke MusicBrainz lookups, ISRC registry queries, and confidence score computations as structured tool calls -- all within the conversational flow. The WebRTC transport eliminates the need for a transcription intermediary, reducing latency and infrastructure complexity. However, the cost structure ($0.30/min blended) makes this viable only for the Pro tier, not for free-tier users. The 32K context window is sufficient to maintain the full attribution history for a typical album review session.

---

## 2. Speech Synthesis Quality and Evaluation

Evaluating TTS quality for a voice agent requires both objective metrics and understanding of how synthesis quality affects user trust -- particularly important when the agent is communicating confidence scores and attribution certainty.

### 2.1 TTSDS2: Robust Objective TTS Evaluation

| Field | Details |
|-------|---------|
| **Title** | TTSDS2: A Robust Benchmark for Text-to-Speech Evaluation |
| **Authors** | TTSDS Consortium |
| **Date** | SSW 2025 (Speech Synthesis Workshop) |
| **Link** | SSW 2025 proceedings |

**Key Findings:**
TTSDS2 establishes a comprehensive evaluation framework that benchmarks five major objective speech quality metrics: UTMOS, UTMOSv2, NISQA, DNSMOS, and SQUIM MOS. The paper demonstrates that no single metric captures all dimensions of speech quality -- UTMOS excels at naturalness but misses intelligibility issues, while DNSMOS better captures environmental noise artifacts. The framework proposes a composite scoring approach that weights metrics differently based on the deployment context. For voice assistants specifically, the authors recommend a naturalness-weighted composite with intelligibility as a hard constraint (minimum threshold rather than soft weight). The benchmark includes 15,000 synthesized utterances across 12 TTS systems, with human MOS scores as ground truth.

**Relevance to Music Attribution:**
When the voice agent communicates attribution confidence ("I'm 87% confident that the songwriter is..."), the quality of the synthesis directly affects how much the user trusts the information. A robotic or unnatural voice undermines confidence in the data itself. TTSDS2 provides the evaluation framework to select and monitor TTS quality for the attribution agent, with the naturalness-weighted composite being the most appropriate metric for a premium voice feature targeting professional musicians.

---

### 2.2 Good Practices for TTS Evaluation

| Field | Details |
|-------|---------|
| **Title** | Good Practices for Evaluation of Text-to-Speech Systems |
| **Authors** | TTS Evaluation Working Group |
| **Date** | March 2025 |
| **Link** | [arXiv:2503.03250](https://arxiv.org/abs/2503.03250) |

**Key Findings:**
This paper provides a methodological guide for TTS evaluation, covering Mean Opinion Score (MOS) testing protocols, MUSHRA (MUltiple Stimuli with Hidden Reference and Anchor) experimental design, and common pitfalls that invalidate results. Key recommendations include: minimum 30 listeners for statistically significant MOS results, anchor stimuli calibration for cross-study comparability, and Latin-square designs to control for listener fatigue. The paper identifies several persistent pitfalls: cherry-picking test utterances, using text-only metrics as proxies for speech quality, and failing to control for playback conditions. The authors also address the growing practice of using LLM-based evaluators as MOS proxies, finding that current LLM judges correlate at r=0.72 with human MOS -- useful for development but insufficient for publication-quality evaluation.

**Relevance to Music Attribution:**
For a music-industry-facing product, evaluation rigor matters. Musicians have trained ears and will notice synthesis artifacts that general users might miss. This paper provides the evaluation protocol for selecting and benchmarking the voice agent's TTS component, ensuring that quality assessments are methodologically sound rather than based on informal listening tests.

---

### 2.3 Multi-Sampling-Frequency MOS Prediction

| Field | Details |
|-------|---------|
| **Title** | MSR-UTMOS: Multi-Sampling-Rate Naturalness MOS Prediction |
| **Authors** | AudioMOS Challenge 2025 participants |
| **Date** | July 2025 |
| **Link** | [arXiv:2507.14647](https://arxiv.org/abs/2507.14647) |

**Key Findings:**
MSR-UTMOS addresses a gap in TTS evaluation: most MOS prediction models are trained and evaluated at a single sampling rate (typically 16kHz), but production voice agents operate across different quality contexts -- 16kHz for telephony, 24kHz for standard web audio, and 48kHz for high-fidelity applications. The model achieves consistent MOS prediction accuracy across all three sampling rates, with Pearson correlation above 0.90 at each frequency. A key finding is that naturalness perception is not linearly related to sampling rate: the jump from 16kHz to 24kHz produces a larger perceptual improvement than 24kHz to 48kHz, suggesting that 24kHz is the optimal quality-cost trade-off for most voice agent deployments.

**Relevance to Music Attribution:**
Attribution voice agents will operate in varied audio quality contexts: a browser-based web app (24-48kHz), a mobile app on cellular data (16kHz), or integration with DAW software (48kHz). MSR-UTMOS provides the evaluation framework to ensure consistent voice quality assessment across these contexts. The finding that 24kHz is the perceptual sweet spot informs the default audio configuration for the attribution agent.

---

### 2.4 Prosody and Intelligibility Metrics Beyond MOS

| Field | Details |
|-------|---------|
| **Title** | Objective Metrics for Prosody and Intelligibility in Synthesized Speech |
| **Authors** | Prosody Metrics Research Group |
| **Date** | September 2025 |
| **Link** | [arXiv:2509.20485](https://arxiv.org/abs/2509.20485) |

**Key Findings:**
This paper goes beyond MOS to propose objective metrics for specific prosodic dimensions: rhythm regularity, lexical stress accuracy, intonation contour matching, and phrase boundary placement. The authors demonstrate that these fine-grained metrics capture quality differences that MOS scores flatten. Specifically, two TTS systems with identical MOS scores (4.2) showed significantly different performance on stress accuracy (0.91 vs. 0.78), which affected listener comprehension in information-dense utterances. The paper proposes a hierarchical evaluation framework: MOS as a coarse filter, then prosodic metrics for nuanced comparison between systems that pass the MOS threshold. Intelligibility metrics include character error rate in noise (CER-N) and information retrieval accuracy from spoken passages.

**Relevance to Music Attribution:**
Attribution responses are information-dense: artist names (often non-English), role descriptions, confidence percentages, and ISRC codes. Prosodic quality directly affects whether these details are correctly perceived. The stress accuracy metric is particularly relevant -- mispronouncing artist names or misplacing stress in confidence statements ("EIGHTY-seven percent" vs. "eighty-SEVEN percent") changes the perceived meaning. This paper provides the evaluation criteria for selecting a TTS system that handles attribution-specific utterances well.

---

## 3. Voice Cloning Ethics and Safety

Voice AI in the music industry carries heightened ethical stakes -- artists' voices are their creative identity, and unauthorized voice cloning threatens both economic rights and personal autonomy. These papers address the detection, prevention, and governance of voice synthesis.

### 3.1 ASVspoof 5: Anti-Spoofing and Deepfake Detection

| Field | Details |
|-------|---------|
| **Title** | ASVspoof 5: Crowdsourced Speech Data, Deepfakes, and Adversarial Attacks at Scale |
| **Authors** | ASVspoof Consortium |
| **Date** | 2025 |
| **Link** | [ScienceDirect](https://doi.org/10.1016/j.csl.2024.101723) |

**Key Findings:**
ASVspoof 5 is the largest spoofing and deepfake detection challenge dataset to date, featuring 32 different attack algorithms including the latest neural codec-based synthesis, voice conversion, and adversarial perturbation methods. The dataset uses crowdsourced data (rather than studio-quality recordings) to better represent real-world conditions. Key findings include: (1) state-of-the-art detection systems achieve 95%+ accuracy on known attack types but degrade to 70-80% on adversarial attacks specifically designed to evade detection; (2) codec-based attacks (using EnCodec, SoundStream) are harder to detect than traditional vocoder-based synthesis; (3) ensemble detectors combining spectral, temporal, and embedding-based features achieve the most robust performance. The challenge also introduces a new "partially fake" track where only segments of an utterance are synthesized.

**Relevance to Music Attribution:**
For A2/A3 assurance levels in the attribution framework, voice-authorized submissions must be verified as genuine. ASVspoof 5's findings directly inform the design of voice verification in the attribution pipeline: the detection system must handle adversarial attacks (someone submitting a cloned voice to claim authorship), and the "partially fake" scenario maps to real-world cases where an artist's genuine vocal recording might be spliced with synthesized segments. The degradation on adversarial attacks (95% to 70-80%) highlights the Oracle Problem -- detection is not binary certainty but probabilistic confidence.

---

### 3.2 Audio Deepfake Detection: A Comprehensive Survey

| Field | Details |
|-------|---------|
| **Title** | Audio Deepfake Detection: A Comprehensive Survey of Methods and Challenges |
| **Authors** | Audio Deepfake Detection Survey Group |
| **Date** | 2025 |
| **Link** | [PMC (PubMed Central)](https://pmc.ncbi.nlm.nih.gov/) |

**Key Findings:**
This survey categorizes audio deepfake detection methods into three families: (1) watermarking-based approaches that embed imperceptible signals during synthesis and verify their presence/absence during detection; (2) ML classifier approaches that train discriminative models on spectral, prosodic, and embedding features; and (3) forensic spectral analysis that identifies synthesis artifacts in the frequency domain. A critical finding is that detection models require frequent retraining as synthesis technology improves -- a model trained on 2024-era synthesis achieves only 65% accuracy on 2025-era outputs. The survey also identifies a fundamental asymmetry: synthesis requires only one successful method, while detection must defend against all methods. Ensemble approaches combining all three families achieve the highest robustness but at significant computational cost.

**Relevance to Music Attribution:**
The finding that detection requires continuous retraining is directly relevant to the attribution agent's design: any voice verification component must be treated as a continuously updated service, not a static model. The watermarking approach is the most promising for the attribution use case because it operates proactively (embed at creation) rather than reactively (detect after the fact), aligning with the "attribution-by-design" philosophy. The forensic spectral analysis methods provide fallback detection for audio submitted without watermarks.

---

### 3.3 PRAC3: Privacy, Reputation, Accountability, Consent, Credit, Compensation

| Field | Details |
|-------|---------|
| **Title** | PRAC3: Expanding the C3 Framework for Voice AI Ethics -- Privacy, Reputation, Accountability, Consent, Credit, Compensation |
| **Authors** | PRAC3 Working Group |
| **Date** | July 2025 |
| **Link** | [arXiv:2507.16247](https://arxiv.org/abs/2507.16247) |

**Key Findings:**
PRAC3 extends the earlier C3 framework (Consent, Credit, Compensation) with three additional dimensions: Privacy (control over biometric voice data), Reputation (preventing association with unwanted content), and Accountability (traceable provenance chains). The study includes interviews with 20 professional voice actors and analyzes two landmark legal cases: voice actors' class-action suit against TikTok for unauthorized voice cloning, and individual lawsuits against OpenAI for using actors' voices without consent. Key findings: (1) voice actors unanimously ranked Consent as the top priority, above Compensation; (2) Credit was considered important but operationally difficult -- current platforms lack metadata fields for voice attribution; (3) Accountability mechanisms (who used my voice, where, when) were considered the minimum viable governance requirement. The paper proposes a governance matrix mapping PRAC3 dimensions to technical enforcement mechanisms.

**Relevance to Music Attribution:**
PRAC3 maps almost perfectly onto the A0-A3 assurance framework from the manuscript. Credit corresponds to attribution metadata (ISRC, ISWC, ISNI). Compensation maps to royalty chain tracking. Consent aligns with MCP permission queries -- the voice agent can serve as the interface for artists to set and query their consent preferences. Accountability maps to provenance audit trails. The finding that Consent outranks Compensation validates the design decision to build consent infrastructure (MCP permission patchbay) before royalty tracking. The PRAC3 governance matrix provides a ready-made framework for mapping the attribution agent's capabilities to ethical requirements.

---

### 3.4 EU AI Act Article 50: Transparency Obligations

| Field | Details |
|-------|---------|
| **Title** | EU AI Act (Regulation 2024/1689), Article 50: Transparency obligations for certain AI systems |
| **Authors** | European Parliament and Council |
| **Date** | Enforcement phased through August 2026 |
| **Link** | [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1689) |

**Key Findings:**
Article 50 of the EU AI Act mandates specific transparency requirements for AI systems that generate synthetic audio, video, or text content. Key provisions: (1) AI systems that interact with natural persons must disclose that they are AI-powered, unless this is obvious from the context; (2) synthetic audio content must be labeled as artificially generated using machine-readable technical standards; (3) providers must ensure that labeling is robust against removal. The transparency obligations apply to the deployer (not just the developer), meaning any organization deploying a voice AI agent in the EU must ensure compliance. Enforcement begins in phases, with AI system disclosure requirements active from August 2025 and synthetic content labeling from August 2026.

**Relevance to Music Attribution:**
The voice attribution agent must identify itself as AI-powered at the start of every interaction. Synthetic audio generated by the TTS component must carry machine-readable labels. This has direct design implications: the agent's greeting must include a disclosure ("I'm an AI attribution assistant"), and all generated audio outputs must embed C2PA-compatible provenance markers (see Section 3.5). For the digital twin use case -- where the agent mimics an artist's voice -- the disclosure requirements are even more stringent, as users might reasonably believe they're interacting with the actual artist.

---

### 3.5 C2PA Content Credentials for Audio

| Field | Details |
|-------|---------|
| **Title** | C2PA (Coalition for Content Provenance and Authenticity) Specifications 2.1-2.3 |
| **Authors** | C2PA Consortium (Adobe, Microsoft, BBC, Sony, others) |
| **Date** | 2025 (specifications 2.1 through 2.3) |
| **Link** | [C2PA Specification](https://c2pa.org/specifications/) |

**Key Findings:**
The C2PA 2.1-2.3 specifications extend content provenance to audio as a first-class content type. The technical approach combines three layers: (1) cryptographic hashing that creates a tamper-evident binding between content and metadata; (2) optional watermarking that survives format conversion and compression; and (3) fingerprinting for matching content even after modification. The specifications are on a fast track toward ISO standardization. Key technical details: the manifest store uses JUMBF (JPEG Universal Metadata Box Format) extended for audio containers (WAV, FLAC, MP3, AAC); the cryptographic binding uses SHA-256 with X.509 certificate chains; and the watermarking layer supports both audible (for human verification) and inaudible (for machine verification) modes. The specifications also define "ingredient" relationships, allowing provenance tracking through remix and derivative work chains.

**Relevance to Music Attribution:**
C2PA directly addresses the Oracle Problem described in the manuscript: digital systems cannot fully verify physical/training reality, but cryptographic binding creates strong evidence chains. For the voice agent, C2PA provides: (1) provenance markers on the agent's own speech output (meeting EU AI Act requirements); (2) verification of submitted audio claims ("this recording proves I performed on this track"); and (3) chain-of-custody tracking through remix and derivative work attribution. The "ingredient" relationship model is particularly powerful for music, where a single track may incorporate dozens of contributors' work. C2PA credentials can be embedded at creation time (attribution-by-design) rather than added post-hoc.

---

## 4. Turn-Taking in Voice AI

Turn-taking -- the mechanism by which conversation participants negotiate who speaks when -- is critical for voice agents. Poor turn-taking creates the frustrating experience of being interrupted or waiting in silence. For attribution workflows where users need to rapidly approve, reject, or modify suggestions, turn-taking must be precise.

### 4.1 Voice Activity Projection (VAP)

| Field | Details |
|-------|---------|
| **Title** | Voice Activity Projection: Self-Supervised Learning of Turn-Taking Events / Multimodal Voice Activity Projection |
| **Authors** | VAP Research Group |
| **Date** | January 2024 (arXiv:2401.04868), June 2025 (arXiv:2506.03980, multimodal extension) |
| **Link** | [arXiv:2401.04868](https://arxiv.org/abs/2401.04868), [arXiv:2506.03980](https://arxiv.org/abs/2506.03980) |

**Key Findings:**
Voice Activity Projection (VAP) predicts speaker activity over the next 2 seconds using cross-attention Transformers operating on audio features. The original 2024 model operates on audio-only input and achieves state-of-the-art turn-taking prediction on the Switchboard and Fisher corpora. The model runs in real-time on CPU (no GPU required), making it deployable as a lightweight preprocessing stage. The 2025 multimodal extension (arXiv:2506.03980) adds visual signals -- facial expressions, lip movements, gaze direction -- to improve prediction in video-call contexts. The multilingual evaluation covers English, Chinese, and Japanese, demonstrating that turn-taking patterns transfer across languages with modest adaptation. A key architectural insight: the 2-second prediction horizon balances responsiveness (reacting to turn boundaries) with anticipation (predicting upcoming turns before they occur).

**Relevance to Music Attribution:**
For the attribution review workflow -- where users rapidly approve or reject suggestions -- VAP enables the agent to anticipate when the user is about to respond ("approved" / "skip" / "let me correct that"). The CPU-only operation is critical because the voice agent's GPU resources should be dedicated to LLM inference and TTS synthesis, not consumed by a turn-taking model. The 2-second prediction horizon allows the agent to prepare attribution data for the next item while the user is still finishing their response to the current one.

---

### 4.2 Krisp Turn-Taking v1 and v2

| Field | Details |
|-------|---------|
| **Title** | Krisp Turn-Taking Models v1 and v2 |
| **Authors** | Krisp AI |
| **Date** | 2025 |
| **Link** | [Krisp AI Research](https://krisp.ai/research/) |

**Key Findings:**
Krisp's turn-taking models are purpose-built for production voice agents, prioritizing computational efficiency over academic benchmarks. The v1 model uses a lightweight CNN architecture (6M parameters) that operates entirely on audio features -- no transcription required. This is a critical design decision: by avoiding dependency on an ASR pipeline, the turn-taking prediction is not bottlenecked by transcription latency. The v2 model refines the architecture with attention pooling and achieves 94% accuracy on end-of-turn prediction while maintaining CPU-only deployment. Both models are trained on a proprietary dataset of 50,000+ hours of real voice agent interactions (not read speech or scripted conversations), which the authors argue better represents the actual distribution of turn-taking patterns in production systems.

**Relevance to Music Attribution:**
Krisp's models are the most deployment-ready turn-taking solution for the attribution voice agent. The audio-only operation (no text pipeline dependency) means turn-taking prediction runs independently of the ASR/LLM pipeline, enabling the agent to detect turn boundaries even before transcription completes. The 6M parameter count ensures the model does not compete for computational resources with the main voice pipeline. The training on real voice agent interactions (rather than human-human conversation) better matches the interaction patterns expected in attribution workflows.

---

### 4.3 Turn-Taking Survey (IWSDS 2025)

| Field | Details |
|-------|---------|
| **Title** | A Survey of Turn-Taking Models for Spoken Dialogue Systems |
| **Authors** | IWSDS 2025 Workshop Group |
| **Date** | 2025 |
| **Link** | [ACL Anthology / IWSDS 2025](https://aclanthology.org/) |

**Key Findings:**
This survey provides a comprehensive taxonomy of turn-taking models for spoken dialogue systems, covering three generations: rule-based (silence threshold), statistical (TurnGPT, VAP), and end-to-end neural approaches. The paper evaluates each approach on four dimensions: end-of-turn prediction accuracy, backchannel detection rate, overlap handling capability, and computational cost. Key findings: (1) silence-threshold approaches (the industry default) achieve only 72% accuracy because they cannot distinguish thinking pauses from turn yields; (2) TurnGPT (text-based) achieves 89% but adds ASR latency; (3) VAP (audio-based) achieves 91% without ASR dependency; (4) end-to-end models in full-duplex systems (like Moshi) implicitly learn turn-taking but cannot be independently tuned. The survey recommends hybrid approaches: a fast audio-based detector for initial response, refined by text-based analysis once transcription is available.

**Relevance to Music Attribution:**
The survey's recommendation of hybrid turn-taking aligns with the tandem architecture from KAME (Section 1.2). For the attribution agent, this means: Krisp-style audio detection for immediate turn boundary response, refined by LLM-based understanding of the semantic content. The finding that silence thresholds achieve only 72% accuracy validates investing in proper turn-taking rather than relying on simple timeout-based approaches, which would create a frustrating experience during attribution review sessions.

---

### 4.4 Interruption Handling in Voice Agents

| Field | Details |
|-------|---------|
| **Title** | Distinguishing Genuine Interruptions from Collaborative Overlap in Conversational AI |
| **Authors** | Interruption Handling Research Group |
| **Date** | January 2025 |
| **Link** | [arXiv:2501.01568](https://arxiv.org/abs/2501.01568) |

**Key Findings:**
This paper addresses a nuanced challenge in voice agent interaction: distinguishing between genuine interruptions (the user wants the agent to stop and change direction) and collaborative overlap (backchannels like "right", "okay", "yes" that indicate engagement without requesting a turn change). The authors identify prosodic, temporal, and semantic features that differentiate these two overlap types. Genuine interruptions typically feature rising pitch, increased volume, and semantic content that contradicts or redirects the current topic. Collaborative overlaps have flat or falling pitch, lower volume, and semantically supportive content. A classifier trained on these features achieves 88% accuracy in distinguishing the two types. The paper also proposes response strategies: genuine interruptions trigger immediate stop-and-listen, while collaborative overlaps are acknowledged but do not halt the agent's response.

**Relevance to Music Attribution:**
During batch attribution review, users will frequently produce collaborative overlaps ("mm-hmm", "okay", "next") to keep the review moving, interspersed with genuine interruptions ("wait, that's wrong" or "go back"). Misclassifying a collaborative overlap as an interruption would halt the review flow; misclassifying an interruption as overlap would cause the agent to ignore a correction. The 88% classification accuracy provides a baseline, with the attribution context providing additional disambiguation signal (e.g., "wrong" and "go back" are strong interruption indicators regardless of prosody).

---

## 5. Multimodal Voice Agents

Multimodal agents combine voice with visual and textual modalities, enabling richer interaction patterns for attribution workflows.

### 5.1 GLM-4-Voice (Zhipu AI)

| Field | Details |
|-------|---------|
| **Title** | GLM-4-Voice: Towards Intelligent and Human-Like End-to-End Spoken Chatbot |
| **Authors** | Zhipu AI |
| **Date** | December 2024 (arXiv), updated through 2025 |
| **Link** | [arXiv:2412.02612](https://arxiv.org/abs/2412.02612) |

**Key Findings:**
GLM-4-Voice is a half-duplex but knowledge-rich spoken dialogue model. While it cannot handle simultaneous speech (only one party speaks at a time), it compensates with strong factual knowledge and reasoning capabilities inherited from the GLM-4 text foundation model. The model supports streaming speech-to-speech interaction with 400ms latency. A notable feature is the model's ability to control its own speech characteristics -- speed, emotion, accent -- through natural language instructions embedded in the system prompt. The model achieves the highest accuracy on knowledge-intensive spoken QA benchmarks among open-source models, outperforming several full-duplex competitors that sacrifice knowledge depth for conversational responsiveness.

**Relevance to Music Attribution:**
The half-duplex limitation is acceptable for structured attribution queries where turn-taking is naturally sequential ("Tell me about this track" / [response] / "What's the confidence?" / [response]). The strong knowledge capabilities make GLM-4-Voice a candidate for the back-end knowledge model in a KAME-style tandem architecture, where conversational responsiveness is handled by a separate front-end. The controllable speech characteristics could be used to vary voice properties based on confidence level -- speaking more slowly and clearly for low-confidence attributions that require careful human review.

---

### 5.2 Mini-Omni2

| Field | Details |
|-------|---------|
| **Title** | Mini-Omni2: Towards Open-source GPT-4o with Vision, Speech and Duplex Capabilities |
| **Authors** | Mini-Omni Research Team |
| **Date** | October 2024 (arXiv:2410.11190), updated 2025 |
| **Link** | [arXiv:2410.11190](https://arxiv.org/abs/2410.11190) |

**Key Findings:**
Mini-Omni2 combines vision, speech, and duplex conversational capabilities in an open-source package. The model can process visual input (images, video frames) alongside audio, enabling interactions like "look at this and tell me about it." The duplex capability allows the model to process new visual or audio input while generating a response. The architecture uses a shared multimodal encoder that projects visual and audio features into a common representation space, with modality-specific adapters. The model is significantly smaller than commercial alternatives (3B parameters vs. GPT-4o's estimated 200B+), which limits its knowledge depth but enables edge deployment.

**Relevance to Music Attribution:**
The vision + speech combination enables a powerful attribution workflow: a user could point their phone at a vinyl record, CD booklet, or concert poster, and ask "who played keyboards on this album?" The visual input provides context (album art, liner notes) that the speech-only agent would lack. While the model's knowledge depth may be insufficient for comprehensive attribution, it could serve as the multimodal front-end in a tandem architecture, routing visual context to a more capable back-end attribution engine.

---

### 5.3 CHI 2025: Prompting Embodied AI Agents

| Field | Details |
|-------|---------|
| **Title** | Prompting and Communicating with Embodied AI Agents |
| **Authors** | CHI 2025 Study Group (39 adult participants with Furhat robot) |
| **Date** | CHI 2025 |
| **Link** | [ACM Digital Library](https://dl.acm.org/) |

**Key Findings:**
This study examined how 39 adults adapted their communication style when interacting with an embodied AI agent (Furhat robot). Key findings: (1) users converged toward shorter, more directive utterances over the course of a session (from 12.3 words/utterance initially to 7.8 after 10 minutes); (2) users who were told the agent was "AI-powered" used 23% fewer hedging expressions and 31% more direct commands compared to users told it was "human-assisted"; (3) communication style adaptation was not uniform -- users with technical backgrounds adapted faster but plateau at a less natural communication style; (4) embodied presence (physical robot vs. screen avatar vs. voice-only) significantly affected trust ratings but not task completion accuracy. The study proposes design guidelines for AI agent communication: support both verbose and terse interaction styles, provide progressive feedback to guide users toward efficient interaction patterns.

**Relevance to Music Attribution:**
The finding that users naturally converge toward shorter, more directive utterances is directly relevant to attribution review workflow design. The voice agent should support both verbose queries ("Can you tell me who the session musicians were on track three of this album?") and terse commands ("track three, musicians"), with the interface naturally guiding users toward efficient patterns. The EU AI Act disclosure requirement (Section 3.4) means the agent must identify as AI-powered, which this study suggests will actually improve interaction efficiency as users adopt more direct communication styles.

---

## 6. Voice AI Evaluation Frameworks

Evaluating voice agents for the attribution use case requires benchmarks that test both conversational quality and task-specific capabilities (tool use, knowledge retrieval, multi-turn reasoning).

### 6.1 VoiceAssistant-Eval

| Field | Details |
|-------|---------|
| **Title** | VoiceAssistant-Eval: A Comprehensive Evaluation Framework for Voice Assistants |
| **Authors** | VoiceAssistant-Eval Team |
| **Date** | September 2025 |
| **Link** | [arXiv:2509.22651](https://arxiv.org/abs/2509.22651) |

**Key Findings:**
VoiceAssistant-Eval introduces a benchmark of 10,497 examples across 13 task categories, including knowledge QA, instruction following, tool invocation, multi-turn dialogue management, and error recovery. The benchmark uses both automatic metrics (task completion, factual accuracy, response latency) and LLM-based judges (coherence, helpfulness, safety). A key finding is that proprietary models do not universally outperform open-source alternatives: while GPT-4o leads on knowledge QA and tool invocation, open-source models (Moshi, LLaMA-Omni) outperform on conversational naturalness and response latency. The benchmark also reveals a quality cliff in multi-turn interactions: all models degrade significantly after 5+ turns, with factual accuracy dropping 15-30% by turn 10.

**Relevance to Music Attribution:**
The multi-turn degradation finding is critical for attribution review sessions, which may involve reviewing 10-15 tracks in a single session. The voice agent must maintain attribution accuracy across extended interactions, not just in the first few turns. The task category breakdown (knowledge QA, tool invocation, error recovery) maps well to attribution workflows: knowledge QA for answering "who wrote this?", tool invocation for querying MusicBrainz, and error recovery for handling "that's incorrect, the actual songwriter is...". The finding that open-source models match or exceed proprietary models on naturalness supports the viability of a self-hosted attribution agent for the "BYO" archetype.

---

### 6.2 VoiceAgentBench

| Field | Details |
|-------|---------|
| **Title** | VoiceAgentBench: Benchmarking Agentic Capabilities of Voice AI |
| **Authors** | VoiceAgentBench Consortium |
| **Date** | October 2025 |
| **Link** | [arXiv:2510.07978](https://arxiv.org/abs/2510.07978) |

**Key Findings:**
VoiceAgentBench is the first benchmark specifically designed for agentic voice capabilities -- voice AI that takes actions in the world rather than just answering questions. The benchmark includes 6,000+ spoken queries across 7 languages, covering tool invocation, API calling, multi-step reasoning, and state management across conversation turns. A critical finding: cascaded ASR-LLM pipelines (transcribe first, then reason) outperform end-to-end Speech Language Models (SpeechLMs) by a significant margin -- 60.6% task completion for the best SpeechLM vs. 78.3% for the best cascaded pipeline. The gap is largest on tool invocation tasks, where precise parameter extraction is essential. The authors attribute this to the information loss in speech tokenization: discrete audio tokens discard fine-grained semantic distinctions that text tokens preserve.

**Relevance to Music Attribution:**
The attribution voice agent is inherently agentic: it must invoke MusicBrainz APIs, query ISRC registries, compute confidence scores, and update attribution records -- all through voice interaction. VoiceAgentBench's finding that cascaded pipelines outperform end-to-end SpeechLMs by nearly 18 percentage points on agentic tasks strongly favors a cascaded architecture for the attribution agent. Precise parameter extraction (ISRC codes, artist names, work identifiers) cannot tolerate the information loss that speech tokenization introduces. This validates the KAME tandem approach (Section 1.2) where a text-based LLM handles the agentic reasoning while a speech model handles the conversational interface.

---

### 6.3 Testing the Testers: Meta-Evaluation of Voice AI Platforms

| Field | Details |
|-------|---------|
| **Title** | Testing the Testers: A Meta-Evaluation of Voice AI Testing Platforms |
| **Authors** | Meta-Evaluation Research Group |
| **Date** | November 2025 |
| **Link** | [arXiv:2511.04133](https://arxiv.org/abs/2511.04133) |

**Key Findings:**
This paper evaluates the evaluation platforms themselves -- a meta-problem that has been largely ignored. The study collects 21,600 human judgments to benchmark seven commercial and academic voice AI testing platforms. The top-performing platform (Evalion) achieves 0.92 F1 on response quality assessment, but simulation quality (generating realistic test conversations) scores only 0.61. This reveals a critical gap: platforms are good at evaluating responses to well-formed queries but poor at generating the messy, ambiguous, interrupted, and context-dependent queries that real users produce. The paper identifies specific failure modes: synthetic test voices lack natural hesitation patterns, test scenarios underrepresent error recovery situations, and multi-turn test dialogues are unrealistically coherent.

**Relevance to Music Attribution:**
The simulation quality gap (0.92 evaluation vs. 0.61 generation) means that standard voice AI testing platforms will underestimate real-world failure modes for the attribution agent. Attribution queries are particularly prone to the identified failure modes: users will hesitate over artist names they're unsure of, interrupt to correct themselves, and produce queries that mix natural language with domain-specific identifiers. Testing the attribution agent requires custom test scenarios that capture these patterns, not reliance on generic voice AI testing platforms.

---

### 6.4 VCB Bench: Real Human Speech Evaluation

| Field | Details |
|-------|---------|
| **Title** | VCB Bench: Voice Chatbot Benchmark Built on Real Human Speech |
| **Authors** | VCB Research Team |
| **Date** | October 2025 |
| **Link** | [arXiv:2510.11098](https://arxiv.org/abs/2510.11098) |

**Key Findings:**
VCB Bench distinguishes itself from other voice AI benchmarks by using exclusively real human speech recordings rather than TTS-generated test queries. This methodological choice captures acoustic phenomena that synthetic speech lacks: ambient noise, microphone variation, non-native accents, emotional coloring, and natural disfluencies. The benchmark evaluates robustness under controlled perturbations: background noise (office, street, music), reverberation, codec compression, and bandwidth limitation. Key finding: model performance degrades 12-25% under realistic noise conditions compared to clean speech evaluation, with background music causing the largest degradation (25% for models without music-aware preprocessing). The benchmark includes 4,200 utterances from 380 speakers across 12 accents.

**Relevance to Music Attribution:**
Attribution agents will frequently operate in noisy environments -- recording studios with monitors playing, live venues, or casual settings with background music. The 25% degradation with background music is particularly concerning since music attribution queries often occur in the presence of the music being discussed. VCB Bench's real-speech methodology provides the most realistic evaluation framework for the attribution agent, and its noise robustness metrics should be primary selection criteria for the ASR component. The accent diversity (12 accents, 380 speakers) is also relevant given the global nature of music attribution.

---

### 6.5 MULTI-Bench: Emotional Intelligence in Multi-Turn Dialogue

| Field | Details |
|-------|---------|
| **Title** | MULTI-Bench: Emotional Intelligence Benchmark for Multi-Turn Spoken Dialogue |
| **Authors** | MULTI-Bench Research Group |
| **Date** | November 2025 |
| **Link** | [arXiv:2511.00850](https://arxiv.org/abs/2511.00850) |

**Key Findings:**
MULTI-Bench is the first benchmark specifically targeting emotional intelligence in multi-turn spoken dialogue. The benchmark includes 3,200 dialogue samples across two tracks: a basic track evaluating emotion recognition and appropriate response generation, and an advanced track evaluating empathetic response, emotional de-escalation, and sentiment-aware conversation steering. Key findings: (1) current models achieve 78% accuracy on basic emotion recognition from speech but only 45% on generating contextually appropriate empathetic responses; (2) multi-turn emotional consistency (maintaining appropriate affect across a conversation) drops significantly after 3 turns; (3) the gap between text-based emotional understanding and speech-based performance is smaller than expected (8% vs. the 15-20% typically reported), suggesting that speech features add modest but meaningful signal.

**Relevance to Music Attribution:**
Attribution disputes can be emotionally charged -- an artist discovering their contribution was uncredited, a producer disagreeing with confidence scores, or a rights holder frustrated by incorrect metadata. The voice agent must handle these emotional contexts appropriately, not with robotic neutrality but with calibrated empathy. MULTI-Bench's finding that empathetic response generation lags far behind emotion recognition (45% vs. 78%) suggests that the attribution agent should focus on emotion detection (to flag sensitive interactions) rather than attempting to generate empathetic responses, which risk sounding patronizing or insincere.

---

### 6.6 Audio MultiChallenge

| Field | Details |
|-------|---------|
| **Title** | Audio MultiChallenge: Comprehensive Evaluation of Audio Understanding |
| **Authors** | Audio MultiChallenge Consortium |
| **Date** | December 2025 |
| **Link** | [arXiv:2512.14865](https://arxiv.org/abs/2512.14865) |

**Key Findings:**
Audio MultiChallenge evaluates audio understanding across multiple axes: speech comprehension, environmental sound recognition, music understanding, audio reasoning, and voice editing. The benchmark reveals that even the best model (Gemini 3 Pro Preview) achieves only 54.65% overall pass rate, with voice editing being the most challenging axis (32% pass rate). Music understanding scores higher (61%) but still demonstrates significant gaps in tasks requiring fine-grained audio analysis -- identifying specific instruments, estimating tempo, or recognizing production techniques. The benchmark also tests cross-modal reasoning: answering questions that require integrating audio features with textual knowledge, where performance drops to 41%.

**Relevance to Music Attribution:**
The 61% music understanding score highlights a fundamental limitation: current audio AI models cannot reliably perform the kind of fine-grained audio analysis that music attribution sometimes requires (e.g., identifying a specific guitarist's playing style from a recording). This reinforces the scaffold's approach of using structured metadata and human-in-the-loop verification rather than relying on AI audio analysis for attribution. The voice agent should be designed to communicate these limitations transparently -- "Based on the metadata, the guitarist is likely X, but I cannot confirm this from the audio alone."

---

### 6.7 ICASSP 2026 HumDial Challenge

| Field | Details |
|-------|---------|
| **Title** | ICASSP 2026 Human-Like Dialogue Challenge (HumDial) |
| **Authors** | ICASSP 2026 HumDial Organizers |
| **Date** | January 2026 |
| **Link** | [arXiv:2601.05564](https://arxiv.org/abs/2601.05564) |

**Key Findings:**
The HumDial Challenge attracted 100+ teams with 15 valid final submissions across two tracks: Emotional Intelligence (EI) and Full-Duplex Interaction (FDI). The EI track evaluated models on recognizing, interpreting, and responding to emotional cues in spoken dialogue. The FDI track evaluated simultaneous speech handling, backchannel generation, and interruption management. Key finding: emotion analysis (recognition + interpretation) is advancing faster than empathetic generation -- the best EI-track system achieved 82% on analysis but only 51% on generation. In the FDI track, the best system achieved 73% on full-duplex metrics, with backchannel timing being the strongest capability (81%) and overlap resolution the weakest (58%). The challenge revealed that combining EI and FDI capabilities remains an open problem: systems optimized for one track performed poorly on the other.

**Relevance to Music Attribution:**
The finding that emotion analysis outpaces empathetic generation aligns with Section 6.5 and reinforces the design recommendation: the attribution agent should detect emotional states (frustration during review, excitement about correct attributions) and adapt its behavior (slow down, provide more detail, offer human escalation) rather than attempting to generate emotionally sophisticated responses. The FDI track results confirm that full-duplex is still challenging, supporting a pragmatic half-duplex design for the initial attribution agent with full-duplex as a future enhancement.

---

### 6.8 TRACE: Hearing Between the Lines

| Field | Details |
|-------|---------|
| **Title** | TRACE: Hearing Between the Lines -- Dimension-First Speech-to-Speech Evaluation |
| **Authors** | TRACE Research Group |
| **Date** | January 2026 |
| **Link** | [arXiv:2601.13742](https://arxiv.org/abs/2601.13742) |

**Key Findings:**
TRACE proposes a dimension-first evaluation framework for speech-to-speech (S2S) systems, where individual quality dimensions (fluency, relevance, informativeness, safety, prosodic appropriateness) are evaluated independently before being combined into an overall score. The key innovation is using LLM judges that reason over audio cues rather than transcriptions -- the judges receive both the audio and a structured prompt asking them to evaluate specific dimensions. Surprisingly, this approach achieves higher human agreement (Spearman rho = 0.84) than audio-native LLM judges (rho = 0.76) while being significantly cheaper (text LLM inference vs. audio LLM inference). The paper argues that current audio-native models are worse judges than text models operating on rich audio descriptions, because text models are better calibrated through extensive RLHF.

**Relevance to Music Attribution:**
TRACE's dimension-first approach is directly applicable to evaluating the attribution voice agent. The relevant dimensions map cleanly: fluency (natural speech), relevance (correct attribution data), informativeness (confidence scores, source citations), safety (not leaking private data), and prosodic appropriateness (tone matching the confidence level). The finding that text-LLM judges outperform audio-native judges at lower cost enables scalable automated evaluation of the attribution agent during development and A/B testing.

---

### 6.9 LALM-as-a-Judge: Safety Evaluation in Spoken Dialogues

| Field | Details |
|-------|---------|
| **Title** | LALM-as-a-Judge: Evaluating Safety in Multi-Turn Spoken Dialogues |
| **Authors** | LALM-as-a-Judge Research Group |
| **Date** | February 2026 |
| **Link** | [arXiv:2602.04796](https://arxiv.org/abs/2602.04796) |

**Key Findings:**
LALM-as-a-Judge is the first benchmark specifically targeting safety evaluation in multi-turn spoken dialogues. The paper identifies safety failure modes unique to speech that text-based evaluation misses: (1) prosodic manipulation (using tone to convey harmful intent while text content appears benign); (2) voice identity attacks (impersonating authority figures to extract information); (3) emotional pressure escalation across turns; and (4) context window exploitation (spreading harmful requests across many turns to evade per-turn safety filters). The benchmark includes 2,800 adversarial multi-turn dialogues annotated by domain experts. The best Large Audio Language Model (LALM) judge achieves 0.79 F1 on safety violation detection, compared to 0.71 for text-only evaluation of the same dialogues, confirming that speech-specific safety signals matter.

**Relevance to Music Attribution:**
The voice identity attack vector is directly relevant to the attribution agent: an attacker could impersonate an artist's manager to modify attribution records, or use emotional pressure to coerce the agent into approving fraudulent credits. The multi-turn context window exploitation is also relevant for attribution disputes where a bad actor gradually shifts the conversation toward unauthorized modifications. The attribution agent must implement both per-turn and cross-turn safety evaluation, with higher scrutiny for actions that modify attribution records (approval, rejection, credit changes) compared to read-only queries.

---

### 6.10 Gender Bias in Speech Language Models

| Field | Details |
|-------|---------|
| **Title** | Uncovering Gender Bias in Speech Language Models |
| **Authors** | SpeechLM Bias Research Group |
| **Date** | October 2025 |
| **Link** | [arXiv:2510.01254](https://arxiv.org/abs/2510.01254) |

**Key Findings:**
This paper demonstrates that SpeechLMs exhibit voice-specific biases not captured by text-only bias benchmarks. When the same text query is spoken by male vs. female voices, SpeechLMs produce responses that differ in helpfulness, authority attribution, and assumed expertise level. Specifically: (1) female voices receive 14% more clarifying questions (implying assumed lower expertise); (2) male voices receive 18% more direct, detailed technical responses; (3) these biases persist even when the text content explicitly establishes expertise. The biases are not present in the underlying text LLMs -- they emerge from the speech encoder's learned associations between voice characteristics and social attributes. The paper proposes bias mitigation through voice-characteristic-agnostic embedding normalization, which reduces the gap to 3-4%.

**Relevance to Music Attribution:**
The music industry already faces well-documented gender inequities in production credits. A voice attribution agent that gives less detailed or less authoritative responses to female-voiced queries would compound these inequities. The finding that biases emerge from the speech encoder (not the text LLM) means that using a cascaded architecture (ASR to text, then text LLM) may inadvertently avoid this bias -- another point in favor of the cascaded approach. If an end-to-end SpeechLM is used, the voice-characteristic-agnostic normalization technique should be applied. Evaluation must include gender-stratified testing as a mandatory quality gate.

---

## 7. Cost Optimization and Edge Deployment

Voice AI is computationally expensive, making cost optimization critical for sustainable deployment. Edge deployment enables offline and low-latency use cases.

### 7.1 WhisperKit (ICML 2025)

| Field | Details |
|-------|---------|
| **Title** | WhisperKit: Efficient On-Device Speech Recognition with Whisper |
| **Authors** | WhisperKit Team |
| **Date** | July 2025 |
| **Link** | [arXiv:2507.10860](https://arxiv.org/abs/2507.10860) |

**Key Findings:**
WhisperKit demonstrates that Whisper Large V3 Turbo can run on Apple Neural Engine (ANE) with 0.46 second latency and 2.2% Word Error Rate -- matching cloud-hosted Whisper performance. The key engineering contributions are: (1) model graph restructuring to maximize ANE utilization (achieving 85% ANE occupancy vs. 40% with naive deployment); (2) dynamic batching that processes audio chunks in parallel during silence periods; (3) a streaming mode that provides partial transcriptions every 250ms while maintaining accuracy on the final result. The system operates without network connectivity, processes audio locally, and consumes approximately 1.5W of power on iPhone 15 Pro. Memory footprint is 1.2GB for the full model, which fits comfortably alongside typical app memory budgets.

**Relevance to Music Attribution:**
On-device ASR enables the attribution voice agent to function in environments without reliable internet -- recording studios in basements, live venues, field recordings. The 0.46s latency is fast enough for interactive attribution queries, and the 2.2% WER ensures accurate transcription of artist names and identifiers. The Apple Neural Engine optimization is particularly relevant given the music industry's strong iOS adoption. For the "BYO" archetype that prioritizes self-sovereignty, on-device ASR means voice data never leaves the user's device -- addressing privacy concerns about voice biometric data.

---

### 7.2 Whisper Quantization Analysis

| Field | Details |
|-------|---------|
| **Title** | Quantization of Whisper Models: Accuracy-Efficiency Tradeoffs |
| **Authors** | Whisper Quantization Research Group |
| **Date** | March 2025 |
| **Link** | [arXiv:2503.09905](https://arxiv.org/abs/2503.09905) |

**Key Findings:**
This paper provides a systematic analysis of quantization effects on Whisper models across multiple precision levels (FP16, INT8, INT4, INT3). The key finding: 4-bit quantization (GPTQ) reduces model size from 1.6GB to 0.6GB (62.5% reduction) with WER degradation within 1% of the full-precision model. INT8 quantization introduces no measurable WER degradation while halving the model size. However, INT3 quantization causes significant quality degradation (3.8% WER increase) that makes it unsuitable for production use. The paper also evaluates quantization sensitivity across languages, finding that languages with smaller training data representation (Japanese, Korean, Arabic) are more sensitive to quantization than well-represented languages (English, Spanish, French). Mixed-precision approaches (INT8 for encoder, INT4 for decoder) offer the best accuracy-size tradeoff.

**Relevance to Music Attribution:**
The 4-bit quantization result enables deployment of high-quality ASR on resource-constrained devices -- mobile phones, embedded studio hardware, or budget servers. The 0.6GB model fits alongside other application components without memory pressure. The language sensitivity finding is relevant for international music attribution: names, titles, and metadata in less-represented languages will have higher ASR error rates, which should be reflected in the attribution confidence scoring. The mixed-precision recommendation (INT8 encoder, INT4 decoder) provides a concrete deployment configuration for the attribution agent.

---

### 7.3 Muon-Optimized Distillation for Voice Models

| Field | Details |
|-------|---------|
| **Title** | Muon-Optimized Task-Specific Distillation for Edge Voice Models |
| **Authors** | Muon Distillation Research Group |
| **Date** | January 2026 |
| **Link** | [arXiv:2601.09865](https://arxiv.org/abs/2601.09865) |

**Key Findings:**
This paper combines task-specific knowledge distillation with the Muon optimizer (a recently introduced optimizer that demonstrates faster convergence than AdamW on language model training) to create compact, high-quality voice models for edge deployment. The approach trains a small student model (125M parameters) to match a large teacher model (1.5B) on a specific task distribution, then applies post-training quantization (GPTQ 4-bit). The resulting model achieves 94% of the teacher's performance on the target task at 1/12th the parameter count and 1/48th the memory footprint. The Muon optimizer specifically enables faster distillation (40% fewer training steps to converge) and better final quality (1.2% accuracy improvement) compared to AdamW-based distillation. The paper demonstrates results on ASR, TTS, and spoken dialogue tasks.

**Relevance to Music Attribution:**
Task-specific distillation enables creating attribution-domain-specific voice models: a student model trained specifically on music attribution queries, artist names, technical terminology, and metadata formats. Such a model would outperform a general-purpose model of the same size on attribution tasks while fitting on edge devices. The 40% training efficiency gain from the Muon optimizer reduces the cost of creating and updating these domain-specific models, which would need periodic retraining as new artists and works enter the database.

---

### 7.4 On-Device LLMs: State of the Union 2026

| Field | Details |
|-------|---------|
| **Title** | On-Device Large Language Models: A 2026 Survey |
| **Authors** | Various (survey paper) |
| **Date** | Early 2026 |
| **Link** | Multiple sources (survey) |

**Key Findings:**
The emerging consensus for on-device LLM deployment follows a train-in-16-bit, deploy-in-4-bit paradigm. GPTQ and AWQ (Activation-aware Weight Quantization) are the dominant quantization methods, achieving approximately 4x memory reduction with minimal quality loss for models up to 7B parameters. Key developments in 2025-2026: (1) Apple's MLX framework enables efficient LLM inference on Apple Silicon with unified memory; (2) Qualcomm's AI Engine Direct supports INT4 inference on Snapdragon 8 Gen 3+; (3) MediaTek's APU 700 enables on-device inference for models up to 13B (4-bit); (4) speculative decoding improves throughput 2-3x without quality loss. The practical ceiling for on-device models in 2026 is approximately 7B parameters at 4-bit quantization, which corresponds to a 3.5GB model file.

**Relevance to Music Attribution:**
The 7B/4-bit practical ceiling means that a capable attribution agent can run entirely on-device for basic queries and local database lookups, with cloud fallback for complex multi-source attribution. The cross-platform hardware support (Apple, Qualcomm, MediaTek) ensures the attribution agent is not locked to a single ecosystem. The speculative decoding improvement directly reduces voice agent latency, as the LLM inference step is typically the second-largest latency contributor (after TTS synthesis).

---

## 8. Emotional and Expressive TTS

The attribution agent's voice must convey information through prosody, not just words. Confidence levels, urgency, and data completeness should be audible.

### 8.1 IndexTTS2: Emotion from Minimal Audio Prompts

| Field | Details |
|-------|---------|
| **Title** | IndexTTS2: Zero-Shot Emotional Text-to-Speech with Duration Control |
| **Authors** | IndexTTS Research Team |
| **Date** | June 2025 |
| **Link** | [arXiv:2506.21619](https://arxiv.org/abs/2506.21619) |

**Key Findings:**
IndexTTS2 achieves controllable emotional speech synthesis from minimal audio prompts (3-5 seconds of reference audio). The key innovation is a duration control mechanism that allows independent manipulation of speaking rate without affecting emotional quality -- previous systems conflated speed with emotion (faster = excited, slower = sad). The model disentangles three controllable dimensions: emotion (from reference audio), duration (from explicit control), and speaker identity (from a separate speaker embedding). This three-way disentanglement enables combinations like "sad but fast" or "excited but measured" that previous systems could not produce. Zero-shot capability means no fine-tuning is needed for new emotions or speakers.

**Relevance to Music Attribution:**
The disentangled control dimensions map to attribution communication needs: the agent should speak confidently and at normal speed for high-confidence attributions, cautiously (hedging emotion) but at normal speed for medium-confidence results, and slowly with emphasis for low-confidence results that require careful human review. The duration control is particularly useful for reading out structured data (ISRC codes, long artist names) at a measured pace regardless of the emotional context. Zero-shot capability means the system can adapt to new voice personas without retraining.

---

### 8.2 ECE-TTS: Zero-Shot Emotion via VAD Mapping

| Field | Details |
|-------|---------|
| **Title** | ECE-TTS: Zero-Shot Emotion Control Using VAD-to-Spherical-Vector Mapping |
| **Authors** | ECE-TTS Team |
| **Date** | May 2025 |
| **Link** | [MDPI Applied Sciences](https://www.mdpi.com/journal/applsci) |

**Key Findings:**
ECE-TTS introduces a novel approach to emotional speech synthesis by mapping Valence-Arousal-Dominance (VAD) values to Emotion-Adaptive Spherical Vectors that control the TTS model's emotional output. The VAD representation provides a continuous emotion space rather than discrete categories (happy/sad/angry), enabling fine-grained emotional control. The spherical vector mapping ensures smooth transitions between emotional states, avoiding the "emotion jumping" artifact common in discrete-category systems. The system achieves zero-shot emotion control (no emotion-specific training data required) by learning the VAD-to-speech mapping from a general emotional speech corpus. Human evaluation shows 73% emotion recognition accuracy for the synthesized speech, compared to 81% for natural emotional speech -- a gap of only 8%.

**Relevance to Music Attribution:**
The continuous VAD representation enables mapping attribution confidence scores directly to voice emotion parameters. A confidence score of 0.92 could map to high valence (positive), low arousal (calm), and high dominance (authoritative): "I'm quite confident about this attribution." A score of 0.35 could map to lower valence, slightly higher arousal, and lower dominance: "I have limited confidence here -- you may want to verify manually." This creates an audible confidence signal that supplements the explicit verbal confidence reporting, leveraging the human ability to perceive emotional nuance in speech.

---

### 8.3 ParaStyleTTS: Phoneme-Level Style Control

| Field | Details |
|-------|---------|
| **Title** | ParaStyleTTS: Phoneme-Level Parameterized Style Control for Emotion, Age, and Gender |
| **Authors** | ParaStyleTTS Research Team |
| **Date** | October 2025 |
| **Link** | [arXiv:2510.18308](https://arxiv.org/abs/2510.18308) |

**Key Findings:**
ParaStyleTTS enables style control at the phoneme level rather than the utterance level, allowing different parts of a single sentence to carry different emotional colorings. The model parameterizes three style dimensions -- emotion, perceived age, and perceived gender -- independently for each phoneme. This enables effects like emphasizing a specific word with increased intensity while keeping the rest of the sentence neutral, or transitioning smoothly from one emotion to another within a sentence. The phoneme-level control is achieved through a style encoder that produces per-phoneme style vectors, which are then used to condition the acoustic model. The system maintains naturalness (MOS 3.9/5.0) even with complex intra-sentence style variations.

**Relevance to Music Attribution:**
Phoneme-level control enables the attribution agent to emphasize key information within a sentence: "The songwriter is *John Smith* [emphasized] with *87 percent* [confident tone] confidence, based on *MusicBrainz* [neutral] and *Discogs* [neutral] agreement." This micro-level prosodic control conveys the A0-A3 assurance level through voice quality: A3 (artist-verified) with confident emphasis, A1 (single source) with cautious hedging, A0 (no data) with explicit uncertainty. The per-phoneme approach is more natural than utterance-level emotion switching, which would sound robotic during information-dense attribution responses.

---

### 8.4 Orpheus TTS

| Field | Details |
|-------|---------|
| **Title** | Orpheus TTS: Open-Source Expressive Text-to-Speech |
| **Authors** | Orpheus Team |
| **Date** | March 2025 |
| **Link** | [GitHub](https://github.com/canopyai/Orpheus-TTS) (Apache 2.0) |

**Key Findings:**
Orpheus TTS is a 3B-parameter open-source TTS model built on a LLaMA-3b backbone, trained on over 100,000 hours of expressive speech data. The model supports simple emotion tags (<laugh>, <sigh>, <whisper>, <emphasis>) that can be embedded in the input text to control expressiveness. Streaming synthesis achieves approximately 200ms time-to-first-audio, enabling real-time conversational use. The model supports 8 pre-defined voice personas with distinct characteristics (pitch, speaking rate, vocal quality). The Apache 2.0 license allows commercial use without restrictions. Quality benchmarks show Orpheus achieving MOS 4.1/5.0, competitive with commercial TTS services (ElevenLabs: 4.3, OpenAI TTS: 4.2, Azure Neural: 4.0). The LLaMA backbone enables fine-tuning on domain-specific data with standard LLM training tooling.

**Relevance to Music Attribution:**
Orpheus is the strongest open-source TTS candidate for the attribution voice agent. The Apache 2.0 license allows unrestricted commercial deployment, eliminating licensing risk. The simple emotion tags provide adequate expressiveness for attribution communication without the complexity of full VAD-based control. The LLaMA backbone means the same fine-tuning infrastructure used for the attribution LLM can be applied to the TTS model, enabling domain-specific voice customization (e.g., correct pronunciation of music terminology, artist names, label names). The 200ms streaming latency meets the real-time conversational requirement. For the "BYO" archetype, Orpheus enables fully self-hosted voice synthesis.

---

### 8.5 Controllable Speech Synthesis Survey

| Field | Details |
|-------|---------|
| **Title** | A Survey on Controllable Speech Synthesis in the Era of Large Language Models |
| **Authors** | Controllable TTS Survey Group |
| **Date** | December 2024 (arXiv), updated through 2025 |
| **Link** | [arXiv:2412.06602](https://arxiv.org/abs/2412.06602) |

**Key Findings:**
This comprehensive survey covers the landscape of controllable TTS, categorizing control dimensions into: prosodic (pitch, duration, energy), stylistic (emotion, speaking style), speaker (identity, age, gender), and environmental (room acoustics, channel characteristics). The survey identifies a trend toward unified control frameworks that handle all dimensions simultaneously, replacing earlier single-dimension approaches. Key findings: (1) LLM-based TTS architectures (like Orpheus) provide the most flexible control through natural language instructions, but at higher computational cost; (2) diffusion-based models offer the highest audio quality but lack streaming capability; (3) the "control vs. naturalness" tradeoff has largely been resolved for single-dimension control but remains challenging for multi-dimension control; (4) evaluation methodology is the field's biggest gap -- there is no standard benchmark for controllable TTS.

**Relevance to Music Attribution:**
The survey provides the decision framework for selecting the TTS component of the attribution voice agent. The key tradeoff for the attribution use case is between control flexibility (conveying confidence through prosody) and streaming capability (real-time conversation). Based on the survey's findings, LLM-based architectures (Orpheus, VITS2) offer the best balance, while diffusion models (Stable Audio) are better suited for pre-generated content (e.g., attribution reports read aloud). The lack of standardized evaluation for controllable TTS means the attribution project will need custom evaluation protocols.

---

## 9. Music Domain Specific

These papers and industry developments directly address the intersection of voice AI and music attribution.

### 9.1 From Generation to Attribution (NeurIPS 2025 Workshop)

| Field | Details |
|-------|---------|
| **Title** | From Generation to Attribution: Agent Architectures for Music Attribution in the Post-Streaming Era |
| **Authors** | NeurIPS 2025 Music AI Workshop contributors |
| **Date** | NeurIPS 2025 (December 2025) |
| **Link** | NeurIPS 2025 Workshop proceedings |

**Key Findings:**
This workshop paper is the most directly relevant to the music attribution scaffold project. It proposes agent architectures specifically designed for music attribution, addressing the unique challenges of the post-streaming era: fragmented metadata across multiple databases, conflicting attribution claims, and the need for probabilistic confidence rather than binary correctness. The paper outlines three architecture patterns: (1) a retrieval-augmented agent that queries multiple metadata sources and reconciles conflicts; (2) a conversational agent that guides artists through attribution review; and (3) a proactive monitoring agent that detects attribution changes and alerts stakeholders. The paper emphasizes that attribution is not a single query but an ongoing process requiring persistent state and multi-turn interaction -- aligning with the voice agent paradigm.

**Relevance to Music Attribution:**
This paper validates the core design philosophy of the scaffold project. The three architecture patterns map to the scaffold's planned capabilities: the retrieval-augmented pattern maps to the ETL and Entity Resolution pipelines, the conversational pattern maps to the voice agent, and the monitoring pattern maps to the drift detection and feedback systems. The emphasis on probabilistic confidence rather than binary attribution directly supports the conformal prediction and Bayesian updating approaches in the manuscript.

---

### 9.2 Pex Voice Identification

| Field | Details |
|-------|---------|
| **Title** | Pex Voice ID: Biometric Vocal Fingerprinting for Content Attribution |
| **Authors** | Pex (industry) |
| **Date** | 2025 |
| **Link** | [Pex Platform](https://pex.com/) |

**Key Findings:**
Pex's Voice ID technology extracts biometric vocal fingerprints from audio recordings for singer identification and attribution. The system creates a compact embedding (256-dimensional vector) from vocal characteristics including formant structure, vibrato patterns, breath patterns, and spectral envelope. Critically, the fingerprint is identification-only: it can match a voice to a known identity but cannot regenerate the voice from the fingerprint, addressing privacy and deepfake concerns. The system achieves 96% identification accuracy on a database of 50,000+ registered artists, with accuracy degrading gracefully for heavily processed vocals (auto-tune: 89%, pitch-shifted: 82%, distorted: 71%). False positive rate is 0.01% at the 96% recall threshold.

**Relevance to Music Attribution:**
Pex Voice ID provides automated singer attribution without requiring explicit metadata -- if a recording contains vocals, the system can probabilistically identify the singer. This directly feeds the attribution confidence scoring: a Voice ID match provides one evidence source that can be combined with metadata from MusicBrainz, Discogs, and other sources. The identification-only design (cannot regenerate voices) aligns with privacy requirements. The degradation profile (96% clean to 71% distorted) maps to confidence adjustments: clean vocal recordings warrant higher confidence from Voice ID evidence than heavily processed tracks.

---

### 9.3 Singing Voice Conversion Challenge 2025

| Field | Details |
|-------|---------|
| **Title** | Singing Voice Conversion Challenge 2025 |
| **Authors** | SVC Challenge Organizers |
| **Date** | 2025 |
| **Link** | SVC Challenge 2025 proceedings |

**Key Findings:**
The 2025 Singing Voice Conversion (SVC) Challenge evaluated systems that transform one singer's voice to sound like another while preserving the musical content (melody, lyrics, expression). The best systems achieved speaker similarity scores above 0.90 (nearly indistinguishable from the target singer) with naturalness MOS above 4.0. The challenge revealed that modern SVC systems can create convincing conversions from as little as 30 seconds of target singer audio. However, conversion quality degrades significantly for singing styles that differ substantially from the training distribution (e.g., operatic to rap conversion), and artifacts become audible in extreme pitch ranges. The challenge also included a detection track, where the best detection system achieved only 78% accuracy in distinguishing converted from original singing.

**Relevance to Music Attribution:**
SVC technology exemplifies the Oracle Problem from the manuscript: if a singer's voice can be convincingly converted to sound like another artist, the digital recording alone cannot definitively prove who actually sang. The 78% detection accuracy means that 22% of converted vocals would pass undetected, creating a significant attribution integrity risk. This reinforces the design principle that attribution must rely on provenance chains (who was in the studio, who has the session files) rather than audio analysis alone. The voice agent should communicate this limitation when attribution is based primarily on audio fingerprinting: "Audio analysis suggests this is Artist X, but voice conversion cannot be ruled out."

---

### 9.4 DDEX AI Metadata Standards

| Field | Details |
|-------|---------|
| **Title** | DDEX Standards Updates for AI-Generated and AI-Assisted Music |
| **Authors** | DDEX (Digital Data Exchange) |
| **Date** | 2025 (ongoing) |
| **Link** | [DDEX Standards](https://ddex.net/) |

**Key Findings:**
DDEX is updating its metadata standards to accommodate AI usage disclosure in music production. The updated standards introduce granular AI involvement categories: vocals (AI-generated, AI-assisted, AI-modified), instrumentation (per instrument), composition (melody, harmony, lyrics, arrangement), production (mixing, mastering, sound design), and post-production (editing, restoration). Each category supports three disclosure levels: "AI-generated" (primarily AI), "AI-assisted" (human-led with AI tools), and "human-only" (no AI involvement). The standards also introduce provenance fields linking to training data disclosure (which datasets were used to train the AI) and consent records (whether rights holders of training data granted permission). The updated ERN (Electronic Release Notification) schema includes these new fields as optional elements.

**Relevance to Music Attribution:**
DDEX standards are the industry metadata infrastructure that the attribution scaffold consumes and produces. The new AI disclosure categories must be supported in the scaffold's data model (NormalizedRecord, ResolvedEntity, AttributionRecord). The voice agent needs to communicate these categories clearly: "This track's vocals are marked as AI-assisted, meaning the artist used AI tools but led the creative process." The granular per-element disclosure (vocals vs. instrumentation vs. composition) aligns with the scaffold's per-role attribution model. The provenance and consent fields directly map to the A0-A3 assurance levels and MCP permission queries.

---

### 9.5 Conformal Prediction for Affective Speech Analysis

| Field | Details |
|-------|---------|
| **Title** | Conformal Prediction for Risk-Calibrated Affective Speech Recognition |
| **Authors** | Conformal Speech Research Group |
| **Date** | March 2025 |
| **Link** | [arXiv:2503.22712](https://arxiv.org/abs/2503.22712) |

**Key Findings:**
This paper applies conformal prediction to speech emotion recognition, providing formal uncertainty bounds on predictions rather than point estimates. The approach produces prediction sets (e.g., {happy, excited} rather than just "happy") with a guaranteed coverage probability: if the coverage is set to 95%, the true emotion is in the prediction set at least 95% of the time. Key findings: (1) conformal prediction sets are well-calibrated even when the underlying model is poorly calibrated; (2) prediction set size correlates with genuine ambiguity (ambiguous utterances produce larger sets); (3) the coverage guarantee holds across demographic subgroups, providing built-in fairness properties. The paper also demonstrates adaptive conformal prediction that adjusts coverage based on the cost of errors -- higher coverage (larger sets, fewer false negatives) for high-stakes decisions.

**Relevance to Music Attribution:**
Conformal prediction is already a core technique in the attribution scaffold's confidence scoring (per the manuscript). This paper extends its application to the voice interaction layer: when the agent interprets a user's spoken attribution claim, conformal prediction provides formal bounds on the interpretation. For example, if the user says something ambiguous, the agent can present a prediction set: "Did you mean John Smith the songwriter, or John Smith the producer? I'm 95% confident it's one of these two." The adaptive coverage mechanism maps to the A0-A3 assurance levels: A3 decisions (artist-verified) require higher coverage (smaller prediction sets, more certainty) than A0 annotations (no data, exploratory queries).

---

## 10. Responsible AI for Voice

These papers address the broader ethical and social implications of voice AI deployment, with specific relevance to the music industry context.

### 10.1 Stanford AI Index 2025

| Field | Details |
|-------|---------|
| **Title** | Stanford AI Index Report 2025 |
| **Authors** | Stanford Institute for Human-Centered Artificial Intelligence |
| **Date** | 2025 |
| **Link** | [Stanford AI Index](https://aiindex.stanford.edu/) |

**Key Findings:**
The 2025 AI Index Report documents a 28.8% year-over-year increase in responsible AI publications, reflecting growing research attention to AI safety, fairness, and governance. Specific to voice AI, the report notes: (1) advanced LLMs continue to exhibit implicit biases in voice interaction settings that differ from text-only biases; (2) voice AI deployment in high-stakes domains (healthcare, legal, financial) is outpacing the development of domain-specific evaluation frameworks; (3) the gap between AI capability and AI governance is widening, with voice cloning capabilities advancing faster than detection and regulation. The report recommends industry-specific responsible AI frameworks rather than one-size-fits-all approaches, citing the music industry as a domain where intellectual property, identity, and creative rights create unique ethical considerations.

**Relevance to Music Attribution:**
The report's recommendation for industry-specific responsible AI frameworks validates the scaffold's approach of developing music-attribution-specific confidence scoring and assurance levels rather than applying generic AI safety frameworks. The finding that voice AI biases differ from text biases reinforces the need for voice-specific evaluation (Section 6.10). The observation that governance lags capability highlights the importance of building governance infrastructure (A0-A3, MCP permissions, C2PA credentials) proactively rather than reactively.

---

### 10.2 Systematic Review of Voice Assistant Ethics

| Field | Details |
|-------|---------|
| **Title** | A Systematic Review of Ethical Considerations in Voice Assistant Design |
| **Authors** | Montreal AI Ethics Institute |
| **Date** | October 2025 |
| **Link** | [Montreal AI Ethics Institute](https://montrealethics.ai/) |

**Key Findings:**
This systematic review synthesizes 127 papers on voice assistant ethics, organizing findings into five categories: accessibility, social norms, gender stereotypes, privacy, and power dynamics. Key findings: (1) voice assistants with female-coded default voices reinforce gender stereotypes about service roles -- multiple studies recommend offering gender-neutral voice options or requiring explicit voice selection; (2) accessibility gaps persist for users with speech impediments, strong accents, or atypical speech patterns, with error rates 3-5x higher than for "standard" speakers; (3) always-on listening creates privacy concerns that users underestimate until informed; (4) the conversational metaphor creates false intimacy that can be exploited for data extraction; (5) power dynamics are asymmetric -- the voice assistant controls the conversation flow, which disadvantages users with less experience navigating AI interfaces.

**Relevance to Music Attribution:**
The attribution voice agent must avoid reinforcing music industry power dynamics. The voice selection recommendation is directly actionable: offer multiple voice options including gender-neutral, and do not default to a female-coded service voice. The accessibility finding is critical for global music attribution: artists worldwide, many speaking English as a second language with diverse accents, must be served equally. The privacy concern maps to voice biometric data handling: the agent must clearly communicate what voice data is stored, processed, or transmitted, and obtain explicit consent. The power dynamics concern informs the UX design: the agent should support user-led conversation flow (letting artists set the pace of attribution review) rather than agent-led flow.

---

### 10.3 SpeechLM Survey (ACL 2025)

| Field | Details |
|-------|---------|
| **Title** | A Comprehensive Survey of Speech Language Models |
| **Authors** | SpeechLM Survey Group |
| **Date** | ACL 2025 (arXiv:2410.03751) |
| **Link** | [arXiv:2410.03751](https://arxiv.org/abs/2410.03751) |

**Key Findings:**
This is the first comprehensive survey of Speech Language Models (SpeechLMs), providing a taxonomy of architectures, training recipes, and evaluation frameworks. The survey categorizes SpeechLMs into four architecture families: (1) cascaded (ASR + text LLM + TTS), (2) early fusion (audio tokens in LLM vocabulary), (3) late fusion (separate audio and text encoders, shared decoder), and (4) end-to-end (single model, audio in and out). Key findings: (1) cascaded architectures remain the most reliable for task-oriented applications despite higher latency; (2) early fusion models (like AudioPaLM) achieve the best quality on generative tasks but require the most training data; (3) late fusion (like SALMONN) offers the best quality-efficiency tradeoff; (4) end-to-end models are improving rapidly but still lag on knowledge-intensive tasks. The survey also identifies a critical evaluation gap: no existing benchmark simultaneously tests speech quality, task completion, and conversational coherence.

**Relevance to Music Attribution:**
The survey's architecture taxonomy provides the decision framework for the attribution voice agent's technical architecture. Based on the findings: a cascaded architecture (ASR + text LLM + TTS) is recommended for the MVP due to its reliability on task-oriented applications (attribution lookup and review); a late fusion architecture (SALMONN-style) is the target for v2 to reduce latency; end-to-end is premature for the attribution use case given the knowledge-intensive nature of the task. The evaluation gap identified (no benchmark testing speech quality + task completion + coherence simultaneously) means the scaffold project will need to develop its own evaluation framework, potentially contributing it as an open benchmark.

---

## Summary: Top 10 Papers for Music Attribution Voice Agent

The following papers represent the highest-impact reading for teams building a music attribution voice agent, ranked by direct relevance to the project's design decisions.

| Rank | Paper | Section | Why It Matters |
|------|-------|---------|----------------|
| 1 | **From Generation to Attribution** (NeurIPS 2025 Workshop) | 9.1 | Exact problem domain -- agent architectures specifically for music attribution |
| 2 | **PRAC3** ([arXiv:2507.16247](https://arxiv.org/abs/2507.16247)) | 3.3 | Maps Consent/Credit/Compensation directly to A0-A3 assurance framework |
| 3 | **Moshi** ([arXiv:2410.00037](https://arxiv.org/abs/2410.00037)) | 1.1 | Full-duplex architecture blueprint, 200ms latency target |
| 4 | **KAME** ([arXiv:2510.02327](https://arxiv.org/abs/2510.02327)) | 1.2 | Tandem architecture separating responsiveness from knowledge retrieval |
| 5 | **VoiceAgentBench** ([arXiv:2510.07978](https://arxiv.org/abs/2510.07978)) | 6.2 | Proves cascaded pipelines beat end-to-end for agentic voice tasks |
| 6 | **C2PA 2.1-2.3** ([c2pa.org](https://c2pa.org/specifications/)) | 3.5 | Audio provenance standard bridging the Oracle Problem |
| 7 | **WhisperKit** ([arXiv:2507.10860](https://arxiv.org/abs/2507.10860)) | 7.1 | On-device ASR matching cloud quality for edge/mobile deployment |
| 8 | **Conformal Prediction for Speech** ([arXiv:2503.22712](https://arxiv.org/abs/2503.22712)) | 9.5 | Formal uncertainty bounds on voice-based attribution queries |
| 9 | **Krisp Turn-Taking v2** | 4.2 | Production-ready, lightweight, CPU-only turn-taking |
| 10 | **Orpheus TTS** ([GitHub](https://github.com/canopyai/Orpheus-TTS)) | 8.4 | Strongest open-source emotional TTS, Apache 2.0 license |

### Key Takeaways for Architecture Decisions

1. **Cascaded over end-to-end**: VoiceAgentBench (Section 6.2) demonstrates an 18-point accuracy gap favoring cascaded ASR-LLM pipelines for agentic tasks. The attribution voice agent should use ASR + text LLM + TTS, not an end-to-end SpeechLM.

2. **Tandem for latency**: KAME's tandem pattern (Section 1.2) solves the latency-vs-knowledge tradeoff: a fast conversational front-end maintains flow while the attribution engine processes queries.

3. **Confidence through prosody**: ECE-TTS (Section 8.2) and ParaStyleTTS (Section 8.3) demonstrate that attribution confidence can be conveyed through voice quality, supplementing explicit verbal confidence reporting.

4. **Governance is non-negotiable**: PRAC3 (Section 3.3), EU AI Act (Section 3.4), and C2PA (Section 3.5) collectively mandate: AI disclosure, synthetic audio labeling, consent infrastructure, and provenance tracking.

5. **Test with real speech**: VCB Bench (Section 6.4) shows 12-25% performance degradation with real speech vs. synthetic test data. Attribution agent testing must use real human speech recordings, not TTS-generated test queries.

6. **Edge is viable**: WhisperKit (Section 7.1) and 4-bit quantization (Section 7.2) demonstrate that high-quality voice processing runs on consumer devices, enabling the "BYO" archetype's self-sovereignty requirements.

---

*This document is part of the voice agent research series. See also: [voice-ai-infrastructure.md](voice-ai-infrastructure.md), [finops-economics.md](finops-economics.md), [leaderboards-evaluation.md](leaderboards-evaluation.md), [recommended-stack.md](recommended-stack.md).*
