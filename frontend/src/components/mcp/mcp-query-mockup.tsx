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
      <div className="mb-[var(--space-4)] flex flex-wrap gap-[var(--space-2)]">
        {MCP_SCENARIOS.map((s, i) => (
          <button
            key={s.id}
            onClick={() => handleScenarioChange(i)}
            className={`rounded-[var(--radius-md)] px-[var(--space-3)] py-[var(--space-2)] text-[var(--text-xs)] font-medium transition-colors duration-[var(--transition-fast)] ${
              i === activeScenario
                ? "bg-[var(--color-primary)] text-white"
                : "border border-[var(--color-border)] text-[var(--color-label)] hover:bg-[var(--color-surface-secondary)]"
            }`}
          >
            {s.title}
          </button>
        ))}
      </div>

      <p className="mb-[var(--space-4)] text-[var(--text-sm)] text-[var(--color-body)]">
        {scenario.description}
      </p>

      {/* Split panel */}
      <div className="grid gap-[var(--space-4)] md:grid-cols-2">
        {/* Request panel */}
        <div className="rounded-[var(--radius-lg)] border border-[var(--color-border)] bg-[var(--color-surface-elevated)] p-[var(--space-4)]">
          <div className="mb-[var(--space-3)] flex items-center justify-between">
            <span className="text-[var(--text-xs)] font-semibold uppercase tracking-wider text-[var(--color-primary)]">
              AI Request
            </span>
            <span className="text-[var(--text-xs)] text-[var(--color-muted)]">
              {scenario.requester}
            </span>
          </div>
          <pre className="overflow-x-auto rounded-[var(--radius-md)] bg-[var(--color-surface-secondary)] p-[var(--space-3)] text-[var(--text-xs)] leading-relaxed"
            style={{ fontFamily: "var(--font-mono)" }}
          >
            {JSON.stringify(scenario.mcpRequest, null, 2)}
          </pre>
        </div>

        {/* Response panel */}
        <div className="rounded-[var(--radius-lg)] border border-[var(--color-border)] bg-[var(--color-surface-elevated)] p-[var(--space-4)]">
          <div className="mb-[var(--space-3)] flex items-center justify-between">
            <span
              className="text-[var(--text-xs)] font-semibold uppercase tracking-wider"
              style={{ color: resultColorVar }}
            >
              MCP Response
            </span>
            {phase === "response" && (
              <span
                className="rounded-[var(--radius-full)] px-[var(--space-2)] py-[var(--space-1)] text-[var(--text-xs)] font-medium"
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
                className="rounded-[var(--radius-md)] bg-[var(--color-primary)] px-[var(--space-6)] py-[var(--space-3)] text-[var(--text-sm)] font-medium text-white hover:bg-[var(--color-primary-hover)] transition-colors duration-[var(--transition-fast)]"
              >
                Run Query
              </button>
            </div>
          ) : phase === "request" ? (
            <div className="flex h-32 items-center justify-center">
              <div className="flex items-center gap-[var(--space-2)] text-[var(--color-primary)]">
                <span className="inline-block h-2 w-2 animate-pulse rounded-full bg-current" />
                <span className="text-[var(--text-sm)]">Sending request...</span>
              </div>
            </div>
          ) : phase === "checking" ? (
            <div className="flex h-32 items-center justify-center">
              <div className="flex items-center gap-[var(--space-2)] text-[var(--color-accent)]">
                <span className="inline-block h-2 w-2 animate-pulse rounded-full bg-current" />
                <span className="text-[var(--text-sm)]">
                  Checking permissions...
                </span>
              </div>
            </div>
          ) : (
            <pre
              className="overflow-x-auto rounded-[var(--radius-md)] bg-[var(--color-surface-secondary)] p-[var(--space-3)] text-[var(--text-xs)] leading-relaxed"
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
