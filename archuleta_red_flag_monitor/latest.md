# Archuleta Red Flag Risk Monitor

Generated: Jul 14, 2026 at 11:49 AM MDT (Pagosa Springs, CO local time)
Next update: Jul 14, 2026 at 5:20 PM MDT (Pagosa Springs, CO local time)
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
- LPEA signal: `operational_outage_active` - Official LPEA outage data indicates an operational outage; use as grid context, not PSPS/fire evidence unless LPEA identifies that cause.
- LPEA source coverage: 13 sources; 5/5 official social sources reachable
- NWS discussion: No concerning fire-weather language found in latest GJT discussion.

## Decision Support

- Summary: Highest LPEA PSPS concern is Tue, Jul 14 near Arboles / southwest county (ELEVATED 18/100), driven by breezy wind/gust signal near 15 mph; dry RH near 22%; Official fire-posture context for Arboles / southwest county is escalated (STAGE 2; fire danger UNKNOWN); it adds a small preparedness modifier but does not create a PSPS WATCH by itself.
- Confidence: **HIGH** (77/100) - 8/8 sampled weather points available; 7/7 fire-posture sources reachable; official NWS alert zones checked; 13/13 LPEA public sources reachable; LPEA active/update sources checked; active LPEA operational outage context checked separately from PSPS scoring; no confirmed PSPS events logged yet for calibration
- Weather fire-potential peak: Tue, Jul 14: Pagosa Springs LOW 24/100
- Red Flag likelihood peak: Tue, Jul 14: Arboles / southwest county LOW 0/100
- LPEA PSPS peak: Tue, Jul 14: Arboles / southwest county ELEVATED 18/100
- Method: rules-based decision support using public weather, fire-posture, and LPEA source signals; scores are screening estimates, not official or statistically calibrated probabilities.

| Date | Weather fire potential | Red Flag likelihood | LPEA PSPS | Main window |
| --- | --- | --- | --- | --- |
| Tue, Jul 14 | Pagosa Springs: LOW 24/100 | Arboles / southwest county: LOW 0/100 | Arboles / southwest county: ELEVATED 18/100 | Peak ingredients near 4 PM local; RH 31%, wind 15 mph. |
| Wed, Jul 15 | Pagosa Springs: LOW 24/100 | Arboles / southwest county: LOW 0/100 | Arboles / southwest county: LOW 12/100 | Peak ingredients near 4 PM local; RH 40%, wind 15 mph. |
| Thu, Jul 16 | Pagosa Springs: LOW 24/100 | Pagosa Springs: LOW 0/100 | Pagosa Springs: LOW 4/100 | Peak ingredients near 3 PM local; RH 39%, wind 12 mph. |
| Fri, Jul 17 | Pagosa Springs: LOW 24/100 | Pagosa Springs: LOW 0/100 | Pagosa Springs: LOW 4/100 | Peak ingredients near 3 PM local; RH 35%, wind 12 mph. |
| Sat, Jul 18 | Pagosa Springs: LOW 24/100 | Durango / La Plata County: LOW 0/100 | Durango / La Plata County: LOW 12/100 | Peak ingredients near 2 PM local; RH 34%, wind 15 mph. |
| Sun, Jul 19 | Pagosa Springs: LOW 24/100 | Arboles / southwest county: LOW 0/100 | Arboles / southwest county: LOW 12/100 | Peak ingredients near 4 PM local; RH 30%, wind 15 mph. |
| Mon, Jul 20 | Pagosa Springs: LOW 24/100 | Chimney Rock / west county: LOW 0/100 | Chimney Rock / west county: LOW 12/100 | Peak ingredients near 3 PM local; RH 25%, wind 15 mph. |

## Analyst Interpretation

- Headline: Fire-weather risk is low; elevated PSPS screening reflects preparedness context, not watch-level weather.
- Summary: The fire-weather tier is GREEN, with no official NWS fire-weather alert and no WATCH or LIKELY PSPS date. The 18/100 ELEVATED PSPS peak near Arboles combines modest dryness and breeze with Stage 2 fire restrictions, which add context but do not create a watch by themselves. Two localized LPEA outages affect one customer each, and neither has a posted fire-weather or PSPS cause.
- Uncertainty: No confirmed LPEA PSPS event is logged for calibration, and LPEA's internal circuit conditions and shutoff thresholds are not public.
- Evidence used: overall_status, weather_peaks, official_alerts, forecast_change, lpea_context, fire_posture, calibration
- This interpretation cannot change the deterministic tiers, scores, official alerts, or notification decision.

Changing drivers:
- Forecast momentum is steady with low volatility versus the prior run.
- No current or prior-run date reaches WATCH-or-higher PSPS screening.
- The top PSPS screen remains ELEVATED 18/100 near Arboles on Tuesday.

What to watch next:
- Watch official NWS alerts and any increase in coincident low humidity and wind.
- Check LPEA sources for direct PSPS intent rather than broad seasonal safety language.
- Track whether either localized outage changes size, cause, or fire relationship.

## Trend Intelligence

- Summary: Momentum is steady versus the prior run (Jul 14 at 11:40 AM MDT); forecast volatility is low and first WATCH-or-higher date is not present.
- Momentum: **Steady**
- Forecast volatility: **LOW** (0/100)
- First WATCH-or-higher PSPS date: None
- Watch-date movement: No WATCH-or-higher PSPS dates in current or prior run.
- Method: compares current forecast evidence against prior local forecast history.

Notable changes:
- No WATCH-or-higher PSPS dates in current or prior run.
- No major day-level movement versus the prior run.

## Public Analysis Export

- Summary: Highest LPEA PSPS concern is Tue, Jul 14 near Arboles / southwest county (ELEVATED 18/100), driven by breezy wind/gust signal near 15 mph; dry RH near 22%; Official fire-posture context for Arboles / southwest county is escalated (STAGE 2; fire danger UNKNOWN); it adds a small preparedness modifier but does not create a PSPS WATCH by itself.
- Trend: Momentum is steady versus the prior run (Jul 14 at 11:40 AM MDT); forecast volatility is low and first WATCH-or-higher date is not present.
- Confidence: **HIGH** (77/100)
- First WATCH-or-higher PSPS date: None
- PSPS peak: Tue, Jul 14 near Arboles / southwest county at ELEVATED 18/100
- Red Flag peak: Tue, Jul 14 near Arboles / southwest county at LOW 0/100
- Weather fire-potential peak: Tue, Jul 14 near Pagosa Springs at LOW 24/100
- LPEA operational outage context: 2 active outages; 1 planned and 1 unplanned; 2 customers out. No fire-weather or PSPS cause is identified.
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
| Tue, Jul 14 | ELEVATED | Arboles / southwest county (ELEVATED 18/100); Chimney Rock / west county (LOW 12/100); Durango / La Plata County (LOW 12/100) | Top weather score 14/100 at Arboles / southwest county. Weather score 14/100: RH 22%, wind/gust 15 mph, red-flag hours 0, near-threshold hours 0. |
| Wed, Jul 15 | LOW | Arboles / southwest county (LOW 12/100); Durango / La Plata County (LOW 12/100); Ignacio / southeast La Plata County (LOW 12/100) | Top weather score 8/100 at Arboles / southwest county. Weather score 8/100: RH 29%, wind/gust 15 mph, red-flag hours 0, near-threshold hours 0. |
| Thu, Jul 16 | LOW | Pagosa Springs (LOW 4/100); Arboles / southwest county (LOW 4/100); Chimney Rock / west county (LOW 4/100) | Top weather score 0/100 at Pagosa Springs. Weather score 0/100: RH 39%, wind/gust 12 mph, red-flag hours 0, near-threshold hours 0. |
| Fri, Jul 17 | LOW | Pagosa Springs (LOW 4/100); Arboles / southwest county (LOW 4/100); Chimney Rock / west county (LOW 4/100) | Top weather score 0/100 at Pagosa Springs. Weather score 0/100: RH 35%, wind/gust 12 mph, red-flag hours 0, near-threshold hours 0. |
| Sat, Jul 18 | LOW | Durango / La Plata County (LOW 12/100); Ignacio / southeast La Plata County (LOW 12/100); Pagosa Springs (LOW 4/100) | Top weather score 8/100 at Durango / La Plata County. Weather score 8/100: RH 34%, wind/gust 15 mph, red-flag hours 0, near-threshold hours 0. |
| Sun, Jul 19 | LOW | Arboles / southwest county (LOW 12/100); Chimney Rock / west county (LOW 12/100); Durango / La Plata County (LOW 12/100) | Top weather score 8/100 at Arboles / southwest county. Weather score 8/100: RH 29%, wind/gust 15 mph, red-flag hours 0, near-threshold hours 0. |
| Mon, Jul 20 | LOW | Chimney Rock / west county (LOW 12/100); Durango / La Plata County (LOW 12/100); Bayfield / east La Plata County (LOW 12/100) | Top weather score 8/100 at Chimney Rock / west county. Weather score 8/100: RH 25%, wind/gust 15 mph, red-flag hours 0, near-threshold hours 0. |

## Area-Specific Outlook

| Area | Today | Peak this run | Highest-risk window |
| --- | --- | --- | --- |
| Arboles | ELEVATED 18/100 | Tue, Jul 14: ELEVATED 18/100 | Peak ingredients near 4 PM local; RH 31%, wind 15 mph. |
| Chimney Rock | LOW 12/100 | Tue, Jul 14: LOW 12/100 | Peak ingredients near 3 PM local; RH 26%, wind 15 mph. |
| Durango | LOW 12/100 | Tue, Jul 14: LOW 12/100 | Peak ingredients near 3 PM local; RH 34%, wind 17 mph. |
| Bayfield | LOW 12/100 | Tue, Jul 14: LOW 12/100 | Peak ingredients near 3 PM local; RH 35%, wind 16 mph. |
| Ignacio | LOW 12/100 | Tue, Jul 14: LOW 12/100 | Peak ingredients near 3 PM local; RH 31%, wind 16 mph. |
| Pagosa Springs | LOW 4/100 | Tue, Jul 14: LOW 4/100 | Peak ingredients near 4 PM local; RH 25%, wind 13 mph. |
| Piedra | LOW 4/100 | Tue, Jul 14: LOW 4/100 | Peak ingredients near 3 PM local; RH 31%, wind 13 mph. |
| Chromo | LOW 4/100 | Tue, Jul 14: LOW 4/100 | Peak ingredients near 9 PM local; RH 53%, wind 13 mph. |

## Fire Posture + Restrictions

- Summary: 5 official sources indicate fire restrictions or staged restrictions.
- Max restriction stage detected: STAGE 2
- Max fire danger detected: VERY HIGH
- Sources reachable: 7/7
- Note: Official-source status check only; verify restrictions and burn decisions with the responsible jurisdiction.

| Jurisdiction | Restrictions | Fire danger | Source |
| --- | --- | --- | --- |
| Archuleta County | STAGE 2 | UNKNOWN | [Archuleta County Sheriff fire updates](https://sheriff.archuletacounty.gov/divisions/emergency-operations/fire-updates-and-information/) |
| Pagosa Springs | STAGE 2 | UNKNOWN | [Town of Pagosa Springs](https://www.pagosasprings.co.gov/) |
| San Juan National Forest | STAGE 2 | VERY HIGH | [San Juan National Forest fire](https://www.fs.usda.gov/r02/sanjuan/fire) |
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

- Status: `operational_outage_active` - Official LPEA outage data indicates an operational outage; use as grid context, not PSPS/fire evidence unless LPEA identifies that cause.
- Meaning: Active source match means a monitored LPEA active/update source currently contains fire, outage, PSPS, or power-interruption keywords. Operational outages are shown separately and are not treated as PSPS/fire evidence unless the source text says so.
- Operational outage context: 2 active outages; 1 planned and 1 unplanned; 2 customers out. No fire-weather or PSPS cause is identified.
- Source coverage: 13 sources; 5/5 official social sources reachable
- Evidence quality: 0 operational, 3 active/update, 0 archive/context, 6 reference source matches.
- Operational outage source links: [861 MEADOWS DR](https://outage.lpea.coop); [FASSETT 2-13 NO 1 WELLSITE](https://outage.lpea.coop)
- Active/update source pages with matches: LPEA homepage (red flag, public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation); LPEA LinkedIn (wildfire, public safety power shutoff, power shutoff, shutoff, fire mitigation)
- Distinct active/update signals: LPEA homepage (red flag, public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation); LPEA LinkedIn (wildfire, public safety power shutoff, power shutoff, shutoff, fire mitigation); LinkedIn PSPS explainer post (wildfire, public safety power shutoff, power shutoff, shutoff, fire mitigation)
- Example signal: ...tings & Resources Board Committees Voting Districts Policies & Bylaws Elections Red Flag Conditions May Result in Longer, More Frequent Outages Learn Why That's a Good Thing LPEA Announces 2026-27 Board Leade...
- Reference/context hits: [LPEA outage center](https://lpea.coop/outage-center); [LPEA wildfire / public safety power shutoffs](https://lpea.coop/psps); [LPEA red flag outage impact page](https://lpea.coop/outages/red-flag-warnings-and-impact-outages-prioritizing-safety-our-members); [LPEA fire mitigation](https://lpea.coop/fire-mitigation); [LPEA latest news](https://lpea.coop/Posts)

**Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## Next 7 Days

| Date | Tier | Main reason | Worst sampled metrics |
| --- | --- | --- | --- |
| Tue, Jul 14 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 25%, wind/gust 13 mph, thunder 37%<br>Arboles / southwest county: RH 22%, wind/gust 15 mph, thunder 34%<br>Chimney Rock / west county: RH 23%, wind/gust 15 mph, thunder 49% |
| Wed, Jul 15 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 35%, wind/gust 13 mph, thunder 68%<br>Arboles / southwest county: RH 29%, wind/gust 15 mph, thunder 61%<br>Chimney Rock / west county: RH 31%, wind/gust 14 mph, thunder 66% |
| Thu, Jul 16 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 39%, wind/gust 12 mph, thunder 73%<br>Arboles / southwest county: RH 39%, wind/gust 13 mph, thunder 66%<br>Chimney Rock / west county: RH 38%, wind/gust 13 mph, thunder 71% |
| Fri, Jul 17 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 35%, wind/gust 12 mph, thunder 83%<br>Arboles / southwest county: RH 36%, wind/gust 12 mph, thunder 70%<br>Chimney Rock / west county: RH 33%, wind/gust 13 mph, thunder 78% |
| Sat, Jul 18 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 29%, wind/gust 12 mph, thunder 50%<br>Arboles / southwest county: RH 32%, wind/gust 14 mph, thunder 45%<br>Chimney Rock / west county: RH 27%, wind/gust 14 mph, thunder 48% |
| Sun, Jul 19 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 26%, wind/gust 14 mph, thunder 39%<br>Arboles / southwest county: RH 29%, wind/gust 15 mph, thunder 45%<br>Chimney Rock / west county: RH 24%, wind/gust 15 mph, thunder 40% |
| Mon, Jul 20 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 28%, wind/gust 14 mph, thunder 53%<br>Arboles / southwest county: RH 28%, wind/gust 14 mph, thunder 46%<br>Chimney Rock / west county: RH 25%, wind/gust 15 mph, thunder 48% |

## Sample Point Status

- Pagosa Springs: COZ295 (matches), forecast zone COZ023, county zone COC007
- Arboles / southwest county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Chimney Rock / west county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Piedra / north county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Chromo / southeast county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Durango / La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Bayfield / east La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Ignacio / southeast La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
