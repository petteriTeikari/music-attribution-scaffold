/**
 * API client for the FastAPI attribution backend.
 *
 * Uses NEXT_PUBLIC_API_URL environment variable for the backend URL.
 * Falls back to mock data when the API is unavailable.
 */

import type { AttributionRecord } from "@/lib/types/attribution";
import type { PermissionBundle, AuditLogEntry } from "@/lib/types/permissions";
import type { ProvenanceResponse } from "@/lib/types/uncertainty";

const API_URL = process.env.NEXT_PUBLIC_API_URL || "";
const API_BASE = API_URL ? `${API_URL}/api/v1` : "";

export interface SearchResult {
  attribution: AttributionRecord;
  rrf_score: number;
}

export interface PermissionCheckResult {
  result: string;
  conditions: string[];
}

async function fetchJson<T>(url: string, options?: RequestInit): Promise<T> {
  const response = await fetch(url, {
    headers: { Accept: "application/json" },
    ...options,
  });
  if (!response.ok) {
    throw new Error(`API error: ${response.status}`);
  }
  return response.json() as Promise<T>;
}

export const apiClient = {
  async getWorks(): Promise<AttributionRecord[]> {
    if (!API_BASE) return fallbackGetWorks();
    try {
      return await fetchJson<AttributionRecord[]>(
        `${API_BASE}/attributions/`
      );
    } catch {
      return fallbackGetWorks();
    }
  },

  async getWorkById(id: string): Promise<AttributionRecord | null> {
    if (!API_BASE) return fallbackGetWorkById(id);
    try {
      return await fetchJson<AttributionRecord>(
        `${API_BASE}/attributions/work/${id}`
      );
    } catch {
      return fallbackGetWorkById(id);
    }
  },

  async getProvenance(
    attributionId: string
  ): Promise<ProvenanceResponse | null> {
    if (!API_BASE) return fallbackGetProvenance(attributionId);
    try {
      return await fetchJson<ProvenanceResponse>(
        `${API_BASE}/attributions/${attributionId}/provenance`
      );
    } catch {
      return fallbackGetProvenance(attributionId);
    }
  },

  async search(query: string): Promise<SearchResult[]> {
    if (!API_BASE) return [];
    try {
      return await fetchJson<SearchResult[]>(
        `${API_BASE}/attributions/search?q=${encodeURIComponent(query)}`
      );
    } catch {
      return [];
    }
  },

  async checkPermission(
    entityId: string,
    permissionType: string
  ): Promise<PermissionCheckResult> {
    return fetchJson<PermissionCheckResult>(
      `${API_BASE}/permissions/check`,
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Accept: "application/json",
        },
        body: JSON.stringify({
          entity_id: entityId,
          permission_type: permissionType,
        }),
      }
    );
  },

  async getPermissions(entityId: string): Promise<PermissionBundle | null> {
    if (!API_BASE) return fallbackGetPermissions();
    try {
      const bundles = await fetchJson<PermissionBundle[]>(
        `${API_BASE}/permissions/${entityId}`
      );
      return bundles.length > 0 ? bundles[0] : null;
    } catch {
      return fallbackGetPermissions();
    }
  },

  async getAuditLog(): Promise<AuditLogEntry[]> {
    if (!API_BASE) return fallbackGetAuditLog();
    try {
      return await fetchJson<AuditLogEntry[]>(
        `${API_BASE}/permissions/audit-log`
      );
    } catch {
      return fallbackGetAuditLog();
    }
  },
};

async function fallbackGetWorks(): Promise<AttributionRecord[]> {
  const { mockApi } = await import("./mock-client");
  return mockApi.getWorks();
}

async function fallbackGetWorkById(
  id: string
): Promise<AttributionRecord | null> {
  const { mockApi } = await import("./mock-client");
  return mockApi.getWorkById(id);
}

async function fallbackGetProvenance(
  attributionId: string
): Promise<ProvenanceResponse | null> {
  const { mockApi } = await import("./mock-client");
  return mockApi.getProvenance(attributionId);
}

async function fallbackGetPermissions(): Promise<PermissionBundle | null> {
  const { mockApi } = await import("./mock-client");
  return mockApi.getPermissions();
}

async function fallbackGetAuditLog(): Promise<AuditLogEntry[]> {
  const { mockApi } = await import("./mock-client");
  return mockApi.getAuditLog();
}
