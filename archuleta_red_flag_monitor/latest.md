# Archuleta Red Flag Risk Monitor

Generated: May 31, 2026 at 5:22 AM MDT (Pagosa Springs, CO local time)
Next update: May 31, 2026 at 6:22 AM MDT (Pagosa Springs, CO local time)
Date/time basis: Pagosa Springs, CO local time (America/Denver)
> **Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## At A Glance

- Overall tier: **HIGH**
- PSPS likelihood: **LIKELY**
- PSPS likely dates: Mon, Jun 1
- PSPS watch dates: Sun, May 31; Tue, Jun 2; Fri, Jun 5; Sat, Jun 6
- Monitor heads-up recommended: **YES** - Send this monitor report because current risk is HIGH. This is not an official LPEA or NWS notice.
- HIGH dates: Mon, Jun 1
- CONCERN dates: Sun, May 31; Tue, Jun 2; Thu, Jun 4; Fri, Jun 5; Sat, Jun 6
- ELEVATED dates: Wed, Jun 3
- Official NWS Red Flag / Fire Weather alerts (COZ295): 0
- LPEA signal: `active_keyword_match` - LPEA active/update sources contained power-interruption keywords; review source before treating as confirmed outage intent.
- LPEA source coverage: 13 sources; 5/5 official social sources reachable
- NWS discussion: NWS discussion contains fire-weather concern language.

## Decision Support

- Summary: Highest LPEA PSPS concern is Mon, Jun 1 near Pagosa Springs (LIKELY 97/100), driven by red-flag wind/gust signal near 25 mph; very dry RH near 10%; 3 sampled hours meet red-flag screen.
- Confidence: **MEDIUM** (68/100) - 8/8 sampled weather points available; 6/7 fire-posture sources reachable; official NWS alert zones checked; 13/13 LPEA public sources reachable; LPEA active/update sources checked; forecast changed substantially versus prior run; no confirmed PSPS events logged yet for calibration
- Fire danger peak: Mon, Jun 1: Durango / La Plata County EXTREME 86/100
- Red Flag likelihood peak: Mon, Jun 1: Durango / La Plata County LIKELY 81/100
- LPEA PSPS peak: Mon, Jun 1: Pagosa Springs LIKELY 97/100
- Method: rules-based decision support using public weather, fire-posture, and LPEA source signals; scores are screening estimates, not official or statistically calibrated probabilities.

| Date | Fire danger | Red Flag likelihood | LPEA PSPS | Main window |
| --- | --- | --- | --- | --- |
| Sun, May 31 | Durango / La Plata County: VERY HIGH 75/100 | Durango / La Plata County: WATCH 62/100 | Durango / La Plata County: LIKELY 76/100 | 2 PM-5 PM local; 4 near/red-flag threshold hours. |
| Mon, Jun 1 | Durango / La Plata County: EXTREME 86/100 | Durango / La Plata County: LIKELY 81/100 | Pagosa Springs: LIKELY 97/100 | 1 PM-6 PM local; 6 near/red-flag threshold hours. |
| Tue, Jun 2 | Ignacio / southeast La Plata County: VERY HIGH 80/100 | Ignacio / southeast La Plata County: WATCH 70/100 | Bayfield / east La Plata County: LIKELY 80/100 | 3 PM-6 PM local; 4 near/red-flag threshold hours. |
| Wed, Jun 3 | Arboles / southwest county: MODERATE 48/100 | Arboles / southwest county: LOW 25/100 | Arboles / southwest county: ELEVATED 38/100 | Peak ingredients near 5 PM local; RH 24%, wind 16 mph. |
| Thu, Jun 4 | Chimney Rock / west county: HIGH 63/100 | Chimney Rock / west county: POSSIBLE 50/100 | Ignacio / southeast La Plata County: WATCH 48/100 | 5 PM-5 PM local; 1 near/red-flag threshold hour. |
| Fri, Jun 5 | Durango / La Plata County: VERY HIGH 74/100 | Durango / La Plata County: WATCH 61/100 | Durango / La Plata County: LIKELY 72/100 | 2 PM-6 PM local; 5 near/red-flag threshold hours. |
| Sat, Jun 6 | Durango / La Plata County: VERY HIGH 77/100 | Durango / La Plata County: WATCH 65/100 | Arboles / southwest county: LIKELY 76/100 | 3 PM-6 PM local; 4 near/red-flag threshold hours. |

## Trend Intelligence

- Summary: Momentum is steady versus the prior run (May 30 at 5:21 AM MDT); forecast volatility is high and first WATCH-or-higher date is Sun, May 31.
- Momentum: **Steady**
- Forecast volatility: **HIGH** (36/100)
- First WATCH-or-higher PSPS date: Sun, May 31
- Watch-date movement: First WATCH-or-higher PSPS date moved later from Sat, May 30 to Sun, May 31.
- Method: compares current forecast evidence against prior local forecast history.

Notable changes:
- First WATCH-or-higher PSPS date moved later from Sat, May 30 to Sun, May 31.
- Fri, Jun 5: worsening vs prior run; PSPS ELEVATED -> WATCH; score +4, wind +1 mph, RH 0%, red-flag hours 0.
- Thu, Jun 4: easing vs prior run; PSPS ELEVATED -> ELEVATED; score -14, wind 0 mph, RH 0%, red-flag hours 0. Driver shifted to Ignacio / southeast La Plata County.

## Public Analysis Export

- Summary: Highest LPEA PSPS concern is Mon, Jun 1 near Pagosa Springs (LIKELY 97/100), driven by red-flag wind/gust signal near 25 mph; very dry RH near 10%; 3 sampled hours meet red-flag screen.
- Trend: Momentum is steady versus the prior run (May 30 at 5:21 AM MDT); forecast volatility is high and first WATCH-or-higher date is Sun, May 31.
- Confidence: **MEDIUM** (68/100)
- First WATCH-or-higher PSPS date: Sun, May 31
- PSPS peak: Mon, Jun 1 near Pagosa Springs at LIKELY 97/100
- Red Flag peak: Mon, Jun 1 near Durango / La Plata County at LIKELY 81/100
- Fire danger peak: Mon, Jun 1 near Durango / La Plata County at EXTREME 86/100
- Public JSON: `archuleta_red_flag_monitor/public_analysis_export.json`

What changed:
- First WATCH-or-higher PSPS date moved later from Sat, May 30 to Sun, May 31.
- Fri, Jun 5: worsening vs prior run; PSPS ELEVATED -> WATCH; score +4, wind +1 mph, RH 0%, red-flag hours 0.
- Thu, Jun 4: easing vs prior run; PSPS ELEVATED -> ELEVATED; score -14, wind 0 mph, RH 0%, red-flag hours 0. Driver shifted to Ignacio / southeast La Plata County.

What to watch next:
- Check whether the largest day-level changes line up with wind/RH movement or public-source context.
- Check whether the LPEA active match is still a broad red-flag banner rather than direct PSPS/outage intent.
- Watch whether the highest-risk locations remain consistent across runs or the driver area is moving.
- If a PSPS occurs, log the confirmed date, location, and source so future hit-rate scoring can improve.

## PSPS Likelihood

- **PSPS means Public Safety Power Shutoff:** a planned, safety-related power shutoff LPEA may use during dangerous fire-weather conditions to reduce wildfire ignition risk. See [LPEA PSPS guidance](https://lpea.coop/psps) and the [LPEA outage center](https://lpea.coop/outage-center); if power is out, also check the [LPEA outage map](https://outage.lpea.coop).
- Overall: **LIKELY** - PSPS likelihood is high on weather-driven red-flag days; prepare for possible LPEA safety-related interruption behavior.
- Likely PSPS watch dates: Mon, Jun 1
- PSPS watch dates: Sun, May 31; Tue, Jun 2; Fri, Jun 5; Sat, Jun 6
- LPEA signal basis: LPEA active/update source contains red-flag, wildfire, or power-interruption language.
- Note: This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

| Date | PSPS likelihood | Driver locations | Weather basis |
| --- | --- | --- | --- |
| Sun, May 31 | WATCH | Durango / La Plata County (WATCH 52/100); Piedra / north county (WATCH 48/100); Bayfield / east La Plata County (WATCH 48/100); Ignacio / southeast La Plata County (WATCH 48/100) | Top weather score 52/100 at Durango / La Plata County. Weather score 52/100: RH 11%, wind/gust 22 mph, red-flag hours 0, near-threshold hours 4. |
| Mon, Jun 1 | LIKELY | Pagosa Springs (LIKELY 67/100); Bayfield / east La Plata County (LIKELY 67/100); Durango / La Plata County (WATCH 64/100); Ignacio / southeast La Plata County (WATCH 64/100) | Top weather score 67/100 at Pagosa Springs. Weather score 67/100: RH 10%, wind/gust 25 mph, red-flag hours 3, near-threshold hours 6. |
| Tue, Jun 2 | WATCH | Bayfield / east La Plata County (WATCH 56/100); Ignacio / southeast La Plata County (WATCH 56/100); Arboles / southwest county (WATCH 52/100); Chimney Rock / west county (WATCH 52/100) | Top weather score 56/100 at Bayfield / east La Plata County. Weather score 56/100: RH 11%, wind/gust 22 mph, red-flag hours 0, near-threshold hours 4. |
| Wed, Jun 3 | ELEVATED | Arboles / southwest county (ELEVATED 18/100); Chimney Rock / west county (ELEVATED 18/100); Durango / La Plata County (ELEVATED 18/100) | Top weather score 18/100 at Arboles / southwest county. Weather score 18/100: RH 21%, wind/gust 16 mph, red-flag hours 0, near-threshold hours 0. |
| Thu, Jun 4 | ELEVATED | Ignacio / southeast La Plata County (ELEVATED 28/100); Chimney Rock / west county (ELEVATED 27/100); Durango / La Plata County (ELEVATED 24/100) | Top weather score 28/100 at Ignacio / southeast La Plata County. Weather score 28/100: RH 17%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 1. |
| Fri, Jun 5 | WATCH | Durango / La Plata County (WATCH 48/100); Bayfield / east La Plata County (WATCH 48/100); Ignacio / southeast La Plata County (WATCH 48/100) | Top weather score 48/100 at Durango / La Plata County. Weather score 48/100: RH 13%, wind/gust 23 mph, red-flag hours 0, near-threshold hours 5. |
| Sat, Jun 6 | WATCH | Arboles / southwest county (WATCH 52/100); Chimney Rock / west county (WATCH 52/100); Durango / La Plata County (WATCH 52/100); Ignacio / southeast La Plata County (WATCH 52/100) | Top weather score 52/100 at Arboles / southwest county. Weather score 52/100: RH 12%, wind/gust 22 mph, red-flag hours 0, near-threshold hours 4. |

## Area-Specific Outlook

| Area | Today | Peak this run | Highest-risk window |
| --- | --- | --- | --- |
| Pagosa Springs | ELEVATED 44/100 | Mon, Jun 1: LIKELY 67/100 | 1 PM-6 PM local; 6 near/red-flag threshold hours. |
| Bayfield | WATCH 48/100 | Mon, Jun 1: LIKELY 67/100 | 1 PM-6 PM local; 6 near/red-flag threshold hours. |
| Durango | WATCH 52/100 | Mon, Jun 1: WATCH 64/100 | 12 PM-6 PM local; 7 near/red-flag threshold hours. |
| Ignacio | WATCH 48/100 | Mon, Jun 1: WATCH 64/100 | 1 PM-6 PM local; 6 near/red-flag threshold hours. |
| Piedra | WATCH 48/100 | Mon, Jun 1: WATCH 61/100 | 12 PM-6 PM local; 7 near/red-flag threshold hours. |
| Arboles | ELEVATED 30/100 | Mon, Jun 1: WATCH 55/100 | 1 PM-6 PM local; 6 near/red-flag threshold hours. |
| Chimney Rock | ELEVATED 30/100 | Mon, Jun 1: WATCH 55/100 | 1 PM-6 PM local; 6 near/red-flag threshold hours. |
| Chromo | ELEVATED 26/100 | Mon, Jun 1: WATCH 52/100 | 1 PM-6 PM local; 6 near/red-flag threshold hours. |

## Fire Posture + Restrictions

- Summary: 2 official sources indicate fire restrictions or staged restrictions.
- Max restriction stage detected: STAGE 1
- Max fire danger detected: VERY HIGH
- Sources reachable: 6/7
- Note: Official-source status check only; verify restrictions and burn decisions with the responsible jurisdiction.

| Jurisdiction | Restrictions | Fire danger | Source |
| --- | --- | --- | --- |
| Archuleta County | UNKNOWN | UNKNOWN | [Archuleta County Sheriff fire updates](https://sheriff.archuletacounty.gov/divisions/emergency-operations/fire-updates-and-information/) |
| Pagosa Springs | UNKNOWN | UNKNOWN | [Town of Pagosa Springs](https://www.pagosasprings.co.gov/) |
| San Juan National Forest | STAGE 1 | VERY HIGH | [San Juan National Forest fire](https://www.fs.usda.gov/r02/sanjuan/fire) |
| BLM Tres Rios | STAGE 1 | UNKNOWN | [BLM Tres Rios Field Office](https://www.blm.gov/office/tres-rios-field-office) |
| La Plata County / Durango Fire | UNKNOWN | UNKNOWN | [Durango Fire & Rescue fire conditions](https://www.durangofire.org/fire-conditions) |
| Durango | UNKNOWN | UNKNOWN | [City of Durango](https://www.durangoco.gov/) |
| Southern Ute / Ignacio | UNKNOWN | UNKNOWN | [Southern Ute Indian Tribe](https://www.southernute-nsn.gov/) |

## Forecast Calibration

- Summary: No confirmed LPEA PSPS events logged yet; calibration will start once events are added.
- Confirmed PSPS events logged: 0
- Candidate/unconfirmed events logged: 0
- WATCH/LIKELY false-watch past days: 3
- Pending WATCH/LIKELY dates in current forecast: Sun, May 31; Mon, Jun 1; Tue, Jun 2; Fri, Jun 5; Sat, Jun 6
- Calibration source: manual PSPS event log plus forecast history from prior monitor runs.

## Official Weather Alerts

- Monitored NWS zones: COC007, COC067, COZ019, COZ022, COZ023, COZ295
- No active official NWS Red Flag / Fire Weather or related weather alerts found for monitored zones.

## LPEA Power Signal

- Status: `active_keyword_match` - LPEA active/update sources contained power-interruption keywords; review source before treating as confirmed outage intent.
- Meaning: Active source match means a monitored LPEA active/update source currently contains fire, outage, PSPS, or power-interruption keywords. It is a watch cue for review, not a confirmed outage or shutoff notice.
- Source coverage: 13 sources; 5/5 official social sources reachable
- Evidence quality: 0 operational, 3 active/update, 1 archive/context, 4 reference source matches.
- Active/update source pages with matches: LPEA homepage (red flag, public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation); LPEA latest news (red flag, public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation); LPEA news releases (red flag, wildfire, public safety power shutoff, power shutoff, shutoff, power outage); LPEA LinkedIn (wildfire, public safety power shutoff, power shutoff, shutoff)
- Distinct active/update signals: Site-wide red flag banner across 3 sources: LPEA homepage, LPEA latest news, and LPEA news releases (red flag, public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation); News-release archive PSPS item (red flag, wildfire, public safety power shutoff, power shutoff, shutoff, power outage); LinkedIn wildfire preparedness post (wildfire, public safety power shutoff, power shutoff, shutoff); LinkedIn PSPS explainer post (wildfire, public safety power shutoff, power shutoff, shutoff)
- Example signal: Site-wide LPEA banner: Red Flag Warnings are in place across the service territory; LPEA links members to outage-impact guidance.
- Reference/context hits: [LPEA outage center](https://lpea.coop/outage-center); [LPEA wildfire / public safety power shutoffs](https://lpea.coop/psps); [LPEA red flag outage impact page](https://lpea.coop/outages/red-flag-warnings-and-impact-outages-prioritizing-safety-our-members); [LPEA fire mitigation](https://lpea.coop/fire-mitigation)

**Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## Next 7 Days

| Date | Tier | Main reason | Worst sampled metrics |
| --- | --- | --- | --- |
| Sun, May 31 | CONCERN | Pagosa Springs: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Pagosa Springs: RH 13%, wind/gust 22 mph, thunder 0%<br>Arboles / southwest county: RH 10%, wind/gust 20 mph, thunder 0%<br>Chimney Rock / west county: RH 9%, wind/gust 20 mph, thunder 0% |
| Mon, Jun 1 | HIGH | Pagosa Springs: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 10%, wind/gust 25 mph, thunder 0%<br>Arboles / southwest county: RH 8%, wind/gust 24 mph, thunder 0%<br>Chimney Rock / west county: RH 7%, wind/gust 23 mph, thunder 0% |
| Tue, Jun 2 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Pagosa Springs: RH 13%, wind/gust 20 mph, thunder 20%<br>Arboles / southwest county: RH 10%, wind/gust 21 mph, thunder 16%<br>Chimney Rock / west county: RH 9%, wind/gust 21 mph, thunder 18% |
| Wed, Jun 3 | ELEVATED | Pagosa Springs: Elevated ingredient present: thunder probability reaches 47%. | Pagosa Springs: RH 25%, wind/gust 13 mph, thunder 47%<br>Arboles / southwest county: RH 21%, wind/gust 16 mph, thunder 33%<br>Chimney Rock / west county: RH 19%, wind/gust 16 mph, thunder 42% |
| Thu, Jun 4 | CONCERN | Chimney Rock / west county: Dry-thunder signal: thunder probability reaches 20% with low precipitation probability. | Pagosa Springs: RH 22%, wind/gust 16 mph, thunder 33%<br>Chimney Rock / west county: RH 16%, wind/gust 17 mph, thunder 20%<br>Piedra / north county: RH 26%, wind/gust 16 mph, thunder 41% |
| Fri, Jun 5 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Pagosa Springs: RH 17%, wind/gust 17 mph, thunder 24%<br>Arboles / southwest county: RH 13%, wind/gust 21 mph, thunder 11%<br>Chimney Rock / west county: RH 12%, wind/gust 18 mph, thunder 18% |
| Sat, Jun 6 | CONCERN | Pagosa Springs: Dry-thunder signal: thunder probability reaches 20% with low precipitation probability. | Pagosa Springs: RH 15%, wind/gust 21 mph, thunder 20%<br>Arboles / southwest county: RH 12%, wind/gust 22 mph, thunder 9%<br>Chimney Rock / west county: RH 11%, wind/gust 21 mph, thunder 17% |

## Sample Point Status

- Pagosa Springs: COZ295 (matches), forecast zone COZ023, county zone COC007
- Arboles / southwest county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Chimney Rock / west county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Piedra / north county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Chromo / southeast county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Durango / La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Bayfield / east La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Ignacio / southeast La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
