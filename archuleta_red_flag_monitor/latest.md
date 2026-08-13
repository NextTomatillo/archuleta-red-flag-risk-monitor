# Archuleta County fire-weather monitor

Generated: Aug 13, 2026 at 5:23 PM MDT (Pagosa Springs, CO local time)
Next update: Aug 14, 2026 at 5:20 AM MDT (Pagosa Springs, CO local time)
Date/time basis: Pagosa Springs, CO local time (America/Denver)
> **Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## At A Glance

- Fire-weather tier: **CONCERN**
- PSPS likelihood: **LIKELY**
- PSPS likely dates: Wed, Aug 19
- PSPS watch dates: None
- Monitor heads-up recommended: **YES** - Send this monitor report because fire-weather screening tier is CONCERN; PSPS screening level is LIKELY; a material current wildfire is reported in Archuleta County. This is not an official LPEA or NWS notice.
- HIGH dates: None
- CONCERN dates: Sat, Aug 15; Sun, Aug 16; Tue, Aug 18; Wed, Aug 19
- ELEVATED dates: None
- Official NWS Red Flag / Fire Weather alerts (COZ295): 0
- LPEA signal: `active_keyword_match` - LPEA active/update sources contained power-interruption keywords; review source before treating as confirmed outage intent.
- LPEA source coverage: 13 sources; 5/5 official social sources reachable
- Current Archuleta County wildfires: 2
- Official evacuation notices: No current evacuation order or warning detected in the checked official county feeds.
- NWS discussion: No concerning fire-weather language found in latest GJT discussion.

## Decision Support

- Summary: Highest LPEA PSPS concern is Wed, Aug 19 near Arboles / southwest county (LIKELY 66/100), driven by red-flag wind/gust signal near 25 mph; red-flag RH near 15%; 5 sampled hours are near red-flag thresholds. NIFC reports 2 current wildfires in Archuleta County.
- Confidence: **MEDIUM** (69/100) - 8/8 sampled weather points available; 7/7 fire-posture sources reachable; official NWS alert zones checked; 13/13 LPEA public sources reachable; LPEA active/update sources checked; authoritative NIFC current-incident feed checked for Archuleta County; official Archuleta County evacuation feeds checked; forecast changed substantially versus prior run; no confirmed PSPS events logged yet for calibration
- Weather fire-potential peak: Wed, Aug 19: Arboles / southwest county VERY HIGH 82/100
- Red Flag likelihood peak: Wed, Aug 19: Arboles / southwest county LIKELY 77/100
- LPEA PSPS peak: Wed, Aug 19: Arboles / southwest county LIKELY 66/100
- Method: rules-based decision support using public weather, fire-posture, and LPEA source signals; scores are screening estimates, not official or statistically calibrated probabilities.

| Date | Weather fire potential | Red Flag likelihood | LPEA PSPS | Main window |
| --- | --- | --- | --- | --- |
| Thu, Aug 13 | Durango / La Plata County: MODERATE 36/100 | Durango / La Plata County: LOW 8/100 | Durango / La Plata County: ELEVATED 20/100 | Peak ingredients near 5 PM local; RH 37%, wind 22 mph. |
| Fri, Aug 14 | Durango / La Plata County: MODERATE 36/100 | Durango / La Plata County: LOW 8/100 | Durango / La Plata County: ELEVATED 20/100 | Peak ingredients near 3 PM local; RH 32%, wind 21 mph. |
| Sat, Aug 15 | Chimney Rock / west county: HIGH 62/100 | Chimney Rock / west county: POSSIBLE 50/100 | Chimney Rock / west county: ELEVATED 40/100 | 4 PM-5 PM local; 2 near/red-flag threshold hours. |
| Sun, Aug 16 | Chimney Rock / west county: HIGH 62/100 | Arboles / southwest county: POSSIBLE 50/100 | Arboles / southwest county: ELEVATED 40/100 | 3 PM-5 PM local; 3 near/red-flag threshold hours. |
| Mon, Aug 17 | Durango / La Plata County: LOW 32/100 | Arboles / southwest county: LOW 8/100 | Arboles / southwest county: ELEVATED 24/100 | Peak ingredients near 4 PM local; RH 19%, wind 21 mph. |
| Tue, Aug 18 | Chimney Rock / west county: HIGH 64/100 | Chimney Rock / west county: POSSIBLE 54/100 | Arboles / southwest county: ELEVATED 44/100 | 3 PM-6 PM local; 4 near/red-flag threshold hours. |
| Wed, Aug 19 | Arboles / southwest county: VERY HIGH 82/100 | Arboles / southwest county: LIKELY 77/100 | Arboles / southwest county: LIKELY 66/100 | 2 PM-6 PM local; 5 near/red-flag threshold hours. |

## Analyst Interpretation

- Headline: Screening rises to CONCERN with a Wednesday PSPS LIKELY outlook near Arboles; no official COZ295 alert or LPEA outage is active.
- Summary: Wednesday is the screening peak near Arboles: PSPS LIKELY 66/100 and Red Flag LIKELY 77/100, with RH near 15%, wind near 25 mph, and five near-threshold hours. Saturday, Sunday, Tuesday, and Wednesday are CONCERN dates. Official checks show zero COZ295 fire alerts and no active LPEA outages; county feeds show no evacuation notice.
- Uncertainty: No confirmed LPEA PSPS events are logged, and 56 prior WATCH/LIKELY dates did not become confirmed events. Wednesday remains a screening estimate with MEDIUM 69/100 confidence and HIGH forecast volatility.
- Evidence used: overall_status, weather_peaks, official_alerts, forecast_change, lpea_context, fire_posture, active_incidents, calibration
- This interpretation cannot change the deterministic tiers, scores, official alerts, or notification decision.

Changing drivers:
- The area-wide PSPS screening level rose from WATCH to LIKELY; Wednesday's PSPS score increased 16 points.
- Sunday, Monday, and Tuesday also worsened versus the prior run, with Arboles becoming the primary driver.
- Official-source fire posture remains Stage 2 with VERY HIGH fire danger.
- Rio Blanco is about 1,388 acres and 97% contained; Gunsight is 0.10 acre, with no evacuation notice detected.

What to watch next:
- Recheck Wednesday near Arboles for an official NWS alert, LPEA notice, or further threshold shift.
- Monitor the Saturday, Sunday, and Tuesday CONCERN windows for worsening wind, humidity, or thunder overlap.
- Treat the LPEA keyword match as broad public-source context unless direct outage or PSPS intent appears.
- Continue checking Rio Blanco, Gunsight, and county evacuation feeds for operational changes.

## Trend Intelligence

- Summary: Momentum is rising versus the prior run (Aug 13 at 5:26 AM MDT); forecast volatility is high and first WATCH-or-higher date is Wed, Aug 19.
- Momentum: **Rising**
- Forecast volatility: **HIGH** (53/100)
- First WATCH-or-higher PSPS date: Wed, Aug 19
- Watch-date movement: First WATCH-or-higher PSPS date remains Wed, Aug 19.
- Method: compares current forecast evidence against prior local forecast history.

Notable changes:
- First WATCH-or-higher PSPS date remains Wed, Aug 19.
- Overall PSPS likelihood changed from WATCH to LIKELY.
- Wed, Aug 19: worsening vs prior run; PSPS WATCH -> LIKELY; score +16, wind +2 mph, RH +1%, red-flag hours +1.
- Mon, Aug 17: worsening vs prior run; PSPS LOW -> ELEVATED; score +8, wind +2 mph, RH -2%, red-flag hours 0.
- Sun, Aug 16: worsening vs prior run; PSPS ELEVATED -> ELEVATED; score +14, wind +1 mph, RH -2%, red-flag hours 0. Driver shifted to Arboles / southwest county.
- Tue, Aug 18: worsening vs prior run; PSPS ELEVATED -> ELEVATED; score +10, wind +2 mph, RH 0%, red-flag hours 0.

## Public Analysis Export

- Summary: Highest LPEA PSPS concern is Wed, Aug 19 near Arboles / southwest county (LIKELY 66/100), driven by red-flag wind/gust signal near 25 mph; red-flag RH near 15%; 5 sampled hours are near red-flag thresholds. NIFC reports 2 current wildfires in Archuleta County.
- Trend: Momentum is rising versus the prior run (Aug 13 at 5:26 AM MDT); forecast volatility is high and first WATCH-or-higher date is Wed, Aug 19.
- Confidence: **MEDIUM** (69/100)
- First WATCH-or-higher PSPS date: Wed, Aug 19
- PSPS peak: Wed, Aug 19 near Arboles / southwest county at LIKELY 66/100
- Red Flag peak: Wed, Aug 19 near Arboles / southwest county at LIKELY 77/100
- Weather fire-potential peak: Wed, Aug 19 near Arboles / southwest county at VERY HIGH 82/100
- LPEA operational outage context: No active outages are listed by the official LPEA outage viewer.
- Public JSON: `archuleta_red_flag_monitor/public_analysis_export.json`

What changed:
- First WATCH-or-higher PSPS date remains Wed, Aug 19.
- Overall PSPS likelihood changed from WATCH to LIKELY.
- Wed, Aug 19: worsening vs prior run; PSPS WATCH -> LIKELY; score +16, wind +2 mph, RH +1%, red-flag hours +1.
- Mon, Aug 17: worsening vs prior run; PSPS LOW -> ELEVATED; score +8, wind +2 mph, RH -2%, red-flag hours 0.
- Sun, Aug 16: worsening vs prior run; PSPS ELEVATED -> ELEVATED; score +14, wind +1 mph, RH -2%, red-flag hours 0. Driver shifted to Arboles / southwest county.
- Tue, Aug 18: worsening vs prior run; PSPS ELEVATED -> ELEVATED; score +10, wind +2 mph, RH 0%, red-flag hours 0.

What to watch next:
- Check whether the largest day-level changes line up with wind/RH movement or public-source context.
- Check whether the LPEA active match is still a broad red-flag banner rather than direct PSPS/outage intent.
- Watch whether the highest-risk locations remain consistent across runs or the driver area is moving.
- If a PSPS occurs, log the confirmed date, location, and source so future hit-rate scoring can improve.

## PSPS Likelihood

- **PSPS means Public Safety Power Shutoff:** a planned, safety-related power shutoff LPEA may use during dangerous fire-weather conditions to reduce wildfire ignition risk. See [LPEA PSPS guidance](https://lpea.coop/psps) and the [LPEA outage center](https://lpea.coop/outage-center); if power is out, also check the [LPEA outage map](https://outage.lpea.coop).
- Overall: **LIKELY** - PSPS likelihood is high on weather-driven red-flag days; prepare for possible LPEA safety-related interruption behavior.
- Likely PSPS watch dates: Wed, Aug 19
- PSPS watch dates: None
- LPEA signal basis: LPEA active/update source contains red-flag, wildfire, or power-interruption language.
- Note: This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

| Date | PSPS likelihood | Driver locations | Weather basis |
| --- | --- | --- | --- |
| Thu, Aug 13 | ELEVATED | Durango / La Plata County (ELEVATED 20/100); Arboles / southwest county (ELEVATED 18/100); Bayfield / east La Plata County (ELEVATED 18/100) | Top weather score 16/100 at Arboles / southwest county. Weather score 16/100: RH 34%, wind/gust 22 mph, red-flag hours 0, near-threshold hours 0. |
| Fri, Aug 14 | ELEVATED | Durango / La Plata County (ELEVATED 20/100); Arboles / southwest county (ELEVATED 18/100); Chimney Rock / west county (ELEVATED 18/100) | Top weather score 16/100 at Arboles / southwest county. Weather score 16/100: RH 28%, wind/gust 22 mph, red-flag hours 0, near-threshold hours 0. |
| Sat, Aug 15 | ELEVATED | Chimney Rock / west county (ELEVATED 40/100); Durango / La Plata County (ELEVATED 26/100); Arboles / southwest county (ELEVATED 24/100) | Top weather score 38/100 at Chimney Rock / west county. Weather score 38/100: RH 18%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 2. |
| Sun, Aug 16 | ELEVATED | Arboles / southwest county (ELEVATED 40/100); Chimney Rock / west county (ELEVATED 40/100); Durango / La Plata County (ELEVATED 26/100) | Top weather score 38/100 at Arboles / southwest county. Weather score 38/100: RH 18%, wind/gust 22 mph, red-flag hours 0, near-threshold hours 3. |
| Mon, Aug 17 | ELEVATED | Arboles / southwest county (ELEVATED 24/100); Ignacio / southeast La Plata County (ELEVATED 22/100); Chimney Rock / west county (ELEVATED 22/100) | Top weather score 22/100 at Arboles / southwest county. Weather score 22/100: RH 19%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 0. |
| Tue, Aug 18 | ELEVATED | Arboles / southwest county (ELEVATED 44/100); Chimney Rock / west county (ELEVATED 44/100); Durango / La Plata County (ELEVATED 26/100) | Top weather score 42/100 at Arboles / southwest county. Weather score 42/100: RH 17%, wind/gust 23 mph, red-flag hours 0, near-threshold hours 4. |
| Wed, Aug 19 | LIKELY | Arboles / southwest county (LIKELY 66/100); Chimney Rock / west county (WATCH 50/100); Ignacio / southeast La Plata County (WATCH 47/100) | Top weather score 64/100 at Arboles / southwest county. Weather score 64/100: RH 15%, wind/gust 25 mph, red-flag hours 1, near-threshold hours 5. |

## Area-Specific Outlook

| Area | Today | Peak this run | Highest-risk window |
| --- | --- | --- | --- |
| Arboles | ELEVATED 18/100 | Wed, Aug 19: LIKELY 66/100 | 2 PM-6 PM local; 5 near/red-flag threshold hours. |
| Chimney Rock | LOW 10/100 | Wed, Aug 19: WATCH 50/100 | 2 PM-6 PM local; 5 near/red-flag threshold hours. |
| Ignacio | LOW 16/100 | Wed, Aug 19: WATCH 47/100 | 3 PM-5 PM local; 3 near/red-flag threshold hours. |
| Durango | ELEVATED 20/100 | Wed, Aug 19: ELEVATED 42/100 | 4 PM-5 PM local; 2 near/red-flag threshold hours. |
| Bayfield | ELEVATED 18/100 | Wed, Aug 19: ELEVATED 39/100 | 4 PM-4 PM local; 1 near/red-flag threshold hour. |
| Pagosa Springs | LOW 12/100 | Wed, Aug 19: ELEVATED 26/100 | Peak ingredients near 4 PM local; RH 22%, wind 22 mph. |
| Chromo | LOW 10/100 | Tue, Aug 18: LOW 16/100 | Peak ingredients near 5 PM local; RH 22%, wind 18 mph. |
| Piedra | LOW 10/100 | Thu, Aug 13: LOW 10/100 | Peak ingredients near 5 PM local; RH 45%, wind 16 mph. |

## Current Fires + Evacuations

- Incident summary: 2 current wildfires reported in Archuleta County; no current evacuation notice detected in checked county feeds.
- Evacuation status: **NONE DETECTED** - No current evacuation order or warning detected in the checked official county feeds.
- Safety note: Current incidents and evacuation notices are operational context. They do not raise PSPS scores by themselves; follow official evacuation instructions immediately.

### Current NIFC Incidents

| Incident | Type | Size | Containment | Nearest monitored area | Updated |
| --- | --- | --- | --- | --- | --- |
| Rio Blanco | Wildfire | 1,387.74 acres | 97% | Chromo / southeast county (9.9 mi) | Aug 13 at 4:30 PM MDT |
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
| Thu, Aug 13 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 45%, wind/gust 18 mph, thunder 41%<br>Arboles / southwest county: RH 34%, wind/gust 22 mph, thunder 19%<br>Chimney Rock / west county: RH 34%, wind/gust 20 mph, thunder 30% |
| Fri, Aug 14 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 34%, wind/gust 18 mph, thunder 36%<br>Arboles / southwest county: RH 28%, wind/gust 22 mph, thunder 21%<br>Chimney Rock / west county: RH 26%, wind/gust 21 mph, thunder 29% |
| Sat, Aug 15 | CONCERN | Chimney Rock / west county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Chimney Rock / west county: RH 18%, wind/gust 21 mph, thunder 5% |
| Sun, Aug 16 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 18%, wind/gust 22 mph, thunder 7%<br>Chimney Rock / west county: RH 16%, wind/gust 21 mph, thunder 10% |
| Mon, Aug 17 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 26%, wind/gust 17 mph, thunder 34%<br>Arboles / southwest county: RH 19%, wind/gust 21 mph, thunder 31%<br>Chimney Rock / west county: RH 18%, wind/gust 20 mph, thunder 30% |
| Tue, Aug 18 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 17%, wind/gust 23 mph, thunder 11%<br>Chimney Rock / west county: RH 16%, wind/gust 22 mph, thunder 15% |
| Wed, Aug 19 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 15%, wind/gust 25 mph, thunder 25%<br>Chimney Rock / west county: RH 15%, wind/gust 23 mph, thunder 25%<br>Durango / La Plata County: RH 18%, wind/gust 24 mph, thunder 31% |

## Sample Point Status

- Pagosa Springs: COZ295 (matches), forecast zone COZ023, county zone COC007
- Arboles / southwest county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Chimney Rock / west county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Piedra / north county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Chromo / southeast county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Durango / La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Bayfield / east La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Ignacio / southeast La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
