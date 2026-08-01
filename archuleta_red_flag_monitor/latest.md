# Archuleta County fire-weather monitor

Generated: Aug 1, 2026 at 5:29 AM MDT (Pagosa Springs, CO local time)
Next update: Aug 1, 2026 at 5:20 PM MDT (Pagosa Springs, CO local time)
Date/time basis: Pagosa Springs, CO local time (America/Denver)
> **Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## At A Glance

- Fire-weather tier: **HIGH**
- PSPS likelihood: **LIKELY**
- PSPS likely dates: Mon, Aug 3; Tue, Aug 4
- PSPS watch dates: Wed, Aug 5; Thu, Aug 6
- Monitor heads-up recommended: **YES** - Send this monitor report because fire-weather screening tier is HIGH; PSPS screening level is LIKELY; a material current wildfire is reported in Archuleta County. This is not an official LPEA or NWS notice.
- HIGH dates: Mon, Aug 3; Tue, Aug 4
- CONCERN dates: Wed, Aug 5; Thu, Aug 6
- ELEVATED dates: Sat, Aug 1; Sun, Aug 2; Fri, Aug 7
- Official NWS Red Flag / Fire Weather alerts (COZ295): 0
- LPEA signal: `active_keyword_match` - LPEA active/update sources contained power-interruption keywords; review source before treating as confirmed outage intent.
- LPEA source coverage: 13 sources; 5/5 official social sources reachable
- Current Archuleta County wildfires: 1
- Official evacuation notices: No current evacuation order or warning detected in the checked official county feeds.
- NWS discussion: NWS discussion contains fire-weather concern language.

## Decision Support

- Summary: Highest LPEA PSPS concern is Mon, Aug 3 near Bayfield / east La Plata County (LIKELY 73/100), driven by red-flag wind/gust signal near 26 mph; very dry RH near 12%; 4 sampled hours meet red-flag screen. NIFC reports 1 current wildfire in Archuleta County.
- Confidence: **MEDIUM** (69/100) - 8/8 sampled weather points available; 7/7 fire-posture sources reachable; official NWS alert zones checked; 13/13 LPEA public sources reachable; LPEA active/update sources checked; authoritative NIFC current-incident feed checked for Archuleta County; official Archuleta County evacuation feeds checked; forecast changed substantially versus prior run; no confirmed PSPS events logged yet for calibration
- Weather fire-potential peak: Mon, Aug 3: Durango / La Plata County EXTREME 87/100
- Red Flag likelihood peak: Mon, Aug 3: Bayfield / east La Plata County LIKELY 84/100
- LPEA PSPS peak: Mon, Aug 3: Bayfield / east La Plata County LIKELY 73/100
- Method: rules-based decision support using public weather, fire-posture, and LPEA source signals; scores are screening estimates, not official or statistically calibrated probabilities.

| Date | Weather fire potential | Red Flag likelihood | LPEA PSPS | Main window |
| --- | --- | --- | --- | --- |
| Sat, Aug 1 | Durango / La Plata County: MODERATE 48/100 | Durango / La Plata County: LOW 25/100 | Durango / La Plata County: ELEVATED 30/100 | Peak ingredients near 3 PM local; RH 17%, wind 18 mph. |
| Sun, Aug 2 | Durango / La Plata County: MODERATE 48/100 | Arboles / southwest county: LOW 25/100 | Arboles / southwest county: ELEVATED 32/100 | Peak ingredients near 5 PM local; RH 11%, wind 18 mph. |
| Mon, Aug 3 | Durango / La Plata County: EXTREME 87/100 | Bayfield / east La Plata County: LIKELY 84/100 | Bayfield / east La Plata County: LIKELY 73/100 | 1 PM-7 PM local; 7 near/red-flag threshold hours. |
| Tue, Aug 4 | Durango / La Plata County: VERY HIGH 79/100 | Ignacio / southeast La Plata County: LIKELY 80/100 | Ignacio / southeast La Plata County: LIKELY 67/100 | 2 PM-6 PM local; 5 near/red-flag threshold hours. |
| Wed, Aug 5 | Durango / La Plata County: VERY HIGH 78/100 | Ignacio / southeast La Plata County: WATCH 69/100 | Ignacio / southeast La Plata County: WATCH 61/100 | 3 PM-6 PM local; 4 near/red-flag threshold hours. |
| Thu, Aug 6 | Arboles / southwest county: HIGH 62/100 | Arboles / southwest county: WATCH 57/100 | Arboles / southwest county: WATCH 50/100 | 4 PM-5 PM local; 2 near/red-flag threshold hours. |
| Fri, Aug 7 | Chimney Rock / west county: MODERATE 42/100 | Chimney Rock / west county: LOW 25/100 | Chimney Rock / west county: ELEVATED 28/100 | Peak ingredients near 3 PM local; RH 15%, wind 17 mph. |

## Analyst Interpretation

- Headline: HIGH fire-weather screening centers on Aug 3-4, while no official COZ295 fire alert or active LPEA outage is currently reported.
- Summary: The monitor recommends a heads-up: screening reaches HIGH on Aug 3-4, with the Aug 3 peak driven by very dry humidity, gusts near 26 mph, and several sampled red-flag hours. These are screening estimates, not official warnings or shutdown notices. Official checks show zero COZ295 fire-weather alerts and no active LPEA outage; one current Archuleta County wildfire is reported, with no evacuation order or warning detected in the checked county feeds.
- Uncertainty: PSPS scores are uncalibrated screening estimates: no confirmed LPEA PSPS events are logged, and 45 past WATCH/LIKELY days did not become confirmed events.
- Evidence used: overall_status, weather_peaks, official_alerts, forecast_change, lpea_context, fire_posture, active_incidents, calibration
- This interpretation cannot change the deterministic tiers, scores, official alerts, or notification decision.

Changing drivers:
- The first WATCH-or-higher PSPS screening date moved later from Jul 31 to Aug 3.
- Aug 6 worsened from ELEVATED to WATCH as humidity fell and winds increased.
- Aug 1 eased from WATCH to ELEVATED as forecast winds declined.
- Forecast momentum is rising and volatility is HIGH at 56/100.

What to watch next:
- Watch for an official NWS COZ295 fire-weather alert for Aug 3-4.
- Check whether LPEA posts direct outage or PSPS intent rather than general keyword context.
- Monitor the Rio Blanco wildfire and official county evacuation feeds.
- Recheck wind, humidity, and red-flag-hour changes for Aug 3-6.

## Trend Intelligence

- Summary: Momentum is rising versus the prior run (Jul 31 at 6:07 PM MDT); forecast volatility is high and first WATCH-or-higher date is Mon, Aug 3.
- Momentum: **Rising**
- Forecast volatility: **HIGH** (56/100)
- First WATCH-or-higher PSPS date: Mon, Aug 3
- Watch-date movement: First WATCH-or-higher PSPS date moved later from Fri, Jul 31 to Mon, Aug 3.
- Method: compares current forecast evidence against prior local forecast history.

Notable changes:
- First WATCH-or-higher PSPS date moved later from Fri, Jul 31 to Mon, Aug 3.
- Thu, Aug 6: worsening vs prior run; PSPS ELEVATED -> WATCH; score +24, wind +2 mph, RH -3%, red-flag hours 0. Driver shifted to Arboles / southwest county.
- Sat, Aug 1: easing vs prior run; PSPS WATCH -> ELEVATED; score -18, wind -4 mph, RH 0%, red-flag hours 0.
- Wed, Aug 5: worsening vs prior run; PSPS WATCH -> WATCH; score +11, wind +4 mph, RH 0%, red-flag hours 0. Driver shifted to Ignacio / southeast La Plata County.
- Tue, Aug 4: worsening vs prior run; PSPS LIKELY -> LIKELY; score -2, wind -4 mph, RH 0%, red-flag hours +2. Driver shifted to Ignacio / southeast La Plata County.

## Public Analysis Export

- Summary: Highest LPEA PSPS concern is Mon, Aug 3 near Bayfield / east La Plata County (LIKELY 73/100), driven by red-flag wind/gust signal near 26 mph; very dry RH near 12%; 4 sampled hours meet red-flag screen. NIFC reports 1 current wildfire in Archuleta County.
- Trend: Momentum is rising versus the prior run (Jul 31 at 6:07 PM MDT); forecast volatility is high and first WATCH-or-higher date is Mon, Aug 3.
- Confidence: **MEDIUM** (69/100)
- First WATCH-or-higher PSPS date: Mon, Aug 3
- PSPS peak: Mon, Aug 3 near Bayfield / east La Plata County at LIKELY 73/100
- Red Flag peak: Mon, Aug 3 near Bayfield / east La Plata County at LIKELY 84/100
- Weather fire-potential peak: Mon, Aug 3 near Durango / La Plata County at EXTREME 87/100
- LPEA operational outage context: No active outages are listed by the official LPEA outage viewer.
- Public JSON: `archuleta_red_flag_monitor/public_analysis_export.json`

What changed:
- First WATCH-or-higher PSPS date moved later from Fri, Jul 31 to Mon, Aug 3.
- Thu, Aug 6: worsening vs prior run; PSPS ELEVATED -> WATCH; score +24, wind +2 mph, RH -3%, red-flag hours 0. Driver shifted to Arboles / southwest county.
- Sat, Aug 1: easing vs prior run; PSPS WATCH -> ELEVATED; score -18, wind -4 mph, RH 0%, red-flag hours 0.
- Wed, Aug 5: worsening vs prior run; PSPS WATCH -> WATCH; score +11, wind +4 mph, RH 0%, red-flag hours 0. Driver shifted to Ignacio / southeast La Plata County.
- Tue, Aug 4: worsening vs prior run; PSPS LIKELY -> LIKELY; score -2, wind -4 mph, RH 0%, red-flag hours +2. Driver shifted to Ignacio / southeast La Plata County.

What to watch next:
- Check whether the largest day-level changes line up with wind/RH movement or public-source context.
- Check whether the LPEA active match is still a broad red-flag banner rather than direct PSPS/outage intent.
- Watch whether the highest-risk locations remain consistent across runs or the driver area is moving.
- If a PSPS occurs, log the confirmed date, location, and source so future hit-rate scoring can improve.

## PSPS Likelihood

- **PSPS means Public Safety Power Shutoff:** a planned, safety-related power shutoff LPEA may use during dangerous fire-weather conditions to reduce wildfire ignition risk. See [LPEA PSPS guidance](https://lpea.coop/psps) and the [LPEA outage center](https://lpea.coop/outage-center); if power is out, also check the [LPEA outage map](https://outage.lpea.coop).
- Overall: **LIKELY** - PSPS likelihood is high on weather-driven red-flag days; prepare for possible LPEA safety-related interruption behavior.
- Likely PSPS watch dates: Mon, Aug 3; Tue, Aug 4
- PSPS watch dates: Wed, Aug 5; Thu, Aug 6
- LPEA signal basis: LPEA active/update source contains red-flag, wildfire, or power-interruption language.
- Note: This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

| Date | PSPS likelihood | Driver locations | Weather basis |
| --- | --- | --- | --- |
| Sat, Aug 1 | ELEVATED | Durango / La Plata County (ELEVATED 30/100); Ignacio / southeast La Plata County (ELEVATED 26/100); Chimney Rock / west county (ELEVATED 24/100) | Top weather score 26/100 at Durango / La Plata County. Weather score 26/100: RH 14%, wind/gust 18 mph, red-flag hours 0, near-threshold hours 0. |
| Sun, Aug 2 | ELEVATED | Arboles / southwest county (ELEVATED 32/100); Chimney Rock / west county (ELEVATED 32/100); Durango / La Plata County (ELEVATED 30/100) | Top weather score 30/100 at Arboles / southwest county. Weather score 30/100: RH 11%, wind/gust 18 mph, red-flag hours 0, near-threshold hours 0. |
| Mon, Aug 3 | LIKELY | Bayfield / east La Plata County (LIKELY 73/100); Ignacio / southeast La Plata County (LIKELY 71/100); Durango / La Plata County (LIKELY 71/100); Arboles / southwest county (LIKELY 69/100) | Top weather score 71/100 at Bayfield / east La Plata County. Weather score 71/100: RH 12%, wind/gust 26 mph, red-flag hours 4, near-threshold hours 7. |
| Tue, Aug 4 | LIKELY | Ignacio / southeast La Plata County (LIKELY 67/100); Arboles / southwest county (WATCH 63/100); Durango / La Plata County (WATCH 56/100); Bayfield / east La Plata County (WATCH 54/100) | Top weather score 67/100 at Ignacio / southeast La Plata County. Weather score 67/100: RH 10%, wind/gust 26 mph, red-flag hours 3, near-threshold hours 5. |
| Wed, Aug 5 | WATCH | Ignacio / southeast La Plata County (WATCH 61/100); Durango / La Plata County (WATCH 56/100); Arboles / southwest county (WATCH 54/100); Bayfield / east La Plata County (WATCH 54/100) | Top weather score 61/100 at Ignacio / southeast La Plata County. Weather score 61/100: RH 13%, wind/gust 26 mph, red-flag hours 0, near-threshold hours 4. |
| Thu, Aug 6 | WATCH | Arboles / southwest county (WATCH 50/100) | Top weather score 48/100 at Arboles / southwest county. Weather score 48/100: RH 14%, wind/gust 22 mph, red-flag hours 0, near-threshold hours 2. |
| Fri, Aug 7 | ELEVATED | Ignacio / southeast La Plata County (ELEVATED 28/100); Chimney Rock / west county (ELEVATED 28/100); Arboles / southwest county (ELEVATED 22/100) | Top weather score 28/100 at Ignacio / southeast La Plata County. Weather score 28/100: RH 18%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 0. |

## Area-Specific Outlook

| Area | Today | Peak this run | Highest-risk window |
| --- | --- | --- | --- |
| Bayfield | ELEVATED 22/100 | Mon, Aug 3: LIKELY 73/100 | 1 PM-7 PM local; 7 near/red-flag threshold hours. |
| Durango | ELEVATED 30/100 | Mon, Aug 3: LIKELY 71/100 | 1 PM-7 PM local; 7 near/red-flag threshold hours. |
| Ignacio | ELEVATED 26/100 | Mon, Aug 3: LIKELY 71/100 | 2 PM-7 PM local; 6 near/red-flag threshold hours. |
| Arboles | ELEVATED 20/100 | Mon, Aug 3: LIKELY 69/100 | 2 PM-7 PM local; 6 near/red-flag threshold hours. |
| Chimney Rock | ELEVATED 24/100 | Mon, Aug 3: WATCH 54/100 | 3 PM-6 PM local; 4 near/red-flag threshold hours. |
| Pagosa Springs | LOW 10/100 | Mon, Aug 3: WATCH 48/100 | 4 PM-5 PM local; 2 near/red-flag threshold hours. |
| Chromo | LOW 8/100 | Tue, Aug 4: WATCH 45/100 | Peak ingredients near 10 PM local; RH 40%, wind 30 mph. |
| Piedra | ELEVATED 18/100 | Mon, Aug 3: ELEVATED 28/100 | Peak ingredients near 4 PM local; RH 14%, wind 20 mph. |

## Current Fires + Evacuations

- Incident summary: 1 current wildfire reported in Archuleta County; no current evacuation notice detected in checked county feeds.
- Evacuation status: **NONE DETECTED** - No current evacuation order or warning detected in the checked official county feeds.
- Safety note: Current incidents and evacuation notices are operational context. They do not raise PSPS scores by themselves; follow official evacuation instructions immediately.

### Current NIFC Incidents

| Incident | Type | Size | Containment | Nearest monitored area | Updated |
| --- | --- | --- | --- | --- | --- |
| Rio Blanco | Wildfire | 783.30 acres | 0% | Chromo / southeast county (9.9 mi) | Jul 31 at 7:16 PM MDT |

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
- WATCH/LIKELY false-watch past days: 45
- Pending WATCH/LIKELY dates in current forecast: Mon, Aug 3; Tue, Aug 4; Wed, Aug 5; Thu, Aug 6
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
| Sat, Aug 1 | ELEVATED | Arboles / southwest county: Elevated ingredient present: very low RH forecast near 14%. | Arboles / southwest county: RH 14%, wind/gust 14 mph, thunder 14%<br>Chimney Rock / west county: RH 14%, wind/gust 14 mph, thunder 23%<br>Piedra / north county: RH 18%, wind/gust 13 mph, thunder 18% |
| Sun, Aug 2 | ELEVATED | Arboles / southwest county: Elevated ingredient present: very low RH forecast near 11%. | Arboles / southwest county: RH 11%, wind/gust 18 mph, thunder 2%<br>Chimney Rock / west county: RH 12%, wind/gust 17 mph, thunder 4%<br>Durango / La Plata County: RH 15%, wind/gust 20 mph, thunder 6% |
| Mon, Aug 3 | HIGH | Arboles / southwest county: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 14%, wind/gust 21 mph, thunder 1%<br>Arboles / southwest county: RH 10%, wind/gust 26 mph, thunder 0%<br>Chimney Rock / west county: RH 9%, wind/gust 23 mph, thunder 0% |
| Tue, Aug 4 | HIGH | Ignacio / southeast La Plata County: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 14%, wind/gust 21 mph, thunder 6%<br>Arboles / southwest county: RH 9%, wind/gust 25 mph, thunder 0%<br>Chimney Rock / west county: RH 9%, wind/gust 22 mph, thunder 2% |
| Wed, Aug 5 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Pagosa Springs: RH 17%, wind/gust 18 mph, thunder 15%<br>Arboles / southwest county: RH 12%, wind/gust 21 mph, thunder 15%<br>Chimney Rock / west county: RH 12%, wind/gust 21 mph, thunder 15% |
| Thu, Aug 6 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 14%, wind/gust 22 mph, thunder 17%<br>Chimney Rock / west county: RH 13%, wind/gust 18 mph, thunder 29%<br>Ignacio / southeast La Plata County: RH 16%, wind/gust 23 mph, thunder 18% |
| Fri, Aug 7 | ELEVATED | Chimney Rock / west county: Elevated ingredient present: very low RH forecast near 15%. | Chimney Rock / west county: RH 15%, wind/gust 17 mph, thunder 34% |

## Sample Point Status

- Pagosa Springs: COZ295 (matches), forecast zone COZ023, county zone COC007
- Arboles / southwest county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Chimney Rock / west county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Piedra / north county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Chromo / southeast county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Durango / La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Bayfield / east La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Ignacio / southeast La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
