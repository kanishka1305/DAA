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
