"""Questions for Nick (meeting checklist). Used by build_page.py and written to docs/06-questions-for-nick.md."""
QUESTIONS = [
 ("Business and schedule", [
  "What kind of food business is this (catering, commissary, restaurant prep, classes)? Have you talked to the Washoe County Health District yet?",
  "Days per week and hours per day the kitchen will run? Busiest time of day? Any seasonal swings?",
  "When do you need power in the kitchen? Target opening date?",
  "Is there a general contractor or licensed electrician on the kitchen build? (They may need to sign off on the solar too.)",
 ]),
 ("Kitchen equipment", [
  "Fridge and freezer: reach-in or chest, how many doors? Any plans for a walk-in? Models if picked.",
  "Hood: length, fan size, is make-up air required? Fire suppression system?",
  "Cooking: propane burners confirmed. Any electric ovens (convection, combi), fryer or griddle?",
  "Dishwasher, ice machine, espresso machine, proofer, sous vide, dehydrator, electric smoker?",
  "Heating and cooling: mini-split, propane heater, or both? Is AC wanted in summer?",
  "Shop tools: welder, air compressor, table saw? Anything on 240 V?",
  "What must never lose power (freezer, fridge, anything else)?",
 ]),
 ("Well and water", [
  "Well depth and pump horsepower once the driller knows? Can the driller install a soft-start pump (Grundfos SQ type)?",
  "Pressure tank only, or a storage tank/cistern too?",
  "Will the well also serve irrigation, animals, or the future house?",
 ]),
 ("Propane and generator", [
  "OK to upsize to a 500 gal tank, or add a separate tank for the generator? Leased or owned? Which supplier?",
  "Who will run the gas lines (licensed gas fitter)?",
  "Buy the generator used to save $2-4k, or new with a warranty?",
  "Where should the generator sit for noise: how far from the kitchen and the future house?",
 ]),
 ("Site layout", [
  "Where can the panels go? Each Phase 1 pallet needs an unshaded area of roughly 70 x 35 ft facing south. Phase 2 needs about the same again.",
  "Where should the power shed go? Distance from shed to kitchen, and shed to the future house?",
  "Where are the septic tank, leach field and well, so trenches avoid them?",
  "Anything that could shade the array later (trees, a barn, the house itself)?",
  "Any deed or HOA restrictions on solar or outbuildings?",
 ]),
 ("Future house", [
  "When will the house be built? How many bedrooms and square feet?",
  "Propane for cooking, water heating and heat, or all-electric/heat pump?",
  "Any EV charging, pool, hot tub, or large shop planned? (Each changes Phase 2 size a lot.)",
  "Should we lay empty conduit toward the house site now while the trench is open?",
 ]),
 ("Budget and logistics", [
  "Budget for Phase 1? OK to start with 3 batteries and add a 4th later?",
  "Who pays vendors: Nick directly, or through me?",
  "Delivery: can a freight truck reach the site? Is there a forklift or tractor to unload a ~1,500 lb panel pallet?",
  "Internet or cell signal at the site (for remote system monitoring)?",
 ]),
]

def markdown():
    out = ["# Questions for Nick", "", "Meeting checklist. Answers update the load calc (`calc/load_calc.py`) and parts list (`calc/bom.py`).", ""]
    n = 1
    for group, qs in QUESTIONS:
        out += [f"## {group}", ""]
        for q in qs:
            out.append(f"{n}. {q}"); n += 1
        out.append("")
    return "\n".join(out)
