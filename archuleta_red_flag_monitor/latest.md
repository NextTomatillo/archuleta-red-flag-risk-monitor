# Archuleta County fire-weather monitor

Generated: Sep 4, 2026 at 5:29 AM MDT (Pagosa Springs, CO local time)
Next update: Sep 4, 2026 at 5:20 PM MDT (Pagosa Springs, CO local time)
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
- ELEVATED dates: Mon, Sep 7
- Official NWS Red Flag / Fire Weather alerts (COZ295): 0
- LPEA signal: `active_keyword_match` - LPEA active/update sources contained power-interruption keywords; review source before treating as confirmed outage intent.
- LPEA source coverage: 13 sources; 5/5 official social sources reachable
- Current Archuleta County wildfires: 1
- Official evacuation notices: No current evacuation order or warning detected in the checked official county feeds.
- NWS discussion: No concerning fire-weather language found in latest GJT discussion.

## Decision Support

- Summary: Highest LPEA PSPS concern is Mon, Sep 7 near Bayfield / east La Plata County (ELEVATED 27/100), driven by red-flag wind/gust signal near 25 mph; Official fire-posture context for Bayfield / east La Plata County is elevated (STAGE 1; fire danger HIGH), used as a small supporting modifier. NIFC reports 1 current wildfire in Archuleta County.
- Confidence: **MEDIUM** (69/100) - 8/8 sampled weather points available; 7/7 fire-posture sources reachable; official NWS alert zones checked; 13/13 LPEA public sources reachable; LPEA active/update sources checked; authoritative NIFC current-incident feed checked for Archuleta County; official Archuleta County evacuation feeds checked; forecast changed substantially versus prior run; no confirmed PSPS events logged yet for calibration
- Weather fire-potential peak: Mon, Sep 7: Bayfield / east La Plata County MODERATE 35/100
- Red Flag likelihood peak: Mon, Sep 7: Bayfield / east La Plata County LOW 25/100
- LPEA PSPS peak: Mon, Sep 7: Bayfield / east La Plata County ELEVATED 27/100
- Method: rules-based decision support using public weather, fire-posture, and LPEA source signals; scores are screening estimates, not official or statistically calibrated probabilities.

| Date | Weather fire potential | Red Flag likelihood | LPEA PSPS | Main window |
| --- | --- | --- | --- | --- |
| Fri, Sep 4 | Pagosa Springs: LOW 14/100 | Pagosa Springs: LOW 0/100 | Pagosa Springs: LOW 10/100 | Peak ingredients near 3 PM local; RH 30%, wind 18 mph. |
| Sat, Sep 5 | Durango / La Plata County: LOW 26/100 | Arboles / southwest county: LOW 8/100 | Arboles / southwest county: ELEVATED 18/100 | Peak ingredients near 6 PM local; RH 24%, wind 22 mph. |
| Sun, Sep 6 | Chimney Rock / west county: LOW 34/100 | Arboles / southwest county: LOW 8/100 | Arboles / southwest county: ELEVATED 24/100 | Peak ingredients near 4 PM local; RH 22%, wind 21 mph. |
| Mon, Sep 7 | Bayfield / east La Plata County: MODERATE 35/100 | Bayfield / east La Plata County: LOW 25/100 | Bayfield / east La Plata County: ELEVATED 27/100 | Peak ingredients near 4 PM local; RH 36%, wind 25 mph. |
| Tue, Sep 8 | Durango / La Plata County: LOW 26/100 | Arboles / southwest county: LOW 8/100 | Arboles / southwest county: ELEVATED 18/100 | Peak ingredients near 4 PM local; RH 25%, wind 21 mph. |
| Wed, Sep 9 | Durango / La Plata County: LOW 26/100 | Arboles / southwest county: LOW 8/100 | Arboles / southwest county: ELEVATED 18/100 | Peak ingredients near 4 PM local; RH 26%, wind 21 mph. |
| Thu, Sep 10 | Durango / La Plata County: LOW 26/100 | Arboles / southwest county: LOW 8/100 | Arboles / southwest county: ELEVATED 18/100 | Peak ingredients near 4 PM local; RH 26%, wind 22 mph. |

## Analyst Interpretation

- Headline: Regional screening is ELEVATED for Sep 7 near Bayfield; no official COZ295 fire alert or active LPEA outage is listed.
- Summary: The Sep 7 regional peak near Bayfield / east La Plata County is MODERATE for fire potential (35/100), LOW for Red Flag likelihood (25/100), and ELEVATED for PSPS screening (27/100); no date reaches WATCH. Official COZ295 alerts and active LPEA outages are both zero, while LPEA keyword matches remain unconfirmed context rather than an outage or PSPS notice. NIFC lists the 1.5-acre Swiss Roll wildfire, with containment unreported, and checked county feeds show no current evacuation notice.
- Uncertainty: Scores are unofficial screening estimates, not calibrated PSPS probabilities; source updates can lag, and screening does not override restrictions or official safety instructions.
- Evidence used: overall_status, weather_peaks, official_alerts, forecast_change, lpea_context, fire_posture, active_incidents, calibration
- This interpretation cannot change the deterministic tiers, scores, official alerts, or notification decision.

Changing drivers:
- Sep 7 strengthened by 9 points and the regional driver shifted from Pagosa Springs to Bayfield / east La Plata County.
- Sep 4 eased from ELEVATED to LOW as wind decreased and relative humidity increased.
- Stage 1 restrictions and HIGH official fire danger remain supporting context, not an official warning.
- The LPEA keyword match is public-source context only; the official outage viewer lists no active outages.

What to watch next:
- Recheck Sep 7 wind and humidity as the regional forecast changes.
- Verify whether LPEA keyword matches become a direct outage or PSPS notice.
- Watch Swiss Roll acreage, containment, and county evacuation feeds for updates.
- Treat Bayfield context separately from Pagosa Springs local conditions.

## Trend Intelligence

- Summary: Momentum is rising versus the prior run (Sep 3 at 5:38 AM MDT); forecast volatility is high and first WATCH-or-higher date is not present.
- Momentum: **Rising**
- Forecast volatility: **HIGH** (41/100)
- First WATCH-or-higher PSPS date: None
- Watch-date movement: No WATCH-or-higher PSPS dates in current or prior run.
- Method: compares current forecast evidence against prior local forecast history.

Notable changes:
- No WATCH-or-higher PSPS dates in current or prior run.
- Fri, Sep 4: easing vs prior run; PSPS ELEVATED -> LOW; score -8, wind -2 mph, RH +2%, red-flag hours 0.
- Mon, Sep 7: worsening vs prior run; PSPS ELEVATED -> ELEVATED; score +9, wind +1 mph, RH -3%, red-flag hours 0. Driver shifted to Bayfield / east La Plata County.
- Sun, Sep 6: worsening vs prior run; PSPS ELEVATED -> ELEVATED; score +6, wind 0 mph, RH -5%, red-flag hours 0. Driver shifted to Arboles / southwest county.
- Wed, Sep 9: worsening vs prior run; PSPS ELEVATED -> ELEVATED; score 0, wind -1 mph, RH -6%, red-flag hours 0.

## Public Analysis Export

- Summary: Highest LPEA PSPS concern is Mon, Sep 7 near Bayfield / east La Plata County (ELEVATED 27/100), driven by red-flag wind/gust signal near 25 mph; Official fire-posture context for Bayfield / east La Plata County is elevated (STAGE 1; fire danger HIGH), used as a small supporting modifier. NIFC reports 1 current wildfire in Archuleta County.
- Trend: Momentum is rising versus the prior run (Sep 3 at 5:38 AM MDT); forecast volatility is high and first WATCH-or-higher date is not present.
- Confidence: **MEDIUM** (69/100)
- First WATCH-or-higher PSPS date: None
- PSPS peak: Mon, Sep 7 near Bayfield / east La Plata County at ELEVATED 27/100
- Red Flag peak: Mon, Sep 7 near Bayfield / east La Plata County at LOW 25/100
- Weather fire-potential peak: Mon, Sep 7 near Bayfield / east La Plata County at MODERATE 35/100
- LPEA operational outage context: No active outages are listed by the official LPEA outage viewer.
- Public JSON: `archuleta_red_flag_monitor/public_analysis_export.json`

What changed:
- No WATCH-or-higher PSPS dates in current or prior run.
- Fri, Sep 4: easing vs prior run; PSPS ELEVATED -> LOW; score -8, wind -2 mph, RH +2%, red-flag hours 0.
- Mon, Sep 7: worsening vs prior run; PSPS ELEVATED -> ELEVATED; score +9, wind +1 mph, RH -3%, red-flag hours 0. Driver shifted to Bayfield / east La Plata County.
- Sun, Sep 6: worsening vs prior run; PSPS ELEVATED -> ELEVATED; score +6, wind 0 mph, RH -5%, red-flag hours 0. Driver shifted to Arboles / southwest county.
- Wed, Sep 9: worsening vs prior run; PSPS ELEVATED -> ELEVATED; score 0, wind -1 mph, RH -6%, red-flag hours 0.

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
| Fri, Sep 4 | LOW | Pagosa Springs (LOW 10/100); Arboles / southwest county (LOW 10/100); Chimney Rock / west county (LOW 10/100) | Top weather score 8/100 at Pagosa Springs. Weather score 8/100: RH 30%, wind/gust 18 mph, red-flag hours 0, near-threshold hours 0. |
| Sat, Sep 5 | ELEVATED | Arboles / southwest county (ELEVATED 18/100); Durango / La Plata County (ELEVATED 18/100); Bayfield / east La Plata County (ELEVATED 18/100) | Top weather score 16/100 at Arboles / southwest county. Weather score 16/100: RH 24%, wind/gust 22 mph, red-flag hours 0, near-threshold hours 0. |
| Sun, Sep 6 | ELEVATED | Arboles / southwest county (ELEVATED 24/100); Chimney Rock / west county (ELEVATED 24/100); Pagosa Springs (ELEVATED 18/100) | Top weather score 22/100 at Arboles / southwest county. Weather score 22/100: RH 21%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 0. |
| Mon, Sep 7 | ELEVATED | Bayfield / east La Plata County (ELEVATED 27/100); Ignacio / southeast La Plata County (ELEVATED 25/100); Pagosa Springs (ELEVATED 18/100) | Top weather score 25/100 at Bayfield / east La Plata County. Weather score 25/100: RH 36%, wind/gust 25 mph, red-flag hours 0, near-threshold hours 0. |
| Tue, Sep 8 | ELEVATED | Arboles / southwest county (ELEVATED 18/100); Durango / La Plata County (ELEVATED 18/100); Bayfield / east La Plata County (ELEVATED 18/100) | Top weather score 16/100 at Arboles / southwest county. Weather score 16/100: RH 25%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 0. |
| Wed, Sep 9 | ELEVATED | Arboles / southwest county (ELEVATED 18/100); Durango / La Plata County (ELEVATED 18/100); Bayfield / east La Plata County (ELEVATED 18/100) | Top weather score 16/100 at Arboles / southwest county. Weather score 16/100: RH 25%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 0. |
| Thu, Sep 10 | ELEVATED | Arboles / southwest county (ELEVATED 18/100); Durango / La Plata County (ELEVATED 18/100); Bayfield / east La Plata County (ELEVATED 18/100) | Top weather score 16/100 at Arboles / southwest county. Weather score 16/100: RH 26%, wind/gust 22 mph, red-flag hours 0, near-threshold hours 0. |

## Area-Specific Outlook

| Area | Today | Peak this run | Highest-risk window |
| --- | --- | --- | --- |
| Bayfield | LOW 10/100 | Mon, Sep 7: ELEVATED 27/100 | Peak ingredients near 4 PM local; RH 36%, wind 25 mph. |
| Ignacio | LOW 8/100 | Mon, Sep 7: ELEVATED 25/100 | Peak ingredients near 4 PM local; RH 34%, wind 25 mph. |
| Arboles | LOW 10/100 | Sun, Sep 6: ELEVATED 24/100 | Peak ingredients near 4 PM local; RH 22%, wind 21 mph. |
| Chimney Rock | LOW 10/100 | Sun, Sep 6: ELEVATED 24/100 | Peak ingredients near 4 PM local; RH 19%, wind 21 mph. |
| Pagosa Springs | LOW 10/100 | Sun, Sep 6: ELEVATED 18/100 | Peak ingredients near 5 PM local; RH 26%, wind 21 mph. |
| Piedra | LOW 10/100 | Mon, Sep 7: ELEVATED 18/100 | Peak ingredients near 3 PM local; RH 42%, wind 21 mph. |
| Durango | LOW 10/100 | Sat, Sep 5: ELEVATED 18/100 | Peak ingredients near 3 PM local; RH 27%, wind 21 mph. |
| Chromo | LOW 10/100 | Fri, Sep 4: LOW 10/100 | Peak ingredients near 4 PM local; RH 32%, wind 16 mph. |

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
- WATCH/LIKELY false-watch past days: 73
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
- Source coverage: 13 sources; 5/5 official social sources reachable
- Evidence quality: 0 operational, 4 active/update, 0 archive/context, 6 reference source matches.
- Active/update source pages with matches: LPEA homepage (public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation, restoration); LPEA X (power outage, outage map, high winds, restore power); LPEA LinkedIn (wildfire, fire mitigation)
- Distinct active/update signals: LPEA X (power outage, outage map, high winds, restore power); LPEA X (power outage, outage map, high winds, restore power); LPEA LinkedIn (wildfire, fire mitigation); LPEA LinkedIn (wildfire, fire mitigation)
- Example signal: ...ibrary! 1 2 537 LPEA @LaPlataElectric May 7, 2024 LPEA members are experiencing power outages in the Bayfield and Pagosa Springs areas. Approximately 200 meters are out and it is suspected that the high winds are...
- Reference/context hits: [LPEA outage center](https://lpea.coop/outage-center); [LPEA wildfire / public safety power shutoffs](https://lpea.coop/psps); [LPEA red flag outage impact page](https://lpea.coop/outages/red-flag-warnings-and-impact-outages-prioritizing-safety-our-members); [LPEA fire mitigation](https://lpea.coop/fire-mitigation); [LPEA latest news](https://lpea.coop/Posts)

**Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## Next 7 Days

| Date | Tier | Main reason | Worst sampled metrics |
| --- | --- | --- | --- |
| Fri, Sep 4 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 30%, wind/gust 18 mph, thunder 28%<br>Arboles / southwest county: RH 27%, wind/gust 20 mph, thunder 20%<br>Chimney Rock / west county: RH 26%, wind/gust 18 mph, thunder 25% |
| Sat, Sep 5 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 26%, wind/gust 18 mph, thunder 8%<br>Arboles / southwest county: RH 24%, wind/gust 22 mph, thunder 5%<br>Chimney Rock / west county: RH 22%, wind/gust 20 mph, thunder 5% |
| Sun, Sep 6 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 23%, wind/gust 21 mph, thunder 28%<br>Arboles / southwest county: RH 21%, wind/gust 21 mph, thunder 27%<br>Chimney Rock / west county: RH 19%, wind/gust 21 mph, thunder 28% |
| Mon, Sep 7 | ELEVATED | Bayfield / east La Plata County: Elevated ingredient present: wind/gust forecast near 25 mph. | Bayfield / east La Plata County: RH 36%, wind/gust 25 mph, thunder 49%<br>Ignacio / southeast La Plata County: RH 34%, wind/gust 25 mph, thunder 41% |
| Tue, Sep 8 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 28%, wind/gust 20 mph, thunder 24%<br>Arboles / southwest county: RH 25%, wind/gust 21 mph, thunder 11%<br>Chimney Rock / west county: RH 24%, wind/gust 20 mph, thunder 15% |
| Wed, Sep 9 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 29%, wind/gust 17 mph, thunder 39%<br>Arboles / southwest county: RH 25%, wind/gust 21 mph, thunder 30%<br>Chimney Rock / west county: RH 24%, wind/gust 18 mph, thunder 34% |
| Thu, Sep 10 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 30%, wind/gust 17 mph, thunder 45%<br>Arboles / southwest county: RH 26%, wind/gust 22 mph, thunder 32%<br>Chimney Rock / west county: RH 25%, wind/gust 20 mph, thunder 40% |

## Sample Point Status

- Pagosa Springs: COZ295 (matches), forecast zone COZ023, county zone COC007
- Arboles / southwest county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Chimney Rock / west county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Piedra / north county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Chromo / southeast county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Durango / La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Bayfield / east La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Ignacio / southeast La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
