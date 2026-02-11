"use client";

import { CopilotKit } from "@copilotkit/react-core";

const API_URL = process.env.NEXT_PUBLIC_API_URL;

export function CopilotProvider({ children }: { children: React.ReactNode }) {
  if (!API_URL) {
    // Graceful degradation — no agent backend configured
    return <>{children}</>;
  }

  return (
    <CopilotKit runtimeUrl={`${API_URL}/api/v1/copilotkit`}>
      {children}
    </CopilotKit>
  );
}
