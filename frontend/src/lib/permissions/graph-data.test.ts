import { describe, it, expect } from "vitest";
import { buildGraphData } from "./graph-data";
import { MOCK_AUDIT_LOG } from "@/lib/data/mock-permissions";

describe("buildGraphData", () => {
  const { nodes, links } = buildGraphData(MOCK_AUDIT_LOG);

  it("creates 1 artist node", () => {
    const artistNodes = nodes.filter((n) => n.type === "artist");
    expect(artistNodes).toHaveLength(1);
    expect(artistNodes[0].id).toBe("artist");
    expect(artistNodes[0].label).toBe("Imogen Heap");
  });

  it("creates 3 group nodes", () => {
    const groupNodes = nodes.filter((n) => n.type === "group");
    expect(groupNodes).toHaveLength(3);
    expect(groupNodes.map((n) => n.label)).toContain("AI & Generation");
    expect(groupNodes.map((n) => n.label)).toContain("Distribution");
    expect(groupNodes.map((n) => n.label)).toContain("Creative");
  });

  it("creates platform nodes from audit log", () => {
    const platformNodes = nodes.filter((n) => n.type === "platform");
    // Should have unique platforms from audit log
    expect(platformNodes.length).toBeGreaterThanOrEqual(10);
    // SoundCloud should appear only once even though it has 2 audit entries
    const soundcloudNodes = platformNodes.filter((n) => n.label === "SoundCloud");
    expect(soundcloudNodes).toHaveLength(1);
  });

  it("creates links from platforms to groups", () => {
    // Each audit entry creates a link from platform to the appropriate group
    expect(links.length).toBeGreaterThanOrEqual(15);
  });

  it("creates 3 core links from artist to groups", () => {
    const coreLinks = links.filter((l) => l.source === "artist");
    expect(coreLinks).toHaveLength(3);
  });

  it("handles empty input gracefully", () => {
    const result = buildGraphData([]);
    expect(result.nodes).toHaveLength(4); // artist + 3 groups
    expect(result.links).toHaveLength(3); // artist → 3 groups
  });
});
