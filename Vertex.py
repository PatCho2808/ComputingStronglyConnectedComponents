class Vertex:
    def __init__(self, number):
        self.number = number
        self.edges = []
        self.explored = False

    def get_number(self):
        return self.number

    def add_edge(self, edge):
        self.edges.append(edge)

    def get_next_vertices(self):
        next_vertices = []
        for edge in self.edges:
            next_vertex = edge.get_head()
            if next_vertex != self:
                next_vertices.append(next_vertex)
        return next_vertices

    def get_edges(self):
        return self.edges



