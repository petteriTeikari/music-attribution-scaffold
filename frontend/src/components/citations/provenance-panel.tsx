"use client";

/**
 * ProvenancePanel — Collapsible panel showing full provenance chain.
 *
 * Inspired by Perplexity's "Sources" panel. Shows chronological list
 * of provenance events with event type badges, confidence values,
 * and optional uncertainty decomposition.
 *
 * Uses editorial design: horizontal rows with accent line dividers,
 * data-mono for numbers, editorial-caps for labels.
 */

import { useState } from "react";
import type { ProvenanceEvent } from "@/lib/types/attribution";
import { formatDate } from "@/lib/utils/format";

interface ProvenancePanelProps {
  events: ProvenanceEvent[];
  defaultExpanded?: boolean;
}

const formatTimestamp = formatDate;

function EventTypeBadge({ type }: { type: string }) {
  return (
    <span
      className="editorial-caps text-xs px-2 py-0.5 rounded"
      style={{
        backgroundColor: "var(--color-surface-tertiary)",
        color: "var(--color-muted)",
      }}
    >
      {type}
    </span>
  );
}

function EventRow({ event }: { event: ProvenanceEvent }) {
  const isScore = event.details.type === "score";
  const confidence =
    isScore && "new_confidence" in event.details
      ? event.details.new_confidence
      : null;

  return (
    <div
      data-testid="provenance-event"
      className="flex items-start gap-3 py-3"
      style={{ borderBottom: "1px solid var(--color-border)" }}
    >
      <div className="flex-shrink-0 pt-0.5">
        <EventTypeBadge type={event.event_type} />
      </div>
      <div className="flex-grow min-w-0">
        <div className="text-sm" style={{ color: "var(--color-heading)" }}>
          {event.agent}
        </div>
        <div
          className="text-xs mt-0.5"
          style={{ color: "var(--color-muted)" }}
        >
          {formatTimestamp(event.timestamp)}
        </div>
      </div>
      {confidence !== null && (
        <div
          className="flex-shrink-0 data-mono text-sm font-medium"
          style={{ color: "var(--color-accent)" }}
        >
          {confidence.toFixed(2)}
        </div>
      )}
      {event.citation_index !== null && (
        <div
          className="flex-shrink-0 data-mono text-xs"
          style={{ color: "var(--color-muted)" }}
        >
          [{event.citation_index}]
        </div>
      )}
    </div>
  );
}

export function ProvenancePanel({
  events,
  defaultExpanded = true,
}: ProvenancePanelProps) {
  const [expanded, setExpanded] = useState(defaultExpanded);

  if (events.length === 0) {
    return (
      <div
        className="py-4 text-sm text-center"
        style={{ color: "var(--color-muted)" }}
      >
        No provenance data available
      </div>
    );
  }

  return (
    <div>
      <button
        onClick={() => setExpanded(!expanded)}
        className="flex items-center gap-2 w-full py-2 text-left"
        style={{ color: "var(--color-heading)" }}
        aria-expanded={expanded}
      >
        <span className="editorial-caps text-xs">Sources</span>
        <span
          className="text-xs"
          style={{ color: "var(--color-muted)" }}
        >
          ({events.length})
        </span>
        <span
          className="ml-auto text-xs transition-transform duration-150"
          style={{
            transform: expanded ? "rotate(180deg)" : "rotate(0deg)",
            color: "var(--color-muted)",
          }}
        >
          ▼
        </span>
      </button>
      {expanded && (
        <div>
          {events.map((event, i) => (
            <EventRow key={`${event.timestamp}-${i}`} event={event} />
          ))}
        </div>
      )}
    </div>
  );
}
