"""Ch 2 Electricity (K123 topic 1.2): 20 calculation / data templates and 40 explanation items.
lo codes: 1.2a circuit diagrams and components, 1.2b series / parallel, 1.2c multimeter, 1.2d series current same,
1.2e parallel currents add, 1.2f series voltages add, 1.2g parallel voltage same, 1.2h series resistance increases,
1.2i parallel resistance decreases, 1.2j why household appliances are in parallel, 1.2k voltage and power ratings on labels,
1.2l power = current x voltage, 1.2m cost in kWh, 1.2n reading an electricity bill, 1.2o reducing electrical energy wastage."""
from .. import sketches as S, sketches_g1 as G1
from .base import fmt, md_table, nice, numeric_options, pick, register_explain, template, text_options

KP = lambda label, *phr: {"label": label, "any": list(phr)}

APPLIANCES = [("kettle", 2000), ("iron", 1200), ("hair dryer", 1500), ("television", 100), ("fan", 60), ("LED lamp", 10),
              ("rice cooker", 500), ("microwave oven", 800), ("air-conditioner", 1000), ("water heater", 3000)]


def money(x):
    return f"${x:,.2f}"


# ================================================================ CALCULATION / DATA
# ---------------------------------------------------------------- L1
@template("c02_series_current_same", chapter=2, level=1, lo="1.2d")
def series_current_same(rng):
    I = nice(rng, 0.2, 0.25, 0.3, 0.4, 0.5, 0.6)
    opts, key, mis = numeric_options(rng, I, [
        (I / 2, "In a SERIES circuit the current is the same everywhere; it is not shared between the lamps."),
        (I * 2, "The current does not add up around a series loop. It is the same at every point."),
        (I + 0.1, "The current is the same at every point in a series circuit."),
    ], unit="A", sf=2)
    return dict(
        stem=f"Fig. 1 shows two lamps and two ammeters connected in series. Ammeter A₁ reads **{fmt(I)} A**. What does ammeter A₂ read?",
        figure=S.circuit(["ammeter", "lamp", "lamp", "ammeter"], top=("cell",), labels=["A₁", "", "", "A₂"]),
        options=opts, key=key, misconceptions=mis,
        formula="in a series circuit the current is the same at every point",
        working=["series circuit → same current everywhere", f"A₂ = **{fmt(I)} A**"],
        hints=["Is there more than one path for the current?", "In a single loop, the charge that passes A₁ must also pass A₂.", "Same current at every point."],
    )


@template("c02_parallel_currents_add", chapter=2, level=1, lo="1.2e")
def parallel_currents_add(rng):
    I1 = nice(rng, 0.2, 0.3, 0.4, 0.5)
    I2 = nice(rng, 0.1, 0.2, 0.6, 0.8)
    tot = I1 + I2
    opts, key, mis = numeric_options(rng, tot, [
        (max(I1, I2), "The current through the battery is the SUM of the branch currents, not the larger one."),
        (abs(I1 - I2) or 0.05, "Add the branch currents; do not subtract."),
        (tot / 2, "Do not average: the branch currents add up."),
    ], unit="A", sf=2)
    return dict(
        stem=f"Fig. 1 shows two lamps in parallel. The current in lamp P is **{fmt(I1)} A** and in lamp Q is **{fmt(I2)} A**. What is the current through the battery?",
        figure=S.circuit([], parallel=[["lamp"], ["lamp"]], top=("battery",), labels=["P", "Q"]),
        options=opts, key=key, misconceptions=mis,
        formula="current through the power source = sum of the currents in the branches",
        working=[f"current from battery = {fmt(I1)} + {fmt(I2)}", f"= **{fmt(tot)} A**"],
        hints=["The current splits between the branches.", "What splits must add back up at the battery.", f"{fmt(I1)} + {fmt(I2)}."],
    )


@template("c02_series_voltages_add", chapter=2, level=1, lo="1.2f")
def series_voltages_add(rng):
    V1 = nice(rng, 1.5, 2.0, 2.5, 3.0)
    V2 = nice(rng, 1.0, 1.5, 3.0, 4.5)
    tot = V1 + V2
    opts, key, mis = numeric_options(rng, tot, [
        (max(V1, V2), "The battery voltage equals the SUM of the voltages across the components in series."),
        (abs(V1 - V2) or 0.5, "Add the two voltages; do not subtract."),
        (tot / 2, "Do not average: the voltages across series components add up."),
    ], unit="V", sf=2)
    return dict(
        stem=f"Fig. 1 shows two lamps in series. The voltage across lamp P is **{fmt(V1)} V** and across lamp Q is **{fmt(V2)} V**. What is the voltage across the battery?",
        figure=S.circuit(["lamp", "lamp"], top=("battery",), labels=["P", "Q"]),
        options=opts, key=key, misconceptions=mis,
        formula="voltage across the power source = sum of the voltages across the series components",
        working=[f"battery voltage = {fmt(V1)} + {fmt(V2)}", f"= **{fmt(tot)} V**"],
        hints=["The battery's voltage is shared between the lamps.", "Shared means the parts add up to the whole.", f"{fmt(V1)} + {fmt(V2)}."],
    )


@template("c02_power_iv", chapter=2, level=1, lo="1.2l")
def power_iv(rng):
    V = nice(rng, 12, 230, 240)
    I = nice(rng, 0.5, 2, 4, 5, 10) if V > 100 else nice(rng, 0.5, 1, 2)
    P = I * V
    opts, key, mis = numeric_options(rng, P, [
        (V / I, "You divided. Power = current × voltage."),
        (V + I, "You added. Power = current × voltage."),
        (I / V, "Upside down and the wrong operation: multiply current by voltage."),
    ], unit="W", sf=3)
    return dict(
        stem=f"An appliance works as shown.\n\n{md_table(['voltage / V', 'current / A'], [[V, I]])}\n\nWhat is its power?",
        options=opts, key=key, misconceptions=mis,
        formula="power = current × voltage   (W = A × V)",
        working=[f"power = {fmt(I)} A × {V} V", f"= **{fmt(P, sf=4)} W**"],
        hints=["Power is current times voltage.", "Multiply the two numbers.", f"{fmt(I)} × {V}."],
    )


# ---------------------------------------------------------------- L2
@template("c02_current_from_power", chapter=2, level=2, lo="1.2l")
def current_from_power(rng):
    name, P = pick(rng, APPLIANCES)
    V = 230
    I = P / V
    opts, key, mis = numeric_options(rng, I, [
        (P * V, "You multiplied. Current = power ÷ voltage."),
        (V / P, "Upside down: power ÷ voltage."),
        (P / 100, "The voltage is 230 V, not 100 V."),
    ], unit="A", sf=3)
    return dict(
        stem=f"The label on a {name} is shown.\n\n{md_table(['voltage', 'power'], [[f'{V} V', f'{P} W']])}\n\nWhat current does it draw?",
        options=opts, key=key, misconceptions=mis,
        formula="current = power ÷ voltage",
        working=[f"current = {P} ÷ {V}", f"= **{fmt(I)} A**"],
        hints=["Rearrange power = current × voltage.", "current = power ÷ voltage.", f"{P} ÷ {V}."],
    )


@template("c02_kwh_from_kw_hours", chapter=2, level=2, lo="1.2m")
def kwh_from_kw_hours(rng):
    name, P = pick(rng, [a for a in APPLIANCES if a[1] >= 500])
    h = nice(rng, 2, 3, 4, 5, 8)
    E = P / 1000 * h
    opts, key, mis = numeric_options(rng, E, [
        (P * h, "Change watts to kilowatts first: 1 kW = 1000 W."),
        (P / 1000 / h, "You divided. Energy in kWh = power in kW × time in hours."),
        (P / 100 * h, "1 kW = 1000 W, not 100 W."),
    ], unit="kWh", sf=3)
    return dict(
        stem=f"A {name} is used as shown.\n\n{md_table(['power rating', 'time used'], [[f'{P} W', f'{h} h']])}\n\nHow much energy does it use, in kWh?",
        options=opts, key=key, misconceptions=mis,
        formula="energy (kWh) = power (kW) × time (h);  1 kW = 1000 W",
        working=[f"{P} W = {P / 1000:g} kW", f"energy = {P / 1000:g} × {h} = **{fmt(E)} kWh**"],
        hints=["Change the power to kilowatts.", f"{P} W = {P / 1000:g} kW.", f"{P / 1000:g} × {h}."],
    )


@template("c02_cost_from_kwh", chapter=2, level=2, lo="1.2m")
def cost_from_kwh(rng):
    E = nice(rng, 5, 8, 12, 20, 30)
    rate = nice(rng, 0.25, 0.28, 0.30, 0.32)
    c = E * rate
    opts, key, mis = numeric_options(rng, c, [
        (E / rate, "You divided. Cost = number of kWh × price per kWh."),
        (E + rate, "You added. Multiply the units by the price of one unit."),
        (E * rate * 100, "The price is in dollars already; do not multiply by 100."),
    ], unit="$", sf=3, dp=2)
    return dict(
        stem=f"The table shows the electricity used and the price.\n\n{md_table(['energy used', 'price per kWh (1 unit)'], [[f'{E} kWh', money(rate)]])}\n\nWhat is the cost?",
        options=opts, key=key, misconceptions=mis,
        formula="cost = energy in kWh × price per kWh",
        working=[f"cost = {E} × {money(rate)}", f"= **{money(c)}**"],
        hints=["Each kWh is one 'unit' with a price.", "Units × price per unit.", f"{E} × {rate}."],
    )


@template("c02_series_missing_voltage", chapter=2, level=2, lo="1.2f")
def series_missing_voltage(rng):
    Vb = nice(rng, 6, 9, 12)
    V1 = nice(rng, 2, 3, 4, 5)
    V2 = Vb - V1
    opts, key, mis = numeric_options(rng, V2, [
        (Vb + V1, "The battery voltage is SHARED: subtract the known voltage from it."),
        (Vb, "The whole battery voltage is across both lamps together, not across Q alone."),
        (V1, "P and Q need not have the same voltage; use battery voltage − voltage across P."),
    ], unit="V", sf=2)
    return dict(
        stem=f"Fig. 1 shows two lamps P and Q in series with a **{Vb} V** battery. The voltage across P is **{V1} V**. What is the voltage across Q?",
        figure=S.circuit(["lamp", "lamp"], top=("battery",), voltmeter_across=0, labels=["P", "Q"]),
        options=opts, key=key, misconceptions=mis,
        formula="battery voltage = voltage across P + voltage across Q",
        working=[f"voltage across Q = {Vb} − {V1}", f"= **{fmt(V2)} V**"],
        hints=["The two voltages add up to the battery voltage.", "Subtract the known one.", f"{Vb} − {V1}."],
    )


# ---------------------------------------------------------------- L3
@template("c02_cost_minutes", chapter=2, level=3, lo="1.2m")
def cost_minutes(rng):
    name, P = pick(rng, [a for a in APPLIANCES if a[1] >= 800])
    m = nice(rng, 15, 30, 45)
    rate = nice(rng, 0.25, 0.30)
    E = P / 1000 * m / 60
    c = E * rate
    opts, key, mis = numeric_options(rng, c, [
        (P / 1000 * m * rate, "The time must be in HOURS: divide the minutes by 60."),
        (P * m / 60 * rate, "The power must be in kilowatts: divide the watts by 1000."),
        (E, "That is the energy in kWh; multiply by the price to get the cost."),
    ], unit="$", sf=3, dp=3)
    return dict(
        stem=f"A {name} is used as shown. Electricity costs {money(rate)} per kWh.\n\n{md_table(['power rating', 'time used'], [[f'{P} W', f'{m} min']])}\n\nWhat is the cost?",
        options=opts, key=key, misconceptions=mis,
        formula="energy (kWh) = power (kW) × time (h);  cost = kWh × price",
        working=[f"power = {P / 1000:g} kW;  time = {m}/60 = {m / 60:g} h", f"energy = {P / 1000:g} × {m / 60:g} = {fmt(E)} kWh", f"cost = {fmt(E)} × {money(rate)} = **{money(c)}**"],
        hints=["Convert W to kW and minutes to hours first.", f"{m} min = {m / 60:g} h.", f"{P / 1000:g} × {m / 60:g} × {rate}."],
    )


@template("c02_parallel_missing_branch", chapter=2, level=3, lo="1.2e")
def parallel_missing_branch(rng):
    tot = nice(rng, 1.0, 1.2, 1.5, 2.0)
    I1 = nice(rng, 0.3, 0.4, 0.5, 0.6)
    I2 = round(tot - I1, 2)
    opts, key, mis = numeric_options(rng, I2, [
        (tot + I1, "The branch currents ADD UP to the battery current, so subtract the known branch."),
        (tot, "The battery current is shared between the two branches."),
        (I1, "The two branches need not carry the same current; use total − known branch."),
    ], unit="A", sf=2)
    return dict(
        stem=f"Fig. 1 shows two lamps in parallel. The ammeter next to the battery reads **{fmt(tot)} A** and the current in lamp P is **{fmt(I1)} A**. What is the current in lamp Q?",
        figure=S.circuit(["ammeter"], parallel=[["lamp"], ["lamp"]], top=("battery",), labels=["P", "Q"]),
        options=opts, key=key, misconceptions=mis,
        formula="current through the battery = current in P + current in Q",
        working=[f"current in Q = {fmt(tot)} − {fmt(I1)}", f"= **{fmt(I2)} A**"],
        hints=["The battery current splits into the two branches.", "Known total, known branch: subtract.", f"{fmt(tot)} − {fmt(I1)}."],
    )


@template("c02_bill_units_used", chapter=2, level=3, lo="1.2n")
def bill_units_used(rng):
    prev = nice(rng, 12345, 20480, 30127, 45010)
    used = nice(rng, 180, 240, 310, 420)
    cur = prev + used
    rate = nice(rng, 0.25, 0.28, 0.30)
    opts, key, mis = numeric_options(rng, used, [
        (cur, "That is the meter reading, not the amount used. Subtract the previous reading."),
        (cur + prev, "Subtract the previous reading from the current one; do not add."),
        (used * rate, "That is the cost in dollars. The question asks for the number of units."),
    ], unit="kWh", sf=4)
    return dict(
        stem=f"Part of an electricity bill is shown.\n\n{md_table(['item', 'value'], [['previous meter reading', f'{prev} kWh'], ['current meter reading', f'{cur} kWh'], ['price per kWh', money(rate)]])}\n\nHow many units (kWh) were used in this period?",
        options=opts, key=key, misconceptions=mis,
        formula="units used = current meter reading − previous meter reading",
        working=[f"units used = {cur} − {prev}", f"= **{used} kWh**"],
        hints=["The meter counts kWh continuously.", "Usage this period = new reading − old reading.", f"{cur} − {prev}."],
    )


@template("c02_label_energy_table", chapter=2, level=3, lo="1.2k")
def label_energy_table(rng):
    name, P = pick(rng, [a for a in APPLIANCES if a[1] >= 500])
    V = 230
    h = nice(rng, 1, 2, 3)
    E = P / 1000 * h
    opts, key, mis = numeric_options(rng, E, [
        (V / 1000 * h, "Use the POWER rating (W), not the voltage, to find the energy."),
        (P * h, "Change W to kW: divide by 1000."),
        (P / 1000, "That is the power in kW; multiply by the hours."),
    ], unit="kWh", sf=3)
    return dict(
        stem=f"The rating label of a {name} is shown.\n\n{md_table(['Model', 'Voltage', 'Power', 'Frequency'], [['QT-200', f'{V} V', f'{P} W', '50 Hz']])}\n\nHow much energy does it use in **{h} h**?",
        options=opts, key=key, misconceptions=mis,
        formula="energy (kWh) = power (kW) × time (h)",
        working=[f"power rating = {P} W = {P / 1000:g} kW", f"energy = {P / 1000:g} × {h} = **{fmt(E)} kWh**"],
        hints=["Which number on the label is the power?", "Convert it to kW.", f"{P / 1000:g} × {h}."],
    )


# ---------------------------------------------------------------- L4
@template("c02_bill_cost", chapter=2, level=4, lo="1.2n")
def bill_cost(rng):
    prev = nice(rng, 15230, 28004, 41177)
    used = nice(rng, 200, 250, 300, 350)
    cur = prev + used
    rate = nice(rng, 0.25, 0.28, 0.30, 0.32)
    c = used * rate
    opts, key, mis = numeric_options(rng, c, [
        (cur * rate, "Use the units USED (current − previous), not the meter reading."),
        (used / rate, "Multiply units by price; do not divide."),
        (used * rate / 2, "The price applies to every unit used."),
    ], unit="$", sf=4, dp=2)
    return dict(
        stem=f"Part of an electricity bill is shown.\n\n{md_table(['item', 'value'], [['previous meter reading', f'{prev} kWh'], ['current meter reading', f'{cur} kWh'], ['price per kWh', money(rate)]])}\n\nWhat is the charge for the electricity used?",
        options=opts, key=key, misconceptions=mis,
        formula="units used = current − previous reading;  cost = units × price per kWh",
        working=[f"units used = {cur} − {prev} = {used} kWh", f"cost = {used} × {money(rate)} = **{money(c)}**"],
        hints=["First find the units used.", f"{cur} − {prev} = {used}.", f"{used} × {rate}."],
    )


@template("c02_bar_chart_monthly_kwh", chapter=2, level=4, lo="1.2o")
def bar_chart_monthly_kwh(rng):
    names = ["air-con", "fridge", "water heater", "lights"]
    vals = [nice(rng, 120, 150, 180), nice(rng, 40, 50, 60), nice(rng, 60, 80, 100), nice(rng, 10, 20, 30)]
    rate = nice(rng, 0.25, 0.30)
    tot = sum(vals)
    c = tot * rate
    opts, key, mis = numeric_options(rng, c, [
        (max(vals) * rate, "That is the cost of the largest bar only. Add all four."),
        (tot, "That is the total energy in kWh; multiply by the price."),
        (tot / rate, "Multiply by the price; do not divide."),
    ], unit="$", sf=4, dp=2)
    return dict(
        stem=f"Fig. 1 shows a household's electricity use in one month. Electricity costs {money(rate)} per kWh. What is the total cost for the month?",
        figure=S.bar_chart(names, vals, "energy used / kWh", ymax=200, ystep=50),
        options=opts, key=key, misconceptions=mis,
        formula="total cost = (sum of kWh) × price per kWh",
        working=[f"total energy = {' + '.join(map(str, vals))} = {tot} kWh", f"cost = {tot} × {money(rate)} = **{money(c)}**"],
        hints=["Read all four bars.", "Add them, then multiply by the price.", f"{tot} × {rate}."],
    )


@template("c02_compare_currents_labels", chapter=2, level=4, lo="1.2l")
def compare_currents_labels(rng):
    P1 = nice(rng, 1200, 1500, 2000)
    P2 = nice(rng, 60, 100, 500)
    I1, I2 = P1 / 230, P2 / 230
    ratio = I1 / I2
    opts, key, mis = numeric_options(rng, ratio, [
        (I2 / I1, "Upside down: the kettle's current divided by the other one's."),
        (P1 - P2, "Divide the currents (or the powers); do not subtract."),
        (ratio * 230, "Both run at 230 V, so the voltage cancels in the ratio."),
    ], unit="", sf=3)
    return dict(
        stem=f"Two appliances run on the 230 V mains.\n\n{md_table(['appliance', 'voltage / V', 'power / W'], [['kettle', 230, P1], ['television', 230, P2]])}\n\nHow many times larger is the current in the kettle than in the television?",
        options=opts, key=key, misconceptions=mis,
        formula="current = power ÷ voltage; at the same voltage the current is proportional to the power",
        working=[f"kettle: {P1} ÷ 230 = {fmt(I1)} A;  television: {P2} ÷ 230 = {fmt(I2)} A", f"ratio = {fmt(I1)} ÷ {fmt(I2)} = **{fmt(ratio)}**"],
        hints=["Work out each current with current = power ÷ voltage.", "Then divide the larger by the smaller.", f"{fmt(I1)} ÷ {fmt(I2)}."],
    )


@template("c02_led_saving_month", chapter=2, level=4, lo="1.2o")
def led_saving_month(rng):
    Pf = nice(rng, 40, 60, 100)
    Pl = nice(rng, 5, 8, 10)
    h = nice(rng, 4, 5, 6)
    days = 30
    rate = nice(rng, 0.25, 0.30)
    saved_kwh = (Pf - Pl) / 1000 * h * days
    c = saved_kwh * rate
    opts, key, mis = numeric_options(rng, c, [
        (Pf / 1000 * h * days * rate, "That is the whole cost of the filament lamp. The SAVING is the difference between the lamps."),
        ((Pf - Pl) / 1000 * h * rate, "That is the saving for ONE day; the question asks for 30 days."),
        ((Pf - Pl) * h * days * rate, "Change watts to kilowatts first."),
    ], unit="$", sf=3, dp=2)
    return dict(
        stem=f"A filament lamp is replaced by an LED lamp of the same brightness. Each is used {h} h a day for {days} days. Electricity costs {money(rate)} per kWh.\n\n{md_table(['lamp', 'power / W'], [['filament', Pf], ['LED', Pl]])}\n\nHow much money is saved in the {days} days?",
        options=opts, key=key, misconceptions=mis,
        formula="saving = (difference in power, kW) × hours × price",
        working=[f"difference = {Pf} − {Pl} = {Pf - Pl} W = {(Pf - Pl) / 1000:g} kW", f"energy saved = {(Pf - Pl) / 1000:g} × {h} × {days} = {fmt(saved_kwh)} kWh", f"money saved = {fmt(saved_kwh)} × {money(rate)} = **{money(c)}**"],
        hints=["Find the power difference in kW.", f"Hours in {days} days = {h * days}.", f"{(Pf - Pl) / 1000:g} × {h * days} × {rate}."],
    )


# ---------------------------------------------------------------- L5
@template("c02_month_cost_several", chapter=2, level=5, lo="1.2m")
def month_cost_several(rng):
    rows = [["air-conditioner", 1000, nice(rng, 4, 6, 8)], ["water heater", 3000, nice(rng, 0.5, 1)], ["television", 100, nice(rng, 3, 5)]]
    rate = nice(rng, 0.25, 0.30)
    days = 30
    kwh_day = sum(P / 1000 * h for _, P, h in rows)
    c = kwh_day * days * rate
    opts, key, mis = numeric_options(rng, c, [
        (kwh_day * rate, "That is one day's cost; multiply by 30 days."),
        (rows[0][1] / 1000 * rows[0][2] * days * rate, "That is the air-conditioner only. Add all three appliances."),
        (kwh_day * days, "That is the energy in kWh; multiply by the price."),
    ], unit="$", sf=4, dp=2)
    return dict(
        stem=f"The table shows a family's daily use of three appliances. Electricity costs {money(rate)} per kWh.\n\n{md_table(['appliance', 'power / W', 'hours used each day'], rows)}\n\nWhat is the cost for **{days} days**?",
        options=opts, key=key, misconceptions=mis,
        formula="energy (kWh) = power (kW) × hours;  add the appliances;  cost = kWh × price",
        working=[f"per day: " + " + ".join(f"{P / 1000:g} × {h}" for _, P, h in rows) + f" = {fmt(kwh_day)} kWh", f"{days} days: {fmt(kwh_day)} × {days} = {fmt(kwh_day * days)} kWh", f"cost = {fmt(kwh_day * days)} × {money(rate)} = **{money(c)}**"],
        hints=["Work out each appliance's kWh per day and add.", f"Daily total = {fmt(kwh_day)} kWh.", f"{fmt(kwh_day)} × {days} × {rate}."],
    )


@template("c02_series_add_lamps_data", chapter=2, level=5, lo="1.2h")
def series_add_lamps_data(rng):
    I1 = nice(rng, 0.6, 0.9, 1.2)
    rows = [[1, fmt(I1)], [2, fmt(I1 / 2)], [3, fmt(I1 / 3)]]
    ans = f"about {fmt(I1 / 4)} A, because each extra lamp in series increases the effective resistance"
    opts, key, mis = text_options(rng, ans, {
        f"about {fmt(I1)} A, because the current in a series circuit is always the same": "The current is the same at every point in ONE circuit, but adding a lamp makes a NEW circuit with more resistance and a smaller current.",
        f"about {fmt(I1 / 3)} A, because the current cannot fall any further": "The pattern continues: more lamps, more resistance, less current.",
        f"about {fmt(I1 * 4)} A, because more lamps draw more current": "More lamps in SERIES means more resistance and LESS current.",
    })
    return dict(
        stem=f"A student adds identical lamps one at a time in series with a battery and records the current.\n\n{md_table(['number of lamps in series', 'current / A'], rows)}\n\nWhat current is expected with 4 lamps, and why?",
        options=opts, key=key, misconceptions=mis,
        formula="effective resistance increases as more resistors (lamps) are connected in series, so the current falls",
        working=["1 lamp → 2 lamps → 3 lamps: the current falls to 1/2, then 1/3", f"with 4 lamps: {fmt(I1)} ÷ 4 = **about {fmt(I1 / 4)} A** (more resistance in series)"],
        hints=["Look at the pattern in the current column.", "Each extra lamp adds resistance.", f"{fmt(I1)} ÷ 4."],
    )


@template("c02_power_then_cost", chapter=2, level=5, lo="1.2l")
def power_then_cost(rng):
    I = nice(rng, 4, 5, 8, 10)
    V = 230
    h = nice(rng, 1, 2, 3)
    rate = nice(rng, 0.25, 0.30)
    P = I * V
    E = P / 1000 * h
    c = E * rate
    opts, key, mis = numeric_options(rng, c, [
        (P * h * rate, "Change the power to kilowatts before finding kWh."),
        (E, "That is the energy in kWh; multiply by the price for the cost."),
        (I * h * rate, "First find the power: current × voltage."),
    ], unit="$", sf=3, dp=2)
    return dict(
        stem=f"A heater draws a current of **{I} A** from the **{V} V** mains for **{h} h**. Electricity costs {money(rate)} per kWh.\n\n{md_table(['current / A', 'voltage / V', 'time / h'], [[I, V, h]])}\n\nWhat is the cost?",
        options=opts, key=key, misconceptions=mis,
        formula="power = current × voltage;  energy (kWh) = kW × h;  cost = kWh × price",
        working=[f"power = {I} × {V} = {P} W = {P / 1000:g} kW", f"energy = {P / 1000:g} × {h} = {fmt(E)} kWh", f"cost = {fmt(E)} × {money(rate)} = **{money(c)}**"],
        hints=["Three steps: power, then kWh, then cost.", f"Power = {P} W = {P / 1000:g} kW.", f"{P / 1000:g} × {h} × {rate}."],
    )


@template("c02_parallel_add_lamps_data", chapter=2, level=5, lo="1.2i")
def parallel_add_lamps_data(rng):
    I1 = nice(rng, 0.3, 0.4, 0.5)
    rows = [[1, fmt(I1)], [2, fmt(2 * I1)], [3, fmt(3 * I1)]]
    ans = f"{fmt(4 * I1)} A, because adding branches in parallel lowers the effective resistance"
    opts, key, mis = text_options(rng, ans, {
        f"{fmt(I1)} A, because each lamp gets the same voltage": "Each lamp does get the full voltage, which is WHY each extra lamp adds another {0} A to the battery current.".format(fmt(I1)),
        f"{fmt(3 * I1)} A, because the battery current cannot keep rising": "Each added branch adds its own current; the total keeps rising.",
        f"{fmt(I1 / 4)} A, because more lamps increase the resistance": "In PARALLEL, more lamps LOWER the effective resistance, so the battery current rises.",
    })
    return dict(
        stem=f"A student adds identical lamps one at a time in parallel across a battery and records the battery current.\n\n{md_table(['number of lamps in parallel', 'battery current / A'], rows)}\n\nWhat current is expected with 4 lamps, and why?",
        options=opts, key=key, misconceptions=mis,
        formula="effective resistance decreases as more resistors (lamps) are connected in parallel, so the battery current rises",
        working=[f"each parallel lamp adds {fmt(I1)} A to the battery current", f"with 4 lamps: 4 × {fmt(I1)} = **{fmt(4 * I1)} A** (less effective resistance)"],
        hints=["Look at the pattern in the current column.", "Each new branch adds another path for current.", f"4 × {fmt(I1)}."],
    )


# ================================================================ EXPLANATION
T_SYM = md_table(["component", "what it does"], [["cell", "pushes current round the circuit"], ["switch", "opens or closes the circuit"], ["lamp", "gives out light"], ["fixed resistor", "limits the current"], ["variable resistor", "changes the current"], ["bell", "rings"], ["fuse", "melts and breaks the circuit if the current is too large"], ["ammeter", "measures current"], ["voltmeter", "measures voltage"]])

EXPLAIN = [
    # ------------------------------------------------------------ L1
    dict(id="e02_ammeter_measures", level=1, lo="1.2a",
         stem=f"The table lists circuit components.\n\n{T_SYM}\n\nWhich component measures the current in a circuit?",
         correct="ammeter",
         wrongs={"voltmeter": "A voltmeter measures the voltage across a component.", "fuse": "A fuse protects the circuit; it does not measure anything.", "variable resistor": "A variable resistor changes the current; it does not measure it."},
         hints=["Current is measured in amperes.", "The meter's name comes from the unit.", "Ammeter."]),
    dict(id="e02_component_vary_current", level=1, lo="1.2a",
         stem=f"The table lists circuit components.\n\n{T_SYM}\n\nWhich component is used to vary the current in a circuit, for example to dim a lamp?",
         correct="variable resistor",
         wrongs={"switch": "A switch only turns the current fully on or off.", "fuse": "A fuse breaks the circuit when the current is too large.", "ammeter": "An ammeter measures the current; it does not change it."},
         hints=["Its resistance can be changed by sliding or turning a knob.", "More resistance → less current.", "Variable resistor."]),
    dict(id="e02_fuse_purpose", level=1, lo="1.2a",
         stem=f"The table lists circuit components.\n\n{T_SYM}\n\nWhat is the purpose of a fuse?",
         correct="to melt and break the circuit if the current becomes too large",
         wrongs={"to measure the current": "That is the ammeter's job.", "to make the current larger": "A fuse does not change the normal current.", "to switch the circuit on and off": "That is the switch's job."},
         hints=["It protects the appliance and the wires.", "A thin wire inside it melts.", "Breaks the circuit when the current is too large."]),
    dict(id="e02_series_identify", level=1, lo="1.2b",
         stem="Fig. 1 shows a circuit with two lamps. How are the lamps connected?",
         fig=lambda rng: S.circuit(["lamp", "lamp"], top=("cell",)),
         correct="in series, because there is only one path for the current",
         wrongs={"in parallel, because there are two lamps": "The number of lamps does not decide it; the number of PATHS does.", "in parallel, because they share one cell": "Series lamps also share one cell.", "in series, because they are the same size": "Size has nothing to do with it; the single loop does."},
         hints=["Trace the current from the cell and back.", "How many separate paths are there?", "One path → series."]),
    dict(id="e02_parallel_identify", level=1, lo="1.2b",
         stem="Fig. 1 shows a circuit with two lamps. How are the lamps connected?",
         fig=lambda rng: S.circuit([], parallel=[["lamp"], ["lamp"]], top=("cell",)),
         correct="in parallel, because the current has two separate paths",
         wrongs={"in series, because there is one cell": "Parallel circuits can also have one cell.", "in series, because the lamps are the same": "Identical lamps can be in series or in parallel.", "in parallel, because the wires are longer": "Wire length does not decide it; the branching does."},
         hints=["Trace the current from the cell.", "Does it split into more than one path?", "Two paths → parallel."]),
    dict(id="e02_multimeter_use", level=1, lo="1.2c",
         stem=f"The table shows the settings on a multimeter.\n\n{md_table(['setting', 'symbol'], [['voltage', 'V'], ['current', 'A'], ['resistance', 'Ω']])}\n\nA student wants to measure the resistance of a resistor. Which setting should be selected?",
         correct="Ω",
         wrongs={"V": "V measures voltage.", "A": "A measures current.", "any setting, because a multimeter measures everything at once": "A multimeter measures one quantity at a time; the dial must be set to it."},
         hints=["Resistance is measured in ohms.", "The symbol is a Greek letter.", "A capital omega."]),
    dict(id="e02_series_current_rule", level=1, lo="1.2d",
         stem=f"The table shows ammeter readings taken at three points in a series circuit.\n\n{md_table(['point', 'current / A'], [['next to the cell', 0.4], ['between the lamps', 0.4], ['after the last lamp', 0.4]])}\n\nWhat do the readings show?",
         correct="the current is the same at every point in a series circuit",
         wrongs={"the current is used up by the lamps": "If current were used up, the readings would fall around the circuit. They do not.", "the current gets larger after each lamp": "All three readings are equal.", "the ammeters are faulty": "Equal readings are exactly what a series circuit gives."},
         hints=["Compare the three readings.", "They are all equal.", "Same current at every point."]),
    dict(id="e02_household_parallel_fact", level=1, lo="1.2j",
         stem=f"The table shows what happens in two homes when one lamp blows.\n\n{md_table(['home', 'wiring', 'what happens to the other lamps'], [['P', 'series', 'all go out'], ['Q', 'parallel', 'stay on']])}\n\nHow are the lamps in a house wired, and why?",
         correct="in parallel, so that each lamp works independently",
         wrongs={"in series, so that less wire is needed": "In series one broken lamp would switch off all the others.", "in series, so that the lamps are brighter": "Series lamps share the voltage and are DIMMER.", "in parallel, so that all the lamps use less energy": "Parallel wiring is about independence and full voltage, not saving energy."},
         hints=["Look at home Q.", "One lamp blowing does not affect the others.", "Parallel."]),

    # ------------------------------------------------------------ L2
    dict(id="e02_parallel_voltage_same", level=2, lo="1.2g",
         stem="Fig. 1 shows two lamps P and Q in parallel with a 6 V battery. A voltmeter across P reads 6 V. What does a voltmeter across Q read?",
         fig=lambda rng: S.circuit([], parallel=[["lamp"], ["lamp"]], top=("battery",), labels=["P", "Q"]),
         correct="6 V, because the voltage is the same across each parallel branch",
         wrongs={"3 V, because the battery voltage is shared": "Voltages are SHARED in series; in parallel each branch gets the full battery voltage.", "0 V, because all the voltage is used by P": "Voltage is not used up by one branch.", "12 V, because the branches add up": "The voltage across each branch is equal to the battery voltage; nothing adds."},
         hints=["Each branch is connected straight across the battery.", "So each branch gets the full battery voltage.", "6 V."]),
    dict(id="e02_series_voltage_share", level=2, lo="1.2f",
         stem="Fig. 1 shows two identical lamps P and Q in series with a 6 V battery. What is the voltage across lamp P?",
         fig=lambda rng: S.circuit(["lamp", "lamp"], top=("battery",), labels=["P", "Q"]),
         correct="3 V, because the battery voltage is shared equally between the two identical lamps",
         wrongs={"6 V, because each lamp gets the battery voltage": "That is true in PARALLEL. In series the voltages add up to 6 V.", "12 V, because the two lamps add up": "The two voltages add up to the battery voltage, 6 V.", "0 V, because series lamps have no voltage": "Each lamp has a share of the battery voltage."},
         hints=["In series, the voltages across the components add up to the battery voltage.", "Two identical lamps share it equally.", "6 ÷ 2."]),
    dict(id="e02_which_circuit_brighter", level=2, lo="1.2b",
         stem=f"Two circuits each use one cell and two identical lamps.\n\n{md_table(['circuit', 'connection', 'voltage across each lamp'], [['X', 'series', '0.75 V'], ['Y', 'parallel', '1.5 V']])}\n\nIn which circuit are the lamps brighter, and why?",
         correct="Y, because each lamp gets the full cell voltage",
         wrongs={"X, because series lamps share the current": "Series lamps SHARE the voltage, so they are dimmer.", "X, because there is only one path": "One path means the lamps share the voltage.", "both the same, because the lamps are identical": "The voltage across each lamp is different, so the brightness differs."},
         hints=["Compare the voltage across each lamp.", "A higher voltage across a lamp makes it brighter.", "Y."]),
    dict(id="e02_label_reading", level=2, lo="1.2k",
         stem=f"The label on an appliance is shown.\n\n{md_table(['Model', 'Voltage', 'Power', 'Frequency'], [['KX-10', '230 V', '1500 W', '50 Hz']])}\n\nWhich two values are the voltage rating and the power rating?",
         correct="230 V and 1500 W",
         wrongs={"50 Hz and 1500 W": "50 Hz is the mains frequency, not the voltage rating.", "230 V and 50 Hz": "50 Hz is the frequency; the power rating is in watts.", "KX-10 and 230 V": "KX-10 is the model number."},
         hints=["Voltage is measured in volts.", "Power is measured in watts.", "Look for the V and the W."]),
    dict(id="e02_bill_item", level=2, lo="1.2n",
         stem=f"Part of an electricity bill is shown.\n\n{md_table(['item', 'value'], [['previous reading', '20 480 kWh'], ['current reading', '20 790 kWh'], ['usage', '310 kWh'], ['rate', '$0.30 per kWh']])}\n\nWhat does the 'usage' line show?",
         correct="the number of units of electricity used since the last bill",
         wrongs={"the total electricity ever used in the home": "That is closer to the meter reading, not the usage for the period.", "the cost of the electricity": "Cost is usage × rate; the usage line is in kWh.", "the power of the appliances": "Power is in watts; usage is energy in kWh."},
         hints=["Usage = current reading − previous reading.", "20 790 − 20 480 = 310.", "Units used this period."]),
    dict(id="e02_save_energy_way", level=2, lo="1.2o",
         stem=f"The table lists actions in a home.\n\n{md_table(['action'], [['leave the television on standby all night'], ['set the air-conditioner to 18 °C'], ['switch off lights when leaving a room'], ['boil a full kettle for one cup of tea']])}\n\nWhich action reduces electrical energy wastage?",
         correct="switch off lights when leaving a room",
         wrongs={"leave the television on standby all night": "Standby still uses energy.", "set the air-conditioner to 18 °C": "A very low setting uses MORE energy; 25 °C is recommended.", "boil a full kettle for one cup of tea": "Heating water you do not use wastes energy."},
         hints=["Which action means less electricity is used for nothing?", "Lights nobody is using waste energy.", "Switch them off."]),
    dict(id="e02_multimeter_as_ammeter", level=2, lo="1.2c",
         stem="Fig. 1 shows a multimeter reading. A student connected the multimeter in series with a lamp to measure the current. Which reading and setting are correct?",
         fig=lambda rng: G1.multimeter("0.25", "A"),
         correct="0.25 A on the current (A) setting, connected in series",
         wrongs={"0.25 V on the voltage setting, connected in series": "To measure current the dial must be on A, and the display shows A.", "0.25 A on the current setting, connected across the lamp": "An ammeter goes IN SERIES, in the path of the current.", "0.25 Ω on the resistance setting": "The display shows A, the unit of current."},
         hints=["Read the unit on the display.", "A is for amperes, the unit of current.", "In series."]),
    dict(id="e02_series_resistance_more", level=2, lo="1.2h",
         stem=f"The table shows what happens as resistors are added one at a time to a series circuit.\n\n{md_table(['resistors in series', 'effective resistance / Ω'], [[1, 10], [2, 20], [3, 30]])}\n\nWhat happens to the effective resistance as more resistors are added in series?",
         correct="it increases",
         wrongs={"it decreases": "The table shows the resistance rising: 10, 20, 30.", "it stays the same": "The values change.", "it increases then decreases": "It keeps increasing."},
         hints=["Read the second column downwards.", "10 → 20 → 30.", "It goes up."]),

    # ------------------------------------------------------------ L3
    dict(id="e02_why_parallel_independent", level=3, lo="1.2j",
         stem="Fig. 1 shows the lamps in a kitchen. Lamp P blows. Explain why lamp Q keeps working.",
         fig=lambda rng: S.circuit([], parallel=[["lamp"], ["lamp"]], top=("battery", "switch_closed"), labels=["P", "Q"]),
         correct="the lamps are in parallel, so Q still has its own complete path to the supply",
         wrongs={"the lamps are in series, so the current goes round P": "In series a blown lamp breaks the only path and everything goes off.", "Q stores enough energy to keep working": "Lamps do not store energy.", "the switch sends the current to Q instead": "The switch is not involved; Q has its own branch."},
         hints=["Trace the path through Q only.", "Does it pass through P?", "No: Q has its own branch."],
         keypoints=[KP("parallel", "parallel", "own branch", "separate branch", "two paths"), KP("Q still has a complete path", "complete", "path", "loop", "circuit", "still flows", "still connected")]),
    dict(id="e02_parallel_full_voltage", level=3, lo="1.2j",
         stem=f"The table compares two ways of wiring three lamps to a 230 V supply.\n\n{md_table(['wiring', 'voltage across each lamp', 'brightness'], [['series', '77 V', 'dim'], ['parallel', '230 V', 'normal']])}\n\nWhy are household appliances connected in parallel rather than in series?",
         correct="each appliance gets the full mains voltage and can be switched on and off on its own",
         wrongs={"parallel wiring uses less electricity": "Parallel appliances each use their normal power; the advantage is full voltage and independence.", "series wiring is more dangerous": "The problem with series is that appliances share the voltage and all switch off together.", "parallel wiring needs fewer wires": "It usually needs more wire, not less."},
         hints=["Compare the voltage column.", "What happens in series if one appliance is switched off?", "Full voltage and independent switching."],
         keypoints=[KP("full / same voltage for each", "full voltage", "same voltage", "230", "whole voltage", "mains voltage"), KP("work independently / switched separately", "independent", "separately", "on its own", "own switch", "others still work", "not affect")]),
    dict(id="e02_series_vs_parallel_meter", level=3, lo="1.2c",
         stem=f"A student uses two multimeters to find the power of a lamp.\n\n{md_table(['multimeter', 'set to', 'connected'], [['P', 'A', 'in series with the lamp'], ['Q', 'V', 'across the lamp']])}\n\nWhich statement is correct?",
         correct="P measures the current through the lamp and Q the voltage across it, so power = reading of P × reading of Q",
         wrongs={"P and Q should both be across the lamp": "An ammeter must be IN SERIES so the current flows through it.", "P measures the voltage because it is in series": "P is set to A: it measures current.", "the power is reading of Q ÷ reading of P": "Power = current × voltage, a product not a quotient."},
         hints=["Which setting measures current?", "Power = current × voltage.", "Multiply the two readings."],
         keypoints=[KP("P current, Q voltage", "current", "voltage"), KP("multiply", "multiply", "times", "product", "reading of", "readings")]),
    dict(id="e02_fuse_rating_choice", level=3, lo="1.2k",
         stem=f"The table shows the label on a kettle and the fuses available.\n\n{md_table(['kettle', 'fuses available'], [['230 V, 2000 W', '3 A, 5 A, 13 A']])}\n\nThe kettle draws about 8.7 A. Which fuse should be fitted, and why?",
         correct="13 A, the smallest fuse rated above the normal current",
         wrongs={"3 A, because a small fuse is safest": "A 3 A fuse would melt as soon as the kettle was switched on.", "5 A, because it is close to 8.7 A": "5 A is BELOW the working current, so it would melt in normal use.", "13 A, because a bigger fuse lets more current through": "The fuse is chosen to be just above the normal current, not as big as possible."},
         hints=["Current = power ÷ voltage = 2000 ÷ 230 ≈ 8.7 A.", "The fuse must not melt in normal use.", "The smallest fuse above 8.7 A."],
         keypoints=[KP("13 A", "13"), KP("just above the normal current", "above", "higher than", "more than", "greater than", "exceed", "normal current", "8.7")]),
    dict(id="e02_lamp_brightness_series_three", level=3, lo="1.2h",
         stem=f"A student adds identical lamps in series.\n\n{md_table(['lamps in series', 'brightness of each lamp'], [[1, 'bright'], [2, 'dimmer'], [3, 'very dim']])}\n\nWhy do the lamps get dimmer?",
         correct="more lamps in series means more resistance, so the current is smaller",
         wrongs={"the cell runs out of energy faster": "The dimming happens immediately, not because the cell is used up.", "each lamp uses up some current": "Current is not used up; it is the same everywhere in the loop, but smaller.", "the lamps are further from the cell": "Distance from the cell makes no difference."},
         hints=["What does each extra lamp add to the circuit?", "More resistance → ?", "Less current, dimmer lamps."],
         keypoints=[KP("more resistance", "resistance"), KP("smaller current", "current", "less current", "smaller", "lower", "decrease")]),
    dict(id="e02_cost_saving_explain", level=3, lo="1.2o",
         stem=f"The table shows two air-conditioner settings.\n\n{md_table(['setting', 'energy used per night / kWh'], [['18 °C', 9.0], ['25 °C', 6.0]])}\n\nWhy does the 25 °C setting reduce the electricity bill?",
         correct="it uses less energy each night, so fewer kWh are paid for",
         wrongs={"it makes the air-conditioner more powerful": "Power is not shown; it uses LESS energy.", "the price per kWh is lower at 25 °C": "The price per kWh is fixed by the supplier, not by the setting.", "it does not use any electricity": "It still uses 6.0 kWh a night."},
         hints=["Compare the kWh.", "Cost = kWh × price.", "Fewer kWh → lower cost."],
         keypoints=[KP("uses less energy / fewer kWh", "less energy", "fewer", "less electricity", "6", "3 kwh", "lower energy"), KP("cost depends on kWh", "cost", "bill", "pay", "paid", "cheaper", "price")]),
    dict(id="e02_switch_position", level=3, lo="1.2a",
         stem="Fig. 1 shows a circuit. The switch is open. What happens, and why?",
         fig=lambda rng: S.circuit(["lamp"], top=("cell", "switch_open")),
         correct="the lamp is off, because the open switch breaks the circuit so no current flows",
         wrongs={"the lamp is on, because the cell is connected": "A complete loop is needed; an open switch leaves a gap.", "the lamp is dim, because only some current gets across the gap": "No current crosses the gap in an open switch.", "the lamp is on, because the switch is only for safety": "A switch controls whether the circuit is complete."},
         hints=["Is the circuit a complete loop?", "What does an open switch do to the loop?", "Breaks it: no current."],
         keypoints=[KP("circuit broken / incomplete", "break", "broken", "incomplete", "gap", "open", "not complete"), KP("no current flows", "no current", "current cannot", "does not flow", "stops")]),
    dict(id="e02_bill_higher_month", level=3, lo="1.2n",
         stem=f"The table shows two months from a family's electricity bills.\n\n{md_table(['month', 'units used / kWh', 'price per kWh', 'cost'], [['May', 350, '$0.30', '$105.00'], ['June', 420, '$0.30', '$126.00']])}\n\nWhy was the June bill higher?",
         correct="more units were used in June at the same price per unit",
         wrongs={"the price per unit went up in June": "The price is $0.30 in both months.", "the meter was read wrongly in June": "There is no evidence of that; the usage simply rose.", "the family used more appliances at a lower price": "The price did not change."},
         hints=["Compare the two rows.", "Which value changed?", "The units used."],
         keypoints=[KP("more units / kWh used", "more units", "more kwh", "more energy", "420", "used more", "higher usage"), KP("same price", "same price", "same rate", "price did not", "unchanged", "0.30")]),

    # ------------------------------------------------------------ L4
    dict(id="e02_parallel_data_voltage", level=4, lo="1.2g",
         stem=f"A student measures three different lamps connected in parallel to a 6 V battery.\n\n{md_table(['lamp', 'current / A', 'voltage / V'], [['P', 0.2, 6], ['Q', 0.5, 6], ['R', 0.3, 6]])}\n\nWhich conclusion do the data support?",
         correct="each branch has the same voltage as the battery, but the currents differ because the lamps differ",
         wrongs={"the voltage is shared between the lamps": "Every lamp has the full 6 V; sharing happens in series.", "the current is the same in every branch": "The currents are 0.2, 0.5 and 0.3 A.", "the battery supplies 0.5 A in total": "The battery current is the SUM, 1.0 A."},
         hints=["Compare the voltage column, then the current column.", "Same voltage, different currents.", "Parallel branches share the voltage equally but not the current."],
         keypoints=[KP("same voltage across each branch", "same voltage", "6 v", "equal voltage", "full voltage"), KP("currents differ / add up", "different current", "currents differ", "add", "sum", "1.0")]),
    dict(id="e02_fault_finding_ammeter", level=4, lo="1.2d",
         stem=f"Three ammeters P, Q and R are placed at different points in one series circuit.\n\n{md_table(['ammeter', 'reading / A'], [['P', 0.30], ['Q', 0.30], ['R', 0.15]])}\n\nWhat can be concluded?",
         correct="ammeter R is faulty, because the current must be the same at every point in a series circuit",
         wrongs={"the current is used up before it reaches R": "Current is not used up; all three readings should be equal.", "R is after a lamp that halves the current": "A lamp does not halve the current in a series loop.", "the readings are all correct for a series circuit": "Equal readings are expected; 0.15 A is wrong."},
         hints=["What rule applies to current in a series circuit?", "Which reading breaks the rule?", "R should also read 0.30 A."],
         keypoints=[KP("current should be the same everywhere", "same", "equal", "every point", "everywhere"), KP("R is wrong / faulty", "r", "faulty", "wrong", "broken", "error")]),
    dict(id="e02_standby_data", level=4, lo="1.2o",
         stem=f"The table shows the power of a television in two states.\n\n{md_table(['state', 'power / W', 'hours per day'], [['on', 100, 4], ['standby', 5, 20]])}\n\nWhich statement is a correct evaluation of switching off at the wall instead of leaving the set on standby?",
         correct="standby uses 0.1 kWh a day, about 3 kWh a month, so switching off at the wall saves a small but real amount",
         wrongs={"standby uses no energy, so there is nothing to save": "5 W for 20 h is 0.1 kWh every day.", "standby uses more energy than watching, so it is the main waste": "Watching uses 0.4 kWh a day, more than standby's 0.1 kWh.", "switching off at the wall uses more energy because of restarting": "Restarting uses a negligible amount."},
         hints=["Energy = power (kW) × hours.", "Standby: 0.005 kW × 20 h.", "0.1 kWh a day, 3 kWh a month."],
         keypoints=[KP("standby still uses energy", "standby", "still uses", "0.1", "5 w", "uses energy"), KP("small saving over time", "save", "saving", "month", "3 kwh", "adds up")]),
    dict(id="e02_two_appliances_current_reason", level=4, lo="1.2l",
         stem=f"Two appliances are plugged into the same 230 V supply.\n\n{md_table(['appliance', 'power / W', 'current / A'], [['toaster', 920, 4.0], ['phone charger', 23, 0.1]])}\n\nWhy does the toaster draw a much larger current?",
         correct="at the same voltage, current = power ÷ voltage, so the higher power needs a larger current",
         wrongs={"the toaster uses a higher voltage": "Both use 230 V.", "the toaster has thicker wires, so more current fits": "Thicker wires are a RESULT of the larger current, not the cause.", "the charger is further from the socket": "Distance does not matter."},
         hints=["Both appliances have the same voltage.", "Rearrange power = current × voltage.", "More power → more current."],
         keypoints=[KP("same voltage", "same voltage", "230", "voltage is the same", "both 230"), KP("higher power needs more current", "power", "more current", "larger current", "bigger current")]),
    dict(id="e02_label_mismatch", level=4, lo="1.2k",
         stem=f"A traveller brings a hair dryer to Singapore, where the mains is 230 V.\n\n{md_table(['label on hair dryer'], [['110 V, 1200 W']])}\n\nWhat would happen if it were plugged straight into a 230 V socket, and what should be done?",
         correct="the voltage is too high for it, so it could overheat or be damaged; a step-down transformer should be used",
         wrongs={"it would work normally, because the power rating matches": "The VOLTAGE rating must match the supply.", "it would work but be dim, because the voltage is too low": "230 V is HIGHER than 110 V.", "a step-up transformer should be used": "The voltage must be stepped DOWN from 230 V to 110 V."},
         hints=["Compare the voltage rating with the supply.", "Too much voltage drives too much current.", "Step the voltage down."],
         keypoints=[KP("voltage too high / damage", "too high", "damage", "overheat", "burn", "blow", "higher voltage"), KP("step-down transformer", "step-down", "step down", "transformer", "reduce the voltage", "lower the voltage")]),
    dict(id="e02_parallel_resistance_data", level=4, lo="1.2i",
         stem=f"A student measures the battery current as resistors are added in parallel.\n\n{md_table(['resistors in parallel', 'battery current / A', 'effective resistance / Ω'], [[1, 0.6, 10], [2, 1.2, 5], [3, 1.8, 3.3]])}\n\nWhich statement explains the data?",
         correct="each added branch gives the current another path, so the effective resistance falls and the battery current rises",
         wrongs={"adding resistors always increases resistance": "That is true in SERIES; in parallel the effective resistance falls.", "the battery voltage rises with each resistor": "The battery voltage stays the same.", "the current is shared, so each resistor gets less": "Each resistor still gets the full voltage and its own full current; the battery supplies the sum."},
         hints=["Read the resistance column downwards.", "More paths for current → ?", "Lower effective resistance."],
         keypoints=[KP("more paths for current", "path", "branch", "route"), KP("effective resistance decreases", "resistance", "decrease", "falls", "lower", "less")]),
    dict(id="e02_bulb_blows_series_q", level=4, lo="1.2b",
         stem="Fig. 1 shows three lamps P, Q and R. P is in series with the supply; Q and R are in parallel with each other. P blows. What happens to Q and R, and why?",
         fig=lambda rng: S.circuit(["lamp"], parallel=[["lamp"], ["lamp"]], top=("battery",), labels=["P", "Q", "R"]),
         correct="both go out, because all the current must pass through P to reach them",
         wrongs={"Q and R stay on, because they are in parallel": "They are in parallel with EACH OTHER, but both are in series with P.", "only Q goes out": "Q and R are treated the same by the circuit.", "Q and R get brighter": "No current reaches them at all."},
         hints=["Trace the current from the battery.", "Does it pass through P before splitting?", "Yes: P is in the main path."],
         keypoints=[KP("both go out", "both", "go out", "off", "stop"), KP("P is in the main path / in series", "series", "main path", "through p", "all the current", "only path")]),
    dict(id="e02_saving_choice_data", level=4, lo="1.2o",
         stem=f"A family wants to cut its electricity bill. The table shows the options.\n\n{md_table(['option', 'energy saved per month / kWh'], [['replace 5 filament lamps with LEDs', 30], ['raise air-conditioner setting from 20 to 25 °C', 90], ['switch television off at the wall', 3]])}\n\nWhich option saves the most, and what is a correct conclusion?",
         correct="raising the air-conditioner setting saves the most; cooling is the largest use, so small changes there matter most",
         wrongs={"switching off the television saves the most": "That saves only 3 kWh.", "the LED change saves the most because lights are on all evening": "It saves 30 kWh, less than the air-conditioner's 90 kWh.", "all three save the same amount": "The savings are 30, 90 and 3 kWh."},
         hints=["Compare the kWh saved.", "Which is largest?", "The air-conditioner."],
         keypoints=[KP("air-conditioner saves the most", "air", "aircon", "90", "cooling"), KP("largest energy user", "most energy", "largest", "biggest", "main")]),

    # ------------------------------------------------------------ L5
    dict(id="e02_christmas_lights", level=5, lo="1.2b",
         stem=f"A string of decorative lights uses 20 small lamps in series. The table shows a test.\n\n{md_table(['test', 'result'], [['one lamp removed', 'all lamps go out'], ['one lamp replaced with a wire', 'the other 19 light slightly brighter']])}\n\nWhich explanation is correct?",
         correct="removing a lamp breaks the only path; replacing it with a wire lowers the total resistance so the current rises",
         wrongs={"the lamps are in parallel, so removing one breaks them all": "In parallel the others would stay on.", "the wire adds resistance, so the lamps get brighter": "A wire has almost no resistance; it LOWERS the total resistance.", "the lamps get brighter because the supply voltage rises": "The supply voltage is unchanged; the current rises because the resistance fell."},
         hints=["One path only: series.", "What does a plain wire have instead of a lamp's resistance?", "Less total resistance → more current → brighter."],
         keypoints=[KP("series / single path broken", "series", "one path", "single path", "break", "broken", "incomplete"), KP("less resistance so more current", "resistance", "current")]),
    dict(id="e02_design_choice_parallel_switches", level=5, lo="1.2j",
         stem="Fig. 1 shows a design for a room with a lamp and a fan. The owner wants to use each on its own. Which circuit change is needed, and why?",
         fig=lambda rng: S.circuit(["lamp", "motor"], top=("battery", "switch_closed"), labels=["lamp", "fan"]),
         correct="connect the lamp and fan in parallel, each with its own switch, so each gets the full voltage and works independently",
         wrongs={"keep the series circuit and add a second switch": "In series one switch opening turns BOTH off.", "use a bigger battery": "A bigger battery does not let the devices be controlled separately.", "connect them in parallel with one switch": "One switch in the main line still turns both on and off together."},
         hints=["In series, can one be off while the other is on?", "Parallel gives separate paths.", "A switch in each branch."],
         keypoints=[KP("parallel", "parallel", "separate branch", "own branch"), KP("own switch / independent", "own switch", "each switch", "separate switch", "independent", "separately")]),
    dict(id="e02_meter_reading_trick", level=5, lo="1.2n",
         stem=f"A tenant's bill is shown. The tenant says the bill is wrong because 'I only used 110 units'.\n\n{md_table(['item', 'value'], [['previous reading', '10 990 kWh'], ['current reading', '11 100 kWh'], ['usage charged', '1 100 kWh'], ['rate', '$0.30 per kWh'], ['amount', '$330.00']])}\n\nWho is right, and why?",
         correct="the tenant: 11 100 − 10 990 = 110 kWh, so the usage and the amount ($33.00) were entered wrongly",
         wrongs={"the supplier: the usage is the current reading minus 10 000": "Usage is current reading minus the PREVIOUS reading.", "the supplier: $330 is correct for 1100 units at $0.30": "The arithmetic is right but the 1100 units are wrong; only 110 were used.", "neither: the usage should be 11 100 kWh": "That is the meter reading, not the usage."},
         hints=["Usage = current − previous reading.", "11 100 − 10 990.", "110 units, not 1100."],
         keypoints=[KP("usage is 110 kWh", "110"), KP("subtract previous from current", "subtract", "minus", "difference", "previous", "wrongly", "entered")]),
    dict(id="e02_eco_label_evaluate", level=5, lo="1.2o",
         stem=f"Two refrigerators of the same size are on sale.\n\n{md_table(['fridge', 'price', 'energy used per year / kWh'], [['P', '$600', 600], ['Q', '$900', 300]])}\n\nElectricity costs $0.30 per kWh. Which is the better buy over 5 years, and why?",
         correct="Q: it costs $300 more but saves 300 kWh a year, which is $90 a year, so $450 over 5 years",
         wrongs={"P, because it is $300 cheaper": "Over 5 years P costs $300 + $900 = $1200 in electricity, more than Q's total.", "Q, because it uses no electricity": "Q still uses 300 kWh a year.", "P, because the electricity cost is the same for both": "P uses twice as many kWh, so its running cost is double."},
         hints=["Running cost per year = kWh × $0.30.", "P: $180 a year; Q: $90 a year.", "Over 5 years the saving is $450, more than the $300 extra price."],
         keypoints=[KP("Q saves energy / running cost", "q", "saves", "less electricity", "lower running", "cheaper to run"), KP("saving exceeds the extra price", "450", "more than", "exceeds", "pays back", "worth", "over 5 years", "long run")]),
    dict(id="e02_power_rating_confusion", level=5, lo="1.2k",
         stem=f"A student says: 'The kettle is rated 2000 W, so it always uses 2000 J no matter how long it is on.' The table shows the kettle in use.\n\n{md_table(['time on / s', 'energy used / J'], [[1, 2000], [10, 20000], [60, 120000]])}\n\nWhat is wrong with the student's statement?",
         correct="2000 W means 2000 J every SECOND; the energy used grows with the time the kettle is on",
         wrongs={"nothing: the power rating is the energy used": "Power is energy per second, not a fixed amount of energy.", "the kettle uses 2000 J per minute": "It uses 2000 J per SECOND (120 000 J per minute).", "the rating is wrong because the table shows 120 000 J": "The table agrees with 2000 J per second for 60 s."},
         hints=["What does 1 W mean?", "1 W = 1 J per second.", "Energy = power × time."],
         keypoints=[KP("watt = joule per second / rate", "per second", "each second", "every second", "rate", "j/s"), KP("energy depends on time", "time", "longer", "depends", "multiply")]),
    dict(id="e02_series_parallel_mixed_data", level=5, lo="1.2e",
         stem="Fig. 1 shows a circuit. The ammeter reads 0.9 A and lamp Q carries 0.3 A. P, Q and R are not identical. Which statement must be true?",
         fig=lambda rng: S.circuit(["ammeter"], parallel=[["lamp"], ["lamp"], ["lamp"]], top=("battery",), labels=["P", "Q", "R"]),
         correct="P and R together carry 0.6 A, and every lamp has the same voltage across it",
         wrongs={"each lamp carries 0.3 A": "Only Q is known to carry 0.3 A; the lamps differ.", "the voltage is shared so each lamp gets a third of it": "Parallel branches all get the full battery voltage.", "P carries 0.9 A": "0.9 A is the TOTAL for all three branches."},
         hints=["The battery current is the sum of the branch currents.", "0.9 − 0.3 = 0.6 A for the other two together.", "Parallel: same voltage across each branch."],
         keypoints=[KP("P + R = 0.6 A", "0.6"), KP("same voltage across each branch", "same voltage", "equal voltage", "full voltage")]),
    dict(id="e02_transformer_vs_fuse_misuse", level=5, lo="1.2a",
         stem=f"A student replaces a blown 3 A fuse in a lamp plug with a 13 A fuse 'so it will not blow again'.\n\n{md_table(['item', 'value'], [['lamp', '230 V, 60 W'], ['normal current', '0.26 A'], ['fuse fitted', '13 A']])}\n\nWhy is this dangerous?",
         correct="a fault could let a current of up to 13 A flow before the fuse melts, enough to overheat the wires and start a fire",
         wrongs={"the lamp will be too bright with a 13 A fuse": "The fuse does not change the normal current.", "the 13 A fuse will blow immediately": "It will not blow at 0.26 A; that is the problem: it will not blow early enough in a fault.", "it is not dangerous because the current is only 0.26 A normally": "The fuse is there for FAULTS, when the current can rise far above normal."},
         hints=["What is a fuse for?", "When does a 13 A fuse melt?", "Only at 13 A, far above what the thin wires can take."],
         keypoints=[KP("fuse will not melt early enough", "not melt", "won't blow", "will not blow", "too large", "too high", "13"), KP("wires overheat / fire", "overheat", "fire", "heat", "burn", "damage")]),
]

register_explain(EXPLAIN, chapter=2)
