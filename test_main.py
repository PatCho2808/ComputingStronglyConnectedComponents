from unittest import TestCase
from main import *


class TestComputeNumberOfStronglyConnectedComponents(TestCase):
    def test_compute_number_of_strongly_connected_components(self):
        graph = Graph([[1, 2],
                       [2, 3],
                       [3, 1],
                       [2, 11],
                       [11, 10],
                       [11, 9],
                       [9, 10],
                       [10, 8],
                       [5, 9],
                       [6, 8],
                       [5, 6],
                       [6, 7],
                       [5, 7],
                       [7, 4],
                       [4, 5],
                       [3, 4],
                       [3, 5]])

        self.assertEqual(4, compute_number_of_strongly_connected_components(graph))

        graph = Graph([[2, 3],
                       [1, 2],
                       [3, 1],
                       [6, 3],
                       [6, 4],
                       [4, 5],
                       [5, 6],
                       [7, 5],
                       [9, 7],
                       [7, 8],
                       [8, 9]])

        self.assertEqual(3, compute_number_of_strongly_connected_components(graph))