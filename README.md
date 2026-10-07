# Chef Nick Solar Project

Solar + battery + generator system for Chef Nick's 560 sq ft workshop/kitchen, designed to expand to a future ~2,000 sq ft house on the same property.

## Known facts
- Existing 560 sq ft structure, converting to workshop/kitchen
- New 100 A panel being installed (240 V split-phase assumed)
- Generac 24 kW standby generator for no-sun periods
- Future 2,000 sq ft house planned next to the kitchen

## Phases
1. **Intake** - collect site, load, and equipment data (`docs/01-intake-questionnaire.md`)
2. **Load calc + sizing** - daily kWh, peak kW, autonomy, array/battery/inverter sizing
3. **Architecture decision** - one expandable system vs two systems
4. **Schematic** - one-line diagram for presentation to Nick
5. **BOM + quote** - parts list with estimated costs, labor, contingency
6. **Permitting + install plan**

## Status
- 2026-10-06: Repo created, intake questionnaire drafted.
- 2026-10-06: Site walkthrough, off-grid design basis, preliminary load calc + sizing (docs/04). Architecture: one central expandable system. 
- 2026-10-06: Incentives research (docs/07-incentives.md). PAUSED: waiting on Nick's answers to docs/06-questions-for-nick.md, then update calc/load_calc.py + calc/bom.py, run calc/build_page.py, republish.
- 2026-10-06: BOM split into Phase 1 (kitchen) and Phase 2 (house); questions for Nick in docs/06-questions-for-nick.md.
- 2026-10-06: EG4 parts-only BOM (docs/05-bom.md, bom.csv), one-line schematic (site/schematic.svg), proposal page (site/index.html, rebuild with `python calc/build_page.py`). Published: https://claude.ai/artifact/C2YyRvJhQ2ShejyRCWfYSW
