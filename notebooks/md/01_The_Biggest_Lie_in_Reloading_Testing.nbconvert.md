[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ReevesJustin/data-driven-reloading/blob/main/notebooks/01_The_Biggest_Lie_in_Reloading_Testing.ipynb)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ReevesJustin/data-driven-reloading/main?filepath=notebooks/01_The_Biggest_Lie_in_Reloading_Testing.ipynb)

Time to complete: 10-15 minutes

# The Biggest Lie in Reloading Testing

## Goal: Visually prove small samples mislead

**Simple simulation:** Same exact load (fixed true SD = 12 fps). Generate 1,000 shots.
Then repeatedly pull random 5-, 10-, or 20-shot strings. Plot their SDs.
**Interactive slider:** Change sample size → watch how often you get **"magical" ** single-digit SD by *pure chance*.
**Key takeaway:** "**A low SD over 10 shots proves almost nothing. It happens by luck more often than you think.**"
Repeat for group sizes: Show how **3×5-shot groups** can look amazing even from a mediocre rifle.

## Simulating Velocity Standard Deviation

This code creates a **fake rifle** with a true SD of 15 fps (like really good factory ammo). We generate 10,000 virtual shots, then pull random samples of 5, 10, 20, or 50 shots to see how their SDs vary. **SD** is how spread out the speeds are. Like how consistent your shots are.

**Key Takeaway:** **A low SD over 10 shots proves almost nothing. It happens by luck more often than you think.**

> **Key Takeaways**
> - Small sample sizes in reloading tests lead to unreliable results
> - Statistical significance requires adequate sample sizes
> - Common testing practices often fail to detect real differences
> - Simulation shows how luck can create false positives
> - Proper testing methodology prevents chasing illusions

[Previous: 00_Welcome_and_Why_This_Matters.ipynb](00_Welcome_and_Why_This_Matters.ipynb) | [Next: 02_What_We_Actually_Mean_by_Consistency.ipynb](02_What_We_Actually_Mean_by_Consistency.ipynb)