import { describe, it, expect } from "vitest";
import { render, screen } from "@testing-library/react";
import { ProvenanceTimeline } from "./provenance-timeline";
import type { ProvenanceEvent } from "@/lib/types/attribution";

const MOCK_EVENTS: ProvenanceEvent[] = [
  {
    event_type: "FETCH",
    timestamp: "2024-06-15T10:00:00Z",
    agent: "etl-musicbrainz-v2",
    details: {
      type: "fetch",
      source: "MUSICBRAINZ",
      source_id: "mb-rec-123",
      records_fetched: 15,
      rate_limited: false,
    },
    feedback_card_id: null,
    step_uncertainty: null,
    citation_index: null,
  },
  {
    event_type: "SCORE",
    timestamp: "2024-06-15T10:15:00Z",
    agent: "attribution-aggregator-v1",
    details: {
      type: "score",
      previous_confidence: null,
      new_confidence: 0.3,
      scoring_method: "weighted_source_agreement",
    },
    feedback_card_id: null,
    step_uncertainty: null,
    citation_index: null,
  },
];

describe("ProvenanceTimeline", () => {
  it("renders all events", () => {
    render(<ProvenanceTimeline events={MOCK_EVENTS} />);
    expect(screen.getByText(/FETCH/)).toBeInTheDocument();
    expect(screen.getByText(/SCORE/)).toBeInTheDocument();
  });

  it("shows fetch event description", () => {
    render(<ProvenanceTimeline events={MOCK_EVENTS} />);
    expect(screen.getByText(/Fetched 15 records/)).toBeInTheDocument();
  });

  it("shows score event with confidence", () => {
    render(<ProvenanceTimeline events={MOCK_EVENTS} />);
    const matches = screen.getAllByText(/30%/);
    expect(matches.length).toBeGreaterThanOrEqual(1);
  });

  it("shows empty state for no events", () => {
    render(<ProvenanceTimeline events={[]} />);
    expect(screen.getByText(/No provenance events/)).toBeInTheDocument();
  });

  it("renders agent names", () => {
    render(<ProvenanceTimeline events={MOCK_EVENTS} />);
    expect(screen.getByText("etl-musicbrainz-v2")).toBeInTheDocument();
  });
});
