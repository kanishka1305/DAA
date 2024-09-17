def vertex_cover_approximation(n, m, edges):
    from collections import defaultdict
    graph = defaultdict(set)
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)
    vertex_cover = set()
    covered_edges = set()
    while covered_edges != set(edges):
        max_degree_vertex = max(graph, key=lambda x: len(graph[x]))
        vertex_cover.add(max_degree_vertex)
        for neighbor in graph[max_degree_vertex]:
            covered_edges.add((min(max_degree_vertex, neighbor), max(max_degree_vertex, neighbor)))
        del graph[max_degree_vertex]
    return list(vertex_cover)
n = 6
m = 7
edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 4), (3, 5), (4, 5)]
result = vertex_cover_approximation(n, m, edges)
print("Vertex Cover:", result)
