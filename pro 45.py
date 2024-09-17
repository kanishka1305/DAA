import sys
def dijkstra(graph, source):
    n = len(graph)
    distances = [sys.maxsize] * n
    distances[source] = 0
    visited = [False] * n
    for _ in range(n):
        min_distance = sys.maxsize
        min_index = -1
        for v in range(n):
            if not visited[v] and distances[v] < min_distance:
                min_distance = distances[v]
                min_index = v
        visited[min_index] = True
        for v in range(n):
            if (not visited[v] and 
                graph[min_index][v] != sys.maxsize and 
                distances[min_index] + graph[min_index][v] < distances[v]):
                distances[v] = distances[min_index] + graph[min_index][v]
    return distances
n = 5
graph = [[0, 10, 3, sys.maxsize, sys.maxsize],
         [sys.maxsize, 0, 1, 2, sys.maxsize],
         [sys.maxsize, 4, 0, 8, 2],
         [sys.maxsize, sys.maxsize, sys.maxsize, 0, 7],
         [sys.maxsize, sys.maxsize, sys.maxsize, 9, 0]]
source = 0
output = dijkstra(graph, source)
print(output) 
