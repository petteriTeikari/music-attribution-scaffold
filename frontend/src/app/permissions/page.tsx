"use client";

import { useEffect, useState } from "react";
import type { PermissionBundle, AuditLogEntry } from "@/lib/types/permissions";
import { mockApi } from "@/lib/api/mock-client";
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
    Promise.all([mockApi.getPermissions(), mockApi.getAuditLog()]).then(
      ([perms, log]) => {
        setPermissions(perms);
        setAuditLog(log);
        setLoading(false);
      }
    );
  }, []);

  return (
    <div className="mx-auto max-w-4xl px-[var(--space-6)] py-[var(--space-10)]">
      {/* Header */}
      <div className="mb-[var(--space-8)]">
        <h1 className="text-[var(--text-3xl)] font-bold text-[var(--color-heading)]">
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

      {/* Tabs */}
      <div className="mb-[var(--space-6)] flex border-b border-[var(--color-border)]">
        {TABS.map((tab) => (
          <button
            key={tab.id}
            onClick={() => setActiveTab(tab.id)}
            className={`px-[var(--space-4)] py-[var(--space-3)] text-[var(--text-sm)] font-medium transition-colors duration-[var(--transition-fast)] border-b-2 -mb-px ${
              activeTab === tab.id
                ? "border-[var(--color-primary)] text-[var(--color-primary)]"
                : "border-transparent text-[var(--color-label)] hover:text-[var(--color-body)]"
            }`}
            role="tab"
            aria-selected={activeTab === tab.id}
          >
            {tab.label}
          </button>
        ))}
      </div>

      {/* Tab content */}
      {loading ? (
        <div className="h-64 animate-pulse rounded-[var(--radius-lg)] bg-[var(--color-surface-secondary)]" />
      ) : (
        <div>
          {activeTab === "permissions" && permissions && (
            <div className="rounded-[var(--radius-lg)] border border-[var(--color-border)] bg-[var(--color-surface-elevated)] p-[var(--space-6)]">
              <div className="mb-[var(--space-4)] flex items-center justify-between">
                <h2 className="text-[var(--text-lg)] font-semibold text-[var(--color-heading)]">
                  Catalog-Wide Permissions
                </h2>
                <span className="text-[var(--text-xs)] text-[var(--color-muted)]">
                  Default: {permissions.default_permission.replace(/_/g, " ")} | v{permissions.version}
                </span>
              </div>
              <PermissionMatrix permissions={permissions.permissions} />
            </div>
          )}

          {activeTab === "mcp" && (
            <div className="rounded-[var(--radius-lg)] border border-[var(--color-border)] bg-[var(--color-surface-elevated)] p-[var(--space-6)]">
              <h2 className="mb-[var(--space-4)] text-[var(--text-lg)] font-semibold text-[var(--color-heading)]">
                MCP Permission Query Simulation
              </h2>
              <MCPQueryMockup />
            </div>
          )}

          {activeTab === "audit" && (
            <div className="rounded-[var(--radius-lg)] border border-[var(--color-border)] bg-[var(--color-surface-elevated)] p-[var(--space-6)]">
              <h2 className="mb-[var(--space-4)] text-[var(--text-lg)] font-semibold text-[var(--color-heading)]">
                Permission Audit Log
              </h2>
              <AuditLog entries={auditLog} />
            </div>
          )}
        </div>
      )}

      {/* Delegation chain */}
      {permissions && !loading && (
        <div className="mt-[var(--space-8)] rounded-[var(--radius-lg)] border border-[var(--color-border)] bg-[var(--color-surface-elevated)] p-[var(--space-6)]">
          <h2 className="mb-[var(--space-4)] text-[var(--text-lg)] font-semibold text-[var(--color-heading)]">
            Delegation Chain
          </h2>
          <div className="flex items-center gap-[var(--space-4)]">
            {permissions.delegation_chain.map((entry, index) => (
              <div key={entry.entity_id} className="flex items-center gap-[var(--space-4)]">
                {index > 0 && (
                  <span className="text-[var(--color-muted)]">→</span>
                )}
                <div className="rounded-[var(--radius-md)] border border-[var(--color-border)] px-[var(--space-4)] py-[var(--space-3)]">
                  <p className="font-medium text-[var(--color-heading)] text-[var(--text-sm)]">
                    {entry.entity_name}
                  </p>
                  <p className="text-[var(--text-xs)] text-[var(--color-label)]">
                    {entry.role} {entry.can_modify && "• Can modify"}{" "}
                    {entry.can_delegate && "• Can delegate"}
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
    <div className="rounded-[var(--radius-lg)] border border-[var(--color-border)] bg-[var(--color-surface-elevated)] p-[var(--space-4)]">
      <div className="flex items-center justify-between">
        <h3 className="text-[var(--text-sm)] font-semibold text-[var(--color-heading)]">
          {title}
        </h3>
        <span
          className="rounded-[var(--radius-full)] px-[var(--space-2)] py-[var(--space-1)] text-[var(--text-xs)] font-medium"
          style={{
            backgroundColor: `color-mix(in srgb, ${colorVar} 12%, transparent)`,
            color: colorVar,
          }}
        >
          {enabled ? "ON" : "OFF"}
        </span>
      </div>
      <p className="mt-[var(--space-2)] text-[var(--text-xs)] text-[var(--color-muted)]">
        {description}
      </p>
    </div>
  );
}
