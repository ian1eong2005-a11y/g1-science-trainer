"""Ch 4 Effects of Force: extra calculation / data templates adapted from the 1.4 assignments (1, 2, 3) and Mastery Test 1,
plus explanation items from the same worksheets. Numbers are varied on every serve."""
from .. import figs, sketches_g1 as G1
from .base import fmt, md_table, nice, numeric_options, pick, register_explain, template, text_options

KP = lambda label, *phr: {"label": label, "any": list(phr)}
SRC = "_Adapted from the QTSS 1.4 Forces worksheets._"


def _sw(t):
    m = int(t // 60)
    return f"{m}:{t - 60 * m:05.2f}"


# ---------------------------------------------------------------- L1
@template("c04w_net_force_box", chapter=4, level=1, lo="1.4c")
def net_force_box(rng):
    a = nice(rng, 5, 7, 10)
    b = nice(rng, 2, 3, 4)
    same = rng.random() < 0.4
    if same:
        net, d = a + b, "right"
        fig = G1.pushes((a + b, 0))
        stem = f"Fig. 1 shows a box pushed from the left by two people with forces of {a} N and {b} N in the same direction (shown as one {a + b} N push). What is the net force, and which way does the box move?"
    else:
        net, d = a - b, "right"
        fig = G1.pushes((a, b))
        stem = f"Fig. 1 shows a box pushed to the right with {a} N and to the left with {b} N. What is the net force, and which way does the box move?"
    opts, key, mis = text_options(rng, f"{net} N to the {d}", {
        f"{a + b if not same else a} N to the right": "Forces in opposite directions are subtracted; forces in the same direction are added.",
        f"{net} N to the left": "The net force points in the direction of the LARGER force.",
        "0 N, the box does not move": "The forces are not equal, so they do not cancel.",
    })
    return dict(
        stem=stem, figure=fig,
        options=opts, key=key, misconceptions=mis,
        formula="net force = larger force − smaller force (opposite directions); = sum (same direction)",
        working=[f"net force = {a} {'+' if same else '−'} {b} = {net} N", f"direction: **{d}**", SRC],
        hints=["Are the forces in the same or opposite directions?", "Same: add. Opposite: subtract.", "The box moves the way the bigger force points."],
    )


@template("c04w_time_from_kmh", chapter=4, level=1, lo="1.4e")
def time_from_kmh(rng):
    v = nice(rng, 40, 50, 60, 80)
    d = v * nice(rng, 1.5, 2, 3)
    t = d / v
    opts, key, mis = numeric_options(rng, t, [
        (d * v, "Time = distance ÷ speed; do not multiply."),
        (v / d, "Upside down: distance ÷ speed."),
        (d, "That is the distance; divide by the speed."),
    ], unit="h", sf=3)
    return dict(
        stem=f"A car travels at a steady speed.\n\n{md_table(['speed / km/h', 'distance / km'], [[v, d]])}\n\nHow long does the journey take?",
        options=opts, key=key, misconceptions=mis,
        formula="time = distance ÷ speed",
        working=[f"t = {d:g} ÷ {v}", f"= **{fmt(t)} h**", SRC],
        hints=["Rearrange speed = distance ÷ time.", "time = distance ÷ speed.", f"{d:g} ÷ {v}."],
    )


@template("c04w_distance_from_kmh", chapter=4, level=1, lo="1.4e")
def distance_from_kmh(rng):
    v = nice(rng, 50, 60, 80, 90)
    t = nice(rng, 0.5, 1.5, 2, 3)
    d = v * t
    opts, key, mis = numeric_options(rng, d, [
        (v / t, "Distance = speed × time; do not divide."),
        (v + t, "Multiply, do not add."),
        (v, "That is the speed; multiply by the time."),
    ], unit="km", sf=3)
    return dict(
        stem=f"A car travels at a steady speed.\n\n{md_table(['speed / km/h', 'time / h'], [[v, t]])}\n\nWhat distance does it travel?",
        options=opts, key=key, misconceptions=mis,
        formula="distance = speed × time",
        working=[f"d = {v} × {t:g}", f"= **{fmt(d)} km**", SRC],
        hints=["Distance = speed × time.", f"{v} × {t:g}.", "Kilometres."],
    )


@template("c04w_ruler_damaged_end", chapter=4, level=1, lo="1.4a")
def ruler_damaged_end(rng):
    start = nice(rng, 1.0, 2.0, 1.5)
    L = nice(rng, 4.3, 4.6, 5.2, 6.1)
    end = round(start + L, 1)
    opts, key, mis = numeric_options(rng, L * 10, [
        (end * 10, "The rod starts at the {0} cm mark, not at 0: subtract.".format(start)),
        ((end + start) * 10, "Subtract the start reading; do not add."),
        (L, "The question asks for millimetres: 1 cm = 10 mm."),
    ], unit="mm", sf=3)
    return dict(
        stem=f"The end of a ruler is damaged, so a student places one end of a metal rod at the **{start:g} cm** mark.\n\n{md_table(['reading at the other end of the rod / cm'], [[end]])}\n\nWhat is the length of the rod, in mm?",
        options=opts, key=key, misconceptions=mis,
        formula="length = end reading − start reading;  1 cm = 10 mm",
        working=[f"length = {end} − {start:g} = {L:g} cm", f"= **{L * 10:g} mm**", SRC],
        hints=["Subtract the starting mark.", f"{end} − {start:g} = {L:g} cm.", "Change to mm."],
    )


# ---------------------------------------------------------------- L2
@template("c04w_stopwatch_vs_record", chapter=4, level=2, lo="1.4b")
def stopwatch_vs_record(rng):
    record = 9.58
    t = nice(rng, 14.25, 16.80, 18.39, 20.07)
    diff = round(t - record, 2)
    opts, key, mis = numeric_options(rng, diff, [
        (t + record, "Subtract, do not add."),
        (t, "That is the student's time, not the difference."),
        (round(diff + 0.4, 2), "Check the subtraction of the hundredths."),
    ], unit="s", sf=4, dp=2)
    return dict(
        stem=f"Fig. 1 shows a teacher's stopwatch after a student runs 100 m. The world record for 100 m is **{record} s**. How much slower than the record was the student?",
        figure=figs.stopwatch(_sw(t)),
        options=opts, key=key, misconceptions=mis,
        formula="difference = student's time − record time",
        working=[f"stopwatch reads {t:.2f} s", f"{t:.2f} − {record} = **{diff:.2f} s**", SRC],
        hints=["Read the stopwatch in seconds.", "Subtract the record.", f"{t:.2f} − {record}."],
    )


@template("c04w_pile_of_blocks", chapter=4, level=2, lo="1.4a")
def pile_of_blocks(rng):
    n = nice(rng, 3, 4, 5)
    one = nice(rng, 3, 4, 5)
    H = n * one
    opts, key, mis = numeric_options(rng, one, [
        (H, "That is the height of the whole pile; divide by the number of blocks."),
        (H * n, "Divide, do not multiply."),
        (H / (n - 1), f"There are {n} blocks in the pile."),
    ], unit="cm", sf=3)
    return dict(
        stem=f"A ruler measures the height of a pile of identical blocks.\n\n{md_table(['blocks in the pile', 'height of pile / cm'], [[n, H]])}\n\nWhat is the height of one block?",
        options=opts, key=key, misconceptions=mis,
        formula="height of one block = height of pile ÷ number of blocks",
        working=[f"{H} ÷ {n}", f"= **{one} cm**", SRC],
        hints=["Share the pile's height between the blocks.", f"{H} ÷ {n}.", "Each block is the same."],
    )


@template("c04w_speed_track_laps_ms", chapter=4, level=2, lo="1.4e")
def speed_track_laps_ms(rng):
    km = nice(rng, 2.4, 3.0, 4.8)
    m = nice(rng, 12, 15, 20)
    v = km * 1000 / (m * 60)
    opts, key, mis = numeric_options(rng, v, [
        (km / m, "Change km to m and minutes to seconds."),
        (km * 1000 / m, "Change the minutes to seconds."),
        (km / (m * 60), "Change the km to metres."),
    ], unit="m/s", sf=3)
    return dict(
        stem=f"Rayyan completes a run.\n\n{md_table(['distance', 'time'], [[f'{km} km', f'{m} min']])}\n\nCalculate his speed in m/s.",
        options=opts, key=key, misconceptions=mis,
        formula="speed = distance (m) ÷ time (s);  1 km = 1000 m;  1 min = 60 s",
        working=[f"{km} km = {km * 1000:g} m;  {m} min = {m * 60} s", f"speed = {km * 1000:g} ÷ {m * 60} = **{fmt(v)} m/s**", SRC],
        hints=["Convert both units first.", f"{km * 1000:g} m and {m * 60} s.", "Divide."],
    )


@template("c04w_tug_of_war", chapter=4, level=2, lo="1.4c")
def tug_of_war(rng):
    np_, fp = nice(rng, 3, 4), nice(rng, 150, 200)
    nt, ft = nice(rng, 2, 3), nice(rng, 200, 300)
    L, R = np_ * fp, nt * ft
    if L == R:
        ans = "a draw, because the total forces are equal"
    elif L > R:
        ans = f"the pupils win by {L - R} N"
    else:
        ans = f"the teachers win by {R - L} N"
    cands = [("the pupils win because there are more of them", "Compare the TOTAL force on each side, not the number of people."),
             (f"the teachers win by {ft - fp} N", "Compare the totals, not one teacher against one pupil."),
             (f"the pupils win by {abs(L - R) or 100} N", "Work out each side's total: pupils × force each, teachers × force each, then compare."),
             (f"the teachers win by {abs(L - R) or 100} N", "Work out each side's total: pupils × force each, teachers × force each, then compare."),
             ("a draw, because the total forces are equal", "Work out each side's total: pupils × force each, teachers × force each, then compare."),
             (f"the teachers win by {R + L} N", "Subtract the totals; do not add them.")]
    wrongs = {}
    for text, why in cands:
        if text != ans and text not in wrongs and len(wrongs) < 3:
            wrongs[text] = why
    opts, key, mis = text_options(rng, ans, wrongs)
    return dict(
        stem=f"Pupils and teachers have a tug-of-war.\n\n{md_table(['side', 'number', 'force each / N', 'total force / N'], [['pupils', np_, fp, L], ['teachers', nt, ft, R]])}\n\nWhat happens?",
        options=opts, key=key, misconceptions=mis,
        formula="total force on each side = number × force each;  net force = difference",
        working=[f"pupils {L} N, teachers {R} N", f"**{ans}**", SRC],
        hints=["Find each side's total force.", "Compare the totals.", "Equal totals mean a draw."],
    )


# ---------------------------------------------------------------- L3
@template("c04w_ball_ruler_positions", chapter=4, level=3, lo="1.4e")
def ball_ruler_positions(rng):
    x1 = nice(rng, 1.0, 1.5, 2.0)
    dx = nice(rng, 2.0, 2.5, 3.0)
    t1 = nice(rng, 1.0, 2.0)
    dt = nice(rng, 0.5, 1.0)
    v = dx / dt
    opts, key, mis = numeric_options(rng, v, [
        ((x1 + dx) / (t1 + dt), "Use the CHANGE in position and the CHANGE in time, not the final readings."),
        (dx * dt, "Speed = distance ÷ time; do not multiply."),
        (dx / (t1 + dt), "The time taken is the difference between the two times."),
    ], unit="cm/s", sf=3)
    return dict(
        stem=f"A student photographs a ball against a ruler at two times.\n\n{md_table(['time / s', 'position on ruler / cm'], [[t1, x1], [t1 + dt, x1 + dx]])}\n\nWhat is the average speed of the ball between the two photographs?",
        options=opts, key=key, misconceptions=mis,
        formula="speed = distance moved ÷ time taken",
        working=[f"distance = {x1 + dx:g} − {x1:g} = {dx:g} cm;  time = {t1 + dt:g} − {t1:g} = {dt:g} s", f"speed = {dx:g} ÷ {dt:g} = **{fmt(v)} cm/s**", SRC],
        hints=["Distance moved = difference in positions.", "Time taken = difference in times.", f"{dx:g} ÷ {dt:g}."],
    )


@template("c04w_track_laps_kmh", chapter=4, level=3, lo="1.4e")
def track_laps_kmh(rng):
    L = nice(rng, 3, 4, 5)
    laps = nice(rng, 20, 25, 30)
    m = nice(rng, 30, 45, 60)
    v = L * laps / (m / 60)
    opts, key, mis = numeric_options(rng, v, [
        (L * laps / m, "Change the minutes to hours before dividing."),
        (L * laps, "That is the total distance; divide by the time in hours."),
        (L / (m / 60), "Use the TOTAL distance: track length × laps."),
    ], unit="km/h", sf=3)
    return dict(
        stem=f"A racing car goes round a track.\n\n{md_table(['length of track / km', 'laps completed', 'time'], [[L, laps, f'{m} min']])}\n\nWhat is the average speed in km/h?",
        options=opts, key=key, misconceptions=mis,
        formula="average speed = total distance ÷ total time (h);  1 h = 60 min",
        working=[f"total distance = {L} × {laps} = {L * laps} km;  time = {m}/60 = {m / 60:g} h", f"speed = {L * laps} ÷ {m / 60:g} = **{fmt(v)} km/h**", SRC],
        hints=["Total distance = laps × track length.", f"{m} min = {m / 60:g} h.", "Divide."],
    )


@template("c04w_round_trip_average", chapter=4, level=3, lo="1.4e")
def round_trip_average(rng):
    d = nice(rng, 100, 150, 200)
    t1 = nice(rng, 25, 30, 40)
    pause = nice(rng, 10, 15, 20)
    t2 = nice(rng, 50, 60, 80)
    v = 2 * d / (t1 + pause + t2)
    opts, key, mis = numeric_options(rng, v, [
        (d / (t1 + pause + t2), "The trip is there AND back: total distance is 2 × {0} m.".format(d)),
        (2 * d / (t1 + t2), "The pause counts in the total time."),
        (d / t1, "That is the speed on the way there only."),
    ], unit="m/s", sf=3)
    return dict(
        stem=f"Aliff walks from the classroom to a water cooler **{d} m** away, drinks, and walks back.\n\n{md_table(['stage', 'time / s'], [['walk there', t1], ['drink', pause], ['walk back', t2]])}\n\nCalculate his average speed for the whole trip.",
        options=opts, key=key, misconceptions=mis,
        formula="average speed = total distance ÷ total time (including stops)",
        working=[f"total distance = 2 × {d} = {2 * d} m;  total time = {t1} + {pause} + {t2} = {t1 + pause + t2} s", f"speed = {2 * d} ÷ {t1 + pause + t2} = **{fmt(v)} m/s**", SRC],
        hints=["There and back: double the distance.", "Add ALL the times, including the drink.", f"{2 * d} ÷ {t1 + pause + t2}."],
    )


@template("c04w_acceleration_kmh_per_h", chapter=4, level=3, lo="1.4f")
def acceleration_kmh_per_h(rng):
    u = nice(rng, 30, 40, 50)
    v = u + nice(rng, 30, 40, 50)
    a = nice(rng, 5, 10)
    t = (v - u) / a
    opts, key, mis = numeric_options(rng, t, [
        (v / a, "Use the CHANGE in speed (final − starting)."),
        ((v - u) * a, "Time = change in speed ÷ acceleration; do not multiply."),
        ((v + u) / a, "Subtract the speeds; do not add."),
    ], unit="h", sf=3)
    return dict(
        stem=f"A car's speed changes as shown. Its acceleration is **{a} km/h per hour**.\n\n{md_table(['starting speed / km/h', 'final speed / km/h'], [[u, v]])}\n\nHow long does the car take to speed up?",
        options=opts, key=key, misconceptions=mis,
        formula="time = change in speed ÷ acceleration",
        working=[f"change in speed = {v} − {u} = {v - u} km/h", f"t = {v - u} ÷ {a} = **{fmt(t)} h**", SRC],
        hints=["Find the change in speed.", "Rearrange acceleration = change in speed ÷ time.", f"{v - u} ÷ {a}."],
    )


# ---------------------------------------------------------------- L4
@template("c04w_mschee_journey_kmh", chapter=4, level=4, lo="1.4e")
def mschee_journey_kmh(rng):
    d1, m1 = nice(rng, 5, 6), nice(rng, 10, 12)
    stop = nice(rng, 0.5, 1)
    d2, m2 = nice(rng, 10, 12), nice(rng, 20, 24)
    T = m1 / 60 + stop + m2 / 60
    v = (d1 + d2) / T
    opts, key, mis = numeric_options(rng, v, [
        ((d1 + d2) / (m1 / 60 + m2 / 60), "The time at the supermarket counts in the total time."),
        ((d1 / (m1 / 60) + d2 / (m2 / 60)) / 2, "Do not average the stage speeds; use total distance ÷ total time."),
        ((d1 + d2) / (m1 + stop + m2), "Change the minutes to hours before adding."),
    ], unit="km/h", sf=3)
    return dict(
        stem=f"Ms Chee's trip is shown.\n\n{md_table(['stage', 'distance / km', 'time'], [['school to supermarket', d1, f'{m1} min'], ['at the supermarket', 0, f'{stop:g} h'], ['supermarket to home', d2, f'{m2} min']])}\n\nCalculate her average speed for the whole journey in km/h.",
        options=opts, key=key, misconceptions=mis,
        formula="average speed = total distance ÷ total time (h)",
        working=[f"total distance = {d1} + {d2} = {d1 + d2} km", f"total time = {m1 / 60:g} + {stop:g} + {m2 / 60:g} = {T:g} h", f"speed = {d1 + d2} ÷ {T:g} = **{fmt(v)} km/h**", SRC],
        hints=["Add the distances.", "Add ALL the times in hours, including the stop.", f"{d1 + d2} ÷ {T:g}."],
    )


@template("c04w_ironman_average", chapter=4, level=4, lo="1.4e")
def ironman_average(rng):
    rows = [["run", nice(rng, 8, 10), 30], ["swim", nice(rng, 12, 15), 45], ["cycle", nice(rng, 20, 25), 45]]
    D = sum(r[1] for r in rows)
    T = sum(r[2] for r in rows) / 60
    v = D / T
    which = pick(rng, rows)
    vs = which[1] / (which[2] / 60)
    opts, key, mis = text_options(rng, f"{which[0]} speed {fmt(vs)} km/h; whole journey {fmt(v)} km/h", {
        f"{which[0]} speed {fmt(which[1] / which[2])} km/h; whole journey {fmt(D / (T * 60))} km/h": "Change the minutes to hours.",
        f"{which[0]} speed {fmt(vs)} km/h; whole journey {fmt(sum(r[1] / (r[2] / 60) for r in rows) / 3)} km/h": "Do not average the three speeds; use total distance ÷ total time.",
        f"{which[0]} speed {fmt(vs)} km/h; whole journey {fmt(D)} km/h": "The whole-journey speed is the total distance divided by the total time.",
    })
    return dict(
        stem=f"Danish trains for a triathlon.\n\n{md_table(['stage', 'distance / km', 'time / min'], rows)}\n\nWhat is his **{which[0]}** speed, and his average speed for the whole session?",
        options=opts, key=key, misconceptions=mis,
        formula="speed = distance ÷ time (h);  average speed = total distance ÷ total time",
        working=[f"{which[0]}: {which[1]} ÷ {which[2] / 60:g} = {fmt(vs)} km/h", f"whole: {D} ÷ {T:g} = {fmt(v)} km/h", SRC],
        hints=["Change each time to hours.", f"{which[0]}: {which[1]} ÷ {which[2] / 60:g}.", f"Whole: {D} ÷ {T:g}."],
    )


@template("c04w_graph_sections_rest", chapter=4, level=4, lo="1.4g")
def graph_sections_rest(rng):
    v1 = nice(rng, 2, 3)
    segs = [(0, 0), (10, 10 * v1), (20, 10 * v1), (30, 10 * v1 + 10 * v1 / 2), (40, 10 * v1 + 10 * v1 / 2)]
    ans = "at rest during PQ and RS; fastest during OP"
    opts, key, mis = text_options(rng, ans, {
        "at rest during OP and QR; fastest during PQ": "Flat sections (no distance change) are the rest periods: PQ and RS.",
        "at rest during PQ and RS; fastest during QR": "OP is steeper than QR, so OP is faster.",
        "never at rest; fastest during RS": "RS is flat: the object is stationary there."},
    )
    return dict(
        stem="Fig. 1 is a distance-time graph. When is the object at rest, and when is it fastest?",
        figure=G1.dt_graph(segs, xmax=40, ymax=segs[-1][1] * 1.2, xstep=10, ystep=10),
        options=opts, key=key, misconceptions=mis,
        formula="flat = at rest; steeper = faster",
        working=["PQ and RS are flat → at rest", "OP is the steepest → fastest", SRC],
        hints=["Flat lines mean no distance covered.", "Compare the steepness of OP and QR.", "Steepest is fastest."],
    )


# ---------------------------------------------------------------- L5
@template("c04w_stopping_distance_average", chapter=4, level=5, lo="1.4g")
def stopping_distance_average(rng):
    rows = [[20, 12, 14], [30, nice(rng, 24, 26), nice(rng, 28, 30)], [40, 40, 44], [50, 60, 66], [70, nice(rng, 110, 114), nice(rng, 118, 122)]]
    avg30 = (rows[1][1] + rows[1][2]) / 2
    avg70 = (rows[4][1] + rows[4][2]) / 2
    opts, key, mis = text_options(rng, f"30 m/s: {fmt(avg30)} m; 70 m/s: {fmt(avg70)} m; stopping distance rises faster and faster with speed", {
        f"30 m/s: {fmt(rows[1][1] + rows[1][2])} m; 70 m/s: {fmt(rows[4][1] + rows[4][2])} m; stopping distance rises faster and faster with speed": "Average the two days: add and divide by 2.",
        f"30 m/s: {fmt(avg30)} m; 70 m/s: {fmt(avg70)} m; stopping distance rises by the same amount for each 10 m/s": "The increases get bigger: 13 → 42 → 54 m.",
        f"30 m/s: {fmt(avg30)} m; 70 m/s: {fmt(avg70)} m; stopping distance does not depend on speed": "It rises from 13 m to over 110 m.",
    })
    return dict(
        stem=f"A student measures a car's stopping distance at different speeds on two days.\n\n{md_table(['speed / m/s', 'day 1 stopping distance / m', 'day 2 stopping distance / m'], rows)}\n\nWhat are the average stopping distances at 30 m/s and 70 m/s, and what trend do the data show?",
        options=opts, key=key, misconceptions=mis,
        formula="average = (day 1 + day 2) ÷ 2;  look at how the increases change",
        working=[f"30 m/s: ({rows[1][1]} + {rows[1][2]}) ÷ 2 = {fmt(avg30)} m", f"70 m/s: ({rows[4][1]} + {rows[4][2]}) ÷ 2 = {fmt(avg70)} m", "the stopping distance grows faster and faster as the speed rises (a curve, not a straight line)", SRC],
        hints=["Average the two days for each speed.", "Compare how much the distance rises for each 10 m/s.", "The rises get bigger."],
    )


@template("c04w_stopping_experiment_fair", chapter=4, level=5, lo="1.4b")
def stopping_experiment_fair(rng):
    d1 = [nice(rng, 11, 12, 13), nice(rng, 38, 40, 42), nice(rng, 110, 112, 115)]
    d2 = [d1[0] + nice(rng, 2, 3), d1[1] + nice(rng, 4, 6), d1[2] + nice(rng, 8, 10)]
    ans = "use the same driver and car, and repeat each speed several times and average, because the driver's reaction time changes the stopping distance"
    opts, key, mis = text_options(rng, ans, {
        "use a different car each day so the results are more varied": "Changing the car is NOT a fair test.",
        "measure only once at each speed to save time": "Repeats and averages reduce the effect of reaction time.",
        "test only at 70 m/s, where the distances are largest": "A trend needs several speeds."},
    )
    return dict(
        stem=f"A stopping-distance investigation was done over two days with a different driver each day.\n\n{md_table(['speed / m/s', 'day 1 / m', 'day 2 / m'], [[20, d1[0], d2[0]], [40, d1[1], d2[1]], [70, d1[2], d2[2]]])}\n\nThe day 2 distances are always longer. What is the best improvement to the method?",
        options=opts, key=key, misconceptions=mis,
        formula="fair test: change only the speed; repeat and average to reduce the effect of reaction time",
        working=["the driver changed between the days, so reaction time (and the car) may differ", f"**{ans}**", SRC],
        hints=["What changed between the days apart from the speed?", "The driver.", "Keep it the same and repeat."],
    )


# ================================================================ EXPLANATION (worksheet items)
EXPLAIN = [
    dict(id="e04w_force_cannot_change_mass", level=1, lo="1.4c",
         stem=f"A soccer ball hits the goal post and rebounds. The table shows what a force can change.\n\n{md_table(['property'], [['shape'], ['motion'], ['direction'], ['mass']])}\n\nWhat happens to the ball's shape and mass when it hits the post?",
         correct="the shape is altered for an instant and the mass is unchanged",
         wrongs={"the shape is altered and the mass decreases": "A force cannot change the mass of an object.", "the shape is constant and the mass decreases": "The ball squashes briefly, and mass never changes.", "the shape and the mass are both constant": "The ball is squashed for a moment by the post."},
         hints=["Which property in the table can a force NOT change?", "Mass.", "The ball squashes briefly."],
         working=["Correct answer: **the shape is altered for an instant and the mass is unchanged**", SRC]),
    dict(id="e04w_push_pull_examples", level=1, lo="1.4c",
         stem=f"The table lists actions.\n\n{md_table(['action'], [['kicking a ball'], ['raising a flag with a rope'], ['doing push-ups'], ['lifting a bag']])}\n\nWhich actions use a PULLING force?",
         correct="raising a flag with a rope and lifting a bag",
         wrongs={"kicking a ball and doing push-ups": "Both are pushes.", "kicking a ball and lifting a bag": "Kicking is a push.", "all four": "Kicking and push-ups are pushes."},
         hints=["A pull brings the object towards you.", "A rope and a bag handle are pulled.", "Kicking and pushing up are pushes."],
         working=["Correct answer: **raising a flag with a rope and lifting a bag**", SRC]),
    dict(id="e04w_stopwatch_minutes_trap", level=5, lo="1.4b",
         stem="Fig. 1 shows a digital stopwatch at the end of a race. A student writes '1.58 seconds'. Explain the mistake and give the correct time.",
         fig=lambda rng: figs.stopwatch("1:58.00"),
         correct="the display shows 1 minute 58 seconds, which is 118 s; the student read the minutes as seconds",
         wrongs={"the display shows 158 seconds": "The first digit is MINUTES: 1 min = 60 s, so 60 + 58 = 118 s.", "the student is correct": "1.58 s would be far too short for a race; the display reads 1:58.", "the display shows 1.58 minutes": "1:58 means 1 minute and 58 seconds, not 1.58 minutes."},
         hints=["What does the number before the colon mean?", "Minutes.", "Convert: 1 × 60 + 58."],
         keypoints=[KP("minutes before the colon", "minute", "colon", "1 min", "60"), KP("118 s", "118")],
         working=["Correct answer: **the display shows 1 minute 58 seconds, which is 118 s; the student read the minutes as seconds**", SRC]),
]

register_explain(EXPLAIN, chapter=4)
