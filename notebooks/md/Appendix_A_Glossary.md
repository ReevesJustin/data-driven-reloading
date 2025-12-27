# Glossary of Technical Terms

## How to Use This Glossary

This reference guide defines all technical terms used throughout the curriculum. Definitions are written in plain English at an 8th-grade reading level, with supporting formulas provided where applicable.

**Organization:** Alphabetical order
**Cross-references:** Terms reference the notebooks where they're discussed in detail
**Formulas:** Mathematical definitions appear after plain-English explanations

---

## A

### Accuracy

**Plain English:** How close your shots land to where you're aiming. Different from precision (consistency).

**Example:** If you aim at the bullseye and hit it, that's accurate. If you always hit the same spot but it's 2 inches left of the bullseye, that's precise but not accurate.

**Key distinction:** You can be precise without being accurate (consistent groups in the wrong place) or accurate without being precise (shots average on target but spread widely).

**See:** Notebook 06 - Group Size and Accuracy

---

### Alpha (α)

**Plain English:** The probability threshold you set for calling something "statistically significant." Commonly set at 0.05 (5%).

**Example:** If alpha = 0.05, you're saying "I'll accept a 5% risk of falsely claiming there's a difference when there isn't."

**Usage:** Lower alpha means stricter requirements for claiming significance.

**See:** Notebook 10 - When Is A Result Real

**Formula:**
```
α = P(rejecting null hypothesis | null hypothesis is true)
Commonly: α = 0.05 (5% false positive rate)
```

---

## B

### Barrel Harmonics

**Plain English:** The vibration pattern of a rifle barrel when a round is fired. The barrel flexes and whips as the bullet travels down it.

**The claim:** Some powder charges create "nodes" where harmonics minimize dispersion.

**The reality:** While harmonics exist, the claimed "nodes" from ladder tests are usually just random variation. See Notebook 07 for the debunking.

**See:** Notebook 07 - Real Examples (Velocity Nodes section)

---

### Bias

**Plain English:** A systematic error that makes measurements consistently wrong in one direction.

**Example:** Small samples systematically underestimate SD (they're biased optimistic). Three-shot groups systematically underestimate your rifle's true capability.

**Types:**
- **Optimistic bias:** Results look better than reality (small samples)
- **Confirmation bias:** Seeing what you expect instead of what's there
- **Selection bias:** Cherry-picking data that supports your conclusion

**See:** Notebooks 01, 03, 11

---

## C

### Central Limit Theorem (CLT)

**Plain English:** A mathematical law stating that when you take many samples and average them, those averages form a predictable bell curve pattern—even if the original data wasn't bell-curved.

**Why it matters:** This is why averages become reliable faster than spread measurements. It's the foundation for most statistical testing.

**Practical impact:** With just 10-15 shots, your average velocity is probably close to the true population mean.

**See:** Notebook 03 - How Many Shots Do You Really Need

---

### Chronograph

**Plain English:** A device that measures bullet velocity by timing how long it takes a bullet to pass between sensors.

**Common types:**
- Optical chronographs (use light screens)
- Doppler radar chronographs (track bullet speed downrange)

**Precision:** Budget models ±5-10 fps error, quality models ±2-3 fps error

**See:** Notebook 05 - Velocity Data (Chronograph Precision section)

---

### COAL (Cartridge Overall Length)

**Plain English:** The total length of a loaded cartridge from the base to the tip of the bullet.

**Why it matters:** COAL affects how much powder fits in the case (pressure) and how far the bullet "jumps" to the rifling (see Jump/Jam).

**Measurement:** Use a caliper, measure from case head to bullet tip.

**See:** Notebook 07 - Seating Depth section

---

### Confidence Interval (CI)

**Plain English:** A range that probably contains the true value you're trying to measure. Usually expressed as 95% confidence.

**Example:** "The true SD is 15 fps ± 3 fps (95% CI)" means you're 95% confident the real SD is between 12 and 18 fps.

**Key insight:** Smaller samples have wider confidence intervals (more uncertainty).

**See:** Notebook 03 - Sample Size sections

**Formula:**
```
For a mean:
CI = x̄ ± (t × SE)

Where:
x̄ = sample mean
t = t-distribution value for your confidence level
SE = standard error = SD / √n

Example (95% CI):
With n=30, SD=15 fps
SE = 15 / √30 = 2.74 fps
t ≈ 2.045 (for 29 df at 95%)
CI = x̄ ± (2.045 × 2.74) = x̄ ± 5.6 fps
```

---

### Confounded Variables

**Plain English:** When you change multiple things at once and can't tell which one caused the result.

**Example:** You switched primers AND powder. Your groups shrunk. Which change helped? You can't know—the variables are confounded.

**Solution:** Test one variable at a time.

**See:** Notebook 04 - Testing One Thing at a Time

---

## D

### Degrees of Freedom (df)

**Plain English:** A statistical concept representing how many independent pieces of information you have to estimate something.

**Practical meaning:** For most calculations, df = n - 1 (sample size minus 1).

**Why it matters:** Used in t-tests and other statistical tests to determine critical values.

**Formula:**
```
For single sample: df = n - 1
For two samples: df = n₁ + n₂ - 2
```

---

### DOPE (Data On Previous Engagements)

**Plain English:** A log of your ballistic data (drop, wind drift, etc.) at various ranges and conditions.

**Usage:** Precision shooters maintain DOPE books to quickly reference correct adjustments.

**Quality DOPE requires:** Accurate environmental data, proper ranging, consistent ammunition.

**See:** Notebook 04 - Environmental Control section

---

## E

### Extreme Spread (ES)

**Plain English:** The difference between your fastest and slowest shot in a sample.

**Example:** Velocities of 2,835, 2,848, 2,851, 2,846, 2,863 fps have ES = 2,863 - 2,835 = 28 fps

**Problem:** ES grows forever as you add shots. It can never shrink, only stay the same or increase. This makes it a poor metric for comparing loads unless sample sizes are identical.

**Better alternative:** Use Standard Deviation (SD) instead.

**See:** Notebook 05 - Velocity Data

**Formula:**
```
ES = max(velocity) - min(velocity)

For velocities: 2835, 2848, 2851, 2846, 2863 fps
ES = 2863 - 2835 = 28 fps
```

---

### Extreme Spread (Group Size)

**Plain English:** The maximum distance between any two shots in a group, measured center-to-center.

**Example:** If your widest two shots are 1.2 inches apart, your group ES is 1.2 inches.

**Problem:** Like velocity ES, this is dominated by the most extreme shots and is highly variable in small samples.

**Better alternative:** Use Mean Radius (MR) instead.

**See:** Notebook 06 - Group Size and Accuracy

**Formula:**
```
Group ES = maximum distance between any two shot centers

Converted to MOA:
MOA = (inches / distance in yards) × 100 / 1.047

Example: 1.2" group at 100 yards
MOA = (1.2 / 100) × 100 / 1.047 = 1.15 MOA
```

---

## F

### Factorial Experiment

**Plain English:** Testing all possible combinations of multiple variables.

**Example:** Testing 3 primers × 4 powders × 3 seating depths = 36 combinations.

**Problem:** With 30 shots per combination, that's 1,080 rounds. Prohibitively expensive for hobbyists.

**Better approach:** Sequential one-variable-at-a-time testing.

**See:** Notebook 04 - Factorial Explosion section

**Formula:**
```
Total combinations = (options for variable 1) × (options for variable 2) × ... × (options for variable n)

Total rounds = combinations × shots per combination

Example: 2 primers × 3 powders × 4 charges = 24 combinations
At 30 shots each = 720 rounds
```

---

### False Negative (Type II Error)

**Plain English:** Failing to detect a real difference because your test wasn't sensitive enough (usually due to small sample size).

**Example:** Load A really is better than Load B, but you tested with only 10 shots each and couldn't detect the difference.

**How to reduce:** Use larger sample sizes to increase statistical power.

**See:** Notebook 10 - When Is A Result Real

---

### False Positive (Type I Error)

**Plain English:** Claiming there's a difference when there really isn't (seeing a pattern in random noise).

**Example:** You test two identical loads with small samples and declare one "better" based on luck.

**How to reduce:** Use proper sample sizes, set appropriate alpha levels, avoid p-hacking.

**See:** Notebook 10 - When Is A Result Real

---

## H

### Hybrid Ogive

**Plain English:** A bullet design combining tangent and secant ogives, developed by Bryan Litz to retain high BC while reducing seating depth sensitivity.

**Why it matters:** Hybrid bullets are less finicky about seating depth than pure secant (VLD) bullets.

**See:** Notebook 07 - Seating Depth section

---

## J

### Jam / Jump

**Plain English:** Terms describing bullet seating relative to the rifling lands.

**Jam (into the lands):** Bullet is seated long enough to contact the rifling when chambered. Creates higher pressure, can improve accuracy in some rifles but makes feeding unreliable.

**Jump (off the lands):** Bullet is seated shorter, leaving a gap between bullet and rifling. This is the "jump" distance (e.g., "0.020 inches off the lands" = 0.020" jump).

**Typical ranges:**
- Jam: 0.000" to -0.010" (negative = into lands)
- Touch: 0.000" (just touching)
- Jump: 0.010" to 0.100" off lands (common range)

**Measurement:** Use a comparator or Hornady OAL gauge to measure base-to-ogive length.

**See:** Notebook 07 - Seating Depth testing

---

## M

### Mean

**Plain English:** The average. Add up all values and divide by how many you have.

**Example:** Velocities of 2,840, 2,850, 2,845, 2,855 fps have a mean of (2,840+2,850+2,845+2,855) / 4 = 2,847.5 fps

**Why it matters:** Sample means converge quickly to population means (10-15 shots is usually adequate).

**See:** Notebook 05 - Average Velocity section

**Formula:**
```
Mean (x̄) = Σx / n

Where:
Σx = sum of all values
n = number of values

Example:
Values: 2840, 2850, 2845, 2855 fps
Mean = (2840 + 2850 + 2845 + 2855) / 4 = 2847.5 fps
```

---

### Mean Radius (MR)

**Plain English:** The average distance of all shots from the center of the group.

**Why it's better than ES:** Uses all shots (not just the two most extreme), more stable across samples, better represents true precision.

**Calculation:** Find the group center (average X and Y positions), measure each shot's distance from center, average those distances.

**See:** Notebook 06 - Mean Radius vs Extreme Spread

**Formula:**
```
1. Find group center:
   Center_X = Σ(x_i) / n
   Center_Y = Σ(y_i) / n

2. Calculate each shot's radius from center:
   r_i = √[(x_i - Center_X)² + (y_i - Center_Y)²]

3. Mean Radius:
   MR = Σ(r_i) / n

Example:
Shots at (X, Y) in inches: (0.2, 0.3), (-0.1, 0.4), (0.3, -0.2)
Center: (0.133, 0.167)
Radii: 0.208, 0.300, 0.430 inches
MR = (0.208 + 0.300 + 0.430) / 3 = 0.313 inches
```

---

### Minute of Angle (MOA)

**Plain English:** An angular measurement equal to approximately 1 inch per 100 yards.

**Precision:**
- 1 MOA = 1.047 inches at 100 yards (often rounded to 1")
- 1 MOA = 2.094 inches at 200 yards
- 1 MOA = 10.47 inches at 1,000 yards

**Usage:** "This rifle shoots 1 MOA" means groups average about 1 inch at 100 yards, 2 inches at 200 yards, etc.

**See:** Notebook 06 - Group Size measurements

**Formula:**
```
Exact MOA conversion:
MOA = (group size in inches / distance in yards) × 100 / 1.047

Approximate (1 inch per 100 yards):
MOA ≈ (group size in inches / distance in yards) × 100

Example: 1.5" group at 100 yards
Exact: MOA = (1.5 / 100) × 100 / 1.047 = 1.43 MOA
Approximate: MOA ≈ 1.5 MOA
```

---

### Monte Carlo Simulation

**Plain English:** A computer technique that runs thousands of random trials to see what typically happens by chance.

**How it works:**
1. Define the true population (e.g., rifle with 1.0 MOA true precision)
2. Randomly "shoot" many samples (e.g., 1,000 five-shot groups)
3. Observe the distribution of results

**Why we use it:** Shows you what random variation looks like, helping you distinguish real effects from noise.

**Example in this curriculum:** We simulate shooting 1,000 three-shot groups from a 1.5 MOA rifle to show how wildly group sizes vary (0.4 to 3.0 MOA) despite consistent underlying capability.

**See:** Notebooks 01, 02, 03 (throughout curriculum)

**Pseudocode:**
```python
# Monte Carlo simulation of group sizes
true_precision = 1.0  # MOA
num_simulations = 1000
shots_per_group = 5

for i in range(num_simulations):
    # Generate random group from normal distribution
    group = generate_random_shots(true_precision, shots_per_group)
    # Measure this sample's group size
    measured_size = calculate_group_size(group)
    # Store result
    results.append(measured_size)

# Analyze distribution of measured_size
# Shows range: 0.3 MOA to 2.5 MOA from 1.0 MOA rifle
```

---

## N

### Node (Velocity)

**Plain English:** A claimed "sweet spot" in powder charge where velocity doesn't increase much (a "flat spot" in the charge ladder).

**The claim:** These nodes indicate optimal barrel harmonics for accuracy.

**The reality:** These apparent flat spots are random variation in single-shot-per-charge testing, not real phenomena. Controlled tests show "node" charges perform no better than adjacent charges.

**See:** Notebook 05 - Velocity Node Myth section

---

### Normal Distribution

**Plain English:** The classic "bell curve" shape. Most values cluster near the average, with fewer and fewer values as you move away from center.

**Properties:**
- Symmetric around the mean
- 68% of values within ±1 SD
- 95% of values within ±2 SD
- 99.7% of values within ±3 SD

**Why it matters:** Many natural phenomena follow normal distributions, including shot-to-shot variation in ammunition.

**See:** Notebook 02 - Ocean and Cup analogy

**Formula:**
```
Probability density function:
f(x) = (1 / (σ√(2π))) × e^(-(x-μ)²/(2σ²))

Where:
μ = population mean
σ = population standard deviation
x = value

Cumulative percentages (empirical rule):
μ ± 1σ contains ~68% of values
μ ± 2σ contains ~95% of values
μ ± 3σ contains ~99.7% of values
```

---

## O

### OCW (Optimal Charge Weight)

**Plain English:** A testing method where you shoot round-robin groups at different targets with incrementing powder charges, looking for charges that "converge" (impact close together across targets).

**The claim:** Convergence indicates optimal charge weight with forgiving harmonics.

**The problem:** With 3 shots per charge, random variation dominates. Different trials show different "optimal" charges. Recoil management variation exceeds any charge weight effects.

**See:** Notebook 07 - OCW section

---

### Ogive

**Plain English:** The curved nose portion of a bullet from the shank to the tip.

**Types:**
- **Secant ogive:** Sharp curve, high BC, but more sensitive to seating depth
- **Tangent ogive:** Gradual curve, lower BC, but more forgiving
- **Hybrid ogive:** Combination design (secant front, tangent rear) balancing BC and forgiveness

**See:** Notebook 07 - Seating Depth section

---

## P

### p-hacking

**Plain English:** Manipulating data or analysis after seeing results to achieve statistical significance. Forms of statistical cheating.

**Examples:**
- Testing stops when results look good
- Excluding "outliers" without pre-defined criteria
- Trying multiple analyses until one shows significance
- Selectively reporting only significant results

**Prevention:** Pre-register your analysis plan before collecting data.

**See:** Notebook 11 - Pre-Registration section

---

### Population

**Plain English:** The complete set of all possible rounds you could make with your load recipe. The "ocean" in the ocean-and-cup analogy.

**Example:** If you could load infinite rounds with your exact recipe, that infinite set is the population.

**Key concept:** You can never measure the entire population—you can only sample from it.

**See:** Notebook 02 - What We Actually Mean by Consistency

---

### p-value

**Plain English:** The probability of getting your result (or more extreme) if there really is no difference.

**Example:** p = 0.03 means "If the loads really perform identically, there's a 3% chance I'd see a difference this big just by random luck."

**Common threshold:** p < 0.05 is often used to call something "statistically significant."

**Important:** Low p-value doesn't mean the effect is large or important, just that it's unlikely to be random chance.

**See:** Notebook 10 - When Is A Result Real

**Formula:**
```
p-value = P(data | null hypothesis is true)

Interpretation:
p < 0.01: Strong evidence against null hypothesis (< 1% chance)
p < 0.05: Moderate evidence (< 5% chance) - common threshold
p > 0.05: Insufficient evidence to reject null hypothesis

Note: p-value does NOT tell you:
- Probability the null hypothesis is true
- Size of the effect
- Practical importance of the result
```

---

### Precision

**Plain English:** How consistently shots group together, regardless of where they impact. Different from accuracy (how close to your aim point).

**Example:** Five shots in a 0.5-inch group that's 2 inches left of bullseye = precise but not accurate.

**Measurement:** Usually measured as group size (MOA) or mean radius.

**See:** Notebook 06 - Precision vs Accuracy

---

## R

### Ragged Hole

**Plain English:** When multiple bullets pass through nearly the same hole, creating one enlarged, irregular hole.

**Usage:** Benchrest shooters measure the perimeter of the ragged hole.

**Limitation:** Only works at close range where individual bullet holes can be identified. Impractical at distance or with overlapping groups.

**See:** Notebook 06 - Measurement Methods

---

### Replication

**Plain English:** Repeating a test under the same conditions to verify the result wasn't just luck.

**Example:** You test a load and get great results. Shooting the same test on a different day and getting similar results = successful replication.

**Importance:** Results that don't replicate were probably statistical flukes, not real effects.

**See:** Notebook 11 - Replication section

---

## S

### Sample

**Plain English:** A subset of the population that you actually test. The "cup" in the ocean-and-cup analogy.

**Example:** You load and test 30 rounds = your sample. The infinite possible rounds you could make = the population.

**Key insight:** Sample statistics (like sample SD) estimate population parameters (true SD) with some uncertainty.

**See:** Notebook 02 - What We Actually Mean by Consistency

---

### Sample Size (n)

**Plain English:** How many rounds you test. Written as "n" in formulas.

**Critical concept:** Larger samples give more reliable estimates of the true population.

**Guidelines:**
- n = 10-15: Adequate for average velocity
- n = 30+: Minimum for SD measurements
- n = 50+: Better for comparing loads
- n = 100+: Needed for strong claims

**See:** Notebook 03 - How Many Shots Do You Really Need

---

### Secant Ogive

**Plain English:** A bullet nose design with a sharp, aggressive curve. Common in VLD (Very Low Drag) bullets.

**Characteristics:**
- High ballistic coefficient (BC)
- More sensitive to seating depth
- Abrupt transition to rifling

**Examples:** Berger VLD, Sierra MatchKing (some)

**See:** Notebook 07 - Seating Depth section

---

### Standard Deviation (SD)

**Plain English:** A measure of spread or variation. Shows how much individual values typically differ from the average.

**For velocity:** Lower SD means more consistent velocities. Example: SD of 10 fps means shots typically vary by about 10 fps from the mean.

**Critical issue:** SD calculated from small samples systematically underestimates the true population SD (optimistic bias).

**See:** Notebook 05 - The Perverse Nature of Standard Deviation

**Formula:**
```
Sample Standard Deviation:
SD = √[Σ(x_i - x̄)² / (n - 1)]

Where:
x_i = each individual value
x̄ = sample mean
n = sample size
Σ = sum of all values

Example (velocities in fps):
Data: 2840, 2850, 2845, 2855, 2848
Mean (x̄) = 2847.6 fps

Deviations from mean:
(2840 - 2847.6)² = 57.76
(2850 - 2847.6)² = 5.76
(2845 - 2847.6)² = 6.76
(2855 - 2847.6)² = 54.76
(2848 - 2847.6)² = 0.16

Sum of squared deviations = 125.2
SD = √(125.2 / 4) = √31.3 = 5.6 fps
```

---

### Standard Error (SE)

**Plain English:** A measure of how much your sample mean probably differs from the true population mean. Gets smaller as sample size increases.

**Key insight:** This is why larger samples give more precise estimates of the true average.

**See:** Notebook 03 - Confidence Intervals

**Formula:**
```
SE = SD / √n

Where:
SD = sample standard deviation
n = sample size

Example:
SD = 15 fps, n = 30 shots
SE = 15 / √30 = 15 / 5.48 = 2.74 fps

Interpretation: Sample mean is probably within ±2.74 fps
of true population mean (at ~68% confidence)
```

---

### Statistical Power

**Plain English:** The probability of detecting a real difference when one actually exists. Higher power = less likely to miss a real effect.

**Factors affecting power:**
- Sample size (bigger = more power)
- Effect size (larger differences easier to detect)
- Variability (less noise = more power)

**Typical goal:** 80% power (80% chance of detecting real effect)

**See:** Notebook 10 - Statistical Power section

**Formula:**
```
Power = 1 - β

Where:
β = probability of Type II error (false negative)

Power depends on:
- Sample size (n)
- Effect size (difference you want to detect)
- Alpha level (significance threshold)
- Standard deviation (noise)

General relationship:
Required n ≈ (Z_α + Z_β)² × (2σ² / d²)

Where:
Z_α, Z_β = values from normal distribution for alpha and beta
σ = standard deviation
d = difference you want to detect
```

---

### Statistical Significance

**Plain English:** When the probability your result happened by chance is low enough (usually p < 0.05) to conclude there's probably a real difference.

**Important distinction:** "Statistically significant" doesn't mean "large" or "important"—it just means "probably not random chance."

**Example:** A 0.5 fps difference in SD might be statistically significant with 100 shots per load but is too small to matter practically.

**See:** Notebook 10 - Significance vs Practical Importance

---

### Survivorship Bias

**Plain English:** When you only see successful results because failures aren't reported, creating a distorted view of reality.

**Example:** 100 shooters try OCW testing. 20 get lucky and post success stories online. 80 get inconclusive results and stay quiet. New shooters see only the 20 successes and think "OCW has a 100% success rate!"

**See:** Notebooks 00, 07, 12

---

## T

### Tangent Ogive

**Plain English:** A bullet nose design with a gradual curve. Traditional design for most bullets.

**Characteristics:**
- Lower ballistic coefficient than secant
- Less sensitive to seating depth
- Gradual transition to rifling

**Examples:** Most traditional hunting bullets, Sierra MatchKing (some models)

**See:** Notebook 07 - Seating Depth section

---

### Temperature Sensitivity

**Plain English:** How much velocity changes with temperature. Some powder/cartridge combinations are more temperature-stable than others.

**Typical range:** 0.5 to 3.0 fps per degree Fahrenheit

**Why it matters:** A load developed at 70°F might be 40-50 fps faster at 95°F or slower at 30°F with temp-sensitive powder.

**Testing:** Properly test by acclimating ammunition to target temperature for 60+ minutes before shooting.

**See:** Notebooks 04, 05 - Temperature sections

**Formula:**
```
Velocity change ≈ Temperature coefficient × ΔT

Example:
Coefficient = 1.5 fps/°F
Developed at 70°F: 2,850 fps
Shot at 30°F: ΔT = -40°F
Expected velocity = 2,850 + (1.5 × -40) = 2,790 fps

Note: Relationship may not be perfectly linear across extreme ranges
```

---

### t-test

**Plain English:** A statistical test to determine if two sample means are significantly different.

**When to use:** Comparing average velocity or average group size between two loads.

**Result:** Produces a p-value indicating probability the difference is random chance.

**See:** Notebook 10 - Statistical Tests

**Formula:**
```
Independent samples t-test:
t = (x̄₁ - x̄₂) / SE_diff

Where:
x̄₁, x̄₂ = sample means
SE_diff = √(SE₁² + SE₂²)
SE = SD / √n

Example:
Load A: mean = 2,850 fps, SD = 12 fps, n = 30
Load B: mean = 2,835 fps, SD = 15 fps, n = 30

SE_A = 12 / √30 = 2.19 fps
SE_B = 15 / √30 = 2.74 fps
SE_diff = √(2.19² + 2.74²) = 3.51 fps

t = (2,850 - 2,835) / 3.51 = 4.27

With df = 58, this t-value gives p < 0.001
(Strong evidence of real difference)
```

---

### Type I Error (False Positive)

**Plain English:** Claiming there's a difference when there really isn't. Also called alpha error or false alarm.

**Example:** You declare Load A better than Load B based on lucky samples, but they're actually identical.

**Probability:** Set by your alpha level (commonly 0.05 = 5% chance)

**See:** Notebook 10 - Errors in Testing

---

### Type II Error (False Negative)

**Plain English:** Failing to detect a real difference. Also called beta error or missed opportunity.

**Example:** Load A really is better, but your sample size was too small to detect the difference.

**Probability:** Set by your statistical power (1 - beta). With 80% power, you have 20% chance of Type II error.

**See:** Notebook 10 - Errors in Testing

---

## V

### Variance

**Plain English:** The square of standard deviation. Measures spread, but in squared units.

**Usage:** Used in statistical calculations, but SD is more interpretable because it's in the same units as your data.

**Relationship:** Variance = SD²

**See:** Notebook 05 - Spread measurements

**Formula:**
```
Sample Variance:
s² = Σ(x_i - x̄)² / (n - 1)

Standard Deviation:
SD = √(variance) = √s²

Example:
If SD = 15 fps
Then variance = 15² = 225 fps²
```

---

### VLD (Very Low Drag)

**Plain English:** A bullet design with a secant ogive and boat-tail optimized for high ballistic coefficient.

**Characteristics:**
- Excellent long-range performance
- Often sensitive to seating depth
- May require specific jump distances for best accuracy

**Common examples:** Berger VLD bullets

**See:** Notebook 07 - Seating Depth testing

---

## Additional Reloading-Specific Terms

### Freebore

**Plain English:** The unrifled portion of the barrel throat ahead of the chamber. The bullet travels through this before engaging the rifling.

**Effect:** Longer freebore allows longer bullets to be seated without excessive pressure. Shorter freebore may require shorter bullets or deeper seating.

---

### Leade (also Lead)

**Plain English:** The angled transition from the freebore to the full rifling. Where the bullet first contacts the rifling lands.

**Relationship to seating:** "Off the lands" measurements reference this transition point.

---

### Throat Erosion

**Plain English:** Wear in the barrel throat from hot gases and bullets, gradually increasing the freebore length.

**Effect:** As throat erodes, bullets must "jump" farther to reach rifling. This can affect accuracy and pressure over the barrel's life.

---

### Case Capacity

**Plain English:** The internal volume of the cartridge case available for powder.

**Factors affecting it:**
- Bullet seating depth (longer seating = less capacity)
- Case wall thickness
- Case manufacturer

**Why it matters:** More capacity generally allows more powder and higher velocities, but also affects pressure.

---

### Neck Tension

**Plain English:** How tightly the case neck grips the bullet.

**Measurement:** Usually expressed as the difference between bullet diameter and sized neck internal diameter (e.g., 0.002" tension)

**Effect:** Affects initial pressure and consistency. More tension = higher initial pressure spike.

---

## Cross-Reference by Notebook

**Notebook 01:** Sample, Population, Bias, Monte Carlo Simulation
**Notebook 02:** Normal Distribution, Mean, Standard Deviation, Population, Sample
**Notebook 03:** Sample Size, Confidence Interval, Statistical Power, Standard Error
**Notebook 04:** Confounded Variables, Factorial Experiment, DOPE, Temperature Sensitivity
**Notebook 05:** Standard Deviation, Extreme Spread (velocity), Mean, Chronograph, Node
**Notebook 06:** Mean Radius, Extreme Spread (group), MOA, Precision, Accuracy
**Notebook 07:** OCW, Node, Ogive types, Jam/Jump, Survivorship Bias
**Notebook 10:** p-value, Statistical Significance, Type I/II Errors, Statistical Power, t-test
**Notebook 11:** p-hacking, Replication, Bias, Confirmation Bias

---

## Quick Formula Reference

**Standard Deviation:**
```
SD = √[Σ(x_i - x̄)² / (n - 1)]
```

**Standard Error:**
```
SE = SD / √n
```

**Confidence Interval:**
```
CI = x̄ ± (t × SE)
```

**Mean Radius:**
```
MR = Σ√[(x_i - x̄)² + (y_i - ȳ)²] / n
```

**MOA Conversion:**
```
MOA = (inches / yards) × 100 / 1.047
```

**Sample Size for Comparing Means:**
```
n ≈ 2(Z_α/2 + Z_β)² × (σ² / d²)
```

Where: σ = standard deviation, d = difference to detect

---

**Need more detail?** Each term references the notebook(s) where it's discussed in depth. Use this glossary as a quick reference, then dive into the specific notebooks for complete explanations and examples.

[Back to Curriculum](../../README.md)
