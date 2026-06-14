# Archuleta Red Flag Risk Monitor

Generated: Jun 14, 2026 at 5:37 PM MDT (Pagosa Springs, CO local time)
Next update: Jun 14, 2026 at 6:37 PM MDT (Pagosa Springs, CO local time)
Date/time basis: Pagosa Springs, CO local time (America/Denver)
> **Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## At A Glance

- Overall tier: **HIGH**
- PSPS likelihood: **LIKELY**
- PSPS likely dates: Mon, Jun 15; Tue, Jun 16; Wed, Jun 17; Thu, Jun 18; Fri, Jun 19; Sat, Jun 20
- PSPS watch dates: Sun, Jun 14
- Monitor heads-up recommended: **YES** - Send this monitor report because current risk is HIGH. This is not an official LPEA or NWS notice.
- HIGH dates: Mon, Jun 15; Tue, Jun 16; Wed, Jun 17; Thu, Jun 18; Fri, Jun 19; Sat, Jun 20
- CONCERN dates: None
- ELEVATED dates: Sun, Jun 14
- Official NWS Red Flag / Fire Weather alerts (COZ295): 0
- LPEA signal: `active_keyword_match` - LPEA active/update sources contained power-interruption keywords; review source before treating as confirmed outage intent.
- LPEA source coverage: 13 sources; 5/5 official social sources reachable
- NWS discussion: NWS discussion contains fire-weather concern language.

## Decision Support

- Summary: Highest LPEA PSPS concern is Mon, Jun 15 near Durango / La Plata County (LIKELY 100/100), driven by red-flag wind/gust signal near 28 mph; very dry RH near 12%; 4 sampled hours meet red-flag screen.
- Confidence: **HIGH** (77/100) - 8/8 sampled weather points available; 7/7 fire-posture sources reachable; official NWS alert zones checked; 13/13 LPEA public sources reachable; LPEA active/update sources checked; no confirmed PSPS events logged yet for calibration
- Fire danger peak: Tue, Jun 16: Arboles / southwest county EXTREME 100/100
- Red Flag likelihood peak: Tue, Jun 16: Arboles / southwest county LIKELY 100/100
- LPEA PSPS peak: Mon, Jun 15: Durango / La Plata County LIKELY 100/100
- Method: rules-based decision support using public weather, fire-posture, and LPEA source signals; scores are screening estimates, not official or statistically calibrated probabilities.

| Date | Fire danger | Red Flag likelihood | LPEA PSPS | Main window |
| --- | --- | --- | --- | --- |
| Sun, Jun 14 | Durango / La Plata County: HIGH 59/100 | Durango / La Plata County: LOW 25/100 | Durango / La Plata County: WATCH 46/100 | Peak ingredients near 5 PM local; RH 22%, wind 23 mph. |
| Mon, Jun 15 | Ignacio / southeast La Plata County: EXTREME 98/100 | Durango / La Plata County: LIKELY 89/100 | Durango / La Plata County: LIKELY 100/100 | 2 PM-7 PM local; 6 near/red-flag threshold hours. |
| Tue, Jun 16 | Arboles / southwest county: EXTREME 100/100 | Arboles / southwest county: LIKELY 100/100 | Arboles / southwest county: LIKELY 100/100 | 12 PM-9 PM local; 10 near/red-flag threshold hours. |
| Wed, Jun 17 | Arboles / southwest county: EXTREME 100/100 | Arboles / southwest county: LIKELY 100/100 | Pagosa Springs: LIKELY 100/100 | 1 PM-7 PM local; 7 near/red-flag threshold hours. |
| Thu, Jun 18 | Durango / La Plata County: EXTREME 100/100 | Durango / La Plata County: LIKELY 100/100 | Arboles / southwest county: LIKELY 100/100 | 12 PM-7 PM local; 8 near/red-flag threshold hours. |
| Fri, Jun 19 | Bayfield / east La Plata County: EXTREME 89/100 | Bayfield / east La Plata County: LIKELY 80/100 | Bayfield / east La Plata County: LIKELY 97/100 | 2 PM-7 PM local; 6 near/red-flag threshold hours. |
| Sat, Jun 20 | Durango / La Plata County: EXTREME 100/100 | Durango / La Plata County: LIKELY 100/100 | Arboles / southwest county: LIKELY 100/100 | 12 PM-7 PM local; 8 near/red-flag threshold hours. |

## Trend Intelligence

- Summary: Momentum is steady versus the prior run (Jun 14 at 6:00 AM MDT); forecast volatility is low and first WATCH-or-higher date is Mon, Jun 15.
- Momentum: **Steady**
- Forecast volatility: **LOW** (4/100)
- First WATCH-or-higher PSPS date: Mon, Jun 15
- Watch-date movement: First WATCH-or-higher PSPS date remains Mon, Jun 15.
- Method: compares current forecast evidence against prior local forecast history.

Notable changes:
- First WATCH-or-higher PSPS date remains Mon, Jun 15.
- No major day-level movement versus the prior run.

## Public Analysis Export

- Summary: Highest LPEA PSPS concern is Mon, Jun 15 near Durango / La Plata County (LIKELY 100/100), driven by red-flag wind/gust signal near 28 mph; very dry RH near 12%; 4 sampled hours meet red-flag screen.
- Trend: Momentum is steady versus the prior run (Jun 14 at 6:00 AM MDT); forecast volatility is low and first WATCH-or-higher date is Mon, Jun 15.
- Confidence: **HIGH** (77/100)
- First WATCH-or-higher PSPS date: Mon, Jun 15
- PSPS peak: Mon, Jun 15 near Durango / La Plata County at LIKELY 100/100
- Red Flag peak: Tue, Jun 16 near Arboles / southwest county at LIKELY 100/100
- Fire danger peak: Tue, Jun 16 near Arboles / southwest county at EXTREME 100/100
- LPEA operational outage context: No monitored active LPEA source currently describes a non-PSPS outage.
- Public JSON: `archuleta_red_flag_monitor/public_analysis_export.json`

What changed:
- First WATCH-or-higher PSPS date remains Mon, Jun 15.
- No major day-level movement versus the prior run.

What to watch next:
- Check whether the largest day-level changes line up with wind/RH movement or public-source context.
- Check whether the LPEA active match is still a broad red-flag banner rather than direct PSPS/outage intent.
- Watch whether the highest-risk locations remain consistent across runs or the driver area is moving.
- If a PSPS occurs, log the confirmed date, location, and source so future hit-rate scoring can improve.

## PSPS Likelihood

- **PSPS means Public Safety Power Shutoff:** a planned, safety-related power shutoff LPEA may use during dangerous fire-weather conditions to reduce wildfire ignition risk. See [LPEA PSPS guidance](https://lpea.coop/psps) and the [LPEA outage center](https://lpea.coop/outage-center); if power is out, also check the [LPEA outage map](https://outage.lpea.coop).
- Overall: **LIKELY** - PSPS likelihood is high on weather-driven red-flag days; prepare for possible LPEA safety-related interruption behavior.
- Likely PSPS watch dates: Mon, Jun 15; Tue, Jun 16; Wed, Jun 17; Thu, Jun 18; Fri, Jun 19; Sat, Jun 20
- PSPS watch dates: Sun, Jun 14
- LPEA signal basis: LPEA active/update source contains red-flag, wildfire, or power-interruption language.
- Note: This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

| Date | PSPS likelihood | Driver locations | Weather basis |
| --- | --- | --- | --- |
| Sun, Jun 14 | WATCH | Durango / La Plata County (ELEVATED 26/100); Arboles / southwest county (ELEVATED 20/100); Bayfield / east La Plata County (ELEVATED 20/100) | Top weather score 26/100 at Durango / La Plata County. Weather score 26/100: RH 22%, wind/gust 23 mph, red-flag hours 0, near-threshold hours 0. |
| Mon, Jun 15 | LIKELY | Durango / La Plata County (LIKELY 75/100); Ignacio / southeast La Plata County (LIKELY 67/100); Arboles / southwest county (WATCH 61/100); Bayfield / east La Plata County (WATCH 61/100) | Top weather score 75/100 at Durango / La Plata County. Weather score 75/100: RH 12%, wind/gust 28 mph, red-flag hours 4, near-threshold hours 6. |
| Tue, Jun 16 | LIKELY | Durango / La Plata County (LIKELY 80/100); Ignacio / southeast La Plata County (LIKELY 80/100); Bayfield / east La Plata County (LIKELY 77/100); Arboles / southwest county (LIKELY 74/100) | Top weather score 80/100 at Durango / La Plata County. Weather score 80/100: RH 8%, wind/gust 32 mph, red-flag hours 8, near-threshold hours 10. |
| Wed, Jun 17 | LIKELY | Durango / La Plata County (LIKELY 81/100); Ignacio / southeast La Plata County (LIKELY 81/100); Arboles / southwest county (LIKELY 80/100); Bayfield / east La Plata County (LIKELY 77/100) | Top weather score 81/100 at Durango / La Plata County. Weather score 81/100: RH 9%, wind/gust 36 mph, red-flag hours 9, near-threshold hours 11. |
| Thu, Jun 18 | LIKELY | Arboles / southwest county (LIKELY 74/100); Durango / La Plata County (LIKELY 74/100); Ignacio / southeast La Plata County (LIKELY 74/100); Bayfield / east La Plata County (LIKELY 71/100) | Top weather score 74/100 at Arboles / southwest county. Weather score 74/100: RH 8%, wind/gust 26 mph, red-flag hours 5, near-threshold hours 8. |
| Fri, Jun 19 | LIKELY | Bayfield / east La Plata County (LIKELY 67/100); Ignacio / southeast La Plata County (LIKELY 67/100); Arboles / southwest county (WATCH 52/100); Chimney Rock / west county (WATCH 52/100) | Top weather score 67/100 at Bayfield / east La Plata County. Weather score 67/100: RH 12%, wind/gust 28 mph, red-flag hours 3, near-threshold hours 6. |
| Sat, Jun 20 | LIKELY | Durango / La Plata County (LIKELY 77/100); Bayfield / east La Plata County (LIKELY 77/100); Ignacio / southeast La Plata County (LIKELY 77/100); Arboles / southwest county (LIKELY 71/100) | Top weather score 77/100 at Durango / La Plata County. Weather score 77/100: RH 11%, wind/gust 33 mph, red-flag hours 7, near-threshold hours 10. |

## Area-Specific Outlook

| Area | Today | Peak this run | Highest-risk window |
| --- | --- | --- | --- |
| Durango | ELEVATED 26/100 | Wed, Jun 17: LIKELY 81/100 | 11 AM-9 PM local; 11 near/red-flag threshold hours. |
| Ignacio | ELEVATED 20/100 | Wed, Jun 17: LIKELY 81/100 | 11 AM-9 PM local; 11 near/red-flag threshold hours. |
| Arboles | ELEVATED 20/100 | Wed, Jun 17: LIKELY 80/100 | 12 PM-9 PM local; 10 near/red-flag threshold hours. |
| Bayfield | ELEVATED 20/100 | Tue, Jun 16: LIKELY 77/100 | 12 PM-9 PM local; 10 near/red-flag threshold hours. |
| Chimney Rock | LOW 12/100 | Tue, Jun 16: LIKELY 74/100 | 12 PM-9 PM local; 10 near/red-flag threshold hours. |
| Pagosa Springs | LOW 12/100 | Wed, Jun 17: LIKELY 71/100 | 1 PM-7 PM local; 7 near/red-flag threshold hours. |
| Chromo | LOW 12/100 | Wed, Jun 17: LIKELY 71/100 | 12 PM-7 PM local; 8 near/red-flag threshold hours. |
| Piedra | LOW 12/100 | Wed, Jun 17: WATCH 63/100 | 1 PM-7 PM local; 7 near/red-flag threshold hours. |

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
- WATCH/LIKELY false-watch past days: 16
- Pending WATCH/LIKELY dates in current forecast: Sun, Jun 14; Mon, Jun 15; Tue, Jun 16; Wed, Jun 17; Thu, Jun 18; Fri, Jun 19; Sat, Jun 20
- Calibration source: manual PSPS event log plus forecast history from prior monitor runs.

### Red Flag / Fire Weather Calibration

- Summary: 6/6 official Red Flag / Fire Weather alert dates had a pre-alert HIGH monitor signal. Average lead time: 4.5 days.
- Official alert dates logged: 6
- Pre-alert HIGH hit rate: 100%
- Average lead time: 4.5 days
- HIGH false-watch past days: 7
- Pending HIGH dates in current forecast: Mon, Jun 15; Tue, Jun 16; Wed, Jun 17; Thu, Jun 18; Fri, Jun 19; Sat, Jun 20
- Calibration source: official NWS Red Flag / Fire Weather alert dates plus forecast history from prior monitor runs.

## Official Weather Alerts

- Monitored NWS zones: COC007, COC067, COZ019, COZ022, COZ023, COZ295
- No active official NWS Red Flag / Fire Weather or related weather alerts found for monitored zones.

## LPEA Power Signal

- Status: `active_keyword_match` - LPEA active/update sources contained power-interruption keywords; review source before treating as confirmed outage intent.
- Meaning: Active source match means a monitored LPEA active/update source currently contains fire, outage, PSPS, or power-interruption keywords. Operational outages are shown separately and are not treated as PSPS/fire evidence unless the source text says so.
- Operational outage context: No monitored active LPEA source currently describes a non-PSPS outage.
- Source coverage: 13 sources; 5/5 official social sources reachable
- Evidence quality: 0 operational, 3 active/update, 1 archive/context, 4 reference source matches.
- Active/update source pages with matches: LPEA homepage (red flag, public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation); LPEA latest news (red flag, public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation); LPEA news releases (red flag, wildfire, public safety power shutoff, power shutoff, shutoff, power outage); LPEA LinkedIn (wildfire, public safety power shutoff, power shutoff, shutoff)
- Distinct active/update signals: Shared signal across 3 sources across 3 sources: LPEA homepage, LPEA latest news, and LPEA news releases (red flag, public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation); News-release archive PSPS item (red flag, wildfire, public safety power shutoff, power shutoff, shutoff, power outage); LPEA LinkedIn (wildfire, public safety power shutoff, power shutoff, shutoff); LinkedIn PSPS explainer post (wildfire, public safety power shutoff, power shutoff, shutoff)
- Example signal: ...tings & Resources Board Committees Voting Districts Policies & Bylaws Elections Red Flag Warnings are in effect across our service territory for Friday, June 12. Learn what Red Flag Warnings mean for your pow...
- Reference/context hits: [LPEA outage center](https://lpea.coop/outage-center); [LPEA wildfire / public safety power shutoffs](https://lpea.coop/psps); [LPEA red flag outage impact page](https://lpea.coop/outages/red-flag-warnings-and-impact-outages-prioritizing-safety-our-members); [LPEA fire mitigation](https://lpea.coop/fire-mitigation)

**Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## Next 7 Days

| Date | Tier | Main reason | Worst sampled metrics |
| --- | --- | --- | --- |
| Sun, Jun 14 | ELEVATED | Pagosa Springs: Elevated ingredient present: thunder probability reaches 40%. | Pagosa Springs: RH 31%, wind/gust 18 mph, thunder 40%<br>Arboles / southwest county: RH 25%, wind/gust 21 mph, thunder 28%<br>Chimney Rock / west county: RH 24%, wind/gust 20 mph, thunder 33% |
| Mon, Jun 15 | HIGH | Durango / La Plata County: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 16%, wind/gust 20 mph, thunder 31%<br>Arboles / southwest county: RH 13%, wind/gust 25 mph, thunder 25%<br>Chimney Rock / west county: RH 12%, wind/gust 23 mph, thunder 18% |
| Tue, Jun 16 | HIGH | Arboles / southwest county: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 10%, wind/gust 24 mph, thunder 0%<br>Arboles / southwest county: RH 7%, wind/gust 30 mph, thunder 0%<br>Chimney Rock / west county: RH 7%, wind/gust 26 mph, thunder 0% |
| Wed, Jun 17 | HIGH | Pagosa Springs: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 10%, wind/gust 28 mph, thunder 1%<br>Arboles / southwest county: RH 8%, wind/gust 32 mph, thunder 0%<br>Chimney Rock / west county: RH 8%, wind/gust 28 mph, thunder 0% |
| Thu, Jun 18 | HIGH | Arboles / southwest county: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 10%, wind/gust 21 mph, thunder 3%<br>Arboles / southwest county: RH 8%, wind/gust 26 mph, thunder 0%<br>Chimney Rock / west county: RH 7%, wind/gust 23 mph, thunder 1% |
| Fri, Jun 19 | HIGH | Bayfield / east La Plata County: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 14%, wind/gust 24 mph, thunder 8%<br>Arboles / southwest county: RH 11%, wind/gust 24 mph, thunder 8%<br>Chimney Rock / west county: RH 10%, wind/gust 23 mph, thunder 9% |
| Sat, Jun 20 | HIGH | Pagosa Springs: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 13%, wind/gust 30 mph, thunder 3%<br>Arboles / southwest county: RH 11%, wind/gust 30 mph, thunder 5%<br>Chimney Rock / west county: RH 9%, wind/gust 29 mph, thunder 4% |

## Sample Point Status

- Pagosa Springs: COZ295 (matches), forecast zone COZ023, county zone COC007
- Arboles / southwest county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Chimney Rock / west county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Piedra / north county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Chromo / southeast county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Durango / La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Bayfield / east La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Ignacio / southeast La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
