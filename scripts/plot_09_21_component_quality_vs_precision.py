#!/usr/bin/env python3
"""
Plot 21: The Pareto Principle - Last 10% Costs 90% (Notebook 09)
Shows how the final increments of precision improvement require disproportionate investment.

Educational Purpose:
Demonstrates the Pareto Principle (80/20 rule) in precision shooting: getting 80% of
maximum capability requires ~20% of maximum investment, but the final 20% of capability
requires 80% of investment. Emphasizes testing to identify YOUR limiting factor.
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Set random seed for reproducibility
np.random.seed(42)

# Define upgrade path with cumulative cost and capability
# Using "capability" (0-100%) instead of specific MOA to avoid equipment claims
upgrades = [
    # (name, cumulative_cost, capability_percent, notes)
    ('Factory Rifle\n+ Budget Optic\n+ Factory Ammo', 1200, 50,
     'Starting point:\n$800 rifle\n$250 optic/mount\n$1.50/rd ammo'),

    ('+ Match Ammo', 1350, 65,
     'Upgrade:\n$3.00/rd ammo\n+$150 for 50 rounds'),

    ('+ Quality Optic\n  & Mount', 2200, 78,
     'Upgrade:\n$850 optic/mount\nOften the weak link!'),

    ('+ Barrel & Stock\nUpgrade', 3400, 87,
     'Upgrade:\n$1200 work\nBarrel + bedding'),

    ('+ Premium Ammo\n  Tools', 6100, 91,
     'Upgrade:\n$2700 more\nAnnealer, lab scale,\npremium dies, etc.'),

    ('Full Custom\nBuild', 10200, 95,
     'Upgrade:\n$4100 more\nCustom action, trigger,\npremium barrel, stock'),
]

# Extract data
names = [u[0] for u in upgrades]
costs = [u[1] for u in upgrades]
capabilities = [u[2] for u in upgrades]
notes = [u[3] for u in upgrades]

# Create figure with two panels
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 12))
fig.subplots_adjust(hspace=0.35)
ax1.plot(costs, capabilities, 'o-', color='steelblue', linewidth=3,
         markersize=12, markeredgecolor='darkblue', markeredgewidth=2)

# Annotate each upgrade
for i, (cost, cap, name) in enumerate(zip(costs, capabilities, names)):
    offset_y = 8 if i % 2 == 0 else -8
    va = 'bottom' if i % 2 == 0 else 'top'

    ax1.annotate(name, xy=(cost, cap),
                xytext=(0, offset_y), textcoords='offset points',
                fontsize=9, fontweight='bold', ha='center', va=va,
                bbox=dict(boxstyle='round,pad=0.4', facecolor='yellow',
                         alpha=0.7, edgecolor='black', linewidth=1),
                arrowprops=dict(arrowstyle='->', color='black', lw=1.5))

# Highlight the Pareto zones
ax1.axhspan(0, 80, alpha=0.15, color='green', label='High ROI Zone (80% capability)')
ax1.axhspan(80, 100, alpha=0.15, color='red', label='Diminishing Returns (last 20%)')

# Add cost comparison annotation
ax1.annotate('', xy=(2200, 78), xytext=(1200, 50),
             arrowprops=dict(arrowstyle='<->', color='green', lw=4))
ax1.text(2750, 64, 'First 28%:\n$1,000 cost',
         fontsize=11, fontweight='bold', color='darkgreen', ha='center',
         bbox=dict(boxstyle='round,pad=0.5', facecolor='lightgreen',
                  alpha=0.8, edgecolor='darkgreen', linewidth=2))

ax1.annotate('', xy=(10200, 95), xytext=(2200, 78),
             arrowprops=dict(arrowstyle='<->', color='darkred', lw=4))
ax1.text(6200, 76, 'Last 17%:\n$8,000 cost',
         fontsize=11, fontweight='bold', color='darkred', ha='center',
         bbox=dict(boxstyle='round,pad=0.5', facecolor='lightcoral',
                  alpha=0.8, edgecolor='darkred', linewidth=2))

ax1.set_xlabel('Cumulative Investment ($)', fontsize=13, fontweight='bold')
ax1.set_ylabel('System Capability (%)', fontsize=13, fontweight='bold')
ax1.set_title('The Pareto Principle: Last 10% Costs 90%\n'
              'Getting 80% of Maximum Capability is Cheap - Chasing Perfection is Expensive',
              fontsize=14, fontweight='bold', pad=15)
ax1.grid(True, alpha=0.3, linestyle=':', linewidth=0.5)
ax1.set_ylim(45, 100)
ax1.legend(loc='lower right', fontsize=10, framealpha=0.9)

# Panel 2: Cost efficiency ($ per 1% capability gain)
incremental_costs = [costs[0]] + [costs[i] - costs[i-1] for i in range(1, len(costs))]
incremental_caps = [capabilities[0]] + [capabilities[i] - capabilities[i-1] for i in range(1, len(capabilities))]
efficiency = [cost/cap if cap > 0 else 0 for cost, cap in zip(incremental_costs, incremental_caps)]

colors = ['green' if e < 20 else 'orange' if e < 50 else 'red' for e in efficiency]
positions = np.arange(len(efficiency))

bars = ax2.barh(positions, efficiency, color=colors, edgecolor='black',
                linewidth=1.5, alpha=0.7)

ax2.set_yticks(positions)
ax2.set_yticklabels([f'Step {i+1}' for i in range(len(efficiency))], fontsize=9)
ax2.set_xlabel('Cost per 1% Capability Gain ($)', fontsize=12, fontweight='bold')
ax2.set_title('Where Your Money Goes\nGreen = Good Value, Red = Expensive',
              fontsize=12, fontweight='bold', pad=12)
ax2.grid(True, alpha=0.3, linestyle=':', linewidth=0.5, axis='x')

# Add value labels with dynamic positioning
for i, eff in enumerate(efficiency):
    # Position label to the right of bar, with padding
    label_x = max(eff + 5, 15)  # Ensure minimum distance from left edge
    ax2.text(label_x, i, f'${eff:.0f}',
             fontsize=9, fontweight='bold', va='center', ha='left')

# Add upgrade path annotation box (positioned to avoid bar overlap)
upgrade_details = (
    'Upgrade Path:\n'
    '1. Factory + Budget Optic + Factory Ammo\n'
    '2. + Match Ammo\n'
    '3. + Quality Optic & Mount ← Often weak link!\n'
    '4. + Barrel & Stock Upgrade\n'
    '5. + Premium Ammo Tools (annealer, etc.)\n'
    '6. Full Custom Build'
)
ax2.text(0.98, 0.03, upgrade_details,
         transform=ax2.transAxes,
         fontsize=8, verticalalignment='bottom', horizontalalignment='right',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.85,
                  edgecolor='black', linewidth=1),
         family='monospace')

# Overall title
fig.suptitle('The Pareto Principle: Diminishing Returns in Precision Equipment\n'
             'Getting 80% of Capability Takes 20% of Investment — The Last 20% Takes 80%',
             fontsize=14, fontweight='bold', y=0.99)

# Save the figure
output_path = Path(__file__).parent.parent / 'lessons' / 'static' / 'nb09_plot21_component_quality_vs_precision.png'
output_path.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Saved: {output_path}")

# Also display if running interactively
# plt.show()
