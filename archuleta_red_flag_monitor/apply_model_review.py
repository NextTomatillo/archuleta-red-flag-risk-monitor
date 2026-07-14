#!/usr/bin/env python3
"""Validate a model interpretation and merge it into the current public report."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import monitor


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--config",
        default=str(Path(__file__).with_name("config.json")),
        help="Path to monitor config.json",
    )
    parser.add_argument(
        "--review",
        default=None,
        help="Path to review JSON; defaults to output.public_model_review_json",
    )
    return parser.parse_args()


def load_json(path: Path) -> dict:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"Required file not found: {path.name}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON in {path.name}: {exc}") from exc
    if not isinstance(payload, dict):
        raise ValueError(f"{path.name} must contain a JSON object.")
    return payload


def main() -> int:
    args = parse_args()
    config_path = Path(args.config).resolve()
    config = monitor.load_config(config_path)
    latest_path = monitor.output_path(config_path, config, "latest_json", "latest.json")
    request_path = monitor.model_review_request_path(config_path, config)
    review_path = Path(args.review).resolve() if args.review else monitor.public_model_review_path(config_path, config)

    try:
        report = load_json(latest_path)
        request = load_json(request_path)
        review = load_json(review_path)
        validated = monitor.validate_model_review(review, request)
    except ValueError as exc:
        print(f"Model review rejected: {exc}")
        return 2

    report["model_review"] = validated
    report["public_analysis_export"] = monitor.build_public_analysis_export(report)
    monitor.write_rendered_outputs(report, config_path, config)
    review_path.write_text(json.dumps(validated, indent=2, sort_keys=True), encoding="utf-8")
    print(
        "Model review applied to report "
        f"{validated['report_generated_at']} using evidence: {', '.join(validated['evidence_ids'])}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
