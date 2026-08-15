# Archuleta County fire-weather monitor

Generated: Aug 15, 2026 at 5:39 PM MDT (Pagosa Springs, CO local time)
Next update: Aug 16, 2026 at 5:20 AM MDT (Pagosa Springs, CO local time)
Date/time basis: Pagosa Springs, CO local time (America/Denver)
> **Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## At A Glance

- Fire-weather tier: **HIGH**
- PSPS likelihood: **WATCH**
- PSPS likely dates: None
- PSPS watch dates: Sat, Aug 15; Sun, Aug 16; Tue, Aug 18; Wed, Aug 19; Thu, Aug 20; Fri, Aug 21
- Monitor heads-up recommended: **YES** - Send this monitor report because fire-weather screening tier is HIGH; PSPS screening level is WATCH; a material current wildfire is reported in Archuleta County. This is not an official LPEA or NWS notice.
- HIGH dates: Wed, Aug 19
- CONCERN dates: Sat, Aug 15; Sun, Aug 16; Tue, Aug 18; Thu, Aug 20; Fri, Aug 21
- ELEVATED dates: Mon, Aug 17
- Official NWS Red Flag / Fire Weather alerts (COZ295): 0
- LPEA signal: `active_keyword_match` - LPEA active/update sources contained power-interruption keywords; review source before treating as confirmed outage intent.
- LPEA source coverage: 13 sources; 5/5 official social sources reachable
- Current Archuleta County wildfires: 1
- Official evacuation notices: No current evacuation order or warning detected in the checked official county feeds.
- NWS discussion: No concerning fire-weather language found in latest GJT discussion.

## Decision Support

- Summary: Highest LPEA PSPS concern is Wed, Aug 19 near Ignacio / southeast La Plata County (WATCH 63/100), driven by red-flag wind/gust signal near 26 mph; red-flag RH near 15%; 3 sampled hours meet red-flag screen. NIFC reports 1 current wildfire in Archuleta County.
- Confidence: **MEDIUM** (69/100) - 8/8 sampled weather points available; 7/7 fire-posture sources reachable; official NWS alert zones checked; 13/13 LPEA public sources reachable; LPEA active/update sources checked; authoritative NIFC current-incident feed checked for Archuleta County; official Archuleta County evacuation feeds checked; forecast changed substantially versus prior run; no confirmed PSPS events logged yet for calibration
- Weather fire-potential peak: Wed, Aug 19: Durango / La Plata County VERY HIGH 80/100
- Red Flag likelihood peak: Wed, Aug 19: Ignacio / southeast La Plata County LIKELY 78/100
- LPEA PSPS peak: Wed, Aug 19: Ignacio / southeast La Plata County WATCH 63/100
- Method: rules-based decision support using public weather, fire-posture, and LPEA source signals; scores are screening estimates, not official or statistically calibrated probabilities.

| Date | Weather fire potential | Red Flag likelihood | LPEA PSPS | Main window |
| --- | --- | --- | --- | --- |
| Sat, Aug 15 | Chimney Rock / west county: HIGH 69/100 | Arboles / southwest county: WATCH 61/100 | Arboles / southwest county: WATCH 55/100 | 5 PM-7 PM local; 3 near/red-flag threshold hours. |
| Sun, Aug 16 | Bayfield / east La Plata County: VERY HIGH 73/100 | Arboles / southwest county: WATCH 58/100 | Arboles / southwest county: WATCH 50/100 | 3 PM-6 PM local; 4 near/red-flag threshold hours. |
| Mon, Aug 17 | Chimney Rock / west county: MODERATE 46/100 | Chimney Rock / west county: LOW 25/100 | Chimney Rock / west county: ELEVATED 28/100 | Peak ingredients near 4 PM local; RH 14%, wind 18 mph. |
| Tue, Aug 18 | Chimney Rock / west county: HIGH 69/100 | Arboles / southwest county: WATCH 58/100 | Arboles / southwest county: WATCH 50/100 | 3 PM-6 PM local; 4 near/red-flag threshold hours. |
| Wed, Aug 19 | Durango / La Plata County: VERY HIGH 80/100 | Ignacio / southeast La Plata County: LIKELY 78/100 | Ignacio / southeast La Plata County: WATCH 63/100 | 2 PM-7 PM local; 6 near/red-flag threshold hours. |
| Thu, Aug 20 | Bayfield / east La Plata County: HIGH 66/100 | Ignacio / southeast La Plata County: WATCH 66/100 | Ignacio / southeast La Plata County: WATCH 52/100 | 2 PM-6 PM local; 5 near/red-flag threshold hours. |
| Fri, Aug 21 | Ignacio / southeast La Plata County: HIGH 55/100 | Ignacio / southeast La Plata County: WATCH 57/100 | Ignacio / southeast La Plata County: WATCH 48/100 | 4 PM-5 PM local; 2 near/red-flag threshold hours. |

## Analyst Interpretation

- Headline: Fire-weather screening remains HIGH as PSPS WATCH moves to today; Wednesday remains the peak, with no official COZ295 alert or active LPEA outage.
- Summary: Today's Arboles screen worsened from ELEVATED to WATCH 55/100, moving first WATCH-or-higher timing from Sunday to Saturday. Wednesday remains the peak near Ignacio at PSPS WATCH 63/100 and Red Flag LIKELY 78/100; official checks show zero COZ295 alerts, no active LPEA outage, and no county evacuation notice. Rio Blanco remains about 1,388 acres and 97% contained.
- Uncertainty: This is a screening estimate with MEDIUM 69/100 confidence and HIGH forecast volatility; no confirmed LPEA PSPS events are logged, and 56 prior WATCH or LIKELY dates did not become confirmed events.
- Evidence used: overall_status, weather_peaks, official_alerts, forecast_change, lpea_context, fire_posture, active_incidents, calibration
- This interpretation cannot change the deterministic tiers, scores, official alerts, or notification decision.

Changing drivers:
- Saturday worsened from PSPS ELEVATED to WATCH 55/100 as RH fell 2 points, wind rose about 1 mph, and one sampled hour met the red-flag screen.
- The first WATCH-or-higher PSPS date moved earlier from Sunday to Saturday.
- Wednesday remains the peak near Ignacio at PSPS WATCH 63/100 and Red Flag LIKELY 78/100, with a 2 PM-7 PM risk window.
- Official-source fire posture remains Stage 2 with VERY HIGH fire danger; one wildfire remains listed and no evacuation notice was detected.

What to watch next:
- Recheck conditions at the next update Sunday morning for any official NWS or LPEA escalation.
- Monitor Wednesday's 2 PM-7 PM Ignacio window for changes in wind, humidity, and red-flag duration.
- Treat the LPEA keyword match as broad public-source context unless direct outage or PSPS intent appears.
- Continue checking Rio Blanco and county evacuation feeds for operational changes.

## Trend Intelligence

- Summary: Momentum is rising versus the prior run (Aug 15 at 5:27 AM MDT); forecast volatility is high and first WATCH-or-higher date is Sat, Aug 15.
- Momentum: **Rising**
- Forecast volatility: **HIGH** (37/100)
- First WATCH-or-higher PSPS date: Sat, Aug 15
- Watch-date movement: First WATCH-or-higher PSPS date moved earlier from Sun, Aug 16 to Sat, Aug 15.
- Method: compares current forecast evidence against prior local forecast history.

Notable changes:
- First WATCH-or-higher PSPS date moved earlier from Sun, Aug 16 to Sat, Aug 15.
- Sat, Aug 15: worsening vs prior run; PSPS ELEVATED -> WATCH; score +15, wind +1 mph, RH -2%, red-flag hours +1.
- Mon, Aug 17: worsening vs prior run; PSPS ELEVATED -> ELEVATED; score +6, wind 0 mph, RH -4%, red-flag hours 0.

## Public Analysis Export

- Summary: Highest LPEA PSPS concern is Wed, Aug 19 near Ignacio / southeast La Plata County (WATCH 63/100), driven by red-flag wind/gust signal near 26 mph; red-flag RH near 15%; 3 sampled hours meet red-flag screen. NIFC reports 1 current wildfire in Archuleta County.
- Trend: Momentum is rising versus the prior run (Aug 15 at 5:27 AM MDT); forecast volatility is high and first WATCH-or-higher date is Sat, Aug 15.
- Confidence: **MEDIUM** (69/100)
- First WATCH-or-higher PSPS date: Sat, Aug 15
- PSPS peak: Wed, Aug 19 near Ignacio / southeast La Plata County at WATCH 63/100
- Red Flag peak: Wed, Aug 19 near Ignacio / southeast La Plata County at LIKELY 78/100
- Weather fire-potential peak: Wed, Aug 19 near Durango / La Plata County at VERY HIGH 80/100
- LPEA operational outage context: No active outages are listed by the official LPEA outage viewer.
- Public JSON: `archuleta_red_flag_monitor/public_analysis_export.json`

What changed:
- First WATCH-or-higher PSPS date moved earlier from Sun, Aug 16 to Sat, Aug 15.
- Sat, Aug 15: worsening vs prior run; PSPS ELEVATED -> WATCH; score +15, wind +1 mph, RH -2%, red-flag hours +1.
- Mon, Aug 17: worsening vs prior run; PSPS ELEVATED -> ELEVATED; score +6, wind 0 mph, RH -4%, red-flag hours 0.

What to watch next:
- Check whether the largest day-level changes line up with wind/RH movement or public-source context.
- Check whether the LPEA active match is still a broad red-flag banner rather than direct PSPS/outage intent.
- Watch whether the highest-risk locations remain consistent across runs or the driver area is moving.
- If a PSPS occurs, log the confirmed date, location, and source so future hit-rate scoring can improve.

## PSPS Likelihood

- **PSPS means Public Safety Power Shutoff:** a planned, safety-related power shutoff LPEA may use during dangerous fire-weather conditions to reduce wildfire ignition risk. See [LPEA PSPS guidance](https://lpea.coop/psps) and the [LPEA outage center](https://lpea.coop/outage-center); if power is out, also check the [LPEA outage map](https://outage.lpea.coop).
- Overall: **WATCH** - PSPS watch screening is present from forecast thresholds or direct LPEA shutoff language; monitor official LPEA and NWS updates.
- Likely PSPS watch dates: None
- PSPS watch dates: Sat, Aug 15; Sun, Aug 16; Tue, Aug 18; Wed, Aug 19; Thu, Aug 20; Fri, Aug 21
- LPEA signal basis: LPEA active/update source contains red-flag, wildfire, or power-interruption language.
- Note: This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

| Date | PSPS likelihood | Driver locations | Weather basis |
| --- | --- | --- | --- |
| Sat, Aug 15 | WATCH | Arboles / southwest county (WATCH 55/100); Chimney Rock / west county (WATCH 46/100) | Top weather score 53/100 at Arboles / southwest county. Weather score 53/100: RH 15%, wind/gust 25 mph, red-flag hours 1, near-threshold hours 3. |
| Sun, Aug 16 | WATCH | Arboles / southwest county (WATCH 50/100); Chimney Rock / west county (WATCH 50/100); Bayfield / east La Plata County (WATCH 50/100); Ignacio / southeast La Plata County (WATCH 48/100) | Top weather score 48/100 at Arboles / southwest county. Weather score 48/100: RH 13%, wind/gust 22 mph, red-flag hours 0, near-threshold hours 4. |
| Mon, Aug 17 | ELEVATED | Chimney Rock / west county (ELEVATED 28/100); Arboles / southwest county (ELEVATED 22/100); Ignacio / southeast La Plata County (ELEVATED 20/100) | Top weather score 26/100 at Chimney Rock / west county. Weather score 26/100: RH 14%, wind/gust 18 mph, red-flag hours 0, near-threshold hours 0. |
| Tue, Aug 18 | WATCH | Arboles / southwest county (WATCH 50/100); Chimney Rock / west county (WATCH 46/100) | Top weather score 48/100 at Arboles / southwest county. Weather score 48/100: RH 15%, wind/gust 23 mph, red-flag hours 0, near-threshold hours 4. |
| Wed, Aug 19 | WATCH | Ignacio / southeast La Plata County (WATCH 63/100); Arboles / southwest county (WATCH 59/100); Durango / La Plata County (WATCH 59/100); Chimney Rock / west county (WATCH 50/100) | Top weather score 63/100 at Ignacio / southeast La Plata County. Weather score 63/100: RH 15%, wind/gust 26 mph, red-flag hours 3, near-threshold hours 6. |
| Thu, Aug 20 | WATCH | Ignacio / southeast La Plata County (WATCH 52/100); Arboles / southwest county (WATCH 50/100); Bayfield / east La Plata County (WATCH 48/100) | Top weather score 52/100 at Ignacio / southeast La Plata County. Weather score 52/100: RH 15%, wind/gust 23 mph, red-flag hours 0, near-threshold hours 5. |
| Fri, Aug 21 | WATCH | Ignacio / southeast La Plata County (WATCH 48/100) | Top weather score 48/100 at Ignacio / southeast La Plata County. Weather score 48/100: RH 15%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 2. |

## Area-Specific Outlook

| Area | Today | Peak this run | Highest-risk window |
| --- | --- | --- | --- |
| Ignacio | ELEVATED 37/100 | Wed, Aug 19: WATCH 63/100 | 2 PM-7 PM local; 6 near/red-flag threshold hours. |
| Arboles | WATCH 55/100 | Wed, Aug 19: WATCH 59/100 | 2 PM-7 PM local; 6 near/red-flag threshold hours. |
| Durango | ELEVATED 40/100 | Wed, Aug 19: WATCH 59/100 | 2 PM-7 PM local; 6 near/red-flag threshold hours. |
| Chimney Rock | WATCH 46/100 | Sun, Aug 16: WATCH 50/100 | 4 PM-5 PM local; 2 near/red-flag threshold hours. |
| Bayfield | ELEVATED 39/100 | Sun, Aug 16: WATCH 50/100 | 3 PM-6 PM local; 4 near/red-flag threshold hours. |
| Pagosa Springs | ELEVATED 26/100 | Wed, Aug 19: ELEVATED 32/100 | 4 PM-4 PM local; 1 near/red-flag threshold hour. |
| Chromo | LOW 16/100 | Thu, Aug 20: ELEVATED 26/100 | Peak ingredients near 3 PM local; RH 17%, wind 17 mph. |
| Piedra | LOW 16/100 | Sun, Aug 16: ELEVATED 22/100 | Peak ingredients near 3 PM local; RH 17%, wind 17 mph. |

## Current Fires + Evacuations

- Incident summary: 1 current wildfire reported in Archuleta County; no current evacuation notice detected in checked county feeds.
- Evacuation status: **NONE DETECTED** - No current evacuation order or warning detected in the checked official county feeds.
- Safety note: Current incidents and evacuation notices are operational context. They do not raise PSPS scores by themselves; follow official evacuation instructions immediately.

### Current NIFC Incidents

| Incident | Type | Size | Containment | Nearest monitored area | Updated |
| --- | --- | --- | --- | --- | --- |
| Rio Blanco | Wildfire | 1,387.74 acres | 97% | Chromo / southeast county (9.9 mi) | Aug 13 at 4:30 PM MDT |

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
- WATCH/LIKELY false-watch past days: 56
- Pending WATCH/LIKELY dates in current forecast: Sat, Aug 15; Sun, Aug 16; Tue, Aug 18; Wed, Aug 19; Thu, Aug 20; Fri, Aug 21
- Calibration source: manual PSPS event log plus forecast history from prior monitor runs.

### Red Flag / Fire Weather Calibration

- Summary: 3/3 official Red Flag / Fire Weather episodes had a pre-alert HIGH monitor signal; date-level result was 21/21. Episode-average lead time: 3.5 days.
- Official alert episodes logged: 3 (21 alert dates)
- Episode-level pre-alert HIGH hit rate: 100%
- Date-level pre-alert HIGH hit rate: 100%
- Episode-level average lead time: 3.5 days
- HIGH false-watch past days: 20
- Pending HIGH dates in current forecast: Wed, Aug 19
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
- Example signal: ...ibrary! 1 2 522 LPEA @LaPlataElectric May 7, 2024 LPEA members are experiencing power outages in the Bayfield and Pagosa Springs areas. Approximately 200 meters are out and it is suspected that the high winds are...
- Reference/context hits: [LPEA outage center](https://lpea.coop/outage-center); [LPEA wildfire / public safety power shutoffs](https://lpea.coop/psps); [LPEA red flag outage impact page](https://lpea.coop/outages/red-flag-warnings-and-impact-outages-prioritizing-safety-our-members); [LPEA fire mitigation](https://lpea.coop/fire-mitigation); [LPEA latest news](https://lpea.coop/Posts)

**Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## Next 7 Days

| Date | Tier | Main reason | Worst sampled metrics |
| --- | --- | --- | --- |
| Sat, Aug 15 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 15%, wind/gust 25 mph, thunder 3%<br>Chimney Rock / west county: RH 14%, wind/gust 22 mph, thunder 3%<br>Durango / La Plata County: RH 18%, wind/gust 24 mph, thunder 6% |
| Sun, Aug 16 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 13%, wind/gust 22 mph, thunder 2%<br>Chimney Rock / west county: RH 11%, wind/gust 21 mph, thunder 3%<br>Durango / La Plata County: RH 16%, wind/gust 22 mph, thunder 2% |
| Mon, Aug 17 | ELEVATED | Chimney Rock / west county: Elevated ingredient present: very low RH forecast near 14%. | Chimney Rock / west county: RH 14%, wind/gust 18 mph, thunder 7% |
| Tue, Aug 18 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 15%, wind/gust 23 mph, thunder 0%<br>Chimney Rock / west county: RH 14%, wind/gust 21 mph, thunder 1%<br>Durango / La Plata County: RH 17%, wind/gust 23 mph, thunder 3% |
| Wed, Aug 19 | HIGH | Ignacio / southeast La Plata County: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Arboles / southwest county: RH 13%, wind/gust 25 mph, thunder 4%<br>Chimney Rock / west county: RH 12%, wind/gust 21 mph, thunder 5%<br>Durango / La Plata County: RH 15%, wind/gust 25 mph, thunder 5% |
| Thu, Aug 20 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Pagosa Springs: RH 18%, wind/gust 18 mph, thunder 18%<br>Arboles / southwest county: RH 13%, wind/gust 22 mph, thunder 18%<br>Chimney Rock / west county: RH 12%, wind/gust 20 mph, thunder 17% |
| Fri, Aug 21 | CONCERN | Ignacio / southeast La Plata County: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 13%, wind/gust 20 mph, thunder 30%<br>Chimney Rock / west county: RH 12%, wind/gust 17 mph, thunder 28%<br>Bayfield / east La Plata County: RH 16%, wind/gust 20 mph, thunder 27% |

## Sample Point Status

- Pagosa Springs: COZ295 (matches), forecast zone COZ023, county zone COC007
- Arboles / southwest county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Chimney Rock / west county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Piedra / north county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Chromo / southeast county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Durango / La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Bayfield / east La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Ignacio / southeast La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
