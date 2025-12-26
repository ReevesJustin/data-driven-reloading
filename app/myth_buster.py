"""
Myth Buster Streamlit App

This app provides tools for analyzing reloading data and understanding statistical concepts
in shooting and reloading.
"""

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
from sklearn.metrics import pairwise_distances
from scipy.spatial.distance import pdist, squareform
import warnings
warnings.filterwarnings('ignore')

# Set page config
st.set_page_config(page_title="Myth Buster", page_icon="🎯", layout="wide")

# Sidebar navigation
st.sidebar.title("Myth Buster Tools")
page = st.sidebar.selectbox(
    "Choose a tool:",
    [
        "Is My SD Real?",
        "Sample Size Calculator",
        "Compare Two Loads",
        "Group Size Analyzer",
        "The Reloading Casino"
    ]
)

def page_is_my_sd_real():
    """Page 1: Assess if observed SD is reliable."""
    st.title("Is My SD Real?")
    st.markdown("Estimate the confidence interval for your true population standard deviation.")

    col1, col2 = st.columns(2)

    with col1:
        observed_sd = st.number_input(
            "Observed Standard Deviation (fps)",
            min_value=0.0,
            value=10.0,
            step=0.1,
            help="The SD you calculated from your sample."
        )

        sample_size = st.number_input(
            "Sample Size",
            min_value=2,
            value=10,
            step=1,
            help="Number of shots in your sample."
        )

    with col2:
        threshold = st.number_input(
            "Threshold SD (fps)",
            min_value=0.0,
            value=5.0,
            step=0.1,
            help="Check probability true SD is below this value."
        )

        n_boot = st.slider(
            "Bootstrap Samples",
            min_value=1000,
            max_value=10000,
            value=5000,
            step=1000,
            help="Number of bootstrap resamples."
        )

    if st.button("Calculate"):
        try:
            # Simulate data with observed SD
            sample_data = np.random.normal(0, observed_sd, sample_size)

            # Bootstrap for SD distribution
            boot_sds = []
            for _ in range(n_boot):
                boot_sample = np.random.choice(sample_data, size=sample_size, replace=True)
                boot_sds.append(np.std(boot_sample, ddof=1))

            boot_sds = np.array(boot_sds)
            ci_lower = np.percentile(boot_sds, 2.5)
            ci_upper = np.percentile(boot_sds, 97.5)

            prob_below = np.mean(boot_sds < threshold) * 100

            st.success(f"95% CI for true SD: {ci_lower:.2f} - {ci_upper:.2f} fps")
            st.info(f"Probability true SD < {threshold} fps: {prob_below:.1f}%")

            # Plot
            fig, ax = plt.subplots(figsize=(8, 5))
            ax.hist(boot_sds, bins=50, alpha=0.7, color='blue', density=True)
            ax.axvline(observed_sd, color='red', linestyle='--', label=f'Observed SD: {observed_sd:.2f}')
            ax.axvline(ci_lower, color='green', linestyle=':', label=f'CI Lower: {ci_lower:.2f}')
            ax.axvline(ci_upper, color='green', linestyle=':', label=f'CI Upper: {ci_upper:.2f}')
            ax.set_xlabel('Standard Deviation (fps)')
            ax.set_ylabel('Density')
            ax.set_title('Bootstrap Distribution of True SD')
            ax.legend()
            st.pyplot(fig)

        except Exception as e:
            st.error(f"Error in calculation: {str(e)}")

def page_sample_size_calculator():
    """Page 2: Calculate required sample size for detecting effect."""
    st.title("Sample Size Calculator")
    st.markdown("Determine sample size needed to detect a difference in velocities.")

    col1, col2 = st.columns(2)

    with col1:
        effect_size = st.number_input(
            "Effect Size (fps)",
            min_value=0.0,
            value=5.0,
            step=0.1,
            help="Minimum difference you want to detect."
        )

        pop_sd = st.number_input(
            "Population SD (fps)",
            min_value=0.0,
            value=10.0,
            step=0.1,
            help="Estimated true SD of velocities."
        )

        alpha = st.slider(
            "Significance Level (α)",
            min_value=0.01,
            max_value=0.10,
            value=0.05,
            step=0.01,
            help="Type I error rate."
        )

    with col2:
        power = st.slider(
            "Power (1-β)",
            min_value=0.8,
            max_value=0.99,
            value=0.8,
            step=0.01,
            help="Probability of detecting effect if it exists."
        )

    if st.button("Calculate"):
        try:
            # Power analysis for two-sample t-test
            # Effect size d = delta / sigma
            d = effect_size / pop_sd

            # Approximate sample size per group
            # Using formula: n = (z_alpha + z_beta)^2 / d^2
            z_alpha = stats.norm.ppf(1 - alpha/2)
            z_beta = stats.norm.ppf(power)
            n_per_group = int(np.ceil((z_alpha + z_beta)**2 / d**2))

            st.success(f"Required sample size per group: {n_per_group}")

            # Plot power curve
            sample_sizes = np.arange(5, 200, 5)
            powers = []
            for n in sample_sizes:
                se = pop_sd * np.sqrt(2/n)  # SE of difference
                t_crit = stats.t.ppf(1 - alpha/2, df=2*n-2)
                power_val = 1 - stats.t.cdf(t_crit - effect_size/se, df=2*n-2)
                powers.append(power_val)

            fig, ax = plt.subplots(figsize=(8, 5))
            ax.plot(sample_sizes, powers, 'b-', linewidth=2)
            ax.axhline(power, color='r', linestyle='--', label=f'Desired Power: {power:.2f}')
            ax.axvline(n_per_group, color='g', linestyle='--', label=f'Calculated n: {n_per_group}')
            ax.set_xlabel('Sample Size per Group')
            ax.set_ylabel('Power')
            ax.set_title('Power vs Sample Size')
            ax.legend()
            ax.grid(True)
            st.pyplot(fig)

        except Exception as e:
            st.error(f"Error in calculation: {str(e)}")

def page_compare_two_loads():
    """Page 3: Compare two sets of velocity data."""
    st.title("Compare Two Loads")
    st.markdown("Paste velocity data and compare two loads statistically.")

    col1, col2 = st.columns(2)

    with col1:
        load1_data = st.text_area(
            "Load 1 Velocities (comma-separated)",
            placeholder="e.g., 2650, 2670, 2645, ...",
            height=100
        )

        load1_name = st.text_input("Load 1 Name", value="Load A")

    with col2:
        load2_data = st.text_area(
            "Load 2 Velocities (comma-separated)",
            placeholder="e.g., 2660, 2680, 2655, ...",
            height=100
        )

        load2_name = st.text_input("Load 2 Name", value="Load B")

    if st.button("Compare"):
        try:
            # Parse data
            load1_vels = [float(x.strip()) for x in load1_data.split(',') if x.strip()]
            load2_vels = [float(x.strip()) for x in load2_data.split(',') if x.strip()]

            if len(load1_vels) < 2 or len(load2_vels) < 2:
                st.error("Each load needs at least 2 velocity measurements.")
                return

            load1_vels = np.array(load1_vels)
            load2_vels = np.array(load2_vels)

            # Statistics
            mean1, sd1 = np.mean(load1_vels), np.std(load1_vels, ddof=1)
            mean2, sd2 = np.mean(load2_vels), np.std(load2_vels, ddof=1)

            # T-test
            t_stat, p_val = stats.ttest_ind(load1_vels, load2_vels)
            mean_diff = mean1 - mean2
            se_diff = np.sqrt(sd1**2/len(load1_vels) + sd2**2/len(load2_vels))
            ci_lower = mean_diff - 1.96 * se_diff
            ci_upper = mean_diff + 1.96 * se_diff

            # Display results
            st.subheader("Results")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric(f"{load1_name} Mean", f"{mean1:.1f} fps", f"SD: {sd1:.1f}")
            with col2:
                st.metric(f"{load2_name} Mean", f"{mean2:.1f} fps", f"SD: {sd2:.1f}")
            with col3:
                st.metric("Mean Difference", f"{mean_diff:.1f} fps", f"p-value: {p_val:.3f}")

            st.write(f"95% CI for difference: ({ci_lower:.1f}, {ci_upper:.1f}) fps")

            if p_val < 0.05:
                st.success("Significant difference detected (p < 0.05)")
            else:
                st.info("No significant difference detected (p >= 0.05)")

            # Plots
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

            # Histograms
            ax1.hist(load1_vels, alpha=0.7, label=load1_name, bins=10)
            ax1.hist(load2_vels, alpha=0.7, label=load2_name, bins=10)
            ax1.set_xlabel('Velocity (fps)')
            ax1.set_ylabel('Frequency')
            ax1.set_title('Velocity Distributions')
            ax1.legend()

            # Box plots
            ax2.boxplot([load1_vels, load2_vels], labels=[load1_name, load2_name])
            ax2.set_ylabel('Velocity (fps)')
            ax2.set_title('Velocity Box Plots')

            plt.tight_layout()
            st.pyplot(fig)

        except ValueError as e:
            st.error("Invalid data format. Please enter comma-separated numbers.")
        except Exception as e:
            st.error(f"Error in comparison: {str(e)}")

def page_group_size_analyzer():
    """Page 4: Analyze group size from shot coordinates."""
    st.title("Group Size Analyzer")
    st.markdown("Enter shot coordinates to analyze group size and accuracy.")

    coords_input = st.text_area(
        "Shot Coordinates (space-separated x,y pairs)",
        placeholder="e.g., 0,0 1,2 -1,1 0.5,-0.5",
        height=100,
        help="Enter coordinates as 'x1,y1 x2,y2 ...' in inches."
    )

    if st.button("Analyze"):
        try:
            # Parse coordinates
            coords_str = coords_input.split()
            coords = []
            for pair in coords_str:
                x, y = map(float, pair.split(','))
                coords.append([x, y])
            coords = np.array(coords)

            if len(coords) < 2:
                st.error("Need at least 2 shot coordinates.")
                return

            # Calculate center
            center = np.mean(coords, axis=0)

            # Distances from center
            distances = np.linalg.norm(coords - center, axis=1)
            mean_radius = np.mean(distances)
            es = np.max(distances) * 2  # Extreme spread

            # CI for true accuracy (mean radius)
            # Bootstrap
            n_boot = 1000
            boot_radii = []
            for _ in range(n_boot):
                boot_idx = np.random.choice(len(distances), size=len(distances), replace=True)
                boot_dists = distances[boot_idx]
                boot_radii.append(np.mean(boot_dists))

            boot_radii = np.array(boot_radii)
            ci_lower = np.percentile(boot_radii, 2.5)
            ci_upper = np.percentile(boot_radii, 97.5)

            st.subheader("Results")
            st.metric("Mean Radius", f"{mean_radius:.3f} inches")
            st.metric("Extreme Spread", f"{es:.3f} inches")
            st.write(f"95% CI for mean radius: ({ci_lower:.3f}, {ci_upper:.3f}) inches")

            # Plot
            fig, ax = plt.subplots(figsize=(8, 8))
            ax.scatter(coords[:, 0], coords[:, 1], c='red', s=50, alpha=0.7, label='Shots')
            ax.scatter(center[0], center[1], c='blue', s=100, marker='x', label='Center')
            circle = plt.Circle(center, mean_radius, fill=False, color='green', linestyle='--', label=f'Mean Radius: {mean_radius:.3f}"')
            ax.add_artist(circle)
            ax.set_xlabel('X (inches)')
            ax.set_ylabel('Y (inches)')
            ax.set_title('Shot Group')
            ax.legend()
            ax.axis('equal')
            ax.grid(True)
            st.pyplot(fig)

        except ValueError as e:
            st.error("Invalid coordinate format. Use 'x,y x,y ...'")
        except Exception as e:
            st.error(f"Error in analysis: {str(e)}")

def page_reloading_casino():
    """Page 5: Game to demonstrate statistical testing concepts."""
    st.title("The Reloading Casino 🎰")
    st.markdown("Test different loads and find the 'optimal' one. Learn why chasing the best group wastes ammo!")

    # Initialize session state
    if 'rounds_left' not in st.session_state:
        st.session_state.rounds_left = 200
        st.session_state.loads_tested = {}
        st.session_state.true_optimal = np.random.uniform(2600, 2700)  # True optimal velocity
        st.session_state.leaderboard = []

    st.sidebar.subheader("Game Status")
    st.sidebar.metric("Rounds Left", st.session_state.rounds_left)

    if st.session_state.rounds_left > 0:
        shots_per_test = st.slider("Shots per Test Load", min_value=3, max_value=20, value=5)
        test_button = st.button(f"Test Load (costs {shots_per_test} rounds)")

        if test_button:
            # Simulate testing a load
            true_vel = st.session_state.true_optimal + np.random.normal(0, 15)  # Variation
            velocities = np.random.normal(true_vel, 10, shots_per_test)
            mean_vel = np.mean(velocities)
            sd_vel = np.std(velocities, ddof=1)

            load_name = f"Load_{len(st.session_state.loads_tested)+1}"
            st.session_state.loads_tested[load_name] = {
                'mean': mean_vel,
                'sd': sd_vel,
                'shots': shots_per_test
            }
            st.session_state.rounds_left -= shots_per_test

            st.success(f"Tested {load_name}: Mean {mean_vel:.1f} fps, SD {sd_vel:.1f} fps")

        # Display current loads
        if st.session_state.loads_tested:
            st.subheader("Your Tested Loads")
            df = pd.DataFrame.from_dict(st.session_state.loads_tested, orient='index')
            df = df.sort_values('mean', ascending=False)
            st.dataframe(df)

            best_load = df.iloc[0]
            st.metric("Current Best Load", f"{best_load.name}: {best_load['mean']:.1f} fps")

            # Check if optimal found
            if abs(best_load['mean'] - st.session_state.true_optimal) < 5:
                st.balloons()
                st.success("Congratulations! You found a near-optimal load!")
                if best_load.name not in [entry['load'] for entry in st.session_state.leaderboard]:
                    st.session_state.leaderboard.append({
                        'load': best_load.name,
                        'mean': best_load['mean'],
                        'rounds_used': 200 - st.session_state.rounds_left
                    })

    else:
        st.error("Out of rounds! Game over.")
        st.write(f"True optimal velocity was: {st.session_state.true_optimal:.1f} fps")
        st.subheader("Leaderboard")
        if st.session_state.leaderboard:
            leaderboard_df = pd.DataFrame(st.session_state.leaderboard)
            leaderboard_df = leaderboard_df.sort_values('rounds_used')
            st.dataframe(leaderboard_df)
        else:
            st.write("No optimal loads found.")

    if st.button("Reset Game"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.experimental_rerun()

# Main app logic
if page == "Is My SD Real?":
    page_is_my_sd_real()
elif page == "Sample Size Calculator":
    page_sample_size_calculator()
elif page == "Compare Two Loads":
    page_compare_two_loads()
elif page == "Group Size Analyzer":
    page_group_size_analyzer()
elif page == "The Reloading Casino":
    page_reloading_casino()