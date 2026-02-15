/**
 * Tests for external links data module.
 */
import { describe, it, expect } from "vitest";
import {
  getExternalLinks,
  MUSICBRAINZ_ARTIST_URL,
  MUSICBRAINZ_ARTIST_ID,
} from "@/lib/data/external-links";

describe("getExternalLinks", () => {
  it("returns both URLs for work-001 (full coverage)", () => {
    const links = getExternalLinks("work-001");
    expect(links.musicbrainz_recording_url).toBe(
      "https://musicbrainz.org/recording/c257113a-c792-4f8d-b18f-2bf1fe8f863f",
    );
    expect(links.discogs_master_url).toBe(
      "https://www.discogs.com/master/17476",
    );
  });

  it("returns null MusicBrainz + valid Discogs for work-002 (partial)", () => {
    const links = getExternalLinks("work-002");
    expect(links.musicbrainz_recording_url).toBeNull();
    expect(links.discogs_master_url).toBe(
      "https://www.discogs.com/master/3230830",
    );
  });

  it("returns both nulls for work-008 (no coverage)", () => {
    const links = getExternalLinks("work-008");
    expect(links.musicbrainz_recording_url).toBeNull();
    expect(links.discogs_master_url).toBeNull();
  });

  it("returns both nulls for unknown attribution_id", () => {
    const links = getExternalLinks("work-999");
    expect(links.musicbrainz_recording_url).toBeNull();
    expect(links.discogs_master_url).toBeNull();
  });

  it("generates valid URL formats", () => {
    const links = getExternalLinks("work-001");
    expect(links.musicbrainz_recording_url).toMatch(
      /^https:\/\/musicbrainz\.org\/recording\/[0-9a-f-]+$/,
    );
    expect(links.discogs_master_url).toMatch(
      /^https:\/\/www\.discogs\.com\/master\/\d+$/,
    );
  });
});

describe("MUSICBRAINZ_ARTIST_URL", () => {
  it("exports the correct artist URL", () => {
    expect(MUSICBRAINZ_ARTIST_URL).toBe(
      `https://musicbrainz.org/artist/${MUSICBRAINZ_ARTIST_ID}`,
    );
  });

  it("contains the verified artist ID", () => {
    expect(MUSICBRAINZ_ARTIST_ID).toBe(
      "328d146c-79f1-4eb6-9e40-8ee5710c14e5",
    );
  });
});
