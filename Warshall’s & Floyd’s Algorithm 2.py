# Warshall’s & Floyd’s Algorithm

def floyd_warshall(n, times, k):
    # Initialize the distance matrix
    inf = float('inf')
    dist = [[inf] * n for _ in range(n)]
    
    for u, v, w in times:
        dist[u - 1][v - 1] = min(dist[u - 1][v - 1], w)
    
    for i in range(n):
        dist[i][i] = 0
    
    # Floyd-Warshall algorithm
    for mid in range(n):
        for start in range(n):
            for end in range(n):
                if dist[start][mid] < inf and dist[mid][end] < inf:
                    dist[start][end] = min(dist[start][end], dist[start][mid] + dist[mid][end])
    
    # Calculate the maximum time from node k
    max_time = 0
    for i in range(n):
        if dist[k - 1][i] == inf:
            return -1
        max_time = max(max_time, dist[k - 1][i])
    
    return max_time
