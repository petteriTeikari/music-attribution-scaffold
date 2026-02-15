"use client";

import { useEffect, useState } from "react";
import { useParams } from "next/navigation";
import Link from "next/link";
import type { AttributionRecord } from "@/lib/types/attribution";
import { apiClient } from "@/lib/api/api-client";
import { ConfidenceGauge, ConfidenceBadge } from "@/components/confidence/confidence-gauge";
import { AssuranceBadge } from "@/components/works/assurance-badge";
import { CreditList } from "@/components/attribution/credit-list";
import { ProvenanceTimeline } from "@/components/provenance/provenance-timeline";
import { ProvenancePanel } from "@/components/citations/provenance-panel";
import { ProvenanceDag } from "@/components/provenance/provenance-dag";
import { ExternalLinkBadge } from "@/components/works/external-link-badge";
import { getExternalLinks, MUSICBRAINZ_ARTIST_URL } from "@/lib/data/external-links";
import { trackEvent, EVENTS } from "@/lib/analytics/events";
import { AdaptiveTooltip } from "@/components/ui/adaptive-tooltip";

export default function WorkDetailPage() {
  const params = useParams();
  const workId = params.workId as string;
  const [work, setWork] = useState<AttributionRecord | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    setLoading(true);
    apiClient.getWorkById(workId).then((data) => {
      setWork(data);
      setLoading(false);
    }).catch(() => {
      setWork(null);
      setLoading(false);
    });
  }, [workId]);

  if (loading) {
    return (
      <div className="px-8 py-10">
        <div className="space-y-6">
          <div className="h-8 w-48 animate-pulse bg-surface-secondary" />
          <div className="h-40 animate-pulse bg-surface-secondary" />
          <div className="h-64 animate-pulse bg-surface-secondary" />
        </div>
      </div>
    );
  }

  if (!work) {
    return (
      <div className="px-8 py-10">
        <div className="py-20 text-center">
          <h2 className="editorial-display text-2xl text-heading">
            Work Not Found
          </h2>
          <p className="mt-2 text-label">
            No attribution record found for this ID.
          </p>
          <Link
            href="/works"
            className="mt-4 inline-block text-sm text-accent underline underline-offset-2"
          >
            Back to catalog
          </Link>
        </div>
      </div>
    );
  }

  const externalLinks = getExternalLinks(work.attribution_id);
  const hasExternalLinks =
    externalLinks.musicbrainz_recording_url || externalLinks.discogs_master_url;

  return (
    <div className="px-8 py-10">
      {/* Breadcrumb */}
      <nav className="mb-6" aria-label="Breadcrumb">
        <ol className="flex items-center gap-2 text-xs editorial-caps text-muted">
          <li>
            <Link
              href="/works"
              className="text-accent hover:underline"
            >
              Works
            </Link>
          </li>
          <li aria-hidden="true">/</li>
          <li className="text-label">{work.work_title}</li>
        </ol>
      </nav>

      {/* Hero section — large confidence + work info */}
      <div className="grid gap-8 lg:grid-cols-[auto_1fr] items-start">
        {/* Large confidence display */}
        <div className="flex flex-col items-center">
          <AdaptiveTooltip
            id="detail-gauge-intro"
            skill="confidence_reading"
            content="This gauge shows overall attribution confidence. Green (85%+) means high agreement across sources. The score updates as new evidence arrives through the provenance pipeline."
            compactContent="Confidence from multi-source agreement."
            placement="right"
          >
            <ConfidenceGauge score={work.confidence_score} size="lg" />
          </AdaptiveTooltip>
        </div>

        {/* Work info */}
        <div>
          <h1 className="editorial-display text-4xl text-heading">
            {work.work_title}
          </h1>
          <p className="mt-2 text-lg text-label">
            {work.artist_name}
          </p>

          <div className="mt-4 flex flex-wrap items-center gap-3">
            <AdaptiveTooltip
              id="detail-assurance-intro"
              skill="confidence_reading"
              content="Assurance levels range from A0 (no data) to A3 (artist-verified). Higher levels require more independent verification sources."
              compactContent="A0-A3: provenance tiers."
            >
              <AssuranceBadge level={work.assurance_level} />
            </AdaptiveTooltip>
            <ConfidenceBadge score={work.confidence_score} />
            <span className="text-sm text-muted data-mono">
              Source agreement: {Math.round(work.source_agreement * 100)}%
            </span>
          </div>

          {work.needs_review && (
            <div className="mt-4 border-l-2 border-confidence-medium pl-4 py-2">
              <p className="text-sm font-medium" style={{ color: "var(--color-confidence-medium)" }}>
                This attribution needs review (priority: {Math.round(work.review_priority * 100)}%)
              </p>
            </div>
          )}

          {/* Conformal set info */}
          <div className="mt-4 text-sm text-muted data-mono">
            <span>
              Conformal coverage: {Math.round(work.conformal_set.marginal_coverage * 100)}%
              at {Math.round(work.conformal_set.coverage_level * 100)}% level
            </span>
            <span className="mx-2">|</span>
            <span>
              Calibration error: {work.conformal_set.calibration_error.toFixed(3)}
            </span>
            <span className="mx-2">|</span>
            <span>v{work.version}</span>
          </div>
        </div>
      </div>

      <div className="accent-line my-8" style={{ opacity: 0.3 }} />

      {/* External sources section */}
      <div>
        <div className="flex items-center gap-2 mb-2">
          <span className="accent-square-sm" aria-hidden="true" />
          <span className="editorial-caps text-xs text-accent">
            External Sources
          </span>
        </div>

        {hasExternalLinks ? (
          <div className="flex flex-wrap items-center gap-4">
            {externalLinks.musicbrainz_recording_url && (
              <ExternalLinkBadge
                source="musicbrainz"
                url={externalLinks.musicbrainz_recording_url}
                onClick={() =>
                  trackEvent(EVENTS.EXTERNAL_LINK_CLICKED, {
                    attribution_id: work.attribution_id,
                    source: "musicbrainz",
                    url: externalLinks.musicbrainz_recording_url!,
                  })
                }
              />
            )}
            {externalLinks.discogs_master_url && (
              <ExternalLinkBadge
                source="discogs"
                url={externalLinks.discogs_master_url}
                onClick={() =>
                  trackEvent(EVENTS.EXTERNAL_LINK_CLICKED, {
                    attribution_id: work.attribution_id,
                    source: "discogs",
                    url: externalLinks.discogs_master_url!,
                  })
                }
              />
            )}
            <a
              href={MUSICBRAINZ_ARTIST_URL}
              target="_blank"
              rel="noopener noreferrer"
              className="text-xs text-muted underline underline-offset-2 hover:text-heading"
            >
              MusicBrainz artist profile
            </a>
          </div>
        ) : (
          <p className="text-sm text-muted">
            No external sources verified for this work.
          </p>
        )}
      </div>

      <div className="accent-line my-8" style={{ opacity: 0.3 }} />

      {/* Credits section */}
      <div>
        <span className="editorial-caps text-xs text-accent block mb-2">
          Credits
        </span>
        <CreditList credits={work.credits} provenanceEvents={work.provenance_chain} />
      </div>

      <div className="accent-line my-8" style={{ opacity: 0.3 }} />

      {/* Provenance sources panel (Perplexity-like) */}
      <div>
        <ProvenancePanel events={work.provenance_chain} />
      </div>

      <div className="accent-line my-8" style={{ opacity: 0.3 }} />

      {/* Provenance DAG */}
      <div>
        <span className="editorial-caps text-xs text-accent block mb-2">
          Pipeline
        </span>
        <h3 className="editorial-display text-xl text-heading mb-4">
          Provenance DAG
        </h3>
        <ProvenanceDag
          events={work.provenance_chain}
          attributionId={work.attribution_id}
          onExpand={() =>
            trackEvent(EVENTS.PROVENANCE_DAG_EXPANDED, {
              attribution_id: work.attribution_id,
              event_count: work.provenance_chain.length,
            })
          }
        />
      </div>

      <div className="accent-line my-8" style={{ opacity: 0.3 }} />

      {/* Provenance timeline */}
      <div>
        <span className="editorial-caps text-xs text-accent block mb-2">
          Provenance
        </span>
        <h3 className="editorial-display text-xl text-heading mb-4">
          Timeline
        </h3>
        <ProvenanceTimeline events={work.provenance_chain} />
      </div>
    </div>
  );
}
