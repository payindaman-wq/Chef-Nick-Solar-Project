# Site Conditions and Design Basis

Confirmed 2026-10-06.

- **Location:** 1739 Dixie Ln, Reno, NV 89510 (rural north Washoe County).
- **Grid:** none. **Fully off-grid.** No utility, no net metering, no interconnection agreement.
- **Water:** private well being drilled week of 2026-10-06. Well pump becomes a load.
- **Backup:** Generac 24 kW. With no natural gas on site, fuel is assumed **propane** (to confirm).

## Design implications
1. **Winter sizing.** Off-grid systems are sized for the worst month (December), not the annual average.
   North Reno is roughly 1,700-1,800 kWh per kW of panels per year, but December gives about a third of the June output.
   Mount panels steep (45-50 degrees) to favor winter. Exact monthly figures from NREL PVWatts are still to run (the API was not reachable from this machine).
2. **Generator role.** It becomes the planned winter / cloudy-stretch charging source, not just emergency backup. Air-cooled
   Generac Guardian units are standby-rated, so runtime hours, oil-change intervals and propane use go into the operating plan.
   The inverter needs a 2-wire auto-start signal to the generator.
3. **Propane for heat loads.** Off-grid, every kWh costs battery and panels. Propane burners and a propane tankless water heater
   remove the two biggest electric loads. Strong recommendation unless Nick is set on electric.
4. **Well pump.** Submersible pumps (typically 1-2 HP, 240 V) have a 3-6x start-up surge. The inverter must handle the surge,
   or use a soft-start or variable-speed pump (e.g., Grundfos SQ-type). Pump HP and depth are needed.
5. **Cold.** Reno winter lows in the teens F; LiFePO4 cannot charge below 32 F. Batteries go in a conditioned/insulated space
   or a heated battery model is used.
6. **Wind/snow.** North valleys get strong wind. Racking must meet Washoe County wind/snow design loads; ground mounts need
   engineered footings.
7. **Permits.** Washoe County Building for the PV/electrical work; the kitchen side also needs the Washoe County Health District
   (food establishment, and potentially well/water-system approval for a food business).
8. **Tax:** off-grid commercial equipment may be depreciable as a business asset; check with a CPA.
