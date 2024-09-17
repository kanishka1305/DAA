class WordFilter:
    def _init_(self, words):
        self.words = words
        self.prefix_suffix_map = {}
        
        for index, word in enumerate(words):
            for i in range(len(word) + 1):
                for j in range(len(word) + 1):
                    prefix = word[:i]
                    suffix = word[j:]
                    self.prefix_suffix_map[(prefix, suffix)] = index

    def f(self, pref, suff):
        return self.prefix_suffix_map.get((pref, suff), -1)
