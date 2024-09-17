def is_hamiltonian_cycle(edges, n):
    from itertools import permutations
    graph = {i: [] for i in range(n)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    for perm in permutations(range(n)):
        if all(perm[i] in graph[perm[i - 1]] for i in range(n)):
            return True
    return False
edges = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)]
n = 4
print(is_hamiltonian_cycle(edges, n))
