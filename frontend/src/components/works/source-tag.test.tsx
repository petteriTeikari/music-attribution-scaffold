import { describe, it, expect, vi } from "vitest";
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
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

  it("renders as span when no href or onNavigate", () => {
    render(<SourceTag source="MUSICBRAINZ" />);
    const el = screen.getByText("MusicBrainz").closest("span");
    expect(el).toBeInTheDocument();
    expect(el?.tagName).toBe("SPAN");
  });

  it("renders as anchor when href provided", () => {
    render(
      <SourceTag
        source="MUSICBRAINZ"
        href="https://musicbrainz.org/recording/abc"
      />,
    );
    const link = screen.getByRole("link", { name: /MusicBrainz/ });
    expect(link).toBeInTheDocument();
    expect(link).toHaveAttribute("href", "https://musicbrainz.org/recording/abc");
    expect(link).toHaveAttribute("target", "_blank");
    expect(link).toHaveAttribute("rel", "noopener noreferrer");
  });

  it("calls onClick when href link is clicked", async () => {
    const user = userEvent.setup();
    const handleClick = vi.fn();
    render(
      <SourceTag
        source="DISCOGS"
        href="https://www.discogs.com/master/123"
        onClick={handleClick}
      />,
    );
    const link = screen.getByRole("link", { name: /Discogs/ });
    await user.click(link);
    expect(handleClick).toHaveBeenCalledOnce();
  });

  it("renders as span with role=link when onNavigate provided (safe inside <a>)", () => {
    render(
      <SourceTag
        source="MUSICBRAINZ"
        onNavigate="https://musicbrainz.org/recording/abc"
      />,
    );
    const el = screen.getByRole("link", { name: /MusicBrainz/ });
    expect(el.tagName).toBe("SPAN");
    expect(el.className).toContain("underline");
    expect(el.className).toContain("cursor-pointer");
  });

  it("opens window and fires onClick on onNavigate click", async () => {
    const user = userEvent.setup();
    const handleClick = vi.fn();
    const openSpy = vi.spyOn(window, "open").mockImplementation(() => null);
    render(
      <SourceTag
        source="DISCOGS"
        onNavigate="https://www.discogs.com/master/123"
        onClick={handleClick}
      />,
    );
    const el = screen.getByRole("link", { name: /Discogs/ });
    await user.click(el);
    expect(openSpy).toHaveBeenCalledWith(
      "https://www.discogs.com/master/123",
      "_blank",
      "noopener,noreferrer",
    );
    expect(handleClick).toHaveBeenCalledOnce();
    openSpy.mockRestore();
  });
});
