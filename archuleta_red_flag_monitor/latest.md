# Archuleta Red Flag Risk Monitor

Generated: Jul 1, 2026 at 5:39 PM MDT (Pagosa Springs, CO local time)
Next update: Jul 1, 2026 at 6:39 PM MDT (Pagosa Springs, CO local time)
Date/time basis: Pagosa Springs, CO local time (America/Denver)
> **Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## At A Glance

- Overall tier: **HIGH**
- PSPS likelihood: **LIKELY**
- PSPS likely dates: Wed, Jul 1; Fri, Jul 3
- PSPS watch dates: Thu, Jul 2; Sat, Jul 4; Sun, Jul 5; Mon, Jul 6; Tue, Jul 7
- Monitor heads-up recommended: **YES** - Send this monitor report because current risk is HIGH. This is not an official LPEA or NWS notice.
- HIGH dates: Wed, Jul 1; Fri, Jul 3
- CONCERN dates: Thu, Jul 2; Sat, Jul 4; Sun, Jul 5; Tue, Jul 7
- ELEVATED dates: Mon, Jul 6
- Official NWS Red Flag / Fire Weather alerts (COZ295): 1
- LPEA signal: `active_keyword_match` - LPEA active/update sources contained power-interruption keywords; review source before treating as confirmed outage intent.
- LPEA source coverage: 13 sources; 5/5 official social sources reachable
- NWS discussion: NWS discussion contains fire-weather concern language.

## Decision Support

- Summary: Highest LPEA PSPS concern is Wed, Jul 1 near Pagosa Springs (LIKELY 100/100), driven by red-flag wind/gust signal near 25 mph; very dry RH near 10%; 3 sampled hours are near red-flag thresholds.
- Confidence: **MEDIUM** (69/100) - 8/8 sampled weather points available; 7/7 fire-posture sources reachable; official NWS alert zones checked; 13/13 LPEA public sources reachable; LPEA active/update sources checked; active LPEA operational outage context checked separately from PSPS scoring; forecast changed substantially versus prior run; no confirmed PSPS events logged yet for calibration
- Fire danger peak: Wed, Jul 1: Arboles / southwest county EXTREME 100/100
- Red Flag likelihood peak: Wed, Jul 1: Arboles / southwest county LIKELY 89/100
- LPEA PSPS peak: Wed, Jul 1: Pagosa Springs LIKELY 100/100
- Method: rules-based decision support using public weather, fire-posture, and LPEA source signals; scores are screening estimates, not official or statistically calibrated probabilities.

| Date | Fire danger | Red Flag likelihood | LPEA PSPS | Main window |
| --- | --- | --- | --- | --- |
| Wed, Jul 1 | Arboles / southwest county: EXTREME 100/100 | Arboles / southwest county: LIKELY 89/100 | Pagosa Springs: LIKELY 100/100 | 5 PM-7 PM local; 3 near/red-flag threshold hours. |
| Thu, Jul 2 | Pagosa Springs: EXTREME 93/100 | Pagosa Springs: LIKELY 76/100 | Pagosa Springs: LIKELY 85/100 | 12 PM-7 PM local; 8 near/red-flag threshold hours. |
| Fri, Jul 3 | Durango / La Plata County: EXTREME 98/100 | Durango / La Plata County: LIKELY 84/100 | Durango / La Plata County: LIKELY 100/100 | 1 PM-6 PM local; 6 near/red-flag threshold hours. |
| Sat, Jul 4 | Durango / La Plata County: EXTREME 89/100 | Durango / La Plata County: WATCH 69/100 | Durango / La Plata County: LIKELY 79/100 | 2 PM-6 PM local; 5 near/red-flag threshold hours. |
| Sun, Jul 5 | Arboles / southwest county: EXTREME 86/100 | Arboles / southwest county: WATCH 63/100 | Arboles / southwest county: LIKELY 75/100 | 4 PM-6 PM local; 3 near/red-flag threshold hours. |
| Mon, Jul 6 | Pagosa Springs: HIGH 56/100 | Chimney Rock / west county: LOW 25/100 | Chimney Rock / west county: WATCH 50/100 | Peak ingredients near 4 PM local; RH 12%, wind 17 mph. |
| Tue, Jul 7 | Durango / La Plata County: EXTREME 92/100 | Durango / La Plata County: WATCH 60/100 | Arboles / southwest county: LIKELY 72/100 | 4 PM-5 PM local; 2 near/red-flag threshold hours. |

## Trend Intelligence

- Summary: Momentum is easing versus the prior run (Jul 1 at 5:32 AM MDT); forecast volatility is high and first WATCH-or-higher date is Wed, Jul 1.
- Momentum: **Easing**
- Forecast volatility: **HIGH** (61/100)
- First WATCH-or-higher PSPS date: Wed, Jul 1
- Watch-date movement: First WATCH-or-higher PSPS date remains Wed, Jul 1.
- Method: compares current forecast evidence against prior local forecast history.

Notable changes:
- First WATCH-or-higher PSPS date remains Wed, Jul 1.
- Thu, Jul 2: easing vs prior run; PSPS LIKELY -> WATCH; score -34, wind -2 mph, RH 0%, red-flag hours -4.
- Sat, Jul 4: easing vs prior run; PSPS LIKELY -> WATCH; score -15, wind -2 mph, RH 0%, red-flag hours -3.
- Wed, Jul 1: easing vs prior run; PSPS LIKELY -> LIKELY; score -14, wind 0 mph, RH 0%, red-flag hours -4. Driver shifted to Arboles / southwest county.

## Public Analysis Export

- Summary: Highest LPEA PSPS concern is Wed, Jul 1 near Pagosa Springs (LIKELY 100/100), driven by red-flag wind/gust signal near 25 mph; very dry RH near 10%; 3 sampled hours are near red-flag thresholds.
- Trend: Momentum is easing versus the prior run (Jul 1 at 5:32 AM MDT); forecast volatility is high and first WATCH-or-higher date is Wed, Jul 1.
- Confidence: **MEDIUM** (69/100)
- First WATCH-or-higher PSPS date: Wed, Jul 1
- PSPS peak: Wed, Jul 1 near Pagosa Springs at LIKELY 100/100
- Red Flag peak: Wed, Jul 1 near Arboles / southwest county at LIKELY 89/100
- Fire danger peak: Wed, Jul 1 near Arboles / southwest county at EXTREME 100/100
- LPEA operational outage context: LPEA service territory. Source text includes fire/PSPS language.
- Public JSON: `archuleta_red_flag_monitor/public_analysis_export.json`

What changed:
- First WATCH-or-higher PSPS date remains Wed, Jul 1.
- Thu, Jul 2: easing vs prior run; PSPS LIKELY -> WATCH; score -34, wind -2 mph, RH 0%, red-flag hours -4.
- Sat, Jul 4: easing vs prior run; PSPS LIKELY -> WATCH; score -15, wind -2 mph, RH 0%, red-flag hours -3.
- Wed, Jul 1: easing vs prior run; PSPS LIKELY -> LIKELY; score -14, wind 0 mph, RH 0%, red-flag hours -4. Driver shifted to Arboles / southwest county.

What to watch next:
- Check whether the largest day-level changes line up with wind/RH movement or public-source context.
- Check whether the LPEA active match is still a broad red-flag banner rather than direct PSPS/outage intent.
- Watch whether the highest-risk locations remain consistent across runs or the driver area is moving.
- If a PSPS occurs, log the confirmed date, location, and source so future hit-rate scoring can improve.

## PSPS Likelihood

- **PSPS means Public Safety Power Shutoff:** a planned, safety-related power shutoff LPEA may use during dangerous fire-weather conditions to reduce wildfire ignition risk. See [LPEA PSPS guidance](https://lpea.coop/psps) and the [LPEA outage center](https://lpea.coop/outage-center); if power is out, also check the [LPEA outage map](https://outage.lpea.coop).
- Overall: **LIKELY** - PSPS likelihood is high on weather-driven red-flag days; prepare for possible LPEA safety-related interruption behavior.
- Likely PSPS watch dates: Wed, Jul 1; Fri, Jul 3
- PSPS watch dates: Thu, Jul 2; Sat, Jul 4; Sun, Jul 5; Mon, Jul 6; Tue, Jul 7
- LPEA signal basis: LPEA active/update source contains red-flag, wildfire, or power-interruption language.
- Note: This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

| Date | PSPS likelihood | Driver locations | Weather basis |
| --- | --- | --- | --- |
| Wed, Jul 1 | LIKELY | Arboles / southwest county (LIKELY 75/100); Bayfield / east La Plata County (LIKELY 75/100); Ignacio / southeast La Plata County (LIKELY 75/100); Pagosa Springs (LIKELY 72/100) | Top weather score 75/100 at Arboles / southwest county. Weather score 75/100: RH 7%, wind/gust 25 mph, red-flag hours 2, near-threshold hours 3. |
| Thu, Jul 2 | WATCH | Pagosa Springs (WATCH 55/100); Arboles / southwest county (WATCH 55/100); Chimney Rock / west county (WATCH 55/100); Chromo / southeast county (WATCH 55/100) | Top weather score 55/100 at Pagosa Springs. Weather score 55/100: RH 7%, wind/gust 24 mph, red-flag hours 0, near-threshold hours 8. |
| Fri, Jul 3 | LIKELY | Durango / La Plata County (LIKELY 70/100); Pagosa Springs (WATCH 64/100); Bayfield / east La Plata County (WATCH 64/100); Arboles / southwest county (WATCH 55/100) | Top weather score 70/100 at Durango / La Plata County. Weather score 70/100: RH 7%, wind/gust 25 mph, red-flag hours 3, near-threshold hours 6. |
| Sat, Jul 4 | WATCH | Durango / La Plata County (WATCH 55/100); Ignacio / southeast La Plata County (WATCH 55/100); Bayfield / east La Plata County (WATCH 52/100); Arboles / southwest county (WATCH 51/100) | Top weather score 55/100 at Durango / La Plata County. Weather score 55/100: RH 8%, wind/gust 22 mph, red-flag hours 0, near-threshold hours 5. |
| Sun, Jul 5 | WATCH | Arboles / southwest county (WATCH 51/100); Durango / La Plata County (WATCH 48/100); Bayfield / east La Plata County (WATCH 48/100); Ignacio / southeast La Plata County (WATCH 48/100) | Top weather score 51/100 at Arboles / southwest county. Weather score 51/100: RH 8%, wind/gust 22 mph, red-flag hours 0, near-threshold hours 3. |
| Mon, Jul 6 | WATCH | Chimney Rock / west county (ELEVATED 30/100); Pagosa Springs (ELEVATED 26/100); Arboles / southwest county (ELEVATED 26/100) | Top weather score 30/100 at Chimney Rock / west county. Weather score 30/100: RH 12%, wind/gust 17 mph, red-flag hours 0, near-threshold hours 0. |
| Tue, Jul 7 | WATCH | Arboles / southwest county (WATCH 48/100); Durango / La Plata County (WATCH 48/100) | Top weather score 48/100 at Arboles / southwest county. Weather score 48/100: RH 15%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 2. |

## Area-Specific Outlook

| Area | Today | Peak this run | Highest-risk window |
| --- | --- | --- | --- |
| Arboles | LIKELY 75/100 | Wed, Jul 1: LIKELY 75/100 | 5 PM-7 PM local; 3 near/red-flag threshold hours. |
| Bayfield | LIKELY 75/100 | Wed, Jul 1: LIKELY 75/100 | 5 PM-7 PM local; 3 near/red-flag threshold hours. |
| Ignacio | LIKELY 75/100 | Wed, Jul 1: LIKELY 75/100 | 5 PM-7 PM local; 3 near/red-flag threshold hours. |
| Pagosa Springs | LIKELY 72/100 | Wed, Jul 1: LIKELY 72/100 | 5 PM-7 PM local; 3 near/red-flag threshold hours. |
| Piedra | LIKELY 72/100 | Wed, Jul 1: LIKELY 72/100 | 5 PM-7 PM local; 3 near/red-flag threshold hours. |
| Durango | LIKELY 66/100 | Fri, Jul 3: LIKELY 70/100 | 1 PM-6 PM local; 6 near/red-flag threshold hours. |
| Chimney Rock | LIKELY 66/100 | Wed, Jul 1: LIKELY 66/100 | 5 PM-7 PM local; 3 near/red-flag threshold hours. |
| Chromo | WATCH 63/100 | Wed, Jul 1: WATCH 63/100 | 5 PM-6 PM local; 2 near/red-flag threshold hours. |

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
| San Juan National Forest | STAGE 1 | EXTREME | [San Juan National Forest fire](https://www.fs.usda.gov/r02/sanjuan/fire) |
| BLM Tres Rios | STAGE 1 | UNKNOWN | [BLM Tres Rios Field Office](https://www.blm.gov/office/tres-rios-field-office) |
| La Plata County / Durango Fire | NONE | UNKNOWN | [Durango Fire & Rescue fire conditions](https://www.durangofire.org/fire-conditions) |
| Durango | STAGE 2 | UNKNOWN | [City of Durango](https://www.durangoco.gov/) |
| Southern Ute / Ignacio | STAGE 2 | UNKNOWN | [Southern Ute Indian Tribe](https://www.southernute-nsn.gov/) |

## Forecast Calibration

### PSPS Calibration

- Summary: No confirmed LPEA PSPS events logged yet; calibration will start once events are added.
- Confirmed PSPS events logged: 0
- Candidate/unconfirmed events logged: 0
- WATCH/LIKELY false-watch past days: 33
- Pending WATCH/LIKELY dates in current forecast: Wed, Jul 1; Thu, Jul 2; Fri, Jul 3; Sat, Jul 4; Sun, Jul 5; Mon, Jul 6; Tue, Jul 7
- Calibration source: manual PSPS event log plus forecast history from prior monitor runs.

### Red Flag / Fire Weather Calibration

- Summary: 21/21 official Red Flag / Fire Weather alert dates had a pre-alert HIGH monitor signal. Average lead time: 5.0 days.
- Official alert dates logged: 21
- Pre-alert HIGH hit rate: 100%
- Average lead time: 5.0 days
- HIGH false-watch past days: 11
- Pending HIGH dates in current forecast: Fri, Jul 3
- Calibration source: official NWS Red Flag / Fire Weather alert dates plus forecast history from prior monitor runs.

## Official Weather Alerts

- Monitored NWS zones: COC007, COC067, COZ019, COZ022, COZ023, COZ295
- [Red Flag Warning](https://api.weather.gov/alerts/urn:oid:2.49.0.1.840.0.92540b2495dec4198f3f12fcc6a4a8081697a9e8.001.2): Red Flag Warning issued July 1 at 12:34PM MDT until July 1 at 8:00PM MDT by NWS Grand Junction CO; 2026-07-01T12:34:00-06:00 to 2026-07-01T20:00:00-06:00; zones COZ295

## LPEA Power Signal

- Status: `active_keyword_match` - LPEA active/update sources contained power-interruption keywords; review source before treating as confirmed outage intent.
- Meaning: Active source match means a monitored LPEA active/update source currently contains fire, outage, PSPS, or power-interruption keywords. Operational outages are shown separately and are not treated as PSPS/fire evidence unless the source text says so.
- Operational outage context: LPEA service territory. Source text includes fire/PSPS language.
- Source coverage: 13 sources; 5/5 official social sources reachable
- Evidence quality: 0 operational, 5 active/update, 1 archive/context, 4 reference source matches.
- Operational outage source links: [LPEA homepage](https://lpea.coop); [LPEA latest news](https://lpea.coop/Posts); [LPEA news releases](https://lpea.coop/news-releases)
- Active/update source pages with matches: LPEA homepage (red flag, public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation); LPEA latest news (red flag, public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation); LPEA news releases (red flag, wildfire, public safety power shutoff, power shutoff, shutoff, power outage); LPEA LinkedIn (wildfire, public safety power shutoff, power shutoff, shutoff, fire mitigation)
- Distinct active/update signals: LPEA homepage (red flag, public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation); LPEA latest news (red flag, public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation); LPEA news releases (red flag, wildfire, public safety power shutoff, power shutoff, shutoff, power outage); News-release archive PSPS item (red flag, wildfire, public safety power shutoff, power shutoff, shutoff, power outage); LPEA LinkedIn (wildfire, public safety power shutoff, power shutoff, shutoff, fire mitigation)
- Example signal: ...on July 2 in observance of the July 4th holiday. We are currently experiencing Red Flag Conditions in our service territory. This may lead to more frequent prolonged outages. Learn more. Previous Next Red Fl...
- Reference/context hits: [LPEA outage center](https://lpea.coop/outage-center); [LPEA wildfire / public safety power shutoffs](https://lpea.coop/psps); [LPEA red flag outage impact page](https://lpea.coop/outages/red-flag-warnings-and-impact-outages-prioritizing-safety-our-members); [LPEA fire mitigation](https://lpea.coop/fire-mitigation)

**Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## Next 7 Days

| Date | Tier | Main reason | Worst sampled metrics |
| --- | --- | --- | --- |
| Wed, Jul 1 | HIGH | Active NWS Red Flag Warning or Fire Weather Watch touches this local date. | Pagosa Springs: RH 10%, wind/gust 25 mph, thunder 2%<br>Arboles / southwest county: RH 7%, wind/gust 25 mph, thunder 0%<br>Chimney Rock / west county: RH 7%, wind/gust 24 mph, thunder 0% |
| Thu, Jul 2 | CONCERN | Pagosa Springs: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Pagosa Springs: RH 7%, wind/gust 24 mph, thunder 0%<br>Arboles / southwest county: RH 5%, wind/gust 22 mph, thunder 0%<br>Chimney Rock / west county: RH 5%, wind/gust 22 mph, thunder 0% |
| Fri, Jul 3 | HIGH | Durango / La Plata County: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 7%, wind/gust 26 mph, thunder 0%<br>Arboles / southwest county: RH 5%, wind/gust 22 mph, thunder 0%<br>Chimney Rock / west county: RH 5%, wind/gust 23 mph, thunder 0% |
| Sat, Jul 4 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Pagosa Springs: RH 10%, wind/gust 21 mph, thunder 0%<br>Arboles / southwest county: RH 7%, wind/gust 22 mph, thunder 0%<br>Chimney Rock / west county: RH 6%, wind/gust 21 mph, thunder 0% |
| Sun, Jul 5 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Pagosa Springs: RH 11%, wind/gust 20 mph, thunder 3%<br>Arboles / southwest county: RH 8%, wind/gust 22 mph, thunder 4%<br>Chimney Rock / west county: RH 8%, wind/gust 20 mph, thunder 4% |
| Mon, Jul 6 | ELEVATED | Pagosa Springs: Elevated ingredient present: very low RH forecast near 15%. | Pagosa Springs: RH 15%, wind/gust 17 mph, thunder 10%<br>Arboles / southwest county: RH 13%, wind/gust 18 mph, thunder 7%<br>Chimney Rock / west county: RH 12%, wind/gust 17 mph, thunder 9% |
| Tue, Jul 7 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Pagosa Springs: RH 18%, wind/gust 17 mph, thunder 30%<br>Arboles / southwest county: RH 15%, wind/gust 21 mph, thunder 19%<br>Chimney Rock / west county: RH 14%, wind/gust 18 mph, thunder 22% |

## Sample Point Status

- Pagosa Springs: COZ295 (matches), forecast zone COZ023, county zone COC007
- Arboles / southwest county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Chimney Rock / west county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Piedra / north county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Chromo / southeast county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Durango / La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Bayfield / east La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Ignacio / southeast La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
