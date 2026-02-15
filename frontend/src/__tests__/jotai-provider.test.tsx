/**
 * Tests for explicit Jotai Provider at root layout.
 *
 * Verifies that:
 * 1. JotaiProvider exists and renders children
 * 2. layout.tsx wraps content with JotaiProvider
 */

import { readFileSync } from "fs";
import { resolve } from "path";
import { describe, it, expect } from "vitest";
import { render, screen } from "@testing-library/react";
import React from "react";

describe("Jotai Provider", () => {
  it("JotaiProvider renders children", async () => {
    const { JotaiProvider } = await import("@/lib/jotai-provider");
    render(
      <JotaiProvider>
        <div data-testid="child">Hello Jotai</div>
      </JotaiProvider>,
    );
    expect(screen.getByTestId("child")).toHaveTextContent("Hello Jotai");
  });

  it("layout.tsx imports JotaiProvider", () => {
    const layoutPath = resolve(__dirname, "..", "app", "layout.tsx");
    const content = readFileSync(layoutPath, "utf-8");
    expect(content).toContain("JotaiProvider");
    expect(content).toMatch(/import.*JotaiProvider.*from/);
  });

  it("jotai-provider.tsx imports Provider from jotai", () => {
    const providerPath = resolve(__dirname, "..", "lib", "jotai-provider.tsx");
    const content = readFileSync(providerPath, "utf-8");
    expect(content).toMatch(/import.*Provider.*from\s+["']jotai["']/);
  });
});
