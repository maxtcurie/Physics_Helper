import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import chi2 as chi2_dist

# Create a simple dataset
data = {'Gender': ['Male', 'Male', 'Female', 'Female', 'Male', 'Female', 'Female', 'Male'],
        'Preference': ['A', 'B', 'A', 'A', 'B', 'B', 'A', 'A']}

# Convert the dataset into a pandas DataFrame
df = pd.DataFrame(data)

# Unique categories
genders = df['Gender'].unique()
preferences = df['Preference'].unique()

# Create the contingency table manually
contingency_table = np.zeros((len(genders), len(preferences)))

# Populate the contingency table
for i, gender in enumerate(genders):
    for j, preference in enumerate(preferences):
        contingency_table[i, j] = np.sum((df['Gender'] == gender) & (df['Preference'] == preference))



# Calculate the expected frequencies
row_totals = contingency_table.sum(axis=1).reshape(-1, 1)
col_totals = contingency_table.sum(axis=0).reshape(1, -1)
total = contingency_table.sum()
expected = row_totals @ col_totals / total

# Perform the Chi-squared test manually
chi2 = ((contingency_table - expected) ** 2 / expected).sum()

# Calculate degrees of freedom
dof = (contingency_table.shape[0] - 1) * (contingency_table.shape[1] - 1)

# Calculate the p-value using the chi-squared distribution
p = 1 - chi2_dist.cdf(chi2, dof)

# Output the results
print("\nChi-squared Test Results:")
print(f"Chi-squared value: {chi2}")
print(f"P-value: {p}")
print(f"Degrees of freedom: {dof}")
print("Observed frequencies:")
print(pd.DataFrame(contingency_table, index=genders, columns=preferences))
print("Expected frequencies:")
print(pd.DataFrame(expected, index=genders, columns=preferences))

# Interpretation of the results
alpha = 0.05
if p < alpha:
    print("\nSince the P-value is less than 0.05, we reject the null hypothesis.")
    print("There is a significant association between gender and preference.")
else:
    print("\nSince the P-value is greater than 0.05, we fail to reject the null hypothesis.")
    print("There is no significant association between gender and preference.")

# Plot the Chi-squared distribution
x = np.linspace(0, 20, 500)
y = chi2_dist.pdf(x, dof)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label=f'Chi-squared distribution (dof={dof})')
plt.axvline(chi2, color='r', linestyle='--', label=f'Chi-squared value = {chi2:.2f}')
plt.fill_between(x, 0, y, where=(x >= chi2), color='red', alpha=0.5, label=f'P-value = {p:.2f}')
plt.xlabel('Chi-squared value')
plt.ylabel(r'$\chi$ PDF')
plt.title('Chi-squared Distribution with Test Statistic')
plt.legend()
plt.grid(True)
plt.show()



dof_list=[1,3, 5,20]
# Plot the Chi-squared distribution
x = np.linspace(0, 20, 500)

plt.figure(figsize=(10, 6))
for dof in dof_list:
    y = chi2_dist.pdf(x, dof)
    plt.plot(x, y, label=f'Chi-squared distribution (dof={dof})')

plt.xlabel('Chi-squared value')
plt.ylabel(r'$\chi$ PDF')
plt.title('Chi-squared Distribution with Test Statistic')
plt.legend()
plt.grid(True)
plt.show()