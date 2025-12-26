[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ReevesJustin/data-driven-reloading/blob/main/notebooks/01_The_Biggest_Lie_in_Reloading_Testing.ipynb)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ReevesJustin/data-driven-reloading/main?filepath=notebooks/01_The_Biggest_Lie_in_Reloading_Testing.ipynb)

Time to complete: 10-15 minutes

# The Biggest Lie in Reloading Testing

## Goal: Visually prove small samples mislead

**Simple simulation:** Same exact load (fixed true SD = 12 fps). Generate 1,000 shots.
Then repeatedly pull random 3-, 5-, 10-, or 30-shot strings. Plot their SDs.
**Interactive slider:** Change sample size → watch how often you get **"magical" ** single-digit SD by *pure chance*.
**Key takeaway:** "Getting a low SD with less than 30 shots proves almost nothing."
Repeat for group sizes: Show how **3×5-shot groups** can look amazing even from a mediocre rifle.

## Simulating Velocity Standard Deviation

This code creates a **fake rifle** with a true SD of 15 fps (like really good factory ammo). We generate 10,000 virtual shots, then pull random samples of 3, 5, 10, or 30 shots to see how their SDs vary. **SD** is how spread out the speeds are. Like how consistent your shots are.

**Interpretation:** This graph shows the distribution of sample standard deviations (SD) for different shot counts from the same rifle. The red line marks the true SD (15 fps). Notice how smaller samples (3, 5 shots) produce highly variable SDs, often much lower than the true value by chance. Larger samples (30 shots) cluster closer to the truth, making them more reliable for detecting real differences in load precision.

**Key Takeaway:** **Getting a low SD with less than 30 shots proves almost nothing.**

**Interpretation:** This histogram compares group size distributions for 3-shot vs. 5-shot groups from a rifle with true 1.5 MOA precision. The 3-shot groups show more extreme variation, with many appearing much tighter than the true capability. The mean group sizes are smaller than expected due to sampling bias, and 5-shot groups are more consistent but still variable. Use this to understand why small groups can mislead you into thinking your rifle/load is better than it is.

- A surprising number of "one-hole" groups and sub-half MOA groups show up for a true 1.5 MOA rifle.
- Even when 1000 3-shot groups are fired the mean group size is notably smaller than the true precision of the rifle.

Our same true 1.5MOA rifle randomly produced groups that range from half MOA to over 3 MOA. Depending on the order you shot them, you might be very pleased or very displeased. Imagine if you were shooting 5 shot groups while varying powder charge looking for precision. You might think you have it but will get a very different apparent result the next time at the range.

**Interpretation:** These scatter plots display actual shot placements for six 5-shot groups, including the most extreme examples from 1000 simulations. The tightest group (smallest size) looks like exceptional accuracy, while the loosest appears poor. In practice, this variability means relying on a single group can lead to wrong conclusions about your rifle's true precision or load quality—always collect more data!

> **Key Takeaways**
> - Small sample sizes in reloading tests lead to unreliable results
> - Statistical significance requires adequate sample sizes
> - Common testing practices often fail to detect real differences
> - Simulation shows how luck can create false positives
> - 2/3 of 3-shot groups and over half of the 5-shot groups are lying to you
> - Even at 30-shot groups approximately half of them are lying to you, this is why it takes so many shots to validate claims regarding group sizes and SD
> - Proper testing methodology prevents chasing illusions

[Previous: 00_Welcome_and_Why_This_Matters.ipynb](00_Welcome_and_Why_This_Matters.ipynb) | [Next: 02_What_We_Actually_Mean_by_Consistency.ipynb](02_What_We_Actually_Mean_by_Consistency.ipynb)