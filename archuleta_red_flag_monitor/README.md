# Archuleta Red Flag Risk Monitor

Forecast-screening monitor for possible Red Flag / fire-setting days in Archuleta County, Colorado.

Run from the workspace root:

```bash
.venv/bin/python archuleta_red_flag_monitor/monitor.py
```

Outputs are written beside the script:

- `latest.md`
- `latest.html`
- `latest.json`
- `history.csv`

The Markdown report now starts with an `At A Glance` section that groups `HIGH`, `CONCERN`, and `ELEVATED` dates plus the notification decision and signal status.
The HTML dashboard provides the same information in a one-page visual layout with colored tier chips and a 7-day risk strip.

All human-facing dates and times are rendered in Pagosa Springs, Colorado local time using the configured `America/Denver` timezone. The JSON report keeps an explicit `generated_at_utc` field for auditing, but `generated_at`, `generated_at_local`, displayed dates, and official alert start/end times use the local timezone.

`expected_update_interval_minutes` controls the displayed `Next update` estimate. Set it to match the automation or cron cadence that refreshes the monitor.

`COZ295` is the official National Weather Service fire-weather zone used for the Archuleta County screening area. The monitor counts active official Red Flag Warning and Fire Weather Watch alerts for that zone separately from its own forecast-based risk tier.

## Hosting options

The monitor output is static, so `latest.html`, `latest.json`, and `latest.md` can be served by almost any web host.

- Best private/local option: serve the files from the VOORMI Pi with Caddy or nginx, ideally behind Tailscale or a Cloudflare Tunnel.
- Best public option: publish the generated files to a static host such as Cloudflare Pages, Azure Static Web Apps, S3/CloudFront, or GitHub Pages.
- Avoid exposing the Pi directly to the open internet unless it is intentionally hardened, monitored, and kept patched.

## LPEA signal monitoring

The LPEA check monitors official public sources that could indicate power interruptions, including the outage map, homepage, outage center, PSPS information, red-flag outage guidance, fire-mitigation guidance, latest news, news releases, and official social profile URLs listed from LPEA's site.

Sources are split into two modes:

- `active`: current/update surfaces such as homepage, outage map, news pages, and social profiles. Keyword matches here can indicate something worth reviewing now.
- `reference`: standing informational pages such as PSPS or fire-mitigation explainers. Keyword matches here are retained as context but do not imply a current outage or shutoff plan by themselves.

Social pages often limit unauthenticated scraping, so their reachability is reported separately as source coverage rather than treated as authoritative silence.

## Optional email delivery

To email the report after every successful run, enable the `email` block in `config.json` and set SMTP credentials in environment variables:

```bash
export ARCHULETA_MONITOR_SMTP_USERNAME='your-smtp-username'
export ARCHULETA_MONITOR_SMTP_PASSWORD='your-smtp-password'
.venv/bin/python archuleta_red_flag_monitor/monitor.py
```

The script sends a plain-text email after writing `latest.md` and `latest.json`. It does this on every successful run when `email.enabled` is `true`.

This is not an official NWS warning product. It screens official NWS forecast-grid data and active `COZ295` alerts for early heads-up conditions.
