def string_matching(words):
    result = []
    for i in range(len(words)):
        for j in range(len(words)):
            if i != j and words[j] in words[i]:
                result.append(words[j])
                break  
    return result
words1 = ["mass", "as", "hero", "superhero"]
print(string_matching(words1))  
words2 = ["leetcode", "et", "code"]
print(string_matching(words2))  words3 = ["blue", "green", "bu"]
print(string_matching(words3))  
