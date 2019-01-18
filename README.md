ntds_IMDb_team4
================================================================================

![License : MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)
![version : alpha](https://img.shields.io/badge/version-final-blue.svg)

## Structure of the repository

+ [/](./): contains the final notebook, this README and the different folders.
+ [data/](./data/): Contains the data necessary for the project, such as .csv files and numpy arrays.
+ [milestones/](./milestones/): Contains the 4 milestone notebooks that were written during the semester.
+ [pictures/](./pictures/): Contains figures that were exported from our different notebooks.
+ [src/](./src/): Contains the python codes we wrote during the milestones to manipulate our data, such as scripts and functions.


### Notebook

The main code is in the jupyter notebook [final_project_ntds_2018.ipynb](./final_project_ntds_2018.ipynb).


### Python functions

A few functions were developped in their own function file. These functions can be found in the folder [src](./src/). The most important ones are the following:

+ [load_data](./src/load_data.py`) contains multiple functions used to clean the initial dataset, create features dataframes and adjacency matrices. 
+ [genre_graph](./src/genre_graph.py`) contains functions used to create graphs based on the genres of the movies.
+ [test_success](./src/test_success.py`) contains functions that reorder adjacency matrices based on kmeans results.
