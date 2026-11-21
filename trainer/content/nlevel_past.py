"""N level exam practice (category 'nlevel'): questions adapted from SEAB 5148 N(T) Science Paper 1 papers 2013-2023,
Chapters 1-5 of the K123 syllabus only. Adapted, never copied: contexts kept, numbers changed and varied, diagram
options turned into words or redrawn. Each item names its source under the working."""
from .. import figs, sketches as S, sketches_g1 as G1
from .base import fmt, md_table, nice, numeric_options, pick, register_explain, template, text_options

CAT = "nlevel"


def src(year, q):
    return f"_Adapted from SEAB 5148 N(T) Science {year} Paper 1 Q{q}._"


def R(id, ch, level, lo, stem, correct, wrongs, hints, year, q, fig=None, keypoints=None):
    d = dict(id=id, level=level, lo=lo, stem=stem, correct=correct, wrongs=wrongs, hints=hints,
             working=[f"Correct answer: **{correct}**", src(year, q)])
    if fig:
        d["fig"] = fig
    if keypoints:
        d["keypoints"] = keypoints
    return ch, d


# ================================================================ varying-number templates
@template("np_ball_table_speed", chapter=4, level=3, lo="1.4e", category=CAT)
def ball_table_speed(rng):
    d1 = nice(rng, 2.0, 3.0, 5.0)
    gain = nice(rng, 3.0, 4.0, 5.0, 8.0)
    d2 = d1 + gain
    v = gain / 1.0
    opts, key, mis = numeric_options(rng, v, [
        (d2, "Use the distance fallen BETWEEN 1.0 s and 2.0 s, not the total distance."),
        (d2 / 2, "Speed over the second second = (d at 2 s − d at 1 s) ÷ 1 s."),
        ((d1 + d2) / 2, "Do not average the distances; subtract them."),
    ], unit="m/s", sf=3)
    return dict(
        stem=f"A small ball is dropped. The table shows the distance d fallen at different times t.\n\n{md_table(['t / s', 'd / m'], [[1.0, d1], [2.0, d2]])}\n\nWhat is the average speed of the ball between t = 1.0 s and t = 2.0 s?",
        options=opts, key=key, misconceptions=mis,
        formula="average speed = distance moved ÷ time taken",
        working=[f"distance moved = {d2:g} − {d1:g} = {gain:g} m in 1.0 s", f"speed = **{fmt(v)} m/s**", src(2013, 18)],
        hints=["How far did it fall between 1.0 s and 2.0 s?", f"{d2:g} − {d1:g}.", "Divide by the 1.0 s taken."],
    )


@template("np_pump_energy_row", chapter=1, level=3, lo="1.1c", category=CAT)
def pump_energy_row(rng):
    inp = nice(rng, 8000, 10000, 12000)
    gpe = int(inp * nice(rng, 0.6, 0.7, 0.75))
    heat = inp - gpe
    correct = f"electrical {inp} J, gravitational potential {gpe} J, heat {heat} J"
    w = {f"electrical {gpe} J, gravitational potential {inp} J, heat {heat} J": "The energy gained by the water cannot be MORE than the electrical energy used.",
         f"electrical {inp} J, gravitational potential {inp} J, heat {heat} J": f"{inp} + {heat} is more than the input; outputs must add up to the input.",
         f"electrical {inp} J, gravitational potential {heat} J, heat {gpe} J": "Most of the energy goes to the useful output (lifting the water); the smaller share is wasted as heat."}
    opts, key, mis = text_options(rng, correct, w)
    return dict(
        stem=f"An electric pump sends water from a lower tank to an upper tank. Most of the electrical energy lifts the water; the rest is passed to the surroundings as heat.\n\n{md_table(['electrical energy used / J'], [[inp]])}\n\nWhich row correctly shows the amounts of energy?",
        options=opts, key=key, misconceptions=mis,
        formula="electrical energy used = gravitational potential energy gained + heat passed to the surroundings",
        working=[f"{gpe} + {heat} = {inp}", f"**{correct}**", src(2016, 3)],
        hints=["The two outputs must add up to the input.", "The useful output (lifting) is the larger share.", "Check each row adds up."],
    )


@template("np_heater_energy_minute", chapter=2, level=3, lo="1.2l", category=CAT)
def heater_energy_minute(rng):
    I = nice(rng, 4, 6, 8, 10)
    V = nice(rng, 230, 240, 250)
    m = nice(rng, 1, 2, 5)
    E = I * V * m * 60
    opts, key, mis = numeric_options(rng, E, [
        (I * V * m, "The time must be in seconds: 1 min = 60 s."),
        (I * V, "That is the power in watts; multiply by the time in seconds."),
        (V / I * m * 60, "Power = current × voltage, not voltage ÷ current."),
    ], unit="J", sf=4)
    return dict(
        stem=f"An electric heater uses a current of **{I} A** when connected to a **{V} V** supply.\n\n{md_table(['current / A', 'voltage / V', 'time'], [[I, V, f'{m} min']])}\n\nHow much energy is converted by the heater in this time?",
        options=opts, key=key, misconceptions=mis,
        formula="power = current × voltage;  energy = power × time (s)",
        working=[f"P = {I} × {V} = {I * V} W", f"E = {I * V} × {m * 60} = **{E} J**", src(2017, 13)],
        hints=["Find the power first.", f"{m} min = {m * 60} s.", "Energy = power × time."],
    )


@template("np_aircon_cost_cents", chapter=2, level=2, lo="1.2m", category=CAT)
def aircon_cost_cents(rng):
    cents = nice(rng, 20, 25, 30)
    Pk = nice(rng, 1.2, 1.5, 2)
    h = nice(rng, 5, 8, 10)
    c = cents * Pk * h
    opts, key, mis = numeric_options(rng, c, [
        (cents * h, "Multiply by the power in kW as well."),
        (cents * Pk, "Multiply by the hours as well."),
        (Pk * h, "That is the energy in kWh; multiply by the price."),
    ], unit="cents", sf=3)
    return dict(
        stem=f"The cost of electricity is **{cents} cents per kWh**. The average power of an air conditioner is **{Pk:g} kW**.\n\n{md_table(['power / kW', 'time used / h'], [[Pk, h]])}\n\nHow much does it cost to use the air conditioner for this time?",
        options=opts, key=key, misconceptions=mis,
        formula="cost = power (kW) × time (h) × price per kWh",
        working=[f"energy = {Pk:g} × {h} = {Pk * h:g} kWh", f"cost = {Pk * h:g} × {cents} = **{c:g} cents**", src(2017, 14)],
        hints=["kW × h = kWh.", f"{Pk * h:g} kWh.", f"× {cents} cents."],
    )


@template("np_computer_power", chapter=1, level=1, lo="1.1d", category=CAT)
def computer_power(rng):
    P = nice(rng, 60, 90, 120, 150)
    t = nice(rng, 2000, 3000, 6000)
    E = P * t
    opts, key, mis = numeric_options(rng, P, [
        (t / E, "Power = energy ÷ time; this is time ÷ energy."),
        (P * 10, "Check the division."),
        (E * t, "Divide, do not multiply."),
    ], unit="W", sf=3)
    return dict(
        stem=f"A computer uses energy.\n\n{md_table(['energy used / J', 'time / s'], [[E, t]])}\n\nWhat is the power of the computer?",
        options=opts, key=key, misconceptions=mis,
        formula="power = energy ÷ time",
        working=[f"P = {E} ÷ {t}", f"= **{P} W**", src(2022, 2)],
        hints=["Power = energy ÷ time.", f"{E} ÷ {t}.", "Watts."],
    )


@template("np_laptop_cost_small", chapter=2, level=3, lo="1.2m", category=CAT)
def laptop_cost_small(rng):
    P = nice(rng, 40, 45, 60)
    h = nice(rng, 2, 4, 5)
    cents = nice(rng, 25, 30)
    c = P / 1000 * h * cents
    opts, key, mis = numeric_options(rng, c, [
        (P * h * cents / 100, "Change the watts to kilowatts (÷ 1000), not to hundredths."),
        (P * h * cents, "Change the watts to kilowatts first."),
        (c * 100, "The price is in cents, so the answer is in cents."),
    ], unit="cents", sf=3)
    return dict(
        stem=f"A laptop uses **{P} W** of power. Electricity costs **{cents} cents for 1 kWh**.\n\n{md_table(['power / W', 'time used / h'], [[P, h]])}\n\nWhat is the cost of using the laptop for this time?",
        options=opts, key=key, misconceptions=mis,
        formula="energy (kWh) = power (kW) × hours;  cost = kWh × price",
        working=[f"{P} W = {P / 1000:g} kW", f"energy = {P / 1000:g} × {h} = {P / 1000 * h:g} kWh", f"cost = {P / 1000 * h:g} × {cents} = **{fmt(c)} cents**", src(2023, 11)],
        hints=["Change W to kW.", f"{P / 1000:g} kW × {h} h.", "Then multiply by the price per kWh."],
    )


@template("np_least_cost_appliance", chapter=2, level=3, lo="1.2m", category=CAT)
def least_cost_appliance(rng):
    rows = [[nice(rng, 300, 350), 9], [nice(rng, 550, 600), 5], [nice(rng, 700, 750), 4], [nice(rng, 800, 850), 3.5]]
    Es = [P * h for P, h in rows]
    i = Es.index(min(Es))
    correct = f"{rows[i][0]} W for {rows[i][1]:g} hours"
    w = {f"{rows[j][0]} W for {rows[j][1]:g} hours": f"{rows[j][0]} × {rows[j][1]:g} = {Es[j]:g} Wh, more than {Es[i]:g} Wh." for j in range(4) if j != i}
    opts, key, mis = text_options(rng, correct, w)
    return dict(
        stem=f"A man uses four electrical appliances in his home.\n\n{md_table(['appliance', 'power / W', 'time used / h'], [[l, P, h] for l, (P, h) in zip('PQRS', rows)])}\n\nWhich appliance costs the least to use for the time shown?",
        options=opts, key=key, misconceptions=mis,
        formula="cost depends on energy = power × time; the least energy costs the least",
        working=["; ".join(f"{P} × {h:g} = {E:g} Wh" for (P, h), E in zip(rows, Es)), f"least energy: **{correct}**", src(2020, 12)],
        hints=["Cost depends on energy, not power alone.", "Multiply power × hours for each.", "Pick the smallest."],
    )


@template("np_acceleration_speeds", chapter=4, level=2, lo="1.4f", category=CAT)
def acceleration_speeds(rng):
    u = nice(rng, 12, 15, 18, 20)
    v = u + nice(rng, 6, 8, 10, 12)
    t = nice(rng, 5, 8, 10)
    a = (v - u) / t
    opts, key, mis = numeric_options(rng, a, [
        (v / t, "Use the CHANGE in speed, final − initial."),
        ((v + u) / t, "Subtract the speeds; do not add."),
        ((v - u) * t, "Divide by the time; do not multiply."),
    ], unit="m/s²", sf=3)
    return dict(
        stem=f"A car travelling at **{u} m/s** accelerates for **{t} s** to a speed of **{v} m/s**.\n\n{md_table(['initial speed / m/s', 'final speed / m/s', 'time / s'], [[u, v, t]])}\n\nWhat is the average acceleration of the car during this time?",
        options=opts, key=key, misconceptions=mis,
        formula="acceleration = change in speed ÷ time taken",
        working=[f"change in speed = {v} − {u} = {v - u} m/s", f"a = {v - u} ÷ {t} = **{fmt(a)} m/s²**", src(2017, 10)],
        hints=["Find the change in speed.", f"{v} − {u}.", f"÷ {t}."],
    )


@template("np_stopwatch_mins_secs", chapter=4, level=2, lo="1.4b", category=CAT)
def stopwatch_mins_secs(rng):
    m = nice(rng, 1, 2)
    s = nice(rng, 6, 12, 25, 48)
    t = 60 * m + s
    opts, key, mis = numeric_options(rng, t, [
        (int(f"{m}{s:02d}"), "The digits before the colon are MINUTES: multiply by 60 and add the seconds."),
        (s, "Do not ignore the minutes."),
        (m + s, "1 minute = 60 seconds."),
    ], unit="s", sf=3)
    return dict(
        stem=f"A stopwatch is set to 00:00. When a moving car is first seen, the start button is pressed. When the car passes an observer the stopwatch shows **{m:02d}:{s:02d}** (minutes : seconds).\n\n{md_table(['display'], [[f'{m:02d}:{s:02d}']])}\n\nHow long did the car take to reach the observer?",
        options=opts, key=key, misconceptions=mis,
        formula="time in seconds = minutes × 60 + seconds",
        working=[f"{m} min {s} s = {m} × 60 + {s}", f"= **{t} s**", src(2016, 1)],
        hints=["Read the minutes and the seconds separately.", f"{m} min = {m * 60} s.", f"Add the {s} s."],
    )


@template("np_stopwatch_after_interval", chapter=4, level=2, lo="1.4b", category=CAT)
def stopwatch_after_interval(rng):
    t = nice(rng, 29.00, 45.50, 72.25, 95.08)
    m = int(t // 60); s = t - 60 * m
    correct = f"{m:02d}:{s:05.2f}"
    w = {f"{int(t):02d}:{round((t - int(t)) * 100):02d}.00": "The display is minutes : seconds . hundredths; 60 s makes 1 minute." if t >= 60 else "The seconds field holds up to 59.99 s; put the whole time in seconds.",
         f"{m:02d}:{s + 1:05.2f}": "Check the seconds.",
         f"{m + 1:02d}:{s:05.2f}": "Only every 60 s adds a minute."}
    opts, key, mis = text_options(rng, correct, w)
    return dict(
        stem=f"A digital stopwatch shows **00:13.08** when the reading is 0 min 13.08 s. The stopwatch is set to zero and used to measure a time interval of **{t:.2f} s**.\n\n{md_table(['time interval / s'], [[f'{t:.2f}']])}\n\nWhat is the new display on the stopwatch?",
        options=opts, key=key, misconceptions=mis,
        formula="display = minutes : seconds . hundredths",
        working=[f"{t:.2f} s = {m} min {s:.2f} s", f"display **{correct}**", src(2022, 8)],
        hints=["How many whole minutes in the time?", "The rest goes in the seconds field.", "Hundredths after the point."],
    )


@template("np_walk_jog_distance", chapter=4, level=5, lo="1.4g", category=CAT)
def walk_jog_distance(rng):
    v1, t1 = nice(rng, 1, 2), nice(rng, 4, 5)
    v2, t2 = nice(rng, 3, 4), nice(rng, 5, 6)
    D = v1 * t1 + v2 * t2
    segs = [(0, 0), (t1, v1 * t1), (t1 + t2, D)]
    opts, key, mis = text_options(rng, f"a straight line to {v1 * t1} m at {t1} s, then a steeper straight line to {D} m at {t1 + t2} s", {
        f"a straight line to {v1 * t1} m at {t1} s, then a less steep straight line to {D} m at {t1 + t2} s": "Jogging is faster than walking, so the second section is STEEPER.",
        f"a curve rising to {D} m, because the speed changes": "Each stage is at a constant speed, so each section is a straight line.",
        f"a straight line to {v2 * t2} m at {t1} s, then a steeper line to {D} m": f"In the first {t1} s at {v1} m/s the distance is {v1 * t1} m.",
    })
    return dict(
        stem=f"A man walks away from home at a constant speed of **{v1} m/s** for **{t1} s** and then jogs at **{v2} m/s** for **{t2} s**. Fig. 1 shows the correct distance-time graph. Which description matches it?",
        figure=G1.dt_graph(segs, xmax=t1 + t2, ymax=D * 1.15, xstep=2, ystep=5, labels=False),
        options=opts, key=key, misconceptions=mis,
        formula="distance = speed × time for each stage; constant speed = straight line; faster = steeper",
        working=[f"walk: {v1} × {t1} = {v1 * t1} m;  jog: {v2} × {t2} = {v2 * t2} m", f"total {D} m; the jog section is steeper", src(2022, 9)],
        hints=["Work out the distance for each stage.", "Constant speed gives a straight line.", "Faster means steeper."],
    )


@template("np_stationary_minutes_graph", chapter=4, level=3, lo="1.4g", category=CAT)
def stationary_minutes_graph(rng):
    stop1 = nice(rng, 5, 10)
    stop2 = nice(rng, 5, 10, 15)
    segs = [(0, 0), (10, 2), (10 + stop1, 2), (25 + stop1 - 10 + 10, 4), (25 + stop1 + stop2, 4), (50, 5)]
    total = stop1 + stop2
    opts, key, mis = numeric_options(rng, total, [
        (stop1, "There are TWO flat sections; add both."),
        (50 - total, "That is the time spent moving."),
        (0, "The flat sections show times when the distance does not change: stationary."),
    ], unit="minutes", sf=3)
    return dict(
        stem="Fig. 1 is the distance-time graph of a student's bicycle ride. For how many minutes during the journey was the student stationary?",
        figure=G1.dt_graph(segs, xmax=50, ymax=6, xstep=5, ystep=1, labels=False),
        options=opts, key=key, misconceptions=mis,
        formula="a flat section of a distance-time graph means the object is stationary",
        working=[f"flat sections last {stop1} min and {stop2} min", f"total **{total} minutes**", src(2021, 9)],
        hints=["Look for sections where the distance does not change.", "Read how long each lasts.", "Add them."],
    )


@template("np_blocks_end_to_end", chapter=4, level=3, lo="1.4a", category=CAT)
def blocks_end_to_end(rng):
    start = nice(rng, 8.1, 9.3, 10.6)
    lens = [3.1, 2.9, 2.7, 3.0]
    rng.shuffle(lens)
    marks = [start]
    for L in lens:
        marks.append(round(marks[-1] + L, 1))
    target = 2.7
    i = lens.index(target)
    correct = "ABCD"[i]
    w = {"ABCD"[j]: f"Block {'ABCD'[j]} runs from {marks[j]} cm to {marks[j + 1]} cm: {lens[j]} cm long." for j in range(4) if j != i}
    opts, key, mis = text_options(rng, f"block {correct}", {f"block {k}": v for k, v in w.items()})
    return dict(
        stem=f"Four blocks of wood A, B, C and D are placed end-to-end alongside a ruler. The table shows where each block starts and ends.\n\n{md_table(['block', 'start / cm', 'end / cm'], [['ABCD'[j], marks[j], marks[j + 1]] for j in range(4)])}\n\nWhich block has a length of **{target} cm**?",
        options=opts, key=key, misconceptions=mis,
        formula="length = end reading − start reading",
        working=["; ".join(f"{'ABCD'[j]}: {marks[j + 1]} − {marks[j]} = {lens[j]} cm" for j in range(4)), f"**block {correct}**", src(2023, 7)],
        hints=["Subtract start from end for each block.", "One block gives exactly 2.7 cm.", "Check the subtraction to one decimal place."],
    )


@template("np_fertiliser_week_difference", chapter=5, level=5, lo="2.1c", category=CAT)
def fertiliser_week_difference(rng):
    P = [4, 9, 15, 22, 30, 36]
    Q = [4, 7, 11, 14, 20, 26]
    bump = rng.randrange(2, 6)
    Q = [q if k != bump else q - nice(rng, 2, 3) for k, q in enumerate(Q)]
    diffs = [p - q for p, q in zip(P, Q)]
    wk = diffs.index(max(diffs)) + 1
    opts, key, mis = numeric_options(rng, wk, [
        (6 if wk != 6 else 5, "Compare the DIFFERENCE each week, not the final heights only." if wk != 6 else "Check the differences again."),
        (1, "In week 1 the plants are the same height."),
        (wk + 1 if wk < 6 else wk - 1, "Work out P − Q for every week and find the largest."),
    ], unit="(week)", sf=1)
    return dict(
        stem=f"A student grows two plants P and Q with different fertilisers and measures their heights each week.\n\n{md_table(['week', 'height of P / cm', 'height of Q / cm'], [[k + 1, P[k], Q[k]] for k in range(6)])}\n\nIn which week is the difference in height between P and Q the largest?",
        options=opts, key=key, misconceptions=mis,
        formula="difference = height of P − height of Q, for each week",
        working=["differences: " + ", ".join(f"week {k + 1}: {d}" for k, d in enumerate(diffs)), f"largest in **week {wk}**", src(2020, 16)],
        hints=["Subtract Q from P for every week.", "Find the biggest answer.", "It is not always the last week."],
    )


@template("np_wave_amp_wavelength_rope", chapter=3, level=3, lo="1.3c", category=CAT)
def wave_amp_wavelength_rope(rng):
    A = nice(rng, 1.5, 2.0, 3.0)
    lam = nice(rng, 16, 20, 24)
    n = 1.5
    L = lam * n
    opts, key, mis = text_options(rng, f"amplitude {A:g} cm, wavelength {lam:g} cm", {
        f"amplitude {A:g} cm, wavelength {lam / 2:g} cm": "Crest to trough is HALF a wavelength.",
        f"amplitude {2 * A:g} cm, wavelength {lam:g} cm": "Amplitude is measured from the rest position, half of crest-to-trough.",
        f"amplitude {2 * A:g} cm, wavelength {L:g} cm": f"The {L:g} cm shown holds 1.5 waves; one wavelength is {lam:g} cm.",
    })
    return dict(
        stem=f"Part of a wave on a rope is shown in Fig. 1: the drawn section is **{L:g} cm** long and holds one and a half waves; the distance from the top of a crest to the bottom of a trough is **{2 * A:g} cm**. Which row gives the amplitude and wavelength?",
        figure=G1.wave(A, lam, n_waves=1.5, show="none"),
        options=opts, key=key, misconceptions=mis,
        formula="amplitude = half of crest-to-trough;  wavelength = length ÷ number of waves",
        working=[f"amplitude = {2 * A:g} ÷ 2 = {A:g} cm", f"wavelength = {L:g} ÷ 1.5 = {lam:g} cm", src(2019, 4)],
        hints=["Amplitude is measured from the rest line.", "How many wavelengths fit in the drawn section?", "1.5."],
    )


# ================================================================ fixed items, grouped by chapter
_ITEMS = [
    # ---------------- Ch 1 Energy
    R("np_forms_of_energy_list", 1, 1, "1.1a",
      f"The table lists groups of words.\n\n{md_table(['list'], [['P: chemical potential, elastic potential, temperature'], ['Q: chemical potential, gravitational potential, kinetic'], ['R: conservation, elastic potential, kinetic'], ['S: elastic potential, power, thermal']])}\n\nWhich list shows only forms of energy?",
      "list Q", {"list P": "Temperature is not a form of energy.", "list R": "Conservation is a principle, not a form of energy.", "list S": "Power is the rate of energy conversion, not a form of energy."},
      ["Cross out any word that is not a form of energy.", "Temperature, conservation and power are not forms.", "Which list has none of those?"], 2023, 1),
    R("np_unit_of_power", 1, 1, "1.1d",
      f"Power is a measure of the rate of energy transfer.\n\n{md_table(['unit'], [['joule'], ['watt'], ['newton'], ['kilogram']])}\n\nWhat is the unit of power?",
      "watt", {"joule": "The joule is the unit of energy.", "newton": "The newton is the unit of force.", "kilogram": "The kilogram is the unit of mass."},
      ["Power is energy per second.", "The unit is named after James Watt.", "W."], 2021, 1),
    R("np_cell_stores", 1, 1, "1.1a",
      f"The table shows two cells (batteries).\n\n{md_table(['object', 'what it does'], [['cell', 'supplies electrical energy when connected in a circuit']])}\n\nWhich type of energy is stored inside a cell?",
      "chemical potential energy", {"elastic potential energy": "Nothing in a cell is stretched or squashed.", "gravitational potential energy": "That depends on height, not on the chemicals inside.", "thermal energy": "A cell is not a store of heat."},
      ["A cell works by chemical reactions.", "Fuels and food store the same form.", "Chemical potential."], 2021, 3),
    R("np_conservation_statement", 1, 1, "1.1c",
      f"The table gives a statement.\n\n{md_table(['statement'], [['When energy is converted from one form to another, the total amount of energy stays the same.']])}\n\nWhat is this statement describing?",
      "the principle of conservation of energy", {"chemical potential energy": "That is one form of energy, not a rule about totals.", "waves": "Waves transfer energy; the statement is about totals staying the same.", "elastic potential energy": "That is one form of energy."},
      ["'Stays the same' means conserved.", "It is a principle about energy.", "Conservation of energy."], 2020, 3),
    R("np_braking_energy_change", 1, 2, "1.1c",
      f"A car travels along a horizontal road at a steady speed. The brakes are applied and the car comes to rest.\n\n{md_table(['before braking', 'after braking'], [['moving, kinetic energy', 'at rest, brakes hot']])}\n\nWhich statement describes the energy change during braking?",
      "kinetic energy is converted to thermal energy", {"gravitational potential energy is converted to thermal energy": "The road is horizontal, so the height does not change.", "gravitational potential energy is converted to kinetic energy": "The car slows down; it does not gain kinetic energy.", "kinetic energy is converted to gravitational potential energy": "The car does not rise."},
      ["What energy does a moving car have?", "Where does it go when friction stops the car?", "Heat in the brakes."], 2017, 5),
    R("np_matchstick_chemical_thermal", 1, 2, "1.1a",
      f"The table lists situations.\n\n{md_table(['situation'], [['a matchstick burning'], ['an electric iron switched on'], ['a television switched on'], ['water boiling in a kettle']])}\n\nIn which situation is chemical energy converted into thermal energy?",
      "a matchstick burning", {"an electric iron switched on": "An iron converts ELECTRICAL energy to thermal energy.", "a television switched on": "A television converts electrical energy to light and sound.", "water boiling in a kettle": "The kettle converts electrical energy to thermal energy."},
      ["Which situation involves a fuel?", "Burning a fuel releases chemical energy.", "The match."], 2017, 9),
    R("np_archer_energy_chain", 1, 3, "1.1c",
      f"An archer pulls a bow string back and releases it so the arrow flies.\n\n{md_table(['stage'], [['1 the archer pulls the string back'], ['2 the bent bow holds the string'], ['3 the arrow flies off']])}\n\nWhich energy changes take place?",
      "kinetic energy of the arm → elastic potential energy in the bow → kinetic energy of the arrow", {"kinetic energy → chemical potential energy → kinetic energy": "The bow stores energy by being BENT, which is elastic potential energy.", "kinetic energy → elastic potential energy → chemical potential energy": "The flying arrow has kinetic energy.", "chemical potential energy → gravitational potential energy → kinetic energy": "The bow is bent, not lifted; it stores elastic potential energy."},
      ["What does a bent bow store?", "Elastic potential energy.", "What does a flying arrow have?"], 2021, 2),
    R("np_pendulum_energy_chain", 1, 2, "1.1c",
      f"A pendulum bob is pulled to one side and released. It swings back and forth until it comes to rest.\n\n{md_table(['stage'], [['released from the raised position'], ['swings through the lowest point'], ['eventually stops']])}\n\nWhich energy transfer shows the energy changes?",
      "gravitational potential energy → kinetic energy → thermal energy", {"elastic potential energy → kinetic energy → thermal energy": "The bob is RAISED, not stretched, so it starts with gravitational potential energy.", "kinetic energy → elastic potential energy → thermal energy": "It starts at rest in a raised position: gravitational potential energy.", "kinetic energy → gravitational potential energy → thermal energy": "The first store is gravitational potential energy, not kinetic."},
      ["What energy does the raised bob have?", "What does it have at the bottom?", "Where does the energy go as it stops?"], 2018, 3),
    R("np_ball_pq_energies", 1, 2, "1.1a",
      f"A ball is held stationary at point P above the floor, then dropped. It bounces on the floor at point Q.\n\n{md_table(['point', 'what the ball is doing'], [['P', 'held still, high up'], ['Q', 'squashed against the floor at the moment of the bounce']])}\n\nWhich row gives the energy the ball has at P and at Q?",
      "P gravitational potential energy; Q elastic potential energy", {"P elastic potential energy; Q gravitational potential energy": "At P the ball is high up and not squashed.", "P gravitational potential energy; Q kinetic energy": "At the moment of the bounce the ball is squashed and momentarily still.", "P kinetic energy; Q gravitational potential energy": "At P the ball is stationary."},
      ["At P the ball is high and still.", "At Q it is squashed.", "Squashed means elastic."], 2019, 2),
    R("np_cold_drink_direction", 1, 2, "1.1b",
      f"On a hot day, a student holds a cold drink containing ice cubes.\n\n{md_table(['object', 'temperature'], [['hand', 'about 35 °C'], ['drink', 'about 2 °C']])}\n\nIn which direction is thermal energy transferred?",
      "from the hand to the drink", {"from the drink to the hand": "Thermal energy flows from the HOTTER object (the hand) to the colder one.", "from the air to the hand": "The air is cooler than the hand; the main flow is hand to drink.", "no transfer takes place": "Objects at different temperatures in contact exchange thermal energy."},
      ["Which is hotter?", "Hot to cold.", "Hand to drink."], 2022, 3),
    R("np_coffee_tea_transfer", 1, 2, "1.1b",
      f"A cup of hot coffee and a cup of iced tea are left on a table in a classroom at 25 °C.\n\n{md_table(['drink', 'temperature / °C'], [['hot coffee', 80], ['iced tea', 5], ['air', 25]])}\n\nWhich shows the correct transfer of thermal energy?",
      "from the coffee to the air, and from the air to the iced tea", {"from the air to the coffee, and from the iced tea to the air": "Energy flows OUT of the hot coffee and INTO the cold tea.", "from the coffee to the air, and from the iced tea to the air": "The tea is colder than the air, so it gains energy.", "from the air to both drinks": "The coffee is hotter than the air, so it loses energy."},
      ["Compare each drink with the air.", "Hot coffee → air.", "Air → iced tea."], 2015, 10),
    R("np_transformer_decreases", 1, 1, "1.1g",
      f"The table describes a transformer.\n\n{md_table(['type', 'input', 'output'], [['step-down', '11 000 V', '230 V']])}\n\nWhich quantity is a step-down transformer designed to decrease?",
      "voltage", {"current": "A step-down transformer lowers the voltage (the current in the output coil is larger).", "power": "A transformer changes the voltage, not the power supplied.", "resistance": "Transformers do not change resistance."},
      ["'Step-down' tells you which quantity goes down.", "11 000 V → 230 V.", "The quantity measured in volts."], 2014, 20),
    R("np_transformer_statement", 1, 2, "1.1g",
      f"A transformer has two coils of wire wound on a metal core.\n\n{md_table(['coil', 'connected to'], [['input coil', 'the supply'], ['output coil', 'the appliance']])}\n\nWhich statement about the transformer is correct?",
      "the input and output voltages are different", {"the core is made from copper": "The core is iron; the coils are copper.", "the current in both coils is the same": "Changing the voltage changes the current too.", "the transformer works from a d.c. supply": "Transformers need a changing (alternating) supply."},
      ["What is a transformer for?", "Changing the voltage.", "Input and output differ."], 2016, 14),
    R("np_fossil_fuel_reason", 1, 2, "1.1e",
      f"The table shows parts of a fossil fuel power station.\n\n{md_table(['part', 'what happens'], [['boiler', '?'], ['turbine', 'turned by steam'], ['generator', 'produces electricity']])}\n\nWhy are fossil fuels burnt in power stations?",
      "to convert water into steam", {"to convert water into electricity": "Water is not turned into electricity; the steam turns a turbine that turns a generator.", "to cool the water": "Burning fuel heats the water.", "to treat waste water": "That is not the job of the furnace."},
      ["What does the boiler do?", "Burning fuel heats water.", "Steam drives the turbine."], 2021, 14),
    R("np_grid_roles", 1, 2, "1.1f",
      f"The table shows parts of the system that provides electrical energy to homes.\n\n{md_table(['part'], [['high-voltage transmission lines'], ['step-up transformer']])}\n\nWhich row correctly describes their roles?",
      "transmission lines: transmitting electricity; step-up transformer: increasing the voltage for transmission", {"transmission lines: increasing the voltage; step-up transformer: transmitting electricity": "The roles are swapped.", "transmission lines: transmitting electricity; step-up transformer: providing kinetic energy to the generator": "The turbine, not a transformer, turns the generator.", "transmission lines: increasing the voltage; step-up transformer: providing kinetic energy": "Lines carry electricity; the step-up transformer raises the voltage."},
      ["Lines carry; transformers change voltage.", "Step-UP raises.", "Match each part to its job."], 2019, 14),
    R("np_transformer_uses_statements", 1, 5, "1.1g",
      f"The table lists statements about transformers.\n\n{md_table(['statement'], [['1  step up the voltage between the transmission lines and the home'], ['2  step down the voltage from the mains supply for charging a laptop'], ['3  step up the voltage for transmission along transmission lines']])}\n\nWhich statements are correct?",
      "2 and 3 only", {"1 only": "Between the lines and the home the voltage is stepped DOWN.", "1 and 2 only": "Statement 1 is wrong: homes need a lower voltage than the lines.", "1, 2 and 3": "Statement 1 is wrong."},
      ["Homes use a LOW voltage.", "Transmission uses a HIGH voltage.", "Chargers step down."], 2021, 15),
    R("np_power_not_needed", 1, 4, "1.1d",
      f"A box is lifted from the floor onto a shelf. The power developed is to be calculated.\n\n{md_table(['quantity'], [['the height of the person lifting the box'], ['the height of the shelf above the floor'], ['the time taken to lift the box'], ['the weight of the box']])}\n\nWhich quantity is NOT required?",
      "the height of the person lifting the box", {"the height of the shelf above the floor": "The energy transferred depends on how high the box is lifted.", "the time taken to lift the box": "Power = energy ÷ time.", "the weight of the box": "The energy needed depends on the weight lifted."},
      ["Power = energy ÷ time.", "Energy to lift depends on weight and height lifted.", "Which quantity has nothing to do with either?"], 2014, 21),
    R("np_most_power_car", 1, 5, "1.1d",
      f"Four identical cars set off on the same road and accelerate for 15 s.\n\n{md_table(['car', 'mass of people inside / kg', 'speed reached after 15 s / km/h'], [['P', 70, 30], ['Q', 140, 30], ['R', 70, 50], ['S', 140, 50]])}\n\nWhich car produces the most power?",
      "S", {"P": "P moves the least mass to the lowest speed in the same time.", "Q": "Q carries more mass but only reaches 30 km/h.", "R": "R reaches 50 km/h but carries less mass than S."},
      ["Power = energy converted ÷ time; the time is the same for all.", "More mass AND more speed means more kinetic energy.", "Which car has both?"], 2022, 5),
    # ---------------- Ch 2 Electricity
    R("np_kwh_unit", 2, 1, "1.2m",
      f"The table lists quantities.\n\n{md_table(['quantity'], [['current'], ['energy'], ['power'], ['time']])}\n\nThe kWh is a unit of which quantity?",
      "energy", {"current": "Current is measured in amperes.", "power": "Power is measured in watts or kilowatts; kWh = kW × hours.", "time": "Time is measured in seconds or hours."},
      ["kWh = kilowatt × hour.", "Power × time = ?", "Energy."], 2015, 1),
    R("np_unit_of_current", 2, 1, "1.2a",
      f"The table lists units.\n\n{md_table(['unit'], [['ampere'], ['ohm'], ['volt'], ['watt']])}\n\nWhich is the unit of current?",
      "ampere", {"ohm": "The ohm is the unit of resistance.", "volt": "The volt is the unit of voltage.", "watt": "The watt is the unit of power."},
      ["Current is measured by an ammeter.", "The unit's symbol is A.", "Ampere."], 2018, 8),
    R("np_unit_of_resistance", 2, 1, "1.2a",
      f"The table lists units.\n\n{md_table(['unit'], [['ampere'], ['ohm'], ['volt'], ['watt']])}\n\nWhich is the unit of electrical resistance?",
      "ohm", {"ampere": "The ampere is the unit of current.", "volt": "The volt is the unit of voltage.", "watt": "The watt is the unit of power."},
      ["Resistance has the Greek-letter symbol Ω.", "The unit is named after Georg Ohm.", "Ohm."], 2021, 10),
    R("np_saw_power_rating", 2, 1, "1.2k",
      f"A new electric saw has this information on its box.\n\n{md_table(['information'], [['1700 W'], ['460 revolutions per minute'], ['230 mm blade'], ['6.9 kg']])}\n\nWhat is the power rating of the saw?",
      "1700 W", {"460 revolutions per minute": "That is the speed of rotation.", "230 mm blade": "That is the blade size.", "6.9 kg": "That is the mass."},
      ["Power is measured in watts.", "Find the value in W.", "The first line of the box."], 2020, 2),
    R("np_power_equation", 2, 1, "1.2l",
      f"The table lists equations.\n\n{md_table(['equation'], [['power = voltage × current'], ['power = voltage ÷ current'], ['power = voltage × current × time'], ['power = voltage × current ÷ time']])}\n\nWhich equation gives the electrical power of a resistor?",
      "power = voltage × current", {"power = voltage ÷ current": "Power is the PRODUCT of voltage and current.", "power = voltage × current × time": "That is the ENERGY transferred.", "power = voltage × current ÷ time": "Power already is a rate; do not divide by time."},
      ["P = IV.", "Multiply current and voltage.", "No time in the equation."], 2018, 11),
    R("np_what_causes_current", 2, 1, "1.2a",
      f"The table lists items in a circuit.\n\n{md_table(['item'], [['ammeter'], ['fuse'], ['resistance'], ['voltage']])}\n\nWhat causes a current in an electrical circuit?",
      "voltage", {"ammeter": "An ammeter measures current; it does not cause it.", "fuse": "A fuse protects the circuit.", "resistance": "Resistance OPPOSES current."},
      ["What provides the energy to push charge round?", "Think about what the cell provides.", "Voltage."], 2023, 9),
    R("np_series_current_statement", 2, 1, "1.2d",
      f"The table lists statements about current.\n\n{md_table(['statement'], [['current is the same at every point of a parallel circuit'], ['current is the same at every point of a series circuit'], ['keeping the voltage constant and increasing the current decreases the power'], ['the unit of current is the ohm']])}\n\nWhich statement is correct?",
      "current is the same at every point of a series circuit", {"current is the same at every point of a parallel circuit": "In parallel the current splits between the branches.", "keeping the voltage constant and increasing the current decreases the power": "Power = current × voltage, so more current means MORE power.", "the unit of current is the ohm": "The unit of current is the ampere."},
      ["Series: one path.", "The same current everywhere along one path.", "Pick that statement."], 2020, 5),
    R("np_batteries_items", 2, 1, "1.2a",
      f"The table lists items.\n\n{md_table(['item'], [['1  laptop computers'], ['2  mobile phones'], ['3  portable radios'], ['4  motor cars']])}\n\nIn which items can batteries be used as a source of electricity?",
      "1, 2, 3 and 4", {"1, 2 and 3 only": "Cars have a battery that starts the engine and runs the lights.", "2 and 4 only": "Laptops and portable radios also run on batteries.", "3 and 4 only": "Laptops and phones have batteries too."},
      ["Which items work without being plugged in?", "A car has a battery as well.", "All four."], 2023, 13),
    R("np_reduce_wastage", 2, 1, "1.2o",
      f"The table lists actions.\n\n{md_table(['action'], [['brushing your teeth with an electric toothbrush'], ['using the air-conditioning for 24 hours'], ['switching off the lights when you leave a room'], ['using a hairdryer to dry your hair']])}\n\nWhich action reduces electrical energy wastage at home?",
      "switching off the lights when you leave a room", {"brushing your teeth with an electric toothbrush": "That uses electricity rather than saving it.", "using the air-conditioning for 24 hours": "That wastes a great deal of energy.", "using a hairdryer to dry your hair": "A hairdryer uses electricity; a towel would use none."},
      ["Which action stops electricity being used for nothing?", "Lights in an empty room.", "Switch them off."], 2021, 12),
    R("np_parallel_main_current", 2, 2, "1.2e",
      "Fig. 1 shows a parallel circuit with two lamps. At which point is the current greatest?",
      "next to the cell, where the two branch currents have joined", {"in the branch with the first lamp": "A branch carries only part of the total current.", "in the branch with the second lamp": "A branch carries only part of the total current.", "the current is the same at every point": "In parallel the current splits between the branches and rejoins."},
      ["The current splits at the junction.", "Where is it all together again?", "Next to the cell."], 2021, 11,
      fig=lambda rng: S.circuit([], parallel=[["lamp"], ["lamp"]], top=("cell",))),
    R("np_three_lamps_series_current", 2, 2, "1.2d",
      "Fig. 1 shows three lamps X, Y and Z connected in series. Which statement is correct?",
      "the current in all the lamps is the same", {"the current in lamp X is the largest": "In a series circuit the current is the same at every point.", "the current in lamp Y is the largest": "There is only one path, so the current is the same everywhere.", "the current in lamp Z is the largest": "Current is not used up along the loop."},
      ["How many paths for the current?", "One.", "Same current at every point."], 2014, 1,
      fig=lambda rng: S.circuit(["lamp", "lamp", "lamp"], top=("cell",), labels=["X", "Y", "Z"])),
    R("np_parallel_p_equals", 2, 2, "1.2e",
      "Fig. 1 shows two resistors in parallel connected to a battery. The current from the battery is P and the currents through the resistors are Q and R. What is the size of P?",
      "Q + R", {"Q − R": "The branch currents add; they are not subtracted.", "Q × R": "Currents are added, not multiplied.", "Q ÷ R": "Currents are added, not divided."},
      ["The current from the battery splits into the two branches.", "What splits must add back up.", "Add the branch currents."], 2015, 3,
      fig=lambda rng: S.circuit(["ammeter"], parallel=[["resistor"], ["resistor"]], top=("battery",), labels=["P", "Q", "R"])),
    R("np_series_point_q", 2, 1, "1.2d",
      "Fig. 1 shows a series circuit with two lamps. The current at point P (before the first lamp) is 1.2 A. What is the current at point Q (after the second lamp)?",
      "1.2 A", {"0.6 A": "The current is not shared between lamps in series.", "2.4 A": "The current does not add up around a series loop.", "0 A": "Current is not used up by the lamps."},
      ["One path only.", "Same current at every point.", "The same as at P."], 2015, 25,
      fig=lambda rng: S.circuit(["ammeter", "lamp", "lamp", "ammeter"], top=("cell",), labels=["P", "", "", "Q"])),
    R("np_battery_behaviour", 2, 2, "1.2a",
      f"The table lists statements about a battery.\n\n{md_table(['statement'], [['it delivers current from the negative to the positive terminal outside the battery'], ['it delivers current when it is disconnected'], ['it delivers current when it is connected to a resistor'], ['it is made from two coils of wire on an iron core']])}\n\nWhich statement describes the behaviour of a battery?",
      "it delivers current when it is connected to a resistor", {"it delivers current from the negative to the positive terminal outside the battery": "Conventional current goes from positive to negative outside the battery.", "it delivers current when it is disconnected": "A current needs a complete circuit.", "it is made from two coils of wire on an iron core": "That describes a transformer."},
      ["A current needs a closed path.", "Connecting a resistor completes the circuit.", "Then current flows."], 2015, 19),
    R("np_fuse_purpose_3a", 2, 2, "1.2a",
      f"A television is fitted with a 3 A fuse and connected to the 230 V mains.\n\n{md_table(['fuse rating', 'mains voltage'], [['3 A', '230 V']])}\n\nWhat is the purpose of the fuse?",
      "to break the circuit when the current is greater than 3 A", {"to break the circuit when the mains supply is lower than 230 V": "A fuse responds to current, not to a low voltage.", "to keep the current in the circuit at 3 A": "A fuse does not control the normal current.", "to keep the mains voltage at 230 V": "A fuse does not control the voltage."},
      ["A fuse is a thin wire.", "It melts when the current is too large.", "Larger than its rating."], 2015, 22),
    R("np_blown_fuse_cause", 2, 2, "1.2a",
      f"A student's circuit has a 5 A fuse. The fuse has blown and stopped the current.\n\n{md_table(['observation'], [['fuse wire melted'], ['bulb undamaged']])}\n\nWhat could have caused this?",
      "the current was too large", {"the bulb was loose": "A loose bulb breaks the circuit; it does not melt the fuse.", "the fuse rating was too high": "A high rating makes a fuse LESS likely to blow.", "the voltage was too small": "A small voltage means a small current."},
      ["What melts a fuse?", "A current above its rating.", "Too large a current."], 2013, 7),
    R("np_series_parallel_resistance_row", 2, 2, "1.2h",
      f"Two circuits each contain one cell and one bulb. A second bulb is added to each: in series in one circuit, in parallel in the other.\n\n{md_table(['circuit', 'second bulb added'], [['X', 'in series'], ['Y', 'in parallel']])}\n\nWhich row describes the change in effective resistance?",
      "X increases; Y decreases", {"X increases; Y increases": "Adding a branch in parallel gives the current another path, so the resistance FALLS.", "X decreases; Y decreases": "Adding a bulb in series adds resistance.", "X decreases; Y increases": "Both are the wrong way round."},
      ["Series adds resistance.", "Parallel adds paths.", "More paths, less resistance."], 2022, 12),
    R("np_fan_power_calc", 2, 2, "1.2l",
      f"An electric fan has a label.\n\n{md_table(['label'], [['230 V  50 Hz  0.2 A']])}\n\nWhich calculation gives the power of the fan, in W?",
      "0.2 × 230", {"230 ÷ 0.2": "Power = current × voltage, a product.", "50 × 230": "50 Hz is the frequency, not the current.", "0.2 ÷ 230": "Multiply the current by the voltage."},
      ["Power = current × voltage.", "Which two numbers are current and voltage?", "0.2 A and 230 V."], 2022, 13),
    R("np_ceiling_lamps_cooker", 2, 2, "1.2j",
      f"The table shows two sets of components.\n\n{md_table(['situation'], [['ceiling lamps in a house'], ['heating elements on an electric cooker']])}\n\nWhich type of circuit is used in these situations?",
      "both in parallel", {"both in series": "Each lamp and each element must work on its own.", "lamps in parallel; cooker elements in series": "Each element has its own switch, so they are in parallel.", "lamps in series; cooker elements in parallel": "Lamps are in parallel so one can be switched off alone."},
      ["Can you switch one ceiling lamp off alone?", "Can you use one cooker plate alone?", "Both need parallel."], 2019, 12),
    R("np_circuit_instructions", 2, 3, "1.2a",
      "Fig. 1 shows a circuit with a battery, a variable resistor, a bulb and an ammeter in one loop, and a voltmeter across the bulb. Which set of instructions builds it?",
      "connect the battery, variable resistor, bulb and ammeter in series, then connect the voltmeter in parallel with the bulb", {"connect the bulb in series with the battery, with the variable resistor and ammeter in parallel to each other, then the voltmeter across the bulb": "The variable resistor and ammeter are in the same loop as the bulb, not in parallel.", "connect the bulb, variable resistor and ammeter in parallel to the battery, then the voltmeter in series": "A voltmeter is always in parallel.", "connect the voltmeter in parallel with the battery, bulb, variable resistor and ammeter together": "The voltmeter must be across the bulb only."},
      ["Everything in one loop is in series.", "The voltmeter goes across the bulb.", "Series first, then the voltmeter in parallel."], 2018, 9,
      fig=lambda rng: S.circuit(["variable", "lamp", "ammeter"], top=("battery",), voltmeter_across=1)),
    R("np_greatest_resistance_circuit", 2, 3, "1.2h",
      f"Four circuits use identical resistors.\n\n{md_table(['circuit', 'arrangement'], [['P', 'two resistors in series'], ['Q', 'two resistors in parallel'], ['R', 'three resistors in series'], ['S', 'three resistors in parallel']])}\n\nWhich circuit has the greatest effective resistance?",
      "R", {"P": "Three in series is more than two in series.", "Q": "Parallel resistors give a SMALLER effective resistance.", "S": "Three in parallel is the smallest of all."},
      ["Series adds up.", "More resistors in series, more resistance.", "Three in series."], 2018, 10),
    R("np_a1_a2_readings", 2, 3, "1.2e",
      "Fig. 1 shows ammeter A₁ next to the battery and ammeter A₂ in one branch of a parallel circuit with two bulbs. Which statement explains the readings?",
      "A₁ has the highest reading because it measures the total current in both bulbs", {"A₁ and A₂ have the same reading because they are in the same circuit": "A₂ carries only the current of one branch.", "A₂ has the highest reading because it is close to a bulb": "Being close to a bulb does not increase the current.", "A₁ has the lowest reading because there are no bulbs at that point": "A₁ carries the SUM of the branch currents."},
      ["Where does the current split?", "A₁ is before the split.", "It carries the total."], 2023, 10,
      fig=lambda rng: S.circuit(["ammeter"], parallel=[["ammeter", "lamp"], ["lamp"]], top=("battery",), labels=["A₁", "A₂", ""])),
    R("np_xyz_components", 2, 3, "1.2c",
      "Fig. 1 shows a circuit used to find the resistance of a length of wire: a component in the main loop (X), a component in parallel across it (Y) and a component in series with the battery (Z). Which components should be placed at X, Y and Z?",
      "X the length of wire, Y the voltmeter, Z the ammeter", {"X the ammeter, Y the voltmeter, Z the length of wire": "The voltmeter must be ACROSS the wire, so the wire is at X.", "X the voltmeter, Y the ammeter, Z the length of wire": "The ammeter goes in series; the voltmeter in parallel.", "X the length of wire, Y the ammeter, Z the voltmeter": "Swap: voltmeter across, ammeter in series."},
      ["The voltmeter goes across the wire.", "The ammeter goes in the loop.", "So Y is the voltmeter."], 2016, 10,
      fig=lambda rng: S.circuit(["resistor", "ammeter"], top=("battery",), voltmeter_across=0, labels=["X", "Z"])),
    R("np_remove_r2_series", 2, 5, "1.2h",
      "Fig. 1 shows two identical resistors R₁ and R₂ in series with a cell, an ammeter and a voltmeter across R₁. R₂ is then removed and the gap closed with a wire. What happens to the ammeter and voltmeter readings?",
      "ammeter increases; voltmeter increases", {"ammeter decreases; voltmeter decreases": "Less resistance means MORE current.", "ammeter increases; voltmeter decreases": "R₁ now has the whole cell voltage across it, so the voltmeter reading rises.", "ammeter decreases; voltmeter increases": "Removing a resistor lowers the total resistance, so the current rises."},
      ["Removing a series resistor lowers the total resistance.", "Lower resistance → more current.", "R₁ now gets the whole cell voltage."], 2015, 9,
      fig=lambda rng: S.circuit(["resistor", "resistor", "ammeter"], top=("cell",), voltmeter_across=0, labels=["R₁", "R₂", ""])),
    # ---------------- Ch 3 Wave
    R("np_light_transfers_energy", 3, 3, "1.3b",
      f"The table lists statements about light.\n\n{md_table(['statement'], [['light can be reflected'], ['light can be used to power calculators'], ['light can form shadows'], ['light travels at a high speed']])}\n\nWhich statement shows that light waves transfer energy?",
      "light can be used to power calculators", {"light can be reflected": "Reflection does not show that energy is delivered.", "light can form shadows": "Shadows show light is blocked, not that energy is transferred.", "light travels at a high speed": "Speed does not show energy transfer."},
      ["Which statement shows light DOING something useful?", "Powering a calculator needs energy.", "The solar cell receives it."], 2017, 1),
    R("np_optical_fibre_remote", 3, 1, "1.3d",
      f"A television receives signals through an optical fibre, and a remote control switches it on and off.\n\n{md_table(['device'], [['optical fibre'], ['remote control']])}\n\nWhich row gives the waves used?",
      "optical fibre: visible light; remote control: infrared", {"optical fibre: infrared; remote control: ultraviolet": "Remotes use infrared; fibres carry light.", "optical fibre: microwaves; remote control: ultraviolet": "Microwaves are for ovens and satellites.", "optical fibre: visible light; remote control: radio waves": "Remotes use infrared, not radio."},
      ["'Optical' means light.", "Remote controls use infrared.", "Light and infrared."], 2018, 5),
    R("np_optical_fibre_wave", 3, 1, "1.3d",
      f"The table lists waves.\n\n{md_table(['wave'], [['light'], ['microwave'], ['ultraviolet'], ['X-ray']])}\n\nWhich type of wave is used in optical fibres for telecommunications?",
      "light", {"microwave": "Microwaves are used in ovens and satellite links.", "ultraviolet": "Ultraviolet is used for sterilising and sunbeds.", "X-ray": "X-rays are used for imaging bones."},
      ["Optical means to do with seeing.", "Light travels along the glass fibre.", "Light."], 2021, 6),
    R("np_water_waves_electricity", 3, 1, "1.3b",
      f"Wave-power stations use water waves to produce electricity.\n\n{md_table(['statement'], [['water waves transfer energy'], ['water waves transfer electricity'], ['water waves transfer time'], ['water waves transfer water']])}\n\nWhich statement explains why water waves can produce electricity?",
      "water waves transfer energy", {"water waves transfer electricity": "The waves carry energy, which a generator turns into electricity.", "water waves transfer time": "Time is not transferred.", "water waves transfer water": "The water only moves up and down; the energy travels."},
      ["What does any wave carry?", "Energy.", "The generator converts it."], 2020, 7),
    R("np_rope_wave_direction", 3, 2, "1.3a",
      f"A rope is tied to a post at T. A man at S moves his hand up and down to make a wave travel along the rope. P is a point on the rope.\n\n{md_table(['item'], [['the wave'], ['point P on the rope']])}\n\nWhich row is correct?",
      "the wave travels from S to T; point P moves up and down", {"the wave travels from T to S; point P moves up and down": "The wave starts at the hand (S) and travels towards the post (T).", "the wave travels from S to T; point P moves left to right": "Points on the rope move up and down, like the hand.", "the wave travels from T to S; point P moves left to right": "Both parts are wrong."},
      ["Where does the wave start?", "At the hand.", "The rope goes up and down with the hand."], 2020, 6),
    R("np_hand_direction_wave", 3, 2, "1.3a",
      f"A student holds one end of a rope and moves her hand up and down. The other end is fixed.\n\n{md_table(['motion'], [['hand: up and down']])}\n\nWhat is the direction of the wave motion?",
      "along the rope, away from the hand", {"up and down, like the hand": "That is the motion of each piece of rope, not the direction the wave travels.", "towards the hand": "The wave moves away from the source.", "there is no wave motion": "The vibration sends a wave along the rope."},
      ["The hand is the source.", "The wave travels away from the source.", "Along the rope."], 2023, 3),
    R("np_uses_pairs_light", 3, 4, "1.3d",
      f"The table lists waves with two claimed uses each.\n\n{md_table(['wave', 'uses'], [['light', 'optical fibres and vision'], ['radio waves', 'communications and sterilisation'], ['ultraviolet', 'thermal cameras and sunbeds'], ['X-rays', 'radiography and remote control']])}\n\nWhich row shows two correct uses?",
      "light: optical fibres and vision", {"radio waves: communications and sterilisation": "Sterilisation uses ultraviolet.", "ultraviolet: thermal cameras and sunbeds": "Thermal cameras use infrared.", "X-rays: radiography and remote control": "Remote controls use infrared."},
      ["Check each pair.", "Sterilisation, thermal cameras and remotes belong to other waves.", "Only one row has both correct."], 2022, 6),
    R("np_wave_amplitude_half_cm", 3, 1, "1.3c",
      "Fig. 1 shows a wave. What is the amplitude of the wave?",
      "0.5 cm", {"1.0 cm": "That is crest to trough; the amplitude is from the rest line to a crest.", "2.0 cm": "That is the wavelength.", "6.0 cm": "That is the length of rope shown."},
      ["Find the rest line.", "How high is a crest above it?", "Read the vertical scale."], 2016, 5,
      fig=lambda rng: G1.wave(0.5, 2.0, n_waves=3, show="none")),
    # ---------------- Ch 4 Effects of Force
    R("np_dt_graph_constant_speed", 4, 1, "1.4g",
      f"The table describes four distance-time graphs.\n\n{md_table(['graph', 'shape'], [['P', 'a straight line sloping upwards'], ['Q', 'a flat horizontal line'], ['R', 'a curve getting steeper'], ['S', 'a curve getting flatter']])}\n\nWhich graph shows a body moving at constant speed?",
      "P", {"Q": "A flat line means the body is stationary.", "R": "A curve getting steeper means speeding up.", "S": "A curve getting flatter means slowing down."},
      ["Constant speed covers equal distances in equal times.", "That gives a straight slope.", "The straight sloping one."], 2014, 2),
    R("np_apparatus_30m", 4, 1, "1.4a",
      f"A student wants to measure how fast his friends can run 30 m.\n\n{md_table(['apparatus'], [['30 cm ruler'], ['40 m measuring tape'], ['metre ruler'], ['stopwatch']])}\n\nWhich is the best apparatus to measure the 30 m distance?",
      "40 m measuring tape", {"30 cm ruler": "Far too short for 30 m.", "metre ruler": "It would have to be moved 30 times.", "stopwatch": "A stopwatch measures time, not distance."},
      ["30 m is long.", "Which instrument reaches 30 m in one go?", "The tape."], 2019, 1),
    R("np_instruments_50m", 4, 1, "1.4b",
      f"A teacher wants to find out how quickly a student can run 50 m.\n\n{md_table(['instrument for distance', 'instrument for time'], [['10 m measuring tape or 30 cm ruler', 'stopwatch or wall clock']])}\n\nWhich row shows the instruments the teacher should use?",
      "10 m measuring tape and a stopwatch", {"10 m measuring tape and a wall clock": "A wall clock cannot time to the nearest second easily.", "30 cm ruler and a stopwatch": "A 30 cm ruler is far too short.", "30 cm ruler and a wall clock": "Both are poor choices."},
      ["Which measures a long distance?", "Which times a short interval precisely?", "Tape and stopwatch."], 2023, 4),
    R("np_units_speed_acceleration", 4, 1, "1.4d",
      f"The table lists units.\n\n{md_table(['unit'], [['m/s'], ['m/s²'], ['m/s³']])}\n\nWhich row shows the correct units of speed and acceleration?",
      "speed m/s; acceleration m/s²", {"speed m/s²; acceleration m/s": "Swapped.", "speed m/s; acceleration m/s³": "Acceleration is change in speed (m/s) per second: m/s².", "speed m/s²; acceleration m/s³": "Speed is in m/s."},
      ["Speed is distance per second.", "Acceleration is speed per second.", "m/s and m/s²."], 2023, 6),
    R("np_acceleration_equation", 4, 1, "1.4f",
      f"The table lists equations.\n\n{md_table(['equation'], [['change in speed ÷ time taken'], ['change in speed × time taken'], ['distance travelled × time taken'], ['distance travelled ÷ time taken']])}\n\nWhich equation is used to calculate acceleration?",
      "change in speed ÷ time taken", {"change in speed × time taken": "Acceleration is a rate: divide by time.", "distance travelled × time taken": "That is not a physical quantity here.", "distance travelled ÷ time taken": "That is average speed."},
      ["Acceleration is how fast the speed changes.", "Change in speed per second.", "Divide by time."], 2019, 7),
    R("np_racket_no_change", 4, 2, "1.4c",
      f"A tennis racket hits a ball.\n\n{md_table(['item'], [['direction of movement of the ball'], ['mass of the racket'], ['shape of the ball'], ['shape of the racket strings']])}\n\nWhat does NOT change when the racket hits the ball?",
      "the mass of the racket", {"the direction of movement of the ball": "The ball is sent back the other way.", "the shape of the ball": "The ball is squashed for an instant.", "the shape of the racket strings": "The strings bend briefly."},
      ["A force can change shape, size and motion.", "What can a force never change?", "Mass."], 2017, 8),
    R("np_must_be_accelerating", 4, 3, "1.4d",
      f"The table lists moving objects.\n\n{md_table(['object'], [['an aeroplane cruising in the upper atmosphere'], ['a person skiing downhill at a steady speed'], ['a stone immediately after being dropped from a cliff'], ['a train passing slowly through a station']])}\n\nWhich must be accelerating?",
      "a stone immediately after being dropped from a cliff", {"an aeroplane cruising in the upper atmosphere": "Cruising means a steady speed.", "a person skiing downhill at a steady speed": "Steady speed means zero acceleration.", "a train passing slowly through a station": "Slow does not mean accelerating."},
      ["Accelerating means the speed is changing.", "A dropped stone speeds up from rest.", "That one."], 2013, 20),
    R("np_cyclist_friction_less", 4, 3, "1.4c",
      f"A cyclist moves at a steady speed with the forward force equal to friction. Then the forces change.\n\n{md_table(['before', 'after'], [['forward force = friction', 'friction is now less than the forward force']])}\n\nWhat is the effect of this change?",
      "the cyclist speeds up", {"the cyclist continues at the same steady speed": "The forces are no longer balanced.", "the cyclist slows down": "The forward force is now the larger one.", "the cyclist stops": "A net forward force makes the cyclist go faster."},
      ["Which force is bigger now?", "The forward force.", "Net force forward → speeds up."], 2023, 8),
    R("np_rocket_forces", 4, 3, "1.4c",
      f"A rocket speeds up as it moves upward. Three forces act on it.\n\n{md_table(['force', 'direction'], [['thrust', 'upward'], ['drag', 'downward'], ['gravity', 'downward']])}\n\nWhich statement describes the forces?",
      "thrust is greater than drag plus gravity", {"drag is greater than gravity": "Comparing the two downward forces does not explain the upward acceleration.", "drag plus gravity is greater than thrust": "Then the rocket would slow down or fall.", "gravity is greater than thrust": "Then the rocket could not rise."},
      ["The rocket speeds up UPWARD.", "The upward force must beat both downward forces together.", "Thrust > drag + gravity."], 2022, 10),
    R("np_beam_balanced_action", 4, 4, "1.4h",
      "Fig. 1 shows a beam pivoted at its centre with two equal weights fixed at equal distances, so it is balanced. Which action rotates the beam so that the LEFT side goes down?",
      "move weight 1 (on the left) further to the left", {"remove weight 1": "That would make the RIGHT side go down.", "double the mass of weight 2 (on the right)": "That makes the right side go down.", "move weight 2 closer to the pivot and weight 1 closer to the pivot by the same amount": "Both turning effects fall equally; it stays balanced."},
      ["A force further from the pivot has a bigger turning effect.", "Which change increases the left side's turning effect?", "Move the left weight outwards."], 2019, 8,
      fig=lambda rng: S.lever(pivot_frac=0.5, load=("weight 1", 0.2), effort=("weight 2", 0.8))),
    # ---------------- Ch 5 Sources of Food
    R("np_fertilisers_why", 5, 1, "2.1c",
      f"The table lists reasons.\n\n{md_table(['reason'], [['to kill pests living on the crop'], ['to kill weeds growing with the crop'], ['to make the crop grow faster'], ['to reduce the acidity of the soil']])}\n\nWhy do farmers often use fertilisers on their crops?",
      "to make the crop grow faster", {"to kill pests living on the crop": "That is a pesticide.", "to kill weeds growing with the crop": "That is a herbicide.", "to reduce the acidity of the soil": "That is lime."},
      ["Fertilisers provide nutrients.", "What do nutrients do for a plant?", "Faster, bigger growth."], 2019, 15),
    R("np_predators_pest_control", 5, 1, "2.1e",
      f"Some farmers use predators to reduce the number of pests on their crops.\n\n{md_table(['type of pest control'], [['biological'], ['hormone'], ['intensive'], ['pesticide']])}\n\nWhich type of pest control is this?",
      "biological", {"hormone": "Plant hormones control growth and ripening or kill weeds.", "intensive": "Intensive farming is about producing more from the same space.", "pesticide": "Pesticides are chemicals, not living predators."},
      ["A living predator is used.", "The word for using living things.", "Biological control."], 2019, 16),
    R("np_biological_control_action", 5, 1, "2.1e",
      f"The table lists actions.\n\n{md_table(['action'], [['adding artificial fertiliser to the soil'], ['adding insects to a crop to eat other insects'], ['spraying plants with pesticides to kill insects'], ['using slash-and-burn to clear land']])}\n\nWhich action is biological control?",
      "adding insects to a crop to eat other insects", {"adding artificial fertiliser to the soil": "Fertiliser feeds plants; it is not pest control.", "spraying plants with pesticides to kill insects": "That is chemical control.", "using slash-and-burn to clear land": "That clears land; it is not pest control."},
      ["Biological control uses living things.", "Which action adds a living predator?", "The insects that eat other insects."], 2018, 16),
    R("np_plant_conditions_row", 5, 1, "2.1a",
      f"Four seedlings are grown in different conditions.\n\n{md_table(['seedling', 'light', 'fertiliser', 'watering'], [['P', 'bright', 'no', 'daily'], ['Q', 'bright', 'yes', 'daily'], ['R', 'dark', 'no', 'once a week'], ['S', 'dark', 'yes', 'once a week']])}\n\nWhich seedling has the best conditions for growth?",
      "Q", {"P": "P has no fertiliser, so fewer nutrients than Q.", "R": "R has no light, no fertiliser and little water.", "S": "S has no light and little water."},
      ["Plants need light, water and nutrients.", "Which row has all three?", "Only one row does."], 2018, 15),
    R("np_hormone_uses_statements", 5, 2, "2.1g",
      f"The table lists statements about plant hormones in agriculture.\n\n{md_table(['statement'], [['1  to act as a weedkiller'], ['2  to regulate plant growth'], ['3  to improve plant varieties'], ['4  to ripen fruits']])}\n\nWhich statements give uses of plant hormones?",
      "1, 2 and 4", {"1 and 3": "Hormones do not improve varieties; that is done by breeding and selection.", "1, 2 and 3": "Statement 3 is not a hormone use; statement 4 is.", "2, 3 and 4": "Statement 3 is wrong; statement 1 (weedkiller) is right."},
      ["Plant hormones: weedkillers, growth, ripening.", "Improving varieties is a different method.", "Three of the four statements are right."], 2016, 15),
    R("np_phosphate_fish_harm", 5, 4, "2.1d",
      f"A flow chart shows what happens when phosphate detergent (a plant nutrient) gets into a pond.\n\n{md_table(['step'], [['phosphate gets into the pond'], ['algae grow rapidly'], ['less light reaches plants at the bottom, which die'], ['bacteria feed on the dead plants and use up the oxygen'], ['fish die']])}\n\nWhy is the detergent harmful to fish?",
      "it leads to low levels of oxygen in the water", {"increased light levels heat the water": "The algae REDUCE the light reaching the bottom.", "the fish are poisoned by the algae": "The algae are not poisonous; the problem is the oxygen used up when plants decay.", "there are fewer bacteria for the fish to feed on": "There are MORE bacteria, and they use up the oxygen."},
      ["Follow the chart to the end.", "What do the bacteria use up?", "Oxygen."], 2021, 19),
    R("np_phosphate_effect_rivers", 5, 2, "2.1d",
      f"Phosphate detergents, which act as plant nutrients, often pollute rivers.\n\n{md_table(['possible effect'], [['decrease in growth of microbes'], ['decrease in growth of water weeds'], ['increase in growth of algae'], ['increase in growth of fish']])}\n\nWhat is an effect of phosphate detergents on rivers?",
      "an increase in the growth of algae", {"a decrease in the growth of microbes": "Microbes increase as they feed on the extra dead plants.", "a decrease in the growth of water weeds": "Nutrients make water weeds and algae grow MORE.", "an increase in the growth of fish": "Fish die as the oxygen is used up."},
      ["Phosphate is a nutrient.", "What grows when nutrients are added to water?", "Algae."], 2023, 17),
]

for _ch in range(1, 6):
    register_explain([d for c, d in _ITEMS if c == _ch], chapter=_ch, category=CAT)
