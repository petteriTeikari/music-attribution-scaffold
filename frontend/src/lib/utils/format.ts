/**
 * Shared formatting utilities — single source of truth for display formatting.
 *
 * Eliminates duplication of formatRole, formatPermissionType, and
 * formatTimestamp across 8+ component files.
 */

/** Convert SNAKE_CASE to Title Case (e.g. "VOICE_CLONING" → "Voice Cloning"). */
export function formatSnakeCase(value: string): string {
  return value
    .split("_")
    .map((w) => w.charAt(0).toUpperCase() + w.slice(1).toLowerCase())
    .join(" ");
}

/** Format an ISO timestamp as a short date (e.g. "Feb 22, 2026"). */
export function formatDate(iso: string): string {
  return new Date(iso).toLocaleDateString("en-US", {
    month: "short",
    day: "numeric",
    year: "numeric",
  });
}

/** Format an ISO timestamp as short date + time (e.g. "Feb 22, 02:30 PM"). */
export function formatDateTime(iso: string): string {
  return new Date(iso).toLocaleDateString("en-US", {
    month: "short",
    day: "numeric",
    hour: "2-digit",
    minute: "2-digit",
  });
}
