# Reloading Analysis Templates - Excel Edition

Professional Excel spreadsheet templates for ammunition testing and load development, matching the functionality of the Python templates from Lesson 08.

## Files in this Directory

### Excel Templates (Ready to Use)

**`Reloading_Analysis_Templates.xlsx`**
- Blank templates ready for your data
- Use this as your starting point for new tests
- Recommended: Make a copy for each new test (keep this as your master)

**`Reloading_Analysis_Templates_Examples.xlsx`**
- Same templates pre-filled with example data from Lesson 08
- Use this to see how the templates work before using your own data
- See the formulas and interpretations in action

### Generator Script (For Advanced Users)

**`generate_excel_templates.py`**
- Python script that created the Excel templates
- Requires: Python 3.x with openpyxl (`pip install openpyxl`)
- Run: `python3 generate_excel_templates.py`
- Useful if you need to regenerate templates or customize them

**`requirements.txt`**
- Python dependencies for the generator script
- Install with: `pip install -r requirements.txt`

## What These Templates Do

Each workbook contains **three professional analysis templates**:

### Template A: Two-Load Comparison
**Purpose:** Compare velocity performance between any two loads

**Use Cases:**
- Primer comparison (CCI vs Federal)
- Powder comparison (H4350 vs Varget)
- Bullet comparison (Sierra vs Berger)
- Any head-to-head load test

**Data Required:** 30 shots per load (60 total recommended)

**Features:**
- Automatic statistical calculations (mean, SD, ES, 95% CI)
- T-test and Cohen's d (effect size)
- Plain-English interpretation
- Clear decision guidance (3 verdict levels)
- Protected formulas (can't break them accidentally)

### Template B: Charge Weight Ladder
**Purpose:** Test multiple powder charges systematically

**Use Cases:**
- Finding optimal charge weight
- Initial screening of 3-6 charges
- Velocity progression analysis

**Data Required:** 10-30 shots per charge, 3-6 different charges

**Features:**
- Per-charge statistics table
- Best charge identification (lowest SD)
- Sample size warnings
- ⚠ **WARNING:** Use for screening only! Validate winners with 30+ shots.

### Template C: Before/After Modification
**Purpose:** Evaluate the impact of a single component change

**Use Cases:**
- Barrel cleaning effects
- Adding/removing tuners
- Brass lot changes
- Any single-variable modification

**Data Required:** 20-30 shots before, 20-30 shots after

**Features:**
- Change metrics (Δ mean, Δ SD)
- Statistical significance testing
- Practical vs statistical significance
- Clear verdict (2 decision levels)

## How to Use These Templates

### Quick Start (3 Steps)

**STEP 1: Choose Your Template**
- Open the blank version (`Reloading_Analysis_Templates.xlsx`)
- Or start with examples (`Reloading_Analysis_Templates_Examples.xlsx`) to see how it works
- Navigate to the template sheet you need (Template_A, Template_B, or Template_C)

**STEP 2: Enter Your Data**
- Find the data entry area (colored columns A-C)
- Paste or type your chronograph readings
- Use the dropdown menus for Load/Condition/Charge columns
- Do NOT modify formula cells (they're protected)

**STEP 3: Review Results**
- Statistics calculate automatically
- Read the interpretation section (plain English)
- Follow the recommendation guidance
- Save your completed analysis with a descriptive name

### Data Format Examples

**Template A (Two-Load Comparison):**
```
Shot | Load    | Velocity
1    | Load_A  | 2850
2    | Load_A  | 2855
...
31   | Load_B  | 2863
32   | Load_B  | 2858
```

**Template B (Charge Ladder):**
```
Shot | Charge | Velocity
1    | 41.0   | 2720
2    | 41.0   | 2725
...
11   | 41.5   | 2750
```

**Template C (Before/After):**
```
Shot | Condition | Velocity
1    | Before    | 2850
2    | Before    | 2855
...
31   | After     | 2848
```

## Best Practices

### Before You Start
✓ Read the README sheet in the Excel workbook
✓ Review the example data version first
✓ Plan your sample sizes (30+ shots per load for valid SD comparison)
✓ Document test conditions (date, temp, barrel fouling, lot numbers)

### While Testing
✓ Include ALL shots (even flyers) - no cherry-picking
✓ Use equal sample sizes when comparing loads
✓ Test on the same day when possible
✓ Alternate between conditions to minimize barrel heating effects

### After Testing
✓ Save completed templates with descriptive names
  - Example: `2024-03-15_CCI_vs_Federal_Primers.xlsx`
✓ Review all sections: statistics, interpretation, and recommendation
✓ Document any anomalies or unusual conditions
✓ Keep a testing logbook

## Understanding the Statistics

**Mean**: Average velocity - the center of your data
**SD (Standard Deviation)**: How spread out velocities are (lower = more consistent)
**ES (Extreme Spread)**: Max velocity minus min velocity
**95% CI**: We're 95% confident the true mean is within this range
**P-value**: Probability the difference is random (< 0.05 means real difference)
**Cohen's d**: Effect size
  - < 0.2 = tiny
  - 0.2-0.5 = small
  - 0.5-0.8 = medium
  - \> 0.8 = large

## Troubleshooting

**#DIV/0! error**
- Not enough data entered
- Enter at least 10 data points per load/condition

**#VALUE! error**
- Non-numeric data in Velocity column
- Check for text entries, remove any non-numbers

**Charts not present**
- openpyxl has limited chart support
- Chart placeholders are noted in the templates
- Create charts manually for best results (see Lesson 08 for chart specifications)

**Dropdowns not working**
- Make sure data validation is enabled
- Check that you're entering data in the correct cells

**Need to modify formulas**
- Sheets are protected with password: `reloading`
- Click Review → Unprotect Sheet → Enter: reloading
- Be careful not to break the formulas!

## Requirements

**Software:**
- Microsoft Excel 2016 or newer (Windows/Mac)
- Or: Excel Online / Microsoft 365
- Or: Google Sheets (with some limitations - see notes below)

**Google Sheets Compatibility:**
The templates work in Google Sheets with these notes:
- Array formulas may show differently
- Some conditional formatting may not transfer perfectly
- Data validation dropdowns work
- All core calculations function correctly
- Consider saving as Google Sheets format after opening

## Additional Resources

**Data-Driven Reloading Curriculum:**
- See Lesson 08 for complete documentation of these templates
- Lessons 01-07 explain the statistical concepts used
- Lessons 09-12 help you interpret and apply results

**Python Templates:**
- Original Python/Jupyter notebook templates in Lesson 08
- More powerful but require Python knowledge
- These Excel templates provide equivalent functionality

## Password

**Sheet Protection Password:** `reloading`

Use this to unprotect sheets if you need to modify formulas. Be careful - protected formulas prevent accidental errors.

## Support

For questions, issues, or feedback:
1. Review the README sheet in the Excel workbook
2. Check Lesson 08 of the Data-Driven Reloading curriculum
3. Ensure you're using the correct data format
4. Try the example data version to verify templates work on your system

## License & Credits

These templates are part of the Data-Driven Reloading educational curriculum.

**Philosophy:** Copy, paste data, get answers - no programming required.

The goal is to make professional statistical analysis accessible to all reloaders, regardless of technical background.
