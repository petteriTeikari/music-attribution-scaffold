# Agentic Systems Technical Research Synthesis

**Date**: 2026-02-03
**Version**: 1.0
**Status**: Complete
**Scope**: Technical architecture patterns for AI agents, MCP security, agentic commerce protocols, and compliance frameworks relevant to the system sprint implementation.

---

## Executive Summary

This synthesis consolidates technical research from the dpp-agents knowledge base and recent publications (August 2025 - February 2026) to inform the system' architectural decisions. Key findings impact MCP server design, multi-agent orchestration, memory systems, and regulatory compliance.

### Key Findings for the system

| Finding | Source | The System Implication |
|---------|--------|---------------------|
| MCP security: 40.71% average attack success rate | MCPSecBench 2025 | Three-tier trust model essential |
| Multi-agent adds 17.2x error amplification on sequential tasks | Google Research 2025 | Single-agent preferred for attribution pipeline |
| EU AI Act penalties: up to 7% global turnover | DLA Piper 2025 | Audit logging mandatory |
| RAG → Contextual Memory shift in 2026 | VentureBeat 2026 | Chat interface memory architecture |
| Agentic commerce protocols fragmenting (ACP, AP2, TAP) | Multiple 2025-2026 | MCP as unifying foundation layer |

---

## 1. MCP Security Architecture (2025-2026)

### 1.1 Threat Landscape

The Model Context Protocol faces four primary attack surfaces [[1]](#ref-mcpsecbench):

| Attack Surface | Threat Examples | The System Mitigation |
|----------------|-----------------|---------------------|
| **Tool Manifest Injection** | Malicious descriptions, prompt injection via metadata | Three-stage detection (static → neural → LLM arbiter) |
| **Server Communication** | MITM attacks, unauthorized registration | Server whitelist with SHA-256 verification |
| **Resource Access** | File system traversal, credential theft | Capability-based sandbox (READ, WRITE, EXECUTE, NETWORK) |
| **Execution Environment** | Code injection, privilege escalation | Secure subprocess executor with arg validation |

**Critical Statistic**: 85%+ of attacks successfully compromise at least one major MCP host (Claude, OpenAI, Cursor) [[2]](#ref-mcp-security-redhat).

### 1.2 November 2025 Specification Updates

The November 2025 MCP specification introduced enterprise-critical security features [[3]](#ref-mcp-spec-nov):

1. **OAuth Resource Server Classification**: MCP servers now officially classified as OAuth Resource Servers
2. **Resource Indicators (RFC 8707)**: Mandatory for clients to prevent token mis-redemption
3. **SEP-1024**: Client security requirements for local server installation
4. **SEP-835**: Default scopes definition in authorization specification

**System Implementation**: The three-tier trust model (Internal → Verified → Public) aligns with these specifications.

### 1.3 Real-World Incidents (2025)

| Incident | Date | Impact | Lesson |
|----------|------|--------|--------|
| Supabase Cursor Agent | Mid-2025 | SQL injection via support tickets exfiltrated tokens | Input sanitization mandatory |
| GitHub MCP Server | May 2025 | Prompt injection allowed repo manipulation | Tool descriptions must be sanitized |

### 1.4 MCP Governance: Agentic AI Foundation

In December 2025, Anthropic donated MCP to the Agentic AI Foundation (AAIF) under the Linux Foundation, co-founded with Block and OpenAI [[4]](#ref-mcp-aaif). The September 2025 MCP Registry preview serves as the single source of truth for available MCP servers.

**System Decision**: Register attribution tools in MCP Registry for discoverability by verified partners.

---

## 2. Multi-Agent vs Single-Agent Architecture

### 2.1 Quantitative Scaling Principles

Google Research (2025) established the first empirical scaling principles through 180 agent configurations [[5]](#ref-google-scaling):

| Condition | Recommendation | Rationale |
|-----------|----------------|-----------|
| Single-agent accuracy > 45% | Don't add more agents | Diminishing returns beyond threshold |
| Independent parallel tasks | Multi-agent beneficial | 17.2x error amplification avoided |
| Sequential dependencies | Single-agent preferred | Step B errors cascade from Step A |
| >3 major functions | Multi-agent with hierarchy | Keep teams to 3-7 agents |

### 2.2 Industry Adoption (2026)

- AI agent adoption: 11% → 42% in two quarters [[6]](#ref-analytics-vidhya)
- 40% of enterprise applications will feature task-specific agents by 2026 (up from <5% in 2025)
- 86% of copilot spending ($7.2B) directed to agent-based systems

### 2.3 Attribution Pipeline Decision

The attribution engine processes sequential tasks:
1. Fetch from Discogs → 2. Fetch from MusicBrainz → 3. Entity resolution → 4. Confidence scoring

**Recommendation**: Single-agent architecture with tool orchestration, not multi-agent. Error amplification risk too high for sequential attribution chain.

### 2.4 Key Infrastructure (January 2026)

| Framework | Release | Significance |
|-----------|---------|--------------|
| LangGraph 1.0 | January 2026 | First stable durable agent framework [[7]](#ref-langgraph) |
| A2A (Google) | 2025 | Peer-to-peer agent collaboration without central oversight |
| MCP (Anthropic) | November 2025 | Standardized tool access |

---

## 3. Agentic Commerce Protocols

### 3.1 Protocol Landscape (2025-2026)

| Protocol | Provider | Focus | Status |
|----------|----------|-------|--------|
| **ACP** (Agentic Commerce Protocol) | OpenAI + Stripe | Payment flows, instant checkout | Production (Sep 2025) [[8]](#ref-openai-acp) |
| **AP2** (Agent Payment Protocol) | Google | Payment mandates, delegated consent | Production (Jan 2026) |
| **TAP** (Trusted Agent Protocol) | Visa | Agent verification, bot authentication | Production (Oct 2025) [[9]](#ref-visa-tap) |
| **UCP** (Universal Commerce Protocol) | Google + Shopify + Walmart | Full commerce lifecycle | Announced (Jan 2026) [[10]](#ref-google-ucp) |
| **A2A** (Agent-to-Agent) | Linux Foundation | Multi-agent coordination | Production |
| **MCP** | Anthropic/AAIF | Tool access, context management | Production |

### 3.2 AI Hallucination in Commerce

The ACE Benchmark reveals critical limitations [[11]](#ref-ace-benchmark):

| Model | Shopping Score | Key Failure Mode |
|-------|----------------|------------------|
| GPT-5 | <50% | Price hallucination |
| o3 Pro | <50% | Broken links |
| Gemini 3 Pro | -54% on links | Fabricated URLs |
| Claude Opus 4.5 | Negative | Link hallucination |

**Implication for the system**: Structured, verifiable attribution data prevents hallucination. MCP tools return canonical data, not LLM-generated guesses.

### 3.3 MCP Payment Server Releases

| Provider | Release | Capabilities |
|----------|---------|--------------|
| Worldpay | Nov 2025 | 52B+ annual transactions, 135+ currencies |
| Adyen | Nov 2025 | Direct LLM integration |
| Visa | Coming 2026 | Native Visa API access |

**System Opportunity**: Position as verified attribution data source for agentic commerce—AI agents querying artist permissions before training/generation.

---

## 4. EU AI Act Compliance (August 2025+)

### 4.1 Enforcement Timeline

| Date | Milestone | The System Impact |
|------|-----------|-----------------|
| **Aug 2, 2025** | Penalty regime active, GPAI obligations enforceable | Audit logging mandatory |
| **Aug 2, 2026** | High-risk AI system rules apply | If AI-assisted attribution = high-risk |
| **Aug 2, 2027** | Regulated product AI rules | Extended transition |

### 4.2 GPAI Provider Requirements (Active)

Providers of General-Purpose AI models must [[12]](#ref-eu-ai-act-dlapiper):

1. **Technical Documentation**: Model development, training, evaluation traceable
2. **Transparency Reports**: Capabilities, limitations, potential risks
3. **Training Data Summary**: Must be published

### 4.3 Penalty Regime

| Infringement Type | Maximum Penalty |
|-------------------|-----------------|
| Prohibited AI practices | €35M or 7% global turnover |
| Other obligations | €15M or 3% global turnover |
| Misleading information | €7.5M or 1% global turnover |

### 4.4 System Compliance Strategy

| EU AI Act Requirement | System Implementation |
|----------------------|------------------------|
| Record-keeping (Art. 12) | Telemetry Pipeline with immutable audit events |
| Human oversight (Art. 14) | Chat interface for artist verification |
| Transparency (Art. 13) | Confidence scores with source provenance |
| Data governance (Art. 10) | Multi-source aggregation with authority weights |

---

## 5. MLSecOps Framework (2025-2026)

### 5.1 Five Core Pillars (OpenSSF)

Per the OpenSSF MLSecOps whitepaper (August 2025) [[13]](#ref-openssf):

| Pillar | Description | System Status |
|--------|-------------|-----------------|
| Supply Chain Vulnerability | Model/data provenance tracking | Partial (attribution, not model) |
| Model Provenance | Training lineage, signed artifacts | N/A (API-only, no model training) |
| GRC | Policies as code, compliance validation | Via Policy Engine |
| Trusted AI | Bias detection, explainability | Via confidence disclaimers |
| Adversarial ML | Evasion, poisoning, extraction defenses | Input sanitization |

### 5.2 MITRE ATLAS Attack Types

| Attack Type | Description | The System Relevance |
|-------------|-------------|-------------------|
| Evasion | Adversarial examples fool model | Low (retrieval, not classification) |
| Poisoning | Malicious training data | Medium (source data quality) |
| Extraction | Stealing model weights | Low (API-only) |
| Inference | Extracting sensitive info from outputs | Medium (artist data privacy) |

### 5.3 SOC2 AI-Specific Controls (2025)

| Control | Requirement | Implementation |
|---------|-------------|----------------|
| MS-1 | Model weight protection | N/A (API-only) |
| MS-2 | Model versioning | Via Tool Registry |
| MS-3 | Model signing | N/A |
| TD-1 | Training data encryption | Source data at rest encryption |
| CC6.6 | Encryption at rest/transit | PostgreSQL + TLS |
| CC7.2 | Threat monitoring | Security Dashboard |

---

## 6. Chatbot Memory Architecture

### 6.1 The Conversational Amnesia Problem

LLMs are fundamentally stateless—a drawback called "conversational amnesia" [[14]](#ref-datacamp-memory). Context window growth paradoxically loses signal, making reliable multi-turn conversation challenging beyond 10-15 turns.

### 6.2 Memory Architecture Patterns (2026)

| Pattern | Description | Use Case |
|---------|-------------|----------|
| **Conversation Buffer** | Store entire history | Simple, token-expensive |
| **Summary Buffer** | Recent raw + old summaries | Long conversations (recommended) |
| **Knowledge Graph** | Entity/relationship extraction | Complex domain knowledge |
| **Vector DB + RAG** | Semantic retrieval | Cross-session persistence |
| **Agentic Memory** | Self-organizing, adaptive | Stateful assistants |

### 6.3 Industry Shift: RAG → Contextual Memory

RAG remains useful for static data, but agentic memory becomes critical for adaptive assistants [[15]](#ref-venturebeat-rag):

> "In 2026, contextual memory will no longer be a novel technique; it will become table stakes for many operational agentic AI deployments."

### 6.4 System Chat Interface Memory Design

| Memory Type | Implementation | Purpose |
|-------------|----------------|---------|
| **Short-term** | Session state (Redis) | Current album/track context |
| **Long-term** | Vector DB (pgvector) | Previous artist conversations |
| **Semantic** | Entity extraction | Collaborator relationships |
| **Procedural** | Prompt templates | Gap-filling patterns |

### 6.5 Key Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Response latency (text) | <800ms | APM |
| Engagement rate | >35% | Analytics |
| Mean conversation length | >10 turns | Session tracking |
| Context retention accuracy | >90% | Validation set |

---

## 7. Cross-Topic Synthesis for the system

### 7.1 Architecture Decision Matrix

| Decision Point | Options | Chosen | Rationale (Research-Backed) |
|----------------|---------|--------|----------------------------|
| Agent architecture | Multi-agent / Single-agent | Single-agent | Sequential tasks + 17.2x error amplification |
| MCP trust model | Open / Tiered | Three-tier | 40.71% attack success rate |
| Memory pattern | RAG / Agentic Memory | Hybrid | Static attribution + adaptive conversation |
| Compliance approach | Reactive / Proactive | Proactive | €35M penalty exposure |
| Commerce integration | Direct / MCP gateway | MCP gateway | Protocol fragmentation (ACP/AP2/TAP) |

### 7.2 Security Architecture Summary

```
┌─────────────────────────────────────────────────────────────────┐
│                    the attribution MCP Security Layers                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Layer 1: Authentication (OAuth 2.0 + Resource Indicators)      │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │  • Tier 1 (Internal): Full R/W, unlimited                 │  │
│  │  • Tier 2 (Verified): R + scoped W, 1000/hr              │  │
│  │  • Tier 3 (Public): Read-only, 100/hr                    │  │
│  └───────────────────────────────────────────────────────────┘  │
│                                                                 │
│  Layer 2: Input Validation                                      │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │  • Static scanner (SQL/command injection)                 │  │
│  │  • Neural detector (adversarial patterns)                 │  │
│  │  • LLM arbiter (semantic analysis)                       │  │
│  └───────────────────────────────────────────────────────────┘  │
│                                                                 │
│  Layer 3: Capability Sandbox                                    │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │  • READ, WRITE, EXECUTE, NETWORK permissions             │  │
│  │  • Time-limited grants                                    │  │
│  │  • Path normalization (traversal prevention)              │  │
│  └───────────────────────────────────────────────────────────┘  │
│                                                                 │
│  Layer 4: Audit & Compliance                                    │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │  • Immutable audit trail (EU AI Act Art. 12)             │  │
│  │  • Artist-accessible usage logs                           │  │
│  │  • Telemetry export (Prometheus)                         │  │
│  └───────────────────────────────────────────────────────────┘  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 7.3 PRD Update Recommendations

Based on this research, the following PRD updates are recommended:

| PRD | Section | Update |
|-----|---------|--------|
| `mcp-server-prd.md` | Security | Add November 2025 spec compliance notes |
| `chat-interface-prd.md` | Memory | Add agentic memory architecture patterns |
| `attribution-engine-prd.md` | Architecture | Confirm single-agent decision |
| `vision-v1.md` | Compliance | Add EU AI Act penalty exposure |

---

## References

<a name="ref-mcpsecbench"></a>
[1] AIS2Lab. "MCPSecBench: A Benchmark for MCP Security." arXiv:2508.13220, 2025. GitHub: https://github.com/AIS2Lab/MCPSecBench

<a name="ref-mcp-security-redhat"></a>
[2] Red Hat. "Model Context Protocol (MCP): Understanding security risks and controls." Red Hat Blog, 2025. https://www.redhat.com/en/blog/model-context-protocol-mcp-understanding-security-risks-and-controls

<a name="ref-mcp-spec-nov"></a>
[3] Model Context Protocol. "One Year of MCP: November 2025 Spec Release." MCP Blog, November 2025. http://blog.modelcontextprotocol.io/posts/2025-11-25-first-mcp-anniversary/

<a name="ref-mcp-aaif"></a>
[4] Linux Foundation. "Agentic AI Foundation (AAIF) Launch." December 2025. See: https://modelcontextprotocol.io/specification/2025-11-25

<a name="ref-google-scaling"></a>
[5] Google Research. "Towards a science of scaling agent systems: When and why agent systems work." Google Research Blog, 2025. https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work/

<a name="ref-analytics-vidhya"></a>
[6] Analytics Vidhya. "Single-Agent vs Multi-Agent Systems." January 2026. https://www.analyticsvidhya.com/blog/2026/01/single-agent-vs-multi-agent-systems/

<a name="ref-langgraph"></a>
[7] LangChain. "LangGraph 1.0 Release." January 2026. See: Medium article by Ida Silfverskiöld.

<a name="ref-openai-acp"></a>
[8] OpenAI. "Agentic Commerce Protocol (ACP)." OpenAI Developers, 2025. https://developers.openai.com/commerce/

<a name="ref-visa-tap"></a>
[9] Oscilar. "Visa's Trusted Agent Protocol (TAP) and the Future of Agentic Commerce." 2025. https://oscilar.com/blog/visatap

<a name="ref-google-ucp"></a>
[10] TechCrunch. "Google announces a new protocol to facilitate commerce using AI agents." January 2026. https://techcrunch.com/2026/01/11/google-announces-a-new-protocol-to-facilitate-commerce-using-ai-agents/

<a name="ref-ace-benchmark"></a>
[11] AI Consumer Index (ACE) Benchmark. arXiv:2512.04921, 2025.

<a name="ref-eu-ai-act-dlapiper"></a>
[12] DLA Piper. "Latest wave of obligations under the EU AI Act take effect." August 2025. https://www.dlapiper.com/en-us/insights/publications/2025/08/latest-wave-of-obligations-under-the-eu-ai-act-take-effect

<a name="ref-openssf"></a>
[13] OpenSSF. "MLSecOps Whitepaper." August 2025. See: dpp-agents/knowledge-base/documentation/infrastructure/security/mlsecops-comprehensive-roadmap.md

<a name="ref-datacamp-memory"></a>
[14] DataCamp. "How Does LLM Memory Work? Building Context-Aware AI Applications." 2025. https://www.datacamp.com/blog/how-does-llm-memory-work

<a name="ref-venturebeat-rag"></a>
[15] VentureBeat. "6 data predictions for 2026: RAG is dead, what's old is new again." January 2026. https://venturebeat.com/data/six-data-shifts-that-will-shape-enterprise-ai-in-2026

---

## Cross-References

### Internal Knowledge Base
- [music-attribution-research-2026-02-03.md](../music/music-attribution-research-2026-02-03.md) - Music domain research
- [mcp/SYNTHESIS.md](mcp/SYNTHESIS.md) - MCP protocol patterns
- [uncertainty/SYNTHESIS.md](uncertainty/SYNTHESIS.md) - Confidence scoring approaches

### PRDs
- [vision-v1.md](../../prd/vision-v1.md) - Product vision
- [attribution-engine-prd.md](../../prd/attribution-engine-prd.md) - Core engine
- [mcp-server-prd.md](../../prd/mcp-server-prd.md) - API specification
- [chat-interface-prd.md](../../prd/chat-interface-prd.md) - Conversational UX

### External dpp-agents Sources
- `agentic-commerce/agentic-commerce-revolution-research.md` - Protocol landscape
- `ai-agents/multi-agent-vs-single-agent-research.md` - Architecture patterns
- `backend/mcp/architecture/ecosystem-architecture.md` - MCP patterns
- `infrastructure/security/mlsecops-comprehensive-roadmap.md` - Security framework

---

## Changelog

| Date | Change | Author |
|------|--------|--------|
| 2026-02-03 | Initial creation with dpp-agents + web search synthesis | Claude |
