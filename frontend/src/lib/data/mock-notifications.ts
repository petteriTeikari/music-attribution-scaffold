/**
 * Mock notification data for the artist notification dropdown.
 *
 * Demonstrates the breadth of ecosystem interactions: attribution reviews,
 * permission requests, settlement compliance, royalty payments, and
 * certification audits.
 */

export interface Notification {
  id: string;
  type: "review" | "feedback" | "permission" | "royalty" | "compliance";
  title: string;
  description: string;
  timestamp: string;
  read: boolean;
}

export const MOCK_NOTIFICATIONS: Notification[] = [
  {
    id: "notif-1",
    type: "review",
    title: "3 attributions need review",
    description: "Headlock, Just for Now, and 2-1 have conflicting data",
    timestamp: "2026-02-10T14:00:00Z",
    read: false,
  },
  {
    id: "notif-2",
    type: "permission",
    title: "Suno AI requested style learning access",
    description:
      "Post-settlement verified partner — requires case-by-case approval",
    timestamp: "2026-02-09T10:00:00Z",
    read: false,
  },
  {
    id: "notif-3",
    type: "compliance",
    title: "Udio settlement compliance verified",
    description:
      "Recording-level training access restricted per settlement terms",
    timestamp: "2026-02-08T16:00:00Z",
    read: false,
  },
  {
    id: "notif-4",
    type: "royalty",
    title: "Jen/Futureverse voice model royalty received",
    description:
      "StyleFilter AI models — 70% revenue share via Auracles processed",
    timestamp: "2026-02-07T11:00:00Z",
    read: true,
  },
  {
    id: "notif-5",
    type: "permission",
    title: "Musical AI attribution query processed",
    description:
      "Fairly Trained certified platform — catalog indexed for attribution tracking",
    timestamp: "2026-02-06T09:00:00Z",
    read: true,
  },
  {
    id: "notif-6",
    type: "compliance",
    title: "Fairly Trained certification audit scheduled",
    description:
      "Dataset inclusion audit for Q1 2026 — catalog eligibility confirmed",
    timestamp: "2026-02-05T15:00:00Z",
    read: true,
  },
];
