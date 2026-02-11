/**
 * Tests for real API client with fetch mock.
 */

import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";

// Mock fetch globally before importing the client
const mockFetch = vi.fn();
vi.stubGlobal("fetch", mockFetch);

describe("ApiClient", () => {
  const API_URL = "http://localhost:8000";

  beforeEach(() => {
    vi.stubEnv("NEXT_PUBLIC_API_URL", API_URL);
    mockFetch.mockReset();
  });

  afterEach(() => {
    vi.unstubAllEnvs();
  });

  it("fetches works from /api/v1/attributions/", async () => {
    const { apiClient } = await import("@/lib/api/api-client");
    const mockData = [
      { attribution_id: "work-001", confidence_score: 0.95, credits: [] },
    ];
    mockFetch.mockResolvedValueOnce({
      ok: true,
      json: () => Promise.resolve(mockData),
    });

    const works = await apiClient.getWorks();
    expect(mockFetch).toHaveBeenCalledWith(
      `${API_URL}/api/v1/attributions/`,
      expect.any(Object)
    );
    expect(works).toHaveLength(1);
  });

  it("fetches work by ID from /api/v1/attributions/work/{id}", async () => {
    const { apiClient } = await import("@/lib/api/api-client");
    const mockData = {
      attribution_id: "work-001",
      work_entity_id: "entity-001",
      confidence_score: 0.95,
    };
    mockFetch.mockResolvedValueOnce({
      ok: true,
      json: () => Promise.resolve(mockData),
    });

    const work = await apiClient.getWorkById("entity-001");
    expect(mockFetch).toHaveBeenCalledWith(
      `${API_URL}/api/v1/attributions/work/entity-001`,
      expect.any(Object)
    );
    expect(work).toBeTruthy();
    expect(work?.work_entity_id).toBe("entity-001");
  });

  it("searches via /api/v1/attributions/search", async () => {
    const { apiClient } = await import("@/lib/api/api-client");
    const mockData = [
      {
        attribution: { attribution_id: "work-001", confidence_score: 0.95 },
        rrf_score: 0.03,
      },
    ];
    mockFetch.mockResolvedValueOnce({
      ok: true,
      json: () => Promise.resolve(mockData),
    });

    const results = await apiClient.search("vocoder");
    expect(mockFetch).toHaveBeenCalledWith(
      expect.stringContaining("/api/v1/attributions/search?q=vocoder"),
      expect.any(Object)
    );
    expect(results).toHaveLength(1);
    expect(results[0].rrf_score).toBe(0.03);
  });

  it("checks permission via /api/v1/permissions/check", async () => {
    const { apiClient } = await import("@/lib/api/api-client");
    const mockResponse = { result: "ALLOW", conditions: [] };
    mockFetch.mockResolvedValueOnce({
      ok: true,
      json: () => Promise.resolve(mockResponse),
    });

    const result = await apiClient.checkPermission(
      "entity-id",
      "streaming"
    );
    expect(mockFetch).toHaveBeenCalledWith(
      `${API_URL}/api/v1/permissions/check`,
      expect.objectContaining({ method: "POST" })
    );
    expect(result.result).toBe("ALLOW");
  });

  it("falls back to mock data when API unavailable", async () => {
    const { apiClient } = await import("@/lib/api/api-client");
    mockFetch.mockRejectedValue(new Error("Network error"));

    const works = await apiClient.getWorks();
    // Falls back to mock data — should return Imogen Heap works
    expect(works.length).toBeGreaterThan(0);
  });
});
