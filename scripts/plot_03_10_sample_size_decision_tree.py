#!/usr/bin/env python3
"""
Plot 10: Sample Size Decision Tree (Notebook 03)
Visual flowchart helping readers choose appropriate sample size based on testing goals.

Educational Purpose:
Provides a practical decision-making tool for selecting sample sizes based on
what you're testing and the expected effect size. Helps readers avoid both
under-testing (waste of components) and over-testing (unnecessary expense).
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from pathlib import Path

# Set random seed for reproducibility
np.random.seed(42)

# Create the figure
fig, ax = plt.subplots(figsize=(14, 10))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Define colors
box_color = 'steelblue'
endpoint_color = 'wheat'
arrow_color = 'gray'

# Helper function to create boxes
def create_box(ax, x, y, width, height, text, color, fontsize=11, fontweight='normal'):
    box = FancyBboxPatch((x, y), width, height,
                         boxstyle="round,pad=0.1",
                         edgecolor='black',
                         facecolor=color,
                         alpha=0.7,
                         linewidth=2)
    ax.add_patch(box)
    ax.text(x + width/2, y + height/2, text,
            ha='center', va='center',
            fontsize=fontsize, fontweight=fontweight,
            wrap=True)

# Helper function to create arrows
def create_arrow(ax, x1, y1, x2, y2, label=''):
    arrow = FancyArrowPatch((x1, y1), (x2, y2),
                           arrowstyle='->,head_width=0.4,head_length=0.4',
                           color=arrow_color,
                           linewidth=2,
                           alpha=0.7)
    ax.add_patch(arrow)
    if label:
        mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
        ax.text(mid_x, mid_y, label,
                ha='center', va='bottom',
                fontsize=9, style='italic',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8))

# Title
ax.text(5, 9.5, 'Sample Size Decision Guide',
        ha='center', va='top',
        fontsize=16, fontweight='bold')

# Main question box
create_box(ax, 3.5, 8, 3, 0.8, 'What are you testing?', box_color, fontsize=12, fontweight='bold')

# Branch 1: Testing goals
create_arrow(ax, 5, 8, 2, 7)
create_arrow(ax, 5, 8, 5, 7)
create_arrow(ax, 5, 8, 8, 7)

# Goal boxes
create_box(ax, 0.5, 6.2, 2.5, 0.7, 'Just want average\nvelocity/zero', box_color, fontsize=10)
create_box(ax, 3.75, 6.2, 2.5, 0.7, 'Comparing\ntwo loads', box_color, fontsize=10)
create_box(ax, 7, 6.2, 2.5, 0.7, 'Claiming one\nis better', box_color, fontsize=10)

# Arrows to recommendations
create_arrow(ax, 1.75, 6.2, 1.75, 5.5)
create_arrow(ax, 5, 6.2, 5, 5.5)
create_arrow(ax, 8.25, 6.2, 8.25, 5.5)

# Recommendation boxes (first row)
create_box(ax, 0.5, 4.5, 2.5, 0.9, '10 shots\n($15-20)', endpoint_color, fontsize=11, fontweight='bold')
create_box(ax, 3.75, 4.5, 2.5, 0.9, '30+ shots per load\n($45-60)', endpoint_color, fontsize=11, fontweight='bold')
create_box(ax, 7, 4.5, 2.5, 0.9, '50+ shots per load\n($75-100)', endpoint_color, fontsize=11, fontweight='bold')

# Second decision branch - Effect size
ax.text(5, 3.8, 'How big is the difference you expect to detect?',
        ha='center', va='top',
        fontsize=12, fontweight='bold')

create_box(ax, 3.5, 2.8, 3, 0.7, 'Expected Effect Size', box_color, fontsize=11, fontweight='bold')

# Effect size branches
create_arrow(ax, 5, 2.8, 2.5, 2)
create_arrow(ax, 5, 2.8, 7.5, 2)

# Effect size boxes
create_box(ax, 0.75, 1.2, 3.5, 0.7, 'Large effect\n(20 fps SD difference)', box_color, fontsize=10)
create_box(ax, 5.75, 1.2, 3.5, 0.7, 'Small effect\n(5 fps SD difference)', box_color, fontsize=10)

# Arrows to final recommendations
create_arrow(ax, 2.5, 1.2, 2.5, 0.5)
create_arrow(ax, 7.5, 1.2, 7.5, 0.5)

# Final recommendation boxes (effect size)
create_box(ax, 1, 0.1, 3, 0.35, '30 shots might work', endpoint_color, fontsize=10, fontweight='bold')
create_box(ax, 6, 0.1, 3, 0.35, '100+ shots needed', endpoint_color, fontsize=10, fontweight='bold')

# Add publication branch
create_box(ax, 0.5, 6.2 - 2.5, 2.5, 0.7, 'Publishing or\nsharing results', box_color, fontsize=10)
create_arrow(ax, 1.75, 6.2 - 2.5, 1.75, 6.2 - 2.5 - 0.7)
create_box(ax, 0.5, 6.2 - 2.5 - 1.6, 2.5, 0.9, '100+ shots per load\n($150-200)', endpoint_color, fontsize=11, fontweight='bold')

# Reposition for better layout
ax.clear()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(5, 9.5, 'Sample Size Decision Guide',
        ha='center', va='top',
        fontsize=16, fontweight='bold')

# Main question box
create_box(ax, 3.25, 8.1, 3.5, 0.7, 'What are you testing?', box_color, fontsize=12, fontweight='bold')

# Branch arrows (updated to point to new box centers)
create_arrow(ax, 4.2, 8.1, 1.3, 7.3)
create_arrow(ax, 5, 8.1, 3.6, 7.3)
create_arrow(ax, 5.8, 8.1, 5.8, 7.3)
create_arrow(ax, 6.3, 8.1, 8.1, 7.3)

# Goal boxes (reduced width to prevent overlap)
create_box(ax, 0.2, 6.5, 2.2, 0.7, 'Just want average\nvelocity/zero', box_color, fontsize=10)
create_box(ax, 2.6, 6.5, 2.0, 0.7, 'Comparing\ntwo loads', box_color, fontsize=10)
create_box(ax, 4.8, 6.5, 2.0, 0.7, 'Claiming one\nis better', box_color, fontsize=10)
create_box(ax, 7.0, 6.5, 2.2, 0.7, 'Publishing or\nsharing results', box_color, fontsize=10)

# Arrows to recommendations (aligned with box centers)
create_arrow(ax, 1.3, 6.5, 1.3, 5.8)
create_arrow(ax, 3.6, 6.5, 3.6, 5.8)
create_arrow(ax, 5.8, 6.5, 5.8, 5.8)
create_arrow(ax, 8.1, 6.5, 8.1, 5.8)

# Recommendation boxes (first row, aligned with goal boxes above)
create_box(ax, 0.2, 4.9, 2.2, 0.8, '10 shots\n$15-20', endpoint_color, fontsize=11, fontweight='bold')
create_box(ax, 2.6, 4.9, 2.0, 0.8, '30+ shots\nper load\n$45-60', endpoint_color, fontsize=10, fontweight='bold')
create_box(ax, 4.8, 4.9, 2.0, 0.8, '50+ shots\nper load\n$75-100', endpoint_color, fontsize=10, fontweight='bold')
create_box(ax, 7.0, 4.9, 2.2, 0.8, '100+ shots\nper load\n$150-200', endpoint_color, fontsize=11, fontweight='bold')

# Second decision branch - Effect size
ax.text(5, 4.2, 'How big is the difference you expect to detect?',
        ha='center', va='top',
        fontsize=12, fontweight='bold')

create_box(ax, 3.25, 3.3, 3.5, 0.6, 'Expected Effect Size', box_color, fontsize=11, fontweight='bold')

# Effect size branches
create_arrow(ax, 4.5, 3.3, 2.5, 2.7)
create_arrow(ax, 5.5, 3.3, 7.5, 2.7)

# Effect size boxes
create_box(ax, 0.5, 2.0, 4, 0.6, 'Large effect (20+ fps SD difference)', box_color, fontsize=10)
create_box(ax, 5.5, 2.0, 4, 0.6, 'Small effect (5 fps SD difference)', box_color, fontsize=10)

# Arrows to final recommendations
create_arrow(ax, 2.5, 2.0, 2.5, 1.4)
create_arrow(ax, 7.5, 2.0, 7.5, 1.4)

# Final recommendation boxes (effect size)
create_box(ax, 0.75, 0.6, 3.5, 0.7, '30 shots might work\nBut consider 50+', endpoint_color, fontsize=10, fontweight='bold')
create_box(ax, 6.0, 0.6, 3, 0.7, '100+ shots needed\nfor reliable detection', endpoint_color, fontsize=10, fontweight='bold')

# Add note at bottom
note_text = ('Note: Cost estimates assume $1.50/round. More shots = better data, but also more expense.\n'
             'Choose based on your goals and budget. When in doubt, go with more shots.')
ax.text(5, 0.05, note_text,
        ha='center', va='bottom',
        fontsize=9, style='italic',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# Grid (subtle)
ax.grid(True, alpha=0.3, linestyle=':', linewidth=0.5)

# Tight layout
plt.tight_layout()

# Save the figure
output_path = Path(__file__).parent.parent / 'lessons' / 'static' / 'nb03_plot10_sample_size_decision_tree.png'
output_path.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Saved: {output_path}")

# Also display if running interactively
# plt.show()
