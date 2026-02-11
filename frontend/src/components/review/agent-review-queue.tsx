"use client";

import { useState } from "react";
import type { AttributionRecord } from "@/lib/types/attribution";
import { ConfidenceGauge } from "@/components/confidence/confidence-gauge";
import { AssuranceBadge } from "@/components/works/assurance-badge";

interface AgentSuggestion {
  field: string;
  current: string;
  suggested: string;
  reason: string;
  confidence: number;
}

interface AgentReviewQueueProps {
  works: AttributionRecord[];
  onApprove: (id: string) => void;
  onApproveAll: () => void;
  onSelectWork: (work: AttributionRecord) => void;
  approvedIds: Set<string>;
}

function generateAgentSuggestions(work: AttributionRecord): AgentSuggestion[] {
  const suggestions: AgentSuggestion[] = [];

  if (work.confidence_score < 0.5) {
    suggestions.push({
      field: "assurance_level",
      current: work.assurance_level,
      suggested: "LEVEL_2",
      reason: "Cross-referencing MusicBrainz and Discogs confirms credit chain",
      confidence: 0.82,
    });
  }

  const uniqueSources = new Set(work.credits.flatMap((c) => c.sources));
  if (uniqueSources.size < 3) {
    suggestions.push({
      field: "sources",
      current: `${uniqueSources.size} source(s)`,
      suggested: "Add MusicBrainz cross-reference",
      reason: "Additional source corroboration improves confidence by ~15%",
      confidence: 0.75,
    });
  }

  if (work.credits.some((c) => c.confidence < 0.5)) {
    suggestions.push({
      field: "credit_confidence",
      current: "Some credits below 50%",
      suggested: "Request artist verification",
      reason: "Low-confidence credits benefit from A3 artist verification",
      confidence: 0.88,
    });
  }

  return suggestions;
}

export function AgentReviewQueue({
  works,
  onApprove,
  onApproveAll,
  onSelectWork,
  approvedIds,
}: AgentReviewQueueProps) {
  const [expandedId, setExpandedId] = useState<string | null>(null);
  const pendingWorks = works.filter((w) => !approvedIds.has(w.attribution_id));
  const approvedCount = approvedIds.size;

  return (
    <div>
      {/* Agent narration header */}
      <div className="mb-[var(--space-6)] flex items-center gap-[var(--space-3)] py-[var(--space-3)] border-b border-[var(--color-border)]">
        <div className="accent-square-sm" aria-hidden="true" />
        <p className="text-sm text-[var(--color-body)]">
          <span className="font-semibold text-[var(--color-heading)]">Agent:</span>{" "}
          {pendingWorks.length > 0
            ? `I've analyzed ${pendingWorks.length} attribution${pendingWorks.length !== 1 ? "s" : ""} and generated suggestions. Items are sorted by review priority.`
            : "All attributions have been reviewed. Great work!"}
        </p>
      </div>

      {/* Progress bar */}
      <div className="mb-[var(--space-4)] flex items-center gap-[var(--space-4)]">
        <div className="flex-1 h-px bg-[var(--color-border)] relative">
          <div
            className="h-px absolute top-0 left-0 transition-all duration-[var(--transition-slow)]"
            style={{
              width: works.length > 0 ? `${(approvedCount / works.length) * 100}%` : "0%",
              backgroundColor: "var(--color-confidence-high)",
            }}
          />
        </div>
        <span className="text-xs text-[var(--color-muted)] data-mono">
          {approvedCount}/{works.length}
        </span>
        {pendingWorks.length > 0 && (
          <button
            onClick={onApproveAll}
            className="editorial-caps text-xs text-[var(--color-heading)] underline underline-offset-4 decoration-[var(--color-accent)] decoration-2 hover:text-[var(--color-accent)] transition-colors duration-[var(--transition-fast)]"
          >
            Approve All
          </button>
        )}
      </div>

      {/* Review items */}
      <div className="divide-y divide-[var(--color-border)]">
        {pendingWorks.map((work, index) => {
          const suggestions = generateAgentSuggestions(work);
          const isExpanded = expandedId === work.attribution_id;

          return (
            <div key={work.attribution_id} className="py-[var(--space-5)]">
              <div className="flex items-start gap-[var(--space-4)]">
                {/* Roman numeral index */}
                <span className="editorial-caps text-xs text-[var(--color-muted)] w-8 pt-1 data-mono">
                  {toRoman(index + 1)}
                </span>

                <div className="flex items-center gap-[var(--space-3)]">
                  <ConfidenceGauge score={work.confidence_score} size="sm" showLabel={false} />
                </div>

                <div className="min-w-0 flex-1">
                  <button
                    onClick={() => onSelectWork(work)}
                    className="text-left"
                  >
                    <div className="flex items-center gap-[var(--space-3)]">
                      <h3 className="text-base font-semibold text-[var(--color-heading)] hover:text-[var(--color-accent)] transition-colors">
                        {work.work_title}
                      </h3>
                      <AssuranceBadge level={work.assurance_level} />
                    </div>
                  </button>
                  <p className="mt-[var(--space-1)] text-sm text-[var(--color-label)]">
                    {work.artist_name}
                  </p>

                  {/* Agent suggestions */}
                  {suggestions.length > 0 && (
                    <div className="mt-[var(--space-3)]">
                      <button
                        onClick={() => setExpandedId(isExpanded ? null : work.attribution_id)}
                        className="editorial-caps text-xs text-[var(--color-accent)] underline underline-offset-2"
                      >
                        {isExpanded ? "Hide" : `${suggestions.length} suggestion${suggestions.length !== 1 ? "s" : ""}`}
                      </button>

                      {isExpanded && (
                        <div className="mt-[var(--space-3)] space-y-[var(--space-3)]">
                          {suggestions.map((s, i) => (
                            <div
                              key={i}
                              className="pl-[var(--space-4)] border-l-2 border-[var(--color-accent-muted)]"
                            >
                              <div className="flex items-center gap-[var(--space-3)] text-sm">
                                <span className="text-[var(--color-confidence-low)] line-through">
                                  {s.current}
                                </span>
                                <span className="text-[var(--color-accent)]">&rarr;</span>
                                <span className="text-[var(--color-confidence-high)] font-medium">
                                  {s.suggested}
                                </span>
                                <span className="text-xs text-[var(--color-muted)] data-mono">
                                  ({Math.round(s.confidence * 100)}%)
                                </span>
                              </div>
                              <p className="mt-[var(--space-1)] text-xs text-[var(--color-label)]">
                                {s.reason}
                              </p>
                            </div>
                          ))}
                        </div>
                      )}
                    </div>
                  )}
                </div>

                <button
                  onClick={() => onApprove(work.attribution_id)}
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
    </div>
  );
}

function toRoman(num: number): string {
  const romans: [number, string][] = [
    [10, "X"], [9, "IX"], [5, "V"], [4, "IV"], [1, "I"],
  ];
  let result = "";
  let remaining = num;
  for (const [value, symbol] of romans) {
    while (remaining >= value) {
      result += symbol;
      remaining -= value;
    }
  }
  return result;
}
