ntds_IMDb_team4
================================================================================

![License : MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)
![version : alpha](https://img.shields.io/badge/version-alpha-blue.svg)


## Structure of the repository

+ [/](./): contains the notebooks, this README and a compressed copy of the adjacency matrix ([adjacency.zip](./adjacency.zip)).
+ [data/](./data/): Contains the data necessary for the project.
+ [src/](./src/): Contains the python code we wrote during the milestones and final part to manipulate our data.

## Milestone 1

### Notebook

For the first milestone, the main code is in the jupyter notebook [1_network_properties.ipynb](./1_network_properties.ipynb)

Use the following command to launch it : `jupyter notebook 1_network_properties.ipynb`

### Python scripts

A few functions were developped in their own function file. These functions can be found in the folder [src](./src/).

A few test scripts were also developped. To launch one of these script, from the root folder folder, use the following command : `python ./src/[name of test script]`


+ `python ./src/connected_graph_test.py`
+ `python ./src/shortest_path_lengths_test.py`
+ `python ./src/network_properties.py` but for this last one, make sure that the adjacency matrix is in the [data](./data) folder under the name `adjacency.npy`
+ `python ./src/compute_diameter_test.py`

## Milestone 2

The purpose of this milestone is to explore various random network models, analyse their properties and compare them to your network. In the first part of the milestone you will implement two random graph models and try to fit them to your network. In this part you are not allowed to use any additional package. In the second part of the milestone you will choose a third random graph model that you think shares some properties with your network. You will be allowed to use additional packages to construct this network, but you must explain your network choice. Finally, make your code as clean as possible, and keep your textual answers short.
