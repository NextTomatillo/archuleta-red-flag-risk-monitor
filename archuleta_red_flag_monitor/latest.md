# Archuleta County fire-weather monitor

Generated: Jul 31, 2026 at 6:07 PM MDT (Pagosa Springs, CO local time)
Next update: Aug 1, 2026 at 5:20 AM MDT (Pagosa Springs, CO local time)
Date/time basis: Pagosa Springs, CO local time (America/Denver)
> **Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## At A Glance

- Fire-weather tier: **HIGH**
- PSPS likelihood: **LIKELY**
- PSPS likely dates: Mon, Aug 3; Tue, Aug 4
- PSPS watch dates: Fri, Jul 31; Sat, Aug 1; Wed, Aug 5
- Monitor heads-up recommended: **YES** - Send this monitor report because fire-weather screening tier is HIGH; PSPS screening level is LIKELY; a material current wildfire is reported in Archuleta County. This is not an official LPEA or NWS notice.
- HIGH dates: Mon, Aug 3
- CONCERN dates: Fri, Jul 31; Sat, Aug 1; Tue, Aug 4; Wed, Aug 5
- ELEVATED dates: Sun, Aug 2
- Official NWS Red Flag / Fire Weather alerts (COZ295): 0
- LPEA signal: `active_keyword_match` - LPEA active/update sources contained power-interruption keywords; review source before treating as confirmed outage intent.
- LPEA source coverage: 13 sources; 5/5 official social sources reachable
- Current Archuleta County wildfires: 1
- Official evacuation notices: No current evacuation order or warning detected in the checked official county feeds.
- NWS discussion: NWS discussion contains fire-weather concern language.

## Decision Support

- Summary: Highest LPEA PSPS concern is Tue, Aug 4 near Arboles / southwest county (LIKELY 69/100), driven by strong wind/gust signal near 33 mph; very dry RH near 9%; 5 sampled hours are near red-flag thresholds. NIFC reports 1 current wildfire in Archuleta County.
- Confidence: **HIGH** (77/100) - 8/8 sampled weather points available; 7/7 fire-posture sources reachable; official NWS alert zones checked; 13/13 LPEA public sources reachable; LPEA active/update sources checked; authoritative NIFC current-incident feed checked for Archuleta County; official Archuleta County evacuation feeds checked; no confirmed PSPS events logged yet for calibration
- Weather fire-potential peak: Mon, Aug 3: Durango / La Plata County VERY HIGH 80/100
- Red Flag likelihood peak: Mon, Aug 3: Ignacio / southeast La Plata County LIKELY 80/100
- LPEA PSPS peak: Tue, Aug 4: Arboles / southwest county LIKELY 69/100
- Method: rules-based decision support using public weather, fire-posture, and LPEA source signals; scores are screening estimates, not official or statistically calibrated probabilities.

| Date | Weather fire potential | Red Flag likelihood | LPEA PSPS | Main window |
| --- | --- | --- | --- | --- |
| Fri, Jul 31 | Durango / La Plata County: VERY HIGH 73/100 | Arboles / southwest county: WATCH 56/100 | Arboles / southwest county: WATCH 50/100 | 6 PM-7 PM local; 2 near/red-flag threshold hours. |
| Sat, Aug 1 | Durango / La Plata County: VERY HIGH 73/100 | Durango / La Plata County: WATCH 55/100 | Durango / La Plata County: WATCH 48/100 | 3 PM-5 PM local; 3 near/red-flag threshold hours. |
| Sun, Aug 2 | Durango / La Plata County: MODERATE 48/100 | Arboles / southwest county: LOW 25/100 | Arboles / southwest county: ELEVATED 32/100 | Peak ingredients near 4 PM local; RH 12%, wind 17 mph. |
| Mon, Aug 3 | Durango / La Plata County: VERY HIGH 80/100 | Ignacio / southeast La Plata County: LIKELY 80/100 | Ignacio / southeast La Plata County: LIKELY 67/100 | 3 PM-7 PM local; 5 near/red-flag threshold hours. |
| Tue, Aug 4 | Durango / La Plata County: VERY HIGH 79/100 | Arboles / southwest county: LIKELY 75/100 | Arboles / southwest county: LIKELY 69/100 | 3 PM-7 PM local; 5 near/red-flag threshold hours. |
| Wed, Aug 5 | Bayfield / east La Plata County: HIGH 66/100 | Arboles / southwest county: WATCH 56/100 | Arboles / southwest county: WATCH 50/100 | 4 PM-5 PM local; 2 near/red-flag threshold hours. |
| Thu, Aug 6 | Durango / La Plata County: MODERATE 40/100 | Durango / La Plata County: LOW 8/100 | Durango / La Plata County: ELEVATED 26/100 | Peak ingredients near 4 PM local; RH 22%, wind 21 mph. |

## Analyst Interpretation

- Headline: HIGH fire-weather screening continues, with the strongest PSPS screening on Aug 3-4 and no official COZ295 alert or active LPEA outage.
- Summary: The monitor places Mon, Aug 3 at HIGH fire-weather screening and Tue, Aug 4 at LIKELY PSPS screening near Arboles, driven by very dry RH and strong wind. Official checks show no COZ295 Red Flag or Fire Weather alert and no active LPEA outage; one current wildfire is reported with no evacuation notice detected. A heads-up remains recommended.
- Uncertainty: These are screening estimates, not official forecasts or calibrated outage probabilities; LPEA operational decisions and thresholds are not visible, and no confirmed PSPS events are logged.
- Evidence used: overall_status, weather_peaks, official_alerts, forecast_change, lpea_context, fire_posture, active_incidents, calibration
- This interpretation cannot change the deterministic tiers, scores, official alerts, or notification decision.

Changing drivers:
- Forecast momentum is steady, with low volatility (6/100) and no major day-level movement.
- The first WATCH-or-higher PSPS date remains Fri, Jul 31.
- Tue, Aug 4 remains the PSPS screening peak near Arboles at LIKELY 69/100, driven by RH near 9% and wind/gust near 33 mph.
- One current wildfire remains reported; no current evacuation notice was detected.

What to watch next:
- Recheck Mon, Aug 3 for HIGH fire-weather ingredients near Ignacio and Durango.
- Recheck Tue, Aug 4 for dry, windy conditions near Arboles.
- Confirm any change in official COZ295 alerts or LPEA outage status.
- Follow official incident and evacuation updates for the Rio Blanco wildfire.

## Trend Intelligence

- Summary: Momentum is steady versus the prior run (Jul 31 at 5:37 PM MDT); forecast volatility is low and first WATCH-or-higher date is Fri, Jul 31.
- Momentum: **Steady**
- Forecast volatility: **LOW** (6/100)
- First WATCH-or-higher PSPS date: Fri, Jul 31
- Watch-date movement: First WATCH-or-higher PSPS date remains Fri, Jul 31.
- Method: compares current forecast evidence against prior local forecast history.

Notable changes:
- First WATCH-or-higher PSPS date remains Fri, Jul 31.
- No major day-level movement versus the prior run.

## Public Analysis Export

- Summary: Highest LPEA PSPS concern is Tue, Aug 4 near Arboles / southwest county (LIKELY 69/100), driven by strong wind/gust signal near 33 mph; very dry RH near 9%; 5 sampled hours are near red-flag thresholds. NIFC reports 1 current wildfire in Archuleta County.
- Trend: Momentum is steady versus the prior run (Jul 31 at 5:37 PM MDT); forecast volatility is low and first WATCH-or-higher date is Fri, Jul 31.
- Confidence: **HIGH** (77/100)
- First WATCH-or-higher PSPS date: Fri, Jul 31
- PSPS peak: Tue, Aug 4 near Arboles / southwest county at LIKELY 69/100
- Red Flag peak: Mon, Aug 3 near Ignacio / southeast La Plata County at LIKELY 80/100
- Weather fire-potential peak: Mon, Aug 3 near Durango / La Plata County at VERY HIGH 80/100
- LPEA operational outage context: No active outages are listed by the official LPEA outage viewer.
- Public JSON: `archuleta_red_flag_monitor/public_analysis_export.json`

What changed:
- First WATCH-or-higher PSPS date remains Fri, Jul 31.
- No major day-level movement versus the prior run.

What to watch next:
- Check whether the largest day-level changes line up with wind/RH movement or public-source context.
- Check whether the LPEA active match is still a broad red-flag banner rather than direct PSPS/outage intent.
- Watch whether the highest-risk locations remain consistent across runs or the driver area is moving.
- If a PSPS occurs, log the confirmed date, location, and source so future hit-rate scoring can improve.

## PSPS Likelihood

- **PSPS means Public Safety Power Shutoff:** a planned, safety-related power shutoff LPEA may use during dangerous fire-weather conditions to reduce wildfire ignition risk. See [LPEA PSPS guidance](https://lpea.coop/psps) and the [LPEA outage center](https://lpea.coop/outage-center); if power is out, also check the [LPEA outage map](https://outage.lpea.coop).
- Overall: **LIKELY** - PSPS likelihood is high on weather-driven red-flag days; prepare for possible LPEA safety-related interruption behavior.
- Likely PSPS watch dates: Mon, Aug 3; Tue, Aug 4
- PSPS watch dates: Fri, Jul 31; Sat, Aug 1; Wed, Aug 5
- LPEA signal basis: LPEA active/update source contains red-flag, wildfire, or power-interruption language.
- Note: This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

| Date | PSPS likelihood | Driver locations | Weather basis |
| --- | --- | --- | --- |
| Fri, Jul 31 | WATCH | Arboles / southwest county (WATCH 50/100); Durango / La Plata County (WATCH 48/100) | Top weather score 48/100 at Arboles / southwest county. Weather score 48/100: RH 12%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 2. |
| Sat, Aug 1 | WATCH | Durango / La Plata County (WATCH 48/100) | Top weather score 44/100 at Durango / La Plata County. Weather score 44/100: RH 14%, wind/gust 22 mph, red-flag hours 0, near-threshold hours 3. |
| Sun, Aug 2 | ELEVATED | Arboles / southwest county (ELEVATED 32/100); Chimney Rock / west county (ELEVATED 32/100); Durango / La Plata County (ELEVATED 30/100) | Top weather score 30/100 at Arboles / southwest county. Weather score 30/100: RH 12%, wind/gust 17 mph, red-flag hours 0, near-threshold hours 0. |
| Mon, Aug 3 | LIKELY | Ignacio / southeast La Plata County (LIKELY 67/100); Durango / La Plata County (WATCH 56/100); Arboles / southwest county (WATCH 54/100); Bayfield / east La Plata County (WATCH 54/100) | Top weather score 67/100 at Ignacio / southeast La Plata County. Weather score 67/100: RH 11%, wind/gust 26 mph, red-flag hours 3, near-threshold hours 5. |
| Tue, Aug 4 | LIKELY | Arboles / southwest county (LIKELY 69/100); Bayfield / east La Plata County (WATCH 63/100); Ignacio / southeast La Plata County (WATCH 61/100); Durango / La Plata County (WATCH 56/100) | Top weather score 67/100 at Arboles / southwest county. Weather score 67/100: RH 9%, wind/gust 33 mph, red-flag hours 1, near-threshold hours 5. |
| Wed, Aug 5 | WATCH | Arboles / southwest county (WATCH 50/100) | Top weather score 48/100 at Arboles / southwest county. Weather score 48/100: RH 12%, wind/gust 22 mph, red-flag hours 0, near-threshold hours 2. |
| Thu, Aug 6 | ELEVATED | Durango / La Plata County (ELEVATED 26/100); Bayfield / east La Plata County (ELEVATED 24/100); Ignacio / southeast La Plata County (ELEVATED 22/100) | Top weather score 22/100 at Durango / La Plata County. Weather score 22/100: RH 21%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 0. |

## Area-Specific Outlook

| Area | Today | Peak this run | Highest-risk window |
| --- | --- | --- | --- |
| Arboles | WATCH 50/100 | Tue, Aug 4: LIKELY 69/100 | 3 PM-7 PM local; 5 near/red-flag threshold hours. |
| Ignacio | ELEVATED 44/100 | Mon, Aug 3: LIKELY 67/100 | 3 PM-7 PM local; 5 near/red-flag threshold hours. |
| Bayfield | ELEVATED 36/100 | Tue, Aug 4: WATCH 63/100 | 3 PM-7 PM local; 5 near/red-flag threshold hours. |
| Durango | WATCH 48/100 | Mon, Aug 3: WATCH 56/100 | 2 PM-7 PM local; 6 near/red-flag threshold hours. |
| Chromo | ELEVATED 30/100 | Tue, Aug 4: WATCH 55/100 | Peak ingredients near 9 PM local; RH 40%, wind 33 mph. |
| Chimney Rock | ELEVATED 32/100 | Mon, Aug 3: WATCH 50/100 | 4 PM-6 PM local; 3 near/red-flag threshold hours. |
| Pagosa Springs | ELEVATED 32/100 | Tue, Aug 4: WATCH 47/100 | Peak ingredients near 9 PM local; RH 34%, wind 26 mph. |
| Piedra | ELEVATED 30/100 | Fri, Jul 31: ELEVATED 30/100 | Peak ingredients near 9 PM local; RH 31%, wind 21 mph. |

## Current Fires + Evacuations

- Incident summary: 1 current wildfire reported in Archuleta County; no current evacuation notice detected in checked county feeds.
- Evacuation status: **NONE DETECTED** - No current evacuation order or warning detected in the checked official county feeds.
- Safety note: Current incidents and evacuation notices are operational context. They do not raise PSPS scores by themselves; follow official evacuation instructions immediately.

### Current NIFC Incidents

| Incident | Type | Size | Containment | Nearest monitored area | Updated |
| --- | --- | --- | --- | --- | --- |
| Rio Blanco | Wildfire | 783.30 acres | 0% | Chromo / southeast county (9.9 mi) | Jul 31 at 5:38 PM MDT |

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
- WATCH/LIKELY false-watch past days: 44
- Pending WATCH/LIKELY dates in current forecast: Fri, Jul 31; Sat, Aug 1; Mon, Aug 3; Tue, Aug 4; Wed, Aug 5
- Calibration source: manual PSPS event log plus forecast history from prior monitor runs.

### Red Flag / Fire Weather Calibration

- Summary: 3/3 official Red Flag / Fire Weather episodes had a pre-alert HIGH monitor signal; date-level result was 21/21. Episode-average lead time: 3.5 days.
- Official alert episodes logged: 3 (21 alert dates)
- Episode-level pre-alert HIGH hit rate: 100%
- Date-level pre-alert HIGH hit rate: 100%
- Episode-level average lead time: 3.5 days
- HIGH false-watch past days: 16
- Pending HIGH dates in current forecast: Mon, Aug 3
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
| Fri, Jul 31 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 12%, wind/gust 21 mph, thunder 1%<br>Chimney Rock / west county: RH 11%, wind/gust 20 mph, thunder 2%<br>Durango / La Plata County: RH 13%, wind/gust 23 mph, thunder 0% |
| Sat, Aug 1 | CONCERN | Durango / La Plata County: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 15%, wind/gust 22 mph, thunder 10%<br>Chimney Rock / west county: RH 14%, wind/gust 17 mph, thunder 14%<br>Durango / La Plata County: RH 14%, wind/gust 22 mph, thunder 13% |
| Sun, Aug 2 | ELEVATED | Arboles / southwest county: Elevated ingredient present: very low RH forecast near 12%. | Arboles / southwest county: RH 12%, wind/gust 17 mph, thunder 2%<br>Chimney Rock / west county: RH 12%, wind/gust 17 mph, thunder 3%<br>Durango / La Plata County: RH 14%, wind/gust 20 mph, thunder 8% |
| Mon, Aug 3 | HIGH | Ignacio / southeast La Plata County: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 14%, wind/gust 18 mph, thunder 2%<br>Arboles / southwest county: RH 9%, wind/gust 23 mph, thunder 0%<br>Chimney Rock / west county: RH 9%, wind/gust 22 mph, thunder 1% |
| Tue, Aug 4 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Pagosa Springs: RH 14%, wind/gust 26 mph, thunder 12%<br>Arboles / southwest county: RH 9%, wind/gust 33 mph, thunder 3%<br>Chimney Rock / west county: RH 9%, wind/gust 24 mph, thunder 5% |
| Wed, Aug 5 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 12%, wind/gust 22 mph, thunder 24%<br>Chimney Rock / west county: RH 12%, wind/gust 20 mph, thunder 25%<br>Bayfield / east La Plata County: RH 16%, wind/gust 22 mph, thunder 20% |
| Thu, Aug 6 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 21%, wind/gust 16 mph, thunder 36%<br>Arboles / southwest county: RH 17%, wind/gust 20 mph, thunder 24%<br>Chimney Rock / west county: RH 16%, wind/gust 16 mph, thunder 34% |

## Sample Point Status

- Pagosa Springs: COZ295 (matches), forecast zone COZ023, county zone COC007
- Arboles / southwest county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Chimney Rock / west county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Piedra / north county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Chromo / southeast county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Durango / La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Bayfield / east La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Ignacio / southeast La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
