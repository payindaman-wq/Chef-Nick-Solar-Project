"""Phase 1 parts list (parts only, no labor). Prices researched 2026-10-06; (low, high) USD."""
import csv, sys
TAX = 0.08265  # Washoe County sales tax
CONTINGENCY = 0.10
BOM = [
 # (category, item, qty, unit_low, unit_high, notes)
 ("Generation", "440 W bifacial N-type panels (1 pallet of 36 = 15.84 kW)", 36, 125, 155, "~$0.28-0.35/W new pallet. Used panels only worth it under ~$0.15/W (more panels = more racking)."),
 ("Generation", "Ground mount, DIY galvanized pipe + rails, 2 rows of 18, 45-50 deg tilt", 1, 3500, 5500, "Sch40 pipe, clamp fittings, rails, mid/end clamps, module bonding."),
 ("Generation", "Concrete for footings", 1, 600, 1000, ""),
 ("Power conversion", "EG4 6000XP off-grid inverter (6 kW out, 8 kW PV, 125 A charge)", 2, 1450, 1630, "Paralleled = 12 kW split-phase, 24 kW surge, redundancy. Phase 2 adds more."),
 ("Storage", "EG4 WallMount Indoor 14.3 kWh 48 V LiFePO4 (heated, UL9540A)", 3, 3110, 3450, "42.9 kWh to start; 4th unit is the first add (+$3.1-3.5k)."),
 ("Storage", "Battery cables / busbar / Class T fuse", 1, 400, 700, ""),
 ("Backup", "Generac Guardian 24 kW (7209, no transfer switch), propane", 1, 6000, 6730, "Used 20-24 kW units often $2.5-4.5k locally. Needs a utility-sense relay so the inverter can start/stop it."),
 ("Backup", "Generator pad + start relay + 60 A gen feeder wire", 1, 400, 700, "Propane line run by a licensed gas fitter is not included."),
 ("Balance of system", "PV wire, MC4, string fusing, DC surge protector, conduit array->shed (~100 ft)", 1, 800, 1300, ""),
 ("Balance of system", "Shed AC combining panel, breakers, AC surge protector", 1, 500, 900, "Combines both inverter outputs and the gen input."),
 ("Balance of system", "100 A feeder shed->kitchen, 2-2-2-4 Al, conduit (~100 ft)", 1, 600, 1000, "Separate building = 4-wire feeder + its own ground rods."),
 ("Balance of system", "Grounding: rods, bonding, array equipment ground", 1, 200, 350, ""),
 ("Balance of system", "Trencher rental (2 days)", 1, 600, 900, ""),
 ("Structure", "8x10 insulated power shed (DIY build)", 1, 2500, 4000, "Houses inverters + batteries; generator pad beside it."),
 ("Soft costs", "Freight (panel pallet + batteries)", 1, 400, 900, ""),
 ("Soft costs", "Washoe County permits + stamped ground-mount structural letter", 1, 1000, 2500, "Confirm with Washoe County Building."),
]
def main(out_csv=None):
    lo = hi = 0; rows = []
    for c, i, q, l, h, n in BOM:
        rows.append((c, i, q, l, h, q*l, q*h, n)); lo += q*l; hi += q*h
    tlo, thi = lo*TAX, hi*TAX; clo, chi = (lo+tlo)*CONTINGENCY, (hi+thi)*CONTINGENCY
    print("| Category | Item | Qty | Unit | Total | Notes |\n|---|---|---:|---:|---:|---|")
    for c, i, q, l, h, tl, th, n in rows:
        print(f"| {c} | {i} | {q} | ${l:,}-{h:,} | ${tl:,}-{th:,} | {n} |")
    print(f"| | **Subtotal** | | | **${lo:,.0f}-{hi:,.0f}** | |")
    print(f"| | Sales tax 8.265% | | | ${tlo:,.0f}-{thi:,.0f} | |")
    print(f"| | Contingency 10% | | | ${clo:,.0f}-{chi:,.0f} | |")
    print(f"| | **Total (parts only)** | | | **${lo+tlo+clo:,.0f}-{hi+thi+chi:,.0f}** | |")
    if out_csv:
        with open(out_csv, "w", newline="") as f:
            w = csv.writer(f); w.writerow(["Category","Item","Qty","Unit low","Unit high","Total low","Total high","Notes"]); w.writerows(rows)
if __name__ == "__main__": main(sys.argv[1] if len(sys.argv) > 1 else None)
