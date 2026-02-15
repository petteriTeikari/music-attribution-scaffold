/**
 * Tests for citation TypeScript types (Task 3.0) and API client provenance (Task 2.1).
 */

import { describe, it, expect } from "vitest";

describe("Citation TypeScript types", () => {
  it("CitationReference has required fields", async () => {
    const ref: import("@/lib/types/uncertainty").CitationReference = {
      index: 1,
      source: "MUSICBRAINZ" as import("@/lib/types/enums").Source,
      confidence: 0.92,
      label: "MusicBrainz",
      detail: "Matched via ISRC lookup",
      timestamp: "2024-06-15T10:00:00Z",
    };
    expect(ref.index).toBe(1);
    expect(ref.source).toBe("MUSICBRAINZ");
    expect(ref.confidence).toBeGreaterThanOrEqual(0);
  });

  it("StepUncertainty TS type has same fields as Python model", async () => {
    const step: import("@/lib/types/uncertainty").StepUncertainty = {
      step_id: "etl-musicbrainz",
      step_name: "MusicBrainz ETL",
      step_index: 0,
      stated_confidence: 0.85,
      calibrated_confidence: 0.82,
      intrinsic_uncertainty: 0.05,
      extrinsic_uncertainty: 0.08,
      total_uncertainty: 0.13,
      input_uncertainty: null,
      reasoning_uncertainty: null,
      parameter_uncertainty: null,
      prediction_uncertainty: null,
      uncertainty_sources: [],
      confidence_method: "SOURCE_WEIGHTED",
      preceding_step_ids: [],
    };
    expect(step.step_id).toBe("etl-musicbrainz");
    expect(step.total_uncertainty).toBeGreaterThanOrEqual(
      step.intrinsic_uncertainty
    );
  });

  it("mock data conforms to updated TS types", async () => {
    const { MOCK_WORKS } = await import("@/lib/data/mock-works");
    expect(MOCK_WORKS.length).toBe(9);

    for (const work of MOCK_WORKS) {
      // ProvenanceEvent has citation_index field
      for (const event of work.provenance_chain) {
        expect("citation_index" in event).toBe(true);
        expect("step_uncertainty" in event).toBe(true);
      }
      // AttributionRecord has uncertainty_summary field
      expect("uncertainty_summary" in work).toBe(true);
    }
  });
});

describe("API client provenance", () => {
  it("apiClient has getProvenance method", async () => {
    const { apiClient } = await import("@/lib/api/api-client");
    expect(typeof apiClient.getProvenance).toBe("function");
  });

  it("mockApi.getProvenance returns provenance data", async () => {
    const { mockApi } = await import("@/lib/api/mock-client");
    const result = await mockApi.getProvenance("work-001");
    expect(result).not.toBeNull();
    expect(result?.attribution_id).toBe("work-001");
    expect(result?.provenance_chain).toBeDefined();
    expect(result?.provenance_chain.length).toBeGreaterThan(0);
  });

  it("provenance response has citation_index", async () => {
    const { mockApi } = await import("@/lib/api/mock-client");
    const result = await mockApi.getProvenance("work-001");
    expect(result).not.toBeNull();
    if (result) {
      for (const event of result.provenance_chain) {
        expect("citation_index" in event).toBe(true);
      }
    }
  });

  it("apiClient falls back to mock when API_URL unset", async () => {
    // API_URL is unset in test environment, so getProvenance should fall back to mock
    const { apiClient } = await import("@/lib/api/api-client");
    const result = await apiClient.getProvenance("work-001");
    expect(result).not.toBeNull();
    expect(result?.attribution_id).toBe("work-001");
  });
});
