-- Initialize PostgreSQL extensions for Music Attribution Scaffold
-- This script runs on first container initialization.

-- pgvector: Vector similarity search for embeddings
CREATE EXTENSION IF NOT EXISTS vector;

-- UUID generation (for UUIDv7 when PG18 is available)
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Apache AGE: Graph database extension
-- Note: AGE requires a custom PostgreSQL build. When using the standard
-- pgvector image, this will fail gracefully. Use the custom Dockerfile
-- with AGE pre-installed for full graph support.
-- CREATE EXTENSION IF NOT EXISTS age;
-- SET search_path = ag_catalog, "$user", public;

-- Verify extensions loaded
SELECT extname, extversion FROM pg_extension ORDER BY extname;
