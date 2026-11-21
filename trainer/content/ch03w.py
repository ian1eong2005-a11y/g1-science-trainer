"""Ch 3 Wave: extra calculation / data templates adapted from the Topic 1.3 assignments, Revision 1 and the two Checkpoints,
plus explanation items from the same worksheets. Numbers are varied on every serve."""
from .. import sketches_g1 as G1
from .base import fmt, md_table, nice, numeric_options, pick, register_explain, template, text_options

KP = lambda label, *phr: {"label": label, "any": list(phr)}
SRC = "_Adapted from the QTSS Topic 1.3 worksheets._"
EM_ORDER = ["radio waves", "microwaves", "infrared", "visible light", "ultraviolet", "X-rays", "gamma rays"]


# ---------------------------------------------------------------- L1
@template("c03w_small_amplitude_read", chapter=3, level=1, lo="1.3c")
def small_amplitude_read(rng):
    A = nice(rng, 0.5, 1.0, 1.5)
    lam = nice(rng, 2, 3, 4)
    opts, key, mis = numeric_options(rng, A, [
        (2 * A, "Crest to trough is twice the amplitude."),
        (lam, "That is the wavelength."),
        (lam / 2, "That is half a wavelength, not the amplitude."),
    ], unit="cm", sf=2)
    return dict(
        stem="Fig. 1 shows a wave. What is the amplitude of the wave?",
        figure=G1.wave(A, lam, show="amplitude"),
        options=opts, key=key, misconceptions=mis,
        formula="amplitude = maximum displacement from the rest position",
        working=[f"crest height above the rest line = {A} cm", f"amplitude = **{A} cm**", SRC],
        hints=["Find the dashed rest line.", "Measure up to the top of a crest.", "Read the vertical scale."],
    )


@template("c03w_osc_in_5s", chapter=3, level=1, lo="1.3c")
def osc_in_5s(rng):
    f = nice(rng, 3, 4, 5, 6)
    t = nice(rng, 4, 5, 8)
    n = f * t
    opts, key, mis = numeric_options(rng, n, [
        (f / t, "Multiply the frequency by the time; do not divide."),
        (f, "That is the number in ONE second."),
        (t, "That is the time; multiply by the frequency."),
    ], unit="oscillations", sf=3)
    return dict(
        stem=f"A wave has the frequency shown.\n\n{md_table(['frequency / Hz'], [[f]])}\n\nHow many oscillations (complete waves) does it make in **{t} seconds**?",
        options=opts, key=key, misconceptions=mis,
        formula="number of oscillations = frequency × time",
        working=[f"{f} per second × {t} s", f"= **{n} oscillations**", SRC],
        hints=[f"{f} Hz means {f} oscillations each second.", "Multiply by the number of seconds.", f"{f} × {t}."],
    )


# ---------------------------------------------------------------- L2
@template("c03w_two_cycles_time", chapter=3, level=2, lo="1.3c")
def two_cycles_time(rng):
    n = nice(rng, 2, 3, 4, 8)
    t = nice(rng, 0.5, 1, 2)
    f = n / t
    opts, key, mis = numeric_options(rng, f, [
        (n * t, "Frequency = waves ÷ time; do not multiply."),
        (t / n, "Upside down: waves ÷ seconds."),
        (n, "That is the number of waves; divide by the time."),
    ], unit="Hz", sf=2)
    return dict(
        stem=f"A wave is drawn and timed.\n\n{md_table(['complete waves (cycles)', 'time taken / s'], [[n, t]])}\n\nWhat is the frequency of the wave?",
        options=opts, key=key, misconceptions=mis,
        formula="frequency = number of complete waves ÷ time (s)",
        working=[f"f = {n} ÷ {t}", f"= **{fmt(f)} Hz**", SRC],
        hints=["Frequency is waves per second.", f"{n} waves in {t} s.", f"{n} ÷ {t}."],
    )


@template("c03w_speaker_per_minute", chapter=3, level=2, lo="1.3c")
def speaker_per_minute(rng):
    n = nice(rng, 30, 45, 90, 150)
    f = n / 60
    opts, key, mis = numeric_options(rng, f, [
        (n, "Frequency is per SECOND: divide by 60."),
        (60 / n, "Upside down: oscillations ÷ seconds."),
        (n / 100, "1 minute = 60 s, not 100 s."),
    ], unit="Hz", sf=2)
    return dict(
        stem=f"A speaker cone vibrates.\n\n{md_table(['oscillations', 'time'], [[n, '1 minute']])}\n\nCalculate the frequency of the sound wave.",
        options=opts, key=key, misconceptions=mis,
        formula="frequency = oscillations ÷ time (s);  1 min = 60 s",
        working=[f"60 s → {n} oscillations", f"f = {n} ÷ 60 = **{fmt(f)} Hz**", SRC],
        hints=["Change the minute to seconds.", "Oscillations per second.", f"{n} ÷ 60."],
    )


@template("c03w_distance_d_wavelength", chapter=3, level=2, lo="1.3c")
def distance_d_wavelength(rng):
    n = nice(rng, 2, 3, 4, 5)
    lam = nice(rng, 2, 3, 4, 6)
    D = n * lam
    opts, key, mis = numeric_options(rng, lam, [
        (D, "D covers several waves; divide by the number of waves."),
        (D * n, "Divide, do not multiply."),
        (D / (2 * n), "One wavelength is one COMPLETE wave, crest to crest."),
    ], unit="cm", sf=3)
    return dict(
        stem=f"A wave travels along a rope. A distance D is marked on the rope.\n\n{md_table(['distance D / cm', 'complete waves within D'], [[D, n]])}\n\nCalculate the wavelength of the wave.",
        options=opts, key=key, misconceptions=mis,
        formula="wavelength = D ÷ number of complete waves",
        working=[f"wavelength = {D} ÷ {n}", f"= **{lam} cm**", SRC],
        hints=["How many waves fit into D?", "Share D between them.", f"{D} ÷ {n}."],
    )


@template("c03w_pq_quantities", chapter=3, level=2, lo="1.3c")
def pq_quantities(rng):
    A = nice(rng, 2, 3)
    lam = nice(rng, 8, 10, 12)
    ans = "P is the amplitude and Q is the wavelength"
    opts, key, mis = text_options(rng, ans, {
        "P is the amplitude and Q is half the wavelength": "Q spans crest to the NEXT crest, a full wavelength.",
        "P is half the amplitude and Q is the wavelength": "P goes from the rest line to a crest, the full amplitude.",
        "P is the wavelength and Q is the amplitude": "P is vertical (a displacement); Q is horizontal (a distance along the wave).",
    })
    return dict(
        stem="Fig. 1 shows a wave with two distances marked, P and Q. Which quantities are shown by P and Q?",
        figure=G1.wave(A, lam, show="both"),
        options=opts, key=key, misconceptions=mis,
        formula="amplitude: rest position to crest;  wavelength: crest to the next crest",
        working=["P: vertical, rest line to crest = amplitude", "Q: horizontal, crest to next crest = wavelength", SRC],
        hints=["Which arrow is vertical?", "Vertical from the rest line = amplitude.", "Crest to crest = wavelength."],
    )


# ---------------------------------------------------------------- L3
@template("c03w_three_waves_table", chapter=3, level=3, lo="1.3c")
def three_waves_table(rng):
    a1 = nice(rng, 1, 2)
    rows = [["1", a1, 4], ["2", 2 * a1, 4], ["3", a1, 6]]
    ans = "waves 1 and 2 have the same wavelength; wave 2 has twice the amplitude of wave 1"
    opts, key, mis = text_options(rng, ans, {
        "waves 1 and 3 have the same wavelength; wave 3 has twice the amplitude of wave 1": "Waves 1 and 3 have the same AMPLITUDE but different wavelengths.",
        "waves 2 and 3 have the same amplitude; wave 1 has the longest wavelength": "Wave 3 has the longest wavelength and wave 2 the largest amplitude.",
        "all three waves have the same amplitude": "Wave 2's amplitude is double the others'.",
    })
    return dict(
        stem=f"Three waves are drawn on the same scale.\n\n{md_table(['wave', 'amplitude / cm', 'wavelength / cm'], rows)}\n\nWhich statement is correct?",
        options=opts, key=key, misconceptions=mis,
        formula="compare amplitudes and wavelengths column by column",
        working=[f"wavelengths: 1 and 2 both 4 cm; amplitudes: wave 2 ({2 * a1}) is twice wave 1 ({a1})", f"**{ans}**", SRC],
        hints=["Compare the wavelength column first.", "Then the amplitude column.", "Which is double which?"],
    )


@template("c03w_wavelength_range_use", chapter=3, level=3, lo="1.3d")
def wavelength_range_use(rng):
    bands = [("radio waves", "more than 1 m", "radio and television broadcasts"), ("microwaves", "1 mm to 1 m", "satellite communication and ovens"),
             ("infrared", "700 nm to 1 mm", "remote-controlled devices"), ("ultraviolet", "10 nm to 400 nm", "sunbeds and sterilisation"),
             ("X-rays", "0.01 nm to 10 nm", "radiological applications")]
    pick_i = rng.randrange(len(bands))
    name, rng_txt, use = bands[pick_i]
    others = [b for i, b in enumerate(bands) if i != pick_i]
    rng.shuffle(others)
    opts, key, mis = text_options(rng, use, {o[2]: f"That is the use of {o[0]}, whose wavelengths are {o[1]}." for o in others[:3]})
    return dict(
        stem=f"The table shows the wavelengths of some waves.\n\n{md_table(['wave', 'wavelength'], [[b[0], b[1]] for b in bands])}\n\nWhat are waves with wavelengths in the range **{rng_txt}** used for?",
        options=opts, key=key, misconceptions=mis,
        formula="each region of the electromagnetic spectrum has its own wavelength range and uses",
        working=[f"{rng_txt} → {name}", f"{name} are used for **{use}**", SRC],
        hints=["Find the wavelength range in the table.", f"It belongs to {name}.", f"What are {name} used for?"],
    )


@template("c03w_em_gaps_pqr", chapter=3, level=3, lo="1.3d")
def em_gaps_pqr(rng):
    idx = sorted(rng.sample(range(1, 6), 3))
    shown = [w if i not in idx else "PQR"[idx.index(i)] for i, w in enumerate(EM_ORDER)]
    ans = ", ".join(EM_ORDER[i] for i in idx)
    wrongs = {}
    rev = ", ".join(EM_ORDER[i] for i in reversed(idx))
    wrongs[rev] = "The order is reversed; follow the spectrum from radio waves to gamma rays."
    alt = [i for i in range(1, 6) if i not in idx]
    w2 = ", ".join(EM_ORDER[i] for i in [alt[0]] + idx[1:])
    wrongs[w2] = f"P is between {EM_ORDER[idx[0] - 1]} and {EM_ORDER[idx[0] + 1]}."
    w3 = ", ".join(EM_ORDER[i] for i in idx[:2] + [alt[-1]])
    wrongs[w3] = f"R is between {EM_ORDER[idx[2] - 1]} and {EM_ORDER[idx[2] + 1]}."
    opts, key, mis = text_options(rng, ans, wrongs)
    return dict(
        stem=f"The table shows the electromagnetic spectrum in order of increasing frequency, with three gaps.\n\n{md_table(['order'], [[w] for w in shown])}\n\nWhat are P, Q and R?",
        options=opts, key=key, misconceptions=mis,
        formula="radio, microwaves, infrared, visible light, ultraviolet, X-rays, gamma rays (increasing frequency)",
        working=["the full order is " + ", ".join(EM_ORDER), f"**P, Q, R = {ans}**", SRC],
        hints=["Learn the order: radio, micro, infrared, visible, UV, X, gamma.", "Fill each gap from its neighbours.", "Check the direction: radio first."],
    )


@template("c03w_freq_from_crests_passing", chapter=3, level=3, lo="1.3c")
def freq_from_crests_passing(rng):
    n = nice(rng, 4, 6, 8, 12)
    t = nice(rng, 1, 2, 4)
    D = nice(rng, 8, 12, 16)
    k = nice(rng, 2, 4)
    f = n / t
    lam = D / k
    wf = n * t if t != 1 else n / 2
    opts, key, mis = text_options(rng, f"frequency {fmt(f)} Hz, wavelength {fmt(lam)} cm", {
        f"frequency {fmt(wf)} Hz, wavelength {fmt(lam)} cm": "Frequency = crests passing ÷ time.",
        f"frequency {fmt(f)} Hz, wavelength {fmt(D)} cm": f"D contains {k} waves, so divide by {k}.",
        f"frequency {fmt(f)} Hz, wavelength {fmt(lam / 2)} cm": "A wavelength is one COMPLETE wave.",
    })
    return dict(
        stem=f"A wave travels along a rope past point X.\n\n{md_table(['crests passing X', 'time / s', 'distance D / cm', 'complete waves in D'], [[n, t, D, k]])}\n\nWhat are the frequency and the wavelength?",
        options=opts, key=key, misconceptions=mis,
        formula="frequency = crests passing ÷ time;  wavelength = D ÷ number of waves in D",
        working=[f"f = {n} ÷ {t} = {fmt(f)} Hz", f"wavelength = {D} ÷ {k} = {fmt(lam)} cm", SRC],
        hints=["Frequency: crests per second.", "Wavelength: D shared between the waves.", f"{n} ÷ {t} and {D} ÷ {k}."],
    )


# ---------------------------------------------------------------- L4
@template("c03w_large_amp_high_freq", chapter=3, level=4, lo="1.3c")
def large_amp_high_freq(rng):
    rows = [["P", 2, 2], ["Q", 2, 8], ["R", 6, 2], ["S", 6, 8]]
    rng.shuffle(rows)
    big = [r for r in rows if r[1] == 6 and r[2] == 8][0][0]
    opts, key, mis = text_options(rng, big, {r[0]: f"{r[0]} has amplitude {r[1]} cm and frequency {r[2]} Hz." for r in rows if r[0] != big})
    return dict(
        stem=f"Four sound waves are measured.\n\n{md_table(['wave', 'amplitude / cm', 'frequency / Hz'], rows)}\n\nWhich wave has a large amplitude AND a high frequency?",
        options=opts, key=key, misconceptions=mis,
        formula="amplitude = size of the vibration;  frequency = vibrations per second",
        working=["largest amplitude = 6 cm; highest frequency = 8 Hz", f"both: **{big}**", SRC],
        hints=["Find the rows with the largest amplitude.", "Of those, which has the highest frequency?", "One wave has both."],
    )


@template("c03w_ripple_tank_ruler", chapter=3, level=4, lo="1.3c")
def ripple_tank_ruler(rng):
    pos = pick(rng, ["vertically in the water", "horizontally along the surface"])
    ans = "the amplitude of the wave" if pos.startswith("vert") else "the wavelength of the wave"
    other = "the wavelength of the wave" if pos.startswith("vert") else "the amplitude of the wave"
    opts, key, mis = text_options(rng, ans, {
        other: f"A ruler held {pos} measures {'up-and-down' if pos.startswith('vert') else 'along-the-surface'} distances only.",
        "the frequency of the wave": "Frequency needs a timer, not a ruler.",
        "the speed of the wave": "Speed needs a distance AND a time.",
    })
    return dict(
        stem=f"A student places a ruler **{pos}** in a ripple tank with waves on it.\n\n{md_table(['instrument', 'position'], [['ruler', pos]])}\n\nWhat can be measured with the ruler in this position?",
        options=opts, key=key, misconceptions=mis,
        formula="amplitude is measured vertically (rest position to crest); wavelength horizontally (crest to crest)",
        working=[f"{pos} → {'vertical' if pos.startswith('vert') else 'horizontal'} distances", f"**{ans}**", SRC],
        hints=["Which direction does the ruler measure in?", "Amplitude is vertical; wavelength is horizontal.", "Pick the matching quantity."],
    )


@template("c03w_incorrect_classification", chapter=3, level=4, lo="1.3d")
def incorrect_classification(rng):
    rows = [["gamma rays", "medical treatment"], ["ultraviolet", "artificial tanning"], ["microwaves", "cooking food in microwave ovens"], ["infrared", "sterilisation of medical equipment"]]
    rng.shuffle(rows)
    bad = "infrared"
    opts, key, mis = text_options(rng, f"{bad}: sterilisation of medical equipment", {
        f"{r[0]}: {r[1]}": f"{r[0]} really are used for {r[1]}." for r in rows if r[0] != bad
    })
    return dict(
        stem=f"The table matches waves with uses.\n\n{md_table(['wave', 'use'], rows)}\n\nWhich row is INCORRECT?",
        options=opts, key=key, misconceptions=mis,
        formula="sterilisation uses ultraviolet; infrared is used in remote controls (and heating)",
        working=["sterilising medical equipment is a use of ULTRAVIOLET", f"**{bad}: sterilisation** is wrong", SRC],
        hints=["Which wave sterilises equipment?", "Ultraviolet.", "So the infrared row is wrong."],
    )


# ---------------------------------------------------------------- L5
@template("c03w_sketch_wave_check", chapter=3, level=5, lo="1.3c")
def sketch_wave_check(rng):
    A = nice(rng, 2, 3)
    lam = nice(rng, 4, 6)
    t = nice(rng, 0.5, 1)
    f = 2 / t
    ans = f"height {A} cm above and below the rest line, repeating every {lam} cm, frequency {fmt(f)} Hz"
    opts, key, mis = text_options(rng, ans, {
        f"height {2 * A} cm above and below the rest line, repeating every {lam} cm, frequency {fmt(f)} Hz": "The amplitude is measured from the rest line, so the crest is only {0} cm above it.".format(A),
        f"height {A} cm above and below the rest line, repeating every {lam / 2:g} cm, frequency {fmt(f)} Hz": "One cycle (crest and trough) is a full wavelength.",
        f"height {A} cm above and below the rest line, repeating every {lam} cm, frequency {fmt(t / 2)} Hz": "Frequency = cycles ÷ time = 2 ÷ {0}, not time ÷ cycles.".format(t),
    })
    return dict(
        stem=f"A student must sketch two cycles of a wave and find its frequency.\n\n{md_table(['amplitude / cm', 'wavelength / cm', 'time for the two cycles / s'], [[A, lam, t]])}\n\nWhich description of the correct sketch and frequency is right?",
        options=opts, key=key, misconceptions=mis,
        formula="amplitude = rest line to crest;  wavelength = length of one cycle;  frequency = cycles ÷ time",
        working=[f"crests {A} cm above the rest line, troughs {A} cm below; one cycle every {lam} cm", f"frequency = 2 ÷ {t} = {fmt(f)} Hz", SRC],
        hints=["Amplitude is from the rest line, not crest to trough.", "Each cycle is one wavelength long.", "2 cycles ÷ time."],
    )


@template("c03w_cork_bob_count", chapter=3, level=5, lo="1.3b")
def cork_bob_count(rng):
    n = nice(rng, 10, 12, 20)
    t = nice(rng, 5, 10)
    f = n / t
    ans = f"it bobs up and down {fmt(f)} times a second but does not travel across the pond, because the wave carries energy, not water"
    opts, key, mis = text_options(rng, ans, {
        f"it travels across the pond at {fmt(f)} m/s with the wave": "The cork stays in place; only energy travels.",
        f"it bobs {fmt(n * t)} times a second": "Frequency = bobs ÷ time.",
        "it sinks because the wave pushes it down": "The wave lifts and lowers it; the cork floats."},
    )
    return dict(
        stem=f"A cork floats on a pond. Waves pass it.\n\n{md_table(['times the cork bobs up and down', 'time / s', "change in position across the pond"], [[n, t, 'none']])}\n\nWhat does the cork do, and what does this show?",
        options=opts, key=key, misconceptions=mis,
        formula="waves transfer energy without transferring the medium; frequency = oscillations ÷ time",
        working=[f"frequency = {n} ÷ {t} = {fmt(f)} Hz", f"**{ans}**", SRC],
        hints=["Does the cork move along with the wave?", "What travels along the pond?", "Energy, not water."],
    )


# ================================================================ EXPLANATION (worksheet items)
EXPLAIN = [
    dict(id="e03w_fill_blanks_terms", level=1, lo="1.3c",
         stem=f"The table gives descriptions.\n\n{md_table(['description', 'term'], [['the number of waves passing a point each second', 'P'], ['the distance from a point on one wave to the same point on the next', 'Q'], ['the maximum distance of a point from its undisturbed position', 'R']])}\n\nWhat are P, Q and R?",
         correct="P frequency, Q wavelength, R amplitude",
         wrongs={"P amplitude, Q wavelength, R frequency": "Waves per second is the FREQUENCY; maximum distance from rest is the AMPLITUDE.", "P frequency, Q amplitude, R wavelength": "The distance between matching points on neighbouring waves is the WAVELENGTH.", "P wavelength, Q frequency, R amplitude": "Per second → frequency; distance along the wave → wavelength."},
         hints=["Per second → frequency.", "Along the wave → wavelength.", "Height from rest → amplitude."],
         working=["Correct answer: **P frequency, Q wavelength, R amplitude**", SRC]),
    dict(id="e03w_em_list_components", level=2, lo="1.3d",
         stem=f"The table lists groups of waves.\n\n{md_table(['group', 'waves'], [['P', 'water waves, light waves, infrared'], ['Q', 'infrared, microwaves, sound'], ['R', 'gamma rays, X-rays, ultraviolet'], ['S', 'sound, light waves, radio waves']])}\n\nWhich group contains ONLY members of the electromagnetic spectrum?",
         correct="R",
         wrongs={"P": "Water waves are not electromagnetic.", "Q": "Sound is not electromagnetic.", "S": "Sound is not electromagnetic."},
         hints=["Sound and water waves are not electromagnetic.", "Which group has neither?", "The group of gamma, X and UV."],
         working=["Correct answer: **R**", SRC]),
    dict(id="e03w_ball_on_pond", level=5, lo="1.3b",
         stem=f"A rubber ball floats on a large pond. A water wave travels from left to right.\n\n{md_table(['observation', 'wave moving left to right'], [['ball position across the pond', 'unchanged'], ['ball height', 'rises and falls']])}\n\nA student says 'the wave must carry no energy, because the ball did not move along'. Explain what is wrong with this.",
         correct="the ball moved up and down, so energy did reach it; waves transfer energy along the pond without carrying the water (or the ball) along",
         wrongs={"the student is right because the ball stayed where it was": "The ball rose and fell, which needs energy from the wave.", "the wave carried the water along but the ball was too heavy": "Water in a wave only moves up and down about its rest position.", "energy was lost because the ball absorbed it": "The ball's bobbing shows the energy arriving; it does not show a loss."},
         hints=["Did the ball move at all?", "Up-and-down motion needs energy.", "What travels: energy or water?"],
         keypoints=[KP("ball moves up and down = energy received", "up and down", "rise", "bob", "move", "energy"), KP("water / medium not carried along", "water", "medium", "not carried", "stays", "same place")],
         working=["Correct answer: **the ball moved up and down, so energy did reach it; waves transfer energy along the pond without carrying the water (or the ball) along**", SRC]),
]

register_explain(EXPLAIN, chapter=3)
