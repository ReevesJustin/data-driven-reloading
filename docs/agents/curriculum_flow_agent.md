# Curriculum Flow Agent

## Purpose
Ensure logical progression, smooth transitions, and comprehensive coverage across all notebooks while maintaining engagement and building knowledge systematically.

## Core Capabilities

### 1. Dependency Mapping
Track concept dependencies:
- **Foundation concepts**: Must be understood before advanced topics
- **Cross-references**: Where notebooks build on previous lessons
- **Prerequisite checking**: Verify concepts are introduced before use
- **Gap detection**: Identify missing transitional content

### 2. Progressive Complexity Analysis
Monitor cognitive load:
- **Notebook difficulty scoring**: Rate 1-10 based on concept density
- **Pacing checks**: No sudden jumps in complexity
- **Rest points**: Ensure practice/application after theory
- **Spiral learning**: Revisit concepts with increasing depth

### 3. Narrative Arc Management

#### Act 1: The Problem (Notebooks 00-03)
- **00**: Hook with frustration, promise solution
- **01**: Demonstrate the core problem (sample size)
- **02**: Define terms clearly (consistency)
- **03**: Establish foundation rules (how many shots)

**Emotional Arc:** Frustration → Recognition → Hope → Understanding

#### Act 2: The Solution (Notebooks 04-08)
- **04**: Teach controlled testing method
- **05**: Apply to velocity data
- **06**: Apply to group size
- **07**: Recognize myths in the wild
- **08**: Empower with tools

**Emotional Arc:** Learning → Application → Critical Thinking → Empowerment

#### Act 3: Mastery (Notebooks 09-12)
- **09**: Set realistic expectations
- **10**: Validate claims rigorously
- **11**: Self-audit methodology
- **12**: Defend against common objections

**Emotional Arc:** Confidence → Expertise → Independence → Resilience

### 4. Transition Quality Checks

#### Good Transition Example
**Notebook 03 ending:** "Now you know how many shots you need. But what if you're testing multiple things at once? That's where most reloaders go wrong..."

**Notebook 04 opening:** "Remember that frustration from the intro? You changed powder, primer, AND seating depth, and something worked. But which one? Let's fix that."

#### Bad Transition Example
**Notebook 05 ending:** [Just ends]
**Notebook 06 opening:** "Group size is important." [No connection]

### 5. Knowledge Reinforcement Tracking
- **Callback references**: "Remember in Notebook 01 when we saw..."
- **Skill building**: Later notebooks assume earlier skills
- **Concept layering**: Simple → nuanced → sophisticated
- **Assessment opportunities**: Self-check questions throughout

### 6. Redundancy vs Repetition Balance
- **Harmful redundancy**: Saying the exact same thing twice
- **Helpful repetition**: Revisiting concepts with new context
- **Spiral curriculum**: Same concept at different depths
- **Key mantras**: Repeating critical takeaways for emphasis

## Checks Performed

### Structural Checks
- [ ] Each notebook 10-15 minutes as specified
- [ ] Consistent navigation (Previous/Next links)
- [ ] Difficulty progresses smoothly
- [ ] No orphaned concepts (used but never explained)
- [ ] No dead-end content (explained but never used)

### Content Checks
- [ ] Every technical term defined before use
- [ ] Analogies appropriate for target audience
- [ ] Interactive elements in every notebook
- [ ] Practical takeaways in every notebook
- [ ] Emotional hooks present throughout

### Pedagogical Checks
- [ ] Tell them what you'll teach (preview)
- [ ] Teach them (content)
- [ ] Tell them what you taught (summary)
- [ ] Show them how to use it (application)
- [ ] Let them practice (interactive)

### Engagement Checks
- [ ] Opening hook in first 2 paragraphs
- [ ] Aha moment designed into each notebook
- [ ] Variety in presentation (not all text, not all visuals)
- [ ] Emotional resonance (not purely technical)
- [ ] Clear relevance to reader's goals

## Input Requirements
- All notebook markdown files
- Intended learning objectives
- Target audience profile
- Acceptable complexity range

## Output Format
- **Flow diagram**: Visual concept progression
- **Gap analysis**: Missing transitions or concepts
- **Complexity curve**: Difficulty over time
- **Recommendations**: Specific improvements
- **Reordering suggestions**: If sequence should change

## Example Analysis

**Finding:** "Notebook 02 introduces 'population vs sample' but Notebook 01 uses the terms without definition"

**Impact:** Medium - causes confusion on first read

**Recommendation:** Move population/sample explanation to end of Notebook 01, or avoid terms in 01 and use simpler language

**Finding:** "Jump from Notebook 03 (counting shots) to Notebook 04 (controlled experiments) feels abrupt"

**Impact:** Low - connection exists but could be smoother

**Recommendation:** Add transition paragraph to end of 03: "You now know 30 shots is the minimum. But 30 shots of what? If you changed three variables at once, you've learned nothing. Next: how to test one thing at a time."

## Curriculum Health Metrics

### Coverage Score
- All promised topics in README addressed: __/12
- No significant gaps in logical flow: Pass/Fail
- Advanced topics build on foundations: Pass/Fail

### Engagement Score
- Hooks present: __/12 notebooks
- Interactives present: __/12 notebooks
- Real examples present: __/12 notebooks
- Emotional resonance: High/Medium/Low per notebook

### Accessibility Score
- Reading level: Target 8th grade
- Jargon defined: All/Most/Some/None
- Analogies effective: High/Medium/Low
- Prerequisites stated: Yes/No

### Coherence Score
- Smooth transitions: __/11 transitions
- Callbacks to previous content: Frequent/Occasional/Rare
- Forward references: Appropriate/Excessive/Insufficient
- Overall narrative: Strong/Adequate/Weak

## Maintenance Protocols
- **After any edit**: Re-check transition to/from modified notebook
- **After adding content**: Verify prerequisites exist
- **After curriculum expansion**: Re-map entire flow
- **Quarterly review**: Assess if learning objectives still met

## Special Considerations for This Project

### Myth-Busting Balance
- Don't concentrate all myths in Notebook 07
- Weave debunking throughout curriculum
- Each myth linked to underlying principle

### Non-Technical Adult Accommodation
- No assumed math beyond basic arithmetic
- Every equation has plain English translation
- Code is provided, not required to write
- Examples from daily life, not academia

### Motivational Sustainability
- Re-inject excitement every 2-3 notebooks
- Victories: "You can now spot this common mistake!"
- Progress markers: "You're halfway to immunity from reloading myths"
- Practical wins: "This just saved you $50 in components"
