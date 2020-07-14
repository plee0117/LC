class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        from collections import Counter
        c = Counter(words).most_common()
        c.sort(key = lambda x: x[0])
        c.sort(reverse = True, key = lambda x: x[1])
        return [x[0] for x in c][:k]