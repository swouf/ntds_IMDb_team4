import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
import queue as Q
import logging

################################################################################
# Code for question 11
#
#
def compute_paths(adjacency, source, target, length):
    """Compute the number of paths of a given length between a source and target node.

    Parameters
    ----------
    adjacency: numpy array
        The (weighted) adjacency matrix of a graph.
    source: int
        The source node. A number between 0 and n_nodes-1.
    target: int
        The target node. A number between 0 and n_nodes-1.
    length: int
        The path length to be considered.

    Returns
    -------
    int
        The number of paths.
    """

    n_paths = 0
    node = source
    nodeDist = 0

    # Creates a node list with the number nodes contained in the adjacency matrix
    nbOfNodes = (adjacency.shape)[0]

    # Initialize a queue
    queueBuffer = Q.SimpleQueue()

    # Init the queue
    queueBuffer.put((source, 0))

    # Test the case where source == target
    if source == target :
        n_paths = 0
        return n_paths

    # 1. Get the node in the queue and its distance from the source
    # 2. Find the adjacent nodes
    # 3. Test if the adjacent nodes are the target node and at a good distance
    #   - If *yes*, continue to the next node in the list
    #   - If *no*, but you are at a good distance, continue to the next node
    #       in the list without incrementing the path counter
    #   - Else, juste add the node in the queue for further process
    while queueBuffer.empty() == False :
        (node,nodeDist) = queueBuffer.get()

        tmp = np.nonzero(adjacency[node,:])
        for j in np.nditer(tmp):
            if j == target and (nodeDist+1) == length :
                n_paths = n_paths + 1
                continue
            elif (nodeDist+1) == length :
                continue
            else:
                queueBuffer.put((j,nodeDist+1))

    return n_paths
