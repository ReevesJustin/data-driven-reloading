#!/usr/bin/env python3
"""
Primer Test Analysis Script
Data-Driven Reloading - Lesson 04

This script analyzes data from a controlled primer comparison test.
Usage: python primer_test_analysis.py

Requirements:
- pandas
- matplotlib
- numpy

Install with: pip install pandas matplotlib numpy
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load your data
data = pd.read_csv('primer_test.csv')

# Split by primer type
cci_data = data[data['Primer'] == 'CCI BR2']
fed_data = data[data['Primer'] == 'Federal 210M']

# Calculate statistics
print("=== CCI BR2 Results ===")
print(f"Average velocity: {cci_data['Velocity_FPS'].mean():.1f} fps")
print(f"SD: {cci_data['Velocity_FPS'].std():.1f} fps")
print(f"Extreme spread: {cci_data['Velocity_FPS'].max() - cci_data['Velocity_FPS'].min():.1f} fps")

print("\n=== Federal 210M Results ===")
print(f"Average velocity: {fed_data['Velocity_FPS'].mean():.1f} fps")
print(f"SD: {fed_data['Velocity_FPS'].std():.1f} fps")
print(f"Extreme spread: {fed_data['Velocity_FPS'].max() - fed_data['Velocity_FPS'].min():.1f} fps")

# Visual comparison
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Velocity distributions
axes[0].hist(cci_data['Velocity_FPS'], bins=15, alpha=0.6, label='CCI BR2', color='blue')
axes[0].hist(fed_data['Velocity_FPS'], bins=15, alpha=0.6, label='Federal 210M', color='red')
axes[0].set_xlabel('Velocity (fps)')
axes[0].set_ylabel('Count')
axes[0].set_title('Velocity Distributions')
axes[0].legend()
axes[0].grid(alpha=0.3)

# Velocity over shot sequence
axes[1].scatter(cci_data['Shot'], cci_data['Velocity_FPS'], label='CCI BR2', alpha=0.7, color='blue')
axes[1].scatter(fed_data['Shot'], fed_data['Velocity_FPS'], label='Federal 210M', alpha=0.7, color='red')
axes[1].axhline(cci_data['Velocity_FPS'].mean(), color='blue', linestyle='--', alpha=0.5)
axes[1].axhline(fed_data['Velocity_FPS'].mean(), color='red', linestyle='--', alpha=0.5)
axes[1].set_xlabel('Shot Number')
axes[1].set_ylabel('Velocity (fps)')
axes[1].set_title('Velocity Over Time')
axes[1].legend()
axes[1].grid(alpha=0.3)

plt.tight_layout()
plt.show()
