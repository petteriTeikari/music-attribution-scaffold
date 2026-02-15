"use client";

import { useEffect, useState, useCallback } from "react";
import dynamic from "next/dynamic";
import { useAtomValue } from "jotai";
import { useRouter } from "next/navigation";
import { userRoleAtom } from "@/lib/stores/mode";
import type { AttributionRecord } from "@/lib/types/attribution";
import { apiClient } from "@/lib/api/api-client";
import { AgentReviewQueue } from "@/components/review/agent-review-queue";
import { AdaptiveTooltip } from "@/components/ui/adaptive-tooltip";
import type { FeedbackData } from "@/components/feedback/agent-feedback-flow";
import { useAttributionContext } from "@/hooks/use-attribution-context";
import { useAgentActions } from "@/hooks/use-agent-actions";

const AgentFeedbackFlow = dynamic(
  () => import("@/components/feedback/agent-feedback-flow").then((mod) => ({ default: mod.AgentFeedbackFlow })),
  { ssr: false },
);

export default function ReviewPage() {
  const role = useAtomValue(userRoleAtom);
  const router = useRouter();
  const [works, setWorks] = useState<AttributionRecord[]>([]);
  const [loading, setLoading] = useState(true);
  const [approvedIds, setApprovedIds] = useState<Set<string>>(new Set());
  const [selectedWork, setSelectedWork] = useState<AttributionRecord | null>(null);
  const [feedbackWorkId, setFeedbackWorkId] = useState<string | null>(null);

  // Feed context to CopilotKit agent
  useAttributionContext(selectedWork);

  // Wire agent actions to real UI effects
  const handleNavigateToWork = useCallback(
    (workId: string) => router.push(`/works/${workId}`),
    [router]
  );
  const handleHighlightCredit = useCallback(
    (entityId: string) => {
      const el = document.querySelector(`[data-entity-id="${entityId}"]`);
      el?.scrollIntoView({ behavior: "smooth", block: "center" });
      el?.classList.add("ring-2", "ring-accent");
      setTimeout(() => el?.classList.remove("ring-2", "ring-accent"), 3000);
    },
    []
  );
  useAgentActions({
    onNavigateToWork: handleNavigateToWork,
    onHighlightCredit: handleHighlightCredit,
    onOpenFeedbackPanel: setFeedbackWorkId,
  });

  useEffect(() => {
    apiClient.getWorks().then((data) => {
      setWorks(data.filter((w) => w.needs_review).sort((a, b) => b.review_priority - a.review_priority));
      setLoading(false);
    });
  }, []);

  const pendingWorks = works.filter((w) => !approvedIds.has(w.attribution_id));
  const approvedCount = approvedIds.size;

  function handleApprove(id: string) {
    setApprovedIds((prev) => { const next = new Set(prev); next.add(id); return next; });
  }

  function handleApproveAll() {
    setApprovedIds(new Set(works.map((w) => w.attribution_id)));
  }

  function handleFeedbackSubmit(feedback: FeedbackData) {
    // After structured feedback, close panel
    setFeedbackWorkId(null);
    // Mark as reviewed
    handleApprove(feedback.workId);
  }

  const feedbackWork = feedbackWorkId
    ? works.find((w) => w.attribution_id === feedbackWorkId) ?? null
    : null;

  if (role !== "artist") {
    return (
      <div className="px-8 py-10">
        <div className="py-20 text-center">
          <h2 className="editorial-display text-2xl text-heading">
            Artist Mode Required
          </h2>
          <p className="mt-2 text-label">
            Switch to Artist mode to access the review queue.
          </p>
        </div>
      </div>
    );
  }

  return (
    <div className="px-8 py-10">
      {/* Header */}
      <div className="mb-8">
        <span className="editorial-caps text-xs text-accent block mb-2">
          Review
        </span>
        <AdaptiveTooltip
          id="review-queue-intro"
          skill="review"
          content="The review queue shows attributions needing human verification. The agent generates suggestions you can approve, reject, or expand for detailed reasoning. Items are sorted by review priority."
          compactContent="Agent suggestions sorted by priority."
          placement="right"
        >
          <h1 className="editorial-display text-4xl text-heading">
            Review Queue
          </h1>
        </AdaptiveTooltip>
        <p className="mt-2 text-label">
          Agent-assisted attribution review with AI-generated suggestions.
        </p>
      </div>

      {/* Feedback flow panel */}
      {feedbackWork && (
        <div className="mb-8 border border-border p-6">
          <AgentFeedbackFlow
            work={feedbackWork}
            onSubmit={handleFeedbackSubmit}
            onCancel={() => setFeedbackWorkId(null)}
          />
        </div>
      )}

      {loading ? (
        <div className="space-y-4">
          {Array.from({ length: 3 }).map((_, i) => (
            <div
              key={i}
              className="h-32 animate-pulse bg-surface-secondary"
            />
          ))}
        </div>
      ) : pendingWorks.length === 0 && approvedCount > 0 ? (
        <div className="py-20 text-center">
          <p className="editorial-display text-2xl text-confidence-high">
            All caught up
          </p>
          <p className="mt-2 text-label">
            {approvedCount} attribution{approvedCount !== 1 ? "s" : ""} reviewed.
          </p>
        </div>
      ) : (
        <AgentReviewQueue
          works={works}
          onApprove={handleApprove}
          onApproveAll={handleApproveAll}
          onSelectWork={setSelectedWork}
          approvedIds={approvedIds}
        />
      )}
    </div>
  );
}
