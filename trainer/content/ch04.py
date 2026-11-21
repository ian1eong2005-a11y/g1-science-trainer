"""Ch 4 Effects of Force (K123 topic 1.4): 20 calculation / data templates and 40 explanation items.
lo codes: 1.4a ruler and measuring tape, 1.4b digital stopwatch, 1.4c effects of force (shape, motion, turning), 1.4d speed and
acceleration, 1.4e average speed = distance / time, 1.4f acceleration = change in speed / time, 1.4g distance-time graphs,
1.4h moment of a force (turning effect, no equations)."""
from .. import figs, sketches as S, sketches_g1 as G1
from .base import fmt, md_table, nice, numeric_options, pick, register_explain, template, text_options

KP = lambda label, *phr: {"label": label, "any": list(phr)}


def _sw(t):
    """stopwatch text m:ss.hh from seconds"""
    m = int(t // 60)
    s = t - 60 * m
    return f"{m}:{s:05.2f}"


# ================================================================ CALCULATION / DATA
# ---------------------------------------------------------------- L1
@template("c04_average_speed", chapter=4, level=1, lo="1.4e")
def average_speed(rng):
    d = nice(rng, 100, 200, 400, 1500)
    t = nice(rng, 10, 20, 25, 50)
    v = d / t
    opts, key, mis = numeric_options(rng, v, [
        (d * t, "You multiplied. Speed = distance ÷ time."),
        (t / d, "Upside down: distance ÷ time."),
        (d - t, "You subtracted. Divide the distance by the time."),
    ], unit="m/s", sf=3)
    return dict(
        stem=f"A runner's race is timed.\n\n{md_table(['distance / m', 'time / s'], [[d, t]])}\n\nWhat is the runner's average speed?",
        options=opts, key=key, misconceptions=mis,
        formula="average speed = total distance ÷ total time taken",
        working=[f"speed = {d} ÷ {t}", f"= **{fmt(v)} m/s**"],
        hints=["Speed is distance covered each second.", "Divide distance by time.", f"{d} ÷ {t}."],
    )


@template("c04_read_stopwatch", chapter=4, level=1, lo="1.4b")
def read_stopwatch(rng):
    t = nice(rng, 12.34, 45.60, 73.25, 95.08, 125.50)
    opts, key, mis = numeric_options(rng, t, [
        (t + 60 if t < 60 else t - 60, "Check the minutes: the first number before the colon is minutes, not seconds." if t >= 60 else "The display shows 0 minutes; do not add a minute."),
        (round(t * 100) / 10, "The last two digits are hundredths of a second."),
        (t + 0.5, "Read the digits again carefully."),
    ], unit="s", sf=4, dp=2)
    return dict(
        stem="Fig. 1 shows a digital stopwatch at the end of a race. What time does it show, in seconds?",
        figure=figs.stopwatch(_sw(t)),
        options=opts, key=key, misconceptions=mis,
        formula="minutes : seconds . hundredths;  1 min = 60 s",
        working=[f"display {_sw(t)} = {int(t // 60)} min {t - 60 * int(t // 60):.2f} s", f"= **{t:.2f} s**"],
        hints=["The digits before the colon are minutes.", "The digits after the point are hundredths of a second.", "Convert minutes to seconds and add."],
    )


@template("c04_acceleration_simple", chapter=4, level=1, lo="1.4f")
def acceleration_simple(rng):
    v = nice(rng, 10, 12, 15, 20, 30)
    t = nice(rng, 2, 4, 5, 10)
    a = v / t
    opts, key, mis = numeric_options(rng, a, [
        (v * t, "You multiplied. Acceleration = change in speed ÷ time."),
        (t / v, "Upside down: change in speed ÷ time."),
        (v, "That is the final speed. Divide the change in speed by the time."),
    ], unit="m/s²", sf=3)
    return dict(
        stem=f"A car starts from rest.\n\n{md_table(['starting speed / m/s', 'final speed / m/s', 'time taken / s'], [[0, v, t]])}\n\nWhat is the car's acceleration?",
        options=opts, key=key, misconceptions=mis,
        formula="acceleration = change in speed ÷ time taken",
        working=[f"change in speed = {v} − 0 = {v} m/s", f"acceleration = {v} ÷ {t} = **{fmt(a)} m/s²**"],
        hints=["Find the change in speed first.", "Then divide by the time.", f"{v} ÷ {t}."],
    )


@template("c04_tape_length", chapter=4, level=1, lo="1.4a")
def tape_length(rng):
    start = nice(rng, 0, 10, 20, 35)
    L = nice(rng, 120, 150, 185, 240)
    end = start + L
    opts, key, mis = numeric_options(rng, L, [
        (end, "Subtract the reading at the start of the object; it did not begin at 0."),
        (end + start, "Subtract, do not add."),
        (L / 100 if L >= 100 else L * 100, "Check the units: the readings are in cm."),
    ], unit="cm", sf=4)
    return dict(
        stem=f"A measuring tape is laid along a table. The table shows the tape readings at the two ends.\n\n{md_table(['end of table', 'tape reading / cm'], [['left', start], ['right', end]])}\n\nWhat is the length of the table?",
        options=opts, key=key, misconceptions=mis,
        formula="length = reading at one end − reading at the other end",
        working=[f"length = {end} − {start}", f"= **{L} cm**"],
        hints=["The tape does not start at zero.", "Subtract the two readings.", f"{end} − {start}."],
    )


# ---------------------------------------------------------------- L2
@template("c04_time_from_speed", chapter=4, level=2, lo="1.4e")
def time_from_speed(rng):
    v = nice(rng, 4, 5, 8, 10)
    d = nice(rng, 200, 400, 800, 1000)
    t = d / v
    opts, key, mis = numeric_options(rng, t, [
        (d * v, "You multiplied. Time = distance ÷ speed."),
        (v / d, "Upside down: distance ÷ speed."),
        (d, "That is the distance; divide it by the speed."),
    ], unit="s", sf=3)
    return dict(
        stem=f"A cyclist rides at a steady speed.\n\n{md_table(['speed / m/s', 'distance / m'], [[v, d]])}\n\nHow long does the ride take?",
        options=opts, key=key, misconceptions=mis,
        formula="time = distance ÷ speed",
        working=[f"time = {d} ÷ {v}", f"= **{fmt(t)} s**"],
        hints=["Rearrange speed = distance ÷ time.", "time = distance ÷ speed.", f"{d} ÷ {v}."],
    )


@template("c04_speed_km_min", chapter=4, level=2, lo="1.4e")
def speed_km_min(rng):
    km = nice(rng, 3, 6, 9, 12)
    m = nice(rng, 10, 15, 20, 30)
    v = km * 1000 / (m * 60)
    opts, key, mis = numeric_options(rng, v, [
        (km / m, "Change km to m and minutes to seconds first."),
        (km * 1000 / m, "The time must be in seconds: multiply the minutes by 60."),
        (km / (m * 60), "The distance must be in metres: multiply the km by 1000."),
    ], unit="m/s", sf=3)
    return dict(
        stem=f"A bus journey is recorded.\n\n{md_table(['distance', 'time'], [[f'{km} km', f'{m} min']])}\n\nWhat is the average speed in m/s?",
        options=opts, key=key, misconceptions=mis,
        formula="average speed = distance (m) ÷ time (s);  1 km = 1000 m;  1 min = 60 s",
        working=[f"{km} km = {km * 1000} m;  {m} min = {m * 60} s", f"speed = {km * 1000} ÷ {m * 60} = **{fmt(v)} m/s**"],
        hints=["Convert both units first.", f"{km * 1000} m and {m * 60} s.", f"{km * 1000} ÷ {m * 60}."],
    )


@template("c04_acceleration_two_speeds", chapter=4, level=2, lo="1.4f")
def acceleration_two_speeds(rng):
    u = nice(rng, 4, 5, 6, 10)
    v = u + nice(rng, 6, 8, 10, 15)
    t = nice(rng, 2, 4, 5)
    a = (v - u) / t
    opts, key, mis = numeric_options(rng, a, [
        (v / t, "Use the CHANGE in speed (final − starting), not the final speed."),
        ((v + u) / t, "Subtract the speeds; do not add."),
        ((v - u) * t, "Divide by the time; do not multiply."),
    ], unit="m/s²", sf=3)
    return dict(
        stem=f"A motorcycle speeds up.\n\n{md_table(['starting speed / m/s', 'final speed / m/s', 'time taken / s'], [[u, v, t]])}\n\nWhat is its acceleration?",
        options=opts, key=key, misconceptions=mis,
        formula="acceleration = (final speed − starting speed) ÷ time taken",
        working=[f"change in speed = {v} − {u} = {v - u} m/s", f"acceleration = {v - u} ÷ {t} = **{fmt(a)} m/s²**"],
        hints=["Change in speed = final − starting.", f"{v} − {u} = {v - u}.", f"{v - u} ÷ {t}."],
    )


@template("c04_distance_from_graph_point", chapter=4, level=2, lo="1.4g")
def distance_from_graph_point(rng):
    v = nice(rng, 2, 4, 5)
    tmax = nice(rng, 10, 20)
    t1 = nice(rng, 4, 6, 8)
    d = v * t1
    opts, key, mis = numeric_options(rng, d, [
        (v * tmax, "Read the distance at the time asked, not at the end of the graph."),
        (t1, "That is the time; read UP from it to the line and across to the distance axis."),
        (d / 2, "Read the distance axis again at that time."),
    ], unit="m", sf=3)
    return dict(
        stem=f"Fig. 1 is the distance-time graph of a walker. How far had the walker gone after **{t1} s**?",
        figure=G1.dt_graph([(0, 0), (tmax, v * tmax)], xmax=tmax, ymax=v * tmax * 1.1, xstep=tmax // 5, ystep=v * tmax // 5, labels=False),
        options=opts, key=key, misconceptions=mis,
        formula="read the distance axis at the given time",
        working=[f"at t = {t1} s the line is at {d} m", f"distance = **{d} m**"],
        hints=[f"Find {t1} s on the time axis.", "Go up to the line, then across to the distance axis.", f"The line rises {v} m every second."],
    )


# ---------------------------------------------------------------- L3
@template("c04_speed_from_gradient", chapter=4, level=3, lo="1.4g")
def speed_from_gradient(rng):
    v = nice(rng, 1.5, 2, 3, 5)
    tmax = nice(rng, 10, 20)
    opts, key, mis = numeric_options(rng, v, [
        (v * tmax, "That is the total distance, not the speed. Divide by the time."),
        (tmax / (v * tmax), "Upside down: distance ÷ time."),
        (v * 2, "Check: distance ÷ time at any point on the line."),
    ], unit="m/s", sf=3)
    return dict(
        stem="Fig. 1 is a distance-time graph. What is the speed of the object?",
        figure=G1.dt_graph([(0, 0), (tmax, v * tmax)], xmax=tmax, ymax=v * tmax * 1.1, xstep=tmax // 5, ystep=v * tmax / 5, labels=False),
        options=opts, key=key, misconceptions=mis,
        formula="speed = distance ÷ time = gradient of a distance-time graph",
        working=[f"at t = {tmax} s the distance is {v * tmax:g} m", f"speed = {v * tmax:g} ÷ {tmax} = **{fmt(v)} m/s**"],
        hints=["Pick a point on the line and read its distance and time.", "Divide distance by time.", f"At {tmax} s the distance is {v * tmax:g} m."],
    )


@template("c04_stopwatch_difference", chapter=4, level=3, lo="1.4b")
def stopwatch_difference(rng):
    t1 = nice(rng, 5.20, 12.45, 30.10)
    dt = nice(rng, 8.30, 15.75, 42.50)
    t2 = t1 + dt
    opts, key, mis = numeric_options(rng, dt, [
        (t2, "The stopwatch was not reset: subtract the first reading."),
        (t2 + t1, "Subtract the readings; do not add."),
        (dt + 1, "Check the subtraction, including the hundredths."),
    ], unit="s", sf=4, dp=2)
    return dict(
        stem=f"A stopwatch is left running. The table shows its readings when a toy car passes two marks.\n\n{md_table(['mark', 'stopwatch reading'], [['first', _sw(t1)], ['second', _sw(t2)]])}\n\nHow long did the car take between the marks?",
        options=opts, key=key, misconceptions=mis,
        formula="time interval = second reading − first reading",
        working=[f"{_sw(t2)} = {t2:.2f} s;  {_sw(t1)} = {t1:.2f} s", f"interval = {t2:.2f} − {t1:.2f} = **{dt:.2f} s**"],
        hints=["Change each reading to seconds.", "Subtract the first from the second.", f"{t2:.2f} − {t1:.2f}."],
    )


@template("c04_average_two_parts", chapter=4, level=3, lo="1.4e")
def average_two_parts(rng):
    d1, t1 = nice(rng, 300, 600), nice(rng, 60, 100)
    d2, t2 = nice(rng, 200, 400), nice(rng, 40, 50)
    v = (d1 + d2) / (t1 + t2)
    opts, key, mis = numeric_options(rng, v, [
        ((d1 / t1 + d2 / t2) / 2, "Do not average the two speeds; use TOTAL distance ÷ TOTAL time."),
        (d1 / t1, "That is the speed of the first part only."),
        ((d1 + d2) / t1, "Divide by the TOTAL time, both parts."),
    ], unit="m/s", sf=3)
    return dict(
        stem=f"A jogger's run has two parts.\n\n{md_table(['part', 'distance / m', 'time / s'], [['1', d1, t1], ['2', d2, t2]])}\n\nWhat is the average speed for the whole run?",
        options=opts, key=key, misconceptions=mis,
        formula="average speed = total distance ÷ total time",
        working=[f"total distance = {d1} + {d2} = {d1 + d2} m;  total time = {t1} + {t2} = {t1 + t2} s", f"average speed = {d1 + d2} ÷ {t1 + t2} = **{fmt(v)} m/s**"],
        hints=["Add the distances and add the times.", "Then divide.", f"{d1 + d2} ÷ {t1 + t2}."],
    )


@template("c04_deceleration", chapter=4, level=3, lo="1.4f")
def deceleration(rng):
    u = nice(rng, 20, 24, 30)
    v = nice(rng, 0, 6, 10)
    t = nice(rng, 4, 5, 7)
    a = (u - v) / t
    opts, key, mis = numeric_options(rng, a, [
        (u / t, "Use the CHANGE in speed: starting − final."),
        ((u + v) / t, "Subtract the speeds; do not add."),
        ((u - v) * t, "Divide by the time; do not multiply."),
    ], unit="m/s²", sf=3)
    return dict(
        stem=f"A car brakes.\n\n{md_table(['starting speed / m/s', 'final speed / m/s', 'time taken / s'], [[u, v, t]])}\n\nBy how much does the speed change each second (the size of the deceleration)?",
        options=opts, key=key, misconceptions=mis,
        formula="deceleration = (starting speed − final speed) ÷ time taken",
        working=[f"change in speed = {u} − {v} = {u - v} m/s", f"deceleration = {u - v} ÷ {t} = **{fmt(a)} m/s²**"],
        hints=["Find how much the speed fell.", f"{u} − {v} = {u - v}.", f"{u - v} ÷ {t}."],
    )


# ---------------------------------------------------------------- L4
@template("c04_graph_fastest_section", chapter=4, level=4, lo="1.4g")
def graph_fastest_section(rng):
    v1, v2, v3 = nice(rng, 1, 2), nice(rng, 4, 5), nice(rng, 0.5, 1)
    segs = [(0, 0), (10, 10 * v1), (20, 10 * v1 + 10 * v2), (30, 10 * v1 + 10 * v2 + 10 * v3)]
    opts, key, mis = text_options(rng, f"PQ, at {fmt(v2)} m/s", {
        f"OP, at {fmt(v1)} m/s": "OP is less steep than PQ, so the speed is lower there.",
        f"QR, at {fmt(v3)} m/s": "QR is the least steep section, so the slowest.",
        f"PQ, at {fmt(10 * v2)} m/s": f"PQ covers {10 * v2:g} m in 10 s, so the speed is {fmt(v2)} m/s.",
    })
    return dict(
        stem="Fig. 1 is the distance-time graph of a delivery rider. In which section is the rider fastest, and at what speed?",
        figure=G1.dt_graph(segs, xmax=30, ymax=segs[-1][1] * 1.15, xstep=5, ystep=10),
        options=opts, key=key, misconceptions=mis,
        formula="the steepest section of a distance-time graph is the fastest; speed = distance ÷ time for that section",
        working=["the steepest section is PQ", f"PQ: {10 * v2:g} m in 10 s → {fmt(v2)} m/s"],
        hints=["Which section is steepest?", "Steepest = fastest.", f"PQ rises {10 * v2:g} m in 10 s."],
    )


@template("c04_speed_table_acceleration", chapter=4, level=4, lo="1.4f")
def speed_table_acceleration(rng):
    a = nice(rng, 1.5, 2, 2.5, 3)
    rows = [[t, fmt(a * t)] for t in (0, 2, 4, 6)]
    opts, key, mis = numeric_options(rng, a, [
        (a * 6, "That is the speed at 6 s, not the acceleration. Divide the change in speed by the time."),
        (a * 2, "The speed changes by that amount every 2 s; per second it is half of that."),
        (a / 2, "Check: change in speed ÷ time."),
    ], unit="m/s²", sf=3)
    return dict(
        stem=f"The table shows the speed of a train leaving a station.\n\n{md_table(['time / s', 'speed / m/s'], rows)}\n\nWhat is the train's acceleration?",
        options=opts, key=key, misconceptions=mis,
        formula="acceleration = change in speed ÷ time taken",
        working=[f"from 0 to 6 s the speed rises from 0 to {fmt(a * 6)} m/s", f"acceleration = {fmt(a * 6)} ÷ 6 = **{fmt(a)} m/s²**"],
        hints=["How much does the speed change over the whole table?", "Divide by the time taken.", f"{fmt(a * 6)} ÷ 6."],
    )


@template("c04_journey_with_stop", chapter=4, level=4, lo="1.4g")
def journey_with_stop(rng):
    v1 = nice(rng, 2, 3, 4)
    stop = nice(rng, 5, 10)
    segs = [(0, 0), (10, 10 * v1), (10 + stop, 10 * v1), (30, 10 * v1 + (20 - stop) * v1 * 0.5)]
    opts, key, mis = text_options(rng, f"the walker stopped for {stop} s, then walked on more slowly", {
        f"the walker stopped for {stop} s, then walked on faster": "The last section is LESS steep than the first, so slower.",
        "the walker turned round and walked back": "The distance never decreases, so the walker did not come back.",
        "the walker walked at a steady speed throughout": "The flat part shows no distance covered: a stop."},
    )
    return dict(
        stem="Fig. 1 is the distance-time graph of a walker. Which description fits the graph?",
        figure=G1.dt_graph(segs, xmax=30, ymax=segs[-1][1] * 1.2, xstep=5, ystep=5),
        options=opts, key=key, misconceptions=mis,
        formula="flat section = stationary; steeper = faster",
        working=[f"OP: moving; PQ: flat for {stop} s, so stationary; QR: less steep than OP, so slower", f"**the walker stopped for {stop} s, then walked on more slowly**"],
        hints=["What does a flat section mean?", "Compare the slopes of the first and last sections.", "Less steep = slower."],
    )


@template("c04_compare_runners", chapter=4, level=4, lo="1.4e")
def compare_runners(rng):
    d1, t1 = nice(rng, 100, 200), nice(rng, 12.5, 25)
    d2, t2 = nice(rng, 400, 800), nice(rng, 60, 110)
    v1, v2 = d1 / t1, d2 / t2
    if abs(v1 - v2) < 0.2:
        t2 += 10; v2 = d2 / t2
    ans = "P" if v1 > v2 else "Q"
    hi, lo = max(v1, v2), min(v1, v2)
    opts, key, mis = text_options(rng, f"{ans}, at {fmt(hi)} m/s compared with {fmt(lo)} m/s", {
        f"{'Q' if ans == 'P' else 'P'}, at {fmt(lo)} m/s compared with {fmt(hi)} m/s": "Check the divisions: the faster runner has the larger distance ÷ time.",
        "Q, because Q ran further": "Running further in a much longer time does not mean faster; divide.",
        "P, because P took less time": "A shorter time over a shorter distance does not decide it; divide distance by time.",
    })
    return dict(
        stem=f"Two runners are timed over different distances.\n\n{md_table(['runner', 'distance / m', 'time / s'], [['P', d1, t1], ['Q', d2, t2]])}\n\nWho has the higher average speed?",
        options=opts, key=key, misconceptions=mis,
        formula="average speed = distance ÷ time",
        working=[f"P: {d1} ÷ {t1} = {fmt(v1)} m/s", f"Q: {d2} ÷ {t2} = {fmt(v2)} m/s", f"faster: **{ans}**"],
        hints=["Work out each speed.", f"P: {fmt(v1)} m/s.", f"Q: {fmt(v2)} m/s."],
    )


# ---------------------------------------------------------------- L5
@template("c04_trip_three_parts", chapter=4, level=5, lo="1.4e")
def trip_three_parts(rng):
    rows = [["walk to bus stop", nice(rng, 400, 600), nice(rng, 5, 8)], ["wait for bus", 0, nice(rng, 4, 6)], ["bus ride", nice(rng, 6000, 9000), nice(rng, 15, 20)]]
    D = sum(r[1] for r in rows)
    T = sum(r[2] for r in rows)
    v = D / (T * 60)
    opts, key, mis = numeric_options(rng, v, [
        (D / ((T - rows[1][2]) * 60), "The waiting time counts in the TOTAL time, even though no distance is covered."),
        (D / T, "Change the minutes to seconds."),
        (rows[2][1] / (rows[2][2] * 60), "That is the bus's speed only; use the whole journey."),
    ], unit="m/s", sf=3)
    return dict(
        stem=f"A student's journey to school is shown.\n\n{md_table(['stage', 'distance / m', 'time / min'], rows)}\n\nWhat is the average speed for the whole journey, in m/s?",
        options=opts, key=key, misconceptions=mis,
        formula="average speed = total distance ÷ total time (including stops), time in seconds",
        working=[f"total distance = {D} m;  total time = {T} min = {T * 60} s", f"average speed = {D} ÷ {T * 60} = **{fmt(v)} m/s**"],
        hints=["Add ALL the distances and ALL the times, including the wait.", f"{T} min = {T * 60} s.", f"{D} ÷ {T * 60}."],
    )


@template("c04_graph_stationary_question", chapter=4, level=5, lo="1.4g")
def graph_stationary_question(rng):
    v1 = nice(rng, 2, 3)
    stop = nice(rng, 6, 8)
    segs = [(0, 0), (8, 8 * v1), (8 + stop, 8 * v1), (24, 8 * v1 + (16 - stop) * v1)]
    total = segs[-1][1]
    v = total / 24
    opts, key, mis = numeric_options(rng, v, [
        (v1, f"That is the speed while moving; the AVERAGE over 24 s includes the {stop} s stop."),
        (total / (24 - stop), "The time stationary counts in the total time."),
        (total, "That is the total distance; divide by 24 s."),
    ], unit="m/s", sf=3)
    return dict(
        stem="Fig. 1 is the distance-time graph of a trolley. What is its average speed over the whole 24 s?",
        figure=G1.dt_graph(segs, xmax=24, ymax=total * 1.15, xstep=4, ystep=8),
        options=opts, key=key, misconceptions=mis,
        formula="average speed = total distance ÷ total time, including time spent stationary",
        working=[f"total distance at 24 s = {total:g} m", f"average speed = {total:g} ÷ 24 = **{fmt(v)} m/s**"],
        hints=["Read the final distance from the graph.", "Divide by the WHOLE time, 24 s.", f"{total:g} ÷ 24."],
    )


@template("c04_speed_vs_acceleration_trap", chapter=4, level=5, lo="1.4d")
def speed_vs_acceleration_trap(rng):
    v = nice(rng, 20, 25, 30)
    rows = [[t, v] for t in (0, 5, 10, 15)]
    opts, key, mis = text_options(rng, f"the speed is {v} m/s and the acceleration is 0", {
        f"the speed is {v} m/s and the acceleration is {v} m/s²": "The speed is NOT changing, so the acceleration is zero.",
        f"the acceleration is {v / 5:g} m/s² because the speed is {v} m/s every 5 s": "Acceleration is the CHANGE in speed per second; the change is 0.",
        "the car must be slowing down because the acceleration is 0": "Zero acceleration means a steady speed, not slowing."},
    )
    return dict(
        stem=f"The table shows a car on a highway.\n\n{md_table(['time / s', 'speed / m/s'], rows)}\n\nWhich statement is correct?",
        options=opts, key=key, misconceptions=mis,
        formula="acceleration = change in speed ÷ time; a steady speed means zero acceleration",
        working=["the speed is the same at every time, so the change in speed is 0", f"**speed {v} m/s, acceleration 0**"],
        hints=["Is the speed changing?", "What is acceleration a measure of?", "No change → zero acceleration."],
    )


@template("c04_spanner_data", chapter=4, level=5, lo="1.4h")
def spanner_data(rng):
    rows = [[10, nice(rng, 60, 80)], [20, None], [40, None]]
    f10 = rows[0][1]
    rows[1][1] = f10 // 2
    rows[2][1] = f10 // 4
    opts, key, mis = text_options(rng, "a longer spanner gives a larger turning effect for the same force, so less force is needed", {
        "a longer spanner is heavier, so it pushes harder by itself": "The spanner's weight is not what loosens the nut; the force applied further from the nut is.",
        "a shorter spanner gives a larger turning effect": "The table shows the SHORT spanner needs the MOST force.",
        "the force needed does not depend on the length": "The force halves each time the length doubles."},
    )
    return dict(
        stem=f"A mechanic measures the smallest force needed to loosen the same nut with spanners of different lengths.\n\n{md_table(['length of spanner / cm', 'force needed / N'], rows)}\n\nWhat do the results show about the turning effect of a force?",
        options=opts, key=key, misconceptions=mis,
        formula="the turning effect (moment) of a force is greater when the force acts further from the pivot",
        working=["doubling the length halves the force needed", "**a longer spanner gives a larger turning effect for the same force, so less force is needed**"],
        hints=["Read the force column as the length grows.", "Where is the force applied relative to the nut?", "Further from the pivot: bigger turning effect."],
    )


# ================================================================ EXPLANATION
T_EFFECTS = md_table(["effect of a force", "example"], [["change the shape or size of an object", "squeezing a sponge"], ["make a stationary object move", "kicking a ball"], ["speed up, slow down or stop a moving object", "braking a bicycle"], ["change the direction of a moving object", "hitting a tennis ball back"], ["turn an object about a pivot", "opening a door"]])

EXPLAIN = [
    # ------------------------------------------------------------ L1
    dict(id="e04_effect_shape", level=1, lo="1.4c",
         stem=f"The table lists effects of forces.\n\n{T_EFFECTS}\n\nA student stretches a spring. Which effect of a force is this?",
         correct="a change in the shape or size of the object",
         wrongs={"a change in the direction of a moving object": "The spring is not moving along; it is being stretched.", "a turning effect": "Nothing is turning about a pivot.", "making a stationary object move": "The spring stays where it is; its length changes."},
         hints=["What happens to the spring's length?", "That is a change in its ...?", "Shape or size."]),
    dict(id="e04_effect_stop", level=1, lo="1.4c",
         stem=f"The table lists effects of forces.\n\n{T_EFFECTS}\n\nA goalkeeper catches a fast-moving ball. Which effect of a force is this?",
         correct="a moving object is stopped (its state of motion changes)",
         wrongs={"the ball's shape is changed": "The main effect is that the ball stops moving.", "a turning effect": "The ball does not turn about a pivot.", "the ball is made to move": "It was already moving; the force STOPS it."},
         hints=["What was the ball doing before and after?", "Moving, then at rest.", "A change in motion."]),
    dict(id="e04_effect_turn", level=1, lo="1.4c",
         stem=f"The table lists effects of forces.\n\n{T_EFFECTS}\n\nA student pushes a door handle and the door swings open. Which effect of a force is this?",
         correct="a turning effect about a pivot (the hinges)",
         wrongs={"a change in shape of the door": "The door keeps its shape; it swings.", "a change in the speed of a moving object": "The door was at rest and turns.", "no effect, because the door is heavy": "The door moves, so the force had an effect."},
         hints=["What does the door turn about?", "The hinges are the pivot.", "A turning effect."]),
    dict(id="e04_speed_meaning", level=1, lo="1.4d",
         stem=f"The table lists quantities.\n\n{md_table(['quantity', 'meaning'], [['P', 'distance travelled each second'], ['Q', 'change in speed each second'], ['R', 'how far an object has moved']])}\n\nWhich quantity is speed?",
         correct="P",
         wrongs={"Q": "Q is acceleration.", "R": "R is distance.", "none of them": "P describes speed."},
         hints=["Speed is measured in m/s.", "Metres per second.", "Distance each second."]),
    dict(id="e04_acceleration_meaning", level=1, lo="1.4d",
         stem=f"The table lists quantities.\n\n{md_table(['quantity', 'meaning'], [['P', 'distance travelled each second'], ['Q', 'change in speed each second'], ['R', 'how far an object has moved']])}\n\nWhich quantity is acceleration?",
         correct="Q",
         wrongs={"P": "P is speed.", "R": "R is distance.", "none of them": "Q describes acceleration."},
         hints=["Acceleration is measured in m/s².", "Metres per second, per second.", "Change in speed each second."]),
    dict(id="e04_instrument_time", level=1, lo="1.4b",
         stem=f"The table lists instruments.\n\n{md_table(['instrument'], [['ruler'], ['measuring tape'], ['digital stopwatch'], ['measuring cylinder']])}\n\nWhich instrument is used to measure the time for a toy car to cross a room?",
         correct="digital stopwatch",
         wrongs={"ruler": "A ruler measures length.", "measuring tape": "A measuring tape measures length.", "measuring cylinder": "A measuring cylinder measures volume."},
         hints=["Time is measured in seconds.", "Which instrument shows seconds?", "Stopwatch."]),
    dict(id="e04_instrument_length", level=1, lo="1.4a",
         stem=f"The table lists instruments.\n\n{md_table(['instrument', 'range'], [['ruler', '30 cm'], ['measuring tape', '5 m'], ['digital stopwatch', '–'], ['measuring cylinder', '100 cm³']])}\n\nWhich instrument is best for measuring the length of a classroom?",
         correct="measuring tape",
         wrongs={"ruler": "A 30 cm ruler is far too short for a room.", "digital stopwatch": "A stopwatch measures time.", "measuring cylinder": "A measuring cylinder measures the volume of a liquid."},
         hints=["A classroom is several metres long.", "Which instrument can measure metres?", "Measuring tape."]),
    dict(id="e04_graph_flat", level=1, lo="1.4g",
         stem="Fig. 1 is a distance-time graph. What is the object doing between P and Q?",
         fig=lambda rng: G1.dt_graph([(0, 0), (10, 20), (20, 20), (30, 40)], xmax=30, ymax=48, xstep=5, ystep=10),
         correct="it is stationary",
         wrongs={"it is moving at a steady speed": "The distance does not change, so it is not moving.", "it is speeding up": "The distance stays at 20 m.", "it is moving backwards": "The distance stays the same; it does not decrease."},
         hints=["Does the distance change between P and Q?", "No change in distance means ...?", "Not moving."]),

    # ------------------------------------------------------------ L2
    dict(id="e04_door_handle_position", level=2, lo="1.4h",
         stem=f"The table shows where handles are fitted on doors.\n\n{md_table(['door', 'handle position'], [['P', 'near the hinges'], ['Q', 'far from the hinges']])}\n\nWhich door is easier to open, and why?",
         correct="Q, because the force acts further from the pivot and has a bigger turning effect",
         wrongs={"P, because the handle is closer to the pivot": "Closer to the pivot gives a SMALLER turning effect.", "both the same, because the same force is used": "The same force has a different turning effect at different distances.", "Q, because the door is lighter": "The doors are the same; the handle position differs."},
         hints=["Where is the pivot?", "Does a push far from the pivot turn the door more easily?", "Yes: bigger turning effect."]),
    dict(id="e04_identify_acceleration_table", level=2, lo="1.4d",
         stem=f"The table shows three vehicles.\n\n{md_table(['vehicle', 'speed at 0 s / m/s', 'speed at 10 s / m/s'], [['P', 10, 10], ['Q', 5, 15], ['R', 20, 12]])}\n\nWhich vehicle is accelerating (speeding up)?",
         correct="Q",
         wrongs={"P": "P's speed does not change.", "R": "R is slowing down.", "all three": "Only Q's speed increases."},
         hints=["Compare the speed at 0 s and at 10 s.", "Which one increases?", "Only one row goes up."]),
    dict(id="e04_steeper_graph", level=2, lo="1.4g",
         stem="Fig. 1 shows the distance-time graph of a cyclist. In which section is the cyclist moving faster, OP or PQ?",
         fig=lambda rng: G1.dt_graph([(0, 0), (10, 10), (20, 50)], xmax=20, ymax=60, xstep=5, ystep=10),
         correct="PQ, because the line is steeper",
         wrongs={"OP, because it comes first": "Order does not matter; steepness does.", "OP, because the line is less steep": "Less steep means slower.", "both the same, because the time is the same": "In the same time, PQ covers more distance."},
         hints=["Steeper line = more distance in the same time.", "Which section is steeper?", "PQ."]),
    dict(id="e04_change_direction", level=2, lo="1.4c",
         stem=f"The table shows a ball's motion before and after it is hit by a bat.\n\n{md_table(['before', 'after'], [['moving north at 10 m/s', 'moving south at 10 m/s']])}\n\nWhich effect did the force of the bat have?",
         correct="it changed the direction of the moving ball",
         wrongs={"it changed the speed of the ball": "The speed is 10 m/s both before and after.", "it changed the shape of the ball permanently": "The ball keeps its shape after the hit.", "it had no effect because the speed is the same": "The direction changed, which is an effect of force."},
         hints=["Compare speed before and after.", "Compare direction before and after.", "Direction changed."]),
    dict(id="e04_parallax_ruler", level=2, lo="1.4a",
         stem=f"A student measures a pencil with a ruler. The table shows two attempts.\n\n{md_table(['attempt', 'where the pencil starts on the ruler', 'reading at the other end / cm', 'answer given / cm'], [['1', 'at the 0 mark', 14.5, 14.5], ['2', 'at the 2.0 cm mark', 16.5, 16.5]])}\n\nWhat mistake was made in attempt 2?",
         correct="the 2.0 cm starting reading was not subtracted; the length is 14.5 cm",
         wrongs={"the ruler was too short": "The ruler covered the pencil.", "the pencil grew by 2 cm": "The pencil is the same; the reading was handled wrongly.", "attempt 1 is wrong because it started at 0": "Starting at 0 is fine; attempt 2 forgot to subtract."},
         hints=["Where did the pencil start on the ruler in attempt 2?", "Length = end reading − start reading.", "16.5 − 2.0."]),
    dict(id="e04_stopwatch_reset", level=2, lo="1.4b",
         stem=f"The table shows the buttons on a digital stopwatch.\n\n{md_table(['button', 'function'], [['start / stop', 'starts or stops the timing'], ['reset', 'sets the display back to 0:00.00']])}\n\nBefore timing a race, what should the student do?",
         correct="press reset so the display shows 0:00.00, then press start at the moment the race begins",
         wrongs={"press start, then reset at the end": "Resetting at the end wipes the result.", "press start before the race so the watch warms up": "The timing must start exactly when the race starts.", "read the display and subtract 1 second for reaction time": "Reaction time is not a fixed 1 s; reset and start promptly."},
         hints=["What should the display show at the start?", "Zero.", "Then start exactly as the race starts."]),
    dict(id="e04_speed_units", level=2, lo="1.4d",
         stem=f"The table lists units.\n\n{md_table(['unit'], [['m'], ['s'], ['m/s'], ['m/s²']])}\n\nWhich unit is used for acceleration?",
         correct="m/s²",
         wrongs={"m/s": "m/s is the unit of speed.", "m": "m is the unit of distance.", "s": "s is the unit of time."},
         hints=["Acceleration is change in speed per second.", "Speed is in m/s, so change in speed per second is ...?", "Metres per second, per second."]),
    dict(id="e04_balanced_bricks", level=2, lo="1.4c",
         stem="Fig. 1 shows bricks viewed from above with two forces on each. Which brick stays at rest?",
         fig=lambda rng: G1.block_forces([("P", [("left", 2), ("right", 2)]), ("Q", [("left", 2), ("up", 2)]), ("R", [("left", 2), ("left", 2)])]),
         correct="P, because the two equal forces act in opposite directions and cancel",
         wrongs={"Q, because the forces are equal": "Equal forces in DIFFERENT directions (not opposite) do not cancel.", "R, because both forces push the same way": "Two forces the same way add up and move the brick.", "all of them, because 2 N is a small force": "Any unbalanced force moves a free brick."},
         hints=["Forces cancel only when equal AND opposite.", "Which brick has equal and opposite forces?", "P."]),

    # ------------------------------------------------------------ L3
    dict(id="e04_wrench_explain", level=3, lo="1.4h",
         stem=f"A mechanic cannot loosen a tight nut with a short spanner.\n\n{md_table(['spanner', 'length / cm', 'result with the same push'], [['short', 15, 'nut does not move'], ['long', 45, 'nut loosens']])}\n\nExplain why the long spanner works.",
         correct="the force acts further from the nut (the pivot), so its turning effect is larger",
         wrongs={"the long spanner is heavier, so it pushes harder": "The push is the same; the distance from the pivot is what changes.", "the long spanner grips the nut more tightly": "Both spanners fit the nut the same way.", "the long spanner makes the nut smaller": "The nut does not change."},
         hints=["Where is the pivot?", "How far from it is the hand on each spanner?", "Further → bigger turning effect."],
         keypoints=[KP("force further from the pivot", "further", "farther", "longer", "distance", "away from"), KP("larger turning effect / moment", "turning effect", "moment", "turn", "larger", "bigger", "greater")]),
    dict(id="e04_graph_explain_stop", level=3, lo="1.4g",
         stem="Fig. 1 is the distance-time graph of a bus. Describe the bus's motion and explain how the graph shows it.",
         fig=lambda rng: G1.dt_graph([(0, 0), (20, 300), (40, 300), (60, 600)], xmax=60, ymax=700, xstep=10, ystep=100),
         correct="it moves at a steady speed, stops for 20 s (flat section), then moves at the same steady speed again",
         wrongs={"it speeds up, slows down, then speeds up": "Straight sloping lines mean steady speed, not speeding up.", "it moves, reverses, then moves forward": "The distance never falls, so it never reverses.", "it moves at a steady speed throughout": "The flat section from 20 s to 40 s shows a stop."},
         hints=["What does a straight sloping line mean?", "What does a flat line mean?", "Compare the slopes of the two sloping parts."],
         keypoints=[KP("flat section = stopped", "stop", "stationary", "rest", "not moving", "flat"), KP("steady speed in sloping parts", "steady", "constant", "same speed", "uniform")]),
    dict(id="e04_effects_two_at_once", level=3, lo="1.4c",
         stem=f"A footballer kicks a ball that was rolling slowly across the pitch.\n\n{md_table(['before the kick', 'after the kick'], [['rolling slowly to the left', 'flying fast to the right'], ['round', 'squashed for an instant, then round']])}\n\nWhich effects did the force of the kick have?",
         correct="it changed the ball's speed and direction, and briefly changed its shape",
         wrongs={"it only changed the ball's direction": "The speed also changed (slow to fast) and the ball was squashed for an instant.", "it only changed the ball's shape": "The ball also moved differently afterwards.", "it had no effect on the motion because the ball was already moving": "The speed AND direction changed."},
         hints=["Compare speed before and after.", "Compare direction before and after.", "What happened to the shape at the moment of the kick?"],
         keypoints=[KP("speed / direction changed", "speed", "direction", "faster", "motion"), KP("shape changed", "shape", "squash", "deform")]),
    dict(id="e04_reaction_time_measure", level=3, lo="1.4b",
         stem=f"A student times a 100 m race with a hand-held digital stopwatch. The table shows the results.\n\n{md_table(['timer', 'time / s'], [['electronic gate', 12.30], ['student with stopwatch', 12.52]])}\n\nWhy is the student's time different, and how can it be improved?",
         correct="the student's reaction time adds to the reading; starting and stopping promptly or using electronic timing reduces the error",
         wrongs={"the stopwatch is broken": "A 0.2 s difference is typical of human reaction time, not a fault.", "the student measured a longer track": "Both timed the same 100 m.", "the runner ran slower for the student": "There was one race; the timings differ because of the timer."},
         hints=["What does a person need time to do when they see the start?", "React.", "How does an electronic gate avoid that?"],
         keypoints=[KP("reaction time", "reaction", "react", "delay", "slow to press"), KP("use electronic timing / be prompt", "electronic", "light gate", "sensor", "prompt", "practise", "repeat")]),
    dict(id="e04_speed_vs_velocity_language", level=3, lo="1.4d",
         stem=f"Two students describe a bus.\n\n{md_table(['student', 'statement'], [['P', 'the bus has a high speed'], ['Q', 'the bus has a high acceleration']])}\n\nThe bus is moving at 20 m/s and its speed is not changing. Who is correct, and why?",
         correct="P, because speed is how far it moves each second, while acceleration is how much the speed changes each second, which is zero here",
         wrongs={"Q, because 20 m/s is a large acceleration": "20 m/s is a speed; the acceleration is zero because the speed is steady.", "both, because a fast bus must be accelerating": "A fast bus can have zero acceleration if its speed is constant.", "neither, because the bus is not moving": "It is moving at 20 m/s."},
         hints=["Is the speed changing?", "Acceleration measures change in speed.", "No change → zero acceleration."],
         keypoints=[KP("P is right about speed", "p", "speed"), KP("acceleration is zero / speed not changing", "zero", "not changing", "constant", "steady", "no acceleration")]),
    dict(id="e04_measure_small_object", level=3, lo="1.4a",
         stem=f"A student needs the thickness of one sheet of paper.\n\n{md_table(['method', 'result'], [['measure one sheet with a ruler', 'cannot read, less than 1 mm'], ['measure 100 sheets with a ruler', '10 mm']])}\n\nWhat is the thickness of one sheet, and why is the second method better?",
         correct="0.1 mm; measuring many sheets gives a reading the ruler can show, then divide by the number of sheets",
         wrongs={"10 mm; the ruler reading is the answer": "That is the thickness of 100 sheets.", "1 mm; the ruler's smallest division": "The ruler's smallest division is not the paper's thickness.", "0.1 mm; the ruler becomes more accurate with more sheets": "The ruler is the same; the stack is big enough to measure."},
         hints=["Why can't one sheet be measured with a ruler?", "What do you do with the 10 mm?", "Divide by 100."],
         keypoints=[KP("0.1 mm", "0.1"), KP("measure many and divide", "divide", "many sheets", "100", "stack", "share")]),
    dict(id="e04_average_speed_reason", level=3, lo="1.4e",
         stem=f"A car's journey is shown.\n\n{md_table(['stage', 'distance / km', 'time / h'], [['motorway', 90, 1], ['town traffic', 10, 0.5]])}\n\nThe driver says 'my average speed was 90 km/h'. Why is this wrong?",
         correct="average speed uses the total distance (100 km) and the total time (1.5 h), which gives about 67 km/h",
         wrongs={"the average is (90 + 20) ÷ 2 = 55 km/h": "Averaging the two stage speeds ignores how long each lasted.", "the driver is right because the motorway is most of the trip": "The slow town stage still counts in the total time.", "the average should be 100 km/h because 100 km were covered": "100 km in 1.5 h is not 100 km/h."},
         hints=["Add the distances and add the times.", "100 km in 1.5 h.", "Divide."],
         keypoints=[KP("total distance ÷ total time", "total", "whole", "divide", "100", "1.5"), KP("about 67 km/h", "67", "66")]),
    dict(id="e04_force_on_stationary", level=3, lo="1.4c",
         stem=f"A heavy box rests on the floor. A student pushes it.\n\n{md_table(['push / N', 'what happens'], [[50, 'box does not move'], [150, 'box starts to slide']])}\n\nWhy does the box not move with the 50 N push?",
         correct="friction from the floor balances the 50 N push, so the forces are balanced and the box stays at rest",
         wrongs={"50 N is not a force": "50 N is a force; it is just balanced by friction.", "the box pushes back with 150 N": "The floor's friction matches the push, 50 N, until the push is big enough.", "the floor has no effect on the box": "The floor provides the friction that stops the box."},
         hints=["What other force acts on the box along the floor?", "Friction.", "Balanced forces → no change in motion."],
         keypoints=[KP("friction", "friction", "grip", "rough"), KP("forces balanced", "balance", "equal", "cancel", "same size")]),

    # ------------------------------------------------------------ L4
    dict(id="e04_graph_two_objects", level=4, lo="1.4g",
         stem=f"The table gives distance-time data for two cyclists starting together.\n\n{md_table(['time / s', 'P distance / m', 'Q distance / m'], [[0, 0, 0], [10, 50, 30], [20, 100, 90], [30, 150, 180]])}\n\nWhich statement is correct?",
         correct="P moves at a steady 5 m/s; Q is accelerating and overtakes P after 20 s",
         wrongs={"P is accelerating because its distance keeps increasing": "P covers 50 m every 10 s: a STEADY speed.", "Q moves at a steady speed of 3 m/s": "Q covers 30, 60, then 90 m in each 10 s: speeding up.", "P is always ahead because it starts faster": "At 30 s Q (180 m) is ahead of P (150 m)."},
         hints=["Look at how much each covers in each 10 s.", "P: equal steps. Q: growing steps.", "Where does Q pass P?"],
         keypoints=[KP("P steady speed", "steady", "constant", "5 m/s", "same"), KP("Q accelerating / overtakes", "accelerat", "speeding up", "overtake", "ahead", "faster")]),
    dict(id="e04_acceleration_data_compare", level=4, lo="1.4f",
         stem=f"Two cars are tested from rest.\n\n{md_table(['car', 'final speed / m/s', 'time to reach it / s'], [['P', 30, 10], ['Q', 24, 6]])}\n\nWhich car has the greater acceleration, and why?",
         correct="Q, because its speed changes by 4 m/s each second compared with 3 m/s each second for P",
         wrongs={"P, because it reaches a higher speed": "Acceleration is the change in speed PER SECOND, not the final speed.", "P, because it takes longer": "Taking longer for a similar change means a SMALLER acceleration.", "both the same, because both start from rest": "Starting from rest does not make the accelerations equal."},
         hints=["Acceleration = change in speed ÷ time.", "P: 30 ÷ 10. Q: 24 ÷ 6.", "Compare 3 and 4."],
         keypoints=[KP("Q greater", "q"), KP("4 m/s² vs 3 m/s²", "4", "3", "per second", "each second")]),
    dict(id="e04_seesaw_balance", level=4, lo="1.4h",
         stem="Fig. 1 shows a see-saw. A heavy adult sits close to the pivot and a child sits at the far end, and it balances. Explain how.",
         fig=lambda rng: S.lever(pivot_frac=0.5, load=("adult", 0.35), effort=("child", 0.95)),
         correct="the child's smaller weight acts further from the pivot, giving the same turning effect as the adult's larger weight close to the pivot",
         wrongs={"the adult and child weigh the same": "An adult is heavier; the distances make the turning effects equal.", "the pivot pushes the child up": "The pivot supports the plank; the balance comes from the turning effects.", "the see-saw cannot balance with different weights": "It can, when the distances from the pivot differ."},
         hints=["What two things decide a turning effect?", "Force and distance from the pivot.", "Small force far away can match a large force close in."],
         keypoints=[KP("distance from pivot matters", "distance", "further", "closer", "far", "near"), KP("turning effects equal / balance", "equal", "same", "balance", "cancel", "turning effect", "moment")]),
    dict(id="e04_brake_effect_graph", level=4, lo="1.4c",
         stem=f"The table shows a cyclist's speed when the brakes are applied.\n\n{md_table(['time / s', 'speed / m/s'], [[0, 8], [1, 6], [2, 4], [3, 2], [4, 0]])}\n\nWhich statement correctly describes the effect of the braking force?",
         correct="the force slows the cyclist by 2 m/s every second until the cyclist stops",
         wrongs={"the force changes the cyclist's direction": "The speed falls; nothing in the table shows a change of direction.", "the force keeps the speed steady": "The speed falls from 8 to 0.", "the force makes the cyclist go faster at first": "The speed falls from the start."},
         hints=["How does the speed change each second?", "By 2 m/s.", "A force slowing a moving object."],
         keypoints=[KP("slows down / decelerates", "slow", "decelerat", "decrease", "reduce", "stop"), KP("2 m/s each second", "2", "each second", "per second")]),
    dict(id="e04_measuring_uncertainty", level=4, lo="1.4a",
         stem=f"Three students measure the same desk with a measuring tape.\n\n{md_table(['student', 'reading / cm'], [['P', 120.4], ['Q', 120.6], ['R', 124.0]])}\n\nWhich statement is the best conclusion?",
         correct="P and Q agree closely; R probably made a mistake such as not keeping the tape straight or misreading the start",
         wrongs={"R is correct because 124.0 is the biggest": "The biggest reading is not the right one; R disagrees with two careful readings.", "all three are wrong because they differ": "Small differences are normal; R's is large and points to an error.", "the desk changed length between readings": "A desk does not change length."},
         hints=["Which two readings are close?", "Which one stands out?", "What could cause a 3.5 cm error?"],
         keypoints=[KP("R is the odd one / error", "r", "error", "mistake", "wrong", "odd"), KP("P and Q agree / repeat readings", "agree", "close", "similar", "average", "repeat")]),
    dict(id="e04_graph_which_fastest_start", level=4, lo="1.4g",
         stem="Fig. 1 is the distance-time graph of a runner. Describe how the speed changes, giving the evidence.",
         fig=lambda rng: G1.dt_graph([(0, 0), (10, 80), (20, 120), (30, 130)], xmax=30, ymax=150, xstep=5, ystep=25),
         correct="the runner slows down: each section is less steep than the one before (80 m, then 40 m, then 10 m in each 10 s)",
         wrongs={"the runner speeds up because the distance keeps rising": "The distance rises more SLOWLY each section, so the runner is slowing.", "the runner moves at a steady speed": "The slope changes at P and Q.", "the runner stops at Q": "The last section still rises, so the runner is moving, just slowly."},
         hints=["Compare the slopes of OP, PQ and QR.", "Steep, then less steep, then almost flat.", "Less steep = slower."],
         keypoints=[KP("slowing down", "slow", "decreas", "less", "decelerat"), KP("evidence: less steep / smaller distance each 10 s", "steep", "gradient", "slope", "80", "40", "10")]),
    dict(id="e04_force_effect_identify_data", level=4, lo="1.4c",
         stem=f"The table shows what happens to objects when a force acts.\n\n{md_table(['object', 'before', 'after'], [['clay', 'ball', 'flat disc'], ['trolley', 'at rest', 'moving at 2 m/s'], ['spinner', 'at rest', 'spinning about its centre']])}\n\nWhich row shows a turning effect?",
         correct="the spinner, because it rotates about a pivot (its centre)",
         wrongs={"the clay, because it was pressed flat": "That is a change in shape.", "the trolley, because it started to move": "That is a change in the state of rest.", "all three rows": "Only the spinner turns about a pivot."},
         hints=["A turning effect makes something rotate about a point.", "Which object rotates?", "The spinner."],
         keypoints=[KP("spinner", "spinner"), KP("rotates about a pivot / centre", "rotat", "spin", "turn", "pivot", "centre", "center")]),
    dict(id="e04_timing_method_improve", level=4, lo="1.4b",
         stem=f"A student times a ball rolling 2 m down a ramp. The table shows five trials with a hand-held stopwatch.\n\n{md_table(['trial', 'time / s'], [[1, 1.85], [2, 1.72], [3, 1.91], [4, 1.78], [5, 1.80]])}\n\nWhat should the student do with these results, and why?",
         correct="take the average of the five, because reaction time makes each reading slightly different",
         wrongs={"use the smallest time, because it has the least reaction time in it": "The smallest could be an early stop; averaging cancels random errors better.", "use only trial 1, because the ball was freshest": "The ball does not get tired; repeats are there to average.", "throw away all the results because they differ": "Small differences are normal; the average is reliable."},
         hints=["Why do the times differ?", "What do you do with repeated readings?", "Average them."],
         keypoints=[KP("average / mean", "average", "mean"), KP("reaction time causes variation", "reaction", "human", "random", "vary", "differ")]),

    # ------------------------------------------------------------ L5
    dict(id="e04_design_speed_experiment", level=5, lo="1.4e",
         stem=f"A student plans to find the average speed of a toy car.\n\n{md_table(['step', 'detail'], [['distance', 'measure with a 30 cm ruler, laid end to end 6 times'], ['time', 'start the stopwatch when the car is released, stop when it crosses the line'], ['repeats', 'once']])}\n\nWhich improvement matters most for a reliable result?",
         correct="repeat the timing several times and average, because reaction time varies each run",
         wrongs={"use a longer ruler because the car might be faster than the ruler": "Laying the ruler end to end works; a tape is neater but not the main problem.", "time with a wall clock instead": "A wall clock has no hundredths and is harder to start and stop.", "release the car from a greater height so it is faster": "Faster makes timing errors WORSE."},
         hints=["Which measurement has the biggest random error?", "Timing by hand.", "Repeats and averages reduce it."],
         keypoints=[KP("repeat and average", "repeat", "average", "mean", "several"), KP("reaction time / timing error", "reaction", "timing", "error", "vary")]),
    dict(id="e04_graph_misread", level=5, lo="1.4g",
         stem="Fig. 1 is a distance-time graph. A student says 'the object is slowing down between P and Q because the line goes flat'. What is wrong with this?",
         fig=lambda rng: G1.dt_graph([(0, 0), (10, 40), (20, 40), (30, 60)], xmax=30, ymax=70, xstep=5, ystep=10),
         correct="a flat line means the object is stationary the whole time between P and Q, not slowing; the slowing happened at P",
         wrongs={"nothing; a flat line shows slowing down": "A flat line shows NO distance covered: the object is at rest.", "the object is moving backwards between P and Q": "The distance stays at 40 m; it does not fall.", "the object is moving at a steady speed between P and Q": "A steady speed would give a sloping line."},
         hints=["What does the distance do between P and Q?", "Nothing: it stays at 40 m.", "What does that mean about motion?"],
         keypoints=[KP("stationary / at rest", "stationary", "rest", "not moving", "stopped", "still"), KP("flat line = no distance covered", "flat", "no distance", "same distance", "40")]),
    dict(id="e04_turning_effect_design", level=5, lo="1.4h",
         stem=f"A designer is choosing where to put the handle on a heavy gate that turns on hinges.\n\n{md_table(['option', 'handle distance from hinges / m'], [['P', 0.2], ['Q', 0.8], ['R', 1.4]])}\n\nWhich option should be chosen for the easiest opening, and what is the reason?",
         correct="R, because the same push has the largest turning effect when applied furthest from the hinges",
         wrongs={"P, because a handle near the hinges is strongest": "Near the hinges the turning effect is smallest, so the gate is hardest to open.", "Q, because it is in the middle": "The middle is not the best; the far end gives the biggest turning effect.", "any option, because the push is the same": "The same push has different turning effects at different distances."},
         hints=["Turning effect depends on force and distance from the pivot.", "Which option is furthest from the hinges?", "R."],
         keypoints=[KP("R / furthest from hinges", "r", "furthest", "farthest", "1.4", "far"), KP("largest turning effect for the same force", "turning effect", "moment", "easier", "less force", "larger")]),
    dict(id="e04_crumple_zone", level=5, lo="1.4c",
         stem=f"The table compares two cars in a crash test at the same speed.\n\n{md_table(['car', 'front of car', 'time for car to stop / s', 'injury to dummy'], [['P', 'rigid', 0.05, 'severe'], ['Q', 'crumples', 0.20, 'minor']])}\n\nWhy is the dummy in Q less injured?",
         correct="the crumpling front takes longer to stop the car, so the dummy's speed changes more gradually (smaller deceleration and force)",
         wrongs={"the rigid front is stronger and protects better": "The rigid front stops the car so quickly that the force on the dummy is huge.", "car Q was moving more slowly": "Both were tested at the same speed.", "the dummy in Q did not stop": "It stopped, but over a longer time."},
         hints=["Compare the stopping times.", "Same change in speed over a longer time means ...?", "Smaller deceleration, smaller force."],
         keypoints=[KP("longer time to stop", "longer", "more time", "0.2", "slowly", "gradual"), KP("smaller deceleration / force", "decelerat", "force", "smaller", "less", "lower")]),
    dict(id="e04_evaluate_speed_claim", level=5, lo="1.4d",
         stem=f"An advert says: 'This scooter accelerates from 0 to 10 m/s, faster than a sports car that goes from 0 to 30 m/s.' The table gives the data.\n\n{md_table(['vehicle', 'speed change / m/s', 'time / s'], [['scooter', 10, 2], ['sports car', 30, 4]])}\n\nIs the advert right?",
         correct="partly: the scooter's acceleration is 5 m/s², less than the car's 7.5 m/s², so the car accelerates faster even though the scooter reaches its top speed sooner",
         wrongs={"yes, because 2 s is less than 4 s": "The car's speed changes by more in each second: compare change in speed ÷ time.", "yes, because the scooter has a smaller top speed": "Top speed is not acceleration.", "no, because the scooter is not a car": "The vehicle type is irrelevant; compare the accelerations."},
         hints=["Acceleration = change in speed ÷ time.", "Scooter: 10 ÷ 2. Car: 30 ÷ 4.", "Compare 5 with 7.5."],
         keypoints=[KP("car's acceleration is larger (7.5 vs 5)", "7.5", "larger", "greater", "more", "car"), KP("time alone does not decide", "time", "change in speed", "divide", "per second", "partly", "less than")]),
    dict(id="e04_two_graphs_same_journey", level=5, lo="1.4g",
         stem=f"A bus and a bicycle leave the same point. The table gives their distance-time data.\n\n{md_table(['time / min', 'bus distance / km', 'bicycle distance / km'], [[0, 0, 0], [5, 0, 1.5], [10, 4, 3], [15, 8, 4.5]])}\n\nWhich statement is correct?",
         correct="the bicycle moves at a steady 0.3 km/min; the bus waits 5 min then travels at 0.8 km/min and overtakes the bicycle before 10 min",
         wrongs={"the bus is always behind because it started late": "At 10 min the bus (4 km) is ahead of the bicycle (3 km).", "the bicycle accelerates throughout": "It covers 1.5 km every 5 min: steady speed.", "the bus moves at 0.4 km/min": "After its 5 min wait it covers 4 km in 5 min: 0.8 km/min."},
         hints=["Check equal steps for steady speed.", "When does the bus start moving?", "Compare distances at 10 min."],
         keypoints=[KP("bicycle steady", "steady", "constant", "0.3", "same"), KP("bus waits then faster / overtakes", "wait", "stationary", "overtake", "0.8", "faster", "ahead")]),
    dict(id="e04_ruler_choice_precision", level=5, lo="1.4a",
         stem=f"A student wants to measure the diameter of a 5-cent coin and the length of a football pitch.\n\n{md_table(['instrument', 'range', 'smallest division'], [['ruler', '30 cm', '1 mm'], ['measuring tape', '50 m', '1 mm'], ['trundle wheel', 'unlimited', '1 cm']])}\n\nWhich instruments should be used, and why?",
         correct="ruler for the coin (small object, mm divisions); measuring tape or trundle wheel for the pitch (needs a long range, mm precision not needed)",
         wrongs={"measuring tape for both, because it has mm divisions": "A 50 m tape is awkward for a 2 cm coin; a ruler is better suited.", "trundle wheel for both, because it has unlimited range": "Its 1 cm divisions are far too coarse for a coin.", "ruler for both, laid end to end": "Laying a 30 cm ruler across a 100 m pitch is slow and inaccurate."},
         hints=["Match the range to the object.", "Match the precision to what is needed.", "Small and precise → ruler; long → tape or wheel."],
         keypoints=[KP("ruler for the coin", "ruler"), KP("tape / wheel for the pitch", "tape", "trundle", "wheel")]),
]

register_explain(EXPLAIN, chapter=4)
