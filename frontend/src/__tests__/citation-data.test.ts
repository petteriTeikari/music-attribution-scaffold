/**
 * Tests for citation data module — Task 0.1
 *
 * Validates the citation database and topic card definitions
 * that power the landing page academic citation redesign.
 */

import { describe, expect, it } from "vitest";

import { CITATIONS, type CitationRef } from "@/lib/data/citations";
import {
  TOPIC_CARDS,
  type TopicCard,
  TOPIC_GROUPS,
} from "@/lib/data/topic-cards";

describe("Citation database", () => {
  it("exports an array of CitationRef objects", () => {
    expect(Array.isArray(CITATIONS)).toBe(true);
    expect(CITATIONS.length).toBeGreaterThanOrEqual(25);
  });

  it("each citation has required fields", () => {
    for (const c of CITATIONS) {
      expect(c).toHaveProperty("id");
      expect(c).toHaveProperty("authors");
      expect(c).toHaveProperty("year");
      expect(c).toHaveProperty("title");
      expect(c).toHaveProperty("venue");
      expect(typeof c.id).toBe("number");
      expect(typeof c.authors).toBe("string");
      expect(typeof c.year).toBe("number");
      expect(typeof c.title).toBe("string");
      expect(typeof c.venue).toBe("string");
    }
  });

  it("citation IDs are sequential starting from 1", () => {
    CITATIONS.forEach((c, i) => {
      expect(c.id).toBe(i + 1);
    });
  });

  it("citation IDs are unique", () => {
    const ids = CITATIONS.map((c) => c.id);
    expect(new Set(ids).size).toBe(ids.length);
  });

  it("URLs are well-formed when present", () => {
    const urlPattern = /^https?:\/\//;
    for (const c of CITATIONS) {
      if (c.url) {
        expect(c.url).toMatch(urlPattern);
      }
      if (c.doi) {
        expect(c.doi).toMatch(/^https?:\/\//);
      }
    }
  });

  it("includes key citations from the plan", () => {
    const titles = CITATIONS.map((c) => c.title.toLowerCase());
    // Conformal prediction
    expect(titles.some((t) => t.includes("conformal"))).toBe(true);
    // Uncertainty
    expect(titles.some((t) => t.includes("uncertainty"))).toBe(true);
    // MCP
    expect(
      titles.some((t) => t.includes("model context protocol")),
    ).toBe(true);
    // DPP / agentic supply chain
    expect(
      titles.some((t) => t.includes("digital product passport")),
    ).toBe(true);
    // Main paper
    expect(
      titles.some((t) => t.includes("governing generative music")),
    ).toBe(true);
  });
});

describe("Topic cards", () => {
  it("exports an array of TopicCard objects", () => {
    expect(Array.isArray(TOPIC_CARDS)).toBe(true);
    expect(TOPIC_CARDS.length).toBe(12);
  });

  it("each topic card has required fields", () => {
    for (const card of TOPIC_CARDS) {
      expect(card).toHaveProperty("id");
      expect(card).toHaveProperty("marker");
      expect(card).toHaveProperty("title");
      expect(card).toHaveProperty("summary");
      expect(card).toHaveProperty("detail");
      expect(card).toHaveProperty("citationIds");
      expect(card).toHaveProperty("figurePlan");
      expect(typeof card.id).toBe("string");
      expect(typeof card.marker).toBe("string");
      expect(typeof card.title).toBe("string");
      expect(typeof card.summary).toBe("string");
      expect(typeof card.detail).toBe("string");
      expect(Array.isArray(card.citationIds)).toBe(true);
      expect(typeof card.figurePlan).toBe("string");
    }
  });

  it("Roman numeral markers are sequential I through XII", () => {
    const expected = [
      "I", "II", "III", "IV", "V", "VI",
      "VII", "VIII", "IX", "X", "XI", "XII",
    ];
    TOPIC_CARDS.forEach((card, i) => {
      expect(card.marker).toBe(expected[i]);
    });
  });

  it("all citationIds reference valid citation IDs", () => {
    const validIds = new Set(CITATIONS.map((c) => c.id));
    for (const card of TOPIC_CARDS) {
      for (const id of card.citationIds) {
        expect(validIds.has(id)).toBe(true);
      }
    }
  });

  it("each card has at least one citation", () => {
    for (const card of TOPIC_CARDS) {
      expect(card.citationIds.length).toBeGreaterThanOrEqual(1);
    }
  });

  it("summary is concise (under 300 chars)", () => {
    for (const card of TOPIC_CARDS) {
      expect(card.summary.length).toBeLessThan(300);
    }
  });

  it("detail provides more depth (at least 100 chars)", () => {
    for (const card of TOPIC_CARDS) {
      expect(card.detail.length).toBeGreaterThanOrEqual(100);
    }
  });

  it("figurePlan is non-empty", () => {
    for (const card of TOPIC_CARDS) {
      expect(card.figurePlan.length).toBeGreaterThan(20);
    }
  });
});

describe("Topic groups", () => {
  it("exports three topic groups", () => {
    expect(TOPIC_GROUPS).toHaveLength(3);
  });

  it("each group has a label and card IDs", () => {
    for (const group of TOPIC_GROUPS) {
      expect(group).toHaveProperty("label");
      expect(group).toHaveProperty("cardIds");
      expect(typeof group.label).toBe("string");
      expect(Array.isArray(group.cardIds)).toBe(true);
    }
  });

  it("all card IDs in groups reference valid topic cards", () => {
    const validIds = new Set(TOPIC_CARDS.map((c) => c.id));
    for (const group of TOPIC_GROUPS) {
      for (const id of group.cardIds) {
        expect(validIds.has(id)).toBe(true);
      }
    }
  });

  it("groups cover all 12 topic cards", () => {
    const allGroupIds = TOPIC_GROUPS.flatMap((g) => g.cardIds);
    expect(new Set(allGroupIds).size).toBe(12);
  });
});
