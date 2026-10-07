# Preliminary Load Calc and System Sizing (Phase 1 - Kitchen)

Draft 2026-10-06. Fridge, freezer, hood, well pump and HVAC are **assumed** (no models chosen yet), on the conservative side.
Regenerate with `python calc/load_calc.py` after editing the load table there.

Confirmed inputs: off-grid, propane burners + propane tankless water heater, 250 gal propane tank, generator not yet purchased,
well being drilled, ground mount acceptable.

## Load table
| Load | Watts | Hrs/day | Duty | kWh/day |
|---|---:|---:|---:|---:|
| Hood exhaust fan (~1/2 HP) | 600 | 8 | 100% | 4.8 |
| Reach-in fridge, 2-door | 500 | 24 | 40% | 4.8 |
| Reach-in freezer, 2-door | 700 | 24 | 45% | 7.6 |
| Well pump (1.5 HP submersible) | 1500 | 1 | 100% | 1.5 |
| Mini-split 18k BTU (cool/heat) | 1500 | 8 | 65% | 7.8 |
| LED lighting | 300 | 10 | 100% | 3.0 |
| Small appliances (mixer, microwave, etc.) | 1800 | 2.5 | 100% | 4.5 |
| Shop tools (intermittent) | 1500 | 1.5 | 100% | 2.2 |
| Propane tankless WH electronics | 60 | 24 | 50% | 0.7 |
| Misc plug loads / chargers / Wi-Fi | 100 | 24 | 100% | 2.4 |
| Inverter self-consumption | 100 | 24 | 100% | 2.4 |
| **Total** | | | | **41.7** |

- Coincident running peak: ~8.6 kW
- Worst-case surge (well pump start under full load): ~14.6 kW
- Battery (usable 1.25 days at 90% DoD): ~58 kWh nameplate
- PV for December break-even (3.8 PSH x 75%): ~14.6 kW
- Summer surplus at ~7 PSH: ~35 kWh/day unused (headroom for house phase / hot-weather AC)

## Recommended Phase 1 system
| Component | Spec | Notes |
|---|---|---|
| PV array | ~15 kW, ground mount, 45-50 deg fixed tilt, due south | Steep tilt favors winter and sheds snow. Leave pad space to extend for the house. Ground mount is not on a building, so rapid-shutdown hardware is not required (NEC 690.12). |
| Inverter | 2 x EG4 6000XP in parallel (12 kW, 24 kW surge, 16 kW PV input) | Chosen 2026-10-06 over one 18kPV: cheaper, off-grid native, redundant. Phase 2 adds more units. |
| Battery | Start with 42.9 kWh (3 x EG4 WallMount Indoor 14.3 kWh), add a 4th for ~57 kWh / 1.25 days | Frugal start chosen 2026-10-06. Generator auto-starts below ~25-30% charge. |
| Generator | 24 kW propane standby (Generac class) | Charges batteries in winter/cloudy stretches. Must accept a 2-wire start signal. Confirm warranty covers off-grid "prime power" use before buying. |
| Power shed | ~10x12 insulated shed (sized for Phase 2) between the kitchen and future house site, small heater to keep batteries above 32 F | Keeps batteries, heat and noise out of the kitchen; becomes the hub for the house in Phase 2. Generator on a pad next to it. |
| Well pump | Soft-start / variable-speed pump (Grundfos SQ type) + pressure tank | Cuts the ~7.5 kW start-up surge to ~2-3 kW, so the inverter doesn't need extra surge headroom. |
| Feeders | PV strings -> shed (high-voltage DC, small wire); 100 A AC feeder shed -> kitchen panel | Trenched in conduit. Short runs keep wire cost down. |

## Propane check
- 250 gal tank holds ~200 gal usable (80% fill).
- Kitchen burners + tankless water heater: a few gallons a day depending on volume.
- A 24 kW generator on propane burns roughly 2.5-3.5 gal/hr at half load. A cloudy December week with 3-4 hr/day of charging = ~60-100 gal.
- **Recommendation: 500 gal tank** (suppliers often lease them), or a separate tank for the generator, so a winter storm doesn't empty the tank mid-service.

## Phase 2 (house) expansion path
Second paralleled inverter, more battery modules, extend the ground array, 200 A feeder from the power shed to the house.
The generator and propane are shared. Size trench/conduit and the shed for this from day one.

## Open items that tighten these numbers
Fridge/freezer/hood models, well pump HP and depth, HVAC plan (mini-split vs propane heat), hours of operation, exact array location.
