/**
 * Mock API client with simulated latency.
 * Replaces real API calls during demo/development.
 */

import type { AttributionRecord } from "@/lib/types/attribution";
import type { PermissionBundle, AuditLogEntry } from "@/lib/types/permissions";
import type { ProvenanceResponse } from "@/lib/types/uncertainty";

function delay(ms: number): Promise<void> {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

function randomDelay(): number {
  return 200 + Math.random() * 300; // 200-500ms
}

export const mockApi = {
  async getWorks(): Promise<AttributionRecord[]> {
    // Dynamic import to avoid circular dependencies
    const { MOCK_WORKS } = await import("@/lib/data/mock-works");
    await delay(randomDelay());
    return MOCK_WORKS;
  },

  async getWorkById(id: string): Promise<AttributionRecord | null> {
    const { getWorkById } = await import("@/lib/data/mock-works");
    await delay(randomDelay());
    return getWorkById(id) ?? null;
  },

  async getProvenance(
    attributionId: string
  ): Promise<ProvenanceResponse | null> {
    await delay(randomDelay());
    const { MOCK_WORKS } = await import("@/lib/data/mock-works");
    const work = MOCK_WORKS.find((w) => w.attribution_id === attributionId);
    if (!work) return null;
    return {
      attribution_id: work.attribution_id,
      provenance_chain: work.provenance_chain,
      uncertainty_summary: work.uncertainty_summary,
    };
  },

  async getPermissions(): Promise<PermissionBundle | null> {
    const { MOCK_PERMISSIONS } = await import("@/lib/data/mock-permissions");
    await delay(randomDelay());
    return MOCK_PERMISSIONS;
  },

  async getAuditLog(): Promise<AuditLogEntry[]> {
    const { MOCK_AUDIT_LOG } = await import("@/lib/data/mock-permissions");
    await delay(randomDelay());
    return MOCK_AUDIT_LOG;
  },
};
