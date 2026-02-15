/**
 * Mock permission data for Imogen Heap's catalog.
 *
 * Demonstrates the MCP permission patchbay with realistic ecosystem
 * scenarios: AI generators, LLM providers, attribution infrastructure,
 * certification bodies, rights organizations, and individuals.
 *
 * Key insight: Voice cloning is NOT a flat DENY — it's conditional on
 * the requester. Jen/Futureverse (authorized via Auracles) gets
 * ALLOW_WITH_ROYALTY; unknown platforms get DENY.
 */

import type { PermissionBundle, AuditLogEntry } from "@/lib/types/permissions";
import { PlatformType } from "@/lib/types/enums";

export const MOCK_PERMISSIONS: PermissionBundle = {
  schema_version: "1.0.0",
  permission_id: "perm-imogen-catalog",
  entity_id: "artist-imogen-heap",
  scope: "CATALOG",
  scope_entity_id: null,
  permissions: [
    {
      permission_type: "STREAM",
      value: "ALLOW",
      conditions: [],
      royalty_rate: null,
      attribution_requirement: null,
      territory: null,
    },
    {
      permission_type: "DOWNLOAD",
      value: "ALLOW_WITH_ROYALTY",
      conditions: [],
      royalty_rate: 0.15,
      attribution_requirement: null,
      territory: null,
    },
    {
      permission_type: "SYNC_LICENSE",
      value: "ASK",
      conditions: [{ condition_type: "approval_required", value: "true" }],
      royalty_rate: null,
      attribution_requirement: null,
      territory: null,
    },
    {
      permission_type: "AI_TRAINING",
      value: "ALLOW_WITH_ATTRIBUTION",
      conditions: [
        { condition_type: "partner_verified", value: "true" },
        { condition_type: "opt_out_available", value: "true" },
      ],
      royalty_rate: null,
      attribution_requirement: "Credit 'Imogen Heap' in training data manifest",
      territory: null,
    },
    {
      permission_type: "VOICE_CLONING",
      value: "DENY",
      conditions: [
        {
          condition_type: "unless_authorized_platform",
          value: "jen-futureverse",
        },
      ],
      royalty_rate: null,
      attribution_requirement: null,
      territory: null,
    },
    {
      permission_type: "STYLE_LEARNING",
      value: "ASK",
      conditions: [{ condition_type: "case_by_case", value: "true" }],
      royalty_rate: null,
      attribution_requirement: null,
      territory: null,
    },
    {
      permission_type: "LYRICS_IN_CHATBOTS",
      value: "ALLOW_WITH_ATTRIBUTION",
      conditions: [],
      royalty_rate: null,
      attribution_requirement:
        "Include songwriter credit and link to official lyrics",
      territory: null,
    },
    {
      permission_type: "COVER_VERSIONS",
      value: "ALLOW_WITH_ROYALTY",
      conditions: [],
      royalty_rate: 0.091,
      attribution_requirement: null,
      territory: null,
    },
    {
      permission_type: "REMIX",
      value: "ASK",
      conditions: [{ condition_type: "approval_required", value: "true" }],
      royalty_rate: null,
      attribution_requirement: null,
      territory: null,
    },
    {
      permission_type: "SAMPLE",
      value: "ASK",
      conditions: [{ condition_type: "clearance_required", value: "true" }],
      royalty_rate: null,
      attribution_requirement: null,
      territory: null,
    },
    {
      permission_type: "DERIVATIVE_WORK",
      value: "ASK",
      conditions: [],
      royalty_rate: null,
      attribution_requirement: null,
      territory: null,
    },
    {
      permission_type: "AI_TRAINING_COMPOSITION",
      value: "ALLOW_WITH_ATTRIBUTION",
      conditions: [{ condition_type: "partner_verified", value: "true" }],
      royalty_rate: null,
      attribution_requirement:
        "Credit 'Imogen Heap' as composer in training manifest",
      territory: null,
    },
    {
      permission_type: "AI_TRAINING_RECORDING",
      value: "ASK",
      conditions: [{ condition_type: "case_by_case", value: "true" }],
      royalty_rate: null,
      attribution_requirement: null,
      territory: null,
    },
    {
      permission_type: "DATASET_INCLUSION",
      value: "ALLOW_WITH_ATTRIBUTION",
      conditions: [
        { condition_type: "certification_required", value: "true" },
      ],
      royalty_rate: null,
      attribution_requirement:
        "Include in Fairly Trained certified datasets only",
      territory: null,
    },
  ],
  effective_from: "2025-06-01T00:00:00Z",
  effective_until: null,
  delegation_chain: [
    {
      entity_id: "artist-imogen-heap",
      entity_name: "Imogen Heap",
      role: "OWNER",
      can_modify: true,
      can_delegate: true,
    },
    {
      entity_id: "mgmt-megaphonic",
      entity_name: "Megaphonic Management",
      role: "MANAGER",
      can_modify: true,
      can_delegate: false,
    },
    {
      entity_id: "platform-auracles",
      entity_name: "Auracles (Consent Infrastructure)",
      role: "DELEGATE",
      can_modify: false,
      can_delegate: true,
    },
  ],
  default_permission: "ASK",
  created_by: "artist-imogen-heap",
  updated_at: "2026-01-15T10:30:00Z",
  version: 4,
};

export const MOCK_AUDIT_LOG: AuditLogEntry[] = [
  {
    id: "audit-001",
    timestamp: "2026-02-10T14:22:00Z",
    requester_name: "Suno AI",
    requester_type: PlatformType.AI_GENERATOR,
    permission_type: "AI_TRAINING",
    work_title: null,
    scope: "CATALOG",
    result: "ALLOW_WITH_ATTRIBUTION",
    reason:
      "Verified partner (post-settlement) — attribution requirement met",
  },
  {
    id: "audit-002",
    timestamp: "2026-02-09T16:30:00Z",
    requester_name: "Udio",
    requester_type: PlatformType.AI_GENERATOR,
    permission_type: "AI_TRAINING_RECORDING",
    work_title: "Hide and Seek",
    scope: "RECORDING",
    result: "ASK",
    reason:
      "Post-settlement, recording-level training requires case-by-case approval",
  },
  {
    id: "audit-003",
    timestamp: "2026-02-09T09:15:00Z",
    requester_name: "VoiceClone.ai",
    requester_type: PlatformType.AI_GENERATOR,
    permission_type: "VOICE_CLONING",
    work_title: "Hide and Seek",
    scope: "RECORDING",
    result: "DENY",
    reason: "Voice cloning denied — unknown platform, not Auracles-authorized",
  },
  {
    id: "audit-004",
    timestamp: "2026-02-08T18:45:00Z",
    requester_name: "Jen (Futureverse)",
    requester_type: PlatformType.INDIVIDUAL,
    permission_type: "VOICE_CLONING",
    work_title: null,
    scope: "CATALOG",
    result: "ALLOW_WITH_ROYALTY",
    reason:
      "Authorized via Auracles consent infrastructure — 70% revenue share",
  },
  {
    id: "audit-005",
    timestamp: "2026-02-08T16:45:00Z",
    requester_name: "Spotify",
    requester_type: PlatformType.STREAMING,
    permission_type: "STREAM",
    work_title: null,
    scope: "CATALOG",
    result: "ALLOW",
    reason: "Streaming is allowed for all works",
  },
  {
    id: "audit-005a",
    timestamp: "2026-02-08T15:30:00Z",
    requester_name: "SoundCloud",
    requester_type: PlatformType.STREAMING,
    permission_type: "STREAM",
    work_title: null,
    scope: "CATALOG",
    result: "ALLOW",
    reason:
      "Auracles-connected platform — streaming rights inherited from consent profile",
  },
  {
    id: "audit-005b",
    timestamp: "2026-02-08T15:31:00Z",
    requester_name: "SoundCloud",
    requester_type: PlatformType.STREAMING,
    permission_type: "AI_TRAINING",
    work_title: null,
    scope: "CATALOG",
    result: "DENY",
    reason:
      "SoundCloud 2025 policy: will not use artist content for generative AI training",
  },
  {
    id: "audit-006",
    timestamp: "2026-02-07T14:00:00Z",
    requester_name: "OpenAI",
    requester_type: PlatformType.LLM_PROVIDER,
    permission_type: "LYRICS_IN_CHATBOTS",
    work_title: null,
    scope: "CATALOG",
    result: "ALLOW_WITH_ATTRIBUTION",
    reason: "Verified partner — songwriter credit required in chatbot output",
  },
  {
    id: "audit-007",
    timestamp: "2026-02-07T11:30:00Z",
    requester_name: "PRS for Music",
    requester_type: PlatformType.RIGHTS_ORG,
    permission_type: "SYNC_LICENSE",
    work_title: "Tiny Human",
    scope: "WORK",
    result: "ASK",
    reason: "Sync license requires case-by-case approval",
  },
  {
    id: "audit-008",
    timestamp: "2026-02-06T15:20:00Z",
    requester_name: "Anthropic",
    requester_type: PlatformType.LLM_PROVIDER,
    permission_type: "AI_TRAINING_COMPOSITION",
    work_title: null,
    scope: "CATALOG",
    result: "ALLOW_WITH_ATTRIBUTION",
    reason: "Composition training allowed — credit required in manifest",
  },
  {
    id: "audit-009",
    timestamp: "2026-02-06T08:00:00Z",
    requester_name: "Musical AI",
    requester_type: PlatformType.ATTRIBUTION_INFRA,
    permission_type: "AI_TRAINING",
    work_title: null,
    scope: "CATALOG",
    result: "ALLOW_WITH_ATTRIBUTION",
    reason:
      "Fairly Trained certified platform — attribution query for catalog inclusion",
  },
  {
    id: "audit-010",
    timestamp: "2026-02-05T13:20:00Z",
    requester_name: "Independent Producer",
    requester_type: PlatformType.INDIVIDUAL,
    permission_type: "SAMPLE",
    work_title: "Hide and Seek",
    scope: "RECORDING",
    result: "ASK",
    reason: "Sample clearance required — forwarded to management",
  },
  {
    id: "audit-011",
    timestamp: "2026-02-04T10:00:00Z",
    requester_name: "Suno AI",
    requester_type: PlatformType.AI_GENERATOR,
    permission_type: "STYLE_LEARNING",
    work_title: null,
    scope: "CATALOG",
    result: "ASK",
    reason: "Style learning requires case-by-case review",
  },
  {
    id: "audit-012",
    timestamp: "2026-02-03T09:30:00Z",
    requester_name: "Fairly Trained",
    requester_type: PlatformType.CERTIFICATION_BODY,
    permission_type: "DATASET_INCLUSION",
    work_title: null,
    scope: "CATALOG",
    result: "ALLOW_WITH_ATTRIBUTION",
    reason: "Certification audit — catalog eligible for Fairly Trained badge",
  },
  {
    id: "audit-013",
    timestamp: "2026-02-02T14:15:00Z",
    requester_name: "STIM",
    requester_type: PlatformType.RIGHTS_ORG,
    permission_type: "COVER_VERSIONS",
    work_title: "Just for Now",
    scope: "WORK",
    result: "ALLOW_WITH_ROYALTY",
    reason: "Collective license — statutory royalty rate 9.1%",
  },
  {
    id: "audit-014",
    timestamp: "2026-02-01T11:45:00Z",
    requester_name: "Soundverse",
    requester_type: PlatformType.AI_GENERATOR,
    permission_type: "AI_TRAINING_COMPOSITION",
    work_title: null,
    scope: "CATALOG",
    result: "ALLOW_WITH_ATTRIBUTION",
    reason: "Composition training — attribution manifest required",
  },
  {
    id: "audit-015",
    timestamp: "2026-01-30T16:00:00Z",
    requester_name: "Boomy",
    requester_type: PlatformType.AI_GENERATOR,
    permission_type: "AI_TRAINING",
    work_title: null,
    scope: "CATALOG",
    result: "ALLOW_WITH_ATTRIBUTION",
    reason: "Verified partner — full catalog training with attribution",
  },
  {
    id: "audit-016",
    timestamp: "2026-01-28T10:30:00Z",
    requester_name: "SoundExchange",
    requester_type: PlatformType.REGISTRY,
    permission_type: "STREAM",
    work_title: null,
    scope: "CATALOG",
    result: "ALLOW",
    reason: "ISRC registry check — catalog streaming rights confirmed",
  },
  {
    id: "audit-017",
    timestamp: "2026-01-25T09:00:00Z",
    requester_name: "ASCAP",
    requester_type: PlatformType.RIGHTS_ORG,
    permission_type: "COVER_VERSIONS",
    work_title: "Goodnight and Go",
    scope: "WORK",
    result: "ALLOW_WITH_ROYALTY",
    reason: "Mechanical license — statutory royalty rate 9.1%",
  },
  {
    id: "audit-018",
    timestamp: "2026-01-22T14:30:00Z",
    requester_name: "ProRata.ai",
    requester_type: PlatformType.ATTRIBUTION_INFRA,
    permission_type: "AI_TRAINING",
    work_title: null,
    scope: "CATALOG",
    result: "ALLOW_WITH_ATTRIBUTION",
    reason:
      "Fair attribution platform — catalog indexed for compensation tracking",
  },
];

export interface MCPScenario {
  id: string;
  title: string;
  requester: string;
  requester_type: (typeof PlatformType)[keyof typeof PlatformType];
  permission: string;
  result: string;
  description: string;
  category: "ai_generator" | "llm_provider" | "attribution" | "individual";
  mcpRequest: {
    method: string;
    params: Record<string, string>;
  };
  mcpResponse: Record<string, unknown>;
}

export const MCP_SCENARIOS: MCPScenario[] = [
  {
    id: "scenario-1",
    title: "AI Training — Verified Partner",
    requester: "Suno",
    requester_type: PlatformType.AI_GENERATOR,
    permission: "AI_TRAINING",
    result: "ALLOW_WITH_ATTRIBUTION",
    category: "ai_generator",
    description:
      "Post-settlement verified partner requests catalog training access. Permission granted with attribution in data manifest.",
    mcpRequest: {
      method: "permissions/check",
      params: {
        entity_id: "artist-imogen-heap",
        permission_type: "AI_TRAINING",
        requester_id: "suno-verified",
      },
    },
    mcpResponse: {
      result: "ALLOW_WITH_ATTRIBUTION",
      attribution_requirement:
        "Credit 'Imogen Heap' in training data manifest",
      conditions: ["partner_verified", "opt_out_available"],
    },
  },
  {
    id: "scenario-2",
    title: "Recording Training — Case-by-Case",
    requester: "Udio",
    requester_type: PlatformType.AI_GENERATOR,
    permission: "AI_TRAINING_RECORDING",
    result: "ASK",
    category: "ai_generator",
    description:
      "Post-settlement platform requests recording-level training. Requires individual approval — composition vs. recording distinction matters.",
    mcpRequest: {
      method: "permissions/check",
      params: {
        entity_id: "artist-imogen-heap",
        permission_type: "AI_TRAINING_RECORDING",
        requester_id: "udio-settlement",
      },
    },
    mcpResponse: {
      result: "ASK",
      reason:
        "Recording-level training requires case-by-case approval post-settlement",
      contact: "management@megaphonic.com",
    },
  },
  {
    id: "scenario-3",
    title: "Voice Cloning — Authorized (Jen)",
    requester: "Jen (Futureverse)",
    requester_type: PlatformType.INDIVIDUAL,
    permission: "VOICE_CLONING",
    result: "ALLOW_WITH_ROYALTY",
    category: "individual",
    description:
      "Authorized platform via Auracles consent infrastructure. StyleFilter AI models with ~70% artist revenue share. Same permission type as scenario 4 — different result.",
    mcpRequest: {
      method: "permissions/check",
      params: {
        entity_id: "artist-imogen-heap",
        permission_type: "VOICE_CLONING",
        requester_id: "jen-futureverse-auracles",
      },
    },
    mcpResponse: {
      result: "ALLOW_WITH_ROYALTY",
      royalty_rate: 0.7,
      authorization: "auracles-consent-infrastructure",
      note: "StyleFilter AI models — artist-authorized voice synthesis",
    },
  },
  {
    id: "scenario-4",
    title: "Voice Cloning — Denied (Unknown)",
    requester: "VoiceClone.ai",
    requester_type: PlatformType.AI_GENERATOR,
    permission: "VOICE_CLONING",
    result: "DENY",
    category: "ai_generator",
    description:
      "Unknown platform requests voice cloning. Blanket deny — not Auracles-authorized. Same permission type as scenario 3 — different result.",
    mcpRequest: {
      method: "permissions/check",
      params: {
        entity_id: "artist-imogen-heap",
        permission_type: "VOICE_CLONING",
        requester_id: "voiceclone-unknown",
      },
    },
    mcpResponse: {
      result: "DENY",
      reason:
        "Voice cloning denied for unauthorized platforms. Apply via Auracles for authorization.",
    },
  },
  {
    id: "scenario-5",
    title: "Lyrics in Chatbot — Attributed",
    requester: "OpenAI",
    requester_type: PlatformType.LLM_PROVIDER,
    permission: "LYRICS_IN_CHATBOTS",
    result: "ALLOW_WITH_ATTRIBUTION",
    category: "llm_provider",
    description:
      "Verified LLM provider requests lyrics display in chatbot. Allowed with songwriter credit and official link.",
    mcpRequest: {
      method: "permissions/check",
      params: {
        entity_id: "artist-imogen-heap",
        permission_type: "LYRICS_IN_CHATBOTS",
        requester_id: "openai-verified",
      },
    },
    mcpResponse: {
      result: "ALLOW_WITH_ATTRIBUTION",
      attribution_requirement:
        "Include songwriter credit and link to official lyrics",
    },
  },
  {
    id: "scenario-6",
    title: "Composition Training — Attributed",
    requester: "Anthropic",
    requester_type: PlatformType.LLM_PROVIDER,
    permission: "AI_TRAINING_COMPOSITION",
    result: "ALLOW_WITH_ATTRIBUTION",
    category: "llm_provider",
    description:
      "LLM provider requests composition-level training specifically. Finer-grained than general AI_TRAINING — composition structure only.",
    mcpRequest: {
      method: "permissions/check",
      params: {
        entity_id: "artist-imogen-heap",
        permission_type: "AI_TRAINING_COMPOSITION",
        requester_id: "anthropic-verified",
      },
    },
    mcpResponse: {
      result: "ALLOW_WITH_ATTRIBUTION",
      attribution_requirement:
        "Credit 'Imogen Heap' as composer in training manifest",
      scope: "composition_structure_only",
    },
  },
  {
    id: "scenario-7",
    title: "Attribution Query — Fairly Trained",
    requester: "Musical AI",
    requester_type: PlatformType.ATTRIBUTION_INFRA,
    permission: "AI_TRAINING",
    result: "ALLOW_WITH_ATTRIBUTION",
    category: "attribution",
    description:
      "Fairly Trained certified attribution platform queries catalog for inclusion. Demonstrates infrastructure-to-infrastructure MCP handshake.",
    mcpRequest: {
      method: "permissions/check",
      params: {
        entity_id: "artist-imogen-heap",
        permission_type: "AI_TRAINING",
        requester_id: "musical-ai-certified",
      },
    },
    mcpResponse: {
      result: "ALLOW_WITH_ATTRIBUTION",
      attribution_requirement:
        "Credit 'Imogen Heap' in training data manifest",
      certification: "fairly_trained_verified",
    },
  },
  {
    id: "scenario-8",
    title: "Dataset Audit — Certification",
    requester: "Fairly Trained",
    requester_type: PlatformType.CERTIFICATION_BODY,
    permission: "DATASET_INCLUSION",
    result: "ALLOW_WITH_ATTRIBUTION",
    category: "attribution",
    description:
      "Certification body auditing dataset composition. Catalog is eligible for inclusion in Fairly Trained certified datasets.",
    mcpRequest: {
      method: "permissions/check",
      params: {
        entity_id: "artist-imogen-heap",
        permission_type: "DATASET_INCLUSION",
        requester_id: "fairly-trained-audit",
      },
    },
    mcpResponse: {
      result: "ALLOW_WITH_ATTRIBUTION",
      attribution_requirement:
        "Include in Fairly Trained certified datasets only",
      audit_status: "eligible",
    },
  },
  {
    id: "scenario-9",
    title: "Streaming Check — Standard",
    requester: "Spotify",
    requester_type: PlatformType.STREAMING,
    permission: "STREAM",
    result: "ALLOW",
    category: "individual",
    description:
      "Standard streaming platform permission check. Immediate allow — no conditions or attribution required.",
    mcpRequest: {
      method: "permissions/check",
      params: {
        entity_id: "artist-imogen-heap",
        permission_type: "STREAM",
        requester_id: "spotify-platform",
      },
    },
    mcpResponse: {
      result: "ALLOW",
    },
  },
  {
    id: "scenario-10",
    title: "Sample Clearance — Requires Approval",
    requester: "Independent Producer",
    requester_type: PlatformType.INDIVIDUAL,
    permission: "SAMPLE",
    result: "ASK",
    category: "individual",
    description:
      "Independent producer requests sample clearance for 'Hide and Seek'. Forwarded to management — human-in-the-loop required.",
    mcpRequest: {
      method: "permissions/check",
      params: {
        entity_id: "artist-imogen-heap",
        permission_type: "SAMPLE",
        requester_id: "producer-independent",
        scope_entity_id: "work-001",
      },
    },
    mcpResponse: {
      result: "ASK",
      reason: "Sample clearance required",
      contact: "management@megaphonic.com",
    },
  },
];
