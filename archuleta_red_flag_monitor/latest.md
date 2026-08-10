# Archuleta County fire-weather monitor

Generated: Aug 9, 2026 at 5:31 PM MDT (Pagosa Springs, CO local time)
Next update: Aug 10, 2026 at 5:20 AM MDT (Pagosa Springs, CO local time)
Date/time basis: Pagosa Springs, CO local time (America/Denver)
> **Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## At A Glance

- Fire-weather tier: **CONCERN**
- PSPS likelihood: **WATCH**
- PSPS likely dates: None
- PSPS watch dates: Sun, Aug 9; Mon, Aug 10
- Monitor heads-up recommended: **YES** - Send this monitor report because fire-weather screening tier is CONCERN; PSPS screening level is WATCH; a material current wildfire is reported in Archuleta County. This is not an official LPEA or NWS notice.
- HIGH dates: None
- CONCERN dates: Sun, Aug 9; Mon, Aug 10
- ELEVATED dates: None
- Official NWS Red Flag / Fire Weather alerts (COZ295): 0
- LPEA signal: `active_keyword_match` - LPEA active/update sources contained power-interruption keywords; review source before treating as confirmed outage intent.
- LPEA source coverage: 13 sources; 5/5 official social sources reachable
- Current Archuleta County wildfires: 1
- Official evacuation notices: No current evacuation order or warning detected in the checked official county feeds.
- NWS discussion: No concerning fire-weather language found in latest GJT discussion.

## Decision Support

- Summary: Highest LPEA PSPS concern is Sun, Aug 9 near Arboles / southwest county (WATCH 50/100), driven by near-threshold wind/gust signal near 21 mph; very dry RH near 12%; 2 sampled hours are near red-flag thresholds. NIFC reports 1 current wildfire in Archuleta County.
- Confidence: **MEDIUM** (69/100) - 8/8 sampled weather points available; 7/7 fire-posture sources reachable; official NWS alert zones checked; 13/13 LPEA public sources reachable; LPEA active/update sources checked; authoritative NIFC current-incident feed checked for Archuleta County; official Archuleta County evacuation feeds checked; forecast changed substantially versus prior run; no confirmed PSPS events logged yet for calibration
- Weather fire-potential peak: Sun, Aug 9: Arboles / southwest county HIGH 61/100
- Red Flag likelihood peak: Sun, Aug 9: Arboles / southwest county WATCH 56/100
- LPEA PSPS peak: Sun, Aug 9: Arboles / southwest county WATCH 50/100
- Method: rules-based decision support using public weather, fire-posture, and LPEA source signals; scores are screening estimates, not official or statistically calibrated probabilities.

| Date | Weather fire potential | Red Flag likelihood | LPEA PSPS | Main window |
| --- | --- | --- | --- | --- |
| Sun, Aug 9 | Arboles / southwest county: HIGH 61/100 | Arboles / southwest county: WATCH 56/100 | Arboles / southwest county: WATCH 50/100 | 5 PM-6 PM local; 2 near/red-flag threshold hours. |
| Mon, Aug 10 | Arboles / southwest county: HIGH 61/100 | Arboles / southwest county: WATCH 55/100 | Arboles / southwest county: WATCH 46/100 | 2 PM-4 PM local; 3 near/red-flag threshold hours. |
| Tue, Aug 11 | Durango / La Plata County: MODERATE 44/100 | Ignacio / southeast La Plata County: LOW 16/100 | Ignacio / southeast La Plata County: ELEVATED 28/100 | 3 PM-3 PM local; 1 near/red-flag threshold hour. |
| Wed, Aug 12 | Bayfield / east La Plata County: LOW 30/100 | Arboles / southwest county: LOW 8/100 | Arboles / southwest county: ELEVATED 18/100 | Peak ingredients near 3 PM local; RH 23%, wind 21 mph. |
| Thu, Aug 13 | Durango / La Plata County: MODERATE 36/100 | Durango / La Plata County: LOW 8/100 | Durango / La Plata County: ELEVATED 20/100 | Peak ingredients near 3 PM local; RH 36%, wind 22 mph. |
| Fri, Aug 14 | Durango / La Plata County: MODERATE 36/100 | Durango / La Plata County: LOW 8/100 | Durango / La Plata County: ELEVATED 20/100 | Peak ingredients near 4 PM local; RH 32%, wind 23 mph. |
| Sat, Aug 15 | Chimney Rock / west county: MODERATE 38/100 | Arboles / southwest county: LOW 8/100 | Arboles / southwest county: ELEVATED 24/100 | Peak ingredients near 4 PM local; RH 21%, wind 22 mph. |

## Analyst Interpretation

- Headline: Screening remains CONCERN with PSPS WATCH through Monday, while no official COZ295 alert or active LPEA outage is reported.
- Summary: Sunday and Monday remain PSPS WATCH periods centered on Arboles, peaking Sunday at 50/100 and Monday at 46/100. Official sources show no COZ295 Red Flag or Fire Weather alert, active LPEA outage, or confirmed shutoff notice; two Air Quality Alerts are separate health advisories. Rio Blanco is mapped at about 1,388 acres and 79% contained, with no evacuation notice detected.
- Uncertainty: PSPS screening is uncalibrated because no confirmed LPEA PSPS events have been logged; 53 false-WATCH days and HIGH forecast volatility mean estimates may change materially.
- Evidence used: overall_status, weather_peaks, official_alerts, forecast_change, lpea_context, fire_posture, active_incidents, calibration
- This interpretation cannot change the deterministic tiers, scores, official alerts, or notification decision.

Changing drivers:
- Momentum is easing, but HIGH forecast volatility at 40/100 indicates substantial run-to-run change.
- Tuesday eased from PSPS WATCH to ELEVATED, falling 18 points to 28/100 near Ignacio.
- Saturday eased 16 points and remains ELEVATED, with Arboles now the driver.
- Rio Blanco remains about 1,388 acres and 79% contained, with no evacuation notice detected.

What to watch next:
- Recheck Arboles through 6 PM Sunday for wind, humidity, or official-alert escalation.
- Watch Arboles from 2 PM to 4 PM Monday, the next PSPS WATCH window.
- Treat any new NWS alert or LPEA outage notice as official context, separate from screening estimates.
- Monitor Rio Blanco containment and county evacuation feeds for operational changes.

## Trend Intelligence

- Summary: Momentum is easing versus the prior run (Aug 9 at 5:23 AM MDT); forecast volatility is high and first WATCH-or-higher date is Sun, Aug 9.
- Momentum: **Easing**
- Forecast volatility: **HIGH** (40/100)
- First WATCH-or-higher PSPS date: Sun, Aug 9
- Watch-date movement: First WATCH-or-higher PSPS date remains Sun, Aug 9.
- Method: compares current forecast evidence against prior local forecast history.

Notable changes:
- First WATCH-or-higher PSPS date remains Sun, Aug 9.
- Tue, Aug 11: easing vs prior run; PSPS WATCH -> ELEVATED; score -18, wind 0 mph, RH +1%, red-flag hours 0. Driver shifted to Ignacio / southeast La Plata County.
- Sat, Aug 15: easing vs prior run; PSPS ELEVATED -> ELEVATED; score -16, wind 0 mph, RH +2%, red-flag hours 0. Driver shifted to Arboles / southwest county.

## Public Analysis Export

- Summary: Highest LPEA PSPS concern is Sun, Aug 9 near Arboles / southwest county (WATCH 50/100), driven by near-threshold wind/gust signal near 21 mph; very dry RH near 12%; 2 sampled hours are near red-flag thresholds. NIFC reports 1 current wildfire in Archuleta County.
- Trend: Momentum is easing versus the prior run (Aug 9 at 5:23 AM MDT); forecast volatility is high and first WATCH-or-higher date is Sun, Aug 9.
- Confidence: **MEDIUM** (69/100)
- First WATCH-or-higher PSPS date: Sun, Aug 9
- PSPS peak: Sun, Aug 9 near Arboles / southwest county at WATCH 50/100
- Red Flag peak: Sun, Aug 9 near Arboles / southwest county at WATCH 56/100
- Weather fire-potential peak: Sun, Aug 9 near Arboles / southwest county at HIGH 61/100
- LPEA operational outage context: No active outages are listed by the official LPEA outage viewer.
- Public JSON: `archuleta_red_flag_monitor/public_analysis_export.json`

What changed:
- First WATCH-or-higher PSPS date remains Sun, Aug 9.
- Tue, Aug 11: easing vs prior run; PSPS WATCH -> ELEVATED; score -18, wind 0 mph, RH +1%, red-flag hours 0. Driver shifted to Ignacio / southeast La Plata County.
- Sat, Aug 15: easing vs prior run; PSPS ELEVATED -> ELEVATED; score -16, wind 0 mph, RH +2%, red-flag hours 0. Driver shifted to Arboles / southwest county.

What to watch next:
- Check whether the largest day-level changes line up with wind/RH movement or public-source context.
- Check whether the LPEA active match is still a broad red-flag banner rather than direct PSPS/outage intent.
- Watch whether the highest-risk locations remain consistent across runs or the driver area is moving.
- If a PSPS occurs, log the confirmed date, location, and source so future hit-rate scoring can improve.

## PSPS Likelihood

- **PSPS means Public Safety Power Shutoff:** a planned, safety-related power shutoff LPEA may use during dangerous fire-weather conditions to reduce wildfire ignition risk. See [LPEA PSPS guidance](https://lpea.coop/psps) and the [LPEA outage center](https://lpea.coop/outage-center); if power is out, also check the [LPEA outage map](https://outage.lpea.coop).
- Overall: **WATCH** - PSPS watch screening is present from forecast thresholds or direct LPEA shutoff language; monitor official LPEA and NWS updates.
- Likely PSPS watch dates: None
- PSPS watch dates: Sun, Aug 9; Mon, Aug 10
- LPEA signal basis: LPEA active/update source contains red-flag, wildfire, or power-interruption language.
- Note: This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

| Date | PSPS likelihood | Driver locations | Weather basis |
| --- | --- | --- | --- |
| Sun, Aug 9 | WATCH | Arboles / southwest county (WATCH 50/100) | Top weather score 48/100 at Arboles / southwest county. Weather score 48/100: RH 12%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 2. |
| Mon, Aug 10 | WATCH | Arboles / southwest county (WATCH 46/100) | Top weather score 44/100 at Arboles / southwest county. Weather score 44/100: RH 15%, wind/gust 22 mph, red-flag hours 0, near-threshold hours 3. |
| Tue, Aug 11 | ELEVATED | Ignacio / southeast La Plata County (ELEVATED 28/100); Durango / La Plata County (ELEVATED 26/100); Bayfield / east La Plata County (ELEVATED 24/100) | Top weather score 28/100 at Ignacio / southeast La Plata County. Weather score 28/100: RH 18%, wind/gust 23 mph, red-flag hours 0, near-threshold hours 1. |
| Wed, Aug 12 | ELEVATED | Arboles / southwest county (ELEVATED 18/100); Bayfield / east La Plata County (ELEVATED 18/100); Ignacio / southeast La Plata County (LOW 16/100) | Top weather score 16/100 at Arboles / southwest county. Weather score 16/100: RH 23%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 0. |
| Thu, Aug 13 | ELEVATED | Durango / La Plata County (ELEVATED 20/100); Arboles / southwest county (ELEVATED 18/100); Chimney Rock / west county (ELEVATED 18/100) | Top weather score 16/100 at Arboles / southwest county. Weather score 16/100: RH 29%, wind/gust 22 mph, red-flag hours 0, near-threshold hours 0. |
| Fri, Aug 14 | ELEVATED | Durango / La Plata County (ELEVATED 20/100); Arboles / southwest county (ELEVATED 18/100); Chimney Rock / west county (ELEVATED 18/100) | Top weather score 16/100 at Arboles / southwest county. Weather score 16/100: RH 27%, wind/gust 23 mph, red-flag hours 0, near-threshold hours 0. |
| Sat, Aug 15 | ELEVATED | Arboles / southwest county (ELEVATED 24/100); Chimney Rock / west county (ELEVATED 24/100); Durango / La Plata County (ELEVATED 20/100) | Top weather score 22/100 at Arboles / southwest county. Weather score 22/100: RH 21%, wind/gust 22 mph, red-flag hours 0, near-threshold hours 0. |

## Area-Specific Outlook

| Area | Today | Peak this run | Highest-risk window |
| --- | --- | --- | --- |
| Arboles | WATCH 50/100 | Sun, Aug 9: WATCH 50/100 | 5 PM-6 PM local; 2 near/red-flag threshold hours. |
| Ignacio | ELEVATED 44/100 | Sun, Aug 9: ELEVATED 44/100 | 5 PM-6 PM local; 2 near/red-flag threshold hours. |
| Durango | ELEVATED 38/100 | Sun, Aug 9: ELEVATED 38/100 | 5 PM-5 PM local; 1 near/red-flag threshold hour. |
| Bayfield | ELEVATED 36/100 | Sun, Aug 9: ELEVATED 36/100 | 5 PM-5 PM local; 1 near/red-flag threshold hour. |
| Chimney Rock | ELEVATED 32/100 | Sun, Aug 9: ELEVATED 32/100 | Peak ingredients near 5 PM local; RH 11%, wind 20 mph. |
| Piedra | ELEVATED 28/100 | Sun, Aug 9: ELEVATED 28/100 | Peak ingredients near 9 PM local; RH 32%, wind 18 mph. |
| Chromo | ELEVATED 28/100 | Sun, Aug 9: ELEVATED 28/100 | Peak ingredients near 6 PM local; RH 16%, wind 16 mph. |
| Pagosa Springs | ELEVATED 18/100 | Mon, Aug 10: ELEVATED 26/100 | Peak ingredients near 3 PM local; RH 24%, wind 21 mph. |

## Current Fires + Evacuations

- Incident summary: 1 current wildfire reported in Archuleta County; no current evacuation notice detected in checked county feeds.
- Evacuation status: **NONE DETECTED** - No current evacuation order or warning detected in the checked official county feeds.
- Safety note: Current incidents and evacuation notices are operational context. They do not raise PSPS scores by themselves; follow official evacuation instructions immediately.

### Current NIFC Incidents

| Incident | Type | Size | Containment | Nearest monitored area | Updated |
| --- | --- | --- | --- | --- | --- |
| Rio Blanco | Wildfire | 1,387.74 acres | 79% | Chromo / southeast county (9.9 mi) | Aug 9 at 10:53 AM MDT |

Official links: [NIFC map](https://www.nifc.gov/fire-information/maps), [Archuleta County fire updates](https://sheriff.archuletacounty.gov/divisions/emergency-operations/fire-updates-and-information/), [County alerts](https://nixle.us/archuleta-county-office-of-emergency-management-aux/), [Watch Duty](https://app.watchduty.org/)

## Fire Posture + Restrictions

- Summary: 4 official sources indicate fire restrictions or staged restrictions.
- Max restriction stage detected: STAGE 2
- Max fire danger detected: VERY HIGH
- Sources reachable: 7/7
- Note: Official-source status check only; verify restrictions and burn decisions with the responsible jurisdiction.

| Jurisdiction | Restrictions | Fire danger | Source |
| --- | --- | --- | --- |
| Archuleta County | STAGE 1 | UNKNOWN | [Archuleta County Sheriff fire updates](https://sheriff.archuletacounty.gov/divisions/emergency-operations/fire-updates-and-information/) |
| Pagosa Springs | STAGE 2 | UNKNOWN | [Town of Pagosa Springs](https://www.pagosasprings.co.gov/) |
| San Juan National Forest | STAGE 1 | VERY HIGH | [San Juan National Forest fire](https://www.fs.usda.gov/r02/sanjuan/fire) |
| BLM Tres Rios | UNKNOWN | UNKNOWN | [BLM Tres Rios Field Office](https://www.blm.gov/office/tres-rios-field-office) |
| La Plata County / Durango Fire | NONE | UNKNOWN | [Durango Fire & Rescue fire conditions](https://www.durangofire.org/fire-conditions) |
| Durango | STAGE 2 | UNKNOWN | [City of Durango](https://www.durangoco.gov/) |
| Southern Ute / Ignacio | UNKNOWN | UNKNOWN | [Southern Ute Indian Tribe](https://www.southernute-nsn.gov/) |

## Forecast Calibration

### PSPS Calibration

- Summary: No confirmed LPEA PSPS events logged yet; calibration will start once events are added.
- Confirmed PSPS events logged: 0
- Candidate/unconfirmed events logged: 0
- WATCH/LIKELY false-watch past days: 53
- Pending WATCH/LIKELY dates in current forecast: Sun, Aug 9; Mon, Aug 10
- Calibration source: manual PSPS event log plus forecast history from prior monitor runs.

### Red Flag / Fire Weather Calibration

- Summary: 3/3 official Red Flag / Fire Weather episodes had a pre-alert HIGH monitor signal; date-level result was 21/21. Episode-average lead time: 3.5 days.
- Official alert episodes logged: 3 (21 alert dates)
- Episode-level pre-alert HIGH hit rate: 100%
- Date-level pre-alert HIGH hit rate: 100%
- Episode-level average lead time: 3.5 days
- HIGH false-watch past days: 20
- Pending HIGH dates in current forecast: None
- Calibration source: official NWS Red Flag / Fire Weather alert dates plus forecast history from prior monitor runs.

## Official Weather Alerts

- Monitored NWS zones: COC007, COC067, COZ019, COZ022, COZ023, COZ295
- [Air Quality Alert](https://api.weather.gov/alerts/urn:oid:2.49.0.1.840.0.cb25db9bf3233e72f4b724d2b4ebc65421e209c8.001.1): Air Quality Alert issued August 9 at 4:10PM MDT by NWS Grand Junction CO; 2026-08-09T16:10:00-06:00 to 2026-08-09T22:00:00-06:00; zones COC007, COC067
- [Air Quality Alert](https://api.weather.gov/alerts/urn:oid:2.49.0.1.840.0.eb447065089d5e1876e32a34cd983cc7d72ae17e.001.1): Air Quality Alert issued August 9 at 3:10PM MDT by NWS Grand Junction CO; 2026-08-09T15:10:00-06:00 to 2026-08-09T22:00:00-06:00; zones COC007, COC067

## LPEA Power Signal

- Status: `active_keyword_match` - LPEA active/update sources contained power-interruption keywords; review source before treating as confirmed outage intent.
- Meaning: Active source match means a monitored LPEA active/update source currently contains fire, outage, PSPS, or power-interruption keywords. Operational outages are shown separately and are not treated as PSPS/fire evidence unless the source text says so.
- Operational outage context: No active outages are listed by the official LPEA outage viewer.
- Source coverage: 13 sources; 5/5 official social sources reachable
- Evidence quality: 0 operational, 4 active/update, 0 archive/context, 6 reference source matches.
- Active/update source pages with matches: LPEA homepage (public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation, restoration); LPEA X (power outage, outage map, high winds, restore power); LPEA LinkedIn (wildfire, fire mitigation)
- Distinct active/update signals: LPEA X (power outage, outage map, high winds, restore power); LPEA X (power outage, outage map, high winds, restore power); LPEA LinkedIn (wildfire, fire mitigation); LPEA LinkedIn (wildfire, fire mitigation)
- Example signal: ...ibrary! 1 2 521 LPEA @LaPlataElectric May 7, 2024 LPEA members are experiencing power outages in the Bayfield and Pagosa Springs areas. Approximately 200 meters are out and it is suspected that the high winds are...
- Reference/context hits: [LPEA outage center](https://lpea.coop/outage-center); [LPEA wildfire / public safety power shutoffs](https://lpea.coop/psps); [LPEA red flag outage impact page](https://lpea.coop/outages/red-flag-warnings-and-impact-outages-prioritizing-safety-our-members); [LPEA fire mitigation](https://lpea.coop/fire-mitigation); [LPEA latest news](https://lpea.coop/Posts)

**Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## Next 7 Days

| Date | Tier | Main reason | Worst sampled metrics |
| --- | --- | --- | --- |
| Sun, Aug 9 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 12%, wind/gust 21 mph, thunder 3%<br>Chimney Rock / west county: RH 11%, wind/gust 20 mph, thunder 3%<br>Piedra / north county: RH 15%, wind/gust 18 mph, thunder 3% |
| Mon, Aug 10 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 15%, wind/gust 22 mph, thunder 13%<br>Chimney Rock / west county: RH 16%, wind/gust 20 mph, thunder 16%<br>Ignacio / southeast La Plata County: RH 17%, wind/gust 24 mph, thunder 10% |
| Tue, Aug 11 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 22%, wind/gust 17 mph, thunder 48%<br>Arboles / southwest county: RH 16%, wind/gust 20 mph, thunder 28%<br>Chimney Rock / west county: RH 16%, wind/gust 17 mph, thunder 37% |
| Wed, Aug 12 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 31%, wind/gust 17 mph, thunder 73%<br>Arboles / southwest county: RH 23%, wind/gust 21 mph, thunder 50%<br>Chimney Rock / west county: RH 24%, wind/gust 18 mph, thunder 64% |
| Thu, Aug 13 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 38%, wind/gust 20 mph, thunder 74%<br>Arboles / southwest county: RH 29%, wind/gust 22 mph, thunder 47%<br>Chimney Rock / west county: RH 29%, wind/gust 21 mph, thunder 62% |
| Fri, Aug 14 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 36%, wind/gust 20 mph, thunder 51%<br>Arboles / southwest county: RH 27%, wind/gust 23 mph, thunder 40%<br>Chimney Rock / west county: RH 26%, wind/gust 21 mph, thunder 46% |
| Sat, Aug 15 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 28%, wind/gust 20 mph, thunder 35%<br>Arboles / southwest county: RH 21%, wind/gust 22 mph, thunder 21%<br>Chimney Rock / west county: RH 20%, wind/gust 22 mph, thunder 30% |

## Sample Point Status

- Pagosa Springs: COZ295 (matches), forecast zone COZ023, county zone COC007
- Arboles / southwest county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Chimney Rock / west county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Piedra / north county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Chromo / southeast county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Durango / La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Bayfield / east La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Ignacio / southeast La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
