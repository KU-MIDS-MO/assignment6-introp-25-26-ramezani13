import numpy as np

def estimate_pi(num_samples):

    count_inside = 0

    for _ in range(num_samples):
        ## generate random point (x, y) in [0,1] × [0,1]
        x = np.random.rand()
        y = np.random.rand()

        ## check if insid quarter circle
        if x*x + y*y <= 1.0:
            count_inside += 1

    ## Monte Carlo estimate
    pi_hat = 4.0 * count_inside / num_samples
    return float(pi_hat)
