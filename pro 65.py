class OBST:
    def __init__(self, keys, freq):
        self.keys = keys
        self.freq = freq
        self.n = len(keys)
        self.cost = [[0] * (self.n + 1) for _ in range(self.n + 1)]
        self.root = [[0] * (self.n + 1) for _ in range(self.n + 1)]
    def construct_obst(self):
        for i in range(self.n):
            self.cost[i][i + 1] = self.freq[i]
        for length in range(2, self.n + 1):
            for i in range(self.n - length + 1):
                j = i + length
                self.cost[i][j] = float('inf')
                for r in range(i, j):
                    c = self.cost[i][r] + self.cost[r + 1][j] + self.sum_freq(i, j)
                    if c < self.cost[i][j]:
                        self.cost[i][j] = c
                        self.root[i][j] = r
    def sum_freq(self, i, j):
        return sum(self.freq[k] for k in range(i, j))
    def display_results(self):
        print("Cost Matrix:")
        for row in self.cost:
            print(row)
        print("\nRoot Matrix:")
        for row in self.root:
            print(row)
        print("\nTotal Cost:", self.cost[0][self.n])
keys = [10, 12, 16, 21]
frequencies = [4, 2, 6, 3]
obst = OBST(keys, frequencies)
obst.construct_obst()
obst.display_results()
