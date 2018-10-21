#find_components(adjacency)

def reshape_adjacency(source_index,newNode,adjacency):

    for j in range(0,adjacency.shape[0]):
        if j!=newNode or j not in source_index:
            #Delete all the row that are not in examened
            reshapedAdjacency=np.delete(adjacency ,j, axis=0)
            #Delete all the column that are not  examened
            reshapedAdjacency=np.delete(reshapedAdjacency ,j, axis=1)
            break
    
    #Delete all the row that are not in the connected 
    reshapedAdjacency=np.delete(adjacency , j,0)

    return reshapedAdjacency

def find_components(adjacency):

   #initialisation

    nodeList = np.full(adjacency.shape[0],0)
   
    newComponent=0
    components= np.empty(nodeList.size)
    components.fill(np.nan)
    tmp = []
   
    while np.nonzero(nodeList) and (newComponent<nodeList.size):
        for i in range(0,nodeList.size):
            tmp=reshape_adjacency(tmp,i,adjacency)
            if connected_graph(tmp)==true and nodeList[i]==0:
                components[newComponent]=append(components[newComponent],i)
                nodeList[i]=1
            
        
    
    newCoumponent=+1

#remove all the nan elements in components
    components = components[numpy.logical_not(numpy.isnan(x))]
    return components

components = find_components(adjacency)
components
