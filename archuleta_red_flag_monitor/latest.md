# Archuleta Red Flag Risk Monitor

Generated: Jun 12, 2026 at 5:21 AM MDT (Pagosa Springs, CO local time)
Next update: Jun 12, 2026 at 6:21 AM MDT (Pagosa Springs, CO local time)
Date/time basis: Pagosa Springs, CO local time (America/Denver)
> **Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## At A Glance

- Overall tier: **HIGH**
- PSPS likelihood: **LIKELY**
- PSPS likely dates: Fri, Jun 12; Mon, Jun 15; Tue, Jun 16; Wed, Jun 17; Thu, Jun 18
- PSPS watch dates: Sat, Jun 13; Sun, Jun 14
- Monitor heads-up recommended: **YES** - Send this monitor report because current risk is HIGH. This is not an official LPEA or NWS notice.
- HIGH dates: Fri, Jun 12; Mon, Jun 15; Tue, Jun 16; Wed, Jun 17; Thu, Jun 18
- CONCERN dates: Sat, Jun 13
- ELEVATED dates: Sun, Jun 14
- Official NWS Red Flag / Fire Weather alerts (COZ295): 1
- LPEA signal: `active_keyword_match` - LPEA active/update sources contained power-interruption keywords; review source before treating as confirmed outage intent.
- LPEA source coverage: 13 sources; 5/5 official social sources reachable
- NWS discussion: NWS discussion contains fire-weather concern language.

## Decision Support

- Summary: Highest LPEA PSPS concern is Fri, Jun 12 near Pagosa Springs (LIKELY 100/100), driven by red-flag wind/gust signal near 29 mph; very dry RH near 12%; 5 sampled hours meet red-flag screen.
- Confidence: **MEDIUM** (68/100) - 8/8 sampled weather points available; 6/7 fire-posture sources reachable; official NWS alert zones checked; 13/13 LPEA public sources reachable; LPEA active/update sources checked; forecast changed substantially versus prior run; no confirmed PSPS events logged yet for calibration
- Fire danger peak: Fri, Jun 12: Pagosa Springs EXTREME 100/100
- Red Flag likelihood peak: Fri, Jun 12: Pagosa Springs LIKELY 100/100
- LPEA PSPS peak: Fri, Jun 12: Pagosa Springs LIKELY 100/100
- Method: rules-based decision support using public weather, fire-posture, and LPEA source signals; scores are screening estimates, not official or statistically calibrated probabilities.

| Date | Fire danger | Red Flag likelihood | LPEA PSPS | Main window |
| --- | --- | --- | --- | --- |
| Fri, Jun 12 | Pagosa Springs: EXTREME 100/100 | Pagosa Springs: LIKELY 100/100 | Pagosa Springs: LIKELY 100/100 | 1 PM-7 PM local; 7 near/red-flag threshold hours. |
| Sat, Jun 13 | Ignacio / southeast La Plata County: VERY HIGH 81/100 | Ignacio / southeast La Plata County: WATCH 65/100 | Bayfield / east La Plata County: LIKELY 76/100 | 3 PM-6 PM local; 4 near/red-flag threshold hours. |
| Sun, Jun 14 | Arboles / southwest county: HIGH 59/100 | Ignacio / southeast La Plata County: LOW 25/100 | Ignacio / southeast La Plata County: WATCH 55/100 | Peak ingredients near 4 PM local; RH 20%, wind 25 mph. |
| Mon, Jun 15 | Durango / La Plata County: EXTREME 100/100 | Durango / La Plata County: LIKELY 96/100 | Arboles / southwest county: LIKELY 100/100 | 1 PM-9 PM local; 9 near/red-flag threshold hours. |
| Tue, Jun 16 | Arboles / southwest county: EXTREME 100/100 | Arboles / southwest county: LIKELY 100/100 | Pagosa Springs: LIKELY 100/100 | 1 PM-8 PM local; 8 near/red-flag threshold hours. |
| Wed, Jun 17 | Pagosa Springs: EXTREME 100/100 | Pagosa Springs: LIKELY 100/100 | Pagosa Springs: LIKELY 100/100 | 12 PM-9 PM local; 10 near/red-flag threshold hours. |
| Thu, Jun 18 | Arboles / southwest county: EXTREME 100/100 | Arboles / southwest county: LIKELY 100/100 | Arboles / southwest county: LIKELY 100/100 | 12 PM-8 PM local; 9 near/red-flag threshold hours. |

## Trend Intelligence

- Summary: Momentum is easing versus the prior run (Jun 11 at 5:31 PM MDT); forecast volatility is high and first WATCH-or-higher date is Fri, Jun 12.
- Momentum: **Easing**
- Forecast volatility: **HIGH** (46/100)
- First WATCH-or-higher PSPS date: Fri, Jun 12
- Watch-date movement: First WATCH-or-higher PSPS date moved later from Thu, Jun 11 to Fri, Jun 12.
- Method: compares current forecast evidence against prior local forecast history.

Notable changes:
- First WATCH-or-higher PSPS date moved later from Thu, Jun 11 to Fri, Jun 12.
- Sat, Jun 13: easing vs prior run; PSPS LIKELY -> WATCH; score -19, wind -5 mph, RH +1%, red-flag hours -4. Driver shifted to Bayfield / east La Plata County.
- Sun, Jun 14: easing vs prior run; PSPS WATCH -> ELEVATED; score -16, wind -2 mph, RH +1%, red-flag hours 0. Driver shifted to Ignacio / southeast La Plata County.
- Mon, Jun 15: easing vs prior run; PSPS LIKELY -> LIKELY; score 0, wind -3 mph, RH 0%, red-flag hours -2.

## Public Analysis Export

- Summary: Highest LPEA PSPS concern is Fri, Jun 12 near Pagosa Springs (LIKELY 100/100), driven by red-flag wind/gust signal near 29 mph; very dry RH near 12%; 5 sampled hours meet red-flag screen.
- Trend: Momentum is easing versus the prior run (Jun 11 at 5:31 PM MDT); forecast volatility is high and first WATCH-or-higher date is Fri, Jun 12.
- Confidence: **MEDIUM** (68/100)
- First WATCH-or-higher PSPS date: Fri, Jun 12
- PSPS peak: Fri, Jun 12 near Pagosa Springs at LIKELY 100/100
- Red Flag peak: Fri, Jun 12 near Pagosa Springs at LIKELY 100/100
- Fire danger peak: Fri, Jun 12 near Pagosa Springs at EXTREME 100/100
- LPEA operational outage context: No monitored active LPEA source currently describes a non-PSPS outage.
- Public JSON: `archuleta_red_flag_monitor/public_analysis_export.json`

What changed:
- First WATCH-or-higher PSPS date moved later from Thu, Jun 11 to Fri, Jun 12.
- Sat, Jun 13: easing vs prior run; PSPS LIKELY -> WATCH; score -19, wind -5 mph, RH +1%, red-flag hours -4. Driver shifted to Bayfield / east La Plata County.
- Sun, Jun 14: easing vs prior run; PSPS WATCH -> ELEVATED; score -16, wind -2 mph, RH +1%, red-flag hours 0. Driver shifted to Ignacio / southeast La Plata County.
- Mon, Jun 15: easing vs prior run; PSPS LIKELY -> LIKELY; score 0, wind -3 mph, RH 0%, red-flag hours -2.

What to watch next:
- Check whether the largest day-level changes line up with wind/RH movement or public-source context.
- Check whether the LPEA active match is still a broad red-flag banner rather than direct PSPS/outage intent.
- Watch whether the highest-risk locations remain consistent across runs or the driver area is moving.
- If a PSPS occurs, log the confirmed date, location, and source so future hit-rate scoring can improve.

## PSPS Likelihood

- **PSPS means Public Safety Power Shutoff:** a planned, safety-related power shutoff LPEA may use during dangerous fire-weather conditions to reduce wildfire ignition risk. See [LPEA PSPS guidance](https://lpea.coop/psps) and the [LPEA outage center](https://lpea.coop/outage-center); if power is out, also check the [LPEA outage map](https://outage.lpea.coop).
- Overall: **LIKELY** - PSPS likelihood is high on weather-driven red-flag days; prepare for possible LPEA safety-related interruption behavior.
- Likely PSPS watch dates: Fri, Jun 12; Mon, Jun 15; Tue, Jun 16; Wed, Jun 17; Thu, Jun 18
- PSPS watch dates: Sat, Jun 13; Sun, Jun 14
- LPEA signal basis: LPEA active/update source contains red-flag, wildfire, or power-interruption language.
- Note: This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

| Date | PSPS likelihood | Driver locations | Weather basis |
| --- | --- | --- | --- |
| Fri, Jun 12 | LIKELY | Bayfield / east La Plata County (LIKELY 92/100); Ignacio / southeast La Plata County (LIKELY 92/100); Pagosa Springs (LIKELY 86/100); Arboles / southwest county (LIKELY 86/100) | Top weather score 92/100 at Bayfield / east La Plata County. Weather score 92/100: RH 9%, wind/gust 31 mph, red-flag hours 5, near-threshold hours 7. |
| Sat, Jun 13 | WATCH | Bayfield / east La Plata County (WATCH 52/100); Ignacio / southeast La Plata County (WATCH 52/100); Arboles / southwest county (WATCH 48/100); Durango / La Plata County (WATCH 48/100) | Top weather score 52/100 at Bayfield / east La Plata County. Weather score 52/100: RH 12%, wind/gust 22 mph, red-flag hours 0, near-threshold hours 4. |
| Sun, Jun 14 | WATCH | Ignacio / southeast La Plata County (ELEVATED 35/100); Arboles / southwest county (ELEVATED 26/100); Durango / La Plata County (ELEVATED 26/100) | Top weather score 35/100 at Ignacio / southeast La Plata County. Weather score 35/100: RH 20%, wind/gust 25 mph, red-flag hours 0, near-threshold hours 0. |
| Mon, Jun 15 | LIKELY | Durango / La Plata County (LIKELY 77/100); Ignacio / southeast La Plata County (LIKELY 77/100); Arboles / southwest county (LIKELY 71/100); Bayfield / east La Plata County (LIKELY 71/100) | Top weather score 77/100 at Durango / La Plata County. Weather score 77/100: RH 10%, wind/gust 31 mph, red-flag hours 6, near-threshold hours 8. |
| Tue, Jun 16 | LIKELY | Ignacio / southeast La Plata County (LIKELY 84/100); Durango / La Plata County (LIKELY 81/100); Bayfield / east La Plata County (LIKELY 81/100); Arboles / southwest county (LIKELY 80/100) | Top weather score 84/100 at Ignacio / southeast La Plata County. Weather score 84/100: RH 8%, wind/gust 36 mph, red-flag hours 10, near-threshold hours 12. |
| Wed, Jun 17 | LIKELY | Arboles / southwest county (LIKELY 84/100); Durango / La Plata County (LIKELY 84/100); Ignacio / southeast La Plata County (LIKELY 84/100); Bayfield / east La Plata County (LIKELY 81/100) | Top weather score 84/100 at Arboles / southwest county. Weather score 84/100: RH 8%, wind/gust 37 mph, red-flag hours 10, near-threshold hours 12. |
| Thu, Jun 18 | LIKELY | Durango / La Plata County (LIKELY 77/100); Bayfield / east La Plata County (LIKELY 77/100); Ignacio / southeast La Plata County (LIKELY 77/100); Arboles / southwest county (LIKELY 74/100) | Top weather score 77/100 at Durango / La Plata County. Weather score 77/100: RH 9%, wind/gust 32 mph, red-flag hours 9, near-threshold hours 11. |

## Area-Specific Outlook

| Area | Today | Peak this run | Highest-risk window |
| --- | --- | --- | --- |
| Bayfield | LIKELY 92/100 | Fri, Jun 12: LIKELY 92/100 | 1 PM-7 PM local; 7 near/red-flag threshold hours. |
| Ignacio | LIKELY 92/100 | Fri, Jun 12: LIKELY 92/100 | 1 PM-7 PM local; 7 near/red-flag threshold hours. |
| Pagosa Springs | LIKELY 86/100 | Fri, Jun 12: LIKELY 86/100 | 1 PM-7 PM local; 7 near/red-flag threshold hours. |
| Arboles | LIKELY 86/100 | Fri, Jun 12: LIKELY 86/100 | 2 PM-7 PM local; 6 near/red-flag threshold hours. |
| Durango | LIKELY 86/100 | Fri, Jun 12: LIKELY 86/100 | 1 PM-7 PM local; 7 near/red-flag threshold hours. |
| Chimney Rock | LIKELY 85/100 | Fri, Jun 12: LIKELY 85/100 | 1 PM-7 PM local; 7 near/red-flag threshold hours. |
| Chromo | LIKELY 82/100 | Fri, Jun 12: LIKELY 82/100 | 1 PM-7 PM local; 7 near/red-flag threshold hours. |
| Piedra | LIKELY 78/100 | Fri, Jun 12: LIKELY 78/100 | 1 PM-7 PM local; 6 near/red-flag threshold hours. |

## Fire Posture + Restrictions

- Summary: 5 official sources indicate fire restrictions or staged restrictions.
- Max restriction stage detected: STAGE 1
- Max fire danger detected: EXTREME
- Sources reachable: 6/7
- Note: Official-source status check only; verify restrictions and burn decisions with the responsible jurisdiction.

| Jurisdiction | Restrictions | Fire danger | Source |
| --- | --- | --- | --- |
| Archuleta County | STAGE 1 | UNKNOWN | [Archuleta County Sheriff fire updates](https://sheriff.archuletacounty.gov/divisions/emergency-operations/fire-updates-and-information/) |
| Pagosa Springs | STAGE 1 | UNKNOWN | [Town of Pagosa Springs](https://www.pagosasprings.co.gov/) |
| San Juan National Forest | STAGE 1 | EXTREME | [San Juan National Forest fire](https://www.fs.usda.gov/r02/sanjuan/fire) |
| BLM Tres Rios | STAGE 1 | UNKNOWN | [BLM Tres Rios Field Office](https://www.blm.gov/office/tres-rios-field-office) |
| La Plata County / Durango Fire | UNKNOWN | UNKNOWN | [Durango Fire & Rescue fire conditions](https://www.durangofire.org/fire-conditions) |
| Durango | UNKNOWN | UNKNOWN | [City of Durango](https://www.durangoco.gov/) |
| Southern Ute / Ignacio | STAGE 1 | UNKNOWN | [Southern Ute Indian Tribe](https://www.southernute-nsn.gov/) |

## Forecast Calibration

### PSPS Calibration

- Summary: No confirmed LPEA PSPS events logged yet; calibration will start once events are added.
- Confirmed PSPS events logged: 0
- Candidate/unconfirmed events logged: 0
- WATCH/LIKELY false-watch past days: 14
- Pending WATCH/LIKELY dates in current forecast: Fri, Jun 12; Sat, Jun 13; Sun, Jun 14; Mon, Jun 15; Tue, Jun 16; Wed, Jun 17; Thu, Jun 18
- Calibration source: manual PSPS event log plus forecast history from prior monitor runs.

### Red Flag / Fire Weather Calibration

- Summary: 6/6 official Red Flag / Fire Weather alert dates had a pre-alert HIGH monitor signal. Average lead time: 4.5 days.
- Official alert dates logged: 6
- Pre-alert HIGH hit rate: 100%
- Average lead time: 4.5 days
- HIGH false-watch past days: 6
- Pending HIGH dates in current forecast: Mon, Jun 15; Tue, Jun 16; Wed, Jun 17; Thu, Jun 18
- Calibration source: official NWS Red Flag / Fire Weather alert dates plus forecast history from prior monitor runs.

## Official Weather Alerts

- Monitored NWS zones: COC007, COC067, COZ019, COZ022, COZ023, COZ295
- [Red Flag Warning](https://api.weather.gov/alerts/urn:oid:2.49.0.1.840.0.ecaacbfd8a7723d81ddfda2a7fe8d47468f6b0af.001.2): Red Flag Warning issued June 11 at 8:17PM MDT until June 12 at 9:00PM MDT by NWS Grand Junction CO; 2026-06-11T20:17:00-06:00 to 2026-06-12T21:00:00-06:00; zones COZ207, COZ293, COZ295

## LPEA Power Signal

- Status: `active_keyword_match` - LPEA active/update sources contained power-interruption keywords; review source before treating as confirmed outage intent.
- Meaning: Active source match means a monitored LPEA active/update source currently contains fire, outage, PSPS, or power-interruption keywords. Operational outages are shown separately and are not treated as PSPS/fire evidence unless the source text says so.
- Operational outage context: No monitored active LPEA source currently describes a non-PSPS outage.
- Source coverage: 13 sources; 5/5 official social sources reachable
- Evidence quality: 0 operational, 3 active/update, 1 archive/context, 4 reference source matches.
- Active/update source pages with matches: LPEA homepage (red flag, public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation); LPEA latest news (red flag, public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation); LPEA news releases (red flag, wildfire, public safety power shutoff, power shutoff, shutoff, power outage); LPEA LinkedIn (wildfire, public safety power shutoff, power shutoff, shutoff)
- Distinct active/update signals: Shared signal across 3 sources across 3 sources: LPEA homepage, LPEA latest news, and LPEA news releases (red flag, public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation); News-release archive PSPS item (red flag, wildfire, public safety power shutoff, power shutoff, shutoff, power outage); LPEA LinkedIn (wildfire, public safety power shutoff, power shutoff, shutoff); LinkedIn PSPS explainer post (wildfire, public safety power shutoff, power shutoff, shutoff)
- Example signal: ...ngs & Resources Board Committees Voting Districts Policies & Bylaws Elections A Red Flag Warning is in effect across our service territory from 10 AM - 10 PM on Thursday, June 11. Learn what Red Flag Warnings...
- Reference/context hits: [LPEA outage center](https://lpea.coop/outage-center); [LPEA wildfire / public safety power shutoffs](https://lpea.coop/psps); [LPEA red flag outage impact page](https://lpea.coop/outages/red-flag-warnings-and-impact-outages-prioritizing-safety-our-members); [LPEA fire mitigation](https://lpea.coop/fire-mitigation)

**Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## Next 7 Days

| Date | Tier | Main reason | Worst sampled metrics |
| --- | --- | --- | --- |
| Fri, Jun 12 | HIGH | Pagosa Springs: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 12%, wind/gust 29 mph, thunder 1%<br>Arboles / southwest county: RH 9%, wind/gust 28 mph, thunder 2%<br>Chimney Rock / west county: RH 8%, wind/gust 28 mph, thunder 1% |
| Sat, Jun 13 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Pagosa Springs: RH 13%, wind/gust 18 mph, thunder 4%<br>Arboles / southwest county: RH 11%, wind/gust 21 mph, thunder 2%<br>Chimney Rock / west county: RH 10%, wind/gust 18 mph, thunder 2% |
| Sun, Jun 14 | ELEVATED | Pagosa Springs: Elevated ingredient present: thunder probability reaches 43%. | Pagosa Springs: RH 25%, wind/gust 18 mph, thunder 43%<br>Arboles / southwest county: RH 20%, wind/gust 22 mph, thunder 35%<br>Chimney Rock / west county: RH 19%, wind/gust 20 mph, thunder 40% |
| Mon, Jun 15 | HIGH | Arboles / southwest county: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 14%, wind/gust 22 mph, thunder 17%<br>Arboles / southwest county: RH 11%, wind/gust 29 mph, thunder 9%<br>Chimney Rock / west county: RH 10%, wind/gust 24 mph, thunder 11% |
| Tue, Jun 16 | HIGH | Pagosa Springs: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 10%, wind/gust 29 mph, thunder 0%<br>Arboles / southwest county: RH 8%, wind/gust 33 mph, thunder 0%<br>Chimney Rock / west county: RH 7%, wind/gust 29 mph, thunder 0% |
| Wed, Jun 17 | HIGH | Pagosa Springs: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 10%, wind/gust 31 mph, thunder 0%<br>Arboles / southwest county: RH 8%, wind/gust 37 mph, thunder 0%<br>Chimney Rock / west county: RH 7%, wind/gust 32 mph, thunder 0% |
| Thu, Jun 18 | HIGH | Pagosa Springs: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 10%, wind/gust 26 mph, thunder 1%<br>Arboles / southwest county: RH 8%, wind/gust 30 mph, thunder 1%<br>Chimney Rock / west county: RH 8%, wind/gust 26 mph, thunder 1% |

## Sample Point Status

- Pagosa Springs: COZ295 (matches), forecast zone COZ023, county zone COC007
- Arboles / southwest county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Chimney Rock / west county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Piedra / north county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Chromo / southeast county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Durango / La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Bayfield / east La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Ignacio / southeast La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
