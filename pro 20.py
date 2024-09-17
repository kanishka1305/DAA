# Implementing Floyd's Algorithm to find the shortest path between all pairs of cities
def floyd_warshall(n, edges):
    # Initialize the distance matrix with infinity
    distance = [[float('inf')] * n for _ in range(n)]
    
    # Set the distance from each city to itself as 0
    for i in range(n):
        distance[i][i] = 0
    
    # Populate the distance matrix with the given edges
    for u, v, w in edges:
        distance[u][v] = w
        distance[v][u] = w  # Assuming undirected graph
    
    # Display the distance matrix before applying the algorithm
    print("Distance matrix before applying Floyd's Algorithm:")
    for row in distance:
        print(row)
    
    # Floyd's Algorithm to find shortest paths
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
    
    # Display the distance matrix after applying the algorithm
    print("\nDistance matrix after applying Floyd's Algorithm:")
    for row in distance:
        print(row)
    
    return distance

# Example usage
n = 5
edges = [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]]
distance_matrix = floyd_warshall(n, edges)

# Finding the shortest path from C (2) to A (0)
shortest_path = distance_matrix[2][0]
print(f"\nShortest path from C to A: {shortest_path}")

# Finding the shortest path from E (4) to C (2)
# Assuming E is represented as 4 in the distance matrix
shortest_path_E_to_C = distance_matrix[4][2]
print(f"Shortest path from E to C: {shortest_path_E_to_C}")
