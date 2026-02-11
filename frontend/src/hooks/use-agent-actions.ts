"use client";

import { useCopilotAction } from "@copilotkit/react-core";

interface UseAgentActionsOptions {
  onNavigateToWork?: (workId: string) => void;
  onHighlightCredit?: (entityId: string) => void;
  onOpenFeedbackPanel?: (workId: string) => void;
  onShowCorrectionDiff?: (field: string, current: string, suggested: string) => void;
}

/**
 * Register CopilotKit actions that the agent can invoke to manipulate the UI.
 * This is the agent→UI direction of the DuetUI bidirectional context loop.
 */
export function useAgentActions(options: UseAgentActionsOptions = {}) {
  useCopilotAction({
    name: "navigate_to_work",
    description: "Navigate the UI to show a specific attribution record",
    parameters: [
      {
        name: "workId",
        type: "string",
        description: "Attribution ID to navigate to",
        required: true,
      },
    ],
    handler: async ({ workId }: { workId: string }) => {
      options.onNavigateToWork?.(workId);
      return `Navigated to work ${workId}`;
    },
  });

  useCopilotAction({
    name: "highlight_credit",
    description: "Highlight a specific credit entity in the UI",
    parameters: [
      {
        name: "entityId",
        type: "string",
        description: "Entity ID to highlight",
        required: true,
      },
    ],
    handler: async ({ entityId }: { entityId: string }) => {
      options.onHighlightCredit?.(entityId);
      return `Highlighted entity ${entityId}`;
    },
  });

  useCopilotAction({
    name: "open_feedback_panel",
    description: "Open the feedback panel for a specific attribution",
    parameters: [
      {
        name: "workId",
        type: "string",
        description: "Attribution ID to open feedback for",
        required: true,
      },
    ],
    handler: async ({ workId }: { workId: string }) => {
      options.onOpenFeedbackPanel?.(workId);
      return `Opened feedback panel for ${workId}`;
    },
  });

  useCopilotAction({
    name: "show_correction_diff",
    description: "Show a before/after correction diff in the UI",
    parameters: [
      {
        name: "field",
        type: "string",
        description: "Field being corrected",
        required: true,
      },
      {
        name: "current",
        type: "string",
        description: "Current value",
        required: true,
      },
      {
        name: "suggested",
        type: "string",
        description: "Suggested new value",
        required: true,
      },
    ],
    handler: async ({
      field,
      current,
      suggested,
    }: {
      field: string;
      current: string;
      suggested: string;
    }) => {
      options.onShowCorrectionDiff?.(field, current, suggested);
      return `Showing diff: ${field} "${current}" → "${suggested}"`;
    },
  });
}
