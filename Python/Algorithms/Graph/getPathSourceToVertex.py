from Representation.Graph import Graph


# def get_path(graph, source, destination, path, visited):
#     visited.append(source)
#     if source == destination:
#         return
#     for node in graph[source]:
def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath
            return None


graph = Graph()
graph.add_edge('Bangalore', 'Hyderabad')
graph.add_edge('Bangalore', 'New York')
graph.add_edge('Delhi', 'Kota')
graph.add_edge('Hyderabad', 'Goa')
graph.add_edge('J&K', 'UK')
graph.add_edge('UK', 'Norway')
graph.add_edge('Kota', 'Ahamadabad')
graph.add_edge('New York', 'Silicon Valley')
graph.add_edge('New York', 'Canada')
graph.add_edge('Times Square', 'Time Square')
print(find_path(graph.graph, 'Bangalore', 'New York'))
# path = []
# visited = []
# with open("web-Google.txt") as file:
#     for line in file:
#         if '#' in line:
#             continue
#         edge = [int(x) for x in line.strip().split("\t")]
#         graph.add_edge(edge[0], edge[1])
#         print(graph.graph[edge[0]])
# print(find_path(graph.graph, 756512, 616250))
