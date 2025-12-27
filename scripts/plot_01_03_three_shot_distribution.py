#!/usr/bin/env python3
"""
Plot 3: Three-Shot Group Distribution (Notebook 01)
Demonstrates massive variation in 3-shot groups from a consistent rifle.

Educational Purpose:
Shows that a true 1.5 MOA rifle produces 3-shot groups ranging from 0.4 to 3.2 MOA,
illustrating why small samples mislead.
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Set random seed for reproducibility
np.random.seed(42)

# Simulation parameters
TRUE_MOA = 1.5  # True rifle capability
N_GROUPS = 1000  # Number of 3-shot groups to simulate
SHOTS_PER_GROUP = 3

# Simulate 1000 three-shot groups
group_sizes = []

for _ in range(N_GROUPS):
    # Generate shots from a 2D normal distribution
    # Convert MOA to standard deviation for 2D normal distribution
    # TRUE_MOA represents expected 5-shot group size
    # For 2D normal, E[5-shot ES] ≈ 3.0 * sigma, so sigma ≈ TRUE_MOA / 3.0
    sigma = TRUE_MOA / 3.0

    x = np.random.normal(0, sigma, SHOTS_PER_GROUP)
    y = np.random.normal(0, sigma, SHOTS_PER_GROUP)

    # Calculate group size (extreme spread - max distance between any two shots)
    max_dist = 0
    for i in range(SHOTS_PER_GROUP):
        for j in range(i + 1, SHOTS_PER_GROUP):
            dist = np.sqrt((x[i] - x[j])**2 + (y[i] - y[j])**2)
            max_dist = max(max_dist, dist)

    group_sizes.append(max_dist)

# Convert to numpy array for calculations
group_sizes = np.array(group_sizes)

# Calculate statistics
best_group = np.min(group_sizes)
worst_group = np.max(group_sizes)
mean_group = np.mean(group_sizes)
groups_within_20_percent = np.sum(
    (group_sizes >= TRUE_MOA * 0.8) & (group_sizes <= TRUE_MOA * 1.2)
) / N_GROUPS

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot histogram
n, bins, patches = ax.hist(group_sizes, bins=40, color='steelblue',
                            edgecolor='black', alpha=0.7, linewidth=0.5)

# Add vertical line for true capability
ax.axvline(TRUE_MOA, color='red', linestyle='--', linewidth=2,
           label=f'True Capability: {TRUE_MOA} MOA')

# Add vertical line for mean
ax.axvline(mean_group, color='orange', linestyle='--', linewidth=2,
           label=f'Mean of Groups: {mean_group:.2f} MOA')

# Labels and title
ax.set_xlabel('Group Size (MOA)', fontsize=12, fontweight='bold')
ax.set_ylabel('Frequency', fontsize=12, fontweight='bold')
ax.set_title('Distribution of 1,000 Three-Shot Groups\nFrom True 1.5 MOA Rifle',
             fontsize=14, fontweight='bold', pad=20)

# Add statistics annotation
stats_text = (
    f'Best Group: {best_group:.2f} MOA\n'
    f'Worst Group: {worst_group:.2f} MOA\n'
    f'Average: {mean_group:.2f} MOA\n'
    f'\n'
    f'Groups within ±20% of truth: {groups_within_20_percent:.0%}\n'
    f'Groups "lying" by >20%: {1-groups_within_20_percent:.0%}'
)

ax.text(0.98, 0.97, stats_text, transform=ax.transAxes,
        fontsize=10, verticalalignment='top', horizontalalignment='right',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

ax.legend(loc='upper left', fontsize=10)
ax.grid(True, alpha=0.3, linestyle=':', linewidth=0.5)

# Tight layout
plt.tight_layout()

# Save the figure
output_path = Path(__file__).parent.parent / 'lessons' / 'static' / 'nb01_plot03_three_shot_distribution.png'
output_path.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Saved: {output_path}")

# Also display if running interactively
# plt.show()
