"use client";

import { useEffect, useState } from "react";
import { useAtomValue } from "jotai";
import { userRoleAtom } from "@/lib/stores/mode";
import type { AttributionRecord } from "@/lib/types/attribution";
import { mockApi } from "@/lib/api/mock-client";
import { ConfidenceGauge } from "@/components/confidence/confidence-gauge";
import { AssuranceBadge } from "@/components/works/assurance-badge";

interface SuggestionDiff {
  field: string;
  current: string;
  suggested: string;
}

function generateSuggestions(work: AttributionRecord): SuggestionDiff[] {
  const suggestions: SuggestionDiff[] = [];

  if (work.confidence_score < 0.5) {
    suggestions.push({
      field: "assurance_level",
      current: work.assurance_level,
      suggested: "LEVEL_2",
    });
  }

  // Suggest adding missing credits for works with low source count
  const uniqueSources = new Set(work.credits.flatMap((c) => c.sources));
  if (uniqueSources.size < 3) {
    suggestions.push({
      field: "sources",
      current: `${uniqueSources.size} source(s)`,
      suggested: "Add MusicBrainz cross-reference",
    });
  }

  if (work.credits.some((c) => c.confidence < 0.5)) {
    suggestions.push({
      field: "credit_confidence",
      current: "Some credits below 50%",
      suggested: "Request artist verification",
    });
  }

  return suggestions;
}

export default function ReviewPage() {
  const role = useAtomValue(userRoleAtom);
  const [works, setWorks] = useState<AttributionRecord[]>([]);
  const [loading, setLoading] = useState(true);
  const [approvedIds, setApprovedIds] = useState<Set<string>>(new Set());

  useEffect(() => {
    mockApi.getWorks().then((data) => {
      setWorks(data.filter((w) => w.needs_review).sort((a, b) => b.review_priority - a.review_priority));
      setLoading(false);
    });
  }, []);

  const pendingWorks = works.filter((w) => !approvedIds.has(w.attribution_id));
  const approvedCount = approvedIds.size;

  function handleApprove(id: string) {
    setApprovedIds((prev) => new Set([...prev, id]));
  }

  function handleApproveAll() {
    setApprovedIds(new Set(works.map((w) => w.attribution_id)));
  }

  if (role !== "artist") {
    return (
      <div className="px-[var(--space-8)] py-[var(--space-10)]">
        <div className="py-[var(--space-20)] text-center">
          <h2 className="editorial-display text-2xl text-[var(--color-heading)]">
            Artist Mode Required
          </h2>
          <p className="mt-[var(--space-2)] text-[var(--color-label)]">
            Switch to Artist mode to access the review queue.
          </p>
        </div>
      </div>
    );
  }

  return (
    <div className="px-[var(--space-8)] py-[var(--space-10)]">
      {/* Header */}
      <div className="mb-[var(--space-8)] flex items-start justify-between">
        <div>
          <span className="editorial-caps text-xs text-[var(--color-accent)] block mb-[var(--space-2)]">
            Review
          </span>
          <h1 className="editorial-display text-4xl text-[var(--color-heading)]">
            Review Queue
          </h1>
          <p className="mt-[var(--space-2)] text-[var(--color-label)]">
            AI-suggested attribution improvements for your review.
          </p>
        </div>

        {/* Progress + Approve All */}
        <div className="flex items-center gap-[var(--space-4)]">
          <span className="text-sm text-[var(--color-label)] data-mono">
            {approvedCount}/{works.length}
          </span>
          {pendingWorks.length > 0 && (
            <button
              onClick={handleApproveAll}
              className="editorial-caps text-xs text-[var(--color-heading)] underline underline-offset-4 decoration-[var(--color-accent)] decoration-2 hover:text-[var(--color-accent)] transition-colors duration-[var(--transition-fast)]"
            >
              Approve All
            </button>
          )}
        </div>
      </div>

      {/* Progress bar */}
      <div className="mb-[var(--space-6)] h-px bg-[var(--color-border)] relative">
        <div
          className="h-px absolute top-0 left-0 transition-all duration-[var(--transition-slow)]"
          style={{
            width: works.length > 0 ? `${(approvedCount / works.length) * 100}%` : "0%",
            backgroundColor: "var(--color-confidence-high)",
          }}
        />
      </div>

      {loading ? (
        <div className="space-y-[var(--space-4)]">
          {Array.from({ length: 3 }).map((_, i) => (
            <div
              key={i}
              className="h-32 animate-pulse bg-[var(--color-surface-secondary)]"
            />
          ))}
        </div>
      ) : pendingWorks.length === 0 ? (
        <div className="py-[var(--space-20)] text-center">
          <p className="editorial-display text-2xl text-[var(--color-confidence-high)]">
            All caught up
          </p>
          <p className="mt-[var(--space-2)] text-[var(--color-label)]">
            {approvedCount} attribution{approvedCount !== 1 ? "s" : ""} reviewed.
          </p>
        </div>
      ) : (
        <div className="divide-y divide-[var(--color-border)]">
          {pendingWorks.map((work) => {
            const suggestions = generateSuggestions(work);
            return (
              <div
                key={work.attribution_id}
                className="py-[var(--space-6)]"
              >
                <div className="flex items-start gap-[var(--space-5)]">
                  <div className="flex items-center gap-[var(--space-3)]">
                    <div className="accent-square-sm" aria-hidden="true" />
                    <ConfidenceGauge
                      score={work.confidence_score}
                      size="sm"
                      showLabel={false}
                    />
                  </div>

                  <div className="min-w-0 flex-1">
                    <div className="flex items-center gap-[var(--space-3)]">
                      <h3 className="text-base font-semibold text-[var(--color-heading)]">
                        {work.work_title}
                      </h3>
                      <AssuranceBadge level={work.assurance_level} />
                    </div>
                    <p className="mt-[var(--space-1)] text-sm text-[var(--color-label)]">
                      {work.artist_name} — Priority{" "}
                      {Math.round(work.review_priority * 100)}%
                    </p>

                    {/* Suggestion diffs */}
                    {suggestions.length > 0 && (
                      <div className="mt-[var(--space-4)] space-y-[var(--space-2)]">
                        <p className="editorial-caps text-xs text-[var(--color-label)]">
                          Suggestions
                        </p>
                        {suggestions.map((s, i) => (
                          <div
                            key={i}
                            className="flex items-center gap-[var(--space-3)] py-[var(--space-1)] text-sm"
                          >
                            <span className="text-[var(--color-confidence-low)] line-through">
                              {s.current}
                            </span>
                            <span className="text-[var(--color-accent)]">→</span>
                            <span className="text-[var(--color-confidence-high)] font-medium">
                              {s.suggested}
                            </span>
                          </div>
                        ))}
                      </div>
                    )}
                  </div>

                  <button
                    onClick={() => handleApprove(work.attribution_id)}
                    className="flex-shrink-0 editorial-caps text-xs border-b-2 border-[var(--color-confidence-high)] pb-[var(--space-1)] transition-colors duration-[var(--transition-fast)] hover:text-[var(--color-confidence-high)]"
                    style={{ color: "var(--color-confidence-high)" }}
                  >
                    Approve
                  </button>
                </div>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
}
