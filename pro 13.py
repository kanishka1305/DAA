def generate_subsets(S):
    # Sort the input set to ensure lexicographical order
    S.sort()
    result = []
    
    def backtrack(start, path):
        # Append the current subset (path) to the result
        result.append(path)
        for i in range(start, len(S)):
            # Include the current element and move to the next
            backtrack(i + 1, path + [S[i]])
    
    backtrack(0, [])
    return result

# Example usage
A = [1, 2, 3]
subsets = generate_subsets(A)
print(subsets)  # Output: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
9
