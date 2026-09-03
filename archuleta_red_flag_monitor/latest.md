# Archuleta County fire-weather monitor

Generated: Sep 3, 2026 at 5:38 AM MDT (Pagosa Springs, CO local time)
Next update: Sep 3, 2026 at 5:20 PM MDT (Pagosa Springs, CO local time)
Date/time basis: Pagosa Springs, CO local time (America/Denver)
> **Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## At A Glance

- Fire-weather tier: **GREEN**
- PSPS likelihood: **ELEVATED**
- PSPS likely dates: None
- PSPS watch dates: None
- Monitor heads-up recommended: **NO** - No material alert, fire, evacuation, significant outage, CONCERN/HIGH weather, or WATCH/LIKELY PSPS signal is present.
- HIGH dates: None
- CONCERN dates: None
- ELEVATED dates: None
- Official NWS Red Flag / Fire Weather alerts (COZ295): 0
- LPEA signal: `operational_outage_active` - Official LPEA outage data indicates an operational outage; use as grid context, not PSPS/fire evidence unless LPEA identifies that cause.
- LPEA source coverage: 13 sources; 5/5 official social sources reachable
- Current Archuleta County wildfires: 1
- Official evacuation notices: No current evacuation order or warning detected in the checked official county feeds.
- NWS discussion: No concerning fire-weather language found in latest GJT discussion.

## Decision Support

- Summary: Highest LPEA PSPS concern is Thu, Sep 3 near Arboles / southwest county (ELEVATED 24/100), driven by near-threshold wind/gust signal near 22 mph; dry RH near 20%; Official fire-posture context for Arboles / southwest county is elevated (STAGE 1; fire danger UNKNOWN), used as a small supporting modifier. NIFC reports 1 current wildfire in Archuleta County.
- Confidence: **HIGH** (77/100) - 8/8 sampled weather points available; 7/7 fire-posture sources reachable; official NWS alert zones checked; 13/13 LPEA public sources reachable; LPEA active/update sources checked; active LPEA operational outage context checked separately from PSPS scoring; authoritative NIFC current-incident feed checked for Archuleta County; official Archuleta County evacuation feeds checked; no confirmed PSPS events logged yet for calibration
- Weather fire-potential peak: Thu, Sep 3: Chimney Rock / west county LOW 34/100
- Red Flag likelihood peak: Thu, Sep 3: Arboles / southwest county LOW 8/100
- LPEA PSPS peak: Thu, Sep 3: Arboles / southwest county ELEVATED 24/100
- Method: rules-based decision support using public weather, fire-posture, and LPEA source signals; scores are screening estimates, not official or statistically calibrated probabilities.

| Date | Weather fire potential | Red Flag likelihood | LPEA PSPS | Main window |
| --- | --- | --- | --- | --- |
| Thu, Sep 3 | Chimney Rock / west county: LOW 34/100 | Arboles / southwest county: LOW 8/100 | Arboles / southwest county: ELEVATED 24/100 | Peak ingredients near 3 PM local; RH 23%, wind 22 mph. |
| Fri, Sep 4 | Pagosa Springs: LOW 26/100 | Pagosa Springs: LOW 8/100 | Pagosa Springs: ELEVATED 18/100 | Peak ingredients near 4 PM local; RH 34%, wind 21 mph. |
| Sat, Sep 5 | Chimney Rock / west county: LOW 34/100 | Arboles / southwest county: LOW 8/100 | Arboles / southwest county: ELEVATED 24/100 | Peak ingredients near 5 PM local; RH 22%, wind 22 mph. |
| Sun, Sep 6 | Pagosa Springs: LOW 26/100 | Pagosa Springs: LOW 8/100 | Pagosa Springs: ELEVATED 18/100 | Peak ingredients near 4 PM local; RH 30%, wind 21 mph. |
| Mon, Sep 7 | Pagosa Springs: LOW 26/100 | Pagosa Springs: LOW 8/100 | Pagosa Springs: ELEVATED 18/100 | Peak ingredients near 3 PM local; RH 38%, wind 22 mph. |
| Tue, Sep 8 | Durango / La Plata County: LOW 26/100 | Arboles / southwest county: LOW 8/100 | Arboles / southwest county: ELEVATED 18/100 | Peak ingredients near 4 PM local; RH 28%, wind 21 mph. |
| Wed, Sep 9 | Durango / La Plata County: LOW 26/100 | Arboles / southwest county: LOW 8/100 | Arboles / southwest county: ELEVATED 18/100 | Peak ingredients near 4 PM local; RH 32%, wind 21 mph. |

## Analyst Interpretation

- Headline: Fire-weather screening remains GREEN; LPEA lists a one-customer outage near Chromo, with no fire or PSPS cause identified.
- Summary: Sep 3 remains the screening peak: LOW fire potential 34/100 near Chimney Rock, LOW Red Flag likelihood 8/100 and ELEVATED PSPS screening 24/100 near Arboles, with no WATCH-or-higher date. There are no active official COZ295 fire alerts; LPEA lists one customer out near Chromo without a stated cause or restoration estimate, not evidence of a PSPS. NIFC still lists Swiss Roll at 1.5 acres with containment unreported, and no evacuation notice was detected in checked county feeds.
- Uncertainty: Scores are unofficial screening estimates, not calibrated PSPS probabilities; source reports can lag, and GREEN does not override fire restrictions or evacuation instructions.
- Evidence used: overall_status, weather_peaks, official_alerts, forecast_change, lpea_context, fire_posture, active_incidents, calibration
- This interpretation cannot change the deterministic tiers, scores, official alerts, or notification decision.

Changing drivers:
- Weather screening remains GREEN with no major day-level movement; forecast volatility is LOW at 6/100.
- LPEA now lists a localized, unplanned outage affecting one customer near Chromo; no cause or restoration estimate is provided.
- Swiss Roll remains listed at 1.5 acres, with containment unreported and its incident record last updated Sep 2.
- Stage 1 restrictions and HIGH official fire-danger context remain relevant despite GREEN weather screening.

What to watch next:
- Check LPEA for restoration and any stated outage cause; keep operational outages separate from PSPS estimates.
- Monitor afternoon wind and humidity updates near Arboles and Chimney Rock.
- Check Swiss Roll incident updates and official county evacuation notices; unreported containment is unknown, not zero.
- Verify restrictions with the responsible jurisdiction; GREEN screening is not an all-clear for burning.

## Trend Intelligence

- Summary: Momentum is steady versus the prior run (Sep 2 at 5:36 PM MDT); forecast volatility is low and first WATCH-or-higher date is not present.
- Momentum: **Steady**
- Forecast volatility: **LOW** (6/100)
- First WATCH-or-higher PSPS date: None
- Watch-date movement: No WATCH-or-higher PSPS dates in current or prior run.
- Method: compares current forecast evidence against prior local forecast history.

Notable changes:
- No WATCH-or-higher PSPS dates in current or prior run.
- No major day-level movement versus the prior run.

## Public Analysis Export

- Summary: Highest LPEA PSPS concern is Thu, Sep 3 near Arboles / southwest county (ELEVATED 24/100), driven by near-threshold wind/gust signal near 22 mph; dry RH near 20%; Official fire-posture context for Arboles / southwest county is elevated (STAGE 1; fire danger UNKNOWN), used as a small supporting modifier. NIFC reports 1 current wildfire in Archuleta County.
- Trend: Momentum is steady versus the prior run (Sep 2 at 5:36 PM MDT); forecast volatility is low and first WATCH-or-higher date is not present.
- Confidence: **HIGH** (77/100)
- First WATCH-or-higher PSPS date: None
- PSPS peak: Thu, Sep 3 near Arboles / southwest county at ELEVATED 24/100
- Red Flag peak: Thu, Sep 3 near Arboles / southwest county at LOW 8/100
- Weather fire-potential peak: Thu, Sep 3 near Chimney Rock / west county at LOW 34/100
- LPEA operational outage context: 1 active outage; 0 planned and 1 unplanned; 1 customer out. No fire-weather or PSPS cause is identified.
- Public JSON: `archuleta_red_flag_monitor/public_analysis_export.json`

What changed:
- No WATCH-or-higher PSPS dates in current or prior run.
- No major day-level movement versus the prior run.

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
| Thu, Sep 3 | ELEVATED | Arboles / southwest county (ELEVATED 24/100); Chimney Rock / west county (ELEVATED 24/100); Pagosa Springs (ELEVATED 18/100) | Top weather score 22/100 at Arboles / southwest county. Weather score 22/100: RH 20%, wind/gust 22 mph, red-flag hours 0, near-threshold hours 0. |
| Fri, Sep 4 | ELEVATED | Pagosa Springs (ELEVATED 18/100); Arboles / southwest county (ELEVATED 18/100); Chimney Rock / west county (ELEVATED 18/100) | Top weather score 16/100 at Pagosa Springs. Weather score 16/100: RH 31%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 0. |
| Sat, Sep 5 | ELEVATED | Arboles / southwest county (ELEVATED 24/100); Chimney Rock / west county (ELEVATED 24/100); Durango / La Plata County (ELEVATED 18/100) | Top weather score 22/100 at Arboles / southwest county. Weather score 22/100: RH 21%, wind/gust 22 mph, red-flag hours 0, near-threshold hours 0. |
| Sun, Sep 6 | ELEVATED | Pagosa Springs (ELEVATED 18/100); Arboles / southwest county (ELEVATED 18/100); Chimney Rock / west county (ELEVATED 18/100) | Top weather score 16/100 at Pagosa Springs. Weather score 16/100: RH 29%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 0. |
| Mon, Sep 7 | ELEVATED | Pagosa Springs (ELEVATED 18/100); Arboles / southwest county (ELEVATED 18/100); Chimney Rock / west county (ELEVATED 18/100) | Top weather score 16/100 at Pagosa Springs. Weather score 16/100: RH 38%, wind/gust 22 mph, red-flag hours 0, near-threshold hours 0. |
| Tue, Sep 8 | ELEVATED | Arboles / southwest county (ELEVATED 18/100); Durango / La Plata County (ELEVATED 18/100); Bayfield / east La Plata County (ELEVATED 18/100) | Top weather score 16/100 at Arboles / southwest county. Weather score 16/100: RH 28%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 0. |
| Wed, Sep 9 | ELEVATED | Arboles / southwest county (ELEVATED 18/100); Durango / La Plata County (ELEVATED 18/100); Bayfield / east La Plata County (ELEVATED 18/100) | Top weather score 16/100 at Arboles / southwest county. Weather score 16/100: RH 32%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 0. |

## Area-Specific Outlook

| Area | Today | Peak this run | Highest-risk window |
| --- | --- | --- | --- |
| Arboles | ELEVATED 24/100 | Thu, Sep 3: ELEVATED 24/100 | Peak ingredients near 3 PM local; RH 23%, wind 22 mph. |
| Chimney Rock | ELEVATED 24/100 | Thu, Sep 3: ELEVATED 24/100 | Peak ingredients near 3 PM local; RH 21%, wind 22 mph. |
| Pagosa Springs | ELEVATED 18/100 | Thu, Sep 3: ELEVATED 18/100 | Peak ingredients near 3 PM local; RH 27%, wind 22 mph. |
| Piedra | ELEVATED 18/100 | Thu, Sep 3: ELEVATED 18/100 | Peak ingredients near 4 PM local; RH 30%, wind 21 mph. |
| Durango | ELEVATED 18/100 | Thu, Sep 3: ELEVATED 18/100 | Peak ingredients near 3 PM local; RH 28%, wind 23 mph. |
| Bayfield | ELEVATED 18/100 | Thu, Sep 3: ELEVATED 18/100 | Peak ingredients near 3 PM local; RH 26%, wind 23 mph. |
| Ignacio | LOW 16/100 | Thu, Sep 3: LOW 16/100 | Peak ingredients near 3 PM local; RH 25%, wind 23 mph. |
| Chromo | LOW 10/100 | Thu, Sep 3: LOW 10/100 | Peak ingredients near 3 PM local; RH 24%, wind 20 mph. |

## Current Fires + Evacuations

- Incident summary: 1 current wildfire reported in Archuleta County; no current evacuation notice detected in checked county feeds.
- Evacuation status: **NONE DETECTED** - No current evacuation order or warning detected in the checked official county feeds.
- Safety note: Current incidents and evacuation notices are operational context. They do not raise PSPS scores by themselves; follow official evacuation instructions immediately.

### Current NIFC Incidents

| Incident | Type | Size | Containment | Nearest monitored area | Updated |
| --- | --- | --- | --- | --- | --- |
| Swiss Roll | Wildfire | 1.50 acres | Not reported | Pagosa Springs (14.6 mi) | Sep 2 at 8:40 AM MDT |

Official links: [NIFC map](https://www.nifc.gov/fire-information/maps), [Archuleta County fire updates](https://sheriff.archuletacounty.gov/divisions/emergency-operations/fire-updates-and-information/), [County alerts](https://nixle.us/archuleta-county-office-of-emergency-management-aux/), [Watch Duty](https://app.watchduty.org/)

## Fire Posture + Restrictions

- Summary: 3 official sources indicate fire restrictions or staged restrictions.
- Max restriction stage detected: STAGE 1
- Max fire danger detected: HIGH
- Sources reachable: 7/7
- Note: Official-source status check only; verify restrictions and burn decisions with the responsible jurisdiction.

| Jurisdiction | Restrictions | Fire danger | Source |
| --- | --- | --- | --- |
| Archuleta County | STAGE 1 | UNKNOWN | [Archuleta County Sheriff fire updates](https://sheriff.archuletacounty.gov/divisions/emergency-operations/fire-updates-and-information/) |
| Pagosa Springs | STAGE 1 | UNKNOWN | [Town of Pagosa Springs](https://www.pagosasprings.co.gov/) |
| San Juan National Forest | STAGE 1 | HIGH | [San Juan National Forest fire](https://www.fs.usda.gov/r02/sanjuan/fire) |
| BLM Tres Rios | UNKNOWN | UNKNOWN | [BLM Tres Rios Field Office](https://www.blm.gov/office/tres-rios-field-office) |
| La Plata County / Durango Fire | NONE | UNKNOWN | [Durango Fire & Rescue fire conditions](https://www.durangofire.org/fire-conditions) |
| Durango | UNKNOWN | UNKNOWN | [City of Durango](https://www.durangoco.gov/) |
| Southern Ute / Ignacio | UNKNOWN | UNKNOWN | [Southern Ute Indian Tribe](https://www.southernute-nsn.gov/) |

## Forecast Calibration

### PSPS Calibration

- Summary: No confirmed LPEA PSPS events logged yet; calibration will start once events are added.
- Confirmed PSPS events logged: 0
- Candidate/unconfirmed events logged: 0
- WATCH/LIKELY false-watch past days: 72
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
- Example signal: ...ibrary! 1 2 537 LPEA @LaPlataElectric May 7, 2024 LPEA members are experiencing power outages in the Bayfield and Pagosa Springs areas. Approximately 200 meters are out and it is suspected that the high winds are...
- Reference/context hits: [LPEA outage center](https://lpea.coop/outage-center); [LPEA wildfire / public safety power shutoffs](https://lpea.coop/psps); [LPEA red flag outage impact page](https://lpea.coop/outages/red-flag-warnings-and-impact-outages-prioritizing-safety-our-members); [LPEA fire mitigation](https://lpea.coop/fire-mitigation); [LPEA latest news](https://lpea.coop/Posts)

**Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## Next 7 Days

| Date | Tier | Main reason | Worst sampled metrics |
| --- | --- | --- | --- |
| Thu, Sep 3 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 26%, wind/gust 22 mph, thunder 7%<br>Arboles / southwest county: RH 20%, wind/gust 22 mph, thunder 7%<br>Chimney Rock / west county: RH 21%, wind/gust 22 mph, thunder 7% |
| Fri, Sep 4 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 31%, wind/gust 21 mph, thunder 25%<br>Arboles / southwest county: RH 24%, wind/gust 21 mph, thunder 21%<br>Chimney Rock / west county: RH 26%, wind/gust 21 mph, thunder 22% |
| Sat, Sep 5 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 26%, wind/gust 18 mph, thunder 20%<br>Arboles / southwest county: RH 21%, wind/gust 22 mph, thunder 5%<br>Chimney Rock / west county: RH 21%, wind/gust 21 mph, thunder 11% |
| Sun, Sep 6 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 29%, wind/gust 21 mph, thunder 37%<br>Arboles / southwest county: RH 25%, wind/gust 21 mph, thunder 33%<br>Chimney Rock / west county: RH 24%, wind/gust 22 mph, thunder 34% |
| Mon, Sep 7 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 38%, wind/gust 22 mph, thunder 58%<br>Arboles / southwest county: RH 33%, wind/gust 23 mph, thunder 44%<br>Chimney Rock / west county: RH 34%, wind/gust 22 mph, thunder 54% |
| Tue, Sep 8 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 33%, wind/gust 20 mph, thunder 41%<br>Arboles / southwest county: RH 28%, wind/gust 21 mph, thunder 34%<br>Chimney Rock / west county: RH 27%, wind/gust 20 mph, thunder 34% |
| Wed, Sep 9 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 36%, wind/gust 18 mph, thunder 51%<br>Arboles / southwest county: RH 32%, wind/gust 21 mph, thunder 40%<br>Chimney Rock / west county: RH 30%, wind/gust 20 mph, thunder 47% |

## Sample Point Status

- Pagosa Springs: COZ295 (matches), forecast zone COZ023, county zone COC007
- Arboles / southwest county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Chimney Rock / west county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Piedra / north county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Chromo / southeast county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Durango / La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Bayfield / east La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Ignacio / southeast La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
