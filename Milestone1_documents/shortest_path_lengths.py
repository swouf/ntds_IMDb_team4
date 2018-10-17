import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json

################################################################################
# Code for question 9
#
#
import queue as Q

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
        The length of the shortest path from source to all nodes. Returned list should be of length n_nodes.
    """

    # Creates a node list with the number nodes contained in the adjacency matrix
    nodeList = adjacency.shape
    nodeList = nodeList[0]
    nodeList = np.full(nodeList, np.nan)

    nodeDist = 0

    # Initialize a queue
    queueBuffer = Q.SimpleQueue()

    # Initialize an array containing all the indexes of all the non-zero elements connecting the the 0 node with the others
    connectedNodesToSource = np.nonzero(adjacency[source,:])

    # Init the queue
    nodeDist = nodeDist+1
    for i in np.nditer(connectedNodesToSource):
        nodeList[i] = nodeDist
        queueBuffer.put(i)

    # Test the case where source == destination

    # Test each node if they are connected
    #
    # 1. Get the node in the queue and the distance from the source of the previous node.
    # 2. If the node has not been assigned a distance yet, assign it the distance of the previous node + 1.
    # 3. Get all the connected nodes and put them in the queue.
    # 4. When there is no more nodes in the queue, exit the loop.
    #
    while queueBuffer.empty() == False :
        nodeDist = nodeDist+1
        node = queueBuffer.get()
        tmp = np.nonzero(adjacency[node,:])
        for j in np.nditer(tmp):
            if np.isnan(nodeList[j]):
                nodeList[j] = nodeDist
                queueBuffer.put(j)

    return nodeList
