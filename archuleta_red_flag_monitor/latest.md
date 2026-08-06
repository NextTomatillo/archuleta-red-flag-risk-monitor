# Archuleta County fire-weather monitor

Generated: Aug 5, 2026 at 5:37 PM MDT (Pagosa Springs, CO local time)
Next update: Aug 6, 2026 at 5:20 AM MDT (Pagosa Springs, CO local time)
Date/time basis: Pagosa Springs, CO local time (America/Denver)
> **Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## At A Glance

- Fire-weather tier: **CONCERN**
- PSPS likelihood: **LIKELY**
- PSPS likely dates: Thu, Aug 6
- PSPS watch dates: Wed, Aug 5; Sun, Aug 9; Mon, Aug 10
- Monitor heads-up recommended: **YES** - Send this monitor report because fire-weather screening tier is CONCERN; PSPS screening level is LIKELY; a material current wildfire is reported in Archuleta County. This is not an official LPEA or NWS notice.
- HIGH dates: None
- CONCERN dates: Wed, Aug 5; Thu, Aug 6; Sun, Aug 9; Mon, Aug 10
- ELEVATED dates: Fri, Aug 7; Sat, Aug 8
- Official NWS Red Flag / Fire Weather alerts (COZ295): 0
- LPEA signal: `operational_outage_active` - Official LPEA outage data indicates an operational outage; use as grid context, not PSPS/fire evidence unless LPEA identifies that cause.
- LPEA source coverage: 13 sources; 5/5 official social sources reachable
- Current Archuleta County wildfires: 1
- Official evacuation notices: No current evacuation order or warning detected in the checked official county feeds.
- NWS discussion: NWS discussion contains fire-weather concern language.

## Decision Support

- Summary: Highest LPEA PSPS concern is Thu, Aug 6 near Durango / La Plata County (LIKELY 65/100), driven by red-flag wind/gust signal near 28 mph; very dry RH near 9%; 7 sampled hours are near red-flag thresholds. NIFC reports 1 current wildfire in Archuleta County.
- Confidence: **MEDIUM** (69/100) - 8/8 sampled weather points available; 7/7 fire-posture sources reachable; official NWS alert zones checked; 12/13 LPEA public sources reachable; LPEA active/update sources checked; active LPEA operational outage context checked separately from PSPS scoring; authoritative NIFC current-incident feed checked for Archuleta County; official Archuleta County evacuation feeds checked; forecast changed substantially versus prior run; no confirmed PSPS events logged yet for calibration
- Weather fire-potential peak: Thu, Aug 6: Durango / La Plata County EXTREME 86/100
- Red Flag likelihood peak: Thu, Aug 6: Durango / La Plata County LIKELY 77/100
- LPEA PSPS peak: Thu, Aug 6: Durango / La Plata County LIKELY 65/100
- Method: rules-based decision support using public weather, fire-posture, and LPEA source signals; scores are screening estimates, not official or statistically calibrated probabilities.

| Date | Weather fire potential | Red Flag likelihood | LPEA PSPS | Main window |
| --- | --- | --- | --- | --- |
| Wed, Aug 5 | Durango / La Plata County: VERY HIGH 75/100 | Arboles / southwest county: WATCH 66/100 | Arboles / southwest county: WATCH 62/100 | 6 PM-7 PM local; 2 near/red-flag threshold hours. |
| Thu, Aug 6 | Durango / La Plata County: EXTREME 86/100 | Durango / La Plata County: LIKELY 77/100 | Durango / La Plata County: LIKELY 65/100 | 3 PM-11 PM local; 7 near/red-flag threshold hours. |
| Fri, Aug 7 | Durango / La Plata County: HIGH 56/100 | Piedra / north county: POSSIBLE 30/100 | Piedra / north county: ELEVATED 43/100 | Peak ingredients near 12 AM local; RH 21%, wind 23 mph. |
| Sat, Aug 8 | Pagosa Springs: MODERATE 48/100 | Arboles / southwest county: LOW 25/100 | Arboles / southwest county: ELEVATED 32/100 | Peak ingredients near 6 PM local; RH 12%, wind 20 mph. |
| Sun, Aug 9 | Durango / La Plata County: VERY HIGH 74/100 | Durango / La Plata County: WATCH 57/100 | Durango / La Plata County: WATCH 52/100 | 4 PM-5 PM local; 2 near/red-flag threshold hours. |
| Mon, Aug 10 | Arboles / southwest county: HIGH 61/100 | Arboles / southwest county: WATCH 55/100 | Arboles / southwest county: WATCH 46/100 | 3 PM-5 PM local; 3 near/red-flag threshold hours. |
| Tue, Aug 11 | Bayfield / east La Plata County: LOW 34/100 | Arboles / southwest county: LOW 16/100 | Arboles / southwest county: ELEVATED 30/100 | 3 PM-3 PM local; 1 near/red-flag threshold hour. |

## Analyst Interpretation

- Headline: Fire-weather screening eased to CONCERN, but Thursday near Durango remains the strongest weather-driven PSPS signal.
- Summary: Thursday has the strongest combined signal near Durango: LIKELY PSPS screening at 65/100, relative humidity near 9%, gusts near 28 mph, and an EXTREME fire-danger estimate. No official COZ295 Red Flag or Fire Weather alert is active; one unplanned one-customer Durango-area outage has no identified PSPS or fire-weather cause. Rio Blanco is mapped at about 1,388 acres and 55% containment, with no evacuation notice detected.
- Uncertainty: Confidence is medium: 8/8 weather and 7/7 fire-posture sources were available, but only 12/13 LPEA sources responded, the forecast shifted materially, and no confirmed PSPS events exist for calibration.
- Evidence used: overall_status, weather_peaks, official_alerts, forecast_change, lpea_context, fire_posture, active_incidents, calibration
- This interpretation cannot change the deterministic tiers, scores, official alerts, or notification decision.

Changing drivers:
- The first WATCH-or-higher PSPS date moved later from Tuesday to Wednesday as overall momentum eased.
- Wednesday eased from LIKELY to WATCH, with its score down 12 points and the leading location shifting to Arboles.
- Monday remains WATCH, but its screening score eased 8 points from the prior run.

What to watch next:
- Watch Thursday's 3-11 PM Durango-area window for relative humidity near 9% and gusts near 28 mph.
- Check whether Thursday's signal strengthens or an official NWS fire-weather alert is issued.
- Keep the localized LPEA outage separate from PSPS inference unless LPEA identifies a fire-weather or safety-shutoff cause.
- Monitor Rio Blanco and official county evacuation feeds for changes.

## Trend Intelligence

- Summary: Momentum is easing versus the prior run (Aug 4 at 5:56 PM MDT); forecast volatility is high and first WATCH-or-higher date is Wed, Aug 5.
- Momentum: **Easing**
- Forecast volatility: **HIGH** (34/100)
- First WATCH-or-higher PSPS date: Wed, Aug 5
- Watch-date movement: First WATCH-or-higher PSPS date moved later from Tue, Aug 4 to Wed, Aug 5.
- Method: compares current forecast evidence against prior local forecast history.

Notable changes:
- First WATCH-or-higher PSPS date moved later from Tue, Aug 4 to Wed, Aug 5.
- Wed, Aug 5: easing vs prior run; PSPS LIKELY -> WATCH; score -12, wind -1 mph, RH +1%, red-flag hours -4. Driver shifted to Arboles / southwest county.
- Mon, Aug 10: easing vs prior run; PSPS WATCH -> WATCH; score -8, wind 0 mph, RH +1%, red-flag hours 0.

## Public Analysis Export

- Summary: Highest LPEA PSPS concern is Thu, Aug 6 near Durango / La Plata County (LIKELY 65/100), driven by red-flag wind/gust signal near 28 mph; very dry RH near 9%; 7 sampled hours are near red-flag thresholds. NIFC reports 1 current wildfire in Archuleta County.
- Trend: Momentum is easing versus the prior run (Aug 4 at 5:56 PM MDT); forecast volatility is high and first WATCH-or-higher date is Wed, Aug 5.
- Confidence: **MEDIUM** (69/100)
- First WATCH-or-higher PSPS date: Wed, Aug 5
- PSPS peak: Thu, Aug 6 near Durango / La Plata County at LIKELY 65/100
- Red Flag peak: Thu, Aug 6 near Durango / La Plata County at LIKELY 77/100
- Weather fire-potential peak: Thu, Aug 6 near Durango / La Plata County at EXTREME 86/100
- LPEA operational outage context: 1 active outage; 0 planned and 1 unplanned; 1 customer out. No fire-weather or PSPS cause is identified.
- Public JSON: `archuleta_red_flag_monitor/public_analysis_export.json`

What changed:
- First WATCH-or-higher PSPS date moved later from Tue, Aug 4 to Wed, Aug 5.
- Wed, Aug 5: easing vs prior run; PSPS LIKELY -> WATCH; score -12, wind -1 mph, RH +1%, red-flag hours -4. Driver shifted to Arboles / southwest county.
- Mon, Aug 10: easing vs prior run; PSPS WATCH -> WATCH; score -8, wind 0 mph, RH +1%, red-flag hours 0.

What to watch next:
- Check whether the largest day-level changes line up with wind/RH movement or public-source context.
- Check whether the LPEA active match is still a broad red-flag banner rather than direct PSPS/outage intent.
- Watch whether the highest-risk locations remain consistent across runs or the driver area is moving.
- If a PSPS occurs, log the confirmed date, location, and source so future hit-rate scoring can improve.

## PSPS Likelihood

- **PSPS means Public Safety Power Shutoff:** a planned, safety-related power shutoff LPEA may use during dangerous fire-weather conditions to reduce wildfire ignition risk. See [LPEA PSPS guidance](https://lpea.coop/psps) and the [LPEA outage center](https://lpea.coop/outage-center); if power is out, also check the [LPEA outage map](https://outage.lpea.coop).
- Overall: **LIKELY** - PSPS likelihood is high on weather-driven red-flag days; prepare for possible LPEA safety-related interruption behavior.
- Likely PSPS watch dates: Thu, Aug 6
- PSPS watch dates: Wed, Aug 5; Sun, Aug 9; Mon, Aug 10
- LPEA signal basis: LPEA active/update source contains red-flag, wildfire, or power-interruption language.
- Note: This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

| Date | PSPS likelihood | Driver locations | Weather basis |
| --- | --- | --- | --- |
| Wed, Aug 5 | WATCH | Arboles / southwest county (WATCH 62/100); Ignacio / southeast La Plata County (WATCH 57/100); Durango / La Plata County (WATCH 52/100); Bayfield / east La Plata County (WATCH 50/100) | Top weather score 60/100 at Arboles / southwest county. Weather score 60/100: RH 8%, wind/gust 26 mph, red-flag hours 1, near-threshold hours 2. |
| Thu, Aug 6 | LIKELY | Durango / La Plata County (LIKELY 65/100); Arboles / southwest county (WATCH 57/100); Ignacio / southeast La Plata County (WATCH 55/100); Bayfield / east La Plata County (WATCH 54/100) | Top weather score 61/100 at Durango / La Plata County. Weather score 61/100: RH 9%, wind/gust 28 mph, red-flag hours 2, near-threshold hours 7. |
| Fri, Aug 7 | ELEVATED | Piedra / north county (ELEVATED 43/100); Durango / La Plata County (ELEVATED 42/100); Arboles / southwest county (ELEVATED 35/100) | Top weather score 41/100 at Piedra / north county. Weather score 41/100: RH 8%, wind/gust 23 mph, red-flag hours 0, near-threshold hours 0. |
| Sat, Aug 8 | ELEVATED | Arboles / southwest county (ELEVATED 32/100); Chimney Rock / west county (ELEVATED 32/100); Ignacio / southeast La Plata County (ELEVATED 30/100) | Top weather score 30/100 at Arboles / southwest county. Weather score 30/100: RH 10%, wind/gust 20 mph, red-flag hours 0, near-threshold hours 0. |
| Sun, Aug 9 | WATCH | Durango / La Plata County (WATCH 52/100); Arboles / southwest county (WATCH 50/100); Bayfield / east La Plata County (WATCH 50/100) | Top weather score 48/100 at Arboles / southwest county. Weather score 48/100: RH 11%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 2. |
| Mon, Aug 10 | WATCH | Arboles / southwest county (WATCH 46/100) | Top weather score 44/100 at Arboles / southwest county. Weather score 44/100: RH 14%, wind/gust 23 mph, red-flag hours 0, near-threshold hours 3. |
| Tue, Aug 11 | ELEVATED | Arboles / southwest county (ELEVATED 30/100); Bayfield / east La Plata County (ELEVATED 24/100); Ignacio / southeast La Plata County (ELEVATED 22/100) | Top weather score 28/100 at Arboles / southwest county. Weather score 28/100: RH 17%, wind/gust 23 mph, red-flag hours 0, near-threshold hours 1. |

## Area-Specific Outlook

| Area | Today | Peak this run | Highest-risk window |
| --- | --- | --- | --- |
| Durango | WATCH 52/100 | Thu, Aug 6: LIKELY 65/100 | 3 PM-11 PM local; 7 near/red-flag threshold hours. |
| Arboles | WATCH 62/100 | Wed, Aug 5: WATCH 62/100 | 6 PM-7 PM local; 2 near/red-flag threshold hours. |
| Ignacio | WATCH 57/100 | Wed, Aug 5: WATCH 57/100 | 6 PM-7 PM local; 2 near/red-flag threshold hours. |
| Bayfield | WATCH 50/100 | Thu, Aug 6: WATCH 54/100 | 2 PM-10 PM local; 6 near/red-flag threshold hours. |
| Piedra | ELEVATED 40/100 | Thu, Aug 6: WATCH 49/100 | 9 PM-9 PM local; 1 near/red-flag threshold hour. |
| Chimney Rock | ELEVATED 43/100 | Wed, Aug 5: ELEVATED 43/100 | 6 PM-6 PM local; 1 near/red-flag threshold hour. |
| Pagosa Springs | ELEVATED 34/100 | Wed, Aug 5: ELEVATED 34/100 | Peak ingredients near 6 PM local; RH 13%, wind 20 mph. |
| Chromo | ELEVATED 32/100 | Wed, Aug 5: ELEVATED 32/100 | Peak ingredients near 6 PM local; RH 11%, wind 18 mph. |

## Current Fires + Evacuations

- Incident summary: 1 current wildfire reported in Archuleta County; no current evacuation notice detected in checked county feeds.
- Evacuation status: **NONE DETECTED** - No current evacuation order or warning detected in the checked official county feeds.
- Safety note: Current incidents and evacuation notices are operational context. They do not raise PSPS scores by themselves; follow official evacuation instructions immediately.

### Current NIFC Incidents

| Incident | Type | Size | Containment | Nearest monitored area | Updated |
| --- | --- | --- | --- | --- | --- |
| Rio Blanco | Wildfire | 1,387.74 acres | 55% | Chromo / southeast county (9.9 mi) | Aug 5 at 5:36 PM MDT |

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
- WATCH/LIKELY false-watch past days: 49
- Pending WATCH/LIKELY dates in current forecast: Wed, Aug 5; Thu, Aug 6; Sun, Aug 9; Mon, Aug 10
- Calibration source: manual PSPS event log plus forecast history from prior monitor runs.

### Red Flag / Fire Weather Calibration

- Summary: 3/3 official Red Flag / Fire Weather episodes had a pre-alert HIGH monitor signal; date-level result was 21/21. Episode-average lead time: 3.5 days.
- Official alert episodes logged: 3 (21 alert dates)
- Episode-level pre-alert HIGH hit rate: 100%
- Date-level pre-alert HIGH hit rate: 100%
- Episode-level average lead time: 3.5 days
- HIGH false-watch past days: 18
- Pending HIGH dates in current forecast: None
- Calibration source: official NWS Red Flag / Fire Weather alert dates plus forecast history from prior monitor runs.

## Official Weather Alerts

- Monitored NWS zones: COC007, COC067, COZ019, COZ022, COZ023, COZ295
- [Air Quality Alert](https://api.weather.gov/alerts/urn:oid:2.49.0.1.840.0.c7ff73802fcb7d74e1ab5a1e0a2abdbc1bb15c4b.001.1): Air Quality Alert issued August 5 at 4:10PM MDT by NWS Grand Junction CO; 2026-08-05T16:10:00-06:00 to 2026-08-06T09:00:00-06:00; zones COC007, COC029, COC033, COC037, COC045, COC051, COC053, COC067, COC077, COC081, COC083, COC085, COC091, COC097, COC103, COC107, COC111, COC113
- [Air Quality Alert](https://api.weather.gov/alerts/urn:oid:2.49.0.1.840.0.0cc88f0e111c36e340048c0c4c22b9a3630c3173.001.1): Air Quality Alert issued August 5 at 9:10AM MDT by NWS Grand Junction CO; 2026-08-05T09:10:00-06:00 to 2026-08-06T09:00:00-06:00; zones COC007, COC029, COC033, COC037, COC045, COC051, COC053, COC067, COC077, COC081, COC083, COC085, COC091, COC097, COC103, COC107, COC111, COC113

## LPEA Power Signal

- Status: `operational_outage_active` - Official LPEA outage data indicates an operational outage; use as grid context, not PSPS/fire evidence unless LPEA identifies that cause.
- Meaning: Active source match means a monitored LPEA active/update source currently contains fire, outage, PSPS, or power-interruption keywords. Operational outages are shown separately and are not treated as PSPS/fire evidence unless the source text says so.
- Operational outage context: 1 active outage; 0 planned and 1 unplanned; 1 customer out. No fire-weather or PSPS cause is identified.
- Source coverage: 13 sources; 5/5 official social sources reachable
- Evidence quality: 0 operational, 4 active/update, 0 archive/context, 6 reference source matches.
- Operational outage source links: [99 WINTERHAWK DR](https://outage.lpea.coop)
- Active/update source pages with matches: LPEA X (power outage, outage map, high winds, restore power); LPEA LinkedIn (wildfire, fire mitigation)
- Distinct active/update signals: LPEA X (power outage, outage map, high winds, restore power); LPEA X (power outage, outage map, high winds, restore power); LPEA LinkedIn (wildfire, fire mitigation); LPEA LinkedIn (wildfire, fire mitigation)
- Example signal: ...ibrary! 1 2 519 LPEA @LaPlataElectric May 7, 2024 LPEA members are experiencing power outages in the Bayfield and Pagosa Springs areas. Approximately 200 meters are out and it is suspected that the high winds are...
- Reference/context hits: [LPEA outage center](https://lpea.coop/outage-center); [LPEA wildfire / public safety power shutoffs](https://lpea.coop/psps); [LPEA red flag outage impact page](https://lpea.coop/outages/red-flag-warnings-and-impact-outages-prioritizing-safety-our-members); [LPEA fire mitigation](https://lpea.coop/fire-mitigation); [LPEA latest news](https://lpea.coop/Posts)

**Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## Next 7 Days

| Date | Tier | Main reason | Worst sampled metrics |
| --- | --- | --- | --- |
| Wed, Aug 5 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Pagosa Springs: RH 12%, wind/gust 20 mph, thunder 1%<br>Arboles / southwest county: RH 8%, wind/gust 26 mph, thunder 0%<br>Chimney Rock / west county: RH 8%, wind/gust 22 mph, thunder 1% |
| Thu, Aug 6 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Pagosa Springs: RH 11%, wind/gust 20 mph, thunder 6%<br>Arboles / southwest county: RH 8%, wind/gust 24 mph, thunder 0%<br>Chimney Rock / west county: RH 7%, wind/gust 21 mph, thunder 3% |
| Fri, Aug 7 | ELEVATED | Pagosa Springs: Elevated ingredient present: very low RH forecast near 9%. | Pagosa Springs: RH 9%, wind/gust 17 mph, thunder 4%<br>Arboles / southwest county: RH 7%, wind/gust 17 mph, thunder 0%<br>Chimney Rock / west county: RH 6%, wind/gust 20 mph, thunder 1% |
| Sat, Aug 8 | ELEVATED | Pagosa Springs: Elevated ingredient present: very low RH forecast near 15%. | Pagosa Springs: RH 15%, wind/gust 16 mph, thunder 9%<br>Arboles / southwest county: RH 10%, wind/gust 20 mph, thunder 5%<br>Chimney Rock / west county: RH 10%, wind/gust 17 mph, thunder 6% |
| Sun, Aug 9 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 11%, wind/gust 21 mph, thunder 11%<br>Chimney Rock / west county: RH 11%, wind/gust 20 mph, thunder 15%<br>Chromo / southeast county: RH 15%, wind/gust 15 mph, thunder 25% |
| Mon, Aug 10 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 14%, wind/gust 23 mph, thunder 25%<br>Chimney Rock / west county: RH 13%, wind/gust 21 mph, thunder 32%<br>Bayfield / east La Plata County: RH 18%, wind/gust 22 mph, thunder 31% |
| Tue, Aug 11 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 22%, wind/gust 16 mph, thunder 51%<br>Arboles / southwest county: RH 17%, wind/gust 23 mph, thunder 29%<br>Chimney Rock / west county: RH 17%, wind/gust 20 mph, thunder 45% |

## Sample Point Status

- Pagosa Springs: COZ295 (matches), forecast zone COZ023, county zone COC007
- Arboles / southwest county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Chimney Rock / west county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Piedra / north county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Chromo / southeast county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Durango / La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Bayfield / east La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Ignacio / southeast La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
