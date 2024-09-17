def is_hamiltonian_cycle(edges, n):
    from itertools import permutations
    graph = {i: [] for i in range(n)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    for perm in permutations(range(n)):
        if all(perm[i] in graph[perm[i - 1]] for i in range(n)):
            if perm[0] in graph[perm[-1]]:
                return True
    return False
edges = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2), (2, 4), (4, 0)]
n = 5
print(is_hamiltonian_cycle(edges, n))
