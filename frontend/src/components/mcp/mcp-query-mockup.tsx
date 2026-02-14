"use client";

import { useState, useEffect, useRef } from "react";
import { MCP_SCENARIOS } from "@/lib/data/mock-permissions";
import type { MCPScenario } from "@/lib/data/mock-permissions";
import { PlatformBadge } from "@/components/ui/platform-badge";

type AnimationPhase = "idle" | "request" | "checking" | "response";

const CATEGORY_LABELS: Record<MCPScenario["category"], string> = {
  ai_generator: "AI Generators",
  llm_provider: "LLM Providers",
  attribution: "Attribution & Certification",
  individual: "Individual",
};

const CATEGORY_ORDER: MCPScenario["category"][] = [
  "ai_generator",
  "llm_provider",
  "attribution",
  "individual",
];

export function MCPQueryMockup() {
  const [activeCategory, setActiveCategory] = useState<
    "all" | MCPScenario["category"]
  >("all");
  const [activeScenarioId, setActiveScenarioId] = useState(
    MCP_SCENARIOS[0].id,
  );
  const [phase, setPhase] = useState<AnimationPhase>("idle");
  const timerRef = useRef<NodeJS.Timeout | null>(null);

  const filteredScenarios =
    activeCategory === "all"
      ? MCP_SCENARIOS
      : MCP_SCENARIOS.filter((s) => s.category === activeCategory);

  const scenario =
    filteredScenarios.find((s) => s.id === activeScenarioId) ??
    filteredScenarios[0];

  function runAnimation() {
    const prefersReduced = window.matchMedia(
      "(prefers-reduced-motion: reduce)",
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

  function handleScenarioChange(id: string) {
    if (timerRef.current) clearTimeout(timerRef.current);
    setActiveScenarioId(id);
    setPhase("idle");
  }

  function handleCategoryChange(cat: "all" | MCPScenario["category"]) {
    setActiveCategory(cat);
    const newFiltered =
      cat === "all"
        ? MCP_SCENARIOS
        : MCP_SCENARIOS.filter((s) => s.category === cat);
    if (newFiltered.length > 0 && !newFiltered.find((s) => s.id === activeScenarioId)) {
      setActiveScenarioId(newFiltered[0].id);
    }
    setPhase("idle");
  }

  const resultColorVar =
    scenario.result === "DENY"
      ? "var(--color-permission-deny)"
      : scenario.result === "ASK"
        ? "var(--color-permission-ask)"
        : "var(--color-permission-allow)";

  // Detect the Jen vs VoiceClone contrast pair
  const isContrastPair =
    scenario.id === "scenario-3" || scenario.id === "scenario-4";

  return (
    <div>
      {/* Category filter tabs — editorial underline style */}
      <div className="mb-4 flex items-center gap-4 border-b border-divider pb-2">
        <button
          onClick={() => handleCategoryChange("all")}
          className={`editorial-caps pb-1 text-xs transition-colors duration-150 border-b-2 ${
            activeCategory === "all"
              ? "border-accent text-heading"
              : "border-transparent text-label hover:text-heading"
          }`}
        >
          All
        </button>
        {CATEGORY_ORDER.map((cat) => (
          <button
            key={cat}
            onClick={() => handleCategoryChange(cat)}
            className={`editorial-caps pb-1 text-xs transition-colors duration-150 border-b-2 ${
              activeCategory === cat
                ? "border-accent text-heading"
                : "border-transparent text-label hover:text-heading"
            }`}
          >
            {CATEGORY_LABELS[cat]}
          </button>
        ))}
      </div>

      {/* Scenario buttons */}
      <div className="mb-4 flex flex-wrap gap-2">
        {filteredScenarios.map((s) => (
          <button
            key={s.id}
            onClick={() => handleScenarioChange(s.id)}
            className={`flex items-center gap-2 rounded-md px-3 py-2 text-xs font-medium transition-colors duration-150 ${
              s.id === scenario.id
                ? "bg-primary text-white"
                : "border border-border text-label hover:bg-surface-secondary"
            }`}
          >
            {s.id !== scenario.id && (
              <PlatformBadge type={s.requester_type} />
            )}
            <span>{s.title}</span>
          </button>
        ))}
      </div>

      {/* Description + platform badge */}
      <div className="mb-4 flex items-start gap-3">
        <PlatformBadge type={scenario.requester_type} className="mt-0.5" />
        <p className="text-sm text-body">{scenario.description}</p>
      </div>

      {/* Contrast callout for Jen vs VoiceClone pair */}
      {isContrastPair && (
        <div
          className="mb-4 border-l-2 py-2 pl-3 text-xs text-label"
          style={{ borderColor: "var(--color-accent)" }}
        >
          Compare scenarios 3 & 4: same permission type (VOICE_CLONING),
          different results based on requester identity and Auracles authorization.
        </div>
      )}

      {/* Split panel */}
      <div className="grid gap-4 md:grid-cols-2">
        {/* Request panel */}
        <div className="rounded-lg border border-border bg-surface-elevated p-4">
          <div className="mb-3 flex items-center justify-between">
            <span className="text-xs font-semibold uppercase tracking-wider text-primary">
              AI Request
            </span>
            <span className="text-xs text-muted">{scenario.requester}</span>
          </div>
          <pre
            className="overflow-x-auto rounded-md bg-surface-secondary p-3 text-xs leading-relaxed"
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
                <span className="text-sm">Checking permissions...</span>
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
