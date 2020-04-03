class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ind = list(range(len(t)))
        for i in s:
            ind[t.index(i)] = 0
            t = t.replace(i, '0', 1)
        return t[sum(ind)]