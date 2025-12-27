#!/usr/bin/env python3
"""
Plot 4: Five-Shot Group Distribution Comparison (Notebook 01)
Overlaid histograms comparing 3-shot vs 5-shot groups from a 1.5 MOA rifle.

Educational Purpose:
Shows that 5-shot groups are better than 3-shot groups but still unreliable.
The 5-shot distribution is narrower but still shows substantial variation.
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Set random seed for reproducibility
np.random.seed(42)

# Simulation parameters
TRUE_MOA = 1.5  # True rifle capability
N_GROUPS = 1000  # Number of groups to simulate for each


def simulate_groups(n_groups, shots_per_group, true_moa):
    """Simulate groups and return their sizes."""
    group_sizes = []
    # TRUE_MOA represents expected 5-shot group size
    # For 2D normal, E[5-shot ES] ≈ 3.0 * sigma, so sigma ≈ TRUE_MOA / 3.0
    sigma = true_moa / 3.0

    for _ in range(n_groups):
        # Generate shots from a 2D normal distribution
        x = np.random.normal(0, sigma, shots_per_group)
        y = np.random.normal(0, sigma, shots_per_group)

        # Calculate group size (extreme spread - max distance between any two shots)
        max_dist = 0
        for i in range(shots_per_group):
            for j in range(i + 1, shots_per_group):
                dist = np.sqrt((x[i] - x[j])**2 + (y[i] - y[j])**2)
                max_dist = max(max_dist, dist)

        group_sizes.append(max_dist)

    return np.array(group_sizes)


# Simulate both 3-shot and 5-shot groups
three_shot_groups = simulate_groups(N_GROUPS, 3, TRUE_MOA)
five_shot_groups = simulate_groups(N_GROUPS, 5, TRUE_MOA)

# Calculate statistics
three_shot_mean = np.mean(three_shot_groups)
five_shot_mean = np.mean(five_shot_groups)
three_shot_std = np.std(three_shot_groups)
five_shot_std = np.std(five_shot_groups)

# Create the plot
fig, ax = plt.subplots(figsize=(12, 7))

# Plot overlaid histograms with transparency
ax.hist(three_shot_groups, bins=40, color='lightcoral', edgecolor='darkred',
        alpha=0.6, linewidth=0.8, label=f'3-Shot Groups (mean={three_shot_mean:.2f})')
ax.hist(five_shot_groups, bins=40, color='steelblue', edgecolor='darkblue',
        alpha=0.6, linewidth=0.8, label=f'5-Shot Groups (mean={five_shot_mean:.2f})')

# Add vertical line for true capability
ax.axvline(TRUE_MOA, color='red', linestyle='--', linewidth=2.5,
           label=f'True Capability: {TRUE_MOA} MOA', zorder=10)

# Labels and title
ax.set_xlabel('Group Size (MOA)', fontsize=12, fontweight='bold')
ax.set_ylabel('Frequency', fontsize=12, fontweight='bold')
ax.set_title('3-Shot vs 5-Shot Groups: Both Show Substantial Variation\n'
             f'1,000 Groups Each from True {TRUE_MOA} MOA Rifle',
             fontsize=14, fontweight='bold', pad=20)

# Add statistics annotation
stats_text = (
    f'3-Shot Groups:\n'
    f'  Mean: {three_shot_mean:.2f} MOA\n'
    f'  Std Dev: {three_shot_std:.2f} MOA\n'
    f'  Range: {np.min(three_shot_groups):.2f} - {np.max(three_shot_groups):.2f} MOA\n'
    f'\n'
    f'5-Shot Groups:\n'
    f'  Mean: {five_shot_mean:.2f} MOA\n'
    f'  Std Dev: {five_shot_std:.2f} MOA\n'
    f'  Range: {np.min(five_shot_groups):.2f} - {np.max(five_shot_groups):.2f} MOA\n'
    f'\n'
    f'5-shot is {((three_shot_std - five_shot_std) / three_shot_std * 100):.0f}% less variable\n'
    f'but still unreliable!'
)

ax.text(0.98, 0.97, stats_text, transform=ax.transAxes,
        fontsize=10, verticalalignment='top', horizontalalignment='right',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8),
        family='monospace')

ax.legend(loc='upper left', fontsize=11, framealpha=0.9)
ax.grid(True, alpha=0.3, linestyle=':', linewidth=0.5)

# Tight layout
plt.tight_layout()

# Save the figure
output_path = Path(__file__).parent.parent / 'lessons' / 'static' / 'nb01_plot04_five_shot_comparison.png'
output_path.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Saved: {output_path}")

# Also display if running interactively
# plt.show()
