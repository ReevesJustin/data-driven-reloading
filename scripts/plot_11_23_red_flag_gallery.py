#!/usr/bin/env python3
"""
Plot 23: Red Flag Gallery (Notebook 11)
Side-by-side comparison of good vs questionable data claims.

Educational Purpose:
Teaches readers to spot suspiciously perfect data, cherry-picked results,
and unrealistic precision claims. Critical thinking for evaluating online
load data and forum posts.
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Set random seed for reproducibility
np.random.seed(42)

# Create figure with 3x2 grid
fig, axes = plt.subplots(3, 2, figsize=(14, 12))

# Example 1: Group sizes - normal variance vs suspiciously consistent
ax_good_1 = axes[0, 0]
ax_bad_1 = axes[0, 1]

# Good: Realistic variance
np.random.seed(42)
good_groups = np.random.lognormal(np.log(0.8), 0.25, 10)
ax_good_1.bar(range(1, 11), good_groups, color='steelblue', edgecolor='black',
              linewidth=1.5, alpha=0.7)
ax_good_1.axhline(np.mean(good_groups), color='red', linestyle='--', linewidth=2,
                  label=f'Average: {np.mean(good_groups):.2f} MOA')
ax_good_1.set_ylabel('Group Size (MOA)', fontsize=10, fontweight='bold')
ax_good_1.set_xlabel('Group Number', fontsize=10, fontweight='bold')
ax_good_1.set_title('GOOD: Normal Variance\nRealistic group-to-group variation',
                    fontsize=11, fontweight='bold', color='green')
ax_good_1.set_ylim([0, 2])
ax_good_1.legend(fontsize=8)
ax_good_1.grid(True, alpha=0.3, linestyle=':', linewidth=0.5)

# Bad: Suspiciously consistent
np.random.seed(42)
bad_groups = np.random.normal(0.45, 0.02, 10)  # Unrealistically tight
ax_bad_1.bar(range(1, 11), bad_groups, color='red', edgecolor='black',
             linewidth=1.5, alpha=0.7)
ax_bad_1.axhline(np.mean(bad_groups), color='darkred', linestyle='--', linewidth=2,
                 label=f'Average: {np.mean(bad_groups):.2f} MOA')
ax_bad_1.set_ylabel('Group Size (MOA)', fontsize=10, fontweight='bold')
ax_bad_1.set_xlabel('Group Number', fontsize=10, fontweight='bold')
ax_bad_1.set_title('RED FLAG: Too Consistent\nAll groups <0.5 MOA? Suspicious!',
                   fontsize=11, fontweight='bold', color='darkred')
ax_bad_1.set_ylim([0, 2])
ax_bad_1.legend(fontsize=8)
ax_bad_1.grid(True, alpha=0.3, linestyle=':', linewidth=0.5)

# Example 2: Velocity ladder - scatter vs perfect staircase
ax_good_2 = axes[1, 0]
ax_bad_2 = axes[1, 1]

# Good: Realistic scatter
charges = np.array([40.0, 40.5, 41.0, 41.5, 42.0, 42.5, 43.0])
np.random.seed(42)
good_velocities = 2700 + 25 * (charges - 40.0) + np.random.normal(0, 10, len(charges))
ax_good_2.plot(charges, good_velocities, 'o-', color='steelblue', markersize=10,
               linewidth=2, markeredgecolor='darkblue', markeredgewidth=1.5)
ax_good_2.set_ylabel('Velocity (fps)', fontsize=10, fontweight='bold')
ax_good_2.set_xlabel('Charge Weight (grains)', fontsize=10, fontweight='bold')
ax_good_2.set_title('GOOD: Realistic Scatter\nNormal variation around trend',
                    fontsize=11, fontweight='bold', color='green')
ax_good_2.grid(True, alpha=0.3, linestyle=':', linewidth=0.5)

# Bad: Perfect staircase
bad_velocities = 2700 + 25 * (charges - 40.0)  # Perfectly linear, no variation
ax_bad_2.plot(charges, bad_velocities, 'o-', color='red', markersize=10,
              linewidth=2, markeredgecolor='darkred', markeredgewidth=1.5)
ax_bad_2.set_ylabel('Velocity (fps)', fontsize=10, fontweight='bold')
ax_bad_2.set_xlabel('Charge Weight (grains)', fontsize=10, fontweight='bold')
ax_bad_2.set_title('RED FLAG: Perfect Staircase\nNo variation? Too perfect to be real!',
                   fontsize=11, fontweight='bold', color='darkred')
ax_bad_2.grid(True, alpha=0.3, linestyle=':', linewidth=0.5)

# Example 3: SD measurements - uncertainty vs exact values
ax_good_3 = axes[2, 0]
ax_bad_3 = axes[2, 1]

# Good: With error bars showing uncertainty
loads = ['Load A', 'Load B', 'Load C', 'Load D']
np.random.seed(42)
good_sds = [12.5, 14.2, 11.8, 13.6]
good_errors = [2.1, 2.3, 2.0, 2.2]  # Realistic uncertainty

ax_good_3.bar(loads, good_sds, color='steelblue', edgecolor='black',
              linewidth=1.5, alpha=0.7, yerr=good_errors, capsize=5,
              error_kw={'linewidth': 2, 'ecolor': 'black'})
ax_good_3.set_ylabel('Velocity SD (fps)', fontsize=10, fontweight='bold')
ax_good_3.set_xlabel('Load', fontsize=10, fontweight='bold')
ax_good_3.set_title('GOOD: Shows Uncertainty\nError bars = honest data',
                    fontsize=11, fontweight='bold', color='green')
ax_good_3.set_ylim([0, 20])
ax_good_3.grid(True, alpha=0.3, linestyle=':', linewidth=0.5, axis='y')
ax_good_3.text(0.5, 0.95, 'Sample size: 30 shots\nWith 95% confidence intervals',
               transform=ax_good_3.transAxes, fontsize=8, ha='center', va='top',
               bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.6))

# Bad: Suspiciously exact values
bad_sds = [8.0, 8.0, 8.0, 8.0]  # Exactly the same - unrealistic

ax_bad_3.bar(loads, bad_sds, color='red', edgecolor='black',
             linewidth=1.5, alpha=0.7)
ax_bad_3.set_ylabel('Velocity SD (fps)', fontsize=10, fontweight='bold')
ax_bad_3.set_xlabel('Load', fontsize=10, fontweight='bold')
ax_bad_3.set_title('RED FLAG: Exactly 8.0 fps\nEvery test? Unrealistic precision!',
                   fontsize=11, fontweight='bold', color='darkred')
ax_bad_3.set_ylim([0, 20])
ax_bad_3.grid(True, alpha=0.3, linestyle=':', linewidth=0.5, axis='y')
ax_bad_3.text(0.5, 0.95, 'Claims: "All loads exactly 8 fps SD"\nNo error bars, no uncertainty',
              transform=ax_bad_3.transAxes, fontsize=8, ha='center', va='top',
              bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.6))

# Add explanatory annotations
explanation_good = (
    'Signs of GOOD data:\n'
    '• Realistic variance\n'
    '• Uncertainty shown\n'
    '• Large sample sizes\n'
    '• Multiple groups reported\n'
    '• Average emphasized\n'
    '• Error bars included'
)

explanation_bad = (
    'RED FLAGS:\n'
    '• Too perfect/consistent\n'
    '• No uncertainty\n'
    '• Small sample sizes\n'
    '• Cherry-picked "best"\n'
    '• Point estimates only\n'
    '• Bold claims from few shots'
)

fig.text(0.02, 0.02, explanation_good, fontsize=10,
         verticalalignment='bottom', horizontalalignment='left',
         bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7),
         fontweight='bold')

fig.text(0.98, 0.02, explanation_bad, fontsize=10,
         verticalalignment='bottom', horizontalalignment='right',
         bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7),
         fontweight='bold')

# Overall title
fig.suptitle('Data Quality Red Flag Gallery: Learn to Spot Questionable Claims\n'
             'Left Column = Good Honest Data | Right Column = Suspicious Red Flags',
             fontsize=14, fontweight='bold', y=0.98)

# Add warning banner
warning_text = (
    'CRITICAL THINKING REQUIRED: When evaluating online load data, forum posts, or published results,\n'
    'look for realistic variation, proper sample sizes, error bars, and honest uncertainty.\n'
    'Beware of suspiciously perfect data, cherry-picked "best groups", and bold claims from tiny samples!'
)

fig.text(0.5, 0.005, warning_text, fontsize=9,
         verticalalignment='bottom', horizontalalignment='center',
         bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.8),
         style='italic', fontweight='bold')

# Tight layout
plt.tight_layout(rect=[0, 0.06, 1, 0.96])

# Save the figure
output_path = Path(__file__).parent.parent / 'lessons' / 'static' / 'nb11_plot23_red_flag_gallery.png'
output_path.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Saved: {output_path}")

# Also display if running interactively
# plt.show()
