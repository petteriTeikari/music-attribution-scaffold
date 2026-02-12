/**
 * Tests for shared frontend config module.
 */
import { describe, it, expect } from "vitest";
import * as fs from "fs";
import * as path from "path";

describe("Frontend config module", () => {
  it("exports API_URL and API_BASE from single module", async () => {
    const config = await import("@/lib/config");
    expect(config).toHaveProperty("API_URL");
    expect(config).toHaveProperty("API_BASE");
    expect(config).toHaveProperty("COPILOT_RUNTIME_URL");
  });

  it("api-client imports from config, not process.env", () => {
    const source = fs.readFileSync(
      path.resolve(__dirname, "../lib/api/api-client.ts"),
      "utf-8"
    );
    expect(source).not.toContain("process.env.NEXT_PUBLIC_API_URL");
    expect(source).toContain("from \"@/lib/config\"");
  });

  it("copilot-provider imports from config, not process.env", () => {
    const source = fs.readFileSync(
      path.resolve(__dirname, "../lib/copilot/copilot-provider.tsx"),
      "utf-8"
    );
    expect(source).not.toContain("process.env.NEXT_PUBLIC_API_URL");
    expect(source).toContain("from \"@/lib/config\"");
  });
});
