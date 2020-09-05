from Representation.Graph import Graph
from collections import defaultdict
import math


class BellmanFord:

    def __init__(self, graph):
        self.vertex_distance = {}
        self.vertex_parent = {}
        self.graph = graph
        # initialize vertex distance and parent with infinity and None respectively
        for g in graph.graph_adjacencylist:
            self.vertex_distance[g] = math.inf
            self.vertex_parent[g] = None

    # relax edge and return 1 if relaxation happens else return 0
    def relax(self, u, v):
        if self.vertex_distance[v] > self.vertex_distance[u] + self.graph.edge_weight(u, v):
            self.vertex_distance[v] = self.vertex_distance[u] + self.graph.edge_weight(u, v)
            self.vertex_parent[v] = u
            return 1
        return 0

    def singleSourceShortestPath(self, source):
        self.vertex_distance[source] = 0
        self.vertex_parent[source] = None
        for i in range(len(self.graph.edges) - 1):
            for edge in self.graph.edges:
                u, v = edge
                res = self.relax(u, v)

        for edge in self.graph.edges:
            u, v = edge
            res = self.relax(u, v)
            if res == 1:
                raise RuntimeError("Graph contains Negative cycle")
        return self.vertex_distance


if __name__ == "__main__":
    graph = Graph(True, True)
    # graph.add_edge(0, 3, 6)
    # graph.add_edge(0, 1, 4)
    # graph.add_edge(0, 2, 5)
    # graph.add_edge(1, 2, -3)
    # graph.add_edge(2, 4, 4)
    # graph.add_edge(3, 4, 2)
    # graph.add_edge(4, 3, 1)
    graph.add_edge(0, 1, 1)
    graph.add_edge(1, 3, 2)
    graph.add_edge(2, 3, 2)
    graph.add_edge(3, 1, -6)
    # print(graph.graph)
    # print(graph.get_edges())
    # print(graph.edge_weights)

    bellman_ford = BellmanFord(graph)
    print(bellman_ford.singleSourceShortestPath(0))
    print(bellman_ford.vertex_parent)