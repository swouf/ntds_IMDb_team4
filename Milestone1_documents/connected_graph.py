import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json

def breadth_first_search(adjacency, source, destination):
    nodeList = adjacency.shape
    nodeList = nodeList[0]
    nodeList = np.full(nodeList, np.nan)

    queue = np.nonzero(adjacency[source,:])
    queue = np.array(queue[0])

    k = 1

    if source == destination :
        nodeList[destination] = 0

    while np.isnan(nodeList[destination]):
        for i in np.nditer(queue) :
            #print("node = ", i)
            if np.isnan(nodeList[i]) :
                nodeList[i] = k
                tmp = np.nonzero(adjacency[i,:])
                tmp = np.array(tmp[0])
                #print(queue, "+" ,tmp)
                queue = np.concatenate((queue, tmp))


        k = k+1

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

    nodeList = adjacency.shape
    nodeList = nodeList[0]
    nodeList = np.full(nodeList, np.nan)

    nodeList[0] = 1;

    for i in range(0,nodeList.size):
        for j in range(i+1,nodeList.size):
            #print("i=",i,"j=",j, nodeList[j] ,np.isnan(nodeList[j]))
            if nodeList[i] == 1 and np.isnan(nodeList[j]):
                if np.isnan(breadth_first_search(adjacency,i,j)) == False:
                    nodeList[j] = 1
                else:
                    nodeList[j] = 0

    #print(nodeList)

    if np.sum(nodeList) == nodeList.size:
        connected = True
    else:
        connected = False


    return connected
