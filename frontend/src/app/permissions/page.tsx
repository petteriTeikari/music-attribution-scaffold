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
    <div className="px-8 py-10">
      {/* Header */}
      <div className="mb-8">
        <span className="editorial-caps text-xs text-accent block mb-2">
          Control
        </span>
        <h1 className="editorial-display text-4xl text-heading">
          Your Music, Your Rules
        </h1>
        <p className="mt-2 text-label">
          Granular permission control with MCP consent infrastructure.
        </p>
      </div>

      {/* Category toggles overview */}
      {permissions && !loading && (
        <div className="mb-8 grid gap-4 sm:grid-cols-3">
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
      <div className="mb-6">
        <div className="flex gap-6">
          {TABS.map((tab) => (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id)}
              className={`editorial-caps text-xs pb-2 transition-colors duration-150 border-b-2 ${
                activeTab === tab.id
                  ? "border-accent text-heading"
                  : "border-transparent text-label hover:text-heading"
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
        <div className="h-64 animate-pulse bg-surface-secondary" />
      ) : (
        <div>
          {activeTab === "permissions" && permissions && (
            <div>
              <div className="mb-4 flex items-center justify-between">
                <h2 className="text-base font-semibold text-heading">
                  Catalog-Wide Permissions
                </h2>
                <span className="text-xs text-muted data-mono">
                  Default: {permissions.default_permission.replace(/_/g, " ")} | v{permissions.version}
                </span>
              </div>
              <PermissionMatrix permissions={permissions.permissions} />
            </div>
          )}

          {activeTab === "mcp" && (
            <div>
              <h2 className="mb-4 text-base font-semibold text-heading">
                MCP Permission Query Simulation
              </h2>
              <MCPQueryMockup />
            </div>
          )}

          {activeTab === "audit" && (
            <div>
              <h2 className="mb-4 text-base font-semibold text-heading">
                Permission Audit Log
              </h2>
              <AuditLog entries={auditLog} />
            </div>
          )}
        </div>
      )}

      {/* Delegation chain */}
      {permissions && !loading && (
        <div className="mt-8">
          <div className="accent-line mb-6" style={{ opacity: 0.2 }} />
          <span className="editorial-caps text-xs text-accent block mb-2">
            Delegation
          </span>
          <h2 className="text-base font-semibold text-heading mb-4">
            Delegation Chain
          </h2>
          <div className="flex items-center gap-4">
            {permissions.delegation_chain.map((entry, index) => (
              <div key={entry.entity_id} className="flex items-center gap-4">
                {index > 0 && (
                  <span className="text-accent">→</span>
                )}
                <div className="border-l-2 border-border pl-4 py-2">
                  <p className="font-medium text-heading text-sm">
                    {entry.entity_name}
                  </p>
                  <p className="text-xs text-label">
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
    <div className="border-l-2 pl-4 py-2" style={{ borderColor: colorVar }}>
      <div className="flex items-center justify-between">
        <h3 className="text-sm font-semibold text-heading">
          {title}
        </h3>
        <span
          className="editorial-caps text-xs"
          style={{ color: colorVar }}
        >
          {enabled ? "ON" : "OFF"}
        </span>
      </div>
      <p className="mt-1 text-xs text-muted">
        {description}
      </p>
    </div>
  );
}
