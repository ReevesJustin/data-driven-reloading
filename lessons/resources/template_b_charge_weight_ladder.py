#================================================
# TEMPLATE B: CHARGE WEIGHT LADDER
# Purpose: Compare multiple powder charges
#================================================

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams['figure.figsize'] = (16, 10)
plt.rcParams['font.size'] = 11

#================================================
# YOUR DATA GOES HERE
#================================================

data_text = """
Shot,Charge,Velocity
1,41.0,2720
2,41.0,2725
3,41.0,2718
4,41.0,2722
5,41.0,2721
6,41.0,2719
7,41.0,2723
8,41.0,2720
9,41.0,2724
10,41.0,2718
11,41.5,2750
12,41.5,2755
13,41.5,2748
14,41.5,2752
15,41.5,2751
16,41.5,2749
17,41.5,2753
18,41.5,2750
19,41.5,2754
20,41.5,2748
21,42.0,2780
22,42.0,2785
23,42.0,2778
24,42.0,2782
25,42.0,2781
26,42.0,2779
27,42.0,2783
28,42.0,2780
29,42.0,2784
30,42.0,2778
"""

from io import StringIO
data = pd.read_csv(StringIO(data_text))

# Calculate statistics per charge
charges = sorted(data['Charge'].unique())
results = []

for charge in charges:
    subset = data[data['Charge'] == charge]['Velocity']
    results.append({
        'Charge': charge,
        'n': len(subset),
        'Mean': subset.mean(),
        'SD': subset.std(),
        'ES': subset.max() - subset.min(),
        'Min': subset.min(),
        'Max': subset.max()
    })

results_df = pd.DataFrame(results)

# Create visualization
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Charge Weight Ladder Analysis', fontsize=16, fontweight='bold')

# Plot 1: Mean velocity vs charge
ax1 = axes[0, 0]
ax1.errorbar(results_df['Charge'], results_df['Mean'],
             yerr=1.96 * results_df['SD'] / np.sqrt(results_df['n']),
             fmt='o-', markersize=10, capsize=8, capthick=2, linewidth=2, color='steelblue')
ax1.set_xlabel('Powder Charge (grains)', fontsize=12, fontweight='bold')
ax1.set_ylabel('Mean Velocity (fps)', fontsize=12, fontweight='bold')
ax1.set_title('Velocity vs Charge Weight (with 95% CI)', fontsize=14, fontweight='bold')
ax1.grid(True, alpha=0.3)

# Plot 2: SD vs charge
ax2 = axes[0, 1]
ax2.plot(results_df['Charge'], results_df['SD'], 'o-', markersize=10, linewidth=2, color='coral')
ax2.axhline(results_df['SD'].mean(), color='red', linestyle='--', alpha=0.5,
            label=f'Average SD: {results_df["SD"].mean():.1f} fps')
ax2.set_xlabel('Powder Charge (grains)', fontsize=12, fontweight='bold')
ax2.set_ylabel('Standard Deviation (fps)', fontsize=12, fontweight='bold')
ax2.set_title('Velocity Consistency vs Charge Weight', fontsize=14, fontweight='bold')
ax2.legend()
ax2.grid(True, alpha=0.3)

# Plot 3: Box plots
ax3 = axes[1, 0]
data_by_charge = [data[data['Charge'] == c]['Velocity'] for c in charges]
bp = ax3.boxplot(data_by_charge, labels=[f"{c:.1f}" for c in charges],
                 patch_artist=True, showmeans=True)
for patch in bp['boxes']:
    patch.set_facecolor('lightblue')
ax3.set_xlabel('Powder Charge (grains)', fontsize=12, fontweight='bold')
ax3.set_ylabel('Velocity (fps)', fontsize=12, fontweight='bold')
ax3.set_title('Velocity Distributions by Charge', fontsize=14, fontweight='bold')
ax3.grid(axis='y', alpha=0.3)

# Plot 4: All data points
ax4 = axes[1, 1]
for charge in charges:
    subset = data[data['Charge'] == charge]
    ax4.scatter([charge] * len(subset), subset['Velocity'], alpha=0.6, s=50)
ax4.plot(results_df['Charge'], results_df['Mean'], 'r-', linewidth=2, label='Mean')
ax4.set_xlabel('Powder Charge (grains)', fontsize=12, fontweight='bold')
ax4.set_ylabel('Velocity (fps)', fontsize=12, fontweight='bold')
ax4.set_title('All Individual Shots', fontsize=14, fontweight='bold')
ax4.legend()
ax4.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Print results table
print("=" * 80)
print(" CHARGE WEIGHT LADDER RESULTS")
print("=" * 80)
print()
print(f"{'Charge':<10} {'n':<6} {'Mean':<10} {'SD':<8} {'ES':<8} {'Min':<8} {'Max':<8}")
print("-" * 80)
for _, row in results_df.iterrows():
    print(f"{row['Charge']:<10.1f} {row['n']:<6.0f} {row['Mean']:<10.1f} "
          f"{row['SD']:<8.1f} {row['ES']:<8.0f} {row['Min']:<8.0f} {row['Max']:<8.0f}")
print()

# Interpretation
print("=" * 80)
print(" INTERPRETATION")
print("=" * 80)
print()

# Find best charge based on lowest SD
best_sd_idx = results_df['SD'].idxmin()
best_charge = results_df.loc[best_sd_idx, 'Charge']
best_sd = results_df.loc[best_sd_idx, 'SD']

print(f"Most consistent charge: {best_charge:.1f} grains (SD = {best_sd:.1f} fps)")
print()

# Check for velocity plateaus (fake "nodes")
velocity_increases = np.diff(results_df['Mean'])
avg_increase = velocity_increases.mean()
print(f"Average velocity increase per 0.5gr: {avg_increase:.1f} fps")
print()

# WARNING about sample size
if results_df['n'].min() < 20:
    print("⚠ WARNING: Some charges have less than 20 shots!")
    print("  With small samples, SD and patterns are unreliable.")
    print("  Consider testing top 2-3 charges with 30 shots each.")
print()

print("=" * 80)
print(" RECOMMENDATION")
print("=" * 80)
print()
print(f"Based on {results_df['n'].sum()} total shots:")
print(f"  Best overall: {best_charge:.1f} grains")
print()
print("Next steps:")
print("  1. Validate with 30+ shots at the best charge")
print("  2. Test group size at this charge weight")
print("  3. Check for pressure signs before using regularly")
print()
print("=" * 80)