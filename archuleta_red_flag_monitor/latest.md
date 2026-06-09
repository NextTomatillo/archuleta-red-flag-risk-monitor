# Archuleta Red Flag Risk Monitor

Generated: Jun 8, 2026 at 11:21 PM MDT (Pagosa Springs, CO local time)
Next update: Jun 9, 2026 at 12:21 AM MDT (Pagosa Springs, CO local time)
Date/time basis: Pagosa Springs, CO local time (America/Denver)
> **Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## At A Glance

- Overall tier: **HIGH**
- PSPS likelihood: **LIKELY**
- PSPS likely dates: Tue, Jun 9; Wed, Jun 10; Thu, Jun 11; Fri, Jun 12; Sat, Jun 13; Sun, Jun 14
- PSPS watch dates: None
- Monitor heads-up recommended: **YES** - Send this monitor report because current risk is HIGH. This is not an official LPEA or NWS notice.
- HIGH dates: Mon, Jun 8; Tue, Jun 9; Wed, Jun 10; Thu, Jun 11; Fri, Jun 12; Sat, Jun 13; Sun, Jun 14
- CONCERN dates: None
- ELEVATED dates: None
- Official NWS Red Flag / Fire Weather alerts (COZ295): 3
- LPEA signal: `active_keyword_match` - LPEA active/update sources contained power-interruption keywords; review source before treating as confirmed outage intent.
- LPEA source coverage: 13 sources; 5/5 official social sources reachable
- NWS discussion: NWS discussion contains fire-weather concern language.

## Decision Support

- Summary: Highest LPEA PSPS concern is Tue, Jun 9 near Pagosa Springs (LIKELY 100/100), driven by very strong wind/gust signal near 41 mph; red-flag RH near 15%; 4 sampled hours are near red-flag thresholds.
- Confidence: **MEDIUM** (69/100) - 8/8 sampled weather points available; 7/7 fire-posture sources reachable; official NWS alert zones checked; 13/13 LPEA public sources reachable; LPEA active/update sources checked; forecast changed substantially versus prior run; no confirmed PSPS events logged yet for calibration
- Fire danger peak: Tue, Jun 9: Arboles / southwest county EXTREME 100/100
- Red Flag likelihood peak: Tue, Jun 9: Arboles / southwest county LIKELY 100/100
- LPEA PSPS peak: Tue, Jun 9: Pagosa Springs LIKELY 100/100
- Method: rules-based decision support using public weather, fire-posture, and LPEA source signals; scores are screening estimates, not official or statistically calibrated probabilities.

| Date | Fire danger | Red Flag likelihood | LPEA PSPS | Main window |
| --- | --- | --- | --- | --- |
| Mon, Jun 8 | Chimney Rock / west county: MODERATE 38/100 | Chimney Rock / west county: LOW 20/100 | Chimney Rock / west county: WATCH 53/100 | Peak ingredients near 11 PM local; RH 22%, wind 13 mph. |
| Tue, Jun 9 | Arboles / southwest county: EXTREME 100/100 | Arboles / southwest county: LIKELY 100/100 | Pagosa Springs: LIKELY 100/100 | 5 PM-8 PM local; 4 near/red-flag threshold hours. |
| Wed, Jun 10 | Pagosa Springs: EXTREME 100/100 | Pagosa Springs: LIKELY 100/100 | Pagosa Springs: LIKELY 100/100 | 12 PM-8 PM local; 9 near/red-flag threshold hours. |
| Thu, Jun 11 | Arboles / southwest county: EXTREME 100/100 | Pagosa Springs: LIKELY 100/100 | Pagosa Springs: LIKELY 100/100 | 1 PM-7 PM local; 7 near/red-flag threshold hours. |
| Fri, Jun 12 | Bayfield / east La Plata County: EXTREME 90/100 | Bayfield / east La Plata County: LIKELY 88/100 | Durango / La Plata County: LIKELY 100/100 | 1 PM-7 PM local; 7 near/red-flag threshold hours. |
| Sat, Jun 13 | Durango / La Plata County: EXTREME 90/100 | Durango / La Plata County: LIKELY 88/100 | Durango / La Plata County: LIKELY 100/100 | 1 PM-8 PM local; 8 near/red-flag threshold hours. |
| Sun, Jun 14 | Durango / La Plata County: EXTREME 100/100 | Durango / La Plata County: LIKELY 100/100 | Arboles / southwest county: LIKELY 100/100 | 1 PM-8 PM local; 8 near/red-flag threshold hours. |

## Trend Intelligence

- Summary: Momentum is easing versus the prior run (Jun 8 at 11:21 AM MDT); forecast volatility is high and first WATCH-or-higher date is Tue, Jun 9.
- Momentum: **Easing**
- Forecast volatility: **HIGH** (94/100)
- First WATCH-or-higher PSPS date: Tue, Jun 9
- Watch-date movement: First WATCH-or-higher PSPS date moved later from Mon, Jun 8 to Tue, Jun 9.
- Method: compares current forecast evidence against prior local forecast history.

Notable changes:
- First WATCH-or-higher PSPS date moved later from Mon, Jun 8 to Tue, Jun 9.
- Mon, Jun 8: easing vs prior run; PSPS LIKELY -> ELEVATED; score -65, wind -16 mph, RH +11%, red-flag hours -7. Driver shifted to Chimney Rock / west county.

## Public Analysis Export

- Summary: Highest LPEA PSPS concern is Tue, Jun 9 near Pagosa Springs (LIKELY 100/100), driven by very strong wind/gust signal near 41 mph; red-flag RH near 15%; 4 sampled hours are near red-flag thresholds.
- Trend: Momentum is easing versus the prior run (Jun 8 at 11:21 AM MDT); forecast volatility is high and first WATCH-or-higher date is Tue, Jun 9.
- Confidence: **MEDIUM** (69/100)
- First WATCH-or-higher PSPS date: Tue, Jun 9
- PSPS peak: Tue, Jun 9 near Pagosa Springs at LIKELY 100/100
- Red Flag peak: Tue, Jun 9 near Arboles / southwest county at LIKELY 100/100
- Fire danger peak: Tue, Jun 9 near Arboles / southwest county at EXTREME 100/100
- LPEA operational outage context: No monitored active LPEA source currently describes a non-PSPS outage.
- Public JSON: `archuleta_red_flag_monitor/public_analysis_export.json`

What changed:
- First WATCH-or-higher PSPS date moved later from Mon, Jun 8 to Tue, Jun 9.
- Mon, Jun 8: easing vs prior run; PSPS LIKELY -> ELEVATED; score -65, wind -16 mph, RH +11%, red-flag hours -7. Driver shifted to Chimney Rock / west county.

What to watch next:
- Check whether the largest day-level changes line up with wind/RH movement or public-source context.
- Check whether the LPEA active match is still a broad red-flag banner rather than direct PSPS/outage intent.
- Watch whether the highest-risk locations remain consistent across runs or the driver area is moving.
- If a PSPS occurs, log the confirmed date, location, and source so future hit-rate scoring can improve.

## PSPS Likelihood

- **PSPS means Public Safety Power Shutoff:** a planned, safety-related power shutoff LPEA may use during dangerous fire-weather conditions to reduce wildfire ignition risk. See [LPEA PSPS guidance](https://lpea.coop/psps) and the [LPEA outage center](https://lpea.coop/outage-center); if power is out, also check the [LPEA outage map](https://outage.lpea.coop).
- Overall: **LIKELY** - PSPS likelihood is high on weather-driven red-flag days; prepare for possible LPEA safety-related interruption behavior.
- Likely PSPS watch dates: Tue, Jun 9; Wed, Jun 10; Thu, Jun 11; Fri, Jun 12; Sat, Jun 13; Sun, Jun 14
- PSPS watch dates: None
- LPEA signal basis: LPEA active/update source contains red-flag, wildfire, or power-interruption language.
- Note: This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

| Date | PSPS likelihood | Driver locations | Weather basis |
| --- | --- | --- | --- |
| Mon, Jun 8 | ELEVATED | Chimney Rock / west county (ELEVATED 21/100); Durango / La Plata County (ELEVATED 21/100); Pagosa Springs (LOW 15/100) | Top weather score 21/100 at Chimney Rock / west county. Weather score 21/100: RH 22%, wind/gust 13 mph, red-flag hours 0, near-threshold hours 0. |
| Tue, Jun 9 | LIKELY | Chimney Rock / west county (LIKELY 100/100); Arboles / southwest county (LIKELY 96/100); Durango / La Plata County (LIKELY 96/100); Bayfield / east La Plata County (LIKELY 96/100) | Top weather score 100/100 at Chimney Rock / west county. Weather score 100/100: RH 10%, wind/gust 41 mph, red-flag hours 7, near-threshold hours 10. |
| Wed, Jun 10 | LIKELY | Bayfield / east La Plata County (LIKELY 96/100); Chimney Rock / west county (LIKELY 95/100); Pagosa Springs (LIKELY 92/100); Arboles / southwest county (LIKELY 92/100) | Top weather score 96/100 at Bayfield / east La Plata County. Weather score 96/100: RH 10%, wind/gust 36 mph, red-flag hours 8, near-threshold hours 10. |
| Thu, Jun 11 | LIKELY | Arboles / southwest county (LIKELY 95/100); Durango / La Plata County (LIKELY 95/100); Bayfield / east La Plata County (LIKELY 95/100); Ignacio / southeast La Plata County (LIKELY 95/100) | Top weather score 95/100 at Arboles / southwest county. Weather score 95/100: RH 8%, wind/gust 31 mph, red-flag hours 8, near-threshold hours 9. |
| Fri, Jun 12 | LIKELY | Durango / La Plata County (LIKELY 71/100); Bayfield / east La Plata County (LIKELY 71/100); Ignacio / southeast La Plata County (LIKELY 71/100); Arboles / southwest county (LIKELY 67/100) | Top weather score 71/100 at Durango / La Plata County. Weather score 71/100: RH 9%, wind/gust 28 mph, red-flag hours 4, near-threshold hours 7. |
| Sat, Jun 13 | LIKELY | Durango / La Plata County (LIKELY 71/100); Bayfield / east La Plata County (LIKELY 71/100); Ignacio / southeast La Plata County (LIKELY 71/100); Arboles / southwest county (WATCH 52/100) | Top weather score 71/100 at Durango / La Plata County. Weather score 71/100: RH 11%, wind/gust 29 mph, red-flag hours 5, near-threshold hours 8. |
| Sun, Jun 14 | LIKELY | Durango / La Plata County (LIKELY 77/100); Bayfield / east La Plata County (LIKELY 77/100); Ignacio / southeast La Plata County (LIKELY 77/100); Arboles / southwest county (LIKELY 71/100) | Top weather score 77/100 at Durango / La Plata County. Weather score 77/100: RH 11%, wind/gust 32 mph, red-flag hours 7, near-threshold hours 9. |

## Area-Specific Outlook

| Area | Today | Peak this run | Highest-risk window |
| --- | --- | --- | --- |
| Chimney Rock | ELEVATED 21/100 | Tue, Jun 9: LIKELY 100/100 | 2 PM-11 PM local; 10 near/red-flag threshold hours. |
| Arboles | LOW 15/100 | Tue, Jun 9: LIKELY 96/100 | 2 PM-11 PM local; 10 near/red-flag threshold hours. |
| Durango | ELEVATED 21/100 | Tue, Jun 9: LIKELY 96/100 | 2 PM-11 PM local; 10 near/red-flag threshold hours. |
| Bayfield | LOW 15/100 | Tue, Jun 9: LIKELY 96/100 | 3 PM-10 PM local; 8 near/red-flag threshold hours. |
| Ignacio | LOW 15/100 | Tue, Jun 9: LIKELY 96/100 | 2 PM-11 PM local; 10 near/red-flag threshold hours. |
| Pagosa Springs | LOW 15/100 | Wed, Jun 10: LIKELY 92/100 | 12 PM-8 PM local; 9 near/red-flag threshold hours. |
| Piedra | LOW 15/100 | Wed, Jun 10: LIKELY 88/100 | 1 PM-8 PM local; 8 near/red-flag threshold hours. |
| Chromo | LOW 15/100 | Wed, Jun 10: LIKELY 86/100 | 11 AM-8 PM local; 10 near/red-flag threshold hours. |

## Fire Posture + Restrictions

- Summary: 5 official sources indicate fire restrictions or staged restrictions.
- Max restriction stage detected: STAGE 1
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
| Durango | UNKNOWN | UNKNOWN | [City of Durango](https://www.durangoco.gov/) |
| Southern Ute / Ignacio | STAGE 1 | UNKNOWN | [Southern Ute Indian Tribe](https://www.southernute-nsn.gov/) |

## Forecast Calibration

### PSPS Calibration

- Summary: No confirmed LPEA PSPS events logged yet; calibration will start once events are added.
- Confirmed PSPS events logged: 0
- Candidate/unconfirmed events logged: 0
- WATCH/LIKELY false-watch past days: 10
- Pending WATCH/LIKELY dates in current forecast: Tue, Jun 9; Wed, Jun 10; Thu, Jun 11; Fri, Jun 12; Sat, Jun 13; Sun, Jun 14
- Calibration source: manual PSPS event log plus forecast history from prior monitor runs.

### Red Flag / Fire Weather Calibration

- Summary: 5/5 official Red Flag / Fire Weather alert dates had a pre-alert HIGH monitor signal. Average lead time: 4.4 days.
- Official alert dates logged: 5
- Pre-alert HIGH hit rate: 100%
- Average lead time: 4.4 days
- HIGH false-watch past days: 6
- Pending HIGH dates in current forecast: Fri, Jun 12; Sat, Jun 13; Sun, Jun 14
- Calibration source: official NWS Red Flag / Fire Weather alert dates plus forecast history from prior monitor runs.

## Official Weather Alerts

- Monitored NWS zones: COC007, COC067, COZ019, COZ022, COZ023, COZ295
- [Fire Weather Watch](https://api.weather.gov/alerts/urn:oid:2.49.0.1.840.0.ac96ace3cbbd33baf5f1d6f7eab462d1761b8cbd.001.4): Fire Weather Watch issued June 8 at 9:05PM MDT until June 11 at 8:00PM MDT by NWS Grand Junction CO; 2026-06-08T21:05:00-06:00 to 2026-06-11T20:00:00-06:00; zones COZ207, COZ291, COZ292, COZ293, COZ294, COZ295
- [Red Flag Warning](https://api.weather.gov/alerts/urn:oid:2.49.0.1.840.0.ac96ace3cbbd33baf5f1d6f7eab462d1761b8cbd.001.2): Red Flag Warning issued June 8 at 9:05PM MDT until June 9 at 10:00PM MDT by NWS Grand Junction CO; 2026-06-08T21:05:00-06:00 to 2026-06-09T22:00:00-06:00; zones COZ207, COZ291, COZ292, COZ293, COZ294, COZ295
- [Red Flag Warning](https://api.weather.gov/alerts/urn:oid:2.49.0.1.840.0.ac96ace3cbbd33baf5f1d6f7eab462d1761b8cbd.001.3): Red Flag Warning issued June 8 at 9:05PM MDT until June 10 at 10:00PM MDT by NWS Grand Junction CO; 2026-06-08T21:05:00-06:00 to 2026-06-10T22:00:00-06:00; zones COZ207, COZ291, COZ292, COZ293, COZ294, COZ295
- [Wind Advisory](https://api.weather.gov/alerts/urn:oid:2.49.0.1.840.0.52ccca9378c8a82625e7ce70b568bafdd14d0847.001.1): Wind Advisory issued June 8 at 10:48PM MDT until June 9 at 8:00PM MDT by NWS Grand Junction CO; 2026-06-08T22:48:00-06:00 to 2026-06-09T20:00:00-06:00; zones COZ002, COZ007, COZ008, COZ011, COZ020, COZ021, COZ022, UTZ022

## LPEA Power Signal

- Status: `active_keyword_match` - LPEA active/update sources contained power-interruption keywords; review source before treating as confirmed outage intent.
- Meaning: Active source match means a monitored LPEA active/update source currently contains fire, outage, PSPS, or power-interruption keywords. Operational outages are shown separately and are not treated as PSPS/fire evidence unless the source text says so.
- Operational outage context: No monitored active LPEA source currently describes a non-PSPS outage.
- Source coverage: 13 sources; 5/5 official social sources reachable
- Evidence quality: 0 operational, 3 active/update, 1 archive/context, 4 reference source matches.
- Active/update source pages with matches: LPEA homepage (red flag, public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation); LPEA latest news (red flag, public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation); LPEA news releases (red flag, wildfire, public safety power shutoff, power shutoff, shutoff, power outage); LPEA LinkedIn (wildfire, public safety power shutoff, power shutoff, shutoff)
- Distinct active/update signals: Shared signal across 3 sources across 3 sources: LPEA homepage, LPEA latest news, and LPEA news releases (red flag, public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation); News-release archive PSPS item (red flag, wildfire, public safety power shutoff, power shutoff, shutoff, power outage); LinkedIn wildfire preparedness post (wildfire, public safety power shutoff, power shutoff, shutoff); LinkedIn PSPS explainer post (wildfire, public safety power shutoff, power shutoff, shutoff)
- Example signal: ...ngs & Resources Board Committees Voting Districts Policies & Bylaws Elections A Red Flag Warning will be in effect from 10 AM - 10 PM Monday, June 8. Learn what Red Flag Warnings mean for your power. Previous...
- Reference/context hits: [LPEA outage center](https://lpea.coop/outage-center); [LPEA wildfire / public safety power shutoffs](https://lpea.coop/psps); [LPEA red flag outage impact page](https://lpea.coop/outages/red-flag-warnings-and-impact-outages-prioritizing-safety-our-members); [LPEA fire mitigation](https://lpea.coop/fire-mitigation)

**Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## Next 7 Days

| Date | Tier | Main reason | Worst sampled metrics |
| --- | --- | --- | --- |
| Mon, Jun 8 | HIGH | Active NWS Red Flag Warning or Fire Weather Watch touches this local date. | No standout sampled point. |
| Tue, Jun 9 | HIGH | Arboles / southwest county: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 15%, wind/gust 41 mph, thunder 23%<br>Arboles / southwest county: RH 10%, wind/gust 41 mph, thunder 14%<br>Chimney Rock / west county: RH 10%, wind/gust 41 mph, thunder 17% |
| Wed, Jun 10 | HIGH | Pagosa Springs: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 11%, wind/gust 33 mph, thunder 1%<br>Arboles / southwest county: RH 9%, wind/gust 32 mph, thunder 1%<br>Chimney Rock / west county: RH 8%, wind/gust 32 mph, thunder 1% |
| Thu, Jun 11 | HIGH | Pagosa Springs: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 9%, wind/gust 29 mph, thunder 1%<br>Arboles / southwest county: RH 8%, wind/gust 31 mph, thunder 0%<br>Chimney Rock / west county: RH 7%, wind/gust 28 mph, thunder 1% |
| Fri, Jun 12 | HIGH | Arboles / southwest county: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 11%, wind/gust 25 mph, thunder 1%<br>Arboles / southwest county: RH 9%, wind/gust 26 mph, thunder 1%<br>Chimney Rock / west county: RH 8%, wind/gust 25 mph, thunder 1% |
| Sat, Jun 13 | HIGH | Durango / La Plata County: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 14%, wind/gust 22 mph, thunder 4%<br>Arboles / southwest county: RH 10%, wind/gust 24 mph, thunder 2%<br>Chimney Rock / west county: RH 10%, wind/gust 23 mph, thunder 2% |
| Sun, Jun 14 | HIGH | Arboles / southwest county: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 14%, wind/gust 24 mph, thunder 13%<br>Arboles / southwest county: RH 11%, wind/gust 30 mph, thunder 5%<br>Chimney Rock / west county: RH 10%, wind/gust 26 mph, thunder 7% |

## Sample Point Status

- Pagosa Springs: COZ295 (matches), forecast zone COZ023, county zone COC007
- Arboles / southwest county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Chimney Rock / west county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Piedra / north county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Chromo / southeast county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Durango / La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Bayfield / east La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Ignacio / southeast La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
