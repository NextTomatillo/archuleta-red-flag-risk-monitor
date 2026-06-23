# Archuleta Red Flag Risk Monitor

Generated: Jun 23, 2026 at 3:21 AM MDT (Pagosa Springs, CO local time)
Next update: Jun 23, 2026 at 4:21 AM MDT (Pagosa Springs, CO local time)
Date/time basis: Pagosa Springs, CO local time (America/Denver)
> **Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## At A Glance

- Overall tier: **HIGH**
- PSPS likelihood: **LIKELY**
- PSPS likely dates: Tue, Jun 23; Wed, Jun 24; Sat, Jun 27; Sun, Jun 28; Mon, Jun 29
- PSPS watch dates: Thu, Jun 25; Fri, Jun 26
- Monitor heads-up recommended: **YES** - Send this monitor report because current risk is HIGH. This is not an official LPEA or NWS notice.
- HIGH dates: Tue, Jun 23; Wed, Jun 24; Sat, Jun 27; Sun, Jun 28; Mon, Jun 29
- CONCERN dates: Fri, Jun 26
- ELEVATED dates: Thu, Jun 25
- Official NWS Red Flag / Fire Weather alerts (COZ295): 1
- LPEA signal: `active_keyword_match` - LPEA active/update sources contained power-interruption keywords; review source before treating as confirmed outage intent.
- LPEA source coverage: 13 sources; 5/5 official social sources reachable
- NWS discussion: NWS discussion contains fire-weather concern language.

## Decision Support

- Summary: Highest LPEA PSPS concern is Tue, Jun 23 near Pagosa Springs (LIKELY 100/100), driven by red-flag wind/gust signal near 29 mph; critically dry RH near 8%; 6 sampled hours meet red-flag screen.
- Confidence: **MEDIUM** (68/100) - 8/8 sampled weather points available; 6/7 fire-posture sources reachable; official NWS alert zones checked; 13/13 LPEA public sources reachable; LPEA active/update sources checked; forecast changed substantially versus prior run; no confirmed PSPS events logged yet for calibration
- Fire danger peak: Tue, Jun 23: Pagosa Springs EXTREME 100/100
- Red Flag likelihood peak: Tue, Jun 23: Pagosa Springs LIKELY 100/100
- LPEA PSPS peak: Tue, Jun 23: Pagosa Springs LIKELY 100/100
- Method: rules-based decision support using public weather, fire-posture, and LPEA source signals; scores are screening estimates, not official or statistically calibrated probabilities.

| Date | Fire danger | Red Flag likelihood | LPEA PSPS | Main window |
| --- | --- | --- | --- | --- |
| Tue, Jun 23 | Pagosa Springs: EXTREME 100/100 | Pagosa Springs: LIKELY 100/100 | Pagosa Springs: LIKELY 100/100 | 12 PM-8 PM local; 9 near/red-flag threshold hours. |
| Wed, Jun 24 | Chimney Rock / west county: EXTREME 100/100 | Chimney Rock / west county: LIKELY 97/100 | Arboles / southwest county: LIKELY 100/100 | 12 PM-7 PM local; 8 near/red-flag threshold hours. |
| Thu, Jun 25 | Bayfield / east La Plata County: HIGH 64/100 | Chimney Rock / west county: LOW 27/100 | Chimney Rock / west county: WATCH 61/100 | 5 PM-5 PM local; 1 near/red-flag threshold hour. |
| Fri, Jun 26 | Chimney Rock / west county: EXTREME 87/100 | Chimney Rock / west county: LIKELY 75/100 | Chimney Rock / west county: LIKELY 91/100 | 2 PM-7 PM local; 6 near/red-flag threshold hours. |
| Sat, Jun 27 | Arboles / southwest county: EXTREME 100/100 | Arboles / southwest county: LIKELY 100/100 | Pagosa Springs: LIKELY 100/100 | 1 PM-9 PM local; 9 near/red-flag threshold hours. |
| Sun, Jun 28 | Arboles / southwest county: EXTREME 100/100 | Arboles / southwest county: LIKELY 100/100 | Pagosa Springs: LIKELY 100/100 | 1 PM-8 PM local; 8 near/red-flag threshold hours. |
| Mon, Jun 29 | Durango / La Plata County: EXTREME 100/100 | Durango / La Plata County: LIKELY 100/100 | Pagosa Springs: LIKELY 100/100 | 12 PM-8 PM local; 9 near/red-flag threshold hours. |

## Trend Intelligence

- Summary: Momentum is easing versus the prior run (Jun 22 at 3:21 AM MDT); forecast volatility is high and first WATCH-or-higher date is Tue, Jun 23.
- Momentum: **Easing**
- Forecast volatility: **HIGH** (43/100)
- First WATCH-or-higher PSPS date: Tue, Jun 23
- Watch-date movement: First WATCH-or-higher PSPS date moved later from Mon, Jun 22 to Tue, Jun 23.
- Method: compares current forecast evidence against prior local forecast history.

Notable changes:
- First WATCH-or-higher PSPS date moved later from Mon, Jun 22 to Tue, Jun 23.
- Thu, Jun 25: easing vs prior run; PSPS WATCH -> ELEVATED; score -16, wind 0 mph, RH +2%, red-flag hours 0. Driver shifted to Chimney Rock / west county.
- Fri, Jun 26: easing vs prior run; PSPS LIKELY -> WATCH; score -6, wind -4 mph, RH 0%, red-flag hours -1.
- Wed, Jun 24: easing vs prior run; PSPS LIKELY -> LIKELY; score 0, wind -1 mph, RH +2%, red-flag hours -2.

## Public Analysis Export

- Summary: Highest LPEA PSPS concern is Tue, Jun 23 near Pagosa Springs (LIKELY 100/100), driven by red-flag wind/gust signal near 29 mph; critically dry RH near 8%; 6 sampled hours meet red-flag screen.
- Trend: Momentum is easing versus the prior run (Jun 22 at 3:21 AM MDT); forecast volatility is high and first WATCH-or-higher date is Tue, Jun 23.
- Confidence: **MEDIUM** (68/100)
- First WATCH-or-higher PSPS date: Tue, Jun 23
- PSPS peak: Tue, Jun 23 near Pagosa Springs at LIKELY 100/100
- Red Flag peak: Tue, Jun 23 near Pagosa Springs at LIKELY 100/100
- Fire danger peak: Tue, Jun 23 near Pagosa Springs at EXTREME 100/100
- LPEA operational outage context: No monitored active LPEA source currently describes a non-PSPS outage.
- Public JSON: `archuleta_red_flag_monitor/public_analysis_export.json`

What changed:
- First WATCH-or-higher PSPS date moved later from Mon, Jun 22 to Tue, Jun 23.
- Thu, Jun 25: easing vs prior run; PSPS WATCH -> ELEVATED; score -16, wind 0 mph, RH +2%, red-flag hours 0. Driver shifted to Chimney Rock / west county.
- Fri, Jun 26: easing vs prior run; PSPS LIKELY -> WATCH; score -6, wind -4 mph, RH 0%, red-flag hours -1.
- Wed, Jun 24: easing vs prior run; PSPS LIKELY -> LIKELY; score 0, wind -1 mph, RH +2%, red-flag hours -2.

What to watch next:
- Check whether the largest day-level changes line up with wind/RH movement or public-source context.
- Check whether the LPEA active match is still a broad red-flag banner rather than direct PSPS/outage intent.
- Watch whether the highest-risk locations remain consistent across runs or the driver area is moving.
- If a PSPS occurs, log the confirmed date, location, and source so future hit-rate scoring can improve.

## PSPS Likelihood

- **PSPS means Public Safety Power Shutoff:** a planned, safety-related power shutoff LPEA may use during dangerous fire-weather conditions to reduce wildfire ignition risk. See [LPEA PSPS guidance](https://lpea.coop/psps) and the [LPEA outage center](https://lpea.coop/outage-center); if power is out, also check the [LPEA outage map](https://outage.lpea.coop).
- Overall: **LIKELY** - PSPS likelihood is high on weather-driven red-flag days; prepare for possible LPEA safety-related interruption behavior.
- Likely PSPS watch dates: Tue, Jun 23; Wed, Jun 24; Sat, Jun 27; Sun, Jun 28; Mon, Jun 29
- PSPS watch dates: Thu, Jun 25; Fri, Jun 26
- LPEA signal basis: LPEA active/update source contains red-flag, wildfire, or power-interruption language.
- Note: This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

| Date | PSPS likelihood | Driver locations | Weather basis |
| --- | --- | --- | --- |
| Tue, Jun 23 | LIKELY | Bayfield / east La Plata County (LIKELY 95/100); Ignacio / southeast La Plata County (LIKELY 95/100); Pagosa Springs (LIKELY 89/100); Arboles / southwest county (LIKELY 89/100) | Top weather score 95/100 at Bayfield / east La Plata County. Weather score 95/100: RH 8%, wind/gust 32 mph, red-flag hours 7, near-threshold hours 9. |
| Wed, Jun 24 | LIKELY | Durango / La Plata County (LIKELY 77/100); Bayfield / east La Plata County (LIKELY 77/100); Ignacio / southeast La Plata County (LIKELY 77/100); Chimney Rock / west county (LIKELY 75/100) | Top weather score 77/100 at Durango / La Plata County. Weather score 77/100: RH 14%, wind/gust 31 mph, red-flag hours 6, near-threshold hours 9. |
| Thu, Jun 25 | WATCH | Chimney Rock / west county (ELEVATED 41/100); Bayfield / east La Plata County (ELEVATED 41/100); Ignacio / southeast La Plata County (ELEVATED 41/100) | Top weather score 41/100 at Chimney Rock / west county. Weather score 41/100: RH 18%, wind/gust 28 mph, red-flag hours 0, near-threshold hours 1. |
| Fri, Jun 26 | WATCH | Chimney Rock / west county (WATCH 61/100); Durango / La Plata County (WATCH 57/100); Bayfield / east La Plata County (WATCH 53/100); Ignacio / southeast La Plata County (WATCH 53/100) | Top weather score 61/100 at Chimney Rock / west county. Weather score 61/100: RH 15%, wind/gust 28 mph, red-flag hours 2, near-threshold hours 6. |
| Sat, Jun 27 | LIKELY | Arboles / southwest county (LIKELY 81/100); Chimney Rock / west county (LIKELY 81/100); Durango / La Plata County (LIKELY 81/100); Bayfield / east La Plata County (LIKELY 81/100) | Top weather score 81/100 at Arboles / southwest county. Weather score 81/100: RH 11%, wind/gust 47 mph, red-flag hours 10, near-threshold hours 13. |
| Sun, Jun 28 | LIKELY | Arboles / southwest county (LIKELY 81/100); Chimney Rock / west county (LIKELY 81/100); Durango / La Plata County (LIKELY 81/100); Bayfield / east La Plata County (LIKELY 81/100) | Top weather score 81/100 at Arboles / southwest county. Weather score 81/100: RH 10%, wind/gust 40 mph, red-flag hours 10, near-threshold hours 14. |
| Mon, Jun 29 | LIKELY | Pagosa Springs (LIKELY 77/100); Durango / La Plata County (LIKELY 77/100); Bayfield / east La Plata County (LIKELY 77/100); Ignacio / southeast La Plata County (LIKELY 77/100) | Top weather score 77/100 at Pagosa Springs. Weather score 77/100: RH 12%, wind/gust 33 mph, red-flag hours 6, near-threshold hours 9. |

## Area-Specific Outlook

| Area | Today | Peak this run | Highest-risk window |
| --- | --- | --- | --- |
| Bayfield | LIKELY 95/100 | Tue, Jun 23: LIKELY 95/100 | 12 PM-8 PM local; 9 near/red-flag threshold hours. |
| Ignacio | LIKELY 95/100 | Tue, Jun 23: LIKELY 95/100 | 12 PM-8 PM local; 9 near/red-flag threshold hours. |
| Pagosa Springs | LIKELY 89/100 | Tue, Jun 23: LIKELY 89/100 | 12 PM-8 PM local; 9 near/red-flag threshold hours. |
| Arboles | LIKELY 89/100 | Tue, Jun 23: LIKELY 89/100 | 12 PM-8 PM local; 9 near/red-flag threshold hours. |
| Chimney Rock | LIKELY 89/100 | Tue, Jun 23: LIKELY 89/100 | 12 PM-8 PM local; 9 near/red-flag threshold hours. |
| Durango | LIKELY 89/100 | Tue, Jun 23: LIKELY 89/100 | 12 PM-7 PM local; 8 near/red-flag threshold hours. |
| Piedra | LIKELY 86/100 | Tue, Jun 23: LIKELY 86/100 | 12 PM-7 PM local; 8 near/red-flag threshold hours. |
| Chromo | LIKELY 86/100 | Tue, Jun 23: LIKELY 86/100 | 12 PM-8 PM local; 9 near/red-flag threshold hours. |

## Fire Posture + Restrictions

- Summary: 4 official sources indicate fire restrictions or staged restrictions.
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
| Southern Ute / Ignacio | UNKNOWN | UNKNOWN | [Southern Ute Indian Tribe](https://www.southernute-nsn.gov/) |

## Forecast Calibration

### PSPS Calibration

- Summary: No confirmed LPEA PSPS events logged yet; calibration will start once events are added.
- Confirmed PSPS events logged: 0
- Candidate/unconfirmed events logged: 0
- WATCH/LIKELY false-watch past days: 25
- Pending WATCH/LIKELY dates in current forecast: Tue, Jun 23; Wed, Jun 24; Thu, Jun 25; Fri, Jun 26; Sat, Jun 27; Sun, Jun 28; Mon, Jun 29
- Calibration source: manual PSPS event log plus forecast history from prior monitor runs.

### Red Flag / Fire Weather Calibration

- Summary: 14/14 official Red Flag / Fire Weather alert dates had a pre-alert HIGH monitor signal. Average lead time: 4.9 days.
- Official alert dates logged: 14
- Pre-alert HIGH hit rate: 100%
- Average lead time: 4.9 days
- HIGH false-watch past days: 9
- Pending HIGH dates in current forecast: Wed, Jun 24; Sat, Jun 27; Sun, Jun 28; Mon, Jun 29
- Calibration source: official NWS Red Flag / Fire Weather alert dates plus forecast history from prior monitor runs.

## Official Weather Alerts

- Monitored NWS zones: COC007, COC067, COZ019, COZ022, COZ023, COZ295
- [Red Flag Warning](https://api.weather.gov/alerts/urn:oid:2.49.0.1.840.0.c2108b2ac4a480a71e903bae85d89ce295241eb9.003.1): Red Flag Warning issued June 22 at 8:35PM MDT until June 23 at 10:00PM MDT by NWS Grand Junction CO; 2026-06-22T20:35:00-06:00 to 2026-06-23T22:00:00-06:00; zones COZ295

## LPEA Power Signal

- Status: `active_keyword_match` - LPEA active/update sources contained power-interruption keywords; review source before treating as confirmed outage intent.
- Meaning: Active source match means a monitored LPEA active/update source currently contains fire, outage, PSPS, or power-interruption keywords. Operational outages are shown separately and are not treated as PSPS/fire evidence unless the source text says so.
- Operational outage context: No monitored active LPEA source currently describes a non-PSPS outage.
- Source coverage: 13 sources; 5/5 official social sources reachable
- Evidence quality: 0 operational, 5 active/update, 1 archive/context, 4 reference source matches.
- Active/update source pages with matches: LPEA homepage (red flag, public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation); LPEA latest news (red flag, public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation); LPEA news releases (red flag, wildfire, public safety power shutoff, power shutoff, shutoff, power outage); LPEA LinkedIn (wildfire, public safety power shutoff, power shutoff, shutoff)
- Distinct active/update signals: LPEA homepage (red flag, public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation); LPEA latest news (red flag, public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation); LPEA news releases (red flag, wildfire, public safety power shutoff, power shutoff, shutoff, power outage); News-release archive PSPS item (red flag, wildfire, public safety power shutoff, power shutoff, shutoff, power outage); LPEA LinkedIn (wildfire, public safety power shutoff, power shutoff, shutoff)
- Example signal: ...icts Policies & Bylaws Elections All of La Plata and Archuleta County are under Red Flag Warnings. Follow our Facebook for updates. Previous Next LPEA Announces 2026-27 Board Leadership View Board Appointment...
- Reference/context hits: [LPEA outage center](https://lpea.coop/outage-center); [LPEA wildfire / public safety power shutoffs](https://lpea.coop/psps); [LPEA red flag outage impact page](https://lpea.coop/outages/red-flag-warnings-and-impact-outages-prioritizing-safety-our-members); [LPEA fire mitigation](https://lpea.coop/fire-mitigation)

**Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## Next 7 Days

| Date | Tier | Main reason | Worst sampled metrics |
| --- | --- | --- | --- |
| Tue, Jun 23 | HIGH | Pagosa Springs: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 8%, wind/gust 29 mph, thunder 0%<br>Arboles / southwest county: RH 7%, wind/gust 29 mph, thunder 0%<br>Chimney Rock / west county: RH 6%, wind/gust 28 mph, thunder 0% |
| Wed, Jun 24 | HIGH | Pagosa Springs: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 15%, wind/gust 28 mph, thunder 21%<br>Arboles / southwest county: RH 12%, wind/gust 30 mph, thunder 14%<br>Chimney Rock / west county: RH 11%, wind/gust 28 mph, thunder 21% |
| Thu, Jun 25 | ELEVATED | Pagosa Springs: Elevated ingredient present: wind/gust forecast near 28 mph; thunder probability reaches 38%. | Pagosa Springs: RH 24%, wind/gust 28 mph, thunder 38%<br>Arboles / southwest county: RH 21%, wind/gust 30 mph, thunder 29%<br>Chimney Rock / west county: RH 18%, wind/gust 28 mph, thunder 25% |
| Fri, Jun 26 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Pagosa Springs: RH 20%, wind/gust 30 mph, thunder 15%<br>Arboles / southwest county: RH 17%, wind/gust 29 mph, thunder 10%<br>Chimney Rock / west county: RH 15%, wind/gust 28 mph, thunder 15% |
| Sat, Jun 27 | HIGH | Pagosa Springs: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 14%, wind/gust 46 mph, thunder 6%<br>Arboles / southwest county: RH 11%, wind/gust 47 mph, thunder 6%<br>Chimney Rock / west county: RH 10%, wind/gust 45 mph, thunder 7% |
| Sun, Jun 28 | HIGH | Pagosa Springs: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 13%, wind/gust 40 mph, thunder 0%<br>Arboles / southwest county: RH 10%, wind/gust 40 mph, thunder 1%<br>Chimney Rock / west county: RH 9%, wind/gust 40 mph, thunder 1% |
| Mon, Jun 29 | HIGH | Pagosa Springs: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 12%, wind/gust 33 mph, thunder 1%<br>Arboles / southwest county: RH 10%, wind/gust 29 mph, thunder 1%<br>Chimney Rock / west county: RH 9%, wind/gust 29 mph, thunder 1% |

## Sample Point Status

- Pagosa Springs: COZ295 (matches), forecast zone COZ023, county zone COC007
- Arboles / southwest county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Chimney Rock / west county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Piedra / north county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Chromo / southeast county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Durango / La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Bayfield / east La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Ignacio / southeast La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
