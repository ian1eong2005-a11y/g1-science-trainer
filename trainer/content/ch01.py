"""Ch 1 Energy (K123 topic 1.1): 20 calculation / data templates and 40 explanation items.
lo codes: 1.1a forms of energy, 1.1b thermal energy flows hot -> cold, 1.1c conservation of energy, 1.1d power = energy / time,
1.1e fossil-fuel power station, 1.1f high-voltage transmission, 1.1g step-up and step-down transformers."""
from .. import figs, sketches as S, sketches_g1 as G1
from .base import fmt, md_table, nice, numeric_options, pick, register_explain, template, text_options

KP = lambda label, *phr: {"label": label, "any": list(phr)}

APPLIANCES = [("kettle", 2000), ("iron", 1200), ("hair dryer", 1500), ("television", 100), ("fan", 60), ("LED lamp", 10),
              ("filament lamp", 60), ("rice cooker", 500), ("laptop", 50), ("microwave oven", 800)]


# ================================================================ CALCULATION / DATA
# ---------------------------------------------------------------- L1
@template("c01_power_from_energy_time", chapter=1, level=1, lo="1.1d")
def power_from_energy_time(rng):
    name, _ = pick(rng, APPLIANCES)
    t = nice(rng, 5, 10, 20, 25, 50)
    P = nice(rng, 40, 60, 100, 200, 500)
    E = P * t
    opts, key, mis = numeric_options(rng, P, [
        (E * t, "You multiplied. Power = energy ÷ time."),
        (E, "That is the energy, not the power. Divide by the time."),
        (t / E, "Upside down: energy ÷ time, not time ÷ energy."),
    ], unit="W", sf=3)
    return dict(
        stem=f"The table shows how much energy a {name} converts.\n\n{md_table(['energy converted / J', 'time taken / s'], [[E, t]])}\n\nWhat is the power of the {name}?",
        options=opts, key=key, misconceptions=mis,
        formula="power = energy ÷ time taken   (W = J ÷ s)",
        working=[f"power = {E} J ÷ {t} s", f"= **{fmt(P)} W**"],
        hints=["Power is how much energy is converted every second.", "Divide the energy by the time.", f"{E} ÷ {t}."],
    )


@template("c01_energy_from_power_time", chapter=1, level=1, lo="1.1d")
def energy_from_power_time(rng):
    name, P = pick(rng, APPLIANCES)
    t = nice(rng, 2, 5, 10, 20, 30)
    E = P * t
    opts, key, mis = numeric_options(rng, E, [
        (P / t, "You divided. Energy = power × time."),
        (P, "That is the power: the energy converted in ONE second. Multiply by the number of seconds."),
        (P + t, "You added. Energy = power × time."),
    ], unit="J", sf=3)
    return dict(
        stem=f"The table gives the power rating of a {name}.\n\n{md_table(['appliance', 'power'], [[name, f'{P} W']])}\n\nHow much energy does the {name} convert in **{t} s**?",
        options=opts, key=key, misconceptions=mis,
        formula="energy = power × time taken   (J = W × s)",
        working=[f"energy = {P} W × {t} s", f"= **{fmt(E, sf=4)} J**"],
        hints=["1 W means 1 J every second.", "Multiply the power by the number of seconds.", f"{P} × {t}."],
    )


@template("c01_time_from_energy_power", chapter=1, level=1, lo="1.1d")
def time_from_energy_power(rng):
    name, P = pick(rng, APPLIANCES[:4] + APPLIANCES[7:8])
    t = nice(rng, 4, 5, 10, 15, 30)
    E = P * t
    opts, key, mis = numeric_options(rng, t, [
        (E * P, "You multiplied. Time = energy ÷ power."),
        (P / E, "Upside down: energy ÷ power."),
        (E, "That is the energy in joules, not a time."),
    ], unit="s", sf=3)
    return dict(
        stem=f"The table shows the power of a {name} and the energy it converts.\n\n{md_table(['power / W', 'energy converted / J'], [[P, E]])}\n\nFor how long was the {name} switched on?",
        options=opts, key=key, misconceptions=mis,
        formula="time = energy ÷ power",
        working=[f"time = {E} J ÷ {P} W", f"= **{fmt(t)} s**"],
        hints=["Rearrange power = energy ÷ time.", "time = energy ÷ power.", f"{E} ÷ {P}."],
    )


@template("c01_heat_flow_direction", chapter=1, level=1, lo="1.1b")
def heat_flow_direction(rng):
    hot = nice(rng, 60, 70, 80, 90)
    cold = nice(rng, 10, 20, 25, 30)
    swap = rng.random() < 0.5
    a, b = (cold, hot) if swap else (hot, cold)
    ans = "from Q to P" if swap else "from P to Q"
    wrong = "from P to Q" if swap else "from Q to P"
    opts, key, mis = text_options(rng, ans, {
        wrong: "Thermal energy flows from the HOTTER object to the COLDER one. Check which temperature is higher.",
        "in both directions equally": "There is a net flow from the hotter object until both reach the same temperature.",
        "no flow, because they are touching": "Touching objects at different temperatures exchange thermal energy.",
    })
    return dict(
        stem=f"Two metal blocks P and Q are placed in contact.\n\n{md_table(['block', 'temperature / °C'], [['P', a], ['Q', b]])}\n\nIn which direction does thermal energy flow?",
        options=opts, key=key, misconceptions=mis,
        formula="thermal energy flows from a region of higher temperature to a region of lower temperature",
        working=[f"P is at {a} °C and Q is at {b} °C", f"energy flows from the hotter block: **{ans}**"],
        hints=["Which block is hotter?", "Thermal energy always leaves the hotter object.", f"The hotter block is at {max(a, b)} °C."],
    )


# ---------------------------------------------------------------- L2
@template("c01_power_kj", chapter=1, level=2, lo="1.1d")
def power_kj(rng):
    Ek = nice(rng, 12, 18, 24, 36, 60)
    t = nice(rng, 20, 30, 40, 60)
    P = Ek * 1000 / t
    opts, key, mis = numeric_options(rng, P, [
        (Ek / t, "You forgot that 1 kJ = 1000 J."),
        (Ek * 1000 * t, "You multiplied. Power = energy ÷ time."),
        (Ek * 1000 / (t * 60), "The time is already in seconds; do not divide by 60."),
    ], unit="W", sf=3)
    return dict(
        stem=f"A motor converts the energy shown in the table.\n\n{md_table(['energy converted', 'time taken'], [[f'{Ek} kJ', f'{t} s']])}\n\nWhat is the power of the motor?",
        options=opts, key=key, misconceptions=mis,
        formula="power = energy ÷ time;  1 kJ = 1000 J",
        working=[f"{Ek} kJ = {Ek * 1000} J", f"power = {Ek * 1000} ÷ {t} = **{fmt(P)} W**"],
        hints=["Change kJ into J first.", "1 kJ = 1000 J.", f"{Ek * 1000} ÷ {t}."],
    )


@template("c01_energy_minutes", chapter=1, level=2, lo="1.1d")
def energy_minutes(rng):
    name, P = pick(rng, APPLIANCES)
    m = nice(rng, 2, 3, 5, 10)
    E = P * m * 60
    opts, key, mis = numeric_options(rng, E, [
        (P * m, "The time must be in seconds: multiply the minutes by 60."),
        (P / (m * 60), "You divided. Energy = power × time."),
        (P * m * 100, "1 minute = 60 s, not 100 s."),
    ], unit="J", sf=3)
    return dict(
        stem=f"The table gives the power of a {name}.\n\n{md_table(['appliance', 'power / W', 'time used'], [[name, P, f'{m} min']])}\n\nHow much energy does it convert?",
        options=opts, key=key, misconceptions=mis,
        formula="energy = power × time (in seconds);  1 min = 60 s",
        working=[f"time = {m} × 60 = {m * 60} s", f"energy = {P} × {m * 60} = **{fmt(E, sf=4)} J**"],
        hints=["Power × time gives energy, but the time must be in seconds.", f"{m} minutes = {m * 60} s.", f"{P} × {m * 60}."],
    )


@template("c01_wasted_energy", chapter=1, level=2, lo="1.1c")
def wasted_energy(rng):
    inp = nice(rng, 100, 200, 400, 500, 1000)
    useful = int(inp * nice(rng, 0.2, 0.25, 0.4, 0.6))
    waste = inp - useful
    opts, key, mis = numeric_options(rng, waste, [
        (inp + useful, "You added. The wasted energy is input MINUS useful output."),
        (useful, "That is the useful output, not the wasted part."),
        (inp, "Not all of the input is wasted; subtract the useful output."),
    ], unit="J", sf=3)
    return dict(
        stem=f"Fig. 1 shows the energy entering and the useful energy leaving a lamp every second. Energy cannot be created or destroyed. How much energy is wasted (as thermal energy) each second?",
        figure=S.energy_arrows(["electrical energy in", "useful light out"], [inp, useful]),
        options=opts, key=key, misconceptions=mis,
        formula="energy in = useful energy out + wasted energy   (conservation of energy)",
        working=[f"wasted = {inp} − {useful}", f"= **{fmt(waste)} J**"],
        hints=["Energy is conserved: input = useful + wasted.", "Subtract the useful output from the input.", f"{inp} − {useful}."],
    )


@template("c01_power_kw_to_w", chapter=1, level=2, lo="1.1d")
def power_kw_to_w(rng):
    Pk = nice(rng, 1.5, 2, 2.5, 3)
    t = nice(rng, 4, 5, 10, 20)
    E = Pk * 1000 * t
    opts, key, mis = numeric_options(rng, E, [
        (Pk * t, "1 kW = 1000 W. Change kW into W first."),
        (Pk * 1000 / t, "You divided. Energy = power × time."),
        (Pk * 100 * t, "1 kW = 1000 W, not 100 W."),
    ], unit="J", sf=3)
    return dict(
        stem=f"A heater is labelled as shown.\n\n{md_table(['power rating'], [[f'{Pk} kW']])}\n\nHow much energy does it convert in **{t} s**?",
        options=opts, key=key, misconceptions=mis,
        formula="energy = power × time;  1 kW = 1000 W",
        working=[f"{Pk} kW = {Pk * 1000:g} W", f"energy = {Pk * 1000:g} × {t} = **{fmt(E, sf=4)} J**"],
        hints=["Change kilowatts into watts.", "1 kW = 1000 W.", f"{Pk * 1000:g} × {t}."],
    )


# ---------------------------------------------------------------- L3
@template("c01_conservation_table", chapter=1, level=3, lo="1.1c")
def conservation_table(rng):
    inp = nice(rng, 500, 800, 1000, 2000)
    light = int(inp * nice(rng, 0.1, 0.2, 0.25))
    sound = int(inp * nice(rng, 0.05, 0.1))
    heat = inp - light - sound
    opts, key, mis = numeric_options(rng, heat, [
        (inp - light, "You forgot to subtract the sound energy as well."),
        (light + sound, "That is the useful output. Thermal energy = input − light − sound."),
        (inp, "The input is shared between three outputs; the thermal part is only one of them."),
    ], unit="J", sf=3)
    return dict(
        stem=f"A television converts energy as shown. Energy is conserved.\n\n{md_table(['energy', 'amount / J'], [['electrical energy in', inp], ['light energy out', light], ['sound energy out', sound], ['thermal energy out', '?']])}\n\nHow much thermal energy is produced?",
        options=opts, key=key, misconceptions=mis,
        formula="energy in = light + sound + thermal   (conservation of energy)",
        working=[f"thermal = {inp} − {light} − {sound}", f"= **{fmt(heat)} J**"],
        hints=["Total energy out must equal the energy in.", "Subtract BOTH useful outputs from the input.", f"{inp} − {light} − {sound}."],
    )


@template("c01_bar_chart_energy_use", chapter=1, level=3, lo="1.1d")
def bar_chart_energy_use(rng):
    names = ["kettle", "fan", "iron", "lamp"]
    vals = [nice(rng, 1800, 2000, 2200), nice(rng, 40, 60, 80), nice(rng, 1000, 1200, 1400), nice(rng, 10, 20, 60)]
    t = nice(rng, 10, 20, 30)
    i = rng.randrange(4)
    E = vals[i] * t
    opts, key, mis = numeric_options(rng, E, [
        (vals[i], "That is the power read from the chart, not the energy. Multiply by the time."),
        (vals[i] / t, "You divided. Energy = power × time."),
        (vals[(i + 1) % 4] * t, f"You read the wrong bar. The {names[i]} bar is the one you need."),
    ], unit="J", sf=3)
    return dict(
        stem=f"Fig. 1 shows the power of four appliances. How much energy does the **{names[i]}** convert in **{t} s**?",
        figure=S.bar_chart(names, vals, "power / W", ymax=2500, ystep=500),
        options=opts, key=key, misconceptions=mis,
        formula="energy = power × time",
        working=[f"from the chart, {names[i]} power = {vals[i]} W", f"energy = {vals[i]} × {t} = **{fmt(E, sf=4)} J**"],
        hints=[f"Read the height of the {names[i]} bar.", "Then multiply the power by the time in seconds.", f"{vals[i]} × {t}."],
    )


@template("c01_time_to_convert", chapter=1, level=3, lo="1.1d")
def time_to_convert(rng):
    Pk = nice(rng, 1, 2, 2.5, 4)
    E_MJ = nice(rng, 1.2, 1.5, 2.4, 3.0, 6.0)
    t = E_MJ * 1e6 / (Pk * 1000)
    opts, key, mis = numeric_options(rng, t, [
        (E_MJ / Pk, "Units: change MJ to J and kW to W before dividing."),
        (E_MJ * 1e6 / Pk, "You forgot that 1 kW = 1000 W."),
        (E_MJ * 1000 / (Pk * 1000), "1 MJ = 1 000 000 J, not 1000 J."),
    ], unit="s", sf=3)
    return dict(
        stem=f"A heater is used until it has converted the energy in the table.\n\n{md_table(['power', 'energy converted'], [[f'{Pk} kW', f'{E_MJ} MJ']])}\n\nHow long was the heater on? (1 MJ = 1 000 000 J)",
        options=opts, key=key, misconceptions=mis,
        formula="time = energy ÷ power;  1 kW = 1000 W;  1 MJ = 1 000 000 J",
        working=[f"{E_MJ} MJ = {E_MJ * 1e6:.0f} J;  {Pk} kW = {Pk * 1000:g} W", f"time = {E_MJ * 1e6:.0f} ÷ {Pk * 1000:g} = **{fmt(t)} s**"],
        hints=["Convert both quantities to base units first.", "time = energy ÷ power.", f"{E_MJ * 1e6:.0f} ÷ {Pk * 1000:g}."],
    )


@template("c01_which_transformer", chapter=1, level=3, lo="1.1g")
def which_transformer(rng):
    vin = nice(rng, 230, 11000, 25000)
    vout = pick(rng, [v for v in (12, 230, 11000, 400000) if v != vin])
    up = vout > vin
    ans = "step-up transformer" if up else "step-down transformer"
    opts, key, mis = text_options(rng, ans, {
        ("step-down transformer" if up else "step-up transformer"): "Compare the voltages: step-UP raises the voltage, step-DOWN lowers it.",
        "a fuse": "A fuse protects a circuit from a large current; it does not change the voltage.",
        "a variable resistor": "A variable resistor changes the current, not the supply voltage.",
    })
    return dict(
        stem=f"A device changes the voltage as shown in the table.\n\n{md_table(['voltage in / V', 'voltage out / V'], [[vin, vout]])}\n\nWhat is the device?",
        options=opts, key=key, misconceptions=mis,
        formula="step-up transformer: voltage out > voltage in;  step-down transformer: voltage out < voltage in",
        working=[f"voltage goes from {vin} V to {vout} V, which is {'higher' if up else 'lower'}", f"so it is a **{ans}**"],
        hints=["Is the voltage higher or lower after the device?", "Higher → step-up; lower → step-down.", f"{vout} V is {'more' if up else 'less'} than {vin} V."],
    )


# ---------------------------------------------------------------- L4
@template("c01_gradient_power", chapter=1, level=4, lo="1.1d")
def gradient_power(rng):
    P = nice(rng, 20, 40, 50, 100)
    tmax = nice(rng, 20, 40, 50)
    pts = [(0, 0), (tmax, P * tmax)]
    t1 = tmax // 2
    opts, key, mis = numeric_options(rng, P, [
        (P * tmax, "That is the total energy at the end, not the power. Power = energy ÷ time (the gradient)."),
        (tmax / (P * tmax) if P * tmax else 1, "Upside down: divide energy by time, not time by energy."),
        (P * 2, "Check your reading: energy ÷ time at any point gives the same value."),
    ], unit="W", sf=3)
    return dict(
        stem="Fig. 1 shows the energy converted by a lamp against time. What is the power of the lamp?",
        figure=figs.graph(pts, tmax, P * tmax, tmax // 4, P * tmax // 4, xlabel="time / s", ylabel="energy converted / J"),
        options=opts, key=key, misconceptions=mis,
        formula="power = energy ÷ time = gradient of an energy-time graph",
        working=[f"at t = {tmax} s the energy is {P * tmax} J", f"power = {P * tmax} ÷ {tmax} = **{fmt(P)} W**"],
        hints=["Pick any point on the line and read its energy and time.", "Divide energy by time.", f"At {t1} s the energy is {P * t1} J."],
    )


@template("c01_equilibrium_table", chapter=1, level=4, lo="1.1b")
def equilibrium_table(rng):
    hot0 = nice(rng, 80, 90, 100)
    cold0 = nice(rng, 20, 25, 30)
    final = (hot0 + cold0) // 2 + nice(rng, -5, 0, 5)
    rows = []
    for i, t in enumerate((0, 2, 4, 6, 8)):
        f = min(1, i / 3.5)
        rows.append([t, round(hot0 - (hot0 - final) * f), round(cold0 + (final - cold0) * f)])
    rows[-1] = [8, final, final]
    opts, key, mis = text_options(rng, f"both reach {final} °C and stay there", {
        f"the spoon keeps cooling below {final} °C": "Once both are at the same temperature there is no net flow of thermal energy.",
        f"the water keeps warming above {final} °C": "The water cannot get hotter than the spoon that is heating it.",
        f"the spoon returns to {cold0} °C": "Thermal energy has already flowed into the spoon; it does not flow back out while the water is at the same temperature.",
    })
    return dict(
        stem=f"A cold metal spoon is placed in hot water. The table shows the temperatures.\n\n{md_table(['time / min', 'water / °C', 'spoon / °C'], rows)}\n\nWhat happens after 8 minutes if no energy is lost to the surroundings?",
        options=opts, key=key, misconceptions=mis,
        formula="thermal energy flows from hot to cold until both regions reach the same temperature",
        working=["the water cools and the spoon warms", f"at {final} °C they are at the same temperature, so the net flow stops: **both reach {final} °C and stay there**"],
        hints=["Where does the energy flow from, and to?", "When does the flow stop?", "When the temperatures are equal."],
    )


@template("c01_transmission_loss", chapter=1, level=4, lo="1.1f")
def transmission_loss(rng):
    rows = [[v, w] for v, w in zip((11000, 132000, 400000), (nice(rng, 40, 50, 60), nice(rng, 8, 10, 12), nice(rng, 1, 2, 3)))]
    ans = "400 000 V, because the energy wasted is smallest"
    opts, key, mis = text_options(rng, ans, {
        "11 000 V, because the energy wasted is smallest": "Read the table again: the wasted energy is largest at 11 000 V.",
        "11 000 V, because a lower voltage is safer": "Safety is handled by insulation and high pylons; the grid uses high voltage to cut the energy wasted.",
        "132 000 V, because it is the middle value": "Choose the voltage with the least energy wasted, not the middle one.",
    })
    return dict(
        stem=f"Electricity is sent through the same cables at three different voltages. The table shows the percentage of energy wasted as heat in the cables.\n\n{md_table(['transmission voltage / V', 'energy wasted / %'], rows)}\n\nWhich voltage should the power company use, and why?",
        options=opts, key=key, misconceptions=mis,
        formula="transmitting at high voltage reduces the current in the cables, so less energy is wasted as heat",
        working=["the wasted energy falls as the voltage rises", f"so the grid uses the highest voltage: **{ans}**"],
        hints=["Compare the 'energy wasted' column.", "Which voltage wastes the least?", "The highest voltage."],
    )


@template("c01_station_output", chapter=1, level=4, lo="1.1e")
def station_output(rng):
    chem = nice(rng, 1000, 2000, 5000)
    boiler = int(chem * nice(rng, 0.8, 0.9))
    turbine = int(boiler * nice(rng, 0.5, 0.6))
    gen = int(turbine * nice(rng, 0.9, 0.95))
    waste = chem - gen
    opts, key, mis = numeric_options(rng, waste, [
        (chem - boiler, "That is only the energy wasted in the boiler. Count every stage."),
        (gen, "That is the useful electrical output, not the wasted energy."),
        (chem, "Some of the input becomes useful electricity; not all of it is wasted."),
    ], unit="MJ", sf=3)
    return dict(
        stem="Fig. 1 shows the energy passing through the stages of a fossil fuel power station every minute. How much energy in total is wasted as thermal energy?",
        figure=S.energy_arrows(["chemical energy in fuel", "thermal energy in steam", "kinetic energy of turbine", "electrical energy out"], [chem, boiler, turbine, gen], unit="MJ"),
        options=opts, key=key, misconceptions=mis,
        formula="total wasted = energy in − useful energy out   (conservation of energy)",
        working=[f"energy in = {chem} MJ, electrical energy out = {gen} MJ", f"wasted = {chem} − {gen} = **{fmt(waste)} MJ**"],
        hints=["Energy is conserved across the whole station.", "Wasted = input − final useful output.", f"{chem} − {gen}."],
    )


# ---------------------------------------------------------------- L5
@template("c01_two_lamps_saving", chapter=1, level=5, lo="1.1d")
def two_lamps_saving(rng):
    Pf = nice(rng, 40, 60, 100)
    Pl = nice(rng, 5, 8, 10, 12)
    hours = nice(rng, 2, 4, 5)
    saved = (Pf - Pl) * hours * 3600
    opts, key, mis = numeric_options(rng, saved, [
        ((Pf - Pl) * hours, "The time must be in seconds: 1 hour = 3600 s."),
        (Pf * hours * 3600, "That is the energy the filament lamp alone converts; the saving is the DIFFERENCE between the lamps."),
        ((Pf - Pl) * hours * 60, "1 hour = 3600 s, not 60 s."),
    ], unit="J", sf=3)
    return dict(
        stem=f"A family replaces a filament lamp with an LED lamp that gives the same brightness.\n\n{md_table(['lamp', 'power / W'], [['filament', Pf], ['LED', Pl]])}\n\nHow much energy is saved when the lamp is used for **{hours} hours**?",
        options=opts, key=key, misconceptions=mis,
        formula="energy saved = (difference in power) × time in seconds;  1 h = 3600 s",
        working=[f"difference in power = {Pf} − {Pl} = {Pf - Pl} W", f"time = {hours} × 3600 = {hours * 3600} s", f"saved = {Pf - Pl} × {hours * 3600} = **{fmt(saved, sf=4)} J**"],
        hints=["Find the difference in power first.", "Then multiply by the time in seconds.", f"{Pf - Pl} × {hours * 3600}."],
    )


@template("c01_two_stage_machine", chapter=1, level=5, lo="1.1c")
def two_stage_machine(rng):
    inp = nice(rng, 1000, 2000, 4000)
    p1 = nice(rng, 0.6, 0.7, 0.8)
    p2 = nice(rng, 0.5, 0.6, 0.75)
    out = inp * p1 * p2
    opts, key, mis = numeric_options(rng, out, [
        (inp * p1, "That is after the first stage only. The second stage wastes some more."),
        (inp * (p1 + p2) / 2, "Do not average the percentages: apply them one after the other."),
        (inp * (1 - p1 * p2), "That is the energy wasted, not the useful output."),
    ], unit="J", sf=3)
    return dict(
        stem=f"Fig. 1 shows a motor driving a pump. The motor passes on {int(p1 * 100)}% of its input as useful energy; the pump passes on {int(p2 * 100)}% of what it receives. The motor receives {inp} J of electrical energy. How much useful energy leaves the pump?",
        figure=S.flow_boxes(["electrical energy", "motor", "pump", "useful energy out"], arrow_labels=[f"{inp} J", f"{int(p1 * 100)}%", f"{int(p2 * 100)}%"]),
        options=opts, key=key, misconceptions=mis,
        formula="useful output = input × fraction passed on at each stage",
        working=[f"after the motor: {inp} × {p1} = {inp * p1:g} J", f"after the pump: {inp * p1:g} × {p2} = **{fmt(out)} J**"],
        hints=["Work through one stage at a time.", f"The motor passes on {inp * p1:g} J.", f"{inp * p1:g} × {p2}."],
    )


@template("c01_station_percentage", chapter=1, level=5, lo="1.1e")
def station_percentage(rng):
    chem = nice(rng, 2000, 2500, 4000)
    gen = int(chem * nice(rng, 0.3, 0.35, 0.4))
    pc = gen / chem * 100
    opts, key, mis = numeric_options(rng, pc, [
        (100 - pc, "That is the percentage WASTED. The question asks for the useful percentage."),
        (chem / gen, "Upside down, and not a percentage: useful ÷ input × 100."),
        (gen / chem, "Multiply by 100 to get a percentage."),
    ], unit="%", sf=3)
    return dict(
        stem=f"A fossil fuel power station converts energy as shown.\n\n{md_table(['energy', 'amount / MJ'], [['chemical energy in fuel burnt', chem], ['electrical energy delivered', gen]])}\n\nWhat percentage of the fuel's energy becomes electrical energy?",
        options=opts, key=key, misconceptions=mis,
        formula="percentage useful = useful energy ÷ energy input × 100%",
        working=[f"useful ÷ input = {gen} ÷ {chem}", f"× 100 = **{fmt(pc)} %**"],
        hints=["Divide the useful output by the input.", "Then multiply by 100.", f"{gen} ÷ {chem} × 100."],
    )


@template("c01_total_power_two_devices", chapter=1, level=5, lo="1.1d")
def total_power_two_devices(rng):
    E1 = nice(rng, 3000, 6000, 9000)
    t1 = nice(rng, 30, 60)
    E2 = nice(rng, 1200, 2400, 4800)
    t2 = nice(rng, 20, 40, 120)
    P1, P2 = E1 / t1, E2 / t2
    ans = "P" if P1 > P2 else "Q"
    stronger, weaker = (P1, P2) if P1 > P2 else (P2, P1)
    opts, key, mis = text_options(rng, f"{ans}, because its power is {fmt(stronger)} W compared with {fmt(weaker)} W", {
        f"{'Q' if ans == 'P' else 'P'}, because its power is {fmt(weaker)} W compared with {fmt(stronger)} W": "Check the division: the higher power is the larger energy ÷ time.",
        f"{'P' if E1 > E2 else 'Q'}, because it converts more energy in total": "Power is energy PER SECOND. The one converting more energy may take much longer to do it.",
        "they have the same power because both are motors": "Work out energy ÷ time for each motor.",
    })
    return dict(
        stem=f"Two motors P and Q are tested.\n\n{md_table(['motor', 'energy converted / J', 'time / s'], [['P', E1, t1], ['Q', E2, t2]])}\n\nWhich motor has the higher power?",
        options=opts, key=key, misconceptions=mis,
        formula="power = energy ÷ time",
        working=[f"P: {E1} ÷ {t1} = {fmt(P1)} W", f"Q: {E2} ÷ {t2} = {fmt(P2)} W", f"higher power: **{ans}**"],
        hints=["Work out each power separately.", "power = energy ÷ time for each motor.", f"P gives {fmt(P1)} W."],
    )


# ================================================================ EXPLANATION
T_FORMS = md_table(["form of energy", "example"], [["kinetic", "a moving car"], ["chemical potential", "food, fuel, a battery"], ["gravitational potential", "a book on a shelf"], ["elastic potential", "a stretched spring"], ["thermal", "a hot drink"], ["light", "a torch beam"], ["sound", "a ringing bell"], ["electrical", "current in a wire"]])

EXPLAIN = [
    # ------------------------------------------------------------ L1
    dict(id="e01_energy_stored_food", level=1, lo="1.1a",
         stem=f"The table lists forms of energy.\n\n{T_FORMS}\n\nWhich form of energy is stored in food?",
         correct="chemical potential energy",
         wrongs={"kinetic energy": "Kinetic energy is the energy of a MOVING object.", "thermal energy": "Thermal energy is the energy of a hot object.", "sound energy": "Sound energy comes from vibrations."},
         hints=["Food is a store of energy, like fuel.", "Fuels and batteries store the same form.", "It is released by chemical reactions in the body."]),
    dict(id="e01_energy_moving_object", level=1, lo="1.1a",
         stem=f"The table lists forms of energy.\n\n{T_FORMS}\n\nA bus is travelling along a road. Which form of energy does the bus have because it is moving?",
         correct="kinetic energy",
         wrongs={"gravitational potential energy": "That depends on height, not on motion.", "chemical potential energy": "That is the energy stored in the fuel, not the energy of motion.", "elastic potential energy": "That is stored in a stretched or squashed object."},
         hints=["'Kinetic' means to do with motion.", "Any moving object has this form of energy.", "Kinetic."]),
    dict(id="e01_stretched_spring", level=1, lo="1.1a",
         stem=f"The table lists forms of energy.\n\n{T_FORMS}\n\nWhich form of energy is stored in a stretched rubber band?",
         correct="elastic potential energy",
         wrongs={"gravitational potential energy": "That depends on height above the ground.", "kinetic energy": "A stretched band held still is not moving.", "thermal energy": "Stretching stores energy in the band's shape, not as heat."},
         hints=["The energy is stored because the band's shape is changed.", "Stretched or squashed objects store this form.", "Elastic."]),
    dict(id="e01_book_on_shelf", level=1, lo="1.1a",
         stem=f"The table lists forms of energy.\n\n{T_FORMS}\n\nA book rests on a high shelf. Which form of energy does it have because of its height?",
         correct="gravitational potential energy",
         wrongs={"kinetic energy": "The book is not moving.", "elastic potential energy": "The book is not stretched or squashed.", "chemical potential energy": "That is the energy stored in fuels and food."},
         hints=["It is a stored energy that depends on height.", "If the book fell, this energy would turn into kinetic energy.", "Gravitational potential."]),
    dict(id="e01_hot_to_cold", level=1, lo="1.1b",
         stem=f"The table shows two cups of water placed in contact.\n\n{md_table(['cup', 'temperature / °C'], [['X', 90], ['Y', 20]])}\n\nThermal energy flows",
         correct="from X to Y, because X is hotter",
         wrongs={"from Y to X, because Y is colder": "Thermal energy leaves the HOTTER object.", "from X to Y, because X has more water": "The direction depends on temperature, not on the amount of water.", "in neither direction, because they are different cups": "Objects in contact at different temperatures exchange thermal energy."},
         hints=["Which cup is at the higher temperature?", "Thermal energy always flows out of the hotter object.", "From the hotter to the colder."]),
    dict(id="e01_conservation_statement", level=1, lo="1.1c",
         stem=f"The table shows three statements about energy.\n\n{md_table(['statement'], [['1  Energy cannot be created.'], ['2  Energy cannot be destroyed.'], ['3  Energy can be converted from one form to another.']])}\n\nWhich statements make up the principle of conservation of energy?",
         correct="1, 2 and 3",
         wrongs={"1 only": "The principle also says energy cannot be destroyed and can be converted.", "3 only": "Conversion is part of it, but the principle also says the total amount never changes.", "1 and 2 only": "The principle also includes conversion from one form to another."},
         hints=["The principle has three parts.", "Not created, not destroyed, and ...?", "... only converted from one form to another."]),
    dict(id="e01_power_unit", level=1, lo="1.1d",
         stem=f"The table lists units.\n\n{md_table(['unit', 'symbol'], [['joule', 'J'], ['watt', 'W'], ['newton', 'N'], ['second', 's']])}\n\nWhich unit is used for power?",
         correct="watt (W)",
         wrongs={"joule (J)": "The joule is the unit of energy.", "newton (N)": "The newton is the unit of force.", "second (s)": "The second is the unit of time."},
         hints=["Power is the rate of converting energy.", "The unit is named after James Watt.", "W."]),
    dict(id="e01_power_station_fuel", level=1, lo="1.1e",
         stem=f"The table lists fuels.\n\n{md_table(['fuel'], [['coal'], ['natural gas'], ['oil'], ['wood']])}\n\nWhich of these are fossil fuels burnt in power stations?",
         correct="coal, natural gas and oil",
         wrongs={"wood only": "Wood is not a fossil fuel: it comes from living trees.", "coal only": "Natural gas and oil are also fossil fuels.", "natural gas and wood": "Wood is not a fossil fuel."},
         hints=["Fossil fuels formed from the remains of living things over millions of years.", "There are three of them in the table.", "Coal, oil and natural gas."]),

    # ------------------------------------------------------------ L2
    dict(id="e01_torch_conversion", level=2, lo="1.1a",
         stem=f"Fig. 1 shows the energy conversion in a torch. Which forms of energy are X and Y?",
         fig=lambda rng: S.flow_boxes(["X in the battery", "electrical energy", "Y from the lamp"]),
         correct="X = chemical potential energy, Y = light energy",
         wrongs={"X = kinetic energy, Y = light energy": "A battery stores energy chemically; nothing in it is moving.", "X = chemical potential energy, Y = sound energy": "A torch gives out light, not sound.", "X = electrical energy, Y = thermal energy": "The battery stores chemical energy; the useful output is light."},
         hints=["What does a battery store?", "What is the useful output of a torch?", "Chemical → electrical → light."]),
    dict(id="e01_falling_ball", level=2, lo="1.1a",
         stem=f"The table shows a ball at three positions as it falls.\n\n{md_table(['position', 'height / m', 'speed / m/s'], [['top', 5, 0], ['middle', 2.5, 7], ['just above ground', 0, 10]])}\n\nAs the ball falls, which energy change takes place?",
         correct="gravitational potential energy → kinetic energy",
         wrongs={"kinetic energy → gravitational potential energy": "That happens when a ball is thrown UP. Falling is the reverse.", "chemical potential energy → kinetic energy": "No fuel or food is involved.", "elastic potential energy → kinetic energy": "The ball is not stretched or squashed while falling."},
         hints=["Height goes down, speed goes up.", "Which energy depends on height, and which on speed?", "Gravitational potential → kinetic."]),
    dict(id="e01_identify_higher_power", level=2, lo="1.1d",
         stem=f"The table shows two kettles.\n\n{md_table(['kettle', 'energy converted / J', 'time / s'], [['P', 20000, 10], ['Q', 20000, 20]])}\n\nWhich statement is correct?",
         correct="P has twice the power of Q",
         wrongs={"Q has twice the power of P": "Q takes LONGER to convert the same energy, so its power is lower.", "P and Q have the same power": "Same energy in different times means different powers.", "P converts more energy than Q": "Both convert 20 000 J; they differ in the time taken."},
         hints=["Power = energy ÷ time.", "Same energy, half the time → ?", "Twice the power."]),
    dict(id="e01_hot_drink_cooling", level=2, lo="1.1b",
         stem=f"The table shows the temperature of a cup of tea left on a table in a room at 25 °C.\n\n{md_table(['time / min', 'temperature / °C'], [[0, 80], [10, 60], [20, 45], [30, 36]])}\n\nWhy does the tea cool down?",
         correct="thermal energy flows from the hot tea to the cooler air around it",
         wrongs={"cold flows from the air into the tea": "'Cold' is not a form of energy; it is thermal energy that moves, from hot to cold.", "the tea loses its thermal energy because it is evaporating only": "Evaporation plays a part, but the main idea is that thermal energy flows from the hotter tea to the cooler surroundings.", "thermal energy flows from the air into the tea": "Energy flows from the HOTTER region (the tea) to the colder one (the air)."},
         hints=["Which is hotter, the tea or the room?", "Thermal energy leaves the hotter one.", "From the tea to the air."]),
    dict(id="e01_station_stages_order", level=2, lo="1.1e",
         stem=f"The table lists the parts of a fossil fuel power station.\n\n{md_table(['part', 'what it does'], [['boiler', 'burns fuel to make steam'], ['turbine', 'turned by the steam'], ['generator', 'turned by the turbine']])}\n\nWhich energy conversion happens in the **generator**?",
         correct="kinetic energy → electrical energy",
         wrongs={"chemical potential energy → thermal energy": "That happens in the boiler when the fuel burns.", "thermal energy → kinetic energy": "That happens in the turbine, pushed round by the steam.", "electrical energy → kinetic energy": "That is a motor, the reverse of a generator."},
         hints=["The generator is turned by the turbine.", "Turning means kinetic energy goes IN.", "Kinetic → electrical."]),
    dict(id="e01_transformer_near_home", level=2, lo="1.1g",
         stem=f"Fig. 1 shows how electricity reaches homes. Which type of transformer is used just before the homes, and why?",
         fig=lambda rng: G1.transmission(),
         correct="step-down, to lower the voltage to a safe 230 V",
         wrongs={"step-up, to raise the voltage for the homes": "Homes use a LOW voltage (230 V); the voltage must come DOWN from the transmission lines.", "step-down, to raise the voltage": "Step-down transformers LOWER the voltage.", "step-up, to lower the voltage": "Step-up transformers RAISE the voltage."},
         hints=["Transmission lines carry very high voltage.", "Homes need 230 V, which is much lower.", "The voltage must be stepped DOWN."]),
    dict(id="e01_transformer_after_station", level=2, lo="1.1g",
         stem=f"Fig. 1 shows how electricity reaches homes. Which type of transformer is used just after the power station, and why?",
         fig=lambda rng: G1.transmission(),
         correct="step-up, to raise the voltage for transmission",
         wrongs={"step-down, to lower the voltage for transmission": "Transmission needs a HIGH voltage, so the voltage is raised.", "step-up, to lower the voltage": "Step-up transformers RAISE the voltage.", "step-down, to make the current larger": "A larger current would waste MORE energy in the cables."},
         hints=["Transmission lines run at a very high voltage.", "The station's output voltage must be raised.", "Step-up."]),
    dict(id="e01_appliance_wasted_form", level=2, lo="1.1c",
         stem=f"The table shows the useful energy from four appliances.\n\n{md_table(['appliance', 'useful energy out'], [['lamp', 'light'], ['radio', 'sound'], ['fan', 'kinetic'], ['heater', 'thermal']])}\n\nIn which form is energy usually WASTED by the lamp, radio and fan?",
         correct="thermal energy",
         wrongs={"electrical energy": "Electrical energy is the INPUT, not the waste.", "light energy": "Light is the useful output of the lamp only.", "kinetic energy": "Kinetic energy is the useful output of the fan only."},
         hints=["Appliances get warm when they run.", "The waste energy heats the appliance and the air.", "Thermal."]),

    # ------------------------------------------------------------ L3
    dict(id="e01_rollercoaster_top", level=3, lo="1.1c",
         stem=f"The table shows the energy of a roller-coaster car at the top of a hill and at the bottom.\n\n{md_table(['position', 'gravitational potential energy / kJ', 'kinetic energy / kJ'], [['top', 100, 0], ['bottom', 0, 90]])}\n\nWhy is the kinetic energy at the bottom less than 100 kJ?",
         correct="some energy is converted to thermal energy by friction, so the total is still 100 kJ",
         wrongs={"energy is destroyed as the car goes down": "Energy is never destroyed; it is converted to another form.", "the car gains gravitational potential energy at the bottom": "At the bottom the height, and so the gravitational potential energy, is zero.", "the table has a mistake because energy must be equal": "The TOTAL energy is equal; some of it is in a third form, thermal energy."},
         hints=["Energy is conserved: where did the missing 10 kJ go?", "Think of the rubbing of wheels and air.", "Friction converts it to thermal energy."],
         keypoints=[KP("friction / rubbing", "friction", "rubbing", "air resistance", "resistance"), KP("thermal energy produced", "thermal", "heat", "warm")]),
    dict(id="e01_which_cools_faster", level=3, lo="1.1b",
         stem=f"Two identical cups of water are placed in two rooms.\n\n{md_table(['cup', 'water temperature / °C', 'room temperature / °C'], [['X', 80, 10], ['Y', 80, 30]])}\n\nWhich cup cools faster at first, and why?",
         correct="X, because the temperature difference between the water and the room is larger",
         wrongs={"Y, because the room is warmer": "A warmer room means a SMALLER temperature difference, so slower cooling.", "both the same, because the water is at the same temperature": "The rate depends on the difference between water and room, not the water alone.", "X, because cold flows into it faster": "It is thermal energy that flows, OUT of the hot water."},
         hints=["Thermal energy flows from hot to cold.", "A bigger temperature difference gives a faster flow.", "Which cup has the bigger difference?"],
         keypoints=[KP("larger temperature difference", "temperature difference", "bigger difference", "larger difference", "greater difference", "colder room"), KP("energy flows faster", "faster", "quicker", "more quickly", "rate", "is larger", "bigger")]),
    dict(id="e01_fan_energy_chain", level=3, lo="1.1a",
         stem="Fig. 1 shows the energy conversions in an electric fan. Which forms of energy are X and Y?",
         fig=lambda rng: S.flow_boxes(["electrical energy", "X (useful)", "Y (wasted)"], arrow_labels=["motor", "motor"]),
         correct="X = kinetic energy, Y = thermal energy",
         wrongs={"X = thermal energy, Y = kinetic energy": "The useful output of a fan is the MOVING air (kinetic); heat is the waste.", "X = sound energy, Y = kinetic energy": "Sound is a waste product of a fan, not its purpose.", "X = kinetic energy, Y = light energy": "A fan does not give out light."},
         hints=["What is a fan for?", "What do you feel if you touch a motor that has been running?", "Kinetic useful, thermal wasted."],
         keypoints=[KP("kinetic energy is useful", "kinetic", "moving", "motion", "movement"), KP("thermal energy is wasted", "thermal", "heat", "warm")]),
    dict(id="e01_why_grid_high_voltage", level=3, lo="1.1f",
         stem=f"The table compares two ways of sending the same electrical power through cables.\n\n{md_table(['voltage', 'current', 'energy wasted as heat'], [['low', 'large', 'large'], ['high', 'small', 'small']])}\n\nWhy is electricity transmitted at high voltage?",
         correct="a high voltage means a small current, so less energy is wasted as heat in the cables",
         wrongs={"a high voltage makes the current larger, so more energy reaches homes": "At high voltage the current is SMALLER, which is the point.", "a high voltage is safer for people living near the lines": "High voltage is dangerous; it is used despite that, to cut energy losses.", "cables can only carry electricity at high voltage": "Cables can carry any voltage; the choice is about wasted energy."},
         hints=["Read the current column.", "What does a small current do to the heat in the cables?", "Less heat wasted."],
         keypoints=[KP("current is smaller", "small current", "smaller current", "less current", "lower current", "reduces the current", "current is low"), KP("less energy wasted as heat", "less energy", "less heat", "wasted", "lost", "loss")]),
    dict(id="e01_kettle_power_rating", level=3, lo="1.1d",
         stem=f"The table shows two kettles that each boil the same amount of water.\n\n{md_table(['kettle', 'power rating / W', 'time to boil / s'], [['P', 2000, 120], ['Q', 1000, 240]])}\n\nWhich statement explains the times?",
         correct="P converts energy twice as fast, so it needs half the time for the same energy",
         wrongs={"P uses twice as much energy to boil the water": "Both convert the same energy (2000 × 120 = 1000 × 240); P just does it faster.", "Q is more powerful because it takes longer": "Taking longer means LOWER power.", "the kettles use different amounts of water": "The question says the same amount of water."},
         hints=["Power is energy converted per second.", "Compare 2000 × 120 with 1000 × 240.", "Same energy, half the time."],
         keypoints=[KP("P has higher power / converts faster", "higher power", "more power", "twice the power", "faster", "quicker", "more powerful"), KP("same energy needed", "same energy", "same amount of energy", "equal energy")]),
    dict(id="e01_station_sequence", level=3, lo="1.1e",
         stem="Fig. 1 shows the energy conversions in a fossil fuel power station. What are X and Y?",
         fig=lambda rng: S.flow_boxes(["chemical energy in fuel", "X", "kinetic energy of turbine", "Y"], arrow_labels=["boiler", "steam", "generator"]),
         correct="X = thermal energy, Y = electrical energy",
         wrongs={"X = electrical energy, Y = thermal energy": "Burning fuel produces heat first; electricity comes out of the generator at the end.", "X = kinetic energy, Y = light energy": "The boiler makes thermal energy, and a power station delivers electrical energy.", "X = thermal energy, Y = chemical energy": "Chemical energy is the INPUT from the fuel, not the output."},
         hints=["What does burning fuel in the boiler produce?", "What does a generator produce?", "Thermal, then electrical."],
         keypoints=[KP("thermal energy from burning", "thermal", "heat"), KP("electrical energy out", "electrical", "electricity")]),
    dict(id="e01_transformer_charger", level=3, lo="1.1g",
         stem=f"The table shows the label on a phone charger.\n\n{md_table(['input', 'output'], [['230 V', '5 V']])}\n\nWhat does the charger contain, and why?",
         correct="a step-down transformer, because the phone needs a much lower voltage than the mains",
         wrongs={"a step-up transformer, because the phone needs more voltage": "5 V is LESS than 230 V, so the voltage is stepped DOWN.", "a fuse, because the phone needs less voltage": "A fuse does not change the voltage.", "a step-down transformer, because it makes the current smaller": "Its job is to lower the VOLTAGE to what the phone needs."},
         hints=["Compare the input and output voltages.", "230 V → 5 V is a decrease.", "Step-down."],
         keypoints=[KP("step-down", "step-down", "step down", "steps down", "lower the voltage", "reduce the voltage"), KP("phone needs a lower voltage", "lower voltage", "smaller voltage", "less voltage", "5 V", "low voltage")]),
    dict(id="e01_bouncing_ball_height", level=3, lo="1.1c",
         stem="Fig. 1 shows a ball bouncing. Each bounce is lower than the one before. Explain why, using the principle of conservation of energy.",
         fig=lambda rng: S.bounce([100, 70, 49]),
         correct="at each bounce some energy is converted to thermal and sound energy, so less is left to lift the ball",
         wrongs={"energy is lost at each bounce, so there is less energy": "Energy is never lost; it is CONVERTED to other forms such as thermal and sound.", "the ball gets heavier with each bounce": "The mass of the ball does not change.", "gravity gets stronger with each bounce": "Gravity is the same each time."},
         hints=["Energy cannot be destroyed, only converted.", "What do you hear at each bounce? What happens to the ball's temperature?", "Sound and thermal energy."],
         keypoints=[KP("converted to thermal / sound", "thermal", "heat", "sound"), KP("less energy left for height", "less", "smaller", "lower", "reduced")]),

    # ------------------------------------------------------------ L4
    dict(id="e01_pendulum_energy", level=4, lo="1.1c",
         stem=f"The table shows the energy of a swinging pendulum at three points.\n\n{md_table(['position', 'gravitational potential energy / J', 'kinetic energy / J'], [['highest point', 4, 0], ['halfway down', 2, 2], ['lowest point', 0, 4]])}\n\nWhich statement is correct?",
         correct="the total energy stays at 4 J because gravitational potential energy is converted to kinetic energy",
         wrongs={"energy is created as the pendulum speeds up": "Energy is never created; the kinetic energy comes from the gravitational potential energy.", "the pendulum has most energy at the lowest point": "The total is 4 J at every position.", "kinetic energy is destroyed at the highest point": "It is converted back to gravitational potential energy."},
         hints=["Add the two columns at each position.", "What do you notice about the total?", "It is always 4 J."],
         keypoints=[KP("total stays the same", "total", "same", "constant", "conserved", "4 J"), KP("gravitational to kinetic", "kinetic", "gravitational", "potential")]),
    dict(id="e01_insulated_cup", level=4, lo="1.1b",
         stem=f"Hot water is poured into two cups: one made of thin metal and one made of foam. The table shows the temperatures after 10 minutes.\n\n{md_table(['cup', 'start / °C', 'after 10 min / °C'], [['thin metal', 80, 50], ['foam', 80, 72]])}\n\nWhy does the water in the foam cup stay hotter?",
         correct="foam slows the flow of thermal energy from the hot water to the cooler air",
         wrongs={"foam stops thermal energy from flowing completely": "The foam cup still cools (80 → 72 °C); the flow is slowed, not stopped.", "foam produces thermal energy to keep the water warm": "Foam does not produce energy.", "metal absorbs cold from the air": "Cold is not a substance; thermal energy flows OUT through the metal quickly."},
         hints=["Thermal energy flows from the hot water to the air.", "Which cup lets it flow through more easily?", "Foam slows the flow."],
         keypoints=[KP("foam slows / reduces the flow", "slow", "reduce", "less", "insulat", "poor conductor"), KP("thermal energy to the surroundings", "thermal", "heat", "air", "surrounding")]),
    dict(id="e01_grid_losses_data", level=4, lo="1.1f",
         stem=f"A power company tests its cables.\n\n{md_table(['transmission voltage / kV', 'current in cable / A', 'power wasted in cable / kW'], [[25, 400, 160], [100, 100, 10], [400, 25, 0.6]])}\n\nWhat do the data show?",
         correct="raising the voltage lowers the current, and the power wasted falls very sharply",
         wrongs={"raising the voltage raises the current, so more power is wasted": "Read the current column: it FALLS as the voltage rises.", "the power wasted is the same at every voltage": "It falls from 160 kW to 0.6 kW.", "a lower voltage is better because the current is larger": "A larger current wastes MORE power as heat."},
         hints=["Follow each column from top to bottom.", "Current goes down, and the waste goes down even faster.", "High voltage, small current, little waste."],
         keypoints=[KP("current decreases", "current", "smaller", "lower", "less", "decrease", "falls"), KP("less power wasted", "wasted", "lost", "loss", "waste")]),
    dict(id="e01_led_vs_filament", level=4, lo="1.1c",
         stem=f"The table shows two lamps of the same brightness.\n\n{md_table(['lamp', 'electrical energy in each second / J', 'light energy out each second / J'], [['filament', 60, 3], ['LED', 10, 3]])}\n\nWhy is the LED lamp better?",
         correct="it wastes far less energy as thermal energy to give the same light",
         wrongs={"it gives out more light": "Both give 3 J of light each second; the LED just needs less input.", "it converts all its energy to light": "It converts 3 J of 10 J to light; the rest is still thermal energy.", "it uses a higher voltage": "Voltage is not shown; the data are about energy."},
         hints=["Compare the energy in with the light out for each lamp.", "Where does the rest of the input go?", "The filament lamp wastes 57 J as heat; the LED only 7 J."],
         keypoints=[KP("less energy wasted", "less", "waste", "wasted", "fewer", "lower"), KP("same light output", "same light", "same brightness", "equal light", "3 J")]),
    dict(id="e01_generator_vs_motor", level=4, lo="1.1e",
         stem=f"The table describes two machines.\n\n{md_table(['machine', 'energy in', 'energy out'], [['P', 'kinetic', 'electrical'], ['Q', 'electrical', 'kinetic']])}\n\nWhich machine is the generator in a power station, and what turns it?",
         correct="P; it is turned by the turbine, which is pushed round by steam",
         wrongs={"Q; it is turned by the turbine": "Q takes electrical energy IN: that is a motor.", "P; it is turned by the burning fuel directly": "Burning fuel heats water to make steam; the steam turns the turbine, and the turbine turns the generator.", "Q; it is turned by the steam directly": "Q is a motor, and steam turns the turbine, not the generator directly."},
         hints=["A generator produces electricity from motion.", "Which machine has electrical energy OUT?", "Steam → turbine → generator."],
         keypoints=[KP("P is the generator", "p"), KP("turned by the turbine / steam", "turbine", "steam")]),
    dict(id="e01_power_station_efficiency_reason", level=4, lo="1.1e",
         stem=f"The table shows where the fuel's energy goes in a fossil fuel power station.\n\n{md_table(['where the energy goes', 'percentage'], [['electrical energy to the grid', 35], ['thermal energy in cooling towers and chimney', 60], ['other wasted energy', 5]])}\n\nWhich statement is a correct conclusion?",
         correct="most of the fuel's energy is wasted as thermal energy, but no energy is destroyed",
         wrongs={"65% of the fuel's energy is destroyed": "It is converted to thermal energy, not destroyed.", "the station creates 35% more energy than the fuel has": "The 35% is PART of the fuel's energy.", "the cooling towers add thermal energy to the station": "The cooling towers carry WASTED thermal energy away."},
         hints=["Add up the percentages.", "The total is 100%: energy is conserved.", "The biggest share is thermal energy."],
         keypoints=[KP("most is wasted as thermal", "most", "60", "thermal", "heat", "wasted"), KP("energy is conserved / not destroyed", "conserved", "not destroyed", "cannot be destroyed", "converted", "total", "destroyed")]),
    dict(id="e01_transformer_substation_design", level=4, lo="1.1g",
         stem="Fig. 1 shows the electricity supply chain. A factory wants to use the 400 000 V transmission supply directly to save money on transformers. Why is this a bad idea?",
         fig=lambda rng: G1.transmission(),
         correct="the machines are designed for a much lower voltage, so the supply must be stepped down first",
         wrongs={"the factory would receive less power at high voltage": "High voltage carries the power efficiently; the problem is that appliances need a low voltage.", "the transmission lines carry no energy": "They carry the energy very efficiently.", "400 000 V is too low for machines": "It is far too HIGH; machines run on a few hundred volts."},
         hints=["What voltage do appliances and machines run on?", "Which transformer makes a high voltage lower?", "A step-down transformer is needed."],
         keypoints=[KP("too high / needs lower voltage", "too high", "lower voltage", "low voltage", "dangerous", "damage"), KP("step-down transformer", "step-down", "step down", "transformer", "stepped down")]),
    dict(id="e01_car_braking", level=4, lo="1.1c",
         stem=f"The table shows a car before and after braking to a stop.\n\n{md_table(['stage', 'kinetic energy / kJ', 'temperature of brakes / °C'], [['before braking', 400, 40], ['after stopping', 0, 180]])}\n\nWhat happened to the car's kinetic energy?",
         correct="it was converted mainly to thermal energy in the brakes by friction",
         wrongs={"it was destroyed when the car stopped": "Energy is never destroyed; the hot brakes show where it went.", "it was stored as chemical energy in the fuel": "Braking does not refill the tank.", "it was converted to gravitational potential energy": "The car did not rise."},
         hints=["Energy is conserved: look at the brake temperature.", "Friction between brake pads and wheels.", "Thermal energy."],
         keypoints=[KP("friction in the brakes", "friction", "brake", "rub"), KP("thermal energy", "thermal", "heat", "hot", "warm")]),

    # ------------------------------------------------------------ L5
    dict(id="e01_solar_vs_fossil", level=5, lo="1.1e",
         stem=f"The table compares two ways of generating electricity.\n\n{md_table(['method', 'energy in', 'carbon dioxide produced', 'works at night'], [['fossil fuel station', 'chemical (coal)', 'yes', 'yes'], ['solar panels', 'light', 'no', 'no']])}\n\nWhich statement is the best evaluation?",
         correct="fossil fuel stations supply electricity at any time but produce carbon dioxide; solar panels are cleaner but depend on daylight",
         wrongs={"solar panels are better in every way": "They cannot generate at night.", "fossil fuel stations are better in every way": "They produce carbon dioxide.", "both produce carbon dioxide while generating": "Solar panels do not produce carbon dioxide while generating."},
         hints=["Each method has a strength and a weakness in the table.", "Think about pollution AND reliability.", "Trade-off: clean but daytime only, or any time but polluting."],
         keypoints=[KP("fossil fuels produce carbon dioxide / pollution", "carbon dioxide", "pollut", "greenhouse", "co2"), KP("solar depends on daylight / not at night", "night", "daylight", "sun", "weather", "dark")]),
    dict(id="e01_perpetual_machine", level=5, lo="1.1c",
         stem=f"An inventor claims a machine that, once started, runs forever and powers a lamp with no fuel. The table shows a test.\n\n{md_table(['time / min', 'speed of wheel / rev/min'], [[0, 300], [5, 240], [10, 190], [15, 150]])}\n\nWhy must the claim be false?",
         correct="energy cannot be created, and friction converts the wheel's kinetic energy to thermal energy, so it slows down",
         wrongs={"the wheel is too heavy to keep turning": "Mass is not the issue; a machine cannot output energy it does not receive.", "the lamp uses up the wheel's mass": "Mass is not used up; ENERGY is converted.", "the inventor started it at the wrong speed": "No starting speed can make a machine create energy."},
         hints=["What does the principle of conservation of energy say about creating energy?", "Why does the wheel slow down?", "Friction and the lamp take energy out; nothing puts it in."],
         keypoints=[KP("energy cannot be created", "cannot be created", "not created", "conservation", "no energy in", "no input"), KP("friction / thermal energy", "friction", "thermal", "heat", "lamp uses energy", "energy out")]),
    dict(id="e01_cooking_pot_lid", level=5, lo="1.1b",
         stem=f"A cook heats two identical pots of soup on identical stoves.\n\n{md_table(['pot', 'lid', 'time to boil / min'], [['P', 'on', 8], ['Q', 'off', 12]])}\n\nWhich explanation is best?",
         correct="with the lid off, more thermal energy flows from the hot soup to the cooler air, so more energy is needed before boiling",
         wrongs={"the lid adds thermal energy to the soup": "A lid does not produce energy; it reduces energy leaving.", "the stove gives Q less energy": "The stoves are identical; Q loses more of what it receives.", "the soup in Q is colder to begin with": "The pots and soup are identical at the start."},
         hints=["Both pots receive the same energy per minute.", "Which pot loses more thermal energy to the air?", "The open pot."],
         keypoints=[KP("more energy escapes without a lid", "escape", "lost", "loses", "leaves", "flows out", "to the air", "surroundings"), KP("so it takes longer / needs more energy", "longer", "more energy", "more time", "slower")]),
    dict(id="e01_choose_appliance", level=5, lo="1.1d",
         stem=f"A family wants to cut the energy used by lighting. The table shows their lamps, each used 5 hours a day.\n\n{md_table(['lamp', 'power / W', 'useful light / W'], [['filament', 60, 3], ['LED', 10, 3]])}\n\nWhich statement correctly compares the lamps for one day?",
         correct="the LED converts 50 W less for the same light, saving 50 × 5 × 3600 = 900 000 J a day",
         wrongs={"the LED gives six times more light": "Both give 3 W of useful light.", "the filament lamp saves energy because it is brighter": "They are equally bright; the filament lamp wastes more.", "the LED saves 50 J a day": "The saving is 50 J EVERY SECOND, for 5 hours."},
         hints=["Find the difference in power.", "Multiply by the time in seconds (5 h = 18 000 s).", "50 × 18 000."],
         keypoints=[KP("LED uses less power / wastes less", "less", "lower", "saves", "wastes less"), KP("same light output", "same light", "same brightness", "equal")]),
    dict(id="e01_hydro_pumped", level=5, lo="1.1c",
         stem=f"At night a power company pumps water up to a high lake; in the day the water flows down through a generator. The table shows the energy.\n\n{md_table(['stage', 'energy / GJ'], [['electrical energy used to pump at night', 100], ['gravitational potential energy stored', 80], ['electrical energy generated in the day', 60]])}\n\nWhich statement is correct?",
         correct="40 GJ is converted to thermal energy by friction in the pump, pipes and generator; the total energy is conserved",
         wrongs={"the scheme creates 60 GJ of energy": "It RETURNS 60 of the 100 GJ put in.", "40 GJ of energy is destroyed": "It is converted to thermal energy, not destroyed.", "the water stores 100 GJ": "Only 80 GJ is stored; 20 GJ is wasted while pumping."},
         hints=["Follow the energy: 100 in, 60 out.", "Energy cannot be destroyed, so where is the difference?", "Thermal energy from friction."],
         keypoints=[KP("difference becomes thermal energy / friction", "thermal", "heat", "friction"), KP("energy is conserved", "conserved", "not destroyed", "cannot be destroyed", "total")]),
    dict(id="e01_grid_decision", level=5, lo="1.1f",
         stem=f"A new island town is 50 km from a power station. Two plans are considered.\n\n{md_table(['plan', 'voltage in cable', 'energy reaching town per 100 J sent'], [['P', '11 000 V', '70 J'], ['Q', '275 000 V', '98 J']])}\n\nWhich plan is better, and why?",
         correct="Q, because the higher voltage means a smaller current, so much less energy is wasted as heat in the 50 km cable",
         wrongs={"P, because a lower voltage is safer to transmit": "Safety is managed with insulation and tall pylons; P wastes 30 J of every 100 J.", "P, because it needs no transformers": "Both plans need transformers for the town; P wastes far more energy.", "Q, because the higher voltage pushes more energy into the cable": "The voltage does not add energy; it reduces the current and so the heat loss."},
         hints=["Compare the energy reaching the town.", "Why does the high voltage lose less?", "Smaller current, less heating."],
         keypoints=[KP("smaller current", "current", "smaller", "less current", "lower current"), KP("less energy wasted as heat", "wasted", "lost", "heat", "loss")]),
    dict(id="e01_hot_object_same_temp", level=5, lo="1.1b",
         stem=f"A student says: 'A metal spoon and a wooden spoon have been in the same room for a day. The metal spoon feels colder, so it must be at a lower temperature.' The table shows measurements.\n\n{md_table(['spoon', 'temperature / °C'], [['metal', 25], ['wooden', 25]])}\n\nWhy does the metal spoon feel colder?",
         correct="thermal energy flows faster from the warm hand into the metal, so the hand loses energy quickly",
         wrongs={"the metal spoon is at a lower temperature": "The thermometer shows both at 25 °C.", "cold flows out of the metal into the hand": "'Cold' does not flow; thermal energy flows from the warmer hand into the spoon.", "the wooden spoon produces its own thermal energy": "Wood does not produce energy; it just lets energy flow slowly."},
         hints=["Both spoons are at the same temperature.", "Your hand is warmer than 25 °C: which way does energy flow?", "Metal lets it flow quickly."],
         keypoints=[KP("energy flows from the hand to the spoon", "hand", "from the hand", "out of the hand"), KP("faster through metal", "faster", "quickly", "quicker", "good conductor", "conductor")]),
    dict(id="e01_step_up_at_appliance", level=5, lo="1.1g",
         stem=f"A microwave oven has a transformer inside it. The table shows its voltages.\n\n{md_table(['input from mains / V', 'output to the microwave tube / V'], [[230, 2000]])}\n\nWhich statement is correct?",
         correct="it is a step-up transformer, because some parts of an appliance need a higher voltage than the mains",
         wrongs={"it must be a mistake, because appliances only use step-down transformers": "Some appliances step the voltage UP inside, such as the tube in a microwave oven.", "it is a step-down transformer, because it is inside an appliance": "The voltage RISES from 230 V to 2000 V, so it steps up.", "it is a step-up transformer, so the oven uses more energy than the mains supplies": "A transformer cannot create energy; it only changes the voltage."},
         hints=["Compare 230 V with 2000 V.", "Is that an increase or a decrease?", "Step-up, inside the appliance."],
         keypoints=[KP("step-up", "step-up", "step up", "steps up", "increase", "raise", "higher"), KP("the tube needs a higher voltage", "need", "higher voltage", "2000", "tube", "high voltage")]),
]

register_explain(EXPLAIN, chapter=1)
