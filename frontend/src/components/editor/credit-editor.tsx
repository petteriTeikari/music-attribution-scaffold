"use client";

// TODO: Component not yet integrated — wire up during UI fine-tuning

import { useState, useRef, useEffect } from "react";
import type { Credit } from "@/lib/types/attribution";
import { CreditRole } from "@/lib/types/enums";

interface CreditEditorProps {
  credit: Credit;
  onSave?: (updated: Credit) => void;
  onCancel?: () => void;
}

const ROLE_OPTIONS = Object.values(CreditRole);

function formatRole(role: string): string {
  return role
    .split("_")
    .map((w) => w.charAt(0).toUpperCase() + w.slice(1).toLowerCase())
    .join(" ");
}

export function CreditEditor({ credit, onSave, onCancel }: CreditEditorProps) {
  const [editingField, setEditingField] = useState<string | null>(null);
  const [name, setName] = useState(credit.entity_name);
  const [role, setRole] = useState(credit.role);
  const [roleDetail, setRoleDetail] = useState(credit.role_detail ?? "");
  const inputRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    if (editingField && inputRef.current) {
      inputRef.current.focus();
    }
  }, [editingField]);

  function handleSave() {
    onSave?.({
      ...credit,
      entity_name: name,
      role,
      role_detail: roleDetail || null,
    });
    setEditingField(null);
  }

  function handleKeyDown(e: React.KeyboardEvent) {
    if (e.key === "Enter") {
      handleSave();
    } else if (e.key === "Escape") {
      setName(credit.entity_name);
      setRole(credit.role);
      setRoleDetail(credit.role_detail ?? "");
      setEditingField(null);
      onCancel?.();
    } else if (e.key === "Tab") {
      // Tab between fields
      e.preventDefault();
      if (editingField === "name") setEditingField("role");
      else if (editingField === "role") setEditingField("detail");
      else handleSave();
    }
  }

  return (
    <div
      className="rounded-[var(--radius-md)] border border-[var(--color-primary)] bg-[var(--color-surface-elevated)] p-[var(--space-4)]"
      onKeyDown={handleKeyDown}
    >
      <div className="space-y-[var(--space-3)]">
        {/* Name field */}
        <div>
          <label className="text-xs text-[var(--color-label)]">
            Name
          </label>
          {editingField === "name" ? (
            <input
              ref={inputRef}
              value={name}
              onChange={(e) => setName(e.target.value)}
              className="w-full rounded-[var(--radius-sm)] border border-[var(--color-border)] bg-[var(--color-surface)] px-[var(--space-2)] py-[var(--space-1)] text-sm text-[var(--color-heading)]"
              aria-label="Credit name"
            />
          ) : (
            <button
              onClick={() => setEditingField("name")}
              className="w-full text-left px-[var(--space-2)] py-[var(--space-1)] text-sm text-[var(--color-heading)] hover:bg-[var(--color-surface-secondary)] rounded-[var(--radius-sm)]"
            >
              {name}
            </button>
          )}
        </div>

        {/* Role field */}
        <div>
          <label className="text-xs text-[var(--color-label)]">
            Role
          </label>
          {editingField === "role" ? (
            <select
              value={role}
              onChange={(e) => setRole(e.target.value as Credit["role"])}
              className="w-full rounded-[var(--radius-sm)] border border-[var(--color-border)] bg-[var(--color-surface)] px-[var(--space-2)] py-[var(--space-1)] text-sm text-[var(--color-heading)]"
              aria-label="Credit role"
            >
              {ROLE_OPTIONS.map((r) => (
                <option key={r} value={r}>
                  {formatRole(r)}
                </option>
              ))}
            </select>
          ) : (
            <button
              onClick={() => setEditingField("role")}
              className="w-full text-left px-[var(--space-2)] py-[var(--space-1)] text-sm text-[var(--color-heading)] hover:bg-[var(--color-surface-secondary)] rounded-[var(--radius-sm)]"
            >
              {formatRole(role)}
            </button>
          )}
        </div>

        {/* Detail field */}
        <div>
          <label className="text-xs text-[var(--color-label)]">
            Detail
          </label>
          {editingField === "detail" ? (
            <input
              value={roleDetail}
              onChange={(e) => setRoleDetail(e.target.value)}
              placeholder="Optional detail..."
              className="w-full rounded-[var(--radius-sm)] border border-[var(--color-border)] bg-[var(--color-surface)] px-[var(--space-2)] py-[var(--space-1)] text-sm text-[var(--color-heading)] placeholder:text-[var(--color-muted)]"
              aria-label="Credit detail"
            />
          ) : (
            <button
              onClick={() => setEditingField("detail")}
              className="w-full text-left px-[var(--space-2)] py-[var(--space-1)] text-sm text-[var(--color-muted)] hover:bg-[var(--color-surface-secondary)] rounded-[var(--radius-sm)]"
            >
              {roleDetail || "Click to add detail..."}
            </button>
          )}
        </div>
      </div>

      {/* Action buttons */}
      <div className="mt-[var(--space-3)] flex justify-end gap-[var(--space-2)]">
        <button
          onClick={() => {
            setName(credit.entity_name);
            setRole(credit.role);
            setRoleDetail(credit.role_detail ?? "");
            setEditingField(null);
            onCancel?.();
          }}
          className="rounded-[var(--radius-sm)] border border-[var(--color-border)] px-[var(--space-3)] py-[var(--space-1)] text-xs text-[var(--color-label)]"
        >
          Cancel
        </button>
        <button
          onClick={handleSave}
          className="rounded-[var(--radius-sm)] bg-[var(--color-primary)] px-[var(--space-3)] py-[var(--space-1)] text-xs text-white"
        >
          Save
        </button>
      </div>
    </div>
  );
}
