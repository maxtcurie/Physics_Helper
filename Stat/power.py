from statsmodels.stats.power import TTestIndPower
import numpy as np
import matplotlib.pyplot as plt

# Parameters for power analysis
effect_size = 0.5
alpha = 0.05
power = 0.8

analysis = TTestIndPower()
sample_size = analysis.solve_power(effect_size=effect_size, alpha=alpha, power=power, alternative='two-sided')

print(f"Required sample size: {sample_size}")

# Plotting power curve
effect_sizes = np.linspace(0.1, 1.0, 50)
powers = analysis.power(effect_size=effect_sizes, nobs1=int(sample_size), alpha=alpha)

plt.plot(effect_sizes, powers)
plt.title('Power Curve')
plt.xlabel('Effect Size')
plt.ylabel('Power')
plt.axhline(0.8, color='red', linestyle='--')
plt.show()
