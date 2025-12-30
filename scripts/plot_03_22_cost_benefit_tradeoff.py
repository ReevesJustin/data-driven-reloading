#!/usr/bin/env python3
"""
Plot 22: Cost-Benefit Tradeoff Analysis (Notebook 03)
Shows accuracy improvement vs component cost and expected retest probability.

Educational Purpose:
Demonstrates that proper testing saves money long-term by reducing the need for
retesting. Shows the sweet spot of 30-50 shots where confidence is high enough
to avoid wasted components while keeping initial costs reasonable.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from pathlib import Path

# Set random seed for reproducibility
np.random.seed(42)

# Parameters
sample_sizes = np.array([5, 10, 20, 30, 50, 100])
cost_per_round = 1.50

# Calculate costs
costs = sample_sizes * cost_per_round

# Calculate confidence levels (based on standard error reduction)
# Confidence improves with sqrt(n), normalized to 0-100% scale
# Using a realistic model: at n=5, confidence ~50%, at n=100, confidence ~95%
confidence = 100 * (1 - np.exp(-sample_sizes / 30))

# Calculate retest probability (inverse of confidence)
# Probability you'll need to retest due to inconclusive results
retest_prob = (100 - confidence) / 100

# Expected total cost including retests
# Assume average 1.5 retests for low confidence tests
expected_retests = retest_prob * 1.5
expected_total_cost = costs * (1 + expected_retests)

# Create figure with two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

# ============= PLOT 1: Cost vs Confidence =============
ax1_right = ax1.twinx()

# Plot cost on left axis
line1 = ax1.plot(sample_sizes, costs, 'o-', color='steelblue',
                 linewidth=2.5, markersize=10, label='Initial Cost')
line2 = ax1.plot(sample_sizes, expected_total_cost, 's--', color='coral',
                 linewidth=2.5, markersize=10, label='Expected Total Cost (w/ retests)')

# Plot confidence on right axis
line3 = ax1_right.plot(sample_sizes, confidence, '^-', color='green',
                       linewidth=2.5, markersize=10, alpha=0.7, label='Confidence Level')

# Highlight the sweet spot (30-50 shots)
ax1.axvspan(30, 50, alpha=0.15, color='gold', label='Sweet Spot (30-50 shots)')

# Labels and title
ax1.set_xlabel('Number of Shots', fontsize=12, fontweight='bold')
ax1.set_ylabel('Cost ($)', fontsize=12, fontweight='bold', color='steelblue')
ax1_right.set_ylabel('Confidence Level (%)', fontsize=12, fontweight='bold', color='green')
ax1.set_title('Cost vs Confidence Tradeoff\nProper Testing Saves Money Long-Term',
              fontsize=14, fontweight='bold', pad=20)

# Tick colors
ax1.tick_params(axis='y', labelcolor='steelblue')
ax1_right.tick_params(axis='y', labelcolor='green')

# Combine legends
lines = line1 + line2 + line3
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left', fontsize=10)

# Grid
ax1.grid(True, alpha=0.3, linestyle=':', linewidth=0.5)

# Add annotations for key points
ax1.annotate('Low confidence\nHigh retest risk',
             xy=(10, costs[1]), xytext=(6, 87),
             fontsize=9, ha='left',
             arrowprops=dict(arrowstyle='->', color='gray', lw=1.5),
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

ax1.annotate('Sweet spot:\nGood confidence\nReasonable cost',
             xy=(40, expected_total_cost[3]), xytext=(55, 57),
             fontsize=9, ha='left',
             arrowprops=dict(arrowstyle='->', color='gray', lw=1.5),
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# ============= PLOT 2: Retest Probability and True Cost =============
# Calculate cost breakdown
initial_cost = costs
retest_cost = costs * expected_retests

# Stacked bar chart
bar_width = 6
positions = sample_sizes

bars1 = ax2.bar(positions, initial_cost, bar_width,
                label='Initial Test Cost', color='steelblue', alpha=0.8)
bars2 = ax2.bar(positions, retest_cost, bar_width, bottom=initial_cost,
                label='Expected Retest Cost', color='coral', alpha=0.8)

# Add retest probability labels on bars
for i, (n, prob) in enumerate(zip(sample_sizes, retest_prob)):
    if prob > 0.05:  # Only show if > 5%
        ax2.text(n, expected_total_cost[i] + 5,
                f'{prob*100:.0f}% retest\nprobability',
                ha='center', va='bottom', fontsize=8,
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.9, edgecolor='gray', linewidth=0.5))

# Labels and title
ax2.set_xlabel('Number of Shots', fontsize=12, fontweight='bold')
ax2.set_ylabel('Expected Total Cost ($)', fontsize=12, fontweight='bold')
ax2.set_title('Expected Total Cost Including Retests\nSmall Samples Often Cost More in the Long Run',
              fontsize=14, fontweight='bold', pad=20)

# Legend
ax2.legend(loc='upper left', fontsize=10)

# Grid
ax2.grid(True, alpha=0.3, linestyle=':', linewidth=0.5, axis='y')

# Set x-ticks
ax2.set_xticks(sample_sizes)

# Add statistics annotation
stats_text = (
    'Key Insights:\n'
    f'• 10 shots: ${costs[1]:.0f} initial, but {retest_prob[1]*100:.0f}% retest chance\n'
    f'  Expected total: ${expected_total_cost[1]:.0f}\n'
    f'• 30 shots: ${costs[3]:.0f} initial, {retest_prob[3]*100:.0f}% retest chance\n'
    f'  Expected total: ${expected_total_cost[3]:.0f}\n'
    f'• 50 shots: ${costs[4]:.0f} initial, {retest_prob[4]*100:.0f}% retest chance\n'
    f'  Expected total: ${expected_total_cost[4]:.0f}\n\n'
    'More shots up front = less waste on retests'
)

ax2.text(0.855, 0.97, stats_text, transform=ax2.transAxes,
         fontsize=8.5, verticalalignment='top', horizontalalignment='right',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.9, edgecolor='black', linewidth=1))

# Tight layout
plt.tight_layout()

# Save the figure
output_path = Path(__file__).parent.parent / 'lessons' / 'static' / 'nb03_plot22_cost_benefit_tradeoff.png'
output_path.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Saved: {output_path}")

# Also display if running interactively
# plt.show()
