# fig-howto-03: How to Query the API

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-howto-03 |
| **Title** | How to Query the API |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 (implementation detail) |
| **Location** | docs/guides/api-quickstart.md, docs/api/ |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure walks an engineer through making their first API request to the attribution service. It shows the full request-response cycle from a curl command through FastAPI routing to the attribution engine and back. It answers: "How do I get attribution data out of this system?"

The key message is: "A single curl command to `/api/v1/attribution/{isrc}` returns a JSON response with per-field confidence scores, source provenance, and assurance level -- everything needed to assess attribution quality."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  HOW TO QUERY THE API                                          |
|  ■ From curl to Confidence-Scored Response                     |
+---------------------------------------------------------------+
|                                                                |
|  I. REQUEST                                                    |
|  ─────────                                                     |
|  ┌─────────────────────────────────────────────┐              |
|  │ $ curl http://localhost:8000/api/v1/         │              |
|  │   attribution/USRC17607839                   │              |
|  └──────────────────────┬──────────────────────┘              |
|                          │                                      |
|                          v                                      |
|  II. FASTAPI ROUTING                                           |
|  ───────────────────                                           |
|  ┌─────────────────────────────────────────────┐              |
|  │ api/routes/attribution.py                    │              |
|  │ @router.get("/attribution/{isrc}")           │              |
|  └──────────────────────┬──────────────────────┘              |
|                          │                                      |
|                          v                                      |
|  III. ATTRIBUTION SERVICE                                      |
|  ────────────────────────                                      |
|  ┌─────────────────────────────────────────────┐              |
|  │ attribution/engine.py                        │              |
|  │ Multi-source lookup → Confidence scoring     │              |
|  │ → Assurance level assignment                 │              |
|  └──────────────────────┬──────────────────────┘              |
|                          │                                      |
|                          v                                      |
|  IV. JSON RESPONSE                                             |
|  ─────────────────                                             |
|  ┌─────────────────────────────────────────────┐              |
|  │ {                                            │              |
|  │   "isrc": "USRC17607839",                   │              |
|  │   "title": "Hide and Seek",                 │              |
|  │   "artist": "Imogen Heap",                  │              |
|  │   "confidence": 0.87,                       │              |
|  │   "assurance_level": "A2",                  │              |
|  │   "sources": ["musicbrainz", "discogs"]     │              |
|  │ }                                            │              |
|  └─────────────────────────────────────────────┘              |
|                                                                |
|  V. OTHER ENDPOINTS                                            |
|  ──────────────────                                            |
|  ■ GET /api/v1/health          ■ POST /api/v1/permissions     |
|  ■ GET /api/v1/attribution/    ■ GET  /api/v1/works           |
|     batch                                                      |
+---------------------------------------------------------------+
|  ■ All responses include per-field confidence + provenance     |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "HOW TO QUERY THE API" in Instrument Serif ALL-CAPS with coral accent square |
| Subtitle | `label_editorial` | "From curl to Confidence-Scored Response" in Plus Jakarta Sans caps |
| Step I: curl command | `data_mono` | Actual curl command with ISRC example in monospace |
| Step II: FastAPI routing | `api_endpoint` | Route definition showing path parameter pattern |
| Step III: Attribution service | `source_corroborate` | Engine processing: multi-source lookup, confidence scoring, assurance assignment |
| Step IV: JSON response | `data_mono` | Example JSON response with confidence 0.87 and A2 assurance |
| Step V: Other endpoints | `api_endpoint` | List of additional available endpoints |
| Flow arrows (I to IV) | `data_flow` | Vertical downward arrows showing request-response flow |
| Roman numerals I-V | `section_numeral` | Step headers in editorial style |
| Confidence value "0.87" | `confidence_high` | Green tier confidence score in response |
| Assurance level "A2" | `assurance_a2` | Blue corroborated level tag |
| Footer callout | `callout_box` | "All responses include per-field confidence + provenance" |

## Anti-Hallucination Rules

1. The API base path is `/api/v1/` -- not `/api/` or `/v1/` alone.
2. The ISRC "USRC17607839" is a plausible example -- do not use a real ISRC that might map to an incorrect attribution.
3. Confidence score 0.87 is in the high tier (>= 0.85) -- color it accordingly.
4. Assurance level A2 means "Corroborated" (multiple sources agree) -- not "Verified" (that is A3).
5. The response JSON is illustrative -- the actual Pydantic response model has more fields. Do not claim this is the exact schema.
6. FastAPI routes live in `api/routes/` -- not `api/endpoints/` or `api/views/`.
7. The example uses "Hide and Seek" by Imogen Heap (the project persona) -- not a random song.
8. Background must be warm cream (#f6f3e6), not white or gray.

## Alt Text

Vertical flow diagram showing API request lifecycle: curl command at top flows through FastAPI routing and attribution engine to JSON response with confidence score.
