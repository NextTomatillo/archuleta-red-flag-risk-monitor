# Archuleta Red Flag Risk Monitor

Generated: Jul 20, 2026 at 5:39 AM MDT (Pagosa Springs, CO local time)
Next update: Jul 20, 2026 at 5:20 PM MDT (Pagosa Springs, CO local time)
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

- Summary: Highest LPEA PSPS concern is Tue, Jul 21 near Durango / La Plata County (ELEVATED 20/100), driven by near-threshold wind/gust signal near 21 mph; Official fire-posture context for Durango / La Plata County is escalated (STAGE 2; fire danger HIGH); it adds a small preparedness modifier but does not create a PSPS WATCH by itself.
- Confidence: **MEDIUM** (69/100) - 8/8 sampled weather points available; 7/7 fire-posture sources reachable; official NWS alert zones checked; 13/13 LPEA public sources reachable; LPEA active/update sources checked; active LPEA operational outage context checked separately from PSPS scoring; forecast changed substantially versus prior run; no confirmed PSPS events logged yet for calibration
- Weather fire-potential peak: Tue, Jul 21: Durango / La Plata County LOW 32/100
- Red Flag likelihood peak: Tue, Jul 21: Durango / La Plata County LOW 8/100
- LPEA PSPS peak: Tue, Jul 21: Durango / La Plata County ELEVATED 20/100
- Method: rules-based decision support using public weather, fire-posture, and LPEA source signals; scores are screening estimates, not official or statistically calibrated probabilities.

| Date | Weather fire potential | Red Flag likelihood | LPEA PSPS | Main window |
| --- | --- | --- | --- | --- |
| Mon, Jul 20 | Pagosa Springs: LOW 28/100 | Chimney Rock / west county: LOW 0/100 | Chimney Rock / west county: ELEVATED 18/100 | Peak ingredients near 3 PM local; RH 19%, wind 15 mph. |
| Tue, Jul 21 | Durango / La Plata County: LOW 32/100 | Durango / La Plata County: LOW 8/100 | Durango / La Plata County: ELEVATED 20/100 | Peak ingredients near 3 PM local; RH 24%, wind 21 mph. |
| Wed, Jul 22 | Pagosa Springs: LOW 20/100 | Pagosa Springs: LOW 0/100 | Pagosa Springs: LOW 12/100 | Peak ingredients near 3 PM local; RH 35%, wind 17 mph. |
| Thu, Jul 23 | Durango / La Plata County: LOW 32/100 | Durango / La Plata County: LOW 8/100 | Durango / La Plata County: ELEVATED 20/100 | Peak ingredients near 3 PM local; RH 37%, wind 21 mph. |
| Fri, Jul 24 | Ignacio / southeast La Plata County: LOW 26/100 | Ignacio / southeast La Plata County: LOW 8/100 | Ignacio / southeast La Plata County: ELEVATED 20/100 | Peak ingredients near 3 PM local; RH 32%, wind 21 mph. |
| Sat, Jul 25 | Durango / La Plata County: LOW 32/100 | Durango / La Plata County: LOW 8/100 | Durango / La Plata County: ELEVATED 20/100 | Peak ingredients near 4 PM local; RH 30%, wind 21 mph. |
| Sun, Jul 26 | Bayfield / east La Plata County: LOW 32/100 | Bayfield / east La Plata County: LOW 8/100 | Bayfield / east La Plata County: ELEVATED 20/100 | Peak ingredients near 4 PM local; RH 29%, wind 21 mph. |

## Analyst Interpretation

- Headline: Screening stays GREEN overall, with the top PSPS estimate elevated for Tuesday, July 21 near Durango while official COZ295 fire alerts remain absent.
- Summary: Current screening stays GREEN overall with no official COZ295 Red Flag or Fire Weather alerts and no WATCH-or-higher PSPS dates. The top screening signal is an ELEVATED PSPS estimate for Tuesday, July 21 near Durango / La Plata County, driven by near-threshold wind and supported by Stage 2 restrictions with HIGH fire danger there. Official LPEA outage data separately shows two localized outages affecting two customers, but no fire-weather or PSPS cause has been identified.
- Uncertainty: These are screening estimates rather than official forecasts, and confidence is limited by high forecast volatility plus the lack of confirmed PSPS events for calibration.
- Evidence used: overall_status, weather_peaks, official_alerts, lpea_context, forecast_change, fire_posture, calibration
- This interpretation cannot change the deterministic tiers, scores, official alerts, or notification decision.

Changing drivers:
- Tuesday, July 21 remains the top screening concern near Durango / La Plata County because wind is near 21 mph and local fire posture is Stage 2 with HIGH fire danger.
- No official COZ295 Red Flag or Fire Weather alerts are active in the monitored zones.
- Official LPEA outage data shows two localized outages near Durango / La Plata County, but no fire-weather or PSPS cause has been identified.
- Forecast momentum is steady, while late-week driver locations continue to shift within the broader service area.

What to watch next:
- Recheck Tuesday, July 21 wind and humidity for any move toward WATCH-level PSPS screening.
- Watch whether the localized Durango-area outages are cleared or receive a stated cause from LPEA.
- Monitor whether the highest-risk driver area keeps shifting between Pagosa Springs and La Plata County later this week.
- Check for any new official COZ295 fire-weather alerts before conditions peak.

## Trend Intelligence

- Summary: Momentum is steady versus the prior run (Jul 19 at 5:23 PM MDT); forecast volatility is high and first WATCH-or-higher date is not present.
- Momentum: **Steady**
- Forecast volatility: **HIGH** (30/100)
- First WATCH-or-higher PSPS date: None
- Watch-date movement: No WATCH-or-higher PSPS dates in current or prior run.
- Method: compares current forecast evidence against prior local forecast history.

Notable changes:
- No WATCH-or-higher PSPS dates in current or prior run.
- Wed, Jul 22: easing vs prior run; PSPS ELEVATED -> LOW; score -8, wind -1 mph, RH +2%, red-flag hours 0. Driver shifted to Pagosa Springs.
- Sat, Jul 25: worsening vs prior run; PSPS LOW -> ELEVATED; score +8, wind +1 mph, RH +1%, red-flag hours 0. Driver shifted to Durango / La Plata County.

## Public Analysis Export

- Summary: Highest LPEA PSPS concern is Tue, Jul 21 near Durango / La Plata County (ELEVATED 20/100), driven by near-threshold wind/gust signal near 21 mph; Official fire-posture context for Durango / La Plata County is escalated (STAGE 2; fire danger HIGH); it adds a small preparedness modifier but does not create a PSPS WATCH by itself.
- Trend: Momentum is steady versus the prior run (Jul 19 at 5:23 PM MDT); forecast volatility is high and first WATCH-or-higher date is not present.
- Confidence: **MEDIUM** (69/100)
- First WATCH-or-higher PSPS date: None
- PSPS peak: Tue, Jul 21 near Durango / La Plata County at ELEVATED 20/100
- Red Flag peak: Tue, Jul 21 near Durango / La Plata County at LOW 8/100
- Weather fire-potential peak: Tue, Jul 21 near Durango / La Plata County at LOW 32/100
- LPEA operational outage context: 2 active outages; 0 planned and 2 unplanned; 2 customers out. No fire-weather or PSPS cause is identified.
- Public JSON: `archuleta_red_flag_monitor/public_analysis_export.json`

What changed:
- No WATCH-or-higher PSPS dates in current or prior run.
- Wed, Jul 22: easing vs prior run; PSPS ELEVATED -> LOW; score -8, wind -1 mph, RH +2%, red-flag hours 0. Driver shifted to Pagosa Springs.
- Sat, Jul 25: worsening vs prior run; PSPS LOW -> ELEVATED; score +8, wind +1 mph, RH +1%, red-flag hours 0. Driver shifted to Durango / La Plata County.

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
| Mon, Jul 20 | ELEVATED | Chimney Rock / west county (ELEVATED 18/100); Durango / La Plata County (LOW 12/100); Bayfield / east La Plata County (LOW 12/100) | Top weather score 14/100 at Chimney Rock / west county. Weather score 14/100: RH 19%, wind/gust 15 mph, red-flag hours 0, near-threshold hours 0. |
| Tue, Jul 21 | ELEVATED | Durango / La Plata County (ELEVATED 20/100); Bayfield / east La Plata County (ELEVATED 20/100); Chimney Rock / west county (ELEVATED 18/100) | Top weather score 16/100 at Durango / La Plata County. Weather score 16/100: RH 24%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 0. |
| Wed, Jul 22 | LOW | Pagosa Springs (LOW 12/100); Arboles / southwest county (LOW 12/100); Chimney Rock / west county (LOW 12/100) | Top weather score 8/100 at Pagosa Springs. Weather score 8/100: RH 35%, wind/gust 17 mph, red-flag hours 0, near-threshold hours 0. |
| Thu, Jul 23 | ELEVATED | Durango / La Plata County (ELEVATED 20/100); Bayfield / east La Plata County (ELEVATED 20/100); Ignacio / southeast La Plata County (ELEVATED 20/100) | Top weather score 16/100 at Durango / La Plata County. Weather score 16/100: RH 37%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 0. |
| Fri, Jul 24 | ELEVATED | Ignacio / southeast La Plata County (ELEVATED 20/100); Pagosa Springs (LOW 12/100); Arboles / southwest county (LOW 12/100) | Top weather score 16/100 at Ignacio / southeast La Plata County. Weather score 16/100: RH 32%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 0. |
| Sat, Jul 25 | ELEVATED | Durango / La Plata County (ELEVATED 20/100); Pagosa Springs (LOW 12/100); Arboles / southwest county (LOW 12/100) | Top weather score 16/100 at Durango / La Plata County. Weather score 16/100: RH 29%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 0. |
| Sun, Jul 26 | ELEVATED | Bayfield / east La Plata County (ELEVATED 20/100); Ignacio / southeast La Plata County (ELEVATED 20/100); Chimney Rock / west county (ELEVATED 18/100) | Top weather score 16/100 at Bayfield / east La Plata County. Weather score 16/100: RH 28%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 0. |

## Area-Specific Outlook

| Area | Today | Peak this run | Highest-risk window |
| --- | --- | --- | --- |
| Durango | LOW 12/100 | Tue, Jul 21: ELEVATED 20/100 | Peak ingredients near 3 PM local; RH 24%, wind 21 mph. |
| Bayfield | LOW 12/100 | Tue, Jul 21: ELEVATED 20/100 | Peak ingredients near 3 PM local; RH 26%, wind 21 mph. |
| Ignacio | LOW 4/100 | Thu, Jul 23: ELEVATED 20/100 | Peak ingredients near 3 PM local; RH 38%, wind 21 mph. |
| Chimney Rock | ELEVATED 18/100 | Mon, Jul 20: ELEVATED 18/100 | Peak ingredients near 3 PM local; RH 19%, wind 15 mph. |
| Pagosa Springs | LOW 10/100 | Tue, Jul 21: LOW 12/100 | Peak ingredients near 3 PM local; RH 24%, wind 17 mph. |
| Arboles | LOW 10/100 | Tue, Jul 21: LOW 12/100 | Peak ingredients near 3 PM local; RH 23%, wind 18 mph. |
| Piedra | LOW 4/100 | Tue, Jul 21: LOW 12/100 | Peak ingredients near 3 PM local; RH 26%, wind 17 mph. |
| Chromo | LOW 10/100 | Tue, Jul 21: LOW 12/100 | Peak ingredients near 3 PM local; RH 25%, wind 16 mph. |

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

- Status: `operational_outage_active` - Official LPEA outage data indicates an operational outage; use as grid context, not PSPS/fire evidence unless LPEA identifies that cause.
- Meaning: Active source match means a monitored LPEA active/update source currently contains fire, outage, PSPS, or power-interruption keywords. Operational outages are shown separately and are not treated as PSPS/fire evidence unless the source text says so.
- Operational outage context: 2 active outages; 0 planned and 2 unplanned; 2 customers out. No fire-weather or PSPS cause is identified.
- Source coverage: 13 sources; 5/5 official social sources reachable
- Evidence quality: 0 operational, 3 active/update, 0 archive/context, 6 reference source matches.
- Operational outage source links: [BONDAD WELL #32 33.9](https://outage.lpea.coop); [511 COUNTY RD 220](https://outage.lpea.coop)
- Active/update source pages with matches: LPEA homepage (red flag, public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation); LPEA LinkedIn (wildfire, fire mitigation)
- Distinct active/update signals: LPEA homepage (red flag, public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation); LPEA LinkedIn (wildfire, fire mitigation); LPEA LinkedIn (wildfire, fire mitigation)
- Example signal: ...tings & Resources Board Committees Voting Districts Policies & Bylaws Elections Red Flag Conditions May Result in Longer, More Frequent Outages Learn Why That's a Good Thing LPEA Announces 2026-27 Board Leade...
- Reference/context hits: [LPEA outage center](https://lpea.coop/outage-center); [LPEA wildfire / public safety power shutoffs](https://lpea.coop/psps); [LPEA red flag outage impact page](https://lpea.coop/outages/red-flag-warnings-and-impact-outages-prioritizing-safety-our-members); [LPEA fire mitigation](https://lpea.coop/fire-mitigation); [LPEA latest news](https://lpea.coop/Posts)

**Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## Next 7 Days

| Date | Tier | Main reason | Worst sampled metrics |
| --- | --- | --- | --- |
| Mon, Jul 20 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 22%, wind/gust 14 mph, thunder 21%<br>Arboles / southwest county: RH 22%, wind/gust 14 mph, thunder 23%<br>Chimney Rock / west county: RH 19%, wind/gust 15 mph, thunder 21% |
| Tue, Jul 21 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 24%, wind/gust 17 mph, thunder 39%<br>Arboles / southwest county: RH 23%, wind/gust 18 mph, thunder 42%<br>Chimney Rock / west county: RH 20%, wind/gust 18 mph, thunder 42% |
| Wed, Jul 22 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 35%, wind/gust 17 mph, thunder 59%<br>Arboles / southwest county: RH 35%, wind/gust 17 mph, thunder 49%<br>Chimney Rock / west county: RH 31%, wind/gust 17 mph, thunder 55% |
| Thu, Jul 23 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 36%, wind/gust 20 mph, thunder 55%<br>Arboles / southwest county: RH 35%, wind/gust 20 mph, thunder 35%<br>Chimney Rock / west county: RH 31%, wind/gust 18 mph, thunder 47% |
| Fri, Jul 24 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 31%, wind/gust 16 mph, thunder 45%<br>Arboles / southwest county: RH 29%, wind/gust 20 mph, thunder 19%<br>Chimney Rock / west county: RH 26%, wind/gust 17 mph, thunder 33% |
| Sat, Jul 25 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 29%, wind/gust 15 mph, thunder 43%<br>Arboles / southwest county: RH 25%, wind/gust 17 mph, thunder 26%<br>Chimney Rock / west county: RH 24%, wind/gust 17 mph, thunder 34% |
| Sun, Jul 26 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 27%, wind/gust 15 mph, thunder 47%<br>Arboles / southwest county: RH 24%, wind/gust 18 mph, thunder 34%<br>Chimney Rock / west county: RH 22%, wind/gust 17 mph, thunder 41% |

## Sample Point Status

- Pagosa Springs: COZ295 (matches), forecast zone COZ023, county zone COC007
- Arboles / southwest county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Chimney Rock / west county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Piedra / north county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Chromo / southeast county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Durango / La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Bayfield / east La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Ignacio / southeast La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
