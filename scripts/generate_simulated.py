import numpy as np
import pandas as pd
import os

# Ensure directory exists
os.makedirs('data/simulated', exist_ok=True)

# 1. velocity_5fps_sd_1000shots.csv
np.random.seed(42)  # For reproducibility
vel_5 = np.random.normal(2850, 5, 1000)
df_5 = pd.DataFrame({'velocity_fps': vel_5})
df_5.to_csv('data/simulated/velocity_5fps_sd_1000shots.csv', index=False)

# 2. velocity_10fps_sd_1000shots.csv
vel_10 = np.random.normal(2850, 10, 1000)
df_10 = pd.DataFrame({'velocity_fps': vel_10})
df_10.to_csv('data/simulated/velocity_10fps_sd_1000shots.csv', index=False)

# 3. velocity_15fps_sd_1000shots.csv
vel_15 = np.random.normal(2850, 15, 1000)
df_15 = pd.DataFrame({'velocity_fps': vel_15})
df_15.to_csv('data/simulated/velocity_15fps_sd_1000shots.csv', index=False)

# 4. velocity_20fps_sd_1000shots.csv
vel_20 = np.random.normal(2850, 20, 1000)
df_20 = pd.DataFrame({'velocity_fps': vel_20})
df_20.to_csv('data/simulated/velocity_20fps_sd_1000shots.csv', index=False)

# 5. velocity_ladder_test_raw.csv
charges = np.linspace(38.0, 42.0, 13)
sd_values = np.linspace(20, 10, 13)
data = []
for i, charge in enumerate(charges):
    sd = sd_values[i]
    vels = np.random.normal(2850, sd, 5)
    for vel in vels:
        data.append({'charge_gr': charge, 'velocity_fps': vel})
df_ladder = pd.DataFrame(data)
df_ladder.to_csv('data/simulated/velocity_ladder_test_raw.csv', index=False)

# 6. group_size_simulation.csv
# Simulate 100 groups, each 5 shots, positions in inches
# For 1 MOA at 100 yards, group size ~1 inch diameter
# Use SD=0.25 inches for x,y to get ~1 inch group
groups = []
group_id = 0
for _ in range(100):
    x = np.random.normal(0, 0.25, 5)
    y = np.random.normal(0, 0.25, 5)
    for shot in range(5):
        groups.append({'group_id': group_id, 'shot_id': shot, 'x_inches': x[shot], 'y_inches': y[shot]})
    group_id += 1
df_groups = pd.DataFrame(groups)
df_groups.to_csv('data/simulated/group_size_simulation.csv', index=False)

# 7. ocw_test_simulation.csv
# Simulate charges from 38 to 42 in 0.1 steps, 5 shots each
charges_ocw = np.arange(38.0, 42.1, 0.1)
data_ocw = []
for charge in charges_ocw:
    # SD with some variation to show false nodes
    base_sd = 10 + 5 * np.sin(2 * np.pi * (charge - 38) / 4) + np.random.normal(0, 1)
    sd = max(5, base_sd)  # Clip to positive
    vels = np.random.normal(2850, sd, 5)
    for vel in vels:
        data_ocw.append({'charge_gr': charge, 'velocity_fps': vel})
df_ocw = pd.DataFrame(data_ocw)
df_ocw.to_csv('data/simulated/ocw_test_simulation.csv', index=False)