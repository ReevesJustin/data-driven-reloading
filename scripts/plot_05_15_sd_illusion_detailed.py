#!/usr/bin/env python3
"""
Plot 15: The SD Illusion (Notebook 05)
Demonstrates systematic underestimation of SD in small samples.

Educational Purpose:
Shows that SD calculated from small samples systematically underestimates
true population SD. This is the "perverse nature" Denton Bramwell warned about.
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from scipy import stats

# Set random seed for reproducibility
np.random.seed(42)

# Population parameters
TRUE_MEAN = 2850  # fps
TRUE_SD = 15  # fps
N_TRIALS = 500  # Number of samples to simulate

# Sample sizes to test
sample_sizes = [5, 10, 20, 30]

# Create figure with 2x2 subplots
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
axes = axes.flatten()

for idx, n_shots in enumerate(sample_sizes):
    # Simulate N_TRIALS samples of size n_shots
    calculated_sds = []

    for _ in range(N_TRIALS):
        sample = np.random.normal(TRUE_MEAN, TRUE_SD, n_shots)
        sample_sd = np.std(sample, ddof=1)
        calculated_sds.append(sample_sd)

    calculated_sds = np.array(calculated_sds)

    # Calculate statistics
    mean_measured_sd = np.mean(calculated_sds)
    percent_below_10 = 100 * np.sum(calculated_sds < 10) / N_TRIALS
    percent_within_20pct = 100 * np.sum(
        (calculated_sds >= TRUE_SD * 0.8) & (calculated_sds <= TRUE_SD * 1.2)
    ) / N_TRIALS

    # Plot histogram
    ax = axes[idx]
    n, bins, patches = ax.hist(calculated_sds, bins=25, color='steelblue',
                                 edgecolor='black', alpha=0.7, linewidth=0.5)

    # Add vertical line for true SD
    ax.axvline(TRUE_SD, color='red', linestyle='--', linewidth=2.5,
               label=f'True SD: {TRUE_SD} fps', zorder=10)

    # Add vertical line for mean measured SD
    ax.axvline(mean_measured_sd, color='orange', linestyle='--', linewidth=2,
               label=f'Mean Measured: {mean_measured_sd:.1f} fps', zorder=10)

    # Labels and title
    ax.set_xlabel('Calculated SD (fps)', fontsize=11, fontweight='bold')
    ax.set_ylabel('Frequency', fontsize=11, fontweight='bold')
    ax.set_title(f'{n_shots}-Shot Samples\n({N_TRIALS} trials)',
                 fontsize=12, fontweight='bold')

    # Stats annotation
    stats_text = (
        f'Mean SD: {mean_measured_sd:.1f} fps\n'
        f'Range: {np.min(calculated_sds):.1f} - {np.max(calculated_sds):.1f} fps\n'
        f'\n'
        f'SD < 10 fps: {percent_below_10:.0f}%\n'
        f'Within ±20%: {percent_within_20pct:.0f}%'
    )

    ax.text(0.97, 0.97, stats_text, transform=ax.transAxes,
            fontsize=9, verticalalignment='top', horizontalalignment='right',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

    ax.legend(loc='upper left', fontsize=9)
    ax.grid(True, alpha=0.3, linestyle=':', linewidth=0.5)

    # Adjust x-axis limits for consistency
    if n_shots <= 10:
        ax.set_xlim(0, 35)
    else:
        ax.set_xlim(5, 25)

# Add main title
fig.suptitle('The Perverse Nature of Standard Deviation: Small Samples Systematically Underestimate',
             fontsize=15, fontweight='bold', y=0.98)

# Add main insight text
fig.text(0.5, 0.02,
         'Key Insight: With < 30 shots, measured SD is often much lower than true SD by pure chance.\n' +
         'That "amazing" 8 fps SD from 10 shots is likely from a 15 fps load that got lucky.',
         ha='center', fontsize=11, fontweight='bold', style='italic',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9,
                   edgecolor='orange', linewidth=2))

# Tight layout
plt.tight_layout(rect=[0, 0.06, 1, 0.96])

# Save the figure
output_path = Path(__file__).parent.parent / 'lessons' / 'static' / 'nb05_plot15_sd_illusion.png'
output_path.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Saved: {output_path}")
