class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import Counter
        group = [[]]
        for idx, word in enumerate(strs):
            if Counter(word) in group[0]:
                group[group[0].index(Counter(word)) + 1].append(word)
            else:
                group[0].append(Counter(word))
                group.append([word])
        return group[1:]