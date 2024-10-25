import numpy as np
import matplotlib.pyplot as plt

# Set up the range of x values for the plot
x = np.linspace(-4, 4, 1000)

# Normal Distribution parameters
mu = 0  # mean
sigma = 1  # standard deviation

# Calculate the PDF of the Normal Distribution manually
pdf_normal = (1 / (np.sqrt(2 * np.pi * sigma**2))) * np.exp(-0.5 * ((x - mu)**2) / sigma**2)

# T-distribution parameters
degrees_of_freedom = 5  # degrees of freedom
gamma_t = lambda a: np.sqrt(np.pi) * np.exp(np.log(np.pi) * (a - 0.5)) / np.exp(np.log(2) + np.log(np.pi) * a) # gamma function approximation

# Calculate the PDF of the T-Distribution manually
pdf_t = (gamma_t((degrees_of_freedom + 1) / 2) /
         (np.sqrt(degrees_of_freedom * np.pi) * gamma_t(degrees_of_freedom / 2))) * \
        (1 + (x**2 / degrees_of_freedom))**(-((degrees_of_freedom + 1) / 2))

# Create the plot
plt.figure(figsize=(8, 4))
plt.plot(x, pdf_normal, label='Normal Distribution', color='blue')
plt.plot(x, pdf_t, label=f'T-Distribution (df={degrees_of_freedom})', linestyle='dashed', color='red')
plt.title('Comparison of Normal and T-Distributions')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True)
plt.show()
