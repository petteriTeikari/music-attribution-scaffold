# fig-choice-16: Object Storage Strategy — Zero-Egress R2 vs Hyperscaler S3

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-choice-16 |
| **Title** | Object Storage: Cloudflare R2 Zero-Egress vs Hyperscaler Pricing |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 (implementation detail) |
| **Location** | docs/prd/decisions/L4-deployment/object-storage.decision.yaml |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

Explains the object storage decision added in PRD v2.1.0. Audio files dominate egress costs -- a music attribution platform serving 10TB/month in audio previews pays $0 with Cloudflare R2 vs $900+ with AWS S3. This figure shows the egress cost comparison across six options and maps each to the scaffold's compute platform archetypes.

The key message is: "Cloudflare R2 eliminates egress fees entirely -- the dominant cost for audio-heavy workloads. At 100TB/month, R2 saves $2,700-9,000 compared to hyperscaler object storage."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  OBJECT STORAGE STRATEGY                                       |
|  ■ Zero-Egress vs Hyperscaler Pricing                          |
+---------------------------------------------------------------+
|                                                                |
|  WHY IT MATTERS FOR AUDIO                                      |
|  ────────────────────────                                      |
|  Audio previews, waveform renders, and metadata exports        |
|  make egress the dominant storage cost.                         |
|  A 30-second MP3 preview = ~500KB per request.                 |
|                                                                |
|  EGRESS COST AT SCALE                                          |
|  ────────────────────                                          |
|                                                                |
|  Monthly egress       10 TB         100 TB                     |
|  ────────────────────────────────────────────                  |
|  Cloudflare R2        $0            $0                         |
|  Hetzner Object       ~$10          ~$100                      |
|  Backblaze B2         $10           $100                       |
|  AWS S3               $900          $9,000                     |
|  GCP Cloud Storage    $1,200        $12,000                    |
|  Azure Blob           $870          $8,700                     |
|                                                                |
|  ┌───────────────────────────────────────────────────────┐    |
|  │  CLOUDFLARE R2                                         │    |
|  │  ■ RECOMMENDED (P=0.45)                                │    |
|  │                                                        │    |
|  │  ■ Zero egress fees (S3-compatible API)                │    |
|  │  ■ $0.015/GB storage ($150/10TB)                       │    |
|  │  ■ Workers for edge processing                         │    |
|  │  ■ No minimum commitment                               │    |
|  │  ■ Works with any compute platform                     │    |
|  └───────────────────────────────────────────────────────┘    |
|                                                                |
|  vs ALTERNATIVES                                               |
|  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐          |
|  │ Hetzner Obj  │ │ Backblaze B2 │ │ AWS S3       │          |
|  │──────────────│ │──────────────│ │──────────────│          |
|  │ Low egress   │ │ Low egress   │ │ S3-native    │          |
|  │ EU-only      │ │ B2+CF free   │ │ Full eco-    │          |
|  │ P=0.20       │ │ P=0.15       │ │ system       │          |
|  │              │ │              │ │ P=0.10       │          |
|  │ Best with    │ │ Best with    │ │ Best with    │          |
|  │ Hetzner      │ │ CF Workers   │ │ Big Three    │          |
|  │ compute      │ │              │ │ compute      │          |
|  └──────────────┘ └──────────────┘ └──────────────┘          |
|                                                                |
+---------------------------------------------------------------+
|  NEW in PRD v2.1.0 — egress is the hidden cost of audio       |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "OBJECT STORAGE STRATEGY" with coral accent square |
| Audio context | `callout_box` | Why egress matters for audio workloads (500KB per preview) |
| Egress cost table | `data_mono` | Six providers at 10TB and 100TB monthly egress |
| R2 recommendation | `selected_option` | Zero egress, S3-compatible API, Workers, no minimum |
| Hetzner Object Storage | `deferred_option` | Low egress, EU-only, best with Hetzner compute |
| Backblaze B2 | `deferred_option` | Low egress, B2+CF bandwidth alliance |
| AWS S3 | `deferred_option` | S3-native ecosystem, high egress costs |
| PRD version footer | `callout_bar` | New node in v2.1.0 |

## Anti-Hallucination Rules

1. Object Storage is a NEW node in PRD v2.1.0 (`_network.yaml` v2.1.0) -- it did not exist before.
2. Cloudflare R2 has ZERO egress fees -- this is its primary differentiator. Storage is $0.015/GB/month.
3. AWS S3 standard egress is ~$0.09/GB after first 100GB. At 100TB/month that is ~$9,000.
4. R2 provides an S3-compatible API -- existing S3 SDKs work with minimal config changes.
5. Six options in the decision YAML: cloudflare_r2 (0.45), hetzner_object_storage (0.20), backblaze_b2 (0.15), aws_s3 (0.10), gcp_gcs (0.05), azure_blob (0.05).
6. Hetzner Object Storage is EU-only (Falkenstein, Nuremberg, Helsinki) as of Feb 2026.
7. Backblaze B2 has a bandwidth alliance with Cloudflare -- zero egress when served through CF.
8. The audio use case (previews, waveforms, exports) makes egress the dominant cost, not storage volume.
9. Do NOT claim R2 is "free" -- storage costs still apply, only egress is zero.
10. Background must be warm cream (#f6f3e6).

## Alt Text

Architecture decision: Cloudflare R2 selected for music attribution scaffold object storage with zero egress fees, compared against Hetzner Object Storage, Backblaze B2, and AWS S3 in an egress cost table showing $0 versus $9,000 per month at 100TB scale -- a critical FinOps decision for audio-heavy workloads where preview serving dominates bandwidth costs in the open-source attribution platform.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Architecture decision: Cloudflare R2 selected for music attribution scaffold object storage with zero egress fees, compared against Hetzner Object Storage, Backblaze B2, and AWS S3 in an egress cost table showing $0 versus $9,000 per month at 100TB scale -- a critical FinOps decision for audio-heavy workloads where preview serving dominates bandwidth costs in the open-source attribution platform.](docs/figures/repo-figures/assets/fig-choice-16-object-storage-strategy.jpg)

*Cloudflare R2 eliminates egress fees entirely for the music attribution scaffold's audio workloads -- at 100TB/month, R2 saves $9,000 versus AWS S3. The S3-compatible API means switching requires only endpoint configuration, not code changes (PRD v2.1.0 node: object_storage).*

### From this figure plan (relative)

![Architecture decision: Cloudflare R2 selected for music attribution scaffold object storage with zero egress fees, compared against Hetzner Object Storage, Backblaze B2, and AWS S3 in an egress cost table showing $0 versus $9,000 per month at 100TB scale -- a critical FinOps decision for audio-heavy workloads where preview serving dominates bandwidth costs in the open-source attribution platform.](../assets/fig-choice-16-object-storage-strategy.jpg)
