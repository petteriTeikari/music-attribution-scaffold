"use client";

/**
 * AuraclesBadge — Sovereign digital identity indicator in sidebar.
 *
 * Shows "Au" monogram linking to /permissions. Artist-mode only,
 * same visibility pattern as NotificationBadge.
 */

import Link from "next/link";
import { useAtomValue } from "jotai";
import { userRoleAtom } from "@/lib/stores/mode";

export function AuraclesBadge() {
  const role = useAtomValue(userRoleAtom);

  if (role !== "artist") return null;

  return (
    <Link
      href="/permissions"
      className="group flex h-7 w-7 items-center justify-center rounded-full border transition-colors duration-150"
      style={{ borderColor: "var(--color-teal)" }}
      aria-label="Auracles identity — view permissions"
      onMouseEnter={(e) => {
        e.currentTarget.style.borderColor = "var(--color-accent)";
      }}
      onMouseLeave={(e) => {
        e.currentTarget.style.borderColor = "var(--color-teal)";
      }}
    >
      <span
        className="data-mono text-[9px] font-medium"
        style={{ color: "var(--color-teal)" }}
      >
        Au
      </span>
    </Link>
  );
}

export function AuraclesBadgeMobile() {
  const role = useAtomValue(userRoleAtom);

  if (role !== "artist") return null;

  return (
    <Link
      href="/permissions"
      className="flex items-center gap-2 py-2 text-label hover:text-heading transition-colors duration-150"
      aria-label="Auracles identity — view permissions"
    >
      <span
        className="flex h-5 w-5 items-center justify-center rounded-full border"
        style={{ borderColor: "var(--color-teal)" }}
      >
        <span
          className="data-mono text-[7px] font-medium"
          style={{ color: "var(--color-teal)" }}
        >
          Au
        </span>
      </span>
      <span className="text-xs">Auracles ID</span>
    </Link>
  );
}
