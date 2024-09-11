# Word Wrap Problem

class WordFilter:

    def __init__(self, words):
        self.words = words
        self.prefix_map = {}
        self.suffix_map = {}
        
        for index, word in enumerate(words):
            for i in range(len(word) + 1):
                prefix = word[:i]
                if prefix not in self.prefix_map:
                    self.prefix_map[prefix] = []
                self.prefix_map[prefix].append(index)
                
            for j in range(len(word) + 1):
                suffix = word[j:]
                if suffix not in self.suffix_map:
                    self.suffix_map[suffix] = []
                self.suffix_map[suffix].append(index)

    def f(self, pref, suff):
        if pref in self.prefix_map and suff in self.suffix_map:
            prefix_indices = self.prefix_map[pref]
            suffix_indices = self.suffix_map[suff]
            valid_indices = set(prefix_indices) & set(suffix_indices)
            if valid_indices:
                return max(valid_indices)
        return -1
