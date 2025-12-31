#!/usr/bin/env python3
"""
Plot 13: Seating Depth "Sweet Spots" Illusion (Notebook 07)
Shows how small samples create false seating depth patterns.

Educational Purpose:
Demonstrates that typical 5-shot groups at different seating depths will
randomly create apparent "sweet spots" that change from test to test.
With small samples, every test finds a different "best" seating depth.
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Set random seed for reproducibility
np.random.seed(42)

# Simulation parameters
SEATING_DEPTHS = np.array([0.010, 0.020, 0.030, 0.040, 0.050])  # inches off lands
SHOTS_PER_DEPTH = 5  # Typical forum test
TRUE_GROUP_SIZE = 1.0  # MOA (flat response - no real difference)
N_SMALL_TRIALS = 4  # Number of small-sample trials to show
N_LARGE_SAMPLE = 30  # Large sample to show truth

# Function to simulate group size (Rayleigh distribution approximation)
def simulate_group_size(true_moa, n_shots):
    """Simulate extreme spread group size from circular normal distribution."""
    # TRUE_MOA represents expected 5-shot group size
    # For 2D normal, E[5-shot ES] ≈ 3.0 * sigma
    sigma = true_moa / 3.0
    x = np.random.normal(0, sigma, n_shots)
    y = np.random.normal(0, sigma, n_shots)

    # Calculate extreme spread
    max_dist = 0
    for i in range(n_shots):
        for j in range(i + 1, n_shots):
            dist = np.sqrt((x[i] - x[j])**2 + (y[i] - y[j])**2)
            max_dist = max(max_dist, dist)

    return max_dist

# Create figure with small multiples
fig = plt.figure(figsize=(14, 10))

# Top row: 4 small-sample trials
for trial_idx in range(N_SMALL_TRIALS):
    ax = plt.subplot(2, 4, trial_idx + 1)

    # Set different random seed for each trial
    np.random.seed(42 + trial_idx * 5)

    # Simulate group sizes for each seating depth
    group_sizes = []
    for depth in SEATING_DEPTHS:
        group_size = simulate_group_size(TRUE_GROUP_SIZE, SHOTS_PER_DEPTH)
        group_sizes.append(group_size)

    group_sizes = np.array(group_sizes)

    # Plot the data
    ax.plot(SEATING_DEPTHS, group_sizes, 'o-', color='steelblue',
            markersize=10, linewidth=2, markeredgecolor='darkblue',
            markeredgewidth=1.5)

    # Highlight the "best" (smallest) group
    best_idx = np.argmin(group_sizes)
    ax.plot(SEATING_DEPTHS[best_idx], group_sizes[best_idx], 'o',
            color='gold', markersize=15, markeredgecolor='orange',
            markeredgewidth=3)

    # Annotate the best - positioned at bottom left of graph
    center_x = np.mean(SEATING_DEPTHS) - 0.007  # Slightly left of center
    ax.annotate(f'Best: {group_sizes[best_idx]:.2f} MOA\nat {SEATING_DEPTHS[best_idx]:.3f}"',
                xy=(SEATING_DEPTHS[best_idx], group_sizes[best_idx]),
                xytext=(center_x, 0.1),
                fontsize=8, fontweight='bold', color='darkgreen',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='lightgreen', alpha=0.7),
                arrowprops=dict(arrowstyle='->', color='darkgreen', lw=1.5))

    # Labels
    ax.set_xlabel('Seating Depth (in off lands)', fontsize=9, fontweight='bold')
    ax.set_ylabel('Group Size (MOA)', fontsize=9, fontweight='bold')
    ax.set_title(f'Small Sample Trial {trial_idx + 1}\n({SHOTS_PER_DEPTH} shots each)',
                 fontsize=10, fontweight='bold')

    # Set consistent y-axis range
    ax.set_ylim([0, 2.5])

    ax.grid(True, alpha=0.3, linestyle=':', linewidth=0.5)

# Bottom: Large sample comparison
ax_large = plt.subplot(2, 1, 2)

# Multiple large samples to show convergence
n_large_trials = 5
all_large_group_sizes = []

for trial_idx in range(n_large_trials):
    np.random.seed(100 + trial_idx)

    large_group_sizes = []
    for depth in SEATING_DEPTHS:
        group_size = simulate_group_size(TRUE_GROUP_SIZE, N_LARGE_SAMPLE)
        large_group_sizes.append(group_size)

    all_large_group_sizes.append(large_group_sizes)

    # Plot each trial
    alpha_val = 0.3 if trial_idx < n_large_trials - 1 else 0.8
    linewidth_val = 1 if trial_idx < n_large_trials - 1 else 2.5
    label_val = 'Other trials' if trial_idx == 0 else None
    if trial_idx == n_large_trials - 1:
        label_val = f'Large sample ({N_LARGE_SAMPLE} shots each)'

    ax_large.plot(SEATING_DEPTHS, large_group_sizes, 'o-', color='steelblue',
                  alpha=alpha_val, linewidth=linewidth_val, markersize=8,
                  label=label_val)

# Add true capability line
ax_large.axhline(TRUE_GROUP_SIZE, color='red', linestyle='--', linewidth=2,
                 label=f'True capability: {TRUE_GROUP_SIZE} MOA')

# Labels
ax_large.set_xlabel('Seating Depth (inches off lands)', fontsize=11, fontweight='bold')
ax_large.set_ylabel('Group Size (MOA)', fontsize=11, fontweight='bold')
ax_large.set_title(f'Large Sample Reality: Flat Response Revealed\n'
                   f'({N_LARGE_SAMPLE} shots per depth shows no real "sweet spot")',
                   fontsize=12, fontweight='bold')

ax_large.set_ylim([0, 2.5])
ax_large.grid(True, alpha=0.3, linestyle=':', linewidth=0.5)
ax_large.legend(loc='upper right', fontsize=10)

# Overall title
fig.suptitle('Seating Depth Illusion: Small Samples Create False "Sweet Spots"\n'
             'Every Test Finds a Different "Best" - Evidence That It\'s Just Random Variation',
             fontsize=14, fontweight='bold', y=0.98)

# Add explanatory text
explanation = (
    f'Truth: All seating depths are {TRUE_GROUP_SIZE} MOA\n'
    f'Small samples ({SHOTS_PER_DEPTH} shots): Random "winner" each time\n'
    f'Large samples ({N_LARGE_SAMPLE} shots): Flat response revealed\n'
    f'\n'
    f'Lesson: Don\'t trust 5-shot seating tests!\n'
    f'Need 20-30+ shots per depth to see reality'
)

fig.text(0.99, 0.01, explanation, fontsize=8.5,
         verticalalignment='bottom', horizontalalignment='right',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.9, edgecolor='black', linewidth=1))

# Tight layout
plt.tight_layout(rect=[0, 0.04, 1, 0.96])

# Save the figure
output_path = Path(__file__).parent.parent / 'lessons' / 'static' / 'nb07_plot13_seating_depth_scatter.png'
output_path.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Saved: {output_path}")

# Also display if running interactively
# plt.show()
