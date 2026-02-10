# AI/LLM Tooling Landscape -- February 2026

> Web research conducted 2026-02-10. Intended as a **living reference** for the
> probabilistic PRD's technology-option nodes. Each section maps to a decision
> variable in the Bayesian decision network.

---

## Table of Contents

1. [LLM Providers](#1-llm-providers)
2. [AI Agent / Orchestration Frameworks](#2-ai-agent--orchestration-frameworks)
3. [MCP Ecosystem](#3-mcp-ecosystem)
4. [Agent SDKs and Inter-Agent Protocols](#4-agent-sdks-and-inter-agent-protocols)
5. [Structured Output Libraries](#5-structured-output-libraries)
6. [RAG Frameworks](#6-rag-frameworks)
7. [Embedding Models](#7-embedding-models)
8. [LLM Evaluation and Observability](#8-llm-evaluation-and-observability)
9. [Conformal Prediction Libraries](#9-conformal-prediction-libraries)
10. [Graph RAG Approaches](#10-graph-rag-approaches)

---

## 1. LLM Providers

### 1.1 Anthropic Claude Family

| Model | Released | Input $/M tok | Output $/M tok | Context | Key Capability |
|-------|----------|---------------|-----------------|---------|----------------|
| **Claude Opus 4.6** | 2026-02-05 | $5.00 | $25.00 | 1M (beta) | Adaptive thinking, 72.7% OSWorld, 80.8% SWE-bench Verified, 128K max output, agent teams |
| **Claude Sonnet 4.5** | 2025 | $3.00 | $15.00 | 200K | Hybrid reasoning, best cost/performance for dev productivity |
| **Claude Haiku 4.5** | 2025 | $1.00 | $5.00 | 200K | Fastest, extended thinking support |
| **Claude Opus 4.5** | 2025 | $5.00 | $25.00 | 200K | Long-horizon coding, 65% fewer tokens than competitors |

**What is new since mid-2025:**
- **Opus 4.6** (Feb 2026): Adaptive thinking replaces extended thinking as the recommended reasoning mode -- Claude dynamically decides when and how much to reason. Context compaction enables infinite conversations via server-side summarization. Agent Teams allow orchestrating multiple Claude Code instances with a lead agent coordinating teammates.
- **1M context window** now available for Opus 4.6, Sonnet 4.5, and Sonnet 4.
- Prompt caching offers up to 90% cost savings; batch processing offers 50% savings.

**When to use:** Opus 4.6 for complex agentic workflows, multi-file coding, and computer use. Sonnet 4.5 for day-to-day development where cost matters. Haiku 4.5 for high-volume classification/extraction.

**Maturity:** Production. Claude is the strongest coding/agentic model as of Feb 2026 per benchmarks.

Sources:
- [Claude Opus 4.6 Product Page](https://www.anthropic.com/claude/opus)
- [Claude Pricing Documentation](https://platform.claude.com/docs/en/about-claude/pricing)
- [Claude Opus 4.6 Features and Benchmarks](https://www.digitalapplied.com/blog/claude-opus-4-6-release-features-benchmarks-guide)
- [Claude Opus 4.6 vs 4.5 Benchmarks](https://www.vellum.ai/blog/claude-opus-4-6-benchmarks)

---

### 1.2 OpenAI GPT-5 Family

| Model | Input $/M tok | Output $/M tok | Key Capability |
|-------|---------------|-----------------|----------------|
| **GPT-5** | $1.25 | $10.00 | New default ChatGPT model, replaced GPT-4o/o3/o4-mini |
| **GPT-5 Mini** | $0.25 | $2.00 | Ultra-competitive for high-volume |
| **GPT-5 Nano** | $0.05 | $0.40 | Cheapest frontier-adjacent option |
| **GPT-5.2** | TBD | TBD | Latest flagship with adaptive computation |
| **o3** (legacy) | $2.00 | $8.00 | Reasoning model, succeeded by GPT-5 |
| **o4-mini** (legacy) | $1.10 | $4.40 | Fast reasoning, succeeded by GPT-5 Mini |

**What is new since mid-2025:**
- **GPT-5** launched as the unified default model, replacing GPT-4o, o3, o4-mini, GPT-4.1, and GPT-4.5 for signed-in users.
- **GPT-5.2** is the latest flagship with three modes (Auto, Instant, Thinking), improved reasoning, reduced hallucinations, and adaptive computation.
- GPT-5 performs better than o3 with 50-80% fewer output tokens across visual reasoning, agentic coding, and scientific problem solving.
- Aggressive pricing: GPT-5 at $1.25/M input is half the price of GPT-4o ($2.50/M) while matching or exceeding capabilities.

**When to use:** GPT-5 for general-purpose tasks at excellent price/performance. GPT-5 Nano for embedding-adjacent cheap inference. o3/o4-mini are legacy but still available.

**Maturity:** Production. GPT-5.2 is the latest; ecosystem tooling fully supports the GPT-5 family.

Sources:
- [Introducing GPT-5 - OpenAI](https://openai.com/index/introducing-gpt-5/)
- [OpenAI Pricing](https://platform.openai.com/docs/pricing)
- [OpenAI Pricing in 2026](https://www.finout.io/blog/openai-pricing-in-2026)

---

### 1.3 Google Gemini 2.5

| Model | Input $/M tok | Output $/M tok | Context | Key Capability |
|-------|---------------|-----------------|---------|----------------|
| **Gemini 2.5 Pro** | $1.25 | $10.00 | 1M | Thinking model, code/math/STEM, long context |
| **Gemini 2.5 Flash** | $0.30 | $2.50 | 1M | Fast thinking, agentic, large-scale processing |
| **Gemini 2.5 Flash-Lite** | Lower | Lower | - | Throughput-optimized |

**What is new since mid-2025:**
- **Thinking budget control**: developers choose when and how much the model "thinks" before responding.
- **Context caching** reduces costs by up to 75% for applications with large, repeated prompts.
- Costs increase above 200K input tokens for Pro, affecting long-document use cases.
- Free tier includes Flash and limited Pro access.

**When to use:** Best for cost-sensitive RAG pipelines (Flash), long-document analysis (Pro with 1M context), and Google Cloud-native deployments.

**Maturity:** Production. Strong Vertex AI integration.

Sources:
- [Gemini Models Documentation](https://ai.google.dev/gemini-api/docs/models)
- [Gemini 2.5 Thinking Model Updates](https://developers.googleblog.com/en/gemini-2-5-thinking-model-updates/)
- [Gemini Pricing in 2026](https://www.finout.io/blog/gemini-pricing-in-2026)

---

### 1.4 Open-Source / Open-Weight Models

| Model | Parameters | License | Key Capability |
|-------|-----------|---------|----------------|
| **Llama 4 Scout** | MoE | Meta license | 128K context, strong general performance |
| **Llama 4 Maverick** | MoE | Meta license | Instruction-tuned, 128K context |
| **Llama 4 Behemoth** | 2T (MoE) | Meta license | Largest open model, selective expert activation |
| **DeepSeek V3.2** | MoE | MIT | Sparse attention, thinking/non-thinking modes |
| **DeepSeek R1** | - | MIT | Reasoning-first, shows chain-of-thought transparently |
| **DeepSeek R2** | - | Expected MIT | Expected mid-Feb 2026, revolutionary reasoning upgrades |
| **Qwen 3** | 4B/30B/235B | Apache 2.0 | 92.3% on AIME25 math, thinking + non-thinking variants |
| **Qwen 3.1** | - | Apache 2.0 | Better code generation |
| **Mistral Large** | - | Apache 2.0 | Balanced 85-90% of Qwen 3, easier to deploy |
| **Devstral 2** | - | Mistral license | Agentic coding with vision, tool use for codebases |

**What is new since mid-2025:**
- **Llama 4** family with MoE architecture (Behemoth at 2T parameters), competing with closed models.
- **DeepSeek V3.1** (Aug 2025) and **V3.2-Exp** (Sep 2025) with hybrid thinking/non-thinking modes. R2 expected imminently (Feb 2026) after Huawei Ascend training delays forced pivot back to NVIDIA.
- **Qwen 3** leads in math (92.3% AIME25) and coding benchmarks. Qwen 3.1 already out.
- **Devstral 2** adds vision to agentic coding.

**When to use:** Qwen 3 for math/coding tasks on self-hosted infrastructure. Llama 4 for general-purpose open-weight needs. DeepSeek R1/R2 when reasoning transparency matters. Mistral for easiest deployment of a competitive open model.

**Maturity:** Production for Qwen 3, Llama 4, DeepSeek V3.x. R2 is pre-release.

Sources:
- [Open-Source LLMs on Hugging Face](https://huggingface.co/blog/daya-shankar/open-source-llms)
- [Best Open Source LLMs 2026](https://contabo.com/blog/open-source-llms/)
- [DeepSeek Technical Tour](https://magazine.sebastianraschka.com/p/technical-deepseek)
- [DeepSeek R1 vs Qwen 3 vs Mistral Large Comparison](https://www.digitalapplied.com/blog/deepseek-r1-vs-qwen-3-vs-mistral-large-comparison)

---

## 2. AI Agent / Orchestration Frameworks

### 2.1 Comparison Matrix

| Framework | Architecture | Best For | Maturity | GitHub Stars (approx) |
|-----------|-------------|----------|----------|----------------------|
| **LangGraph** | Graph-based stateful orchestration | Controllable agents, human-in-the-loop, retries | High | 10K+ |
| **CrewAI** | Role-based multi-agent crews | SOP-style workflows, human-readable configs | High | 25K+ |
| **AutoGen** | Event-driven multi-agent | Flexible dialogues, Studio UI prototyping | High | 40K+ |
| **PydanticAI** | Type-safe tool contracts | Schema-safe tools, structured I/O, Pydantic ecosystem | Medium-High | 10K+ |
| **smolagents** | Ultra-minimal Python | Quick prototyping, any LLM, readability | Medium | 15K+ |
| **Agno** (ex-Phidata) | Multi-modal agent runtime | Memory + knowledge + tools, plug-and-play LLMs | Medium-High | 20K+ |
| **DSPy** | Declarative compilation | Prompt optimization, auto-tuning weights | Medium-High | 20K+ |
| **Instructor** | Structured extraction | Type-safe LLM outputs, validation, retries | High | 11K+ |
| **Mirascope** | Multi-provider LLM abstraction | Prompt engineering, chaining, structured output | Medium | 2K+ |
| **Marvin** | High-level task functions | Quick cast/classify/extract, OpenAI only | Medium | 5K+ |

### 2.2 Detailed Notes

**LangGraph** achieved the lowest latency and token usage across benchmarks thanks to graph-based approach reducing redundant context passing. Purpose-built for long-running, stateful agents with explicit control over nodes, edges, retries, and human-in-the-loop. Pairs with LangSmith for observability.

**CrewAI** provides human-readable multi-agent "crews" with roles, tasks, tools, and memory. Best for teams that think in terms of job descriptions and standard operating procedures.

**AutoGen** uses an event-driven architecture with robust recipes and optional Studio UI for visual prototyping. Conversation-based approach gives natural, flexible multi-agent dialogues.

**PydanticAI** is the official agent runtime from the Pydantic team. Adds typed tools, replayable datasets, evals, and production dashboards while using Pydantic models natively. Best when parameter correctness and type safety are critical.

**smolagents** (by Hugging Face) is ultra-minimal -- easy to read, extend, and works with any LLM. Best for learning and quick experiments.

**Agno** (formerly Phidata) provides agents with persistent memory, knowledge accumulation, and tool integrations. Supports OpenAI, Anthropic, Gemini, and open-source models via Ollama. Plug-and-play architecture.

**DSPy 3.1** (Stanford) takes a radically different approach: you program with modules, and DSPy's optimizers compile your program into effective prompts/weights. Version 3.0+ introduced human-in-the-loop optimizers. Best for teams that want to decouple logic from prompt engineering.

**What is new since mid-2025:**
- LangGraph solidified as the performance leader for stateful agents.
- PydanticAI matured into a full agent runtime (beyond just structured output).
- Agno rebranded from Phidata with enhanced multi-modal support.
- DSPy 3.0/3.1 introduced new optimizer paradigm with human-in-the-loop feedback.
- OpenAI Agents SDK emerged as a serious lightweight option (see Section 4).

**PRD relevance:** The framework choice is heavily conditional on team archetype. Engineer-Heavy teams gravitate to LangGraph or DSPy; Musician-First teams to CrewAI or Agno; Solo Hackers to smolagents or Instructor.

Sources:
- [Top 10 AI Agent Frameworks 2026](https://genta.dev/resources/best-ai-agent-frameworks-2026)
- [AI Agent Framework Comparison - Langfuse](https://langfuse.com/blog/2025-03-19-ai-agent-comparison)
- [AutoGen vs CrewAI vs LangGraph vs PydanticAI](https://newsletter.victordibia.com/p/autogen-vs-crewai-vs-langgraph-vs)
- [DSPy Official Site](https://dspy.ai/)
- [Agno GitHub](https://github.com/agno-agi/agno)

---

## 3. MCP Ecosystem

### 3.1 Specification Status

| Spec Version | Date | Key Changes |
|-------------|------|-------------|
| **2025-11-25** | Nov 2025 | Latest stable. Changes to dynamic client registration. |
| **2025-06-18** | Jun 2025 | Streamable HTTP transport, OAuth 2.1 refinements, MCP servers as OAuth Resource Servers, resource indicators. |
| **Draft** | Ongoing | Further auth and security refinements. |

**Transport:** Streamable HTTP is the standard for remote MCP connections (introduced March 2025). Uses a single HTTP endpoint for bidirectional messaging. Replaces the earlier SSE-based transport for new deployments.

**Authorization:** MCP servers act as OAuth 2.1 resource servers. When authorization is required, servers return HTTP 401 with WWW-Authenticate header containing resource_metadata URL per RFC 9728.

### 3.2 Ecosystem Scale

- **1,000+ community-built MCP servers** covering Google Drive, Slack, databases, custom enterprise systems.
- **Server categories:** Reference servers (protocol maintainers), official integrations (company-maintained), community servers (independent contributors).
- **50+ enterprise partners** including Salesforce, ServiceNow, Workday, Accenture, Deloitte.
- **Major AI providers** standardized around MCP: OpenAI, Anthropic, Hugging Face, LangChain.

### 3.3 2026 Outlook

2026 is the year of enterprise MCP adoption. The framework is reaching full standardization with alignment to global compliance frameworks. Key focus areas:
- Enterprise-grade auth and security
- Compliance alignment (GDPR, AI Act)
- Production hardening of the Streamable HTTP transport

**What is new since mid-2025:**
- Specification 2025-11-25 changed dynamic client registration approach.
- OAuth 2.1 refinement as core auth mechanism.
- Ecosystem crossed 1,000 servers.
- Enterprise adoption accelerating with major consulting firms.

**PRD relevance:** MCP is central to the music attribution scaffold as the consent infrastructure layer -- machine-readable permission queries for AI training rights. The specification maturity directly affects the A0-A3 assurance level implementation.

Sources:
- [MCP Specification 2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25)
- [2026: The Year for Enterprise-Ready MCP Adoption](https://www.cdata.com/blog/2026-year-enterprise-ready-mcp-adoption)
- [Why the Model Context Protocol Won](https://thenewstack.io/why-the-model-context-protocol-won/)
- [MCP Specs Update from June 2025](https://auth0.com/blog/mcp-specs-update-all-about-auth/)
- [MCP Authorization - Stack Overflow Blog](https://stackoverflow.blog/2026/01/21/is-that-allowed-authentication-and-authorization-in-model-context-protocol/)

---

## 4. Agent SDKs and Inter-Agent Protocols

### 4.1 Vendor Agent SDKs

| SDK | Vendor | Key Features | Model Lock-in |
|-----|--------|-------------|---------------|
| **OpenAI Agents SDK** | OpenAI | Lightweight, production-ready, few abstractions, open-source, successor to Swarm | OpenAI-first but extensible |
| **Claude Agent SDK** | Anthropic | Agent teams, tool use, computer use, composable with other agents | Claude-first |
| **Google ADK** | Google | Model-agnostic, deployment-agnostic, framework-compatible, A2A native | Model-agnostic |
| **Semantic Kernel** | Microsoft | Enterprise agent framework, multi-provider, A2A support | Multi-provider |

**OpenAI Agents SDK** is the production-ready upgrade of Swarm. Fully open-source and free. Nearly matched LangGraph in efficiency benchmarks. Best for teams already in the OpenAI ecosystem.

**Claude Agent SDK** enables composing Claude agents with other agents (Azure OpenAI, OpenAI, GitHub Copilot) in sequential, concurrent, handoff, and group chat workflows. Full A2A protocol support.

**Google ADK** is the most framework-agnostic option. Built for compatibility with other frameworks and supports A2A natively. Best for multi-cloud, multi-model deployments.

### 4.2 Inter-Agent Protocols

| Protocol | Origin | Status | Purpose |
|----------|--------|--------|---------|
| **MCP** | Anthropic | Production (spec 2025-11-25) | Tool/context access for LLM applications |
| **A2A** | Google -> Linux Foundation | Early production | Agent-to-agent communication and task coordination |
| **ACP** | IBM | Merged into A2A | Originally for BeeAI platform, now unified |
| **UTCP** | Emerging | Draft | Universal tool calling protocol |

**A2A Protocol** has been donated to the Linux Foundation and merged with IBM's ACP. Uses JSON-over-HTTP with SSE/webhooks for real-time communication. Defines task lifecycle (discovery, authorization, communication). 88% of surveyed executives plan to increase agentic AI budgets. However, A2A is still maturing -- expect improvements as it stabilizes.

**What is new since mid-2025:**
- OpenAI Agents SDK launched as production-ready Swarm replacement.
- A2A donated to Linux Foundation and merged with IBM's ACP.
- Claude Agent SDK gained agent teams and A2A compatibility.
- Gartner predicts 40% of enterprise apps will feature task-specific AI agents by 2026.
- "Protocol soup" is consolidating: MCP for tool access, A2A for agent communication.

**PRD relevance:** The MCP-as-consent-infrastructure concept from the manuscript maps directly here. The choice between MCP-only vs. MCP+A2A affects the architecture's complexity and interoperability.

Sources:
- [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/)
- [Google ADK Documentation](https://google.github.io/adk-docs/)
- [A2A Protocol](https://a2a-protocol.org/latest/)
- [Top AI Agent Protocols in 2026](https://getstream.io/blog/ai-agent-protocols/)
- [Agentic AI Protocols - The Register](https://www.theregister.com/2026/01/30/agnetic_ai_protocols_mcp_utcp_a2a_etc/)
- [Claude Agent SDK with Microsoft Agent Framework](https://devblogs.microsoft.com/semantic-kernel/build-ai-agents-with-claude-agent-sdk-and-microsoft-agent-framework/)

---

## 5. Structured Output Libraries

### 5.1 Comparison Matrix

| Library | Approach | Multi-Provider | Streaming | Validation | Stars |
|---------|----------|---------------|-----------|------------|-------|
| **Instructor** | Pydantic + retry loop | 15+ providers | Partial streaming, list streaming | Pydantic + Tenacity retries | 11K+ |
| **PydanticAI** | Full agent runtime | Multi-provider | Yes | Pydantic native | 10K+ |
| **Outlines** | Constrained token sampling | Local models | Yes | Grammar-constrained | 10K+ |
| **Guidance** | Constrained token sampling | Local models | Yes | Template-based | 19K+ |
| **Mirascope** | Multi-provider abstraction | 10+ providers | Yes | Pydantic | 2K+ |
| **Marvin** | High-level task API | OpenAI only | Limited | Built-in | 5K+ |

### 5.2 Detailed Notes

**Instructor** is the most popular library (3M+ monthly downloads). Works by patching LLM client libraries to add Pydantic validation and automatic retries. Supports multimodal inputs (images, PDFs, audio) with a unified API across providers. Multi-language: Python, TypeScript, Ruby, Go, Elixir.

**PydanticAI** started as structured output but has grown into a full agent runtime with typed tools, replayable datasets, evals, and production dashboards. Use Instructor for fast extraction; PydanticAI when you need the full agent lifecycle.

**Outlines** uses constrained token sampling -- if you control the token generation process, this is the most efficient approach. Supports Pydantic models for defining schemas. Best for local/self-hosted models where you have access to logits.

**Guidance** is similar to Outlines but uses a template-based approach. More mature but slightly harder to use than Outlines.

**Mirascope** provides a unified interface across 10+ providers with prompt engineering techniques and chaining. Wider scope than Instructor but smaller community.

**Marvin** has the simplest syntax with many built-in tasks (cast, classify, extract, generate) but is limited to OpenAI.

**What is new since mid-2025:**
- Instructor crossed 3M monthly downloads, added multimodal support.
- PydanticAI evolved from structured output library to full agent runtime.
- Native structured output support from providers (OpenAI, Anthropic, Google) has improved, but libraries still add value through validation, retries, and multi-provider abstraction.

**PRD relevance:** For the music attribution scaffold's confidence scoring, Instructor or PydanticAI handles extracting structured attribution metadata. For self-hosted models with conformal prediction, Outlines enables grammar-constrained generation.

Sources:
- [Instructor Official Site](https://python.useinstructor.com/)
- [Instructor GitHub](https://github.com/567-labs/instructor)
- [The Best Library for Structured LLM Output](https://simmering.dev/blog/structured_output/)
- [PydanticAI vs Instructor](https://medium.com/@mahadevan.varadhan/pydanticai-vs-instructor-structured-llm-ai-outputs-with-python-tools-c7b7b202eb23)
- [Mirascope GitHub](https://github.com/mirascope/mirascope)

---

## 6. RAG Frameworks

### 6.1 Comparison Matrix

| Framework | Focus | Latency | Token Usage | Best For |
|-----------|-------|---------|-------------|----------|
| **LangChain** | General LLM apps + agents | ~10 ms overhead | ~2.4K | Complex agents with tools, largest ecosystem |
| **LlamaIndex** | RAG-specific indexing | ~6 ms overhead | ~1.6K | Indexing/retrieving from complex corpora |
| **Haystack** | Production pipelines | ~5.9 ms overhead | ~1.57K | Enterprise, clear pipeline architecture |
| **txtai** | All-in-one embeddings DB | Low | Low | Self-contained vector + LLM workflows |
| **RAGFlow** | Visual/low-code RAG | Medium | Medium | Non-developers, visual pipeline design |

### 6.2 Detailed Notes

**LangChain** remains the largest ecosystem for LLM application development. Not exclusively RAG, but comprehensive tooling for chains, agents, and retrieval. Highest community support and integrations.

**LlamaIndex** is often considered superior for RAG-specific use cases due to focused design, simpler API, and optimized indexing. The Property Graph Index (2025-2026) enables rich knowledge graph modeling with labeled property graphs. Supports keyword/synonym retrieval, free-form extraction, and modular constructors/retrievers. Recent additions include Agent Workflows with ACP integration and MCP server support.

**Haystack** (deepset) is the enterprise choice. Pre-dates the RAG hype, giving it maturity that newer frameworks lack. Pipeline-based architecture with clear data flow. Lowest overhead in benchmarks.

**txtai** combines vector storage, text processing pipelines, and LLM orchestration in one package. Best for teams wanting a self-contained stack without external dependencies.

**RAGFlow** offers an intuitive low-code interface with pre-built components and vector database integrations. Best for teams with less engineering capacity.

**What is new since mid-2025:**
- LlamaIndex Property Graph Index matured with modular constructors and multiple retrieval strategies.
- LlamaIndex added Agent Workflows with ACP/MCP integration.
- Haystack continued to lead in production performance metrics.
- RAGFlow gained traction in the low-code space.

**PRD relevance:** The framework choice maps directly to team archetype. Engineer-Heavy teams use LlamaIndex with Property Graph Index for knowledge-graph-backed attribution. Musician-First teams use RAGFlow or txtai. The LlamaIndex Property Graph Index is particularly relevant for the music attribution knowledge graph (ISRC/ISWC/ISNI relationships).

Sources:
- [15 Best Open-Source RAG Frameworks 2026](https://www.firecrawl.dev/blog/best-open-source-rag-frameworks)
- [Top 10 RAG Frameworks on GitHub - Jan 2026](https://florinelchis.medium.com/top-10-rag-frameworks-on-github-by-stars-january-2026-e6edff1e0d91)
- [RAG Frameworks: LangChain vs LangGraph vs LlamaIndex](https://research.aimultiple.com/rag-frameworks/)
- [LlamaIndex Property Graph Index](https://www.llamaindex.ai/blog/introducing-the-property-graph-index-a-powerful-new-way-to-build-knowledge-graphs-with-llms)
- [LlamaIndex Newsletter 2026-01-13](https://www.llamaindex.ai/blog/llamaindex-newsletter-2026-01-13)

---

## 7. Embedding Models

### 7.1 Comparison Matrix

| Model | Provider | Dimensions | MTEB Score | Price $/M tok | Multimodal | Open Source |
|-------|----------|-----------|------------|---------------|------------|-------------|
| **Cohere embed-v4** | Cohere | 1,536 | 65.2 | $0.12 (text), $0.47 (image) | Yes | No |
| **text-embedding-3-large** | OpenAI | 3,072 | 64.6 | $0.13 | No | No |
| **text-embedding-3-small** | OpenAI | 1,536 | - | $0.02 | No | No |
| **Jina Embeddings v4** | Jina AI | 2,048 (adjustable) | - | Free tier + paid | Yes (text + images) | Partially |
| **voyage-3** | Voyage AI | - | - | $0.06-$0.18 | No | No |
| **Nomic Embed Text V2** | Nomic AI | - | - | Self-hostable | No | Yes (open) |
| **BGE-M3** | BAAI | - | 63.0 | Free | No | Yes |
| **E5 (Microsoft)** | Microsoft | - | - | Free | No | Yes |
| **GTE** | Alibaba | - | - | Free | No | Yes |
| **mistral-embed** | Mistral | - | 77.8% accuracy | - | No | No |
| **Gemini embedding** | Google | - | - | Free | No | No |

### 7.2 Detailed Notes

**Cohere embed-v4** leads MTEB at 65.2. Multimodal (text + images). Designed to work with Cohere's Rerank model for maximize retrieval quality. Best for enterprise search with reranking.

**OpenAI text-embedding-3-large** is the safe default at 64.6 MTEB. Mature, well-documented, wide ecosystem support. The small variant at $0.02/M tokens is excellent for cost-sensitive applications.

**Jina Embeddings v4** is built on Qwen2.5-VL-3B-Instruct. Universal multimodal (text, images, visual documents). Adjustable dimensions (2,048 down to 128) for storage/performance tradeoff.

**Voyage AI** (Anthropic's recommended embedding partner) offers better performance than OpenAI at competitive pricing ($0.06-$0.18/M tokens).

**Nomic Embed Text V2** uses Mixture-of-Experts architecture. Fully open-source with focus on transparency and reproducibility. Excellent for self-hosting.

**BGE-M3, E5, GTE** are the leading open-source options. Production-ready and widely used in enterprise. Free to use and modify. E5 competes with commercial options.

**mistral-embed** achieved the highest accuracy (77.8%) in retrieval benchmarks, though on different evaluation criteria than MTEB.

**Gemini embedding** is free via Google's API, making it attractive for cost-sensitive prototyping.

**What is new since mid-2025:**
- Cohere embed-v4 launched with multimodal support and MTEB leadership.
- Jina v4 brought vision-language foundation to embeddings.
- Nomic v2 introduced MoE architecture for embeddings.
- Google offering free embeddings pushed pricing pressure across the market.

**PRD relevance:** Embedding model choice depends on deployment target. Hetzner self-hosted: use BGE-M3 or Nomic. Cloud API: OpenAI or Voyage. Multimodal (album art + text): Cohere embed-v4 or Jina v4.

Sources:
- [13 Best Embedding Models in 2026](https://elephas.app/blog/best-embedding-models)
- [Embedding Models: OpenAI vs Gemini vs Cohere](https://research.aimultiple.com/embedding-models/)
- [Best Open-Source Embedding Models 2026](https://www.bentoml.com/blog/a-guide-to-open-source-embedding-models)
- [Cohere Embed v4 Announcement](https://docs.cohere.com/changelog/embed-multimodal-v4)
- [10 Best Embedding Models 2026](https://www.openxcell.com/blog/best-embedding-models/)

---

## 8. LLM Evaluation and Observability

### 8.1 Comparison Matrix

| Platform | Type | Open Source | Key Strength | Best For |
|----------|------|------------|--------------|----------|
| **Langfuse** | Tracing + eval | Yes (MIT since Jun 2025) | 6M+ SDK installs/month, LLM-as-judge | Open-source-first teams |
| **LangSmith** | Tracing + eval | No | Deep LangChain integration | LangChain-ecosystem teams |
| **Braintrust** | Eval + monitoring | Partial | Unified eval + monitoring, strong TS/JS | Eval-first workflows, TypeScript |
| **Arize Phoenix** | Production observability | Yes | Real-time tracing/debugging, ML background | Production monitoring, debugging |
| **Maxim AI** | End-to-end platform | No | Most complete platform coverage | Comprehensive needs |
| **DeepEval** (Confident AI) | Evaluation framework | Yes | GenAI-native metrics, no ground truth needed | Testing pipelines, CI/CD |
| **Patronus AI** | Evaluation + safety | No | Lynx model for hallucination detection | Factuality, safety-critical apps |

### 8.2 Detailed Notes

**Langfuse** became fully MIT open-source in June 2025, open-sourcing previously commercial modules (LLM-as-judge evaluations, annotation queues, prompt experiments, Playground). 6M+ SDK installs/month. Best for teams that value open-source flexibility and want to self-host.

**LangSmith** is tightly integrated with LangChain/LangGraph. Best for Python-centric teams building complex agent applications within the LangChain ecosystem.

**Braintrust** excels at unified evaluation and monitoring. Strong TypeScript/JavaScript support. Enterprise-grade security with self-hosting options. Best for teams that want evaluation-first workflows.

**Arize Phoenix** focuses on production observability. Deep tracing and debugging for real-time LLM applications. Natural extension for teams with existing ML observability infrastructure.

**DeepEval** (by Confident AI) is a specialized evaluation framework with GenAI-native metrics: hallucination detection, factuality assessment, contextual appropriateness. No ground truth data required for many metrics. Works as a pytest-style testing framework for LLMs.

**Patronus AI** developed Lynx, a state-of-the-art evaluation model that outperforms GPT-4 in hallucination detection and factual accuracy assessment. Especially strong in medical and financial contexts.

**What is new since mid-2025:**
- Langfuse went fully MIT open-source (June 2025), major milestone.
- Patronus AI released Lynx evaluation model.
- Multi-agent tracing became a key differentiator across platforms.
- DeepEval continued to grow as the pytest-for-LLMs standard.

**PRD relevance:** Evaluation tooling is critical for the confidence scoring system. DeepEval for CI/CD testing of attribution confidence. Langfuse for tracing the full attribution pipeline. Patronus Lynx for verifying factual accuracy of attribution claims.

Sources:
- [Best LLM Tracing Tools 2026 - Braintrust](https://www.braintrust.dev/articles/best-llm-tracing-tools-2026)
- [Top 5 LLM Observability Platforms 2026](https://www.getmaxim.ai/articles/top-5-llm-observability-platforms-for-2026/)
- [Langfuse Alternatives 2026 - Braintrust](https://www.braintrust.dev/articles/langfuse-alternatives-2026)
- [DeepEval](https://deepeval.com/)
- [Patronus AI](https://patronus.ai/)

---

## 9. Conformal Prediction Libraries

### 9.1 Comparison Matrix

| Library | Focus | Backend | Key Feature | Maturity |
|---------|-------|---------|-------------|----------|
| **MAPIE** | General-purpose CP | scikit-learn | Classification, regression, time series, risk control | High |
| **crepes** | Lightweight CP | scikit-learn | Conformal regressors + predictive systems, fast | Medium |
| **TorchCP** | Deep learning CP | PyTorch | DNN, GNN, LLM conformal prediction, GPU-accelerated | Medium-High |
| **Fortuna** | Deep learning UQ | - | Broader uncertainty quantification with CP support | Medium |

### 9.2 Detailed Notes

**MAPIE** (scikit-learn-contrib) is the most comprehensive conformal prediction library. Computes prediction intervals/sets for regression, classification, and time series. Version 1.3.0 is the latest.

- **2026 Roadmap**: Application to LLM-as-Judge and image segmentation use cases. Introduction of exchangeability tests to verify when MAPIE can legitimately be applied. Revisiting methods with stronger focus on adaptability.
- Best for: Teams using scikit-learn-compatible models who need production-grade conformal prediction.

**crepes** is simpler and faster for basic tasks -- 10x faster than MAPIE for simple prediction intervals. Turns predictions into well-calibrated p-values and cumulative distribution functions, or prediction sets/intervals with coverage guarantees.
- Best for: Quick conformal wrapping of existing regressors/classifiers.

**TorchCP** is the PyTorch-native option, covering DNNs, GNNs, and LLMs. ~16,000 lines of code with 100% unit test coverage. GPU-accelerated batch processing achieves up to 90% reduction in inference time on large datasets. Published in JMLR (volume 26).
- **Recent updates** (Jan 2026): p-value computation, conformal predictive distributions, expanded score functions.
- Best for: Deep learning models, especially LLM uncertainty quantification.

**Fortuna** provides broader uncertainty quantification for deep learning, with conformal prediction as one component.

**What is new since mid-2025:**
- MAPIE 2026 roadmap explicitly targets LLM-as-Judge use cases.
- TorchCP published in JMLR and actively maintained (latest update Jan 30, 2026).
- TECP (Token-Entropy Conformal Prediction) emerged as a research direction for LLM-specific conformal prediction.

**PRD relevance:** This is the most directly relevant section for the scaffold's probabilistic confidence scoring. The paper's SConU confidence calibration maps to conformal prediction sets. MAPIE for traditional ML confidence scoring; TorchCP for LLM-based attribution confidence. The exchangeability assumption is important -- music attribution data may violate it, requiring MAPIE's planned exchangeability tests.

Sources:
- [MAPIE GitHub](https://github.com/scikit-learn-contrib/MAPIE)
- [MAPIE Documentation](https://mapie.readthedocs.io/)
- [crepes GitHub](https://github.com/henrikbostrom/crepes)
- [TorchCP Paper (JMLR)](http://jmlr.org/papers/v26/24-2141.html)
- [TorchCP GitHub](https://github.com/ml-stat-Sustech/TorchCP)
- [TECP: Token-Entropy Conformal Prediction](https://www.mdpi.com/2227-7390/13/20/3351)

---

## 10. Graph RAG Approaches

### 10.1 Comparison Matrix

| Framework | Lines of Code | Storage Backends | Search Modes | Best For |
|-----------|--------------|------------------|-------------|----------|
| **Microsoft GraphRAG** | Large | Multiple (Neo4j, etc.) | Local, Global, DRIFT | Production knowledge graphs, comprehensive |
| **LightRAG** | Medium | Hugging Face + local | Embedding + KG hybrid | Fast, performant, local LLM friendly |
| **nano-graphrag** | ~1,100 | NetworkX, Neo4j | Core GraphRAG | Learning, prototyping, hacking |
| **LlamaIndex PropertyGraphIndex** | Part of LlamaIndex | Neo4j, etc. | Keyword, free-form, modular | RAG-integrated knowledge graphs |

### 10.2 Detailed Notes

**Microsoft GraphRAG** is the reference implementation. Extracts knowledge graphs from unstructured text, builds community hierarchies, generates summaries, and uses these for RAG tasks. Three search modes:
- **Local Search**: Finds entities/relationships relevant to a query.
- **Global Search**: Uses community summaries for broad questions.
- **DRIFT Search**: Dynamic, iterative retrieval combining local and global.
Best for: Comprehensive enterprise knowledge graph applications with diverse query types.

**LightRAG** combines knowledge graph attributes with embedding-based retrieval. Built on nano-graphrag with well-documented pipeline for local LLMs. Active community with responsive maintainers. Supports Hugging Face integration for fully local deployment.
Best for: Teams wanting graph RAG without cloud dependencies, local LLM deployments.

**nano-graphrag** is a lightweight reimplementation (~1,100 lines) that retains core GraphRAG functionality while being easy to read and modify. Unified storage interface (BaseGraphStorage) with NetworkX and Neo4j backends.
Best for: Learning GraphRAG internals, quick prototyping, customization.

**LlamaIndex PropertyGraphIndex** integrates graph RAG directly into the LlamaIndex ecosystem. Modular constructors and retrievers. Supports multiple query strategies simultaneously.
Best for: Teams already using LlamaIndex who want to add knowledge graph capabilities.

**Research frontier -- E2GraphRAG** (2025): A streamlined approach for high efficiency and effectiveness, representing the next evolution in graph-based RAG.

**What is new since mid-2025:**
- Microsoft GraphRAG added DRIFT Search mode.
- LightRAG gained traction as the practical alternative with local LLM support.
- LlamaIndex PropertyGraphIndex matured with modular architecture.
- E2GraphRAG emerged as a research direction for efficiency.

**PRD relevance:** Graph RAG is directly relevant for the music attribution knowledge graph. The ISRC/ISWC/ISNI relationships form a natural knowledge graph. Microsoft GraphRAG for comprehensive deployment; nano-graphrag for prototyping the concept. The hierarchical community structure maps well to the attribution confidence hierarchy (A0-A3 assurance levels).

Sources:
- [Microsoft GraphRAG GitHub](https://github.com/microsoft/graphrag)
- [GraphRAG Documentation](https://microsoft.github.io/graphrag/)
- [nano-graphrag GitHub](https://github.com/gusye1234/nano-graphrag)
- [LightRAG Explained](https://learnopencv.com/lightrag/)
- [E2GraphRAG Paper](https://arxiv.org/html/2505.24226v3)
- [Microsoft GraphRAG vs nano-graphrag Comparison](https://aiexpjourney.substack.com/p/microsoft-graphrag-vs-nano-graphrag)

---

## Cross-Cutting Observations

### Price Compression (mid-2025 to Feb 2026)

The LLM API pricing landscape has compressed dramatically:
- GPT-5 at $1.25/M input is half the price of GPT-4o at release.
- Gemini embeddings are free.
- Google and OpenAI are in a race to the bottom on inference costs.
- Open-source models (Qwen 3, Llama 4, DeepSeek) provide free alternatives for self-hosted deployments.

### Convergence Trends

1. **Protocol consolidation**: MCP for tool access, A2A for agent communication. The "protocol soup" is simplifying.
2. **Agent runtime convergence**: PydanticAI, OpenAI Agents SDK, and Google ADK are converging on similar patterns (typed tools, structured I/O, observability hooks).
3. **Evaluation as infrastructure**: LLM evaluation is moving from ad-hoc to CI/CD-integrated (DeepEval as pytest plugin, Langfuse as open-source standard).
4. **Graph RAG maturation**: Moving from research to production with multiple viable implementations.
5. **Conformal prediction meets LLMs**: MAPIE targeting LLM-as-Judge, TorchCP covering LLM uncertainty -- the field is catching up to the need.

### Volatility Assessment

| Category | Stability | Change Velocity | Risk of Choosing Now |
|----------|-----------|----------------|---------------------|
| LLM providers | Medium | Quarterly model releases | Low (APIs are backward-compatible) |
| Agent frameworks | Low | Monthly breaking changes | Medium (abstractions still shifting) |
| MCP ecosystem | Medium-High | Spec updates ~6 months | Low (industry standard) |
| Structured output | High | Stable | Very Low (Pydantic is foundational) |
| RAG frameworks | Medium | Feature releases monthly | Low-Medium |
| Embedding models | High | Annual improvements | Low (easy to re-embed) |
| Evaluation tools | Medium | Rapidly evolving | Medium |
| Conformal prediction | High | Annual releases | Very Low (math doesn't change) |
| Graph RAG | Low-Medium | Active research area | Medium (approaches still competing) |

### Mapping to Probabilistic PRD Archetypes

| Tool Category | Engineer-Heavy | Musician-First | Solo Hacker | Well-Funded |
|--------------|---------------|----------------|-------------|-------------|
| LLM | Claude Opus 4.6 / self-hosted Qwen 3 | GPT-5 / Claude Sonnet 4.5 | GPT-5 Nano / Gemini Flash | Claude Opus 4.6 + GPT-5 |
| Agent Framework | LangGraph / DSPy | CrewAI / Agno | smolagents / Instructor | LangGraph + custom |
| RAG | LlamaIndex + PropertyGraphIndex | RAGFlow / txtai | LlamaIndex basic | LlamaIndex + GraphRAG |
| Embeddings | Self-hosted BGE-M3 / Nomic | OpenAI text-embedding-3-small | Gemini (free) | Cohere embed-v4 + Rerank |
| Evaluation | Langfuse (self-hosted) + DeepEval | Braintrust (managed) | DeepEval only | Langfuse + Patronus |
| Conformal Pred | TorchCP + MAPIE | MAPIE only | crepes | TorchCP + MAPIE + custom |
| Graph RAG | Microsoft GraphRAG | LlamaIndex PropertyGraph | nano-graphrag | Microsoft GraphRAG + Neo4j |

---

*Last updated: 2026-02-10*
