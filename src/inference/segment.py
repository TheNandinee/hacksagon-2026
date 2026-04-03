import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import os


def normalize_to_rgb(image_array):
    """Convert satellite bands to displayable RGB.
    Handles both 3-band (RGB) and 4-band imagery.
    """
    if image_array.ndim == 2:
        # grayscale — stack to RGB
        rgb = np.stack([image_array] * 3, axis=-1).astype(float)
    elif image_array.shape[2] >= 3:
        rgb = image_array[:, :, :3].astype(float)
    else:
        raise ValueError(f"Unexpected image shape: {image_array.shape}")

    # Stretch each band to 0-1
    for i in range(3):
        band = rgb[:, :, i]
        p2, p98 = np.percentile(band, (2, 98))
        denom = p98 - p2
        if denom < 1e-10:
            denom = 1e-10
        rgb[:, :, i] = np.clip((band - p2) / denom, 0, 1)

    return (rgb * 255).astype(np.uint8)


def run_segmentation():
    # Load arrays
    before_raw = np.load("data/raw/before_2020.npy")
    after_raw  = np.load("data/raw/after_2024.npy")
    disturbance_mask = np.load("data/processed/disturbance_mask.npy")

    print(f"before shape: {before_raw.shape}")
    print(f"after shape:  {after_raw.shape}")
    print(f"mask shape:   {disturbance_mask.shape}")

    before_rgb = normalize_to_rgb(before_raw)
    after_rgb  = normalize_to_rgb(after_raw)

    # Save clean RGB images
    os.makedirs("data/processed", exist_ok=True)
    Image.fromarray(before_rgb).save("data/processed/before_rgb.png")
    Image.fromarray(after_rgb).save("data/processed/after_rgb.png")

    # Resize mask to match image if needed
    if disturbance_mask.shape != after_rgb.shape[:2]:
        from PIL import Image as PILImage
        mask_img = PILImage.fromarray((disturbance_mask * 255).astype(np.uint8))
        mask_img = mask_img.resize(
            (after_rgb.shape[1], after_rgb.shape[0]),
            PILImage.NEAREST
        )
        disturbance_mask = (np.array(mask_img) > 127).astype(np.uint8)
        print(f"Mask resized to: {disturbance_mask.shape}")

    # Overlay red on disturbed zones
    after_overlay = after_rgb.copy()
    after_overlay[disturbance_mask == 1, 0] = 220
    after_overlay[disturbance_mask == 1, 1] = 30
    after_overlay[disturbance_mask == 1, 2] = 30

    # Build 3-panel figure
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    fig.patch.set_facecolor("#0f0f0f")

    axes[0].imshow(before_rgb)
    axes[0].set_title("Aravali — 2020\nBaseline (pre-mining expansion)",
                       fontsize=12, fontweight="bold", color="white", pad=10)
    axes[0].axis("off")

    axes[1].imshow(after_rgb)
    axes[1].set_title("Aravali — 2024\nCurrent state",
                       fontsize=12, fontweight="bold", color="white", pad=10)
    axes[1].axis("off")

    axes[2].imshow(after_overlay)
    red_patch = mpatches.Patch(color="#DC1E1E", label="Detected disturbance zone")
    axes[2].legend(handles=[red_patch], loc="lower right",
                   fontsize=10, facecolor="#1a1a1a", labelcolor="white")
    axes[2].set_title("ARANYA Detection Output\nIllegal mining zones flagged",
                       fontsize=12, fontweight="bold", color="white", pad=10)
    axes[2].axis("off")

    for ax in axes:
        ax.set_facecolor("#0f0f0f")

    plt.suptitle("ARANYA — Autonomous Mining Detection System",
                  fontsize=15, fontweight="bold", color="white", y=1.01)
    plt.tight_layout()

    os.makedirs("outputs", exist_ok=True)
    plt.savefig("outputs/detection_output.png", dpi=150,
                bbox_inches="tight", facecolor="#0f0f0f")
    plt.close()
    print("Saved: outputs/detection_output.png")

    # Print detection summary
    disturbed = int(disturbance_mask.sum())
    total = disturbance_mask.size
    area_km2 = round(disturbed * (0.06 * 0.06), 2)
    print(f"\nDetection summary:")
    print(f"  Disturbed pixels : {disturbed} / {total}")
    print(f"  Disturbed area   : {area_km2} km²")
    print(f"  Coverage         : {round(disturbed/total*100, 1)}%")

    return "outputs/detection_output.png"


if __name__ == "__main__":
    run_segmentation()