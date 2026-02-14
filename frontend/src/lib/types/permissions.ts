/**
 * Permission types mirroring Python schemas from
 * src/music_attribution/schemas/permissions.py
 */

import type {
  DelegationRole,
  PlatformType,
  PermissionScope,
  PermissionType,
  PermissionValue,
} from "./enums";

export interface PermissionCondition {
  condition_type: string;
  value: string;
}

export interface PermissionEntry {
  permission_type: PermissionType;
  value: PermissionValue;
  conditions: PermissionCondition[];
  royalty_rate: number | null;
  attribution_requirement: string | null;
  territory: string[] | null;
}

export interface DelegationEntry {
  entity_id: string;
  entity_name: string; // Display field (frontend addition)
  role: DelegationRole;
  can_modify: boolean;
  can_delegate: boolean;
}

export interface PermissionBundle {
  schema_version: string;
  permission_id: string;
  entity_id: string;
  scope: PermissionScope;
  scope_entity_id: string | null;
  permissions: PermissionEntry[];
  effective_from: string; // ISO 8601
  effective_until: string | null;
  delegation_chain: DelegationEntry[];
  default_permission: PermissionValue;
  created_by: string;
  updated_at: string; // ISO 8601
  version: number;
}

export interface AuditLogEntry {
  id: string;
  timestamp: string; // ISO 8601
  requester_name: string;
  requester_type: PlatformType;
  permission_type: PermissionType;
  work_title: string | null;
  scope: PermissionScope;
  result: PermissionValue;
  reason: string;
}
