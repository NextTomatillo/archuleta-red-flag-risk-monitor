# Archuleta County fire-weather monitor

Generated: Aug 23, 2026 at 4:42 PM MDT (Pagosa Springs, CO local time)
Next update: Aug 23, 2026 at 5:20 PM MDT (Pagosa Springs, CO local time)
Date/time basis: Pagosa Springs, CO local time (America/Denver)
> **Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## At A Glance

- Fire-weather tier: **HIGH**
- PSPS likelihood: **LIKELY**
- PSPS likely dates: Fri, Aug 28; Sat, Aug 29
- PSPS watch dates: Wed, Aug 26; Thu, Aug 27
- Monitor heads-up recommended: **YES** - Send this monitor report because fire-weather screening tier is HIGH; PSPS screening level is LIKELY; a material current wildfire is reported in Archuleta County. This is not an official LPEA or NWS notice.
- HIGH dates: Fri, Aug 28; Sat, Aug 29
- CONCERN dates: Mon, Aug 24; Tue, Aug 25; Wed, Aug 26; Thu, Aug 27
- ELEVATED dates: None
- Official NWS Red Flag / Fire Weather alerts (COZ295): 0
- LPEA signal: `operational_outage_active` - Official LPEA outage data indicates an operational outage; use as grid context, not PSPS/fire evidence unless LPEA identifies that cause.
- LPEA source coverage: 13 sources; 5/5 official social sources reachable
- Current Archuleta County wildfires: 3
- Official evacuation notices: No current evacuation order or warning detected in the checked official county feeds.
- NWS discussion: No concerning fire-weather language found in latest GJT discussion.

## Decision Support

- Summary: Highest LPEA PSPS concern is Sat, Aug 29 near Arboles / southwest county (LIKELY 73/100), driven by red-flag wind/gust signal near 28 mph; very dry RH near 11%; 4 sampled hours meet red-flag screen. NIFC reports 3 current wildfires in Archuleta County.
- Confidence: **MEDIUM** (69/100) - 8/8 sampled weather points available; 7/7 fire-posture sources reachable; official NWS alert zones checked; 13/13 LPEA public sources reachable; LPEA active/update sources checked; active LPEA operational outage context checked separately from PSPS scoring; authoritative NIFC current-incident feed checked for Archuleta County; official Archuleta County evacuation feeds checked; forecast changed substantially versus prior run; no confirmed PSPS events logged yet for calibration
- Weather fire-potential peak: Sat, Aug 29: Durango / La Plata County EXTREME 88/100
- Red Flag likelihood peak: Sat, Aug 29: Ignacio / southeast La Plata County LIKELY 88/100
- LPEA PSPS peak: Sat, Aug 29: Arboles / southwest county LIKELY 73/100
- Method: rules-based decision support using public weather, fire-posture, and LPEA source signals; scores are screening estimates, not official or statistically calibrated probabilities.

| Date | Weather fire potential | Red Flag likelihood | LPEA PSPS | Main window |
| --- | --- | --- | --- | --- |
| Sun, Aug 23 | Pagosa Springs: LOW 24/100 | Pagosa Springs: LOW 0/100 | Pagosa Springs: LOW 12/100 | Peak ingredients near 4 PM local; RH 34%, wind 17 mph. |
| Mon, Aug 24 | Arboles / southwest county: HIGH 55/100 | Arboles / southwest county: POSSIBLE 51/100 | Arboles / southwest county: ELEVATED 44/100 | 3 PM-4 PM local; 2 near/red-flag threshold hours. |
| Tue, Aug 25 | Arboles / southwest county: HIGH 55/100 | Arboles / southwest county: POSSIBLE 50/100 | Arboles / southwest county: ELEVATED 40/100 | 3 PM-5 PM local; 3 near/red-flag threshold hours. |
| Wed, Aug 26 | Chimney Rock / west county: HIGH 69/100 | Arboles / southwest county: POSSIBLE 54/100 | Chimney Rock / west county: WATCH 46/100 | 3 PM-4 PM local; 2 near/red-flag threshold hours. |
| Thu, Aug 27 | Chimney Rock / west county: VERY HIGH 83/100 | Chimney Rock / west county: WATCH 62/100 | Chimney Rock / west county: WATCH 53/100 | 3 PM-4 PM local; 2 near/red-flag threshold hours. |
| Fri, Aug 28 | Durango / La Plata County: EXTREME 85/100 | Arboles / southwest county: LIKELY 80/100 | Arboles / southwest county: LIKELY 69/100 | 3 PM-7 PM local; 5 near/red-flag threshold hours. |
| Sat, Aug 29 | Durango / La Plata County: EXTREME 88/100 | Ignacio / southeast La Plata County: LIKELY 88/100 | Arboles / southwest county: LIKELY 73/100 | 1 PM-7 PM local; 7 near/red-flag threshold hours. |

## Analyst Interpretation

- Headline: PSPS screening remains LIKELY Aug 28-29, peaking Saturday near Arboles; no official COZ295 alert or fire-related LPEA outage is reported.
- Summary: PSPS screening remains LIKELY Fri, Aug 28 and Sat, Aug 29; these are screening estimates, not LPEA shutoff notices. Saturday peaks near Arboles at LIKELY 73/100, while Ignacio reaches red-flag screening LIKELY 88/100 and Durango fire potential reaches EXTREME 88/100. Official COZ295 alerts remain zero; LPEA lists one unplanned one-customer outage near Pagosa Springs without a fire or PSPS cause, and no evacuation notice was detected for three listed wildfires.
- Uncertainty: Confidence is MEDIUM 69/100 because coverage is complete but forecast volatility remains HIGH 50/100; no confirmed PSPS events are available for calibration, so Aug 28-29 may still shift.
- Evidence used: overall_status, weather_peaks, official_alerts, forecast_change, lpea_context, fire_posture, active_incidents, calibration
- This interpretation cannot change the deterministic tiers, scores, official alerts, or notification decision.

Changing drivers:
- The first WATCH-or-higher PSPS date moved later from Tuesday, Aug 25 to Wednesday, Aug 26, while the overall level remains LIKELY.
- Wednesday rose from ELEVATED to WATCH by 18 points as the driver shifted to Chimney Rock / west county.
- Tuesday eased from WATCH to ELEVATED by 6 points, and today's Pagosa Springs screening eased to LOW.
- NIFC added the 0.10-acre Arroyo wildfire near Arboles; no evacuation notice was detected, and incidents remain operational context rather than PSPS score inputs.

What to watch next:
- Recheck the Aug 28-29 LIKELY window after the next forecast update because day-level signals remain volatile.
- Monitor Saturday afternoon near Arboles, Ignacio, and Durango, where the PSPS, red-flag, and fire-potential peaks align.
- Treat the one-customer Pagosa Springs outage as operational context unless LPEA identifies a fire or PSPS cause.
- Check official incident and evacuation feeds for changes to the new Arroyo wildfire and the other listed incidents.

## Trend Intelligence

- Summary: Momentum is steady versus the prior run (Aug 23 at 4:38 AM MDT); forecast volatility is high and first WATCH-or-higher date is Wed, Aug 26.
- Momentum: **Steady**
- Forecast volatility: **HIGH** (50/100)
- First WATCH-or-higher PSPS date: Wed, Aug 26
- Watch-date movement: First WATCH-or-higher PSPS date moved later from Tue, Aug 25 to Wed, Aug 26.
- Method: compares current forecast evidence against prior local forecast history.

Notable changes:
- First WATCH-or-higher PSPS date moved later from Tue, Aug 25 to Wed, Aug 26.
- Wed, Aug 26: worsening vs prior run; PSPS ELEVATED -> WATCH; score +18, wind +2 mph, RH +1%, red-flag hours 0. Driver shifted to Chimney Rock / west county.
- Sun, Aug 23: easing vs prior run; PSPS ELEVATED -> LOW; score -10, wind -2 mph, RH +4%, red-flag hours 0. Driver shifted to Pagosa Springs.
- Tue, Aug 25: easing vs prior run; PSPS WATCH -> ELEVATED; score -6, wind -1 mph, RH +1%, red-flag hours 0.
- Mon, Aug 24: worsening vs prior run; PSPS ELEVATED -> ELEVATED; score +16, wind 0 mph, RH +1%, red-flag hours 0. Driver shifted to Arboles / southwest county.

## Public Analysis Export

- Summary: Highest LPEA PSPS concern is Sat, Aug 29 near Arboles / southwest county (LIKELY 73/100), driven by red-flag wind/gust signal near 28 mph; very dry RH near 11%; 4 sampled hours meet red-flag screen. NIFC reports 3 current wildfires in Archuleta County.
- Trend: Momentum is steady versus the prior run (Aug 23 at 4:38 AM MDT); forecast volatility is high and first WATCH-or-higher date is Wed, Aug 26.
- Confidence: **MEDIUM** (69/100)
- First WATCH-or-higher PSPS date: Wed, Aug 26
- PSPS peak: Sat, Aug 29 near Arboles / southwest county at LIKELY 73/100
- Red Flag peak: Sat, Aug 29 near Ignacio / southeast La Plata County at LIKELY 88/100
- Weather fire-potential peak: Sat, Aug 29 near Durango / La Plata County at EXTREME 88/100
- LPEA operational outage context: 1 active outage; 0 planned and 1 unplanned; 1 customer out. No fire-weather or PSPS cause is identified.
- Public JSON: `archuleta_red_flag_monitor/public_analysis_export.json`

What changed:
- First WATCH-or-higher PSPS date moved later from Tue, Aug 25 to Wed, Aug 26.
- Wed, Aug 26: worsening vs prior run; PSPS ELEVATED -> WATCH; score +18, wind +2 mph, RH +1%, red-flag hours 0. Driver shifted to Chimney Rock / west county.
- Sun, Aug 23: easing vs prior run; PSPS ELEVATED -> LOW; score -10, wind -2 mph, RH +4%, red-flag hours 0. Driver shifted to Pagosa Springs.
- Tue, Aug 25: easing vs prior run; PSPS WATCH -> ELEVATED; score -6, wind -1 mph, RH +1%, red-flag hours 0.
- Mon, Aug 24: worsening vs prior run; PSPS ELEVATED -> ELEVATED; score +16, wind 0 mph, RH +1%, red-flag hours 0. Driver shifted to Arboles / southwest county.

What to watch next:
- Check whether the largest day-level changes line up with wind/RH movement or public-source context.
- Check whether the LPEA active match is still a broad red-flag banner rather than direct PSPS/outage intent.
- Watch whether the highest-risk locations remain consistent across runs or the driver area is moving.
- If a PSPS occurs, log the confirmed date, location, and source so future hit-rate scoring can improve.

## PSPS Likelihood

- **PSPS means Public Safety Power Shutoff:** a planned, safety-related power shutoff LPEA may use during dangerous fire-weather conditions to reduce wildfire ignition risk. See [LPEA PSPS guidance](https://lpea.coop/psps) and the [LPEA outage center](https://lpea.coop/outage-center); if power is out, also check the [LPEA outage map](https://outage.lpea.coop).
- Overall: **LIKELY** - PSPS likelihood is high on weather-driven red-flag days; prepare for possible LPEA safety-related interruption behavior.
- Likely PSPS watch dates: Fri, Aug 28; Sat, Aug 29
- PSPS watch dates: Wed, Aug 26; Thu, Aug 27
- LPEA signal basis: LPEA active/update source contains red-flag, wildfire, or power-interruption language.
- Note: This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

| Date | PSPS likelihood | Driver locations | Weather basis |
| --- | --- | --- | --- |
| Sun, Aug 23 | LOW | Pagosa Springs (LOW 12/100); Arboles / southwest county (LOW 10/100); Chimney Rock / west county (LOW 10/100) | Top weather score 8/100 at Pagosa Springs. Weather score 8/100: RH 34%, wind/gust 17 mph, red-flag hours 0, near-threshold hours 0. |
| Mon, Aug 24 | ELEVATED | Arboles / southwest county (ELEVATED 44/100); Chimney Rock / west county (ELEVATED 26/100); Durango / La Plata County (ELEVATED 24/100) | Top weather score 42/100 at Arboles / southwest county. Weather score 42/100: RH 18%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 2. |
| Tue, Aug 25 | ELEVATED | Arboles / southwest county (ELEVATED 40/100); Ignacio / southeast La Plata County (ELEVATED 38/100); Chimney Rock / west county (ELEVATED 32/100) | Top weather score 38/100 at Arboles / southwest county. Weather score 38/100: RH 16%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 3. |
| Wed, Aug 26 | WATCH | Chimney Rock / west county (WATCH 46/100) | Top weather score 44/100 at Chimney Rock / west county. Weather score 44/100: RH 15%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 2. |
| Thu, Aug 27 | WATCH | Chimney Rock / west county (WATCH 53/100) | Top weather score 51/100 at Chimney Rock / west county. Weather score 51/100: RH 15%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 2. |
| Fri, Aug 28 | LIKELY | Arboles / southwest county (LIKELY 69/100); Durango / La Plata County (LIKELY 69/100); Ignacio / southeast La Plata County (LIKELY 67/100); Bayfield / east La Plata County (LIKELY 65/100) | Top weather score 67/100 at Arboles / southwest county. Weather score 67/100: RH 12%, wind/gust 26 mph, red-flag hours 3, near-threshold hours 5. |
| Sat, Aug 29 | LIKELY | Arboles / southwest county (LIKELY 73/100); Ignacio / southeast La Plata County (LIKELY 71/100); Chimney Rock / west county (LIKELY 69/100); Durango / La Plata County (LIKELY 69/100) | Top weather score 71/100 at Arboles / southwest county. Weather score 71/100: RH 11%, wind/gust 28 mph, red-flag hours 4, near-threshold hours 7. |

## Area-Specific Outlook

| Area | Today | Peak this run | Highest-risk window |
| --- | --- | --- | --- |
| Arboles | LOW 10/100 | Sat, Aug 29: LIKELY 73/100 | 1 PM-7 PM local; 7 near/red-flag threshold hours. |
| Ignacio | LOW 8/100 | Sat, Aug 29: LIKELY 71/100 | 1 PM-8 PM local; 8 near/red-flag threshold hours. |
| Chimney Rock | LOW 10/100 | Sat, Aug 29: LIKELY 69/100 | 1 PM-7 PM local; 7 near/red-flag threshold hours. |
| Durango | LOW 10/100 | Fri, Aug 28: LIKELY 69/100 | 2 PM-7 PM local; 6 near/red-flag threshold hours. |
| Bayfield | LOW 10/100 | Sat, Aug 29: LIKELY 69/100 | 1 PM-8 PM local; 8 near/red-flag threshold hours. |
| Pagosa Springs | LOW 12/100 | Sat, Aug 29: WATCH 52/100 | 2 PM-6 PM local; 5 near/red-flag threshold hours. |
| Chromo | LOW 10/100 | Sat, Aug 29: WATCH 50/100 | 1 PM-6 PM local; 6 near/red-flag threshold hours. |
| Piedra | LOW 2/100 | Sat, Aug 29: ELEVATED 44/100 | 2 PM-5 PM local; 4 near/red-flag threshold hours. |

## Current Fires + Evacuations

- Incident summary: 3 current wildfires reported in Archuleta County; no current evacuation notice detected in checked county feeds.
- Evacuation status: **NONE DETECTED** - No current evacuation order or warning detected in the checked official county feeds.
- Safety note: Current incidents and evacuation notices are operational context. They do not raise PSPS scores by themselves; follow official evacuation instructions immediately.

### Current NIFC Incidents

| Incident | Type | Size | Containment | Nearest monitored area | Updated |
| --- | --- | --- | --- | --- | --- |
| Rio Blanco | Wildfire | 1,387.74 acres | 100% | Chromo / southeast county (9.9 mi) | Aug 18 at 7:20 PM MDT |
| Swiss Roll | Wildfire | 0.25 acres | Not reported | Pagosa Springs (14.5 mi) | Aug 21 at 2:06 PM MDT |
| Arroyo | Wildfire | 0.10 acres | Not reported | Arboles / southwest county (8.7 mi) | Aug 23 at 4:12 PM MDT |

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
- Pending WATCH/LIKELY dates in current forecast: Wed, Aug 26; Thu, Aug 27; Fri, Aug 28; Sat, Aug 29
- Calibration source: manual PSPS event log plus forecast history from prior monitor runs.

### Red Flag / Fire Weather Calibration

- Summary: 3/3 official Red Flag / Fire Weather episodes had a pre-alert HIGH monitor signal; date-level result was 21/21. Episode-average lead time: 3.5 days.
- Official alert episodes logged: 3 (21 alert dates)
- Episode-level pre-alert HIGH hit rate: 100%
- Date-level pre-alert HIGH hit rate: 100%
- Episode-level average lead time: 3.5 days
- HIGH false-watch past days: 21
- Pending HIGH dates in current forecast: Fri, Aug 28; Sat, Aug 29
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
- Operational outage source links: [304 N 2ND ST](https://outage.lpea.coop)
- Active/update source pages with matches: LPEA homepage (public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation, restoration); LPEA X (power outage, outage map, high winds, restore power); LPEA LinkedIn (wildfire, public safety power shutoff, psps, power shutoff, shutoff, deenergize)
- Distinct active/update signals: LPEA X (power outage, outage map, high winds, restore power); LPEA X (power outage, outage map, high winds, restore power); LPEA LinkedIn (wildfire, public safety power shutoff, psps, power shutoff, shutoff, deenergize); LinkedIn PSPS explainer post (wildfire, public safety power shutoff, psps, power shutoff, shutoff, deenergize)
- Example signal: ...ibrary! 1 2 536 LPEA @LaPlataElectric May 7, 2024 LPEA members are experiencing power outages in the Bayfield and Pagosa Springs areas. Approximately 200 meters are out and it is suspected that the high winds are...
- Reference/context hits: [LPEA outage center](https://lpea.coop/outage-center); [LPEA wildfire / public safety power shutoffs](https://lpea.coop/psps); [LPEA red flag outage impact page](https://lpea.coop/outages/red-flag-warnings-and-impact-outages-prioritizing-safety-our-members); [LPEA fire mitigation](https://lpea.coop/fire-mitigation); [LPEA latest news](https://lpea.coop/Posts)

**Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## Next 7 Days

| Date | Tier | Main reason | Worst sampled metrics |
| --- | --- | --- | --- |
| Sun, Aug 23 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 34%, wind/gust 17 mph, thunder 35%<br>Arboles / southwest county: RH 25%, wind/gust 20 mph, thunder 35%<br>Chimney Rock / west county: RH 23%, wind/gust 18 mph, thunder 40% |
| Mon, Aug 24 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 18%, wind/gust 21 mph, thunder 15%<br>Chimney Rock / west county: RH 16%, wind/gust 20 mph, thunder 24% |
| Tue, Aug 25 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 16%, wind/gust 21 mph, thunder 12%<br>Chimney Rock / west county: RH 15%, wind/gust 20 mph, thunder 19%<br>Ignacio / southeast La Plata County: RH 18%, wind/gust 23 mph, thunder 13% |
| Wed, Aug 26 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 16%, wind/gust 22 mph, thunder 15%<br>Chimney Rock / west county: RH 15%, wind/gust 21 mph, thunder 22%<br>Ignacio / southeast La Plata County: RH 17%, wind/gust 22 mph, thunder 15% |
| Thu, Aug 27 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 16%, wind/gust 22 mph, thunder 13%<br>Chimney Rock / west county: RH 15%, wind/gust 21 mph, thunder 20%<br>Ignacio / southeast La Plata County: RH 17%, wind/gust 24 mph, thunder 13% |
| Fri, Aug 28 | HIGH | Arboles / southwest county: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 18%, wind/gust 21 mph, thunder 5%<br>Arboles / southwest county: RH 12%, wind/gust 26 mph, thunder 1%<br>Chimney Rock / west county: RH 11%, wind/gust 24 mph, thunder 2% |
| Sat, Aug 29 | HIGH | Arboles / southwest county: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 15%, wind/gust 24 mph, thunder 3%<br>Arboles / southwest county: RH 11%, wind/gust 28 mph, thunder 4%<br>Chimney Rock / west county: RH 10%, wind/gust 26 mph, thunder 4% |

## Sample Point Status

- Pagosa Springs: COZ295 (matches), forecast zone COZ023, county zone COC007
- Arboles / southwest county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Chimney Rock / west county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Piedra / north county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Chromo / southeast county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Durango / La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Bayfield / east La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Ignacio / southeast La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
