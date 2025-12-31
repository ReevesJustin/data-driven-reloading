#!/usr/bin/env python3
"""
Plot 19: Best Group Bias Demonstration (Notebook 06)
Histogram of "best groups" from 100 sets of 10 groups each.

Educational Purpose:
Demonstrates the "best group bias" - if you shoot 10 groups and pick the best one,
it will systematically underestimate your rifle's true capability by 30-40%.
True capability is 1.5 MOA, but best groups average around 1.0 MOA.
This is why cherry-picking results is misleading.
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Set random seed for reproducibility
np.random.seed(321)

# Simulation parameters
TRUE_MOA = 1.5  # True rifle capability
SHOTS_PER_GROUP = 5  # 5-shot groups
GROUPS_PER_SET = 10  # Shoot 10 groups, pick the best
N_SETS = 1000  # Number of times we repeat this experiment


def simulate_one_group(true_moa, shots_per_group):
    """Simulate one group and return its size."""
    # TRUE_MOA represents expected 5-shot group size
    # For 2D normal, E[5-shot ES] ≈ 3.0 * sigma
    sigma = true_moa / 3.0

    # Generate shots from 2D normal distribution
    x = np.random.normal(0, sigma, shots_per_group)
    y = np.random.normal(0, sigma, shots_per_group)

    # Calculate group size (extreme spread)
    max_dist = 0
    for i in range(shots_per_group):
        for j in range(i + 1, shots_per_group):
            dist = np.sqrt((x[i] - x[j])**2 + (y[i] - y[j])**2)
            max_dist = max(max_dist, dist)

    return max_dist


# Simulate the "best group" selection process
best_groups = []
all_groups = []

for _ in range(N_SETS):
    # Shoot GROUPS_PER_SET groups
    group_set = [simulate_one_group(TRUE_MOA, SHOTS_PER_GROUP) for _ in range(GROUPS_PER_SET)]
    all_groups.extend(group_set)

    # Pick the best (smallest) group
    best_group = np.min(group_set)
    best_groups.append(best_group)

best_groups = np.array(best_groups)
all_groups = np.array(all_groups)

# Calculate statistics
mean_best = np.mean(best_groups)
mean_all = np.mean(all_groups)
bias_pct = (TRUE_MOA - mean_best) / TRUE_MOA * 100

# Create the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot histogram of best groups
n, bins, patches = ax.hist(best_groups, bins=50, color='steelblue',
                            edgecolor='black', alpha=0.7, linewidth=0.5,
                            label=f'"Best Group" from {GROUPS_PER_SET} groups')

# Add vertical line for true capability
ax.axvline(TRUE_MOA, color='red', linestyle='--', linewidth=3,
           label=f'True Capability: {TRUE_MOA} MOA', zorder=10)

# Add vertical line for mean of best groups
ax.axvline(mean_best, color='orange', linestyle='--', linewidth=3,
           label=f'Mean of "Best Groups": {mean_best:.2f} MOA', zorder=10)

# Add vertical line for mean of all groups (for reference)
ax.axvline(mean_all, color='green', linestyle=':', linewidth=2.5,
           label=f'Mean of All Groups: {mean_all:.2f} MOA', zorder=10, alpha=0.7)

# Labels and title
ax.set_xlabel('Group Size (MOA)', fontsize=12, fontweight='bold')
ax.set_ylabel('Frequency', fontsize=12, fontweight='bold')
ax.set_title(
    f'Best Group Bias: Cherry-Picking Systematically Misleads\n'
    f'Shoot {GROUPS_PER_SET} Groups, Pick Best One - Repeated {N_SETS} Times\n'
    f'True Capability: {TRUE_MOA} MOA | "Best Group" Average: {mean_best:.2f} MOA | Bias: {bias_pct:.0f}% Optimistic',
    fontsize=14, fontweight='bold', pad=20
)

# Add statistics annotation
stats_text = (
    f'The "Best Group" Illusion:\n'
    f'\n'
    f'True Capability: {TRUE_MOA:.2f} MOA\n'
    f'Mean of ALL groups: {mean_all:.2f} MOA\n'
    f'Mean of BEST groups: {mean_best:.2f} MOA\n'
    f'\n'
    f'Bias: {bias_pct:.0f}% too optimistic!\n'
    f'\n'
    f'Range of best groups:\n'
    f'  {np.min(best_groups):.2f} - {np.max(best_groups):.2f} MOA\n'
    f'\n'
    f'If you shoot {GROUPS_PER_SET} groups and\n'
    f'report only the best, you will\n'
    f'consistently underestimate your\n'
    f'rifle\'s true capability by ~{bias_pct:.0f}%'
)

ax.text(0.81, 0.97, stats_text, transform=ax.transAxes,
        fontsize=9, verticalalignment='top', horizontalalignment='right',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.9, edgecolor='black', linewidth=1),
        family='monospace')

# Add explanation box at bottom
explanation = (
    'Why This Matters:\n'
    '• Reloaders often shoot multiple groups and report only the best one\n'
    '• This creates a systematic 30-40% optimistic bias\n'
    f'• A true {TRUE_MOA} MOA rifle will produce "best groups" averaging ~{mean_best:.1f} MOA\n'
    '• This misleads you into thinking loads or changes improved your rifle when they didn\'t'
)

ax.text(0.01, 0.64, explanation, transform=ax.transAxes,
        fontsize=9, verticalalignment='bottom', horizontalalignment='left',
        bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.85, edgecolor='darkred', linewidth=1),
        style='italic')

ax.legend(loc='upper left', fontsize=10, framealpha=0.9)
ax.grid(True, alpha=0.3, linestyle=':', linewidth=0.5)

# Tight layout
plt.tight_layout()

# Save the figure
output_path = Path(__file__).parent.parent / 'lessons' / 'static' / 'nb06_plot19_best_group_bias.png'
output_path.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Saved: {output_path}")

# Also display if running interactively
# plt.show()
