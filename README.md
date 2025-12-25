Stop chasing ghosts. Learn to test handloads the way that actually reveals truth—even if you hated math in school.

**Start Here: [00_Welcome_and_Why_This_Matters.ipynb](notebooks/00_Welcome_and_Why_This_Matters.ipynb)** - Hook emotionally, validate frustration.

Notebook Sequence (Designed for Non-Technical Adults)

00_Welcome_and_Why_This_Matters.ipynb
Goal: Hook the learner emotionally, validate frustration.
Content:
"You've probably seen it: One guy shoots three 5-shot groups and declares a charge weight 'perfect.' Another gets 8 fps SD over 10 shots and calls it 'the node.' A third adds a tuner and his groups shrink—proof, right?"
Show screenshots (anonymized) of common forum claims.
Explain: Most of this is just random luck in tiny samples. You can do better without a stats degree.
Adult hook: "This course saves you time, money, components, and disappointment by teaching you to separate signal from noise."


01_The_Biggest_Lie_in_Reloading_Testing.ipynb
Goal: Visually prove small samples mislead.
Content:
Simple simulation: Same exact load (fixed true SD = 12 fps). Generate 1,000 shots.
Then repeatedly pull random 5-, 10-, or 20-shot strings. Plot their SDs.
Interactive slider: Change sample size → watch how often you get "magical" single-digit SD by pure chance.
Key takeaway (big bold text): "A low SD over 10 shots proves almost nothing. It happens by luck more often than you think."
Repeat for group sizes: Show how 3×5-shot groups can look amazing even from a mediocre rifle.


02_What_We_Actually_Mean_by_Consistency.ipynb
Goal: Define clear, honest terms without jargon.
Content:
Velocity consistency ≠ one lucky low SD.
Accuracy ≠ one tight group.
Explain in plain English: "Consistency is how predictable your results are over many, many rounds—not just the best ones you happened to shoot."
Introduce the idea of a "population" (all possible rounds you could ever load) vs. "sample" (the few you test).


03_How_Many_Shots_Do_You_Really_Need.ipynb
Goal: Give practical rules of thumb.
Content:
Show simulations: To tell if one powder truly has lower velocity spread than another (say, 10 fps vs. 15 fps true difference), how many shots per powder?
Slider/interactive: Desired confidence → required shots.
Practical guidelines:
– Quick screening: 20–30 shots (better than 10, but still rough).
– Serious comparison: 50–100 shots per variable.
– Proving a big claim (e.g., "this primer cuts SD in half"): 200+ shots.
Acknowledge reality: "Yes, it's a lot of ammo. But it's less than you'll waste chasing false leads."


04_Testing_One_Thing_at_a_Time.ipynb
Goal: Teach simple, controlled experiments.
Content:
Common mistake: Changing powder, charge, seating depth, and primer all at once.
Rule: Change one variable at a time, shoot enough rounds, then interpret carefully.
Example walkthrough: Testing two primers. Show proper setup, data collection template (CSV), basic plots.


05_Velocity_Data_-_What_to_Measure_and_How_to_Think_About_It.ipynb
Goal: Demystify chronograph numbers.
Content:
Average velocity matters (for trajectory).
Standard deviation from small samples is misleading (revisit Bramwell's "perverse nature" in plain language).
Better: Plot all velocities in order, look for trends; calculate extreme spread over large n; use running SD.
Debunk "flat spots" in velocity: Show how random variation creates fake "nodes" in small charge ladders.


06_Group_Size_and_Accuracy_-_Beyond_the_Best_Group.ipynb
Goal: Teach honest on-target evaluation.
Content:
Why extreme spread grows forever.
Simple alternative: Mean radius (average distance from center).
Practical method: Shoot 25–50 rounds at once on one big target (or aggregate multiple), measure mean radius.
Interactive: Overlay many 5-shot groups vs. one 50-shot aggregate from the same rifle.


07_Real_Examples_-_Dissecting_Common_Myths.ipynb
Goal: Apply lessons to popular methods.
Content (neutral, evidence-based, no personal attacks):
OCW: Show how small samples make multiple charge weights look "forgiving."
Velocity nodes/flat spots: Simulate charge ladders—random data creates apparent flats.
Barrel tuners: Simulate dispersion—random tight groups appear with any setting.
Each with interactive sims so learners see the illusion themselves.


08_Your_Experiments_Template.ipynb
Goal: Empower the learner.
Blank template with:
Data entry tables.
Auto-plotting code (velocity traces, histograms, group overlays).
Simple statistical checks (confidence intervals in plain English).
Instructions: "Copy this notebook, paste your chronograph CSV, change titles, and see the truth."


09_Reasonable_Expectations_-_What_Real_Precision_Looks_Like.ipynb
Goal: Shift from debunking myths to setting realistic goals and understanding real-world performance.
Content:
Introduction: Address pain of unrealistic expectations from small samples.
Section 1: Three contributors to dispersion (rifle/ammo, shooter, recoil).
Section 2: Benchmarks for precision with large samples; interactive sims.
Section 3: Why large samples matter (pro protocols).
Section 4: WEZ thinking for hit probability; interactive plots.
Conclusion: Focus on achievable goals and progress.



Technical & Presentation Tips for Accessibility

Language level: 8th-grade reading. No Greek letters until necessary (then define immediately).
Visuals everywhere: Big plots, animations (use matplotlib with %matplotlib inline), color.
Interactivity: Use ipywidgets sliders generously—adults learn by playing.
Short/punchy notebooks: 10-15 minutes each, with bold takeaways and analogies.
Progress checklist in README: "Complete notebooks in order → become immune to reloading myths."
No prerequisites: All code explained in markdown cells. Learners don't need to write code—just run it.
Example data CSVs in /data directory for practice.
Bonus notebooks: bootstrapping, cartridge-specific.

## Project Design Specifications

- **Short & Punchy**: 10–15 min per notebook, bold takeaways, reloading analogies (e.g., "Like judging a powder by one throw on a scale").
- **Example Data**: CSVs in /data folder (simulated velocities, real anonymized chronograph exports if available).
- **Bonus Notebooks**: Advanced (bootstrapping confidence intervals), or cartridge-specific examples (.223 gas gun vs. bolt).
- **References**: 
  - Denton Bramwell's "Perverse Nature of Standard Deviation" PDF.
  - Bryan Litz's books (e.g., Applied Ballistics) and podcasts (Hornady Ep. 50).
  - Reloading All Day posts.

## Mobile Viewing Notes

To ensure this repository is mobile-friendly for phones and tablets:

- Notebooks are optimized for GitHub rendering with wide tables for comprehensive data display and large text for readability.
- On mobile devices, wide tables may cause horizontal scrolling; view in landscape mode or on a larger screen for full visibility.
- GitHub's notebook renderer supports responsive elements; however, for the best experience, use a desktop browser or tablet.
- All content has been reviewed for responsiveness, ensuring text and images scale appropriately without distortion.

This structure respects adult learners: it starts with their pain points, shows why common methods fail (through experience, not lecture), builds confidence gradually, and ends with tools they can use immediately.

## References

- Denton Bramwell's "The Perverse Nature of Standard Deviation" [PDF](https://www.google.com/search?q=perverse+nature+of+standard+deviation+bramwell+pdf) (search for available copy).
- Bryan Litz's *Applied Ballistics for Long Range Shooting* (book) and podcasts like [Hornady Manufacturing Ep. 50](https://www.hornady.com/ammunition/ballistics-resource-center/podcast/episode-50-bryan-litz).
- Reloading All Day blog posts on data-driven reloading.
