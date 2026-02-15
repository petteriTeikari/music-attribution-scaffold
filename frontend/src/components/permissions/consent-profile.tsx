"use client";

/**
 * ConsentProfile — Data-driven consent summary replacing static CategoryCards.
 *
 * Groups the 14-entry permission model into 3 editorial rows with
 * allow/ask/deny counts, exception callouts, and educational tooltips.
 */

import { useState, useId } from "react";
import type { PermissionEntry } from "@/lib/types/permissions";
import {
  buildConsentGroups,
  formatPermissionType,
  type ConsentGroup,
} from "@/lib/permissions/consent-groups";

interface ConsentProfileProps {
  permissions: PermissionEntry[];
}

export function ConsentProfile({ permissions }: ConsentProfileProps) {
  const groups = buildConsentGroups(permissions);

  return (
    <div className="mb-8">
      {/* Header */}
      <span className="editorial-caps text-xs text-accent block mb-4">
        Consent Profile
      </span>

      {/* Identity row */}
      <div className="py-4">
        <div className="flex items-baseline gap-2 flex-wrap">
          <span className="text-base font-semibold text-heading">
            Imogen Heap
          </span>
          <span className="text-xs text-label">·</span>
          <span className="text-xs font-medium" style={{ color: "var(--color-assurance-a3)" }}>
            A3 Identity-Verified
          </span>
        </div>
        <div className="mt-1 flex items-center gap-2 flex-wrap">
          <span className="data-mono text-xs" style={{ color: "var(--color-teal)" }}>
            Auracles ID: AU-2025-IH-0001
          </span>
          <InfoTooltip text="Auracles provides a unified digital identity for musicians — a single canonical source for permissions, metadata and samples. Connected platforms query this profile via MCP before any AI-related use of the artist's catalog." />
        </div>
        <div className="mt-1 text-xs text-muted">
          Default policy: <span className="font-medium text-heading">ASK</span> — explicit approval for unlisted uses
        </div>
        <div className="mt-2 flex items-center gap-2 flex-wrap">
          <span className="text-xs text-label">Connected:</span>
          <a
            href="https://auracles.io/soundcloud"
            target="_blank"
            rel="noopener noreferrer"
            className="text-xs font-medium underline underline-offset-2 decoration-1 transition-colors duration-150 hover:text-accent"
            style={{ color: "var(--color-teal)" }}
          >
            SoundCloud
          </a>
          <InfoTooltip text="SoundCloud connects directly to your Auracles profile. Permission settings automatically apply when platforms query your consent profile — SoundCloud has committed to not using artist content for generative AI training (2025 policy)." />
          <span className="text-xs text-muted">·</span>
          <span className="text-xs text-label">Spotify</span>
        </div>
      </div>

      <div className="accent-line" style={{ opacity: 0.2 }} />

      {/* Group rows */}
      {groups.map((group) => (
        <GroupRow key={group.roman} group={group} />
      ))}
    </div>
  );
}

function GroupRow({ group }: { group: ConsentGroup }) {
  return (
    <div className="py-4">
      <div className="flex items-center justify-between gap-4">
        <div className="flex items-center gap-3">
          <div className="accent-square-sm" aria-hidden="true" />
          <span className="editorial-caps text-xs text-heading">
            {group.roman}
          </span>
          <span className="editorial-caps text-xs text-heading">
            {group.label}
          </span>
        </div>
        <div className="flex items-center gap-3">
          <CountDots counts={group.counts} />
          <InfoTooltip text={group.tooltip} />
        </div>
      </div>

      {/* Exceptions */}
      {group.exceptions.map((ex) => (
        <div
          key={`${ex.permissionType}-${ex.platformId}`}
          className="mt-3 ml-10 border-l-2 pl-3 py-1 text-xs text-muted"
          style={{ borderColor: "var(--color-accent)" }}
        >
          <span className="text-heading font-medium">
            {formatPermissionType(ex.permissionType)}
          </span>{" "}
          is{" "}
          <span className="font-medium" style={{ color: "var(--color-permission-deny)" }}>
            {ex.baseValue}
          </span>{" "}
          — except{" "}
          <span className="font-medium text-heading">{ex.platformName}</span>{" "}
          via Auracles authorization (70% revenue share)
        </div>
      ))}

      <div className="accent-line mt-4" style={{ opacity: 0.2 }} />
    </div>
  );
}

function CountDots({ counts }: { counts: { allow: number; ask: number; deny: number } }) {
  return (
    <div className="flex items-center gap-3 data-mono text-xs">
      <span className="flex items-center gap-1">
        <span
          className="inline-block h-1.5 w-1.5 rounded-full"
          style={{ backgroundColor: "var(--color-permission-allow)" }}
          aria-hidden="true"
        />
        <span>{counts.allow} allow</span>
      </span>
      <span className="flex items-center gap-1">
        <span
          className="inline-block h-1.5 w-1.5 rounded-full"
          style={{ backgroundColor: "var(--color-permission-ask)" }}
          aria-hidden="true"
        />
        <span>{counts.ask} ask</span>
      </span>
      <span className="flex items-center gap-1">
        <span
          className="inline-block h-1.5 w-1.5 rounded-full"
          style={{ backgroundColor: "var(--color-permission-deny)" }}
          aria-hidden="true"
        />
        <span>{counts.deny} deny</span>
      </span>
    </div>
  );
}

function InfoTooltip({ text }: { text: string }) {
  const [show, setShow] = useState(false);
  const tooltipId = useId();

  return (
    <span className="relative inline-block">
      <span
        role="button"
        aria-label="More information"
        aria-describedby={tooltipId}
        className="inline-flex items-center justify-center cursor-pointer text-xs text-muted hover:text-heading transition-colors duration-150"
        onMouseEnter={() => setShow(true)}
        onMouseLeave={() => setShow(false)}
        onFocus={() => setShow(true)}
        onBlur={() => setShow(false)}
        tabIndex={0}
      >
        (i)
      </span>
      {show && (
        <span
          id={tooltipId}
          role="tooltip"
          className="absolute z-50 bottom-full right-0 mb-2 px-3 py-2 text-xs rounded max-w-72"
          style={{
            backgroundColor: "var(--color-surface-elevated)",
            color: "var(--color-heading)",
            border: "1px solid var(--color-border)",
            boxShadow: "0 2px 8px rgba(0,0,0,0.12)",
          }}
        >
          {text}
        </span>
      )}
    </span>
  );
}
