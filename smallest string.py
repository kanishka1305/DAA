def smallestStringWithSwaps(s, pairs):
    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        root_x, root_y = find(x), find(y)
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_x] = root_y
            if rank[root_x] == rank[root_y]:
                rank[root_y] += 1

    parent = list(range(len(s)))
    rank = [0] * len(s)

    for a, b in pairs:
        union(a, b)

    groups = collections.defaultdict(list)
    for i, char in enumerate(s):
        groups[find(i)].append(char)

    for group in groups:
        groups[group].sort(reverse=True)

    result = []
    for i in range(len(s)):
        result.append(groups[find(i)].pop())

    return ''.join(result)

s = "dcab"
pairs = [[0, 3], [1, 2]]
print(smallestStringWithSwaps(s, pairs))  # Output: "bacd"
