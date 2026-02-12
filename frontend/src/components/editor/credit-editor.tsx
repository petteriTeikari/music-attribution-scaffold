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
      className="rounded-md border border-primary bg-surface-elevated p-4"
      onKeyDown={handleKeyDown}
    >
      <div className="space-y-3">
        {/* Name field */}
        <div>
          <label className="text-xs text-label">
            Name
          </label>
          {editingField === "name" ? (
            <input
              ref={inputRef}
              value={name}
              onChange={(e) => setName(e.target.value)}
              className="w-full rounded-sm border border-border bg-surface px-2 py-1 text-sm text-heading"
              aria-label="Credit name"
            />
          ) : (
            <button
              onClick={() => setEditingField("name")}
              className="w-full text-left px-2 py-1 text-sm text-heading hover:bg-surface-secondary rounded-sm"
            >
              {name}
            </button>
          )}
        </div>

        {/* Role field */}
        <div>
          <label className="text-xs text-label">
            Role
          </label>
          {editingField === "role" ? (
            <select
              value={role}
              onChange={(e) => setRole(e.target.value as Credit["role"])}
              className="w-full rounded-sm border border-border bg-surface px-2 py-1 text-sm text-heading"
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
              className="w-full text-left px-2 py-1 text-sm text-heading hover:bg-surface-secondary rounded-sm"
            >
              {formatRole(role)}
            </button>
          )}
        </div>

        {/* Detail field */}
        <div>
          <label className="text-xs text-label">
            Detail
          </label>
          {editingField === "detail" ? (
            <input
              value={roleDetail}
              onChange={(e) => setRoleDetail(e.target.value)}
              placeholder="Optional detail..."
              className="w-full rounded-sm border border-border bg-surface px-2 py-1 text-sm text-heading placeholder:text-muted"
              aria-label="Credit detail"
            />
          ) : (
            <button
              onClick={() => setEditingField("detail")}
              className="w-full text-left px-2 py-1 text-sm text-muted hover:bg-surface-secondary rounded-sm"
            >
              {roleDetail || "Click to add detail..."}
            </button>
          )}
        </div>
      </div>

      {/* Action buttons */}
      <div className="mt-3 flex justify-end gap-2">
        <button
          onClick={() => {
            setName(credit.entity_name);
            setRole(credit.role);
            setRoleDetail(credit.role_detail ?? "");
            setEditingField(null);
            onCancel?.();
          }}
          className="rounded-sm border border-border px-3 py-1 text-xs text-label"
        >
          Cancel
        </button>
        <button
          onClick={handleSave}
          className="rounded-sm bg-primary px-3 py-1 text-xs text-white"
        >
          Save
        </button>
      </div>
    </div>
  );
}
