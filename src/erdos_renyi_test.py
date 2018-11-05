import unittest
import numpy as np
import matplotlib.pyplot as plt
import erdos_renyi as er
import logging

class TestComputeDiameter(unittest.TestCase):

    def setUp(self):
        pass

    def test_1(self):
        logging.basicConfig(level=logging.INFO)
        adjacency = er.erdos_renyi(100,0.6);

        self.assertEqual(adjacency.shape,(100,100))

    def test_2(self):
        adjacency = er.erdos_renyi(200,0.98);

        plt.figure(figsize=(10, 10))
        plt.spy(adjacency, markersize=0.1)
        plt.title('adjacency matrix')
        plt.show();

        self.assertEqual(adjacency.shape,(200,200))

    def test_3(self):
        adjacency = er.erdos_renyi(9628,0.01);

        plt.figure(figsize=(10, 10))
        plt.spy(adjacency, markersize=0.1)
        plt.title('adjacency matrix')
        plt.show()

        self.assertEqual(adjacency.shape,(9628,9628))

if __name__ == '__main__':
    unittest.main()
