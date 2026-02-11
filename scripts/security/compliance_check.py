#!/usr/bin/env python3
"""Music Attribution Scaffold - Security Compliance Check.

Standalone script (stdlib only) that validates secrets hygiene,
gitignore coverage, and quality gate infrastructure.
Designed for CI via GitHub Actions.

Usage:
    uv run python scripts/security/compliance_check.py --validate
    uv run python scripts/security/compliance_check.py --validate --output report.json
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import UTC, datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

# Common secret patterns
SECRET_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("AWS Access Key", re.compile(r"AKIA[0-9A-Z]{16}")),
    (
        "Generic API Key",
        re.compile(
            r"""(?:api[_-]?key|apikey)\s*[:=]\s*['"][A-Za-z0-9_\-]{20,}['"]""",
            re.IGNORECASE,
        ),
    ),
    (
        "Generic Secret",
        re.compile(
            r"""(?:secret|password|passwd|pwd)\s*[:=]\s*['"][^'"]{8,}['"]""",
            re.IGNORECASE,
        ),
    ),
    (
        "Private Key Header",
        re.compile(r"-----BEGIN (?:RSA |EC |DSA )?PRIVATE KEY-----"),
    ),
    ("GitHub Token", re.compile(r"gh[pousr]_[A-Za-z0-9_]{36,}")),
    (
        "Discogs Token",
        re.compile(
            r"""(?:discogs[_-]?token)\s*[:=]\s*['"][A-Za-z0-9]{20,}['"]""",
            re.IGNORECASE,
        ),
    ),
    (
        "AcoustID API Key",
        re.compile(
            r"""(?:acoustid[_-]?(?:api[_-]?)?key)\s*[:=]\s*['"][A-Za-z0-9]{8,}['"]""",
            re.IGNORECASE,
        ),
    ),
]

# File extensions to scan
SCAN_EXTENSIONS = {
    ".py",
    ".yaml",
    ".yml",
    ".md",
    ".json",
    ".toml",
    ".cfg",
    ".ini",
    ".sh",
}

# Gitignore patterns that must be present for security
REQUIRED_GITIGNORE_PATTERNS = [
    ".env",
    ".venv/",
    ".coverage",
    "htmlcov/",
    "*.log",
]


def get_tracked_files() -> list[Path]:
    """Get list of git-tracked files."""
    result = subprocess.run(
        ["git", "ls-files"],
        capture_output=True,
        text=True,
        cwd=PROJECT_ROOT,
    )
    if result.returncode != 0:
        return []
    return [PROJECT_ROOT / f for f in result.stdout.strip().splitlines() if f]


def check_secrets(tracked_files: list[Path]) -> dict:
    """Scan tracked files for common secret patterns."""
    findings: list[dict] = []
    files_scanned = 0

    for fpath in tracked_files:
        if fpath.suffix not in SCAN_EXTENSIONS:
            continue
        rel = fpath.relative_to(PROJECT_ROOT)
        # Skip this script itself
        if str(rel).startswith("scripts/security/"):
            continue

        files_scanned += 1
        try:
            content = fpath.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue

        for name, pattern in SECRET_PATTERNS:
            for match in pattern.finditer(content):
                line_num = content[: match.start()].count("\n") + 1
                findings.append(
                    {
                        "file": str(rel),
                        "line": line_num,
                        "pattern_name": name,
                        "severity": "CRITICAL",
                        "message": f"Potential {name} detected",
                    }
                )

    return {
        "check": "secrets_scan",
        "description": "Check for API keys, tokens, and passwords in tracked files",
        "framework": "Security Hygiene",
        "passed": len(findings) == 0,
        "files_scanned": files_scanned,
        "findings": findings,
    }


def check_env_files_not_tracked() -> dict:
    """Verify .env files are not tracked by git."""
    findings: list[dict] = []

    result = subprocess.run(
        ["git", "ls-files"],
        capture_output=True,
        text=True,
        cwd=PROJECT_ROOT,
    )
    tracked = result.stdout.strip().splitlines() if result.returncode == 0 else []

    for f in tracked:
        fname = Path(f).name
        # .env.example and .env.*.example are safe templates — skip them
        if fname.endswith(".example"):
            continue
        if fname.startswith(".env") or fname.endswith(".env"):
            findings.append(
                {
                    "file": f,
                    "severity": "CRITICAL",
                    "message": "Environment file is tracked by git",
                }
            )

    return {
        "check": "env_file_isolation",
        "description": "Verify .env files are not tracked by git",
        "framework": "Security Hygiene",
        "passed": len(findings) == 0,
        "findings": findings,
    }


def check_gitignore_coverage() -> dict:
    """Confirm critical security patterns exist in .gitignore."""
    findings: list[dict] = []
    gitignore_path = PROJECT_ROOT / ".gitignore"

    if not gitignore_path.exists():
        findings.append(
            {
                "severity": "CRITICAL",
                "message": ".gitignore file not found",
            }
        )
        return {
            "check": "gitignore_coverage",
            "description": "Verify critical security patterns in .gitignore",
            "framework": "Defense in Depth",
            "passed": False,
            "findings": findings,
        }

    content = gitignore_path.read_text(encoding="utf-8")

    for pattern in REQUIRED_GITIGNORE_PATTERNS:
        if pattern not in content:
            findings.append(
                {
                    "pattern": pattern,
                    "severity": "HIGH",
                    "message": f"Required gitignore pattern '{pattern}' not found",
                }
            )

    return {
        "check": "gitignore_coverage",
        "description": "Verify critical security patterns in .gitignore",
        "framework": "Defense in Depth",
        "passed": len(findings) == 0,
        "findings": findings,
    }


def check_license_present() -> dict:
    """Verify LICENSE file exists for open-source compliance."""
    findings: list[dict] = []
    license_path = PROJECT_ROOT / "LICENSE"

    if not license_path.exists():
        findings.append(
            {
                "severity": "HIGH",
                "message": "LICENSE file not found — required for open-source compliance",
            }
        )

    return {
        "check": "license_present",
        "description": "Verify LICENSE file exists for open-source compliance",
        "framework": "License Compliance",
        "passed": len(findings) == 0,
        "findings": findings,
    }


def run_all_checks() -> dict:
    """Run all compliance checks and return structured report."""
    tracked_files = get_tracked_files()

    checks = [
        check_secrets(tracked_files),
        check_env_files_not_tracked(),
        check_gitignore_coverage(),
        check_license_present(),
    ]

    total_findings = sum(len(c["findings"]) for c in checks)
    critical_findings = sum(1 for c in checks for f in c["findings"] if f.get("severity") == "CRITICAL")
    passed_checks = sum(1 for c in checks if c["passed"])
    total_checks = len(checks)
    compliance_pct = (passed_checks / total_checks) * 100 if total_checks > 0 else 0

    return {
        "timestamp": datetime.now(UTC).isoformat(),
        "overall_compliance": compliance_pct,
        "critical_findings": critical_findings,
        "total_findings": total_findings,
        "checks_passed": passed_checks,
        "checks_total": total_checks,
        "validation_details": {c["check"]: c for c in checks},
    }


def main() -> int:
    """Run compliance checks and output report."""
    parser = argparse.ArgumentParser(description="Music Attribution Scaffold Compliance Check")
    parser.add_argument("--validate", action="store_true", help="Run all compliance checks")
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Write JSON report to file (default: stdout)",
    )
    args = parser.parse_args()

    if not args.validate:
        parser.print_help()
        return 0

    report = run_all_checks()
    report_json = json.dumps(report, indent=2)

    if args.output:
        args.output.write_text(report_json, encoding="utf-8")
        print(f"Report written to {args.output}", file=sys.stderr)
    else:
        print(report_json)

    print(
        f"\nCompliance: {report['overall_compliance']:.0f}% "
        f"({report['checks_passed']}/{report['checks_total']} checks passed, "
        f"{report['critical_findings']} critical findings)",
        file=sys.stderr,
    )

    return 1 if report["critical_findings"] > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
