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

    return (movies, people)

def make_budget_based_adjacency(movies):

    import json
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import queue as Q # Package used to manage queues
    import logging

    #(movies, people) = load_dataframes();

    budgets = movies['budget'].copy()

    budget_max = budgets.max();

    logging.info(f'The budget max = {budget_max}');

    budgets_filtered = budgets[budgets != 0];

    logging.info(budgets_filtered.head())

    budgets_filtered.to_csv('./data/budgets.csv');

    n_nodes=len(budgets_filtered)

    movies_filtered_by_budget = movies.iloc[budgets_filtered.index]

    #Create a matrix of 0 of size (the number of nodes)
    adjacency = np.zeros((n_nodes, n_nodes), dtype=float)

    k = 0
    for movieBudget in enumerate(budgets_filtered):
        b = budgets_filtered.copy()
        b = b.apply(lambda x: budget_max-abs(x-movieBudget[1]))
        adjacency[:,k] = b.values;
        k += 1

    np.fill_diagonal(adjacency, 0)

    logging.info(f'Adjacency done !');

    return (adjacency,movies_filtered_by_budget)
