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
  /** Detailed reasoning with source references — shown in 3rd disclosure level */
  detail?: string;
  sourceRefs?: string[];
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
      detail:
        "MusicBrainz recording entry lists performer and songwriter credits with matching entity IDs. " +
        "Discogs master release corroborates the same credits with additional role details. " +
        "Combined source agreement (0.81) exceeds the A2 threshold.",
      sourceRefs: ["MusicBrainz recording", "Discogs master release"],
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
      detail:
        "The current attribution relies on a limited source set. Adding a MusicBrainz cross-reference " +
        "would provide independent verification, typically improving conformal coverage by 12-18%. " +
        "The MusicBrainz API rate limiter was not triggered in the last fetch cycle.",
      sourceRefs: ["MusicBrainz API", "Conformal prediction calibration set"],
    });
  }

  if (work.credits.some((c) => c.confidence < 0.5)) {
    suggestions.push({
      field: "credit_confidence",
      current: "Some credits below 50%",
      suggested: "Request artist verification",
      reason: "Low-confidence credits benefit from A3 artist verification",
      confidence: 0.88,
      detail:
        "Credits with confidence below 0.50 have prediction sets containing 3+ alternative roles, " +
        "indicating the model is uncertain about the exact attribution. Artist self-verification (A3) " +
        "would reduce the prediction set to the correct role and apply a Bayesian update.",
      sourceRefs: [
        "Conformal prediction set analysis",
        "A3 verification protocol",
      ],
    });
  }

  return suggestions;
}

type DisclosureLevel = "hidden" | "summary" | "detail";

export function AgentReviewQueue({
  works,
  onApprove,
  onApproveAll,
  onSelectWork,
  approvedIds,
}: AgentReviewQueueProps) {
  const [expandedId, setExpandedId] = useState<string | null>(null);
  const [detailSuggestionIdx, setDetailSuggestionIdx] = useState<number | null>(null);
  const pendingWorks = works.filter((w) => !approvedIds.has(w.attribution_id));
  const approvedCount = approvedIds.size;

  function getDisclosureLevel(workId: string, suggestionIdx: number): DisclosureLevel {
    if (expandedId !== workId) return "hidden";
    if (detailSuggestionIdx === suggestionIdx) return "detail";
    return "summary";
  }

  function handleToggleExpand(workId: string) {
    setExpandedId((prev) => {
      if (prev === workId) {
        setDetailSuggestionIdx(null);
        return null;
      }
      setDetailSuggestionIdx(null);
      return workId;
    });
  }

  function handleToggleDetail(suggestionIdx: number) {
    setDetailSuggestionIdx((prev) => (prev === suggestionIdx ? null : suggestionIdx));
  }

  return (
    <div>
      {/* Agent narration header */}
      <div className="mb-6 flex items-center gap-3 py-3 border-b border-border">
        <div className="accent-square-sm" aria-hidden="true" />
        <p className="text-sm text-body">
          <span className="font-semibold text-heading">Agent:</span>{" "}
          {pendingWorks.length > 0
            ? `I've analyzed ${pendingWorks.length} attribution${pendingWorks.length !== 1 ? "s" : ""} and generated suggestions. Items are sorted by review priority.`
            : "All attributions have been reviewed. Great work!"}
        </p>
      </div>

      {/* Progress bar */}
      <div className="mb-4 flex items-center gap-4">
        <div className="flex-1 h-px bg-border relative">
          <div
            className="h-px absolute top-0 left-0 transition-all duration-300"
            style={{
              width: works.length > 0 ? `${(approvedCount / works.length) * 100}%` : "0%",
              backgroundColor: "var(--color-confidence-high)",
            }}
          />
        </div>
        <span className="text-xs text-muted data-mono">
          {approvedCount}/{works.length}
        </span>
        {pendingWorks.length > 0 && (
          <button
            onClick={onApproveAll}
            className="editorial-caps text-xs text-heading underline underline-offset-4 decoration-accent decoration-2 hover:text-accent transition-colors duration-150"
          >
            Approve All
          </button>
        )}
      </div>

      {/* Review items */}
      <div className="divide-y divide-border">
        {pendingWorks.map((work, index) => {
          const suggestions = generateAgentSuggestions(work);
          const isExpanded = expandedId === work.attribution_id;

          return (
            <div key={work.attribution_id} className="py-5">
              <div className="flex items-start gap-4">
                {/* Roman numeral index */}
                <span className="editorial-caps text-xs text-muted w-8 pt-1 data-mono">
                  {toRoman(index + 1)}
                </span>

                <div className="flex items-center gap-3">
                  <ConfidenceGauge score={work.confidence_score} size="sm" showLabel={false} />
                </div>

                <div className="min-w-0 flex-1">
                  <button
                    onClick={() => onSelectWork(work)}
                    className="text-left"
                  >
                    <div className="flex items-center gap-3">
                      <h3 className="text-base font-semibold text-heading hover:text-accent transition-colors">
                        {work.work_title}
                      </h3>
                      <AssuranceBadge level={work.assurance_level} />
                    </div>
                  </button>
                  <p className="mt-1 text-sm text-label">
                    {work.artist_name}
                  </p>

                  {/* Agent suggestions — 3-level progressive disclosure */}
                  {suggestions.length > 0 && (
                    <div className="mt-3">
                      <button
                        onClick={() => handleToggleExpand(work.attribution_id)}
                        className="editorial-caps text-xs text-accent underline underline-offset-2"
                        aria-expanded={isExpanded}
                      >
                        {isExpanded ? "Hide" : `${suggestions.length} suggestion${suggestions.length !== 1 ? "s" : ""}`}
                      </button>

                      {isExpanded && (
                        <div className="mt-3 space-y-3">
                          {suggestions.map((s, i) => {
                            const level = getDisclosureLevel(work.attribution_id, i);
                            return (
                              <div
                                key={i}
                                className="pl-4 border-l-2 border-accent-muted"
                              >
                                {/* Level 2: Summary (diff view) */}
                                <div className="flex items-center gap-3 text-sm">
                                  <span className="text-confidence-low line-through">
                                    {s.current}
                                  </span>
                                  <span className="text-accent">&rarr;</span>
                                  <span className="text-confidence-high font-medium">
                                    {s.suggested}
                                  </span>
                                  <span className="text-xs text-muted data-mono">
                                    ({Math.round(s.confidence * 100)}%)
                                  </span>
                                </div>
                                <p className="mt-1 text-xs text-label">
                                  {s.reason}
                                </p>

                                {/* Level 3: Detail toggle */}
                                {s.detail && (
                                  <div className="mt-1">
                                    <button
                                      onClick={() => handleToggleDetail(i)}
                                      className="text-xs text-muted underline underline-offset-2 hover:text-heading"
                                      aria-expanded={level === "detail"}
                                    >
                                      {level === "detail" ? "Hide detail" : "Why?"}
                                    </button>

                                    {level === "detail" && (
                                      <div className="mt-2 pl-3 border-l border-border">
                                        <p className="text-xs text-body leading-relaxed">
                                          {s.detail}
                                        </p>
                                        {s.sourceRefs && s.sourceRefs.length > 0 && (
                                          <div className="mt-1.5 flex flex-wrap gap-1.5">
                                            {s.sourceRefs.map((ref, ri) => (
                                              <span
                                                key={ri}
                                                className="text-xs text-muted bg-surface-secondary px-1.5 py-0.5"
                                              >
                                                {ref}
                                              </span>
                                            ))}
                                          </div>
                                        )}
                                      </div>
                                    )}
                                  </div>
                                )}
                              </div>
                            );
                          })}
                        </div>
                      )}
                    </div>
                  )}
                </div>

                <button
                  onClick={() => onApprove(work.attribution_id)}
                  className="flex-shrink-0 editorial-caps text-xs border-b-2 border-confidence-high pb-1 transition-colors duration-150 hover:text-confidence-high"
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
