# Archuleta Red Flag Risk Monitor

Generated: Jun 16, 2026 at 7:12 PM MDT (Pagosa Springs, CO local time)
Next update: Jun 16, 2026 at 8:12 PM MDT (Pagosa Springs, CO local time)
Date/time basis: Pagosa Springs, CO local time (America/Denver)
> **Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## At A Glance

- Overall tier: **HIGH**
- PSPS likelihood: **LIKELY**
- PSPS likely dates: Tue, Jun 16; Wed, Jun 17; Thu, Jun 18; Sat, Jun 20; Sun, Jun 21; Mon, Jun 22
- PSPS watch dates: Fri, Jun 19
- Monitor heads-up recommended: **YES** - Send this monitor report because current risk is HIGH. This is not an official LPEA or NWS notice.
- HIGH dates: Tue, Jun 16; Wed, Jun 17; Thu, Jun 18; Sat, Jun 20; Sun, Jun 21; Mon, Jun 22
- CONCERN dates: Fri, Jun 19
- ELEVATED dates: None
- Official NWS Red Flag / Fire Weather alerts (COZ295): 1
- LPEA signal: `active_keyword_match` - LPEA active/update sources contained power-interruption keywords; review source before treating as confirmed outage intent.
- LPEA source coverage: 13 sources; 5/5 official social sources reachable
- NWS discussion: NWS discussion contains fire-weather concern language.

## Decision Support

- Summary: Highest LPEA PSPS concern is Tue, Jun 16 near Pagosa Springs (LIKELY 100/100), driven by near-threshold wind/gust signal near 24 mph; very dry RH near 10%; 2 sampled hours are near red-flag thresholds.
- Confidence: **MEDIUM** (69/100) - 8/8 sampled weather points available; 7/7 fire-posture sources reachable; official NWS alert zones checked; 13/13 LPEA public sources reachable; LPEA active/update sources checked; forecast changed substantially versus prior run; no confirmed PSPS events logged yet for calibration
- Fire danger peak: Tue, Jun 16: Arboles / southwest county EXTREME 100/100
- Red Flag likelihood peak: Tue, Jun 16: Arboles / southwest county LIKELY 100/100
- LPEA PSPS peak: Tue, Jun 16: Pagosa Springs LIKELY 100/100
- Method: rules-based decision support using public weather, fire-posture, and LPEA source signals; scores are screening estimates, not official or statistically calibrated probabilities.

| Date | Fire danger | Red Flag likelihood | LPEA PSPS | Main window |
| --- | --- | --- | --- | --- |
| Tue, Jun 16 | Arboles / southwest county: EXTREME 100/100 | Arboles / southwest county: LIKELY 100/100 | Pagosa Springs: LIKELY 100/100 | 7 PM-8 PM local; 2 near/red-flag threshold hours. |
| Wed, Jun 17 | Arboles / southwest county: EXTREME 100/100 | Arboles / southwest county: LIKELY 100/100 | Pagosa Springs: LIKELY 100/100 | 1 PM-7 PM local; 7 near/red-flag threshold hours. |
| Thu, Jun 18 | Ignacio / southeast La Plata County: EXTREME 96/100 | Ignacio / southeast La Plata County: LIKELY 92/100 | Arboles / southwest county: LIKELY 100/100 | 1 PM-8 PM local; 8 near/red-flag threshold hours. |
| Fri, Jun 19 | Ignacio / southeast La Plata County: VERY HIGH 81/100 | Ignacio / southeast La Plata County: WATCH 65/100 | Arboles / southwest county: LIKELY 76/100 | 3 PM-6 PM local; 4 near/red-flag threshold hours. |
| Sat, Jun 20 | Chimney Rock / west county: EXTREME 100/100 | Chimney Rock / west county: LIKELY 100/100 | Pagosa Springs: LIKELY 100/100 | 1 PM-7 PM local; 7 near/red-flag threshold hours. |
| Sun, Jun 21 | Durango / La Plata County: EXTREME 100/100 | Durango / La Plata County: LIKELY 100/100 | Arboles / southwest county: LIKELY 100/100 | 1 PM-7 PM local; 7 near/red-flag threshold hours. |
| Mon, Jun 22 | Bayfield / east La Plata County: EXTREME 92/100 | Bayfield / east La Plata County: LIKELY 84/100 | Bayfield / east La Plata County: LIKELY 100/100 | 2 PM-7 PM local; 6 near/red-flag threshold hours. |

## Trend Intelligence

- Summary: Momentum is easing versus the prior run (Jun 16 at 5:33 AM MDT); forecast volatility is high and first WATCH-or-higher date is Tue, Jun 16.
- Momentum: **Easing**
- Forecast volatility: **HIGH** (35/100)
- First WATCH-or-higher PSPS date: Tue, Jun 16
- Watch-date movement: First WATCH-or-higher PSPS date remains Tue, Jun 16.
- Method: compares current forecast evidence against prior local forecast history.

Notable changes:
- First WATCH-or-higher PSPS date remains Tue, Jun 16.
- Tue, Jun 16: mixed vs prior run; PSPS LIKELY -> LIKELY; score +8, wind 0 mph, RH +1%, red-flag hours -6. Driver shifted to Bayfield / east La Plata County.
- Wed, Jun 17: worsening vs prior run; PSPS LIKELY -> LIKELY; score +15, wind +1 mph, RH +1%, red-flag hours +1. Driver shifted to Arboles / southwest county.
- Fri, Jun 19: easing vs prior run; PSPS WATCH -> WATCH; score -9, wind -1 mph, RH 0%, red-flag hours -2. Driver shifted to Arboles / southwest county.
- Mon, Jun 22: easing vs prior run; PSPS LIKELY -> LIKELY; score -4, wind -2 mph, RH -1%, red-flag hours -2. Driver shifted to Bayfield / east La Plata County.

## Public Analysis Export

- Summary: Highest LPEA PSPS concern is Tue, Jun 16 near Pagosa Springs (LIKELY 100/100), driven by near-threshold wind/gust signal near 24 mph; very dry RH near 10%; 2 sampled hours are near red-flag thresholds.
- Trend: Momentum is easing versus the prior run (Jun 16 at 5:33 AM MDT); forecast volatility is high and first WATCH-or-higher date is Tue, Jun 16.
- Confidence: **MEDIUM** (69/100)
- First WATCH-or-higher PSPS date: Tue, Jun 16
- PSPS peak: Tue, Jun 16 near Pagosa Springs at LIKELY 100/100
- Red Flag peak: Tue, Jun 16 near Arboles / southwest county at LIKELY 100/100
- Fire danger peak: Tue, Jun 16 near Arboles / southwest county at EXTREME 100/100
- LPEA operational outage context: No monitored active LPEA source currently describes a non-PSPS outage.
- Public JSON: `archuleta_red_flag_monitor/public_analysis_export.json`

What changed:
- First WATCH-or-higher PSPS date remains Tue, Jun 16.
- Tue, Jun 16: mixed vs prior run; PSPS LIKELY -> LIKELY; score +8, wind 0 mph, RH +1%, red-flag hours -6. Driver shifted to Bayfield / east La Plata County.
- Wed, Jun 17: worsening vs prior run; PSPS LIKELY -> LIKELY; score +15, wind +1 mph, RH +1%, red-flag hours +1. Driver shifted to Arboles / southwest county.
- Fri, Jun 19: easing vs prior run; PSPS WATCH -> WATCH; score -9, wind -1 mph, RH 0%, red-flag hours -2. Driver shifted to Arboles / southwest county.
- Mon, Jun 22: easing vs prior run; PSPS LIKELY -> LIKELY; score -4, wind -2 mph, RH -1%, red-flag hours -2. Driver shifted to Bayfield / east La Plata County.

What to watch next:
- Check whether the largest day-level changes line up with wind/RH movement or public-source context.
- Check whether the LPEA active match is still a broad red-flag banner rather than direct PSPS/outage intent.
- Watch whether the highest-risk locations remain consistent across runs or the driver area is moving.
- If a PSPS occurs, log the confirmed date, location, and source so future hit-rate scoring can improve.

## PSPS Likelihood

- **PSPS means Public Safety Power Shutoff:** a planned, safety-related power shutoff LPEA may use during dangerous fire-weather conditions to reduce wildfire ignition risk. See [LPEA PSPS guidance](https://lpea.coop/psps) and the [LPEA outage center](https://lpea.coop/outage-center); if power is out, also check the [LPEA outage map](https://outage.lpea.coop).
- Overall: **LIKELY** - PSPS likelihood is high on weather-driven red-flag days; prepare for possible LPEA safety-related interruption behavior.
- Likely PSPS watch dates: Tue, Jun 16; Wed, Jun 17; Thu, Jun 18; Sat, Jun 20; Sun, Jun 21; Mon, Jun 22
- PSPS watch dates: Fri, Jun 19
- LPEA signal basis: LPEA active/update source contains red-flag, wildfire, or power-interruption language.
- Note: This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

| Date | PSPS likelihood | Driver locations | Weather basis |
| --- | --- | --- | --- |
| Tue, Jun 16 | LIKELY | Bayfield / east La Plata County (LIKELY 92/100); Ignacio / southeast La Plata County (LIKELY 92/100); Arboles / southwest county (LIKELY 91/100); Chimney Rock / west county (LIKELY 85/100) | Top weather score 92/100 at Bayfield / east La Plata County. Weather score 92/100: RH 9%, wind/gust 36 mph, red-flag hours 3, near-threshold hours 4. |
| Wed, Jun 17 | LIKELY | Arboles / southwest county (LIKELY 99/100); Durango / La Plata County (LIKELY 96/100); Bayfield / east La Plata County (LIKELY 96/100); Ignacio / southeast La Plata County (LIKELY 96/100) | Top weather score 99/100 at Arboles / southwest county. Weather score 99/100: RH 8%, wind/gust 36 mph, red-flag hours 10, near-threshold hours 12. |
| Thu, Jun 18 | LIKELY | Arboles / southwest county (LIKELY 74/100); Durango / La Plata County (LIKELY 71/100); Bayfield / east La Plata County (LIKELY 71/100); Ignacio / southeast La Plata County (LIKELY 71/100) | Top weather score 74/100 at Arboles / southwest county. Weather score 74/100: RH 8%, wind/gust 26 mph, red-flag hours 4, near-threshold hours 8. |
| Fri, Jun 19 | WATCH | Arboles / southwest county (WATCH 52/100); Ignacio / southeast La Plata County (WATCH 52/100); Chimney Rock / west county (WATCH 48/100); Durango / La Plata County (WATCH 48/100) | Top weather score 52/100 at Arboles / southwest county. Weather score 52/100: RH 12%, wind/gust 23 mph, red-flag hours 0, near-threshold hours 4. |
| Sat, Jun 20 | LIKELY | Durango / La Plata County (LIKELY 80/100); Pagosa Springs (LIKELY 77/100); Bayfield / east La Plata County (LIKELY 77/100); Ignacio / southeast La Plata County (LIKELY 77/100) | Top weather score 80/100 at Durango / La Plata County. Weather score 80/100: RH 8%, wind/gust 34 mph, red-flag hours 8, near-threshold hours 10. |
| Sun, Jun 21 | LIKELY | Bayfield / east La Plata County (LIKELY 80/100); Ignacio / southeast La Plata County (LIKELY 80/100); Arboles / southwest county (LIKELY 74/100); Chimney Rock / west county (LIKELY 74/100) | Top weather score 80/100 at Bayfield / east La Plata County. Weather score 80/100: RH 8%, wind/gust 31 mph, red-flag hours 7, near-threshold hours 9. |
| Mon, Jun 22 | LIKELY | Bayfield / east La Plata County (LIKELY 70/100); Durango / La Plata County (WATCH 64/100); Pagosa Springs (WATCH 55/100); Arboles / southwest county (WATCH 55/100) | Top weather score 70/100 at Bayfield / east La Plata County. Weather score 70/100: RH 7%, wind/gust 25 mph, red-flag hours 3, near-threshold hours 6. |

## Area-Specific Outlook

| Area | Today | Peak this run | Highest-risk window |
| --- | --- | --- | --- |
| Arboles | LIKELY 91/100 | Wed, Jun 17: LIKELY 99/100 | 11 AM-10 PM local; 12 near/red-flag threshold hours. |
| Durango | LIKELY 85/100 | Wed, Jun 17: LIKELY 96/100 | 10 AM-10 PM local; 13 near/red-flag threshold hours. |
| Bayfield | LIKELY 92/100 | Wed, Jun 17: LIKELY 96/100 | 11 AM-10 PM local; 12 near/red-flag threshold hours. |
| Ignacio | LIKELY 92/100 | Wed, Jun 17: LIKELY 96/100 | 11 AM-10 PM local; 12 near/red-flag threshold hours. |
| Chimney Rock | LIKELY 85/100 | Wed, Jun 17: LIKELY 95/100 | 12 PM-10 PM local; 11 near/red-flag threshold hours. |
| Chromo | LIKELY 72/100 | Wed, Jun 17: LIKELY 86/100 | 12 PM-8 PM local; 9 near/red-flag threshold hours. |
| Pagosa Springs | WATCH 63/100 | Sat, Jun 20: LIKELY 77/100 | 1 PM-7 PM local; 7 near/red-flag threshold hours. |
| Piedra | WATCH 59/100 | Sat, Jun 20: LIKELY 73/100 | 2 PM-8 PM local; 7 near/red-flag threshold hours. |

## Fire Posture + Restrictions

- Summary: 5 official sources indicate fire restrictions or staged restrictions.
- Max restriction stage detected: STAGE 1
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
| Durango | UNKNOWN | UNKNOWN | [City of Durango](https://www.durangoco.gov/) |
| Southern Ute / Ignacio | STAGE 1 | UNKNOWN | [Southern Ute Indian Tribe](https://www.southernute-nsn.gov/) |

## Forecast Calibration

### PSPS Calibration

- Summary: No confirmed LPEA PSPS events logged yet; calibration will start once events are added.
- Confirmed PSPS events logged: 0
- Candidate/unconfirmed events logged: 0
- WATCH/LIKELY false-watch past days: 18
- Pending WATCH/LIKELY dates in current forecast: Tue, Jun 16; Wed, Jun 17; Thu, Jun 18; Fri, Jun 19; Sat, Jun 20; Sun, Jun 21; Mon, Jun 22
- Calibration source: manual PSPS event log plus forecast history from prior monitor runs.

### Red Flag / Fire Weather Calibration

- Summary: 8/8 official Red Flag / Fire Weather alert dates had a pre-alert HIGH monitor signal. Average lead time: 4.8 days.
- Official alert dates logged: 8
- Pre-alert HIGH hit rate: 100%
- Average lead time: 4.8 days
- HIGH false-watch past days: 9
- Pending HIGH dates in current forecast: Thu, Jun 18; Sat, Jun 20; Sun, Jun 21; Mon, Jun 22
- Calibration source: official NWS Red Flag / Fire Weather alert dates plus forecast history from prior monitor runs.

## Official Weather Alerts

- Monitored NWS zones: COC007, COC067, COZ019, COZ022, COZ023, COZ295
- [Red Flag Warning](https://api.weather.gov/alerts/urn:oid:2.49.0.1.840.0.928b6525570b12f407fe68bcfdc138e5a872eded.005.1): Red Flag Warning issued June 16 at 11:46AM MDT until June 17 at 9:00PM MDT by NWS Grand Junction CO; 2026-06-16T11:46:00-06:00 to 2026-06-17T21:00:00-06:00; zones COZ295

## LPEA Power Signal

- Status: `active_keyword_match` - LPEA active/update sources contained power-interruption keywords; review source before treating as confirmed outage intent.
- Meaning: Active source match means a monitored LPEA active/update source currently contains fire, outage, PSPS, or power-interruption keywords. Operational outages are shown separately and are not treated as PSPS/fire evidence unless the source text says so.
- Operational outage context: No monitored active LPEA source currently describes a non-PSPS outage.
- Source coverage: 13 sources; 5/5 official social sources reachable
- Evidence quality: 0 operational, 3 active/update, 2 archive/context, 4 reference source matches.
- Active/update source pages with matches: LPEA homepage (red flag, public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation); LPEA latest news (public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation, restoration); LPEA news releases (red flag, wildfire, public safety power shutoff, power shutoff, shutoff, power outage); LPEA LinkedIn (wildfire, public safety power shutoff, power shutoff, shutoff)
- Distinct active/update signals: LPEA homepage (red flag, public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation); LPEA news releases (red flag, wildfire, public safety power shutoff, power shutoff, shutoff, power outage); News-release archive PSPS item (red flag, wildfire, public safety power shutoff, power shutoff, shutoff, power outage); LPEA LinkedIn (wildfire, public safety power shutoff, power shutoff, shutoff); LinkedIn PSPS explainer post (wildfire, public safety power shutoff, power shutoff, shutoff)
- Example signal: ...ort LPEA Prioritizes Safety this Fire Season with Proactive Planning Learn More Red Flag Conditions May Result in Longer, More Frequent Outages Learn Why That's a Good Thing Previous Next Pay Bill Online MANA...
- Reference/context hits: [LPEA outage center](https://lpea.coop/outage-center); [LPEA wildfire / public safety power shutoffs](https://lpea.coop/psps); [LPEA red flag outage impact page](https://lpea.coop/outages/red-flag-warnings-and-impact-outages-prioritizing-safety-our-members); [LPEA fire mitigation](https://lpea.coop/fire-mitigation)

**Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## Next 7 Days

| Date | Tier | Main reason | Worst sampled metrics |
| --- | --- | --- | --- |
| Tue, Jun 16 | HIGH | Arboles / southwest county: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 10%, wind/gust 24 mph, thunder 0%<br>Arboles / southwest county: RH 8%, wind/gust 34 mph, thunder 0%<br>Chimney Rock / west county: RH 8%, wind/gust 30 mph, thunder 0% |
| Wed, Jun 17 | HIGH | Arboles / southwest county: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 11%, wind/gust 25 mph, thunder 2%<br>Arboles / southwest county: RH 8%, wind/gust 36 mph, thunder 0%<br>Chimney Rock / west county: RH 8%, wind/gust 31 mph, thunder 0% |
| Thu, Jun 18 | HIGH | Arboles / southwest county: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 11%, wind/gust 20 mph, thunder 3%<br>Arboles / southwest county: RH 8%, wind/gust 26 mph, thunder 1%<br>Chimney Rock / west county: RH 8%, wind/gust 22 mph, thunder 1% |
| Fri, Jun 19 | CONCERN | Pagosa Springs: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Pagosa Springs: RH 15%, wind/gust 21 mph, thunder 3%<br>Arboles / southwest county: RH 12%, wind/gust 23 mph, thunder 1%<br>Chimney Rock / west county: RH 11%, wind/gust 21 mph, thunder 1% |
| Sat, Jun 20 | HIGH | Pagosa Springs: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 11%, wind/gust 33 mph, thunder 0%<br>Arboles / southwest county: RH 9%, wind/gust 30 mph, thunder 0%<br>Chimney Rock / west county: RH 8%, wind/gust 30 mph, thunder 1% |
| Sun, Jun 21 | HIGH | Pagosa Springs: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 9%, wind/gust 28 mph, thunder 0%<br>Arboles / southwest county: RH 6%, wind/gust 29 mph, thunder 0%<br>Chimney Rock / west county: RH 6%, wind/gust 28 mph, thunder 0% |
| Mon, Jun 22 | HIGH | Bayfield / east La Plata County: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 8%, wind/gust 24 mph, thunder 1%<br>Arboles / southwest county: RH 6%, wind/gust 24 mph, thunder 0%<br>Chimney Rock / west county: RH 5%, wind/gust 24 mph, thunder 0% |

## Sample Point Status

- Pagosa Springs: COZ295 (matches), forecast zone COZ023, county zone COC007
- Arboles / southwest county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Chimney Rock / west county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Piedra / north county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Chromo / southeast county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Durango / La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Bayfield / east La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Ignacio / southeast La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
