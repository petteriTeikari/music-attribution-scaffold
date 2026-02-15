# API Examples

Practical examples for querying the Music Attribution REST API and interacting with the agent SSE endpoint.

All examples use `http://localhost:8000` as the base URL. Start the backend with `make agent` before running any of these.

---

## Health Check

Verify the server is running:

=== "curl"

    ```bash
    curl http://localhost:8000/health
    ```

=== "Python"

    ```python
    import httpx

    response = httpx.get("http://localhost:8000/health")
    print(response.json())
    ```

Expected response:

```json
{"status": "healthy", "service": "music-attribution-api"}
```

---

## List Attribution Records

Retrieve all attribution records with pagination.

=== "curl"

    ```bash
    # List first 10 records
    curl "http://localhost:8000/api/v1/attributions/?limit=10&offset=0" | python -m json.tool

    # List records needing review
    curl "http://localhost:8000/api/v1/attributions/?needs_review=true" | python -m json.tool

    # Filter by assurance level
    curl "http://localhost:8000/api/v1/attributions/?assurance_level=LEVEL_3" | python -m json.tool
    ```

=== "Python"

    ```python
    import httpx

    BASE_URL = "http://localhost:8000/api/v1"

    # List first 10 records
    response = httpx.get(f"{BASE_URL}/attributions/", params={"limit": 10, "offset": 0})
    records = response.json()
    for record in records:
        print(f"{record['confidence_score']:.0%} - {record['assurance_level']}")

    # List records needing review
    response = httpx.get(f"{BASE_URL}/attributions/", params={"needs_review": True})
    review_queue = response.json()
    print(f"{len(review_queue)} records need review")

    # Filter by assurance level
    response = httpx.get(f"{BASE_URL}/attributions/", params={"assurance_level": "LEVEL_3"})
    a3_records = response.json()
    print(f"{len(a3_records)} records at A3 assurance")
    ```

### Query Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `limit` | int | 50 | Maximum results (1-100) |
| `offset` | int | 0 | Records to skip |
| `needs_review` | bool | null | Filter by review flag |
| `assurance_level` | string | null | Filter by level (LEVEL_0 through LEVEL_3) |

---

## Get a Specific Work

Retrieve a single attribution record by work entity UUID.

=== "curl"

    ```bash
    WORK_ID="your-work-uuid-here"
    curl "http://localhost:8000/api/v1/attributions/work/${WORK_ID}" | python -m json.tool
    ```

=== "Python"

    ```python
    import httpx

    BASE_URL = "http://localhost:8000/api/v1"
    work_id = "your-work-uuid-here"

    response = httpx.get(f"{BASE_URL}/attributions/work/{work_id}")
    if response.status_code == 200:
        record = response.json()
        print(f"Confidence: {record['confidence_score']:.0%}")
        print(f"Assurance: {record['assurance_level']}")
        print(f"Credits: {len(record['credits'])}")
    elif response.status_code == 404:
        print("Attribution not found")
    ```

### Response Structure

The response includes the full `AttributionRecord`:

```json
{
    "attribution_id": "uuid",
    "work_entity_id": "uuid",
    "credits": [
        {
            "entity_id": "uuid",
            "role": "PERFORMER",
            "confidence": 0.92,
            "sources": ["MUSICBRAINZ", "DISCOGS"],
            "assurance_level": "LEVEL_3"
        }
    ],
    "assurance_level": "LEVEL_3",
    "confidence_score": 0.95,
    "conformal_set": {
        "coverage_level": 0.9,
        "marginal_coverage": 0.92,
        "calibration_error": 0.02,
        "calibration_method": "APS"
    },
    "source_agreement": 0.88,
    "needs_review": false,
    "provenance_chain": [...]
}
```

---

## Search Attributions

Search across works using hybrid search (full-text + vector + graph context).

=== "curl"

    ```bash
    # Search by artist name
    curl "http://localhost:8000/api/v1/attributions/search?q=imogen+heap&limit=5" | python -m json.tool

    # Search by track title
    curl "http://localhost:8000/api/v1/attributions/search?q=hide+and+seek" | python -m json.tool
    ```

=== "Python"

    ```python
    import httpx

    BASE_URL = "http://localhost:8000/api/v1"

    response = httpx.get(f"{BASE_URL}/attributions/search", params={"q": "imogen heap", "limit": 5})
    results = response.json()
    for result in results:
        attribution = result["attribution"]
        rrf_score = result["rrf_score"]
        print(f"[{rrf_score:.3f}] {attribution['confidence_score']:.0%} confidence")
    ```

### Query Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `q` | string | "" | Search query |
| `limit` | int | 20 | Maximum results (1-100) |

---

## Get Provenance Chain

Retrieve the full provenance chain and uncertainty metadata for an attribution record.

=== "curl"

    ```bash
    ATTRIBUTION_ID="your-attribution-uuid-here"
    curl "http://localhost:8000/api/v1/attributions/${ATTRIBUTION_ID}/provenance" | python -m json.tool
    ```

=== "Python"

    ```python
    import httpx

    BASE_URL = "http://localhost:8000/api/v1"
    attribution_id = "your-attribution-uuid-here"

    response = httpx.get(f"{BASE_URL}/attributions/{attribution_id}/provenance")
    if response.status_code == 200:
        data = response.json()
        for event in data["provenance_chain"]:
            print(f"[{event['event_type']}] {event['agent']} at {event['timestamp']}")
        if data["uncertainty_summary"]:
            print(f"Uncertainty: {data['uncertainty_summary']}")
    ```

---

## Check Permissions

Query the Permission Patchbay to check AI training rights and other permissions.

=== "curl"

    ```bash
    # Check AI training permission
    curl -X POST http://localhost:8000/api/v1/permissions/check \
      -H "Content-Type: application/json" \
      -d '{
        "entity_id": "your-entity-uuid-here",
        "permission_type": "AI_TRAINING",
        "requester_id": "my-app"
      }' | python -m json.tool

    # Check voice cloning permission
    curl -X POST http://localhost:8000/api/v1/permissions/check \
      -H "Content-Type: application/json" \
      -d '{
        "entity_id": "your-entity-uuid-here",
        "permission_type": "VOICE_CLONING",
        "requester_id": "my-app"
      }' | python -m json.tool
    ```

=== "Python"

    ```python
    import httpx

    BASE_URL = "http://localhost:8000/api/v1"

    # Check AI training permission
    response = httpx.post(
        f"{BASE_URL}/permissions/check",
        json={
            "entity_id": "your-entity-uuid-here",
            "permission_type": "AI_TRAINING",
            "requester_id": "my-app",
        },
    )
    result = response.json()
    print(f"Permission: {result['permission_type']} = {result['result']}")

    # List all permissions for an entity
    entity_id = "your-entity-uuid-here"
    response = httpx.get(f"{BASE_URL}/permissions/{entity_id}")
    if response.status_code == 200:
        bundles = response.json()
        for bundle in bundles:
            for perm in bundle.get("permissions", []):
                print(f"  {perm['permission_type']}: {perm['value']}")
    ```

### Available Permission Types

| Permission Type | Description |
|----------------|-------------|
| `STREAM` | Streaming rights |
| `DOWNLOAD` | Download rights |
| `SYNC_LICENSE` | Sync licensing (film, TV, ads) |
| `AI_TRAINING` | General AI training |
| `AI_TRAINING_COMPOSITION` | Training on composition |
| `AI_TRAINING_RECORDING` | Training on master recording |
| `AI_TRAINING_STYLE` | Style learning |
| `VOICE_CLONING` | Voice cloning |
| `LYRICS_IN_CHATBOTS` | Lyrics reproduction in chatbots |
| `COVER_VERSIONS` | Cover version rights |
| `REMIX` | Remix rights |
| `SAMPLE` | Sampling rights |
| `DERIVATIVE_WORK` | Derivative work rights |

### Permission Values

| Value | Meaning |
|-------|---------|
| `ALLOW` | Permission granted unconditionally |
| `DENY` | Permission denied |
| `ASK` | Must contact rights holder |
| `ALLOW_WITH_ATTRIBUTION` | Allowed if attribution is provided |
| `ALLOW_WITH_ROYALTY` | Allowed with royalty payment |

---

## Agent SSE Endpoint

The `/api/v1/copilotkit` endpoint provides Server-Sent Events (SSE) streaming for the attribution agent. This is used by the CopilotKit frontend, but you can interact with it directly.

=== "curl"

    ```bash
    # Send a message to the agent
    curl -X POST http://localhost:8000/api/v1/copilotkit \
      -H "Content-Type: application/json" \
      -d '{
        "messages": [
          {"role": "user", "content": "What is the confidence score for Hide and Seek?"}
        ]
      }' --no-buffer
    ```

=== "Python"

    ```python
    import httpx

    BASE_URL = "http://localhost:8000/api/v1"

    # Stream SSE events from the agent
    with httpx.stream(
        "POST",
        f"{BASE_URL}/copilotkit",
        json={
            "messages": [
                {"role": "user", "content": "Which works need review?"},
            ],
        },
    ) as response:
        for line in response.iter_lines():
            if line.startswith("data: "):
                import json
                event = json.loads(line[6:])
                event_type = event.get("type")

                if event_type == "TextMessageContent":
                    print(event["content"], end="", flush=True)
                elif event_type == "RunFinished":
                    print("\n--- Done ---")
    ```

### SSE Event Types

The endpoint emits AG-UI protocol events:

| Event Type | Description |
|-----------|-------------|
| `RunStarted` | Agent run has begun |
| `TextMessageStart` | New assistant message starting |
| `TextMessageContent` | Chunk of response text |
| `TextMessageEnd` | Message complete |
| `StateSnapshot` | Agent state after processing |
| `RunFinished` | Agent run complete |

!!! note "ANTHROPIC_API_KEY Required"
    The agent endpoint requires `ANTHROPIC_API_KEY` to be set in the environment. Without it, the agent will return an error message.

---

## Error Handling Patterns

### HTTP Status Codes

| Code | Meaning | When |
|------|---------|------|
| 200 | Success | Record found, search completed |
| 404 | Not Found | Work UUID or entity UUID does not exist |
| 422 | Validation Error | Invalid UUID format, out-of-range parameters |
| 500 | Internal Server Error | Database connection failure, unexpected error |

### Handling Errors in Python

```python
import httpx

BASE_URL = "http://localhost:8000/api/v1"


def get_attribution(work_id: str) -> dict | None:
    """Fetch an attribution record with error handling."""
    try:
        response = httpx.get(f"{BASE_URL}/attributions/work/{work_id}")
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            print(f"Work {work_id} not found")
            return None
        elif e.response.status_code == 422:
            print(f"Invalid work ID format: {work_id}")
            return None
        else:
            raise
    except httpx.ConnectError:
        print("Cannot connect to API. Is the server running? (make agent)")
        return None
```

### Handling Errors in curl

```bash
# Check HTTP status code
STATUS=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8000/api/v1/attributions/work/invalid-uuid)
if [ "$STATUS" -eq 404 ]; then
    echo "Work not found"
elif [ "$STATUS" -eq 422 ]; then
    echo "Invalid UUID format"
fi
```

---

## OpenAPI Documentation

The FastAPI server provides interactive API documentation at:

- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

These are auto-generated from the route type annotations and include request/response schemas for every endpoint.
