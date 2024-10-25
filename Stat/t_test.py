import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Generate random data
np.random.seed(0)
group1 = np.random.normal(50, 10, 1000)
group2 = np.random.normal(55, 10, 1000)

# Perform t-test
t_stat, p_value = stats.ttest_ind(group1, group2)

print(f"T-statistic: {t_stat}")
print(f"P-value: {p_value}")

# Plotting
plt.hist(group1, bins=20, alpha=0.5, label='Group 1')
plt.hist(group2, bins=20, alpha=0.5, label='Group 2')
plt.legend(loc='upper right')
plt.title('T-test Example')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
