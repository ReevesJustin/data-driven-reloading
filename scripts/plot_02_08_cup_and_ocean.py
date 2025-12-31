#!/usr/bin/env python3
"""
Plot 8: The Cup and the Ocean (Notebook 02)
Demonstrates sample convergence to population truth.

Educational Purpose:
Shows how running average and SD converge toward true population
values as sample size increases. This is the foundational "cup and ocean" concept.
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Set random seed for reproducibility
np.random.seed(42)

# Population parameters (the "ocean")
TRUE_MEAN = 2850  # fps
TRUE_SD = 15  # fps
N_SHOTS = 100

# Generate shots from population
shots = np.random.normal(TRUE_MEAN, TRUE_SD, N_SHOTS)

# Calculate running statistics
running_mean = np.cumsum(shots) / np.arange(1, N_SHOTS + 1)
running_sd = np.array([np.std(shots[:i+1], ddof=1) for i in range(N_SHOTS)])

# Create figure with two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

# Plot 1: Running Mean
ax1.plot(range(1, N_SHOTS + 1), running_mean, 'steelblue', linewidth=2, label='Running Average')
ax1.axhline(TRUE_MEAN, color='red', linestyle='--', linewidth=2, label=f'True Mean: {TRUE_MEAN} fps')
ax1.fill_between(range(1, N_SHOTS + 1),
                  TRUE_MEAN - 5, TRUE_MEAN + 5,
                  alpha=0.2, color='red', label='±5 fps band')
ax1.set_xlabel('Number of Shots', fontsize=12, fontweight='bold')
ax1.set_ylabel('Average Velocity (fps)', fontsize=12, fontweight='bold')
ax1.set_title('The Cup and the Ocean: Average Velocity Converges Quickly',
              fontsize=14, fontweight='bold', pad=15)
ax1.legend(loc='upper right', fontsize=10)
ax1.grid(True, alpha=0.3, linestyle=':', linewidth=0.5)
ax1.set_xlim(1, N_SHOTS)

# Add annotation
ax1.annotate('Within ±5 fps\nby shot 15',
             xy=(15, running_mean[14]), xytext=(30, TRUE_MEAN + 7),
             arrowprops=dict(arrowstyle='->', color='darkgreen', lw=2),
             fontsize=10, color='darkgreen', fontweight='bold',
             bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))

# Plot 2: Running SD
ax2.plot(range(1, N_SHOTS + 1), running_sd, 'steelblue', linewidth=2, label='Running SD')
ax2.axhline(TRUE_SD, color='red', linestyle='--', linewidth=2, label=f'True SD: {TRUE_SD} fps')
ax2.fill_between(range(1, N_SHOTS + 1),
                  TRUE_SD - 2, TRUE_SD + 2,
                  alpha=0.2, color='red', label='±2 fps band')
ax2.set_xlabel('Number of Shots', fontsize=12, fontweight='bold')
ax2.set_ylabel('Standard Deviation (fps)', fontsize=12, fontweight='bold')
ax2.set_title('Standard Deviation Converges Slowly - Needs Many Shots',
              fontsize=14, fontweight='bold', pad=15)
ax2.legend(loc='upper right', fontsize=10)
ax2.grid(True, alpha=0.3, linestyle=':', linewidth=0.5)
ax2.set_xlim(1, N_SHOTS)
ax2.set_ylim(0, 30)

# Add annotation
ax2.annotate('Still varying\nafter 30 shots',
             xy=(30, running_sd[29]), xytext=(50, 25),
             arrowprops=dict(arrowstyle='->', color='darkorange', lw=2),
             fontsize=10, color='darkorange', fontweight='bold',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.7))

# Add main insight text
fig.text(0.5, 0.02,
         'Key Insight: Average velocity stabilizes with ~10-15 shots. SD requires 30+ shots to be reliable.',
         ha='center', fontsize=11, fontweight='bold', style='italic',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8, edgecolor='orange', linewidth=2))

# Tight layout
plt.tight_layout(rect=[0, 0.04, 1, 1])

# Save the figure
output_path = Path(__file__).parent.parent / 'lessons' / 'static' / 'nb02_plot08_cup_and_ocean.png'
output_path.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Saved: {output_path}")
