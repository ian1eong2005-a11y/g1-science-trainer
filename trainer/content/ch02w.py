"""Ch 2 Electricity: extra calculation / data templates adapted from the Chapter 1.2 assignments (1, 2, 2a, 2b, 3a, 3b, 4a, 4b)
and the mastery test, plus explanation items from the same worksheets. Numbers are varied on every serve."""
from .. import sketches as S
from .base import fmt, md_table, nice, numeric_options, pick, register_explain, template, text_options

KP = lambda label, *phr: {"label": label, "any": list(phr)}
SRC = "_Adapted from the QTSS Chapter 1.2 worksheets._"


def money(x):
    return f"${x:,.2f}"


# ---------------------------------------------------------------- L1
@template("c02w_charger_time", chapter=2, level=1, lo="1.2l")
def charger_time(rng):
    P = nice(rng, 20, 25, 40, 50)
    E = P * nice(rng, 100, 125, 200, 250)
    t = E / P
    opts, key, mis = numeric_options(rng, t, [
        (E * P, "Time = energy ÷ power; do not multiply."),
        (P / E, "Upside down: energy ÷ power."),
        (E, "That is the energy; divide it by the power."),
    ], unit="s", sf=3)
    return dict(
        stem=f"Afzal's phone charger is used.\n\n{md_table(['power rating of charger / W', 'electrical energy supplied / J'], [[P, E]])}\n\nHow long does the charger take to supply this energy?",
        options=opts, key=key, misconceptions=mis,
        formula="time = energy ÷ power",
        working=[f"t = {E} ÷ {P}", f"= **{fmt(t)} s**", SRC],
        hints=["Rearrange power = energy ÷ time.", "time = energy ÷ power.", f"{E} ÷ {P}."],
    )


@template("c02w_minifan_power", chapter=2, level=1, lo="1.2l")
def minifan_power(rng):
    P = nice(rng, 5, 10, 20, 25)
    t = nice(rng, 20, 30, 40)
    E = P * t
    opts, key, mis = numeric_options(rng, P, [
        (E * t, "Power = energy ÷ time; do not multiply."),
        (t / E, "Upside down: energy ÷ time."),
        (E, "That is the energy in joules; divide by the seconds."),
    ], unit="W", sf=3)
    return dict(
        stem=f"A USB mini fan is plugged into a phone.\n\n{md_table(['energy used / J', 'time / s'], [[E, t]])}\n\nWhat is the power of the mini fan?",
        options=opts, key=key, misconceptions=mis,
        formula="power = energy ÷ time",
        working=[f"P = {E} ÷ {t}", f"= **{fmt(P)} W**", SRC],
        hints=["Power is energy per second.", "Divide.", f"{E} ÷ {t}."],
    )


@template("c02w_oven_power_iv", chapter=2, level=1, lo="1.2l")
def oven_power_iv(rng):
    V = nice(rng, 230, 240, 250)
    I = nice(rng, 2, 3, 4, 5, 8)
    P = I * V
    opts, key, mis = numeric_options(rng, P, [
        (V / I, "Power = current × voltage; do not divide."),
        (V + I, "Multiply, do not add."),
        (I, "That is the current; multiply by the voltage."),
    ], unit="W", sf=4)
    return dict(
        stem=f"An oven is tested.\n\n{md_table(['voltage / V', 'current / A'], [[V, I]])}\n\nCalculate the power of the oven.",
        options=opts, key=key, misconceptions=mis,
        formula="power = current × voltage",
        working=[f"P = {I} × {V}", f"= **{P} W**", SRC],
        hints=["Power = current × voltage.", f"{I} × {V}.", "Watts."],
    )


# ---------------------------------------------------------------- L2
@template("c02w_bulb_power_kw_units", chapter=2, level=2, lo="1.2l")
def bulb_power_kw_units(rng):
    I = nice(rng, 2, 2.5, 4)
    V = nice(rng, 6, 8, 12)
    P = I * V
    opts, key, mis = text_options(rng, f"{P / 1000:g} kW", {
        f"{V / I:g} W": "Power = current × voltage; do not divide.",
        f"{P:g} J": "The unit of power is the watt, not the joule.",
        f"{V - I:g} W": "Multiply the current by the voltage.",
    })
    return dict(
        stem=f"A bulb in a circuit has the readings shown.\n\n{md_table(['current / A', 'potential difference / V'], [[I, V]])}\n\nWhat is the power of the bulb? (1 kW = 1000 W)",
        options=opts, key=key, misconceptions=mis,
        formula="power = current × voltage;  1 kW = 1000 W",
        working=[f"P = {I} × {V} = {P:g} W", f"= **{P / 1000:g} kW**", SRC],
        hints=["Multiply current by voltage.", f"{P:g} W.", "Change to kW: divide by 1000."],
    )


@template("c02w_iron_minutes_energy", chapter=2, level=2, lo="1.2l")
def iron_minutes_energy(rng):
    P = nice(rng, 400, 500, 1000, 1200)
    m = nice(rng, 15, 20, 30)
    E = P * m * 60
    opts, key, mis = numeric_options(rng, E, [
        (P * m, "The time must be in seconds: 1 min = 60 s."),
        (P * m * 100, "1 minute = 60 s, not 100 s."),
        (P / (m * 60), "Energy = power × time; do not divide."),
    ], unit="J", sf=4)
    return dict(
        stem=f"Syafrinah irons her clothes.\n\n{md_table(['power of iron / W', 'time used'], [[P, f'{m} min']])}\n\nCalculate the electrical energy used, in joules.",
        options=opts, key=key, misconceptions=mis,
        formula="energy = power × time (s);  1 min = 60 s",
        working=[f"t = {m} × 60 = {m * 60} s", f"E = {P} × {m * 60} = **{fmt(E, sf=4)} J**", SRC],
        hints=["Change minutes to seconds.", f"{m} min = {m * 60} s.", f"{P} × {m * 60}."],
    )


@template("c02w_heater_current", chapter=2, level=2, lo="1.2l")
def heater_current(rng):
    V = nice(rng, 230, 240, 250)
    P = V * nice(rng, 2, 4, 5, 6)
    I = P / V
    opts, key, mis = numeric_options(rng, I, [
        (P * V, "Current = power ÷ voltage; do not multiply."),
        (V / P, "Upside down: power ÷ voltage."),
        (P / 1000, "Divide by the voltage, not by 1000."),
    ], unit="A", sf=3)
    return dict(
        stem=f"A heater is connected to the mains.\n\n{md_table(['power / W', 'mains voltage / V'], [[P, V]])}\n\nCalculate the current it draws.",
        options=opts, key=key, misconceptions=mis,
        formula="current = power ÷ voltage",
        working=[f"I = {P} ÷ {V}", f"= **{fmt(I)} A**", SRC],
        hints=["Rearrange power = current × voltage.", "current = power ÷ voltage.", f"{P} ÷ {V}."],
    )


@template("c02w_cost_simple_kw_h", chapter=2, level=2, lo="1.2m")
def cost_simple_kw_h(rng):
    Pk = nice(rng, 0.5, 1, 2, 2.5)
    h = nice(rng, 2, 3, 4)
    rate = nice(rng, 0.20, 0.25, 0.30)
    c = Pk * h * rate
    opts, key, mis = numeric_options(rng, c, [
        (Pk * h, "That is the energy in kWh; multiply by the price."),
        (Pk * rate, "Multiply by the hours as well."),
        (Pk * h * rate * 100, "The price is already in dollars."),
    ], unit="$", sf=3, dp=2)
    return dict(
        stem=f"Electricity costs {money(rate)} per kWh.\n\n{md_table(['appliance power', 'time used'], [[f'{Pk:g} kW', f'{h} h']])}\n\nWhat is the cost of using the appliance?",
        options=opts, key=key, misconceptions=mis,
        formula="energy (kWh) = kW × h;  cost = kWh × price",
        working=[f"E = {Pk:g} × {h} = {Pk * h:g} kWh", f"cost = {Pk * h:g} × {money(rate)} = **{money(c)}**", SRC],
        hints=["Energy in kWh = kW × hours.", f"{Pk * h:g} kWh.", f"× {rate}."],
    )


@template("c02w_oven_kwh_then_cost", chapter=2, level=2, lo="1.2m")
def oven_kwh_then_cost(rng):
    Pk = nice(rng, 1.5, 2, 3)
    h = nice(rng, 2, 3, 4)
    cents = nice(rng, 15, 20, 25)
    E = Pk * h
    c = E * cents
    opts, key, mis = text_options(rng, f"{E:g} kWh, costing {c:g} cents", {
        f"{E:g} kWh, costing {E * cents / 100:g} cents": "Multiply the kWh by the price per kWh in cents.",
        f"{Pk * h * 60:g} kWh, costing {Pk * h * 60 * cents:g} cents": "kWh uses hours, not minutes.",
        f"{E:g} kW, costing {c:g} cents": "The energy unit is kWh, not kW.",
    })
    return dict(
        stem=f"An oven bakes a chicken. Electricity costs {cents} cents per kWh.\n\n{md_table(['power of oven', 'baking time'], [[f'{Pk:g} kW', f'{h} h']])}\n\nHow much energy is used, and what does it cost?",
        options=opts, key=key, misconceptions=mis,
        formula="energy (kWh) = kW × h;  cost = kWh × price per kWh",
        working=[f"E = {Pk:g} × {h} = {E:g} kWh", f"cost = {E:g} × {cents} = **{c:g} cents**", SRC],
        hints=["kW × hours gives kWh.", f"{E:g} kWh.", f"{E:g} × {cents} cents."],
    )


# ---------------------------------------------------------------- L3
@template("c02w_fridge_power_rating", chapter=2, level=3, lo="1.2m")
def fridge_power_rating(rng):
    h = nice(rng, 10, 12, 24)
    Pk = nice(rng, 0.1, 0.15, 0.3)
    E = Pk * h
    opts, key, mis = numeric_options(rng, Pk, [
        (E * h, "Power = energy ÷ time; do not multiply."),
        (h / E, "Upside down: energy ÷ time."),
        (E, "That is the energy in kWh; divide by the hours."),
    ], unit="kW", sf=3)
    return dict(
        stem=f"A restaurant fridge is monitored.\n\n{md_table(['energy used / kWh', 'time switched on / h'], [[fmt(E), h]])}\n\nCalculate the power rating of the fridge, in kW.",
        options=opts, key=key, misconceptions=mis,
        formula="power (kW) = energy (kWh) ÷ time (h)",
        working=[f"P = {fmt(E)} ÷ {h}", f"= **{fmt(Pk)} kW**", SRC],
        hints=["Rearrange energy = power × time.", "power = energy ÷ time.", f"{fmt(E)} ÷ {h}."],
    )


@template("c02w_aircon_minutes_kwh_cost", chapter=2, level=3, lo="1.2m")
def aircon_minutes_kwh_cost(rng):
    P = nice(rng, 1000, 1500, 2000)
    m = nice(rng, 90, 120, 150)
    cents = nice(rng, 15, 20, 25)
    E = P / 1000 * m / 60
    c = E * cents
    opts, key, mis = text_options(rng, f"{E:g} kWh, costing {c:g} cents", {
        f"{P / 1000 * m:g} kWh, costing {P / 1000 * m * cents:g} cents": "Change the minutes to hours before multiplying.",
        f"{P * m / 60:g} kWh, costing {P * m / 60 * cents:g} cents": "Change the watts to kilowatts.",
        f"{E:g} kWh, costing {E:g} cents": "Multiply the kWh by the price.",
    })
    return dict(
        stem=f"Adam switches on an air-conditioner. Electricity costs {cents} cents per kWh.\n\n{md_table(['power / W', 'time on'], [[P, f'{m} min']])}\n\nHow much energy is used, and what does it cost?",
        options=opts, key=key, misconceptions=mis,
        formula="energy (kWh) = power (kW) × time (h);  cost = kWh × price",
        working=[f"{P} W = {P / 1000:g} kW;  {m} min = {m / 60:g} h", f"E = {P / 1000:g} × {m / 60:g} = {E:g} kWh", f"cost = {E:g} × {cents} = **{c:g} cents**", SRC],
        hints=["Convert W → kW and min → h.", f"{P / 1000:g} kW and {m / 60:g} h.", f"Multiply, then × {cents}."],
    )


@template("c02w_switch_meter_combo", chapter=2, level=3, lo="1.2a")
def switch_meter_combo(rng):
    I = nice(rng, 0.5, 1, 1.5)
    V = nice(rng, 3, 6, 9)
    ans = f"switch closed, ammeter {I:g} A, voltmeter {V:g} V"
    opts, key, mis = text_options(rng, ans, {
        f"switch closed, ammeter 0 A, voltmeter 0 V": "With the switch closed the circuit is complete, so there is a current and a voltage across the lamp.",
        f"switch open, ammeter {I:g} A, voltmeter 0 V": "With the switch open no current flows.",
        f"switch open, ammeter 0 A, voltmeter {V:g} V": "With no current there is no voltage across the lamp.",
    })
    return dict(
        stem=f"Fig. 1 shows a circuit with a **{V:g} V** battery, a switch, a lamp, an ammeter and a voltmeter across the lamp. Which row shows a possible set of readings?",
        figure=S.circuit(["ammeter", "lamp"], top=("battery", "switch_closed"), voltmeter_across=1),
        options=opts, key=key, misconceptions=mis,
        formula="a closed switch completes the circuit: current flows and the lamp has a voltage across it; an open switch gives 0 A and 0 V across the lamp",
        working=["closed switch → complete circuit → current and voltage across the lamp", f"**{ans}**", SRC],
        hints=["Is the switch open or closed in the figure?", "What does an open switch do to the current?", "No current → no voltage across the lamp."],
    )


@template("c02w_parallel_voltmeters_equal", chapter=2, level=3, lo="1.2g")
def parallel_voltmeters_equal(rng):
    V = nice(rng, 0.8, 1.2, 1.5, 3)
    opts, key, mis = text_options(rng, f"V1 = {V:g} V and V2 = {V:g} V", {
        f"V1 = {V:g} V and V2 = {V / 2:g} V": "In parallel the voltage is the SAME across every branch.",
        f"V1 = {V / 2:g} V and V2 = {V / 2:g} V": "The branches do not share the voltage; each gets the full voltage.",
        f"V1 = {2 * V:g} V and V2 = {V:g} V": "Branch voltages are equal to the supply voltage, not double it.",
    })
    return dict(
        stem=f"Fig. 1 shows two lamps in parallel. A voltmeter V3 across the battery reads **{V:g} V**. Voltmeters V1 and V2 are across the two lamps. What do V1 and V2 read?",
        figure=S.circuit([], parallel=[["lamp"], ["lamp"]], top=("battery",), labels=["V1", "V2"]),
        options=opts, key=key, misconceptions=mis,
        formula="the voltage is the same across the separate branches of a parallel circuit",
        working=["each branch is connected directly across the battery", f"**V1 = V2 = {V:g} V**", SRC],
        hints=["Each lamp is on its own branch across the battery.", "Parallel branches have the same voltage.", f"Both read {V:g} V."],
    )


# ---------------------------------------------------------------- L4
@template("c02w_three_branch_ammeters", chapter=2, level=4, lo="1.2e")
def three_branch_ammeters(rng):
    I1 = nice(rng, 2, 3, 4)
    I3 = nice(rng, 4, 5, 6)
    tot = I1 + I3 + nice(rng, 1, 2)
    I2 = tot - I1 - I3
    opts, key, mis = text_options(rng, f"A2 = {I1} A and A4 = {I2} A", {
        f"A2 = {tot} A and A4 = {I2} A": "A2 is in the same branch as A1, so it reads the same as A1.",
        f"A2 = {I1} A and A4 = {tot - I1} A": "A4's branch gets what is left after BOTH other branches: total − A1 − A5.",
        f"A2 = {I1} A and A4 = {I3} A": "A4 is not in the same branch as A5; subtract both known branches from the total.",
    })
    return dict(
        stem=f"Fig. 1 shows three lamps in parallel. Ammeter A1 is in the first branch, A2 further along the same branch, A3 next to the battery, A4 in the second branch and A5 in the third branch.\n\n{md_table(['ammeter', 'reading / A'], [['A1', I1], ['A3', tot], ['A5', I3]])}\n\nWhat are the readings of A2 and A4?",
        figure=S.circuit(["ammeter"], parallel=[["ammeter", "lamp", "ammeter"], ["ammeter", "lamp"], ["ammeter", "lamp"]], top=("battery",), labels=["A3", "", "", ""]),
        options=opts, key=key, misconceptions=mis,
        formula="series: same current along a branch;  parallel: branch currents add up to the battery current",
        working=[f"A2 is in A1's branch: A2 = {I1} A", f"A4 = {tot} − {I1} − {I3} = **{I2} A**", SRC],
        hints=["A1 and A2 are in the same branch.", "The three branches add up to A3.", f"{tot} − {I1} − {I3}."],
    )


@template("c02w_cost_proportion", chapter=2, level=4, lo="1.2m")
def cost_proportion(rng):
    base_cost = nice(rng, 0.20, 0.30)
    P2 = nice(rng, 200, 400, 500)
    h2 = nice(rng, 2, 4, 5)
    c = base_cost * (P2 / 1000) * h2
    opts, key, mis = numeric_options(rng, c, [
        (base_cost * h2, "The computer uses less power than 1000 W: scale the cost down by the power as well."),
        (base_cost * P2 / 1000, "Multiply by the hours as well."),
        (base_cost * P2 * h2, "Change the watts to kilowatts."),
    ], unit="$", sf=3, dp=2)
    return dict(
        stem=f"It costs {money(base_cost)} to run a 1000 W heater for 1 hour.\n\n{md_table(['appliance', 'power / W', 'time / h'], [['computer', P2, h2]])}\n\nWhat is the cost of running the computer?",
        options=opts, key=key, misconceptions=mis,
        formula="cost is proportional to power × time;  1000 W for 1 h costs the price of 1 kWh",
        working=[f"1 kWh costs {money(base_cost)}", f"computer: {P2 / 1000:g} kW × {h2} h = {P2 / 1000 * h2:g} kWh", f"cost = {P2 / 1000 * h2:g} × {money(base_cost)} = **{money(c)}**", SRC],
        hints=[f"The heater uses 1 kWh, so 1 kWh costs {money(base_cost)}.", "How many kWh does the computer use?", f"{P2 / 1000:g} × {h2}."],
    )


@template("c02w_correct_expression", chapter=2, level=4, lo="1.2m")
def correct_expression(rng):
    P = nice(rng, 2400, 2500, 3000)
    m = nice(rng, 30, 45)
    rate = nice(rng, 0.25, 0.30)
    ans = f"cost = {P / 1000:g} × {m / 60:g} × {rate}"
    opts, key, mis = text_options(rng, ans, {
        f"cost = {P / 1000:g} × {m} × {int(rate * 100)}": "The time must be in hours and the price in dollars per kWh.",
        f"cost = {P} × {m} × {m / 60:g}": "The power must be in kW and the price must appear.",
        f"cost = {P} × {m / 60:g} × {int(rate * 100)}": "The power must be in kW (divide by 1000) and the price in dollars.",
    })
    return dict(
        stem=f"The cost of electricity is {money(rate)} per unit (kWh).\n\n{md_table(['appliance', 'power / W', 'time used'], [['electric kettle', P, f'{m} min']])}\n\nWhich is the correct calculation for the cost, in dollars?",
        options=opts, key=key, misconceptions=mis,
        formula="cost ($) = power (kW) × time (h) × price per kWh ($)",
        working=[f"{P} W = {P / 1000:g} kW;  {m} min = {m / 60:g} h", f"**{ans}**", SRC],
        hints=["Change W to kW.", "Change minutes to hours.", "Multiply by the price in dollars."],
    )


@template("c02w_microwave_time_from_kwh", chapter=2, level=4, lo="1.2m")
def microwave_time_from_kwh(rng):
    P = nice(rng, 600, 800, 1200)
    m = nice(rng, 15, 30, 45)
    E = P / 1000 * m / 60
    opts, key, mis = numeric_options(rng, m, [
        (m / 60, "That is the time in hours; the question asks for minutes."),
        (E / P * 60, "Change the power to kW before dividing."),
        (m * 60, "That is seconds; hours × 60 gives minutes."),
    ], unit="min", sf=3)
    return dict(
        stem=f"Elvis warms a drink in a microwave oven.\n\n{md_table(['power / W', 'energy used / kWh'], [[P, fmt(E)]])}\n\nHow many minutes was the oven on?",
        options=opts, key=key, misconceptions=mis,
        formula="time (h) = energy (kWh) ÷ power (kW);  minutes = hours × 60",
        working=[f"{P} W = {P / 1000:g} kW", f"t = {fmt(E)} ÷ {P / 1000:g} = {m / 60:g} h = **{m} min**", SRC],
        hints=["Change the power to kW.", "time = energy ÷ power gives hours.", "Multiply by 60."],
    )


# ---------------------------------------------------------------- L5
@template("c02w_two_rate_bill", chapter=2, level=5, lo="1.2n")
def two_rate_bill(rng):
    u1 = nice(rng, 900, 976, 1020)
    r1 = nice(rng, 0.2565, 0.2602)
    u2 = nice(rng, 40, 49, 60)
    r2 = r1 + 0.0008
    c1, c2 = u1 * r1, u2 * r2
    tot = c1 + c2
    opts, key, mis = numeric_options(rng, tot, [
        (c1, "That is only the first block of units; add the second block."),
        ((u1 + u2) * r1, "The second block has a different rate."),
        ((u1 + u2) * (r1 + r2), "Do not add the rates; each block uses its own rate."),
    ], unit="$", sf=5, dp=2)
    return dict(
        stem=f"Part of Alif's electricity bill is shown. Two different rates apply.\n\n{md_table(['units / kWh', 'rate / $ per kWh', 'amount / $'], [[u1, f'{r1:.4f}', '?'], [u2, f'{r2:.4f}', '?'], ['total', '', '?']])}\n\nWhat is the total cost?",
        options=opts, key=key, misconceptions=mis,
        formula="amount = units × rate for each block;  total = sum of the amounts",
        working=[f"{u1} × {r1:.4f} = {money(c1)}", f"{u2} × {r2:.4f} = {money(c2)}", f"total = **{money(tot)}**", SRC],
        hints=["Work out each block separately.", f"{u1} × {r1:.4f} first.", "Then add the second block."],
    )


@template("c02w_water_heater_cost_minutes", chapter=2, level=5, lo="1.2m")
def water_heater_cost_minutes(rng):
    P = nice(rng, 1500, 2000, 3000)
    m = nice(rng, 20, 30, 45)
    cents = nice(rng, 20, 25, 30)
    E = P / 1000 * m / 60
    c = E * cents
    opts, key, mis = numeric_options(rng, c, [
        (P / 1000 * m * cents, "Change the minutes to hours."),
        (P * m / 60 * cents, "Change the watts to kilowatts."),
        (E, "That is the energy in kWh; multiply by the price."),
    ], unit="cents", sf=3)
    return dict(
        stem=f"A water heater is used. One unit (kWh) costs {cents} cents.\n\n{md_table(['power / W', 'time on'], [[P, f'{m} min']])}\n\nCalculate the cost, in cents.",
        options=opts, key=key, misconceptions=mis,
        formula="energy (kWh) = power (kW) × time (h);  cost = kWh × price",
        working=[f"E = {P / 1000:g} × {m / 60:g} = {fmt(E)} kWh", f"cost = {fmt(E)} × {cents} = **{fmt(c)} cents**", SRC],
        hints=["kW × h gives kWh.", f"{P / 1000:g} × {m / 60:g}.", f"× {cents}."],
    )


# ================================================================ EXPLANATION (worksheet items)
EXPLAIN = [
    dict(id="e02w_blown_fuse_cause", level=2, lo="1.2a",
         stem=f"Shilah's circuit stops working. The table shows what she finds.\n\n{md_table(['observation'], [['the fuse wire has melted'], ['the lamp is undamaged']])}\n\nWhat most likely caused this?",
         correct="the current was too large",
         wrongs={"the bulb was loose": "A loose bulb breaks the circuit; it does not melt a fuse.", "the fuse rating was too high": "A fuse with too HIGH a rating would not melt.", "the voltage was too small": "A small voltage gives a small current, which cannot melt a fuse."},
         hints=["What makes a fuse melt?", "A current larger than its rating.", "Too large a current."],
         working=["Correct answer: **the current was too large**", SRC]),
    dict(id="e02w_resistance_order", level=4, lo="1.2h",
         stem=f"Four identical resistors are arranged in three circuits.\n\n{md_table(['circuit', 'arrangement'], [['E', 'all four in series'], ['F', 'all four in parallel'], ['G', 'two in series, in parallel with two in series']])}\n\nWhich list gives the circuits in order of effective resistance, largest to smallest?",
         correct="E, G, F",
         wrongs={"E, F, G": "F, with all four in parallel, has the SMALLEST resistance.", "F, G, E": "That is smallest to largest.", "F, E, G": "Series gives the largest resistance, so E is first."},
         hints=["Series adds resistance; parallel reduces it.", "All in series is largest; all in parallel is smallest.", "G is in between."],
         keypoints=[KP("E largest (series)", "e"), KP("F smallest (parallel)", "f")],
         working=["Correct answer: **E, G, F**", SRC]),
    dict(id="e02w_ammeter_wrongly_parallel", level=5, lo="1.2c",
         stem=f"A student connects an ammeter ACROSS a lamp instead of in series. The table shows what happens.\n\n{md_table(['observation'], [['the lamp does not light'], ['the ammeter reading is very large']])}\n\nExplain both observations.",
         correct="an ammeter has very low resistance, so the current takes the easy path through it instead of the lamp, and the very large current can damage the meter",
         wrongs={"the lamp is broken and the ammeter is measuring the voltage": "The lamp is bypassed, not broken; an ammeter measures current.", "the ammeter increases the resistance so no current reaches the lamp": "An ammeter has LOW resistance; it gives the current an easy path.", "the battery is flat": "A flat battery would give a small reading, not a large one."},
         hints=["An ammeter has almost no resistance.", "Where does the current go when it has an easy path?", "Around the lamp, through the meter."],
         keypoints=[KP("low resistance / easy path through ammeter", "low resistance", "easy path", "bypass", "short", "through the ammeter"), KP("lamp gets little current / large current damages meter", "lamp", "large current", "damage")],
         working=["Correct answer: **an ammeter has very low resistance, so the current takes the easy path through it instead of the lamp, and the very large current can damage the meter**", SRC]),
]

register_explain(EXPLAIN, chapter=2)
