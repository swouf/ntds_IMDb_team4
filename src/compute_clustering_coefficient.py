def compute_clustering_coefficient(adjacency, node):
    """Compute the clustering coefficient of a node.

    Parameters
    ----------
    adjacency: numpy array
        The (weighted) adjacency matrix of a graph.
    node: int
        The node whose clustering coefficient will be computed. A number between 0 and n_nodes-1.

    Returns
    -------
    float
        The clustering coefficient of the node. A number between 0 and 1.
    """

    adjacency[adjacency !=0]=1 #masking to get the unweighted matrix
    clustering_coefficient=0
    idx_neighbours=np.nonzero(adjacency[node])  #get the indices of the neighbours
    number_neighbours=idx_neighbours[0].size    #get the number of neighbours

    if number_neighbours<2: #if only 0 or 1 neighbour, the clustering coefficient is equal to 0
           return 0

    #For all neighbours, see if they have links between them
    for j in range(number_neighbours):
        idx_test=idx_neighbours[0][j]
        nb_similar_neighbours=adjacency[node]*adjacency[idx_test]
        clustering_coefficient=clustering_coefficient+sum(nb_similar_neighbours)

    clustering_coefficient=clustering_coefficient/(number_neighbours*(number_neighbours-1))
    #no need to multiply by 2 because we already count each link twice

    return clustering_coefficient
