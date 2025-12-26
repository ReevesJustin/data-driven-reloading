[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ReevesJustin/data-driven-reloading/blob/main/notebooks/10_When_Is_A_Result_Real.ipynb)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ReevesJustin/data-driven-reloading/main?filepath=notebooks/10_When_Is_A_Result_Real.ipynb)

Time to complete: 10-15 minutes

# When IS a Result Real? — Power Analysis and Confidence Intervals

**Goal:** Learn to distinguish real effects from noise using statistical tools.


## 1. The Question You Should Always Ask

In reloading, we often see small differences between loads: "Primer A gives 5 fps more than Primer B." But is this difference *real*, or could it be due to random chance?

Statistical hypothesis testing helps us answer this. We set up a null hypothesis (H0: no difference) and alternative (H1: there is a difference). We collect data and see if the results are unlikely under H0.

The key question: **Before declaring a winner, ask: 'Could this difference have occurred by chance alone?'**

<div style="border: 2px solid black; padding: 10px; margin: 10px 0; background-color: #f9f9f9;">
**Bold Takeaway:** Always consider the possibility of random variation. Small samples can fool you into thinking there's a real effect when there isn't.
</div>

## 2. What is Statistical Power?

Statistical power is the probability of correctly rejecting the null hypothesis when it's false (detecting a real effect).

There are two types of errors:
- **Type I Error (False Positive):** Rejecting H0 when it's true (α, significance level).
- **Type II Error (False Negative):** Failing to reject H0 when it's false (β, 1 - power).

Power = 1 - β. Higher power means less chance of missing a real effect.

Factors affecting power: sample size (n), effect size (δ), significance level (α).


<div style="border: 2px solid black; padding: 10px; margin: 10px 0; background-color: #f9f9f9;">
**Bold Takeaway:** Increase sample size or effect size to boost power. Low power means you might miss real differences.
</div>

## 3. Confidence Intervals: Your Uncertainty Made Visible

A confidence interval (CI) gives a range where the true parameter likely lies, with a certain probability (e.g., 95%).

For means, CI width depends on sample size: larger n → narrower CI.

Small samples give wide intervals — be skeptical of 'precise' results from few shots.


<div style="border: 2px solid black; padding: 10px; margin: 10px 0; background-color: #f9f9f9;">
**Bold Takeaway:** Small samples give wide intervals — be skeptical of 'precise' results from few shots.
</div>

## 4. The Magic Number Calculator

Calculate the sample size needed to achieve desired power.

Formula (approximate for two-sample t-test): n = ((z_α + z_β) / δ)^2 * 2

Where δ is effect size (difference / SD).


## 5. Real Example: Is Primer A Really Better Than Primer B?

Simulate: Primer A: μ=2850, σ=10; Primer B: μ=2860, σ=10. Sample size n=20 each.

Perform t-test, show p-value, CI, power.


Discussion: With n=20, power is moderate. If p<0.05, the difference might be real, but check CI and power.

<div style="border: 2px solid black; padding: 10px; margin: 10px 0; background-color: #f9f9f9;">
**Bold Takeaway:** Always check power and CIs. A 'significant' p-value doesn't mean the effect is practically important.
</div>

> **Key Takeaways**
> - Statistical significance testing determines if results are real
> - P-values and confidence levels quantify result reliability
> - Type I and Type II errors affect conclusion validity
> - Power analysis ensures adequate test sensitivity
> - Proper statistical methods validate or refute claims

[Previous: 10_When_IS_a_Result_Real.ipynb](10_When_IS_a_Result_Real.ipynb) | [Next: 11_Peer_Review_Your_Own_Data.ipynb](11_Peer_Review_Your_Own_Data.ipynb)