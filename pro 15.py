def is_hamiltonian_cycle(edges, n):
    from itertools import permutations

    # Create an adjacency list from the edges
    graph = {i: [] for i in range(n)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Check all permutations of vertices
    for perm in permutations(range(n)):
        # Check if the current permutation forms a Hamiltonian cycle
        if all(perm[i] in graph[perm[i - 1]] for i in range(n)) and perm[0] in graph[perm[-1]]:
            return True

    return False

# Example usage
edges = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2), (2, 4), (4, 0)]
n = 5
print(is_hamiltonian_cycle(edges, n)) 
