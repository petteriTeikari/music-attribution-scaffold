# fig-backend-05: Rate Limiting Strategy

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-backend-05 |
| **Title** | Token Bucket Rate Limiter: Per-Source API Compliance |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 |
| **Location** | docs/architecture/, docs/etl/ |
| **Priority** | P2 (Medium) |
| **Dimensions** | 1200 x 675px (16:9) |

## Purpose & Key Message

This figure explains the token bucket rate limiting mechanism used to comply with external API rate limits. Engineers extending the system with new data sources need to understand how the rate limiter works and how to configure it per source.

The key message is: "A shared TokenBucketRateLimiter class enforces per-source rate limits with async locking -- tokens refill over time, requests wait when the bucket is empty, and each connector gets its own instance configured for its API's policy."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  TOKEN BUCKET RATE LIMITER                                     |
|  ■ Async API Compliance with Exponential Backoff               |
+---------------------------------------------------------------+
|                                                                 |
|  HOW IT WORKS                                                  |
|  ─────────────                                                 |
|                                                                 |
|  ┌──────────────────────────────────┐                          |
|  │         TOKEN BUCKET              │                          |
|  │  ┌─┬─┬─┐                         │                          |
|  │  │T│T│ │  capacity = max tokens   │                          |
|  │  └─┴─┴─┘                         │                          |
|  │  Refill: +rate tokens/second      │                          |
|  │  Acquire: -1 token per request    │                          |
|  │  Empty: await sleep(wait_time)    │                          |
|  │  Lock: asyncio.Lock (1 at a time)│                          |
|  └──────────────────────────────────┘                          |
|                                                                 |
|  PER-SOURCE CONFIGURATION             RETRY STRATEGY           |
|  ────────────────────────             ──────────────           |
|  ┌──────────────┬──────┬──────────┐   Attempts: max_retries=3  |
|  │ Source       │ Rate │ Capacity │   Backoff: 2^attempt sec   |
|  ├──────────────┼──────┼──────────┤   ┌──────────────────────┐ |
|  │ MusicBrainz  │ 1.0/s│    1     │   │ Attempt 1: immediate │ |
|  │ Discogs(auth)│ 1.0/s│    1     │   │ Attempt 2: wait 1s   │ |
|  │ Discogs(no)  │ 0.42/s│   1     │   │ Attempt 3: wait 2s   │ |
|  │ AcoustID     │ 3.0/s│    3     │   │ Attempt 4: wait 4s   │ |
|  │ tinytag      │  N/A │   N/A    │   │ (then raise)         │ |
|  │ Artist Input │  N/A │   N/A    │   └──────────────────────┘ |
|  └──────────────┴──────┴──────────┘                            |
|                                                                 |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "TOKEN BUCKET RATE LIMITER" |
| Token bucket diagram | `processing_stage` | Visual bucket with tokens, showing refill/acquire/wait mechanics |
| Rate table | `data_mono` | Per-source rate and capacity values |
| Retry strategy | `processing_stage` | Exponential backoff: 2^attempt seconds |
| asyncio.Lock note | `label_editorial` | Concurrency control mechanism |
| MusicBrainz row | `source_musicbrainz` | 1.0 req/s, capacity 1 |
| Discogs auth row | `source_discogs` | 1.0 req/s (60/min), capacity 1 |
| Discogs unauth row | `source_discogs` | 0.42 req/s (25/min), capacity 1 |
| AcoustID row | `source_acoustid` | 3.0 req/s, capacity 3 |
| tinytag row | `source_file` | N/A -- local file reads |
| Flow arrows | `data_flow` | Token flow: refill -> acquire -> wait cycle |

## Anti-Hallucination Rules

1. The class is TokenBucketRateLimiter in `music_attribution.etl.rate_limiter`, not a leaky bucket or sliding window.
2. MusicBrainz rate limit is exactly 1 req/s (from code: rate=1.0, capacity=1).
3. Discogs authenticated is 1.0/s (60/min), unauthenticated is 25.0/60.0 = ~0.42/s (from DiscogsConnector.__init__).
4. AcoustID rate is 3.0/s with capacity=3 (from AcoustIDConnector.__init__).
5. The lock mechanism is asyncio.Lock, not threading.Lock.
6. Backoff formula is 2^attempt seconds (wait = 2**attempt from the code).
7. Default max_retries is 3 for all connectors.
8. tinytag and Artist Input have no rate limiting -- they are local operations.

## Alt Text

Architecture diagram of the token bucket rate limiter used in the music attribution scaffold, showing per-source API rate configurations — MusicBrainz at 1 req/s, Discogs at 1 req/s authenticated, and AcoustID at 3 req/s — with async locking, exponential backoff retry strategy, and capacity settings ensuring compliant music metadata extraction.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Architecture diagram of the token bucket rate limiter used in the music attribution scaffold, showing per-source API rate configurations — MusicBrainz at 1 req/s, Discogs at 1 req/s authenticated, and AcoustID at 3 req/s — with async locking, exponential backoff retry strategy, and capacity settings ensuring compliant music metadata extraction.](docs/figures/repo-figures/assets/fig-backend-05-rate-limiting-strategy.jpg)

*Figure 5. The TokenBucketRateLimiter enforces per-source API rate limits with asyncio locking and exponential backoff (2^attempt seconds), ensuring that the ETL pipeline remains compliant with MusicBrainz, Discogs, and AcoustID usage policies.*

### From this figure plan (relative)

![Architecture diagram of the token bucket rate limiter used in the music attribution scaffold, showing per-source API rate configurations — MusicBrainz at 1 req/s, Discogs at 1 req/s authenticated, and AcoustID at 3 req/s — with async locking, exponential backoff retry strategy, and capacity settings ensuring compliant music metadata extraction.](../assets/fig-backend-05-rate-limiting-strategy.jpg)
