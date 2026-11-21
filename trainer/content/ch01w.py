"""Ch 1 Energy: extra calculation / data templates adapted from the Topic 1.1 assignments (1a, 1b, 2, 3), the Quick Check
and Revision 1, plus a few explanation items from the same worksheets. Numbers are varied on every serve."""
from .. import sketches as S
from .base import fmt, md_table, nice, numeric_options, pick, register_explain, template, text_options

KP = lambda label, *phr: {"label": label, "any": list(phr)}
SRC = "_Adapted from the QTSS Topic 1.1 worksheets._"


# ---------------------------------------------------------------- L1
@template("c01w_pushups_power", chapter=1, level=1, lo="1.1d")
def pushups_power(rng):
    n = nice(rng, 10, 20, 30)
    E = n * nice(rng, 100, 120, 150)
    t = nice(rng, 20, 25, 30, 40)
    P = E / t
    opts, key, mis = numeric_options(rng, P, [
        (E * t, "You multiplied. Power = energy ÷ time."),
        (E, "That is the energy; divide by the time to get the power."),
        (E / n, "Divide by the TIME in seconds, not by the number of push-ups."),
    ], unit="W", sf=3)
    return dict(
        stem=f"Sam does {n} push-ups.\n\n{md_table(['energy needed / J', 'time taken / s'], [[E, t]])}\n\nCalculate Sam's power.",
        options=opts, key=key, misconceptions=mis,
        formula="power = energy ÷ time taken",
        working=[f"P = {E} ÷ {t}", f"= **{fmt(P)} W**", SRC],
        hints=["Power = energy ÷ time.", "Use the time in seconds.", f"{E} ÷ {t}."],
    )


@template("c01w_diving_board_ke", chapter=1, level=1, lo="1.1c")
def diving_board_ke(rng):
    gpe = nice(rng, 1200, 1400, 1800, 2000)
    h = nice(rng, 3, 3.5, 5)
    opts, key, mis = numeric_options(rng, gpe, [
        (gpe / 2, "With no air resistance, ALL the lost gravitational potential energy becomes kinetic energy."),
        (gpe * h, "Do not multiply by the height; the energy lost is given directly."),
        (0, "The boy is moving fast when he reaches the water, so his kinetic energy is not zero."),
    ], unit="J", sf=4)
    return dict(
        stem=f"A boy stands on a diving board {h} m above the water.\n\n{md_table(['gravitational potential energy lost during the dive / J'], [[gpe]])}\n\nIgnoring air resistance, how much kinetic energy does the boy have when he reaches the water?",
        options=opts, key=key, misconceptions=mis,
        formula="conservation of energy: gravitational potential energy lost = kinetic energy gained",
        working=["energy is conserved: the lost GPE becomes KE", f"KE = **{gpe} J**", SRC],
        hints=["Energy cannot be destroyed, only converted.", "Where does the lost gravitational potential energy go?", "All of it becomes kinetic energy."],
    )


@template("c01w_kettle_power_large", chapter=1, level=1, lo="1.1d")
def kettle_power_large(rng):
    P = nice(rng, 1100, 1200, 1500, 1800)
    t = nice(rng, 10, 20, 30)
    E = P * t
    opts, key, mis = numeric_options(rng, P, [
        (E * t, "You multiplied. Power = energy ÷ time."),
        (E / 1000, "Divide by the time, not by 1000."),
        (E, "That is the energy in joules; divide by the seconds."),
    ], unit="W", sf=4)
    return dict(
        stem=f"An electric kettle is tested.\n\n{md_table(['electrical energy used / J', 'time / s'], [[E, t]])}\n\nWhat is the power of the kettle?",
        options=opts, key=key, misconceptions=mis,
        formula="power = energy ÷ time",
        working=[f"P = {E} ÷ {t}", f"= **{P} W**", SRC],
        hints=["Power = energy ÷ time.", f"{E} ÷ {t}.", "The answer is in watts."],
    )


# ---------------------------------------------------------------- L2
@template("c01w_time_in_minutes", chapter=1, level=2, lo="1.1d")
def time_in_minutes(rng):
    P = nice(rng, 20, 30, 50)
    m = nice(rng, 5, 10, 12, 15)
    E = P * m * 60
    opts, key, mis = numeric_options(rng, m, [
        (m * 60, "That is the time in SECONDS; the question asks for minutes."),
        (E / P / 3600, "Divide the seconds by 60, not by 3600."),
        (P / E * 60, "Upside down: time = energy ÷ power."),
    ], unit="min", sf=3)
    return dict(
        stem=f"Irfan cycles to the market.\n\n{md_table(['energy used / J', 'power / W'], [[E, P]])}\n\nHow many **minutes** does the ride take?",
        options=opts, key=key, misconceptions=mis,
        formula="time (s) = energy ÷ power;  minutes = seconds ÷ 60",
        working=[f"t = {E} ÷ {P} = {m * 60} s", f"= {m * 60} ÷ 60 = **{m} min**", SRC],
        hints=["First find the time in seconds: energy ÷ power.", f"{E} ÷ {P} = {m * 60} s.", "Divide by 60 for minutes."],
    )


@template("c01w_power_from_minutes", chapter=1, level=2, lo="1.1d")
def power_from_minutes(rng):
    E = nice(rng, 36000, 48000, 54000, 72000)
    m = nice(rng, 10, 15, 20)
    P = E / (m * 60)
    opts, key, mis = numeric_options(rng, P, [
        (E / m, "The time must be in seconds: multiply the minutes by 60."),
        (E / (m * 100), "1 minute = 60 s, not 100 s."),
        (E * m * 60, "Divide the energy by the time; do not multiply."),
    ], unit="W", sf=3)
    return dict(
        stem=f"Jason climbs four storeys of stairs.\n\n{md_table(['energy used / J', 'time taken'], [[E, f'{m} min']])}\n\nCalculate Jason's power.",
        options=opts, key=key, misconceptions=mis,
        formula="power = energy ÷ time (s);  1 min = 60 s",
        working=[f"t = {m} × 60 = {m * 60} s", f"P = {E} ÷ {m * 60} = **{fmt(P)} W**", SRC],
        hints=["Change the minutes to seconds.", f"{m} min = {m * 60} s.", f"{E} ÷ {m * 60}."],
    )


@template("c01w_heater_hours_joules", chapter=1, level=2, lo="1.1d")
def heater_hours_joules(rng):
    P = nice(rng, 200, 300, 500)
    h = nice(rng, 1.5, 2, 3)
    E = P * h * 3600
    opts, key, mis = numeric_options(rng, E, [
        (P * h, "The time must be in SECONDS: 1 h = 3600 s."),
        (P * h * 60, "1 hour = 3600 s, not 60 s."),
        (P * h * 100, "1 hour = 60 × 60 = 3600 s."),
    ], unit="J", sf=4)
    return dict(
        stem=f"A heater is used as shown.\n\n{md_table(['power / W', 'time used'], [[P, f'{h:g} h']])}\n\nHow much energy does it use, in joules?",
        options=opts, key=key, misconceptions=mis,
        formula="energy = power × time (s);  1 h = 3600 s",
        working=[f"t = {h:g} × 3600 = {h * 3600:g} s", f"E = {P} × {h * 3600:g} = **{fmt(E, sf=4)} J**", SRC],
        hints=["Change hours to seconds.", f"{h:g} h = {h * 3600:g} s.", f"{P} × {h * 3600:g}."],
    )


@template("c01w_hairdryer_sound", chapter=1, level=2, lo="1.1c")
def hairdryer_sound(rng):
    inp = nice(rng, 12000, 18000, 24000)
    ke = int(inp * nice(rng, 0.8, 0.85, 0.9))
    snd = inp - ke
    opts, key, mis = numeric_options(rng, snd, [
        (inp + ke, "Subtract: output energies add up to the input."),
        (ke, "That is the kinetic energy of the moving air."),
        (inp, "Only part of the input becomes sound."),
    ], unit="J", sf=4)
    return dict(
        stem=f"Fig. 1 shows the energy conversion in a hair dryer with no heating element. How much sound energy is produced?",
        figure=S.energy_arrows(["electrical energy in", "kinetic energy of air"], [inp, ke]),
        options=opts, key=key, misconceptions=mis,
        formula="electrical energy in = kinetic energy + sound energy (conservation of energy)",
        working=[f"sound = {inp} − {ke}", f"= **{snd} J**", SRC],
        hints=["The two outputs add up to the input.", "Subtract the kinetic energy from the input.", f"{inp} − {ke}."],
    )


@template("c01w_beaker_warms", chapter=1, level=2, lo="1.1b")
def beaker_warms(rng):
    water = nice(rng, 10, 15, 18)
    room = nice(rng, 25, 28, 30)
    ans = "increases, because thermal energy is transferred into the water from the warmer surroundings"
    opts, key, mis = text_options(rng, ans, {
        "decreases, because thermal energy is transferred from the water into the surroundings": "The water is COLDER than the room, so energy flows INTO it.",
        "increases, because thermal energy is transferred from the water into the surroundings": "Losing energy would make the water cooler, not warmer.",
        "stays the same, because water cannot gain thermal energy": "Anything colder than its surroundings gains thermal energy.",
    })
    return dict(
        stem=f"A beaker of water is left on a table in a classroom for 10 minutes.\n\n{md_table(['water temperature at start / °C', 'room temperature / °C'], [[water, room]])}\n\nWhat happens to the water temperature, and why?",
        options=opts, key=key, misconceptions=mis,
        formula="thermal energy flows from the region of higher temperature to the region of lower temperature",
        working=[f"the room ({room} °C) is hotter than the water ({water} °C)", f"energy flows into the water: **{ans}**", SRC],
        hints=["Which is hotter, the water or the room?", "Energy flows from hot to cold.", "So the water gains energy."],
    )


# ---------------------------------------------------------------- L3
@template("c01w_which_device_most_energy", chapter=1, level=3, lo="1.1d")
def which_device_most_energy(rng):
    devs = [("light bulb", nice(rng, 50, 60), nice(rng, 200, 250)), ("soldering iron", nice(rng, 100, 120), nice(rng, 120, 150)),
            ("toaster", nice(rng, 500, 600), nice(rng, 40, 50)), ("heater", 1000, nice(rng, 15, 20))]
    Es = [(n, P, t, P * t) for n, P, t in devs]
    best = max(Es, key=lambda x: x[3])
    others = [e for e in Es if e != best]
    opts, key, mis = text_options(rng, f"the {best[1]} W {best[0]} in {best[2]} s", {
        f"the {o[1]} W {o[0]} in {o[2]} s": f"{o[1]} × {o[2]} = {o[3]} J, less than {best[3]} J." for o in others
    })
    return dict(
        stem=f"Four devices are switched on for different times.\n\n{md_table(['device', 'power / W', 'time / s'], [[n, P, t] for n, P, t in devs])}\n\nWhich device uses the most electrical energy?",
        options=opts, key=key, misconceptions=mis,
        formula="energy = power × time",
        working=["; ".join(f"{n}: {P} × {t} = {E} J" for n, P, t, E in Es), f"largest: **{best[0]} ({best[3]} J)**", SRC],
        hints=["Work out power × time for each device.", "The highest power is not always the most energy.", "Compare the four products."],
    )


@template("c01w_three_outputs_x", chapter=1, level=3, lo="1.1c")
def three_outputs_x(rng):
    inp = nice(rng, 500, 800, 1000)
    big = int(inp * nice(rng, 0.9, 0.95, 0.98))
    small = nice(rng, 1, 2, 5)
    X = inp - big - small
    opts, key, mis = numeric_options(rng, X, [
        (inp - big, "You forgot to subtract the sound energy as well."),
        (inp + big + small, "The outputs add up TO the input; subtract to find X."),
        (big - small, "X = input − thermal − sound."),
    ], unit="J", sf=3)
    return dict(
        stem=f"A hair dryer converts energy as shown.\n\n{md_table(['energy', 'amount / J'], [['electrical energy in', inp], ['thermal energy out', big], ['sound energy out', small], ['kinetic energy out (X)', '?']])}\n\nWhat is the value of X?",
        options=opts, key=key, misconceptions=mis,
        formula="energy in = thermal + sound + kinetic (conservation of energy)",
        working=[f"X = {inp} − {big} − {small}", f"= **{X} J**", SRC],
        hints=["All the outputs add up to the input.", "Subtract the two known outputs.", f"{inp} − {big} − {small}."],
    )


@template("c01w_trolley_split_row", chapter=1, level=3, lo="1.1c")
def trolley_split_row(rng):
    gpe = nice(rng, 800, 1000, 1200)
    ke = int(gpe * nice(rng, 0.6, 0.7, 0.75))
    th = gpe - ke
    correct = f"kinetic {ke} J, thermal {th} J"
    w = {f"kinetic {ke} J, thermal {th + 100} J": f"{ke} + {th + 100} is more than the {gpe} J lost; energy cannot be created.",
         f"kinetic {ke - 100} J, thermal {th} J": f"{ke - 100} + {th} is less than {gpe} J; energy cannot be destroyed.",
         f"kinetic {gpe} J, thermal {th} J": "The two outputs must ADD to the energy lost, not each equal it."}
    opts, key, mis = text_options(rng, correct, w)
    return dict(
        stem=f"A trolley rolls down a slope and loses **{gpe} J** of gravitational potential energy, which becomes kinetic energy and thermal energy.\n\n{md_table(['energy lost from the gravitational store / J'], [[gpe]])}\n\nWhich row is possible?",
        options=opts, key=key, misconceptions=mis,
        formula="kinetic + thermal = gravitational potential energy lost",
        working=[f"the two outputs must add up to {gpe} J", f"**{correct}** ({ke} + {th} = {gpe})", SRC],
        hints=["Add the kinetic and thermal values in each row.", f"Which pair adds up to {gpe}?", "Energy is conserved."],
    )


@template("c01w_two_appliances_time_equal", chapter=1, level=3, lo="1.1d")
def two_appliances_time_equal(rng):
    P1 = nice(rng, 1200, 1500, 2000)
    t1 = nice(rng, 40, 60)
    P2 = nice(rng, 300, 400, 500)
    E = P1 * t1
    t2 = E / P2
    opts, key, mis = numeric_options(rng, t2, [
        (t1, "The lower-power device needs LONGER to convert the same energy."),
        (E * P2, "Divide the energy by the power; do not multiply."),
        (t1 * P2 / P1, "Upside down ratio: time = energy ÷ power."),
    ], unit="s", sf=3)
    return dict(
        stem=f"Two appliances convert the same amount of energy.\n\n{md_table(['appliance', 'power / W', 'time / s'], [['kettle', P1, t1], ['toaster', P2, '?']])}\n\nHow long must the toaster run to convert the same energy as the kettle?",
        options=opts, key=key, misconceptions=mis,
        formula="energy = power × time;  time = energy ÷ power",
        working=[f"energy = {P1} × {t1} = {E} J", f"toaster time = {E} ÷ {P2} = **{fmt(t2)} s**", SRC],
        hints=["Find the kettle's energy first.", f"{P1} × {t1} = {E} J.", f"Then {E} ÷ {P2}."],
    )


# ---------------------------------------------------------------- L4
@template("c01w_thermal_arrows_order", chapter=1, level=4, lo="1.1b")
def thermal_arrows_order(rng):
    what = pick(rng, ["metal blocks", "cups of water", "stones", "bricks"])
    flows = [["P", "Q"], ["Q", "R"], ["S", "R"]]
    ans = "Q is hotter than R but colder than P"
    opts, key, mis = text_options(rng, ans, {
        "P is colder than Q and R": "Energy flows FROM P, so P is the hottest of the three.",
        "R is the hottest object": "Energy flows INTO R from both Q and S, so R is coldest.",
        "S and R are at the same temperature": "Energy flows from S to R, so S is hotter than R.",
    })
    return dict(
        stem=f"Four {what} P, Q, R and S are in contact. The table shows the direction of thermal energy flow between them.\n\n{md_table(['from', 'to'], flows)}\n\nWhich statement about their temperatures is correct?",
        options=opts, key=key, misconceptions=mis,
        formula="thermal energy flows from the hotter object to the colder object",
        working=["P → Q means P hotter than Q; Q → R means Q hotter than R; S → R means S hotter than R", f"**{ans}**", SRC],
        hints=["Each arrow goes from hotter to colder.", "Write the order for P, Q and R.", "P > Q > R."],
    )


@template("c01w_energy_bar_chart_compare", chapter=1, level=4, lo="1.1d")
def energy_bar_chart_compare(rng):
    names = ["bulb", "iron", "toaster", "heater"]
    Ps = [nice(rng, 50, 60), nice(rng, 100, 120), nice(rng, 500, 600), 1000]
    ts = [nice(rng, 200, 250), nice(rng, 120, 150), nice(rng, 40, 50), nice(rng, 15, 20)]
    Es = [P * t for P, t in zip(Ps, ts)]
    i = Es.index(max(Es))
    ans = f"{names[i]}, because its energy = {Ps[i]} × {ts[i]} = {Es[i]} J is the largest"
    others = [j for j in range(4) if j != i]
    opts, key, mis = text_options(rng, ans, {
        f"{names[j]}, because its energy = {Ps[j]} × {ts[j]} = {Es[j]} J is the largest": f"{Es[j]} J is less than {Es[i]} J." for j in others
    })
    return dict(
        stem=f"Fig. 1 shows the power of four appliances. The table shows how long each is used.\n\n{md_table(['appliance', 'time / s'], [[n, t] for n, t in zip(names, ts)])}\n\nWhich appliance converts the most energy?",
        figure=S.bar_chart(names, Ps, "power / W", ymax=1200, ystep=200),
        options=opts, key=key, misconceptions=mis,
        formula="energy = power × time",
        working=["; ".join(f"{n}: {P} × {t} = {E} J" for n, P, t, E in zip(names, Ps, ts, Es)), f"**{names[i]}**", SRC],
        hints=["Read each power from the chart.", "Multiply by its time.", "Compare the four energies."],
    )


# ---------------------------------------------------------------- L5
@template("c01w_station_energy_chain_percent", chapter=1, level=5, lo="1.1e")
def station_energy_chain_percent(rng):
    chem = nice(rng, 1000, 2000)
    thermal = int(chem * nice(rng, 0.85, 0.9))
    kinetic = int(thermal * nice(rng, 0.45, 0.5))
    elec = int(kinetic * nice(rng, 0.9, 0.95))
    stage_loss = [chem - thermal, thermal - kinetic, kinetic - elec]
    names = ["furnace/boiler", "turbine", "generator"]
    j = stage_loss.index(max(stage_loss))
    opts, key, mis = text_options(rng, f"the {names[j]} stage, which wastes {stage_loss[j]} MJ", {
        f"the {names[k]} stage, which wastes {stage_loss[k]} MJ": f"{stage_loss[k]} MJ is less than {stage_loss[j]} MJ." for k in range(3) if k != j
    } | {"no stage wastes energy, because energy is conserved": "Conservation means the total is constant, but at each stage some becomes wasted thermal energy."})
    return dict(
        stem="Fig. 1 shows the energy at each stage of a fossil fuel power station every second. Which stage wastes the most energy?",
        figure=S.energy_arrows(["chemical (fuel)", "thermal (steam)", "kinetic (turbine)", "electrical"], [chem, thermal, kinetic, elec], unit="MJ"),
        options=opts, key=key, misconceptions=mis,
        formula="energy wasted at a stage = energy entering the stage − energy leaving it",
        working=["; ".join(f"{n}: {l} MJ" for n, l in zip(names, stage_loss)), f"largest loss: **{names[j]}**", SRC],
        hints=["Subtract the energy leaving each stage from the energy entering it.", "Do it for all three stages.", "Pick the biggest difference."],
    )


@template("c01w_cost_of_wasted_energy", chapter=1, level=5, lo="1.1c")
def cost_of_wasted_energy(rng):
    P = nice(rng, 60, 100)
    frac = nice(rng, 0.9, 0.95)
    hours = nice(rng, 4, 5, 6)
    wasted_W = P * frac
    wasted_J = wasted_W * hours * 3600
    opts, key, mis = numeric_options(rng, wasted_J, [
        (P * hours * 3600, "That is the TOTAL energy; only the wasted fraction is asked for."),
        (wasted_W * hours, "The time must be in seconds."),
        (P * (1 - frac) * hours * 3600, "That is the USEFUL light energy, not the wasted part."),
    ], unit="J", sf=3)
    return dict(
        stem=f"A filament lamp converts only {int((1 - frac) * 100)}% of its electrical energy to light; the rest is wasted as thermal energy.\n\n{md_table(['power / W', 'time on each evening / h'], [[P, hours]])}\n\nHow much energy is wasted as thermal energy in one evening?",
        options=opts, key=key, misconceptions=mis,
        formula="wasted power = power × wasted fraction;  energy = power × time (s)",
        working=[f"wasted power = {P} × {frac} = {fmt(wasted_W)} W", f"time = {hours} × 3600 = {hours * 3600} s", f"wasted energy = {fmt(wasted_W)} × {hours * 3600} = **{fmt(wasted_J)} J**", SRC],
        hints=["First find how many watts are wasted.", f"{P} × {frac}.", "Then multiply by the seconds."],
    )


# ================================================================ EXPLANATION (worksheet items)
EXPLAIN = [
    dict(id="e01w_object_energy_forms", level=1, lo="1.1a",
         stem=f"The table lists objects.\n\n{md_table(['object', 'form of energy'], [['stretched rubber band', 'P'], ['battery', 'Q'], ['hot plate', 'R'], ['turning ceiling fan', 'S']])}\n\nWhat are P, Q, R and S?",
         correct="P elastic potential, Q chemical potential, R thermal, S kinetic",
         wrongs={"P kinetic, Q chemical potential, R thermal, S elastic potential": "A stretched band stores ELASTIC potential energy; a turning fan has KINETIC energy.", "P elastic potential, Q thermal, R chemical potential, S kinetic": "A battery stores CHEMICAL potential energy; a hot plate has THERMAL energy.", "P gravitational potential, Q chemical potential, R thermal, S kinetic": "A stretched band stores elastic, not gravitational, potential energy."},
         hints=["Stretched → elastic.", "Battery → chemical.", "Hot → thermal; moving → kinetic."],
         working=["Correct answer: **P elastic potential, Q chemical potential, R thermal, S kinetic**", SRC]),
    dict(id="e01w_match_energy", level=2, lo="1.1a",
         stem=f"Ling Ling says a match stores heat energy. The table shows what happens when it is struck.\n\n{md_table(['before', 'after'], [['unlit match', 'flame giving out light and heat']])}\n\nWhat form of energy does the match store, and what conversion takes place?",
         correct="chemical potential energy, converted to thermal and light energy",
         wrongs={"thermal energy, converted to light energy": "The match is not hot before it is struck; it stores chemical potential energy.", "kinetic energy, converted to thermal energy": "The match is not moving.", "light energy, converted to thermal energy": "An unlit match gives out no light."},
         hints=["What do fuels store?", "The match is a fuel.", "Chemical → thermal + light."],
         working=["Correct answer: **chemical potential energy, converted to thermal and light energy**", SRC]),
    dict(id="e01w_pendulum_rest", level=5, lo="1.1c",
         stem=f"A pendulum is released from P and swings until it eventually stops.\n\n{md_table(['swing', 'height reached on the other side / cm'], [[1, 19], [10, 12], [50, 2]])}\n\nUsing the principle of conservation of energy, explain why the pendulum stops even though energy cannot be destroyed.",
         correct="at each swing some energy is converted by air resistance and friction into thermal energy, so less remains as gravitational potential and kinetic energy",
         wrongs={"energy is slowly destroyed by gravity": "Energy is never destroyed; it is converted to other forms.", "the pendulum runs out of kinetic energy at the top and cannot get it back": "At the top the energy is stored as gravitational potential energy, which becomes kinetic energy again on the way down.", "the string absorbs the gravitational energy": "The string transmits the motion; the energy becomes thermal energy through friction and air resistance."},
         hints=["Where does the energy go if it is not destroyed?", "Think about air resistance at the pivot and on the bob.", "Thermal energy."],
         keypoints=[KP("friction / air resistance", "friction", "air resistance", "resistance", "rubbing"), KP("thermal energy", "thermal", "heat")],
         working=["Correct answer: **at each swing some energy is converted by air resistance and friction into thermal energy, so less remains as gravitational potential and kinetic energy**", SRC]),
]

register_explain(EXPLAIN, chapter=1)
