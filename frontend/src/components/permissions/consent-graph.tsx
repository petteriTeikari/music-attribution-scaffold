"use client";

/**
 * ConsentGraph — Interactive D3 force-directed graph showing
 * how consent queries propagate through the ecosystem.
 *
 * Nodes: Artist (center), 3 consent groups, N platforms from audit log.
 * Links: Platform → Group, colored by result (allow/ask/deny).
 * Interactions: Filter by result type, hover to highlight.
 */

import { useRef, useEffect, useState, useMemo, useCallback } from "react";
import type { AuditLogEntry } from "@/lib/types/permissions";
import { buildGraphData, type GraphNode, type GraphLink } from "@/lib/permissions/graph-data";

type ResultFilter = "all" | "allow" | "ask" | "deny";

interface ConsentGraphProps {
  auditLog: AuditLogEntry[];
}

const WIDTH = 600;
const HEIGHT = 400;

function isAllowResult(result: string): boolean {
  return result === "ALLOW" || result === "ALLOW_WITH_ATTRIBUTION" || result === "ALLOW_WITH_ROYALTY";
}

function getLinkColor(result: string): string {
  if (result === "core") return "var(--color-border)";
  if (result === "DENY") return "var(--color-permission-deny)";
  if (result === "ASK") return "var(--color-permission-ask)";
  if (isAllowResult(result)) return "var(--color-permission-allow)";
  return "var(--color-muted)";
}

function getLinkDash(result: string): string {
  if (result === "DENY") return "4 3";
  if (result === "ASK") return "2 2";
  return "none";
}

function getNodeRadius(type: string): number {
  if (type === "artist") return 20;
  if (type === "group") return 14;
  return 8;
}

function getNodeColor(type: string): string {
  if (type === "artist") return "var(--color-accent)";
  if (type === "group") return "var(--color-primary)";
  return "var(--color-teal)";
}

function matchesFilter(result: string, filter: ResultFilter): boolean {
  if (filter === "all") return true;
  if (filter === "allow") return isAllowResult(result);
  return result.toUpperCase() === filter.toUpperCase();
}

export function ConsentGraph({ auditLog }: ConsentGraphProps) {
  const svgRef = useRef<SVGSVGElement>(null);
  const [filter, setFilter] = useState<ResultFilter>("all");
  const [hoveredNode, setHoveredNode] = useState<string | null>(null);
  const [positions, setPositions] = useState<Map<string, { x: number; y: number }>>(new Map());

  const { nodes, links } = useMemo(() => buildGraphData(auditLog), [auditLog]);

  // Initialize static positions (radial layout as fallback, d3 simulation for real)
  useEffect(() => {
    const posMap = new Map<string, { x: number; y: number }>();
    const cx = WIDTH / 2;
    const cy = HEIGHT / 2;

    // Place artist at center
    posMap.set("artist", { x: cx, y: cy });

    // Place groups in inner ring
    const groupNodes = nodes.filter((n) => n.type === "group");
    groupNodes.forEach((node, i) => {
      const angle = (2 * Math.PI * i) / groupNodes.length - Math.PI / 2;
      posMap.set(node.id, {
        x: cx + Math.cos(angle) * 100,
        y: cy + Math.sin(angle) * 100,
      });
    });

    // Place platforms in outer ring
    const platformNodes = nodes.filter((n) => n.type === "platform");
    platformNodes.forEach((node, i) => {
      const angle = (2 * Math.PI * i) / platformNodes.length - Math.PI / 2;
      posMap.set(node.id, {
        x: cx + Math.cos(angle) * 170,
        y: cy + Math.sin(angle) * 170,
      });
    });

    setPositions(posMap);

    // Run D3 force simulation if available
    import("d3").then((d3) => {
      const simNodes = nodes.map((n) => ({
        ...n,
        x: posMap.get(n.id)?.x ?? cx,
        y: posMap.get(n.id)?.y ?? cy,
        fx: n.id === "artist" ? cx : undefined,
        fy: n.id === "artist" ? cy : undefined,
      }));

      const simLinks = links.map((l) => ({ ...l }));

      const simulation = d3.forceSimulation(simNodes)
        .force("link", d3.forceLink(simLinks).id((d) => (d as unknown as { id: string }).id).distance(80))
        .force("charge", d3.forceManyBody().strength(-200))
        .force("center", d3.forceCenter(cx, cy))
        .force("collide", d3.forceCollide().radius(25));

      simulation.on("tick", () => {
        const newPos = new Map<string, { x: number; y: number }>();
        for (const node of simNodes) {
          // Clamp to viewport
          const x = Math.max(30, Math.min(WIDTH - 30, node.x ?? cx));
          const y = Math.max(30, Math.min(HEIGHT - 30, node.y ?? cy));
          newPos.set(node.id, { x, y });
        }
        setPositions(new Map(newPos));
      });

      // Stop after settling
      setTimeout(() => simulation.stop(), 3000);

      return () => simulation.stop();
    }).catch(() => {
      // D3 not available — static layout is fine
    });
  }, [nodes, links]);

  const filteredLinks = useMemo(() => {
    return links.filter(
      (l) => l.result === "core" || matchesFilter(l.result, filter),
    );
  }, [links, filter]);

  const activeNodeIds = useMemo(() => {
    const ids = new Set<string>(["artist", "group-ai", "group-dist", "group-creative"]);
    for (const link of filteredLinks) {
      ids.add(typeof link.source === "string" ? link.source : "");
      ids.add(typeof link.target === "string" ? link.target : "");
    }
    return ids;
  }, [filteredLinks]);

  const handleNodeHover = useCallback((nodeId: string | null) => {
    setHoveredNode(nodeId);
  }, []);

  return (
    <div>
      {/* Screen reader summary */}
      <p className="sr-only">
        Interactive consent propagation graph showing how {nodes.filter((n) => n.type === "platform").length} platforms
        connect to 3 consent groups through the artist&apos;s permission profile.
      </p>

      {/* Filter buttons */}
      <div className="flex items-center gap-2 mb-4">
        <span className="editorial-caps text-xs text-label">Filter:</span>
        {(["all", "allow", "ask", "deny"] as ResultFilter[]).map((f) => (
          <button
            key={f}
            onClick={() => setFilter(f)}
            className={`editorial-caps text-xs px-2 py-1 transition-colors duration-150 ${
              filter === f
                ? "text-heading border-b border-accent"
                : "text-muted hover:text-heading"
            }`}
          >
            {f.charAt(0).toUpperCase() + f.slice(1)}
          </button>
        ))}
      </div>

      {/* SVG graph */}
      <svg
        ref={svgRef}
        role="img"
        aria-label="Consent propagation graph showing platform queries to artist permission groups"
        viewBox={`0 0 ${WIDTH} ${HEIGHT}`}
        className="w-full border border-border"
        style={{ maxWidth: WIDTH, backgroundColor: "var(--color-surface-secondary)" }}
      >
        {/* Links */}
        {filteredLinks.map((link, i) => {
          const sourcePos = positions.get(typeof link.source === "string" ? link.source : "");
          const targetPos = positions.get(typeof link.target === "string" ? link.target : "");
          if (!sourcePos || !targetPos) return null;
          const isHighlighted =
            hoveredNode === link.source || hoveredNode === link.target;

          return (
            <line
              key={`link-${i}`}
              x1={sourcePos.x}
              y1={sourcePos.y}
              x2={targetPos.x}
              y2={targetPos.y}
              stroke={getLinkColor(link.result)}
              strokeWidth={isHighlighted ? 2 : 1}
              strokeDasharray={getLinkDash(link.result)}
              opacity={hoveredNode && !isHighlighted ? 0.2 : 0.7}
            />
          );
        })}

        {/* Nodes */}
        {nodes
          .filter((n) => activeNodeIds.has(n.id))
          .map((node) => {
            const pos = positions.get(node.id);
            if (!pos) return null;
            const r = getNodeRadius(node.type);
            const isHovered = hoveredNode === node.id;

            return (
              <g
                key={node.id}
                onMouseEnter={() => handleNodeHover(node.id)}
                onMouseLeave={() => handleNodeHover(null)}
                style={{ cursor: "pointer" }}
              >
                <circle
                  cx={pos.x}
                  cy={pos.y}
                  r={r}
                  fill={getNodeColor(node.type)}
                  stroke={isHovered ? "var(--color-heading)" : "none"}
                  strokeWidth={isHovered ? 2 : 0}
                  opacity={hoveredNode && !isHovered ? 0.4 : 1}
                />
                <text
                  x={pos.x}
                  y={pos.y + r + 12}
                  textAnchor="middle"
                  style={{
                    fontSize: node.type === "platform" ? 8 : 10,
                    fill: "var(--color-body)",
                  }}
                  opacity={hoveredNode && !isHovered ? 0.3 : 1}
                >
                  {node.label}
                </text>
              </g>
            );
          })}
      </svg>

      {/* Legend */}
      <div className="flex items-center gap-4 mt-3 text-xs text-muted">
        <span className="flex items-center gap-1">
          <span
            className="inline-block h-2.5 w-2.5 rounded-full"
            style={{ backgroundColor: "var(--color-accent)" }}
          />
          Artist
        </span>
        <span className="flex items-center gap-1">
          <span
            className="inline-block h-2.5 w-2.5 rounded-full"
            style={{ backgroundColor: "var(--color-primary)" }}
          />
          Group
        </span>
        <span className="flex items-center gap-1">
          <span
            className="inline-block h-2.5 w-2.5 rounded-full"
            style={{ backgroundColor: "var(--color-teal)" }}
          />
          Platform
        </span>
        <span className="text-muted">|</span>
        <span className="flex items-center gap-1">
          <span className="inline-block w-4 border-t" style={{ borderColor: "var(--color-permission-allow)" }} />
          Allow
        </span>
        <span className="flex items-center gap-1">
          <span className="inline-block w-4 border-t border-dashed" style={{ borderColor: "var(--color-permission-ask)" }} />
          Ask
        </span>
        <span className="flex items-center gap-1">
          <span className="inline-block w-4 border-t border-dashed" style={{ borderColor: "var(--color-permission-deny)" }} />
          Deny
        </span>
      </div>
    </div>
  );
}
