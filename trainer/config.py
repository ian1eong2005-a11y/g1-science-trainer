"""Constants for the G1 Science (3NT) adaptive trainer. Change class lists and rules here only."""

APP_TITLE = "G1 Science Trainer"
SCHOOL = "Queenstown Secondary School"

# Login dropdown, grouped by level. To add a class, add its name to the right list.
CLASSES = {
    "Sec 3": ["3NT1", "3NT2"],
    "Sec 4": ["4NT1", "4NT2"],
}
CLASS_LIST = [c for group in CLASSES.values() for c in group]

# G1 Science, syllabus K123 (Secondary Education Certificate 2027), numbered as the school's chapter notes (Chap 1-11).
# Syllabus topic codes in brackets; learning-outcome tags are "<topic><letter>", e.g. "1.2m" = 1.2 Electricity (m) cost in kWh.
CHAPTERS = {
    1: "Energy",                      # 1.1
    2: "Electricity",                 # 1.2
    3: "Wave",                        # 1.3
    4: "Effects of Force",            # 1.4
    5: "Sources of Food",             # 2.1
    6: "Food Chemistry",              # 2.2
    7: "Food Safety",                 # 2.3
    8: "Staying Healthy",             # 3.1
    9: "Digestion",                   # 3.2
    10: "Breathing",                  # 3.3
    11: "Blood Circulation",          # 3.4
}
TOPIC_OF = {1: "1.1", 2: "1.2", 3: "1.3", 4: "1.4", 5: "2.1", 6: "2.2", 7: "2.3", 8: "3.1", 9: "3.2", 10: "3.3", 11: "3.4"}
SECTIONS = {"1": "Machines Around Us (II)", "2": "Food Matters", "3": "Our Body and Health (II)"}

CATEGORIES = {
    "calc": "Calculation & data",
    "explain": "Explanation",
    "nlevel": "N level exam practice",
}

LEVEL_NAMES = {
    1: "L1 - one formula or one reading",
    2: "L2 - one conversion, reading or rearrangement",
    3: "L3 - two steps, with a figure or table",
    4: "L4 - graphs and data interpretation",
    5: "L5 - multi-step, unfamiliar context or a trap",
}
EXPLAIN_LEVEL_NAMES = {
    1: "L1 - recall and definitions",
    2: "L2 - identify and classify",
    3: "L3 - apply a concept",
    4: "L4 - explain with reasoning",
    5: "L5 - evaluate and predict",
}
NLEVEL_LEVEL_NAMES = {
    1: "L1 - recall a fact (exam style)",
    2: "L2 - one step: a rule or a formula",
    3: "L3 - read a diagram, table or graph",
    4: "L4 - link two ideas or interpret an experiment",
    5: "L5 - unfamiliar context, or a trap in the data",
}

# Adaptive rules (the teacher's rules for the other QTSS trainers, 24 Oct 2026)
UP_STREAK = 5          # correct in a row at a level -> level + 1
DOWN_STREAK = 3        # wrong in a row at a level -> level - 1
MIN_LEVEL, MAX_LEVEL = 1, 5
START_LEVEL = 1
RECENT_AVOID = 10      # do not repeat any of the last N template ids

ONLINE_SECONDS = 120   # "online" on the dashboard if active within this many seconds
DASHBOARD_REFRESH_S = 5

DEFAULT_TEACHER_PASSWORD = "science"   # used only when no TEACHER_PASSWORD secret / env var is set

G = 10.0               # N/kg, as used in school papers
