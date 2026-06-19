# Archuleta Red Flag Risk Monitor

Generated: Jun 19, 2026 at 3:21 PM MDT (Pagosa Springs, CO local time)
Next update: Jun 19, 2026 at 4:21 PM MDT (Pagosa Springs, CO local time)
Date/time basis: Pagosa Springs, CO local time (America/Denver)
> **Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## At A Glance

- Overall tier: **HIGH**
- PSPS likelihood: **LIKELY**
- PSPS likely dates: Fri, Jun 19; Sat, Jun 20; Sun, Jun 21; Mon, Jun 22; Tue, Jun 23; Wed, Jun 24; Thu, Jun 25
- PSPS watch dates: None
- Monitor heads-up recommended: **YES** - Send this monitor report because current risk is HIGH. This is not an official LPEA or NWS notice.
- HIGH dates: Fri, Jun 19; Sat, Jun 20; Sun, Jun 21; Mon, Jun 22; Tue, Jun 23; Wed, Jun 24; Thu, Jun 25
- CONCERN dates: None
- ELEVATED dates: None
- Official NWS Red Flag / Fire Weather alerts (COZ295): 1
- LPEA signal: `active_keyword_match` - LPEA active/update sources contained power-interruption keywords; review source before treating as confirmed outage intent.
- LPEA source coverage: 13 sources; 5/5 official social sources reachable
- NWS discussion: NWS discussion contains fire-weather concern language.

## Decision Support

- Summary: Highest LPEA PSPS concern is Fri, Jun 19 near Arboles / southwest county (LIKELY 100/100), driven by near-threshold wind/gust signal near 23 mph; very dry RH near 12%; 5 sampled hours are near red-flag thresholds.
- Confidence: **MEDIUM** (74/100) - 8/8 sampled weather points available; 7/7 fire-posture sources reachable; official NWS alert zones checked; 13/13 LPEA public sources reachable; LPEA active/update sources checked; forecast changed moderately versus prior run; no confirmed PSPS events logged yet for calibration
- Fire danger peak: Sat, Jun 20: Pagosa Springs EXTREME 100/100
- Red Flag likelihood peak: Sat, Jun 20: Pagosa Springs LIKELY 100/100
- LPEA PSPS peak: Fri, Jun 19: Arboles / southwest county LIKELY 100/100
- Method: rules-based decision support using public weather, fire-posture, and LPEA source signals; scores are screening estimates, not official or statistically calibrated probabilities.

| Date | Fire danger | Red Flag likelihood | LPEA PSPS | Main window |
| --- | --- | --- | --- | --- |
| Fri, Jun 19 | Arboles / southwest county: EXTREME 92/100 | Arboles / southwest county: LIKELY 85/100 | Arboles / southwest county: LIKELY 100/100 | 3 PM-7 PM local; 5 near/red-flag threshold hours. |
| Sat, Jun 20 | Pagosa Springs: EXTREME 100/100 | Pagosa Springs: LIKELY 100/100 | Pagosa Springs: LIKELY 100/100 | 12 PM-8 PM local; 9 near/red-flag threshold hours. |
| Sun, Jun 21 | Bayfield / east La Plata County: EXTREME 100/100 | Bayfield / east La Plata County: LIKELY 100/100 | Arboles / southwest county: LIKELY 100/100 | 1 PM-8 PM local; 8 near/red-flag threshold hours. |
| Mon, Jun 22 | Durango / La Plata County: EXTREME 96/100 | Durango / La Plata County: LIKELY 92/100 | Pagosa Springs: LIKELY 100/100 | 2 PM-6 PM local; 5 near/red-flag threshold hours. |
| Tue, Jun 23 | Durango / La Plata County: EXTREME 100/100 | Durango / La Plata County: LIKELY 100/100 | Pagosa Springs: LIKELY 100/100 | 2 PM-7 PM local; 6 near/red-flag threshold hours. |
| Wed, Jun 24 | Durango / La Plata County: EXTREME 100/100 | Durango / La Plata County: LIKELY 100/100 | Arboles / southwest county: LIKELY 100/100 | 1 PM-10 PM local; 10 near/red-flag threshold hours. |
| Thu, Jun 25 | Durango / La Plata County: EXTREME 100/100 | Durango / La Plata County: LIKELY 100/100 | Chimney Rock / west county: LIKELY 100/100 | 1 PM-7 PM local; 7 near/red-flag threshold hours. |

## Trend Intelligence

- Summary: Momentum is easing versus the prior run (Jun 19 at 3:21 AM MDT); forecast volatility is medium and first WATCH-or-higher date is Fri, Jun 19.
- Momentum: **Easing**
- Forecast volatility: **MEDIUM** (14/100)
- First WATCH-or-higher PSPS date: Fri, Jun 19
- Watch-date movement: First WATCH-or-higher PSPS date remains Fri, Jun 19.
- Method: compares current forecast evidence against prior local forecast history.

Notable changes:
- First WATCH-or-higher PSPS date remains Fri, Jun 19.
- Fri, Jun 19: easing vs prior run; PSPS LIKELY -> LIKELY; score -9, wind -1 mph, RH +1%, red-flag hours -2. Driver shifted to Arboles / southwest county.

## Public Analysis Export

- Summary: Highest LPEA PSPS concern is Fri, Jun 19 near Arboles / southwest county (LIKELY 100/100), driven by near-threshold wind/gust signal near 23 mph; very dry RH near 12%; 5 sampled hours are near red-flag thresholds.
- Trend: Momentum is easing versus the prior run (Jun 19 at 3:21 AM MDT); forecast volatility is medium and first WATCH-or-higher date is Fri, Jun 19.
- Confidence: **MEDIUM** (74/100)
- First WATCH-or-higher PSPS date: Fri, Jun 19
- PSPS peak: Fri, Jun 19 near Arboles / southwest county at LIKELY 100/100
- Red Flag peak: Sat, Jun 20 near Pagosa Springs at LIKELY 100/100
- Fire danger peak: Sat, Jun 20 near Pagosa Springs at EXTREME 100/100
- LPEA operational outage context: No monitored active LPEA source currently describes a non-PSPS outage.
- Public JSON: `archuleta_red_flag_monitor/public_analysis_export.json`

What changed:
- First WATCH-or-higher PSPS date remains Fri, Jun 19.
- Fri, Jun 19: easing vs prior run; PSPS LIKELY -> LIKELY; score -9, wind -1 mph, RH +1%, red-flag hours -2. Driver shifted to Arboles / southwest county.

What to watch next:
- Check whether the largest day-level changes line up with wind/RH movement or public-source context.
- Check whether the LPEA active match is still a broad red-flag banner rather than direct PSPS/outage intent.
- Watch whether the highest-risk locations remain consistent across runs or the driver area is moving.
- If a PSPS occurs, log the confirmed date, location, and source so future hit-rate scoring can improve.

## PSPS Likelihood

- **PSPS means Public Safety Power Shutoff:** a planned, safety-related power shutoff LPEA may use during dangerous fire-weather conditions to reduce wildfire ignition risk. See [LPEA PSPS guidance](https://lpea.coop/psps) and the [LPEA outage center](https://lpea.coop/outage-center); if power is out, also check the [LPEA outage map](https://outage.lpea.coop).
- Overall: **LIKELY** - PSPS likelihood is high on weather-driven red-flag days; prepare for possible LPEA safety-related interruption behavior.
- Likely PSPS watch dates: Fri, Jun 19; Sat, Jun 20; Sun, Jun 21; Mon, Jun 22; Tue, Jun 23; Wed, Jun 24; Thu, Jun 25
- PSPS watch dates: None
- LPEA signal basis: LPEA active/update source contains red-flag, wildfire, or power-interruption language.
- Note: This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

| Date | PSPS likelihood | Driver locations | Weather basis |
| --- | --- | --- | --- |
| Fri, Jun 19 | LIKELY | Arboles / southwest county (LIKELY 67/100); Chimney Rock / west county (LIKELY 67/100); Durango / La Plata County (LIKELY 67/100); Bayfield / east La Plata County (LIKELY 67/100) | Top weather score 67/100 at Arboles / southwest county. Weather score 67/100: RH 12%, wind/gust 23 mph, red-flag hours 0, near-threshold hours 5. |
| Sat, Jun 20 | LIKELY | Pagosa Springs (LIKELY 95/100); Durango / La Plata County (LIKELY 95/100); Bayfield / east La Plata County (LIKELY 95/100); Ignacio / southeast La Plata County (LIKELY 95/100) | Top weather score 95/100 at Pagosa Springs. Weather score 95/100: RH 8%, wind/gust 31 mph, red-flag hours 7, near-threshold hours 9. |
| Sun, Jun 21 | LIKELY | Bayfield / east La Plata County (LIKELY 80/100); Ignacio / southeast La Plata County (LIKELY 80/100); Arboles / southwest county (LIKELY 74/100); Durango / La Plata County (LIKELY 74/100) | Top weather score 80/100 at Bayfield / east La Plata County. Weather score 80/100: RH 8%, wind/gust 31 mph, red-flag hours 6, near-threshold hours 9. |
| Mon, Jun 22 | LIKELY | Arboles / southwest county (LIKELY 74/100); Durango / La Plata County (LIKELY 74/100); Bayfield / east La Plata County (LIKELY 74/100); Ignacio / southeast La Plata County (LIKELY 74/100) | Top weather score 74/100 at Arboles / southwest county. Weather score 74/100: RH 6%, wind/gust 28 mph, red-flag hours 4, near-threshold hours 6. |
| Tue, Jun 23 | LIKELY | Durango / La Plata County (LIKELY 80/100); Bayfield / east La Plata County (LIKELY 80/100); Ignacio / southeast La Plata County (LIKELY 80/100); Arboles / southwest county (LIKELY 74/100) | Top weather score 80/100 at Durango / La Plata County. Weather score 80/100: RH 7%, wind/gust 31 mph, red-flag hours 7, near-threshold hours 8. |
| Wed, Jun 24 | LIKELY | Durango / La Plata County (LIKELY 77/100); Bayfield / east La Plata County (LIKELY 77/100); Ignacio / southeast La Plata County (LIKELY 77/100); Chimney Rock / west county (LIKELY 74/100) | Top weather score 77/100 at Durango / La Plata County. Weather score 77/100: RH 10%, wind/gust 32 mph, red-flag hours 9, near-threshold hours 11. |
| Thu, Jun 25 | LIKELY | Durango / La Plata County (LIKELY 77/100); Bayfield / east La Plata County (LIKELY 77/100); Chimney Rock / west county (LIKELY 75/100); Ignacio / southeast La Plata County (LIKELY 73/100) | Top weather score 77/100 at Durango / La Plata County. Weather score 77/100: RH 13%, wind/gust 31 mph, red-flag hours 7, near-threshold hours 9. |

## Area-Specific Outlook

| Area | Today | Peak this run | Highest-risk window |
| --- | --- | --- | --- |
| Pagosa Springs | WATCH 49/100 | Sat, Jun 20: LIKELY 95/100 | 12 PM-8 PM local; 9 near/red-flag threshold hours. |
| Durango | LIKELY 67/100 | Sat, Jun 20: LIKELY 95/100 | 11 AM-8 PM local; 10 near/red-flag threshold hours. |
| Bayfield | LIKELY 67/100 | Sat, Jun 20: LIKELY 95/100 | 11 AM-8 PM local; 10 near/red-flag threshold hours. |
| Ignacio | LIKELY 67/100 | Sat, Jun 20: LIKELY 95/100 | 11 AM-8 PM local; 10 near/red-flag threshold hours. |
| Arboles | LIKELY 67/100 | Sat, Jun 20: LIKELY 89/100 | 12 PM-8 PM local; 9 near/red-flag threshold hours. |
| Chimney Rock | LIKELY 67/100 | Sat, Jun 20: LIKELY 89/100 | 12 PM-8 PM local; 9 near/red-flag threshold hours. |
| Piedra | ELEVATED 41/100 | Sat, Jun 20: LIKELY 86/100 | 1 PM-8 PM local; 8 near/red-flag threshold hours. |
| Chromo | ELEVATED 41/100 | Sat, Jun 20: LIKELY 86/100 | 12 PM-8 PM local; 9 near/red-flag threshold hours. |

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
- WATCH/LIKELY false-watch past days: 21
- Pending WATCH/LIKELY dates in current forecast: Fri, Jun 19; Sat, Jun 20; Sun, Jun 21; Mon, Jun 22; Tue, Jun 23; Wed, Jun 24; Thu, Jun 25
- Calibration source: manual PSPS event log plus forecast history from prior monitor runs.

### Red Flag / Fire Weather Calibration

- Summary: 11/11 official Red Flag / Fire Weather alert dates had a pre-alert HIGH monitor signal. Average lead time: 4.9 days.
- Official alert dates logged: 11
- Pre-alert HIGH hit rate: 100%
- Average lead time: 4.9 days
- HIGH false-watch past days: 9
- Pending HIGH dates in current forecast: Sun, Jun 21; Mon, Jun 22; Tue, Jun 23; Wed, Jun 24; Thu, Jun 25
- Calibration source: official NWS Red Flag / Fire Weather alert dates plus forecast history from prior monitor runs.

## Official Weather Alerts

- Monitored NWS zones: COC007, COC067, COZ019, COZ022, COZ023, COZ295
- [Red Flag Warning](https://api.weather.gov/alerts/urn:oid:2.49.0.1.840.0.1006c1965bc5a471b800c4ee987bc4456ef65841.003.2): Red Flag Warning issued June 19 at 11:41AM MDT until June 20 at 10:00PM MDT by NWS Grand Junction CO; 2026-06-19T11:41:00-06:00 to 2026-06-20T22:00:00-06:00; zones COZ295

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
| Fri, Jun 19 | HIGH | Active NWS Red Flag Warning or Fire Weather Watch touches this local date. | Pagosa Springs: RH 14%, wind/gust 21 mph, thunder 2%<br>Arboles / southwest county: RH 12%, wind/gust 23 mph, thunder 1%<br>Chimney Rock / west county: RH 11%, wind/gust 21 mph, thunder 1% |
| Sat, Jun 20 | HIGH | Pagosa Springs: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 8%, wind/gust 31 mph, thunder 0%<br>Arboles / southwest county: RH 7%, wind/gust 29 mph, thunder 1%<br>Chimney Rock / west county: RH 6%, wind/gust 29 mph, thunder 0% |
| Sun, Jun 21 | HIGH | Pagosa Springs: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 9%, wind/gust 26 mph, thunder 0%<br>Arboles / southwest county: RH 7%, wind/gust 29 mph, thunder 0%<br>Chimney Rock / west county: RH 6%, wind/gust 26 mph, thunder 0% |
| Mon, Jun 22 | HIGH | Pagosa Springs: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 8%, wind/gust 28 mph, thunder 0%<br>Arboles / southwest county: RH 6%, wind/gust 28 mph, thunder 0%<br>Chimney Rock / west county: RH 5%, wind/gust 26 mph, thunder 0% |
| Tue, Jun 23 | HIGH | Pagosa Springs: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 8%, wind/gust 29 mph, thunder 0%<br>Arboles / southwest county: RH 6%, wind/gust 30 mph, thunder 0%<br>Chimney Rock / west county: RH 5%, wind/gust 28 mph, thunder 0% |
| Wed, Jun 24 | HIGH | Pagosa Springs: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 12%, wind/gust 25 mph, thunder 4%<br>Arboles / southwest county: RH 9%, wind/gust 30 mph, thunder 3%<br>Chimney Rock / west county: RH 8%, wind/gust 26 mph, thunder 4% |
| Thu, Jun 25 | HIGH | Arboles / southwest county: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 16%, wind/gust 24 mph, thunder 20%<br>Arboles / southwest county: RH 13%, wind/gust 29 mph, thunder 13%<br>Chimney Rock / west county: RH 11%, wind/gust 26 mph, thunder 17% |

## Sample Point Status

- Pagosa Springs: COZ295 (matches), forecast zone COZ023, county zone COC007
- Arboles / southwest county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Chimney Rock / west county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Piedra / north county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Chromo / southeast county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Durango / La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Bayfield / east La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Ignacio / southeast La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
