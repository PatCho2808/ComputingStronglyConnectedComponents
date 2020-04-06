from unittest import TestCase
from ComputeStronglyConnectedComponents import *


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

        compute_components = ComputeStronglyConnectedComponents(graph)

        self.assertEqual(4, compute_components.compute())

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

        compute_components = ComputeStronglyConnectedComponents(graph)

        self.assertEqual(3, compute_components.compute())


class TestComputeFinishingTimes(TestCase):
    def test_compute_finishing_times_loop(self):
        graph = Graph([[1, 4],
                       [4, 6],
                       [6, 5],
                       [5, 4],
                       [1, 2],
                       [2, 3],
                       [3, 1]])

        compute_components = ComputeStronglyConnectedComponents(graph)
        finishing_times = compute_components.dfs_finishing_times_loop()
        print(finishing_times)

        self.assertEqual(5, finishing_times[graph.get_vertex(1)])
        self.assertEqual(4, finishing_times[graph.get_vertex(2)])
        self.assertEqual(6, finishing_times[graph.get_vertex(3)])
        self.assertEqual(1, finishing_times[graph.get_vertex(4)])
        self.assertEqual(2, finishing_times[graph.get_vertex(5)])
        self.assertEqual(3, finishing_times[graph.get_vertex(6)])

        graph = Graph([[1, 3],
                       [1, 4],
                       [3, 2]])

        compute_components = ComputeStronglyConnectedComponents(graph)
        finishing_times = compute_components.dfs_finishing_times_loop()

        self.assertEqual(4, finishing_times[graph.get_vertex(1)])
        self.assertEqual(2, finishing_times[graph.get_vertex(2)])
        self.assertEqual(3, finishing_times[graph.get_vertex(3)])
        self.assertEqual(1, finishing_times[graph.get_vertex(4)])

