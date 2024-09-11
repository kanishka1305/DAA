# Brute-Force String Matching

def substring_words(words):
    result = []
    for i in range(len(words)):
        for j in range(len(words)):
            if i != j and words[i] in words[j]:
                result.append(words[i])
                break
    return list(set(result))

# Example usage
words = ["mass", "as", "hero", "superhero", "heroics"]
print(substring_words(words))
