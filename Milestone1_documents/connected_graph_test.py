import unittest
import numpy as np
import connected_graph as cg

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
        self.assertEqual(cg.connected_graph(adjacency), True)

    def test_2(self):
        adjacency = np.array([[0,1,1,0,0,0],
                    [1,0,0,1,0,1],
                    [1,0,0,0,0,0],
                    [0,1,0,0,1,0],
                    [0,0,0,1,0,0],
                    [0,1,0,0,0,0]], np.int32)
        a = cg.breadth_first_search(adjacency, 2,4)
        print("distance between nodes 2 and 4 : ", a)
        self.assertEqual(a, 4)

    def test_3(self):
        adjacency = np.array([[0,1,1,0,0,0],
                    [1,0,0,1,0,1],
                    [1,0,0,0,0,0],
                    [0,1,0,0,1,0],
                    [0,0,0,1,0,0],
                    [0,1,0,0,0,0]], np.int32)
        a = cg.breadth_first_search(adjacency, 4,5)
        print("distance between nodes 2 and 4 : ", a)
        self.assertEqual(a, 3)

    def test_4(self):
        adjacency = np.array([[0,1,1,0,0,0],
                    [1,0,0,1,0,1],
                    [1,0,0,0,0,0],
                    [0,1,0,0,1,0],
                    [0,0,0,1,0,0],
                    [0,1,0,0,0,0]], np.int32)
        a = cg.breadth_first_search(adjacency, 2,2)
        print("distance between nodes 2 and 4 : ", a)
        self.assertEqual(a, 0)

if __name__ == '__main__':
    unittest.main()
