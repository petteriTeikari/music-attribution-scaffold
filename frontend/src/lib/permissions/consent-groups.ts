/**
 * Groups the 14-entry permission model into 3 consent categories
 * and extracts per-platform exceptions from conditions.
 *
 * Pure utility — no React dependencies.
 */

import type { PermissionEntry } from "@/lib/types/permissions";
import type { PermissionType } from "@/lib/types/enums";
import { getPlatform } from "@/lib/data/ecosystem-platforms";

/** Roman-numeral labels for groups. */
const ROMAN = ["I", "II", "III"] as const;

/** Permission types belonging to each consent group. */
const AI_GENERATION_TYPES: PermissionType[] = [
  "AI_TRAINING",
  "AI_TRAINING_COMPOSITION",
  "AI_TRAINING_RECORDING",
  "AI_TRAINING_STYLE",
  "VOICE_CLONING",
  "STYLE_LEARNING",
  "LYRICS_IN_CHATBOTS",
  "DATASET_INCLUSION",
];

const DISTRIBUTION_TYPES: PermissionType[] = [
  "STREAM",
  "DOWNLOAD",
  "SYNC_LICENSE",
  "COVER_VERSIONS",
];

const CREATIVE_TYPES: PermissionType[] = [
  "REMIX",
  "SAMPLE",
  "DERIVATIVE_WORK",
];

export interface ConsentException {
  permissionType: PermissionType;
  baseValue: string;
  platformId: string;
  platformName: string;
}

export interface ConsentGroupCounts {
  allow: number;
  ask: number;
  deny: number;
}

export interface ConsentGroup {
  roman: (typeof ROMAN)[number];
  label: string;
  tooltip: string;
  entries: PermissionEntry[];
  counts: ConsentGroupCounts;
  exceptions: ConsentException[];
}

const GROUP_TOOLTIPS: Record<string, string> = {
  "AI & GENERATION":
    "Manage training permissions via MCP queries and API. Auracles consent infrastructure enables per-platform overrides — e.g. Voice Cloning denied by default but allowed for authorized partners like Jen (Futureverse).",
  "DISTRIBUTION & LICENSING":
    "Standard royalty and sync terms. Connected platforms like SoundCloud inherit these settings automatically through the Auracles integration.",
  "CREATIVE DERIVATIVES":
    "Case-by-case approvals routed through the delegation chain. Remix, sample, and derivative requests go to management for review.",
};

function isAllowValue(value: string): boolean {
  return value === "ALLOW" || value === "ALLOW_WITH_ATTRIBUTION" || value === "ALLOW_WITH_ROYALTY";
}

function countValues(entries: PermissionEntry[]): ConsentGroupCounts {
  let allow = 0;
  let ask = 0;
  let deny = 0;
  for (const e of entries) {
    if (isAllowValue(e.value)) allow++;
    else if (e.value === "ASK") ask++;
    else if (e.value === "DENY") deny++;
  }
  return { allow, ask, deny };
}

function extractExceptions(entries: PermissionEntry[]): ConsentException[] {
  const exceptions: ConsentException[] = [];
  for (const entry of entries) {
    for (const cond of entry.conditions) {
      if (cond.condition_type === "unless_authorized_platform") {
        const platform = getPlatform(cond.value);
        exceptions.push({
          permissionType: entry.permission_type,
          baseValue: entry.value,
          platformId: cond.value,
          platformName: platform?.name ?? cond.value,
        });
      }
    }
  }
  return exceptions;
}

function buildGroup(
  roman: (typeof ROMAN)[number],
  label: string,
  types: PermissionType[],
  allPermissions: PermissionEntry[],
): ConsentGroup {
  const entries = allPermissions.filter((p) => types.includes(p.permission_type));
  return {
    roman,
    label,
    tooltip: GROUP_TOOLTIPS[label] ?? "",
    entries,
    counts: countValues(entries),
    exceptions: extractExceptions(entries),
  };
}

/** Build the 3 consent groups from a flat permission array. */
export function buildConsentGroups(permissions: PermissionEntry[]): ConsentGroup[] {
  return [
    buildGroup("I", "AI & GENERATION", AI_GENERATION_TYPES, permissions),
    buildGroup("II", "DISTRIBUTION & LICENSING", DISTRIBUTION_TYPES, permissions),
    buildGroup("III", "CREATIVE DERIVATIVES", CREATIVE_TYPES, permissions),
  ];
}

/** Format a permission type for display (e.g. "VOICE_CLONING" → "Voice Cloning"). */
export function formatPermissionType(type: string): string {
  return type
    .split("_")
    .map((w) => w.charAt(0).toUpperCase() + w.slice(1).toLowerCase())
    .join(" ");
}
