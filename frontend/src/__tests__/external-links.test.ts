/**
 * Tests for external links data module.
 */
import { describe, it, expect } from "vitest";
import {
  getExternalLinks,
  getSourceUrl,
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
    expect(links.discogs_url).toBe(
      "https://www.discogs.com/master/17476",
    );
  });

  it("returns both URLs for work-002 (now has MB recording ID)", () => {
    const links = getExternalLinks("work-002");
    expect(links.musicbrainz_recording_url).toBe(
      "https://musicbrainz.org/recording/76865919-d657-48b9-b6be-79bc25f50260",
    );
    expect(links.discogs_master_url).toBe(
      "https://www.discogs.com/master/3230830",
    );
  });

  it("returns both nulls for work-008 (no coverage)", () => {
    const links = getExternalLinks("work-008");
    expect(links.musicbrainz_recording_url).toBeNull();
    expect(links.discogs_master_url).toBeNull();
    expect(links.discogs_url).toBeNull();
  });

  it("returns both nulls for unknown attribution_id", () => {
    const links = getExternalLinks("work-999");
    expect(links.musicbrainz_recording_url).toBeNull();
    expect(links.discogs_master_url).toBeNull();
    expect(links.discogs_url).toBeNull();
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

  it("returns Discogs release URL when no master exists (work-009)", () => {
    const links = getExternalLinks("work-009");
    expect(links.musicbrainz_recording_url).toBe(
      "https://musicbrainz.org/recording/db692772-333f-4c00-a080-7f25cad8e3a0",
    );
    expect(links.discogs_master_url).toBeNull();
    expect(links.discogs_url).toBe(
      "https://www.discogs.com/release/35937472",
    );
  });
});

describe("getSourceUrl", () => {
  it("returns MB recording URL for MUSICBRAINZ source", () => {
    const url = getSourceUrl("MUSICBRAINZ", "work-001");
    expect(url).toBe(
      "https://musicbrainz.org/recording/c257113a-c792-4f8d-b18f-2bf1fe8f863f",
    );
  });

  it("returns Discogs URL for DISCOGS source", () => {
    const url = getSourceUrl("DISCOGS", "work-001");
    expect(url).toBe("https://www.discogs.com/master/17476");
  });

  it("returns Discogs release URL for DISCOGS source on work-009", () => {
    const url = getSourceUrl("DISCOGS", "work-009");
    expect(url).toBe("https://www.discogs.com/release/35937472");
  });

  it("returns null for non-linkable sources", () => {
    expect(getSourceUrl("ACOUSTID", "work-001")).toBeNull();
    expect(getSourceUrl("ARTIST_INPUT", "work-001")).toBeNull();
    expect(getSourceUrl("FILE_METADATA", "work-001")).toBeNull();
  });

  it("returns null for unknown work", () => {
    expect(getSourceUrl("MUSICBRAINZ", "work-999")).toBeNull();
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
