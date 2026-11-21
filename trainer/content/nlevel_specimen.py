"""N level exam practice (category 'nlevel'): questions adapted from the SEAB 5148 N(T) Science specimen Paper 1 (2024),
Chapters 1-5 only. Adapted, never copied: contexts kept, numbers changed and varied, picture options turned into words.
Each item names its source under the working."""
from .. import sketches as S, sketches_g1 as G1
from .base import fmt, md_table, nice, numeric_options, pick, register_explain, template, text_options

KP = lambda label, *phr: {"label": label, "any": list(phr)}


def src(n):
    return f"_Adapted from SEAB 5148 specimen paper 2024 Paper 1 Q{n}._"


CAT = "nlevel"


# ---------------------------------------------------------------- varying-number items
@template("n26_lamp_saving_cost", chapter=2, level=4, lo="1.2m", category=CAT)
def lamp_saving_cost(rng):
    Pf = nice(rng, 40, 50, 60, 100)
    Pl = nice(rng, 8, 10, 12)
    hours = nice(rng, 500, 1000, 2000)
    rate = nice(rng, 0.20, 0.25, 0.30)
    saved = (Pf - Pl) / 1000 * hours * rate
    opts, key, mis = numeric_options(rng, saved, [
        (Pf / 1000 * hours * rate, "That is the whole cost of the filament lamp; the saving is the DIFFERENCE between the two lamps."),
        (Pl / 1000 * hours * rate, "That is the cost of the LED lamp, not the money saved."),
        ((Pf - Pl) * hours * rate, "Change the watts to kilowatts before finding kWh."),
    ], unit="$", sf=3, dp=2)
    return dict(
        stem=f"A filament lamp is rated at **{Pf} W**. The equivalent LED lamp is rated at **{Pl} W**. Electricity costs **{money(rate)} per unit (1 kWh)**.\n\n{md_table(['lamp', 'power / W'], [['filament', Pf], ['LED', Pl]])}\n\nHow much money is saved if the LED lamp is used instead of the filament lamp for **{hours} hours**?",
        options=opts, key=key, misconceptions=mis,
        formula="energy (kWh) = kW × h;  cost = kWh × price;  saving = difference in cost",
        working=[f"filament: {Pf / 1000:g} × {hours} = {Pf / 1000 * hours:g} kWh → {money(Pf / 1000 * hours * rate)}", f"LED: {Pl / 1000:g} × {hours} = {Pl / 1000 * hours:g} kWh → {money(Pl / 1000 * hours * rate)}", f"saved = **{money(saved)}**", src(10)],
        hints=["Find the kWh used by each lamp.", "Cost each one, then subtract.", f"Or: ({Pf} − {Pl}) W difference × {hours} h ÷ 1000 × price."],
    )


def money(x):
    return f"${x:,.2f}"


@template("n26_hairdryer_power_energy", chapter=2, level=3, lo="1.2l", category=CAT)
def hairdryer_power_energy(rng):
    V = nice(rng, 230, 240)
    I = nice(rng, 5, 8, 10)
    m = nice(rng, 1, 2, 3)
    P = V * I
    E = P * m * 60
    opts, key, mis = text_options(rng, f"power {P} W, energy {E} J", {
        f"power {P} W, energy {P * m} J": "The time must be in seconds: 1 min = 60 s.",
        f"power {V / I:g} W, energy {V / I * m * 60:g} J": "Power = current × voltage, not voltage ÷ current.",
        f"power {P} W, energy {P * m * 3600} J": "The time is in minutes, not hours: 1 min = 60 s.",
    })
    return dict(
        stem=f"A hair dryer operates on **{V} V** with a current of **{I} A**. It is used for **{m} minute{'s' if m > 1 else ''}**.\n\n{md_table(['voltage / V', 'current / A', 'time'], [[V, I, f'{m} min']])}\n\nWhat is the power of the hair dryer and the energy used?",
        options=opts, key=key, misconceptions=mis,
        formula="power = current × voltage;  energy = power × time (s)",
        working=[f"P = {I} × {V} = {P} W", f"E = {P} × {m * 60} = **{E} J**", src(14)],
        hints=["Power first: current × voltage.", f"Time = {m} × 60 s.", "Energy = power × time."],
    )


@template("n26_toy_car_speed", chapter=4, level=2, lo="1.4e", category=CAT)
def toy_car_speed(rng):
    t = nice(rng, 4, 5, 6, 8)
    d = nice(rng, 12, 15, 20, 24)
    v = d / t
    opts, key, mis = numeric_options(rng, v, [
        (d * t, "Speed = distance ÷ time; do not multiply."),
        (t / d, "Upside down: distance ÷ time."),
        (d, "That is the distance; divide by the time."),
    ], unit="cm/s", sf=3)
    return dict(
        stem=f"A toy car moves in a straight line from point O to point A. A stopwatch starts when the car begins to move.\n\n{md_table(['time from O to A / s', 'distance from O to A / cm'], [[t, d]])}\n\nDetermine the average speed of the car from O to A.",
        options=opts, key=key, misconceptions=mis,
        formula="average speed = distance ÷ time",
        working=[f"speed = {d} ÷ {t}", f"= **{fmt(v)} cm/s**", src(36)],
        hints=["Average speed = distance ÷ time.", f"{d} ÷ {t}.", "cm/s."],
    )


@template("n26_bricks_forces", chapter=4, level=2, lo="1.4c", category=CAT)
def bricks_forces(rng):
    F = nice(rng, 2, 3, 5)
    letters = ["A", "B", "C", "D"]
    rng.shuffle(letters)
    cases = [(letters[0], [("left", F), ("right", F)]), (letters[1], [("left", F), ("up", F)]), (letters[2], [("left", F), ("left", F)]), (letters[3], [("up", F), ("up", F)])]
    cases.sort(key=lambda c: c[0])
    still = letters[0]
    opts, key, mis = text_options(rng, f"brick {still}", {
        f"brick {letters[1]}": "Its two forces act at right angles, so they do not cancel.",
        f"brick {letters[2]}": "Its two forces act the same way and add up.",
        f"brick {letters[3]}": "Its two forces act the same way and add up.",
    })
    return dict(
        stem=f"Fig. 1 shows four bricks at rest viewed from above. Two forces of **{F} N** are applied to each brick. Which brick does not move?",
        figure=G1.block_forces(cases),
        options=opts, key=key, misconceptions=mis,
        formula="equal forces in opposite directions cancel: no net force, no change in motion",
        working=["only equal AND opposite forces cancel", f"**brick {still}**", src(3)],
        hints=["Look for forces that are opposite as well as equal.", "Forces the same way add; forces at right angles do not cancel.", "One brick has equal and opposite forces."],
    )


# ---------------------------------------------------------------- fixed items (options reshuffled each serve)
ITEMS = [
    dict(id="n26_slash_burn_effect", level=2, lo="2.1d",
         stem=f"Large areas of tropical rain forest are cleared using slash-and-burn.\n\n{md_table(['method', 'what happens'], [['slash-and-burn', 'trees are cut down and burnt']])}\n\nWhich effect is caused by this?",
         correct="increased soil erosion", wrongs={"decreased soil fertility at first": "The ash from the burnt trees adds nutrients at first; the lasting damage is erosion.", "decreased carbon dioxide levels in the air": "Burning releases carbon dioxide, and fewer trees remain to absorb it.", "increased nitrogen levels in the air": "Burning does not raise the nitrogen level of the air."},
         hints=["What holds soil in place on a hillside?", "Tree roots.", "What happens to soil when they are gone?"],
         working=["Correct answer: **increased soil erosion** (deforestation leaves the soil unprotected)", src(2)]),
    dict(id="n26_nitrates_source", level=2, lo="2.1d",
         stem=f"Many rivers near farms are clogged with fast-growing water plants because of high levels of dissolved nitrates.\n\n{md_table(['observation'], [['thick growth of water plants'], ['farms along the river']])}\n\nWhat is the main source of these nitrates?",
         correct="drainage of fertilisers from the fields", wrongs={"decay of animals in the river": "Decay adds some nutrients, but not enough to clog a river; fertiliser run-off does.", "drainage of weedkillers": "Weedkillers KILL plants; they do not feed them.", "pollution from the atmosphere": "Rain adds very little nitrate compared with fertiliser run-off."},
         hints=["What do farmers add to make plants grow?", "Fertilisers contain nitrates.", "Rain washes them into the river."],
         working=["Correct answer: **drainage of fertilisers from the fields**", src(5)]),
    dict(id="n26_waves_treatment_remote", level=2, lo="1.3d",
         stem=f"A patient is treated for cancer in hospital. In the ward, a remote control switches the television on and off.\n\n{md_table(['use'], [['medical treatment of cancer'], ['television remote control']])}\n\nWhich row gives the waves used?",
         correct="gamma rays for the treatment; infrared for the remote control", wrongs={"ultraviolet for the treatment; radio waves for the remote control": "Ultraviolet is used for sterilising, and remotes use infrared.", "microwaves for the treatment; ultraviolet for the remote control": "Microwaves are for cooking and satellites; remotes use infrared.", "X-rays for the treatment; gamma rays for the remote control": "X-rays take pictures of bones; gamma rays treat cancer; remotes use infrared."},
         hints=["Which wave is used for medical TREATMENT?", "Gamma rays.", "Remote controls use infrared."],
         working=["Correct answer: **gamma rays for the treatment; infrared for the remote control**", src(9)]),
    dict(id="n26_biological_control_how", level=1, lo="2.1e",
         stem=f"Small insects are eating the plants in a garden. The gardener introduces organism X as biological control.\n\n{md_table(['organism', 'role'], [['small insects', 'pests eating the plants'], ['organism X', '?']])}\n\nWhich statement describes how biological control works?",
         correct="organism X eats the small insects", wrongs={"organism X eats the plants": "That would make X another pest.", "the small insects eat organism X": "X must be the PREDATOR of the pest.", "organism X kills the insects with a chemical it is sprayed with": "Biological control uses a living predator, not a chemical."},
         hints=["Biological control uses a predator.", "Who is the prey?", "The pest insects."],
         working=["Correct answer: **organism X eats the small insects** (predators control the pests)", src(12)]),
    dict(id="n26_multimeter_arrangement", level=3, lo="1.2c",
         stem=f"Two multimeters measure the voltage across and the current through a resistor. One is set as a voltmeter and one as an ammeter.\n\n{md_table(['meter', 'must be connected'], [['ammeter (A)', '?'], ['voltmeter (V)', '?']])}\n\nWhich arrangement is correct?",
         correct="the ammeter in series with the resistor and the voltmeter in parallel across it", wrongs={"both meters in series with the resistor": "A voltmeter must go ACROSS the resistor.", "both meters in parallel across the resistor": "An ammeter must be IN the path of the current.", "the voltmeter in series and the ammeter in parallel": "That is the wrong way round."},
         hints=["Current flows THROUGH an ammeter.", "A voltmeter compares the two ends of the resistor.", "Series for A, parallel for V."],
         working=["Correct answer: **ammeter in series, voltmeter in parallel**", src(16)]),
    dict(id="n26_bulb_p_blows", level=3, lo="1.2j",
         stem="Fig. 1 shows a circuit used in a household appliance: bulb P is in series with the supply, and bulbs Q and R are in parallel with each other. After some time, bulb P blows. What happens to bulbs Q and R?",
         fig=lambda rng: S.circuit(["lamp"], parallel=[["lamp"], ["lamp"]], top=("battery",), labels=["P", "Q", "R"]),
         correct="Q and R both go out", wrongs={"Q and R both remain lit": "All the current must pass through P to reach them.", "Q goes out but R remains lit": "Q and R are in the same position relative to P.", "Q remains lit but R goes out": "Q and R are in the same position relative to P."},
         hints=["Trace the current from the supply.", "Does it pass through P before reaching Q and R?", "P is in the main path."],
         working=["Correct answer: **Q and R both go out** (P is in series with the rest; the path is broken)", src(17)]),
    dict(id="n26_vary_current_component", level=1, lo="1.2a",
         stem=f"The table lists circuit components.\n\n{md_table(['component'], [['fuse'], ['bell'], ['variable resistor'], ['lamp']])}\n\nWhich component is used to vary the current in a circuit?",
         correct="variable resistor", wrongs={"fuse": "A fuse protects the circuit by melting if the current is too large.", "bell": "A bell rings; it does not control the current.", "lamp": "A lamp gives out light."},
         hints=["Its resistance can be changed.", "More resistance, less current.", "Variable resistor."],
         working=["Correct answer: **variable resistor**", src(19)]),
    dict(id="n26_herbicide_river_weeds", level=4, lo="2.1d",
         stem=f"A farm uses herbicides. Water from the farm flows into a river at position 2. Positions 1 to 4 are along the river, in the direction of flow.\n\n{md_table(['position', 'where'], [['1', 'upstream of the farm'], ['2', 'where the farm water enters'], ['3', 'just downstream'], ['4', 'far downstream']])}\n\nWhich graph of the amount of water weeds against position is correct?",
         correct="many weeds at 1, a sharp fall at 2 and 3, then weeds slowly returning by 4", wrongs={"few weeds at 1, rising sharply at 2 and 3": "Herbicides KILL weeds, so the amount falls where the farm water enters.", "the same amount of weeds at every position": "The herbicide must have an effect where it enters.", "many weeds at 1 falling steadily to none at 4": "The herbicide is diluted downstream, so weeds slowly recover."},
         hints=["What does a herbicide do to weeds?", "Where does it enter the river?", "What happens as it is diluted downstream?"],
         working=["Correct answer: **many weeds at 1, a sharp fall at 2 and 3, slow recovery by 4**", src(23)]),
    dict(id="n26_spoon_water_graph", level=3, lo="1.1b",
         stem=f"A metal spoon at **25 °C** is dropped into a cup of water at **78 °C**.\n\n{md_table(['object', 'start temperature / °C'], [['spoon', 25], ['water', 78]])}\n\nWhich graph shows how the temperatures of the spoon and the water change?",
         correct="the spoon's temperature rises and the water's falls until both meet at the same temperature", wrongs={"the water's temperature rises and the spoon's falls": "Thermal energy flows from the HOT water to the COLD spoon.", "both temperatures stay the same": "Objects at different temperatures in contact exchange thermal energy.", "the spoon's temperature rises above the water's": "The spoon cannot become hotter than the water heating it."},
         hints=["Which is hotter?", "Energy flows from hot to cold.", "When does the flow stop?"],
         working=["Correct answer: **spoon rises, water falls, both meet at one temperature**", src(25)]),
    dict(id="n26_energy_sentences", level=1, lo="1.1c",
         stem=f"Complete the sentences about energy.\n\n{md_table(['sentence'], [['Energy is never ___(1)___, it is ___(2)___ from one form to another.'], ['This is called the principle of ___(3)___ of energy.']])}\n\nWhich words fill the gaps?",
         correct="(1) created (or destroyed), (2) converted, (3) conservation", wrongs={"(1) increased, (2) decreased, (3) reaction": "Energy is never created or destroyed; it is converted; the principle is conservation.", "(1) converted, (2) created, (3) conservation": "(1) and (2) are swapped.", "(1) created, (2) converted, (3) preservation": "The principle is CONSERVATION of energy."},
         hints=["Energy cannot be made or destroyed.", "It changes form.", "The principle of conservation of energy."],
         working=["Correct answer: **created, converted, conservation**", src(31)]),
]

register_explain(ITEMS, chapter=5, category=CAT)   # chapter is overridden per item below


def _rechapter():
    """Items above cover several chapters; fix each item's chapter from its lo code."""
    from .base import TEMPLATES
    topic_to_ch = {"1.1": 1, "1.2": 2, "1.3": 3, "1.4": 4, "2.1": 5}
    ids = {it["id"] for it in ITEMS}
    for t in TEMPLATES:
        if t.id in ids:
            t.chapter = topic_to_ch[t.lo[:3]]
            orig_make = t.make

            def make(seed, _m=orig_make, _ch=t.chapter):
                q = _m(seed)
                q.chapter = _ch
                return q
            t.make = make


_rechapter()
