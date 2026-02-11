import { describe, it, expect } from "vitest";
import { render, screen } from "@testing-library/react";
import { SourceTag } from "./source-tag";

describe("SourceTag", () => {
  it("renders MusicBrainz label", () => {
    render(<SourceTag source="MUSICBRAINZ" />);
    expect(screen.getByText("MusicBrainz")).toBeInTheDocument();
  });

  it("renders Discogs label", () => {
    render(<SourceTag source="DISCOGS" />);
    expect(screen.getByText("Discogs")).toBeInTheDocument();
  });

  it("renders AcoustID label", () => {
    render(<SourceTag source="ACOUSTID" />);
    expect(screen.getByText("AcoustID")).toBeInTheDocument();
  });

  it("renders Artist label for ARTIST_INPUT", () => {
    render(<SourceTag source="ARTIST_INPUT" />);
    expect(screen.getByText("Artist")).toBeInTheDocument();
  });

  it("renders File label for FILE_METADATA", () => {
    render(<SourceTag source="FILE_METADATA" />);
    expect(screen.getByText("File")).toBeInTheDocument();
  });
});
