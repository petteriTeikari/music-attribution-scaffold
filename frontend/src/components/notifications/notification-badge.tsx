"use client";

import { useState, useRef } from "react";
import { useAtomValue } from "jotai";
import { userRoleAtom } from "@/lib/stores/mode";
import { MOCK_NOTIFICATIONS } from "@/lib/data/mock-notifications";

export function NotificationBadge() {
  const role = useAtomValue(userRoleAtom);
  const [isOpen, setIsOpen] = useState(false);
  const [notifications] = useState(MOCK_NOTIFICATIONS);
  const containerRef = useRef<HTMLDivElement>(null);

  if (role !== "artist") return null;

  const unreadCount = notifications.filter((n) => !n.read).length;

  return (
    <div className="relative" ref={containerRef}>
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="relative flex h-6 w-6 items-center justify-center text-label hover:text-heading transition-colors"
        aria-label={`Notifications (${unreadCount} unread)`}
        aria-expanded={isOpen}
        aria-haspopup="true"
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
        <div
          role="menu"
          className="absolute left-full top-0 ml-2 w-72 border border-border bg-surface-elevated z-50"
        >
          <div className="p-3 border-b border-divider">
            <h3 className="editorial-caps text-xs text-heading">
              Notifications
            </h3>
          </div>
          <div className="max-h-80 overflow-y-auto">
            {notifications.map((notif) => (
              <div
                key={notif.id}
                className={`p-3 border-b border-divider last:border-0 ${
                  !notif.read
                    ? "border-l-2 border-l-accent"
                    : ""
                }`}
              >
                <p className="text-sm font-medium text-heading">
                  {notif.title}
                </p>
                <p className="mt-1 text-xs text-muted">
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
