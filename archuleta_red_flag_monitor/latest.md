# Archuleta Red Flag Risk Monitor

Generated: Jul 28, 2026 at 9:34 AM MDT (Pagosa Springs, CO local time)
Next update: Jul 28, 2026 at 5:20 PM MDT (Pagosa Springs, CO local time)
Date/time basis: Pagosa Springs, CO local time (America/Denver)
> **Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## At A Glance

- Fire-weather tier: **CONCERN**
- PSPS likelihood: **WATCH**
- PSPS likely dates: None
- PSPS watch dates: Mon, Aug 3
- Monitor heads-up recommended: **YES** - Send this monitor report because fire-weather screening tier is CONCERN; PSPS screening level is WATCH. This is not an official LPEA or NWS notice.
- HIGH dates: None
- CONCERN dates: Tue, Jul 28; Mon, Aug 3
- ELEVATED dates: Fri, Jul 31; Sat, Aug 1
- Official NWS Red Flag / Fire Weather alerts (COZ295): 0
- LPEA signal: `operational_outage_active` - Official LPEA outage data indicates an operational outage; use as grid context, not PSPS/fire evidence unless LPEA identifies that cause.
- LPEA source coverage: 13 sources; 5/5 official social sources reachable
- NWS discussion: No concerning fire-weather language found in latest GJT discussion.

## Decision Support

- Summary: Highest LPEA PSPS concern is Mon, Aug 3 near Arboles / southwest county (WATCH 50/100), driven by near-threshold wind/gust signal near 23 mph; red-flag RH near 15%; 3 sampled hours are near red-flag thresholds.
- Confidence: **HIGH** (77/100) - 8/8 sampled weather points available; 7/7 fire-posture sources reachable; official NWS alert zones checked; 13/13 LPEA public sources reachable; LPEA active/update sources checked; active LPEA operational outage context checked separately from PSPS scoring; no confirmed PSPS events logged yet for calibration
- Weather fire-potential peak: Mon, Aug 3: Durango / La Plata County HIGH 66/100
- Red Flag likelihood peak: Mon, Aug 3: Arboles / southwest county WATCH 60/100
- LPEA PSPS peak: Mon, Aug 3: Arboles / southwest county WATCH 50/100
- Method: rules-based decision support using public weather, fire-posture, and LPEA source signals; scores are screening estimates, not official or statistically calibrated probabilities.

| Date | Weather fire potential | Red Flag likelihood | LPEA PSPS | Main window |
| --- | --- | --- | --- | --- |
| Tue, Jul 28 | Arboles / southwest county: HIGH 55/100 | Arboles / southwest county: POSSIBLE 50/100 | Arboles / southwest county: ELEVATED 40/100 | 3 PM-5 PM local; 3 near/red-flag threshold hours. |
| Wed, Jul 29 | Durango / La Plata County: MODERATE 40/100 | Arboles / southwest county: LOW 16/100 | Arboles / southwest county: ELEVATED 30/100 | 3 PM-3 PM local; 1 near/red-flag threshold hour. |
| Thu, Jul 30 | Durango / La Plata County: LOW 32/100 | Arboles / southwest county: LOW 8/100 | Arboles / southwest county: ELEVATED 24/100 | Peak ingredients near 3 PM local; RH 20%, wind 21 mph. |
| Fri, Jul 31 | Chimney Rock / west county: MODERATE 48/100 | Chimney Rock / west county: LOW 25/100 | Chimney Rock / west county: ELEVATED 30/100 | Peak ingredients near 3 PM local; RH 15%, wind 16 mph. |
| Sat, Aug 1 | Ignacio / southeast La Plata County: MODERATE 36/100 | Ignacio / southeast La Plata County: LOW 25/100 | Ignacio / southeast La Plata County: ELEVATED 28/100 | Peak ingredients near 4 PM local; RH 18%, wind 17 mph. |
| Sun, Aug 2 | Durango / La Plata County: MODERATE 40/100 | Durango / La Plata County: LOW 8/100 | Durango / La Plata County: ELEVATED 26/100 | Peak ingredients near 4 PM local; RH 20%, wind 21 mph. |
| Mon, Aug 3 | Durango / La Plata County: HIGH 66/100 | Arboles / southwest county: WATCH 60/100 | Arboles / southwest county: WATCH 50/100 | 3 PM-5 PM local; 3 near/red-flag threshold hours. |

## Analyst Interpretation

- Headline: Fire-weather screening is CONCERN, with Aug 3 the peak WATCH screening date; no official NWS fire alert or confirmed PSPS is reported.
- Summary: Screening identifies CONCERN conditions on Jul 28 and Aug 3, with Aug 3 peaking near Arboles at WATCH for Red Flag likelihood and PSPS screening. Official NWS fire-alert count is zero; three active LPEA outages affect six customers, but the official outage data identifies no fire-weather or PSPS cause. Conditions are steady versus the prior run, and a monitor heads-up is recommended.
- Uncertainty: These are screening estimates, not official forecasts or calibrated PSPS probabilities; no confirmed LPEA PSPS events are available for calibration, and 44 past WATCH-or-higher days did not confirm an event.
- Evidence used: overall_status, weather_peaks, official_alerts, forecast_change, lpea_context, fire_posture, calibration
- This interpretation cannot change the deterministic tiers, scores, official alerts, or notification decision.

Changing drivers:
- Aug 3 combines RH near 15%, wind or gusts near 23 mph, and three near-threshold hours near Arboles.
- The first WATCH-or-higher PSPS screening date remains Aug 3, with no major day-level movement.
- Official fire posture reaches Stage 2 restrictions and HIGH fire danger in the monitored region.
- Three active LPEA outages are localized operational events with no identified fire-weather or PSPS cause.

What to watch next:
- Check official NWS alerts as Aug 3 approaches.
- Track whether Aug 3 wind and RH remain near screening thresholds.
- Monitor official LPEA updates for any explicit PSPS notice or outage-cause change.
- Reassess if the peak location shifts away from Arboles.

## Trend Intelligence

- Summary: Momentum is steady versus the prior run (Jul 28 at 9:32 AM MDT); forecast volatility is low and first WATCH-or-higher date is Mon, Aug 3.
- Momentum: **Steady**
- Forecast volatility: **LOW** (0/100)
- First WATCH-or-higher PSPS date: Mon, Aug 3
- Watch-date movement: First WATCH-or-higher PSPS date remains Mon, Aug 3.
- Method: compares current forecast evidence against prior local forecast history.

Notable changes:
- First WATCH-or-higher PSPS date remains Mon, Aug 3.
- No major day-level movement versus the prior run.

## Public Analysis Export

- Summary: Highest LPEA PSPS concern is Mon, Aug 3 near Arboles / southwest county (WATCH 50/100), driven by near-threshold wind/gust signal near 23 mph; red-flag RH near 15%; 3 sampled hours are near red-flag thresholds.
- Trend: Momentum is steady versus the prior run (Jul 28 at 9:32 AM MDT); forecast volatility is low and first WATCH-or-higher date is Mon, Aug 3.
- Confidence: **HIGH** (77/100)
- First WATCH-or-higher PSPS date: Mon, Aug 3
- PSPS peak: Mon, Aug 3 near Arboles / southwest county at WATCH 50/100
- Red Flag peak: Mon, Aug 3 near Arboles / southwest county at WATCH 60/100
- Weather fire-potential peak: Mon, Aug 3 near Durango / La Plata County at HIGH 66/100
- LPEA operational outage context: 3 active outages; 1 planned and 2 unplanned; 6 customers out. No fire-weather or PSPS cause is identified.
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
- Overall: **WATCH** - PSPS watch screening is present from forecast thresholds or direct LPEA shutoff language; monitor official LPEA and NWS updates.
- Likely PSPS watch dates: None
- PSPS watch dates: Mon, Aug 3
- LPEA signal basis: LPEA active/update source contains red-flag, wildfire, or power-interruption language.
- Note: This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

| Date | PSPS likelihood | Driver locations | Weather basis |
| --- | --- | --- | --- |
| Tue, Jul 28 | ELEVATED | Arboles / southwest county (ELEVATED 40/100); Durango / La Plata County (ELEVATED 26/100); Bayfield / east La Plata County (ELEVATED 26/100) | Top weather score 38/100 at Arboles / southwest county. Weather score 38/100: RH 17%, wind/gust 22 mph, red-flag hours 0, near-threshold hours 3. |
| Wed, Jul 29 | ELEVATED | Arboles / southwest county (ELEVATED 30/100); Durango / La Plata County (ELEVATED 26/100); Ignacio / southeast La Plata County (ELEVATED 26/100) | Top weather score 28/100 at Arboles / southwest county. Weather score 28/100: RH 18%, wind/gust 22 mph, red-flag hours 0, near-threshold hours 1. |
| Thu, Jul 30 | ELEVATED | Arboles / southwest county (ELEVATED 24/100); Durango / La Plata County (ELEVATED 20/100); Bayfield / east La Plata County (ELEVATED 20/100) | Top weather score 22/100 at Arboles / southwest county. Weather score 22/100: RH 20%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 0. |
| Fri, Jul 31 | ELEVATED | Chimney Rock / west county (ELEVATED 30/100); Arboles / southwest county (ELEVATED 28/100); Durango / La Plata County (ELEVATED 24/100) | Top weather score 26/100 at Arboles / southwest county. Weather score 26/100: RH 15%, wind/gust 16 mph, red-flag hours 0, near-threshold hours 0. |
| Sat, Aug 1 | ELEVATED | Ignacio / southeast La Plata County (ELEVATED 28/100); Arboles / southwest county (ELEVATED 26/100); Chimney Rock / west county (ELEVATED 24/100) | Top weather score 24/100 at Arboles / southwest county. Weather score 24/100: RH 17%, wind/gust 16 mph, red-flag hours 0, near-threshold hours 0. |
| Sun, Aug 2 | ELEVATED | Durango / La Plata County (ELEVATED 26/100); Bayfield / east La Plata County (ELEVATED 26/100); Ignacio / southeast La Plata County (ELEVATED 26/100) | Top weather score 22/100 at Durango / La Plata County. Weather score 22/100: RH 20%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 0. |
| Mon, Aug 3 | WATCH | Arboles / southwest county (WATCH 50/100); Durango / La Plata County (WATCH 46/100); Bayfield / east La Plata County (WATCH 46/100); Ignacio / southeast La Plata County (WATCH 46/100) | Top weather score 48/100 at Arboles / southwest county. Weather score 48/100: RH 15%, wind/gust 23 mph, red-flag hours 0, near-threshold hours 3. |

## Area-Specific Outlook

| Area | Today | Peak this run | Highest-risk window |
| --- | --- | --- | --- |
| Arboles | ELEVATED 40/100 | Mon, Aug 3: WATCH 50/100 | 3 PM-5 PM local; 3 near/red-flag threshold hours. |
| Durango | ELEVATED 26/100 | Mon, Aug 3: WATCH 46/100 | 3 PM-5 PM local; 3 near/red-flag threshold hours. |
| Bayfield | ELEVATED 26/100 | Mon, Aug 3: WATCH 46/100 | 3 PM-4 PM local; 2 near/red-flag threshold hours. |
| Ignacio | ELEVATED 26/100 | Mon, Aug 3: WATCH 46/100 | 3 PM-5 PM local; 3 near/red-flag threshold hours. |
| Chimney Rock | ELEVATED 24/100 | Fri, Jul 31: ELEVATED 30/100 | Peak ingredients near 3 PM local; RH 15%, wind 16 mph. |
| Pagosa Springs | ELEVATED 18/100 | Tue, Jul 28: ELEVATED 18/100 | Peak ingredients near 3 PM local; RH 21%, wind 16 mph. |
| Piedra | LOW 12/100 | Fri, Jul 31: ELEVATED 18/100 | Peak ingredients near 12 AM local; RH 65%, wind 18 mph. |
| Chromo | ELEVATED 18/100 | Tue, Jul 28: ELEVATED 18/100 | Peak ingredients near 4 PM local; RH 22%, wind 15 mph. |

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
- Pending WATCH/LIKELY dates in current forecast: Mon, Aug 3
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
- Operational outage context: 3 active outages; 1 planned and 2 unplanned; 6 customers out. No fire-weather or PSPS cause is identified.
- Source coverage: 13 sources; 5/5 official social sources reachable
- Evidence quality: 0 operational, 4 active/update, 0 archive/context, 6 reference source matches.
- Operational outage source links: [2340 W 2ND AVE](https://outage.lpea.coop); [2016 Crestview Dr](https://outage.lpea.coop); [10893 CR 141](https://outage.lpea.coop)
- Active/update source pages with matches: LPEA homepage (public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation, restoration); LPEA X (power outage, outage map, high winds, restore power); LPEA LinkedIn (wildfire, fire mitigation)
- Distinct active/update signals: LPEA X (power outage, outage map, high winds, restore power); LPEA X (power outage, outage map, high winds, restore power); LPEA LinkedIn (wildfire, fire mitigation); LPEA LinkedIn (wildfire, fire mitigation)
- Example signal: ...ibrary! 1 2 513 LPEA @LaPlataElectric May 7, 2024 LPEA members are experiencing power outages in the Bayfield and Pagosa Springs areas. Approximately 200 meters are out and it is suspected that the high winds are...
- Reference/context hits: [LPEA outage center](https://lpea.coop/outage-center); [LPEA wildfire / public safety power shutoffs](https://lpea.coop/psps); [LPEA red flag outage impact page](https://lpea.coop/outages/red-flag-warnings-and-impact-outages-prioritizing-safety-our-members); [LPEA fire mitigation](https://lpea.coop/fire-mitigation); [LPEA latest news](https://lpea.coop/Posts)

**Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## Next 7 Days

| Date | Tier | Main reason | Worst sampled metrics |
| --- | --- | --- | --- |
| Tue, Jul 28 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 17%, wind/gust 22 mph, thunder 17% |
| Wed, Jul 29 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 24%, wind/gust 18 mph, thunder 52%<br>Arboles / southwest county: RH 18%, wind/gust 22 mph, thunder 38%<br>Chimney Rock / west county: RH 19%, wind/gust 20 mph, thunder 44% |
| Thu, Jul 30 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 27%, wind/gust 17 mph, thunder 52%<br>Arboles / southwest county: RH 20%, wind/gust 21 mph, thunder 22%<br>Chimney Rock / west county: RH 20%, wind/gust 18 mph, thunder 35% |
| Fri, Jul 31 | ELEVATED | Arboles / southwest county: Elevated ingredient present: very low RH forecast near 15%. | Arboles / southwest county: RH 15%, wind/gust 16 mph, thunder 15%<br>Chimney Rock / west county: RH 15%, wind/gust 16 mph, thunder 13% |
| Sat, Aug 1 | ELEVATED | Arboles / southwest county: Elevated ingredient present: dry-thunder probability reaches 16%. | Arboles / southwest county: RH 17%, wind/gust 16 mph, thunder 16%<br>Ignacio / southeast La Plata County: RH 18%, wind/gust 17 mph, thunder 16% |
| Sun, Aug 2 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 23%, wind/gust 16 mph, thunder 35%<br>Arboles / southwest county: RH 17%, wind/gust 18 mph, thunder 13%<br>Chimney Rock / west county: RH 18%, wind/gust 18 mph, thunder 28% |
| Mon, Aug 3 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 15%, wind/gust 23 mph, thunder 18%<br>Chimney Rock / west county: RH 15%, wind/gust 20 mph, thunder 27%<br>Durango / La Plata County: RH 17%, wind/gust 22 mph, thunder 18% |

## Sample Point Status

- Pagosa Springs: COZ295 (matches), forecast zone COZ023, county zone COC007
- Arboles / southwest county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Chimney Rock / west county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Piedra / north county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Chromo / southeast county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Durango / La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Bayfield / east La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Ignacio / southeast La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
