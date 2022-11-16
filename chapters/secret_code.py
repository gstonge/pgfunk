import numpy as np

def poisson_branching_process(T):
    R = 1.5
    n = [5]
    for t in range(1,T):
        n.append(np.random.poisson(R*n[t-1]))
    return n

def poisson_branching_process_with_noise(T):
    n = poisson_branching_process(T)
    n_out = [np.random.binomial(n_,0.1) for n_ in n]
    return n_out

