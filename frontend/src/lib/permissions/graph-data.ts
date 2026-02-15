/**
 * Transforms audit log entries into a D3-compatible node-link graph.
 *
 * Graph structure:
 * - Center: Artist node (pinned)
 * - Ring 1: 3 consent group nodes (AI & Generation, Distribution, Creative)
 * - Ring 2: Platform nodes (from audit log, deduplicated)
 * - Links: Platform → Group (colored by result), Artist → Group (core)
 */

import type { AuditLogEntry } from "@/lib/types/permissions";
import type { PermissionType } from "@/lib/types/enums";
import {
  AI_GENERATION_TYPES,
  DISTRIBUTION_TYPES,
  CREATIVE_TYPES,
} from "./consent-groups";

export interface GraphNode {
  id: string;
  label: string;
  type: "artist" | "group" | "platform";
  platformType?: string;
}

export interface GraphLink {
  source: string;
  target: string;
  result: string;
  permissionType: string;
}

export interface GraphData {
  nodes: GraphNode[];
  links: GraphLink[];
}

function getGroupForPermission(permType: PermissionType): string | null {
  if (AI_GENERATION_TYPES.includes(permType)) return "group-ai";
  if (DISTRIBUTION_TYPES.includes(permType)) return "group-dist";
  if (CREATIVE_TYPES.includes(permType)) return "group-creative";
  return null;
}

export function buildGraphData(auditLog: AuditLogEntry[]): GraphData {
  const nodes: GraphNode[] = [
    { id: "artist", label: "Imogen Heap", type: "artist" },
    { id: "group-ai", label: "AI & Generation", type: "group" },
    { id: "group-dist", label: "Distribution", type: "group" },
    { id: "group-creative", label: "Creative", type: "group" },
  ];

  const links: GraphLink[] = [
    { source: "artist", target: "group-ai", result: "core", permissionType: "" },
    { source: "artist", target: "group-dist", result: "core", permissionType: "" },
    { source: "artist", target: "group-creative", result: "core", permissionType: "" },
  ];

  const seenPlatforms = new Set<string>();

  for (const entry of auditLog) {
    const platformId = `platform-${entry.requester_name.toLowerCase().replace(/[^a-z0-9]/g, "-")}`;
    const groupId = getGroupForPermission(entry.permission_type);
    if (!groupId) continue;

    // Add platform node (deduplicated)
    if (!seenPlatforms.has(platformId)) {
      seenPlatforms.add(platformId);
      nodes.push({
        id: platformId,
        label: entry.requester_name,
        type: "platform",
        platformType: entry.requester_type,
      });
    }

    // Add link from platform to group
    links.push({
      source: platformId,
      target: groupId,
      result: entry.result,
      permissionType: entry.permission_type,
    });
  }

  return { nodes, links };
}
