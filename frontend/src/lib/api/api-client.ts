/**
 * API client for the FastAPI attribution backend.
 *
 * Uses NEXT_PUBLIC_API_URL environment variable for the backend URL.
 * Falls back to mock data when the API is unavailable.
 */

import type { AttributionRecord } from "@/lib/types/attribution";
import type { ProvenanceResponse } from "@/lib/types/uncertainty";

const API_URL = process.env.NEXT_PUBLIC_API_URL || "";

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
    if (!API_URL) return fallbackGetWorks();
    try {
      return await fetchJson<AttributionRecord[]>(`${API_URL}/attributions/`);
    } catch {
      return fallbackGetWorks();
    }
  },

  async getWorkById(id: string): Promise<AttributionRecord | null> {
    if (!API_URL) return fallbackGetWorkById(id);
    try {
      return await fetchJson<AttributionRecord>(
        `${API_URL}/attributions/work/${id}`
      );
    } catch {
      return fallbackGetWorkById(id);
    }
  },

  async getProvenance(
    attributionId: string
  ): Promise<ProvenanceResponse | null> {
    if (!API_URL) return fallbackGetProvenance(attributionId);
    try {
      return await fetchJson<ProvenanceResponse>(
        `${API_URL}/attributions/${attributionId}/provenance`
      );
    } catch {
      return fallbackGetProvenance(attributionId);
    }
  },

  async search(query: string): Promise<SearchResult[]> {
    if (!API_URL) return [];
    try {
      return await fetchJson<SearchResult[]>(
        `${API_URL}/attributions/search?q=${encodeURIComponent(query)}`
      );
    } catch {
      return [];
    }
  },

  async checkPermission(
    entityId: string,
    permissionType: string
  ): Promise<PermissionCheckResult> {
    return fetchJson<PermissionCheckResult>(`${API_URL}/permissions/check`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
      body: JSON.stringify({
        entity_id: entityId,
        permission_type: permissionType,
      }),
    });
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
