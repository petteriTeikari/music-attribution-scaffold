/**
 * Tests for ProvenanceDag component.
 */
import { describe, it, expect, vi, beforeEach } from "vitest";
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { ProvenanceDag } from "@/components/provenance/provenance-dag";
import type { ProvenanceEvent } from "@/lib/types/attribution";
import { ProvenanceEventType, Source } from "@/lib/types/enums";

// Mock anime.js v4
vi.mock("animejs", () => ({
  animate: vi.fn(),
}));

const MOCK_EVENTS: ProvenanceEvent[] = [
  {
    event_type: ProvenanceEventType.FETCH,
    timestamp: "2024-06-15T10:00:00Z",
    agent: "etl-musicbrainz-v2",
    details: {
      type: "fetch",
      source: Source.MUSICBRAINZ,
      source_id: "mb-rec-1",
      records_fetched: 4,
      rate_limited: false,
    },
    feedback_card_id: null,
    step_uncertainty: null,
    citation_index: null,
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
    citation_index: null,
  },
  {
    event_type: ProvenanceEventType.SCORE,
    timestamp: "2024-06-15T10:10:00Z",
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
  {
    event_type: ProvenanceEventType.SCORE,
    timestamp: "2024-07-01T14:30:00Z",
    agent: "attribution-aggregator-v1",
    details: {
      type: "score",
      previous_confidence: 0.3,
      new_confidence: 0.95,
      scoring_method: "bayesian_update_post_review",
    },
    feedback_card_id: null,
    step_uncertainty: null,
    citation_index: null,
  },
];

describe("ProvenanceDag", () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  it("renders collapsed by default with Show Pipeline button", () => {
    render(<ProvenanceDag events={MOCK_EVENTS} />);
    expect(screen.getByText("Show Pipeline")).toBeInTheDocument();
    expect(screen.queryByRole("img")).not.toBeInTheDocument();
  });

  it("expands to show SVG with correct node count", async () => {
    const user = userEvent.setup();
    render(<ProvenanceDag events={MOCK_EVENTS} />);
    await user.click(screen.getByText("Show Pipeline"));

    const svg = screen.getByRole("img");
    expect(svg).toBeInTheDocument();
    expect(svg).toHaveAttribute(
      "aria-label",
      "Provenance pipeline with 4 events",
    );

    // Should have 4 circle nodes
    const circles = svg.querySelectorAll("[data-dag-node]");
    expect(circles).toHaveLength(4);
  });

  it("displays confidence values on SCORE events", async () => {
    const user = userEvent.setup();
    render(<ProvenanceDag events={MOCK_EVENTS} />);
    await user.click(screen.getByText("Show Pipeline"));

    // SCORE events show confidence: 30% and 95%
    expect(screen.getByText("30%")).toBeInTheDocument();
    expect(screen.getByText("95%")).toBeInTheDocument();
  });

  it("shows empty state when no events", () => {
    render(<ProvenanceDag events={[]} />);
    expect(screen.getByTestId("provenance-dag-empty")).toBeInTheDocument();
    expect(
      screen.getByText("No provenance events recorded."),
    ).toBeInTheDocument();
  });

  it("collapses back with Hide Pipeline button", async () => {
    const user = userEvent.setup();
    render(<ProvenanceDag events={MOCK_EVENTS} />);
    await user.click(screen.getByText("Show Pipeline"));
    expect(screen.getByRole("img")).toBeInTheDocument();

    await user.click(screen.getByText("Hide Pipeline"));
    expect(screen.queryByRole("img")).not.toBeInTheDocument();
  });

  it("calls onExpand callback on first expand only", async () => {
    const user = userEvent.setup();
    const onExpand = vi.fn();
    render(<ProvenanceDag events={MOCK_EVENTS} onExpand={onExpand} />);

    await user.click(screen.getByText("Show Pipeline"));
    expect(onExpand).toHaveBeenCalledTimes(1);

    await user.click(screen.getByText("Hide Pipeline"));
    await user.click(screen.getByText("Show Pipeline"));
    // Should still only be called once
    expect(onExpand).toHaveBeenCalledTimes(1);
  });

  it("has aria-expanded attribute on toggle button", async () => {
    const user = userEvent.setup();
    render(<ProvenanceDag events={MOCK_EVENTS} />);

    const button = screen.getByText("Show Pipeline");
    expect(button).toHaveAttribute("aria-expanded", "false");

    await user.click(button);
    expect(screen.getByText("Hide Pipeline")).toHaveAttribute(
      "aria-expanded",
      "true",
    );
  });
});
