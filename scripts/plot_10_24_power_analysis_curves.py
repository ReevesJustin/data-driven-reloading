#!/usr/bin/env python3
"""
Plot 24: Detection Calculator (Power Analysis Curves) (Notebook 10)
Shows sample size needed to detect various effect sizes with 80% confidence.

Educational Purpose:
Helps readers understand how many shots they need to reliably detect differences
between loads. Uses accessible language ("detection" instead of "power") to make
statistical concepts approachable. Shows that small differences require many more
shots to detect reliably.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from pathlib import Path

# Set random seed for reproducibility
np.random.seed(42)

# Parameters
sample_sizes = np.array([5, 10, 15, 20, 30, 40, 50, 75, 100])
baseline_sd = 12  # fps, typical velocity SD
alpha = 0.05  # Significance level (5% false alarm rate)

# Effect sizes to test (SD difference from baseline)
effect_sizes = {
    'Small (5 fps)': 5,
    'Medium (10 fps)': 10,
    'Large (20 fps)': 20
}

# Calculate statistical power for each effect size
# Power = probability of detecting a true difference
# Using two-sample t-test power calculation

def calculate_power(n, effect_size, baseline_sd, alpha=0.05):
    """
    Calculate statistical power for a two-sample t-test.

    Parameters:
    n: sample size per group
    effect_size: difference in means (fps)
    baseline_sd: standard deviation (fps)
    alpha: significance level
    """
    # Cohen's d (standardized effect size)
    d = effect_size / baseline_sd

    # Non-centrality parameter for t-test
    # For two-sample test with equal n: ncp = d * sqrt(n/2)
    ncp = d * np.sqrt(n / 2)

    # Critical value for two-tailed test
    df = 2 * n - 2
    t_critical = stats.t.ppf(1 - alpha/2, df)

    # Power = probability of rejecting null when alternative is true
    # This is 1 - beta (Type II error rate)
    power = 1 - stats.nct.cdf(t_critical, df, ncp) + stats.nct.cdf(-t_critical, df, ncp)

    return power * 100  # Convert to percentage

# Calculate power curves
power_curves = {}
for effect_name, effect_size in effect_sizes.items():
    power_curves[effect_name] = [
        calculate_power(n, effect_size, baseline_sd, alpha)
        for n in sample_sizes
    ]

# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot power curves
colors = {'Small (5 fps)': 'coral', 'Medium (10 fps)': 'steelblue', 'Large (20 fps)': 'green'}
markers = {'Small (5 fps)': 'o', 'Medium (10 fps)': 's', 'Large (20 fps)': '^'}

for effect_name in effect_sizes.keys():
    ax.plot(sample_sizes, power_curves[effect_name],
            marker=markers[effect_name], markersize=8,
            linewidth=2.5, label=effect_name,
            color=colors[effect_name], alpha=0.8)

# Add 80% power threshold line
ax.axhline(80, color='red', linestyle='--', linewidth=2,
           label='80% Detection Threshold (Standard Goal)', alpha=0.7)

# Shade the "good detection" region
ax.axhspan(80, 100, alpha=0.1, color='green', label='High Detection Zone')

# Labels and title
ax.set_xlabel('Sample Size Per Load (Number of Shots)', fontsize=12, fontweight='bold')
ax.set_ylabel('Detection Probability (%)', fontsize=12, fontweight='bold')
ax.set_title('Detection Calculator: How Many Shots to Reliably Find Differences?\n'
             'Based on Baseline SD = 12 fps (typical for precision rifle)',
             fontsize=14, fontweight='bold', pad=20)

# Set limits
ax.set_xlim(0, 105)
ax.set_ylim(0, 105)

# Grid
ax.grid(True, alpha=0.3, linestyle=':', linewidth=0.5)

# Legend
ax.legend(loc='lower right', bbox_to_anchor=(1.0, 0.1), fontsize=10, framealpha=0.9)

# Annotate key points (sample size needed for 80% power)
def find_n_for_power(sample_sizes, powers, target_power=80):
    """Find sample size needed to achieve target power."""
    for i, power in enumerate(powers):
        if power >= target_power:
            return sample_sizes[i]
    return None

# Add annotations for each curve
for effect_name, color in colors.items():
    n_needed = find_n_for_power(sample_sizes, power_curves[effect_name])
    if n_needed:
        power_at_n = power_curves[effect_name][list(sample_sizes).index(n_needed)]
        ax.annotate(f'n = {n_needed}',
                   xy=(n_needed, power_at_n),
                   xytext=(n_needed + 10, power_at_n - 10),
                   fontsize=9, ha='left',
                   arrowprops=dict(arrowstyle='->', color=color, lw=1.5),
                   bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

# Add statistics box
stats_text = (
    'Reading this chart:\n'
    '• Higher curves = easier to detect\n'
    '• Larger differences need fewer shots\n'
    '• Small differences (5 fps) need 75+ shots\n'
    '  to reliably detect at 80% confidence\n\n'
    'Example:\n'
    'To detect a 10 fps SD improvement\n'
    'with 80% confidence, you need\n'
    'about 30 shots per load.\n\n'
    'Rule of thumb:\n'
    '• Quick check: 10-20 shots\n'
    '• Serious testing: 30-50 shots\n'
    '• Publication: 100+ shots'
)

ax.text(0.98, 0.65, stats_text, transform=ax.transAxes,
        fontsize=8.5, verticalalignment='top', horizontalalignment='right',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.9, edgecolor='black', linewidth=1))

# Add note about Type II error
note_text = (
    'Note: "Detection probability" = chance of finding a real difference when it exists.\n'
    'Lower curves mean higher risk of missing a real improvement (false negative).\n'
    '80% is the standard threshold: accepts 20% risk of missing a real effect.'
)

ax.text(0.5, 0.02, note_text, transform=ax.transAxes,
        fontsize=8, verticalalignment='bottom', horizontalalignment='center',
        style='italic',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.5))

# Tight layout
plt.tight_layout()

# Save the figure
output_path = Path(__file__).parent.parent / 'lessons' / 'static' / 'nb10_plot24_power_analysis_curves.png'
output_path.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Saved: {output_path}")

# Also display if running interactively
# plt.show()
