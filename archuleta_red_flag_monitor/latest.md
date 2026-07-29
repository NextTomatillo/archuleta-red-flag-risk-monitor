# Archuleta County fire-weather monitor

Generated: Jul 29, 2026 at 1:36 PM MDT (Pagosa Springs, CO local time)
Next update: Jul 29, 2026 at 5:20 PM MDT (Pagosa Springs, CO local time)
Date/time basis: Pagosa Springs, CO local time (America/Denver)
> **Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## At A Glance

- Fire-weather tier: **CONCERN**
- PSPS likelihood: **LIKELY**
- PSPS likely dates: Mon, Aug 3
- PSPS watch dates: Tue, Aug 4
- Monitor heads-up recommended: **YES** - Send this monitor report because fire-weather screening tier is CONCERN; PSPS screening level is LIKELY; an official Archuleta County evacuation order or warning is active. This is not an official LPEA or NWS notice.
- HIGH dates: None
- CONCERN dates: Thu, Jul 30; Mon, Aug 3; Tue, Aug 4
- ELEVATED dates: Fri, Jul 31; Sat, Aug 1; Sun, Aug 2
- Official NWS Red Flag / Fire Weather alerts (COZ295): 0
- LPEA signal: `operational_outage_active` - Official LPEA outage data indicates an operational outage; use as grid context, not PSPS/fire evidence unless LPEA identifies that cause.
- LPEA source coverage: 13 sources; 5/5 official social sources reachable
- Current Archuleta County wildfires: 3
- Official evacuation notices: 1 evacuation order and 3 evacuation warnings detected in recent official county notices.
- NWS discussion: No concerning fire-weather language found in latest GJT discussion.

## Decision Support

- Summary: Highest LPEA PSPS concern is Mon, Aug 3 near Ignacio / southeast La Plata County (LIKELY 65/100), driven by red-flag wind/gust signal near 25 mph; very dry RH near 12%; 5 sampled hours are near red-flag thresholds. 1 evacuation order and 3 evacuation warnings detected in recent official county notices.
- Confidence: **HIGH** (77/100) - 8/8 sampled weather points available; 7/7 fire-posture sources reachable; official NWS alert zones checked; 13/13 LPEA public sources reachable; LPEA active/update sources checked; active LPEA operational outage context checked separately from PSPS scoring; authoritative NIFC current-incident feed checked for Archuleta County; official Archuleta County evacuation feeds checked; no confirmed PSPS events logged yet for calibration
- Weather fire-potential peak: Mon, Aug 3: Durango / La Plata County VERY HIGH 79/100
- Red Flag likelihood peak: Mon, Aug 3: Ignacio / southeast La Plata County WATCH 71/100
- LPEA PSPS peak: Mon, Aug 3: Ignacio / southeast La Plata County LIKELY 65/100
- Method: rules-based decision support using public weather, fire-posture, and LPEA source signals; scores are screening estimates, not official or statistically calibrated probabilities.

| Date | Weather fire potential | Red Flag likelihood | LPEA PSPS | Main window |
| --- | --- | --- | --- | --- |
| Wed, Jul 29 | Durango / La Plata County: MODERATE 40/100 | Durango / La Plata County: LOW 8/100 | Durango / La Plata County: ELEVATED 26/100 | Peak ingredients near 5 PM local; RH 23%, wind 21 mph. |
| Thu, Jul 30 | Chimney Rock / west county: HIGH 64/100 | Chimney Rock / west county: POSSIBLE 50/100 | Chimney Rock / west county: ELEVATED 42/100 | 3 PM-4 PM local; 2 near/red-flag threshold hours. |
| Fri, Jul 31 | Durango / La Plata County: HIGH 55/100 | Durango / La Plata County: LOW 25/100 | Durango / La Plata County: ELEVATED 38/100 | 7 PM-7 PM local; 1 near/red-flag threshold hour. |
| Sat, Aug 1 | Chimney Rock / west county: MODERATE 48/100 | Chimney Rock / west county: LOW 25/100 | Chimney Rock / west county: ELEVATED 30/100 | Peak ingredients near 4 PM local; RH 13%, wind 16 mph. |
| Sun, Aug 2 | Chimney Rock / west county: MODERATE 48/100 | Chimney Rock / west county: LOW 25/100 | Chimney Rock / west county: ELEVATED 30/100 | Peak ingredients near 4 PM local; RH 14%, wind 17 mph. |
| Mon, Aug 3 | Durango / La Plata County: VERY HIGH 79/100 | Ignacio / southeast La Plata County: WATCH 71/100 | Ignacio / southeast La Plata County: LIKELY 65/100 | 3 PM-7 PM local; 5 near/red-flag threshold hours. |
| Tue, Aug 4 | Ignacio / southeast La Plata County: VERY HIGH 72/100 | Ignacio / southeast La Plata County: WATCH 63/100 | Ignacio / southeast La Plata County: WATCH 61/100 | 3 PM-4 PM local; 2 near/red-flag threshold hours. |


## Trend Intelligence

- Summary: Momentum is steady versus the prior run (Jul 29 at 1:21 PM MDT); forecast volatility is low and first WATCH-or-higher date is Mon, Aug 3.
- Momentum: **Steady**
- Forecast volatility: **LOW** (0/100)
- First WATCH-or-higher PSPS date: Mon, Aug 3
- Watch-date movement: First WATCH-or-higher PSPS date remains Mon, Aug 3.
- Method: compares current forecast evidence against prior local forecast history.

Notable changes:
- First WATCH-or-higher PSPS date remains Mon, Aug 3.
- No major day-level movement versus the prior run.

## Public Analysis Export

- Summary: Highest LPEA PSPS concern is Mon, Aug 3 near Ignacio / southeast La Plata County (LIKELY 65/100), driven by red-flag wind/gust signal near 25 mph; very dry RH near 12%; 5 sampled hours are near red-flag thresholds. 1 evacuation order and 3 evacuation warnings detected in recent official county notices.
- Trend: Momentum is steady versus the prior run (Jul 29 at 1:21 PM MDT); forecast volatility is low and first WATCH-or-higher date is Mon, Aug 3.
- Confidence: **HIGH** (77/100)
- First WATCH-or-higher PSPS date: Mon, Aug 3
- PSPS peak: Mon, Aug 3 near Ignacio / southeast La Plata County at LIKELY 65/100
- Red Flag peak: Mon, Aug 3 near Ignacio / southeast La Plata County at WATCH 71/100
- Weather fire-potential peak: Mon, Aug 3 near Durango / La Plata County at VERY HIGH 79/100
- LPEA operational outage context: 2 active outages; 1 planned and 1 unplanned; 4 customers out. No fire-weather or PSPS cause is identified.
- Public JSON: `archuleta_red_flag_monitor/public_analysis_export.json`

What changed:
- First WATCH-or-higher PSPS date remains Mon, Aug 3.
- No major day-level movement versus the prior run.

What to watch next:
- Check whether the largest day-level changes line up with wind/RH movement or public-source context.
- Check whether the LPEA active match is still a broad red-flag banner rather than direct PSPS/outage intent.
- Watch whether the highest-risk locations remain consistent across runs or the driver area is moving.
- If a PSPS occurs, log the confirmed date, location, and source so future hit-rate scoring can improve.

## PSPS Likelihood

- **PSPS means Public Safety Power Shutoff:** a planned, safety-related power shutoff LPEA may use during dangerous fire-weather conditions to reduce wildfire ignition risk. See [LPEA PSPS guidance](https://lpea.coop/psps) and the [LPEA outage center](https://lpea.coop/outage-center); if power is out, also check the [LPEA outage map](https://outage.lpea.coop).
- Overall: **LIKELY** - PSPS likelihood is high on weather-driven red-flag days; prepare for possible LPEA safety-related interruption behavior.
- Likely PSPS watch dates: Mon, Aug 3
- PSPS watch dates: Tue, Aug 4
- LPEA signal basis: LPEA active/update source contains red-flag, wildfire, or power-interruption language.
- Note: This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

| Date | PSPS likelihood | Driver locations | Weather basis |
| --- | --- | --- | --- |
| Wed, Jul 29 | ELEVATED | Durango / La Plata County (ELEVATED 26/100); Bayfield / east La Plata County (ELEVATED 20/100); Ignacio / southeast La Plata County (ELEVATED 20/100) | Top weather score 22/100 at Durango / La Plata County. Weather score 22/100: RH 20%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 0. |
| Thu, Jul 30 | ELEVATED | Chimney Rock / west county (ELEVATED 42/100); Arboles / southwest county (ELEVATED 40/100); Durango / La Plata County (ELEVATED 26/100) | Top weather score 38/100 at Arboles / southwest county. Weather score 38/100: RH 18%, wind/gust 23 mph, red-flag hours 0, near-threshold hours 3. |
| Fri, Jul 31 | ELEVATED | Durango / La Plata County (ELEVATED 38/100); Ignacio / southeast La Plata County (ELEVATED 38/100); Chimney Rock / west county (ELEVATED 34/100) | Top weather score 34/100 at Durango / La Plata County. Weather score 34/100: RH 15%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 1. |
| Sat, Aug 1 | ELEVATED | Chimney Rock / west county (ELEVATED 30/100); Durango / La Plata County (ELEVATED 30/100); Bayfield / east La Plata County (ELEVATED 30/100) | Top weather score 26/100 at Arboles / southwest county. Weather score 26/100: RH 13%, wind/gust 17 mph, red-flag hours 0, near-threshold hours 0. |
| Sun, Aug 2 | ELEVATED | Chimney Rock / west county (ELEVATED 30/100); Ignacio / southeast La Plata County (ELEVATED 30/100); Arboles / southwest county (ELEVATED 28/100) | Top weather score 26/100 at Arboles / southwest county. Weather score 26/100: RH 13%, wind/gust 18 mph, red-flag hours 0, near-threshold hours 0. |
| Mon, Aug 3 | LIKELY | Ignacio / southeast La Plata County (LIKELY 65/100); Durango / La Plata County (WATCH 56/100); Bayfield / east La Plata County (WATCH 52/100); Arboles / southwest county (WATCH 50/100) | Top weather score 61/100 at Ignacio / southeast La Plata County. Weather score 61/100: RH 12%, wind/gust 25 mph, red-flag hours 2, near-threshold hours 5. |
| Tue, Aug 4 | WATCH | Ignacio / southeast La Plata County (WATCH 61/100); Arboles / southwest county (WATCH 46/100) | Top weather score 57/100 at Ignacio / southeast La Plata County. Weather score 57/100: RH 14%, wind/gust 25 mph, red-flag hours 0, near-threshold hours 2. |

## Area-Specific Outlook

| Area | Today | Peak this run | Highest-risk window |
| --- | --- | --- | --- |
| Ignacio | ELEVATED 20/100 | Mon, Aug 3: LIKELY 65/100 | 3 PM-7 PM local; 5 near/red-flag threshold hours. |
| Durango | ELEVATED 26/100 | Mon, Aug 3: WATCH 56/100 | 3 PM-7 PM local; 5 near/red-flag threshold hours. |
| Bayfield | ELEVATED 20/100 | Mon, Aug 3: WATCH 52/100 | 3 PM-6 PM local; 4 near/red-flag threshold hours. |
| Arboles | LOW 16/100 | Mon, Aug 3: WATCH 50/100 | 4 PM-6 PM local; 3 near/red-flag threshold hours. |
| Chimney Rock | ELEVATED 18/100 | Thu, Jul 30: ELEVATED 42/100 | 3 PM-4 PM local; 2 near/red-flag threshold hours. |
| Pagosa Springs | LOW 12/100 | Mon, Aug 3: ELEVATED 30/100 | Peak ingredients near 4 PM local; RH 15%, wind 17 mph. |
| Piedra | LOW 12/100 | Mon, Aug 3: ELEVATED 30/100 | Peak ingredients near 3 PM local; RH 15%, wind 15 mph. |
| Chromo | LOW 12/100 | Mon, Aug 3: ELEVATED 30/100 | Peak ingredients near 11 PM local; RH 43%, wind 16 mph. |

## Current Fires + Evacuations

- Incident summary: Official evacuation notices are active; 3 current wildfires reported in Archuleta County.
- Evacuation status: **ACTIVE** - 1 evacuation order and 3 evacuation warnings detected in recent official county notices.
- Safety note: Current incidents and evacuation notices are operational context. They do not raise PSPS scores by themselves; follow official evacuation instructions immediately.

### Official Evacuation Notices

| Level | Area | Issued | Official notice |
| --- | --- | --- | --- |
| WARNING | County Road 337 and County Road 339 area | Jul 28 at 6:42 PM MDT | [Open notice](https://nixle.us/HH7YX) |
| WARNING | Pinon Hills Subdivision, at Mile marker 13.5 on County Road 500 | Jul 28 at 6:18 PM MDT | [Open notice](https://nixle.us/HH7XB) |
| ORDER | County Road 335 | Jul 28 at 4:28 PM MDT | [Open notice](https://nixle.us/HH7KM) |
| WARNING | Lower Blanco area | Jul 28 at 4:09 PM MDT | [Open notice](https://nixle.us/HH7HT) |

### Current NIFC Incidents

| Incident | Type | Size | Containment | Nearest monitored area | Updated |
| --- | --- | --- | --- | --- | --- |
| Rio Blanco | Wildfire | 440.27 acres | 0% | Chromo / southeast county (9.9 mi) | Jul 29 at 12:58 PM MDT |
| Blanco | Wildfire | 0.41 acres | Not reported | Pagosa Springs (9.2 mi) | Jul 27 at 5:30 PM MDT |
| Walker | Wildfire | 0.10 acres | Not reported | Arboles / southwest county (2.9 mi) | Jul 29 at 11:20 AM MDT |

Official links: [NIFC map](https://www.nifc.gov/fire-information/maps), [Archuleta County fire updates](https://sheriff.archuletacounty.gov/divisions/emergency-operations/fire-updates-and-information/), [County alerts](https://nixle.us/archuleta-county-office-of-emergency-management-aux/), [Watch Duty](https://app.watchduty.org/)

## Fire Posture + Restrictions

- Summary: 5 official sources indicate fire restrictions or staged restrictions.
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
| Southern Ute / Ignacio | STAGE 2 | UNKNOWN | [Southern Ute Indian Tribe](https://www.southernute-nsn.gov/) |

## Forecast Calibration

### PSPS Calibration

- Summary: No confirmed LPEA PSPS events logged yet; calibration will start once events are added.
- Confirmed PSPS events logged: 0
- Candidate/unconfirmed events logged: 0
- WATCH/LIKELY false-watch past days: 44
- Pending WATCH/LIKELY dates in current forecast: Mon, Aug 3; Tue, Aug 4
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

- Status: `operational_outage_active` - Official LPEA outage data indicates an operational outage; use as grid context, not PSPS/fire evidence unless LPEA identifies that cause.
- Meaning: Active source match means a monitored LPEA active/update source currently contains fire, outage, PSPS, or power-interruption keywords. Operational outages are shown separately and are not treated as PSPS/fire evidence unless the source text says so.
- Operational outage context: 2 active outages; 1 planned and 1 unplanned; 4 customers out. No fire-weather or PSPS cause is identified.
- Source coverage: 13 sources; 5/5 official social sources reachable
- Evidence quality: 0 operational, 4 active/update, 0 archive/context, 6 reference source matches.
- Operational outage source links: [4838 CR 633](https://outage.lpea.coop); [358 Quarter Horse](https://outage.lpea.coop)
- Active/update source pages with matches: LPEA homepage (public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation, restoration); LPEA X (power outage, outage map, high winds, restore power); LPEA LinkedIn (wildfire, fire mitigation)
- Distinct active/update signals: LPEA X (power outage, outage map, high winds, restore power); LPEA X (power outage, outage map, high winds, restore power); LPEA LinkedIn (wildfire, fire mitigation); LPEA LinkedIn (wildfire, fire mitigation)
- Example signal: ...ibrary! 1 2 516 LPEA @LaPlataElectric May 7, 2024 LPEA members are experiencing power outages in the Bayfield and Pagosa Springs areas. Approximately 200 meters are out and it is suspected that the high winds are...
- Reference/context hits: [LPEA outage center](https://lpea.coop/outage-center); [LPEA wildfire / public safety power shutoffs](https://lpea.coop/psps); [LPEA red flag outage impact page](https://lpea.coop/outages/red-flag-warnings-and-impact-outages-prioritizing-safety-our-members); [LPEA fire mitigation](https://lpea.coop/fire-mitigation); [LPEA latest news](https://lpea.coop/Posts)

**Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## Next 7 Days

| Date | Tier | Main reason | Worst sampled metrics |
| --- | --- | --- | --- |
| Wed, Jul 29 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 26%, wind/gust 18 mph, thunder 17%<br>Arboles / southwest county: RH 21%, wind/gust 20 mph, thunder 14%<br>Chimney Rock / west county: RH 20%, wind/gust 20 mph, thunder 15% |
| Thu, Jul 30 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 18%, wind/gust 23 mph, thunder 7%<br>Chimney Rock / west county: RH 17%, wind/gust 21 mph, thunder 8% |
| Fri, Jul 31 | ELEVATED | Arboles / southwest county: Elevated ingredient present: very low RH forecast near 12%. | Arboles / southwest county: RH 12%, wind/gust 20 mph, thunder 2%<br>Chimney Rock / west county: RH 12%, wind/gust 16 mph, thunder 3%<br>Durango / La Plata County: RH 15%, wind/gust 21 mph, thunder 5% |
| Sat, Aug 1 | ELEVATED | Arboles / southwest county: Elevated ingredient present: very low RH forecast near 13%. | Arboles / southwest county: RH 13%, wind/gust 17 mph, thunder 8%<br>Chimney Rock / west county: RH 13%, wind/gust 16 mph, thunder 11%<br>Durango / La Plata County: RH 14%, wind/gust 20 mph, thunder 11% |
| Sun, Aug 2 | ELEVATED | Arboles / southwest county: Elevated ingredient present: very low RH forecast near 13%. | Arboles / southwest county: RH 13%, wind/gust 18 mph, thunder 3%<br>Chimney Rock / west county: RH 14%, wind/gust 17 mph, thunder 7%<br>Ignacio / southeast La Plata County: RH 15%, wind/gust 18 mph, thunder 4% |
| Mon, Aug 3 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Pagosa Springs: RH 15%, wind/gust 17 mph, thunder 9%<br>Arboles / southwest county: RH 10%, wind/gust 22 mph, thunder 7%<br>Chimney Rock / west county: RH 10%, wind/gust 20 mph, thunder 8% |
| Tue, Aug 4 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 13%, wind/gust 24 mph, thunder 23%<br>Chimney Rock / west county: RH 13%, wind/gust 21 mph, thunder 31%<br>Durango / La Plata County: RH 16%, wind/gust 22 mph, thunder 26% |

## Sample Point Status

- Pagosa Springs: COZ295 (matches), forecast zone COZ023, county zone COC007
- Arboles / southwest county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Chimney Rock / west county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Piedra / north county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Chromo / southeast county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Durango / La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Bayfield / east La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Ignacio / southeast La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
