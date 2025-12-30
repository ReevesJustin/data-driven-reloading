#!/usr/bin/env python3
"""
Plot 26: Three Types of Consistency - Independent Concepts (Notebook 02)
Visual demonstration that velocity SD, precision, and their correlation are independent.

Educational Purpose:
Shows three distinct scenarios to illustrate that velocity consistency and
precision consistency are related but NOT the same thing:
1. Low velocity SD, good precision (ideal correlation)
2. Low velocity SD, poor precision (other factors dominate)
3. High velocity SD, good precision at 100 yards (velocity matters less at short range)

This breaks the common misconception that "low SD = tight groups automatically."
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Set random seed for reproducibility
np.random.seed(42)

# Create the figure
fig, axes = plt.subplots(2, 3, figsize=(16, 11))
fig.suptitle('The Three Types of Consistency: Velocity, Precision, and Their Relationship',
             fontsize=18, fontweight='bold', y=0.995)

# Simulation parameters
n_shots = 30

# Scenario 1: Low SD, Good Precision (High Correlation)
# This is the ideal case where good velocity consistency leads to good precision
mean_velocity_1 = 2850
sd_velocity_1 = 8  # Low SD
precision_1 = 0.6  # Good precision (MOA)

velocities_1 = np.random.normal(mean_velocity_1, sd_velocity_1, n_shots)
# Create positions that correlate with velocity
# Higher velocity = higher impact (simplified ballistics)
base_positions_y_1 = (velocities_1 - mean_velocity_1) / sd_velocity_1 * 0.2
positions_x_1 = np.random.normal(0, precision_1 * 0.3, n_shots)
positions_y_1 = base_positions_y_1 + np.random.normal(0, precision_1 * 0.3, n_shots)

# Scenario 2: Low SD, Poor Precision (Low Correlation)
# Good velocity consistency but other factors cause poor precision
mean_velocity_2 = 2850
sd_velocity_2 = 8  # Low SD (same as scenario 1)
precision_2 = 1.4  # Poor precision (MOA)

velocities_2 = np.random.normal(mean_velocity_2, sd_velocity_2, n_shots)
# Positions are mostly independent of velocity (other factors dominate)
positions_x_2 = np.random.normal(0, precision_2 * 0.4, n_shots)
positions_y_2 = np.random.normal(0, precision_2 * 0.4, n_shots)

# Scenario 3: High SD, Good Precision (at short range)
# Poor velocity consistency but precision is good at short range
mean_velocity_3 = 2850
sd_velocity_3 = 20  # High SD
precision_3 = 0.7  # Good precision at 100 yards (MOA)

velocities_3 = np.random.normal(mean_velocity_3, sd_velocity_3, n_shots)
# At 100 yards, velocity variation doesn't dominate yet
positions_x_3 = np.random.normal(0, precision_3 * 0.35, n_shots)
positions_y_3 = np.random.normal(0, precision_3 * 0.35, n_shots)

# Plot all three scenarios
scenarios = [
    {
        'title': 'LOW SD + GOOD PRECISION\n(High Correlation)',
        'subtitle': 'The Ideal Load',
        'velocities': velocities_1,
        'positions_x': positions_x_1,
        'positions_y': positions_y_1,
        'mean_velocity': mean_velocity_1,
        'sd_velocity': sd_velocity_1,
        'precision': precision_1,
        'color': 'darkgreen',
        'interpretation': 'Good velocity control AND\ngood precision. Everything\nworking together.\n\nVelocity consistency helps\nprecision (especially at\nlong range).'
    },
    {
        'title': 'LOW SD + POOR PRECISION\n(Low Correlation)',
        'subtitle': 'Velocity Isn\'t Everything',
        'velocities': velocities_2,
        'positions_x': positions_x_2,
        'positions_y': positions_y_2,
        'mean_velocity': mean_velocity_2,
        'sd_velocity': sd_velocity_2,
        'precision': precision_2,
        'color': 'orange',
        'interpretation': 'Good velocity control BUT\npoor precision.\n\nOther factors dominate:\n• Bullet quality\n• Barrel fouling\n• Bedding issues\n• Shooter technique'
    },
    {
        'title': 'HIGH SD + GOOD PRECISION\n(At 100 Yards)',
        'subtitle': 'Distance Matters',
        'velocities': velocities_3,
        'positions_x': positions_x_3,
        'positions_y': positions_y_3,
        'mean_velocity': mean_velocity_3,
        'sd_velocity': sd_velocity_3,
        'precision': precision_3,
        'color': 'steelblue',
        'interpretation': 'Poor velocity control BUT\ngood precision at short range.\n\nVelocity matters MORE\nat long range.\n\nAt 100 yds: tolerable\nAt 600 yds: problematic'
    }
]

# Top row: Velocity distributions
for idx, (ax, scenario) in enumerate(zip(axes[0], scenarios)):
    # Plot velocity distribution
    ax.hist(scenario['velocities'], bins=15, color=scenario['color'],
           alpha=0.7, edgecolor='black', linewidth=1.5)

    # Add mean line
    ax.axvline(scenario['mean_velocity'], color='red', linestyle='--',
              linewidth=3, label=f'Mean: {scenario["mean_velocity"]:.0f} fps')

    # Add SD annotation
    sd_actual = np.std(scenario['velocities'], ddof=1)
    ax.text(0.95, 0.95,
           f'True SD: {scenario["sd_velocity"]} fps\n'
           f'Measured SD: {sd_actual:.1f} fps\n'
           f'({n_shots} shots)',
           transform=ax.transAxes, fontsize=10,
           verticalalignment='top', horizontalalignment='right',
           bbox=dict(boxstyle='round,pad=0.5', facecolor='wheat', alpha=0.8),
           fontweight='bold')

    ax.set_xlabel('Velocity (fps)', fontsize=11, fontweight='bold')
    ax.set_ylabel('Count', fontsize=11, fontweight='bold')
    ax.set_title(scenario['title'], fontsize=12, fontweight='bold',
                color=scenario['color'])
    ax.grid(True, alpha=0.3, linestyle=':', linewidth=0.5)
    ax.legend(fontsize=9)

# Bottom row: Target impacts (precision)
for idx, (ax, scenario) in enumerate(zip(axes[1], scenarios)):
    # Draw target rings (5 MOA target at 100 yards = ~5 inch radius)
    target_radius = 3  # inches
    for ring_r in [3, 2, 1]:
        circle = plt.Circle((0, 0), ring_r, fill=False, edgecolor='lightgray',
                           linewidth=1.5, zorder=1)
        ax.add_patch(circle)

    # Draw aim point
    ax.plot([-0.2, 0.2], [0, 0], 'r-', linewidth=3, zorder=5)
    ax.plot([0, 0], [-0.2, 0.2], 'r-', linewidth=3, zorder=5)

    # Plot shots
    ax.scatter(scenario['positions_x'], scenario['positions_y'],
              c=scenario['color'], s=120, alpha=0.7,
              edgecolors='black', linewidths=1.5, zorder=10)

    # Calculate and show group center
    center_x = np.mean(scenario['positions_x'])
    center_y = np.mean(scenario['positions_y'])
    ax.scatter([center_x], [center_y], c='gold', s=250, marker='*',
              edgecolors='black', linewidths=2, zorder=15, label='Group Center')

    # Calculate mean radius
    distances = np.sqrt((scenario['positions_x'] - center_x)**2 +
                       (scenario['positions_y'] - center_y)**2)
    mean_radius = np.mean(distances)

    # Add precision annotation
    ax.text(0.95, 0.95,
           f'True Precision: {scenario["precision"]:.1f} MOA\n'
           f'Measured MR: {mean_radius:.2f} in\n'
           f'(≈ {mean_radius:.2f} MOA @ 100 yds)',
           transform=ax.transAxes, fontsize=10,
           verticalalignment='top', horizontalalignment='right',
           bbox=dict(boxstyle='round,pad=0.5', facecolor='lightblue', alpha=0.8),
           fontweight='bold')

    # Add interpretation
    ax.text(0.05, 0.05,
           scenario['interpretation'],
           transform=ax.transAxes, fontsize=9,
           verticalalignment='bottom', horizontalalignment='left',
           bbox=dict(boxstyle='round,pad=0.5', facecolor='wheat', alpha=0.8),
           family='monospace')

    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    ax.set_aspect('equal')
    ax.set_xlabel('Horizontal (inches @ 100 yds)', fontsize=11, fontweight='bold')
    ax.set_ylabel('Vertical (inches @ 100 yds)', fontsize=11, fontweight='bold')
    ax.set_title(scenario['subtitle'], fontsize=11, style='italic',
                color=scenario['color'])
    ax.grid(True, alpha=0.3, linestyle=':', linewidth=0.5)

# Add educational note at bottom
fig.text(0.5, 0.01,
         'CRITICAL INSIGHT: Velocity SD and precision are RELATED but NOT THE SAME. '
         'Low SD doesn\'t guarantee tight groups (Scenario 2), and high SD can still shoot well at short range (Scenario 3). '
         'You must measure BOTH metrics independently. Never assume one from the other!',
         ha='center', va='bottom', fontsize=11, style='italic',
         bbox=dict(boxstyle='round,pad=0.8', facecolor='lightyellow',
                  edgecolor='black', linewidth=2, alpha=0.9))

# Tight layout
plt.tight_layout(rect=[0, 0.04, 1, 0.98])

# Save the figure
output_path = Path(__file__).parent.parent / 'lessons' / 'static' / 'nb02_plot26_three_types_of_consistency.png'
output_path.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Saved: {output_path}")

# Also display if running interactively
# plt.show()
