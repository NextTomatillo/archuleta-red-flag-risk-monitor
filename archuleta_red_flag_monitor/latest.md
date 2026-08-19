# Archuleta County fire-weather monitor

Generated: Aug 19, 2026 at 8:55 AM MDT (Pagosa Springs, CO local time)
Next update: Aug 19, 2026 at 5:20 PM MDT (Pagosa Springs, CO local time)
Date/time basis: Pagosa Springs, CO local time (America/Denver)
> **Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## At A Glance

- Fire-weather tier: **CONCERN**
- PSPS likelihood: **WATCH**
- PSPS likely dates: None
- PSPS watch dates: Mon, Aug 24; Tue, Aug 25
- Monitor heads-up recommended: **YES** - Send this monitor report because fire-weather screening tier is CONCERN; PSPS screening level is WATCH; a material current wildfire is reported in Archuleta County. This is not an official LPEA or NWS notice.
- HIGH dates: None
- CONCERN dates: Sun, Aug 23; Mon, Aug 24; Tue, Aug 25
- ELEVATED dates: Wed, Aug 19; Thu, Aug 20; Fri, Aug 21
- Official NWS Red Flag / Fire Weather alerts (COZ295): 0
- LPEA signal: `operational_outage_active` - Official LPEA outage data indicates an operational outage; use as grid context, not PSPS/fire evidence unless LPEA identifies that cause.
- LPEA source coverage: 13 sources; 5/5 official social sources reachable
- Current Archuleta County wildfires: 1
- Official evacuation notices: No current evacuation order or warning detected in the checked official county feeds.
- NWS discussion: No concerning fire-weather language found in latest GJT discussion.

## Decision Support

- Summary: Highest LPEA PSPS concern is Tue, Aug 25 near Chimney Rock / west county (WATCH 50/100), driven by near-threshold wind/gust signal near 21 mph; very dry RH near 12%; 2 sampled hours are near red-flag thresholds. NIFC reports 1 current wildfire in Archuleta County.
- Confidence: **MEDIUM** (69/100) - 8/8 sampled weather points available; 7/7 fire-posture sources reachable; official NWS alert zones checked; 13/13 LPEA public sources reachable; LPEA active/update sources checked; active LPEA operational outage context checked separately from PSPS scoring; authoritative NIFC current-incident feed checked for Archuleta County; official Archuleta County evacuation feeds checked; forecast changed substantially versus prior run; no confirmed PSPS events logged yet for calibration
- Weather fire-potential peak: Tue, Aug 25: Chimney Rock / west county VERY HIGH 71/100
- Red Flag likelihood peak: Tue, Aug 25: Ignacio / southeast La Plata County WATCH 61/100
- LPEA PSPS peak: Tue, Aug 25: Chimney Rock / west county WATCH 50/100
- Method: rules-based decision support using public weather, fire-posture, and LPEA source signals; scores are screening estimates, not official or statistically calibrated probabilities.

| Date | Weather fire potential | Red Flag likelihood | LPEA PSPS | Main window |
| --- | --- | --- | --- | --- |
| Wed, Aug 19 | Chimney Rock / west county: MODERATE 46/100 | Chimney Rock / west county: LOW 25/100 | Chimney Rock / west county: ELEVATED 32/100 | Peak ingredients near 3 PM local; RH 16%, wind 17 mph. |
| Thu, Aug 20 | Chimney Rock / west county: MODERATE 46/100 | Arboles / southwest county: LOW 25/100 | Durango / La Plata County: ELEVATED 30/100 | Peak ingredients near 3 PM local; RH 20%, wind 22 mph. |
| Fri, Aug 21 | Chimney Rock / west county: MODERATE 46/100 | Chimney Rock / west county: LOW 25/100 | Chimney Rock / west county: ELEVATED 28/100 | Peak ingredients near 8 PM local; RH 41%, wind 17 mph. |
| Sat, Aug 22 | Pagosa Springs: LOW 32/100 | Chimney Rock / west county: LOW 8/100 | Chimney Rock / west county: ELEVATED 22/100 | Peak ingredients near 3 PM local; RH 17%, wind 18 mph. |
| Sun, Aug 23 | Arboles / southwest county: HIGH 55/100 | Arboles / southwest county: POSSIBLE 50/100 | Arboles / southwest county: ELEVATED 40/100 | 3 PM-4 PM local; 2 near/red-flag threshold hours. |
| Mon, Aug 24 | Arboles / southwest county: HIGH 61/100 | Arboles / southwest county: WATCH 55/100 | Arboles / southwest county: WATCH 46/100 | 3 PM-5 PM local; 3 near/red-flag threshold hours. |
| Tue, Aug 25 | Chimney Rock / west county: VERY HIGH 71/100 | Ignacio / southeast La Plata County: WATCH 61/100 | Chimney Rock / west county: WATCH 50/100 | 3 PM-4 PM local; 2 near/red-flag threshold hours. |

## Analyst Interpretation

- Headline: Today's screening eased to ELEVATED, but area-wide risk remains CONCERN as PSPS WATCH shifts to Monday and Tuesday; no official COZ295 alert is active.
- Summary: Today is ELEVATED, while Monday and Tuesday are PSPS WATCH; Tuesday peaks near Chimney Rock at 50/100, with Red Flag WATCH 61/100 near Ignacio and VERY HIGH fire potential 71/100 near Chimney Rock. Official COZ295 alerts remain at zero. The official LPEA viewer lists three localized outages affecting nine customers, with no fire-weather or PSPS cause identified.
- Uncertainty: Confidence is MEDIUM 69/100 because forecast volatility is HIGH 60/100, and PSPS scoring has no confirmed-event calibration; WATCH is screening, not an official notice.
- Evidence used: overall_status, weather_peaks, official_alerts, forecast_change, lpea_context, fire_posture, active_incidents, calibration
- This interpretation cannot change the deterministic tiers, scores, official alerts, or notification decision.

Changing drivers:
- The first WATCH-or-higher date moved later from Tue, Aug 18 to Mon, Aug 24; today eased from WATCH to ELEVATED, down 22 points.
- Monday worsened from ELEVATED to WATCH, up 28 points, while Sunday rose 22 points but remains ELEVATED.
- Tuesday is the peak: PSPS WATCH 50/100 near Chimney Rock, Red Flag WATCH 61/100 near Ignacio, and fire potential VERY HIGH 71/100 near Chimney Rock.
- Rio Blanco is reported at 100% containment, with no current evacuation order or warning detected; Stage 2 restrictions and VERY HIGH fire danger remain in checked sources.

What to watch next:
- Recheck whether the Monday and Tuesday WATCH signals persist as the forecast window approaches.
- Monitor the official LPEA viewer for outage restoration or cause changes; do not classify these outages as PSPS without official attribution.
- Continue checking official NWS alerts, especially for Monday and Tuesday's dry and breezy windows.
- Continue checking Rio Blanco and official county evacuation sources despite the reported 100% containment.

## Trend Intelligence

- Summary: Momentum is rising versus the prior run (Aug 18 at 5:24 PM MDT); forecast volatility is high and first WATCH-or-higher date is Mon, Aug 24.
- Momentum: **Rising**
- Forecast volatility: **HIGH** (60/100)
- First WATCH-or-higher PSPS date: Mon, Aug 24
- Watch-date movement: First WATCH-or-higher PSPS date moved later from Tue, Aug 18 to Mon, Aug 24.
- Method: compares current forecast evidence against prior local forecast history.

Notable changes:
- First WATCH-or-higher PSPS date moved later from Tue, Aug 18 to Mon, Aug 24.
- Mon, Aug 24: worsening vs prior run; PSPS ELEVATED -> WATCH; score +28, wind +9 mph, RH -1%, red-flag hours 0.
- Wed, Aug 19: easing vs prior run; PSPS WATCH -> ELEVATED; score -22, wind -1 mph, RH -1%, red-flag hours 0. Driver shifted to Chimney Rock / west county.
- Sun, Aug 23: worsening vs prior run; PSPS ELEVATED -> ELEVATED; score +22, wind +8 mph, RH -1%, red-flag hours 0.
- Sat, Aug 22: worsening vs prior run; PSPS LOW -> ELEVATED; score +8, wind +7 mph, RH -1%, red-flag hours 0. Driver shifted to Ignacio / southeast La Plata County.

## Public Analysis Export

- Summary: Highest LPEA PSPS concern is Tue, Aug 25 near Chimney Rock / west county (WATCH 50/100), driven by near-threshold wind/gust signal near 21 mph; very dry RH near 12%; 2 sampled hours are near red-flag thresholds. NIFC reports 1 current wildfire in Archuleta County.
- Trend: Momentum is rising versus the prior run (Aug 18 at 5:24 PM MDT); forecast volatility is high and first WATCH-or-higher date is Mon, Aug 24.
- Confidence: **MEDIUM** (69/100)
- First WATCH-or-higher PSPS date: Mon, Aug 24
- PSPS peak: Tue, Aug 25 near Chimney Rock / west county at WATCH 50/100
- Red Flag peak: Tue, Aug 25 near Ignacio / southeast La Plata County at WATCH 61/100
- Weather fire-potential peak: Tue, Aug 25 near Chimney Rock / west county at VERY HIGH 71/100
- LPEA operational outage context: 3 active outages; 1 planned and 2 unplanned; 9 customers out. No fire-weather or PSPS cause is identified.
- Public JSON: `archuleta_red_flag_monitor/public_analysis_export.json`

What changed:
- First WATCH-or-higher PSPS date moved later from Tue, Aug 18 to Mon, Aug 24.
- Mon, Aug 24: worsening vs prior run; PSPS ELEVATED -> WATCH; score +28, wind +9 mph, RH -1%, red-flag hours 0.
- Wed, Aug 19: easing vs prior run; PSPS WATCH -> ELEVATED; score -22, wind -1 mph, RH -1%, red-flag hours 0. Driver shifted to Chimney Rock / west county.
- Sun, Aug 23: worsening vs prior run; PSPS ELEVATED -> ELEVATED; score +22, wind +8 mph, RH -1%, red-flag hours 0.
- Sat, Aug 22: worsening vs prior run; PSPS LOW -> ELEVATED; score +8, wind +7 mph, RH -1%, red-flag hours 0. Driver shifted to Ignacio / southeast La Plata County.

What to watch next:
- Check whether the largest day-level changes line up with wind/RH movement or public-source context.
- Check whether the LPEA active match is still a broad red-flag banner rather than direct PSPS/outage intent.
- Watch whether the highest-risk locations remain consistent across runs or the driver area is moving.
- If a PSPS occurs, log the confirmed date, location, and source so future hit-rate scoring can improve.

## PSPS Likelihood

- **PSPS means Public Safety Power Shutoff:** a planned, safety-related power shutoff LPEA may use during dangerous fire-weather conditions to reduce wildfire ignition risk. See [LPEA PSPS guidance](https://lpea.coop/psps) and the [LPEA outage center](https://lpea.coop/outage-center); if power is out, also check the [LPEA outage map](https://outage.lpea.coop).
- Overall: **WATCH** - PSPS watch screening is present from forecast thresholds or direct LPEA shutoff language; monitor official LPEA and NWS updates.
- Likely PSPS watch dates: None
- PSPS watch dates: Mon, Aug 24; Tue, Aug 25
- LPEA signal basis: LPEA active/update source contains red-flag, wildfire, or power-interruption language.
- Note: This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

| Date | PSPS likelihood | Driver locations | Weather basis |
| --- | --- | --- | --- |
| Wed, Aug 19 | ELEVATED | Chimney Rock / west county (ELEVATED 32/100); Ignacio / southeast La Plata County (ELEVATED 28/100); Arboles / southwest county (ELEVATED 28/100) | Top weather score 30/100 at Chimney Rock / west county. Weather score 30/100: RH 15%, wind/gust 17 mph, red-flag hours 0, near-threshold hours 0. |
| Thu, Aug 20 | ELEVATED | Durango / La Plata County (ELEVATED 30/100); Arboles / southwest county (ELEVATED 28/100); Chimney Rock / west county (ELEVATED 28/100) | Top weather score 28/100 at Durango / La Plata County. Weather score 28/100: RH 18%, wind/gust 22 mph, red-flag hours 0, near-threshold hours 0. |
| Fri, Aug 21 | ELEVATED | Chimney Rock / west county (ELEVATED 28/100); Arboles / southwest county (ELEVATED 22/100); Ignacio / southeast La Plata County (ELEVATED 20/100) | Top weather score 26/100 at Chimney Rock / west county. Weather score 26/100: RH 15%, wind/gust 17 mph, red-flag hours 0, near-threshold hours 0. |
| Sat, Aug 22 | ELEVATED | Ignacio / southeast La Plata County (ELEVATED 22/100); Chimney Rock / west county (ELEVATED 22/100); Pagosa Springs (ELEVATED 18/100) | Top weather score 22/100 at Ignacio / southeast La Plata County. Weather score 22/100: RH 21%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 0. |
| Sun, Aug 23 | ELEVATED | Arboles / southwest county (ELEVATED 40/100); Chimney Rock / west county (ELEVATED 30/100); Durango / La Plata County (ELEVATED 24/100) | Top weather score 38/100 at Arboles / southwest county. Weather score 38/100: RH 18%, wind/gust 22 mph, red-flag hours 0, near-threshold hours 2. |
| Mon, Aug 24 | WATCH | Arboles / southwest county (WATCH 46/100) | Top weather score 44/100 at Arboles / southwest county. Weather score 44/100: RH 15%, wind/gust 22 mph, red-flag hours 0, near-threshold hours 3. |
| Tue, Aug 25 | WATCH | Chimney Rock / west county (WATCH 50/100); Ignacio / southeast La Plata County (WATCH 48/100); Arboles / southwest county (WATCH 46/100) | Top weather score 48/100 at Chimney Rock / west county. Weather score 48/100: RH 12%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 2. |

## Area-Specific Outlook

| Area | Today | Peak this run | Highest-risk window |
| --- | --- | --- | --- |
| Chimney Rock | ELEVATED 32/100 | Tue, Aug 25: WATCH 50/100 | 3 PM-4 PM local; 2 near/red-flag threshold hours. |
| Ignacio | ELEVATED 28/100 | Tue, Aug 25: WATCH 48/100 | 2 PM-6 PM local; 5 near/red-flag threshold hours. |
| Arboles | ELEVATED 28/100 | Mon, Aug 24: WATCH 46/100 | 3 PM-5 PM local; 3 near/red-flag threshold hours. |
| Durango | ELEVATED 24/100 | Tue, Aug 25: ELEVATED 44/100 | 3 PM-6 PM local; 4 near/red-flag threshold hours. |
| Bayfield | ELEVATED 24/100 | Tue, Aug 25: ELEVATED 44/100 | 3 PM-6 PM local; 4 near/red-flag threshold hours. |
| Pagosa Springs | ELEVATED 26/100 | Tue, Aug 25: ELEVATED 32/100 | 4 PM-4 PM local; 1 near/red-flag threshold hour. |
| Chromo | ELEVATED 22/100 | Tue, Aug 25: ELEVATED 26/100 | Peak ingredients near 4 PM local; RH 17%, wind 17 mph. |
| Piedra | LOW 16/100 | Wed, Aug 19: LOW 16/100 | Peak ingredients near 9 PM local; RH 46%, wind 16 mph. |

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
- WATCH/LIKELY false-watch past days: 59
- Pending WATCH/LIKELY dates in current forecast: Mon, Aug 24; Tue, Aug 25
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
- No active official NWS Red Flag / Fire Weather or related weather alerts found for monitored zones.

## LPEA Power Signal

- Status: `operational_outage_active` - Official LPEA outage data indicates an operational outage; use as grid context, not PSPS/fire evidence unless LPEA identifies that cause.
- Meaning: Active source match means a monitored LPEA active/update source currently contains fire, outage, PSPS, or power-interruption keywords. Operational outages are shown separately and are not treated as PSPS/fire evidence unless the source text says so.
- Operational outage context: 3 active outages; 1 planned and 2 unplanned; 9 customers out. No fire-weather or PSPS cause is identified.
- Source coverage: 13 sources; 5/5 official social sources reachable
- Evidence quality: 0 operational, 4 active/update, 0 archive/context, 6 reference source matches.
- Operational outage source links: [2028 DELWOOD AVE](https://outage.lpea.coop); [1648 COUNTY RD 975](https://outage.lpea.coop); [3649 MAIN AVE](https://outage.lpea.coop)
- Active/update source pages with matches: LPEA homepage (public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation, restoration); LPEA X (power outage, outage map, high winds, restore power); LPEA LinkedIn (wildfire, deenergize, fire mitigation)
- Distinct active/update signals: LPEA X (power outage, outage map, high winds, restore power); LPEA X (power outage, outage map, high winds, restore power); LPEA LinkedIn (wildfire, deenergize, fire mitigation); LPEA LinkedIn (wildfire, deenergize, fire mitigation)
- Example signal: ...ibrary! 1 2 536 LPEA @LaPlataElectric May 7, 2024 LPEA members are experiencing power outages in the Bayfield and Pagosa Springs areas. Approximately 200 meters are out and it is suspected that the high winds are...
- Reference/context hits: [LPEA outage center](https://lpea.coop/outage-center); [LPEA wildfire / public safety power shutoffs](https://lpea.coop/psps); [LPEA red flag outage impact page](https://lpea.coop/outages/red-flag-warnings-and-impact-outages-prioritizing-safety-our-members); [LPEA fire mitigation](https://lpea.coop/fire-mitigation); [LPEA latest news](https://lpea.coop/Posts)

**Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## Next 7 Days

| Date | Tier | Main reason | Worst sampled metrics |
| --- | --- | --- | --- |
| Wed, Aug 19 | ELEVATED | Arboles / southwest county: Elevated ingredient present: very low RH forecast near 14%. | Arboles / southwest county: RH 14%, wind/gust 16 mph, thunder 14%<br>Chimney Rock / west county: RH 15%, wind/gust 17 mph, thunder 30% |
| Thu, Aug 20 | ELEVATED | Arboles / southwest county: Elevated ingredient present: very low RH forecast near 14%. | Arboles / southwest county: RH 14%, wind/gust 15 mph, thunder 33%<br>Chimney Rock / west county: RH 14%, wind/gust 16 mph, thunder 39% |
| Fri, Aug 21 | ELEVATED | Chimney Rock / west county: Elevated ingredient present: very low RH forecast near 15%. | Chimney Rock / west county: RH 15%, wind/gust 17 mph, thunder 43% |
| Sat, Aug 22 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 22%, wind/gust 20 mph, thunder 46%<br>Arboles / southwest county: RH 19%, wind/gust 18 mph, thunder 38%<br>Chimney Rock / west county: RH 17%, wind/gust 18 mph, thunder 32% |
| Sun, Aug 23 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 18%, wind/gust 22 mph, thunder 11% |
| Mon, Aug 24 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 15%, wind/gust 22 mph, thunder 10%<br>Chimney Rock / west county: RH 15%, wind/gust 20 mph, thunder 13%<br>Ignacio / southeast La Plata County: RH 17%, wind/gust 22 mph, thunder 7% |
| Tue, Aug 25 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 13%, wind/gust 22 mph, thunder 7%<br>Chimney Rock / west county: RH 12%, wind/gust 21 mph, thunder 9%<br>Chromo / southeast county: RH 17%, wind/gust 17 mph, thunder 15% |

## Sample Point Status

- Pagosa Springs: COZ295 (matches), forecast zone COZ023, county zone COC007
- Arboles / southwest county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Chimney Rock / west county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Piedra / north county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Chromo / southeast county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Durango / La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Bayfield / east La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Ignacio / southeast La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
