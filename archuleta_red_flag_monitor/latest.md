# Archuleta Red Flag Risk Monitor

Generated: Jun 3, 2026 at 5:39 AM MDT (Pagosa Springs, CO local time)
Next update: Jun 3, 2026 at 6:39 AM MDT (Pagosa Springs, CO local time)
Date/time basis: Pagosa Springs, CO local time (America/Denver)
> **Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## At A Glance

- Overall tier: **HIGH**
- PSPS likelihood: **LIKELY**
- PSPS likely dates: Sat, Jun 6; Sun, Jun 7; Mon, Jun 8; Tue, Jun 9
- PSPS watch dates: Thu, Jun 4
- Monitor heads-up recommended: **YES** - Send this monitor report because current risk is HIGH. This is not an official LPEA or NWS notice.
- HIGH dates: Sat, Jun 6; Sun, Jun 7; Mon, Jun 8; Tue, Jun 9
- CONCERN dates: Thu, Jun 4
- ELEVATED dates: Wed, Jun 3; Fri, Jun 5
- Official NWS Red Flag / Fire Weather alerts (COZ295): 0
- LPEA signal: `active_keyword_match` - LPEA active/update sources contained power-interruption keywords; review source before treating as confirmed outage intent.
- LPEA source coverage: 13 sources; 5/5 official social sources reachable
- NWS discussion: NWS discussion contains fire-weather concern language.

## Decision Support

- Summary: Highest LPEA PSPS concern is Sat, Jun 6 near Durango / La Plata County (LIKELY 100/100), driven by red-flag wind/gust signal near 29 mph; very dry RH near 11%; 5 sampled hours meet red-flag screen.
- Confidence: **MEDIUM** (69/100) - 8/8 sampled weather points available; 7/7 fire-posture sources reachable; official NWS alert zones checked; 13/13 LPEA public sources reachable; LPEA active/update sources checked; forecast changed substantially versus prior run; no confirmed PSPS events logged yet for calibration
- Fire danger peak: Sun, Jun 7: Durango / La Plata County EXTREME 100/100
- Red Flag likelihood peak: Sun, Jun 7: Durango / La Plata County LIKELY 100/100
- LPEA PSPS peak: Sat, Jun 6: Durango / La Plata County LIKELY 100/100
- Method: rules-based decision support using public weather, fire-posture, and LPEA source signals; scores are screening estimates, not official or statistically calibrated probabilities.

| Date | Fire danger | Red Flag likelihood | LPEA PSPS | Main window |
| --- | --- | --- | --- | --- |
| Wed, Jun 3 | Arboles / southwest county: HIGH 55/100 | Arboles / southwest county: LOW 25/100 | Arboles / southwest county: WATCH 46/100 | Peak ingredients near 5 PM local; RH 28%, wind 21 mph. |
| Thu, Jun 4 | Durango / La Plata County: VERY HIGH 76/100 | Durango / La Plata County: WATCH 63/100 | Durango / La Plata County: LIKELY 76/100 | 3 PM-6 PM local; 4 near/red-flag threshold hours. |
| Fri, Jun 5 | Pagosa Springs: MODERATE 46/100 | Arboles / southwest county: LOW 25/100 | Arboles / southwest county: WATCH 50/100 | Peak ingredients near 5 PM local; RH 11%, wind 18 mph. |
| Sat, Jun 6 | Durango / La Plata County: EXTREME 90/100 | Durango / La Plata County: LIKELY 88/100 | Durango / La Plata County: LIKELY 100/100 | 1 PM-7 PM local; 7 near/red-flag threshold hours. |
| Sun, Jun 7 | Durango / La Plata County: EXTREME 100/100 | Durango / La Plata County: LIKELY 100/100 | Arboles / southwest county: LIKELY 100/100 | 12 PM-7 PM local; 8 near/red-flag threshold hours. |
| Mon, Jun 8 | Durango / La Plata County: EXTREME 88/100 | Durango / La Plata County: LIKELY 84/100 | Durango / La Plata County: LIKELY 100/100 | 12 PM-7 PM local; 8 near/red-flag threshold hours. |
| Tue, Jun 9 | Durango / La Plata County: EXTREME 90/100 | Durango / La Plata County: LIKELY 88/100 | Arboles / southwest county: LIKELY 100/100 | 12 PM-7 PM local; 8 near/red-flag threshold hours. |

## Trend Intelligence

- Summary: Momentum is easing versus the prior run (Jun 2 at 5:22 AM MDT); forecast volatility is high and first WATCH-or-higher date is Thu, Jun 4.
- Momentum: **Easing**
- Forecast volatility: **HIGH** (39/100)
- First WATCH-or-higher PSPS date: Thu, Jun 4
- Watch-date movement: First WATCH-or-higher PSPS date moved later from Tue, Jun 2 to Thu, Jun 4.
- Method: compares current forecast evidence against prior local forecast history.

Notable changes:
- First WATCH-or-higher PSPS date moved later from Tue, Jun 2 to Thu, Jun 4.
- Fri, Jun 5: easing vs prior run; PSPS WATCH -> ELEVATED; score -22, wind -5 mph, RH -1%, red-flag hours 0. Driver shifted to Arboles / southwest county.

## Public Analysis Export

- Summary: Highest LPEA PSPS concern is Sat, Jun 6 near Durango / La Plata County (LIKELY 100/100), driven by red-flag wind/gust signal near 29 mph; very dry RH near 11%; 5 sampled hours meet red-flag screen.
- Trend: Momentum is easing versus the prior run (Jun 2 at 5:22 AM MDT); forecast volatility is high and first WATCH-or-higher date is Thu, Jun 4.
- Confidence: **MEDIUM** (69/100)
- First WATCH-or-higher PSPS date: Thu, Jun 4
- PSPS peak: Sat, Jun 6 near Durango / La Plata County at LIKELY 100/100
- Red Flag peak: Sun, Jun 7 near Durango / La Plata County at LIKELY 100/100
- Fire danger peak: Sun, Jun 7 near Durango / La Plata County at EXTREME 100/100
- Public JSON: `archuleta_red_flag_monitor/public_analysis_export.json`

What changed:
- First WATCH-or-higher PSPS date moved later from Tue, Jun 2 to Thu, Jun 4.
- Fri, Jun 5: easing vs prior run; PSPS WATCH -> ELEVATED; score -22, wind -5 mph, RH -1%, red-flag hours 0. Driver shifted to Arboles / southwest county.

What to watch next:
- Check whether the largest day-level changes line up with wind/RH movement or public-source context.
- Check whether the LPEA active match is still a broad red-flag banner rather than direct PSPS/outage intent.
- Watch whether the highest-risk locations remain consistent across runs or the driver area is moving.
- If a PSPS occurs, log the confirmed date, location, and source so future hit-rate scoring can improve.

## PSPS Likelihood

- **PSPS means Public Safety Power Shutoff:** a planned, safety-related power shutoff LPEA may use during dangerous fire-weather conditions to reduce wildfire ignition risk. See [LPEA PSPS guidance](https://lpea.coop/psps) and the [LPEA outage center](https://lpea.coop/outage-center); if power is out, also check the [LPEA outage map](https://outage.lpea.coop).
- Overall: **LIKELY** - PSPS likelihood is high on weather-driven red-flag days; prepare for possible LPEA safety-related interruption behavior.
- Likely PSPS watch dates: Sat, Jun 6; Sun, Jun 7; Mon, Jun 8; Tue, Jun 9
- PSPS watch dates: Thu, Jun 4
- LPEA signal basis: LPEA active/update source contains red-flag, wildfire, or power-interruption language.
- Note: This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

| Date | PSPS likelihood | Driver locations | Weather basis |
| --- | --- | --- | --- |
| Wed, Jun 3 | ELEVATED | Arboles / southwest county (ELEVATED 26/100); Durango / La Plata County (ELEVATED 26/100); Bayfield / east La Plata County (ELEVATED 26/100) | Top weather score 26/100 at Arboles / southwest county. Weather score 26/100: RH 20%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 0. |
| Thu, Jun 4 | WATCH | Durango / La Plata County (WATCH 52/100); Ignacio / southeast La Plata County (WATCH 48/100); Bayfield / east La Plata County (WATCH 46/100) | Top weather score 52/100 at Durango / La Plata County. Weather score 52/100: RH 14%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 4. |
| Fri, Jun 5 | ELEVATED | Arboles / southwest county (ELEVATED 30/100); Chimney Rock / west county (ELEVATED 30/100); Durango / La Plata County (ELEVATED 30/100) | Top weather score 30/100 at Arboles / southwest county. Weather score 30/100: RH 10%, wind/gust 18 mph, red-flag hours 0, near-threshold hours 0. |
| Sat, Jun 6 | LIKELY | Durango / La Plata County (LIKELY 71/100); Ignacio / southeast La Plata County (LIKELY 71/100); Arboles / southwest county (LIKELY 67/100); Bayfield / east La Plata County (LIKELY 67/100) | Top weather score 71/100 at Durango / La Plata County. Weather score 71/100: RH 11%, wind/gust 29 mph, red-flag hours 5, near-threshold hours 7. |
| Sun, Jun 7 | LIKELY | Durango / La Plata County (LIKELY 77/100); Bayfield / east La Plata County (LIKELY 77/100); Ignacio / southeast La Plata County (LIKELY 77/100); Arboles / southwest county (LIKELY 71/100) | Top weather score 77/100 at Durango / La Plata County. Weather score 77/100: RH 11%, wind/gust 31 mph, red-flag hours 7, near-threshold hours 8. |
| Mon, Jun 8 | LIKELY | Durango / La Plata County (LIKELY 71/100); Bayfield / east La Plata County (LIKELY 67/100); Pagosa Springs (WATCH 63/100); Ignacio / southeast La Plata County (WATCH 61/100) | Top weather score 71/100 at Durango / La Plata County. Weather score 71/100: RH 12%, wind/gust 26 mph, red-flag hours 4, near-threshold hours 8. |
| Tue, Jun 9 | LIKELY | Arboles / southwest county (LIKELY 71/100); Pagosa Springs (LIKELY 67/100); Durango / La Plata County (LIKELY 67/100); Bayfield / east La Plata County (LIKELY 67/100) | Top weather score 71/100 at Arboles / southwest county. Weather score 71/100: RH 12%, wind/gust 26 mph, red-flag hours 4, near-threshold hours 8. |

## Area-Specific Outlook

| Area | Today | Peak this run | Highest-risk window |
| --- | --- | --- | --- |
| Durango | ELEVATED 26/100 | Sun, Jun 7: LIKELY 77/100 | 12 PM-7 PM local; 8 near/red-flag threshold hours. |
| Bayfield | ELEVATED 26/100 | Sun, Jun 7: LIKELY 77/100 | 11 AM-7 PM local; 9 near/red-flag threshold hours. |
| Ignacio | ELEVATED 26/100 | Sun, Jun 7: LIKELY 77/100 | 11 AM-8 PM local; 10 near/red-flag threshold hours. |
| Arboles | ELEVATED 26/100 | Sun, Jun 7: LIKELY 71/100 | 12 PM-7 PM local; 8 near/red-flag threshold hours. |
| Chimney Rock | ELEVATED 18/100 | Sun, Jun 7: LIKELY 71/100 | 12 PM-7 PM local; 8 near/red-flag threshold hours. |
| Pagosa Springs | LOW 12/100 | Sun, Jun 7: LIKELY 67/100 | 1 PM-7 PM local; 7 near/red-flag threshold hours. |
| Chromo | LOW 12/100 | Sun, Jun 7: WATCH 63/100 | 1 PM-7 PM local; 7 near/red-flag threshold hours. |
| Piedra | LOW 12/100 | Sun, Jun 7: WATCH 51/100 | 1 PM-6 PM local; 6 near/red-flag threshold hours. |

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
- WATCH/LIKELY false-watch past days: 6
- Pending WATCH/LIKELY dates in current forecast: Thu, Jun 4; Sat, Jun 6; Sun, Jun 7; Mon, Jun 8; Tue, Jun 9
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
| Wed, Jun 3 | ELEVATED | Pagosa Springs: Elevated ingredient present: thunder probability reaches 32%. | Pagosa Springs: RH 23%, wind/gust 20 mph, thunder 32%<br>Arboles / southwest county: RH 20%, wind/gust 21 mph, thunder 24%<br>Chimney Rock / west county: RH 19%, wind/gust 20 mph, thunder 26% |
| Thu, Jun 4 | CONCERN | Durango / La Plata County: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Pagosa Springs: RH 20%, wind/gust 18 mph, thunder 26%<br>Arboles / southwest county: RH 15%, wind/gust 20 mph, thunder 5%<br>Chimney Rock / west county: RH 15%, wind/gust 20 mph, thunder 14% |
| Fri, Jun 5 | ELEVATED | Pagosa Springs: Elevated ingredient present: very low RH forecast near 14%. | Pagosa Springs: RH 14%, wind/gust 17 mph, thunder 7%<br>Arboles / southwest county: RH 10%, wind/gust 18 mph, thunder 1%<br>Chimney Rock / west county: RH 10%, wind/gust 16 mph, thunder 3% |
| Sat, Jun 6 | HIGH | Arboles / southwest county: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Arboles / southwest county: RH 12%, wind/gust 25 mph, thunder 5%<br>Chimney Rock / west county: RH 12%, wind/gust 23 mph, thunder 7%<br>Durango / La Plata County: RH 11%, wind/gust 29 mph, thunder 4% |
| Sun, Jun 7 | HIGH | Pagosa Springs: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 13%, wind/gust 29 mph, thunder 1%<br>Arboles / southwest county: RH 11%, wind/gust 28 mph, thunder 1%<br>Chimney Rock / west county: RH 9%, wind/gust 28 mph, thunder 1% |
| Mon, Jun 8 | HIGH | Pagosa Springs: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 13%, wind/gust 26 mph, thunder 4%<br>Arboles / southwest county: RH 11%, wind/gust 22 mph, thunder 5%<br>Chimney Rock / west county: RH 10%, wind/gust 24 mph, thunder 5% |
| Tue, Jun 9 | HIGH | Pagosa Springs: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 15%, wind/gust 28 mph, thunder 16%<br>Arboles / southwest county: RH 12%, wind/gust 26 mph, thunder 11%<br>Chimney Rock / west county: RH 11%, wind/gust 24 mph, thunder 14% |

## Sample Point Status

- Pagosa Springs: COZ295 (matches), forecast zone COZ023, county zone COC007
- Arboles / southwest county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Chimney Rock / west county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Piedra / north county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Chromo / southeast county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Durango / La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Bayfield / east La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Ignacio / southeast La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
