#!/usr/bin/env python3
"""
Plot 9: Anonymized Ladder Test (Notebook 07)
Shows false patterns in charge weight testing from small samples.

Educational Purpose:
Demonstrates how random variation in small ladder tests creates illusory "nodes"
and "flat spots" that appear in one test but disappear in the next. Same rifle,
same components, different random samples = different apparent "patterns".
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Set random seed for reproducibility
np.random.seed(42)

# Simulation parameters
CHARGE_WEIGHTS = np.arange(41.0, 43.2, 0.2)  # 41.0 to 43.0 in 0.2gr steps (11 charges)
SHOTS_PER_CHARGE = 3  # Typical ladder test
TRUE_VELOCITY_SLOPE = 25  # fps per grain (linear relationship)
TRUE_SD = 12  # fps (shot-to-shot variation)
N_TRIALS = 6  # Number of different ladder tests to show

# Create figure with small multiples
fig, axes = plt.subplots(2, 3, figsize=(14, 9))
axes = axes.flatten()

# Store which trials show apparent "nodes" for annotation
interesting_trials = []

for trial_idx in range(N_TRIALS):
    ax = axes[trial_idx]

    # Generate velocities for this trial
    base_velocity = 2700  # fps at 41.0 grains
    true_velocities = base_velocity + TRUE_VELOCITY_SLOPE * (CHARGE_WEIGHTS - 41.0)

    # Add random variation
    np.random.seed(42 + trial_idx)  # Different seed for each trial
    measured_velocities = []

    for charge in CHARGE_WEIGHTS:
        true_vel = base_velocity + TRUE_VELOCITY_SLOPE * (charge - 41.0)
        shots = np.random.normal(true_vel, TRUE_SD, SHOTS_PER_CHARGE)
        avg_vel = np.mean(shots)
        measured_velocities.append(avg_vel)

    measured_velocities = np.array(measured_velocities)

    # Plot the data
    ax.plot(CHARGE_WEIGHTS, measured_velocities, 'o-', color='steelblue',
            markersize=8, linewidth=2, markeredgecolor='darkblue',
            markeredgewidth=1.5, label='Measured avg')

    # Plot true relationship
    ax.plot(CHARGE_WEIGHTS, true_velocities, '--', color='red',
            linewidth=1.5, alpha=0.6, label='True relationship')

    # Manual annotations for specific trials
    # Trial-specific node locations to highlight different "patterns"
    manual_nodes = {
        0: [(41.9, 0.3, -20)],  # Trial 1: node at 41.9
        4: [(42.4, 0.3, -20)],  # Trial 5: additional node at 42.4
        5: [(41.5, 0.3, -20), (42.9, -0.4, -20)]  # Trial 6: nodes at 41.5 and 42.9
    }

    # Add manual annotations for specific trials
    if trial_idx in manual_nodes:
        for target_charge, x_offset, y_offset in manual_nodes[trial_idx]:
            # Find the closest charge weight index
            idx = np.argmin(np.abs(CHARGE_WEIGHTS - target_charge))
            charge = CHARGE_WEIGHTS[idx]
            vel = measured_velocities[idx]

            ax.annotate('Apparent\n"node"?',
                        xy=(charge, vel),
                        xytext=(charge + x_offset, vel + y_offset),
                        fontsize=8, fontweight='bold', color='darkgreen',
                        bbox=dict(boxstyle='round,pad=0.3', facecolor='lightgreen', alpha=0.7),
                        arrowprops=dict(arrowstyle='->', color='darkgreen', lw=1.5))
        interesting_trials.append(trial_idx)
    else:
        # Auto-detect flat spots for other trials
        velocity_changes = np.diff(measured_velocities)
        expected_change = TRUE_VELOCITY_SLOPE * 0.2  # 0.2 grain steps

        # Find "flat" regions (change < 50% of expected)
        flat_spots = np.where(np.abs(velocity_changes) < expected_change * 0.5)[0]

        if len(flat_spots) > 0:
            # Annotate the first flat spot
            idx = flat_spots[0]
            mid_charge = (CHARGE_WEIGHTS[idx] + CHARGE_WEIGHTS[idx + 1]) / 2
            mid_vel = (measured_velocities[idx] + measured_velocities[idx + 1]) / 2

            ax.annotate('Apparent\n"node"?',
                        xy=(mid_charge, mid_vel),
                        xytext=(mid_charge + 0.3, mid_vel - 20),
                        fontsize=8, fontweight='bold', color='darkgreen',
                        bbox=dict(boxstyle='round,pad=0.3', facecolor='lightgreen', alpha=0.7),
                        arrowprops=dict(arrowstyle='->', color='darkgreen', lw=1.5))
            interesting_trials.append(trial_idx)

    # Labels
    ax.set_xlabel('Charge Weight (grains)', fontsize=9, fontweight='bold')
    ax.set_ylabel('Avg Velocity (fps)', fontsize=9, fontweight='bold')
    ax.set_title(f'Trial {trial_idx + 1}: 3 shots per charge',
                 fontsize=10, fontweight='bold')

    # Set consistent y-axis range for comparison
    ax.set_ylim([2680, 2790])

    ax.legend(loc='upper left', fontsize=7)
    ax.grid(True, alpha=0.3, linestyle=':', linewidth=0.5)

# Overall title
fig.suptitle('Ladder Test Illusion: Random Variation Creates False "Nodes"\n'
             'Same Rifle, Same Components, Different Random Samples = Different "Patterns"',
             fontsize=14, fontweight='bold', y=0.98)

# Add explanatory text
explanation = (
    f'True relationship: Linear, {TRUE_VELOCITY_SLOPE} fps/grain\n'
    f'Random variation: {TRUE_SD} fps SD\n'
    f'Sample size: {SHOTS_PER_CHARGE} shots per charge\n'
    f'\n'
    f'Notice: Each trial suggests different\n'
    f'"nodes" or "flat spots" - evidence that\n'
    f'apparent patterns are just randomness!'
)

fig.text(0.99, 0.02, explanation, fontsize=8.5,
         verticalalignment='bottom', horizontalalignment='right',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.9, edgecolor='black', linewidth=1))

# Tight layout
plt.tight_layout(rect=[0, 0.03, 1, 0.96])

# Save the figure
output_path = Path(__file__).parent.parent / 'lessons' / 'static' / 'nb07_plot09_anonymized_ladder_test.png'
output_path.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Saved: {output_path}")

# Also display if running interactively
# plt.show()
