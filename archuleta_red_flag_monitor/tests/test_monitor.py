import datetime as dt
import sys
import unittest
from unittest import mock
from pathlib import Path
from zoneinfo import ZoneInfo

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import monitor


THRESHOLDS = {
    "red_flag_rh_percent": 15,
    "red_flag_wind_mph": 25,
    "red_flag_min_hours": 3,
    "red_flag_window_hours": 12,
    "near_rh_percent": 18,
    "near_wind_mph": 20,
    "near_min_hours": 2,
    "thunder_concern_percent": 20,
    "dry_thunder_precip_max_percent": 20,
    "elevated_thunder_percent": 15,
}


def record(hour, rh=None, wind=None, gust=None, thunder=None, precip=None):
    usable = max([value for value in (wind, gust) if value is not None], default=None)
    return {
        "utc_hour": hour,
        "relative_humidity": rh,
        "wind_speed_mph": wind,
        "wind_gust_mph": gust,
        "usable_wind_mph": usable,
        "probability_of_thunder": thunder,
        "probability_of_precip": precip,
        "red_flag_threat_index": None,
    }


class FakeResponse:
    def __init__(self, text, status_code=200):
        self.text = text
        self.status_code = status_code


class FakeSession:
    def __init__(self, responses):
        self.responses = responses

    def get(self, url, timeout=20):
        return self.responses[url]


class MonitorTests(unittest.TestCase):
    def test_has_hours_in_window_counts_nonconsecutive_hours(self):
        base = dt.datetime(2026, 6, 1, 12, tzinfo=dt.timezone.utc)
        hours = [base, base + dt.timedelta(hours=4), base + dt.timedelta(hours=11)]
        self.assertTrue(monitor.has_hours_in_window(hours, min_hours=3, window_hours=12))

    def test_has_hours_in_window_rejects_hours_outside_window(self):
        base = dt.datetime(2026, 6, 1, 12, tzinfo=dt.timezone.utc)
        hours = [base, base + dt.timedelta(hours=4), base + dt.timedelta(hours=12)]
        self.assertFalse(monitor.has_hours_in_window(hours, min_hours=3, window_hours=12))

    def test_score_day_high_for_red_flag_screen(self):
        base = dt.datetime(2026, 6, 1, 12, tzinfo=dt.timezone.utc)
        records = [
            record(base, rh=14, wind=26),
            record(base + dt.timedelta(hours=1), rh=15, gust=28),
            record(base + dt.timedelta(hours=4), rh=13, wind=20, gust=25),
        ]
        scored = monitor.score_day(records, THRESHOLDS)
        self.assertEqual(scored["tier"], "HIGH")
        self.assertEqual(scored["red_flag_hours"], 3)

    def test_score_day_concern_for_near_threshold(self):
        base = dt.datetime(2026, 6, 1, 12, tzinfo=dt.timezone.utc)
        records = [
            record(base, rh=18, wind=21),
            record(base + dt.timedelta(hours=2), rh=17, gust=22),
        ]
        scored = monitor.score_day(records, THRESHOLDS)
        self.assertEqual(scored["tier"], "CONCERN")

    def test_score_day_elevated_for_single_ingredient(self):
        base = dt.datetime(2026, 6, 1, 12, tzinfo=dt.timezone.utc)
        scored = monitor.score_day([record(base, rh=14, wind=10)], THRESHOLDS)
        self.assertEqual(scored["tier"], "ELEVATED")

    def test_speed_conversion(self):
        self.assertAlmostEqual(monitor.speed_to_mph(40, "wmoUnit:km_h-1"), 24.85484, places=4)
        self.assertAlmostEqual(monitor.speed_to_mph(10, "wmoUnit:m_s-1"), 22.3694, places=4)
        self.assertEqual(monitor.speed_to_mph(25, "wmoUnit:mi_h-1"), 25)

    def test_grid_field_expansion_groups_local_day(self):
        start = dt.datetime(2026, 6, 1, 0, tzinfo=dt.timezone.utc)
        end = start + dt.timedelta(hours=3)
        field = {"values": [{"validTime": "2026-06-01T00:00:00+00:00/PT3H", "value": 12}]}
        expanded = monitor.expand_grid_field(field, start, end)
        self.assertEqual(len(expanded), 3)
        self.assertEqual(expanded[start + dt.timedelta(hours=2)], 12)

    def test_alert_summary_marks_fire_alert_dates(self):
        tz = ZoneInfo("America/Denver")
        payload = {
            "features": [
                {
                    "id": "https://api.weather.gov/alerts/test-red-flag",
                    "properties": {
                        "event": "Red Flag Warning",
                        "headline": "Red Flag Warning issued for Southwest Colorado",
                        "affectedZones": ["https://api.weather.gov/zones/fire/COZ295"],
                        "effective": "2026-06-01T18:00:00+00:00",
                        "ends": "2026-06-02T03:00:00+00:00",
                    }
                }
            ]
        }
        summary = monitor.summarize_alerts(payload, "COZ295", tz)
        self.assertEqual(summary["fire_alert_count"], 1)
        self.assertEqual(summary["high_dates"], ["2026-06-01"])
        self.assertEqual(summary["alerts"][0]["effective"], "2026-06-01T12:00:00-06:00")
        self.assertEqual(summary["alerts"][0]["ends"], "2026-06-01T21:00:00-06:00")
        self.assertEqual(summary["alerts"][0]["timezone"], "America/Denver")
        self.assertEqual(summary["alerts"][0]["url"], "https://api.weather.gov/alerts/test-red-flag")
        self.assertEqual(summary["alerts"][0]["zones"], ["COZ295"])

    def test_alert_summary_filters_unmonitored_fire_alert_zones(self):
        tz = ZoneInfo("America/Denver")
        payload = {
            "features": [
                {
                    "id": "https://api.weather.gov/alerts/unmonitored-red-flag",
                    "properties": {
                        "event": "Red Flag Warning",
                        "headline": "Red Flag Warning outside monitored zones",
                        "affectedZones": ["https://api.weather.gov/zones/fire/COZ207"],
                        "effective": "2026-06-01T18:00:00+00:00",
                        "ends": "2026-06-02T03:00:00+00:00",
                    },
                }
            ]
        }
        summary = monitor.summarize_alerts(payload, "COZ295", tz, ["COZ295", "COZ023", "COC007"])
        self.assertEqual(summary["fire_alert_count"], 0)
        self.assertEqual(summary["alerts"], [])
        self.assertEqual(summary["high_dates"], [])

    def test_lpea_active_source_match_flags_current_signal(self):
        config = {
            "lpea": {
                "enabled": True,
                "alert_keywords": ["power outage", "psps"],
                "sources": [
                    {"name": "Active updates", "url": "https://example.test/active", "type": "official_updates", "signal_mode": "active"},
                    {"name": "Reference page", "url": "https://example.test/reference", "type": "official_info", "signal_mode": "reference"},
                    {"name": "Social", "url": "https://example.test/social", "type": "official_social", "signal_mode": "active"},
                ],
            }
        }
        session = FakeSession(
            {
                "https://example.test/active": FakeResponse("Power outage update for members."),
                "https://example.test/reference": FakeResponse("PSPS information page."),
                "https://example.test/social": FakeResponse("No current alerts."),
            }
        )
        result = monitor.check_lpea(session, config)
        self.assertEqual(result["status"], "active_keyword_match")
        self.assertEqual(result["monitored_source_count"], 3)
        self.assertEqual(result["social_status"], "1/1 official social sources reachable")
        self.assertEqual(result["active_hits"][0]["name"], "Active updates")

    def test_lpea_signal_groups_collapse_duplicate_snippets(self):
        hits = [
            {
                "name": "LPEA homepage",
                "url": "https://example.test",
                "type": "official_updates",
                "matches": ["red flag"],
                "snippets": ["Red Flag Warnings are in place across our service territory. Learn how this may affect you HERE."],
            },
            {
                "name": "LPEA latest news",
                "url": "https://example.test/news",
                "type": "official_updates",
                "matches": ["red flag"],
                "snippets": ["Red Flag Warnings are in place across our service territory. Learn how this may affect you HERE."],
            },
            {
                "name": "LPEA LinkedIn",
                "url": "https://example.test/linkedin",
                "type": "official_social",
                "matches": ["wildfire"],
                "snippets": ["Wildfire season does not wait, and neither do we."],
            },
        ]
        groups = monitor.group_lpea_signal_hits(hits)
        self.assertEqual(len(groups), 2)
        self.assertEqual(groups[0]["name"], "Site-wide red flag banner")
        self.assertEqual(groups[0]["source_count"], 2)
        self.assertEqual(groups[0]["source_names"], ["LPEA homepage", "LPEA latest news"])
        self.assertEqual(groups[1]["name"], "LinkedIn wildfire preparedness post")

    def test_lpea_reference_only_match_is_context(self):
        config = {
            "lpea": {
                "enabled": True,
                "alert_keywords": ["public safety power shutoff"],
                "sources": [
                    {"name": "Reference page", "url": "https://example.test/reference", "type": "official_info", "signal_mode": "reference"},
                    {"name": "Active page", "url": "https://example.test/active", "type": "official_updates", "signal_mode": "active"},
                ],
            }
        }
        session = FakeSession(
            {
                "https://example.test/reference": FakeResponse("Public Safety Power Shutoff overview."),
                "https://example.test/active": FakeResponse("Routine member news."),
            }
        )
        result = monitor.check_lpea(session, config)
        self.assertEqual(result["status"], "reference_keyword_match")
        self.assertEqual(result["active_hits"], [])
        self.assertEqual(result["reference_hits"][0]["name"], "Reference page")

    def test_build_psps_forecast_marks_high_days_likely(self):
        days = [
            {
                "date": "2026-06-01",
                "tier": "HIGH",
                "points": [
                    {"name": "Arboles", "tier": "HIGH", "min_rh_percent": 12, "max_usable_wind_mph": 33, "max_thunder_percent": 7, "max_precip_percent": 0, "red_flag_hours": 3, "near_hours": 5}
                ],
            },
            {
                "date": "2026-06-02",
                "tier": "CONCERN",
                "points": [
                    {"name": "Durango", "tier": "CONCERN", "min_rh_percent": 14, "max_usable_wind_mph": 23, "max_thunder_percent": 8, "max_precip_percent": 0, "red_flag_hours": 0, "near_hours": 4}
                ],
            },
            {
                "date": "2026-06-03",
                "tier": "ELEVATED",
                "points": [
                    {"name": "Pagosa Springs", "tier": "ELEVATED", "min_rh_percent": 14, "max_usable_wind_mph": 12, "max_thunder_percent": 0, "max_precip_percent": 0, "red_flag_hours": 0, "near_hours": 0}
                ],
            },
            {
                "date": "2026-06-04",
                "tier": "GREEN",
                "points": [
                    {"name": "Bayfield", "tier": "GREEN", "min_rh_percent": 30, "max_usable_wind_mph": 10, "max_thunder_percent": 0, "max_precip_percent": 0, "red_flag_hours": 0, "near_hours": 0}
                ],
            },
        ]
        lpea = {
            "active_hits": [
                {
                    "matches": ["red flag"],
                    "snippets": ["Red Flag Warnings are in place across our service territory."],
                }
            ]
        }
        psps = monitor.build_psps_forecast(days, {"high_dates": []}, lpea)
        self.assertEqual(psps["overall_level"], "LIKELY")
        self.assertEqual(psps["days"][0]["level"], "LIKELY")
        self.assertEqual(psps["days"][1]["level"], "WATCH")
        self.assertEqual(psps["days"][1]["driver_locations"][0]["name"], "Durango")
        self.assertEqual(psps["days"][1]["trend"]["label"], "Easing")
        self.assertEqual(psps["days"][2]["level"], "ELEVATED")
        self.assertEqual(psps["days"][3]["level"], "LOW")

    def test_risk_window_summary_uses_local_near_threshold_hours(self):
        base = dt.datetime(2026, 6, 1, 18, tzinfo=dt.timezone.utc)
        records = [
            record(base, rh=19, wind=19),
            record(base + dt.timedelta(hours=1), rh=17, wind=21),
            record(base + dt.timedelta(hours=3), rh=14, gust=27),
        ]
        for item in records:
            item["local_hour"] = item["utc_hour"].astimezone(ZoneInfo("America/Denver"))
        summary = monitor.risk_window_summary(records, THRESHOLDS)
        self.assertIn("1 PM-3 PM local", summary)
        self.assertIn("2 near/red-flag threshold hours", summary)

    def test_calibration_summary_scores_confirmed_event_against_history(self):
        events = [
            {
                "date": "2026-06-01",
                "status": "confirmed",
                "locations": ["Pagosa Springs"],
                "source_url": "https://example.test/psps",
                "summary": "Confirmed PSPS.",
            }
        ]
        history = [
            {"date": "2026-06-01", "location": "Pagosa Springs", "psps_level": "LIKELY"},
            {"date": "2026-06-02", "location": "Pagosa Springs", "psps_level": "WATCH"},
        ]
        current_psps = {"days": [{"date": "2026-06-03", "level": "WATCH"}]}
        summary = monitor.build_calibration_summary(
            events,
            history,
            current_psps,
            dt.date(2026, 6, 4),
            Path("psps_events.json"),
            Path("forecast_history.csv"),
        )
        self.assertEqual(summary["confirmed_event_count"], 1)
        self.assertEqual(summary["hit_count"], 1)
        self.assertEqual(summary["hit_rate_percent"], 100)
        self.assertEqual(summary["false_watch_day_count"], 1)
        self.assertEqual(summary["pending_watch_dates"], ["2026-06-03"])

    def test_lpea_evidence_quality_labels_archived_items(self):
        lpea = {
            "active_signal_groups": [
                {
                    "name": "News-release archive PSPS item",
                    "source_names": ["LPEA news releases"],
                    "types": ["official_updates"],
                    "snippet": "Power Shutoffs Possible to Protect Public Safety 07/22/2025",
                    "matches": ["power shutoff"],
                },
                {
                    "name": "Site-wide red flag banner",
                    "source_names": ["LPEA homepage"],
                    "types": ["official_updates"],
                    "snippet": "Site-wide LPEA banner: Red Flag Warnings are in place across the service territory.",
                    "matches": ["red flag"],
                },
            ],
            "reference_hits": [{"name": "PSPS guidance"}],
        }
        quality = monitor.lpea_evidence_quality(lpea)
        self.assertEqual(quality["groups"][0]["quality"]["label"], "Archive/context")
        self.assertEqual(quality["groups"][1]["quality"]["label"], "Current banner")
        self.assertIn("1 active/update", quality["summary"])

    def test_fire_posture_parser_detects_stage_and_danger(self):
        text = "Current fire danger is Very High. Stage 1 Fire Restrictions are in effect for public lands."
        self.assertEqual(monitor.detect_restriction_stage(text), "STAGE 1")
        self.assertEqual(monitor.detect_fire_danger_level(text), "VERY HIGH")

    def test_fire_posture_parser_ignores_stale_or_water_restrictions(self):
        self.assertEqual(
            monitor.detect_restriction_stage("La Plata County Stage 1 Fire Restrictions Rescinded, August 31, 2023."),
            "NONE",
        )
        self.assertEqual(
            monitor.detect_restriction_stage("City of Durango implements Stage 1 mandatory water restrictions."),
            "UNKNOWN",
        )
        self.assertEqual(
            monitor.detect_restriction_stage("Stage 1 Fire Restrictions Guidelines are in effect when fire restrictions are enacted."),
            "UNKNOWN",
        )

    def test_fire_posture_snippets_filter_non_fire_restrictions(self):
        text = (
            "City of Durango implements Stage 1 mandatory water restrictions effective April 10. "
            + "Other public works updates follow. " * 20
            + "Fire restrictions are currently in effect for public lands."
        )
        snippets = monitor.fire_posture_snippets(text)
        self.assertTrue(snippets)
        self.assertNotIn("water restrictions", " ".join(snippets).lower())
        self.assertIn("fire restrictions", " ".join(snippets).lower())

    def test_fire_posture_signal_bumps_to_watch_for_stage_two(self):
        signal = monitor.fire_posture_psps_signal(
            {
                "status": "checked",
                "max_restriction_stage": "STAGE 2",
                "max_fire_danger": "HIGH",
            }
        )
        self.assertEqual(signal["level_floor"], "WATCH")
        self.assertIn("STAGE 2", signal["reason"])

    def test_jurisdiction_type_label_is_human_readable(self):
        self.assertEqual(monitor.jurisdiction_type_label("federal_forest"), "Federal forest")
        self.assertEqual(monitor.jurisdiction_type_label("county_fire_district"), "Fire district")
        self.assertEqual(monitor.jurisdiction_type_label("custom_source"), "Custom Source")

    def test_fire_posture_omits_generic_snippets_for_unknown_sources(self):
        config = {
            "fire_posture": {
                "enabled": True,
                "sources": [
                    {"name": "Generic source", "url": "https://example.test/generic", "area": "Town", "type": "town"}
                ],
            }
        }
        session = FakeSession(
            {
                "https://example.test/generic": FakeResponse("Please observe fire restrictions outside of town limits.")
            }
        )
        result = monitor.check_fire_posture(session, config)
        self.assertEqual(result["sources"][0]["restriction_stage"], "UNKNOWN")
        self.assertEqual(result["sources"][0]["snippets"], [])

    def test_render_markdown_includes_at_a_glance(self):
        report = {
            "generated_at_local": "2026-06-01T08:00:00-06:00",
            "next_update_at": "2026-06-01T09:00:00-06:00",
            "timezone": "America/Denver",
            "local_time_name": "Pagosa Springs, CO",
            "overall_tier": "HIGH",
            "psps": {
                "overall_level": "LIKELY",
                "headline": "PSPS likelihood is high.",
                "lpea_signal": {"reason": "LPEA active source signal."},
                "disclaimer": "Not official.",
                "days": [
                    {"date": "2026-06-01", "level": "LIKELY", "weather_score": 75, "driver_locations": [{"name": "Arboles", "level": "LIKELY", "score": 75}], "reasons": ["Red-flag screen."]},
                    {"date": "2026-06-02", "level": "WATCH", "weather_score": 50, "driver_locations": [{"name": "Durango", "level": "WATCH", "score": 50}], "reasons": ["Near threshold."]},
                ],
            },
            "notify_recommended": True,
            "official_alerts": {
                "fire_alert_count": 1,
                "monitored_zones": ["COZ295", "COZ023"],
                "alerts": [
                    {
                        "event": "Red Flag Warning",
                        "headline": "Red Flag Warning issued",
                        "url": "https://api.weather.gov/alerts/test-red-flag",
                        "zones": ["COZ295"],
                        "effective": "2026-06-01T12:00:00-06:00",
                        "ends": "2026-06-01T21:00:00-06:00",
                    }
                ],
            },
            "lpea": {"status": "keyword_match", "headline": "Keyword detected."},
            "discussion": {"headline": "Concern language found."},
            "calibration": {
                "summary": "No confirmed LPEA PSPS events logged yet.",
                "confirmed_event_count": 0,
                "candidate_event_count": 0,
                "false_watch_day_count": 0,
                "pending_watch_dates": ["2026-06-01"],
                "event_log_path": "psps_events.json",
                "forecast_history_path": "forecast_history.csv",
            },
            "days": [
                {"date": "2026-06-01", "tier": "HIGH", "reasons": ["Critical winds."], "points": []},
                {"date": "2026-06-02", "tier": "CONCERN", "reasons": ["Near threshold."], "points": []},
                {"date": "2026-06-03", "tier": "ELEVATED", "reasons": ["Low RH."], "points": []},
            ],
            "points": [],
        }
        rendered = monitor.render_markdown(report)
        self.assertIn("## At A Glance", rendered)
        self.assertIn("Generated: Jun 1, 2026 at 8:00 AM MDT (Pagosa Springs, CO local time)", rendered)
        self.assertIn("Next update: Jun 1, 2026 at 9:00 AM MDT (Pagosa Springs, CO local time)", rendered)
        self.assertIn("Date/time basis: Pagosa Springs, CO local time (America/Denver)", rendered)
        self.assertIn("not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice", rendered)
        self.assertIn("PSPS likelihood: **LIKELY**", rendered)
        self.assertIn("Monitor heads-up recommended: **YES**", rendered)
        self.assertIn("not an official LPEA or NWS notice", rendered)
        self.assertIn("## PSPS Likelihood", rendered)
        self.assertIn("PSPS means Public Safety Power Shutoff", rendered)
        self.assertIn("https://lpea.coop/outage-center", rendered)
        self.assertIn("## Official Weather Alerts", rendered)
        self.assertIn("[Red Flag Warning](https://api.weather.gov/alerts/test-red-flag)", rendered)
        self.assertIn("HIGH dates: Mon, Jun 1", rendered)
        self.assertIn("CONCERN dates: Tue, Jun 2", rendered)
        self.assertIn("ELEVATED dates: Wed, Jun 3", rendered)

    def test_render_html_includes_risk_strip_and_day_cards(self):
        report = {
            "generated_at_local": "2026-06-01T08:00:00-06:00",
            "next_update_at": "2026-06-01T09:00:00-06:00",
            "timezone": "America/Denver",
            "local_time_name": "Pagosa Springs, CO",
            "overall_tier": "HIGH",
            "psps": {
                "overall_level": "LIKELY",
                "headline": "PSPS likelihood is high.",
                "lpea_signal": {"reason": "LPEA active source signal."},
                "disclaimer": "Not official.",
                "days": [
                    {"date": "2026-06-01", "level": "LIKELY", "weather_score": 75, "driver_locations": [{"name": "Pagosa Springs", "level": "LIKELY", "score": 75, "summary": "Weather score 75/100."}], "location_scores": [{"name": "Pagosa Springs", "level": "LIKELY", "score": 75, "summary": "Weather score 75/100."}], "reasons": ["Red-flag screen."]},
                    {"date": "2026-06-02", "level": "WATCH", "weather_score": 50, "driver_locations": [{"name": "Durango", "level": "WATCH", "score": 50, "summary": "Weather score 50/100."}], "reasons": ["Near threshold."]},
                ],
            },
            "notify_recommended": True,
            "official_alerts": {
                "fire_alert_count": 1,
                "monitored_zones": ["COZ295", "COZ023"],
                "alerts": [
                    {
                        "event": "Red Flag Warning",
                        "headline": "Red Flag Warning issued",
                        "url": "https://api.weather.gov/alerts/test-red-flag",
                        "zones": ["COZ295"],
                        "effective": "2026-06-01T12:00:00-06:00",
                        "ends": "2026-06-01T21:00:00-06:00",
                    }
                ],
            },
            "lpea": {
                "status": "keyword_match",
                "headline": "Keyword detected.",
                "active_signal_groups": [
                    {
                        "name": "Test LPEA source",
                        "primary_url": "https://example.test/lpea",
                        "source_count": 1,
                        "source_names": ["Test LPEA source"],
                        "urls": ["https://example.test/lpea"],
                        "matches": ["red flag"],
                        "snippet": "Red flag keyword found.",
                    }
                ],
                "reference_hits": [{"name": "Reference page", "url": "https://example.test/ref"}],
            },
            "discussion": {"headline": "Concern language found."},
            "days": [
                {
                    "date": "2026-06-01",
                    "tier": "HIGH",
                    "reasons": ["Critical winds."],
                    "points": [
                        {"name": "Pagosa Springs", "tier": "HIGH", "min_rh_percent": 12, "max_usable_wind_mph": 31, "max_thunder_percent": 3}
                    ],
                },
                {
                    "date": "2026-06-02",
                    "tier": "CONCERN",
                    "reasons": ["Near threshold."],
                    "points": [
                        {"name": "Arboles", "tier": "CONCERN", "min_rh_percent": 15, "max_usable_wind_mph": 22, "max_thunder_percent": 8}
                    ],
                },
            ],
            "points": [
                {"name": "Pagosa", "status": "ok", "fire_weather_zone": "COZ295", "zone_status": "matches", "forecast_zone": "COZ023", "county_zone": "COC007"}
            ],
        }
        rendered = monitor.render_html(report)
        self.assertIn("Weather + PSPS Outlook", rendered)
        self.assertIn("PSPS = Public Safety Power Shutoff", rendered)
        self.assertIn("LPEA outage center", rendered)
        self.assertIn("https://lpea.coop/outage-center", rendered)
        self.assertIn("Pagosa Springs today", rendered)
        self.assertIn("Pagosa PSPS score 75/100", rendered)
        self.assertIn("RH 12%, wind 31 mph", rendered)
        self.assertIn("Official Weather Alerts", rendered)
        self.assertIn("hero-alert-panel", rendered)
        self.assertIn("1 active", rendered)
        self.assertIn("hero-status-rail", rendered)
        self.assertIn("Current monitor status", rendered)
        self.assertIn("Official NWS", rendered)
        self.assertIn("https://api.weather.gov/alerts/test-red-flag", rendered)
        self.assertLess(rendered.index("Official Weather Alerts"), rendered.index("Weather + PSPS Outlook"))
        self.assertLess(rendered.index("Weather + PSPS Outlook"), rendered.index("What Drives Each Day"))
        self.assertLess(rendered.index("What Drives Each Day"), rendered.index("Power Interruption Signals"))
        self.assertIn("href=\"https://example.test/lpea\"", rendered)
        self.assertIn("href=\"https://example.test/ref\"", rendered)
        self.assertIn("outlook-segment psps-likely", rendered)
        self.assertIn("PSPS LIKELY", rendered)
        self.assertIn("Weather HIGH", rendered)
        self.assertIn("Arboles", rendered)
        self.assertIn("Durango", rendered)
        self.assertIn("Next update: Jun 1, 2026 at 9:00 AM MDT (Pagosa Springs, CO local time)", rendered)
        self.assertIn("All dates and times use Pagosa Springs, CO local time (America/Denver).", rendered)
        self.assertIn("official-warning", rendered)
        self.assertIn("not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice", rendered)
        self.assertIn("Send monitor heads-up?", rendered)
        self.assertIn("Send this monitor report because current risk is HIGH.", rendered)
        self.assertIn("risk-strip", rendered)
        self.assertIn("Mon</strong><span>Jun 1", rendered)
        self.assertIn("<small>Jun 1</small>", rendered)
        self.assertIn("day-card tier-high", rendered)
        self.assertIn("Forecast Accuracy Scorecard", rendered)
        self.assertIn("Area-specific", rendered)
        self.assertIn("Highest-risk window", rendered)
        self.assertIn("Evidence quality", rendered)
        self.assertIn("Keyword Match", rendered)
        self.assertIn("Keyword detected.", rendered)

    @mock.patch.dict("os.environ", {"ARCHULETA_MONITOR_SMTP_USERNAME": "user", "ARCHULETA_MONITOR_SMTP_PASSWORD": "pass"})
    def test_send_email_uses_smtp_when_enabled(self):
        report = {
            "generated_at_local": "2026-06-01T08:00:00-06:00",
            "next_update_at": "2026-06-01T09:00:00-06:00",
            "timezone": "America/Denver",
            "local_time_name": "Pagosa Springs, CO",
            "overall_tier": "CONCERN",
            "notify_recommended": True,
            "official_alerts": {"fire_alert_count": 0},
            "lpea": {"status": "reachable_no_fire_keywords", "headline": "No fire keywords."},
            "discussion": {"headline": "No concerning language."},
            "days": [{"date": "2026-06-01", "tier": "CONCERN", "reasons": ["Near threshold."], "points": []}],
        }
        config = {
            "email": {
                "enabled": True,
                "from": "from@example.com",
                "to": ["to@example.com"],
                "smtp_host": "smtp.example.com",
                "smtp_port": 587,
                "smtp_starttls": True,
                "smtp_username_env": "ARCHULETA_MONITOR_SMTP_USERNAME",
                "smtp_password_env": "ARCHULETA_MONITOR_SMTP_PASSWORD",
                "timeout_seconds": 30,
            }
        }
        with mock.patch("monitor.smtplib.SMTP") as smtp_cls:
            status = monitor.send_email(report, config)
        self.assertEqual(status, "sent to to@example.com")
        smtp_instance = smtp_cls.return_value.__enter__.return_value
        smtp_instance.starttls.assert_called_once()
        smtp_instance.login.assert_called_once_with("user", "pass")
        smtp_instance.send_message.assert_called_once()

    def test_send_email_returns_reason_when_not_configured(self):
        report = {
            "generated_at_local": "2026-06-01T08:00:00-06:00",
            "next_update_at": "2026-06-01T09:00:00-06:00",
            "timezone": "America/Denver",
            "local_time_name": "Pagosa Springs, CO",
            "overall_tier": "GREEN",
            "notify_recommended": False,
            "official_alerts": {"fire_alert_count": 0},
            "lpea": {"status": "unavailable", "headline": "Unavailable."},
            "discussion": {"headline": "Unavailable."},
            "days": [],
        }
        config = {"email": {"enabled": True}}
        status = monitor.send_email(report, config)
        self.assertIn("missing smtp_host, from, or to", status)


if __name__ == "__main__":
    unittest.main()
