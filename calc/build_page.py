"""Build site/index.html (proposal page for Nick) from the load calc, BOM and schematic. Run: python calc/build_page.py"""
import html, pathlib
from load_calc import LOADS, DEC_PSH, SYS_EFF
from bom import BOM, TAX, CONTINGENCY

ROOT = pathlib.Path(__file__).resolve().parent.parent
svg = (ROOT / "site" / "schematic.svg").read_text(encoding="utf-8")
e = html.escape

load_rows, total = [], 0
for n, (w, h, d, _s) in LOADS.items():
    k = w * h * d / 1000; total += k
    load_rows.append(f"<tr><td>{e(n)}</td><td class=n>{w:,}</td><td class=n>{h:g}</td><td class=n>{d:.0%}</td><td class=n>{k:.1f}</td></tr>")

bom_rows, lo, hi, cat_prev = [], 0, 0, None
for c, i, q, l, h, note in BOM:
    lo += q * l; hi += q * h
    cat = f"<tr class=cat><th colspan=4>{e(c)}</th></tr>" if c != cat_prev else ""
    cat_prev = c
    bom_rows.append(f"{cat}<tr><td>{e(i)}{'<div class=note>' + e(note) + '</div>' if note else ''}</td>"
                    f"<td class=n>{q}</td><td class=n>${l:,}–{h:,}</td><td class=n>${q*l:,}–{q*h:,}</td></tr>")
tlo, thi = lo * TAX, hi * TAX
clo, chi = (lo + tlo) * CONTINGENCY, (hi + thi) * CONTINGENCY
glo, ghi = lo + tlo + clo, hi + thi + chi
fmt = lambda a, b: f"${a:,.0f}–{b:,.0f}"

page = f"""<title>Chef Nick Off-Grid Power</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Semi+Condensed:wght@500;600;700&family=Source+Sans+3:wght@400;600&family=JetBrains+Mono:wght@400;500&display=swap">
<style>
/* Layout: engineering drawing sheet - title block header, full-width one-line, then spec sheets below */
:root {{
  --bg: #f3f4f1; --paper: #ffffff; --ink: #1d2428; --ink-2: #56626a; --rule: #d3d8d6;
  --sun: #c7740a; --ac: #1f5f8b; --dc: #2b2f33; --pv: #b8322a; --gas: #b98a10; --future: #8a949b; --tint: #fbf3e6;
  --display: "Barlow Semi Condensed", "Arial Narrow", system-ui, sans-serif;
  --body: "Source Sans 3", system-ui, -apple-system, "Segoe UI", sans-serif;
  --mono: "JetBrains Mono", ui-monospace, Consolas, monospace;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
  --bg: #121618; --paper: #1a2023; --ink: #e6eaeb; --ink-2: #9aa7ae; --rule: #313b40;
  --sun: #f0a43a; --ac: #6fb3e3; --dc: #c9d1d5; --pv: #f07468; --gas: #e2bd4b; --future: #6f7a80; --tint: #2a2318; color-scheme: dark }} }}
:root[data-theme="dark"] {{
  --bg: #121618; --paper: #1a2023; --ink: #e6eaeb; --ink-2: #9aa7ae; --rule: #313b40;
  --sun: #f0a43a; --ac: #6fb3e3; --dc: #c9d1d5; --pv: #f07468; --gas: #e2bd4b; --future: #6f7a80; --tint: #2a2318; color-scheme: dark }}
body {{ background: var(--bg); color: var(--ink); font: 16px/1.55 var(--body); }}
.wrap {{ max-width: 1180px; margin: 0 auto; padding-inline: 16px; padding-block: 28px 64px; display: grid; gap: 28px; }}
h1, h2, h3 {{ font-family: var(--display); line-height: 1.15; text-wrap: balance; margin: 0; }}
h1 {{ font-size: clamp(30px, 5vw, 46px); font-weight: 700; letter-spacing: .01em; }}
h2 {{ font-size: 24px; font-weight: 600; }}
h3 {{ font-size: 18px; font-weight: 600; }}
p {{ margin: 0; max-width: 68ch; }}
.eyebrow {{ font: 500 12px/1 var(--mono); letter-spacing: .12em; text-transform: uppercase; color: var(--sun); }}
header.tb {{ display: grid; grid-template-columns: 1fr auto; gap: 16px 32px; align-items: end; border-bottom: 2px solid var(--ink); padding-bottom: 16px; }}
header.tb .lede {{ grid-column: 1 / -1; color: var(--ink-2); }}
dl.block {{ display: grid; grid-template-columns: auto auto; gap: 2px 16px; margin: 0; font: 13px/1.5 var(--mono); }}
dl.block dt {{ color: var(--ink-2); }} dl.block dd {{ margin: 0; }}
section {{ display: grid; gap: 14px; min-width: 0; }}
.sheet {{ background: var(--paper); border: 1px solid var(--rule); border-radius: 6px; padding: 16px; min-width: 0; }}
.scroll {{ overflow-x: auto; }}
svg.oneline {{ display: block; width: 100%; min-width: 860px; height: auto; font-family: var(--body); }}
.zone {{ fill: none; stroke: var(--ink-2); stroke-width: 1.2; stroke-dasharray: 2 4; }}
.zone.k {{ stroke: var(--ink); stroke-dasharray: none; fill: var(--tint); }}
.zlabel {{ font: 600 12px var(--mono); letter-spacing: .1em; fill: var(--ink-2); }}
.box {{ fill: var(--paper); stroke: var(--ink); stroke-width: 1.4; }}
.box.inv {{ stroke: var(--sun); stroke-width: 2; }}
.box.panel {{ stroke: var(--ac); stroke-width: 1.8; }}
.box.gen {{ stroke: var(--gas); stroke-width: 2; }}
.pv rect {{ fill: var(--tint); stroke: var(--sun); stroke-width: 1.6; }}
.cells {{ stroke: var(--sun); stroke-width: .6; opacity: .55; fill: none; }}
.batt rect {{ fill: var(--paper); stroke: var(--dc); stroke-width: 2; }}
.fuse {{ fill: var(--paper); stroke: var(--dc); stroke-width: 1.6; }}
.tank {{ fill: var(--tint); stroke: var(--gas); stroke-width: 1.8; }}
.future {{ fill: none; stroke: var(--future); stroke-width: 1.4; stroke-dasharray: 6 5; }}
.t-b {{ font: 600 14px var(--body); fill: var(--ink); }}
.t-s {{ font: 400 12px var(--body); fill: var(--ink-2); }}
.t-f {{ font: 600 13px var(--body); fill: var(--future); }}
.w-pv, .w-dc, .w-ac, .w-gas, .w-ctl, .w-future {{ fill: none; stroke-linejoin: round; }}
.w-pv {{ stroke: var(--pv); stroke-width: 2.2; }}
.w-dc {{ stroke: var(--dc); stroke-width: 3; }}
.w-ac {{ stroke: var(--ac); stroke-width: 2.6; }}
.w-gas {{ stroke: var(--gas); stroke-width: 2.4; stroke-dasharray: 1 5; stroke-linecap: round; }}
.w-ctl {{ stroke: var(--ink-2); stroke-width: 1.4; stroke-dasharray: 7 4; }}
.w-future {{ stroke: var(--future); stroke-width: 2; stroke-dasharray: 6 5; }}
.specs {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 14px; }}
.spec {{ display: grid; gap: 6px; align-content: start; }}
.spec .big {{ font: 600 28px/1.1 var(--display); color: var(--ink); font-variant-numeric: tabular-nums; }}
.spec .big small {{ font-size: 16px; color: var(--ink-2); font-weight: 500; }}
.spec p {{ font-size: 14.5px; color: var(--ink-2); }}
.spec .label {{ font: 500 11.5px var(--mono); letter-spacing: .1em; text-transform: uppercase; color: var(--sun); }}
table {{ width: 100%; border-collapse: collapse; font-size: 14.5px; font-variant-numeric: tabular-nums; }}
th, td {{ text-align: left; padding: 8px 10px; border-bottom: 1px solid var(--rule); vertical-align: top; }}
thead th {{ font: 500 11.5px var(--mono); letter-spacing: .08em; text-transform: uppercase; color: var(--ink-2); border-bottom: 1.5px solid var(--ink); }}
td.n, th.n {{ text-align: right; white-space: nowrap; }}
tr.cat th {{ font: 600 13px var(--display); letter-spacing: .06em; text-transform: uppercase; color: var(--sun); padding-top: 18px; border-bottom: 1px solid var(--rule); }}
.note {{ font-size: 13px; color: var(--ink-2); margin-top: 2px; }}
tfoot td {{ border-bottom: none; }}
tfoot tr.sub td {{ border-top: 1.5px solid var(--ink); font-weight: 600; }}
tfoot tr.grand td {{ font: 700 20px var(--display); border-top: 2px solid var(--ink); padding-top: 12px; }}
.two {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 28px; }}
ul.plain {{ margin: 0; padding-left: 20px; display: grid; gap: 6px; max-width: 70ch; }}
ul.plain li::marker {{ color: var(--sun); }}
ol.steps {{ margin: 0; padding-left: 22px; display: grid; gap: 6px; }}
.src {{ font-size: 13.5px; color: var(--ink-2); }}
.src a {{ color: var(--ac); }}
a:focus-visible {{ outline: 2px solid var(--sun); outline-offset: 2px; }}
</style>

<div class="wrap">
  <header class="tb">
    <div style="display:grid;gap:10px;min-width:0">
      <span class="eyebrow">Off-grid solar · Phase 1 proposal</span>
      <h1>Chef Nick Kitchen Power System</h1>
    </div>
    <dl class="block">
      <dt>Site</dt><dd>Dixie Ln, Reno NV 89510</dd>
      <dt>Service</dt><dd>Off-grid, no utility</dd>
      <dt>Rev</dt><dd>A · 2026-10-06</dd>
      <dt>Status</dt><dd>Preliminary, for discussion</dd>
    </dl>
    <p class="lede">One central solar, battery and generator system powers the 560 sq ft kitchen now and grows to carry the future house. Panels sit on a ground mount, the electronics live in a small insulated power shed, and a propane generator starts on its own when the batteries run low.</p>
  </header>

  <section>
    <h2>One-line diagram</h2>
    <div class="sheet scroll">{svg}</div>
  </section>

  <section>
    <h2>System at a glance</h2>
    <div class="specs">
      <div class="sheet spec"><span class="label">Solar</span><div class="big">15.84 <small>kW</small></div><p>36 × 440 W bifacial panels, one pallet. Ground mount at 45–50° to favor winter sun and shed snow. Four strings of 9, about 400 V on the coldest morning, under the inverter's 480 V limit.</p></div>
      <div class="sheet spec"><span class="label">Inverters</span><div class="big">12 <small>kW · 24 kW surge</small></div><p>Two EG4 6000XP in parallel, 120/240 V split-phase. If one fails, the other keeps the fridge and freezer running.</p></div>
      <div class="sheet spec"><span class="label">Battery</span><div class="big">42.9 <small>kWh</small></div><p>Three EG4 WallMount Indoor 14.3 kWh LiFePO4 with built-in heaters. Just under one day of kitchen use; the generator covers the rest. A fourth unit (≈1.25 days) is the first upgrade.</p></div>
      <div class="sheet spec"><span class="label">Generator</span><div class="big">24 <small>kW propane</small></div><p>Auto-starts when the battery drops to ~25–30% and charges at up to ~13 kW. Expected mainly in December–January and long storms.</p></div>
    </div>
  </section>

  <section class="two">
    <div style="display:grid;gap:14px;min-width:0">
      <h2>Estimated daily use</h2>
      <p class="src">Appliances are not chosen yet, so these are conservative placeholders. Real nameplate numbers will tighten the sizing.</p>
      <div class="sheet scroll">
        <table>
          <thead><tr><th>Load</th><th class=n>Watts</th><th class=n>Hrs</th><th class=n>Duty</th><th class=n>kWh/day</th></tr></thead>
          <tbody>{''.join(load_rows)}</tbody>
          <tfoot><tr class=sub><td colspan=4>Total</td><td class=n>{total:.1f}</td></tr></tfoot>
        </table>
      </div>
    </div>
    <div style="display:grid;gap:14px;align-content:start;min-width:0">
      <h2>Design decisions</h2>
      <ul class="plain">
        <li><b>One system, not two.</b> One generator, one propane supply and one battery bank serve both buildings. The house adds inverters, batteries and panels to the same shed.</li>
        <li><b>Propane for cooking and hot water.</b> Keeps the two biggest loads off the batteries and roughly halves system cost.</li>
        <li><b>Ground mount.</b> Ideal winter tilt, no roof penetrations on a food business, easy to extend. No rapid-shutdown hardware needed since it is not on a building.</li>
        <li><b>Power shed.</b> Keeps batteries, inverter noise and heat out of the kitchen and above freezing in winter.</li>
        <li><b>Soft-start well pump.</b> A Grundfos SQ-type pump cuts start-up surge from ~7.5 kW to ~2–3 kW.</li>
        <li><b>Upsize propane to 500 gal.</b> A cloudy December week can burn 60–100 gal in the generator on top of cooking.</li>
        <li><b>Winter math.</b> Sized to break even at ~{DEC_PSH} December sun-hours × {SYS_EFF:.0%} efficiency. Summer leaves a large surplus for the house phase.</li>
      </ul>
    </div>
  </section>

  <section>
    <h2>Parts list and estimate</h2>
    <p class="src">Parts only, no labor. EG4 equipment, new; buying used where noted can lower it. Prices researched October 2026.</p>
    <div class="sheet scroll">
      <table>
        <thead><tr><th>Item</th><th class=n>Qty</th><th class=n>Unit</th><th class=n>Total</th></tr></thead>
        <tbody>{''.join(bom_rows)}</tbody>
        <tfoot>
          <tr class=sub><td colspan=3>Subtotal</td><td class=n>{fmt(lo, hi)}</td></tr>
          <tr><td colspan=3>Sales tax, Washoe County 8.265%</td><td class=n>{fmt(tlo, thi)}</td></tr>
          <tr><td colspan=3>Contingency 10%</td><td class=n>{fmt(clo, chi)}</td></tr>
          <tr class=grand><td colspan=3>Estimated parts total</td><td class=n>{fmt(glo, ghi)}</td></tr>
        </tfoot>
      </table>
    </div>
  </section>

  <section class="two">
    <div style="display:grid;gap:14px;align-content:start;min-width:0">
      <h2>Not included</h2>
      <ul class="plain">
        <li>Installation labor, electrician sign-off if the county requires one</li>
        <li>Well, pump and pressure tank (choose a soft-start pump)</li>
        <li>Propane tank, gas lines and gas-fitter labor</li>
        <li>Kitchen wiring past the 100 A panel, appliances, mini-split</li>
        <li>Phase 2 house equipment</li>
      </ul>
    </div>
    <div style="display:grid;gap:14px;align-content:start;min-width:0">
      <h2>Next steps</h2>
      <ol class="steps">
        <li>Pick the array and shed location; measure trench distances.</li>
        <li>Choose fridge, freezer, hood and well pump; update the load table.</li>
        <li>Call Washoe County Building and the Health District about permits and well approval.</li>
        <li>Confirm with Generac that off-grid use keeps the warranty, or source a used unit.</li>
        <li>Order the long-lead items: panels, batteries, inverters.</li>
      </ol>
    </div>
  </section>

  <p class="src">Price sources: <a href="https://signaturesolar.com/eg4-6000xp-off-grid-inverter-split-phase/">EG4 6000XP (Signature Solar)</a> ·
  <a href="https://shopsolarkits.com/products/eg4-wallmount-indoor-lithium-battery">EG4 WallMount Indoor (Shop Solar Kits)</a> ·
  <a href="https://www.generac.com/residential-products/standby-generators/gaseous/24kw-standby-generator-wifi-enabled-7209/">Generac 24 kW 7209</a> ·
  <a href="https://a1solarstore.com/solar-panels.html">pallet panel pricing (A1 SolarStore)</a> ·
  <a href="https://eg4electronics.com/wp-content/uploads/2024/04/EG4-6000XP-Manual.pdf">EG4 6000XP manual</a>.</p>
</div>
"""
(ROOT / "site" / "index.html").write_text(page, encoding="utf-8")
print(f"wrote site/index.html  load {total:.1f} kWh/day  parts {fmt(glo, ghi)}")
