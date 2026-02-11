import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  experimental: {
    // Deduplicate jotai across server/client boundaries in dev mode
    // See: https://github.com/pmndrs/jotai/discussions/2044
    optimizePackageImports: ["jotai"],
  },
};

export default nextConfig;
