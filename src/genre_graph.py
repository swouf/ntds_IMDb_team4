def make_genre_adjacency(movies):
    
    import json
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import logging
    
    genres = movies['genres'].copy()
    
    n_nodes=len(genres)

    adjacency = np.zeros((n_nodes, n_nodes), dtype=bool)

    for genre in enumerate(genres):
        b = genres.copy()
        b = b.apply(lambda x: x==genre[1])
        adjacency[:,genre[0]] = b.values
    np.fill_diagonal(adjacency, 0)
    
    return adjacency