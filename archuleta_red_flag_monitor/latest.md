# Archuleta Red Flag Risk Monitor

Generated: Jul 21, 2026 at 7:15 PM MDT (Pagosa Springs, CO local time)
Next update: Jul 22, 2026 at 5:20 AM MDT (Pagosa Springs, CO local time)
Date/time basis: Pagosa Springs, CO local time (America/Denver)
> **Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## At A Glance

- Fire-weather tier: **GREEN**
- PSPS likelihood: **ELEVATED**
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

- Summary: Highest LPEA PSPS concern is Thu, Jul 23 near Ignacio / southeast La Plata County (ELEVATED 20/100), driven by near-threshold wind/gust signal near 21 mph; Official fire-posture context for Ignacio / southeast La Plata County is escalated (STAGE 2; fire danger UNKNOWN); it adds a small preparedness modifier but does not create a PSPS WATCH by itself.
- Confidence: **MEDIUM** (69/100) - 8/8 sampled weather points available; 7/7 fire-posture sources reachable; official NWS alert zones checked; 13/13 LPEA public sources reachable; LPEA active/update sources checked; forecast changed substantially versus prior run; no confirmed PSPS events logged yet for calibration
- Weather fire-potential peak: Sat, Jul 25: Chimney Rock / west county LOW 28/100
- Red Flag likelihood peak: Thu, Jul 23: Ignacio / southeast La Plata County LOW 8/100
- LPEA PSPS peak: Thu, Jul 23: Ignacio / southeast La Plata County ELEVATED 20/100
- Method: rules-based decision support using public weather, fire-posture, and LPEA source signals; scores are screening estimates, not official or statistically calibrated probabilities.

| Date | Weather fire potential | Red Flag likelihood | LPEA PSPS | Main window |
| --- | --- | --- | --- | --- |
| Tue, Jul 21 | Pagosa Springs: LOW 20/100 | Arboles / southwest county: LOW 0/100 | Arboles / southwest county: LOW 12/100 | Peak ingredients near 7 PM local; RH 40%, wind 16 mph. |
| Wed, Jul 22 | Pagosa Springs: LOW 20/100 | Pagosa Springs: LOW 0/100 | Pagosa Springs: LOW 12/100 | Peak ingredients near 2 PM local; RH 34%, wind 16 mph. |
| Thu, Jul 23 | Ignacio / southeast La Plata County: LOW 26/100 | Ignacio / southeast La Plata County: LOW 8/100 | Ignacio / southeast La Plata County: ELEVATED 20/100 | Peak ingredients near 3 PM local; RH 39%, wind 21 mph. |
| Fri, Jul 24 | Pagosa Springs: LOW 20/100 | Arboles / southwest county: LOW 0/100 | Arboles / southwest county: LOW 12/100 | Peak ingredients near 3 PM local; RH 27%, wind 17 mph. |
| Sat, Jul 25 | Chimney Rock / west county: LOW 28/100 | Chimney Rock / west county: LOW 0/100 | Chimney Rock / west county: ELEVATED 18/100 | Peak ingredients near 3 PM local; RH 22%, wind 16 mph. |
| Sun, Jul 26 | Chimney Rock / west county: LOW 28/100 | Arboles / southwest county: LOW 0/100 | Arboles / southwest county: ELEVATED 18/100 | Peak ingredients near 3 PM local; RH 22%, wind 16 mph. |
| Mon, Jul 27 | Chimney Rock / west county: LOW 28/100 | Chimney Rock / west county: LOW 0/100 | Chimney Rock / west county: ELEVATED 18/100 | Peak ingredients near 3 PM local; RH 22%, wind 15 mph. |

## Analyst Interpretation

- Headline: Fire-weather screening remains GREEN with no official COZ295 alerts, while Jul 23 has the highest ELEVATED PSPS screening estimate.
- Summary: Official NWS data shows no active Red Flag or Fire Weather alerts for COZ295, and official LPEA outage data shows no active customer outages. Screening estimates put the Jul 23 PSPS peak at ELEVATED 20/100 near Ignacio, driven by near-threshold wind around 21 mph and Stage 2 fire-posture context; this does not create a WATCH or trigger a heads-up.
- Uncertainty: These are screening estimates, not official or statistically calibrated probabilities; no confirmed LPEA PSPS events are available for calibration.
- Evidence used: overall_status, weather_peaks, official_alerts, forecast_change, lpea_context, fire_posture, calibration
- This interpretation cannot change the deterministic tiers, scores, official alerts, or notification decision.

Changing drivers:
- Jul 23 worsened from LOW to ELEVATED PSPS screening as the driver shifted to Ignacio, with wind near 21 mph.
- Jul 21 eased from ELEVATED to LOW as wind fell 5 mph and RH rose 15 points.
- Jul 26 and Jul 27 moved to ELEVATED PSPS screening, but no WATCH-or-higher date emerged.
- Stage 2 restrictions and HIGH fire danger add preparedness context without creating a PSPS WATCH.

What to watch next:
- Recheck Jul 23 wind and RH trends near Ignacio.
- Verify whether LPEA keyword matches remain broad wildfire-mitigation context rather than a direct outage or PSPS notice.
- Watch whether Jul 25-27 dryness and driver locations persist across runs.
- Confirm any new official COZ295 alert or LPEA outage before taking action.

## Trend Intelligence

- Summary: Momentum is rising versus the prior run (Jul 21 at 5:21 AM MDT); forecast volatility is high and first WATCH-or-higher date is not present.
- Momentum: **Rising**
- Forecast volatility: **HIGH** (45/100)
- First WATCH-or-higher PSPS date: None
- Watch-date movement: No WATCH-or-higher PSPS dates in current or prior run.
- Method: compares current forecast evidence against prior local forecast history.

Notable changes:
- No WATCH-or-higher PSPS dates in current or prior run.
- Tue, Jul 21: easing vs prior run; PSPS ELEVATED -> LOW; score -8, wind -5 mph, RH +15%, red-flag hours 0. Driver shifted to Arboles / southwest county.
- Thu, Jul 23: worsening vs prior run; PSPS LOW -> ELEVATED; score +8, wind +1 mph, RH +3%, red-flag hours 0. Driver shifted to Ignacio / southeast La Plata County.
- Sun, Jul 26: worsening vs prior run; PSPS LOW -> ELEVATED; score +6, wind +1 mph, RH -3%, red-flag hours 0.
- Mon, Jul 27: worsening vs prior run; PSPS LOW -> ELEVATED; score +6, wind -1 mph, RH -1%, red-flag hours 0. Driver shifted to Chimney Rock / west county.

## Public Analysis Export

- Summary: Highest LPEA PSPS concern is Thu, Jul 23 near Ignacio / southeast La Plata County (ELEVATED 20/100), driven by near-threshold wind/gust signal near 21 mph; Official fire-posture context for Ignacio / southeast La Plata County is escalated (STAGE 2; fire danger UNKNOWN); it adds a small preparedness modifier but does not create a PSPS WATCH by itself.
- Trend: Momentum is rising versus the prior run (Jul 21 at 5:21 AM MDT); forecast volatility is high and first WATCH-or-higher date is not present.
- Confidence: **MEDIUM** (69/100)
- First WATCH-or-higher PSPS date: None
- PSPS peak: Thu, Jul 23 near Ignacio / southeast La Plata County at ELEVATED 20/100
- Red Flag peak: Thu, Jul 23 near Ignacio / southeast La Plata County at LOW 8/100
- Weather fire-potential peak: Sat, Jul 25 near Chimney Rock / west county at LOW 28/100
- LPEA operational outage context: No active outages are listed by the official LPEA outage viewer.
- Public JSON: `archuleta_red_flag_monitor/public_analysis_export.json`

What changed:
- No WATCH-or-higher PSPS dates in current or prior run.
- Tue, Jul 21: easing vs prior run; PSPS ELEVATED -> LOW; score -8, wind -5 mph, RH +15%, red-flag hours 0. Driver shifted to Arboles / southwest county.
- Thu, Jul 23: worsening vs prior run; PSPS LOW -> ELEVATED; score +8, wind +1 mph, RH +3%, red-flag hours 0. Driver shifted to Ignacio / southeast La Plata County.
- Sun, Jul 26: worsening vs prior run; PSPS LOW -> ELEVATED; score +6, wind +1 mph, RH -3%, red-flag hours 0.
- Mon, Jul 27: worsening vs prior run; PSPS LOW -> ELEVATED; score +6, wind -1 mph, RH -1%, red-flag hours 0. Driver shifted to Chimney Rock / west county.

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
| Tue, Jul 21 | LOW | Arboles / southwest county (LOW 12/100); Bayfield / east La Plata County (LOW 12/100); Ignacio / southeast La Plata County (LOW 12/100) | Top weather score 8/100 at Arboles / southwest county. Weather score 8/100: RH 40%, wind/gust 16 mph, red-flag hours 0, near-threshold hours 0. |
| Wed, Jul 22 | LOW | Pagosa Springs (LOW 12/100); Arboles / southwest county (LOW 12/100); Chimney Rock / west county (LOW 12/100) | Top weather score 8/100 at Pagosa Springs. Weather score 8/100: RH 34%, wind/gust 16 mph, red-flag hours 0, near-threshold hours 0. |
| Thu, Jul 23 | ELEVATED | Ignacio / southeast La Plata County (ELEVATED 20/100); Pagosa Springs (LOW 12/100); Arboles / southwest county (LOW 12/100) | Top weather score 16/100 at Ignacio / southeast La Plata County. Weather score 16/100: RH 39%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 0. |
| Fri, Jul 24 | LOW | Arboles / southwest county (LOW 12/100); Chimney Rock / west county (LOW 12/100); Durango / La Plata County (LOW 12/100) | Top weather score 8/100 at Arboles / southwest county. Weather score 8/100: RH 27%, wind/gust 17 mph, red-flag hours 0, near-threshold hours 0. |
| Sat, Jul 25 | ELEVATED | Chimney Rock / west county (ELEVATED 18/100); Arboles / southwest county (LOW 12/100); Piedra / north county (LOW 12/100) | Top weather score 14/100 at Chimney Rock / west county. Weather score 14/100: RH 22%, wind/gust 16 mph, red-flag hours 0, near-threshold hours 0. |
| Sun, Jul 26 | ELEVATED | Arboles / southwest county (ELEVATED 18/100); Chimney Rock / west county (ELEVATED 18/100); Piedra / north county (LOW 12/100) | Top weather score 14/100 at Arboles / southwest county. Weather score 14/100: RH 22%, wind/gust 16 mph, red-flag hours 0, near-threshold hours 0. |
| Mon, Jul 27 | ELEVATED | Chimney Rock / west county (ELEVATED 18/100); Arboles / southwest county (LOW 12/100); Piedra / north county (LOW 12/100) | Top weather score 14/100 at Chimney Rock / west county. Weather score 14/100: RH 22%, wind/gust 15 mph, red-flag hours 0, near-threshold hours 0. |

## Area-Specific Outlook

| Area | Today | Peak this run | Highest-risk window |
| --- | --- | --- | --- |
| Ignacio | LOW 12/100 | Thu, Jul 23: ELEVATED 20/100 | Peak ingredients near 3 PM local; RH 39%, wind 21 mph. |
| Arboles | LOW 12/100 | Sun, Jul 26: ELEVATED 18/100 | Peak ingredients near 3 PM local; RH 22%, wind 16 mph. |
| Chimney Rock | LOW 4/100 | Sat, Jul 25: ELEVATED 18/100 | Peak ingredients near 3 PM local; RH 22%, wind 16 mph. |
| Pagosa Springs | LOW 4/100 | Wed, Jul 22: LOW 12/100 | Peak ingredients near 2 PM local; RH 34%, wind 16 mph. |
| Piedra | LOW 4/100 | Wed, Jul 22: LOW 12/100 | Peak ingredients near 2 PM local; RH 42%, wind 15 mph. |
| Chromo | LOW 4/100 | Thu, Jul 23: LOW 12/100 | Peak ingredients near 3 PM local; RH 40%, wind 17 mph. |
| Durango | LOW 4/100 | Wed, Jul 22: LOW 12/100 | Peak ingredients near 2 PM local; RH 35%, wind 17 mph. |
| Bayfield | LOW 12/100 | Tue, Jul 21: LOW 12/100 | Peak ingredients near 9 PM local; RH 56%, wind 16 mph. |

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
- No active official NWS Red Flag / Fire Weather or related weather alerts found for monitored zones.

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
| Tue, Jul 21 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 34%, wind/gust 14 mph, thunder 48%<br>Arboles / southwest county: RH 40%, wind/gust 16 mph, thunder 53%<br>Chimney Rock / west county: RH 36%, wind/gust 14 mph, thunder 51% |
| Wed, Jul 22 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 34%, wind/gust 16 mph, thunder 72%<br>Arboles / southwest county: RH 34%, wind/gust 17 mph, thunder 68%<br>Chimney Rock / west county: RH 33%, wind/gust 16 mph, thunder 71% |
| Thu, Jul 23 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 40%, wind/gust 18 mph, thunder 73%<br>Arboles / southwest county: RH 36%, wind/gust 20 mph, thunder 41%<br>Chimney Rock / west county: RH 35%, wind/gust 18 mph, thunder 69% |
| Fri, Jul 24 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 31%, wind/gust 14 mph, thunder 59%<br>Arboles / southwest county: RH 27%, wind/gust 17 mph, thunder 26%<br>Chimney Rock / west county: RH 26%, wind/gust 16 mph, thunder 47% |
| Sat, Jul 25 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 28%, wind/gust 14 mph, thunder 46%<br>Arboles / southwest county: RH 23%, wind/gust 16 mph, thunder 24%<br>Chimney Rock / west county: RH 22%, wind/gust 16 mph, thunder 40% |
| Sun, Jul 26 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 26%, wind/gust 13 mph, thunder 44%<br>Arboles / southwest county: RH 22%, wind/gust 16 mph, thunder 35%<br>Chimney Rock / west county: RH 21%, wind/gust 16 mph, thunder 41% |
| Mon, Jul 27 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 28%, wind/gust 14 mph, thunder 52%<br>Arboles / southwest county: RH 23%, wind/gust 15 mph, thunder 38%<br>Chimney Rock / west county: RH 22%, wind/gust 15 mph, thunder 46% |

## Sample Point Status

- Pagosa Springs: COZ295 (matches), forecast zone COZ023, county zone COC007
- Arboles / southwest county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Chimney Rock / west county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Piedra / north county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Chromo / southeast county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Durango / La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Bayfield / east La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Ignacio / southeast La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
