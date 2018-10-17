import unittest
import numpy as np
import shortest_path_lengths as spl

class TestConnectedGraph(unittest.TestCase):

    def setUp(self):
        pass

    def test_1(self):
        adjacency = np.array([[0,1,1,0,0,0],
                    [1,0,0,1,0,1],
                    [1,0,0,0,0,0],
                    [0,1,0,0,1,0],
                    [0,0,0,1,0,0],
                    [0,1,0,0,0,0]], np.int32)
        paths_length = np.array([0,1,1,2,3,2])
        self.assertEqual(spl.compute_shortest_path_lengths(adjacency,0), paths_length)

if __name__ == '__main__':
    unittest.main()
