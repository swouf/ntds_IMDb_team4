import random

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy

# Code question 1 milestone 2


def erdos_renyi(n, p, seed=None):
    """Create an instance from the Erdos-Renyi graph model.

    Parameters
    ----------
    n: int
        Size of the graph.
    p: float
        Edge probability. A number between 0 and 1.
    seed: int (optional)
        Seed for the random number generator. To get reproducible results.

    Returns
    -------
    adjacency
        The adjacency matrix of a graph.
    """

    np.random.seed(seed)

    adjacency = np.zeros((n,n), dtype=float)

    for i in range(1,n):
        for j in range(0,i):
            adjacency[i,j] = (np.random.random()<p)
            adjacency[j,i] = adjacency[i,j]

    return adjacency
