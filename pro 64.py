class OptimalBinarySearchTree:
    def __init__(self, keys, freq):
        self.keys = keys
        self.freq = freq
        self.n = len(keys)
        self.cost = [[0] * self.n for _ in range(self.n)]
        self.root = [[0] * self.n for _ in range(self.n)]
    def construct_obst(self):
        for i in range(self.n):
            self.cost[i][i] = self.freq[i]
        for length in range(2, self.n + 1):
            for i in range(self.n - length + 1):
                j = i + length - 1
                self.cost[i][j] = float('inf')
                total_freq = sum(self.freq[k] for k in range(i, j + 1))
                for r in range(i, j + 1):
                    c = (self.cost[i][r - 1] if r > i else 0) + \
                        (self.cost[r + 1][j] if r < j else 0) + total_freq
                    if c < self.cost[i][j]:
                        self.cost[i][j] = c
                        self.root[i][j] = r
    def print_cost_and_root(self):
        print("Cost Matrix:")
        for row in self.cost:
            print(row)
        print("\nRoot Matrix:")
        for row in self.root:
            print(row)
keys = ['A', 'B', 'C', 'D']
frequencies = [0.1, 0.2, 0.4, 0.3]
obst = OptimalBinarySearchTree(keys, frequencies)
obst.construct_obst()
obst.print_cost_and_root()
print("\nOptimal Cost:", obst.cost[0][len(keys) - 1])
