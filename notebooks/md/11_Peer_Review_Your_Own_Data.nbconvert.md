[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ReevesJustin/data-driven-reloading/blob/main/notebooks/11_Peer_Review_Your_Own_Data.ipynb)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ReevesJustin/data-driven-reloading/main?filepath=notebooks/11_Peer_Review_Your_Own_Data.ipynb)

Time to complete: 10-15 minutes

# Peer Review Your Own Data — Self-Skepticism Checklist

**Goal:** Provide a self-skepticism checklist for reloading data analysis to avoid common pitfalls and ensure reliable conclusions.

## 1. The Checklist

Before declaring success in your reloading experiments, ask yourself these 10 questions. Each comes with a brief explanation and a key takeaway.

1. **Did I change only one variable at a time?**
   - Explanation: Testing multiple changes simultaneously makes it impossible to know which caused any observed effect.
   > **Takeaway:** Isolate variables to attribute results accurately.

2. **Is my sample size adequate for the effect I'm claiming?**
   - Explanation: Small samples can lead to false positives or negatives due to random variation.
   > **Takeaway:** Use statistical power calculations to ensure enough shots.

3. **Did I account for barrel temperature and other environmental factors?**
   - Explanation: Barrel heating can artificially inflate velocities over time, skewing results.
   > **Takeaway:** Control or measure environmental variables consistently.

4. **Am I cherry-picking my best group instead of averaging?**
   - Explanation: Selecting only the best data ignores natural variation and leads to over-optimism.
   > **Takeaway:** Analyze all data, not just the highlights.

5. **Would I bet $500 on this result repeating?**
   - Explanation: If you're not confident enough to risk money, the evidence isn't strong enough.
   > **Takeaway:** Treat skepticism as a bet on reality.

6. **Are there any obvious outliers or flyers in my data?**
   - Explanation: Extreme values can distort means and should be investigated or handled appropriately.
   > **Takeaway:** Inspect data for anomalies before trusting statistics.

7. **Did I test multiple groups per condition?**
   - Explanation: A single group per test can't distinguish signal from noise reliably.
   > **Takeaway:** Replicate conditions to confirm patterns.

8. **Is the difference I'm seeing larger than my measurement precision?**
   - Explanation: If changes are within error margins, they're likely noise, not signal.
   > **Takeaway:** Compare effects to your instrument's accuracy.

9. **Have I replicated this result at least once?**
   - Explanation: One-off results might be flukes; replication builds confidence.
   > **Takeaway:** Repeat experiments to verify findings.

10. **Am I letting the data speak or forcing it to say what I want?**
    - Explanation: Confirmation bias can make you ignore contradictory evidence.
    > **Takeaway:** Approach data with humility and openness.

## 2. Red Flags in Your Data

Visual examples of suspicious patterns using simulated data. These plots highlight common issues. (For GitHub viewing, static images would be embedded here if generated.)

## 3. The Pre-Registration Mindset

Pre-registration means deciding your analysis plan BEFORE collecting data. This prevents p-hacking (trying many analyses until you find significance) and confirmation bias (seeing what you want to see).

Example: If testing powder charges, decide in advance: "I'll measure mean velocity and SD for 20 shots per charge, and compare using t-tests." Don't adjust based on results.

Another example: Avoid adding "outlier removal" post-hoc; define criteria beforehand.

> **Takeaway:** Plan your analysis before you pull the trigger.

## 4. Interactive Data Health Check Tool

Paste your velocities (comma-separated) below and run the cell to get a health check. (For GitHub, this is interactive in Jupyter; static version shows example output.)

> **Key Takeaways**
> - Self-review process catches common analytical errors
> - Checklists ensure thorough data examination
> - Bias recognition improves result interpretation
> - Critical thinking about data prevents false conclusions
> - Systematic review methodology enhances reliability

[Previous: 10_When_Is_A_Result_Real.ipynb](10_When_Is_A_Result_Real.ipynb) | [Next: 12_What_About_The_Pros.ipynb](12_What_About_The_Pros.ipynb)