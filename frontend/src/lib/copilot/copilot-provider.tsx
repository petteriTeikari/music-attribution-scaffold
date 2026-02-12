"use client";

import { CopilotKit } from "@copilotkit/react-core";
import { COPILOT_RUNTIME_URL } from "@/lib/config";

export function CopilotProvider({ children }: { children: React.ReactNode }) {
  if (!COPILOT_RUNTIME_URL) {
    // Graceful degradation — no agent backend configured
    return <>{children}</>;
  }

  return (
    <CopilotKit runtimeUrl={COPILOT_RUNTIME_URL}>
      {children}
    </CopilotKit>
  );
}
