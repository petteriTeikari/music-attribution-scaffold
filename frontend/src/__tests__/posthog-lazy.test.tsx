/**
 * Tests for lazy PostHog loading pattern.
 *
 * Verifies that posthog-js is NOT statically imported,
 * and that the provider/events/feature-flags gracefully
 * handle the "not yet loaded" state.
 */

import { describe, it, expect } from "vitest";
import { render, screen } from "@testing-library/react";
import React from "react";

describe("PostHog lazy loading", () => {
  it("PostHogProvider renders children without posthog-js loaded", async () => {
    // Dynamic import to avoid pulling posthog-js into test bundle
    const { PostHogProvider } = await import("@/lib/analytics/posthog-provider");
    render(
      <PostHogProvider>
        <div data-testid="child">Hello</div>
      </PostHogProvider>,
    );
    expect(screen.getByTestId("child")).toHaveTextContent("Hello");
  });

  it("trackEvent is a no-op when posthog is not initialized", async () => {
    const { trackEvent } = await import("@/lib/analytics/events");
    // Should not throw
    expect(() => {
      trackEvent("work_selected", { attribution_id: "test-123" });
    }).not.toThrow();
  });

  it("getPostHogInstance returns null when not initialized", async () => {
    const { getPostHogInstance } = await import("@/lib/analytics/posthog-provider");
    // In test environment, PostHog is never initialized (no env var)
    expect(getPostHogInstance()).toBeNull();
  });

  it("posthog-provider does NOT have a static import of posthog-js", async () => {
    // Read the source file and verify it uses dynamic import, not static
    const fs = await import("fs");
    const providerSource = fs.readFileSync(
      "src/lib/analytics/posthog-provider.tsx",
      "utf-8",
    );
    // Should NOT have `import posthog from "posthog-js"`
    expect(providerSource).not.toMatch(/^import\s+posthog\s+from\s+["']posthog-js["']/m);
    // Should have dynamic import
    expect(providerSource).toMatch(/import\(["']posthog-js["']\)/);
  });

  it("events.ts does NOT have a static import of posthog-js", async () => {
    const fs = await import("fs");
    const eventsSource = fs.readFileSync(
      "src/lib/analytics/events.ts",
      "utf-8",
    );
    // Should NOT directly import posthog from posthog-js
    expect(eventsSource).not.toMatch(/^import\s+.*from\s+["']posthog-js["']/m);
  });
});
