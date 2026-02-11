"use client";

import Link from "next/link";
import type { AttributionRecord } from "@/lib/types/attribution";
import { getConfidenceTier, getConfidenceCssVar } from "@/lib/theme/confidence";
import { AssuranceBadge } from "./assurance-badge";
import { SourceTag } from "./source-tag";
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

  return (
    <Link
      href={`/works/${work.attribution_id}`}
      className="group flex items-center gap-[var(--space-6)] py-[var(--space-5)] transition-colors duration-[var(--transition-fast)] hover:bg-[var(--color-surface-secondary)]"
    >
      {/* Large confidence number — editorial typography */}
      <div className="flex-shrink-0 w-16 text-right">
        <span
          className="editorial-display text-[var(--text-3xl)]"
          style={{ color }}
        >
          {Math.round(work.confidence_score * 100)}
        </span>
      </div>

      {/* Work info */}
      <div className="min-w-0 flex-1">
        <h3 className="text-[var(--text-base)] font-semibold text-[var(--color-heading)] group-hover:text-[var(--color-accent)] transition-colors duration-[var(--transition-fast)]">
          {work.work_title}
        </h3>
        <p className="mt-[var(--space-1)] text-[var(--text-sm)] text-[var(--color-label)]">
          {work.artist_name}
          {primaryCredit?.role && (
            <span className="text-[var(--color-muted)]">
              {" "}
              — {primaryCredit.role.toLowerCase().replace(/_/g, " ")}
            </span>
          )}
        </p>
      </div>

      {/* Badges */}
      <div className="hidden sm:flex items-center gap-[var(--space-2)]">
        <AssuranceBadge level={work.assurance_level} />
        {Array.from(allSources).map((source) => (
          <SourceTag key={source} source={source} />
        ))}
      </div>

      {/* Review indicator + version */}
      <div className="flex-shrink-0 text-right">
        {work.needs_review && (
          <p className="text-[var(--text-xs)] text-[var(--color-confidence-medium)] mb-[var(--space-1)]">
            Review
          </p>
        )}
        <span className="text-[var(--text-xs)] text-[var(--color-muted)] data-mono">
          v{work.version}
        </span>
      </div>
    </Link>
  );
}
