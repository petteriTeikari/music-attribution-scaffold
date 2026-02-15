/**
 * Tests for analytics event types — verifies new Phase 2 events exist.
 */
import { describe, it, expect } from "vitest";
import { EVENTS } from "@/lib/analytics/events";

describe("Analytics events", () => {
  it("includes EXTERNAL_LINK_CLICKED event", () => {
    expect(EVENTS.EXTERNAL_LINK_CLICKED).toBe("external_link_clicked");
  });

  it("includes NODE_OVERLAY_VIEWED event", () => {
    expect(EVENTS.NODE_OVERLAY_VIEWED).toBe("node_overlay_viewed");
  });

  it("includes CONFIDENCE_POPOVER_VIEWED event", () => {
    expect(EVENTS.CONFIDENCE_POPOVER_VIEWED).toBe("confidence_popover_viewed");
  });

  it("includes PROVENANCE_DAG_EXPANDED event", () => {
    expect(EVENTS.PROVENANCE_DAG_EXPANDED).toBe("provenance_dag_expanded");
  });
});
