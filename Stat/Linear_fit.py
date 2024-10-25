import numpy as np
import matplotlib.pyplot as plt

# Generating synthetic data
np.random.seed(0)
X = np.random.rand(100, 2)  # 100 samples, 2 predictors
y = 3 + 5*X[:, 0] + 2*X[:, 1] + np.random.randn(100)  # Dependent variable with noise

# Add a column of ones to X to account for the intercept term
X = np.hstack((np.ones((X.shape[0], 1)), X))

# Calculate the OLS estimates using the normal equation
XtX = np.dot(X.T, X)
XtX_inv = np.linalg.inv(XtX)
Xty = np.dot(X.T, y)
beta_hat = np.dot(XtX_inv, Xty)

# Predicting y using the estimated coefficients
y_pred = np.dot(X, beta_hat)

# Residuals
residuals = y - y_pred

# Linearity: Residual Plot
plt.scatter(y_pred, residuals)
plt.axhline(y=0, color='r', linestyle='--')
plt.xlabel('Predicted values')
plt.ylabel('Residuals')
plt.title('Residual Plot')
plt.show()

# No Endogeneity: Correlation between predictors and residuals
corr_matrix = np.corrcoef(X[:, 1:], residuals, rowvar=False)
print("Correlation between predictors and residuals:", corr_matrix[:-1, -1])

# Homoscedasticity: Plotting residuals vs fitted values
plt.scatter(y_pred, residuals)
plt.axhline(y=0, color='r', linestyle='--')
plt.xlabel('Fitted values')
plt.ylabel('Residuals')
plt.title('Residuals vs Fitted values for Homoscedasticity')
plt.show()

# No Autocorrelation: Durbin-Watson statistic
dw_stat = np.sum(np.diff(residuals)**2) / np.sum(residuals**2)
print("Durbin-Watson statistic:", dw_stat)
print("Durbin-Watson closes to 2 means no autocorrelation")

# Normality: Custom QQ plot
def qq_plot(data):
    data_sorted = np.sort(data)
    n = len(data)
    theoretical_quantiles = np.array([(i - 0.5) / n for i in range(1, n + 1)])
    normal_quantiles = np.percentile(np.random.normal(size=100000), theoretical_quantiles * 100)
    
    plt.scatter(normal_quantiles, data_sorted)
    plt.plot([normal_quantiles[0], normal_quantiles[-1]], [data_sorted[0], data_sorted[-1]], 'r--')
    plt.xlabel('Theoretical Quantiles')
    plt.ylabel('Sample Quantiles')
    plt.title('QQ Plot')
    plt.show()

qq_plot(residuals)

# A simple normality check: checking skewness and kurtosis
def skewness(data):
    n = len(data)
    mean_data = np.mean(data)
    std_data = np.std(data, ddof=1)
    skew = np.sum(((data - mean_data) / std_data) ** 3) / n
    return skew

def kurtosis(data):
    n = len(data)
    mean_data = np.mean(data)
    std_data = np.std(data, ddof=1)
    kurt = np.sum(((data - mean_data) / std_data) ** 4) / n - 3
    return kurt

skew_value = skewness(residuals)
kurt_value = kurtosis(residuals)

print("Skewness of residuals (acceptable -0.5 ~ 0.5):", skew_value)
print("Kurtosis of residuals (acceptable -0.5 ~ 0.5):", kurt_value)
