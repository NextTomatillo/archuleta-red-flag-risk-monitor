# Archuleta Red Flag Risk Monitor

Public-source fire-weather and PSPS risk monitor for the LPEA / Archuleta County area.

This repository includes:

- `index.html`: static GitHub Pages dashboard snapshot.
- `archuleta_red_flag_monitor/monitor.py`: monitor script.
- `archuleta_red_flag_monitor/latest.html`: generated dashboard output.
- `archuleta_red_flag_monitor/latest.json`: generated structured report.
- `archuleta_red_flag_monitor/latest.md`: generated text report.

Important: this is an unofficial monitor. It is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice.

Security note: this repo is public for GitHub Pages. See [SECURITY.md](SECURITY.md) for what is safe to publish and what must stay out of the repo.

## Run Locally

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python archuleta_red_flag_monitor/monitor.py
```

After a run, copy the dashboard snapshot to the Pages entry point:

```bash
cp archuleta_red_flag_monitor/latest.html index.html
```

## GitHub Pages

Enable Pages from `Settings -> Pages -> Deploy from a branch`, using branch `main` and folder `/root`.
