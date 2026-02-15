"use client";

import { useState, useMemo, useRef, useEffect, useCallback } from "react";
import type { ProvenanceEvent } from "@/lib/types/attribution";

interface ProvenanceDagProps {
  events: ProvenanceEvent[];
  attributionId?: string;
  onExpand?: () => void;
}

/** Static horizontal layout — X = time position, Y = event type lane. */
const EVENT_LANES: Record<string, number> = {
  FETCH: 0,
  RESOLVE: 1,
  SCORE: 2,
  REVIEW: 3,
  UPDATE: 4,
  FEEDBACK: 5,
};

const LANE_COLORS: Record<string, string> = {
  FETCH: "var(--color-teal)",
  RESOLVE: "var(--color-primary)",
  SCORE: "var(--color-accent)",
  REVIEW: "var(--color-confidence-high)",
  UPDATE: "var(--color-muted)",
  FEEDBACK: "var(--color-confidence-medium)",
};

const NODE_RADIUS = 12;
const LANE_HEIGHT = 50;
const X_SPACING = 100;
const PADDING = { top: 30, right: 40, bottom: 20, left: 80 };

function getConfidenceLabel(event: ProvenanceEvent): string | null {
  if (event.details.type === "score") {
    return `${Math.round(event.details.new_confidence * 100)}%`;
  }
  return null;
}

function formatEventType(type: string): string {
  return type.charAt(0) + type.slice(1).toLowerCase();
}

/**
 * Provenance DAG — horizontal pipeline visualization.
 * Collapsed by default with "Show Pipeline" toggle.
 * Uses static layout (not force simulation) since provenance is chronological.
 */
export function ProvenanceDag({
  events,
  attributionId: _attributionId,
  onExpand,
}: ProvenanceDagProps) {
  const [expanded, setExpanded] = useState(false);
  const svgRef = useRef<SVGSVGElement>(null);
  const hasAnimated = useRef(false);

  const handleToggle = useCallback(() => {
    const next = !expanded;
    setExpanded(next);
    if (next && !hasAnimated.current) {
      hasAnimated.current = true;
      onExpand?.();
    }
  }, [expanded, onExpand]);

  // Compute node positions
  const layout = useMemo(() => {
    if (events.length === 0) return { nodes: [], edges: [], width: 0, height: 0 };

    const usedLanes = new Set(events.map((e) => EVENT_LANES[e.event_type] ?? 0));
    const laneCount = Math.max(...usedLanes) + 1;
    const width = PADDING.left + events.length * X_SPACING + PADDING.right;
    const height = PADDING.top + laneCount * LANE_HEIGHT + PADDING.bottom;

    const nodes = events.map((event, i) => ({
      event,
      x: PADDING.left + i * X_SPACING,
      y: PADDING.top + (EVENT_LANES[event.event_type] ?? 0) * LANE_HEIGHT,
      color: LANE_COLORS[event.event_type] ?? "var(--color-muted)",
    }));

    // Edges connect consecutive events
    const edges = nodes.slice(1).map((node, i) => ({
      x1: nodes[i].x,
      y1: nodes[i].y,
      x2: node.x,
      y2: node.y,
    }));

    return { nodes, edges, width, height };
  }, [events]);

  // Optional anime.js pulse animation on first expand
  useEffect(() => {
    if (!expanded || !svgRef.current) return;

    const prefersReducedMotion = globalThis.matchMedia?.(
      "(prefers-reduced-motion: reduce)",
    )?.matches;
    if (prefersReducedMotion) return;

    import("animejs")
      .then(({ animate }) => {
        const circles = svgRef.current?.querySelectorAll("[data-dag-node]");
        if (!circles?.length) return;

        animate(Array.from(circles), {
          r: [0, NODE_RADIUS],
          opacity: [0, 1],
          duration: 400,
          delay: (_target: unknown, i: number) => i * 80,
          ease: "outQuad",
        });
      })
      .catch(() => {
        // anime.js not available — no animation
      });
  }, [expanded]);

  if (events.length === 0) {
    return (
      <div data-testid="provenance-dag-empty">
        <p className="text-sm text-muted">
          No provenance events recorded.
        </p>
      </div>
    );
  }

  return (
    <div>
      <button
        onClick={handleToggle}
        className="editorial-caps text-xs text-accent underline underline-offset-2 mb-3"
        aria-expanded={expanded}
      >
        {expanded ? "Hide Pipeline" : "Show Pipeline"}
      </button>

      {expanded && (
        <svg
          ref={svgRef}
          role="img"
          aria-label={`Provenance pipeline with ${events.length} events`}
          viewBox={`0 0 ${layout.width} ${layout.height}`}
          className="w-full border border-border"
          style={{
            maxWidth: layout.width,
            backgroundColor: "var(--color-surface-secondary)",
          }}
        >
          {/* Lane labels */}
          {Object.entries(EVENT_LANES).map(([type, lane]) => {
            const y = PADDING.top + lane * LANE_HEIGHT;
            const hasEvents = events.some((e) => e.event_type === type);
            if (!hasEvents) return null;
            return (
              <text
                key={`lane-${type}`}
                x={8}
                y={y + 4}
                style={{
                  fontSize: 9,
                  fill: "var(--color-muted)",
                  fontFamily: "var(--font-mono)",
                }}
              >
                {formatEventType(type)}
              </text>
            );
          })}

          {/* Edges */}
          {layout.edges.map((edge, i) => (
            <line
              key={`edge-${i}`}
              x1={edge.x1}
              y1={edge.y1}
              x2={edge.x2}
              y2={edge.y2}
              stroke="var(--color-border)"
              strokeWidth={1}
              opacity={0.6}
            />
          ))}

          {/* Nodes */}
          {layout.nodes.map((node, i) => {
            const confLabel = getConfidenceLabel(node.event);
            return (
              <g key={`node-${i}`}>
                <circle
                  data-dag-node
                  cx={node.x}
                  cy={node.y}
                  r={NODE_RADIUS}
                  fill={node.color}
                  opacity={1}
                />
                {/* Confidence label below SCORE nodes */}
                {confLabel && (
                  <text
                    x={node.x}
                    y={node.y + NODE_RADIUS + 14}
                    textAnchor="middle"
                    style={{
                      fontSize: 10,
                      fill: node.color,
                      fontFamily: "var(--font-mono)",
                    }}
                  >
                    {confLabel}
                  </text>
                )}
              </g>
            );
          })}
        </svg>
      )}
    </div>
  );
}
