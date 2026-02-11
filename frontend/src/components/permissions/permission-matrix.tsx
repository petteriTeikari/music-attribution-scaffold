"use client";

import type { PermissionEntry } from "@/lib/types/permissions";

const PERMISSION_LABELS: Record<string, string> = {
  STREAM: "Stream",
  DOWNLOAD: "Download",
  SYNC_LICENSE: "Sync License",
  AI_TRAINING: "AI Training",
  VOICE_CLONING: "Voice Cloning",
  STYLE_LEARNING: "Style Learning",
  LYRICS_IN_CHATBOTS: "Lyrics in Chatbots",
  COVER_VERSIONS: "Cover Versions",
  REMIX: "Remix",
  SAMPLE: "Sample",
  DERIVATIVE_WORK: "Derivative Work",
};

const VALUE_CONFIG: Record<
  string,
  { label: string; colorVar: string }
> = {
  ALLOW: { label: "Allow", colorVar: "var(--color-permission-allow)" },
  DENY: { label: "Deny", colorVar: "var(--color-permission-deny)" },
  ASK: { label: "Ask", colorVar: "var(--color-permission-ask)" },
  ALLOW_WITH_ATTRIBUTION: {
    label: "Allow + Credit",
    colorVar: "var(--color-permission-allow)",
  },
  ALLOW_WITH_ROYALTY: {
    label: "Allow + Royalty",
    colorVar: "var(--color-permission-allow)",
  },
};

interface PermissionMatrixProps {
  permissions: PermissionEntry[];
  onToggle?: (permType: string, newValue: string) => void;
  readonly?: boolean;
}

export function PermissionMatrix({
  permissions,
  readonly = false,
}: PermissionMatrixProps) {
  return (
    <div className="overflow-x-auto">
      <table className="w-full text-[var(--text-sm)]">
        <thead>
          <tr className="border-b border-[var(--color-border)]">
            <th className="py-[var(--space-3)] pr-[var(--space-4)] text-left font-semibold text-[var(--color-heading)]">
              Permission
            </th>
            <th className="py-[var(--space-3)] px-[var(--space-4)] text-left font-semibold text-[var(--color-heading)]">
              Status
            </th>
            <th className="py-[var(--space-3)] px-[var(--space-4)] text-left font-semibold text-[var(--color-heading)]">
              Details
            </th>
          </tr>
        </thead>
        <tbody>
          {permissions.map((perm) => {
            const config = VALUE_CONFIG[perm.value] ?? {
              label: perm.value,
              colorVar: "var(--color-muted)",
            };
            const label = PERMISSION_LABELS[perm.permission_type] ?? perm.permission_type;

            return (
              <tr
                key={perm.permission_type}
                className="border-b border-[var(--color-divider)]"
              >
                <td className="py-[var(--space-3)] pr-[var(--space-4)] text-[var(--color-body)]">
                  {label}
                </td>
                <td className="py-[var(--space-3)] px-[var(--space-4)]">
                  <span
                    className="inline-flex items-center gap-[var(--space-1)] rounded-[var(--radius-full)] px-[var(--space-3)] py-[var(--space-1)] text-[var(--text-xs)] font-medium"
                    style={{
                      backgroundColor: `color-mix(in srgb, ${config.colorVar} 12%, transparent)`,
                      color: config.colorVar,
                    }}
                  >
                    <span
                      className="h-1.5 w-1.5 rounded-full"
                      style={{ backgroundColor: config.colorVar }}
                      aria-hidden="true"
                    />
                    {config.label}
                  </span>
                </td>
                <td className="py-[var(--space-3)] px-[var(--space-4)] text-[var(--color-muted)]">
                  {perm.attribution_requirement && (
                    <span className="text-[var(--text-xs)]">
                      {perm.attribution_requirement}
                    </span>
                  )}
                  {perm.royalty_rate !== null && (
                    <span className="text-[var(--text-xs)]">
                      Royalty: {(perm.royalty_rate * 100).toFixed(1)}%
                    </span>
                  )}
                  {perm.conditions.length > 0 &&
                    !perm.attribution_requirement &&
                    perm.royalty_rate === null && (
                      <span className="text-[var(--text-xs)]">
                        {perm.conditions.map((c) => c.condition_type.replace(/_/g, " ")).join(", ")}
                      </span>
                    )}
                </td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
}
