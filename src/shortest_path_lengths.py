import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
import queue as Q

################################################################################
# Code for question 9
#
#
def compute_shortest_path_lengths(adjacency, source):
    """Compute the shortest path length between a source node and all nodes.

    Parameters
    ----------
    adjacency: numpy array
        The (weighted) adjacency matrix of a graph.
    source: int
        The source node. A number between 0 and n_nodes-1.

    Returns
    -------
    list of ints
        The length of the shortest path from source to all nodes. Returned list
        should be of length n_nodes.
    """

    # Creates a node list with the number of nodes contained in the adjacency
    # matrix
    nodeList = adjacency.shape
    nodeList = nodeList[0]
    nodeList = np.full(nodeList, np.nan)

    # Set the distance of the source node to 0
    nodeList[source] = 0

    # Initialize a queue
    queueBuffer = Q.SimpleQueue()

    # Initialize an array containing all the indexes of all the non-zero
    # elements connecting the the 0 node with the others
    connectedNodesToSource = np.nonzero(adjacency[source,:])

    # Init the queue and set the distances of the adjacent nodes
    # (to the source) to 1
    for i in np.nditer(connectedNodesToSource):
        nodeList[i] = 1
        queueBuffer.put(i)

    # Iterate over the nodes and calculate their distance
    while queueBuffer.empty() == False :
        node = queueBuffer.get() # Get the node in the queue
        tmp = np.nonzero(adjacency[node,:]) # Get a list of the connected nodes
        for j in np.nditer(tmp): # Iterate over the connected nodes
            if np.isnan(nodeList[j]): # Eliminate the ones that are already been processed
                nodeList[j] = nodeList[node]+1 # Add, for each node, their distance to the source node using the distance of the parent node
                queueBuffer.put(j) # Place it in the queue

    shortest_path_lengths = np.array(nodeList, np.int32)
    return shortest_path_lengths
