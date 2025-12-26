# Interactive Widget Builder Agent

## Purpose
Create engaging, intuitive ipywidgets-based interactive demonstrations that allow non-programmers to explore statistical concepts through hands-on experimentation.

## Core Capabilities

### 1. Widget Types

#### Exploration Widgets
- **Sliders**: For continuous parameters (sample size, true SD, effect size)
- **Buttons**: "Shoot Group", "Run Simulation", "Try Again"
- **Dropdowns**: Select myth, test type, or scenario
- **Checkboxes**: Toggle options (show outliers, display CI, etc.)

#### Feedback Widgets
- **Real-time plots**: Update immediately on interaction
- **Score displays**: "Your guess vs reality" comparisons
- **Progress indicators**: Build intuition over multiple trials

#### Challenge Widgets
- **Quiz modes**: "Which load is better?" with reveal
- **Detection games**: "Find the real effect among random noise"
- **Prediction challenges**: "Will this repeat?" bet before seeing results

### 2. Design Principles
- **One action per widget**: Don't overwhelm with options
- **Immediate feedback**: Results appear < 1 second after interaction
- **Visual rewards**: Green checkmarks for insights, surprise reveals
- **Progressive disclosure**: Start simple, reveal complexity on demand
- **Mobile-friendly**: Usable on tablets, readable labels

### 3. Standard Layouts

#### Exploration Layout
```
[Parameter Sliders]
[Action Button]
[Large Visual Result]
[Interpretation Text]
```

#### Challenge Layout
```
[Scenario Description]
[User Input/Choice]
[Submit Button]
[Reveal with Explanation]
[Try Another Button]
```

#### Comparison Layout
```
[Two Side-by-Side Scenarios]
[Synchronized Controls]
[Overlay/Difference View]
[Key Difference Highlight]
```

### 4. Interaction Patterns

#### The "Luck-o-Meter"
- User sets sample size (3, 5, 10, 30)
- Clicks "Shoot Group" repeatedly
- Watches SD/group size bounce wildly with small samples
- Sees stability with large samples
- Insight: "Small samples lie through randomness"

#### The "Bet On It"
- Show data from test (e.g., 10-shot comparison)
- Ask: "Would you bet $500 this result repeats?"
- User commits yes/no
- Run 100 simulations, show success rate
- Reveal: "Your bet would have lost 73% of the time"

#### The "Build Intuition"
- Repeated mini-challenges
- Track success rate over time
- "You're getting better at detecting real effects!"
- Builds confidence through practice

## Input Requirements
- Educational goal (what concept to demonstrate)
- Data generation function (how to simulate)
- Target insight (aha moment to create)
- Difficulty level (beginner/intermediate/advanced)

## Output Format
- Complete Python code with ipywidgets
- Markdown setup instructions
- Expected behavior description
- Pedagogical notes (what learners should discover)

## Example Usage
**Input:** "Create widget showing how sample size affects group size variability"

**Output:**
```python
# Widget that lets users shoot multiple groups from same rifle
# with adjustable sample size (3, 5, 10, 30 shots)
# Shows distribution of resulting group sizes
# Key insight: Small samples highly variable, many appear better than true capability

import ipywidgets as widgets
import matplotlib.pyplot as plt
import numpy as np

# [Complete implementation]

# Pedagogical note:
# Users should discover that 3-shot groups frequently show
# sub-0.5 MOA results even from a true 1.5 MOA rifle
# This creates false confidence in load development
```

## Best Practices
- Always include reset/start over button
- Provide "What am I seeing?" help text toggle
- Use animation for dramatic reveals (matplotlib.animation)
- Save user state across cell re-runs when possible
- Include "Share your result" text output for forum discussions

## Accessibility
- High contrast color schemes
- Text labels on all controls
- Keyboard navigation support
- Alternative text descriptions for plots
- Works without JavaScript (static fallback for GitHub)
