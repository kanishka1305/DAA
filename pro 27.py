def findTheCity(n, edges, distanceThreshold):
    # Initialize the distance matrix with infinity
    dist = [[float('inf')] * n for _ in range(n)]
    
    # Set the distance from each city to itself as 0
    for i in range(n):
        dist[i][i] = 0
    
    # Populate the distance matrix with the given edges
    for u, v, w in edges:
        dist[u][v] = w
        dist[v][u] = w
    
    # Apply the Floyd-Warshall algorithm to find the shortest paths
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    # Count reachable cities within the distance threshold
    city_count = [0] * n
    for i in range(n):
        for j in range(n):
            if dist[i][j] <= distanceThreshold:
                city_count[i] += 1
    
    # Find the city with the smallest number of reachable cities
    # If there are ties, return the city with the greatest index
    min_city = float('inf')
    city_index = -1
    for i in range(n):
        if city_count[i] <= min_city:
            min_city = city_count[i]
            city_index = i
    
    return city_index
