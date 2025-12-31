# Appendix B: Research Status and Evidence Levels

## Understanding What We Know (And How We Know It)

Have you ever read a forum post claiming "seating depth doesn't matter—I tested it" only to find another claiming "seating depth is EVERYTHING"? Both shooters ran tests. Both got results. Both are convinced. Who's right?

The answer depends not just on WHAT they found, but on HOW THEY TESTED IT—and more importantly, what level of evidence backs the claim.

This curriculum makes many claims. Some are backed by extensive research, others by simulations and statistical theory, and some represent areas where rigorous research is lacking. Here's an honest assessment of the evidence levels behind everything we've taught you.

---

## Evidence Level Quick Reference

| Topic | Evidence Level | Sample Size Needed | Lesson Coverage | Key Source |
|-------|---------------|-------------------|-----------------|------------|
| Sample size requirements | Established | 30+ per condition | Lesson 03 | Statistical theory |
| Mean radius vs extreme spread | Established | 10+ for comparison | Lesson 06 | Precision Rifle Blog |
| Velocity nodes | Simulation + Empirical debunking | 30+ per charge | Lesson 05, 07 | Hornady testing |
| OCW methodology | Simulation-based critique | 30+ validation | Lesson 07 | None |
| Ladder tests | Partial validation | 10+ for pressure only | Lesson 07 | Litz (recoil) |
| Best group bias | Proven | 5 groups × 5 shots | Lesson 06 | Sampling theory |
| Seating depth effects | Limited research | 30+ per depth | Lesson 07 | Reloading All Day |
| Primer selection | Emerging evidence | 30+ per primer | Lesson 07 | Reloading All Day |
| Brass preparation | Research gap | 30+ per condition | Not covered | None |
| Recoil management impact | Established | N/A | Lesson 09, 12 | Litz TOP Gun |

*(Full details in sections below)*

---

## Well-Researched and Validated Areas

These claims are supported by published research, controlled experiments, or established statistical theory:

### Statistical Sampling Behavior and Precision Measurement
- **Source:** Mathematical statistics (established field), Cal Zant / Precision Rifle Blog
- **Evidence:** Textbook-level theory + extensive practical testing
- **Examples:** Sample size requirements (Lesson 03), confidence intervals (ranges where the truth likely lives - Lesson 10), bias in small samples (why 3-shot groups lie to you - Lesson 01), and distribution properties (how your results spread out - Lesson 02)
- **Key findings:**
  - Think of it like taste-testing soup: one spoonful (small sample) might miss the salt that settled at the bottom, but five spoonfuls from different spots (large sample) give you the real flavor
  - Minimum 30 shots for reliable SD/ES estimation
  - Confidence intervals shrink with larger samples (demonstrated in Lesson 03)
- **Reference:** [Precision Rifle Blog: Statistics for Shooters](https://precisionrifleblog.com/2020/12/16/statistics-for-shooters-executive-summary/)

### Precision Measurement: Mean Radius vs. Extreme Spread
- **Source:** Military ballistics standards, Cal Zant statistical analysis, Precision Rifle Blog
- **Evidence:** Mathematical proof + extensive practical testing
- **Key findings:**
  - **Mean Radius (MR):** Uses all shots; converges to true precision as sample size increases; statistically superior for comparing loads (demonstrated in Lesson 06)
  - **Extreme Spread (ES):** Uses only two shots (widest pair); grows with sample size; useful for understanding worst-case scenarios but poor for load comparison
- **Examples:** MR provides stable precision estimate with 10+ shots; ES continues to grow indefinitely as you shoot more (mathematical property, not rifle inconsistency)
- **Recommendation:** Use mean radius for load development comparisons; use ES to understand maximum dispersion limits
- **References:**
  - [Measuring Group Size: Mean Radius](https://precisionrifleblog.com/2020/12/12/measuring-group-size-statistics-for-shooters/)
  - [Outdoor Life: What is Mean Radius?](https://www.outdoorlife.com/guns/what-is-mean-radius/)

### Bullet Ballistic Performance
- **Source:** Bryan Litz, Applied Ballistics Research
- **Evidence:** Controlled testing with Doppler radar (high-tech speed measurement tools), published books and papers
- **Examples:** Ballistic coefficients (how well a bullet slices through air), drag models (mathematical predictions of bullet slowdown), bullet stability calculations

### Temperature Effects on Propellant
- **Source:** Denton Bramwell (temperature measurement studies published in Varmint Hunter Magazine), SAAMI protocols (industry testing standards)
- **Evidence:** Experimental measurements with controlled conditions
- **Examples:** How long ammunition needs to adjust to temperature changes (1+ hours), how bullet speed changes with hot or cold weather (discussed in Lesson 04)
- **Analogy:** Your ammo is like a cold car engine—it needs time to adjust to the weather. Leave it in a hot truck for an hour, and your bullets will fly faster than if you just pulled them from an air-conditioned room.

### Standard Deviation Bias in Small Samples
- **Source:** Denton Bramwell, statistical sampling theory
- **Evidence:** Both mathematical proof (the math guarantees it) and computer simulations (we tested it thousands of times)
- **Examples:** Small samples underestimate true SD (3-shot groups make your rifle look better than it is - demonstrated in Lesson 01), need large samples for accurate ES/SD (you need 30+ shots to know the truth - Lesson 05)

### Recoil Management Impact on Precision
- **Source:** Bryan Litz TOP Gun research
- **Evidence:** Controlled comparison of ammunition vs. shooter variables
- **Examples:** Majority of group size variance comes from you (how you hold the rifle, how you manage recoil), with ammunition quality contributing lesser but still important variance (discussed in Lesson 09 and Lesson 12)
- **Analogy:** It's like handwriting—70% depends on how steady your hand is, only 30% on which pen you use.

---

## Simulation-Supported (But Not Experimentally Validated)

While the topics above have solid experimental validation, the following claims rely primarily on statistical simulations and theory. Simulations show what random variation CAN create, but they can't prove what physical phenomena DON'T exist:

### Velocity Nodes Don't Exist
- **Evidence level:** Simulation-based + theoretical + large-sample empirical testing
- **What we can prove:** Random variation creates convincing node patterns in small samples (see Lesson 05 Figure 16: Velocity Node Illusion and Lesson 07 ladder test analysis). Hornady large-sample testing found no repeatable accuracy nodes with adequate sample sizes.
- **What we can't prove:** That barrel harmonics never create any accuracy benefit (theoretical possibility remains, but practical evidence lacking)
- **Status:** Strong evidence against nodes from simulation, theory, and empirical testing
- **Caveat:** Hornady research discussed in podcast (Episode 50); formal peer-reviewed paper not published
- **Recommendation:** If someone claims nodes exist, ask for large-sample proof (30+ shots per charge). Test yourself if you believe they're real for your rifle.
- **Reference:** [Hornady Podcast Episode 50](https://www.hornady.com/podcast)

### OCW Methodology (Optimal Charge Weight) Ineffectiveness
- **Evidence level:** Simulation-based + statistical theory
- **What we can prove:** 3-shot samples are too small. They can't tell the difference between real patterns and random luck (see Lesson 07: Real Examples - OCW section)
- **What we can't prove:** That OCW never identifies genuinely better charge weights
- **Status:** No published controlled validation of OCW with proper blinded methodology
- **Recommendation:** Better methods exist. If you use OCW, validate results with 30+ shot samples.

### Ladder Test Limitations
- **Evidence level:** Simulation + Bryan Litz recoil research
- **What we can prove:** How you manage recoil affects up/down spread more than powder charge does (Litz TOP Gun research). Small samples create false patterns (statistical fact demonstrated in Lesson 07).
- **What we can't prove:** That ladder tests provide zero useful information
- **Status:** Partial validation (recoil dominance researched; small sample problems are statistical fact)
- **Recommendation:** Use ladder tests only to check for pressure signs (flattened primers, sticky bolts), not to find "nodes" or best accuracy

### Best Group Bias (Cherry-Picking Problem)
- **Evidence level:** Statistical simulation + sampling theory (demonstrated in Lesson 06)
- **What we can prove:** Picking your best 3-shot group makes your rifle look better than it really is
- **What we can't prove:** The exact amount of lying for every sample size (depends on computer models)
- **Status:** Mathematical certainty + simulation demonstration
- **Analogy:** Shooting one 3-shot group and keeping the best is like flipping a coin 3 times, getting heads twice, and claiming the coin lands heads 67% of the time. Do it 100 times and you'll see it's really 50%.
- **Recommendation:** Average many groups instead of picking your best one (Lesson 06 composite groups section - use group aggregation methodology)

---

## Under-Researched Areas (Research Gaps)

Finally, several commonly discussed topics have limited public research with proper sample sizes. This doesn't mean they don't matter—it means the burden of proof is on individual shooters to test systematically:

### Seating Depth Effects (How Far the Bullet Sits in the Case)
- **Available research:**
  - Bryan Litz work on bullet nose shapes (VLD = Very Low Drag with sharp point, tangent = gradual curve, hybrid = combination of both)
  - Reloading All Day controlled testing: ["I Failed to Prove Seating Depth Matters"](https://www.reloadingallday.com/post/i-failed-to-prove-seating-depth-matters) - proper sample sizes, multiple seating depths, found no statistically significant differences
- **Missing research:** Large-sample controlled studies across more bullet types and cartridges
- **Anecdotal reports:** Many shooters report seating depth matters for VLDs; mixed results for other shapes
- **Status:** Limited testing failed to find significant effects with proper sample sizes. The theory exists (bullet-to-rifling alignment and engraving consistency), but we don't know how much it matters in practice.
- **Recommendation:** Test if using VLD or secant ogive bullets with large jumps (0.020-0.040") to save time. Don't assume it matters without testing YOUR specific bullet and rifle. (See Lesson 07 for detailed discussion)

### Brass Preparation Effects (Weight Sorting, Volume Sorting, Neck Turning)
- **Available research:** Minimal published work with proper sample sizes
- **Missing research:** Controlled experiments isolating each prep step with 30+ shot samples
- **Anecdotal reports:** Extreme Long Range (ELR) and benchrest shooters report benefits
- **Status:** The theory makes sense (more consistent brass = more consistent velocity). But we lack proof.
- **Recommendation:** Test for your system at your precision level. Don't assume benefits.

### Primer Selection Effects
- **Available research:**
  - Reloading All Day controlled testing: ["Do Primers Affect Consistency?"](https://www.reloadingallday.com/post/do-primers-affect-consistency) - proper sample sizes (30+ rounds), multiple primer types, measured both velocity and precision effects
- **Missing research:** Controlled comparisons across more cartridges and powder types
- **Anecdotal reports:** Shooters report significant velocity and ES changes with primer swaps
- **Status:** Limited testing shows primers DO affect both velocity and consistency. The reason is clear: primer energy affects how evenly powder burns. How much it matters varies by load.
- **Recommendation:** Test primer selection if chasing extremely low ES or if velocity changes matter. Effects are real but may be smaller than powder choice in most cases.

### Flash Hole Deburring/Uniforming
- **Available research:** Very limited, None we're aware of using sufficient sample sizes
- **Missing research:** Controlled testing with proper samples
- **Anecdotal reports:** Mixed—some claim improvements, others see no difference
- **Status:** Theoretical mechanism weak; likely minimal impact
- **Recommendation:** Low priority unless you're at extreme precision levels

### Neck Tension / Case Annealing Effects
- **Available research:** Limited; some evidence annealing improves consistency more than weight sorting
- **Missing research:** Large-sample controlled comparison of annealing vs. other prep steps
- **Anecdotal reports:** Competitive shooters report measurable benefits from consistent neck tension
- **Status:** Theoretical mechanism strong (consistent bullet grip = consistent pressure curve); validation lacking
- **Recommendation:** Test if pursuing extreme consistency; may provide better return than brass sorting or flash hole work

### Runout/Concentricity Effects
- **Available research:** Minimal controlled testing with proper samples
- **Missing research:** Systematic testing isolating runout from other variables
- **Anecdotal reports:** Some evidence suggests runout matters more than brass weight sorting
- **Status:** Theoretical mechanism plausible (bullet enters bore crooked if case neck misaligned); magnitude unknown
- **Recommendation:** Low priority unless achieving sub-0.5 MOA precision; address after fundamentals mastered

---

## How to Interpret This Information

### When Research Exists: Trust It (But Verify)

If published research exists, you now know how to check if the sample sizes are big enough. Ask these questions:
- Did they control other variables (only change one thing at a time)?
- Are they making absolute claims ("this ALWAYS works") without qualification?
- What was their testing methodology (how did they measure)?
- Has the material been peer-reviewed (checked by other experts) and successfully replicated (repeated by others)?

Remember: A single well-controlled study can disprove a theory, but many replicated studies are needed to support a theory. Even "disproof" requires replication to rule out measurement error or confounding variables.

### When Only Simulations Exist: Understand the Limitations

Simulations prove what the math predicts. They're excellent for understanding sampling behavior (how groups of shots behave). But they can't validate claims about real-world physical effects (barrel vibrations, harmonic nodes, etc.).

### When Research Gaps Exist: Test for Yourself

The absence of research doesn't mean something doesn't work. It means you need to prove it to yourself with proper sample sizes (30+ shots per test). Don't blindly accept OR reject claims—test systematically.

### Sample Size Guidelines by Purpose

| Testing Purpose | Minimum Sample | Recommended | Notes |
|----------------|---------------|-------------|-------|
| Pressure/safety screening | 5-10 rounds | 10 rounds | Watch for pressure signs only |
| Preliminary load comparison | 20-25 rounds | 30 rounds | Screening test before commitment |
| Velocity SD/ES estimation | 30 rounds | 50+ rounds | ±20% accuracy with 95% confidence |
| Load validation (single condition) | 30 rounds | 50+ rounds | For confident performance claims |
| Comparing two loads | 30 per load | 50+ per load | Detect meaningful differences |
| Publication-grade research | 100+ per condition | 200+ per condition | Journal-quality evidence |

**Effect Size Consideration:** Detecting small differences (e.g., 0.1 MOA) requires larger samples than detecting large differences (e.g., 0.5 MOA). The above assumes moderate effect sizes.

### Sample Sizes Depend on Effect Size

The sample size recommendations in this appendix assume **moderate effect sizes** (differences large enough to matter practically). Key points:

- **Large effects** (e.g., switching from cheap to match-grade bullets): Detectable with smaller samples (~20 per condition)
- **Moderate effects** (e.g., primer swaps, seating depth): Require 30+ per condition
- **Small effects** (e.g., 0.1 MOA improvement from brass sorting): May require 50-100+ per condition to detect reliably

This is why so much reloading testing fails—shooters use 5-10 shots to detect small effects that would require 100+ shots to measure reliably.

> ### 📊 The Gold Standard: Published, Peer-Reviewed, Replicated
>
> The best evidence comes from:
> 1. **Published research** with transparent methodology (they explain exactly what they did so you can repeat it)
> 2. **Adequate sample sizes** (30+ per condition minimum, 100+ for journal quality)
> 3. **Replication** by independent researchers (other people repeated the test and got the same results)
> 4. **Controlled variables** (only changed one thing at a time) and proper blinding (the shooter didn't know which ammo they were testing to avoid bias)
>
> Most reloading topics haven't received this level of scrutiny. That's not ideal, but it's reality.

---

## Our Commitment

This curriculum clearly distinguishes between:
- **Established fact** (research validated, mathematically proven)
- **Strong simulation evidence** (statistically demonstrated, theoretically sound)
- **Theoretical but unvalidated** (plausible mechanism, awaiting proper testing)
- **Unknown** (insufficient evidence either way)

When we make strong claims, we tell you the evidence level. When we're uncertain, we say so. When research gaps exist, we acknowledge them.

Your job as a data-driven reloader: **Test properly. Replicate your findings. Trust your data.**

---

## How to Report New Research

If you encounter published research (peer-reviewed papers, controlled studies with proper sample sizes, replicated findings) relevant to topics in this appendix:

**Report it to:** [GitHub Issues](https://github.com/ReevesJustin/data-driven-reloading/issues)

**Include:**
- Full citation (author, title, publication, year)
- Link to paper/study if publicly accessible
- Which section of Appendix B it relates to
- Brief summary of findings and sample sizes
- Why it's relevant

**We commit to:**
- Reviewing submitted research within 30 days
- Updating appendix if research meets evidence standards
- Crediting contributors who identify important sources

**Evidence standards:**
- Sample sizes adequate for claims (generally 30+ per condition)
- Controlled variables (one thing at a time)
- Transparent methodology (replicable)
- Peer review or independent validation preferred

This appendix is a living document—help us keep it current and complete.

---

**Last Updated:** January 2025

---

---

[← Previous: Appendix A - Glossary](Appendix_A_Glossary.html) | [Next: Appendix C - Composite Groups →](Appendix_C_Composite_Groups.html)

[Return to Main Index](../../README.md)
