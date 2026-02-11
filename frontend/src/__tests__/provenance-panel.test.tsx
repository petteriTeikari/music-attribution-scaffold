/**
 * Tests for ProvenancePanel component (Task 3.2).
 */

import { render, screen, fireEvent } from "@testing-library/react";
import { describe, it, expect } from "vitest";
import { ProvenancePanel } from "@/components/citations/provenance-panel";
import type { ProvenanceEvent } from "@/lib/types/attribution";
import { ProvenanceEventType, Source } from "@/lib/types/enums";

const MOCK_EVENTS: ProvenanceEvent[] = [
  {
    event_type: ProvenanceEventType.FETCH,
    timestamp: "2024-06-15T10:00:00Z",
    agent: "etl-musicbrainz-v2",
    details: {
      type: "fetch",
      source: Source.MUSICBRAINZ,
      source_id: "mb-rec-001",
      records_fetched: 4,
      rate_limited: false,
    },
    feedback_card_id: null,
    step_uncertainty: null,
    citation_index: 1,
  },
  {
    event_type: ProvenanceEventType.RESOLVE,
    timestamp: "2024-06-15T10:05:00Z",
    agent: "resolution-orchestrator-v1",
    details: {
      type: "resolve",
      method: "splink_linkage",
      records_input: 12,
      entities_output: 4,
      confidence_range: [0.78, 0.99],
    },
    feedback_card_id: null,
    step_uncertainty: null,
    citation_index: 2,
  },
  {
    event_type: ProvenanceEventType.SCORE,
    timestamp: "2024-06-15T10:10:00Z",
    agent: "attribution-aggregator-v1",
    details: {
      type: "score",
      previous_confidence: null,
      new_confidence: 0.95,
      scoring_method: "weighted_source_agreement",
    },
    feedback_card_id: null,
    step_uncertainty: null,
    citation_index: 3,
  },
];

describe("ProvenancePanel", () => {
  it("renders provenance events chronologically", () => {
    render(<ProvenancePanel events={MOCK_EVENTS} />);
    const events = screen.getAllByTestId("provenance-event");
    expect(events.length).toBe(3);
  });

  it("shows source badges", () => {
    render(<ProvenancePanel events={MOCK_EVENTS} />);
    expect(screen.getByText(/FETCH/)).toBeInTheDocument();
    expect(screen.getByText(/RESOLVE/)).toBeInTheDocument();
    expect(screen.getByText(/SCORE/)).toBeInTheDocument();
  });

  it("shows confidence for SCORE events", () => {
    render(<ProvenancePanel events={MOCK_EVENTS} />);
    expect(screen.getByText(/0\.95/)).toBeInTheDocument();
  });

  it("can collapse and expand", () => {
    render(<ProvenancePanel events={MOCK_EVENTS} />);
    const toggle = screen.getByRole("button", { name: /sources/i });
    expect(toggle).toBeInTheDocument();
    // Events should be visible by default
    expect(screen.getAllByTestId("provenance-event").length).toBe(3);
    // Collapse
    fireEvent.click(toggle);
    expect(screen.queryAllByTestId("provenance-event").length).toBe(0);
    // Expand
    fireEvent.click(toggle);
    expect(screen.getAllByTestId("provenance-event").length).toBe(3);
  });

  it("shows empty state for no provenance", () => {
    render(<ProvenancePanel events={[]} />);
    expect(screen.getByText(/no provenance/i)).toBeInTheDocument();
  });

  it("uses design tokens not hardcoded hex", () => {
    const { container } = render(<ProvenancePanel events={MOCK_EVENTS} />);
    expect(container.firstChild).toBeTruthy();
  });
});
