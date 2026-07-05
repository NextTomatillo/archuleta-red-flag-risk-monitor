# Archuleta Red Flag Risk Monitor

Generated: Jul 5, 2026 at 5:23 PM MDT (Pagosa Springs, CO local time)
Next update: Jul 5, 2026 at 6:23 PM MDT (Pagosa Springs, CO local time)
Date/time basis: Pagosa Springs, CO local time (America/Denver)
> **Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## At A Glance

- Overall tier: **HIGH**
- PSPS likelihood: **LIKELY**
- PSPS likely dates: Wed, Jul 8; Thu, Jul 9
- PSPS watch dates: Sun, Jul 5; Mon, Jul 6; Tue, Jul 7; Fri, Jul 10; Sat, Jul 11
- Monitor heads-up recommended: **YES** - Send this monitor report because current risk is HIGH. This is not an official LPEA or NWS notice.
- HIGH dates: Wed, Jul 8; Thu, Jul 9
- CONCERN dates: Tue, Jul 7; Fri, Jul 10
- ELEVATED dates: Sun, Jul 5; Mon, Jul 6; Sat, Jul 11
- Official NWS Red Flag / Fire Weather alerts (COZ295): 0
- LPEA signal: `active_keyword_match` - LPEA active/update sources contained power-interruption keywords; review source before treating as confirmed outage intent.
- LPEA source coverage: 13 sources; 5/5 official social sources reachable
- NWS discussion: NWS discussion contains fire-weather concern language.

## Decision Support

- Summary: Highest LPEA PSPS concern is Thu, Jul 9 near Arboles / southwest county (LIKELY 100/100), driven by red-flag wind/gust signal near 26 mph; very dry RH near 10%; 4 sampled hours meet red-flag screen.
- Confidence: **MEDIUM** (74/100) - 8/8 sampled weather points available; 7/7 fire-posture sources reachable; official NWS alert zones checked; 13/13 LPEA public sources reachable; LPEA active/update sources checked; active LPEA operational outage context checked separately from PSPS scoring; forecast changed moderately versus prior run; no confirmed PSPS events logged yet for calibration
- Fire danger peak: Thu, Jul 9: Bayfield / east La Plata County EXTREME 100/100
- Red Flag likelihood peak: Thu, Jul 9: Bayfield / east La Plata County LIKELY 92/100
- LPEA PSPS peak: Thu, Jul 9: Arboles / southwest county LIKELY 100/100
- Method: rules-based decision support using public weather, fire-posture, and LPEA source signals; scores are screening estimates, not official or statistically calibrated probabilities.

| Date | Fire danger | Red Flag likelihood | LPEA PSPS | Main window |
| --- | --- | --- | --- | --- |
| Sun, Jul 5 | Durango / La Plata County: HIGH 66/100 | Durango / La Plata County: POSSIBLE 30/100 | Durango / La Plata County: WATCH 61/100 | 5 PM-5 PM local; 1 near/red-flag threshold hour. |
| Mon, Jul 6 | Pagosa Springs: HIGH 56/100 | Pagosa Springs: LOW 25/100 | Pagosa Springs: WATCH 46/100 | Peak ingredients near 4 PM local; RH 15%, wind 16 mph. |
| Tue, Jul 7 | Arboles / southwest county: VERY HIGH 72/100 | Arboles / southwest county: POSSIBLE 50/100 | Arboles / southwest county: WATCH 62/100 | 3 PM-4 PM local; 2 near/red-flag threshold hours. |
| Wed, Jul 8 | Ignacio / southeast La Plata County: EXTREME 95/100 | Ignacio / southeast La Plata County: LIKELY 80/100 | Ignacio / southeast La Plata County: LIKELY 97/100 | 2 PM-7 PM local; 6 near/red-flag threshold hours. |
| Thu, Jul 9 | Bayfield / east La Plata County: EXTREME 100/100 | Bayfield / east La Plata County: LIKELY 92/100 | Arboles / southwest county: LIKELY 100/100 | 1 PM-7 PM local; 7 near/red-flag threshold hours. |
| Fri, Jul 10 | Durango / La Plata County: EXTREME 87/100 | Durango / La Plata County: WATCH 65/100 | Arboles / southwest county: LIKELY 76/100 | 3 PM-6 PM local; 4 near/red-flag threshold hours. |
| Sat, Jul 11 | Pagosa Springs: HIGH 56/100 | Arboles / southwest county: LOW 25/100 | Arboles / southwest county: WATCH 50/100 | Peak ingredients near 4 PM local; RH 11%, wind 16 mph. |

## Trend Intelligence

- Summary: Momentum is easing versus the prior run (Jul 5 at 5:30 AM MDT); forecast volatility is medium and first WATCH-or-higher date is Wed, Jul 8.
- Momentum: **Easing**
- Forecast volatility: **MEDIUM** (24/100)
- First WATCH-or-higher PSPS date: Wed, Jul 8
- Watch-date movement: First WATCH-or-higher PSPS date moved later from Sun, Jul 5 to Wed, Jul 8.
- Method: compares current forecast evidence against prior local forecast history.

Notable changes:
- First WATCH-or-higher PSPS date moved later from Sun, Jul 5 to Wed, Jul 8.
- Sun, Jul 5: easing vs prior run; PSPS WATCH -> ELEVATED; score -7, wind 0 mph, RH 0%, red-flag hours 0.

## Public Analysis Export

- Summary: Highest LPEA PSPS concern is Thu, Jul 9 near Arboles / southwest county (LIKELY 100/100), driven by red-flag wind/gust signal near 26 mph; very dry RH near 10%; 4 sampled hours meet red-flag screen.
- Trend: Momentum is easing versus the prior run (Jul 5 at 5:30 AM MDT); forecast volatility is medium and first WATCH-or-higher date is Wed, Jul 8.
- Confidence: **MEDIUM** (74/100)
- First WATCH-or-higher PSPS date: Wed, Jul 8
- PSPS peak: Thu, Jul 9 near Arboles / southwest county at LIKELY 100/100
- Red Flag peak: Thu, Jul 9 near Bayfield / east La Plata County at LIKELY 92/100
- Fire danger peak: Thu, Jul 9 near Bayfield / east La Plata County at EXTREME 100/100
- LPEA operational outage context: LPEA service territory. Source text includes fire/PSPS language.
- Public JSON: `archuleta_red_flag_monitor/public_analysis_export.json`

What changed:
- First WATCH-or-higher PSPS date moved later from Sun, Jul 5 to Wed, Jul 8.
- Sun, Jul 5: easing vs prior run; PSPS WATCH -> ELEVATED; score -7, wind 0 mph, RH 0%, red-flag hours 0.

What to watch next:
- Check whether the largest day-level changes line up with wind/RH movement or public-source context.
- Check whether the LPEA active match is still a broad red-flag banner rather than direct PSPS/outage intent.
- Watch whether the highest-risk locations remain consistent across runs or the driver area is moving.
- If a PSPS occurs, log the confirmed date, location, and source so future hit-rate scoring can improve.

## PSPS Likelihood

- **PSPS means Public Safety Power Shutoff:** a planned, safety-related power shutoff LPEA may use during dangerous fire-weather conditions to reduce wildfire ignition risk. See [LPEA PSPS guidance](https://lpea.coop/psps) and the [LPEA outage center](https://lpea.coop/outage-center); if power is out, also check the [LPEA outage map](https://outage.lpea.coop).
- Overall: **LIKELY** - PSPS likelihood is high on weather-driven red-flag days; prepare for possible LPEA safety-related interruption behavior.
- Likely PSPS watch dates: Wed, Jul 8; Thu, Jul 9
- PSPS watch dates: Sun, Jul 5; Mon, Jul 6; Tue, Jul 7; Fri, Jul 10; Sat, Jul 11
- LPEA signal basis: LPEA active/update source contains red-flag, wildfire, or power-interruption language.
- Note: This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

| Date | PSPS likelihood | Driver locations | Weather basis |
| --- | --- | --- | --- |
| Sun, Jul 5 | WATCH | Durango / La Plata County (ELEVATED 41/100); Bayfield / east La Plata County (ELEVATED 41/100); Arboles / southwest county (ELEVATED 33/100) | Top weather score 41/100 at Durango / La Plata County. Weather score 41/100: RH 8%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 1. |
| Mon, Jul 6 | WATCH | Pagosa Springs (ELEVATED 26/100); Arboles / southwest county (ELEVATED 26/100); Chimney Rock / west county (ELEVATED 26/100) | Top weather score 26/100 at Pagosa Springs. Weather score 26/100: RH 14%, wind/gust 16 mph, red-flag hours 0, near-threshold hours 0. |
| Tue, Jul 7 | WATCH | Arboles / southwest county (ELEVATED 38/100); Durango / La Plata County (ELEVATED 38/100); Ignacio / southeast La Plata County (ELEVATED 28/100) | Top weather score 38/100 at Arboles / southwest county. Weather score 38/100: RH 18%, wind/gust 22 mph, red-flag hours 0, near-threshold hours 2. |
| Wed, Jul 8 | LIKELY | Ignacio / southeast La Plata County (LIKELY 67/100); Durango / La Plata County (WATCH 57/100); Arboles / southwest county (WATCH 48/100); Bayfield / east La Plata County (WATCH 48/100) | Top weather score 67/100 at Ignacio / southeast La Plata County. Weather score 67/100: RH 14%, wind/gust 26 mph, red-flag hours 4, near-threshold hours 6. |
| Thu, Jul 9 | LIKELY | Arboles / southwest county (LIKELY 71/100); Durango / La Plata County (LIKELY 71/100); Bayfield / east La Plata County (LIKELY 71/100); Ignacio / southeast La Plata County (LIKELY 71/100) | Top weather score 71/100 at Arboles / southwest county. Weather score 71/100: RH 10%, wind/gust 26 mph, red-flag hours 4, near-threshold hours 7. |
| Fri, Jul 10 | WATCH | Arboles / southwest county (WATCH 52/100); Durango / La Plata County (WATCH 52/100); Bayfield / east La Plata County (WATCH 52/100); Ignacio / southeast La Plata County (WATCH 52/100) | Top weather score 52/100 at Arboles / southwest county. Weather score 52/100: RH 10%, wind/gust 22 mph, red-flag hours 0, near-threshold hours 4. |
| Sat, Jul 11 | WATCH | Arboles / southwest county (ELEVATED 30/100); Chimney Rock / west county (ELEVATED 30/100); Durango / La Plata County (ELEVATED 30/100) | Top weather score 30/100 at Arboles / southwest county. Weather score 30/100: RH 11%, wind/gust 16 mph, red-flag hours 0, near-threshold hours 0. |

## Area-Specific Outlook

| Area | Today | Peak this run | Highest-risk window |
| --- | --- | --- | --- |
| Arboles | ELEVATED 33/100 | Thu, Jul 9: LIKELY 71/100 | 1 PM-7 PM local; 7 near/red-flag threshold hours. |
| Durango | ELEVATED 41/100 | Thu, Jul 9: LIKELY 71/100 | 1 PM-9 PM local; 9 near/red-flag threshold hours. |
| Bayfield | ELEVATED 41/100 | Thu, Jul 9: LIKELY 71/100 | 1 PM-9 PM local; 9 near/red-flag threshold hours. |
| Ignacio | ELEVATED 33/100 | Thu, Jul 9: LIKELY 71/100 | 1 PM-8 PM local; 8 near/red-flag threshold hours. |
| Pagosa Springs | ELEVATED 30/100 | Thu, Jul 9: WATCH 57/100 | 2 PM-7 PM local; 6 near/red-flag threshold hours. |
| Chimney Rock | ELEVATED 33/100 | Thu, Jul 9: WATCH 52/100 | 2 PM-7 PM local; 6 near/red-flag threshold hours. |
| Chromo | ELEVATED 22/100 | Thu, Jul 9: WATCH 48/100 | 2 PM-6 PM local; 5 near/red-flag threshold hours. |
| Piedra | ELEVATED 30/100 | Thu, Jul 9: WATCH 47/100 | 4 PM-6 PM local; 3 near/red-flag threshold hours. |

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
- WATCH/LIKELY false-watch past days: 37
- Pending WATCH/LIKELY dates in current forecast: Sun, Jul 5; Mon, Jul 6; Tue, Jul 7; Wed, Jul 8; Thu, Jul 9; Fri, Jul 10; Sat, Jul 11
- Calibration source: manual PSPS event log plus forecast history from prior monitor runs.

### Red Flag / Fire Weather Calibration

- Summary: 21/21 official Red Flag / Fire Weather alert dates had a pre-alert HIGH monitor signal. Average lead time: 5.0 days.
- Official alert dates logged: 21
- Pre-alert HIGH hit rate: 100%
- Average lead time: 5.0 days
- HIGH false-watch past days: 13
- Pending HIGH dates in current forecast: Wed, Jul 8; Thu, Jul 9
- Calibration source: official NWS Red Flag / Fire Weather alert dates plus forecast history from prior monitor runs.

## Official Weather Alerts

- Monitored NWS zones: COC007, COC067, COZ019, COZ022, COZ023, COZ295
- [Air Quality Alert](https://api.weather.gov/alerts/urn:oid:2.49.0.1.840.0.991cdcf49a9be90f949e8c2b1c836e3aef746784.001.1): Air Quality Alert issued July 5 at 4:10PM MDT by NWS Grand Junction CO; 2026-07-05T16:10:00-06:00 to 2026-07-06T09:00:00-06:00; zones COC029, COC033, COC051, COC053, COC067, COC083, COC085, COC091, COC111, COC113
- [Air Quality Alert](https://api.weather.gov/alerts/urn:oid:2.49.0.1.840.0.983b3822f4f9529d2c6e2fc3a8f18f9786cdb232.001.1): Air Quality Alert issued July 5 at 9:10AM MDT by NWS Grand Junction CO; 2026-07-05T09:10:00-06:00 to 2026-07-06T09:00:00-06:00; zones COC029, COC033, COC051, COC053, COC067, COC083, COC085, COC091, COC111, COC113

## LPEA Power Signal

- Status: `active_keyword_match` - LPEA active/update sources contained power-interruption keywords; review source before treating as confirmed outage intent.
- Meaning: Active source match means a monitored LPEA active/update source currently contains fire, outage, PSPS, or power-interruption keywords. Operational outages are shown separately and are not treated as PSPS/fire evidence unless the source text says so.
- Operational outage context: LPEA service territory. Source text includes fire/PSPS language.
- Source coverage: 13 sources; 5/5 official social sources reachable
- Evidence quality: 0 operational, 5 active/update, 1 archive/context, 4 reference source matches.
- Operational outage source links: [LPEA homepage](https://lpea.coop); [LPEA latest news](https://lpea.coop/Posts); [LPEA news releases](https://lpea.coop/news-releases)
- Active/update source pages with matches: LPEA homepage (red flag, public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation); LPEA latest news (red flag, public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation); LPEA news releases (red flag, wildfire, public safety power shutoff, power shutoff, shutoff, power outage); LPEA LinkedIn (wildfire, public safety power shutoff, power shutoff, shutoff, fire mitigation)
- Distinct active/update signals: LPEA homepage (red flag, public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation); LPEA latest news (red flag, public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation); LPEA news releases (red flag, wildfire, public safety power shutoff, power shutoff, shutoff, power outage); News-release archive PSPS item (red flag, wildfire, public safety power shutoff, power shutoff, shutoff, power outage); LPEA LinkedIn (wildfire, public safety power shutoff, power shutoff, shutoff, fire mitigation)
- Example signal: ...on July 3 in observance of the July 4th holiday. We are currently experiencing Red Flag Conditions in our service territory. This may lead to more frequent prolonged outages. Learn more. Previous Next Red Fl...
- Reference/context hits: [LPEA outage center](https://lpea.coop/outage-center); [LPEA wildfire / public safety power shutoffs](https://lpea.coop/psps); [LPEA red flag outage impact page](https://lpea.coop/outages/red-flag-warnings-and-impact-outages-prioritizing-safety-our-members); [LPEA fire mitigation](https://lpea.coop/fire-mitigation)

**Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## Next 7 Days

| Date | Tier | Main reason | Worst sampled metrics |
| --- | --- | --- | --- |
| Sun, Jul 5 | ELEVATED | Pagosa Springs: Elevated ingredient present: very low RH forecast near 9%. | Pagosa Springs: RH 9%, wind/gust 16 mph, thunder 1%<br>Arboles / southwest county: RH 7%, wind/gust 17 mph, thunder 0%<br>Chimney Rock / west county: RH 7%, wind/gust 18 mph, thunder 1% |
| Mon, Jul 6 | ELEVATED | Pagosa Springs: Elevated ingredient present: very low RH forecast near 14%. | Pagosa Springs: RH 14%, wind/gust 16 mph, thunder 6%<br>Arboles / southwest county: RH 14%, wind/gust 17 mph, thunder 7%<br>Chimney Rock / west county: RH 13%, wind/gust 17 mph, thunder 5% |
| Tue, Jul 7 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Pagosa Springs: RH 21%, wind/gust 20 mph, thunder 22%<br>Arboles / southwest county: RH 18%, wind/gust 22 mph, thunder 4%<br>Piedra / north county: RH 28%, wind/gust 16 mph, thunder 31% |
| Wed, Jul 8 | HIGH | Ignacio / southeast La Plata County: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 18%, wind/gust 20 mph, thunder 17%<br>Arboles / southwest county: RH 14%, wind/gust 24 mph, thunder 2%<br>Chimney Rock / west county: RH 13%, wind/gust 22 mph, thunder 6% |
| Thu, Jul 9 | HIGH | Arboles / southwest county: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 14%, wind/gust 25 mph, thunder 5%<br>Arboles / southwest county: RH 10%, wind/gust 26 mph, thunder 5%<br>Chimney Rock / west county: RH 10%, wind/gust 24 mph, thunder 5% |
| Fri, Jul 10 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Pagosa Springs: RH 14%, wind/gust 25 mph, thunder 8%<br>Arboles / southwest county: RH 10%, wind/gust 22 mph, thunder 3%<br>Chimney Rock / west county: RH 10%, wind/gust 22 mph, thunder 5% |
| Sat, Jul 11 | ELEVATED | Pagosa Springs: Elevated ingredient present: very low RH forecast near 13%. | Pagosa Springs: RH 13%, wind/gust 18 mph, thunder 7%<br>Arboles / southwest county: RH 11%, wind/gust 16 mph, thunder 7%<br>Chimney Rock / west county: RH 10%, wind/gust 16 mph, thunder 6% |

## Sample Point Status

- Pagosa Springs: COZ295 (matches), forecast zone COZ023, county zone COC007
- Arboles / southwest county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Chimney Rock / west county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Piedra / north county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Chromo / southeast county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Durango / La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Bayfield / east La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Ignacio / southeast La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
