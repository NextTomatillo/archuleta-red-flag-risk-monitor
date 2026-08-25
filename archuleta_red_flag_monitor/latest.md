# Archuleta County fire-weather monitor

Generated: Aug 25, 2026 at 9:25 AM MDT (Pagosa Springs, CO local time)
Next update: Aug 25, 2026 at 5:20 PM MDT (Pagosa Springs, CO local time)
Date/time basis: Pagosa Springs, CO local time (America/Denver)
> **Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## At A Glance

- Fire-weather tier: **HIGH**
- PSPS likelihood: **LIKELY**
- PSPS likely dates: Sat, Aug 29
- PSPS watch dates: Tue, Aug 25; Fri, Aug 28
- Monitor heads-up recommended: **YES** - Send this monitor report because fire-weather screening tier is HIGH; PSPS screening level is LIKELY; a material current wildfire is reported in Archuleta County. This is not an official LPEA or NWS notice.
- HIGH dates: Sat, Aug 29
- CONCERN dates: Tue, Aug 25; Wed, Aug 26; Fri, Aug 28
- ELEVATED dates: Thu, Aug 27; Sun, Aug 30
- Official NWS Red Flag / Fire Weather alerts (COZ295): 0
- LPEA signal: `operational_outage_active` - Official LPEA outage data indicates an operational outage; use as grid context, not PSPS/fire evidence unless LPEA identifies that cause.
- LPEA source coverage: 13 sources; 5/5 official social sources reachable
- Current Archuleta County wildfires: 1
- Official evacuation notices: No current evacuation order or warning detected in the checked official county feeds.
- NWS discussion: NWS discussion contains fire-weather concern language.

## Decision Support

- Summary: Highest LPEA PSPS concern is Sat, Aug 29 near Arboles / southwest county (LIKELY 69/100), driven by red-flag wind/gust signal near 26 mph; red-flag RH near 15%; 3 sampled hours meet red-flag screen. NIFC reports 1 current wildfire in Archuleta County.
- Confidence: **MEDIUM** (69/100) - 8/8 sampled weather points available; 7/7 fire-posture sources reachable; official NWS alert zones checked; 13/13 LPEA public sources reachable; LPEA active/update sources checked; active LPEA operational outage context checked separately from PSPS scoring; authoritative NIFC current-incident feed checked for Archuleta County; official Archuleta County evacuation feeds checked; forecast changed substantially versus prior run; no confirmed PSPS events logged yet for calibration
- Weather fire-potential peak: Sat, Aug 29: Chimney Rock / west county VERY HIGH 78/100
- Red Flag likelihood peak: Sat, Aug 29: Arboles / southwest county LIKELY 81/100
- LPEA PSPS peak: Sat, Aug 29: Arboles / southwest county LIKELY 69/100
- Method: rules-based decision support using public weather, fire-posture, and LPEA source signals; scores are screening estimates, not official or statistically calibrated probabilities.

| Date | Weather fire potential | Red Flag likelihood | LPEA PSPS | Main window |
| --- | --- | --- | --- | --- |
| Tue, Aug 25 | Arboles / southwest county: HIGH 61/100 | Arboles / southwest county: WATCH 55/100 | Arboles / southwest county: WATCH 46/100 | 4 PM-6 PM local; 3 near/red-flag threshold hours. |
| Wed, Aug 26 | Chimney Rock / west county: HIGH 69/100 | Chimney Rock / west county: POSSIBLE 50/100 | Chimney Rock / west county: ELEVATED 35/100 | Peak ingredients near 4 PM local; RH 16%, wind 18 mph. |
| Thu, Aug 27 | Arboles / southwest county: MODERATE 45/100 | Arboles / southwest county: LOW 27/100 | Arboles / southwest county: ELEVATED 40/100 | 3 PM-3 PM local; 1 near/red-flag threshold hour. |
| Fri, Aug 28 | Chimney Rock / west county: VERY HIGH 71/100 | Arboles / southwest county: WATCH 58/100 | Arboles / southwest county: WATCH 50/100 | 3 PM-6 PM local; 4 near/red-flag threshold hours. |
| Sat, Aug 29 | Chimney Rock / west county: VERY HIGH 78/100 | Arboles / southwest county: LIKELY 81/100 | Arboles / southwest county: LIKELY 69/100 | 2 PM-6 PM local; 5 near/red-flag threshold hours. |
| Sun, Aug 30 | Bayfield / east La Plata County: MODERATE 39/100 | Arboles / southwest county: LOW 25/100 | Arboles / southwest county: ELEVATED 33/100 | Peak ingredients near 4 PM local; RH 20%, wind 25 mph. |
| Mon, Aug 31 | Chimney Rock / west county: MODERATE 38/100 | Arboles / southwest county: LOW 8/100 | Arboles / southwest county: ELEVATED 24/100 | Peak ingredients near 4 PM local; RH 21%, wind 23 mph. |

## Analyst Interpretation

- Headline: Today moved into PSPS WATCH and Saturday remains LIKELY near Arboles; official COZ295 alerts are zero, and two planned Durango outages are not fire-related.
- Summary: PSPS screening moved earlier: Tue, Aug 25 is now WATCH 46/100, Fri remains WATCH 50/100, and Sat remains LIKELY 69/100 near Arboles; these are screening estimates, not LPEA notices. Official COZ295 alerts remain zero. LPEA lists two planned Durango outages affecting 30 customers, attributed to construction and maintenance rather than fire weather or PSPS; Rio Blanco remains the only listed county wildfire at 1,387.74 acres and 100% containment, with no evacuation notice detected.
- Uncertainty: Confidence is MEDIUM 69/100 because forecast volatility is HIGH 45/100 and no confirmed PSPS events exist for calibration; the timing and driver area may still change.
- Evidence used: overall_status, weather_peaks, official_alerts, forecast_change, lpea_context, fire_posture, active_incidents, calibration
- This interpretation cannot change the deterministic tiers, scores, official alerts, or notification decision.

Changing drivers:
- The first WATCH-or-higher PSPS date moved earlier from Friday, Aug 28 to Tuesday, Aug 25.
- Tuesday worsened from ELEVATED to WATCH, rising 6 points as projected RH fell 1 percentage point.
- Sunday eased from WATCH to ELEVATED, falling 23 points as projected RH rose 2 percentage points.
- Saturday remains the peak near Arboles at PSPS LIKELY 69/100 and red-flag LIKELY 81/100.

What to watch next:
- Monitor today's WATCH conditions near Arboles through the late-afternoon risk window.
- Recheck Saturday's LIKELY peak after the next forecast update because volatility remains high.
- Keep the two planned Durango outages separate from PSPS evidence unless LPEA identifies a fire-weather cause.
- Continue official NWS, wildfire, and evacuation checks; COZ295 alerts are zero and no evacuation notice was detected.

## Trend Intelligence

- Summary: Momentum is steady versus the prior run (Aug 24 at 4:23 PM MDT); forecast volatility is high and first WATCH-or-higher date is Tue, Aug 25.
- Momentum: **Steady**
- Forecast volatility: **HIGH** (45/100)
- First WATCH-or-higher PSPS date: Tue, Aug 25
- Watch-date movement: First WATCH-or-higher PSPS date moved earlier from Fri, Aug 28 to Tue, Aug 25.
- Method: compares current forecast evidence against prior local forecast history.

Notable changes:
- First WATCH-or-higher PSPS date moved earlier from Fri, Aug 28 to Tue, Aug 25.
- Sun, Aug 30: easing vs prior run; PSPS WATCH -> ELEVATED; score -23, wind +1 mph, RH +2%, red-flag hours 0.
- Tue, Aug 25: worsening vs prior run; PSPS ELEVATED -> WATCH; score +6, wind 0 mph, RH -1%, red-flag hours 0.

## Public Analysis Export

- Summary: Highest LPEA PSPS concern is Sat, Aug 29 near Arboles / southwest county (LIKELY 69/100), driven by red-flag wind/gust signal near 26 mph; red-flag RH near 15%; 3 sampled hours meet red-flag screen. NIFC reports 1 current wildfire in Archuleta County.
- Trend: Momentum is steady versus the prior run (Aug 24 at 4:23 PM MDT); forecast volatility is high and first WATCH-or-higher date is Tue, Aug 25.
- Confidence: **MEDIUM** (69/100)
- First WATCH-or-higher PSPS date: Tue, Aug 25
- PSPS peak: Sat, Aug 29 near Arboles / southwest county at LIKELY 69/100
- Red Flag peak: Sat, Aug 29 near Arboles / southwest county at LIKELY 81/100
- Weather fire-potential peak: Sat, Aug 29 near Chimney Rock / west county at VERY HIGH 78/100
- LPEA operational outage context: 2 active outages; 2 planned and 0 unplanned; 30 customers out. No fire-weather or PSPS cause is identified.
- Public JSON: `archuleta_red_flag_monitor/public_analysis_export.json`

What changed:
- First WATCH-or-higher PSPS date moved earlier from Fri, Aug 28 to Tue, Aug 25.
- Sun, Aug 30: easing vs prior run; PSPS WATCH -> ELEVATED; score -23, wind +1 mph, RH +2%, red-flag hours 0.
- Tue, Aug 25: worsening vs prior run; PSPS ELEVATED -> WATCH; score +6, wind 0 mph, RH -1%, red-flag hours 0.

What to watch next:
- Check whether the largest day-level changes line up with wind/RH movement or public-source context.
- Check whether the LPEA active match is still a broad red-flag banner rather than direct PSPS/outage intent.
- Watch whether the highest-risk locations remain consistent across runs or the driver area is moving.
- If a PSPS occurs, log the confirmed date, location, and source so future hit-rate scoring can improve.

## PSPS Likelihood

- **PSPS means Public Safety Power Shutoff:** a planned, safety-related power shutoff LPEA may use during dangerous fire-weather conditions to reduce wildfire ignition risk. See [LPEA PSPS guidance](https://lpea.coop/psps) and the [LPEA outage center](https://lpea.coop/outage-center); if power is out, also check the [LPEA outage map](https://outage.lpea.coop).
- Overall: **LIKELY** - PSPS likelihood is high on weather-driven red-flag days; prepare for possible LPEA safety-related interruption behavior.
- Likely PSPS watch dates: Sat, Aug 29
- PSPS watch dates: Tue, Aug 25; Fri, Aug 28
- LPEA signal basis: LPEA active/update source contains red-flag, wildfire, or power-interruption language.
- Note: This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

| Date | PSPS likelihood | Driver locations | Weather basis |
| --- | --- | --- | --- |
| Tue, Aug 25 | WATCH | Arboles / southwest county (WATCH 46/100) | Top weather score 44/100 at Arboles / southwest county. Weather score 44/100: RH 15%, wind/gust 22 mph, red-flag hours 0, near-threshold hours 3. |
| Wed, Aug 26 | ELEVATED | Chimney Rock / west county (ELEVATED 35/100); Arboles / southwest county (ELEVATED 28/100); Durango / La Plata County (ELEVATED 24/100) | Top weather score 33/100 at Chimney Rock / west county. Weather score 33/100: RH 15%, wind/gust 18 mph, red-flag hours 0, near-threshold hours 0. |
| Thu, Aug 27 | ELEVATED | Arboles / southwest county (ELEVATED 40/100); Ignacio / southeast La Plata County (ELEVATED 32/100); Chimney Rock / west county (ELEVATED 30/100) | Top weather score 38/100 at Arboles / southwest county. Weather score 38/100: RH 15%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 1. |
| Fri, Aug 28 | WATCH | Arboles / southwest county (WATCH 50/100); Chimney Rock / west county (WATCH 46/100) | Top weather score 48/100 at Arboles / southwest county. Weather score 48/100: RH 13%, wind/gust 23 mph, red-flag hours 0, near-threshold hours 4. |
| Sat, Aug 29 | LIKELY | Arboles / southwest county (LIKELY 69/100); Chimney Rock / west county (WATCH 59/100); Ignacio / southeast La Plata County (WATCH 51/100) | Top weather score 67/100 at Arboles / southwest county. Weather score 67/100: RH 15%, wind/gust 26 mph, red-flag hours 3, near-threshold hours 5. |
| Sun, Aug 30 | ELEVATED | Arboles / southwest county (ELEVATED 33/100); Bayfield / east La Plata County (ELEVATED 27/100); Ignacio / southeast La Plata County (ELEVATED 25/100) | Top weather score 31/100 at Arboles / southwest county. Weather score 31/100: RH 20%, wind/gust 25 mph, red-flag hours 0, near-threshold hours 0. |
| Mon, Aug 31 | ELEVATED | Arboles / southwest county (ELEVATED 24/100); Chimney Rock / west county (ELEVATED 24/100); Durango / La Plata County (ELEVATED 18/100) | Top weather score 22/100 at Arboles / southwest county. Weather score 22/100: RH 21%, wind/gust 23 mph, red-flag hours 0, near-threshold hours 0. |

## Area-Specific Outlook

| Area | Today | Peak this run | Highest-risk window |
| --- | --- | --- | --- |
| Arboles | WATCH 46/100 | Sat, Aug 29: LIKELY 69/100 | 2 PM-6 PM local; 5 near/red-flag threshold hours. |
| Chimney Rock | ELEVATED 36/100 | Sat, Aug 29: WATCH 59/100 | 2 PM-6 PM local; 5 near/red-flag threshold hours. |
| Ignacio | ELEVATED 28/100 | Sat, Aug 29: WATCH 51/100 | 2 PM-5 PM local; 4 near/red-flag threshold hours. |
| Chromo | LOW 16/100 | Sat, Aug 29: ELEVATED 40/100 | 4 PM-5 PM local; 2 near/red-flag threshold hours. |
| Durango | ELEVATED 24/100 | Fri, Aug 28: ELEVATED 40/100 | 3 PM-5 PM local; 3 near/red-flag threshold hours. |
| Bayfield | ELEVATED 24/100 | Fri, Aug 28: ELEVATED 40/100 | 3 PM-5 PM local; 3 near/red-flag threshold hours. |
| Pagosa Springs | LOW 12/100 | Sat, Aug 29: ELEVATED 26/100 | Peak ingredients near 4 PM local; RH 20%, wind 23 mph. |
| Piedra | ELEVATED 18/100 | Sat, Aug 29: ELEVATED 24/100 | Peak ingredients near 4 PM local; RH 22%, wind 21 mph. |

## Current Fires + Evacuations

- Incident summary: 1 current wildfire reported in Archuleta County; no current evacuation notice detected in checked county feeds.
- Evacuation status: **NONE DETECTED** - No current evacuation order or warning detected in the checked official county feeds.
- Safety note: Current incidents and evacuation notices are operational context. They do not raise PSPS scores by themselves; follow official evacuation instructions immediately.

### Current NIFC Incidents

| Incident | Type | Size | Containment | Nearest monitored area | Updated |
| --- | --- | --- | --- | --- | --- |
| Rio Blanco | Wildfire | 1,387.74 acres | 100% | Chromo / southeast county (9.9 mi) | Aug 18 at 7:20 PM MDT |

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
- WATCH/LIKELY false-watch past days: 64
- Pending WATCH/LIKELY dates in current forecast: Tue, Aug 25; Fri, Aug 28; Sat, Aug 29
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

- Status: `operational_outage_active` - Official LPEA outage data indicates an operational outage; use as grid context, not PSPS/fire evidence unless LPEA identifies that cause.
- Meaning: Active source match means a monitored LPEA active/update source currently contains fire, outage, PSPS, or power-interruption keywords. Operational outages are shown separately and are not treated as PSPS/fire evidence unless the source text says so.
- Operational outage context: 2 active outages; 2 planned and 0 unplanned; 30 customers out. No fire-weather or PSPS cause is identified.
- Source coverage: 13 sources; 5/5 official social sources reachable
- Evidence quality: 0 operational, 4 active/update, 0 archive/context, 6 reference source matches.
- Operational outage source links: [1831 GLENISLE AVE](https://outage.lpea.coop); [1465 W 3RD AVE](https://outage.lpea.coop)
- Active/update source pages with matches: LPEA homepage (public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation, restoration); LPEA X (power outage, outage map, high winds, restore power); LPEA LinkedIn (wildfire, public safety power shutoff, psps, power shutoff, shutoff, deenergize)
- Distinct active/update signals: LPEA X (power outage, outage map, high winds, restore power); LPEA X (power outage, outage map, high winds, restore power); LPEA LinkedIn (wildfire, public safety power shutoff, psps, power shutoff, shutoff, deenergize); LinkedIn PSPS explainer post (wildfire, public safety power shutoff, psps, power shutoff, shutoff, deenergize)
- Example signal: ...ibrary! 1 2 536 LPEA @LaPlataElectric May 7, 2024 LPEA members are experiencing power outages in the Bayfield and Pagosa Springs areas. Approximately 200 meters are out and it is suspected that the high winds are...
- Reference/context hits: [LPEA outage center](https://lpea.coop/outage-center); [LPEA wildfire / public safety power shutoffs](https://lpea.coop/psps); [LPEA red flag outage impact page](https://lpea.coop/outages/red-flag-warnings-and-impact-outages-prioritizing-safety-our-members); [LPEA fire mitigation](https://lpea.coop/fire-mitigation); [LPEA latest news](https://lpea.coop/Posts)

**Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## Next 7 Days

| Date | Tier | Main reason | Worst sampled metrics |
| --- | --- | --- | --- |
| Tue, Aug 25 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 15%, wind/gust 22 mph, thunder 9%<br>Chimney Rock / west county: RH 15%, wind/gust 21 mph, thunder 10% |
| Wed, Aug 26 | CONCERN | Chimney Rock / west county: Dry-thunder signal: 5 hourly periods combine thunder near 20% with limited precipitation and dry air. | Arboles / southwest county: RH 15%, wind/gust 17 mph, thunder 11%<br>Chimney Rock / west county: RH 15%, wind/gust 18 mph, thunder 20% |
| Thu, Aug 27 | ELEVATED | Arboles / southwest county: Elevated ingredient present: very low RH forecast near 15%; dry-thunder probability reaches 15%. | Arboles / southwest county: RH 15%, wind/gust 21 mph, thunder 15%<br>Ignacio / southeast La Plata County: RH 18%, wind/gust 23 mph, thunder 16% |
| Fri, Aug 28 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 13%, wind/gust 23 mph, thunder 2%<br>Chimney Rock / west county: RH 13%, wind/gust 22 mph, thunder 6%<br>Durango / La Plata County: RH 16%, wind/gust 23 mph, thunder 5% |
| Sat, Aug 29 | HIGH | Arboles / southwest county: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Arboles / southwest county: RH 15%, wind/gust 26 mph, thunder 19%<br>Chimney Rock / west county: RH 14%, wind/gust 25 mph, thunder 14%<br>Chromo / southeast county: RH 18%, wind/gust 22 mph, thunder 24% |
| Sun, Aug 30 | ELEVATED | Arboles / southwest county: Elevated ingredient present: wind/gust forecast near 25 mph. | Arboles / southwest county: RH 20%, wind/gust 25 mph, thunder 33%<br>Bayfield / east La Plata County: RH 24%, wind/gust 25 mph, thunder 33%<br>Ignacio / southeast La Plata County: RH 23%, wind/gust 26 mph, thunder 32% |
| Mon, Aug 31 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 28%, wind/gust 20 mph, thunder 50%<br>Arboles / southwest county: RH 21%, wind/gust 23 mph, thunder 34%<br>Chimney Rock / west county: RH 20%, wind/gust 22 mph, thunder 43% |

## Sample Point Status

- Pagosa Springs: COZ295 (matches), forecast zone COZ023, county zone COC007
- Arboles / southwest county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Chimney Rock / west county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Piedra / north county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Chromo / southeast county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Durango / La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Bayfield / east La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Ignacio / southeast La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
