import numpy as np

# Simulate shot groups to find relationship between ES and MR

def calculate_es(group_x, group_y):
    """Calculate extreme spread: max distance between any two points"""
    distances = []
    for i in range(len(group_x)):
        for j in range(i+1, len(group_x)):
            dist = np.sqrt((group_x[i] - group_x[j])**2 + (group_y[i] - group_y[j])**2)
            distances.append(dist)
    return max(distances) if distances else 0

def calculate_mr(group_x, group_y):
    """Calculate mean radius: average distance from centroid"""
    centroid_x = np.mean(group_x)
    centroid_y = np.mean(group_y)
    radii = np.sqrt((group_x - centroid_x)**2 + (group_y - centroid_y)**2)
    return np.mean(radii)

# Parameters
n_shots = 5  # Typical group size
n_simulations = 10000
sigma = 1.0  # Standard deviation in MOA

ratios = []

for sim in range(n_simulations):
    # Generate bivariate normal shots
    x_shots = np.random.normal(0, sigma, n_shots)
    y_shots = np.random.normal(0, sigma, n_shots)
    
    es = calculate_es(x_shots, y_shots)
    mr = calculate_mr(x_shots, y_shots)
    
    if es > 0:  # Avoid division by zero
        ratios.append(mr / es)

# Results
mean_ratio = np.mean(ratios)
std_ratio = np.std(ratios)

print("Mean MR/ES ratio: {:.3f}".format(mean_ratio))
print("Standard deviation: {:.3f}".format(std_ratio))
print("95% confidence interval: {:.3f} to {:.3f}".format(mean_ratio - 1.96*std_ratio, mean_ratio + 1.96*std_ratio))

# For different group sizes
for n in [3, 5, 10, 20, 30, 50, 100]:
    ratios_n = []
    for sim in range(1000):
        x_shots = np.random.normal(0, sigma, n)
        y_shots = np.random.normal(0, sigma, n)
        es = calculate_es(x_shots, y_shots)
        mr = calculate_mr(x_shots, y_shots)
        if es > 0:
            ratios_n.append(mr / es)
    avg_ratio = np.mean(ratios_n)
    print("For {} shots: MR/ES ≈ {:.3f}".format(n, avg_ratio))