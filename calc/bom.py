"""Parts list by phase (parts only, no labor). Prices researched 2026-10-06; (low, high) USD.
Phase 1 = power the kitchen now. Phase 2 = expand the same system for the future house (priced at today's prices)."""
import csv, sys
TAX = 0.08265  # Washoe County sales tax
CONTINGENCY = 0.10
PHASES = {1: "Phase 1: Kitchen", 2: "Phase 2: House expansion"}
BOM = [
 # (phase, category, item, qty, unit_low, unit_high, notes)
 (1, "Generation", "440 W bifacial N-type panels (1 pallet of 36 = 15.84 kW)", 36, 125, 155, "~$0.28-0.35/W new pallet. Used panels only worth it under ~$0.15/W (more panels = more racking)."),
 (1, "Generation", "Ground mount, DIY galvanized pipe + rails, 2 rows of 18, 45-50 deg tilt", 1, 3500, 5500, "Lay out the rows so Phase 2 rows extend in line."),
 (1, "Generation", "Concrete for footings", 1, 600, 1000, ""),
 (1, "Power conversion", "EG4 6000XP off-grid inverter (6 kW out, 8 kW PV, 125 A charge)", 2, 1450, 1630, "Paralleled = 12 kW split-phase, 24 kW surge, redundancy."),
 (1, "Storage", "EG4 WallMount Indoor 14.3 kWh 48 V LiFePO4 (heated, UL9540A)", 3, 3110, 3450, "42.9 kWh. A 4th unit (+$3.1-3.5k) is the first upgrade if the generator runs more than expected."),
 (1, "Storage", "Battery cables / busbar / Class T fuse", 1, 400, 700, "Busbar sized for Phase 2 battery count."),
 (1, "Backup", "Generac Guardian 24 kW (7209, no transfer switch), propane", 1, 6000, 6730, "Shared by both phases. Used 20-24 kW units often $2.5-4.5k locally. Needs a start relay."),
 (1, "Backup", "Generator pad + start relay + 60 A gen feeder wire", 1, 400, 700, "Propane line by a licensed gas fitter not included."),
 (1, "Balance of system", "PV wire, MC4, string fusing, DC surge protector, conduit array->shed (~100 ft)", 1, 800, 1300, ""),
 (1, "Balance of system", "Shed AC combining panel, breakers, AC surge protector", 1, 500, 900, "Combines inverter outputs and the gen input."),
 (1, "Balance of system", "100 A feeder shed->kitchen, 2-2-2-4 Al, conduit (~100 ft)", 1, 600, 1000, "Separate building = 4-wire feeder + its own ground rods."),
 (1, "Balance of system", "Grounding: rods, bonding, array equipment ground", 1, 200, 350, ""),
 (1, "Balance of system", "Trencher rental (2 days)", 1, 600, 900, ""),
 (1, "Balance of system", "Empty conduit toward the house site, laid while the trench is open", 1, 150, 400, "Only if the house location is known. Saves re-trenching in Phase 2."),
 (1, "Structure", "10x12 insulated power shed, sized for Phase 2 (DIY build)", 1, 3000, 4800, "~$500-800 more than 8x10 now; avoids a second shed later."),
 (1, "Soft costs", "Freight (panel pallet + batteries)", 1, 400, 900, ""),
 (1, "Soft costs", "Washoe County permits + stamped ground-mount structural letter", 1, 1000, 2500, "Confirm with Washoe County Building."),

 (2, "Generation", "440 W bifacial panels, 2nd pallet (36 = 15.84 kW; 31.7 kW total)", 36, 125, 155, ""),
 (2, "Generation", "Ground mount extension + concrete", 1, 4100, 6500, ""),
 (2, "Power conversion", "EG4 6000XP, 2 more in parallel (4 total = 24 kW)", 2, 1450, 1630, "Matches the 24 kW generator."),
 (2, "Storage", "EG4 WallMount Indoor 14.3 kWh, 3 more (6 total = 85.8 kWh)", 3, 3110, 3450, ""),
 (2, "Storage", "Battery cables for added units", 1, 300, 500, ""),
 (2, "Balance of system", "PV wire, MC4, fusing, DC surge protector for new strings", 1, 800, 1300, ""),
 (2, "Balance of system", "Shed distribution panel upgrade + house feeder breaker", 1, 800, 1500, ""),
 (2, "Balance of system", "Feeder shed->house, 4/0 Al, ~150 ft (pull through Phase 1 conduit)", 1, 1200, 2000, "Distance is a placeholder."),
 (2, "Balance of system", "Trencher rental (if Phase 1 conduit was not laid)", 1, 0, 900, ""),
 (2, "Soft costs", "Freight", 1, 400, 900, ""),
 (2, "Soft costs", "Permit revision + structural letter for added rows", 1, 800, 2000, ""),
]

def totals(phase):
    lo = sum(q*l for p, _c, _i, q, l, _h, _n in BOM if p == phase)
    hi = sum(q*h for p, _c, _i, q, _l, h, _n in BOM if p == phase)
    tlo, thi = lo*TAX, hi*TAX
    clo, chi = (lo+tlo)*CONTINGENCY, (hi+thi)*CONTINGENCY
    return dict(lo=lo, hi=hi, tlo=tlo, thi=thi, clo=clo, chi=chi, glo=lo+tlo+clo, ghi=hi+thi+chi)

def main(out_csv=None):
    for ph, name in PHASES.items():
        print(f"\n## {name}\n\n| Category | Item | Qty | Unit | Total | Notes |\n|---|---|---:|---:|---:|---|")
        for p, c, i, q, l, h, n in BOM:
            if p == ph: print(f"| {c} | {i} | {q} | ${l:,}-{h:,} | ${q*l:,}-{q*h:,} | {n} |")
        t = totals(ph)
        print(f"| | **Subtotal** | | | **${t['lo']:,.0f}-{t['hi']:,.0f}** | |")
        print(f"| | Sales tax 8.265% | | | ${t['tlo']:,.0f}-{t['thi']:,.0f} | |")
        print(f"| | Contingency 10% | | | ${t['clo']:,.0f}-{t['chi']:,.0f} | |")
        print(f"| | **{name} total (parts only)** | | | **${t['glo']:,.0f}-{t['ghi']:,.0f}** | |")
    a, b = totals(1), totals(2)
    print(f"\n**Both phases: ${a['glo']+b['glo']:,.0f}-{a['ghi']+b['ghi']:,.0f}** (Phase 2 at today's prices)")
    if out_csv:
        with open(out_csv, "w", newline="") as f:
            w = csv.writer(f); w.writerow(["Phase","Category","Item","Qty","Unit low","Unit high","Total low","Total high","Notes"])
            w.writerows((p, c, i, q, l, h, q*l, q*h, n) for p, c, i, q, l, h, n in BOM)

if __name__ == "__main__": main(sys.argv[1] if len(sys.argv) > 1 else None)
