# Warshall’s & Floyd’s Algorithm

def floyd_warshall(n, edges, distanceThreshold):
    # Initialize the distance matrix
    dist = [[float('inf')] * n for _ in range(n)]
    
    for i in range(n):
        dist[i][i] = 0
        
    for fromi, toi, weight in edges:
        dist[fromi][toi] = min(dist[fromi][toi], weight)
        dist[toi][fromi] = min(dist[toi][fromi], weight)
    
    # Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist

def findTheCity(n, edges, distanceThreshold):
    dist = floyd_warshall(n, edges, distanceThreshold)
    city_count = [0] * n
    
    for i in range(n):
        for j in range(n):
            if dist[i][j] <= distanceThreshold:
                city_count[i] += 1
    
    min_count = float('inf')
    result_city = -1
    
    for i in range(n):
        if city_count[i] <= min_count:
            min_count = city_count[i]
            result_city = i
            
    return result_city

# Example usage
n = 4
edges = [[0, 1, 3], [1, 2, 1], [2, 3, 4], [0, 3, 5]]
distanceThreshold = 4
print(findTheCity(n, edges, distanceThreshold))
