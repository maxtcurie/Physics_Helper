import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import f

# Define the parameters for the F-distributions
dfn = [1, 3]  # degrees of freedom for the numerator
dfd = [1, 3]  # degrees of freedom for the denominator
x = np.linspace(0, 5, 1000)

# Create a plot for each combination of degrees of freedom
plt.figure(figsize=(12, 8))

for i in dfn:
    for j in dfd:
        y = f.pdf(x, i, j)
        plt.plot(x, y, label=f'dfn={i}, dfd={j}')

plt.title('F-distribution for various degrees of freedom')
plt.xlabel('x')
#plt.xscale('log')

plt.ylabel('Probability Density Function')
plt.legend()
plt.grid(True)
plt.show()


# Define the parameters for the F-distributions
i, j = 5, 10
x = np.linspace(0.1, 5, 1000)  # Avoid division by zero by starting from 0.1

# Calculate the F-distribution PDFs
F_ij = f.pdf(x, i, j)
F_ji = f.pdf(1/x, j, i)

# Demonstrate the relationship
relationship = F_ij * F_ji

print("Demonstration of the relationship F(x, i, j) = 1 / F(1/x, j, i):")
print(relationship)
plt.clf()
plt.plot(F_ij)
plt.plot(F_ji)

plt.plot(relationship)
plt.show()