#!/usr/bin/env python3
"""
Plot 5: Which Load Is Better? Challenge (Notebook 01)
3x2 grid of targets showing 6 five-shot groups - all from the same 1.2 MOA rifle.

Educational Purpose:
Dramatically demonstrates how random variation creates apparent differences.
All 6 groups are from the SAME rifle with IDENTICAL capability, yet they
look convincingly different. This is the core illusion that misleads reloaders.
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Set random seed for reproducibility
np.random.seed(108)  # Seed chosen to give representative group sizes

# Simulation parameters
TRUE_MOA = 1.2  # True rifle capability
SHOTS_PER_GROUP = 5
N_GROUPS = 3  # 3 groups to display in 1x3 grid


def simulate_one_group(true_moa, shots_per_group):
    """Simulate one group and return shot coordinates and group size."""
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

    return x, y, max_dist


# Create figure with 1x3 subplot grid
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Simulate and plot each group
group_sizes = []
for idx in range(N_GROUPS):
    ax = axes[idx]

    # Simulate one group
    x, y, group_size = simulate_one_group(TRUE_MOA, SHOTS_PER_GROUP)
    group_sizes.append(group_size)

    # Plot shots
    ax.scatter(x, y, s=150, c='steelblue', edgecolors='darkblue',
               linewidths=2, alpha=0.7, zorder=10)

    # Draw circles to represent MOA reference
    # Add reference circles for 1 MOA and 2 MOA
    circle_1moa = plt.Circle((0, 0), 1.0, color='lightgray',
                             fill=False, linestyle='--', linewidth=1, alpha=0.5)
    circle_2moa = plt.Circle((0, 0), 2.0, color='lightgray',
                             fill=False, linestyle='--', linewidth=1, alpha=0.3)
    ax.add_patch(circle_1moa)
    ax.add_patch(circle_2moa)

    # Mark center
    ax.plot(0, 0, 'r+', markersize=15, markeredgewidth=2)

    # Set equal aspect ratio and limits
    ax.set_aspect('equal')
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)

    # Add grid
    ax.grid(True, alpha=0.3, linestyle=':', linewidth=0.5)

    # Title with group size
    ax.set_title(f'Load {chr(65 + idx)}: {group_size:.2f} MOA',
                 fontsize=12, fontweight='bold', pad=10)

    # Labels
    ax.set_xlabel('Inches', fontsize=10)
    ax.set_ylabel('Inches', fontsize=10)

# Overall title
mean_group_size = np.mean(group_sizes)
std_group_size = np.std(group_sizes)
min_group_size = np.min(group_sizes)
max_group_size = np.max(group_sizes)

fig.suptitle(
    f'Which Load Is Better? They\'re ALL THE SAME!\n'
    f'Three 5-Shot Groups from Identical {TRUE_MOA} MOA Rifle\n'
    f'Range: {min_group_size:.2f} to {max_group_size:.2f} MOA | '
    f'Mean: {mean_group_size:.2f} MOA | Std: {std_group_size:.2f} MOA',
    fontsize=15, fontweight='bold', y=1.02
)

# Add explanation text at bottom
explanation = (
    "These groups look different and you might be tempted to choose 'Load A' or another as 'better.'\n"
    "But they're all from the SAME rifle with IDENTICAL capability. The differences are pure random variation.\n"
    "This is the fundamental illusion that misleads reloaders into thinking they've found improvements."
)

fig.text(0.5, 0.02, explanation, ha='center', fontsize=11,
         style='italic', wrap=True,
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.6))

# Tight layout with space for suptitle and bottom text
plt.tight_layout(rect=[0, 0.06, 1, 0.95])

# Save the figure
output_path = Path(__file__).parent.parent / 'lessons' / 'static' / 'nb01_plot05_which_load_better.png'
output_path.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Saved: {output_path}")

# Also display if running interactively
# plt.show()
