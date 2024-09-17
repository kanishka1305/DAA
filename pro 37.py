import numpy as np
def floyd_warshall(n, edges):
    dist = np.full((n, n), float('inf'))
    for i in range(n):
        dist[i][i] = 0
    for u, v, w in edges:
        dist[u][v] = min(dist[u][v], w)
        dist[v][u] = min(dist[v][u], w)
    print("Distance matrix before applying Floyd's Algorithm:")
    print(dist)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    print("Distance matrix after applying Floyd's Algorithm:")
    print(dist)
    return dist
def shortest_path(dist, start, end):
    return dist[start][end]
n = 5
edges = [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]]
distance_matrix = floyd_warshall(n, edges)
shortest_distance = shortest_path(distance_matrix, 2, 0)
print(f"Shortest path from C to A: {shortest_distance}")
test_edges = [[1, 0, 2], [0, 2, 3], [2, 3, 1], [3, 0, 6], [2, 1, 7]]
n_test = 4
distance_matrix_test = floyd_warshall(n_test, test_edges)
shortest_distance_test = shortest_path(distance_matrix_test, 2, 0)
print(f"Shortest path from C to A in test case: {shortest_distance_test}")
