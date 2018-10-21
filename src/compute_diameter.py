import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
import queue as Q
import logging

from shortest_path_lengths import compute_shortest_path_lengths

################################################################################
# Code for question 10
#
#
def compute_diameter(adjacency,nbOfSamples=1000):

    # Init diameter
    diameter = 0

    # Get the number of nodes
    nbOfNodes = (adjacency.shape)[0]

    # Init an nparray to contain all the length between nodes
    shortest_path_lengths = np.zeros(nbOfNodes, np.int32)

    # Make a sampling of the nodes but if the number of samples exceed the
    # number of nodes, keep the list of nodes.
    if nbOfSamples >= nbOfNodes:
        samples = range(0,nbOfNodes)
    else:
        samples = np.random.randint(0,nbOfNodes,(1000))

    logging.info(f'nbOfNodes = {nbOfNodes}')
    logging.info(f'nbOfSamples = {nbOfSamples}')

    # Compute the distance for each node in the list between itself and all the
    # other nodes
    for i in samples:
        logging.debug(f'Testing node {i} and diameter = {diameter}')

        shortest_path_lengths = compute_shortest_path_lengths(adjacency, i)
        maxVal = np.amax(shortest_path_lengths)
        if maxVal > diameter:
            diameter = maxVal

    return diameter
