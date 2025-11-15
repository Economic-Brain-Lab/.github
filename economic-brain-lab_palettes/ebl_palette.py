
"""
EBL Palette Module
==================
Economic Brain Lab categorical palettes and helpers for matplotlib/seaborn.

Contents:
- EBL_PALETTE: 12-color brand-aligned categorical palette (hex)
- EBL_SAFE_PALETTE: 12-color colorblind-safe variant (hex)
- get_ebl_cmap(name='ebl12'): return ListedColormap for EBL_PALETTE
- get_ebl_safe_cmap(name='ebl12_safe'): return ListedColormap for EBL_SAFE_PALETTE
- register_colormaps(): register both cmaps with matplotlib
- use_ebl_palette(safe=False): set plotting defaults to one of the palettes
- cycle_colors(ax=None, safe=False): apply color cycle to an axes or global rcParams
- demo(): quick visual demo of palettes (requires matplotlib)

This module is pure-Python and has optional dependencies:
- matplotlib (for colormaps and plotting)
- seaborn (optional; used only in examples)
"""
from typing import List

# 12-color, brand-aligned categorical palette
EBL_PALETTE: List[str] = [
    "#B4417E",  # 1 Cranberry Plum
    "#E774B1",  # 2 Light Cranberry
    "#810D4B",  # 3 Dark Cranberry
    "#F3A45E",  # 4 Soft Apricot
    "#FFD791",  # 5 Light Apricot
    "#C0712B",  # 6 Dark Apricot
    "#4BA6A6",  # 7 Cool Mint
    "#7ED9D9",  # 8 Light Mint
    "#187373",  # 9 Dark Mint
    "#6A2E4F",  # 10 Plum Shadow
    "#9D6182",  # 11 Light Plum
    "#37001C",  # 12 Dark Plum
]

# 12-color, colorblind-safe variant
EBL_SAFE_PALETTE: List[str] = [
    "#B63E6A", "#E982B0", "#800629",
    "#F7956A", "#FEC891", "#C34E22",
    "#4880A8", "#83BDDA", "#124271",
    "#6D2D43", "#9D6179", "#350009",
]


def get_ebl_cmap(name: str = "ebl12"):
    """Return a matplotlib ListedColormap for the brand palette.

    Parameters
    ----------
    name : str
        Name to attach to the colormap.
    """
    from matplotlib.colors import ListedColormap
    return ListedColormap(EBL_PALETTE, name=name)


def get_ebl_safe_cmap(name: str = "ebl12_safe"):
    """Return a matplotlib ListedColormap for the colorblind-safe palette."""
    from matplotlib.colors import ListedColormap
    return ListedColormap(EBL_SAFE_PALETTE, name=name)


def register_colormaps():
    """Register both colormaps with matplotlib under names 'ebl12' and 'ebl12_safe'."""
    import matplotlib as mpl
    mpl.colormaps.register(get_ebl_cmap("ebl12"), name="ebl12")
    mpl.colormaps.register(get_ebl_safe_cmap("ebl12_safe"), name="ebl12_safe")


def use_ebl_palette(safe: bool = False):
    """Set current plotting palette (matplotlib + seaborn if available).

    Parameters
    ----------
    safe : bool
        If True, use colorblind-safe palette; otherwise brand palette.
    """
    import matplotlib.pyplot as plt
    palette = EBL_SAFE_PALETTE if safe else EBL_PALETTE
    # Matplotlib color cycle
    plt.rcParams["axes.prop_cycle"] = plt.cycler(color=palette)
    # Seaborn, if present
    try:
        import seaborn as sns
        sns.set_palette(palette)
    except Exception:
        pass


def cycle_colors(ax=None, safe: bool = False):
    """Apply the palette as a color cycle to a given axes (or globally if ax is None)."""
    import matplotlib.pyplot as plt
    from cycler import cycler

    palette = EBL_SAFE_PALETTE if safe else EBL_PALETTE
    if ax is None:
        plt.rcParams["axes.prop_cycle"] = cycler(color=palette)
        return None
    ax.set_prop_cycle(cycler(color=palette))
    return ax


def demo():
    """Quick visual demo of both palettes (12 bars each)."""
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(2, 1, figsize=(10, 4), constrained_layout=True)

    labels = [f"G{i+1}" for i in range(12)]
    values = [12, 7, 9, 14, 6, 10, 11, 8, 13, 5, 15, 9]

    # Brand palette
    axes[0].bar(labels, values, color=EBL_PALETTE)
    axes[0].set_title("Economic Brain Lab — Brand Palette (12)")
    axes[0].tick_params(axis='x', rotation=0)

    # Colorblind-safe palette
    axes[1].bar(labels, values, color=EBL_SAFE_PALETTE)
    axes[1].set_title("Economic Brain Lab — Colorblind-Safe Palette (12)")
    axes[1].tick_params(axis='x', rotation=0)

    return fig, axes


if __name__ == "__main__":
    # Minimal smoke test / preview
    register_colormaps()
    use_ebl_palette(safe=False)
    fig, axes = demo()
    fig.suptitle("EBL Palettes Demo", fontsize=12)
    import matplotlib.pyplot as plt
    plt.show()
