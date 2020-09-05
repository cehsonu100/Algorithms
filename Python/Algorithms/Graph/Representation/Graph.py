""""
use adjacency list to represent the graph
e.g.
{a: [b, e]}
{b: [f, c]}
{e: [g, a, j, r]}
above: dictionary key represent the vertex and its values represent the vertices that are connected with dictionary's key vertex
"""

from collections import defaultdict
import math
import matplotlib.pyplot as plt
import networkx as nx


class Graph:

    # Constructor => can take 2 argument
    # 1. is_directed_graph
    # 2. is_weighted_graph
    # if not passed any parameter, then it will that that value as False by default
    def __init__(self, is_directed_graph=False, is_weighted_graph=False):
        self.is_weighted_graph = is_weighted_graph
        self.is_directed_graph = is_directed_graph
        self.graph_adjacencylist = defaultdict(list)
        #  temp = {"a": ["b", "c", "d"] , "d":[1, 7, 8, 'a'],  "b": ["a"]}

        self.edges = []
        self.edge_weights = {}

    # Add edge in graph
    # if graph is undirected graph, add 1 more edges from destination to source also
    # if graph is weighted graph, add weight associated with that edge
    def add_edge(self, u, v, w=math.inf):
        self.graph_adjacencylist[u].append(v)
        if not self.is_directed_graph:
            self.graph_adjacencylist[v].append(u)
        edges = (u, v)
        self.edges.append(edges)  # adding this to use in draw_graph() method
        if self.is_weighted_graph:
            self.edge_weights[(u, v)] = w

    # Get weight of edge
    # Raise error if edge not found in graph
    def edge_weight(self, u, v):
        if (u, v) not in self.edge_weights:
            raise RuntimeError('Given edge is not present in graph.')
        return self.edge_weights[(u, v)]

    # Get already added edge list in graph
    # It will not include the weight of the edge
    def get_edges(self):
        edges = []
        for node in self.graph_adjacencylist:
            for neighbour in self.graph_adjacencylist[node]:
                edges.append((node, neighbour))
        return edges

    # Draw the graph using networkx and matplotlib lib
    def draw_graph(self):
        G = nx.Graph()
        G.add_edges_from(self.edges)
        nx.draw(G, with_labels=True)
        plt.savefig("graph.png")  # save as png
        plt.show()  # display


if __name__ == "__main__":
    graph = Graph()
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(4, 1)
    graph.add_edge(4, 3)
    graph.add_edge(1, 3)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    # graph.add_edge('Hyderabad', 'Goa')
    # graph.add_edge('J&K', 'UK')
    # graph.add_edge('UK', 'Norway')
    # graph.add_edge('Kota', 'Ahamadabad')
    # graph.add_edge('New York', 'Silicon Valley')
    # graph.add_edge('New York', 'Canada')
    # graph.add_edge('Times Square', 'Time Square')
    print(graph.graph_adjacencylist)
    print(graph.get_edges())
    # print(graph.edge_weights)
    # print(graph.get_edge_weight('Bangalore','Hyderabad'))
    graph.draw_graph()

if __name__ == "__main__":
    graph = Graph(False, True)
    graph.add_edge('Bangalore', 'Hyderabad', 67)
    graph.add_edge('Bangalore', 'New York', 78)
    graph.add_edge('Delhi', 'Kota', 106)
    graph.add_edge('Hyderabad', 'Goa', 34)
    graph.add_edge('J&K', 'UK', 300)
    graph.add_edge('UK', 'Norway', 570)
    graph.add_edge('Kota', 'Ahamadabad', 10)
    graph.add_edge('New York', 'Silicon Valley', 40)
    graph.add_edge('New York', 'Canada', 140)
    graph.add_edge('Times Square', 'Time Square', 0)
    print(graph.graph_adjacencylist)
    print(graph.get_edges())
    print(graph.edge_weights)
    print(graph.get_edge_weight('Bangalore','Hyderabad'))
    graph.draw_graph()
#
#
# # with open("web-Google.txt") as file:
# #     for line in file:
# #         if '#' in line:
# #             continue
# #         edge = [int(x) for x in  line.strip().split("\t")]
# #         graph.add_edge(edge[0], edge[1])
# #         print(graph.graph[edge[0]])
# #
# # print(graph.graph)
# # graph.draw_graph()
# # print(graph.get_edges())
