"use client";

import { useState } from "react";
import type { AuditLogEntry } from "@/lib/types/permissions";
import { PlatformBadge } from "@/components/ui/platform-badge";
import { formatDateTime } from "@/lib/utils/format";

const FILTER_TABS = [
  { key: "all", label: "All" },
  { key: "ai_generator", label: "AI Generators" },
  { key: "llm_provider", label: "LLM Providers" },
  { key: "attribution_infra", label: "Attribution" },
  { key: "certification_body", label: "Certification" },
  { key: "rights_org", label: "Rights Orgs" },
  { key: "individual", label: "Individual" },
] as const;

const formatTimestamp = formatDateTime;

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
      <div className="mb-4 flex items-center gap-4 overflow-x-auto">
        <span className="editorial-caps text-xs text-label flex-shrink-0">
          Filter:
        </span>
        {FILTER_TABS.map(({ key, label }) => (
          <button
            key={key}
            onClick={() => setFilter(key)}
            className={`editorial-caps text-xs pb-1 transition-colors duration-150 border-b-2 whitespace-nowrap ${
              filter === key
                ? "border-accent text-heading"
                : "border-transparent text-label hover:text-heading"
            }`}
          >
            {label}
          </button>
        ))}
      </div>

      {/* Log entries */}
      <div className="divide-y divide-divider">
        {filtered.map((entry) => {
          const color = getResultColorVar(entry.result);
          return (
            <div
              key={entry.id}
              className="flex items-start gap-3 py-3"
            >
              {/* Result indicator — square */}
              <span
                className="mt-1 h-2 w-2 flex-shrink-0"
                style={{ backgroundColor: color }}
                aria-hidden="true"
              />

              <div className="min-w-0 flex-1">
                <div className="flex items-center gap-2">
                  <span className="font-medium text-heading text-sm">
                    {entry.requester_name}
                  </span>
                  <PlatformBadge type={entry.requester_type} />
                  <span
                    className="editorial-caps text-xs"
                    style={{ color }}
                  >
                    {entry.result.replace(/_/g, " ")}
                  </span>
                </div>
                <p className="mt-1 text-xs text-label">
                  {entry.permission_type.replace(/_/g, " ")}
                  {entry.work_title && ` — "${entry.work_title}"`}
                </p>
                <p className="mt-1 text-xs text-muted">
                  {entry.reason}
                </p>
              </div>

              <span className="flex-shrink-0 text-xs text-muted whitespace-nowrap data-mono">
                {formatTimestamp(entry.timestamp)}
              </span>
            </div>
          );
        })}
      </div>
    </div>
  );
}
