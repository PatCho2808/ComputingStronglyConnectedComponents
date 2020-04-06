from unittest import TestCase
from Graph import *


class TestGraph(TestCase):
    def test_create_graph(self):
        graph = Graph([[1, 2],
                       [2, 3]])

        self.assertEqual([graph.get_vertex(2)], graph.get_vertex(1).get_next_vertices())
        self.assertEqual([graph.get_vertex(3)], graph.get_vertex(2).get_next_vertices())
        self.assertEqual([], graph.get_vertex(3).get_next_vertices())

        graph = Graph([[1, 2],
                       [2, 3],
                       [3, 1]])

        self.assertEqual([graph.get_vertex(2)], graph.get_vertex(1).get_next_vertices())
        self.assertEqual([graph.get_vertex(3)], graph.get_vertex(2).get_next_vertices())
        self.assertEqual([graph.get_vertex(1)], graph.get_vertex(3).get_next_vertices())

        graph = Graph([[1, 2],
                       [1, 3],
                       [2, 3],
                       [3, 1]])

        self.assertEqual([graph.get_vertex(2), graph.get_vertex(3)], graph.get_vertex(1).get_next_vertices())
        self.assertEqual([graph.get_vertex(3)], graph.get_vertex(2).get_next_vertices())
        self.assertEqual([graph.get_vertex(1)], graph.get_vertex(3).get_next_vertices())


    def test_reverse_graph(self):

        graph = Graph([[1, 2],
                       [2, 3]])

        graph.reverse()

        self.assertEqual([graph.get_vertex(1)], graph.get_vertex(2).get_next_vertices())
        self.assertEqual([graph.get_vertex(2)], graph.get_vertex(3).get_next_vertices())




