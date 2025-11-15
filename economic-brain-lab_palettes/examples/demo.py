"""Generate demo figures for Economic Brain Lab palettes and styles.
Run:
    python examples/demo.py
"""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from cycler import cycler

# Palettes
EBL_PALETTE = [
    "#B4417E", "#E774B1", "#810D4B",
    "#F3A45E", "#FFD791", "#C0712B",
    "#4BA6A6", "#7ED9D9", "#187373",
    "#6A2E4F", "#9D6182", "#37001C",
]

EBL_SAFE_PALETTE = [
    "#B63E6A", "#E982B0", "#800629",
    "#F7956A", "#FEC891", "#C34E22",
    "#4880A8", "#83BDDA", "#124271",
    "#6D2D43", "#9D6179", "#350009",
]

seq_mint = ListedColormap(["#E7F7F7", "#BDEAEA", "#7ED9D9", "#4BA6A6", "#2D6F6F"])  # light->dark mint
seq_apricot = ListedColormap(["#FFF2E2", "#FFE2C3", "#FFD091", "#F3A45E", "#C0712B"])  # light->dark apricot
div_cran_mint = LinearSegmentedColormap.from_list(
    "div_cran_mint", ["#810D4B", "#B4417E", "#FFF8E6", "#4BA6A6", "#187373"], N=256
)


def plot_all(style_path: str, suffix: str, dark: bool = False):
    plt.style.use(style_path)

    labels = [f"G{i+1}" for i in range(12)]
    vals = np.array([12, 7, 9, 14, 6, 10, 11, 8, 13, 5, 15, 9])
    x = np.linspace(0, 2*np.pi, 200)
    rng = np.random.default_rng(42)

    # 1) Categorical bars — Brand vs Safe
    fig, axes = plt.subplots(2, 1, figsize=(10, 6), constrained_layout=True)
    axes[0].bar(labels, vals, color=EBL_PALETTE,
                edgecolor=('#FFF8E6' if dark else '#2B2B2B'), linewidth=0.6)
    axes[0].set_title(f"Categorical Bar — EBL Brand Palette (12) [{suffix}]")

    axes[1].bar(labels, vals, color=EBL_SAFE_PALETTE,
                edgecolor=('#FFF8E6' if dark else '#2B2B2B'), linewidth=0.6)
    axes[1].set_title(f"Categorical Bar — EBL Colorblind-Safe Palette (12) [{suffix}]")
    fig.savefig(f"figures/demo_categorical_bars_{suffix}.png", dpi=150)

    # 2) Line plot — Brand palette
    fig2, ax2 = plt.subplots(figsize=(10, 4))
    for i, c in enumerate(EBL_PALETTE):
        ax2.plot(x, np.sin(x + i*0.3) + 0.1*i, color=c, label=f"S{i+1}")
    ax2.set_title(f"Line Plot — 12 Series (Brand) [{suffix}]")
    ax2.set_xlabel("Angle (rad)")
    ax2.set_ylabel("Amplitude")
    ax2.legend(ncol=6, fontsize=8, frameon=False)
    fig2.tight_layout()
    fig2.savefig(f"figures/demo_lines_brand_{suffix}.png", dpi=150)

    # 3) Scatter — Colorblind-safe palette + marker redundancy
    X = rng.normal(0, 1, size=(12, 40))
    Y = rng.normal(0, 1, size=(12, 40))
    markers = ['o','s','^','v','D','P','X','*','<','>','h','+']
    fig3, ax3 = plt.subplots(figsize=(8, 6))
    for i, (c, m) in enumerate(zip(EBL_SAFE_PALETTE, markers)):
        ec = '#FFF8E6' if dark else '#2B2B2B'
        ax3.scatter(X[i], Y[i] + i*0.2, c=c, s=40, marker=m, edgecolors=ec, linewidths=0.6, label=f"C{i+1}")
    ax3.set_title(f"Scatter — Colorblind-Safe Palette [{suffix}]")
    ax3.set_xlabel("X")
    ax3.set_ylabel("Y")
    ax3.legend(ncol=3, fontsize=8, frameon=False)
    fig3.tight_layout()
    fig3.savefig(f"figures/demo_scatter_safe_{suffix}.png", dpi=150)

    # 4) Heatmaps — Sequential + Diverging
    mat_seq = rng.normal(0.5, 0.15, size=(10, 20))
    mat_seq = np.clip(mat_seq, 0, 1)
    mat_div = rng.normal(0, 1, size=(15, 30))

    fig4, axes4 = plt.subplots(1, 3, figsize=(12, 3), constrained_layout=True)
    im0 = axes4[0].imshow(mat_seq, cmap=seq_mint, aspect='auto')
    axes4[0].set_title(f"Sequential — Mint [{suffix}]")
    fig4.colorbar(im0, ax=axes4[0], fraction=0.046, pad=0.04)

    im1 = axes4[1].imshow(mat_seq, cmap=seq_apricot, aspect='auto')
    axes4[1].set_title(f"Sequential — Apricot [{suffix}]")
    fig4.colorbar(im1, ax=axes4[1], fraction=0.046, pad=0.04)

    im2 = axes4[2].imshow(mat_div, cmap=div_cran_mint, aspect='auto', vmin=-3, vmax=3)
    axes4[2].set_title(f"Diverging — Cranberry↔Mint [{suffix}]")
    fig4.colorbar(im2, ax=axes4[2], fraction=0.046, pad=0.04)

    fig4.savefig(f"figures/demo_heatmaps_{suffix}.png", dpi=150)

    # 5) Swatch sheets — Brand vs Safe
    fig5, ax5 = plt.subplots(2, 1, figsize=(10, 2.8), constrained_layout=True)
    ax5[0].axis('off'); ax5[1].axis('off')
    for i, color in enumerate(EBL_PALETTE):
        ax5[0].add_patch(plt.Rectangle((i, 0), 1, 1, color=color))
        ax5[0].text(i+0.5, -0.1, color, ha='center', va='top', fontsize=8)
    ax5[0].set_xlim(0, 12); ax5[0].set_ylim(0, 1); ax5[0].set_title(f'EBL Brand — Categorical (12) [{suffix}]')

    for i, color in enumerate(EBL_SAFE_PALETTE):
        ax5[1].add_patch(plt.Rectangle((i, 0), 1, 1, color=color))
        ax5[1].text(i+0.5, -0.1, color, ha='center', va='top', fontsize=8)
    ax5[1].set_xlim(0, 12); ax5[1].set_ylim(0, 1); ax5[1].set_title(f'EBL Colorblind-Safe — Categorical (12) [{suffix}]')

    fig5.savefig(f"figures/demo_swatches_{suffix}.png", dpi=150)

if __name__ == '__main__':
    plot_all('styles/ebl.mplstyle', 'bright', dark=False)
    plot_all('styles/ebl_dark.mplstyle', 'dark', dark=True)
    print('Created demo figures in ./figures')
