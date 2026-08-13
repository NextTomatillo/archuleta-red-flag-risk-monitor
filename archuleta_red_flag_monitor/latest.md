# Archuleta County fire-weather monitor

Generated: Aug 13, 2026 at 5:26 AM MDT (Pagosa Springs, CO local time)
Next update: Aug 13, 2026 at 5:20 PM MDT (Pagosa Springs, CO local time)
Date/time basis: Pagosa Springs, CO local time (America/Denver)
> **Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## At A Glance

- Fire-weather tier: **CONCERN**
- PSPS likelihood: **WATCH**
- PSPS likely dates: None
- PSPS watch dates: Wed, Aug 19
- Monitor heads-up recommended: **YES** - Send this monitor report because fire-weather screening tier is CONCERN; PSPS screening level is WATCH; a material current wildfire is reported in Archuleta County. This is not an official LPEA or NWS notice.
- HIGH dates: None
- CONCERN dates: Sat, Aug 15; Wed, Aug 19
- ELEVATED dates: Sun, Aug 16; Tue, Aug 18
- Official NWS Red Flag / Fire Weather alerts (COZ295): 0
- LPEA signal: `active_keyword_match` - LPEA active/update sources contained power-interruption keywords; review source before treating as confirmed outage intent.
- LPEA source coverage: 13 sources; 5/5 official social sources reachable
- Current Archuleta County wildfires: 2
- Official evacuation notices: No current evacuation order or warning detected in the checked official county feeds.
- NWS discussion: No concerning fire-weather language found in latest GJT discussion.

## Decision Support

- Summary: Highest LPEA PSPS concern is Wed, Aug 19 near Arboles / southwest county (WATCH 50/100), driven by near-threshold wind/gust signal near 23 mph; red-flag RH near 15%; 4 sampled hours are near red-flag thresholds. NIFC reports 2 current wildfires in Archuleta County.
- Confidence: **MEDIUM** (74/100) - 8/8 sampled weather points available; 7/7 fire-posture sources reachable; official NWS alert zones checked; 13/13 LPEA public sources reachable; LPEA active/update sources checked; authoritative NIFC current-incident feed checked for Archuleta County; official Archuleta County evacuation feeds checked; forecast changed moderately versus prior run; no confirmed PSPS events logged yet for calibration
- Weather fire-potential peak: Wed, Aug 19: Durango / La Plata County HIGH 68/100
- Red Flag likelihood peak: Wed, Aug 19: Arboles / southwest county WATCH 58/100
- LPEA PSPS peak: Wed, Aug 19: Arboles / southwest county WATCH 50/100
- Method: rules-based decision support using public weather, fire-posture, and LPEA source signals; scores are screening estimates, not official or statistically calibrated probabilities.

| Date | Weather fire potential | Red Flag likelihood | LPEA PSPS | Main window |
| --- | --- | --- | --- | --- |
| Thu, Aug 13 | Durango / La Plata County: MODERATE 36/100 | Durango / La Plata County: LOW 8/100 | Durango / La Plata County: ELEVATED 20/100 | Peak ingredients near 4 PM local; RH 32%, wind 23 mph. |
| Fri, Aug 14 | Durango / La Plata County: MODERATE 36/100 | Durango / La Plata County: LOW 8/100 | Durango / La Plata County: ELEVATED 20/100 | Peak ingredients near 3 PM local; RH 30%, wind 23 mph. |
| Sat, Aug 15 | Chimney Rock / west county: HIGH 62/100 | Chimney Rock / west county: POSSIBLE 50/100 | Chimney Rock / west county: ELEVATED 40/100 | 4 PM-5 PM local; 2 near/red-flag threshold hours. |
| Sun, Aug 16 | Durango / La Plata County: MODERATE 44/100 | Chimney Rock / west county: LOW 25/100 | Chimney Rock / west county: ELEVATED 26/100 | Peak ingredients near 3 PM local; RH 18%, wind 20 mph. |
| Mon, Aug 17 | Chimney Rock / west county: LOW 26/100 | Arboles / southwest county: LOW 0/100 | Arboles / southwest county: LOW 16/100 | Peak ingredients near 3 PM local; RH 21%, wind 18 mph. |
| Tue, Aug 18 | Durango / La Plata County: MODERATE 44/100 | Arboles / southwest county: LOW 25/100 | Arboles / southwest county: ELEVATED 34/100 | 4 PM-4 PM local; 1 near/red-flag threshold hour. |
| Wed, Aug 19 | Durango / La Plata County: HIGH 68/100 | Arboles / southwest county: WATCH 58/100 | Arboles / southwest county: WATCH 50/100 | 3 PM-6 PM local; 4 near/red-flag threshold hours. |

## Analyst Interpretation

- Headline: Screening rises to CONCERN with a Wednesday PSPS WATCH near Arboles; official sources show no COZ295 alert, LPEA outage, or evacuation notice.
- Summary: Wednesday is the screening peak: PSPS WATCH 50/100 and Red Flag WATCH 58/100 near Arboles, with RH near 15%, wind near 23 mph, and four near-threshold hours. Saturday is also a CONCERN day near Chimney Rock, but official sources report zero COZ295 fire alerts and no active LPEA outages. Rio Blanco remains about 1,388 acres and 91% contained; Gunsight remains 0.10 acre, and no evacuation notice was detected.
- Uncertainty: No confirmed LPEA PSPS events are logged; 56 prior WATCH/LIKELY days became false watches, so Wednesday's WATCH remains a screening estimate despite MEDIUM 74/100 confidence.
- Evidence used: overall_status, weather_peaks, official_alerts, forecast_change, lpea_context, fire_posture, active_incidents, calibration
- This interpretation cannot change the deterministic tiers, scores, official alerts, or notification decision.

Changing drivers:
- The first WATCH-or-higher PSPS date appeared on Wednesday, Aug. 19, raising the overall PSPS screen from ELEVATED to WATCH.
- Saturday worsened by 16 points but remains PSPS ELEVATED near Chimney Rock.
- Official fire posture remains Stage 2 with VERY HIGH fire danger.
- Two current wildfires are reported, with no evacuation notice detected.

What to watch next:
- Recheck Wednesday near Arboles for threshold changes or an official NWS or LPEA notice.
- Monitor Saturday near Chimney Rock as RH and wind approach red-flag screening levels.
- Check the official LPEA outage viewer; the current keyword match is broad context, not confirmed outage or PSPS intent.
- Monitor Rio Blanco, Gunsight, and official county evacuation feeds.

## Trend Intelligence

- Summary: Momentum is rising versus the prior run (Aug 12 at 6:11 PM MDT); forecast volatility is medium and first WATCH-or-higher date is Wed, Aug 19.
- Momentum: **Rising**
- Forecast volatility: **MEDIUM** (21/100)
- First WATCH-or-higher PSPS date: Wed, Aug 19
- Watch-date movement: First WATCH-or-higher PSPS date appeared at Wed, Aug 19.
- Method: compares current forecast evidence against prior local forecast history.

Notable changes:
- First WATCH-or-higher PSPS date appeared at Wed, Aug 19.
- Overall PSPS likelihood changed from ELEVATED to WATCH.
- Sat, Aug 15: worsening vs prior run; PSPS ELEVATED -> ELEVATED; score +16, wind +1 mph, RH -2%, red-flag hours 0. Driver shifted to Chimney Rock / west county.

## Public Analysis Export

- Summary: Highest LPEA PSPS concern is Wed, Aug 19 near Arboles / southwest county (WATCH 50/100), driven by near-threshold wind/gust signal near 23 mph; red-flag RH near 15%; 4 sampled hours are near red-flag thresholds. NIFC reports 2 current wildfires in Archuleta County.
- Trend: Momentum is rising versus the prior run (Aug 12 at 6:11 PM MDT); forecast volatility is medium and first WATCH-or-higher date is Wed, Aug 19.
- Confidence: **MEDIUM** (74/100)
- First WATCH-or-higher PSPS date: Wed, Aug 19
- PSPS peak: Wed, Aug 19 near Arboles / southwest county at WATCH 50/100
- Red Flag peak: Wed, Aug 19 near Arboles / southwest county at WATCH 58/100
- Weather fire-potential peak: Wed, Aug 19 near Durango / La Plata County at HIGH 68/100
- LPEA operational outage context: No active outages are listed by the official LPEA outage viewer.
- Public JSON: `archuleta_red_flag_monitor/public_analysis_export.json`

What changed:
- First WATCH-or-higher PSPS date appeared at Wed, Aug 19.
- Overall PSPS likelihood changed from ELEVATED to WATCH.
- Sat, Aug 15: worsening vs prior run; PSPS ELEVATED -> ELEVATED; score +16, wind +1 mph, RH -2%, red-flag hours 0. Driver shifted to Chimney Rock / west county.

What to watch next:
- Check whether the largest day-level changes line up with wind/RH movement or public-source context.
- Check whether the LPEA active match is still a broad red-flag banner rather than direct PSPS/outage intent.
- Watch whether the highest-risk locations remain consistent across runs or the driver area is moving.
- If a PSPS occurs, log the confirmed date, location, and source so future hit-rate scoring can improve.

## PSPS Likelihood

- **PSPS means Public Safety Power Shutoff:** a planned, safety-related power shutoff LPEA may use during dangerous fire-weather conditions to reduce wildfire ignition risk. See [LPEA PSPS guidance](https://lpea.coop/psps) and the [LPEA outage center](https://lpea.coop/outage-center); if power is out, also check the [LPEA outage map](https://outage.lpea.coop).
- Overall: **WATCH** - PSPS watch screening is present from forecast thresholds or direct LPEA shutoff language; monitor official LPEA and NWS updates.
- Likely PSPS watch dates: None
- PSPS watch dates: Wed, Aug 19
- LPEA signal basis: LPEA active/update source contains red-flag, wildfire, or power-interruption language.
- Note: This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

| Date | PSPS likelihood | Driver locations | Weather basis |
| --- | --- | --- | --- |
| Thu, Aug 13 | ELEVATED | Durango / La Plata County (ELEVATED 20/100); Arboles / southwest county (ELEVATED 18/100); Chimney Rock / west county (ELEVATED 18/100) | Top weather score 16/100 at Arboles / southwest county. Weather score 16/100: RH 29%, wind/gust 23 mph, red-flag hours 0, near-threshold hours 0. |
| Fri, Aug 14 | ELEVATED | Durango / La Plata County (ELEVATED 20/100); Arboles / southwest county (ELEVATED 18/100); Chimney Rock / west county (ELEVATED 18/100) | Top weather score 16/100 at Arboles / southwest county. Weather score 16/100: RH 26%, wind/gust 23 mph, red-flag hours 0, near-threshold hours 0. |
| Sat, Aug 15 | ELEVATED | Chimney Rock / west county (ELEVATED 40/100); Arboles / southwest county (ELEVATED 24/100); Ignacio / southeast La Plata County (ELEVATED 22/100) | Top weather score 38/100 at Chimney Rock / west county. Weather score 38/100: RH 18%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 2. |
| Sun, Aug 16 | ELEVATED | Chimney Rock / west county (ELEVATED 26/100); Durango / La Plata County (ELEVATED 26/100); Arboles / southwest county (ELEVATED 24/100) | Top weather score 24/100 at Chimney Rock / west county. Weather score 24/100: RH 18%, wind/gust 20 mph, red-flag hours 0, near-threshold hours 0. |
| Mon, Aug 17 | LOW | Arboles / southwest county (LOW 16/100); Chimney Rock / west county (LOW 16/100); Pagosa Springs (LOW 12/100) | Top weather score 14/100 at Arboles / southwest county. Weather score 14/100: RH 21%, wind/gust 18 mph, red-flag hours 0, near-threshold hours 0. |
| Tue, Aug 18 | ELEVATED | Arboles / southwest county (ELEVATED 34/100); Chimney Rock / west county (ELEVATED 26/100); Durango / La Plata County (ELEVATED 26/100) | Top weather score 32/100 at Arboles / southwest county. Weather score 32/100: RH 17%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 1. |
| Wed, Aug 19 | WATCH | Arboles / southwest county (WATCH 50/100) | Top weather score 48/100 at Arboles / southwest county. Weather score 48/100: RH 15%, wind/gust 23 mph, red-flag hours 0, near-threshold hours 4. |

## Area-Specific Outlook

| Area | Today | Peak this run | Highest-risk window |
| --- | --- | --- | --- |
| Arboles | ELEVATED 18/100 | Wed, Aug 19: WATCH 50/100 | 3 PM-6 PM local; 4 near/red-flag threshold hours. |
| Bayfield | ELEVATED 18/100 | Wed, Aug 19: ELEVATED 44/100 | 4 PM-5 PM local; 2 near/red-flag threshold hours. |
| Durango | ELEVATED 20/100 | Wed, Aug 19: ELEVATED 42/100 | 4 PM-5 PM local; 2 near/red-flag threshold hours. |
| Ignacio | LOW 16/100 | Wed, Aug 19: ELEVATED 42/100 | 3 PM-6 PM local; 4 near/red-flag threshold hours. |
| Chimney Rock | ELEVATED 18/100 | Sat, Aug 15: ELEVATED 40/100 | 4 PM-5 PM local; 2 near/red-flag threshold hours. |
| Pagosa Springs | LOW 12/100 | Wed, Aug 19: ELEVATED 18/100 | Peak ingredients near 4 PM local; RH 21%, wind 20 mph. |
| Piedra | LOW 10/100 | Wed, Aug 19: LOW 16/100 | Peak ingredients near 4 PM local; RH 22%, wind 18 mph. |
| Chromo | LOW 10/100 | Wed, Aug 19: LOW 16/100 | Peak ingredients near 4 PM local; RH 21%, wind 16 mph. |

## Current Fires + Evacuations

- Incident summary: 2 current wildfires reported in Archuleta County; no current evacuation notice detected in checked county feeds.
- Evacuation status: **NONE DETECTED** - No current evacuation order or warning detected in the checked official county feeds.
- Safety note: Current incidents and evacuation notices are operational context. They do not raise PSPS scores by themselves; follow official evacuation instructions immediately.

### Current NIFC Incidents

| Incident | Type | Size | Containment | Nearest monitored area | Updated |
| --- | --- | --- | --- | --- | --- |
| Rio Blanco | Wildfire | 1,387.74 acres | 91% | Chromo / southeast county (9.9 mi) | Aug 11 at 4:14 PM MDT |
| Gunsight | Wildfire | 0.10 acres | Not reported | Pagosa Springs (15.4 mi) | Aug 12 at 2:17 PM MDT |

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
- WATCH/LIKELY false-watch past days: 56
- Pending WATCH/LIKELY dates in current forecast: Wed, Aug 19
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
- No active official NWS Red Flag / Fire Weather or related weather alerts found for monitored zones.

## LPEA Power Signal

- Status: `active_keyword_match` - LPEA active/update sources contained power-interruption keywords; review source before treating as confirmed outage intent.
- Meaning: Active source match means a monitored LPEA active/update source currently contains fire, outage, PSPS, or power-interruption keywords. Operational outages are shown separately and are not treated as PSPS/fire evidence unless the source text says so.
- Operational outage context: No active outages are listed by the official LPEA outage viewer.
- Source coverage: 13 sources; 5/5 official social sources reachable
- Evidence quality: 0 operational, 4 active/update, 0 archive/context, 6 reference source matches.
- Active/update source pages with matches: LPEA homepage (public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation, restoration); LPEA X (power outage, outage map, high winds, restore power); LPEA LinkedIn (wildfire, fire mitigation)
- Distinct active/update signals: LPEA X (power outage, outage map, high winds, restore power); LPEA X (power outage, outage map, high winds, restore power); LPEA LinkedIn (wildfire, fire mitigation); LPEA LinkedIn (wildfire, fire mitigation)
- Example signal: ...ibrary! 1 2 522 LPEA @LaPlataElectric May 7, 2024 LPEA members are experiencing power outages in the Bayfield and Pagosa Springs areas. Approximately 200 meters are out and it is suspected that the high winds are...
- Reference/context hits: [LPEA outage center](https://lpea.coop/outage-center); [LPEA wildfire / public safety power shutoffs](https://lpea.coop/psps); [LPEA red flag outage impact page](https://lpea.coop/outages/red-flag-warnings-and-impact-outages-prioritizing-safety-our-members); [LPEA fire mitigation](https://lpea.coop/fire-mitigation); [LPEA latest news](https://lpea.coop/Posts)

**Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## Next 7 Days

| Date | Tier | Main reason | Worst sampled metrics |
| --- | --- | --- | --- |
| Thu, Aug 13 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 37%, wind/gust 20 mph, thunder 53%<br>Arboles / southwest county: RH 29%, wind/gust 23 mph, thunder 23%<br>Chimney Rock / west county: RH 28%, wind/gust 21 mph, thunder 37% |
| Fri, Aug 14 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 33%, wind/gust 20 mph, thunder 41%<br>Arboles / southwest county: RH 26%, wind/gust 23 mph, thunder 14%<br>Chimney Rock / west county: RH 24%, wind/gust 21 mph, thunder 29% |
| Sat, Aug 15 | CONCERN | Chimney Rock / west county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Chimney Rock / west county: RH 18%, wind/gust 21 mph, thunder 7% |
| Sun, Aug 16 | ELEVATED | Chimney Rock / west county: Elevated ingredient present: dry-thunder probability reaches 18%. | Chimney Rock / west county: RH 18%, wind/gust 20 mph, thunder 29% |
| Mon, Aug 17 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 29%, wind/gust 17 mph, thunder 50%<br>Arboles / southwest county: RH 21%, wind/gust 18 mph, thunder 27%<br>Chimney Rock / west county: RH 20%, wind/gust 18 mph, thunder 38% |
| Tue, Aug 18 | ELEVATED | Arboles / southwest county: Elevated ingredient present: dry-thunder probability reaches 15%. | Arboles / southwest county: RH 17%, wind/gust 21 mph, thunder 15%<br>Chimney Rock / west county: RH 16%, wind/gust 18 mph, thunder 16% |
| Wed, Aug 19 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 15%, wind/gust 23 mph, thunder 30%<br>Chimney Rock / west county: RH 14%, wind/gust 20 mph, thunder 31%<br>Durango / La Plata County: RH 17%, wind/gust 22 mph, thunder 35% |

## Sample Point Status

- Pagosa Springs: COZ295 (matches), forecast zone COZ023, county zone COC007
- Arboles / southwest county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Chimney Rock / west county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Piedra / north county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Chromo / southeast county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Durango / La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Bayfield / east La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Ignacio / southeast La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
