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
}

export function SourceTag({ source, className = "" }: SourceTagProps) {
  const color = getSourceCssVar(source);
  const label = SOURCE_LABELS[source] ?? source;

  return (
    <span
      className={`inline-flex items-center gap-[var(--space-1)] text-xs ${className}`}
      style={{ color }}
    >
      <span
        className="h-1.5 w-1.5"
        style={{ backgroundColor: color }}
        aria-hidden="true"
      />
      {label}
    </span>
  );
}
