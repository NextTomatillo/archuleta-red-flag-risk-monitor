# Archuleta Red Flag Risk Monitor

Generated: Jun 2, 2026 at 5:22 AM MDT (Pagosa Springs, CO local time)
Next update: Jun 2, 2026 at 6:22 AM MDT (Pagosa Springs, CO local time)
Date/time basis: Pagosa Springs, CO local time (America/Denver)
> **Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## At A Glance

- Overall tier: **HIGH**
- PSPS likelihood: **LIKELY**
- PSPS likely dates: Sat, Jun 6; Sun, Jun 7; Mon, Jun 8
- PSPS watch dates: Tue, Jun 2; Thu, Jun 4; Fri, Jun 5
- Monitor heads-up recommended: **YES** - Send this monitor report because current risk is HIGH. This is not an official LPEA or NWS notice.
- HIGH dates: Sat, Jun 6; Sun, Jun 7; Mon, Jun 8
- CONCERN dates: Tue, Jun 2; Thu, Jun 4; Fri, Jun 5
- ELEVATED dates: Wed, Jun 3
- Official NWS Red Flag / Fire Weather alerts (COZ295): 0
- LPEA signal: `active_keyword_match` - LPEA active/update sources contained power-interruption keywords; review source before treating as confirmed outage intent.
- LPEA source coverage: 13 sources; 5/5 official social sources reachable
- NWS discussion: NWS discussion contains fire-weather concern language.

## Decision Support

- Summary: Highest LPEA PSPS concern is Sun, Jun 7 near Arboles / southwest county (LIKELY 100/100), driven by red-flag wind/gust signal near 26 mph; very dry RH near 11%; 5 sampled hours meet red-flag screen.
- Confidence: **MEDIUM** (74/100) - 8/8 sampled weather points available; 7/7 fire-posture sources reachable; official NWS alert zones checked; 13/13 LPEA public sources reachable; LPEA active/update sources checked; forecast changed moderately versus prior run; no confirmed PSPS events logged yet for calibration
- Fire danger peak: Sun, Jun 7: Ignacio / southeast La Plata County EXTREME 100/100
- Red Flag likelihood peak: Sun, Jun 7: Ignacio / southeast La Plata County LIKELY 100/100
- LPEA PSPS peak: Sun, Jun 7: Arboles / southwest county LIKELY 100/100
- Method: rules-based decision support using public weather, fire-posture, and LPEA source signals; scores are screening estimates, not official or statistically calibrated probabilities.

| Date | Fire danger | Red Flag likelihood | LPEA PSPS | Main window |
| --- | --- | --- | --- | --- |
| Tue, Jun 2 | Durango / La Plata County: VERY HIGH 78/100 | Durango / La Plata County: WATCH 68/100 | Durango / La Plata County: LIKELY 76/100 | 1 PM-6 PM local; 6 near/red-flag threshold hours. |
| Wed, Jun 3 | Durango / La Plata County: HIGH 55/100 | Durango / La Plata County: LOW 25/100 | Durango / La Plata County: WATCH 46/100 | Peak ingredients near 5 PM local; RH 21%, wind 21 mph. |
| Thu, Jun 4 | Durango / La Plata County: VERY HIGH 73/100 | Durango / La Plata County: WATCH 58/100 | Durango / La Plata County: LIKELY 72/100 | 3 PM-6 PM local; 4 near/red-flag threshold hours. |
| Fri, Jun 5 | Durango / La Plata County: VERY HIGH 75/100 | Durango / La Plata County: WATCH 62/100 | Durango / La Plata County: LIKELY 76/100 | 2 PM-5 PM local; 4 near/red-flag threshold hours. |
| Sat, Jun 6 | Durango / La Plata County: EXTREME 85/100 | Durango / La Plata County: LIKELY 80/100 | Durango / La Plata County: LIKELY 97/100 | 2 PM-7 PM local; 6 near/red-flag threshold hours. |
| Sun, Jun 7 | Ignacio / southeast La Plata County: EXTREME 100/100 | Ignacio / southeast La Plata County: LIKELY 100/100 | Arboles / southwest county: LIKELY 100/100 | 12 PM-6 PM local; 7 near/red-flag threshold hours. |
| Mon, Jun 8 | Durango / La Plata County: EXTREME 85/100 | Durango / La Plata County: LIKELY 80/100 | Durango / La Plata County: LIKELY 97/100 | 1 PM-7 PM local; 7 near/red-flag threshold hours. |

## Trend Intelligence

- Summary: Momentum is easing versus the prior run (Jun 1 at 6:27 PM MDT); forecast volatility is medium and first WATCH-or-higher date is Tue, Jun 2.
- Momentum: **Easing**
- Forecast volatility: **MEDIUM** (14/100)
- First WATCH-or-higher PSPS date: Tue, Jun 2
- Watch-date movement: First WATCH-or-higher PSPS date moved later from Mon, Jun 1 to Tue, Jun 2.
- Method: compares current forecast evidence against prior local forecast history.

Notable changes:
- First WATCH-or-higher PSPS date moved later from Mon, Jun 1 to Tue, Jun 2.
- Fri, Jun 5: easing vs prior run; PSPS WATCH -> WATCH; score -9, wind -1 mph, RH 0%, red-flag hours -2. Driver shifted to Durango / La Plata County.

## Public Analysis Export

- Summary: Highest LPEA PSPS concern is Sun, Jun 7 near Arboles / southwest county (LIKELY 100/100), driven by red-flag wind/gust signal near 26 mph; very dry RH near 11%; 5 sampled hours meet red-flag screen.
- Trend: Momentum is easing versus the prior run (Jun 1 at 6:27 PM MDT); forecast volatility is medium and first WATCH-or-higher date is Tue, Jun 2.
- Confidence: **MEDIUM** (74/100)
- First WATCH-or-higher PSPS date: Tue, Jun 2
- PSPS peak: Sun, Jun 7 near Arboles / southwest county at LIKELY 100/100
- Red Flag peak: Sun, Jun 7 near Ignacio / southeast La Plata County at LIKELY 100/100
- Fire danger peak: Sun, Jun 7 near Ignacio / southeast La Plata County at EXTREME 100/100
- Public JSON: `archuleta_red_flag_monitor/public_analysis_export.json`

What changed:
- First WATCH-or-higher PSPS date moved later from Mon, Jun 1 to Tue, Jun 2.
- Fri, Jun 5: easing vs prior run; PSPS WATCH -> WATCH; score -9, wind -1 mph, RH 0%, red-flag hours -2. Driver shifted to Durango / La Plata County.

What to watch next:
- Check whether the largest day-level changes line up with wind/RH movement or public-source context.
- Check whether the LPEA active match is still a broad red-flag banner rather than direct PSPS/outage intent.
- Watch whether the highest-risk locations remain consistent across runs or the driver area is moving.
- If a PSPS occurs, log the confirmed date, location, and source so future hit-rate scoring can improve.

## PSPS Likelihood

- **PSPS means Public Safety Power Shutoff:** a planned, safety-related power shutoff LPEA may use during dangerous fire-weather conditions to reduce wildfire ignition risk. See [LPEA PSPS guidance](https://lpea.coop/psps) and the [LPEA outage center](https://lpea.coop/outage-center); if power is out, also check the [LPEA outage map](https://outage.lpea.coop).
- Overall: **LIKELY** - PSPS likelihood is high on weather-driven red-flag days; prepare for possible LPEA safety-related interruption behavior.
- Likely PSPS watch dates: Sat, Jun 6; Sun, Jun 7; Mon, Jun 8
- PSPS watch dates: Tue, Jun 2; Thu, Jun 4; Fri, Jun 5
- LPEA signal basis: LPEA active/update source contains red-flag, wildfire, or power-interruption language.
- Note: This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

| Date | PSPS likelihood | Driver locations | Weather basis |
| --- | --- | --- | --- |
| Tue, Jun 2 | WATCH | Durango / La Plata County (WATCH 52/100); Bayfield / east La Plata County (WATCH 52/100); Ignacio / southeast La Plata County (WATCH 52/100); Pagosa Springs (WATCH 48/100) | Top weather score 52/100 at Durango / La Plata County. Weather score 52/100: RH 10%, wind/gust 23 mph, red-flag hours 0, near-threshold hours 6. |
| Wed, Jun 3 | ELEVATED | Durango / La Plata County (ELEVATED 26/100); Bayfield / east La Plata County (ELEVATED 26/100); Ignacio / southeast La Plata County (ELEVATED 26/100) | Top weather score 26/100 at Durango / La Plata County. Weather score 26/100: RH 19%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 0. |
| Thu, Jun 4 | WATCH | Durango / La Plata County (WATCH 48/100); Ignacio / southeast La Plata County (WATCH 48/100) | Top weather score 48/100 at Durango / La Plata County. Weather score 48/100: RH 14%, wind/gust 24 mph, red-flag hours 0, near-threshold hours 4. |
| Fri, Jun 5 | WATCH | Durango / La Plata County (WATCH 52/100); Bayfield / east La Plata County (WATCH 52/100); Ignacio / southeast La Plata County (WATCH 52/100); Arboles / southwest county (WATCH 48/100) | Top weather score 52/100 at Durango / La Plata County. Weather score 52/100: RH 11%, wind/gust 23 mph, red-flag hours 0, near-threshold hours 4. |
| Sat, Jun 6 | LIKELY | Durango / La Plata County (LIKELY 67/100); Ignacio / southeast La Plata County (LIKELY 67/100); Bayfield / east La Plata County (WATCH 57/100); Arboles / southwest county (WATCH 48/100) | Top weather score 67/100 at Durango / La Plata County. Weather score 67/100: RH 13%, wind/gust 28 mph, red-flag hours 4, near-threshold hours 6. |
| Sun, Jun 7 | LIKELY | Ignacio / southeast La Plata County (LIKELY 77/100); Arboles / southwest county (LIKELY 71/100); Chimney Rock / west county (LIKELY 71/100); Durango / La Plata County (LIKELY 71/100) | Top weather score 77/100 at Ignacio / southeast La Plata County. Weather score 77/100: RH 11%, wind/gust 31 mph, red-flag hours 7, near-threshold hours 9. |
| Mon, Jun 8 | LIKELY | Durango / La Plata County (LIKELY 67/100); Pagosa Springs (WATCH 52/100); Chimney Rock / west county (WATCH 52/100); Bayfield / east La Plata County (WATCH 52/100) | Top weather score 67/100 at Durango / La Plata County. Weather score 67/100: RH 10%, wind/gust 25 mph, red-flag hours 3, near-threshold hours 7. |

## Area-Specific Outlook

| Area | Today | Peak this run | Highest-risk window |
| --- | --- | --- | --- |
| Ignacio | WATCH 52/100 | Sun, Jun 7: LIKELY 77/100 | 11 AM-7 PM local; 9 near/red-flag threshold hours. |
| Arboles | ELEVATED 38/100 | Sun, Jun 7: LIKELY 71/100 | 12 PM-6 PM local; 7 near/red-flag threshold hours. |
| Chimney Rock | ELEVATED 38/100 | Sun, Jun 7: LIKELY 71/100 | 12 PM-7 PM local; 8 near/red-flag threshold hours. |
| Durango | WATCH 52/100 | Sun, Jun 7: LIKELY 71/100 | 11 AM-7 PM local; 9 near/red-flag threshold hours. |
| Bayfield | WATCH 52/100 | Sun, Jun 7: LIKELY 71/100 | 11 AM-7 PM local; 9 near/red-flag threshold hours. |
| Pagosa Springs | WATCH 48/100 | Sun, Jun 7: LIKELY 67/100 | 1 PM-7 PM local; 7 near/red-flag threshold hours. |
| Piedra | ELEVATED 44/100 | Sun, Jun 7: WATCH 51/100 | 2 PM-6 PM local; 5 near/red-flag threshold hours. |
| Chromo | ELEVATED 34/100 | Sun, Jun 7: WATCH 48/100 | 1 PM-7 PM local; 7 near/red-flag threshold hours. |

## Fire Posture + Restrictions

- Summary: 2 official sources indicate fire restrictions or staged restrictions.
- Max restriction stage detected: STAGE 1
- Max fire danger detected: VERY HIGH
- Sources reachable: 7/7
- Note: Official-source status check only; verify restrictions and burn decisions with the responsible jurisdiction.

| Jurisdiction | Restrictions | Fire danger | Source |
| --- | --- | --- | --- |
| Archuleta County | UNKNOWN | UNKNOWN | [Archuleta County Sheriff fire updates](https://sheriff.archuletacounty.gov/divisions/emergency-operations/fire-updates-and-information/) |
| Pagosa Springs | UNKNOWN | UNKNOWN | [Town of Pagosa Springs](https://www.pagosasprings.co.gov/) |
| San Juan National Forest | STAGE 1 | VERY HIGH | [San Juan National Forest fire](https://www.fs.usda.gov/r02/sanjuan/fire) |
| BLM Tres Rios | STAGE 1 | UNKNOWN | [BLM Tres Rios Field Office](https://www.blm.gov/office/tres-rios-field-office) |
| La Plata County / Durango Fire | NONE | UNKNOWN | [Durango Fire & Rescue fire conditions](https://www.durangofire.org/fire-conditions) |
| Durango | UNKNOWN | UNKNOWN | [City of Durango](https://www.durangoco.gov/) |
| Southern Ute / Ignacio | UNKNOWN | UNKNOWN | [Southern Ute Indian Tribe](https://www.southernute-nsn.gov/) |

## Forecast Calibration

- Summary: No confirmed LPEA PSPS events logged yet; calibration will start once events are added.
- Confirmed PSPS events logged: 0
- Candidate/unconfirmed events logged: 0
- WATCH/LIKELY false-watch past days: 5
- Pending WATCH/LIKELY dates in current forecast: Tue, Jun 2; Thu, Jun 4; Fri, Jun 5; Sat, Jun 6; Sun, Jun 7; Mon, Jun 8
- Calibration source: manual PSPS event log plus forecast history from prior monitor runs.

## Official Weather Alerts

- Monitored NWS zones: COC007, COC067, COZ019, COZ022, COZ023, COZ295
- No active official NWS Red Flag / Fire Weather or related weather alerts found for monitored zones.

## LPEA Power Signal

- Status: `active_keyword_match` - LPEA active/update sources contained power-interruption keywords; review source before treating as confirmed outage intent.
- Meaning: Active source match means a monitored LPEA active/update source currently contains fire, outage, PSPS, or power-interruption keywords. It is a watch cue for review, not a confirmed outage or shutoff notice.
- Source coverage: 13 sources; 5/5 official social sources reachable
- Evidence quality: 0 operational, 2 active/update, 2 archive/context, 4 reference source matches.
- Active/update source pages with matches: LPEA homepage (public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation, restoration); LPEA latest news (public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation, restoration); LPEA news releases (red flag, wildfire, public safety power shutoff, power shutoff, shutoff, power outage); LPEA LinkedIn (wildfire, public safety power shutoff, power shutoff, shutoff)
- Distinct active/update signals: LPEA news releases (red flag, wildfire, public safety power shutoff, power shutoff, shutoff, power outage); News-release archive PSPS item (red flag, wildfire, public safety power shutoff, power shutoff, shutoff, power outage); LinkedIn wildfire preparedness post (wildfire, public safety power shutoff, power shutoff, shutoff); LinkedIn PSPS explainer post (wildfire, public safety power shutoff, power shutoff, shutoff)
- Example signal: ...Board Election Season 04/17/2025 LPEA Implements Proactive Fire Measures Due to Red Flag Warning 04/14/2025 PSA: La Plata Electric Association – 2025 Board Election Voting Information 04/10/2025 LPEA Awards $...
- Reference/context hits: [LPEA outage center](https://lpea.coop/outage-center); [LPEA wildfire / public safety power shutoffs](https://lpea.coop/psps); [LPEA red flag outage impact page](https://lpea.coop/outages/red-flag-warnings-and-impact-outages-prioritizing-safety-our-members); [LPEA fire mitigation](https://lpea.coop/fire-mitigation)

**Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## Next 7 Days

| Date | Tier | Main reason | Worst sampled metrics |
| --- | --- | --- | --- |
| Tue, Jun 2 | CONCERN | Pagosa Springs: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Pagosa Springs: RH 12%, wind/gust 21 mph, thunder 11%<br>Arboles / southwest county: RH 10%, wind/gust 21 mph, thunder 7%<br>Chimney Rock / west county: RH 9%, wind/gust 21 mph, thunder 9% |
| Wed, Jun 3 | ELEVATED | Pagosa Springs: Elevated ingredient present: thunder probability reaches 38%. | Pagosa Springs: RH 22%, wind/gust 16 mph, thunder 38%<br>Arboles / southwest county: RH 18%, wind/gust 20 mph, thunder 31%<br>Chimney Rock / west county: RH 17%, wind/gust 18 mph, thunder 34% |
| Thu, Jun 4 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Pagosa Springs: RH 19%, wind/gust 18 mph, thunder 27%<br>Arboles / southwest county: RH 14%, wind/gust 22 mph, thunder 8%<br>Chimney Rock / west county: RH 14%, wind/gust 20 mph, thunder 15% |
| Fri, Jun 5 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Pagosa Springs: RH 15%, wind/gust 17 mph, thunder 10%<br>Arboles / southwest county: RH 11%, wind/gust 22 mph, thunder 4%<br>Chimney Rock / west county: RH 11%, wind/gust 20 mph, thunder 6% |
| Sat, Jun 6 | HIGH | Durango / La Plata County: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 19%, wind/gust 18 mph, thunder 20%<br>Arboles / southwest county: RH 13%, wind/gust 23 mph, thunder 7%<br>Chimney Rock / west county: RH 13%, wind/gust 21 mph, thunder 12% |
| Sun, Jun 7 | HIGH | Pagosa Springs: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 13%, wind/gust 28 mph, thunder 3%<br>Arboles / southwest county: RH 11%, wind/gust 26 mph, thunder 1%<br>Chimney Rock / west county: RH 10%, wind/gust 26 mph, thunder 2% |
| Mon, Jun 8 | HIGH | Durango / La Plata County: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 12%, wind/gust 23 mph, thunder 6%<br>Arboles / southwest county: RH 10%, wind/gust 21 mph, thunder 5%<br>Chimney Rock / west county: RH 9%, wind/gust 22 mph, thunder 7% |

## Sample Point Status

- Pagosa Springs: COZ295 (matches), forecast zone COZ023, county zone COC007
- Arboles / southwest county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Chimney Rock / west county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Piedra / north county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Chromo / southeast county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Durango / La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Bayfield / east La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Ignacio / southeast La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
