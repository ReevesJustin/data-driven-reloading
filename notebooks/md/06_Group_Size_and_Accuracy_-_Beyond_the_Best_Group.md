[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ReevesJustin/data-driven-reloading/blob/main/notebooks/06_Group_Size_and_Accuracy_-_Beyond_the_Best_Group.ipynb)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ReevesJustin/data-driven-reloading/main?filepath=notebooks/06_Group_Size_and_Accuracy_-_Beyond_the_Best_Group.ipynb)

Time to complete: 10-15 minutes

# Group Size and Accuracy - Beyond the Best Group

## Your Best Group Is Lying to You

You've just finished shooting at the range. You're packing up, looking over your targets. One group in particular catches your eye:

**Five shots. All touching. Maybe 0.4 MOA.**

You snap a photo, head home, post it online: "Finally dialed in this load! Consistent 0.4 MOA!"

A week later, you're back at the range. Same rifle, same ammo, same everything. You shoot five more groups. They measure 0.9, 1.1, 0.7, 1.3, 0.8 MOA.

What happened? Did your rifle forget how to shoot? Did the ammo go bad? Did you mess up your fundamentals?

**None of the above. That first 0.4 MOA group was luck. You just didn't know it yet.**

This is the single most common mistake in reloading: judging a load by its best group instead of its average behavior. It feels intuitive. "This load CAN shoot 0.4 MOA—I've seen it!" But that logic is backwards.

In this notebook, you'll learn:
- Why extreme spread (traditional group size) grows forever and misleads you
- Mean radius: a better metric that actually stabilizes
- The "best group bias" and why your smallest groups are 30-40% better than your rifle's true capability
- How to aggregate data honestly for real precision measurement
- The critical difference between precision (tight groups) and accuracy (hitting your aim point)
- Why you should shoot one big 50-round group instead of ten 5-round groups

By the end, you'll understand how to measure on-target performance honestly—and stop being fooled by lucky groups that never repeat.

---

## The Problem With Extreme Spread (Traditional Group Size)

When you measure a group, you're probably measuring **extreme spread (ES)**: the distance between your two farthest-apart shots.

```
Five shots on target:
- Four in the center (tight cluster)
- One "flyer" 2 inches out

Group size: 2 inches (because of that one shot)
```

**Extreme spread has a fundamental problem: it can only stay the same or grow, never shrink.**

### Why Extreme Spread Grows Forever

Think about it:
- Your first two shots set the initial ES
- Shot 3 either lands inside that spread (ES stays same) or outside (ES grows)
- Shot 4 either lands inside or outside
- Shot 5... and so on

**Every new shot has a chance to increase ES but can never decrease it** (unless you get lucky and it lands exactly between your current extremes).

**Practical impact:**

A true 1.0 MOA rifle (that's its real average capability):
- 3-shot group: Probably 0.6-0.8 MOA (looks better than it is!)
- 5-shot group: Probably 0.8-1.0 MOA (getting closer to truth)
- 10-shot group: Probably 1.0-1.3 MOA (now representative)
- 20-shot group: Probably 1.3-1.5 MOA (one unlucky flyer dominates)
- 50-shot group: Probably 1.6-1.9 MOA (extreme shots eventually appear)

**Does this mean the rifle got worse as you shot more?** No. It means extreme spread is a terrible metric for comparing loads unless sample sizes are identical.

### The Flyer Problem

Every shooter has experienced this: Four shots in a tiny cluster, one shot way out. "It's a flyer! I pulled it!"

Maybe you did pull it. Or maybe:
- That's just normal variation (remember the cup and the ocean?)
- Your rifle naturally produces that spread, and four shots happened to cluster
- Random chance gave you four lucky ones and one normal one

**The problem:** We call outliers "flyers" and ignore them because they don't match our expectations. But if you shoot enough groups, EVERY group has outliers. They're not flyers—they're reality.

**The honest approach:** Include all shots. Outliers are data, not mistakes (unless you actually flinched and know it).

> **Key Insight**
>
> Extreme spread (traditional group size) grows as sample size increases. This makes it useless for comparing loads with different sample sizes. A 0.8 MOA 5-shot group and a 1.2 MOA 30-shot group might represent the SAME rifle—the larger sample just caught more of the natural variation.

---

## Mean Radius: The Better Metric

There's a better way to measure precision: **mean radius (MR)**.

Instead of measuring the distance between your two worst shots, mean radius measures **the average distance of each shot from the group center**.

### How to Calculate Mean Radius

**Step 1:** Find the center of your group (average X coordinate, average Y coordinate)

**Step 2:** Measure the distance from each shot to that center

**Step 3:** Average those distances

**Example:**

Five shots with distances from center:
- Shot 1: 0.3 inches
- Shot 2: 0.5 inches
- Shot 3: 0.2 inches
- Shot 4: 0.6 inches
- Shot 5: 0.4 inches

Mean radius = (0.3 + 0.5 + 0.2 + 0.6 + 0.4) / 5 = **0.4 inches**

### Why Mean Radius Is Better

**1. It stabilizes with more shots** (unlike extreme spread, which grows)

A true 1.0 MOA rifle measured by mean radius:
- 5-shot group: MR probably 0.3-0.4 MOA
- 10-shot group: MR probably 0.35-0.38 MOA
- 30-shot group: MR probably 0.36-0.37 MOA
- 50-shot group: MR probably 0.36-0.37 MOA

Notice: It converges toward the true value instead of growing forever.

**2. It uses all shots equally** (not dominated by one outlier)

Extreme spread: One bad shot ruins the measurement
Mean radius: One bad shot contributes, but doesn't dominate

**3. It's consistent across sample sizes**

You can compare a 10-shot MR to a 30-shot MR meaningfully. You can't do that with extreme spread.

### The Conversion (Rough Approximation)

For typical shooting:
- **Mean Radius ≈ Extreme Spread × 0.3** (for same group)

So a 1.0 MOA group (extreme spread) has a mean radius of about 0.3 MOA.

**Why this matters:** When you report MR, the numbers seem "smaller" but they're more honest and more comparable.

![Extreme Spread vs Mean Radius Comparison](../static/nb06_plot18_es_vs_mr_comparison.png)

**Figure 1:** Comparison of extreme spread (ES) versus mean radius (MR) as shots are added to a group from a true 1.0 MOA rifle. While extreme spread continues climbing with each additional shot (reaching 1.6+ MOA by 50 shots), mean radius quickly stabilizes around 0.36 MOA after just 10-15 shots and remains consistent. This demonstrates why mean radius is the superior metric - it converges to truth and allows meaningful comparison across different sample sizes, unlike extreme spread which grows forever.

> **Critical Takeaway**
>
> Mean radius is a better precision metric than extreme spread because it stabilizes with more data instead of growing forever. For comparing loads, use mean radius. It's honest, consistent, and actually tells you about your rifle's capability.

---

## The Best Group Bias: Why Your Smallest Groups Lie

Here's a devastating truth that most shooters never realize:

**If you shoot 10 groups and pick the smallest one, it will be approximately 30-40% smaller than your rifle's true capability.**

Not 5% smaller. Not 10% smaller. **30-40% smaller.**

This is pure statistics, and it's wrecking load development decisions across the reloading world.

### The Mechanism

Imagine your rifle's true capability is 1.0 MOA (that's the population average if you shot 1,000 groups).

When you shoot 10 groups, you're taking 10 random samples from that population. Some will be better than 1.0 MOA (lucky random variation), some will be worse.

**The best of those 10 will average around 0.6 MOA.**

The worst will average around 1.4 MOA.

**Neither represents your rifle.** The average of all 10 (about 1.0 MOA) represents your rifle.

### The Proof By Simulation

Let's simulate a true 1.5 MOA rifle shooting 10 five-shot groups:

```
Group 1: 1.2 MOA
Group 2: 1.6 MOA
Group 3: 0.9 MOA ← "Best group!"
Group 4: 1.8 MOA
Group 5: 1.3 MOA
Group 6: 1.7 MOA
Group 7: 1.1 MOA
Group 8: 1.5 MOA
Group 9: 2.0 MOA ← "Worst group"
Group 10: 1.4 MOA

Average: 1.45 MOA (close to truth)
Best: 0.9 MOA (40% better than truth!)
Worst: 2.0 MOA (33% worse than truth!)
```

If you judge this rifle by its best group, you'd think it's a 0.9 MOA rifle. **You'd be wrong by 60%.**

### Why This Matters for Load Development

**Common mistake:**

Shooter tests three loads:
- Load A: Shoots 5 groups, best is 0.7 MOA → "Amazing!"
- Load B: Shoots 5 groups, best is 0.9 MOA → "Good"
- Load C: Shoots 5 groups, best is 1.1 MOA → "Mediocre"

Conclusion: Load A is clearly superior.

**The problem:** All three might be identical 1.2 MOA loads, and Load A just got lucky. Without looking at ALL groups from each load, you can't tell.

**The fix:**

Look at the **average** of all groups for each load:
- Load A: Average 1.3 MOA (best was 0.7, others were 1.4, 1.5, 1.2, 1.6)
- Load B: Average 1.2 MOA (best was 0.9, others were 1.1, 1.3, 1.2, 1.4)
- Load C: Average 1.1 MOA (best was 1.1, others were 0.9, 1.2, 1.0, 1.3)

**New conclusion:** Load C is actually the best! Load A's amazing 0.7 MOA group was a lucky outlier.

![The Best Group Bias](../static/nb06_plot19_best_group_bias.png)

**Figure 2:** Distribution of "best groups" from 100 simulated trials, each shooting 10 five-shot groups from a true 1.5 MOA rifle. The best groups average 1.0 MOA - a systematic 33% underestimate of true capability. This proves that selecting your smallest group from a set of attempts will consistently mislead you by 30-40%. If you judge loads by best groups rather than averages, you're cherry-picking lucky samples and making decisions based on statistical artifacts, not real performance differences.

### Real-World Impact

Browse any reloading forum. Count how many people post their "best group" as evidence their load is dialed in.

**They're all doing it wrong.**

The correct approach:
1. Shoot 5-10 groups with a load
2. Calculate the **average** group size (or better, mean radius)
3. THAT number represents the load
4. Compare averages between loads, not best groups

**Bonus honesty points:** Report both average and best group. "This load averages 1.2 MOA with a best of 0.8 MOA." Now people can evaluate properly.

> **Critical Takeaway**
>
> Your best group from a set is systematically 30-40% smaller than your true capability due to random variation. Judging loads by best groups is cherry-picking lucky samples. Always use average group size or, better yet, aggregate all shots into one large sample.

---

## The String of Fire Concept: One Big Group vs. Many Small Ones

Here's a better way to test: **Stop shooting multiple small groups. Shoot one large group.**

### Traditional Approach

- Shoot 10 five-shot groups
- Measure each group
- Average the group sizes (if you're honest)
- Or pick the best group (if you're fooling yourself)

**Problems:**
- 10 separate aiming processes (introduces variation)
- 10 separate zero confirmations (wind shifts, mirage changes)
- Temptation to cherry-pick
- Time-consuming measurement

### String of Fire Approach

- Shoot 50 rounds at one large target
- Measure the aggregate (one measurement of all 50 shots)
- Calculate mean radius from center

**Advantages:**
- One aiming process (removes that source of variation)
- Shows true dispersion pattern
- No cherry-picking possible
- Faster measurement
- More honest result

### The Data Is Identical (Almost)

Both approaches fire the same 50 rounds. But the aggregated approach:
- Removes target-to-target variables (e.g., different wind for each group)
- Gives you one clear number instead of a distribution you have to interpret
- Is harder to cheat (can't ignore "bad targets")

**Practical implementation:**

Use a large target (24" square or bigger). Mark your aiming point clearly. Fire all shots at the same point. Measure the center (average position of all shots). Calculate mean radius (average distance from that center).

**Interactive Element Placeholder:**
```python
# Interactive widget: "10 Groups vs 1 Aggregate"
#
# Setup: True rifle = 1.2 MOA capability
#
# Simulation:
# - Generate 50 shots from this rifle
#
# Display Option 1: "Traditional approach"
# - Show shots divided into 10 five-shot groups
# - Each group on separate target
# - Measure each group's ES
# - Show list of 10 group sizes
# - Show average
# - User tempted to focus on best group
#
# Display Option 2: "Aggregate approach"
# - Show all 50 shots on one large target
# - Calculate mean radius
# - Show aggregate result
# - Clean, single number
#
# Comparison:
# - Both approaches used same 50 shots
# - Aggregate approach gives cleaner answer
# - Traditional approach invites cherry-picking
#
# Aha moment: "Same data, but aggregating it prevents me from
# fooling myself by focusing on the lucky groups!"
```

---

## Precision vs. Accuracy: Not the Same Thing

This is a critical distinction that gets confused all the time.

**Precision:** How close your shots are to **each other**
**Accuracy:** How close your shots are to your **aim point**

### The Four Scenarios

**Scenario 1: High Precision, High Accuracy**
- Tight group (precise)
- Centered on aim point (accurate)
- This is the goal

**Scenario 2: High Precision, Low Accuracy**
- Tight group (precise)
- Off-center from aim point (inaccurate)
- Your zero is off, or wind pushed your group

**Scenario 3: Low Precision, High Accuracy**
- Scattered shots (imprecise)
- Centered on aim point on average (accurate)
- Rifle/ammo has lots of variation, but zero is good

**Scenario 4: Low Precision, Low Accuracy**
- Scattered shots (imprecise)
- Off-center from aim point (inaccurate)
- Multiple problems compounding

### Why This Matters

**Common mistake:** Blaming your ammunition for an accuracy problem when the real issue is a scope zero or wind call.

**Example:**

You're testing a new load. You shoot a group. It's 1.2 MOA (not terrible) but it's 3 inches left of your aim point.

**Wrong conclusion:** "This load shoots poorly."

**Right conclusion:** "This load has 1.2 MOA precision. The fact that it's off-center means my zero has shifted or wind affected this group. That's an accuracy issue, not a precision issue."

### Wind: The Accuracy Killer

Wind doesn't make your groups bigger (precision issue). **Wind shifts your group center** (accuracy issue).

**Simulation scenario:**

Calm day: 1.0 MOA group centered on target
Windy day: 1.0 MOA group centered 4 inches right of target

The load didn't change. The precision didn't change. Wind moved the center.

**Don't blame your load for wind calls.** Separate precision problems from accuracy problems.

**Interactive Element Placeholder:**
```python
# Interactive widget: "Precision vs Accuracy"
#
# Display: Target with aim point marked
#
# User controls:
# - Slider 1: Precision (0.5 to 2.0 MOA) - controls group tightness
# - Slider 2: Accuracy offset X (0 to 5 inches)
# - Slider 3: Accuracy offset Y (0 to 5 inches)
#
# Simulation:
# - Generate 20 shots with specified precision
# - Offset group center by specified accuracy offsets
#
# Display shows:
# - Shots on target
# - Group size measurement (precision)
# - Distance of group center from aim point (accuracy error)
# - Labels: "Precision: X MOA" and "Accuracy error: Y inches"
#
# User can adjust sliders to see:
# - Tight group, badly off-center (precise but inaccurate)
# - Scattered group, well-centered (imprecise but accurate)
# - Tight group, well-centered (precise and accurate - the goal)
#
# Aha moment: "I've been blaming my ammo for groups that were off-center
# due to wind. The group SIZE was fine! It was just SHIFTED."
```

### Testing for Precision vs. Testing for Accuracy

**Precision test:**
- Control variables (bench, bags, calm conditions)
- Shoot many rounds
- Measure spread (MR or ES)
- Goal: Understand ammunition consistency

**Accuracy test:**
- Field conditions
- Multiple sessions, different days
- Track where groups center relative to aim point
- Goal: Verify zero, practice wind calls

Don't confuse the two. A precision test in perfect conditions tells you about your ammo and rifle. It doesn't tell you if your zero is correct or if you can call wind.

---

## How to Honestly Measure Precision

Based on everything we've learned, here's the correct process:

### Option A: Aggregate Approach (Best)

1. **Set up:** Large target, marked aim point, stable position
2. **Shoot:** 30-50 rounds at the same aim point, same session
3. **Measure:** Calculate mean radius from group center
4. **Result:** One clean number representing your load's precision

**Advantages:**
- No cherry-picking possible
- Most honest result
- Fastest to measure

**Disadvantages:**
- Requires large target
- Can't easily compare to traditional group size claims (but that's actually good—stops the comparison trap)

### Option B: Multiple Groups, Honestly Averaged (Second Best)

1. **Set up:** Multiple targets or marked aim points
2. **Shoot:** 5-10 groups of 5-10 shots each
3. **Measure:** Each group size (ES or MR)
4. **Calculate:** Average across all groups
5. **Report:** "Average group size: X MOA (best: Y, worst: Z)"

**Advantages:**
- Familiar to traditional shooters
- Gives you distribution information (best/worst/average)
- Can compare to factory claims (they also use small groups)

**Disadvantages:**
- Target-to-target variation adds noise
- More measurement work
- Temptation to cherry-pick

### Option C: Ragged Hole Method (For Benchrest and Close Range)

Some benchrest shooters shoot all shots into one target and measure the overall "ragged hole" perimeter.

**This works at close range (100-200 yards) where you can see individual bullet holes.**

At distance or with calibers where holes overlap, this becomes impractical. Use mean radius instead.

### What to Report

**Minimum honest reporting:**
"Average group size: 1.1 MOA (5 groups, 5 shots each)"

**Better reporting:**
"Mean radius: 0.35 MOA (50 shots, aggregated)"

**Best reporting:**
"Mean radius: 0.35 MOA (50 shots), tested across 2 sessions (0.34 and 0.36 MOA)"

The more data and context you provide, the more trustworthy your claim. Single amazing groups mean nothing without context.

---

## The Path to Honest Assessment

You now understand:
- Extreme spread grows forever; mean radius stabilizes (use MR)
- Best groups are 30-40% better than true capability (use averages)
- Aggregating all shots is better than multiple small groups
- Precision (group tightness) and accuracy (hitting aim point) are different
- Wind shifts groups without making them larger (don't blame ammo for wind)

**This fundamentally changes how you evaluate ammunition:**

Instead of: "I shot a 0.6 MOA group! This load is amazing!"

You'll say: "I shot 50 rounds. Mean radius 0.38 MOA. Repeatable across sessions. This load is legitimately good."

Instead of: "This load shoots terribly—groups were all over the place!"

You'll ask: "Was that precision (large groups) or accuracy (groups off-center)? What was the average group size, not just the worst one?"

In the next notebook, we'll apply this honest thinking to real-world examples—dissecting common myths and claims you see online, and learning to spot the red flags of bad testing.

You've learned how to measure velocity honestly (Notebook 05) and precision honestly (this notebook). Now let's use those skills to evaluate claims critically.

> **Key Takeaways**
> - Extreme spread (traditional group size) grows with sample size; mean radius stabilizes—use MR for honest measurement
> - Your best group from a set is 30-40% smaller than true capability due to random variation—always use averages, never cherry-pick
> - Shooting one large aggregate (30-50 shots) is better than many small groups (removes cherry-picking temptation)
> - Precision is group tightness; accuracy is hitting aim point—these are different problems with different solutions
> - Wind shifts group centers without enlarging groups—don't blame ammunition for accuracy issues
> - Report averages across multiple groups or sessions, not single lucky results

---

## Coming Up Next

**In Notebook 07**, we'll dissect real-world examples of common myths and flawed testing methods. You'll learn:
- Specific examples of popular methods that fail under scrutiny
- How to spot red flags in online claims
- Simulations showing why common approaches mislead
- What to do instead of these flawed methods
- How to politely challenge claims in your community

You now have the tools to measure honestly. Next, you'll learn to apply those tools to evaluate what you see online—and separate signal from noise.

[Previous: 05_Velocity_Data_-_What_to_Measure_and_How_to_Think_About_It](05_Velocity_Data_-_What_to_Measure_and_How_to_Think_About_It.ipynb) | [Next: 07_Real_Examples_-_Dissecting_Common_Myths](07_Real_Examples_-_Dissecting_Common_Myths.ipynb)
