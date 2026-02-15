/**
 * Tests for lazy CopilotKit loading pattern.
 *
 * Verifies that CopilotKit is dynamically imported (not eagerly parsed),
 * reducing ~350 modules from initial page load.
 */

import { readFileSync } from "fs";
import { resolve } from "path";
import { describe, it, expect } from "vitest";
import { render, screen } from "@testing-library/react";
import React from "react";

describe("CopilotKit lazy loading", () => {
  it("CopilotProvider renders children without CopilotKit loaded", async () => {
    const { CopilotProvider } = await import("@/lib/copilot/copilot-provider");
    render(
      <CopilotProvider>
        <div data-testid="child">Hello</div>
      </CopilotProvider>,
    );
    expect(screen.getByTestId("child")).toHaveTextContent("Hello");
  });

  it("copilot-provider.tsx uses next/dynamic instead of static import", () => {
    const providerPath = resolve(__dirname, "..", "lib", "copilot", "copilot-provider.tsx");
    const content = readFileSync(providerPath, "utf-8");
    // Should NOT have static import of CopilotKit
    expect(content).not.toMatch(/^import\s+\{\s*CopilotKit\s*\}\s+from\s+["']@copilotkit\/react-core["']/m);
    // Should use next/dynamic
    expect(content).toMatch(/dynamic\(/);
  });

  it("app-shell.tsx uses dynamic import for AgentSidebar", () => {
    const shellPath = resolve(__dirname, "..", "components", "layout", "app-shell.tsx");
    const content = readFileSync(shellPath, "utf-8");
    // Should NOT have static import of AgentSidebar
    expect(content).not.toMatch(/^import\s+\{\s*AgentSidebar\s*\}\s+from/m);
    // Should use next/dynamic
    expect(content).toMatch(/dynamic\(/);
  });
});
