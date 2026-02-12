/**
 * Single source of truth for frontend configuration.
 *
 * All environment variable reads should go through this module.
 * Components and services import from here instead of reading
 * process.env directly.
 */

export const API_URL = process.env.NEXT_PUBLIC_API_URL || "";
export const API_BASE = API_URL ? `${API_URL}/api/v1` : "";
export const COPILOT_RUNTIME_URL = API_URL
  ? `${API_URL}/api/v1/copilotkit`
  : null;
