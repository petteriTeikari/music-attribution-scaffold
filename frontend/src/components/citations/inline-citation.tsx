"use client";

/**
 * InlineCitation — Perplexity-like numbered citation badge.
 *
 * Small [N] badge that shows source details on hover.
 * Uses editorial design system: data-mono for number,
 * coral accent for hover, Plus Jakarta Sans for tooltip.
 */

import { useState, useId } from "react";
import type { CitationReference } from "@/lib/types/uncertainty";

interface InlineCitationProps {
  citation: CitationReference;
}

export function InlineCitation({ citation }: InlineCitationProps) {
  const [showTooltip, setShowTooltip] = useState(false);
  const tooltipId = useId();

  return (
    <span className="relative inline-block">
      <span
        role="doc-noteref"
        aria-label={`Citation ${citation.index}: ${citation.label}`}
        aria-describedby={tooltipId}
        className="inline-flex items-center justify-center cursor-pointer data-mono text-xs transition-colors duration-150 hover:opacity-80"
        style={{
          color: "var(--color-accent)",
          fontVariantNumeric: "tabular-nums",
        }}
        onMouseEnter={() => setShowTooltip(true)}
        onMouseLeave={() => setShowTooltip(false)}
        onFocus={() => setShowTooltip(true)}
        onBlur={() => setShowTooltip(false)}
        tabIndex={0}
      >
        [{citation.index}]
      </span>
      {showTooltip && (
        <span
          id={tooltipId}
          role="tooltip"
          className="absolute z-50 bottom-full left-1/2 -translate-x-1/2 mb-2 px-3 py-2 text-xs rounded whitespace-nowrap"
          style={{
            backgroundColor: "var(--color-surface-elevated)",
            color: "var(--color-heading)",
            border: "1px solid var(--color-border)",
            boxShadow: "0 2px 8px rgba(0,0,0,0.12)",
          }}
        >
          <span className="font-medium">{citation.label}</span>
          <span className="mx-1" style={{ color: "var(--color-muted)" }}>
            ·
          </span>
          <span style={{ color: "var(--color-accent)" }}>
            {Math.round(citation.confidence * 100)}%
          </span>
          <br />
          <span
            className="text-xs"
            style={{ color: "var(--color-muted)" }}
          >
            {citation.detail}
          </span>
        </span>
      )}
    </span>
  );
}
