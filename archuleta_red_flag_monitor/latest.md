# Archuleta County fire-weather monitor

Generated: Aug 22, 2026 at 9:29 AM MDT (Pagosa Springs, CO local time)
Next update: Aug 22, 2026 at 5:20 PM MDT (Pagosa Springs, CO local time)
Date/time basis: Pagosa Springs, CO local time (America/Denver)
> **Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## At A Glance

- Fire-weather tier: **CONCERN**
- PSPS likelihood: **WATCH**
- PSPS likely dates: None
- PSPS watch dates: Tue, Aug 25; Wed, Aug 26; Thu, Aug 27; Fri, Aug 28
- Monitor heads-up recommended: **YES** - Send this monitor report because fire-weather screening tier is CONCERN; PSPS screening level is WATCH; a material current wildfire is reported in Archuleta County. This is not an official LPEA or NWS notice.
- HIGH dates: None
- CONCERN dates: Mon, Aug 24; Tue, Aug 25; Wed, Aug 26; Thu, Aug 27; Fri, Aug 28
- ELEVATED dates: None
- Official NWS Red Flag / Fire Weather alerts (COZ295): 0
- LPEA signal: `operational_outage_active` - Official LPEA outage data indicates an operational outage; use as grid context, not PSPS/fire evidence unless LPEA identifies that cause.
- LPEA source coverage: 13 sources; 5/5 official social sources reachable
- Current Archuleta County wildfires: 2
- Official evacuation notices: No current evacuation order or warning detected in the checked official county feeds.
- NWS discussion: No concerning fire-weather language found in latest GJT discussion.

## Decision Support

- Summary: Highest LPEA PSPS concern is Fri, Aug 28 near Bayfield / east La Plata County (WATCH 63/100), driven by red-flag wind/gust signal near 25 mph; very dry RH near 12%; 6 sampled hours are near red-flag thresholds. NIFC reports 2 current wildfires in Archuleta County.
- Confidence: **HIGH** (77/100) - 8/8 sampled weather points available; 7/7 fire-posture sources reachable; official NWS alert zones checked; 13/13 LPEA public sources reachable; LPEA active/update sources checked; active LPEA operational outage context checked separately from PSPS scoring; authoritative NIFC current-incident feed checked for Archuleta County; official Archuleta County evacuation feeds checked; no confirmed PSPS events logged yet for calibration
- Weather fire-potential peak: Fri, Aug 28: Bayfield / east La Plata County VERY HIGH 82/100
- Red Flag likelihood peak: Fri, Aug 28: Bayfield / east La Plata County WATCH 74/100
- LPEA PSPS peak: Fri, Aug 28: Bayfield / east La Plata County WATCH 63/100
- Method: rules-based decision support using public weather, fire-posture, and LPEA source signals; scores are screening estimates, not official or statistically calibrated probabilities.

| Date | Weather fire potential | Red Flag likelihood | LPEA PSPS | Main window |
| --- | --- | --- | --- | --- |
| Sat, Aug 22 | Pagosa Springs: LOW 32/100 | Pagosa Springs: LOW 0/100 | Pagosa Springs: ELEVATED 18/100 | Peak ingredients near 3 PM local; RH 22%, wind 18 mph. |
| Sun, Aug 23 | Durango / La Plata County: MODERATE 38/100 | Arboles / southwest county: LOW 8/100 | Arboles / southwest county: ELEVATED 24/100 | Peak ingredients near 3 PM local; RH 19%, wind 22 mph. |
| Mon, Aug 24 | Arboles / southwest county: HIGH 55/100 | Arboles / southwest county: POSSIBLE 50/100 | Arboles / southwest county: ELEVATED 40/100 | 3 PM-5 PM local; 3 near/red-flag threshold hours. |
| Tue, Aug 25 | Chimney Rock / west county: VERY HIGH 72/100 | Chimney Rock / west county: WATCH 57/100 | Chimney Rock / west county: WATCH 50/100 | 3 PM-4 PM local; 2 near/red-flag threshold hours. |
| Wed, Aug 26 | Durango / La Plata County: HIGH 64/100 | Ignacio / southeast La Plata County: WATCH 61/100 | Ignacio / southeast La Plata County: WATCH 51/100 | 2 PM-6 PM local; 5 near/red-flag threshold hours. |
| Thu, Aug 27 | Durango / La Plata County: VERY HIGH 74/100 | Durango / La Plata County: WATCH 61/100 | Arboles / southwest county: WATCH 50/100 | 3 PM-6 PM local; 4 near/red-flag threshold hours. |
| Fri, Aug 28 | Bayfield / east La Plata County: VERY HIGH 82/100 | Bayfield / east La Plata County: WATCH 74/100 | Bayfield / east La Plata County: WATCH 63/100 | 2 PM-7 PM local; 6 near/red-flag threshold hours. |

## Analyst Interpretation

- Headline: PSPS screening remains WATCH Aug 25-28, peaking Friday near Bayfield; no official COZ295 alert or fire-related LPEA outage is reported.
- Summary: PSPS screening is unchanged at WATCH Tue, Aug 25 through Fri, Aug 28; these are screening estimates, not LPEA shutoff notices. Friday peaks near Bayfield at WATCH 63/100, with red-flag screening WATCH 74/100 and weather fire potential VERY HIGH 82/100. Official COZ295 alerts remain at zero; LPEA lists two localized one-customer outages with no fire or PSPS cause, and no evacuation notice was detected for the two listed wildfires.
- Uncertainty: Confidence is HIGH 77/100 because source coverage is complete and the forecast is steady, but PSPS calibration has no confirmed events and Friday's forecast may still change.
- Evidence used: overall_status, weather_peaks, official_alerts, forecast_change, lpea_context, fire_posture, active_incidents, calibration
- This interpretation cannot change the deterministic tiers, scores, official alerts, or notification decision.

Changing drivers:
- The first WATCH-or-higher PSPS date remains Tuesday, Aug 25, with no major day-level movement versus the prior run.
- Friday remains the peak near Bayfield at WATCH 63/100, with RH near 12%, wind near 25 mph, and 6 near-threshold hours.
- Current official-source fire posture includes Stage 2 restrictions and VERY HIGH fire danger.
- Two current wildfires are listed in Archuleta County, with no evacuation notice detected in the checked official feeds.

What to watch next:
- Recheck the Aug 25-28 WATCH window after the next forecast update, especially Tuesday's first signal near Chimney Rock.
- Monitor Friday afternoon near Bayfield, where the current PSPS, red-flag, and weather fire-potential peaks align.
- Treat both one-customer LPEA outages as operational context only unless LPEA identifies a fire or PSPS cause.
- Continue official NWS, incident, and evacuation checks; COZ295 alerts are zero and no evacuation notice was detected.

## Trend Intelligence

- Summary: Momentum is steady versus the prior run (Aug 22 at 4:15 AM MDT); forecast volatility is low and first WATCH-or-higher date is Tue, Aug 25.
- Momentum: **Steady**
- Forecast volatility: **LOW** (0/100)
- First WATCH-or-higher PSPS date: Tue, Aug 25
- Watch-date movement: First WATCH-or-higher PSPS date remains Tue, Aug 25.
- Method: compares current forecast evidence against prior local forecast history.

Notable changes:
- First WATCH-or-higher PSPS date remains Tue, Aug 25.
- No major day-level movement versus the prior run.

## Public Analysis Export

- Summary: Highest LPEA PSPS concern is Fri, Aug 28 near Bayfield / east La Plata County (WATCH 63/100), driven by red-flag wind/gust signal near 25 mph; very dry RH near 12%; 6 sampled hours are near red-flag thresholds. NIFC reports 2 current wildfires in Archuleta County.
- Trend: Momentum is steady versus the prior run (Aug 22 at 4:15 AM MDT); forecast volatility is low and first WATCH-or-higher date is Tue, Aug 25.
- Confidence: **HIGH** (77/100)
- First WATCH-or-higher PSPS date: Tue, Aug 25
- PSPS peak: Fri, Aug 28 near Bayfield / east La Plata County at WATCH 63/100
- Red Flag peak: Fri, Aug 28 near Bayfield / east La Plata County at WATCH 74/100
- Weather fire-potential peak: Fri, Aug 28 near Bayfield / east La Plata County at VERY HIGH 82/100
- LPEA operational outage context: 2 active outages; 0 planned and 2 unplanned; 2 customers out. No fire-weather or PSPS cause is identified.
- Public JSON: `archuleta_red_flag_monitor/public_analysis_export.json`

What changed:
- First WATCH-or-higher PSPS date remains Tue, Aug 25.
- No major day-level movement versus the prior run.

What to watch next:
- Check whether the largest day-level changes line up with wind/RH movement or public-source context.
- Check whether the LPEA active match is still a broad red-flag banner rather than direct PSPS/outage intent.
- Watch whether the highest-risk locations remain consistent across runs or the driver area is moving.
- If a PSPS occurs, log the confirmed date, location, and source so future hit-rate scoring can improve.

## PSPS Likelihood

- **PSPS means Public Safety Power Shutoff:** a planned, safety-related power shutoff LPEA may use during dangerous fire-weather conditions to reduce wildfire ignition risk. See [LPEA PSPS guidance](https://lpea.coop/psps) and the [LPEA outage center](https://lpea.coop/outage-center); if power is out, also check the [LPEA outage map](https://outage.lpea.coop).
- Overall: **WATCH** - PSPS watch screening is present from forecast thresholds or direct LPEA shutoff language; monitor official LPEA and NWS updates.
- Likely PSPS watch dates: None
- PSPS watch dates: Tue, Aug 25; Wed, Aug 26; Thu, Aug 27; Fri, Aug 28
- LPEA signal basis: LPEA active/update source contains red-flag, wildfire, or power-interruption language.
- Note: This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

| Date | PSPS likelihood | Driver locations | Weather basis |
| --- | --- | --- | --- |
| Sat, Aug 22 | ELEVATED | Pagosa Springs (ELEVATED 18/100); Arboles / southwest county (LOW 16/100); Chimney Rock / west county (LOW 16/100) | Top weather score 14/100 at Pagosa Springs. Weather score 14/100: RH 22%, wind/gust 18 mph, red-flag hours 0, near-threshold hours 0. |
| Sun, Aug 23 | ELEVATED | Arboles / southwest county (ELEVATED 24/100); Durango / La Plata County (ELEVATED 24/100); Ignacio / southeast La Plata County (ELEVATED 22/100) | Top weather score 22/100 at Arboles / southwest county. Weather score 22/100: RH 19%, wind/gust 22 mph, red-flag hours 0, near-threshold hours 0. |
| Mon, Aug 24 | ELEVATED | Arboles / southwest county (ELEVATED 40/100); Ignacio / southeast La Plata County (ELEVATED 28/100); Durango / La Plata County (ELEVATED 24/100) | Top weather score 38/100 at Arboles / southwest county. Weather score 38/100: RH 17%, wind/gust 22 mph, red-flag hours 0, near-threshold hours 3. |
| Tue, Aug 25 | WATCH | Chimney Rock / west county (WATCH 50/100); Ignacio / southeast La Plata County (WATCH 47/100) | Top weather score 48/100 at Chimney Rock / west county. Weather score 48/100: RH 15%, wind/gust 21 mph, red-flag hours 0, near-threshold hours 2. |
| Wed, Aug 26 | WATCH | Ignacio / southeast La Plata County (WATCH 51/100); Arboles / southwest county (WATCH 50/100) | Top weather score 51/100 at Ignacio / southeast La Plata County. Weather score 51/100: RH 16%, wind/gust 25 mph, red-flag hours 0, near-threshold hours 5. |
| Thu, Aug 27 | WATCH | Arboles / southwest county (WATCH 50/100); Chimney Rock / west county (WATCH 50/100); Durango / La Plata County (WATCH 50/100); Bayfield / east La Plata County (WATCH 50/100) | Top weather score 48/100 at Arboles / southwest county. Weather score 48/100: RH 13%, wind/gust 23 mph, red-flag hours 0, near-threshold hours 4. |
| Fri, Aug 28 | WATCH | Bayfield / east La Plata County (WATCH 63/100); Ignacio / southeast La Plata County (WATCH 61/100); Arboles / southwest county (WATCH 54/100); Chimney Rock / west county (WATCH 54/100) | Top weather score 61/100 at Bayfield / east La Plata County. Weather score 61/100: RH 12%, wind/gust 25 mph, red-flag hours 2, near-threshold hours 6. |

## Area-Specific Outlook

| Area | Today | Peak this run | Highest-risk window |
| --- | --- | --- | --- |
| Bayfield | LOW 10/100 | Fri, Aug 28: WATCH 63/100 | 2 PM-7 PM local; 6 near/red-flag threshold hours. |
| Ignacio | LOW 14/100 | Fri, Aug 28: WATCH 61/100 | 2 PM-7 PM local; 6 near/red-flag threshold hours. |
| Arboles | LOW 16/100 | Fri, Aug 28: WATCH 54/100 | 3 PM-6 PM local; 4 near/red-flag threshold hours. |
| Chimney Rock | LOW 16/100 | Fri, Aug 28: WATCH 54/100 | 3 PM-6 PM local; 4 near/red-flag threshold hours. |
| Durango | LOW 16/100 | Fri, Aug 28: WATCH 54/100 | 2 PM-6 PM local; 5 near/red-flag threshold hours. |
| Pagosa Springs | ELEVATED 18/100 | Fri, Aug 28: WATCH 48/100 | 3 PM-5 PM local; 3 near/red-flag threshold hours. |
| Chromo | LOW 2/100 | Fri, Aug 28: WATCH 46/100 | 4 PM-5 PM local; 2 near/red-flag threshold hours. |
| Piedra | LOW 10/100 | Fri, Aug 28: ELEVATED 28/100 | Peak ingredients near 4 PM local; RH 16%, wind 20 mph. |

## Current Fires + Evacuations

- Incident summary: 2 current wildfires reported in Archuleta County; no current evacuation notice detected in checked county feeds.
- Evacuation status: **NONE DETECTED** - No current evacuation order or warning detected in the checked official county feeds.
- Safety note: Current incidents and evacuation notices are operational context. They do not raise PSPS scores by themselves; follow official evacuation instructions immediately.

### Current NIFC Incidents

| Incident | Type | Size | Containment | Nearest monitored area | Updated |
| --- | --- | --- | --- | --- | --- |
| Rio Blanco | Wildfire | 1,387.74 acres | 100% | Chromo / southeast county (9.9 mi) | Aug 18 at 7:20 PM MDT |
| Swiss Roll | Wildfire | 0.25 acres | Not reported | Pagosa Springs (14.5 mi) | Aug 21 at 2:06 PM MDT |

Official links: [NIFC map](https://www.nifc.gov/fire-information/maps), [Archuleta County fire updates](https://sheriff.archuletacounty.gov/divisions/emergency-operations/fire-updates-and-information/), [County alerts](https://nixle.us/archuleta-county-office-of-emergency-management-aux/), [Watch Duty](https://app.watchduty.org/)

## Fire Posture + Restrictions

- Summary: 3 official sources indicate fire restrictions or staged restrictions.
- Max restriction stage detected: STAGE 2
- Max fire danger detected: VERY HIGH
- Sources reachable: 7/7
- Note: Official-source status check only; verify restrictions and burn decisions with the responsible jurisdiction.

| Jurisdiction | Restrictions | Fire danger | Source |
| --- | --- | --- | --- |
| Archuleta County | STAGE 1 | UNKNOWN | [Archuleta County Sheriff fire updates](https://sheriff.archuletacounty.gov/divisions/emergency-operations/fire-updates-and-information/) |
| Pagosa Springs | STAGE 2 | UNKNOWN | [Town of Pagosa Springs](https://www.pagosasprings.co.gov/) |
| San Juan National Forest | STAGE 1 | VERY HIGH | [San Juan National Forest fire](https://www.fs.usda.gov/r02/sanjuan/fire) |
| BLM Tres Rios | UNKNOWN | UNKNOWN | [BLM Tres Rios Field Office](https://www.blm.gov/office/tres-rios-field-office) |
| La Plata County / Durango Fire | NONE | UNKNOWN | [Durango Fire & Rescue fire conditions](https://www.durangofire.org/fire-conditions) |
| Durango | UNKNOWN | UNKNOWN | [City of Durango](https://www.durangoco.gov/) |
| Southern Ute / Ignacio | UNKNOWN | UNKNOWN | [Southern Ute Indian Tribe](https://www.southernute-nsn.gov/) |

## Forecast Calibration

### PSPS Calibration

- Summary: No confirmed LPEA PSPS events logged yet; calibration will start once events are added.
- Confirmed PSPS events logged: 0
- Candidate/unconfirmed events logged: 0
- WATCH/LIKELY false-watch past days: 62
- Pending WATCH/LIKELY dates in current forecast: Tue, Aug 25; Wed, Aug 26; Thu, Aug 27; Fri, Aug 28
- Calibration source: manual PSPS event log plus forecast history from prior monitor runs.

### Red Flag / Fire Weather Calibration

- Summary: 3/3 official Red Flag / Fire Weather episodes had a pre-alert HIGH monitor signal; date-level result was 21/21. Episode-average lead time: 3.5 days.
- Official alert episodes logged: 3 (21 alert dates)
- Episode-level pre-alert HIGH hit rate: 100%
- Date-level pre-alert HIGH hit rate: 100%
- Episode-level average lead time: 3.5 days
- HIGH false-watch past days: 21
- Pending HIGH dates in current forecast: None
- Calibration source: official NWS Red Flag / Fire Weather alert dates plus forecast history from prior monitor runs.

## Official Weather Alerts

- Monitored NWS zones: COC007, COC067, COZ019, COZ022, COZ023, COZ295
- No active official NWS Red Flag / Fire Weather or related weather alerts found for monitored zones.

## LPEA Power Signal

- Status: `operational_outage_active` - Official LPEA outage data indicates an operational outage; use as grid context, not PSPS/fire evidence unless LPEA identifies that cause.
- Meaning: Active source match means a monitored LPEA active/update source currently contains fire, outage, PSPS, or power-interruption keywords. Operational outages are shown separately and are not treated as PSPS/fire evidence unless the source text says so.
- Operational outage context: 2 active outages; 0 planned and 2 unplanned; 2 customers out. No fire-weather or PSPS cause is identified.
- Source coverage: 13 sources; 5/5 official social sources reachable
- Evidence quality: 0 operational, 4 active/update, 0 archive/context, 6 reference source matches.
- Operational outage source links: [288 ANIMAS VIEW DR #21](https://outage.lpea.coop); [740 COUNTY RD 382](https://outage.lpea.coop)
- Active/update source pages with matches: LPEA homepage (public safety power shutoff, power shutoff, shutoff, power outage, fire mitigation, restoration); LPEA X (power outage, outage map, high winds, restore power); LPEA LinkedIn (wildfire, public safety power shutoff, psps, power shutoff, shutoff, deenergize)
- Distinct active/update signals: LPEA X (power outage, outage map, high winds, restore power); LPEA X (power outage, outage map, high winds, restore power); LPEA LinkedIn (wildfire, public safety power shutoff, psps, power shutoff, shutoff, deenergize); LinkedIn PSPS explainer post (wildfire, public safety power shutoff, psps, power shutoff, shutoff, deenergize)
- Example signal: ...ibrary! 1 2 536 LPEA @LaPlataElectric May 7, 2024 LPEA members are experiencing power outages in the Bayfield and Pagosa Springs areas. Approximately 200 meters are out and it is suspected that the high winds are...
- Reference/context hits: [LPEA outage center](https://lpea.coop/outage-center); [LPEA wildfire / public safety power shutoffs](https://lpea.coop/psps); [LPEA red flag outage impact page](https://lpea.coop/outages/red-flag-warnings-and-impact-outages-prioritizing-safety-our-members); [LPEA fire mitigation](https://lpea.coop/fire-mitigation); [LPEA latest news](https://lpea.coop/Posts)

**Unofficial monitor:** This is not an official forecast, National Weather Service warning, LPEA outage notice, or LPEA Public Safety Power Shutoff notice. Confirm conditions and safety decisions with NWS and LPEA.

## Next 7 Days

| Date | Tier | Main reason | Worst sampled metrics |
| --- | --- | --- | --- |
| Sat, Aug 22 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 22%, wind/gust 18 mph, thunder 26%<br>Arboles / southwest county: RH 20%, wind/gust 20 mph, thunder 20%<br>Chimney Rock / west county: RH 19%, wind/gust 18 mph, thunder 21% |
| Sun, Aug 23 | GREEN | No notable red-flag ingredients across sampled county points. | Pagosa Springs: RH 26%, wind/gust 20 mph, thunder 34%<br>Arboles / southwest county: RH 19%, wind/gust 22 mph, thunder 12%<br>Chimney Rock / west county: RH 18%, wind/gust 20 mph, thunder 24% |
| Mon, Aug 24 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 17%, wind/gust 22 mph, thunder 4% |
| Tue, Aug 25 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 16%, wind/gust 24 mph, thunder 7%<br>Chimney Rock / west county: RH 15%, wind/gust 21 mph, thunder 16%<br>Ignacio / southeast La Plata County: RH 17%, wind/gust 25 mph, thunder 9% |
| Wed, Aug 26 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Arboles / southwest county: RH 14%, wind/gust 23 mph, thunder 7%<br>Chimney Rock / west county: RH 14%, wind/gust 20 mph, thunder 12%<br>Chromo / southeast county: RH 17%, wind/gust 18 mph, thunder 16% |
| Thu, Aug 27 | CONCERN | Arboles / southwest county: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Pagosa Springs: RH 18%, wind/gust 18 mph, thunder 17%<br>Arboles / southwest county: RH 13%, wind/gust 23 mph, thunder 6%<br>Chimney Rock / west county: RH 12%, wind/gust 21 mph, thunder 11% |
| Fri, Aug 28 | CONCERN | Pagosa Springs: Near red-flag screen: RH <= 18% with wind/gust >= 20 mph for at least 2 hours. | Pagosa Springs: RH 14%, wind/gust 22 mph, thunder 8%<br>Arboles / southwest county: RH 10%, wind/gust 24 mph, thunder 5%<br>Chimney Rock / west county: RH 10%, wind/gust 23 mph, thunder 7% |

## Sample Point Status

- Pagosa Springs: COZ295 (matches), forecast zone COZ023, county zone COC007
- Arboles / southwest county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Chimney Rock / west county: COZ295 (matches), forecast zone COZ023, county zone COC007
- Piedra / north county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Chromo / southeast county: COZ295 (matches), forecast zone COZ019, county zone COC007
- Durango / La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Bayfield / east La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
- Ignacio / southeast La Plata County: COZ295 (matches), forecast zone COZ022, county zone COC067
