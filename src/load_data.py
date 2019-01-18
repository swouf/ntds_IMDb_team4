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
    #########################################################################################################################
    #########################################################################################################################
    
    #expending the genre JSON column and keeping only the first 1
    genre = []
    movies.genres.apply(lambda x: genre.extend(x))
    genre = pd.DataFrame(genre)
    genre['type'] = 'genre'
    genre=genre.drop_duplicates('id')
    genre['index']=genre['id']
    genre=genre.set_index('id') 
    
    genre_names=genre['name'].copy()
    
    #transform the name of the genre into numbers to assign a specific ID to each genre
    factorized_names = pd.factorize(genre_names)[0]
    movies['genres']=factorized_names
    movies['genres_names']=genre_names
    
    
    #Removing movies with no information about budget or revenue
    features_filter= movies.loc[:, ['budget', 'revenue']]
    new_features=features_filter[(features_filter != 0).all(1)] 
    movies_filtered_by_features=movies.loc[new_features.index]
    movies=movies_filtered_by_features

    
    #add the return on investment in the movies dataframe
    budget=movies['budget']
    revenue=movies['revenue']
    ROI=(revenue-budget)
    ROI=ROI.divide(budget)
    movies['ROI']=ROI
    
    #add the success indicator of the movie (value of 1 if the ROI is above a threshold and 0 otherwise)
    success=ROI
    threshold_success=0.5
    success[success<threshold_success]=0
    success[success>=threshold_success]=1
    movies['success']=success
    
    #Create the people dataframe using the cast and the crew
    cast = []
    credits.cast.apply(lambda x: cast.extend(x))
    cast = pd.DataFrame(cast)
    cast['type'] = 'cast'
    
    crew = []
    credits.crew.apply(lambda x: crew.extend(x))
    crew = pd.DataFrame(crew)
    crew['type'] = 'crew'
    people = pd.concat([cast, crew],  ignore_index=True, sort=False)
    
    people=people.loc[people['movie_id'].isin(movies.index)]
    
    logging.info("Data loaded !");

    return (movies, people)

def make_budget_based_adjacency(movies):
    #Ma version (julien), utilise le budget, mais aussi le revenu, et fait la norme euclidienne entre les points.
    import json
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import queue as Q # Package used to manage queues
    import logging
    from scipy.spatial.distance import pdist, squareform


    budgets = movies['budget'].copy()
    budget_max = budgets.max();
    
    #Use the euclidean norm on the budget and the genres to build the adjacency
    features= movies.loc[:, ['budget', 'revenue']]
    features_filtered=features[(features != 0).all(1)]

    movies_filtered_by_budget=movies.loc[features_filtered.index]
    n_nodes=movies_filtered_by_budget.shape[0]
    
    #creation of the adjacency matrix
    adjacency = np.zeros((n_nodes, n_nodes), dtype=float)
    distances = pdist(features_filtered, metric='euclidean')
    kernel_width = distances.mean()
    weights = np.exp(-distances**2 / kernel_width**2)
    adjacency = squareform(weights)
    
    #plot the weight histogram
    plt.hist(weights, bins = 30)
    plt.xlabel('Weights')
    plt.ylabel('Occurence')
    plt.title('Weights distribution')
    plt.show()
    
    #remove some edges by selecting the threshold here 
    adjacency[adjacency <0.90]=0 
    np.fill_diagonal(adjacency, 0)
    n_edges=int(np.count_nonzero(adjacency)/2)
    
    return (adjacency,movies_filtered_by_budget)

def filter_movies_window_years(movies,startyear, endyear):
    import pandas as pd
    #decade = 1960 + i*10
    #decadeEnd = decade + 10
    moviesFilteredByYears = filter_movies_by_years(movies, pd.to_datetime(f'{startyear}-01-01').date(), pd.to_datetime(f'{endyear}-01-01').date())
    return moviesFilteredByYears

def filter_movies_by_years(movies, startdate, enddate):

    movies=movies[(movies['release_date'] > startdate) & (movies['release_date'] <enddate)]
    
    return movies

#loads the feature dataframe, removes useless columns and transpose it.
def load_features():

    import json
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import queue as Q # Package used to manage queues
    import logging
    
    #select the type of
    features = pd.read_csv('./data/test_actors_crew.csv')
    features = features.drop(features.columns[0],axis=1)
    features = features.drop(columns=['name'],axis=1)
    #drop useless columns
    features=features.drop(features.iloc[:, 0:2], axis=1)
    
    #transpose to get adjacency of movies
    features_transposed=features.transpose()
    
    return features_transposed

#Uses the clean feature dataframe from the load_features() function to create the adjacency matrix
def make_adjacency_from_feature_matrix(features):
    import json
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import queue as Q # Package used to manage queues
    import logging  
    
    #We calculate the number of nodes   
    n_nodes=len(features)
    
    #Create a matrix of 0 of size equal to the number of nodes
    adjacency = np.zeros((n_nodes, n_nodes), dtype=int)
    
    for idx_mul in range(n_nodes):
        tmp=features.multiply(features.iloc[idx_mul])
        #On each row of the adjacency matrix, sum all the values of this temporary array
        adjacency[idx_mul]=tmp.sum(axis=1)
    
    #fill the diagonal of the matrix with zeroes
    np.fill_diagonal(adjacency, 0)
    
    #save the adjacency for later use
    np.save('./data/adjacency_actors_crew.npy', adjacency);
    
    #We connect movies if they have at least 2 poeple in common
    adjacency[adjacency <2]=0
    return adjacency


#This function is used to create the feature matrix that connects people and movies
def create_features(movies,people):
    import json
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import queue as Q # Package used to manage queues
    import logging
    
    people = people.drop(columns=['gender', 'credit_id','cast_id','order','character','type'])
    people = people.sort_values(by='id')

    #removing the rows with similar person and ID (For example if someone played 2 different roles in a movie we only keep one of these entries)
    people=people.drop_duplicates(subset=['id', 'movie_id'])

    #get the number of movie that each person worked on
    table_nb_movies=people['id'].value_counts()

    movies['movie_id']=movies['id']
    
    #remove the columns that are not usefull
    movies=movies.drop(columns=['vote_count','budget','genres','homepage','keywords','original_language','overview','popularity','production_companies','production_countries','revenue','runtime','spoken_languages','status','tagline','original_title','ROI','success'])
    movies=movies.set_index('movie_id') 

    #merge the movies and the people so that we can get the rating of each movie 
    people = people.merge(movies, on='movie_id')
    unique_values=people['id_x'].unique()
    unique_values.sort()
    people['id']=people['id_x']
    people = people.drop(columns=['id_x','id_y','release_date','department','job'])

    #simple_list will contain all the different actor names, this will be the column of our features
    simple_list=people.loc[:, ['id','movie_id','name']]
    simple_list=simple_list.sort_values(by='id')
    simple_list=simple_list.drop_duplicates('id')
    simple_list=simple_list.set_index('id') 
    simple_list=simple_list.drop(columns=['movie_id'])

    #only take people that worked on at least 5 movies
    threshold_movies=5
    for idx in unique_values:
        nb_films=table_nb_movies[idx] 
        if (nb_films)<threshold_movies:
            simple_list=simple_list.drop(index=idx)
            
    #save the dataframe to        
    simple_list.to_csv('./data/test_actors_crew.csv', sep=','); 
    simple_list = pd.read_csv('./data/test_actors_crew.csv') 

    #Add a column that will contain the average rating of the actor 
    simple_list['Average_Rating']=np.nan

    new_movie_index=movies['id']
    for i in new_movie_index:
        simple_list['Movie_ID_%d' % i]=0

    unique_id=simple_list['id'].unique()
    unique_id.sort()
    index_ini=0

    for idx in unique_id:
        rating_average=1
        subset=people[people['id'] == idx]
        new_index_subset = pd.Series(range(0,len(subset)))
        subset=subset.set_index(new_index_subset) 
        index_person=subset.iloc[0,5]

        for i in new_index_subset:
            index_film=subset.iloc[i,0] 
            simple_list.loc[index_ini, 'Movie_ID_%d' % index_film]=1
            rating_average=rating_average+subset.iloc[i,3]    
        np.seterr(divide='ignore', invalid='ignore')

        #place the average rating of the person
        rating_average=rating_average/len(subset)
        simple_list.iloc[index_ini, 2]=rating_average    
        index_ini=index_ini+1 
    
    #save the dataframe to reload it quickyl later
    simple_list.to_csv('./data/test_actors_crew.csv', sep=','); 
    features = pd.read_csv('./data/test_actors_crew.csv')
    features = features.drop(features.columns[0],axis=1)
    
    return features