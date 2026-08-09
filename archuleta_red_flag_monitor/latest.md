# Archuleta County fire-weather monitor

Generated: Aug 8, 2026 at 5:38 PM MDT (Pagosa Springs, CO local time)
Next update: Aug 9, 2026 at 5:20 AM MDT (Pagosa Springs, CO local time)
Date/time basis: Pagosa Springs, CO local time (America/Denver)
> **Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## At A Glance

- Fire-weather tier: **CONCERN**
- PSPS likelihood: **WATCH**
- PSPS likely dates: None
- PSPS watch dates: Sun, Aug 9; Mon, Aug 10
- Monitor heads-up recommended: **YES** - Send this monitor report because fire-weather screening tier is CONCERN; PSPS screening level is WATCH; a material current wildfire is reported in Archuleta County. This is not an official LPEA or NWS notice.
- HIGH dates: None
- CONCERN dates: Sun, Aug 9; Mon, Aug 10; Tue, Aug 11
- ELEVATED dates: Sat, Aug 8; Fri, Aug 14
- Official NWS Red Flag / Fire Weather alerts (COZ295): 0
- LPEA signal: `active_keyword_match` - LPEA active/update sources contained power-interruption keywords; review source before treating as confirmed outage intent.
- LPEA source coverage: 13 sources; 5/5 official social sources reachable
- Current Archuleta County wildfires: 1
- Official evacuation notices: No current evacuation order or warning detected in the checked official county feeds.
- NWS discussion: No concerning fire-weather language found in latest GJT discussion.

## Decision Support

- Summary: Highest LPEA PSPS concern is Mon, Aug 10 near Ignacio / southeast La Plata County (WATCH 51/100), driven by red-flag wind/gust signal near 25 mph; near-threshold RH near 16%; 3 sampled hours are near red-flag thresholds. NIFC reports 1 current wildfire in Archuleta County.
- Confidence: **HIGH** (77/100) - 8/8 sampled weather points available; 7/7 fire-posture sources reachable; official NWS alert zones checked; 13/13 LPEA public sources reachable; LPEA active/update sources checked; authoritative NIFC current-incident feed checked for Archuleta County; official Archuleta County evacuation feeds checked; no confirmed PSPS events logged yet for calibration
- Weather fire-potential peak: Sun, Aug 9: Durango / La Plata County VERY HIGH 77/100
- Red Flag likelihood peak: Mon, Aug 10: Ignacio / southeast La Plata County WATCH 60/100
- LPEA PSPS peak: Mon, Aug 10: Ignacio / southeast La Plata County WATCH 51/100
- Method: rules-based decision support using public weather, fire-posture, and LPEA source signals; scores are screening estimates, not official or statistically calibrated probabilities.

| Date | Weather fire potential | Red Flag likelihood | LPEA PSPS | Main window |
| --- | --- | --- | --- | --- |
| Sat, Aug 8 | Pagosa Springs: MODERATE 52/100 | Arboles / southwest county: LOW 25/100 | Arboles / southwest county: ELEVATED 32/100 | Peak ingredients near 5 PM local; RH 10%, wind 16 mph. |
| Sun, Aug 9 | Durango / La Plata County: VERY HIGH 77/100 | Ignacio / southeast La Plata County: WATCH 59/100 | Durango / La Plata County: WATCH 48/100 | 3 PM-5 PM local; 3 near/red-flag threshold hours. |
| Mon, Aug 10 | Arboles / southwest county: HIGH 61/100 | Ignacio / southeast La Plata County: WATCH 60/100 | Ignacio / southeast La Plata County: WATCH 51/100 | 2 PM-4 PM local; 3 near/red-flag threshold hours. |
| Tue, Aug 11 | Arboles / southwest county: HIGH 55/100 | Arboles / southwest county: POSSIBLE 50/100 | Arboles / southwest county: ELEVATED 40/100 | 3 PM-4 PM local; 2 near/red-flag threshold hours. |
| Wed, Aug 12 | Chimney Rock / west county: MODERATE 38/100 | Arboles / southwest county: LOW 8/100 | Arboles / southwest county: ELEVATED 24/100 | Peak ingredients near 4 PM local; RH 22%, wind 23 mph. |
| Thu, Aug 13 | Durango / La Plata County: MODERATE 36/100 | Durango / La Plata County: LOW 8/100 | Durango / La Plata County: ELEVATED 20/100 | Peak ingredients near 3 PM local; RH 34%, wind 21 mph. |
| Fri, Aug 14 | Durango / La Plata County: MODERATE 36/100 | Ignacio / southeast La Plata County: LOW 25/100 | Ignacio / southeast La Plata County: ELEVATED 25/100 | Peak ingredients near 4 PM local; RH 29%, wind 25 mph. |

## Analyst Interpretation

- Headline: Screening remains CONCERN with PSPS WATCH periods Sunday and Monday; no official COZ295 alert or active LPEA outage is reported.
- Summary: Fire-weather and PSPS screening eased slightly but keep Sunday and Monday as WATCH periods. Sunday has the strongest estimated fire danger near Durango at VERY HIGH 77/100; Monday peaks near Ignacio at PSPS WATCH 51/100. Official NWS and LPEA data show no COZ295 fire-weather alert or active outage, while Rio Blanco remains about 1,388 acres and 63% contained with no evacuation notice detected.
- Uncertainty: PSPS screening is not statistically calibrated because no confirmed LPEA PSPS events have been logged; public keyword matches may reflect broad or older context, and forecasts can change.
- Evidence used: overall_status, weather_peaks, official_alerts, forecast_change, lpea_context, fire_posture, active_incidents, calibration
- This interpretation cannot change the deterministic tiers, scores, official alerts, or notification decision.

Changing drivers:
- Momentum is easing versus the morning run, with LOW forecast volatility at 11/100.
- Sunday and Monday remain WATCH periods; Monday's highest PSPS screening shifted to Ignacio at 51/100.
- Official LPEA outage data currently lists no active customer outages.
- Rio Blanco is mapped at about 1,388 acres and 63% contained, with no evacuation notice detected.

What to watch next:
- Watch Durango and Ignacio from roughly 3 PM to 5 PM Sunday for near-threshold fire-weather conditions.
- Watch Ignacio from roughly 2 PM to 4 PM Monday for the run's highest PSPS and Red Flag screening scores.
- Recheck official NWS alerts and the LPEA outage viewer for operational changes.
- Recheck Rio Blanco containment and official Archuleta County evacuation feeds.

## Trend Intelligence

- Summary: Momentum is easing versus the prior run (Aug 8 at 5:21 AM MDT); forecast volatility is low and first WATCH-or-higher date is Sun, Aug 9.
- Momentum: **Easing**
- Forecast volatility: **LOW** (11/100)
- First WATCH-or-higher PSPS date: Sun, Aug 9
- Watch-date movement: First WATCH-or-higher PSPS date remains Sun, Aug 9.
- Method: compares current forecast evidence against prior local forecast history.

Notable changes:
- First WATCH-or-higher PSPS date remains Sun, Aug 9.
- Thu, Aug 13: easing vs prior run; PSPS ELEVATED -> ELEVATED; score +2, wind +2 mph, RH +4%, red-flag hours 0. Driver shifted to Durango / La Plata County.

## Public Analysis Export

- Summary: Highest LPEA PSPS concern is Mon, Aug 10 near Ignacio / southeast La Plata County (WATCH 51/100), driven by red-flag wind/gust signal near 25 mph; near-threshold RH near 16%; 3 sampled hours are near red-flag thresholds. NIFC reports 1 current wildfire in Archuleta County.
- Trend: Momentum is easing versus the prior run (Aug 8 at 5:21 AM MDT); forecast volatility is low and first WATCH-or-higher date is Sun, Aug 9.
- Confidence: **HIGH** (77/100)
- First WATCH-or-higher PSPS date: Sun, Aug 9
- PSPS peak: Mon, Aug 10 near Ignacio / southeast La Plata County at WATCH 51/100
- Red Flag peak: Mon, Aug 10 near Ignacio / southeast La Plata County at WATCH 60/100
- Weather fire-potential peak: Sun, Aug 9 near Durango / La Plata County at VERY HIGH 77/100
- LPEA operational outage context: No active outages are listed by the official LPEA outage viewer.
- Public JSON: `archuleta_red_flag_monitor/public_analysis_export.json`

What changed:
- First WATCH-or-higher PSPS date remains Sun, Aug 9.
- Thu, Aug 13: easing vs prior run; PSPS ELEVATED -> ELEVATED; score +2, wind +2 mph, RH +4%, red-flag hours 0. Driver shifted to Durango / La Plata County.

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
| Sat, Aug 8 | ELEVATED | Arboles / southwest county (ELEVATED 32/100); Chimney Rock / west county (ELEVATED 32/100); Ignacio / southeast La Plata County (ELEVATED 30/100) | Top weather score 30/100 at Arboles / southwest county. Weather score 30/100: RH 10%, wind/gust 16 mph, red-flag hours 0, near-threshold hours 0. |
| Sun, Aug 9 | WATCH | Ignacio / southeast La Plata County (WATCH 48/100); Durango / La Plata County (WATCH 48/100) | Top weather score 48/100 at Ignacio / southeast La Plata County. Weather score 48/100: RH 12%, wind/gust 22 mph, red-flag hours 0, near-threshold hours 3. |
| Mon, Aug 10 | WATCH | Ignacio / southeast La Plata County (WATCH 51/100); Arboles / southwest county (WATCH 46/100) | Top weather score 51/100 at Ignacio / southeast La Plata County. Weather score 51/100: RH 16%, wind/gust 25 mph, red-flag hours 0, near-threshold hours 3. |
| Tue, Aug 11 | ELEVATED | Arboles / southwest county (ELEVATED 40/100); Ignacio / southeast La Plata County (ELEVATED 28/100); Durango / La Plata County (ELEVATED 26/100) | Top weather score 38/100 at Arboles / southwest county. Weather score 38/100: RH 16%, wind/gust 22 mph, red-flag hours 0, near-threshold hours 2. |
| Wed, Aug 12 | ELEVATED | Arboles / southwest county (ELEVATED 24/100); Chimney Rock / west county (ELEVATED 24/100); Durango / La Plata County (ELEVATED 20/100) | Top weather score 22/100 at Arboles / southwest county. Weather score 22/100: RH 21%, wind/gust 23 mph, red-flag hours 0, near-threshold hours 0. |
| Thu, Aug 13 | ELEVATED | Durango / La Plata County (ELEVATED 20/100); Arboles / southwest county (ELEVATED 18/100); Bayfield / east La Plata County (ELEVATED 18/100) | Top weather score 16/100 at Arboles / southwest county. Weather score 16/100: RH 30%, wind/gust 23 mph, red-flag hours 0, near-threshold hours 0. |
| Fri, Aug 14 | ELEVATED | Ignacio / southeast La Plata County (ELEVATED 25/100); Durango / La Plata County (ELEVATED 20/100); Arboles / southwest county (ELEVATED 18/100) | Top weather score 25/100 at Ignacio / southeast La Plata County. Weather score 25/100: RH 29%, wind/gust 25 mph, red-flag hours 0, near-threshold hours 0. |

## Area-Specific Outlook

| Area | Today | Peak this run | Highest-risk window |
| --- | --- | --- | --- |
| Ignacio | ELEVATED 30/100 | Mon, Aug 10: WATCH 51/100 | 2 PM-4 PM local; 3 near/red-flag threshold hours. |
| Durango | ELEVATED 30/100 | Sun, Aug 9: WATCH 48/100 | 3 PM-5 PM local; 3 near/red-flag threshold hours. |
| Arboles | ELEVATED 32/100 | Mon, Aug 10: WATCH 46/100 | 3 PM-5 PM local; 3 near/red-flag threshold hours. |
| Pagosa Springs | ELEVATED 30/100 | Sun, Aug 9: ELEVATED 38/100 | Peak ingredients near 9 PM local; RH 30%, wind 21 mph. |
| Bayfield | ELEVATED 28/100 | Sun, Aug 9: ELEVATED 36/100 | 4 PM-4 PM local; 1 near/red-flag threshold hour. |
| Chimney Rock | ELEVATED 32/100 | Sat, Aug 8: ELEVATED 32/100 | Peak ingredients near 5 PM local; RH 10%, wind 16 mph. |
| Piedra | LOW 14/100 | Sun, Aug 9: ELEVATED 28/100 | Peak ingredients near 9 PM local; RH 33%, wind 20 mph. |
| Chromo | ELEVATED 20/100 | Sun, Aug 9: ELEVATED 28/100 | Peak ingredients near 5 PM local; RH 13%, wind 16 mph. |

## Current Fires + Evacuations

- Incident summary: 1 current wildfire reported in Archuleta County; no current evacuation notice detected in checked county feeds.
- Evacuation status: **NONE DETECTED** - No current evacuation order or warning detected in the checked official county feeds.
- Safety note: Current incidents and evacuation notices are operational context. They do not raise PSPS scores by themselves; follow official evacuation instructions immediately.

### Current NIFC Incidents

| Incident | Type | Size | Containment | Nearest monitored area | Updated |
| --- | --- | --- | --- | --- | --- |
| Rio Blanco | Wildfire | 1,387.74 acres | 63% | Chromo / southeast county (9.9 mi) | Aug 7 at 6:12 PM MDT |

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
- WATCH/LIKELY false-watch past days: 52
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
- No active official NWS Red Flag / Fire Weather or related weather alerts found for monitored zones.

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
| Sat, Aug 8 | ELEVATED | Pagosa Springs: Elevated ingredient present: very low RH forecast near 15%. | Pagosa Springs: RH 15%, wind/gust 15 mph, thunder 2%<br>Arboles / southwest county: RH 10%, wind/gust 16 mph, thunder 2%<br>Chimney Rock / west county: RH 10%, wind/gust 16 mph, thunder 2% |
| Sun, Aug 9 | CONCERN | Durango / La Plata County: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Pagosa Springs: RH 14%, wind/gust 21 mph, thunder 4%<br>Arboles / southwest county: RH 11%, wind/gust 20 mph, thunder 3%<br>Chimney Rock / west county: RH 10%, wind/gust 18 mph, thunder 4% |
| Mon, Aug 10 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 14%, wind/gust 23 mph, thunder 15%<br>Chimney Rock / west county: RH 15%, wind/gust 20 mph, thunder 21%<br>Chromo / southeast county: RH 17%, wind/gust 17 mph, thunder 18% |
| Tue, Aug 11 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 16%, wind/gust 22 mph, thunder 27% |
| Wed, Aug 12 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 29%, wind/gust 20 mph, thunder 63%<br>Arboles / southwest county: RH 21%, wind/gust 23 mph, thunder 44%<br>Chimney Rock / west county: RH 20%, wind/gust 21 mph, thunder 50% |
| Thu, Aug 13 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 38%, wind/gust 20 mph, thunder 72%<br>Arboles / southwest county: RH 30%, wind/gust 23 mph, thunder 52%<br>Chimney Rock / west county: RH 29%, wind/gust 20 mph, thunder 66% |
| Fri, Aug 14 | ELEVATED | Ignacio / southeast La Plata County: Elevated ingredient present: wind/gust forecast near 25 mph. | Ignacio / southeast La Plata County: RH 29%, wind/gust 25 mph, thunder 36% |

## Sample Point Status

- Pagosa Springs: COZ295 (matches), forecast zone COZ023, county zone COC007
- Arboles / southwest county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Chimney Rock / west county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Piedra / north county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Chromo / southeast county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Durango / La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Bayfield / east La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Ignacio / southeast La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
