# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 17:41:07 2026

@author: cfoggia
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches

# --- Flag Dimensions (Official Proportions) ---
hoist = 1.0        # Height of the flag
fly = 1.9          # Width of the flag
stripe_h = hoist / 13  # Height of an individual stripe

# --- Initialize Plot ---
fig, ax = plt.subplots(figsize=(12, 7))
ax.set_xlim(0, fly)
ax.set_ylim(0, hoist)
ax.set_aspect('equal')
plt.axis('off')    # Hide grid lines and axes

# --- 1. Draw the 13 Stripes ---
# This loop builds the 13 stripes from the bottom (y=0) to the top (y=1)
for i in range(13): 
    # i=0 is the bottom stripe (Red), i=1 is White, alternating up to i=12 (Red)
    color = '#B22234' if i % 2 == 0 else '#FFFFFF'
    y_pos = i * stripe_h
    stripe = patches.Rectangle((0, y_pos), fly, stripe_h, linewidth=0, facecolor=color, zorder=2)
    ax.add_patch(stripe)

# --- 2. Draw the Union (Blue Canton) ---
union_h = 7 * stripe_h
union_w = 0.76
union = patches.Rectangle((0, hoist - union_h), union_w, union_h, linewidth=0, facecolor='#3C3B6E', zorder=3)
ax.add_patch(union)

# --- 3. Render the 50 Stars ---
for row in range(9):
    y_star = (hoist - union_h) + (union_h / 10) * (row + 1)
    if row % 2 == 0:
        cols = 6
        x_start = union_w / 12
    else:
        cols = 5
        x_start = union_w / 6

    for col in range(cols):
        x_star = x_start + (union_w / 6) * col
        ax.plot(x_star, y_star, marker='*', color='#FFFFFF', markersize=9, markeredgewidth=0, zorder=4)

# --- 4. Add the 250 Years Commemoration Text ---
# Placed neatly on the lower right side so it doesn't obscure the whole flag
ax.text(fly * 0.65, hoist * 0.25, "250 YEARS OF INDEPENDENCE",
        color='#3C3B6E', fontsize=42, fontweight='bold',
        ha='center', va='center', wrap=True, zorder=5,
        bbox=dict(facecolor='#FFFFFF', edgecolor='#3C3B6E', boxstyle='round,pad=0.4', lw=2))

# Show the final graphic
plt.tight_layout()
plt.show()
