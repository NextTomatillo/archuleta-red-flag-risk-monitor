# Archuleta Red Flag Risk Monitor

Generated: Jun 6, 2026 at 9:59 AM MDT (Pagosa Springs, CO local time)
Next update: Jun 6, 2026 at 10:59 AM MDT (Pagosa Springs, CO local time)
Date/time basis: Pagosa Springs, CO local time (America/Denver)
> **Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## At A Glance

- Overall tier: **HIGH**
- PSPS likelihood: **LIKELY**
- PSPS likely dates: Sun, Jun 7; Mon, Jun 8; Tue, Jun 9; Wed, Jun 10; Thu, Jun 11; Fri, Jun 12
- PSPS watch dates: Sat, Jun 6
- Monitor heads-up recommended: **YES** - Send this monitor report because current risk is HIGH. This is not an official LPEA or NWS notice.
- HIGH dates: Sun, Jun 7; Mon, Jun 8; Tue, Jun 9; Wed, Jun 10; Thu, Jun 11; Fri, Jun 12
- CONCERN dates: Sat, Jun 6
- ELEVATED dates: None
- Official NWS Red Flag / Fire Weather alerts (COZ295): 0
- LPEA signal: `active_keyword_match` - LPEA active/update sources contained power-interruption keywords; review source before treating as confirmed outage intent.
- LPEA source coverage: 13 sources; 5/5 official social sources reachable
- NWS discussion: NWS discussion contains fire-weather concern language.

## Decision Support

- Summary: Highest LPEA PSPS concern is Sun, Jun 7 near Arboles / southwest county (LIKELY 100/100), driven by red-flag wind/gust signal near 29 mph; very dry RH near 12%; 8 sampled hours meet red-flag screen.
- Confidence: **HIGH** (77/100) - 8/8 sampled weather points available; 7/7 fire-posture sources reachable; official NWS alert zones checked; 13/13 LPEA public sources reachable; LPEA active/update sources checked; no confirmed PSPS events logged yet for calibration
- Fire danger peak: Sun, Jun 7: Durango / La Plata County EXTREME 100/100
- Red Flag likelihood peak: Sun, Jun 7: Durango / La Plata County LIKELY 100/100
- LPEA PSPS peak: Sun, Jun 7: Arboles / southwest county LIKELY 100/100
- Method: rules-based decision support using public weather, fire-posture, and LPEA source signals; scores are screening estimates, not official or statistically calibrated probabilities.

| Date | Fire danger | Red Flag likelihood | LPEA PSPS | Main window |
| --- | --- | --- | --- | --- |
| Sat, Jun 6 | Bayfield / east La Plata County: VERY HIGH 80/100 | Bayfield / east La Plata County: WATCH 71/100 | Bayfield / east La Plata County: LIKELY 85/100 | 3 PM-7 PM local; 5 near/red-flag threshold hours. |
| Sun, Jun 7 | Durango / La Plata County: EXTREME 100/100 | Durango / La Plata County: LIKELY 100/100 | Arboles / southwest county: LIKELY 100/100 | 12 PM-8 PM local; 9 near/red-flag threshold hours. |
| Mon, Jun 8 | Ignacio / southeast La Plata County: EXTREME 100/100 | Ignacio / southeast La Plata County: LIKELY 100/100 | Pagosa Springs: LIKELY 100/100 | 12 PM-7 PM local; 8 near/red-flag threshold hours. |
| Tue, Jun 9 | Arboles / southwest county: EXTREME 100/100 | Arboles / southwest county: LIKELY 100/100 | Arboles / southwest county: LIKELY 100/100 | 12 PM-9 PM local; 10 near/red-flag threshold hours. |
| Wed, Jun 10 | Pagosa Springs: EXTREME 100/100 | Pagosa Springs: LIKELY 100/100 | Pagosa Springs: LIKELY 100/100 | 12 PM-8 PM local; 9 near/red-flag threshold hours. |
| Thu, Jun 11 | Pagosa Springs: EXTREME 100/100 | Pagosa Springs: LIKELY 100/100 | Pagosa Springs: LIKELY 100/100 | 11 AM-8 PM local; 10 near/red-flag threshold hours. |
| Fri, Jun 12 | Pagosa Springs: EXTREME 100/100 | Pagosa Springs: LIKELY 100/100 | Pagosa Springs: LIKELY 100/100 | 11 AM-8 PM local; 10 near/red-flag threshold hours. |

## Trend Intelligence

- Summary: Momentum is steady versus the prior run (Jun 5 at 11:38 PM MDT); forecast volatility is low and first WATCH-or-higher date is Sat, Jun 6.
- Momentum: **Steady**
- Forecast volatility: **LOW** (10/100)
- First WATCH-or-higher PSPS date: Sat, Jun 6
- Watch-date movement: First WATCH-or-higher PSPS date remains Sat, Jun 6.
- Method: compares current forecast evidence against prior local forecast history.

Notable changes:
- First WATCH-or-higher PSPS date remains Sat, Jun 6.
- Tue, Jun 9: worsening vs prior run; PSPS LIKELY -> LIKELY; score 0, wind 0 mph, RH 0%, red-flag hours +4.
- Wed, Jun 10: easing vs prior run; PSPS LIKELY -> LIKELY; score 0, wind -4 mph, RH 0%, red-flag hours -2. Driver shifted to Durango / La Plata County.

## Public Analysis Export

- Summary: Highest LPEA PSPS concern is Sun, Jun 7 near Arboles / southwest county (LIKELY 100/100), driven by red-flag wind/gust signal near 29 mph; very dry RH near 12%; 8 sampled hours meet red-flag screen.
- Trend: Momentum is steady versus the prior run (Jun 5 at 11:38 PM MDT); forecast volatility is low and first WATCH-or-higher date is Sat, Jun 6.
- Confidence: **HIGH** (77/100)
- First WATCH-or-higher PSPS date: Sat, Jun 6
- PSPS peak: Sun, Jun 7 near Arboles / southwest county at LIKELY 100/100
- Red Flag peak: Sun, Jun 7 near Durango / La Plata County at LIKELY 100/100
- Fire danger peak: Sun, Jun 7 near Durango / La Plata County at EXTREME 100/100
- LPEA operational outage context: No monitored active LPEA source currently describes a non-PSPS outage.
- Public JSON: `archuleta_red_flag_monitor/public_analysis_export.json`

What changed:
- First WATCH-or-higher PSPS date remains Sat, Jun 6.
- Tue, Jun 9: worsening vs prior run; PSPS LIKELY -> LIKELY; score 0, wind 0 mph, RH 0%, red-flag hours +4.
- Wed, Jun 10: easing vs prior run; PSPS LIKELY -> LIKELY; score 0, wind -4 mph, RH 0%, red-flag hours -2. Driver shifted to Durango / La Plata County.

What to watch next:
- Check whether the largest day-level changes line up with wind/RH movement or public-source context.
- Check whether the LPEA active match is still a broad red-flag banner rather than direct PSPS/outage intent.
- Watch whether the highest-risk locations remain consistent across runs or the driver area is moving.
- If a PSPS occurs, log the confirmed date, location, and source so future hit-rate scoring can improve.

## PSPS Likelihood

- **PSPS means Public Safety Power Shutoff:** a planned, safety-related power shutoff LPEA may use during dangerous fire-weather conditions to reduce wildfire ignition risk. See [LPEA PSPS guidance](https://lpea.coop/psps) and the [LPEA outage center](https://lpea.coop/outage-center); if power is out, also check the [LPEA outage map](https://outage.lpea.coop).
- Overall: **LIKELY** - PSPS likelihood is high on weather-driven red-flag days; prepare for possible LPEA safety-related interruption behavior.
- Likely PSPS watch dates: Sun, Jun 7; Mon, Jun 8; Tue, Jun 9; Wed, Jun 10; Thu, Jun 11; Fri, Jun 12
- PSPS watch dates: Sat, Jun 6
- LPEA signal basis: LPEA active/update source contains red-flag, wildfire, or power-interruption language.
- Note: This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

| Date | PSPS likelihood | Driver locations | Weather basis |
| --- | --- | --- | --- |
| Sat, Jun 6 | WATCH | Bayfield / east La Plata County (WATCH 61/100); Ignacio / southeast La Plata County (WATCH 61/100); Arboles / southwest county (WATCH 52/100); Durango / La Plata County (WATCH 52/100) | Top weather score 61/100 at Bayfield / east La Plata County. Weather score 61/100: RH 11%, wind/gust 25 mph, red-flag hours 1, near-threshold hours 5. |
| Sun, Jun 7 | LIKELY | Durango / La Plata County (LIKELY 77/100); Ignacio / southeast La Plata County (LIKELY 77/100); Bayfield / east La Plata County (LIKELY 73/100); Arboles / southwest county (LIKELY 71/100) | Top weather score 77/100 at Durango / La Plata County. Weather score 77/100: RH 12%, wind/gust 32 mph, red-flag hours 8, near-threshold hours 10. |
| Mon, Jun 8 | LIKELY | Ignacio / southeast La Plata County (LIKELY 77/100); Pagosa Springs (LIKELY 71/100); Arboles / southwest county (LIKELY 71/100); Chimney Rock / west county (LIKELY 71/100) | Top weather score 77/100 at Ignacio / southeast La Plata County. Weather score 77/100: RH 10%, wind/gust 31 mph, red-flag hours 7, near-threshold hours 10. |
| Tue, Jun 9 | LIKELY | Chimney Rock / west county (LIKELY 85/100); Ignacio / southeast La Plata County (LIKELY 85/100); Arboles / southwest county (LIKELY 81/100); Durango / La Plata County (LIKELY 81/100) | Top weather score 85/100 at Chimney Rock / west county. Weather score 85/100: RH 12%, wind/gust 40 mph, red-flag hours 10, near-threshold hours 12. |
| Wed, Jun 10 | LIKELY | Durango / La Plata County (LIKELY 81/100); Bayfield / east La Plata County (LIKELY 81/100); Ignacio / southeast La Plata County (LIKELY 81/100); Pagosa Springs (LIKELY 77/100) | Top weather score 81/100 at Durango / La Plata County. Weather score 81/100: RH 11%, wind/gust 38 mph, red-flag hours 9, near-threshold hours 11. |
| Thu, Jun 11 | LIKELY | Durango / La Plata County (LIKELY 81/100); Bayfield / east La Plata County (LIKELY 81/100); Ignacio / southeast La Plata County (LIKELY 81/100); Chimney Rock / west county (LIKELY 80/100) | Top weather score 81/100 at Durango / La Plata County. Weather score 81/100: RH 10%, wind/gust 37 mph, red-flag hours 9, near-threshold hours 11. |
| Fri, Jun 12 | LIKELY | Pagosa Springs (LIKELY 77/100); Durango / La Plata County (LIKELY 77/100); Bayfield / east La Plata County (LIKELY 77/100); Ignacio / southeast La Plata County (LIKELY 77/100) | Top weather score 77/100 at Pagosa Springs. Weather score 77/100: RH 11%, wind/gust 31 mph, red-flag hours 7, near-threshold hours 10. |

## Area-Specific Outlook

| Area | Today | Peak this run | Highest-risk window |
| --- | --- | --- | --- |
| Chimney Rock | WATCH 48/100 | Tue, Jun 9: LIKELY 85/100 | 11 AM-10 PM local; 12 near/red-flag threshold hours. |
| Ignacio | WATCH 61/100 | Tue, Jun 9: LIKELY 85/100 | 12 PM-9 PM local; 10 near/red-flag threshold hours. |
| Arboles | WATCH 52/100 | Tue, Jun 9: LIKELY 81/100 | 12 PM-9 PM local; 10 near/red-flag threshold hours. |
| Durango | WATCH 52/100 | Tue, Jun 9: LIKELY 81/100 | 12 PM-10 PM local; 11 near/red-flag threshold hours. |
| Bayfield | WATCH 61/100 | Tue, Jun 9: LIKELY 81/100 | 12 PM-9 PM local; 10 near/red-flag threshold hours. |
| Pagosa Springs | ELEVATED 26/100 | Wed, Jun 10: LIKELY 77/100 | 12 PM-8 PM local; 9 near/red-flag threshold hours. |
| Chromo | ELEVATED 20/100 | Thu, Jun 11: LIKELY 77/100 | 12 PM-8 PM local; 9 near/red-flag threshold hours. |
| Piedra | ELEVATED 20/100 | Wed, Jun 10: LIKELY 73/100 | 1 PM-7 PM local; 7 near/red-flag threshold hours. |

## Fire Posture + Restrictions

- Summary: 4 official sources indicate fire restrictions or staged restrictions.
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
| Southern Ute / Ignacio | UNKNOWN | UNKNOWN | [Southern Ute Indian Tribe](https://www.southernute-nsn.gov/) |

## Forecast Calibration

- Summary: No confirmed LPEA PSPS events logged yet; calibration will start once events are added.
- Confirmed PSPS events logged: 0
- Candidate/unconfirmed events logged: 0
- WATCH/LIKELY false-watch past days: 8
- Pending WATCH/LIKELY dates in current forecast: Sat, Jun 6; Sun, Jun 7; Mon, Jun 8; Tue, Jun 9; Wed, Jun 10; Thu, Jun 11; Fri, Jun 12
- Calibration source: manual PSPS event log plus forecast history from prior monitor runs.

## Official Weather Alerts

- Monitored NWS zones: COC007, COC067, COZ019, COZ022, COZ023, COZ295
- No active official NWS Red Flag / Fire Weather or related weather alerts found for monitored zones.

## LPEA Power Signal

- Status: `active_keyword_match` - LPEA active/update sources contained power-interruption keywords; review source before treating as confirmed outage intent.
- Meaning: Active source match means a monitored LPEA active/update source currently contains fire, outage, PSPS, or power-interruption keywords. Operational outages are shown separately and are not treated as PSPS/fire evidence unless the source text says so.
- Operational outage context: No monitored active LPEA source currently describes a non-PSPS outage.
- Source coverage: 13 sources; 5/5 official social sources reachable
- Evidence quality: 0 operational, 3 active/update, 1 archive/context, 4 reference source matches.
- Active/update source pages with matches: LPEA homepage (red flag, public safety power shutoff, power shutoff, shutoff, power outage, outage map); LPEA latest news (red flag, public safety power shutoff, power shutoff, shutoff, power outage, outage map); LPEA news releases (red flag, wildfire, public safety power shutoff, power shutoff, shutoff, power outage); LPEA LinkedIn (wildfire, public safety power shutoff, power shutoff, shutoff)
- Distinct active/update signals: Shared signal across 3 sources across 3 sources: LPEA homepage, LPEA latest news, and LPEA news releases (red flag, public safety power shutoff, power shutoff, shutoff, power outage, outage map); News-release archive PSPS item (red flag, wildfire, public safety power shutoff, power shutoff, shutoff, power outage); LinkedIn wildfire preparedness post (wildfire, public safety power shutoff, power shutoff, shutoff); LinkedIn PSPS explainer post (wildfire, public safety power shutoff, power shutoff, shutoff)
- Example signal: ...ngs & Resources Board Committees Voting Districts Policies & Bylaws Elections A Red Flag Warning will be in effect from Noon - 10 PM Saturday, June 6. Follow our Facebook for updates. View Outage Map. Previou...
- Reference/context hits: [LPEA outage center](https://lpea.coop/outage-center); [LPEA wildfire / public safety power shutoffs](https://lpea.coop/psps); [LPEA red flag outage impact page](https://lpea.coop/outages/red-flag-warnings-and-impact-outages-prioritizing-safety-our-members); [LPEA fire mitigation](https://lpea.coop/fire-mitigation)

**Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## Next 7 Days

| Date | Tier | Main reason | Worst sampled metrics |
| --- | --- | --- | --- |
| Sat, Jun 6 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Pagosa Springs: RH 15%, wind/gust 20 mph, thunder 5%<br>Arboles / southwest county: RH 10%, wind/gust 23 mph, thunder 1%<br>Chimney Rock / west county: RH 10%, wind/gust 22 mph, thunder 3% |
| Sun, Jun 7 | HIGH | Pagosa Springs: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 14%, wind/gust 29 mph, thunder 1%<br>Arboles / southwest county: RH 12%, wind/gust 29 mph, thunder 1%<br>Chimney Rock / west county: RH 10%, wind/gust 29 mph, thunder 0% |
| Mon, Jun 8 | HIGH | Pagosa Springs: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 12%, wind/gust 30 mph, thunder 7%<br>Arboles / southwest county: RH 10%, wind/gust 29 mph, thunder 5%<br>Chimney Rock / west county: RH 9%, wind/gust 28 mph, thunder 6% |
| Tue, Jun 9 | HIGH | Arboles / southwest county: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 16%, wind/gust 41 mph, thunder 22%<br>Arboles / southwest county: RH 13%, wind/gust 39 mph, thunder 16%<br>Chimney Rock / west county: RH 12%, wind/gust 40 mph, thunder 19% |
| Wed, Jun 10 | HIGH | Pagosa Springs: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 13%, wind/gust 38 mph, thunder 1%<br>Arboles / southwest county: RH 10%, wind/gust 34 mph, thunder 1%<br>Chimney Rock / west county: RH 9%, wind/gust 33 mph, thunder 1% |
| Thu, Jun 11 | HIGH | Pagosa Springs: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 11%, wind/gust 34 mph, thunder 3%<br>Arboles / southwest county: RH 9%, wind/gust 33 mph, thunder 2%<br>Chimney Rock / west county: RH 8%, wind/gust 32 mph, thunder 3% |
| Fri, Jun 12 | HIGH | Pagosa Springs: Forecast meets red-flag screen: RH <= 15% and wind/gust >= 25 mph for at least 3 hours in a 12-hour window. | Pagosa Springs: RH 11%, wind/gust 31 mph, thunder 4%<br>Arboles / southwest county: RH 9%, wind/gust 30 mph, thunder 3%<br>Chimney Rock / west county: RH 8%, wind/gust 29 mph, thunder 3% |

## Sample Point Status

- Pagosa Springs: COZ295 (matches), forecast zone COZ023, county zone COC007
- Arboles / southwest county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Chimney Rock / west county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Piedra / north county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Chromo / southeast county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Durango / La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Bayfield / east La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Ignacio / southeast La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
