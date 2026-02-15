import { describe, it, expect } from "vitest";
import { buildConsentGroups, formatPermissionType } from "./consent-groups";
import { MOCK_PERMISSIONS } from "@/lib/data/mock-permissions";

describe("buildConsentGroups", () => {
  const groups = buildConsentGroups(MOCK_PERMISSIONS.permissions);

  it("produces exactly 3 groups", () => {
    expect(groups).toHaveLength(3);
  });

  it("labels groups with roman numerals", () => {
    expect(groups.map((g) => g.roman)).toEqual(["I", "II", "III"]);
  });

  it("group I contains AI & Generation entries", () => {
    expect(groups[0].label).toBe("AI & GENERATION");
    // 7 of 8 types present in mock data (AI_TRAINING_STYLE missing)
    expect(groups[0].entries).toHaveLength(7);
  });

  it("group I counts are 4 allow, 2 ask, 1 deny", () => {
    expect(groups[0].counts).toEqual({ allow: 4, ask: 2, deny: 1 });
  });

  it("group II contains Distribution & Licensing entries", () => {
    expect(groups[1].label).toBe("DISTRIBUTION & LICENSING");
    expect(groups[1].entries).toHaveLength(4);
  });

  it("group II counts are 3 allow, 1 ask, 0 deny", () => {
    expect(groups[1].counts).toEqual({ allow: 3, ask: 1, deny: 0 });
  });

  it("group III contains Creative Derivatives entries", () => {
    expect(groups[2].label).toBe("CREATIVE DERIVATIVES");
    expect(groups[2].entries).toHaveLength(3);
  });

  it("group III counts are 0 allow, 3 ask, 0 deny", () => {
    expect(groups[2].counts).toEqual({ allow: 0, ask: 3, deny: 0 });
  });

  it("extracts voice cloning exception with Jen (Futureverse)", () => {
    const exceptions = groups[0].exceptions;
    expect(exceptions).toHaveLength(1);
    expect(exceptions[0].permissionType).toBe("VOICE_CLONING");
    expect(exceptions[0].baseValue).toBe("DENY");
    expect(exceptions[0].platformId).toBe("jen-futureverse");
    expect(exceptions[0].platformName).toBe("Jen (Futureverse)");
  });

  it("handles empty permissions gracefully", () => {
    const empty = buildConsentGroups([]);
    expect(empty).toHaveLength(3);
    for (const g of empty) {
      expect(g.entries).toHaveLength(0);
      expect(g.counts).toEqual({ allow: 0, ask: 0, deny: 0 });
      expect(g.exceptions).toHaveLength(0);
    }
  });

  it("each group has tooltip text", () => {
    for (const g of groups) {
      expect(g.tooltip.length).toBeGreaterThan(0);
    }
  });
});

describe("formatPermissionType", () => {
  it("formats VOICE_CLONING as 'Voice Cloning'", () => {
    expect(formatPermissionType("VOICE_CLONING")).toBe("Voice Cloning");
  });

  it("formats AI_TRAINING as 'Ai Training'", () => {
    expect(formatPermissionType("AI_TRAINING")).toBe("Ai Training");
  });

  it("formats single word", () => {
    expect(formatPermissionType("STREAM")).toBe("Stream");
  });
});
