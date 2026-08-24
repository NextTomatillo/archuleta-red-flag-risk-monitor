# Archuleta County fire-weather monitor

Generated: Aug 24, 2026 at 4:23 PM MDT (Pagosa Springs, CO local time)
Next update: Aug 24, 2026 at 5:20 PM MDT (Pagosa Springs, CO local time)
Date/time basis: Pagosa Springs, CO local time (America/Denver)
> **Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## At A Glance

- Fire-weather tier: **HIGH**
- PSPS likelihood: **LIKELY**
- PSPS likely dates: Sat, Aug 29
- PSPS watch dates: Fri, Aug 28; Sun, Aug 30
- Monitor heads-up recommended: **YES** - Send this monitor report because fire-weather screening tier is HIGH; PSPS screening level is LIKELY; a material current wildfire is reported in Archuleta County. This is not an official LPEA or NWS notice.
- HIGH dates: Sat, Aug 29
- CONCERN dates: Tue, Aug 25; Thu, Aug 27; Fri, Aug 28; Sun, Aug 30
- ELEVATED dates: Wed, Aug 26
- Official NWS Red Flag / Fire Weather alerts (COZ295): 0
- LPEA signal: `active_keyword_match` - LPEA active/update sources contained power-interruption keywords; review source before treating as confirmed outage intent.
- LPEA source coverage: 13 sources; 5/5 official social sources reachable
- Current Archuleta County wildfires: 3
- Official evacuation notices: No current evacuation order or warning detected in the checked official county feeds.
- NWS discussion: NWS discussion contains fire-weather concern language.

## Decision Support

- Summary: Highest LPEA PSPS concern is Sat, Aug 29 near Arboles / southwest county (LIKELY 65/100), driven by red-flag wind/gust signal near 28 mph; red-flag RH near 15%; 3 sampled hours meet red-flag screen. NIFC reports 3 current wildfires in Archuleta County.
- Confidence: **MEDIUM** (74/100) - 8/8 sampled weather points available; 7/7 fire-posture sources reachable; official NWS alert zones checked; 13/13 LPEA public sources reachable; LPEA active/update sources checked; authoritative NIFC current-incident feed checked for Archuleta County; official Archuleta County evacuation feeds checked; forecast changed moderately versus prior run; no confirmed PSPS events logged yet for calibration
- Weather fire-potential peak: Sat, Aug 29: Chimney Rock / west county VERY HIGH 78/100
- Red Flag likelihood peak: Sat, Aug 29: Arboles / southwest county LIKELY 78/100
- LPEA PSPS peak: Sat, Aug 29: Arboles / southwest county LIKELY 65/100
- Method: rules-based decision support using public weather, fire-posture, and LPEA source signals; scores are screening estimates, not official or statistically calibrated probabilities.

| Date | Weather fire potential | Red Flag likelihood | LPEA PSPS | Main window |
| --- | --- | --- | --- | --- |
| Mon, Aug 24 | Durango / La Plata County: LOW 30/100 | Arboles / southwest county: LOW 8/100 | Arboles / southwest county: ELEVATED 24/100 | Peak ingredients near 4 PM local; RH 19%, wind 22 mph. |
| Tue, Aug 25 | Arboles / southwest county: HIGH 55/100 | Arboles / southwest county: POSSIBLE 50/100 | Arboles / southwest county: ELEVATED 40/100 | 3 PM-5 PM local; 3 near/red-flag threshold hours. |
| Wed, Aug 26 | Chimney Rock / west county: MODERATE 40/100 | Chimney Rock / west county: LOW 25/100 | Arboles / southwest county: ELEVATED 30/100 | 4 PM-4 PM local; 1 near/red-flag threshold hour. |
| Thu, Aug 27 | Chimney Rock / west county: HIGH 62/100 | Arboles / southwest county: POSSIBLE 50/100 | Arboles / southwest county: ELEVATED 40/100 | 3 PM-4 PM local; 2 near/red-flag threshold hours. |
| Fri, Aug 28 | Chimney Rock / west county: VERY HIGH 71/100 | Arboles / southwest county: WATCH 58/100 | Arboles / southwest county: WATCH 50/100 | 3 PM-6 PM local; 4 near/red-flag threshold hours. |
| Sat, Aug 29 | Chimney Rock / west county: VERY HIGH 78/100 | Arboles / southwest county: LIKELY 78/100 | Arboles / southwest county: LIKELY 65/100 | 2 PM-6 PM local; 5 near/red-flag threshold hours. |
| Sun, Aug 30 | Arboles / southwest county: HIGH 67/100 | Arboles / southwest county: WATCH 62/100 | Arboles / southwest county: WATCH 56/100 | 4 PM-5 PM local; 2 near/red-flag threshold hours. |

## Analyst Interpretation

- Headline: Saturday remains the modeled peak near Arboles, but PSPS screening eased to 65/100; no official COZ295 alert, active LPEA outage, or evacuation notice is reported.
- Summary: PSPS screening remains LIKELY Sat, Aug 29 near Arboles at 65/100, with red-flag likelihood 78/100; these are screening estimates, not official LPEA or NWS notices. Official COZ295 alerts remain zero, and the official LPEA outage viewer lists no active outages despite broad keyword matches on monitored LPEA pages. NIFC lists Rio Blanco at 1,387.74 acres and 100% contained plus two new small incidents, Snow Springs at 1 acre and Spring Basin at 0.1 acre; no evacuation notice was detected.
- Uncertainty: Confidence is MEDIUM 74/100; forecast volatility is MEDIUM 17/100 and no confirmed PSPS events exist for calibration. The two new small fire records have no reported containment and may update quickly.
- Evidence used: overall_status, weather_peaks, official_alerts, forecast_change, lpea_context, fire_posture, active_incidents, calibration
- This interpretation cannot change the deterministic tiers, scores, official alerts, or notification decision.

Changing drivers:
- The first WATCH-or-higher PSPS date remains Friday, Aug 28.
- Friday and Sunday each eased by 7 points while remaining at WATCH.
- Saturday remains the peak near Arboles at PSPS LIKELY 65/100, with RH near 15%, wind/gust near 28 mph, and 3 red-flag hours.
- Snow Springs and Spring Basin were discovered today at 1 acre and 0.1 acre; no evacuation notice was detected.

What to watch next:
- Recheck Saturday's LIKELY peak after the next forecast update because the timing and driver area can still shift.
- Monitor official updates for Snow Springs and Spring Basin, including any containment or evacuation changes.
- Treat the LPEA keyword match as broad public-source context, not evidence of an active outage or PSPS decision.
- Continue checking official NWS alerts; the current COZ295 alert count is zero.

## Trend Intelligence

- Summary: Momentum is easing versus the prior run (Aug 24 at 9:55 AM MDT); forecast volatility is medium and first WATCH-or-higher date is Fri, Aug 28.
- Momentum: **Easing**
- Forecast volatility: **MEDIUM** (17/100)
- First WATCH-or-higher PSPS date: Fri, Aug 28
- Watch-date movement: First WATCH-or-higher PSPS date remains Fri, Aug 28.
- Method: compares current forecast evidence against prior local forecast history.

Notable changes:
- First WATCH-or-higher PSPS date remains Fri, Aug 28.
- Sun, Aug 30: easing vs prior run; PSPS WATCH -> WATCH; score -7, wind -1 mph, RH +4%, red-flag hours -1.
- Fri, Aug 28: easing vs prior run; PSPS WATCH -> WATCH; score -7, wind -1 mph, RH 0%, red-flag hours -2. Driver shifted to Arboles / southwest county.

## Public Analysis Export

- Summary: Highest LPEA PSPS concern is Sat, Aug 29 near Arboles / southwest county (LIKELY 65/100), driven by red-flag wind/gust signal near 28 mph; red-flag RH near 15%; 3 sampled hours meet red-flag screen. NIFC reports 3 current wildfires in Archuleta County.
- Trend: Momentum is easing versus the prior run (Aug 24 at 9:55 AM MDT); forecast volatility is medium and first WATCH-or-higher date is Fri, Aug 28.
- Confidence: **MEDIUM** (74/100)
- First WATCH-or-higher PSPS date: Fri, Aug 28
- PSPS peak: Sat, Aug 29 near Arboles / southwest county at LIKELY 65/100
- Red Flag peak: Sat, Aug 29 near Arboles / southwest county at LIKELY 78/100
- Weather fire-potential peak: Sat, Aug 29 near Chimney Rock / west county at VERY HIGH 78/100
- LPEA operational outage context: No active outages are listed by the official LPEA outage viewer.
- Public JSON: `archuleta_red_flag_monitor/public_analysis_export.json`

What changed:
- First WATCH-or-higher PSPS date remains Fri, Aug 28.
- Sun, Aug 30: easing vs prior run; PSPS WATCH -> WATCH; score -7, wind -1 mph, RH +4%, red-flag hours -1.
- Fri, Aug 28: easing vs prior run; PSPS WATCH -> WATCH; score -7, wind -1 mph, RH 0%, red-flag hours -2. Driver shifted to Arboles / southwest county.

What to watch next:
- Check whether the largest day-level changes line up with wind/RH movement or public-source context.
- Check whether the LPEA active match is still a broad red-flag banner rather than direct PSPS/outage intent.
- Watch whether the highest-risk locations remain consistent across runs or the driver area is moving.
- If a PSPS occurs, log the confirmed date, location, and source so future hit-rate scoring can improve.

## PSPS Likelihood

- **PSPS means Public Safety Power Shutoff:** a planned, safety-related power shutoff LPEA may use during dangerous fire-weather conditions to reduce wildfire ignition risk. See [LPEA PSPS guidance](https://lpea.coop/psps) and the [LPEA outage center](https://lpea.coop/outage-center); if power is out, also check the [LPEA outage map](https://outage.lpea.coop).
- Overall: **LIKELY** - PSPS likelihood is high on weather-driven red-flag days; prepare for possible LPEA safety-related interruption behavior.
- Likely PSPS watch dates: Sat, Aug 29
- PSPS watch dates: Fri, Aug 28; Sun, Aug 30
- LPEA signal basis: LPEA active/update source contains red-flag, wildfire, or power-interruption language.
- Note: This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

| Date | PSPS likelihood | Driver locations | Weather basis |
| --- | --- | --- | --- |
| Mon, Aug 24 | ELEVATED | Arboles / southwest county (ELEVATED 24/100); Ignacio / southeast La Plata County (ELEVATED 22/100); Durango / La Plata County (ELEVATED 18/100) | Top weather score 22/100 at Arboles / southwest county. Weather score 22/100: RH 19%, wind/gust 22 mph, red-flag hours 0, near-threshold hours 0. |
| Tue, Aug 25 | ELEVATED | Arboles / southwest county (ELEVATED 40/100); Ignacio / southeast La Plata County (ELEVATED 28/100); Durango / La Plata County (ELEVATED 24/100) | Top weather score 38/100 at Arboles / southwest county. Weather score 38/100: RH 16%, wind/gust 22 mph, red-flag hours 0, near-threshold hours 3. |
| Wed, Aug 26 | ELEVATED | Arboles / southwest county (ELEVATED 30/100); Chimney Rock / west county (ELEVATED 26/100); Bayfield / east La Plata County (ELEVATED 24/100) | Top weather score 28/100 at Arboles / southwest county. Weather score 28/100: RH 17%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 1. |
| Thu, Aug 27 | ELEVATED | Arboles / southwest county (ELEVATED 40/100); Chimney Rock / west county (ELEVATED 40/100); Ignacio / southeast La Plata County (ELEVATED 28/100) | Top weather score 38/100 at Arboles / southwest county. Weather score 38/100: RH 16%, wind/gust 22 mph, red-flag hours 0, near-threshold hours 2. |
| Fri, Aug 28 | WATCH | Arboles / southwest county (WATCH 50/100); Ignacio / southeast La Plata County (WATCH 48/100); Chimney Rock / west county (WATCH 46/100) | Top weather score 48/100 at Arboles / southwest county. Weather score 48/100: RH 14%, wind/gust 23 mph, red-flag hours 0, near-threshold hours 4. |
| Sat, Aug 29 | LIKELY | Arboles / southwest county (LIKELY 65/100); Chimney Rock / west county (WATCH 59/100); Durango / La Plata County (WATCH 53/100); Ignacio / southeast La Plata County (WATCH 51/100) | Top weather score 63/100 at Arboles / southwest county. Weather score 63/100: RH 15%, wind/gust 28 mph, red-flag hours 3, near-threshold hours 5. |
| Sun, Aug 30 | WATCH | Arboles / southwest county (WATCH 56/100) | Top weather score 54/100 at Arboles / southwest county. Weather score 54/100: RH 18%, wind/gust 25 mph, red-flag hours 0, near-threshold hours 2. |

## Area-Specific Outlook

| Area | Today | Peak this run | Highest-risk window |
| --- | --- | --- | --- |
| Arboles | ELEVATED 24/100 | Sat, Aug 29: LIKELY 65/100 | 2 PM-6 PM local; 5 near/red-flag threshold hours. |
| Chimney Rock | LOW 16/100 | Sat, Aug 29: WATCH 59/100 | 2 PM-6 PM local; 5 near/red-flag threshold hours. |
| Durango | ELEVATED 18/100 | Sat, Aug 29: WATCH 53/100 | 4 PM-5 PM local; 2 near/red-flag threshold hours. |
| Ignacio | ELEVATED 22/100 | Sat, Aug 29: WATCH 51/100 | 2 PM-5 PM local; 4 near/red-flag threshold hours. |
| Bayfield | ELEVATED 18/100 | Sat, Aug 29: WATCH 49/100 | 3 PM-5 PM local; 3 near/red-flag threshold hours. |
| Chromo | LOW 10/100 | Sat, Aug 29: ELEVATED 40/100 | 3 PM-5 PM local; 3 near/red-flag threshold hours. |
| Pagosa Springs | LOW 12/100 | Sat, Aug 29: ELEVATED 26/100 | Peak ingredients near 3 PM local; RH 20%, wind 24 mph. |
| Piedra | LOW 10/100 | Sat, Aug 29: ELEVATED 24/100 | Peak ingredients near 3 PM local; RH 21%, wind 23 mph. |

## Current Fires + Evacuations

- Incident summary: 3 current wildfires reported in Archuleta County; no current evacuation notice detected in checked county feeds.
- Evacuation status: **NONE DETECTED** - No current evacuation order or warning detected in the checked official county feeds.
- Safety note: Current incidents and evacuation notices are operational context. They do not raise PSPS scores by themselves; follow official evacuation instructions immediately.

### Current NIFC Incidents

| Incident | Type | Size | Containment | Nearest monitored area | Updated |
| --- | --- | --- | --- | --- | --- |
| Rio Blanco | Wildfire | 1,387.74 acres | 100% | Chromo / southeast county (9.9 mi) | Aug 18 at 7:20 PM MDT |
| Snow Springs | Wildfire | 1.00 acres | Not reported | Chimney Rock / west county (6.8 mi) | Aug 24 at 3:49 PM MDT |
| Spring Basin | Wildfire | 0.10 acres | Not reported | Chromo / southeast county (10.2 mi) | Aug 24 at 3:47 PM MDT |

Official links: [NIFC map](https://www.nifc.gov/fire-information/maps), [Archuleta County fire updates](https://sheriff.archuletacounty.gov/divisions/emergency-operations/fire-updates-and-information/), [County alerts](https://nixle.us/archuleta-county-office-of-emergency-management-aux/), [Watch Duty](https://app.watchduty.org/)

## Fire Posture + Restrictions

- Summary: 3 official sources indicate fire restrictions or staged restrictions.
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
| Durango | UNKNOWN | UNKNOWN | [City of Durango](https://www.durangoco.gov/) |
| Southern Ute / Ignacio | UNKNOWN | UNKNOWN | [Southern Ute Indian Tribe](https://www.southernute-nsn.gov/) |

## Forecast Calibration

### PSPS Calibration

- Summary: No confirmed LPEA PSPS events logged yet; calibration will start once events are added.
- Confirmed PSPS events logged: 0
- Candidate/unconfirmed events logged: 0
- WATCH/LIKELY false-watch past days: 63
- Pending WATCH/LIKELY dates in current forecast: Fri, Aug 28; Sat, Aug 29; Sun, Aug 30
- Calibration source: manual PSPS event log plus forecast history from prior monitor runs.

### Red Flag / Fire Weather Calibration

- Summary: 3/3 official Red Flag / Fire Weather episodes had a pre-alert HIGH monitor signal; date-level result was 21/21. Episode-average lead time: 3.5 days.
- Official alert episodes logged: 3 (21 alert dates)
- Episode-level pre-alert HIGH hit rate: 100%
- Date-level pre-alert HIGH hit rate: 100%
- Episode-level average lead time: 3.5 days
- HIGH false-watch past days: 21
- Pending HIGH dates in current forecast: Sat, Aug 29
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
- Active/update source pages with matches: LPEA homepage (public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation, restoration); LPEA X (power outage, outage map, high winds, restore power); LPEA LinkedIn (wildfire, public safety power shutoff, psps, power shutoff, shutoff, deenergize)
- Distinct active/update signals: LPEA X (power outage, outage map, high winds, restore power); LPEA X (power outage, outage map, high winds, restore power); LinkedIn PSPS explainer post (wildfire, public safety power shutoff, psps, power shutoff, shutoff, deenergize); LinkedIn PSPS explainer post (wildfire, public safety power shutoff, psps, power shutoff, shutoff, deenergize)
- Example signal: ...ibrary! 1 2 536 LPEA @LaPlataElectric May 7, 2024 LPEA members are experiencing power outages in the Bayfield and Pagosa Springs areas. Approximately 200 meters are out and it is suspected that the high winds are...
- Reference/context hits: [LPEA outage center](https://lpea.coop/outage-center); [LPEA wildfire / public safety power shutoffs](https://lpea.coop/psps); [LPEA red flag outage impact page](https://lpea.coop/outages/red-flag-warnings-and-impact-outages-prioritizing-safety-our-members); [LPEA fire mitigation](https://lpea.coop/fire-mitigation); [LPEA latest news](https://lpea.coop/Posts)

**Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## Next 7 Days

| Date | Tier | Main reason | Worst sampled metrics |
| --- | --- | --- | --- |
| Mon, Aug 24 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 25%, wind/gust 17 mph, thunder 17%<br>Arboles / southwest county: RH 19%, wind/gust 22 mph, thunder 7%<br>Chimney Rock / west county: RH 19%, wind/gust 18 mph, thunder 12% |
| Tue, Aug 25 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 16%, wind/gust 22 mph, thunder 5% |
| Wed, Aug 26 | ELEVATED | Chimney Rock / west county: Elevated ingredient present: dry-thunder probability reaches 18%. | Chimney Rock / west county: RH 16%, wind/gust 18 mph, thunder 18% |
| Thu, Aug 27 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 16%, wind/gust 22 mph, thunder 10%<br>Chimney Rock / west county: RH 17%, wind/gust 21 mph, thunder 26% |
| Fri, Aug 28 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 14%, wind/gust 23 mph, thunder 3%<br>Chimney Rock / west county: RH 13%, wind/gust 22 mph, thunder 3%<br>Durango / La Plata County: RH 16%, wind/gust 22 mph, thunder 6% |
| Sat, Aug 29 | HIGH | Arboles / southwest county: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Arboles / southwest county: RH 15%, wind/gust 28 mph, thunder 24%<br>Chimney Rock / west county: RH 14%, wind/gust 25 mph, thunder 26%<br>Chromo / southeast county: RH 18%, wind/gust 22 mph, thunder 36% |
| Sun, Aug 30 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 18%, wind/gust 25 mph, thunder 22%<br>Chimney Rock / west county: RH 17%, wind/gust 22 mph, thunder 26%<br>Ignacio / southeast La Plata County: RH 20%, wind/gust 25 mph, thunder 22% |

## Sample Point Status

- Pagosa Springs: COZ295 (matches), forecast zone COZ023, county zone COC007
- Arboles / southwest county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Chimney Rock / west county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Piedra / north county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Chromo / southeast county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Durango / La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Bayfield / east La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Ignacio / southeast La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
