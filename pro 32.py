def subsets(S):
    S = sorted(set(S))  
    result = []
    def backtrack(start, path):
        result.append(path)
        for i in range(start, len(S)):
            backtrack(i + 1, path + [S[i]])
    backtrack(0, [])
    return result
A = [1, 2, 3]
print(subsets(A))
