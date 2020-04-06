from Graph import *


class ComputeStronglyConnectedComponents:
    def __init__(self, graph):
        self.graph = graph
        self.finishing_time = 0
        self.leading_node = None

    def compute(self):
        self.finishing_time = 0
        self.leading_node = None
        self.graph.reverse()
        self.dfs_finishing_times_loop()
        self.graph.reverse()
        # DFS_loop(graph)
        return 0

    def dfs_finishing_times_loop(self):
        return {}

    def dfs_finishing_times(self):
        return 0