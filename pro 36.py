from collections import defaultdict
import sys
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    def is_safe(self, v, color, c):
        for i in self.graph[v]:
            if color[i] == c:
                return False
        return True
    def graph_coloring_util(self, m, color, v):
        if v == self.V:
            return True
        for c in range(1, m + 1):
            if self.is_safe(v, color, c):
                color[v] = c
                if self.graph_coloring_util(m, color, v + 1):
                    return True
                color[v] = 0
        return False
    def graph_coloring(self, m):
        color = [0] * self.V
        if not self.graph_coloring_util(m, color, 0):
            return False
        return color
def max_colored_regions(n, edges):
    g = Graph(n)
    for u, v in edges:
        g.add_edge(u, v)
    m = 3  
    color = g.graph_coloring(m)
    return color.count(0)
n = 5
edges = [[0, 1], [0, 4], [1, 2], [1, 4], [2, 3], [3, 4]]
print(max_colored_regions(n, edges))
def shortest_path(graph, start, end):
    distances = {vertex: sys.maxsize for vertex in graph}
    distances[start] = 0
    visited = set()
    while visited != set(graph):
        min_vertex = min((vertex for vertex in graph if vertex not in visited), key=lambda vertex: distances[vertex])
        visited.add(min_vertex)
        for neighbor, weight in graph[min_vertex].items():
            if neighbor not in visited:
                new_distance = distances[min_vertex] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
    return distances[end]
graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 7},
    'C': {'A': 3, 'B': 7, 'D': 1},
    'D': {'A': 6, 'C': 1}
}
                  print(shortest_path(graph, 'C', 'A'))
