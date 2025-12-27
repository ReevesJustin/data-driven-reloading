#!/usr/bin/env python3
"""
Plot 21: Component Quality vs Precision (Notebook 09)
Shows diminishing returns curve for component cost vs precision improvement.

Educational Purpose:
Demonstrates that biggest gains come from upgrading low-end components, not
chasing ultimate perfection. High-end components show tiny improvements at
huge cost increases - classic diminishing returns.
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Set random seed for reproducibility
np.random.seed(42)

# Define upgrade paths with cost and precision data
upgrades = [
    # (component, cost_increase, precision_improvement_moa, cumulative_cost, cumulative_precision)
    ('Stock rifle', 0, 2.5, 0, 2.5),
    ('Quality barrel', 400, 0.8, 400, 1.7),
    ('Match bullets', 0.20 * 50, 0.4, 410, 1.3),  # $0.20/bullet * 50 bullets
    ('Bedding job', 150, 0.25, 560, 1.05),
    ('Premium trigger', 250, 0.20, 810, 0.85),
    ('Custom bullets', 0.80 * 50, 0.15, 850, 0.70),  # Additional $0.80/bullet
    ('Premium barrel', 500, 0.15, 1350, 0.55),
    ('Blueprinting', 300, 0.10, 1650, 0.45),
    ('Custom action', 1200, 0.10, 2850, 0.35),
    ('Full custom build', 2000, 0.10, 4850, 0.25),
]

# Extract data for plotting
components = [u[0] for u in upgrades]
costs = [u[3] for u in upgrades]
precisions = [u[4] for u in upgrades]
incremental_costs = [u[1] for u in upgrades]
incremental_improvements = [upgrades[i-1][4] - u[4] if i > 0 else 0 for i, u in enumerate(upgrades)]

# Create figure with two panels
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Panel 1: Cumulative cost vs precision
ax1.plot(costs, precisions, 'o-', color='steelblue', linewidth=2.5,
         markersize=10, markeredgecolor='darkblue', markeredgewidth=1.5)

# Annotate key points
key_indices = [0, 1, 2, 4, 7, 9]
for idx in key_indices:
    if idx < len(components):
        ax1.annotate(components[idx],
                     xy=(costs[idx], precisions[idx]),
                     xytext=(10, -5 if idx % 2 == 0 else 5),
                     textcoords='offset points',
                     fontsize=8, fontweight='bold',
                     bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.6),
                     arrowprops=dict(arrowstyle='->', color='black', lw=1))

# Labels
ax1.set_xlabel('Cumulative Cost ($)', fontsize=12, fontweight='bold')
ax1.set_ylabel('Rifle Precision (MOA)', fontsize=12, fontweight='bold')
ax1.set_title('Diminishing Returns: Cost vs Precision\n'
              'Biggest Gains from Upgrading Low-End Components',
              fontsize=13, fontweight='bold', pad=15)

# Invert y-axis (smaller MOA is better)
ax1.invert_yaxis()

ax1.grid(True, alpha=0.3, linestyle=':', linewidth=0.5)

# Add annotation showing diminishing returns
ax1.annotate('', xy=(850, 0.70), xytext=(400, 1.7),
             arrowprops=dict(arrowstyle='<->', color='red', lw=3))
ax1.text(625, 1.2, '$450 → 1.0 MOA\nimprovement',
         fontsize=10, fontweight='bold', color='red',
         bbox=dict(boxstyle='round,pad=0.5', facecolor='lightcoral', alpha=0.7))

ax1.annotate('', xy=(4850, 0.25), xytext=(1650, 0.45),
             arrowprops=dict(arrowstyle='<->', color='darkred', lw=3))
ax1.text(3250, 0.35, '$3200 → 0.2 MOA\nimprovement',
         fontsize=10, fontweight='bold', color='darkred',
         bbox=dict(boxstyle='round,pad=0.5', facecolor='lightcoral', alpha=0.7))

# Panel 2: Cost per 0.1 MOA improvement
# Calculate efficiency (cost per 0.1 MOA improvement)
efficiencies = []
efficiency_labels = []

for i in range(1, len(upgrades)):
    cost = incremental_costs[i]
    improvement = incremental_improvements[i]

    if improvement > 0:
        cost_per_01moa = cost / (improvement / 0.1)
        efficiencies.append(cost_per_01moa)
        efficiency_labels.append(components[i])

# Create bar chart
positions = np.arange(len(efficiencies))
colors = ['green' if e < 200 else 'orange' if e < 500 else 'red' for e in efficiencies]

ax2.barh(positions, efficiencies, color=colors, edgecolor='black', linewidth=1.5, alpha=0.7)

# Labels
ax2.set_yticks(positions)
ax2.set_yticklabels(efficiency_labels, fontsize=9)
ax2.set_xlabel('Cost per 0.1 MOA Improvement ($)', fontsize=12, fontweight='bold')
ax2.set_title('Upgrade Efficiency: Where to Spend Your Money\n'
              'Green = Good Value, Red = Expensive Improvements',
              fontsize=13, fontweight='bold', pad=15)

ax2.grid(True, alpha=0.3, linestyle=':', linewidth=0.5, axis='x')

# Add value annotations
for i, (eff, label) in enumerate(zip(efficiencies, efficiency_labels)):
    ax2.text(eff + 50, i, f'${eff:.0f}',
             fontsize=8, fontweight='bold', va='center')

# Add statistics box
stats_text = (
    'Specific Examples:\n'
    '\n'
    'Bulk → Match bullets:\n'
    '  0.4 MOA better, +$10 (50 rnds)\n'
    '  $25 per 0.1 MOA - Great value!\n'
    '\n'
    'Match → Custom bullets:\n'
    '  0.15 MOA better, +$40 (50 rnds)\n'
    '  $267 per 0.1 MOA - Expensive!\n'
    '\n'
    'Quality → Premium barrel:\n'
    '  0.15 MOA better, +$500\n'
    '  $333 per 0.1 MOA - Ouch!\n'
    '\n'
    'Best bang for buck:\n'
    '1. Quality barrel\n'
    '2. Match bullets\n'
    '3. Bedding job'
)

ax2.text(0.98, 0.97, stats_text, transform=ax2.transAxes,
         fontsize=8.5, verticalalignment='top', horizontalalignment='right',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.9, edgecolor='black', linewidth=1),
         family='monospace')

# Overall title
fig.suptitle('Component Quality Diminishing Returns: Biggest Gains from Basic Upgrades\n'
             'Don\'t Chase Ultimate Perfection - Upgrade Smart, Not Expensive',
             fontsize=14, fontweight='bold', y=1.00)

# Tight layout
plt.tight_layout()

# Save the figure
output_path = Path(__file__).parent.parent / 'notebooks' / 'static' / 'nb09_plot21_component_quality_vs_precision.png'
output_path.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Saved: {output_path}")

# Also display if running interactively
# plt.show()
