# Archuleta County fire-weather monitor

Generated: Aug 29, 2026 at 5:22 PM MDT (Pagosa Springs, CO local time)
Next update: Aug 30, 2026 at 5:20 AM MDT (Pagosa Springs, CO local time)
Date/time basis: Pagosa Springs, CO local time (America/Denver)
> **Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## At A Glance

- Fire-weather tier: **ELEVATED**
- PSPS likelihood: **ELEVATED**
- PSPS likely dates: None
- PSPS watch dates: None
- Monitor heads-up recommended: **YES** - Send this monitor report because a material current wildfire is reported in Archuleta County. This is not an official LPEA or NWS notice.
- HIGH dates: None
- CONCERN dates: None
- ELEVATED dates: Sun, Aug 30; Tue, Sep 1; Wed, Sep 2
- Official NWS Red Flag / Fire Weather alerts (COZ295): 0
- LPEA signal: `operational_outage_active` - Official LPEA outage data indicates an operational outage; use as grid context, not PSPS/fire evidence unless LPEA identifies that cause.
- LPEA source coverage: 13 sources; 5/5 official social sources reachable
- Current Archuleta County wildfires: 3
- Official evacuation notices: No current evacuation order or warning detected in the checked official county feeds.
- NWS discussion: No concerning fire-weather language found in latest GJT discussion.

## Decision Support

- Summary: Highest LPEA PSPS concern is Wed, Sep 2 near Arboles / southwest county (ELEVATED 33/100), driven by red-flag wind/gust signal near 25 mph; dry RH near 22%; Official fire-posture context for Arboles / southwest county is elevated (STAGE 1; fire danger UNKNOWN), used as a small supporting modifier. NIFC reports 3 current wildfires in Archuleta County.
- Confidence: **MEDIUM** (69/100) - 8/8 sampled weather points available; 7/7 fire-posture sources reachable; official NWS alert zones checked; 13/13 LPEA public sources reachable; LPEA active/update sources checked; active LPEA operational outage context checked separately from PSPS scoring; authoritative NIFC current-incident feed checked for Archuleta County; official Archuleta County evacuation feeds checked; forecast changed substantially versus prior run; no confirmed PSPS events logged yet for calibration
- Weather fire-potential peak: Thu, Sep 3: Chimney Rock / west county MODERATE 42/100
- Red Flag likelihood peak: Wed, Sep 2: Arboles / southwest county LOW 25/100
- LPEA PSPS peak: Wed, Sep 2: Arboles / southwest county ELEVATED 33/100
- Method: rules-based decision support using public weather, fire-posture, and LPEA source signals; scores are screening estimates, not official or statistically calibrated probabilities.

| Date | Weather fire potential | Red Flag likelihood | LPEA PSPS | Main window |
| --- | --- | --- | --- | --- |
| Sat, Aug 29 | Pagosa Springs: LOW 30/100 | Pagosa Springs: LOW 8/100 | Pagosa Springs: ELEVATED 18/100 | Peak ingredients near 5 PM local; RH 32%, wind 21 mph. |
| Sun, Aug 30 | Ignacio / southeast La Plata County: MODERATE 35/100 | Ignacio / southeast La Plata County: LOW 25/100 | Ignacio / southeast La Plata County: ELEVATED 25/100 | Peak ingredients near 4 PM local; RH 31%, wind 25 mph. |
| Mon, Aug 31 | Pagosa Springs: LOW 18/100 | Pagosa Springs: LOW 0/100 | Pagosa Springs: LOW 10/100 | Peak ingredients near 3 PM local; RH 38%, wind 17 mph. |
| Tue, Sep 1 | Durango / La Plata County: MODERATE 39/100 | Durango / La Plata County: LOW 25/100 | Durango / La Plata County: ELEVATED 27/100 | Peak ingredients near 4 PM local; RH 26%, wind 25 mph. |
| Wed, Sep 2 | Pagosa Springs: MODERATE 39/100 | Arboles / southwest county: LOW 25/100 | Arboles / southwest county: ELEVATED 33/100 | Peak ingredients near 4 PM local; RH 22%, wind 25 mph. |
| Thu, Sep 3 | Chimney Rock / west county: MODERATE 42/100 | Chimney Rock / west county: LOW 16/100 | Chimney Rock / west county: ELEVATED 30/100 | 4 PM-4 PM local; 1 near/red-flag threshold hour. |
| Fri, Sep 4 | Chimney Rock / west county: MODERATE 38/100 | Arboles / southwest county: LOW 8/100 | Arboles / southwest county: ELEVATED 24/100 | Peak ingredients near 4 PM local; RH 20%, wind 22 mph. |

## Analyst Interpretation

- Headline: Fire-weather and PSPS screening eased to ELEVATED with no watch dates; LPEA reports one localized outage with no fire or PSPS cause identified.
- Summary: The prior Sep 4 WATCH fell to ELEVATED, and no HIGH or CONCERN dates remain. Peak PSPS screening is ELEVATED 33/100 near Arboles on Sep 2; the weather peak is MODERATE 42/100 near Chimney Rock on Sep 3. LPEA's official viewer lists one unplanned one-customer outage near Durango, but no fire-weather or PSPS cause is identified; NWS alerts and evacuation notices remain zero.
- Uncertainty: Screening scores are not official warnings or calibrated PSPS probabilities; the outage cause is unreported, and forecast, incident, and public-page data may change or lag.
- Evidence used: overall_status, weather_peaks, official_alerts, forecast_change, lpea_context, fire_posture, active_incidents, calibration
- This interpretation cannot change the deterministic tiers, scores, official alerts, or notification decision.

Changing drivers:
- The prior Sep 4 PSPS WATCH fell to ELEVATED, lowering overall PSPS screening from WATCH to ELEVATED.
- Sep 4 eased by 24 points as RH increased by 3 percentage points; its leading location shifted to Arboles.
- LPEA reports one unplanned one-customer outage near Durango, with no fire-weather or PSPS cause identified.
- Three wildfires remain listed, including Swiss Roll at 1.50 acres, with no evacuation notice detected.

What to watch next:
- Check the official LPEA outage viewer for restoration or a posted cause for the localized Durango-area outage.
- Recheck Sep 2 near Arboles and Sep 3 near Chimney Rock for renewed drying or wind increases.
- Check official NWS COZ295 and LPEA updates for any direct alert or PSPS notice.
- Continue monitoring current fires and official county evacuation feeds.

## Trend Intelligence

- Summary: Momentum is easing versus the prior run (Aug 29 at 5:21 AM MDT); forecast volatility is high and first WATCH-or-higher date is not present.
- Momentum: **Easing**
- Forecast volatility: **HIGH** (56/100)
- First WATCH-or-higher PSPS date: None
- Watch-date movement: Prior WATCH-or-higher PSPS date Fri, Sep 4 dropped below WATCH.
- Method: compares current forecast evidence against prior local forecast history.

Notable changes:
- Prior WATCH-or-higher PSPS date Fri, Sep 4 dropped below WATCH.
- Overall PSPS likelihood changed from WATCH to ELEVATED.
- Fri, Sep 4: easing vs prior run; PSPS WATCH -> ELEVATED; score -24, wind 0 mph, RH +3%, red-flag hours 0. Driver shifted to Arboles / southwest county.
- Mon, Aug 31: easing vs prior run; PSPS ELEVATED -> LOW; score -8, wind -2 mph, RH +2%, red-flag hours 0. Driver shifted to Pagosa Springs.
- Thu, Sep 3: easing vs prior run; PSPS ELEVATED -> ELEVATED; score -10, wind -1 mph, RH +1%, red-flag hours 0.
- Sat, Aug 29: easing vs prior run; PSPS ELEVATED -> ELEVATED; score -6, wind -1 mph, RH +4%, red-flag hours 0. Driver shifted to Pagosa Springs.

## Public Analysis Export

- Summary: Highest LPEA PSPS concern is Wed, Sep 2 near Arboles / southwest county (ELEVATED 33/100), driven by red-flag wind/gust signal near 25 mph; dry RH near 22%; Official fire-posture context for Arboles / southwest county is elevated (STAGE 1; fire danger UNKNOWN), used as a small supporting modifier. NIFC reports 3 current wildfires in Archuleta County.
- Trend: Momentum is easing versus the prior run (Aug 29 at 5:21 AM MDT); forecast volatility is high and first WATCH-or-higher date is not present.
- Confidence: **MEDIUM** (69/100)
- First WATCH-or-higher PSPS date: None
- PSPS peak: Wed, Sep 2 near Arboles / southwest county at ELEVATED 33/100
- Red Flag peak: Wed, Sep 2 near Arboles / southwest county at LOW 25/100
- Weather fire-potential peak: Thu, Sep 3 near Chimney Rock / west county at MODERATE 42/100
- LPEA operational outage context: 1 active outage; 0 planned and 1 unplanned; 1 customer out. No fire-weather or PSPS cause is identified.
- Public JSON: `archuleta_red_flag_monitor/public_analysis_export.json`

What changed:
- Prior WATCH-or-higher PSPS date Fri, Sep 4 dropped below WATCH.
- Overall PSPS likelihood changed from WATCH to ELEVATED.
- Fri, Sep 4: easing vs prior run; PSPS WATCH -> ELEVATED; score -24, wind 0 mph, RH +3%, red-flag hours 0. Driver shifted to Arboles / southwest county.
- Mon, Aug 31: easing vs prior run; PSPS ELEVATED -> LOW; score -8, wind -2 mph, RH +2%, red-flag hours 0. Driver shifted to Pagosa Springs.
- Thu, Sep 3: easing vs prior run; PSPS ELEVATED -> ELEVATED; score -10, wind -1 mph, RH +1%, red-flag hours 0.
- Sat, Aug 29: easing vs prior run; PSPS ELEVATED -> ELEVATED; score -6, wind -1 mph, RH +4%, red-flag hours 0. Driver shifted to Pagosa Springs.

What to watch next:
- Check whether the largest day-level changes line up with wind/RH movement or public-source context.
- Check whether the LPEA active match is still a broad red-flag banner rather than direct PSPS/outage intent.
- Watch whether the highest-risk locations remain consistent across runs or the driver area is moving.
- If a PSPS occurs, log the confirmed date, location, and source so future hit-rate scoring can improve.

## PSPS Likelihood

- **PSPS means Public Safety Power Shutoff:** a planned, safety-related power shutoff LPEA may use during dangerous fire-weather conditions to reduce wildfire ignition risk. See [LPEA PSPS guidance](https://lpea.coop/psps) and the [LPEA outage center](https://lpea.coop/outage-center); if power is out, also check the [LPEA outage map](https://outage.lpea.coop).
- Overall: **ELEVATED** - PSPS likelihood is elevated, but weather remains below watch thresholds.
- Likely PSPS watch dates: None
- PSPS watch dates: None
- LPEA signal basis: LPEA active/update source contains red-flag, wildfire, or power-interruption language.
- Note: This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

| Date | PSPS likelihood | Driver locations | Weather basis |
| --- | --- | --- | --- |
| Sat, Aug 29 | ELEVATED | Pagosa Springs (ELEVATED 18/100); Arboles / southwest county (ELEVATED 18/100); Chimney Rock / west county (ELEVATED 18/100) | Top weather score 16/100 at Pagosa Springs. Weather score 16/100: RH 32%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 0. |
| Sun, Aug 30 | ELEVATED | Ignacio / southeast La Plata County (ELEVATED 25/100); Pagosa Springs (ELEVATED 18/100); Arboles / southwest county (ELEVATED 18/100) | Top weather score 25/100 at Ignacio / southeast La Plata County. Weather score 25/100: RH 28%, wind/gust 25 mph, red-flag hours 0, near-threshold hours 0. |
| Mon, Aug 31 | LOW | Pagosa Springs (LOW 10/100); Arboles / southwest county (LOW 10/100); Chimney Rock / west county (LOW 10/100) | Top weather score 8/100 at Pagosa Springs. Weather score 8/100: RH 37%, wind/gust 17 mph, red-flag hours 0, near-threshold hours 0. |
| Tue, Sep 1 | ELEVATED | Durango / La Plata County (ELEVATED 27/100); Bayfield / east La Plata County (ELEVATED 27/100); Ignacio / southeast La Plata County (ELEVATED 25/100) | Top weather score 25/100 at Durango / La Plata County. Weather score 25/100: RH 26%, wind/gust 25 mph, red-flag hours 0, near-threshold hours 0. |
| Wed, Sep 2 | ELEVATED | Arboles / southwest county (ELEVATED 33/100); Pagosa Springs (ELEVATED 27/100); Durango / La Plata County (ELEVATED 27/100) | Top weather score 31/100 at Arboles / southwest county. Weather score 31/100: RH 22%, wind/gust 25 mph, red-flag hours 0, near-threshold hours 0. |
| Thu, Sep 3 | ELEVATED | Chimney Rock / west county (ELEVATED 30/100); Arboles / southwest county (ELEVATED 24/100); Ignacio / southeast La Plata County (ELEVATED 22/100) | Top weather score 28/100 at Chimney Rock / west county. Weather score 28/100: RH 18%, wind/gust 23 mph, red-flag hours 0, near-threshold hours 1. |
| Fri, Sep 4 | ELEVATED | Arboles / southwest county (ELEVATED 24/100); Chimney Rock / west county (ELEVATED 24/100); Pagosa Springs (ELEVATED 18/100) | Top weather score 22/100 at Arboles / southwest county. Weather score 22/100: RH 20%, wind/gust 22 mph, red-flag hours 0, near-threshold hours 0. |

## Area-Specific Outlook

| Area | Today | Peak this run | Highest-risk window |
| --- | --- | --- | --- |
| Arboles | ELEVATED 18/100 | Wed, Sep 2: ELEVATED 33/100 | Peak ingredients near 4 PM local; RH 22%, wind 25 mph. |
| Chimney Rock | ELEVATED 18/100 | Thu, Sep 3: ELEVATED 30/100 | 4 PM-4 PM local; 1 near/red-flag threshold hour. |
| Pagosa Springs | ELEVATED 18/100 | Wed, Sep 2: ELEVATED 27/100 | Peak ingredients near 4 PM local; RH 25%, wind 25 mph. |
| Durango | ELEVATED 18/100 | Tue, Sep 1: ELEVATED 27/100 | Peak ingredients near 4 PM local; RH 26%, wind 25 mph. |
| Bayfield | ELEVATED 18/100 | Tue, Sep 1: ELEVATED 27/100 | Peak ingredients near 4 PM local; RH 27%, wind 25 mph. |
| Ignacio | LOW 16/100 | Sun, Aug 30: ELEVATED 25/100 | Peak ingredients near 4 PM local; RH 31%, wind 25 mph. |
| Piedra | LOW 10/100 | Sun, Aug 30: ELEVATED 18/100 | Peak ingredients near 3 PM local; RH 40%, wind 21 mph. |
| Chromo | LOW 10/100 | Wed, Sep 2: ELEVATED 18/100 | Peak ingredients near 4 PM local; RH 23%, wind 22 mph. |

## Current Fires + Evacuations

- Incident summary: 3 current wildfires reported in Archuleta County; no current evacuation notice detected in checked county feeds.
- Evacuation status: **NONE DETECTED** - No current evacuation order or warning detected in the checked official county feeds.
- Safety note: Current incidents and evacuation notices are operational context. They do not raise PSPS scores by themselves; follow official evacuation instructions immediately.

### Current NIFC Incidents

| Incident | Type | Size | Containment | Nearest monitored area | Updated |
| --- | --- | --- | --- | --- | --- |
| Rio Blanco | Wildfire | 1,387.74 acres | 100% | Chromo / southeast county (9.9 mi) | Aug 18 at 7:20 PM MDT |
| Swiss Roll | Wildfire | 1.50 acres | Not reported | Pagosa Springs (14.6 mi) | Aug 29 at 1:29 PM MDT |
| Medicine Creek | Wildfire | 0.10 acres | Not reported | Piedra / north county (11.5 mi) | Aug 28 at 6:26 PM MDT |

Official links: [NIFC map](https://www.nifc.gov/fire-information/maps), [Archuleta County fire updates](https://sheriff.archuletacounty.gov/divisions/emergency-operations/fire-updates-and-information/), [County alerts](https://nixle.us/archuleta-county-office-of-emergency-management-aux/), [Watch Duty](https://app.watchduty.org/)

## Fire Posture + Restrictions

- Summary: 3 official sources indicate fire restrictions or staged restrictions.
- Max restriction stage detected: STAGE 1
- Max fire danger detected: VERY HIGH
- Sources reachable: 7/7
- Note: Official-source status check only; verify restrictions and burn decisions with the responsible jurisdiction.

| Jurisdiction | Restrictions | Fire danger | Source |
| --- | --- | --- | --- |
| Archuleta County | STAGE 1 | UNKNOWN | [Archuleta County Sheriff fire updates](https://sheriff.archuletacounty.gov/divisions/emergency-operations/fire-updates-and-information/) |
| Pagosa Springs | STAGE 1 | UNKNOWN | [Town of Pagosa Springs](https://www.pagosasprings.co.gov/) |
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
- WATCH/LIKELY false-watch past days: 68
- Pending WATCH/LIKELY dates in current forecast: None
- Calibration source: manual PSPS event log plus forecast history from prior monitor runs.

### Red Flag / Fire Weather Calibration

- Summary: 3/3 official Red Flag / Fire Weather episodes had a pre-alert HIGH monitor signal; date-level result was 21/21. Episode-average lead time: 3.5 days.
- Official alert episodes logged: 3 (21 alert dates)
- Episode-level pre-alert HIGH hit rate: 100%
- Date-level pre-alert HIGH hit rate: 100%
- Episode-level average lead time: 3.5 days
- HIGH false-watch past days: 22
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
- Operational outage source links: [6867 COUNTY RD 203](https://outage.lpea.coop)
- Active/update source pages with matches: LPEA homepage (public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation, restoration); LPEA X (power outage, outage map, high winds, restore power); LPEA LinkedIn (wildfire, public safety power shutoff, psps, power shutoff, shutoff, deenergize)
- Distinct active/update signals: LPEA X (power outage, outage map, high winds, restore power); LPEA X (power outage, outage map, high winds, restore power); LPEA LinkedIn (wildfire, public safety power shutoff, psps, power shutoff, shutoff, deenergize); LinkedIn PSPS explainer post (wildfire, public safety power shutoff, psps, power shutoff, shutoff, deenergize)
- Example signal: ...ibrary! 1 2 537 LPEA @LaPlataElectric May 7, 2024 LPEA members are experiencing power outages in the Bayfield and Pagosa Springs areas. Approximately 200 meters are out and it is suspected that the high winds are...
- Reference/context hits: [LPEA outage center](https://lpea.coop/outage-center); [LPEA wildfire / public safety power shutoffs](https://lpea.coop/psps); [LPEA red flag outage impact page](https://lpea.coop/outages/red-flag-warnings-and-impact-outages-prioritizing-safety-our-members); [LPEA fire mitigation](https://lpea.coop/fire-mitigation); [LPEA latest news](https://lpea.coop/Posts)

**Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## Next 7 Days

| Date | Tier | Main reason | Worst sampled metrics |
| --- | --- | --- | --- |
| Sat, Aug 29 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 32%, wind/gust 21 mph, thunder 26%<br>Arboles / southwest county: RH 24%, wind/gust 22 mph, thunder 30%<br>Chimney Rock / west county: RH 25%, wind/gust 21 mph, thunder 30% |
| Sun, Aug 30 | ELEVATED | Ignacio / southeast La Plata County: Elevated ingredient present: wind/gust forecast near 25 mph. | Ignacio / southeast La Plata County: RH 28%, wind/gust 25 mph, thunder 32% |
| Mon, Aug 31 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 37%, wind/gust 17 mph, thunder 52%<br>Arboles / southwest county: RH 33%, wind/gust 18 mph, thunder 48%<br>Chimney Rock / west county: RH 30%, wind/gust 18 mph, thunder 54% |
| Tue, Sep 1 | ELEVATED | Durango / La Plata County: Elevated ingredient present: wind/gust forecast near 25 mph. | Durango / La Plata County: RH 26%, wind/gust 25 mph, thunder 8%<br>Bayfield / east La Plata County: RH 27%, wind/gust 25 mph, thunder 9%<br>Ignacio / southeast La Plata County: RH 26%, wind/gust 25 mph, thunder 9% |
| Wed, Sep 2 | ELEVATED | Pagosa Springs: Elevated ingredient present: wind/gust forecast near 25 mph. | Pagosa Springs: RH 25%, wind/gust 25 mph, thunder 7%<br>Arboles / southwest county: RH 22%, wind/gust 25 mph, thunder 4%<br>Durango / La Plata County: RH 27%, wind/gust 25 mph, thunder 15% |
| Thu, Sep 3 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 24%, wind/gust 23 mph, thunder 13%<br>Arboles / southwest county: RH 20%, wind/gust 24 mph, thunder 8%<br>Chimney Rock / west county: RH 18%, wind/gust 23 mph, thunder 10% |
| Fri, Sep 4 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 27%, wind/gust 22 mph, thunder 29%<br>Arboles / southwest county: RH 20%, wind/gust 22 mph, thunder 23%<br>Chimney Rock / west county: RH 19%, wind/gust 22 mph, thunder 25% |

## Sample Point Status

- Pagosa Springs: COZ295 (matches), forecast zone COZ023, county zone COC007
- Arboles / southwest county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Chimney Rock / west county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Piedra / north county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Chromo / southeast county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Durango / La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Bayfield / east La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Ignacio / southeast La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
