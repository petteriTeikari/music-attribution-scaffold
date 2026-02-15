import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  experimental: {
    // Tree-shake barrel exports for heavy packages in Webpack mode.
    // Turbopack handles this automatically, but Webpack needs the hint.
    optimizePackageImports: [
      "jotai",
      "posthog-js",
      "@copilotkit/react-core",
      "@copilotkit/react-ui",
      "motion",
    ],
  },
};

export default nextConfig;
