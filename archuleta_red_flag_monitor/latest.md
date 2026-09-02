# Archuleta County fire-weather monitor

Generated: Sep 2, 2026 at 5:40 AM MDT (Pagosa Springs, CO local time)
Next update: Sep 2, 2026 at 5:20 PM MDT (Pagosa Springs, CO local time)
Date/time basis: Pagosa Springs, CO local time (America/Denver)
> **Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## At A Glance

- Fire-weather tier: **ELEVATED**
- PSPS likelihood: **ELEVATED**
- PSPS likely dates: None
- PSPS watch dates: None
- Monitor heads-up recommended: **NO** - No material alert, fire, evacuation, significant outage, CONCERN/HIGH weather, or WATCH/LIKELY PSPS signal is present.
- HIGH dates: None
- CONCERN dates: None
- ELEVATED dates: Wed, Sep 2
- Official NWS Red Flag / Fire Weather alerts (COZ295): 0
- LPEA signal: `active_keyword_match` - LPEA active/update sources contained power-interruption keywords; review source before treating as confirmed outage intent.
- LPEA source coverage: 13 sources; 4/5 official social sources reachable
- Current Archuleta County wildfires: 0
- Official evacuation notices: No current evacuation order or warning detected in the checked official county feeds.
- NWS discussion: No concerning fire-weather language found in latest GJT discussion.

## Decision Support

- Summary: Highest LPEA PSPS concern is Wed, Sep 2 near Arboles / southwest county (ELEVATED 33/100), driven by red-flag wind/gust signal near 25 mph; dry RH near 21%; Official fire-posture context for Arboles / southwest county is elevated (STAGE 1; fire danger UNKNOWN), used as a small supporting modifier.
- Confidence: **MEDIUM** (74/100) - 8/8 sampled weather points available; 7/7 fire-posture sources reachable; official NWS alert zones checked; 12/13 LPEA public sources reachable; LPEA active/update sources checked; authoritative NIFC current-incident feed checked for Archuleta County; official Archuleta County evacuation feeds checked; forecast changed moderately versus prior run; no confirmed PSPS events logged yet for calibration
- Weather fire-potential peak: Wed, Sep 2: Arboles / southwest county MODERATE 37/100
- Red Flag likelihood peak: Wed, Sep 2: Arboles / southwest county LOW 25/100
- LPEA PSPS peak: Wed, Sep 2: Arboles / southwest county ELEVATED 33/100
- Method: rules-based decision support using public weather, fire-posture, and LPEA source signals; scores are screening estimates, not official or statistically calibrated probabilities.

| Date | Weather fire potential | Red Flag likelihood | LPEA PSPS | Main window |
| --- | --- | --- | --- | --- |
| Wed, Sep 2 | Arboles / southwest county: MODERATE 37/100 | Arboles / southwest county: LOW 25/100 | Arboles / southwest county: ELEVATED 33/100 | Peak ingredients near 3 PM local; RH 21%, wind 25 mph. |
| Thu, Sep 3 | Chimney Rock / west county: LOW 34/100 | Arboles / southwest county: LOW 8/100 | Arboles / southwest county: ELEVATED 24/100 | Peak ingredients near 3 PM local; RH 20%, wind 23 mph. |
| Fri, Sep 4 | Pagosa Springs: LOW 26/100 | Pagosa Springs: LOW 8/100 | Pagosa Springs: ELEVATED 18/100 | Peak ingredients near 3 PM local; RH 30%, wind 21 mph. |
| Sat, Sep 5 | Chimney Rock / west county: LOW 34/100 | Chimney Rock / west county: LOW 8/100 | Chimney Rock / west county: ELEVATED 24/100 | Peak ingredients near 4 PM local; RH 21%, wind 21 mph. |
| Sun, Sep 6 | Durango / La Plata County: LOW 26/100 | Arboles / southwest county: LOW 8/100 | Arboles / southwest county: ELEVATED 18/100 | Peak ingredients near 4 PM local; RH 24%, wind 21 mph. |
| Mon, Sep 7 | Chimney Rock / west county: LOW 26/100 | Arboles / southwest county: LOW 8/100 | Arboles / southwest county: ELEVATED 18/100 | Peak ingredients near 4 PM local; RH 28%, wind 22 mph. |
| Tue, Sep 8 | Durango / La Plata County: LOW 26/100 | Arboles / southwest county: LOW 8/100 | Arboles / southwest county: ELEVATED 18/100 | Peak ingredients near 4 PM local; RH 28%, wind 22 mph. |

## Analyst Interpretation

- Headline: Fire-weather and PSPS screening are ELEVATED, with no official COZ295 alerts, active LPEA outages, current county fires, or evacuation notices.
- Summary: Sep 2 near Arboles is the peak: fire potential MODERATE 37/100, Red Flag screening LOW 25/100, and PSPS screening ELEVATED 33/100. Sep 3 eased from the prior run, no WATCH-or-higher PSPS date is present, and official NWS alerts and LPEA outages are clear. The checked NIFC feed reports no current Archuleta County wildfire, and no evacuation notice was detected.
- Uncertainty: These are rules-based screening estimates, not official warnings or calibrated PSPS probabilities; weather forecasts and public incident, alert, outage, and social-source data may change or lag.
- Evidence used: overall_status, weather_peaks, official_alerts, forecast_change, lpea_context, fire_posture, active_incidents, calibration
- This interpretation cannot change the deterministic tiers, scores, official alerts, or notification decision.

Changing drivers:
- Sep 2 near Arboles is the peak, with fire potential MODERATE 37/100 and PSPS screening ELEVATED 33/100.
- Sep 3 eased from the prior run, with the PSPS score down 16 points and no WATCH-or-higher date present.
- No official weather alert or LPEA outage is active; broad LPEA keyword matches remain context only.
- The checked NIFC feed reports no current Archuleta County wildfire, and no evacuation notice was detected.

What to watch next:
- Monitor Sep 2 near Arboles around 3 PM for changes from RH near 21% and wind near 25 mph.
- Watch whether Sep 3 continues to remain below CONCERN thresholds.
- Check LPEA directly for any new outage or PSPS notice rather than relying on keyword matches.
- Continue checking authoritative incident and county evacuation feeds.

## Trend Intelligence

- Summary: Momentum is steady versus the prior run (Sep 1 at 5:31 AM MDT); forecast volatility is medium and first WATCH-or-higher date is not present.
- Momentum: **Steady**
- Forecast volatility: **MEDIUM** (26/100)
- First WATCH-or-higher PSPS date: None
- Watch-date movement: No WATCH-or-higher PSPS dates in current or prior run.
- Method: compares current forecast evidence against prior local forecast history.

Notable changes:
- No WATCH-or-higher PSPS dates in current or prior run.
- Thu, Sep 3: easing vs prior run; PSPS ELEVATED -> ELEVATED; score -16, wind -1 mph, RH +2%, red-flag hours 0. Driver shifted to Arboles / southwest county.
- Sun, Sep 6: worsening vs prior run; PSPS ELEVATED -> ELEVATED; score 0, wind +1 mph, RH -5%, red-flag hours 0. Driver shifted to Arboles / southwest county.

## Public Analysis Export

- Summary: Highest LPEA PSPS concern is Wed, Sep 2 near Arboles / southwest county (ELEVATED 33/100), driven by red-flag wind/gust signal near 25 mph; dry RH near 21%; Official fire-posture context for Arboles / southwest county is elevated (STAGE 1; fire danger UNKNOWN), used as a small supporting modifier.
- Trend: Momentum is steady versus the prior run (Sep 1 at 5:31 AM MDT); forecast volatility is medium and first WATCH-or-higher date is not present.
- Confidence: **MEDIUM** (74/100)
- First WATCH-or-higher PSPS date: None
- PSPS peak: Wed, Sep 2 near Arboles / southwest county at ELEVATED 33/100
- Red Flag peak: Wed, Sep 2 near Arboles / southwest county at LOW 25/100
- Weather fire-potential peak: Wed, Sep 2 near Arboles / southwest county at MODERATE 37/100
- LPEA operational outage context: No active outages are listed by the official LPEA outage viewer.
- Public JSON: `archuleta_red_flag_monitor/public_analysis_export.json`

What changed:
- No WATCH-or-higher PSPS dates in current or prior run.
- Thu, Sep 3: easing vs prior run; PSPS ELEVATED -> ELEVATED; score -16, wind -1 mph, RH +2%, red-flag hours 0. Driver shifted to Arboles / southwest county.
- Sun, Sep 6: worsening vs prior run; PSPS ELEVATED -> ELEVATED; score 0, wind +1 mph, RH -5%, red-flag hours 0. Driver shifted to Arboles / southwest county.

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
| Wed, Sep 2 | ELEVATED | Arboles / southwest county (ELEVATED 33/100); Ignacio / southeast La Plata County (ELEVATED 31/100); Pagosa Springs (ELEVATED 27/100) | Top weather score 31/100 at Arboles / southwest county. Weather score 31/100: RH 21%, wind/gust 25 mph, red-flag hours 0, near-threshold hours 0. |
| Thu, Sep 3 | ELEVATED | Arboles / southwest county (ELEVATED 24/100); Chimney Rock / west county (ELEVATED 24/100); Ignacio / southeast La Plata County (ELEVATED 22/100) | Top weather score 22/100 at Arboles / southwest county. Weather score 22/100: RH 20%, wind/gust 23 mph, red-flag hours 0, near-threshold hours 0. |
| Fri, Sep 4 | ELEVATED | Pagosa Springs (ELEVATED 18/100); Arboles / southwest county (ELEVATED 18/100); Chimney Rock / west county (ELEVATED 18/100) | Top weather score 16/100 at Pagosa Springs. Weather score 16/100: RH 30%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 0. |
| Sat, Sep 5 | ELEVATED | Chimney Rock / west county (ELEVATED 24/100); Arboles / southwest county (ELEVATED 18/100); Durango / La Plata County (ELEVATED 18/100) | Top weather score 22/100 at Chimney Rock / west county. Weather score 22/100: RH 21%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 0. |
| Sun, Sep 6 | ELEVATED | Arboles / southwest county (ELEVATED 18/100); Durango / La Plata County (ELEVATED 18/100); Bayfield / east La Plata County (ELEVATED 18/100) | Top weather score 16/100 at Arboles / southwest county. Weather score 16/100: RH 24%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 0. |
| Mon, Sep 7 | ELEVATED | Arboles / southwest county (ELEVATED 18/100); Chimney Rock / west county (ELEVATED 18/100); Durango / La Plata County (ELEVATED 18/100) | Top weather score 16/100 at Arboles / southwest county. Weather score 16/100: RH 28%, wind/gust 22 mph, red-flag hours 0, near-threshold hours 0. |
| Tue, Sep 8 | ELEVATED | Arboles / southwest county (ELEVATED 18/100); Durango / La Plata County (ELEVATED 18/100); Bayfield / east La Plata County (ELEVATED 18/100) | Top weather score 16/100 at Arboles / southwest county. Weather score 16/100: RH 28%, wind/gust 22 mph, red-flag hours 0, near-threshold hours 0. |

## Area-Specific Outlook

| Area | Today | Peak this run | Highest-risk window |
| --- | --- | --- | --- |
| Arboles | ELEVATED 33/100 | Wed, Sep 2: ELEVATED 33/100 | Peak ingredients near 3 PM local; RH 21%, wind 25 mph. |
| Ignacio | ELEVATED 31/100 | Wed, Sep 2: ELEVATED 31/100 | Peak ingredients near 3 PM local; RH 22%, wind 26 mph. |
| Pagosa Springs | ELEVATED 27/100 | Wed, Sep 2: ELEVATED 27/100 | Peak ingredients near 3 PM local; RH 26%, wind 25 mph. |
| Durango | ELEVATED 27/100 | Wed, Sep 2: ELEVATED 27/100 | Peak ingredients near 2 PM local; RH 26%, wind 26 mph. |
| Bayfield | ELEVATED 27/100 | Wed, Sep 2: ELEVATED 27/100 | Peak ingredients near 4 PM local; RH 26%, wind 28 mph. |
| Chimney Rock | ELEVATED 24/100 | Wed, Sep 2: ELEVATED 24/100 | Peak ingredients near 3 PM local; RH 20%, wind 24 mph. |
| Piedra | ELEVATED 18/100 | Wed, Sep 2: ELEVATED 18/100 | Peak ingredients near 4 PM local; RH 28%, wind 24 mph. |
| Chromo | ELEVATED 18/100 | Wed, Sep 2: ELEVATED 18/100 | Peak ingredients near 4 PM local; RH 24%, wind 23 mph. |

## Current Fires + Evacuations

- Incident summary: No current wildfire reported in Archuleta County by the checked NIFC feed.
- Evacuation status: **NONE DETECTED** - No current evacuation order or warning detected in the checked official county feeds.
- Safety note: Current incidents and evacuation notices are operational context. They do not raise PSPS scores by themselves; follow official evacuation instructions immediately.

No current incidents were returned by the checked NIFC feed.

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
- WATCH/LIKELY false-watch past days: 71
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

- Status: `active_keyword_match` - LPEA active/update sources contained power-interruption keywords; review source before treating as confirmed outage intent.
- Meaning: Active source match means a monitored LPEA active/update source currently contains fire, outage, PSPS, or power-interruption keywords. Operational outages are shown separately and are not treated as PSPS/fire evidence unless the source text says so.
- Operational outage context: No active outages are listed by the official LPEA outage viewer.
- Source coverage: 13 sources; 4/5 official social sources reachable
- Evidence quality: 0 operational, 2 active/update, 0 archive/context, 6 reference source matches.
- Active/update source pages with matches: LPEA homepage (public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation, restoration); LPEA LinkedIn (wildfire, fire mitigation)
- Distinct active/update signals: LPEA LinkedIn (wildfire, fire mitigation); LPEA LinkedIn (wildfire, fire mitigation)
- Example signal: ...on (Kit Carson Electric, Montrose, and Farmington Electric) to compare notes on wildfire mitigation, advanced metering, and what it looks like to actually let members drive power supply decisions. Give it a l...
- Reference/context hits: [LPEA outage center](https://lpea.coop/outage-center); [LPEA wildfire / public safety power shutoffs](https://lpea.coop/psps); [LPEA red flag outage impact page](https://lpea.coop/outages/red-flag-warnings-and-impact-outages-prioritizing-safety-our-members); [LPEA fire mitigation](https://lpea.coop/fire-mitigation); [LPEA latest news](https://lpea.coop/Posts)

**Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## Next 7 Days

| Date | Tier | Main reason | Worst sampled metrics |
| --- | --- | --- | --- |
| Wed, Sep 2 | ELEVATED | Pagosa Springs: Elevated ingredient present: wind/gust forecast near 25 mph. | Pagosa Springs: RH 26%, wind/gust 25 mph, thunder 2%<br>Arboles / southwest county: RH 21%, wind/gust 25 mph, thunder 3%<br>Durango / La Plata County: RH 26%, wind/gust 26 mph, thunder 6% |
| Thu, Sep 3 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 25%, wind/gust 23 mph, thunder 7%<br>Arboles / southwest county: RH 20%, wind/gust 23 mph, thunder 9%<br>Chimney Rock / west county: RH 19%, wind/gust 22 mph, thunder 12% |
| Fri, Sep 4 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 30%, wind/gust 21 mph, thunder 29%<br>Arboles / southwest county: RH 25%, wind/gust 22 mph, thunder 22%<br>Chimney Rock / west county: RH 24%, wind/gust 22 mph, thunder 26% |
| Sat, Sep 5 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 26%, wind/gust 18 mph, thunder 10%<br>Arboles / southwest county: RH 23%, wind/gust 22 mph, thunder 6%<br>Chimney Rock / west county: RH 21%, wind/gust 21 mph, thunder 9% |
| Sun, Sep 6 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 28%, wind/gust 18 mph, thunder 29%<br>Arboles / southwest county: RH 24%, wind/gust 21 mph, thunder 36%<br>Chimney Rock / west county: RH 22%, wind/gust 20 mph, thunder 35% |
| Mon, Sep 7 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 34%, wind/gust 20 mph, thunder 51%<br>Arboles / southwest county: RH 28%, wind/gust 22 mph, thunder 38%<br>Chimney Rock / west county: RH 27%, wind/gust 21 mph, thunder 45% |
| Tue, Sep 8 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 33%, wind/gust 20 mph, thunder 46%<br>Arboles / southwest county: RH 28%, wind/gust 22 mph, thunder 36%<br>Chimney Rock / west county: RH 27%, wind/gust 20 mph, thunder 41% |

## Sample Point Status

- Pagosa Springs: COZ295 (matches), forecast zone COZ023, county zone COC007
- Arboles / southwest county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Chimney Rock / west county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Piedra / north county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Chromo / southeast county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Durango / La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Bayfield / east La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Ignacio / southeast La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
