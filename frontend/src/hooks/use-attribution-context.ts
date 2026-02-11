"use client";

import { useCopilotReadable } from "@copilotkit/react-core";
import { useAtomValue } from "jotai";
import { userRoleAtom } from "@/lib/stores/mode";
import type { AttributionRecord } from "@/lib/types/attribution";

/**
 * Feed selected work + user role to the CopilotKit agent context.
 * This enables the DuetUI bidirectional context loop — the agent
 * sees what the user is looking at and adapts its responses.
 */
export function useAttributionContext(selectedWork: AttributionRecord | null) {
  const role = useAtomValue(userRoleAtom);

  useCopilotReadable({
    description: "Current user role (artist or query)",
    value: role,
  });

  useCopilotReadable({
    description: "Currently selected attribution record",
    value: selectedWork
      ? {
          attribution_id: selectedWork.attribution_id,
          work_title: selectedWork.work_title,
          artist_name: selectedWork.artist_name,
          confidence_score: selectedWork.confidence_score,
          assurance_level: selectedWork.assurance_level,
          source_agreement: selectedWork.source_agreement,
          credits_count: selectedWork.credits.length,
          needs_review: selectedWork.needs_review,
          review_priority: selectedWork.review_priority,
        }
      : null,
  });
}
