import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Sample data
np.random.seed(42)  # For reproducibility
sample_data = np.random.normal(loc=5, scale=2, size=30)  # Sample data from a normal distribution

# Population mean (hypothetical)
population_mean = 5.5

# Calculate the sample mean and standard deviation
sample_mean = np.mean(sample_data)
sample_std = np.std(sample_data, ddof=1)

# Calculate the t-statistic
t_statistic = (sample_mean - population_mean) / (sample_std / np.sqrt(len(sample_data)))

# Degrees of freedom
df = len(sample_data) - 1

# Calculate the p-value (two-tailed test)
p_value = 2 * (1 - stats.t.cdf(np.abs(t_statistic), df))

# Plot the sample data
plt.figure(figsize=(12, 6))

# Histogram of the sample data
plt.subplot(1, 2, 1)
plt.hist(sample_data, bins=10, edgecolor='black')
plt.axvline(sample_mean, color='r', linestyle='dashed', linewidth=2)
plt.title('Sample Data Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend(['Sample Mean'])

# Plot the t-distribution
x = np.linspace(-4, 4, 1000)
y = stats.t.pdf(x, df)
plt.subplot(1, 2, 2)
plt.plot(x, y, label='t-distribution')
plt.axvline(t_statistic, color='r', linestyle='dashed', linewidth=2)
plt.axvline(-t_statistic, color='r', linestyle='dashed', linewidth=2)
plt.fill_between(x, 0, y, where=(x > np.abs(t_statistic)), color='grey', alpha=0.5)
plt.fill_between(x, 0, y, where=(x < -np.abs(t_statistic)), color='grey', alpha=0.5)
plt.title('t-distribution with Sample t-statistic')
plt.xlabel('t-value')
plt.ylabel('Probability Density')
plt.legend(['t-distribution', 't-statistic'])

plt.tight_layout()
plt.show()

print(f"Sample Mean: {sample_mean}")
print(f"T-Statistic: {t_statistic}")
print(f"P-Value: {p_value}")

# Interpretation
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: There is a significant difference between the sample mean and the population mean.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference between the sample mean and the population mean.")
