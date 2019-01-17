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

def compute_ROI_genre(movies):
    
    import json
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import logging
    
    list_genres=movies[['genres_names','genres']].copy()
    list_genres=list_genres.drop_duplicates()
    list_genres=list_genres.set_index('genres')
    
    sumROI = movies['ROI'].sum()

    roi = movies['ROI'].copy()

    #roi = roi.apply(lambda x: x/sumROI)
    perGenreROI = list_genres.copy()
    perGenreROI['ROI_fraction'] = 0
    perGenreROI['number_films'] = 0
    
    print(perGenreROI)

    for fraction in enumerate(roi):
        perGenreROI.loc[movies['genres'].iloc[fraction[0]],'ROI_fraction']+=fraction[1]
        perGenreROI.loc[movies['genres'].iloc[fraction[0]],'number_films']+=1
    
    perGenreROI.loc[:,'ROI_fraction'] = perGenreROI.loc[:,'ROI_fraction'].div(perGenreROI['number_films'])
    return perGenreROI