# Security Policy

## Supported Versions

Security updates should be applied to the latest code on the `main` branch.

## Reporting a Vulnerability

Do not commit secrets or vulnerability details directly into the repository.

If you find a vulnerability, report it privately to the repository owner or through GitHub Security Advisories when enabled.

## Local Development Rules

- Store real credentials only in `.env`.
- Rotate any secret that is accidentally committed.
- Keep `DEBUG=False` outside local development.
- Review dependency updates before deployment.
