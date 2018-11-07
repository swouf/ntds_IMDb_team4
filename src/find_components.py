def find_components(adjacency):
    """Find the connected components of a graph.

    Parameters
    ----------
    adjacency: numpy array
        The (weighted) adjacency matrix of a graph.

    Returns
    -------
    list of numpy arrays
        A list of adjacency matrices, one per connected component.
    """
    import numpy as np
    import queue as Q

    #initializing the array used to store the indices of nodes in each connected component
    connectedIndices = np.zeros((adjacency.shape[0],adjacency.shape[0]))

    #array used to keep track of the visited nodes (NaN = not visited):
    nodeList = np.full(adjacency.shape[0], np.nan)

    #initializing a queue to store connected nodes
    queueBuffer = Q.Queue()



    for i in range(adjacency.shape[0]):
        if np.isnan(nodeList[i]):
            #if the node has no connections to the other nodes
            if sum(adjacency[i,:]) == 0:
                connectedIndices[i,i] = 1
                nodeList[i] = 1
            else:
                #initializing the connections of node i
                connectionsToI = np.nonzero(adjacency[i,:])

                #We will add to queue the nodes connected to the first not visited (=NaN) node in nodeList
                for k in np.nditer(connectionsToI):
                    queueBuffer.put(k)

                #extracting all the nodes that have a path to node i
                while queueBuffer.empty() == False:
                    node = queueBuffer.get()
                    tmp = np.nonzero(adjacency[node,:])
                    for j in np.nditer(tmp):
                        if np.isnan(nodeList[j]):
                            nodeList[j] = 1
                            queueBuffer.put(j)

                    if i == 0:
                        connectedIndices[i,:]=nodeList
                    else:
                        connectedIndices[i,:]=nodeList-np.nansum(connectedIndices, axis=0)

    #converting NaN values to zeros:
    connectedIndices=np.nan_to_num(connectedIndices)

    #deleting zero lines:
    connectedIndices = connectedIndices[~(connectedIndices==0).all(1)]

    #Now let's build a 3D matrix with the adjecency matrices of each connected componnent

    n_components = connectedIndices.shape[0] #number of total connected components, including isolated nodes
    #components = np.zeros((n_components,adjacency.shape[0],adjacency.shape[0]))

    return connectedIndices
