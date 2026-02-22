"use client";

import type { GraphNode } from "@/lib/permissions/graph-data";
import {
  getPlatform,
  ECOSYSTEM_PLATFORMS,
  type EcosystemPlatform,
} from "@/lib/data/ecosystem-platforms";

interface NodeOverlayPanelProps {
  node: GraphNode;
  /** Permission count breakdown for group nodes */
  groupCounts?: { allow: number; ask: number; deny: number };
  /** Total permission count for artist node */
  totalCount?: number;
  onClose: () => void;
  onNavigateToPermissions?: () => void;
}

function PlatformOverlay({ platform }: { platform: EcosystemPlatform }) {
  return (
    <>
      <p className="editorial-caps text-xs text-accent mb-1">Platform</p>
      <h4 className="text-base font-semibold text-heading">{platform.name}</h4>
      <p className="mt-1 text-sm text-label">{platform.description}</p>
      <p className="mt-1 text-xs text-muted italic">{platform.tagline}</p>

      {platform.url && (
        <a
          href={platform.url}
          target="_blank"
          rel="noopener noreferrer"
          className="mt-2 inline-block text-xs text-accent underline underline-offset-2"
        >
          {platform.url}
        </a>
      )}

      {platform.fairly_trained_certified && (
        <div className="mt-2 flex items-center gap-1.5">
          <span
            className="h-2 w-2 rounded-full"
            style={{ backgroundColor: "var(--color-confidence-high)" }}
            aria-hidden="true"
          />
          <span className="text-xs text-confidence-high">
            Fairly Trained Certified
          </span>
        </div>
      )}
    </>
  );
}

function GroupOverlay({
  node,
  counts,
}: {
  node: GraphNode;
  counts: { allow: number; ask: number; deny: number };
}) {
  const total = counts.allow + counts.ask + counts.deny;
  return (
    <>
      <p className="editorial-caps text-xs text-accent mb-1">Consent Group</p>
      <h4 className="text-base font-semibold text-heading">{node.label}</h4>
      <div className="mt-2 space-y-1 text-xs">
        <div className="flex justify-between">
          <span className="text-muted">Total permissions</span>
          <span className="data-mono text-body">{total}</span>
        </div>
        <div className="flex justify-between">
          <span style={{ color: "var(--color-permission-allow)" }}>Allow</span>
          <span className="data-mono text-body">{counts.allow}</span>
        </div>
        <div className="flex justify-between">
          <span style={{ color: "var(--color-permission-ask)" }}>Ask</span>
          <span className="data-mono text-body">{counts.ask}</span>
        </div>
        <div className="flex justify-between">
          <span style={{ color: "var(--color-permission-deny)" }}>Deny</span>
          <span className="data-mono text-body">{counts.deny}</span>
        </div>
      </div>
    </>
  );
}

function ArtistOverlay({
  node,
  totalCount,
  onNavigateToPermissions,
}: {
  node: GraphNode;
  totalCount: number;
  onNavigateToPermissions?: () => void;
}) {
  return (
    <>
      <p className="editorial-caps text-xs text-accent mb-1">Artist</p>
      <h4 className="text-base font-semibold text-heading">{node.label}</h4>
      <div className="mt-2 flex justify-between text-xs">
        <span className="text-muted">Total permissions</span>
        <span className="data-mono text-body">{totalCount}</span>
      </div>
      {onNavigateToPermissions && (
        <button
          onClick={onNavigateToPermissions}
          className="mt-2 text-xs text-accent underline underline-offset-2"
        >
          View all permissions
        </button>
      )}
    </>
  );
}

/**
 * Overlay panel showing details for a clicked consent graph node.
 * Positioned as an absolute HTML sibling to the SVG graph.
 */
export function NodeOverlayPanel({
  node,
  groupCounts,
  totalCount = 0,
  onClose,
  onNavigateToPermissions,
}: NodeOverlayPanelProps) {
  // Resolve platform from ecosystem registry via platformType
  const platform =
    node.type === "platform" && node.platformType
      ? findPlatformByType(node.label, node.platformType)
      : undefined;

  return (
    <div
      role="dialog"
      aria-label={`Details for ${node.label}`}
      className="absolute right-0 top-0 z-50 w-64 bg-surface-elevated border border-border p-4"
    >
      <button
        onClick={onClose}
        className="absolute top-2 right-2 text-muted hover:text-heading text-sm"
        aria-label="Close overlay"
      >
        &times;
      </button>

      {node.type === "platform" && platform && (
        <PlatformOverlay platform={platform} />
      )}

      {node.type === "platform" && !platform && (
        <>
          <p className="editorial-caps text-xs text-accent mb-1">Platform</p>
          <h4 className="text-base font-semibold text-heading">{node.label}</h4>
          <p className="mt-1 text-xs text-muted">No registry data available</p>
        </>
      )}

      {node.type === "group" && groupCounts && (
        <GroupOverlay node={node} counts={groupCounts} />
      )}

      {node.type === "artist" && (
        <ArtistOverlay
          node={node}
          totalCount={totalCount}
          onNavigateToPermissions={onNavigateToPermissions}
        />
      )}
    </div>
  );
}

/**
 * Find a platform by matching label against ecosystem registry.
 */
function findPlatformByType(
  label: string,
  _platformType: string,
): EcosystemPlatform | undefined {
  // Match by name (case-insensitive) since platformType from graph is requester_type
  const normalizedLabel = label.toLowerCase().replace(/[^a-z0-9]/g, "");
  return getPlatform(normalizedLabel) ?? findPlatformByName(label);
}

function findPlatformByName(name: string): EcosystemPlatform | undefined {
  return ECOSYSTEM_PLATFORMS.find(
    (p) => p.name.toLowerCase() === name.toLowerCase(),
  );
}
