from itertools import product
A = [1, 2]
B = [-2, -1]
C = [-1, 2]
D = [0, 2]
count = sum(1 for i, j, k, l in product(A, B, C, D) if i + j + k + l == 0)
print(count)
