"""
Generate architecture diagrams for the COMPSCI 714 exam prep book.
Run from compsci-714/ with: uv run python exam/generate_diagrams.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
import numpy as np
from pathlib import Path

OUT = Path(__file__).parent / "src" / "images"
OUT.mkdir(parents=True, exist_ok=True)

BLUE   = "#4A90D9"
GREEN  = "#5CB85C"
ORANGE = "#F0AD4E"
RED    = "#D9534F"
PURPLE = "#9B59B6"
GRAY   = "#95A5A6"
DARK   = "#2C3E50"
WHITE  = "#FFFFFF"
BG     = "#F8F9FA"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 11,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.spines.left": False,
    "axes.spines.bottom": False,
    "figure.facecolor": BG,
    "axes.facecolor": BG,
})


def box(ax, x, y, w, h, label, color=BLUE, fontsize=10, textcolor=WHITE, radius=0.05):
    rect = FancyBboxPatch((x - w/2, y - h/2), w, h,
                          boxstyle=f"round,pad=0,rounding_size={radius}",
                          facecolor=color, edgecolor=DARK, linewidth=1.2, zorder=3)
    ax.add_patch(rect)
    ax.text(x, y, label, ha="center", va="center", fontsize=fontsize,
            color=textcolor, fontweight="bold", zorder=4)


def arrow(ax, x1, y1, x2, y2, color=DARK, lw=1.5):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="-|>", color=color,
                                lw=lw, mutation_scale=14), zorder=2)


def label(ax, x, y, text, fontsize=9, color=DARK, ha="center", va="center"):
    ax.text(x, y, text, ha=ha, va=va, fontsize=fontsize, color=color, zorder=5)


# ─────────────────────────────────────────────
# 1. Transformer Encoder Block
# ─────────────────────────────────────────────
def draw_transformer_encoder():
    fig, ax = plt.subplots(figsize=(5, 9))
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 10)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.patch.set_facecolor(BG)

    # Input
    box(ax, 2.5, 0.6, 2.2, 0.55, "Input Embeddings\n+ Positional Encoding", BLUE, 9)

    # Self-Attention block
    box(ax, 2.5, 2.0, 2.2, 0.55, "Multi-Head\nSelf-Attention", ORANGE, 9)
    arrow(ax, 2.5, 0.88, 2.5, 1.72)

    # Add & Norm 1
    box(ax, 2.5, 3.1, 2.2, 0.45, "Add & Norm", GREEN, 9)
    arrow(ax, 2.5, 2.28, 2.5, 2.87)

    # Residual skip 1
    ax.annotate("", xy=(3.9, 2.87), xytext=(3.9, 0.88),
                arrowprops=dict(arrowstyle="-|>", color=RED, lw=1.5,
                                connectionstyle="arc3,rad=0", mutation_scale=12))
    ax.plot([2.5+1.1, 3.9], [0.88, 0.88], color=RED, lw=1.5, zorder=2)
    label(ax, 4.25, 1.9, "residual", 8, RED)

    # FFN
    box(ax, 2.5, 4.4, 2.2, 0.55, "Feed-Forward\nNetwork (FFN)", ORANGE, 9)
    arrow(ax, 2.5, 3.33, 2.5, 4.12)

    # Add & Norm 2
    box(ax, 2.5, 5.5, 2.2, 0.45, "Add & Norm", GREEN, 9)
    arrow(ax, 2.5, 4.68, 2.5, 5.27)

    # Residual skip 2
    ax.annotate("", xy=(3.9, 5.27), xytext=(3.9, 3.33),
                arrowprops=dict(arrowstyle="-|>", color=RED, lw=1.5, mutation_scale=12))
    ax.plot([2.5+1.1, 3.9], [3.33, 3.33], color=RED, lw=1.5, zorder=2)

    # Output
    box(ax, 2.5, 6.6, 2.2, 0.45, "Encoder Output", BLUE, 9)
    arrow(ax, 2.5, 5.72, 2.5, 6.37)

    # Repeat N label
    rect = FancyBboxPatch((0.3, 1.5), 4.4, 4.4,
                          boxstyle="round,pad=0,rounding_size=0.1",
                          facecolor="none", edgecolor=PURPLE,
                          linewidth=1.5, linestyle="--", zorder=1)
    ax.add_patch(rect)
    label(ax, 0.7, 5.7, "×N", 13, PURPLE, ha="left")

    ax.set_title("Transformer Encoder Block", fontsize=13, fontweight="bold",
                 color=DARK, pad=10)
    plt.tight_layout()
    fig.savefig(OUT / "transformer_encoder.png", dpi=150, bbox_inches="tight",
                facecolor=BG)
    plt.close()
    print("  transformer_encoder.png")


# ─────────────────────────────────────────────
# 1b. ViT Pipeline
# ─────────────────────────────────────────────
def draw_vit_pipeline():
    fig, ax = plt.subplots(figsize=(14, 5))
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 6)
    ax.axis("off")
    fig.patch.set_facecolor(BG)

    # Step 1: Image
    box(ax, 1.0, 3.0, 1.6, 2.0, "Image\n224x224x3", BLUE, 9)

    # Step 2: Patches
    arrow(ax, 1.8, 3.0, 2.6, 3.0)
    # Draw patch grid
    gx, gy, gs = 3.2, 2.2, 0.35
    for i in range(4):
        for j in range(4):
            rect = FancyBboxPatch((gx + j * gs, gy + i * gs), gs - 0.04, gs - 0.04,
                                  boxstyle="round,pad=0,rounding_size=0.02",
                                  facecolor=ORANGE, edgecolor=WHITE, lw=0.8, alpha=0.75)
            ax.add_patch(rect)
    label(ax, gx + 2 * gs, 4.0, "14x14 = 196\npatches", 8, DARK)

    # Step 3: Linear projection
    arrow(ax, 4.7, 3.0, 5.3, 3.0)
    box(ax, 6.2, 3.0, 1.6, 1.2, "Linear\nProjection\n(learned)", ORANGE, 8.5)
    label(ax, 6.2, 1.9, "768 -> D dim", 7.5, GRAY)

    # Step 4: [CLS] + Pos Enc
    arrow(ax, 7.0, 3.0, 7.7, 3.0)
    # CLS token
    box(ax, 8.2, 4.2, 0.8, 0.5, "[CLS]", PURPLE, 8)
    arrow(ax, 8.2, 3.95, 8.2, 3.5)
    # Patch embeddings
    for i in range(5):
        c = BLUE if i < 4 else GRAY
        lbl = f"P{i+1}" if i < 4 else "..."
        box(ax, 8.2 + (i + 1) * 0.55, 3.0, 0.45, 0.45, lbl, c, 7)
    label(ax, 9.5, 2.2, "+ Positional\n  Embeddings", 8, GREEN)
    box(ax, 9.5, 1.5, 2.0, 0.4, "197 tokens total", DARK, 7.5, WHITE)

    # Step 5: Transformer Encoder
    arrow(ax, 11.2, 3.0, 11.7, 3.0)
    box(ax, 12.5, 3.0, 1.4, 1.6, "Transformer\nEncoder\n(x N)", GREEN, 9)

    # Step 6: MLP Head (only CLS)
    arrow(ax, 13.2, 3.0, 13.7, 3.0)
    box(ax, 14.3, 3.0, 1.0, 1.0, "MLP\nHead", RED, 9)
    label(ax, 14.3, 2.2, "reads [CLS]\nonly", 7.5, PURPLE)
    label(ax, 14.3, 4.0, "Class\nprediction", 8, DARK)
    arrow(ax, 14.3, 3.5, 14.3, 3.8)

    ax.set_title("Vision Transformer (ViT) — Full Pipeline", fontsize=13,
                 fontweight="bold", color=DARK, pad=8)
    plt.tight_layout()
    fig.savefig(OUT / "vit_pipeline.png", dpi=150, bbox_inches="tight",
                facecolor=BG)
    plt.close()
    print("  vit_pipeline.png")


# ─────────────────────────────────────────────
# 2. Scaled Dot-Product Attention
# ─────────────────────────────────────────────
def draw_attention():
    fig, ax = plt.subplots(figsize=(5, 7))
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 8)
    ax.axis("off")
    fig.patch.set_facecolor(BG)

    # Q K V inputs
    for i, (x, name, color) in enumerate([(1, "Q\n(Query)", BLUE),
                                           (2.5, "K\n(Key)", GREEN),
                                           (4, "V\n(Value)", ORANGE)]):
        box(ax, x, 0.7, 0.9, 0.7, name, color, 10)

    # MatMul QK
    box(ax, 1.75, 2.1, 1.6, 0.55, "MatMul\n(Q × Kᵀ)", PURPLE, 9)
    arrow(ax, 1.0, 1.05, 1.55, 1.82)
    arrow(ax, 2.5, 1.05, 1.95, 1.82)

    # Scale
    box(ax, 1.75, 3.1, 1.6, 0.55, "Scale ÷ √dₖ", GRAY, 9, DARK)
    arrow(ax, 1.75, 2.38, 1.75, 2.82)

    # Softmax
    box(ax, 1.75, 4.1, 1.6, 0.55, "Softmax\n(attention weights)", RED, 9)
    arrow(ax, 1.75, 3.38, 1.75, 3.82)

    # MatMul with V
    box(ax, 1.75, 5.3, 1.6, 0.55, "MatMul\n(weights × V)", PURPLE, 9)
    arrow(ax, 1.75, 4.38, 1.75, 5.02)
    arrow(ax, 4.0, 1.05, 4.0, 5.3)
    ax.plot([4.0, 2.55], [5.3, 5.3], color=DARK, lw=1.5, zorder=2)

    # Output
    box(ax, 1.75, 6.4, 1.6, 0.45, "Output", BLUE, 10)
    arrow(ax, 1.75, 5.58, 1.75, 6.17)

    ax.set_title("Scaled Dot-Product Attention", fontsize=13,
                 fontweight="bold", color=DARK, pad=10)
    plt.tight_layout()
    fig.savefig(OUT / "attention_mechanism.png", dpi=150, bbox_inches="tight",
                facecolor=BG)
    plt.close()
    print("  attention_mechanism.png")


# ─────────────────────────────────────────────
# 3. CNN Architecture
# ─────────────────────────────────────────────
def draw_cnn():
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.set_xlim(0, 13)
    ax.set_ylim(-0.5, 4.5)
    ax.axis("off")
    fig.patch.set_facecolor(BG)

    layers = [
        (1.0, "Input\n[32×32×3]",     BLUE,   2.0, 3.0),
        (3.0, "Conv Layer\n16 filters\n[30×30×16]", ORANGE, 2.0, 3.2),
        (5.0, "Max Pool\n[15×15×16]",  GREEN,  1.6, 2.6),
        (7.0, "Conv Layer\n32 filters\n[13×13×32]", ORANGE, 1.6, 2.8),
        (9.0, "Max Pool\n[6×6×32]",    GREEN,  1.2, 2.2),
        (11.0,"FC + Softmax\n[num_classes]", RED, 1.0, 1.4),
    ]

    for i, (x, name, color, w, h) in enumerate(layers):
        box(ax, x, 2.0, w, h, name, color, 8.5)
        if i < len(layers) - 1:
            next_x = layers[i+1][0]
            arrow(ax, x + w/2, 2.0, next_x - layers[i+1][3]/2, 2.0)

    ax.set_title("CNN Architecture (Image Classification)", fontsize=13,
                 fontweight="bold", color=DARK, pad=8)
    plt.tight_layout()
    fig.savefig(OUT / "cnn_architecture.png", dpi=150, bbox_inches="tight",
                facecolor=BG)
    plt.close()
    print("  cnn_architecture.png")


# ─────────────────────────────────────────────
# 4. Conv Output Size Calculation
# ─────────────────────────────────────────────
def draw_conv_formula():
    fig, ax = plt.subplots(figsize=(8, 3))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4)
    ax.axis("off")
    fig.patch.set_facecolor(BG)

    box(ax, 2.0, 2.8, 3.5, 0.7, "Input: W × H × C_in", BLUE, 10)
    box(ax, 2.0, 1.5, 3.5, 0.7, "Filter: f × f × C_in\n(×N filters)", ORANGE, 9)
    box(ax, 7.5, 2.15, 3.5, 0.7, "Output: W' × H' × N", GREEN, 10)

    arrow(ax, 3.75, 2.15, 5.75, 2.15)

    label(ax, 5.0, 2.8,
          r"W' = $\lfloor$(W − f + 2p) / s$\rfloor$ + 1",
          9.5, DARK)
    label(ax, 5.0, 2.45,
          "Depth = N  (number of filters)",
          9, GRAY)

    ax.set_title("Conv Layer: Output Size Formula", fontsize=13,
                 fontweight="bold", color=DARK, pad=8)
    plt.tight_layout()
    fig.savefig(OUT / "conv_formula.png", dpi=150, bbox_inches="tight",
                facecolor=BG)
    plt.close()
    print("  conv_formula.png")


# ─────────────────────────────────────────────
# 5. RNN Unrolled
# ─────────────────────────────────────────────
def draw_rnn_unrolled():
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 5)
    ax.axis("off")
    fig.patch.set_facecolor(BG)

    steps = [("x₁", "h₁", 2), ("x₂", "h₂", 5), ("x₃", "h₃", 8)]

    for xt, ht, cx in steps:
        # Hidden state box
        box(ax, cx, 3.0, 1.4, 0.8, f"RNN Cell\n{ht}", ORANGE, 9.5)
        # Input
        box(ax, cx, 1.2, 1.0, 0.6, xt, BLUE, 11)
        arrow(ax, cx, 1.5, cx, 2.6)
        # Output
        box(ax, cx, 4.5, 1.0, 0.6, f"y_{xt[1]}", GREEN, 11)
        arrow(ax, cx, 3.4, cx, 4.2)

    # Horizontal hidden state arrows
    for i in range(len(steps) - 1):
        x1, x2 = steps[i][2], steps[i+1][2]
        arrow(ax, x1 + 0.7, 3.0, x2 - 0.7, 3.0, PURPLE, 2.0)
        label(ax, (x1+x2)/2, 3.3, "h", 9, PURPLE)

    # h0
    arrow(ax, 0.3, 3.0, 1.3, 3.0, GRAY)
    label(ax, 0.3, 3.4, "h₀", 9, GRAY)

    # Dots for continuation
    label(ax, 9.8, 3.0, "···", 16, GRAY)

    ax.set_title("RNN — Unrolled Through Time", fontsize=13,
                 fontweight="bold", color=DARK, pad=8)
    plt.tight_layout()
    fig.savefig(OUT / "rnn_unrolled.png", dpi=150, bbox_inches="tight",
                facecolor=BG)
    plt.close()
    print("  rnn_unrolled.png")


# ─────────────────────────────────────────────
# 6. LSTM Cell
# ─────────────────────────────────────────────
def draw_lstm():
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_xlim(0, 9)
    ax.set_ylim(0, 7)
    ax.axis("off")
    fig.patch.set_facecolor(BG)

    # Cell state line (top)
    ax.annotate("", xy=(8.5, 5.8), xytext=(0.5, 5.8),
                arrowprops=dict(arrowstyle="-|>", color=RED, lw=2.5,
                                mutation_scale=14))
    label(ax, 4.5, 6.2, "Cell State  Cₜ  (long-term memory)", 10, RED)

    # Gates
    gates = [
        (1.8, 3.5, "Forget Gate\nσ", RED,    "Discard from\ncell state"),
        (4.0, 3.5, "Input Gate\nσ  ×  tanh", GREEN,  "Write to\ncell state"),
        (6.5, 3.5, "Output Gate\nσ  ×  tanh(Cₜ)", BLUE, "Read from\ncell state"),
    ]

    for x, y, name, color, desc in gates:
        box(ax, x, y, 1.9, 1.1, name, color, 8.5)
        label(ax, x, y - 1.1, desc, 8, GRAY)
        # Arrow to cell state
        arrow(ax, x, y + 0.55, x, 5.5, color, 1.5)

    # Inputs
    arrow(ax, 0.5, 1.2, 1.8, 2.95)
    arrow(ax, 0.5, 1.2, 4.0, 2.95)
    arrow(ax, 0.5, 1.2, 6.5, 2.95)
    box(ax, 0.5, 1.2, 1.0, 0.6, "xₜ, hₜ₋₁", ORANGE, 9)

    # Output hₜ
    box(ax, 6.5, 1.5, 1.2, 0.5, "hₜ", BLUE, 10)
    arrow(ax, 6.5, 3.0, 6.5, 1.75)

    ax.set_title("LSTM Cell — Three Gates", fontsize=13,
                 fontweight="bold", color=DARK, pad=8)
    plt.tight_layout()
    fig.savefig(OUT / "lstm_cell.png", dpi=150, bbox_inches="tight",
                facecolor=BG)
    plt.close()
    print("  lstm_cell.png")


# ─────────────────────────────────────────────
# 7. MLP Architecture
# ─────────────────────────────────────────────
def draw_mlp():
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")
    fig.patch.set_facecolor(BG)

    layers = [
        (1.5,  [1, 2, 3, 4],    BLUE,   "Input\nLayer"),
        (4.0,  [1, 2, 3, 4, 5], ORANGE, "Hidden\nLayer 1"),
        (6.5,  [1, 2, 3, 4],    ORANGE, "Hidden\nLayer 2"),
        (9.0,  [2, 3, 4],       GREEN,  "Output\nLayer"),
    ]

    neuron_positions = []
    for lx, nodes, color, lname in layers:
        n = len(nodes)
        ys = np.linspace(1.0, 5.0, n)
        neuron_positions.append((lx, ys, color))
        for y in ys:
            circle = plt.Circle((lx, y), 0.25, color=color,
                                 ec=DARK, lw=1.2, zorder=3)
            ax.add_patch(circle)
        label(ax, lx, 0.4, lname, 9, DARK)

    # Connections
    for i in range(len(neuron_positions) - 1):
        x1, ys1, _ = neuron_positions[i]
        x2, ys2, _ = neuron_positions[i + 1]
        for y1 in ys1:
            for y2 in ys2:
                ax.plot([x1 + 0.25, x2 - 0.25], [y1, y2],
                        color=GRAY, lw=0.6, alpha=0.5, zorder=1)

    # Activation labels
    for x in [4.0, 6.5]:
        label(ax, x, 5.6, "ReLU", 8.5, RED)
    label(ax, 9.0, 5.6, "Softmax", 8.5, RED)

    ax.set_title("Multi-Layer Perceptron (MLP)", fontsize=13,
                 fontweight="bold", color=DARK, pad=8)
    plt.tight_layout()
    fig.savefig(OUT / "mlp_architecture.png", dpi=150, bbox_inches="tight",
                facecolor=BG)
    plt.close()
    print("  mlp_architecture.png")


# ─────────────────────────────────────────────
# 8a. Loss Curve Diagnosis (EXAM CORE)
# ─────────────────────────────────────────────
def draw_loss_diagnosis():
    """6-panel loss curve reference — covers every scenario tested in exams."""
    fig, axes = plt.subplots(2, 3, figsize=(14, 8))
    fig.patch.set_facecolor(BG)
    e = np.linspace(1, 60, 300)

    scenarios = [
        # Row 0
        dict(
            title="[GOOD]  Good Training",
            train=2.5 * np.exp(-e / 12) + 0.15,
            val=2.8 * np.exp(-e / 14) + 0.22,
            ylabel="Loss",
            diag="Both decrease and converge\n-> Model is learning well",
            fix="Keep training or add early stopping",
            color=GREEN,
        ),
        dict(
            title="[WARN]  Overfitting\n(High Variance)",
            train=2.5 * np.exp(-e / 10) + 0.10,
            val=2.2 * np.exp(-e / 18) + 0.35 + 0.012 * e,
            ylabel="Loss",
            diag="Train loss down, Val loss rises\n-> Large gap = Overfitting",
            fix="Dropout / L2 / more data / early stop",
            color=RED,
        ),
        dict(
            title="[WARN]  Underfitting\n(High Bias)",
            train=1.8 * np.exp(-e / 80) + 0.85,
            val=1.9 * np.exp(-e / 80) + 0.88,
            ylabel="Loss",
            diag="Both remain HIGH, small gap\n-> Model too simple",
            fix="Bigger model / more epochs / remove reg.",
            color=ORANGE,
        ),
        dict(
            title="[BAD]  LR Too High\n(Diverging / Oscillating)",
            train=np.clip(0.5 + 0.08 * e + 0.4 * np.sin(e / 2.5), 0.1, 8),
            val=np.clip(0.6 + 0.09 * e + 0.5 * np.sin(e / 2.5 + 1), 0.1, 8),
            ylabel="Loss",
            diag="Loss oscillates or explodes\n-> Learning rate too high",
            fix="Reduce LR by 10x  or  use LR scheduler",
            color=RED,
        ),
        dict(
            title="[SLOW]  LR Too Low\n(Barely Decreasing)",
            train=2.5 - 0.008 * e + 0.01 * np.sin(e),
            val=2.55 - 0.007 * e + 0.01 * np.sin(e + 0.5),
            ylabel="Loss",
            diag="Both decrease very slowly\n-> Learning rate too small",
            fix="Increase LR or use warm-up schedule",
            color=ORANGE,
        ),
        dict(
            title="[WARN]  Overfitting\n(Accuracy View)",
            train=0.55 + 0.40 * (1 - np.exp(-e / 8)),
            val=0.55 + 0.25 * (1 - np.exp(-e / 15)) - 0.003 * np.clip(e - 20, 0, None),
            ylabel="Accuracy",
            diag="Train Acc up,  Val Acc plateaus or drops\n-> Same diagnosis as loss-based overfitting",
            fix="Same fixes: dropout / L2 / more data",
            color=PURPLE,
        ),
    ]

    for ax, s in zip(axes.flat, scenarios):
        ax.set_facecolor(BG)
        tr = ax.plot(e, s["train"], color=BLUE, lw=2.2, label="Train")[0]
        vl = ax.plot(e, s["val"],   color=s["color"], lw=2.2,
                     linestyle="--", label="Validation")[0]

        ax.set_xlabel("Epochs", fontsize=8.5)
        ax.set_ylabel(s["ylabel"], fontsize=8.5)
        ax.set_title(s["title"], fontsize=10.5, fontweight="bold", color=DARK, pad=6)
        ax.legend(fontsize=8, loc="upper right")
        ax.tick_params(labelsize=7.5)

        # Diagnosis annotation box at bottom
        ax.text(0.5, -0.32, s["diag"],
                transform=ax.transAxes, ha="center", va="top",
                fontsize=8.5, color=s["color"], fontweight="bold",
                bbox=dict(boxstyle="round,pad=0.35", facecolor=WHITE,
                          edgecolor=s["color"], alpha=0.9))
        ax.text(0.5, -0.52, f"Fix: {s['fix']}",
                transform=ax.transAxes, ha="center", va="top",
                fontsize=7.5, color=GRAY,
                bbox=dict(boxstyle="round,pad=0.25", facecolor=WHITE,
                          edgecolor=GRAY, alpha=0.7))

        for sp in ax.spines.values():
            sp.set_color("#DEE2E6")

    fig.suptitle("Loss Curve Diagnosis — All Exam Scenarios",
                 fontsize=14, fontweight="bold", color=DARK, y=1.01)
    plt.tight_layout(rect=[0, 0.05, 1, 1])
    fig.savefig(OUT / "loss_diagnosis.png", dpi=150, bbox_inches="tight",
                facecolor=BG)
    plt.close()
    print("  loss_diagnosis.png")


# ─────────────────────────────────────────────
# 8b. Accuracy Training Curves (compact)
# ─────────────────────────────────────────────
def draw_training_curves():
    fig, axes = plt.subplots(1, 3, figsize=(13, 4))
    fig.patch.set_facecolor(BG)

    epochs = np.linspace(1, 50, 200)

    scenarios = [
        {
            "title": "Overfitting\n(High Variance)",
            "train": 0.95 - 0.03 * np.exp(-epochs / 10),
            "val":   0.70 - 0.10 * (1 - np.exp(-epochs / 30)) + 0.02 * np.sin(epochs / 5),
            "diag":  "Train ↑↑  Val ↓↓\nGap = Overfitting",
            "color": RED,
        },
        {
            "title": "Underfitting\n(High Bias)",
            "train": 0.60 + 0.05 * (1 - np.exp(-epochs / 20)),
            "val":   0.58 + 0.04 * (1 - np.exp(-epochs / 20)),
            "diag":  "Both low → Underfitting",
            "color": ORANGE,
        },
        {
            "title": "Good Fit",
            "train": 0.93 - 0.01 * np.exp(-epochs / 8),
            "val":   0.89 - 0.02 * np.exp(-epochs / 15) + 0.005 * np.sin(epochs / 4),
            "diag":  "Small gap → Good!",
            "color": GREEN,
        },
    ]

    for ax, s in zip(axes, scenarios):
        ax.set_facecolor(BG)
        ax.plot(epochs, s["train"], color=BLUE,  lw=2.0, label="Train")
        ax.plot(epochs, s["val"],   color=s["color"], lw=2.0,
                linestyle="--", label="Validation")
        ax.set_ylim(0.3, 1.05)
        ax.set_xlabel("Epochs", fontsize=9)
        ax.set_ylabel("Accuracy", fontsize=9)
        ax.set_title(s["title"], fontsize=11, fontweight="bold", color=DARK)
        ax.legend(fontsize=8)
        ax.tick_params(labelsize=8)
        ax.text(0.5, 0.12, s["diag"], transform=ax.transAxes,
                ha="center", va="bottom", fontsize=8.5,
                color=s["color"], fontweight="bold",
                bbox=dict(boxstyle="round,pad=0.3", facecolor=WHITE,
                          edgecolor=s["color"], alpha=0.8))
        for spine in ax.spines.values():
            spine.set_visible(True)
            spine.set_color("#DEE2E6")

    fig.suptitle("Training Curves — Diagnosing Model Behaviour",
                 fontsize=13, fontweight="bold", color=DARK, y=1.02)
    plt.tight_layout()
    fig.savefig(OUT / "training_curves.png", dpi=150, bbox_inches="tight",
                facecolor=BG)
    plt.close()
    print("  training_curves.png")


# ─────────────────────────────────────────────
# 9a. 4 LR Curves (exact 2025/2024 Q4 scenario)
# ─────────────────────────────────────────────
def draw_lr_curves():
    """Single-panel comparison of 4 LR curves — the exact exam question."""
    fig, ax = plt.subplots(figsize=(8, 5))
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    e = np.linspace(0, 60, 400)

    curves = [
        dict(lr="lr = 0.5  (too high — diverges)",
             y=np.clip(1.0 + 0.08 * e + 0.35 * np.abs(np.sin(e / 3)), 0, 9),
             color=RED, ls="-"),
        dict(lr="lr = 0.1  (slightly high — plateaus)",
             y=3.0 * np.exp(-e / 4) + 0.9 + 0.06 * np.sin(e / 2),
             color=ORANGE, ls="-"),
        dict(lr="lr = 0.01  (best — fast & low)",
             y=3.0 * np.exp(-e / 10) + 0.18,
             color=GREEN, ls="-"),
        dict(lr="lr = 0.001  (too low — very slow)",
             y=3.0 * np.exp(-e / 80) + 0.20,
             color=BLUE, ls="--"),
    ]

    for c in curves:
        ax.plot(e, c["y"], color=c["color"], lw=2.2,
                linestyle=c["ls"], label=c["lr"])

    # Annotation arrows
    ax.annotate("Diverging", xy=(55, curves[0]["y"][-1]),
                xytext=(42, 7.5), fontsize=8.5, color=RED, fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=RED, lw=1.2))
    ax.annotate("High plateau\n(overshooting)", xy=(55, curves[1]["y"][-1]),
                xytext=(38, 2.8), fontsize=8.5, color=ORANGE, fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=ORANGE, lw=1.2))
    ax.annotate("Best fit", xy=(30, curves[2]["y"][200]),
                xytext=(20, 1.2), fontsize=8.5, color=GREEN, fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=GREEN, lw=1.2))
    ax.annotate("Too slow\n(barely moving)", xy=(55, curves[3]["y"][-1]),
                xytext=(35, 1.9), fontsize=8.5, color=BLUE, fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=BLUE, lw=1.2))

    ax.set_ylim(-0.1, 9.5)
    ax.set_xlabel("Epochs", fontsize=10)
    ax.set_ylabel("Training Loss", fontsize=10)
    ax.set_title("4 Learning Rate Curves  (2025 Q4 / 2024 Q4 — exact exam scenario)",
                 fontsize=11, fontweight="bold", color=DARK, pad=8)
    ax.legend(fontsize=9, loc="upper right",
              framealpha=0.9, edgecolor="#DEE2E6")
    ax.tick_params(labelsize=9)
    for sp in ax.spines.values():
        sp.set_color("#DEE2E6")

    plt.tight_layout()
    fig.savefig(OUT / "lr_curves.png", dpi=150, bbox_inches="tight",
                facecolor=BG)
    plt.close()
    print("  lr_curves.png")


# ─────────────────────────────────────────────
# 9b. LR Schedule Shapes
# ─────────────────────────────────────────────
def draw_lr_schedules():
    fig, axes = plt.subplots(1, 4, figsize=(14, 3.8))
    fig.patch.set_facecolor(BG)
    e = np.linspace(0, 100, 500)

    schedules = [
        dict(title="Exponential Decay",
             y=0.1 * np.exp(-0.03 * e),
             note="lr × γᵗ\nSmooth, gradual",
             color=BLUE),
        dict(title="Step Decay",
             y=0.1 * np.array([0.5 ** int(x // 25) for x in e]),
             note="Halve every N epochs\nSimple, predictable",
             color=GREEN),
        dict(title="Cosine Annealing",
             y=0.005 + 0.5 * 0.095 * (1 + np.cos(np.pi * e / 100)),
             note="Smooth cosine curve\nWarm restarts possible",
             color=ORANGE),
        dict(title="Warm-up + Decay",
             y=np.where(e < 15,
                        0.1 * e / 15,
                        0.1 * np.exp(-0.025 * (e - 15))),
             note="Start small, grow,\nthen decay",
             color=PURPLE),
    ]

    for ax, s in zip(axes, schedules):
        ax.set_facecolor(BG)
        ax.plot(e, s["y"], color=s["color"], lw=2.2)
        ax.fill_between(e, s["y"], alpha=0.12, color=s["color"])
        ax.set_title(s["title"], fontsize=10, fontweight="bold",
                     color=DARK, pad=5)
        ax.set_xlabel("Epochs", fontsize=8.5)
        ax.set_ylabel("LR", fontsize=8.5)
        ax.tick_params(labelsize=7.5)
        ax.text(0.5, 0.72, s["note"], transform=ax.transAxes,
                ha="center", fontsize=8, color=s["color"], fontweight="bold",
                bbox=dict(boxstyle="round,pad=0.3", facecolor=WHITE,
                          edgecolor=s["color"], alpha=0.85))
        for sp in ax.spines.values():
            sp.set_color("#DEE2E6")

    fig.suptitle("Learning Rate Schedules — Why Not Keep LR Fixed?",
                 fontsize=12, fontweight="bold", color=DARK)
    plt.tight_layout()
    fig.savefig(OUT / "lr_schedules.png", dpi=150, bbox_inches="tight",
                facecolor=BG)
    plt.close()
    print("  lr_schedules.png")


# ─────────────────────────────────────────────
# 9c. Optimizer Comparison (SGD vs Momentum vs Adam)
# ─────────────────────────────────────────────
def draw_optimizer_comparison():
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))
    fig.patch.set_facecolor(BG)
    e = np.linspace(0, 80, 400)

    # Left: Loss curves
    ax = axes[0]
    ax.set_facecolor(BG)
    noise = np.random.default_rng(42).normal(0, 0.04, len(e))

    sgd   = 3.0 * np.exp(-e / 30) + 0.35 + np.abs(noise) * 0.8
    mom   = 3.0 * np.exp(-e / 18) + 0.22 + np.abs(noise) * 0.3
    adam  = 3.0 * np.exp(-e / 12) + 0.15 + np.abs(noise) * 0.15

    ax.plot(e, sgd,  color=RED,    lw=2.0, label="SGD (plain)",      alpha=0.85)
    ax.plot(e, mom,  color=ORANGE, lw=2.0, label="SGD + Momentum",   alpha=0.85)
    ax.plot(e, adam, color=GREEN,  lw=2.0, label="Adam",             alpha=0.85)

    ax.set_xlabel("Epochs", fontsize=9)
    ax.set_ylabel("Training Loss", fontsize=9)
    ax.set_title("Loss Convergence by Optimizer", fontsize=10,
                 fontweight="bold", color=DARK)
    ax.legend(fontsize=8.5)
    ax.tick_params(labelsize=8)
    for sp in ax.spines.values():
        sp.set_color("#DEE2E6")

    # Right: Summary table as visual
    ax2 = axes[1]
    ax2.axis("off")
    rows = [
        ["SGD",            "Current gradient only",   "Noisy, slow",    "Simple baselines"],
        ["SGD+Momentum",   "Avg of past gradients",   "Smoother, faster", "CV training"],
        ["RMSProp",        "Adaptive per-param LR",   "Good for RNNs",  "RNN/non-stationary"],
        ["Adam",           "Momentum + RMSProp",      "Fast, stable",   "Default choice"],
    ]
    col_labels = ["Optimizer", "Key Idea", "Behaviour", "When to Use"]
    colors_rows = [[BG]*4]*4
    table = ax2.table(
        cellText=rows,
        colLabels=col_labels,
        cellLoc="center",
        loc="center",
        cellColours=colors_rows,
    )
    table.auto_set_font_size(False)
    table.set_fontsize(9)
    table.scale(1, 2.0)
    for (r, c), cell in table.get_celld().items():
        cell.set_edgecolor("#DEE2E6")
        if r == 0:
            cell.set_facecolor(DARK)
            cell.set_text_props(color=WHITE, fontweight="bold")
        elif c == 0:
            cell.set_facecolor("#EBF5FB")
    ax2.set_title("Optimizer Quick Reference", fontsize=10,
                  fontweight="bold", color=DARK, pad=10)

    fig.suptitle("Optimizer Comparison", fontsize=12,
                 fontweight="bold", color=DARK)
    plt.tight_layout()
    fig.savefig(OUT / "optimizer_comparison.png", dpi=150, bbox_inches="tight",
                facecolor=BG)
    plt.close()
    print("  optimizer_comparison.png")


# ─────────────────────────────────────────────
# 9. Confusion Matrix
# ─────────────────────────────────────────────
def draw_confusion_matrix():
    fig, ax = plt.subplots(figsize=(6, 5))
    fig.patch.set_facecolor(BG)

    data = np.array([[45, 5], [10, 40]])
    colors = [[GREEN, RED], [ORANGE, BLUE]]
    labels = [["TP\n(True Positive)\n= 45", "FN\n(False Negative)\n= 5"],
              ["FP\n(False Positive)\n= 10", "TN\n(True Negative)\n= 40"]]

    for i in range(2):
        for j in range(2):
            rect = FancyBboxPatch((j * 2.5 + 0.5, (1 - i) * 2.0 + 0.5),
                                  2.2, 1.7,
                                  boxstyle="round,pad=0,rounding_size=0.08",
                                  facecolor=colors[i][j], edgecolor=WHITE,
                                  linewidth=2, zorder=2)
            ax.add_patch(rect)
            ax.text(j * 2.5 + 1.6, (1 - i) * 2.0 + 1.35,
                    labels[i][j], ha="center", va="center",
                    fontsize=10, color=WHITE, fontweight="bold", zorder=3)

    ax.set_xlim(0, 6.2)
    ax.set_ylim(0, 5.2)
    ax.axis("off")

    label(ax, 1.6, 4.7, "Predicted\nPositive", 10, DARK)
    label(ax, 4.1, 4.7, "Predicted\nNegative", 10, DARK)
    label(ax, 0.1, 3.35, "Actual\nPositive", 10, DARK, ha="left")
    label(ax, 0.1, 1.35, "Actual\nNegative", 10, DARK, ha="left")

    # Metric formulas
    formulas = [
        (3.1, 0.20, "Accuracy = (TP+TN) / Total"),
        (3.1, -0.10, "Precision = TP / (TP+FP)    Recall = TP / (TP+FN)"),
    ]
    for x, y, txt in formulas:
        ax.text(x, y, txt, ha="center", va="center", fontsize=8.5,
                color=DARK, style="italic")

    ax.set_title("Confusion Matrix", fontsize=13, fontweight="bold",
                 color=DARK, pad=8)
    plt.tight_layout()
    fig.savefig(OUT / "confusion_matrix.png", dpi=150, bbox_inches="tight",
                facecolor=BG)
    plt.close()
    print("  confusion_matrix.png")


# ─────────────────────────────────────────────
# V2: Knowledge Visualization Diagrams
# ─────────────────────────────────────────────

def draw_activation_functions():
    """4 activation functions + their gradients — B_mlp core concept."""
    fig, axes = plt.subplots(2, 4, figsize=(16, 7))
    fig.patch.set_facecolor(BG)
    x = np.linspace(-4, 4, 400)

    fns = [
        dict(name="ReLU",
             f=np.maximum(0, x),
             df=np.where(x > 0, 1.0, 0.0),
             color=GREEN,
             note="Dead zone: x<0\ngradient=0 always"),
        dict(name="LeakyReLU  (alpha=0.1)",
             f=np.where(x > 0, x, 0.1 * x),
             df=np.where(x > 0, 1.0, 0.1),
             color=BLUE,
             note="Small slope for x<0\nNo dead neurons"),
        dict(name="Sigmoid",
             f=1 / (1 + np.exp(-x)),
             df=(1 / (1 + np.exp(-x))) * (1 - 1 / (1 + np.exp(-x))),
             color=ORANGE,
             note="Output (0,1)\nGradient max=0.25\nVanishing gradient!"),
        dict(name="Tanh",
             f=np.tanh(x),
             df=1 - np.tanh(x) ** 2,
             color=PURPLE,
             note="Output (-1,1)\nZero-centered\nGradient max=1.0"),
    ]

    for col, fn in enumerate(fns):
        # Top row: function
        ax_f = axes[0][col]
        ax_f.set_facecolor(BG)
        ax_f.plot(x, fn["f"], color=fn["color"], lw=2.5)
        ax_f.axhline(0, color=GRAY, lw=0.8, linestyle="--")
        ax_f.axvline(0, color=GRAY, lw=0.8, linestyle="--")
        ax_f.set_title(fn["name"], fontsize=10, fontweight="bold", color=DARK)
        ax_f.set_ylabel("f(x)", fontsize=8.5)
        ax_f.set_ylim(-1.6, 1.6)
        ax_f.tick_params(labelsize=7.5)

        # Highlight dead zone for ReLU
        if col == 0:
            ax_f.axvspan(-4, 0, alpha=0.08, color=RED)
            ax_f.text(-2, 0.5, "dead zone\ngradient=0", ha="center",
                      fontsize=8, color=RED, fontweight="bold")

        # Bottom row: gradient
        ax_d = axes[1][col]
        ax_d.set_facecolor(BG)
        ax_d.plot(x, fn["df"], color=fn["color"], lw=2.5, linestyle="--")
        ax_d.axhline(0, color=GRAY, lw=0.8, linestyle="--")
        ax_d.set_ylabel("f'(x)  (gradient)", fontsize=8.5)
        ax_d.set_ylim(-0.1, 1.2)
        ax_d.tick_params(labelsize=7.5)
        ax_d.text(0.5, 0.88, fn["note"], transform=ax_d.transAxes,
                  ha="center", va="top", fontsize=7.5, color=fn["color"],
                  fontweight="bold",
                  bbox=dict(boxstyle="round,pad=0.25", facecolor=WHITE,
                            edgecolor=fn["color"], alpha=0.85))

        for ax in [ax_f, ax_d]:
            for sp in ax.spines.values():
                sp.set_color("#DEE2E6")

    fig.suptitle("Activation Functions — f(x) and Gradient f'(x)",
                 fontsize=13, fontweight="bold", color=DARK)
    plt.tight_layout()
    fig.savefig(OUT / "activation_functions.png", dpi=150,
                bbox_inches="tight", facecolor=BG)
    plt.close()
    print("  activation_functions.png")


def draw_sigmoid_vs_softmax():
    """Multi-label (sigmoid) vs Multi-class (softmax) output structure."""
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    fig.patch.set_facecolor(BG)

    for ax, title, outputs, note, color in [
        (axes[0],
         "Multi-Label Classification\n(use Sigmoid per output)",
         [("Cat?",    0.92, GREEN),
          ("Dog?",    0.08, GREEN),
          ("Hat?",    0.85, GREEN)],
         "Each output is INDEPENDENT\nSum can exceed 1\nExample: image may contain\nboth cat AND hat",
         GREEN),
        (axes[1],
         "Multi-Class Classification\n(use Softmax)",
         [("Cat",  0.75, BLUE),
          ("Dog",  0.20, BLUE),
          ("Bird", 0.05, BLUE)],
         "Outputs SUM to 1.0\nCompeting probabilities\nExample: image is EXACTLY\none of these classes",
         BLUE),
    ]:
        ax.set_facecolor(BG)
        ax.axis("off")
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 7)
        ax.set_title(title, fontsize=11, fontweight="bold",
                     color=DARK, pad=8)

        # Draw output nodes with probability bars
        for i, (label, prob, c) in enumerate(outputs):
            y = 5.5 - i * 1.6
            # Node
            circle = plt.Circle((1.5, y), 0.35, color=c,
                                 ec=DARK, lw=1.2, zorder=3)
            ax.add_patch(circle)
            ax.text(1.5, y, label, ha="center", va="center",
                    fontsize=8, color=WHITE, fontweight="bold", zorder=4)
            # Bar
            bar_w = prob * 5.0
            rect = FancyBboxPatch((2.5, y - 0.25), bar_w, 0.5,
                                  boxstyle="round,pad=0,rounding_size=0.05",
                                  facecolor=c, edgecolor="none",
                                  alpha=0.75, zorder=2)
            ax.add_patch(rect)
            ax.text(2.5 + bar_w + 0.1, y, f"{prob:.2f}",
                    va="center", fontsize=9, color=DARK, fontweight="bold")
            # Activation label
            act = "σ(z)" if color == GREEN else "e^z / Σe^z"
            ax.text(1.5, y - 0.55, act, ha="center",
                    fontsize=7, color=GRAY, style="italic")

        # Sum annotation
        total = sum(p for _, p, _ in outputs)
        sum_color = ORANGE if abs(total - 1.0) > 0.01 else GREEN
        ax.text(5, 0.5, f"Sum = {total:.2f}",
                ha="center", fontsize=10, fontweight="bold", color=sum_color,
                bbox=dict(boxstyle="round,pad=0.4", facecolor=WHITE,
                          edgecolor=sum_color, alpha=0.9))

        # Note box
        ax.text(5, 1.4, note, ha="center", va="center",
                fontsize=8.5, color=color,
                bbox=dict(boxstyle="round,pad=0.4", facecolor=WHITE,
                          edgecolor=color, alpha=0.85))

    fig.suptitle("Sigmoid vs Softmax — When to Use Which?",
                 fontsize=13, fontweight="bold", color=DARK)
    plt.tight_layout()
    fig.savefig(OUT / "sigmoid_vs_softmax.png", dpi=150,
                bbox_inches="tight", facecolor=BG)
    plt.close()
    print("  sigmoid_vs_softmax.png")


def draw_vanishing_gradient():
    """Vanishing gradient: grouped bar chart + annotation.

    Design rationale:
    - Exclude output layer (gradient = 1.0 trivially) — it pollutes the scale
    - Show layers 5→1 (backprop order, left→right)
    - Sigmoid and ReLU as grouped bars ON THE SAME Y-AXIS (0–1)
    - Sigmoid bars collapse to near-zero; ReLU bars stay tall
    - Direct visual contrast with no scale trick needed
    """
    fig, axes = plt.subplots(1, 2, figsize=(13, 6.5), gridspec_kw={"width_ratios": [2, 1]})
    fig.patch.set_facecolor(BG)

    # Layers in backprop order (output→input), excluding output layer itself
    layer_labels = ["Layer 5", "Layer 4", "Layer 3", "Layer 2", "Layer 1\n(input)"]
    n = len(layer_labels)

    # Gradient received at each layer (output layer = 1.0, not shown)
    # Sigmoid: each layer multiplies by max(σ') = 0.25  →  exponential collapse
    sigmoid_g = np.array([0.25 ** (i + 1) for i in range(n)])   # 0.25, 0.0625, 0.0156, ...
    # ReLU: σ'(x) = 1 for active neurons → signal passes through unchanged = 1.0
    relu_g = np.ones(n)   # exactly 1.0 at every layer — this is the ideal

    x = np.arange(n)
    w = 0.32

    # ── Left panel: grouped bar chart ──
    ax = axes[0]
    ax.set_facecolor(BG)

    bars_s = ax.bar(x - w/2, sigmoid_g, width=w, color=RED,   alpha=0.80,
                    edgecolor=DARK, lw=0.8, label="Sigmoid (vanishing)")
    bars_r = ax.bar(x + w/2, relu_g,    width=w, color=GREEN, alpha=0.80,
                    edgecolor=DARK, lw=0.8, label="ReLU (preserved)")

    # Value labels
    for bar, val in zip(bars_s, sigmoid_g):
        ax.text(bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 0.015,
                f"{val:.3f}", ha="center", fontsize=7.5,
                color=RED, fontweight="bold")
    for bar, val in zip(bars_r, relu_g):
        ax.text(bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 0.015,
                f"{val:.1f}", ha="center", fontsize=7.5,
                color=GREEN, fontweight="bold")

    ax.set_xticks(x)
    ax.set_xticklabels(layer_labels, fontsize=9)
    ax.set_ylabel("Activation derivative σ'(x)\n= how much error signal passes through", fontsize=9)
    ax.set_ylim(0, 1.45)
    ax.set_title("Gradient Received at Each Layer",
                 fontsize=11, fontweight="bold", color=DARK, pad=8)
    ax.legend(fontsize=9, loc="upper right")
    ax.tick_params(labelsize=8.5)

    # Backprop direction label below x-axis ticks
    ax.annotate("Backprop direction  (output → input)",
                xy=(0.85, -0.20), xytext=(0.05, -0.20),
                xycoords="axes fraction", textcoords="axes fraction",
                fontsize=9, color=DARK, fontweight="bold",
                arrowprops=dict(arrowstyle="-|>", color=DARK, lw=1.5,
                                mutation_scale=13))

    for sp in ax.spines.values():
        sp.set_color("#DEE2E6")

    # ── Right panel: summary key ──
    ax2 = axes[1]
    ax2.set_facecolor(BG)
    ax2.axis("off")
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 12)

    box(ax2, 5, 11.2, 9, 0.9,  "Backprop chain rule per layer:",                   DARK,  10, WHITE)
    box(ax2, 5,  9.5, 9, 1.3,  "dL/dw  =  error_signal  x  sigma'(x)  x  input",  DARK,   8, WHITE)
    box(ax2, 5,  7.7, 9, 1.4,  "sigmoid'(x) max = 0.25\n0.25^5 = 0.001 after 5 layers", RED,  9, WHITE)
    box(ax2, 5,  5.8, 9, 1.4,  "=> error_signal ~ 0\n=> dL/dw ~ 0  =>  no update",RED,    9, WHITE)
    box(ax2, 5,  3.8, 9, 1.4,  "ReLU'(x) = 1  (x > 0)\n1^5 = 1.0  at every layer",GREEN,  9, WHITE)
    box(ax2, 5,  1.8, 9, 1.4,  "=> signal preserved\n=> all layers learn",         GREEN,  9, WHITE)

    plt.tight_layout(rect=[0, 0.08, 1, 1])
    fig.suptitle("Vanishing Gradient — Why ReLU Replaced Sigmoid in Hidden Layers",
                 fontsize=12, fontweight="bold", color=DARK)
    fig.savefig(OUT / "vanishing_gradient.png", dpi=150,
                bbox_inches="tight", facecolor=BG)
    plt.close()
    print("  vanishing_gradient.png")


def draw_l1_vs_l2():
    """L1 vs L2: geometric constraint + weight sparsity side by side."""
    fig, axes = plt.subplots(1, 3, figsize=(14, 5))
    fig.patch.set_facecolor(BG)

    # ── Left: Geometric constraint view ──
    ax = axes[0]
    ax.set_facecolor(BG)
    ax.set_aspect("equal")
    ax.set_xlim(-2.2, 2.2)
    ax.set_ylim(-2.2, 2.2)

    # Loss contours (ellipse)
    theta = np.linspace(0, 2 * np.pi, 300)
    for r, a in [(0.5, 0.12), (1.0, 0.1), (1.5, 0.08), (2.0, 0.06)]:
        ax.plot(1.2 + r * 1.3 * np.cos(theta), 1.0 + r * np.sin(theta),
                color=GRAY, alpha=a * 5, lw=0.8)
    ax.text(1.2, 1.0, "Loss\nminimum", ha="center", fontsize=7.5,
            color=GRAY, style="italic")

    # L2 constraint (circle)
    circle = plt.Circle((0, 0), 1.2, fill=False, color=BLUE,
                         lw=2.0, linestyle="-", zorder=3)
    ax.add_patch(circle)
    ax.text(0.85, 0.85, "L2\n(circle)", ha="center", color=BLUE,
            fontsize=9, fontweight="bold")

    # L1 constraint (diamond)
    diamond_x = [1.2, 0, -1.2, 0, 1.2]
    diamond_y = [0,  1.2, 0, -1.2, 0]
    ax.plot(diamond_x, diamond_y, color=RED, lw=2.0, zorder=3)
    ax.text(-0.5, 0.9, "L1\n(diamond)", ha="center", color=RED,
            fontsize=9, fontweight="bold")

    # Intersection points
    ax.plot(0, 1.2, "o", color=RED, ms=9, zorder=5)
    ax.annotate("L1 hits corner\n→ w1=0 (sparse!)",
                xy=(0, 1.2), xytext=(-1.5, 1.7), fontsize=8, color=RED,
                fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=RED, lw=1.2))
    ax.plot(0.6, 1.04, "o", color=BLUE, ms=9, zorder=5)
    ax.annotate("L2 hits curve\nboth w1,w2 small",
                xy=(0.6, 1.04), xytext=(0.8, -0.8), fontsize=8, color=BLUE,
                fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=BLUE, lw=1.2))

    ax.axhline(0, color=GRAY, lw=0.5)
    ax.axvline(0, color=GRAY, lw=0.5)
    ax.set_xlabel("w1", fontsize=9)
    ax.set_ylabel("w2", fontsize=9)
    ax.set_title("Geometric Constraint\n(why L1 = sparse)", fontsize=10,
                 fontweight="bold", color=DARK)
    for sp in ax.spines.values():
        sp.set_color("#DEE2E6")

    # ── Middle: weight histogram after L2 ──
    rng = np.random.default_rng(0)
    ax2 = axes[1]
    ax2.set_facecolor(BG)
    w_l2 = rng.normal(0, 0.3, 500)
    ax2.hist(w_l2, bins=40, color=BLUE, alpha=0.75, edgecolor=WHITE, lw=0.4)
    ax2.axvline(0, color=DARK, lw=1.5, linestyle="--")
    ax2.set_title("L2 Weights Distribution\n(all small, few zeros)", fontsize=10,
                  fontweight="bold", color=DARK)
    ax2.set_xlabel("Weight value", fontsize=9)
    ax2.set_ylabel("Count", fontsize=9)
    ax2.text(0.5, 0.88, "Dense: many small\nnon-zero weights",
             transform=ax2.transAxes, ha="center", va="top",
             fontsize=9, color=BLUE, fontweight="bold",
             bbox=dict(boxstyle="round,pad=0.3", facecolor=WHITE,
                       edgecolor=BLUE, alpha=0.85))
    for sp in ax2.spines.values():
        sp.set_color("#DEE2E6")

    # ── Right: weight histogram after L1 ──
    ax3 = axes[2]
    ax3.set_facecolor(BG)
    w_l1_raw = rng.laplace(0, 0.2, 500)
    w_l1 = np.where(np.abs(w_l1_raw) < 0.08, 0, w_l1_raw)  # soft threshold
    ax3.hist(w_l1, bins=40, color=RED, alpha=0.75, edgecolor=WHITE, lw=0.4)
    ax3.axvline(0, color=DARK, lw=1.5, linestyle="--")
    n_zeros = np.sum(w_l1 == 0)
    ax3.set_title("L1 Weights Distribution\n(many exact zeros = sparse)", fontsize=10,
                  fontweight="bold", color=DARK)
    ax3.set_xlabel("Weight value", fontsize=9)
    ax3.set_ylabel("Count", fontsize=9)
    ax3.text(0.5, 0.88,
             f"~{n_zeros} weights = 0\nSparse: irrelevant\nfeatures removed",
             transform=ax3.transAxes, ha="center", va="top",
             fontsize=9, color=RED, fontweight="bold",
             bbox=dict(boxstyle="round,pad=0.3", facecolor=WHITE,
                       edgecolor=RED, alpha=0.85))
    for sp in ax3.spines.values():
        sp.set_color("#DEE2E6")

    fig.suptitle("L1 vs L2 Regularisation — Geometric Intuition & Weight Sparsity",
                 fontsize=12, fontweight="bold", color=DARK)
    plt.tight_layout()
    fig.savefig(OUT / "l1_vs_l2.png", dpi=150, bbox_inches="tight",
                facecolor=BG)
    plt.close()
    print("  l1_vs_l2.png")


def draw_dropout():
    """Dropout: training (neurons off) vs inference (all on, scaled)."""
    fig, axes = plt.subplots(1, 2, figsize=(12, 5.5))
    fig.patch.set_facecolor(BG)

    layer_sizes = [4, 5, 4, 3]
    layer_xs = [1.5, 3.5, 5.5, 7.5]

    # Which neurons are dropped in training (middle two layers)
    dropped = {1: [1, 3], 2: [0, 2]}  # layer index: list of dropped neuron indices

    for ax_idx, (ax, mode) in enumerate(zip(axes, ["Training", "Inference"])):
        ax.set_facecolor(BG)
        ax.set_xlim(0, 9)
        ax.set_ylim(-0.5, 7)
        ax.axis("off")
        ax.set_title(f"{mode}\n{'(p=0.5 neurons randomly dropped)' if mode=='Training' else '(all neurons active, outputs × 0.5)'}",
                     fontsize=10.5, fontweight="bold", color=DARK, pad=6)

        positions = []
        for li, (lx, ln) in enumerate(zip(layer_xs, layer_sizes)):
            ys = np.linspace(1, 5.5, ln)
            layer_pos = []
            for ni, y in enumerate(ys):
                is_dropped = (mode == "Training" and
                              li in dropped and ni in dropped[li])
                color = "#DEE2E6" if is_dropped else (
                    BLUE if li == 0 else
                    GREEN if li == len(layer_sizes) - 1 else ORANGE)
                ec = RED if is_dropped else DARK
                lw = 2.0 if is_dropped else 1.2
                ls = "--" if is_dropped else "-"
                circle = plt.Circle((lx, y), 0.3,
                                     color=color, ec=ec, lw=lw,
                                     linestyle=ls, zorder=3)
                ax.add_patch(circle)
                if is_dropped:
                    ax.text(lx, y, "X", ha="center", va="center",
                            fontsize=12, color=RED, fontweight="bold", zorder=4)
                layer_pos.append((lx, y, is_dropped))
            positions.append(layer_pos)

        # Connections
        for li in range(len(positions) - 1):
            for (x1, y1, d1) in positions[li]:
                for (x2, y2, d2) in positions[li + 1]:
                    if d1 or d2:
                        continue  # skip dropped neurons
                    ax.plot([x1 + 0.3, x2 - 0.3], [y1, y2],
                            color=GRAY, lw=0.6, alpha=0.4, zorder=1)

        # Inference scaling note
        if mode == "Inference":
            ax.text(4.5, 0.1, "All neurons active — each output scaled by (1-p) to compensate",
                    ha="center", fontsize=8.5, color=DARK, style="italic",
                    bbox=dict(boxstyle="round,pad=0.3", facecolor=WHITE,
                              edgecolor=BLUE, alpha=0.85))
        else:
            ax.text(4.5, 0.1, "Dropped neurons (X) produce zero output — forces network to not rely on any single neuron",
                    ha="center", fontsize=8.5, color=RED, fontweight="bold",
                    bbox=dict(boxstyle="round,pad=0.3", facecolor=WHITE,
                              edgecolor=RED, alpha=0.85))

        # Layer labels
        for lx, lname in zip(layer_xs, ["Input", "Hidden 1", "Hidden 2", "Output"]):
            ax.text(lx, 6.5, lname, ha="center", fontsize=9, color=DARK,
                    fontweight="bold")

    fig.suptitle("Dropout — Training vs Inference",
                 fontsize=13, fontweight="bold", color=DARK)
    plt.tight_layout()
    fig.savefig(OUT / "dropout.png", dpi=150, bbox_inches="tight",
                facecolor=BG)
    plt.close()
    print("  dropout.png")


def draw_batchnorm():
    """Batch normalization: activation distribution before and after."""
    fig, axes = plt.subplots(1, 3, figsize=(13, 4.5))
    fig.patch.set_facecolor(BG)
    rng = np.random.default_rng(7)

    # Before: skewed distribution (bad activations)
    raw = rng.exponential(2, 1000) + rng.normal(3, 1, 1000)
    # After BN: zero mean, unit variance
    bn  = (raw - raw.mean()) / raw.std()
    # After BN + gamma/beta (learnable): scaled and shifted back to useful range
    final = bn * 1.5 + 0.5

    panels = [
        (axes[0], raw,   "Before Batch Norm\n(raw activations)", RED,
         f"mean={raw.mean():.1f}\nstd={raw.std():.1f}\nSkewed, large values\n→ unstable training"),
        (axes[1], bn,    "After Normalise\n(subtract mean, div by std)", ORANGE,
         f"mean={bn.mean():.2f}\nstd={bn.std():.2f}\nZero-mean, unit variance\n→ stable gradients"),
        (axes[2], final, "After Scale+Shift\n(learnable gamma, beta)", GREEN,
         f"mean={final.mean():.2f}\nstd={final.std():.2f}\nNetwork can undo norm\nif needed (flexible)"),
    ]

    for ax, data, title, color, note in panels:
        ax.set_facecolor(BG)
        ax.hist(data, bins=50, color=color, alpha=0.75,
                edgecolor=WHITE, lw=0.3, density=True)
        ax.axvline(data.mean(), color=DARK, lw=1.8, linestyle="--",
                   label=f"mean={data.mean():.2f}")
        ax.set_title(title, fontsize=10, fontweight="bold", color=DARK, pad=5)
        ax.set_xlabel("Activation value", fontsize=8.5)
        ax.set_ylabel("Density", fontsize=8.5)
        ax.tick_params(labelsize=8)
        ax.text(0.97, 0.95, note, transform=ax.transAxes,
                ha="right", va="top", fontsize=8, color=color, fontweight="bold",
                bbox=dict(boxstyle="round,pad=0.3", facecolor=WHITE,
                          edgecolor=color, alpha=0.85))
        for sp in ax.spines.values():
            sp.set_color("#DEE2E6")

    fig.suptitle("Batch Normalisation — What Happens to Activation Distributions",
                 fontsize=12, fontweight="bold", color=DARK)
    plt.tight_layout()
    fig.savefig(OUT / "batchnorm.png", dpi=150, bbox_inches="tight",
                facecolor=BG)
    plt.close()
    print("  batchnorm.png")


def draw_mean_vs_median():
    """Mean vs Median imputation: why median is robust to outliers."""
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))
    fig.patch.set_facecolor(BG)
    rng = np.random.default_rng(3)

    normal_vals = rng.normal(500, 80, 200)
    outliers    = rng.uniform(4000, 5000, 6)
    all_vals    = np.concatenate([normal_vals, outliers])

    mean_v   = all_vals.mean()
    median_v = np.median(all_vals)

    # Left: distribution with outlier markers
    ax = axes[0]
    ax.set_facecolor(BG)
    ax.hist(normal_vals, bins=30, color=BLUE, alpha=0.7,
            edgecolor=WHITE, lw=0.4, label="Normal values", density=True)
    for ov in outliers:
        ax.axvline(ov, color=RED, lw=1.5, alpha=0.6)
    ax.scatter(outliers, [0.0015] * len(outliers), color=RED,
               s=60, zorder=5, label="Outliers")

    ax.axvline(mean_v, color=ORANGE, lw=2.5, linestyle="-",
               label=f"Mean = {mean_v:.0f}")
    ax.axvline(median_v, color=GREEN, lw=2.5, linestyle="--",
               label=f"Median = {median_v:.0f}")

    ax.annotate(f"Mean pulled\nto {mean_v:.0f}!",
                xy=(mean_v, 0.001), xytext=(mean_v + 300, 0.002),
                fontsize=8.5, color=ORANGE, fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=ORANGE, lw=1.2))
    ax.annotate(f"Median stays\nnear {median_v:.0f}",
                xy=(median_v, 0.003), xytext=(median_v - 350, 0.004),
                fontsize=8.5, color=GREEN, fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=GREEN, lw=1.2))

    ax.set_title("Distribution with Outliers\n(only 6 out of 206 values)",
                 fontsize=10, fontweight="bold", color=DARK)
    ax.set_xlabel("Value", fontsize=9)
    ax.legend(fontsize=8.5)
    ax.tick_params(labelsize=8)
    for sp in ax.spines.values():
        sp.set_color("#DEE2E6")

    # Right: imputed value comparison
    ax2 = axes[1]
    ax2.set_facecolor(BG)
    ax2.axis("off")
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 7)

    entries = [
        (2.5, 5.5, "Missing value\n(NaN)", GRAY, WHITE),
        (2.5, 3.8, f"Mean imputation\n→ {mean_v:.0f}", ORANGE, WHITE),
        (7.5, 3.8, f"Median imputation\n→ {median_v:.0f}", GREEN, WHITE),
        (2.5, 2.0, "Biased by outliers\nActual centre ~500", RED, WHITE),
        (7.5, 2.0, "Robust to outliers\nReflects true centre", GREEN, WHITE),
    ]
    for x, y, txt, fc, tc in entries:
        box(ax2, x, y, 3.8, 0.9, txt, fc, 9, tc)

    arrow(ax2, 2.5, 5.1, 2.5, 4.25, ORANGE)
    arrow(ax2, 2.5, 5.1, 7.5, 4.25, GREEN)
    arrow(ax2, 2.5, 3.35, 2.5, 2.5, RED)
    arrow(ax2, 7.5, 3.35, 7.5, 2.5, GREEN)

    ax2.set_title("Why Median > Mean\nwhen outliers exist",
                  fontsize=10, fontweight="bold", color=DARK, pad=8)

    fig.suptitle("Mean vs Median Imputation — Why Median is Preferred with Outliers",
                 fontsize=12, fontweight="bold", color=DARK)
    plt.tight_layout()
    fig.savefig(OUT / "mean_vs_median.png", dpi=150, bbox_inches="tight",
                facecolor=BG)
    plt.close()
    print("  mean_vs_median.png")


def draw_conv_sliding():
    """Convolution sliding window — step-by-step operation visual."""
    fig, axes = plt.subplots(1, 3, figsize=(14, 5))
    fig.patch.set_facecolor(BG)

    # Input 5×5
    inp = np.array([
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1],
    ], dtype=float)

    # Filter 3×3
    filt = np.array([
        [1, 0, 1],
        [0, 1, 0],
        [1, 0, 1],
    ], dtype=float)

    # Output 3×3
    out = np.zeros((3, 3))
    for i in range(3):
        for j in range(3):
            out[i, j] = np.sum(inp[i:i+3, j:j+3] * filt)

    def draw_grid(ax, data, title, highlight=None, hl_color=ORANGE):
        n = data.shape[0]
        ax.set_facecolor(BG)
        ax.set_xlim(-0.5, n - 0.5)
        ax.set_ylim(-0.5, n - 0.5)
        ax.set_aspect("equal")
        ax.set_title(title, fontsize=10, fontweight="bold", color=DARK, pad=8)
        ax.axis("off")
        for i in range(n):
            for j in range(n):
                is_hl = (highlight is not None and
                         highlight[0] <= i < highlight[0] + highlight[2] and
                         highlight[1] <= j < highlight[1] + highlight[2])
                fc = hl_color if is_hl else WHITE
                rect = FancyBboxPatch((j - 0.48, (n-1-i) - 0.48), 0.96, 0.96,
                                      boxstyle="round,pad=0,rounding_size=0.04",
                                      facecolor=fc, edgecolor=DARK,
                                      linewidth=1.0, zorder=2)
                ax.add_patch(rect)
                val = int(data[i, j]) if data[i, j] == int(data[i, j]) else f"{data[i,j]:.0f}"
                ax.text(j, (n-1-i), str(val), ha="center", va="center",
                        fontsize=11, color=DARK, fontweight="bold", zorder=3)

    # Panel 1: Input with highlight at position (0,0)
    draw_grid(axes[0], inp, "Input  [5×5×1]", highlight=(0, 0, 3))
    axes[0].text(2, -1.0, "Highlighted 3×3 patch\n= first position of filter",
                 ha="center", fontsize=8.5, color=ORANGE, fontweight="bold")

    # Panel 2: Filter
    draw_grid(axes[1], filt, "Filter  [3×3×1]\n(learned weights)", hl_color=BLUE)
    # Calculation annotation
    calc_str = ("Position (0,0):\n"
                "1×1 + 0×0 + 1×1\n"
                "+ 0×0 + 1×1 + 0×0\n"
                "+ 1×1 + 0×0 + 1×1\n"
                "= 5")
    axes[1].text(1, -1.2, calc_str, ha="center", fontsize=8.5,
                 color=BLUE, fontweight="bold",
                 bbox=dict(boxstyle="round,pad=0.3", facecolor=WHITE,
                           edgecolor=BLUE, alpha=0.9))

    # Panel 3: Output with first cell highlighted
    draw_grid(axes[2], out, "Output  [3×3×1]\n(one filter = one channel)", highlight=(0, 0, 1), hl_color=GREEN)
    axes[2].text(1, -1.0, "Output size: (5-3)/1+1 = 3\nEach cell = dot product\nof filter with patch",
                 ha="center", fontsize=8.5, color=GREEN, fontweight="bold")

    fig.suptitle("Convolution Sliding Window — How One Filter Produces One Output Channel",
                 fontsize=12, fontweight="bold", color=DARK)
    plt.tight_layout()
    fig.savefig(OUT / "conv_sliding.png", dpi=150, bbox_inches="tight",
                facecolor=BG)
    plt.close()
    print("  conv_sliding.png")


# ─────────────────────────────────────────────
# Run all
# ─────────────────────────────────────────────
if __name__ == "__main__":
    print(f"Generating diagrams → {OUT}")
    draw_transformer_encoder()
    draw_vit_pipeline()
    draw_attention()
    draw_cnn()
    draw_conv_formula()
    draw_rnn_unrolled()
    draw_lstm()
    draw_mlp()
    draw_loss_diagnosis()      # main exam focus
    draw_training_curves()
    draw_lr_curves()           # A_optimization
    draw_lr_schedules()        # A_optimization
    draw_optimizer_comparison() # A_optimization
    draw_confusion_matrix()
    # V2 knowledge visualizations
    draw_activation_functions()  # B_mlp
    draw_sigmoid_vs_softmax()    # B_mlp
    draw_vanishing_gradient()    # B_mlp
    draw_l1_vs_l2()              # A_regularization
    draw_dropout()               # A_regularization
    draw_batchnorm()             # A_regularization
    draw_mean_vs_median()        # A_overview
    draw_conv_sliding()          # B_cnn
    print("Done.")
