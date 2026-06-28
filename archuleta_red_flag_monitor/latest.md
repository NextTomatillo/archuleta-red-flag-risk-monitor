# Archuleta Red Flag Risk Monitor

Generated: Jun 28, 2026 at 3:53 AM MDT (Pagosa Springs, CO local time)
Next update: Jun 28, 2026 at 4:53 AM MDT (Pagosa Springs, CO local time)
Date/time basis: Pagosa Springs, CO local time (America/Denver)
> **Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## At A Glance

- Overall tier: **HIGH**
- PSPS likelihood: **LIKELY**
- PSPS likely dates: Sun, Jun 28; Mon, Jun 29; Tue, Jun 30; Wed, Jul 1; Thu, Jul 2; Fri, Jul 3
- PSPS watch dates: Sat, Jul 4
- Monitor heads-up recommended: **YES** - Send this monitor report because current risk is HIGH. This is not an official LPEA or NWS notice.
- HIGH dates: Sun, Jun 28; Mon, Jun 29; Tue, Jun 30; Wed, Jul 1; Thu, Jul 2; Fri, Jul 3
- CONCERN dates: Sat, Jul 4
- ELEVATED dates: None
- Official NWS Red Flag / Fire Weather alerts (COZ295): 1
- LPEA signal: `active_keyword_match` - LPEA active/update sources contained power-interruption keywords; review source before treating as confirmed outage intent.
- LPEA source coverage: 13 sources; 5/5 official social sources reachable
- NWS discussion: NWS discussion contains fire-weather concern language.

## Decision Support

- Summary: Highest LPEA PSPS concern is Sun, Jun 28 near Pagosa Springs (LIKELY 100/100), driven by very strong wind/gust signal near 43 mph; red-flag RH near 14%; 7 sampled hours are near red-flag thresholds.
- Confidence: **MEDIUM** (74/100) - 8/8 sampled weather points available; 7/7 fire-posture sources reachable; official NWS alert zones checked; 13/13 LPEA public sources reachable; LPEA active/update sources checked; active LPEA operational outage context checked separately from PSPS scoring; forecast changed moderately versus prior run; no confirmed PSPS events logged yet for calibration
- Fire danger peak: Sun, Jun 28: Pagosa Springs EXTREME 100/100
- Red Flag likelihood peak: Sun, Jun 28: Pagosa Springs LIKELY 100/100
- LPEA PSPS peak: Sun, Jun 28: Pagosa Springs LIKELY 100/100
- Method: rules-based decision support using public weather, fire-posture, and LPEA source signals; scores are screening estimates, not official or statistically calibrated probabilities.

| Date | Fire danger | Red Flag likelihood | LPEA PSPS | Main window |
| --- | --- | --- | --- | --- |
| Sun, Jun 28 | Pagosa Springs: EXTREME 100/100 | Pagosa Springs: LIKELY 100/100 | Pagosa Springs: LIKELY 100/100 | 2 PM-8 PM local; 7 near/red-flag threshold hours. |
| Mon, Jun 29 | Arboles / southwest county: EXTREME 100/100 | Arboles / southwest county: LIKELY 100/100 | Pagosa Springs: LIKELY 100/100 | 1 PM-8 PM local; 8 near/red-flag threshold hours. |
| Tue, Jun 30 | Ignacio / southeast La Plata County: EXTREME 100/100 | Ignacio / southeast La Plata County: LIKELY 96/100 | Arboles / southwest county: LIKELY 100/100 | 11 AM-7 PM local; 9 near/red-flag threshold hours. |
| Wed, Jul 1 | Pagosa Springs: EXTREME 96/100 | Pagosa Springs: LIKELY 88/100 | Pagosa Springs: LIKELY 100/100 | 12 PM-6 PM local; 7 near/red-flag threshold hours. |
| Thu, Jul 2 | Pagosa Springs: EXTREME 100/100 | Pagosa Springs: LIKELY 96/100 | Pagosa Springs: LIKELY 100/100 | 11 AM-7 PM local; 9 near/red-flag threshold hours. |
| Fri, Jul 3 | Durango / La Plata County: EXTREME 100/100 | Durango / La Plata County: LIKELY 100/100 | Pagosa Springs: LIKELY 100/100 | 11 AM-8 PM local; 10 near/red-flag threshold hours. |
| Sat, Jul 4 | Ignacio / southeast La Plata County: EXTREME 90/100 | Ignacio / southeast La Plata County: LIKELY 78/100 | Ignacio / southeast La Plata County: LIKELY 94/100 | 2 PM-7 PM local; 6 near/red-flag threshold hours. |

## Trend Intelligence

- Summary: Momentum is rising versus the prior run (Jun 26 at 3:21 PM MDT); forecast volatility is medium and first WATCH-or-higher date is Sun, Jun 28.
- Momentum: **Rising**
- Forecast volatility: **MEDIUM** (25/100)
- First WATCH-or-higher PSPS date: Sun, Jun 28
- Watch-date movement: First WATCH-or-higher PSPS date moved later from Sat, Jun 27 to Sun, Jun 28.
- Method: compares current forecast evidence against prior local forecast history.

Notable changes:
- First WATCH-or-higher PSPS date moved later from Sat, Jun 27 to Sun, Jun 28.
- Sun, Jun 28: worsening vs prior run; PSPS LIKELY -> LIKELY; score +15, wind +4 mph, RH 0%, red-flag hours -1.
- Thu, Jul 2: worsening vs prior run; PSPS LIKELY -> LIKELY; score +3, wind +1 mph, RH -2%, red-flag hours +3. Driver shifted to Durango / La Plata County.

## Public Analysis Export

- Summary: Highest LPEA PSPS concern is Sun, Jun 28 near Pagosa Springs (LIKELY 100/100), driven by very strong wind/gust signal near 43 mph; red-flag RH near 14%; 7 sampled hours are near red-flag thresholds.
- Trend: Momentum is rising versus the prior run (Jun 26 at 3:21 PM MDT); forecast volatility is medium and first WATCH-or-higher date is Sun, Jun 28.
- Confidence: **MEDIUM** (74/100)
- First WATCH-or-higher PSPS date: Sun, Jun 28
- PSPS peak: Sun, Jun 28 near Pagosa Springs at LIKELY 100/100
- Red Flag peak: Sun, Jun 28 near Pagosa Springs at LIKELY 100/100
- Fire danger peak: Sun, Jun 28 near Pagosa Springs at EXTREME 100/100
- LPEA operational outage context: Pagosa Springs. Not classified as fire-weather or PSPS-related by this monitor.
- Public JSON: `archuleta_red_flag_monitor/public_analysis_export.json`

What changed:
- First WATCH-or-higher PSPS date moved later from Sat, Jun 27 to Sun, Jun 28.
- Sun, Jun 28: worsening vs prior run; PSPS LIKELY -> LIKELY; score +15, wind +4 mph, RH 0%, red-flag hours -1.
- Thu, Jul 2: worsening vs prior run; PSPS LIKELY -> LIKELY; score +3, wind +1 mph, RH -2%, red-flag hours +3. Driver shifted to Durango / La Plata County.

What to watch next:
- Check whether the largest day-level changes line up with wind/RH movement or public-source context.
- Check whether the LPEA active match is still a broad red-flag banner rather than direct PSPS/outage intent.
- Watch whether the highest-risk locations remain consistent across runs or the driver area is moving.
- If a PSPS occurs, log the confirmed date, location, and source so future hit-rate scoring can improve.

## PSPS Likelihood

- **PSPS means Public Safety Power Shutoff:** a planned, safety-related power shutoff LPEA may use during dangerous fire-weather conditions to reduce wildfire ignition risk. See [LPEA PSPS guidance](https://lpea.coop/psps) and the [LPEA outage center](https://lpea.coop/outage-center); if power is out, also check the [LPEA outage map](https://outage.lpea.coop).
- Overall: **LIKELY** - PSPS likelihood is high on weather-driven red-flag days; prepare for possible LPEA safety-related interruption behavior.
- Likely PSPS watch dates: Sun, Jun 28; Mon, Jun 29; Tue, Jun 30; Wed, Jul 1; Thu, Jul 2; Fri, Jul 3
- PSPS watch dates: Sat, Jul 4
- LPEA signal basis: LPEA active/update source contains red-flag, wildfire, or power-interruption language.
- Note: This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

| Date | PSPS likelihood | Driver locations | Weather basis |
| --- | --- | --- | --- |
| Sun, Jun 28 | LIKELY | Arboles / southwest county (LIKELY 96/100); Chimney Rock / west county (LIKELY 96/100); Durango / La Plata County (LIKELY 96/100); Ignacio / southeast La Plata County (LIKELY 96/100) | Top weather score 96/100 at Arboles / southwest county. Weather score 96/100: RH 12%, wind/gust 44 mph, red-flag hours 9, near-threshold hours 12. |
| Mon, Jun 29 | LIKELY | Arboles / southwest county (LIKELY 77/100); Bayfield / east La Plata County (LIKELY 77/100); Ignacio / southeast La Plata County (LIKELY 77/100); Pagosa Springs (LIKELY 73/100) | Top weather score 77/100 at Arboles / southwest county. Weather score 77/100: RH 11%, wind/gust 31 mph, red-flag hours 7, near-threshold hours 10. |
| Tue, Jun 30 | LIKELY | Chimney Rock / west county (LIKELY 74/100); Arboles / southwest county (LIKELY 71/100); Durango / La Plata County (LIKELY 71/100); Bayfield / east La Plata County (LIKELY 71/100) | Top weather score 74/100 at Chimney Rock / west county. Weather score 74/100: RH 8%, wind/gust 26 mph, red-flag hours 4, near-threshold hours 8. |
| Wed, Jul 1 | LIKELY | Pagosa Springs (LIKELY 71/100); Ignacio / southeast La Plata County (WATCH 64/100); Piedra / north county (WATCH 61/100); Durango / La Plata County (WATCH 61/100) | Top weather score 71/100 at Pagosa Springs. Weather score 71/100: RH 11%, wind/gust 26 mph, red-flag hours 5, near-threshold hours 7. |
| Thu, Jul 2 | LIKELY | Durango / La Plata County (LIKELY 74/100); Bayfield / east La Plata County (LIKELY 74/100); Ignacio / southeast La Plata County (LIKELY 74/100); Pagosa Springs (LIKELY 71/100) | Top weather score 74/100 at Durango / La Plata County. Weather score 74/100: RH 7%, wind/gust 26 mph, red-flag hours 5, near-threshold hours 7. |
| Fri, Jul 3 | LIKELY | Durango / La Plata County (LIKELY 74/100); Ignacio / southeast La Plata County (LIKELY 74/100); Pagosa Springs (LIKELY 71/100); Piedra / north county (LIKELY 71/100) | Top weather score 74/100 at Durango / La Plata County. Weather score 74/100: RH 8%, wind/gust 29 mph, red-flag hours 7, near-threshold hours 9. |
| Sat, Jul 4 | WATCH | Ignacio / southeast La Plata County (WATCH 64/100); Durango / La Plata County (WATCH 61/100); Bayfield / east La Plata County (WATCH 61/100); Arboles / southwest county (WATCH 55/100) | Top weather score 64/100 at Ignacio / southeast La Plata County. Weather score 64/100: RH 8%, wind/gust 25 mph, red-flag hours 1, near-threshold hours 6. |

## Area-Specific Outlook

| Area | Today | Peak this run | Highest-risk window |
| --- | --- | --- | --- |
| Arboles | LIKELY 96/100 | Sun, Jun 28: LIKELY 96/100 | 12 PM-11 PM local; 12 near/red-flag threshold hours. |
| Chimney Rock | LIKELY 96/100 | Sun, Jun 28: LIKELY 96/100 | 11 AM-11 PM local; 13 near/red-flag threshold hours. |
| Durango | LIKELY 96/100 | Sun, Jun 28: LIKELY 96/100 | 1 PM-10 PM local; 10 near/red-flag threshold hours. |
| Ignacio | LIKELY 96/100 | Sun, Jun 28: LIKELY 96/100 | 12 PM-10 PM local; 11 near/red-flag threshold hours. |
| Bayfield | LIKELY 92/100 | Sun, Jun 28: LIKELY 92/100 | 1 PM-10 PM local; 10 near/red-flag threshold hours. |
| Pagosa Springs | LIKELY 82/100 | Sun, Jun 28: LIKELY 82/100 | 2 PM-8 PM local; 7 near/red-flag threshold hours. |
| Piedra | LIKELY 82/100 | Sun, Jun 28: LIKELY 82/100 | 3 PM-10 PM local; 8 near/red-flag threshold hours. |
| Chromo | LIKELY 76/100 | Sun, Jun 28: LIKELY 76/100 | 3 PM-8 PM local; 6 near/red-flag threshold hours. |

## Fire Posture + Restrictions

- Summary: 6 official sources indicate fire restrictions or staged restrictions.
- Max restriction stage detected: STAGE 2
- Max fire danger detected: VERY HIGH
- Sources reachable: 7/7
- Note: Official-source status check only; verify restrictions and burn decisions with the responsible jurisdiction.

| Jurisdiction | Restrictions | Fire danger | Source |
| --- | --- | --- | --- |
| Archuleta County | STAGE 1 | UNKNOWN | [Archuleta County Sheriff fire updates](https://sheriff.archuletacounty.gov/divisions/emergency-operations/fire-updates-and-information/) |
| Pagosa Springs | STAGE 1 | UNKNOWN | [Town of Pagosa Springs](https://www.pagosasprings.co.gov/) |
| San Juan National Forest | STAGE 1 | VERY HIGH | [San Juan National Forest fire](https://www.fs.usda.gov/r02/sanjuan/fire) |
| BLM Tres Rios | STAGE 1 | UNKNOWN | [BLM Tres Rios Field Office](https://www.blm.gov/office/tres-rios-field-office) |
| La Plata County / Durango Fire | NONE | UNKNOWN | [Durango Fire & Rescue fire conditions](https://www.durangofire.org/fire-conditions) |
| Durango | STAGE 2 | UNKNOWN | [City of Durango](https://www.durangoco.gov/) |
| Southern Ute / Ignacio | STAGE 2 | UNKNOWN | [Southern Ute Indian Tribe](https://www.southernute-nsn.gov/) |

## Forecast Calibration

### PSPS Calibration

- Summary: No confirmed LPEA PSPS events logged yet; calibration will start once events are added.
- Confirmed PSPS events logged: 0
- Candidate/unconfirmed events logged: 0
- WATCH/LIKELY false-watch past days: 30
- Pending WATCH/LIKELY dates in current forecast: Sun, Jun 28; Mon, Jun 29; Tue, Jun 30; Wed, Jul 1; Thu, Jul 2; Fri, Jul 3; Sat, Jul 4
- Calibration source: manual PSPS event log plus forecast history from prior monitor runs.

### Red Flag / Fire Weather Calibration

- Summary: 19/19 official Red Flag / Fire Weather alert dates had a pre-alert HIGH monitor signal. Average lead time: 4.9 days.
- Official alert dates logged: 19
- Pre-alert HIGH hit rate: 100%
- Average lead time: 4.9 days
- HIGH false-watch past days: 9
- Pending HIGH dates in current forecast: Mon, Jun 29; Tue, Jun 30; Wed, Jul 1; Thu, Jul 2; Fri, Jul 3
- Calibration source: official NWS Red Flag / Fire Weather alert dates plus forecast history from prior monitor runs.

## Official Weather Alerts

- Monitored NWS zones: COC007, COC067, COZ019, COZ022, COZ023, COZ295
- [Red Flag Warning](https://api.weather.gov/alerts/urn:oid:2.49.0.1.840.0.30e67ac59e528032290bec40c47dc9910e45d4f6.004.1): Red Flag Warning issued June 28 at 2:43AM MDT until June 28 at 10:00PM MDT by NWS Grand Junction CO; 2026-06-28T02:43:00-06:00 to 2026-06-28T22:00:00-06:00; zones COZ295

## LPEA Power Signal

- Status: `active_keyword_match` - LPEA active/update sources contained power-interruption keywords; review source before treating as confirmed outage intent.
- Meaning: Active source match means a monitored LPEA active/update source currently contains fire, outage, PSPS, or power-interruption keywords. Operational outages are shown separately and are not treated as PSPS/fire evidence unless the source text says so.
- Operational outage context: Pagosa Springs. Not classified as fire-weather or PSPS-related by this monitor.
- Source coverage: 13 sources; 5/5 official social sources reachable
- Evidence quality: 0 operational, 3 active/update, 2 archive/context, 4 reference source matches.
- Operational outage source links: [LPEA homepage](https://lpea.coop); [LPEA latest news](https://lpea.coop/Posts); [LPEA news releases](https://lpea.coop/news-releases)
- Active/update source pages with matches: LPEA homepage (red flag, public safety power shutoff, power shutoff, shutoff, power outage, outage map); LPEA latest news (public safety power shutoff, power shutoff, shutoff, power outage, outage map, fire mitigation); LPEA news releases (red flag, wildfire, public safety power shutoff, power shutoff, shutoff, power outage); LPEA LinkedIn (wildfire, public safety power shutoff, power shutoff, shutoff, fire mitigation)
- Distinct active/update signals: LPEA homepage (red flag, public safety power shutoff, power shutoff, shutoff, power outage, outage map); LPEA news releases (red flag, wildfire, public safety power shutoff, power shutoff, shutoff, power outage); News-release archive PSPS item (red flag, wildfire, public safety power shutoff, power shutoff, shutoff, power outage); LPEA LinkedIn (wildfire, public safety power shutoff, power shutoff, shutoff, fire mitigation); LinkedIn PSPS explainer post (wildfire, public safety power shutoff, power shutoff, shutoff, fire mitigation)
- Example signal: ...Springs. Find updates on our Facebook pag e. View our outage map. Previous Next Red Flag Conditions May Result in Longer, More Frequent Outages Learn Why That's a Good Thing LPEA Announces 2026-27 Board Leade...
- Reference/context hits: [LPEA outage center](https://lpea.coop/outage-center); [LPEA wildfire / public safety power shutoffs](https://lpea.coop/psps); [LPEA red flag outage impact page](https://lpea.coop/outages/red-flag-warnings-and-impact-outages-prioritizing-safety-our-members); [LPEA fire mitigation](https://lpea.coop/fire-mitigation)

**Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## Next 7 Days

| Date | Tier | Main reason | Worst sampled metrics |
| --- | --- | --- | --- |
| Sun, Jun 28 | HIGH | Arboles / southwest county: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 14%, wind/gust 43 mph, thunder 3%<br>Arboles / southwest county: RH 12%, wind/gust 44 mph, thunder 2%<br>Chimney Rock / west county: RH 10%, wind/gust 41 mph, thunder 2% |
| Mon, Jun 29 | HIGH | Pagosa Springs: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 14%, wind/gust 31 mph, thunder 1%<br>Arboles / southwest county: RH 11%, wind/gust 31 mph, thunder 1%<br>Chimney Rock / west county: RH 9%, wind/gust 29 mph, thunder 1% |
| Tue, Jun 30 | HIGH | Pagosa Springs: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 13%, wind/gust 30 mph, thunder 1%<br>Arboles / southwest county: RH 9%, wind/gust 28 mph, thunder 1%<br>Chimney Rock / west county: RH 8%, wind/gust 26 mph, thunder 1% |
| Wed, Jul 1 | HIGH | Pagosa Springs: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 11%, wind/gust 26 mph, thunder 1%<br>Arboles / southwest county: RH 7%, wind/gust 23 mph, thunder 1%<br>Chimney Rock / west county: RH 7%, wind/gust 23 mph, thunder 1% |
| Thu, Jul 2 | HIGH | Pagosa Springs: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 9%, wind/gust 28 mph, thunder 0%<br>Arboles / southwest county: RH 6%, wind/gust 25 mph, thunder 0%<br>Chimney Rock / west county: RH 6%, wind/gust 24 mph, thunder 0% |
| Fri, Jul 3 | HIGH | Pagosa Springs: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 10%, wind/gust 29 mph, thunder 2%<br>Arboles / southwest county: RH 8%, wind/gust 24 mph, thunder 2%<br>Chimney Rock / west county: RH 7%, wind/gust 25 mph, thunder 2% |
| Sat, Jul 4 | CONCERN | Pagosa Springs: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Pagosa Springs: RH 11%, wind/gust 22 mph, thunder 2%<br>Arboles / southwest county: RH 8%, wind/gust 24 mph, thunder 2%<br>Chimney Rock / west county: RH 7%, wind/gust 23 mph, thunder 2% |

## Sample Point Status

- Pagosa Springs: COZ295 (matches), forecast zone COZ023, county zone COC007
- Arboles / southwest county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Chimney Rock / west county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Piedra / north county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Chromo / southeast county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Durango / La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Bayfield / east La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Ignacio / southeast La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
