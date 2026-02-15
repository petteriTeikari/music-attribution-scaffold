/**
 * Central registry of music AI ecosystem platforms.
 *
 * Real-world companies across attribution infrastructure, AI generation,
 * licensing/certification, and open-source tools. Used in MCP scenario
 * demos and audit log entries.
 */

import { PlatformType } from "@/lib/types/enums";

export interface EcosystemPlatform {
  id: string;
  name: string;
  type: (typeof PlatformType)[keyof typeof PlatformType];
  description: string;
  url: string;
  tagline: string;
  fairly_trained_certified: boolean;
}

export const ECOSYSTEM_PLATFORMS: EcosystemPlatform[] = [
  // --- AI Generators ---
  {
    id: "suno",
    name: "Suno",
    type: PlatformType.AI_GENERATOR,
    description: "Text-to-music generation platform",
    url: "https://suno.com",
    tagline: "Make any song you can imagine",
    fairly_trained_certified: false,
  },
  {
    id: "udio",
    name: "Udio",
    type: PlatformType.AI_GENERATOR,
    description: "AI music creation and generation",
    url: "https://udio.com",
    tagline: "Create music with AI",
    fairly_trained_certified: false,
  },
  {
    id: "soundverse",
    name: "Soundverse",
    type: PlatformType.AI_GENERATOR,
    description: "AI music assistant for creators",
    url: "https://soundverse.ai",
    tagline: "Your AI music co-pilot",
    fairly_trained_certified: false,
  },
  {
    id: "boomy",
    name: "Boomy",
    type: PlatformType.AI_GENERATOR,
    description: "Instant AI song creation and distribution",
    url: "https://boomy.com",
    tagline: "Create original songs in seconds",
    fairly_trained_certified: false,
  },

  // --- Attribution Infrastructure ---
  {
    id: "sureel-ai",
    name: "Sureel AI",
    type: PlatformType.ATTRIBUTION_INFRA,
    description: "AI-powered music rights and attribution platform",
    url: "https://sureel.ai",
    tagline: "Transparent music attribution",
    fairly_trained_certified: true,
  },
  {
    id: "musical-ai",
    name: "Musical AI",
    type: PlatformType.ATTRIBUTION_INFRA,
    description: "Music identification and attribution infrastructure",
    url: "https://musical.ai",
    tagline: "Attribution infrastructure for the AI era",
    fairly_trained_certified: true,
  },
  {
    id: "prorata-ai",
    name: "ProRata.ai",
    type: PlatformType.ATTRIBUTION_INFRA,
    description: "Fair attribution and compensation for AI-used content",
    url: "https://prorata.ai",
    tagline: "Fair value for every contribution",
    fairly_trained_certified: true,
  },

  // --- LLM Providers ---
  {
    id: "openai",
    name: "OpenAI",
    type: PlatformType.LLM_PROVIDER,
    description: "Large language model provider (GPT, DALL-E, Jukebox)",
    url: "https://openai.com",
    tagline: "Creating safe AGI",
    fairly_trained_certified: false,
  },
  {
    id: "anthropic",
    name: "Anthropic",
    type: PlatformType.LLM_PROVIDER,
    description: "AI safety company (Claude)",
    url: "https://anthropic.com",
    tagline: "AI safety research and products",
    fairly_trained_certified: false,
  },

  // --- Streaming ---
  {
    id: "spotify",
    name: "Spotify",
    type: PlatformType.STREAMING,
    description: "Music streaming platform",
    url: "https://spotify.com",
    tagline: "Music for everyone",
    fairly_trained_certified: false,
  },
  {
    id: "soundcloud",
    name: "SoundCloud",
    type: PlatformType.STREAMING,
    description: "Artist-first streaming and distribution with Auracles integration",
    url: "https://soundcloud.com",
    tagline: "Hear the world's sounds",
    fairly_trained_certified: false,
  },

  // --- Rights Organizations ---
  {
    id: "prs-for-music",
    name: "PRS for Music",
    type: PlatformType.RIGHTS_ORG,
    description: "UK performing rights society",
    url: "https://prsformusic.com",
    tagline: "Supporting music creators",
    fairly_trained_certified: false,
  },
  {
    id: "ascap",
    name: "ASCAP",
    type: PlatformType.RIGHTS_ORG,
    description: "American Society of Composers, Authors and Publishers",
    url: "https://ascap.com",
    tagline: "We create music opportunities",
    fairly_trained_certified: false,
  },
  {
    id: "stim",
    name: "STIM",
    type: PlatformType.RIGHTS_ORG,
    description: "Swedish performing rights organization",
    url: "https://stim.se",
    tagline: "Music creates value",
    fairly_trained_certified: false,
  },

  // --- Certification ---
  {
    id: "fairly-trained",
    name: "Fairly Trained",
    type: PlatformType.CERTIFICATION_BODY,
    description: "Certification for AI models trained on licensed data",
    url: "https://fairlytrained.org",
    tagline: "Certifying ethical AI training",
    fairly_trained_certified: true,
  },

  // --- Registry ---
  {
    id: "soundexchange",
    name: "SoundExchange",
    type: PlatformType.REGISTRY,
    description: "Digital performance rights organization and ISRC registry",
    url: "https://soundexchange.com",
    tagline: "Powering the future of music",
    fairly_trained_certified: false,
  },

  // --- Individual ---
  {
    id: "jen-futureverse",
    name: "Jen (Futureverse)",
    type: PlatformType.INDIVIDUAL,
    description:
      "Imogen Heap's AI model partner — StyleFilter models with ~70% artist revenue share via Auracles consent infrastructure",
    url: "https://jen.world",
    tagline: "Artist-authorized AI music creation",
    fairly_trained_certified: true,
  },
  {
    id: "independent-producer",
    name: "Independent Producer",
    type: PlatformType.INDIVIDUAL,
    description: "Independent music producer seeking sample clearance",
    url: "",
    tagline: "Independent creator",
    fairly_trained_certified: false,
  },
];

/** Look up a platform by ID. */
export function getPlatform(id: string): EcosystemPlatform | undefined {
  return ECOSYSTEM_PLATFORMS.find((p) => p.id === id);
}

/** Get all platforms of a given type. */
export function getPlatformsByType(
  type: (typeof PlatformType)[keyof typeof PlatformType],
): EcosystemPlatform[] {
  return ECOSYSTEM_PLATFORMS.filter((p) => p.type === type);
}
