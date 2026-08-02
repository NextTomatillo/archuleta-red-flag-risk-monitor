# Archuleta County fire-weather monitor

Generated: Aug 2, 2026 at 5:24 AM MDT (Pagosa Springs, CO local time)
Next update: Aug 2, 2026 at 5:20 PM MDT (Pagosa Springs, CO local time)
Date/time basis: Pagosa Springs, CO local time (America/Denver)
> **Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## At A Glance

- Fire-weather tier: **HIGH**
- PSPS likelihood: **LIKELY**
- PSPS likely dates: Mon, Aug 3; Tue, Aug 4
- PSPS watch dates: Sun, Aug 2; Wed, Aug 5; Thu, Aug 6; Fri, Aug 7; Sat, Aug 8
- Monitor heads-up recommended: **YES** - Send this monitor report because fire-weather screening tier is HIGH; PSPS screening level is LIKELY; a material current wildfire is reported in Archuleta County. This is not an official LPEA or NWS notice.
- HIGH dates: Mon, Aug 3; Tue, Aug 4
- CONCERN dates: Sun, Aug 2; Wed, Aug 5; Thu, Aug 6; Fri, Aug 7; Sat, Aug 8
- ELEVATED dates: None
- Official NWS Red Flag / Fire Weather alerts (COZ295): 0
- LPEA signal: `operational_outage_active` - Official LPEA outage data indicates an operational outage; use as grid context, not PSPS/fire evidence unless LPEA identifies that cause.
- LPEA source coverage: 13 sources; 4/5 official social sources reachable
- Current Archuleta County wildfires: 1
- Official evacuation notices: No current evacuation order or warning detected in the checked official county feeds.
- NWS discussion: NWS discussion contains fire-weather concern language.

## Decision Support

- Summary: Highest LPEA PSPS concern is Mon, Aug 3 near Durango / La Plata County (LIKELY 75/100), driven by red-flag wind/gust signal near 26 mph; very dry RH near 11%; 4 sampled hours meet red-flag screen. NIFC reports 1 current wildfire in Archuleta County.
- Confidence: **MEDIUM** (74/100) - 8/8 sampled weather points available; 7/7 fire-posture sources reachable; official NWS alert zones checked; 12/13 LPEA public sources reachable; LPEA active/update sources checked; active LPEA operational outage context checked separately from PSPS scoring; authoritative NIFC current-incident feed checked for Archuleta County; official Archuleta County evacuation feeds checked; forecast changed moderately versus prior run; no confirmed PSPS events logged yet for calibration
- Weather fire-potential peak: Mon, Aug 3: Durango / La Plata County EXTREME 90/100
- Red Flag likelihood peak: Mon, Aug 3: Bayfield / east La Plata County LIKELY 88/100
- LPEA PSPS peak: Mon, Aug 3: Durango / La Plata County LIKELY 75/100
- Method: rules-based decision support using public weather, fire-posture, and LPEA source signals; scores are screening estimates, not official or statistically calibrated probabilities.

| Date | Weather fire potential | Red Flag likelihood | LPEA PSPS | Main window |
| --- | --- | --- | --- | --- |
| Sun, Aug 2 | Durango / La Plata County: VERY HIGH 71/100 | Durango / La Plata County: POSSIBLE 52/100 | Durango / La Plata County: WATCH 48/100 | 4 PM-5 PM local; 2 near/red-flag threshold hours. |
| Mon, Aug 3 | Durango / La Plata County: EXTREME 90/100 | Bayfield / east La Plata County: LIKELY 88/100 | Durango / La Plata County: LIKELY 75/100 | 1 PM-7 PM local; 7 near/red-flag threshold hours. |
| Tue, Aug 4 | Durango / La Plata County: VERY HIGH 80/100 | Ignacio / southeast La Plata County: LIKELY 80/100 | Ignacio / southeast La Plata County: LIKELY 67/100 | 2 PM-7 PM local; 6 near/red-flag threshold hours. |
| Wed, Aug 5 | Durango / La Plata County: VERY HIGH 75/100 | Ignacio / southeast La Plata County: WATCH 65/100 | Durango / La Plata County: WATCH 52/100 | 3 PM-5 PM local; 3 near/red-flag threshold hours. |
| Thu, Aug 6 | Durango / La Plata County: VERY HIGH 76/100 | Ignacio / southeast La Plata County: WATCH 70/100 | Ignacio / southeast La Plata County: WATCH 56/100 | 3 PM-7 PM local; 5 near/red-flag threshold hours. |
| Fri, Aug 7 | Durango / La Plata County: VERY HIGH 74/100 | Arboles / southwest county: WATCH 64/100 | Arboles / southwest county: WATCH 54/100 | 4 PM-6 PM local; 3 near/red-flag threshold hours. |
| Sat, Aug 8 | Durango / La Plata County: VERY HIGH 76/100 | Ignacio / southeast La Plata County: WATCH 63/100 | Arboles / southwest county: WATCH 54/100 | 4 PM-5 PM local; 2 near/red-flag threshold hours. |

## Analyst Interpretation

- Headline: HIGH fire-weather screening continues, peaking Aug 3-4, while no official NWS fire alert or fire-related LPEA outage is identified.
- Summary: The screening outlook is HIGH with LIKELY PSPS conditions on Aug 3-4, led by dry humidity, strong wind, and multiple sampled red-flag-screen hours. Officially, there are zero active NWS fire-weather alerts, and LPEA reports one planned outage affecting 38 customers with no fire-weather or PSPS cause identified. Rio Blanco remains an active wildfire, while checked county feeds show no current evacuation order or warning.
- Uncertainty: These are rules-based screening estimates, not official or calibrated probabilities; no confirmed LPEA PSPS events are logged, 46 prior WATCH/LIKELY days were false watches, and conditions may change.
- Evidence used: overall_status, weather_peaks, official_alerts, forecast_change, lpea_context, fire_posture, active_incidents, calibration
- This interpretation cannot change the deterministic tiers, scores, official alerts, or notification decision.

Changing drivers:
- Forecast momentum is rising, while the first WATCH-or-higher screening date remains Sun, Aug 2.
- Fri, Aug 7 remains WATCH but its screening score rose 8 points as minimum humidity fell 1 percentage point.
- The Aug 3 peak remains LIKELY, with very dry humidity, gusts near 26 mph, and four sampled red-flag-screen hours.
- Rio Blanco is reported at 1,011 acres and 13% containment, with no current evacuation notice detected in checked county feeds.

What to watch next:
- Check NWS zones for any new official Red Flag Warning or Fire Weather Watch.
- Recheck whether the planned LPEA outage remains active and whether LPEA identifies any fire-weather or PSPS cause.
- Track wind, humidity, and sampled red-flag hours for the Aug 3-4 peak.
- Follow official Rio Blanco containment and evacuation updates.

## Trend Intelligence

- Summary: Momentum is rising versus the prior run (Aug 1 at 6:35 PM MDT); forecast volatility is medium and first WATCH-or-higher date is Sun, Aug 2.
- Momentum: **Rising**
- Forecast volatility: **MEDIUM** (13/100)
- First WATCH-or-higher PSPS date: Sun, Aug 2
- Watch-date movement: First WATCH-or-higher PSPS date remains Sun, Aug 2.
- Method: compares current forecast evidence against prior local forecast history.

Notable changes:
- First WATCH-or-higher PSPS date remains Sun, Aug 2.
- Fri, Aug 7: worsening vs prior run; PSPS WATCH -> WATCH; score +8, wind 0 mph, RH -1%, red-flag hours 0.

## Public Analysis Export

- Summary: Highest LPEA PSPS concern is Mon, Aug 3 near Durango / La Plata County (LIKELY 75/100), driven by red-flag wind/gust signal near 26 mph; very dry RH near 11%; 4 sampled hours meet red-flag screen. NIFC reports 1 current wildfire in Archuleta County.
- Trend: Momentum is rising versus the prior run (Aug 1 at 6:35 PM MDT); forecast volatility is medium and first WATCH-or-higher date is Sun, Aug 2.
- Confidence: **MEDIUM** (74/100)
- First WATCH-or-higher PSPS date: Sun, Aug 2
- PSPS peak: Mon, Aug 3 near Durango / La Plata County at LIKELY 75/100
- Red Flag peak: Mon, Aug 3 near Bayfield / east La Plata County at LIKELY 88/100
- Weather fire-potential peak: Mon, Aug 3 near Durango / La Plata County at EXTREME 90/100
- LPEA operational outage context: 1 active outage; 1 planned and 0 unplanned; 38 customers out. No fire-weather or PSPS cause is identified.
- Public JSON: `archuleta_red_flag_monitor/public_analysis_export.json`

What changed:
- First WATCH-or-higher PSPS date remains Sun, Aug 2.
- Fri, Aug 7: worsening vs prior run; PSPS WATCH -> WATCH; score +8, wind 0 mph, RH -1%, red-flag hours 0.

What to watch next:
- Check whether the largest day-level changes line up with wind/RH movement or public-source context.
- Check whether the LPEA active match is still a broad red-flag banner rather than direct PSPS/outage intent.
- Watch whether the highest-risk locations remain consistent across runs or the driver area is moving.
- If a PSPS occurs, log the confirmed date, location, and source so future hit-rate scoring can improve.

## PSPS Likelihood

- **PSPS means Public Safety Power Shutoff:** a planned, safety-related power shutoff LPEA may use during dangerous fire-weather conditions to reduce wildfire ignition risk. See [LPEA PSPS guidance](https://lpea.coop/psps) and the [LPEA outage center](https://lpea.coop/outage-center); if power is out, also check the [LPEA outage map](https://outage.lpea.coop).
- Overall: **LIKELY** - PSPS likelihood is high on weather-driven red-flag days; prepare for possible LPEA safety-related interruption behavior.
- Likely PSPS watch dates: Mon, Aug 3; Tue, Aug 4
- PSPS watch dates: Sun, Aug 2; Wed, Aug 5; Thu, Aug 6; Fri, Aug 7; Sat, Aug 8
- LPEA signal basis: LPEA active/update source contains red-flag, wildfire, or power-interruption language.
- Note: This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

| Date | PSPS likelihood | Driver locations | Weather basis |
| --- | --- | --- | --- |
| Sun, Aug 2 | WATCH | Durango / La Plata County (WATCH 48/100) | Top weather score 44/100 at Durango / La Plata County. Weather score 44/100: RH 14%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 2. |
| Mon, Aug 3 | LIKELY | Durango / La Plata County (LIKELY 75/100); Arboles / southwest county (LIKELY 73/100); Bayfield / east La Plata County (LIKELY 73/100); Ignacio / southeast La Plata County (LIKELY 71/100) | Top weather score 71/100 at Arboles / southwest county. Weather score 71/100: RH 9%, wind/gust 28 mph, red-flag hours 4, near-threshold hours 7. |
| Tue, Aug 4 | LIKELY | Ignacio / southeast La Plata County (LIKELY 67/100); Arboles / southwest county (WATCH 63/100); Bayfield / east La Plata County (WATCH 63/100); Durango / La Plata County (WATCH 56/100) | Top weather score 67/100 at Ignacio / southeast La Plata County. Weather score 67/100: RH 10%, wind/gust 26 mph, red-flag hours 3, near-threshold hours 6. |
| Wed, Aug 5 | WATCH | Ignacio / southeast La Plata County (WATCH 52/100); Durango / La Plata County (WATCH 52/100); Arboles / southwest county (WATCH 50/100); Bayfield / east La Plata County (WATCH 50/100) | Top weather score 52/100 at Ignacio / southeast La Plata County. Weather score 52/100: RH 11%, wind/gust 22 mph, red-flag hours 0, near-threshold hours 5. |
| Thu, Aug 6 | WATCH | Ignacio / southeast La Plata County (WATCH 56/100); Durango / La Plata County (WATCH 52/100); Arboles / southwest county (WATCH 50/100); Bayfield / east La Plata County (WATCH 50/100) | Top weather score 56/100 at Ignacio / southeast La Plata County. Weather score 56/100: RH 12%, wind/gust 23 mph, red-flag hours 0, near-threshold hours 5. |
| Fri, Aug 7 | WATCH | Arboles / southwest county (WATCH 54/100); Durango / La Plata County (WATCH 52/100); Bayfield / east La Plata County (WATCH 50/100); Ignacio / southeast La Plata County (WATCH 48/100) | Top weather score 52/100 at Arboles / southwest county. Weather score 52/100: RH 12%, wind/gust 22 mph, red-flag hours 0, near-threshold hours 3. |
| Sat, Aug 8 | WATCH | Arboles / southwest county (WATCH 54/100); Ignacio / southeast La Plata County (WATCH 52/100); Durango / La Plata County (WATCH 52/100); Bayfield / east La Plata County (WATCH 50/100) | Top weather score 52/100 at Arboles / southwest county. Weather score 52/100: RH 11%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 2. |

## Area-Specific Outlook

| Area | Today | Peak this run | Highest-risk window |
| --- | --- | --- | --- |
| Durango | WATCH 48/100 | Mon, Aug 3: LIKELY 75/100 | 1 PM-7 PM local; 7 near/red-flag threshold hours. |
| Arboles | ELEVATED 32/100 | Mon, Aug 3: LIKELY 73/100 | 1 PM-7 PM local; 7 near/red-flag threshold hours. |
| Bayfield | ELEVATED 28/100 | Mon, Aug 3: LIKELY 73/100 | 1 PM-7 PM local; 7 near/red-flag threshold hours. |
| Ignacio | ELEVATED 26/100 | Mon, Aug 3: LIKELY 71/100 | 1 PM-7 PM local; 7 near/red-flag threshold hours. |
| Chimney Rock | ELEVATED 32/100 | Mon, Aug 3: WATCH 54/100 | 2 PM-6 PM local; 5 near/red-flag threshold hours. |
| Chromo | LOW 14/100 | Mon, Aug 3: WATCH 50/100 | 3 PM-5 PM local; 3 near/red-flag threshold hours. |
| Pagosa Springs | ELEVATED 24/100 | Mon, Aug 3: WATCH 48/100 | 3 PM-5 PM local; 3 near/red-flag threshold hours. |
| Piedra | ELEVATED 22/100 | Sat, Aug 8: ELEVATED 35/100 | Peak ingredients near 3 PM local; RH 15%, wind 15 mph. |

## Current Fires + Evacuations

- Incident summary: 1 current wildfire reported in Archuleta County; no current evacuation notice detected in checked county feeds.
- Evacuation status: **NONE DETECTED** - No current evacuation order or warning detected in the checked official county feeds.
- Safety note: Current incidents and evacuation notices are operational context. They do not raise PSPS scores by themselves; follow official evacuation instructions immediately.

### Current NIFC Incidents

| Incident | Type | Size | Containment | Nearest monitored area | Updated |
| --- | --- | --- | --- | --- | --- |
| Rio Blanco | Wildfire | 1,011.00 acres | 13% | Chromo / southeast county (9.9 mi) | Aug 1 at 6:06 PM MDT |

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
- WATCH/LIKELY false-watch past days: 46
- Pending WATCH/LIKELY dates in current forecast: Sun, Aug 2; Mon, Aug 3; Tue, Aug 4; Wed, Aug 5; Thu, Aug 6; Fri, Aug 7; Sat, Aug 8
- Calibration source: manual PSPS event log plus forecast history from prior monitor runs.

### Red Flag / Fire Weather Calibration

- Summary: 3/3 official Red Flag / Fire Weather episodes had a pre-alert HIGH monitor signal; date-level result was 21/21. Episode-average lead time: 3.5 days.
- Official alert episodes logged: 3 (21 alert dates)
- Episode-level pre-alert HIGH hit rate: 100%
- Date-level pre-alert HIGH hit rate: 100%
- Episode-level average lead time: 3.5 days
- HIGH false-watch past days: 16
- Pending HIGH dates in current forecast: Mon, Aug 3; Tue, Aug 4
- Calibration source: official NWS Red Flag / Fire Weather alert dates plus forecast history from prior monitor runs.

## Official Weather Alerts

- Monitored NWS zones: COC007, COC067, COZ019, COZ022, COZ023, COZ295
- No active official NWS Red Flag / Fire Weather or related weather alerts found for monitored zones.

## LPEA Power Signal

- Status: `operational_outage_active` - Official LPEA outage data indicates an operational outage; use as grid context, not PSPS/fire evidence unless LPEA identifies that cause.
- Meaning: Active source match means a monitored LPEA active/update source currently contains fire, outage, PSPS, or power-interruption keywords. Operational outages are shown separately and are not treated as PSPS/fire evidence unless the source text says so.
- Operational outage context: 1 active outage; 1 planned and 0 unplanned; 38 customers out. No fire-weather or PSPS cause is identified.
- Source coverage: 13 sources; 4/5 official social sources reachable
- Evidence quality: 0 operational, 4 active/update, 0 archive/context, 6 reference source matches.
- Operational outage source links: [108 MEADOWBROOK PL](https://outage.lpea.coop)
- Active/update source pages with matches: LPEA homepage (public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation, restoration); LPEA X (power outage, outage map, high winds, restore power); LPEA LinkedIn (wildfire, fire mitigation)
- Distinct active/update signals: LPEA X (power outage, outage map, high winds, restore power); LPEA X (power outage, outage map, high winds, restore power); LPEA LinkedIn (wildfire, fire mitigation); LPEA LinkedIn (wildfire, fire mitigation)
- Example signal: ...ibrary! 1 2 519 LPEA @LaPlataElectric May 7, 2024 LPEA members are experiencing power outages in the Bayfield and Pagosa Springs areas. Approximately 200 meters are out and it is suspected that the high winds are...
- Reference/context hits: [LPEA outage center](https://lpea.coop/outage-center); [LPEA wildfire / public safety power shutoffs](https://lpea.coop/psps); [LPEA red flag outage impact page](https://lpea.coop/outages/red-flag-warnings-and-impact-outages-prioritizing-safety-our-members); [LPEA fire mitigation](https://lpea.coop/fire-mitigation); [LPEA latest news](https://lpea.coop/Posts)

**Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## Next 7 Days

| Date | Tier | Main reason | Worst sampled metrics |
| --- | --- | --- | --- |
| Sun, Aug 2 | CONCERN | Durango / La Plata County: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 11%, wind/gust 18 mph, thunder 2%<br>Chimney Rock / west county: RH 12%, wind/gust 17 mph, thunder 4%<br>Durango / La Plata County: RH 14%, wind/gust 21 mph, thunder 3% |
| Mon, Aug 3 | HIGH | Arboles / southwest county: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 14%, wind/gust 22 mph, thunder 1%<br>Arboles / southwest county: RH 9%, wind/gust 28 mph, thunder 1%<br>Chimney Rock / west county: RH 9%, wind/gust 23 mph, thunder 1% |
| Tue, Aug 4 | HIGH | Ignacio / southeast La Plata County: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 13%, wind/gust 21 mph, thunder 3%<br>Arboles / southwest county: RH 9%, wind/gust 25 mph, thunder 0%<br>Chimney Rock / west county: RH 9%, wind/gust 22 mph, thunder 1% |
| Wed, Aug 5 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Pagosa Springs: RH 15%, wind/gust 17 mph, thunder 10%<br>Arboles / southwest county: RH 9%, wind/gust 21 mph, thunder 6%<br>Chimney Rock / west county: RH 9%, wind/gust 21 mph, thunder 8% |
| Thu, Aug 6 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Pagosa Springs: RH 15%, wind/gust 17 mph, thunder 16%<br>Arboles / southwest county: RH 10%, wind/gust 21 mph, thunder 11%<br>Chimney Rock / west county: RH 10%, wind/gust 18 mph, thunder 15% |
| Fri, Aug 7 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Pagosa Springs: RH 14%, wind/gust 16 mph, thunder 15%<br>Arboles / southwest county: RH 12%, wind/gust 22 mph, thunder 15%<br>Chimney Rock / west county: RH 11%, wind/gust 18 mph, thunder 15% |
| Sat, Aug 8 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Pagosa Springs: RH 14%, wind/gust 17 mph, thunder 17%<br>Arboles / southwest county: RH 11%, wind/gust 21 mph, thunder 15%<br>Chimney Rock / west county: RH 11%, wind/gust 20 mph, thunder 15% |

## Sample Point Status

- Pagosa Springs: COZ295 (matches), forecast zone COZ023, county zone COC007
- Arboles / southwest county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Chimney Rock / west county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Piedra / north county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Chromo / southeast county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Durango / La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Bayfield / east La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Ignacio / southeast La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
