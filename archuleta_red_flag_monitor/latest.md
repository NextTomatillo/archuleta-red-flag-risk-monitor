# Archuleta County fire-weather monitor

Generated: Aug 12, 2026 at 6:11 PM MDT (Pagosa Springs, CO local time)
Next update: Aug 13, 2026 at 5:20 AM MDT (Pagosa Springs, CO local time)
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
- ELEVATED dates: Tue, Aug 18
- Official NWS Red Flag / Fire Weather alerts (COZ295): 0
- LPEA signal: `active_keyword_match` - LPEA active/update sources contained power-interruption keywords; review source before treating as confirmed outage intent.
- LPEA source coverage: 13 sources; 5/5 official social sources reachable
- Current Archuleta County wildfires: 2
- Official evacuation notices: No current evacuation order or warning detected in the checked official county feeds.
- NWS discussion: No concerning fire-weather language found in latest GJT discussion.

## Decision Support

- Summary: Highest LPEA PSPS concern is Tue, Aug 18 near Arboles / southwest county (ELEVATED 34/100), driven by near-threshold wind/gust signal near 21 mph; near-threshold RH near 18%; modest coincident dry-thunder signal near 17%. NIFC reports 2 current wildfires in Archuleta County.
- Confidence: **MEDIUM** (69/100) - 8/8 sampled weather points available; 7/7 fire-posture sources reachable; official NWS alert zones checked; 13/13 LPEA public sources reachable; LPEA active/update sources checked; authoritative NIFC current-incident feed checked for Archuleta County; official Archuleta County evacuation feeds checked; forecast changed substantially versus prior run; no confirmed PSPS events logged yet for calibration
- Weather fire-potential peak: Tue, Aug 18: Durango / La Plata County MODERATE 44/100
- Red Flag likelihood peak: Tue, Aug 18: Arboles / southwest county LOW 25/100
- LPEA PSPS peak: Tue, Aug 18: Arboles / southwest county ELEVATED 34/100
- Method: rules-based decision support using public weather, fire-posture, and LPEA source signals; scores are screening estimates, not official or statistically calibrated probabilities.

| Date | Weather fire potential | Red Flag likelihood | LPEA PSPS | Main window |
| --- | --- | --- | --- | --- |
| Wed, Aug 12 | Pagosa Springs: LOW 24/100 | Pagosa Springs: LOW 0/100 | Pagosa Springs: LOW 12/100 | Peak ingredients near 6 PM local; RH 33%, wind 17 mph. |
| Thu, Aug 13 | Durango / La Plata County: MODERATE 36/100 | Durango / La Plata County: LOW 8/100 | Durango / La Plata County: ELEVATED 20/100 | Peak ingredients near 3 PM local; RH 35%, wind 22 mph. |
| Fri, Aug 14 | Durango / La Plata County: MODERATE 36/100 | Durango / La Plata County: LOW 8/100 | Durango / La Plata County: ELEVATED 20/100 | Peak ingredients near 3 PM local; RH 30%, wind 22 mph. |
| Sat, Aug 15 | Chimney Rock / west county: MODERATE 38/100 | Arboles / southwest county: LOW 8/100 | Arboles / southwest county: ELEVATED 24/100 | Peak ingredients near 4 PM local; RH 22%, wind 22 mph. |
| Sun, Aug 16 | Bayfield / east La Plata County: LOW 30/100 | Arboles / southwest county: LOW 8/100 | Arboles / southwest county: ELEVATED 24/100 | Peak ingredients near 4 PM local; RH 22%, wind 21 mph. |
| Mon, Aug 17 | Chimney Rock / west county: LOW 26/100 | Ignacio / southeast La Plata County: LOW 8/100 | Arboles / southwest county: LOW 16/100 | Peak ingredients near 4 PM local; RH 21%, wind 20 mph. |
| Tue, Aug 18 | Durango / La Plata County: MODERATE 44/100 | Arboles / southwest county: LOW 25/100 | Arboles / southwest county: ELEVATED 34/100 | 4 PM-4 PM local; 1 near/red-flag threshold hour. |

## Analyst Interpretation

- Headline: Screening is ELEVATED for Tuesday near Arboles, while official sources show no COZ295 fire alert, active LPEA outage, or evacuation notice.
- Summary: Tuesday is the screening peak: PSPS ELEVATED 34/100 near Arboles and Red Flag LOW 25/100, with RH near 18%, wind near 21 mph, and a modest dry-thunder signal. An official Flood Watch is active for mountain zones, but the COZ295 fire-alert count is zero and LPEA lists no active customer outages. NIFC reports Rio Blanco at about 1,388 acres and 91% contained plus the 0.10-acre Gunsight incident; no evacuation notice was detected.
- Uncertainty: PSPS estimates are not calibrated to confirmed LPEA shutoffs: no confirmed events are logged, 56 past WATCH/LIKELY days were false watches, and forecast volatility is HIGH at 39/100.
- Evidence used: overall_status, weather_peaks, official_alerts, forecast_change, lpea_context, fire_posture, active_incidents, calibration
- This interpretation cannot change the deterministic tiers, scores, official alerts, or notification decision.

Changing drivers:
- Today and Monday eased to LOW, while Tuesday rose 12 points but remained ELEVATED.
- Tuesday's peak shifted to Arboles, with RH near 18%, wind near 21 mph, and one near-threshold hour.
- Official fire posture remains Stage 2 with VERY HIGH fire danger.
- Two current wildfires are reported; no evacuation notice was detected.

What to watch next:
- Recheck Tuesday near Arboles for movement toward PSPS WATCH or Red Flag thresholds.
- Monitor the official Flood Watch through midnight and check for any new NWS fire-weather alert.
- Check the official LPEA outage viewer for operational changes; the current keyword match is not outage intent.
- Monitor Rio Blanco and Gunsight updates and any official evacuation directive.

## Trend Intelligence

- Summary: Momentum is easing versus the prior run (Aug 12 at 6:36 AM MDT); forecast volatility is high and first WATCH-or-higher date is not present.
- Momentum: **Easing**
- Forecast volatility: **HIGH** (39/100)
- First WATCH-or-higher PSPS date: None
- Watch-date movement: No WATCH-or-higher PSPS dates in current or prior run.
- Method: compares current forecast evidence against prior local forecast history.

Notable changes:
- No WATCH-or-higher PSPS dates in current or prior run.
- Wed, Aug 12: easing vs prior run; PSPS ELEVATED -> LOW; score -8, wind -2 mph, RH +2%, red-flag hours 0. Driver shifted to Pagosa Springs.
- Mon, Aug 17: easing vs prior run; PSPS ELEVATED -> LOW; score -6, wind 0 mph, RH +1%, red-flag hours 0.
- Tue, Aug 18: worsening vs prior run; PSPS ELEVATED -> ELEVATED; score +12, wind 0 mph, RH -1%, red-flag hours 0. Driver shifted to Arboles / southwest county.

## Public Analysis Export

- Summary: Highest LPEA PSPS concern is Tue, Aug 18 near Arboles / southwest county (ELEVATED 34/100), driven by near-threshold wind/gust signal near 21 mph; near-threshold RH near 18%; modest coincident dry-thunder signal near 17%. NIFC reports 2 current wildfires in Archuleta County.
- Trend: Momentum is easing versus the prior run (Aug 12 at 6:36 AM MDT); forecast volatility is high and first WATCH-or-higher date is not present.
- Confidence: **MEDIUM** (69/100)
- First WATCH-or-higher PSPS date: None
- PSPS peak: Tue, Aug 18 near Arboles / southwest county at ELEVATED 34/100
- Red Flag peak: Tue, Aug 18 near Arboles / southwest county at LOW 25/100
- Weather fire-potential peak: Tue, Aug 18 near Durango / La Plata County at MODERATE 44/100
- LPEA operational outage context: No active outages are listed by the official LPEA outage viewer.
- Public JSON: `archuleta_red_flag_monitor/public_analysis_export.json`

What changed:
- No WATCH-or-higher PSPS dates in current or prior run.
- Wed, Aug 12: easing vs prior run; PSPS ELEVATED -> LOW; score -8, wind -2 mph, RH +2%, red-flag hours 0. Driver shifted to Pagosa Springs.
- Mon, Aug 17: easing vs prior run; PSPS ELEVATED -> LOW; score -6, wind 0 mph, RH +1%, red-flag hours 0.
- Tue, Aug 18: worsening vs prior run; PSPS ELEVATED -> ELEVATED; score +12, wind 0 mph, RH -1%, red-flag hours 0. Driver shifted to Arboles / southwest county.

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
| Wed, Aug 12 | LOW | Pagosa Springs (LOW 12/100); Durango / La Plata County (LOW 12/100); Arboles / southwest county (LOW 10/100) | Top weather score 8/100 at Pagosa Springs. Weather score 8/100: RH 33%, wind/gust 17 mph, red-flag hours 0, near-threshold hours 0. |
| Thu, Aug 13 | ELEVATED | Durango / La Plata County (ELEVATED 20/100); Arboles / southwest county (ELEVATED 18/100); Chimney Rock / west county (ELEVATED 18/100) | Top weather score 16/100 at Arboles / southwest county. Weather score 16/100: RH 25%, wind/gust 22 mph, red-flag hours 0, near-threshold hours 0. |
| Fri, Aug 14 | ELEVATED | Durango / La Plata County (ELEVATED 20/100); Arboles / southwest county (ELEVATED 18/100); Chimney Rock / west county (ELEVATED 18/100) | Top weather score 16/100 at Arboles / southwest county. Weather score 16/100: RH 26%, wind/gust 23 mph, red-flag hours 0, near-threshold hours 0. |
| Sat, Aug 15 | ELEVATED | Arboles / southwest county (ELEVATED 24/100); Chimney Rock / west county (ELEVATED 24/100); Pagosa Springs (ELEVATED 20/100) | Top weather score 22/100 at Arboles / southwest county. Weather score 22/100: RH 22%, wind/gust 22 mph, red-flag hours 0, near-threshold hours 0. |
| Sun, Aug 16 | ELEVATED | Arboles / southwest county (ELEVATED 24/100); Bayfield / east La Plata County (ELEVATED 18/100); Ignacio / southeast La Plata County (LOW 16/100) | Top weather score 22/100 at Arboles / southwest county. Weather score 22/100: RH 22%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 0. |
| Mon, Aug 17 | LOW | Ignacio / southeast La Plata County (LOW 16/100); Arboles / southwest county (LOW 16/100); Chimney Rock / west county (LOW 16/100) | Top weather score 16/100 at Ignacio / southeast La Plata County. Weather score 16/100: RH 23%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 0. |
| Tue, Aug 18 | ELEVATED | Arboles / southwest county (ELEVATED 34/100); Durango / La Plata County (ELEVATED 26/100); Ignacio / southeast La Plata County (ELEVATED 22/100) | Top weather score 32/100 at Arboles / southwest county. Weather score 32/100: RH 18%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 1. |

## Area-Specific Outlook

| Area | Today | Peak this run | Highest-risk window |
| --- | --- | --- | --- |
| Arboles | LOW 10/100 | Tue, Aug 18: ELEVATED 34/100 | 4 PM-4 PM local; 1 near/red-flag threshold hour. |
| Durango | LOW 12/100 | Tue, Aug 18: ELEVATED 26/100 | Peak ingredients near 4 PM local; RH 20%, wind 21 mph. |
| Chimney Rock | LOW 10/100 | Sat, Aug 15: ELEVATED 24/100 | Peak ingredients near 4 PM local; RH 20%, wind 21 mph. |
| Ignacio | LOW 8/100 | Tue, Aug 18: ELEVATED 22/100 | Peak ingredients near 4 PM local; RH 19%, wind 21 mph. |
| Pagosa Springs | LOW 12/100 | Sat, Aug 15: ELEVATED 20/100 | Peak ingredients near 4 PM local; RH 27%, wind 21 mph. |
| Bayfield | LOW 10/100 | Thu, Aug 13: ELEVATED 18/100 | Peak ingredients near 4 PM local; RH 34%, wind 23 mph. |
| Piedra | LOW 10/100 | Wed, Aug 12: LOW 10/100 | Peak ingredients near 6 PM local; RH 32%, wind 15 mph. |
| Chromo | LOW 10/100 | Wed, Aug 12: LOW 10/100 | Peak ingredients near 6 PM local; RH 34%, wind 15 mph. |

## Current Fires + Evacuations

- Incident summary: 2 current wildfires reported in Archuleta County; no current evacuation notice detected in checked county feeds.
- Evacuation status: **NONE DETECTED** - No current evacuation order or warning detected in the checked official county feeds.
- Safety note: Current incidents and evacuation notices are operational context. They do not raise PSPS scores by themselves; follow official evacuation instructions immediately.

### Current NIFC Incidents

| Incident | Type | Size | Containment | Nearest monitored area | Updated |
| --- | --- | --- | --- | --- | --- |
| Rio Blanco | Wildfire | 1,387.74 acres | 91% | Chromo / southeast county (9.9 mi) | Aug 11 at 4:14 PM MDT |
| Gunsight | Wildfire | 0.10 acres | Not reported | Pagosa Springs (15.4 mi) | Aug 12 at 2:17 PM MDT |

Official links: [NIFC map](https://www.nifc.gov/fire-information/maps), [Archuleta County fire updates](https://sheriff.archuletacounty.gov/divisions/emergency-operations/fire-updates-and-information/), [County alerts](https://nixle.us/archuleta-county-office-of-emergency-management-aux/), [Watch Duty](https://app.watchduty.org/)

## Fire Posture + Restrictions

- Summary: 4 official sources indicate fire restrictions or staged restrictions.
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
| Durango | STAGE 2 | UNKNOWN | [City of Durango](https://www.durangoco.gov/) |
| Southern Ute / Ignacio | UNKNOWN | UNKNOWN | [Southern Ute Indian Tribe](https://www.southernute-nsn.gov/) |

## Forecast Calibration

### PSPS Calibration

- Summary: No confirmed LPEA PSPS events logged yet; calibration will start once events are added.
- Confirmed PSPS events logged: 0
- Candidate/unconfirmed events logged: 0
- WATCH/LIKELY false-watch past days: 56
- Pending WATCH/LIKELY dates in current forecast: None
- Calibration source: manual PSPS event log plus forecast history from prior monitor runs.

### Red Flag / Fire Weather Calibration

- Summary: 3/3 official Red Flag / Fire Weather episodes had a pre-alert HIGH monitor signal; date-level result was 21/21. Episode-average lead time: 3.5 days.
- Official alert episodes logged: 3 (21 alert dates)
- Episode-level pre-alert HIGH hit rate: 100%
- Date-level pre-alert HIGH hit rate: 100%
- Episode-level average lead time: 3.5 days
- HIGH false-watch past days: 20
- Pending HIGH dates in current forecast: None
- Calibration source: official NWS Red Flag / Fire Weather alert dates plus forecast history from prior monitor runs.

## Official Weather Alerts

- Monitored NWS zones: COC007, COC067, COZ019, COZ022, COZ023, COZ295
- [Flood Watch](https://api.weather.gov/alerts/urn:oid:2.49.0.1.840.0.cc7be630582fcd5ec76ded79501bdba320f000bf.001.1): Flood Watch issued August 12 at 11:46AM MDT until August 13 at 12:00AM MDT by NWS Grand Junction CO; 2026-08-12T11:46:00-06:00 to 2026-08-13T00:00:00-06:00; zones COZ018, COZ019

## LPEA Power Signal

- Status: `active_keyword_match` - LPEA active/update sources contained power-interruption keywords; review source before treating as confirmed outage intent.
- Meaning: Active source match means a monitored LPEA active/update source currently contains fire, outage, PSPS, or power-interruption keywords. Operational outages are shown separately and are not treated as PSPS/fire evidence unless the source text says so.
- Operational outage context: No active outages are listed by the official LPEA outage viewer.
- Source coverage: 13 sources; 5/5 official social sources reachable
- Evidence quality: 0 operational, 4 active/update, 0 archive/context, 6 reference source matches.
- Active/update source pages with matches: LPEA homepage (public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation, restoration); LPEA X (power outage, outage map, high winds, restore power); LPEA LinkedIn (wildfire, fire mitigation)
- Distinct active/update signals: LPEA X (power outage, outage map, high winds, restore power); LPEA X (power outage, outage map, high winds, restore power); LPEA LinkedIn (wildfire, fire mitigation); LPEA LinkedIn (wildfire, fire mitigation)
- Example signal: ...ibrary! 1 2 522 LPEA @LaPlataElectric May 7, 2024 LPEA members are experiencing power outages in the Bayfield and Pagosa Springs areas. Approximately 200 meters are out and it is suspected that the high winds are...
- Reference/context hits: [LPEA outage center](https://lpea.coop/outage-center); [LPEA wildfire / public safety power shutoffs](https://lpea.coop/psps); [LPEA red flag outage impact page](https://lpea.coop/outages/red-flag-warnings-and-impact-outages-prioritizing-safety-our-members); [LPEA fire mitigation](https://lpea.coop/fire-mitigation); [LPEA latest news](https://lpea.coop/Posts)

**Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## Next 7 Days

| Date | Tier | Main reason | Worst sampled metrics |
| --- | --- | --- | --- |
| Wed, Aug 12 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 33%, wind/gust 17 mph, thunder 30%<br>Arboles / southwest county: RH 26%, wind/gust 20 mph, thunder 42%<br>Chimney Rock / west county: RH 23%, wind/gust 18 mph, thunder 42% |
| Thu, Aug 13 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 36%, wind/gust 20 mph, thunder 46%<br>Arboles / southwest county: RH 25%, wind/gust 22 mph, thunder 30%<br>Chimney Rock / west county: RH 27%, wind/gust 21 mph, thunder 35% |
| Fri, Aug 14 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 33%, wind/gust 20 mph, thunder 52%<br>Arboles / southwest county: RH 26%, wind/gust 23 mph, thunder 29%<br>Chimney Rock / west county: RH 24%, wind/gust 21 mph, thunder 38% |
| Sat, Aug 15 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 27%, wind/gust 21 mph, thunder 33%<br>Arboles / southwest county: RH 22%, wind/gust 22 mph, thunder 12%<br>Chimney Rock / west county: RH 20%, wind/gust 21 mph, thunder 22% |
| Sun, Aug 16 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 30%, wind/gust 18 mph, thunder 48%<br>Arboles / southwest county: RH 22%, wind/gust 21 mph, thunder 39%<br>Chimney Rock / west county: RH 21%, wind/gust 18 mph, thunder 43% |
| Mon, Aug 17 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 29%, wind/gust 16 mph, thunder 52%<br>Arboles / southwest county: RH 21%, wind/gust 20 mph, thunder 32%<br>Chimney Rock / west county: RH 20%, wind/gust 18 mph, thunder 43% |
| Tue, Aug 18 | ELEVATED | Arboles / southwest county: Elevated ingredient present: dry-thunder probability reaches 17%. | Arboles / southwest county: RH 18%, wind/gust 21 mph, thunder 26% |

## Sample Point Status

- Pagosa Springs: COZ295 (matches), forecast zone COZ023, county zone COC007
- Arboles / southwest county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Chimney Rock / west county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Piedra / north county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Chromo / southeast county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Durango / La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Bayfield / east La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Ignacio / southeast La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
