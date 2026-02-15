"use client";

/**
 * ConsentQueryFlow — Animated SVG showing the MCP consent delegation chain.
 *
 * Demonstrates how a permission query flows from REQUESTER → DELEGATE → MANAGER → OWNER.
 * Uses anime.js for a pulse animation along the chain path.
 * Respects `prefers-reduced-motion` — shows static chain when motion is reduced.
 */

import { useRef, useEffect, useCallback } from "react";

interface ChainNode {
  role: string;
  name: string;
  x: number;
}

const CHAIN_NODES: ChainNode[] = [
  { role: "OWNER", name: "Imogen Heap", x: 100 },
  { role: "MANAGER", name: "Megaphonic", x: 300 },
  { role: "DELEGATE", name: "Auracles", x: 500 },
  { role: "REQUESTER", name: "Platform", x: 700 },
];

const NODE_RADIUS = 6;
const Y_CENTER = 40;

export function ConsentQueryFlow() {
  const svgRef = useRef<SVGSVGElement>(null);
  const pulseRef = useRef<SVGCircleElement>(null);
  const hasAnimated = useRef(false);

  const startAnimation = useCallback(async () => {
    if (hasAnimated.current || !pulseRef.current) return;

    // Check reduced motion preference
    if (typeof window !== "undefined" && window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
      return;
    }

    hasAnimated.current = true;

    try {
      const { createTimeline } = await import("animejs");
      const tl = createTimeline({
        defaults: { duration: 375 },
      });

      // Animate pulse from REQUESTER (right) to OWNER (left)
      for (let i = CHAIN_NODES.length - 1; i >= 0; i--) {
        tl.add(pulseRef.current, {
          cx: CHAIN_NODES[i].x,
          opacity: [0.3, 1],
        });
      }
    } catch {
      // animejs not available — degrade gracefully
    }
  }, []);

  useEffect(() => {
    if (typeof IntersectionObserver === "undefined") return;

    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          startAnimation();
          observer.disconnect();
        }
      },
      { threshold: 0.5 },
    );

    if (svgRef.current) {
      observer.observe(svgRef.current);
    }

    return () => observer.disconnect();
  }, [startAnimation]);

  return (
    <div className="py-4">
      <span className="editorial-caps text-xs text-accent block mb-3">
        Consent Query Flow
      </span>
      <svg
        ref={svgRef}
        role="img"
        aria-label="Consent query flow showing how permission requests travel through the delegation chain: Requester to Delegate to Manager to Owner"
        viewBox="0 0 800 80"
        className="w-full"
        style={{ maxWidth: 800 }}
      >
        {/* Connection lines */}
        {CHAIN_NODES.slice(0, -1).map((node, i) => (
          <line
            key={`line-${node.role}`}
            x1={node.x + NODE_RADIUS}
            y1={Y_CENTER}
            x2={CHAIN_NODES[i + 1].x - NODE_RADIUS}
            y2={Y_CENTER}
            stroke="var(--color-border)"
            strokeWidth="1"
            strokeDasharray="4 3"
          />
        ))}

        {/* Arrow heads */}
        {CHAIN_NODES.slice(0, -1).map((node, i) => {
          const midX = (node.x + CHAIN_NODES[i + 1].x) / 2;
          return (
            <polygon
              key={`arrow-${node.role}`}
              points={`${midX - 4},${Y_CENTER - 3} ${midX + 4},${Y_CENTER} ${midX - 4},${Y_CENTER + 3}`}
              fill="var(--color-accent)"
              opacity={0.6}
            />
          );
        })}

        {/* Node circles */}
        {CHAIN_NODES.map((node) => (
          <circle
            key={`node-${node.role}`}
            cx={node.x}
            cy={Y_CENTER}
            r={NODE_RADIUS}
            fill="var(--color-surface-elevated)"
            stroke="var(--color-accent)"
            strokeWidth="1.5"
          />
        ))}

        {/* Role labels (above) */}
        {CHAIN_NODES.map((node) => (
          <text
            key={`role-${node.role}`}
            x={node.x}
            y={Y_CENTER - 16}
            textAnchor="middle"
            className="editorial-caps"
            style={{
              fontSize: 9,
              fill: "var(--color-heading)",
              letterSpacing: "0.1em",
            }}
          >
            {node.role}
          </text>
        ))}

        {/* Entity names (below) */}
        {CHAIN_NODES.map((node) => (
          <text
            key={`name-${node.role}`}
            x={node.x}
            y={Y_CENTER + 24}
            textAnchor="middle"
            style={{
              fontSize: 10,
              fill: "var(--color-muted)",
            }}
          >
            {node.name}
          </text>
        ))}

        {/* Animated pulse dot — starts at REQUESTER position */}
        <circle
          ref={pulseRef}
          cx={CHAIN_NODES[CHAIN_NODES.length - 1].x}
          cy={Y_CENTER}
          r={4}
          fill="var(--color-accent)"
          opacity={0}
        />
      </svg>
    </div>
  );
}
