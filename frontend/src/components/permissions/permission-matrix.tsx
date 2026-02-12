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
      <table className="w-full text-sm">
        <thead>
          <tr className="border-b border-border">
            <th className="py-3 pr-4 text-left editorial-caps text-xs text-label">
              Permission
            </th>
            <th className="py-3 px-4 text-left editorial-caps text-xs text-label">
              Status
            </th>
            <th className="py-3 px-4 text-left editorial-caps text-xs text-label">
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
                className="border-b border-divider"
              >
                <td className="py-3 pr-4 text-body">
                  {label}
                </td>
                <td className="py-3 px-4">
                  <span
                    className="inline-flex items-center gap-1 editorial-caps text-xs"
                    style={{ color: config.colorVar }}
                  >
                    <span
                      className="h-1.5 w-1.5"
                      style={{ backgroundColor: config.colorVar }}
                      aria-hidden="true"
                    />
                    {config.label}
                  </span>
                </td>
                <td className="py-3 px-4 text-muted text-xs">
                  {perm.attribution_requirement && (
                    <span>{perm.attribution_requirement}</span>
                  )}
                  {perm.royalty_rate !== null && (
                    <span className="data-mono">
                      Royalty: {(perm.royalty_rate * 100).toFixed(1)}%
                    </span>
                  )}
                  {perm.conditions.length > 0 &&
                    !perm.attribution_requirement &&
                    perm.royalty_rate === null && (
                      <span>
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
