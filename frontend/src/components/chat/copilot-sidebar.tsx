"use client";

import { CopilotSidebar as CKSidebar } from "@copilotkit/react-ui";
import "@copilotkit/react-ui/styles.css";

interface AgentSidebarProps {
  open: boolean;
  onOpenChange: (open: boolean) => void;
}

export function AgentSidebar({ open, onOpenChange }: AgentSidebarProps) {
  if (!open) return null;

  return (
    <div className="agent-sidebar-wrapper">
      <CKSidebar
        defaultOpen={true}
        onSetOpen={onOpenChange}
        labels={{
          title: "Attribution Agent",
          placeholder: "Ask about confidence scores, credits, or attributions...",
        }}
        icons={{
          headerCloseIcon: (
            <span className="text-[var(--color-muted)] hover:text-[var(--color-heading)] transition-colors">
              &times;
            </span>
          ),
        }}
      />
    </div>
  );
}
