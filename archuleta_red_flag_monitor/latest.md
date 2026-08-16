# Archuleta County fire-weather monitor

Generated: Aug 16, 2026 at 5:29 AM MDT (Pagosa Springs, CO local time)
Next update: Aug 16, 2026 at 5:20 PM MDT (Pagosa Springs, CO local time)
Date/time basis: Pagosa Springs, CO local time (America/Denver)
> **Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## At A Glance

- Fire-weather tier: **CONCERN**
- PSPS likelihood: **WATCH**
- PSPS likely dates: None
- PSPS watch dates: Wed, Aug 19; Thu, Aug 20; Fri, Aug 21; Sat, Aug 22
- Monitor heads-up recommended: **YES** - Send this monitor report because fire-weather screening tier is CONCERN; PSPS screening level is WATCH; a material current wildfire is reported in Archuleta County. This is not an official LPEA or NWS notice.
- HIGH dates: None
- CONCERN dates: Sun, Aug 16; Tue, Aug 18; Wed, Aug 19; Thu, Aug 20; Fri, Aug 21; Sat, Aug 22
- ELEVATED dates: Mon, Aug 17
- Official NWS Red Flag / Fire Weather alerts (COZ295): 0
- LPEA signal: `operational_outage_active` - Official LPEA outage data indicates an operational outage; use as grid context, not PSPS/fire evidence unless LPEA identifies that cause.
- LPEA source coverage: 13 sources; 5/5 official social sources reachable
- Current Archuleta County wildfires: 1
- Official evacuation notices: No current evacuation order or warning detected in the checked official county feeds.
- NWS discussion: NWS discussion contains fire-weather concern language.

## Decision Support

- Summary: Highest LPEA PSPS concern is Wed, Aug 19 near Arboles / southwest county (WATCH 63/100), driven by red-flag wind/gust signal near 25 mph; very dry RH near 12%; 4 sampled hours are near red-flag thresholds. NIFC reports 1 current wildfire in Archuleta County.
- Confidence: **MEDIUM** (69/100) - 8/8 sampled weather points available; 7/7 fire-posture sources reachable; official NWS alert zones checked; 13/13 LPEA public sources reachable; LPEA active/update sources checked; active LPEA operational outage context checked separately from PSPS scoring; authoritative NIFC current-incident feed checked for Archuleta County; official Archuleta County evacuation feeds checked; forecast changed substantially versus prior run; no confirmed PSPS events logged yet for calibration
- Weather fire-potential peak: Wed, Aug 19: Chimney Rock / west county VERY HIGH 73/100
- Red Flag likelihood peak: Wed, Aug 19: Arboles / southwest county WATCH 68/100
- LPEA PSPS peak: Wed, Aug 19: Arboles / southwest county WATCH 63/100
- Method: rules-based decision support using public weather, fire-posture, and LPEA source signals; scores are screening estimates, not official or statistically calibrated probabilities.

| Date | Weather fire potential | Red Flag likelihood | LPEA PSPS | Main window |
| --- | --- | --- | --- | --- |
| Sun, Aug 16 | Durango / La Plata County: HIGH 65/100 | Durango / La Plata County: WATCH 55/100 | Durango / La Plata County: ELEVATED 44/100 | 2 PM-6 PM local; 5 near/red-flag threshold hours. |
| Mon, Aug 17 | Chimney Rock / west county: MODERATE 46/100 | Chimney Rock / west county: LOW 25/100 | Chimney Rock / west county: ELEVATED 28/100 | Peak ingredients near 4 PM local; RH 15%, wind 16 mph. |
| Tue, Aug 18 | Durango / La Plata County: HIGH 62/100 | Durango / La Plata County: POSSIBLE 50/100 | Durango / La Plata County: ELEVATED 40/100 | 4 PM-6 PM local; 3 near/red-flag threshold hours. |
| Wed, Aug 19 | Chimney Rock / west county: VERY HIGH 73/100 | Arboles / southwest county: WATCH 68/100 | Arboles / southwest county: WATCH 63/100 | 3 PM-6 PM local; 4 near/red-flag threshold hours. |
| Thu, Aug 20 | Arboles / southwest county: HIGH 64/100 | Ignacio / southeast La Plata County: WATCH 63/100 | Ignacio / southeast La Plata County: WATCH 52/100 | 3 PM-6 PM local; 4 near/red-flag threshold hours. |
| Fri, Aug 21 | Arboles / southwest county: HIGH 62/100 | Ignacio / southeast La Plata County: WATCH 60/100 | Arboles / southwest county: WATCH 50/100 | 4 PM-5 PM local; 2 near/red-flag threshold hours. |
| Sat, Aug 22 | Arboles / southwest county: HIGH 62/100 | Arboles / southwest county: WATCH 57/100 | Arboles / southwest county: WATCH 50/100 | 4 PM-5 PM local; 2 near/red-flag threshold hours. |

## Analyst Interpretation

- Headline: Weather screening eases to CONCERN and PSPS WATCH shifts to Wednesday; one localized LPEA outage is active near Chromo with no fire or PSPS cause identified.
- Summary: The first PSPS WATCH date moved later from Saturday to Wednesday as Sunday and Tuesday eased to ELEVATED. Wednesday remains the peak near Arboles at PSPS WATCH 63/100 and Red Flag WATCH 68/100; official checks show zero COZ295 alerts. LPEA lists one unplanned outage affecting one customer near Chromo, but no fire-weather or PSPS cause is identified.
- Uncertainty: This remains a screening estimate with MEDIUM 69/100 confidence and HIGH forecast volatility; no confirmed LPEA PSPS events are logged, and 57 prior WATCH or LIKELY dates did not become confirmed events.
- Evidence used: overall_status, weather_peaks, official_alerts, forecast_change, lpea_context, fire_posture, active_incidents, calibration
- This interpretation cannot change the deterministic tiers, scores, official alerts, or notification decision.

Changing drivers:
- The overall fire-weather tier eased from HIGH to CONCERN, and the first PSPS WATCH date moved later from Saturday to Wednesday.
- Sunday and Tuesday both eased from PSPS WATCH to ELEVATED, with scores down 6 and 10 points respectively.
- Wednesday remains the peak near Arboles at PSPS WATCH 63/100 and Red Flag WATCH 68/100, with RH near 12% and wind near 25 mph.
- LPEA reports one localized unplanned outage near Chromo affecting one customer; no fire-weather or PSPS cause is identified.

What to watch next:
- Recheck the localized Chromo outage for restoration or any posted cause; do not treat it as PSPS evidence without official attribution.
- Monitor Wednesday's 3 PM-6 PM Arboles window for changes in wind, humidity, and near-threshold duration.
- Check for an official NWS alert or direct LPEA PSPS notice before escalating the screening estimate.
- Continue checking Rio Blanco and county evacuation feeds for operational changes.

## Trend Intelligence

- Summary: Momentum is easing versus the prior run (Aug 15 at 5:39 PM MDT); forecast volatility is high and first WATCH-or-higher date is Wed, Aug 19.
- Momentum: **Easing**
- Forecast volatility: **HIGH** (32/100)
- First WATCH-or-higher PSPS date: Wed, Aug 19
- Watch-date movement: First WATCH-or-higher PSPS date moved later from Sat, Aug 15 to Wed, Aug 19.
- Method: compares current forecast evidence against prior local forecast history.

Notable changes:
- First WATCH-or-higher PSPS date moved later from Sat, Aug 15 to Wed, Aug 19.
- Tue, Aug 18: easing vs prior run; PSPS WATCH -> ELEVATED; score -10, wind -1 mph, RH 0%, red-flag hours 0. Driver shifted to Durango / La Plata County.
- Sun, Aug 16: easing vs prior run; PSPS WATCH -> ELEVATED; score -6, wind 0 mph, RH 0%, red-flag hours 0. Driver shifted to Ignacio / southeast La Plata County.

## Public Analysis Export

- Summary: Highest LPEA PSPS concern is Wed, Aug 19 near Arboles / southwest county (WATCH 63/100), driven by red-flag wind/gust signal near 25 mph; very dry RH near 12%; 4 sampled hours are near red-flag thresholds. NIFC reports 1 current wildfire in Archuleta County.
- Trend: Momentum is easing versus the prior run (Aug 15 at 5:39 PM MDT); forecast volatility is high and first WATCH-or-higher date is Wed, Aug 19.
- Confidence: **MEDIUM** (69/100)
- First WATCH-or-higher PSPS date: Wed, Aug 19
- PSPS peak: Wed, Aug 19 near Arboles / southwest county at WATCH 63/100
- Red Flag peak: Wed, Aug 19 near Arboles / southwest county at WATCH 68/100
- Weather fire-potential peak: Wed, Aug 19 near Chimney Rock / west county at VERY HIGH 73/100
- LPEA operational outage context: 1 active outage; 0 planned and 1 unplanned; 1 customer out. No fire-weather or PSPS cause is identified.
- Public JSON: `archuleta_red_flag_monitor/public_analysis_export.json`

What changed:
- First WATCH-or-higher PSPS date moved later from Sat, Aug 15 to Wed, Aug 19.
- Tue, Aug 18: easing vs prior run; PSPS WATCH -> ELEVATED; score -10, wind -1 mph, RH 0%, red-flag hours 0. Driver shifted to Durango / La Plata County.
- Sun, Aug 16: easing vs prior run; PSPS WATCH -> ELEVATED; score -6, wind 0 mph, RH 0%, red-flag hours 0. Driver shifted to Ignacio / southeast La Plata County.

What to watch next:
- Check whether the largest day-level changes line up with wind/RH movement or public-source context.
- Check whether the LPEA active match is still a broad red-flag banner rather than direct PSPS/outage intent.
- Watch whether the highest-risk locations remain consistent across runs or the driver area is moving.
- If a PSPS occurs, log the confirmed date, location, and source so future hit-rate scoring can improve.

## PSPS Likelihood

- **PSPS means Public Safety Power Shutoff:** a planned, safety-related power shutoff LPEA may use during dangerous fire-weather conditions to reduce wildfire ignition risk. See [LPEA PSPS guidance](https://lpea.coop/psps) and the [LPEA outage center](https://lpea.coop/outage-center); if power is out, also check the [LPEA outage map](https://outage.lpea.coop).
- Overall: **WATCH** - PSPS watch screening is present from forecast thresholds or direct LPEA shutoff language; monitor official LPEA and NWS updates.
- Likely PSPS watch dates: None
- PSPS watch dates: Wed, Aug 19; Thu, Aug 20; Fri, Aug 21; Sat, Aug 22
- LPEA signal basis: LPEA active/update source contains red-flag, wildfire, or power-interruption language.
- Note: This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

| Date | PSPS likelihood | Driver locations | Weather basis |
| --- | --- | --- | --- |
| Sun, Aug 16 | ELEVATED | Ignacio / southeast La Plata County (ELEVATED 44/100); Durango / La Plata County (ELEVATED 44/100); Bayfield / east La Plata County (ELEVATED 40/100) | Top weather score 44/100 at Ignacio / southeast La Plata County. Weather score 44/100: RH 15%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 2. |
| Mon, Aug 17 | ELEVATED | Chimney Rock / west county (ELEVATED 28/100); Ignacio / southeast La Plata County (ELEVATED 20/100); Arboles / southwest county (ELEVATED 20/100) | Top weather score 26/100 at Chimney Rock / west county. Weather score 26/100: RH 15%, wind/gust 16 mph, red-flag hours 0, near-threshold hours 0. |
| Tue, Aug 18 | ELEVATED | Durango / La Plata County (ELEVATED 40/100); Ignacio / southeast La Plata County (ELEVATED 38/100); Arboles / southwest county (ELEVATED 36/100) | Top weather score 38/100 at Durango / La Plata County. Weather score 38/100: RH 18%, wind/gust 22 mph, red-flag hours 0, near-threshold hours 3. |
| Wed, Aug 19 | WATCH | Arboles / southwest county (WATCH 63/100); Ignacio / southeast La Plata County (WATCH 57/100); Durango / La Plata County (WATCH 53/100); Chimney Rock / west county (WATCH 50/100) | Top weather score 61/100 at Arboles / southwest county. Weather score 61/100: RH 12%, wind/gust 25 mph, red-flag hours 2, near-threshold hours 4. |
| Thu, Aug 20 | WATCH | Ignacio / southeast La Plata County (WATCH 52/100); Arboles / southwest county (WATCH 50/100) | Top weather score 52/100 at Ignacio / southeast La Plata County. Weather score 52/100: RH 15%, wind/gust 23 mph, red-flag hours 0, near-threshold hours 4. |
| Fri, Aug 21 | WATCH | Arboles / southwest county (WATCH 50/100); Ignacio / southeast La Plata County (WATCH 48/100) | Top weather score 48/100 at Arboles / southwest county. Weather score 48/100: RH 13%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 2. |
| Sat, Aug 22 | WATCH | Arboles / southwest county (WATCH 50/100) | Top weather score 48/100 at Arboles / southwest county. Weather score 48/100: RH 15%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 2. |

## Area-Specific Outlook

| Area | Today | Peak this run | Highest-risk window |
| --- | --- | --- | --- |
| Arboles | ELEVATED 32/100 | Wed, Aug 19: WATCH 63/100 | 3 PM-6 PM local; 4 near/red-flag threshold hours. |
| Ignacio | ELEVATED 44/100 | Wed, Aug 19: WATCH 57/100 | 2 PM-6 PM local; 5 near/red-flag threshold hours. |
| Durango | ELEVATED 44/100 | Wed, Aug 19: WATCH 53/100 | 3 PM-6 PM local; 4 near/red-flag threshold hours. |
| Chimney Rock | ELEVATED 32/100 | Wed, Aug 19: WATCH 50/100 | 3 PM-5 PM local; 3 near/red-flag threshold hours. |
| Bayfield | ELEVATED 40/100 | Wed, Aug 19: ELEVATED 44/100 | 3 PM-6 PM local; 4 near/red-flag threshold hours. |
| Pagosa Springs | ELEVATED 24/100 | Wed, Aug 19: ELEVATED 42/100 | 3 PM-4 PM local; 2 near/red-flag threshold hours. |
| Chromo | ELEVATED 22/100 | Thu, Aug 20: ELEVATED 26/100 | Peak ingredients near 3 PM local; RH 18%, wind 16 mph. |
| Piedra | ELEVATED 22/100 | Sun, Aug 16: ELEVATED 22/100 | Peak ingredients near 3 PM local; RH 18%, wind 17 mph. |

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
- WATCH/LIKELY false-watch past days: 57
- Pending WATCH/LIKELY dates in current forecast: Wed, Aug 19; Thu, Aug 20; Fri, Aug 21; Sat, Aug 22
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
- Operational outage context: 1 active outage; 0 planned and 1 unplanned; 1 customer out. No fire-weather or PSPS cause is identified.
- Source coverage: 13 sources; 5/5 official social sources reachable
- Evidence quality: 0 operational, 4 active/update, 0 archive/context, 6 reference source matches.
- Operational outage source links: [740 COUNTY RD 382](https://outage.lpea.coop)
- Active/update source pages with matches: LPEA homepage (public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation, restoration); LPEA X (power outage, outage map, high winds, restore power); LPEA LinkedIn (wildfire, fire mitigation)
- Distinct active/update signals: LPEA X (power outage, outage map, high winds, restore power); LPEA X (power outage, outage map, high winds, restore power); LPEA LinkedIn (wildfire, fire mitigation); LPEA LinkedIn (wildfire, fire mitigation)
- Example signal: ...ibrary! 1 2 522 LPEA @LaPlataElectric May 7, 2024 LPEA members are experiencing power outages in the Bayfield and Pagosa Springs areas. Approximately 200 meters are out and it is suspected that the high winds are...
- Reference/context hits: [LPEA outage center](https://lpea.coop/outage-center); [LPEA wildfire / public safety power shutoffs](https://lpea.coop/psps); [LPEA red flag outage impact page](https://lpea.coop/outages/red-flag-warnings-and-impact-outages-prioritizing-safety-our-members); [LPEA fire mitigation](https://lpea.coop/fire-mitigation); [LPEA latest news](https://lpea.coop/Posts)

**Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## Next 7 Days

| Date | Tier | Main reason | Worst sampled metrics |
| --- | --- | --- | --- |
| Sun, Aug 16 | CONCERN | Durango / La Plata County: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 12%, wind/gust 18 mph, thunder 2%<br>Chimney Rock / west county: RH 11%, wind/gust 18 mph, thunder 3%<br>Durango / La Plata County: RH 16%, wind/gust 23 mph, thunder 2% |
| Mon, Aug 17 | ELEVATED | Arboles / southwest county: Elevated ingredient present: very low RH forecast near 15%. | Arboles / southwest county: RH 15%, wind/gust 14 mph, thunder 7%<br>Chimney Rock / west county: RH 15%, wind/gust 16 mph, thunder 6% |
| Tue, Aug 18 | CONCERN | Durango / La Plata County: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 14%, wind/gust 21 mph, thunder 1%<br>Chimney Rock / west county: RH 14%, wind/gust 20 mph, thunder 2%<br>Durango / La Plata County: RH 18%, wind/gust 22 mph, thunder 2% |
| Wed, Aug 19 | CONCERN | Pagosa Springs: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Pagosa Springs: RH 18%, wind/gust 21 mph, thunder 7%<br>Arboles / southwest county: RH 12%, wind/gust 25 mph, thunder 5%<br>Chimney Rock / west county: RH 12%, wind/gust 22 mph, thunder 5% |
| Thu, Aug 20 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 13%, wind/gust 22 mph, thunder 17%<br>Chimney Rock / west county: RH 13%, wind/gust 20 mph, thunder 21%<br>Chromo / southeast county: RH 18%, wind/gust 16 mph, thunder 19% |
| Fri, Aug 21 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 13%, wind/gust 21 mph, thunder 27%<br>Chimney Rock / west county: RH 13%, wind/gust 18 mph, thunder 27%<br>Durango / La Plata County: RH 17%, wind/gust 22 mph, thunder 29% |
| Sat, Aug 22 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 15%, wind/gust 21 mph, thunder 37%<br>Chimney Rock / west county: RH 14%, wind/gust 20 mph, thunder 37%<br>Ignacio / southeast La Plata County: RH 17%, wind/gust 21 mph, thunder 37% |

## Sample Point Status

- Pagosa Springs: COZ295 (matches), forecast zone COZ023, county zone COC007
- Arboles / southwest county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Chimney Rock / west county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Piedra / north county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Chromo / southeast county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Durango / La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Bayfield / east La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Ignacio / southeast La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
