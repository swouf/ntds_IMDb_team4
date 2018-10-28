import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json

import connected_graph as cg

adjacency = np.load('../data/adjacency.npy')

connected = cg.connected_graph(adjacency)

print("The graph is connected : ", connected)
