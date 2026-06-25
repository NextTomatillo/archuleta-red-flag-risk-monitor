# Archuleta Red Flag Risk Monitor

Generated: Jun 25, 2026 at 3:21 AM MDT (Pagosa Springs, CO local time)
Next update: Jun 25, 2026 at 4:21 AM MDT (Pagosa Springs, CO local time)
Date/time basis: Pagosa Springs, CO local time (America/Denver)
> **Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## At A Glance

- Overall tier: **HIGH**
- PSPS likelihood: **LIKELY**
- PSPS likely dates: Sat, Jun 27; Sun, Jun 28; Mon, Jun 29; Tue, Jun 30; Wed, Jul 1
- PSPS watch dates: Thu, Jun 25; Fri, Jun 26
- Monitor heads-up recommended: **YES** - Send this monitor report because current risk is HIGH. This is not an official LPEA or NWS notice.
- HIGH dates: Thu, Jun 25; Fri, Jun 26; Sat, Jun 27; Sun, Jun 28; Mon, Jun 29; Tue, Jun 30; Wed, Jul 1
- CONCERN dates: None
- ELEVATED dates: None
- Official NWS Red Flag / Fire Weather alerts (COZ295): 1
- LPEA signal: `active_keyword_match` - LPEA active/update sources contained power-interruption keywords; review source before treating as confirmed outage intent.
- LPEA source coverage: 13 sources; 5/5 official social sources reachable
- NWS discussion: NWS discussion contains fire-weather concern language.

## Decision Support

- Summary: Highest LPEA PSPS concern is Sat, Jun 27 near Pagosa Springs (LIKELY 100/100), driven by very strong wind/gust signal near 43 mph; red-flag RH near 14%; 4 sampled hours meet red-flag screen.
- Confidence: **MEDIUM** (69/100) - 8/8 sampled weather points available; 7/7 fire-posture sources reachable; official NWS alert zones checked; 13/13 LPEA public sources reachable; LPEA active/update sources checked; forecast changed substantially versus prior run; no confirmed PSPS events logged yet for calibration
- Fire danger peak: Sat, Jun 27: Pagosa Springs EXTREME 100/100
- Red Flag likelihood peak: Sat, Jun 27: Pagosa Springs LIKELY 100/100
- LPEA PSPS peak: Sat, Jun 27: Pagosa Springs LIKELY 100/100
- Method: rules-based decision support using public weather, fire-posture, and LPEA source signals; scores are screening estimates, not official or statistically calibrated probabilities.

| Date | Fire danger | Red Flag likelihood | LPEA PSPS | Main window |
| --- | --- | --- | --- | --- |
| Thu, Jun 25 | Chimney Rock / west county: VERY HIGH 74/100 | Ignacio / southeast La Plata County: POSSIBLE 43/100 | Chimney Rock / west county: LIKELY 86/100 | Peak ingredients near 5 PM local; RH 22%, wind 26 mph. |
| Fri, Jun 26 | Arboles / southwest county: VERY HIGH 74/100 | Arboles / southwest county: POSSIBLE 39/100 | Arboles / southwest county: LIKELY 86/100 | Peak ingredients near 4 PM local; RH 24%, wind 28 mph. |
| Sat, Jun 27 | Pagosa Springs: EXTREME 100/100 | Pagosa Springs: LIKELY 100/100 | Pagosa Springs: LIKELY 100/100 | 2 PM-8 PM local; 7 near/red-flag threshold hours. |
| Sun, Jun 28 | Arboles / southwest county: EXTREME 100/100 | Arboles / southwest county: LIKELY 100/100 | Pagosa Springs: LIKELY 100/100 | 1 PM-8 PM local; 8 near/red-flag threshold hours. |
| Mon, Jun 29 | Ignacio / southeast La Plata County: EXTREME 100/100 | Ignacio / southeast La Plata County: LIKELY 100/100 | Pagosa Springs: LIKELY 100/100 | 1 PM-7 PM local; 7 near/red-flag threshold hours. |
| Tue, Jun 30 | Durango / La Plata County: EXTREME 100/100 | Durango / La Plata County: LIKELY 92/100 | Durango / La Plata County: LIKELY 100/100 | 12 PM-7 PM local; 8 near/red-flag threshold hours. |
| Wed, Jul 1 | Durango / La Plata County: EXTREME 95/100 | Durango / La Plata County: LIKELY 80/100 | Durango / La Plata County: LIKELY 97/100 | 12 PM-6 PM local; 7 near/red-flag threshold hours. |

## Trend Intelligence

- Summary: Momentum is easing versus the prior run (Jun 24 at 3:22 PM MDT); forecast volatility is high and first WATCH-or-higher date is Thu, Jun 25.
- Momentum: **Easing**
- Forecast volatility: **HIGH** (33/100)
- First WATCH-or-higher PSPS date: Thu, Jun 25
- Watch-date movement: First WATCH-or-higher PSPS date moved later from Wed, Jun 24 to Thu, Jun 25.
- Method: compares current forecast evidence against prior local forecast history.

Notable changes:
- First WATCH-or-higher PSPS date moved later from Wed, Jun 24 to Thu, Jun 25.
- Fri, Jun 26: easing vs prior run; PSPS LIKELY -> WATCH; score -16, wind -5 mph, RH +3%, red-flag hours 0. Driver shifted to Arboles / southwest county.

## Public Analysis Export

- Summary: Highest LPEA PSPS concern is Sat, Jun 27 near Pagosa Springs (LIKELY 100/100), driven by very strong wind/gust signal near 43 mph; red-flag RH near 14%; 4 sampled hours meet red-flag screen.
- Trend: Momentum is easing versus the prior run (Jun 24 at 3:22 PM MDT); forecast volatility is high and first WATCH-or-higher date is Thu, Jun 25.
- Confidence: **MEDIUM** (69/100)
- First WATCH-or-higher PSPS date: Thu, Jun 25
- PSPS peak: Sat, Jun 27 near Pagosa Springs at LIKELY 100/100
- Red Flag peak: Sat, Jun 27 near Pagosa Springs at LIKELY 100/100
- Fire danger peak: Sat, Jun 27 near Pagosa Springs at EXTREME 100/100
- LPEA operational outage context: No monitored active LPEA source currently describes a non-PSPS outage.
- Public JSON: `archuleta_red_flag_monitor/public_analysis_export.json`

What changed:
- First WATCH-or-higher PSPS date moved later from Wed, Jun 24 to Thu, Jun 25.
- Fri, Jun 26: easing vs prior run; PSPS LIKELY -> WATCH; score -16, wind -5 mph, RH +3%, red-flag hours 0. Driver shifted to Arboles / southwest county.

What to watch next:
- Check whether the largest day-level changes line up with wind/RH movement or public-source context.
- Check whether the LPEA active match is still a broad red-flag banner rather than direct PSPS/outage intent.
- Watch whether the highest-risk locations remain consistent across runs or the driver area is moving.
- If a PSPS occurs, log the confirmed date, location, and source so future hit-rate scoring can improve.

## PSPS Likelihood

- **PSPS means Public Safety Power Shutoff:** a planned, safety-related power shutoff LPEA may use during dangerous fire-weather conditions to reduce wildfire ignition risk. See [LPEA PSPS guidance](https://lpea.coop/psps) and the [LPEA outage center](https://lpea.coop/outage-center); if power is out, also check the [LPEA outage map](https://outage.lpea.coop).
- Overall: **LIKELY** - PSPS likelihood is high on weather-driven red-flag days; prepare for possible LPEA safety-related interruption behavior.
- Likely PSPS watch dates: Sat, Jun 27; Sun, Jun 28; Mon, Jun 29; Tue, Jun 30; Wed, Jul 1
- PSPS watch dates: Thu, Jun 25; Fri, Jun 26
- LPEA signal basis: LPEA active/update source contains red-flag, wildfire, or power-interruption language.
- Note: This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

| Date | PSPS likelihood | Driver locations | Weather basis |
| --- | --- | --- | --- |
| Thu, Jun 25 | WATCH | Chimney Rock / west county (WATCH 50/100); Durango / La Plata County (WATCH 50/100); Ignacio / southeast La Plata County (WATCH 50/100) | Top weather score 50/100 at Chimney Rock / west county. Weather score 50/100: RH 21%, wind/gust 26 mph, red-flag hours 0, near-threshold hours 0. |
| Fri, Jun 26 | WATCH | Arboles / southwest county (WATCH 50/100); Chimney Rock / west county (WATCH 50/100); Durango / La Plata County (WATCH 50/100); Ignacio / southeast La Plata County (WATCH 50/100) | Top weather score 50/100 at Arboles / southwest county. Weather score 50/100: RH 22%, wind/gust 28 mph, red-flag hours 0, near-threshold hours 0. |
| Sat, Jun 27 | LIKELY | Arboles / southwest county (LIKELY 96/100); Chimney Rock / west county (LIKELY 96/100); Durango / La Plata County (LIKELY 96/100); Bayfield / east La Plata County (LIKELY 96/100) | Top weather score 96/100 at Arboles / southwest county. Weather score 96/100: RH 11%, wind/gust 41 mph, red-flag hours 9, near-threshold hours 12. |
| Sun, Jun 28 | LIKELY | Arboles / southwest county (LIKELY 81/100); Chimney Rock / west county (LIKELY 81/100); Durango / La Plata County (LIKELY 81/100); Ignacio / southeast La Plata County (LIKELY 81/100) | Top weather score 81/100 at Arboles / southwest county. Weather score 81/100: RH 11%, wind/gust 40 mph, red-flag hours 9, near-threshold hours 13. |
| Mon, Jun 29 | LIKELY | Arboles / southwest county (LIKELY 77/100); Durango / La Plata County (LIKELY 77/100); Bayfield / east La Plata County (LIKELY 77/100); Ignacio / southeast La Plata County (LIKELY 77/100) | Top weather score 77/100 at Arboles / southwest county. Weather score 77/100: RH 11%, wind/gust 34 mph, red-flag hours 6, near-threshold hours 9. |
| Tue, Jun 30 | LIKELY | Durango / La Plata County (LIKELY 71/100); Bayfield / east La Plata County (LIKELY 71/100); Ignacio / southeast La Plata County (LIKELY 71/100); Pagosa Springs (LIKELY 67/100) | Top weather score 71/100 at Durango / La Plata County. Weather score 71/100: RH 11%, wind/gust 28 mph, red-flag hours 6, near-threshold hours 8. |
| Wed, Jul 1 | LIKELY | Durango / La Plata County (LIKELY 67/100); Arboles / southwest county (WATCH 52/100); Chimney Rock / west county (WATCH 52/100); Bayfield / east La Plata County (WATCH 52/100) | Top weather score 67/100 at Durango / La Plata County. Weather score 67/100: RH 11%, wind/gust 25 mph, red-flag hours 3, near-threshold hours 7. |

## Area-Specific Outlook

| Area | Today | Peak this run | Highest-risk window |
| --- | --- | --- | --- |
| Arboles | ELEVATED 44/100 | Sat, Jun 27: LIKELY 96/100 | 12 PM-11 PM local; 12 near/red-flag threshold hours. |
| Chimney Rock | WATCH 50/100 | Sat, Jun 27: LIKELY 96/100 | 12 PM-11 PM local; 12 near/red-flag threshold hours. |
| Durango | WATCH 50/100 | Sat, Jun 27: LIKELY 96/100 | 1 PM-10 PM local; 10 near/red-flag threshold hours. |
| Bayfield | ELEVATED 44/100 | Sat, Jun 27: LIKELY 96/100 | 1 PM-10 PM local; 10 near/red-flag threshold hours. |
| Ignacio | WATCH 50/100 | Sat, Jun 27: LIKELY 96/100 | 1 PM-10 PM local; 10 near/red-flag threshold hours. |
| Pagosa Springs | ELEVATED 44/100 | Sat, Jun 27: LIKELY 92/100 | 2 PM-8 PM local; 7 near/red-flag threshold hours. |
| Piedra | ELEVATED 35/100 | Sat, Jun 27: LIKELY 82/100 | 4 PM-8 PM local; 5 near/red-flag threshold hours. |
| Chromo | ELEVATED 44/100 | Sat, Jun 27: LIKELY 82/100 | 3 PM-8 PM local; 6 near/red-flag threshold hours. |

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
- WATCH/LIKELY false-watch past days: 27
- Pending WATCH/LIKELY dates in current forecast: Thu, Jun 25; Fri, Jun 26; Sat, Jun 27; Sun, Jun 28; Mon, Jun 29; Tue, Jun 30; Wed, Jul 1
- Calibration source: manual PSPS event log plus forecast history from prior monitor runs.

### Red Flag / Fire Weather Calibration

- Summary: 18/18 official Red Flag / Fire Weather alert dates had a pre-alert HIGH monitor signal. Average lead time: 4.9 days.
- Official alert dates logged: 18
- Pre-alert HIGH hit rate: 100%
- Average lead time: 4.9 days
- HIGH false-watch past days: 9
- Pending HIGH dates in current forecast: Sun, Jun 28; Mon, Jun 29; Tue, Jun 30; Wed, Jul 1
- Calibration source: official NWS Red Flag / Fire Weather alert dates plus forecast history from prior monitor runs.

## Official Weather Alerts

- Monitored NWS zones: COC007, COC067, COZ019, COZ022, COZ023, COZ295
- [Fire Weather Watch](https://api.weather.gov/alerts/urn:oid:2.49.0.1.840.0.296bc85c62445a3e39aa22cbf3721c27e0a3e854.004.1): Fire Weather Watch issued June 25 at 1:30AM MDT until June 28 at 12:00AM MDT by NWS Grand Junction CO; 2026-06-25T01:30:00-06:00 to 2026-06-28T00:00:00-06:00; zones COZ201, COZ205, COZ291, COZ292, COZ293, COZ294, COZ295
- [Air Quality Alert](https://api.weather.gov/alerts/urn:oid:2.49.0.1.840.0.9b8b8196feec5d69cd107d214f2b0c5c910a1500.001.1): Air Quality Alert issued June 25 at 12:10AM MDT by NWS Grand Junction CO; 2026-06-25T00:10:00-06:00 to 2026-06-25T09:00:00-06:00; zones COC029, COC033, COC037, COC045, COC051, COC053, COC067, COC077, COC083, COC085, COC091, COC097, COC103, COC111, COC113
- [Air Quality Alert](https://api.weather.gov/alerts/urn:oid:2.49.0.1.840.0.2e75599a9beaa31404559dc71435b64d53aec14b.001.1): Air Quality Alert issued June 24 at 4:10PM MDT by NWS Grand Junction CO; 2026-06-24T16:10:00-06:00 to 2026-06-25T09:00:00-06:00; zones COC029, COC033, COC037, COC045, COC051, COC053, COC067, COC077, COC083, COC085, COC091, COC097, COC103, COC111, COC113
- [Air Quality Alert](https://api.weather.gov/alerts/urn:oid:2.49.0.1.840.0.29e749e5d1196f64bf6c88f21f880c8d31c8983b.001.1): Air Quality Alert issued June 24 at 9:10AM MDT by NWS Grand Junction CO; 2026-06-24T09:10:00-06:00 to 2026-06-25T09:00:00-06:00; zones COC029, COC033, COC037, COC045, COC051, COC053, COC067, COC077, COC083, COC085, COC091, COC097, COC103, COC111, COC113

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
| Thu, Jun 25 | HIGH | Active NWS Red Flag Warning or Fire Weather Watch touches this local date. | Pagosa Springs: RH 25%, wind/gust 26 mph, thunder 27%<br>Arboles / southwest county: RH 24%, wind/gust 29 mph, thunder 24%<br>Chimney Rock / west county: RH 21%, wind/gust 26 mph, thunder 23% |
| Fri, Jun 26 | HIGH | Active NWS Red Flag Warning or Fire Weather Watch touches this local date. | Pagosa Springs: RH 24%, wind/gust 29 mph, thunder 33%<br>Arboles / southwest county: RH 22%, wind/gust 28 mph, thunder 29%<br>Chimney Rock / west county: RH 20%, wind/gust 28 mph, thunder 31% |
| Sat, Jun 27 | HIGH | Pagosa Springs: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 14%, wind/gust 43 mph, thunder 10%<br>Arboles / southwest county: RH 11%, wind/gust 41 mph, thunder 7%<br>Chimney Rock / west county: RH 10%, wind/gust 41 mph, thunder 11% |
| Sun, Jun 28 | HIGH | Pagosa Springs: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 14%, wind/gust 43 mph, thunder 0%<br>Arboles / southwest county: RH 11%, wind/gust 40 mph, thunder 0%<br>Chimney Rock / west county: RH 10%, wind/gust 40 mph, thunder 0% |
| Mon, Jun 29 | HIGH | Pagosa Springs: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 14%, wind/gust 32 mph, thunder 1%<br>Arboles / southwest county: RH 11%, wind/gust 34 mph, thunder 1%<br>Chimney Rock / west county: RH 10%, wind/gust 28 mph, thunder 1% |
| Tue, Jun 30 | HIGH | Pagosa Springs: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 13%, wind/gust 29 mph, thunder 2%<br>Arboles / southwest county: RH 11%, wind/gust 25 mph, thunder 2%<br>Chimney Rock / west county: RH 9%, wind/gust 24 mph, thunder 2% |
| Wed, Jul 1 | HIGH | Durango / La Plata County: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 13%, wind/gust 24 mph, thunder 4%<br>Arboles / southwest county: RH 10%, wind/gust 22 mph, thunder 4%<br>Chimney Rock / west county: RH 9%, wind/gust 22 mph, thunder 4% |

## Sample Point Status

- Pagosa Springs: COZ295 (matches), forecast zone COZ023, county zone COC007
- Arboles / southwest county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Chimney Rock / west county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Piedra / north county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Chromo / southeast county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Durango / La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Bayfield / east La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Ignacio / southeast La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
