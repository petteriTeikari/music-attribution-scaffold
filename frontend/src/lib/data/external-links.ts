/**
 * Verified external database links for Imogen Heap works.
 *
 * External IDs are a frontend display concern (not part of AttributionRecord schema).
 * All IDs have been manually verified against MusicBrainz and Discogs — no hallucinated links.
 */

import type { Source } from "@/lib/types/enums";

export const MUSICBRAINZ_ARTIST_ID = "328d146c-79f1-4eb6-9e40-8ee5710c14e5";
export const MUSICBRAINZ_ARTIST_URL = `https://musicbrainz.org/artist/${MUSICBRAINZ_ARTIST_ID}`;

export interface ExternalLinks {
  musicbrainz_recording_url: string | null;
  discogs_master_url: string | null;
  /** Generic Discogs URL — master if available, otherwise release. */
  discogs_url: string | null;
}

interface ExternalIds {
  musicbrainz_recording_id: string | null;
  discogs_master_id: string | null;
  /** Fallback when no master exists (e.g. single-only releases). */
  discogs_release_id: string | null;
}

/**
 * Verified external IDs per attribution_id.
 * null = not found or not yet verified. Never guessed.
 */
const EXTERNAL_IDS: Record<string, ExternalIds> = {
  "work-001": {
    musicbrainz_recording_id: "c257113a-c792-4f8d-b18f-2bf1fe8f863f",
    discogs_master_id: "17476",
    discogs_release_id: null,
  },
  "work-002": {
    musicbrainz_recording_id: "76865919-d657-48b9-b6be-79bc25f50260",
    discogs_master_id: "3230830",
    discogs_release_id: null,
  },
  "work-003": {
    musicbrainz_recording_id: "dffcffa4-e27c-46f7-9e7e-b56296432339",
    discogs_master_id: "213632",
    discogs_release_id: null,
  },
  "work-004": {
    musicbrainz_recording_id: "3b4a3bd3-944d-45f4-ac92-ab72a7448ba2",
    discogs_master_id: "17439",
    discogs_release_id: null,
  },
  "work-005": {
    musicbrainz_recording_id: "d871b5ab-0a48-4b93-95d7-be3e6a599248",
    discogs_master_id: "17472",
    discogs_release_id: null,
  },
  "work-006": {
    musicbrainz_recording_id: "850aa908-f047-46f3-a190-d037feddf38f",
    discogs_master_id: "17483",
    discogs_release_id: null,
  },
  "work-007": {
    musicbrainz_recording_id: "c38db271-3579-41ca-94d3-3238d34b173a",
    discogs_master_id: "173677",
    discogs_release_id: null,
  },
  "work-008": {
    musicbrainz_recording_id: null,
    discogs_master_id: null,
    discogs_release_id: null,
  },
  "work-009": {
    musicbrainz_recording_id: "db692772-333f-4c00-a080-7f25cad8e3a0",
    discogs_master_id: null,
    discogs_release_id: "35937472",
  },
};

/**
 * Get external links for a work by attribution_id.
 * Returns resolved URLs (not raw IDs).
 */
export function getExternalLinks(attributionId: string): ExternalLinks {
  const ids = EXTERNAL_IDS[attributionId];
  if (!ids) {
    return { musicbrainz_recording_url: null, discogs_master_url: null, discogs_url: null };
  }

  const discogsUrl = ids.discogs_master_id
    ? `https://www.discogs.com/master/${ids.discogs_master_id}`
    : ids.discogs_release_id
      ? `https://www.discogs.com/release/${ids.discogs_release_id}`
      : null;

  return {
    musicbrainz_recording_url: ids.musicbrainz_recording_id
      ? `https://musicbrainz.org/recording/${ids.musicbrainz_recording_id}`
      : null,
    discogs_master_url: ids.discogs_master_id
      ? `https://www.discogs.com/master/${ids.discogs_master_id}`
      : null,
    discogs_url: discogsUrl,
  };
}

/**
 * Get the external URL for a specific source on a given work.
 * Returns null if no verified link exists for that source.
 */
export function getSourceUrl(source: Source, attributionId: string): string | null {
  const links = getExternalLinks(attributionId);
  switch (source) {
    case "MUSICBRAINZ":
      return links.musicbrainz_recording_url;
    case "DISCOGS":
      return links.discogs_url;
    default:
      return null;
  }
}
