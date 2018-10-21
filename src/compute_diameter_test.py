import unittest
import numpy as np
import compute_diameter as cd
import logging

class TestComputeDiameter(unittest.TestCase):

    def setUp(self):
        pass

    def test_1(self):
        logging.basicConfig(level=logging.DEBUG)
        adjacency = np.array([[0,1,1,0,0,0],
                    [1,0,0,1,0,1],
                    [1,0,0,0,0,0],
                    [0,1,0,0,1,0],
                    [0,0,0,1,0,0],
                    [0,1,0,0,0,0]], np.int32)

        self.assertEqual(cd.compute_diameter(adjacency),4)

    def test_original_graph(self):
        adjacency = np.load("./data/adjacency.npy")

        diameter = cd.compute_diameter(adjacency)

        print("Final diameter found ! Diameter = ", diameter)

        self.assertEqual(diameter,10)

    def test_original_graph_100_samples(self):
        adjacency = np.load("./data/adjacency.npy")

        diameter = cd.compute_diameter(adjacency, 100)

        print("Final diameter found ! Diameter = ", diameter)

        self.assertEqual(diameter,10)

if __name__ == '__main__':
    unittest.main()
