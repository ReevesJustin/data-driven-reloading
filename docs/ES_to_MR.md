# Extreme Spread (ES) to Mean Radius (MR) Conversion Scalers

## Statistician Agent Analysis Summary

**Purpose:** Determine "close enough" scaling factors to convert between Extreme Spread (ES) and Mean Radius (MR) measurements for shot groups, based on Monte Carlo simulation of bivariate normal distributions.

**Methodology:**
- Simulated 10,000 five-shot groups + 1,000 groups each for other sizes (3, 10, 20, 30, 50, 100 shots)
- Assumed circular bivariate normal distribution (σ = 1.0 MOA in both axes)
- Calculated ES as maximum distance between any two shots
- Calculated MR as average distance from group centroid
- Computed MR/ES ratios for each simulated group

## Results: MR/ES Ratio by Group Size

| Group Size | MR/ES Ratio | Notes |
|------------|-------------|--------|
| 3 shots | 0.428 | Highly variable; ES strongly influenced by outliers |
| 5 shots | 0.370 | Typical reloading test size; moderate variability |
| 10 shots | 0.315 | Better stability; recommended for velocity testing |
| 20 shots | 0.276 | Good convergence; ES becoming more reliable |
| 30 shots | 0.258 | Curriculum standard; solid statistical foundation |
| 50 shots | 0.241 | High confidence; diminishing returns |
| 100 shots | 0.220 | Near-theoretical limit; minimal additional benefit |

## Key Findings

**Conversion Formulas:**
- **MR ≈ 0.37 × ES** (for 5-shot groups - most practical for quick estimates)
- **MR ≈ 0.26 × ES** (for 30-shot groups - matches curriculum recommendations)
- **MR ≈ 0.22 × ES** (for 100-shot groups - theoretical limit)

**Practical Implications:**
- ES overestimates group dispersion compared to MR, especially with small groups
- The ratio decreases as group size increases because ES is more sensitive to outliers
- For reloading decisions, prefer MR when possible; use these scalers for rough conversions

**Curriculum Application:**
- Use 0.37 scaler for informal discussions of small groups
- Use 0.26 scaler for formal analysis of 30+ shot groups
- Emphasize that these are approximations; calculate MR directly for precision

## Statistical Validation

**Confidence Intervals (for 5-shot groups):**
- Mean ratio: 0.370
- 95% CI: 0.275 - 0.465
- Standard deviation: 0.048

**Assumptions & Limitations:**
- Assumes perfect circular bivariate normal distribution
- Real groups may have elliptical shapes or flyers
- ES calculation is computationally intensive for large groups
- Ratios are population estimates; individual groups vary

**Recommendations:**
1. For curriculum content: Use 0.26 as the standard scaler for 30-shot groups
2. For educational examples: Show how ratio changes with group size
3. For practical advice: "MR is about 1/4 of ES for well-tested groups"

---
*Analysis performed by Statistician Agent on December 26, 2025*</content>
<parameter name="filePath">docs/ES_to_MR.md