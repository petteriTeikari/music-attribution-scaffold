# ADR-0003: Pure Python + Pydantic

## Status

Accepted

## Context

AI/LLM application frameworks offer varying levels of abstraction:
1. **LangChain**: High-level abstractions, large ecosystem
2. **LlamaIndex**: RAG-focused framework
3. **Pure Python + Pydantic**: Direct API calls, explicit control

## Decision

Avoid LangChain and similar frameworks. Use pure Python with Pydantic for:
- API client wrappers
- Data validation and serialization
- Type safety

## Consequences

### Positive

- **Debuggability**: No framework magic, clear stack traces
- **Flexibility**: Direct control over prompts and API calls
- **No lock-in**: Can switch LLM providers easily
- **Smaller dependencies**: Fewer transitive dependencies
- **Better understanding**: Team learns LLM APIs directly

### Negative

- **More boilerplate**: Must implement patterns that frameworks provide
- **No pre-built chains**: Must compose workflows manually

### Implementation Notes

- Use `httpx` for async HTTP clients
- Use `pydantic` for all data models
- Implement retry logic with `tenacity`
- Use Anthropic SDK directly for Claude API
