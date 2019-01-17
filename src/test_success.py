
def compute_kmeans(coordinates, k_clusters):
    from sklearn.cluster import KMeans

    kmeans = KMeans(n_clusters=k_clusters, random_state=0).fit(coordinates)

    predictedLabels = kmeans.labels_
    
    return predictedLabels

def reorder_adjacency(adjacency, predictedLabels):
    import numpy as np

    s = adjacency.shape[0]

    tmp_adjacency = np.zeros((s,s))
    ordered_adjacency = np.zeros((s,s))
    
    k_clusters = np.unique(predictedLabels).shape[0]

    a = 0
    for k in range(0,k_clusters):
        indexes = np.argwhere(predictedLabels==k)
        for i in np.nditer(indexes):
            tmp_adjacency[a,:] = adjacency[i,:]
            a = a+1
        
    a = 0
    for k in range(0,k_clusters):
        indexes = np.argwhere(predictedLabels==k)
        for i in np.nditer(indexes):
            ordered_adjacency[:,a] = tmp_adjacency[:,i]
            a = a+1
    return ordered_adjacency;