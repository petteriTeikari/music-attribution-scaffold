import { getSourceCssVar } from "@/lib/theme/confidence";
import type { Source } from "@/lib/types/enums";

const SOURCE_LABELS: Record<string, string> = {
  MUSICBRAINZ: "MusicBrainz",
  DISCOGS: "Discogs",
  ACOUSTID: "AcoustID",
  ARTIST_INPUT: "Artist",
  FILE_METADATA: "File",
};

interface SourceTagProps {
  source: Source;
  className?: string;
  /** When provided, renders as a clickable link opening in a new tab. */
  href?: string;
  onClick?: () => void;
}

export function SourceTag({ source, className = "", href, onClick }: SourceTagProps) {
  const color = getSourceCssVar(source);
  const label = SOURCE_LABELS[source] ?? source;

  const inner = (
    <>
      <span
        className="h-1.5 w-1.5"
        style={{ backgroundColor: color }}
        aria-hidden="true"
      />
      {label}
    </>
  );

  if (href) {
    return (
      <a
        href={href}
        target="_blank"
        rel="noopener noreferrer"
        className={`inline-flex items-center gap-1 text-xs underline underline-offset-2 decoration-current/40 hover:decoration-current ${className}`}
        style={{ color }}
        onClick={(e) => {
          e.stopPropagation();
          onClick?.();
        }}
      >
        {inner}
      </a>
    );
  }

  return (
    <span
      className={`inline-flex items-center gap-1 text-xs ${className}`}
      style={{ color }}
    >
      {inner}
    </span>
  );
}
