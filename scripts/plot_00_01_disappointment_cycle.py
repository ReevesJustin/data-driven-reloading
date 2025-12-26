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

# Create the figure
fig, ax = plt.subplots(figsize=(14, 12))

# Define the cycle stages and their positions
# Circular arrangement with emotional colors
stages = [
    ('EXCITEMENT', 'Find amazing group!\n0.5 MOA, 8 fps SD!', 'lightgreen', (0, 3)),
    ('CONFIDENCE', 'Post online, declare success\nOrder components', 'lime', (2.5, 2.5)),
    ('CONFUSION', 'Next session: 1.2 MOA, 16 fps SD\n"What changed?"', 'yellow', (3.5, 0)),
    ('DOUBT', '"Weather? Technique?\nComponents? Scope?"', 'orange', (2.5, -2.5)),
    ('FRUSTRATION', 'Try again, different results\nNothing makes sense!', 'darkorange', (0, -3)),
    ('CHASE', 'Change something else\nHoping to recover magic', 'orangered', (-2.5, -2.5)),
    ('BURNOUT', 'Wasted components, time,\nmoney, confidence', 'red', (-3.5, 0)),
    ('CYCLE REPEATS', 'New lucky group appears\n→ Back to excitement!', 'lightcoral', (-2.5, 2.5)),
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

    # Add text
    ax.text(x, y + 0.3, title, fontsize=12, fontweight='bold',
            ha='center', va='center', zorder=11)
    ax.text(x, y - 0.2, text, fontsize=9,
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

# Add central message
central_text = (
    'THE SMALL-SAMPLE TRAP\n'
    '\n'
    'Keeps You Spinning\n'
    '\n'
    'Break Free With\n'
    'Proper Sample Sizes'
)

ax.text(0, 0, central_text, fontsize=14, fontweight='bold',
        ha='center', va='center',
        bbox=dict(boxstyle='round,pad=0.8', facecolor='wheat',
                 edgecolor='black', linewidth=3, alpha=0.9),
        zorder=15)

# Add emotional gradient labels around the circle
ax.text(-5.5, 2, 'HIGH EMOTION', fontsize=11, fontweight='bold',
        color='green', rotation=90, va='center')
ax.text(-5.5, -2, 'HIGH EMOTION', fontsize=11, fontweight='bold',
        color='red', rotation=90, va='center')

# Add timeline/experience labels
ax.text(0, 5, 'Session 1: Lucky!', fontsize=10, fontweight='bold',
        ha='center', style='italic', color='darkgreen')
ax.text(3, 3.5, 'Day 2-3: Reality hits', fontsize=10, fontweight='bold',
        ha='center', style='italic', color='orange')
ax.text(0, -4.5, 'Weeks later: Still confused', fontsize=10, fontweight='bold',
        ha='center', style='italic', color='darkred')
ax.text(-3, 3.5, 'Eventually: New lucky result', fontsize=10, fontweight='bold',
        ha='center', style='italic', color='purple')

# Set axis limits and properties
ax.set_xlim([-6, 6])
ax.set_ylim([-6, 6])
ax.set_aspect('equal')
ax.axis('off')

# Add title
ax.text(0, 5.7, 'The Disappointment Cycle: Emotional Journey of Chasing False Leads',
        fontsize=16, fontweight='bold', ha='center', va='bottom')

# Add subtitle
ax.text(0, -5.7, 'Small samples create lucky results that disappear, leading to endless frustration.\n'
                 'The cycle repeats because random variation keeps producing new "discoveries".\n'
                 'ESCAPE: Use 30+ shot samples to see reality instead of random noise.',
        fontsize=11, ha='center', va='top', style='italic',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='lightyellow', alpha=0.8))

# Add statistics box showing the math behind the cycle
stats_box_text = (
    'Why the cycle repeats:\n'
    '\n'
    'With small samples (3-5 shots):\n'
    '• ~10% of groups look "amazing"\n'
    '• ~10% look "terrible"\n'
    '• ~80% look "average"\n'
    '\n'
    'We remember & chase the 10%\n'
    'amazing results, but they\'re\n'
    'just random luck!\n'
    '\n'
    'With large samples (30+ shots):\n'
    '• True performance revealed\n'
    '• No more lucky flukes\n'
    '• Cycle broken'
)

ax.text(0.98, 0.98, stats_box_text, transform=ax.transAxes,
        fontsize=9, verticalalignment='top', horizontalalignment='right',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5),
        family='monospace')

# Add cost counter
cost_text = (
    'TYPICAL COSTS OF ONE CYCLE:\n'
    '• Components tried: $50-200\n'
    '• Time wasted: 10-20 hours\n'
    '• Confidence lost: Priceless\n'
    '• Lessons learned: None\n'
    '  (until you understand statistics)'
)

ax.text(0.02, 0.98, cost_text, transform=ax.transAxes,
        fontsize=9, verticalalignment='top', horizontalalignment='left',
        bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.6),
        fontweight='bold')

# Tight layout
plt.tight_layout()

# Save the figure
output_path = Path(__file__).parent.parent / 'notebooks' / 'static' / 'nb00_plot01_disappointment_cycle.png'
output_path.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Saved: {output_path}")

# Also display if running interactively
# plt.show()
