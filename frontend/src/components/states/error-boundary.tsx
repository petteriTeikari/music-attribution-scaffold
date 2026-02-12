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
        <div className="rounded-lg border border-confidence-low bg-confidence-low-bg p-8 text-center">
          <h2 className="text-lg font-semibold text-heading">
            Something went wrong
          </h2>
          <p className="mt-2 text-sm text-body">
            {this.state.error?.message ?? "An unexpected error occurred."}
          </p>
          <button
            onClick={() => this.setState({ hasError: false, error: null })}
            className="mt-4 rounded-md border border-border px-4 py-2 text-sm font-medium text-primary hover:bg-surface-secondary"
          >
            Try again
          </button>
        </div>
      );
    }

    return this.props.children;
  }
}
