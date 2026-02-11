"use client";

import type { ProvenanceEvent } from "@/lib/types/attribution";
import { getSourceCssVar } from "@/lib/theme/confidence";

interface ProvenanceTimelineProps {
  events: ProvenanceEvent[];
  className?: string;
}

function formatTimestamp(iso: string): string {
  const date = new Date(iso);
  return date.toLocaleDateString("en-US", {
    month: "short",
    day: "numeric",
    year: "numeric",
  });
}

function getEventDescription(event: ProvenanceEvent): string {
  const { details } = event;
  switch (details.type) {
    case "fetch":
      return `Fetched ${details.records_fetched} records from ${details.source}`;
    case "resolve":
      return `Resolved ${details.records_input} records → ${details.entities_output} entities via ${details.method}`;
    case "score":
      if (details.previous_confidence !== null) {
        return `Score updated: ${Math.round(details.previous_confidence * 100)}% → ${Math.round(details.new_confidence * 100)}% (${details.scoring_method})`;
      }
      return `Initial score: ${Math.round(details.new_confidence * 100)}% (${details.scoring_method})`;
    case "review":
      return `Review applied ${details.corrections_applied} corrections`;
    case "update":
      return `Updated v${details.previous_version} → v${details.new_version}: ${details.fields_changed.join(", ")}`;
    case "feedback":
      return `Feedback: ${Math.round(details.overall_assessment * 100)}% assessment (${details.corrections_count} corrections${details.accepted ? ", accepted" : ""})`;
  }
}

function getEventColor(event: ProvenanceEvent): string {
  if (event.details.type === "fetch") {
    return getSourceCssVar((event.details as { source: string }).source);
  }
  const colorMap: Record<string, string> = {
    resolve: "var(--color-teal)",
    score: "var(--color-primary)",
    review: "var(--color-accent)",
    update: "var(--color-body)",
    feedback: "var(--color-confidence-medium)",
  };
  return colorMap[event.details.type] ?? "var(--color-muted)";
}

function getRunningConfidence(
  events: ProvenanceEvent[]
): (number | null)[] {
  return events.map((event) => {
    if (event.details.type === "score") {
      return event.details.new_confidence;
    }
    return null;
  });
}

export function ProvenanceTimeline({
  events,
  className = "",
}: ProvenanceTimelineProps) {
  const confidences = getRunningConfidence(events);

  if (events.length === 0) {
    return (
      <p className="text-[var(--text-sm)] text-[var(--color-muted)] italic">
        No provenance events recorded.
      </p>
    );
  }

  return (
    <div className={`relative ${className}`} aria-label="Provenance timeline">
      {/* Vertical accent line as timeline spine */}
      <div
        className="absolute left-[7px] top-0 bottom-0 accent-line-v"
        style={{ opacity: 0.4 }}
        aria-hidden="true"
      />

      <ol className="space-y-[var(--space-4)]">
        {events.map((event, index) => {
          const color = getEventColor(event);
          const confidence = confidences[index];

          return (
            <li key={`${event.timestamp}-${index}`} className="relative pl-[var(--space-8)]">
              {/* Timeline marker — accent square instead of dot */}
              <div
                className="absolute left-0 top-[var(--space-1)] accent-square-sm"
                style={{ backgroundColor: color }}
                aria-hidden="true"
              />

              <div className="border-b border-[var(--color-divider)] pb-[var(--space-3)]">
                <div className="flex items-start justify-between gap-[var(--space-2)]">
                  <div className="min-w-0 flex-1">
                    <div className="flex items-center gap-[var(--space-2)]">
                      <span
                        className="editorial-caps text-[var(--text-xs)]"
                        style={{ color }}
                      >
                        {event.event_type}
                      </span>
                      <span className="text-[var(--text-xs)] text-[var(--color-muted)]">
                        {event.agent}
                      </span>
                    </div>
                    <p className="mt-[var(--space-1)] text-[var(--text-sm)] text-[var(--color-body)]">
                      {getEventDescription(event)}
                    </p>
                  </div>

                  <div className="flex flex-col items-end gap-[var(--space-1)]">
                    <span className="text-[var(--text-xs)] text-[var(--color-muted)] whitespace-nowrap data-mono">
                      {formatTimestamp(event.timestamp)}
                    </span>
                    {confidence !== null && (
                      <span
                        className="editorial-display text-[var(--text-base)]"
                        style={{ color }}
                      >
                        {Math.round(confidence * 100)}%
                      </span>
                    )}
                  </div>
                </div>
              </div>
            </li>
          );
        })}
      </ol>
    </div>
  );
}
