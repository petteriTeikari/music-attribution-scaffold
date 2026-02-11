/**
 * Tests for Task 3.3: Wire citations into work detail page.
 *
 * Verifies that InlineCitation badges appear in credit-list.tsx
 * and ProvenancePanel is rendered on the work detail page.
 */

import { render, screen } from "@testing-library/react";
import { describe, it, expect } from "vitest";
import { CreditList } from "@/components/attribution/credit-list";
import { ProvenancePanel } from "@/components/citations/provenance-panel";
import type { Credit, ProvenanceEvent } from "@/lib/types/attribution";
import { AssuranceLevel, CreditRole, ProvenanceEventType, Source } from "@/lib/types/enums";

const MOCK_PROVENANCE: ProvenanceEvent[] = [
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
    event_type: ProvenanceEventType.FETCH,
    timestamp: "2024-06-15T10:01:00Z",
    agent: "etl-acoustid-v1",
    details: {
      type: "fetch",
      source: Source.ACOUSTID,
      source_id: "aid-001",
      records_fetched: 2,
      rate_limited: false,
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
      new_confidence: 0.92,
      scoring_method: "weighted_source_agreement",
    },
    feedback_card_id: null,
    step_uncertainty: null,
    citation_index: 3,
  },
];

const MOCK_CREDITS: Credit[] = [
  {
    entity_id: "ent-001",
    entity_name: "Imogen Heap",
    role: CreditRole.PERFORMER,
    role_detail: "Vocals, piano",
    confidence: 0.95,
    sources: [Source.MUSICBRAINZ, Source.ACOUSTID],
    assurance_level: AssuranceLevel.LEVEL_2,
  },
  {
    entity_id: "ent-002",
    entity_name: "Guy Sigsworth",
    role: CreditRole.PRODUCER,
    role_detail: null,
    confidence: 0.78,
    sources: [Source.MUSICBRAINZ],
    assurance_level: AssuranceLevel.LEVEL_1,
  },
];

describe("CreditList with citations", () => {
  it("shows citation badges when provenance events are provided", () => {
    render(
      <CreditList credits={MOCK_CREDITS} provenanceEvents={MOCK_PROVENANCE} />
    );
    // Citation [1] for MusicBrainz should appear (both credits have MB)
    expect(screen.getAllByText("[1]").length).toBeGreaterThanOrEqual(1);
  });

  it("shows citation badges matching credit sources", () => {
    render(
      <CreditList credits={MOCK_CREDITS} provenanceEvents={MOCK_PROVENANCE} />
    );
    // First credit has MUSICBRAINZ + ACOUSTID → should show [1] and [2]
    // Second credit has MUSICBRAINZ only → should show [1]
    // Total citation badges: at least 3 (2 for first credit + 1 for second)
    const badges = screen.getAllByRole("doc-noteref");
    expect(badges.length).toBe(3);
  });

  it("renders without citations when no provenance events provided", () => {
    render(<CreditList credits={MOCK_CREDITS} />);
    // Should render credits normally without citation badges
    expect(screen.getByText("Imogen Heap")).toBeInTheDocument();
    expect(screen.getByText("Guy Sigsworth")).toBeInTheDocument();
    expect(screen.queryByRole("doc-noteref")).toBeNull();
  });

  it("citation indexes match provenance event citation_index", () => {
    render(
      <CreditList credits={MOCK_CREDITS} provenanceEvents={MOCK_PROVENANCE} />
    );
    const badges = screen.getAllByRole("doc-noteref");
    // Extract citation indexes from badge aria-labels
    const indexes = badges.map((badge) => {
      const label = badge.getAttribute("aria-label") ?? "";
      const match = label.match(/Citation (\d+)/);
      return match ? parseInt(match[1], 10) : null;
    });
    // All citation indexes should exist in the provenance events
    const validIndexes = MOCK_PROVENANCE
      .filter((e) => e.citation_index !== null)
      .map((e) => e.citation_index);
    for (const idx of indexes) {
      expect(validIndexes).toContain(idx);
    }
  });
});

describe("Work detail page ProvenancePanel", () => {
  it("renders ProvenancePanel with events", () => {
    render(<ProvenancePanel events={MOCK_PROVENANCE} />);
    // Should show "Sources" header
    expect(screen.getByText(/sources/i)).toBeInTheDocument();
    // Should show provenance events
    const events = screen.getAllByTestId("provenance-event");
    expect(events.length).toBe(3);
  });

  it("works with empty provenance chain", () => {
    render(<ProvenancePanel events={[]} />);
    expect(screen.getByText(/no provenance/i)).toBeInTheDocument();
  });
});
