#!/usr/bin/env python3
"""PRD Context Assembly Tool.

Parses PRD frontmatter and assembles context for LLM consumption.
Implements progressive disclosure - only load what's needed.

Usage:
    python scripts/prd_context.py --domain attribution-engine
    python scripts/prd_context.py --file attribution-engine/confidence-scoring.md
    python scripts/prd_context.py --validate
"""

from __future__ import annotations

import argparse
import logging
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

import yaml

logger = logging.getLogger(__name__)

# Constants
PRD_DIR = Path(__file__).parent.parent / "docs" / "prd"
MAX_CONTEXT_TOKENS = 10000  # Target for progressive disclosure
APPROX_CHARS_PER_TOKEN = 4


@dataclass
class PRDMetadata:
    """Parsed PRD frontmatter."""

    id: str
    title: str
    status: str
    version: str
    requires: list[str] = field(default_factory=list)
    cross_refs: list[str] = field(default_factory=list)
    alternatives: list[str] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)
    priority: str = "medium"
    file_path: Path = field(default_factory=Path)
    content: str = ""

    @property
    def char_count(self) -> int:
        """Approximate character count."""
        return len(self.content)

    @property
    def estimated_tokens(self) -> int:
        """Approximate token count."""
        return self.char_count // APPROX_CHARS_PER_TOKEN


def parse_frontmatter(file_path: Path) -> PRDMetadata | None:
    """Parse YAML frontmatter from a PRD file."""
    try:
        content = file_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        logger.warning("File not found: %s", file_path)
        return None

    # Extract frontmatter
    match = re.match(r"^---\n(.*?)\n---\n(.*)$", content, re.DOTALL)
    if not match:
        logger.warning("No frontmatter found in: %s", file_path)
        return None

    frontmatter_text, body = match.groups()

    try:
        fm = yaml.safe_load(frontmatter_text)
    except yaml.YAMLError as e:
        logger.warning("Invalid YAML in %s: %s", file_path, e)
        return None

    return PRDMetadata(
        id=fm.get("id", ""),
        title=fm.get("title", ""),
        status=fm.get("status", "unknown"),
        version=fm.get("version", "0.0.0"),
        requires=fm.get("requires", []),
        cross_refs=fm.get("cross_refs", []),
        alternatives=fm.get("alternatives", []),
        tags=fm.get("tags", []),
        priority=fm.get("priority", "medium"),
        file_path=file_path,
        content=body,
    )


def resolve_path(ref: str, base_dir: Path) -> Path:
    """Resolve a reference to an absolute path."""
    # Handle section references (e.g., "file.md#section")
    ref = ref.split("#")[0]

    # Try relative to PRD dir
    path = base_dir / ref
    if path.exists():
        return path

    # Try without leading ../
    if ref.startswith("../"):
        path = base_dir / ref[3:]
        if path.exists():
            return path

    return base_dir / ref


def build_dependency_graph(prd_dir: Path) -> dict[str, PRDMetadata]:
    """Build graph of all PRDs and their dependencies."""
    graph: dict[str, PRDMetadata] = {}

    for md_file in prd_dir.rglob("*.md"):
        # Skip non-PRD files
        if md_file.name in ("README.md", "SYNTHESIS.md", "llm-context.md"):
            continue

        metadata = parse_frontmatter(md_file)
        if metadata and metadata.id:
            graph[metadata.id] = metadata

    return graph


def assemble_context(
    entry_point: str,
    graph: dict[str, PRDMetadata],
    max_tokens: int = MAX_CONTEXT_TOKENS,
) -> list[PRDMetadata]:
    """Assemble context starting from an entry point, following requires."""
    if entry_point not in graph:
        logger.error("Entry point not found: %s", entry_point)
        return []

    # BFS to collect required PRDs
    visited: set[str] = set()
    queue: list[str] = [entry_point]
    result: list[PRDMetadata] = []
    total_tokens = 0

    while queue:
        current_id = queue.pop(0)
        if current_id in visited:
            continue
        visited.add(current_id)

        if current_id not in graph:
            logger.warning("Missing dependency: %s", current_id)
            continue

        prd = graph[current_id]

        # Check token budget
        if total_tokens + prd.estimated_tokens > max_tokens:
            logger.info(
                "Token budget reached at %d tokens, stopping at: %s",
                total_tokens,
                current_id,
            )
            break

        result.append(prd)
        total_tokens += prd.estimated_tokens

        # Add required dependencies to queue
        for req in prd.requires:
            req_id = req.split("#")[0]  # Remove section ref
            # Convert path to id if needed
            if req_id.endswith(".md"):
                req_id = req_id.replace(".md", "").replace("/", "/")
            if req_id not in visited:
                queue.append(req_id)

    return result


def format_context(prds: list[PRDMetadata], format_type: str = "markdown") -> str:
    """Format assembled context for output."""
    if format_type == "markdown":
        output = ["# Assembled PRD Context\n"]
        output.append(f"**Total PRDs**: {len(prds)}\n")
        output.append(f"**Estimated Tokens**: {sum(p.estimated_tokens for p in prds)}\n")
        output.append("\n---\n")

        for prd in prds:
            output.append(f"\n## {prd.title}\n")
            output.append(f"*ID: {prd.id} | Status: {prd.status}*\n")
            output.append(prd.content)
            output.append("\n---\n")

        return "".join(output)

    if format_type == "summary":
        lines = ["Assembled PRDs:"]
        for prd in prds:
            lines.append(f"  - {prd.id}: {prd.title} (~{prd.estimated_tokens} tokens)")
        lines.append(f"\nTotal: ~{sum(p.estimated_tokens for p in prds)} tokens")
        return "\n".join(lines)

    return ""


def validate_all(prd_dir: Path) -> list[str]:
    """Validate all PRDs for schema compliance and broken references."""
    errors: list[str] = []
    graph = build_dependency_graph(prd_dir)

    for _prd_id, prd in graph.items():
        # Check required fields
        if not prd.id:
            errors.append(f"{prd.file_path}: Missing 'id' field")
        if not prd.title:
            errors.append(f"{prd.file_path}: Missing 'title' field")
        if not prd.status:
            errors.append(f"{prd.file_path}: Missing 'status' field")

        # Check references resolve
        for req in prd.requires:
            req_path = resolve_path(req, prd_dir)
            if not req_path.exists():
                errors.append(f"{prd.file_path}: Broken require: {req}")

        for ref in prd.cross_refs:
            ref_path = resolve_path(ref, prd_dir)
            if not ref_path.exists():
                errors.append(f"{prd.file_path}: Broken cross_ref: {ref}")

    return errors


def get_domain_entry_point(domain: str, graph: dict[str, PRDMetadata]) -> str | None:
    """Find the TOC entry point for a domain."""
    toc_id = f"{domain}/toc-{domain}"
    if toc_id in graph:
        return toc_id

    # Try finding any file in the domain
    for prd_id in graph:
        if prd_id.startswith(f"{domain}/"):
            return prd_id

    return None


def main() -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(description="PRD Context Assembly Tool")
    parser.add_argument(
        "--domain",
        help="Domain to assemble context for (e.g., 'attribution-engine')",
    )
    parser.add_argument(
        "--file",
        help="Specific PRD file to start from (e.g., 'attribution-engine/confidence-scoring.md')",
    )
    parser.add_argument(
        "--validate",
        action="store_true",
        help="Validate all PRDs for schema compliance",
    )
    parser.add_argument(
        "--format",
        choices=["markdown", "summary"],
        default="summary",
        help="Output format",
    )
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=MAX_CONTEXT_TOKENS,
        help="Maximum token budget",
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Verbose output",
    )

    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(levelname)s: %(message)s",
    )

    if args.validate:
        errors = validate_all(PRD_DIR)
        if errors:
            print("Validation errors found:")
            for error in errors:
                print(f"  - {error}")
            return 1
        print("All PRDs valid!")
        return 0

    graph = build_dependency_graph(PRD_DIR)
    print(f"Found {len(graph)} PRDs")

    entry_point = None

    if args.file:
        # Convert file path to ID
        entry_point = args.file.replace(".md", "")
    elif args.domain:
        entry_point = get_domain_entry_point(args.domain, graph)
        if not entry_point:
            print(f"Could not find entry point for domain: {args.domain}")
            return 1

    if entry_point:
        prds = assemble_context(entry_point, graph, args.max_tokens)
        output = format_context(prds, args.format)
        print(output)
    else:
        # List all domains
        domains = set()
        for prd_id in graph:
            parts = prd_id.split("/")
            if len(parts) > 1:
                domains.add(parts[0])

        print("Available domains:")
        for domain in sorted(domains):
            print(f"  - {domain}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
