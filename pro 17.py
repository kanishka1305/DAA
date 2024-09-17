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
