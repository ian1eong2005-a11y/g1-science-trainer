# G1 Science Trainer (3NT)

Adaptive self-study trainer for G1 Science, syllabus **K123** (Secondary Education Certificate 2027), for the 3NT / Sec 3 G1
classes at Queenstown Secondary School. Streamlit app, no database. Built from the Sec 2 Science trainer (same engine, store,
marker and UIs); content written for the K123 learning outcomes, from the school's chapter worksheets and the SEAB 5148 papers.

**Scope so far: Chapters 1-5** (Section I Machines Around Us (II) and topic 2.1). Chapters 6-11 are listed in the app but hold no
questions yet; the test suite only requires Chapters 1-5.

| Ch | Topic (K123 code) | Calculation & data | Explanation | N level exam practice |
|---|---|---|---|---|
| 1 | Energy (1.1) | yes | yes | yes |
| 2 | Electricity (1.2) | yes | yes | yes |
| 3 | Wave (1.3) | yes | yes | yes |
| 4 | Effects of Force (1.4) | yes | yes | yes |
| 5 | Sources of Food (2.1) | data questions | yes | yes |
| 6-11 | Food Chemistry, Food Safety, Staying Healthy, Digestion, Breathing, Blood Circulation | not yet | not yet | not yet |

## How it works

- Students log in with **name + class** (no password). Teacher view is password protected.
- Three categories:
  - **Calculation & data**: parametrised templates, numbers change on every serve, every question has a diagram or a table.
    Each chapter has at least 4 per level, with extra sets adapted from the school worksheets (`chNNw.py`): the worksheet
    calculation questions (power, energy, kWh and cost, speed, acceleration, net force, waves) are all covered, with new numbers.
  - **Explanation**: fixed MCQs, options reshuffled on every serve. From L3 up the student first answers in their own words and a
    scripted checker (`trainer/marking.py`, no LLM) looks for the key ideas.
  - **N level exam practice**: MCQs adapted from the SEAB 5148 N(T) Science specimen Paper 1 (2024) and the 2013-2023 Paper 1
    papers, Chapters 1-5 only. Adapted, never copied (the repo is public): contexts kept, numbers changed and varied, picture
    options turned into words or redrawn. Each question names its source under the working.
- **5 correct in a row → level up. 3 wrong in a row → level down.** Everyone starts at L1. Only the first attempt counts.
- A wrong answer opens the scripted **tutor**: a message about the chosen option, up to 3 hints, the formula / key fact on request,
  then one retry (correct retries never count towards the streak). Explanation L1 questions come back until answered correctly.
- **Teacher dashboard** (sidebar → Teacher, or `?teacher=1`): who is online, levels, streaks, accuracy, last 20 attempts,
  reset / clear / CSV. Data lives in memory only and disappears when the app restarts.
- Every question shows its learning-outcome code (e.g. `1.2m` = topic 1.2 Electricity, outcome (m): cost in kWh).

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

Default local teacher password is `science`. Set `TEACHER_PASSWORD` as an environment variable or in `.streamlit/secrets.toml`.

## Deploy on Streamlit Community Cloud

1. share.streamlit.io → **Create app** → this repo, branch `main`, main file `app.py`.
2. Advanced settings → **Secrets**: `TEACHER_PASSWORD = "choose-something"`.
3. Deploy. Every push to `main` redeploys automatically; live data is cleared on each redeploy.

## Tests

```bash
python -m pytest -q
```

`tests/test_content.py` builds every template with 20 seeds (four distinct options, key present, a misconception message for every
wrong option, three hints, a figure or a table, no hint that gives the answer away) and checks the minimum inventory per chapter and
level; `tests/test_engine.py` the level rules; `tests/test_marking.py` the own-words checker; `tests/test_app.py` the app end to end.

## Adding a question

- **Calculation / data**: one function per template in `trainer/content/chNN.py` (or `chNNw.py` for worksheet sets), decorated
  `@template("id", chapter=N, level=L, lo="1.2m")`. Drawers: `trainer/figs.py`, `trainer/sketches.py`, `trainer/sketches_g1.py`.
- **Explanation**: a dict in the chapter's `EXPLAIN` list; L3-L5 items carry `keypoints` for own-words marking.
- **N level practice**: `trainer/content/nlevel_specimen.py`, `nlevel_past.py` (category `nlevel`).
- Register new modules in `trainer/content/__init__.py` (`MODULES`), then run the tests.

## Layout

```
app.py                      entry point: login, routing
trainer/config.py           classes, chapters (K123 numbering), categories, rules (5 up / 3 down)
trainer/engine.py           adaptive rules
trainer/store.py            in-memory live store shared by all sessions
trainer/marking.py          meaning-based marker for own-words answers
trainer/figs.py, sketches.py, sketches_g1.py   drawers
trainer/content/            ch01..ch05 (+ ch01w..ch04w worksheet sets), nlevel_specimen, nlevel_past
trainer/ui_student.py       student screen + tutor panel
trainer/ui_teacher.py       live dashboard
tests/                      pytest
```
