#!/usr/bin/env python3
"""
Plot 11: Statistical Power Demonstration (Notebook 10)
Visual demonstration of Type I vs Type II errors using accessible language.

Educational Purpose:
Makes statistical concepts intuitive by showing overlapping distributions and
error regions. Uses plain language ("false alarm" and "missed opportunity")
instead of technical jargon. Shows how increasing sample size reduces the
overlap between null and alternative distributions, improving detection power.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from pathlib import Path

# Set random seed for reproducibility
np.random.seed(42)

# Parameters for demonstration
null_mean = 0  # Null hypothesis: no difference
effect_size = 0.8  # Cohen's d (standardized effect size)
alpha = 0.05  # Significance level (Type I error rate)

# Create figure with 2x2 grid
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Generate x-axis values
x = np.linspace(-4, 5, 1000)

# ============= Panel 1: Show Alpha Region (False Alarm) =============
ax1 = axes[0, 0]

# Sample size for this demo
n = 20
sem = 1 / np.sqrt(n)  # Standard error of the mean

# Null distribution (no difference)
null_dist = stats.norm.pdf(x, null_mean, sem)
# Alternative distribution (real difference exists)
alt_mean = effect_size * sem * np.sqrt(n)
alt_dist = stats.norm.pdf(x, alt_mean, sem)

# Critical value for alpha = 0.05 (two-tailed)
critical_value = stats.norm.ppf(1 - alpha/2, null_mean, sem)

# Plot distributions
ax1.plot(x, null_dist, 'b-', linewidth=2.5, label='No Real Difference (Null)')
ax1.fill_between(x, 0, null_dist,
                 where=(x >= critical_value),
                 alpha=0.3, color='red',
                 label=f'False Alarm Zone (α = {alpha*100:.0f}%)')
ax1.axvline(critical_value, color='red', linestyle='--', linewidth=2, alpha=0.7)

ax1.set_xlabel('Measured Difference', fontsize=11, fontweight='bold')
ax1.set_ylabel('Probability', fontsize=11, fontweight='bold')
ax1.set_title('Type I Error: False Alarm\n"Thinking you found something when it\'s just luck"',
              fontsize=12, fontweight='bold', pad=15)
ax1.legend(loc='upper right', fontsize=9)
ax1.grid(True, alpha=0.3, linestyle=':', linewidth=0.5)

# Annotation
ax1.text(0.05, 0.95, 'If no real difference exists,\n5% chance we claim one anyway\n(false positive)',
         transform=ax1.transAxes, fontsize=9,
         verticalalignment='top', horizontalalignment='left',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# ============= Panel 2: Show Beta Region (Missed Opportunity) =============
ax2 = axes[0, 1]

# Plot distributions
ax2.plot(x, alt_dist, 'g-', linewidth=2.5, label='Real Difference Exists (Alternative)')
ax2.fill_between(x, 0, alt_dist,
                 where=(x <= critical_value),
                 alpha=0.3, color='orange',
                 label='Missed Opportunity Zone (β)')
ax2.axvline(critical_value, color='red', linestyle='--', linewidth=2, alpha=0.7)

# Calculate beta (Type II error)
beta = stats.norm.cdf(critical_value, alt_mean, sem)

ax2.set_xlabel('Measured Difference', fontsize=11, fontweight='bold')
ax2.set_ylabel('Probability', fontsize=11, fontweight='bold')
ax2.set_title('Type II Error: Missed Opportunity\n"Real difference hidden by noise"',
              fontsize=12, fontweight='bold', pad=15)
ax2.legend(loc='upper right', fontsize=9)
ax2.grid(True, alpha=0.3, linestyle=':', linewidth=0.5)

# Annotation
ax2.text(0.05, 0.95, f'If real difference exists,\n{beta*100:.0f}% chance we miss it\n(false negative)',
         transform=ax2.transAxes, fontsize=9,
         verticalalignment='top', horizontalalignment='left',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# ============= Panel 3: Show Power Region (Correct Detection) =============
ax3 = axes[1, 0]

# Plot both distributions
ax3.plot(x, null_dist, 'b-', linewidth=2, alpha=0.5, label='No Real Difference (Null)')
ax3.plot(x, alt_dist, 'g-', linewidth=2.5, label='Real Difference Exists (Alternative)')

# Power region (1 - beta)
ax3.fill_between(x, 0, alt_dist,
                 where=(x >= critical_value),
                 alpha=0.3, color='green',
                 label=f'Power Zone (1-β = {(1-beta)*100:.0f}%)')
ax3.axvline(critical_value, color='red', linestyle='--', linewidth=2, alpha=0.7,
           label='Decision Threshold')

ax3.set_xlabel('Measured Difference', fontsize=11, fontweight='bold')
ax3.set_ylabel('Probability', fontsize=11, fontweight='bold')
ax3.set_title('Statistical Power: Correct Detection\n"Probability of finding a real difference"',
              fontsize=12, fontweight='bold', pad=15)
ax3.legend(loc='upper left', fontsize=9)
ax3.grid(True, alpha=0.3, linestyle=':', linewidth=0.5)

# Annotation
ax3.text(0.95, 0.95, f'Power = {(1-beta)*100:.0f}%\n\nWhen real difference exists,\n'
         f'{(1-beta)*100:.0f}% chance we detect it\n(correct detection)',
         transform=ax3.transAxes, fontsize=9,
         verticalalignment='top', horizontalalignment='right',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# ============= Panel 4: Sample Size Effect =============
ax4 = axes[1, 1]

# Show how increasing n reduces overlap
sample_sizes = [10, 20, 50, 100]
colors = ['lightcoral', 'coral', 'steelblue', 'darkblue']
alphas = [0.3, 0.4, 0.6, 0.8]

for i, n_demo in enumerate(sample_sizes):
    sem_demo = 1 / np.sqrt(n_demo)
    alt_mean_demo = effect_size * sem_demo * np.sqrt(n_demo)

    null_dist_demo = stats.norm.pdf(x, null_mean, sem_demo)
    alt_dist_demo = stats.norm.pdf(x, alt_mean_demo, sem_demo)

    # Plot only alternative distributions to show separation
    ax4.plot(x, alt_dist_demo, color=colors[i], linewidth=2,
            alpha=alphas[i], label=f'n = {n_demo}')

# Reference null distribution
sem_ref = 1 / np.sqrt(20)
null_dist_ref = stats.norm.pdf(x, null_mean, sem_ref)
ax4.plot(x, null_dist_ref, 'k--', linewidth=2, alpha=0.5, label='Null (n=20)')

ax4.set_xlabel('Measured Difference', fontsize=11, fontweight='bold')
ax4.set_ylabel('Probability', fontsize=11, fontweight='bold')
ax4.set_title('More Data = Better Separation = Higher Power\n"Why sample size matters"',
              fontsize=12, fontweight='bold', pad=15)
ax4.legend(loc='upper right', fontsize=9)
ax4.grid(True, alpha=0.3, linestyle=':', linewidth=0.5)

# Annotation
summary_text = (
    'As sample size increases:\n'
    '• Distributions become narrower\n'
    '• Less overlap between null/alternative\n'
    '• Higher power (better detection)\n'
    '• More confidence in results\n\n'
    'Trade-off:\n'
    '• More shots = more cost\n'
    '• But also = less wasted retests'
)

ax4.text(0.02, 0.98, summary_text, transform=ax4.transAxes,
         fontsize=9, verticalalignment='top', horizontalalignment='left',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# Overall title
fig.suptitle('Understanding Statistical Errors and Power\nMaking Sense of False Alarms and Missed Opportunities',
             fontsize=16, fontweight='bold', y=0.995)

# Tight layout
plt.tight_layout(rect=[0, 0, 1, 0.99])

# Save the figure
output_path = Path(__file__).parent.parent / 'lessons' / 'static' / 'nb10_plot11_statistical_power_demo.png'
output_path.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Saved: {output_path}")

# Also display if running interactively
# plt.show()
