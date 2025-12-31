#!/usr/bin/env python3
"""
Plot 16: Velocity Node Illusion (Notebook 05)
Scatter plot showing charge weight vs velocity with perfectly linear true relationship.

Educational Purpose:
Demonstrates that "velocity nodes" (flat spots) are an illusion created by random scatter.
The TRUE relationship is perfectly linear, but random measurement variation creates
apparent flat spots and nodes. Overlaying multiple ladder tests shows the variation.
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Set random seed for reproducibility
np.random.seed(456)

# Simulation parameters
MIN_CHARGE = 40.0  # grains
MAX_CHARGE = 44.0  # grains
CHARGE_STEP = 0.3  # grains
TRUE_VELOCITY_AT_MIN = 2700  # fps at minimum charge
TRUE_VELOCITY_PER_GRAIN = 25  # fps per grain increase (perfectly linear)
VELOCITY_SD = 15  # Standard deviation of velocity measurements (fps)
N_LADDER_TESTS = 100  # Number of ladder tests to overlay


def true_velocity(charge_weight):
    """Calculate the TRUE velocity for a given charge weight (perfectly linear)."""
    return TRUE_VELOCITY_AT_MIN + (charge_weight - MIN_CHARGE) * TRUE_VELOCITY_PER_GRAIN


def measured_velocity(charge_weight):
    """Simulate measured velocity with random error."""
    true_vel = true_velocity(charge_weight)
    return true_vel + np.random.normal(0, VELOCITY_SD)


# Generate charge weights for ladder test
charge_weights = np.arange(MIN_CHARGE, MAX_CHARGE + CHARGE_STEP, CHARGE_STEP)

# Create the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot multiple ladder tests in light gray to show variation
for _ in range(N_LADDER_TESTS):
    velocities = [measured_velocity(cw) for cw in charge_weights]
    ax.plot(charge_weights, velocities, 'o-', color='lightgray',
            alpha=0.2, linewidth=0.5, markersize=3)

# Plot one "your ladder test" in color to highlight
your_velocities = [measured_velocity(cw) for cw in charge_weights]
ax.plot(charge_weights, your_velocities, 'o-', color='steelblue',
        linewidth=2, markersize=8, label='Your Ladder Test',
        markeredgecolor='darkblue', markeredgewidth=1.5, zorder=10)

# Plot the TRUE relationship (perfectly linear) in red
true_velocities = [true_velocity(cw) for cw in charge_weights]
ax.plot(charge_weights, true_velocities, '--', color='red',
        linewidth=3, label='True Relationship (Perfectly Linear)',
        zorder=15)

# Labels and title
ax.set_xlabel('Charge Weight (grains)', fontsize=12, fontweight='bold')
ax.set_ylabel('Velocity (fps)', fontsize=12, fontweight='bold')
ax.set_title('Velocity "Nodes" Are an Illusion Created by Random Scatter\n'
             f'True Relationship is Perfectly Linear: {TRUE_VELOCITY_PER_GRAIN} fps/grain\n'
             f'100 Ladder Tests Overlaid (gray) | Measurement SD = {VELOCITY_SD} fps',
             fontsize=14, fontweight='bold', pad=20)

# Add annotation pointing to the 42.0gr region (commonly identified as a "node")
# Find the index for 42.0gr charge weight
target_charge = 42.0
target_idx = np.argmin(np.abs(charge_weights - target_charge))

# Annotate apparent node at 42.0gr
ax.annotate('Apparent "Node"\n(actually random)',
            xy=(charge_weights[target_idx], your_velocities[target_idx]),
            xytext=(charge_weights[target_idx] - 0.1, your_velocities[target_idx] - 30),
            fontsize=10, fontweight='bold', color='darkred',
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7),
            arrowprops=dict(arrowstyle='->', color='darkred', linewidth=2))

# Add explanation text box
explanation_text = (
    f'The Truth:\n'
    f'• Velocity increases {TRUE_VELOCITY_PER_GRAIN} fps per grain (linear)\n'
    f'• No "nodes" or "flat spots" exist\n'
    f'• Random scatter (SD={VELOCITY_SD} fps) creates illusion\n'
    f'\n'
    f'What You See:\n'
    f'• Apparent flat spots and jumps\n'
    f'• Each test looks different\n'
    f'• All are random variation around truth'
)

ax.text(0.02, 0.97, explanation_text, transform=ax.transAxes,
        fontsize=10, verticalalignment='top', horizontalalignment='left',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8),
        family='monospace')

ax.legend(loc='lower right', fontsize=11, framealpha=0.9)
ax.grid(True, alpha=0.3, linestyle=':', linewidth=0.5)

# Tight layout
plt.tight_layout()

# Save the figure
output_path = Path(__file__).parent.parent / 'lessons' / 'static' / 'nb05_plot16_velocity_node_illusion.png'
output_path.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Saved: {output_path}")

# Also display if running interactively
# plt.show()
