[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ReevesJustin/data-driven-reloading/blob/main/notebooks/03_How_Many_Shots_Do_You_Really_Need.ipynb)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ReevesJustin/data-driven-reloading/main?filepath=notebooks/03_How_Many_Shots_Do_You_Really_Need.ipynb)

Time to complete: 10-15 minutes

# How Many Shots Do You Really Need?

## Goal: Give practical rules of thumb

Show simulations: To tell if one powder truly has lower velocity spread than another (say, 10 fps vs. 15 fps true difference), how many shots per powder?
Slider/interactive: Desired confidence → required shots.
Practical guidelines:
– Quick screening: 20–30 shots (better than 10, but still rough).
– Serious comparison: 50–100 shots per variable.
– Proving a big claim (e.g., "this primer cuts SD in half"): 200+ shots.
Acknowledge reality: "Yes, it's a lot of ammo. But it's less than you'll waste chasing false leads."

## Central Limit Theorem and Minimum Samples for SD

Due to **central limit theorem**, the minimum samples to start looking at SD is 30. Explain that comparing two groups with 30 samples and SD's close means you have to shoot more to determine if they are **statistically different**.

## Minimum Shots for Precision

The **minimum number** of shots to call a rifle 1/2 MOA is 30.

## Average Convergence

The average or mean converges fast, so when zeroing or getting a velocity average, the average gets closer to the actual mean sooner, often **10 shots** is sufficient for zeroing or establishing a zero.

> **Key Takeaways**
> - Sample size calculations determine minimum shots needed for reliable results
> - Statistical power analysis helps design effective tests
> - Too few shots lead to inconclusive or misleading outcomes
> - Different variables require different sample sizes
> - Proper sample planning saves time and resources

[Previous: 02_What_We_Actually_Mean_by_Consistency.ipynb](02_What_We_Actually_Mean_by_Consistency.ipynb) | [Next: 04_Testing_One_Thing_at_a_Time.ipynb](04_Testing_One_Thing_at_a_Time.ipynb)