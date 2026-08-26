# Archuleta County fire-weather monitor

Generated: Aug 26, 2026 at 5:24 AM MDT (Pagosa Springs, CO local time)
Next update: Aug 26, 2026 at 5:20 PM MDT (Pagosa Springs, CO local time)
Date/time basis: Pagosa Springs, CO local time (America/Denver)
> **Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## At A Glance

- Fire-weather tier: **CONCERN**
- PSPS likelihood: **WATCH**
- PSPS likely dates: None
- PSPS watch dates: Fri, Aug 28; Sat, Aug 29; Tue, Sep 1
- Monitor heads-up recommended: **YES** - Send this monitor report because fire-weather screening tier is CONCERN; PSPS screening level is WATCH; a material current wildfire is reported in Archuleta County. This is not an official LPEA or NWS notice.
- HIGH dates: None
- CONCERN dates: Thu, Aug 27; Fri, Aug 28; Sat, Aug 29; Tue, Sep 1
- ELEVATED dates: Wed, Aug 26; Sun, Aug 30; Mon, Aug 31
- Official NWS Red Flag / Fire Weather alerts (COZ295): 0
- LPEA signal: `active_keyword_match` - LPEA active/update sources contained power-interruption keywords; review source before treating as confirmed outage intent.
- LPEA source coverage: 13 sources; 4/5 official social sources reachable
- Current Archuleta County wildfires: 1
- Official evacuation notices: No current evacuation order or warning detected in the checked official county feeds.
- NWS discussion: NWS discussion contains fire-weather concern language.

## Decision Support

- Summary: Highest LPEA PSPS concern is Tue, Sep 1 near Chimney Rock / west county (WATCH 56/100), driven by red-flag wind/gust signal near 25 mph; near-threshold RH near 18%; 2 sampled hours are near red-flag thresholds. NIFC reports 1 current wildfire in Archuleta County.
- Confidence: **MEDIUM** (74/100) - 8/8 sampled weather points available; 7/7 fire-posture sources reachable; official NWS alert zones checked; 12/13 LPEA public sources reachable; LPEA active/update sources checked; authoritative NIFC current-incident feed checked for Archuleta County; official Archuleta County evacuation feeds checked; forecast changed moderately versus prior run; no confirmed PSPS events logged yet for calibration
- Weather fire-potential peak: Tue, Sep 1: Chimney Rock / west county VERY HIGH 77/100
- Red Flag likelihood peak: Tue, Sep 1: Chimney Rock / west county WATCH 62/100
- LPEA PSPS peak: Tue, Sep 1: Chimney Rock / west county WATCH 56/100
- Method: rules-based decision support using public weather, fire-posture, and LPEA source signals; scores are screening estimates, not official or statistically calibrated probabilities.

| Date | Weather fire potential | Red Flag likelihood | LPEA PSPS | Main window |
| --- | --- | --- | --- | --- |
| Wed, Aug 26 | Chimney Rock / west county: MODERATE 46/100 | Chimney Rock / west county: LOW 25/100 | Chimney Rock / west county: ELEVATED 32/100 | Peak ingredients near 3 PM local; RH 15%, wind 18 mph. |
| Thu, Aug 27 | Arboles / southwest county: HIGH 60/100 | Arboles / southwest county: POSSIBLE 50/100 | Arboles / southwest county: ELEVATED 37/100 | Peak ingredients near 4 PM local; RH 20%, wind 21 mph. |
| Fri, Aug 28 | Chimney Rock / west county: HIGH 69/100 | Arboles / southwest county: WATCH 58/100 | Arboles / southwest county: WATCH 50/100 | 3 PM-6 PM local; 4 near/red-flag threshold hours. |
| Sat, Aug 29 | Chimney Rock / west county: HIGH 68/100 | Chimney Rock / west county: WATCH 61/100 | Arboles / southwest county: WATCH 53/100 | 2 PM-5 PM local; 4 near/red-flag threshold hours. |
| Sun, Aug 30 | Bayfield / east La Plata County: MODERATE 39/100 | Bayfield / east La Plata County: LOW 25/100 | Bayfield / east La Plata County: ELEVATED 27/100 | Peak ingredients near 4 PM local; RH 26%, wind 25 mph. |
| Mon, Aug 31 | Chimney Rock / west county: MODERATE 38/100 | Ignacio / southeast La Plata County: LOW 25/100 | Ignacio / southeast La Plata County: ELEVATED 25/100 | Peak ingredients near 4 PM local; RH 25%, wind 25 mph. |
| Tue, Sep 1 | Chimney Rock / west county: VERY HIGH 77/100 | Chimney Rock / west county: WATCH 62/100 | Chimney Rock / west county: WATCH 56/100 | 4 PM-5 PM local; 2 near/red-flag threshold hours. |

## Analyst Interpretation

- Headline: Fire-weather screening remains CONCERN as Sep 1 becomes the peak WATCH date near Chimney Rock; no official NWS alert or active LPEA outage is posted.
- Summary: Screening estimates peak Tue, Sep 1 near Chimney Rock at VERY HIGH fire potential 77/100, Red Flag WATCH 62/100, and PSPS WATCH 56/100, mainly 4-5 PM. Official NWS alerts are zero, and the official LPEA outage viewer lists no active outages; public-page keyword matches are context only, not a PSPS notice. Rio Blanco remains reported at 1,387.74 acres and 100% contained, with no evacuation notice detected.
- Uncertainty: These are screening estimates, not official warnings or calibrated PSPS probabilities; medium forecast volatility remains, no confirmed PSPS events exist for calibration, and incident data may lag field conditions.
- Evidence used: overall_status, weather_peaks, official_alerts, forecast_change, lpea_context, fire_posture, active_incidents, calibration
- This interpretation cannot change the deterministic tiers, scores, official alerts, or notification decision.

Changing drivers:
- Tue, Sep 1 entered the forecast as the highest screening peak, with WATCH-level Red Flag and PSPS concern near Chimney Rock.
- Sat, Aug 29 remains WATCH but eased 10 points as RH increased 1 percentage point and red-flag hours declined by one; the driver shifted to Arboles.
- Wed, Aug 26 eased 8 points and remains ELEVATED, with the driver shifting to Chimney Rock.
- The official LPEA outage viewer lists no active outages; remaining keyword matches are context only, not outage or PSPS intent.

What to watch next:
- Watch the Aug 28-29 and Sep 1 afternoon wind, RH, and dry-thunder forecasts, especially near Chimney Rock and Arboles.
- Check NWS COZ295 for any official Red Flag or Fire Weather alert.
- Check LPEA for a direct outage or PSPS notice rather than relying on broad or historical keyword matches.
- Follow official county feeds for fire and evacuation changes; none is currently detected.

## Trend Intelligence

- Summary: Momentum is easing versus the prior run (Aug 25 at 9:19 PM MDT); forecast volatility is medium and first WATCH-or-higher date is Fri, Aug 28.
- Momentum: **Easing**
- Forecast volatility: **MEDIUM** (20/100)
- First WATCH-or-higher PSPS date: Fri, Aug 28
- Watch-date movement: First WATCH-or-higher PSPS date remains Fri, Aug 28.
- Method: compares current forecast evidence against prior local forecast history.

Notable changes:
- First WATCH-or-higher PSPS date remains Fri, Aug 28.
- Sat, Aug 29: easing vs prior run; PSPS WATCH -> WATCH; score -10, wind 0 mph, RH +1%, red-flag hours -1. Driver shifted to Arboles / southwest county.
- Wed, Aug 26: easing vs prior run; PSPS ELEVATED -> ELEVATED; score -8, wind -1 mph, RH 0%, red-flag hours 0. Driver shifted to Chimney Rock / west county.

## Public Analysis Export

- Summary: Highest LPEA PSPS concern is Tue, Sep 1 near Chimney Rock / west county (WATCH 56/100), driven by red-flag wind/gust signal near 25 mph; near-threshold RH near 18%; 2 sampled hours are near red-flag thresholds. NIFC reports 1 current wildfire in Archuleta County.
- Trend: Momentum is easing versus the prior run (Aug 25 at 9:19 PM MDT); forecast volatility is medium and first WATCH-or-higher date is Fri, Aug 28.
- Confidence: **MEDIUM** (74/100)
- First WATCH-or-higher PSPS date: Fri, Aug 28
- PSPS peak: Tue, Sep 1 near Chimney Rock / west county at WATCH 56/100
- Red Flag peak: Tue, Sep 1 near Chimney Rock / west county at WATCH 62/100
- Weather fire-potential peak: Tue, Sep 1 near Chimney Rock / west county at VERY HIGH 77/100
- LPEA operational outage context: No active outages are listed by the official LPEA outage viewer.
- Public JSON: `archuleta_red_flag_monitor/public_analysis_export.json`

What changed:
- First WATCH-or-higher PSPS date remains Fri, Aug 28.
- Sat, Aug 29: easing vs prior run; PSPS WATCH -> WATCH; score -10, wind 0 mph, RH +1%, red-flag hours -1. Driver shifted to Arboles / southwest county.
- Wed, Aug 26: easing vs prior run; PSPS ELEVATED -> ELEVATED; score -8, wind -1 mph, RH 0%, red-flag hours 0. Driver shifted to Chimney Rock / west county.

What to watch next:
- Check whether the largest day-level changes line up with wind/RH movement or public-source context.
- Check whether the LPEA active match is still a broad red-flag banner rather than direct PSPS/outage intent.
- Watch whether the highest-risk locations remain consistent across runs or the driver area is moving.
- If a PSPS occurs, log the confirmed date, location, and source so future hit-rate scoring can improve.

## PSPS Likelihood

- **PSPS means Public Safety Power Shutoff:** a planned, safety-related power shutoff LPEA may use during dangerous fire-weather conditions to reduce wildfire ignition risk. See [LPEA PSPS guidance](https://lpea.coop/psps) and the [LPEA outage center](https://lpea.coop/outage-center); if power is out, also check the [LPEA outage map](https://outage.lpea.coop).
- Overall: **WATCH** - PSPS watch screening is present from forecast thresholds or direct LPEA shutoff language; monitor official LPEA and NWS updates.
- Likely PSPS watch dates: None
- PSPS watch dates: Fri, Aug 28; Sat, Aug 29; Tue, Sep 1
- LPEA signal basis: LPEA active/update source contains red-flag, wildfire, or power-interruption language.
- Note: This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

| Date | PSPS likelihood | Driver locations | Weather basis |
| --- | --- | --- | --- |
| Wed, Aug 26 | ELEVATED | Chimney Rock / west county (ELEVATED 32/100); Ignacio / southeast La Plata County (ELEVATED 28/100); Bayfield / east La Plata County (ELEVATED 24/100) | Top weather score 30/100 at Chimney Rock / west county. Weather score 30/100: RH 15%, wind/gust 18 mph, red-flag hours 0, near-threshold hours 0. |
| Thu, Aug 27 | ELEVATED | Arboles / southwest county (ELEVATED 37/100); Durango / La Plata County (ELEVATED 24/100); Bayfield / east La Plata County (ELEVATED 24/100) | Top weather score 35/100 at Arboles / southwest county. Weather score 35/100: RH 16%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 0. |
| Fri, Aug 28 | WATCH | Arboles / southwest county (WATCH 50/100); Chimney Rock / west county (WATCH 46/100) | Top weather score 48/100 at Arboles / southwest county. Weather score 48/100: RH 15%, wind/gust 22 mph, red-flag hours 0, near-threshold hours 4. |
| Sat, Aug 29 | WATCH | Arboles / southwest county (WATCH 53/100); Chimney Rock / west county (WATCH 53/100) | Top weather score 51/100 at Arboles / southwest county. Weather score 51/100: RH 17%, wind/gust 28 mph, red-flag hours 0, near-threshold hours 4. |
| Sun, Aug 30 | ELEVATED | Bayfield / east La Plata County (ELEVATED 27/100); Ignacio / southeast La Plata County (ELEVATED 25/100); Chimney Rock / west county (ELEVATED 24/100) | Top weather score 25/100 at Bayfield / east La Plata County. Weather score 25/100: RH 26%, wind/gust 25 mph, red-flag hours 0, near-threshold hours 0. |
| Mon, Aug 31 | ELEVATED | Ignacio / southeast La Plata County (ELEVATED 25/100); Arboles / southwest county (ELEVATED 24/100); Chimney Rock / west county (ELEVATED 24/100) | Top weather score 25/100 at Ignacio / southeast La Plata County. Weather score 25/100: RH 25%, wind/gust 25 mph, red-flag hours 0, near-threshold hours 0. |
| Tue, Sep 1 | WATCH | Chimney Rock / west county (WATCH 56/100) | Top weather score 54/100 at Chimney Rock / west county. Weather score 54/100: RH 18%, wind/gust 25 mph, red-flag hours 0, near-threshold hours 2. |

## Area-Specific Outlook

| Area | Today | Peak this run | Highest-risk window |
| --- | --- | --- | --- |
| Chimney Rock | ELEVATED 32/100 | Tue, Sep 1: WATCH 56/100 | 4 PM-5 PM local; 2 near/red-flag threshold hours. |
| Arboles | ELEVATED 22/100 | Sat, Aug 29: WATCH 53/100 | 2 PM-5 PM local; 4 near/red-flag threshold hours. |
| Ignacio | ELEVATED 28/100 | Fri, Aug 28: ELEVATED 42/100 | 3 PM-6 PM local; 4 near/red-flag threshold hours. |
| Durango | LOW 16/100 | Fri, Aug 28: ELEVATED 40/100 | 3 PM-5 PM local; 3 near/red-flag threshold hours. |
| Bayfield | ELEVATED 24/100 | Fri, Aug 28: ELEVATED 40/100 | 4 PM-5 PM local; 2 near/red-flag threshold hours. |
| Chromo | LOW 16/100 | Sat, Aug 29: ELEVATED 24/100 | Peak ingredients near 4 PM local; RH 20%, wind 22 mph. |
| Pagosa Springs | ELEVATED 18/100 | Sat, Aug 29: ELEVATED 20/100 | Peak ingredients near 3 PM local; RH 23%, wind 23 mph. |
| Piedra | LOW 10/100 | Sat, Aug 29: ELEVATED 18/100 | Peak ingredients near 5 PM local; RH 24%, wind 22 mph. |

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
- WATCH/LIKELY false-watch past days: 65
- Pending WATCH/LIKELY dates in current forecast: Fri, Aug 28; Sat, Aug 29; Tue, Sep 1
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

- Status: `active_keyword_match` - LPEA active/update sources contained power-interruption keywords; review source before treating as confirmed outage intent.
- Meaning: Active source match means a monitored LPEA active/update source currently contains fire, outage, PSPS, or power-interruption keywords. Operational outages are shown separately and are not treated as PSPS/fire evidence unless the source text says so.
- Operational outage context: No active outages are listed by the official LPEA outage viewer.
- Source coverage: 13 sources; 4/5 official social sources reachable
- Evidence quality: 0 operational, 4 active/update, 0 archive/context, 6 reference source matches.
- Active/update source pages with matches: LPEA homepage (public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation, restoration); LPEA X (power outage, outage map, high winds, restore power); LPEA LinkedIn (wildfire, public safety power shutoff, psps, power shutoff, shutoff, deenergize)
- Distinct active/update signals: LPEA X (power outage, outage map, high winds, restore power); LPEA X (power outage, outage map, high winds, restore power); LPEA LinkedIn (wildfire, public safety power shutoff, psps, power shutoff, shutoff, deenergize); LinkedIn PSPS explainer post (wildfire, public safety power shutoff, psps, power shutoff, shutoff, deenergize)
- Example signal: ...ibrary! 1 2 536 LPEA @LaPlataElectric May 7, 2024 LPEA members are experiencing power outages in the Bayfield and Pagosa Springs areas. Approximately 200 meters are out and it is suspected that the high winds are...
- Reference/context hits: [LPEA outage center](https://lpea.coop/outage-center); [LPEA wildfire / public safety power shutoffs](https://lpea.coop/psps); [LPEA red flag outage impact page](https://lpea.coop/outages/red-flag-warnings-and-impact-outages-prioritizing-safety-our-members); [LPEA fire mitigation](https://lpea.coop/fire-mitigation); [LPEA latest news](https://lpea.coop/Posts)

**Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## Next 7 Days

| Date | Tier | Main reason | Worst sampled metrics |
| --- | --- | --- | --- |
| Wed, Aug 26 | ELEVATED | Chimney Rock / west county: Elevated ingredient present: very low RH forecast near 15%; dry-thunder probability reaches 15%. | Chimney Rock / west county: RH 15%, wind/gust 18 mph, thunder 15% |
| Thu, Aug 27 | CONCERN | Arboles / southwest county: Dry-thunder signal: 1 hourly period combine thunder near 20% with limited precipitation and dry air. | Arboles / southwest county: RH 16%, wind/gust 21 mph, thunder 20% |
| Fri, Aug 28 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 15%, wind/gust 22 mph, thunder 1%<br>Chimney Rock / west county: RH 14%, wind/gust 21 mph, thunder 2%<br>Durango / La Plata County: RH 17%, wind/gust 22 mph, thunder 4% |
| Sat, Aug 29 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 17%, wind/gust 28 mph, thunder 26%<br>Chimney Rock / west county: RH 16%, wind/gust 25 mph, thunder 21%<br>Durango / La Plata County: RH 20%, wind/gust 26 mph, thunder 35% |
| Sun, Aug 30 | ELEVATED | Bayfield / east La Plata County: Elevated ingredient present: wind/gust forecast near 25 mph. | Bayfield / east La Plata County: RH 26%, wind/gust 25 mph, thunder 32%<br>Ignacio / southeast La Plata County: RH 25%, wind/gust 26 mph, thunder 28% |
| Mon, Aug 31 | ELEVATED | Ignacio / southeast La Plata County: Elevated ingredient present: wind/gust forecast near 25 mph. | Ignacio / southeast La Plata County: RH 25%, wind/gust 25 mph, thunder 23% |
| Tue, Sep 1 | CONCERN | Chimney Rock / west county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 20%, wind/gust 26 mph, thunder 14%<br>Chimney Rock / west county: RH 18%, wind/gust 25 mph, thunder 20%<br>Durango / La Plata County: RH 23%, wind/gust 26 mph, thunder 25% |

## Sample Point Status

- Pagosa Springs: COZ295 (matches), forecast zone COZ023, county zone COC007
- Arboles / southwest county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Chimney Rock / west county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Piedra / north county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Chromo / southeast county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Durango / La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Bayfield / east La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Ignacio / southeast La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
