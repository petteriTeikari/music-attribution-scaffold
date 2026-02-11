"use client";

import { useState } from "react";
import type { AuditLogEntry } from "@/lib/types/permissions";

const REQUESTER_TYPE_LABELS: Record<string, string> = {
  ai_platform: "AI Platform",
  rights_org: "Rights Org",
  individual: "Individual",
};

function formatTimestamp(iso: string): string {
  const date = new Date(iso);
  return date.toLocaleDateString("en-US", {
    month: "short",
    day: "numeric",
    hour: "2-digit",
    minute: "2-digit",
  });
}

function getResultColorVar(result: string): string {
  if (result === "DENY") return "var(--color-permission-deny)";
  if (result === "ASK") return "var(--color-permission-ask)";
  return "var(--color-permission-allow)";
}

interface AuditLogProps {
  entries: AuditLogEntry[];
}

export function AuditLog({ entries }: AuditLogProps) {
  const [filter, setFilter] = useState<string>("all");

  const filtered =
    filter === "all"
      ? entries
      : entries.filter((e) => e.requester_type === filter);

  return (
    <div>
      {/* Filter controls — editorial underline tabs */}
      <div className="mb-[var(--space-4)] flex items-center gap-[var(--space-4)]">
        <span className="editorial-caps text-xs text-[var(--color-label)]">
          Filter:
        </span>
        {["all", "ai_platform", "rights_org", "individual"].map((type) => (
          <button
            key={type}
            onClick={() => setFilter(type)}
            className={`editorial-caps text-xs pb-[var(--space-1)] transition-colors duration-[var(--transition-fast)] border-b-2 ${
              filter === type
                ? "border-[var(--color-accent)] text-[var(--color-heading)]"
                : "border-transparent text-[var(--color-label)] hover:text-[var(--color-heading)]"
            }`}
          >
            {type === "all" ? "All" : REQUESTER_TYPE_LABELS[type] ?? type}
          </button>
        ))}
      </div>

      {/* Log entries */}
      <div className="divide-y divide-[var(--color-divider)]">
        {filtered.map((entry) => {
          const color = getResultColorVar(entry.result);
          return (
            <div
              key={entry.id}
              className="flex items-start gap-[var(--space-3)] py-[var(--space-3)]"
            >
              {/* Result indicator — square */}
              <span
                className="mt-[var(--space-1)] h-2 w-2 flex-shrink-0"
                style={{ backgroundColor: color }}
                aria-hidden="true"
              />

              <div className="min-w-0 flex-1">
                <div className="flex items-center gap-[var(--space-2)]">
                  <span className="font-medium text-[var(--color-heading)] text-sm">
                    {entry.requester_name}
                  </span>
                  <span
                    className="editorial-caps text-xs"
                    style={{ color }}
                  >
                    {entry.result.replace(/_/g, " ")}
                  </span>
                </div>
                <p className="mt-[var(--space-1)] text-xs text-[var(--color-label)]">
                  {entry.permission_type.replace(/_/g, " ")}
                  {entry.work_title && ` — "${entry.work_title}"`}
                </p>
                <p className="mt-[var(--space-1)] text-xs text-[var(--color-muted)]">
                  {entry.reason}
                </p>
              </div>

              <span className="flex-shrink-0 text-xs text-[var(--color-muted)] whitespace-nowrap data-mono">
                {formatTimestamp(entry.timestamp)}
              </span>
            </div>
          );
        })}
      </div>
    </div>
  );
}
