#!/usr/bin/env python3
"""
Plot 2: Mean Radius vs Extreme Spread Stability (Notebook 01)
Demonstrates that mean radius stabilizes while extreme spread grows with sample size.

Educational Purpose:
Shows why extreme spread (ES) is an unreliable metric that grows with sample size,
while mean radius (MR) converges to the true rifle capability. Helps readers
understand that ES depends more on luck and sample size than on rifle accuracy.
Multiple simulation runs show consistency of this pattern.
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Set random seed for reproducibility
np.random.seed(42)

# Simulation parameters
TRUE_SIGMA = 0.75  # True rifle capability in MOA (sigma for 2D normal)
TRUE_MR = TRUE_SIGMA * np.sqrt(np.pi / 2)  # Theoretical mean radius
MAX_SHOTS = 50
N_SIMULATIONS = 20  # Number of simulation runs to show

# Function to calculate extreme spread
def calculate_es(x, y):
    """Calculate extreme spread (maximum distance between any two shots)."""
    n = len(x)
    max_dist = 0
    for i in range(n):
        for j in range(i + 1, n):
            dist = np.sqrt((x[i] - x[j])**2 + (y[i] - y[j])**2)
            max_dist = max(max_dist, dist)
    return max_dist

# Function to calculate mean radius
def calculate_mr(x, y):
    """Calculate mean radius (average distance from center)."""
    radii = np.sqrt(x**2 + y**2)
    return np.mean(radii)

# Run multiple simulations
all_es_curves = []
all_mr_curves = []

for sim in range(N_SIMULATIONS):
    # Generate shots from 2D normal distribution
    x = np.random.normal(0, TRUE_SIGMA, MAX_SHOTS)
    y = np.random.normal(0, TRUE_SIGMA, MAX_SHOTS)

    # Calculate running ES and MR
    es_values = []
    mr_values = []

    for n in range(1, MAX_SHOTS + 1):
        es_values.append(calculate_es(x[:n], y[:n]))
        mr_values.append(calculate_mr(x[:n], y[:n]))

    all_es_curves.append(es_values)
    all_mr_curves.append(mr_values)

# Convert to arrays
all_es_curves = np.array(all_es_curves)
all_mr_curves = np.array(all_mr_curves)
shot_numbers = np.arange(1, MAX_SHOTS + 1)

# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot background simulations (lighter colors)
for i in range(N_SIMULATIONS):
    if i == 0:
        # Highlight one simulation
        ax.plot(shot_numbers, all_es_curves[i], color='coral',
                linewidth=2, alpha=0.9, label='Extreme Spread (ES) - Sample Run')
        ax.plot(shot_numbers, all_mr_curves[i], color='steelblue',
                linewidth=2, alpha=0.9, label='Mean Radius (MR) - Sample Run')
    else:
        # Other simulations in background
        ax.plot(shot_numbers, all_es_curves[i], color='coral',
                linewidth=0.5, alpha=0.2)
        ax.plot(shot_numbers, all_mr_curves[i], color='steelblue',
                linewidth=0.5, alpha=0.2)

# Add theoretical mean radius line
ax.axhline(TRUE_MR, color='darkblue', linestyle='--', linewidth=2,
           label=f'True Mean Radius: {TRUE_MR:.2f} MOA', alpha=0.8)

# Add trend lines (averages across all simulations)
mean_es = np.mean(all_es_curves, axis=0)
mean_mr = np.mean(all_mr_curves, axis=0)

ax.plot(shot_numbers, mean_es, color='darkred', linestyle='-', linewidth=2.5,
        label='Average ES (across all runs)', alpha=0.7)
ax.plot(shot_numbers, mean_mr, color='darkblue', linestyle='-', linewidth=2.5,
        label='Average MR (across all runs)', alpha=0.7)

# Labels and title
ax.set_xlabel('Number of Shots', fontsize=12, fontweight='bold')
ax.set_ylabel('Group Size (MOA)', fontsize=12, fontweight='bold')
ax.set_title('Mean Radius Stabilizes, Extreme Spread Grows\n'
             f'Simulation of {N_SIMULATIONS} strings from true {TRUE_SIGMA*2:.1f} MOA rifle (σ = {TRUE_SIGMA} MOA)',
             fontsize=14, fontweight='bold', pad=20)

# Set limits
ax.set_xlim(1, MAX_SHOTS)
ax.set_ylim(0, max(np.max(all_es_curves), 5))

# Grid
ax.grid(True, alpha=0.3, linestyle=':', linewidth=0.5)

# Legend
ax.legend(loc='upper left', fontsize=9, framealpha=0.9)

# Add annotations
ax.annotate('ES keeps growing\nwith more shots',
           xy=(40, mean_es[39]), xytext=(25, mean_es[39] + 0.8),
           fontsize=9, ha='center',
           arrowprops=dict(arrowstyle='->', color='coral', lw=2),
           bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

ax.annotate('MR converges to\ntrue capability',
           xy=(40, mean_mr[39]), xytext=(25, mean_mr[39] - 0.5),
           fontsize=9, ha='center',
           arrowprops=dict(arrowstyle='->', color='steelblue', lw=2),
           bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# Add statistics box
es_final_mean = mean_es[-1]
mr_final_mean = mean_mr[-1]
es_growth = (es_final_mean - mean_es[9]) / mean_es[9] * 100  # Growth from shot 10 to 50
mr_stability = abs(mr_final_mean - TRUE_MR) / TRUE_MR * 100  # Error at shot 50

stats_text = (
    f'At {MAX_SHOTS} shots:\n'
    f'• Average ES: {es_final_mean:.2f} MOA\n'
    f'  (grew {es_growth:.0f}% from shot 10)\n'
    f'• Average MR: {mr_final_mean:.2f} MOA\n'
    f'  (within {mr_stability:.1f}% of true value)\n\n'
    f'Key Insight:\n'
    f'ES is unreliable - it depends on\n'
    f'sample size and luck.\n\n'
    f'MR converges to true rifle capability\n'
    f'and is a much better metric for\n'
    f'comparing loads or rifles.'
)

ax.text(0.98, 0.60, stats_text, transform=ax.transAxes,
        fontsize=8, verticalalignment='top', horizontalalignment='right',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.85, edgecolor='black', linewidth=1))

# Add note at bottom
note_text = (
    'Note: Light lines show individual simulation runs. Dark lines show averages.\n'
    'This pattern is consistent: ES always grows, MR always stabilizes.'
)

ax.text(0.5, 0.02, note_text, transform=ax.transAxes,
        fontsize=8, verticalalignment='bottom', horizontalalignment='center',
        style='italic',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.5))

# Tight layout
plt.tight_layout()

# Save the figure
output_path = Path(__file__).parent.parent / 'lessons' / 'static' / 'nb01_plot02_mean_radius_vs_extreme_spread.png'
output_path.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Saved: {output_path}")

# Also display if running interactively
# plt.show()
