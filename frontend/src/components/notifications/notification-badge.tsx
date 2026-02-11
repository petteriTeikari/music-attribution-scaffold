"use client";

import { useState } from "react";
import { useAtomValue } from "jotai";
import { userRoleAtom } from "@/lib/stores/mode";

interface Notification {
  id: string;
  type: "review" | "feedback" | "permission";
  title: string;
  description: string;
  timestamp: string;
  read: boolean;
}

const MOCK_NOTIFICATIONS: Notification[] = [
  {
    id: "notif-1",
    type: "review",
    title: "3 attributions need review",
    description: "Headlock, Just for Now, and 2-1 have conflicting data",
    timestamp: "2025-02-10T14:00:00Z",
    read: false,
  },
  {
    id: "notif-2",
    type: "permission",
    title: "New permission request",
    description: "Suno AI requested style learning access",
    timestamp: "2025-02-09T10:00:00Z",
    read: false,
  },
  {
    id: "notif-3",
    type: "feedback",
    title: "Feedback processed",
    description: "Your correction on Goodnight and Go was applied",
    timestamp: "2025-02-08T16:00:00Z",
    read: true,
  },
];

export function NotificationBadge() {
  const role = useAtomValue(userRoleAtom);
  const [isOpen, setIsOpen] = useState(false);
  const [notifications] = useState(MOCK_NOTIFICATIONS);

  if (role !== "artist") return null;

  const unreadCount = notifications.filter((n) => !n.read).length;

  return (
    <div className="relative">
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="relative rounded-[var(--radius-md)] border border-[var(--color-border)] p-[var(--space-2)] text-[var(--color-label)] hover:bg-[var(--color-surface-secondary)] transition-colors"
        aria-label={`Notifications (${unreadCount} unread)`}
      >
        <svg
          width="16"
          height="16"
          viewBox="0 0 16 16"
          fill="none"
          aria-hidden="true"
        >
          <path
            d="M8 1a4 4 0 0 0-4 4v2.5L2.5 10v1h11v-1L12 7.5V5a4 4 0 0 0-4-4ZM6.5 12a1.5 1.5 0 0 0 3 0"
            stroke="currentColor"
            strokeWidth="1.2"
          />
        </svg>
        {unreadCount > 0 && (
          <span
            className="absolute -right-1 -top-1 flex h-4 w-4 items-center justify-center rounded-full text-[10px] font-bold text-white"
            style={{ backgroundColor: "var(--color-confidence-low)" }}
          >
            {unreadCount}
          </span>
        )}
      </button>

      {/* Dropdown */}
      {isOpen && (
        <div className="absolute right-0 top-full mt-[var(--space-2)] w-80 rounded-[var(--radius-lg)] border border-[var(--color-border)] bg-[var(--color-surface-elevated)] shadow-[var(--shadow-lg)] z-50">
          <div className="p-[var(--space-3)] border-b border-[var(--color-divider)]">
            <h3 className="text-[var(--text-sm)] font-semibold text-[var(--color-heading)]">
              Notifications
            </h3>
          </div>
          <div className="max-h-80 overflow-y-auto">
            {notifications.map((notif) => (
              <div
                key={notif.id}
                className={`p-[var(--space-3)] border-b border-[var(--color-divider)] last:border-0 ${
                  !notif.read
                    ? "bg-[var(--color-primary-muted)]"
                    : ""
                }`}
              >
                <p className="text-[var(--text-sm)] font-medium text-[var(--color-heading)]">
                  {notif.title}
                </p>
                <p className="mt-[var(--space-1)] text-[var(--text-xs)] text-[var(--color-muted)]">
                  {notif.description}
                </p>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
