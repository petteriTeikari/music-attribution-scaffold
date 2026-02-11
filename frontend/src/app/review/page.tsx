"use client";

import { useEffect, useState, useCallback } from "react";
import { useAtomValue } from "jotai";
import { useRouter } from "next/navigation";
import { userRoleAtom } from "@/lib/stores/mode";
import type { AttributionRecord } from "@/lib/types/attribution";
import { apiClient } from "@/lib/api/api-client";
import { AgentReviewQueue } from "@/components/review/agent-review-queue";
import { AgentFeedbackFlow, type FeedbackData } from "@/components/feedback/agent-feedback-flow";
import { useAttributionContext } from "@/hooks/use-attribution-context";
import { useAgentActions } from "@/hooks/use-agent-actions";

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
      el?.classList.add("ring-2", "ring-[var(--color-accent)]");
      setTimeout(() => el?.classList.remove("ring-2", "ring-[var(--color-accent)]"), 3000);
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
    setApprovedIds((prev) => new Set([...prev, id]));
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
      <div className="mb-[var(--space-8)]">
        <span className="editorial-caps text-xs text-[var(--color-accent)] block mb-[var(--space-2)]">
          Review
        </span>
        <h1 className="editorial-display text-4xl text-[var(--color-heading)]">
          Review Queue
        </h1>
        <p className="mt-[var(--space-2)] text-[var(--color-label)]">
          Agent-assisted attribution review with AI-generated suggestions.
        </p>
      </div>

      {/* Feedback flow panel */}
      {feedbackWork && (
        <div className="mb-[var(--space-8)] border border-[var(--color-border)] p-[var(--space-6)]">
          <AgentFeedbackFlow
            work={feedbackWork}
            onSubmit={handleFeedbackSubmit}
            onCancel={() => setFeedbackWorkId(null)}
          />
        </div>
      )}

      {loading ? (
        <div className="space-y-[var(--space-4)]">
          {Array.from({ length: 3 }).map((_, i) => (
            <div
              key={i}
              className="h-32 animate-pulse bg-[var(--color-surface-secondary)]"
            />
          ))}
        </div>
      ) : pendingWorks.length === 0 && approvedCount > 0 ? (
        <div className="py-[var(--space-20)] text-center">
          <p className="editorial-display text-2xl text-[var(--color-confidence-high)]">
            All caught up
          </p>
          <p className="mt-[var(--space-2)] text-[var(--color-label)]">
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
