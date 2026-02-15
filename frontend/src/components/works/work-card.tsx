"use client";

import Link from "next/link";
import type { AttributionRecord } from "@/lib/types/attribution";
import { getConfidenceTier, getConfidenceCssVar } from "@/lib/theme/confidence";
import { AssuranceBadge } from "./assurance-badge";
import { SourceTag } from "./source-tag";
import { ExternalLinkBadge } from "./external-link-badge";
import { ConfidencePopover } from "./confidence-popover";
import { getExternalLinks } from "@/lib/data/external-links";
import { trackEvent, EVENTS } from "@/lib/analytics/events";
import type { Source } from "@/lib/types/enums";

interface WorkCardProps {
  work: AttributionRecord;
}

export function WorkCard({ work }: WorkCardProps) {
  // Collect unique sources across all credits
  const allSources = new Set<Source>();
  for (const credit of work.credits) {
    for (const source of credit.sources) {
      allSources.add(source);
    }
  }

  const tier = getConfidenceTier(work.confidence_score);
  const color = getConfidenceCssVar(tier);
  const primaryCredit = work.credits[0];
  const externalLinks = getExternalLinks(work.attribution_id);

  return (
    <Link
      href={`/works/${work.attribution_id}`}
      className="group flex items-center gap-6 py-5 transition-colors duration-150 hover:bg-surface-secondary"
    >
      {/* Large confidence number — editorial typography with hover popover */}
      <ConfidencePopover
        score={work.confidence_score}
        conformalSet={work.conformal_set}
        onView={() =>
          trackEvent(EVENTS.CONFIDENCE_POPOVER_VIEWED, {
            attribution_id: work.attribution_id,
            confidence_score: work.confidence_score,
          })
        }
      >
        <div className="flex-shrink-0 w-16 text-right">
          <span
            className="editorial-display text-3xl"
            style={{ color }}
          >
            {Math.round(work.confidence_score * 100)}
          </span>
        </div>
      </ConfidencePopover>

      {/* Work info */}
      <div className="min-w-0 flex-1">
        <h3 className="text-base font-semibold text-heading group-hover:text-accent transition-colors duration-150">
          {work.work_title}
        </h3>
        <p className="mt-1 text-sm text-label">
          {work.artist_name}
          {primaryCredit?.role && (
            <span className="text-muted">
              {" "}
              — {primaryCredit.role.toLowerCase().replace(/_/g, " ")}
            </span>
          )}
        </p>
      </div>

      {/* Badges — source tags + external links */}
      <div className="hidden sm:flex items-center gap-2">
        <AssuranceBadge level={work.assurance_level} />
        {Array.from(allSources).map((source) => (
          <SourceTag key={source} source={source} />
        ))}
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
      </div>

      {/* Review indicator + version */}
      <div className="flex-shrink-0 text-right">
        {work.needs_review && (
          <p className="text-xs text-confidence-medium mb-1">
            Review
          </p>
        )}
        <span className="text-xs text-muted data-mono">
          v{work.version}
        </span>
      </div>
    </Link>
  );
}
