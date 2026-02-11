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
      <div className="px-[var(--space-8)] py-[var(--space-10)]">
        <div className="space-y-[var(--space-6)]">
          <div className="h-8 w-48 animate-pulse bg-[var(--color-surface-secondary)]" />
          <div className="h-40 animate-pulse bg-[var(--color-surface-secondary)]" />
          <div className="h-64 animate-pulse bg-[var(--color-surface-secondary)]" />
        </div>
      </div>
    );
  }

  if (!work) {
    return (
      <div className="px-[var(--space-8)] py-[var(--space-10)]">
        <div className="py-[var(--space-20)] text-center">
          <h2 className="editorial-display text-[var(--text-2xl)] text-[var(--color-heading)]">
            Work Not Found
          </h2>
          <p className="mt-[var(--space-2)] text-[var(--color-label)]">
            No attribution record found for this ID.
          </p>
          <Link
            href="/works"
            className="mt-[var(--space-4)] inline-block text-[var(--text-sm)] text-[var(--color-accent)] underline underline-offset-2"
          >
            Back to catalog
          </Link>
        </div>
      </div>
    );
  }

  return (
    <div className="px-[var(--space-8)] py-[var(--space-10)]">
      {/* Breadcrumb */}
      <nav className="mb-[var(--space-6)]" aria-label="Breadcrumb">
        <ol className="flex items-center gap-[var(--space-2)] text-[var(--text-xs)] editorial-caps text-[var(--color-muted)]">
          <li>
            <Link
              href="/works"
              className="text-[var(--color-accent)] hover:underline"
            >
              Works
            </Link>
          </li>
          <li aria-hidden="true">/</li>
          <li className="text-[var(--color-label)]">{work.work_title}</li>
        </ol>
      </nav>

      {/* Hero section — large confidence + work info */}
      <div className="grid gap-[var(--space-8)] lg:grid-cols-[auto_1fr] items-start">
        {/* Large confidence display */}
        <div className="flex flex-col items-center">
          <ConfidenceGauge score={work.confidence_score} size="lg" />
        </div>

        {/* Work info */}
        <div>
          <h1 className="editorial-display text-[var(--text-4xl)] text-[var(--color-heading)]">
            {work.work_title}
          </h1>
          <p className="mt-[var(--space-2)] text-[var(--text-lg)] text-[var(--color-label)]">
            {work.artist_name}
          </p>

          <div className="mt-[var(--space-4)] flex flex-wrap items-center gap-[var(--space-3)]">
            <AssuranceBadge level={work.assurance_level} />
            <ConfidenceBadge score={work.confidence_score} />
            <span className="text-[var(--text-sm)] text-[var(--color-muted)] data-mono">
              Source agreement: {Math.round(work.source_agreement * 100)}%
            </span>
          </div>

          {work.needs_review && (
            <div className="mt-[var(--space-4)] border-l-2 border-[var(--color-confidence-medium)] pl-[var(--space-4)] py-[var(--space-2)]">
              <p className="text-[var(--text-sm)] font-medium" style={{ color: "var(--color-confidence-medium)" }}>
                This attribution needs review (priority: {Math.round(work.review_priority * 100)}%)
              </p>
            </div>
          )}

          {/* Conformal set info */}
          <div className="mt-[var(--space-4)] text-[var(--text-sm)] text-[var(--color-muted)] data-mono">
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

      <div className="accent-line my-[var(--space-8)]" style={{ opacity: 0.3 }} />

      {/* Credits section */}
      <div>
        <span className="editorial-caps text-[var(--text-xs)] text-[var(--color-accent)] block mb-[var(--space-2)]">
          Credits
        </span>
        <CreditList credits={work.credits} />
      </div>

      <div className="accent-line my-[var(--space-8)]" style={{ opacity: 0.3 }} />

      {/* Provenance timeline */}
      <div>
        <span className="editorial-caps text-[var(--text-xs)] text-[var(--color-accent)] block mb-[var(--space-2)]">
          Provenance
        </span>
        <h3 className="editorial-display text-[var(--text-xl)] text-[var(--color-heading)] mb-[var(--space-4)]">
          Timeline
        </h3>
        <ProvenanceTimeline events={work.provenance_chain} />
      </div>
    </div>
  );
}
