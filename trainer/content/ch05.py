"""Ch 5 Sources of Food (K123 topic 2.1): 20 data templates and 40 explanation items, built from the Topic 2.1 assignments
and the Ch 5 Brain Gym. lo codes: 2.1a plants need air, light, water, nutrients, suitable pH; 2.1b growing population and limited
space; 2.1c fertilisers, pesticides / herbicides, slash-and-burn improve crops; 2.1d their environmental problems; 2.1e biological
control; 2.1f better varieties and intensive farming; 2.1g plant hormones (weed killers, growth and ripening)."""
from .. import sketches as S
from .base import fmt, md_table, nice, numeric_options, pick, register_explain, template, text_options

KP = lambda label, *phr: {"label": label, "any": list(phr)}

UI = [(0, "red"), (1, "red"), (2, "red"), (3, "orange"), (4, "orange"), (5, "yellow"), (6, "yellow-green"), (7, "green"),
      (8, "blue-green"), (9, "blue"), (10, "blue"), (11, "indigo"), (12, "violet"), (13, "violet"), (14, "violet")]
T_UI = md_table(["pH", "Universal Indicator colour"], [["0-2", "red"], ["3-4", "orange"], ["5-6", "yellow"], ["7", "green"], ["8-11", "blue"], ["12-14", "violet"]])


def _kind(ph):
    return "acidic" if ph < 7 else ("neutral" if ph == 7 else "alkaline")


# ================================================================ CALCULATION / DATA
# ---------------------------------------------------------------- L1
@template("c05_ph_meter_classify", chapter=5, level=1, lo="2.1a")
def ph_meter_classify(rng):
    vals = {"A": nice(rng, 3.2, 4.5, 5.8), "B": 7.0, "C": nice(rng, 8.3, 9.1, 10.4), "D": nice(rng, 2.1, 6.2)}
    ask = pick(rng, ["acidic", "neutral", "alkaline"])
    ans = {"acidic": "samples A and D", "neutral": "sample B", "alkaline": "sample C"}[ask]
    wrongs = {k: v for k, v in {"acidic": "samples A and D", "neutral": "sample B", "alkaline": "sample C"}.items() if k != ask}
    w = {v: f"That substance is {k}: pH below 7 is acidic, 7 is neutral, above 7 is alkaline." for k, v in wrongs.items()}
    w["samples A, B, C and D"] = "Only pH values on one side of 7 fit the description."
    opts, key, mis = text_options(rng, ans, w)
    rows = [[k, vals[k]] for k in "ABCD"]
    return dict(
        stem=f"A student tests four soil samples with a pH meter.\n\n{md_table(['soil sample', 'pH'], rows)}\n\nWhich sample(s) are **{ask}**?",
        options=opts, key=key, misconceptions=mis,
        formula="pH below 7 = acidic;  pH 7 = neutral;  pH above 7 = alkaline",
        working=[", ".join(f"{k}: pH {vals[k]} is {_kind(vals[k])}" for k in "ABCD"), f"{ask}: **{ans}**"],
        hints=["Compare each pH with 7.", "Remember what being on each side of 7 means.", f"Look for the {ask} ones."],
    )


@template("c05_ui_colour_to_ph", chapter=5, level=1, lo="2.1a")
def ui_colour_to_ph(rng):
    ph, colour = pick(rng, [(2, "red"), (4, "orange"), (6, "yellow"), (7, "green"), (9, "blue"), (13, "violet")])
    ans = f"about pH {ph}, so the soil is {_kind(ph)}"
    others = [p for p in (2, 4, 6, 7, 9, 13) if p != ph]
    rng.shuffle(others)
    w = {f"about pH {p}, so the soil is {_kind(p)}": f"pH {p} gives {dict(UI)[p]} with Universal Indicator, not {colour}." for p in others[:3]}
    opts, key, mis = text_options(rng, ans, w)
    return dict(
        stem=f"A farmer adds Universal Indicator to a soil sample mixed with water. It turns **{colour}**.\n\n{T_UI}\n\nWhat is the pH of the soil, and is it acidic, neutral or alkaline?",
        options=opts, key=key, misconceptions=mis,
        formula="Universal Indicator: red / orange / yellow = acidic, green = neutral, blue / violet = alkaline",
        working=[f"{colour} → about pH {ph}", f"pH {ph} is **{_kind(ph)}**"],
        hints=["Find the colour in the table.", "Read off the pH range.", "Below 7 acidic, 7 neutral, above 7 alkaline."],
    )


@template("c05_litmus_result", chapter=5, level=1, lo="2.1a")
def litmus_result(rng):
    kind = pick(rng, ["acidic", "alkaline", "neutral"])
    res = {"acidic": ("stays red", "turns red"), "alkaline": ("turns blue", "stays blue"), "neutral": ("stays red", "stays blue")}[kind]
    ans = f"red litmus {res[0]}, blue litmus {res[1]}"
    allres = {"acidic": "red litmus stays red, blue litmus turns red", "alkaline": "red litmus turns blue, blue litmus stays blue", "neutral": "red litmus stays red, blue litmus stays blue"}
    w = {v: f"That is the result for a {k} substance." for k, v in allres.items() if k != kind}
    w["both papers turn green"] = "Litmus paper is only red or blue; green is a Universal Indicator colour."
    opts, key, mis = text_options(rng, ans, w)
    ph = {"acidic": nice(rng, 3, 5, 6), "alkaline": nice(rng, 8, 10, 12), "neutral": 7}[kind]
    return dict(
        stem=f"A soil sample has the pH shown.\n\n{md_table(['soil sample', 'pH'], [['X', ph]])}\n\nWhat happens when red and blue litmus papers are dipped into water mixed with the soil?",
        options=opts, key=key, misconceptions=mis,
        formula="acid: blue litmus → red;  alkali: red litmus → blue;  neutral: no change",
        working=[f"pH {ph} is {kind}", f"**{ans}**"],
        hints=["Is the pH below, at or above 7?", "Acids turn blue litmus red; alkalis turn red litmus blue.", "Neutral changes neither."],
    )


@template("c05_yield_table_read", chapter=5, level=1, lo="2.1c")
def yield_table_read(rng):
    base = nice(rng, 20, 25, 30)
    rows = [["none", base], ["fertiliser", base + nice(rng, 12, 15, 20)], ["fertiliser + pesticide", base + nice(rng, 25, 30)]]
    ans = f"{rows[2][1] - base} kg more"
    opts, key, mis = numeric_options(rng, rows[2][1] - base, [
        (rows[2][1], "That is the yield WITH both treatments; the question asks how much MORE than with no treatment."),
        (rows[1][1] - base, "That is the increase from fertiliser alone."),
        (rows[2][1] + base, "Subtract the two yields; do not add."),
    ], unit="kg", sf=3)
    return dict(
        stem=f"A farmer grows the same crop in three plots of the same size.\n\n{md_table(['treatment', 'mass of crop harvested / kg'], rows)}\n\nHow much more crop did the plot with fertiliser and pesticide give than the untreated plot?",
        options=opts, key=key, misconceptions=mis,
        formula="increase = treated yield − untreated yield",
        working=[f"{rows[2][1]} − {base}", f"= **{ans}**"],
        hints=["Find the untreated plot's yield.", "Subtract it from the treated plot's yield.", f"{rows[2][1]} − {base}."],
    )


# ---------------------------------------------------------------- L2
@template("c05_ph_bar_chart", chapter=5, level=2, lo="2.1a")
def ph_bar_chart(rng):
    vals = [nice(rng, 3.2, 4.0), nice(rng, 5.4, 6.1), 7.0, nice(rng, 8.3, 9.5)]
    labels = ["A", "B", "C", "D"]
    rng.shuffle(vals)
    i7 = vals.index(7.0)
    ans = labels[i7]
    w = {labels[j]: f"{labels[j]} has pH {vals[j]}, which is {_kind(vals[j])}." for j in range(4) if j != i7}
    opts, key, mis = text_options(rng, ans, w)
    return dict(
        stem="Fig. 1 shows the pH of four household substances measured with a pH meter. Which substance is neutral?",
        figure=S.bar_chart(labels, vals, "pH", ymax=14, ystep=2),
        options=opts, key=key, misconceptions=mis,
        formula="pH 7 = neutral",
        working=[f"the bar at exactly 7 is {ans}", f"**{ans}** is neutral"],
        hints=["Neutral means pH 7.", "Which bar reaches exactly 7?", "Read the heights carefully."],
    )


@template("c05_choose_plant_for_soil", chapter=5, level=2, lo="2.1a")
def choose_plant_for_soil(rng):
    ph = nice(rng, 5, 5.5, 8, 8.5)
    acidic = ph < 7
    plants = [["azalea", "acidic"], ["boxwood", "alkaline"], ["hydrangea", "alkaline"], ["blueberry", "acidic"]]
    good = [p[0] for p in plants if (p[1] == "acidic") == acidic]
    ans = pick(rng, good)
    bad = [p[0] for p in plants if p[0] != ans]
    w = {b: (f"{b} prefers {'alkaline' if acidic else 'acidic'} soil, but pH {ph} is {'acidic' if acidic else 'alkaline'}." if b not in good else f"{b} would also grow, but check the option given as correct: both suit this soil; only one is listed as the answer here.") for b in bad}
    # make sure only one 'good' plant appears among the options
    bad_only = [b for b in bad if b not in good][:2]
    extra = "any plant, because pH does not matter"
    w = {b: w[b] for b in bad_only}
    w[extra] = "Plants need a suitable pH for healthy growth; the table shows each plant's preference."
    opts, key, mis = text_options(rng, ans, w)
    return dict(
        stem=f"The table shows the soil each plant grows best in. A garden's soil has a pH of **{ph}**.\n\n{md_table(['plant', 'type of soil'], plants)}\n\nWhich plant would grow well in this garden?",
        options=opts, key=key, misconceptions=mis,
        formula="pH below 7 is acidic, above 7 is alkaline; match the plant to the soil",
        working=[f"pH {ph} is {'acidic' if acidic else 'alkaline'}", f"a plant that likes {'acidic' if acidic else 'alkaline'} soil: **{ans}**"],
        hints=["Is pH " + str(ph) + " acidic or alkaline?", "Find a plant that prefers that type.", "Read the second column."],
    )


@template("c05_pest_count_biocontrol", chapter=5, level=2, lo="2.1e")
def pest_count_biocontrol(rng):
    start = nice(rng, 400, 500, 600)
    rows = [[0, start], [2, int(start * 0.7)], [4, int(start * 0.4)], [6, int(start * 0.2)]]
    drop = start - rows[3][1]
    opts, key, mis = numeric_options(rng, drop, [
        (rows[3][1], "That is the number LEFT after 6 weeks, not the fall."),
        (start, "That is the starting number; subtract the final number."),
        (start + rows[3][1], "Subtract, do not add."),
    ], unit="aphids", sf=3)
    return dict(
        stem=f"Ladybirds (which eat aphids) are released into a greenhouse. The table shows the aphid count.\n\n{md_table(['weeks after release', 'number of aphids'], rows)}\n\nBy how much did the number of aphids fall in 6 weeks?",
        options=opts, key=key, misconceptions=mis,
        formula="fall = starting number − final number",
        working=[f"{start} − {rows[3][1]}", f"= **{drop}**"],
        hints=["Read the first and last rows.", "Subtract the final count from the starting count.", f"{start} − {rows[3][1]}."],
    )


@template("c05_population_food_table", chapter=5, level=2, lo="2.1b")
def population_food_table(rng):
    rows = [[2000, 6.1, nice(rng, 1.8, 1.9)], [2020, 7.8, nice(rng, 2.6, 2.8)], [2050, 9.7, "?"]]
    per = round(rows[0][2] / rows[0][1], 2)
    need = round(9.7 * per, 1)
    opts, key, mis = numeric_options(rng, need, [
        (rows[1][2], "That is the 2020 amount; the population keeps growing."),
        (9.7, "That is the population in billions, not the food needed."),
        (need / 2, "Each billion people needs the same amount; multiply up."),
    ], unit="billion tonnes", sf=2)
    return dict(
        stem=f"The table shows the world population and the cereal grown to feed it. Each billion people needs about the same amount of cereal.\n\n{md_table(['year', 'population / billion', 'cereal needed / billion tonnes'], rows)}\n\nAbout how much cereal will be needed in 2050?",
        options=opts, key=key, misconceptions=mis,
        formula="cereal needed is proportional to population (same amount per billion people)",
        working=[f"per billion people: {rows[0][2]} ÷ {rows[0][1]} ≈ {per} billion tonnes", f"2050: 9.7 × {per} ≈ **{need} billion tonnes**"],
        hints=["How much cereal per billion people in 2000?", f"About {per} billion tonnes per billion people.", "Multiply by 9.7."],
    )


# ---------------------------------------------------------------- L3
@template("c05_fertiliser_dose_data", chapter=5, level=3, lo="2.1c")
def fertiliser_dose_data(rng):
    rows = [[0, nice(rng, 20, 22)], [50, nice(rng, 30, 32)], [100, nice(rng, 36, 38)], [150, nice(rng, 37, 38)], [200, nice(rng, 36, 37)]]
    ans = "yield rises with fertiliser up to about 100 kg per hectare, then stops rising; extra fertiliser is wasted and may pollute water"
    opts, key, mis = text_options(rng, ans, {
        "yield keeps rising, so the farmer should use as much fertiliser as possible": "From 100 kg onwards the yield hardly changes; more fertiliser does not help.",
        "fertiliser has no effect on yield": "The yield rises from the first to the third row.",
        "fertiliser reduces the yield": "The yield rises with the first doses.",
    })
    return dict(
        stem=f"A farmer tests different amounts of fertiliser on equal plots.\n\n{md_table(['fertiliser / kg per hectare', 'yield / tonnes per hectare'], rows)}\n\nWhat is the best conclusion?",
        options=opts, key=key, misconceptions=mis,
        formula="fertilisers add nutrients and raise yield, but excess fertiliser gives no extra yield and can wash into rivers",
        working=["yield rises until 100 kg per hectare, then levels off", f"**{ans}**"],
        hints=["Read the yield column downwards.", "Where does it stop rising?", "Think about where extra fertiliser ends up."],
    )


@template("c05_oxygen_algae_data", chapter=5, level=3, lo="2.1d")
def oxygen_algae_data(rng):
    rows = [["upstream of farm", nice(rng, 8, 9), "clear"], ["next to farm", nice(rng, 5, 6), "green"], ["downstream of farm", nice(rng, 1, 2), "thick green scum"]]
    ans = "fertiliser washed from the farm caused algae to grow, blocking sunlight and lowering the oxygen in the water"
    opts, key, mis = text_options(rng, ans, {
        "the farm adds oxygen to the river": "The oxygen FALLS downstream of the farm.",
        "algae add oxygen, so the water downstream is healthier": "The water downstream has the least oxygen.",
        "the river is cleaner downstream because it is further from the farm": "Downstream has the thickest algae and the least oxygen.",
    })
    return dict(
        stem=f"A river flows past a farm that uses a lot of fertiliser. Water samples are tested.\n\n{md_table(['sample point', 'dissolved oxygen / mg per litre', 'appearance'], rows)}\n\nWhat do the results show?",
        options=opts, key=key, misconceptions=mis,
        formula="fertiliser in water → algae bloom → sunlight blocked, plants die, oxygen falls, fish die",
        working=["oxygen falls and algae increase as the water passes the farm", f"**{ans}**"],
        hints=["Compare the oxygen upstream and downstream.", "What is growing in the water?", "What causes algae to grow?"],
    )


@template("c05_intensive_vs_traditional", chapter=5, level=3, lo="2.1f")
def intensive_vs_traditional(rng):
    t_chick, t_days = nice(rng, 2000, 3000), nice(rng, 90, 100)
    i_chick, i_days = nice(rng, 20000, 30000), nice(rng, 35, 42)
    ans = "the intensive farm raises far more chickens in less time on the same land"
    opts, key, mis = text_options(rng, ans, {
        "the traditional farm produces more chickens per year": "It raises fewer birds, and each batch takes longer.",
        "both farms produce the same amount of food": f"{i_chick} chickens in {i_days} days is far more than {t_chick} in {t_days} days.",
        "the intensive farm uses more land": "Both farms use the same land area.",
    })
    return dict(
        stem=f"Two chicken farms use the same area of land.\n\n{md_table(['farm', 'chickens per batch', 'days to grow a batch'], [['traditional', t_chick, t_days], ['intensive', i_chick, i_days]])}\n\nWhat does the table show about intensive farming?",
        options=opts, key=key, misconceptions=mis,
        formula="intensive farming produces more food from the same space in less time",
        working=[f"intensive: {i_chick} chickens every {i_days} days; traditional: {t_chick} every {t_days} days", f"**{ans}**"],
        hints=["Compare the numbers of chickens.", "Compare the days per batch.", "More birds, less time, same land."],
    )


@template("c05_ph_change_lime", chapter=5, level=3, lo="2.1a")
def ph_change_lime(rng):
    start = nice(rng, 4.5, 5.0, 5.5)
    rows = [[0, start], [1, start + 0.5], [2, start + 1.0], [3, round(min(7.0, start + 1.5), 1)]]
    ans = "the lime makes the soil less acidic, moving the pH towards 7, which suits most crops"
    opts, key, mis = text_options(rng, ans, {
        "the lime makes the soil more acidic": "The pH RISES, so the soil becomes less acidic.",
        "the lime has no effect on the soil": "The pH changes every week.",
        "the lime makes the soil neutral immediately": "The pH rises slowly over three weeks.",
    })
    return dict(
        stem=f"A farmer adds lime to acidic soil and measures the pH each week.\n\n{md_table(['weeks after adding lime', 'soil pH'], rows)}\n\nWhat is the effect of the lime?",
        options=opts, key=key, misconceptions=mis,
        formula="plants need a suitable pH; pH rising towards 7 means less acidic",
        working=[f"pH rises from {start} towards 7", f"**{ans}**"],
        hints=["Read the pH column downwards.", "Rising pH means ... acidic?", "Less acidic."],
    )


# ---------------------------------------------------------------- L4
@template("c05_pesticide_food_chain", chapter=5, level=4, lo="2.1d")
def pesticide_food_chain(rng):
    base = nice(rng, 0.02, 0.05)
    rows = [["water", base], ["water plants", round(base * 10, 2)], ["small fish", round(base * 100, 1)], ["birds that eat fish", round(base * 1000, 0)]]
    ans = "the pesticide is passed along the food chain and builds up, so the birds at the top receive the most"
    opts, key, mis = text_options(rng, ans, {
        "the pesticide is broken down as it moves along the food chain": "The amount RISES at each step.",
        "the birds drank the most water": "Birds get the pesticide from the fish they eat, which got it from plants.",
        "the water has the highest level of pesticide": "The water has the lowest level in the table.",
    })
    return dict(
        stem=f"Pesticide sprayed on a farm washes into a lake. Scientists measure it in the lake's food chain.\n\n{md_table(['sample', 'pesticide / mg per kg'], rows)}\n\nWhat do the results show?",
        options=opts, key=key, misconceptions=mis,
        formula="pesticides contaminate soil and water and are transferred along the food chain, building up in top consumers",
        working=["the level is ten times higher at each step of the food chain", f"**{ans}**"],
        hints=["Read the amounts down the chain.", "They multiply by 10 each step.", "Who ends up with the most?"],
    )


@template("c05_slash_burn_data", chapter=5, level=4, lo="2.1d")
def slash_burn_data(rng):
    rows = [[1, nice(rng, 3.0, 3.5), nice(rng, 2, 3)], [2, nice(rng, 2.0, 2.4), nice(rng, 8, 10)], [3, nice(rng, 1.0, 1.2), nice(rng, 18, 22)]]
    ans = "the ash gives a good first harvest, but with no trees the soil is washed away and the yield falls each year"
    opts, key, mis = text_options(rng, ans, {
        "the yield rises every year because the ash keeps adding nutrients": "The yield FALLS each year.",
        "soil loss is not linked to clearing the forest": "Soil loss rises sharply once the trees are gone.",
        "the farmer should burn the land again each year to restore the yield": "Burning again cannot replace the soil that has eroded, and it causes more haze.",
    })
    return dict(
        stem=f"A forest is cleared by slash-and-burn and farmed. The table shows the results.\n\n{md_table(['year after burning', 'crop yield / tonnes per hectare', 'soil lost by erosion / tonnes per hectare'], rows)}\n\nWhat do the data show?",
        options=opts, key=key, misconceptions=mis,
        formula="slash-and-burn: ash adds nutrients at first, but deforestation leads to soil erosion (and burning causes haze)",
        working=["yield falls each year while soil loss rises", f"**{ans}**"],
        hints=["Compare the yield across the years.", "What happens to the soil?", "Why does soil wash away without trees?"],
    )


@template("c05_growth_conditions_data", chapter=5, level=4, lo="2.1a")
def growth_conditions_data(rng):
    rows = [["P", "bright", "yes", "daily", nice(rng, 28, 32)], ["Q", "bright", "no", "daily", nice(rng, 18, 22)], ["R", "dark", "yes", "daily", nice(rng, 4, 6)], ["S", "bright", "yes", "none", nice(rng, 2, 3)]]
    ans = "light, water and nutrients are all needed: removing any one of them greatly reduces growth"
    opts, key, mis = text_options(rng, ans, {
        "only fertiliser matters, because P grew tallest": "Q (no fertiliser) still grew; R (no light) and S (no water) barely grew at all.",
        "water is not needed because S got sunlight": "S got no water and grew least.",
        "plants grow better in the dark": "R, in the dark, grew only a few centimetres.",
    })
    return dict(
        stem=f"Four identical seedlings are grown for 4 weeks.\n\n{md_table(['seedling', 'light', 'fertiliser', 'watering', 'height after 4 weeks / cm'], rows)}\n\nWhat conclusion do the results support?",
        options=opts, key=key, misconceptions=mis,
        formula="plants need light, air, water, nutrients and a suitable pH for photosynthesis and growth",
        working=["P (everything) grew most; Q (no fertiliser) less; R (no light) and S (no water) hardly at all", f"**{ans}**"],
        hints=["Compare each seedling with P.", "Which conditions were removed?", "Each missing condition cut the growth."],
    )


@template("c05_hormone_ripening_data", chapter=5, level=4, lo="2.1g")
def hormone_ripening_data(rng):
    rows = [["none", nice(rng, 10, 12)], ["ripening hormone", nice(rng, 3, 4)]]
    ans = "the plant hormone speeds up ripening, so the fruit is ready to sell sooner"
    opts, key, mis = text_options(rng, ans, {
        "the hormone slows ripening so the fruit lasts longer": f"Treated fruit ripened in {rows[1][1]} days, faster than the untreated {rows[0][1]} days.",
        "the hormone kills the fruit": "The fruit ripened; it was not killed.",
        "the hormone is a pesticide": "Plant hormones regulate growth and ripening; they do not kill pests.",
    })
    return dict(
        stem=f"Green bananas are picked and stored in two rooms.\n\n{md_table(['treatment', 'days until the bananas are yellow and ripe'], rows)}\n\nWhat does this show about plant hormones?",
        options=opts, key=key, misconceptions=mis,
        formula="plant hormones are used to regulate the growth and ripening of fruits (and as weed killers)",
        working=[f"treated bananas ripened in {rows[1][1]} days instead of {rows[0][1]}", f"**{ans}**"],
        hints=["Compare the two rows.", "Which ripened faster?", "What was different?"],
    )


# ---------------------------------------------------------------- L5
@template("c05_choose_method_evaluate", chapter=5, level=5, lo="2.1e")
def choose_method_evaluate(rng):
    rows = [["chemical pesticide", nice(rng, 90, 95), "yes", "yes"], ["biological control (predators)", nice(rng, 70, 80), "no", "no"]]
    ans = "biological control kills fewer pests but leaves no chemicals in the soil, water or food chain, so it is the safer long-term choice"
    opts, key, mis = text_options(rng, ans, {
        "the pesticide is better in every way because it kills more pests": "It contaminates soil and water and harms other animals.",
        "biological control is useless because it kills fewer pests": f"It still removes {rows[1][1]}% of pests without pollution.",
        "neither method affects the environment": "The pesticide contaminates soil and water.",
    })
    return dict(
        stem=f"A farmer compares two ways of controlling caterpillars.\n\n{md_table(['method', 'pests killed / %', 'chemicals left in soil and water', 'harm to birds and bees'], rows)}\n\nWhich is the best evaluation?",
        options=opts, key=key, misconceptions=mis,
        formula="biological control uses natural predators to control pests, reducing the need for pesticides",
        working=["pesticide: more pests killed, but contamination and harm to wildlife", f"**{ans}**"],
        hints=["Look at all three columns, not just the first.", "What are the costs of the pesticide?", "Weigh pests killed against pollution."],
    )


@template("c05_space_population_calc", chapter=5, level=5, lo="2.1b")
def space_population_calc(rng):
    land = nice(rng, 500, 600, 800)
    per = nice(rng, 2, 2.5)
    pop_now = int(land / per)
    pop_future = int(pop_now * nice(rng, 1.3, 1.5))
    need = pop_future * per
    extra = need - land
    opts, key, mis = numeric_options(rng, extra, [
        (need, "That is the total land needed, not the EXTRA land."),
        (pop_future - pop_now, "That is the extra people, not the land in hectares."),
        (extra / 2, "Each extra person needs the full amount of land."),
    ], unit="hectares", sf=3)
    return dict(
        stem=f"An island has {land} hectares of farmland, which feeds its people at {per} hectares per person. Its population is expected to grow.\n\n{md_table(['population now', 'population expected'], [[pop_now, pop_future]])}\n\nHow much extra farmland would be needed to feed everyone the same way, and what does this show?",
        options=opts, key=key, misconceptions=mis,
        formula="land needed = people × land per person; a growing population with limited space is why food production must improve",
        working=[f"land needed = {pop_future} × {per} = {fmt(need)} hectares", f"extra = {fmt(need)} − {land} = **{fmt(extra)} hectares**, which the island may not have: food production per hectare must rise"],
        hints=["Work out the land needed for the future population.", f"{pop_future} × {per}.", "Subtract the land the island already has."],
    )


@template("c05_fertiliser_runoff_rain", chapter=5, level=5, lo="2.1d")
def fertiliser_runoff_rain(rng):
    rows = [["dry week", nice(rng, 1, 2), nice(rng, 8, 9)], ["week of heavy rain", nice(rng, 15, 20), nice(rng, 3, 4)]]
    ans = "heavy rain washes fertiliser from the fields into the river, where it feeds algae that use up oxygen; the farmer should avoid spreading fertiliser before rain"
    opts, key, mis = text_options(rng, ans, {
        "rain adds nitrate to the river directly from the clouds": "Rainwater has very little nitrate; it carries fertiliser off the fields.",
        "the fish are fine because rain adds oxygen to rivers": "Oxygen FELL in the rainy week.",
        "the farmer should use more fertiliser in rainy weeks to replace what is lost": "That would wash even more into the river."},
    )
    return dict(
        stem=f"A river below farmland is tested in two weeks.\n\n{md_table(['week', 'nitrate in river / mg per litre', 'dissolved oxygen / mg per litre'], rows)}\n\nWhat is the best explanation and advice?",
        options=opts, key=key, misconceptions=mis,
        formula="fertilisers washed into water cause algae growth and lower oxygen (water contamination)",
        working=["nitrate rises and oxygen falls after heavy rain", f"**{ans}**"],
        hints=["Where does the extra nitrate come from?", "What does nitrate do in a river?", "When should fertiliser NOT be spread?"],
    )


@template("c05_variety_data", chapter=5, level=5, lo="2.1f")
def variety_data(rng):
    rows = [["old variety", nice(rng, 4.0, 4.5), nice(rng, 120, 130), "often"], ["new variety", nice(rng, 6.5, 7.0), nice(rng, 95, 100), "rarely"]]
    ans = "the new variety gives more grain, grows faster and resists disease, so more food comes from the same land"
    opts, key, mis = text_options(rng, ans, {
        "the old variety is better because it takes longer and so grows bigger": "Taking longer is a disadvantage; the new variety still gives more grain.",
        "the new variety needs more land to give more grain": "The yield is per hectare, so it is more food from the SAME land.",
        "there is no difference between the varieties": "Every column differs.",
    })
    return dict(
        stem=f"A rice farmer compares two varieties on equal plots.\n\n{md_table(['variety', 'yield / tonnes per hectare', 'days to harvest', 'disease'], rows)}\n\nWhat is the best conclusion?",
        options=opts, key=key, misconceptions=mis,
        formula="improving varieties of plants and animals increases food production",
        working=["more yield, fewer days, less disease for the new variety", f"**{ans}**"],
        hints=["Compare each column.", "Which variety wins on all three?", "More food from the same land."],
    )


# ================================================================ EXPLANATION
T_METHODS = md_table(["method", "what it does"], [["fertiliser", "adds nutrients so crops grow faster and bigger"], ["pesticide", "kills pests that eat crops"], ["herbicide", "kills weeds that compete with crops"], ["slash-and-burn", "clears forest quickly; ash adds nutrients"], ["biological control", "predators eat the pests"], ["plant hormones", "kill weeds; control growth and ripening of fruit"]])
T_PROBLEMS = md_table(["method", "environmental problem"], [["fertiliser", "washes into water, algae grow, oxygen falls"], ["pesticide / herbicide", "contaminates soil and water; passes along the food chain"], ["slash-and-burn", "haze (breathing problems); deforestation and soil erosion"]])

EXPLAIN = [
    # ------------------------------------------------------------ L1
    dict(id="e05_plants_need", level=1, lo="2.1a",
         stem=f"The table lists things.\n\n{md_table(['item'], [['carbon dioxide'], ['nitrogen gas'], ['sunlight'], ['water']])}\n\nWhich of these do plants need to make food by photosynthesis?",
         correct="carbon dioxide, sunlight and water",
         wrongs={"nitrogen gas and water": "Plants take nitrogen from nutrients in the soil, not from nitrogen gas, and photosynthesis needs carbon dioxide and light too.", "sunlight only": "Carbon dioxide and water are also needed.", "carbon dioxide and nitrogen gas": "Nitrogen gas is not used; water and sunlight are needed."},
         hints=["Photosynthesis: carbon dioxide + water → sugar + oxygen, using light.", "Which three are in that equation?", "Not nitrogen gas."]),
    dict(id="e05_not_needed_wind", level=1, lo="2.1a",
         stem=f"The table lists conditions.\n\n{md_table(['condition'], [['wind'], ['light'], ['water'], ['nutrients']])}\n\nWhich condition is NOT needed for plants to grow and make food?",
         correct="wind",
         wrongs={"light": "Light provides the energy for photosynthesis.", "water": "Water is a raw material of photosynthesis.", "nutrients": "Nutrients from the soil are needed for healthy growth."},
         hints=["Plants need light, air, water, nutrients and a suitable pH.", "Which item is not in that list?", "Wind."]),
    dict(id="e05_photosynthesis_products", level=1, lo="2.1a",
         stem=f"The table shows the word equation for photosynthesis with gaps.\n\n{md_table(['raw materials', 'products'], [['carbon dioxide + water', 'X + oxygen']])}\n\nWhat is X?",
         correct="sugar (glucose)",
         wrongs={"protein": "Photosynthesis makes sugar, not protein.", "carbon dioxide": "Carbon dioxide is a raw material, not a product.", "nitrogen": "Nitrogen is not made by photosynthesis."},
         hints=["Plants make their own food.", "The food is a sugar.", "Glucose."]),
    dict(id="e05_why_improve_food", level=1, lo="2.1b",
         stem=f"The table shows world data.\n\n{md_table(['year', 'population / billion'], [[1950, 2.5], [2020, 7.8]])}\n\nWhy must food production be improved?",
         correct="the population is growing but the space to grow food is limited",
         wrongs={"people eat less than they used to": "More people need more food, not less.", "there is unlimited land for farming": "Land for farming is limited.", "food can be made in factories without plants": "Our food still comes from plants and animals that need space."},
         hints=["What is happening to the population?", "Is there more land to farm?", "More people, limited space."]),
    dict(id="e05_fertiliser_purpose", level=1, lo="2.1c",
         stem=f"The table lists farming methods.\n\n{T_METHODS}\n\nWhy do farmers add fertilisers to the soil?",
         correct="to add nutrients so the crops grow faster and bigger",
         wrongs={"to kill the pests on the crop": "That is what pesticides do.", "to kill weeds": "That is what herbicides do.", "to make the soil more acidic": "Fertilisers add nutrients; they are not used to make soil acidic."},
         hints=["Fertilisers are food for plants.", "What do plants take from fertilisers?", "Nutrients."]),
    dict(id="e05_pesticide_vs_herbicide", level=1, lo="2.1c",
         stem=f"The table lists farming methods.\n\n{T_METHODS}\n\nWhich chemical is sprayed to kill weeds growing among the crop?",
         correct="herbicide",
         wrongs={"pesticide": "Pesticides kill pests (insects and other animals), not weeds.", "fertiliser": "Fertilisers feed plants; they do not kill weeds.", "plant hormone used for ripening": "That hormone controls ripening of fruit."},
         hints=["'Herb' refers to plants.", "Which product is named after plants?", "Weeds are unwanted plants."]),
    dict(id="e05_biocontrol_def", level=1, lo="2.1e",
         stem=f"The table lists farming methods.\n\n{T_METHODS}\n\nA farmer releases ladybirds to eat the aphids on her crop. What is this method called?",
         correct="biological control",
         wrongs={"use of pesticides": "No chemical is sprayed; a living predator is used.", "slash-and-burn": "That is a way of clearing land.", "use of plant hormones": "Plant hormones control growth and ripening or kill weeds."},
         hints=["A living thing is used to control the pest.", "The ladybird is a predator of the aphid.", "Biological (living) control."]),
    dict(id="e05_hormone_uses", level=1, lo="2.1g",
         stem=f"The table lists farming methods.\n\n{T_METHODS}\n\nWhich of the following is a use of plant hormones?",
         correct="making fruit ripen at the right time for sale",
         wrongs={"killing insects on the crop": "That is a pesticide.", "adding nitrogen to the soil": "That is a fertiliser.", "clearing forest for new fields": "That is slash-and-burn."},
         hints=["Plant hormones control the plant's own processes.", "Growth, ripening, and some kill weeds.", "Ripening of fruit."]),

    # ------------------------------------------------------------ L2
    dict(id="e05_slash_burn_benefit", level=2, lo="2.1c",
         stem=f"The table describes slash-and-burn.\n\n{md_table(['step'], [['trees are cut down'], ['the land is burnt'], ['crops are planted in the cleared land']])}\n\nWhich is a benefit of this method?",
         correct="it is a cheap and fast way to clear land, and the ash adds nutrients to the soil",
         wrongs={"the smoke improves the air": "The smoke causes haze and breathing difficulties.", "it stops soil erosion": "Removing trees CAUSES soil erosion.", "it uses very little land": "Large areas of forest are cleared."},
         hints=["Why would a farmer choose it?", "Think about cost, speed and the ash.", "Ash contains nutrients."]),
    dict(id="e05_slash_burn_problem", level=2, lo="2.1d",
         stem=f"The table lists environmental problems.\n\n{T_PROBLEMS}\n\nWhich problems are caused by slash-and-burn?",
         correct="haze that causes breathing difficulties, and soil erosion after deforestation",
         wrongs={"algae growing in rivers": "That is caused by fertilisers washing into water.", "pesticide passing along food chains": "That is caused by pesticides.", "no problems at all": "Burning causes haze and removing trees causes erosion."},
         hints=["What does burning produce?", "What happens to soil when trees are gone?", "Haze and erosion."]),
    dict(id="e05_algae_cause", level=2, lo="2.1d",
         stem=f"The table shows observations of a river near farmland.\n\n{md_table(['observation'], [['thick green algae on the surface'], ['dead fish'], ['fields of crops next to the river']])}\n\nWhat is the most likely cause of the algae?",
         correct="chemical fertilisers washed into the river",
         wrongs={"the water is very clean, so algae grow well": "Algae blooms are a sign of nutrient pollution, not clean water.", "pesticides washed into the river": "Pesticides kill living things; they do not feed algae.", "warm weather alone": "Warmth helps, but the nutrients from fertiliser cause the bloom."},
         hints=["Algae are plants: what do plants need to grow fast?", "Nutrients.", "Where could extra nutrients come from near a farm?"]),
    dict(id="e05_algae_effect", level=2, lo="2.1d",
         stem=f"The table shows what happens after an algae bloom.\n\n{md_table(['effect'], [['algae cover the surface'], ['plants at the bottom cannot get sunlight'], ['? ']])}\n\nWhat is the final effect on the pond?",
         correct="the oxygen level falls and fish die",
         wrongs={"the pond becomes more acidic": "The main problem is the loss of oxygen.", "the fish turn green": "Fish do not turn green; they die from lack of oxygen.", "more fish are produced": "Fish die when oxygen runs out."},
         hints=["Plants at the bottom die without sunlight.", "What do they stop producing?", "Oxygen."]),
    dict(id="e05_ui_colour_acid", level=2, lo="2.1a",
         stem=f"A farmer tests soil with Universal Indicator and it turns yellow.\n\n{T_UI}\n\nWhat is the soil?",
         correct="acidic, with a pH below 7",
         wrongs={"neutral, with a pH of 7": "Neutral gives green.", "alkaline, with a pH above 7": "Alkaline gives blue or violet.", "acidic, with a pH above 7": "Acidic means BELOW 7."},
         hints=["Find yellow in the table.", "What pH range is it?", "Is that below or above 7?"]),
    dict(id="e05_ph_meter_reading_choose", level=2, lo="2.1a",
         stem=f"Soybeans grow best in slightly acidic soil. The table shows pH meter readings of four fields.\n\n{md_table(['field', 'pH'], [['P', 1.5], ['Q', 3.0], ['R', 6.5], ['S', 8.0]])}\n\nWhich field is best for soybeans?",
         correct="R",
         wrongs={"P": "pH 1.5 is strongly acidic, far too acidic.", "Q": "pH 3.0 is strongly acidic.", "S": "pH 8.0 is alkaline."},
         hints=["Slightly acidic means just below 7.", "Which pH is just below 7?", "Not far below."]),
    dict(id="e05_intensive_farming_def", level=2, lo="2.1f",
         stem=f"The table describes two farms.\n\n{md_table(['farm', 'description'], [['P', 'thousands of chickens kept in a large shed, fed a controlled diet'], ['Q', 'a few chickens roaming a yard']])}\n\nWhich farm uses intensive farming, and what is its aim?",
         correct="P; to produce more food from the same space in less time",
         wrongs={"Q; to produce more food from the same space": "Q keeps few animals in a large space.", "P; to give the chickens more room": "Intensive farming keeps many animals in little space.", "Q; to use the latest technology": "Q is traditional farming."},
         hints=["Intensive means many animals or crops in a small space.", "Which farm fits?", "More food per area."]),
    dict(id="e05_plant_hormone_weedkiller", level=2, lo="2.1g",
         stem=f"The table lists ways to deal with weeds.\n\n{md_table(['method'], [['pull them out by hand'], ['spray a plant hormone weed killer'], ['burn the field']])}\n\nHow does a plant hormone weed killer work?",
         correct="it makes the weeds grow in an uncontrolled way until they die",
         wrongs={"it poisons the insects that live on the weeds": "That would be a pesticide.", "it adds nutrients to the crop": "That would be a fertiliser.", "it blocks sunlight from the weeds": "It acts chemically on the weed's growth."},
         hints=["It is a hormone: it affects growth.", "Too much growth is harmful.", "The weeds grow themselves to death."]),

    # ------------------------------------------------------------ L3
    dict(id="e05_why_not_taste_acid", level=3, lo="2.1a",
         stem=f"A student tests an acid.\n\n{md_table(['test', 'observation'], [['pH meter', 6], ['red litmus', 'stays red'], ['blue litmus', 'turns red']])}\n\nAnother student suggests tasting it to confirm it is sour. Why is this not allowed in the laboratory?",
         correct="laboratory chemicals may be harmful or contaminated, so safe tests such as litmus or a pH meter are used instead",
         wrongs={"because the litmus test already proves it is an alkali": "The litmus results show an ACID.", "because acids have no taste": "Acids taste sour; tasting is banned for safety.", "because tasting would change the pH": "The reason is safety, not the pH."},
         hints=["Think about safety.", "What might be in a lab chemical?", "Use indicators instead."],
         keypoints=[KP("harmful / unsafe / poisonous", "harm", "unsafe", "danger", "poison", "toxic", "contaminat"), KP("use indicators / pH meter instead", "litmus", "indicator", "ph meter", "test", "instead")]),
    dict(id="e05_fertiliser_two_sides", level=3, lo="2.1d",
         stem=f"The table shows a farmer's results.\n\n{md_table(['fertiliser used', 'crop yield', 'river nearby'], [['none', 'low', 'clear'], ['a lot', 'high', 'green algae, dead fish']])}\n\nExplain the two effects of the fertiliser.",
         correct="it adds nutrients so the crop grows better, but the excess washes into the river, feeds algae and lowers the oxygen so fish die",
         wrongs={"it poisons the fish directly": "Fertiliser is not a poison; it feeds algae, which use up the oxygen.", "it only helps and has no bad effects": "The river shows algae and dead fish.", "it kills the weeds in the river": "Fertiliser makes water plants and algae grow MORE."},
         hints=["Why did the yield rise?", "Why did algae appear?", "What do algae do to the oxygen?"],
         keypoints=[KP("nutrients raise yield", "nutrient", "grow", "yield", "bigger", "faster"), KP("algae / oxygen falls / fish die", "algae", "oxygen", "fish")]),
    dict(id="e05_biocontrol_explain", level=3, lo="2.1e",
         stem=f"A farmer has aphids on her crop. The table shows two options.\n\n{md_table(['option', 'result after 4 weeks'], [['spray pesticide', 'aphids gone; bees and ladybirds also dead'], ['release ladybirds', 'aphids much fewer; bees unharmed']])}\n\nExplain how releasing ladybirds controls the aphids and why it reduces the need for pesticides.",
         correct="ladybirds are predators that eat the aphids, so the pest numbers fall without spraying chemicals that harm other living things",
         wrongs={"ladybirds eat the crop instead of the aphids": "Ladybirds eat aphids, not the crop.", "ladybirds spread a disease to the aphids": "They eat them; it is predation.", "the ladybirds frighten the aphids away": "They eat them."},
         hints=["What is the relationship between ladybirds and aphids?", "Predator and prey.", "No chemicals are needed."],
         keypoints=[KP("predator eats the pest", "eat", "predator", "prey", "feed on"), KP("no chemicals / no pollution", "chemical", "pesticide", "pollut", "contaminat", "harm")]),
    dict(id="e05_bird_decline", level=3, lo="2.1d",
         stem=f"After a farm starts using pesticides, the birds that eat insects there become fewer each year.\n\n{md_table(['year', 'birds counted'], [[1, 120], [2, 80], [3, 35]])}\n\nExplain the fall in bird numbers.",
         correct="the pesticide contaminates the insects, is passed along the food chain and builds up in the birds, poisoning them (and there are fewer insects to eat)",
         wrongs={"the birds moved away because of the noise": "The data follow the pesticide use; the chemical passes up the food chain.", "the pesticide makes the birds breed more": "Numbers FELL.", "fertiliser from the farm poisoned the birds": "The question says pesticide was used."},
         hints=["What do the birds eat?", "Where did the pesticide go after spraying?", "Along the food chain."],
         keypoints=[KP("passed along the food chain", "food chain", "eat", "insects", "passed", "transfer"), KP("poisoned / builds up", "poison", "build", "accumulat", "kill", "harm", "toxic")]),
    dict(id="e05_pH_soil_fix", level=3, lo="2.1a",
         stem=f"A gardener's tomatoes grow poorly. She tests the soil.\n\n{md_table(['test', 'result'], [['Universal Indicator', 'red'], ['pH meter', 3.5]])}\n\nTomatoes grow best at pH 6 to 7. What is wrong, and what could she do?",
         correct="the soil is far too acidic; she could add lime (an alkali) to raise the pH towards 6 to 7",
         wrongs={"the soil is alkaline; she should add acid": "Red and pH 3.5 mean strongly ACIDIC.", "the soil is neutral, so the problem is water": "pH 3.5 is not neutral.", "she should add more fertiliser": "Fertiliser does not correct the pH."},
         hints=["Red means strongly acidic.", "What does adding an alkali do to an acid?", "Raises the pH."],
         keypoints=[KP("too acidic", "acidic", "acid", "low ph", "3.5"), KP("add lime / alkali to raise pH", "lime", "alkali", "raise", "increase", "neutralis")]),
    dict(id="e05_haze_explain", level=3, lo="2.1d",
         stem=f"The table shows air readings in a city during a season when forests nearby are burnt to clear land.\n\n{md_table(['month', 'air quality', 'hospital visits for breathing problems'], [['June', 'good', 200], ['September', 'very unhealthy (haze)', 1400]])}\n\nExplain the link.",
         correct="burning forests (slash-and-burn) releases smoke that forms haze, and breathing the haze causes breathing difficulties",
         wrongs={"the hospital visits caused the haze": "The haze came first and caused the illness.", "September is simply a cold month": "The air quality reading shows haze from burning.", "fertiliser from the farms caused the haze": "Haze comes from smoke, not fertiliser."},
         hints=["What is produced when forests are burnt?", "Smoke → haze.", "What does haze do to people's lungs?"],
         keypoints=[KP("burning produces smoke / haze", "burn", "smoke", "haze", "fire"), KP("breathing difficulties", "breath", "lung", "asthma", "health", "respirat")]),
    dict(id="e05_herbicide_crop_safe", level=3, lo="2.1c",
         stem=f"A farmer sprays a herbicide over a field of maize. The table shows the result.\n\n{md_table(['plant', 'effect'], [['weeds', 'die'], ['maize', 'unaffected']])}\n\nWhy does the farmer want to kill the weeds, and why is the maize unaffected?",
         correct="weeds compete with the maize for light, water and nutrients; the herbicide is chosen to kill the weeds but not the crop",
         wrongs={"weeds eat the maize": "Weeds are plants; they compete for resources, they do not eat the crop.", "the maize is sprayed separately with fertiliser": "The herbicide itself is selective: it harms the weeds and not the crop.", "the herbicide is really a pesticide": "Herbicides kill plants (weeds); pesticides kill pests."},
         hints=["What do weeds take from the crop?", "Light, water and nutrients.", "Herbicides are designed to spare the crop."],
         keypoints=[KP("weeds compete for light / water / nutrients", "compet", "light", "water", "nutrient", "space"), KP("selective herbicide spares crop", "select", "not harm", "does not kill", "unaffected", "spare", "only kill")]),
    dict(id="e05_hormone_shipping", level=3, lo="2.1g",
         stem=f"Bananas are shipped green and treated on arrival.\n\n{md_table(['stage', 'treatment', 'state'], [['picked', 'none', 'green and hard'], ['shipped for 3 weeks', 'kept cool', 'still green'], ['warehouse', 'ripening hormone gas', 'yellow in 4 days']])}\n\nWhy is the hormone used only at the end?",
         correct="the hormone controls ripening, so the fruit stays firm for shipping and is ripened just before sale",
         wrongs={"the hormone kills insects on the fruit": "It is a plant hormone for ripening, not a pesticide.", "the hormone makes the bananas grow bigger on the ship": "It triggers ripening, not growth.", "green bananas cannot ripen without being replanted": "The hormone ripens them after picking."},
         hints=["What would happen if they ripened on the ship?", "They would be soft and spoil.", "Hormones let the farmer choose when the fruit ripens."],
         keypoints=[KP("hormone controls / triggers ripening", "ripen", "hormone"), KP("firm for transport / ripened before sale", "ship", "transport", "firm", "spoil", "sale", "sell", "market")]),

    # ------------------------------------------------------------ L4
    dict(id="e05_fish_farm_intensive", level=4, lo="2.1f",
         stem=f"A fish farm keeps thousands of fish in floating cages in the sea and feeds them pellets.\n\n{md_table(['item', 'value'], [['fish per cage', 5000], ['harvests per year', 3], ['wild fishing from the same area', 'a few hundred fish a year']])}\n\nWhich statement best explains why such farms are used?",
         correct="intensive farming produces far more food from the same area, which is needed as the population grows and space is limited",
         wrongs={"the fish grow larger in the wild": "Wild fishing yields far fewer fish.", "the cages protect the sea from pollution": "Feeding many fish in one place can pollute the water; the aim is food output.", "it is the only way to catch fish": "Wild fishing still exists, but gives much less."},
         hints=["Compare the numbers in the table.", "Why do we need so much more food?", "Growing population, limited space."],
         keypoints=[KP("more food from same space", "more food", "more fish", "same area", "same space", "limited space"), KP("growing population", "population", "more people")]),
    dict(id="e05_evaluate_fertiliser_timing", level=4, lo="2.1d",
         stem=f"A farmer records how much fertiliser is found in the river after two ways of applying it.\n\n{md_table(['method', 'fertiliser in river / mg per litre'], [['spread the whole amount in one day before rain', 18], ['spread small amounts over several dry weeks', 3]])}\n\nWhat is the best advice, and why?",
         correct="spread small amounts in dry weather, because less is washed off the fields into the river, so less algae and less oxygen loss",
         wrongs={"spread it all at once to save time": "That is when most ends up in the river.", "stop using fertiliser altogether": "Fertiliser is needed for yield; the aim is to use it without pollution.", "spread it before rain so the rain carries it to the roots": "Rain carries it INTO THE RIVER."},
         hints=["Compare the two rows.", "What carries fertiliser into the river?", "Rain and large amounts."],
         keypoints=[KP("small amounts / dry weather", "small", "dry", "little", "spread out", "several"), KP("less washed into river / less pollution", "wash", "river", "pollut", "algae", "run")]),
    dict(id="e05_pesticide_resistance_data", level=4, lo="2.1e",
         stem=f"A farmer sprays the same pesticide every year.\n\n{md_table(['year', 'pests killed / %'], [[1, 95], [3, 70], [5, 40]])}\n\nWhat is happening, and what could the farmer try?",
         correct="the pesticide is becoming less effective, so the farmer could use biological control with the pest's natural predators",
         wrongs={"the pesticide is getting stronger": "It kills FEWER pests each year.", "the pests have stopped eating the crop": "Fewer are killed; the pests are still there.", "the farmer should spray more of the same pesticide": "More chemical means more contamination and the trend may continue."},
         hints=["Read the percentage killed over the years.", "Is the spray working as well?", "What alternative uses no chemicals?"],
         keypoints=[KP("pesticide less effective", "less effective", "not working", "fewer", "falling", "resist"), KP("biological control / predators", "biological", "predator", "natural enem", "ladybird")]),
    dict(id="e05_erosion_mechanism", level=4, lo="2.1d",
         stem=f"Two hillsides are compared after a storm.\n\n{md_table(['hillside', 'cover', 'soil washed away / tonnes'], [['P', 'forest', 1], ['Q', 'cleared by slash-and-burn', 25]])}\n\nExplain the difference.",
         correct="tree roots hold the soil and leaves shield it from rain; without trees the rain washes the soil away (erosion)",
         wrongs={"the burnt soil is heavier so it moves more easily": "Soil washes away because nothing holds it, not because it is heavier.", "the forest soil is dry": "Both hillsides had the same storm.", "the ash made the soil slippery": "The missing roots and cover are the cause."},
         hints=["What do roots do for soil?", "What do leaves do for raindrops?", "Deforestation leads to erosion."],
         keypoints=[KP("roots hold soil", "root", "hold", "bind", "anchor"), KP("rain washes soil away without trees", "wash", "erosion", "rain", "no trees", "cleared")]),
    dict(id="e05_space_cities_vertical", level=4, lo="2.1b",
         stem=f"Singapore imports most of its food. The table shows two farms.\n\n{md_table(['farm', 'land area / hectares', 'vegetables per year / tonnes'], [['traditional field', 1, 20], ['vertical farm (stacked trays, LED lights)', 1, 180]])}\n\nWhy are vertical farms used in Singapore?",
         correct="land is very limited, so growing crops in stacked layers gives much more food from the same small area",
         wrongs={"vertical farms need no light": "They use LED lights because the trays are stacked indoors.", "traditional farms are illegal": "They are allowed but use too much land.", "vegetables taste better when stacked": "The reason is food production per area."},
         hints=["How much land does Singapore have for farming?", "Compare the yields per hectare.", "Stacking multiplies the growing area."],
         keypoints=[KP("limited land / space", "limited", "little land", "small", "space", "land"), KP("more food per area / stacked", "more food", "stack", "layer", "same area", "per hectare")]),
    dict(id="e05_ph_experiment_design", level=4, lo="2.1a",
         stem=f"A student wants to find the best soil pH for bean plants. The plan is shown.\n\n{md_table(['pot', 'soil pH', 'light', 'water per day'], [['1', 5, 'window', '50 ml'], ['2', 6, 'window', '50 ml'], ['3', 7, 'cupboard', '50 ml'], ['4', 8, 'window', '100 ml']])}\n\nWhat is wrong with the plan?",
         correct="pots 3 and 4 change other conditions (light, water), so any difference cannot be blamed on the pH alone",
         wrongs={"the pH values are too close together": "The problem is the other variables, not the pH steps.", "beans do not need light": "Beans need light; pot 3 in a cupboard is the problem.", "nothing; four pots is enough": "Only the pH should change between pots."},
         hints=["Which variable should be the only one changed?", "Look at the light and water columns.", "Fair test: keep everything else the same."],
         keypoints=[KP("other conditions changed / not fair", "fair", "other", "light", "water", "same", "control", "only"), KP("cannot tell if pH caused the difference", "cannot", "not sure", "blame", "cause", "due to")]),
    dict(id="e05_herbicide_runoff_pond", level=4, lo="2.1d",
         stem=f"A pond next to a field is tested before and after the field is sprayed with herbicide.\n\n{md_table(['time', 'water plants in pond', 'herbicide in water'], [['before spraying', 'many', 'none'], ['2 weeks after', 'most dead', 'present']])}\n\nExplain what happened.",
         correct="herbicide washed off the field into the pond and killed the water plants, contaminating the water",
         wrongs={"the herbicide fed the water plants": "Herbicides kill plants.", "the water plants died of old age": "The timing and the herbicide in the water point to contamination.", "the pond dried up": "The water was tested, so it was still there."},
         hints=["What does a herbicide do to plants?", "How did it get into the pond?", "Soil and water contamination."],
         keypoints=[KP("herbicide washed into pond", "wash", "run", "into the pond", "water", "contaminat"), KP("killed the plants", "kill", "die", "dead")]),
    dict(id="e05_compare_methods_table", level=4, lo="2.1c",
         stem=f"Four problems on a farm are listed.\n\n{md_table(['problem', 'method used'], [['poor soil', 'fertiliser'], ['insects eating leaves', 'pesticide'], ['weeds', 'herbicide'], ['fruit ripening at different times', 'plant hormone']])}\n\nWhich method has been matched correctly, and why do the others fit too?",
         correct="all four are correctly matched: each method targets the specific problem",
         wrongs={"only the fertiliser is correct": "Pesticides do kill insects, herbicides kill weeds and hormones control ripening.", "the pesticide and herbicide are swapped": "Pesticides kill pests (insects); herbicides kill weeds.", "the plant hormone should be used on the soil": "Hormones act on the plant's growth and ripening."},
         hints=["Check each row against what the method does.", "Pest → pesticide; weed → herbicide.", "Ripening → plant hormone."],
         keypoints=[KP("all correct", "all", "correct", "match", "each"), KP("each method targets its problem", "target", "specific", "pest", "weed", "nutrient", "ripen")]),

    # ------------------------------------------------------------ L5
    dict(id="e05_evaluate_slash_burn_decision", level=5, lo="2.1d",
         stem=f"A village must decide how to clear land for a new farm.\n\n{md_table(['option', 'cost', 'speed', 'effects'], [['slash-and-burn', 'low', 'days', 'haze, soil erosion later'], ['cut and remove trees, no burning', 'high', 'months', 'no haze, less erosion if some trees kept']])}\n\nWhich is the better evaluation?",
         correct="slash-and-burn is cheaper and faster but harms health and the soil for years, so the slower method is better in the long run",
         wrongs={"slash-and-burn is better because the ash feeds the crops": "The ash helps only the first harvest; erosion and haze last longer.", "the cost is all that matters": "Health and soil loss are costs too.", "neither method affects the environment": "Burning causes haze and erosion."},
         hints=["Compare the short-term and the long-term effects.", "Who is affected by haze?", "What happens to the soil in later years?"],
         keypoints=[KP("slash-and-burn cheaper / faster", "cheap", "fast", "quick", "low cost"), KP("long-term harm: haze, erosion", "haze", "erosion", "long", "health", "soil")]),
    dict(id="e05_integrated_pest_plan", level=5, lo="2.1e",
         stem=f"A farmer's records are shown.\n\n{md_table(['year', 'method', 'pests', 'bees in orchard', 'cost'], [[1, 'weekly pesticide', 'few', 'very few', 'high'], [2, 'predators released + pesticide only when pests are many', 'few', 'many', 'low']])}\n\nWhat is the best conclusion?",
         correct="using predators and spraying only when needed controls the pests just as well, protects the bees and costs less",
         wrongs={"weekly spraying is better because the pest count is lower": "The pest counts are both 'few'; weekly spraying killed the bees and cost more.", "predators alone can never control pests": "Year 2 shows they mostly can, with occasional spraying.", "bees are pests and should be killed": "Bees pollinate the orchard; losing them cuts the fruit crop."},
         hints=["Compare pests, bees and cost across the years.", "Which year is better in every column?", "Biological control reduces the need for pesticide."],
         keypoints=[KP("predators / less pesticide controls pests", "predator", "biological", "less pesticide", "only when"), KP("protects bees / costs less", "bee", "cost", "cheaper", "wildlife")]),
    dict(id="e05_fertiliser_trade_off", level=5, lo="2.1d",
         stem=f"A government must decide whether to limit fertiliser use near rivers.\n\n{md_table(['fertiliser use near rivers', 'crop yield', 'river fish catch', 'drinking water treatment cost'], [['unlimited', 'high', 'very low', 'high'], ['limited', 'slightly lower', 'high', 'low']])}\n\nWhich is the best evaluation?",
         correct="limiting fertiliser near rivers costs a little yield but keeps the fish and the drinking water clean, so it is the better choice",
         wrongs={"unlimited use is best because yield matters most": "The lost fish and the cost of cleaning water outweigh the small yield gain.", "fertiliser should be banned everywhere": "The table only concerns land near rivers; fertiliser is still needed elsewhere.", "fertiliser has no effect on rivers": "The fish catch and water cost change with fertiliser use."},
         hints=["Look at all four columns.", "How big is the yield loss compared with the other changes?", "Weigh food against water and fish."],
         keypoints=[KP("limit near rivers", "limit", "restrict", "reduce", "less"), KP("protects fish / water; small yield loss", "fish", "water", "clean", "slightly", "small loss")]),
    dict(id="e05_gm_variety_evaluate", level=5, lo="2.1f",
         stem=f"A new rice variety is offered to farmers.\n\n{md_table(['feature', 'old variety', 'new variety'], [['yield per hectare', '4 t', '7 t'], ['needs fertiliser', 'little', 'a lot'], ['resists flooding', 'no', 'yes'], ['seed cost', 'low', 'high']])}\n\nWhich is the best evaluation for a farmer in a flood-prone area?",
         correct="the new variety gives more rice and survives floods, but needs more fertiliser and costly seed, so it is worth it if the extra rice pays for these",
         wrongs={"the new variety is better in every way": "It needs more fertiliser and the seed costs more.", "the old variety is better because it is cheaper": "In a flood-prone area the old variety may be lost to flooding.", "yield does not matter for a farmer": "Yield is the farmer's income and food."},
         hints=["List the pros and cons of the new variety.", "Which matter most in a flood-prone area?", "Weigh the extra cost against the extra rice."],
         keypoints=[KP("more yield / flood resistant", "yield", "more rice", "flood", "survive"), KP("needs more fertiliser / costly seed", "fertiliser", "cost", "expensive", "seed")]),
    dict(id="e05_algae_sequence_evaluate", level=5, lo="2.1d",
         stem=f"A student lists the steps of fertiliser pollution but in the wrong order.\n\n{md_table(['letter', 'step'], [['P', 'fish die'], ['Q', 'fertiliser washes into the river'], ['R', 'algae bloom blocks sunlight'], ['S', 'underwater plants die and oxygen falls']])}\n\nWhat is the correct order, and why does S come before P?",
         correct="Q, R, S, P: the plants die first and stop making oxygen, and only then do the fish run out of oxygen",
         wrongs={"P, Q, R, S": "Fish die LAST, after the oxygen falls.", "Q, S, R, P": "The algae bloom must block the sunlight before the plants die.", "R, Q, S, P": "The fertiliser must reach the river before the algae can bloom."},
         hints=["What arrives first?", "What do algae block?", "What happens to oxygen when plants die?"],
         keypoints=[KP("order Q R S P", "q, r, s, p", "qrsp", "q r s p"), KP("plants stop making oxygen before fish die", "oxygen", "plants", "photosynth")]),
    dict(id="e05_soil_test_method_evaluate", level=5, lo="2.1a",
         stem=f"Three ways of testing soil pH are compared.\n\n{md_table(['method', 'result', 'precision'], [['litmus paper', 'acidic or alkaline only', 'low'], ['Universal Indicator', 'colour → pH to about 1 unit', 'medium'], ['pH meter', 'e.g. 6.4', 'high']])}\n\nA farmer wants to know whether soil at pH about 6 needs lime to reach 6.5. Which method should be used, and why?",
         correct="the pH meter, because it gives a precise number; litmus and Universal Indicator cannot tell 6.0 from 6.5",
         wrongs={"litmus paper, because it is the simplest": "It only says acidic or alkaline.", "Universal Indicator, because colours are easy to read": "It cannot separate pH 6.0 from 6.5.", "any method, because they all give the pH": "Only the meter gives a precise value."},
         hints=["How precise does the farmer need to be?", "Which method gives a number with a decimal?", "The pH meter."],
         keypoints=[KP("pH meter", "meter"), KP("precise / exact value needed", "precise", "exact", "accurate", "decimal", "small difference", "6.5")]),
    dict(id="e05_weed_hormone_vs_herbicide", level=5, lo="2.1g",
         stem=f"A farmer compares two weed-control products on a lawn.\n\n{md_table(['product', 'effect on broad-leaved weeds', 'effect on grass'], [['general herbicide', 'die', 'dies'], ['plant hormone weed killer', 'grow abnormally and die', 'unaffected']])}\n\nWhich product should be used on the lawn, and why?",
         correct="the plant hormone weed killer, because it kills the weeds while leaving the grass unharmed",
         wrongs={"the general herbicide, because it kills everything": "Killing the grass defeats the purpose of a lawn.", "neither, because weeds are harmless": "Weeds compete with the grass for light, water and nutrients.", "the plant hormone, because it feeds the grass": "It does not feed the grass; it simply does not harm it."},
         hints=["What must survive on a lawn?", "Which product leaves the grass alone?", "Selective action."],
         keypoints=[KP("plant hormone weed killer", "hormone"), KP("grass unharmed / selective", "grass", "unharm", "not kill", "select", "leave")]),
    dict(id="e05_vertical_farm_tradeoff", level=5, lo="2.1f",
         stem=f"A company proposes a vertical farm in a warehouse.\n\n{md_table(['item', 'vertical farm', 'open field'], [['vegetables per hectare per year', '180 t', '20 t'], ['electricity for lights', 'very high', 'none'], ['pesticide needed', 'none (indoors)', 'yes'], ['land needed for 180 t', '1 ha', '9 ha']])}\n\nWhich is the best evaluation?",
         correct="the vertical farm gives far more food from little land without pesticides, but its electricity use is high, so it suits a small, land-scarce country best",
         wrongs={"the open field is better because it uses no electricity": "It needs nine times the land and pesticides.", "the vertical farm is better in every way": "Its electricity use is very high.", "both produce the same amount of food per hectare": "180 t against 20 t is nine times more."},
         hints=["List the advantages of the vertical farm.", "List its disadvantage.", "Where would it be worth it?"],
         keypoints=[KP("more food per land / no pesticide", "more food", "180", "little land", "small area", "no pesticide"), KP("high electricity use", "electricity", "energy", "cost", "lights")]),
]

register_explain(EXPLAIN, chapter=5)
