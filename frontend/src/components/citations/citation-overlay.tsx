"use client";

import { useState } from "react";
import Image from "next/image";
import type { CitationRef } from "@/lib/data/citations";

interface CitationOverlayProps {
  title: string;
  marker: string;
  summary: string;
  detail: string;
  citationIds: number[];
  figurePlan: string;
  citations: CitationRef[];
  image?: string;
  imageAlt?: string;
}

export function CitationOverlay({
  title,
  marker,
  summary,
  detail,
  citationIds,
  figurePlan,
  citations,
  image,
  imageAlt,
}: CitationOverlayProps) {
  const [expanded, setExpanded] = useState(false);

  const citationLabel = `[${citationIds.join(", ")}]`;

  return (
    <div className="py-5">
      <div className="flex items-start gap-4">
        {/* Accent square + Roman numeral */}
        <div className="flex items-center gap-3 flex-shrink-0">
          <div className="accent-square" aria-hidden="true" />
          <span className="editorial-caps text-xs text-muted w-8 data-mono">
            {marker}
          </span>
        </div>

        {/* Content */}
        <div className="min-w-0 flex-1">
          <h3 className="text-xl font-semibold text-heading editorial-display">
            {title}
          </h3>

          <p className="mt-2 text-base text-body leading-relaxed max-w-2xl">
            {summary}{" "}
            <span className="text-xs text-accent data-mono font-medium">
              {citationLabel}
            </span>
          </p>

          {/* Read More / Close toggle */}
          {!expanded ? (
            <button
              onClick={() => setExpanded(true)}
              className="mt-3 editorial-caps text-xs text-accent underline underline-offset-2 hover:text-accent-hover transition-colors duration-150"
              aria-label="Read more"
            >
              Read More
            </button>
          ) : (
            <div className="mt-4 pl-4 border-l-2 border-accent-muted">
              <p className="text-sm text-body leading-relaxed max-w-2xl">
                {detail}
              </p>

              {/* Topic figure */}
              {image ? (
                <div className="mt-4">
                  <Image
                    src={image}
                    alt={imageAlt || figurePlan}
                    width={1200}
                    height={900}
                    sizes="(max-width: 768px) 100vw, 640px"
                    className="w-full h-auto"
                  />
                </div>
              ) : (
                <div className="mt-4 border border-dashed border-border p-4">
                  <span className="editorial-caps text-xs text-muted block mb-2">
                    Planned Infographic
                  </span>
                  <p className="text-xs text-label leading-relaxed">
                    {figurePlan}
                  </p>
                </div>
              )}

              {/* Inline citation details */}
              <div className="mt-3 space-y-1">
                {citationIds.map((id) => {
                  const ref = citations.find((c) => c.id === id);
                  if (!ref) return null;
                  return (
                    <p key={id} className="text-xs text-muted data-mono">
                      [{ref.id}] {ref.authors} ({ref.year}). &ldquo;{ref.title}&rdquo;{" "}
                      <span className="text-label">{ref.venue}</span>
                      {ref.url && (
                        <>
                          {" "}
                          <a
                            href={ref.url}
                            target="_blank"
                            rel="noopener noreferrer"
                            className="text-primary underline underline-offset-2 hover:text-primary-hover"
                          >
                            Link
                          </a>
                        </>
                      )}
                    </p>
                  );
                })}
              </div>

              <button
                onClick={() => setExpanded(false)}
                className="mt-3 editorial-caps text-xs text-muted underline underline-offset-2 hover:text-heading transition-colors duration-150"
                aria-label="Close"
              >
                Close
              </button>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
