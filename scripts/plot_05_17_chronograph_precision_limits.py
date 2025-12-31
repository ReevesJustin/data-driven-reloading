#!/usr/bin/env python3
"""
Plot 17: Chronograph Precision Limits (Notebook 05)
Shows measurement error contribution from chronograph precision.

Educational Purpose:
Demonstrates that chronograph measurement error adds to total variance.
A cheap chronograph with ±10 fps error cannot reliably measure loads with
true 10 fps SD. Need chronograph with ±2-3 fps precision for load development.
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Set random seed for reproducibility
np.random.seed(42)

# Simulation parameters
TRUE_AMMUNITION_SDS = np.array([5, 10, 15, 20, 25, 30])  # fps
CHRONOGRAPH_ERRORS = [2, 5, 10]  # fps (different quality chronographs)
CHRONOGRAPH_LABELS = ['Premium (±2 fps)', 'Mid-grade (±5 fps)', 'Budget (±10 fps)']
CHRONOGRAPH_COLORS = ['green', 'orange', 'red']

# Formula: Measured_SD² = True_SD² + Measurement_error²
# Therefore: Measured_SD = sqrt(True_SD² + Measurement_error²)

# Create the plot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Panel 1: Total measured SD vs true SD
for i, (error, label, color) in enumerate(zip(CHRONOGRAPH_ERRORS, CHRONOGRAPH_LABELS, CHRONOGRAPH_COLORS)):
    measured_sds = np.sqrt(TRUE_AMMUNITION_SDS**2 + error**2)

    ax1.plot(TRUE_AMMUNITION_SDS, measured_sds, 'o-', linewidth=2.5,
             markersize=8, color=color, markeredgecolor='black',
             markeredgewidth=1.5, label=label)

# Add perfect measurement line (no error)
ax1.plot(TRUE_AMMUNITION_SDS, TRUE_AMMUNITION_SDS, '--', linewidth=2,
         color='black', alpha=0.5, label='Perfect chronograph (no error)')

# Labels
ax1.set_xlabel('True Ammunition SD (fps)', fontsize=12, fontweight='bold')
ax1.set_ylabel('Measured Total SD (fps)', fontsize=12, fontweight='bold')
ax1.set_title('How Chronograph Error Inflates Measured SD\n'
              'Measured SD² = True SD² + Measurement Error²',
              fontsize=13, fontweight='bold', pad=15)

ax1.legend(loc='upper left', fontsize=10)
ax1.grid(True, alpha=0.3, linestyle=':', linewidth=0.5)

# Add annotation for key point
ax1.annotate('Budget chrono makes\n10 fps load look like 14 fps!',
             xy=(10, np.sqrt(10**2 + 10**2)),
             xytext=(15, 12),
             fontsize=9, fontweight='bold', color='darkred',
             bbox=dict(boxstyle='round,pad=0.5', facecolor='lightcoral', alpha=0.7),
             arrowprops=dict(arrowstyle='->', color='darkred', lw=2))

# Panel 2: Added error (difference from truth)
for i, (error, label, color) in enumerate(zip(CHRONOGRAPH_ERRORS, CHRONOGRAPH_LABELS, CHRONOGRAPH_COLORS)):
    measured_sds = np.sqrt(TRUE_AMMUNITION_SDS**2 + error**2)
    added_error = measured_sds - TRUE_AMMUNITION_SDS

    ax2.plot(TRUE_AMMUNITION_SDS, added_error, 'o-', linewidth=2.5,
             markersize=8, color=color, markeredgecolor='black',
             markeredgewidth=1.5, label=label)

# Labels
ax2.set_xlabel('True Ammunition SD (fps)', fontsize=12, fontweight='bold')
ax2.set_ylabel('Added Error (fps)', fontsize=12, fontweight='bold')
ax2.set_title('How Much Does Chronograph Error Matter?\n'
              'Added Error = Measured SD - True SD',
              fontsize=13, fontweight='bold', pad=15)

ax2.legend(loc='upper right', fontsize=10)
ax2.grid(True, alpha=0.3, linestyle=':', linewidth=0.5)

# Add annotation for key insight
ax2.annotate('Error matters most\nfor consistent loads!',
             xy=(5, np.sqrt(5**2 + 10**2) - 5),
             xytext=(12, 4.5),
             fontsize=9, fontweight='bold', color='darkred',
             bbox=dict(boxstyle='round,pad=0.5', facecolor='lightcoral', alpha=0.7),
             arrowprops=dict(arrowstyle='->', color='darkred', lw=2))

# Add statistics box
stats_text = (
    f'For 10 fps true SD load:\n'
    f'Premium (±2 fps): Measures {np.sqrt(10**2 + 2**2):.1f} fps\n'
    f'Mid-grade (±5 fps): Measures {np.sqrt(10**2 + 5**2):.1f} fps\n'
    f'Budget (±10 fps): Measures {np.sqrt(10**2 + 10**2):.1f} fps\n'
    f'\n'
    f'Recommendation:\n'
    f'Need ±2-3 fps precision for\n'
    f'reliable load development'
)

ax2.text(0.98, 0.50, stats_text, transform=ax2.transAxes,
         fontsize=9, verticalalignment='bottom', horizontalalignment='right',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.9, edgecolor='black', linewidth=1))

# Overall title
fig.suptitle('Chronograph Precision Limits: Cheap Chronograph Can\'t Measure Consistent Loads\n'
             'Measurement Error Adds to Total Variance - Choose Your Equipment Wisely',
             fontsize=14, fontweight='bold', y=1.02)

# Tight layout
plt.tight_layout()

# Save the figure
output_path = Path(__file__).parent.parent / 'lessons' / 'static' / 'nb05_plot17_chronograph_precision_limits.png'
output_path.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Saved: {output_path}")

# Also display if running interactively
# plt.show()
