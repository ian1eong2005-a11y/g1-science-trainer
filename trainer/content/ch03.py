"""Ch 3 Wave (K123 topic 1.3): 20 calculation / data templates and 40 explanation items.
lo codes: 1.3a waves made by vibrations (ropes, springs), 1.3b waves transfer energy, 1.3c amplitude, frequency, wavelength,
1.3d uses of radio waves, microwaves, infrared, light, ultraviolet, X-rays, gamma rays."""
from .. import sketches as S, sketches_g1 as G1
from .base import fmt, md_table, nice, numeric_options, pick, register_explain, template, text_options

KP = lambda label, *phr: {"label": label, "any": list(phr)}

EM = [("radio waves", "radio and television broadcasts"), ("microwaves", "microwave ovens and satellite communication"),
      ("infrared", "remote controls for televisions"), ("light", "optical fibres for telecommunication"),
      ("ultraviolet", "sterilising equipment and sunbeds"), ("X-rays", "photographing bones and checking welds in engineering"),
      ("gamma rays", "treating cancer in medicine")]
T_EM = md_table(["type of wave", "example of use"], [[a, b] for a, b in EM])


# ================================================================ CALCULATION / DATA
# ---------------------------------------------------------------- L1
@template("c03_read_amplitude", chapter=3, level=1, lo="1.3c")
def read_amplitude(rng):
    A = nice(rng, 2, 3, 4, 5)
    lam = nice(rng, 8, 10, 12)
    opts, key, mis = numeric_options(rng, A, [
        (2 * A, "That is the distance from crest to trough. The amplitude is measured from the REST position to the crest."),
        (lam, "That is the wavelength (crest to crest), not the amplitude."),
        (A / 2, "Read the height of the crest above the dashed rest line again."),
    ], unit="cm", sf=2)
    return dict(
        stem="Fig. 1 shows a wave on a rope. The dashed line is the rest position. What is the amplitude of the wave?",
        figure=G1.wave(A, lam, show="amplitude"),
        options=opts, key=key, misconceptions=mis,
        formula="amplitude = maximum displacement from the rest position",
        working=[f"the crest is {A} cm above the rest line", f"amplitude = **{A} cm**"],
        hints=["Find the dashed rest line.", "How high is the top of a crest above it? (Arrow P.)", "Read the scale on the vertical axis."],
    )


@template("c03_read_wavelength", chapter=3, level=1, lo="1.3c")
def read_wavelength(rng):
    A = nice(rng, 2, 3, 4)
    lam = nice(rng, 6, 8, 10, 12, 16)
    opts, key, mis = numeric_options(rng, lam, [
        (lam / 2, "That is crest to trough. The wavelength is from one crest to the NEXT crest."),
        (A, "That is the amplitude, not the wavelength."),
        (2 * lam, "That is two whole waves. Measure crest to the next crest only."),
    ], unit="cm", sf=2)
    return dict(
        stem="Fig. 1 shows a wave on a rope. What is the wavelength of the wave?",
        figure=G1.wave(A, lam, show="wavelength"),
        options=opts, key=key, misconceptions=mis,
        formula="wavelength = distance from one crest to the next crest (one complete wave)",
        working=[f"crest to next crest (arrow Q) = {lam} cm", f"wavelength = **{lam} cm**"],
        hints=["Arrow Q goes from one crest to the next.", "Read it off the horizontal scale.", "Read where Q starts and ends on the distance axis."],
    )


@template("c03_frequency_count", chapter=3, level=1, lo="1.3c")
def frequency_count(rng):
    n = nice(rng, 10, 20, 30, 40, 60)
    t = nice(rng, 5, 10, 20)
    f = n / t
    opts, key, mis = numeric_options(rng, f, [
        (n * t, "You multiplied. Frequency = number of waves ÷ time."),
        (t / n, "Upside down: waves ÷ seconds."),
        (n, "That is the total number of waves; divide by the time to get waves per second."),
    ], unit="Hz", sf=2)
    return dict(
        stem=f"A student shakes a rope and counts the waves.\n\n{md_table(['waves produced', 'time taken / s'], [[n, t]])}\n\nWhat is the frequency of the wave?",
        options=opts, key=key, misconceptions=mis,
        formula="frequency = number of waves produced ÷ time taken   (Hz = waves per second)",
        working=[f"frequency = {n} ÷ {t}", f"= **{fmt(f)} Hz**"],
        hints=["Frequency is the number of waves each second.", "Divide the number of waves by the time.", f"{n} ÷ {t}."],
    )


@template("c03_waves_in_time", chapter=3, level=1, lo="1.3c")
def waves_in_time(rng):
    f = nice(rng, 2, 3, 4, 5)
    t = nice(rng, 5, 10, 15, 20)
    n = f * t
    opts, key, mis = numeric_options(rng, n, [
        (f, "That is the number of waves in ONE second. Multiply by the number of seconds."),
        (t / f, "You divided. Waves = frequency × time."),
        (f + t, "You added. Waves = frequency × time."),
    ], unit="waves", sf=3)
    return dict(
        stem=f"A wave has the frequency shown.\n\n{md_table(['frequency / Hz', 'time / s'], [[f, t]])}\n\nHow many complete waves are produced in this time?",
        options=opts, key=key, misconceptions=mis,
        formula="number of waves = frequency × time",
        working=[f"{f} waves each second for {t} s", f"= {f} × {t} = **{n} waves**"],
        hints=[f"{f} Hz means {f} waves every second.", "Multiply by the number of seconds.", f"{f} × {t}."],
    )


# ---------------------------------------------------------------- L2
@template("c03_frequency_minute", chapter=3, level=2, lo="1.3c")
def frequency_minute(rng):
    n = nice(rng, 120, 180, 240, 300)
    f = n / 60
    opts, key, mis = numeric_options(rng, f, [
        (n, "Frequency is waves per SECOND; change the minute into 60 s."),
        (n / 100, "1 minute = 60 s, not 100 s."),
        (60 / n, "Upside down: waves ÷ seconds."),
    ], unit="Hz", sf=2)
    return dict(
        stem=f"A buoy bobs up and down on sea waves.\n\n{md_table(['waves passing the buoy', 'time'], [[n, '1 minute']])}\n\nWhat is the frequency of the waves?",
        options=opts, key=key, misconceptions=mis,
        formula="frequency = waves ÷ time in seconds;  1 min = 60 s",
        working=[f"time = 60 s", f"frequency = {n} ÷ 60 = **{fmt(f)} Hz**"],
        hints=["Hertz means waves per second.", "Change the minute to seconds.", f"{n} ÷ 60."],
    )


@template("c03_wavelength_from_length", chapter=3, level=2, lo="1.3c")
def wavelength_from_length(rng):
    n = nice(rng, 2, 3, 4, 5)
    lam = nice(rng, 20, 30, 40, 50)
    L = n * lam
    opts, key, mis = numeric_options(rng, lam, [
        (L, "That is the whole length of the rope; it holds several waves."),
        (L * n, "Divide the length by the number of waves; do not multiply."),
        (lam / 2, "One wavelength is one COMPLETE wave (crest and trough)."),
    ], unit="cm", sf=3)
    return dict(
        stem=f"A rope of the length shown has the number of complete waves shown on it.\n\n{md_table(['length of rope / cm', 'complete waves on the rope'], [[L, n]])}\n\nWhat is the wavelength?",
        options=opts, key=key, misconceptions=mis,
        formula="wavelength = length ÷ number of complete waves",
        working=[f"wavelength = {L} ÷ {n}", f"= **{lam} cm**"],
        hints=["One wavelength = one complete wave.", "Share the length between the waves.", f"{L} ÷ {n}."],
    )


@template("c03_amplitude_crest_trough", chapter=3, level=2, lo="1.3c")
def amplitude_crest_trough(rng):
    d = nice(rng, 4, 6, 8, 10, 12)
    A = d / 2
    opts, key, mis = numeric_options(rng, A, [
        (d, "Crest to trough is TWICE the amplitude."),
        (d * 2, "Amplitude is half of the crest-to-trough distance, not double."),
        (d / 4, "Halve the crest-to-trough distance once only."),
    ], unit="cm", sf=2)
    return dict(
        stem=f"A student measures a wave on a spring.\n\n{md_table(['distance from the top of a crest to the bottom of a trough / cm'], [[d]])}\n\nWhat is the amplitude of the wave?",
        options=opts, key=key, misconceptions=mis,
        formula="amplitude = (crest-to-trough distance) ÷ 2",
        working=["the rest position is halfway between crest and trough", f"amplitude = {d} ÷ 2 = **{fmt(A)} cm**"],
        hints=["Amplitude is measured from the rest position.", "Where is the rest position between crest and trough?", "Halfway: divide by 2."],
    )


@template("c03_khz_to_hz", chapter=3, level=2, lo="1.3c")
def khz_to_hz(rng):
    fk = nice(rng, 2, 5, 20, 50)
    t = nice(rng, 2, 3, 5)
    n = fk * 1000 * t
    opts, key, mis = numeric_options(rng, n, [
        (fk * t, "1 kHz = 1000 Hz. Change kHz to Hz first."),
        (fk * 100 * t, "1 kHz = 1000 Hz, not 100 Hz."),
        (fk * 1000 / t, "Multiply by the time; do not divide."),
    ], unit="waves", sf=3)
    return dict(
        stem=f"A sound wave has the frequency shown.\n\n{md_table(['frequency', 'time'], [[f'{fk} kHz', f'{t} s']])}\n\nHow many complete waves are produced in this time? (1 kHz = 1000 Hz)",
        options=opts, key=key, misconceptions=mis,
        formula="number of waves = frequency (Hz) × time (s);  1 kHz = 1000 Hz",
        working=[f"{fk} kHz = {fk * 1000} Hz", f"waves = {fk * 1000} × {t} = **{n}**"],
        hints=["Change kHz to Hz.", f"{fk} kHz = {fk * 1000} Hz.", f"{fk * 1000} × {t}."],
    )


# ---------------------------------------------------------------- L3
@template("c03_compare_two_waves_table", chapter=3, level=3, lo="1.3c")
def compare_two_waves_table(rng):
    A1, A2 = nice(rng, 2, 3), nice(rng, 4, 5, 6)
    f1, f2 = nice(rng, 2, 3), nice(rng, 4, 5, 6)
    lam1, lam2 = nice(rng, 20, 30), nice(rng, 8, 10, 12)
    ans = "Q has the larger amplitude, the higher frequency and the shorter wavelength"
    opts, key, mis = text_options(rng, ans, {
        "P has the larger amplitude, the higher frequency and the longer wavelength": "Read each row: P's amplitude and frequency are smaller.",
        "Q has the larger amplitude, the lower frequency and the shorter wavelength": "Q's frequency is the HIGHER number.",
        "P and Q have the same frequency because they are on the same rope": "The frequencies in the table differ.",
    })
    return dict(
        stem=f"Two waves are sent along the same rope at different times.\n\n{md_table(['wave', 'amplitude / cm', 'frequency / Hz', 'wavelength / cm'], [['P', A1, f1, lam1], ['Q', A2, f2, lam2]])}\n\nWhich statement is correct?",
        options=opts, key=key, misconceptions=mis,
        formula="amplitude = height of crest above rest; frequency = waves per second; wavelength = crest-to-crest distance",
        working=[f"amplitude: Q ({A2}) > P ({A1});  frequency: Q ({f2}) > P ({f1});  wavelength: Q ({lam2}) < P ({lam1})", f"so: **{ans}**"],
        hints=["Compare one column at a time.", "Bigger number = larger amplitude / higher frequency / longer wavelength.", "Q wins on amplitude and frequency, P on wavelength."],
    )


@template("c03_identify_pq_arrows", chapter=3, level=3, lo="1.3c")
def identify_pq_arrows(rng):
    A = nice(rng, 2, 3, 4)
    lam = nice(rng, 8, 10, 12)
    opts, key, mis = text_options(rng, f"P = amplitude = {A} cm, Q = wavelength = {lam} cm", {
        f"P = wavelength = {A} cm, Q = amplitude = {lam} cm": "P is a vertical arrow from the rest line to a crest: that is the amplitude.",
        f"P = amplitude = {2 * A} cm, Q = wavelength = {lam} cm": f"P goes from the REST line to the crest, {A} cm, not crest to trough.",
        f"P = amplitude = {A} cm, Q = wavelength = {lam / 2:g} cm": "Q spans a whole wave, crest to the next crest.",
    })
    return dict(
        stem="Fig. 1 shows a wave on a rope with two arrows P and Q. What do P and Q show, and what are their values?",
        figure=G1.wave(A, lam, show="both"),
        options=opts, key=key, misconceptions=mis,
        formula="amplitude: rest position to crest (vertical); wavelength: crest to next crest (horizontal)",
        working=[f"P is vertical, rest line to crest: amplitude = {A} cm", f"Q is horizontal, crest to next crest: wavelength = {lam} cm"],
        hints=["Which arrow is vertical and which is horizontal?", "Vertical from the rest line = amplitude.", "Read both scales."],
    )


@template("c03_waves_passing_point", chapter=3, level=3, lo="1.3c")
def waves_passing_point(rng):
    f = nice(rng, 0.5, 2, 2.5, 4)
    m = nice(rng, 1, 2, 3)
    n = f * m * 60
    opts, key, mis = numeric_options(rng, n, [
        (f * m, "The time must be in seconds: 1 min = 60 s."),
        (f * m * 100, "1 minute = 60 s, not 100 s."),
        (m * 60 / f, "Multiply frequency by time; do not divide."),
    ], unit="waves", sf=3)
    return dict(
        stem=f"Water waves pass a post at the frequency shown.\n\n{md_table(['frequency / Hz', 'time'], [[f, f'{m} min']])}\n\nHow many waves pass the post in this time?",
        options=opts, key=key, misconceptions=mis,
        formula="number of waves = frequency × time (s);  1 min = 60 s",
        working=[f"time = {m} × 60 = {m * 60} s", f"waves = {fmt(f)} × {m * 60} = **{fmt(n)}**"],
        hints=["Change the minutes to seconds.", f"{m} min = {m * 60} s.", f"{fmt(f)} × {m * 60}."],
    )


@template("c03_em_order_table", chapter=3, level=3, lo="1.3d")
def em_order_table(rng):
    use = pick(rng, EM)
    others = [e for e in EM if e != use]
    rng.shuffle(others)
    wrongs = {others[i][0]: f"That wave is used for {others[i][1]}." for i in range(3)}
    return dict(
        stem=f"The table shows some uses of waves.\n\n{T_EM}\n\nWhich type of wave is used for **{use[1]}**?",
        formula="each region of the electromagnetic spectrum has its own uses",
        working=[f"from the table: {use[1]} → **{use[0]}**"],
        hints=["Find the use in the right-hand column.", "Read across to the left-hand column.", "Match the row."],
        **_wrap(rng, use[0], wrongs),
    )


def _wrap(rng, correct, wrongs):
    opts, key, mis = text_options(rng, correct, wrongs)
    return dict(options=opts, key=key, misconceptions=mis)


# ---------------------------------------------------------------- L4
@template("c03_graph_read_both", chapter=3, level=4, lo="1.3c")
def graph_read_both(rng):
    A = nice(rng, 2, 3, 5)
    lam = nice(rng, 8, 10, 12, 16)
    n = nice(rng, 2, 2.5, 3)
    L = lam * n
    opts, key, mis = text_options(rng, f"amplitude {A} cm, wavelength {lam} cm, {n:g} waves shown", {
        f"amplitude {2 * A} cm, wavelength {lam} cm, {n:g} waves shown": "Amplitude is measured from the rest line, not crest to trough.",
        f"amplitude {A} cm, wavelength {L:g} cm, 1 wave shown": "The whole graph holds more than one wave; one wavelength is crest to next crest.",
        f"amplitude {A} cm, wavelength {lam / 2:g} cm, {2 * n:g} waves shown": "Crest to trough is only HALF a wavelength.",
    })
    return dict(
        stem="Fig. 1 shows a wave on a rope. Which row gives the amplitude, the wavelength and the number of complete waves shown?",
        figure=G1.wave(A, lam, n_waves=n, show="none"),
        options=opts, key=key, misconceptions=mis,
        formula="amplitude from the rest line; wavelength crest to crest; number of waves = total length ÷ wavelength",
        working=[f"crest height above rest line = {A} cm", f"crest to next crest = {lam} cm", f"length shown = {L:g} cm, so {L:g} ÷ {lam} = {n:g} waves"],
        hints=["Read the crest height first.", "Then the crest-to-crest distance.", "Count the crests."],
    )


@template("c03_energy_amplitude_data", chapter=3, level=4, lo="1.3b")
def energy_amplitude_data(rng):
    rows = [[2, nice(rng, 4, 5)], [4, nice(rng, 16, 20)], [6, nice(rng, 36, 45)]]
    ans = "the larger the amplitude, the more energy the wave carries"
    opts, key, mis = text_options(rng, ans, {
        "the energy carried does not depend on the amplitude": "The energy column rises steeply as the amplitude rises.",
        "a larger amplitude means the wave carries the sand along": "Waves transfer ENERGY, not the material; the sand is just pushed up the slope.",
        "the wave with the smallest amplitude carries the most energy": "Read the table: the largest amplitude moved the sand furthest.",
    })
    return dict(
        stem=f"Waves of different amplitudes hit a beach. A student measures how far sand is pushed up the slope by each wave.\n\n{md_table(['amplitude / cm', 'distance sand is pushed / cm'], rows)}\n\nWhat does the experiment show about the energy transferred by waves?",
        options=opts, key=key, misconceptions=mis,
        formula="waves transfer energy; a larger amplitude carries more energy",
        working=["the distance pushed rises with amplitude", f"so **{ans}**"],
        hints=["Which column measures the effect of the energy?", "How does it change as the amplitude grows?", "More amplitude, more energy."],
    )


@template("c03_frequency_wavelength_data", chapter=3, level=4, lo="1.3c")
def frequency_wavelength_data(rng):
    base = nice(rng, 40, 60, 120)
    rows = [[1, base], [2, base // 2], [4, base // 4]]
    ans = "the wavelength gets shorter as the frequency rises"
    opts, key, mis = text_options(rng, ans, {
        "the wavelength gets longer as the frequency rises": "Read the second column: it FALLS as the frequency rises.",
        "the wavelength does not change with frequency": "It halves each time the frequency doubles.",
        "the amplitude gets shorter as the frequency rises": "The table shows wavelength, not amplitude.",
    })
    return dict(
        stem=f"A student shakes a rope at different frequencies and measures the wavelength each time.\n\n{md_table(['frequency / Hz', 'wavelength / cm'], rows)}\n\nWhat does the table show?",
        options=opts, key=key, misconceptions=mis,
        formula="for a wave on the same rope, a higher frequency gives a shorter wavelength",
        working=[f"frequency 1 → 2 → 4 Hz; wavelength {base} → {base // 2} → {base // 4} cm", f"so **{ans}**"],
        hints=["Read the frequency column, then the wavelength column.", "One goes up while the other goes ...?", "Down."],
    )


@template("c03_em_uses_table_two", chapter=3, level=4, lo="1.3d")
def em_uses_table_two(rng):
    a, b = rng.sample(EM, 2)
    others = [e for e in EM if e not in (a, b)]
    c, d = rng.sample(others, 2)
    correct = f"X = {a[0]}, Y = {b[0]}"
    wrongs = {f"X = {b[0]}, Y = {a[0]}": "The two are swapped: check which use goes with which wave.",
              f"X = {c[0]}, Y = {b[0]}": f"{c[0]} are used for {c[1]}, not for X's use.",
              f"X = {a[0]}, Y = {d[0]}": f"{d[0]} are used for {d[1]}, not for Y's use."}
    return dict(
        stem=f"The table shows two uses.\n\n{md_table(['label', 'use'], [['X', a[1]], ['Y', b[1]]])}\n\nWhich types of wave are X and Y?",
        formula="each region of the electromagnetic spectrum has its own uses",
        working=[f"{a[1]} → {a[0]}", f"{b[1]} → {b[0]}"],
        hints=["Match each use with its wave.", f"Think about where {a[0]} are used.", f"Y: which wave is used for {b[1]}?"],
        **_wrap(rng, correct, wrongs),
    )


# ---------------------------------------------------------------- L5
@template("c03_waves_counted_two_ropes", chapter=3, level=5, lo="1.3c")
def waves_counted_two_ropes(rng):
    n1, t1 = nice(rng, 30, 40, 60), nice(rng, 10, 20)
    n2, t2 = nice(rng, 45, 50, 90), nice(rng, 15, 30)
    f1, f2 = n1 / t1, n2 / t2
    if abs(f1 - f2) < 0.05:
        f2 = f1 + 0.5; n2 = int(f2 * t2)
    ans = "P" if f1 > f2 else "Q"
    hi, lo = (f1, f2) if f1 > f2 else (f2, f1)
    opts, key, mis = text_options(rng, f"{ans}, with a frequency of {fmt(hi)} Hz against {fmt(lo)} Hz", {
        f"{'Q' if ans == 'P' else 'P'}, with a frequency of {fmt(lo)} Hz against {fmt(hi)} Hz": "Check the division: the higher frequency is the larger waves ÷ time.",
        f"{'P' if n1 > n2 else 'Q'}, because more waves were counted": "More waves in a LONGER time can still be a lower frequency; divide by the time.",
        "both the same, because they are the same kind of rope": "Work out waves ÷ time for each.",
    })
    return dict(
        stem=f"Two students shake ropes and count the waves.\n\n{md_table(['student', 'waves counted', 'time / s'], [['P', n1, t1], ['Q', n2, t2]])}\n\nWhich rope has the higher frequency?",
        options=opts, key=key, misconceptions=mis,
        formula="frequency = number of waves ÷ time",
        working=[f"P: {n1} ÷ {t1} = {fmt(f1)} Hz", f"Q: {n2} ÷ {t2} = {fmt(f2)} Hz", f"higher frequency: **{ans}**"],
        hints=["Frequency is waves per second, so divide for each.", f"P gives {fmt(f1)} Hz.", f"Q gives {fmt(f2)} Hz."],
    )


@template("c03_wavelength_from_graph_count", chapter=3, level=5, lo="1.3c")
def wavelength_from_graph_count(rng):
    A = nice(rng, 2, 3)
    lam = nice(rng, 8, 10, 12)
    n = nice(rng, 2.5, 3)
    f = nice(rng, 2, 4, 5)
    t = nice(rng, 10, 20)
    N = f * t
    opts, key, mis = numeric_options(rng, N, [
        (n * t, "The number of waves on the rope is not the frequency; use the frequency given."),
        (f, "That is waves per second; multiply by the time."),
        (N / 2, "Check: frequency × time."),
    ], unit="waves", sf=3)
    return dict(
        stem=f"Fig. 1 shows a wave on a rope at one instant. The wave is produced at a frequency of **{f} Hz**. How many complete waves are produced in **{t} s**?",
        figure=G1.wave(A, lam, n_waves=n, show="none"),
        options=opts, key=key, misconceptions=mis,
        formula="number of waves produced = frequency × time (the picture shows only the waves present at one instant)",
        working=[f"the picture shows {n:g} waves at one instant, which is not needed", f"waves produced = {f} × {t} = **{N}**"],
        hints=["The picture is a snapshot; the frequency tells you waves per second.", "Multiply the frequency by the time.", f"{f} × {t}."],
    )


@template("c03_em_safety_choice", chapter=3, level=5, lo="1.3d")
def em_safety_choice(rng):
    rows = [["radio waves", "no"], ["ultraviolet", "yes"], ["X-rays", "yes"], ["gamma rays", "yes"]]
    rng.shuffle(rows)
    part = pick(rng, ["arm bone", "leg bone", "wrist", "ankle", "collar bone"])
    ans = "X-rays, because they pass through flesh but are stopped by bone"
    opts, key, mis = text_options(rng, ans, {
        "radio waves, because they are the safest": "Radio waves pass through the body without making an image of the bones.",
        "gamma rays, because they are the most powerful": "Gamma rays are used to treat cancer, not to photograph bones; their high energy would be harmful for a simple photo.",
        "ultraviolet, because it can be used for sterilising": "Ultraviolet does not pass through the body to show bones.",
    })
    return dict(
        stem=f"A doctor needs an image of a patient's broken {part}. The table shows some waves.\n\n{md_table(['wave', 'can damage living cells'], rows)}\n\nWhich wave should be used, and why?",
        options=opts, key=key, misconceptions=mis,
        formula="X-rays: radiological applications (bone images) and engineering checks",
        working=["an image of bones needs a wave that passes through flesh but not bone", f"**{ans}**"],
        hints=["Which wave is used in hospitals for pictures of bones?", "It passes through soft tissue.", "X-rays."],
    )


@template("c03_energy_not_matter_data", chapter=3, level=5, lo="1.3b")
def energy_not_matter_data(rng):
    rows = [[0, 50], [2, nice(rng, 50, 51)], [4, nice(rng, 49, 50)], [6, 50]]
    ans = "the cork bobs up and down but stays near 50 cm, so the wave carries energy along the rope, not the rope itself"
    opts, key, mis = text_options(rng, ans, {
        "the cork moves along with the wave to the end of the rope": "Its position stays around 50 cm from the start.",
        "the rope material travels along to the far end": "The rope only moves up and down; the wave pattern travels.",
        "no energy reaches the far end because the cork does not move there": "The up-and-down motion at the far end shows energy has arrived.",
    })
    return dict(
        stem=f"A small cork is tied to a long rope 50 cm from one end. The end is shaken and a wave travels along the rope. The table shows the cork's position along the rope.\n\n{md_table(['time / s', 'distance of cork along rope / cm'], rows)}\n\nWhat does this show?",
        options=opts, key=key, misconceptions=mis,
        formula="waves transfer energy from one place to another without transferring matter",
        working=["the cork's distance along the rope hardly changes", f"**{ans}**"],
        hints=["Does the cork travel along the rope?", "What does travel along the rope?", "Energy, not matter."],
    )


# ================================================================ EXPLANATION
EXPLAIN = [
    # ------------------------------------------------------------ L1
    dict(id="e03_wave_source", level=1, lo="1.3a",
         stem=f"The table shows ways of making waves.\n\n{md_table(['action'], [['shaking the end of a rope up and down'], ['pushing and pulling the end of a spring'], ['dropping a stone into a pond']])}\n\nWhat do all these actions have in common?",
         correct="a vibration produces the wave",
         wrongs={"the material is pushed along to the far end": "The material moves to and fro; only the wave pattern travels along.", "energy is destroyed as the wave spreads": "Energy is carried by the wave, not destroyed.", "the waves need light to form": "Waves on ropes and water form in the dark too."},
         hints=["What is the hand or stone doing to the material?", "A to-and-fro movement.", "A vibration."]),
    dict(id="e03_amplitude_def", level=1, lo="1.3c",
         stem=f"The table lists wave terms.\n\n{md_table(['term', 'meaning'], [['P', 'maximum displacement from the rest position'], ['Q', 'number of waves produced each second'], ['R', 'distance from one crest to the next crest']])}\n\nWhich term is P?",
         correct="amplitude",
         wrongs={"frequency": "Frequency is the number of waves per second (Q).", "wavelength": "Wavelength is crest to crest (R).", "speed": "Speed is how fast the wave travels; it is not in the table."},
         hints=["It is measured from the rest line.", "It tells you how 'tall' the wave is.", "Amplitude."]),
    dict(id="e03_frequency_def", level=1, lo="1.3c",
         stem=f"The table lists wave terms.\n\n{md_table(['term', 'meaning'], [['P', 'maximum displacement from the rest position'], ['Q', 'number of waves produced each second'], ['R', 'distance from one crest to the next crest']])}\n\nWhich term is Q?",
         correct="frequency",
         wrongs={"amplitude": "Amplitude is the maximum displacement (P).", "wavelength": "Wavelength is crest to crest (R).", "energy": "Energy is what the wave carries; it is not a wave term in the table."},
         hints=["It is measured in hertz.", "Hertz means 'per second'.", "Frequency."]),
    dict(id="e03_wavelength_def", level=1, lo="1.3c",
         stem=f"The table lists wave terms.\n\n{md_table(['term', 'meaning'], [['P', 'maximum displacement from the rest position'], ['Q', 'number of waves produced each second'], ['R', 'distance from one crest to the next crest']])}\n\nWhich term is R?",
         correct="wavelength",
         wrongs={"amplitude": "Amplitude is a height, measured from the rest line.", "frequency": "Frequency is a number per second, not a distance.", "period": "Period is a time; R is a distance."},
         hints=["It is a distance along the wave.", "One complete wave long.", "Wavelength."]),
    dict(id="e03_unit_frequency", level=1, lo="1.3c",
         stem=f"The table lists units.\n\n{md_table(['unit', 'symbol'], [['hertz', 'Hz'], ['metre', 'm'], ['second', 's'], ['joule', 'J']])}\n\nWhich unit is used for frequency?",
         correct="hertz (Hz)",
         wrongs={"metre (m)": "Metres measure wavelength and amplitude.", "second (s)": "Seconds measure time.", "joule (J)": "Joules measure energy."},
         hints=["Frequency is waves per second.", "The unit is named after Heinrich Hertz.", "Hz."]),
    dict(id="e03_remote_control_wave", level=1, lo="1.3d",
         stem=f"The table shows uses of waves.\n\n{T_EM}\n\nWhich wave does a television remote control use?",
         correct="infrared",
         wrongs={"microwaves": "Microwaves are used in ovens and for satellite communication.", "ultraviolet": "Ultraviolet is used for sterilising and sunbeds.", "X-rays": "X-rays are used to see bones."},
         hints=["Find 'remote control' in the table.", "Read the left-hand column.", "Infrared."]),
    dict(id="e03_microwave_oven_wave", level=1, lo="1.3d",
         stem=f"The table shows uses of waves.\n\n{T_EM}\n\nWhich wave heats food in a microwave oven?",
         correct="microwaves",
         wrongs={"infrared": "Infrared is used in remote controls (and in grills, but the oven in the question uses microwaves).", "radio waves": "Radio waves carry broadcasts.", "gamma rays": "Gamma rays are used in medical treatment."},
         hints=["The oven is named after the wave.", "Also used for satellite communication.", "Microwaves."]),
    dict(id="e03_energy_transfer_fact", level=1, lo="1.3b",
         stem=f"The table describes a boat on the sea when waves pass.\n\n{md_table(['observation'], [['the boat bobs up and down'], ['the boat stays in the same place']])}\n\nWhat do waves transfer from place to place?",
         correct="energy",
         wrongs={"water": "The water (and the boat) only moves up and down; it does not travel along with the wave.", "the boat": "The boat stays where it is.", "nothing": "The bobbing shows energy has arrived."},
         hints=["The boat moves but does not travel.", "Something made it move.", "Energy."]),

    # ------------------------------------------------------------ L2
    dict(id="e03_rope_vs_spring", level=2, lo="1.3a",
         stem=f"The table describes two ways of making waves.\n\n{md_table(['material', 'how the end is moved'], [['rope', 'up and down'], ['spring', 'pushed and pulled along its length']])}\n\nWhat is the same about both?",
         correct="in both, the vibrating end passes energy along the material",
         wrongs={"in both, the hand must move along the material": "The hand stays at one end.", "in both, the material travels to the far end": "The material moves to and fro about its rest position.", "only the rope produces a wave": "Both produce waves."},
         hints=["What does the hand do in each case?", "It vibrates the end.", "The vibration sends energy along."]),
    dict(id="e03_bigger_shake", level=2, lo="1.3c",
         stem=f"A student shakes a rope. The table shows two trials.\n\n{md_table(['trial', 'how the end is shaken'], [['1', 'small up-and-down movements'], ['2', 'large up-and-down movements, same number per second']])}\n\nHow does the wave in trial 2 differ from trial 1?",
         correct="it has a larger amplitude",
         wrongs={"it has a higher frequency": "The number of shakes per second is the same, so the frequency is the same.", "it has a shorter wavelength": "Same frequency on the same rope gives the same wavelength.", "it has a smaller amplitude": "LARGER movements give a LARGER amplitude."},
         hints=["Which wave term describes the size of the up-and-down movement?", "Same shakes per second → same frequency.", "Amplitude."]),
    dict(id="e03_faster_shake", level=2, lo="1.3c",
         stem=f"A student shakes a rope. The table shows two trials.\n\n{md_table(['trial', 'shakes per second'], [['1', 2], ['2', 4]])}\n\nHow does the wave in trial 2 differ from trial 1?",
         correct="it has a higher frequency",
         wrongs={"it has a larger amplitude": "Frequency is about how OFTEN the end is shaken, not how far.", "it has a lower frequency": "4 shakes per second is MORE than 2.", "it carries no energy": "All waves carry energy."},
         hints=["Shakes per second is the ...?", "Frequency.", "4 Hz is higher than 2 Hz."]),
    dict(id="e03_crest_trough_fig", level=2, lo="1.3c",
         stem="Fig. 1 shows a wave with arrows P and Q. Which arrow shows the wavelength?",
         fig=lambda rng: G1.wave(3, 10, show="both"),
         correct="Q, the distance from one crest to the next",
         wrongs={"P, the height of a crest": "P shows the amplitude.", "P, because wavelength is measured upwards": "Wavelength is a distance ALONG the wave.", "neither; wavelength is the length of the whole rope": "Wavelength is one complete wave, crest to crest."},
         hints=["Wavelength is measured along the direction the wave travels.", "Which arrow is horizontal?", "Q."]),
    dict(id="e03_sunbed_wave", level=2, lo="1.3d",
         stem=f"The table shows uses of waves.\n\n{T_EM}\n\nA clinic uses a wave to sterilise its instruments, and the same type of wave is used in sunbeds. Which wave is it?",
         correct="ultraviolet",
         wrongs={"infrared": "Infrared is used in remote controls.", "X-rays": "X-rays are used for imaging bones.", "microwaves": "Microwaves are used for cooking and satellite links."},
         hints=["It comes from the Sun and tans skin.", "'Ultra' means beyond; it is beyond violet light.", "Ultraviolet."]),
    dict(id="e03_optical_fibre_wave", level=2, lo="1.3d",
         stem=f"The table shows uses of waves.\n\n{T_EM}\n\nInternet signals are sent along glass optical fibres. Which wave carries them?",
         correct="light",
         wrongs={"radio waves": "Radio waves are broadcast through the air.", "gamma rays": "Gamma rays are used in medicine.", "ultraviolet": "Ultraviolet is used for sterilising."},
         hints=["The fibre is 'optical'.", "Optical means to do with ...?", "Light."]),
    dict(id="e03_medical_treatment_wave", level=2, lo="1.3d",
         stem=f"The table shows uses of waves.\n\n{T_EM}\n\nA patient's cancer is treated with a beam of radiation. Which wave is used?",
         correct="gamma rays",
         wrongs={"X-rays": "X-rays are used to photograph bones.", "microwaves": "Microwaves cook food.", "light": "Light is used in optical fibres."},
         hints=["It is the most energetic wave in the table.", "Used for medical TREATMENT, not pictures.", "Gamma rays."]),
    dict(id="e03_energy_from_sun", level=2, lo="1.3b",
         stem=f"The table shows what happens to a solar panel on a sunny day.\n\n{md_table(['observation'], [['the panel warms up'], ['it produces electricity'], ['nothing travels from the Sun except light']])}\n\nWhat does this show about light waves?",
         correct="they transfer energy from the Sun to the panel",
         wrongs={"they transfer matter from the Sun": "No material travels from the Sun to the panel.", "they do not carry energy": "The panel warms and produces electricity, so energy has arrived.", "they only carry sound": "Light is not sound."},
         hints=["Where does the panel's energy come from?", "What links the Sun and the panel?", "Light carries the energy."]),

    # ------------------------------------------------------------ L3
    dict(id="e03_explain_amplitude_energy", level=3, lo="1.3b",
         stem=f"The table shows two sea waves.\n\n{md_table(['wave', 'amplitude / m', 'effect on a boat'], [['P', 0.5, 'gentle rocking'], ['Q', 3.0, 'violent tossing']])}\n\nWhy does wave Q affect the boat more?",
         correct="a larger amplitude means the wave carries more energy to the boat",
         wrongs={"a larger amplitude means a higher frequency": "Amplitude and frequency are separate; the table says nothing about frequency.", "wave Q carries more water with it": "Waves transfer energy, not water.", "the boat is heavier in wave Q": "The boat is the same."},
         hints=["Which wave term is given in the table?", "How does amplitude relate to energy?", "More amplitude, more energy."],
         keypoints=[KP("larger amplitude", "amplitude", "bigger", "larger", "higher"), KP("more energy", "energy")]),
    dict(id="e03_wave_terms_change", level=3, lo="1.3c",
         stem="Fig. 1 shows a wave on a rope. The student now shakes the rope twice as often but with the same size of movement. Which wave terms change?",
         fig=lambda rng: G1.wave(3, 12, show="none"),
         correct="the frequency doubles and the wavelength becomes shorter; the amplitude stays the same",
         wrongs={"only the amplitude changes": "The size of the movement is unchanged, so the amplitude is unchanged.", "the frequency and amplitude both double": "The amplitude depends on the SIZE of the shake, which is the same.", "nothing changes because it is the same rope": "Shaking twice as often doubles the frequency."},
         hints=["Shaking more often changes which term?", "Same size of shake → same amplitude.", "More waves per second fit into the same rope: shorter wavelength."],
         keypoints=[KP("frequency doubles / increases", "frequency"), KP("amplitude unchanged", "amplitude")]),
    dict(id="e03_choose_wave_satellite", level=3, lo="1.3d",
         stem=f"The table shows three jobs.\n\n{md_table(['job'], [['send a television signal to a satellite'], ['check a metal weld for cracks'], ['control a television from the sofa']])}\n\nWhich waves are used, in order?",
         correct="microwaves, X-rays, infrared",
         wrongs={"radio waves, gamma rays, light": "Satellite links use microwaves; weld checks use X-rays; remotes use infrared.", "microwaves, infrared, X-rays": "The last two are swapped.", "infrared, X-rays, microwaves": "The first and last are swapped."},
         hints=["Satellite communication → ?", "Engineering checks → X-rays.", "Remote control → infrared."],
         keypoints=[KP("microwaves for satellite", "microwave"), KP("X-rays for welds", "x-ray", "x ray", "xray", "rays"), KP("infrared for remote", "infrared", "infra")]),
    dict(id="e03_same_frequency_rope", level=3, lo="1.3c",
         stem=f"A rope is shaken and the wave is observed at two points.\n\n{md_table(['point', 'distance from hand / m', 'waves passing each second'], [['near', 1, 3], ['far', 5, 3]])}\n\nWhat does the table show about the frequency along the rope?",
         correct="the frequency is the same everywhere because it is set by the vibrating hand",
         wrongs={"the frequency falls as the wave travels": "Both points see 3 waves per second.", "the frequency rises as the wave travels": "Both points see 3 waves per second.", "the far point has no frequency": "Three waves pass it every second."},
         hints=["Compare the last column.", "Who decides how many waves are made each second?", "The source."],
         keypoints=[KP("same frequency", "same", "equal", "constant", "3"), KP("set by the source / hand", "hand", "source", "vibration", "shake")]),
    dict(id="e03_wave_speed_lake", level=3, lo="1.3b",
         stem=f"A stone is dropped into a still pond. The table shows observations.\n\n{md_table(['time / s', 'observation'], [[0, 'stone hits the water'], [2, 'ripples reach a floating leaf 1 m away'], [2, 'the leaf bobs up and down but stays 1 m away']])}\n\nWhich explanation is correct?",
         correct="the ripples carried energy from the splash to the leaf; the water itself did not travel to the leaf",
         wrongs={"the water from the splash flowed to the leaf": "The leaf stays in place, showing the water only bobs up and down.", "the leaf moved because the stone pushed it": "The stone did not touch the leaf; the ripples did.", "no energy reached the leaf": "The bobbing shows energy arrived."},
         hints=["What reached the leaf?", "Did the leaf drift away with the wave?", "Energy travelled, matter did not."],
         keypoints=[KP("energy transferred", "energy"), KP("water / leaf stays in place", "stay", "same place", "does not move along", "not carried", "bob", "up and down")]),
    dict(id="e03_spring_pulse", level=3, lo="1.3a",
         stem=f"A long spring lies on a table. A student pushes one end forward once and lets go. The table shows what is seen.\n\n{md_table(['observation'], [['a squashed region travels along the spring'], ['each coil moves forward then back to where it started']])}\n\nWhat produced the wave, and what travelled along the spring?",
         correct="the push (a vibration of the end) produced it, and energy travelled along the spring",
         wrongs={"the coils travelled along to the far end": "Each coil returns to its starting place.", "the table produced the wave": "The table is passive; the push at the end produced it.", "the wave carried the spring forward": "The spring stays on the table where it was."},
         hints=["What did the student do to the end?", "Do the coils end up somewhere else?", "No: only energy travels."],
         keypoints=[KP("push / vibration at the end", "push", "vibrat", "end", "hand"), KP("energy travels along", "energy")]),
    dict(id="e03_bigger_waves_wind", level=3, lo="1.3b",
         stem=f"The table shows sea conditions on two days.\n\n{md_table(['day', 'wind', 'wave amplitude / m', 'damage to sea wall'], [['Monday', 'light', 0.3, 'none'], ['Friday', 'strong', 2.5, 'stones washed away']])}\n\nWhy was there damage on Friday?",
         correct="the strong wind made larger waves, which carried more energy to the wall",
         wrongs={"the strong wind blew the stones away directly": "It was the waves hitting the wall that moved the stones.", "the sea water was heavier on Friday": "Water density did not change.", "the waves had a lower frequency on Friday": "The table gives amplitude, not frequency; energy rises with amplitude."},
         hints=["Compare the amplitude column.", "How does amplitude relate to energy?", "Larger waves, more energy."],
         keypoints=[KP("larger amplitude / bigger waves", "amplitude", "bigger", "larger", "2.5"), KP("more energy", "energy")]),
    dict(id="e03_em_table_identify", level=3, lo="1.3d",
         stem=f"The table shows what a student noticed at a hospital.\n\n{md_table(['place', 'what the wave is used for'], [['X-ray room', 'picture of a broken leg'], ['oncology ward', 'treating a tumour'], ['sterilising room', 'killing germs on tools']])}\n\nWhich waves are used in the three places, in order?",
         correct="X-rays, gamma rays, ultraviolet",
         wrongs={"X-rays, X-rays, infrared": "Tumours are treated with gamma rays, and infrared is not used for sterilising.", "gamma rays, X-rays, ultraviolet": "The first two are swapped.", "X-rays, gamma rays, microwaves": "Sterilising uses ultraviolet."},
         hints=["Pictures of bones → ?", "Treatment of cancer → gamma rays.", "Sterilising → ultraviolet."],
         keypoints=[KP("X-rays for the picture", "x-ray", "x ray", "xray", "rays"), KP("gamma for treatment", "gamma"), KP("ultraviolet for sterilising", "ultraviolet", "uv")]),

    # ------------------------------------------------------------ L4
    dict(id="e03_graph_interpret_two", level=4, lo="1.3c",
         stem="Fig. 1 shows wave P. Wave Q has twice the amplitude and half the wavelength of P. Which description of Q is correct?",
         fig=lambda rng: G1.wave(2, 12, show="none"),
         correct="crests 4 cm high and 6 cm apart",
         wrongs={"crests 4 cm high and 24 cm apart": "Half the wavelength means the crests are CLOSER, 6 cm apart.", "crests 1 cm high and 6 cm apart": "Twice the amplitude means HIGHER crests, 4 cm.", "crests 2 cm high and 12 cm apart": "That is P itself."},
         hints=["Read P's amplitude and wavelength from the graph.", "Double one and halve the other.", "2 → 4 cm; 12 → 6 cm."],
         keypoints=[KP("amplitude 4 cm", "4"), KP("wavelength 6 cm", "6")]),
    dict(id="e03_which_fits_data_freq", level=4, lo="1.3c",
         stem=f"A student times waves on a rope.\n\n{md_table(['trial', 'waves counted', 'time / s', 'frequency / Hz'], [['1', 20, 10, 2], ['2', 40, 10, 4], ['3', 20, 5, '?']])}\n\nWhat is the missing frequency, and which trial has the same frequency?",
         correct="4 Hz, the same as trial 2",
         wrongs={"2 Hz, the same as trial 1": "20 waves in 5 s is 4 per second, not 2.", "10 Hz, different from both": "20 ÷ 5 = 4, not 10.", "4 Hz, the same as trial 1": "Trial 1 is 2 Hz."},
         hints=["Frequency = waves ÷ time.", "20 ÷ 5.", "Compare with the other trials."],
         keypoints=[KP("4 Hz", "4"), KP("same as trial 2", "trial 2", "2")]),
    dict(id="e03_choose_wave_evidence", level=4, lo="1.3d",
         stem=f"The table gives facts about two waves.\n\n{md_table(['wave', 'passes through', 'can harm cells'], [['radio waves', 'walls and the body', 'no'], ['X-rays', 'flesh but not bone', 'yes']])}\n\nWhy are radio waves used for broadcasting but X-rays for bone pictures?",
         correct="radio waves reach receivers through walls safely; X-rays make a shadow of bone because bone stops them",
         wrongs={"X-rays are used for broadcasting because they travel further": "X-rays harm cells; they are not broadcast around towns.", "radio waves could make bone pictures too": "Radio waves pass through bone, so no shadow forms.", "both are chosen only because they are cheap": "The choice follows from what each wave passes through."},
         hints=["Which wave passes through walls harmlessly?", "Which wave is stopped by bone?", "Match the property to the job."],
         keypoints=[KP("radio waves pass through walls safely", "wall", "safe", "harmless", "no harm", "through"), KP("X-rays stopped by bone", "bone", "shadow", "stop", "absorb")]),
    dict(id="e03_amplitude_decay_data", level=4, lo="1.3b",
         stem=f"A wave travels along a long rope. The amplitude is measured at different distances from the hand.\n\n{md_table(['distance from hand / m', 'amplitude / cm'], [[1, 10], [3, 6], [5, 3]])}\n\nWhat happens to the energy carried by the wave, and why?",
         correct="less energy is carried as the wave travels, because some is converted to thermal energy and sound in the rope and air",
         wrongs={"the energy stays the same because the rope is the same": "The falling amplitude shows energy has been lost from the wave.", "the energy increases as the wave spreads out": "Amplitude is falling, so energy carried is falling.", "the wave carries no energy at 5 m": "At 5 m the amplitude is 3 cm, so it still carries some energy."},
         hints=["Amplitude falls with distance.", "What does a smaller amplitude mean for energy?", "Where could the energy have gone?"],
         keypoints=[KP("less energy / amplitude falls", "less", "decrease", "smaller", "lost", "reduce"), KP("converted to heat / sound", "thermal", "heat", "sound", "friction", "air")]),
    dict(id="e03_remote_blocked", level=4, lo="1.3d",
         stem=f"A student tests a television remote control.\n\n{md_table(['test', 'result'], [['pointed at the television', 'works'], ['a book held in front of the remote', 'does not work'], ['pointed at a mirror facing the television', 'works']])}\n\nWhich explanation is correct?",
         correct="the remote sends infrared, which is blocked by the book but reflected by the mirror",
         wrongs={"the remote sends radio waves, which pass through books": "The book blocked the signal, so it is not a radio wave.", "the remote sends sound, which bounced off the mirror": "Remotes use infrared; sound would pass round the book.", "the mirror produces its own infrared": "The mirror reflects the remote's infrared."},
         hints=["Which wave do remotes use?", "What does the book result show?", "What does the mirror result show?"],
         keypoints=[KP("infrared", "infrared", "infra", "ir"), KP("blocked by book / reflected by mirror", "block", "reflect", "bounce", "absorb")]),
    dict(id="e03_wave_period_count", level=4, lo="1.3c",
         stem=f"A pendulum-like float on a pond is filmed.\n\n{md_table(['time / s', 'float position'], [[0, 'top'], [1, 'bottom'], [2, 'top'], [3, 'bottom'], [4, 'top']])}\n\nWhat is the frequency of the water waves?",
         correct="0.5 Hz, because one complete up-and-down takes 2 s",
         wrongs={"1 Hz, because the float moves every second": "One complete wave is top → bottom → top, which takes 2 s.", "2 Hz, because the float is at the top every 2 s": "Every 2 s means ONE wave in 2 s, which is 0.5 per second.", "4 Hz, because there are 4 seconds": "Count complete waves in the 4 s: there are 2."},
         hints=["One complete wave: top to top.", "How long does that take?", "Frequency = waves ÷ time = 2 ÷ 4."],
         keypoints=[KP("0.5 Hz", "0.5", "half"), KP("one wave takes 2 s", "2 s", "2 second", "two second")]),
    dict(id="e03_microwave_vs_ir_cooking", level=4, lo="1.3d",
         stem=f"The table compares two cooking appliances.\n\n{md_table(['appliance', 'wave used', 'how food heats'], [['microwave oven', 'microwaves', 'inside and outside at once'], ['grill', 'infrared', 'from the surface inwards']])}\n\nWhich statement is a correct conclusion?",
         correct="different waves are chosen for different jobs: microwaves penetrate the food, infrared heats its surface",
         wrongs={"both appliances use the same wave": "The table names two different waves.", "infrared is not used for cooking": "The grill uses infrared.", "microwaves are used only for communication": "Microwaves also cook food."},
         hints=["Compare the 'how food heats' column.", "Which wave goes deeper into the food?", "Each wave suits a different job."],
         keypoints=[KP("microwaves penetrate / heat inside", "inside", "penetrat", "through", "deep"), KP("infrared heats the surface", "surface", "outside")]),
    dict(id="e03_sound_vs_light_energy", level=4, lo="1.3b",
         stem=f"A loudspeaker plays a note. A candle flame nearby flickers in time with the note; a sheet of paper 2 m away does not move.\n\n{md_table(['distance from speaker / m', 'observation'], [[0.1, 'flame flickers strongly'], [2.0, 'paper does not move']])}\n\nWhich statement is correct?",
         correct="the sound wave carries energy, which is spread out and too small to move the paper by 2 m",
         wrongs={"sound waves carry no energy": "The flickering flame shows energy arriving.", "the sound stops at 1 m": "It spreads out and weakens; it does not stop.", "the flame flickers because air flows from the speaker": "No wind is produced; the air vibrates to and fro."},
         hints=["What made the flame move?", "What happens to the wave's energy as it spreads?", "It is shared over a bigger area."],
         keypoints=[KP("sound carries energy", "energy"), KP("spreads out / weaker with distance", "spread", "weaker", "smaller", "less", "distance", "too far")]),

    # ------------------------------------------------------------ L5
    dict(id="e03_design_experiment_amplitude", level=5, lo="1.3b",
         stem=f"A student wants to test whether waves with a larger amplitude carry more energy. The table shows the plan.\n\n{md_table(['step'], [['drop a ball into a tank from different heights to make waves'], ['measure how far a floating cork is pushed up a ramp at the far end'], ['keep the tank, water depth and cork the same']])}\n\nWhich improvement makes the test fair AND measures the right thing?",
         correct="measure the wave amplitude each time, so the cork's travel can be matched to a known amplitude",
         wrongs={"use a different cork for each height": "Changing the cork is not a fair test.", "measure how far the cork drifts sideways": "Energy transfer is shown by the push up the ramp, not sideways drift.", "drop the ball from the same height every time": "Then the amplitude never changes and nothing can be compared."},
         hints=["What is the independent variable?", "Is it being measured?", "Record the amplitude."],
         keypoints=[KP("measure the amplitude", "amplitude", "height of the wave", "measure the wave"), KP("fair test / same conditions", "fair", "same", "control", "constant", "only change", "each time", "matched")]),
    dict(id="e03_evaluate_claim_frequency", level=5, lo="1.3c",
         stem=f"A student says: 'Shaking the rope harder makes the waves closer together.' The table shows the student's own results.\n\n{md_table(['trial', 'size of shake', 'shakes per second', 'wavelength / cm'], [['1', 'small', 2, 50], ['2', 'large', 2, 50], ['3', 'small', 4, 25]])}\n\nWhat do the results show?",
         correct="the wavelength depends on the frequency (shakes per second), not on how hard the rope is shaken",
         wrongs={"shaking harder halves the wavelength": "Trials 1 and 2 shake differently but the wavelength is the same.", "shaking harder changes the frequency": "Trials 1 and 2 both have 2 shakes per second.", "the wavelength never changes": "Trial 3 has a different wavelength."},
         hints=["Compare trials 1 and 2 first.", "Then compare trials 1 and 3.", "What changed the wavelength?"],
         keypoints=[KP("frequency changes the wavelength", "frequency", "shakes per second", "faster"), KP("size of shake / amplitude does not", "size", "amplitude", "hard", "not")]),
    dict(id="e03_em_misuse_sunbed", level=5, lo="1.3d",
         stem=f"A sunbed advertisement says: 'Our ultraviolet lamps are completely safe because ultraviolet is used in hospitals.' The table gives facts.\n\n{md_table(['fact'], [['ultraviolet kills bacteria on hospital tools'], ['ultraviolet can damage skin cells'], ['hospitals shield people while the lamps sterilise tools']])}\n\nWhich evaluation is correct?",
         correct="the claim is misleading: the same property that kills bacteria can damage living skin, which is why hospitals keep people away from the lamps",
         wrongs={"the claim is correct because hospitals are safe places": "Hospitals use ultraviolet on tools, not on people, and shield people from it.", "ultraviolet cannot be used in both places": "It is used in both; the question is about safety for skin.", "the claim is correct because ultraviolet is a kind of light": "Being 'light-like' does not make it harmless."},
         hints=["Why does ultraviolet kill bacteria?", "What would it do to skin cells?", "Hospitals shield people for a reason."],
         keypoints=[KP("UV damages skin / cells", "damage", "harm", "skin", "cells", "cancer", "burn"), KP("hospitals shield people / not used on people", "shield", "away", "tools", "not on people", "protect")]),
    dict(id="e03_tsunami_energy", level=5, lo="1.3b",
         stem=f"The table compares a tsunami in the open sea and at the coast.\n\n{md_table(['place', 'amplitude / m', 'wavelength / km', 'effect'], [['open sea', 0.5, 200, 'ships barely notice'], ['coast', 10, 5, 'buildings destroyed']])}\n\nWhich explanation is best?",
         correct="the wave's energy is squeezed into a shorter wavelength near the coast, so the amplitude grows and the energy hits the coast in a huge wave",
         wrongs={"the wave gains energy from the coast": "The energy was carried from the open sea; it becomes concentrated, not created.", "ships are safe because the wave carries no energy in deep water": "It carries enormous energy; it is spread over a long wavelength and small amplitude.", "the wavelength grows near the coast, making it dangerous": "The wavelength SHRINKS from 200 km to 5 km."},
         hints=["Compare amplitude and wavelength in the two places.", "Energy is conserved as the wave travels.", "Shorter and taller: the energy is concentrated."],
         keypoints=[KP("energy concentrated / amplitude grows", "concentrat", "squeez", "amplitude", "taller", "higher", "grows"), KP("wavelength shorter", "shorter", "wavelength", "5 km")]),
    dict(id="e03_choose_wave_communication", level=5, lo="1.3d",
         stem=f"An engineer must send data between two buildings 500 m apart. The table shows options.\n\n{md_table(['option', 'wave', 'notes'], [['P', 'infrared beam through the air', 'blocked by fog and birds'], ['Q', 'light through an optical fibre', 'needs a cable laid'], ['R', 'X-rays', 'harmful; needs shielding']])}\n\nWhich option is best for a reliable, safe link, and why?",
         correct="Q, because light in an optical fibre is not affected by weather and is safe",
         wrongs={"P, because no cable is needed": "The infrared beam fails in fog or when something crosses it.", "R, because X-rays travel through buildings": "X-rays are harmful and not used for communication.", "P, because infrared is faster than light": "Both travel at the same speed; the issue is reliability."},
         hints=["Which option is unaffected by weather?", "Which option is safe?", "Optical fibre."],
         keypoints=[KP("optical fibre / light", "fibre", "fiber", "optical", "light", "q"), KP("reliable and safe", "reliable", "safe", "weather", "fog", "not blocked")]),
    dict(id="e03_wave_graph_mistake", level=5, lo="1.3c",
         stem="Fig. 1 shows a wave. A student writes: 'amplitude = 6 cm, wavelength = 5 cm'. What has the student done wrong?",
         fig=lambda rng: G1.wave(3, 10, show="none"),
         correct="measured crest to trough for the amplitude (should be 3 cm) and crest to trough for the wavelength (should be 10 cm)",
         wrongs={"nothing; both values are correct": "Amplitude is from the rest line (3 cm) and wavelength is crest to crest (10 cm).", "the amplitude is right but the wavelength should be 20 cm": "The amplitude is also wrong, and the wavelength is 10 cm.", "the wavelength is right but the amplitude should be 1.5 cm": "The amplitude is 3 cm, measured from the rest line to a crest."},
         hints=["Amplitude is measured from the rest line.", "Wavelength is one COMPLETE wave.", "Both student values are from crest to trough."],
         keypoints=[KP("amplitude from rest line = 3 cm", "3", "rest", "half"), KP("wavelength crest to crest = 10 cm", "10", "crest to crest", "complete wave", "whole wave")]),
    dict(id="e03_evaluate_spring_claim", level=5, lo="1.3a",
         stem=f"Two students argue about a wave on a spring.\n\n{md_table(['student', 'claim'], [['P', 'the coils travel to the far end, that is how the energy gets there'], ['Q', 'each coil only vibrates about its rest position; the energy is passed from coil to coil']])}\n\nA mark is painted on one coil. After the wave passes, the mark is in its original place. Who is right?",
         correct="Q: the marked coil did not travel, so matter stayed put while the energy was passed along by the vibrations",
         wrongs={"P: the energy must be carried by moving coils": "The mark shows the coil returned to its place.", "both: the coils travel and come back": "Returning to the same place means no net travel; that is vibration.", "neither: no energy reaches the far end": "The far end moves when the wave arrives, so energy does reach it."},
         hints=["What does the painted mark show?", "Vibration means moving to and fro about a fixed point.", "Energy is passed along, not the coils."],
         keypoints=[KP("Q is right / coils vibrate in place", "q", "vibrat", "same place", "return", "does not travel"), KP("energy passed along", "energy")]),
]

register_explain(EXPLAIN, chapter=3)
