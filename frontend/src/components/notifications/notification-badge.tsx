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
        className="relative flex h-6 w-6 items-center justify-center text-[var(--color-label)] hover:text-[var(--color-heading)] transition-colors"
        aria-label={`Notifications (${unreadCount} unread)`}
      >
        <svg
          width="14"
          height="14"
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
            className="absolute -right-0.5 -top-0.5 flex h-3 w-3 items-center justify-center text-[8px] font-bold text-white"
            style={{ backgroundColor: "var(--color-accent)" }}
          >
            {unreadCount}
          </span>
        )}
      </button>

      {/* Dropdown */}
      {isOpen && (
        <div className="absolute left-full top-0 ml-[var(--space-2)] w-72 border border-[var(--color-border)] bg-[var(--color-surface-elevated)] shadow-[var(--shadow-lg)] z-50">
          <div className="p-[var(--space-3)] border-b border-[var(--color-divider)]">
            <h3 className="editorial-caps text-xs text-[var(--color-heading)]">
              Notifications
            </h3>
          </div>
          <div className="max-h-80 overflow-y-auto">
            {notifications.map((notif) => (
              <div
                key={notif.id}
                className={`p-[var(--space-3)] border-b border-[var(--color-divider)] last:border-0 ${
                  !notif.read
                    ? "border-l-2 border-l-[var(--color-accent)]"
                    : ""
                }`}
              >
                <p className="text-sm font-medium text-[var(--color-heading)]">
                  {notif.title}
                </p>
                <p className="mt-[var(--space-1)] text-xs text-[var(--color-muted)]">
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
