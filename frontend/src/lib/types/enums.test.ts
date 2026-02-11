import { describe, it, expect } from "vitest";
import {
  Source,
  EntityType,
  AssuranceLevel,
  CreditRole,
  PermissionType,
  PermissionValue,
} from "./enums";

describe("TypeScript enum objects", () => {
  it("Source has all 5 values", () => {
    expect(Object.keys(Source)).toHaveLength(5);
    expect(Source.MUSICBRAINZ).toBe("MUSICBRAINZ");
    expect(Source.ARTIST_INPUT).toBe("ARTIST_INPUT");
  });

  it("EntityType has 6 values", () => {
    expect(Object.keys(EntityType)).toHaveLength(6);
  });

  it("AssuranceLevel has 4 levels (A0-A3)", () => {
    expect(Object.keys(AssuranceLevel)).toHaveLength(4);
    expect(AssuranceLevel.LEVEL_0).toBe("LEVEL_0");
    expect(AssuranceLevel.LEVEL_3).toBe("LEVEL_3");
  });

  it("CreditRole has 14 roles", () => {
    expect(Object.keys(CreditRole)).toHaveLength(14);
    expect(CreditRole.PERFORMER).toBe("PERFORMER");
    expect(CreditRole.REMIXER).toBe("REMIXER");
  });

  it("PermissionType has 11 types", () => {
    expect(Object.keys(PermissionType)).toHaveLength(11);
    expect(PermissionType.AI_TRAINING).toBe("AI_TRAINING");
    expect(PermissionType.VOICE_CLONING).toBe("VOICE_CLONING");
  });

  it("PermissionValue has 5 values", () => {
    expect(Object.keys(PermissionValue)).toHaveLength(5);
    expect(PermissionValue.ALLOW).toBe("ALLOW");
    expect(PermissionValue.DENY).toBe("DENY");
    expect(PermissionValue.ALLOW_WITH_ROYALTY).toBe("ALLOW_WITH_ROYALTY");
  });
});
