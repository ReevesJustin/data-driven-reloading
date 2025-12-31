#================================================
# TEMPLATE A: TWO-LOAD COMPARISON
# Purpose: Compare velocity performance of two loads
#================================================

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Set plot style for clarity
plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams['figure.figsize'] = (14, 10)
plt.rcParams['font.size'] = 11

#================================================
# YOUR DATA GOES HERE
#================================================

# Option 1: Paste data directly (recommended for quick tests)
data_text = """
Shot,Load,Velocity
1,CCI,2850
2,CCI,2855
3,CCI,2848
4,CCI,2852
5,CCI,2851
6,CCI,2849
7,CCI,2853
8,CCI,2850
9,CCI,2854
10,CCI,2847
11,CCI,2852
12,CCI,2851
13,CCI,2850
14,CCI,2856
15,CCI,2849
16,CCI,2851
17,CCI,2853
18,CCI,2850
19,CCI,2848
20,CCI,2852
21,CCI,2851
22,CCI,2850
23,CCI,2854
24,CCI,2849
25,CCI,2852
26,CCI,2851
27,CCI,2853
28,CCI,2850
29,CCI,2855
30,CCI,2848
31,Federal,2863
32,Federal,2858
33,Federal,2861
34,Federal,2860
35,Federal,2862
36,Federal,2859
37,Federal,2861
38,Federal,2863
39,Federal,2860
40,Federal,2859
41,Federal,2862
42,Federal,2861
43,Federal,2860
44,Federal,2864
45,Federal,2859
46,Federal,2861
47,Federal,2862
48,Federal,2860
49,Federal,2858
50,Federal,2863
51,Federal,2861
52,Federal,2860
53,Federal,2862
54,Federal,2859
55,Federal,2861
56,Federal,2863
57,Federal,2862
58,Federal,2860
59,Federal,2861
60,Federal,2859
"""

# Load data from text
from io import StringIO
data = pd.read_csv(StringIO(data_text))

# Option 2: Load from CSV file (for larger datasets)
# data = pd.read_csv('your_file.csv')

#================================================
# AUTOMATIC ANALYSIS - DON'T MODIFY BELOW
#================================================

# Split data by load type
loads = data['Load'].unique()
if len(loads) != 2:
    print(f"ERROR: Expected 2 loads, found {len(loads)}: {loads}")
    print("This template is for comparing TWO loads. Check your data.")
else:
    load1_name = loads[0]
    load2_name = loads[1]

    load1_data = data[data['Load'] == load1_name]['Velocity']
    load2_data = data[data['Load'] == load2_name]['Velocity']

    # Calculate statistics
    load1_mean = load1_data.mean()
    load1_std = load1_data.std()
    load1_n = len(load1_data)
    load1_sem = load1_std / np.sqrt(load1_n)  # Standard error of mean
    load1_ci = 1.96 * load1_sem  # 95% confidence interval

    load2_mean = load2_data.mean()
    load2_std = load2_data.std()
    load2_n = len(load2_data)
    load2_sem = load2_std / np.sqrt(load2_n)
    load2_ci = 1.96 * load2_sem

    # Statistical test
    t_stat, p_value = stats.ttest_ind(load1_data, load2_data)

    # Effect size (Cohen's d)
    pooled_std = np.sqrt(((load1_n - 1) * load1_std**2 + (load2_n - 1) * load2_std**2) / (load1_n + load2_n - 2))
    cohens_d = (load2_mean - load1_mean) / pooled_std

    # Create comprehensive visualization
    fig = plt.figure(figsize=(16, 12))
    gs = fig.add_gridspec(3, 2, hspace=0.3, wspace=0.3)

    # Plot 1: Histograms
    ax1 = fig.add_subplot(gs[0, :])
    bins = np.linspace(min(load1_data.min(), load2_data.min()),
                       max(load1_data.max(), load2_data.max()), 20)
    ax1.hist(load1_data, bins=bins, alpha=0.6, label=f'{load1_name} (n={load1_n})',
             color='steelblue', edgecolor='black')
    ax1.hist(load2_data, bins=bins, alpha=0.6, label=f'{load2_name} (n={load2_n})',
             color='coral', edgecolor='black')
    ax1.axvline(load1_mean, color='steelblue', linestyle='--', linewidth=2,
                label=f'{load1_name} mean: {load1_mean:.1f} fps')
    ax1.axvline(load2_mean, color='coral', linestyle='--', linewidth=2,
                label=f'{load2_name} mean: {load2_mean:.1f} fps')
    ax1.set_xlabel('Velocity (fps)', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Frequency', fontsize=12, fontweight='bold')
    ax1.set_title('Velocity Distributions', fontsize=14, fontweight='bold')
    ax1.legend(fontsize=10)
    ax1.grid(alpha=0.3)

    # Plot 2: Box plots with individual points
    ax2 = fig.add_subplot(gs[1, 0])
    positions = [1, 2]
    bp = ax2.boxplot([load1_data, load2_data], positions=positions, widths=0.6,
                     patch_artist=True, showmeans=True,
                     boxprops=dict(facecolor='lightblue', alpha=0.7),
                     medianprops=dict(color='red', linewidth=2),
                     meanprops=dict(marker='D', markerfacecolor='green', markersize=8))

    # Overlay individual points
    for i, load_data in enumerate([load1_data, load2_data], 1):
        y = load_data
        x = np.random.normal(i, 0.04, size=len(y))  # Add jitter for visibility
        ax2.scatter(x, y, alpha=0.4, s=30, color='black')

    ax2.set_xticks(positions)
    ax2.set_xticklabels([load1_name, load2_name], fontweight='bold')
    ax2.set_ylabel('Velocity (fps)', fontsize=12, fontweight='bold')
    ax2.set_title('Velocity Distributions (Box Plot)', fontsize=14, fontweight='bold')
    ax2.grid(axis='y', alpha=0.3)

    # Plot 3: Means with error bars (95% CI)
    ax3 = fig.add_subplot(gs[1, 1])
    ax3.errorbar([1], [load1_mean], yerr=[load1_ci], fmt='o', markersize=12,
                 capsize=10, capthick=2, color='steelblue', label=f'{load1_name}')
    ax3.errorbar([2], [load2_mean], yerr=[load2_ci], fmt='o', markersize=12,
                 capsize=10, capthick=2, color='coral', label=f'{load2_name}')
    ax3.set_xlim(0.5, 2.5)
    ax3.set_xticks([1, 2])
    ax3.set_xticklabels([load1_name, load2_name], fontweight='bold')
    ax3.set_ylabel('Mean Velocity (fps)', fontsize=12, fontweight='bold')
    ax3.set_title('Mean Velocities with 95% Confidence Intervals', fontsize=14, fontweight='bold')
    ax3.legend(fontsize=10)
    ax3.grid(axis='y', alpha=0.3)

    # Plot 4: Sequential plot (velocity over shots)
    ax4 = fig.add_subplot(gs[2, :])
    load1_shots = data[data['Load'] == load1_name]['Shot']
    load2_shots = data[data['Load'] == load2_name]['Shot']
    ax4.scatter(load1_shots, load1_data, alpha=0.7, s=50, color='steelblue', label=load1_name)
    ax4.scatter(load2_shots, load2_data, alpha=0.7, s=50, color='coral', label=load2_name)
    ax4.axhline(load1_mean, color='steelblue', linestyle='--', alpha=0.5, linewidth=1.5)
    ax4.axhline(load2_mean, color='coral', linestyle='--', alpha=0.5, linewidth=1.5)
    ax4.set_xlabel('Shot Number', fontsize=12, fontweight='bold')
    ax4.set_ylabel('Velocity (fps)', fontsize=12, fontweight='bold')
    ax4.set_title('Velocity Over Shot Sequence', fontsize=14, fontweight='bold')
    ax4.legend(fontsize=10)
    ax4.grid(alpha=0.3)

    plt.suptitle('Two-Load Velocity Comparison Analysis', fontsize=16, fontweight='bold', y=0.995)
    plt.tight_layout()
    plt.show()

    #================================================
    # STATISTICAL SUMMARY
    #================================================

    print("=" * 80)
    print(" STATISTICAL SUMMARY")
    print("=" * 80)
    print()
    print(f"{'Load':<15} {'n':<6} {'Mean (fps)':<12} {'SD (fps)':<10} {'ES (fps)':<10} {'95% CI':<20}")
    print("-" * 80)
    print(f"{load1_name:<15} {load1_n:<6} {load1_mean:>10.1f}   {load1_std:>8.1f}   "
          f"{load1_data.max() - load1_data.min():>8.0f}   ±{load1_ci:.1f} fps")
    print(f"{load2_name:<15} {load2_n:<6} {load2_mean:>10.1f}   {load2_std:>8.1f}   "
          f"{load2_data.max() - load2_data.min():>8.0f}   ±{load2_ci:.1f} fps")
    print()

    print("=" * 80)
    print(" COMPARISON")
    print("=" * 80)
    print()
    print(f"Difference in means: {abs(load2_mean - load1_mean):.1f} fps")
    print(f"  ({load2_name} is {'faster' if load2_mean > load1_mean else 'slower'} than {load1_name})")
    print()
    print(f"Difference in SD: {abs(load2_std - load1_std):.1f} fps")
    print(f"  ({load2_name} has {'more' if load2_std > load1_std else 'less'} spread than {load1_name})")
    print()
    print(f"T-test p-value: {p_value:.4f}")
    print(f"  (p < 0.05 suggests a statistically significant difference)")
    print()
    print(f"Effect size (Cohen's d): {abs(cohens_d):.3f}")
    print(f"  (< 0.2 = tiny, 0.2-0.5 = small, 0.5-0.8 = medium, > 0.8 = large)")
    print()

    #================================================
    # INTERPRETATION (PLAIN ENGLISH)
    #================================================

    print("=" * 80)
    print(" INTERPRETATION")
    print("=" * 80)
    print()

    # Velocity difference
    if abs(load2_mean - load1_mean) < 5:
        print(f"✓ Velocity difference is NEGLIGIBLE ({abs(load2_mean - load1_mean):.1f} fps)")
        print(f"  This won't matter at any practical distance.")
    elif abs(load2_mean - load1_mean) < 15:
        print(f"⚠ Velocity difference is SMALL ({abs(load2_mean - load1_mean):.1f} fps)")
        print(f"  Might matter at extreme long range (1000+ yards), irrelevant otherwise.")
    else:
        print(f"★ Velocity difference is MEANINGFUL ({abs(load2_mean - load1_mean):.1f} fps)")
        print(f"  This will affect trajectory at long range.")
    print()

    # SD difference
    if abs(load2_std - load1_std) < 2:
        print(f"✓ SD difference is NEGLIGIBLE ({abs(load2_std - load1_std):.1f} fps)")
        print(f"  Both loads have essentially the same consistency.")
    elif abs(load2_std - load1_std) < 5:
        print(f"⚠ SD difference is SMALL ({abs(load2_std - load1_std):.1f} fps)")
        print(f"  Slight difference, but both are reasonably consistent.")
    else:
        print(f"★ SD difference is MEANINGFUL ({abs(load2_std - load1_std):.1f} fps)")
        print(f"  {load2_name if load2_std < load1_std else load1_name} is noticeably more consistent.")
    print()

    # Statistical significance
    if p_value < 0.05:
        print(f"★ The difference is STATISTICALLY SIGNIFICANT (p = {p_value:.4f})")
        print(f"  With {load1_n + load2_n} total shots, this difference is unlikely to be random chance.")
    else:
        print(f"✓ The difference is NOT statistically significant (p = {p_value:.4f})")
        print(f"  This difference could easily be random variation.")
    print()

    # Practical significance
    if abs(cohens_d) < 0.2:
        print(f"✓ Effect size is TINY (d = {abs(cohens_d):.3f})")
        print(f"  Even if statistically significant, the practical difference is minimal.")
    elif abs(cohens_d) < 0.5:
        print(f"⚠ Effect size is SMALL (d = {abs(cohens_d):.3f})")
        print(f"  Detectable difference, but not dramatic.")
    else:
        print(f"★ Effect size is MEDIUM or LARGE (d = {abs(cohens_d):.3f})")
        print(f"  This is a substantial, practically meaningful difference.")
    print()

    #================================================
    # DECISION GUIDANCE
    #================================================

    print("=" * 80)
    print(" RECOMMENDATION")
    print("=" * 80)
    print()

    # Decision logic
    if p_value >= 0.05 or abs(cohens_d) < 0.2:
        print("➤ VERDICT: No meaningful difference detected")
        print()
        print(f"  The data shows no reliable difference between {load1_name} and {load2_name}.")
        print(f"  Either would work fine. Choose based on:")
        print(f"    - Cost (use cheaper option)")
        print(f"    - Availability (use easier to find)")
        print(f"    - Other factors (temperature stability, brass life, etc.)")
        print()
        print(f"  No need to switch if you're currently using {load1_name}.")
    elif p_value < 0.05 and abs(cohens_d) >= 0.2 and abs(cohens_d) < 0.5:
        print("➤ VERDICT: Small but real difference detected")
        print()
        faster_load = load2_name if load2_mean > load1_mean else load1_name
        more_consistent = load2_name if load2_std < load1_std else load1_name
        print(f"  {faster_load} is faster.")
        print(f"  {more_consistent} is more consistent.")
        print()
        print(f"  This difference is real but not huge. Switch if:")
        print(f"    - You shoot long range (>600 yards) where velocity matters")
        print(f"    - The better load is the same price")
        print(f"    - You want every edge for competition")
        print()
        print(f"  Stick with {load1_name} if you're just hunting or shooting casually.")
    else:
        print("➤ VERDICT: Clear, meaningful difference detected")
        print()
        better_load = load2_name if (load2_mean > load1_mean and load2_std <= load1_std) else load1_name
        print(f"  {better_load} is the clear winner.")
        print(f"  The difference is large enough to matter in practical shooting.")
        print()
        print(f"  RECOMMENDATION: Switch to {better_load} if you're not using it already.")

    print()
    print("=" * 80)
    print(" ANALYSIS COMPLETE")
    print("=" * 80)