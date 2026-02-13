# MCP Tool Roadmap

> **Protocol**: Model Context Protocol (MCP) — machine-readable permission queries for AI training rights.
> **Server**: `src/music_attribution/mcp/server.py`

## Implemented Tools (v0.5)

| Tool | Description | Status |
|------|-------------|--------|
| `query_attribution` | Query attribution record by work entity ID | Implemented |
| `check_permission` | Check a specific permission for an entity (AI training, sync, etc.) | Implemented |
| `list_permissions` | List all permissions for an entity | Implemented |

## Future Tools (Roadmap)

### Phase 1: Training Data Attribution

| Tool | Description | Dependencies |
|------|-------------|-------------|
| `query_training_influence` | Query how much a source work influenced a specific model's output. Returns influence percentage, method used (TRAK, DataInf, embedding similarity), and confidence score. | `TrainingInfluence` schema (B3), TDA integration decision (B4) |
| `register_training_consent` | Register or update consent for AI training usage. Supports fine-grained permissions: composition-only, recording-only, style learning, dataset inclusion. | `PermissionTypeEnum` extensions (B2) |

### Phase 2: Registry & Compliance

| Tool | Description | Dependencies |
|------|-------------|-------------|
| `check_registry_status` | Check registration status across external registries (SoundExchange AI Registry, ISRC agencies). Returns registration status, timestamps, and any conflicts. | External registry integration decision (B4) |
| `verify_compliance` | Verify compliance attestations (Fairly Trained certification, C2PA provenance, EU AI Act). Returns attestation validity, issuer, and expiration. | `ComplianceAttestation` schema (B3) |

### Phase 3: Multi-Modal Attribution

| Tool | Description | Dependencies |
|------|-------------|-------------|
| `query_multimodal_influence` | Cross-media influence query for audio, image, text, and video. Extends `query_training_influence` to non-audio modalities. | Multi-modal domain overlay (B5) |
| `detect_watermark` | Detect embedded watermarks (SynthID, AudioSeal, WavMark, Digimarc) in audio content. Returns watermark type, model origin, and confidence. | `WatermarkTypeEnum` (B1), provenance verification decision (B4) |

## Design Principles

1. **Consent-first**: Every tool respects the Permission Patchbay. No attribution data is returned without checking consent.
2. **Confidence-scored**: All responses include calibrated confidence scores with uncertainty quantification.
3. **Assurance-leveled**: Results indicate A0-A3 assurance level reflecting verification depth.
4. **Batch-capable**: Future tools will support batch queries for catalog-scale operations.

## Integration Pattern

```
AI Platform → MCP Client → Permission Patchbay → Attribution Engine
                                    ↓
                            Consent Check (ALLOW/DENY/ASK)
                                    ↓
                            Attribution Response (with confidence)
```

## References

- [MCP Specification](https://modelcontextprotocol.io/)
- Manuscript Section 5: "MCP as Consent Infrastructure"
- PRD Decision: `api_protocol` → MCP-primary selected
