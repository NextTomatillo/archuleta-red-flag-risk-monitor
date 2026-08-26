# Archuleta County fire-weather monitor

Generated: Aug 25, 2026 at 6:53 PM MDT (Pagosa Springs, CO local time)
Next update: Aug 26, 2026 at 5:20 AM MDT (Pagosa Springs, CO local time)
Date/time basis: Pagosa Springs, CO local time (America/Denver)
> **Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## At A Glance

- Fire-weather tier: **CONCERN**
- PSPS likelihood: **WATCH**
- PSPS likely dates: None
- PSPS watch dates: Fri, Aug 28; Sat, Aug 29
- Monitor heads-up recommended: **YES** - Send this monitor report because fire-weather screening tier is CONCERN; PSPS screening level is WATCH; a material official LPEA operational outage is active. This is not an official LPEA or NWS notice.
- HIGH dates: None
- CONCERN dates: Wed, Aug 26; Fri, Aug 28; Sat, Aug 29
- ELEVATED dates: Thu, Aug 27; Sun, Aug 30
- Official NWS Red Flag / Fire Weather alerts (COZ295): 0
- LPEA signal: `operational_outage_active` - Official LPEA outage data indicates an operational outage; use as grid context, not PSPS/fire evidence unless LPEA identifies that cause.
- LPEA source coverage: 13 sources; 4/5 official social sources reachable
- Current Archuleta County wildfires: 1
- Official evacuation notices: No current evacuation order or warning detected in the checked official county feeds.
- NWS discussion: NWS discussion contains fire-weather concern language.

## Decision Support

- Summary: Highest LPEA PSPS concern is Sat, Aug 29 near Chimney Rock / west county (WATCH 63/100), driven by red-flag wind/gust signal near 25 mph; red-flag RH near 15%; 5 sampled hours are near red-flag thresholds. NIFC reports 1 current wildfire in Archuleta County.
- Confidence: **MEDIUM** (69/100) - 8/8 sampled weather points available; 7/7 fire-posture sources reachable; official NWS alert zones checked; 12/13 LPEA public sources reachable; LPEA active/update sources checked; active LPEA operational outage context checked separately from PSPS scoring; authoritative NIFC current-incident feed checked for Archuleta County; official Archuleta County evacuation feeds checked; forecast changed substantially versus prior run; no confirmed PSPS events logged yet for calibration
- Weather fire-potential peak: Sat, Aug 29: Chimney Rock / west county VERY HIGH 81/100
- Red Flag likelihood peak: Sat, Aug 29: Chimney Rock / west county WATCH 72/100
- LPEA PSPS peak: Sat, Aug 29: Chimney Rock / west county WATCH 63/100
- Method: rules-based decision support using public weather, fire-posture, and LPEA source signals; scores are screening estimates, not official or statistically calibrated probabilities.

| Date | Weather fire potential | Red Flag likelihood | LPEA PSPS | Main window |
| --- | --- | --- | --- | --- |
| Tue, Aug 25 | Chimney Rock / west county: LOW 26/100 | Ignacio / southeast La Plata County: LOW 8/100 | Ignacio / southeast La Plata County: ELEVATED 22/100 | Peak ingredients near 6 PM local; RH 22%, wind 21 mph. |
| Wed, Aug 26 | Chimney Rock / west county: HIGH 69/100 | Arboles / southwest county: POSSIBLE 50/100 | Arboles / southwest county: ELEVATED 40/100 | 3 PM-5 PM local; 3 near/red-flag threshold hours. |
| Thu, Aug 27 | Chimney Rock / west county: MODERATE 40/100 | Chimney Rock / west county: LOW 25/100 | Arboles / southwest county: ELEVATED 30/100 | 4 PM-4 PM local; 1 near/red-flag threshold hour. |
| Fri, Aug 28 | Chimney Rock / west county: HIGH 69/100 | Arboles / southwest county: WATCH 58/100 | Arboles / southwest county: WATCH 50/100 | 3 PM-6 PM local; 4 near/red-flag threshold hours. |
| Sat, Aug 29 | Chimney Rock / west county: VERY HIGH 81/100 | Chimney Rock / west county: WATCH 72/100 | Chimney Rock / west county: WATCH 63/100 | 2 PM-6 PM local; 5 near/red-flag threshold hours. |
| Sun, Aug 30 | Bayfield / east La Plata County: MODERATE 39/100 | Arboles / southwest county: LOW 25/100 | Arboles / southwest county: ELEVATED 33/100 | Peak ingredients near 4 PM local; RH 20%, wind 25 mph. |
| Mon, Aug 31 | Chimney Rock / west county: MODERATE 38/100 | Arboles / southwest county: LOW 8/100 | Arboles / southwest county: ELEVATED 24/100 | Peak ingredients near 4 PM local; RH 22%, wind 23 mph. |

## Analyst Interpretation

- Headline: Fire-weather screening eased to CONCERN; Aug 29 remains the peak WATCH period near Chimney Rock, with no official NWS fire-weather alert.
- Summary: Screening estimates place the highest fire potential on Sat, Aug 29 near Chimney Rock: VERY HIGH fire potential (81/100), Red Flag WATCH (72/100), and PSPS WATCH (63/100), mainly 2-6 PM. Official NWS alert count is zero. LPEA reports two unplanned outages affecting 58 customers near Bayfield and Pagosa Springs, but identifies no fire-weather or PSPS cause, so they are operational context only.
- Uncertainty: These are screening estimates, not official warnings or calibrated PSPS probabilities; forecast volatility is high, no confirmed PSPS events exist for calibration, and incident data may lag field conditions.
- Evidence used: overall_status, weather_peaks, official_alerts, forecast_change, lpea_context, fire_posture, active_incidents, calibration
- This interpretation cannot change the deterministic tiers, scores, official alerts, or notification decision.

Changing drivers:
- Momentum eased: PSPS screening shifted from LIKELY to WATCH, and the first WATCH-or-higher date moved from Aug 25 to Aug 28.
- Aug 25 fell from WATCH to ELEVATED as wind eased 2 mph, RH rose 4 percentage points, and red-flag hours remained zero.
- Aug 29 fell from LIKELY to WATCH as RH increased 1 percentage point and red-flag hours declined by two.
- Very high fire danger and Stage 1 restrictions near Chimney Rock support the Aug 29 concern; Pagosa Springs is under Stage 2 restrictions.

What to watch next:
- Watch the Aug 28-29 afternoon wind and RH forecast, especially near Chimney Rock and Arboles.
- Check NWS COZ295 for any official Red Flag or Fire Weather alert.
- Check LPEA for an identified outage cause or PSPS notice; current outages are unplanned and not linked to fire weather.
- Follow official county feeds for evacuation changes; none is currently detected.

## Trend Intelligence

- Summary: Momentum is easing versus the prior run (Aug 25 at 9:25 AM MDT); forecast volatility is high and first WATCH-or-higher date is Fri, Aug 28.
- Momentum: **Easing**
- Forecast volatility: **HIGH** (51/100)
- First WATCH-or-higher PSPS date: Fri, Aug 28
- Watch-date movement: First WATCH-or-higher PSPS date moved later from Tue, Aug 25 to Fri, Aug 28.
- Method: compares current forecast evidence against prior local forecast history.

Notable changes:
- First WATCH-or-higher PSPS date moved later from Tue, Aug 25 to Fri, Aug 28.
- Overall PSPS likelihood changed from LIKELY to WATCH.
- Tue, Aug 25: easing vs prior run; PSPS WATCH -> ELEVATED; score -24, wind -2 mph, RH +4%, red-flag hours 0. Driver shifted to Ignacio / southeast La Plata County.
- Sat, Aug 29: easing vs prior run; PSPS LIKELY -> WATCH; score -6, wind 0 mph, RH +1%, red-flag hours -2. Driver shifted to Chimney Rock / west county.
- Thu, Aug 27: easing vs prior run; PSPS ELEVATED -> ELEVATED; score -10, wind -1 mph, RH +2%, red-flag hours 0.

## Public Analysis Export

- Summary: Highest LPEA PSPS concern is Sat, Aug 29 near Chimney Rock / west county (WATCH 63/100), driven by red-flag wind/gust signal near 25 mph; red-flag RH near 15%; 5 sampled hours are near red-flag thresholds. NIFC reports 1 current wildfire in Archuleta County.
- Trend: Momentum is easing versus the prior run (Aug 25 at 9:25 AM MDT); forecast volatility is high and first WATCH-or-higher date is Fri, Aug 28.
- Confidence: **MEDIUM** (69/100)
- First WATCH-or-higher PSPS date: Fri, Aug 28
- PSPS peak: Sat, Aug 29 near Chimney Rock / west county at WATCH 63/100
- Red Flag peak: Sat, Aug 29 near Chimney Rock / west county at WATCH 72/100
- Weather fire-potential peak: Sat, Aug 29 near Chimney Rock / west county at VERY HIGH 81/100
- LPEA operational outage context: 2 active outages; 0 planned and 2 unplanned; 58 customers out. No fire-weather or PSPS cause is identified.
- Public JSON: `archuleta_red_flag_monitor/public_analysis_export.json`

What changed:
- First WATCH-or-higher PSPS date moved later from Tue, Aug 25 to Fri, Aug 28.
- Overall PSPS likelihood changed from LIKELY to WATCH.
- Tue, Aug 25: easing vs prior run; PSPS WATCH -> ELEVATED; score -24, wind -2 mph, RH +4%, red-flag hours 0. Driver shifted to Ignacio / southeast La Plata County.
- Sat, Aug 29: easing vs prior run; PSPS LIKELY -> WATCH; score -6, wind 0 mph, RH +1%, red-flag hours -2. Driver shifted to Chimney Rock / west county.
- Thu, Aug 27: easing vs prior run; PSPS ELEVATED -> ELEVATED; score -10, wind -1 mph, RH +2%, red-flag hours 0.

What to watch next:
- Check whether the largest day-level changes line up with wind/RH movement or public-source context.
- Check whether the LPEA active match is still a broad red-flag banner rather than direct PSPS/outage intent.
- Watch whether the highest-risk locations remain consistent across runs or the driver area is moving.
- If a PSPS occurs, log the confirmed date, location, and source so future hit-rate scoring can improve.

## PSPS Likelihood

- **PSPS means Public Safety Power Shutoff:** a planned, safety-related power shutoff LPEA may use during dangerous fire-weather conditions to reduce wildfire ignition risk. See [LPEA PSPS guidance](https://lpea.coop/psps) and the [LPEA outage center](https://lpea.coop/outage-center); if power is out, also check the [LPEA outage map](https://outage.lpea.coop).
- Overall: **WATCH** - PSPS watch screening is present from forecast thresholds or direct LPEA shutoff language; monitor official LPEA and NWS updates.
- Likely PSPS watch dates: None
- PSPS watch dates: Fri, Aug 28; Sat, Aug 29
- LPEA signal basis: LPEA active/update source contains red-flag, wildfire, or power-interruption language.
- Note: This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

| Date | PSPS likelihood | Driver locations | Weather basis |
| --- | --- | --- | --- |
| Tue, Aug 25 | ELEVATED | Ignacio / southeast La Plata County (ELEVATED 22/100); Arboles / southwest county (LOW 16/100); Chimney Rock / west county (LOW 16/100) | Top weather score 22/100 at Ignacio / southeast La Plata County. Weather score 22/100: RH 22%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 0. |
| Wed, Aug 26 | ELEVATED | Arboles / southwest county (ELEVATED 40/100); Ignacio / southeast La Plata County (ELEVATED 38/100); Chimney Rock / west county (ELEVATED 35/100) | Top weather score 38/100 at Arboles / southwest county. Weather score 38/100: RH 16%, wind/gust 22 mph, red-flag hours 0, near-threshold hours 3. |
| Thu, Aug 27 | ELEVATED | Arboles / southwest county (ELEVATED 30/100); Ignacio / southeast La Plata County (ELEVATED 28/100); Chimney Rock / west county (ELEVATED 26/100) | Top weather score 28/100 at Arboles / southwest county. Weather score 28/100: RH 17%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 1. |
| Fri, Aug 28 | WATCH | Arboles / southwest county (WATCH 50/100); Chimney Rock / west county (WATCH 46/100) | Top weather score 48/100 at Arboles / southwest county. Weather score 48/100: RH 15%, wind/gust 22 mph, red-flag hours 0, near-threshold hours 4. |
| Sat, Aug 29 | WATCH | Chimney Rock / west county (WATCH 63/100); Arboles / southwest county (WATCH 53/100); Ignacio / southeast La Plata County (WATCH 47/100) | Top weather score 61/100 at Chimney Rock / west county. Weather score 61/100: RH 15%, wind/gust 25 mph, red-flag hours 1, near-threshold hours 5. |
| Sun, Aug 30 | ELEVATED | Arboles / southwest county (ELEVATED 33/100); Bayfield / east La Plata County (ELEVATED 27/100); Ignacio / southeast La Plata County (ELEVATED 25/100) | Top weather score 31/100 at Arboles / southwest county. Weather score 31/100: RH 20%, wind/gust 25 mph, red-flag hours 0, near-threshold hours 0. |
| Mon, Aug 31 | ELEVATED | Arboles / southwest county (ELEVATED 24/100); Chimney Rock / west county (ELEVATED 24/100); Durango / La Plata County (ELEVATED 18/100) | Top weather score 22/100 at Arboles / southwest county. Weather score 22/100: RH 22%, wind/gust 23 mph, red-flag hours 0, near-threshold hours 0. |

## Area-Specific Outlook

| Area | Today | Peak this run | Highest-risk window |
| --- | --- | --- | --- |
| Chimney Rock | LOW 16/100 | Sat, Aug 29: WATCH 63/100 | 2 PM-6 PM local; 5 near/red-flag threshold hours. |
| Arboles | LOW 16/100 | Sat, Aug 29: WATCH 53/100 | 2 PM-6 PM local; 5 near/red-flag threshold hours. |
| Ignacio | ELEVATED 22/100 | Sat, Aug 29: WATCH 47/100 | 3 PM-5 PM local; 3 near/red-flag threshold hours. |
| Bayfield | LOW 10/100 | Fri, Aug 28: ELEVATED 44/100 | 3 PM-6 PM local; 4 near/red-flag threshold hours. |
| Chromo | LOW 10/100 | Sat, Aug 29: ELEVATED 40/100 | 4 PM-5 PM local; 2 near/red-flag threshold hours. |
| Durango | LOW 10/100 | Fri, Aug 28: ELEVATED 40/100 | 3 PM-5 PM local; 3 near/red-flag threshold hours. |
| Pagosa Springs | LOW 12/100 | Sat, Aug 29: ELEVATED 26/100 | Peak ingredients near 4 PM local; RH 21%, wind 23 mph. |
| Piedra | LOW 10/100 | Sat, Aug 29: ELEVATED 18/100 | Peak ingredients near 4 PM local; RH 23%, wind 23 mph. |

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
- Pending WATCH/LIKELY dates in current forecast: Fri, Aug 28; Sat, Aug 29
- Calibration source: manual PSPS event log plus forecast history from prior monitor runs.

### Red Flag / Fire Weather Calibration

- Summary: 3/3 official Red Flag / Fire Weather episodes had a pre-alert HIGH monitor signal; date-level result was 21/21. Episode-average lead time: 3.5 days.
- Official alert episodes logged: 3 (21 alert dates)
- Episode-level pre-alert HIGH hit rate: 100%
- Date-level pre-alert HIGH hit rate: 100%
- Episode-level average lead time: 3.5 days
- HIGH false-watch past days: 21
- Pending HIGH dates in current forecast: None
- Calibration source: official NWS Red Flag / Fire Weather alert dates plus forecast history from prior monitor runs.

## Official Weather Alerts

- Monitored NWS zones: COC007, COC067, COZ019, COZ022, COZ023, COZ295
- No active official NWS Red Flag / Fire Weather or related weather alerts found for monitored zones.

## LPEA Power Signal

- Status: `operational_outage_active` - Official LPEA outage data indicates an operational outage; use as grid context, not PSPS/fire evidence unless LPEA identifies that cause.
- Meaning: Active source match means a monitored LPEA active/update source currently contains fire, outage, PSPS, or power-interruption keywords. Operational outages are shown separately and are not treated as PSPS/fire evidence unless the source text says so.
- Operational outage context: 2 active outages; 0 planned and 2 unplanned; 58 customers out. No fire-weather or PSPS cause is identified.
- Source coverage: 13 sources; 4/5 official social sources reachable
- Evidence quality: 0 operational, 2 active/update, 0 archive/context, 6 reference source matches.
- Operational outage source links: [584 FREEMAN PARK WAY](https://outage.lpea.coop); [5535 CR 302](https://outage.lpea.coop)
- Active/update source pages with matches: LPEA homepage (public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation, restoration); LPEA LinkedIn (wildfire, public safety power shutoff, psps, power shutoff, shutoff, deenergize)
- Distinct active/update signals: LPEA LinkedIn (wildfire, public safety power shutoff, psps, power shutoff, shutoff, deenergize); LinkedIn PSPS explainer post (wildfire, public safety power shutoff, psps, power shutoff, shutoff, deenergize)
- Example signal: ...on (Kit Carson Electric, Montrose, and Farmington Electric) to compare notes on wildfire mitigation, advanced metering, and what it looks like to actually let members drive power supply decisions. Give it a l...
- Reference/context hits: [LPEA outage center](https://lpea.coop/outage-center); [LPEA wildfire / public safety power shutoffs](https://lpea.coop/psps); [LPEA red flag outage impact page](https://lpea.coop/outages/red-flag-warnings-and-impact-outages-prioritizing-safety-our-members); [LPEA fire mitigation](https://lpea.coop/fire-mitigation); [LPEA latest news](https://lpea.coop/Posts)

**Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## Next 7 Days

| Date | Tier | Main reason | Worst sampled metrics |
| --- | --- | --- | --- |
| Tue, Aug 25 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 32%, wind/gust 17 mph, thunder 10%<br>Arboles / southwest county: RH 19%, wind/gust 20 mph, thunder 4%<br>Chimney Rock / west county: RH 20%, wind/gust 17 mph, thunder 8% |
| Wed, Aug 26 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 16%, wind/gust 22 mph, thunder 11%<br>Chimney Rock / west county: RH 15%, wind/gust 20 mph, thunder 20%<br>Ignacio / southeast La Plata County: RH 17%, wind/gust 23 mph, thunder 8% |
| Thu, Aug 27 | ELEVATED | Chimney Rock / west county: Elevated ingredient present: dry-thunder probability reaches 17%. | Chimney Rock / west county: RH 17%, wind/gust 20 mph, thunder 17% |
| Fri, Aug 28 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 15%, wind/gust 22 mph, thunder 2%<br>Chimney Rock / west county: RH 14%, wind/gust 21 mph, thunder 2%<br>Durango / La Plata County: RH 17%, wind/gust 22 mph, thunder 3% |
| Sat, Aug 29 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 16%, wind/gust 26 mph, thunder 13%<br>Chimney Rock / west county: RH 15%, wind/gust 25 mph, thunder 16%<br>Chromo / southeast county: RH 18%, wind/gust 21 mph, thunder 16% |
| Sun, Aug 30 | ELEVATED | Arboles / southwest county: Elevated ingredient present: wind/gust forecast near 25 mph. | Arboles / southwest county: RH 20%, wind/gust 25 mph, thunder 24%<br>Bayfield / east La Plata County: RH 24%, wind/gust 25 mph, thunder 36%<br>Ignacio / southeast La Plata County: RH 23%, wind/gust 26 mph, thunder 26% |
| Mon, Aug 31 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 30%, wind/gust 20 mph, thunder 35%<br>Arboles / southwest county: RH 22%, wind/gust 23 mph, thunder 23%<br>Chimney Rock / west county: RH 22%, wind/gust 22 mph, thunder 33% |

## Sample Point Status

- Pagosa Springs: COZ295 (matches), forecast zone COZ023, county zone COC007
- Arboles / southwest county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Chimney Rock / west county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Piedra / north county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Chromo / southeast county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Durango / La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Bayfield / east La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Ignacio / southeast La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
