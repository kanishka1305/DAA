def word_break(s, word_dict):
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_dict:
                dp[i] = True
                break

    return dp[n]

# Example usage
dictionary = {"i", "like", "sam", "sung", "samsung", "mobile", "ice", "cream", "icecream", "man", "go", "mango"}
input_string1 = "ilike"
input_string2 = "ilikesamsung"

print("Input:", input_string1, "Output:", "Yes" if word_break(input_string1, dictionary) else "No")
print("Input:", input_string2, "Output:", "Yes" if word_break(input_string2, dictionary) else "No")
