# Archuleta Red Flag Risk Monitor

Generated: Jul 8, 2026 at 5:21 AM MDT (Pagosa Springs, CO local time)
Next update: Jul 8, 2026 at 6:21 AM MDT (Pagosa Springs, CO local time)
Date/time basis: Pagosa Springs, CO local time (America/Denver)
> **Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## At A Glance

- Overall tier: **HIGH**
- PSPS likelihood: **LIKELY**
- PSPS likely dates: Thu, Jul 9; Fri, Jul 10
- PSPS watch dates: Wed, Jul 8; Sat, Jul 11; Sun, Jul 12; Mon, Jul 13; Tue, Jul 14
- Monitor heads-up recommended: **YES** - Send this monitor report because current risk is HIGH. This is not an official LPEA or NWS notice.
- HIGH dates: Thu, Jul 9; Fri, Jul 10
- CONCERN dates: Wed, Jul 8; Sun, Jul 12
- ELEVATED dates: Sat, Jul 11; Mon, Jul 13; Tue, Jul 14
- Official NWS Red Flag / Fire Weather alerts (COZ295): 0
- LPEA signal: `active_keyword_match` - LPEA active/update sources contained power-interruption keywords; review source before treating as confirmed outage intent.
- LPEA source coverage: 13 sources; 5/5 official social sources reachable
- NWS discussion: NWS discussion contains fire-weather concern language.

## Decision Support

- Summary: Highest LPEA PSPS concern is Thu, Jul 9 near Arboles / southwest county (LIKELY 100/100), driven by red-flag wind/gust signal near 28 mph; very dry RH near 9%; 4 sampled hours meet red-flag screen.
- Confidence: **MEDIUM** (66/100) - 7/8 sampled weather points available; 7/7 fire-posture sources reachable; official NWS alert zones checked; 13/13 LPEA public sources reachable; LPEA active/update sources checked; forecast changed substantially versus prior run; no confirmed PSPS events logged yet for calibration
- Fire danger peak: Thu, Jul 9: Ignacio / southeast La Plata County EXTREME 100/100
- Red Flag likelihood peak: Thu, Jul 9: Ignacio / southeast La Plata County LIKELY 96/100
- LPEA PSPS peak: Thu, Jul 9: Arboles / southwest county LIKELY 100/100
- Method: rules-based decision support using public weather, fire-posture, and LPEA source signals; scores are screening estimates, not official or statistically calibrated probabilities.

| Date | Fire danger | Red Flag likelihood | LPEA PSPS | Main window |
| --- | --- | --- | --- | --- |
| Wed, Jul 8 | Durango / La Plata County: EXTREME 86/100 | Ignacio / southeast La Plata County: WATCH 64/100 | Ignacio / southeast La Plata County: LIKELY 81/100 | 2 PM-5 PM local; 4 near/red-flag threshold hours. |
| Thu, Jul 9 | Ignacio / southeast La Plata County: EXTREME 100/100 | Ignacio / southeast La Plata County: LIKELY 96/100 | Arboles / southwest county: LIKELY 100/100 | 2 PM-7 PM local; 6 near/red-flag threshold hours. |
| Fri, Jul 10 | Durango / La Plata County: EXTREME 100/100 | Durango / La Plata County: LIKELY 88/100 | Durango / La Plata County: LIKELY 100/100 | 12 PM-7 PM local; 8 near/red-flag threshold hours. |
| Sat, Jul 11 | Chromo / southeast county: VERY HIGH 73/100 | Chromo / southeast county: POSSIBLE 32/100 | Chromo / southeast county: LIKELY 73/100 | Peak ingredients near 11 PM local; RH 34%, wind 31 mph. |
| Sun, Jul 12 | Arboles / southwest county: EXTREME 86/100 | Arboles / southwest county: POSSIBLE 50/100 | Ignacio / southeast La Plata County: LIKELY 71/100 | Peak ingredients near 12 AM local; RH 29%, wind 28 mph. |
| Mon, Jul 13 | Pagosa Springs: HIGH 58/100 | Pagosa Springs: LOW 25/100 | Pagosa Springs: ELEVATED 44/100 | Peak ingredients near 4 PM local; RH 18%, wind 16 mph. |
| Tue, Jul 14 | Pagosa Springs: HIGH 58/100 | Pagosa Springs: LOW 25/100 | Pagosa Springs: ELEVATED 44/100 | Peak ingredients near 3 PM local; RH 18%, wind 15 mph. |

## Trend Intelligence

- Summary: Momentum is rising versus the prior run (Jul 7 at 5:38 PM MDT); forecast volatility is high and first WATCH-or-higher date is Wed, Jul 8.
- Momentum: **Rising**
- Forecast volatility: **HIGH** (33/100)
- First WATCH-or-higher PSPS date: Wed, Jul 8
- Watch-date movement: First WATCH-or-higher PSPS date remains Wed, Jul 8.
- Method: compares current forecast evidence against prior local forecast history.

Notable changes:
- First WATCH-or-higher PSPS date remains Wed, Jul 8.
- Sun, Jul 12: worsening vs prior run; PSPS ELEVATED -> WATCH; score +6, wind +5 mph, RH +1%, red-flag hours 0. Driver shifted to Ignacio / southeast La Plata County.
- Sat, Jul 11: worsening vs prior run; PSPS ELEVATED -> WATCH; score +6, wind +5 mph, RH 0%, red-flag hours 0.
- Wed, Jul 8: easing vs prior run; PSPS WATCH -> WATCH; score -6, wind 0 mph, RH 0%, red-flag hours -2.

## Public Analysis Export

- Summary: Highest LPEA PSPS concern is Thu, Jul 9 near Arboles / southwest county (LIKELY 100/100), driven by red-flag wind/gust signal near 28 mph; very dry RH near 9%; 4 sampled hours meet red-flag screen.
- Trend: Momentum is rising versus the prior run (Jul 7 at 5:38 PM MDT); forecast volatility is high and first WATCH-or-higher date is Wed, Jul 8.
- Confidence: **MEDIUM** (66/100)
- First WATCH-or-higher PSPS date: Wed, Jul 8
- PSPS peak: Thu, Jul 9 near Arboles / southwest county at LIKELY 100/100
- Red Flag peak: Thu, Jul 9 near Ignacio / southeast La Plata County at LIKELY 96/100
- Fire danger peak: Thu, Jul 9 near Ignacio / southeast La Plata County at EXTREME 100/100
- LPEA operational outage context: No monitored active LPEA source currently describes a non-PSPS outage.
- Public JSON: `archuleta_red_flag_monitor/public_analysis_export.json`

What changed:
- First WATCH-or-higher PSPS date remains Wed, Jul 8.
- Sun, Jul 12: worsening vs prior run; PSPS ELEVATED -> WATCH; score +6, wind +5 mph, RH +1%, red-flag hours 0. Driver shifted to Ignacio / southeast La Plata County.
- Sat, Jul 11: worsening vs prior run; PSPS ELEVATED -> WATCH; score +6, wind +5 mph, RH 0%, red-flag hours 0.
- Wed, Jul 8: easing vs prior run; PSPS WATCH -> WATCH; score -6, wind 0 mph, RH 0%, red-flag hours -2.

What to watch next:
- Check whether the largest day-level changes line up with wind/RH movement or public-source context.
- Check whether the LPEA active match is still a broad red-flag banner rather than direct PSPS/outage intent.
- Watch whether the highest-risk locations remain consistent across runs or the driver area is moving.
- If a PSPS occurs, log the confirmed date, location, and source so future hit-rate scoring can improve.

## PSPS Likelihood

- **PSPS means Public Safety Power Shutoff:** a planned, safety-related power shutoff LPEA may use during dangerous fire-weather conditions to reduce wildfire ignition risk. See [LPEA PSPS guidance](https://lpea.coop/psps) and the [LPEA outage center](https://lpea.coop/outage-center); if power is out, also check the [LPEA outage map](https://outage.lpea.coop).
- Overall: **LIKELY** - PSPS likelihood is high on weather-driven red-flag days; prepare for possible LPEA safety-related interruption behavior.
- Likely PSPS watch dates: Thu, Jul 9; Fri, Jul 10
- PSPS watch dates: Wed, Jul 8; Sat, Jul 11; Sun, Jul 12; Mon, Jul 13; Tue, Jul 14
- LPEA signal basis: LPEA active/update source contains red-flag, wildfire, or power-interruption language.
- Note: This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

| Date | PSPS likelihood | Driver locations | Weather basis |
| --- | --- | --- | --- |
| Wed, Jul 8 | WATCH | Ignacio / southeast La Plata County (WATCH 57/100); Durango / La Plata County (WATCH 48/100); Bayfield / east La Plata County (WATCH 48/100) | Top weather score 57/100 at Ignacio / southeast La Plata County. Weather score 57/100: RH 14%, wind/gust 25 mph, red-flag hours 1, near-threshold hours 4. |
| Thu, Jul 9 | LIKELY | Ignacio / southeast La Plata County (LIKELY 77/100); Arboles / southwest county (LIKELY 71/100); Durango / La Plata County (LIKELY 71/100); Bayfield / east La Plata County (LIKELY 71/100) | Top weather score 77/100 at Ignacio / southeast La Plata County. Weather score 77/100: RH 10%, wind/gust 31 mph, red-flag hours 6, near-threshold hours 8. |
| Fri, Jul 10 | LIKELY | Durango / La Plata County (LIKELY 71/100); Bayfield / east La Plata County (LIKELY 67/100); Ignacio / southeast La Plata County (LIKELY 67/100); Arboles / southwest county (WATCH 64/100) | Top weather score 71/100 at Durango / La Plata County. Weather score 71/100: RH 9%, wind/gust 26 mph, red-flag hours 5, near-threshold hours 8. |
| Sat, Jul 11 | WATCH | Chromo / southeast county (WATCH 49/100) | Top weather score 49/100 at Chromo / southeast county. Weather score 49/100: RH 13%, wind/gust 31 mph, red-flag hours 0, near-threshold hours 0. |
| Sun, Jul 12 | WATCH | Ignacio / southeast La Plata County (WATCH 47/100) | Top weather score 47/100 at Ignacio / southeast La Plata County. Weather score 47/100: RH 14%, wind/gust 28 mph, red-flag hours 0, near-threshold hours 0. |
| Mon, Jul 13 | WATCH | Pagosa Springs (ELEVATED 24/100); Arboles / southwest county (ELEVATED 18/100); Piedra / north county (ELEVATED 18/100) | Top weather score 24/100 at Pagosa Springs. Weather score 24/100: RH 18%, wind/gust 16 mph, red-flag hours 0, near-threshold hours 0. |
| Tue, Jul 14 | WATCH | Pagosa Springs (ELEVATED 24/100); Arboles / southwest county (ELEVATED 18/100); Piedra / north county (ELEVATED 18/100) | Top weather score 24/100 at Pagosa Springs. Weather score 24/100: RH 18%, wind/gust 15 mph, red-flag hours 0, near-threshold hours 0. |

## Area-Specific Outlook

| Area | Today | Peak this run | Highest-risk window |
| --- | --- | --- | --- |
| Ignacio | WATCH 57/100 | Thu, Jul 9: LIKELY 77/100 | 1 PM-8 PM local; 8 near/red-flag threshold hours. |
| Arboles | ELEVATED 44/100 | Thu, Jul 9: LIKELY 71/100 | 2 PM-7 PM local; 6 near/red-flag threshold hours. |
| Durango | WATCH 48/100 | Thu, Jul 9: LIKELY 71/100 | 12 PM-8 PM local; 9 near/red-flag threshold hours. |
| Bayfield | WATCH 48/100 | Thu, Jul 9: LIKELY 71/100 | 12 PM-8 PM local; 9 near/red-flag threshold hours. |
| Pagosa Springs | ELEVATED 18/100 | Thu, Jul 9: LIKELY 67/100 | 1 PM-7 PM local; 7 near/red-flag threshold hours. |
| Chromo | ELEVATED 18/100 | Thu, Jul 9: WATCH 63/100 | 3 PM-7 PM local; 5 near/red-flag threshold hours. |
| Piedra | LOW 12/100 | Thu, Jul 9: WATCH 48/100 | 2 PM-7 PM local; 6 near/red-flag threshold hours. |

## Fire Posture + Restrictions

- Summary: 6 official sources indicate fire restrictions or staged restrictions.
- Max restriction stage detected: STAGE 2
- Max fire danger detected: EXTREME
- Sources reachable: 7/7
- Note: Official-source status check only; verify restrictions and burn decisions with the responsible jurisdiction.

| Jurisdiction | Restrictions | Fire danger | Source |
| --- | --- | --- | --- |
| Archuleta County | STAGE 2 | UNKNOWN | [Archuleta County Sheriff fire updates](https://sheriff.archuletacounty.gov/divisions/emergency-operations/fire-updates-and-information/) |
| Pagosa Springs | STAGE 2 | UNKNOWN | [Town of Pagosa Springs](https://www.pagosasprings.co.gov/) |
| San Juan National Forest | STAGE 2 | EXTREME | [San Juan National Forest fire](https://www.fs.usda.gov/r02/sanjuan/fire) |
| BLM Tres Rios | STAGE 1 | UNKNOWN | [BLM Tres Rios Field Office](https://www.blm.gov/office/tres-rios-field-office) |
| La Plata County / Durango Fire | NONE | UNKNOWN | [Durango Fire & Rescue fire conditions](https://www.durangofire.org/fire-conditions) |
| Durango | STAGE 2 | UNKNOWN | [City of Durango](https://www.durangoco.gov/) |
| Southern Ute / Ignacio | STAGE 2 | UNKNOWN | [Southern Ute Indian Tribe](https://www.southernute-nsn.gov/) |

## Forecast Calibration

### PSPS Calibration

- Summary: No confirmed LPEA PSPS events logged yet; calibration will start once events are added.
- Confirmed PSPS events logged: 0
- Candidate/unconfirmed events logged: 0
- WATCH/LIKELY false-watch past days: 39
- Pending WATCH/LIKELY dates in current forecast: Wed, Jul 8; Thu, Jul 9; Fri, Jul 10; Sat, Jul 11; Sun, Jul 12; Mon, Jul 13; Tue, Jul 14
- Calibration source: manual PSPS event log plus forecast history from prior monitor runs.

### Red Flag / Fire Weather Calibration

- Summary: 21/21 official Red Flag / Fire Weather alert dates had a pre-alert HIGH monitor signal. Average lead time: 5.0 days.
- Official alert dates logged: 21
- Pre-alert HIGH hit rate: 100%
- Average lead time: 5.0 days
- HIGH false-watch past days: 13
- Pending HIGH dates in current forecast: Thu, Jul 9; Fri, Jul 10
- Calibration source: official NWS Red Flag / Fire Weather alert dates plus forecast history from prior monitor runs.

## Official Weather Alerts

- Monitored NWS zones: COC007, COC067, COZ019, COZ022, COZ023, COZ295
- [Air Quality Alert](https://api.weather.gov/alerts/urn:oid:2.49.0.1.840.0.561029007fa1e80005fa6cbea3d5c5f1ccf77887.001.1): Air Quality Alert issued July 7 at 4:10PM MDT by NWS Grand Junction CO; 2026-07-07T16:10:00-06:00 to 2026-07-08T09:00:00-06:00; zones COC029, COC033, COC037, COC051, COC053, COC067, COC077, COC083, COC085, COC091, COC097, COC111, COC113
- [Air Quality Alert](https://api.weather.gov/alerts/urn:oid:2.49.0.1.840.0.d84c48025089e4b476c823a5ec3fbdfaf6666ec5.001.1): Air Quality Alert issued July 7 at 9:10AM MDT by NWS Grand Junction CO; 2026-07-07T09:10:00-06:00 to 2026-07-08T09:00:00-06:00; zones COC029, COC033, COC037, COC051, COC053, COC067, COC077, COC083, COC085, COC091, COC097, COC111, COC113

## LPEA Power Signal

- Status: `active_keyword_match` - LPEA active/update sources contained power-interruption keywords; review source before treating as confirmed outage intent.
- Meaning: Active source match means a monitored LPEA active/update source currently contains fire, outage, PSPS, or power-interruption keywords. Operational outages are shown separately and are not treated as PSPS/fire evidence unless the source text says so.
- Operational outage context: No monitored active LPEA source currently describes a non-PSPS outage.
- Source coverage: 13 sources; 5/5 official social sources reachable
- Evidence quality: 0 operational, 3 active/update, 2 archive/context, 4 reference source matches.
- Active/update source pages with matches: LPEA homepage (red flag, public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation); LPEA latest news (public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation, restoration); LPEA news releases (red flag, wildfire, public safety power shutoff, power shutoff, shutoff, power outage); LPEA LinkedIn (wildfire, public safety power shutoff, power shutoff, shutoff, fire mitigation)
- Distinct active/update signals: LPEA homepage (red flag, public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation); LPEA news releases (red flag, wildfire, public safety power shutoff, power shutoff, shutoff, power outage); News-release archive PSPS item (red flag, wildfire, public safety power shutoff, power shutoff, shutoff, power outage); LPEA LinkedIn (wildfire, public safety power shutoff, power shutoff, shutoff, fire mitigation); LinkedIn PSPS explainer post (wildfire, public safety power shutoff, power shutoff, shutoff, fire mitigation)
- Example signal: ...lections Stop by our Energy & Rebate Office Hours July 8 in Durango Get details Red Flag Conditions May Result in Longer, More Frequent Outages Learn Why That's a Good Thing LPEA Announces 2026-27 Board Leade...
- Reference/context hits: [LPEA outage center](https://lpea.coop/outage-center); [LPEA wildfire / public safety power shutoffs](https://lpea.coop/psps); [LPEA red flag outage impact page](https://lpea.coop/outages/red-flag-warnings-and-impact-outages-prioritizing-safety-our-members); [LPEA fire mitigation](https://lpea.coop/fire-mitigation)

**Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## Next 7 Days

| Date | Tier | Main reason | Worst sampled metrics |
| --- | --- | --- | --- |
| Wed, Jul 8 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Pagosa Springs: RH 20%, wind/gust 20 mph, thunder 39%<br>Arboles / southwest county: RH 14%, wind/gust 22 mph, thunder 11%<br>Piedra / north county: RH 23%, wind/gust 16 mph, thunder 36% |
| Thu, Jul 9 | HIGH | Pagosa Springs: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 13%, wind/gust 26 mph, thunder 4%<br>Arboles / southwest county: RH 9%, wind/gust 28 mph, thunder 5%<br>Piedra / north county: RH 15%, wind/gust 24 mph, thunder 4% |
| Fri, Jul 10 | HIGH | Durango / La Plata County: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 13%, wind/gust 22 mph, thunder 1%<br>Arboles / southwest county: RH 8%, wind/gust 25 mph, thunder 0%<br>Piedra / north county: RH 14%, wind/gust 21 mph, thunder 1% |
| Sat, Jul 11 | ELEVATED | Pagosa Springs: Elevated ingredient present: very low RH forecast near 12%. | Pagosa Springs: RH 12%, wind/gust 22 mph, thunder 3%<br>Arboles / southwest county: RH 9%, wind/gust 20 mph, thunder 2%<br>Piedra / north county: RH 13%, wind/gust 18 mph, thunder 4% |
| Sun, Jul 12 | CONCERN | Arboles / southwest county: Dry-thunder signal: thunder probability reaches 20% with low precipitation probability. | Pagosa Springs: RH 15%, wind/gust 20 mph, thunder 9%<br>Arboles / southwest county: RH 13%, wind/gust 22 mph, thunder 20%<br>Chromo / southeast county: RH 16%, wind/gust 31 mph, thunder 11% |
| Mon, Jul 13 | ELEVATED | Pagosa Springs: Elevated ingredient present: thunder probability reaches 23%. | Pagosa Springs: RH 18%, wind/gust 16 mph, thunder 23%<br>Arboles / southwest county: RH 19%, wind/gust 16 mph, thunder 23%<br>Piedra / north county: RH 22%, wind/gust 16 mph, thunder 30% |
| Tue, Jul 14 | ELEVATED | Pagosa Springs: Elevated ingredient present: thunder probability reaches 25%. | Pagosa Springs: RH 18%, wind/gust 15 mph, thunder 25%<br>Arboles / southwest county: RH 19%, wind/gust 16 mph, thunder 24%<br>Piedra / north county: RH 21%, wind/gust 15 mph, thunder 29% |

## Sample Point Status

- Pagosa Springs: COZ295 (matches), forecast zone COZ023, county zone COC007
- Arboles / southwest county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Chimney Rock / west county: unavailable (ReadTimeout: HTTPSConnectionPool(host='api.weather.gov', port=443): Read timed out. (read timeout=60))
- Piedra / north county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Chromo / southeast county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Durango / La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Bayfield / east La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Ignacio / southeast La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
