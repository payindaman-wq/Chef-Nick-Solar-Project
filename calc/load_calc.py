"""Phase 1 load calc + sizing for Chef Nick's off-grid kitchen. Edit LOADS as real nameplate data arrives."""
# name: (running watts, hours/day, duty cycle, surge watts)
LOADS = {
    "Hood exhaust fan (~1/2 HP)":        (600, 8, 1.0, 1800),
    "Reach-in fridge, 2-door":           (500, 24, 0.40, 1500),
    "Reach-in freezer, 2-door":          (700, 24, 0.45, 2100),
    "Well pump (1.5 HP submersible)":    (1500, 1, 1.0, 7500),
    "Mini-split 18k BTU (cool/heat)":    (1500, 8, 0.65, 1500),
    "LED lighting":                      (300, 10, 1.0, 300),
    "Small appliances (mixer, microwave, etc.)": (1800, 2.5, 1.0, 2500),
    "Shop tools (intermittent)":         (1500, 1.5, 1.0, 4000),
    "Propane tankless WH electronics":   (60, 24, 0.5, 200),
    "Misc plug loads / chargers / Wi-Fi":(100, 24, 1.0, 100),
    "Inverter idle (2x EG4 6000XP @ 60 W)": (120, 24, 1.0, 0),
}
DEC_PSH = 3.8          # est. December peak sun hours at 45-50 deg tilt, north Reno (verify with PVWatts)
SYS_EFF = 0.75         # wiring, temp, MPPT, battery round-trip, soiling/snow
AUTONOMY_DAYS = 1.25   # generator covers anything beyond this
DOD = 0.90

def main():
    rows, total, run_peak, worst_surge = [], 0, 0, 0
    for n, (w, h, duty, surge) in LOADS.items():
        kwh = w * h * duty / 1000; total += kwh; rows.append((n, w, h, duty, kwh))
    run_peak = 600 + 500 + 700 + 1500 + 1500 + 300 + 1800 + 1500 + 160   # realistic coincident peak (everything on)
    worst_surge = run_peak - 1500 + 7500                                   # well pump starting with everything else running
    batt = total * AUTONOMY_DAYS / DOD
    pv = total / (DEC_PSH * SYS_EFF)

    print("| Load | Watts | Hrs/day | Duty | kWh/day |\n|---|---:|---:|---:|---:|")
    for n, w, h, d, k in rows: print(f"| {n} | {w} | {h} | {d:.0%} | {k:.1f} |")
    print(f"| **Total** | | | | **{total:.1f}** |\n")
    print(f"- Coincident running peak: ~{run_peak/1000:.1f} kW")
    print(f"- Worst-case surge (well pump start under full load): ~{worst_surge/1000:.1f} kW")
    print(f"- Battery (usable {AUTONOMY_DAYS} days at {DOD:.0%} DoD): ~{batt:.0f} kWh nameplate")
    print(f"- PV for December break-even ({DEC_PSH} PSH x {SYS_EFF:.0%}): ~{pv:.1f} kW")
    print(f"- Summer surplus at ~7 PSH: ~{pv*7*SYS_EFF - total:.0f} kWh/day unused (headroom for house phase / hot-weather AC)")

if __name__ == "__main__":
    main()
