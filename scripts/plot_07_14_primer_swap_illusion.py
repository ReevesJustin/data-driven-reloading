#!/usr/bin/env python3
"""
Plot 14: Primer Swap Illusion (Notebook 07)
Shows how small samples create false differences between identical primers.

Educational Purpose:
Demonstrates that testing primers with small samples will show apparent SD
differences even when primers are identical. About 20% of small trials show
"amazing" sub-10 fps SD by pure luck. Large samples reveal the truth.
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Set random seed for reproducibility
np.random.seed(42)

# Simulation parameters
TRUE_SD = 15  # fps (both primers are identical)
PRIMER_NAMES = ['CCI', 'Federal']
SMALL_SAMPLE_SIZE = 10
LARGE_SAMPLE_SIZE = 50
N_SMALL_TRIALS = 50  # Many trials to show distribution

# Function to calculate sample SD
def calculate_sample_sd(true_sd, sample_size):
    """Simulate sample standard deviation."""
    samples = np.random.normal(0, true_sd, sample_size)
    return np.std(samples, ddof=1)

# Create figure with multiple panels
fig = plt.figure(figsize=(14, 10))

# Panel 1: Distribution of measured SDs from small samples
ax1 = plt.subplot(2, 2, (1, 2))

# Simulate many small-sample trials
cci_small_sds = []
fed_small_sds = []

for trial in range(N_SMALL_TRIALS):
    np.random.seed(42 + trial * 2)
    cci_sd = calculate_sample_sd(TRUE_SD, SMALL_SAMPLE_SIZE)
    cci_small_sds.append(cci_sd)

    np.random.seed(42 + trial * 2 + 1)
    fed_sd = calculate_sample_sd(TRUE_SD, SMALL_SAMPLE_SIZE)
    fed_small_sds.append(fed_sd)

cci_small_sds = np.array(cci_small_sds)
fed_small_sds = np.array(fed_small_sds)

# Plot histograms
bins = np.linspace(0, 30, 31)
ax1.hist(cci_small_sds, bins=bins, alpha=0.6, color='red', edgecolor='darkred',
         linewidth=1.5, label=f'CCI ({N_SMALL_TRIALS} trials)')
ax1.hist(fed_small_sds, bins=bins, alpha=0.6, color='blue', edgecolor='darkblue',
         linewidth=1.5, label=f'Federal ({N_SMALL_TRIALS} trials)')

# Add true SD line
ax1.axvline(TRUE_SD, color='black', linestyle='--', linewidth=2.5,
            label=f'True SD: {TRUE_SD} fps (both primers)')

# Highlight "amazing" results
amazing_threshold = 10
n_amazing_cci = np.sum(cci_small_sds < amazing_threshold)
n_amazing_fed = np.sum(fed_small_sds < amazing_threshold)

ax1.axvline(amazing_threshold, color='gold', linestyle=':', linewidth=2,
            label=f'"Amazing" threshold (<{amazing_threshold} fps)')

# Labels
ax1.set_xlabel('Measured SD (fps)', fontsize=12, fontweight='bold')
ax1.set_ylabel('Frequency', fontsize=12, fontweight='bold')
ax1.set_title(f'Small Sample Illusion: {SMALL_SAMPLE_SIZE} Shots Per Primer\n'
              f'Same Primers ({TRUE_SD} fps SD) Appear Different Due to Random Variation',
              fontsize=13, fontweight='bold', pad=15)

# Stats annotation
stats_text = (
    f'Sample size: {SMALL_SAMPLE_SIZE} shots\n'
    f'True SD (both): {TRUE_SD} fps\n'
    f'\n'
    f'"Amazing" results (<{amazing_threshold} fps):\n'
    f'CCI: {n_amazing_cci}/{N_SMALL_TRIALS} = {n_amazing_cci/N_SMALL_TRIALS*100:.0f}%\n'
    f'Federal: {n_amazing_fed}/{N_SMALL_TRIALS} = {n_amazing_fed/N_SMALL_TRIALS*100:.0f}%\n'
    f'\n'
    f'~20% of trials look "amazing"\n'
    f'by pure luck!'
)

ax1.text(0.98, 0.97, stats_text, transform=ax1.transAxes,
         fontsize=9, verticalalignment='top', horizontalalignment='right',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.9, edgecolor='black', linewidth=1))

ax1.legend(loc='upper left', fontsize=10)
ax1.grid(True, alpha=0.3, linestyle=':', linewidth=0.5)

# Panel 2: Example "lucky" small sample
ax2 = plt.subplot(2, 2, 3)

# Find a trial with big apparent difference
differences = np.abs(cci_small_sds - fed_small_sds)
lucky_trial_idx = np.argmax(differences)

np.random.seed(42 + lucky_trial_idx * 2)
cci_shots = np.random.normal(2800, TRUE_SD, SMALL_SAMPLE_SIZE)
np.random.seed(42 + lucky_trial_idx * 2 + 1)
fed_shots = np.random.normal(2800, TRUE_SD, SMALL_SAMPLE_SIZE)

# Violin plots
parts = ax2.violinplot([cci_shots, fed_shots], positions=[1, 2],
                       showmeans=True, showextrema=True, widths=0.6)

# Color the violins
for i, pc in enumerate(parts['bodies']):
    pc.set_facecolor(['red', 'blue'][i])
    pc.set_alpha(0.6)
    pc.set_edgecolor('black')
    pc.set_linewidth(1.5)

# Add individual points
ax2.scatter(np.ones(SMALL_SAMPLE_SIZE) + np.random.normal(0, 0.04, SMALL_SAMPLE_SIZE),
            cci_shots, alpha=0.6, color='red', s=50, edgecolors='darkred', linewidths=1)
ax2.scatter(2 * np.ones(SMALL_SAMPLE_SIZE) + np.random.normal(0, 0.04, SMALL_SAMPLE_SIZE),
            fed_shots, alpha=0.6, color='blue', s=50, edgecolors='darkblue', linewidths=1)

# Labels
ax2.set_xticks([1, 2])
ax2.set_xticklabels(['CCI', 'Federal'], fontsize=11, fontweight='bold')
ax2.set_ylabel('Velocity (fps)', fontsize=11, fontweight='bold')
ax2.set_title(f'Lucky Small Sample: Looks Different!\n'
              f'CCI SD: {cci_small_sds[lucky_trial_idx]:.1f} fps, '
              f'Fed SD: {fed_small_sds[lucky_trial_idx]:.1f} fps',
              fontsize=11, fontweight='bold')

ax2.grid(True, alpha=0.3, linestyle=':', linewidth=0.5, axis='y')

# Panel 3: Large sample showing truth
ax3 = plt.subplot(2, 2, 4)

# Generate large samples
np.random.seed(1000)
cci_large = np.random.normal(2800, TRUE_SD, LARGE_SAMPLE_SIZE)
np.random.seed(1001)
fed_large = np.random.normal(2800, TRUE_SD, LARGE_SAMPLE_SIZE)

cci_large_sd = np.std(cci_large, ddof=1)
fed_large_sd = np.std(fed_large, ddof=1)

# Violin plots
parts = ax3.violinplot([cci_large, fed_large], positions=[1, 2],
                       showmeans=True, showextrema=True, widths=0.6)

# Color the violins
for i, pc in enumerate(parts['bodies']):
    pc.set_facecolor(['red', 'blue'][i])
    pc.set_alpha(0.6)
    pc.set_edgecolor('black')
    pc.set_linewidth(1.5)

# Add individual points (subset for visibility)
subset_size = 30
ax3.scatter(np.ones(subset_size) + np.random.normal(0, 0.04, subset_size),
            cci_large[:subset_size], alpha=0.4, color='red', s=30,
            edgecolors='darkred', linewidths=0.5)
ax3.scatter(2 * np.ones(subset_size) + np.random.normal(0, 0.04, subset_size),
            fed_large[:subset_size], alpha=0.4, color='blue', s=30,
            edgecolors='darkblue', linewidths=0.5)

# Labels
ax3.set_xticks([1, 2])
ax3.set_xticklabels(['CCI', 'Federal'], fontsize=11, fontweight='bold')
ax3.set_ylabel('Velocity (fps)', fontsize=11, fontweight='bold')
ax3.set_title(f'Large Sample Reality: Same!\n'
              f'CCI SD: {cci_large_sd:.1f} fps, '
              f'Fed SD: {fed_large_sd:.1f} fps ({LARGE_SAMPLE_SIZE} shots each)',
              fontsize=11, fontweight='bold')

ax3.grid(True, alpha=0.3, linestyle=':', linewidth=0.5, axis='y')

# Overall title
fig.suptitle('Primer Swap Illusion: Same Primers, Different Conclusions from Different Sample Sizes\n'
             'Small Samples Create False Differences, Large Samples Reveal Truth',
             fontsize=14, fontweight='bold', y=0.98)

# Add explanatory text
explanation = (
    f'Both primers truly identical: {TRUE_SD} fps SD\n'
    f'\n'
    f'Small sample ({SMALL_SAMPLE_SIZE} shots): Often looks different\n'
    f'Large sample ({LARGE_SAMPLE_SIZE} shots): Converges to truth\n'
    f'\n'
    f'Don\'t trust primer comparisons with <30 shots!'
)

fig.text(0.99, 0.01, explanation, fontsize=8.5,
         verticalalignment='bottom', horizontalalignment='right',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.9, edgecolor='black', linewidth=1))

# Tight layout
plt.tight_layout(rect=[0, 0.03, 1, 0.96])

# Save the figure
output_path = Path(__file__).parent.parent / 'lessons' / 'static' / 'nb07_plot14_primer_swap_illusion.png'
output_path.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Saved: {output_path}")

# Also display if running interactively
# plt.show()
