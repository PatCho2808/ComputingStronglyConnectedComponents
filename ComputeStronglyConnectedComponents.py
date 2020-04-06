from Graph import *


class ComputeStronglyConnectedComponents:
    def __init__(self, graph):
        self.graph = graph
        self.finishing_time = 0
        self.leading_node = None
        self.leaders = {}
        self.finishing_times = {}
        self.number_of_components = 0

    def compute(self):
        self.finishing_time = 0
        self.leading_node = None
        self.graph.reverse()
        self.dfs_finishing_times_loop()
        self.graph.reverse()
        # DFS_loop(graph)
        return 0

    def dfs_finishing_times_loop(self):
        for i in range(self.graph.get_number_of_vertices(), 0, -1):
            vertex = self.graph.get_vertex(i)
            if not vertex.get_is_explored():
                self.leading_node = vertex
                self.dfs_finishing_times(vertex)
        return self.finishing_times

    def dfs_finishing_times(self, vertex):
        vertex.set_as_explored()
        self.leaders[vertex] = self.leading_node
        for next_vertex in vertex.get_next_vertices():
            if not next_vertex.get_is_explored():
                self.dfs_finishing_times(next_vertex)
        self.finishing_time = self.finishing_time + 1
        self.finishing_times[self.finishing_time] = vertex

    def dfs_compute_components_loop(self):
        for i in range(len(self.finishing_times), 0, -1):
            vertex = self.finishing_times
