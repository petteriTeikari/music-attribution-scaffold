"use client";

interface ExternalLinkBadgeProps {
  source: "musicbrainz" | "discogs";
  url: string;
  className?: string;
  onClick?: () => void;
}

const SOURCE_CONFIG = {
  musicbrainz: {
    label: "MusicBrainz",
    color: "var(--color-source-musicbrainz)",
  },
  discogs: {
    label: "Discogs",
    color: "var(--color-source-discogs)",
  },
} as const;

/**
 * External link badge following the SourceTag pattern.
 * Renders an anchor with target="_blank" and proper security attributes.
 * Returns null when url is empty/null.
 */
export function ExternalLinkBadge({
  source,
  url,
  className = "",
  onClick,
}: ExternalLinkBadgeProps) {
  if (!url) return null;

  const config = SOURCE_CONFIG[source];

  return (
    <a
      href={url}
      target="_blank"
      rel="noopener noreferrer"
      className={`inline-flex items-center gap-1 text-xs underline underline-offset-2 decoration-current/40 hover:decoration-current transition-colors duration-150 ${className}`}
      style={{ color: config.color }}
      onClick={(e) => {
        e.stopPropagation();
        onClick?.();
      }}
    >
      <span
        className="h-1.5 w-1.5 rounded-full"
        style={{ backgroundColor: config.color }}
        aria-hidden="true"
      />
      {config.label}
    </a>
  );
}
