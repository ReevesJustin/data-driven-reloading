#!/usr/bin/env python3
"""
Plot 7: Confidence Interval Shrinkage (Notebook 03)
Shows how confidence interval width decreases with sample size.

Educational Purpose:
Demonstrates the mathematical relationship between sample size and uncertainty.
Confidence intervals shrink as 1/√n, showing why bigger samples give more certainty.
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from scipy import stats

# Set random seed for reproducibility
np.random.seed(42)

# Simulation parameters
TRUE_SD = 15  # True standard deviation in fps
SAMPLE_SIZES = [5, 10, 20, 30, 50, 100]
CONFIDENCE_LEVEL = 0.95

# Calculate 95% confidence interval width for each sample size
ci_widths = []
theoretical_widths = []

for n in SAMPLE_SIZES:
    # For a normal distribution, CI width = 2 * t_critical * (SD / sqrt(n))
    # Using t-distribution for small samples
    t_critical = stats.t.ppf((1 + CONFIDENCE_LEVEL) / 2, df=n-1)

    # Standard error of the mean
    se = TRUE_SD / np.sqrt(n)

    # Half-width of CI (margin of error)
    margin_of_error = t_critical * se

    # Total width (±margin)
    ci_widths.append(margin_of_error)

    # Theoretical (using normal approximation for comparison)
    z_critical = stats.norm.ppf((1 + CONFIDENCE_LEVEL) / 2)
    theoretical_margin = z_critical * (TRUE_SD / np.sqrt(n))
    theoretical_widths.append(theoretical_margin)

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the curve
ax.plot(SAMPLE_SIZES, ci_widths, 'o-', color='steelblue', linewidth=2.5,
        markersize=10, markeredgecolor='darkblue', markeredgewidth=1.5,
        label='95% Confidence Interval (±margin)')

# Add theoretical curve (smooth)
smooth_n = np.linspace(5, 100, 200)
smooth_ci = stats.norm.ppf(0.975) * TRUE_SD / np.sqrt(smooth_n)
ax.plot(smooth_n, smooth_ci, '--', color='gray', linewidth=1.5,
        alpha=0.6, label='Theoretical 1/√n curve')

# Annotate key points
key_points = [(30, ci_widths[3]), (100, ci_widths[5])]
for n, ci in key_points:
    if n == 30:
        # 30 shots annotation - keep original position
        ax.annotate(f'{n} shots\n±{ci:.1f} fps',
                    xy=(n, ci), xytext=(n + 5, ci + 0.5),
                    fontsize=9, fontweight='bold',
                    bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.7),
                    arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
    else:
        # 100 shots annotation - adjusted position
        ax.annotate(f'{n} shots\n±{ci:.1f} fps',
                    xy=(n, ci), xytext=(n - 7, ci + 1.6),
                    fontsize=9, fontweight='bold',
                    bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.7),
                    arrowprops=dict(arrowstyle='->', color='black', lw=1.5))

# Labels and title
ax.set_xlabel('Sample Size (Number of Shots)', fontsize=12, fontweight='bold')
ax.set_ylabel('95% CI Half-Width (±fps)', fontsize=12, fontweight='bold')
ax.set_title('Why Bigger Samples Give More Certainty\nConfidence Interval Shrinks with √n',
             fontsize=14, fontweight='bold', pad=20)

# Add statistics annotation
stats_text = (
    f'True SD: {TRUE_SD} fps\n'
    f'Confidence Level: {CONFIDENCE_LEVEL*100:.0f}%\n'
    f'\n'
    f'At 5 shots: ±{ci_widths[0]:.1f} fps\n'
    f'At 30 shots: ±{ci_widths[3]:.1f} fps\n'
    f'At 100 shots: ±{ci_widths[5]:.1f} fps\n'
    f'\n'
    f'Doubling precision requires 4× shots'
)

ax.text(0.98, 0.75, stats_text, transform=ax.transAxes,
        fontsize=10, verticalalignment='top', horizontalalignment='right',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

ax.legend(loc='upper right', fontsize=10)
ax.grid(True, alpha=0.3, linestyle=':', linewidth=0.5)

# Set y-axis to start at 0 for clarity
ax.set_ylim(bottom=0)

# Tight layout
plt.tight_layout()

# Save the figure
output_path = Path(__file__).parent.parent / 'lessons' / 'static' / 'nb03_plot07_confidence_interval_shrinkage.png'
output_path.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Saved: {output_path}")

# Also display if running interactively
# plt.show()
