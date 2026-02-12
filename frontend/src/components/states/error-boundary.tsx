"use client";

// TODO: Component not yet integrated — wire up during UI fine-tuning

import { Component, type ReactNode } from "react";

interface ErrorBoundaryProps {
  children: ReactNode;
  fallback?: ReactNode;
}

interface ErrorBoundaryState {
  hasError: boolean;
  error: Error | null;
}

export class ErrorBoundary extends Component<
  ErrorBoundaryProps,
  ErrorBoundaryState
> {
  constructor(props: ErrorBoundaryProps) {
    super(props);
    this.state = { hasError: false, error: null };
  }

  static getDerivedStateFromError(error: Error): ErrorBoundaryState {
    return { hasError: true, error };
  }

  render() {
    if (this.state.hasError) {
      if (this.props.fallback) {
        return this.props.fallback;
      }

      return (
        <div className="rounded-[var(--radius-lg)] border border-[var(--color-confidence-low)] bg-[var(--color-confidence-low-bg)] p-[var(--space-8)] text-center">
          <h2 className="text-lg font-semibold text-[var(--color-heading)]">
            Something went wrong
          </h2>
          <p className="mt-[var(--space-2)] text-sm text-[var(--color-body)]">
            {this.state.error?.message ?? "An unexpected error occurred."}
          </p>
          <button
            onClick={() => this.setState({ hasError: false, error: null })}
            className="mt-[var(--space-4)] rounded-[var(--radius-md)] border border-[var(--color-border)] px-[var(--space-4)] py-[var(--space-2)] text-sm font-medium text-[var(--color-primary)] hover:bg-[var(--color-surface-secondary)]"
          >
            Try again
          </button>
        </div>
      );
    }

    return this.props.children;
  }
}
