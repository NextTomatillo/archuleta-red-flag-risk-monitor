# Archuleta County fire-weather monitor

Generated: Aug 31, 2026 at 5:26 AM MDT (Pagosa Springs, CO local time)
Next update: Aug 31, 2026 at 5:20 PM MDT (Pagosa Springs, CO local time)
Date/time basis: Pagosa Springs, CO local time (America/Denver)
> **Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## At A Glance

- Fire-weather tier: **CONCERN**
- PSPS likelihood: **ELEVATED**
- PSPS likely dates: None
- PSPS watch dates: None
- Monitor heads-up recommended: **YES** - Send this monitor report because fire-weather screening tier is CONCERN; a material current wildfire is reported in Archuleta County. This is not an official LPEA or NWS notice.
- HIGH dates: None
- CONCERN dates: Thu, Sep 3
- ELEVATED dates: Wed, Sep 2
- Official NWS Red Flag / Fire Weather alerts (COZ295): 0
- LPEA signal: `operational_outage_active` - Official LPEA outage data indicates an operational outage; use as grid context, not PSPS/fire evidence unless LPEA identifies that cause.
- LPEA source coverage: 13 sources; 5/5 official social sources reachable
- Current Archuleta County wildfires: 3
- Official evacuation notices: No current evacuation order or warning detected in the checked official county feeds.
- NWS discussion: No concerning fire-weather language found in latest GJT discussion.

## Decision Support

- Summary: Highest LPEA PSPS concern is Thu, Sep 3 near Chimney Rock / west county (ELEVATED 40/100), driven by near-threshold wind/gust signal near 22 mph; near-threshold RH near 17%; 3 sampled hours are near red-flag thresholds. NIFC reports 3 current wildfires in Archuleta County.
- Confidence: **MEDIUM** (69/100) - 8/8 sampled weather points available; 7/7 fire-posture sources reachable; official NWS alert zones checked; 13/13 LPEA public sources reachable; LPEA active/update sources checked; active LPEA operational outage context checked separately from PSPS scoring; authoritative NIFC current-incident feed checked for Archuleta County; official Archuleta County evacuation feeds checked; forecast changed substantially versus prior run; no confirmed PSPS events logged yet for calibration
- Weather fire-potential peak: Thu, Sep 3: Chimney Rock / west county HIGH 62/100
- Red Flag likelihood peak: Thu, Sep 3: Chimney Rock / west county POSSIBLE 50/100
- LPEA PSPS peak: Thu, Sep 3: Chimney Rock / west county ELEVATED 40/100
- Method: rules-based decision support using public weather, fire-posture, and LPEA source signals; scores are screening estimates, not official or statistically calibrated probabilities.

| Date | Weather fire potential | Red Flag likelihood | LPEA PSPS | Main window |
| --- | --- | --- | --- | --- |
| Mon, Aug 31 | Pagosa Springs: LOW 18/100 | Ignacio / southeast La Plata County: LOW 8/100 | Ignacio / southeast La Plata County: LOW 16/100 | Peak ingredients near 3 PM local; RH 44%, wind 21 mph. |
| Tue, Sep 1 | Pagosa Springs: LOW 30/100 | Pagosa Springs: LOW 8/100 | Pagosa Springs: ELEVATED 18/100 | Peak ingredients near 4 PM local; RH 32%, wind 21 mph. |
| Wed, Sep 2 | Durango / La Plata County: MODERATE 39/100 | Arboles / southwest county: LOW 25/100 | Arboles / southwest county: ELEVATED 33/100 | Peak ingredients near 4 PM local; RH 21%, wind 25 mph. |
| Thu, Sep 3 | Chimney Rock / west county: HIGH 62/100 | Chimney Rock / west county: POSSIBLE 50/100 | Chimney Rock / west county: ELEVATED 40/100 | 3 PM-5 PM local; 3 near/red-flag threshold hours. |
| Fri, Sep 4 | Pagosa Springs: LOW 30/100 | Pagosa Springs: LOW 8/100 | Pagosa Springs: ELEVATED 18/100 | Peak ingredients near 3 PM local; RH 27%, wind 21 mph. |
| Sat, Sep 5 | Durango / La Plata County: LOW 30/100 | Durango / La Plata County: LOW 8/100 | Durango / La Plata County: ELEVATED 18/100 | Peak ingredients near 3 PM local; RH 29%, wind 21 mph. |
| Sun, Sep 6 | Durango / La Plata County: LOW 30/100 | Arboles / southwest county: LOW 8/100 | Arboles / southwest county: ELEVATED 24/100 | Peak ingredients near 4 PM local; RH 22%, wind 21 mph. |

## Analyst Interpretation

- Headline: Fire-weather screening remains CONCERN for Sep 3 near Chimney Rock; PSPS is ELEVATED, and LPEA lists one localized outage with no fire or PSPS cause.
- Summary: Sep 3 near Chimney Rock is the peak from 3-5 PM: fire-weather HIGH 62/100, Red Flag POSSIBLE 50/100, and PSPS ELEVATED 40/100. LPEA lists one unplanned one-customer outage near Bayfield, but identifies no fire-weather or PSPS cause; no official COZ295 fire alert is active. A separate Flood Watch runs through midnight Sep 1, three fires remain listed, and no evacuation notice is detected.
- Uncertainty: These are rules-based screening estimates, not official warnings or calibrated PSPS probabilities; forecast, incident, alert, outage, and public-page data may change or lag.
- Evidence used: overall_status, weather_peaks, official_alerts, forecast_change, lpea_context, fire_posture, active_incidents, calibration
- This interpretation cannot change the deterministic tiers, scores, official alerts, or notification decision.

Changing drivers:
- Sep 3 worsened 24 points from PSPS LOW to ELEVATED, moving the peak back to Chimney Rock.
- Sep 5 worsened 10 points from PSPS LOW to ELEVATED, with the driver shifting to Durango.
- Sep 3 peaks with RH near 17%, wind/gust near 22 mph, and three near-threshold hours.
- LPEA now lists one localized one-customer outage near Bayfield with no identified fire-weather or PSPS cause.

What to watch next:
- Monitor Sep 3 near Chimney Rock from 3-5 PM for changes in RH, wind, and near-threshold duration.
- Track the localized Bayfield-area outage directly with LPEA without treating it as PSPS or fire evidence.
- Follow the separate NWS Flood Watch through midnight Sep 1 and check for updated official alerts.
- Continue monitoring current fires and official county evacuation feeds.

## Trend Intelligence

- Summary: Momentum is rising versus the prior run (Aug 30 at 5:21 PM MDT); forecast volatility is high and first WATCH-or-higher date is not present.
- Momentum: **Rising**
- Forecast volatility: **HIGH** (51/100)
- First WATCH-or-higher PSPS date: None
- Watch-date movement: No WATCH-or-higher PSPS dates in current or prior run.
- Method: compares current forecast evidence against prior local forecast history.

Notable changes:
- No WATCH-or-higher PSPS dates in current or prior run.
- Thu, Sep 3: worsening vs prior run; PSPS LOW -> ELEVATED; score +24, wind +8 mph, RH 0%, red-flag hours 0. Driver shifted to Chimney Rock / west county.
- Sat, Sep 5: worsening vs prior run; PSPS LOW -> ELEVATED; score +10, wind +8 mph, RH +2%, red-flag hours 0. Driver shifted to Durango / La Plata County.
- Fri, Sep 4: worsening vs prior run; PSPS LOW -> ELEVATED; score +4, wind +8 mph, RH +3%, red-flag hours 0. Driver shifted to Pagosa Springs.

## Public Analysis Export

- Summary: Highest LPEA PSPS concern is Thu, Sep 3 near Chimney Rock / west county (ELEVATED 40/100), driven by near-threshold wind/gust signal near 22 mph; near-threshold RH near 17%; 3 sampled hours are near red-flag thresholds. NIFC reports 3 current wildfires in Archuleta County.
- Trend: Momentum is rising versus the prior run (Aug 30 at 5:21 PM MDT); forecast volatility is high and first WATCH-or-higher date is not present.
- Confidence: **MEDIUM** (69/100)
- First WATCH-or-higher PSPS date: None
- PSPS peak: Thu, Sep 3 near Chimney Rock / west county at ELEVATED 40/100
- Red Flag peak: Thu, Sep 3 near Chimney Rock / west county at POSSIBLE 50/100
- Weather fire-potential peak: Thu, Sep 3 near Chimney Rock / west county at HIGH 62/100
- LPEA operational outage context: 1 active outage; 0 planned and 1 unplanned; 1 customer out. No fire-weather or PSPS cause is identified.
- Public JSON: `archuleta_red_flag_monitor/public_analysis_export.json`

What changed:
- No WATCH-or-higher PSPS dates in current or prior run.
- Thu, Sep 3: worsening vs prior run; PSPS LOW -> ELEVATED; score +24, wind +8 mph, RH 0%, red-flag hours 0. Driver shifted to Chimney Rock / west county.
- Sat, Sep 5: worsening vs prior run; PSPS LOW -> ELEVATED; score +10, wind +8 mph, RH +2%, red-flag hours 0. Driver shifted to Durango / La Plata County.
- Fri, Sep 4: worsening vs prior run; PSPS LOW -> ELEVATED; score +4, wind +8 mph, RH +3%, red-flag hours 0. Driver shifted to Pagosa Springs.

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
| Mon, Aug 31 | LOW | Ignacio / southeast La Plata County (LOW 16/100); Pagosa Springs (LOW 10/100); Arboles / southwest county (LOW 10/100) | Top weather score 16/100 at Ignacio / southeast La Plata County. Weather score 16/100: RH 40%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 0. |
| Tue, Sep 1 | ELEVATED | Pagosa Springs (ELEVATED 18/100); Arboles / southwest county (ELEVATED 18/100); Chimney Rock / west county (ELEVATED 18/100) | Top weather score 16/100 at Pagosa Springs. Weather score 16/100: RH 30%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 0. |
| Wed, Sep 2 | ELEVATED | Arboles / southwest county (ELEVATED 33/100); Durango / La Plata County (ELEVATED 27/100); Bayfield / east La Plata County (ELEVATED 27/100) | Top weather score 31/100 at Arboles / southwest county. Weather score 31/100: RH 21%, wind/gust 25 mph, red-flag hours 0, near-threshold hours 0. |
| Thu, Sep 3 | ELEVATED | Chimney Rock / west county (ELEVATED 40/100); Bayfield / east La Plata County (ELEVATED 33/100); Arboles / southwest county (ELEVATED 24/100) | Top weather score 38/100 at Chimney Rock / west county. Weather score 38/100: RH 17%, wind/gust 22 mph, red-flag hours 0, near-threshold hours 3. |
| Fri, Sep 4 | ELEVATED | Pagosa Springs (ELEVATED 18/100); Arboles / southwest county (ELEVATED 18/100); Durango / La Plata County (ELEVATED 18/100) | Top weather score 16/100 at Pagosa Springs. Weather score 16/100: RH 27%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 0. |
| Sat, Sep 5 | ELEVATED | Durango / La Plata County (ELEVATED 18/100); Chimney Rock / west county (LOW 16/100); Pagosa Springs (LOW 10/100) | Top weather score 16/100 at Durango / La Plata County. Weather score 16/100: RH 29%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 0. |
| Sun, Sep 6 | ELEVATED | Arboles / southwest county (ELEVATED 24/100); Durango / La Plata County (ELEVATED 18/100); Bayfield / east La Plata County (ELEVATED 18/100) | Top weather score 22/100 at Arboles / southwest county. Weather score 22/100: RH 22%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 0. |

## Area-Specific Outlook

| Area | Today | Peak this run | Highest-risk window |
| --- | --- | --- | --- |
| Chimney Rock | LOW 10/100 | Thu, Sep 3: ELEVATED 40/100 | 3 PM-5 PM local; 3 near/red-flag threshold hours. |
| Arboles | LOW 10/100 | Wed, Sep 2: ELEVATED 33/100 | Peak ingredients near 4 PM local; RH 21%, wind 25 mph. |
| Bayfield | LOW 10/100 | Thu, Sep 3: ELEVATED 33/100 | Peak ingredients near 4 PM local; RH 21%, wind 25 mph. |
| Durango | LOW 10/100 | Wed, Sep 2: ELEVATED 27/100 | Peak ingredients near 3 PM local; RH 25%, wind 25 mph. |
| Ignacio | LOW 16/100 | Wed, Sep 2: ELEVATED 25/100 | Peak ingredients near 4 PM local; RH 23%, wind 26 mph. |
| Chromo | LOW 10/100 | Wed, Sep 2: ELEVATED 24/100 | Peak ingredients near 4 PM local; RH 22%, wind 22 mph. |
| Pagosa Springs | LOW 10/100 | Tue, Sep 1: ELEVATED 18/100 | Peak ingredients near 4 PM local; RH 32%, wind 21 mph. |
| Piedra | LOW 10/100 | Wed, Sep 2: ELEVATED 18/100 | Peak ingredients near 4 PM local; RH 28%, wind 23 mph. |

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
- WATCH/LIKELY false-watch past days: 70
- Pending WATCH/LIKELY dates in current forecast: None
- Calibration source: manual PSPS event log plus forecast history from prior monitor runs.

### Red Flag / Fire Weather Calibration

- Summary: 3/3 official Red Flag / Fire Weather episodes had a pre-alert HIGH monitor signal; date-level result was 21/21. Episode-average lead time: 3.5 days.
- Official alert episodes logged: 3 (21 alert dates)
- Episode-level pre-alert HIGH hit rate: 100%
- Date-level pre-alert HIGH hit rate: 100%
- Episode-level average lead time: 3.5 days
- HIGH false-watch past days: 23
- Pending HIGH dates in current forecast: None
- Calibration source: official NWS Red Flag / Fire Weather alert dates plus forecast history from prior monitor runs.

## Official Weather Alerts

- Monitored NWS zones: COC007, COC067, COZ019, COZ022, COZ023, COZ295
- [Flood Watch](https://api.weather.gov/alerts/urn:oid:2.49.0.1.840.0.f7ff695e018105cca90d3b4c59e6816f865c6d8a.002.1): Flood Watch issued August 30 at 7:37PM MDT until September 1 at 12:00AM MDT by NWS Grand Junction CO; 2026-08-30T19:37:00-06:00 to 2026-09-01T00:00:00-06:00; zones COZ022, COZ023
- [Flood Watch](https://api.weather.gov/alerts/urn:oid:2.49.0.1.840.0.f7ff695e018105cca90d3b4c59e6816f865c6d8a.001.1): Flood Watch issued August 30 at 7:37PM MDT until September 1 at 12:00AM MDT by NWS Grand Junction CO; 2026-08-30T19:37:00-06:00 to 2026-09-01T00:00:00-06:00; zones COZ002, COZ003, COZ006, COZ007, COZ008, COZ009, COZ010, COZ011, COZ012, COZ013, COZ014, COZ017, COZ018, COZ019, COZ020, COZ021, UTZ022, UTZ025, UTZ027, UTZ028, UTZ029

## LPEA Power Signal

- Status: `operational_outage_active` - Official LPEA outage data indicates an operational outage; use as grid context, not PSPS/fire evidence unless LPEA identifies that cause.
- Meaning: Active source match means a monitored LPEA active/update source currently contains fire, outage, PSPS, or power-interruption keywords. Operational outages are shown separately and are not treated as PSPS/fire evidence unless the source text says so.
- Operational outage context: 1 active outage; 0 planned and 1 unplanned; 1 customer out. No fire-weather or PSPS cause is identified.
- Source coverage: 13 sources; 5/5 official social sources reachable
- Evidence quality: 0 operational, 4 active/update, 0 archive/context, 6 reference source matches.
- Operational outage source links: [310 S PEARL ST](https://outage.lpea.coop)
- Active/update source pages with matches: LPEA homepage (public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation, restoration); LPEA X (power outage, outage map, high winds, restore power); LPEA LinkedIn (wildfire, public safety power shutoff, psps, power shutoff, shutoff, deenergize)
- Distinct active/update signals: LPEA X (power outage, outage map, high winds, restore power); LPEA X (power outage, outage map, high winds, restore power); LPEA LinkedIn (wildfire, public safety power shutoff, psps, power shutoff, shutoff, deenergize); LinkedIn PSPS explainer post (wildfire, public safety power shutoff, psps, power shutoff, shutoff, deenergize)
- Example signal: ...ibrary! 1 2 537 LPEA @LaPlataElectric May 7, 2024 LPEA members are experiencing power outages in the Bayfield and Pagosa Springs areas. Approximately 200 meters are out and it is suspected that the high winds are...
- Reference/context hits: [LPEA outage center](https://lpea.coop/outage-center); [LPEA wildfire / public safety power shutoffs](https://lpea.coop/psps); [LPEA red flag outage impact page](https://lpea.coop/outages/red-flag-warnings-and-impact-outages-prioritizing-safety-our-members); [LPEA fire mitigation](https://lpea.coop/fire-mitigation); [LPEA latest news](https://lpea.coop/Posts)

**Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## Next 7 Days

| Date | Tier | Main reason | Worst sampled metrics |
| --- | --- | --- | --- |
| Mon, Aug 31 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 36%, wind/gust 18 mph, thunder 57%<br>Arboles / southwest county: RH 36%, wind/gust 20 mph, thunder 51%<br>Chimney Rock / west county: RH 33%, wind/gust 18 mph, thunder 56% |
| Tue, Sep 1 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 30%, wind/gust 21 mph, thunder 9%<br>Arboles / southwest county: RH 26%, wind/gust 22 mph, thunder 8%<br>Chimney Rock / west county: RH 24%, wind/gust 22 mph, thunder 8% |
| Wed, Sep 2 | ELEVATED | Arboles / southwest county: Elevated ingredient present: wind/gust forecast near 25 mph. | Arboles / southwest county: RH 21%, wind/gust 25 mph, thunder 1%<br>Durango / La Plata County: RH 25%, wind/gust 25 mph, thunder 4%<br>Bayfield / east La Plata County: RH 24%, wind/gust 28 mph, thunder 2% |
| Thu, Sep 3 | CONCERN | Chimney Rock / west county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Chimney Rock / west county: RH 17%, wind/gust 22 mph, thunder 4%<br>Bayfield / east La Plata County: RH 21%, wind/gust 25 mph, thunder 5% |
| Fri, Sep 4 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 27%, wind/gust 21 mph, thunder 34%<br>Arboles / southwest county: RH 23%, wind/gust 21 mph, thunder 23%<br>Chimney Rock / west county: RH 21%, wind/gust 20 mph, thunder 32% |
| Sat, Sep 5 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 28%, wind/gust 16 mph, thunder 36%<br>Arboles / southwest county: RH 23%, wind/gust 18 mph, thunder 24%<br>Chimney Rock / west county: RH 21%, wind/gust 18 mph, thunder 33% |
| Sun, Sep 6 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 28%, wind/gust 17 mph, thunder 27%<br>Arboles / southwest county: RH 22%, wind/gust 21 mph, thunder 21%<br>Chimney Rock / west county: RH 21%, wind/gust 20 mph, thunder 25% |

## Sample Point Status

- Pagosa Springs: COZ295 (matches), forecast zone COZ023, county zone COC007
- Arboles / southwest county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Chimney Rock / west county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Piedra / north county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Chromo / southeast county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Durango / La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Bayfield / east La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Ignacio / southeast La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
