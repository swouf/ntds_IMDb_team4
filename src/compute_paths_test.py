import unittest
import numpy as np
import compute_paths as cp
import logging

class TestComputePaths(unittest.TestCase):

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

        nbOfPaths = cp.compute_paths(adjacency, 4, 1, 4)
        logging.info(f'Number of paths of length 4 between node 4 and 1 : {nbOfPaths}')

        self.assertEqual(nbOfPaths,4)

    def test_2(self):
        logging.basicConfig(level=logging.DEBUG)
        adjacency = np.array([[0,1,1,0,0,0],
                    [1,0,0,1,0,1],
                    [1,0,0,0,0,0],
                    [0,1,0,0,1,0],
                    [0,0,0,1,0,0],
                    [0,1,0,0,0,0]], np.int32)

        nbOfPaths = cp.compute_paths(adjacency, 1, 1, 4)
        logging.info(f'Number of paths of length 4 between node 1 and 1 : {nbOfPaths}')

        self.assertEqual(nbOfPaths,0)

    def test_3(self):
        logging.basicConfig(level=logging.DEBUG)
        adjacency = np.array([[0,1,1,0,0,0],
                    [1,0,0,1,0,1],
                    [1,0,0,0,0,0],
                    [0,1,0,0,1,0],
                    [0,0,0,1,0,0],
                    [0,1,0,0,0,0]], np.int32)

        nbOfPaths = cp.compute_paths(adjacency, 2, 4, 4)
        logging.info(f'Number of paths of length 4 between node 2 and 4 : {nbOfPaths}')

        self.assertEqual(nbOfPaths,1)

    def test_original_graph_1(self):
        logging.basicConfig(level=logging.DEBUG)
        adjacency = np.load("./data/adjacency.npy")

        self.assertEqual(10,10)

    def test_original_graph_2(self):
        logging.basicConfig(level=logging.DEBUG)
        adjacency = np.load("./data/adjacency.npy")

        self.assertEqual(10,10)

if __name__ == '__main__':
    unittest.main()
