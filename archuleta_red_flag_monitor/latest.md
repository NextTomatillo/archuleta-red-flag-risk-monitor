# Archuleta County fire-weather monitor

Generated: Aug 3, 2026 at 5:32 AM MDT (Pagosa Springs, CO local time)
Next update: Aug 3, 2026 at 5:20 PM MDT (Pagosa Springs, CO local time)
Date/time basis: Pagosa Springs, CO local time (America/Denver)
> **Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## At A Glance

- Fire-weather tier: **HIGH**
- PSPS likelihood: **LIKELY**
- PSPS likely dates: Mon, Aug 3; Tue, Aug 4; Wed, Aug 5; Thu, Aug 6
- PSPS watch dates: Fri, Aug 7; Sat, Aug 8; Sun, Aug 9
- Monitor heads-up recommended: **YES** - Send this monitor report because fire-weather screening tier is HIGH; PSPS screening level is LIKELY; a material current wildfire is reported in Archuleta County. This is not an official LPEA or NWS notice.
- HIGH dates: Mon, Aug 3; Tue, Aug 4; Thu, Aug 6
- CONCERN dates: Wed, Aug 5; Fri, Aug 7; Sat, Aug 8; Sun, Aug 9
- ELEVATED dates: None
- Official NWS Red Flag / Fire Weather alerts (COZ295): 0
- LPEA signal: `operational_outage_active` - Official LPEA outage data indicates an operational outage; use as grid context, not PSPS/fire evidence unless LPEA identifies that cause.
- LPEA source coverage: 13 sources; 5/5 official social sources reachable
- Current Archuleta County wildfires: 1
- Official evacuation notices: No current evacuation order or warning detected in the checked official county feeds.
- NWS discussion: NWS discussion contains fire-weather concern language.

## Decision Support

- Summary: Highest LPEA PSPS concern is Thu, Aug 6 near Durango / La Plata County (LIKELY 78/100), driven by red-flag wind/gust signal near 30 mph; critically dry RH near 8%; 4 sampled hours meet red-flag screen. NIFC reports 1 current wildfire in Archuleta County.
- Confidence: **MEDIUM** (69/100) - 8/8 sampled weather points available; 7/7 fire-posture sources reachable; official NWS alert zones checked; 13/13 LPEA public sources reachable; LPEA active/update sources checked; active LPEA operational outage context checked separately from PSPS scoring; authoritative NIFC current-incident feed checked for Archuleta County; official Archuleta County evacuation feeds checked; forecast changed substantially versus prior run; no confirmed PSPS events logged yet for calibration
- Weather fire-potential peak: Mon, Aug 3: Durango / La Plata County EXTREME 92/100
- Red Flag likelihood peak: Mon, Aug 3: Ignacio / southeast La Plata County LIKELY 92/100
- LPEA PSPS peak: Thu, Aug 6: Durango / La Plata County LIKELY 78/100
- Method: rules-based decision support using public weather, fire-posture, and LPEA source signals; scores are screening estimates, not official or statistically calibrated probabilities.

| Date | Weather fire potential | Red Flag likelihood | LPEA PSPS | Main window |
| --- | --- | --- | --- | --- |
| Mon, Aug 3 | Durango / La Plata County: EXTREME 92/100 | Ignacio / southeast La Plata County: LIKELY 92/100 | Durango / La Plata County: LIKELY 75/100 | 12 PM-7 PM local; 8 near/red-flag threshold hours. |
| Tue, Aug 4 | Durango / La Plata County: EXTREME 87/100 | Bayfield / east La Plata County: LIKELY 84/100 | Bayfield / east La Plata County: LIKELY 73/100 | 2 PM-7 PM local; 6 near/red-flag threshold hours. |
| Wed, Aug 5 | Durango / La Plata County: EXTREME 86/100 | Durango / La Plata County: LIKELY 78/100 | Durango / La Plata County: LIKELY 65/100 | 2 PM-9 PM local; 8 near/red-flag threshold hours. |
| Thu, Aug 6 | Durango / La Plata County: EXTREME 92/100 | Durango / La Plata County: LIKELY 88/100 | Durango / La Plata County: LIKELY 78/100 | 2 PM-10 PM local; 9 near/red-flag threshold hours. |
| Fri, Aug 7 | Durango / La Plata County: VERY HIGH 75/100 | Ignacio / southeast La Plata County: WATCH 62/100 | Ignacio / southeast La Plata County: WATCH 57/100 | 4 PM-5 PM local; 2 near/red-flag threshold hours. |
| Sat, Aug 8 | Bayfield / east La Plata County: HIGH 65/100 | Bayfield / east La Plata County: POSSIBLE 52/100 | Bayfield / east La Plata County: WATCH 46/100 | 4 PM-5 PM local; 2 near/red-flag threshold hours. |
| Sun, Aug 9 | Durango / La Plata County: EXTREME 85/100 | Durango / La Plata County: WATCH 62/100 | Durango / La Plata County: WATCH 55/100 | 4 PM-5 PM local; 2 near/red-flag threshold hours. |

## Analyst Interpretation

- Headline: HIGH fire-weather screening continues, with LIKELY PSPS screening through Thu, Aug 6 and no active official COZ295 alert.
- Summary: Rules-based screening is HIGH, with the strongest PSPS estimate on Thu, Aug 6 near Durango at LIKELY 78/100, driven by wind near 30 mph, RH near 8%, and four sampled red-flag hours. No official COZ295 fire-weather alert is active. One current wildfire and one localized unplanned LPEA outage are operational context; neither is treated as proof of a PSPS or an official warning.
- Uncertainty: These are uncalibrated screening estimates, not official probabilities; no confirmed LPEA PSPS events are logged, and utility operational data may not be publicly visible.
- Evidence used: overall_status, weather_peaks, official_alerts, forecast_change, lpea_context, fire_posture, active_incidents, calibration
- This interpretation cannot change the deterministic tiers, scores, official alerts, or notification decision.

Changing drivers:
- Thu, Aug 6 worsened from WATCH to LIKELY as wind increased 7 mph, RH fell 3 points, and four more hours met the red-flag screen.
- Wed, Aug 5 worsened from WATCH to LIKELY with a 9-point score increase.
- The first WATCH-or-higher screening date moved later from Sun, Aug 2 to Mon, Aug 3.
- One unplanned LPEA outage affects 38 customers near Pagosa Springs, with no identified fire-weather or PSPS cause.

What to watch next:
- Check official NWS alerts as the Mon-Thu HIGH and LIKELY windows evolve.
- Watch whether Thu, Aug 6 wind and RH forecasts remain near the current peak.
- Confirm the localized outage cause and restoration status directly with LPEA.
- Follow official incident and evacuation sources for Rio Blanco updates.

## Trend Intelligence

- Summary: Momentum is rising versus the prior run (Aug 2 at 5:23 PM MDT); forecast volatility is high and first WATCH-or-higher date is Mon, Aug 3.
- Momentum: **Rising**
- Forecast volatility: **HIGH** (44/100)
- First WATCH-or-higher PSPS date: Mon, Aug 3
- Watch-date movement: First WATCH-or-higher PSPS date moved later from Sun, Aug 2 to Mon, Aug 3.
- Method: compares current forecast evidence against prior local forecast history.

Notable changes:
- First WATCH-or-higher PSPS date moved later from Sun, Aug 2 to Mon, Aug 3.
- Thu, Aug 6: worsening vs prior run; PSPS WATCH -> LIKELY; score +22, wind +7 mph, RH -3%, red-flag hours +4.
- Wed, Aug 5: worsening vs prior run; PSPS WATCH -> LIKELY; score +9, wind +2 mph, RH -1%, red-flag hours +2.

## Public Analysis Export

- Summary: Highest LPEA PSPS concern is Thu, Aug 6 near Durango / La Plata County (LIKELY 78/100), driven by red-flag wind/gust signal near 30 mph; critically dry RH near 8%; 4 sampled hours meet red-flag screen. NIFC reports 1 current wildfire in Archuleta County.
- Trend: Momentum is rising versus the prior run (Aug 2 at 5:23 PM MDT); forecast volatility is high and first WATCH-or-higher date is Mon, Aug 3.
- Confidence: **MEDIUM** (69/100)
- First WATCH-or-higher PSPS date: Mon, Aug 3
- PSPS peak: Thu, Aug 6 near Durango / La Plata County at LIKELY 78/100
- Red Flag peak: Mon, Aug 3 near Ignacio / southeast La Plata County at LIKELY 92/100
- Weather fire-potential peak: Mon, Aug 3 near Durango / La Plata County at EXTREME 92/100
- LPEA operational outage context: 1 active outage; 0 planned and 1 unplanned; 38 customers out. No fire-weather or PSPS cause is identified.
- Public JSON: `archuleta_red_flag_monitor/public_analysis_export.json`

What changed:
- First WATCH-or-higher PSPS date moved later from Sun, Aug 2 to Mon, Aug 3.
- Thu, Aug 6: worsening vs prior run; PSPS WATCH -> LIKELY; score +22, wind +7 mph, RH -3%, red-flag hours +4.
- Wed, Aug 5: worsening vs prior run; PSPS WATCH -> LIKELY; score +9, wind +2 mph, RH -1%, red-flag hours +2.

What to watch next:
- Check whether the largest day-level changes line up with wind/RH movement or public-source context.
- Check whether the LPEA active match is still a broad red-flag banner rather than direct PSPS/outage intent.
- Watch whether the highest-risk locations remain consistent across runs or the driver area is moving.
- If a PSPS occurs, log the confirmed date, location, and source so future hit-rate scoring can improve.

## PSPS Likelihood

- **PSPS means Public Safety Power Shutoff:** a planned, safety-related power shutoff LPEA may use during dangerous fire-weather conditions to reduce wildfire ignition risk. See [LPEA PSPS guidance](https://lpea.coop/psps) and the [LPEA outage center](https://lpea.coop/outage-center); if power is out, also check the [LPEA outage map](https://outage.lpea.coop).
- Overall: **LIKELY** - PSPS likelihood is high on weather-driven red-flag days; prepare for possible LPEA safety-related interruption behavior.
- Likely PSPS watch dates: Mon, Aug 3; Tue, Aug 4; Wed, Aug 5; Thu, Aug 6
- PSPS watch dates: Fri, Aug 7; Sat, Aug 8; Sun, Aug 9
- LPEA signal basis: LPEA active/update source contains red-flag, wildfire, or power-interruption language.
- Note: This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

| Date | PSPS likelihood | Driver locations | Weather basis |
| --- | --- | --- | --- |
| Mon, Aug 3 | LIKELY | Durango / La Plata County (LIKELY 75/100); Arboles / southwest county (LIKELY 73/100); Bayfield / east La Plata County (LIKELY 73/100); Ignacio / southeast La Plata County (LIKELY 71/100) | Top weather score 71/100 at Arboles / southwest county. Weather score 71/100: RH 9%, wind/gust 28 mph, red-flag hours 4, near-threshold hours 7. |
| Tue, Aug 4 | LIKELY | Bayfield / east La Plata County (LIKELY 73/100); Ignacio / southeast La Plata County (LIKELY 71/100); Durango / La Plata County (LIKELY 71/100); Arboles / southwest county (WATCH 63/100) | Top weather score 71/100 at Bayfield / east La Plata County. Weather score 71/100: RH 11%, wind/gust 26 mph, red-flag hours 4, near-threshold hours 6. |
| Wed, Aug 5 | LIKELY | Durango / La Plata County (LIKELY 65/100); Ignacio / southeast La Plata County (WATCH 61/100); Arboles / southwest county (WATCH 54/100); Bayfield / east La Plata County (WATCH 54/100) | Top weather score 61/100 at Durango / La Plata County. Weather score 61/100: RH 9%, wind/gust 25 mph, red-flag hours 2, near-threshold hours 8. |
| Thu, Aug 6 | LIKELY | Durango / La Plata County (LIKELY 78/100); Piedra / north county (WATCH 59/100); Arboles / southwest county (WATCH 57/100); Ignacio / southeast La Plata County (WATCH 55/100) | Top weather score 74/100 at Durango / La Plata County. Weather score 74/100: RH 8%, wind/gust 30 mph, red-flag hours 4, near-threshold hours 9. |
| Fri, Aug 7 | WATCH | Ignacio / southeast La Plata County (WATCH 57/100); Durango / La Plata County (WATCH 52/100); Bayfield / east La Plata County (WATCH 50/100) | Top weather score 57/100 at Ignacio / southeast La Plata County. Weather score 57/100: RH 9%, wind/gust 25 mph, red-flag hours 0, near-threshold hours 2. |
| Sat, Aug 8 | WATCH | Bayfield / east La Plata County (WATCH 46/100) | Top weather score 44/100 at Bayfield / east La Plata County. Weather score 44/100: RH 13%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 2. |
| Sun, Aug 9 | WATCH | Durango / La Plata County (WATCH 55/100); Arboles / southwest county (WATCH 50/100); Bayfield / east La Plata County (WATCH 50/100); Ignacio / southeast La Plata County (WATCH 48/100) | Top weather score 51/100 at Durango / La Plata County. Weather score 51/100: RH 14%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 2. |

## Area-Specific Outlook

| Area | Today | Peak this run | Highest-risk window |
| --- | --- | --- | --- |
| Durango | LIKELY 75/100 | Thu, Aug 6: LIKELY 78/100 | 2 PM-10 PM local; 9 near/red-flag threshold hours. |
| Arboles | LIKELY 73/100 | Mon, Aug 3: LIKELY 73/100 | 1 PM-7 PM local; 7 near/red-flag threshold hours. |
| Bayfield | LIKELY 73/100 | Mon, Aug 3: LIKELY 73/100 | 1 PM-7 PM local; 7 near/red-flag threshold hours. |
| Ignacio | LIKELY 71/100 | Mon, Aug 3: LIKELY 71/100 | 1 PM-8 PM local; 8 near/red-flag threshold hours. |
| Piedra | WATCH 50/100 | Thu, Aug 6: WATCH 59/100 | 7 PM-8 PM local; 2 near/red-flag threshold hours. |
| Chimney Rock | WATCH 54/100 | Tue, Aug 4: WATCH 57/100 | 3 PM-6 PM local; 4 near/red-flag threshold hours. |
| Chromo | WATCH 54/100 | Mon, Aug 3: WATCH 54/100 | 2 PM-6 PM local; 5 near/red-flag threshold hours. |
| Pagosa Springs | WATCH 52/100 | Mon, Aug 3: WATCH 52/100 | 2 PM-6 PM local; 5 near/red-flag threshold hours. |

## Current Fires + Evacuations

- Incident summary: 1 current wildfire reported in Archuleta County; no current evacuation notice detected in checked county feeds.
- Evacuation status: **NONE DETECTED** - No current evacuation order or warning detected in the checked official county feeds.
- Safety note: Current incidents and evacuation notices are operational context. They do not raise PSPS scores by themselves; follow official evacuation instructions immediately.

### Current NIFC Incidents

| Incident | Type | Size | Containment | Nearest monitored area | Updated |
| --- | --- | --- | --- | --- | --- |
| Rio Blanco | Wildfire | 1,082.97 acres | 11% | Chromo / southeast county (9.9 mi) | Aug 2 at 6:11 PM MDT |

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
| San Juan National Forest | STAGE 1 | HIGH | [San Juan National Forest fire](https://www.fs.usda.gov/r02/sanjuan/fire) |
| BLM Tres Rios | UNKNOWN | UNKNOWN | [BLM Tres Rios Field Office](https://www.blm.gov/office/tres-rios-field-office) |
| La Plata County / Durango Fire | NONE | UNKNOWN | [Durango Fire & Rescue fire conditions](https://www.durangofire.org/fire-conditions) |
| Durango | STAGE 2 | UNKNOWN | [City of Durango](https://www.durangoco.gov/) |
| Southern Ute / Ignacio | UNKNOWN | UNKNOWN | [Southern Ute Indian Tribe](https://www.southernute-nsn.gov/) |

## Forecast Calibration

### PSPS Calibration

- Summary: No confirmed LPEA PSPS events logged yet; calibration will start once events are added.
- Confirmed PSPS events logged: 0
- Candidate/unconfirmed events logged: 0
- WATCH/LIKELY false-watch past days: 47
- Pending WATCH/LIKELY dates in current forecast: Mon, Aug 3; Tue, Aug 4; Wed, Aug 5; Thu, Aug 6; Fri, Aug 7; Sat, Aug 8; Sun, Aug 9
- Calibration source: manual PSPS event log plus forecast history from prior monitor runs.

### Red Flag / Fire Weather Calibration

- Summary: 3/3 official Red Flag / Fire Weather episodes had a pre-alert HIGH monitor signal; date-level result was 21/21. Episode-average lead time: 3.5 days.
- Official alert episodes logged: 3 (21 alert dates)
- Episode-level pre-alert HIGH hit rate: 100%
- Date-level pre-alert HIGH hit rate: 100%
- Episode-level average lead time: 3.5 days
- HIGH false-watch past days: 16
- Pending HIGH dates in current forecast: Mon, Aug 3; Tue, Aug 4; Thu, Aug 6
- Calibration source: official NWS Red Flag / Fire Weather alert dates plus forecast history from prior monitor runs.

## Official Weather Alerts

- Monitored NWS zones: COC007, COC067, COZ019, COZ022, COZ023, COZ295
- No active official NWS Red Flag / Fire Weather or related weather alerts found for monitored zones.

## LPEA Power Signal

- Status: `operational_outage_active` - Official LPEA outage data indicates an operational outage; use as grid context, not PSPS/fire evidence unless LPEA identifies that cause.
- Meaning: Active source match means a monitored LPEA active/update source currently contains fire, outage, PSPS, or power-interruption keywords. Operational outages are shown separately and are not treated as PSPS/fire evidence unless the source text says so.
- Operational outage context: 1 active outage; 0 planned and 1 unplanned; 38 customers out. No fire-weather or PSPS cause is identified.
- Source coverage: 13 sources; 5/5 official social sources reachable
- Evidence quality: 0 operational, 4 active/update, 0 archive/context, 6 reference source matches.
- Operational outage source links: [52 MAPLE GLEN PL](https://outage.lpea.coop)
- Active/update source pages with matches: LPEA homepage (public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation, restoration); LPEA X (power outage, outage map, high winds, restore power); LPEA LinkedIn (wildfire, fire mitigation)
- Distinct active/update signals: LPEA X (power outage, outage map, high winds, restore power); LPEA X (power outage, outage map, high winds, restore power); LPEA LinkedIn (wildfire, fire mitigation); LPEA LinkedIn (wildfire, fire mitigation)
- Example signal: ...ibrary! 1 2 519 LPEA @LaPlataElectric May 7, 2024 LPEA members are experiencing power outages in the Bayfield and Pagosa Springs areas. Approximately 200 meters are out and it is suspected that the high winds are...
- Reference/context hits: [LPEA outage center](https://lpea.coop/outage-center); [LPEA wildfire / public safety power shutoffs](https://lpea.coop/psps); [LPEA red flag outage impact page](https://lpea.coop/outages/red-flag-warnings-and-impact-outages-prioritizing-safety-our-members); [LPEA fire mitigation](https://lpea.coop/fire-mitigation); [LPEA latest news](https://lpea.coop/Posts)

**Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## Next 7 Days

| Date | Tier | Main reason | Worst sampled metrics |
| --- | --- | --- | --- |
| Mon, Aug 3 | HIGH | Arboles / southwest county: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 13%, wind/gust 24 mph, thunder 2%<br>Arboles / southwest county: RH 9%, wind/gust 28 mph, thunder 3%<br>Chimney Rock / west county: RH 9%, wind/gust 24 mph, thunder 2% |
| Tue, Aug 4 | HIGH | Durango / La Plata County: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 13%, wind/gust 23 mph, thunder 5%<br>Arboles / southwest county: RH 9%, wind/gust 26 mph, thunder 1%<br>Chimney Rock / west county: RH 8%, wind/gust 23 mph, thunder 2% |
| Wed, Aug 5 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Pagosa Springs: RH 14%, wind/gust 18 mph, thunder 5%<br>Arboles / southwest county: RH 9%, wind/gust 23 mph, thunder 1%<br>Chimney Rock / west county: RH 8%, wind/gust 21 mph, thunder 4% |
| Thu, Aug 6 | HIGH | Durango / La Plata County: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 12%, wind/gust 23 mph, thunder 7%<br>Arboles / southwest county: RH 8%, wind/gust 22 mph, thunder 2%<br>Chimney Rock / west county: RH 7%, wind/gust 21 mph, thunder 4% |
| Fri, Aug 7 | CONCERN | Durango / La Plata County: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Pagosa Springs: RH 12%, wind/gust 17 mph, thunder 8%<br>Arboles / southwest county: RH 9%, wind/gust 18 mph, thunder 5%<br>Chimney Rock / west county: RH 8%, wind/gust 17 mph, thunder 7% |
| Sat, Aug 8 | CONCERN | Bayfield / east La Plata County: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Pagosa Springs: RH 13%, wind/gust 16 mph, thunder 12%<br>Arboles / southwest county: RH 10%, wind/gust 20 mph, thunder 9%<br>Chimney Rock / west county: RH 9%, wind/gust 17 mph, thunder 12% |
| Sun, Aug 9 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Pagosa Springs: RH 14%, wind/gust 17 mph, thunder 15%<br>Arboles / southwest county: RH 11%, wind/gust 22 mph, thunder 13%<br>Chimney Rock / west county: RH 10%, wind/gust 20 mph, thunder 15% |

## Sample Point Status

- Pagosa Springs: COZ295 (matches), forecast zone COZ023, county zone COC007
- Arboles / southwest county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Chimney Rock / west county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Piedra / north county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Chromo / southeast county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Durango / La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Bayfield / east La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Ignacio / southeast La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
