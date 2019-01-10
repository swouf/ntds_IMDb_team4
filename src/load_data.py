def load_dataframes():

    import json
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import queue as Q # Package used to manage queues
    import logging

    # The flattening of the data was achieved by using the code provided alongsided the dataset on kaggle
    # The following section is simply the application of the following method :
    #  https://www.kaggle.com/sohier/tmdb-format-introduction/notebook
    #########################################################################################################################
    #########################################################################################################################
    movies = pd.read_csv('./data/tmdb_5000_movies.csv')
    movies['release_date'] = pd.to_datetime(movies['release_date']).apply(lambda x: x.date())
    json_columns = ['genres', 'keywords', 'production_countries', 'production_companies', 'spoken_languages']
    for column in json_columns:
        movies[column] = movies[column].apply(json.loads)

    credits = pd.read_csv('./data/tmdb_5000_credits.csv')
    json_columns = ['cast', 'crew']
    for column in json_columns:
           credits[column] = credits[column].apply(json.loads)

    #give a new movie index to replace the current movie index
    new_movie_index=np.arange(movies.shape[0])
    movies['id']=new_movie_index
    credits['movie_id']=new_movie_index

    def safe_access(container, index_values):
        # return a missing value rather than an error upon indexing/key failure
        result = container
        try:
            for idx in index_values:
                result = result[idx]
            return result
        except IndexError or KeyError:
            return pd.np.nan

    credits.apply(lambda row: [x.update({'movie_id': row['movie_id']}) for x in row['cast']], axis=1);
    credits.apply(lambda row: [x.update({'movie_id': row['movie_id']}) for x in row['crew']], axis=1);
    credits.apply(lambda row: [person.update({'order': order}) for order, person in enumerate(row['crew'])], axis=1);
    
    movies.apply(lambda row: [x.update({'id': row['id']}) for x in row['genres']], axis=1);

    genre = []
    movies.genres.apply(lambda x: genre.extend(x))
    genre = pd.DataFrame(genre)
    genre['type'] = 'genre'
    genre=genre.drop_duplicates('id')
    genre['index']=genre['id']
    genre=genre.set_index('id') 
    list_of_genres=genre['name'].unique()
    #this list contains the genre types
    #There are 21 different genres
    nb_genres=len(list_of_genres)
    list_of_genres_id=pd.Series(range(nb_genres))
    list_of_genres_id
    gerne_names=genre['name'].copy()
    #transform the name of the genre into numbers
    factorized_names = pd.factorize(gerne_names)[0]
    movies['genres']=factorized_names
    #movies['genres']=genre['name']

    cast = []
    credits.cast.apply(lambda x: cast.extend(x))
    cast = pd.DataFrame(cast)
    cast['type'] = 'cast'

    crew = []
    credits.crew.apply(lambda x: crew.extend(x))
    crew = pd.DataFrame(crew)
    crew['type'] = 'crew'

    people = pd.concat([cast, crew],  ignore_index=True, sort=False)

    logging.info("Data loaded !");

    return (movies, people, list_of_genres_id)

def make_budget_based_adjacency(movies,list_of_genres_id):
    #Ma version (julien), utilise le budget, mais aussi le revenu, et fait la norme euclidienne entre les points.
    import json
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import queue as Q # Package used to manage queues
    import logging
    from scipy.spatial.distance import pdist, squareform

    #(movies, people) = load_dataframes();

    budgets = movies['budget'].copy()
    
    #try to use euclidian norm on budget+revenue
    features= movies.loc[:, ['budget', 'genres']]
    features_filtered=features[(features != 0).all(1)]
    
    budget_max = budgets.max();

    logging.info(f'The budget max = {budget_max}');

    budgets_filtered = budgets[budgets != 0];

    logging.info(budgets_filtered.head())

    budgets_filtered.to_csv('./data/budgets.csv');

    n_nodes=len(budgets_filtered)
    
    logging.info(f'The number of nodes is : {n_nodes}')
    
    #version initial de jérémy
    #movies_filtered_by_budget = movies.loc[budgets_filtered.index]
    #version de julien
    movies_filtered_by_budget=movies.loc[features_filtered.index]
    
    movies_genres_id = movies_filtered_by_budget['genres'].copy()

    adjacency = np.zeros((n_nodes, n_nodes), dtype=float)
    
 #version initiale de jérémy
    #k = 0
    #for movieBudget in enumerate(budgets_filtered):
        #b = budgets_filtered.copy()
        #b = b.apply(lambda x: budget_max-abs(x-movieBudget[1]))
        #adjacency[:,k] = b.values
        #adjacency[:,k] = b.values/budget_max;
        #adjacency[:,k]=weights
        #k += 1
    
    #version julien avec norm euclidienne
    distances = pdist(features_filtered, metric='euclidean')
    kernel_width = distances.mean()
    weights = np.exp(-distances**2 / kernel_width**2)
    adjacency = squareform(weights)
    plt.hist(weights)
    plt.title('Distribution of weights')
    plt.show()

    
    #remove some edges by changing the value here    
    adjacency[adjacency <0.85]=0 
    np.fill_diagonal(adjacency, 0)
    n_edges=int(np.count_nonzero(adjacency)/2)
    
    logging.info(f'The number of edges is : {n_edges}')
    logging.info(f'Adjacency done !');

    return (adjacency,movies_filtered_by_budget, movies_genres_id)


def make_features_based_adjacency(movies,list_of_genres_id):
    #Fonction supplémentaire pour tester différents graphs
    import json
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import queue as Q # Package used to manage queues
    import logging
    from scipy.spatial.distance import pdist, squareform

    #(movies, people) = load_dataframes();

    budgets = movies['budget'].copy()
    
    #CHANGE FEATURES HERE
    features= movies.loc[:, ['budget', 'revenue']]
    features_filtered=features[(features != 0).all(1)]
    
    budget_max = budgets.max();

    logging.info(f'The budget max = {budget_max}');

    budgets_filtered = budgets[budgets != 0];

    logging.info(budgets_filtered.head())

    budgets_filtered.to_csv('./data/budgets.csv');

    n_nodes=len(budgets_filtered)
    
    logging.info(f'The number of nodes is : {n_nodes}')
    
    movies_filtered_by_budget=movies.loc[features_filtered.index]
    
    movies_genres_id = movies_filtered_by_budget['genres'].copy()

    adjacency = np.zeros((n_nodes, n_nodes), dtype=float)  
    
    #version julien avec norm euclidienne
    distances = pdist(features_filtered, metric='euclidean')
    kernel_width = distances.mean()
    weights = np.exp(-distances**2 / kernel_width**2)
    adjacency = squareform(weights)
    plt.hist(weights)
    plt.title('Distribution of weights')
    plt.show()

    
    #remove some edges by changing the value here    
    adjacency[adjacency <0.85]=0 
    np.fill_diagonal(adjacency, 0)
    n_edges=int(np.count_nonzero(adjacency)/2)
    
    logging.info(f'The number of edges is : {n_edges}')
    logging.info(f'Adjacency done !');

    return (adjacency,movies_filtered_by_budget, movies_genres_id)



def filter_movies_by_years(movies, startdate, enddate):
    #DECADE SELECTION
    #Select the decade that you want to keep
    #startdate = pd.to_datetime("2010-01-01").date()
    #enddate = pd.to_datetime("2020-01-01").date()
    movies=movies[(movies['release_date'] > startdate) & (movies['release_date'] <enddate)]
    
    return movies