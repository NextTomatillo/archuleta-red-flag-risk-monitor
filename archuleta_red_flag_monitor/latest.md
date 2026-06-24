# Archuleta Red Flag Risk Monitor

Generated: Jun 24, 2026 at 3:22 PM MDT (Pagosa Springs, CO local time)
Next update: Jun 24, 2026 at 4:22 PM MDT (Pagosa Springs, CO local time)
Date/time basis: Pagosa Springs, CO local time (America/Denver)
> **Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## At A Glance

- Overall tier: **HIGH**
- PSPS likelihood: **LIKELY**
- PSPS likely dates: Wed, Jun 24; Fri, Jun 26; Sat, Jun 27; Sun, Jun 28; Mon, Jun 29; Tue, Jun 30
- PSPS watch dates: Thu, Jun 25
- Monitor heads-up recommended: **YES** - Send this monitor report because current risk is HIGH. This is not an official LPEA or NWS notice.
- HIGH dates: Wed, Jun 24; Thu, Jun 25; Fri, Jun 26; Sat, Jun 27; Sun, Jun 28; Mon, Jun 29; Tue, Jun 30
- CONCERN dates: None
- ELEVATED dates: None
- Official NWS Red Flag / Fire Weather alerts (COZ295): 1
- LPEA signal: `active_keyword_match` - LPEA active/update sources contained power-interruption keywords; review source before treating as confirmed outage intent.
- LPEA source coverage: 13 sources; 5/5 official social sources reachable
- NWS discussion: NWS discussion contains fire-weather concern language.

## Decision Support

- Summary: Highest LPEA PSPS concern is Wed, Jun 24 near Arboles / southwest county (LIKELY 100/100), driven by red-flag wind/gust signal near 29 mph; red-flag RH near 15%; 2 sampled hours are near red-flag thresholds.
- Confidence: **MEDIUM** (69/100) - 8/8 sampled weather points available; 7/7 fire-posture sources reachable; official NWS alert zones checked; 13/13 LPEA public sources reachable; LPEA active/update sources checked; active LPEA operational outage context checked separately from PSPS scoring; forecast changed substantially versus prior run; no confirmed PSPS events logged yet for calibration
- Fire danger peak: Sat, Jun 27: Pagosa Springs EXTREME 100/100
- Red Flag likelihood peak: Sat, Jun 27: Pagosa Springs LIKELY 100/100
- LPEA PSPS peak: Wed, Jun 24: Arboles / southwest county LIKELY 100/100
- Method: rules-based decision support using public weather, fire-posture, and LPEA source signals; scores are screening estimates, not official or statistically calibrated probabilities.

| Date | Fire danger | Red Flag likelihood | LPEA PSPS | Main window |
| --- | --- | --- | --- | --- |
| Wed, Jun 24 | Chimney Rock / west county: EXTREME 100/100 | Chimney Rock / west county: LIKELY 86/100 | Arboles / southwest county: LIKELY 100/100 | 3 PM-4 PM local; 2 near/red-flag threshold hours. |
| Thu, Jun 25 | Bayfield / east La Plata County: VERY HIGH 81/100 | Chimney Rock / west county: POSSIBLE 47/100 | Chimney Rock / west county: LIKELY 92/100 | 4 PM-4 PM local; 1 near/red-flag threshold hour. |
| Fri, Jun 26 | Chimney Rock / west county: EXTREME 97/100 | Chimney Rock / west county: LIKELY 80/100 | Chimney Rock / west county: LIKELY 100/100 | 3 PM-5 PM local; 3 near/red-flag threshold hours. |
| Sat, Jun 27 | Pagosa Springs: EXTREME 100/100 | Pagosa Springs: LIKELY 100/100 | Pagosa Springs: LIKELY 100/100 | 1 PM-7 PM local; 7 near/red-flag threshold hours. |
| Sun, Jun 28 | Arboles / southwest county: EXTREME 100/100 | Arboles / southwest county: LIKELY 100/100 | Arboles / southwest county: LIKELY 100/100 | 12 AM-10 PM local; 13 near/red-flag threshold hours. |
| Mon, Jun 29 | Arboles / southwest county: EXTREME 100/100 | Arboles / southwest county: LIKELY 96/100 | Arboles / southwest county: LIKELY 100/100 | 12 PM-7 PM local; 8 near/red-flag threshold hours. |
| Tue, Jun 30 | Durango / La Plata County: EXTREME 100/100 | Durango / La Plata County: LIKELY 88/100 | Durango / La Plata County: LIKELY 100/100 | 1 PM-7 PM local; 7 near/red-flag threshold hours. |

## Trend Intelligence

- Summary: Momentum is rising versus the prior run (Jun 23 at 3:22 PM MDT); forecast volatility is high and first WATCH-or-higher date is Wed, Jun 24.
- Momentum: **Rising**
- Forecast volatility: **HIGH** (53/100)
- First WATCH-or-higher PSPS date: Wed, Jun 24
- Watch-date movement: First WATCH-or-higher PSPS date moved later from Tue, Jun 23 to Wed, Jun 24.
- Method: compares current forecast evidence against prior local forecast history.

Notable changes:
- First WATCH-or-higher PSPS date moved later from Tue, Jun 23 to Wed, Jun 24.
- Thu, Jun 25: worsening vs prior run; PSPS ELEVATED -> WATCH; score +21, wind +1 mph, RH -2%, red-flag hours 0.
- Fri, Jun 26: worsening vs prior run; PSPS WATCH -> LIKELY; score +15, wind 0 mph, RH 0%, red-flag hours 0.
- Sat, Jun 27: worsening vs prior run; PSPS LIKELY -> LIKELY; score +15, wind -1 mph, RH -1%, red-flag hours 0.
- Wed, Jun 24: easing vs prior run; PSPS LIKELY -> LIKELY; score +5, wind 0 mph, RH +2%, red-flag hours -2. Driver shifted to Arboles / southwest county.

## Public Analysis Export

- Summary: Highest LPEA PSPS concern is Wed, Jun 24 near Arboles / southwest county (LIKELY 100/100), driven by red-flag wind/gust signal near 29 mph; red-flag RH near 15%; 2 sampled hours are near red-flag thresholds.
- Trend: Momentum is rising versus the prior run (Jun 23 at 3:22 PM MDT); forecast volatility is high and first WATCH-or-higher date is Wed, Jun 24.
- Confidence: **MEDIUM** (69/100)
- First WATCH-or-higher PSPS date: Wed, Jun 24
- PSPS peak: Wed, Jun 24 near Arboles / southwest county at LIKELY 100/100
- Red Flag peak: Sat, Jun 27 near Pagosa Springs at LIKELY 100/100
- Fire danger peak: Sat, Jun 27 near Pagosa Springs at EXTREME 100/100
- LPEA operational outage context: Edgemont area. Not classified as fire-weather or PSPS-related by this monitor.
- Public JSON: `archuleta_red_flag_monitor/public_analysis_export.json`

What changed:
- First WATCH-or-higher PSPS date moved later from Tue, Jun 23 to Wed, Jun 24.
- Thu, Jun 25: worsening vs prior run; PSPS ELEVATED -> WATCH; score +21, wind +1 mph, RH -2%, red-flag hours 0.
- Fri, Jun 26: worsening vs prior run; PSPS WATCH -> LIKELY; score +15, wind 0 mph, RH 0%, red-flag hours 0.
- Sat, Jun 27: worsening vs prior run; PSPS LIKELY -> LIKELY; score +15, wind -1 mph, RH -1%, red-flag hours 0.
- Wed, Jun 24: easing vs prior run; PSPS LIKELY -> LIKELY; score +5, wind 0 mph, RH +2%, red-flag hours -2. Driver shifted to Arboles / southwest county.

What to watch next:
- Check whether the largest day-level changes line up with wind/RH movement or public-source context.
- Check whether the LPEA active match is still a broad red-flag banner rather than direct PSPS/outage intent.
- Watch whether the highest-risk locations remain consistent across runs or the driver area is moving.
- If a PSPS occurs, log the confirmed date, location, and source so future hit-rate scoring can improve.

## PSPS Likelihood

- **PSPS means Public Safety Power Shutoff:** a planned, safety-related power shutoff LPEA may use during dangerous fire-weather conditions to reduce wildfire ignition risk. See [LPEA PSPS guidance](https://lpea.coop/psps) and the [LPEA outage center](https://lpea.coop/outage-center); if power is out, also check the [LPEA outage map](https://outage.lpea.coop).
- Overall: **LIKELY** - PSPS likelihood is high on weather-driven red-flag days; prepare for possible LPEA safety-related interruption behavior.
- Likely PSPS watch dates: Wed, Jun 24; Fri, Jun 26; Sat, Jun 27; Sun, Jun 28; Mon, Jun 29; Tue, Jun 30
- PSPS watch dates: Thu, Jun 25
- LPEA signal basis: LPEA active/update source contains red-flag, wildfire, or power-interruption language.
- Note: This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

| Date | PSPS likelihood | Driver locations | Weather basis |
| --- | --- | --- | --- |
| Wed, Jun 24 | LIKELY | Arboles / southwest county (LIKELY 72/100); Chimney Rock / west county (LIKELY 72/100); Ignacio / southeast La Plata County (LIKELY 72/100); Bayfield / east La Plata County (WATCH 62/100) | Top weather score 72/100 at Arboles / southwest county. Weather score 72/100: RH 15%, wind/gust 29 mph, red-flag hours 1, near-threshold hours 2. |
| Thu, Jun 25 | WATCH | Chimney Rock / west county (WATCH 56/100); Bayfield / east La Plata County (WATCH 56/100); Ignacio / southeast La Plata County (WATCH 56/100); Arboles / southwest county (WATCH 50/100) | Top weather score 56/100 at Chimney Rock / west county. Weather score 56/100: RH 18%, wind/gust 26 mph, red-flag hours 0, near-threshold hours 1. |
| Fri, Jun 26 | LIKELY | Chimney Rock / west county (LIKELY 66/100); Pagosa Springs (WATCH 56/100); Durango / La Plata County (WATCH 56/100); Bayfield / east La Plata County (WATCH 56/100) | Top weather score 66/100 at Chimney Rock / west county. Weather score 66/100: RH 17%, wind/gust 29 mph, red-flag hours 0, near-threshold hours 3. |
| Sat, Jun 27 | LIKELY | Arboles / southwest county (LIKELY 96/100); Chimney Rock / west county (LIKELY 96/100); Durango / La Plata County (LIKELY 96/100); Bayfield / east La Plata County (LIKELY 96/100) | Top weather score 96/100 at Arboles / southwest county. Weather score 96/100: RH 10%, wind/gust 41 mph, red-flag hours 11, near-threshold hours 13. |
| Sun, Jun 28 | LIKELY | Arboles / southwest county (LIKELY 81/100); Chimney Rock / west county (LIKELY 81/100); Ignacio / southeast La Plata County (LIKELY 81/100); Durango / La Plata County (LIKELY 77/100) | Top weather score 81/100 at Arboles / southwest county. Weather score 81/100: RH 11%, wind/gust 40 mph, red-flag hours 8, near-threshold hours 13. |
| Mon, Jun 29 | LIKELY | Arboles / southwest county (LIKELY 77/100); Ignacio / southeast La Plata County (LIKELY 77/100); Chimney Rock / west county (LIKELY 71/100); Durango / La Plata County (LIKELY 71/100) | Top weather score 77/100 at Arboles / southwest county. Weather score 77/100: RH 12%, wind/gust 33 mph, red-flag hours 6, near-threshold hours 8. |
| Tue, Jun 30 | LIKELY | Durango / La Plata County (LIKELY 71/100); Bayfield / east La Plata County (LIKELY 67/100); Ignacio / southeast La Plata County (LIKELY 67/100); Arboles / southwest county (WATCH 61/100) | Top weather score 71/100 at Durango / La Plata County. Weather score 71/100: RH 12%, wind/gust 28 mph, red-flag hours 5, near-threshold hours 7. |

## Area-Specific Outlook

| Area | Today | Peak this run | Highest-risk window |
| --- | --- | --- | --- |
| Arboles | LIKELY 72/100 | Sat, Jun 27: LIKELY 96/100 | 11 AM-11 PM local; 13 near/red-flag threshold hours. |
| Chimney Rock | LIKELY 72/100 | Sat, Jun 27: LIKELY 96/100 | 11 AM-11 PM local; 13 near/red-flag threshold hours. |
| Durango | WATCH 56/100 | Sat, Jun 27: LIKELY 96/100 | 12 PM-10 PM local; 11 near/red-flag threshold hours. |
| Bayfield | WATCH 62/100 | Sat, Jun 27: LIKELY 96/100 | 12 PM-10 PM local; 11 near/red-flag threshold hours. |
| Ignacio | LIKELY 72/100 | Sat, Jun 27: LIKELY 96/100 | 12 PM-10 PM local; 11 near/red-flag threshold hours. |
| Pagosa Springs | WATCH 56/100 | Sat, Jun 27: LIKELY 92/100 | 1 PM-7 PM local; 7 near/red-flag threshold hours. |
| Chromo | WATCH 50/100 | Sat, Jun 27: LIKELY 92/100 | 1 PM-7 PM local; 7 near/red-flag threshold hours. |
| Piedra | ELEVATED 41/100 | Sat, Jun 27: LIKELY 82/100 | 1 PM-9 PM local; 9 near/red-flag threshold hours. |

## Fire Posture + Restrictions

- Summary: 5 official sources indicate fire restrictions or staged restrictions.
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
| Durango | UNKNOWN | UNKNOWN | [City of Durango](https://www.durangoco.gov/) |
| Southern Ute / Ignacio | STAGE 2 | UNKNOWN | [Southern Ute Indian Tribe](https://www.southernute-nsn.gov/) |

## Forecast Calibration

### PSPS Calibration

- Summary: No confirmed LPEA PSPS events logged yet; calibration will start once events are added.
- Confirmed PSPS events logged: 0
- Candidate/unconfirmed events logged: 0
- WATCH/LIKELY false-watch past days: 26
- Pending WATCH/LIKELY dates in current forecast: Wed, Jun 24; Thu, Jun 25; Fri, Jun 26; Sat, Jun 27; Sun, Jun 28; Mon, Jun 29; Tue, Jun 30
- Calibration source: manual PSPS event log plus forecast history from prior monitor runs.

### Red Flag / Fire Weather Calibration

- Summary: 18/18 official Red Flag / Fire Weather alert dates had a pre-alert HIGH monitor signal. Average lead time: 4.9 days.
- Official alert dates logged: 18
- Pre-alert HIGH hit rate: 100%
- Average lead time: 4.9 days
- HIGH false-watch past days: 9
- Pending HIGH dates in current forecast: Sun, Jun 28; Mon, Jun 29; Tue, Jun 30
- Calibration source: official NWS Red Flag / Fire Weather alert dates plus forecast history from prior monitor runs.

## Official Weather Alerts

- Monitored NWS zones: COC007, COC067, COZ019, COZ022, COZ023, COZ295
- [Fire Weather Watch](https://api.weather.gov/alerts/urn:oid:2.49.0.1.840.0.e808d94489b27dbb6291525ecd1eafb58997d07c.004.1): Fire Weather Watch issued June 24 at 1:01PM MDT until June 28 at 12:00AM MDT by NWS Grand Junction CO; 2026-06-24T13:01:00-06:00 to 2026-06-28T00:00:00-06:00; zones COZ201, COZ205, COZ291, COZ292, COZ293, COZ294, COZ295
- [Air Quality Alert](https://api.weather.gov/alerts/urn:oid:2.49.0.1.840.0.29e749e5d1196f64bf6c88f21f880c8d31c8983b.001.1): Air Quality Alert issued June 24 at 9:10AM MDT by NWS Grand Junction CO; 2026-06-24T09:10:00-06:00 to 2026-06-25T09:00:00-06:00; zones COC029, COC033, COC037, COC045, COC051, COC053, COC067, COC077, COC083, COC085, COC091, COC097, COC103, COC111, COC113

## LPEA Power Signal

- Status: `active_keyword_match` - LPEA active/update sources contained power-interruption keywords; review source before treating as confirmed outage intent.
- Meaning: Active source match means a monitored LPEA active/update source currently contains fire, outage, PSPS, or power-interruption keywords. Operational outages are shown separately and are not treated as PSPS/fire evidence unless the source text says so.
- Operational outage context: Edgemont area. Not classified as fire-weather or PSPS-related by this monitor.
- Source coverage: 13 sources; 5/5 official social sources reachable
- Evidence quality: 0 operational, 3 active/update, 2 archive/context, 4 reference source matches.
- Operational outage source links: [LPEA homepage](https://lpea.coop); [LPEA latest news](https://lpea.coop/Posts); [LPEA news releases](https://lpea.coop/news-releases)
- Active/update source pages with matches: LPEA homepage (red flag, public safety power shutoff, power shutoff, shutoff, power outage, outage map); LPEA latest news (public safety power shutoff, power shutoff, shutoff, power outage, outage map, fire mitigation); LPEA news releases (red flag, wildfire, public safety power shutoff, power shutoff, shutoff, power outage); LPEA LinkedIn (wildfire, public safety power shutoff, power shutoff, shutoff)
- Distinct active/update signals: LPEA homepage (red flag, public safety power shutoff, power shutoff, shutoff, power outage, outage map); LPEA news releases (red flag, wildfire, public safety power shutoff, power shutoff, shutoff, power outage); News-release archive PSPS item (red flag, wildfire, public safety power shutoff, power shutoff, shutoff, power outage); LPEA LinkedIn (wildfire, public safety power shutoff, power shutoff, shutoff); LinkedIn PSPS explainer post (wildfire, public safety power shutoff, power shutoff, shutoff)
- Example signal: ...ort LPEA Prioritizes Safety this Fire Season with Proactive Planning Learn More Red Flag Conditions May Result in Longer, More Frequent Outages Learn Why That's a Good Thing Previous Next Pay Bill Online MANA...
- Reference/context hits: [LPEA outage center](https://lpea.coop/outage-center); [LPEA wildfire / public safety power shutoffs](https://lpea.coop/psps); [LPEA red flag outage impact page](https://lpea.coop/outages/red-flag-warnings-and-impact-outages-prioritizing-safety-our-members); [LPEA fire mitigation](https://lpea.coop/fire-mitigation)

**Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## Next 7 Days

| Date | Tier | Main reason | Worst sampled metrics |
| --- | --- | --- | --- |
| Wed, Jun 24 | HIGH | Active NWS Red Flag Warning or Fire Weather Watch touches this local date. | Pagosa Springs: RH 18%, wind/gust 25 mph, thunder 29%<br>Arboles / southwest county: RH 15%, wind/gust 29 mph, thunder 26%<br>Chimney Rock / west county: RH 15%, wind/gust 25 mph, thunder 29% |
| Thu, Jun 25 | HIGH | Active NWS Red Flag Warning or Fire Weather Watch touches this local date. | Pagosa Springs: RH 24%, wind/gust 28 mph, thunder 26%<br>Arboles / southwest county: RH 22%, wind/gust 30 mph, thunder 25%<br>Chimney Rock / west county: RH 18%, wind/gust 26 mph, thunder 24% |
| Fri, Jun 26 | HIGH | Active NWS Red Flag Warning or Fire Weather Watch touches this local date. | Pagosa Springs: RH 22%, wind/gust 31 mph, thunder 38%<br>Arboles / southwest county: RH 20%, wind/gust 29 mph, thunder 29%<br>Chimney Rock / west county: RH 17%, wind/gust 29 mph, thunder 32% |
| Sat, Jun 27 | HIGH | Pagosa Springs: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 13%, wind/gust 44 mph, thunder 5%<br>Arboles / southwest county: RH 10%, wind/gust 41 mph, thunder 5%<br>Chimney Rock / west county: RH 9%, wind/gust 43 mph, thunder 5% |
| Sun, Jun 28 | HIGH | Arboles / southwest county: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 16%, wind/gust 41 mph, thunder 1%<br>Arboles / southwest county: RH 11%, wind/gust 40 mph, thunder 1%<br>Chimney Rock / west county: RH 10%, wind/gust 39 mph, thunder 1% |
| Mon, Jun 29 | HIGH | Arboles / southwest county: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 16%, wind/gust 30 mph, thunder 1%<br>Arboles / southwest county: RH 12%, wind/gust 33 mph, thunder 1%<br>Chimney Rock / west county: RH 10%, wind/gust 28 mph, thunder 1% |
| Tue, Jun 30 | HIGH | Durango / La Plata County: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 16%, wind/gust 28 mph, thunder 1%<br>Arboles / southwest county: RH 11%, wind/gust 25 mph, thunder 1%<br>Chimney Rock / west county: RH 10%, wind/gust 24 mph, thunder 1% |

## Sample Point Status

- Pagosa Springs: COZ295 (matches), forecast zone COZ023, county zone COC007
- Arboles / southwest county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Chimney Rock / west county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Piedra / north county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Chromo / southeast county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Durango / La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Bayfield / east La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Ignacio / southeast La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
