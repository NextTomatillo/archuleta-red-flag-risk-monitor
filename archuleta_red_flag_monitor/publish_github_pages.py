#!/usr/bin/env python3
import argparse
import datetime as dt
import json
import shutil
import subprocess
import sys
from pathlib import Path
from zoneinfo import ZoneInfo


PACKAGE_FILES = [
    "README.md",
    "config.json",
    "codex_review_packet.json",
    "forecast_history.csv",
    "latest.html",
    "latest.json",
    "latest.md",
    "monitor.py",
    "publish_github_pages.py",
    "psps_events.json",
    "tests/test_monitor.py",
]


def run(cmd: list[str], cwd: Path, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, cwd=cwd, check=check, text=True, capture_output=True)


def load_generated_label(source_dir: Path) -> str:
    latest_json = source_dir / "latest.json"
    try:
        data = json.loads(latest_json.read_text(encoding="utf-8"))
        generated_at = data.get("generated_at_local") or data.get("generated_at")
        timezone_name = data.get("timezone") or "America/Denver"
        if generated_at:
            parsed = dt.datetime.fromisoformat(generated_at)
            if parsed.tzinfo is None:
                parsed = parsed.replace(tzinfo=ZoneInfo(timezone_name))
            parsed = parsed.astimezone(ZoneInfo(timezone_name))
            return parsed.strftime("%Y-%m-%d %H:%M %Z")
    except Exception:
        pass
    return dt.datetime.now(ZoneInfo("America/Denver")).strftime("%Y-%m-%d %H:%M %Z")


def copy_outputs(source_dir: Path, pages_repo: Path) -> None:
    package_target = pages_repo / "archuleta_red_flag_monitor"
    package_target.mkdir(parents=True, exist_ok=True)
    (package_target / "tests").mkdir(parents=True, exist_ok=True)

    for relative in PACKAGE_FILES:
        source = source_dir / relative
        if not source.exists():
            raise FileNotFoundError(f"Missing source file: {source}")
        target = package_target / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)

    shutil.copy2(source_dir / "latest.html", pages_repo / "index.html")


def publish(source_dir: Path, pages_repo: Path, no_push: bool = False) -> str:
    if not (pages_repo / ".git").exists():
        raise RuntimeError(f"Pages repo is not a Git repository: {pages_repo}")

    copy_outputs(source_dir, pages_repo)

    tracked_paths = [
        "index.html",
        *[f"archuleta_red_flag_monitor/{relative}" for relative in PACKAGE_FILES],
    ]
    run(["git", "add", *tracked_paths], pages_repo)

    diff_result = run(["git", "diff", "--cached", "--quiet"], pages_repo, check=False)
    if diff_result.returncode == 0:
        return "no changes to publish"

    label = load_generated_label(source_dir)
    run(["git", "commit", "-m", f"Publish monitor update {label}"], pages_repo)
    if no_push:
        return "committed locally; push skipped"

    run(["git", "push", "origin", "main"], pages_repo)
    return f"published monitor update {label}"


def parse_args() -> argparse.Namespace:
    here = Path(__file__).resolve().parent
    default_pages_repo = here.parent / "archuleta-red-flag-risk-monitor"
    parser = argparse.ArgumentParser(description="Publish the latest monitor dashboard to GitHub Pages.")
    parser.add_argument("--source-dir", default=str(here), help="Directory containing latest.html/latest.json.")
    parser.add_argument("--pages-repo", default=str(default_pages_repo), help="Local GitHub Pages clone.")
    parser.add_argument("--no-push", action="store_true", help="Commit locally but do not push.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source_dir = Path(args.source_dir).resolve()
    pages_repo = Path(args.pages_repo).resolve()
    try:
        result = publish(source_dir, pages_repo, no_push=args.no_push)
    except Exception as exc:
        print(f"Publish failed: {exc}", file=sys.stderr)
        return 1

    print(f"Publish: {result}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
