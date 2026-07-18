# Archuleta Red Flag Risk Monitor

Generated: Jul 18, 2026 at 5:21 PM MDT (Pagosa Springs, CO local time)
Next update: Jul 19, 2026 at 5:20 AM MDT (Pagosa Springs, CO local time)
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

- Summary: Highest LPEA PSPS concern is Thu, Jul 23 near Bayfield / east La Plata County (ELEVATED 20/100), driven by near-threshold wind/gust signal near 21 mph; Official fire-posture context for Bayfield / east La Plata County is escalated (STAGE 2; fire danger VERY HIGH); it adds a small preparedness modifier but does not create a PSPS WATCH by itself.
- Confidence: **MEDIUM** (69/100) - 8/8 sampled weather points available; 7/7 fire-posture sources reachable; official NWS alert zones checked; 13/13 LPEA public sources reachable; LPEA active/update sources checked; active LPEA operational outage context checked separately from PSPS scoring; forecast changed substantially versus prior run; no confirmed PSPS events logged yet for calibration
- Weather fire-potential peak: Thu, Jul 23: Bayfield / east La Plata County MODERATE 36/100
- Red Flag likelihood peak: Thu, Jul 23: Bayfield / east La Plata County LOW 8/100
- LPEA PSPS peak: Thu, Jul 23: Bayfield / east La Plata County ELEVATED 20/100
- Method: rules-based decision support using public weather, fire-posture, and LPEA source signals; scores are screening estimates, not official or statistically calibrated probabilities.

| Date | Weather fire potential | Red Flag likelihood | LPEA PSPS | Main window |
| --- | --- | --- | --- | --- |
| Sat, Jul 18 | Pagosa Springs: LOW 24/100 | Durango / La Plata County: LOW 0/100 | Durango / La Plata County: LOW 12/100 | Peak ingredients near 5 PM local; RH 42%, wind 15 mph. |
| Sun, Jul 19 | Pagosa Springs: LOW 24/100 | Durango / La Plata County: LOW 0/100 | Durango / La Plata County: LOW 12/100 | Peak ingredients near 3 PM local; RH 30%, wind 16 mph. |
| Mon, Jul 20 | Pagosa Springs: LOW 24/100 | Chimney Rock / west county: LOW 0/100 | Chimney Rock / west county: LOW 12/100 | Peak ingredients near 4 PM local; RH 25%, wind 15 mph. |
| Tue, Jul 21 | Chimney Rock / west county: LOW 32/100 | Chimney Rock / west county: LOW 0/100 | Chimney Rock / west county: ELEVATED 18/100 | Peak ingredients near 3 PM local; RH 22%, wind 16 mph. |
| Wed, Jul 22 | Pagosa Springs: LOW 24/100 | Pagosa Springs: LOW 0/100 | Pagosa Springs: LOW 12/100 | Peak ingredients near 3 PM local; RH 30%, wind 16 mph. |
| Thu, Jul 23 | Bayfield / east La Plata County: MODERATE 36/100 | Bayfield / east La Plata County: LOW 8/100 | Bayfield / east La Plata County: ELEVATED 20/100 | Peak ingredients near 4 PM local; RH 31%, wind 21 mph. |
| Fri, Jul 24 | Chimney Rock / west county: LOW 32/100 | Chimney Rock / west county: LOW 0/100 | Chimney Rock / west county: ELEVATED 18/100 | Peak ingredients near 3 PM local; RH 22%, wind 17 mph. |

## Analyst Interpretation

- Headline: Screening stays GREEN overall, while Thu, Jul 23 carries the highest ELEVATED PSPS concern near Bayfield under breezy conditions and Stage 2 restrictions.
- Summary: The deterministic monitor remains GREEN overall with no HIGH or CONCERN dates and no official COZ295 Red Flag or Fire Weather alerts. Screening concern is highest on Thu, Jul 23 near Bayfield / east La Plata County, where PSPS likelihood reaches ELEVATED on near-threshold wind and very high fire posture, but that still falls short of a WATCH. A separate official LPEA outage affecting one customer near Durango is operational context only, with no posted fire-weather or PSPS cause.
- Uncertainty: These outputs are screening estimates from public sources, the forecast changed materially versus the prior run, and no confirmed PSPS events are available yet for calibration.
- Evidence used: overall_status, weather_peaks, official_alerts, forecast_change, lpea_context, fire_posture, calibration
- This interpretation cannot change the deterministic tiers, scores, official alerts, or notification decision.

Changing drivers:
- Thu, Jul 23 worsened to ELEVATED near Bayfield / east La Plata County as wind edged higher and humidity eased slightly.
- Tue, Jul 21 also worsened to ELEVATED near Chimney Rock / west county despite no WATCH-level signal.
- Official fire posture remains STAGE 2 with VERY HIGH fire danger, which adds preparedness context but does not create an official alert or PSPS watch by itself.
- A localized LPEA outage near Durango is active, but the public data does not identify a fire-weather or PSPS cause.

What to watch next:
- Recheck whether Thu, Jul 23 near Bayfield climbs from ELEVATED toward WATCH if wind increases or humidity drops further.
- Watch whether Tue, Jul 21 near Chimney Rock keeps its ELEVATED screening signal in the next run.
- Confirm whether the Durango-area outage clears or gains any fire-weather or PSPS explanation.
- Check for any new official COZ295 fire-weather alerts; the current official fire-alert count is zero.

## Trend Intelligence

- Summary: Momentum is rising versus the prior run (Jul 18 at 5:25 AM MDT); forecast volatility is high and first WATCH-or-higher date is not present.
- Momentum: **Rising**
- Forecast volatility: **HIGH** (35/100)
- First WATCH-or-higher PSPS date: None
- Watch-date movement: No WATCH-or-higher PSPS dates in current or prior run.
- Method: compares current forecast evidence against prior local forecast history.

Notable changes:
- No WATCH-or-higher PSPS dates in current or prior run.
- Thu, Jul 23: worsening vs prior run; PSPS LOW -> ELEVATED; score +8, wind +1 mph, RH -1%, red-flag hours 0. Driver shifted to Bayfield / east La Plata County.
- Tue, Jul 21: worsening vs prior run; PSPS LOW -> ELEVATED; score +6, wind -1 mph, RH -1%, red-flag hours 0. Driver shifted to Chimney Rock / west county.
- Sat, Jul 18: easing vs prior run; PSPS LOW -> LOW; score 0, wind -1 mph, RH +5%, red-flag hours 0.

## Public Analysis Export

- Summary: Highest LPEA PSPS concern is Thu, Jul 23 near Bayfield / east La Plata County (ELEVATED 20/100), driven by near-threshold wind/gust signal near 21 mph; Official fire-posture context for Bayfield / east La Plata County is escalated (STAGE 2; fire danger VERY HIGH); it adds a small preparedness modifier but does not create a PSPS WATCH by itself.
- Trend: Momentum is rising versus the prior run (Jul 18 at 5:25 AM MDT); forecast volatility is high and first WATCH-or-higher date is not present.
- Confidence: **MEDIUM** (69/100)
- First WATCH-or-higher PSPS date: None
- PSPS peak: Thu, Jul 23 near Bayfield / east La Plata County at ELEVATED 20/100
- Red Flag peak: Thu, Jul 23 near Bayfield / east La Plata County at LOW 8/100
- Weather fire-potential peak: Thu, Jul 23 near Bayfield / east La Plata County at MODERATE 36/100
- LPEA operational outage context: 1 active outage; 0 planned and 1 unplanned; 1 customer out. No fire-weather or PSPS cause is identified.
- Public JSON: `archuleta_red_flag_monitor/public_analysis_export.json`

What changed:
- No WATCH-or-higher PSPS dates in current or prior run.
- Thu, Jul 23: worsening vs prior run; PSPS LOW -> ELEVATED; score +8, wind +1 mph, RH -1%, red-flag hours 0. Driver shifted to Bayfield / east La Plata County.
- Tue, Jul 21: worsening vs prior run; PSPS LOW -> ELEVATED; score +6, wind -1 mph, RH -1%, red-flag hours 0. Driver shifted to Chimney Rock / west county.
- Sat, Jul 18: easing vs prior run; PSPS LOW -> LOW; score 0, wind -1 mph, RH +5%, red-flag hours 0.

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
| Sat, Jul 18 | LOW | Durango / La Plata County (LOW 12/100); Ignacio / southeast La Plata County (LOW 12/100); Pagosa Springs (LOW 4/100) | Top weather score 8/100 at Durango / La Plata County. Weather score 8/100: RH 42%, wind/gust 15 mph, red-flag hours 0, near-threshold hours 0. |
| Sun, Jul 19 | LOW | Durango / La Plata County (LOW 12/100); Bayfield / east La Plata County (LOW 12/100); Ignacio / southeast La Plata County (LOW 12/100) | Top weather score 8/100 at Durango / La Plata County. Weather score 8/100: RH 30%, wind/gust 16 mph, red-flag hours 0, near-threshold hours 0. |
| Mon, Jul 20 | LOW | Chimney Rock / west county (LOW 12/100); Durango / La Plata County (LOW 12/100); Pagosa Springs (LOW 4/100) | Top weather score 8/100 at Chimney Rock / west county. Weather score 8/100: RH 24%, wind/gust 15 mph, red-flag hours 0, near-threshold hours 0. |
| Tue, Jul 21 | ELEVATED | Chimney Rock / west county (ELEVATED 18/100); Pagosa Springs (LOW 12/100); Arboles / southwest county (LOW 12/100) | Top weather score 14/100 at Chimney Rock / west county. Weather score 14/100: RH 22%, wind/gust 16 mph, red-flag hours 0, near-threshold hours 0. |
| Wed, Jul 22 | LOW | Pagosa Springs (LOW 12/100); Arboles / southwest county (LOW 12/100); Chimney Rock / west county (LOW 12/100) | Top weather score 8/100 at Pagosa Springs. Weather score 8/100: RH 30%, wind/gust 16 mph, red-flag hours 0, near-threshold hours 0. |
| Thu, Jul 23 | ELEVATED | Bayfield / east La Plata County (ELEVATED 20/100); Pagosa Springs (LOW 12/100); Arboles / southwest county (LOW 12/100) | Top weather score 16/100 at Bayfield / east La Plata County. Weather score 16/100: RH 31%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 0. |
| Fri, Jul 24 | ELEVATED | Chimney Rock / west county (ELEVATED 18/100); Pagosa Springs (LOW 12/100); Arboles / southwest county (LOW 12/100) | Top weather score 14/100 at Chimney Rock / west county. Weather score 14/100: RH 22%, wind/gust 17 mph, red-flag hours 0, near-threshold hours 0. |

## Area-Specific Outlook

| Area | Today | Peak this run | Highest-risk window |
| --- | --- | --- | --- |
| Bayfield | LOW 4/100 | Thu, Jul 23: ELEVATED 20/100 | Peak ingredients near 4 PM local; RH 31%, wind 21 mph. |
| Chimney Rock | LOW 4/100 | Tue, Jul 21: ELEVATED 18/100 | Peak ingredients near 3 PM local; RH 22%, wind 16 mph. |
| Pagosa Springs | LOW 4/100 | Tue, Jul 21: LOW 12/100 | Peak ingredients near 3 PM local; RH 26%, wind 15 mph. |
| Arboles | LOW 4/100 | Tue, Jul 21: LOW 12/100 | Peak ingredients near 3 PM local; RH 26%, wind 16 mph. |
| Piedra | LOW 4/100 | Tue, Jul 21: LOW 12/100 | Peak ingredients near 1 PM local; RH 29%, wind 15 mph. |
| Chromo | LOW 4/100 | Thu, Jul 23: LOW 12/100 | Peak ingredients near 4 PM local; RH 30%, wind 15 mph. |
| Durango | LOW 12/100 | Sat, Jul 18: LOW 12/100 | Peak ingredients near 5 PM local; RH 42%, wind 15 mph. |
| Ignacio | LOW 12/100 | Sat, Jul 18: LOW 12/100 | Peak ingredients near 5 PM local; RH 45%, wind 15 mph. |

## Fire Posture + Restrictions

- Summary: 4 official sources indicate fire restrictions or staged restrictions.
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
- [Hydrologic Outlook](https://api.weather.gov/alerts/urn:oid:2.49.0.1.840.0.0dfc703053d10c59ca42cf2de6665405cf8552c5.001.1): Hydrologic Outlook issued July 18 at 11:29AM MDT by NWS Grand Junction CO; 2026-07-18T11:29:00-06:00 to 2026-07-19T21:00:00-06:00; zones COC007, COC029, COC033, COC045, COC051, COC053, COC067, COC077, COC081, COC083, COC085, COC091, COC103, COC107, COC111, COC113, UTC019, UTC037
- [Hydrologic Outlook](https://api.weather.gov/alerts/urn:oid:2.49.0.1.840.0.d931ddebe19c0cfec86ec5b05b883c945c796270.001.1): Hydrologic Outlook issued July 17 at 4:35PM MDT by NWS Grand Junction CO; 2026-07-17T16:35:00-06:00 to 2026-07-19T21:00:00-06:00; zones COC007, COC029, COC033, COC045, COC051, COC053, COC067, COC077, COC081, COC083, COC085, COC091, COC103, COC107, COC111, COC113, UTC019, UTC037

## LPEA Power Signal

- Status: `operational_outage_active` - Official LPEA outage data indicates an operational outage; use as grid context, not PSPS/fire evidence unless LPEA identifies that cause.
- Meaning: Active source match means a monitored LPEA active/update source currently contains fire, outage, PSPS, or power-interruption keywords. Operational outages are shown separately and are not treated as PSPS/fire evidence unless the source text says so.
- Operational outage context: 1 active outage; 0 planned and 1 unplanned; 1 customer out. No fire-weather or PSPS cause is identified.
- Source coverage: 13 sources; 5/5 official social sources reachable
- Evidence quality: 0 operational, 3 active/update, 0 archive/context, 6 reference source matches.
- Operational outage source links: [138 FAT DOG LN](https://outage.lpea.coop)
- Active/update source pages with matches: LPEA homepage (red flag, public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation); LPEA LinkedIn (wildfire, fire mitigation)
- Distinct active/update signals: LPEA homepage (red flag, public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation); LPEA LinkedIn (wildfire, fire mitigation); LPEA LinkedIn (wildfire, fire mitigation)
- Example signal: ...tings & Resources Board Committees Voting Districts Policies & Bylaws Elections Red Flag Conditions May Result in Longer, More Frequent Outages Learn Why That's a Good Thing LPEA Announces 2026-27 Board Leade...
- Reference/context hits: [LPEA outage center](https://lpea.coop/outage-center); [LPEA wildfire / public safety power shutoffs](https://lpea.coop/psps); [LPEA red flag outage impact page](https://lpea.coop/outages/red-flag-warnings-and-impact-outages-prioritizing-safety-our-members); [LPEA fire mitigation](https://lpea.coop/fire-mitigation); [LPEA latest news](https://lpea.coop/Posts)

**Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## Next 7 Days

| Date | Tier | Main reason | Worst sampled metrics |
| --- | --- | --- | --- |
| Sat, Jul 18 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 36%, wind/gust 10 mph, thunder 37%<br>Arboles / southwest county: RH 42%, wind/gust 14 mph, thunder 33%<br>Chimney Rock / west county: RH 36%, wind/gust 13 mph, thunder 38% |
| Sun, Jul 19 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 26%, wind/gust 12 mph, thunder 24%<br>Arboles / southwest county: RH 26%, wind/gust 14 mph, thunder 18%<br>Chimney Rock / west county: RH 23%, wind/gust 14 mph, thunder 25% |
| Mon, Jul 20 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 27%, wind/gust 12 mph, thunder 15%<br>Arboles / southwest county: RH 26%, wind/gust 13 mph, thunder 37%<br>Chimney Rock / west county: RH 24%, wind/gust 15 mph, thunder 24% |
| Tue, Jul 21 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 26%, wind/gust 15 mph, thunder 42%<br>Arboles / southwest county: RH 26%, wind/gust 16 mph, thunder 48%<br>Chimney Rock / west county: RH 22%, wind/gust 16 mph, thunder 46% |
| Wed, Jul 22 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 30%, wind/gust 16 mph, thunder 37%<br>Arboles / southwest county: RH 29%, wind/gust 16 mph, thunder 36%<br>Chimney Rock / west county: RH 26%, wind/gust 16 mph, thunder 36% |
| Thu, Jul 23 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 29%, wind/gust 17 mph, thunder 26%<br>Arboles / southwest county: RH 28%, wind/gust 20 mph, thunder 15%<br>Chimney Rock / west county: RH 25%, wind/gust 18 mph, thunder 22% |
| Fri, Jul 24 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 27%, wind/gust 16 mph, thunder 44%<br>Arboles / southwest county: RH 24%, wind/gust 18 mph, thunder 34%<br>Chimney Rock / west county: RH 22%, wind/gust 17 mph, thunder 38% |

## Sample Point Status

- Pagosa Springs: COZ295 (matches), forecast zone COZ023, county zone COC007
- Arboles / southwest county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Chimney Rock / west county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Piedra / north county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Chromo / southeast county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Durango / La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Bayfield / east La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Ignacio / southeast La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
