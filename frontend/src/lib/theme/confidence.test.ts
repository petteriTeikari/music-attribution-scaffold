import { describe, it, expect } from "vitest";
import {
  getConfidenceTier,
  getConfidenceLabel,
  getConfidenceCssVar,
  getConfidenceBgCssVar,
  getAssuranceCssVar,
  getSourceCssVar,
  ASSURANCE_LABELS,
} from "./confidence";

describe("getConfidenceTier", () => {
  it("returns 'high' for scores >= 0.85", () => {
    expect(getConfidenceTier(0.85)).toBe("high");
    expect(getConfidenceTier(0.95)).toBe("high");
    expect(getConfidenceTier(1.0)).toBe("high");
  });

  it("returns 'medium' for scores 0.50-0.84", () => {
    expect(getConfidenceTier(0.5)).toBe("medium");
    expect(getConfidenceTier(0.72)).toBe("medium");
    expect(getConfidenceTier(0.84)).toBe("medium");
  });

  it("returns 'low' for scores < 0.50", () => {
    expect(getConfidenceTier(0.0)).toBe("low");
    expect(getConfidenceTier(0.35)).toBe("low");
    expect(getConfidenceTier(0.49)).toBe("low");
  });
});

describe("getConfidenceLabel", () => {
  it("returns correct labels for each tier", () => {
    expect(getConfidenceLabel(0.95)).toBe("High Confidence");
    expect(getConfidenceLabel(0.72)).toBe("Medium Confidence");
    expect(getConfidenceLabel(0.35)).toBe("Low Confidence");
  });
});

describe("getConfidenceCssVar", () => {
  it("returns correct CSS variable for each tier", () => {
    expect(getConfidenceCssVar("high")).toBe("var(--color-confidence-high)");
    expect(getConfidenceCssVar("medium")).toBe("var(--color-confidence-medium)");
    expect(getConfidenceCssVar("low")).toBe("var(--color-confidence-low)");
  });
});

describe("getConfidenceBgCssVar", () => {
  it("returns correct background CSS variable", () => {
    expect(getConfidenceBgCssVar("high")).toBe(
      "var(--color-confidence-high-bg)"
    );
  });
});

describe("getAssuranceCssVar", () => {
  it("returns correct CSS variable for each assurance level", () => {
    expect(getAssuranceCssVar("LEVEL_0")).toBe("var(--color-assurance-a0)");
    expect(getAssuranceCssVar("LEVEL_1")).toBe("var(--color-assurance-a1)");
    expect(getAssuranceCssVar("LEVEL_2")).toBe("var(--color-assurance-a2)");
    expect(getAssuranceCssVar("LEVEL_3")).toBe("var(--color-assurance-a3)");
  });

  it("falls back to a0 for unknown levels", () => {
    expect(getAssuranceCssVar("UNKNOWN")).toBe("var(--color-assurance-a0)");
  });
});

describe("getSourceCssVar", () => {
  it("returns correct CSS variable for each source", () => {
    expect(getSourceCssVar("MUSICBRAINZ")).toBe(
      "var(--color-source-musicbrainz)"
    );
    expect(getSourceCssVar("DISCOGS")).toBe("var(--color-source-discogs)");
    expect(getSourceCssVar("ACOUSTID")).toBe("var(--color-source-acoustid)");
    expect(getSourceCssVar("ARTIST_INPUT")).toBe("var(--color-source-artist)");
    expect(getSourceCssVar("FILE_METADATA")).toBe("var(--color-source-file)");
  });

  it("falls back to system for unknown sources", () => {
    expect(getSourceCssVar("UNKNOWN")).toBe("var(--color-source-system)");
  });
});

describe("ASSURANCE_LABELS", () => {
  it("has labels for all four levels", () => {
    expect(ASSURANCE_LABELS["LEVEL_0"]).toContain("A0");
    expect(ASSURANCE_LABELS["LEVEL_1"]).toContain("A1");
    expect(ASSURANCE_LABELS["LEVEL_2"]).toContain("A2");
    expect(ASSURANCE_LABELS["LEVEL_3"]).toContain("A3");
  });
});
