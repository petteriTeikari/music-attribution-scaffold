import { describe, it, expect } from "vitest";
import { MOCK_WORKS, getWorkById } from "./mock-works";

describe("MOCK_WORKS", () => {
  it("has exactly 9 works", () => {
    expect(MOCK_WORKS).toHaveLength(9);
  });

  it("all works have required fields", () => {
    for (const work of MOCK_WORKS) {
      expect(work.attribution_id).toBeDefined();
      expect(work.work_title).toBeDefined();
      expect(work.artist_name).toBe("Imogen Heap");
      expect(work.credits.length).toBeGreaterThanOrEqual(1);
      expect(work.confidence_score).toBeGreaterThanOrEqual(0);
      expect(work.confidence_score).toBeLessThanOrEqual(1);
      expect(work.assurance_level).toBeDefined();
      expect(work.conformal_set).toBeDefined();
    }
  });

  it("works span confidence range from 0.0 to 0.95", () => {
    const scores = MOCK_WORKS.map((w) => w.confidence_score).sort(
      (a, b) => a - b
    );
    expect(scores[0]).toBe(0.0);
    expect(scores[scores.length - 1]).toBe(0.95);
  });

  it("Hide and Seek has the richest provenance chain", () => {
    const hideAndSeek = MOCK_WORKS.find(
      (w) => w.work_title === "Hide and Seek"
    );
    expect(hideAndSeek).toBeDefined();
    expect(hideAndSeek!.provenance_chain.length).toBeGreaterThanOrEqual(5);
    expect(hideAndSeek!.confidence_score).toBe(0.95);
  });

  it("works with confidence < 0.7 need review", () => {
    const needsReview = MOCK_WORKS.filter((w) => w.confidence_score < 0.7);
    for (const work of needsReview) {
      expect(work.needs_review).toBe(true);
    }
  });

  it("Blanket has LEVEL_0 assurance", () => {
    const blanket = MOCK_WORKS.find((w) => w.work_title === "Blanket");
    expect(blanket).toBeDefined();
    expect(blanket!.assurance_level).toBe("LEVEL_0");
    expect(blanket!.confidence_score).toBe(0.0);
  });

  it("uses consistent entity ID for Imogen Heap", () => {
    for (const work of MOCK_WORKS) {
      const imogenCredits = work.credits.filter(
        (c) => c.entity_name === "Imogen Heap"
      );
      for (const credit of imogenCredits) {
        expect(credit.entity_id).toBe("artist-imogen-heap");
      }
    }
  });
});

describe("getWorkById", () => {
  it("returns the correct work", () => {
    const work = getWorkById("work-001");
    expect(work).toBeDefined();
    expect(work!.work_title).toBe("Hide and Seek");
  });

  it("returns undefined for non-existent ID", () => {
    expect(getWorkById("nonexistent")).toBeUndefined();
  });
});
