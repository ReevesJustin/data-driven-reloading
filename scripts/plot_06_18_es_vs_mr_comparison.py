#!/usr/bin/env python3
"""
Plot 18: ES vs MR (Mean Radius) Comparison (Notebook 06)
Dual line plot showing ES and MR vs shot count.

Educational Purpose:
Demonstrates that Extreme Spread (ES) grows forever as sample size increases,
while Mean Radius (MR) stabilizes quickly. This shows why ES is a poor metric
for rifle precision and why MR is much more reliable.
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Set random seed for reproducibility
np.random.seed(789)

# Simulation parameters
TRUE_MOA = 1.0  # True rifle capability
MAX_SHOTS = 100  # Maximum number of shots to simulate
N_TRIALS = 200  # Number of trials to average over


def simulate_es_and_mr_progression(true_moa, max_shots, n_trials):
    """
    Simulate how ES and MR change as shot count increases.
    Returns arrays of shot counts, average ES, and average MR.
    """
    # TRUE_MOA represents expected 5-shot group size
    # For 2D normal, E[5-shot ES] ≈ 3.0 * sigma
    sigma = true_moa / 3.0

    shot_counts = range(3, max_shots + 1)
    es_values = []
    mr_values = []

    for n_shots in shot_counts:
        es_trial = []
        mr_trial = []

        for _ in range(n_trials):
            # Generate shots from 2D normal distribution
            x = np.random.normal(0, sigma, n_shots)
            y = np.random.normal(0, sigma, n_shots)

            # Calculate ES (extreme spread - max distance between any two shots)
            max_dist = 0
            for i in range(n_shots):
                for j in range(i + 1, n_shots):
                    dist = np.sqrt((x[i] - x[j])**2 + (y[i] - y[j])**2)
                    max_dist = max(max_dist, dist)
            es_trial.append(max_dist)

            # Calculate MR (mean radius - average distance from center of group)
            # First find center of group
            center_x = np.mean(x)
            center_y = np.mean(y)

            # Then calculate mean distance from center
            distances = np.sqrt((x - center_x)**2 + (y - center_y)**2)
            mean_radius = np.mean(distances)
            mr_trial.append(mean_radius)

        # Average over trials
        es_values.append(np.mean(es_trial))
        mr_values.append(np.mean(mr_trial))

    return np.array(list(shot_counts)), np.array(es_values), np.array(mr_values)


# Simulate the progression
shot_counts, es_values, mr_values = simulate_es_and_mr_progression(TRUE_MOA, MAX_SHOTS, N_TRIALS)

# Create the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot ES and MR
line1 = ax.plot(shot_counts, es_values, 'o-', color='coral', linewidth=2.5,
                markersize=4, label='Extreme Spread (ES)', markevery=5)
line2 = ax.plot(shot_counts, mr_values, 's-', color='steelblue', linewidth=2.5,
                markersize=4, label='Mean Radius (MR)', markevery=5)

# Add horizontal line for true capability reference
ax.axhline(TRUE_MOA, color='red', linestyle='--', linewidth=2,
           label=f'True Rifle Capability: {TRUE_MOA} MOA', alpha=0.7)

# Add shaded region to show where MR stabilizes
stabilization_point = 20
ax.axvspan(stabilization_point, MAX_SHOTS, alpha=0.1, color='green',
           label=f'MR Stable Region (>{stabilization_point} shots)')

# Labels and title
ax.set_xlabel('Number of Shots in Group', fontsize=12, fontweight='bold')
ax.set_ylabel('Group Size (MOA)', fontsize=12, fontweight='bold')
ax.set_title('ES Grows Forever, MR Stabilizes\n'
             f'Why ES Is Unreliable and MR Is Better | True {TRUE_MOA} MOA Rifle\n'
             f'Averaged over {N_TRIALS} trials at each shot count',
             fontsize=14, fontweight='bold', pad=20)

# Add annotations
# Annotate ES growing
es_at_5 = es_values[shot_counts.tolist().index(5)]
es_at_50 = es_values[shot_counts.tolist().index(50)]
es_at_100 = es_values[-1]

ax.annotate(f'ES at 5 shots:\n{es_at_5:.2f} MOA',
            xy=(5, es_at_5),
            xytext=(8, es_at_5 - 0.2),
            fontsize=8.5, color='darkred',
            bbox=dict(boxstyle='round', facecolor='mistyrose', alpha=0.8),
            arrowprops=dict(arrowstyle='->', color='darkred', linewidth=1.5))

ax.annotate(f'ES at 100 shots:\n{es_at_100:.2f} MOA\n(still growing!)',
            xy=(100, es_at_100),
            xytext=(70, es_at_100 + 0.02),
            fontsize=8.5, color='darkred',
            bbox=dict(boxstyle='round', facecolor='mistyrose', alpha=0.8),
            arrowprops=dict(arrowstyle='->', color='darkred', linewidth=1.5))

# Annotate MR stabilization
mr_at_20 = mr_values[shot_counts.tolist().index(20)]
mr_at_100 = mr_values[-1]

ax.annotate(f'MR stabilizes\n{mr_at_100:.2f} MOA',
            xy=(50, mr_at_100),
            xytext=(50, mr_at_100 - 0.3),
            fontsize=8.5, color='darkblue',
            bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8),
            arrowprops=dict(arrowstyle='->', color='darkblue', linewidth=1.5))

# Add explanation text box
explanation_text = (
    f'Key Insights:\n'
    f'• ES increases with every shot (unbounded)\n'
    f'• ES at 100 shots: {es_at_100:.2f} MOA (>{es_at_100/es_at_5:.1f}x larger than 5-shot)\n'
    f'• MR stabilizes around {stabilization_point} shots\n'
    f'• MR at 100 shots: {mr_at_100:.2f} MOA (stable)\n'
    f'\n'
    f'Conclusion:\n'
    f'Use MR, not ES, for reliable precision measurement'
)

ax.text(0.35, 0.70, explanation_text, transform=ax.transAxes,
        fontsize=8.5, verticalalignment='top', horizontalalignment='left',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.9, edgecolor='black', linewidth=1),
        family='monospace')

ax.legend(loc='upper right', bbox_to_anchor=(0.92, 0.80), fontsize=10, framealpha=0.9)
ax.grid(True, alpha=0.3, linestyle=':', linewidth=0.5)

# Set y-axis limits to show the growth clearly
ax.set_ylim(0, max(es_values) * 1.1)

# Tight layout
plt.tight_layout()

# Save the figure
output_path = Path(__file__).parent.parent / 'lessons' / 'static' / 'nb06_plot18_es_vs_mr_comparison.png'
output_path.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Saved: {output_path}")

# Also display if running interactively
# plt.show()
