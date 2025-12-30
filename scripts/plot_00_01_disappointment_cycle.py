#!/usr/bin/env python3
"""
Plot 1: The Disappointment Cycle (Notebook 00)
Emotional journey of chasing false leads from small samples.

Educational Purpose:
Shows the repeating cycle of excitement, confidence, confusion, frustration,
and burnout when relying on small samples. Emotionally engaging and relatable
visualization of the "small-sample trap" that wastes time, money, and confidence.
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from matplotlib.patches import Arc

# Set random seed for reproducibility
np.random.seed(42)

# Create the figure - slightly wider for better information layout
fig, ax = plt.subplots(figsize=(16, 10))

# Define the cycle stages and their positions
# Circular arrangement with emotional colors - more compact descriptions
stages = [
    ('EXCITEMENT', 'Amazing group!\n0.5 MOA, 8 fps SD', 'lightgreen', (0, 3)),
    ('CONFIDENCE', 'Post results online\nOrder components', 'lime', (2.5, 2.5)),
    ('CONFUSION', 'Next: 1.2 MOA, 16 fps SD\nWhat changed?', 'yellow', (3.5, 0)),
    ('DOUBT', 'Weather? Technique?\nComponents?', 'orange', (2.5, -2.5)),
    ('FRUSTRATION', 'Try again, still different\nNothing consistent!', 'darkorange', (0, -3)),
    ('CHASE', 'Change components\nSeek magic again', 'orangered', (-2.5, -2.5)),
    ('BURNOUT', 'Waste: time, money,\nconfidence', 'red', (-3.5, 0)),
    ('CYCLE REPEATS', 'New lucky group!\nBack to excitement', 'lightcoral', (-2.5, 2.5)),
]

# Draw the cycle
n_stages = len(stages)
box_width = 2.2
box_height = 1.2

# Draw boxes and arrows
for i, (title, text, color, pos) in enumerate(stages):
    x, y = pos

    # Draw box
    if i == 0:
        # Excitement - special bright border
        box = FancyBboxPatch((x - box_width/2, y - box_height/2), box_width, box_height,
                            boxstyle="round,pad=0.1",
                            edgecolor='darkgreen', facecolor=color,
                            linewidth=4, alpha=0.9, zorder=10)
    elif i == n_stages - 1:
        # Cycle repeats - dashed border
        box = FancyBboxPatch((x - box_width/2, y - box_height/2), box_width, box_height,
                            boxstyle="round,pad=0.1",
                            edgecolor='darkred', facecolor=color,
                            linewidth=3, linestyle='--', alpha=0.8, zorder=10)
    else:
        box = FancyBboxPatch((x - box_width/2, y - box_height/2), box_width, box_height,
                            boxstyle="round,pad=0.1",
                            edgecolor='black', facecolor=color,
                            linewidth=2, alpha=0.8, zorder=10)

    ax.add_patch(box)

    # Add text - slightly smaller fonts for cleaner look
    ax.text(x, y + 0.3, title, fontsize=11, fontweight='bold',
            ha='center', va='center', zorder=11)
    ax.text(x, y - 0.2, text, fontsize=8,
            ha='center', va='center', zorder=11, style='italic')

    # Draw arrow to next stage
    if i < n_stages - 1:
        x_next, y_next = stages[i + 1][3]
    else:
        # Last stage arrow back to first
        x_next, y_next = stages[0][3]

    # Calculate arrow start and end (from box edge to next box edge)
    dx = x_next - x
    dy = y_next - y
    length = np.sqrt(dx**2 + dy**2)

    # Normalize and shorten to box boundaries
    dx_norm = dx / length
    dy_norm = dy / length

    arrow_start_x = x + dx_norm * (box_width/2 + 0.1)
    arrow_start_y = y + dy_norm * (box_height/2 + 0.1)
    arrow_end_x = x_next - dx_norm * (box_width/2 + 0.1)
    arrow_end_y = y_next - dy_norm * (box_height/2 + 0.1)

    # Special styling for last arrow (cycle repeats)
    if i == n_stages - 1:
        arrow = FancyArrowPatch((arrow_start_x, arrow_start_y),
                               (arrow_end_x, arrow_end_y),
                               arrowstyle='->', mutation_scale=30, linewidth=4,
                               color='darkred', linestyle='--', alpha=0.8, zorder=5)
    else:
        arrow = FancyArrowPatch((arrow_start_x, arrow_start_y),
                               (arrow_end_x, arrow_end_y),
                               arrowstyle='->', mutation_scale=25, linewidth=3,
                               color='black', alpha=0.6, zorder=5)

    ax.add_patch(arrow)

# Add central message - more concise
central_text = (
    'THE SMALL-SAMPLE TRAP\n'
    '\n'
    'Keeps You Spinning\n'
    '\n'
    'Break Free With 30+ Shots'
)

ax.text(0, 0, central_text, fontsize=13, fontweight='bold',
        ha='center', va='center',
        bbox=dict(boxstyle='round,pad=0.7', facecolor='wheat',
                 edgecolor='black', linewidth=2.5, alpha=0.9),
        zorder=15)

# Remove crowded emotion and timeline labels - let the cycle speak for itself

# Set axis limits and properties - wider layout for side panels
ax.set_xlim([-9, 9])
ax.set_ylim([-5, 5])
ax.set_aspect('equal')
ax.axis('off')

# Add title - slightly smaller
ax.text(0, 4.5, 'The Disappointment Cycle: Chasing False Leads from Small Samples',
        fontsize=15, fontweight='bold', ha='center', va='bottom')

# Add subtitle - more concise
ax.text(0, -4.5, 'Small samples create lucky results that disappear. Random variation produces new "discoveries".\n'
                 'ESCAPE: Use 30+ shot samples to see reality instead of noise.',
        fontsize=10, ha='center', va='top', style='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='lightyellow', alpha=0.8))

# Combine stats and costs into cleaner side panels
# Left panel: Why it happens
stats_text = (
    'WHY THE CYCLE REPEATS\n'
    '\n'
    'Small samples (3-5 shots):\n'
    '  10% look amazing\n'
    '  10% look terrible\n'
    '  80% look average\n'
    '\n'
    'We chase the "amazing"\n'
    'results - but they\'re just\n'
    'random luck!\n'
    '\n'
    'Large samples (30+ shots):\n'
    '  True performance shown\n'
    '  No lucky flukes\n'
    '  Cycle broken'
)

ax.text(-8, 0, stats_text, fontsize=8.5, verticalalignment='center', horizontalalignment='left',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='wheat', alpha=0.7, edgecolor='black', linewidth=1))

# Right panel: Cost of the cycle
cost_text = (
    'COST PER CYCLE\n'
    '\n'
    'Components: $50-200\n'
    'Time: 10-20 hours\n'
    'Confidence: Priceless\n'
    '\n'
    'Lessons learned: None\n'
    '(until you understand\n'
    'the statistics)'
)

ax.text(8, 0, cost_text, fontsize=8.5, verticalalignment='center', horizontalalignment='right',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='lightcoral', alpha=0.7, edgecolor='black', linewidth=1),
        fontweight='bold')

# Tight layout
plt.tight_layout()

# Save the figure
output_path = Path(__file__).parent.parent / 'lessons' / 'static' / 'nb00_plot01_disappointment_cycle.png'
output_path.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Saved: {output_path}")

# Also display if running interactively
# plt.show()
