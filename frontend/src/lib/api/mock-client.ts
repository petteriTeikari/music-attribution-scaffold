/**
 * Mock API client with simulated latency.
 * Replaces real API calls during demo/development.
 */

import type { AttributionRecord } from "@/lib/types/attribution";
import type { PermissionBundle, AuditLogEntry } from "@/lib/types/permissions";

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
