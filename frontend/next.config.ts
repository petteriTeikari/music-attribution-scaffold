import type { NextConfig } from "next";
import withBundleAnalyzer from "@next/bundle-analyzer";

const nextConfig: NextConfig = {
  // CopilotKit → streamdown → shiki is ESM-only; Webpack needs transpilation
  transpilePackages: ["streamdown", "shiki"],
  experimental: {
    reactCompiler: true,
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

const config = withBundleAnalyzer({
  enabled: process.env.ANALYZE === "true",
  openAnalyzer: false,
})(nextConfig);

export default config;
