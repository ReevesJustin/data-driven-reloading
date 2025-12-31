#!/usr/bin/env python3
"""
Plot 20: Real-World Precision Distribution (Notebook 09)
Shows realistic precision distribution across different rifle classes.

Educational Purpose:
Demonstrates realistic expectations for different rifle and ammunition
combinations. Know your equipment class - don't expect factory rifle to
shoot like custom benchrest.
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Set random seed for reproducibility
np.random.seed(42)

# Simulation parameters - realistic distributions
RIFLE_CLASSES = [
    'Factory rifle\n+ factory ammo',
    'Factory rifle\n+ handloads',
    'Semi-custom\n+ handloads',
    'Full custom\nbenchrest'
]

# Parameters: (mean_moa, std_moa, color)
CLASS_PARAMS = [
    (1.5, 0.4, 'red'),        # Factory + factory
    (1.0, 0.3, 'orange'),     # Factory + handloads
    (0.6, 0.15, 'steelblue'), # Semi-custom + handloads
    (0.25, 0.08, 'green')     # Full custom benchrest
]

N_SAMPLES = 1000  # Samples per class

# Generate data for each class
all_data = []
for mean, std, _ in CLASS_PARAMS:
    # Use log-normal distribution to avoid negative values and get realistic right tail
    # Convert to log-normal parameters
    sigma = np.sqrt(np.log(1 + (std/mean)**2))
    mu = np.log(mean) - 0.5 * sigma**2

    data = np.random.lognormal(mu, sigma, N_SAMPLES)
    all_data.append(data)

# Create the plot
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

# Panel 1: Violin plots
positions = np.arange(len(RIFLE_CLASSES))
parts = ax1.violinplot(all_data, positions=positions, showmeans=True,
                       showextrema=True, widths=0.7)

# Color the violins
for i, pc in enumerate(parts['bodies']):
    pc.set_facecolor(CLASS_PARAMS[i][2])
    pc.set_alpha(0.7)
    pc.set_edgecolor('black')
    pc.set_linewidth(1.5)

# Add percentile markers
for i, data in enumerate(all_data):
    percentiles = np.percentile(data, [50, 90, 95])

    # 50th percentile (median)
    ax1.plot(i, percentiles[0], 'D', color='white', markersize=10,
             markeredgecolor='black', markeredgewidth=2, zorder=10,
             label='50th %ile' if i == 0 else None)

    # 90th percentile
    ax1.plot(i, percentiles[1], '^', color='yellow', markersize=8,
             markeredgecolor='black', markeredgewidth=1.5, zorder=10,
             label='90th %ile' if i == 0 else None)

    # Annotate with values
    ax1.text(i + 0.35, percentiles[0], f'{percentiles[0]:.2f}"',
             fontsize=8, fontweight='bold', va='center')
    ax1.text(i + 0.35, percentiles[1], f'{percentiles[1]:.2f}"',
             fontsize=8, fontweight='bold', va='center')

# Labels
ax1.set_xticks(positions)
ax1.set_xticklabels(RIFLE_CLASSES, fontsize=11, fontweight='bold')
ax1.set_ylabel('Group Size (MOA at 100 yards)', fontsize=12, fontweight='bold')
ax1.set_title('Real-World Precision Distribution by Equipment Class\n'
              'Know Your Equipment - Set Realistic Expectations',
              fontsize=14, fontweight='bold', pad=15)

ax1.legend(loc='upper right', fontsize=10)
ax1.grid(True, alpha=0.3, linestyle=':', linewidth=0.5, axis='y')
ax1.set_ylim([0, 3.5])

# Panel 2: Overlapping histograms
bins = np.linspace(0, 3.5, 50)

for i, (data, (mean, std, color)) in enumerate(zip(all_data, CLASS_PARAMS)):
    ax2.hist(data, bins=bins, alpha=0.5, color=color, edgecolor='black',
             linewidth=0.5, label=RIFLE_CLASSES[i].replace('\n', ' '))

    # Add vertical line at mean
    ax2.axvline(np.mean(data), color=color, linestyle='--',
                linewidth=2, alpha=0.8)

# Labels
ax2.set_xlabel('Group Size (MOA at 100 yards)', fontsize=12, fontweight='bold')
ax2.set_ylabel('Frequency', fontsize=12, fontweight='bold')
ax2.set_title('Distribution Overlap: Understanding Your Rifle\'s Performance Range',
              fontsize=13, fontweight='bold', pad=15)

ax2.legend(loc='upper right', fontsize=10)
ax2.grid(True, alpha=0.3, linestyle=':', linewidth=0.5)

# Add statistics annotation
stats_text = 'Summary Statistics:\n\n'
for i, (data, rifle_class) in enumerate(zip(all_data, RIFLE_CLASSES)):
    mean_val = np.mean(data)
    p50 = np.percentile(data, 50)
    p90 = np.percentile(data, 90)
    p95 = np.percentile(data, 95)

    class_name = rifle_class.replace('\n', ' ')
    stats_text += f'{class_name}:\n'
    stats_text += f'  Mean: {mean_val:.2f} MOA\n'
    stats_text += f'  50th: {p50:.2f}, 90th: {p90:.2f}, 95th: {p95:.2f}\n'

stats_text += '\nLesson: Don\'t chase unrealistic\ngoals for your equipment class!'

ax2.text(0.98, 0.70, stats_text, transform=ax2.transAxes,
         fontsize=8.5, verticalalignment='top', horizontalalignment='right',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.9, edgecolor='black', linewidth=1),
         family='monospace')

# Overall title
fig.suptitle('Real-World Precision by Equipment Class: Set Realistic Expectations\n'
             'Don\'t Expect Factory Rifle to Shoot Like Custom Benchrest',
             fontsize=14, fontweight='bold', y=0.995)

# Tight layout
plt.tight_layout(rect=[0, 0, 1, 0.985])

# Save the figure
output_path = Path(__file__).parent.parent / 'lessons' / 'static' / 'nb09_plot20_real_world_precision_distribution.png'
output_path.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Saved: {output_path}")

# Also display if running interactively
# plt.show()
