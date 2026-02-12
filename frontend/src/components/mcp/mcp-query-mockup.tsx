"use client";

import { useState, useEffect, useRef } from "react";
import { MCP_SCENARIOS } from "@/lib/data/mock-permissions";

type AnimationPhase = "idle" | "request" | "checking" | "response";

export function MCPQueryMockup() {
  const [activeScenario, setActiveScenario] = useState(0);
  const [phase, setPhase] = useState<AnimationPhase>("idle");
  const timerRef = useRef<NodeJS.Timeout | null>(null);

  const scenario = MCP_SCENARIOS[activeScenario];

  function runAnimation() {
    // Check prefers-reduced-motion
    const prefersReduced = window.matchMedia(
      "(prefers-reduced-motion: reduce)"
    ).matches;

    if (prefersReduced) {
      setPhase("response");
      return;
    }

    setPhase("request");
    timerRef.current = setTimeout(() => {
      setPhase("checking");
      timerRef.current = setTimeout(() => {
        setPhase("response");
      }, 800);
    }, 600);
  }

  useEffect(() => {
    return () => {
      if (timerRef.current) clearTimeout(timerRef.current);
    };
  }, []);

  function handleScenarioChange(index: number) {
    if (timerRef.current) clearTimeout(timerRef.current);
    setActiveScenario(index);
    setPhase("idle");
  }

  const resultColorVar =
    scenario.result === "DENY"
      ? "var(--color-permission-deny)"
      : scenario.result === "ASK"
        ? "var(--color-permission-ask)"
        : "var(--color-permission-allow)";

  return (
    <div>
      {/* Scenario tabs */}
      <div className="mb-4 flex flex-wrap gap-2">
        {MCP_SCENARIOS.map((s, i) => (
          <button
            key={s.id}
            onClick={() => handleScenarioChange(i)}
            className={`rounded-md px-3 py-2 text-xs font-medium transition-colors duration-150 ${
              i === activeScenario
                ? "bg-primary text-white"
                : "border border-border text-label hover:bg-surface-secondary"
            }`}
          >
            {s.title}
          </button>
        ))}
      </div>

      <p className="mb-4 text-sm text-body">
        {scenario.description}
      </p>

      {/* Split panel */}
      <div className="grid gap-4 md:grid-cols-2">
        {/* Request panel */}
        <div className="rounded-lg border border-border bg-surface-elevated p-4">
          <div className="mb-3 flex items-center justify-between">
            <span className="text-xs font-semibold uppercase tracking-wider text-primary">
              AI Request
            </span>
            <span className="text-xs text-muted">
              {scenario.requester}
            </span>
          </div>
          <pre className="overflow-x-auto rounded-md bg-surface-secondary p-3 text-xs leading-relaxed"
            style={{ fontFamily: "var(--font-mono)" }}
          >
            {JSON.stringify(scenario.mcpRequest, null, 2)}
          </pre>
        </div>

        {/* Response panel */}
        <div className="rounded-lg border border-border bg-surface-elevated p-4">
          <div className="mb-3 flex items-center justify-between">
            <span
              className="text-xs font-semibold uppercase tracking-wider"
              style={{ color: resultColorVar }}
            >
              MCP Response
            </span>
            {phase === "response" && (
              <span
                className="rounded-full px-2 py-1 text-xs font-medium"
                style={{
                  backgroundColor: `color-mix(in srgb, ${resultColorVar} 12%, transparent)`,
                  color: resultColorVar,
                }}
              >
                {scenario.result.replace(/_/g, " ")}
              </span>
            )}
          </div>

          {phase === "idle" ? (
            <div className="flex h-32 items-center justify-center">
              <button
                onClick={runAnimation}
                className="rounded-md bg-primary px-6 py-3 text-sm font-medium text-white hover:bg-primary-hover transition-colors duration-150"
              >
                Run Query
              </button>
            </div>
          ) : phase === "request" ? (
            <div className="flex h-32 items-center justify-center">
              <div className="flex items-center gap-2 text-primary">
                <span className="inline-block h-2 w-2 animate-pulse rounded-full bg-current" />
                <span className="text-sm">Sending request...</span>
              </div>
            </div>
          ) : phase === "checking" ? (
            <div className="flex h-32 items-center justify-center">
              <div className="flex items-center gap-2 text-accent">
                <span className="inline-block h-2 w-2 animate-pulse rounded-full bg-current" />
                <span className="text-sm">
                  Checking permissions...
                </span>
              </div>
            </div>
          ) : (
            <pre
              className="overflow-x-auto rounded-md bg-surface-secondary p-3 text-xs leading-relaxed"
              style={{ fontFamily: "var(--font-mono)" }}
            >
              {JSON.stringify(scenario.mcpResponse, null, 2)}
            </pre>
          )}
        </div>
      </div>
    </div>
  );
}
