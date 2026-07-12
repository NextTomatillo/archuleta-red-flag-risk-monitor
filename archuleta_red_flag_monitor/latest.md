# Archuleta Red Flag Risk Monitor

Generated: Jul 12, 2026 at 5:30 AM MDT (Pagosa Springs, CO local time)
Next update: Jul 12, 2026 at 6:30 AM MDT (Pagosa Springs, CO local time)
Date/time basis: Pagosa Springs, CO local time (America/Denver)
> **Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## At A Glance

- Overall tier: **ELEVATED**
- PSPS likelihood: **WATCH**
- PSPS likely dates: None
- PSPS watch dates: Sun, Jul 12; Mon, Jul 13; Tue, Jul 14; Wed, Jul 15; Thu, Jul 16; Fri, Jul 17; Sat, Jul 18
- Monitor heads-up recommended: **YES** - Send this monitor report because current risk is ELEVATED. This is not an official LPEA or NWS notice.
- HIGH dates: None
- CONCERN dates: None
- ELEVATED dates: Sun, Jul 12; Mon, Jul 13; Tue, Jul 14; Wed, Jul 15; Thu, Jul 16; Fri, Jul 17; Sat, Jul 18
- Official NWS Red Flag / Fire Weather alerts (COZ295): 0
- LPEA signal: `active_keyword_match` - LPEA active/update sources contained power-interruption keywords; review source before treating as confirmed outage intent.
- LPEA source coverage: 13 sources; 5/5 official social sources reachable
- NWS discussion: No concerning fire-weather language found in latest GJT discussion.

## Decision Support

- Summary: Highest LPEA PSPS concern is Sun, Jul 12 near Arboles / southwest county (WATCH 50/100), driven by breezy wind/gust signal near 17 mph; red-flag RH near 14%; modest thunder signal near 21%.
- Confidence: **MEDIUM** (66/100) - 7/8 sampled weather points available; 7/7 fire-posture sources reachable; official NWS alert zones checked; 13/13 LPEA public sources reachable; LPEA active/update sources checked; forecast changed substantially versus prior run; no confirmed PSPS events logged yet for calibration
- Fire danger peak: Sun, Jul 12: Arboles / southwest county HIGH 64/100
- Red Flag likelihood peak: Sun, Jul 12: Arboles / southwest county LOW 25/100
- LPEA PSPS peak: Sun, Jul 12: Arboles / southwest county WATCH 50/100
- Method: rules-based decision support using public weather, fire-posture, and LPEA source signals; scores are screening estimates, not official or statistically calibrated probabilities.

| Date | Fire danger | Red Flag likelihood | LPEA PSPS | Main window |
| --- | --- | --- | --- | --- |
| Sun, Jul 12 | Arboles / southwest county: HIGH 64/100 | Arboles / southwest county: LOW 25/100 | Arboles / southwest county: WATCH 50/100 | Peak ingredients near 9 PM local; RH 29%, wind 17 mph. |
| Mon, Jul 13 | Arboles / southwest county: HIGH 58/100 | Durango / La Plata County: LOW 25/100 | Durango / La Plata County: ELEVATED 32/100 | Peak ingredients near 4 PM local; RH 34%, wind 18 mph. |
| Tue, Jul 14 | Pagosa Springs: HIGH 58/100 | Chimney Rock / west county: LOW 25/100 | Chimney Rock / west county: ELEVATED 32/100 | Peak ingredients near 4 PM local; RH 23%, wind 15 mph. |
| Wed, Jul 15 | Chimney Rock / west county: HIGH 58/100 | Pagosa Springs: LOW 25/100 | Pagosa Springs: ELEVATED 38/100 | Peak ingredients near 4 PM local; RH 22%, wind 15 mph. |
| Thu, Jul 16 | Chimney Rock / west county: HIGH 58/100 | Chimney Rock / west county: LOW 25/100 | Chimney Rock / west county: ELEVATED 38/100 | Peak ingredients near 4 PM local; RH 23%, wind 16 mph. |
| Fri, Jul 17 | Chimney Rock / west county: HIGH 58/100 | Chimney Rock / west county: LOW 25/100 | Chimney Rock / west county: ELEVATED 38/100 | Peak ingredients near 3 PM local; RH 22%, wind 16 mph. |
| Sat, Jul 18 | Chimney Rock / west county: HIGH 58/100 | Chimney Rock / west county: LOW 25/100 | Chimney Rock / west county: ELEVATED 38/100 | Peak ingredients near 3 PM local; RH 21%, wind 16 mph. |

## Trend Intelligence

- Summary: Momentum is rising versus the prior run (Jul 11 at 5:41 PM MDT); forecast volatility is high and first WATCH-or-higher date is not present.
- Momentum: **Rising**
- Forecast volatility: **HIGH** (54/100)
- First WATCH-or-higher PSPS date: None
- Watch-date movement: Prior WATCH-or-higher PSPS date Sun, Jul 12 dropped below WATCH.
- Method: compares current forecast evidence against prior local forecast history.

Notable changes:
- Prior WATCH-or-higher PSPS date Sun, Jul 12 dropped below WATCH.
- Sun, Jul 12: easing vs prior run; PSPS WATCH -> ELEVATED; score -17, wind -12 mph, RH -1%, red-flag hours 0.
- Wed, Jul 15: worsening vs prior run; PSPS LOW -> ELEVATED; score +6, wind +2 mph, RH -5%, red-flag hours 0. Driver shifted to Pagosa Springs.
- Fri, Jul 17: worsening vs prior run; PSPS LOW -> ELEVATED; score +6, wind +1 mph, RH -5%, red-flag hours 0. Driver shifted to Chimney Rock / west county.
- Thu, Jul 16: worsening vs prior run; PSPS LOW -> ELEVATED; score +6, wind 0 mph, RH -5%, red-flag hours 0. Driver shifted to Chimney Rock / west county.

## Public Analysis Export

- Summary: Highest LPEA PSPS concern is Sun, Jul 12 near Arboles / southwest county (WATCH 50/100), driven by breezy wind/gust signal near 17 mph; red-flag RH near 14%; modest thunder signal near 21%.
- Trend: Momentum is rising versus the prior run (Jul 11 at 5:41 PM MDT); forecast volatility is high and first WATCH-or-higher date is not present.
- Confidence: **MEDIUM** (66/100)
- First WATCH-or-higher PSPS date: None
- PSPS peak: Sun, Jul 12 near Arboles / southwest county at WATCH 50/100
- Red Flag peak: Sun, Jul 12 near Arboles / southwest county at LOW 25/100
- Fire danger peak: Sun, Jul 12 near Arboles / southwest county at HIGH 64/100
- LPEA operational outage context: No monitored active LPEA source currently describes a non-PSPS outage.
- Public JSON: `archuleta_red_flag_monitor/public_analysis_export.json`

What changed:
- Prior WATCH-or-higher PSPS date Sun, Jul 12 dropped below WATCH.
- Sun, Jul 12: easing vs prior run; PSPS WATCH -> ELEVATED; score -17, wind -12 mph, RH -1%, red-flag hours 0.
- Wed, Jul 15: worsening vs prior run; PSPS LOW -> ELEVATED; score +6, wind +2 mph, RH -5%, red-flag hours 0. Driver shifted to Pagosa Springs.
- Fri, Jul 17: worsening vs prior run; PSPS LOW -> ELEVATED; score +6, wind +1 mph, RH -5%, red-flag hours 0. Driver shifted to Chimney Rock / west county.
- Thu, Jul 16: worsening vs prior run; PSPS LOW -> ELEVATED; score +6, wind 0 mph, RH -5%, red-flag hours 0. Driver shifted to Chimney Rock / west county.

What to watch next:
- Check whether the largest day-level changes line up with wind/RH movement or public-source context.
- Check whether the LPEA active match is still a broad red-flag banner rather than direct PSPS/outage intent.
- Watch whether the highest-risk locations remain consistent across runs or the driver area is moving.
- If a PSPS occurs, log the confirmed date, location, and source so future hit-rate scoring can improve.

## PSPS Likelihood

- **PSPS means Public Safety Power Shutoff:** a planned, safety-related power shutoff LPEA may use during dangerous fire-weather conditions to reduce wildfire ignition risk. See [LPEA PSPS guidance](https://lpea.coop/psps) and the [LPEA outage center](https://lpea.coop/outage-center); if power is out, also check the [LPEA outage map](https://outage.lpea.coop).
- Overall: **WATCH** - Weather-driven PSPS watch conditions are present; monitor LPEA updates and outage channels.
- Likely PSPS watch dates: None
- PSPS watch dates: Sun, Jul 12; Mon, Jul 13; Tue, Jul 14; Wed, Jul 15; Thu, Jul 16; Fri, Jul 17; Sat, Jul 18
- LPEA signal basis: LPEA active/update source contains red-flag, wildfire, or power-interruption language.
- Note: This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

| Date | PSPS likelihood | Driver locations | Weather basis |
| --- | --- | --- | --- |
| Sun, Jul 12 | WATCH | Arboles / southwest county (ELEVATED 30/100); Durango / La Plata County (ELEVATED 30/100); Ignacio / southeast La Plata County (ELEVATED 30/100) | Top weather score 30/100 at Arboles / southwest county. Weather score 30/100: RH 14%, wind/gust 17 mph, red-flag hours 0, near-threshold hours 0. |
| Mon, Jul 13 | WATCH | Durango / La Plata County (LOW 12/100); Ignacio / southeast La Plata County (LOW 12/100); Arboles / southwest county (LOW 10/100) | Top weather score 12/100 at Durango / La Plata County. Weather score 12/100: RH 24%, wind/gust 18 mph, red-flag hours 0, near-threshold hours 0. |
| Tue, Jul 14 | WATCH | Chimney Rock / west county (LOW 12/100); Ignacio / southeast La Plata County (LOW 12/100); Pagosa Springs (LOW 10/100) | Top weather score 12/100 at Chimney Rock / west county. Weather score 12/100: RH 23%, wind/gust 15 mph, red-flag hours 0, near-threshold hours 0. |
| Wed, Jul 15 | WATCH | Pagosa Springs (ELEVATED 18/100); Chimney Rock / west county (ELEVATED 18/100); Arboles / southwest county (LOW 12/100) | Top weather score 18/100 at Pagosa Springs. Weather score 18/100: RH 22%, wind/gust 15 mph, red-flag hours 0, near-threshold hours 0. |
| Thu, Jul 16 | WATCH | Chimney Rock / west county (ELEVATED 18/100); Pagosa Springs (LOW 12/100); Piedra / north county (LOW 12/100) | Top weather score 18/100 at Chimney Rock / west county. Weather score 18/100: RH 22%, wind/gust 16 mph, red-flag hours 0, near-threshold hours 0. |
| Fri, Jul 17 | WATCH | Chimney Rock / west county (ELEVATED 18/100); Pagosa Springs (LOW 12/100); Arboles / southwest county (LOW 12/100) | Top weather score 18/100 at Chimney Rock / west county. Weather score 18/100: RH 22%, wind/gust 16 mph, red-flag hours 0, near-threshold hours 0. |
| Sat, Jul 18 | WATCH | Chimney Rock / west county (ELEVATED 18/100); Pagosa Springs (LOW 12/100); Arboles / southwest county (LOW 12/100) | Top weather score 18/100 at Chimney Rock / west county. Weather score 18/100: RH 21%, wind/gust 16 mph, red-flag hours 0, near-threshold hours 0. |

## Area-Specific Outlook

| Area | Today | Peak this run | Highest-risk window |
| --- | --- | --- | --- |
| Arboles | ELEVATED 30/100 | Sun, Jul 12: ELEVATED 30/100 | Peak ingredients near 9 PM local; RH 29%, wind 17 mph. |
| Durango | ELEVATED 30/100 | Sun, Jul 12: ELEVATED 30/100 | Peak ingredients near 5 PM local; RH 18%, wind 15 mph. |
| Ignacio | ELEVATED 30/100 | Sun, Jul 12: ELEVATED 30/100 | Peak ingredients near 10 PM local; RH 37%, wind 17 mph. |
| Chimney Rock | ELEVATED 26/100 | Sun, Jul 12: ELEVATED 26/100 | Peak ingredients near 9 PM local; RH 26%, wind 14 mph. |
| Pagosa Springs | ELEVATED 24/100 | Sun, Jul 12: ELEVATED 24/100 | Peak ingredients near 9 PM local; RH 31%, wind 16 mph. |
| Chromo | ELEVATED 24/100 | Sun, Jul 12: ELEVATED 24/100 | Peak ingredients near 9 PM local; RH 38%, wind 17 mph. |
| Piedra | LOW 16/100 | Sun, Jul 12: LOW 16/100 | Peak ingredients near 6 PM local; RH 21%, wind 13 mph. |

## Fire Posture + Restrictions

- Summary: 5 official sources indicate fire restrictions or staged restrictions.
- Max restriction stage detected: STAGE 2
- Max fire danger detected: EXTREME
- Sources reachable: 7/7
- Note: Official-source status check only; verify restrictions and burn decisions with the responsible jurisdiction.

| Jurisdiction | Restrictions | Fire danger | Source |
| --- | --- | --- | --- |
| Archuleta County | STAGE 2 | UNKNOWN | [Archuleta County Sheriff fire updates](https://sheriff.archuletacounty.gov/divisions/emergency-operations/fire-updates-and-information/) |
| Pagosa Springs | STAGE 2 | UNKNOWN | [Town of Pagosa Springs](https://www.pagosasprings.co.gov/) |
| San Juan National Forest | STAGE 2 | EXTREME | [San Juan National Forest fire](https://www.fs.usda.gov/r02/sanjuan/fire) |
| BLM Tres Rios | UNKNOWN | UNKNOWN | [BLM Tres Rios Field Office](https://www.blm.gov/office/tres-rios-field-office) |
| La Plata County / Durango Fire | NONE | UNKNOWN | [Durango Fire & Rescue fire conditions](https://www.durangofire.org/fire-conditions) |
| Durango | STAGE 2 | UNKNOWN | [City of Durango](https://www.durangoco.gov/) |
| Southern Ute / Ignacio | STAGE 2 | UNKNOWN | [Southern Ute Indian Tribe](https://www.southernute-nsn.gov/) |

## Forecast Calibration

### PSPS Calibration

- Summary: No confirmed LPEA PSPS events logged yet; calibration will start once events are added.
- Confirmed PSPS events logged: 0
- Candidate/unconfirmed events logged: 0
- WATCH/LIKELY false-watch past days: 43
- Pending WATCH/LIKELY dates in current forecast: Sun, Jul 12; Mon, Jul 13; Tue, Jul 14; Wed, Jul 15; Thu, Jul 16; Fri, Jul 17; Sat, Jul 18
- Calibration source: manual PSPS event log plus forecast history from prior monitor runs.

### Red Flag / Fire Weather Calibration

- Summary: 21/21 official Red Flag / Fire Weather alert dates had a pre-alert HIGH monitor signal. Average lead time: 5.0 days.
- Official alert dates logged: 21
- Pre-alert HIGH hit rate: 100%
- Average lead time: 5.0 days
- HIGH false-watch past days: 16
- Pending HIGH dates in current forecast: None
- Calibration source: official NWS Red Flag / Fire Weather alert dates plus forecast history from prior monitor runs.

## Official Weather Alerts

- Monitored NWS zones: COC007, COC067, COZ019, COZ022, COZ023, COZ295
- No active official NWS Red Flag / Fire Weather or related weather alerts found for monitored zones.

## LPEA Power Signal

- Status: `active_keyword_match` - LPEA active/update sources contained power-interruption keywords; review source before treating as confirmed outage intent.
- Meaning: Active source match means a monitored LPEA active/update source currently contains fire, outage, PSPS, or power-interruption keywords. Operational outages are shown separately and are not treated as PSPS/fire evidence unless the source text says so.
- Operational outage context: No monitored active LPEA source currently describes a non-PSPS outage.
- Source coverage: 13 sources; 5/5 official social sources reachable
- Evidence quality: 0 operational, 3 active/update, 2 archive/context, 4 reference source matches.
- Active/update source pages with matches: LPEA homepage (red flag, public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation); LPEA latest news (public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation, restoration); LPEA news releases (red flag, wildfire, public safety power shutoff, power shutoff, shutoff, power outage); LPEA LinkedIn (wildfire, public safety power shutoff, power shutoff, shutoff, fire mitigation)
- Distinct active/update signals: LPEA homepage (red flag, public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation); LPEA news releases (red flag, wildfire, public safety power shutoff, power shutoff, shutoff, power outage); News-release archive PSPS item (red flag, wildfire, public safety power shutoff, power shutoff, shutoff, power outage); LPEA LinkedIn (wildfire, public safety power shutoff, power shutoff, shutoff, fire mitigation); LinkedIn PSPS explainer post (wildfire, public safety power shutoff, power shutoff, shutoff, fire mitigation)
- Example signal: ...you at the Durango Farmers Market on Main, this Saturday, July 11! View Details Red Flag Conditions May Result in Longer, More Frequent Outages Learn Why That's a Good Thing LPEA Announces 2026-27 Board Leade...
- Reference/context hits: [LPEA outage center](https://lpea.coop/outage-center); [LPEA wildfire / public safety power shutoffs](https://lpea.coop/psps); [LPEA red flag outage impact page](https://lpea.coop/outages/red-flag-warnings-and-impact-outages-prioritizing-safety-our-members); [LPEA fire mitigation](https://lpea.coop/fire-mitigation)

**Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## Next 7 Days

| Date | Tier | Main reason | Worst sampled metrics |
| --- | --- | --- | --- |
| Sun, Jul 12 | ELEVATED | Pagosa Springs: Elevated ingredient present: thunder probability reaches 21%. | Pagosa Springs: RH 16%, wind/gust 16 mph, thunder 21%<br>Arboles / southwest county: RH 14%, wind/gust 17 mph, thunder 21%<br>Chimney Rock / west county: RH 12%, wind/gust 14 mph, thunder 20% |
| Mon, Jul 13 | ELEVATED | Pagosa Springs: Elevated ingredient present: thunder probability reaches 48%. | Pagosa Springs: RH 25%, wind/gust 13 mph, thunder 48%<br>Arboles / southwest county: RH 22%, wind/gust 14 mph, thunder 49%<br>Chimney Rock / west county: RH 22%, wind/gust 14 mph, thunder 56% |
| Tue, Jul 14 | ELEVATED | Pagosa Springs: Elevated ingredient present: thunder probability reaches 25%. | Pagosa Springs: RH 22%, wind/gust 13 mph, thunder 25%<br>Arboles / southwest county: RH 26%, wind/gust 13 mph, thunder 37%<br>Chimney Rock / west county: RH 23%, wind/gust 15 mph, thunder 36% |
| Wed, Jul 15 | ELEVATED | Pagosa Springs: Elevated ingredient present: thunder probability reaches 18%. | Pagosa Springs: RH 22%, wind/gust 15 mph, thunder 18%<br>Arboles / southwest county: RH 27%, wind/gust 17 mph, thunder 28%<br>Chimney Rock / west county: RH 22%, wind/gust 17 mph, thunder 25% |
| Thu, Jul 16 | ELEVATED | Pagosa Springs: Elevated ingredient present: thunder probability reaches 38%. | Pagosa Springs: RH 23%, wind/gust 15 mph, thunder 38%<br>Arboles / southwest county: RH 25%, wind/gust 14 mph, thunder 36%<br>Chimney Rock / west county: RH 22%, wind/gust 16 mph, thunder 38% |
| Fri, Jul 17 | ELEVATED | Pagosa Springs: Elevated ingredient present: thunder probability reaches 46%. | Pagosa Springs: RH 25%, wind/gust 15 mph, thunder 46%<br>Arboles / southwest county: RH 26%, wind/gust 16 mph, thunder 39%<br>Chimney Rock / west county: RH 22%, wind/gust 16 mph, thunder 42% |
| Sat, Jul 18 | ELEVATED | Pagosa Springs: Elevated ingredient present: thunder probability reaches 45%. | Pagosa Springs: RH 23%, wind/gust 16 mph, thunder 45%<br>Arboles / southwest county: RH 25%, wind/gust 16 mph, thunder 40%<br>Chimney Rock / west county: RH 21%, wind/gust 16 mph, thunder 41% |

## Sample Point Status

- Pagosa Springs: COZ295 (matches), forecast zone COZ023, county zone COC007
- Arboles / southwest county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Chimney Rock / west county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Piedra / north county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Chromo / southeast county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Durango / La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Bayfield / east La Plata County: unavailable (ReadTimeout: HTTPSConnectionPool(host='api.weather.gov', port=443): Read timed out. (read timeout=60))
- Ignacio / southeast La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
