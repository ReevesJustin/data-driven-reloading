#!/usr/bin/env python3
"""
Plot 27: Factorial Explosion - OFAT vs Full Factorial (Notebook 04)
Visual demonstration of why full factorial experiments are impractical for reloading.

Educational Purpose:
Shows the combinatorial explosion when testing multiple variables simultaneously:
- Compares One-Factor-At-A-Time (OFAT) to full factorial
- Demonstrates cost in rounds, time, and money
- Makes OFAT approach obviously superior for practical reloading

This visualization makes the mathematical explosion visceral and memorable.
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Set random seed for reproducibility
np.random.seed(42)

# Create the figure
fig = plt.figure(figsize=(16, 12))
gs = fig.add_gridspec(3, 2, hspace=0.35, wspace=0.3, height_ratios=[1, 1, 0.8])

# Main title
fig.suptitle('The Factorial Explosion: Why Full Factorial Testing is Impossible',
             fontsize=18, fontweight='bold', y=0.98)

# Define test scenarios
primers = ['Primer A', 'Primer B', 'Primer C']
powders = ['Powder 1', 'Powder 2', 'Powder 3', 'Powder 4']
charges = ['41.0gr', '41.5gr', '42.0gr', '42.5gr', '43.0gr', '43.5gr']
seating_depths = ['0.020"', '0.040"', '0.060"', '0.080"']

shots_per_combo = 30  # Minimum for reliable SD measurement
cost_per_round = 1.50  # dollars
rounds_per_hour = 60  # at the range

# --- Plot 1: Factorial Matrix Visualization ---
ax1 = fig.add_subplot(gs[0, :])

# For visualization, show a simplified 3x3x3 factorial
n_factors = 3
levels_per_factor = 3
total_combos_simple = levels_per_factor ** n_factors

# Create a 3D-like visualization of combinations
x_coords = []
y_coords = []
colors = []

for i in range(levels_per_factor):
    for j in range(levels_per_factor):
        for k in range(levels_per_factor):
            # Position in 2D with depth illusion
            x = i * 2 + k * 0.3
            y = j * 2 + k * 0.3
            x_coords.append(x)
            y_coords.append(y)
            # Color by depth
            colors.append(plt.cm.viridis(k / (levels_per_factor - 1)))

ax1.scatter(x_coords, y_coords, s=500, c=colors, alpha=0.7,
           edgecolors='black', linewidths=2)

# Add labels
ax1.text(-1, 3, 'Factor 1\n(e.g., Primer)', fontsize=12, fontweight='bold',
        ha='center', va='center', rotation=90)
ax1.text(3, -0.5, 'Factor 2\n(e.g., Powder)', fontsize=12, fontweight='bold',
        ha='center', va='center')
ax1.text(7, 5.5, 'Factor 3\n(e.g., Charge)', fontsize=12, fontweight='bold',
        ha='center', va='center')

ax1.set_xlim(-2, 8)
ax1.set_ylim(-1, 6)
ax1.set_aspect('equal')
ax1.axis('off')
ax1.set_title('Visualizing the Factorial Nightmare: Every Dot is a Different Test Combination',
             fontsize=14, fontweight='bold', color='darkred', pad=20)

# --- Plot 2: Comparison Bar Chart ---
ax2 = fig.add_subplot(gs[1, 0])

# Calculate scenarios
scenarios = [
    {
        'name': 'OFAT\n(Recommended)',
        'n_primers': 1,
        'n_powders': 1,
        'n_charges': 5,
        'n_depths': 1,
        'combos': 5,
        'color': 'darkgreen'
    },
    {
        'name': 'Test 2 Primers\n(OFAT)',
        'n_primers': 2,
        'n_powders': 1,
        'n_charges': 5,
        'n_depths': 1,
        'combos': 2 + 5,  # 2 primers + 5 charges
        'color': 'green'
    },
    {
        'name': 'Add Powder\nTest',
        'n_primers': 1,
        'n_powders': 2,
        'n_charges': 5,
        'n_depths': 1,
        'combos': 2*5,  # 2 powders × 5 charges
        'color': 'orange'
    },
    {
        'name': 'Full Factorial\n(Madness)',
        'n_primers': 3,
        'n_powders': 4,
        'n_charges': 6,
        'n_depths': 4,
        'combos': 3*4*6*4,
        'color': 'darkred'
    }
]

scenario_names = [s['name'] for s in scenarios]
total_rounds = [s['combos'] * shots_per_combo for s in scenarios]
colors_bar = [s['color'] for s in scenarios]

bars = ax2.bar(scenario_names, total_rounds, color=colors_bar, alpha=0.8,
              edgecolor='black', linewidth=2)

ax2.set_ylabel('Total Rounds Required', fontsize=12, fontweight='bold')
ax2.set_title('Total Rounds Comparison', fontsize=13, fontweight='bold')
ax2.grid(True, alpha=0.3, linestyle=':', linewidth=0.5, axis='y')
ax2.set_yscale('log')  # Log scale to show the explosion

# Add value labels on bars
for bar, rounds in zip(bars, total_rounds):
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height,
            f'{rounds:,}',
            ha='center', va='bottom', fontsize=11, fontweight='bold')

# Add recommendation box
ax2.text(0.05, 0.70,
        'RECOMMENDED:\n\nOFAT with 5 charges\n= 150 rounds\n\nReasonable for\none range session',
        transform=ax2.transAxes, fontsize=9,
        verticalalignment='top', horizontalalignment='left',
        bbox=dict(boxstyle='round,pad=0.6', facecolor='lightgreen', alpha=0.9, edgecolor='darkgreen', linewidth=1.5),
        fontweight='bold')

# Add warning box
ax2.text(0.95, 0.70,
        'FULL FACTORIAL:\n\n21,600 rounds!\n\nCompletely\nimpractical',
        transform=ax2.transAxes, fontsize=9,
        verticalalignment='top', horizontalalignment='right',
        bbox=dict(boxstyle='round,pad=0.6', facecolor='lightcoral', alpha=0.9, edgecolor='darkred', linewidth=1.5),
        fontweight='bold')

# --- Plot 3: Cost and Time Comparison ---
ax3 = fig.add_subplot(gs[1, 1])

# Calculate costs and times
costs = [rounds * cost_per_round for rounds in total_rounds]
hours = [rounds / rounds_per_hour for rounds in total_rounds]

# Create grouped bar chart
x = np.arange(len(scenarios))
width = 0.35

bars1 = ax3.bar(x - width/2, costs, width, label='Cost ($)',
               color='goldenrod', alpha=0.8, edgecolor='black', linewidth=1.5)
ax3_twin = ax3.twinx()
bars2 = ax3_twin.bar(x + width/2, hours, width, label='Time (hours)',
                    color='steelblue', alpha=0.8, edgecolor='black', linewidth=1.5)

ax3.set_xlabel('Testing Approach', fontsize=12, fontweight='bold')
ax3.set_ylabel('Cost (dollars)', fontsize=12, fontweight='bold', color='goldenrod')
ax3_twin.set_ylabel('Range Time (hours)', fontsize=12, fontweight='bold', color='steelblue')
ax3.set_title('Cost and Time Impact', fontsize=13, fontweight='bold')
ax3.set_xticks(x)
ax3.set_xticklabels(scenario_names, rotation=15, ha='right')
ax3.tick_params(axis='y', labelcolor='goldenrod')
ax3_twin.tick_params(axis='y', labelcolor='steelblue')
ax3.grid(True, alpha=0.3, linestyle=':', linewidth=0.5, axis='y')

# Add value labels
for bar, cost in zip(bars1, costs):
    height = bar.get_height()
    ax3.text(bar.get_x() + bar.get_width()/2., height,
            f'${cost:,.0f}',
            ha='center', va='bottom', fontsize=9, fontweight='bold', color='darkgoldenrod')

for bar, hour in zip(bars2, hours):
    height = bar.get_height()
    ax3_twin.text(bar.get_x() + bar.get_width()/2., height,
                 f'{hour:.0f}h',
                 ha='center', va='bottom', fontsize=9, fontweight='bold', color='darkblue')

# Combined legend
lines1, labels1 = ax3.get_legend_handles_labels()
lines2, labels2 = ax3_twin.get_legend_handles_labels()
ax3.legend(lines1 + lines2, labels1 + labels2, loc='upper left', fontsize=10)

# --- Plot 4: Bottom Summary Table ---
ax4 = fig.add_subplot(gs[2, :])
ax4.axis('off')

# Create detailed comparison table
table_data = []
table_data.append(['Approach', 'Variables Tested', 'Combinations', 'Total Rounds',
                  'Cost ($)', 'Time (hrs)', 'Practical?'])

for scenario in scenarios:
    practicality = '✓ YES' if scenario['combos'] <= 10 else '✗ NO'
    if scenario['combos'] > 50:
        practicality = '✗✗ IMPOSSIBLE'

    table_data.append([
        scenario['name'].replace('\n', ' '),
        f"{scenario['n_primers']}P × {scenario['n_powders']}Pw × "
        f"{scenario['n_charges']}C × {scenario['n_depths']}D",
        f"{scenario['combos']}",
        f"{scenario['combos'] * shots_per_combo:,}",
        f"${scenario['combos'] * shots_per_combo * cost_per_round:,.0f}",
        f"{scenario['combos'] * shots_per_combo / rounds_per_hour:.1f}",
        practicality
    ])

table = ax4.table(cellText=table_data, cellLoc='center', loc='center',
                 bbox=[0, 0, 1, 1])
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 2.5)

# Style header row
for i in range(7):
    cell = table[(0, i)]
    cell.set_facecolor('lightgray')
    cell.set_text_props(weight='bold', fontsize=11)

# Style data rows with colors
for i in range(1, 5):
    color = scenarios[i-1]['color']
    if 'dark' in color:
        alpha = 0.3
    else:
        alpha = 0.2

    for j in range(7):
        cell = table[(i, j)]
        cell.set_facecolor(color)
        cell.set_alpha(alpha)

    # Highlight practicality column
    cell = table[(i, 6)]
    if '✓' in cell.get_text().get_text():
        cell.set_facecolor('lightgreen')
        cell.set_alpha(0.7)
    else:
        cell.set_facecolor('lightcoral')
        cell.set_alpha(0.7)

ax4.text(0.5, -0.15,
        'THE BOTTOM LINE: Full factorial testing explodes combinatorially. OFAT (One-Factor-At-A-Time) is the only '
        'practical approach for reloaders.\n'
        'Test ONE variable at a time with proper sample sizes. Move to the next variable only after you understand the first.',
        transform=ax4.transAxes, fontsize=12, fontweight='bold',
        ha='center', va='top',
        bbox=dict(boxstyle='round,pad=1.0', facecolor='lightyellow',
                 edgecolor='black', linewidth=3, alpha=0.95))

# Save the figure
output_path = Path(__file__).parent.parent / 'lessons' / 'static' / 'nb04_plot27_factorial_explosion.png'
output_path.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Saved: {output_path}")

# Also display if running interactively
# plt.show()
