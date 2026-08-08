# Archuleta County fire-weather monitor

Generated: Aug 7, 2026 at 6:08 PM MDT (Pagosa Springs, CO local time)
Next update: Aug 8, 2026 at 5:20 AM MDT (Pagosa Springs, CO local time)
Date/time basis: Pagosa Springs, CO local time (America/Denver)
> **Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## At A Glance

- Fire-weather tier: **CONCERN**
- PSPS likelihood: **WATCH**
- PSPS likely dates: None
- PSPS watch dates: Sun, Aug 9; Mon, Aug 10
- Monitor heads-up recommended: **YES** - Send this monitor report because fire-weather screening tier is CONCERN; PSPS screening level is WATCH; a material current wildfire is reported in Archuleta County. This is not an official LPEA or NWS notice.
- HIGH dates: None
- CONCERN dates: Sun, Aug 9; Mon, Aug 10; Tue, Aug 11
- ELEVATED dates: Fri, Aug 7; Sat, Aug 8
- Official NWS Red Flag / Fire Weather alerts (COZ295): 0
- LPEA signal: `operational_outage_active` - Official LPEA outage data indicates an operational outage; use as grid context, not PSPS/fire evidence unless LPEA identifies that cause.
- LPEA source coverage: 13 sources; 5/5 official social sources reachable
- Current Archuleta County wildfires: 1
- Official evacuation notices: No current evacuation order or warning detected in the checked official county feeds.
- NWS discussion: NWS discussion contains fire-weather concern language.

## Decision Support

- Summary: Highest LPEA PSPS concern is Mon, Aug 10 near Ignacio / southeast La Plata County (WATCH 51/100), driven by red-flag wind/gust signal near 25 mph; near-threshold RH near 18%; 2 sampled hours are near red-flag thresholds. NIFC reports 1 current wildfire in Archuleta County.
- Confidence: **MEDIUM** (74/100) - 8/8 sampled weather points available; 7/7 fire-posture sources reachable; official NWS alert zones checked; 13/13 LPEA public sources reachable; LPEA active/update sources checked; active LPEA operational outage context checked separately from PSPS scoring; authoritative NIFC current-incident feed checked for Archuleta County; official Archuleta County evacuation feeds checked; forecast changed moderately versus prior run; no confirmed PSPS events logged yet for calibration
- Weather fire-potential peak: Sun, Aug 9: Chimney Rock / west county VERY HIGH 71/100
- Red Flag likelihood peak: Sun, Aug 9: Arboles / southwest county WATCH 59/100
- LPEA PSPS peak: Mon, Aug 10: Ignacio / southeast La Plata County WATCH 51/100
- Method: rules-based decision support using public weather, fire-posture, and LPEA source signals; scores are screening estimates, not official or statistically calibrated probabilities.

| Date | Weather fire potential | Red Flag likelihood | LPEA PSPS | Main window |
| --- | --- | --- | --- | --- |
| Fri, Aug 7 | Pagosa Springs: MODERATE 52/100 | Arboles / southwest county: LOW 25/100 | Arboles / southwest county: ELEVATED 35/100 | Peak ingredients near 6 PM local; RH 8%, wind 17 mph. |
| Sat, Aug 8 | Pagosa Springs: MODERATE 52/100 | Pagosa Springs: LOW 25/100 | Pagosa Springs: ELEVATED 34/100 | Peak ingredients near 3 PM local; RH 12%, wind 15 mph. |
| Sun, Aug 9 | Chimney Rock / west county: VERY HIGH 71/100 | Arboles / southwest county: WATCH 59/100 | Arboles / southwest county: WATCH 50/100 | 4 PM-6 PM local; 3 near/red-flag threshold hours. |
| Mon, Aug 10 | Chimney Rock / west county: HIGH 62/100 | Ignacio / southeast La Plata County: WATCH 57/100 | Ignacio / southeast La Plata County: WATCH 51/100 | 2 PM-3 PM local; 2 near/red-flag threshold hours. |
| Tue, Aug 11 | Ignacio / southeast La Plata County: HIGH 55/100 | Ignacio / southeast La Plata County: POSSIBLE 50/100 | Ignacio / southeast La Plata County: ELEVATED 38/100 | 2 PM-3 PM local; 2 near/red-flag threshold hours. |
| Wed, Aug 12 | Durango / La Plata County: MODERATE 36/100 | Arboles / southwest county: LOW 8/100 | Arboles / southwest county: ELEVATED 24/100 | Peak ingredients near 3 PM local; RH 19%, wind 21 mph. |
| Thu, Aug 13 | Durango / La Plata County: MODERATE 36/100 | Durango / La Plata County: LOW 8/100 | Durango / La Plata County: ELEVATED 20/100 | Peak ingredients near 3 PM local; RH 30%, wind 21 mph. |

## Analyst Interpretation

- Headline: Fire-weather screening remains CONCERN, with PSPS WATCH conditions Sunday and Monday while two unrelated LPEA outages affect 24 customers.
- Summary: Screening peaks Sunday for fire danger near Chimney Rock and Arboles, while the highest PSPS estimate is WATCH 51/100 Monday near Ignacio. Official NWS data shows no COZ295 Red Flag or Fire Weather alert; official LPEA data shows two unplanned outages affecting 24 customers, with no fire-weather or PSPS cause identified. Rio Blanco remains mapped at about 1,388 acres and 55% containment, with no evacuation notice detected.
- Uncertainty: Forecast volatility is MEDIUM and no confirmed LPEA PSPS events exist for calibration; the active outages have no identified fire or PSPS cause, and public keyword matches may reflect older content.
- Evidence used: overall_status, weather_peaks, official_alerts, forecast_change, lpea_context, fire_posture, active_incidents, calibration
- This interpretation cannot change the deterministic tiers, scores, official alerts, or notification decision.

Changing drivers:
- The first WATCH-or-higher PSPS date remains Sunday, August 9.
- The highest PSPS estimate is WATCH 51/100 Monday near Ignacio, driven by gusts near 25 mph and relative humidity near 18%.
- Thursday, August 13 rose from LOW to ELEVATED, with the driver shifting to Durango / La Plata County.
- Official fire posture includes Stage 2 restrictions and VERY HIGH fire danger.

What to watch next:
- Watch the Arboles and Chimney Rock area Sunday afternoon as relative humidity approaches 11% and gusts approach 22 mph.
- Watch Ignacio Monday from 2-3 PM for gusts near 25 mph with relative humidity near 18%.
- Check the official LPEA outage viewer for restoration or an identified cause; do not treat these outages as PSPS without official confirmation.
- Monitor Rio Blanco and official county evacuation feeds for changes.

## Trend Intelligence

- Summary: Momentum is rising versus the prior run (Aug 7 at 6:30 AM MDT); forecast volatility is medium and first WATCH-or-higher date is Sun, Aug 9.
- Momentum: **Rising**
- Forecast volatility: **MEDIUM** (22/100)
- First WATCH-or-higher PSPS date: Sun, Aug 9
- Watch-date movement: First WATCH-or-higher PSPS date remains Sun, Aug 9.
- Method: compares current forecast evidence against prior local forecast history.

Notable changes:
- First WATCH-or-higher PSPS date remains Sun, Aug 9.
- Thu, Aug 13: worsening vs prior run; PSPS LOW -> ELEVATED; score +4, wind +2 mph, RH +3%, red-flag hours 0. Driver shifted to Durango / La Plata County.

## Public Analysis Export

- Summary: Highest LPEA PSPS concern is Mon, Aug 10 near Ignacio / southeast La Plata County (WATCH 51/100), driven by red-flag wind/gust signal near 25 mph; near-threshold RH near 18%; 2 sampled hours are near red-flag thresholds. NIFC reports 1 current wildfire in Archuleta County.
- Trend: Momentum is rising versus the prior run (Aug 7 at 6:30 AM MDT); forecast volatility is medium and first WATCH-or-higher date is Sun, Aug 9.
- Confidence: **MEDIUM** (74/100)
- First WATCH-or-higher PSPS date: Sun, Aug 9
- PSPS peak: Mon, Aug 10 near Ignacio / southeast La Plata County at WATCH 51/100
- Red Flag peak: Sun, Aug 9 near Arboles / southwest county at WATCH 59/100
- Weather fire-potential peak: Sun, Aug 9 near Chimney Rock / west county at VERY HIGH 71/100
- LPEA operational outage context: 2 active outages; 0 planned and 2 unplanned; 24 customers out. No fire-weather or PSPS cause is identified.
- Public JSON: `archuleta_red_flag_monitor/public_analysis_export.json`

What changed:
- First WATCH-or-higher PSPS date remains Sun, Aug 9.
- Thu, Aug 13: worsening vs prior run; PSPS LOW -> ELEVATED; score +4, wind +2 mph, RH +3%, red-flag hours 0. Driver shifted to Durango / La Plata County.

What to watch next:
- Check whether the largest day-level changes line up with wind/RH movement or public-source context.
- Check whether the LPEA active match is still a broad red-flag banner rather than direct PSPS/outage intent.
- Watch whether the highest-risk locations remain consistent across runs or the driver area is moving.
- If a PSPS occurs, log the confirmed date, location, and source so future hit-rate scoring can improve.

## PSPS Likelihood

- **PSPS means Public Safety Power Shutoff:** a planned, safety-related power shutoff LPEA may use during dangerous fire-weather conditions to reduce wildfire ignition risk. See [LPEA PSPS guidance](https://lpea.coop/psps) and the [LPEA outage center](https://lpea.coop/outage-center); if power is out, also check the [LPEA outage map](https://outage.lpea.coop).
- Overall: **WATCH** - PSPS watch screening is present from forecast thresholds or direct LPEA shutoff language; monitor official LPEA and NWS updates.
- Likely PSPS watch dates: None
- PSPS watch dates: Sun, Aug 9; Mon, Aug 10
- LPEA signal basis: LPEA active/update source contains red-flag, wildfire, or power-interruption language.
- Note: This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

| Date | PSPS likelihood | Driver locations | Weather basis |
| --- | --- | --- | --- |
| Fri, Aug 7 | ELEVATED | Arboles / southwest county (ELEVATED 35/100); Chimney Rock / west county (ELEVATED 35/100); Durango / La Plata County (ELEVATED 34/100) | Top weather score 33/100 at Arboles / southwest county. Weather score 33/100: RH 8%, wind/gust 17 mph, red-flag hours 0, near-threshold hours 0. |
| Sat, Aug 8 | ELEVATED | Pagosa Springs (ELEVATED 34/100); Durango / La Plata County (ELEVATED 34/100); Arboles / southwest county (ELEVATED 32/100) | Top weather score 30/100 at Pagosa Springs. Weather score 30/100: RH 12%, wind/gust 15 mph, red-flag hours 0, near-threshold hours 0. |
| Sun, Aug 9 | WATCH | Arboles / southwest county (WATCH 50/100); Chimney Rock / west county (WATCH 50/100); Ignacio / southeast La Plata County (WATCH 48/100); Bayfield / east La Plata County (WATCH 46/100) | Top weather score 48/100 at Arboles / southwest county. Weather score 48/100: RH 11%, wind/gust 22 mph, red-flag hours 0, near-threshold hours 3. |
| Mon, Aug 10 | WATCH | Ignacio / southeast La Plata County (WATCH 51/100) | Top weather score 51/100 at Ignacio / southeast La Plata County. Weather score 51/100: RH 18%, wind/gust 25 mph, red-flag hours 0, near-threshold hours 2. |
| Tue, Aug 11 | ELEVATED | Ignacio / southeast La Plata County (ELEVATED 38/100); Arboles / southwest county (ELEVATED 30/100); Durango / La Plata County (ELEVATED 26/100) | Top weather score 38/100 at Ignacio / southeast La Plata County. Weather score 38/100: RH 18%, wind/gust 23 mph, red-flag hours 0, near-threshold hours 2. |
| Wed, Aug 12 | ELEVATED | Arboles / southwest county (ELEVATED 24/100); Ignacio / southeast La Plata County (ELEVATED 22/100); Durango / La Plata County (ELEVATED 20/100) | Top weather score 22/100 at Arboles / southwest county. Weather score 22/100: RH 19%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 0. |
| Thu, Aug 13 | ELEVATED | Durango / La Plata County (ELEVATED 20/100); Arboles / southwest county (ELEVATED 18/100); Ignacio / southeast La Plata County (LOW 16/100) | Top weather score 16/100 at Arboles / southwest county. Weather score 16/100: RH 25%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 0. |

## Area-Specific Outlook

| Area | Today | Peak this run | Highest-risk window |
| --- | --- | --- | --- |
| Ignacio | ELEVATED 30/100 | Mon, Aug 10: WATCH 51/100 | 2 PM-3 PM local; 2 near/red-flag threshold hours. |
| Arboles | ELEVATED 35/100 | Sun, Aug 9: WATCH 50/100 | 4 PM-6 PM local; 3 near/red-flag threshold hours. |
| Chimney Rock | ELEVATED 35/100 | Sun, Aug 9: WATCH 50/100 | 5 PM-6 PM local; 2 near/red-flag threshold hours. |
| Durango | ELEVATED 34/100 | Sun, Aug 9: WATCH 46/100 | 3 PM-4 PM local; 2 near/red-flag threshold hours. |
| Bayfield | ELEVATED 32/100 | Sun, Aug 9: WATCH 46/100 | 3 PM-5 PM local; 3 near/red-flag threshold hours. |
| Pagosa Springs | ELEVATED 26/100 | Sat, Aug 8: ELEVATED 34/100 | Peak ingredients near 3 PM local; RH 12%, wind 15 mph. |
| Piedra | ELEVATED 24/100 | Sun, Aug 9: ELEVATED 34/100 | Peak ingredients near 8 PM local; RH 33%, wind 21 mph. |
| Chromo | ELEVATED 24/100 | Sat, Aug 8: ELEVATED 32/100 | Peak ingredients near 12 AM local; RH 35%, wind 17 mph. |

## Current Fires + Evacuations

- Incident summary: 1 current wildfire reported in Archuleta County; no current evacuation notice detected in checked county feeds.
- Evacuation status: **NONE DETECTED** - No current evacuation order or warning detected in the checked official county feeds.
- Safety note: Current incidents and evacuation notices are operational context. They do not raise PSPS scores by themselves; follow official evacuation instructions immediately.

### Current NIFC Incidents

| Incident | Type | Size | Containment | Nearest monitored area | Updated |
| --- | --- | --- | --- | --- | --- |
| Rio Blanco | Wildfire | 1,387.74 acres | 55% | Chromo / southeast county (9.9 mi) | Aug 6 at 6:14 PM MDT |

Official links: [NIFC map](https://www.nifc.gov/fire-information/maps), [Archuleta County fire updates](https://sheriff.archuletacounty.gov/divisions/emergency-operations/fire-updates-and-information/), [County alerts](https://nixle.us/archuleta-county-office-of-emergency-management-aux/), [Watch Duty](https://app.watchduty.org/)

## Fire Posture + Restrictions

- Summary: 4 official sources indicate fire restrictions or staged restrictions.
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
| Durango | STAGE 2 | UNKNOWN | [City of Durango](https://www.durangoco.gov/) |
| Southern Ute / Ignacio | UNKNOWN | UNKNOWN | [Southern Ute Indian Tribe](https://www.southernute-nsn.gov/) |

## Forecast Calibration

### PSPS Calibration

- Summary: No confirmed LPEA PSPS events logged yet; calibration will start once events are added.
- Confirmed PSPS events logged: 0
- Candidate/unconfirmed events logged: 0
- WATCH/LIKELY false-watch past days: 51
- Pending WATCH/LIKELY dates in current forecast: Sun, Aug 9; Mon, Aug 10
- Calibration source: manual PSPS event log plus forecast history from prior monitor runs.

### Red Flag / Fire Weather Calibration

- Summary: 3/3 official Red Flag / Fire Weather episodes had a pre-alert HIGH monitor signal; date-level result was 21/21. Episode-average lead time: 3.5 days.
- Official alert episodes logged: 3 (21 alert dates)
- Episode-level pre-alert HIGH hit rate: 100%
- Date-level pre-alert HIGH hit rate: 100%
- Episode-level average lead time: 3.5 days
- HIGH false-watch past days: 20
- Pending HIGH dates in current forecast: None
- Calibration source: official NWS Red Flag / Fire Weather alert dates plus forecast history from prior monitor runs.

## Official Weather Alerts

- Monitored NWS zones: COC007, COC067, COZ019, COZ022, COZ023, COZ295
- [Air Quality Alert](https://api.weather.gov/alerts/urn:oid:2.49.0.1.840.0.bcfcbc9848adf3339c5273474f9048f80718729e.004.1): Air Quality Alert issued August 7 at 5:10PM MDT by NWS Grand Junction CO; 2026-08-07T17:10:00-06:00 to 2026-08-08T09:00:00-06:00; zones COC007, COC051, COC053, COC085, COC091
- [Air Quality Alert](https://api.weather.gov/alerts/urn:oid:2.49.0.1.840.0.67b412ccc987aaf030e5a45549f9c9edf1209043.003.1): Air Quality Alert issued August 7 at 4:10PM MDT by NWS Grand Junction CO; 2026-08-07T16:10:00-06:00 to 2026-08-08T09:00:00-06:00; zones COC007, COC051, COC053, COC085, COC091
- [Air Quality Alert](https://api.weather.gov/alerts/urn:oid:2.49.0.1.840.0.70810374253fde4b7d0391df0634c1c16fc4721b.002.1): Air Quality Alert issued August 7 at 2:10PM MDT by NWS Grand Junction CO; 2026-08-07T14:10:00-06:00 to 2026-08-08T09:00:00-06:00; zones COC007, COC051, COC053, COC085, COC091
- [Air Quality Alert](https://api.weather.gov/alerts/urn:oid:2.49.0.1.840.0.d951a6a24336ef994e91f5970eb004c24df6d74a.002.1): Air Quality Alert issued August 7 at 12:10PM MDT by NWS Grand Junction CO; 2026-08-07T12:10:00-06:00 to 2026-08-08T09:00:00-06:00; zones COC007, COC051, COC053, COC085, COC091
- [Air Quality Alert](https://api.weather.gov/alerts/urn:oid:2.49.0.1.840.0.9b69296ea8b48edbf02732766a4292a38163ad27.002.1): Air Quality Alert issued August 7 at 9:10AM MDT by NWS Grand Junction CO; 2026-08-07T09:10:00-06:00 to 2026-08-08T09:00:00-06:00; zones COC007, COC051, COC053, COC085, COC091
- [Air Quality Alert](https://api.weather.gov/alerts/urn:oid:2.49.0.1.840.0.bcfcbc9848adf3339c5273474f9048f80718729e.002.1): Air Quality Alert issued August 7 at 5:10PM MDT by NWS Grand Junction CO; 2026-08-07T17:10:00-06:00 to 2026-08-08T09:00:00-06:00; zones COC067
- [Air Quality Alert](https://api.weather.gov/alerts/urn:oid:2.49.0.1.840.0.67b412ccc987aaf030e5a45549f9c9edf1209043.001.1): Air Quality Alert issued August 7 at 4:10PM MDT by NWS Grand Junction CO; 2026-08-07T16:10:00-06:00 to 2026-08-08T09:00:00-06:00; zones COC067

## LPEA Power Signal

- Status: `operational_outage_active` - Official LPEA outage data indicates an operational outage; use as grid context, not PSPS/fire evidence unless LPEA identifies that cause.
- Meaning: Active source match means a monitored LPEA active/update source currently contains fire, outage, PSPS, or power-interruption keywords. Operational outages are shown separately and are not treated as PSPS/fire evidence unless the source text says so.
- Operational outage context: 2 active outages; 0 planned and 2 unplanned; 24 customers out. No fire-weather or PSPS cause is identified.
- Source coverage: 13 sources; 5/5 official social sources reachable
- Evidence quality: 0 operational, 4 active/update, 0 archive/context, 6 reference source matches.
- Operational outage source links: [6085 CR 501](https://outage.lpea.coop); [380 VISION WAY CR 223](https://outage.lpea.coop)
- Active/update source pages with matches: LPEA homepage (public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation, restoration); LPEA X (power outage, outage map, high winds, restore power); LPEA LinkedIn (wildfire, fire mitigation)
- Distinct active/update signals: LPEA X (power outage, outage map, high winds, restore power); LPEA X (power outage, outage map, high winds, restore power); LPEA LinkedIn (wildfire, fire mitigation); LPEA LinkedIn (wildfire, fire mitigation)
- Example signal: ...ibrary! 1 2 519 LPEA @LaPlataElectric May 7, 2024 LPEA members are experiencing power outages in the Bayfield and Pagosa Springs areas. Approximately 200 meters are out and it is suspected that the high winds are...
- Reference/context hits: [LPEA outage center](https://lpea.coop/outage-center); [LPEA wildfire / public safety power shutoffs](https://lpea.coop/psps); [LPEA red flag outage impact page](https://lpea.coop/outages/red-flag-warnings-and-impact-outages-prioritizing-safety-our-members); [LPEA fire mitigation](https://lpea.coop/fire-mitigation); [LPEA latest news](https://lpea.coop/Posts)

**Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## Next 7 Days

| Date | Tier | Main reason | Worst sampled metrics |
| --- | --- | --- | --- |
| Fri, Aug 7 | ELEVATED | Pagosa Springs: Elevated ingredient present: very low RH forecast near 11%. | Pagosa Springs: RH 11%, wind/gust 14 mph, thunder 4%<br>Arboles / southwest county: RH 8%, wind/gust 17 mph, thunder 3%<br>Chimney Rock / west county: RH 8%, wind/gust 15 mph, thunder 2% |
| Sat, Aug 8 | ELEVATED | Pagosa Springs: Elevated ingredient present: very low RH forecast near 12%. | Pagosa Springs: RH 12%, wind/gust 15 mph, thunder 5%<br>Arboles / southwest county: RH 9%, wind/gust 17 mph, thunder 1%<br>Chimney Rock / west county: RH 9%, wind/gust 17 mph, thunder 4% |
| Sun, Aug 9 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 11%, wind/gust 22 mph, thunder 7%<br>Chimney Rock / west county: RH 11%, wind/gust 21 mph, thunder 7%<br>Piedra / north county: RH 18%, wind/gust 21 mph, thunder 16% |
| Mon, Aug 10 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 16%, wind/gust 23 mph, thunder 17%<br>Chimney Rock / west county: RH 16%, wind/gust 21 mph, thunder 30%<br>Ignacio / southeast La Plata County: RH 18%, wind/gust 25 mph, thunder 16% |
| Tue, Aug 11 | CONCERN | Ignacio / southeast La Plata County: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Ignacio / southeast La Plata County: RH 18%, wind/gust 23 mph, thunder 32% |
| Wed, Aug 12 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 27%, wind/gust 18 mph, thunder 70%<br>Arboles / southwest county: RH 19%, wind/gust 21 mph, thunder 42%<br>Chimney Rock / west county: RH 20%, wind/gust 18 mph, thunder 62% |
| Thu, Aug 13 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 32%, wind/gust 17 mph, thunder 74%<br>Arboles / southwest county: RH 25%, wind/gust 21 mph, thunder 51%<br>Chimney Rock / west county: RH 24%, wind/gust 18 mph, thunder 65% |

## Sample Point Status

- Pagosa Springs: COZ295 (matches), forecast zone COZ023, county zone COC007
- Arboles / southwest county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Chimney Rock / west county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Piedra / north county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Chromo / southeast county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Durango / La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Bayfield / east La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Ignacio / southeast La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
