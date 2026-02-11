"use client";

import Link from "next/link";
import type { AttributionRecord } from "@/lib/types/attribution";
import { ConfidenceGauge } from "@/components/confidence/confidence-gauge";
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

  const primaryCredit = work.credits[0];

  return (
    <Link
      href={`/works/${work.attribution_id}`}
      className="group block rounded-[var(--radius-lg)] border border-[var(--color-border)] bg-[var(--color-surface-elevated)] p-[var(--space-6)] shadow-[var(--shadow-sm)] transition-all duration-[var(--transition-base)] hover:border-[var(--color-border-strong)] hover:shadow-[var(--shadow-md)]"
    >
      <div className="flex items-start gap-[var(--space-5)]">
        {/* Confidence gauge */}
        <div className="relative flex-shrink-0">
          <ConfidenceGauge score={work.confidence_score} size="sm" showLabel={false} />
        </div>

        {/* Work info */}
        <div className="min-w-0 flex-1">
          <h3 className="text-[var(--text-lg)] font-semibold text-[var(--color-heading)] group-hover:text-[var(--color-primary)] transition-colors duration-[var(--transition-fast)]">
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

          {/* Badges row */}
          <div className="mt-[var(--space-3)] flex flex-wrap items-center gap-[var(--space-2)]">
            <AssuranceBadge level={work.assurance_level} />
            {Array.from(allSources).map((source) => (
              <SourceTag key={source} source={source} />
            ))}
          </div>

          {/* Review indicator */}
          {work.needs_review && (
            <p className="mt-[var(--space-3)] text-[var(--text-xs)] text-[var(--color-confidence-medium)]">
              Needs review — priority{" "}
              {Math.round(work.review_priority * 100)}%
            </p>
          )}
        </div>

        {/* Score number */}
        <div className="flex-shrink-0 text-right">
          <span className="text-[var(--text-sm)] text-[var(--color-muted)]">
            v{work.version}
          </span>
        </div>
      </div>
    </Link>
  );
}
