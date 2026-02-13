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
          <ConfidenceGauge score={work.confidence_score} size="lg" />
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
            <AssuranceBadge level={work.assurance_level} />
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
