/**
 * Tests for ExternalLinkBadge component.
 */
import { describe, it, expect, vi } from "vitest";
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { ExternalLinkBadge } from "@/components/works/external-link-badge";

describe("ExternalLinkBadge", () => {
  it("renders anchor with target=_blank and noopener noreferrer", () => {
    render(
      <ExternalLinkBadge
        source="musicbrainz"
        url="https://musicbrainz.org/recording/abc"
      />,
    );
    const link = screen.getByRole("link", { name: /MusicBrainz/i });
    expect(link).toHaveAttribute("target", "_blank");
    expect(link).toHaveAttribute("rel", "noopener noreferrer");
    expect(link).toHaveAttribute(
      "href",
      "https://musicbrainz.org/recording/abc",
    );
  });

  it("uses musicbrainz color token", () => {
    render(
      <ExternalLinkBadge
        source="musicbrainz"
        url="https://musicbrainz.org/recording/abc"
      />,
    );
    const link = screen.getByRole("link", { name: /MusicBrainz/i });
    expect(link.style.color).toBe("var(--color-source-musicbrainz)");
  });

  it("uses discogs color token", () => {
    render(
      <ExternalLinkBadge
        source="discogs"
        url="https://www.discogs.com/master/123"
      />,
    );
    const link = screen.getByRole("link", { name: /Discogs/i });
    expect(link.style.color).toBe("var(--color-source-discogs)");
  });

  it("renders nothing when URL is empty string", () => {
    const { container } = render(
      <ExternalLinkBadge source="musicbrainz" url="" />,
    );
    expect(container.innerHTML).toBe("");
  });

  it("calls onClick and stopPropagation on click", async () => {
    const user = userEvent.setup();
    const onClick = vi.fn();
    const stopPropagation = vi.fn();

    render(
      // eslint-disable-next-line jsx-a11y/click-events-have-key-events, jsx-a11y/no-static-element-interactions
      <div onClick={stopPropagation}>
        <ExternalLinkBadge
          source="musicbrainz"
          url="https://musicbrainz.org/recording/abc"
          onClick={onClick}
        />
      </div>,
    );

    const link = screen.getByRole("link", { name: /MusicBrainz/i });
    await user.click(link);

    expect(onClick).toHaveBeenCalledTimes(1);
    // stopPropagation means the parent div should NOT receive the click
    expect(stopPropagation).not.toHaveBeenCalled();
  });
});
