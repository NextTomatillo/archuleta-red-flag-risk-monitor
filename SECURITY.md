# Security and Public Data Notes

This repository is public so GitHub Pages can serve the live dashboard.
Assume every tracked file and every generated Pages artifact is publicly downloadable.

## Safe To Publish

- Public-source weather, fire, LPEA, county, town, federal, and social-source links.
- Generated public dashboard files such as `index.html`, `latest.html`, `latest.md`, and `latest.json`.
- Forecast-history rows that contain only area-level weather and PSPS-screening data.
- Source code, tests, and placeholder configuration.

## Do Not Commit

- SMTP usernames, passwords, app passwords, API keys, GitHub tokens, or private keys.
- `.env` files, local override configs, launchd/cron files, or Codex automation state.
- Personal email addresses unless they are intentionally public.
- Exact home address, street-level coordinates, or private location notes.
- Manual PSPS-event notes that include private contacts, private property details, or non-public operational information.

## Credentials

Email credentials must stay in environment variables or GitHub Secrets if a GitHub Actions sender is added later.
The checked-in `config.json` should keep placeholder email values only.

## GitHub Settings

For this public repo, keep these enabled in GitHub when available:

- Secret scanning and push protection.
- Dependabot alerts and security updates.
- Read-only default GitHub Actions workflow permissions unless a workflow explicitly needs write access.
