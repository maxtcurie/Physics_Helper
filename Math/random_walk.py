import numpy as np

def prob_step_absorption(p, N, n):
    """
    Calculate the expected number of steps to absorption for a 1D random walk 
    with two absorbing barriers at 0 and N.
    
    p: Probability of moving left
    q: Probability of moving right (1-p)
    N: Position of the rightmost absorbing barrier
    n: Starting position (0 < n < N)
    
    Returns:
    Expected number of steps to be absorbed at the left end,
    Expected number of steps to be absorbed at the right end
    """
    q = 1-p
    
    # Creating the Q matrix
    Q = np.zeros((N-1, N-1))
    
    # Filling the diagonal above the main diagonal
    np.fill_diagonal(Q[:, 1:], q)
    # Filling the diagonal below the main diagonal
    np.fill_diagonal(Q[1:, :], p)
    
    # R matrix: transition from transient to absorbing states
    R = np.zeros((N-1, 2))
    R[0, 0] = p
    R[-1, 1] = q


    # Computing the fundamental matrix N
    I = np.identity(N-1)
    N_matrix = np.linalg.inv(I - Q)
    
    # Calculate expected steps to each absorbing barrier
    NR = np.dot(N_matrix, R)

    prob_left_end =NR[n-1, 0]
    prob_right_end=NR[n-1, 1]
    print(N_matrix.shape)

    
    E=np.sum(N_matrix,axis=(1))

    # Expected steps to absorption into specific absorbing states
    expected_steps_to_absorbing_states = np.outer(E, np.sum(R, axis=0))

    print(E)
    print(expected_steps_to_absorbing_states)
    step_left_end = 0
    step_right_end= 0

    return prob_left_end, prob_right_end,step_left_end, step_right_end

p = 0.5  # Probability of moving left for a symmetric walk
N = 10   # Absorbing barriers at 0 and 10
n = 2    # Starting position

prob_left_end, prob_right_end,\
step_left_end, step_right_end = prob_step_absorption(p, N, n)

print(f"Probability to be absorbed at the left end (0): {prob_left_end}")
print(f"Probability to be absorbed at the right end (N): {prob_right_end}")


print(f"Expected steps to be absorbed at the left end (0): {step_left_end}")
print(f"Expected steps to be absorbed at the right end (N): {step_right_end}")

