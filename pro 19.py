# Function to check for Hamiltonian cycle in an undirected graph
def is_hamiltonian_cycle(edges, n):
    # Create an adjacency list from the edges
    from collections import defaultdict

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Helper function to perform backtracking
    def backtrack(path):
        if len(path) == n:
            # Check if the last vertex connects to the first
            return path[0] in graph[path[-1]]
        
        for neighbor in graph[path[-1]]:
            if neighbor not in path:
                path.append(neighbor)
                if backtrack(path):
                    return True
                path.pop()
        return False

    # Start the path with the first vertex
    for start in range(n):
        if backtrack([start]):
            return True
    return False

# Example usage
edges = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)]
n = 4
print(is_hamiltonian_cycle(edges, n))  # Output: True or False
9:32 am
def graph_coloring(edges, n):
    # Create an adjacency list from the edges
    adjacency_list = {i: [] for i in range(n)}
    for u, v in edges:
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)

    # Initialize colors for each vertex
    colors = [-1] * n

    # Function to check if the current color assignment is safe
    def is_safe(vertex, color):
        for neighbor in adjacency_list[vertex]:
            if colors[neighbor] == color:
                return False
        return True

    # Recursive function to assign colors to vertices
    def assign_colors(vertex):
        if vertex == n:
            return True  # All vertices are colored

        for color in range(n):  # Try different colors
            if is_safe(vertex, color):
                colors[vertex] = color
                if assign_colors(vertex + 1):
                    return True
                colors[vertex] = -1  # Backtrack

        return False

    assign_colors(0)
    return colors

# Example usage
edges = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)]
n = 4
result = graph_coloring(edges, n)
print("Color assignment for each vertex:", result)
9:34 am
def graph_coloring(edges, n, k):
    # Create an adjacency list
    graph = {i: [] for i in range(n)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Initialize color assignment
    color_assignment = [-1] * n

    def is_safe(node, color):
        for neighbor in graph[node]:
            if color_assignment[neighbor] == color:
                return False
        return True

    def color_graph(node):
        if node == n:
            return True
        
        for color in range(k):
            if is_safe(node, color):
                color_assignment[node] = color
                if color_graph(node + 1):
                    return True
                color_assignment[node] = -1  # Backtrack
        return False

    if color_graph(0):
        return color_assignment
    else:
        return None

# Example usage
edges = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)]
n = 4
k = 3
result = graph_coloring(edges, n, k)
print("Color assignment:", result)
9:34 am
def floyd_warshall(n, edges):
    # Initialize the distance matrix with infinity
    dist = [[float('inf')] * n for _ in range(n)]
    
    # Set the distance from each city to itself as 0
    for i in range(n):
        dist[i][i] = 0
    
    # Populate the distance matrix with the given edges
    for u, v, w in edges:
        dist[u][v] = min(dist[u][v], w)  # In case of multiple edges, take the minimum weight
        dist[v][u] = min(dist[v][u], w)  # For undirected graph
    
    # Display the initial distance matrix
    print("Initial distance matrix:")
    for row in dist:
        print(row)
    
    # Apply Floyd's Algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    # Display the distance matrix after applying the algorithm
    print("Distance matrix after applying Floyd's Algorithm:")
    for row in dist:
        print(row)
    
    return dist

# Example usage
n = 4
edges = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]]
distance_matrix = floyd_warshall(n, edges)

# Identify and print the shortest path from City 1 to City 3
shortest_path = distance_matrix[1][3]
print(f"Shortest path from City 1 to City 3 = {shortest_path}")
