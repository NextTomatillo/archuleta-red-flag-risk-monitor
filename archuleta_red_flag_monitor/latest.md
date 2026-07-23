# Archuleta Red Flag Risk Monitor

Generated: Jul 22, 2026 at 5:53 PM MDT (Pagosa Springs, CO local time)
Next update: Jul 23, 2026 at 5:20 AM MDT (Pagosa Springs, CO local time)
Date/time basis: Pagosa Springs, CO local time (America/Denver)
> **Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## At A Glance

- Fire-weather tier: **GREEN**
- PSPS likelihood: **LOW**
- PSPS likely dates: None
- PSPS watch dates: None
- Monitor heads-up recommended: **NO** - No material alert, significant outage, CONCERN/HIGH weather, or WATCH/LIKELY PSPS signal is present.
- HIGH dates: None
- CONCERN dates: None
- ELEVATED dates: None
- Official NWS Red Flag / Fire Weather alerts (COZ295): 0
- LPEA signal: `active_keyword_match` - LPEA active/update sources contained power-interruption keywords; review source before treating as confirmed outage intent.
- LPEA source coverage: 13 sources; 5/5 official social sources reachable
- NWS discussion: No concerning fire-weather language found in latest GJT discussion.

## Decision Support

- Summary: Highest LPEA PSPS concern is Thu, Jul 23 near Pagosa Springs (LOW 12/100), driven by breezy wind/gust signal near 17 mph; Official fire-posture context for Pagosa Springs is escalated (STAGE 2; fire danger HIGH); it adds a small preparedness modifier but does not create a PSPS WATCH by itself.
- Confidence: **MEDIUM** (69/100) - 8/8 sampled weather points available; 7/7 fire-posture sources reachable; official NWS alert zones checked; 13/13 LPEA public sources reachable; LPEA active/update sources checked; forecast changed substantially versus prior run; no confirmed PSPS events logged yet for calibration
- Weather fire-potential peak: Wed, Jul 22: Pagosa Springs LOW 20/100
- Red Flag likelihood peak: Thu, Jul 23: Pagosa Springs LOW 0/100
- LPEA PSPS peak: Thu, Jul 23: Pagosa Springs LOW 12/100
- Method: rules-based decision support using public weather, fire-posture, and LPEA source signals; scores are screening estimates, not official or statistically calibrated probabilities.

| Date | Weather fire potential | Red Flag likelihood | LPEA PSPS | Main window |
| --- | --- | --- | --- | --- |
| Wed, Jul 22 | Pagosa Springs: LOW 20/100 | Pagosa Springs: LOW 0/100 | Pagosa Springs: LOW 4/100 | Peak ingredients near 6 PM local; RH 42%, wind 12 mph. |
| Thu, Jul 23 | Pagosa Springs: LOW 20/100 | Pagosa Springs: LOW 0/100 | Pagosa Springs: LOW 12/100 | Peak ingredients near 3 PM local; RH 44%, wind 17 mph. |
| Fri, Jul 24 | Pagosa Springs: LOW 20/100 | Arboles / southwest county: LOW 0/100 | Arboles / southwest county: LOW 12/100 | Peak ingredients near 3 PM local; RH 27%, wind 17 mph. |
| Sat, Jul 25 | Pagosa Springs: LOW 20/100 | Arboles / southwest county: LOW 0/100 | Arboles / southwest county: LOW 12/100 | Peak ingredients near 3 PM local; RH 24%, wind 15 mph. |
| Sun, Jul 26 | Pagosa Springs: LOW 20/100 | Arboles / southwest county: LOW 0/100 | Arboles / southwest county: LOW 12/100 | Peak ingredients near 3 PM local; RH 24%, wind 15 mph. |
| Mon, Jul 27 | Pagosa Springs: LOW 20/100 | Arboles / southwest county: LOW 0/100 | Arboles / southwest county: LOW 12/100 | Peak ingredients near 3 PM local; RH 26%, wind 16 mph. |
| Tue, Jul 28 | Pagosa Springs: LOW 20/100 | Arboles / southwest county: LOW 0/100 | Arboles / southwest county: LOW 12/100 | Peak ingredients near 3 PM local; RH 27%, wind 16 mph. |

## Analyst Interpretation

- Headline: Fire-weather risk is GREEN, with LOW PSPS screening and no official COZ295 fire alert or active LPEA outage.
- Summary: No HIGH or CONCERN fire-weather dates are identified, and the highest PSPS screening estimate is LOW 12/100 on Jul 23 near Pagosa Springs. Official sources show zero COZ295 fire alerts and no active LPEA operational outage; the LPEA keyword match is contextual and does not confirm outage or shutoff intent. Stage 2 restrictions and HIGH fire-danger posture support continued preparedness.
- Uncertainty: These rules-based screening scores are not official or statistically calibrated probabilities, and no confirmed LPEA PSPS events have been logged for calibration.
- Evidence used: overall_status, weather_peaks, official_alerts, forecast_change, lpea_context, fire_posture, calibration
- This interpretation cannot change the deterministic tiers, scores, official alerts, or notification decision.

Changing drivers:
- Overall PSPS screening eased from ELEVATED to LOW versus the prior run.
- The Jul 23 screening score fell by 8 points as wind eased by 2 mph and relative humidity rose by 2 percentage points.
- Stage 2 restrictions and HIGH official fire-danger posture remain preparedness context, but do not create a PSPS WATCH.
- An LPEA keyword match remains present, while the official outage viewer reports no active outages.

What to watch next:
- Recheck Jul 23 wind and relative-humidity trends.
- Confirm whether the LPEA keyword match remains general wildfire-mitigation context.
- Watch for any new official COZ295 fire alert or LPEA operational outage.
- Track whether the highest-risk location shifts in the next run.

## Trend Intelligence

- Summary: Momentum is easing versus the prior run (Jul 21 at 7:15 PM MDT); forecast volatility is high and first WATCH-or-higher date is not present.
- Momentum: **Easing**
- Forecast volatility: **HIGH** (45/100)
- First WATCH-or-higher PSPS date: None
- Watch-date movement: No WATCH-or-higher PSPS dates in current or prior run.
- Method: compares current forecast evidence against prior local forecast history.

Notable changes:
- No WATCH-or-higher PSPS dates in current or prior run.
- Overall PSPS likelihood changed from ELEVATED to LOW.
- Thu, Jul 23: easing vs prior run; PSPS ELEVATED -> LOW; score -8, wind -2 mph, RH +2%, red-flag hours 0. Driver shifted to Pagosa Springs.
- Sun, Jul 26: easing vs prior run; PSPS ELEVATED -> LOW; score -6, wind -2 mph, RH +2%, red-flag hours 0.
- Sat, Jul 25: easing vs prior run; PSPS ELEVATED -> LOW; score -6, wind -1 mph, RH +1%, red-flag hours 0. Driver shifted to Arboles / southwest county.
- Mon, Jul 27: easing vs prior run; PSPS ELEVATED -> LOW; score -6, wind 0 mph, RH +2%, red-flag hours 0. Driver shifted to Arboles / southwest county.

## Public Analysis Export

- Summary: Highest LPEA PSPS concern is Thu, Jul 23 near Pagosa Springs (LOW 12/100), driven by breezy wind/gust signal near 17 mph; Official fire-posture context for Pagosa Springs is escalated (STAGE 2; fire danger HIGH); it adds a small preparedness modifier but does not create a PSPS WATCH by itself.
- Trend: Momentum is easing versus the prior run (Jul 21 at 7:15 PM MDT); forecast volatility is high and first WATCH-or-higher date is not present.
- Confidence: **MEDIUM** (69/100)
- First WATCH-or-higher PSPS date: None
- PSPS peak: Thu, Jul 23 near Pagosa Springs at LOW 12/100
- Red Flag peak: Thu, Jul 23 near Pagosa Springs at LOW 0/100
- Weather fire-potential peak: Wed, Jul 22 near Pagosa Springs at LOW 20/100
- LPEA operational outage context: No active outages are listed by the official LPEA outage viewer.
- Public JSON: `archuleta_red_flag_monitor/public_analysis_export.json`

What changed:
- No WATCH-or-higher PSPS dates in current or prior run.
- Overall PSPS likelihood changed from ELEVATED to LOW.
- Thu, Jul 23: easing vs prior run; PSPS ELEVATED -> LOW; score -8, wind -2 mph, RH +2%, red-flag hours 0. Driver shifted to Pagosa Springs.
- Sun, Jul 26: easing vs prior run; PSPS ELEVATED -> LOW; score -6, wind -2 mph, RH +2%, red-flag hours 0.
- Sat, Jul 25: easing vs prior run; PSPS ELEVATED -> LOW; score -6, wind -1 mph, RH +1%, red-flag hours 0. Driver shifted to Arboles / southwest county.
- Mon, Jul 27: easing vs prior run; PSPS ELEVATED -> LOW; score -6, wind 0 mph, RH +2%, red-flag hours 0. Driver shifted to Arboles / southwest county.

What to watch next:
- Check whether the largest day-level changes line up with wind/RH movement or public-source context.
- Check whether the LPEA active match is still a broad red-flag banner rather than direct PSPS/outage intent.
- Watch whether the highest-risk locations remain consistent across runs or the driver area is moving.
- If a PSPS occurs, log the confirmed date, location, and source so future hit-rate scoring can improve.

## PSPS Likelihood

- **PSPS means Public Safety Power Shutoff:** a planned, safety-related power shutoff LPEA may use during dangerous fire-weather conditions to reduce wildfire ignition risk. See [LPEA PSPS guidance](https://lpea.coop/psps) and the [LPEA outage center](https://lpea.coop/outage-center); if power is out, also check the [LPEA outage map](https://outage.lpea.coop).
- Overall: **LOW** - PSPS likelihood is low based on current monitor inputs.
- Likely PSPS watch dates: None
- PSPS watch dates: None
- LPEA signal basis: LPEA active/update source contains red-flag, wildfire, or power-interruption language.
- Note: This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

| Date | PSPS likelihood | Driver locations | Weather basis |
| --- | --- | --- | --- |
| Wed, Jul 22 | LOW | Pagosa Springs (LOW 4/100); Arboles / southwest county (LOW 4/100); Chimney Rock / west county (LOW 4/100) | Top weather score 0/100 at Pagosa Springs. Weather score 0/100: RH 36%, wind/gust 12 mph, red-flag hours 0, near-threshold hours 0. |
| Thu, Jul 23 | LOW | Pagosa Springs (LOW 12/100); Arboles / southwest county (LOW 12/100); Chimney Rock / west county (LOW 12/100) | Top weather score 8/100 at Pagosa Springs. Weather score 8/100: RH 43%, wind/gust 17 mph, red-flag hours 0, near-threshold hours 0. |
| Fri, Jul 24 | LOW | Arboles / southwest county (LOW 12/100); Chimney Rock / west county (LOW 12/100); Durango / La Plata County (LOW 12/100) | Top weather score 8/100 at Arboles / southwest county. Weather score 8/100: RH 27%, wind/gust 17 mph, red-flag hours 0, near-threshold hours 0. |
| Sat, Jul 25 | LOW | Arboles / southwest county (LOW 12/100); Chimney Rock / west county (LOW 12/100); Durango / La Plata County (LOW 12/100) | Top weather score 8/100 at Arboles / southwest county. Weather score 8/100: RH 24%, wind/gust 15 mph, red-flag hours 0, near-threshold hours 0. |
| Sun, Jul 26 | LOW | Arboles / southwest county (LOW 12/100); Chimney Rock / west county (LOW 12/100); Piedra / north county (LOW 12/100) | Top weather score 8/100 at Arboles / southwest county. Weather score 8/100: RH 24%, wind/gust 15 mph, red-flag hours 0, near-threshold hours 0. |
| Mon, Jul 27 | LOW | Arboles / southwest county (LOW 12/100); Chimney Rock / west county (LOW 12/100); Piedra / north county (LOW 12/100) | Top weather score 8/100 at Arboles / southwest county. Weather score 8/100: RH 26%, wind/gust 16 mph, red-flag hours 0, near-threshold hours 0. |
| Tue, Jul 28 | LOW | Arboles / southwest county (LOW 12/100); Chimney Rock / west county (LOW 12/100); Piedra / north county (LOW 12/100) | Top weather score 8/100 at Arboles / southwest county. Weather score 8/100: RH 27%, wind/gust 16 mph, red-flag hours 0, near-threshold hours 0. |

## Area-Specific Outlook

| Area | Today | Peak this run | Highest-risk window |
| --- | --- | --- | --- |
| Pagosa Springs | LOW 4/100 | Thu, Jul 23: LOW 12/100 | Peak ingredients near 3 PM local; RH 44%, wind 17 mph. |
| Arboles | LOW 4/100 | Thu, Jul 23: LOW 12/100 | Peak ingredients near 3 PM local; RH 37%, wind 18 mph. |
| Chimney Rock | LOW 4/100 | Thu, Jul 23: LOW 12/100 | Peak ingredients near 3 PM local; RH 38%, wind 17 mph. |
| Piedra | LOW 4/100 | Thu, Jul 23: LOW 12/100 | Peak ingredients near 2 PM local; RH 57%, wind 15 mph. |
| Chromo | LOW 4/100 | Thu, Jul 23: LOW 12/100 | Peak ingredients near 3 PM local; RH 45%, wind 16 mph. |
| Durango | LOW 4/100 | Thu, Jul 23: LOW 12/100 | Peak ingredients near 4 PM local; RH 42%, wind 17 mph. |
| Bayfield | LOW 4/100 | Thu, Jul 23: LOW 12/100 | Peak ingredients near 4 PM local; RH 44%, wind 17 mph. |
| Ignacio | LOW 4/100 | Thu, Jul 23: LOW 12/100 | Peak ingredients near 3 PM local; RH 42%, wind 18 mph. |

## Fire Posture + Restrictions

- Summary: 4 official sources indicate fire restrictions or staged restrictions.
- Max restriction stage detected: STAGE 2
- Max fire danger detected: HIGH
- Sources reachable: 7/7
- Note: Official-source status check only; verify restrictions and burn decisions with the responsible jurisdiction.

| Jurisdiction | Restrictions | Fire danger | Source |
| --- | --- | --- | --- |
| Archuleta County | STAGE 2 | UNKNOWN | [Archuleta County Sheriff fire updates](https://sheriff.archuletacounty.gov/divisions/emergency-operations/fire-updates-and-information/) |
| Pagosa Springs | STAGE 2 | UNKNOWN | [Town of Pagosa Springs](https://www.pagosasprings.co.gov/) |
| San Juan National Forest | STAGE 2 | HIGH | [San Juan National Forest fire](https://www.fs.usda.gov/r02/sanjuan/fire) |
| BLM Tres Rios | UNKNOWN | UNKNOWN | [BLM Tres Rios Field Office](https://www.blm.gov/office/tres-rios-field-office) |
| La Plata County / Durango Fire | NONE | UNKNOWN | [Durango Fire & Rescue fire conditions](https://www.durangofire.org/fire-conditions) |
| Durango | UNKNOWN | UNKNOWN | [City of Durango](https://www.durangoco.gov/) |
| Southern Ute / Ignacio | STAGE 2 | UNKNOWN | [Southern Ute Indian Tribe](https://www.southernute-nsn.gov/) |

## Forecast Calibration

### PSPS Calibration

- Summary: No confirmed LPEA PSPS events logged yet; calibration will start once events are added.
- Confirmed PSPS events logged: 0
- Candidate/unconfirmed events logged: 0
- WATCH/LIKELY false-watch past days: 44
- Pending WATCH/LIKELY dates in current forecast: None
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
- [Flood Watch](https://api.weather.gov/alerts/urn:oid:2.49.0.1.840.0.cbd46bf49ded1a07f4e7a0799602e40e9b961467.001.1): Flood Watch issued July 22 at 11:26AM MDT until July 23 at 3:00AM MDT by NWS Grand Junction CO; 2026-07-22T11:26:00-06:00 to 2026-07-23T03:00:00-06:00; zones COZ001, COZ002, COZ003, COZ004, COZ005, COZ006, COZ007, COZ008, COZ009, COZ010, COZ011, COZ012, COZ013, COZ014, COZ017, COZ018, COZ019, COZ020, COZ021, COZ022, COZ023, UTZ022, UTZ023, UTZ024, UTZ025, UTZ027, UTZ028, UTZ029

## LPEA Power Signal

- Status: `active_keyword_match` - LPEA active/update sources contained power-interruption keywords; review source before treating as confirmed outage intent.
- Meaning: Active source match means a monitored LPEA active/update source currently contains fire, outage, PSPS, or power-interruption keywords. Operational outages are shown separately and are not treated as PSPS/fire evidence unless the source text says so.
- Operational outage context: No active outages are listed by the official LPEA outage viewer.
- Source coverage: 13 sources; 5/5 official social sources reachable
- Evidence quality: 0 operational, 2 active/update, 0 archive/context, 6 reference source matches.
- Active/update source pages with matches: LPEA homepage (public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation, restoration); LPEA LinkedIn (wildfire, fire mitigation)
- Distinct active/update signals: LPEA LinkedIn (wildfire, fire mitigation); LPEA LinkedIn (wildfire, fire mitigation)
- Example signal: ...followers 3w Edited Report this post Electric co-ops do a significant amount of wildfire mitigation work every year, all with one goal: protecting our members and the communities we serve. But, in much of the...
- Reference/context hits: [LPEA outage center](https://lpea.coop/outage-center); [LPEA wildfire / public safety power shutoffs](https://lpea.coop/psps); [LPEA red flag outage impact page](https://lpea.coop/outages/red-flag-warnings-and-impact-outages-prioritizing-safety-our-members); [LPEA fire mitigation](https://lpea.coop/fire-mitigation); [LPEA latest news](https://lpea.coop/Posts)

**Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## Next 7 Days

| Date | Tier | Main reason | Worst sampled metrics |
| --- | --- | --- | --- |
| Wed, Jul 22 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 36%, wind/gust 12 mph, thunder 60%<br>Arboles / southwest county: RH 46%, wind/gust 14 mph, thunder 58%<br>Chimney Rock / west county: RH 41%, wind/gust 12 mph, thunder 64% |
| Thu, Jul 23 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 43%, wind/gust 17 mph, thunder 51%<br>Arboles / southwest county: RH 37%, wind/gust 18 mph, thunder 33%<br>Chimney Rock / west county: RH 38%, wind/gust 17 mph, thunder 51% |
| Fri, Jul 24 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 30%, wind/gust 14 mph, thunder 48%<br>Arboles / southwest county: RH 27%, wind/gust 17 mph, thunder 22%<br>Chimney Rock / west county: RH 25%, wind/gust 16 mph, thunder 32% |
| Sat, Jul 25 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 30%, wind/gust 13 mph, thunder 60%<br>Arboles / southwest county: RH 24%, wind/gust 15 mph, thunder 46%<br>Chimney Rock / west county: RH 23%, wind/gust 15 mph, thunder 56% |
| Sun, Jul 26 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 28%, wind/gust 13 mph, thunder 48%<br>Arboles / southwest county: RH 24%, wind/gust 15 mph, thunder 45%<br>Chimney Rock / west county: RH 23%, wind/gust 15 mph, thunder 51% |
| Mon, Jul 27 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 29%, wind/gust 14 mph, thunder 67%<br>Arboles / southwest county: RH 26%, wind/gust 16 mph, thunder 52%<br>Chimney Rock / west county: RH 24%, wind/gust 16 mph, thunder 63% |
| Tue, Jul 28 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 31%, wind/gust 14 mph, thunder 63%<br>Arboles / southwest county: RH 27%, wind/gust 16 mph, thunder 49%<br>Chimney Rock / west county: RH 26%, wind/gust 16 mph, thunder 54% |

## Sample Point Status

- Pagosa Springs: COZ295 (matches), forecast zone COZ023, county zone COC007
- Arboles / southwest county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Chimney Rock / west county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Piedra / north county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Chromo / southeast county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Durango / La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Bayfield / east La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Ignacio / southeast La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
