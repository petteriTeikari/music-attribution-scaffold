# Technical Knowledge Synthesis

Cross-cutting insights from technical knowledge areas relevant to the system.

## Key Research (2026-02-03)

See [agentic-systems-research-2026-02-03.md](agentic-systems-research-2026-02-03.md) for comprehensive synthesis of 15+ sources.

## MCP

### Security Posture
- **40.71%** average attack success rate across MCP implementations
- **85%+** of attacks compromise at least one major platform
- November 2025 spec adds OAuth Resource Server classification + RFC 8707 Resource Indicators

### System Three-Tier Trust Model
| Tier | Access | Rate Limit |
|------|--------|------------|
| Internal | Full R/W | Unlimited |
| Verified | R + scoped W | 1000/hr |
| Public | Read-only | 100/hr |

See [mcp/SYNTHESIS.md](mcp/SYNTHESIS.md) for protocol patterns.

## Agentic Systems

### Multi-Agent vs Single-Agent Decision
- **45% accuracy threshold**: Beyond this, adding agents yields diminishing returns
- **17.2x error amplification** in independent parallel systems
- **Sequential tasks** strongly favor single-agent architecture

**System Decision**: Single-agent for attribution pipeline (sequential: fetch → resolve → score).

See [agentic-systems/SYNTHESIS.md](agentic-systems/SYNTHESIS.md) for patterns.

## Uncertainty Quantification

### Confidence Scoring Approach
- Calibration requires 100+ validation examples
- ECE (Expected Calibration Error) target: <0.15
- Attribution types: corroborative (similarity-based) vs verified (artist-confirmed)

See [uncertainty/SYNTHESIS.md](uncertainty/SYNTHESIS.md) for methods.

## RAG

### 2026 Trend: RAG → Contextual Memory
- RAG remains for static knowledge retrieval
- Agentic memory required for adaptive multi-turn conversation
- Hybrid approach: static attribution + adaptive chat memory

See [rag/SYNTHESIS.md](rag/SYNTHESIS.md) for implementation patterns.

## Semantic Search

### Vector Search for Attribution
- pgvector for PostgreSQL integration
- Embedding similarity for entity resolution
- Cross-session conversation retrieval

See [semantic-search/SYNTHESIS.md](semantic-search/SYNTHESIS.md) for techniques.

## Context Engineering

### Conversation Memory Design
| Memory Type | Purpose | Implementation |
|-------------|---------|----------------|
| Short-term | Current session | Redis |
| Long-term | Cross-session | pgvector |
| Semantic | Entity relationships | Knowledge graph |
| Procedural | Interaction patterns | Prompt templates |

See [context-engineering/SYNTHESIS.md](context-engineering/SYNTHESIS.md) for patterns.

## Cross-Topic Connections

### Security ↔ Compliance
- MCP audit logging satisfies EU AI Act Art. 12 (record-keeping)
- Three-tier trust enables Art. 14 (human oversight) implementation
- €35M penalty exposure requires proactive compliance

### Memory ↔ Chat Interface
- Summary Buffer Memory pattern for long conversations
- Vector retrieval for artist's previous sessions
- 10+ turn target requires explicit context management

### Attribution ↔ Commerce
- Agentic commerce protocols (ACP/AP2/TAP) need verified data
- MCP as unifying foundation layer across protocol fragmentation
- Structured attribution prevents AI hallucination in queries
