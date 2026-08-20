# Archuleta County fire-weather monitor

Generated: Aug 20, 2026 at 4:20 PM MDT (Pagosa Springs, CO local time)
Next update: Aug 20, 2026 at 5:20 PM MDT (Pagosa Springs, CO local time)
Date/time basis: Pagosa Springs, CO local time (America/Denver)
> **Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## At A Glance

- Fire-weather tier: **CONCERN**
- PSPS likelihood: **WATCH**
- PSPS likely dates: None
- PSPS watch dates: Tue, Aug 25; Wed, Aug 26
- Monitor heads-up recommended: **YES** - Send this monitor report because fire-weather screening tier is CONCERN; PSPS screening level is WATCH; a material current wildfire is reported in Archuleta County. This is not an official LPEA or NWS notice.
- HIGH dates: None
- CONCERN dates: Thu, Aug 20; Mon, Aug 24; Tue, Aug 25; Wed, Aug 26
- ELEVATED dates: Fri, Aug 21
- Official NWS Red Flag / Fire Weather alerts (COZ295): 0
- LPEA signal: `operational_outage_active` - Official LPEA outage data indicates an operational outage; use as grid context, not PSPS/fire evidence unless LPEA identifies that cause.
- LPEA source coverage: 13 sources; 5/5 official social sources reachable
- Current Archuleta County wildfires: 2
- Official evacuation notices: No current evacuation order or warning detected in the checked official county feeds.
- NWS discussion: No concerning fire-weather language found in latest GJT discussion.

## Decision Support

- Summary: Highest LPEA PSPS concern is Wed, Aug 26 near Durango / La Plata County (WATCH 50/100), driven by near-threshold wind/gust signal near 21 mph; red-flag RH near 15%; 2 sampled hours are near red-flag thresholds. NIFC reports 2 current wildfires in Archuleta County.
- Confidence: **MEDIUM** (74/100) - 8/8 sampled weather points available; 7/7 fire-posture sources reachable; official NWS alert zones checked; 13/13 LPEA public sources reachable; LPEA active/update sources checked; active LPEA operational outage context checked separately from PSPS scoring; authoritative NIFC current-incident feed checked for Archuleta County; official Archuleta County evacuation feeds checked; forecast changed moderately versus prior run; no confirmed PSPS events logged yet for calibration
- Weather fire-potential peak: Wed, Aug 26: Durango / La Plata County VERY HIGH 72/100
- Red Flag likelihood peak: Wed, Aug 26: Ignacio / southeast La Plata County WATCH 58/100
- LPEA PSPS peak: Wed, Aug 26: Durango / La Plata County WATCH 50/100
- Method: rules-based decision support using public weather, fire-posture, and LPEA source signals; scores are screening estimates, not official or statistically calibrated probabilities.

| Date | Weather fire potential | Red Flag likelihood | LPEA PSPS | Main window |
| --- | --- | --- | --- | --- |
| Thu, Aug 20 | Arboles / southwest county: HIGH 55/100 | Arboles / southwest county: POSSIBLE 50/100 | Arboles / southwest county: ELEVATED 29/100 | Peak ingredients near 5 PM local; RH 25%, wind 20 mph. |
| Fri, Aug 21 | Chimney Rock / west county: MODERATE 46/100 | Chimney Rock / west county: LOW 25/100 | Arboles / southwest county: ELEVATED 30/100 | Peak ingredients near 6 PM local; RH 32%, wind 22 mph. |
| Sat, Aug 22 | Durango / La Plata County: MODERATE 38/100 | Arboles / southwest county: LOW 8/100 | Arboles / southwest county: ELEVATED 24/100 | Peak ingredients near 4 PM local; RH 20%, wind 21 mph. |
| Sun, Aug 23 | Durango / La Plata County: LOW 30/100 | Arboles / southwest county: LOW 8/100 | Arboles / southwest county: ELEVATED 24/100 | Peak ingredients near 3 PM local; RH 19%, wind 21 mph. |
| Mon, Aug 24 | Arboles / southwest county: HIGH 55/100 | Arboles / southwest county: POSSIBLE 50/100 | Arboles / southwest county: ELEVATED 40/100 | 3 PM-5 PM local; 3 near/red-flag threshold hours. |
| Tue, Aug 25 | Durango / La Plata County: HIGH 63/100 | Arboles / southwest county: WATCH 55/100 | Arboles / southwest county: WATCH 46/100 | 3 PM-5 PM local; 3 near/red-flag threshold hours. |
| Wed, Aug 26 | Durango / La Plata County: VERY HIGH 72/100 | Ignacio / southeast La Plata County: WATCH 58/100 | Durango / La Plata County: WATCH 50/100 | 4 PM-5 PM local; 2 near/red-flag threshold hours. |

## Analyst Interpretation

- Headline: PSPS screening remains WATCH for Aug 25-26; a new small wildfire is listed near Pagosa, while no official COZ295 alert or fire-related outage is reported.
- Summary: PSPS screening remains WATCH on Tue, Aug 25 near Arboles (46/100) and Wed, Aug 26 near Durango (50/100); these are screening estimates, not LPEA shutoff notices. Wednesday also carries the peak weather fire potential, VERY HIGH 72/100 near Durango. Official COZ295 alerts remain at zero; the official LPEA viewer lists one localized two-customer outage with no fire or PSPS cause, and NIFC now lists the 0.5-acre Swiss Roll fire with no evacuation notice detected.
- Uncertainty: Confidence is MEDIUM 74/100 because PSPS scoring has no confirmed-event calibration; the forecast eased overall but the Aug 25-26 WATCH signal and new Swiss Roll incident require continued official-source checks.
- Evidence used: overall_status, weather_peaks, official_alerts, forecast_change, lpea_context, fire_posture, active_incidents, calibration
- This interpretation cannot change the deterministic tiers, scores, official alerts, or notification decision.

Changing drivers:
- The first WATCH-or-higher PSPS date remains Tuesday, Aug 25; Wednesday now peaks at WATCH 50/100 near Durango.
- Thursday eased 12 points as wind dropped 3 mph and humidity rose 4%; Sunday eased 16 points.
- NIFC added the 0.5-acre Swiss Roll wildfire near Pagosa Springs; containment is not reported and no evacuation notice was detected.
- The official LPEA viewer lists one unplanned two-customer outage near Durango, with no fire-weather or PSPS cause identified.

What to watch next:
- Recheck the Aug 25-26 WATCH signal, especially Wednesday afternoon wind and humidity near Durango and Ignacio.
- Monitor Swiss Roll acreage, containment, and official county evacuation sources for any change.
- Treat the two-customer LPEA outage as operational context only unless LPEA identifies a fire or PSPS cause.
- Continue official NWS checks; the current COZ295 alert count is zero.

## Trend Intelligence

- Summary: Momentum is easing versus the prior run (Aug 20 at 4:24 AM MDT); forecast volatility is medium and first WATCH-or-higher date is Tue, Aug 25.
- Momentum: **Easing**
- Forecast volatility: **MEDIUM** (26/100)
- First WATCH-or-higher PSPS date: Tue, Aug 25
- Watch-date movement: First WATCH-or-higher PSPS date remains Tue, Aug 25.
- Method: compares current forecast evidence against prior local forecast history.

Notable changes:
- First WATCH-or-higher PSPS date remains Tue, Aug 25.
- Thu, Aug 20: easing vs prior run; PSPS ELEVATED -> ELEVATED; score -12, wind -3 mph, RH +4%, red-flag hours 0. Driver shifted to Arboles / southwest county.
- Sun, Aug 23: easing vs prior run; PSPS ELEVATED -> ELEVATED; score -16, wind -1 mph, RH +1%, red-flag hours 0. Driver shifted to Arboles / southwest county.

## Public Analysis Export

- Summary: Highest LPEA PSPS concern is Wed, Aug 26 near Durango / La Plata County (WATCH 50/100), driven by near-threshold wind/gust signal near 21 mph; red-flag RH near 15%; 2 sampled hours are near red-flag thresholds. NIFC reports 2 current wildfires in Archuleta County.
- Trend: Momentum is easing versus the prior run (Aug 20 at 4:24 AM MDT); forecast volatility is medium and first WATCH-or-higher date is Tue, Aug 25.
- Confidence: **MEDIUM** (74/100)
- First WATCH-or-higher PSPS date: Tue, Aug 25
- PSPS peak: Wed, Aug 26 near Durango / La Plata County at WATCH 50/100
- Red Flag peak: Wed, Aug 26 near Ignacio / southeast La Plata County at WATCH 58/100
- Weather fire-potential peak: Wed, Aug 26 near Durango / La Plata County at VERY HIGH 72/100
- LPEA operational outage context: 1 active outage; 0 planned and 1 unplanned; 2 customers out. No fire-weather or PSPS cause is identified.
- Public JSON: `archuleta_red_flag_monitor/public_analysis_export.json`

What changed:
- First WATCH-or-higher PSPS date remains Tue, Aug 25.
- Thu, Aug 20: easing vs prior run; PSPS ELEVATED -> ELEVATED; score -12, wind -3 mph, RH +4%, red-flag hours 0. Driver shifted to Arboles / southwest county.
- Sun, Aug 23: easing vs prior run; PSPS ELEVATED -> ELEVATED; score -16, wind -1 mph, RH +1%, red-flag hours 0. Driver shifted to Arboles / southwest county.

What to watch next:
- Check whether the largest day-level changes line up with wind/RH movement or public-source context.
- Check whether the LPEA active match is still a broad red-flag banner rather than direct PSPS/outage intent.
- Watch whether the highest-risk locations remain consistent across runs or the driver area is moving.
- If a PSPS occurs, log the confirmed date, location, and source so future hit-rate scoring can improve.

## PSPS Likelihood

- **PSPS means Public Safety Power Shutoff:** a planned, safety-related power shutoff LPEA may use during dangerous fire-weather conditions to reduce wildfire ignition risk. See [LPEA PSPS guidance](https://lpea.coop/psps) and the [LPEA outage center](https://lpea.coop/outage-center); if power is out, also check the [LPEA outage map](https://outage.lpea.coop).
- Overall: **WATCH** - PSPS watch screening is present from forecast thresholds or direct LPEA shutoff language; monitor official LPEA and NWS updates.
- Likely PSPS watch dates: None
- PSPS watch dates: Tue, Aug 25; Wed, Aug 26
- LPEA signal basis: LPEA active/update source contains red-flag, wildfire, or power-interruption language.
- Note: This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

| Date | PSPS likelihood | Driver locations | Weather basis |
| --- | --- | --- | --- |
| Thu, Aug 20 | ELEVATED | Arboles / southwest county (ELEVATED 29/100); Ignacio / southeast La Plata County (ELEVATED 22/100); Durango / La Plata County (ELEVATED 18/100) | Top weather score 27/100 at Arboles / southwest county. Weather score 27/100: RH 18%, wind/gust 20 mph, red-flag hours 0, near-threshold hours 0. |
| Fri, Aug 21 | ELEVATED | Arboles / southwest county (ELEVATED 30/100); Ignacio / southeast La Plata County (ELEVATED 28/100); Chimney Rock / west county (ELEVATED 28/100) | Top weather score 28/100 at Arboles / southwest county. Weather score 28/100: RH 16%, wind/gust 22 mph, red-flag hours 0, near-threshold hours 0. |
| Sat, Aug 22 | ELEVATED | Arboles / southwest county (ELEVATED 24/100); Durango / La Plata County (ELEVATED 24/100); Ignacio / southeast La Plata County (ELEVATED 22/100) | Top weather score 22/100 at Arboles / southwest county. Weather score 22/100: RH 19%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 0. |
| Sun, Aug 23 | ELEVATED | Arboles / southwest county (ELEVATED 24/100); Ignacio / southeast La Plata County (ELEVATED 22/100); Durango / La Plata County (ELEVATED 18/100) | Top weather score 22/100 at Arboles / southwest county. Weather score 22/100: RH 19%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 0. |
| Mon, Aug 24 | ELEVATED | Arboles / southwest county (ELEVATED 40/100); Ignacio / southeast La Plata County (ELEVATED 28/100); Chimney Rock / west county (ELEVATED 26/100) | Top weather score 38/100 at Arboles / southwest county. Weather score 38/100: RH 17%, wind/gust 23 mph, red-flag hours 0, near-threshold hours 3. |
| Tue, Aug 25 | WATCH | Arboles / southwest county (WATCH 46/100) | Top weather score 44/100 at Arboles / southwest county. Weather score 44/100: RH 15%, wind/gust 22 mph, red-flag hours 0, near-threshold hours 3. |
| Wed, Aug 26 | WATCH | Durango / La Plata County (WATCH 50/100); Ignacio / southeast La Plata County (WATCH 48/100); Arboles / southwest county (WATCH 46/100) | Top weather score 48/100 at Durango / La Plata County. Weather score 48/100: RH 15%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 2. |

## Area-Specific Outlook

| Area | Today | Peak this run | Highest-risk window |
| --- | --- | --- | --- |
| Durango | ELEVATED 18/100 | Wed, Aug 26: WATCH 50/100 | 4 PM-5 PM local; 2 near/red-flag threshold hours. |
| Ignacio | ELEVATED 22/100 | Wed, Aug 26: WATCH 48/100 | 3 PM-6 PM local; 4 near/red-flag threshold hours. |
| Arboles | ELEVATED 29/100 | Tue, Aug 25: WATCH 46/100 | 3 PM-5 PM local; 3 near/red-flag threshold hours. |
| Bayfield | ELEVATED 18/100 | Tue, Aug 25: ELEVATED 44/100 | 4 PM-5 PM local; 2 near/red-flag threshold hours. |
| Chimney Rock | LOW 16/100 | Tue, Aug 25: ELEVATED 32/100 | Peak ingredients near 3 PM local; RH 15%, wind 20 mph. |
| Chromo | LOW 10/100 | Tue, Aug 25: ELEVATED 26/100 | Peak ingredients near 4 PM local; RH 18%, wind 17 mph. |
| Pagosa Springs | LOW 12/100 | Fri, Aug 21: ELEVATED 18/100 | Peak ingredients near 4 PM local; RH 24%, wind 16 mph. |
| Piedra | LOW 10/100 | Tue, Aug 25: LOW 16/100 | Peak ingredients near 11 PM local; RH 52%, wind 17 mph. |

## Current Fires + Evacuations

- Incident summary: 2 current wildfires reported in Archuleta County; no current evacuation notice detected in checked county feeds.
- Evacuation status: **NONE DETECTED** - No current evacuation order or warning detected in the checked official county feeds.
- Safety note: Current incidents and evacuation notices are operational context. They do not raise PSPS scores by themselves; follow official evacuation instructions immediately.

### Current NIFC Incidents

| Incident | Type | Size | Containment | Nearest monitored area | Updated |
| --- | --- | --- | --- | --- | --- |
| Rio Blanco | Wildfire | 1,388.00 acres | 100% | Chromo / southeast county (9.9 mi) | Aug 18 at 7:20 PM MDT |
| Swiss Roll | Wildfire | 0.50 acres | Not reported | Pagosa Springs (14.5 mi) | Aug 20 at 9:54 AM MDT |

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
- WATCH/LIKELY false-watch past days: 60
- Pending WATCH/LIKELY dates in current forecast: Tue, Aug 25; Wed, Aug 26
- Calibration source: manual PSPS event log plus forecast history from prior monitor runs.

### Red Flag / Fire Weather Calibration

- Summary: 3/3 official Red Flag / Fire Weather episodes had a pre-alert HIGH monitor signal; date-level result was 21/21. Episode-average lead time: 3.5 days.
- Official alert episodes logged: 3 (21 alert dates)
- Episode-level pre-alert HIGH hit rate: 100%
- Date-level pre-alert HIGH hit rate: 100%
- Episode-level average lead time: 3.5 days
- HIGH false-watch past days: 21
- Pending HIGH dates in current forecast: None
- Calibration source: official NWS Red Flag / Fire Weather alert dates plus forecast history from prior monitor runs.

## Official Weather Alerts

- Monitored NWS zones: COC007, COC067, COZ019, COZ022, COZ023, COZ295
- No active official NWS Red Flag / Fire Weather or related weather alerts found for monitored zones.

## LPEA Power Signal

- Status: `operational_outage_active` - Official LPEA outage data indicates an operational outage; use as grid context, not PSPS/fire evidence unless LPEA identifies that cause.
- Meaning: Active source match means a monitored LPEA active/update source currently contains fire, outage, PSPS, or power-interruption keywords. Operational outages are shown separately and are not treated as PSPS/fire evidence unless the source text says so.
- Operational outage context: 1 active outage; 0 planned and 1 unplanned; 2 customers out. No fire-weather or PSPS cause is identified.
- Source coverage: 13 sources; 5/5 official social sources reachable
- Evidence quality: 0 operational, 4 active/update, 0 archive/context, 6 reference source matches.
- Operational outage source links: [#1 SKIER PL PURGATORY LIFT 8](https://outage.lpea.coop)
- Active/update source pages with matches: LPEA homepage (public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation, restoration); LPEA X (power outage, outage map, high winds, restore power); LPEA LinkedIn (wildfire, public safety power shutoff, psps, power shutoff, shutoff, deenergize)
- Distinct active/update signals: LPEA X (power outage, outage map, high winds, restore power); LPEA X (power outage, outage map, high winds, restore power); LPEA LinkedIn (wildfire, public safety power shutoff, psps, power shutoff, shutoff, deenergize); LinkedIn PSPS explainer post (wildfire, public safety power shutoff, psps, power shutoff, shutoff, deenergize)
- Example signal: ...ibrary! 1 2 536 LPEA @LaPlataElectric May 7, 2024 LPEA members are experiencing power outages in the Bayfield and Pagosa Springs areas. Approximately 200 meters are out and it is suspected that the high winds are...
- Reference/context hits: [LPEA outage center](https://lpea.coop/outage-center); [LPEA wildfire / public safety power shutoffs](https://lpea.coop/psps); [LPEA red flag outage impact page](https://lpea.coop/outages/red-flag-warnings-and-impact-outages-prioritizing-safety-our-members); [LPEA fire mitigation](https://lpea.coop/fire-mitigation); [LPEA latest news](https://lpea.coop/Posts)

**Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## Next 7 Days

| Date | Tier | Main reason | Worst sampled metrics |
| --- | --- | --- | --- |
| Thu, Aug 20 | CONCERN | Arboles / southwest county: Dry-thunder signal: 1 hourly period combine thunder near 20% with limited precipitation and dry air. | Arboles / southwest county: RH 18%, wind/gust 20 mph, thunder 20% |
| Fri, Aug 21 | ELEVATED | Chimney Rock / west county: Elevated ingredient present: very low RH forecast near 15%. | Chimney Rock / west county: RH 15%, wind/gust 18 mph, thunder 33% |
| Sat, Aug 22 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 23%, wind/gust 18 mph, thunder 54%<br>Arboles / southwest county: RH 19%, wind/gust 21 mph, thunder 35%<br>Chimney Rock / west county: RH 18%, wind/gust 20 mph, thunder 44% |
| Sun, Aug 23 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 24%, wind/gust 20 mph, thunder 41%<br>Arboles / southwest county: RH 19%, wind/gust 21 mph, thunder 21%<br>Chimney Rock / west county: RH 19%, wind/gust 20 mph, thunder 30% |
| Mon, Aug 24 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 17%, wind/gust 23 mph, thunder 8%<br>Chimney Rock / west county: RH 16%, wind/gust 20 mph, thunder 19% |
| Tue, Aug 25 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 15%, wind/gust 22 mph, thunder 9%<br>Chimney Rock / west county: RH 15%, wind/gust 20 mph, thunder 15%<br>Chromo / southeast county: RH 18%, wind/gust 17 mph, thunder 15% |
| Wed, Aug 26 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 13%, wind/gust 21 mph, thunder 10%<br>Chimney Rock / west county: RH 13%, wind/gust 20 mph, thunder 18%<br>Durango / La Plata County: RH 15%, wind/gust 21 mph, thunder 19% |

## Sample Point Status

- Pagosa Springs: COZ295 (matches), forecast zone COZ023, county zone COC007
- Arboles / southwest county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Chimney Rock / west county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Piedra / north county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Chromo / southeast county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Durango / La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Bayfield / east La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Ignacio / southeast La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
