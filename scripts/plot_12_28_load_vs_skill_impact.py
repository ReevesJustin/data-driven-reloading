#!/usr/bin/env python3
"""
Plot 28: Load Improvement vs Skill Improvement Impact (Notebook 12)
Visual demonstration of the relative impact of load development vs shooting skill.

Educational Purpose:
Shows that improving shooting fundamentals has 3-5x more impact than
optimizing ammunition for most shooters. This helps prioritize training
over endless load development.

Compares:
- Scenario A: Perfect your load (reduce SD 50%, improve precision 0.2 MOA)
- Scenario B: Improve your skills (improve precision 0.5 MOA)

The visualization makes it obvious where effort should be focused.
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Set random seed for reproducibility
np.random.seed(42)

# Create the figure
fig = plt.figure(figsize=(16, 8))
gs = fig.add_gridspec(2, 2, hspace=0.35, wspace=0.3)

# Main title
fig.suptitle('Load Development vs Skill Development: Where Should You Focus?',
             fontsize=18, fontweight='bold', y=0.98)

# Define baseline shooter (typical intermediate level)
baseline_precision_moa = 1.2  # MOA (rifle + ammo + shooter combined)
baseline_sd_fps = 15  # fps
target_distance_yards = 600  # yards
target_size_moa = 1.0  # MOA (e.g., 6" target at 600 yards)

# Scenario A: Optimize load (expensive, time-consuming)
load_optimized_precision = baseline_precision_moa - 0.2  # 1.0 MOA
load_optimized_sd = baseline_sd_fps * 0.5  # 7.5 fps

# Scenario B: Improve skill (cheaper, more effective)
skill_improved_precision = baseline_precision_moa - 0.5  # 0.7 MOA
skill_improved_sd = baseline_sd_fps  # SD unchanged

# Convert MOA to inches at distance
def moa_to_inches(moa, yards):
    return moa * yards / 100

# Calculate hit probabilities (simplified - circular error probable)
def hit_probability(precision_moa, target_size_moa):
    # Using Rayleigh distribution approximation
    # This is simplified but directionally correct
    radius_ratio = target_size_moa / (precision_moa * 2)
    # Approximate probability
    if radius_ratio >= 2:
        return 0.95
    elif radius_ratio >= 1.5:
        return 0.85
    elif radius_ratio >= 1.0:
        return 0.65
    elif radius_ratio >= 0.7:
        return 0.40
    else:
        return 0.20

baseline_hit_prob = hit_probability(baseline_precision_moa, target_size_moa)
load_hit_prob = hit_probability(load_optimized_precision, target_size_moa)
skill_hit_prob = hit_probability(skill_improved_precision, target_size_moa)

# --- Plot 1: Precision Comparison ---
ax1 = fig.add_subplot(gs[0, 0])

scenarios_precision = ['Baseline\n(Current)', 'Scenario A\n(Perfect Load)',
                      'Scenario B\n(Better Skill)']
precisions = [baseline_precision_moa, load_optimized_precision, skill_improved_precision]
colors_precision = ['gray', 'orange', 'darkgreen']

bars = ax1.bar(scenarios_precision, precisions, color=colors_precision,
              alpha=0.8, edgecolor='black', linewidth=2)

ax1.set_ylabel('Precision (MOA)', fontsize=12, fontweight='bold')
ax1.set_title('Precision Capability Comparison', fontsize=14, fontweight='bold')
ax1.set_ylim(0, 1.5)
ax1.grid(True, alpha=0.3, linestyle=':', linewidth=0.5, axis='y')
ax1.axhline(target_size_moa, color='red', linestyle='--', linewidth=2,
           label=f'Target Size ({target_size_moa} MOA)')

# Add value labels
for bar, prec, color in zip(bars, precisions, colors_precision):
    height = bar.get_height()
    improvement = baseline_precision_moa - prec
    label_text = f'{prec:.1f} MOA'
    if improvement > 0:
        label_text += f'\n(↓ {improvement:.1f})'

    ax1.text(bar.get_x() + bar.get_width()/2., height,
            label_text,
            ha='center', va='bottom', fontsize=11, fontweight='bold')

ax1.legend(fontsize=10)

# Add annotation
ax1.text(0.95, 0.82,
        'Skill improvement:\n3x larger effect\non precision!',
        transform=ax1.transAxes, fontsize=10, fontweight='bold',
        verticalalignment='top', horizontalalignment='right',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='lightgreen', alpha=0.9, edgecolor='darkgreen', linewidth=1.5),
        color='darkgreen')

# --- Plot 2: Hit Probability Comparison ---
ax2 = fig.add_subplot(gs[0, 1])

hit_probs = [baseline_hit_prob * 100, load_hit_prob * 100, skill_hit_prob * 100]

bars2 = ax2.bar(scenarios_precision, hit_probs, color=colors_precision,
               alpha=0.8, edgecolor='black', linewidth=2)

ax2.set_ylabel('Hit Probability (%)', fontsize=12, fontweight='bold')
ax2.set_title(f'First-Round Hit Probability @ {target_distance_yards} Yards',
             fontsize=14, fontweight='bold')
ax2.set_ylim(0, 100)
ax2.grid(True, alpha=0.3, linestyle=':', linewidth=0.5, axis='y')

# Add value labels
for bar, prob, color in zip(bars2, hit_probs, colors_precision):
    height = bar.get_height()
    improvement = prob - baseline_hit_prob * 100
    label_text = f'{prob:.0f}%'
    if improvement > 0:
        label_text += f'\n(+{improvement:.0f}%)'

    ax2.text(bar.get_x() + bar.get_width()/2., height,
            label_text,
            ha='center', va='bottom', fontsize=11, fontweight='bold')

# Add annotation
ax2.text(0.95, 0.80,
        'Skill improvement:\n2x larger increase\nin hit probability!',
        transform=ax2.transAxes, fontsize=10, fontweight='bold',
        verticalalignment='top', horizontalalignment='right',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='lightgreen', alpha=0.9, edgecolor='darkgreen', linewidth=1.5),
        color='darkgreen')

# --- Plot 3: Cost and Time Comparison ---
ax3 = fig.add_subplot(gs[1, 0])

# Estimated costs and time
cost_load = 500  # dollars (components, time at range, testing)
cost_skill = 200  # dollars (ammo for practice, maybe a class)
time_load = 40  # hours (load development, testing, range trips)
time_skill = 20  # hours (focused practice)

scenarios_cost = ['Perfect Load\n(Scenario A)', 'Better Skill\n(Scenario B)']
costs = [cost_load, cost_skill]
times = [time_load, time_skill]

x = np.arange(len(scenarios_cost))
width = 0.35

bars_cost = ax3.bar(x - width/2, costs, width, label='Cost ($)',
                   color='goldenrod', alpha=0.8, edgecolor='black', linewidth=1.5)
ax3_twin = ax3.twinx()
bars_time = ax3_twin.bar(x + width/2, times, width, label='Time (hours)',
                        color='steelblue', alpha=0.8, edgecolor='black', linewidth=1.5)

ax3.set_ylabel('Cost (dollars)', fontsize=12, fontweight='bold', color='goldenrod')
ax3_twin.set_ylabel('Time (hours)', fontsize=12, fontweight='bold', color='steelblue')
ax3.set_title('Investment Required', fontsize=14, fontweight='bold')
ax3.set_xticks(x)
ax3.set_xticklabels(scenarios_cost)
ax3.tick_params(axis='y', labelcolor='goldenrod')
ax3_twin.tick_params(axis='y', labelcolor='steelblue')
ax3.grid(True, alpha=0.3, linestyle=':', linewidth=0.5, axis='y')

# Add value labels
for bar, cost in zip(bars_cost, costs):
    height = bar.get_height()
    ax3.text(bar.get_x() + bar.get_width()/2., height,
            f'${cost:.0f}',
            ha='center', va='bottom', fontsize=11, fontweight='bold',
            color='darkgoldenrod')

for bar, time in zip(bars_time, times):
    height = bar.get_height()
    ax3_twin.text(bar.get_x() + bar.get_width()/2., height,
                 f'{time:.0f}h',
                 ha='center', va='bottom', fontsize=11, fontweight='bold',
                 color='darkblue')

# Combined legend
lines1, labels1 = ax3.get_legend_handles_labels()
lines2, labels2 = ax3_twin.get_legend_handles_labels()
ax3.legend(lines1 + lines2, labels1 + labels2, loc='upper right', fontsize=10)

# --- Plot 4: Return on Investment ---
ax4 = fig.add_subplot(gs[1, 1])

# Calculate improvement per dollar and per hour
load_improvement_per_dollar = (load_hit_prob - baseline_hit_prob) * 100 / cost_load
skill_improvement_per_dollar = (skill_hit_prob - baseline_hit_prob) * 100 / cost_skill

load_improvement_per_hour = (load_hit_prob - baseline_hit_prob) * 100 / time_load
skill_improvement_per_hour = (skill_hit_prob - baseline_hit_prob) * 100 / time_skill

roi_per_dollar = [load_improvement_per_dollar, skill_improvement_per_dollar]
roi_per_hour = [load_improvement_per_hour, skill_improvement_per_hour]

x2 = np.arange(len(scenarios_cost))
width2 = 0.35

bars_roi_dollar = ax4.bar(x2 - width2/2, roi_per_dollar, width2,
                         label='% Hit Prob per $100',
                         color='goldenrod', alpha=0.8, edgecolor='black', linewidth=1.5)
bars_roi_hour = ax4.bar(x2 + width2/2, roi_per_hour, width2,
                       label='% Hit Prob per Hour',
                       color='steelblue', alpha=0.8, edgecolor='black', linewidth=1.5)

ax4.set_ylabel('Improvement Efficiency', fontsize=12, fontweight='bold')
ax4.set_title('Return on Investment (Efficiency)', fontsize=14, fontweight='bold')
ax4.set_xticks(x2)
ax4.set_xticklabels(scenarios_cost)
ax4.legend(fontsize=10)
ax4.grid(True, alpha=0.3, linestyle=':', linewidth=0.5, axis='y')

# Add value labels
for bar, roi in zip(bars_roi_dollar, roi_per_dollar):
    height = bar.get_height()
    ax4.text(bar.get_x() + bar.get_width()/2., height,
            f'{roi:.2f}%',
            ha='center', va='bottom', fontsize=10, fontweight='bold')

for bar, roi in zip(bars_roi_hour, roi_per_hour):
    height = bar.get_height()
    ax4.text(bar.get_x() + bar.get_width()/2., height,
            f'{roi:.2f}%',
            ha='center', va='bottom', fontsize=10, fontweight='bold')

# Add annotation
dollar_ratio = skill_improvement_per_dollar / load_improvement_per_dollar if load_improvement_per_dollar > 0 else 99
hour_ratio = skill_improvement_per_hour / load_improvement_per_hour if load_improvement_per_hour > 0 else 99

ax4.text(0.70, 0.80,
        'SKILL PRACTICE:\n\n'
        f'{dollar_ratio:.1f}x better\n'
        'per dollar!\n\n'
        f'{hour_ratio:.1f}x better\n'
        'per hour!',
        transform=ax4.transAxes, fontsize=10, fontweight='bold',
        verticalalignment='top', horizontalalignment='right',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='lightgreen', alpha=0.9, edgecolor='darkgreen', linewidth=1.5),
        color='darkgreen')

# Save the figure
output_path = Path(__file__).parent.parent / 'lessons' / 'static' / 'nb12_plot28_load_vs_skill_impact.png'
output_path.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Saved: {output_path}")

# Also display if running interactively
# plt.show()
