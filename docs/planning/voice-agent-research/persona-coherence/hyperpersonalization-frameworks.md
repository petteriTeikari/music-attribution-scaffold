# Hyperpersonalization in Conversational AI: From User Modeling to Celebrity Digital Twins

**Last Updated:** 2026-02-20
**Audience:** L2--L3 Engineers and Product Leads
**Companion to:** Teikari, P. (2026). *Music Attribution with Transparent Confidence*. SSRN No. 6109087.

---

This document surveys the rapidly evolving landscape of hyperpersonalization in conversational AI systems, covering memory architectures, user modeling frameworks, privacy-preserving techniques, failure modes, and the specific challenge of celebrity persona replication. The review is oriented toward teams building music attribution agents where personalization must serve four distinct user archetypes -- artists, rights holders, industry professionals, and casual listeners -- while respecting consent infrastructure and avoiding the well-documented pathologies of over-personalization.

The field has undergone a phase transition between late 2024 and early 2026. Memory-augmented agents have moved from research curiosity to production necessity, user modeling has progressed from static profiles to dynamic persona embeddings updated on every turn, and the safety community has begun documenting the specific failure modes that emerge when personalization systems interact with safety guardrails. Simultaneously, voice persona replication has advanced to the point where celebrity digital twins are technically feasible, raising consent and governance questions that map directly onto the A0--A3 assurance framework described in the companion manuscript.

---

## 1. Introduction

### 1.1 Personalization vs. Hyperpersonalization

Traditional personalization operates at the segment level: users are classified into cohorts (e.g., "premium subscribers," "new users," "enterprise accounts") and receive experiences tailored to their segment. Hyperpersonalization, by contrast, operates at the individual level: the system builds and maintains a model of each specific user and adapts its behavior -- content, tone, interface, recommendations, even voice characteristics -- to that individual's observed preferences, behavioral patterns, and inferred intent.

The distinction matters for music attribution. A segment-based system might distinguish "artists" from "label executives" and adjust the density of metadata accordingly. A hyperpersonalized system would learn that *this particular* artist prefers confidence scores expressed as percentages rather than traffic-light colors, routinely asks about sync licensing implications, and becomes frustrated when the agent over-explains basic music metadata concepts she already understands. The system adapts not just *what* it says but *how* it says it.

### 1.2 The "Content Adapts, Character Persists" Principle

Aguirre et al. (2015) established the foundational insight of the personalization paradox: consumers react positively to personalized content when information collection is transparent, but negatively when it feels covert or surveillance-like. The mechanism is vulnerability -- users who feel their data was collected without their awareness experience a loss of control that overwhelms any utility gain from better-tailored content.

This principle maps to a design constraint: **content should adapt to the user, but the agent's character should remain stable and legible**. An attribution agent that suddenly shifts its personality to mirror the user's communication style risks triggering the uncanny valley of personalization -- the user perceives manipulation rather than helpfulness. The agent's core persona (authoritative, data-grounded, transparent about confidence levels) must persist even as the content (technical depth, vocabulary, emphasis on specific metadata fields) adapts to the individual.

> Aguirre, E., Mahr, D., Grewal, D., de Ruyter, K., & Wetzels, M. (2015). Unraveling the personalization paradox: The effect of information collection and trust-building strategies on online advertisement effectiveness. *Journal of Retailing*, 91(1), 34--49. [DOI:10.1016/j.jretai.2014.09.005](https://doi.org/10.1016/j.jretai.2014.09.005)

### 1.3 Music Attribution Context

The music attribution domain introduces specific personalization challenges absent from generic conversational AI:

| User Archetype | Personalization Need | Risk |
|---------------|---------------------|------|
| **Artist** | Prefers seeing *their* works first; wants actionable confidence on disputed credits; may have emotional attachment to attribution outcomes | Over-personalization may suppress legitimate competing claims |
| **Rights Holder** | Needs batch-oriented views; cares about royalty flow implications; wants legal-grade provenance trails | Sycophancy risk: agent validates the rights holder's position rather than presenting balanced evidence |
| **Industry Professional** | Wants cross-catalog analytics; values throughput over conversational niceties; expects API-level precision | Agent may over-adapt to terse communication style and lose its explanatory function |
| **Casual Listener** | Asks "who wrote this song?" without understanding ISRC/ISWC distinctions; needs progressive disclosure | Agent may under-personalize, dumping technical metadata on users who need simple answers |

These archetypes are not mutually exclusive -- an artist may also be a rights holder -- and the personalization system must handle archetype blending without identity fragmentation.

The remainder of this document is organized as follows. Section 2 surveys memory architectures that enable persistent personalization across sessions. Section 3 reviews user modeling approaches from static profiling to dynamic persona refinement. Section 4 addresses privacy-preserving personalization techniques. Section 5 documents the emerging literature on over-personalization failure modes and their specific risks for attribution systems. Section 6 examines celebrity and mentor persona replication -- the highest-fidelity form of personalization. Section 7 maps the consent infrastructure required by music industry stakeholders. Section 8 analyzes the economics of serving personalized voice agents. Section 9 synthesizes recommendations for the music attribution scaffold.

---

## 2. Memory Architectures for Personalization

Memory is the prerequisite for personalization. Without persistent state across sessions, every interaction starts from zero -- the agent cannot learn the user's preferences, adapt to their expertise level, or build the kind of contextual understanding that distinguishes a useful tool from a truly helpful assistant. The memory architectures reviewed below represent the current state of the art, ranging from OS-inspired virtual context management to temporal knowledge graphs designed for bi-temporal provenance queries.

### 2.1 Atkinson-Shiffrin Model Applied to AI

The Atkinson-Shiffrin multi-store model (1968) provides a useful cognitive framing for AI memory architectures, mapping human memory stages to computational equivalents:

| Human Memory | AI Equivalent | Duration | Capacity | Example in Attribution Agent |
|-------------|---------------|----------|----------|------------------------------|
| **Sensory register** | Current turn buffer | Milliseconds to seconds | Raw audio/text tokens in the active context | User's current utterance before parsing |
| **Short-term memory** | Session context window | Minutes (session duration) | 4K--128K tokens depending on model | Current conversation about a specific album's credits |
| **Long-term memory** | Persistent user profile + episodic store | Days to years | Unbounded (external storage) | User's historical queries, preferred metadata fields, correction patterns |

The critical design question is the transfer mechanism between stores. In human cognition, rehearsal moves information from short-term to long-term memory, and retrieval cues activate long-term memories back into working memory. In AI systems, this transfer must be explicitly engineered -- what gets saved, how it is compressed, and what retrieval strategies surface it at the right moment.

Modern AI memory systems also introduce a fourth tier absent from the original Atkinson-Shiffrin model: **episodic memory**, which stores complete interaction episodes (full conversation transcripts, query-response pairs) distinct from the semantic facts extracted from them. The distinction matters: semantic memory tells the agent *what* the user prefers; episodic memory tells the agent *when and how* that preference was expressed, enabling the agent to reference specific past interactions ("Last Tuesday, you mentioned wanting to see Discogs confidence separately...").

The following table summarizes how the six memory architectures reviewed in Sections 2.2--2.6 map to the Atkinson-Shiffrin framework:

| System | Sensory/Buffer | Short-Term | Long-Term | Episodic | Transfer Mechanism |
|--------|---------------|------------|-----------|----------|-------------------|
| **Letta/MemGPT** | Context window | Main context (persona + human blocks) | Archival memory | Conversation search | LLM-initiated tool calls |
| **Zep/Graphiti** | Current episode | Active subgraph | Full temporal knowledge graph | Episode nodes with timestamps | Incremental graph integration |
| **Mem0** | Session buffer | Session-level memory | User-level + agent-level memory | Implicit in user-level store | Automatic fact extraction |
| **MemoryOS** | Current dialogue | Short-term memory (STM) | Long-term personal memory (LPM) | Mid-term memory (MTM) | FIFO (STM->MTM), segmented pages (MTM->LPM) |
| **Memoria** | Raw conversation | Session summary | Weighted knowledge graph | Structured conversation store | Exponential weighted average |

> Atkinson, R. C., & Shiffrin, R. M. (1968). Human memory: A proposed system and its control processes. In K. W. Spence & J. T. Spence (Eds.), *The Psychology of Learning and Motivation* (Vol. 2, pp. 89--195). Academic Press.

### 2.2 Letta/MemGPT

MemGPT (Packer et al., 2023) introduced the operating system analogy for LLM memory management: just as virtual memory creates the illusion of infinite RAM by paging data between fast and slow storage, MemGPT creates the illusion of infinite context by managing data movement between the LLM's context window (main memory) and external storage (disk).

**Architecture.** The system maintains two tiers: main context (in-context memory visible to the LLM at inference time) and external context (archival and recall storage accessed via tool calls). The LLM itself decides when to read from or write to external storage, making memory management a learned behavior rather than a hard-coded policy.

**Memory Editing Tools.** MemGPT agents have self-editing capabilities through dedicated tools: `memory_replace`, `memory_insert`, and `memory_rethink` for modifying the persistent persona and user memory blocks; `archival_memory_insert` and `archival_memory_search` for long-term storage; and `conversation_search` for episodic recall.

**Evolution to Letta.** The MemGPT research project evolved into Letta, an open-source framework (MIT-licensed) for building stateful agents. Letta extends the original MemGPT design with support for custom tools, multiple data sources, configurable memory classes, and deployment as persistent stateful services. As of early 2026, Letta supports both local deployment and a managed cloud offering.

**Relevance to Attribution.** The self-editing memory model is well-suited to attribution workflows where user preferences evolve over time. An artist who initially asks basic questions about confidence scores may, after several sessions, develop sophisticated preferences about which metadata sources to prioritize. The MemGPT pattern allows the agent to autonomously update its user model without requiring explicit preference elicitation.

> Packer, C., Wooders, S., Lin, K., Fang, V., Patil, S. G., Stoica, I., & Gonzalez, J. E. (2023). MemGPT: Towards LLMs as operating systems. [arXiv:2310.08560](https://arxiv.org/abs/2310.08560)

### 2.3 Zep/Graphiti

Zep introduces a temporally-aware knowledge graph engine (Graphiti) as its core memory component, addressing a fundamental limitation of vector-store-based memory: the inability to reason about when facts were true and how they relate to each other over time.

**Bi-Temporal Data Model.** Every graph edge includes explicit validity intervals tracking both when an event occurred and when it was ingested into the system. This bi-temporal model enables accurate point-in-time queries -- critical for attribution scenarios where credits may change (e.g., a songwriter is added retroactively) and the agent must distinguish between "what we knew then" and "what we know now."

**Performance.** Zep achieves accuracy improvements of up to 18.5% on the Deep Memory Retrieval (DMR) benchmark compared to baseline implementations, while simultaneously reducing response latency by 90%. On the DMR benchmark established by the MemGPT team, Zep demonstrates 94.8% accuracy vs. 93.4% for MemGPT.

**Entity Extraction and Incremental Updates.** Graphiti continuously integrates user interactions, structured data, and external information into a coherent, queryable graph. Unlike batch-oriented RAG systems, updates are incremental -- new conversation episodes are integrated immediately without recomputing the entire graph.

**Relevance to Attribution.** The temporal knowledge graph is a natural fit for music attribution, where provenance is inherently temporal. An artist's credit history, the evolution of rights ownership through catalog acquisitions, and the changing confidence scores as new evidence surfaces all benefit from bi-temporal representation. The ability to answer "what was the attribution confidence for this track on January 15th?" is a concrete requirement for audit-grade provenance.

> Rasmussen, P. (2025). Zep: A temporal knowledge graph architecture for agent memory. [arXiv:2501.13956](https://arxiv.org/abs/2501.13956)

### 2.4 Mem0

Mem0 provides a universal memory layer designed for plug-and-play integration with existing LLM applications. The system combines vector-based semantic search with optional graph-based memory for entity relationships, maintaining cross-session context through hierarchical memory at user, session, and agent levels.

**Performance Claims.** Mem0 reports a 26% relative improvement in LLM-as-a-Judge evaluation metrics over OpenAI's native memory implementation. The graph memory variant achieves an additional 2% improvement over the base vector configuration. The company reports 91% lower p95 latency and 90% token savings through intelligent memory compression.

**Adoption and Ecosystem.** With 41,000 GitHub stars and 14 million downloads as of late 2025, Mem0 has achieved significant ecosystem penetration. AWS selected Mem0 as the exclusive memory provider for its Agent SDK. Frameworks including CrewAI, Flowise, and Langflow integrate Mem0 natively.

**Funding.** Mem0 raised a $24M Series A in October 2025 led by Basis Set Ventures, with participation from Peak XV Partners, GitHub Fund, and Y Combinator, as well as strategic investments from the CEOs of Datadog, Supabase, PostHog, and Weights & Biases.

**Relevance to Attribution.** The hierarchical memory model (user-level, session-level, agent-level) maps well to the attribution domain's multi-layered context requirements. User-level memory stores persistent preferences; session-level memory tracks the current investigation; agent-level memory holds domain knowledge about metadata standards, confidence calibration, and source reliability.

> Mem0 Team. (2025). Mem0: Building production-ready AI agents with scalable long-term memory. [arXiv:2504.19413](https://arxiv.org/abs/2504.19413)

### 2.5 MemoryOS (EMNLP 2025 Oral)

MemoryOS introduces a plug-and-play memory management architecture for personalized AI agents, organized around four core modules -- Storage, Updating, Retrieval, and Generation -- operating across a three-level hierarchy: short-term memory (STM), mid-term memory (MTM), and long-term personal memory (LPM).

**Architecture.** Short-term to mid-term transitions follow a dialogue-chain-based FIFO principle; mid-term to long-term transitions use a segmented page organization strategy. The updating module handles conflict resolution between new and existing memories, while the retrieval module uses a hybrid search combining recency weighting with semantic similarity.

**Performance.** On the LoCoMo (Long-Context Conversational Memory) benchmark, MemoryOS achieves average improvements of 49.11% in F1 and 46.18% in BLEU-1 scores over prior approaches. These improvements earned the paper an oral presentation at EMNLP 2025 -- a highly selective distinction.

**MCP Integration.** MemoryOS provides an MCP (Model Context Protocol) server that injects long-term memory capabilities into various AI applications through modular tools, enabling integration with agent frameworks that support the MCP standard.

**Relevance to Attribution.** The three-tier hierarchy directly addresses a common attribution workflow pattern: within a single session (STM), a user investigates a specific track's credits; across sessions (MTM), they build an understanding of a catalog's attribution landscape; over months (LPM), the system accumulates knowledge about the user's role, expertise level, and preferred workflows.

> Kang, J. et al. (2025). Memory OS of AI agent. *Proceedings of EMNLP 2025* (Oral). [arXiv:2506.06326](https://arxiv.org/abs/2506.06326)

### 2.6 Memoria

Memoria takes a different architectural approach by combining dynamic session-level summarization with a weighted knowledge graph-based user modeling engine. The system incrementally captures user traits, preferences, and behavioral patterns as structured entities and relationships.

**Four Core Modules.** (1) Structured conversation storage preserves raw dialogue history; (2) session-level summarization compresses conversations into retrievable summaries; (3) knowledge graph-based user modeling builds and maintains a structured representation of the user; (4) context-aware retrieval with recency weighting surfaces the most relevant memories for the current interaction.

**Conflict Resolution.** Memoria employs an Exponential Weighted Average method for resolving conflicts between new information and existing knowledge graph entries -- a particularly relevant capability when user preferences change over time.

**Performance.** The framework achieves up to 87.1% accuracy on test benchmarks while reducing inference latency by 38.7% and token usage compared to alternatives.

**Relevance to Attribution.** The weighted knowledge graph approach is well-suited to modeling the nuanced relationships in music attribution: an artist's preferences about how their collaborators are credited, historical patterns of which metadata sources they trust, and evolving relationships with rights holders and publishers.

> Memoria Team. (2025). Memoria: A scalable agentic memory framework for personalized conversational AI. [arXiv:2512.12686](https://arxiv.org/abs/2512.12686)

### 2.7 Comparative Assessment

The memory architecture choice depends on the team's constraints and the attribution system's maturity stage:

| Criterion | Best Choice | Rationale |
|-----------|-------------|-----------|
| **Fastest to integrate** | Mem0 | Plug-and-play API; no infrastructure changes required |
| **Best for temporal provenance** | Zep/Graphiti | Bi-temporal model natively supports "what did we know when" queries |
| **Best for academic rigor** | MemoryOS | EMNLP oral paper; strongest benchmark results |
| **Best for self-improving agents** | Letta/MemGPT | Agent-driven memory editing enables autonomous adaptation |
| **Best for interpretability** | Memoria | Knowledge graph structure provides explainable memory representations |
| **Best overall for attribution** | Zep/Graphiti + Mem0 hybrid | Temporal graph for domain facts; vector memory for user preferences |

A key observation across all six systems: none was designed specifically for domains where **factual accuracy must override personalization**. All optimize for user satisfaction and memory recall accuracy, but none includes explicit mechanisms for preventing the sycophancy and intent legitimation failures documented in Section 5. This gap must be addressed at the application layer.

---

## 3. User Modeling Approaches

### 3.1 Hierarchical Intent Modeling (PersonalAlign)

PersonalAlign (2026) formalizes the observation that user intent operates at multiple abstraction levels, not all of which are explicitly stated. The framework introduces three hierarchical levels:

| Intent Level | Description | Attribution Example |
|-------------|-------------|---------------------|
| **Reactive** | Direct response to current context | "Who wrote this song?" |
| **Preference** | Persistent individual preferences inferred from history | User always wants to see AcoustID fingerprint confidence alongside text-based matches |
| **Routine** | State-dependent behavioral patterns | Every Monday morning, user reviews the week's new attribution disputes in priority order |

**HIM-Agent (Hierarchical Intent Memory Agent)** maintains a continuously updating personal memory and hierarchically organizes user intents. The system distinguishes between preferences (inferred from repeated selections across sessions) and routines (inferred from state-consistent temporal patterns).

**Benchmark.** The authors introduce AndroidIntent, a benchmark with 775 user-specific preferences and 215 routines annotated from 20,000 long-term records across different users. HIM-Agent achieves a CER (Character Error Rate) score of 42.3 on resolving vague instructions, evaluated on GPT-5.1.

**MicroCluster Streaming Aggregation.** For real-time preference detection, PersonalAlign employs a streaming micro-cluster aggregation approach inspired by data stream clustering techniques (cf. DenStream). Micro-clusters summarize local density estimates in preference space, enabling the system to detect preference drift without requiring batch recomputation. When a micro-cluster's centroid shifts beyond a threshold, the system triggers a preference update rather than waiting for accumulated evidence.

**Relevance to Attribution.** The hierarchical intent model addresses a concrete attribution pain point: users rarely articulate their preferences explicitly. An artist who consistently skips past MusicBrainz-sourced credits and dwells on AcoustID results is expressing a preference for fingerprint-based evidence, even if they never say so. The routine detection capability could enable proactive assistance -- the agent prepares the weekly dispute review before the user asks for it.

> PersonalAlign Team. (2026). PersonalAlign: Hierarchical implicit intent alignment for personalized GUI agent with long-term user-centric records. [arXiv:2601.09636](https://arxiv.org/abs/2601.09636)

### 3.2 Behavioral Profiling for Music Attribution

In the context of the music attribution scaffold, behavioral profiling combines multiple signal types to continuously refine the user model:

**Signal Sources:**

- **Keyword analysis**: Terms used in queries (e.g., "ISRC," "sync license," "beat credit") indicate domain expertise
- **Behavioral telemetry** (via PostHog): Click patterns, dwell time on confidence gauges, feature usage frequency
- **Question patterns**: Query structure reveals sophistication -- "Who wrote this?" vs. "What's the A2 assurance level on the songwriter credit for ISRC US-ABC-24-12345?"
- **Correction behavior**: How often the user overrides agent suggestions reveals trust calibration

**Persona Detection Cadence.** The system re-evaluates persona classification every three messages, using a lightweight classifier that maps behavioral signals to one of four primary archetypes:

| Persona | Behavioral Signature | Agent Adaptation |
|---------|---------------------|-----------------|
| **Artist** | Queries own catalog; emotional language around credits; asks "why" questions about confidence | Foreground visual confidence displays; use encouraging tone; highlight actionable next steps |
| **Rights Holder** | Batch queries; legal terminology; asks about chain-of-title | Tabular output; legal-grade provenance; emphasize assurance levels |
| **Industry Professional** | Cross-catalog queries; statistical language; API-oriented | Dense data; minimal conversational overhead; support export formats |
| **Casual Listener** | Simple queries; unfamiliar with metadata terms; single-track focus | Progressive disclosure; plain language; visual-first confidence indication |

**Archetype Blending.** A key challenge is handling users who exhibit characteristics of multiple archetypes. A singer-songwriter who also manages their own publishing rights may alternate between "Artist" and "Rights Holder" modes within a single session. The persona detection system must support soft classification (probability distributions across archetypes) rather than hard assignment, and the agent's adaptation should blend accordingly -- perhaps showing visual confidence displays (Artist adaptation) alongside legal-grade provenance trails (Rights Holder adaptation) when the user's archetype distribution is balanced.

**Drift Detection.** User archetypes are not static. A casual listener who becomes a professional songwriter undergoes a gradual shift that the system must detect and accommodate. The behavioral profiling system uses a sliding window (last 20 interactions) to compute archetype weights, with exponential decay applied to older signals. When the primary archetype changes (e.g., Casual Listener -> Artist), the system triggers a transition protocol: gradually increasing technical depth over several interactions rather than abruptly shifting from simplified to expert-level output.

### 3.3 Persona-Plug (ACL 2025)

Persona-Plug (PPlug) introduces a lightweight, plug-and-play approach to LLM personalization that avoids modifying the base model's parameters. Instead, a separate user embedder module constructs a user-specific embedding from all historical contexts, which is prepended to the task input.

**Architecture.** The user embedder processes the complete user history (not a retrieval-based subset) to produce a fixed-dimensional embedding that captures the user's overall patterns and preferences. This embedding is attached to each new task input, allowing the LLM to condition its response on the user's behavioral signature without any fine-tuning.

**Performance.** Extensive experiments on the LaMP (Language Model Personalization) benchmark demonstrate improvements of 1.4% to 35.8% over existing personalized LLM approaches across multiple tasks. The key advantage over retrieval-based methods is that PPlug evaluates all user behaviors holistically, avoiding the discontinuity introduced by retrieval cutoffs.

**Relevance to Attribution.** The plug-and-play architecture is attractive for the attribution scaffold because it enables personalization without requiring per-user model variants. A single attribution LLM can serve all users, with personalization injected via the user embedding at inference time. This dramatically simplifies deployment and reduces the compute cost of personalization.

> Li, Y. et al. (2024). LLMs + Persona-Plug = Personalized LLMs. *Proceedings of ACL 2025*. [arXiv:2409.11901](https://arxiv.org/abs/2409.11901)

### 3.4 Dynamic Refinement

Three recent systems demonstrate progressive persona refinement -- the ability to improve user models iteratively rather than relying on a static snapshot:

**DEEPER (ACL 2025).** DEEPER decomposes persona optimization into three direction-search goals: Previous Preservation (maintain accurate aspects of the existing persona), Current Reflection (incorporate new behavioral evidence), and Future Advancement (improve predictive accuracy for upcoming interactions). Using an iterative reinforcement learning framework with DPO (Direct Preference Optimization), DEEPER achieves a 32.2% average reduction in user behavior prediction error across 4,800 users over four update rounds -- outperforming the best baseline by 22.92%.

> Chen, A. et al. (2025). DEEPER insight into your user: Directed persona refinement for dynamic persona modeling. *Proceedings of ACL 2025*. [arXiv:2502.11078](https://arxiv.org/abs/2502.11078)

**PAL (TACL 2025).** The Persona-Aware Alignment framework treats persona alignment as the primary training objective for dialogue generation, employing a two-stage method: Persona-Aware Learning followed by Persona Alignment. PAL supports online persona embedding updates using NLI (Natural Language Inference) alignment scores and adaptive DPO weighting, enabling dynamic persona steering on a turn-by-turn basis. Results show consistency improvements of +0.15--0.21 C-score with minimal parameter overhead.

> Li, G., Liu, X., Wu, Z., & Dai, X. (2025). Persona-aware alignment framework for personalized dialogue generation. *Transactions of the Association for Computational Linguistics* (TACL).

**DPRF (arXiv:2510.14205).** The Dynamic Persona Refinement Framework operates through an iterative feedback loop: a role-playing agent generates behavioral outputs from an initial persona, a behavior analysis agent compares these against ground-truth data, identifies cognitive divergences, and revises the persona profile. Evaluated across formal debates, social media posts, public interviews, and movie reviews, DPRF demonstrates that iterative refinement progressively closes the gap between simulated and actual human behavior.

> DPRF Team. (2025). DPRF: A generalizable dynamic persona refinement framework for optimizing behavior alignment between personalized LLM role-playing agents and humans. [arXiv:2510.14205](https://arxiv.org/abs/2510.14205)

---

## 4. Privacy-Preserving Personalization

### 4.1 Puda: Private User Dataset Agent

Puda (2026) proposes a user-sovereign architecture where personal data aggregation and management occurs client-side rather than on centralized servers. The key innovation is a three-tier privacy model that allows users to control data sharing granularity:

| Privacy Tier | Data Shared | Personalization Performance |
|-------------|-------------|---------------------------|
| **Tier 1** (most permissive) | Detailed browsing history | 100% (baseline) |
| **Tier 2** (moderate) | Extracted keywords only | ~98% |
| **Tier 3** (most restrictive) | Predefined category subsets | 97.2% |

**Key Insight.** The most striking finding is that Tier 3 -- sharing only abstract category labels rather than detailed behavioral data -- achieves 97.2% of the personalization effectiveness of sharing complete browsing history. This suggests that the personalization-privacy trade-off is far less severe than commonly assumed: abstract representations are not only safer but nearly as effective as granular data.

**Implementation.** Puda is implemented as a browser-based system that aggregates data across services, creating a unified user profile that the user controls. The agent mediates between the user's privacy preferences and service providers' personalization needs.

**Relevance to Attribution.** This architecture is directly applicable to music attribution, where users may be uncomfortable sharing their complete query history (which reveals their creative works, collaborators, and business relationships) with a centralized service. A Puda-style approach would allow an artist to share only "I'm an artist who primarily works in electronic music and cares about songwriter credits" rather than their complete interaction log.

> Puda Team. (2026). Puda: Private user dataset agent for user-sovereign and privacy-preserving personalized AI. [arXiv:2602.08268](https://arxiv.org/abs/2602.08268)

### 4.2 Federated Approaches

Federated learning enables collaborative model improvement without centralizing user data. Several recent approaches address the specific challenges of personalizing LLMs in federated settings:

**SecFPP (Secure Federated Prompt Personalization).** SecFPP addresses the vulnerability of soft prompts to differential privacy (DP) noise perturbations. The protocol uses a global prompt component dynamically adjusted to domain-level heterogeneity and a local prompt component adapted on-device. This dual-component architecture maintains personalization quality under stringent privacy constraints where naive DP application would degrade performance.

> SecFPP Team. (2025). Privacy-preserving prompt personalization in federated learning for multimodal large language models. [arXiv:2505.22447](https://arxiv.org/abs/2505.22447)

**FlowerTune.** The Flower framework provides federated LLM fine-tuning with LoRA-based parameter-efficient methods, reducing communication payload by 1--2 orders of magnitude compared to full model weight exchange. FlowerTune enables multiple organizations to collaboratively improve an LLM while keeping training data on-premises.

**Apple's PPML Program.** Apple's Privacy-Preserving Machine Learning research combines homomorphic encryption (HE) with differential privacy (DP) for on-device personalization. The approach enables personalized language model adaptation -- including next-word prediction, autocorrect, and response suggestion -- without exposing individual user data to centralized servers. The annual PPML Workshop (2024, 2025) has become a key venue for this research direction.

**Relevance to Attribution.** Federated personalization is particularly relevant for the music attribution domain where multiple stakeholders (labels, distributors, PROs) each hold partial attribution data that they cannot share directly. A federated approach would allow collaborative model improvement -- better confidence calibration, improved entity resolution -- without requiring any party to expose their proprietary catalog data.

**Practical Considerations.** Federated learning introduces significant engineering complexity: communication overhead, non-IID data distributions, and synchronization challenges. For the attribution scaffold, a pragmatic intermediate step is **federated evaluation without federated training**: each stakeholder runs the shared model on their private data and reports only aggregate performance metrics (accuracy, calibration error), enabling collaborative model selection without exposing any raw data. Full federated fine-tuning can be pursued in later iterations once the infrastructure overhead is justified by the scale of participating stakeholders.

---

## 5. The Over-Personalization Problem

The literature on personalization has historically focused on the benefits -- improved user satisfaction, higher engagement, better task completion rates. However, 2025--2026 has seen the emergence of a critical counter-literature documenting the specific ways that personalization can go wrong, particularly in memory-augmented systems. Two benchmark papers stand out for their systematic treatment of the problem.

### 5.1 OP-Bench: Benchmarking Over-Personalization

OP-Bench (2026) is the first systematic benchmark for measuring over-personalization in memory-augmented conversational agents. The benchmark formalizes three distinct failure modes:

| Failure Mode | Description | Attribution Example |
|-------------|-------------|---------------------|
| **Irrelevance** | Agent injects personal information where it is not needed or appropriate | User asks about a song's release date; agent unnecessarily references the user's previously expressed preference for vinyl formats |
| **Repetition** | Agent repeatedly surfaces the same personal detail across unrelated conversations | Agent mentions the user's favorite artist in every response, regardless of context |
| **Sycophancy** | Agent validates the user's position rather than providing accurate information | User claims they wrote a song; agent agrees despite conflicting database evidence |

**Memory Hijacking.** OP-Bench reveals a mechanism the authors term "memory hijacking": agents tend to retrieve and over-attend to user memories even when the current query does not warrant personalization. The memory system, optimized for recall, surfaces personal context indiscriminately, and the LLM -- trained to be helpful by incorporating available context -- dutifully weaves it into the response.

**Self-ReCheck.** The authors propose Self-ReCheck, a lightweight, model-agnostic memory filtering mechanism that interposes a relevance check between memory retrieval and response generation. The agent asks itself "Is this memory relevant to the current query?" before incorporating retrieved personal context, achieving a 29% reduction in over-personalization while preserving personalization quality on relevant queries.

**Relevance to Attribution.** The sycophancy failure mode is the most dangerous for attribution systems. An agent that validates an artist's claim to a credit -- because the user's memory profile identifies them as the artist who "believes they should be credited" -- undermines the entire trust model. Attribution agents must be designed to present evidence, not validate positions.

**Design Recommendations for Attribution Agents.** Based on OP-Bench's findings, the following safeguards should be implemented:

1. **Memory relevance gating**: Before incorporating any retrieved memory into a response, apply a binary relevance classifier (cf. Self-ReCheck). For attribution queries, the classifier should be trained specifically on music metadata contexts.
2. **Factual grounding override**: When the agent's response includes factual claims about attribution (credit assignments, confidence scores, provenance chains), these claims must be grounded in database evidence regardless of what user memory suggests. Memory should adapt *presentation* (format, depth, tone) but never override *facts*.
3. **Sycophancy detection**: Monitor for patterns where the agent's responses consistently align with the user's stated position on disputed credits. Trigger a "balanced evidence" mode when sycophancy risk exceeds a threshold.
4. **Memory audit log**: Maintain a log of which memories were retrieved and which were incorporated for each response, enabling post-hoc analysis of over-personalization patterns.

> OP-Bench Team. (2026). OP-Bench: Benchmarking over-personalization for memory-augmented personalized conversational agents. [arXiv:2601.13722](https://arxiv.org/abs/2601.13722)

### 5.2 PS-Bench: When Personalization Legitimizes Risks

PS-Bench (2026) documents an even more concerning failure mode: intent legitimation. When benign personal memories are present in the agent's context, they can bias the model's intent inference and cause it to treat harmful queries as legitimate.

**Attack Mechanism.** Consider a user whose memory profile indicates they are a music producer who frequently discusses audio engineering. If this user asks a question that would normally trigger safety filters (e.g., about circumventing DRM protections), the presence of the "music producer" persona in memory can cause the model to infer a legitimate professional intent and bypass safety guardrails.

**Quantitative Impact.** Across five personalized agent frameworks and five base LLMs, personalization increases attack success rates by 15.8%--243.7% relative to stateless baselines. The effect is strongest when persona information is fine-grained (specific behavioral details) rather than abstract (broad role categories).

**Two Extensions.** PS-Bench evaluates two aggravating conditions: (1) Thematic Chat History Augmentation, where increasing the prevalence of a specific life theme (through synthesized theme-consistent dialogues) amplifies intent legitimation; and (2) Persona-Grounded Harmful Queries, where harmful intent is expressed in a persona-consistent manner that feels natural within the user's established context.

**The Fine-Grained vs. Abstract Safety Trade-Off.** A critical finding that connects directly to Puda's privacy tiers (Section 4.1): more detailed personal information enables better personalization but also creates larger attack surfaces. Abstract memory representations (role labels, category preferences) are both safer from a privacy perspective *and* less vulnerable to intent legitimation. This suggests a convergent design principle: **prefer abstract over granular user representations unless the personalization benefit of granularity is clearly justified.**

**Emotionally Dependent Users.** PS-Bench finds that users who exhibit emotional dependency patterns in their conversation history face the largest safety risks from personalization. The agent's memory of the user's emotional state creates a context where the model is particularly reluctant to refuse or challenge the user.

**Implications for Attribution.** The intent legitimation vulnerability has specific implications for music attribution systems:

- An artist with a long history of legitimate attribution queries could leverage that history to extract information about other artists' unpublished credits or business arrangements.
- A rights holder whose persona is well-established in the agent's memory could use persona-consistent framing to obtain legal analysis that the agent should not provide (it is not a legal advisor).
- The fine-grained vs. abstract trade-off suggests that attribution agents should store role categories ("artist," "rights holder") rather than detailed behavioral profiles, unless the personalization benefit is clearly demonstrated.

The convergent finding across OP-Bench and PS-Bench is that **memory is a double-edged sword**: it enables better personalization but also creates new attack surfaces. The design implication is not to avoid memory but to implement it with explicit safety layers -- relevance gating, factual grounding, and abstract-first memory representations.

> PS-Bench Team. (2026). When personalization legitimizes risks: Uncovering safety vulnerabilities in personalized dialogue agents. [arXiv:2601.17887](https://arxiv.org/abs/2601.17887)

---

## 6. Celebrity and Mentor Persona Replication

### 6.1 The Use Case

Music attribution creates a natural demand for persona replication at several levels:

- **Famous producers as mentors.** An emerging artist might benefit from a Rick Rubin-like attribution advisor that channels the producer's philosophy about creative credits and collaborative attribution. The persona would not replicate Rubin's voice (unless authorized) but would emulate his known perspectives on creative process and credit allocation.

- **Artist digital twins for fan interaction.** Artists with established catalogs could deploy digital twins that answer attribution questions about their work -- "Why did you choose to credit the string section as co-writers on track 7?" -- in their own communication style and, potentially, their own voice.

- **Mentor personas for emerging artists.** The music industry lacks accessible mentorship at scale. AI personas modeled on successful artists' publicly available interviews and statements could provide guidance on attribution best practices, though with clear disclaimers about the synthetic nature of the advice.

### 6.2 Implementation Approaches

**Suno Personas.** Suno's Personas feature (2025) captures the style, vocals, and "vibe" of a track and saves it as a reusable creative asset. The system infers vocal characteristics from mixed songs -- extracting voice qualities from complete tracks where vocals are blended with instrumentation. This approach enables vocal consistency across multiple AI-generated songs but suffers from precision limitations inherent in source separation: vocal drift and tone inconsistency are documented issues that prompted a December 2025 update specifically targeting vocal consistency.

**Soundverse DNA.** Soundverse takes a consent-first approach with its DNA feature: artists explicitly upload their own songs to train a private AI model, with ownership verification at the review stage. The platform provides several provenance mechanisms: audio watermarking (inaudible fingerprints for cross-platform identification), license tagging (rights metadata preserved through ingestion, editing, and export), and digital consent markers linking training materials to verified rights holders. Artists retain full ownership of their DNA model and can set pricing ($0.99--$9.99 per export) for others to use it, earning ongoing revenue.

**IBM/Stanford Digital Twins (2024).** Park et al. conducted two-hour AI-led interviews with 1,052 U.S. adults selected to represent national demographics across age, race, gender, ethnicity, education, and political ideology. The AI interviewer generated personalized follow-up questions -- an average of 82 per session -- producing transcripts averaging 6,500 words. The resulting digital twins matched their human counterparts' General Social Survey answers with 85% accuracy, which is approximately as consistent as the human subjects who matched their own answers when retested two weeks later. This finding establishes a ceiling for digital twin fidelity: if humans are only 85% consistent with themselves across a two-week gap, an 85%-accurate digital twin is arguably indistinguishable from the variance in human self-consistency.

> Park, J. S. et al. (2024). A mega-study of digital twins reveals strengths, weaknesses and opportunities for further improvement. [arXiv:2509.19088](https://arxiv.org/abs/2509.19088)

### 6.3 NVIDIA PersonaPlex

PersonaPlex (NVIDIA, January 2026) is a 7-billion-parameter, open-source (MIT + Open Model licenses) speech-to-speech model that combines full-duplex conversation with persona control through dual-input conditioning.

**Dual-Input System.** Before conversation begins, PersonaPlex is conditioned on two prompts: (1) a voice prompt -- a sequence of audio tokens establishing vocal characteristics and speaking style; and (2) a text prompt -- specifying persona attributes such as role, background, and scenario context. Together, these prompts define the model's conversational identity throughout the interaction.

**Full-Duplex Architecture.** PersonaPlex runs in a dual-stream configuration where listening and speaking occur concurrently, enabling the model to update its internal state based on the user's ongoing speech while producing fluent output audio.

**Latency.** The model achieves 0.07-second speaker-switch latency in controlled conditions, with 0.170 seconds for smooth turn-taking and 0.240 seconds for user interruption handling. For context, NVIDIA reports that PersonaPlex outpaces Gemini Live in latency by a factor of 18x.

**Voice Profiles.** The current version offers 16 ready-made voice profiles with plans for custom voice support. The model supports persona switching within a conversation while maintaining voice consistency.

**Relevance to Attribution.** PersonaPlex's dual-input conditioning maps directly to the attribution agent's needs: the text prompt defines the agent's role (attribution assistant, mentor persona, digital twin) while the voice prompt establishes the vocal identity. The sub-200ms latency for persona switching would enable seamless transitions between, say, a neutral attribution report and a mentor-style commentary on the same data.

> NVIDIA Research. (2026). PersonaPlex: Voice and role control for full-duplex conversational AI. [NVIDIA ADLR](https://research.nvidia.com/labs/adlr/personaplex/)

### 6.4 Voice + Persona Co-Adaptation

Three systems demonstrate the emerging capability to co-adapt voice characteristics and persona attributes:

**P2VA (arXiv:2505.17093).** P2VA (Persona-to-Voice-Attribute) is the first framework to automatically generate voice specifications from textual persona descriptions. The system offers two strategies: P2VA-C (closed-ended) converts persona traits into structured voice attributes (gender, speed, accent), while P2VA-O (open-ended) produces free-form natural language style descriptions. Evaluation shows P2VA-C reduces word error rate by 5% and improves mean opinion score by 0.33 points. Critically, the research also discovers that current LLMs embed societal biases in voice attribute generation -- a male executive persona is assigned a deeper, slower voice than a female artist persona, even when the persona descriptions are otherwise parallel.

> P2VA Team. (2025). Voicing personas: Rewriting persona descriptions into style prompts for controllable text-to-speech. [arXiv:2505.17093](https://arxiv.org/abs/2505.17093)

**Sesame CSM.** Sesame's Conversational Speech Model (February 2025) introduces the concept of "voice presence" -- the combination of emotional intelligence, timing, pauses, interruptions, emphasis, tone, style, and consistency that makes voice interaction feel authentic. CSM frames speech generation as an end-to-end multimodal learning task, leveraging conversation history to produce contextually coherent speech. The model adjusts prosody based on conversational context: it speaks more softly when the topic is sensitive, pauses appropriately before important information, and modulates emphasis based on the semantic weight of content.

**Hume EVI 3.** Hume's Empathic Voice Interface 3 (May 2025) supports over 100,000 custom voices, each with an inferred personality derived from the prosodic characteristics of the voice. The system generates new voices and personalities from natural language descriptions ("create a voice that sounds like a calm, authoritative teacher") and adapts emotional expression in real-time based on the user's speech patterns -- pitch, prosody, pauses, and vocal bursts. In blind comparisons with GPT-4o's voice mode, EVI 3 was rated higher on empathy, expressiveness, naturalness, interruption quality, response speed, and audio quality.

### 6.5 Ethical Boundaries for Attribution Persona Replication

The technical capabilities described above create a spectrum of persona replication, each with distinct ethical requirements:

| Replication Level | Description | Ethical Requirements | A-Level Mapping |
|------------------|-------------|---------------------|-----------------|
| **Style emulation** | Agent adopts communication patterns (terse, verbose, technical) without claiming identity | Minimal -- standard UI personalization | A0--A1 |
| **Role persona** | Agent acts as "a producer-like mentor" without referencing a specific individual | Moderate -- must disclaim synthetic nature | A1 |
| **Named persona** | Agent is presented as channeling a specific public figure's known views | Significant -- requires clear labeling as synthetic; ideally requires public figure's consent | A2 |
| **Digital twin** | Agent replicates a specific individual's voice, style, and knowledge for interactive use | Maximum -- requires explicit, revocable consent; voice rights licensing; ongoing audit trail | A3 |

The critical design principle is **escalating consent**: as the fidelity of persona replication increases, the consent requirements must escalate proportionally. A style emulation requires no special consent. A full digital twin requires explicit, granular, revocable authorization from the individual being replicated, with ongoing audit trails and compensation mechanisms.

For the music attribution scaffold, the recommended approach is to support only style emulation (A0--A1) in the initial release, with named personas and digital twins gated behind explicit artist authorization workflows that integrate with the MCP consent infrastructure described in the companion manuscript.

---

## 7. Music Industry Consent Infrastructure

The technical capabilities described in Sections 2--6 exist within a rapidly evolving regulatory and industry governance landscape. Music attribution voice agents -- particularly those involving persona replication -- must navigate consent frameworks at multiple levels.

### 7.1 NILV Rights Protections (Warner Music Group)

Warner Music Group has established the most explicit major-label position on Name, Image, Likeness, and Voice (NILV) rights in the AI context: "The use of our copyrighted music and our artists' NILV rights to train AI engines and to create output from those models should require a free-market license." WMG demands that AI companies maintain "sufficiently detailed records of the copyrighted music and NILV rights used to train their models" to enable rights enforcement. This position was operationalized in late 2025 through licensing deals with Suno and Udio that establish frameworks for AI music generation with rights holder participation.

### 7.2 GEMA AI Charter

Germany's GEMA (the dominant European music rights society) launched an AI Charter defining ten ethical and legal principles for interaction between human creativity and generative AI. The charter's "digital humanism" principle asserts that AI development is obligated to serve human well-being and must not displace human creativity, "especially not by exploiting pre-existing creative work." Key principles include: mandatory intellectual property protection (creators decide how their works are used), transparency about training data content, and fair compensation through new licensing models. GEMA's position was reinforced by a November 2025 Munich court ruling that OpenAI had violated copyright laws in training ChatGPT.

### 7.3 Water & Music Ethics Playbook 2025

Water & Music's research tracked over 400 music industry organizations that published or co-signed nearly 20 ethics statements and rights declarations between 2023 and 2024. The 2025 Playbook documents the shift from principle-setting to implementation: standardized licensing frameworks, technical infrastructure for monitoring AI training usage, and market-based compensation models being developed before regulatory intervention. Key findings include the convergence between major label and independent label positions (Merlin's December 2024 policy mirrors major-label requirements for advance licensing) and the emerging revenue opportunity from training data licensing.

### 7.4 FTC AI Companion Investigation (September 2025)

On September 11, 2025, the Federal Trade Commission issued Section 6(b) orders to seven companies operating consumer-facing AI companion chatbots. The investigation focuses on: safety practices for companion-acting chatbots (especially regarding children), monetization and engagement optimization practices, character design and approval processes, and compliance with COPPA (Children's Online Privacy Protection Act). While not directly targeting music attribution, the FTC inquiry establishes regulatory precedent for AI systems that build persistent personal relationships with users -- a category that includes personalized voice agents with memory.

### 7.5 PRAC3 to A0--A3 Assurance Level Mapping

The PRAC3 framework (Privacy, Reputation, Accountability, Consent, Credit, Compensation) was developed from qualitative interviews with 20 professional voice actors to capture the risks of vocal identity replication in AI systems. PRAC3 extends the earlier C3 (Consent, Credit, Compensation) framework by foregrounding how privacy risks are amplified through non-consensual training and how reputational harm arises from decontextualized deployment.

PRAC3 maps naturally onto the A0--A3 assurance levels defined in the companion manuscript:

| PRAC3 Dimension | A0 (None) | A1 (Single Source) | A2 (Multi-Source) | A3 (Artist-Verified) |
|----------------|-----------|--------------------|--------------------|---------------------|
| **Privacy** | No privacy controls | Basic anonymization | Aggregated metrics only | User-sovereign data (Puda-style) |
| **Reputation** | No reputational safeguards | Disclaimer present | Provenance chain visible | Real-time artist approval |
| **Accountability** | No audit trail | Log-based audit | Multi-party audit | On-chain attestation |
| **Consent** | No consent mechanism | Terms-of-service consent | Granular permission per use | MCP-mediated machine-readable consent |
| **Credit** | No credit attribution | Automated credit | Multi-source verified credit | Artist-confirmed credit |
| **Compensation** | No compensation | Flat fee | Usage-based royalty | Smart-contract royalty with real-time settlement |

> PRAC3 Team. (2025). PRAC3 (Privacy, Reputation, Accountability, Consent, Credit, Compensation): Long-tailed risks of voice actors in AI data-economy. *Proceedings of AAAI/ACM Conference on AI, Ethics, and Society*. [arXiv:2507.16247](https://arxiv.org/abs/2507.16247)

The NO FAKES Act (Nurture Originals, Foster Art, and Keep Entertainment Safe Act of 2025), reintroduced in both the Senate and House in April 2025, would establish a federal right of publicity covering digital replicas of an individual's voice and visual likeness. The proposed legislation provides a private right of action with statutory damages and a DMCA-style takedown procedure. The right would extend 70 years post-mortem if renewed every ten years. The bill has broad support from SAG-AFTRA, UMG, OpenAI, Warner Music Group, and the RIAA, though the EFF has raised concerns about potential First Amendment implications.

---

## 8. The Power User Economics Trap

### 8.1 The Revenue-Cost Inversion

The economics of hyperpersonalized voice agents are structurally challenging. The most engaged users -- those who derive the most value from personalization -- are also the most expensive to serve. This creates a revenue-cost inversion where the users a company most wants to retain are the users who generate the highest infrastructure costs.

**Character.AI.** The starkest example is Character.AI, which achieved approximately $32.2M in annualized revenue in 2025 with 20 million monthly active users while facing infrastructure costs that dwarfed revenue. The company explored a sale or new funding amid mounting compute bills, eventually accepting a $1 billion valuation -- a 33x revenue multiple reflecting the gap between user engagement and monetization. The fundamental problem: free-tier users consume significant compute (each conversation turn requires LLM inference), and conversion to paid tiers has been insufficient to cover serving costs.

**AI Companion Market.** The broader AI companion market generated approximately $82 million in the first half of 2025, on track for $120 million by year-end. However, the top 10% of apps capture 89% of revenue, and only about 33 apps (10% of the category) have exceeded $1 million in lifetime consumer spending. The economics are winner-take-most with structurally thin margins.

### 8.2 Voice as a Cost Multiplier

Voice interaction dramatically amplifies the cost problem. A text-based conversation might cost $0.001--$0.01 per turn in LLM inference. Adding voice introduces:

| Component | Cost per Minute | Notes |
|-----------|----------------|-------|
| **STT (Speech-to-Text)** | $0.006--$0.024 | Whisper API vs. on-device (amortized HW cost) |
| **LLM Inference** | $0.002--$0.030 | Haiku vs. Sonnet-class, depends on context length |
| **TTS (Text-to-Speech)** | $0.015--$0.100 | ElevenLabs Pro vs. on-device Kokoro/Orpheus |
| **WebRTC Transport** | $0.005--$0.010 | Managed service (Daily/LiveKit Cloud) |
| **Total per minute** | $0.028--$0.164 | 10--50x more expensive than text-only |

For a power user engaging in 30 minutes of voice interaction daily, the daily serving cost ranges from $0.84 to $4.92. At the high end, serving a single highly engaged user costs approximately $150/month -- far exceeding any realistic subscription price.

### 8.3 Credit-Based Pricing as the Sustainable Model

The only economically sustainable model for voice-enabled attribution agents is credit-based pricing that makes cost visible and controllable:

| Tier | Monthly Price | Capabilities | Target User |
|------|--------------|-------------|-------------|
| **Free** | $0 | Text-only attribution queries; 50 queries/month; basic confidence display | Casual listeners; evaluation users |
| **Premium** | $19--29/month | Voice interaction (120 min/month); full confidence dashboard; batch operations; memory-augmented personalization | Artists; rights holders |
| **Pro** | $49--99/month | Unlimited voice; digital twin creation (one persona); API access; multi-catalog analytics; priority confidence recalculation | Labels; publishers; professional studios |

The credit-based model has several advantages over flat-rate pricing:

1. **Cost alignment**: Heavy users pay proportionally to their resource consumption
2. **Behavioral feedback**: Users self-moderate when they see credit balances declining
3. **Upsell surface**: Running low on credits creates a natural upgrade moment
4. **Abuse prevention**: Rate limits are built into the pricing model rather than requiring separate enforcement

### 8.4 The Digital Twin Premium

Celebrity digital twin functionality represents the highest-margin opportunity in the stack, precisely because it requires the most compute but also commands the highest willingness-to-pay:

- **Voice cloning** requires initial compute for profile creation (reference audio processing, embedding generation) but amortizes well across subsequent interactions
- **Persona fine-tuning** requires curated training data from the artist's public communications, interviews, and potentially direct input sessions
- **Ongoing serving** is comparable to standard voice interaction but with additional persona-conditioning overhead

The pricing model for digital twins should separate creation costs (one-time) from usage costs (per-minute/per-query), with the artist receiving a revenue share on any third-party usage of their digital twin.

### 8.5 Lessons from the Companion Market

The AI companion market's struggles offer cautionary lessons for music attribution voice agents:

1. **Do not offer unlimited voice in free tiers.** Character.AI's economics collapsed because free-tier users consumed disproportionate compute. The attribution agent's free tier must be text-only, with voice reserved for paying users.

2. **Voice minutes are the scarce resource, not queries.** A text query costs fractions of a cent; a voice conversation costs dollars per hour. Pricing should be anchored to voice minutes, not query counts.

3. **Personalization depth should correlate with tier.** Free-tier users get segment-level personalization (four archetypes). Premium users get behavioral profiling with memory. Pro users get full digital twin capabilities. This creates genuine upgrade incentives beyond just "more queries."

4. **Monitor engagement for cost exposure.** Implement real-time cost tracking per user, with alerts when a user's serving cost exceeds their revenue contribution. This enables proactive intervention (usage nudges, tier upgrade prompts) before costs become unsustainable.

5. **On-device inference is the long-term hedge.** As on-device STT (Whisper) and TTS (Kokoro, Orpheus) mature, the cost structure shifts from per-minute API fees to amortized hardware costs. Teams should architect for a hybrid future where on-device components handle the expensive audio pipeline while cloud LLMs handle the relatively cheaper text inference.

---

## 9. Synthesis and Recommendations

### 9.1 Architecture Recommendation

For the music attribution scaffold, the recommended memory architecture is a **layered hybrid** combining Mem0's plug-and-play integration (for rapid prototyping) with Zep/Graphiti's temporal knowledge graph (for production-grade provenance). The layered approach:

- **Layer 1 (Session)**: Standard LLM context window manages the current conversation
- **Layer 2 (User Profile)**: Mem0 or equivalent manages cross-session user preferences and archetype classification
- **Layer 3 (Domain Knowledge)**: Zep/Graphiti manages the temporal knowledge graph of attribution facts, rights ownership history, and confidence evolution

### 9.2 Personalization Safety Checklist

Based on the research surveyed in this document, every personalized attribution response should pass through these gates:

| Gate | Check | Action on Failure |
|------|-------|-------------------|
| **Relevance** | Is retrieved user memory relevant to this query? | Suppress irrelevant memories (Self-ReCheck) |
| **Factual grounding** | Do factual claims match database evidence? | Override memory-derived claims with database facts |
| **Sycophancy** | Does the response disproportionately validate the user's position? | Inject balanced evidence from competing sources |
| **Privacy** | Does the response reveal information from other users' interactions? | Block cross-user information leakage |
| **Intent** | Could this query be exploiting persona context to bypass safety? | Apply stateless safety check in parallel with personalized response |

### 9.3 Open Research Questions

Several questions remain open as of February 2026:

1. **Memory compaction for long-term users.** How should an agent compress years of interaction history without losing critical personalization signals? The session summarization approach (Memoria) and knowledge graph approach (Zep) offer different trade-offs that have not been systematically compared in production settings.

2. **Cross-modal persona consistency.** When a user interacts with the same agent via text in some sessions and voice in others, how should the persona model handle the different behavioral signals from each modality? Voice interactions reveal emotional state and urgency through prosody; text interactions reveal sophistication through vocabulary and query structure. No current system addresses cross-modal persona coherence.

3. **Multi-stakeholder personalization conflicts.** In music attribution, the same fact (e.g., a disputed credit) may be presented to multiple stakeholders with competing interests. How should the agent personalize its presentation without introducing bias? This connects to the sycophancy problem (Section 5.1) but goes further: the agent must maintain factual neutrality while adapting tone, depth, and emphasis to each stakeholder.

4. **Consent revocation propagation.** When an artist revokes consent for their digital twin, how quickly must the system propagate that revocation across all instances, cached embeddings, and derived representations? The current state of the art does not address real-time consent propagation in distributed voice agent deployments.

5. **Personalization fairness.** Do personalization systems systematically provide better experiences for some user demographics than others? P2VA's discovery of bias in voice attribute generation (Section 6.4) suggests that persona-to-voice mapping may embed societal biases. Systematic fairness auditing of personalization systems in the music domain remains unexplored.

---

## References

### Memory Architectures

- Atkinson, R. C., & Shiffrin, R. M. (1968). Human memory: A proposed system and its control processes. *The Psychology of Learning and Motivation*, 2, 89--195.
- Packer, C., Wooders, S., Lin, K., Fang, V., Patil, S. G., Stoica, I., & Gonzalez, J. E. (2023). MemGPT: Towards LLMs as operating systems. [arXiv:2310.08560](https://arxiv.org/abs/2310.08560)
- Rasmussen, P. (2025). Zep: A temporal knowledge graph architecture for agent memory. [arXiv:2501.13956](https://arxiv.org/abs/2501.13956)
- Mem0 Team. (2025). Mem0: Building production-ready AI agents with scalable long-term memory. [arXiv:2504.19413](https://arxiv.org/abs/2504.19413)
- Kang, J. et al. (2025). Memory OS of AI agent. *Proceedings of EMNLP 2025* (Oral). [arXiv:2506.06326](https://arxiv.org/abs/2506.06326)
- Memoria Team. (2025). Memoria: A scalable agentic memory framework for personalized conversational AI. [arXiv:2512.12686](https://arxiv.org/abs/2512.12686)

### User Modeling

- PersonalAlign Team. (2026). PersonalAlign: Hierarchical implicit intent alignment for personalized GUI agent with long-term user-centric records. [arXiv:2601.09636](https://arxiv.org/abs/2601.09636)
- Li, Y. et al. (2024). LLMs + Persona-Plug = Personalized LLMs. *Proceedings of ACL 2025*. [arXiv:2409.11901](https://arxiv.org/abs/2409.11901)
- Chen, A. et al. (2025). DEEPER insight into your user: Directed persona refinement for dynamic persona modeling. *Proceedings of ACL 2025*. [arXiv:2502.11078](https://arxiv.org/abs/2502.11078)
- Li, G., Liu, X., Wu, Z., & Dai, X. (2025). Persona-aware alignment framework for personalized dialogue generation. *TACL*. [DOI:10.1162/TACL.a.57](https://direct.mit.edu/tacl/article/doi/10.1162/TACL.a.57/134310/)
- DPRF Team. (2025). DPRF: A generalizable dynamic persona refinement framework. [arXiv:2510.14205](https://arxiv.org/abs/2510.14205)

### Privacy

- Puda Team. (2026). Puda: Private user dataset agent for user-sovereign and privacy-preserving personalized AI. [arXiv:2602.08268](https://arxiv.org/abs/2602.08268)
- SecFPP Team. (2025). Privacy-preserving prompt personalization in federated learning for multimodal LLMs. [arXiv:2505.22447](https://arxiv.org/abs/2505.22447)
- Apple PPML Workshop. (2025). [machinelearning.apple.com/updates/ppml-2025](https://machinelearning.apple.com/updates/ppml-2025)

### Over-Personalization and Safety

- Aguirre, E., Mahr, D., Grewal, D., de Ruyter, K., & Wetzels, M. (2015). Unraveling the personalization paradox. *Journal of Retailing*, 91(1), 34--49.
- OP-Bench Team. (2026). OP-Bench: Benchmarking over-personalization for memory-augmented personalized conversational agents. [arXiv:2601.13722](https://arxiv.org/abs/2601.13722)
- PS-Bench Team. (2026). When personalization legitimizes risks: Uncovering safety vulnerabilities in personalized dialogue agents. [arXiv:2601.17887](https://arxiv.org/abs/2601.17887)

### Voice and Persona

- NVIDIA Research. (2026). PersonaPlex: Voice and role control for full-duplex conversational AI. [research.nvidia.com/labs/adlr/personaplex](https://research.nvidia.com/labs/adlr/personaplex/)
- P2VA Team. (2025). Voicing personas: Rewriting persona descriptions into style prompts for controllable TTS. [arXiv:2505.17093](https://arxiv.org/abs/2505.17093)
- Sesame. (2025). Crossing the uncanny valley of conversational voice. [sesame.com/research](https://www.sesame.com/research/crossing_the_uncanny_valley_of_voice)
- Hume AI. (2025). Introducing EVI 3. [hume.ai/blog/introducing-evi-3](https://www.hume.ai/blog/introducing-evi-3)
- Park, J. S. et al. (2024). A mega-study of digital twins reveals strengths, weaknesses and opportunities. [arXiv:2509.19088](https://arxiv.org/abs/2509.19088)

### Music Industry and Consent

- PRAC3 Team. (2025). PRAC3: Long-tailed risks of voice actors in AI data-economy. *AAAI/ACM AIES*. [arXiv:2507.16247](https://arxiv.org/abs/2507.16247)
- GEMA. (2025). AI Charter: Protection and promotion of human creativity in the era of generative AI. [gema-politik.de](https://gema-politik.de/gema-launches-ai-charter-protection-and-promotion-of-human-creativity-in-the-era-of-generative-ai/)
- Water & Music. (2025). From policy to practice: The music industry's AI ethics playbook. [waterandmusic.com](https://www.waterandmusic.com/music-industry-ai-ethics-playbook-2025/)
- FTC. (2025). FTC launches inquiry into AI chatbots acting as companions. [ftc.gov](https://www.ftc.gov/news-events/news/press-releases/2025/09/ftc-launches-inquiry-ai-chatbots-acting-companions)
- NO FAKES Act of 2025. H.R.2794, 119th Congress. [congress.gov](https://www.congress.gov/bill/119th-congress/house-bill/2794/text)
- Suno. (2025). Personas feature. [suno.com](https://suno.com/home)
- Soundverse. (2025). Soundverse DNA: AI music powered by artists. [soundverse.ai/dna](https://www.soundverse.ai/dna)

### Economics

- Character.AI statistics. (2025). [businessofapps.com/data/character-ai-statistics](https://www.businessofapps.com/data/character-ai-statistics/)
- AI companion app market. (2025). [techcrunch.com](https://techcrunch.com/2025/08/12/ai-companion-apps-on-track-to-pull-in-120m-in-2025/)

### General Surveys

- Liu, S. et al. (2025). Memory in the age of AI agents: A survey. [github.com/Shichun-Liu/Agent-Memory-Paper-List](https://github.com/Shichun-Liu/Agent-Memory-Paper-List)
- TsinghuaC3I. (2025). Awesome memory for agents. [github.com/TsinghuaC3I/Awesome-Memory-for-Agents](https://github.com/TsinghuaC3I/Awesome-Memory-for-Agents)
