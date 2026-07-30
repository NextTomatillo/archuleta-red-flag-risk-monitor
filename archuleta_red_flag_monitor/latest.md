# Archuleta County fire-weather monitor

Generated: Jul 30, 2026 at 9:00 AM MDT (Pagosa Springs, CO local time)
Next update: Jul 30, 2026 at 5:20 PM MDT (Pagosa Springs, CO local time)
Date/time basis: Pagosa Springs, CO local time (America/Denver)
> **Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## At A Glance

- Fire-weather tier: **CONCERN**
- PSPS likelihood: **WATCH**
- PSPS likely dates: None
- PSPS watch dates: Sat, Aug 1; Mon, Aug 3; Tue, Aug 4
- Monitor heads-up recommended: **YES** - Send this monitor report because fire-weather screening tier is CONCERN; PSPS screening level is WATCH; a material current wildfire is reported in Archuleta County. This is not an official LPEA or NWS notice.
- HIGH dates: None
- CONCERN dates: Thu, Jul 30; Fri, Jul 31; Sat, Aug 1; Mon, Aug 3; Tue, Aug 4
- ELEVATED dates: Sun, Aug 2
- Official NWS Red Flag / Fire Weather alerts (COZ295): 0
- LPEA signal: `active_keyword_match` - LPEA active/update sources contained power-interruption keywords; review source before treating as confirmed outage intent.
- LPEA source coverage: 13 sources; 5/5 official social sources reachable
- Current Archuleta County wildfires: 2
- Official evacuation notices: No current evacuation order or warning detected in the checked official county feeds.
- NWS discussion: No concerning fire-weather language found in latest GJT discussion.

## Decision Support

- Summary: Highest LPEA PSPS concern is Tue, Aug 4 near Arboles / southwest county (WATCH 62/100), driven by red-flag wind/gust signal near 25 mph; red-flag RH near 13%; 3 sampled hours are near red-flag thresholds. NIFC reports 2 current wildfires in Archuleta County.
- Confidence: **MEDIUM** (69/100) - 8/8 sampled weather points available; 7/7 fire-posture sources reachable; official NWS alert zones checked; 13/13 LPEA public sources reachable; LPEA active/update sources checked; authoritative NIFC current-incident feed checked for Archuleta County; official Archuleta County evacuation feeds checked; forecast changed substantially versus prior run; no confirmed PSPS events logged yet for calibration
- Weather fire-potential peak: Tue, Aug 4: Arboles / southwest county VERY HIGH 78/100
- Red Flag likelihood peak: Tue, Aug 4: Arboles / southwest county WATCH 71/100
- LPEA PSPS peak: Tue, Aug 4: Arboles / southwest county WATCH 62/100
- Method: rules-based decision support using public weather, fire-posture, and LPEA source signals; scores are screening estimates, not official or statistically calibrated probabilities.

| Date | Weather fire potential | Red Flag likelihood | LPEA PSPS | Main window |
| --- | --- | --- | --- | --- |
| Thu, Jul 30 | Chimney Rock / west county: HIGH 64/100 | Chimney Rock / west county: POSSIBLE 50/100 | Chimney Rock / west county: ELEVATED 42/100 | 3 PM-5 PM local; 3 near/red-flag threshold hours. |
| Fri, Jul 31 | Ignacio / southeast La Plata County: HIGH 55/100 | Ignacio / southeast La Plata County: POSSIBLE 52/100 | Ignacio / southeast La Plata County: ELEVATED 44/100 | 5 PM-6 PM local; 2 near/red-flag threshold hours. |
| Sat, Aug 1 | Durango / La Plata County: VERY HIGH 71/100 | Durango / La Plata County: POSSIBLE 52/100 | Durango / La Plata County: WATCH 48/100 | 4 PM-5 PM local; 2 near/red-flag threshold hours. |
| Sun, Aug 2 | Chimney Rock / west county: MODERATE 48/100 | Chimney Rock / west county: LOW 25/100 | Chimney Rock / west county: ELEVATED 30/100 | Peak ingredients near 3 PM local; RH 15%, wind 17 mph. |
| Mon, Aug 3 | Durango / La Plata County: VERY HIGH 78/100 | Ignacio / southeast La Plata County: WATCH 65/100 | Durango / La Plata County: WATCH 52/100 | 2 PM-7 PM local; 6 near/red-flag threshold hours. |
| Tue, Aug 4 | Arboles / southwest county: VERY HIGH 78/100 | Arboles / southwest county: WATCH 71/100 | Arboles / southwest county: WATCH 62/100 | 3 PM-5 PM local; 3 near/red-flag threshold hours. |
| Wed, Aug 5 | Durango / La Plata County: MODERATE 40/100 | Durango / La Plata County: LOW 8/100 | Durango / La Plata County: ELEVATED 26/100 | Peak ingredients near 4 PM local; RH 23%, wind 21 mph. |

## Analyst Interpretation

- Headline: CONCERN fire-weather and WATCH PSPS screening warrant a heads-up, while no official COZ295 alert or active LPEA outage is reported.
- Summary: Screening peaks Tuesday, Aug 4 near Arboles at VERY HIGH fire potential (78/100), WATCH Red Flag likelihood (71/100), and WATCH PSPS concern (62/100). Official checks found zero COZ295 fire-weather alerts and no active LPEA outage; keyword matches are context, not confirmed outage or shutoff intent. Two current Archuleta County wildfires are reported, including the 440.27-acre Rio Blanco fire at 0% containment, with no current evacuation notice detected.
- Uncertainty: These are screening estimates, not official or calibrated probabilities; no confirmed LPEA PSPS events are logged and 44 past WATCH or LIKELY days were false watches.
- Evidence used: overall_status, weather_peaks, official_alerts, forecast_change, lpea_context, fire_posture, active_incidents, calibration
- This interpretation cannot change the deterministic tiers, scores, official alerts, or notification decision.

Changing drivers:
- The first WATCH-or-higher PSPS screening date moved earlier from Monday, Aug 3 to Saturday, Aug 1.
- Saturday, Aug 1 worsened from ELEVATED to WATCH as the driver shifted to Durango and La Plata County.
- Monday, Aug 3 eased by 9 points but remains WATCH.
- Stage 2 restrictions and HIGH fire danger add preparedness context without creating an official alert.

What to watch next:
- Monitor official NWS and LPEA updates for Saturday, Aug 1 through Tuesday, Aug 4.
- Recheck Tuesday afternoon near Arboles for RH near 13%, wind or gusts near 25 mph, and dry-thunder overlap.
- Track the Rio Blanco fire and follow any official evacuation direction immediately.
- Confirm whether LPEA keyword matches develop into direct outage or shutoff intent.

## Trend Intelligence

- Summary: Momentum is steady versus the prior run (Jul 29 at 8:04 PM MDT); forecast volatility is high and first WATCH-or-higher date is Sat, Aug 1.
- Momentum: **Steady**
- Forecast volatility: **HIGH** (40/100)
- First WATCH-or-higher PSPS date: Sat, Aug 1
- Watch-date movement: First WATCH-or-higher PSPS date moved earlier from Mon, Aug 3 to Sat, Aug 1.
- Method: compares current forecast evidence against prior local forecast history.

Notable changes:
- First WATCH-or-higher PSPS date moved earlier from Mon, Aug 3 to Sat, Aug 1.
- Sat, Aug 1: worsening vs prior run; PSPS ELEVATED -> WATCH; score +18, wind +3 mph, RH +1%, red-flag hours 0. Driver shifted to Durango / La Plata County.
- Mon, Aug 3: easing vs prior run; PSPS WATCH -> WATCH; score -9, wind -1 mph, RH +1%, red-flag hours -2.

## Public Analysis Export

- Summary: Highest LPEA PSPS concern is Tue, Aug 4 near Arboles / southwest county (WATCH 62/100), driven by red-flag wind/gust signal near 25 mph; red-flag RH near 13%; 3 sampled hours are near red-flag thresholds. NIFC reports 2 current wildfires in Archuleta County.
- Trend: Momentum is steady versus the prior run (Jul 29 at 8:04 PM MDT); forecast volatility is high and first WATCH-or-higher date is Sat, Aug 1.
- Confidence: **MEDIUM** (69/100)
- First WATCH-or-higher PSPS date: Sat, Aug 1
- PSPS peak: Tue, Aug 4 near Arboles / southwest county at WATCH 62/100
- Red Flag peak: Tue, Aug 4 near Arboles / southwest county at WATCH 71/100
- Weather fire-potential peak: Tue, Aug 4 near Arboles / southwest county at VERY HIGH 78/100
- LPEA operational outage context: No active outages are listed by the official LPEA outage viewer.
- Public JSON: `archuleta_red_flag_monitor/public_analysis_export.json`

What changed:
- First WATCH-or-higher PSPS date moved earlier from Mon, Aug 3 to Sat, Aug 1.
- Sat, Aug 1: worsening vs prior run; PSPS ELEVATED -> WATCH; score +18, wind +3 mph, RH +1%, red-flag hours 0. Driver shifted to Durango / La Plata County.
- Mon, Aug 3: easing vs prior run; PSPS WATCH -> WATCH; score -9, wind -1 mph, RH +1%, red-flag hours -2.

What to watch next:
- Check whether the largest day-level changes line up with wind/RH movement or public-source context.
- Check whether the LPEA active match is still a broad red-flag banner rather than direct PSPS/outage intent.
- Watch whether the highest-risk locations remain consistent across runs or the driver area is moving.
- If a PSPS occurs, log the confirmed date, location, and source so future hit-rate scoring can improve.

## PSPS Likelihood

- **PSPS means Public Safety Power Shutoff:** a planned, safety-related power shutoff LPEA may use during dangerous fire-weather conditions to reduce wildfire ignition risk. See [LPEA PSPS guidance](https://lpea.coop/psps) and the [LPEA outage center](https://lpea.coop/outage-center); if power is out, also check the [LPEA outage map](https://outage.lpea.coop).
- Overall: **WATCH** - PSPS watch screening is present from forecast thresholds or direct LPEA shutoff language; monitor official LPEA and NWS updates.
- Likely PSPS watch dates: None
- PSPS watch dates: Sat, Aug 1; Mon, Aug 3; Tue, Aug 4
- LPEA signal basis: LPEA active/update source contains red-flag, wildfire, or power-interruption language.
- Note: This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

| Date | PSPS likelihood | Driver locations | Weather basis |
| --- | --- | --- | --- |
| Thu, Jul 30 | ELEVATED | Chimney Rock / west county (ELEVATED 42/100); Arboles / southwest county (ELEVATED 40/100); Bayfield / east La Plata County (ELEVATED 35/100) | Top weather score 38/100 at Arboles / southwest county. Weather score 38/100: RH 18%, wind/gust 24 mph, red-flag hours 0, near-threshold hours 3. |
| Fri, Jul 31 | ELEVATED | Ignacio / southeast La Plata County (ELEVATED 44/100); Arboles / southwest county (ELEVATED 40/100); Durango / La Plata County (ELEVATED 38/100) | Top weather score 44/100 at Ignacio / southeast La Plata County. Weather score 44/100: RH 14%, wind/gust 23 mph, red-flag hours 0, near-threshold hours 2. |
| Sat, Aug 1 | WATCH | Durango / La Plata County (WATCH 48/100) | Top weather score 44/100 at Durango / La Plata County. Weather score 44/100: RH 15%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 2. |
| Sun, Aug 2 | ELEVATED | Chimney Rock / west county (ELEVATED 30/100); Arboles / southwest county (ELEVATED 28/100); Durango / La Plata County (ELEVATED 24/100) | Top weather score 26/100 at Arboles / southwest county. Weather score 26/100: RH 15%, wind/gust 16 mph, red-flag hours 0, near-threshold hours 0. |
| Mon, Aug 3 | WATCH | Ignacio / southeast La Plata County (WATCH 52/100); Durango / La Plata County (WATCH 52/100); Bayfield / east La Plata County (WATCH 52/100); Arboles / southwest county (WATCH 50/100) | Top weather score 52/100 at Ignacio / southeast La Plata County. Weather score 52/100: RH 12%, wind/gust 24 mph, red-flag hours 0, near-threshold hours 5. |
| Tue, Aug 4 | WATCH | Arboles / southwest county (WATCH 62/100); Ignacio / southeast La Plata County (WATCH 57/100) | Top weather score 60/100 at Arboles / southwest county. Weather score 60/100: RH 13%, wind/gust 25 mph, red-flag hours 0, near-threshold hours 3. |
| Wed, Aug 5 | ELEVATED | Durango / La Plata County (ELEVATED 26/100); Bayfield / east La Plata County (ELEVATED 26/100); Chimney Rock / west county (ELEVATED 24/100) | Top weather score 22/100 at Durango / La Plata County. Weather score 22/100: RH 21%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 0. |

## Area-Specific Outlook

| Area | Today | Peak this run | Highest-risk window |
| --- | --- | --- | --- |
| Arboles | ELEVATED 40/100 | Tue, Aug 4: WATCH 62/100 | 3 PM-5 PM local; 3 near/red-flag threshold hours. |
| Ignacio | ELEVATED 31/100 | Tue, Aug 4: WATCH 57/100 | 3 PM-4 PM local; 2 near/red-flag threshold hours. |
| Durango | ELEVATED 26/100 | Mon, Aug 3: WATCH 52/100 | 2 PM-7 PM local; 6 near/red-flag threshold hours. |
| Bayfield | ELEVATED 35/100 | Mon, Aug 3: WATCH 52/100 | 3 PM-6 PM local; 4 near/red-flag threshold hours. |
| Chimney Rock | ELEVATED 42/100 | Thu, Jul 30: ELEVATED 42/100 | 3 PM-5 PM local; 3 near/red-flag threshold hours. |
| Pagosa Springs | ELEVATED 20/100 | Fri, Jul 31: ELEVATED 24/100 | Peak ingredients near 10 PM local; RH 42%, wind 18 mph. |
| Piedra | LOW 12/100 | Fri, Jul 31: ELEVATED 24/100 | Peak ingredients near 9 PM local; RH 37%, wind 18 mph. |
| Chromo | LOW 12/100 | Fri, Jul 31: ELEVATED 24/100 | Peak ingredients near 10 PM local; RH 48%, wind 17 mph. |

## Current Fires + Evacuations

- Incident summary: 2 current wildfires reported in Archuleta County; no current evacuation notice detected in checked county feeds.
- Evacuation status: **NONE DETECTED** - No current evacuation order or warning detected in the checked official county feeds.
- Safety note: Current incidents and evacuation notices are operational context. They do not raise PSPS scores by themselves; follow official evacuation instructions immediately.

### Current NIFC Incidents

| Incident | Type | Size | Containment | Nearest monitored area | Updated |
| --- | --- | --- | --- | --- | --- |
| Rio Blanco | Wildfire | 440.27 acres | 0% | Chromo / southeast county (9.9 mi) | Jul 29 at 7:09 PM MDT |
| Blanco | Wildfire | 0.41 acres | Not reported | Pagosa Springs (9.2 mi) | Jul 27 at 5:30 PM MDT |

Official links: [NIFC map](https://www.nifc.gov/fire-information/maps), [Archuleta County fire updates](https://sheriff.archuletacounty.gov/divisions/emergency-operations/fire-updates-and-information/), [County alerts](https://nixle.us/archuleta-county-office-of-emergency-management-aux/), [Watch Duty](https://app.watchduty.org/)

## Fire Posture + Restrictions

- Summary: 4 official sources indicate fire restrictions or staged restrictions.
- Max restriction stage detected: STAGE 2
- Max fire danger detected: HIGH
- Sources reachable: 7/7
- Note: Official-source status check only; verify restrictions and burn decisions with the responsible jurisdiction.

| Jurisdiction | Restrictions | Fire danger | Source |
| --- | --- | --- | --- |
| Archuleta County | STAGE 1 | UNKNOWN | [Archuleta County Sheriff fire updates](https://sheriff.archuletacounty.gov/divisions/emergency-operations/fire-updates-and-information/) |
| Pagosa Springs | STAGE 2 | UNKNOWN | [Town of Pagosa Springs](https://www.pagosasprings.co.gov/) |
| San Juan National Forest | STAGE 2 | HIGH | [San Juan National Forest fire](https://www.fs.usda.gov/r02/sanjuan/fire) |
| BLM Tres Rios | UNKNOWN | UNKNOWN | [BLM Tres Rios Field Office](https://www.blm.gov/office/tres-rios-field-office) |
| La Plata County / Durango Fire | NONE | UNKNOWN | [Durango Fire & Rescue fire conditions](https://www.durangofire.org/fire-conditions) |
| Durango | STAGE 2 | UNKNOWN | [City of Durango](https://www.durangoco.gov/) |
| Southern Ute / Ignacio | UNKNOWN | UNKNOWN | [Southern Ute Indian Tribe](https://www.southernute-nsn.gov/) |

## Forecast Calibration

### PSPS Calibration

- Summary: No confirmed LPEA PSPS events logged yet; calibration will start once events are added.
- Confirmed PSPS events logged: 0
- Candidate/unconfirmed events logged: 0
- WATCH/LIKELY false-watch past days: 44
- Pending WATCH/LIKELY dates in current forecast: Sat, Aug 1; Mon, Aug 3; Tue, Aug 4
- Calibration source: manual PSPS event log plus forecast history from prior monitor runs.

### Red Flag / Fire Weather Calibration

- Summary: 3/3 official Red Flag / Fire Weather episodes had a pre-alert HIGH monitor signal; date-level result was 21/21. Episode-average lead time: 3.5 days.
- Official alert episodes logged: 3 (21 alert dates)
- Episode-level pre-alert HIGH hit rate: 100%
- Date-level pre-alert HIGH hit rate: 100%
- Episode-level average lead time: 3.5 days
- HIGH false-watch past days: 16
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
- Example signal: ...ibrary! 1 2 519 LPEA @LaPlataElectric May 7, 2024 LPEA members are experiencing power outages in the Bayfield and Pagosa Springs areas. Approximately 200 meters are out and it is suspected that the high winds are...
- Reference/context hits: [LPEA outage center](https://lpea.coop/outage-center); [LPEA wildfire / public safety power shutoffs](https://lpea.coop/psps); [LPEA red flag outage impact page](https://lpea.coop/outages/red-flag-warnings-and-impact-outages-prioritizing-safety-our-members); [LPEA fire mitigation](https://lpea.coop/fire-mitigation); [LPEA latest news](https://lpea.coop/Posts)

**Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## Next 7 Days

| Date | Tier | Main reason | Worst sampled metrics |
| --- | --- | --- | --- |
| Thu, Jul 30 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 18%, wind/gust 24 mph, thunder 5%<br>Chimney Rock / west county: RH 17%, wind/gust 22 mph, thunder 4%<br>Bayfield / east La Plata County: RH 21%, wind/gust 25 mph, thunder 4% |
| Fri, Jul 31 | CONCERN | Ignacio / southeast La Plata County: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 12%, wind/gust 21 mph, thunder 2%<br>Chimney Rock / west county: RH 12%, wind/gust 17 mph, thunder 9%<br>Durango / La Plata County: RH 14%, wind/gust 22 mph, thunder 3% |
| Sat, Aug 1 | CONCERN | Durango / La Plata County: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 14%, wind/gust 23 mph, thunder 7%<br>Chimney Rock / west county: RH 14%, wind/gust 17 mph, thunder 10%<br>Durango / La Plata County: RH 15%, wind/gust 21 mph, thunder 13% |
| Sun, Aug 2 | ELEVATED | Arboles / southwest county: Elevated ingredient present: very low RH forecast near 15%. | Arboles / southwest county: RH 15%, wind/gust 16 mph, thunder 2%<br>Chimney Rock / west county: RH 15%, wind/gust 17 mph, thunder 4% |
| Mon, Aug 3 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 11%, wind/gust 22 mph, thunder 3%<br>Chimney Rock / west county: RH 11%, wind/gust 21 mph, thunder 6%<br>Durango / La Plata County: RH 13%, wind/gust 24 mph, thunder 5% |
| Tue, Aug 4 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 13%, wind/gust 25 mph, thunder 20%<br>Chimney Rock / west county: RH 14%, wind/gust 20 mph, thunder 29%<br>Bayfield / east La Plata County: RH 17%, wind/gust 22 mph, thunder 22% |
| Wed, Aug 5 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 23%, wind/gust 17 mph, thunder 45%<br>Arboles / southwest county: RH 16%, wind/gust 20 mph, thunder 29%<br>Chimney Rock / west county: RH 17%, wind/gust 18 mph, thunder 40% |

## Sample Point Status

- Pagosa Springs: COZ295 (matches), forecast zone COZ023, county zone COC007
- Arboles / southwest county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Chimney Rock / west county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Piedra / north county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Chromo / southeast county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Durango / La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Bayfield / east La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Ignacio / southeast La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
