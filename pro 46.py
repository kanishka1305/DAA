import heapq
def dijkstra(n, edges, source, target):
    graph = {i: [] for i in range(n)}
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))  
    min_heap = [(0, source)]
    distances = {i: float('inf') for i in range(n)}
    distances[source] = 0
    while min_heap:
        current_distance, current_vertex = heapq.heappop(min_heap)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(min_heap, (distance, neighbor))
    return distances[target]
n = 6
edges = [(0, 1, 7), (0, 2, 9), (0, 5, 14), (1, 2, 10), (1, 3, 15),
         (2, 3, 11), (2, 5, 2), (3, 4, 6), (4, 5, 9)]
source = 0
target = 4
output = dijkstra(n, edges, source, target)
print(output) 
