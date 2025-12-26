#!/usr/bin/env python3
"""
Myth Buster Calculator

Simulate common reloading myths and debunk with data.
"""

import numpy as np
import matplotlib.pyplot as plt

def simulate_ocw_myth():
    # Simulate Optimal Charge Weight myth
    # Small samples make multiple weights look good
    true_sd = 12  # fps
    sample_sizes = [5, 10, 20]
    charges = np.linspace(39, 42, 10)

    for n in sample_sizes:
        sds = []
        for charge in charges:
            velocities = np.random.normal(2700, true_sd, n)
            sds.append(np.std(velocities))
        plt.plot(charges, sds, label=f'n={n}')

    plt.xlabel('Charge Weight (gr)')
    plt.ylabel('SD (fps)')
    plt.title('OCW Myth: Small Samples Create Illusions')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    simulate_ocw_myth()