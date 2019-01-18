# ntds_IMDb_team4

## Structure of the repository

+ [/](./): contains the notebooks, this README and a compressed copy of the adjacency matrix ([adjacency.zip](./adjacency.zip)).
+ [data/](./data/): Contains the data necessary for the project, such as .csv files and numpy arrays.
+ [milestones/](./milestones/): Contains the 4 milestone notebooks that were written during the semester.
+ [pictures/](./pictures/): Contains figures that were exported from our different notebooks.
+ [src/](./src/): Contains the python code we wrote during the milestones to manipulate our data.


### Notebook

The main code is in the jupyter notebook [final_project_ntds_2018.ipynb](./final_project_ntds_2018.ipynb).


### Python scripts

A few functions were developped in their own function file. These functions can be found in the folder [src](./src/).

A few test scripts were also developped. To launch one of these script, from the root folder folder, use the following command : `python ./src/[name of test script]`


+ `python ./src/connected_graph_test.py`
+ `python ./src/shortest_path_lengths_test.py`
+ `python ./src/network_properties.py` but for this last one, make sure that the adjacency matrix is in the [data](./data) folder under the name `adjacency.npy`
+ `python ./src/compute_diameter_test.py`
