import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma

# T-distribution parameters
degrees_of_freedom = [1, 4, 40]  # degrees of freedom

# Set up the range of x values for the plot
x = np.linspace(-4, 4, 1000)

# Normal Distribution parameters
mu = 0  # mean
sigma = 1  # standard deviation

# Calculate the PDF of the Normal Distribution manually
pdf_normal = (1 / (np.sqrt(2 * np.pi * sigma**2))) * np.exp(-0.5 * ((x - mu)**2) / sigma**2)

# Calculate the PDF of the T-Distribution manually
def pdf_t(x, df):
    return (gamma((df + 1) / 2) / 
            (np.sqrt(df * np.pi) * gamma(df / 2))) * \
           (1 + (x**2 / df))**(-((df + 1) / 2))

# Create the plot
plt.figure(figsize=(8, 4))
plt.plot(x, pdf_normal, label='Normal Distribution', color='blue')

colors = ['orange', 'green', 'red']
for i, df in enumerate(degrees_of_freedom):
    plt.plot(x, pdf_t(x, df), label=f'T-Distribution (df={df})', linestyle='dashed', color=colors[i])

plt.title('Comparison of Normal and T-Distributions')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True)
plt.show()
