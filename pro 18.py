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








