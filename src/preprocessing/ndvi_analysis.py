import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import os

def compute_ndvi(image):
    """
    For RGB imagery: use Red and Green as proxy.
    True NDVI needs NIR band — this is a vegetation index approximation.
    VARI = (Green - Red) / (Green + Red - Blue)
    """
    r = image[:, :, 0].astype(float)
    g = image[:, :, 1].astype(float)
    b = image[:, :, 2].astype(float)

    # VARI — Visible Atmospherically Resistant Index
    # Works with RGB only, highly correlated with true NDVI
    denom = g + r - b
    denom[np.abs(denom) < 1e-10] = 1e-10
    vari = (g - r) / denom
    return np.clip(vari, -1, 1)

def compute_change(ndvi_before, ndvi_after):
    """
    Negative change = vegetation loss = potential mining disturbance.
    """
    return ndvi_after - ndvi_before

def classify_disturbance(change_map, threshold=-0.15):
    """
    Pixels where NDVI dropped more than threshold = disturbed.
    Returns binary mask.
    """
    return (change_map < threshold).astype(np.uint8)

def run_analysis():
    before = np.load("data/raw/before_2020.npy")
    after = np.load("data/raw/after_2024.npy")
    
    ndvi_before = compute_ndvi(before)
    ndvi_after = compute_ndvi(after)
    change = compute_change(ndvi_before, ndvi_after)
    disturbance_mask = classify_disturbance(change)
    
    # Save outputs
    np.save("data/processed/ndvi_before.npy", ndvi_before)
    np.save("data/processed/ndvi_after.npy", ndvi_after)
    np.save("data/processed/change_map.npy", change)
    np.save("data/processed/disturbance_mask.npy", disturbance_mask)
    
    # Compute disturbance stats
    total_pixels = disturbance_mask.size
    disturbed_pixels = disturbance_mask.sum()
    disturbed_pct = (disturbed_pixels / total_pixels) * 100
    area_km2 = disturbed_pixels * (0.06 * 0.06)  # 60m resolution
    
    print(f"Disturbed pixels: {disturbed_pixels} / {total_pixels}")
    print(f"Disturbed area: {area_km2:.2f} km²")
    print(f"Disturbance percentage: {disturbed_pct:.1f}%")
    
    # Generate visualization
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    
    axes[0].imshow(ndvi_before, cmap="RdYlGn", vmin=-0.3, vmax=0.8)
    axes[0].set_title("NDVI — Before (2019)", fontsize=14, fontweight="bold")
    axes[0].axis("off")
    
    axes[1].imshow(ndvi_after, cmap="RdYlGn", vmin=-0.3, vmax=0.8)
    axes[1].set_title("NDVI — After (2024)", fontsize=14, fontweight="bold")
    axes[1].axis("off")
    
    cmap_change = mcolors.LinearSegmentedColormap.from_list(
        "change", ["#8B0000", "#FF4444", "#FFFFFF", "#90EE90", "#006400"]
    )
    im = axes[2].imshow(change, cmap=cmap_change, vmin=-0.5, vmax=0.5)
    axes[2].set_title("NDVI Change (Red = Vegetation Loss)", fontsize=14, fontweight="bold")
    axes[2].axis("off")
    plt.colorbar(im, ax=axes[2], fraction=0.046)
    
    plt.suptitle("ARANYA — Aravali Disturbance Analysis", fontsize=16, fontweight="bold")
    plt.tight_layout()
    plt.savefig("outputs/ndvi_analysis.png", dpi=150, bbox_inches="tight")
    print("Saved: outputs/ndvi_analysis.png")
    
    return {
        "disturbed_area_km2": round(area_km2, 2),
        "disturbance_pct": round(disturbed_pct, 1),
        "disturbed_pixels": int(disturbed_pixels)
    }

if __name__ == "__main__":
    stats = run_analysis()
    print(stats)