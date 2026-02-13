# Security Policy

## Scope

This project is an **open-source research scaffold** — companion code to [SSRN No. 6109087](https://doi.org/10.2139/ssrn.6109087). It is designed for research and demonstration purposes, not for production deployment with real user data.

## Supported Versions

| Version | Supported |
|---------|-----------|
| 0.x.y (current) | Yes |

## Reporting a Vulnerability

If you discover a security vulnerability, please report it responsibly:

1. **Do not** open a public GitHub issue.
2. **Email**: Send details to the repository maintainer via the email listed in the [CITATION.cff](CITATION.cff).
3. **Include**: Description of the vulnerability, steps to reproduce, and potential impact.
4. **Response time**: We aim to acknowledge reports within 7 days.

## Security Measures

This project uses the following security tooling:

- **detect-secrets**: Baseline scanning for accidentally committed secrets (`.secrets.baseline`)
- **pre-commit hooks**: Automated checks on every commit (private key detection, YAML validation)
- **compliance checks**: `scripts/security/compliance_check.py` validates secrets hygiene and gitignore coverage
- **CI integration**: Security checks run automatically in GitHub Actions

## Known Limitations

As a research scaffold, this project:

- Uses **mock/seed data** (not real artist data) for demonstration
- Does not implement production-grade authentication or authorization
- Uses in-memory implementations for some services in dev/test mode
- Is not designed for deployment at scale without significant hardening

## Dependencies

All dependencies are managed through `pyproject.toml` with `uv.lock` for reproducibility. The project aims for MIT/Apache/BSD-compatible dependencies only.
