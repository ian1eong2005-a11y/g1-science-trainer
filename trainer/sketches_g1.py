"""Extra sketches for the G1 Science trainer (waves, chromatography, breathing, forces on blocks, transformers)."""
import io
import math

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyArrowPatch, Rectangle, Ellipse  # noqa: E402


def _fig(w, h):
    fig, ax = plt.subplots(figsize=(w, h), dpi=150)
    ax.set_axis_off()
    return fig, ax


def _png(fig, pad=0.06):
    buf = io.BytesIO()
    fig.savefig(buf, format="png", bbox_inches="tight", pad_inches=pad, facecolor="white")
    plt.close(fig)
    return buf.getvalue()


def _arrow(ax, p0, p1, lw=1.6, ms=12, color="black"):
    ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle="-|>", mutation_scale=ms, lw=lw, color=color))


def wave(amplitude_cm, wavelength_cm, n_waves=2.5, show="both", size=(5.4, 2.8)):
    """A wave on a rope drawn on a cm grid. show: 'both' | 'amplitude' | 'wavelength' | 'none' (which labels to mark)."""
    fig, ax = plt.subplots(figsize=size, dpi=150)
    L = wavelength_cm * n_waves
    xs = [i * L / 400 for i in range(401)]
    ys = [amplitude_cm * math.sin(2 * math.pi * x / wavelength_cm) for x in xs]
    ax.plot(xs, ys, color="black", lw=1.8)
    ax.axhline(0, color="grey", lw=0.8, ls="--")
    ax.set_xlim(0, L)
    ax.set_ylim(-amplitude_cm * 1.6 - 0.5, amplitude_cm * 1.6 + 0.5)
    ax.set_xlabel("distance along rope / cm")
    ax.set_ylabel("displacement / cm")
    ax.grid(True, lw=0.4, color="#bbbbbb")
    if show in ("both", "amplitude"):
        x0 = wavelength_cm / 4
        _arrow(ax, (x0, 0), (x0, amplitude_cm), ms=10)
        _arrow(ax, (x0, amplitude_cm), (x0, 0), ms=10)
        ax.text(x0 + L * 0.02, amplitude_cm / 2, "P", fontsize=10, va="center")
    if show in ("both", "wavelength"):
        x1, x2 = wavelength_cm / 4, wavelength_cm * 5 / 4
        y = amplitude_cm * 1.3
        _arrow(ax, (x1, y), (x2, y), ms=10)
        _arrow(ax, (x2, y), (x1, y), ms=10)
        ax.text((x1 + x2) / 2, y + amplitude_cm * 0.12, "Q", fontsize=10, ha="center")
    return _png(fig)


def chromatogram(spots, size=(4.2, 3.2)):
    """Paper chromatogram. spots: list of (label, [heights 0-1]) columns. Colours as grey circles."""
    fig, ax = _fig(*size)
    n = len(spots)
    ax.add_patch(Rectangle((0, 0), n + 1, 4.2, fill=False, lw=1.4))
    ax.plot([0, n + 1], [0.5, 0.5], color="black", lw=1, ls="--")
    ax.text(n + 1.05, 0.5, "start line", fontsize=8, va="center")
    ax.plot([0, n + 1], [3.9, 3.9], color="grey", lw=0.8, ls=":")
    ax.text(n + 1.05, 3.9, "solvent front", fontsize=8, va="center")
    for i, (label, hs) in enumerate(spots):
        x = i + 1
        ax.text(x, -0.25, label, ha="center", fontsize=10, fontweight="bold")
        for h in hs:
            ax.add_patch(Ellipse((x, 0.5 + 3.3 * h), 0.42, 0.3, color="#555555"))
    ax.set_xlim(-0.2, n + 2.4)
    ax.set_ylim(-0.6, 4.5)
    return _png(fig)


def block_forces(cases, size=(6.0, 2.2)):
    """Blocks viewed from above, each with two horizontal/vertical forces. cases: list of (letter, [(dir, N), ...]);
    dir in 'left','right','up','down'."""
    fig, ax = _fig(*size)
    for i, (letter, forces) in enumerate(cases):
        cx = i * 3.2 + 1.6
        ax.add_patch(Rectangle((cx - 0.5, 0.5), 1.0, 1.0, fill=True, fc="#e8e8e8", ec="black", lw=1.4))
        ax.text(cx, 2.1, letter, ha="center", fontsize=11, fontweight="bold")
        for d, n in forces:
            if d == "left":
                _arrow(ax, (cx + 0.5, 1.0), (cx + 1.5, 1.0)); ax.text(cx + 1.0, 1.15, f"{n} N", ha="center", fontsize=8)
            elif d == "right":
                _arrow(ax, (cx - 0.5, 1.0), (cx - 1.5, 1.0)); ax.text(cx - 1.0, 1.15, f"{n} N", ha="center", fontsize=8)
            elif d == "up":
                _arrow(ax, (cx, 0.5), (cx, -0.4)); ax.text(cx + 0.12, -0.1, f"{n} N", fontsize=8)
            elif d == "down":
                _arrow(ax, (cx, 1.5), (cx, 2.4)); ax.text(cx + 0.12, 2.1, f"{n} N", fontsize=8)
    ax.set_xlim(-0.2, len(cases) * 3.2)
    ax.set_ylim(-0.7, 2.7)
    ax.invert_yaxis()
    return _png(fig)


def pushes(forces, size=(4.6, 1.8)):
    """One block with pushes from the left and right. forces: (left_N, right_N) (left pushes to the right)."""
    fig, ax = _fig(*size)
    ax.add_patch(Rectangle((2.0, 0.3), 1.4, 1.0, fc="#e8e8e8", ec="black", lw=1.4))
    ax.text(2.7, 0.8, "block", ha="center", va="center", fontsize=9)
    l, r = forces
    if l:
        _arrow(ax, (0.6, 0.8), (1.95, 0.8), lw=2); ax.text(1.25, 1.0, f"{l} N", ha="center", fontsize=9)
    if r:
        _arrow(ax, (4.8, 0.8), (3.45, 0.8), lw=2); ax.text(4.1, 1.0, f"{r} N", ha="center", fontsize=9)
    ax.plot([0.2, 5.2], [0.3, 0.3], color="black", lw=1)
    ax.set_xlim(0, 5.4)
    ax.set_ylim(0, 1.6)
    return _png(fig)


def transmission(size=(6.4, 2.0)):
    """Power station -> step-up transformer -> transmission lines -> step-down transformer -> homes."""
    fig, ax = _fig(*size)
    boxes = [("power\nstation", 0.4), ("step-up\ntransformer", 1.9), ("high-voltage\ntransmission lines", 3.6), ("step-down\ntransformer", 5.5), ("homes\n230 V", 7.0)]
    for i, (t, x) in enumerate(boxes):
        w = 1.2 if i != 2 else 1.5
        ax.add_patch(Rectangle((x, 0.3), w, 1.0, fc="white", ec="black", lw=1.3))
        ax.text(x + w / 2, 0.8, t, ha="center", va="center", fontsize=8)
        if i < len(boxes) - 1:
            nx = boxes[i + 1][1]
            _arrow(ax, (x + w, 0.8), (nx, 0.8))
    ax.set_xlim(0.2, 8.4)
    ax.set_ylim(0, 1.6)
    return _png(fig)


def lungs(label=None, size=(3.6, 3.6)):
    """Schematic respiratory system with letters at the windpipe, bronchus, lung, diaphragm and ribcage."""
    fig, ax = _fig(*size)
    ax.plot([5, 5], [9.5, 6.5], color="black", lw=4)                      # windpipe
    ax.plot([5, 3.6], [6.5, 5.3], color="black", lw=3)                    # bronchi
    ax.plot([5, 6.4], [6.5, 5.3], color="black", lw=3)
    ax.add_patch(Ellipse((3.1, 4.0), 2.8, 4.6, fc="#f2dede", ec="black", lw=1.4))   # lungs
    ax.add_patch(Ellipse((6.9, 4.0), 2.8, 4.6, fc="#f2dede", ec="black", lw=1.4))
    for y in (7.2, 6.2, 5.2, 4.2, 3.2):                                   # ribs
        ax.plot([1.2, 8.8], [y, y], color="#888888", lw=1.2)
    xs = [i / 10 for i in range(14, 87)]
    ax.plot(xs, [1.6 + 0.4 * math.sin(math.pi * (x - 1.4) / 7.2) for x in xs], color="black", lw=2.5)  # diaphragm
    pts = {"P": (5.6, 8.6), "Q": (6.3, 5.9), "R": (7.8, 3.0), "S": (5.0, 1.1), "T": (9.2, 5.2)}
    for k, (x, y) in pts.items():
        ax.text(x, y, k, fontsize=11, fontweight="bold")
    if label:
        ax.text(5, 10.3, label, ha="center", fontsize=9)
    ax.set_xlim(0.5, 10)
    ax.set_ylim(0.5, 10.8)
    return _png(fig)


def heart_loop(size=(4.8, 3.2)):
    """Double circulation: heart in the middle, lungs above, body below, lettered vessels."""
    fig, ax = _fig(*size)
    ax.add_patch(Rectangle((3.2, 1.6), 1.6, 1.2, fc="#f7d7d7", ec="black", lw=1.4)); ax.text(4.0, 2.2, "heart", ha="center", va="center", fontsize=9)
    ax.add_patch(Rectangle((3.0, 3.8), 2.0, 0.8, fc="#eeeeee", ec="black", lw=1.2)); ax.text(4.0, 4.2, "lungs", ha="center", va="center", fontsize=9)
    ax.add_patch(Rectangle((3.0, -0.2), 2.0, 0.8, fc="#eeeeee", ec="black", lw=1.2)); ax.text(4.0, 0.2, "rest of body", ha="center", va="center", fontsize=9)
    _arrow(ax, (4.6, 2.8), (4.6, 3.8)); ax.text(4.75, 3.3, "W", fontsize=10, fontweight="bold")
    _arrow(ax, (3.4, 3.8), (3.4, 2.8)); ax.text(2.9, 3.3, "X", fontsize=10, fontweight="bold")
    _arrow(ax, (3.4, 1.6), (3.4, 0.6)); ax.text(2.9, 1.0, "Y", fontsize=10, fontweight="bold")
    _arrow(ax, (4.6, 0.6), (4.6, 1.6)); ax.text(4.75, 1.0, "Z", fontsize=10, fontweight="bold")
    ax.set_xlim(2.4, 5.8)
    ax.set_ylim(-0.4, 4.8)
    return _png(fig)


def dt_graph(segments, xmax=None, ymax=None, xstep=None, ystep=None, size=(4.8, 3.0), labels=True):
    """Distance-time graph from segments [(t0, d0), (t1, d1), ...] joined by straight lines, letters at the corners."""
    fig, ax = plt.subplots(figsize=size, dpi=150)
    xs = [p[0] for p in segments]; ys = [p[1] for p in segments]
    ax.plot(xs, ys, color="black", lw=1.8)
    if labels:
        for i, (x, y) in enumerate(segments):
            ax.text(x, y + (ymax or max(ys)) * 0.04, "OPQRSTUV"[i], fontsize=10, ha="center")
    ax.set_xlim(0, xmax or max(xs)); ax.set_ylim(0, ymax or max(ys) * 1.15)
    ax.set_xlabel("time / s"); ax.set_ylabel("distance / m")
    if xstep: ax.set_xticks([i * xstep for i in range(int((xmax or max(xs)) / xstep) + 1)])
    if ystep: ax.set_yticks([i * ystep for i in range(int((ymax or max(ys) * 1.15) / ystep) + 1)])
    ax.grid(True, lw=0.4, color="#bbbbbb")
    return _png(fig)


def multimeter(reading, unit, size=(2.6, 2.2)):
    """Digital multimeter face showing a reading and the selected unit."""
    fig, ax = _fig(*size)
    ax.add_patch(Rectangle((0, 0), 4, 3.4, fc="#f4f4f4", ec="black", lw=1.5))
    ax.add_patch(Rectangle((0.4, 2.0), 3.2, 1.0, fc="#dfe9dc", ec="black", lw=1))
    ax.text(3.4, 2.5, f"{reading} {unit}", ha="right", va="center", fontsize=14, family="monospace")
    ax.text(2.0, 1.2, "V    A    Ω", ha="center", fontsize=10)
    ax.add_patch(Ellipse((2.0, 1.2), 1.3, 1.3, fill=False, lw=1))
    ax.text(2.0, 0.3, "multimeter", ha="center", fontsize=8)
    ax.set_xlim(-0.1, 4.1); ax.set_ylim(-0.1, 3.5)
    return _png(fig)


def joint(size=(3.2, 3.0)):
    """Schematic joint: two bones, cartilage ends, ligament, lettered."""
    fig, ax = _fig(*size)
    ax.add_patch(Rectangle((1.4, 3.4), 1.2, 2.6, fc="#fff4d6", ec="black", lw=1.3))
    ax.add_patch(Rectangle((1.4, 0.0), 1.2, 2.6, fc="#fff4d6", ec="black", lw=1.3))
    ax.add_patch(Ellipse((2.0, 3.4), 1.4, 0.5, fc="#cfe3ff", ec="black", lw=1))
    ax.add_patch(Ellipse((2.0, 2.6), 1.4, 0.5, fc="#cfe3ff", ec="black", lw=1))
    ax.plot([0.9, 0.7, 0.9], [4.2, 3.0, 1.8], color="#b05030", lw=3)
    ax.plot([3.1, 3.3, 3.1], [4.2, 3.0, 1.8], color="#b05030", lw=3)
    ax.text(2.0, 5.0, "P", fontsize=11, fontweight="bold", ha="center")
    ax.text(2.85, 3.5, "Q", fontsize=11, fontweight="bold")
    ax.text(0.25, 3.0, "R", fontsize=11, fontweight="bold")
    ax.set_xlim(0, 4); ax.set_ylim(-0.2, 6.2)
    return _png(fig)
