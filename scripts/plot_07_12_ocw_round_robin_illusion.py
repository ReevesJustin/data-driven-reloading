#!/usr/bin/env python3
"""
Plot 12: OCW Round-Robin Convergence Illusion (Notebook 07)
Shows how OCW-style testing creates false convergence patterns.

Educational Purpose:
Demonstrates that round-robin shooting at different targets creates apparent
convergence to a point by random chance, not because of a real "node". About
1 in 5-10 trials will show convincing convergence purely by luck.
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Set random seed for reproducibility
np.random.seed(42)

# Simulation parameters
N_CHARGES = 3  # Three different charge weights
SHOTS_PER_CHARGE = 3  # Three shots each, round-robin
TRUE_MOA = 1.2  # True rifle precision (same for all charges)
N_TRIALS = 6  # Show multiple trials

# Charge weight labels
CHARGE_LABELS = ['40.5gr', '41.0gr', '41.5gr']
CHARGE_COLORS = ['red', 'blue', 'green']

# Create figure with small multiples
fig, axes = plt.subplots(2, 3, figsize=(14, 9))
axes = axes.flatten()

convergence_scores = []

for trial_idx in range(N_TRIALS):
    ax = axes[trial_idx]

    # Set different random seed for each trial
    np.random.seed(42 + trial_idx * 10)

    # Simulate shooting - all charges have same true precision
    # TRUE_MOA represents expected 5-shot group size
    # For 2D normal, E[5-shot ES] ≈ 3.0 * sigma
    sigma = TRUE_MOA / 3.0

    all_shots_x = []
    all_shots_y = []

    for charge_idx in range(N_CHARGES):
        # Each charge has its own random center point (representing aim point variation)
        # but same dispersion
        center_x = np.random.normal(0, 0.3)  # Small aim point variation
        center_y = np.random.normal(0, 0.3)

        # Generate shots
        x = np.random.normal(center_x, sigma, SHOTS_PER_CHARGE)
        y = np.random.normal(center_y, sigma, SHOTS_PER_CHARGE)

        all_shots_x.append(x)
        all_shots_y.append(y)

        # Plot shots for this charge
        ax.scatter(x, y, c=CHARGE_COLORS[charge_idx], s=100,
                   alpha=0.7, edgecolors='black', linewidths=1.5,
                   label=CHARGE_LABELS[charge_idx], marker='o')

    # Calculate "convergence score" - how tight are all shots together?
    # Measure by calculating the radius of smallest circle containing 50% of shots
    all_x = np.concatenate(all_shots_x)
    all_y = np.concatenate(all_shots_y)

    # Calculate centroid
    centroid_x = np.mean(all_x)
    centroid_y = np.mean(all_y)

    # Calculate distances from centroid
    distances = np.sqrt((all_x - centroid_x)**2 + (all_y - centroid_y)**2)
    median_distance = np.median(distances)
    max_distance = np.max(distances)

    convergence_scores.append(median_distance)

    # Draw circle around centroid to show "convergence"
    circle = plt.Circle((centroid_x, centroid_y), median_distance,
                        fill=False, edgecolor='purple', linewidth=2,
                        linestyle='--', alpha=0.5)
    ax.add_patch(circle)

    # Mark centroid
    ax.plot(centroid_x, centroid_y, 'x', color='purple', markersize=15,
            markeredgewidth=3, label='Group center')

    # Annotate if this is a "lucky" convergent trial
    if median_distance < 0.7:  # Threshold for "good convergence"
        ax.text(0.5, 0.95, 'Apparent\nConvergence!',
                transform=ax.transAxes,
                fontsize=10, fontweight='bold', color='darkgreen',
                ha='center', va='top',
                bbox=dict(boxstyle='round,pad=0.5', facecolor='lightgreen', alpha=0.8))

    # Labels
    ax.set_xlabel('Horizontal (inches at 100yd)', fontsize=9, fontweight='bold')
    ax.set_ylabel('Vertical (inches at 100yd)', fontsize=9, fontweight='bold')
    ax.set_title(f'Trial {trial_idx + 1}: Median radius = {median_distance:.2f}"',
                 fontsize=10, fontweight='bold')

    # Set consistent axes for comparison
    ax.set_xlim([-3, 3])
    ax.set_ylim([-3, 3])
    ax.set_aspect('equal')

    # Add crosshairs
    ax.axhline(0, color='gray', linestyle='--', linewidth=0.5, alpha=0.3)
    ax.axvline(0, color='gray', linestyle='--', linewidth=0.5, alpha=0.3)

    ax.legend(loc='upper left', fontsize=7)
    ax.grid(True, alpha=0.3, linestyle=':', linewidth=0.5)

# Overall title
fig.suptitle('OCW Round-Robin Illusion: Random Convergence is NOT a Real "Node"\n'
             '1 in 5-10 Trials Shows Apparent Convergence by Pure Luck',
             fontsize=14, fontweight='bold', y=0.98)

# Add explanatory text
lucky_trials = sum(1 for score in convergence_scores if score < 0.7)
explanation = (
    f'True precision: {TRUE_MOA} MOA (all charges)\n'
    f'No real "nodes" - all charges identical\n'
    f'\n'
    f'Trials showing "convergence": {lucky_trials}/{N_TRIALS}\n'
    f'This is pure random chance!\n'
    f'\n'
    f'Purple circle = 50% of shots\n'
    f'Different colors = different charges\n'
    f'\n'
    f'Message: Convergence proves nothing\n'
    f'without proper statistical testing'
)

fig.text(0.99, 0.02, explanation, fontsize=8.5,
         verticalalignment='bottom', horizontalalignment='right',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.9, edgecolor='black', linewidth=1))

# Tight layout
plt.tight_layout(rect=[0, 0.03, 1, 0.96])

# Save the figure
output_path = Path(__file__).parent.parent / 'lessons' / 'static' / 'nb07_plot12_ocw_round_robin_illusion.png'
output_path.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Saved: {output_path}")

# Also display if running interactively
# plt.show()
