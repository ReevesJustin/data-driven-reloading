# Glossary of Technical Terms

## How to Use This Glossary

This reference guide defines all technical terms used throughout the curriculum.

**Organization:** Alphabetical order
**Cross-references:** Terms reference the lessons where they're discussed in detail
**Formulas:** Mathematical definitions appear after plain-English explanations

---

## A

### Accuracy

**Plain English:** How close your shots land to where you're aiming. Different from precision (consistency).

**Example:** If you aim at the bullseye and hit it, that's accurate. If you always hit the same spot but it's 2 inches left of the bullseye, that's precise but not accurate.

**Key distinction:** You can be precise without being accurate (consistent groups in the wrong place) or accurate without being precise (shots average on target but spread widely).

**See:** Lesson 06 - Group Size and Accuracy

---

### Alpha (α)

**Plain English:** The probability threshold you set for calling something "statistically significant." Commonly set at 0.05 (5%).

**Example:** If alpha = 0.05, you're saying "I'll accept a 5% risk of falsely claiming there's a difference when there isn't."

**Usage:** Lower alpha means stricter requirements for claiming significance.

**See:** Lesson 10 - When Is A Result Real

**Formula:**
```
α = P(rejecting null hypothesis | null hypothesis is true)
Commonly: α = 0.05 (5% false positive rate)
```

---

### Audette Test

**Plain English:** A specific ladder test variant developed by Canadian shooter Creighton Audette, where you shoot groups (typically 3-shot) at each powder charge instead of single shots, looking for the smallest group.

**Method:**
1. Load 3-5 rounds at each powder charge (increments of 0.3-0.5 grains)
2. Shoot groups at each charge
3. Identify charge with smallest group
4. Load more ammunition at that charge and validate

**The problem:** Same as other ladder tests—3-shot groups have massive random variation (see Lesson 01). The "best group" is often just lucky, not actually the best charge. Validation testing frequently shows different results.

**Better approach:** If testing multiple charges, use 20-30 shots per charge and compare average group sizes, not best group.

**See:** Lesson 07 - Testing Methods, Lesson 01 - Small Sample Bias

---

### Barrel Harmonics

**Plain English:** The vibration pattern of a rifle barrel when a round is fired. The barrel flexes and whips as the bullet travels down it.

**The claim:** Some powder charges create "nodes" where harmonics minimize dispersion.

**The reality:** While barrels do vibrate when fired, the claimed "sweet spot" theory doesn't hold up in testing. The bullet leaves the barrel in 1-2 milliseconds—too fast for the barrel to move much. Think of it like a guitar string: the bullet is gone before the "note" fully sounds. Controlled tests show that "node" charges perform no better than nearby charges.

**Bottom line:** Barrel movement exists but is too small and inconsistent to create reliable accuracy nodes that you can find and exploit with typical testing methods.

**For advanced readers:** Research "cantilevered Euler-Bernoulli beam" for the physics. A typical match barrel (~60Hz natural frequency, 24" full contour) has minimal muzzle displacement during the 1-2ms the bullet is in the bore.

**See:** Lesson 07 - Real Examples (Velocity Nodes section)

---

### Bias

**Plain English:** A systematic error that makes measurements consistently wrong in one direction.

**Example:** Small samples systematically underestimate SD (they're biased optimistic). Three-shot groups systematically underestimate your rifle's true capability.

**Types:**
- **Optimistic bias:** Results look better than reality (small samples)
- **Confirmation bias:** Seeing what you expect instead of what's there
- **Selection bias:** Cherry-picking data that supports your conclusion

**See:** Lesson 01 (optimistic bias in small samples), Lesson 03 (sample size bias), Lesson 11 (confirmation bias)

---

### BC (Ballistic Coefficient)

**Plain English:** A number describing how well a bullet resists air drag. Higher BC means the bullet slows down less, flies flatter, and drifts less in wind.

**Typical ranges:**
- 0.200-0.300: Flat-nose pistol bullets, traditional rifle bullets
- 0.400-0.500: Modern hunting bullets (ballistic tip, boat-tail)
- 0.550-0.700+: Match bullets (VLD, hybrid ogive)

**Why it matters:** Higher BC bullets retain velocity better at long range. A 0.600 BC bullet might have 200+ fps more velocity than a 0.400 BC bullet at 600 yards, even with identical muzzle velocity.

**Models:** G1 (traditional), G7 (modern match bullets more accurate with this model)

**See:** Lessons 07, 09 - Bullet selection and long-range performance

**Formula:**
```
BC = (bullet mass / bullet diameter²) × form factor

Higher BC → less velocity loss → flatter trajectory → less wind drift

Example impact at 600 yards:
BC 0.400: ~400 fps velocity loss, ~80" drop
BC 0.600: ~300 fps velocity loss, ~60" drop
```

---

### Bearing Surface

**Plain English:** The cylindrical portion of the bullet that contacts the rifling. Length of bearing surface affects engraving pressure and can influence accuracy and velocity.

**Characteristics:**
- Longer bearing surface = more contact with rifling = higher engraving pressure
- Shorter bearing surface = less contact = lower pressure
- VLD bullets often have relatively short bearing surface despite long overall length

**Why it might matter:**
- Variation in bearing surface length (even in same box of bullets) can cause velocity variation
- Very long bearing surface may require seating deeper (reducing case capacity)

**Practical importance:** Minimal for most applications. More relevant for extreme precision applications (benchrest) or when using bullets near max COAL.

---

### Benchrest

**Plain English:** A precision shooting competition where shooters use specialized equipment and shooting benches to achieve extreme accuracy. Groups as small as 0.2-0.3 MOA are common.

**Equipment:** Custom actions, match barrels replaced every 800-1,500 rounds, return-to-battery rests, lot-tested components.

**Why it matters:** Represents the upper limit of precision achievable with handloaded ammunition. Benchrest techniques inform load development but require specialized equipment.

**See:** Lessons 09, 12 - Equipment and precision expectations

---

## C

### Central Limit Theorem (CLT)

**Plain English:** A math rule that says averages become predictable. Even if your individual shots vary randomly, the average of multiple groups will form a bell curve pattern. This is why averages stabilize faster than spread measurements.

**Why it matters:** This is why 10-15 shots gives you a pretty good average velocity, but you need 30+ shots to trust your SD measurement.

**Practical impact:** Sample means converge quickly to the true population mean—much faster than measures of spread (SD, ES) converge to their true values.

**See:** Lesson 03 - How Many Shots Do You Really Need

---

### Chronograph

**Plain English:** A device that measures bullet velocity by timing how long it takes a bullet to pass between sensors.

**Common types:**
- Optical chronographs (use light screens)
- Doppler radar chronographs (track bullet speed downrange)

**Precision:** Budget models ±5-10 fps error, quality models ±2-3 fps error

**See:** Lesson 05 - Velocity Data (Chronograph Precision section)

---

### COAL (Cartridge Overall Length)

**Plain English:** The total length of a loaded cartridge from the base to the tip of the bullet.

**Why it matters:** COAL affects how much powder fits in the case (pressure) and how far the bullet "jumps" to the rifling (see Jump/Jam).

**Measurement:** Use a caliper, measure from case head to bullet tip.

**See:** Lesson 07 - Seating Depth section

---

### Confidence Interval (CI)

**Plain English:** A range showing where the true value likely falls. Think of it as your "margin of error." The "95% confidence" part means if you repeated this test 100 times, about 95 of those ranges would contain the true answer.

**Example:** "The true SD is between 12 and 18 fps (95% CI)" means we're 95% confident the real SD falls in that range.

**Key insight:** Smaller samples have wider confidence intervals (more uncertainty). With 10 shots, your SD might be 10-25 fps. With 50 shots, it narrows to 13-17 fps.

**See:** Lesson 03 - Sample Size sections

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
t ≈ 2.045 (for 29 degrees of freedom (df) at 95%)
CI = x̄ ± (2.045 × 2.74) = x̄ ± 5.6 fps
```

---

### Confounded Variables

**Plain English:** When you change multiple things at once and can't tell which one caused the result.

**Example:** You switched primers AND powder. Your groups shrunk. Which change helped? You can't know—the variables are confounded.

**Solution:** Test one variable at a time.

**See:** Lesson 04 - Testing One Thing at a Time

---

## D

### Degrees of Freedom (df)

**Plain English:** A math term for how many data points actually vary independently. Think of it like this: if you know 4 numbers average to 20, and you know the first 3 numbers, the 4th number is locked in—it's not "free" to vary. That's why df = n - 1.

**Analogy:** You're picking a 4-person team, and you know the average height must be exactly 6 feet. You can freely pick the first 3 people (any height), but the 4th person's height is determined by the requirement. Only 3 "free" choices = 3 degrees of freedom.

**Practical meaning:** Used in statistical tests to get the right critical values. For most calculations, df = sample size minus 1.

**Why it matters:** Determines which values to use from t-distribution tables and affects confidence interval width.

**Formula:**
```
For single sample: df = n - 1
For two samples: df = n₁ + n₂ - 2
```

---

### Dispersion Budget

**Plain English:** A framework for analyzing all contributors to your total system precision, showing how much each factor "costs" you in MOA.

**Components:**
- Rifle mechanical precision
- Ammunition consistency (velocity SD, ES)
- Shooter error (position, trigger control)
- Recoil management
- Environmental factors (wind reading, mirage)

**Combined using RSS:** Total system precision = √(Rifle² + Ammo² + Shooter² + Recoil² + Env²)

**Why it's called a "budget":** Like a financial budget, you have limited "funds" (total acceptable dispersion). You allocate your improvement effort to the biggest drains first.

**Example budget for 1.0 MOA system:**
- Rifle: 0.5 MOA (25% of budget)
- Ammunition: 0.4 MOA (16% of budget)
- Shooter: 0.6 MOA (36% of budget)
- Recoil: 0.3 MOA (9% of budget)
- Environment: 0.4 MOA (16% of budget)

**Insight:** Shooter error is the biggest factor. Improving ammunition from 0.4 to 0.2 MOA only improves total system from 1.0 to 0.93 MOA. Improving shooter from 0.6 to 0.4 MOA improves system to 0.85 MOA.

**See:** Lesson 09 - System Analysis, RSS

---

### DOPE (Data On Previous Engagements)

**Plain English:** A log of your ballistic data (drop, wind drift, etc.) at various ranges and conditions.

**Usage:** Precision shooters maintain DOPE books to quickly reference correct adjustments.

**Quality DOPE requires:** Accurate environmental data, proper ranging, consistent ammunition.

**See:** Lesson 04 - Environmental Control section

---

## E

### Effect Size

**Plain English:** The magnitude of a difference between groups, separate from whether it's statistically significant. A result can be statistically significant but too small to matter practically.

**Example:** Load A has 2 fps lower SD than Load B (statistically significant with 100 shots per load). Effect size = 2 fps. At 600 yards, this causes ~1 inch vertical difference—real but probably not worth pursuing.

**Common measures:**
- Cohen's d (standardized difference between means)
- Difference in SD or group size (raw units)

**Key insight:** Statistical significance tells you a difference probably exists. Effect size tells you if it matters.

**See:** Lesson 10 - Practical Significance vs Statistical Significance

**See also:** Practical Significance, Statistical Significance, p-value

**Formula:**
```
Cohen's d = (Mean₁ - Mean₂) / Pooled SD

For practical reloading:
Effect size = |Difference in SD or group size|

Example: Load A SD = 12 fps, Load B SD = 15 fps
Effect size = 3 fps (small but potentially meaningful)
```

---

### ELR (Extreme Long Range)

**Plain English:** Shooting at distances beyond 1,500 yards, often extending to a mile or more. Requires extreme attention to ballistic coefficients, environmental conditions, and ammunition consistency.

**Characteristics:** Very high BC bullets, precise velocity control, lot-tested components, advanced ballistic solutions.

**Why it matters:** Context where extreme ammunition preparation (brass sorting, neck turning) may actually provide measurable benefits.

**See:** Lesson 07 - Advanced brass preparation context

---

### Extreme Spread (ES)

**Plain English:** The difference between your fastest and slowest shot in a sample.

**Example:** Velocities of 2,835, 2,848, 2,851, 2,846, 2,863 fps have ES = 2,863 - 2,835 = 28 fps

**Problem:** ES grows forever as you add shots. It can never shrink, only stay the same or increase. This makes it a poor metric for comparing loads unless sample sizes are identical.

**Better alternative:** Use Standard Deviation (SD) instead.

**See:** Lesson 05 - Velocity Data

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

**See:** Lesson 06 - Group Size and Accuracy

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

### F-Class

**Plain English:** A long-range precision shooting competition (typically 600-1,000 yards) where shooters use bipods or rests. Similar precision expectations to benchrest but with heavier rifles optimized for long range.

**Characteristics:** Heavy rifles (often 15-20 lbs), match-grade ammunition, wind flags and coaching allowed.

**Why it matters:** Provides realistic precision benchmarks for long-range load development.

**See:** Lessons 09, 12 - Competition shooting context

---

### Factorial Experiment

**Plain English:** Testing all possible combinations of multiple variables.

**Example:** Testing 3 primers × 4 powders × 3 seating depths = 36 combinations.

**Problem:** With 30 shots per combination, that's 1,080 rounds. Prohibitively expensive for hobbyists.

**Better approach:** Sequential one-variable-at-a-time testing.

**See:** Lesson 04 - Factorial Explosion section

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

**See:** Lesson 10 - When Is A Result Real

---

### False Positive (Type I Error)

**Plain English:** Claiming there's a difference when there really isn't (seeing a pattern in random noise).

**Example:** You test two identical loads with small samples and declare one "better" based on luck.

**How to reduce:** Use proper sample sizes, set appropriate alpha levels, avoid p-hacking.

**See:** Lesson 10 - When Is A Result Real

---

## H

### Hybrid Ogive

**Plain English:** A bullet design combining tangent and secant ogives, developed by Bryan Litz to retain high BC while reducing seating depth sensitivity.

**Why it matters:** Hybrid bullets are less finicky about seating depth than pure secant (VLD) bullets.

**See:** Lesson 07 - Seating Depth section

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

**See:** Lesson 07 - Seating Depth testing

---

## L

### Ladder Test

**Plain English:** A testing method where you load single rounds at incrementing powder charges and shoot them at a distant target (often 300+ yards), looking for charges where vertical impact doesn't increase much ("nodes" or "flat spots").

**The claim:** Nodes indicate optimal barrel harmonics for accuracy.

**The reality:** With one shot per charge, random variation dominates. Recoil management affects vertical impact more than powder charge. "Flat spots" move randomly from test to test. Controlled studies show "node" charges perform no better than adjacent charges.

**See:** Lesson 07 - Ladder Test Debunking, Appendix B - Evidence Status

**Recommendation:** Use ladder tests only for pressure screening (watching for signs of excessive pressure as you approach maximum charges), not for finding accuracy nodes. If you want to find the best charge for accuracy, test 2-3 charges with 30+ shots each and measure group sizes.

---

### Lot Testing

**Plain English:** Testing samples from different manufacturing batches (lots) of the same component to find the most consistent or accurate lot for your rifle.

**Common for:** Bullets (especially in benchrest), primers, brass

**Process:**
1. Obtain samples from multiple lots
2. Test each lot with adequate sample sizes (30+ rounds)
3. Select the lot that performs best in YOUR rifle
4. Buy large quantity from that specific lot

**Why it matters:** Manufacturing variation exists even within the same product line. Top competitors find better performance by testing lots rather than assuming all boxes are identical.

**Practicality:** Makes sense for serious competition or when buying components in bulk (1,000+ bullets). Overkill for most hunters and recreational shooters.

**See:** Lesson 09 - Equipment and component selection

---

## M

### Mean

**Plain English:** The average. Add up all values and divide by how many you have.

**Example:** Velocities of 2,840, 2,850, 2,845, 2,855 fps have a mean of (2,840+2,850+2,845+2,855) / 4 = 2,847.5 fps

**Why it matters:** Sample means converge quickly to population means (10-15 shots is usually adequate).

**See:** Lesson 05 - Average Velocity section

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

**See:** Lesson 06 - Mean Radius vs Extreme Spread

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

### Mirage

**Plain English:** Heat distortion of air that makes targets appear to shimmer or waver through your optic. Caused by temperature differences creating air density variations.

**Effect on shooting:**
- Makes precise aiming difficult (target appears to move)
- Indicates wind direction and strength (mirage "runs" with the wind)
- Worse on hot days, over dark surfaces (pavement, dark soil)

**Mitigation:**
- Shoot early morning or late afternoon (cooler temps)
- Use sunshade on scope to reduce heat near objective lens
- Turn magnification down (less magnification = less mirage)
- Learn to read mirage for wind information

**Why it matters:** Can introduce aiming error larger than ammunition SD differences. Another factor in the "dispersion budget."

**See:** Lesson 11 - Environmental factors affecting testing

---

### Minute of Angle (MOA)

**Plain English:** An angular measurement equal to approximately 1 inch per 100 yards.

**Precision:**
- 1 MOA = 1.047 inches at 100 yards (often rounded to 1")
- 1 MOA = 2.094 inches at 200 yards
- 1 MOA = 10.47 inches at 1,000 yards

**Usage:** "This rifle shoots 1 MOA" means groups average about 1 inch at 100 yards, 2 inches at 200 yards, etc.

**See:** Lesson 06 - Group Size measurements

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

### Muzzle Brake

**Plain English:** A device attached to the muzzle that redirects propellant gases to reduce felt recoil and muzzle rise.

**How it works:** Ports or baffles redirect gas backward and sideways, creating forward thrust that partially cancels recoil.

**Impact:** Can reduce felt recoil by 30-50%, improving shooter's ability to maintain position and spot impacts. This often improves practical precision more than ammunition tweaking.

**Trade-off:** Significantly increases muzzle blast and noise, especially for shooters beside you.

**Why it matters for load development:** A muzzle brake can improve your system precision more than reducing SD from 15 to 10 fps. Consider equipment before endless load testing.

**See:** Lesson 09 - Recoil Management, System Precision

---

### Monte Carlo Simulation

**Plain English:** A computer technique that runs thousands of random trials to see what typically happens by chance.

**How it works:**
1. Define the true population (e.g., rifle with 1.0 MOA true precision)
2. Randomly "shoot" many samples (e.g., 1,000 five-shot groups)
3. Observe the distribution of results

**Why we use it:** Shows you what random variation looks like, helping you distinguish real effects from noise.

**Example in this curriculum:** We simulate shooting 1,000 three-shot groups from a 1.5 MOA rifle to show how wildly group sizes vary (0.4 to 3.0 MOA) despite consistent underlying capability.

**See:** Lesson 01 (group size distributions), Lesson 02 (sampling from populations), Lesson 03 (confidence interval visualization)

**Note for advanced readers:** The code below shows how simulations work. You don't need to understand programming to benefit from the curriculum—all simulations are run for you and results are shown visually.

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

**See:** Lesson 05 - Velocity Node Myth section

---

### Null Hypothesis

**Plain English:** The default assumption that there's no difference or no effect. In statistical testing, you try to prove the null hypothesis wrong.

**Example:**
- **Claim:** "Primer A gives lower SD than Primer B"
- **Null Hypothesis:** "Primers A and B produce the same SD"
- **Your job:** Collect enough data to prove the null hypothesis is probably wrong (reject it)

**Why it's structured this way:** Statistics can't prove something exists, but it can show something is unlikely to be random chance. So we assume "no difference" and try to disprove it.

**In formulas:** Often written as H₀

**Result:**
- If p < 0.05: Reject null hypothesis (conclude difference probably exists)
- If p > 0.05: Fail to reject null hypothesis (can't conclude there's a difference)

**See:** Lesson 10 - Hypothesis Testing

**Important distinction:** "Fail to reject null" doesn't mean "the null is true"—it means "we don't have enough evidence to conclude there's a difference."

---

### Normal Distribution

**Plain English:** The classic "bell curve" shape. Most values cluster near the average, with fewer and fewer values as you move away from center.

**Properties:**
- Symmetric around the mean
- 68% of values within ±1 SD
- 95% of values within ±2 SD
- 99.7% of values within ±3 SD

**Why it matters:** Many natural phenomena follow normal distributions, including shot-to-shot variation in ammunition.

**See:** Lesson 02 - Ocean and Cup analogy

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

**See:** Lesson 07 - OCW section

---

### Ogive

**Plain English:** The curved nose portion of a bullet from the shank to the tip.

**Types:**
- **Secant ogive:** Sharp curve, high BC, but more sensitive to seating depth
- **Tangent ogive:** Gradual curve, lower BC, but more forgiving
- **Hybrid ogive:** Combination design (secant front, tangent rear) balancing BC and forgiveness

**See:** Lesson 07 - Seating Depth section

---

### Outlier

**Plain English:** A data point that's unusually far from the rest of your data. The tricky question: is it legitimate data (showing real variation) or measurement error (chronograph malfunction, flyer from shooter error)?

**The problem:** Temptation to exclude outliers that hurt your conclusion (a form of p-hacking).

**When to exclude:**
- Clear equipment failure (chronograph error message, obvious double-charge)
- Documented shooter error (flinch, called flyer)
- Physical evidence (bullet keyhole, case split)

**When NOT to exclude:**
- Result doesn't match your expectation
- Makes your load look worse
- No clear reason except "doesn't fit the pattern"

**Best practice:**
1. Pre-define outlier criteria BEFORE testing (e.g., "exclude shots >3 SD from mean")
2. Document all exclusions with reason
3. Report both with and without outliers
4. If you frequently get "outliers," your system may be inconsistent (the outliers ARE your data)

**See:** Lesson 11 - Data integrity, p-hacking prevention

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

**See:** Lesson 11 - Pre-Registration section

---

### Pareto Principle (80/20 Rule)

**Plain English:** The observation that roughly 80% of results come from 20% of effort—or in precision shooting, that 80% of maximum capability requires about 20% of maximum investment, while the final 20% of capability requires 80% of the investment.

**Named after:** Italian economist Vilfredo Pareto, who observed that 80% of Italy's land was owned by 20% of the population. The principle has been found to apply across many domains.

**In precision equipment:** The biggest improvements come from upgrading your worst components (high return on investment), while chasing perfection shows extreme diminishing returns (low return on investment).

**Example:** Going from a budget optic ($250) to a quality optic ($1,000) might improve your system capability by 20%. But going from a quality optic to an absolute top-tier optic ($3,000) might only improve system capability by 3-5%. Same pattern applies to barrels, bullets, brass, and other components.

**The "$3,000 rifle with $500 optic" problem:** Many shooters violate this principle by investing heavily in one component (rifle) while skimping on another critical component (optic/mount). If the optic is the limiting factor, no amount of rifle upgrades will help.

**The ammunition tooling trap:** The same principle applies to reloading equipment. Before buying premium tools (annealer, lab-grade scale, custom dies = $2,500+), apply the SAME testing methodology from this curriculum. Does YOUR data show the specific problem that tool solves? Don't copy what pros use—test to identify YOUR system's actual limiting factor. The exponential cost increase for minimal capability gains applies to BOTH rifle hardware and ammunition preparation.

**The system approach:** Shooter + rifle + ammunition = SYSTEM. Equipment choice isn't this curriculum's scope, but you should understand WHY you need something before spending money on it. Testing reveals where your money matters most.

**Key insight:** There's no universal "best" upgrade path. Testing your specific system tells you where YOUR limiting factor is, so you can invest money where it actually matters.

**Practical application:**
1. Test current system (30-50 shots)
2. Identify weakest component
3. Upgrade THAT component only
4. Re-test to quantify improvement
5. Repeat with next weakest component

**Formula:**
```
For many systems:
~80% of maximum capability ≈ 20% of maximum cost
~20% of maximum capability ≈ 80% of maximum cost

Diminishing returns curve:
Investment efficiency = (Δ capability) / (Δ cost)
As capability → maximum, efficiency → 0
```

**See:** Lesson 09 (Component Quality section) - Reasonable Expectations

---

### Population

**Plain English:** The complete set of all possible rounds you could make with your load recipe. The "ocean" in the ocean-and-cup analogy.

**Example:** If you could load infinite rounds with your exact recipe, that infinite set is the population.

**Key concept:** You can never measure the entire population—you can only sample from it.

**See:** Lesson 02 - What We Actually Mean by Consistency

---

### p-value

**Plain English:** A number that tells you how likely your result happened by chance alone. Lower p-values mean "probably not just luck."

**Example:** p = 0.03 means if the two loads were actually identical, you'd only see a difference this big about 3 times out of 100 due to random chance. That's unlikely enough to believe there's probably a real difference.

**Common threshold:** p < 0.05 is often used to call something "statistically significant." This means "less than 5% chance this happened by luck."

**Important:** Low p-value doesn't mean the effect is large or important, just that it's unlikely to be random chance. You still need to check if the difference actually matters (see: Practical Significance, Effect Size).

**See:** Lesson 10 - When Is A Result Real

**Formula:**
```
p-value = P(data | null hypothesis is true)

Interpretation:
p < 0.01: Strong evidence against null hypothesis (< 1% chance)
p < 0.05: Moderate evidence (< 5% chance) - common threshold
p > 0.05: Insufficient evidence to reject null hypothesis

What p-value does NOT tell you:
- Probability the null hypothesis is true
- Size of the effect
- Practical importance of the result
```

---

### Precision

**Plain English:** How consistently shots group together, regardless of where they impact. Different from accuracy (how close to your aim point).

**Example:** Five shots in a 0.5-inch group that's 2 inches left of bullseye = precise but not accurate.

**Measurement:** Usually measured as group size (MOA) or mean radius.

**See:** Lesson 06 - Precision vs Accuracy

---

## R

### Ragged Hole

**Plain English:** When multiple bullets pass through nearly the same hole, creating one enlarged, irregular hole.

**Usage:** Benchrest shooters measure the perimeter of the ragged hole.

**Limitation:** Only works at close range where individual bullet holes can be identified. Impractical at distance or with overlapping groups.

**See:** Lesson 06 - Measurement Methods

---

### Replication

**Plain English:** Repeating a test under the same conditions to verify the result wasn't just luck.

**Example:** You test a load and get great results. Shooting the same test on a different day and getting similar results = successful replication.

**Importance:** Results that don't replicate were probably statistical flukes, not real effects.

**See:** Lesson 11 - Replication section

---

## S

### Sample

**Plain English:** A subset of the population that you actually test. The "cup" in the ocean-and-cup analogy.

**Example:** You load and test 30 rounds = your sample. The infinite possible rounds you could make = the population.

**Key insight:** Sample statistics (like sample SD) estimate population parameters (true SD) with some uncertainty.

**See:** Lesson 02 - What We Actually Mean by Consistency

---

### Sample Size (n)

**Plain English:** How many rounds you test. Written as "n" in formulas.

**Critical concept:** Larger samples give more reliable estimates of the true population.

**Guidelines:**
- n = 10-15: Adequate for average velocity
- n = 30+: Minimum for SD measurements
- n = 50+: Better for comparing loads
- n = 100+: Needed for strong claims

**See:** Lesson 03 - How Many Shots Do You Really Need

---

### Secant Ogive

**Plain English:** A bullet nose design with a sharp, aggressive curve. Common in VLD (Very Low Drag) bullets.

**Characteristics:**
- High ballistic coefficient (BC)
- More sensitive to seating depth
- Abrupt transition to rifling

**Examples:** Berger VLD, Sierra MatchKing (some)

**See:** Lesson 07 - Seating Depth section

---

### Standard Deviation (SD)

**Plain English:** A measure of spread or variation. Shows how much individual values typically differ from the average.

**For velocity:** Lower SD means more consistent velocities. Example: SD of 10 fps means shots typically vary by about 10 fps from the mean.

**Critical issue:** SD calculated from small samples systematically underestimates the true population SD (optimistic bias).

**See:** Lesson 05 - The Perverse Nature of Standard Deviation

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

**See:** Lesson 03 - Confidence Intervals

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

**Analogy:** Think of power like a metal detector's sensitivity. High power = you'll find a coin even if it's deep (small difference). Low power = you'll only find large objects close to the surface (big, obvious differences).

With small samples, your power is low—you can only detect huge differences. With large samples, your power is high—you can detect even small differences reliably.

**Factors affecting power:**
- Sample size (bigger = more power)
- Effect size (larger differences easier to detect)
- Variability (less noise = more power)

**Typical goal:** 80% power (80% chance of detecting real effect)

**See:** Lesson 10 - Statistical Power section

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

**See:** Lesson 10 - Significance vs Practical Importance

---

### Survivorship Bias

**Plain English:** When you only see successful results because failures aren't reported, creating a distorted view of reality.

**Example:** 100 shooters try OCW testing. 20 get lucky and post success stories online. 80 get inconclusive results and stay quiet. New shooters see only the 20 successes and think "OCW has a 100% success rate!"

**See:** Lessons 00, 07, 12

---

## T

### Tangent Ogive

**Plain English:** A bullet nose design with a gradual curve. Traditional design for most bullets.

**Characteristics:**
- Lower ballistic coefficient than secant
- Less sensitive to seating depth
- Gradual transition to rifling

**Examples:** Most traditional hunting bullets, Sierra MatchKing (some models)

**See:** Lesson 07 - Seating Depth section

---

### Temperature Sensitivity

**Plain English:** How much velocity changes with temperature. Some powder/cartridge combinations are more temperature-stable than others.

**Typical range:** 0.5 to 3.0 fps per degree Fahrenheit

**Why it matters:** A load developed at 70°F might be 40-50 fps faster at 95°F or slower at 30°F with temp-sensitive powder.

**Testing:** Properly test by acclimating ammunition to target temperature for 60+ minutes before shooting.

**See:** Lessons 04, 05 - Temperature sections

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

**See:** Lesson 10 - Statistical Tests

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

**See:** Lesson 10 - Errors in Testing

---

### Type II Error (False Negative)

**Plain English:** Failing to detect a real difference. Also called beta error or missed opportunity.

**Example:** Load A really is better, but your sample size was too small to detect the difference.

**Probability:** Set by your statistical power (1 - beta). With 80% power, you have 20% chance of Type II error.

**See:** Lesson 10 - Errors in Testing

---

## V

### Variance

**Plain English:** The square of standard deviation. Measures spread, but in squared units.

**Why square it?** It makes the math work better behind the scenes (negative deviations become positive, large deviations get weighted more). For practical use, stick with SD since it's in the same units as your data (fps or inches, not fps² or inches²).

**When you'll see it:** Variance appears in ANOVA (analysis of variance) and other statistical tests. You can always take the square root to get back to SD.

**Usage:** Used in statistical calculations, but SD is more interpretable because it's in the same units as your data.

**Relationship:** Variance = SD²

**See:** Lesson 05 - Spread measurements

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

**See:** Lesson 07 - Seating Depth testing

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

## Cross-Reference by Lesson

**Lesson 01:** Sample, Population, Bias, Monte Carlo Simulation
**Lesson 02:** Normal Distribution, Mean, Standard Deviation, Population, Sample
**Lesson 03:** Sample Size, Confidence Interval, Statistical Power, Standard Error
**Lesson 04:** Confounded Variables, Factorial Experiment, DOPE, Temperature Sensitivity
**Lesson 05:** Standard Deviation, Extreme Spread (velocity), Mean, Chronograph, Node
**Lesson 06:** Mean Radius, Extreme Spread (group), MOA, Precision, Accuracy
**Lesson 07:** OCW, Node, Ogive types, Jam/Jump, Survivorship Bias
**Lesson 10:** p-value, Statistical Significance, Type I/II Errors, Statistical Power, t-test
**Lesson 11:** p-hacking, Replication, Bias, Confirmation Bias

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

**Need more detail?** Each term references the lesson(s) where it's discussed in depth. Use this glossary as a quick reference, then dive into the specific lessons for complete explanations and examples.

[Back to Curriculum](../../README.md)
