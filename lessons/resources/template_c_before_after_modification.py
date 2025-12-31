#================================================
# TEMPLATE C: BEFORE/AFTER MODIFICATION
# Purpose: Evaluate impact of a single change
#================================================

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams['figure.figsize'] = (14, 10)

#================================================
# YOUR DATA GOES HERE
#================================================

data_text = """
Shot,Condition,Velocity
1,Before,2850
2,Before,2855
3,Before,2848
4,Before,2852
5,Before,2851
6,Before,2849
7,Before,2853
8,Before,2850
9,Before,2854
10,Before,2847
11,After,2848
12,After,2853
13,After,2846
14,After,2851
15,After,2850
16,After,2847
17,After,2852
18,After,2849
19,After,2853
20,After,2846
"""

from io import StringIO
data = pd.read_csv(StringIO(data_text))

before = data[data['Condition'] == 'Before']['Velocity']
after = data[data['Condition'] == 'After']['Velocity']

# Statistics
before_mean, before_std = before.mean(), before.std()
after_mean, after_std = after.mean(), after.std()

# Statistical test (paired if same barrel/conditions, independent otherwise)
t_stat, p_value = stats.ttest_ind(before, after)

# Create plots
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Before/After Modification Analysis', fontsize=16, fontweight='bold')

# Distributions
axes[0, 0].hist(before, bins=15, alpha=0.6, label='Before', color='gray')
axes[0, 0].hist(after, bins=15, alpha=0.6, label='After', color='green')
axes[0, 0].axvline(before_mean, color='gray', linestyle='--', linewidth=2)
axes[0, 0].axvline(after_mean, color='green', linestyle='--', linewidth=2)
axes[0, 0].set_xlabel('Velocity (fps)')
axes[0, 0].set_ylabel('Frequency')
axes[0, 0].set_title('Velocity Distributions')
axes[0, 0].legend()
axes[0, 0].grid(alpha=0.3)

# Box plot comparison
axes[0, 1].boxplot([before, after], labels=['Before', 'After'], patch_artist=True)
axes[0, 1].set_ylabel('Velocity (fps)')
axes[0, 1].set_title('Before vs After Comparison')
axes[0, 1].grid(axis='y', alpha=0.3)

# Sequential plot
axes[1, 0].plot(range(1, len(before)+1), before, 'o-', alpha=0.7, label='Before', color='gray')
axes[1, 0].plot(range(len(before)+1, len(before)+len(after)+1), after, 'o-', alpha=0.7, label='After', color='green')
axes[1, 0].axhline(before_mean, color='gray', linestyle='--', alpha=0.5)
axes[1, 0].axhline(after_mean, color='green', linestyle='--', alpha=0.5)
axes[1, 0].set_xlabel('Shot Number')
axes[1, 0].set_ylabel('Velocity (fps)')
axes[1, 0].set_title('Velocity Over Time')
axes[1, 0].legend()
axes[1, 0].grid(alpha=0.3)

# Difference plot
axes[1, 1].bar(['Mean Velocity', 'SD'],
               [after_mean - before_mean, after_std - before_std],
               color=['green' if after_mean > before_mean else 'red',
                      'green' if after_std < before_std else 'red'])
axes[1, 1].axhline(0, color='black', linestyle='-', linewidth=1)
axes[1, 1].set_ylabel('Change (After - Before)')
axes[1, 1].set_title('Impact of Modification')
axes[1, 1].grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.show()

# Print summary
print("=" * 80)
print(" BEFORE/AFTER SUMMARY")
print("=" * 80)
print()
print(f"{'Condition':<12} {'n':<6} {'Mean':<10} {'SD':<8}")
print("-" * 80)
print(f"{'Before':<12} {len(before):<6} {before_mean:<10.1f} {before_std:<8.1f}")
print(f"{'After':<12} {len(after):<6} {after_mean:<10.1f} {after_std:<8.1f}")
print()
print(f"Change in mean: {after_mean - before_mean:+.1f} fps")
print(f"Change in SD: {after_std - before_std:+.1f} fps")
print(f"P-value: {p_value:.4f}")
print()

# Interpretation
if p_value >= 0.05:
    print("➤ VERDICT: No significant difference detected")
    print("  The modification had no measurable effect.")
else:
    if abs(after_mean - before_mean) < 10 and abs(after_std - before_std) < 3:
        print("➤ VERDICT: Statistically significant but practically small")
        print("  The change is real but probably not worth worrying about.")
    else:
        print("➤ VERDICT: Significant and meaningful difference")
        print("  The modification had a real, measurable effect.")

print()
print("=" * 80)