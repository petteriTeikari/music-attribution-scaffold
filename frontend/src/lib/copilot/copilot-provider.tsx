"use client";

import dynamic from "next/dynamic";
import { COPILOT_RUNTIME_URL } from "@/lib/config";

const CopilotKitLazy = dynamic(
  () => import("@copilotkit/react-core").then((mod) => ({ default: mod.CopilotKit })),
  { ssr: false },
);

export function CopilotProvider({ children }: { children: React.ReactNode }) {
  if (!COPILOT_RUNTIME_URL) {
    // Graceful degradation — no agent backend configured
    return <>{children}</>;
  }

  return (
    <CopilotKitLazy runtimeUrl={COPILOT_RUNTIME_URL}>
      {children}
    </CopilotKitLazy>
  );
}
