#!/usr/bin/env python3
"""
Plot 6: SD Illusion - Sample Size Impact (Notebook 01)
Four panels showing how measured SD varies with sample size.

Educational Purpose:
Demonstrates that small samples give unreliable SD measurements.
True SD = 15 fps, but measured SD varies wildly with small sample sizes.
As sample size increases, measured SD converges to true value.
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Set random seed for reproducibility
np.random.seed(42)

# Simulation parameters
TRUE_SD = 15  # True standard deviation in fps
N_SAMPLES = 1000  # Number of samples to simulate for each sample size
SAMPLE_SIZES = [5, 10, 20, 30]  # Different sample sizes to compare


def simulate_sd_measurements(true_sd, sample_size, n_samples):
    """Simulate n_samples measurements of SD using given sample_size."""
    measured_sds = []

    for _ in range(n_samples):
        # Generate a sample from normal distribution with true SD
        sample = np.random.normal(0, true_sd, sample_size)
        # Calculate sample SD (using ddof=1 for sample SD)
        measured_sd = np.std(sample, ddof=1)
        measured_sds.append(measured_sd)

    return np.array(measured_sds)


# Create figure with 2x2 subplot grid
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
axes = axes.flatten()

# Simulate and plot for each sample size
for idx, sample_size in enumerate(SAMPLE_SIZES):
    ax = axes[idx]

    # Simulate SD measurements
    measured_sds = simulate_sd_measurements(TRUE_SD, sample_size, N_SAMPLES)

    # Calculate statistics
    mean_sd = np.mean(measured_sds)
    std_of_sds = np.std(measured_sds)
    min_sd = np.min(measured_sds)
    max_sd = np.max(measured_sds)

    # Calculate percentage within ±20% of true SD
    within_20_pct = np.sum(
        (measured_sds >= TRUE_SD * 0.8) & (measured_sds <= TRUE_SD * 1.2)
    ) / N_SAMPLES

    # Plot histogram
    n, bins, patches = ax.hist(measured_sds, bins=40, color='steelblue',
                                edgecolor='black', alpha=0.7, linewidth=0.5)

    # Add vertical line for true SD
    ax.axvline(TRUE_SD, color='red', linestyle='--', linewidth=2.5,
               label=f'True SD: {TRUE_SD} fps', zorder=10)

    # Add vertical line for mean of measured SDs
    ax.axvline(mean_sd, color='orange', linestyle='--', linewidth=2,
               label=f'Mean Measured: {mean_sd:.1f} fps', zorder=10)

    # Labels and title for each subplot
    ax.set_xlabel('Measured SD (fps)', fontsize=11, fontweight='bold')
    ax.set_ylabel('Frequency', fontsize=11, fontweight='bold')
    ax.set_title(f'Sample Size: {sample_size} Shots per String',
                 fontsize=12, fontweight='bold', pad=10)

    # Add statistics annotation
    stats_text = (
        f'Range: {min_sd:.1f} - {max_sd:.1f} fps\n'
        f'Spread: {max_sd - min_sd:.1f} fps\n'
        f'Std of SDs: {std_of_sds:.1f} fps\n'
        f'\n'
        f'Within ±20%: {within_20_pct:.0%}'
    )

    ax.text(0.98, 0.97, stats_text, transform=ax.transAxes,
            fontsize=9, verticalalignment='top', horizontalalignment='right',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.7),
            family='monospace')

    ax.legend(loc='upper left', fontsize=9)
    ax.grid(True, alpha=0.3, linestyle=':', linewidth=0.5)

# Overall title
fig.suptitle('SD Measurement Illusion: How Sample Size Affects Reliability\n'
             f'1,000 Measurements at Each Sample Size | True SD = {TRUE_SD} fps',
             fontsize=15, fontweight='bold', y=0.995)

# Tight layout with space for suptitle
plt.tight_layout(rect=[0, 0, 1, 0.98])

# Save the figure
output_path = Path(__file__).parent.parent / 'lessons' / 'static' / 'nb01_plot06_sd_illusion_sample_size.png'
output_path.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Saved: {output_path}")

# Also display if running interactively
# plt.show()
