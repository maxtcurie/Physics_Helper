import numpy as np
import matplotlib.pyplot as plt

n_B = 30
lambada_ = 0.002  # probability of starting a phone call 
mu = 0.003       # probability of ending of a phone call 

n_B_list = np.arange(1, n_B + 1)

# Compute logarithm of factorial
def log_factorial(n):
    return sum(np.log(np.arange(1, n + 1)))

# Calculate pi_i in log space
def pi_i_calc_log(lambada_, mu, i):
    if i == 0:
        return 0  # Log(1) = 0
    return i * np.log(lambada_/mu) - log_factorial(i)

# Calculate pi list in log space
def pi_list_calc_log(lambada_, mu, B):
    return [pi_i_calc_log(lambada_, mu, i) for i in range(B + 1)]

def pi_B_calc_log(lambada_, mu, B):
    log_pi_B = pi_i_calc_log(lambada_, mu, B)
    log_sum = np.log(sum(np.exp(pi_list_calc_log(lambada_, mu, B))))
    return np.exp(log_pi_B - log_sum)

pi_B_list = [pi_B_calc_log(lambada_, mu, B) for B in n_B_list] 

plt.clf()
plt.plot(n_B_list, pi_B_list)
plt.xlabel('B')
plt.ylabel(r'$\pi_B$')
plt.yscale('log')
plt.show()
