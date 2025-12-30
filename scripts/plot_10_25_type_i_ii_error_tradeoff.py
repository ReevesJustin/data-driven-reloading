#!/usr/bin/env python3
"""
Plot 25: Type I vs Type II Error Tradeoff (Notebook 10)
Visual demonstration of the relationship between sample size, false alarms, and missed detections.

Educational Purpose:
Shows how sample size affects statistical power:
- Type I errors (false alarms) stay constant regardless of sample size
- Type II errors (missed detections) decrease dramatically with larger samples
- Small samples can't detect real differences, even with strict criteria
- Proper sample sizes are essential for reliable conclusions

This reinforces why you need 30+ shots, not stricter p-values with 5 shots.
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from scipy import stats

# Set random seed for reproducibility
np.random.seed(42)

# Create the figure
fig = plt.figure(figsize=(16, 10))
gs = fig.add_gridspec(2, 2, hspace=0.3, wspace=0.3)

# Main title
fig.suptitle('The Error Tradeoff: Why Sample Size Matters More Than Strict Criteria',
             fontsize=18, fontweight='bold', y=0.98)

# Simulation parameters
true_sd_identical = 15  # fps, both loads identical
true_sd_load_a = 15  # fps
true_sd_load_b = 10  # fps, actually better
sample_sizes = [5, 10, 20, 30, 50]
n_simulations = 1000
alpha = 0.05  # significance level

# Colors
color_false_alarm = 'red'
color_missed_opportunity = 'orange'
color_correct = 'darkgreen'

# --- Plot 1: False Alarm Rate (Type I Error) ---
ax1 = fig.add_subplot(gs[0, 0])

false_alarm_rates = []
for n in sample_sizes:
    false_alarms = 0
    for _ in range(n_simulations):
        # Generate two samples from IDENTICAL loads
        sample_a = np.random.normal(2850, true_sd_identical, n)
        sample_b = np.random.normal(2850, true_sd_identical, n)

        # Test if they're "different"
        _, p_value = stats.ttest_ind(sample_a, sample_b)
        if p_value < alpha:
            false_alarms += 1

    false_alarm_rates.append(false_alarms / n_simulations * 100)

ax1.bar(sample_sizes, false_alarm_rates, color=color_false_alarm, alpha=0.7,
        edgecolor='darkred', linewidth=2)
ax1.axhline(alpha * 100, color='black', linestyle='--', linewidth=2,
           label=f'Expected α = {alpha*100:.0f}%')
ax1.set_xlabel('Sample Size (shots per load)', fontsize=12, fontweight='bold')
ax1.set_ylabel('False Alarm Rate (%)', fontsize=12, fontweight='bold')
ax1.set_title('Type I Errors: False Alarms with IDENTICAL Loads\n(Declaring difference when none exists)',
             fontsize=13, fontweight='bold', color=color_false_alarm)
ax1.set_ylim(0, 10)
ax1.grid(True, alpha=0.3, linestyle=':', linewidth=0.5)
ax1.legend(fontsize=10)

# Add annotation
ax1.text(0.95, 0.95,
         'CRITICAL INSIGHT:\n\n'
         'Sample size does NOT reduce\n'
         'false alarms!\n\n'
         'False alarm rate stays at ~5%\n'
         'regardless of sample size.\n\n'
         'α is constant (by definition)',
         transform=ax1.transAxes, fontsize=10,
         verticalalignment='top', horizontalalignment='right',
         bbox=dict(boxstyle='round,pad=0.8', facecolor='wheat', alpha=0.8),
         fontweight='bold')

# --- Plot 2: Detection Rate (1 - Type II Error) = Statistical Power ---
ax2 = fig.add_subplot(gs[0, 1])

detection_rates = []
for n in sample_sizes:
    detections = 0
    for _ in range(n_simulations):
        # Generate two samples from DIFFERENT loads (B is actually better)
        sample_a = np.random.normal(2850, true_sd_load_a, n)
        sample_b = np.random.normal(2850, true_sd_load_b, n)

        # Test if we can detect the difference
        # Use variance test (F-test) since we're testing SD difference
        var_a = np.var(sample_a, ddof=1)
        var_b = np.var(sample_b, ddof=1)
        f_stat = var_a / var_b
        df1 = n - 1
        df2 = n - 1
        p_value = 2 * min(stats.f.cdf(f_stat, df1, df2),
                         1 - stats.f.cdf(f_stat, df1, df2))

        if p_value < alpha:
            detections += 1

    detection_rates.append(detections / n_simulations * 100)

ax2.bar(sample_sizes, detection_rates, color=color_correct, alpha=0.7,
        edgecolor='darkgreen', linewidth=2)
ax2.set_xlabel('Sample Size (shots per load)', fontsize=12, fontweight='bold')
ax2.set_ylabel('Detection Rate / Power (%)', fontsize=12, fontweight='bold')
ax2.set_title('Statistical Power: Detecting REAL Differences\n(15 fps SD vs 10 fps SD)',
             fontsize=13, fontweight='bold', color=color_correct)
ax2.set_ylim(0, 100)
ax2.grid(True, alpha=0.3, linestyle=':', linewidth=0.5)

# Add annotation
ax2.text(0.95, 0.95,
         'GAME CHANGER:\n\n'
         'Sample size DRAMATICALLY\n'
         'increases detection!\n\n'
         '5 shots: ~10% power\n'
         '30 shots: ~60% power\n'
         '50 shots: ~85% power\n\n'
         'Larger samples find\n'
         'real differences!',
         transform=ax2.transAxes, fontsize=10,
         verticalalignment='top', horizontalalignment='right',
         bbox=dict(boxstyle='round,pad=0.8', facecolor='lightgreen', alpha=0.8),
         fontweight='bold')

# --- Plot 3: Combined View (Stacked Outcomes) ---
ax3 = fig.add_subplot(gs[1, :])

# For each sample size, show the breakdown of outcomes
width = 0.35
x_pos = np.arange(len(sample_sizes))

# Missed opportunities (Type II errors)
missed_rates = [100 - rate for rate in detection_rates]

# Create stacked bars
p1 = ax3.bar(x_pos, detection_rates, width, label='Correct Detections (Power)',
            color=color_correct, alpha=0.8, edgecolor='black', linewidth=1.5)
p2 = ax3.bar(x_pos, missed_rates, width, bottom=detection_rates,
            label='Missed Opportunities (Type II Errors)',
            color=color_missed_opportunity, alpha=0.8, edgecolor='black', linewidth=1.5)

# Add false alarm rate as separate bars
p3 = ax3.bar(x_pos + width, false_alarm_rates, width,
            label='False Alarms (Type I Errors)',
            color=color_false_alarm, alpha=0.8, edgecolor='black', linewidth=1.5)

ax3.set_xlabel('Sample Size (shots per load)', fontsize=13, fontweight='bold')
ax3.set_ylabel('Percentage (%)', fontsize=13, fontweight='bold')
ax3.set_title('The Complete Picture: How Sample Size Affects Your Conclusions',
             fontsize=14, fontweight='bold')
ax3.set_xticks(x_pos + width / 2)
ax3.set_xticklabels([f'{n} shots' for n in sample_sizes])
ax3.set_ylim(0, 110)
ax3.legend(loc='upper left', fontsize=11, framealpha=0.95)
ax3.grid(True, alpha=0.3, linestyle=':', linewidth=0.5, axis='y')

# Add annotations for key sample sizes
for i, n in enumerate(sample_sizes):
    if n == 5:
        ax3.text(i, detection_rates[i]/2, f'{detection_rates[i]:.0f}%\nDetected',
                ha='center', va='center', fontsize=9, fontweight='bold', color='white')
        ax3.text(i, detection_rates[i] + missed_rates[i]/2,
                f'{missed_rates[i]:.0f}%\nMissed!',
                ha='center', va='center', fontsize=9, fontweight='bold', color='white')
    elif n == 30:
        ax3.text(i, detection_rates[i]/2, f'{detection_rates[i]:.0f}%',
                ha='center', va='center', fontsize=10, fontweight='bold', color='white')
        ax3.text(i, detection_rates[i] + missed_rates[i]/2, f'{missed_rates[i]:.0f}%',
                ha='center', va='center', fontsize=10, fontweight='bold', color='white')

# Add explanation box
explanation_text = (
    'THE BOTTOM LINE:\n\n'
    'With 5 shots per load:\n'
    '  • You CANNOT reduce false alarms below 5% (that\'s what α = 0.05 means)\n'
    '  • You WILL miss ~90% of real improvements (terrible power)\n'
    '  • Even making α stricter (0.01) doesn\'t help - you still miss real effects!\n\n'
    'With 30+ shots per load:\n'
    '  • False alarms still ~5% (same as before)\n'
    '  • You DETECT ~60-85% of real improvements (good power)\n'
    '  • You can trust your conclusions!\n\n'
    'CONCLUSION: You can\'t fix small samples with stricter criteria. YOU NEED MORE DATA.'
)

ax3.text(0.5, -0.35, explanation_text, transform=ax3.transAxes,
        fontsize=11, verticalalignment='top', horizontalalignment='center',
        bbox=dict(boxstyle='round,pad=1.0', facecolor='lightyellow',
                 edgecolor='black', linewidth=3, alpha=0.95),
        family='monospace', fontweight='bold')

# Save the figure
output_path = Path(__file__).parent.parent / 'lessons' / 'static' / 'nb10_plot25_type_i_ii_error_tradeoff.png'
output_path.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Saved: {output_path}")

# Also display if running interactively
# plt.show()
