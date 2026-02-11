/**
 * Typed PostHog event schema for music attribution analytics.
 *
 * All events are no-ops when PostHog is not initialized (env vars missing).
 */

import { posthog } from "./posthog-provider";

// Event name constants
export const EVENTS = {
  REVIEW_APPROVED: "review_approved",
  REVIEW_BATCH_APPROVED: "review_batch_approved",
  AGENT_SUGGESTION_ACCEPTED: "agent_suggestion_accepted",
  AGENT_SUGGESTION_REJECTED: "agent_suggestion_rejected",
  AGENT_CHAT_OPENED: "agent_chat_opened",
  AGENT_CHAT_CLOSED: "agent_chat_closed",
  AGENT_MESSAGE_SENT: "agent_message_sent",
  TOOLTIP_SHOWN: "tooltip_shown",
  TOOLTIP_DISMISSED: "tooltip_dismissed",
  FEEDBACK_SUBMITTED: "feedback_submitted",
  CONFIDENCE_EXPLAINED: "confidence_explained",
  WORK_SELECTED: "work_selected",
  PROFICIENCY_LEVEL_CHANGED: "proficiency_level_changed",
} as const;

export type EventName = (typeof EVENTS)[keyof typeof EVENTS];

interface EventProperties {
  review_approved: { attribution_id: string; confidence_score: number };
  review_batch_approved: { count: number };
  agent_suggestion_accepted: { attribution_id: string; field: string };
  agent_suggestion_rejected: { attribution_id: string; field: string };
  agent_chat_opened: Record<string, never>;
  agent_chat_closed: { messages_exchanged: number };
  agent_message_sent: { message_length: number };
  tooltip_shown: { tooltip_id: string; skill: string };
  tooltip_dismissed: { tooltip_id: string; skill: string };
  feedback_submitted: { attribution_id: string; overall_assessment: number; center_bias: boolean };
  confidence_explained: { attribution_id: string; confidence_score: number };
  work_selected: { attribution_id: string };
  proficiency_level_changed: { skill: string; old_level: string; new_level: string };
}

/**
 * Track a typed PostHog event. No-op when PostHog not initialized.
 */
export function trackEvent<E extends EventName>(
  event: E,
  properties: EventProperties[E],
): void {
  try {
    posthog.capture(event, properties as Record<string, unknown>);
  } catch {
    // PostHog not initialized — graceful no-op
  }
}
