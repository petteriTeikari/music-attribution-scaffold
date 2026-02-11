"use client";

import { useEffect, useState } from "react";
import type { PermissionBundle, AuditLogEntry } from "@/lib/types/permissions";
import { apiClient } from "@/lib/api/api-client";
import { PermissionMatrix } from "@/components/permissions/permission-matrix";
import { AuditLog } from "@/components/permissions/audit-log";
import { MCPQueryMockup } from "@/components/mcp/mcp-query-mockup";

type TabId = "permissions" | "mcp" | "audit";

const TABS: { id: TabId; label: string }[] = [
  { id: "permissions", label: "Permission Matrix" },
  { id: "mcp", label: "MCP Query Demo" },
  { id: "audit", label: "Audit Log" },
];

export default function PermissionsPage() {
  const [permissions, setPermissions] = useState<PermissionBundle | null>(null);
  const [auditLog, setAuditLog] = useState<AuditLogEntry[]>([]);
  const [loading, setLoading] = useState(true);
  const [activeTab, setActiveTab] = useState<TabId>("permissions");

  useEffect(() => {
    // Default entity for demo — Imogen Heap artist entity
    const entityId = "artist-imogen-heap";
    Promise.all([apiClient.getPermissions(entityId), apiClient.getAuditLog()]).then(
      ([perms, log]) => {
        setPermissions(perms);
        setAuditLog(log);
        setLoading(false);
      }
    );
  }, []);

  return (
    <div className="px-[var(--space-8)] py-[var(--space-10)]">
      {/* Header */}
      <div className="mb-[var(--space-8)]">
        <span className="editorial-caps text-xs text-[var(--color-accent)] block mb-[var(--space-2)]">
          Control
        </span>
        <h1 className="editorial-display text-4xl text-[var(--color-heading)]">
          Your Music, Your Rules
        </h1>
        <p className="mt-[var(--space-2)] text-[var(--color-label)]">
          Granular permission control with MCP consent infrastructure.
        </p>
      </div>

      {/* Category toggles overview */}
      {permissions && !loading && (
        <div className="mb-[var(--space-8)] grid gap-[var(--space-4)] sm:grid-cols-3">
          <CategoryCard
            title="Verified AI Partners"
            description="Trusted platforms with attribution agreements"
            enabled={true}
            colorVar="var(--color-permission-allow)"
          />
          <CategoryCard
            title="Unknown Crawlers"
            description="Unverified AI platforms and scrapers"
            enabled={false}
            colorVar="var(--color-permission-deny)"
          />
          <CategoryCard
            title="Rights Organizations"
            description="PROs and collecting societies"
            enabled={true}
            colorVar="var(--color-permission-allow)"
          />
        </div>
      )}

      {/* Tabs — editorial underline style */}
      <div className="mb-[var(--space-6)]">
        <div className="flex gap-[var(--space-6)]">
          {TABS.map((tab) => (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id)}
              className={`editorial-caps text-xs pb-[var(--space-2)] transition-colors duration-[var(--transition-fast)] border-b-2 ${
                activeTab === tab.id
                  ? "border-[var(--color-accent)] text-[var(--color-heading)]"
                  : "border-transparent text-[var(--color-label)] hover:text-[var(--color-heading)]"
              }`}
              role="tab"
              aria-selected={activeTab === tab.id}
            >
              {tab.label}
            </button>
          ))}
        </div>
        <div className="accent-line mt-0" style={{ opacity: 0.2 }} />
      </div>

      {/* Tab content */}
      {loading ? (
        <div className="h-64 animate-pulse bg-[var(--color-surface-secondary)]" />
      ) : (
        <div>
          {activeTab === "permissions" && permissions && (
            <div>
              <div className="mb-[var(--space-4)] flex items-center justify-between">
                <h2 className="text-base font-semibold text-[var(--color-heading)]">
                  Catalog-Wide Permissions
                </h2>
                <span className="text-xs text-[var(--color-muted)] data-mono">
                  Default: {permissions.default_permission.replace(/_/g, " ")} | v{permissions.version}
                </span>
              </div>
              <PermissionMatrix permissions={permissions.permissions} />
            </div>
          )}

          {activeTab === "mcp" && (
            <div>
              <h2 className="mb-[var(--space-4)] text-base font-semibold text-[var(--color-heading)]">
                MCP Permission Query Simulation
              </h2>
              <MCPQueryMockup />
            </div>
          )}

          {activeTab === "audit" && (
            <div>
              <h2 className="mb-[var(--space-4)] text-base font-semibold text-[var(--color-heading)]">
                Permission Audit Log
              </h2>
              <AuditLog entries={auditLog} />
            </div>
          )}
        </div>
      )}

      {/* Delegation chain */}
      {permissions && !loading && (
        <div className="mt-[var(--space-8)]">
          <div className="accent-line mb-[var(--space-6)]" style={{ opacity: 0.2 }} />
          <span className="editorial-caps text-xs text-[var(--color-accent)] block mb-[var(--space-2)]">
            Delegation
          </span>
          <h2 className="text-base font-semibold text-[var(--color-heading)] mb-[var(--space-4)]">
            Delegation Chain
          </h2>
          <div className="flex items-center gap-[var(--space-4)]">
            {permissions.delegation_chain.map((entry, index) => (
              <div key={entry.entity_id} className="flex items-center gap-[var(--space-4)]">
                {index > 0 && (
                  <span className="text-[var(--color-accent)]">→</span>
                )}
                <div className="border-l-2 border-[var(--color-border)] pl-[var(--space-4)] py-[var(--space-2)]">
                  <p className="font-medium text-[var(--color-heading)] text-sm">
                    {entry.entity_name}
                  </p>
                  <p className="text-xs text-[var(--color-label)]">
                    {entry.role} {entry.can_modify && "· Can modify"}{" "}
                    {entry.can_delegate && "· Can delegate"}
                  </p>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}

function CategoryCard({
  title,
  description,
  enabled,
  colorVar,
}: {
  title: string;
  description: string;
  enabled: boolean;
  colorVar: string;
}) {
  return (
    <div className="border-l-2 pl-[var(--space-4)] py-[var(--space-2)]" style={{ borderColor: colorVar }}>
      <div className="flex items-center justify-between">
        <h3 className="text-sm font-semibold text-[var(--color-heading)]">
          {title}
        </h3>
        <span
          className="editorial-caps text-xs"
          style={{ color: colorVar }}
        >
          {enabled ? "ON" : "OFF"}
        </span>
      </div>
      <p className="mt-[var(--space-1)] text-xs text-[var(--color-muted)]">
        {description}
      </p>
    </div>
  );
}
