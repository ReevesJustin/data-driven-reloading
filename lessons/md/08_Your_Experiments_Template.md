Time to complete: 15-20 minutes (one-time setup, then reuse forever)

# Your Experiments Template

## From Theory to Practice: Tools You'll Actually Use

You've made it this far. You understand:
- Why small samples lie (Lesson 01)
- What consistency really means (Lesson 02)
- How many shots you need (Lesson 03)
- How to test one variable at a time (Lesson 04)
- How to analyze velocity data (Lesson 05)
- How to evaluate group size properly (Lesson 06)
- How to recognize common myths (Lesson 07)

**Now it's time to put that knowledge to work.**

This lesson is different. This isn't theory. This isn't examples of what someone else did. This is YOUR toolkit—production-ready templates you'll copy, customize with your data, and use to analyze every test you run from now on.

By the end of this lesson, you'll have three complete templates saved and ready to use:

1. **Template A: Two-Load Comparison** - Compare any two loads (primers, powders, bullets, etc.)
2. **Template B: Charge Weight Ladder** - Test multiple powder charges systematically
3. **Template C: Before/After Modification** - Evaluate any component change

Each template includes:
- CSV data format (copy/paste your numbers)
- Complete analysis code (just click "Run All")
- Auto-generated plots (publication-quality, ready to share)
- Statistical interpretation (plain English, no guessing)
- Decision guidance ("Keep the change" vs "Revert to baseline")

**This is the payoff.** Everything you've learned becomes immediately actionable.

Let's get started.

---

## Choose Your Format: Python or Excel

These templates are available in **two formats** - choose the one that works best for you:

### Option 1: Excel Templates (Recommended for Most Users)

**Best for:** Anyone comfortable with Excel, users who want zero programming

**Download:**
- [Blank Templates (Start Here)](../templates/Reloading_Analysis_Templates.xlsx) - Empty templates ready for your data
- [Example Templates](../templates/Reloading_Analysis_Templates_Examples.xlsx) - Pre-filled with sample data to see how they work
- [Case Data Template](../templates/Reloading_Analysis_CaseData_Template.csv) - Pre-filled template for measuring and analyzing case dimensions, masses, and capacities

**Advantages:**
- ✓ No programming knowledge required
- ✓ Works offline in Microsoft Excel (2016+) or Google Sheets
- ✓ Familiar spreadsheet interface
- ✓ Easy to save and share completed analyses
- ✓ Protected formulas (hard to break accidentally)
- ✓ All calculations automatic
- ✓ Plain-English interpretations
- ✓ Password to modify formulas: `reloading`

**How to Use:**
1. Download the blank templates file
2. Open in Excel (Windows/Mac) or Google Sheets
3. Choose your template sheet (Template_A, Template_B, or Template_C)
4. Paste your data in columns A-C
5. Read the auto-generated analysis
6. Save with a descriptive name (e.g., "2024-03-15_Primer_Test.xlsx")

**See:** [Templates README](../templates/README.md) for complete documentation

### Option 2: Python/Jupyter Notebooks (Original)

**Best for:** Python users, researchers who need full customization, those running many analyses

**Advantages:**
- ✓ Full control over all code and calculations
- ✓ Easy to modify and extend
- ✓ Publication-quality charts (4 per template)
- ✓ Can automate batch processing
- ✓ Reproducible research workflows

**Requirements:**
- Python 3.x
- Jupyter notebook or Google Colab
- Libraries: pandas, matplotlib, numpy, scipy

**How to Use:**
- See the Python code blocks below
- Copy into Jupyter or Colab
- Run the cells
- Modify as needed

---

**For the rest of this lesson, we'll show both formats side-by-side where applicable.**

**Most users should start with the Excel templates and only use Python if they have specific needs for customization.**

---

## How to Use These Templates

### The Three-Step Process

**Step 1: Copy the Template**
- Save this notebook to your own account (File → Save a Copy)
- Or download as .ipynb and open in Jupyter locally

**Step 2: Enter Your Data**
- Find the "YOUR DATA GOES HERE" section
- Paste your chronograph readings or group measurements
- Change the labels (e.g., "CCI" and "Federal" to whatever you're testing)

**Step 3: Run and Interpret**
- Click "Runtime → Run All" (in Colab) or "Kernel → Restart & Run All" (in Jupyter)
- Scroll down to see your plots and statistics
- Read the auto-generated interpretation
- Make your decision based on the data

**That's it.** No programming required. No statistical knowledge needed. The templates do the work.

---

## Template A: Two-Load Comparison

**Use this template when you're comparing two options:**
- CCI primers vs Federal primers
- H4350 powder vs Varget powder
- Sierra bullets vs Berger bullets
- Load A vs Load B

### Data Format

Your data should look like this (CSV format):

```csv
Shot,Load,Velocity
1,Load_A,2850
2,Load_A,2855
3,Load_A,2848
...
30,Load_A,2852
31,Load_B,2863
32,Load_B,2858
...
60,Load_B,2861
```

**Column explanations:**
- **Shot:** Just number them 1, 2, 3, ... (keeps track of order)
- **Load:** Name of what you're testing (e.g., "CCI" and "Federal", or "Load_A" and "Load_B")
- **Velocity:** Chronograph reading in fps

### Complete Working Code

```python
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
```

### How to Use This Template

1. **Replace the example data** in the `data_text` section with your chronograph readings
2. **Update the load names** (change "CCI" and "Federal" to whatever you're testing)
3. **Run the code** (click "Run All")
4. **Review the plots** - Visual comparison of your loads
5. **Read the interpretation** - Plain English explanation
6. **Follow the recommendation** - Clear decision guidance

That's it. The template does all the statistical work for you.

---

## Template B: Charge Weight Ladder Test

**Use this template when testing multiple powder charges:**
- Finding optimal charge weight
- Testing 3-6 different charge weights
- Looking for accuracy or velocity patterns

### Data Format

```csv
Shot,Charge,Velocity
1,41.0,2720
2,41.0,2725
3,41.0,2718
...
11,41.5,2750
12,41.5,2755
...
```

### Complete Working Code

```python
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
```

### Key Warnings for Ladder Tests

**IMPORTANT:** Ladder tests with small samples (< 20 shots per charge) are notoriously unreliable. What looks like a "velocity node" or "flat spot" is usually just random variation.

**This template will:**
- Show you the data honestly
- Warn you about small sample sizes
- Help you avoid seeing patterns that aren't really there

**Use this for initial screening only.** Once you find a promising charge, validate it with 30+ shots before trusting it.

---

## Template C: Before/After Modification Test

**Use this when evaluating a single component change:**
- Before and after barrel cleaning
- Before and after adding a tuner
- Before and after switching brass lots
- Baseline vs modified load

### Data Format

```csv
Shot,Condition,Velocity
1,Before,2850
2,Before,2855
...
30,Before,2852
31,After,2848
32,After,2853
...
60,After,2851
```

### Complete Working Code

```python
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
```

---

## Tips for Using These Templates

### Best Practices

1. **Keep a Testing Logbook**
   - Save each completed template with a descriptive name
   - Example: "2024-03-15_CCI_vs_Federal_Primers.ipynb"
   - Include notes about conditions (temp, wind, barrel fouling)

2. **Don't Cherry-Pick Data**
   - Include ALL shots, even flyers
   - Note unusual shots in the "Notes" column but don't delete them
   - Let the statistics handle outliers

3. **Test in Consistent Conditions**
   - Same day, same temperature if possible
   - Same barrel condition (clean vs fouled)
   - Alternate between conditions to average out barrel heating

4. **Document Everything**
   - Lot numbers for components
   - Environmental conditions
   - Rifle configuration
   - Any anomalies during testing

5. **Share Your Results Properly**
   - Include sample sizes
   - Show the plots
   - Report confidence intervals, not just means
   - Be honest about limitations

### Common Pitfalls to Avoid

**Pitfall 1: Stopping Early**
"The first 5 shots looked great, so I stopped testing."
**Fix:** Complete your planned sample size. One good group means nothing.

**Pitfall 2: Unequal Sample Sizes**
"I shot 30 rounds of Load A but only 15 of Load B."
**Fix:** Equal samples for fair comparison. Always.

**Pitfall 3: Mixing Conditions**
"I tested Load A on Monday and Load B on Thursday."
**Fix:** Test both on the same day when possible.

**Pitfall 4: Ignoring Sample Size Requirements**
"I tested 3 charges with 10 shots each."
**Fix:** 10 shots is inadequate for SD comparison. Use 30 minimum.

**Pitfall 5: Over-Interpreting Small Differences**
"Load B was 2 fps faster, so it's better!"
**Fix:** Read the interpretation section. The template will tell you if differences matter.

---

## Saving and Reusing Templates

### For Google Colab Users

1. **Save a copy:** File → Save a copy in Drive
2. **Organize:** Create a folder called "Reloading Tests"
3. **Reuse:** Copy the blank template for each new test

### For Local Jupyter Users

1. **Save as:** File → Save As → Choose descriptive name
2. **Keep a master:** Save one blank copy as "Template_MASTER.ipynb"
3. **Copy for each test:** Make a copy before entering data

### Creating Your Own Library

After a few tests, you'll have a collection:
```
Reloading_Tests/
├── Template_MASTER_TwoLoad.ipynb
├── Template_MASTER_Ladder.ipynb
├── Template_MASTER_BeforeAfter.ipynb
├── 2024-03-15_CCI_vs_Federal.ipynb
├── 2024-03-22_H4350_Charge_Test.ipynb
├── 2024-04-05_Berger_vs_Sierra.ipynb
└── ...
```

This becomes your testing journal—a record of what you tested, when, and what you learned.

---

## You're Ready

You now have three production-ready templates that handle:
- Comparing two loads
- Testing charge weights
- Evaluating modifications

These templates do all the hard work:
- Statistical calculations
- Professional visualizations
- Plain English interpretations
- Clear decision guidance

**No more guessing. No more relying on "feel." No more chasing internet myths.**

From now on, when you test something, you'll:
1. Enter your data
2. Click "Run All"
3. Get a definitive answer

This is the culmination of everything you've learned. You understand the theory, you recognize the traps, and now you have the tools to test properly.

The next lesson will help you set realistic expectations so you don't chase perfection that doesn't exist. But first, spend some time with these templates. Copy them. Test something this weekend. See how empowering it is to actually KNOW instead of guess.

> **Key Takeaways**
> - Three production-ready templates cover most testing needs
> - Copy, paste data, run—no programming required
> - Auto-generated plots show your data clearly
> - Plain English interpretation removes guesswork
> - Decision guidance tells you what to do next
> - Save completed tests to build your testing library
> - Equal sample sizes, honest data inclusion, same-day testing

---

## Coming Up Next

**In Lesson 09: Reasonable Expectations**, you'll learn:
- What precision is actually achievable (not internet fantasy)
- The three contributors to dispersion (rifle, shooter, recoil)
- Why recoil is the biggest disruptor nobody talks about
- WEZ thinking: Hit probability matters more than tiny groups
- Realistic benchmarks for different rifle/ammo combinations

Now that you can test properly and analyze rigorously, we need to make sure you're chasing realistic goals. No more thinking you "should" shoot 0.25 MOA because someone on the internet said so.

[Previous: 07 Real Examples - Dissecting Common Myths](<07_Real_Examples_-_Dissecting_Common_Myths.html>) | [Next: 09 Reasonable Expectations - What Real Precision Looks Like](<09_Reasonable_Expectations_-_What_Real_Precision_Looks_Like.html>)
