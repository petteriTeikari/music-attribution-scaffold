"use client";

/**
 * ConsentProfile — Data-driven consent summary replacing static CategoryCards.
 *
 * Groups the 14-entry permission model into 3 editorial rows with
 * allow/ask/deny counts, exception callouts, and educational tooltips.
 * Count dots expand on hover to show which permissions belong to each bucket.
 * Includes sequenced onboarding tooltips for novice users.
 */

import { useState, useEffect, useId, useCallback } from "react";
import type { PermissionEntry } from "@/lib/types/permissions";
import {
  buildConsentGroups,
  formatPermissionType,
  isAllowValue,
  type ConsentGroup,
} from "@/lib/permissions/consent-groups";

const ONBOARDING_STEPS = [
  {
    id: "consent-header",
    content:
      "This is your consent profile — a summary of how you've configured permissions across your catalog. It shows three groups of permissions at a glance.",
  },
  {
    id: "count-dots",
    content:
      "Hover over these count dots to see exactly which permissions are in each category. Click any entry to jump straight to it in the Permission Matrix below.",
  },
  {
    id: "permission-tab",
    content:
      "Use the Permission Matrix tab to see and edit individual permission settings. The Consent Graph tab shows how your permissions flow through the ecosystem.",
  },
];

interface ConsentProfileProps {
  permissions: PermissionEntry[];
  onNavigateToEntry?: (permissionType: string) => void;
  onboardingEnabled?: boolean;
}

export function ConsentProfile({
  permissions,
  onNavigateToEntry,
  onboardingEnabled = false,
}: ConsentProfileProps) {
  const groups = buildConsentGroups(permissions);
  const [onboardingStep, setOnboardingStep] = useState<number>(-1);

  useEffect(() => {
    if (onboardingEnabled) {
      const timer = setTimeout(() => setOnboardingStep(0), 400);
      return () => clearTimeout(timer);
    }
  }, [onboardingEnabled]);

  const advanceOnboarding = useCallback(() => {
    setOnboardingStep((prev) => {
      const next = prev + 1;
      return next < ONBOARDING_STEPS.length ? next : -1;
    });
  }, []);

  return (
    <div className="mb-8">
      {/* Header */}
      <div className="relative">
        <span className="editorial-caps text-xs text-accent block mb-4">
          Consent Profile
        </span>
        {onboardingStep === 0 && (
          <OnboardingTooltip
            step={ONBOARDING_STEPS[0]}
            onDismiss={advanceOnboarding}
          />
        )}
      </div>

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
      {groups.map((group, i) => (
        <GroupRow
          key={group.roman}
          group={group}
          onNavigateToEntry={onNavigateToEntry}
          showOnboardingDots={i === 0 && onboardingStep === 1}
          onDismissOnboarding={advanceOnboarding}
        />
      ))}
    </div>
  );
}

function OnboardingTooltip({
  step,
  onDismiss,
}: {
  step: { id: string; content: string };
  onDismiss: () => void;
}) {
  return (
    <div
      role="tooltip"
      className="absolute z-50 left-0 top-full mt-1 px-3 py-2 text-xs max-w-72"
      style={{
        backgroundColor: "var(--color-surface-elevated)",
        border: "1px solid var(--color-accent)",
        boxShadow: "var(--shadow-md)",
      }}
    >
      <p className="text-body">{step.content}</p>
      <button
        onClick={onDismiss}
        className="mt-1 text-accent underline underline-offset-2 text-xs"
      >
        Got it
      </button>
    </div>
  );
}

function GroupRow({
  group,
  onNavigateToEntry,
  showOnboardingDots,
  onDismissOnboarding,
}: {
  group: ConsentGroup;
  onNavigateToEntry?: (permissionType: string) => void;
  showOnboardingDots?: boolean;
  onDismissOnboarding?: () => void;
}) {
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
        <div className="relative flex items-center gap-3">
          <CountDots
            counts={group.counts}
            entries={group.entries}
            onNavigateToEntry={onNavigateToEntry}
          />
          <InfoTooltip text={group.tooltip} />
          {showOnboardingDots && onDismissOnboarding && (
            <OnboardingTooltip
              step={ONBOARDING_STEPS[1]}
              onDismiss={onDismissOnboarding}
            />
          )}
        </div>
      </div>
      {group.subtitle && (
        <p className="mt-1 ml-10 text-xs text-muted">{group.subtitle}</p>
      )}

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

interface CountDotsProps {
  counts: { allow: number; ask: number; deny: number };
  entries: PermissionEntry[];
  onNavigateToEntry?: (permissionType: string) => void;
}

function CountDots({ counts, entries, onNavigateToEntry }: CountDotsProps) {
  const allowEntries = entries.filter((e) => isAllowValue(e.value));
  const askEntries = entries.filter((e) => e.value === "ASK");
  const denyEntries = entries.filter((e) => e.value === "DENY");

  return (
    <div className="flex items-center gap-3 data-mono text-xs">
      <CountBucket
        count={counts.allow}
        label="allow"
        colorVar="var(--color-permission-allow)"
        entries={allowEntries}
        onNavigateToEntry={onNavigateToEntry}
      />
      <CountBucket
        count={counts.ask}
        label="ask"
        colorVar="var(--color-permission-ask)"
        entries={askEntries}
        onNavigateToEntry={onNavigateToEntry}
      />
      <CountBucket
        count={counts.deny}
        label="deny"
        colorVar="var(--color-permission-deny)"
        entries={denyEntries}
        onNavigateToEntry={onNavigateToEntry}
      />
    </div>
  );
}

function CountBucket({
  count,
  label,
  colorVar,
  entries,
  onNavigateToEntry,
}: {
  count: number;
  label: string;
  colorVar: string;
  entries: PermissionEntry[];
  onNavigateToEntry?: (permissionType: string) => void;
}) {
  const [open, setOpen] = useState(false);

  if (count === 0) {
    return (
      <span className="flex items-center gap-1">
        <span
          className="inline-block h-1.5 w-1.5 rounded-full"
          style={{ backgroundColor: colorVar }}
          aria-hidden="true"
        />
        <span>{count} {label}</span>
      </span>
    );
  }

  return (
    <span
      className="relative flex items-center gap-1 cursor-pointer"
      data-count-bucket
      aria-haspopup="listbox"
      onMouseEnter={() => setOpen(true)}
      onMouseLeave={() => setOpen(false)}
      onFocus={() => setOpen(true)}
      onBlur={() => setOpen(false)}
      tabIndex={0}
    >
      <span
        className="inline-block h-1.5 w-1.5 rounded-full"
        style={{ backgroundColor: colorVar }}
        aria-hidden="true"
      />
      <span>{count} {label}</span>
      {open && (
        <span
          role="listbox"
          className="absolute z-50 top-full right-0 mt-1 py-1 min-w-48 text-xs"
          style={{
            backgroundColor: "var(--color-surface-elevated)",
            border: "1px solid var(--color-border)",
            boxShadow: "var(--shadow-md)",
          }}
        >
          {entries.map((entry) => (
            <span
              key={entry.permission_type}
              role="option"
              aria-selected={false}
              className="flex items-center gap-2 px-3 py-1.5 text-body hover:bg-surface-secondary cursor-pointer transition-colors duration-100"
              onClick={() => onNavigateToEntry?.(entry.permission_type)}
            >
              <span
                className="inline-block h-1.5 w-1.5 rounded-full shrink-0"
                style={{ backgroundColor: colorVar }}
                aria-hidden="true"
              />
              {formatPermissionType(entry.permission_type)}
            </span>
          ))}
        </span>
      )}
    </span>
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
            boxShadow: "var(--shadow-md)",
          }}
        >
          {text}
        </span>
      )}
    </span>
  );
}
