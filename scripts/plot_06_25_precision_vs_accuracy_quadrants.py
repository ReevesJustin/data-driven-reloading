#!/usr/bin/env python3
"""
Plot 25: Precision vs Accuracy - Four Quadrants (Notebook 06)
Visual demonstration of the difference between precision and accuracy.

Educational Purpose:
Shows the four combinations of precision (group tightness) and accuracy (hitting aim point):
1. High Precision, High Accuracy (tight group, centered)
2. High Precision, Low Accuracy (tight group, off-center)
3. Low Precision, High Accuracy (scattered shots, centered on average)
4. Low Precision, Low Accuracy (scattered shots, off-center)

This classic visualization helps separate load problems (precision) from zero/wind problems (accuracy).
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from matplotlib.patches import Circle

# Set random seed for reproducibility
np.random.seed(42)

# Create the figure with 2x2 subplots
fig, axes = plt.subplots(2, 2, figsize=(14, 14))
fig.suptitle('Precision vs Accuracy: Understanding the Critical Difference',
             fontsize=18, fontweight='bold', y=0.995)

# Target parameters
target_radius = 5  # inches
aim_point = (0, 0)
n_shots = 20

# Define the four scenarios
scenarios = [
    {
        'title': 'HIGH PRECISION\nHIGH ACCURACY',
        'subtitle': '(The Goal)',
        'precision': 0.4,  # inches (tight group)
        'accuracy_offset': (0, 0),  # centered
        'color': 'darkgreen',
        'description': 'Tight group (precise)\nCentered on aim point (accurate)\n\nThis is what we want:\nGood ammo + Good zero'
    },
    {
        'title': 'HIGH PRECISION\nLOW ACCURACY',
        'subtitle': '(Zero Problem)',
        'precision': 0.4,  # inches (tight group)
        'accuracy_offset': (2.5, 1.5),  # off-center
        'color': 'orange',
        'description': 'Tight group (precise)\nOff aim point (inaccurate)\n\nGood ammo, but:\nScope zero is off OR\nWind shifted the group'
    },
    {
        'title': 'LOW PRECISION\nHIGH ACCURACY',
        'subtitle': '(Load Problem)',
        'precision': 1.2,  # inches (scattered)
        'accuracy_offset': (0, 0),  # centered on average
        'color': 'darkorange',
        'description': 'Scattered shots (imprecise)\nCentered on aim point (accurate)\n\nPoor ammo/rifle, but:\nZero is correct\nGood average wind call'
    },
    {
        'title': 'LOW PRECISION\nLOW ACCURACY',
        'subtitle': '(Multiple Problems)',
        'precision': 1.2,  # inches (scattered)
        'accuracy_offset': (2.5, 1.5),  # off-center
        'color': 'darkred',
        'description': 'Scattered shots (imprecise)\nOff aim point (inaccurate)\n\nMultiple issues:\nPoor ammo/rifle AND\nBad zero AND/OR wind'
    }
]

# Plot each scenario
for idx, (ax, scenario) in enumerate(zip(axes.flat, scenarios)):
    # Generate shots
    # Precision: spread around group center
    shots_x = np.random.normal(0, scenario['precision'], n_shots)
    shots_y = np.random.normal(0, scenario['precision'], n_shots)

    # Accuracy: offset the group center from aim point
    shots_x += scenario['accuracy_offset'][0]
    shots_y += scenario['accuracy_offset'][1]

    # Draw target rings
    for ring_radius in [5, 4, 3, 2, 1]:
        circle = Circle(aim_point, ring_radius, fill=False,
                       edgecolor='lightgray', linewidth=1.5, zorder=1)
        ax.add_patch(circle)

    # Draw aim point (crosshairs)
    ax.plot([aim_point[0]-0.3, aim_point[0]+0.3], [aim_point[1], aim_point[1]],
            'r-', linewidth=3, zorder=5, label='Aim Point')
    ax.plot([aim_point[0], aim_point[0]], [aim_point[1]-0.3, aim_point[1]+0.3],
            'r-', linewidth=3, zorder=5)

    # Draw shots
    ax.scatter(shots_x, shots_y, c='steelblue', s=150, alpha=0.7,
              edgecolors='darkblue', linewidths=2, zorder=10, label='Shots')

    # Calculate and draw group center
    center_x = np.mean(shots_x)
    center_y = np.mean(shots_y)
    ax.scatter([center_x], [center_y], c='gold', s=300, marker='*',
              edgecolors='black', linewidths=2, zorder=15, label='Group Center')

    # Draw line from aim point to group center (if offset)
    if scenario['accuracy_offset'] != (0, 0):
        ax.plot([aim_point[0], center_x], [aim_point[1], center_y],
               'r--', linewidth=2, alpha=0.6, zorder=3)

        # Calculate and annotate accuracy error
        accuracy_error = np.sqrt((center_x - aim_point[0])**2 +
                                 (center_y - aim_point[1])**2)
        mid_x = (aim_point[0] + center_x) / 2
        mid_y = (aim_point[1] + center_y) / 2
        ax.text(mid_x, mid_y + 0.3, f'Error: {accuracy_error:.1f}"',
               fontsize=9, color='red', fontweight='bold',
               bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                        edgecolor='red', alpha=0.8))

    # Calculate mean radius (precision metric)
    distances = np.sqrt((shots_x - center_x)**2 + (shots_y - center_y)**2)
    mean_radius = np.mean(distances)

    # Add title and subtitle
    ax.text(0.5, 1.12, scenario['title'], transform=ax.transAxes,
           fontsize=14, fontweight='bold', ha='center', va='top',
           color=scenario['color'])
    ax.text(0.5, 1.05, scenario['subtitle'], transform=ax.transAxes,
           fontsize=11, style='italic', ha='center', va='top',
           color=scenario['color'])

    # Add description box
    ax.text(0.02, 0.98, scenario['description'], transform=ax.transAxes,
           fontsize=9, verticalalignment='top', horizontalalignment='left',
           bbox=dict(boxstyle='round,pad=0.5', facecolor='wheat', alpha=0.7),
           family='monospace')

    # Add metrics box
    metrics_text = f"Precision (Mean Radius): {mean_radius:.2f}\"\n"
    if scenario['accuracy_offset'] != (0, 0):
        metrics_text += f"Accuracy Error: {accuracy_error:.2f}\""
    else:
        metrics_text += "Accuracy Error: 0.00\""

    ax.text(0.98, 0.02, metrics_text, transform=ax.transAxes,
           fontsize=9, verticalalignment='bottom', horizontalalignment='right',
           bbox=dict(boxstyle='round,pad=0.5', facecolor='lightblue', alpha=0.7),
           family='monospace', fontweight='bold')

    # Set axis properties
    ax.set_xlim(-6, 6)
    ax.set_ylim(-6, 6)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3, linestyle=':', linewidth=0.5)
    ax.set_xlabel('Horizontal (inches)', fontsize=11, fontweight='bold')
    ax.set_ylabel('Vertical (inches)', fontsize=11, fontweight='bold')

    # Legend only on first plot
    if idx == 0:
        ax.legend(loc='upper right', fontsize=9, framealpha=0.9)

# Add educational note at bottom
fig.text(0.5, 0.01,
         'KEY INSIGHT: Precision is when your rifle is zeroed but shots are scattered (load/rifle quality). '
         'Accuracy is like having broken sights—everything shifts off target (zero/wind problem). '
         'These look similar on target but require DIFFERENT solutions. '
         'Don\'t blame your ammunition for accuracy problems—fix your zero first!',
         ha='center', va='bottom', fontsize=11, style='italic',
         bbox=dict(boxstyle='round,pad=0.8', facecolor='lightyellow',
                  edgecolor='black', linewidth=2, alpha=0.9))

# Tight layout
plt.tight_layout(rect=[0, 0.04, 1, 0.98])

# Save the figure
output_path = Path(__file__).parent.parent / 'lessons' / 'static' / 'nb06_plot25_precision_vs_accuracy_quadrants.png'
output_path.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Saved: {output_path}")

# Also display if running interactively
# plt.show()
