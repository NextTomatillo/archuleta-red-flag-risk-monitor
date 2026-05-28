#!/usr/bin/env python3
import argparse
import csv
import datetime as dt
import html
import json
import os
import re
import smtplib
from collections import defaultdict
from email.message import EmailMessage
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

import requests

TIER_RANK = {
    "GREEN": 0,
    "ELEVATED": 1,
    "CONCERN": 2,
    "HIGH": 3,
}

PSPS_RANK = {
    "LOW": 0,
    "ELEVATED": 1,
    "WATCH": 2,
    "LIKELY": 3,
    "CONFIRMED": 4,
}

FIRE_RESTRICTION_RANK = {
    "NONE": 0,
    "UNKNOWN": 0,
    "RESTRICTIONS": 1,
    "STAGE 1": 2,
    "STAGE 2": 3,
    "STAGE 3": 4,
}

FIRE_DANGER_RANK = {
    "UNKNOWN": 0,
    "LOW": 1,
    "MODERATE": 2,
    "HIGH": 3,
    "VERY HIGH": 4,
    "EXTREME": 5,
}

NWS_API_BASE = "https://api.weather.gov"
LPEA_DEFAULT_OUTAGE_URL = "https://lpea.coop/outage-center"
LPEA_DEFAULT_PSPS_URL = "https://lpea.coop/psps"
LPEA_DEFAULT_OUTAGE_MAP_URL = "https://outage.lpea.coop"
UNOFFICIAL_MONITOR_LABEL = "Unofficial monitor"
UNOFFICIAL_MONITOR_DISCLAIMER = (
    "This is not an official forecast, National Weather Service warning, "
    "LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and "
    "safety decisions with NWS and LPEA."
)


def parse_args() -> argparse.Namespace:
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description="Monitor Archuleta County Red Flag risk.")
    parser.add_argument("--config", default=str(here / "config.json"))
    parser.add_argument("--no-write", action="store_true", help="Fetch and print but do not write outputs.")
    parser.add_argument("--json", action="store_true", help="Print the full JSON report.")
    return parser.parse_args()


def load_config(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def request_json(session: requests.Session, url: str, timeout: int = 60) -> Dict[str, Any]:
    resp = session.get(url, timeout=timeout)
    resp.raise_for_status()
    return resp.json()


def parse_datetime(value: Optional[str]) -> Optional[dt.datetime]:
    if not value:
        return None
    normalized = value.replace("Z", "+00:00")
    parsed = dt.datetime.fromisoformat(normalized)
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=dt.timezone.utc)
    return parsed.astimezone(dt.timezone.utc)


def datetime_to_local_iso(value: Optional[dt.datetime], tz: ZoneInfo) -> Optional[str]:
    if value is None:
        return None
    return value.astimezone(tz).isoformat()


def parse_duration(value: str) -> dt.timedelta:
    match = re.fullmatch(
        r"P(?:(?P<days>\d+(?:\.\d+)?)D)?(?:T(?:(?P<hours>\d+(?:\.\d+)?)H)?(?:(?P<minutes>\d+(?:\.\d+)?)M)?(?:(?P<seconds>\d+(?:\.\d+)?)S)?)?",
        value,
    )
    if not match:
        raise ValueError(f"Unsupported ISO 8601 duration: {value}")
    parts = {key: float(match.group(key) or 0) for key in ("days", "hours", "minutes", "seconds")}
    return dt.timedelta(**parts)


def parse_valid_time(value: str) -> Tuple[dt.datetime, dt.datetime]:
    start_text, end_text = value.split("/", 1)
    start = parse_datetime(start_text)
    if start is None:
        raise ValueError(f"Missing interval start in {value}")
    if end_text.startswith("P"):
        end = start + parse_duration(end_text)
    else:
        end = parse_datetime(end_text)
        if end is None:
            raise ValueError(f"Missing interval end in {value}")
    return start, end


def floor_hour(value: dt.datetime) -> dt.datetime:
    return value.replace(minute=0, second=0, microsecond=0)


def iter_utc_hours(start: dt.datetime, end: dt.datetime) -> Iterable[dt.datetime]:
    hour = floor_hour(start.astimezone(dt.timezone.utc))
    end_utc = end.astimezone(dt.timezone.utc)
    while hour < end_utc:
        yield hour
        hour += dt.timedelta(hours=1)


def speed_to_mph(value: Optional[float], uom: Optional[str]) -> Optional[float]:
    if value is None:
        return None
    text = (uom or "").lower()
    if "km_h" in text or "km/h" in text or "kilomet" in text:
        return float(value) * 0.621371
    if "m_s" in text or "m/s" in text or "metre" in text or "meter" in text:
        return float(value) * 2.23694
    if "kn" in text or "knot" in text:
        return float(value) * 1.15078
    return float(value)


def value_to_float(value: Any) -> Optional[float]:
    if value is None:
        return None
    if isinstance(value, (int, float)):
        return float(value)
    try:
        return float(str(value))
    except ValueError:
        return None


def expand_grid_field(field: Optional[Dict[str, Any]], horizon_start: dt.datetime, horizon_end: dt.datetime) -> Dict[dt.datetime, Any]:
    if not field:
        return {}
    by_hour: Dict[dt.datetime, Any] = {}
    for item in field.get("values", []):
        try:
            start, end = parse_valid_time(item["validTime"])
        except (KeyError, ValueError):
            continue
        if end <= horizon_start or start >= horizon_end:
            continue
        clipped_start = max(start, horizon_start)
        clipped_end = min(end, horizon_end)
        for hour in iter_utc_hours(clipped_start, clipped_end):
            by_hour[hour] = item.get("value")
    return by_hour


def has_hours_in_window(hours: Iterable[dt.datetime], min_hours: int, window_hours: int) -> bool:
    ordered = sorted(set(hours))
    for index, start in enumerate(ordered):
        window_end = start + dt.timedelta(hours=window_hours)
        count = sum(1 for hour in ordered[index:] if start <= hour < window_end)
        if count >= min_hours:
            return True
    return False


def max_tier(*tiers: str) -> str:
    return max(tiers, key=lambda tier: TIER_RANK.get(tier, -1))


def max_psps_level(*levels: str) -> str:
    return max(levels, key=lambda level: PSPS_RANK.get(level, -1))


def output_path(config_path: Path, config: Dict[str, Any], key: str, default_name: str) -> Path:
    return config_path.resolve().parent / config.get("output", {}).get(key, default_name)


def event_log_path(config_path: Path, config: Dict[str, Any]) -> Path:
    return output_path(config_path, config, "psps_event_log", "psps_events.json")


def forecast_history_path(config_path: Path, config: Dict[str, Any]) -> Path:
    return output_path(config_path, config, "forecast_history_csv", "forecast_history.csv")


def safe_int(value: Any, default: int = 0) -> int:
    try:
        return int(float(value))
    except (TypeError, ValueError):
        return default


def safe_float(value: Any) -> Optional[float]:
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def hour_label(value: Optional[dt.datetime]) -> str:
    if value is None:
        return "n/a"
    hour = value.hour % 12 or 12
    suffix = "AM" if value.hour < 12 else "PM"
    return f"{hour} {suffix}"


def local_hour_value(record: Dict[str, Any]) -> Optional[dt.datetime]:
    value = record.get("local_hour") or record.get("utc_hour")
    return value if isinstance(value, dt.datetime) else None


def risk_window_summary(records: List[Dict[str, Any]], thresholds: Dict[str, Any]) -> str:
    if not records:
        return "No forecast hours available."
    threshold_hours = [
        record
        for record in records
        if record.get("relative_humidity") is not None
        and record.get("usable_wind_mph") is not None
        and record["relative_humidity"] <= thresholds["near_rh_percent"]
        and record["usable_wind_mph"] >= thresholds["near_wind_mph"]
    ]
    if threshold_hours:
        ordered = sorted(threshold_hours, key=lambda item: item["utc_hour"])
        start = local_hour_value(ordered[0])
        end = local_hour_value(ordered[-1])
        return f"{hour_label(start)}-{hour_label(end)} local; {len(ordered)} near/red-flag threshold hour{'s' if len(ordered) != 1 else ''}."

    ranked = sorted(
        records,
        key=lambda item: (
            item.get("usable_wind_mph") is not None,
            item.get("usable_wind_mph") or -1,
            -(item.get("relative_humidity") or 1000),
        ),
        reverse=True,
    )
    peak = ranked[0]
    peak_hour = hour_label(local_hour_value(peak))
    return (
        f"Peak ingredients near {peak_hour} local; "
        f"RH {format_metric(peak.get('relative_humidity'), '%')}, wind {format_metric(peak.get('usable_wind_mph'), ' mph')}."
    )


def build_hourly_records(
    grid_properties: Dict[str, Any],
    now_utc: dt.datetime,
    horizon_end_utc: dt.datetime,
    tz: ZoneInfo,
) -> List[Dict[str, Any]]:
    fields = {
        "relative_humidity": expand_grid_field(grid_properties.get("relativeHumidity"), now_utc, horizon_end_utc),
        "wind_speed": expand_grid_field(grid_properties.get("windSpeed"), now_utc, horizon_end_utc),
        "wind_gust": expand_grid_field(grid_properties.get("windGust"), now_utc, horizon_end_utc),
        "probability_of_thunder": expand_grid_field(grid_properties.get("probabilityOfThunder"), now_utc, horizon_end_utc),
        "probability_of_precip": expand_grid_field(grid_properties.get("probabilityOfPrecipitation"), now_utc, horizon_end_utc),
        "red_flag_threat_index": expand_grid_field(grid_properties.get("redFlagThreatIndex"), now_utc, horizon_end_utc),
    }
    speed_uom = (grid_properties.get("windSpeed") or {}).get("uom")
    gust_uom = (grid_properties.get("windGust") or {}).get("uom")

    records: List[Dict[str, Any]] = []
    for hour in iter_utc_hours(now_utc, horizon_end_utc):
        local_hour = hour.astimezone(tz)
        wind_speed_mph = speed_to_mph(value_to_float(fields["wind_speed"].get(hour)), speed_uom)
        wind_gust_mph = speed_to_mph(value_to_float(fields["wind_gust"].get(hour)), gust_uom)
        usable_wind = max([value for value in (wind_speed_mph, wind_gust_mph) if value is not None], default=None)
        records.append(
            {
                "utc_hour": hour,
                "local_hour": local_hour,
                "date": local_hour.date().isoformat(),
                "relative_humidity": value_to_float(fields["relative_humidity"].get(hour)),
                "wind_speed_mph": wind_speed_mph,
                "wind_gust_mph": wind_gust_mph,
                "usable_wind_mph": usable_wind,
                "probability_of_thunder": value_to_float(fields["probability_of_thunder"].get(hour)),
                "probability_of_precip": value_to_float(fields["probability_of_precip"].get(hour)),
                "red_flag_threat_index": fields["red_flag_threat_index"].get(hour),
            }
        )
    return records


def min_present(values: Iterable[Optional[float]]) -> Optional[float]:
    present = [value for value in values if value is not None]
    return min(present) if present else None


def max_present(values: Iterable[Optional[float]]) -> Optional[float]:
    present = [value for value in values if value is not None]
    return max(present) if present else None


def score_day(records: List[Dict[str, Any]], thresholds: Dict[str, Any]) -> Dict[str, Any]:
    if not records:
        return {
            "tier": "GREEN",
            "min_rh_percent": None,
            "max_wind_mph": None,
            "max_gust_mph": None,
            "max_usable_wind_mph": None,
            "max_thunder_percent": None,
            "max_precip_percent": None,
            "red_flag_hours": 0,
            "near_hours": 0,
            "highest_risk_window": "No forecast hours available.",
            "reasons": ["No forecast hours available for this day."],
        }

    min_rh = min_present(record["relative_humidity"] for record in records)
    max_wind = max_present(record["wind_speed_mph"] for record in records)
    max_gust = max_present(record["wind_gust_mph"] for record in records)
    max_usable_wind = max_present(record["usable_wind_mph"] for record in records)
    max_thunder = max_present(record["probability_of_thunder"] for record in records)
    max_precip = max_present(record["probability_of_precip"] for record in records)

    critical_hours = [
        record["utc_hour"]
        for record in records
        if record["relative_humidity"] is not None
        and record["usable_wind_mph"] is not None
        and record["relative_humidity"] <= thresholds["red_flag_rh_percent"]
        and record["usable_wind_mph"] >= thresholds["red_flag_wind_mph"]
    ]
    near_hours = [
        record["utc_hour"]
        for record in records
        if record["relative_humidity"] is not None
        and record["usable_wind_mph"] is not None
        and record["relative_humidity"] <= thresholds["near_rh_percent"]
        and record["usable_wind_mph"] >= thresholds["near_wind_mph"]
    ]

    tier = "GREEN"
    reasons: List[str] = []

    if has_hours_in_window(critical_hours, thresholds["red_flag_min_hours"], thresholds["red_flag_window_hours"]):
        tier = "HIGH"
        reasons.append(
            f"Forecast meets red-flag screen: RH <= {thresholds['red_flag_rh_percent']}% and wind/gust >= {thresholds['red_flag_wind_mph']} mph for at least {thresholds['red_flag_min_hours']} hours in a {thresholds['red_flag_window_hours']}-hour window."
        )
    elif has_hours_in_window(near_hours, thresholds["near_min_hours"], thresholds["red_flag_window_hours"]):
        tier = "CONCERN"
        reasons.append(
            f"Near red-flag screen: RH <= {thresholds['near_rh_percent']}% with wind/gust >= {thresholds['near_wind_mph']} mph for at least {thresholds['near_min_hours']} hours."
        )

    if max_thunder is not None and max_thunder >= thresholds["thunder_concern_percent"]:
        dry_enough = max_precip is None or max_precip <= thresholds["dry_thunder_precip_max_percent"]
        if dry_enough:
            tier = max_tier(tier, "CONCERN")
            reasons.append(
                f"Dry-thunder signal: thunder probability reaches {max_thunder:.0f}% with low precipitation probability."
            )

    elevated_reasons = []
    if min_rh is not None and min_rh <= thresholds["red_flag_rh_percent"]:
        elevated_reasons.append(f"very low RH forecast near {min_rh:.0f}%")
    if max_usable_wind is not None and max_usable_wind >= thresholds["red_flag_wind_mph"]:
        elevated_reasons.append(f"wind/gust forecast near {max_usable_wind:.0f} mph")
    if max_thunder is not None and max_thunder >= thresholds["elevated_thunder_percent"]:
        elevated_reasons.append(f"thunder probability reaches {max_thunder:.0f}%")

    if tier == "GREEN" and elevated_reasons:
        tier = "ELEVATED"
        reasons.append("Elevated ingredient present: " + "; ".join(elevated_reasons) + ".")

    threat_values = [record["red_flag_threat_index"] for record in records if record["red_flag_threat_index"] not in (None, "")]
    numeric_threats = [value_to_float(value) for value in threat_values]
    numeric_threats = [value for value in numeric_threats if value is not None]
    if numeric_threats and max(numeric_threats) >= 2:
        tier = max_tier(tier, "CONCERN")
        reasons.append(f"NWS grid redFlagThreatIndex reaches {max(numeric_threats):.0f}.")
    elif numeric_threats and max(numeric_threats) > 0 and tier == "GREEN":
        tier = "ELEVATED"
        reasons.append(f"NWS grid redFlagThreatIndex is nonzero ({max(numeric_threats):.0f}).")

    if not reasons:
        reasons.append("No notable red-flag ingredients in the forecast grid.")

    return {
        "tier": tier,
        "min_rh_percent": round(min_rh, 1) if min_rh is not None else None,
        "max_wind_mph": round(max_wind, 1) if max_wind is not None else None,
        "max_gust_mph": round(max_gust, 1) if max_gust is not None else None,
        "max_usable_wind_mph": round(max_usable_wind, 1) if max_usable_wind is not None else None,
        "max_thunder_percent": round(max_thunder, 1) if max_thunder is not None else None,
        "max_precip_percent": round(max_precip, 1) if max_precip is not None else None,
        "red_flag_hours": len(set(critical_hours)),
        "near_hours": len(set(near_hours)),
        "highest_risk_window": risk_window_summary(records, thresholds),
        "reasons": reasons,
    }


def alert_url(feature: Dict[str, Any], props: Dict[str, Any]) -> Optional[str]:
    for value in (feature.get("id"), props.get("@id"), props.get("id")):
        if isinstance(value, str) and value.startswith("http"):
            return value
    return None


def summarize_alerts(
    payload: Dict[str, Any],
    expected_zone: str,
    tz: ZoneInfo,
    monitored_zones: Optional[List[str]] = None,
) -> Dict[str, Any]:
    alerts = []
    high_dates = set()
    monitored_zone_set = set(monitored_zones or [expected_zone])
    for feature in payload.get("features", []):
        props = feature.get("properties", {})
        event = props.get("event") or "Unknown alert"
        zones = [zone.rsplit("/", 1)[-1] for zone in props.get("affectedZones", [])]
        is_fire_alert = event.lower() in ("red flag warning", "fire weather watch")
        if expected_zone not in zones and props.get("geocode", {}).get("UGC"):
            zones.extend(props["geocode"]["UGC"])
        if not (set(zones) & monitored_zone_set):
            continue
        effective_utc = parse_datetime(props.get("effective"))
        ends_utc = parse_datetime(props.get("ends") or props.get("expires"))
        alert = {
            "event": event,
            "headline": props.get("headline"),
            "url": alert_url(feature, props),
            "zones": sorted(set(zones)),
            "areaDesc": props.get("areaDesc"),
            "severity": props.get("severity"),
            "certainty": props.get("certainty"),
            "urgency": props.get("urgency"),
            "effective": datetime_to_local_iso(effective_utc, tz),
            "ends": datetime_to_local_iso(ends_utc, tz),
            "timezone": getattr(tz, "key", str(tz)),
            "status": props.get("status"),
            "messageType": props.get("messageType"),
        }
        alerts.append(alert)
        if is_fire_alert:
            start = effective_utc
            end = ends_utc
            if start is None:
                start = dt.datetime.now(dt.timezone.utc)
            if end is None:
                end = start + dt.timedelta(days=1)
            local_day = start.astimezone(tz).date()
            last_day = (end - dt.timedelta(microseconds=1)).astimezone(tz).date()
            while local_day <= last_day:
                high_dates.add(local_day.isoformat())
                local_day += dt.timedelta(days=1)
    return {
        "count": len(alerts),
        "fire_alert_count": sum(1 for alert in alerts if alert["event"].lower() in ("red flag warning", "fire weather watch")),
        "alerts": alerts,
        "high_dates": sorted(high_dates),
    }


def collect_alert_zones(config: Dict[str, Any], point_results: List[Dict[str, Any]]) -> List[str]:
    zones = {config["fire_weather_zone"]}
    for point in point_results:
        if point.get("status") != "ok":
            continue
        for key in ("fire_weather_zone", "forecast_zone", "county_zone"):
            zone = point.get(key)
            if zone:
                zones.add(zone)
    return sorted(zones)


def fetch_active_alerts_for_zones(session: requests.Session, zones: List[str]) -> Dict[str, Any]:
    features_by_key: Dict[str, Dict[str, Any]] = {}
    for zone in zones:
        payload = request_json(session, f"{NWS_API_BASE}/alerts/active?zone={zone}")
        for index, feature in enumerate(payload.get("features", [])):
            props = feature.get("properties", {})
            key = (
                feature.get("id")
                or props.get("@id")
                or props.get("id")
                or f"{zone}:{props.get('event', 'alert')}:{props.get('effective', '')}:{index}"
            )
            features_by_key[key] = feature
    return {"features": list(features_by_key.values())}


def fetch_discussion_signal(session: requests.Session) -> Dict[str, Any]:
    result = {
        "status": "unavailable",
        "tier": "GREEN",
        "headline": "NWS fire-weather discussion not checked.",
        "matched_lines": [],
        "product_url": None,
    }
    try:
        listing = request_json(session, f"{NWS_API_BASE}/products/types/AFD/locations/GJT", timeout=30)
        products = listing.get("@graph") or []
        if not products:
            result["headline"] = "No GJT AFD products returned."
            return result
        product_url = products[0].get("@id")
        if not product_url:
            result["headline"] = "Latest GJT AFD did not include a product URL."
            return result
        product = request_json(session, product_url, timeout=30)
    except requests.RequestException as exc:
        result["headline"] = f"NWS discussion unavailable: {exc.__class__.__name__}."
        return result

    text = product.get("productText") or ""
    lines = []
    in_fire_section = False
    for raw_line in text.splitlines():
        line = raw_line.strip()
        upper = line.upper()
        if upper.startswith(".FIRE WEATHER"):
            in_fire_section = True
        elif in_fire_section and upper.startswith(".") and "FIRE WEATHER" not in upper:
            in_fire_section = False
        if in_fire_section or any(word in line.lower() for word in ("red flag", "critical fire", "elevated fire", "near critical")):
            lowered = line.lower()
            has_signal = any(
                phrase in lowered
                for phrase in (
                    "red flag",
                    "critical fire",
                    "near critical",
                    "elevated fire",
                    "fire weather watch",
                )
            )
            has_negation = any(phrase in lowered for phrase in ("no critical", "not critical", "below critical", "no red flag"))
            if has_signal and not has_negation:
                lines.append(line)

    result["status"] = "checked"
    result["product_url"] = product_url
    if lines:
        result["tier"] = "CONCERN"
        result["headline"] = "NWS discussion contains fire-weather concern language."
        result["matched_lines"] = lines[:5]
    else:
        result["headline"] = "No concerning fire-weather language found in latest GJT discussion."
    return result


def configured_lpea_sources(lpea_config: Dict[str, Any]) -> List[Dict[str, Any]]:
    if lpea_config.get("sources"):
        return lpea_config["sources"]
    return [
        {
            "name": source.get("name", source["url"]),
            "url": source["url"],
            "type": "official_info",
            "signal_mode": "active",
        }
        for source in lpea_config.get("urls", [])
    ]


def keyword_matches(text: str, keywords: List[str]) -> List[str]:
    lowered = text.lower()
    return [keyword for keyword in keywords if keyword.lower() in lowered]


def visible_source_text(text: str) -> str:
    without_scripts = re.sub(r"<(script|style)\b[^>]*>.*?</\1>", " ", text, flags=re.IGNORECASE | re.DOTALL)
    without_tags = re.sub(r"<[^>]+>", " ", without_scripts)
    return html.unescape(re.sub(r"\s+", " ", without_tags)).strip()


def keyword_snippets(text: str, matches: List[str], max_snippets: int = 2) -> List[str]:
    collapsed = re.sub(r"\s+", " ", text)
    lowered = collapsed.lower()
    snippets = []
    for keyword in matches:
        index = lowered.find(keyword.lower())
        if index < 0:
            continue
        start = max(index - 80, 0)
        end = min(index + len(keyword) + 120, len(collapsed))
        snippet = collapsed[start:end].strip()
        if start > 0:
            snippet = "..." + snippet
        if end < len(collapsed):
            snippet += "..."
        snippets.append(snippet)
        if len(snippets) >= max_snippets:
            break
    return snippets


def configured_fire_posture_sources(config: Dict[str, Any]) -> List[Dict[str, Any]]:
    return config.get("fire_posture", {}).get("sources", [])


def detect_restriction_stage(text: str) -> str:
    lowered = text.lower()
    no_restriction_phrases = [
        "no fire restrictions are currently in effect",
        "no fire restrictions in effect",
        "there are no fire restrictions",
        "no restrictions are currently in effect",
        "fire restrictions have been lifted",
        "fire restrictions lifted",
        "fire restrictions rescinded",
        "restrictions rescinded",
    ]
    if any(phrase in lowered for phrase in no_restriction_phrases):
        return "NONE"
    stage_patterns = [
        ("STAGE 3", r"\bstage\s*(?:3|iii)\b.{0,80}\bfire (?:restrictions?|prohibitions?|bans?)\b|\bfire (?:restrictions?|prohibitions?|bans?)\b.{0,80}\bstage\s*(?:3|iii)\b"),
        ("STAGE 2", r"\bstage\s*(?:2|ii)\b.{0,80}\bfire (?:restrictions?|prohibitions?|bans?)\b|\bfire (?:restrictions?|prohibitions?|bans?)\b.{0,80}\bstage\s*(?:2|ii)\b"),
        ("STAGE 1", r"\bstage\s*(?:1|i)\b.{0,80}\bfire (?:restrictions?|prohibitions?|bans?)\b|\bfire (?:restrictions?|prohibitions?|bans?)\b.{0,80}\bstage\s*(?:1|i)\b"),
    ]
    for label, pattern in stage_patterns:
        if re.search(pattern, lowered):
            return label
    if "fire restrictions are in place" in lowered or "fire restrictions in effect" in lowered:
        return "RESTRICTIONS"
    return "UNKNOWN"


def detect_fire_danger_level(text: str) -> str:
    lowered = text.lower()
    levels = [("EXTREME", "extreme"), ("VERY HIGH", "very high"), ("HIGH", "high"), ("MODERATE", "moderate"), ("LOW", "low")]
    for label, word in levels:
        for match in re.finditer(re.escape(word), lowered):
            start = max(0, match.start() - 100)
            end = min(len(lowered), match.end() + 100)
            if "fire danger" in lowered[start:end]:
                return label
    return "UNKNOWN"


def fire_posture_snippets(text: str, max_snippets: int = 3) -> List[str]:
    keywords = [
        "stage 1",
        "stage i",
        "stage 2",
        "stage ii",
        "fire restrictions",
        "fire prohibitions",
        "fire bans",
        "fire danger",
        "very high",
        "extreme",
        "no fire restrictions",
    ]
    return keyword_snippets(text, [keyword for keyword in keywords if keyword in text.lower()], max_snippets=max_snippets)


def check_fire_posture(session: requests.Session, config: Dict[str, Any]) -> Dict[str, Any]:
    posture_config = config.get("fire_posture", {})
    if not posture_config.get("enabled", False):
        return {"status": "disabled", "headline": "Fire posture check disabled.", "sources": []}

    sources = []
    for source in configured_fire_posture_sources(config):
        result = {
            "name": source.get("name", source.get("url", "Unknown source")),
            "jurisdiction_type": source.get("type", "official"),
            "area": source.get("area", source.get("name", "Unknown area")),
            "url": source.get("url"),
            "status": "unavailable",
            "restriction_stage": "UNKNOWN",
            "fire_danger": "UNKNOWN",
            "snippets": [],
        }
        if not result.get("url"):
            result["status"] = "missing_url"
            sources.append(result)
            continue
        try:
            resp = session.get(result["url"], timeout=20)
            result["status_code"] = resp.status_code
            if resp.status_code < 400:
                text = visible_source_text(resp.text[:300000])
                result["status"] = "reachable"
                result["restriction_stage"] = detect_restriction_stage(text)
                result["fire_danger"] = detect_fire_danger_level(text)
                result["snippets"] = fire_posture_snippets(text)
            else:
                result["status"] = f"http_{resp.status_code}"
        except requests.RequestException as exc:
            result["error"] = exc.__class__.__name__
        sources.append(result)

    reachable = [source for source in sources if source["status"] == "reachable"]
    max_stage = max((source["restriction_stage"] for source in reachable), key=lambda item: FIRE_RESTRICTION_RANK.get(item, 0), default="UNKNOWN")
    max_danger = max((source["fire_danger"] for source in reachable), key=lambda item: FIRE_DANGER_RANK.get(item, 0), default="UNKNOWN")
    active_restrictions = [source for source in reachable if FIRE_RESTRICTION_RANK.get(source["restriction_stage"], 0) >= FIRE_RESTRICTION_RANK["RESTRICTIONS"]]
    danger_sources = [source for source in reachable if FIRE_DANGER_RANK.get(source["fire_danger"], 0) >= FIRE_DANGER_RANK["HIGH"]]

    if active_restrictions:
        source_word = "source indicates" if len(active_restrictions) == 1 else "sources indicate"
        headline = f"{len(active_restrictions)} official {source_word} fire restrictions or staged restrictions."
    elif danger_sources:
        headline = f"Official sources indicate elevated fire danger; no staged restrictions detected by this check."
    elif reachable:
        headline = "Official fire-posture sources reachable; no staged restrictions detected by this check."
    else:
        headline = "Official fire-posture sources unavailable."

    return {
        "status": "checked" if reachable else "unavailable",
        "headline": headline,
        "source_count": len(sources),
        "reachable_source_count": len(reachable),
        "active_restriction_count": len(active_restrictions),
        "high_danger_source_count": len(danger_sources),
        "max_restriction_stage": max_stage,
        "max_fire_danger": max_danger,
        "sources": sources,
        "disclaimer": "Official-source status check only; verify restrictions and burn decisions with the responsible jurisdiction.",
    }


def fire_posture_psps_signal(fire_posture: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    if not fire_posture or fire_posture.get("status") == "disabled":
        return {"level_floor": "LOW", "reason": "Fire posture check disabled or unavailable."}
    max_stage = fire_posture.get("max_restriction_stage", "UNKNOWN")
    max_danger = fire_posture.get("max_fire_danger", "UNKNOWN")
    if FIRE_RESTRICTION_RANK.get(max_stage, 0) >= FIRE_RESTRICTION_RANK["STAGE 2"] or max_danger == "EXTREME":
        return {
            "level_floor": "WATCH",
            "reason": f"Official fire-posture context is escalated ({max_stage}; fire danger {max_danger}), supporting PSPS watch posture.",
        }
    if FIRE_RESTRICTION_RANK.get(max_stage, 0) >= FIRE_RESTRICTION_RANK["STAGE 1"] or FIRE_DANGER_RANK.get(max_danger, 0) >= FIRE_DANGER_RANK["VERY HIGH"]:
        return {
            "level_floor": "ELEVATED",
            "reason": f"Official fire-posture context is elevated ({max_stage}; fire danger {max_danger}), used as supporting context.",
        }
    return {
        "level_floor": "LOW",
        "reason": f"Official fire-posture context is {max_stage}; fire danger {max_danger}.",
    }


def clean_lpea_signal_snippet(snippet: str) -> str:
    collapsed = re.sub(r"\s+", " ", snippet).strip()
    if "Red Flag Warnings are in place across our service territory" in collapsed:
        return "Site-wide LPEA banner: Red Flag Warnings are in place across the service territory; LPEA links members to outage-impact guidance."
    return collapsed


def normalize_lpea_signal_snippet(snippet: str) -> str:
    cleaned = re.sub(r"^\.+|\.+$", "", snippet).strip().lower()
    return re.sub(r"[^a-z0-9]+", " ", cleaned).strip()


def is_low_signal_lpea_snippet(snippet: str) -> bool:
    lowered = snippet.lower()
    boilerplate_phrases = [
        "pay bill outage center contact us search account",
        "power outage tips power restoration plan standby generator requirements",
        "safety programs first responder electrical hazards training",
    ]
    return any(phrase in lowered for phrase in boilerplate_phrases)


def format_source_names(names: List[str]) -> str:
    if not names:
        return "Unknown source"
    if len(names) == 1:
        return names[0]
    if len(names) == 2:
        return f"{names[0]} and {names[1]}"
    return f"{', '.join(names[:-1])}, and {names[-1]}"


def lpea_signal_group_name(snippet: str, source_names: List[str]) -> str:
    lowered = snippet.lower()
    if "site-wide lpea banner" in lowered or "red flag warnings are in place across the service territory" in lowered:
        return "Site-wide red flag banner"
    if len(source_names) > 1:
        return f"Shared signal across {len(source_names)} sources"
    source_name = source_names[0] if source_names else "LPEA signal"
    if source_name == "LPEA LinkedIn":
        if "public safety power shutoffs" in lowered or "vegetation management" in lowered:
            return "LinkedIn PSPS explainer post"
        if "wildfire season" in lowered:
            return "LinkedIn wildfire preparedness post"
    if source_name == "LPEA news releases" and ("07/22/2025" in lowered or "power shutoffs possible" in lowered):
        return "News-release archive PSPS item"
    return source_names[0] if source_names else "LPEA signal"


def group_lpea_signal_hits(hits: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    groups: Dict[str, Dict[str, Any]] = {}
    order: List[str] = []
    for hit in hits:
        snippets = hit.get("snippets") or []
        if not snippets:
            snippets = ["No snippet available."]
        for raw_snippet in snippets[:2]:
            snippet = clean_lpea_signal_snippet(raw_snippet)
            if not snippet or is_low_signal_lpea_snippet(snippet):
                continue
            key = normalize_lpea_signal_snippet(snippet)
            if not key:
                key = f"{hit.get('url', '')}|{','.join(hit.get('matches', []))}"
            if key not in groups:
                groups[key] = {
                    "snippet": snippet,
                    "source_names": [],
                    "urls": [],
                    "matches": [],
                    "types": [],
                }
                order.append(key)
            group = groups[key]
            source_name = hit.get("name", "Unknown source")
            if source_name not in group["source_names"]:
                group["source_names"].append(source_name)
            url = hit.get("url")
            if url and url not in group["urls"]:
                group["urls"].append(url)
            source_type = hit.get("type")
            if source_type and source_type not in group["types"]:
                group["types"].append(source_type)
            for match in hit.get("matches", []):
                if match not in group["matches"]:
                    group["matches"].append(match)

    signal_groups = [groups[key] for key in order]
    for group in signal_groups:
        group["source_count"] = len(group["source_names"])
        group["source_label"] = format_source_names(group["source_names"])
        group["name"] = lpea_signal_group_name(group["snippet"], group["source_names"])
        group["type"] = ", ".join(group["types"])
        group["primary_url"] = group["urls"][0] if group["urls"] else None
    return signal_groups


def check_lpea(session: requests.Session, config: Dict[str, Any]) -> Dict[str, Any]:
    lpea_config = config.get("lpea", {})
    if not lpea_config.get("enabled"):
        return {"status": "disabled", "headline": "LPEA check disabled.", "sources": []}

    sources = []
    active_hits = []
    reference_hits = []
    keywords = lpea_config.get("alert_keywords") or lpea_config.get("fire_keywords", [])
    for source in configured_lpea_sources(lpea_config):
        url = source["url"]
        source_result = {
            "name": source.get("name", url),
            "url": url,
            "type": source.get("type", "official_info"),
            "signal_mode": source.get("signal_mode", "active"),
            "status": "unavailable",
            "matches": [],
            "snippets": [],
        }
        try:
            resp = session.get(url, timeout=20)
            source_result["status_code"] = resp.status_code
            if resp.status_code < 400:
                source_result["status"] = "reachable"
                text = visible_source_text(resp.text[:250000])
                source_result["matches"] = keyword_matches(text, keywords)
                source_result["snippets"] = keyword_snippets(text, source_result["matches"])
                if source_result["matches"]:
                    hit = {
                        "name": source_result["name"],
                        "url": source_result["url"],
                        "type": source_result["type"],
                        "matches": source_result["matches"],
                        "snippets": source_result["snippets"],
                    }
                    if source_result["signal_mode"] == "active":
                        active_hits.append(hit)
                    else:
                        reference_hits.append(hit)
            else:
                source_result["status"] = f"http_{resp.status_code}"
        except requests.RequestException as exc:
            source_result["error"] = exc.__class__.__name__
        sources.append(source_result)

    social_sources = [source for source in sources if source["type"] == "official_social"]
    social_reachable = sum(1 for source in social_sources if source["status"] == "reachable")
    if active_hits:
        headline = "LPEA active/update sources contained power-interruption keywords; review source before treating as confirmed outage intent."
        status = "active_keyword_match"
    elif reference_hits:
        headline = "LPEA standing/reference pages contain outage/fire-safety language; no active update source matched."
        status = "reference_keyword_match"
    elif any(source["status"] == "reachable" for source in sources):
        headline = "LPEA monitored public sources reachable; no power-interruption keywords detected by this lightweight check."
        status = "reachable_no_power_keywords"
    else:
        headline = "LPEA signal unavailable; no stable parseable public signal found."
        status = "unavailable"

    return {
        "status": status,
        "headline": headline,
        "active_hits": active_hits,
        "reference_hits": reference_hits,
        "active_signal_groups": group_lpea_signal_hits(active_hits),
        "reference_signal_groups": group_lpea_signal_hits(reference_hits),
        "monitored_source_count": len(sources),
        "social_status": f"{social_reachable}/{len(social_sources)} official social sources reachable" if social_sources else "no official social sources configured",
        "sources": sources,
    }


def resolve_point(session: requests.Session, point: Dict[str, Any]) -> Dict[str, Any]:
    url = f"{NWS_API_BASE}/points/{point['lat']},{point['lon']}"
    payload = request_json(session, url)
    props = payload.get("properties", {})
    fire_zone = (props.get("fireWeatherZone") or "").rsplit("/", 1)[-1]
    return {
        "name": point["name"],
        "lat": point["lat"],
        "lon": point["lon"],
        "point_url": url,
        "grid_url": props.get("forecastGridData"),
        "fire_weather_zone": fire_zone,
        "forecast_zone": (props.get("forecastZone") or "").rsplit("/", 1)[-1],
        "county_zone": (props.get("county") or "").rsplit("/", 1)[-1],
    }


def analyze_point(
    session: requests.Session,
    point: Dict[str, Any],
    config: Dict[str, Any],
    now_utc: dt.datetime,
    horizon_end_utc: dt.datetime,
    tz: ZoneInfo,
) -> Dict[str, Any]:
    try:
        resolved = resolve_point(session, point)
        if not resolved.get("grid_url"):
            raise RuntimeError("No forecastGridData URL returned.")
        grid = request_json(session, resolved["grid_url"])
        records = build_hourly_records(grid.get("properties", {}), now_utc, horizon_end_utc, tz)
    except (requests.RequestException, RuntimeError, ValueError) as exc:
        return {
            "name": point["name"],
            "lat": point["lat"],
            "lon": point["lon"],
            "status": "unavailable",
            "error": f"{exc.__class__.__name__}: {exc}",
            "days": [],
        }

    grouped: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for record in records:
        grouped[record["date"]].append(record)

    days = []
    start_local_date = now_utc.astimezone(tz).date()
    for offset in range(config["forecast_horizon_days"]):
        date_key = (start_local_date + dt.timedelta(days=offset)).isoformat()
        scored = score_day(grouped.get(date_key, []), config["thresholds"])
        days.append({"date": date_key, **scored})

    expected_zone = config["fire_weather_zone"]
    zone_status = "matches" if resolved["fire_weather_zone"] == expected_zone else "adjacent_or_mismatch"
    return {
        **resolved,
        "status": "ok",
        "zone_status": zone_status,
        "days": days,
    }


def combine_daily_results(
    point_results: List[Dict[str, Any]],
    alert_summary: Dict[str, Any],
    discussion: Dict[str, Any],
    config: Dict[str, Any],
    now_utc: dt.datetime,
    tz: ZoneInfo,
) -> List[Dict[str, Any]]:
    start_local_date = now_utc.astimezone(tz).date()
    combined = []
    for offset in range(config["forecast_horizon_days"]):
        date_key = (start_local_date + dt.timedelta(days=offset)).isoformat()
        tier = "GREEN"
        point_summaries = []
        reason_entries = []
        for point in point_results:
            if point.get("status") != "ok":
                continue
            day = next((item for item in point["days"] if item["date"] == date_key), None)
            if not day:
                continue
            tier = max_tier(tier, day["tier"])
            if day["tier"] != "GREEN":
                reason_entries.append(
                    {
                        "tier": day["tier"],
                        "reason": f"{point['name']}: {day['reasons'][0]}",
                    }
                )
            point_summaries.append(
                {
                    "name": point["name"],
                    "tier": day["tier"],
                    "min_rh_percent": day["min_rh_percent"],
                    "max_usable_wind_mph": day["max_usable_wind_mph"],
                    "max_thunder_percent": day["max_thunder_percent"],
                    "max_precip_percent": day["max_precip_percent"],
                    "red_flag_hours": day["red_flag_hours"],
                    "near_hours": day["near_hours"],
                    "highest_risk_window": day.get("highest_risk_window", "n/a"),
                    "reasons": day["reasons"],
                }
            )

        if date_key in alert_summary.get("high_dates", []):
            tier = "HIGH"
            reason_entries.append(
                {
                    "tier": "HIGH",
                    "reason": "Active NWS Red Flag Warning or Fire Weather Watch touches this local date.",
                }
            )

        if reason_entries:
            reason_entries.sort(key=lambda item: TIER_RANK[item["tier"]], reverse=True)
            reasons = [entry["reason"] for entry in reason_entries[:5]]
        else:
            reasons = ["No notable red-flag ingredients across sampled county points."]

        combined.append(
            {
                "date": date_key,
                "tier": tier,
                "reasons": reasons[:5],
                "points": point_summaries,
            }
        )

    if discussion.get("tier") == "CONCERN" and all(day["tier"] == "GREEN" for day in combined):
        combined[0]["tier"] = "CONCERN"
        combined[0]["reasons"].insert(0, discussion["headline"])

    return combined


def overall_tier(days: List[Dict[str, Any]], point_results: List[Dict[str, Any]], discussion: Dict[str, Any]) -> str:
    tier = max((day["tier"] for day in days), key=lambda item: TIER_RANK[item])
    if all(point.get("status") != "ok" for point in point_results):
        return "CONCERN"
    if discussion.get("tier") == "CONCERN":
        tier = max_tier(tier, "CONCERN")
    return tier


def lpea_active_text(lpea: Dict[str, Any]) -> str:
    parts = []
    for hit in lpea.get("active_hits", []):
        parts.extend(hit.get("matches", []))
        parts.extend(hit.get("snippets", []))
    return " ".join(parts).lower()


def lpea_active_snippet_text(lpea: Dict[str, Any]) -> str:
    parts = []
    for hit in lpea.get("active_hits", []):
        parts.extend(hit.get("snippets", []))
    return " ".join(parts).lower()


def lpea_psps_signal(lpea: Dict[str, Any]) -> Dict[str, Any]:
    text = lpea_active_text(lpea)
    snippet_text = lpea_active_snippet_text(lpea)
    direct_phrases = [
        "public safety power shutoff alert",
        "psps alert",
        "psps active",
        "precautionary public safety power shutoff",
        "planned power shutoff",
        "will de-energize",
        "will turn off power",
        "electric service will be affected",
    ]
    active_phrases = [
        "red flag warnings are in place",
        "red flag warning",
        "public safety power shutoff",
        "psps",
        "power shutoff",
        "power shutoffs possible",
        "public safety power shutoffs possible",
        "de-energize",
        "power outage",
        "wildfire",
    ]
    direct_matches = [phrase for phrase in direct_phrases if phrase in snippet_text]
    active_matches = [phrase for phrase in active_phrases if phrase in text]
    if direct_matches:
        return {
            "level": "direct_psps_language",
            "matches": direct_matches,
            "reason": "LPEA active/update source contains direct PSPS or power-shutoff language.",
        }
    if active_matches:
        return {
            "level": "active_wildfire_power_language",
            "matches": active_matches,
            "reason": "LPEA active/update source contains red-flag, wildfire, or power-interruption language.",
        }
    return {
        "level": "none",
        "matches": [],
        "reason": "No active LPEA source matched PSPS-specific language.",
    }


def psps_level_from_weather_score(score: int) -> str:
    if score >= 65:
        return "LIKELY"
    if score >= 45:
        return "WATCH"
    if score >= 18:
        return "ELEVATED"
    return "LOW"


def score_weather_inputs(
    date_key: str,
    min_rh: Optional[float],
    max_wind: Optional[float],
    max_thunder: Optional[float],
    max_precip: Optional[float],
    red_flag_hours: int,
    near_hours: int,
    official_alerts: Dict[str, Any],
) -> Dict[str, Any]:
    score = 0
    factors = []

    if max_wind is not None:
        if max_wind >= 35:
            score += 35
            factors.append(f"very strong wind/gust signal near {max_wind:.0f} mph")
        elif max_wind >= 30:
            score += 31
            factors.append(f"strong wind/gust signal near {max_wind:.0f} mph")
        elif max_wind >= 25:
            score += 25
            factors.append(f"red-flag wind/gust signal near {max_wind:.0f} mph")
        elif max_wind >= 20:
            score += 16
            factors.append(f"near-threshold wind/gust signal near {max_wind:.0f} mph")
        elif max_wind >= 15:
            score += 8
            factors.append(f"breezy wind/gust signal near {max_wind:.0f} mph")

    if min_rh is not None:
        if min_rh <= 8:
            score += 25
            factors.append(f"critically dry RH near {min_rh:.0f}%")
        elif min_rh <= 12:
            score += 22
            factors.append(f"very dry RH near {min_rh:.0f}%")
        elif min_rh <= 15:
            score += 18
            factors.append(f"red-flag RH near {min_rh:.0f}%")
        elif min_rh <= 18:
            score += 12
            factors.append(f"near-threshold RH near {min_rh:.0f}%")
        elif min_rh <= 22:
            score += 6
            factors.append(f"dry RH near {min_rh:.0f}%")

    if red_flag_hours >= 4:
        score += 24
        factors.append(f"{red_flag_hours} sampled hours meet red-flag screen")
    elif red_flag_hours >= 3:
        score += 20
        factors.append(f"{red_flag_hours} sampled hours meet red-flag screen")
    elif near_hours >= 4:
        score += 14
        factors.append(f"{near_hours} sampled hours are near red-flag thresholds")
    elif near_hours >= 2:
        score += 10
        factors.append(f"{near_hours} sampled hours are near red-flag thresholds")

    if max_thunder is not None:
        dry_enough = max_precip is None or max_precip <= 20
        if max_thunder >= 30 and dry_enough:
            score += 10
            factors.append(f"dry-thunder signal near {max_thunder:.0f}%")
        elif max_thunder >= 20 and dry_enough:
            score += 7
            factors.append(f"thunder signal near {max_thunder:.0f}% with limited precip")
        elif max_thunder >= 15:
            score += 4
            factors.append(f"modest thunder signal near {max_thunder:.0f}%")

    if date_key in official_alerts.get("high_dates", []):
        score += 15
        factors.append("official NWS Red Flag Warning or Fire Weather Watch touches this day")

    score = min(score, 100)
    level = psps_level_from_weather_score(score)
    if not factors:
        factors.append("weather inputs stay below PSPS watch thresholds")
    summary = (
        f"Weather score {score}/100: "
        f"RH {format_metric(min_rh, '%')}, wind/gust {format_metric(max_wind, ' mph')}, "
        f"red-flag hours {red_flag_hours}, near-threshold hours {near_hours}."
    )
    return {
        "score": score,
        "level": level,
        "summary": summary,
        "factors": factors,
        "metrics": {
            "min_rh_percent": min_rh,
            "max_usable_wind_mph": max_wind,
            "max_thunder_percent": max_thunder,
            "max_precip_percent": max_precip,
            "max_red_flag_hours": red_flag_hours,
            "max_near_hours": near_hours,
        },
    }


def location_weather_score(point: Dict[str, Any], date_key: str, official_alerts: Dict[str, Any]) -> Dict[str, Any]:
    scored = score_weather_inputs(
        date_key,
        point.get("min_rh_percent"),
        point.get("max_usable_wind_mph"),
        point.get("max_thunder_percent"),
        point.get("max_precip_percent"),
        point.get("red_flag_hours") or 0,
        point.get("near_hours") or 0,
        official_alerts,
    )
    return {
        "name": point.get("name", "Unknown location"),
        "score": scored["score"],
        "level": scored["level"],
        "summary": scored["summary"],
        "factors": scored["factors"],
        "metrics": scored["metrics"],
        "highest_risk_window": point.get("highest_risk_window", "n/a"),
        "fire_weather_tier": point.get("tier"),
    }


def weather_score_for_day(day: Dict[str, Any], official_alerts: Dict[str, Any]) -> Dict[str, Any]:
    points = day.get("points", [])
    location_scores = [
        location_weather_score(point, day["date"], official_alerts)
        for point in points
    ]
    location_scores.sort(key=lambda item: (item["score"], PSPS_RANK.get(item["level"], 0)), reverse=True)
    if location_scores:
        scored = {
            "score": location_scores[0]["score"],
            "level": location_scores[0]["level"],
            "summary": f"Top weather score {location_scores[0]['score']}/100 at {location_scores[0]['name']}. {location_scores[0]['summary']}",
            "factors": location_scores[0]["factors"],
            "metrics": location_scores[0]["metrics"],
        }
    else:
        scored = score_weather_inputs(day["date"], None, None, None, None, 0, 0, official_alerts)
    driver_locations = [item for item in location_scores if item["score"] >= 45]
    if not driver_locations and location_scores:
        driver_locations = location_scores[:3]
    scored["location_scores"] = location_scores
    scored["driver_locations"] = driver_locations[:5]
    return scored


def metric_delta(current: Optional[float], previous: Optional[float]) -> Optional[float]:
    if current is None or previous is None:
        return None
    return current - previous


def trend_label(score_delta: Optional[float], wind_delta: Optional[float], rh_delta: Optional[float], red_flag_delta: Optional[float]) -> str:
    worsening = (
        (score_delta is not None and score_delta >= 8)
        or (wind_delta is not None and wind_delta >= 5)
        or (rh_delta is not None and rh_delta <= -4)
        or (red_flag_delta is not None and red_flag_delta >= 2)
    )
    easing = (
        (score_delta is not None and score_delta <= -8)
        or (wind_delta is not None and wind_delta <= -5)
        or (rh_delta is not None and rh_delta >= 4)
        or (red_flag_delta is not None and red_flag_delta <= -2)
    )
    if worsening and not easing:
        return "Worsening"
    if easing and not worsening:
        return "Easing"
    return "Steady"


def signed_metric(value: Optional[float], suffix: str = "") -> str:
    if value is None:
        return "n/a"
    sign = "+" if value > 0 else ""
    return f"{sign}{value:.0f}{suffix}"


def add_weather_trends(forecast_days: List[Dict[str, Any]]) -> None:
    previous: Optional[Dict[str, Any]] = None
    for day in forecast_days:
        metrics = day.get("weather_metrics", {})
        if previous is None:
            day["trend"] = {
                "label": "Starting point",
                "score_delta": None,
                "wind_delta_mph": None,
                "rh_delta_percent": None,
                "red_flag_hours_delta": None,
                "summary": "First day in this forecast run; trend builds from following days.",
            }
        else:
            previous_metrics = previous.get("weather_metrics", {})
            score_delta = metric_delta(safe_float(day.get("weather_score")), safe_float(previous.get("weather_score")))
            wind_delta = metric_delta(safe_float(metrics.get("max_usable_wind_mph")), safe_float(previous_metrics.get("max_usable_wind_mph")))
            rh_delta = metric_delta(safe_float(metrics.get("min_rh_percent")), safe_float(previous_metrics.get("min_rh_percent")))
            red_flag_delta = metric_delta(safe_float(metrics.get("max_red_flag_hours")), safe_float(previous_metrics.get("max_red_flag_hours")))
            label = trend_label(score_delta, wind_delta, rh_delta, red_flag_delta)
            day["trend"] = {
                "label": label,
                "score_delta": score_delta,
                "wind_delta_mph": wind_delta,
                "rh_delta_percent": rh_delta,
                "red_flag_hours_delta": red_flag_delta,
                "summary": (
                    f"{label}: score {signed_metric(score_delta)}, wind {signed_metric(wind_delta, ' mph')}, "
                    f"RH {signed_metric(rh_delta, '%')}, red-flag hours {signed_metric(red_flag_delta)} vs prior day."
                ),
            }
        previous = day


def build_psps_forecast(
    days: List[Dict[str, Any]],
    official_alerts: Dict[str, Any],
    lpea: Dict[str, Any],
    fire_posture: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    lpea_signal = lpea_psps_signal(lpea)
    posture_signal = fire_posture_psps_signal(fire_posture)
    active_lpea_signal = bool(lpea.get("active_hits"))
    forecast_days = []

    for day in days:
        weather_score = weather_score_for_day(day, official_alerts)
        level = weather_score["level"]
        reasons = [weather_score["summary"], *weather_score["factors"][:3]]

        if posture_signal["level_floor"] != "LOW":
            level = max_psps_level(level, posture_signal["level_floor"])
            reasons.append(posture_signal["reason"])

        if lpea_signal["level"] == "direct_psps_language":
            level = max_psps_level(level, "WATCH")
            reasons.append(lpea_signal["reason"])
        elif active_lpea_signal:
            reasons.append("LPEA active/update sources currently contain red-flag or power-interruption language, used as supporting context.")

        if not reasons:
            reasons.append("No red-flag or active LPEA PSPS signal for this day.")

        forecast_days.append(
            {
                "date": day["date"],
                "level": level,
                "fire_weather_tier": day["tier"],
                "weather_score": weather_score["score"],
                "weather_metrics": weather_score["metrics"],
                "weather_factors": weather_score["factors"],
                "driver_locations": weather_score["driver_locations"],
                "location_scores": weather_score["location_scores"],
                "reasons": reasons,
            }
        )

    add_weather_trends(forecast_days)
    overall_level = max((day["level"] for day in forecast_days), key=lambda level: PSPS_RANK[level])
    if overall_level == "LIKELY":
        headline = "PSPS likelihood is high on weather-driven red-flag days; prepare for possible LPEA safety-related interruption behavior."
    elif overall_level == "WATCH":
        headline = "Weather-driven PSPS watch conditions are present; monitor LPEA updates and outage channels."
    elif overall_level == "ELEVATED":
        headline = "PSPS likelihood is elevated, but weather remains below watch thresholds."
    else:
        headline = "PSPS likelihood is low based on current monitor inputs."

    return {
        "overall_level": overall_level,
        "headline": headline,
        "lpea_signal": lpea_signal,
        "fire_posture_signal": posture_signal,
        "days": forecast_days,
        "disclaimer": UNOFFICIAL_MONITOR_DISCLAIMER,
    }


def previous_tier(history_path: Path) -> Optional[str]:
    if not history_path.exists():
        return None
    try:
        with history_path.open("r", encoding="utf-8", newline="") as fh:
            rows = list(csv.DictReader(fh))
    except OSError:
        return None
    return rows[-1].get("overall_tier") if rows else None


def load_psps_events(path: Path) -> List[Dict[str, Any]]:
    if not path.exists():
        return []
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return []
    if isinstance(payload, list):
        events = payload
    else:
        events = payload.get("events", [])
    return [event for event in events if isinstance(event, dict)]


def ensure_psps_event_log(path: Path) -> None:
    if path.exists():
        return
    template = {
        "description": "Manually add confirmed or candidate LPEA Public Safety Power Shutoff events here. The dashboard uses confirmed events to calibrate predictions.",
        "events": [],
        "example_event": {
            "date": "2026-07-26",
            "status": "confirmed",
            "source": "LPEA",
            "source_url": "https://lpea.coop/",
            "locations": ["Pagosa Springs"],
            "started_at": "2026-07-26T14:00:00-06:00",
            "ended_at": "2026-07-26T18:00:00-06:00",
            "summary": "Example only; remove or replace with a real PSPS event.",
        },
    }
    path.write_text(json.dumps(template, indent=2), encoding="utf-8")


def load_forecast_history(path: Path) -> List[Dict[str, Any]]:
    if not path.exists():
        return []
    try:
        with path.open("r", encoding="utf-8", newline="") as fh:
            return list(csv.DictReader(fh))
    except OSError:
        return []


def event_date(event: Dict[str, Any]) -> Optional[str]:
    if event.get("date"):
        return str(event["date"])
    parsed = parse_datetime(event.get("started_at"))
    return parsed.date().isoformat() if parsed else None


def event_locations(event: Dict[str, Any]) -> List[str]:
    locations = event.get("locations") or []
    if isinstance(locations, str):
        return [locations]
    return [str(location) for location in locations]


def history_row_matches_event(row: Dict[str, Any], event: Dict[str, Any]) -> bool:
    date_key = event_date(event)
    if not date_key or row.get("date") != date_key:
        return False
    locations = event_locations(event)
    if not locations:
        return True
    row_location = row.get("location", "")
    return any(location.lower() in row_location.lower() or row_location.lower() in location.lower() for location in locations)


def best_prediction_level(rows: List[Dict[str, Any]]) -> str:
    if not rows:
        return "NONE"
    return max((row.get("psps_level", "LOW") for row in rows), key=lambda level: PSPS_RANK.get(level, -1))


def build_calibration_summary(
    events: List[Dict[str, Any]],
    forecast_history: List[Dict[str, Any]],
    current_psps: Dict[str, Any],
    today: dt.date,
    event_path: Path,
    forecast_path: Path,
) -> Dict[str, Any]:
    confirmed_events = [event for event in events if str(event.get("status", "confirmed")).lower() == "confirmed"]
    candidate_events = [event for event in events if str(event.get("status", "")).lower() != "confirmed"]
    event_dates = {date for date in (event_date(event) for event in confirmed_events) if date}
    hits = []
    misses = []
    for event in confirmed_events:
        matching_rows = [row for row in forecast_history if history_row_matches_event(row, event)]
        level = best_prediction_level(matching_rows)
        scored_event = {
            "date": event_date(event),
            "locations": event_locations(event),
            "summary": event.get("summary", "Confirmed PSPS event."),
            "source_url": event.get("source_url"),
            "best_predicted_level": level,
        }
        if PSPS_RANK.get(level, -1) >= PSPS_RANK["WATCH"]:
            hits.append(scored_event)
        else:
            misses.append(scored_event)

    past_watch_days = set()
    false_watch_days = set()
    for row in forecast_history:
        date_key = row.get("date")
        if not date_key:
            continue
        try:
            row_date = dt.date.fromisoformat(date_key)
        except ValueError:
            continue
        if row_date >= today:
            continue
        if PSPS_RANK.get(row.get("psps_level", "LOW"), 0) >= PSPS_RANK["WATCH"]:
            past_watch_days.add(date_key)
            if date_key not in event_dates:
                false_watch_days.add(date_key)

    pending_watch_days = [
        day["date"]
        for day in current_psps.get("days", [])
        if PSPS_RANK.get(day.get("level", "LOW"), 0) >= PSPS_RANK["WATCH"]
    ]
    if confirmed_events:
        hit_rate = round((len(hits) / len(confirmed_events)) * 100)
        summary = f"{len(hits)}/{len(confirmed_events)} confirmed PSPS event{'s' if len(confirmed_events) != 1 else ''} had WATCH-or-higher monitor signal."
    else:
        hit_rate = None
        summary = "No confirmed LPEA PSPS events logged yet; calibration will start once events are added."

    return {
        "event_log_path": f"archuleta_red_flag_monitor/{event_path.name}",
        "forecast_history_path": f"archuleta_red_flag_monitor/{forecast_path.name}",
        "confirmed_event_count": len(confirmed_events),
        "candidate_event_count": len(candidate_events),
        "hit_count": len(hits),
        "miss_count": len(misses),
        "hit_rate_percent": hit_rate,
        "false_watch_day_count": len(false_watch_days),
        "false_watch_examples": sorted(false_watch_days)[-5:],
        "pending_watch_dates": pending_watch_days,
        "summary": summary,
        "hits": hits[-5:],
        "misses": misses[-5:],
        "logged_events": confirmed_events[-5:],
    }


def forecast_history_rows(report: Dict[str, Any]) -> List[Dict[str, Any]]:
    rows = []
    official_count = report.get("official_alerts", {}).get("fire_alert_count", 0)
    lpea_signal_level = report.get("psps", {}).get("lpea_signal", {}).get("level", "none")
    posture = report.get("fire_posture", {})
    for day in report.get("psps", {}).get("days", []):
        for location in day.get("location_scores", []) or [{"name": "Area", "level": day.get("level"), "score": day.get("weather_score"), "metrics": day.get("weather_metrics", {})}]:
            metrics = location.get("metrics", {})
            rows.append(
                {
                    "generated_at": report.get("generated_at_local") or report.get("generated_at"),
                    "date": day.get("date"),
                    "location": location.get("name", "Unknown location"),
                    "psps_level": location.get("level", day.get("level", "LOW")),
                    "weather_score": location.get("score", day.get("weather_score")),
                    "fire_weather_tier": location.get("fire_weather_tier", day.get("fire_weather_tier")),
                    "min_rh_percent": metrics.get("min_rh_percent"),
                    "max_wind_mph": metrics.get("max_usable_wind_mph"),
                    "max_thunder_percent": metrics.get("max_thunder_percent"),
                    "red_flag_hours": metrics.get("max_red_flag_hours"),
                    "near_hours": metrics.get("max_near_hours"),
                    "highest_risk_window": location.get("highest_risk_window", "n/a"),
                    "overall_psps_level": report.get("psps", {}).get("overall_level"),
                    "lpea_signal_level": lpea_signal_level,
                    "official_fire_alert_count": official_count,
                    "max_fire_restriction_stage": posture.get("max_restriction_stage", "UNKNOWN"),
                    "max_fire_danger": posture.get("max_fire_danger", "UNKNOWN"),
                }
            )
    return rows


def append_forecast_history(report: Dict[str, Any], path: Path) -> None:
    rows = forecast_history_rows(report)
    fieldnames = [
        "generated_at",
        "date",
        "location",
        "psps_level",
        "weather_score",
        "fire_weather_tier",
        "min_rh_percent",
        "max_wind_mph",
        "max_thunder_percent",
        "red_flag_hours",
        "near_hours",
        "highest_risk_window",
        "overall_psps_level",
        "lpea_signal_level",
        "official_fire_alert_count",
        "max_fire_restriction_stage",
        "max_fire_danger",
    ]
    exists = path.exists()
    if exists:
        try:
            with path.open("r", encoding="utf-8", newline="") as fh:
                reader = csv.DictReader(fh)
                existing_fieldnames = reader.fieldnames or []
                existing_rows = list(reader)
            if existing_fieldnames != fieldnames:
                with path.open("w", encoding="utf-8", newline="") as fh:
                    writer = csv.DictWriter(fh, fieldnames=fieldnames)
                    writer.writeheader()
                    for row in existing_rows:
                        writer.writerow({key: row.get(key, "") for key in fieldnames})
                exists = True
        except OSError:
            exists = False
    with path.open("a", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        if not exists:
            writer.writeheader()
        writer.writerows(rows)


def write_outputs(report: Dict[str, Any], config_path: Path, config: Dict[str, Any]) -> None:
    base = config_path.resolve().parent
    output = config["output"]
    latest_json = base / output["latest_json"]
    latest_md = base / output["latest_markdown"]
    latest_html = base / output["latest_html"]
    history_csv = base / output["history_csv"]
    psps_events_path = event_log_path(config_path, config)
    forecast_csv = forecast_history_path(config_path, config)

    latest_json.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    latest_md.write_text(render_markdown(report), encoding="utf-8")
    latest_html.write_text(render_html(report), encoding="utf-8")
    ensure_psps_event_log(psps_events_path)
    append_forecast_history(report, forecast_csv)

    exists = history_csv.exists()
    with history_csv.open("a", encoding="utf-8", newline="") as fh:
        fieldnames = [
            "generated_at",
            "overall_tier",
            "notify_recommended",
            "non_green_dates",
            "active_fire_alerts",
            "lpea_status",
            "discussion_status",
        ]
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        if not exists:
            writer.writeheader()
        writer.writerow(
            {
                "generated_at": report["generated_at"],
                "overall_tier": report["overall_tier"],
                "notify_recommended": report["notify_recommended"],
                "non_green_dates": ",".join(day["date"] for day in report["days"] if day["tier"] != "GREEN"),
                "active_fire_alerts": report["official_alerts"]["fire_alert_count"],
                "lpea_status": report["lpea"]["status"],
                "discussion_status": report["discussion"]["status"],
            }
        )


def format_metric(value: Any, suffix: str = "") -> str:
    if value is None:
        return "n/a"
    if isinstance(value, float):
        return f"{value:.0f}{suffix}"
    return f"{value}{suffix}"


def collect_dates_by_tier(days: List[Dict[str, Any]], tier: str) -> List[str]:
    return [day["date"] for day in days if day["tier"] == tier]


def collect_psps_dates_by_level(psps_days: List[Dict[str, Any]], level: str) -> List[str]:
    return [day["date"] for day in psps_days if day["level"] == level]


def format_display_date(date_text: str, include_year: bool = False) -> str:
    try:
        parsed = dt.date.fromisoformat(date_text)
    except ValueError:
        return date_text
    label = f"{parsed.strftime('%a')}, {parsed.strftime('%b')} {parsed.day}"
    if include_year:
        label = f"{label}, {parsed.year}"
    return label


def split_display_date(date_text: str) -> Tuple[str, str]:
    try:
        parsed = dt.date.fromisoformat(date_text)
    except ValueError:
        return "", date_text
    return parsed.strftime("%a"), f"{parsed.strftime('%b')} {parsed.day}"


def format_date_list(dates: List[str]) -> str:
    return "; ".join(format_display_date(date_text) for date_text in dates) if dates else "None"


def local_time_context(report: Dict[str, Any]) -> str:
    name = report.get("local_time_name") or "Pagosa Springs, CO"
    timezone_name = report.get("timezone") or "America/Denver"
    return f"{name} local time ({timezone_name})"


def format_generated_at(report: Dict[str, Any]) -> str:
    raw_value = report.get("generated_at_local")
    if not raw_value:
        return "Unknown"
    return format_local_datetime(raw_value, report)


def format_next_update_at(report: Dict[str, Any]) -> str:
    raw_value = report.get("next_update_at")
    if not raw_value:
        return "Not scheduled"
    return format_local_datetime(raw_value, report)


def format_local_datetime(raw_value: str, report: Dict[str, Any]) -> str:
    try:
        parsed = dt.datetime.fromisoformat(raw_value)
        timezone_name = report.get("timezone")
        if timezone_name:
            parsed = parsed.astimezone(ZoneInfo(timezone_name))
    except (ValueError, TypeError, ZoneInfoNotFoundError):
        return str(raw_value)
    hour = parsed.strftime("%I").lstrip("0") or "0"
    tz_name = parsed.tzname() or ""
    timestamp = f"{parsed.strftime('%b')} {parsed.day}, {parsed.year} at {hour}:{parsed.strftime('%M %p')} {tz_name}".strip()
    return f"{timestamp} ({report.get('local_time_name') or 'Pagosa Springs, CO'} local time)"


def official_fire_alert_label(report: Dict[str, Any]) -> str:
    zone = report.get("fire_weather_zone", "COZ295")
    return f"Official NWS Red Flag / Fire Weather alerts ({zone})"


def tier_badge_class(tier: str) -> str:
    return f"tier-{tier.lower()}"


def fire_status_class(value: str) -> str:
    return "fire-" + re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def escape_html(value: Any) -> str:
    return html.escape("" if value is None else str(value))


def lpea_source_url(report: Dict[str, Any], source_name: str, default_url: str) -> str:
    for source in report.get("lpea", {}).get("sources", []):
        if source.get("name") == source_name and source.get("url"):
            return source["url"]
    return default_url


def lpea_outage_url(report: Dict[str, Any]) -> str:
    return lpea_source_url(report, "LPEA outage center", LPEA_DEFAULT_OUTAGE_URL)


def lpea_psps_url(report: Dict[str, Any]) -> str:
    return lpea_source_url(report, "LPEA wildfire / public safety power shutoffs", LPEA_DEFAULT_PSPS_URL)


def lpea_outage_map_url(report: Dict[str, Any]) -> str:
    return lpea_source_url(report, "LPEA outage map", LPEA_DEFAULT_OUTAGE_MAP_URL)


def source_group_links_html(group: Dict[str, Any]) -> str:
    names = group.get("source_names", [])
    urls = group.get("urls", [])
    links = []
    for index, name in enumerate(names):
        url = urls[index] if index < len(urls) else group.get("primary_url")
        if url:
            links.append(f'<a href="{escape_html(url)}" target="_blank" rel="noopener noreferrer">{escape_html(name)}</a>')
        else:
            links.append(escape_html(name))
    return ", ".join(links) if links else "Unknown source"


def linked_text_html(text: str, url: Optional[str]) -> str:
    if url:
        return f'<a href="{escape_html(url)}" target="_blank" rel="noopener noreferrer">{escape_html(text)}</a>'
    return escape_html(text)


def build_brief_summary(report: Dict[str, Any]) -> List[str]:
    high_dates = collect_dates_by_tier(report["days"], "HIGH")
    concern_dates = collect_dates_by_tier(report["days"], "CONCERN")
    elevated_dates = collect_dates_by_tier(report["days"], "ELEVATED")
    likely_psps_dates = collect_psps_dates_by_level(report.get("psps", {}).get("days", []), "LIKELY")
    watch_psps_dates = collect_psps_dates_by_level(report.get("psps", {}).get("days", []), "WATCH")
    notify_text = "YES" if report["notify_recommended"] else "NO"
    return [
        f"Overall tier: {report['overall_tier']}",
        f"PSPS likelihood: {report.get('psps', {}).get('overall_level', 'UNKNOWN')}",
        f"PSPS likely dates: {format_date_list(likely_psps_dates)}",
        f"PSPS watch dates: {format_date_list(watch_psps_dates)}",
        f"Monitor heads-up recommended: {notify_text}",
        f"High dates: {format_date_list(high_dates)}",
        f"Concern dates: {format_date_list(concern_dates)}",
        f"Elevated dates: {format_date_list(elevated_dates)}",
        f"{official_fire_alert_label(report)}: {report['official_alerts']['fire_alert_count']}",
        f"LPEA status: {report['lpea']['status']} - {report['lpea']['headline']}",
        f"LPEA source coverage: {report['lpea'].get('monitored_source_count', 0)} sources; {report['lpea'].get('social_status', 'social sources not configured')}",
        f"Fire posture: {report.get('fire_posture', {}).get('max_restriction_stage', 'UNKNOWN')} restrictions; fire danger {report.get('fire_posture', {}).get('max_fire_danger', 'UNKNOWN')}",
        f"NWS discussion: {report['discussion']['headline']}",
    ]


def monitor_heads_up_note(report: Dict[str, Any]) -> str:
    if report.get("notify_recommended"):
        if report.get("overall_tier") != "GREEN":
            return f"Send this monitor report because current risk is {report.get('overall_tier', 'UNKNOWN')}. This is not an official LPEA or NWS notice."
        return "Send a follow-up because the previous run was not green. This is not an official LPEA or NWS notice."
    return "No: current and previous monitor tiers are green, so this run can stay quiet."


def lpea_hit_summary(hit: Dict[str, Any]) -> str:
    matches = ", ".join(hit.get("matches", [])[:6])
    suffix = f" ({matches})" if matches else ""
    return f"{hit.get('name', 'Unknown source')}{suffix}"


def lpea_signal_group_summary(group: Dict[str, Any]) -> str:
    matches = ", ".join(group.get("matches", [])[:6])
    suffix = f" ({matches})" if matches else ""
    source_count = group.get("source_count", len(group.get("source_names", [])))
    if source_count > 1:
        return f"{group.get('name', 'Shared LPEA signal')} across {source_count} sources: {group.get('source_label', 'Unknown sources')}{suffix}"
    return f"{group.get('name', 'LPEA signal')}{suffix}"


def lpea_status_label(status: str) -> str:
    labels = {
        "active_keyword_match": "Active source match",
        "reference_keyword_match": "Reference-only match",
        "reachable_no_power_keywords": "No active signal",
        "unavailable": "Signal unavailable",
        "disabled": "Disabled",
    }
    if status in labels:
        return labels[status]
    return status.replace("_", " ").title()


def lpea_active_source_meaning() -> str:
    return "Active source match means a monitored LPEA active/update source currently contains fire, outage, PSPS, or power-interruption keywords. It is a watch cue for review, not a confirmed outage or shutoff notice."


def lpea_summary_note(lpea: Dict[str, Any]) -> str:
    status = lpea.get("status", "unknown")
    if status == "active_keyword_match":
        groups = lpea.get("active_signal_groups") or group_lpea_signal_hits(lpea.get("active_hits", []))
        if groups:
            first_group = groups[0]
            return f"{first_group.get('name', 'LPEA signal')} across {first_group.get('source_count', 1)} source{'s' if first_group.get('source_count', 1) != 1 else ''}. Review source links before treating as a confirmed outage or PSPS notice."
        return "Keywords found in active/update sources. Review source links before treating as a confirmed outage or PSPS notice."
    if status == "reference_keyword_match":
        return "Standing LPEA safety pages mention outage or fire-safety language; no active update source matched."
    if status == "reachable_no_power_keywords":
        return "LPEA public sources were reachable and no monitored power-interruption keywords matched."
    return lpea.get("headline", "No LPEA signal detail available.")


def lpea_group_quality(group: Dict[str, Any]) -> Dict[str, str]:
    snippet = group.get("snippet", "").lower()
    names = " ".join(group.get("source_names", [])).lower()
    types = set(group.get("types", []))
    if "outage map" in names:
        return {"label": "Operational source", "class": "quality-operational", "detail": "Live outage-map source; strongest public operational cue."}
    if re.search(r"\b\d{2}/\d{2}/20\d{2}\b", snippet) or "archive" in group.get("name", "").lower():
        return {"label": "Archive/context", "class": "quality-context", "detail": "Useful background, but not current outage intent by itself."}
    if "site-wide lpea banner" in snippet or "red flag warnings are in place" in snippet:
        return {"label": "Current banner", "class": "quality-active", "detail": "Active public-site banner; current watch cue."}
    if "official_social" in types:
        return {"label": "Social/update cue", "class": "quality-active", "detail": "Public social/update source; review timing and wording."}
    if types & {"official_updates", "outage_map"}:
        return {"label": "Active/update cue", "class": "quality-active", "detail": "Active monitored source; review link for specificity."}
    return {"label": "Reference/context", "class": "quality-context", "detail": "Reference safety material; should not move prediction alone."}


def lpea_evidence_quality(lpea: Dict[str, Any]) -> Dict[str, Any]:
    active_groups = lpea.get("active_signal_groups") or group_lpea_signal_hits(lpea.get("active_hits", []))
    annotated = []
    counts = {"operational": 0, "active": 0, "context": 0}
    for group in active_groups:
        quality = lpea_group_quality(group)
        annotated.append({**group, "quality": quality})
        if quality["class"] == "quality-operational":
            counts["operational"] += 1
        elif quality["class"] == "quality-active":
            counts["active"] += 1
        else:
            counts["context"] += 1
    reference_count = len(lpea.get("reference_hits", []))
    summary = (
        f"{counts['operational']} operational, {counts['active']} active/update, "
        f"{counts['context']} archive/context, {reference_count} reference source match{'es' if reference_count != 1 else ''}."
    )
    return {
        "summary": summary,
        "counts": counts,
        "reference_match_count": reference_count,
        "groups": annotated,
    }


def find_named_entry(entries: Iterable[Dict[str, Any]], preferred_name: str) -> Optional[Dict[str, Any]]:
    preferred = preferred_name.lower()
    fallback_prefix = preferred.split()[0]
    for entry in entries:
        name = str(entry.get("name", "")).lower()
        if name == preferred:
            return entry
    for entry in entries:
        name = str(entry.get("name", "")).lower()
        if preferred in name or name.startswith(fallback_prefix):
            return entry
    return None


def psps_level_as_tier(level: str) -> str:
    return {
        "CONFIRMED": "HIGH",
        "LIKELY": "HIGH",
        "WATCH": "CONCERN",
        "ELEVATED": "ELEVATED",
        "LOW": "GREEN",
    }.get(level, "GREEN")


def pagosa_outlook_card(report: Dict[str, Any]) -> Dict[str, Any]:
    place_name = "Pagosa Springs"
    current_day = report.get("days", [{}])[0] if report.get("days") else {}
    date_text = format_display_date(current_day["date"]) if current_day.get("date") else "today"
    pagosa_weather = find_named_entry(current_day.get("points", []), place_name) or {}

    psps_days = report.get("psps", {}).get("days", [])
    current_psps_day = next((day for day in psps_days if day.get("date") == current_day.get("date")), {})
    pagosa_psps = (
        find_named_entry(current_psps_day.get("location_scores", []), place_name)
        or find_named_entry(current_psps_day.get("driver_locations", []), place_name)
        or {}
    )

    weather_tier = pagosa_weather.get("tier") or current_day.get("tier", "UNKNOWN")
    psps_level = pagosa_psps.get("level") or current_psps_day.get("level", "UNKNOWN")
    psps_score = pagosa_psps.get("score") or current_psps_day.get("weather_score")

    note_parts = [f"{date_text}: weather {weather_tier}"]
    if pagosa_weather:
        note_parts.append(
            f"RH {format_metric(pagosa_weather.get('min_rh_percent'), '%')}, wind {format_metric(pagosa_weather.get('max_usable_wind_mph'), ' mph')}"
        )
    if psps_score is not None:
        note_parts.append(f"Pagosa PSPS score {psps_score}/100")

    display_tier = max_tier(weather_tier if weather_tier in TIER_RANK else "GREEN", psps_level_as_tier(psps_level))
    return {
        "label": f"{place_name} today",
        "value": f"PSPS {psps_level}",
        "class": tier_badge_class(display_tier),
        "note": "; ".join(note_parts) + ".",
    }


def short_location_name(name: str) -> str:
    return name.split(" / ")[0]


def build_area_outlook(report: Dict[str, Any]) -> List[Dict[str, Any]]:
    psps_days = report.get("psps", {}).get("days", [])
    sample_names = [point.get("name") for point in report.get("points", []) if point.get("name")]
    if not sample_names:
        sample_names = sorted({score.get("name") for day in psps_days for score in day.get("location_scores", []) if score.get("name")})
    cards = []
    for name in sample_names:
        scores = []
        for day in psps_days:
            score = find_named_entry(day.get("location_scores", []), name)
            if score:
                scores.append({**score, "date": day.get("date")})
        if not scores:
            continue
        today = scores[0]
        peak = max(scores, key=lambda item: (PSPS_RANK.get(item.get("level", "LOW"), 0), safe_int(item.get("score"))))
        cards.append(
            {
                "name": name,
                "short_name": short_location_name(name),
                "today": today,
                "peak": peak,
                "sort_score": safe_int(peak.get("score")),
                "sort_rank": PSPS_RANK.get(peak.get("level", "LOW"), 0),
            }
        )
    cards.sort(key=lambda item: (item["sort_rank"], item["sort_score"]), reverse=True)
    return cards


def render_lpea_markdown(report: Dict[str, Any]) -> List[str]:
    lpea = report.get("lpea", {})
    lines = [
        "## LPEA Power Signal",
        "",
        f"- Status: `{lpea.get('status', 'unknown')}` - {lpea.get('headline', 'No LPEA headline available.')}",
        f"- Meaning: {lpea_active_source_meaning()}",
        f"- Source coverage: {lpea.get('monitored_source_count', 0)} sources; {lpea.get('social_status', 'social sources not configured')}",
        f"- Evidence quality: {lpea.get('evidence_quality', {}).get('summary', 'Evidence quality not classified.')}",
    ]
    active_hits = lpea.get("active_hits", [])
    reference_hits = lpea.get("reference_hits", [])
    active_signal_groups = lpea.get("active_signal_groups") or group_lpea_signal_hits(active_hits)
    if active_hits:
        lines.append("- Active/update source pages with matches: " + "; ".join(lpea_hit_summary(hit) for hit in active_hits[:5]))
        if active_signal_groups:
            lines.append("- Distinct active/update signals: " + "; ".join(lpea_signal_group_summary(group) for group in active_signal_groups[:5]))
            lines.append(f"- Example signal: {active_signal_groups[0].get('snippet', 'No snippet available.')}")
    else:
        lines.append("- Active/update hits: None")
    if reference_hits:
        lines.append(
            "- Reference/context hits: "
            + "; ".join(
                f"[{hit.get('name', 'Unknown source')}]({hit.get('url')})" if hit.get("url") else hit.get("name", "Unknown source")
                for hit in reference_hits[:5]
            )
        )
    return lines


def render_official_alerts_markdown(report: Dict[str, Any]) -> List[str]:
    alerts = report.get("official_alerts", {}).get("alerts", [])
    zones = ", ".join(report.get("official_alerts", {}).get("monitored_zones", [])) or report.get("fire_weather_zone", "COZ295")
    lines = [
        "## Official Weather Alerts",
        "",
        f"- Monitored NWS zones: {zones}",
    ]
    if not alerts:
        lines.append("- No active official NWS Red Flag / Fire Weather or related weather alerts found for monitored zones.")
        return lines
    for alert in alerts:
        label = alert.get("event", "NWS alert")
        if alert.get("url"):
            label = f"[{label}]({alert['url']})"
        timing = " to ".join(value for value in (alert.get("effective"), alert.get("ends")) if value)
        timing_text = f"; {timing}" if timing else ""
        zones_text = f"; zones {', '.join(alert.get('zones', []))}" if alert.get("zones") else ""
        headline = alert.get("headline") or alert.get("areaDesc") or "No headline provided."
        lines.append(f"- {label}: {headline}{timing_text}{zones_text}")
    return lines


def render_psps_markdown(report: Dict[str, Any]) -> List[str]:
    psps = report.get("psps", {})
    likely_dates = collect_psps_dates_by_level(psps.get("days", []), "LIKELY")
    watch_dates = collect_psps_dates_by_level(psps.get("days", []), "WATCH")
    outage_url = lpea_outage_url(report)
    psps_url = lpea_psps_url(report)
    outage_map_url = lpea_outage_map_url(report)
    lines = [
        "## PSPS Likelihood",
        "",
        f"- **PSPS means Public Safety Power Shutoff:** a planned, safety-related power shutoff LPEA may use during dangerous fire-weather conditions to reduce wildfire ignition risk. See [LPEA PSPS guidance]({psps_url}) and the [LPEA outage center]({outage_url}); if power is out, also check the [LPEA outage map]({outage_map_url}).",
        f"- Overall: **{psps.get('overall_level', 'UNKNOWN')}** - {psps.get('headline', 'No PSPS forecast available.')}",
        f"- Likely PSPS watch dates: {format_date_list(likely_dates)}",
        f"- PSPS watch dates: {format_date_list(watch_dates)}",
        f"- LPEA signal basis: {psps.get('lpea_signal', {}).get('reason', 'No LPEA signal basis available.')}",
        f"- Note: {psps.get('disclaimer', 'This is not an official shutoff notice.')}",
        "",
        "| Date | PSPS likelihood | Driver locations | Weather basis |",
        "| --- | --- | --- | --- |",
    ]
    for day in psps.get("days", []):
        drivers = "; ".join(
            f"{location['name']} ({location['level']} {location['score']}/100)"
            for location in day.get("driver_locations", [])[:4]
        ) or "No standout sampled location."
        lines.append(
            f"| {format_display_date(day['date'])} | {day['level']} | {drivers.replace('|', '/')} | {day['reasons'][0].replace('|', '/')} |"
        )
    return lines


def render_area_outlook_markdown(report: Dict[str, Any]) -> List[str]:
    cards = build_area_outlook(report)
    if not cards:
        return ["## Area-Specific Outlook", "", "No area-specific PSPS scores available."]
    lines = [
        "## Area-Specific Outlook",
        "",
        "| Area | Today | Peak this run | Highest-risk window |",
        "| --- | --- | --- | --- |",
    ]
    for card in cards:
        today = card["today"]
        peak = card["peak"]
        lines.append(
            f"| {card['short_name']} | {today.get('level', 'LOW')} {today.get('score', 'n/a')}/100 | {format_display_date(peak.get('date'))}: {peak.get('level', 'LOW')} {peak.get('score', 'n/a')}/100 | {peak.get('highest_risk_window', 'n/a')} |"
        )
    return lines


def render_calibration_markdown(report: Dict[str, Any]) -> List[str]:
    calibration = report.get("calibration", {})
    return [
        "## Forecast Calibration",
        "",
        f"- Summary: {calibration.get('summary', 'No calibration summary available.')}",
        f"- Confirmed PSPS events logged: {calibration.get('confirmed_event_count', 0)}",
        f"- Candidate/unconfirmed events logged: {calibration.get('candidate_event_count', 0)}",
        f"- WATCH/LIKELY false-watch past days: {calibration.get('false_watch_day_count', 0)}",
        f"- Pending WATCH/LIKELY dates in current forecast: {format_date_list(calibration.get('pending_watch_dates', []))}",
        f"- Event log: `{calibration.get('event_log_path', 'psps_events.json')}`",
        f"- Forecast history: `{calibration.get('forecast_history_path', 'forecast_history.csv')}`",
    ]


def render_fire_posture_markdown(report: Dict[str, Any]) -> List[str]:
    posture = report.get("fire_posture", {})
    lines = [
        "## Fire Posture + Restrictions",
        "",
        f"- Summary: {posture.get('headline', 'Fire-posture check not available.')}",
        f"- Max restriction stage detected: {posture.get('max_restriction_stage', 'UNKNOWN')}",
        f"- Max fire danger detected: {posture.get('max_fire_danger', 'UNKNOWN')}",
        f"- Sources reachable: {posture.get('reachable_source_count', 0)}/{posture.get('source_count', 0)}",
        f"- Note: {posture.get('disclaimer', 'Verify directly with the responsible jurisdiction.')}",
        "",
        "| Jurisdiction | Restrictions | Fire danger | Source |",
        "| --- | --- | --- | --- |",
    ]
    for source in posture.get("sources", []):
        label = source.get("name", "Unknown source")
        if source.get("url"):
            label = f"[{label}]({source['url']})"
        lines.append(
            f"| {source.get('area', source.get('name', 'Unknown'))} | {source.get('restriction_stage', 'UNKNOWN')} | {source.get('fire_danger', 'UNKNOWN')} | {label} |"
        )
    return lines


def render_markdown(report: Dict[str, Any]) -> str:
    high_dates = collect_dates_by_tier(report["days"], "HIGH")
    concern_dates = collect_dates_by_tier(report["days"], "CONCERN")
    elevated_dates = collect_dates_by_tier(report["days"], "ELEVATED")
    likely_psps_dates = collect_psps_dates_by_level(report.get("psps", {}).get("days", []), "LIKELY")
    watch_psps_dates = collect_psps_dates_by_level(report.get("psps", {}).get("days", []), "WATCH")
    lines = [
        "# Archuleta Red Flag Risk Monitor",
        "",
        f"Generated: {format_generated_at(report)}",
        f"Next update: {format_next_update_at(report)}",
        f"Date/time basis: {local_time_context(report)}",
        f"> **{UNOFFICIAL_MONITOR_LABEL}:** {UNOFFICIAL_MONITOR_DISCLAIMER}",
        "",
        "## At A Glance",
        "",
        f"- Overall tier: **{report['overall_tier']}**",
        f"- PSPS likelihood: **{report.get('psps', {}).get('overall_level', 'UNKNOWN')}**",
        f"- PSPS likely dates: {format_date_list(likely_psps_dates)}",
        f"- PSPS watch dates: {format_date_list(watch_psps_dates)}",
        f"- Monitor heads-up recommended: **{'YES' if report['notify_recommended'] else 'NO'}** - {monitor_heads_up_note(report)}",
        f"- HIGH dates: {format_date_list(high_dates)}",
        f"- CONCERN dates: {format_date_list(concern_dates)}",
        f"- ELEVATED dates: {format_date_list(elevated_dates)}",
        f"- {official_fire_alert_label(report)}: {report['official_alerts']['fire_alert_count']}",
        f"- LPEA signal: `{report['lpea']['status']}` - {report['lpea']['headline']}",
        f"- LPEA source coverage: {report['lpea'].get('monitored_source_count', 0)} sources; {report['lpea'].get('social_status', 'social sources not configured')}",
        f"- NWS discussion: {report['discussion']['headline']}",
        "",
        *render_psps_markdown(report),
        "",
        *render_area_outlook_markdown(report),
        "",
        *render_fire_posture_markdown(report),
        "",
        *render_calibration_markdown(report),
        "",
        *render_official_alerts_markdown(report),
        "",
        *render_lpea_markdown(report),
        "",
        f"**{UNOFFICIAL_MONITOR_LABEL}:** {UNOFFICIAL_MONITOR_DISCLAIMER}",
        "",
        "## Next 7 Days",
        "",
        "| Date | Tier | Main reason | Worst sampled metrics |",
        "| --- | --- | --- | --- |",
    ]
    for day in report["days"]:
        reason = day["reasons"][0].replace("|", "/")
        point_metrics = []
        for point in day["points"]:
            if point["tier"] == day["tier"] or point["tier"] != "GREEN":
                point_metrics.append(
                    f"{point['name']}: RH {format_metric(point['min_rh_percent'], '%')}, wind/gust {format_metric(point['max_usable_wind_mph'], ' mph')}, thunder {format_metric(point['max_thunder_percent'], '%')}"
                )
        metrics = "<br>".join(point_metrics[:3]) if point_metrics else "No standout sampled point."
        lines.append(f"| {format_display_date(day['date'])} | {day['tier']} | {reason} | {metrics} |")

    lines.extend(["", "## Sample Point Status", ""])
    for point in report["points"]:
        if point.get("status") == "ok":
            lines.append(
                f"- {point['name']}: {point['fire_weather_zone']} ({point['zone_status']}), forecast zone {point['forecast_zone']}, county zone {point['county_zone']}"
            )
        else:
            lines.append(f"- {point['name']}: unavailable ({point.get('error', 'unknown error')})")

    return "\n".join(lines) + "\n"


def render_email_text(report: Dict[str, Any]) -> str:
    lines = [
        "Archuleta Red Flag Risk Monitor",
        f"Generated: {format_generated_at(report)}",
        f"Next update: {format_next_update_at(report)}",
        f"Date/time basis: {local_time_context(report)}",
        f"{UNOFFICIAL_MONITOR_LABEL}: {UNOFFICIAL_MONITOR_DISCLAIMER}",
        "",
        *build_brief_summary(report),
        "",
        "Next 7 days:",
    ]
    for day in report["days"]:
        lines.append(f"- {format_display_date(day['date'])}: {day['tier']} - {day['reasons'][0]}")
    return "\n".join(lines) + "\n"


def render_html(report: Dict[str, Any]) -> str:
    high_dates = collect_dates_by_tier(report["days"], "HIGH")
    concern_dates = collect_dates_by_tier(report["days"], "CONCERN")
    elevated_dates = collect_dates_by_tier(report["days"], "ELEVATED")
    psps = report.get("psps", {})
    likely_psps_dates = collect_psps_dates_by_level(psps.get("days", []), "LIKELY")
    watch_psps_dates = collect_psps_dates_by_level(psps.get("days", []), "WATCH")
    outage_url = lpea_outage_url(report)
    psps_url = lpea_psps_url(report)
    outage_map_url = lpea_outage_map_url(report)

    summary_cards = [
        {"label": "Overall tier", "value": report["overall_tier"], "class": tier_badge_class(report["overall_tier"])},
        {"label": "PSPS likelihood", "value": psps.get("overall_level", "UNKNOWN"), "class": f"psps-{psps.get('overall_level', 'unknown').lower()}"},
        pagosa_outlook_card(report),
        {"label": "Likely PSPS dates", "value": format_date_list(likely_psps_dates), "class": "", "dates": likely_psps_dates},
        {
            "label": "Send monitor heads-up?",
            "value": "YES" if report["notify_recommended"] else "NO",
            "class": "tier-high" if report["notify_recommended"] else "tier-green",
            "note": monitor_heads_up_note(report),
        },
        {"label": "HIGH dates", "value": format_date_list(high_dates), "class": "", "dates": high_dates},
        {"label": "CONCERN dates", "value": format_date_list(concern_dates), "class": "", "dates": concern_dates},
        {
            "label": "LPEA signal",
            "value": lpea_status_label(report["lpea"].get("status", "unknown")),
            "class": "signal-watch" if report["lpea"].get("status") in ("active_keyword_match", "reference_keyword_match") else "",
            "note": lpea_summary_note(report["lpea"]),
        },
    ]

    day_tiles = []
    for day in report["days"]:
        day_name, month_day = split_display_date(day["date"])
        strongest_points = [point for point in day["points"] if point["tier"] != "GREEN"] or day["points"][:1]
        metrics = []
        for point in strongest_points[:2]:
            metrics.append(
                f"{escape_html(point['name'])}: RH {escape_html(format_metric(point['min_rh_percent'], '%'))} / wind {escape_html(format_metric(point['max_usable_wind_mph'], ' mph'))}"
            )
        metrics_html = "".join(f"<li>{item}</li>" for item in metrics) or "<li>No standout sampled point.</li>"
        day_tiles.append(
            f"""
            <article class="day-card {tier_badge_class(day['tier'])}">
              <div class="day-card-top">
                <div>
                  <p class="eyebrow">{escape_html(day_name)}</p>
                  <p class="day-date">{escape_html(month_day)}</p>
                  <h3>{escape_html(day['tier'])}</h3>
                </div>
                <span class="chip {tier_badge_class(day['tier'])}">{escape_html(day['tier'])}</span>
              </div>
              <p class="reason">{escape_html(day['reasons'][0])}</p>
              <ul class="metrics">{metrics_html}</ul>
            </article>
            """
        )

    point_rows = []
    for point in report["points"]:
        if point.get("status") == "ok":
            status = f"{point['fire_weather_zone']} ({point['zone_status']})"
            detail = f"forecast zone {point['forecast_zone']}, county zone {point['county_zone']}"
        else:
            status = "unavailable"
            detail = point.get("error", "unknown error")
        point_rows.append(
            f"""
            <tr>
              <td>{escape_html(point['name'])}</td>
              <td>{escape_html(status)}</td>
              <td>{escape_html(detail)}</td>
            </tr>
            """
        )

    summary_cards_html_parts = []
    for card in summary_cards:
        if card.get("dates"):
            date_pills = []
            for date_text in card["dates"]:
                day_name, month_day = split_display_date(date_text)
                date_pills.append(
                    f'<span class="date-pill"><strong>{escape_html(day_name)}</strong><span>{escape_html(month_day)}</span></span>'
                )
            value_html = f'<div class="date-pills">{"".join(date_pills)}</div>'
        else:
            value_html = f'<p class="summary-value {card["class"]}">{escape_html(card["value"])}</p>'
            if card.get("note"):
                value_html += f'<p class="summary-note">{escape_html(card["note"])}</p>'
        summary_cards_html_parts.append(
            f"""
            <section class="summary-card">
              <p class="eyebrow">{escape_html(card['label'])}</p>
              {value_html}
            </section>
            """
        )
    summary_cards_html = "".join(summary_cards_html_parts)

    psps_days_by_date = {day.get("date"): day for day in psps.get("days", [])}
    combined_outlook_parts = []
    for weather_day in report["days"]:
        psps_day = psps_days_by_date.get(weather_day["date"], {})
        day_name, month_day = split_display_date(weather_day["date"])
        psps_level = psps_day.get("level", "LOW")
        trend = psps_day.get("trend", {}).get("label", "Trend pending")
        driver_names = ", ".join(
            location["name"].split(" / ")[0]
            for location in psps_day.get("driver_locations", [])[:2]
        )
        if not driver_names:
            driver_names = "No standout location"
        combined_outlook_parts.append(
            f"""
            <div class="outlook-segment psps-{escape_html(psps_level.lower())}">
              <span>{escape_html(day_name)}</span>
              <small>{escape_html(month_day)}</small>
              <strong>PSPS {escape_html(psps_level)}</strong>
              <em>Weather {escape_html(weather_day['tier'])}</em>
              <em>{escape_html(trend)}</em>
              <b>{escape_html(driver_names)}</b>
            </div>
            """
        )
    combined_outlook_html = "".join(combined_outlook_parts)
    psps_location_cards_html = "".join(
        f"""
        <article class="psps-location-card">
          <div>
            <p class="eyebrow">{escape_html(format_display_date(day['date']))}</p>
            <h3>{escape_html(day['level'])}</h3>
          </div>
          <p class="weather-score">Weather score {escape_html(day.get('weather_score', 'n/a'))}/100</p>
          <p class="source-meta">{escape_html(day.get('trend', {}).get('summary', 'Trend not available.'))}</p>
          <ul>
            {''.join(f'<li><strong>{escape_html(location["name"])}</strong>: {escape_html(location["level"])} {escape_html(location["score"])}/100. {escape_html(location["summary"])} Risk window: {escape_html(location.get("highest_risk_window", "n/a"))}</li>' for location in day.get("driver_locations", [])[:5])}
          </ul>
        </article>
        """
        for day in psps.get("days", [])
        if day.get("level") in ("WATCH", "LIKELY", "CONFIRMED")
    )
    psps_detail_day_count = sum(1 for day in psps.get("days", []) if day.get("level") in ("WATCH", "LIKELY", "CONFIRMED"))
    area_cards_html = "".join(
        f"""
        <article class="area-card psps-{escape_html(card['today'].get('level', 'low').lower())}">
          <div class="area-card-top">
            <div>
              <p class="eyebrow">{escape_html(card['short_name'])}</p>
              <h3>{escape_html(card['today'].get('level', 'LOW'))}</h3>
            </div>
            <span class="score-badge">{escape_html(str(card['today'].get('score', 'n/a')))}/100</span>
          </div>
          <p class="source-meta">Today: {escape_html(card['today'].get('summary', 'No score summary available.'))}</p>
          <p class="source-meta">Peak: {escape_html(format_display_date(card['peak'].get('date')))} at {escape_html(card['peak'].get('level', 'LOW'))} {escape_html(str(card['peak'].get('score', 'n/a')))}/100.</p>
          <p class="risk-window">Highest-risk window: {escape_html(card['peak'].get('highest_risk_window', 'n/a'))}</p>
        </article>
        """
        for card in build_area_outlook(report)
    ) or '<p class="empty-state">No area-specific PSPS scores available.</p>'
    calibration = report.get("calibration", {})
    calibration_cards_html = f"""
        <article class="calibration-card">
          <p class="eyebrow">Confirmed events</p>
          <strong>{escape_html(str(calibration.get('confirmed_event_count', 0)))}</strong>
          <span>logged PSPS events</span>
        </article>
        <article class="calibration-card">
          <p class="eyebrow">Hit rate</p>
          <strong>{escape_html(str(calibration.get('hit_rate_percent')) + '%' if calibration.get('hit_rate_percent') is not None else 'Pending')}</strong>
          <span>WATCH+ before confirmed PSPS</span>
        </article>
        <article class="calibration-card">
          <p class="eyebrow">False-watch days</p>
          <strong>{escape_html(str(calibration.get('false_watch_day_count', 0)))}</strong>
          <span>past WATCH/LIKELY days without logged PSPS</span>
        </article>
        <article class="calibration-card">
          <p class="eyebrow">Pending</p>
          <strong>{escape_html(str(len(calibration.get('pending_watch_dates', []))))}</strong>
          <span>current WATCH/LIKELY dates</span>
        </article>
    """
    fire_posture = report.get("fire_posture", {})
    fire_posture_cards_html = "".join(
        f"""
        <article class="fire-posture-card">
          <p class="source-name">{linked_text_html(source.get('name', 'Unknown source'), source.get('url'))}</p>
          <p class="source-meta">{escape_html(source.get('area', 'Unknown area'))} · {escape_html(source.get('jurisdiction_type', 'official'))}</p>
          <div class="fire-chip-row">
            <span class="fire-chip {escape_html(fire_status_class(source.get('restriction_stage', 'unknown')))}">Restrictions: {escape_html(source.get('restriction_stage', 'UNKNOWN'))}</span>
            <span class="fire-chip {escape_html(fire_status_class(source.get('fire_danger', 'unknown')))}">Danger: {escape_html(source.get('fire_danger', 'UNKNOWN'))}</span>
          </div>
          <p class="source-snippet">{escape_html((source.get('snippets') or ['No specific fire posture snippet found.'])[0])}</p>
        </article>
        """
        for source in fire_posture.get("sources", [])
    ) or '<p class="empty-state">No fire-posture sources configured.</p>'
    lpea = report.get("lpea", {})
    evidence_quality = lpea.get("evidence_quality") or lpea_evidence_quality(lpea)
    active_signal_groups = evidence_quality.get("groups") or lpea.get("active_signal_groups") or group_lpea_signal_hits(lpea.get("active_hits", []))
    active_hits_html = "".join(
        f"""
        <article class="source-card">
          <p class="source-name">{linked_text_html(group.get('name', 'LPEA signal'), group.get('primary_url'))}</p>
          <p class="source-meta">{escape_html(str(group.get('source_count', 1)))} source{'s' if group.get('source_count', 1) != 1 else ''}: {source_group_links_html(group)}</p>
          <p class="quality-pill {escape_html(group.get('quality', {}).get('class', 'quality-context'))}">{escape_html(group.get('quality', {}).get('label', 'Evidence cue'))}</p>
          <p class="source-tags">{escape_html(', '.join(group.get('matches', [])[:6]))}</p>
          <p class="source-snippet">{escape_html(group.get('snippet', 'No snippet available.'))}</p>
        </article>
        """
        for group in active_signal_groups[:4]
    ) or '<p class="empty-state">No active/update LPEA source matched power-interruption keywords.</p>'
    reference_hits_html = "".join(
        f'<span class="reference-pill">{linked_text_html(hit.get("name", "Unknown source"), hit.get("url"))}</span>'
        for hit in lpea.get("reference_hits", [])[:6]
    ) or '<span class="reference-pill">No reference hits</span>'
    alert_cards_html = "".join(
        f"""
        <article class="alert-card">
          <p class="source-name">{linked_text_html(alert.get('event', 'NWS alert'), alert.get('url'))}</p>
          <p class="source-meta">{escape_html(alert.get('headline') or alert.get('areaDesc') or 'No headline provided.')}</p>
          <p class="alert-meta">{escape_html(' to '.join(value for value in (alert.get('effective'), alert.get('ends')) if value) or 'Timing unavailable')}</p>
          <p class="source-tags">{escape_html(', '.join(alert.get('zones', [])[:8]))}</p>
        </article>
        """
        for alert in report.get("official_alerts", {}).get("alerts", [])[:6]
    ) or '<p class="empty-state">No active official NWS Red Flag / Fire Weather or related weather alerts found for monitored zones.</p>'
    monitored_zone_text = ", ".join(report.get("official_alerts", {}).get("monitored_zones", [])) or report.get("fire_weather_zone", "COZ295")
    official_alert_count = int(report.get("official_alerts", {}).get("fire_alert_count", 0))
    official_alert_count_label = f"{official_alert_count} active" if official_alert_count != 1 else "1 active"

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Archuleta Red Flag Risk Monitor</title>
  <style>
    :root {{
      --bg: #f4efe5;
      --panel: rgba(255, 250, 242, 0.88);
      --ink: #1d2a2a;
      --muted: #5c6766;
      --line: rgba(29, 42, 42, 0.12);
      --green: #3c7a44;
      --elevated: #b88418;
      --concern: #cb5a1b;
      --high: #a72f23;
      --shadow: 0 16px 40px rgba(58, 48, 31, 0.12);
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: Georgia, "Times New Roman", serif;
      color: var(--ink);
      background:
        radial-gradient(circle at top left, rgba(203, 90, 27, 0.18), transparent 32%),
        radial-gradient(circle at top right, rgba(167, 47, 35, 0.16), transparent 28%),
        linear-gradient(180deg, #f8f2e8 0%, var(--bg) 100%);
    }}
    .wrap {{
      max-width: 1180px;
      margin: 0 auto;
      padding: 32px 20px 48px;
    }}
    .hero {{
      background: linear-gradient(135deg, rgba(255,255,255,0.86), rgba(255,245,232,0.92));
      border: 1px solid var(--line);
      border-radius: 28px;
      box-shadow: var(--shadow);
      padding: 28px;
    }}
    .hero-top {{
      display: flex;
      justify-content: space-between;
      gap: 16px;
      align-items: start;
      flex-wrap: wrap;
    }}
    h1, h2, h3, strong {{
      font-family: "Avenir Next Condensed", "Franklin Gothic Medium", "Arial Narrow", sans-serif;
      letter-spacing: 0.02em;
      margin: 0;
    }}
    h1 {{
      font-size: clamp(2.2rem, 5vw, 4.2rem);
      line-height: 0.95;
      text-transform: uppercase;
    }}
    h2 {{
      font-size: 1.5rem;
      margin-bottom: 14px;
      text-transform: uppercase;
    }}
    h3 {{
      font-size: 1.4rem;
      text-transform: uppercase;
    }}
    .eyebrow {{
      margin: 0 0 8px;
      font-size: 0.78rem;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      color: var(--muted);
    }}
    .hero-note {{
      max-width: 52rem;
      margin: 16px 0 0;
      font-size: 1.03rem;
      color: var(--muted);
    }}
    .official-warning {{
      max-width: 58rem;
      margin: 18px 0 0;
      padding: 14px 16px;
      border: 2px solid rgba(167, 47, 35, 0.32);
      border-radius: 16px;
      background: rgba(255, 238, 230, 0.92);
      color: #5b2209;
      line-height: 1.35;
      box-shadow: 0 10px 24px rgba(167, 47, 35, 0.1);
    }}
    .official-warning strong {{
      display: block;
      margin-bottom: 4px;
      font-size: 0.9rem;
      letter-spacing: 0.14em;
      text-transform: uppercase;
    }}
    .time-note {{
      margin: 10px 0 0;
      font-family: "Avenir Next Condensed", "Franklin Gothic Medium", "Arial Narrow", sans-serif;
      font-size: 0.86rem;
      font-weight: 800;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: #344241;
    }}
    .next-update-note {{
      display: inline-flex;
      margin: 12px 0 0;
      padding: 8px 11px;
      border-radius: 10px;
      background: rgba(29, 42, 42, 0.07);
      color: var(--ink);
      font-family: "Avenir Next Condensed", "Franklin Gothic Medium", "Arial Narrow", sans-serif;
      font-size: 0.94rem;
      font-weight: 800;
      letter-spacing: 0.04em;
      text-transform: uppercase;
    }}
    .hero-alert-panel {{
      margin-top: 16px;
      padding: 14px 16px;
      border: 1px solid rgba(29, 42, 42, 0.12);
      border-radius: 18px;
      background: rgba(29, 42, 42, 0.045);
    }}
    .hero-alert-head {{
      display: flex;
      justify-content: space-between;
      gap: 12px;
      align-items: flex-start;
      flex-wrap: wrap;
    }}
    .hero-alert-panel h2 {{
      margin-bottom: 0;
      font-size: 1.1rem;
    }}
    .hero-alert-panel .footer-note {{
      margin: 6px 0 0;
      font-size: 0.94rem;
    }}
    .alert-count-chip {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      min-width: 74px;
      padding: 7px 10px;
      border-radius: 999px;
      background: rgba(255, 255, 255, 0.78);
      color: #344241;
      font-family: "Avenir Next Condensed", "Franklin Gothic Medium", "Arial Narrow", sans-serif;
      font-weight: 900;
      letter-spacing: 0.06em;
      text-transform: uppercase;
    }}
    .chip {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      min-width: 110px;
      padding: 10px 14px;
      border-radius: 999px;
      color: #fff;
      font-family: "Avenir Next Condensed", "Franklin Gothic Medium", "Arial Narrow", sans-serif;
      font-size: 0.95rem;
      letter-spacing: 0.08em;
      text-transform: uppercase;
    }}
    .chip.tier-green,
    .risk-segment.tier-green,
    .summary-value.tier-green {{ background: var(--green); color: #fff; }}
    .chip.tier-elevated,
    .risk-segment.tier-elevated,
    .summary-value.tier-elevated {{ background: var(--elevated); color: #1f1700; }}
    .chip.tier-concern,
    .risk-segment.tier-concern,
    .summary-value.tier-concern {{ background: var(--concern); color: #fff; }}
    .chip.tier-high,
    .risk-segment.tier-high,
    .summary-value.tier-high {{ background: var(--high); color: #fff; }}
    .summary-value.psps-low,
    .outlook-segment.psps-low,
    .psps-segment.psps-low {{ background: var(--green); color: #fff; }}
    .summary-value.psps-elevated,
    .outlook-segment.psps-elevated,
    .psps-segment.psps-elevated {{ background: var(--elevated); color: #1f1700; }}
    .summary-value.psps-watch,
    .outlook-segment.psps-watch,
    .psps-segment.psps-watch {{ background: var(--concern); color: #fff; }}
    .summary-value.psps-likely,
    .outlook-segment.psps-likely,
    .psps-segment.psps-likely,
    .summary-value.psps-confirmed,
    .outlook-segment.psps-confirmed,
    .psps-segment.psps-confirmed {{ background: var(--high); color: #fff; }}
    .summary-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 14px;
      margin-top: 24px;
      align-items: start;
    }}
    .summary-card, .section-panel, .day-card {{
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 22px;
      box-shadow: var(--shadow);
    }}
    .summary-card {{
      padding: 18px;
      min-height: 0;
    }}
    .summary-value {{
      margin: 0;
      font-size: 1.15rem;
      line-height: 1.3;
      font-weight: 700;
    }}
    .summary-note {{
      margin: 10px 0 0;
      max-width: 24rem;
      color: var(--muted);
      font-size: 0.94rem;
      line-height: 1.35;
    }}
    .summary-value.signal-watch {{
      display: inline-block;
      padding: 6px 10px;
      border-radius: 12px;
      background: rgba(203, 90, 27, 0.14);
      color: #5b2209;
      font-family: "Avenir Next Condensed", "Franklin Gothic Medium", "Arial Narrow", sans-serif;
      font-size: 1rem;
      font-weight: 900;
      letter-spacing: 0.04em;
      text-transform: uppercase;
    }}
    .date-pills {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-top: 2px;
    }}
    .date-pill {{
      display: inline-flex;
      align-items: baseline;
      gap: 7px;
      padding: 8px 10px;
      border-radius: 12px;
      background: rgba(29, 42, 42, 0.06);
      color: var(--ink);
      line-height: 1;
      white-space: nowrap;
    }}
    .date-pill strong {{
      font-size: 0.88rem;
      text-transform: uppercase;
    }}
    .date-pill span {{
      font-size: 0.98rem;
      font-weight: 700;
    }}
    .summary-value.tier-high,
    .summary-value.tier-concern,
    .summary-value.tier-elevated,
    .summary-value.tier-green,
    .summary-value.psps-low,
    .summary-value.psps-elevated,
    .summary-value.psps-watch,
    .summary-value.psps-likely,
    .summary-value.psps-confirmed {{
      display: inline-block;
      padding: 6px 10px;
      border-radius: 12px;
      font-family: "Avenir Next Condensed", "Franklin Gothic Medium", "Arial Narrow", sans-serif;
      font-size: 1rem;
      font-weight: 900;
      letter-spacing: 0.04em;
      text-transform: uppercase;
    }}
    .section-panel {{
      margin-top: 24px;
      padding: 22px;
    }}
    .subsection-heading {{
      margin-top: 18px;
    }}
    .subsection-heading h3 {{
      font-size: 1.15rem;
    }}
    .compact-panel {{
      padding: 0;
      overflow: hidden;
    }}
    .compact-panel .detail-disclosure {{
      margin-top: 0;
      border: 0;
      border-radius: 0;
      background: transparent;
    }}
    .source-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 12px;
      margin-top: 14px;
    }}
    .source-card {{
      border: 1px solid var(--line);
      border-radius: 14px;
      background: rgba(255, 255, 255, 0.58);
      padding: 14px;
    }}
    .source-name {{
      margin: 0 0 4px;
      font-weight: 800;
    }}
    .source-name a,
    .source-meta a,
    .reference-pill a {{
      color: inherit;
      text-decoration-color: rgba(29, 42, 42, 0.32);
      text-underline-offset: 3px;
    }}
    .source-meta {{
      margin: 0 0 10px;
      color: var(--muted);
      font-size: 0.88rem;
    }}
    .alert-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 12px;
      margin-top: 14px;
    }}
    .hero-alert-panel .alert-grid {{
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      margin-top: 12px;
    }}
    .alert-card {{
      border: 1px solid rgba(167, 47, 35, 0.2);
      border-radius: 14px;
      background: rgba(255, 241, 239, 0.7);
      padding: 14px;
    }}
    .alert-meta {{
      margin: 0 0 10px;
      color: #5b2209;
      font-size: 0.9rem;
      font-weight: 800;
    }}
    .source-tags {{
      display: block;
      width: fit-content;
      margin: 0 0 10px;
      padding: 5px 8px;
      border-radius: 999px;
      background: rgba(29, 42, 42, 0.07);
      color: #344241;
      font-family: "Avenir Next Condensed", "Franklin Gothic Medium", "Arial Narrow", sans-serif;
      font-size: 0.78rem;
      font-weight: 800;
      letter-spacing: 0.04em;
      line-height: 1.2;
      text-transform: uppercase;
    }}
    .source-snippet {{
      margin: 0;
      line-height: 1.35;
      color: #344241;
      font-size: 0.94rem;
      display: -webkit-box;
      -webkit-line-clamp: 5;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }}
    .reference-pills {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-top: 12px;
    }}
    .reference-pill {{
      display: inline-flex;
      padding: 7px 9px;
      border-radius: 999px;
      background: rgba(29, 42, 42, 0.07);
      color: #344241;
      font-size: 0.9rem;
      font-weight: 700;
    }}
    .quality-pill {{
      display: inline-flex;
      margin: 0 0 10px;
      padding: 5px 8px;
      border-radius: 999px;
      font-family: "Avenir Next Condensed", "Franklin Gothic Medium", "Arial Narrow", sans-serif;
      font-size: 0.78rem;
      font-weight: 900;
      letter-spacing: 0.05em;
      text-transform: uppercase;
    }}
    .quality-operational {{ background: rgba(60, 122, 68, 0.16); color: #204923; }}
    .quality-active {{ background: rgba(203, 90, 27, 0.16); color: #5b2209; }}
    .quality-context {{ background: rgba(29, 42, 42, 0.08); color: #344241; }}
    .empty-state {{
      margin: 8px 0 0;
      color: var(--muted);
      font-style: italic;
    }}
    .hero-alert-panel .empty-state {{
      margin: 0;
      padding: 10px 12px;
      border-radius: 12px;
      background: rgba(255, 255, 255, 0.62);
    }}
    .risk-strip {{
      display: grid;
      grid-template-columns: repeat(7, minmax(0, 1fr));
      gap: 10px;
      margin-top: 14px;
    }}
    .risk-segment,
    .outlook-segment,
    .psps-segment {{
      border-radius: 18px;
      padding: 14px 10px;
      text-align: center;
      min-height: 118px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      gap: 6px;
      border: 1px solid rgba(255,255,255,0.28);
      box-shadow: inset 0 1px 0 rgba(255,255,255,0.16);
    }}
    .risk-segment span,
    .outlook-segment span,
    .psps-segment span {{
      font-size: 0.8rem;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      opacity: 0.85;
    }}
    .risk-segment small,
    .outlook-segment small,
    .psps-segment small {{
      font-size: 0.92rem;
      font-weight: 700;
      line-height: 1;
    }}
    .risk-segment strong,
    .outlook-segment strong,
    .psps-segment strong {{
      font-size: 1.05rem;
    }}
    .outlook-segment em,
    .outlook-segment b,
    .psps-segment em {{
      font-size: 0.76rem;
      line-height: 1.1;
      font-style: normal;
      opacity: 0.9;
    }}
    .outlook-segment b {{
      font-weight: 800;
    }}
    .psps-location-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 12px;
      margin-top: 16px;
    }}
    .area-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
      gap: 12px;
      margin-top: 14px;
    }}
    .fire-posture-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 12px;
      margin-top: 14px;
    }}
    .fire-posture-card {{
      border: 1px solid var(--line);
      border-radius: 16px;
      background: rgba(255, 255, 255, 0.62);
      padding: 14px;
      box-shadow: var(--shadow);
    }}
    .fire-chip-row {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin: 10px 0;
    }}
    .fire-chip {{
      display: inline-flex;
      padding: 6px 9px;
      border-radius: 999px;
      background: rgba(29, 42, 42, 0.08);
      color: #344241;
      font-family: "Avenir Next Condensed", "Franklin Gothic Medium", "Arial Narrow", sans-serif;
      font-size: 0.82rem;
      font-weight: 900;
      letter-spacing: 0.04em;
      text-transform: uppercase;
    }}
    .fire-stage-1,
    .fire-stage-2,
    .fire-stage-3,
    .fire-restrictions,
    .fire-very-high,
    .fire-extreme {{ background: rgba(203, 90, 27, 0.16); color: #5b2209; }}
    .fire-stage-2,
    .fire-stage-3,
    .fire-extreme {{ background: rgba(167, 47, 35, 0.16); color: #5b2209; }}
    .fire-none,
    .fire-low {{ background: rgba(60, 122, 68, 0.14); color: #204923; }}
    .fire-moderate,
    .fire-high {{ background: rgba(184, 132, 24, 0.16); color: #4b3400; }}
    .area-card {{
      border: 1px solid var(--line);
      border-radius: 16px;
      background: rgba(255, 255, 255, 0.64);
      padding: 14px;
      box-shadow: var(--shadow);
    }}
    .area-card.psps-watch {{ border-left: 7px solid var(--concern); }}
    .area-card.psps-likely,
    .area-card.psps-confirmed {{ border-left: 7px solid var(--high); }}
    .area-card.psps-elevated {{ border-left: 7px solid var(--elevated); }}
    .area-card.psps-low {{ border-left: 7px solid var(--green); }}
    .area-card-top {{
      display: flex;
      justify-content: space-between;
      gap: 10px;
      align-items: flex-start;
    }}
    .score-badge {{
      display: inline-flex;
      padding: 7px 9px;
      border-radius: 999px;
      background: rgba(29, 42, 42, 0.08);
      font-family: "Avenir Next Condensed", "Franklin Gothic Medium", "Arial Narrow", sans-serif;
      font-weight: 900;
      letter-spacing: 0.05em;
    }}
    .risk-window {{
      margin: 10px 0 0;
      padding-top: 10px;
      border-top: 1px solid var(--line);
      color: #344241;
      font-size: 0.92rem;
      font-weight: 800;
    }}
    .calibration-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 12px;
      margin-top: 14px;
    }}
    .calibration-card {{
      border: 1px solid var(--line);
      border-radius: 16px;
      background: rgba(29, 42, 42, 0.045);
      padding: 14px;
    }}
    .calibration-card strong {{
      display: block;
      font-size: 1.55rem;
      line-height: 1;
    }}
    .calibration-card span {{
      display: block;
      margin-top: 6px;
      color: var(--muted);
      font-size: 0.9rem;
      line-height: 1.25;
    }}
    .psps-location-card {{
      border: 1px solid var(--line);
      border-radius: 14px;
      background: rgba(255, 255, 255, 0.62);
      padding: 14px;
    }}
    .psps-location-card h3 {{
      font-size: 1.2rem;
    }}
    .weather-score {{
      margin: 8px 0;
      font-weight: 800;
      color: #344241;
    }}
    .psps-location-card ul {{
      margin: 0;
      padding-left: 18px;
      color: #344241;
      line-height: 1.35;
    }}
    .detail-disclosure {{
      margin-top: 16px;
      border: 1px solid var(--line);
      border-radius: 18px;
      background: rgba(255, 255, 255, 0.54);
      overflow: hidden;
    }}
    .detail-disclosure > summary {{
      cursor: pointer;
      list-style: none;
      padding: 14px 16px;
      color: #344241;
      font-family: "Avenir Next Condensed", "Franklin Gothic Medium", "Arial Narrow", sans-serif;
      font-size: 1rem;
      font-weight: 900;
      letter-spacing: 0.06em;
      text-transform: uppercase;
    }}
    .detail-disclosure > summary::-webkit-details-marker {{
      display: none;
    }}
    .detail-disclosure > summary::after {{
      content: "Show";
      float: right;
      color: var(--muted);
      font-size: 0.82rem;
      letter-spacing: 0.08em;
    }}
    .detail-disclosure[open] > summary {{
      border-bottom: 1px solid var(--line);
    }}
    .detail-disclosure[open] > summary::after {{
      content: "Hide";
    }}
    .detail-disclosure-content {{
      padding: 0 16px 16px;
    }}
    .audit-summary {{
      display: flex;
      justify-content: space-between;
      gap: 14px;
      align-items: center;
      padding: 18px 22px;
    }}
    .audit-summary small {{
      color: var(--muted);
      font-family: Georgia, "Times New Roman", serif;
      font-size: 0.92rem;
      font-weight: 700;
      letter-spacing: 0;
      text-transform: none;
    }}
    .definition-box {{
      margin-top: 14px;
      padding: 14px 16px;
      border: 1px solid rgba(29, 42, 42, 0.12);
      border-radius: 16px;
      background: rgba(29, 42, 42, 0.055);
      color: #344241;
    }}
    .definition-box strong {{
      display: block;
      margin-bottom: 6px;
      font-size: 1.05rem;
      text-transform: uppercase;
    }}
    .definition-box p {{
      margin: 0 0 10px;
      line-height: 1.42;
    }}
    .definition-box p:last-child {{
      margin-bottom: 0;
    }}
    .definition-links {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }}
    .definition-links a {{
      display: inline-flex;
      padding: 7px 10px;
      border-radius: 999px;
      background: rgba(255, 255, 255, 0.76);
      color: #1d2a2a;
      font-family: "Avenir Next Condensed", "Franklin Gothic Medium", "Arial Narrow", sans-serif;
      font-weight: 900;
      letter-spacing: 0.04em;
      text-decoration: none;
      text-transform: uppercase;
    }}
    .days-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 14px;
      margin-top: 14px;
    }}
    .day-card {{
      padding: 18px;
      position: relative;
      overflow: hidden;
      color: var(--ink);
    }}
    .day-card.tier-green {{ border-left: 8px solid var(--green); background: rgba(247, 255, 246, 0.92); }}
    .day-card.tier-elevated {{ border-left: 8px solid var(--elevated); background: rgba(255, 249, 229, 0.94); }}
    .day-card.tier-concern {{ border-left: 8px solid var(--concern); background: rgba(255, 244, 236, 0.94); }}
    .day-card.tier-high {{ border-left: 8px solid var(--high); background: rgba(255, 241, 239, 0.94); }}
    .day-card::after {{
      content: "";
      position: absolute;
      inset: auto -10% -40% auto;
      width: 140px;
      height: 140px;
      background: rgba(255,255,255,0.14);
      border-radius: 50%;
    }}
    .day-card-top {{
      display: flex;
      justify-content: space-between;
      gap: 12px;
      align-items: start;
    }}
    .day-date {{
      margin: -4px 0 8px;
      font-family: "Avenir Next Condensed", "Franklin Gothic Medium", "Arial Narrow", sans-serif;
      font-size: 1.08rem;
      font-weight: 800;
      text-transform: uppercase;
    }}
    .reason {{
      position: relative;
      z-index: 1;
      line-height: 1.45;
      margin: 14px 0 12px;
    }}
    .metrics {{
      position: relative;
      z-index: 1;
      margin: 0;
      padding-left: 18px;
      color: #364443;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.96rem;
    }}
    th, td {{
      padding: 12px 10px;
      text-align: left;
      border-bottom: 1px solid var(--line);
      vertical-align: top;
    }}
    th {{
      font-family: "Avenir Next Condensed", "Franklin Gothic Medium", "Arial Narrow", sans-serif;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      font-size: 0.82rem;
      color: var(--muted);
    }}
    .footer-note {{
      margin-top: 20px;
      font-size: 0.92rem;
      color: var(--muted);
    }}
    @media (max-width: 760px) {{
      .wrap {{ padding: 18px 14px 32px; }}
      .hero, .section-panel, .summary-card, .day-card {{ border-radius: 18px; }}
      .risk-strip {{ grid-template-columns: repeat(2, minmax(0, 1fr)); }}
      .audit-summary {{ align-items: start; flex-direction: column; }}
    }}
  </style>
</head>
<body>
  <main class="wrap">
    <section class="hero">
      <div class="hero-top">
        <div>
          <p class="eyebrow">Archuleta County fire-weather monitor</p>
          <h1>Red Flag Risk</h1>
          <p class="hero-note">Generated {escape_html(format_generated_at(report))}. This page is a public-source screening view for early heads-up decisions.</p>
          <div class="official-warning">
            <strong>{escape_html(UNOFFICIAL_MONITOR_LABEL)}</strong>
            {escape_html(UNOFFICIAL_MONITOR_DISCLAIMER)}
          </div>
          <p class="next-update-note">Next update: {escape_html(format_next_update_at(report))}</p>
          <p class="time-note">All dates and times use {escape_html(local_time_context(report))}.</p>
        </div>
        <span class="chip {tier_badge_class(report['overall_tier'])}">{escape_html(report['overall_tier'])}</span>
      </div>
      <div class="summary-grid">
        {summary_cards_html}
      </div>
      <section class="hero-alert-panel">
        <div class="hero-alert-head">
          <div>
            <p class="eyebrow">Official Weather Alerts</p>
            <h2>Official NWS alerts</h2>
            <p class="footer-note">Active NWS alerts for monitored zones: {escape_html(monitored_zone_text)}.</p>
          </div>
          <span class="alert-count-chip">{escape_html(official_alert_count_label)}</span>
        </div>
        <div class="alert-grid">
          {alert_cards_html}
        </div>
      </section>
    </section>

    <section class="section-panel">
      <p class="eyebrow">7-Day Outlook</p>
      <h2>Weather + PSPS Outlook</h2>
      <p class="footer-note">{escape_html(psps.get('headline', 'No PSPS forecast available.'))}</p>
      <div class="definition-box">
        <strong>PSPS = Public Safety Power Shutoff</strong>
        <p>A planned, safety-related power shutoff LPEA may use during dangerous fire-weather conditions to reduce wildfire ignition risk. This monitor estimates weather-driven likelihood only; it is not an official shutoff notice.</p>
        <p class="definition-links">
          <a href="{escape_html(psps_url)}" target="_blank" rel="noopener noreferrer">LPEA PSPS guidance</a>
          <a href="{escape_html(outage_url)}" target="_blank" rel="noopener noreferrer">LPEA outage center</a>
          <a href="{escape_html(outage_map_url)}" target="_blank" rel="noopener noreferrer">LPEA outage map</a>
        </p>
      </div>
      <div class="risk-strip">
        {combined_outlook_html}
      </div>
      <div class="subsection-heading">
        <p class="eyebrow">Area-specific PSPS outlook</p>
        <h3>Where the risk is strongest</h3>
      </div>
      <div class="area-grid">
        {area_cards_html}
      </div>
      <details class="detail-disclosure">
        <summary>Location driver detail ({escape_html(str(psps_detail_day_count))} watch/likely days)</summary>
        <div class="detail-disclosure-content">
          <div class="psps-location-grid">
            {psps_location_cards_html}
          </div>
        </div>
      </details>
    </section>

    <section class="section-panel">
      <p class="eyebrow">Official Source Context</p>
      <h2>Fire Posture + Restrictions</h2>
      <p class="footer-note">{escape_html(fire_posture.get('headline', 'Fire-posture check not available.'))}</p>
      <p class="footer-note">Detected max: restrictions {escape_html(fire_posture.get('max_restriction_stage', 'UNKNOWN'))}; fire danger {escape_html(fire_posture.get('max_fire_danger', 'UNKNOWN'))}. Sources reachable: {escape_html(str(fire_posture.get('reachable_source_count', 0)))}/{escape_html(str(fire_posture.get('source_count', 0)))}.</p>
      <p class="footer-note">{escape_html(fire_posture.get('disclaimer', 'Verify directly with the responsible jurisdiction.'))}</p>
      <div class="fire-posture-grid">
        {fire_posture_cards_html}
      </div>
    </section>

    <section class="section-panel">
      <p class="eyebrow">Daily Breakdown</p>
      <h2>What Drives Each Day</h2>
      <div class="days-grid">
        {''.join(day_tiles)}
      </div>
    </section>

    <section class="section-panel">
      <p class="eyebrow">Model Calibration</p>
      <h2>Forecast Accuracy Scorecard</h2>
      <p class="footer-note">{escape_html(calibration.get('summary', 'No calibration summary available.'))}</p>
      <div class="calibration-grid">
        {calibration_cards_html}
      </div>
      <p class="footer-note">Event log: {escape_html(calibration.get('event_log_path', 'psps_events.json'))}</p>
    </section>

    <section class="section-panel">
      <p class="eyebrow">LPEA Monitor</p>
      <h2>Power Interruption Signals</h2>
      <p class="footer-note">{escape_html(lpea.get('headline', 'No LPEA headline available.'))}</p>
      <p class="footer-note">{escape_html(lpea_active_source_meaning())}</p>
      <p class="footer-note">Evidence quality: {escape_html(evidence_quality.get('summary', 'Evidence quality not classified.'))}</p>
      <p class="footer-note">Coverage: {escape_html(str(lpea.get('monitored_source_count', 0)))} sources; {escape_html(lpea.get('social_status', 'social sources not configured'))}</p>
      <div class="source-grid">
        {active_hits_html}
      </div>
      <div class="reference-pills">
        {reference_hits_html}
      </div>
    </section>

    <section class="section-panel compact-panel">
      <details class="detail-disclosure">
        <summary class="audit-summary">
          <span>Coverage + sample points</span>
          <small>NWS discussion: {escape_html(report['discussion']['headline'])}</small>
        </summary>
        <div class="detail-disclosure-content">
          <table>
            <thead>
              <tr>
                <th>Point</th>
                <th>Fire Zone</th>
                <th>Detail</th>
              </tr>
            </thead>
            <tbody>
              {''.join(point_rows)}
            </tbody>
          </table>
        </div>
      </details>
    </section>
  </main>
</body>
</html>
"""


def send_email(report: Dict[str, Any], config: Dict[str, Any]) -> Optional[str]:
    email_config = config.get("email") or {}
    if not email_config.get("enabled"):
        return None

    smtp_host = email_config.get("smtp_host")
    recipients = email_config.get("to") or []
    sender = email_config.get("from")
    if not smtp_host or not recipients or not sender:
        return "email disabled: missing smtp_host, from, or to configuration"

    username = os.environ.get(email_config.get("smtp_username_env", ""))
    password = os.environ.get(email_config.get("smtp_password_env", ""))
    if not username or not password:
        return "email disabled: missing SMTP credentials in configured environment variables"

    msg = EmailMessage()
    msg["Subject"] = f"Archuleta Monitor {report['overall_tier']} {format_display_date(report['generated_at_local'][:10])}"
    msg["From"] = sender
    msg["To"] = ", ".join(recipients)
    msg.set_content(render_email_text(report))

    port = int(email_config.get("smtp_port", 587))
    use_starttls = bool(email_config.get("smtp_starttls", True))
    timeout = int(email_config.get("timeout_seconds", 30))

    with smtplib.SMTP(smtp_host, port, timeout=timeout) as smtp:
        smtp.ehlo()
        if use_starttls:
            smtp.starttls()
            smtp.ehlo()
        smtp.login(username, password)
        smtp.send_message(msg)
    return f"sent to {', '.join(recipients)}"


def build_report(config_path: Path, config: Dict[str, Any]) -> Dict[str, Any]:
    tz = ZoneInfo(config["timezone"])
    now_utc = dt.datetime.now(dt.timezone.utc)
    now_local = now_utc.astimezone(tz)
    update_interval_minutes = config.get("expected_update_interval_minutes")
    next_update_local = (
        now_local + dt.timedelta(minutes=int(update_interval_minutes))
        if update_interval_minutes
        else None
    )
    horizon_end_utc = now_utc + dt.timedelta(days=config["forecast_horizon_days"])

    session = requests.Session()
    session.headers.update(
        {
            "User-Agent": config.get("user_agent", "archuleta-red-flag-monitor/1.0"),
            "Accept": "application/geo+json, application/json",
        }
    )

    point_results = [
        analyze_point(session, point, config, now_utc, horizon_end_utc, tz)
        for point in config["sample_points"]
    ]
    alert_zones = collect_alert_zones(config, point_results)
    alert_payload = fetch_active_alerts_for_zones(session, alert_zones)
    alert_summary = summarize_alerts(alert_payload, config["fire_weather_zone"], tz, alert_zones)
    alert_summary["monitored_zones"] = alert_zones
    discussion = fetch_discussion_signal(session)
    lpea = check_lpea(session, config)
    lpea["evidence_quality"] = lpea_evidence_quality(lpea)
    fire_posture = check_fire_posture(session, config)
    days = combine_daily_results(point_results, alert_summary, discussion, config, now_utc, tz)
    tier = overall_tier(days, point_results, discussion)
    psps = build_psps_forecast(days, alert_summary, lpea, fire_posture)

    history_path = config_path.resolve().parent / config["output"]["history_csv"]
    psps_events_path = event_log_path(config_path, config)
    forecast_csv = forecast_history_path(config_path, config)
    calibration = build_calibration_summary(
        load_psps_events(psps_events_path),
        load_forecast_history(forecast_csv),
        psps,
        now_local.date(),
        psps_events_path,
        forecast_csv,
    )
    prev_tier = previous_tier(history_path)
    notify_recommended = tier != "GREEN" or (prev_tier is not None and prev_tier != "GREEN")

    if all(point.get("status") != "ok" for point in point_results):
        days[0]["tier"] = max_tier(days[0]["tier"], "CONCERN")
        days[0]["reasons"].insert(0, "NWS forecast data unavailable for all sample points; cannot rule out risk.")

    return {
        "area_name": config["area_name"],
        "generated_at": now_local.isoformat(),
        "generated_at_local": now_local.isoformat(),
        "generated_at_utc": now_utc.isoformat(),
        "next_update_at": next_update_local.isoformat() if next_update_local else None,
        "expected_update_interval_minutes": update_interval_minutes,
        "timezone": config["timezone"],
        "local_time_name": config.get("local_time_name", "Pagosa Springs, CO"),
        "fire_weather_zone": config["fire_weather_zone"],
        "forecast_horizon_days": config["forecast_horizon_days"],
        "overall_tier": tier,
        "previous_tier": prev_tier,
        "notify_recommended": notify_recommended,
        "official_alerts": alert_summary,
        "discussion": discussion,
        "lpea": lpea,
        "fire_posture": fire_posture,
        "psps": psps,
        "calibration": calibration,
        "days": days,
        "points": point_results,
    }


def main() -> int:
    args = parse_args()
    config_path = Path(args.config)
    config = load_config(config_path)
    try:
        report = build_report(config_path, config)
    except requests.RequestException as exc:
        print(f"NWS fetch failed: {exc.__class__.__name__}: {exc}")
        return 2

    if not args.no_write:
        write_outputs(report, config_path, config)
        email_status = send_email(report, config)
        if email_status:
            print(f"Email: {email_status}")

    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        print(render_markdown(report))
        print(f"Monitor heads-up recommended: {report['notify_recommended']}")
        if not args.no_write:
            base = config_path.resolve().parent
            print("Saved:")
            print(f"- {base / config['output']['latest_markdown']}")
            print(f"- {base / config['output']['latest_json']}")
            print(f"- {base / config['output']['latest_html']}")
            print(f"- {base / config['output']['history_csv']}")
            print(f"- {forecast_history_path(config_path, config)}")
            print(f"- {event_log_path(config_path, config)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
