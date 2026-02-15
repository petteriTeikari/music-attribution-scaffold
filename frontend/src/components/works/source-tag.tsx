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
  /**
   * When provided, renders as an `<a>` link opening in a new tab.
   * Do NOT use inside a parent `<a>` / `<Link>` — use `onNavigate` instead.
   */
  href?: string;
  /**
   * Programmatic navigation for use inside `<a>` / `<Link>` parents.
   * Renders as a clickable `<span>` (avoids nested `<a>` hydration error).
   * The URL is opened via window.open on click.
   */
  onNavigate?: string;
  onClick?: () => void;
}

export function SourceTag({ source, className = "", href, onNavigate, onClick }: SourceTagProps) {
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

  // Render as <a> — only safe when NOT inside another <a>/<Link>
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

  // Render as clickable <span> — safe inside <a>/<Link> parents
  if (onNavigate) {
    return (
      <span
        role="link"
        tabIndex={0}
        className={`inline-flex items-center gap-1 text-xs underline underline-offset-2 decoration-current/40 hover:decoration-current cursor-pointer ${className}`}
        style={{ color }}
        onClick={(e) => {
          e.stopPropagation();
          e.preventDefault();
          window.open(onNavigate, "_blank", "noopener,noreferrer");
          onClick?.();
        }}
        onKeyDown={(e) => {
          if (e.key === "Enter" || e.key === " ") {
            e.stopPropagation();
            e.preventDefault();
            window.open(onNavigate, "_blank", "noopener,noreferrer");
            onClick?.();
          }
        }}
      >
        {inner}
      </span>
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
