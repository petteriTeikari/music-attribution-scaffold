"use client";

import { useEffect, useState } from "react";
import { useParams } from "next/navigation";
import Link from "next/link";
import type { AttributionRecord } from "@/lib/types/attribution";
import { mockApi } from "@/lib/api/mock-client";
import { ConfidenceGauge, ConfidenceBadge } from "@/components/confidence/confidence-gauge";
import { AssuranceBadge } from "@/components/works/assurance-badge";
import { CreditList } from "@/components/attribution/credit-list";
import { ProvenanceTimeline } from "@/components/provenance/provenance-timeline";

export default function WorkDetailPage() {
  const params = useParams();
  const workId = params.workId as string;
  const [work, setWork] = useState<AttributionRecord | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    setLoading(true);
    mockApi.getWorkById(workId).then((data) => {
      setWork(data);
      setLoading(false);
    });
  }, [workId]);

  if (loading) {
    return (
      <div className="mx-auto max-w-4xl px-[var(--space-6)] py-[var(--space-10)]">
        <div className="space-y-[var(--space-6)]">
          <div className="h-8 w-48 animate-pulse rounded-[var(--radius-md)] bg-[var(--color-surface-secondary)]" />
          <div className="h-40 animate-pulse rounded-[var(--radius-lg)] bg-[var(--color-surface-secondary)]" />
          <div className="h-64 animate-pulse rounded-[var(--radius-lg)] bg-[var(--color-surface-secondary)]" />
        </div>
      </div>
    );
  }

  if (!work) {
    return (
      <div className="mx-auto max-w-4xl px-[var(--space-6)] py-[var(--space-10)]">
        <div className="rounded-[var(--radius-lg)] border border-[var(--color-border)] bg-[var(--color-surface-elevated)] p-[var(--space-12)] text-center">
          <h2 className="text-[var(--text-xl)] font-semibold text-[var(--color-heading)]">
            Work Not Found
          </h2>
          <p className="mt-[var(--space-2)] text-[var(--color-label)]">
            No attribution record found for this ID.
          </p>
          <Link
            href="/works"
            className="mt-[var(--space-4)] inline-block text-[var(--text-sm)] text-[var(--color-primary)] underline underline-offset-2"
          >
            Back to catalog
          </Link>
        </div>
      </div>
    );
  }

  return (
    <div className="mx-auto max-w-4xl px-[var(--space-6)] py-[var(--space-10)]">
      {/* Breadcrumb */}
      <nav className="mb-[var(--space-6)]" aria-label="Breadcrumb">
        <ol className="flex items-center gap-[var(--space-2)] text-[var(--text-sm)] text-[var(--color-muted)]">
          <li>
            <Link
              href="/works"
              className="text-[var(--color-primary)] hover:underline"
            >
              Works
            </Link>
          </li>
          <li aria-hidden="true">/</li>
          <li className="text-[var(--color-label)]">{work.work_title}</li>
        </ol>
      </nav>

      {/* Hero section */}
      <div className="rounded-[var(--radius-xl)] border border-[var(--color-border)] bg-[var(--color-surface-elevated)] p-[var(--space-8)] shadow-[var(--shadow-md)]">
        <div className="flex flex-col items-center gap-[var(--space-8)] md:flex-row md:items-start">
          {/* Large confidence gauge */}
          <div className="relative flex-shrink-0">
            <ConfidenceGauge score={work.confidence_score} size="lg" />
          </div>

          {/* Work info */}
          <div className="flex-1 text-center md:text-left">
            <h1 className="text-[var(--text-3xl)] font-bold text-[var(--color-heading)]">
              {work.work_title}
            </h1>
            <p className="mt-[var(--space-2)] text-[var(--text-lg)] text-[var(--color-label)]">
              {work.artist_name}
            </p>

            <div className="mt-[var(--space-4)] flex flex-wrap items-center justify-center gap-[var(--space-3)] md:justify-start">
              <AssuranceBadge level={work.assurance_level} />
              <ConfidenceBadge score={work.confidence_score} />
              <span className="text-[var(--text-sm)] text-[var(--color-muted)]">
                Source agreement: {Math.round(work.source_agreement * 100)}%
              </span>
            </div>

            {work.needs_review && (
              <div className="mt-[var(--space-4)] rounded-[var(--radius-md)] border border-[var(--color-confidence-medium)] bg-[var(--color-confidence-medium-bg)] px-[var(--space-4)] py-[var(--space-3)]">
                <p className="text-[var(--text-sm)] font-medium" style={{ color: "var(--color-confidence-medium)" }}>
                  This attribution needs review (priority: {Math.round(work.review_priority * 100)}%)
                </p>
              </div>
            )}

            {/* Conformal set info */}
            <div className="mt-[var(--space-4)] text-[var(--text-sm)] text-[var(--color-muted)]">
              <span>
                Conformal coverage: {Math.round(work.conformal_set.marginal_coverage * 100)}%
                at {Math.round(work.conformal_set.coverage_level * 100)}% level
              </span>
              <span className="mx-[var(--space-2)]">|</span>
              <span>
                Calibration error: {work.conformal_set.calibration_error.toFixed(3)}
              </span>
              <span className="mx-[var(--space-2)]">|</span>
              <span>v{work.version}</span>
            </div>
          </div>
        </div>
      </div>

      {/* Credits section */}
      <div className="mt-[var(--space-8)]">
        <CreditList credits={work.credits} />
      </div>

      {/* Provenance timeline */}
      <div className="mt-[var(--space-8)]">
        <h3 className="text-[var(--text-base)] font-semibold text-[var(--color-heading)] mb-[var(--space-4)]">
          Provenance Timeline
        </h3>
        <ProvenanceTimeline events={work.provenance_chain} />
      </div>
    </div>
  );
}
