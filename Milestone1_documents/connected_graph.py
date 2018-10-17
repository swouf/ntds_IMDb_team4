import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json

################################################################################
# Code for question 7
#
#
import queue as Q

def breadth_first_search(adjacency, source, destination):

    #print("Source : ", source, " Destination : ", destination)

    # Creates a node list with the number nodes contained in the adjacency matrix
    nodeList = adjacency.shape
    nodeList = nodeList[0]
    nodeList = np.full(nodeList, np.nan)

    # Initialize a queue
    queueBuffer = Q.SimpleQueue()

    # Initialize an array containing all the indexes of all the non-zero elements connecting the the 0 node with the others
    connectedNodesTo0 = np.nonzero(adjacency[source,:])

    # Init the queue
    for i in np.nditer(connectedNodesTo0):
        #print("i = ",i)
        queueBuffer.put((i,0))

    # Test the case where source == destination
    if source == destination :
        nodeList[destination] = 0
        return nodeList[destination]

    # Test each node if they are connected
    #
    # 1. Get the node in the queue and the distance from the source of the previous node.
    # 2. If the node has not been assigned a distance yet, assign it the distance of the previous node + 1.
    # 3. Get all the connected nodes and put them in the queue.
    # 4. When there is no more nodes in the queue, exit the loop.
    #
    while queueBuffer.empty() == False :
        node = queueBuffer.get()
        nodeDist = node [1]
        node = node[0]
        if np.isnan(nodeList[node]):
            nodeList[node] = nodeDist+1
            tmp = np.nonzero(adjacency[node,:])
            for j in np.nditer(tmp):
                queueBuffer.put((j,nodeList[node]))

    distance = nodeList[destination]
    return distance




def connected_graph(adjacency):
    """Determines whether a graph is connected.

    Parameters
    ----------
    adjacency: numpy array
        The (weighted) adjacency matrix of a graph.

    Returns
    -------
    bool
        True if the graph is connected, False otherwise.
    """
    # Init connected
    connected = False

    # Creates a node list with the number nodes contained in the adjacency matrix
    nodeList = adjacency.shape
    nodeList = nodeList[0]
    nodeList = np.full(nodeList, np.nan)

    # Initialize a queue
    queueBuffer = Q.SimpleQueue()

    # Initialize an array containing all the indexes of all the non-zero elements connecting the the 0 node with the others
    connectedNodesTo0 = np.nonzero(adjacency[0,:])

    # Init the queue
    for i in np.nditer(connectedNodesTo0):
        queueBuffer.put(i)

    # Test each node if they are connected
    #
    # 1. Get the node in the queue and the distance from the source of the previous node.
    # 2. If the node has not been assigned a distance yet, assign it the distance of the previous node + 1.
    # 3. Get all the connected nodes and put them in the queue.
    # 4. When there is no more nodes in the queue, exit the loop.
    #

    n = 0
    m = 0
    print(nodeList.size)

    while queueBuffer.empty() == False :
        n = n+1
        if n >= 10000:
            n = 0
            print("Number of connected nodes : ", np.nansum(nodeList))

        node = queueBuffer.get()
        tmp = np.nonzero(adjacency[node,:])
        for j in np.nditer(tmp):
            if np.isnan(nodeList[j]):
                nodeList[j] = 1
                queueBuffer.put(j)

    nbOfConnectedNodes = np.nansum(nodeList)
    nbOfExpectedConnectedNodes = nodeList.size

    print("nbOfConnectedNodes = ", nbOfConnectedNodes)
    print("nbOfExpectedConnectedNodes = ", nbOfExpectedConnectedNodes)

    if nbOfConnectedNodes == nbOfExpectedConnectedNodes :
        connected = True
    else :
        connected = False

    return connected
