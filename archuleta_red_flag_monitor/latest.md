# Archuleta Red Flag Risk Monitor

Generated: Jun 29, 2026 at 3:37 AM MDT (Pagosa Springs, CO local time)
Next update: Jun 29, 2026 at 4:37 AM MDT (Pagosa Springs, CO local time)
Date/time basis: Pagosa Springs, CO local time (America/Denver)
> **Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## At A Glance

- Overall tier: **HIGH**
- PSPS likelihood: **LIKELY**
- PSPS likely dates: Mon, Jun 29; Tue, Jun 30; Wed, Jul 1; Thu, Jul 2; Fri, Jul 3; Sat, Jul 4
- PSPS watch dates: Sun, Jul 5
- Monitor heads-up recommended: **YES** - Send this monitor report because current risk is HIGH. This is not an official LPEA or NWS notice.
- HIGH dates: Mon, Jun 29; Tue, Jun 30; Wed, Jul 1; Thu, Jul 2; Fri, Jul 3; Sat, Jul 4
- CONCERN dates: Sun, Jul 5
- ELEVATED dates: None
- Official NWS Red Flag / Fire Weather alerts (COZ295): 0
- LPEA signal: `active_keyword_match` - LPEA active/update sources contained power-interruption keywords; review source before treating as confirmed outage intent.
- LPEA source coverage: 13 sources; 5/5 official social sources reachable
- NWS discussion: NWS discussion contains fire-weather concern language.

## Decision Support

- Summary: Highest LPEA PSPS concern is Mon, Jun 29 near Pagosa Springs (LIKELY 100/100), driven by red-flag wind/gust signal near 29 mph; very dry RH near 12%; 5 sampled hours meet red-flag screen.
- Confidence: **MEDIUM** (74/100) - 8/8 sampled weather points available; 7/7 fire-posture sources reachable; official NWS alert zones checked; 13/13 LPEA public sources reachable; LPEA active/update sources checked; active LPEA operational outage context checked separately from PSPS scoring; forecast changed moderately versus prior run; no confirmed PSPS events logged yet for calibration
- Fire danger peak: Tue, Jun 30: Durango / La Plata County EXTREME 100/100
- Red Flag likelihood peak: Tue, Jun 30: Durango / La Plata County LIKELY 100/100
- LPEA PSPS peak: Mon, Jun 29: Pagosa Springs LIKELY 100/100
- Method: rules-based decision support using public weather, fire-posture, and LPEA source signals; scores are screening estimates, not official or statistically calibrated probabilities.

| Date | Fire danger | Red Flag likelihood | LPEA PSPS | Main window |
| --- | --- | --- | --- | --- |
| Mon, Jun 29 | Durango / La Plata County: EXTREME 100/100 | Durango / La Plata County: LIKELY 96/100 | Pagosa Springs: LIKELY 100/100 | 12 PM-7 PM local; 8 near/red-flag threshold hours. |
| Tue, Jun 30 | Durango / La Plata County: EXTREME 100/100 | Durango / La Plata County: LIKELY 100/100 | Arboles / southwest county: LIKELY 100/100 | 1 PM-8 PM local; 8 near/red-flag threshold hours. |
| Wed, Jul 1 | Pagosa Springs: EXTREME 100/100 | Pagosa Springs: LIKELY 92/100 | Pagosa Springs: LIKELY 100/100 | 12 PM-7 PM local; 8 near/red-flag threshold hours. |
| Thu, Jul 2 | Bayfield / east La Plata County: EXTREME 100/100 | Bayfield / east La Plata County: LIKELY 92/100 | Pagosa Springs: LIKELY 100/100 | 12 PM-6 PM local; 7 near/red-flag threshold hours. |
| Fri, Jul 3 | Pagosa Springs: EXTREME 100/100 | Pagosa Springs: LIKELY 92/100 | Pagosa Springs: LIKELY 100/100 | 11 AM-6 PM local; 8 near/red-flag threshold hours. |
| Sat, Jul 4 | Durango / La Plata County: EXTREME 95/100 | Durango / La Plata County: LIKELY 80/100 | Durango / La Plata County: LIKELY 97/100 | 1 PM-6 PM local; 6 near/red-flag threshold hours. |
| Sun, Jul 5 | Durango / La Plata County: EXTREME 85/100 | Durango / La Plata County: WATCH 62/100 | Durango / La Plata County: LIKELY 76/100 | 3 PM-6 PM local; 4 near/red-flag threshold hours. |

## Trend Intelligence

- Summary: Momentum is steady versus the prior run (Jun 28 at 3:44 PM MDT); forecast volatility is medium and first WATCH-or-higher date is Mon, Jun 29.
- Momentum: **Steady**
- Forecast volatility: **MEDIUM** (16/100)
- First WATCH-or-higher PSPS date: Mon, Jun 29
- Watch-date movement: First WATCH-or-higher PSPS date moved later from Sun, Jun 28 to Mon, Jun 29.
- Method: compares current forecast evidence against prior local forecast history.

Notable changes:
- First WATCH-or-higher PSPS date moved later from Sun, Jun 28 to Mon, Jun 29.
- Mon, Jun 29: easing vs prior run; PSPS LIKELY -> LIKELY; score -6, wind -6 mph, RH -1%, red-flag hours +1. Driver shifted to Pagosa Springs.
- Tue, Jun 30: worsening vs prior run; PSPS LIKELY -> LIKELY; score 0, wind 0 mph, RH 0%, red-flag hours +2.

## Public Analysis Export

- Summary: Highest LPEA PSPS concern is Mon, Jun 29 near Pagosa Springs (LIKELY 100/100), driven by red-flag wind/gust signal near 29 mph; very dry RH near 12%; 5 sampled hours meet red-flag screen.
- Trend: Momentum is steady versus the prior run (Jun 28 at 3:44 PM MDT); forecast volatility is medium and first WATCH-or-higher date is Mon, Jun 29.
- Confidence: **MEDIUM** (74/100)
- First WATCH-or-higher PSPS date: Mon, Jun 29
- PSPS peak: Mon, Jun 29 near Pagosa Springs at LIKELY 100/100
- Red Flag peak: Tue, Jun 30 near Durango / La Plata County at LIKELY 100/100
- Fire danger peak: Tue, Jun 30 near Durango / La Plata County at EXTREME 100/100
- LPEA operational outage context: LPEA service territory. Not classified as fire-weather or PSPS-related by this monitor.
- Public JSON: `archuleta_red_flag_monitor/public_analysis_export.json`

What changed:
- First WATCH-or-higher PSPS date moved later from Sun, Jun 28 to Mon, Jun 29.
- Mon, Jun 29: easing vs prior run; PSPS LIKELY -> LIKELY; score -6, wind -6 mph, RH -1%, red-flag hours +1. Driver shifted to Pagosa Springs.
- Tue, Jun 30: worsening vs prior run; PSPS LIKELY -> LIKELY; score 0, wind 0 mph, RH 0%, red-flag hours +2.

What to watch next:
- Check whether the largest day-level changes line up with wind/RH movement or public-source context.
- Check whether the LPEA active match is still a broad red-flag banner rather than direct PSPS/outage intent.
- Watch whether the highest-risk locations remain consistent across runs or the driver area is moving.
- If a PSPS occurs, log the confirmed date, location, and source so future hit-rate scoring can improve.

## PSPS Likelihood

- **PSPS means Public Safety Power Shutoff:** a planned, safety-related power shutoff LPEA may use during dangerous fire-weather conditions to reduce wildfire ignition risk. See [LPEA PSPS guidance](https://lpea.coop/psps) and the [LPEA outage center](https://lpea.coop/outage-center); if power is out, also check the [LPEA outage map](https://outage.lpea.coop).
- Overall: **LIKELY** - PSPS likelihood is high on weather-driven red-flag days; prepare for possible LPEA safety-related interruption behavior.
- Likely PSPS watch dates: Mon, Jun 29; Tue, Jun 30; Wed, Jul 1; Thu, Jul 2; Fri, Jul 3; Sat, Jul 4
- PSPS watch dates: Sun, Jul 5
- LPEA signal basis: LPEA active/update source contains red-flag, wildfire, or power-interruption language.
- Note: This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

| Date | PSPS likelihood | Driver locations | Weather basis |
| --- | --- | --- | --- |
| Mon, Jun 29 | LIKELY | Pagosa Springs (LIKELY 71/100); Durango / La Plata County (LIKELY 71/100); Bayfield / east La Plata County (LIKELY 71/100); Ignacio / southeast La Plata County (LIKELY 71/100) | Top weather score 71/100 at Pagosa Springs. Weather score 71/100: RH 12%, wind/gust 29 mph, red-flag hours 5, near-threshold hours 8. |
| Tue, Jun 30 | LIKELY | Durango / La Plata County (LIKELY 77/100); Bayfield / east La Plata County (LIKELY 77/100); Ignacio / southeast La Plata County (LIKELY 77/100); Arboles / southwest county (LIKELY 71/100) | Top weather score 77/100 at Durango / La Plata County. Weather score 77/100: RH 10%, wind/gust 32 mph, red-flag hours 7, near-threshold hours 9. |
| Wed, Jul 1 | LIKELY | Pagosa Springs (LIKELY 71/100); Durango / La Plata County (LIKELY 71/100); Bayfield / east La Plata County (LIKELY 71/100); Arboles / southwest county (LIKELY 70/100) | Top weather score 71/100 at Pagosa Springs. Weather score 71/100: RH 11%, wind/gust 28 mph, red-flag hours 6, near-threshold hours 8. |
| Thu, Jul 2 | LIKELY | Durango / La Plata County (LIKELY 74/100); Bayfield / east La Plata County (LIKELY 74/100); Ignacio / southeast La Plata County (LIKELY 74/100); Pagosa Springs (LIKELY 71/100) | Top weather score 74/100 at Durango / La Plata County. Weather score 74/100: RH 7%, wind/gust 26 mph, red-flag hours 4, near-threshold hours 7. |
| Fri, Jul 3 | LIKELY | Durango / La Plata County (LIKELY 74/100); Bayfield / east La Plata County (LIKELY 74/100); Ignacio / southeast La Plata County (LIKELY 74/100); Pagosa Springs (LIKELY 71/100) | Top weather score 74/100 at Durango / La Plata County. Weather score 74/100: RH 8%, wind/gust 26 mph, red-flag hours 5, near-threshold hours 7. |
| Sat, Jul 4 | LIKELY | Durango / La Plata County (LIKELY 67/100); Ignacio / southeast La Plata County (LIKELY 67/100); Arboles / southwest county (WATCH 55/100); Chimney Rock / west county (WATCH 55/100) | Top weather score 67/100 at Durango / La Plata County. Weather score 67/100: RH 9%, wind/gust 25 mph, red-flag hours 3, near-threshold hours 6. |
| Sun, Jul 5 | WATCH | Durango / La Plata County (WATCH 52/100); Chimney Rock / west county (WATCH 51/100); Bayfield / east La Plata County (WATCH 48/100); Ignacio / southeast La Plata County (WATCH 48/100) | Top weather score 52/100 at Durango / La Plata County. Weather score 52/100: RH 10%, wind/gust 22 mph, red-flag hours 0, near-threshold hours 4. |

## Area-Specific Outlook

| Area | Today | Peak this run | Highest-risk window |
| --- | --- | --- | --- |
| Durango | LIKELY 71/100 | Tue, Jun 30: LIKELY 77/100 | 12 PM-8 PM local; 9 near/red-flag threshold hours. |
| Bayfield | LIKELY 71/100 | Tue, Jun 30: LIKELY 77/100 | 12 PM-8 PM local; 9 near/red-flag threshold hours. |
| Ignacio | LIKELY 71/100 | Tue, Jun 30: LIKELY 77/100 | 12 PM-8 PM local; 9 near/red-flag threshold hours. |
| Pagosa Springs | LIKELY 71/100 | Mon, Jun 29: LIKELY 71/100 | 12 PM-7 PM local; 8 near/red-flag threshold hours. |
| Arboles | WATCH 52/100 | Tue, Jun 30: LIKELY 71/100 | 1 PM-8 PM local; 8 near/red-flag threshold hours. |
| Chimney Rock | WATCH 64/100 | Tue, Jun 30: LIKELY 71/100 | 1 PM-8 PM local; 8 near/red-flag threshold hours. |
| Piedra | WATCH 63/100 | Thu, Jul 2: LIKELY 67/100 | 12 PM-6 PM local; 7 near/red-flag threshold hours. |
| Chromo | WATCH 61/100 | Thu, Jul 2: WATCH 64/100 | 2 PM-6 PM local; 5 near/red-flag threshold hours. |

## Fire Posture + Restrictions

- Summary: 6 official sources indicate fire restrictions or staged restrictions.
- Max restriction stage detected: STAGE 2
- Max fire danger detected: EXTREME
- Sources reachable: 7/7
- Note: Official-source status check only; verify restrictions and burn decisions with the responsible jurisdiction.

| Jurisdiction | Restrictions | Fire danger | Source |
| --- | --- | --- | --- |
| Archuleta County | STAGE 1 | UNKNOWN | [Archuleta County Sheriff fire updates](https://sheriff.archuletacounty.gov/divisions/emergency-operations/fire-updates-and-information/) |
| Pagosa Springs | STAGE 1 | UNKNOWN | [Town of Pagosa Springs](https://www.pagosasprings.co.gov/) |
| San Juan National Forest | STAGE 1 | EXTREME | [San Juan National Forest fire](https://www.fs.usda.gov/r02/sanjuan/fire) |
| BLM Tres Rios | STAGE 1 | UNKNOWN | [BLM Tres Rios Field Office](https://www.blm.gov/office/tres-rios-field-office) |
| La Plata County / Durango Fire | NONE | UNKNOWN | [Durango Fire & Rescue fire conditions](https://www.durangofire.org/fire-conditions) |
| Durango | STAGE 2 | UNKNOWN | [City of Durango](https://www.durangoco.gov/) |
| Southern Ute / Ignacio | STAGE 2 | UNKNOWN | [Southern Ute Indian Tribe](https://www.southernute-nsn.gov/) |

## Forecast Calibration

### PSPS Calibration

- Summary: No confirmed LPEA PSPS events logged yet; calibration will start once events are added.
- Confirmed PSPS events logged: 0
- Candidate/unconfirmed events logged: 0
- WATCH/LIKELY false-watch past days: 31
- Pending WATCH/LIKELY dates in current forecast: Mon, Jun 29; Tue, Jun 30; Wed, Jul 1; Thu, Jul 2; Fri, Jul 3; Sat, Jul 4; Sun, Jul 5
- Calibration source: manual PSPS event log plus forecast history from prior monitor runs.

### Red Flag / Fire Weather Calibration

- Summary: 19/19 official Red Flag / Fire Weather alert dates had a pre-alert HIGH monitor signal. Average lead time: 4.9 days.
- Official alert dates logged: 19
- Pre-alert HIGH hit rate: 100%
- Average lead time: 4.9 days
- HIGH false-watch past days: 9
- Pending HIGH dates in current forecast: Mon, Jun 29; Tue, Jun 30; Wed, Jul 1; Thu, Jul 2; Fri, Jul 3; Sat, Jul 4
- Calibration source: official NWS Red Flag / Fire Weather alert dates plus forecast history from prior monitor runs.

## Official Weather Alerts

- Monitored NWS zones: COC007, COC067, COZ019, COZ022, COZ023, COZ295
- No active official NWS Red Flag / Fire Weather or related weather alerts found for monitored zones.

## LPEA Power Signal

- Status: `active_keyword_match` - LPEA active/update sources contained power-interruption keywords; review source before treating as confirmed outage intent.
- Meaning: Active source match means a monitored LPEA active/update source currently contains fire, outage, PSPS, or power-interruption keywords. Operational outages are shown separately and are not treated as PSPS/fire evidence unless the source text says so.
- Operational outage context: LPEA service territory. Not classified as fire-weather or PSPS-related by this monitor.
- Source coverage: 13 sources; 5/5 official social sources reachable
- Evidence quality: 0 operational, 3 active/update, 2 archive/context, 4 reference source matches.
- Operational outage source links: [LPEA homepage](https://lpea.coop); [LPEA latest news](https://lpea.coop/Posts); [LPEA news releases](https://lpea.coop/news-releases)
- Active/update source pages with matches: LPEA homepage (red flag, public safety power shutoff, power shutoff, shutoff, power outage, outage update); LPEA latest news (public safety power shutoff, power shutoff, shutoff, power outage, outage update, outage map); LPEA news releases (red flag, wildfire, public safety power shutoff, power shutoff, shutoff, power outage); LPEA LinkedIn (wildfire, public safety power shutoff, power shutoff, shutoff, fire mitigation)
- Distinct active/update signals: LPEA homepage (red flag, public safety power shutoff, power shutoff, shutoff, power outage, outage update); LPEA news releases (red flag, wildfire, public safety power shutoff, power shutoff, shutoff, power outage); News-release archive PSPS item (red flag, wildfire, public safety power shutoff, power shutoff, shutoff, power outage); LPEA LinkedIn (wildfire, public safety power shutoff, power shutoff, shutoff, fire mitigation); LinkedIn PSPS explainer post (wildfire, public safety power shutoff, power shutoff, shutoff, fire mitigation)
- Example signal: ...s Find outage updates on our Facebook pag e. View our outage map. Previous Next Red Flag Conditions May Result in Longer, More Frequent Outages Learn Why That's a Good Thing LPEA Announces 2026-27 Board Leade...
- Reference/context hits: [LPEA outage center](https://lpea.coop/outage-center); [LPEA wildfire / public safety power shutoffs](https://lpea.coop/psps); [LPEA red flag outage impact page](https://lpea.coop/outages/red-flag-warnings-and-impact-outages-prioritizing-safety-our-members); [LPEA fire mitigation](https://lpea.coop/fire-mitigation)

**Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## Next 7 Days

| Date | Tier | Main reason | Worst sampled metrics |
| --- | --- | --- | --- |
| Mon, Jun 29 | HIGH | Pagosa Springs: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 12%, wind/gust 29 mph, thunder 1%<br>Arboles / southwest county: RH 9%, wind/gust 23 mph, thunder 0%<br>Chimney Rock / west county: RH 8%, wind/gust 25 mph, thunder 1% |
| Tue, Jun 30 | HIGH | Pagosa Springs: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 13%, wind/gust 30 mph, thunder 4%<br>Arboles / southwest county: RH 10%, wind/gust 28 mph, thunder 3%<br>Chimney Rock / west county: RH 10%, wind/gust 28 mph, thunder 3% |
| Wed, Jul 1 | HIGH | Pagosa Springs: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 11%, wind/gust 28 mph, thunder 0%<br>Arboles / southwest county: RH 6%, wind/gust 26 mph, thunder 0%<br>Chimney Rock / west county: RH 6%, wind/gust 25 mph, thunder 0% |
| Thu, Jul 2 | HIGH | Pagosa Springs: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 9%, wind/gust 28 mph, thunder 0%<br>Arboles / southwest county: RH 5%, wind/gust 25 mph, thunder 0%<br>Chimney Rock / west county: RH 5%, wind/gust 25 mph, thunder 0% |
| Fri, Jul 3 | HIGH | Pagosa Springs: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 10%, wind/gust 26 mph, thunder 1%<br>Arboles / southwest county: RH 7%, wind/gust 23 mph, thunder 1%<br>Chimney Rock / west county: RH 6%, wind/gust 23 mph, thunder 1% |
| Sat, Jul 4 | HIGH | Durango / La Plata County: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 11%, wind/gust 23 mph, thunder 0%<br>Arboles / southwest county: RH 8%, wind/gust 23 mph, thunder 0%<br>Chimney Rock / west county: RH 7%, wind/gust 23 mph, thunder 0% |
| Sun, Jul 5 | CONCERN | Chimney Rock / west county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Pagosa Springs: RH 12%, wind/gust 18 mph, thunder 5%<br>Arboles / southwest county: RH 9%, wind/gust 21 mph, thunder 4%<br>Chimney Rock / west county: RH 8%, wind/gust 21 mph, thunder 4% |

## Sample Point Status

- Pagosa Springs: COZ295 (matches), forecast zone COZ023, county zone COC007
- Arboles / southwest county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Chimney Rock / west county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Piedra / north county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Chromo / southeast county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Durango / La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Bayfield / east La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Ignacio / southeast La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
