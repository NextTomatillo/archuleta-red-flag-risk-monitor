# Archuleta County fire-weather monitor

Generated: Aug 10, 2026 at 5:30 PM MDT (Pagosa Springs, CO local time)
Next update: Aug 11, 2026 at 5:20 AM MDT (Pagosa Springs, CO local time)
Date/time basis: Pagosa Springs, CO local time (America/Denver)
> **Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## At A Glance

- Fire-weather tier: **CONCERN**
- PSPS likelihood: **WATCH**
- PSPS likely dates: None
- PSPS watch dates: Sun, Aug 16
- Monitor heads-up recommended: **YES** - Send this monitor report because fire-weather screening tier is CONCERN; PSPS screening level is WATCH; a material current wildfire is reported in Archuleta County. This is not an official LPEA or NWS notice.
- HIGH dates: None
- CONCERN dates: Sun, Aug 16
- ELEVATED dates: Tue, Aug 11; Fri, Aug 14; Sat, Aug 15
- Official NWS Red Flag / Fire Weather alerts (COZ295): 0
- LPEA signal: `operational_outage_active` - Official LPEA outage data indicates an operational outage; use as grid context, not PSPS/fire evidence unless LPEA identifies that cause.
- LPEA source coverage: 13 sources; 5/5 official social sources reachable
- Current Archuleta County wildfires: 1
- Official evacuation notices: No current evacuation order or warning detected in the checked official county feeds.
- NWS discussion: No concerning fire-weather language found in latest GJT discussion.

## Decision Support

- Summary: Highest LPEA PSPS concern is Sun, Aug 16 near Arboles / southwest county (WATCH 48/100), driven by near-threshold wind/gust signal near 22 mph; near-threshold RH near 17%; 4 sampled hours are near red-flag thresholds. NIFC reports 1 current wildfire in Archuleta County.
- Confidence: **MEDIUM** (69/100) - 8/8 sampled weather points available; 7/7 fire-posture sources reachable; official NWS alert zones checked; 13/13 LPEA public sources reachable; LPEA active/update sources checked; active LPEA operational outage context checked separately from PSPS scoring; authoritative NIFC current-incident feed checked for Archuleta County; official Archuleta County evacuation feeds checked; forecast changed substantially versus prior run; no confirmed PSPS events logged yet for calibration
- Weather fire-potential peak: Sun, Aug 16: Chimney Rock / west county HIGH 63/100
- Red Flag likelihood peak: Sun, Aug 16: Arboles / southwest county WATCH 57/100
- LPEA PSPS peak: Sun, Aug 16: Arboles / southwest county WATCH 48/100
- Method: rules-based decision support using public weather, fire-posture, and LPEA source signals; scores are screening estimates, not official or statistically calibrated probabilities.

| Date | Weather fire potential | Red Flag likelihood | LPEA PSPS | Main window |
| --- | --- | --- | --- | --- |
| Mon, Aug 10 | Durango / La Plata County: MODERATE 44/100 | Arboles / southwest county: LOW 16/100 | Arboles / southwest county: ELEVATED 30/100 | 5 PM-5 PM local; 1 near/red-flag threshold hour. |
| Tue, Aug 11 | Chimney Rock / west county: MODERATE 46/100 | Arboles / southwest county: LOW 27/100 | Arboles / southwest county: ELEVATED 40/100 | Peak ingredients near 5 PM local; RH 24%, wind 21 mph. |
| Wed, Aug 12 | Durango / La Plata County: MODERATE 36/100 | Arboles / southwest county: LOW 8/100 | Arboles / southwest county: ELEVATED 24/100 | Peak ingredients near 3 PM local; RH 21%, wind 21 mph. |
| Thu, Aug 13 | Durango / La Plata County: MODERATE 36/100 | Durango / La Plata County: LOW 8/100 | Durango / La Plata County: ELEVATED 20/100 | Peak ingredients near 3 PM local; RH 33%, wind 21 mph. |
| Fri, Aug 14 | Durango / La Plata County: MODERATE 36/100 | Ignacio / southeast La Plata County: LOW 25/100 | Ignacio / southeast La Plata County: ELEVATED 25/100 | Peak ingredients near 4 PM local; RH 30%, wind 25 mph. |
| Sat, Aug 15 | Bayfield / east La Plata County: MODERATE 39/100 | Bayfield / east La Plata County: LOW 25/100 | Bayfield / east La Plata County: ELEVATED 27/100 | Peak ingredients near 4 PM local; RH 25%, wind 25 mph. |
| Sun, Aug 16 | Chimney Rock / west county: HIGH 63/100 | Arboles / southwest county: WATCH 57/100 | Arboles / southwest county: WATCH 48/100 | 3 PM-6 PM local; 4 near/red-flag threshold hours. |

## Analyst Interpretation

- Headline: Screening is CONCERN with Sunday PSPS WATCH near Arboles; one localized LPEA outage has no identified fire or PSPS cause.
- Summary: Sunday, Aug 16 is the next peak: Arboles reaches PSPS WATCH 48/100 and Red Flag WATCH 57/100 from 3 PM to 6 PM, while Chimney Rock reaches HIGH fire potential 63/100. Official sources show no active NWS fire-weather alert. LPEA reports one unplanned one-customer outage near Bayfield, separate from PSPS screening; Rio Blanco is 1,388 acres and 91% contained with no evacuation notice detected.
- Uncertainty: No confirmed LPEA PSPS events are available for calibration; 54 false-WATCH days and HIGH forecast volatility at 43/100 mean this screening estimate may change materially.
- Evidence used: overall_status, weather_peaks, official_alerts, forecast_change, lpea_context, fire_posture, active_incidents, calibration
- This interpretation cannot change the deterministic tiers, scores, official alerts, or notification decision.

Changing drivers:
- The first WATCH-or-higher date moved later from Monday to Sunday, Aug 16.
- Monday eased from PSPS WATCH to ELEVATED, falling 16 points as humidity rose 3%.
- Sunday worsened from ELEVATED to WATCH, while Tuesday increased 10 points but remains ELEVATED.
- Rio Blanco containment increased to 91%, with no current evacuation notice detected.

What to watch next:
- Recheck the Sunday Arboles forecast as the 3 PM to 6 PM WATCH window approaches.
- Monitor the localized Bayfield-area outage for restoration or an identified cause.
- Treat any new NWS alert or LPEA PSPS notice as official context, separate from screening estimates.
- Monitor Rio Blanco containment and county evacuation feeds for operational changes.

## Trend Intelligence

- Summary: Momentum is rising versus the prior run (Aug 10 at 5:28 AM MDT); forecast volatility is high and first WATCH-or-higher date is Sun, Aug 16.
- Momentum: **Rising**
- Forecast volatility: **HIGH** (43/100)
- First WATCH-or-higher PSPS date: Sun, Aug 16
- Watch-date movement: First WATCH-or-higher PSPS date moved later from Mon, Aug 10 to Sun, Aug 16.
- Method: compares current forecast evidence against prior local forecast history.

Notable changes:
- First WATCH-or-higher PSPS date moved later from Mon, Aug 10 to Sun, Aug 16.
- Mon, Aug 10: easing vs prior run; PSPS WATCH -> ELEVATED; score -16, wind -1 mph, RH +3%, red-flag hours 0.
- Sun, Aug 16: worsening vs prior run; PSPS ELEVATED -> WATCH; score +4, wind +1 mph, RH 0%, red-flag hours 0.
- Tue, Aug 11: worsening vs prior run; PSPS ELEVATED -> ELEVATED; score +10, wind -1 mph, RH 0%, red-flag hours 0.

## Public Analysis Export

- Summary: Highest LPEA PSPS concern is Sun, Aug 16 near Arboles / southwest county (WATCH 48/100), driven by near-threshold wind/gust signal near 22 mph; near-threshold RH near 17%; 4 sampled hours are near red-flag thresholds. NIFC reports 1 current wildfire in Archuleta County.
- Trend: Momentum is rising versus the prior run (Aug 10 at 5:28 AM MDT); forecast volatility is high and first WATCH-or-higher date is Sun, Aug 16.
- Confidence: **MEDIUM** (69/100)
- First WATCH-or-higher PSPS date: Sun, Aug 16
- PSPS peak: Sun, Aug 16 near Arboles / southwest county at WATCH 48/100
- Red Flag peak: Sun, Aug 16 near Arboles / southwest county at WATCH 57/100
- Weather fire-potential peak: Sun, Aug 16 near Chimney Rock / west county at HIGH 63/100
- LPEA operational outage context: 1 active outage; 0 planned and 1 unplanned; 1 customer out. No fire-weather or PSPS cause is identified.
- Public JSON: `archuleta_red_flag_monitor/public_analysis_export.json`

What changed:
- First WATCH-or-higher PSPS date moved later from Mon, Aug 10 to Sun, Aug 16.
- Mon, Aug 10: easing vs prior run; PSPS WATCH -> ELEVATED; score -16, wind -1 mph, RH +3%, red-flag hours 0.
- Sun, Aug 16: worsening vs prior run; PSPS ELEVATED -> WATCH; score +4, wind +1 mph, RH 0%, red-flag hours 0.
- Tue, Aug 11: worsening vs prior run; PSPS ELEVATED -> ELEVATED; score +10, wind -1 mph, RH 0%, red-flag hours 0.

What to watch next:
- Check whether the largest day-level changes line up with wind/RH movement or public-source context.
- Check whether the LPEA active match is still a broad red-flag banner rather than direct PSPS/outage intent.
- Watch whether the highest-risk locations remain consistent across runs or the driver area is moving.
- If a PSPS occurs, log the confirmed date, location, and source so future hit-rate scoring can improve.

## PSPS Likelihood

- **PSPS means Public Safety Power Shutoff:** a planned, safety-related power shutoff LPEA may use during dangerous fire-weather conditions to reduce wildfire ignition risk. See [LPEA PSPS guidance](https://lpea.coop/psps) and the [LPEA outage center](https://lpea.coop/outage-center); if power is out, also check the [LPEA outage map](https://outage.lpea.coop).
- Overall: **WATCH** - PSPS watch screening is present from forecast thresholds or direct LPEA shutoff language; monitor official LPEA and NWS updates.
- Likely PSPS watch dates: None
- PSPS watch dates: Sun, Aug 16
- LPEA signal basis: LPEA active/update source contains red-flag, wildfire, or power-interruption language.
- Note: This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

| Date | PSPS likelihood | Driver locations | Weather basis |
| --- | --- | --- | --- |
| Mon, Aug 10 | ELEVATED | Arboles / southwest county (ELEVATED 30/100); Durango / La Plata County (ELEVATED 26/100); Bayfield / east La Plata County (ELEVATED 24/100) | Top weather score 28/100 at Arboles / southwest county. Weather score 28/100: RH 17%, wind/gust 22 mph, red-flag hours 0, near-threshold hours 1. |
| Tue, Aug 11 | ELEVATED | Arboles / southwest county (ELEVATED 40/100); Ignacio / southeast La Plata County (ELEVATED 32/100); Chimney Rock / west county (ELEVATED 32/100) | Top weather score 38/100 at Arboles / southwest county. Weather score 38/100: RH 15%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 0. |
| Wed, Aug 12 | ELEVATED | Arboles / southwest county (ELEVATED 24/100); Durango / La Plata County (ELEVATED 20/100); Bayfield / east La Plata County (ELEVATED 18/100) | Top weather score 22/100 at Arboles / southwest county. Weather score 22/100: RH 21%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 0. |
| Thu, Aug 13 | ELEVATED | Durango / La Plata County (ELEVATED 20/100); Arboles / southwest county (ELEVATED 18/100); Chimney Rock / west county (ELEVATED 18/100) | Top weather score 16/100 at Arboles / southwest county. Weather score 16/100: RH 28%, wind/gust 23 mph, red-flag hours 0, near-threshold hours 0. |
| Fri, Aug 14 | ELEVATED | Ignacio / southeast La Plata County (ELEVATED 25/100); Durango / La Plata County (ELEVATED 20/100); Arboles / southwest county (ELEVATED 18/100) | Top weather score 25/100 at Ignacio / southeast La Plata County. Weather score 25/100: RH 30%, wind/gust 25 mph, red-flag hours 0, near-threshold hours 0. |
| Sat, Aug 15 | ELEVATED | Bayfield / east La Plata County (ELEVATED 27/100); Ignacio / southeast La Plata County (ELEVATED 25/100); Arboles / southwest county (ELEVATED 24/100) | Top weather score 25/100 at Bayfield / east La Plata County. Weather score 25/100: RH 25%, wind/gust 25 mph, red-flag hours 0, near-threshold hours 0. |
| Sun, Aug 16 | WATCH | Arboles / southwest county (WATCH 48/100) | Top weather score 46/100 at Arboles / southwest county. Weather score 46/100: RH 17%, wind/gust 22 mph, red-flag hours 0, near-threshold hours 4. |

## Area-Specific Outlook

| Area | Today | Peak this run | Highest-risk window |
| --- | --- | --- | --- |
| Arboles | ELEVATED 30/100 | Sun, Aug 16: WATCH 48/100 | 3 PM-6 PM local; 4 near/red-flag threshold hours. |
| Chimney Rock | ELEVATED 22/100 | Sun, Aug 16: ELEVATED 44/100 | 4 PM-5 PM local; 2 near/red-flag threshold hours. |
| Ignacio | ELEVATED 22/100 | Tue, Aug 11: ELEVATED 32/100 | 3 PM-3 PM local; 1 near/red-flag threshold hour. |
| Bayfield | ELEVATED 24/100 | Sat, Aug 15: ELEVATED 27/100 | Peak ingredients near 4 PM local; RH 25%, wind 25 mph. |
| Durango | ELEVATED 26/100 | Mon, Aug 10: ELEVATED 26/100 | Peak ingredients near 5 PM local; RH 20%, wind 22 mph. |
| Pagosa Springs | LOW 12/100 | Sat, Aug 15: ELEVATED 20/100 | Peak ingredients near 4 PM local; RH 28%, wind 22 mph. |
| Piedra | LOW 16/100 | Mon, Aug 10: LOW 16/100 | Peak ingredients near 9 PM local; RH 44%, wind 17 mph. |
| Chromo | LOW 16/100 | Mon, Aug 10: LOW 16/100 | Peak ingredients near 5 PM local; RH 20%, wind 17 mph. |

## Current Fires + Evacuations

- Incident summary: 1 current wildfire reported in Archuleta County; no current evacuation notice detected in checked county feeds.
- Evacuation status: **NONE DETECTED** - No current evacuation order or warning detected in the checked official county feeds.
- Safety note: Current incidents and evacuation notices are operational context. They do not raise PSPS scores by themselves; follow official evacuation instructions immediately.

### Current NIFC Incidents

| Incident | Type | Size | Containment | Nearest monitored area | Updated |
| --- | --- | --- | --- | --- | --- |
| Rio Blanco | Wildfire | 1,388.00 acres | 91% | Chromo / southeast county (9.9 mi) | Aug 10 at 3:58 PM MDT |

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
- WATCH/LIKELY false-watch past days: 54
- Pending WATCH/LIKELY dates in current forecast: Sun, Aug 16
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

- Status: `operational_outage_active` - Official LPEA outage data indicates an operational outage; use as grid context, not PSPS/fire evidence unless LPEA identifies that cause.
- Meaning: Active source match means a monitored LPEA active/update source currently contains fire, outage, PSPS, or power-interruption keywords. Operational outages are shown separately and are not treated as PSPS/fire evidence unless the source text says so.
- Operational outage context: 1 active outage; 0 planned and 1 unplanned; 1 customer out. No fire-weather or PSPS cause is identified.
- Source coverage: 13 sources; 5/5 official social sources reachable
- Evidence quality: 0 operational, 4 active/update, 0 archive/context, 6 reference source matches.
- Operational outage source links: [34344 HWY 160 #31](https://outage.lpea.coop)
- Active/update source pages with matches: LPEA homepage (public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation, restoration); LPEA X (power outage, outage map, high winds, restore power); LPEA LinkedIn (wildfire, fire mitigation)
- Distinct active/update signals: LPEA X (power outage, outage map, high winds, restore power); LPEA X (power outage, outage map, high winds, restore power); LPEA LinkedIn (wildfire, fire mitigation); LPEA LinkedIn (wildfire, fire mitigation)
- Example signal: ...ibrary! 1 2 522 LPEA @LaPlataElectric May 7, 2024 LPEA members are experiencing power outages in the Bayfield and Pagosa Springs areas. Approximately 200 meters are out and it is suspected that the high winds are...
- Reference/context hits: [LPEA outage center](https://lpea.coop/outage-center); [LPEA wildfire / public safety power shutoffs](https://lpea.coop/psps); [LPEA red flag outage impact page](https://lpea.coop/outages/red-flag-warnings-and-impact-outages-prioritizing-safety-our-members); [LPEA fire mitigation](https://lpea.coop/fire-mitigation); [LPEA latest news](https://lpea.coop/Posts)

**Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## Next 7 Days

| Date | Tier | Main reason | Worst sampled metrics |
| --- | --- | --- | --- |
| Mon, Aug 10 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 25%, wind/gust 18 mph, thunder 19%<br>Arboles / southwest county: RH 17%, wind/gust 22 mph, thunder 11%<br>Chimney Rock / west county: RH 17%, wind/gust 18 mph, thunder 16% |
| Tue, Aug 11 | ELEVATED | Arboles / southwest county: Elevated ingredient present: very low RH forecast near 15%; dry-thunder probability reaches 16%. | Arboles / southwest county: RH 15%, wind/gust 21 mph, thunder 25%<br>Chimney Rock / west county: RH 15%, wind/gust 20 mph, thunder 30%<br>Ignacio / southeast La Plata County: RH 17%, wind/gust 23 mph, thunder 25% |
| Wed, Aug 12 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 28%, wind/gust 17 mph, thunder 51%<br>Arboles / southwest county: RH 21%, wind/gust 21 mph, thunder 36%<br>Chimney Rock / west county: RH 21%, wind/gust 20 mph, thunder 44% |
| Thu, Aug 13 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 37%, wind/gust 20 mph, thunder 55%<br>Arboles / southwest county: RH 28%, wind/gust 23 mph, thunder 39%<br>Chimney Rock / west county: RH 28%, wind/gust 21 mph, thunder 44% |
| Fri, Aug 14 | ELEVATED | Ignacio / southeast La Plata County: Elevated ingredient present: wind/gust forecast near 25 mph. | Ignacio / southeast La Plata County: RH 30%, wind/gust 25 mph, thunder 36% |
| Sat, Aug 15 | ELEVATED | Bayfield / east La Plata County: Elevated ingredient present: wind/gust forecast near 25 mph. | Bayfield / east La Plata County: RH 25%, wind/gust 25 mph, thunder 26%<br>Ignacio / southeast La Plata County: RH 23%, wind/gust 25 mph, thunder 18% |
| Sun, Aug 16 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 17%, wind/gust 22 mph, thunder 17%<br>Chimney Rock / west county: RH 16%, wind/gust 21 mph, thunder 25% |

## Sample Point Status

- Pagosa Springs: COZ295 (matches), forecast zone COZ023, county zone COC007
- Arboles / southwest county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Chimney Rock / west county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Piedra / north county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Chromo / southeast county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Durango / La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Bayfield / east La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Ignacio / southeast La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
